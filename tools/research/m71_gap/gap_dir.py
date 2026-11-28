"""candle-only: which closed-session facts line up with the NEXT session's direction (all 2026 weeks Feb-Oct, 3 pairs; sessions that moved 10+ pips net). LOCATOR."""
import sys, datetime as dt, collections
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import e1_data as D
NY = D.NY
def ms(d, h, mi=0): return int(dt.datetime(d.year, d.month, d.day, h, mi, tzinfo=NY).timestamp() * 1000)
R = collections.defaultdict(lambda: [0, 0])
d = dt.date(2026, 2, 2); days = []
while d <= dt.date(2026, 10, 30):
    if d.weekday() < 5: days.append(d)
    d += dt.timedelta(days=1)
for pair in ('DXY', 'EURUSD', 'GBPUSD'):
    pip = D.PIP[pair]; B = D.bars(pair, '30'); at = {x['time'] + 1800000: x for x in B}
    def seg(a, b): return [at[t] for t in range(a + 1800000, b + 1, 1800000) if t in at]
    for dd in days:
        prev = dd - dt.timedelta(days=3 if dd.weekday() == 0 else 1)
        S = {'asia': seg(ms(dd - dt.timedelta(days=1), 17), ms(dd, 2)) if dd.weekday() else [], 'lon': seg(ms(dd, 2), ms(dd, 8)), 'cage': seg(ms(dd, 8), ms(dd, 10)), 'ny': seg(ms(dd, 10), ms(dd, 17)),
             'pday': seg(ms(prev - dt.timedelta(days=1), 17), ms(prev, 17)), 'pny': seg(ms(prev, 10), ms(prev, 17))}
        net = {k: (v[-1]['close'] - v[0]['open']) if len(v) > 2 else None for k, v in S.items()}
        def rec(name, pred, tgt):
            if pred is None or net[tgt] is None or abs(net[tgt]) < 10 * pip or pred == 0: return
            R[(tgt, name)][1] += 1; R[(tgt, name)][0] += (pred > 0) == (net[tgt] > 0)
        big = lambda k: net[k] if (net[k] is not None and abs(net[k]) >= 10 * pip) else None
        rec('same as the Asian session (10+ p)', big('asia'), 'lon'); rec('same as the prior day (10+ p)', big('pday'), 'lon'); rec('same as the prior NY session (10+ p)', big('pny'), 'lon')
        if S['asia'] and S['lon']:
            hi, lo = max(x['high'] for x in S['asia']), min(x['low'] for x in S['asia']); c = S['asia'][-1]['close']
            rec('toward the NEARER end of the Asian range', (1 if hi - c < c - lo else -1) if hi > lo else None, 'lon')
            # which Asian bound London breaks first, and does London finish on that side
            f = next((1 if x['high'] > hi else -1 for x in S['lon'] if x['high'] > hi or x['low'] < lo), None)
            rec('side of the first Asian-range break in London (known only once it breaks)', f, 'lon')
        rec('same as London (10+ p)', big('lon'), 'cage')
        rec('same as London (10+ p)', big('lon'), 'ny'); rec('OPPOSITE of London (10+ p)', -big('lon') if big('lon') else None, 'ny')
        rec('same as the pre-cut 08-10 (10+ p)', big('cage'), 'ny')
        if S['lon'] and S['cage'] and S['ny']:
            m8 = S['lon'] + S['cage']; hi, lo = max(x['high'] for x in m8), min(x['low'] for x in m8); c = m8[-1]['close']
            rec("back toward the middle of the day's range so far", (-1 if c - lo > hi - c else 1) if hi > lo else None, 'ny')
            n210 = c - S['lon'][0]['open']
            rec('same as 02:00-10:00 net (10+ p)', n210 if abs(n210) >= 10 * pip else None, 'ny')
        rec('same as the prior day (10+ p)', big('pday'), 'ny')
for k in sorted(R):
    a, n = R[k]; print(f"  {k[0]:<5} {k[1]:<74} {a:4d}/{n:4d} = {100 * a / n:3.0f}%")
