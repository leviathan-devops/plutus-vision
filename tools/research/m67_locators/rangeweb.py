"""rangeweb.py [--look H] [--entry 0.236] [--slp 2] MAPS - scratch LOCATOR (plan M5): his printed spiderwebs are drawn on the CURRENT consolidation range (0 = its low, 1 = its high);
Spiderwebs PDF item 2 'Swing Low + Swing High - Deepest + Most Recent - BoM Anchors - NOT subsequent market structure HL/LH'. At each day's London open, from 1H bars closed by then
(last --look hours): the deepest low L and highest high H; the more recent of the two is the surge's end; the range = that extreme and the opposite extreme AFTER it (the recovery).
Orders for the day (to 17:00 NY): long at level --entry (+0.5 p in front), SL level 0 - --slp pips, TP level 1 - 1.5 p; short mirrored (entry 1 - --entry). Range >= 20 pips, price inside it.
One trade at a time per direction; void if the TP prints before the fill; after the fill SL first when one 15m candle touches both."""
import sys, argparse
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import e1_data as D
ap = argparse.ArgumentParser(); ap.add_argument('maps', nargs='+'); ap.add_argument('--look', type=int, default=72); ap.add_argument('--entry', type=float, default=0.236)
ap.add_argument('--slp', type=float, default=2.0); ap.add_argument('--minr', type=float, default=20); ap.add_argument('-v', action='store_true')
A = ap.parse_args()
H = 3600000
tot = {}
for m in A.maps:
    pair, mon = m.split(':'); pip = D.PIP[pair]
    b15all = D.bars(pair, '15')
    row = [0, 0, 0, 0]       # webs, fills, TP, SL
    for i in range(5):
        tL = D.day_anchor_ms(mon, i); tE = tL + 15 * H
        b1 = [b for b in D.closed_until(pair, '60', tL) if b['time'] >= tL - A.look * H]
        if len(b1) < 10: continue
        p0 = b1[-1]['close']
        lo_b = min(b1, key=lambda b: b['low']); hi_b = max(b1, key=lambda b: b['high'])
        if lo_b['time'] > hi_b['time']:            # down surge ended at the deepest low; the recovery high after it
            L = lo_b['low']; after = [b for b in b1 if b['time'] > lo_b['time']]
            if not after: continue
            Hh = max(b['high'] for b in after)
        else:                                       # up surge ended at the highest high; the pullback low after it
            Hh = hi_b['high']; after = [b for b in b1 if b['time'] > hi_b['time']]
            if not after: continue
            L = min(b['low'] for b in after)
        R = Hh - L
        if R < A.minr * pip or not (L < p0 < Hh): continue
        lv = lambda r: L + r * R
        orders = [('LONG', lv(A.entry) + 0.5 * pip, L - A.slp * pip, Hh - 1.5 * pip), ('SHORT', lv(1 - A.entry) - 0.5 * pip, Hh + A.slp * pip, L + 1.5 * pip)]
        row[0] += 1
        bars = [b for b in b15all if tL <= b['time'] < tL + 5 * 24 * H]
        state = {o[0]: None for o in orders}           # None pending, 'void', ('open', t), 'TP'/'SL'
        for b in bars:
            for d, e, sl, tp in orders:
                lng = d == 'LONG'
                st = state[d]
                if st is None:
                    if b['time'] >= tE: state[d] = 'void'; continue
                    other = state['SHORT' if lng else 'LONG']
                    if (b['high'] >= tp) if lng else (b['low'] <= tp):
                        if not ((b['low'] <= e) if lng else (b['high'] >= e)): state[d] = 'void'; continue
                    if (b['low'] <= e) if lng else (b['high'] >= e):
                        state[d] = ('open', b['time']); row[1] += 1
                    else: continue
                st = state[d]
                if isinstance(st, tuple):
                    if (b['low'] <= sl) if lng else (b['high'] >= sl): state[d] = 'SL'; row[3] += 1
                    elif (b['high'] >= tp) if lng else (b['low'] <= tp): state[d] = 'TP'; row[2] += 1
        if A.v:
            f = '%.3f' if pair == 'DXY' else '%.5f'
            print(f"   {pair} {mon} d{i} range {f % L}-{f % Hh} ({R / pip:.0f} p) -> {state}")
    G = 'GOLD' if mon == '2026-07-06' else 'DEV'
    t = tot.setdefault(G, [0, 0, 0, 0])
    for k in range(4): t[k] += row[k]
for G, (w, f_, tp, sl) in tot.items():
    print(f"{G}: webs {w} fills {f_} TP {tp} SL {sl} win {100 * tp / max(1, tp + sl):.0f}%")
