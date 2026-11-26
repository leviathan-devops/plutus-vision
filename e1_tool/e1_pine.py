"""e1_pine.py - the tool's output: ONE Pine v6 script holding the week's map as data, in the form of trident_v8.pine (P533 Part X; e1_tool/reference/trident_v8.pine :40-66, :346-387):
IP Resistance red / Equilibrium orange / IP Support teal by pressure tier (label = name | degree | ZFP range | tier), LSZ green boxes, option-strike targets amber lines.
On top of that the operator's own chart grammar (golden-week screenshots): supply / demand candle zones as red / blue boxes labelled "<TF> (Unmitigated) | BoM", the liquidity ladder as thin green rungs.
L-39: inside an IP zone the computed levels (pivots, moving averages, fibs, strikes, anchors) are drawn as thin lines so the data levels stay visible next to the candle structure.
R-36: window = the active week + one week left. Engine 2 / Engine 3 layers are appended by their modules through generate(..., extra=[...]).
usage: python3 e1_pine.py MONDAY PAIR > out.pine"""
import sys, json, os
import e1_data as D, e1_ip as IP, e1_v1 as V1

# trident_v8.pine :44-66 pressure-ladder colours
SHADE = {'RES': {'EXTREME': '180,40,30', 'HEAVY': '200,60,35', 'MODERATE-HEAVY': '210,80,40', 'MODERATE': '220,100,50', 'LIGHT': '230,130,60', 'MINIMAL': '240,160,90'},
         'MID': {'EXTREME': '255,152,0', 'HEAVY': '245,145,10', 'MODERATE-HEAVY': '235,138,20', 'MODERATE': '225,131,30', 'LIGHT': '215,124,40', 'MINIMAL': '205,117,50'},
         'SUP': {'EXTREME': '0,150,150', 'HEAVY': '0,170,160', 'MODERATE-HEAVY': '20,180,170', 'MODERATE': '40,190,180', 'LIGHT': '60,200,190', 'MINIMAL': '80,210,200'}}
LEVEL_COL = {1: '230,230,230', 2: '250,220,90', 5: '120,220,255', 6: '200,150,255', 8: '255,200,60'}      # pivots / moving averages / structural anchors / fib + round / strikes


def run(pair, monday):
    side = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sidecar', 'out', f'{monday}.json')))
    X = IP.build(pair, monday, side)
    X['v1'] = V1.harvest_all(pair, monday)
    return X


def reach(X, E2):
    """GS Law 2 / Law 7 ('for each day's predicted shape, determine the expected price travel range ... a zone 100 pips away is INVALID if the shape chain predicts consolidation near spot'),
    L-28 (no far floating zones): the week's reach = the envelope of the Engine 2 day map, extended to the first mapped zone beyond each end (what would stop the path next).
    Zones outside it stay in the script behind the toggle 'show_far' (nothing is deleted, R-37)."""
    days = [d for i, d in enumerate(E2['days']) if i < E2.get('n_real', 5)] or E2['days']
    lo, hi = min(d['lo'] for d in days), max(d['hi'] for d in days)
    zs = [z for z in X['zones'] if z['drawn']] + [z for z in X['sd'] if z['tf'] in ('240', '60')]
    below = [z for z in zs if z['top'] < lo]; above = [z for z in zs if z['bot'] > hi]
    if below:
        lo = max(below, key=lambda z: z['top'])['bot']
    if above:
        hi = min(above, key=lambda z: z['bot'])['top']
    # the alternative reading of every bound (6.6 Step 4: the chain that activates if the bound fails) has a target too: where a breakout through the ceiling / the floor would stop
    # (e2_chain.target) belongs to the week's reach, so the zone the week ends up trading at is on the chart when the primary chain is wrong (D-58)
    import e2_chain as E2M
    for side, bound in (('up', E2.get('ceil')), ('down', E2.get('floor'))):
        t = E2M.target(X, side, bound) if bound is not None else None
        if t is not None:
            lo, hi = min(lo, t['bot']), max(hi, t['top'])
    return lo, hi


def generate(pair, monday, X, extra=(), rch=None):
    g = lambda v: ('%.3f' if pair == 'DXY' else '%.5f') % v
    near = (lambda b, t: True) if rch is None else (lambda b, t: b <= rch[1] and t >= rch[0])
    b0, tsR, wk0 = D.boundary_ms(monday), D.week_end_ms(monday), D.week_start_ms(monday)
    tsL, H = wk0 - 7 * 86400000, 3600000
    U = X['U']; pw = X['weekly'][-1]
    adr = sum(d['high'] - d['low'] for d in X['daily'][-10:]) / 10
    lo_v, hi_v = pw['low'] - adr, pw['high'] + adr
    o = ['//@version=6', f'indicator("PLUTUS VISION {pair} {monday}", overlay=true, max_boxes_count=500, max_labels_count=500, max_lines_count=500)',
         f'// week of {monday} ({pair}); every number computed by e1_tool from data closed before the anchor {D.ts(b0)} UTC (Monday London open)',
         'show_ip = input.bool(true, "E1 IP Zones")', 'show_lv = input.bool(true, "E1 levels inside IP zones")', 'show_lsz = input.bool(true, "E1 LSZ")',
         'show_opt = input.bool(true, "E1 Option Strikes")', 'show_sd = input.bool(true, "E1 Supply / Demand 4H + 1H")', 'show_ltf = input.bool(false, "E1 Supply / Demand 30m + 15m")',
         'show_lq = input.bool(true, "E1 Liquidity ladder 1H (V1 data)")', 'show_lq4 = input.bool(true, "E1 Liquidity bands 4H (V1 data)")', 'show_ob = input.bool(false, "V1 order blocks (data)")',
         'show_far = input.bool(false, "E1 zones beyond this week\'s reach")',
         'show_e2 = input.bool(true, "E2 Shape chain")', 'show_e3 = input.bool(true, "E3 Trade setups")',
         f'isPair = str.contains(syminfo.ticker, "{D.SYM[pair].split("_")[-1]}")', 'if barstate.islast and isPair']
    # liquidity ladder: the sealed V1's 1H liquidity bands at the anchor (R-30), around the prior week's range (V1 itself draws the live ladder)
    o.append('    if show_lq')
    n0 = len(o)
    for z in X['v1']['60']['liquidity']:
        if lo_v <= z['bot'] and z['top'] <= hi_v:
            o.append(f"        box.new({tsL}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb(46,139,87), 70), border_color=color.new(color.rgb(63,164,106), 40), border_width=1, xloc=xloc.bar_time)")
    if len(o) == n0:
        o.append('        na')
    o.append('    if show_lq4')
    n0 = len(o)
    for z in X['v1']['240']['liquidity']:
        if lo_v <= z['bot'] and z['top'] <= hi_v and near(z['bot'], z['top']):
            o.append(f"        box.new({tsL}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb(46,139,87), 80), border_color=color.new(color.rgb(63,164,106), 30), border_width=1, xloc=xloc.bar_time)")
    if len(o) == n0:
        o.append('        na')
    o.append('    if show_ob')
    n0 = len(o)
    for tf in ('240', '60', '30', '15'):
        for z in X['v1'][tf]['order_blocks']:
            if lo_v <= z['bot'] and z['top'] <= hi_v:
                c = '49,121,245' if z['side'] == 'Demand' else '247,124,128'
                o.append(f"        box.new({max(z['time'], tsL)}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({c}), 85), border_color=color.new(color.rgb({c}), 30), border_width=1, border_style=line.style_dotted, xloc=xloc.bar_time)")
    if len(o) == n0:
        o.append('        na')
    # supply / demand candle zones (e1_sd): 4H + 1H on the working chart, 30m + 15m as the entry layer
    for flag, tfs, far in (('show_sd', ('240', '60'), False), ('show_sd and show_far', ('240', '60'), True), ('show_ltf', ('30', '15'), False), ('show_ltf and show_far', ('30', '15'), True)):
        o.append(f'    if {flag}')
        n0 = len(o)
        for z in X['sd']:
            if z['tf'] not in tfs or near(z['bot'], z['top']) == far:
                continue
            c = '41,98,255' if z['type'] == 'Demand' else '242,54,69'
            x0 = max(z['origin_time'], tsL)
            o.append(f"        box.new({x0}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({c}), {84 if z['tf'] in ('240', '60') else 90}), border_color=color.rgb({c}), border_width={2 if z['tf'] == '240' else 1}, xloc=xloc.bar_time)")
            o.append(f"        label.new({x0 + int((tsR - x0) * 0.30)}, {g((z['top'] + z['bot']) / 2)}, \"{z['label']}\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.white, size=size.small)")
        if len(o) == n0:
            o.append('        na')
    # liquidity sweep zones (P533:1246-1287): [low, low + 0.05] / [high - 0.05, high]; a swept extreme has no resting stops left
    for flag, far in (('show_lsz', False), ('show_lsz and show_far', True)):
      o.append(f'    if {flag}')
      n0 = len(o)
      for z in X['lsz']:
        if z['swept']:
            continue
        act = z['priority'].startswith('ACTIVE')
        c = '80,230,100' if act else '40,180,80'
        zb, zt = (z['level'], z['level'] + 0.05 * U) if z['side'] == 'Demand-side' else (z['level'] - 0.05 * U, z['level'])
        if near(zb, zt) == far:
            continue
        o.append(f"        box.new({tsL}, {g(zt)}, {tsR}, {g(zb)}, bgcolor=color.new(color.rgb({c}), {78 if act else 84}), border_color=color.rgb({c}), border_width={2 if act else 1}, xloc=xloc.bar_time)")
        # Step 0.45a (P533 'LSZ BOTTOM EDGE EXTENSION'): 'Institutions often sweep 0.05-0.10 beyond the visible extreme before reversing' - the sweep reach beyond the extreme, dotted
        xb, xt = (z['level'] - 0.10 * U, z['level']) if z['side'] == 'Demand-side' else (z['level'], z['level'] + 0.10 * U)
        o.append(f"        box.new({tsL}, {g(xt)}, {tsR}, {g(xb)}, bgcolor=color.new(color.rgb({c}), 100), border_color=color.new(color.rgb({c}), 30), border_width=1, border_style=line.style_dotted, xloc=xloc.bar_time)")
        o.append(f"        label.new({tsL + 24 * H}, {g((zt + zb) / 2)}, \"LSZ {'supply' if z['side'] == 'Supply-side' else 'demand'}-side{' + 4H BoM (confluent)' if z.get('confluent_bom') else ''} | sweep to {g(xt if z['side'] == 'Supply-side' else xb)}\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.rgb({c}), size=size.small)")
      if len(o) == n0:
        o.append('        na')
    # IP zones (the six ranked first), trident_v8 form
    for flag, far in (('show_ip', False), ('show_ip and show_far', True)):
      o.append(f'    if {flag}')
      n0 = len(o)
      for z in X['zones']:
        if not z['drawn'] or near(z['bot'], z['top']) == far:
            continue
        c = SHADE[z['cat']][z['degree']]
        o.append(f"        // #{z['rank']} {z['name']} {g(z['bot'])}-{g(z['top'])} {z['degree']} {z['score']}/14 {z['type']} {z['tier']} | {z['mech']['bom']} {z['mech']['counter']} {z['mech']['reactions']} reactions | {z['mech']['e3_status']}")
        o.append(f"        box.new({tsL}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({c}), 70), border_color=color.rgb({c}), border_width=2, xloc=xloc.bar_time)")
        o.append(f"        label.new({tsL + 60 * H}, {g((z['top'] + z['bot']) / 2)}, \"{z['name']} | {z['degree']} | {z['zfp']} ZFP | {z['tier']} {z['mech']['bom']}\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.white, size=size.small)")
      if len(o) == n0:
        o.append('        na')
    # Step 9.5 gap in-fill levels (P452:1159-1184): MODERATE confidence, drawn thinner than the named zones
    o.append('    if show_ip')
    n0 = len(o)
    for z in X.get('infill', []):
        if not near(z['bot'], z['top']):
            continue
        c = SHADE[z['cat']]['MODERATE']
        o.append(f"        box.new({tsL}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({c}), 82), border_color=color.new(color.rgb({c}), 20), border_width=1, border_style=line.style_dashed, xloc=xloc.bar_time)")
        o.append(f"        label.new({tsL + 96 * H}, {g((z['top'] + z['bot']) / 2)}, \"GAP IN-FILL | MODERATE | {z['zfp']} ZFP\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.white, size=size.small)")
    if len(o) == n0:
        o.append('        na')
    o.append('    if show_ip and show_lv')
    n0 = len(o)
    for z in X['zones']:
        if not z['drawn'] or not near(z['bot'], z['top']):
            continue
        seen = set()
        for l in z['members_lv']:
            if l['pillar'] == 8 or l.get('legacy') or g(l['p']) in seen:
                continue
            seen.add(g(l['p']))
            o.append(f"        line.new({wk0}, {g(l['p'])}, {tsR}, {g(l['p'])}, xloc=xloc.bar_time, color=color.new(color.rgb({LEVEL_COL.get(l['pillar'], '200,200,200')}), 35), width=1, style=line.style_dotted)   // {l['kind'][:60]}")
    if len(o) == n0:
        o.append('        na')
    # live option-strike targets (trident_v8 :377-386)
    o.append('    if show_opt')
    n0 = len(o)
    seen = set()
    for l in sorted(X['L'], key=lambda l: -l.get('notional_m', 0)):
        if l['pillar'] == 8 and not l.get('expired') and g(l['p']) not in seen and near(l['p'], l['p']):
            seen.add(g(l['p']))
            amt = ('%.1fbn' % (l['notional_m'] / 1000)) if l['notional_m'] >= 1000 else '%dM' % l['notional_m']
            o.append(f"        line.new({tsL}, {g(l['p'])}, {tsR}, {g(l['p'])}, xloc=xloc.bar_time, color=color.rgb(255,200,60), width={2 if l['tier'] == 1 else 1})")
            o.append(f"        label.new({tsR - 44 * H}, {g(l['p'])}, \"{amt} Option Strike Target\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.rgb(255,200,60), size=size.small)")
    if len(o) == n0:
        o.append('        na')
    o += list(extra)
    return '\n'.join(o) + '\n'


if __name__ == '__main__':
    monday, pair = sys.argv[1], sys.argv[2]
    sys.stdout.write(generate(pair, monday, run(pair, monday)))
