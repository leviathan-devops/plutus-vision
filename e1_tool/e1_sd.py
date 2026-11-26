"""e1_sd.py - ENGINE 1, FIRE layer: the supply / demand zone map on 4H / 1H / 30m / 15m (coverage rows E1-S0f, E1-S0g, E1-MTF, GS-REF, GS-TAX).

Authority, in order:
- L-38 + the operator's notes (e1_tool/reference/Forex_SMC_Notes-1.txt :29-34, :128-150): "Look out for strong momentum moves ... Identify the candle before the strong move.
  Draw a box around the wicks of that previous candle"; a valid block needs "a gap between the before and after candles surrounding the inefficiency", "must create break of structure",
  and is "a one time use ... unmitigated".  L-37: no minimum move size.
- P452:637-745 (Step 0f): "the SINGULAR candle that immediately precedes a strong directional move"; "Locate the SINGLE candle immediately before that move began";
  zone = [Low, High] of that candle; BoM = origin of the move, continuation bases = MoM ("When in doubt, classify as MoM"); mitigation soft (wicks tap) / hard (bodies enter);
  noise rejection (wider than 0.40, stale > 3 weeks with no interaction).  P452:639 / :753 "2-4 candle base" / "2-3 candle base".
- GS Law 1 (zones from 15m + 30m + 1H + 4H stacked), GS Part 11 (zones of adjacent timeframes at the same level = ONE "Refined" zone, the narrower width, label "15m Refined 30m"),
  GS Part 7 labels: "<TF> (Unmitigated | Mitigated Nx) | BoM / MoM".  L-40: 4H = higher-timeframe overview, the work is on 1H.
Checked against the operator's own hand-drawn boxes of the golden week (context_management/oracle/golden_week.json): DXY 4, EURUSD 4, GBPUSD 4 - comparison only, no oracle number is used here.
No price literal: every threshold is a canon number in DXY points scaled to the pair (1.00 DXY point = 100 pips)."""
import e1_data as D

TFS = ('240', '60', '30', '15')
TFNAME = {'240': '4H', '60': '1H', '30': '30m', '15': '15m'}
SCAN_DAYS = 60            # P452:641 "last 60 calendar days"
STALE_DAYS = 21           # P452:743 "more than 3 weeks ago with no recent price interaction"


def _inside(x, m):
    return x['high'] <= m['high'] and x['low'] >= m['low']


def scan(pair, monday, tf):
    """every candle-before-the-move zone of one timeframe, with its history up to the anchor"""
    b0 = D.boundary_ms(monday)
    b = [x for x in D.closed(pair, tf, monday) if x['time'] >= b0 - SCAN_DAYS * 86400000]
    n = len(b)
    hi_f = [i for i in range(2, n - 2) if b[i]['high'] == max(x['high'] for x in b[i - 2:i + 3])]      # swing points: extreme of the bar and two bars each side (D-13)
    lo_f = [i for i in range(2, n - 2) if b[i]['low'] == min(x['low'] for x in b[i - 2:i + 3])]
    zones, i = [], 1
    while i < n - 1:
        down = b[i + 1]['high'] < b[i - 1]['low']        # inefficiency: the candles before and after candle i do not overlap (notes :136-138)
        up = b[i + 1]['low'] > b[i - 1]['high']
        if not (down or up):
            i += 1
            continue
        j = i
        while j < n - 1 and ((b[j + 1]['high'] < b[j - 1]['low']) if down else (b[j + 1]['low'] > b[j - 1]['high'])):
            j += 1                                       # consecutive inefficiency candles = one impulse
        o = i - 1
        # "the SINGLE candle immediately before that move BEGAN" (P452:649): large-bodied candles in the move's direction directly before the inefficiency belong to the move
        while o > 0:
            x = b[o]; rng = x['high'] - x['low']
            same = (x['close'] < x['open']) if down else (x['close'] > x['open'])
            if rng > 0 and same and abs(x['close'] - x['open']) / rng >= 0.5:
                o -= 1
            else:
                break
        # the base (P452:639 "2-4 candle base"): when the candle before the move sits inside an earlier candle of the base, the zone is that candle's wicks
        m, steps = o, 0
        while m > 0 and steps < 3 and _inside(b[m], b[m - 1]):       # an inside bar adds nothing to the base: the base candle is its mother
            m -= 1; steps += 1
        c = b[m]
        z = {'tf': tf, 'type': 'Supply' if down else 'Demand', 'bot': c['low'], 'top': c['high'], 'origin_time': c['time'],
             'origin': {k: c[k] for k in ('open', 'high', 'low', 'close')}, 'next': {k: b[m + 1][k] for k in ('open', 'high', 'low', 'close')},
             'end_time': b[j]['time'], 'width': c['high'] - c['low']}
        ext = min(x['low'] for x in b[i:j + 1]) if down else max(x['high'] for x in b[i:j + 1])
        z['move'] = abs((c['low'] if down else c['high']) - ext)
        # history after the impulse: visits (soft = wicks only, hard = a body enters, P452:713-730); a close beyond the far edge = the zone is broken (one-time use)
        soft = hard = 0; broken = None; last_in = c['time']; k = j + 1
        far = ext
        while k < n:
            x = b[k]
            if x['low'] <= z['top'] and x['high'] >= z['bot']:
                body = False
                while k < n and b[k]['low'] <= z['top'] and b[k]['high'] >= z['bot']:
                    x = b[k]
                    if z['bot'] <= min(x['open'], x['close']) and max(x['open'], x['close']) <= z['top']:
                        body = True                      # "Full candle bodies enter zone" (P452:717)
                    if broken is None and ((x['close'] > z['top']) if down else (x['close'] < z['bot'])):
                        broken = x['time']
                    last_in = x['time']; k += 1
                hard += 1 if body else 0; soft += 0 if body else 1
            else:
                if broken is None and ((x['close'] > z['top']) if down else (x['close'] < z['bot'])):
                    broken = x['time']
                if broken is None:
                    far = min(far, x['low']) if down else max(far, x['high'])
                k += 1
        z.update(soft=soft, hard=hard, mit=soft + hard, broken=broken, last_in=last_in, excursion=abs((c['low'] if down else c['high']) - far))
        # break of structure (notes :139): by the anchor the move away from the zone has taken out the last swing point that preceded it
        prior = [q for q in (lo_f if down else hi_f) if q < m]
        if prior:
            lvl = b[prior[-1]]['low'] if down else b[prior[-1]]['high']
            z['bos'] = (far < lvl) if down else (far > lvl); z['bos_level'] = lvl
        else:
            z['bos'] = True; z['bos_level'] = None
        zones.append(z)
        i = j + 1
    prev = None
    for z in zones:                                      # P452:694-697: the first zone of a leg = BoM, a continuation base in the same direction = MoM;
        z['kind'] = 'MoM' if prev == z['type'] else 'BoM'   # a candle whose move never broke structure is no block (notes :139) and does not end the leg
        if z['bos']:
            prev = z['type']
    return zones


def valid(z, spot, b0, U):
    """still a zone at the anchor: one-time use (no body has come back, never closed through), price on its own side, not stale, not wider than the canon limit, structure broken"""
    if z['broken'] is not None or z['hard'] > 0 or not z['bos']:
        return False
    if (spot <= z['top']) if z['type'] == 'Demand' else (spot >= z['bot']):
        return False
    if z['width'] > 0.40 * U:
        return False
    return z['last_in'] >= b0 - STALE_DAYS * 86400000           # b0 here = the start of the trading week: zones of the prior three weeks stand (P452:639 "prior 1-3 weeks")


def state(z):
    """GS Part 7 / P452:726-730: one soft tap ~ unmitigated"""
    return 'Unmitigated' if z['mit'] <= 1 and z['hard'] == 0 else f"Mitigated {z['mit']}x"


def zone_map(pair, monday):
    """the stacked map: valid zones of every timeframe; same-type overlaps on one timeframe reduced to the stronger zone; adjacent timeframes at the same level joined as 'Refined'"""
    U, pip = D.PIP[pair] * 100.0, D.PIP[pair]
    b0 = D.boundary_ms(monday)
    spot = D.closed(pair, '60', monday)[-1]['close']
    per = {}
    for tf in TFS:
        vs = [z for z in scan(pair, monday, tf) if valid(z, spot, D.week_start_ms(monday), U)]
        # Zone Type > Mitigation Level (P452:699-703): of two overlapping zones of one type on one timeframe the BoM stands, then the less mitigated, then the fresher
        vs.sort(key=lambda z: (z['kind'] != 'BoM', z['mit'], -z['origin_time']))
        keep = []
        for z in vs:
            o = next((q for q in keep if q['type'] == z['type'] and q['bot'] <= z['top'] and q['top'] >= z['bot']), None)
            if o is None:
                keep.append(z)
            else:
                o['reactions'] = o.get('reactions', 0) + 1          # an origin candle inside a standing zone is that zone reacting again (P533:1154-1161)
        per[tf] = keep
    out = []
    used = set()
    order = list(TFS)                                    # 4H, 1H, 30m, 15m
    for a in range(len(order) - 1, 0, -1):               # lower timeframe first: 15m with 30m, 30m with 1H, 1H with 4H
        lt, ht = order[a], order[a - 1]
        for z in per[lt]:
            if id(z) in used:
                continue
            for q in per[ht]:
                if id(q) in used or q['type'] != z['type']:
                    continue
                if abs(q['bot'] - z['bot']) <= 5 * pip and abs(q['top'] - z['top']) <= 5 * pip:      # GS Part 11: the same zone seen on two timeframes
                    n_ = z if z['width'] <= q['width'] else q
                    fresh = z if z['origin_time'] >= q['origin_time'] else q
                    r = dict(n_); r.update(tf=ht, refined=f"{TFNAME[lt]} Refined {TFNAME[ht]}", kind='BoM' if 'BoM' in (z['kind'], q['kind']) else 'MoM',
                                           soft=fresh['soft'], hard=fresh['hard'], mit=fresh['mit'], origin_time=min(z['origin_time'], q['origin_time']))
                    out.append(r); used.add(id(z)); used.add(id(q))
                    break
    for tf in TFS:
        out += [z for z in per[tf] if id(z) not in used]
    for z in out:
        z['label'] = f"{TFNAME[z['tf']]} ({state(z)}) | {z['kind']}"
        z['nested_in'] = next((TFNAME[q['tf']] for q in out if q is not z and q['type'] == z['type'] and TFS.index(q['tf']) < TFS.index(z['tf'])
                               and q['bot'] <= z['bot'] and q['top'] >= z['top']), None)
    out.sort(key=lambda z: -z['top'])
    return {'zones': out, 'spot': spot, 'U': U}


if __name__ == '__main__':
    import sys, datetime as dt
    monday, pair = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'DXY'
    M = zone_map(pair, monday)
    f = '%.3f' if pair == 'DXY' else '%.5f'
    print(f"{pair} {monday} spot {f % M['spot']} | {len(M['zones'])} zones")
    for z in M['zones']:
        t = dt.datetime.fromtimestamp(z['origin_time'] / 1000, dt.UTC).strftime('%m-%d %H:%M')
        print(f"  {z['label']:<32} {z['type']:<6} {f % z['bot']}-{f % z['top']} w {z['width'] / D.PIP[pair]:5.1f} from {t} move {z['move'] / D.PIP[pair]:6.1f} soft {z['soft']} "
              f"{z.get('refined') or ''}{' nested in ' + z['nested_in'] if z['nested_in'] else ''}")
