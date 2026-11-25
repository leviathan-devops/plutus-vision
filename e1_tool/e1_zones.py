"""e1_zones.py - ZONE ASSEMBLY (P452:1116-1153, Step 9.7 P452:1186-1205) under the operator's rulings L-37/L-38/L-39.
A pressure zone = a candle structure (A) joined with the computed levels on it (B). Where levels meet a structural extreme with no
order block, the pressure zone is drawn across the levels and the sweep zone is drawn too.
Assumptions (listed for the operator): A3 which areas become named zones; A4 a zone price has closed through is no longer a zone."""
import e1_data as D, e1_pillars as P, e1_synth as S


def valid_sd(pair, monday):
    """Step 0f zones after the prompt's noise rejection (P452:741-745) + one-time use (operator notes) + A4 (closed through = broken)"""
    b = D.closed(pair, '240', monday)
    b0 = D.boundary_ms(monday)
    keep, drop = [], []
    for z in P.step0f(pair, monday):
        later = [x for x in b if x['time'] > z['end_time']]
        broken = any((x['close'] < z['bot']) if z['type'] == 'Demand' else (x['close'] > z['top']) for x in later)
        why = ('wider than 0.40' if z['top'] - z['bot'] > P._u(pair, 40) else 'older than 3 weeks' if z['origin_time'] < b0 - 21 * 86400000
               else 'closed through (broken)' if broken else f"{z['mit']}X mitigated" if z['mit'] > 1 else None)
        z['excluded'] = why
        (drop if why else keep).append(z)
    return keep, drop


def build(pair, monday, expiries, K, spot):
    u = lambda pips: P._u(pair, pips)
    L, swings = S.collect(pair, monday, expiries, K)
    sd, sd_drop = valid_sd(pair, monday)
    days = D.daily(pair, monday)
    recent = [s for s in swings if s['date'] >= days[-10]['date']]
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
        fresh_bom = [z for z in a['structs'] if z['kind'] == 'BoM' and z['mit'] <= 1]
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
        if m and m['side'] == z['side'] and z['bot'] <= m['top']:
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
    return {'levels': L, 'zones': shown, 'all': zones, 'sd': sd, 'sd_drop': sd_drop, 'lsz': lsz, 'swings': swings, 'pp': pp, 'spot': spot, 'K': K}


def show(r, pair):
    f = '%.2f' if pair == 'DXY' else '%.4f'
    g = lambda v: f % v
    for z in r['zones']:
        print("  %-18s %s-%s %-14s %4.1f/14 ZFP %-6s %-13s %s | candle %s | sweep %s | walls %s | levels on it %d | top: %s" % (
            z['name'], g(z['bot']), g(z['top']), z['degree'], z['score'], z['zfp'], z['type'], z['tier'][:6],
            [(s['kind'], s['type'], g(s['bot']), g(s['top']), D.ts(s['origin_time'])[5:16], f"{s['mit']}X") for s in z['structs']],
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
