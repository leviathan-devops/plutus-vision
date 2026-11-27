"""legs.py PAIR MONDAY [fills-file] - BUG LOCATOR ONLY (uses bars after the anchor; never imported by the tool; its tally is never a verdict and never goes to the operator).
Lists the week's 1H zigzag(30 pips) legs lasting 3+ hours (the outside reviewers' 'obvious trades' of the non-anchor maps, audit/G1_count_dryrun7.md rules) and, per leg, the setup that
caught it or the nearest same-direction setup / reject line with what happened to it - so every missed leg is traced to the Engine 3 step that lost it."""
import sys, os, re, subprocess, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'e1_tool'))
import e1_data as D

pair, mon = sys.argv[1], sys.argv[2]
pip = 0.01 if pair == 'DXY' else 0.0001
f = '%.3f' if pair == 'DXY' else '%.5f'
t0, t1 = D.boundary_ms(mon), D.week_end_ms(mon)
h1 = [x for x in D.bars(pair, '60') if t0 <= x['time'] < t1]
ts = lambda t: dt.datetime.fromtimestamp(t / 1000, dt.UTC).strftime('%a %H:%M')


def zigzag(b, thr):
    piv, d = [], 0                                   # (time, price, kind) kind = 'H' / 'L'
    hi, lo = (b[0]['time'], b[0]['high']), (b[0]['time'], b[0]['low'])
    for x in b[1:]:
        if d >= 0 and x['high'] > hi[1]:
            hi = (x['time'], x['high'])
        if d <= 0 and x['low'] < lo[1]:
            lo = (x['time'], x['low'])
        if d == 0:
            if hi[1] - x['low'] >= thr and hi[0] <= x['time']:
                piv.append((lo[0], lo[1], 'L')) if lo[0] < hi[0] else None
                piv.append((hi[0], hi[1], 'H')); d = -1; lo = (x['time'], x['low'])
            elif x['high'] - lo[1] >= thr:
                piv.append((hi[0], hi[1], 'H')) if hi[0] < lo[0] else None
                piv.append((lo[0], lo[1], 'L')); d = 1; hi = (x['time'], x['high'])
        elif d == 1:
            if hi[1] - x['low'] >= thr:
                piv.append((hi[0], hi[1], 'H')); d = -1; lo = (x['time'], x['low'])
        else:
            if x['high'] - lo[1] >= thr:
                piv.append((lo[0], lo[1], 'L')); d = 1; hi = (x['time'], x['high'])
    return piv, (hi if d == 1 else lo), d


piv, last, d = zigzag(h1, 30 * pip)
if not piv or piv[0][0] > h1[0]['time']:
    first = h1[0]
    k0 = 'L' if (piv and piv[0][2] == 'H') else 'H'
    piv.insert(0, (first['time'], first['low'] if k0 == 'L' else first['high'], k0))
piv.append((last[0], last[1], 'H' if d == 1 else 'L'))        # the running extreme closes the last leg (its own reversal is not a leg)
# merge legs under 3 hours into their neighbours, keeping the more extreme pivot
ch = True
while ch:
    ch = False
    for i in range(1, len(piv) - 1):
        if piv[i + 1][0] - piv[i][0] < 3 * 3600000 and i + 2 < len(piv):
            a, b_ = piv[i], piv[i + 2]
            keep = a if ((a[2] == 'H' and a[1] >= b_[1]) or (a[2] == 'L' and a[1] <= b_[1])) else b_
            piv[i:i + 3] = [keep]; ch = True; break
legs = [(piv[i], piv[i + 1]) for i in range(len(piv) - 1) if abs(piv[i + 1][1] - piv[i][1]) >= 30 * pip]

src = sys.argv[3] if len(sys.argv) > 3 else None
txt = open(src).read() if src else subprocess.run([sys.executable, os.path.join(HERE, 'fills.py'), pair, mon], capture_output=True, text=True).stdout
if src:                                               # cut this map's block out of an allfills file
    m = re.search(rf"^{pair} {mon} \|.*?(?=^\S|\Z)", txt, re.S | re.M)
    txt = m.group(0) if m else ''
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
mon_ms = int(dt.datetime.strptime(mon, '%Y-%m-%d').replace(tzinfo=dt.UTC).timestamp() * 1000)


def tms(s):
    m = re.match(r'(\w{3}) (\d\d):(\d\d)', s)
    return mon_ms + DAYS.index(m.group(1)) * 86400000 + int(m.group(2)) * 3600000 + int(m.group(3)) * 60000 if m else None


S, REJ = [], []
for l in txt.splitlines():
    m = re.match(r'\s+(\S+)\s+(ALT )?\s*(\w{3}) (\S+)\s+(LONG|SHORT)\s+E ([\d.]+) SL ([\d.]+) TP ([\d.]+) ([\d.]+)R \| (.*)', l)
    if m:
        st = m.group(10)
        fm = re.search(r'filled (\w{3} \d\d:\d\d)', st)
        S.append({'id': m.group(1), 'day': m.group(3), 'shape': m.group(4), 'long': m.group(5) == 'LONG', 'e': float(m.group(6)), 'sl': float(m.group(7)), 'tp': float(m.group(8)),
                  'fill': tms(fm.group(1)) if fm else None, 'tp_hit': 'TP HIT' in st, 'st': st})
    elif l.strip().startswith('!'):
        REJ.append(l.strip())

caught = 0
print(f"{pair} {mon}: {len(legs)} legs")
for i, (a, b_) in enumerate(legs, 1):
    long = a[2] == 'L'
    size = abs(b_[1] - a[1])
    tol = max(10 * pip, 0.25 * size)
    prev_t = legs[i - 2][0][0] if i > 1 else t0 - 1
    lo_t = (prev_t + a[0]) // 2 if i > 1 else t0 - 1
    ok = [s for s in S if s['long'] == long and s['tp_hit'] and s['fill'] is not None and lo_t <= s['fill'] <= b_[0] and abs(s['e'] - a[1]) <= tol]
    head = f"  {i}. {'L' if long else 'S'} {f % a[1]} {ts(a[0])} -> {f % b_[1]} {ts(b_[0])} ({size / pip:.0f}p)"
    if ok:
        caught += 1
        print(head + f"  CAUGHT {ok[0]['id']} E {f % ok[0]['e']}")
        continue
    near = sorted([s for s in S if s['long'] == long and abs(s['e'] - a[1]) <= max(tol, 20 * pip)], key=lambda s: (abs(s['e'] - a[1]), abs((s['fill'] or a[0]) - a[0])))
    why = '; '.join(f"{s['id']} E {f % s['e']} ({(s['e'] - a[1]) / pip:+.1f}p) SL {f % s['sl']} TP {f % s['tp']}: {s['st'][:70]}" for s in near[:3]) or 'NO SETUP of this direction within 20 pips of the turn'
    rj = [r for r in REJ if any(abs(float(p) - a[1]) <= 20 * pip for p in re.findall(r'\d+\.\d{3,5}', r))]
    print(head + '  MISSED: ' + why + (' || ' + ' | '.join(r[:110] for r in rj[:3]) if rj else ''))
print(f"  LOCATOR {caught}/{len(legs)}")
