"""e1_synth.py - SYNTHESIS ENGINE: collect levels, score on 6 dimensions + structural-extreme bonus, cluster, assemble zones
(P452:1075-1205 = P533:1461-1514). Zone extents follow the operator's ruling L-39: candle structure + level cluster joined."""
import json, os
import e1_data as D, e1_pillars as P

DEGREES = ((12, 'EXTREME'), (10, 'HEAVY'), (8, 'MODERATE-HEAVY'), (6, 'MODERATE'), (4, 'LIGHT'), (0, 'MINIMAL'))   # P452:1107-1114
ZFP_RANGE = {'Hard Wall': '5-15%', 'Standard Wall': '15-30%', 'Soft Wall': '30-50%', 'One-Touch': '50-70%', 'Post-Expiry Ghost': '20-40%'}   # P452:964-972


def collect(pair, monday, expiries, K):
    """S1: every level from every pillar, nothing filtered by distance to spot. Each level: p, pillar, tag, kind."""
    u = lambda pips: pips * D.PIP[pair]
    L = []
    p1 = P.pillar1(pair, monday)
    for var in ('classic', 'fib', 'camarilla'):
        for k, v in p1['weekly'][var].items():
            L.append({'p': v, 'pillar': 'P1', 'tag': f'Weekly {var} {k}', 'dim': 'tech'})
        for d in p1['daily']:
            for k, v in d[var].items():
                L.append({'p': v, 'pillar': 'P1', 'tag': f"Daily {var} {k} ({d['date'][5:]})", 'dim': 'tech'})
    for m in P.pillar2(pair, monday):
        L.append({'p': m['p'], 'pillar': 'P2', 'tag': m['name'], 'dim': 'tech', 'w': m['w']})
    w = D.weekly(pair, monday)[-1]
    for k, key in (('Prior week high', 'high'), ('Prior week low', 'low'), ('Prior week close', 'close')):
        L.append({'p': w[key], 'pillar': 'P5', 'tag': k, 'dim': 'anchor'})
    for d in p1['last5']:
        for k in ('close', 'high', 'low'):
            L.append({'p': d[k], 'pillar': 'P5', 'tag': f"Daily {k} {d['date'][5:]}", 'dim': 'anchor'})
    swings = P.step0_swings(pair, monday)
    for s in swings:
        if s['grade']:
            L.append({'p': s['price'], 'pillar': 'P5', 'tag': ('Liquidity Sweep Target' if s['side'] == 'low' else 'Supply Ceiling Target') + f" {s['date'][5:]} ({s['grade']})",
                      'dim': 'extreme', 'bonus': 1.0 if s['grade'] == 'major' else 0.0, 'half': s['grade'] == 'minor'})
    for mg in P.step05_magnets(pair, swings):
        L.append({'p': mg['price'], 'pillar': 'P5', 'tag': f"{mg['kind']} ({mg['n']}x)", 'dim': 'extreme', 'bonus': mg['bonus']})
    lo, hi = min(x['p'] for x in L) - u(50), max(x['p'] for x in L) + u(50)
    fibs, rounds = P.pillar6(pair, monday, lo, hi)
    for f in fibs:
        L.append({'p': f['p'], 'pillar': 'P6', 'tag': f['name'], 'dim': 'tech'})
    for r in rounds:
        L.append({'p': r['p'], 'pillar': 'P6', 'tag': r['name'], 'dim': 'psy', 'kind': r['kind']})
    for e in expiries:
        p = P.strike_to_dxy(K, e['strike']) if pair == 'DXY' else e['strike']
        L.append({'p': p, 'pillar': 'P8', 'tag': f"{e['strike']} {e['notional_m']}M {e.get('day', '')}".strip(), 'dim': 'opt', 'tier': P.tier(e['notional_m']),
                  'ghost': e.get('state') == 'ghost', 'notional_m': e['notional_m'], 'strike': e['strike']})
    return sorted(L, key=lambda x: -x['p']), swings


def score_level(x, L, pair):
    """S2: six dimensions 0-2 each + structural-extreme bonus (max +2). Regime is added per zone from its ZFP band."""
    u = lambda pips: pips * D.PIP[pair]
    near = lambda dims, tol: [o for o in L if o['dim'] in dims and abs(o['p'] - x['p']) <= tol]
    tech = 2 if near(('tech',), u(3)) else 1 if near(('tech',), u(10)) else 0
    opts = [o for o in L if o['dim'] == 'opt' and o['tier'] <= 2 and abs(o['p'] - x['p']) <= (u(7) if o['tier'] == 1 else u(10))]
    opt = 2 if opts else 0
    anchors, extremes = near(('anchor',), u(3)), near(('extreme',), u(3))
    stru = 2 if anchors and extremes else 1 if (near(('anchor', 'extreme'), u(10))) else 0
    if stru == 1 and all(o.get('half') for o in near(('anchor', 'extreme'), u(10))):
        stru = 0.5
    rn = near(('psy',), u(3))
    psy = 2 if any(o['kind'] in ('big', 'half') for o in rn) else 1 if rn else 0
    bonus = min(2.0, max([o.get('bonus', 0) for o in near(('extreme',), u(3))] + [0]))
    return {'tech': tech, 'opt': opt, 'ana': 0, 'stru': stru, 'psy': psy, 'bonus': bonus, 'opts': opts}


def cluster(L, pair):
    """S3/S4: levels grouped where they cluster within 0.15 (15 pips); 3+ = HIGH-DENSITY ZONE, pair within 0.10 = TIGHT CONFLUENCE"""
    u = lambda pips: pips * D.PIP[pair]
    groups, cur = [], []
    for x in L:
        if cur and cur[0]['p'] - x['p'] > u(15):
            groups.append(cur); cur = []
        cur.append(x)
    if cur:
        groups.append(cur)
    return groups


def degree(score):
    for lim, name in DEGREES:
        if score >= lim:
            return name


def assemble(pair, monday, expiries, K, spot):
    L, swings = collect(pair, monday, expiries, K)
    sd_all = P.step0f(pair, monday)
    # 4H noise rejection (P452:741-745) + one-time use (operator notes; Tier 1 = BoM 0X-1X, P452:1201):
    # keep zones no wider than 0.40, formed within the last 3 weeks, visited at most once since
    b0 = D.boundary_ms(monday)
    sd = [z for z in sd_all if z['top'] - z['bot'] <= 40 * D.PIP[pair] and z['origin_time'] >= b0 - 21 * 86400000 and z['mit'] <= 1]
    lsz = P.step045_lsz(pair, monday, [s for s in swings if s['date'] >= D.daily(pair, monday)[-10]['date']], spot)
    groups = [g for g in cluster(L, pair) if len(g) >= 3]
    # a candle structure belongs to ONE zone: the cluster whose level span it overlaps most (no two zones share a structure)
    def owner(z):
        best, bo = None, 0.0
        for gi, g in enumerate(groups):
            ov = min(z['top'], g[0]['p']) - max(z['bot'], g[-1]['p'])
            if ov >= 0 and (best is None or ov > bo):
                best, bo = gi, ov
        return best
    own_sd, own_ls = {}, {}
    for z in sd:
        own_sd.setdefault(owner(z), []).append(z)
    for z in lsz:
        own_ls.setdefault(owner(z), []).append(z)
    zones = []
    for gi, g in enumerate(groups):
        best, bs = None, None
        for x in g:
            sc = score_level(x, L, pair)
            tot = sc['tech'] + sc['opt'] + sc['ana'] + sc['stru'] + sc['psy'] + sc['bonus']
            if bs is None or tot > bs[0]:
                best, bs = x, (tot, sc)
        lo, hi = g[-1]['p'], g[0]['p']
        over, sweeps = own_sd.get(gi, []), own_ls.get(gi, [])
        fresh_bom = [z for z in over if z['kind'] == 'BoM' and z['mit'] <= 1]
        pillars = len({x['pillar'] for x in g})
        wall = min([o['tier'] for o in bs[1]['opts']] + [9])
        ghost = bool(bs[1]['opts']) and all(o.get('ghost') for o in bs[1]['opts'])
        ztype = ('Post-Expiry Ghost' if ghost else 'Hard Wall' if wall == 1 and pillars >= 3 and bs[1]['bonus'] >= 2 else 'Standard Wall' if wall <= 2 and pillars >= 2
                 else 'Soft Wall' if pillars >= 2 else 'One-Touch')
        regime = 2 if ztype == 'Hard Wall' else 0 if ztype == 'One-Touch' else 1                       # P452:1066-1071
        tierpts = 2 if fresh_bom else 1                                                                # Step 9.7
        total = min(14, bs[0] + regime + tierpts)
        zones.append({'levels': g, 'lv_lo': lo, 'lv_hi': hi, 'structs': over, 'sweeps': sweeps,
                      'bot': min([lo] + [z['bot'] for z in over] + [z['bot'] for z in sweeps]), 'top': max([hi] + [z['top'] for z in over] + [z['top'] for z in sweeps]),
                      'score': total, 'degree': degree(total), 'type': ztype, 'zfp': ZFP_RANGE[ztype], 'tier': 'Tier 1: Confluent' if fresh_bom else 'Tier 2: IP-Only',
                      'dims': bs[1], 'best': best, 'n': len(g), 'pillars': pillars, 'wall': wall})
    # S7 names (P452:1148-1153): five standard roles. Equilibrium = the MODERATE+ zone at / nearest spot; above it the two
    # highest-scoring zones (upper = RESISTANCE CEILING, lower = UPPER RESISTANCE); below it the two highest-scoring
    # (nearer = MID-RANGE SUPPORT, further = KEY SUPPORT BAND). Assumption A3.
    # A3'': Step 9.5 treats adjacent mapped zones as >= 0.20 apart (closer = the same area). Take MODERATE+ clusters by score,
    # skipping any within 0.20 of one already taken (tie: holds a candle structure / wall, then nearer to spot). The zone at /
    # nearest spot is the Equilibrium; the two nearest taken zones above it and the two below it get the names by position.
    gap = 20 * D.PIP[pair]
    dist = lambda z: 0 if z['bot'] <= spot <= z['top'] else min(abs(z['bot'] - spot), abs(z['top'] - spot))
    # a pressure zone is where levels meet a candle structure or a wall (L-39): those clusters rank first, then by score
    rank = lambda z: 2 if (z['structs'] or z['wall'] <= 2) else 1 if z['sweeps'] else 0
    cand = sorted([z for z in zones if z['score'] >= 6], key=lambda z: (-rank(z), -z['score'], dist(z)))
    # the Equilibrium is fixed first: the MODERATE+ cluster at / nearest spot. Separation is measured between LEVEL spans.
    sep = lambda z, t: z['lv_lo'] - t['lv_hi'] >= gap or t['lv_lo'] - z['lv_hi'] >= gap
    taken = []
    if cand:
        taken.append(min(cand, key=lambda z: (dist(z), -rank(z), -z['score'])))
    for z in cand:
        if z not in taken and all(sep(z, t) for t in taken):
            taken.append(z)
    named = []
    if taken:
        eq = min(taken, key=dist)
        eq['name'] = 'EQUILIBRIUM ZONE'; named.append(eq)
        up = sorted([z for z in taken if z is not eq and z['bot'] >= eq['top']], key=dist)[:2]
        dn = sorted([z for z in taken if z is not eq and z['top'] <= eq['bot']], key=dist)[:2]
        up.sort(key=lambda z: -z['top']); dn.sort(key=lambda z: -z['top'])
        for z, nm in zip(up, ['RESISTANCE CEILING', 'UPPER RESISTANCE'] if len(up) == 2 else ['RESISTANCE CEILING']):
            z['name'] = nm; named.append(z)
        for z, nm in zip(dn, ['MID-RANGE SUPPORT', 'KEY SUPPORT BAND'] if len(dn) == 2 else ['KEY SUPPORT BAND']):
            z['name'] = nm; named.append(z)
    named.sort(key=lambda z: -z['top'])
    return {'levels': L, 'zones': zones, 'named': named, 'sd': sd, 'sd_all': sd_all, 'lsz': lsz, 'swings': swings}


if __name__ == '__main__':
    import sys
    monday = sys.argv[1] if len(sys.argv) > 1 else '2026-04-20'
    pair = 'DXY'
    spot = D.closed(pair, '60', monday)[-1]['close']
    side = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'sidecar', 'out', f'{monday}.json')))
    K = P.k_factor(side['h10']['rates'])
    exp = [dict(e, day=e.get('cut_date', '')[5:]) for e in side['expiries'].get('EURUSD', [])]
    r = assemble(pair, monday, exp, K, spot)
    print(f"{pair} {monday} spot {spot} K {K:.4f} | levels {len(r['levels'])} | clusters(3+) {len(r['zones'])}")
    print('4H zones kept:', [(z['kind'], z['type'], round(z['bot'], 3), round(z['top'], 3), D.ts(z['origin_time']), f"{z['mit']}X") for z in r['sd']])
    print('sweep zones:', [(round(z['bot'], 2), round(z['top'], 2), z['source'][-10:], z['priority']) for z in r['lsz']])
    for z in r['named']:
        print("  %-18s %.2f-%.2f %-14s %4.1f/14 ZFP %-7s %-17s %s | levels %.2f-%.2f (%d) | S/D %s | LSZ %s | top level: %s" % (
            z['name'], z['bot'], z['top'], z['degree'], z['score'], z['zfp'], z['type'], z['tier'], z['lv_lo'], z['lv_hi'], z['n'],
            [(s['kind'], s['type'], round(s['bot'], 2), round(s['top'], 2)) for s in z['structs']], [(round(s['bot'], 2), round(s['top'], 2)) for s in z['sweeps']], z['best']['tag']))
    print('REPORT: CEILING 99.16-99.23 HEAVY 10 · UPPER RES 98.77-98.99 MOD-HEAVY 8 T1 · EQ 98.29-98.41 MOD-HEAVY 9 · MID SUPPORT 98.00-98.12 MODERATE 7 · KEY SUPPORT 97.63-97.97 HEAVY 11 T1')


def assemble_anchored(pair, monday, expiries, K, spot):
    """Zones built FROM the structures (ruling L-39; report key drivers): every kept 4H supply/demand candle, sweep zone and option
    wall is an anchor; anchors that overlap are one anchor; the levels within 0.10 of it (TIGHT CONFLUENCE band) join it and score it."""
    u = lambda pips: pips * D.PIP[pair]
    r = assemble(pair, monday, expiries, K, spot)
    L = r['levels']
    anchors = [{'bot': z['bot'], 'top': z['top'], 'structs': [z], 'sweeps': [], 'walls': []} for z in r['sd']]
    anchors += [{'bot': z['bot'], 'top': z['top'], 'structs': [], 'sweeps': [z], 'walls': []} for z in r['lsz']]
    anchors += [{'bot': x['p'], 'top': x['p'], 'structs': [], 'sweeps': [], 'walls': [x]} for x in L if x['dim'] == 'opt' and x['tier'] <= 2]
    anchors.sort(key=lambda a: a['bot'])
    merged = []
    for a in anchors:
        m = merged[-1] if merged else None
        ov = (min(a['top'], m['top']) - a['bot']) if m else -1
        small = min(a['top'] - a['bot'], (m['top'] - m['bot']) if m else 0)
        # anchors are one anchor only when they share more than half of the smaller one (or a point anchor sits inside the other)
        if m and ov >= 0 and ov >= small / 2:
            m['top'] = max(m['top'], a['top']); m['structs'] += a['structs']; m['sweeps'] += a['sweeps']; m['walls'] += a['walls']
        else:
            merged.append(a)
    zones = []
    for a in merged:
        lv = [x for x in L if a['bot'] - u(10) <= x['p'] <= a['top'] + u(10)]
        if not lv:
            continue
        best, bs = None, None
        for x in lv:
            sc = score_level(x, L, pair)
            tot = sc['tech'] + sc['opt'] + sc['ana'] + sc['stru'] + sc['psy'] + sc['bonus']
            if bs is None or tot > bs[0]:
                best, bs = x, (tot, sc)
        fresh_bom = [z for z in a['structs'] if z['kind'] == 'BoM' and z['mit'] <= 1]
        pillars = len({x['pillar'] for x in lv})
        wall = min([w['tier'] for w in a['walls']] + [9])
        ghost = bool(a['walls']) and all(w.get('ghost') for w in a['walls'])
        ztype = ('Post-Expiry Ghost' if ghost else 'Hard Wall' if wall == 1 and pillars >= 3 and bs[1]['bonus'] >= 2 else 'Standard Wall' if wall <= 2 and pillars >= 2
                 else 'Soft Wall' if pillars >= 2 else 'One-Touch')
        regime = 2 if ztype == 'Hard Wall' else 0 if ztype == 'One-Touch' else 1
        total = min(14, bs[0] + regime + (2 if fresh_bom else 1))
        inside = [x['p'] for x in lv if a['bot'] - u(3) <= x['p'] <= a['top'] + u(3)]
        zones.append({'bot': min([a['bot']] + inside), 'top': max([a['top']] + inside), 'a_bot': a['bot'], 'a_top': a['top'], 'levels': lv,
                      'lv_lo': min(x['p'] for x in lv), 'lv_hi': max(x['p'] for x in lv), 'structs': a['structs'], 'sweeps': a['sweeps'], 'walls': a['walls'], 'wall': wall,
                      'score': total, 'degree': degree(total), 'type': ztype, 'zfp': ZFP_RANGE[ztype], 'tier': 'Tier 1: Confluent' if fresh_bom else 'Tier 2: IP-Only',
                      'dims': bs[1], 'best': best, 'n': len(lv), 'pillars': pillars})
    gap = u(20)
    dist = lambda z: 0 if z['a_bot'] <= spot <= z['a_top'] else min(abs(z['a_bot'] - spot), abs(z['a_top'] - spot))
    cand = sorted([z for z in zones if z['score'] >= 6], key=lambda z: (-z['score'], dist(z)))
    sep = lambda z, t: z['a_bot'] - t['a_top'] >= gap or t['a_bot'] - z['a_top'] >= gap
    taken = [min(cand, key=lambda z: (dist(z), -z['score']))] if cand else []
    for z in cand:
        if z not in taken and all(sep(z, t) for t in taken):
            taken.append(z)
    named = []
    if taken:
        eq = taken[0]; eq['name'] = 'EQUILIBRIUM ZONE'; named.append(eq)
        up = sorted([z for z in taken[1:] if z['a_bot'] >= eq['a_top']], key=dist)[:2]
        dn = sorted([z for z in taken[1:] if z['a_top'] <= eq['a_bot']], key=dist)[:2]
        up.sort(key=lambda z: -z['top']); dn.sort(key=lambda z: -z['top'])
        for z, nm in zip(up, ['RESISTANCE CEILING', 'UPPER RESISTANCE'] if len(up) == 2 else ['RESISTANCE CEILING']):
            z['name'] = nm; named.append(z)
        for z, nm in zip(dn, ['MID-RANGE SUPPORT', 'KEY SUPPORT BAND'] if len(dn) == 2 else ['KEY SUPPORT BAND']):
            z['name'] = nm; named.append(z)
    named.sort(key=lambda z: -z['top'])
    r['anchored'] = zones; r['named'] = named
    return r
