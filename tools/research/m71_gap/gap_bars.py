"""candle-only facts for the Engine 2 gap (LOCATOR; no engine): what a forward line must contain to sit on the 30m line chart.
For every 2026 week Feb -> Oct and pair: lines through the TRUE closes at given vertex sets -> share of 30m closes within 10 pips (the ceiling of each vertex set);
30m turning points per day; their New York time of day; size of each session's move."""
import sys, datetime as dt, collections
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import e1_data as D
NY = D.NY
def ms(d, h, mi=0): return int(dt.datetime(d.year, d.month, d.day, h, mi, tzinfo=NY).timestamp() * 1000)
def zz(pts, thr):
    piv, d = [], 0; hi = lo = pts[0]
    for t, v in pts[1:]:
        if d >= 0 and v > hi[1]: hi = (t, v)
        if d <= 0 and v < lo[1]: lo = (t, v)
        if d == 0:
            if hi[1] - v >= thr: piv.append(hi + ('H',)); d = -1; lo = (t, v)
            elif v - lo[1] >= thr: piv.append(lo + ('L',)); d = 1; hi = (t, v)
        elif d == 1 and hi[1] - v >= thr: piv.append(hi + ('H',)); d = -1; lo = (t, v)
        elif d == -1 and v - lo[1] >= thr: piv.append(lo + ('L',)); d = 1; hi = (t, v)
    return piv
def interp(vs, t):
    for (ta, va), (tb, vb) in zip(vs, vs[1:]):
        if ta <= t <= tb: return va + (vb - va) * (t - ta) / (tb - ta) if tb > ta else va
    return None
def score(vs, cl, pip):
    e = [abs(v - interp(vs, t)) / pip for t, v in cl if interp(vs, t) is not None]
    return sum(x <= 10 for x in e), len(e), sum(e)
weeks = []
d = dt.date(2026, 2, 2)
while d <= dt.date(2026, 10, 26): weeks.append(d); d += dt.timedelta(days=7)
SETS = collections.OrderedDict()
agg = collections.defaultdict(lambda: [0, 0, 0.0]); nv = collections.defaultdict(int)
hist = collections.defaultdict(int); legs = collections.defaultdict(list); tpd = collections.defaultdict(list); ndays = 0
for pair in ('DXY', 'EURUSD', 'GBPUSD'):
    pip = D.PIP[pair]; B = D.bars(pair, '30')
    for m in weeks:
        w0, w1 = ms(m, 2), ms(m + dt.timedelta(days=4), 17)
        cl = [(x['time'] + 1800000, x['close']) for x in B if w0 <= x['time'] + 1800000 <= w1]
        if len(cl) < 200: continue
        at = dict(cl)
        px = lambda t: at.get(t) if t in at else min(cl, key=lambda q: abs(q[0] - t))[1]
        def clock(hours):
            ts = sorted({t for k in range(5) for h, mi in hours for t in [ms(m + dt.timedelta(days=k + (-1 if h >= 17 and (h, mi) != (17, 0) else 0)), h, mi)]} | {w0, w1} | {ms(m + dt.timedelta(days=k), 17) for k in range(5)})
            return [(t, px(t)) for t in ts if w0 <= t <= w1]
        V = {'A session clock 17/02/08/10/17': clock([(2, 0), (8, 0), (10, 0)]),
             'B + 12:00, 14:30': clock([(2, 0), (8, 0), (10, 0), (12, 0), (14, 30)]),
             'C every 2 hours': [(t, v) for t, v in cl if dt.datetime.fromtimestamp(t / 1000, NY).hour % 2 == 1 and dt.datetime.fromtimestamp(t / 1000, NY).minute == 0] ,
             'D every hour': [(t, v) for t, v in cl if dt.datetime.fromtimestamp(t / 1000, NY).minute == 0]}
        for thr in (30, 20, 15, 10):
            V[f'T true turns of {thr}+ pips'] = [cl[0]] + [(t, v) for t, v, k in zz(cl, thr * pip)] + [cl[-1]]
        # no-forecast baselines: a flat line from the price at each anchor
        def flat(anchors):
            a = sorted(t for t in anchors if w0 <= t < w1); out = []
            for t0, t1 in zip(a, a[1:] + [w1]): out += [(t0, px(t0)), (t1 - 1, px(t0))]
            return out
        V['F flat from each London open (no forecast)'] = flat([ms(m + dt.timedelta(days=k), 2) for k in range(5)])
        V['G flat from each session start 17/02/08/10 (no forecast)'] = flat([ms(m + dt.timedelta(days=k), h) for k in range(-1, 5) for h in (17, 2, 8, 10)] + [w0])
        for k, vs in V.items():
            vs = sorted(set(vs))
            if vs[0][0] > w0: vs = [(w0, px(w0))] + vs
            if vs[-1][0] < w1: vs = vs + [(w1, px(w1))]
            a, n, s = score(vs, cl, pip); agg[k][0] += a; agg[k][1] += n; agg[k][2] += s; nv[k] += len(vs)
        ndays += 5
        for t, v, k in zz(cl, 15 * pip):
            x = dt.datetime.fromtimestamp(t / 1000, NY); hist[(x.hour, x.minute)] += 1
        for k in range(5):
            dd = m + dt.timedelta(days=k)
            for nm, a, b in (('Asia 17-02', ms(dd - dt.timedelta(days=1), 17), ms(dd, 2)), ('London 02-08', ms(dd, 2), ms(dd, 8)), ('pre-cut 08-10', ms(dd, 8), ms(dd, 10)), ('NY 10-17', ms(dd, 10), ms(dd, 17))):
                seg = [v for t, v in cl if a <= t <= b]
                if len(seg) > 2: legs[(pair, nm)].append((abs(seg[-1] - seg[0]) / pip, (max(seg) - min(seg)) / pip))
            day = [(t, v) for t, v in cl if ms(dd - dt.timedelta(days=1), 17) <= t <= ms(dd, 17)]
            if len(day) > 10: tpd[pair].append(len(zz(day, 15 * pip)))
print(f"weeks {len(weeks)} x 3 pairs, {ndays} trading days\n")
print("LINE THROUGH THE TRUE PRICES AT ... -> 30m closes within 10 pips | mean miss | vertices per day")
for k, (a, n, s) in agg.items():
    print(f"  {k:<58} {100 * a / n:5.1f}%  {s / n:5.1f} p  {nv[k] / ndays:5.1f}")
print("\n30m TURNING POINTS (15+ pip swings) per trading day:", {p: round(sum(v) / len(v), 2) for p, v in tpd.items()})
tot = sum(hist.values())
print("TIME OF DAY of the turning points (New York), share of all turns per 30m slot (uniform = 2.1%):")
for h in list(range(17, 24)) + list(range(0, 17)):
    print(f"  {h:02d}:00 {100 * hist[(h, 0)] / tot:4.1f}%   {h:02d}:30 {100 * hist[(h, 30)] / tot:4.1f}%")
print("\nSESSION MOVES (pips): median net move | median range | share of sessions with net >= 10 pips")
import statistics as st
for k, v in sorted(legs.items()):
    print(f"  {k[0]:<7} {k[1]:<14} net {st.median(x[0] for x in v):5.1f}  range {st.median(x[1] for x in v):5.1f}  net>=10p {100 * sum(x[0] >= 10 for x in v) / len(v):3.0f}%   n={len(v)}")
