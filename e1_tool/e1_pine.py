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


REACH_MM = False        # D-105: the measured-move reach (D-93) put zones 60-130 pips beyond the week on 12 of 12 maps (outside count 8, 'floating'); the reach is the E2 envelope + the first zone beyond each end
JOIN_D = 0.05            # D-105: an Engine 1 object within 0.05 of a higher-ranking zone is a PART of it (P533 Step 0.5a 'within 0.05 DXY points of each other, they are a "repeated level"'; zone assembly step 4 groups levels within 0.10-0.15; L-39 joined zone)
LSZ_BOX = 0.05           # D-105: the sweep zone BOX as the operator's reference script draws it (trident_v8.pine: every LSZ 0.05 tall; P533 0.45 [low, low + 0.05]); the 0.10 scan of Step 0.45a stays Engine 2's bound and the dotted reach


def reach(X, E2):
    """GS Law 2 / Law 7 ('for each day's predicted shape, determine the expected price travel range ... a zone 100 pips away is INVALID if the shape chain predicts consolidation near spot'),
    L-28 (no far floating zones): the week's reach = the envelope of the Engine 2 day map, extended to the first mapped zone beyond each end (what would stop the path next).
    Zones outside it stay in the script behind the toggle 'show_far' (nothing is deleted, R-37)."""
    days = [d for i, d in enumerate(E2['days']) if i < E2.get('n_real', 5)] or E2['days']
    lo, hi = min(d['lo'] for d in days), max(d['hi'] for d in days)
    zs = [z for z in X['zones'] if z['drawn']] + [z for z in X['sd'] if z['tf'] in ('240', '60')]
    # ... the first zone beyond each end, when it stands within the swing-scalp reach of that end (GS Law 2: 30 pips): a zone further out is not 'what would stop the path next'
    # this week - it floated 34-67 pips beyond the week on five maps of outside count 10 (D-113)
    R30 = 0.30 * X['U']
    lo0, hi0 = lo, hi
    below = [z for z in zs if z['top'] < lo and lo - z['top'] <= R30]; above = [z for z in zs if z['bot'] > hi and z['bot'] - hi <= R30]
    if below:
        lo = max(below, key=lambda z: z['top'])['bot']
    if above:
        hi = min(above, key=lambda z: z['bot'])['top']
    # the alternative reading of every bound (6.6 Step 4: the chain that activates if the bound fails) has a target too: where a breakout through the ceiling / the floor would stop
    # (e2_chain.target) belongs to the week's reach, so the zone the week ends up trading at is on the chart when the primary chain is wrong (D-58)
    import e2_chain as E2M
    for side, bound, other in (('up', E2.get('ceil'), E2.get('floor')), ('down', E2.get('floor'), E2.get('ceil'))):
        t = E2M.target(X, side, bound) if bound is not None else None
        if t is not None:                                    # the alternative chain's target is where its conditional orders end (D-109 / D-110): it stays on the chart at any distance
            lo, hi = min(lo, t['bot']), max(hi, t['top'])
        # ... and its magnitude: 6.5 'BS | Failing zone triggers BS; target zone determines magnitude | Target: Measured Move' (P452 Pillar 9 Step 4: the range height projected from the
        # failing bound): the week's reach runs to the measured-move target of each bound and to the mapped zone standing at / first beyond it (D-87)
        m = E2M.measured_move(X, bound, other, side) if (bound is not None and other is not None and REACH_MM) else None
        if m is not None:
            if side == 'up':
                hi = max(hi, m['top'])
                at = [z for z in zs if z['bot'] <= hi <= z['top']] or sorted([z for z in zs if z['bot'] > hi], key=lambda z: z['bot'])[:1]
                hi = max([hi] + [z['top'] for z in at if z['bot'] - hi <= 0.30 * X['U']])
            else:
                lo = min(lo, m['bot'])
                at = [z for z in zs if z['bot'] <= lo <= z['top']] or sorted([z for z in zs if z['top'] < lo], key=lambda z: -z['top'])[:1]
                lo = min([lo] + [z['bot'] for z in at if lo - z['top'] <= 0.30 * X['U']])
    # an end of the reach with no mapped zone beyond it (the open side after a trend): the first discovery flag beyond that end is what the map offers there (P452:1220-1228) (D-103)
    dz = X.get('discovery', [])
    if not [z for z in zs if z['top'] < lo]:
        b_ = [z for z in dz if z['top'] < lo and lo - z['top'] <= R30]
        if b_:
            lo = max(b_, key=lambda z: z['top'])['bot']
    if not [z for z in zs if z['bot'] > hi]:
        a_ = [z for z in dz if z['bot'] > hi and z['bot'] - hi <= R30]
        if a_:
            hi = min(a_, key=lambda z: z['bot'])['top']
    return lo, hi


def e2_band(X, z):
    """a V1 4H liquidity band that Engine 2 designates (a range bound, the pivot, a target): the day box rests on it, so it is drawn (D-107)"""
    return any(abs(z['bot'] - b) < 1e-9 and abs(z['top'] - t) < 1e-9 for b, t in X.get('e2_zones', []))


def discovery_drawn(X, near, sweeps):
    """the discovery flags shown: inside the chart window and not on a drawn supply / demand zone, sweep zone or 4H liquidity band (the flag marks EMPTY map, P452:1224)"""
    solid = [z for z in X['sd'] if z['tf'] in ('240', '60')] + list(sweeps) + [z for z in X['zones'] if z['drawn']] + list(X.get('infill', []))
    joined, _ = join_zones(X, near, sweeps)
    solid += [b for b in X['v1']['240']['liquidity'] if id(b) in joined or e2_band(X, b)]      # a flag inside a drawn part is not 'empty map' (outside count 10)
    EX = 0.03 * X['U']
    return [z for z in X.get('discovery', []) if near(z['bot'], z['top']) and not any(q['bot'] - EX <= z['top'] and q['top'] + EX >= z['bot'] for q in solid)]


def sweep_boxes(X):
    """sweep zones as drawn: those of one side within 0.05 of each other are ONE cluster of stops (P533 Step 0.5a 'within 0.05 DXY points of each other, they are a "repeated level"')"""
    U = X['U']
    merged = []
    for z in sorted([z for z in X['lsz'] if not z['swept']], key=lambda z: (z['side'], z['level'])):
        if merged and merged[-1]['side'] == z['side'] and z['level'] - merged[-1]['hi'] <= 0.05 * U + 1e-12:
            merged[-1]['hi'] = z['level']; merged[-1]['n'] += 1
            merged[-1]['priority'] = 'ACTIVE' if (merged[-1]['priority'].startswith('ACTIVE') or z['priority'].startswith('ACTIVE')) else z['priority']
            merged[-1]['confluent_bom'] = merged[-1].get('confluent_bom') or z.get('confluent_bom')
        else:
            merged.append(dict(z, lo=z['level'], hi=z['level'], n=1))
    for z in merged:
        z['bot'], z['top'] = (z['lo'], z['hi'] + LSZ_BOX * U) if z['side'] == 'Demand-side' else (z['lo'] - LSZ_BOX * U, z['hi'])
    return merged


def join_zones(X, near, sweeps):
    """L-39 (operator): 'a pressure zone = candle structure + level cluster JOINED ... inside it the two parts stay visibly distinct'. Every Engine 1 object that overlaps a higher-ranking
    one is drawn as a PART of it (light, dotted, unlabelled) and named in that zone's label; rank: pressure zone > 4H supply/demand > 1H supply/demand > gap in-fill > sweep zone > 4H liquidity
    band. A part joins the leader it overlaps directly (no chains: a joined zone never grows beyond its leader and its own parts). Returns {id(obj): leader} and {id(leader): [part names]}"""
    objs = [(0, z, 'IP') for z in X['zones'] if z['drawn'] and near(z['bot'], z['top'])]
    objs += [(1 if z['tf'] == '240' else 2, z, ('4H ' if z['tf'] == '240' else '1H ') + z['type'].lower()) for z in X['sd'] if z['tf'] in ('240', '60') and near(z['bot'], z['top'])]
    objs += [(3, z, 'in-fill') for z in X.get('infill', []) if near(z['bot'], z['top'])]
    objs += [(4, z, 'sweep zone') for z in sweeps if near(z['bot'], z['top'])]
    objs += [(5, z, '4H liquidity') for z in X['v1']['240']['liquidity'] if near(z['bot'], z['top'])]
    leaders, joined, parts = [], {}, {}
    for rank, z, nm in sorted(objs, key=lambda o: (o[0], o[1]['bot'])):
        JD = JOIN_D * X['U']
        # ... also a zone of the SAME rank (two 1H candle zones or two sweep clusters a pip apart are one zone on the chart: L-28 'three supports bunched'; outside count 10)
        cl = [l for r, l in leaders if r <= rank and l is not z and l['bot'] - JD <= z['top'] and l['top'] + JD >= z['bot']]
        L = min(cl, key=lambda l: max(l['bot'] - z['top'], z['bot'] - l['top'], 0.0)) if cl else None      # the nearest higher-ranking zone within the join distance
        if L is not None:
            joined[id(z)] = L
            if nm not in parts.setdefault(id(L), []):
                parts[id(L)].append(nm)
        else:
            leaders.append((rank, z))
    return joined, parts


def generate(pair, monday, X, extra=(), rch=None):
    g = lambda v: ('%.3f' if pair == 'DXY' else '%.5f') % v
    near = (lambda b, t: True) if rch is None else (lambda b, t: b <= rch[1] and t >= rch[0])
    b0, tsR, wk0 = D.boundary_ms(monday), D.week_end_ms(monday), D.week_start_ms(monday)
    tsL, H = wk0 - 7 * 86400000, 3600000
    # a zone label (label.style_none) is drawn by Pinebox with its text STARTING at the label's point (evidence/chk97, chk99; ledger 99b): the point stands the text's width - counted in
    # 1H BARS, the weekend holds none - before the week start, so the text ENDS before the forecast week's candles (A13 'labels over candles'; outside counts 9 / 10). Width of a
    # size.small character on the two-week 1H frame = about 1.65 bars (measured on evidence/chk100). A right-anchored style is not used - Pinebox draws label.style_label_right to the
    # right of its point too (evidence/chk98)
    _hb = [x_['time'] for x_ in D.closed(pair, '60', monday) if x_['time'] < wk0 - 2 * H]
    lab_x = lambda t: (_hb[max(0, len(_hb) - 2 - int(1.65 * max(len(q_) for q_ in t.split('\\n'))))] if _hb else tsL + 2 * H)
    def lab2(t):
        # a label too long to stand inside the prior week on one line is written on two (split at the ' | ' nearest its middle): its name stays readable instead of being cut by the
        # window's left edge (ledger 103b)
        if len(t) <= 56 or ' | ' not in t:
            return t
        cuts = [i for i in range(len(t)) if t.startswith(' | ', i)]
        c = min(cuts, key=lambda i: abs(i - len(t) / 2))
        return t[:c] + '\\n' + t[c + 3:]
    U = X['U']; pw = X['weekly'][-1]
    sweeps = sweep_boxes(X)
    joined, parts = join_zones(X, near, sweeps)
    # the parts are named in short form (the legend: S = supply zone, D = demand zone, LSZ = sweep zone, LQ = V1 4H liquidity band, IF = gap in-fill) so that a zone's label stays inside the
    # history half of the chart (A13 'labels over candles'; outside counts 8 / 9)
    SHORT = {'4H supply': '4H S', '4H demand': '4H D', '1H supply': '1H S', '1H demand': '1H D', 'sweep zone': 'LSZ', '4H liquidity': 'LQ', 'in-fill': 'IF'}
    plus = lambda z: (' + ' + ', '.join(SHORT.get(n, n) for n in parts[id(z)])) if parts.get(id(z)) else ''
    adr = sum(d['high'] - d['low'] for d in X['daily'][-10:]) / 10
    lo_v, hi_v = pw['low'] - adr, pw['high'] + adr
    o = ['//@version=6', f'indicator("PLUTUS VISION {pair} {monday}", overlay=true, max_boxes_count=2000, max_labels_count=2000, max_lines_count=2000)',      # PG6 (P533:3909)
         f'// week of {monday} ({pair}); every number computed by e1_tool from data closed before the anchor {D.ts(b0)} UTC (Monday London open)',
         'show_ip = input.bool(true, "E1 IP Zones")', 'show_disc = input.bool(true, "E1 Discovery Zones (levels to watch)")', 'show_lv = input.bool(true, "E1 levels inside IP zones")', 'show_lsz = input.bool(true, "E1 LSZ")',
         'show_opt = input.bool(true, "E1 Option Strikes")', 'show_sd = input.bool(true, "E1 Supply / Demand 4H + 1H")', 'show_ltf = input.bool(false, "E1 Supply / Demand 30m + 15m")',
         'show_lq = input.bool(true, "E1 Liquidity ladder 1H (V1 data)")', 'show_lq4 = input.bool(true, "E1 Liquidity bands 4H (V1 data)")', 'show_ob = input.bool(false, "V1 order blocks (data)")',
         'show_far = input.bool(false, "E1 zones beyond this week\'s reach")', 'show_v1s = input.bool(false, "V1 4H liquidity bands standing alone (the sealed V1 draws them)")',
         'show_e2 = input.bool(true, "E2 Shape chain")', 'show_e3 = input.bool(true, "E3 Trade setups")', 'show_tbl = input.bool(true, "Info Table")',
         f'isPair = str.contains(syminfo.ticker, "{D.SYM[pair].split("_")[-1]}")', 'if barstate.islast and isPair']
    # liquidity ladder: the sealed V1's 1H liquidity bands at the anchor (R-30), around the prior week's range (V1 itself draws the live ladder)
    o.append('    if show_lq')
    n0 = len(o)
    for z in X['v1']['60']['liquidity']:
        if lo_v <= z['bot'] and z['top'] <= hi_v:
            o.append(f"        box.new({tsL}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb(46,139,87), 70), border_color=color.new(color.rgb(63,164,106), 40), border_width=1, xloc=xloc.bar_time)")
    if len(o) == n0:
        o.append('        na')
    # a 4H liquidity band of the sealed V1 is drawn by this script only as a PART of an Engine 1 zone; standing alone it is the sealed V1's own drawing underneath (goal prompt 4b: 'E1 = (a) the
    # sealed V1 underneath: order blocks + the liquidity ladder') and sits behind the toggle show_v1s (D-105)
    for flag, alone in (('show_lq4', False), ('show_lq4 and show_v1s', True)):
        o.append('    if ' + flag)
        n0 = len(o)
        for z in X['v1']['240']['liquidity']:
            if lo_v <= z['bot'] and z['top'] <= hi_v and near(z['bot'], z['top']) and (id(z) not in joined and not e2_band(X, z)) == alone:
                if id(z) in joined:
                    o.append(f"        box.new({tsL}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb(46,139,87), 94), border_color=color.new(color.rgb(63,164,106), 60), border_width=1, border_style=line.style_dotted, xloc=xloc.bar_time)")
                else:
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
    n_sd = n_lz = 0
    for flag, tfs, far in (('show_sd', ('240', '60'), False), ('show_sd and show_far', ('240', '60'), True), ('show_ltf', ('30', '15'), False), ('show_ltf and show_far', ('30', '15'), True)):
        o.append(f'    if {flag}')
        n0 = len(o)
        for z in X['sd']:
            if z['tf'] not in tfs or near(z['bot'], z['top']) == far:
                continue
            c = '41,98,255' if z['type'] == 'Demand' else '242,54,69'
            x0 = max(z['origin_time'], tsL)
            if id(z) in joined:
                o.append(f"        box.new({x0}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({c}), 93), border_color=color.new(color.rgb({c}), 45), border_width=1, border_style=line.style_dotted, xloc=xloc.bar_time)")
                continue
            o.append(f"        box.new({x0}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({c}), {84 if z['tf'] in ('240', '60') else 90}), border_color=color.rgb({c}), border_width={2 if z['tf'] == '240' else 1}, xloc=xloc.bar_time)")
            n_sd += 1                                    # labels of stacked zones alternate between three columns so they do not print on one spot (A13)
            o.append(f"        label.new({min(max(x0, tsL + (30 + 34 * (n_sd % 3)) * H), lab_x(z['label'] + plus(z)))}, {g((z['top'] + z['bot']) / 2)}, \"{z['label']}{plus(z)}\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.white, size=size.small)")
        if len(o) == n0:
            o.append('        na')
    # liquidity sweep zones (P533:1246-1287): [low, low + 0.05] / [high - 0.05, high]; a swept extreme has no resting stops left
    for flag, far in (('show_lsz', False), ('show_lsz and show_far', True)):
      o.append(f'    if {flag}')
      n0 = len(o)
      for z in sweeps:
        act = z['priority'].startswith('ACTIVE')
        c = '80,230,100' if act else '40,180,80'
        zb, zt = (z['lo'], z['hi'] + 0.05 * U) if z['side'] == 'Demand-side' else (z['lo'] - 0.05 * U, z['hi'])
        if near(zb, zt) == far:
            continue
        part = id(z) in joined                               # a sweep zone lying on a higher-ranking zone is that zone's liquidity part (L-39): light, dotted, no label of its own
        if part:
            o.append(f"        box.new({tsL}, {g(zt)}, {tsR}, {g(zb)}, bgcolor=color.new(color.rgb({c}), 92), border_color=color.new(color.rgb({c}), 45), border_width=1, border_style=line.style_dotted, xloc=xloc.bar_time)")
        else:
            o.append(f"        box.new({tsL}, {g(zt)}, {tsR}, {g(zb)}, bgcolor=color.new(color.rgb({c}), {78 if act else 84}), border_color=color.rgb({c}), border_width={2 if act else 1}, xloc=xloc.bar_time)")
        # Step 0.45a (P533 'LSZ BOTTOM EDGE EXTENSION'): 'Institutions often sweep 0.05-0.10 beyond the visible extreme before reversing' - the sweep reach beyond the extreme, dotted
        xb, xt = (z['lo'] - 0.10 * U, z['lo']) if z['side'] == 'Demand-side' else (z['hi'], z['hi'] + 0.10 * U)
        o.append(f"        box.new({tsL}, {g(xt)}, {tsR}, {g(xb)}, bgcolor=color.new(color.rgb({c}), 100), border_color=color.new(color.rgb({c}), 30), border_width=1, border_style=line.style_dotted, xloc=xloc.bar_time)")
        if part:
            continue
        n_lz += 1
        txt_ = f"LSZ {'supply' if z['side'] == 'Supply-side' else 'demand'}-side{' + 4H BoM (confluent)' if z.get('confluent_bom') else ''} | sweep to {g(xt if z['side'] == 'Supply-side' else xb)}{plus(z)}"
        o.append(f"        label.new({min(tsL + (8 + 40 * (n_lz % 3)) * H, lab_x(txt_))}, {g((zt + zb) / 2)}, \"{txt_}\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.rgb({c}), size=size.small)")
      if len(o) == n0:
        o.append('        na')
    # IP zones (the six ranked first), trident_v8 form
    # Engine 1 post-processing lines of the report, carried as comments: Step 9.8 re-verification (P533:1516-1527) + Tier 3 override audit trail (P533:1142), Step 5.5 core / spike of the
    # KEY SUPPORT BANDs (P533:1411-1423), Part IV 4.2 recommended stop-loss zones of the critical option walls (P452:1453-1458)
    o.append(f"    // {X.get('reverify', '')}")
    for a_ in X.get('overrides', []):
        o.append(f"    // {a_}")
    for z in X['zones']:
        if z.get('core_line'):
            o.append(f"    // {z['core_line']}")
    for q_ in X.get('sl_zones', []):
        o.append(f"    // {q_['line']}")
    for flag, far in (('show_ip', False), ('show_ip and show_far', True)):
      o.append(f'    if {flag}')
      n0 = len(o)
      for z in X['zones']:
        if not z['drawn'] or near(z['bot'], z['top']) == far:
            continue
        c = SHADE[z['cat']][z['degree']]
        o.append(f"        // #{z['rank']} {z['name']} {g(z['bot'])}-{g(z['top'])} {z['degree']} {z['score']}/14 {z['type']} {z['tier']} | {z['mech']['bom']} {z['mech']['counter']} {z['mech']['reactions']} reactions | {z['mech']['e3_status']}")
        o.append(f"        box.new({tsL}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({c}), 70), border_color=color.rgb({c}), border_width=2, xloc=xloc.bar_time)")
        txt_ = lab2(f"{z['name']} | {z['degree']} | {z['zfp']} ZFP | {z['tier']} {z['mech']['bom']}{plus(z)}")
        o.append(f"        label.new({lab_x(txt_)}, {g((z['top'] + z['bot']) / 2)}, \"{txt_}\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.white, size=size.small)")
      if len(o) == n0:
        o.append('        na')
    # Step 9.5 gap in-fill levels (P452:1159-1184): MODERATE confidence, drawn thinner than the named zones
    o.append('    if show_ip')
    n0 = len(o)
    for z in X.get('infill', []):
        if not near(z['bot'], z['top']):
            continue
        c = SHADE[z['cat']]['MODERATE']
        if id(z) in joined:
            o.append(f"        box.new({tsL}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({c}), 93), border_color=color.new(color.rgb({c}), 50), border_width=1, border_style=line.style_dotted, xloc=xloc.bar_time)")
            continue
        o.append(f"        box.new({tsL}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({c}), 82), border_color=color.new(color.rgb({c}), 20), border_width=1, border_style=line.style_dashed, xloc=xloc.bar_time)")
        txt_ = f"GAP IN-FILL | MODERATE | {z['zfp']} ZFP{plus(z)}"
        o.append(f"        label.new({lab_x(txt_)}, {g((z['top'] + z['bot']) / 2)}, \"{txt_}\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.white, size=size.small)")
    if len(o) == n0:
        o.append('        na')
    # DYNAMIC DISCOVERY PROTOCOL (P452:1220-1228): the pre-week flags where the map is empty - 'level to watch', NEUTRAL (P533:3448): a thin dashed neutral line, small label (D-103)
    o.append('    if show_disc')
    n0 = len(o)
    for z in discovery_drawn(X, near, sweeps):
        if z['top'] - z['bot'] > 1e-9:
            o.append(f"        box.new({b0 - 48 * H}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb(200,200,200), 92), border_color=color.new(color.rgb(200,200,200), 45), border_width=1, border_style=line.style_dashed, xloc=xloc.bar_time)")
        else:
            o.append(f"        line.new({b0 - 48 * H}, {g(z['p'])}, {tsR}, {g(z['p'])}, xloc=xloc.bar_time, color=color.new(color.rgb(200,200,200), 35), style=line.style_dashed, width=1)")
        o.append(f"        label.new({min(b0 - 30 * H, lab_x('DISCOVERY ZONE | ' + ' + '.join(z['flags'])))}, {g(z['top'])}, \"DISCOVERY ZONE | {' + '.join(z['flags'])}\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.new(color.rgb(200,200,200), 10), size=size.tiny)")
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
    seen, put = set(), []
    for l in sorted(X['L'], key=lambda l: -l.get('notional_m', 0)):
        if l['pillar'] == 8 and not l.get('expired') and g(l['p']) not in seen and near(l['p'], l['p']):
            seen.add(g(l['p']))
            amt = ('%.1fbn' % (l['notional_m'] / 1000)) if l['notional_m'] >= 1000 else '%dM' % l['notional_m']
            o.append(f"        line.new({tsL}, {g(l['p'])}, {tsR}, {g(l['p'])}, xloc=xloc.bar_time, color=color.rgb(255,200,60), width={2 if l['tier'] == 1 else 1})")
            k = sum(1 for q in put if abs(q - l['p']) < 0.06 * U)        # strike lines a few pips apart: their labels step left so they do not print over each other (A13)
            put.append(l['p'])
            o.append(f"        label.new({tsR - (44 + 62 * k) * H}, {g(l['p'])}, \"{amt} Option Strike Target\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.rgb(255,200,60), size=size.small)")
    if len(o) == n0:
        o.append('        na')
    o += list(extra)
    return '\n'.join(o) + '\n'


if __name__ == '__main__':
    monday, pair = sys.argv[1], sys.argv[2]
    sys.stdout.write(generate(pair, monday, run(pair, monday)))
