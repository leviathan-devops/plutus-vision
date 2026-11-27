"""week_facts.py PAIR MONDAY - facts for the outside G1 count: the Engine 1 objects on the chart with exact prices, the Engine 2 day map next to each day's actual high / low / close.
Uses bars AFTER the anchor for the 'actual' columns: never imported by the tool, never a verdict (goal prompt A5)."""
import sys, os, io, contextlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'e1_tool'))
import plutus, e1_data as D, e1_pine
pair, mon = sys.argv[1], sys.argv[2]
with contextlib.redirect_stdout(io.StringIO()):
    X, E2, E3, src = plutus.run(pair, mon)
f = (lambda v: '%.3f' % v) if pair == 'DXY' else (lambda v: '%.5f' % v)
U = X['U']
lo, hi = e1_pine.reach(X, E2)
near = lambda b, t: b <= hi and t >= lo
print(pair, mon, 'anchor price', f(X['spot']), '| chart shows zones between', f(lo), 'and', f(hi), '(the week\'s reach; zones beyond it sit behind a toggle)')
print('ENGINE 1 ZONES ON THE CHART (one line = one zone = one labelled box; the indented lines are its PARTS, drawn light and dotted inside / against it - operator: "a pressure zone = candle structure + level cluster joined, the parts visibly distinct"):')
sweeps = e1_pine.sweep_boxes(X)
joined, parts = e1_pine.join_zones(X, near, sweeps)
def desc(z):
    if z in sweeps:
        r = z['lo'] - 0.10 * U if z['side'] == 'Demand-side' else z['hi'] + 0.10 * U
        return f"sweep zone {z['side']:<11} {f(z['bot'])}-{f(z['top'])} | sweep reach to {f(r)} (dotted outline){' | confluent with a 4H BoM zone' if z.get('confluent_bom') else ''}"
    if z.get('gap_infill'):
        return f"gap in-fill level {f(z['bot'])}-{f(z['top'])} MODERATE | {z['zfp']} ZFP | signals: {', '.join(z['signals'])}"
    if 'zfp_num' in z and 'tf' not in z:
        return f"pressure zone {z['name']} {f(z['bot'])}-{f(z['top'])} {z['degree']} | {z['zfp']} ZFP | {z['mech']['bom']}"
    if 'tf' in z and 'label' in z:
        return f"supply/demand {z['label']} {z['type']} {f(z['bot'])}-{f(z['top'])}"
    return f"liquidity band (sealed V1, 4H) {f(z['bot'])}-{f(z['top'])}"
allz = [z for z in X['zones'] if z['drawn'] and near(z['bot'], z['top'])] + [z for z in X['sd'] if z['tf'] in ('240', '60') and near(z['bot'], z['top'])] + \
       [z for z in X.get('infill', []) if near(z['bot'], z['top'])] + [z for z in sweeps if near(z['bot'], z['top'])] + [z for z in X['v1']['240']['liquidity'] if near(z['bot'], z['top'])]
allz = [z for z in allz if id(z) in joined or z not in X['v1']['240']['liquidity']]      # a 4H liquidity band standing alone is the sealed V1's drawing (toggle show_v1s, off)
leaders = [z for z in allz if id(z) not in joined]
for L in sorted(leaders, key=lambda z: -z['top']):
    print('  ' + desc(L))
    for z in sorted([z for z in allz if joined.get(id(z)) is L], key=lambda z: -z['top']):
        print('      part: ' + desc(z))
print(f"  ({len(leaders)} zones, {len(allz) - len(leaders)} parts)")
dz = e1_pine.discovery_drawn(X, near, sweeps)
if dz:
    print("DISCOVERY ZONES (thin dashed grey lines; canon: pre-week 'levels to watch' flagged where the zone map is EMPTY - major round numbers, untraded weekly-close extremes, MA convergences, structural extremes; not pressure zones, not used by Engines 2 / 3):")
    for z in sorted(dz, key=lambda z: -z['top']):
        print(f"  discovery zone {f(z['bot'])}{('-' + f(z['top'])) if z['top'] > z['bot'] else ''} | {' + '.join(z['flags'])}")
print('ENGINE 2:')
for a in E2['audit']:
    if a.startswith(('Ceiling', 'Floor', 'Breakout', 'chain', 'Current', 'PRIMARY')):
        print('  ', a[:260])
b = [x for x in D.bars(pair, '60') if D.boundary_ms(mon) <= x['time'] < D.week_end_ms(mon)]
w0 = D.week_start_ms(mon)
for i in range(5):
    xs = [x for x in b if w0 + i * 86400000 <= x['time'] < w0 + (i + 1) * 86400000]
    d = next((d for d in E2['days'] if d['day'] == ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')[i]), None)
    act = f"actual H {f(max(x['high'] for x in xs))} L {f(min(x['low'] for x in xs))} C {f(xs[-1]['close'])}" if xs else 'no bars'
    if d:
        print(f"  {d['day']} forecast {'+'.join(d['shapes']):<10} {d['dir']:<5} box {f(d['lo'])}-{f(d['hi'])} key zone {d['key'][:34]:<34} | {act}")
    else:
        print(f"  {('Mon', 'Tue', 'Wed', 'Thu', 'Fri')[i]} no designation (chain ended: cumulative confidence under 25%) | {act}")
