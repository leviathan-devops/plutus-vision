"""airweb.py [opts] PAIR:MONDAY ... - LOCATOR for plan memory/16 step M1 (never imported by the tool, never a verdict): the Fibonacci Spiderwebs PDF item 4 scalp web
built at each trading day's London open (02:00 New York) from bars closed by then only, replayed on the 15m candles.

PDF item 4 (verbatim, /home/user/inputs/4d1ca379-Fibonacci_Spiderwebs.pdf): 'For SS/Rcvry SCALP moves - Look at 15m timeframe price action - Anchor to nearest NON-SURGE swing
high/swing low - Very important the fib anchors are inside a 15m consolidation range. NOT anchored to previous BS/WL anchors. - Trade with the trend. Direction = Trend.
- London Session open position = Trade Setup Anchor - Nearest Fib level = entry - Make sure there is a 0.5-1 pip buffer in front of the entry ... - 1-2 Fib levels back = SL
- Add a 1 pip buffer to the SL from the exact fib level. 2-3 is safer ... - Fib wormhole anchor of entry level = TP (0.382 -> 1.382, etc) - Make sure there is a 1.5-2 pip buffer
in front of the TP'.
Readings (each an open choice the PDF leaves; picked on the dev set, recorded as D-rows when adopted):
  --range asia      the 15m consolidation range = the trading day's Asian session (P452 6.6 rule 1 'Asian Session typically manifests SS ... within the prior day's range'), 17:00 NY -> 02:00 NY
  --trend st4h|st30 direction = the 4H structure (P533:2649 / storyline) | the 30m structure (P533:205 'Scalp Stack: 30m (HTF storyline) -> 15m (trading timeframe)'), both as of the London open
  --back 1|2        SL = 1 or 2 Fib levels back;  --slbuf pips (1, '2-3 is safer');  --ebuf pips (0.5-1);  --tpbuf pips (1.5-2)
"""
import sys, os, argparse
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'e1_tool'))
import e1_data as D

ALLV = (-0.236, 0.0, 0.236, 0.382, 0.5, 0.618, 0.786, 1.0, 1.236, 1.382)
H = 3600000
ap = argparse.ArgumentParser()
ap.add_argument('maps', nargs='+')
ap.add_argument('--range', default='asia')
ap.add_argument('--trend', default='st4h')
ap.add_argument('--back', type=int, default=1)
ap.add_argument('--slbuf', type=float, default=1.0)
ap.add_argument('--ebuf', type=float, default=0.5)
ap.add_argument('--tpbuf', type=float, default=1.5)
ap.add_argument('--minrr', type=float, default=0.0)
ap.add_argument('-v', action='store_true')
ap.add_argument('--anchor', default='asia')          # asia | swing15 (the nearest 15m swing high above and swing low below the London-open position, within the last 24 h) | day30 (item 5: nearest 30m swing high / low of the same trading day) | h4 (item 3: the last 4H swing high and swing low)
ap.add_argument('--hours', type=int, default=24)
A = ap.parse_args()


def swings(b, n=2):
    hs = [i for i in range(n, len(b) - n) if b[i]['high'] == max(x['high'] for x in b[i - n:i + n + 1])]
    ls = [i for i in range(n, len(b) - n) if b[i]['low'] == min(x['low'] for x in b[i - n:i + n + 1])]
    return hs, ls


def structure(b):
    """P533:2649 higher highs + higher lows = up; lower highs + lower lows = down; mixed = None (the code's own 4H rule, e2_chain.structure_4h, on any timeframe)"""
    hs, ls = swings(b)
    if len(hs) >= 2 and len(ls) >= 2:
        hh, hl = b[hs[-1]]['high'] > b[hs[-2]]['high'], b[ls[-1]]['low'] > b[ls[-2]]['low']
        return 'up' if (hh and hl) else 'down' if (not hh and not hl) else None
    return None


def web(pair, monday, i):
    """the day-i scalp web at its London open -> (dict, None) or (None, reason)"""
    tL = D.day_anchor_ms(monday, i)
    ta = tL - 9 * H                                    # the trading day's open = 17:00 NY the evening before
    b15 = D.closed_until(pair, '15', tL)
    asia = [x for x in b15 if x['time'] >= ta]
    if len(asia) < 8:
        return None, 'no Asian session bars'
    p0 = b15[-1]['close']
    d = structure(D.closed_until(pair, '240' if A.trend == 'st4h' else '30', tL)[-90:])
    if d is None:
        return None, 'no trend (structure mixed)'
    if A.anchor == 'asia':
        hi = max(x['high'] for x in asia); lo = min(x['low'] for x in asia)
    else:
        tf, n, since = {'swing15': ('15', 2, tL - A.hours * H), 'day30': ('30', 2, ta), 'h4': ('240', 2, tL - 20 * 24 * H)}[A.anchor]
        bb = [x for x in D.closed_until(pair, tf, tL) if x['time'] >= since]
        hs, ls = swings(bb, n)
        his = [bb[k]['high'] for k in hs if bb[k]['high'] > p0]
        los = [bb[k]['low'] for k in ls if bb[k]['low'] < p0]
        if not his or not los:
            return None, 'no swing high above / low below'
        if A.anchor == 'h4':
            hi = bb[[k for k in hs if bb[k]['high'] > p0][-1]]['high']; lo = bb[[k for k in ls if bb[k]['low'] < p0][-1]]['low']   # the most recent swing high above / low below
        else:
            hi = min(his); lo = max(los)                                                                   # the nearest swing high above / low below the London-open position
    R = hi - lo
    pip = D.PIP[pair]
    if R < 5 * pip:
        return None, f'range {R / pip:.1f} p'
    up = d == 'up'
    lv = (lambda r: lo + r * R) if up else (lambda r: hi - r * R)
    cand = [r for r in ALLV if (lv(r) < p0 if up else lv(r) > p0)]      # the entry side of the London-open position: a long buys below it, a short sells above it
    if not cand:
        return None, 'no level on the entry side'
    r = min(cand, key=lambda q: abs(lv(q) - p0))                          # 'Nearest Fib level = entry'
    j = ALLV.index(r)
    if j - A.back < 0:
        return None, 'no level behind'
    rs = ALLV[j - A.back]                                                 # '1-2 Fib levels back = SL'
    sg = 1 if up else -1
    entry = lv(r) + sg * A.ebuf * pip
    sl = lv(rs) - sg * A.slbuf * pip
    tp = lv(r + 1.0) - sg * A.tpbuf * pip                                 # 'Fib wormhole anchor of entry level = TP'
    rr = abs(tp - entry) / abs(entry - sl)
    return {'day': i, 'tL': tL, 'end': tL + 15 * H, 'dir': 'LONG' if up else 'SHORT', 'r': r, 'rs': rs, 'entry': entry, 'sl': sl, 'tp': tp, 'rr': rr,
            'hi': hi, 'lo': lo, 'R': R / pip, 'p0': p0}, None


def replay(pair, w):
    """15m candles from the London open: fill inside the trading day; void if the TP prints before the fill; after the fill SL first when one candle touches both"""
    lng = w['dir'] == 'LONG'
    e = None
    for b in D.bars(pair, '15'):
        if b['time'] < w['tL']:
            continue
        if e is None:
            if b['time'] >= w['end']:
                return 'NOT FILLED', None
            hit_e = (b['low'] <= w['entry']) if lng else (b['high'] >= w['entry'])
            if not hit_e:
                if (b['high'] >= w['tp']) if lng else (b['low'] <= w['tp']):
                    return 'MISSED', None
                continue
            e = b['time']
        if (b['low'] <= w['sl']) if lng else (b['high'] >= w['sl']):
            return 'SL', e
        if (b['high'] >= w['tp']) if lng else (b['low'] <= w['tp']):
            return 'TP', e
        if b['time'] > w['tL'] + 5 * 24 * H:
            return 'OPEN', e
    return 'OPEN', e


tot = {}
for m in A.maps:
    pair, mon = m.split(':')
    row = {'webs': 0, 'filled': 0, 'TP': 0, 'SL': 0, 'NF': 0, 'MISSED': 0}
    for i in range(5):
        w, why = web(pair, mon, i)
        if w is None:
            if A.v: print(f"   {pair} {mon} d{i}: no web - {why}")
            continue
        if w['rr'] < A.minrr:
            if A.v: print(f"   {pair} {mon} d{i}: rr {w['rr']:.1f} < {A.minrr}")
            continue
        res, e = replay(pair, w)
        row['webs'] += 1
        row['filled'] += e is not None
        row[{'TP': 'TP', 'SL': 'SL', 'NOT FILLED': 'NF', 'MISSED': 'MISSED', 'OPEN': 'NF'}[res]] += 1
        if A.v:
            f = '%.3f' if pair == 'DXY' else '%.5f'
            print(f"   {pair} {mon} d{i} {w['dir']:<5} range {f % w['lo']}-{f % w['hi']} ({w['R']:.0f} p) r {w['r']} E {f % w['entry']} SL {f % w['sl']} TP {f % w['tp']} RR {w['rr']:.1f} -> {res} {D.ts(e) if e else ''}")
    for k in (pair, 'ALL'):
        t = tot.setdefault(k, dict.fromkeys(row, 0))
        for q in row: t[q] += row[q]
    print(f"{pair} {mon}: webs {row['webs']} filled {row['filled']} TP {row['TP']} SL {row['SL']} never {row['NF']} missed {row['MISSED']}")
for k, t in tot.items():
    wr = 100 * t['TP'] / max(1, t['TP'] + t['SL'])
    print(f"TOTAL {k}: webs {t['webs']} filled {t['filled']} TP {t['TP']} SL {t['SL']} never {t['NF']} missed {t['MISSED']} | win {wr:.0f}%")
