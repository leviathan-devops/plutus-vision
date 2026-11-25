"""research: instead of a resting limit at the zone edge, enter on the 1H REJECTION close (bar that traded into the zone and closed back out on the approach side),
stop 3 pips past the extreme made inside the zone. Facts for debugging E3 entry timing (canon 8.25 / L-23 'sharp rejection'); not an accuracy score."""
import sys, os, re, collections, statistics
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import e1_data as D, e1_pine as G
tot = collections.Counter(); risks = []
for p in (sys.argv[1:] or ['DXY']):
    pip = D.PIP[p]
    for fn in sorted(os.listdir('/home/user/plutus-vision/sidecar/out')):
        m = fn[:-5]
        if not re.match(r'^2026-\d\d-\d\d$', m): continue
        r = G.run(p, m); b0 = D.boundary_ms(m)
        bars = [x for x in D.bars(p, '60') if b0 + 2 * 86400000 <= x['time'] < b0 + 7 * 86400000]
        for z in r['zones']:
            short = z['side'] == 'Supply'
            if z['bot'] <= r['spot'] <= z['top'] or short != (z['bot'] > r['spot']): continue
            near, far = (z['bot'], z['top']) if short else (z['top'], z['bot'])
            i0 = next((i for i, x in enumerate(bars) if ((x['high'] >= near) if short else (x['low'] <= near))), None)
            if i0 is None: continue
            tot['touched'] += 1
            ext = None; ent = None
            for j in range(i0, min(i0 + 6, len(bars))):
                x = bars[j]
                ext = max(ext or x['high'], x['high']) if short else min(ext or x['low'], x['low'])
                if (x['close'] > far) if short else (x['close'] < far):
                    tot['closed through before any rejection'] += 1; break
                if (x['close'] < near) if short else (x['close'] > near):
                    ent = (j, x['close']); break
            if not ent:
                if ext is not None and not ((bars[min(i0 + 5, len(bars) - 1)]['close'] > far) if short else (bars[min(i0 + 5, len(bars) - 1)]['close'] < far)): tot['no rejection close within 6h'] += 1
                continue
            j, e = ent
            sl = ext + 3 * pip if short else ext - 3 * pip
            risk = abs(e - sl); risks.append(risk / pip); mfe = 0
            for x in bars[j + 1:]:
                if (x['high'] >= sl) if short else (x['low'] <= sl): break
                mfe = max(mfe, (e - x['low']) if short else (x['high'] - e))
            tot['rejection entries'] += 1
            for k in (1, 2, 3, 4):
                tot[f'>= {k}R'] += mfe / risk >= k
print(dict(tot)); print('median risk pips', statistics.median(risks) if risks else None)
