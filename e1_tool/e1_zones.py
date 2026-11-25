"""e1_zones.py - ZONE ASSEMBLY (P452:1116-1153, Step 9.7 P452:1186-1205) under the operator's rulings L-37/L-38/L-39.
A pressure zone = a candle structure (A) joined with the computed levels on it (B). Where levels meet a structural extreme with no
order block, the pressure zone is drawn across the levels and the sweep zone is drawn too.
Assumptions (listed for the operator): A3 which areas become named zones; A4 a demand candle below which price trades / supply candle above which price trades is no longer a zone."""
import e1_data as D, e1_pillars as P, e1_synth as S


def valid_sd(pair, monday, spot):
    """Supply/demand candles. Operator ruling L-40: the 4H chart is the OVERVIEW; the zones are worked on the 1H chart.
    4H: Step 0f over 60 days with the prompt's noise rejection (P452:741-745). 1H: the same candle rule on the prior two weeks (Step 0g window).
    A 1H candle inside a kept 4H zone of its type carries that zone's BoM/MoM class (nested precision); a kept 4H zone with no 1H candle in it stays as its 4H candle."""
    b0 = D.boundary_ms(monday)
    def screen(zs, max_age_days):
        keep, drop = [], []
        for z in zs:
            # A4: a demand candle the market now trades UNDER (or a supply candle it trades OVER) is no longer that zone
            broken = (spot < z['bot']) if z['type'] == 'Demand' else (spot > z['top'])
            why = ('wider than 0.40' if z['top'] - z['bot'] > P._u(pair, 40) else f'older than {max_age_days} days' if z['origin_time'] < b0 - max_age_days * 86400000
                   else 'price beyond it at the boundary (broken)' if broken else f"{z['mit']}X mitigated" if z['mit'] > 1 else None)
            z['excluded'] = why
            (drop if why else keep).append(z)
        return keep, drop
    h4, h4_drop = screen(P.step0f(pair, monday, '240', 60), 21)
    h1, h1_drop = screen(P.step0f(pair, monday, '60', 14), 14)
    for z in h4:
        z['tf'] = '4H'; z['h4bom'] = z['kind'] == 'BoM'
    used = set()
    for z in h1:
        z['tf'] = '1H'
        par = [p for p in h4 if p['type'] == z['type'] and z['bot'] <= p['top'] and z['top'] >= p['bot']]
        z['h4bom'] = any(p['kind'] == 'BoM' for p in par)
        if par:
            z['kind'] = 'BoM' if z['h4bom'] else 'MoM'
            z['parent'] = par[0]
            used.update(id(p) for p in par)
    keep = h1 + [p for p in h4 if id(p) not in used]
    return keep, h4_drop + h1_drop, h4


def build(pair, monday, expiries, K, spot):
    u = lambda pips: P._u(pair, pips)
    L, swings = S.collect(pair, monday, expiries, K)
    sd, sd_drop, h4 = valid_sd(pair, monday, spot)
    days = D.daily(pair, monday)
    # Step 0 / 0.45: ALL prior D1 swing extremes that passed the wick test (major, or minor per Step 0h) in the 90 daily bars,
    # plus every swing of the last 10 days (A2: the report lists each recent daily low / high as a sweep zone)
    recent = [s for s in swings if s['grade'] or s['date'] >= days[-10]['date']]
    lsz = P.step045_lsz(pair, monday, recent, spot)
    for z, s in zip(lsz, recent):
        later = [d for d in days if d['date'] > s['date']]
        z['swept'] = any((d['low'] < s['price']) if s['side'] == 'low' else (d['high'] > s['price']) for d in later)
        z['side'] = s['side']; z['price'] = s['price']
    # candle seeds: supply candles that overlap each other are one structure (same for demand); the prompt forbids supply over demand
    seeds = []
    for z in sorted(sd, key=lambda z: z['bot']):
        m = next((s for s in seeds if s['side'] == z['type'] and z['bot'] <= s['top'] and z['top'] >= s['bot']), None)
        if m:
            m['bot'] = min(m['bot'], z['bot']); m['top'] = max(m['top'], z['top']); m['structs'].append(z)
        else:
            seeds.append({'bot': z['bot'], 'top': z['top'], 'structs': [z], 'sweeps': [], 'kind': 'candle', 'side': z['type']})
    for z in lsz:
        if z['swept'] or (z['side'] == 'low') != (z['price'] < spot):
            continue
        if z['date'] < days[-10]['date'] and not any(c['kind'] == 'candle' and c['bot'] - u(3) <= z['price'] <= c['top'] + u(3) for c in seeds):
            continue          # an older unswept extreme stays a sweep zone (green box) only; level zones come from the last 10 days (as in the report)
        host = [s for s in seeds if s['kind'] == 'candle' and s['bot'] - u(3) <= z['price'] <= s['top'] + u(3)]
        if host:
            host[0]['sweeps'].append(z)                       # swing extreme inside the order block = confluent floor / ceiling (Step 0e)
        else:
            same = [s for s in seeds if s['kind'] == 'levels' and abs(s['price'] - z['price']) <= u(5)]
            if same:
                same[0]['sweeps'].append(z); same[0]['bot'] = min(same[0]['bot'], z['bot']); same[0]['top'] = max(same[0]['top'], z['top'])
            else:
                seeds.append({'bot': z['bot'], 'top': z['top'], 'structs': [], 'sweeps': [z], 'kind': 'levels', 'price': z['price'], 'side': 'Supply' if z['side'] == 'high' else 'Demand'})
    zones = []
    for a in seeds:
        # candle zone: the candle + the levels on it (exact match, 3 pips). Level zone: the levels within 0.05 of the swing extreme
        # (the prompt's sweep-zone / repeated-magnet distance), i.e. the pressure zone across the levels, with the sweep zone inside it
        if a['kind'] == 'candle':
            inside = [x for x in L if a['bot'] - u(3) <= x['p'] <= a['top'] + u(3)]
        else:
            inside = [x for x in L if abs(x['p'] - a['price']) <= u(5)]
        band = [x for x in L if a['bot'] - u(10) <= x['p'] <= a['top'] + u(10)]
        if not band:
            continue
        best, bs = None, None
        for x in band:
            sc = S.score_level(x, L, pair)
            tot = sc['tech'] + sc['opt'] + sc['ana'] + sc['stru'] + sc['psy'] + sc['bonus']
            if bs is None or tot > bs[0]:
                best, bs = x, (tot, sc)
        walls = [x for x in inside if x['dim'] == 'opt' and x['tier'] <= 2]
        wall = min([w['tier'] for w in walls] + [9])
        fresh_bom = [z for z in a['structs'] if z.get('h4bom') and z['mit'] <= 1]      # Tier 1 = overlap with a 4H BoM 0X-1X (Step 9.7)
        pillars = len({x['pillar'] for x in band})
        ghost = bool(walls) and all(w.get('ghost') for w in walls)
        ztype = ('Post-Expiry Ghost' if ghost else 'Hard Wall' if wall == 1 and pillars >= 3 and bs[1]['bonus'] >= 2 else 'Standard Wall' if wall <= 2 and pillars >= 2
                 else 'Soft Wall' if pillars >= 2 else 'One-Touch')
        regime = 2 if ztype == 'Hard Wall' else 0 if ztype == 'One-Touch' else 1
        total = min(14, bs[0] + regime + (2 if fresh_bom else 1))
        ps = [x['p'] for x in inside]
        zones.append({'bot': min([a['bot']] + ps), 'top': max([a['top']] + ps), 'a_bot': a['bot'], 'a_top': a['top'], 'kind': a['kind'], 'levels': inside, 'band': band,
                      'structs': a['structs'], 'sweeps': a['sweeps'], 'walls': walls, 'score': total, 'degree': S.degree(total), 'type': ztype, 'zfp': S.ZFP_RANGE[ztype],
                      'tier': 'Tier 1: Confluent' if fresh_bom else 'Tier 2: IP-Only', 'dims': bs[1], 'best': best, 'pillars': pillars, 'side': a['side']})
    # zones of the same side whose extents overlap or touch are one zone (levels cluster into one group, P452:1140)
    zones.sort(key=lambda z: z['bot'])
    out = []
    for z in zones:
        m = out[-1] if out else None
        # level zones (no candle) of one side within 0.10 of each other are one cluster (P452:1140), kept under 0.40 wide. Candle zones stay
        # separate unless they overlap: merging them joined the report's Resistance Ceiling and Upper Resistance into one (tried, rejected)
        tight = m and m['kind'] == 'levels' and z['kind'] == 'levels' and z['bot'] - m['top'] <= u(10) and z['top'] - m['bot'] <= u(40)
        if m and m['side'] == z['side'] and (z['bot'] <= m['top'] or tight):
            m['top'] = max(m['top'], z['top']); m['structs'] += z['structs']; m['sweeps'] += z['sweeps']
            m['levels'] = m['levels'] + [x for x in z['levels'] if x not in m['levels']]; m['walls'] = m['walls'] + [x for x in z['walls'] if x not in m['walls']]
            if z['score'] > m['score']:
                for k in ('score', 'degree', 'type', 'zfp', 'dims', 'best', 'pillars'):
                    m[k] = z[k]
            if z['tier'].startswith('Tier 1'):
                m['tier'] = z['tier']
            m['kind'] = 'candle' if 'candle' in (m['kind'], z['kind']) else 'levels'
        else:
            out.append(z)
    zones = out
    shown = sorted([z for z in zones if z['score'] >= 6], key=lambda z: -z['top'])          # MODERATE and above only
    # names by position (P452:1146-1153): Equilibrium = the pivot area (the zone holding / nearest the weekly pivot point);
    # above it the top zone is the Resistance Ceiling, the others Upper Resistance; below it the lowest is the Key Support Band, the others Mid-Range Support
    pp = P.pillar1(pair, monday)['weekly']['classic']['PP']
    if shown:
        eq = min(shown, key=lambda z: 0 if z['bot'] <= pp <= z['top'] else min(abs(z['bot'] - pp), abs(z['top'] - pp)))
        up = [z for z in shown if z['bot'] > eq['bot'] and z is not eq]
        dn = [z for z in shown if z is not eq and z not in up]
        eq['name'], eq['cat'] = 'EQUILIBRIUM ZONE', 'MID'
        for i, z in enumerate(up):
            z['name'], z['cat'] = ('RESISTANCE CEILING' if i == 0 else 'UPPER RESISTANCE'), 'RES'
        for i, z in enumerate(dn):
            z['name'], z['cat'] = ('KEY SUPPORT BAND' if i == len(dn) - 1 else 'MID-RANGE SUPPORT'), 'SUP'
    infill = gap_scan(pair, monday, L, shown, eq if shown else None)
    # sweep zones listed / drawn: every swing of the last 10 days (as the report lists them) + older ones still unswept
    lsz = [z for z in lsz if z['date'] >= days[-10]['date'] or not z['swept']]
    return {'infill': infill, 'levels': L, 'zones': shown, 'all': zones, 'sd': sd, 'sd_drop': sd_drop, 'h4': h4, 'lsz': lsz, 'swings': swings, 'pp': pp, 'spot': spot, 'K': K}


def gap_scan(pair, monday, L, shown, eq):
    """STEP 9.5 (P452:1159-1184): gaps >= 0.20 between adjacent mapped zones; a gap-region level with 2+ supporting signals is a
    GAP IN-FILL LEVEL (Confidence MODERATE, Structural = 1). Only gaps BETWEEN mapped zones are scanned (literal). An in-fill level
    splits its gap; a remaining part is scanned again only if it is still >= 0.20, so in-fill levels sit >= 0.20 from zones and from each other."""
    u = lambda pips: P._u(pair, pips)
    edges = [(z['bot'], z['top']) for z in shown]
    edges.sort()
    kind = lambda x: ('round' if x['dim'] == 'psy' else 'option strike' if x['dim'] == 'opt' else 'weekly pivot' if x['tag'].startswith('Weekly') and x['pillar'] == 'P1'
                      else 'daily pivot' if x['pillar'] == 'P1' else 'swing level' if x['dim'] == 'extreme' else 'daily close' if 'close' in x['tag'] else None)
    out = []
    for (lo_b, lo_t), (hi_b, hi_t) in zip(edges, edges[1:]):
        if hi_b - lo_t < u(20):
            continue
        cands = []
        for x in L:
            if not (lo_t + u(20) <= x['p'] <= hi_b - u(20)) or kind(x) is None:
                continue
            sup = {}
            for y in L:
                if abs(y['p'] - x['p']) <= u(3) and kind(y):
                    sup.setdefault(kind(y), y)
            if len(sup) >= 2:
                cands.append({'p': x['p'], 'signals': sorted(sup), 'levels': list(sup.values()), 'n': len(sup)})
        cands.sort(key=lambda c: (-c['n'], -c['p']))
        took = []
        for c in cands:
            if all(abs(c['p'] - t['p']) >= u(20) for t in took):
                took.append(c)
        for t in took:
            ps = [y['p'] for y in t['levels']]
            t['bot'], t['top'] = min(ps), max(ps)
            t['cat'] = 'RES' if eq and t['bot'] > eq['top'] else 'SUP' if eq and t['top'] < eq['bot'] else 'MID'
            t['gap'] = (lo_t, hi_b)
        out += took
    return sorted(out, key=lambda t: -t['p'])


def show(r, pair):
    f = '%.2f' if pair == 'DXY' else '%.4f'
    g = lambda v: f % v
    for z in r['zones']:
        print("  %-18s %s-%s %-14s %4.1f/14 ZFP %-6s %-13s %s | candle %s | sweep %s | walls %s | levels on it %d | top: %s" % (
            z['name'], g(z['bot']), g(z['top']), z['degree'], z['score'], z['zfp'], z['type'], z['tier'][:6],
            [(s['tf'], s['kind'], s['type'][:3], g(s['bot']), g(s['top']), D.ts(s['origin_time'])[5:16], f"{s['mit']}X") for s in z['structs']],
            [(g(s['bot']), g(s['top'])) for s in z['sweeps']], [g(w['p']) for w in z['walls']], len(z['levels']), z['best']['tag']))


if __name__ == '__main__':
    import sys, json, os
    monday = sys.argv[1] if len(sys.argv) > 1 else '2026-04-20'
    pair = sys.argv[2] if len(sys.argv) > 2 else 'DXY'
    side = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sidecar', 'out', f'{monday}.json')))
    K = float(sys.argv[3]) if len(sys.argv) > 3 else P.k_factor(side['h10']['rates'])
    spot = D.closed(pair, '60', monday)[-1]['close']
    src = 'EURUSD' if pair == 'DXY' else pair
    exp = [dict(e, day=e.get('cut_date', '')[5:]) for e in side['expiries'].get(src, [])]
    r = build(pair, monday, exp, K, spot)
    print(f"{pair} {monday} spot {spot} weekly PP {r['pp']:.4f} K {K:.4f} | levels {len(r['levels'])} | 4H zones kept {len(r['sd'])} dropped {len(r['sd_drop'])}")
    show(r, pair)
    for t in r['infill']:
        print('  GAP IN-FILL %.4f (%.4f-%.4f) %s' % (t['p'], t['bot'], t['top'], ' + '.join(t['signals'])))
