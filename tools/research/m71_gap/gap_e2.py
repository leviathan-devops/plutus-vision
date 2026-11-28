"""Engine 2 gap forensics on the 15 cached product runs (LOCATOR: reads the bars after each anchor to measure; nothing here feeds the tool)"""
import sys, glob, pickle, datetime as dt, collections, statistics as st
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
SES = (('Asia 17-02', -1, 17, 0, 2), ('London 02-08', 0, 2, 0, 8), ('pre-cut 08-10', 0, 8, 0, 10), ('NY 10-17', 0, 10, 0, 17))
A = collections.defaultdict(lambda: [0, 0, 0.0])           # name -> within10, n, miss
def add(k, e): A[k][0] += sum(x <= 10 for x in e); A[k][1] += len(e); A[k][2] += sum(e)
bys = collections.defaultdict(lambda: [0, 0, 0.0]); dirs = collections.defaultdict(lambda: [0, 0]); amp = collections.defaultdict(lambda: [[], []])
box = {'days': 0, 'inside': 0, 'cl_in': 0, 'cl': 0, 'ratio': [], 'over': []}
turn = collections.defaultdict(lambda: [0, 0]); cov = collections.defaultdict(list); nlev = []; react = collections.defaultdict(lambda: [0, 0])
G = lambda mon: 'golden' if mon == '2026-07-06' else '4 weeks'
for fn in sorted(glob.glob('gap/*.pkl')):
    P = pickle.load(open(fn, 'rb')); pair, mon = P['pair'], P['mon']; pip = D.PIP[pair]; g = G(mon)
    m = dt.date.fromisoformat(mon); w0, w1 = D.boundary_ms(mon), D.week_end_ms(mon)
    bars = [x for x in D.bars(pair, '30') if w0 <= x['time'] and x['time'] + 1800000 <= w1]
    cl = [(x['time'] + 1800000, x['close']) for x in bars]; at = dict(cl)
    px = lambda t: at[t] if t in at else min(cl, key=lambda q: abs(q[0] - t))[1]
    pts = sorted((int(t), float(v)) for sg in P['segments'] for t, v in sg)
    def line(t):
        best = None
        for (ta, va), (tb, vb) in zip(pts, pts[1:]):
            if ta <= t - 900000 <= tb and tb > ta: best = va + (vb - va) * (t - 900000 - ta) / (tb - ta)
        return best
    L = {t: line(t) for t, _ in cl}
    add((g, '0 PRODUCT line'), [abs(v - L[t]) / pip for t, v in cl if L[t] is not None])
    e_re, e_flat, e_dir, e_end, e_flatL = [], [], [], [], []
    for k in range(5):
        dd = m + dt.timedelta(days=k)
        tL = ms(dd, 2)
        e_flatL += [abs(v - px(tL)) / pip for t, v in cl if tL < t <= ms(dd, 17) + (0 if k == 4 else 9 * 3600000)]
        for nm, off, h0, _, h1 in SES:
            a, b = ms(dd + dt.timedelta(days=off), h0), ms(dd, h1)
            seg = [(t, v) for t, v in cl if a < t <= b]
            if len(seg) < 3 or a < w0: continue
            p0 = px(a); la, lb = line(a + 900000 + 1), line(b + 900000)
            e = [abs(v - L[t]) / pip for t, v in seg if L[t] is not None]
            bys[(g, nm)][0] += sum(x <= 10 for x in e); bys[(g, nm)][1] += len(e); bys[(g, nm)][2] += sum(e)
            net = seg[-1][1] - p0
            if la is not None and lb is not None:
                ln = lb - la
                amp[(g, nm)][0].append(abs(net) / pip); amp[(g, nm)][1].append(abs(ln) / pip)
                if abs(net) >= 10 * pip:
                    dirs[(g, nm)][1] += 1; dirs[(g, nm)][0] += (abs(ln) >= 3 * pip and (ln > 0) == (net > 0))
                # the product's own leg, restarted at the true price of the session start
                e_re += [abs(v - (L[t] - la + p0)) / pip for t, v in seg if L[t] is not None]
            e_flat += [abs(v - p0) / pip for t, v in seg]
            typ = {'Asia 17-02': 8, 'London 02-08': 12, 'pre-cut 08-10': 8, 'NY 10-17': 12}[nm] * (1.0 if pair == 'DXY' else 1.2 if pair == 'EURUSD' else 1.5) * pip
            sgn = 1 if net > 0 else -1
            e_dir += [abs(v - (p0 + sgn * typ * (t - a) / (b - a))) / pip for t, v in seg]
            e_end += [abs(v - (p0 + net * (t - a) / (b - a))) / pip for t, v in seg]
    add((g, '1 no forecast: flat from each London open'), e_flatL)
    add((g, '2 no forecast: flat, restarted at each session start (17/02/08/10)'), e_flat)
    add((g, '3 PRODUCT legs, restarted at each session start'), e_re)
    add((g, '4 session restart + TRUE direction, typical size'), e_dir)
    add((g, '5 session restart + TRUE end price (straight leg)'), e_end)
    # day boxes
    for d_ in P['days']:
        k = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri').index(d_['day']); dd = m + dt.timedelta(days=k)
        a, b = max(ms(dd - dt.timedelta(days=1), 17), w0), ms(dd, 17)
        db = [x for x in bars if a <= x['time'] and x['time'] + 1800000 <= b]
        if len(db) < 5 or d_['t0'] > a + 3600000: continue
        hi, lo = max(x['high'] for x in db), min(x['low'] for x in db)
        box['days'] += 1; box['inside'] += (hi <= d_['hi'] + 3 * pip and lo >= d_['lo'] - 3 * pip)
        box['cl'] += len(db); box['cl_in'] += sum(d_['lo'] - 3 * pip <= x['close'] <= d_['hi'] + 3 * pip for x in db)
        box['ratio'].append((d_['hi'] - d_['lo']) / max(hi - lo, pip)); box['over'].append(max(hi - d_['hi'], d_['lo'] - lo, 0) / pip)
    # levels: where the week's turning points stand vs the Engine 1 map of the anchor
    wk_hi, wk_lo = max(x['high'] for x in bars), min(x['low'] for x in bars)
    lv = [(c, b_, t_, i) for c, b_, t_, i in P['levels'] if t_ >= wk_lo - 5 * pip and b_ <= wk_hi + 5 * pip]
    def cls(c, i):
        if c == 'IP': return 'pressure zone'
        if c.startswith('SD'): return f"S/D {{'240':'4H','60':'1H','30':'30m','15':'15m'}}[{c[2:]!r}]".replace("{'240':'4H','60':'1H','30':'30m','15':'15m'}['240']", '4H').replace("{'240':'4H','60':'1H','30':'30m','15':'15m'}['60']", '1H').replace("{'240':'4H','60':'1H','30':'30m','15':'15m'}['30']", '30m').replace("{'240':'4H','60':'1H','30':'30m','15':'15m'}['15']", '15m') + (' BoM' if i['cls'] == 'BoM' else ' MoM')
        return {'LQ60': 'V1 1H liquidity rung', 'LQ240': 'V1 4H liquidity band', 'LSZ': 'sweep level', 'OPT': 'option strike'}[c]
    by = collections.defaultdict(list)
    for c, b_, t_, i in lv: by[cls(c, i)].append((b_, t_))
    by['ANY Engine 1 level'] = [(b_, t_) for c, b_, t_, i in lv]
    nlev.append(len(lv) / max((wk_hi - wk_lo) / pip, 1) * 10)
    hl = [(x['time'], x['high'], x['low']) for x in bars]
    tps = zz(cl, 15 * pip)
    ext = []
    for t, v, kk in tps:
        w = [x for x in bars if abs(x['time'] + 1800000 - t) <= 1800000]
        ext.append((max(x['high'] for x in w) if kk == 'H' else min(x['low'] for x in w), kk))
    step = pip / 2; grid = [wk_lo + j * step for j in range(int((wk_hi - wk_lo) / step) + 1)]
    for c, zs in by.items():
        near = lambda p: any(b_ - 3 * pip <= p <= t_ + 3 * pip for b_, t_ in zs)
        turn[c][0] += sum(near(p) for p, _ in ext); turn[c][1] += len(ext)
        cov[c].append(sum(near(p) for p in grid) / len(grid))
    # what a zone does when price first reaches it from outside (next 4 hours): turn (15+ pips back before a 30m close 5+ pips beyond its far edge) or pierce
    for c, b_, t_, i in lv:
        if c in ('OPT', 'LSZ') or t_ - b_ <= 0: continue
        name = cls(c, i) + ((' | ' + i['counter']) if i else '')
        for j in range(2, len(bars) - 1):
            pb = bars[j - 1]; x = bars[j]
            up = pb['high'] < b_ and x['high'] >= b_; dn = pb['low'] > t_ and x['low'] <= t_
            if not (up or dn): continue
            if i and i.get('type') and ((up and i['type'] != 'Supply') or (dn and i['type'] != 'Demand')): break
            res = None
            for y in bars[j:j + 8]:
                if (y['close'] > t_ + 5 * pip) if up else (y['close'] < b_ - 5 * pip): res = 0; break
                if (y['low'] <= b_ - 15 * pip) if up else (y['high'] >= t_ + 15 * pip): res = 1; break
            if res is not None: react[name][0] += res; react[name][1] += 1
            break
for g in ('4 weeks', 'golden'):
    print(f"== {g}: 30m closes within 10 pips | mean miss")
    for k in sorted(A):
        if k[0] == g: print(f"   {k[1]:<68} {100 * A[k][0] / A[k][1]:5.1f}%  {A[k][2] / A[k][1]:5.1f} p")
    print("   by session (product line): within 10 p | miss | direction right when the session moved 10+ pips | median size actual vs line")
    for nm, *_ in SES:
        b = bys[(g, nm)]; d = dirs[(g, nm)]; a = amp[(g, nm)]
        print(f"   {nm:<14} {100 * b[0] / b[1]:5.1f}%  {b[2] / b[1]:5.1f} p   dir {d[0]}/{d[1]} = {100 * d[0] / max(1, d[1]):3.0f}%   actual {st.median(a[0]):5.1f} p  line {st.median(a[1]):5.1f} p  (mean line {sum(a[1]) / len(a[1]):5.1f} p)")
print(f"\nDAY BOXES: {box['inside']}/{box['days']} days fully inside their box (3 p tolerance); 30m closes inside the box {100 * box['cl_in'] / box['cl']:.0f}%; "
      f"box height / actual day range: median {st.median(box['ratio']):.2f}; overshoot beyond the box on the other days: median {st.median([o for o in box['over'] if o > 3] or [0]):.0f} p")
print(f"\nENGINE 1 LEVEL DENSITY: {st.mean(nlev):.1f} zones / levels per 10 pips of the week's range")
print("WHERE THE WEEK'S 30m TURNING POINTS STAND: turns within 3 pips of ... | share of all prices within 3 pips of ... (chance) | lift")
for c in sorted(turn, key=lambda c: -turn[c][0] / max(1, turn[c][1]) / max(st.mean(cov[c]), 1e-9)):
    h = turn[c][0] / max(1, turn[c][1]); cv = st.mean(cov[c])
    print(f"   {c:<24} {100 * h:5.1f}%   {100 * cv:5.1f}%   x{h / max(cv, 1e-9):.2f}")
print("\nFIRST TOUCH OF A ZONE from outside, next 4 hours: turned 15+ pips / (turned + closed through)")
for c in sorted(react, key=lambda c: -react[c][1]):
    if react[c][1] >= 8: print(f"   {c:<34} {react[c][0]:3d}/{react[c][1]:3d} = {100 * react[c][0] / react[c][1]:3.0f}%")
