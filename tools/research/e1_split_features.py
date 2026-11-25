"""research: first-touch facts per zone with canon features, split into BUILD weeks (before 2026-07-01) and VERIFY weeks (after). Limit entry at the entry band's near edge, stop 3 pips past the band.
Prints, per feature subset, touches and how many ran >= 2R / >= 3R on each half. Chance level: 33% at 2R, 25% at 3R."""
import sys, os, re, collections
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import e1_data as D, e1_pine as G, e3_setups as E3
rows = []
for p in ('DXY', 'EURUSD', 'GBPUSD'):
    pip = D.PIP[p]
    for fn in sorted(os.listdir('/home/user/plutus-vision/sidecar/out')):
        m = fn[:-5]
        if not re.match(r'^2026-\d\d-\d\d$', m): continue
        r = G.run(p, m); b0 = D.boundary_ms(m)
        bars = [x for x in D.bars(p, '60') if b0 + 2 * 86400000 <= x['time'] < b0 + 7 * 86400000]
        zs = sorted(r['zones'], key=lambda z: z['bot'])
        for z in zs:
            short = z['side'] == 'Supply'
            if z['bot'] <= r['spot'] <= z['top'] or short != (z['bot'] > r['spot']): continue
            lo, hi = E3.anchor_band(z, 'SHORT' if short else 'LONG', r['spot'])
            entry = lo if short else hi
            i0 = next((i for i, x in enumerate(bars) if x['low'] <= entry <= x['high']), None)
            if i0 is None: continue
            sl = hi + 3 * pip if short else lo - 3 * pip
            risk = abs(entry - sl); mfe = 0
            for x in bars[i0:]:
                if (x['high'] >= sl) if short else (x['low'] <= sl): break
                mfe = max(mfe, (entry - x['low']) if short else (x['high'] - entry))
            order = [t for t in zs if (t['bot'] > r['spot']) == short and not (t['bot'] <= r['spot'] <= t['top'])]
            rank = (order.index(z) if short else order[::-1].index(z)) if z in order else 9
            f = {'all': True, 'with 4H storyline': short == (r['e2']['bias'] == 'down'), 'against 4H storyline': short != (r['e2']['bias'] == 'down'),
                 '4H BoM inside': any(q.get('h4bom') for q in z['structs']), 'candle zone': bool(z['structs']), 'level zone': not z['structs'],
                 'all candles 0X': bool(z['structs']) and all(q['mit'] == 0 for q in z['structs']), 'has 1X candle': any(q['mit'] == 1 for q in z['structs']),
                 'Hard/Standard Wall': z['type'] in ('Hard Wall', 'Standard Wall'), 'Soft Wall': z['type'] == 'Soft Wall', 'score >= 11': z['score'] >= 11, 'score <= 8': z['score'] <= 8,
                 'nearest zone to spot': rank == 0, '2nd+ zone from spot': rank >= 1, 'touch Mon': (bars[i0]['time'] - (b0 + 2 * 86400000)) // 86400000 == 0, 'touch Tue-Thu': 1 <= (bars[i0]['time'] - (b0 + 2 * 86400000)) // 86400000 <= 3,
                 'risk <= 8 pips': risk / pip <= 8, 'risk > 12 pips': risk / pip > 12, 'pair DXY': p == 'DXY', 'pair EURUSD': p == 'EURUSD', 'pair GBPUSD': p == 'GBPUSD',
                 'with 4H + 2nd+ zone': short == (r['e2']['bias'] == 'down') and rank >= 1, 'with 4H + Hard/Standard': short == (r['e2']['bias'] == 'down') and z['type'] in ('Hard Wall', 'Standard Wall')}
            rows.append((m < '2026-07-01', mfe / risk, f))
print(f"{'subset':<26}{'BUILD n':>8}{'>=2R':>6}{'>=3R':>6}   {'VERIFY n':>8}{'>=2R':>6}{'>=3R':>6}")
for k in rows[0][2]:
    out = []
    for half in (True, False):
        rr = [x for x in rows if x[0] == half and x[2][k]]
        n = len(rr)
        out += [n, f"{100 * sum(1 for x in rr if x[1] >= 2) // max(n, 1)}%", f"{100 * sum(1 for x in rr if x[1] >= 3) // max(n, 1)}%"]
    print(f"{k:<26}{out[0]:>8}{out[1]:>6}{out[2]:>6}   {out[3]:>8}{out[4]:>6}{out[5]:>6}")
