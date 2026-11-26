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
print('ENGINE 1 OBJECTS ON THE CHART (all of these are Engine 1 zones):')
for z in X['zones']:
    if z['drawn'] and near(z['bot'], z['top']):
        print(f"  pressure zone  {z['name']:<18} {f(z['bot'])}-{f(z['top'])} {z['degree']} | {z['zfp']} ZFP | {z['mech']['bom']}")
for z in X.get('infill', []):
    if near(z['bot'], z['top']):
        print(f"  gap in-fill level (dashed box)    {f(z['bot'])}-{f(z['top'])} MODERATE | {z['zfp']} ZFP | signals: {', '.join(z['signals'])}")
for z in sorted(X['sd'], key=lambda z: -z['top']):
    if z['tf'] in ('240', '60') and near(z['bot'], z['top']):
        print(f"  supply/demand  {z['label']:<28} {z['type']:<6} {f(z['bot'])}-{f(z['top'])}")
merged = []                                              # as drawn: sweep zones of one side within 0.05 of each other are one box
for z in sorted([z for z in X['lsz'] if not z['swept']], key=lambda z: (z['side'], z['level'])):
    if merged and merged[-1]['side'] == z['side'] and z['level'] - merged[-1]['hi'] <= 0.05 * U + 1e-12:
        merged[-1]['hi'] = z['level']; merged[-1]['confluent_bom'] = merged[-1].get('confluent_bom') or z.get('confluent_bom')
    else:
        merged.append(dict(z, lo=z['level'], hi=z['level']))
for z in sorted(merged, key=lambda z: -z['hi']):
    zb, zt = (z['lo'], z['hi'] + 0.05 * U) if z['side'] == 'Demand-side' else (z['lo'] - 0.05 * U, z['hi'])
    if near(zb, zt):
        r = z['lo'] - 0.10 * U if z['side'] == 'Demand-side' else z['hi'] + 0.10 * U
        print(f"  sweep zone     {z['side']:<11} {f(zb)}-{f(zt)} | sweep reach to {f(r)} (dotted box){' | confluent with a 4H BoM zone' if z.get('confluent_bom') else ''}")
for z in sorted(X['v1']['240']['liquidity'], key=lambda z: -z['top']):
    if near(z['bot'], z['top']):
        print(f"  liquidity band (sealed V1, 4H) {f(z['bot'])}-{f(z['top'])}")
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
