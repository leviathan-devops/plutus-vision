"""M-72 research (LOCATOR, candles only): which hours are the volatile ones, and which update times keep a line closest to the candles.
Recent = last 3 months of the bar store (Aug 3 - Nov 6 2026); check = Feb 2 - Jul 31 2026."""
import sys, datetime as dt, collections
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import e1_data as D
NY = D.NY
def ms(d, h, mi=0): return int(dt.datetime(d.year, d.month, d.day, h, mi, tzinfo=NY).timestamp() * 1000)
def days(a, b):
    out, d = [], a
    while d <= b:
        if d.weekday() < 5: out.append(d)
        d += dt.timedelta(days=1)
    return out
P = {'recent': days(dt.date(2026, 8, 3), dt.date(2026, 11, 6)), 'check': days(dt.date(2026, 2, 2), dt.date(2026, 7, 31))}
HOURS = [17, 18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
data = {}
for per, dl in P.items():
    rng = collections.defaultdict(list); paths = []
    for pair in ('DXY', 'EURUSD', 'GBPUSD'):
        pip = D.PIP[pair]; at = {x['time']: x for x in D.bars(pair, '30')}
        for dd in dl:
            t0 = ms(dd - dt.timedelta(days=1 if dd.weekday() else 3), 17) if dd.weekday() else ms(dd - dt.timedelta(days=1), 17)
            t0 = ms(dd - dt.timedelta(days=1), 17)
            bs = [at.get(t0 + k * 1800000) for k in range(48)]
            if sum(b is not None for b in bs) < 44: continue
            for k in range(0, 48, 2):
                two = [b for b in bs[k:k + 2] if b]
                if two: rng[(pair, HOURS[k // 2])].append((max(b['high'] for b in two) - min(b['low'] for b in two)) / pip)
            c = []; last = next(b for b in bs if b)['open']
            for b in bs:
                last = b['close'] if b else last; c.append(last / pip)
            paths.append([next(b for b in bs if b)['open'] / pip] + c)       # 49 points: price at 17:00, 17:30 ... 17:00
    data[per] = (rng, paths)
print("MEAN SIZE OF EACH HOUR'S CANDLE (pips; New York time; hour = the candle that STARTS then) - recent 3 months | Feb-Jul")
for h in HOURS:
    r = lambda per, p: sum(data[per][0][(p, h)]) / max(1, len(data[per][0][(p, h)]))
    print(f"  {h:02d}:00  DXY {r('recent','DXY'):5.1f} | {r('check','DXY'):5.1f}   EURUSD {r('recent','EURUSD'):5.1f} | {r('check','EURUSD'):5.1f}   GBPUSD {r('recent','GBPUSD'):5.1f} | {r('check','GBPUSD'):5.1f}")
def score(paths, anchors, perfect):
    a = sorted(anchors) + [48]; ok = n = 0
    for p in paths:
        for i in range(len(a) - 1):
            s, e = a[i], a[i + 1]
            for t in range(s + 1, e + 1):
                v = p[s] + (p[e] - p[s]) * (t - s) / (e - s) if perfect else p[s]
                ok += abs(p[t] - v) <= 10; n += 1
    return 100 * ok / n
slot = lambda h: ((h - 17) % 24) * 2
name = lambda s: f"{HOURS[s // 2]:02d}:{'30' if s % 2 else '00'}"
print("\nUPDATE TIMES: share of 30m closes within 10 pips of (a) a line that only restarts flat at those times = NO forecast, (b) a line with the correct price at each of those times = PERFECT forecast of every leg")
for label, base in (('approved today: 17:00 day open + 02:00 London open', [slot(17), slot(2)]),):
    cur = list(base)
    for per in ('recent', 'check'):
        print(f"  {per:<6} {label}: no forecast {score(data[per][1], cur, False):4.1f}%  perfect {score(data[per][1], cur, True):4.1f}%")
    for step in range(4):
        best = max((s for s in range(1, 48) if s not in cur and s % 2 == 0), key=lambda s: score(data['recent'][1], cur + [s], False) + score(data['recent'][1], cur + [s], True))
        cur.append(best)
        print(f"  + {name(best)}  -> {len(cur)} a day [{', '.join(name(s) for s in sorted(cur))}]: recent no forecast {score(data['recent'][1], cur, False):4.1f}% perfect {score(data['recent'][1], cur, True):4.1f}%   "
              f"| check no forecast {score(data['check'][1], cur, False):4.1f}% perfect {score(data['check'][1], cur, True):4.1f}%")
print("  named sets (recent | check):")
for nm, hs in (('17 / 02 / 05', [17, 2, 5]), ('17 / 02 / 10', [17, 2, 10]), ('17 / 02 / 05 / 10 / 12', [17, 2, 5, 10, 12]), ('17 / 02 / 05 / 10 / 13', [17, 2, 5, 10, 13]), ('17 / 02 / 05 / 08 / 10', [17, 2, 5, 8, 10]), ('17 / 02 / 08 / 10 (session starts + cut)', [17, 2, 8, 10]), ('17 / 02 / 05 / 10', [17, 2, 5, 10]), ('17 / 02 / 08 / 10 / 13', [17, 2, 8, 10, 13]), ('17 / 02 / 05 / 08 / 10 / 13', [17, 2, 5, 8, 10, 13])):
    a = [slot(h) for h in hs]
    print(f"   {nm:<42} no forecast {score(data['recent'][1], a, False):4.1f}% | {score(data['check'][1], a, False):4.1f}%   perfect {score(data['recent'][1], a, True):4.1f}% | {score(data['check'][1], a, True):4.1f}%")
