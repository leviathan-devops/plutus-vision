"""e1_pine.py - the tool's output: ONE Pine v6 script holding the week's Engine 1 map as data, in the form of trident_v8.pine (P533 Part X; colours C-19 of the approved render):
IP Resistance red / Equilibrium orange / IP Support teal (label = name, degree, ZFP range), LSZ green, option-strike targets amber, plus the supply/demand candles (4H) and the sealed V1's
order blocks + liquidity ladder as data (R-30), all inside the two-week window (R-36). E2 / E3 layers are added by their own modules.
usage: python3 e1_pine.py MONDAY PAIR > out.pine"""
import sys, json, os
import e1_data as D, e1_ip as IP, e1_v1 as V1

CAT = {'RES': '180,40,30', 'MID': '255,152,0', 'SUP': '0,150,150'}


def run(pair, monday):
    side = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sidecar', 'out', f'{monday}.json')))
    X = IP.build(pair, monday, side)
    X['v1'] = V1.harvest_all(pair, monday)
    return X


def generate(pair, monday, X):
    g = lambda v: ('%.3f' if pair == 'DXY' else '%.5f') % v
    b0, tsR = D.boundary_ms(monday), D.week_end_ms(monday)
    tsL, H = D.week_start_ms(monday) - 7 * 86400000, 3600000
    o = ['//@version=6', f'indicator("PLUTUS E1 {pair} {monday}", overlay=true, max_boxes_count=500, max_labels_count=500, max_lines_count=500)',
         f'// Engine 1 map, week of {monday} ({pair}); computed by e1_tool from data closed before the anchor {D.ts(b0)} UTC',
         'show_ip = input.bool(true, "IP Zones")', 'show_lsz = input.bool(true, "LSZ")', 'show_opt = input.bool(true, "Option Strikes")', 'show_sd = input.bool(true, "Supply / Demand (4H candles)")',
         'show_ob = input.bool(true, "V1 order blocks (data)")', 'show_lq = input.bool(true, "V1 liquidity ladder (data)")',
         f'isPair = str.contains(syminfo.ticker, "{D.SYM[pair].split("_")[-1]}")', 'if barstate.islast and isPair']
    o.append('    if show_lq')
    for z in X['v1']['60']['liquidity']:
        o.append(f"        box.new({tsL}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb(46,139,87), 55), border_color=color.new(color.rgb(63,164,106), 30), border_width=1, xloc=xloc.bar_time)")
    o.append('    if show_ob')
    for tf in ('240', '60', '30', '15'):
        for z in X['v1'][tf]['order_blocks']:
            c = '49,121,245' if z['side'] == 'Demand' else '247,124,128'
            o.append(f"        box.new({max(z['time'], tsL)}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({c}), 80), border_color=color.rgb({c}), border_width=1, xloc=xloc.bar_time)")
            o.append(f"        label.new({max(z['time'], tsL)}, {g(z['top'])}, \"{V1.TFNAME[tf]} {z['side']} OB\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.rgb({c}), size=size.small)")
    o.append('    if show_sd')
    for z in X['z4']:
        c = '49,121,245' if z['type'] == 'Demand' else '200,60,60'
        mit = 'Unmitigated' if z['mit'] == 0 else f"Mitigated {z['mit']}x"
        o.append(f"        box.new({max(z['origin_time'], tsL)}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({c}), 82), border_color=color.rgb({c}), border_width=2, xloc=xloc.bar_time)")
        o.append(f"        label.new({max(z['origin_time'], tsL) + 30 * H}, {g(z['top'])}, \"4H ({mit}) | {z['kind']}\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.white, size=size.small)")
    o.append('    if show_lsz')
    days = [d['date'] for d in X['daily'][-10:]]
    for z in X['lsz']:
        if z['swept'] and z['source'][-10:] < days[0]:
            continue
        act = z['priority'].startswith('ACTIVE')
        c = '80,230,100' if act else '40,180,80'
        o.append(f"        box.new({tsL}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({c}), {60 if act else 70}), border_color=color.rgb({c}), border_width={2 if act else 1}, xloc=xloc.bar_time)")
    o.append('    if show_ip')
    for z in X['zones']:
        if not z['drawn']:
            continue
        c = CAT[z['cat']]
        o.append(f"        // #{z['rank']} {z['name']} {g(z['bot'])}-{g(z['top'])} {z['degree']} {z['score']}/14 {z['type']} {z['tier']} | {z['mech']['bom']} {z['mech']['counter']} {z['mech']['reactions']} reactions | {z['mech']['e3_status']}")
        o.append(f"        box.new({tsL}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({c}), 70), border_color=color.rgb({c}), border_width=2, xloc=xloc.bar_time)")
        o.append(f"        label.new({tsL + 8 * H}, {g((z['top'] + z['bot']) / 2)}, \"{z['name']} | {z['degree']} | {z['zfp']} ZFP | {z['tier']} | {z['mech']['bom']} {z['mech']['reactions']}R\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.white, size=size.small)")
    o.append('    if show_opt')
    seen = set()
    for l in X['L']:
        if l['pillar'] == 8 and not l.get('expired') and g(l['p']) not in seen:
            seen.add(g(l['p']))
            amt = ('%.1fbn' % (l['notional_m'] / 1000)) if l['notional_m'] >= 1000 else '%dM' % l['notional_m']
            o.append(f"        line.new({tsL}, {g(l['p'])}, {tsR}, {g(l['p'])}, xloc=xloc.bar_time, color=color.rgb(255,200,60), width={2 if l['tier'] == 1 else 1})")
            o.append(f"        label.new({tsR - 30 * H}, {g(l['p'])}, \"{amt} Option Strike Target\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.rgb(255,200,60), size=size.small)")
    return '\n'.join(o) + '\n'


if __name__ == '__main__':
    monday, pair = sys.argv[1], sys.argv[2]
    sys.stdout.write(generate(pair, monday, run(pair, monday)))
