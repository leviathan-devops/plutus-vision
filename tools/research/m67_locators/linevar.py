"""linevar.py - scratch LOCATOR for plan M2: line readings for the PRODUCT's range (SS) day boxes (cached by ssfade.py), each day from its trading-day open price p0 (17:00 NY prior),
sessions of P452 6.6: Asia flat to 02:00 NY; London leg 02:00-08:00; NY pre-cut pinned 08:00-10:00; post-cut leg 10:00-17:00. Metrics on the day's 30m closes.
 prod      London to the NEARER box bound, post-cut to the other bound (the product's _session_path, P533 2.3 / D-41)
 flat      p0 all day (no-information reference)
 reach     GS Law 2 'SS <= 30 pips from spot': London to the nearest E1 level (V1 band edge / S/D zone edge) in the nearer-bound direction at most 30 p from p0 (none -> 30 p, inside the box);
           post-cut to the nearest E1 level on the other side of p0 within 30 p
 reachfar  as reach, London toward the FAR bound first"""
import sys, pickle, glob, os
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import e1_data as D
SP = '/tmp/claude-0/-home-user-plutus-vision/b6c77a81-471c-536b-9631-0319cefbf3ab/scratchpad/loc/runs'
H = 3600000
def levels(X):
    lv = []
    for z in X['sd']: lv += [z['bot'], z['top']]
    for tf, h in X['v1'].items():
        for z in h['liquidity']: lv += [z['bot'], z['top']]
    return sorted(lv)
def nearest(lv, p0, up, reach, lo, hi):
    c = [v for v in lv if (p0 < v <= min(p0 + reach, hi)) ] if up else [v for v in lv if (max(p0 - reach, lo) <= v < p0)]
    if not c: return min(p0 + reach, hi) if up else max(p0 - reach, lo)
    return min(c) if up else max(c)
agg = {}
for f in sorted(glob.glob(f'{SP}/*.pkl')):
    pair, mon = os.path.basename(f)[:-4].split('_')
    G = 'GOLD' if mon == '2026-07-06' else 'DEV'
    X, days = pickle.load(open(f, 'rb'))
    pip = D.PIP[pair]; b30 = D.bars(pair, '30'); b15 = D.bars(pair, '15')
    lv = levels(X)
    for i, d in enumerate(days):
        if d['dir'] != 'range': continue
        tL = D.day_anchor_ms(mon, i); ta = tL - 9 * H if i else D.boundary_ms(mon)
        pre = [b for b in b15 if b['time'] < ta]
        if not pre: continue
        p0 = pre[-1]['close']; lo, hi = d['lo'], d['hi']
        near_up = (hi - p0) < (p0 - lo)
        r30 = 30 * pip
        V = {}
        V['flat'] = [(ta, p0), (tL + 15 * H, p0)]
        a = hi if near_up else lo; b_ = lo if near_up else hi
        V['prod'] = [(ta, p0), (tL, p0), (tL + 6 * H, a), (tL + 8 * H, a), (tL + 15 * H, b_)]
        for name, up in (('reach', near_up), ('reachfar', not near_up)):
            x1 = nearest(lv, p0, up, r30, lo, hi)
            x2 = nearest(lv, p0, not up, r30, lo, hi)
            V[name] = [(ta, p0), (tL, p0), (tL + 6 * H, x1), (tL + 8 * H, x1), (tL + 15 * H, x2)]
        closes = [x for x in b30 if ta <= x['time'] < tL + 15 * H]
        for name, pts in V.items():
            def at(t):
                for (t0, v0), (t1, v1) in zip(pts, pts[1:]):
                    if t0 <= t <= t1: return v0 + (v1 - v0) * (t - t0) / max(1, t1 - t0)
                return pts[-1][1]
            A_ = agg.setdefault((G, name), [0, 0, 0.0, 0, 0])
            for x in closes:
                e = abs(x['close'] - at(x['time'] + 15 * 60000)) / pip
                A_[0] += 1; A_[1] += e <= 10; A_[2] += e
            for k in range(4, len(closes)):
                dc = closes[k]['close'] - closes[k - 4]['close']; dl = at(closes[k]['time']) - at(closes[k - 4]['time'])
                if abs(dc) < 5 * pip: continue
                A_[4] += 1; A_[3] += (dc > 0) == (dl > 0) and abs(dl) > 0.5 * pip
for (G, name), (n, w10, miss, ok, nd) in sorted(agg.items()):
    print(f"{G:<5} {name:<9} 30m closes {n:5d}  within 10p {100 * w10 / n:4.0f}%  mean miss {miss / n:5.1f}p  2h direction {100 * ok / max(1, nd):3.0f}% (n {nd})")
