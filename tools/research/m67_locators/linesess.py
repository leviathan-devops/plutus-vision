"""linesess.py - scratch LOCATOR for plan M2: the line re-anchored at each SESSION open from the price closed by then (P452 6.6 session rules; 10:01 NY 'the DECISIVE moment'):
anchors = trading-day open (17:00 NY prior), London open (02:00 NY), the cut (10:00 NY). Range days of the product's day boxes. Variants:
 flatS   flat from each anchor;  prodS  London -> nearer box bound by 08:00, pinned 08-10, post-cut -> the other bound, each leg from the actual price at its anchor;
 reachS  as prodS but each leg to the nearest E1 level <= 30 p (GS Law 2);  reachS_far  London toward the far bound first."""
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
def nearest(lv, p0, up, reach, lo, hi, minmove):
    c = [v for v in lv if (p0 + minmove < v <= min(p0 + reach, hi))] if up else [v for v in lv if (max(p0 - reach, lo) <= v < p0 - minmove)]
    if not c: return min(p0 + reach, hi) if up else max(p0 - reach, lo)
    return min(c) if up else max(c)
agg = {}
for f in sorted(glob.glob(f'{SP}/*.pkl')):
    pair, mon = os.path.basename(f)[:-4].split('_')
    G = 'GOLD' if mon == '2026-07-06' else 'DEV'
    X, days = pickle.load(open(f, 'rb'))
    pip = D.PIP[pair]; b30 = D.bars(pair, '30'); b15 = D.bars(pair, '15')
    lv = levels(X)
    def px(t):
        pre = [b for b in b15 if b['time'] + 15 * 60000 <= t]
        return pre[-1]['close'] if pre else None
    for i, d in enumerate(days):
        if d['dir'] != 'range': continue
        tL = D.day_anchor_ms(mon, i); ta = tL - 9 * H if i else D.boundary_ms(mon); tc = tL + 8 * H; te = tL + 15 * H
        p0, pL, pc = px(ta), px(tL), px(tc)
        if None in (p0, pL, pc): continue
        lo, hi = d['lo'], d['hi']; r30 = 30 * pip
        V = {}
        V['flatS'] = [[(ta, p0), (tL, p0)], [(tL, pL), (tc, pL)], [(tc, pc), (te, pc)]]
        nu = (hi - pL) < (pL - lo)
        a = hi if nu else lo
        V['prodS'] = [[(ta, p0), (tL, p0)], [(tL, pL), (tL + 6 * H, a), (tc, a)], [(tc, pc), (te, lo if pc > (lo + hi) / 2 else hi)]]
        for name, up in (('reachS', nu), ('reachS_far', not nu)):
            x1 = nearest(lv, pL, up, r30, lo, hi, 3 * pip)
            x2 = nearest(lv, pc, not up, r30, lo, hi, 3 * pip)
            V[name] = [[(ta, p0), (tL, p0)], [(tL, pL), (tL + 6 * H, x1), (tc, x1)], [(tc, pc), (te, x2)]]
        closes = [x for x in b30 if ta <= x['time'] < te]
        for name, segs in V.items():
            def at(t):
                for pts in segs:
                    for (t0, v0), (t1, v1) in zip(pts, pts[1:]):
                        if t0 <= t < t1: return v0 + (v1 - v0) * (t - t0) / max(1, t1 - t0)
                return segs[-1][-1][1]
            A_ = agg.setdefault((G, name), [0, 0, 0.0, 0, 0])
            for x in closes:
                e = abs(x['close'] - at(x['time'] + 15 * 60000)) / pip
                A_[0] += 1; A_[1] += e <= 10; A_[2] += e
for (G, name), (n, w10, miss, ok, nd) in sorted(agg.items()):
    print(f"{G:<5} {name:<11} 30m closes {n:5d}  within 10p {100 * w10 / n:4.0f}%  mean miss {miss / n:5.1f}p")
