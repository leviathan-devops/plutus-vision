"""qual.py PAIR MONDAY - BUG LOCATOR ONLY for the Engine 1 side condition of G1 ('none bloated, bunched, floating or missing', L-28), with outside reviewer 7's thresholds
(audit/G1_count_dryrun7.md): zone = a top-level line of the facts file, area = its box + its parts' boxes (+ the sweep reach of a top-level sweep zone); bloated = area taller than 20 pips;
bunched = two areas overlap or sit within 3 pips; floating = more than 30 pips from any price of the week; missing = a 1H zigzag(30) turning point with no area within 3 pips.
Uses bars after the anchor: never imported by the tool, never a verdict."""
import sys, os, io, contextlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'e1_tool'))
import plutus, e1_data as D, e1_pine
pair, mon = sys.argv[1], sys.argv[2]
with contextlib.redirect_stdout(io.StringIO()):
    X, E2, E3, src = plutus.run(pair, mon)
pip = D.PIP[pair]; U = X['U']
f = (lambda v: '%.3f' % v) if pair == 'DXY' else (lambda v: '%.5f' % v)
lo, hi = e1_pine.reach(X, E2)
near = lambda b, t: b <= hi and t >= lo
sweeps = e1_pine.sweep_boxes(X)
joined, parts = e1_pine.join_zones(X, near, sweeps)
allz = [z for z in X['zones'] if z['drawn'] and near(z['bot'], z['top'])] + [z for z in X['sd'] if z['tf'] in ('240', '60') and near(z['bot'], z['top'])] + \
       [z for z in X.get('infill', []) if near(z['bot'], z['top'])] + [z for z in sweeps if near(z['bot'], z['top'])] + [z for z in X['v1']['240']['liquidity'] if near(z['bot'], z['top'])]
EXC = os.environ.get('QUAL_EXCLUDE', '').split(',')
if '1H' in EXC:
    allz = [z for z in allz if not (z.get('tf') == '60' and 'label' in z)]
if 'band' in EXC:
    allz = [z for z in allz if z not in X['v1']['240']['liquidity']]
if 'infill' in EXC:
    allz = [z for z in allz if not z.get('gap_infill')]
if EXC != ['']:
    near2 = lambda b, t: any(z['bot'] == b and z['top'] == t for z in allz)
    class _X(dict): pass
    X2 = dict(X, sd=[z for z in X['sd'] if z in allz or z['tf'] not in ('240', '60')], infill=[z for z in X.get('infill', []) if z in allz],
              v1=dict(X['v1'], **{'240': dict(X['v1']['240'], liquidity=[z for z in X['v1']['240']['liquidity'] if z in allz])}))
    joined, parts = e1_pine.join_zones(X2, near, sweeps)
allz = [z for z in allz if id(z) in joined or z not in X['v1']['240']['liquidity']]      # a 4H liquidity band standing alone is the sealed V1's drawing (toggle show_v1s, off)
leaders = [z for z in allz if id(z) not in joined]
def name(z):
    return z.get('name') or z.get('label') or ('sweep' if z in sweeps else '4H band')
areas = []
for L in leaders:
    ps = [z for z in allz if joined.get(id(z)) is L]
    b, t = min([L['bot']] + [z['bot'] for z in ps]), max([L['top']] + [z['top'] for z in ps])
    if L in sweeps:
        r = L['lo'] - 0.10 * U if L['side'] == 'Demand-side' else L['hi'] + 0.10 * U
        b, t = min(b, r), max(t, r)
    areas.append((b, t, name(L)[:22], len(ps)))
areas.sort()
# thresholds: outside reviewer 8 (calibrated on the operator's reference map): bunched = areas overlap or 0-2 pips apart; floating = more than 22 pips beyond the week's extreme; bloated = taller than 35 pips
BLO, BUN, FLO = float(os.environ.get('Q_BLO', 35)), float(os.environ.get('Q_BUN', 2)), float(os.environ.get('Q_FLO', 22))
wk = [x for x in D.bars(pair, '60') if D.boundary_ms(mon) <= x['time'] < D.week_end_ms(mon)]
wl, wh = min(x['low'] for x in wk), max(x['high'] for x in wk)
bloated = [a for a in areas if (a[1] - a[0]) / pip > BLO + 1e-9]
bunched = [(a, b) for i, a in enumerate(areas) for b in areas[i + 1:] if b[0] - a[1] <= BUN * pip]
floating = [a for a in areas if a[0] - wh > FLO * pip or wl - a[1] > FLO * pip]
cover = sum(max(0.0, min(a[1], wh) - max(a[0], wl)) for a in areas) / (wh - wl)
# missing: zigzag(30) turning points of the week with no area within 3 pips
piv, d, hi_, lo_ = [], 0, (wk[0]['time'], wk[0]['high']), (wk[0]['time'], wk[0]['low'])
for x in wk[1:]:
    if d >= 0 and x['high'] > hi_[1]: hi_ = (x['time'], x['high'])
    if d <= 0 and x['low'] < lo_[1]: lo_ = (x['time'], x['low'])
    if d >= 0 and hi_[1] - x['low'] >= 30 * pip and (d == 1 or hi_[0] <= x['time']):
        piv.append(hi_[1]); d = -1; lo_ = (x['time'], x['low'])
    elif d <= 0 and x['high'] - lo_[1] >= 30 * pip:
        piv.append(lo_[1]); d = 1; hi_ = (x['time'], x['high'])
piv.append(hi_[1] if d == 1 else lo_[1])
missing = [p for p in piv if not any(a[0] - 3 * pip <= p <= a[1] + 3 * pip for a in areas)]
print(f"{pair} {mon}: {len(areas)} zones | bloated {len(bloated)} | bunched pairs {len(bunched)} | floating {len(floating)} | missing {len(missing)}/{len(piv)} | cover {cover * 100:.0f}% | week {f(wl)}-{f(wh)}")
if '-v' in sys.argv:
    for a in areas:
        print(f"   {f(a[0])}-{f(a[1])} ({(a[1] - a[0]) / pip:.0f}p) {a[2]} +{a[3]} parts")
