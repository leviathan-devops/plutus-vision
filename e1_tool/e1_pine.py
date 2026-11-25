"""e1_pine.py - the tool's output: a Pine script holding one week's Engine 1 map as data, in the form of trident_v8.pine
(IP Resistance red / Equilibrium orange / IP Support teal, LSZ green boxes, option strike targets amber lines) plus ruling L-39:
inside each pressure zone the candle structure (A) and every computed level (B) stay visible and colour-coded.
usage: python3 e1_pine.py MONDAY PAIR [K] > out.pine"""
import sys, json, os
import e1_data as D, e1_pillars as P, e1_zones as Z
import e2_shapes as E2

CAT = {'RES': (180, 40, 30), 'MID': (255, 152, 0), 'SUP': (0, 150, 150)}
PIL = {'P1': ('100,150,255', 'pivot'), 'P2': ('190,120,255', 'MA'), 'P5': ('235,235,235', 'structure'), 'P6': ('150,150,150', 'fib/round'), 'P8': ('255,200,60', 'option')}


def vol(m):
    return ('%.1fbn' % (m / 1000)) if m >= 1000 else '%dM' % m


def generate(pair, monday, r):
    f = '%.2f' if pair == 'DXY' else '%.4f'
    g = lambda v: f % v
    b0 = D.boundary_ms(monday)
    tsL, tsR, tsLab = b0 - 7 * 86400000, b0 + 7 * 86400000, b0 - 3 * 86400000      # zone labels sit left of the week so the week itself stays clear for E2 / E3
    o = ['//@version=6', f'indicator("TRIDENT E1 {pair} {monday}", overlay=true, max_boxes_count=500, max_labels_count=500, max_lines_count=500)',
         f'// Engine 1 map for the week of {monday} ({pair}); every number below was computed by e1_tool from data closed before the boundary {D.ts(b0)} UTC',
         'show_zones = input.bool(true, "IP Zones")', 'show_candles = input.bool(true, "Candle structures (A)")', 'show_levels = input.bool(true, "Computed levels (B)")',
         'show_lsz = input.bool(true, "LSZ")', 'show_e2 = input.bool(true, "E2 shape chain")', 'show_e3 = input.bool(true, "E3 trade setups")', 'show_infill = input.bool(true, "Gap in-fill levels")', 'show_options = input.bool(true, "Option Strikes")',
         f'isPair = str.contains(syminfo.ticker, "{D.SYM[pair].split("_")[-1]}")', 'if barstate.islast and isPair']
    for z in r['zones']:
        c = '%d,%d,%d' % CAT[z['cat']]
        o.append(f"    // {z['name']} {g(z['bot'])}-{g(z['top'])} {z['degree']} {z['score']}/14 {z['type']} ZFP {z['zfp']} {z['tier']}")
        o.append('    if show_zones')
        o.append(f"        box.new({tsL}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({c}), 80), border_color=color.rgb({c}), border_width=2, xloc=xloc.bar_time)")
        lbl = f"{z['name'].title()} | {z['degree']} | {z['zfp']} ZFP | {z['tier'].split(':')[0]}"
        o.append(f'        label.new({tsLab}, {g(z["top"])}, "{lbl}", xloc=xloc.bar_time, style=label.style_none, textcolor=color.white, size=size.normal)')
        if z['structs']:
            o.append('    if show_candles')
            for s in z['structs']:
                o.append(f"        box.new({s['origin_time']}, {g(s['top'])}, {tsR}, {g(s['bot'])}, bgcolor=color.new(color.rgb({c}), 55), border_color=color.white, border_width=1, border_style=line.style_dashed, xloc=xloc.bar_time)")
                o.append(f"        label.new({s['origin_time']}, {g(s['top'])}, \"{s['tf']} {s['kind']} {s['type']} {s['mit']}X\", xloc=xloc.bar_time, style=label.style_label_down, color=color.new(color.black, 30), textcolor=color.white, size=size.small)")
        o.append('    if show_levels')
        seen = set()
        for x in z['levels']:
            key = (g(x['p']), x['pillar'])
            if key in seen or x['dim'] == 'opt':
                continue
            seen.add(key)
            o.append(f"        line.new({b0}, {g(x['p'])}, {tsR}, {g(x['p'])}, xloc=xloc.bar_time, color=color.new(color.rgb({PIL[x['pillar']][0]}), 35), width=1, style=line.style_dotted)")
    if r['infill']:
        o.append('    if show_infill')
        for t in r['infill']:
            c = '%d,%d,%d' % CAT[t['cat']]
            o.append(f"        box.new({b0}, {g(t['top'])}, {tsR}, {g(t['bot'])}, bgcolor=color.new(color.rgb({c}), 85), border_color=color.new(color.rgb({c}), 20), border_width=1, border_style=line.style_dashed, xloc=xloc.bar_time)")
            o.append(f"        label.new({b0 + 4 * 86400000}, {g(t['top'])}, \"Gap In-fill | MODERATE | {' + '.join(t['signals'])}\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.new(color.white, 25), size=size.small)")
    if r['lsz']:
        o.append('    if show_lsz')
    for z in r['lsz']:
        act = z['priority'].startswith('ACTIVE')
        col = '80,230,100' if act else '40,180,80'
        o.append(f"        box.new({tsL}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({col}), {60 if act else 70}), border_color=color.rgb({col}), border_width={2 if act else 1}, xloc=xloc.bar_time)")
    opts = [x for x in r['levels'] if x['dim'] == 'opt' and x['tier'] <= 2 and not x.get('ghost')]
    if opts:
        o.append('    if show_options')
    n = 0
    for x in r['levels']:
        if x['dim'] == 'opt' and x['tier'] <= 2 and not x.get('ghost'):
            n += 1
            o.append(f"        line.new({tsL}, {g(x['p'])}, {tsR}, {g(x['p'])}, xloc=xloc.bar_time, color=color.rgb(255,200,60), width={2 if x['notional_m'] >= 1000 else 1})")
            o.append(f"        label.new({b0 + (5 + n % 2) * 86400000}, {g(x['p'])}, \"{vol(x['notional_m'])} Option Strike Target\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.rgb(255,200,60), size=size.small)")
    # ── ENGINE 2: macro shape chain, day by day (P533 6.6 Step 5, 6.9): projected path + day labels
    e2 = r.get('e2')
    if e2:
        o.append('    if show_e2')
        o.append(f'        // PRIMARY: {e2["primary"]} | {e2["alternative"]}')
        for d in e2.get('alt_days', []):
            for (ta, pa), (tb, pb) in zip(d['path'], d['path'][1:]):
                o.append(f"        line.new({ta}, {g(pa)}, {tb}, {g(pb)}, xloc=xloc.bar_time, color=color.new(color.rgb(170,170,190), 45), width=1, style=line.style_dashed)")
        for d in e2['days']:
            for (ta, pa), (tb, pb) in zip(d['path'], d['path'][1:]):
                o.append(f"        line.new({ta}, {g(pa)}, {tb}, {g(pb)}, xloc=xloc.bar_time, color=color.new(color.white, 10), width=2, style=line.style_dashed)")
            top = max(p for _, p in d['path'])
            txt = d['day'] + ': ' + d['shape'] + ('' if d['dir'] == 'range' else ' ' + d['dir'])
            o.append(f"        label.new({(d['t0'] + d['t1']) // 2}, {g(top)}, \"{txt}\", xloc=xloc.bar_time, style=label.style_label_down, color=color.new(color.rgb(40,60,120), 10), textcolor=color.white, size=size.normal)")
            o.append(f"        line.new({d['t0']}, {g(top)}, {d['t0']}, {g(min(p for _, p in d['path']))}, xloc=xloc.bar_time, color=color.new(color.white, 70), width=1, style=line.style_dotted, extend=extend.both)")
    # ── ENGINE 3: trade setups (entry / SL / TP), each on its E2 day
    if r.get('e3'):
        o.append('    if show_e3')
        for t in r['e3']:
            tE = min(tsR, t['t0'] + 2 * 86400000)
            o.append(f"        box.new({t['t0']}, {g(max(t['entry'], t['tp']))}, {tE}, {g(min(t['entry'], t['tp']))}, bgcolor=color.new(color.rgb(60,200,90), 88), border_color=color.new(color.rgb(60,200,90), 30), border_width=1, xloc=xloc.bar_time)")
            o.append(f"        box.new({t['t0']}, {g(max(t['entry'], t['sl']))}, {tE}, {g(min(t['entry'], t['sl']))}, bgcolor=color.new(color.rgb(230,60,60), 80), border_color=color.new(color.rgb(230,60,60), 30), border_width=1, xloc=xloc.bar_time)")
            o.append(f"        line.new({t['t0']}, {g(t['entry'])}, {tE}, {g(t['entry'])}, xloc=xloc.bar_time, color=color.rgb(90,160,255), width=2)")
            txt = f"#{t['n']} {t['day']} {t['session']} {t['dir']} {t['shape']}{'' if t['branch'] == 'PRIMARY' else ' (ALT)'} | E {g(t['entry'])} SL {g(t['sl'])} TP {g(t['tp'])} | RRR {t['rrr']:.1f}"
            o.append(f"        label.new({t['t0']}, {g(t['entry'])}, \"{txt}\", xloc=xloc.bar_time, style=label.style_label_{'up' if t['dir'] == 'LONG' else 'down'}, color=color.new(color.rgb(20,40,90), 0), textcolor=color.white, size=size.small)")
    return '\n'.join(o) + '\n'


def run(pair, monday, K=None):
    side = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sidecar', 'out', f'{monday}.json')))
    K = K or P.k_factor(side['h10']['rates'])
    spot = D.closed(pair, '60', monday)[-1]['close']
    exp = [dict(e, day=e.get('cut_date', '')[5:]) for e in side['expiries'].get('EURUSD' if pair == 'DXY' else pair, [])]
    r = Z.build(pair, monday, exp, K, spot)
    r['e2'] = E2.chain(pair, monday, r)
    import e3_setups as E3
    r['e3'] = E3.build(pair, monday, r)
    return r


if __name__ == '__main__':
    monday, pair = sys.argv[1], sys.argv[2]
    r = run(pair, monday, float(sys.argv[3]) if len(sys.argv) > 3 else None)
    sys.stdout.write(generate(pair, monday, r))
