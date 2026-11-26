"""e3_trades.py - ENGINE 3: trade setups = price engineering on the Engine 1 map along the Engine 2 legs (canon/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md = E3C, R-16).
R3 law (E3C:72-73): "E2 DESIGNATES, E3 OBEYS. ... Every anchor traces to an E1 zone ID + an E2 shape day." E3 "resolves only the executable geometry - the entry at the anchor's
internal-LQZ near/deep edge, the SL at the ... ladder step, the TP at the Law-14 opposing-rung walk" (E3C:76).
One trade per Engine 2 leg, chained (E3C Law 27: the TP zone of trade N is the entry zone of trade N+1):
  ENTRY  E3C:177-203  TS-1 sniper entry = zone edge closest to approaching price (short: bottom of supply, long: top of demand); F1-A order-block short +1 pip; F1-C internal LQZ rung near edge;
                      F1-D bounce inset 0.2 pip. Entry sources = ORDER_BLOCK / LQZ only (E3C:139-143); IP zones are confluence + SL / TP rungs.
  SL     E3C:247-296  ladder steps: 3 pips outside the far edge of the current step, or behind the next rung ("1-2 pips OUTSIDE THE BACK EDGE OF THE STOP-LOSS ZONE"); GS Law 4: outside a liquidity
                      shield; golden stops 4-9.5 pips; D17 ceiling 36 pips.
  TP     E3C:298-352  ONE TP at the opposing pressure, the E2-projected zone first; LQZ inside the zone -> midpoint; strong zone -> near edge + 1 pip spread; weak zone -> far edge.
  RRR    E3C:354-386  floor 3.0; a failing setup is re-anchored (SL / TP) up to three times before the hard reject.
  REINF  E3C:619-687  on the breakout primary: stop-limit at an intermediate LQZ rung on the TP path, own SL 1 pip outside the back edge of the next rung, the parent's TP.
Drawn as POSITION BOXES (R-09): red = SL side, green = entry -> TP, entry on their shared edge. At most 11 setups per pair per week.
No price literal: every level is an E1 zone edge, an LQZ band or a sweep-zone level."""
import e1_data as D

RRR_FLOOR, GOLD_MIN, GOLD_MAX, SL_CEIL, MAX_SETUPS = 3.0, 4.0, 9.5, 36.0, 11
ALT_SETUPS = False       # the alternative chain's breakout setups need their Decision Zone trigger (6.6 Step 4) before they may rest as orders: not emitted until that trigger is built
TF_RANK = {'15': 0, '30': 1, '60': 2, '240': 3}
DAY_IDX = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4}
SD_TF = {'240': '4H', '60': '1H', '30': '30m', '15': '15m'}
CAT = {'SS': 'Swing Scalp', 'RWL': 'Reversal', 'WL': 'HTF Swing', 'BS': 'HTF Swing', 'PBS': 'HTF Swing', 'R': 'Swing Scalp'}
SESSION = {'Swing Scalp': 'London', 'Reversal': 'NY', 'HTF Swing': 'NY', 'Reinforcement': 'NY Open'}      # E3C:147-152


def _env(X, pair):
    pip = D.PIP[pair]
    rungs = sorted(X['v1']['60']['liquidity'], key=lambda z: z['bot'])                   # LQZ = the sealed V1's liquidity bands at the anchor (R-30)
    blocks = [{'bot': z['bot'], 'top': z['top'], 'tf': tf, 'type': z['side'], 'src': 'V1 order block'} for tf in ('240', '60', '30', '15') for z in X['v1'][tf]['order_blocks']]
    sd = [dict(z) for z in X['sd']]
    # GS Law 5 / P533:1312-1340 (Step 0.6): a supply / demand zone holding no liquidity band carries its own Fibonacci levels (0.382 / 0.5 / 0.618 / 0.786 of the zone's range)
    # as its internal steps - the operator's GBPUSD rungs inside the 1H demand zone sit on them
    for z in sd:
        if z['tf'] in ('240', '60') and not any(r['bot'] >= z['bot'] and r['top'] <= z['top'] for r in rungs):
            for f in (0.382, 0.5, 0.618, 0.786):
                p = z['bot'] + f * (z['top'] - z['bot'])
                rungs.append({'bot': p, 'top': p, 'fib': f})
    rungs.sort(key=lambda z: z['bot'])
    return pip, rungs, blocks, sd


def _overlap(a, b):
    return a['bot'] <= b['top'] and a['top'] >= b['bot']


def _inside(a, b):
    return b['bot'] <= a['bot'] and a['top'] <= b['top']


def _entries(anchor, direction, shape, env, pair):
    """E3C:177-203 entry candidates inside the anchor zone, in refinement order (E3C:372-386 '3 attempts on each anchor'):
    TS-1 the zone edge closest to approaching price -> F1-C the internal LQZ rung near edge -> F1-A (SHORT only) a nested lower-timeframe order block, 1 pip above its bottom.
    (the spec's own Monday example: band bottom 101.027 gave RRR 1.79 -> rejected; the nested block entry 101.14 gave 4.92)"""
    pip, rungs, blocks, sd = env
    typ = 'Supply' if direction == 'down' else 'Demand'
    inset = 0.2 * pip if shape in ('RWL', 'WL') else 0.0     # F1-D
    if anchor.get('sweep'):
        mid = ((anchor['bot'] + anchor['top']) / 2, anchor, 'sweep zone mid')
        if shape == 'WL':                                    # whiplash into a sweep zone: the middle of the zone the stops rest in (operator's golden Friday long; GS Law 3 'Whiplash: post-spike entry')
            return [mid]
        # every other shape meets the sweep zone as a bound: TS-1 'zone edge CLOSEST to approaching price' (E3C:177-181), then the middle
        return [(anchor['bot'] if direction == 'down' else anchor['top'], anchor, 'sweep zone near edge (TS-1)'), mid]
    out = []
    real = [r for r in rungs if 'fib' not in r]
    if anchor.get('ip'):                                     # an IP zone is never an entry source: the LQZ rung at it is (E3C:139-143)
        inner = [r for r in real if _overlap(r, anchor)]
        inner.sort(key=lambda r: r['bot'] if direction == 'down' else -r['top'])
        for r in inner[:3]:
            out.append((r['bot'] if direction == 'down' else r['top'] - inset, r, 'LQZ rung at the zone'))
        if not out:
            out.append((anchor['bot'] if direction == 'down' else anchor['top'], anchor, 'zone edge (TS-1)'))
        return out
    # priority = the spec's measured fixes first: F1-A (order-block SHORT) -> F1-C (internal LQZ rung, "NOT the zone's defendedEdge") -> TS-1 zone edge; the next one is tried when RRR fails
    if direction == 'down':
        rank = TF_RANK.get(anchor.get('tf', '240'), 3)
        nested = [b for b in blocks if b['type'] == typ and TF_RANK[b['tf']] < max(rank, 1) and anchor['bot'] <= b['bot'] <= anchor['top']]
        for b in sorted(nested, key=lambda b: (-TF_RANK[b['tf']], b['bot']))[:1]:
            out.append((b['bot'] + 1 * pip, b, f"{SD_TF[b['tf']]} order block bottom + 1 pip (F1-A)"))
    inner = [r for r in real if _inside(r, anchor)]
    inner.sort(key=lambda r: r['bot'] if direction == 'down' else -r['top'])
    for r in inner[:1]:
        out.append((r['bot'] if direction == 'down' else r['top'] - inset, r, 'internal LQZ rung'))
    out.append((anchor['bot'] if direction == 'down' else anchor['top'], anchor, 'zone edge (TS-1)'))
    return out


def _stops(entry, step, direction, env, anchor):
    """E3C:247-296 candidates, nearest first"""
    pip, rungs, blocks, sd = env
    out = []
    if anchor.get('sweep'):                                  # 1-2 pips outside the back edge of the stop-loss zone = beyond the swept extreme
        ext = anchor.get('ext', anchor['bot'] if direction == 'up' else anchor['top'])
        return [(ext - k * pip if direction == 'up' else ext + k * pip, 'outside the sweep extreme') for k in (1.3, 2.0)]      # "1-2 pips OUTSIDE THE BACK EDGE OF THE STOP-LOSS ZONE"

    far = step['top'] if direction == 'down' else step['bot']
    out.append((far + 3 * pip if direction == 'down' else far - 3 * pip, '3 pips outside the current step'))
    beyond = [r for r in rungs if (r['bot'] > entry if direction == 'down' else r['top'] < entry)]      # the shield: the first LQZ band lying wholly beyond the entry (GS Law 4)
    beyond.sort(key=lambda r: r['bot'] if direction == 'down' else -r['top'])
    for r in beyond[:3]:
        out.append((r['top'] + 1 * pip if direction == 'down' else r['bot'] - 1 * pip, '1 pip outside the back edge of the next rung'))
    return out


NO_SHIELD = ('EURUSD',)   # E3C 8.19 pair table: EUR/USD 'DIRECT_ZONE_TEST, NO_SHIELD'; FA 10: 'PA often directly touches the overlap point ... No Liquidity Shield'


def _pick_stop(entry, cands, pip, category):
    """golden stops 4-9.5 pips (E3C:279-284). A swing scalp takes the tightest stop inside the envelope; a reversal / HTF swing stands behind the liquidity shield (next rung, GS Law 4:
    'For deep HTF swings: SL ... MUST be behind ... liquidity shield'), under the D17 ceiling of 36 pips"""
    d = [(abs(s - entry) / pip, s, why) for s, why in cands]
    gold = [x for x in d if GOLD_MIN <= x[0] <= GOLD_MAX]
    shield = [x for x in d if ('rung' in x[2] or 'sweep' in x[2]) and GOLD_MIN <= x[0] <= SL_CEIL]
    if category != 'Swing Scalp' and shield:
        return min(shield)[1:]
    if gold:
        return min(gold)[1:]
    ok = [x for x in d if GOLD_MIN <= x[0] <= SL_CEIL]
    return min(ok)[1:] if ok else (None, 'no stop inside the ceiling')


def _band_mid(z, rungs, inside=True):
    c = [r for r in rungs if (_inside(r, z) if inside else _overlap(r, z))]
    return c


def _target(leg, entry, direction, E2, X, env, used, pair):
    """E3C:298-352: the opposing pressure, the E2-projected zone first. Returns candidates (price, zone, why) in walk order (the refinement loop takes the next one)"""
    pip, rungs, blocks, sd = env
    U = X['U']
    opp = 'Demand' if direction == 'down' else 'Supply'
    end, tz = leg['to'], leg['to_zone']
    out = []
    ahead = lambda p: (p < entry) if direction == 'down' else (p > entry)
    if leg['shape'] in ('BS', 'PBS') and tz is not None:
        boms = sorted([z for z in sd if z['tf'] in ('240', '60') and z['type'] == opp and _overlap(z, tz)], key=lambda z: -z['top'] if direction == 'down' else z['bot'])      # the first zone the move reaches
        for z in boms:
            ins = [r for r in rungs if _inside(r, z)]
            if z['tf'] == '240' and z['kind'] == 'BoM':      # GS:477-481 a 4H zone reacts at once; E3C:320-327 STRONG zone (BoM) -> close edge + 1-2 pip spread "so you dont miss the exit"
                out.append((z['top'] + pip if direction == 'down' else z['bot'] - pip, z, '4H target zone near edge + 1 pip (strong zone)'))
            elif z['tf'] == '240' and ins:                   # E3C:306-309 rule 4: S/D + LQZ overlap (Earth + Fire convergence) -> TP at the zone MIDPOINT
                out.append(((z['bot'] + z['top']) / 2, z, '4H target zone midpoint (LQZ inside the zone, rule 4)'))
            for r in sorted(ins, key=lambda r: -r['top'] if direction == 'down' else r['bot']):
                out.append(((r['bot'] + r['top']) / 2, z, 'LQZ inside the target zone: midpoint'))
            out.append((z['top'] + pip if direction == 'down' else z['bot'] - pip, z, 'target zone near edge + 1 pip'))
        out.append((tz['top'] + pip if direction == 'down' else tz['bot'] - pip, tz, 'E2 target near edge + 1 pip'))
        return out
    if leg['shape'] == 'RWL' and tz is not None:
        out.append(((tz['bot'] + tz['top']) / 2, tz, 'opposing zone midpoint (pierce)'))
        out.append((tz['bot'] - pip if direction == 'up' else tz['top'] + pip, tz, 'opposing zone near edge + 1 pip'))
        return out
    if leg['shape'] == 'WL':
        side = 'Supply-side' if direction == 'up' else 'Demand-side'
        lz = [z for z in X['lsz'] if z['side'] == side and not z['swept'] and ahead(z['level'])
              and ((z['level'] <= end + 0.10 * U) if direction == 'up' else (z['level'] >= end - 0.10 * U))]
        lz.sort(key=lambda z: z['level'] if direction == 'up' else -z['level'])
        for z in lz:
            near = z['level'] - 0.05 * U if direction == 'up' else z['level'] + 0.05 * U
            box = {'bot': min(near, z['level']), 'top': max(near, z['level'])}
            rr = [r for r in rungs if r['bot'] <= near <= r['top'] or abs(((r['bot'] + r['top']) / 2) - near) <= 2 * pip]
            if rr:
                out.append(((rr[0]['bot'] + rr[0]['top']) / 2, box, 'LQZ at the opposing sweep zone: midpoint'))
            out.append((near - pip if direction == 'up' else near + pip, box, 'opposing sweep zone near edge + 1 pip'))
        if tz is not None:
            out.append((tz['bot'] - pip if direction == 'up' else tz['top'] + pip, tz, 'pivot near edge + 1 pip'))
        return out
    # SS / R: the nearest unconsumed opposing 1H / 4H zone on the way to the leg's end, the LQZ inside it; else the E2 zone itself
    zs = [z for z in sd if z['tf'] in ('240', '60') and z['type'] == opp and id(z) not in used and z.get('key') not in used
          and ahead(z['top'] if direction == 'down' else z['bot'])
          and (((z['top'] >= end) if direction == 'down' else (z['bot'] <= end)) or (tz is not None and _overlap(z, tz)))]       # on the way to the E2 leg end, or lying against the E2 zone
    zs.sort(key=lambda z: -z['top'] if direction == 'down' else z['bot'])
    for z in zs:
        ov = [r for r in rungs if _overlap(r, z)]
        for r in sorted(ov, key=lambda r: -r['top'] if direction == 'down' else r['bot']):
            out.append(((r['bot'] + r['top']) / 2, z, 'LQZ inside the opposing zone: midpoint'))
        out.append((z['top'] if direction == 'down' else z['bot'], z, 'opposing zone near edge'))
    if tz is None:
        rr = sorted(rungs, key=lambda r: abs((r['bot'] + r['top']) / 2 - end))
        if rr:
            out.append(((rr[0]['bot'] + rr[0]['top']) / 2, dict(rr[0], rung=True), 'LQZ rung at the range middle: midpoint'))
    if tz is not None:
        if tz.get('zfp_num', 40) < 30 and not (tz['bot'] <= X['spot'] <= tz['top']):
            out.append((tz['top'] + pip if direction == 'down' else tz['bot'] - pip, tz, 'bounding zone near edge + 1 pip (strong zone)'))
        else:                                                # weak zone / pivot: far edge, the LQZ band lying on it
            fe = tz['bot'] if direction == 'down' else tz['top']
            rr = sorted([r for r in rungs if r['bot'] - 2 * pip <= fe <= r['top'] + 2 * pip], key=lambda r: abs((r['bot'] + r['top']) / 2 - fe))
            if rr:
                out.append(((rr[0]['bot'] + rr[0]['top']) / 2, dict(rr[0], rung=True), 'LQZ on the far edge of the pivot: midpoint'))
            out.append((fe, tz, 'weak zone far edge'))
    return out


def _first_anchor(leg, X, env):
    """the first trade waits at the nearest 1H / 4H zone against the leg (short: supply at / above spot)"""
    pip, rungs, blocks, sd = env
    spot = X['spot']
    typ = 'Supply' if leg['dir'] == 'down' else 'Demand'
    zs = [z for z in sd if z['tf'] in ('240', '60') and z['type'] == typ and ((z['bot'] >= spot) if typ == 'Supply' else (z['top'] <= spot))]      # price has to travel to it
    zs.sort(key=lambda z: z['bot'] if typ == 'Supply' else -z['top'])
    return zs[0] if zs else None


def _bound_anchor(leg, E2):
    """no supply / demand zone on the waiting side: the Engine 2 bound of that side is the anchor (R3 law, E3C:72-73 'Every anchor traces to an E1 zone ID + an E2 shape day')"""
    z = E2.get('ceil') if leg['dir'] == 'down' else E2.get('floor')
    return dict(z) if z else None


def build(pair, monday, X, E2):
    """primary chain + the conditional setups of the ALTERNATIVE chain (P533 6.6 Step 4: 'For every primary chain, construct at least one alternative chain that activates if the primary
    fails at a specific Decision Zone'): only its breakout family (RWL / BS / WL) - the swing scalps are the same range for both readings"""
    R = _build(pair, monday, X, E2, '')
    alt = E2.get('alt_chain')
    if ALT_SETUPS and alt is not None:
        A = _build(pair, monday, X, alt, 'A')
        keep = [s for s in A['setups'] if s['shape'] in ('RWL', 'BS', 'PBS', 'WL', 'Ladder')]
        for s in keep:
            s['alt'] = True
            s['why'] = 'ALTERNATIVE chain (the other bound fails): ' + s['why']
        R['setups'] = (R['setups'] + keep)[:MAX_SETUPS]
        R['log'] += ['ALT ' + l for l in A['log']]
    b0 = D.boundary_ms(monday)
    ss_days = [DAY_IDX[d['day']] for d in E2['days'] if d['shapes'] == ['SS'] and DAY_IDX[d['day']] < E2.get('n_real', 5)]
    for s in R['setups']:
        day0 = D.week_start_ms(monday) + DAY_IDX[s['day']] * 86400000
        s['valid_from'] = max(day0, b0)
        s['valid_to'] = D.week_start_ms(monday) + (DAY_IDX[s['days'][-1]] + 1) * 86400000
        if s['shape'] == 'SS' and DAY_IDX[s['day']] in ss_days:
            # the swing scalps of a consolidation rest at both bounds for the whole consolidation (E3C Setup Universe: 'SS: Swing Scalps (both directions)'): which bound is met first is not designated
            run = [d for d in ss_days if all(x in ss_days for x in range(min(d, DAY_IDX[s['day']]), max(d, DAY_IDX[s['day']]) + 1))]
            s['valid_from'] = max(D.week_start_ms(monday) + min(run) * 86400000, b0)
            s['valid_to'] = D.week_start_ms(monday) + (max(run) + 1) * 86400000
    return R


def _build(pair, monday, X, E2, tag):
    env = _env(X, pair)
    pip, rungs, blocks, sd = env
    U = X['U']
    for i, z in enumerate(sd):
        z['key'] = (z['tf'], round(z['bot'], 6), round(z['top'], 6))
    legs = E2['legs']
    # merge the consecutive breakout legs into one trade (one entry, ONE TP at the E2 target)
    merged = []
    for l in legs:
        if merged and merged[-1]['shape'] in ('BS', 'PBS') and l['shape'] in ('BS', 'PBS') and merged[-1]['dir'] == l['dir']:
            merged[-1]['to'] = l['to']; merged[-1]['to_zone'] = l['to_zone']; merged[-1]['days'].append(l['day']); merged[-1]['t1'] = l['t1']
        else:
            m = dict(l); m['days'] = [l['day']]; merged.append(m)
    setups, used, anchor, log = [], set(), None, []
    for k, leg in enumerate(merged):
        if leg.get('pad'):
            continue                                         # no E2 designation for that day -> no setup (R3 law)
        direction = leg['dir']
        if anchor is None:
            anchor = _first_anchor(leg, X, env) or _bound_anchor(leg, E2)
            if anchor is None:
                log.append(f"{leg['day']} {leg['shape']}: no entry source against the leg"); continue
        a = dict(anchor)
        if 'zfp_num' in a and 'tf' not in a:
            a['ip'] = True                                   # an IP zone is never an entry source (E3C:139-143): the LQZ rung at it is
        if leg['shape'] == 'WL' and E2['target'] is not None:    # the whiplash is traded in the sweep zones of the E2 target: the first one price reaches; the stop beyond the cluster's extreme
            lv = sorted([z['level'] for z in X['lsz'] if not z['swept'] and E2['target']['bot'] - 1e-9 <= z['level'] <= E2['target']['top'] + 1e-9], reverse=(direction == 'up'))
            if lv:
                cl = [lv[0]]
                for p in lv[1:]:
                    if abs(p - cl[-1]) <= 0.05 * U + 1e-12:  # the next sweep zone touches this one: one cluster
                        cl.append(p)
                if direction == 'up':
                    a = {'bot': lv[0], 'top': lv[0] + 0.05 * U, 'ext': min(cl), 'sweep': True, 'name': 'sweep zone'}
                else:
                    a = {'bot': lv[0] - 0.05 * U, 'top': lv[0], 'ext': max(cl), 'sweep': True, 'name': 'sweep zone'}
        cat = CAT.get(leg['shape'], 'Swing Scalp')
        ecands = _entries(a, direction, leg['shape'], env, pair)
        if a.get('rung'):                                    # the previous TP rung: entry on its near edge for the new direction
            ecands = [((a['bot'] if direction == 'down' else a['top'] - (0.2 * pip if leg['shape'] in ('RWL', 'WL') else 0.0)), a, 'LQZ rung (previous TP rung)')]
        if leg['shape'] in ('BS', 'PBS') and setups and setups[-1]['shape'] == 'RWL':
            lvl = setups[-1]['tp']
            ecands = [(lvl, {'bot': lvl, 'top': lvl}, 'the reverse-whiplash TP level (Law 27: TP of N = entry of N+1)')]
        if pair != 'DXY':
            # E3C 10.4 (mirror lane): 'usedEuAnchors + alt-retry with excludedAnchorIds on collision' - an anchor already carrying a setup of that day and direction is excluded;
            # the mirror then takes the next liquidity step on the deep side (F1-C '#6 EU Wed deep-demand E 1.13935 = deep shield')
            taken = {q['src'] for q in setups if q['day'] == leg['days'][0] and q['dir'] == ('SHORT' if direction == 'down' else 'LONG') and q.get('src')}
            free = [c for c in ecands if (round(c[1]['bot'], 6), round(c[1]['top'], 6)) not in taken]
            if ecands and not free:
                edge = max(c[1]['top'] for c in ecands) if direction == 'down' else min(c[1]['bot'] for c in ecands)
                deep = [r for r in rungs if 'fib' not in r and ((r['bot'] > edge) if direction == 'down' else (r['top'] < edge))]
                deep.sort(key=lambda r: r['bot'] if direction == 'down' else -r['top'])
                free = [(r['bot'] if direction == 'down' else r['top'], r, 'next liquidity step beyond the used anchor (deep shield, F1-C; E3C 10.4 alt-retry)') for r in deep[:1]]
            ecands = free
        s, entry, stop, cands = None, None, None, []
        for entry, step, how in ecands[:3]:                  # E3C:372-386: up to three attempts per anchor - the entry, then the TP walk on it
            sc = _stops(entry, step, direction, env, a)
            if pair in NO_SHIELD and not a.get('sweep'):
                own = [c for c in sc if 'current step' in c[1] and GOLD_MIN <= abs(c[0] - entry) / pip <= SL_CEIL]
                sc = own or sc                               # ladder-steps rule (a): 3 pips outside the far edge of the current step (E3C:252-256)
            stop, why_sl = _pick_stop(entry, sc, pip, cat)
            cands = [c for c in _target(leg, entry, direction, E2, X, env, used, pair) if ((c[0] < entry) if direction == 'down' else (c[0] > entry))]
            if stop is None:
                continue
            for tries, (tp, tz, why_tp) in enumerate(cands[:3], 1):
                rrr = abs(tp - entry) / abs(entry - stop)
                if rrr >= RRR_FLOOR:
                    s = {'dir': 'SHORT' if direction == 'down' else 'LONG', 'entry': entry, 'sl': stop, 'tp': tp, 'rrr': round(rrr, 2), 'tp_zone': tz, 'attempts': tries,
                         'why': f"entry {how}; SL {why_sl}; TP {why_tp}", 'src': (round(step['bot'], 6), round(step['top'], 6))}
                    break
            if s is not None:
                break
        if s is None:
            log.append(f"{leg['day']} {leg['shape']} {direction}: rejected (no TP with RRR >= {RRR_FLOOR} in three attempts; entry {entry:.5f} SL {stop})")
            anchor = (cands[0][1] if cands else leg['to_zone'])
            continue
        s.update(day=leg['days'][0], days=leg['days'], shape=leg['shape'], category=cat, session=SESSION[cat], sl_pips=round(abs(entry - stop) / pip, 1), t0=leg['t0'], t1=leg['t1'],
                 anchor=a, id=f"{pair[:2]}{tag}{len(setups) + 1}")
        setups.append(s)
        used.add(id(anchor)); used.add(anchor.get('key'))
        anchor = s['tp_zone']                                # Law 27: the TP zone is the next entry zone
        # reinforcement on the breakout primary (E3C:619-687): stop-limit at the first LQZ rung the move crosses beyond the pivot, own SL behind the next rung, the parent's TP
        if leg['shape'] in ('BS', 'PBS') and len(leg['days']) > 1:
            piv = E2['pivot']
            ref = (piv['bot'] if direction == 'down' else piv['top']) if piv else E2['mid']
            path = [r for r in rungs if ((r['top'] <= ref + 2 * pip and r['bot'] > s['tp']) if direction == 'down' else (r['bot'] >= ref - 2 * pip and r['top'] < s['tp']))]
            path.sort(key=lambda r: -r['top'] if direction == 'down' else r['bot'])
            if path:
                r = path[0]
                e2 = (r['bot'] + r['top']) / 2
                nxt = [q for q in rungs if (q['bot'] > r['top'] if direction == 'down' else q['top'] < r['bot'])]
                nxt.sort(key=lambda q: q['bot'] if direction == 'down' else -q['top'])
                if nxt:
                    sl2 = nxt[0]['top'] + pip if direction == 'down' else nxt[0]['bot'] - pip
                    if GOLD_MIN <= abs(sl2 - e2) / pip <= SL_CEIL and abs(s['tp'] - e2) / abs(e2 - sl2) >= RRR_FLOOR:      # the emission floor holds for every category (E3C:362-364)
                        setups.append({'dir': s['dir'], 'entry': e2, 'sl': sl2, 'tp': s['tp'], 'rrr': round(abs(s['tp'] - e2) / abs(e2 - sl2), 2), 'day': leg['days'][1], 'days': leg['days'][1:],
                                       't0': D.week_start_ms(monday) + DAY_IDX[leg['days'][1]] * 86400000, 't1': leg['t1'],
                                       'shape': 'Ladder', 'category': 'Reinforcement', 'session': SESSION['Reinforcement'], 'sl_pips': round(abs(sl2 - e2) / pip, 1), 'parent': s['id'],
                                       'id': f"{pair[:2]}{tag}{len(setups) + 1}", 'tp_zone': s['tp_zone'], 'anchor': r,
                                       'why': 'reinforcement: stop-limit at the LQZ rung on the TP path; SL 1 pip outside the back edge of the next rung; parent TP'})
    # Phase 6.3 (E3C:452-463): 'If both setups reference the same anchorZoneId -> dedup by anchor bucket + day identity'; MAX_MIRRORS_PER_ANCHOR_PER_DAY = 1, 'FIRST kept, rest drop EMISSION_CAPPED with logged reasons'
    kept, seen, dropped = [], set(), set()
    for q in setups:
        key = (q['day'], q['dir'], q.get('src'))
        if q.get('parent') in dropped or (q.get('src') is not None and key in seen):
            dropped.add(q['id'])
            log.append(f"{q['id']} {q['day']} {q['shape']} {q['dir']}: EMISSION_CAPPED - same anchor, same day as an earlier setup (Phase 6.3)")
            continue
        seen.add(key); kept.append(q)
    for i, q in enumerate(kept):                             # ids stay consecutive; a reinforcement keeps pointing at its parent
        new_id = f"{pair[:2]}{tag}{i + 1}"
        for c in kept:
            if c.get('parent') == q['id']:
                c['parent'] = new_id
        q['id'] = new_id
    return {'setups': kept[:MAX_SETUPS], 'log': log}


def pine(pair, monday, R):
    """R-09: position boxes - red = SL side, green = entry -> TP, entry on their shared edge; each box spans the time Engine 2 gives its leg"""
    g = lambda v: ('%.3f' if pair == 'DXY' else '%.5f') % v
    b0, wk1 = D.boundary_ms(monday), D.week_end_ms(monday)
    o = ['    if show_e3']
    if not R['setups']:
        o.append('        na')
    seen_day = set()
    for s in R['setups']:
        day0 = D.week_start_ms(monday) + DAY_IDX[s['day']] * 86400000
        first = s['day'] not in seen_day; seen_day.add(s['day'])
        x0 = max(day0 if first else s['t0'], b0)             # a setup is a resting order from the start of its day; later setups of the same day follow in leg order
        x1 = min(max(s['t1'], x0 + 6 * 3600000), wk1)
        o.append(f"        // {s['id']} {s['day']} {s['shape']} {s['dir']} E {g(s['entry'])} SL {g(s['sl'])} TP {g(s['tp'])} RRR {s['rrr']} | {s['category']} / {s['session']} | {s['why']}")
        o.append(f"        box.new({x0}, {g(max(s['entry'], s['sl']))}, {x1}, {g(min(s['entry'], s['sl']))}, bgcolor=color.new(color.rgb(242,54,69), {86 if s.get('alt') else 70}), border_color=color.rgb(242,54,69), border_width=1, border_style={'line.style_dashed' if s.get('alt') else 'line.style_solid'}, xloc=xloc.bar_time)")
        o.append(f"        box.new({x0}, {g(max(s['entry'], s['tp']))}, {x1}, {g(min(s['entry'], s['tp']))}, bgcolor=color.new(color.rgb(8,153,129), {88 if s.get('alt') else 76}), border_color=color.rgb(8,153,129), border_width=1, border_style={'line.style_dashed' if s.get('alt') else 'line.style_solid'}, xloc=xloc.bar_time)")
        o.append(f"        label.new({x0 + 1800000}, {g(s['tp'])}, \"{s['id']} {'ALT ' if s.get('alt') else ''}{s['shape']} {s['dir']} {s['rrr']}R\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.{'gray' if s.get('alt') else 'white'}, size=size.small)")
    return o


if __name__ == '__main__':
    import sys, json, os, e1_pine as EP, e2_chain as E2M
    monday, pair = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'DXY'
    X = EP.run(pair, monday)
    lead = E2M.build('DXY', monday, EP.run('DXY', monday)) if pair != 'DXY' else None
    E2 = E2M.build(pair, monday, X, lead)
    R = build(pair, monday, X, E2)
    f = '%.3f' if pair == 'DXY' else '%.5f'
    for s in R['setups']:
        print(f"{s['id']} {s['day']} {s['shape']:<6} {s['dir']:<5} E {f % s['entry']} SL {f % s['sl']} ({s['sl_pips']}p) TP {f % s['tp']} RRR {s['rrr']} | {s['category']} / {s['session']} | {s['why']}")
    for l in R['log']:
        print('  !', l)
    op = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'context_management', 'oracle', 'golden_week.json')
    if monday == '2026-07-06' and os.path.exists(op):        # bug locator only: distance of each setup to the operator's own trades (never a verdict)
        O = json.load(open(op))[pair]
        pip = D.PIP[pair]
        print('--- nearest oracle trade per setup (pips off: entry / SL / TP)')
        for s in R['setups']:
            best = min((t for t in O['trades'] if t['dir'] == s['dir'] and t.get('tp')), key=lambda t: abs(t['entry'] - s['entry']) + abs(t['tp'] - s['tp']), default=None)
            if best:
                print(f"  {s['id']} {s['day']} {s['shape']:<6} vs #{best['n']} {best['day']}: {abs(best['entry'] - s['entry']) / pip:5.1f} / {abs(best['sl'] - s['sl']) / pip:5.1f} / {abs(best['tp'] - s['tp']) / pip:5.1f}")
