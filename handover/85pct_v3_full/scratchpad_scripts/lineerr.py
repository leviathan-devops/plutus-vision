import sys, io, contextlib
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import plutus, e1_data as D
pairs = sys.argv[1:] or ['DXY', 'EURUSD', 'GBPUSD']
mon = '2026-07-06'
for pair in pairs:
    with contextlib.redirect_stdout(io.StringIO()):
        X, E2, R, src = plutus.run(pair, mon, daily=True)
    segs = E2.get('segments') or []
    pts = []
    for sg in segs:
        for p in (sg if isinstance(sg, list) else [sg]):
            if isinstance(p, (tuple, list)) and len(p) == 2:
                pts.append(p)
    pts = sorted(set((int(t), float(v)) for t, v in pts))
    b1 = [x for x in D.bars(pair, '60') if D.boundary_ms(mon) <= x['time'] < D.week_end_ms(mon)]
    pip = D.PIP[pair]
    def val(t):
        prev = None
        for (ta, va), (tb, vb) in zip(pts, pts[1:]):
            if ta <= t <= tb and tb > ta:
                return va + (vb - va) * (t - ta) / (tb - ta)
        return None
    rng = (max(x['high'] for x in b1) - min(x['low'] for x in b1)) / pip
    per = {}
    for x in b1:
        v = val(x['time'] + 1800000)
        if v is None: continue
        e = max(0.0, x['low'] - v, v - x['high']) / pip
        dname = D.ts(x['time'])[:10]
        per.setdefault(dname, []).append(e)
    allv = [e for v in per.values() for e in v]
    print(pair, f"week range {rng:.0f} pips; line vertices {len(pts)}; hours covered {len(allv)}; mean miss {sum(allv)/max(1,len(allv)):.1f} pips = {100*sum(allv)/max(1,len(allv))/rng:.1f}% of range; hours missed by >5 pips {sum(1 for e in allv if e>5)}")
    for dname in sorted(per):
        v = per[dname]
        print('   ', dname, f"mean miss {sum(v)/len(v):5.1f}  max {max(v):5.1f}  n {len(v)}")
