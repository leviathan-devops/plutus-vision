import sys, os, re, collections, statistics
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import e1_data as D, e1_pine as G, e3_setups as E3
p = sys.argv[1] if len(sys.argv) > 1 else 'DXY'; pip = D.PIP[p]
rows = []
for fn in sorted(os.listdir('/home/user/plutus-vision/sidecar/out')):
    m = fn[:-5]
    if not re.match(r'^2026-\d\d-\d\d$', m): continue
    r = G.run(p, m); b0 = D.boundary_ms(m)
    bars = [x for x in D.bars(p, '60') if b0 + 2*86400000 <= x['time'] < b0 + 7 * 86400000]
    if not bars: continue
    for z in r['zones']:
        short = z['side'] == 'Supply'
        if z['bot'] <= r['spot'] <= z['top']: continue
        if short != (z['bot'] > r['spot']): continue
        lo, hi = E3.anchor_band(z, 'SHORT' if short else 'LONG', r['spot'])
        entry = lo if short else hi
        i0 = next((i for i, x in enumerate(bars) if x['low'] <= entry <= x['high']), None)
        if i0 is None: continue
        for tag, far in (('band', hi if short else lo), ('zone', z['top'] if short else z['bot'])):
            sl = far + 3 * pip if short else far - 3 * pip
            risk = abs(entry - sl); mfe = 0; out = False
            for x in bars[i0:]:
                if (x['high'] >= sl) if short else (x['low'] <= sl): out = True; break
                mfe = max(mfe, (entry - x['low']) if short else (x['high'] - entry))
            rows.append((tag, z['kind'], z['tier'][:6], z['type'], risk / pip, mfe / risk, out, max(s['mit'] for s in z['structs']) if z['structs'] else -1, ('BoM' if any(q.get('h4bom') for q in z['structs']) else '1H-BoM' if any(q['kind']=='BoM' for q in z['structs']) else 'MoM' if z['structs'] else 'lvl') + ('/with4H' if (short == (r['e2']['bias']=='down')) else '/against4H'), z['degree']))
for tag in ('band', 'zone'):
    rr = [x for x in rows if x[0] == tag]
    print(tag, 'touches', len(rr), 'median risk pips %.1f' % statistics.median(x[4] for x in rr),
          '| reached >=1R %d  >=2R %d  >=3R %d  >=4R %d' % tuple(sum(1 for x in rr if x[5] >= k) for k in (1, 2, 3, 4)), '| stopped before 1R', sum(1 for x in rr if x[5] < 1))
    for key, idx in (('class', 8), ('degree', 9), ('type', 3)):
        c = collections.defaultdict(lambda: [0, 0])
        for x in rr:
            c[x[idx]][0] += 1; c[x[idx]][1] += x[5] >= 3
        print('   by', key, {k: f'{v[1]}/{v[0]}' for k, v in sorted(c.items(), key=lambda kv: str(kv[0]))})
