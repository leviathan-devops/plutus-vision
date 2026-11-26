"""e1_ip.py - ENGINE 1, the prompt's side of the coin: the INSTITUTIONAL PRESSURE ZONE MAP (P533 Protocol B :922-1539; v4.5.2 text where 5.3.3 says unchanged, L-33).
Assembly, scoring, zone mechanics, Pillar 9 typing, naming and ranking follow the APPROVED-RENDER RECIPE (handover 02_SUPERSEDED_READ_ONLY/e1_run.py :522-575, :590-680, :742-874;
the operator's verdict on its render: "THESE 6 ARE CORRECT ... 3 4 AND 5 NEED REFINEMENT" = narrower), with the operator's later rulings:
L-37 / L-38 (4H supply/demand = the candle before the strong move, wick to wick, no minimum size -> e1_pillars.step0f), L-35 (ZFP shown as the type's range), tight band for "too wide" (canon TIGHT CONFLUENCE 0.10).
All thresholds are the canon's DXY-point numbers scaled to the pair (1.00 DXY point = 100 pips). No price literal."""
import datetime as dt, math
import e1_data as D, e1_pillars as P, e1_sd as SD

MA_WEIGHT = {200: 3.0, 100: 2.0, 50: 1.5, 20: 1.0, 10: 0.5, 9: 0.5}            # P533:1078-1084
DEGREES = ((12, 'EXTREME'), (10, 'HEAVY'), (8, 'MODERATE-HEAVY'), (6, 'MODERATE'), (4, 'LIGHT'), (0, 'MINIMAL'))    # P533:1487-1494
ZFP_RANGE = {'Hard Wall': '5-15%', 'Standard Wall': '15-30%', 'Soft Wall': '30-50%', 'One-Touch': '50-70%', 'Post-Expiry Ghost': '20-40%'}   # P452:964-972 (L-35)
MAX_DRAWN = 6                                                                  # operator: "six zones at most"
W_EUR = -0.576


def _ema(v, n):
    if len(v) < n:
        return None
    k, e = 2.0 / (n + 1), sum(v[:n]) / n
    out = [None] * (n - 1) + [e]
    for x in v[n:]:
        e += (x - e) * k
        out.append(e)
    return out


def levels(pair, monday, side):
    """every level of every pillar as {p, pillar, kind, ...} + the structures needed later"""
    U = D.PIP[pair] * 100.0
    b1, b4 = D.closed(pair, '60', monday), D.closed(pair, '240', monday)
    daily, weekly = D.daily(pair, monday), D.weekly(pair, monday)
    spot = b1[-1]['close']
    L = []
    # ── Pillar 1 (P533:967-1064; recipe :162-186): weekly + last 3 daily sets seed; historical weeks overlapping the current range are legacy support
    pw = weekly[-1]
    def add_piv(label, H, Lo, C, legacy=False):
        pv = P.pivots(H, Lo, C)
        for var in ('classic', 'fib', 'camarilla'):
            for k, v in pv[var].items():
                L.append({'p': v, 'pillar': 1, 'kind': f'pivot {label} {var} {k}', 'legacy': legacy, 'seed': not legacy})
    add_piv('weekly', pw['high'], pw['low'], pw['close'])
    for d in daily[-3:]:
        add_piv('daily ' + d['date'][5:], d['high'], d['low'], d['close'])
    for w in weekly[-18:-1]:
        if w['low'] <= pw['high'] and w['high'] >= pw['low']:
            add_piv('historical week ' + w['monday'], w['high'], w['low'], w['close'], legacy=True)
    # ── Pillar 2 (P533:1065-1091; recipe :190-230): EMA+SMA on 1H / 4H / D1 / W1, clustered within 0.15, one level per cluster
    mas = []
    for tf, vals in (('1H', [b['close'] for b in b1]), ('4H', [b['close'] for b in b4]), ('D1', [d['close'] for d in daily]), ('W1', [w['close'] for w in weekly])):
        for n in (9, 10, 20, 50, 100, 200):
            e = _ema(vals, n)
            if e is None:
                continue
            mas.append({'p': e[-1], 'n': n, 'kind': f'EMA{n} {tf}'}); mas.append({'p': sum(vals[-n:]) / n, 'n': n, 'kind': f'SMA{n} {tf}'})
    mas.sort(key=lambda m: m['p'])
    cl, cur = [], [mas[0]]
    for m in mas[1:]:
        if m['p'] - cur[0]['p'] <= 0.15 * U:
            cur.append(m)
        else:
            cl.append(cur); cur = [m]
    cl.append(cur)
    closes = [d['close'] for d in daily]
    recap = []
    for n in (50, 100, 200):
        e = _ema(closes, n)
        if e and any(e[i] is not None and e[i - 1] is not None and (closes[i - 1] - e[i - 1]) * (closes[i] - e[i]) < 0 for i in range(len(closes) - 3, len(closes))):
            recap.append(e[-1])
    for c in cl:
        ws = sum(MA_WEIGHT[m['n']] for m in c)
        p = sum(m['p'] * MA_WEIGHT[m['n']] for m in c) / ws
        L.append({'p': p, 'pillar': 2, 'kind': f"MA {'TRIPLE+' if len(c) >= 3 else 'DOUBLE' if len(c) == 2 else 'SINGLE'} [{', '.join(m['kind'] for m in c)}]",
                  'pts': 2 if len(c) >= 3 else 1 if len(c) == 2 else 0.5, 'recapture': any(abs(p - r) <= 0.10 * U for r in recap)})
    # ── Pillars 3 / 8 (P533:1092-1144, 1436-1454; recipe :234-280): K anchored on the boundary spots; tiers by USD notional
    eur = D.closed('EURUSD', '60', monday)[-1]['close']
    # K from the five other component rates (canon formula P533:928-952; the Apr 20 report's K 108.0806 is built this way and is NOT anchored on the index -
    # its own reverse check differs from spot). Rates = the latest Fed H.10 before the anchor (sidecar). The recipe's index-anchored K moved the 1.1400 wall 9 pips: rejected.
    K = P.k_factor(side['h10']['rates']) if pair == 'DXY' else None
    t3 = []
    for e in side['expiries'].get('EURUSD' if pair == 'DXY' else pair, []):
        fx = eur if e.get('ccy', 'EUR') == 'EUR' else D.closed('GBPUSD', '60', monday)[-1]['close'] if e.get('ccy') == 'GBP' else 1.0
        usd = e['notional_m'] / 1000.0 * fx
        t = 1 if e['notional_m'] >= 1500 else 2 if e['notional_m'] >= 850 else 3      # P533:1443-1447: thresholds are stated on the EUR/USD expiry notional (EUR), bands +-0.07 / 0.10 / 0.15
        p = K * e['strike'] ** W_EUR if pair == 'DXY' else e['strike']
        lv = {'p': p, 'pillar': 8, 'kind': f"{'EUR/USD ' if pair == 'DXY' else ''}{e['strike']:.4f} {e['notional_m']}M {e.get('cut_date', '')[5:]} (Tier {t})", 'tier': t, 'usd': usd,
              'band': {1: 0.07, 2: 0.10, 3: 0.15}[t] * U, 'expired': e.get('state') == 'ghost', 'strike': e['strike'], 'notional_m': e['notional_m'], 'cut': e.get('cut_date', '')}
        (L if t < 3 else t3).append(lv)
    # ── Pillar 5 (P533:1205-1423; recipe :304-477)
    win = daily[-90:]
    sess = D.forming(pair, monday)                               # the D1 bar in progress at the anchor (D-25): data available at Monday London open (L-05)
    lows, highs = [], []
    # Step 0b / 0c (P533:1217-1228): swing lows / highs with a rejection wick >= 0.15 and the close in the upper / lower 50% of the daily range.
    # A swing = the extreme of its bar and of the two bars each side THAT EXIST at the anchor (D-13): the text gives no neighbour count, and the reference report (Apr 20-24, section 5)
    # lists the low of Apr 17 - the last day before its boundary - as "D1 swing low ... Liquidity Sweep Target". The last days and the bar in progress are therefore scanned too.
    d1 = win + ([sess] if sess else [])
    for i in range(2, len(d1)):
        d = d1[i]; rng = d['high'] - d['low']
        if rng <= 0:
            continue
        cpos = (d['close'] - d['low']) / rng
        blo, bhi = min(d['open'], d['close']), max(d['open'], d['close'])
        nb = d1[i - 2:i] + d1[i + 1:i + 3]
        if d['low'] < min(x['low'] for x in nb) and blo - d['low'] >= 0.15 * U and cpos >= 0.5:
            lows.append({'p': d['low'], 'date': d['date'], 'wick': blo - d['low']})
        if d['high'] > max(x['high'] for x in nb) and d['high'] - bhi >= 0.15 * U and cpos <= 0.5:
            highs.append({'p': d['high'], 'date': d['date'], 'wick': d['high'] - bhi})
    obs = []                                                     # Step 0d: D1 order blocks
    for i in range(3, len(win) - 13):
        for size in (3, 2, 1):
            base, after = win[i:i + size], win[i + size:i + size + 10]
            rngs = [d['high'] - d['low'] for d in base]
            if len(after) < 10 or min(rngs) <= 0:
                continue
            bull = all(d['close'] > d['open'] and (d['close'] - d['open']) / r >= 0.5 for d, r in zip(base, rngs))
            bear = all(d['close'] < d['open'] and (d['open'] - d['close']) / r >= 0.5 for d, r in zip(base, rngs))
            lo, hi = min(d['low'] for d in base), max(d['high'] for d in base)
            if bull and lo <= min(d['low'] for d in win[i - 3:i]) and max(d['high'] for d in after[:5]) >= hi + 1.0 * U and min(d['low'] for d in after[:5]) > lo:
                obs.append({'kind': 'Demand', 'top': hi, 'bottom': lo, 'date': base[0]['date']}); break
            if bear and hi >= max(d['high'] for d in win[i - 3:i]) and min(d['low'] for d in after[:5]) <= lo - 1.0 * U and max(d['high'] for d in after[:5]) < hi:
                obs.append({'kind': 'Supply', 'top': hi, 'bottom': lo, 'date': base[0]['date']}); break
    for sd, arr in (('low', lows), ('high', highs)):
        for x in arr:
            conf = any(o['kind'] == ('Demand' if sd == 'low' else 'Supply') and o['bottom'] <= x['p'] <= o['top'] for o in obs)
            L.append({'p': x['p'], 'pillar': 5, 'kind': ('Liquidity Sweep Target' if sd == 'low' else 'Supply Ceiling Target') + f" (D1 swing {sd} {x['date'][5:]})" + (' CONFLUENT' if conf else ''),
                      'struct': 2, 'bonus': 2.0 if conf else 1.0, 'confluent': conf, 'extreme': True})
    lsz = [{'bot': x['p'], 'top': x['p'] + 0.10 * U, 'side': 'Demand-side', 'level': x['p'], 'source': 'D1 swing low ' + x['date']} for x in lows] + \
          [{'bot': x['p'] - 0.10 * U, 'top': x['p'], 'side': 'Supply-side', 'level': x['p'], 'source': 'D1 swing high ' + x['date']} for x in highs]
    # Step 0.45 "ALL prior swing lows / highs where stops would cluster": the reference report (Apr 20-24) lists the low / high of each recent day of the prior week as a sweep zone
    # (97.63 Apr 17, 97.83 Apr 16, 97.97 Apr 14 ...), so the daily extremes of the last 5 completed days are sweep-zone sources too; 0.45a: extended 0.05-0.10 beyond the 0.05 base.
    for d in daily[-5:] + ([sess] if sess else []):
        if not any(abs(z['level'] - d['low']) < 1e-9 for z in lsz):
            lsz.append({'bot': d['low'], 'top': d['low'] + 0.10 * U, 'side': 'Demand-side', 'level': d['low'], 'source': 'daily low ' + d['date']})
        if not any(abs(z['level'] - d['high']) < 1e-9 for z in lsz):
            lsz.append({'bot': d['high'] - 0.10 * U, 'top': d['high'], 'side': 'Supply-side', 'level': d['high'], 'source': 'daily high ' + d['date']})
    for z in lsz:
        later = [x for x in daily if x['date'] > z['source'][-10:]]      # completed sessions only: the map is the weekend map (the operator's bands are drawn before Monday's first hours)
        z['swept'] = any((x['low'] < z['level']) if z['side'] == 'Demand-side' else (x['high'] > z['level']) for x in later)
        z['priority'] = 'ACTIVE SL TRIGGER' if abs(z['level'] - spot) <= 0.30 * U else 'STANDARD'
    magnets = []
    for sd, arr in (('low', lows), ('high', highs)):
        used = set()
        for a in range(len(arr)):
            if a in used:
                continue
            grp = [b for b in range(a, len(arr)) if b not in used and abs(arr[b]['p'] - arr[a]['p']) <= 0.05 * U]
            if len(grp) >= 2:
                used.update(grp); ws = sum(arr[b]['wick'] for b in grp)
                magnets.append({'p': sum(arr[b]['p'] * arr[b]['wick'] for b in grp) / ws, 'n': len(grp), 'role': sd, 'kind': 'Repeated ' + ('Low' if sd == 'low' else 'High') + ' Magnet'})
    for lo in lows:
        for hi in highs:
            if abs(lo['p'] - hi['p']) <= 0.05 * U:
                magnets.append({'p': lo['p'], 'n': 2, 'role': 'reversal', 'kind': 'Role Reversal Magnet'})
    for m in magnets:
        inst = any(o['bottom'] <= m['p'] <= o['top'] for o in obs)
        L.append({'p': m['p'], 'pillar': 5, 'kind': m['kind'] + f" ({m['n']}x)" + (' INSTITUTIONAL MAGNET' if inst else ''), 'struct': 2,
                  'bonus': 2.0 if (m['n'] >= 3 or m['role'] == 'reversal' or inst) else 1.5, 'extreme': True})
    # Step 0f 4H supply/demand (L-37, L-38; e1_sd: candle before the move, one-time use, structure break, noise rejection P452:741-745): edges are structural levels (weight 1)
    b0 = D.boundary_ms(monday)
    sd = SD.zone_map(pair, monday)['zones']
    z4 = [z for z in sd if z['tf'] == '240']
    for z in z4:
        lab = f"{z['kind']} {z['mit']}X 4H {z['type']} Zone"
        L.append({'p': z['top'], 'pillar': 5, 'kind': lab + ' (top edge)', 'struct': 1, 'z4': z}); L.append({'p': z['bot'], 'pillar': 5, 'kind': lab + ' (bottom edge)', 'struct': 1, 'z4': z})
    for tf, arr in (('D1', win), ('4H', [x for x in b4 if x['time'] >= b0 - 60 * 86400000])):     # Step 0h minor swings
        for i in range(2, len(arr) - 2):
            d = arr[i]; rng = d['high'] - d['low']
            if rng <= 0:
                continue
            cpos = (d['close'] - d['low']) / rng; nb = arr[i - 2:i] + arr[i + 1:i + 3]
            if d['low'] < min(x['low'] for x in nb) and min(d['open'], d['close']) - d['low'] >= 0.08 * U and cpos >= 0.4 and not any(abs(l['p'] - d['low']) < 1e-9 for l in lows):
                L.append({'p': d['low'], 'pillar': 5, 'kind': f'Minor Swing Level ({tf} low)', 'struct': 0.5})
            if d['high'] > max(x['high'] for x in nb) and d['high'] - max(d['open'], d['close']) >= 0.08 * U and cpos <= 0.6 and not any(abs(h['p'] - d['high']) < 1e-9 for h in highs):
                L.append({'p': d['high'], 'pillar': 5, 'kind': f'Minor Swing Level ({tf} high)', 'struct': 0.5})
    for d in daily[-5:]:                                         # Steps 1-5 anchors (P452:785-833)
        for k in ('close', 'high', 'low'):
            L.append({'p': d[k], 'pillar': 5, 'kind': f"Prior daily {k} {d['date'][5:]}", 'struct': 2, 'anchor': True})
    for k in ('close', 'high', 'low'):
        L.append({'p': pw[k], 'pillar': 5, 'kind': f'Prior weekly {k}', 'struct': 2, 'anchor': True})
    if sess:                                                     # "daily high / low" of the D1 bar in progress at the anchor (D-25); its close is spot, not a close
        for k in ('high', 'low'):
            L.append({'p': sess[k], 'pillar': 5, 'kind': f"Session {k} {sess['date'][5:]} (to the anchor)", 'struct': 2, 'anchor': True})
    # ── Pillar 6 (P452:835-862; recipe :485-510)
    for rr in (0.236, 0.382, 0.5, 0.618):
        L.append({'p': pw['high'] - rr * (pw['high'] - pw['low']), 'pillar': 6, 'kind': f'Fib {rr * 100:.1f}% of prior week'})
    d63 = daily[-63:]
    hi, lo = max(d63, key=lambda d: d['high']), min(d63, key=lambda d: d['low'])
    if lo['date'] < hi['date']:
        sh, sl = hi['high'], min(d['low'] for d in d63 if d['date'] <= hi['date'])
    else:
        sh, sl = max(d['high'] for d in d63 if d['date'] <= lo['date']), lo['low']
    for rr in (0.236, 0.382, 0.5, 0.618):
        L.append({'p': sh - rr * (sh - sl), 'pillar': 6, 'kind': f'Fib {rr * 100:.1f}% of major swing'})
    p5 = [l['p'] for l in L if l['pillar'] == 5]
    q, x = 0.25 * U, math.floor((min(p5) - 0.5 * U) / (0.25 * U))
    while x * q <= max(p5) + 0.5 * U:
        L.append({'p': round(x * q, 6), 'pillar': 6, 'kind': 'Round number ' + ('big figure' if x % 4 == 0 else 'half figure' if x % 2 == 0 else 'quarter figure'), 'round': True}); x += 1
    return {'L': L, 't3': t3, 'spot': spot, 'K': K, 'U': U, 'daily': daily, 'weekly': weekly, 'b4': b4, 'lsz': lsz, 'z4': z4, 'sd': sd, 'obs': obs, 'magnets': magnets, 'lows': lows, 'highs': highs}


def round_psych(p, U):
    f = (p / U) - math.floor(p / U)
    for target, pts in ((0.0, 2), (0.5, 2), (0.25, 1), (0.75, 1)):
        if min(abs(f - target), abs(f - target + 1.0), abs(f - target - 1.0)) <= 0.03 + 1e-9:
            return pts
    return 0


def score(p, by, U):
    """recipe :522-575 = the confluence table P533:1467-1485 applied to a candidate price"""
    EX, ZN = 0.03 * U, 0.10 * U
    near = lambda l, tol: abs(l['p'] - p) <= tol + 1e-12
    tech = opt = anal = struct = bonus = tally = 0.0
    pillars, members, legacy = set(), [], False
    for l in by.get(1, []):
        if near(l, ZN):
            if l.get('legacy'):
                legacy = legacy or near(l, EX); continue
            pillars.add(1); tech = max(tech, 2.0 if near(l, EX) else 1.0); members.append(l)
    if legacy:
        tech = min(2.0, tech + 0.5); pillars.add(1)
    for l in by.get(2, []):
        if near(l, ZN):
            pillars.add(2); tech = max(tech, l['pts']); tally += 2.0 if l.get('recapture') else 0.0; members.append(l)
    # Options-Derived (P533:1470): 2 = the level is a Critical Option Wall (>= 1.5B), 1 = a Significant Magnet; "is" = inside the strike's own confidence band (+-0.07 / +-0.10, P533:1443-1447)
    for l in by.get(8, []):
        if near(l, l['band']):
            pillars.add(8); opt = max(opt, 2 if l['tier'] == 1 else 1); tally = max(tally, {1: 3.0, 2: 2.0, 3: 1.0}[l['tier']]); members.append(l)
    # Structural (P533:1472): 2 = exact price anchor + structural extreme (both within 3 pips); 1 = proximity (10 pips) to an anchor or a structural extreme; 4H zone edge 1, minor swing 0.5 (U-10)
    anc_ex = ext_ex = False
    for l in by.get(5, []):
        if near(l, ZN):
            pillars.add(5); members.append(l)
            anc_ex = anc_ex or (l.get('anchor') and near(l, EX)); ext_ex = ext_ex or (l.get('extreme') and near(l, EX))
            struct = max(struct, 1.0 if (l.get('anchor') or l.get('extreme')) else l['struct'])
            if l.get('extreme') and near(l, EX):
                bonus = max(bonus, l.get('bonus', 0.0))          # the bonus belongs to levels WITH verified structural-extreme status (P533:1476-1484)
    if anc_ex and ext_ex:
        struct = 2.0
    ps = round_psych(p, U)
    for l in by.get(6, []):
        if near(l, ZN):
            pillars.add(6)
            if not l.get('round'):
                tech = max(tech, 1.0)
            members.append(l)
    if ps:
        pillars.add(6)
    return {'tech': min(tech, 2.0), 'opt': opt, 'anal': anal, 'struct': min(struct, 2.0), 'psych': ps, 'bonus': min(bonus, 2.0), 'tally': tally, 'pillars': pillars, 'members': members}


def mechanics(z, b4, trend, extremes, zones, spot, U):
    """recipe :590-656 = P533:1145-1161 (BoM/MoM, reaction counter), Engine 3 status, ladder step; measured on the 4H bars of the last 90 days"""
    b, t = z['bot'], z['top']
    support = (t + b) / 2.0 < spot
    visits, i, n = [], 0, len(b4)
    while i < n:
        if b4[i]['low'] <= t and b4[i]['high'] >= b:
            j = i
            while j + 1 < n and b4[j + 1]['low'] <= t and b4[j + 1]['high'] >= b:
                j += 1
            visits.append((i, j)); i = j + 1
        else:
            i += 1
    kinds = [m['kind'] for m in z['members_lv']]
    bom_4h = any(k.startswith('BoM') and '4H' in k for k in kinds)
    mom_4h = any(k.startswith('MoM') and '4H' in k for k in kinds) and not bom_4h
    origin = bom_4h or any(k.startswith('Liquidity Sweep Target') or k.startswith('Supply Ceiling Target') for k in kinds)
    m = {'role': 'support' if support else 'resistance', 'visits': len(visits), 'mom_4h': mom_4h}
    if not visits:
        m.update(reactions=0, counter='Virgin', bom='BoM' if origin else 'MoM', sweep='Unswept', last_excursion=0.0, post_consolidation=False)
    else:
        after = b4[visits[0][1] + 1:]
        sweep = ('Swept' if any(x['low'] < b for x in after) else 'Partial' if any(x['low'] <= t for x in after) else 'Unswept') if support else \
                ('Swept' if any(x['high'] > t for x in after) else 'Partial' if any(x['high'] >= b for x in after) else 'Unswept')
        reactions, last_out = 0, 0.0
        for k, (s, e) in enumerate(visits):
            seg = b4[e + 1:(visits[k + 1][0] if k + 1 < len(visits) else n)]
            if not seg:
                continue
            up, dn = max(x['high'] for x in seg) - t, b - min(x['low'] for x in seg)
            reactions += 1 if ((support and up >= 0.5 * U) or (not support and dn >= 0.5 * U)) else 0
            if k == len(visits) - 1:
                last_out = up if support else dn
        o = visits[0][0]
        pre = (max(x['high'] for x in b4[o - 12:o]) - min(x['low'] for x in b4[o - 12:o])) if o >= 12 else None
        m.update(reactions=reactions, counter='Depleted' if reactions >= 3 else 'Active' if reactions >= 1 else 'Virgin', bom='BoM' if last_out >= 1.0 * U else 'MoM',
                 sweep=sweep, last_excursion=last_out, post_consolidation=pre is not None and pre <= 0.50 * U)
    aligned = (trend == 'up' and support) or (trend == 'down' and not support)
    far_lo, far_hi = (b - 0.25 * U, b) if support else (t, t + 0.25 * U)
    opposing = any(far_lo <= x <= far_hi for x in extremes) or any(q is not z and q['bot'] <= far_hi and q['top'] >= far_lo for q in zones)
    sr = any(l['pillar'] in (1, 4, 6) for l in z['members_lv'])
    ex = {'a': m['reactions'] >= 1, 'b': aligned, 'c': sr, 'd': not opposing}
    if m['bom'] == 'BoM':
        status = 'TP-TARGET' if m['reactions'] >= 3 else 'ENTRY-PRIMARY'
    elif m['reactions'] == 0 or m['reactions'] >= 3:
        status = 'REJECT'
    else:
        status = 'ENTRY-CONDITIONAL' if all(ex.values()) else 'TP-TARGET'
    if mom_4h and status != 'REJECT':
        status = 'ENTRY-SCALP-ONLY'
    m.update(e3_status=status, mom_exceptions=ex, ladder_step=(m['bom'] == 'MoM' and aligned and 1 <= m['reactions'] <= 2 and status != 'REJECT'))
    return m


def intra_zone(z, X, U):
    """Step 0.6 (P533:1312-1340): micro-levels inside a MODERATE+ zone - 1H supply/demand zones of the prior weeks inside it, fib 0.382 / 0.618 of the zone's own range,
    prior daily closes inside, round numbers inside; tagged Precision Floor (bottom 40%) / Precision Ceiling (top 40%) / Mid-Anchor (middle 20%); Structural 0.5"""
    b, t = z['bot'], z['top']
    out = []
    for q in X['sd']:
        if q['tf'] == '60' and b <= q['bot'] and q['top'] <= t:
            out.append({'p': q['bot'], 'source': f"1H {q['type']} zone (bottom)"}); out.append({'p': q['top'], 'source': f"1H {q['type']} zone (top)"})
    for rr in (0.382, 0.618):
        out.append({'p': b + rr * (t - b), 'source': f'Fib {rr} of the zone'})
    for d in X['daily'][-10:]:
        if b <= d['close'] <= t:
            out.append({'p': d['close'], 'source': 'Prior close ' + d['date'][5:]})
    q, x = 0.25 * U, math.ceil(b / (0.25 * U) - 1e-9)
    while x * q <= t + 1e-9:
        out.append({'p': round(x * q, 6), 'source': 'Round number'}); x += 1
    for l in out:
        f = (l['p'] - b) / (t - b) if t > b else 0.5
        l['tag'] = 'Intra-Zone Precision Floor' if f <= 0.4 else 'Intra-Zone Precision Ceiling' if f >= 0.6 else 'Intra-Zone Mid-Anchor'
    return sorted(out, key=lambda l: -l['p'])


def build(pair, monday, side):
    X = levels(pair, monday, side)
    L, U, spot, daily = X['L'], X['U'], X['spot'], X['daily']
    by = {}
    for l in L:
        by.setdefault(l['pillar'], []).append(l)
    seeds = sorted({l['p'] for l in L if l.get('seed', True)})
    for l in X['t3']:                                            # Step 9.8: a sub-threshold strike counts only with the structural override
        s0 = score(l['p'], {k: v for k, v in by.items() if k != 8}, U)
        if len(s0['pillars'] | {8}) >= 3 and any(abs(x['p'] - l['p']) <= 0.10 * U for x in by.get(5, []) if 'bonus' in x):
            by.setdefault(8, []).append(l); seeds.append(l['p'])
    scored = {}
    for p in sorted(set(seeds)):
        s = score(p, by, U)
        scored[p] = {'p': p, 'base': round(s['tech'] + s['opt'] + s['anal'] + s['struct'] + s['psych'] + s['bonus'], 1), 'dims': {k: s[k] for k in ('tech', 'opt', 'anal', 'struct', 'psych', 'bonus')},
                     'tally': s['tally'], 'pillars': sorted(s['pillars']), 'members': s['members']}
    # ASSEMBLY (recipe :760-773; P533:1496-1501): best level first, centres at least 0.15 apart; the zone = the TIGHT confluence around its best level (0.10; operator: narrower)
    SEP, HALF = 0.15 * U, 0.05 * U
    zones = []
    for c in sorted(scored.values(), key=lambda c: (-c['base'], -len(c['pillars']), -c['tally'], abs(c['p'] - spot))):
        if c['base'] < 4:
            break
        if any(abs(c['p'] - z['seed']['p']) < SEP - 1e-12 for z in zones):
            continue
        mem = [m for m in scored.values() if abs(m['p'] - c['p']) <= HALF + 1e-12]
        lv = [l for l in L if abs(l['p'] - c['p']) <= HALF + 1e-12]
        zones.append({'bot': min(min(m['p'] for m in mem), c['p'] - 0.03 * U), 'top': max(max(m['p'] for m in mem), c['p'] + 0.03 * U), 'seed': c, 'n': len(mem), 'members_lv': lv})
    closes = [d['close'] for d in daily]
    e50, e200 = _ema(closes, 50), _ema(closes, 200)
    trend = 'range' if not (e50 and e200) else 'up' if closes[-1] > e50[-1] > e200[-1] else 'down' if closes[-1] < e50[-1] < e200[-1] else 'range'
    b0 = D.boundary_ms(monday)
    b4 = [x for x in X['b4'] if x['time'] >= b0 - 90 * 86400000]
    extremes = [l['p'] for l in by.get(5, []) if 'bonus' in l]
    mom3 = closes[-1] - closes[-4]
    reach = (max(d['high'] for d in daily[-5:]) - min(d['low'] for d in daily[-5:])) / 2
    cross200 = bool(e200) and any(e200[i] is not None and e200[i - 1] is not None and (closes[i - 1] - e200[i - 1]) * (closes[i] - e200[i]) < 0 for i in range(len(closes) - 5, len(closes)))
    cross_up = cross200 and closes[-1] > e200[-1]                # the side the regime changed to
    mags = [m['p'] for m in X['magnets']]
    for z in zones:
        z['mech'] = mechanics(z, b4, trend, extremes, zones, spot, U)
        seed, npill = z['seed'], len(z['seed']['pillars'])
        opts = [l for l in z['members_lv'] if l['pillar'] == 8]
        wall = max([l['usd'] for l in opts] + [0.0]); live = any(not l.get('expired') for l in opts)
        confluent = any(l.get('confluent') for l in z['members_lv'])
        if live and wall >= 1.0 and npill >= 3 and confluent:
            ztype, base_z = 'Hard Wall', 10
        elif live and wall >= 0.5 and npill >= 2:
            ztype, base_z = 'Standard Wall', 22
        elif wall >= 0.85:
            ztype, base_z = 'Post-Expiry Ghost', {4: 20, 3: 30}.get(min(npill, 4), 40)
        elif npill >= 3:
            ztype, base_z = 'Soft Wall', 30
        elif npill == 2 or wall > 0:
            ztype, base_z = 'Soft Wall', 40
        else:
            ztype, base_z = 'One-Touch', 60
        near_spot = (z['bot'] <= spot <= z['top']) or min(abs(z['top'] - spot), abs(z['bot'] - spot)) <= reach
        above = z['bot'] > spot
        mods = []
        if near_spot and ((above and mom3 >= 0.3 * U) or (z['top'] < spot and mom3 <= -0.3 * U)):
            mods.append(('price approaching with momentum', 15))
        # P452:981-992 Step 2 'Detect breakout pre-conditions that increase failure probability': a regime change is a pre-condition for the zones standing AGAINST the new regime
        # (a cross above the EMA 200 threatens the resistances overhead, not the supports the cross left behind; Step 3 of Pillar 5: the recapture level becomes a KEY anchor)
        if cross200 and ((above and cross_up) or (z['top'] < spot and not cross_up)):
            mods.append(('regime change, EMA200 cross', 15))
        if any(min(abs(m - z['top']), abs(m - z['bot'])) <= 0.20 * U for m in mags):
            mods.append(('structural extreme magnet within 0.20', 10))
        zfp = min(95, base_z + sum(v for _, v in mods))
        reg = 0 if zfp > 50 else 1 if zfp >= 20 else 2
        z.update(type=ztype, zfp_num=zfp, zfp=ZFP_RANGE[ztype], regime=reg, npill=npill, wall=wall, mods=mods,
                 score=round(seed['base'] + reg + (1 if z['mech']['post_consolidation'] else 0), 1))
    final = [z for z in zones if z['score'] >= 6]
    for z in final:
        z['degree'] = next(nm for th, nm in DEGREES if z['score'] >= th)
        z['tier'] = 'Tier 1' if any(q['kind'] == 'BoM' and q['mit'] <= 1 and q['bot'] <= z['top'] and q['top'] >= z['bot'] for q in X['z4']) else 'Tier 2'
        z['intra'] = intra_zone(z, X, U)
    ab = [z for z in final if z['bot'] > spot]; be = sorted([z for z in final if z['top'] < spot], key=lambda z: -z['top'])
    for z in final:
        if z['bot'] <= spot <= z['top']:
            z['name'], z['cat'] = 'EQUILIBRIUM ZONE', 'MID'
        elif z['bot'] > spot:
            z['name'], z['cat'] = ('RESISTANCE CEILING' if z is max(ab, key=lambda x: x['top']) else 'UPPER RESISTANCE'), 'RES'
        else:
            z['name'], z['cat'] = ('MID-RANGE SUPPORT' if be[0] is z else 'KEY SUPPORT BAND'), 'SUP'
    for i, z in enumerate(sorted(final, key=lambda z: (-z['score'], -z['npill'], abs((z['top'] + z['bot']) / 2 - spot)))):
        z['rank'], z['drawn'] = i + 1, i < MAX_DRAWN
    X.update(zones=sorted(final, key=lambda z: -z['top']), all_bands=zones, trend=trend, scored=scored)
    return X


if __name__ == '__main__':
    import sys, json, os
    monday, pair = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'DXY'
    side = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sidecar', 'out', f'{monday}.json')))
    X = build(pair, monday, side)
    f = '%.3f' if pair == 'DXY' else '%.5f'
    print(f"{pair} {monday} anchor {D.ts(D.boundary_ms(monday))} spot {f % X['spot']} trend {X['trend']} K {X['K']} | levels {len(X['L'])} seeds {len(X['scored'])} bands {len(X['all_bands'])} | MODERATE+ {len(X['zones'])}")
    for z in X['zones']:
        d, m = z['seed']['dims'], z['mech']
        print(f"  {'*' if z['drawn'] else ' '}#{z['rank']} {z['name']:<18} {f % z['bot']}-{f % z['top']} {z['degree']:<14} {z['score']:>4}/14 (T{d['tech']:g} O{d['opt']:g} S{d['struct']:g} P{d['psych']} B{d['bonus']:g} R{z['regime']}) {z['type']} {z['zfp']} {z['tier']} | "
              f"{m['bom']} {m['counter']} {m['reactions']}R/{m['visits']}V {m['e3_status']} | {'; '.join(sorted({l['kind'].split(' (')[0][:34] for l in z['members_lv'] if l['pillar'] in (5, 8)}))[:150]}")
