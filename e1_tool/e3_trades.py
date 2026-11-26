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
DAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')
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
    (the spec's own measured example: E3C:186-188)"""
    pip, rungs, blocks, sd = env
    typ = 'Supply' if direction == 'down' else 'Demand'
    inset = 0.2 * pip if shape == 'RWL' else 0.0             # F1-D 'RWL_BOUNCE_INSET_PIPS' (E3C:196)
    if anchor.get('sweep'):
        mid = ((anchor['bot'] + anchor['top']) / 2, anchor, 'sweep zone mid')
        if shape in ('WL', 'RWL'):                           # whiplash into a sweep zone: the middle of the zone the stops rest in (operator's golden Friday long; GS Law 3 'Whiplash: post-spike entry')
            return [mid]
        # every other shape meets the sweep zone as a bound: TS-1 'zone edge CLOSEST to approaching price' (E3C:177-181), then the middle
        return [(anchor['bot'] if direction == 'down' else anchor['top'], anchor, 'sweep zone near edge (TS-1)'), mid]
    out = []
    real = [r for r in rungs if 'fib' not in r]
    if anchor.get('ip'):                                     # an IP zone is never an entry source: the ORDER_BLOCK / LQZ at it are (E3C:139-143 STRUCTURAL_ENTRY_SOURCES)
        inner = [r for r in real if _overlap(r, anchor)]
        for r in inner:
            out.append((r['bot'] if direction == 'down' else r['top'] - inset, r, 'LQZ rung at the zone'))
        # the candle structure of the pressure zone (L-39: zone = A candle structure + B levels joined): an order block of the trade's side lying mostly inside it (D-46)
        half = lambda b: (min(b['top'], anchor['top']) - max(b['bot'], anchor['bot'])) >= 0.5 * (b['top'] - b['bot'])
        obs = [b for b in blocks if b['type'] == typ and TF_RANK.get(b['tf'], 3) <= TF_RANK['60'] and half(b)] + \
              [dict(q, src='E1 S/D') for q in sd if q['type'] == typ and q['tf'] in ('60', '30', '15') and q.get('mit', 0) < 3 and half(q)]
        for b in obs:
            out.append(((b['bot'] + pip) if direction == 'down' else b['top'], b, f"{SD_TF.get(b['tf'], b['tf'])} order block at the zone, {'bottom + 1 pip (F1-A)' if direction == 'down' else 'top (TS-1)'}"))
        out.sort(key=lambda e: e[0] if direction == 'down' else -e[0])          # TS-1 'SNIPER ENTRY = zone edge CLOSEST to approaching price' (E3C:177-181)
        return out[:3]                                       # nothing at the IP zone -> no entry (SOURCE_INVALID, E3C:136)
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
        if tz.get('liq'):                                    # the retest ends at the opposing liquidity (6.4.2): STRONG -> its near edge + 1 pip spread (E3C:320-327)
            out.append((tz['bot'] - pip if direction == 'up' else tz['top'] + pip, tz, 'opposing liquidity near edge + 1 pip (6.4.2 retest)'))
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
    # SS / R: the E2-projected opposing zone FIRST (E3C:333), then the walk over the opposing 1H / 4H zones on the way (LQZ inside -> midpoint, else near edge)
    if tz is not None and tz.get('zfp_num', 40) < 30 and not (tz['bot'] <= X['spot'] <= tz['top']):
        out.append((tz['top'] + pip if direction == 'down' else tz['bot'] - pip, tz, 'E2 bounding zone near edge + 1 pip (strong zone, E3C:320-327)'))
    if tz is not None and 'tf' in tz and 'zfp_num' not in tz and not (tz['bot'] <= X['spot'] <= tz['top']):
        # the E2 zone is a supply / demand candle zone (no ZFP of its own, G2 C-01): E3C:333 'E2-shapeDay projected opposing zone ... FIRST'; rule 5 'no LQZ overlap -> TP at zone NEAR EDGE',
        # BoM = STRONG -> 'closest zone edge ... add a 1-2 pip spread' (E3C:320-327)
        sp = pip if tz.get('kind') == 'BoM' else 0.0
        out.append((tz['top'] + sp if direction == 'down' else tz['bot'] - sp, tz, f"E2 bounding supply / demand zone near edge{' + 1 pip (BoM)' if sp else ''} (E3C:333, rule 5)"))
    if tz is not None and tz.get('liq'):                     # a thick liquidity band (V1 4H) = strong pressure: 'exit on the closest zone edge' (E3C:320-327)
        out.append((tz['top'] if direction == 'down' else tz['bot'], tz, 'liquidity band near edge (strong, E3C:320-327)'))
    zs = [z for z in sd if z['tf'] in ('240', '60') and z['type'] == opp and id(z) not in used and z.get('key') not in used
          and ahead(z['top'] if direction == 'down' else z['bot'])
          and (((z['top'] >= end) if direction == 'down' else (z['bot'] <= end)) or (tz is not None and _overlap(z, tz)))]       # on the way to the E2 leg end, or lying against the E2 zone
    zs.sort(key=lambda z: -z['top'] if direction == 'down' else z['bot'])
    for z in zs:
        ov = [r for r in rungs if _overlap(r, z)]
        for r in sorted(ov, key=lambda r: -r['top'] if direction == 'down' else r['bot']):
            out.append(((r['bot'] + r['top']) / 2, z, 'LQZ inside the opposing zone: midpoint'))
        out.append((z['top'] if direction == 'down' else z['bot'], z, 'opposing zone near edge'))
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


LAW7 = {'DXY': 5, 'EURUSD': 2, 'GBPUSD': 3}       # E3C:299-304 per-pair SL buffers (pips; DXY in index points of 0.01)
MAX_RRR = 15.0                                   # E3C:365 'MAX_CHAIN_RRR ceiling: 15.0 (Law-13) - chains beyond 15R fill-and-stop'
INCLUDE = 65                                     # E3C:1011 'confidence >= 65 required for inclusion'
NO_SHIELD = ('EURUSD',)                          # E3C 8.19 pair table: EUR/USD 'DIRECT_ZONE_TEST, NO_SHIELD'; FA 10: 'PA often directly touches the overlap point ... No Liquidity Shield'
SESSION_WINDOW = {'Swing Scalp': 'London Open', 'HTF Swing': 'NY Mid', 'Reversal': 'NY Open', 'Reinforcement': 'NY Open', 'Transition': 'London/NY Overlap'}    # E3C:563-571


def _steps(X):
    """the liquidity steps of the ladder: the sealed V1's 1H rungs (thin) and 4H bands (thick) (R-30; FA 2.1 'Thin liquidity zones ... If thin zones sit inside a 4H liquidity pool - each thin zone counts as 2')"""
    return [dict(r, thick=False) for r in X['v1']['60']['liquidity']], [dict(b, thick=True) for b in X['v1']['240']['liquidity']]


def _stop(entry, direction, anchor, X, pair):
    """E3C:247-256 SL ladder steps. (b) '1-2 pips INSIDE the CLOSE edge of the NEXT STEP away', the step that may shield a stop being THICK (FA 2.1 'Thin liquidity zones are NEVER allowed as entry or SL
    zones'): the first V1 4H band or the SECOND 1H rung beyond the entry's own (smallest) step; (a) '3 pips OUTSIDE the FAR edge of the CURRENT entry step'. EUR/USD has no shield (NO_SHIELD): (a).
    D17 ceiling 36 pips; golden minimum 4 pips (E3C:279-293). Returns (sl, why) or (None, reason)."""
    pip = D.PIP[pair]
    dn = direction == 'down'
    thin, thick = _steps(X)
    cont = [s for s in thin + thick if s['bot'] - 1e-12 <= entry <= s['top'] + 1e-12]
    cur = min(cont, key=lambda s: s['top'] - s['bot']) if cont else None
    if anchor is not None and anchor.get('sweep') and cur is None:
        cur = anchor
    ref = (cur['top'] if dn else cur['bot']) if cur else entry
    beyond = lambda s: (s['bot'] > ref + 1e-12) if dn else (s['top'] < ref - 1e-12)
    th = sorted([s for s in thin if beyond(s)], key=lambda s: s['bot'] if dn else -s['top'])
    tk = sorted([s for s in thick if beyond(s)], key=lambda s: s['bot'] if dn else -s['top'])
    cands = []
    step_a = cur if cur is not None else anchor
    if step_a is not None:
        cands.append(((step_a['top'] + 3 * pip) if dn else (step_a['bot'] - 3 * pip), "(a) 3 pips outside the far edge of the current step"))
    if pair not in NO_SHIELD:
        # every step that may shield a stop, nearest first: thick 4H bands, and the thin 1H rungs from the second on (FA 2.1); a shield closer than the golden minimum is the step the entry
        # itself stands on - the next one is the 'NEXT STEP away' (E3C:255)
        sh = sorted(th[1:] + tk, key=lambda s: s['bot'] if dn else -s['top'])
        for k, s in enumerate(sh):
            cands.insert(k, ((s['bot'] + pip) if dn else (s['top'] - pip), f"(b) 1 pip inside the close edge of the shield ({'4H band' if s['thick'] else '1H rung beyond the first'})"))
    for sl, why in cands:
        d = abs(sl - entry) / pip
        if GOLD_MIN <= d <= SL_CEIL and ((sl > entry) if dn else (sl < entry)):
            return sl, why
    return None, 'SL_INVALID: no ladder-step stop between 4 and 36 pips'


def _ip_at(z, X):
    """the IP zone at an anchor (overlap), for the confluence / narrative layers"""
    return next((q for q in X['zones'] if q['bot'] <= z['top'] and q['top'] >= z['bot']), None) if z is not None else None


def _confidence(s, X, E2, pair):
    """E3C:392-404 Phase 5.1 (fallback base, no VLM) + Phase 4.1 layer 3 (BoM +5 / MoM -10). Returns (score, parts)."""
    pip = D.PIP[pair]
    a = s['anchor']
    ipz = a if ('zfp_num' in a and 'tf' not in a) else _ip_at(a, X)
    zr = {'Hard Wall': 10, 'Standard Wall': 22.5, 'Soft Wall': 40, 'One-Touch': 60, 'Post-Expiry Ghost': 30}
    base = (100 - zr.get(ipz['type'], 40)) if ipz is not None else 70      # no VLM: the zone's own hold probability (100 - ZFP range midpoint, Appendix B), else the middle of 'typically 50-95' (D-42)
    parts = [('base (fallback zone confidence, no VLM)', max(50, min(95, base)))]
    if ipz is not None:
        parts.append(('IP confluence', min(15, ipz['score'] * 1.5)))
    cls = a.get('kind') or (ipz or {}).get('mech', {}).get('bom')
    if cls == 'BoM':
        parts.append(('BoM', 5))
    elif cls == 'MoM':
        parts.append(('MoM (Phase 4.1 layer 3)', -10))
    side = a.get('type') if a.get('type') in ('Supply', 'Demand') else {'RES': 'Supply', 'SUP': 'Demand'}.get(a.get('cat'), 'Supply' if s['dir'] == 'SHORT' else 'Demand')   # IP: by role; the pivot serves both
    if (side == 'Supply' and s['dir'] == 'SHORT') or (side == 'Demand' and s['dir'] == 'LONG') or a.get('sweep') or a.get('liq'):
        parts.append(('zone-direction alignment', 8))
    story = E2.get('storyline')
    if story:
        parts.append(('storyline', 5 if (story == 'up') == (s['dir'] == 'LONG') else 0))
    parts.append(('RRR', 5 if s['rrr'] >= 3 else 3 if s['rrr'] >= 2 else 0))
    slp = s['sl_pips']
    parts.append(('SL distance', -10 if slp > 80 else -5 if slp > 50 else 0))
    dist = abs(s['entry'] - X['spot']) / pip
    parts.append(('proximity', -8 if dist > 150 else -4 if dist > 80 else 0))
    pw = X['weekly'][-1]
    mom = 'up' if pw['close'] > (pw['high'] + pw['low']) / 2 else 'down'
    parts.append(('prior-week momentum', 3 if (mom == 'up') == (s['dir'] == 'LONG') else -8))
    return max(0, min(100, round(sum(v for _, v in parts), 1))), parts


def _cands(E2, monday, X):
    """Phase 2 candidates (E3C:129 'For each (WorkingDay, zone) pair ... generate a trade candidate'; R3 law: E2 designates the zones): SS steps -> swing scalps in BOTH directions at their two bounds
    (E3C:96 'SS | Swing Scalps (both directions)'); every other E2 move -> one candidate anchored at the zone E2 starts it from; the WL spike is the end of the BS (GS Law 3 'Whiplash: post-spike entry'
    = the RWL after it); R -> no candidate yet (logged)"""
    import e2_chain as E2M
    S = E2M.week_sessions(monday)
    out, log = [], []
    legs = [l for l in E2['legs'] if l['shape'] not in ('SS',)]
    for st in E2['chain']:
        days = sorted({S[k]['i'] for k in range(st['s0'], st['s1'])})
        dn = [DAYS[i] for i in days]
        if st['shape'] == 'SS':
            if st['frm'] is None or st['to'] is None:
                log.append(f"SS {dn}: SOURCE_INVALID - no bound"); continue
            lo, hi = sorted([st['frm'], st['to']], key=lambda z: z['bot'])
            for d, a, t in (('down', hi, lo), ('up', lo, hi)):
                # every (day, zone) pair on the correct side (E3C:129): the E2 bound and each standing 1H / 4H supply (short) / demand (long) zone inside the range within the swing-scalp reach of the
                # range edge it guards (GS Law 2: SS 0-30 pips; GS Law 3: entries at the LTF zones, the bound = the HTF frame)
                lim = 0.30 * X['U']
                inner = [q for q in X['sd'] if q['tf'] in ('240', '60') and q['type'] == ('Supply' if d == 'down' else 'Demand') and lo['top'] <= q['bot'] and q['top'] <= hi['bot']
                         and ((hi['bot'] - q['top'] <= lim) if d == 'down' else (q['bot'] - lo['top'] <= lim))]
                tr = next((x for x in E2['chain'] if x.get('role') == 'retest'), None)
                if tr is not None and E2.get('pivot') is not None and d == E2.get('bdir') and S[tr['s0']]['i'] in days:
                    # 6.4.2: the slow consolidation ends retesting the opposing liquidity FROM the pivot: on the transition day the swing in the breakout direction ends at the pivot (its far side)
                    out.append({'shape': 'SS', 'dir': d, 'from_zone': dict(a), 'to_zone': E2['pivot'], 'from': a['bot'] if d == 'down' else a['top'], 'days': [DAYS[S[tr['s0']]['i']]],
                                'to': E2['pivot']['bot'] if d == 'down' else E2['pivot']['top'], 't0': S[tr['s0']]['t0'] - 86400000, 't1': S[tr['s0']]['t1'], 'role': 'last-swing'})
                for anc in sorted(inner, key=lambda q: -q['top'] if d == 'down' else q['bot']) + [a]:      # GS Law 3: the LTF zone first, the HTF bound after (Phase 6.3 keeps the first)
                    out.append({'shape': 'SS', 'dir': d, 'from_zone': dict(anc, name=anc.get('name', anc.get('label'))), 'to_zone': t, 'from': anc['bot'] if d == 'down' else anc['top'],
                                'to': t['top'] if d == 'down' else t['bot'], 'days': dn, 't0': max(S[st['s0']]['t0'], D.boundary_ms(monday)), 't1': S[st['s1'] - 1]['t1'], 'role': st.get('role')})
        elif st['shape'] in ('WL', 'PWL'):
            continue
        elif st['shape'] == 'R':
            log.append(f"R {dn}: recovery - no designated swing (6.1.3 transitional)"); continue
        else:
            l = next((x for x in legs if x['shape'] == st['shape'] and x['dir'] == st['dir'] and not x.get('used')), None)
            if l is None:
                continue
            l['used'] = True
            c = dict(l, days=dn, role=st.get('role'))
            if st.get('role') == 'retest':                   # 6.4.2 the retest runs from inside the range to the opposing liquidity: its entry is the pivot (else the other bound) (R3 law)
                c['from_zone'] = E2.get('pivot') or E2.get('near')
            if st.get('role') in ('rwl', 'rwl0'):            # the reversal after the spike: entry where the stops rest (an unswept sweep zone against the target, P533 0.45d), TP back to the origin (E2X:215)
                tz = st['frm'] or {}
                sw = [z for z in X['lsz'] if not z['swept'] and tz and z['side'] == ('Demand-side' if st['dir'] == 'up' else 'Supply-side')
                      and ((tz['bot'] - 0.10 * X['U'] <= z['level'] <= tz['top']) if st['dir'] == 'up' else (tz['bot'] <= z['level'] <= tz['top'] + 0.10 * X['U']))]
                if sw:
                    z = max(sw, key=lambda z: z['level']) if st['dir'] == 'up' else min(sw, key=lambda z: z['level'])
                    U = X['U']
                    c['from_zone'] = {'bot': z['level'], 'top': z['level'] + 0.05 * U, 'ext': min(q['level'] for q in sw), 'sweep': True, 'name': 'sweep zone'} if st['dir'] == 'up' else \
                                     {'bot': z['level'] - 0.05 * U, 'top': z['level'], 'ext': max(q['level'] for q in sw), 'sweep': True, 'name': 'sweep zone'}
                c['shape_tp'] = 'WL'
                c['to_zone'] = E2.get('pivot') or st['to']
                c['to'] = (c['to_zone']['bot'] if st['dir'] == 'up' else c['to_zone']['top']) if c['to_zone'] else c['to']
            out.append(c)
    return out, log


def _build(pair, monday, X, E2, tag):
    env = _env(X, pair)
    pip, rungs, blocks, sd = env
    U = X['U']
    for z in sd:
        z['key'] = (z['tf'], round(z['bot'], 6), round(z['top'], 6))
    cands, log = _cands(E2, monday, X)
    setups = []
    for c in cands:
        direction = c['dir']
        a = c['from_zone']
        if a is None:
            log.append(f"{c['days'][0]} {c['shape']} {direction}: SOURCE_INVALID - E2 gives no zone"); continue
        a = dict(a)
        if 'zfp_num' in a and 'tf' not in a:
            a['ip'] = True                                   # IP zones are never entry sources: the LQZ rung at them is (E3C:136)
        cat = CAT.get(c['shape'], 'Swing Scalp')
        # Phase 2 gates
        if 'tf' in a and a.get('mit', 0) >= 3:
            log.append(f"{c['days'][0]} {c['shape']} {direction}: FRESHNESS - {a.get('label', '')} tested {a['mit']}x (E3C:150 'index i > 2 skipped')"); continue
        if a.get('kind') == 'MoM' and cat in ('Reversal', 'HTF Swing') and c['shape'] != 'BS':
            log.append(f"{c['days'][0]} {c['shape']} {direction}: MOM_REVERSAL - {a.get('label', '')} (FA 7 'Do not take reversal entries on MoM zones'; E2X:239 'scalp only at most')"); continue
        ecands = _entries(a, direction, c['shape'], env, pair)
        if c['shape'] in ('BS', 'PBS') and setups and setups[-1]['shape'] == 'RWL' and setups[-1]['dir'] == ('LONG' if direction == 'up' else 'SHORT') is False:
            pass
        if c.get('role') == 'retest':                        # Law 27 (E3C:438-449): the retest starts where the last swing's TP put price
            ls = next((q for q in reversed(setups) if q.get('role') == 'last-swing' and a['bot'] - 3 * pip <= q['tp'] <= a['top'] + 3 * pip), None)
            if ls is not None:
                ecands = [(ls['tp'], {'bot': ls['tp'], 'top': ls['tp']}, 'the last swing\'s TP level (Law 27: TP of N = entry of N+1)')]
        prev = next((q for q in reversed(setups) if q['shape'] == 'RWL' and q['days'][-1] == c['days'][0]), None)
        if c['shape'] in ('BS', 'PBS') and prev is not None:
            lvl, pz = prev['tp'], prev['tp_zone']           # Law 27 (E3C:438-449): TP of the RWL = entry of the BS
            ecands = [(lvl, pz if pz.get('liq') else {'bot': lvl, 'top': lvl}, 'the reverse-whiplash TP level (Law 27: TP of N = entry of N+1)')]
        if not ecands:
            log.append(f"{c['days'][0]} {c['shape']} {direction}: SOURCE_INVALID - no ORDER_BLOCK / LQZ entry at {a.get('name', '')} (E3C:135)"); continue
        s, why_fail = None, 'TP_NULL'
        for entry, step, how in ecands[:3]:                  # E3C:386 '3 attempts on each anchor (3 E, 3 SL, 3 TP)'
            stop, why_sl = _stop(entry, direction, step if 'bot' in step else a, X, pair)
            if stop is None:
                why_fail = why_sl; continue
            tps = [t for t in _target(dict(c, shape=c.get('shape_tp', c['shape'])), entry, direction, E2, X, env, set(), pair) if ((t[0] < entry) if direction == 'down' else (t[0] > entry))]
            if not tps:
                why_fail = 'TP_NULL: no opposing zone on the way (E3C:1016 honest absence)'; continue
            for tries, (tp, tz, why_tp) in enumerate(tps[:3], 1):
                rrr = abs(tp - entry) / abs(entry - stop)
                if RRR_FLOOR <= rrr <= MAX_RRR:
                    s = {'dir': 'SHORT' if direction == 'down' else 'LONG', 'entry': entry, 'sl': stop, 'tp': tp, 'rrr': round(rrr, 2), 'tp_zone': tz, 'attempts': tries,
                         'why': f"entry {how}; SL {why_sl}; TP {why_tp}", 'src': (round(step['bot'], 6), round(step['top'], 6)) if 'bot' in step else None}
                    break
                why_fail = f"RRR {rrr:.2f} outside [{RRR_FLOOR}, {MAX_RRR}]"
            if s is not None:
                break
        if s is None:
            log.append(f"{c['days'][0]} {c['shape']} {direction}: REJECT {why_fail} (entry {entry:.5f})"); continue
        s.update(day=c['days'][0], days=c['days'], shape=c['shape'], category=cat, session=SESSION_WINDOW[cat], sl_pips=round(abs(s['entry'] - s['sl']) / pip, 1),
                 t0=c.get('t0'), t1=c.get('t1'), anchor=a, role=c.get('role'))
        ipz = a if a.get('ip') else _ip_at(a, X)
        if ipz is not None and ipz['zfp_num'] > 30 and not a.get('sweep'):
            log.append(f"{s['day']} {s['shape']} {s['dir']} {s['entry']:.5f}: NARRATIVE - anchor zone {ipz['name']} ZFP {ipz['zfp_num']}% > 30 (E3C:874-876 'suppress > 30 (WEAK)')"); continue
        s['confidence'], s['conf_parts'] = _confidence(s, X, E2, pair)
        if s['confidence'] < INCLUDE:
            log.append(f"{s['day']} {s['shape']} {s['dir']} {s['entry']:.5f}: CONFIDENCE {s['confidence']} < {INCLUDE} (E3C:1011)"); continue
        s['quality'] = 'HIGH' if s['confidence'] >= 80 else 'STANDARD'
        setups.append(s)
        if c['shape'] in ('BS', 'PBS'):
            setups += _reinforce(s, X, E2, env, pair, log)
    # Phase 6.3 (E3C:459-471): duplicates (same category, same day, entries within 5 pips: first kept), conflicts (opposite direction, same day + session, within 15 pips: higher confidence kept),
    # emission cap (pair, anchor bucket, day): one per bucket
    kept = []
    for q in setups:
        dup = next((k for k in kept if k['category'] == q['category'] and k['day'] == q['day'] and abs(k['entry'] - q['entry']) <= 5 * pip and k['dir'] == q['dir']), None)
        con = next((k for k in kept if k['dir'] != q['dir'] and k['day'] == q['day'] and k['session'] == q['session'] and abs(k['entry'] - q['entry']) <= 15 * pip), None)
        if dup is not None:
            log.append(f"{q['day']} {q['shape']} {q['dir']} {q['entry']:.5f}: DUPLICATE of {dup['shape']} {dup['entry']:.5f} (E3C:463)"); continue
        if con is not None:
            if q.get('confidence', 0) > con.get('confidence', 0):
                kept.remove(con); log.append(f"{con['day']} {con['shape']} {con['dir']} {con['entry']:.5f}: CONFLICT - lower confidence than {q['entry']:.5f} (E3C:462)")
            else:
                log.append(f"{q['day']} {q['shape']} {q['dir']} {q['entry']:.5f}: CONFLICT - lower confidence than {con['entry']:.5f} (E3C:462)"); continue
        kept.append(q)
    # Phase 6.2 (E3C:443-457): trade-flow chains - TP of N = entry of N+1 within 3 pips, depth <= 3
    kept.sort(key=lambda q: (DAY_IDX[q['day']], q['entry'] if q['dir'] == 'LONG' else -q['entry']))
    for q in kept:
        q.setdefault('chain', None)
    for i, q in enumerate(kept):
        nxt = next((k for k in kept[i + 1:] if abs(k['entry'] - q['tp']) <= 3 * pip and DAY_IDX[k['day']] >= DAY_IDX[q['day']] and k.get('parent') is None), None)
        if nxt is not None and q.get('depth', 1) < 3:
            nxt['depth'] = q.get('depth', 1) + 1
            nxt['chain'] = q.get('chain') or f"CHAIN-{pair[:2]}{tag}{i + 1}"
            q['chain'] = nxt['chain']
    for i, q in enumerate(kept):
        new_id = f"{pair[:2]}{tag}{i + 1}"
        for k in kept:
            if k.get('parent') == q.get('id'):
                k['parent'] = new_id
        q['id'] = new_id
    if len(kept) > MAX_SETUPS:
        for q in kept[MAX_SETUPS:]:
            log.append(f"{q['day']} {q['shape']} {q['dir']} {q['entry']:.5f}: EMISSION_CAPPED - more than {MAX_SETUPS} setups this week (L-04)")
    return {'setups': kept[:MAX_SETUPS], 'log': log}


def _reinforce(s, X, E2, env, pair, log):
    """Phase 9 (E3C:619-718; GS Law 6): 2-3 reinforcements at the liquidity zones along the TP path of the primary (8R.10 'map ALL liquidity zones between entry and TP'), the first beyond the pivot,
    then 20-30 pips apart (GS Law 6 'Rocket spacing: 20-30 pips'); stop-limit at the rung, OWN SL 1 pip outside the back edge of the next rung (8R.7), the parent's TP; RRR >= 3;
    8R.3 '>= 2 reinforcements inside primary SL -> reject the additional ones'; sizing 50 / 30 / 20 (8R.1)"""
    pip, rungs, blocks, sd = env
    real = [r for r in rungs if 'fib' not in r]
    dn = s['dir'] == 'SHORT'
    piv = E2.get('pivot')
    ref = (piv['bot'] if dn else piv['top']) if piv else s['entry']
    path = sorted([r for r in real if ((r['top'] <= min(ref, s['entry']) + 2 * pip and r['bot'] > s['tp']) if dn else (r['bot'] >= max(ref, s['entry']) - 2 * pip and r['top'] < s['tp']))],
                  key=lambda r: -r['top'] if dn else r['bot'])
    out, last = [], None
    for r in path:
        if len(out) >= 3:
            break
        e2 = (r['bot'] + r['top']) / 2
        if last is not None and abs(e2 - last) < 20 * pip:
            continue
        nxt = sorted([q for q in real if (q['bot'] > r['top'] if dn else q['top'] < r['bot'])], key=lambda q: q['bot'] if dn else -q['top'])
        if not nxt:
            continue
        sl2 = nxt[0]['top'] + pip if dn else nxt[0]['bot'] - pip
        d2 = abs(sl2 - e2) / pip
        rr = abs(s['tp'] - e2) / abs(e2 - sl2) if e2 != sl2 else 0
        if not (GOLD_MIN <= d2 <= SL_CEIL and RRR_FLOOR <= rr <= MAX_RRR):
            log.append(f"reinforcement at {e2:.5f}: REJECT RRR {rr:.2f} / SL {d2:.1f}p"); continue
        if sum(1 for q in out if (min(q['entry'], q['sl']) <= max(s['entry'], s['sl']) and max(q['entry'], q['sl']) >= min(s['entry'], s['sl']))) >= 2:
            log.append(f"reinforcement at {e2:.5f}: REJECT overlapping risk (8R.3)"); continue
        di = min(len(s['days']) - 1, len(out) + 1)
        out.append({'dir': s['dir'], 'entry': e2, 'sl': sl2, 'tp': s['tp'], 'rrr': round(rr, 2), 'day': s['days'][di], 'days': s['days'][di:], 't0': None, 't1': s.get('t1'),
                    'shape': 'Ladder', 'category': 'Reinforcement', 'session': SESSION_WINDOW['Reinforcement'], 'sl_pips': round(d2, 1), 'parent': s.get('id'), 'tp_zone': s['tp_zone'],
                    'anchor': r, 'size': (30, 20, 20)[len(out)], 'confidence': s['confidence'], 'quality': s['quality'],
                    'why': f"reinforcement {len(out) + 1} (stop-limit at the LQZ rung on the TP path; own SL 1 pip outside the back edge of the next rung; parent TP)"})
        last = e2
    return out


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


def pine(pair, monday, R):
    """R-09: position boxes - red = SL side, green = entry -> TP, entry on their shared edge; each box spans the time Engine 2 gives its leg"""
    g = lambda v: ('%.3f' if pair == 'DXY' else '%.5f') % v
    b0, wk1 = D.boundary_ms(monday), D.week_end_ms(monday)
    o = ['    if show_e3']
    if not R['setups']:
        o.append('        na')
    seen_day, starts = set(), {}
    for s in R['setups']:
        day0 = D.week_start_ms(monday) + DAY_IDX[s['day']] * 86400000
        first = s['day'] not in seen_day; seen_day.add(s['day'])
        x0 = max(day0 if first else s['t0'], b0)             # a setup is a resting order from the start of its day; later setups of the same day follow in leg order
        x1 = min(max(s['t1'], x0 + 6 * 3600000), wk1)
        o.append(f"        // {s['id']} {s['day']} {s['shape']} {s['dir']} E {g(s['entry'])} SL {g(s['sl'])} TP {g(s['tp'])} RRR {s['rrr']} | {s['category']} / {s['session']} | {s['why']}")
        o.append(f"        box.new({x0}, {g(max(s['entry'], s['sl']))}, {x1}, {g(min(s['entry'], s['sl']))}, bgcolor=color.new(color.rgb(242,54,69), {86 if s.get('alt') else 70}), border_color=color.rgb(242,54,69), border_width=1, border_style={'line.style_dashed' if s.get('alt') else 'line.style_solid'}, xloc=xloc.bar_time)")
        o.append(f"        box.new({x0}, {g(max(s['entry'], s['tp']))}, {x1}, {g(min(s['entry'], s['tp']))}, bgcolor=color.new(color.rgb(8,153,129), {88 if s.get('alt') else 76}), border_color=color.rgb(8,153,129), border_width=1, border_style={'line.style_dashed' if s.get('alt') else 'line.style_solid'}, xloc=xloc.bar_time)")
        ly = s['entry'] + 0.18 * (s['tp'] - s['entry'])        # inside the green box, next to its own entry edge: setups sharing one TP no longer stack their labels (A13)
        k = starts.get(x0, 0); starts[x0] = k + 1             # setups resting from the same bar: labels staggered along the box so they do not print over each other (A13)
        lx = min(x0 + 3 * 3600000 + k * 9 * 3600000, x1 - 3600000)
        o.append(f"        label.new({lx}, {g(ly)}, \"{s['id']} {'ALT ' if s.get('alt') else ''}{s['shape']} {'S' if s['dir'] == 'SHORT' else 'L'} {s['rrr']:.1f}R\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.{'gray' if s.get('alt') else 'white'}, size=size.small)")
    return o


if __name__ == '__main__':
    import sys, e1_pine as EP, e2_chain as E2M
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
