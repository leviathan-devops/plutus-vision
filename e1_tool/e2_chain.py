"""e2_chain.py - ENGINE 2: the macro shape chain, forward-mapped at the Monday anchor from the Engine 1 map (P533 Part VI :1725-2057; FA sections 8-9).
"Engine 1 answers: Where are the walls?  Engine 2 answers: What path will price take through those walls?"  Primary timeframe 1H, structural validation 4H (P533:1729-1739).

Procedure = P533 6.6 "Forward Mapping Procedure", one function per step:
  Step 1 current_shape()   - Shape Classification Decision Matrix 6.2 applied to the last completed sessions against the IP zones (zone-anchored, Rule 1 / Rule 4)
  Step 2/3 chain()         - Shape Transition Rules 6.4, ZFP-Conditioned Transition Rules 6.4.1, HTF Zone Mechanics Decision Tree 6.4.2 (FA 8), Conservation of Energy (FA 9),
                             Trading Speed Rule 6.10 (+1 day), durations 6.8; audit trail per extension; max 5 shapes; stop below 25% cumulative confidence
  Step 4 alternative       - the chain that activates if the primary fails at the Decision Zone
  Step 5 days()            - day-by-day decomposition (shape, direction, key zone, confidence) = the direct input of Engine 3; pair translation: same shapes, inverted direction (P533:1899-1917)
The path (R-03: day BOXES first, then the LINE) is the same day map expressed as the zone edges each day is expected to travel between.
No price literal; every level is an Engine 1 zone edge."""
import datetime as dt
import e1_data as D, e1_sd as SD

CONF = {'VERY HIGH': 0.90, 'HIGH': 0.80, 'MODERATE-HIGH': 0.65, 'MODERATE': 0.50, 'LOW-MOD': 0.35}       # confidence tiers of the tables 6.2 / 6.4 / 6.4.1
PIERCING = ('BS', 'PBS', 'WL', 'RWL')
DAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')


def storyline(pair, monday):
    """P533:1976-1983 "4H storyline tiebreaker: when in doubt, the 4H storyline bias decides. The weekly trend is identified on the 4H":
    the direction of the move that left the most recent 4H origin zone (BoM) whose move broke structure"""
    zs = [z for z in SD.scan(pair, monday, '240') if z['bos'] and z['kind'] == 'BoM']
    if not zs:
        return None, None
    z = zs[-1]
    return ('down' if z['type'] == 'Supply' else 'up'), z


def classify_day(d, zones, prev):
    """6.2 matrix on one completed session against the IP zones: BS = the session's body crossed a zone (PBS: two or more); WL = it pierced a zone and closed back on the side it came from;
    R = the session after a BS / WL with neither; SS = none of these"""
    o, h, l, c = d['open'], d['high'], d['low'], d['close']
    dn = [z for z in zones if o > z['top'] and c < z['bot']]
    up = [z for z in zones if o < z['bot'] and c > z['top']]
    if dn or up:
        zs, dr = (dn, 'down') if len(dn) >= len(up) else (up, 'up')
        return {'shape': 'PBS' if len(zs) >= 2 else 'BS', 'dir': dr, 'zones': [z['name'] for z in zs]}
    wl_up = [z for z in zones if l < z['bot'] and c > z['top'] and o > z['top']]       # pierced a support and closed back above it
    wl_dn = [z for z in zones if h > z['top'] and c < z['bot'] and o < z['bot']]
    if wl_up or wl_dn:
        zs, dr = (wl_up, 'up') if wl_up else (wl_dn, 'down')
        return {'shape': 'WL', 'dir': dr, 'zones': [z['name'] for z in zs]}
    if prev and prev['shape'] in PIERCING:
        return {'shape': 'R', 'dir': 'up' if c > o else 'down', 'zones': []}
    return {'shape': 'SS', 'dir': 'range', 'zones': []}


def current_shape(X):
    """6.6 Step 1 + 6.4.1 "R persists > 1 full session -> SS (reclassify)" + FA 9 conservation of energy"""
    hist, prev = [], None
    for d in X['daily'][-4:]:
        prev = classify_day(d, X['zones'], prev)
        prev['date'] = d['date']
        hist.append(prev)
    last, before = hist[-1], hist[-2]
    n_pierce = sum(1 for s in hist[-2:] if s['shape'] in PIERCING)
    if last['shape'] in ('BS', 'PBS') and before['shape'] not in PIERCING:
        s0 = {'shape': last['shape'], 'dir': last['dir'], 'why': f"the last session ({last['date']}) broke {', '.join(last['zones'])}"}
    elif n_pierce >= 2:
        s0 = {'shape': 'SS', 'dir': 'range', 'phase': 'post-energy',
              'why': f"two piercing sessions ({before['date']} {before['shape']} {before['dir']}, {last['date']} {last['shape']} {last['dir']}): conservation of energy, 1-2 full days of consolidation (FA 9)"}
    elif last['shape'] in ('WL', 'RWL'):
        s0 = {'shape': 'SS', 'dir': 'range', 'phase': 'late',
              'why': f"a whiplash ({last['date']} {last['dir']}) at the end of a consolidation: the range is old, the breakout is near (6.4 WL -> RWL / SS -> BS)"}
    elif last['shape'] == 'R':
        s0 = {'shape': 'SS', 'dir': 'range', 'phase': 'recovery', 'why': f"recovery after {before['shape']} {before['dir']} has lasted a full session: reclassified SS (6.4.1)"}
    else:
        s0 = {'shape': 'SS', 'dir': 'range', 'phase': 'late', 'why': 'no zone broken or pierced in the last sessions: consolidation in progress'}
    s0['history'] = hist
    return s0


def _bounds(X):
    """6.1.1 / 6.5: SS - 'Ceiling and Floor zones define the range; both bounding zones: ZFP < 30%, Confluence >= 6'. The IP zone holding spot is the pivot.
    On a side with no IP zone under 30% the nearest standing 1H / 4H supply-demand zone bounds the range (an unmitigated zone reacts on its first test, P533:1961-1964); else the nearest IP zone"""
    spot = X['spot']
    above = sorted([z for z in X['zones'] if z['bot'] > spot], key=lambda z: z['bot'])
    below = sorted([z for z in X['zones'] if z['top'] < spot], key=lambda z: -z['top'])
    pivot = next((z for z in X['zones'] if z['bot'] <= spot <= z['top']), None)

    def pick(ips, sds, up):
        z = next((q for q in ips if q['zfp_num'] < 30 and q['score'] >= 6 and min(abs(q['bot'] - spot), abs(q['top'] - spot)) <= 0.30 * X['U']), None)      # GS Law 2: SS zones 0-30 pips from spot
        if z is None and sds:
            q = sds[0]
            z = {'bot': q['bot'], 'top': q['top'], 'name': q['label'], 'zfp_num': 15 if q['kind'] == 'BoM' else 30, 'score': 6, 'sd': q}
        if z is None:
            z = _sweep_bound(X, up)
        return z if z is not None else (ips[0] if ips else None)
    # P452:753 (Step 0g): a 1H zone counts when its base preceded a move of >= 0.3; the same grade picks the supply-demand bound (L-37: the figure grades strength)
    strong = [q for q in X['sd'] if q['tf'] in ('240', '60') and q.get('excursion', 0.0) >= 0.30 * X['U']]
    pool = strong if strong else [q for q in X['sd'] if q['tf'] in ('240', '60')]
    sup = sorted([q for q in pool if q['type'] == 'Supply' and q['bot'] > spot], key=lambda q: q['bot'])
    dem = sorted([q for q in pool if q['type'] == 'Demand' and q['top'] < spot], key=lambda q: -q['top'])
    return pick(above, sup, True), pick(below, dem, False), pivot, above, below


def _sweep_bound(X, up):
    """a side that holds no pressure zone under 30% and no standing 1H / 4H supply-demand zone is bounded by its nearest unswept sweep zone lying wholly beyond spot:
    P533:1246-1262 the zone is '[exact high - 0.05, exact high]' / '[exact low, exact low + 0.05]'; P452:968 'Liquidity Sweep Zone ... high probability of brief breach then reversal';
    6.5 names the LSZ as the rejection anchor; FA 2.1 'LSZs = standard Earth density', FA 8 'consolidation ends in price retesting opposing liquidity'.
    Touching sweep zones are one cluster (its extreme = where the stops end)."""
    U, spot = X['U'], X['spot']
    side = 'Supply-side' if up else 'Demand-side'
    lv = sorted([z['level'] for z in X['lsz'] if z['side'] == side and not z['swept'] and ((z['level'] - 0.05 * U > spot) if up else (z['level'] + 0.05 * U < spot))], reverse=not up)
    if not lv:
        return None
    cl = [lv[0]]
    for p in lv[1:]:
        if abs(p - cl[-1]) <= 0.05 * U + 1e-12:
            cl.append(p)
    return {'bot': lv[0] - 0.05 * U if up else lv[0], 'top': lv[0] if up else lv[0] + 0.05 * U, 'ext': max(cl) if up else min(cl), 'sweep': True, 'name': 'Liquidity Sweep Zone', 'zfp_num': 15, 'score': 6}


def _target(X, side, bound, U):
    """6.5 / 6.8: BS target = 'Next Support / Resistance or Structural Extreme' beyond the failing bound; 6.4.2 last branch: 'pierce through zone until reaching BoM Liquidity'.
    The nearest of: a standing 1H / 4H supply-demand zone reaching beyond the bound, an unswept sweep zone, the next IP zone; joined with the unswept sweep zones lying against it
    (P533:1271-1273 'CONFLUENT LIQUIDITY SWEEP + BoM ZONE')"""
    dn = side == 'down'
    cands = []
    for z in X['sd']:
        if z['tf'] in ('240', '60') and z['type'] == ('Demand' if dn else 'Supply') and z['kind'] == 'BoM':
            if (z['top'] <= bound['top'] and z['bot'] < bound['bot']) if dn else (z['bot'] >= bound['bot'] and z['top'] > bound['top']):
                cands.append((z['top'] if dn else z['bot'], 0, {'bot': z['bot'], 'top': z['top'], 'name': f"{SD.TFNAME[z['tf']]} {z['kind']} {z['type']}", 'sd': z,
                                                               'always_reacts': z['kind'] == 'BoM', 'zfp': 10 if z['kind'] == 'BoM' else (70 if z['mit'] >= 3 else 30)}))
    lsz = sorted([z['level'] for z in X['lsz'] if z['side'] == ('Demand-side' if dn else 'Supply-side') and not z['swept']
                  and ((z['level'] < bound['bot']) if dn else (z['level'] > bound['top']))], reverse=dn)
    for p in lsz[:1]:
        cands.append((p + 0.05 * U if dn else p - 0.05 * U, 1, {'bot': p if dn else p - 0.05 * U, 'top': p + 0.05 * U if dn else p, 'name': 'Liquidity Sweep Target', 'always_reacts': True, 'zfp': 15}))
    for z in X['zones']:
        if ((z['top'] < bound['bot']) if dn else (z['bot'] > bound['top'])) and z['zfp_num'] < 30:
            cands.append((z['top'] if dn else z['bot'], 2, {'bot': z['bot'], 'top': z['top'], 'name': z['name'], 'always_reacts': False, 'zfp': z['zfp_num']}))
    if not cands:                                            # nothing that holds is mapped beyond the bound: the next zone of any class
        for z in X['sd']:
            if z['tf'] in ('240', '60') and z['type'] == ('Demand' if dn else 'Supply') and ((z['top'] <= bound['top'] and z['bot'] < bound['bot']) if dn else (z['bot'] >= bound['bot'] and z['top'] > bound['top'])):
                cands.append((z['top'] if dn else z['bot'], 3, {'bot': z['bot'], 'top': z['top'], 'name': f"{SD.TFNAME[z['tf']]} {z['kind']} {z['type']}", 'sd': z, 'always_reacts': False, 'zfp': 70 if z['mit'] >= 3 else 30}))
        for z in X['zones']:
            if (z['top'] < bound['bot']) if dn else (z['bot'] > bound['top']):
                cands.append((z['top'] if dn else z['bot'], 4, {'bot': z['bot'], 'top': z['top'], 'name': z['name'], 'always_reacts': False, 'zfp': z['zfp_num']}))
    if not cands:
        return None
    t = sorted(cands, key=lambda c: (-c[0] if dn else c[0], c[1]))[0][2]
    for p in lsz:                                            # sweep zones lying against / inside the target: within the canon cluster distance 0.15
        if dn and t['bot'] - 0.15 * U <= p <= t['top']:
            t['bot'] = min(t['bot'], p); t['always_reacts'] = True; t['zfp'] = min(t['zfp'], 15); t['name'] += ' + sweep zone' if 'sweep' not in t['name'].lower() else ''
        if (not dn) and t['bot'] <= p <= t['top'] + 0.15 * U:
            t['top'] = max(t['top'], p); t['always_reacts'] = True; t['zfp'] = min(t['zfp'], 15); t['name'] += ' + sweep zone' if 'sweep' not in t['name'].lower() else ''
    return t


def _mom(z):
    """the bound is a Middle-of-Move supply / demand zone (P452:694-697)"""
    return bool(z) and z.get('sd') is not None and z['sd']['kind'] == 'MoM'


def _after_bs(t):
    """6.4.1: the TARGET zone's ZFP decides what follows a Breakout Surge"""
    if t is None:
        return 'R', 'MODERATE', 'no mapped zone beyond: stabilization'
    if t['always_reacts'] or t['zfp'] < 20:
        return 'WL+RWL', 'HIGH', f"target {t['name']} = Hard Wall class (ZFP < 20% / unmitigated BoM always reacts): rejection, NOT R / PBS"
    if t['zfp'] <= 40:
        return 'R', 'HIGH', f"target {t['name']} ZFP {t['zfp']}% (20-40): stabilization"
    if t['zfp'] > 60:
        return 'PBS', 'MODERATE', f"target {t['name']} ZFP {t['zfp']}% (> 60): cascade continues"
    return 'R', 'MODERATE', f"target {t['name']} ZFP {t['zfp']}% (40-60): pause"


def build(pair, monday, X, lead=None, force_dir=None):
    """lead = the DXY chain when translating to a pair: same shapes, inverted direction (P533:1899-1917), on the pair's own zones"""
    U, spot = X['U'], X['spot']
    ceil, floor, pivot, above, below = _bounds(X)
    story, sz = storyline(pair, monday)
    s0 = current_shape(X)
    audit = [f"Current shape: {s0['shape']} {s0['dir']} | {s0['why']}"]
    inv = {'up': 'down', 'down': 'up', 'range': 'range', None: None}
    failing = None
    for side, z in (('up', ceil), ('down', floor)):
        if z is not None and z['zfp_num'] > 45:
            failing = (side, z)
    # ── direction of the breakout that ends the consolidation
    if force_dir is not None:
        bdir, why = force_dir, 'ALTERNATIVE chain (6.6 Step 4): the breakout through the other bound'
    elif lead is not None:
        bdir, why = inv[lead['bdir']], f"pair translation of the DXY chain ({lead['bdir']} inverted)"
    elif s0['shape'] in ('BS', 'PBS'):
        bdir, why = s0['dir'], 'breakout in progress'
    elif failing:
        bdir, why = failing[0], f"bounding zone {failing[1]['name']} ZFP {failing[1]['zfp_num']}% > 45: failing (6.4.1)"
    elif _mom(ceil) != _mom(floor):
        # 6.4.2 last branch: 'Consolidation ends in price retesting opposing liquidity -> Then pierce through zone until reaching BoM Liquidity' (the zone = the MoM zone under test);
        # 4H MoM one-and-done: 'minor WL followed by BS / PBS through the zone'; FA 7: only BoM zones reverse a move, MoM zones in the path are consumed
        bdir = 'up' if _mom(ceil) else 'down'
        z = ceil if _mom(ceil) else floor
        why = f"the {'ceiling' if _mom(ceil) else 'floor'} is a MoM zone ({z['name']}), the other bound is not: the consolidation ends piercing the MoM zone toward BoM liquidity (6.4.2)"
    else:
        bdir, why = story, (f"both bounding zones hold (ZFP < 30 / < 45): 4H storyline tiebreaker = {story} (last 4H origin zone {sz['type']} {sz['bot']:.5g}-{sz['top']:.5g})" if sz else 'no 4H origin zone')
    if bdir is None:
        bdir, why = 'down', 'no storyline: default'
    audit.append(f"Breakout direction: {bdir} | {why}")
    near, far = (floor, ceil) if bdir == 'down' else (ceil, floor)          # near = the bound the breakout goes through; far = the opposing liquidity retested first (6.4.2)
    tgt = _target(X, bdir, near, U) if near is not None else None
    if tgt is None and floor is not None and ceil is not None:
        h = ceil['bot'] - floor['top']                       # the range the breakout leaves
        p = ceil['top'] + h if bdir == 'up' else floor['bot'] - h
        tgt = {'bot': min(p, p - 0.05 * U) if bdir == 'up' else p, 'top': p if bdir == 'up' else p + 0.05 * U, 'name': 'BREAKOUT EXTENSION TARGET (measured move)', 'always_reacts': False, 'zfp': 30}
    # a breakout already running at the anchor (6.3 'BS -> R -> RWL', 'BS -> RWL -> SS -> BS': "Week opens with BS"): its target is the NEXT support / resistance (6.8) = the near bound itself;
    # what lies beyond that bound is the target of the cycle's second breakout
    mode = lead.get('mode', 'ss') if lead is not None else ('bs0' if (s0['shape'] in ('BS', 'PBS') and force_dir is None) else 'ss')
    tgt2 = None
    if mode == 'bs0' and near is not None:
        tgt2 = tgt
        sdz = near.get('sd')
        tgt = {'bot': near['bot'], 'top': near['top'], 'name': near['name'], 'zfp': near['zfp_num'],
               'always_reacts': bool(near.get('sweep')) or (sdz is not None and sdz['kind'] == 'BoM' and sdz['mit'] <= 1)}
        if sdz is not None:
            tgt['sd'] = sdz
    nxt, conf_t, why_t = _after_bs(tgt)
    # ── chain + timing: durations 6.8 (SS 2-5 sessions, BS 1-3, WL / RWL / R < 1), Trading Speed Rule 6.10 (+1 day)
    n_real = 5
    if lead is not None:
        plan = [list(d['shapes']) for d in lead['days']]
        n_real = lead.get('n_real', 5)
        audit.append('Day shapes = the DXY day shapes (same shapes, inverted direction)')
    elif mode == 'bs0':
        # 6.3 'BS -> RWL -> SS -> BS: complete false breakout cycle. Second BS often succeeds' / 'BS -> R -> PBS'; durations 6.8 (BS 1-3 sessions, WL / RWL / R < 1, SS 2-5)
        plan = [['BS'], ['WL', 'RWL'] if nxt == 'WL+RWL' else [nxt], ['SS'], ['SS'], ['SS', 'BS']]
        audit.append(f"BS {bdir} in progress -> [Trigger: {tgt['name'] if tgt else 'none'}] -> {nxt} ({why_t}) -> SS (RWL / R -> SS, 6.4) -> BS {bdir} (second breakout, 6.3) -> {tgt2['name'] if tgt2 else '-'}")
    else:
        n_ss = 1 if s0.get('phase') == 'late' else 2       # FA 9: 1-2 full days after two piercing moves; 6.4.2: slow consolidation 2-4 days; a late consolidation breaks sooner
        plan = [['SS'] for _ in range(n_ss)] + [['SS', 'RWL', 'BS']] + [['BS'] for _ in range(5)]
        plan = plan[:4] if n_ss == 2 else plan[:3]
        plan.append([nxt] if nxt != 'WL+RWL' else ['WL', 'RWL'])
        n_real = len(plan)                                   # the chain ends here (6.6 Step 3: max 5 shapes / confidence); later days carry no designation
        while len(plan) < 5:
            plan.append(['SS'])
        audit.append(f"SS ({n_ss} session{'s' if n_ss > 1 else ''}) -> [Trigger: consolidation ends retesting the opposing liquidity {far['name'] if far else '-'}, 6.4.2] -> RWL -> BS {bdir} through {near['name'] if near else '-'} "
                     f"-> [Trigger: {tgt['name'] if tgt else 'none'}] -> {nxt} ({why_t})")
    # ── cumulative confidence (6.6 Step 3)
    steps = [('SS', 'HIGH' if not failing else 'MODERATE'), ('BS', 'MODERATE-HIGH' if not failing else 'HIGH'), (nxt, conf_t)]
    if mode == 'bs0':
        steps = [('BS', 'HIGH'), (nxt, conf_t), ('SS', 'HIGH'), ('BS', 'MODERATE-HIGH')]
    cum, chain = 1.0, []
    for sh, tier in steps:
        cum *= CONF[tier]
        chain.append({'shape': sh, 'tier': tier, 'cum': round(cum, 2)})
        if cum < 0.25:
            break
    # ── day-by-day decomposition (6.6 Step 5) and the path
    f_edge = floor['top'] if floor else spot - 0.3 * U
    c_edge = ceil['bot'] if ceil else spot + 0.3 * U
    lo_edge, hi_edge = f_edge, c_edge
    mid = (pivot['bot'] + pivot['top']) / 2 if pivot else (f_edge + c_edge) / 2
    wk0 = D.week_start_ms(monday)
    days, pos = [], spot
    t_anchor = D.boundary_ms(monday)
    pts = [(t_anchor, spot)]
    toward_far = (far['bot'] if bdir == 'down' else far['top']) if far else (c_edge if bdir == 'down' else f_edge)        # the opposing-liquidity edge price retests before the breakout
    far_pierce = (far['top'] if bdir == 'down' else far['bot']) if far else toward_far
    near_edge = (near['top'] if bdir == 'down' else near['bot']) if near else (f_edge if bdir == 'down' else c_edge)
    near_far = (near['bot'] if bdir == 'down' else near['top']) if near else near_edge
    t_in = (tgt['top'] if bdir == 'down' else tgt['bot']) if tgt else near_far
    t_out = (tgt['bot'] if bdir == 'down' else tgt['top']) if tgt else near_far
    ss_seen = 0
    legs = []                                                # every expected zone-to-zone move of the week, in order: the input of Engine 3 (R3 law: E2 designates, E3 obeys)
    piv_far = ((pivot['bot'] if bdir == 'down' else pivot['top']) if pivot else mid)       # the pivot edge on the breakout side

    def leg(day, shape, a, b, t_end, frm, to):
        legs.append({'day': day, 'shape': shape, 'dir': 'up' if b > a else 'down', 'from': a, 'to': b, 'from_zone': frm, 'to_zone': to, 't0': pts[-1][0], 't1': t_end, 'pad': DAYS.index(day) >= n_real})
        pts.append((t_end, b))
        return b
    for i, shapes in enumerate(plan[:5]):
        d0 = wk0 + i * 86400000; d1 = d0 + 86400000
        start = max(d0, t_anchor) if i == 0 else d0
        day = {'day': DAYS[i], 'date': (dt.date.fromisoformat(monday) + dt.timedelta(days=i)).isoformat(), 'shapes': shapes, 't0': start, 't1': d1}
        p0 = pos
        if shapes == ['SS']:
            # one swing per session (6.1.1 'Each swing typically spans 1-3 trading sessions'): first toward the bound farther from price, then back
            left = 0                                         # consecutive SS sessions from this one on: the last of them ends at the opposing liquidity
            for p in plan[i:5]:
                if p != ['SS']:
                    break
                left += 1
            to_far = (left % 2 == 1)
            go_down = (bdir == 'up') if to_far else (bdir == 'down')
            pos = leg(DAYS[i], 'SS', pos, f_edge if go_down else c_edge, d1 - 4 * 3600000, None, floor if go_down else ceil)
            day.update(dir='range', lo=f_edge, hi=c_edge, key=(floor if go_down else ceil)['name'] if (floor if go_down else ceil) else '-', conf=chain[0]['cum']); ss_seen += 1
        elif shapes == ['SS', 'RWL', 'BS']:
            # SS swing back to the pivot, RWL into the opposing liquidity (6.4.2 'consolidation ends in price retesting opposing liquidity'), then the breakout
            if (pos > piv_far) == (bdir == 'down') and abs(pos - piv_far) > 1e-12:
                pos = leg(DAYS[i], 'SS', pos, piv_far, d0 + 7 * 3600000, far, pivot)
            pos = leg(DAYS[i], 'RWL', pos, far_pierce, d0 + 14 * 3600000, pivot, far)
            pos = leg(DAYS[i], 'BS', pos, mid, d1 - 3 * 3600000, far, tgt)
            day.update(dir=bdir, lo=min(piv_far, mid, far_pierce, toward_far), hi=max(piv_far, mid, far_pierce, toward_far), key=far['name'] if far else '-', conf=chain[min(1, len(chain) - 1)]['cum'])
        elif shapes == ['BS']:
            # 6.10 "TODAY'S move is the journey TO what I thought today's move will be": a continuation day reaches the bound; the day after pierces it to the target
            more = any(p not in (['BS'], ['SS']) for p in plan[i + 1:5])
            reached = abs(pos - near_edge) < 1e-12 or ((pos < near_edge) == (bdir == 'down'))
            b_ = near_edge if (more and not reached) else near_far if ((pos > near_far) == (bdir == 'down')) else t_in
            pos = leg(DAYS[i], 'BS', pos, b_, d1 - 4 * 3600000, far, tgt)
            day.update(dir=bdir, lo=min(p0, pos), hi=max(p0, pos), key=near['name'] if near else '-', conf=chain[min(1, len(chain) - 1)]['cum'])
        elif shapes in (['WL', 'RWL'], ['RWL'], ['WL']):
            # 6.8: WL / RWL target = 'Origin zone (return)'; within the session the return reaches the pivot's near edge
            rec = piv_far
            pos = leg(DAYS[i], 'BS', pos, t_out, d0 + 10 * 3600000, far, tgt)
            pos = leg(DAYS[i], 'WL', pos, rec, d1 - 4 * 3600000, tgt, pivot)
            day.update(dir=inv[bdir], lo=min(t_out, rec, p0), hi=max(t_out, rec, p0), key=tgt['name'] if tgt else '-', conf=chain[-1]['cum'])
        elif shapes == ['PBS']:
            z2 = tgt2 if (mode == 'bs0' and tgt2 is not None) else tgt      # the cascade continues through the weak zone to the next one (6.4.1 'BS > 60% -> PBS')
            pos = leg(DAYS[i], 'PBS', pos, ((z2['top'] if bdir == 'down' else z2['bot']) if z2 is not tgt else t_out) if z2 else t_out, d1 - 4 * 3600000, far, z2)
            day.update(dir=bdir, lo=min(p0, pos), hi=max(p0, pos), key=z2['name'] if z2 else '-', conf=chain[min(1, len(chain) - 1)]['cum'])
        elif shapes == ['SS', 'BS']:
            # the second breakout of the cycle (6.3 'BS -> RWL -> SS -> BS ... Second BS often succeeds'): from the opposing liquidity through the bound to the next target
            z2 = tgt2 if tgt2 is not None else tgt
            pos = leg(DAYS[i], 'BS', pos, (z2['top'] if bdir == 'down' else z2['bot']) if z2 else near_far, d1 - 4 * 3600000, far, z2)
            day.update(dir=bdir, lo=min(p0, pos), hi=max(p0, pos), key=z2['name'] if z2 else '-', conf=chain[-1]['cum'])
        else:                                                # R: stabilization at the target
            pos = leg(DAYS[i], 'R', pos, (t_in + t_out) / 2, d1 - 4 * 3600000, tgt, tgt)
            day.update(dir='range', lo=min(p0, t_in, t_out), hi=max(p0, t_in, t_out), key=tgt['name'] if tgt else '-', conf=chain[-1]['cum'])
        days.append(day)
    alt = None
    if far is not None:
        a_t = _target(X, inv[bdir], far, U)
        a_n, _, _ = _after_bs(a_t)
        prim = f"BS {bdir} -> {nxt} -> SS -> BS {bdir}" if mode == 'bs0' else f"SS -> BS {bdir} -> {nxt}"
        alt = {'decision_zone': far['name'], 'dir': inv[bdir], 'target': a_t,
               'text': f"PRIMARY: {prim} | DECISION ZONE: {far['name']} fails (1H close beyond it) -> ALTERNATIVE: SS -> BS {inv[bdir]} -> {a_n} at {a_t['name'] if a_t else '-'}"}
        audit.append(alt['text'])
    alt_chain = None
    if force_dir is None and s0['shape'] not in ('BS', 'PBS'):
        alt_chain = build(pair, monday, X, lead, force_dir=inv[bdir])      # the same map read with the other bound failing: its legs feed the conditional (ALT) setups of Engine 3
    return {'alt_chain': alt_chain, 'pair': pair, 'monday': monday, 's0': s0, 'storyline': story, 'bdir': bdir, 'chain': chain, 'days': days, 'path': pts, 'alt': alt, 'audit': audit,
            'ceil': ceil, 'floor': floor, 'pivot': pivot, 'target': tgt, 'target2': tgt2, 'mode': mode, 'next': nxt, 'range': (f_edge, c_edge), 'mid': mid, 'far': far, 'near': near,
            'legs': legs, 'n_real': n_real}


def pine(pair, monday, E2):
    """R-03: the day BOXES, then the LINE"""
    g = lambda v: ('%.3f' if pair == 'DXY' else '%.5f') % v
    col = {'SS': '120,144,156', 'BS': '255,167,38', 'PBS': '255,112,67', 'WL': '171,71,188', 'RWL': '171,71,188', 'R': '102,187,106'}
    arrow = {'up': ' up', 'down': ' down', 'range': ''}
    o = ['    if show_e2']
    for d in E2['days']:
        c = col[d['shapes'][-1]]
        o.append(f"        box.new({d['t0']}, {g(d['hi'])}, {d['t1']}, {g(d['lo'])}, bgcolor=color.new(color.rgb({c}), 88), border_color=color.new(color.rgb({c}), 20), border_width=1, border_style=line.style_dashed, xloc=xloc.bar_time)")
        o.append(f"        label.new({d['t0'] + 3600000}, {g(d['hi'])}, \"{d['day']}: {' + '.join(d['shapes'])}{arrow[d['dir']]}\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.rgb({c}), size=size.small)")
    p = E2['path']
    for (t0, p0), (t1, p1) in zip(p, p[1:]):
        o.append(f"        line.new({t0}, {g(p0)}, {t1}, {g(p1)}, xloc=xloc.bar_time, color=color.rgb(255,235,59), width=2)")
    return o


if __name__ == '__main__':
    import sys, e1_pine as EP
    monday, pair = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'DXY'
    lead = build('DXY', monday, EP.run('DXY', monday)) if pair != 'DXY' else None
    E2 = build(pair, monday, EP.run(pair, monday), lead)
    f = '%.3f' if pair == 'DXY' else '%.5f'
    for a in E2['audit']:
        print(a)
    print('chain:', ' -> '.join(f"{c['shape']} [{c['tier']}, cum {c['cum']}]" for c in E2['chain']))
    for d in E2['days']:
        print(f"  {d['day']} {d['date']}: {' + '.join(d['shapes']):<14} {d['dir']:<5} | Key Zone: {d['key']:<28} | {f % d['lo']}-{f % d['hi']} | Confidence: {int(d['conf'] * 100)}%")
    print('path:', ' -> '.join(f % p for _, p in E2['path']))
    for l in E2['legs']:
        print(f"  leg {l['day']} {l['shape']:<4} {l['dir']:<5} {f % l['from']} -> {f % l['to']}")
