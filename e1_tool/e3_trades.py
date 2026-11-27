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
ALT_SETUPS = True        # D-109: the alternative chain's breakout family is emitted as CONDITIONAL orders, live only after the Decision Zone trigger (P533 6.6 Step 4: a 1H close beyond the zone)
FWD = {'DXY': 0.02, 'EURUSD': 0.0001, 'GBPUSD': 0.0002}     # E3C 8.19 pair table, column 'Forward Spread'
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
        out = [(anchor['bot'] if direction == 'down' else anchor['top'], anchor, 'sweep zone near edge (TS-1)'), mid]
        if anchor.get('reach') is not None and SWEEP_EXT:    # third attempt (E3C:386): the exact swing extreme the stops rest at (P533 0.45a / 0.45b 'The exact swing low price is where ... stop-loss orders are placed')
            out.append((anchor['top'] if direction == 'down' else anchor['bot'], anchor, 'sweep zone: the exact swing extreme (P533 0.45a/b)'))
        return out
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
    if direction == 'down' and anchor.get('type') == 'Supply' and 'tf' in anchor:
        out.append((anchor['bot'] + 1 * pip, anchor, 'zone edge + 1 pip (TS-1; F1-A, E3C:186)'))       # 'For OB SHORT only, lift the entry 1 pip above the supply zone's bottom edge' (N-20)
    else:
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
        if leg.get('role') in ('rwl', 'rwl0'):
            # the reversal after a breakout is a partial recovery of 30-100 pips (GS Law 2 'RWL | 30-100 pips (partial recovery)'): its TP is the first liquidity rung at least 30 pips
            # along the way, at the rung's midpoint (E3C:306-309 rule 4)
            real = [r for r in rungs if 'fib' not in r]
            far = sorted([r for r in real if 30 * pip <= ((entry - (r['bot'] + r['top']) / 2) if direction == 'down' else ((r['bot'] + r['top']) / 2 - entry)) <= 100 * pip],
                         key=lambda r: -r['top'] if direction == 'down' else r['bot'])
            for r in far[:1]:
                out.append(((r['bot'] + r['top']) / 2, dict(r, rung=True), 'first LQZ rung 30+ pips along the reversal: midpoint (GS Law 2; rule 4)'))
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
    def near(z):
        # the near edge of the JOINED zone (L-39 'a pressure zone = candle structure + level cluster joined'): the pressure zone under 30% and the standing 1H / 4H candle zone of the
        # opposing side that overlap the target are one zone - price meets its first edge. Not on EUR/USD: 'DIRECT_ZONE_TEST' (E3C 8.19; FA 10 'PA often directly touches the overlap
        # point') - his golden EURUSD #3 TP lies in the overlap of the 1H demand and the pressure zone, his DXY #2 / GBPUSD #2 TPs on the candle zone's near edge (D-91; numbers in memory/03)
        e = z['top'] if direction == 'down' else z['bot']
        if pair in NO_SHIELD or not JOIN_TP:
            return e
        parts = [q for q in X['zones'] if q['zfp_num'] < 30 and _overlap(q, z)] + [q for q in sd if q['tf'] in ('240', '60') and q['type'] == opp and q.get('mit', 0) < 3 and _overlap(q, z)]
        for q in parts:
            e = max(e, q['top']) if direction == 'down' else min(e, q['bot'])
        return e if ahead(e) else (z['top'] if direction == 'down' else z['bot'])
    if tz is not None and tz.get('zfp_num', 40) < 30 and not (tz['bot'] <= X['spot'] <= tz['top']):
        out.append((near(tz) + pip if direction == 'down' else near(tz) - pip, tz, 'E2 bounding zone near edge + 1 pip (strong zone, E3C:320-327)'))
    if tz is not None and 'tf' in tz and 'zfp_num' not in tz and not (tz['bot'] <= X['spot'] <= tz['top']):
        # the E2 zone is a supply / demand candle zone (no ZFP of its own, G2 C-01): E3C:333 'E2-shapeDay projected opposing zone ... FIRST'; rule 5 'no LQZ overlap -> TP at zone NEAR EDGE',
        # BoM = STRONG -> 'closest zone edge ... add a 1-2 pip spread' (E3C:320-327)
        sp = pip if (tz.get('kind') == 'BoM' or near(tz) != (tz['top'] if direction == 'down' else tz['bot'])) else 0.0
        out.append((near(tz) + sp if direction == 'down' else near(tz) - sp, tz, f"E2 bounding supply / demand zone near edge{' + 1 pip (strong)' if sp else ''} (E3C:333, rule 5)"))
    if tz is not None and tz.get('liq'):                     # a thick liquidity band (V1 4H) = strong pressure: 'exit on the closest zone edge' (E3C:320-327)
        out.append((tz['top'] if direction == 'down' else tz['bot'], tz, 'liquidity band near edge (strong, E3C:320-327)'))
    zs = [z for z in sd if z['tf'] in ('240', '60') and z['type'] == opp and id(z) not in used and z.get('key') not in used
          and ahead(z['top'] if direction == 'down' else z['bot'])
          and (((z['top'] >= end) if direction == 'down' else (z['bot'] <= end)) or (tz is not None and _overlap(z, tz)))]       # on the way to the E2 leg end, or lying against the E2 zone
    zs.sort(key=lambda z: -z['top'] if direction == 'down' else z['bot'])
    # Refined Law 14 (E3C:346-347): 'Price cannot teleport past UNMITIGATED zones ... The "no teleport" constraint applies ONLY to zones with reactionCount = 0': an unmitigated opposing
    # 1H / 4H zone standing wholly before the E2-projected zone is where this swing ends - nothing beyond it is a target (D-66)
    # ... and only a zone that is a valid stop for price: BoM, or MoM standing under a pressure zone below 30% (P452:2082 'No IP + standalone MoM = it gets pierced (not valid TP)';
    # the same reading as Engine 2's breakout target, D-49 / D-50)
    holds = lambda z: True                                   # every unmitigated opposing zone ends the walk, as the Law says; a virgin MoM of low confluence is exited at its FAR edge (E3C:329) (D-97)
    virgin = [z for z in zs if z.get('mit', 1) == 0 and holds(z) and (tz is None or not _overlap(z, tz)) and ((z['top'] > end) if direction == 'down' else (z['bot'] < end))]
    if virgin and LAW14:
        z0 = virgin[0]
        out = []
        zs = [z for z in zs if ((z['top'] >= z0['top']) if direction == 'down' else (z['bot'] <= z0['bot']))]
        tz = None
    for z in zs:
        ov = [r for r in rungs if _overlap(r, z)]
        for r in sorted(ov, key=lambda r: -r['top'] if direction == 'down' else r['bot']):
            out.append(((r['bot'] + r['top']) / 2, z, 'LQZ inside the opposing zone: midpoint'))
        if z.get('kind') == 'MoM' and z.get('mit', 1) == 0 and not any(q['zfp_num'] < 30 and _overlap(q, z) for q in X['zones']):
            out.append((z['bot'] if direction == 'down' else z['top'], z, 'weak zone (virgin MoM, low confluence): far edge (E3C:329)'))
        else:
            out.append((z['top'] if direction == 'down' else z['bot'], z, 'opposing zone near edge'))
    if tz is not None:
        if tz.get('zfp_num', 40) < 30 and not (tz['bot'] <= X['spot'] <= tz['top']):
            out.append((tz['top'] + pip if direction == 'down' else tz['bot'] - pip, tz, 'bounding zone near edge + 1 pip (strong zone)'))
        elif tz.get('sweep') and SWEEP_TP:
            # a sweep zone bounding the range: E3C:313-315 rule 5 'no LQZ overlap -> TP at zone NEAR EDGE (quick exit)', rule 6 'NEVER target FAR edge of distant zone';
            # P533 7.1 Rule 3 SS 'nearest MAJOR opposing zone edge OR nearest LSZ edge' (D-86)
            out.append((tz['top'] if direction == 'down' else tz['bot'], tz, 'bounding sweep zone near edge (rule 5; P533 7.1 Rule 3 LSZ edge)'))
        else:                                                # weak zone / pivot: far edge, the LQZ band lying on it
            fe = tz['bot'] if direction == 'down' else tz['top']
            rr = sorted([r for r in rungs if r['bot'] - 2 * pip <= fe <= r['top'] + 2 * pip], key=lambda r: abs((r['bot'] + r['top']) / 2 - fe))
            if rr:
                out.append(((rr[0]['bot'] + rr[0]['top']) / 2, dict(rr[0], rung=True), 'LQZ on the far edge of the pivot: midpoint'))
            out.append((fe, tz, 'weak zone far edge'))
    return out


LAW7 = {'DXY': 5, 'EURUSD': 2, 'GBPUSD': 3}       # E3C:299-304 per-pair SL buffers (pips; DXY in index points of 0.01)
LAW14 = True
TP_BUF = 1.5                                     # pips in front of a SCALP's take-profit level (Fibonacci Spiderwebs item 4, SS / Recovery scalps: '1.5-2 pip buffer in front of the TP ... MANDATORY')
MAX_RRR = 15.0                                   # E3C:365 'MAX_CHAIN_RRR ceiling: 15.0 (Law-13) - chains beyond 15R fill-and-stop'
INCLUDE = 65                                     # E3C:1011 'confidence >= 65 required for inclusion'
NO_SHIELD = ('EURUSD',)                          # E3C 8.19 pair table: EUR/USD 'DIRECT_ZONE_TEST, NO_SHIELD'; FA 10: 'PA often directly touches the overlap point ... No Liquidity Shield'
SESSION_WINDOW = {'Swing Scalp': 'London Open', 'HTF Swing': 'NY Mid', 'Reversal': 'NY Open', 'Reinforcement': 'NY Open', 'Transition': 'London/NY Overlap'}    # E3C:563-571


def _steps(X):
    """the liquidity steps of the ladder: the sealed V1's 1H rungs (thin) and 4H bands (thick) (R-30; FA 2.1 'Thin liquidity zones ... If thin zones sit inside a 4H liquidity pool - each thin zone counts as 2')"""
    return [dict(r, thick=False) for r in X['v1']['60']['liquidity']], [dict(b, thick=True) for b in X['v1']['240']['liquidity']]


ZR6B = True
SWEEP_EXT = True
GOLD_FALLBACK = True       # D-102: golden stop fallback when no ladder step gives a stop (E3C:262, :289-294)
BLEND_GATE = True          # D-100: the emission floor is met by the blended RRR of a 3-entry staggered position (E3C:357)
JOIN_TP = True
SWEEP_TP = True
DEPLETED_BOUND = True


def _mirror_conf(c, a, direction, E2):
    """mirrorConfidenceScore (E3C:274-282): base 0.5; +0.2 if shapeConf >= 0.65; +0.15 VIRGIN or ACTIVE_1; -0.2 DEPLETED; +0.15 fuel INTACT; -0.2 ABSORBED; +0.1 shapeDay.direction === direction.
    Pressure state: strong reactions of a pressure zone / taps of a candle zone (E3C:152-165). Fuel (ZR-1 operative defense; handover DESIGN_BLUEPRINT 16.7 'shielding liquidity has been consumed'):
    ABSORBED when the anchor has been visited three times or more (E3C 8.25 '3+ ... Zone depleted'), else INTACT"""
    dday = next((d for d in E2['days'] if d['day'] == c['days'][0]), None)
    sc = 0.5 + (0.2 if (dday is not None and dday['conf'] >= 0.65) else 0.0)
    m = a.get('mech') or {}
    rx = m.get('reactions', a.get('mit', 0)) if ('mech' in a or 'mit' in a) else 0
    visits = m.get('visits', a.get('mit', 0)) if ('mech' in a or 'mit' in a) else 0
    sc += 0.15 if rx <= 1 else (-0.2 if rx >= 3 else 0.0)
    sc += -0.2 if visits >= 3 else 0.15
    if dday is not None and dday['dir'] in ('up', 'down') and dday['dir'] == direction:
        sc += 0.1
    return round(sc, 2)


def _stop(entry, direction, anchor, X, pair, dmin=None, zone=None, every=False, conf=None):
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
    # P533 7.1 Rule 2.5 'LIQUIDITY SWEEP ZONE SL PLACEMENT ... If the LSZ has been extended per LSZ Bottom Edge Extension (sweep scan 0.05-0.10 ...), use the extended range for SL placement';
    # E3C:1027 'LSZ Zones (with bottom edge extension) | Phase 4 | SL ladder-steps model': a sweep zone carrying its extension ('reach', Step 0.45a) is ONE step up to the end of the reach -
    # the stop stands 3 pips outside it (Rule 2.5 'LSZ boundary + 3 pip buffer'), and a shield inside the reach is not a 'NEXT step away'. The same holds for a breakout entry
    # resting on an opposing SWEEP zone (e2_chain.liquidity_beyond, 'lsz') (D-84, D-87). The 'reach' itself = P533:1286 'Institutions often sweep 0.05-0.10 beyond the visible
    # extreme before reversing. Record as "LSZ Extended: ... sweep scan 0.05-0.10 DXY beyond swing [high/low]"' (G2 round 2 N-01 reads the same paragraph's first sentence, the
    # zone's inward widening, which Engine 1 draws; this is its outward breach)
    zr = anchor if (anchor is not None and anchor.get('reach') is not None) else zone
    ext = zr.get('reach') if (zr is not None and (zr.get('sweep') or zr.get('lsz') or zr.get('edge_sweep')) and SWEEP_EXT) else None
    if ext is not None:
        cands.append(((ext + 3 * pip) if dn else (ext - 3 * pip), "(a) 3 pips outside the extended sweep range (P533 7.1 Rule 2.5; E3C:1027)"))
        th = [s_ for s_ in th if ((s_['bot'] > ext) if dn else (s_['top'] < ext))]
        tk = [s_ for s_ in tk if ((s_['bot'] > ext) if dn else (s_['top'] < ext))]
        step_a = None
    if step_a is not None:
        cands.append(((step_a['top'] + 3 * pip) if dn else (step_a['bot'] - 3 * pip), "(a) 3 pips outside the far edge of the current step"))
    # E3C:249 operator verbatim '3 pips outside the back edge of the ENTRY ZONE'; E3C:254 '(entry zone's back edge + 3p)': when the liquidity step holding the entry gives no valid stop,
    # the entry structure, then the anchor zone itself, is the current step (D-65)
    for z_, nm in ((anchor, 'entry structure'), (zone, 'entry zone')):
        if ext is not None:
            break
        if z_ is not None and z_ is not step_a and z_.get('top', 0) > z_.get('bot', 0) and not z_.get('ip'):
            cands.append(((z_['top'] + 3 * pip) if dn else (z_['bot'] - 3 * pip), f"(a) 3 pips outside the back edge of the {nm}"))
    if pair not in NO_SHIELD:
        # every step that may shield a stop, nearest first: thick 4H bands, and the thin 1H rungs from the second on (FA 2.1); a shield closer than the golden minimum is the step the entry
        # itself stands on - the next one is the 'NEXT STEP away' (E3C:255)
        sh = sorted(th[1:] + tk, key=lambda s: s['bot'] if dn else -s['top'])
        for k, s in enumerate(sh):
            cands.insert(k, ((s['bot'] + pip) if dn else (s['top'] - pip), f"(b) 1 pip inside the close edge of the shield ({'4H band' if s['thick'] else '1H rung beyond the first'})"))
    ok = []
    for sl, why in cands:
        d = abs(sl - entry) / pip
        if (dmin or GOLD_MIN) <= d <= SL_CEIL and ((sl > entry) if dn else (sl < entry)) and not any(abs(sl - q[0]) < 0.5 * pip for q in ok):
            ok.append((sl, why))
    if every:
        return ok
    if ok and conf is not None and conf >= 0.6 and ZR6B and pair not in NO_SHIELD:
        # ZR-6B Rule S3 (E3C:284-286): 'confidence >= 0.6 -> RR-tight (3p back edge); confidence < 0.6 -> safety (next-rung)'. RR-tight = the tighter of the first shield stop (b) and
        # rule (a) on the ENTRY ZONE (E3C:249 '3 pips outside the back edge of the entry zone'; E3C:259 'S/D PRESSURE_STRUCTURE (the S/D itself acting as the backstop)') - not on the thin
        # liquidity rung the entry happens to stand in; EUR/USD (NO_SHIELD, direct zone test) keeps rule (a) on its entry step (D-73)
        tight = [q for q in ok if q[1].startswith('(b)')][:1] + [q for q in ok if q[1].startswith('(a)') and (cur is None or 'current step' not in q[1])]
        if tight:
            sl, why = min(tight, key=lambda q: abs(q[0] - entry))
            return sl, why + f' [ZR-6B RR-tight, mirror confidence {conf:.2f}]'
    if ok and conf is not None and ZR6B:
        return ok[0][0], ok[0][1] + f' [ZR-6B safety, mirror confidence {conf:.2f}]'
    if ok:
        return ok[0]
    # E3C:262 'null -> golden fallback (computeGoldenSL_V452)'; E3C:289-294 'computeSL_LMV 4-9.5p reaction-extreme ... D17 36p ceiling'; E3C:379 'sl = next-rung's reactionExtreme + Law-7 buffer':
    # no ladder step gives a stop -> the reaction extreme (far edge) of the next liquidity rung beyond the entry, plus the pair's Law-7 buffer (E3C:299-304) (G2 A-24, D-102)
    if GOLD_FALLBACK and ext is None:
        nxt = sorted([s_ for s_ in thin + thick if ((s_['top'] > entry) if dn else (s_['bot'] < entry))], key=lambda s_: s_['top'] if dn else -s_['bot'])
        for s_ in nxt:
            sl = (s_['top'] + LAW7[pair] * pip) if dn else (s_['bot'] - LAW7[pair] * pip)
            if (dmin or GOLD_MIN) <= abs(sl - entry) / pip <= SL_CEIL:
                return sl, f"golden fallback: the next liquidity rung's reaction extreme + the Law-7 buffer {LAW7[pair]} (E3C:289-294, :379)"
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
    typed = a.get('type') in ('Supply', 'Demand') or a.get('cat') in ('RES', 'SUP')
    if typed and ((side == 'Supply' and s['dir'] == 'SHORT') or (side == 'Demand' and s['dir'] == 'LONG')):
        parts.append(('zone-direction alignment', 8))         # E3C:396 '+8 (SUPPLY->SHORT or DEMAND->LONG)': a supply / demand or resistance / support zone only (G2 round 2 N-33)
    # Phase 4.1 confluence stack, the layers not already above (E3C:237-245; G2 A-20): 1 'Tier 1/2 POI confluence +2 / +1 / 0'; 2 'Three-Tier Option Classification bonus +3 (Critical) /
    # +2 (Significant) / 0'; 5 'Day-Shape Alignment +5 (aligned) / 0 (neutral) / -5 (misaligned)'; 6 'Session Mechanics +3 (London) / +2 (NY) / 0 (Asian)'. Layer 4 (stack compliance) is
    # not scored: R-09 keeps the 1H as the authoritative timeframe for every setup
    if ipz is not None:
        parts.append(('POI tier (layer 1)', 2 if ipz.get('tier') == 'Tier 1' else 1 if ipz.get('tier') == 'Tier 2' else 0))
    opt = [l for l in X.get('L', []) if l.get('cut') and l.get('tier') in (1, 2) and a.get('bot', 9e9) - l.get('band', 0.0) <= l['p'] <= a.get('top', -9e9) + l.get('band', 0.0)]
    if opt:
        parts.append(('option classification (layer 2)', 3 if any(l['tier'] == 1 for l in opt) else 2))
    dd = next((d for d in E2.get('days', []) if d['day'] == s.get('day')), None)
    if dd is not None:
        want = 'up' if s['dir'] == 'LONG' else 'down'
        parts.append(('day-shape alignment (layer 5)', 5 if (dd['dir'] == want or (dd['dir'] == 'range' and s.get('shape') in ('SS', 'R'))) else -5 if dd['dir'] in ('up', 'down') and s.get('shape') in ('BS', 'PBS', 'Ladder') else 0))
    parts.append(('session mechanics (layer 6)', 3 if 'London' in s.get('session', '') else 2 if 'NY' in s.get('session', '') else 0))
    story = E2.get('storyline')
    if story:
        parts.append(('storyline', 5 if (story == 'up') == (s['dir'] == 'LONG') else -5))      # E3C:245 layer 7 '+5 (aligned) / -5 (counter-trend, requires exceptional confluence)' (A-20)
    parts.append(('RRR', 5 if s['rrr'] >= 3 else 3 if s['rrr'] >= 2 else 0))
    slp = s['sl_pips']
    parts.append(('SL distance', -10 if slp > 80 else -5 if slp > 50 else 0))
    smax = {'EURUSD': 100, 'GBPUSD': 120, 'DXY': 30}[pair]  # E3C:407-410 three-band SL-distance confidence (DXY in index points of 0.01)
    parts.append(('SL band', -10 if slp > smax else 10 if slp < 30 else 5 if slp < 60 else 0))
    if s.get('cascade'):
        parts.append(('DXY cascade (E3C:412)', 10))          # '+10 if setup is cascade-source (DXY -> EU inverse or EU -> GU kept)': the mirror of a source setup of the same chain step (Phase 10; N-07)
    if pair == 'GBPUSD' and s['dir'] == 'LONG':
        parts.append(('GU short-squeeze (E3C:414)', 5))
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
                # a zone belongs to the range when its ENTRY edge lies between the bounds (a demand zone whose top is above the floor, a supply zone whose bottom is below the ceiling):
                # one that straddles a bound's edge is still met before the bound (TS-1 'edge closest to approaching price')
                inner = [q for q in X['sd'] if q['tf'] in ('240', '60') and q['type'] == ('Supply' if d == 'down' else 'Demand')
                         and ((lo['top'] <= q['bot'] < hi['bot']) if d == 'down' else (lo['top'] < q['top'] <= hi['bot']))
                         and ((hi['bot'] - q['bot'] <= lim) if d == 'down' else (q['top'] - lo['top'] <= lim))]
                tr = next((x for x in E2['chain'] if x.get('role') == 'retest'), None)
                if tr is not None and E2.get('pivot') is not None and d == E2.get('bdir') and S[tr['s0']]['i'] in days:
                    # 6.4.2: the slow consolidation ends retesting the opposing liquidity FROM the pivot: on the transition day the swing in the breakout direction ends at the pivot (its far side)
                    out.append({'shape': 'SS', 'dir': d, 'from_zone': dict(a), 'to_zone': E2['pivot'], 'from': a['bot'] if d == 'down' else a['top'], 'days': [DAYS[S[tr['s0']]['i']]],
                                'to': E2['pivot']['bot'] if d == 'down' else E2['pivot']['top'], 't0': S[tr['s0']]['t0'] - 86400000, 't1': S[tr['s0']]['t1'], 'role': 'last-swing'})
                bound = [a]
                if DEPLETED_BOUND and (E2M.info(a) or {}).get('counter') == 'Depleted':
                    # P533:1159 '3+ reactions (Depleted): Zone is likely to fail on next test. Use for TP targeting only - NOT for entries ... price will likely pierce through it';
                    # E3C:1052 ZONE_DEPLETED 'reactionCount >= 3 (TP-only)'; 6.4.2 'pierce through zone until reaching BoM Liquidity': the swing from this side starts at the liquidity
                    # beyond the depleted bound, and no structure standing on the depleted zone is an entry (D-85)
                    lb = E2M.liquidity_beyond(X, a, d == 'down', lim=None)
                    inner = [q for q in inner if not _overlap(q, a)]
                    bound = [lb] if lb is not None else []
                    log.append(f"SS {d}: ZONE_DEPLETED - {a.get('name', '')} has 3+ reactions (TP only, P533:1159) -> " + (f"entry at {lb['name']} beyond it (6.4.2)" if lb is not None else 'no liquidity beyond it: no entry on this side'))
                for anc in sorted(inner, key=lambda q: -q['top'] if d == 'down' else q['bot']) + bound:      # GS Law 3: the LTF zone first, the HTF bound after (Phase 6.3 keeps the first)
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
            if st['shape'] in ('BS', 'PBS') and st.get('role') == 'bs' and E2.get('near') is not None and any(x['shape'] == 'SS' for x in E2['chain']):
                # E3C:107 'SS->BS Transition | Transition Entry'; E3C:457 'SS -> BS: Range boundary break becomes BS entry'; E3C:1133 late consolidation -> 'Swing Scalps + BS Transition Entry'
                nb = E2['near']
                out.append(dict(c, role='transition', from_zone=dict(nb), **{'from': nb['top'] if st['dir'] == 'up' else nb['bot']}))
    return out, log


MIRROR_OF = None          # set by build(): the source pair's setup keys (shape, role, day, direction)


def _build(pair, monday, X, E2, tag):
    env = _env(X, pair)
    pip, rungs, blocks, sd = env
    U = X['U']
    for z in sd:
        z['key'] = (z['tf'], round(z['bot'], 6), round(z['top'], 6))
    cands, log = _cands(E2, monday, X)
    import e2_chain as E2M_
    S_ = E2M_.week_sessions(monday)
    setups = []
    floor_rrr = 2.5 if E2['chain'] and all(x['shape'] == 'SS' for x in E2['chain']) else RRR_FLOOR      # E3C:1106-1115 'Consolidation week (relaxed) | 2.5' (a week whose chain is SS throughout)
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
        if a.get('ip') and a.get('score', 99) < 7:
            # E3C:1022 'IP Zone Map | Phase 2 | Zone selection (confluence >= 7) generates trade candidates' (G2 round 2 N-25)
            log.append(f"{c['days'][0]} {c['shape']} {direction}: SOURCE_INVALID - {a.get('name', '')} confluence {a.get('score')} < 7 (E3C:1022)"); continue
        if a.get('ip') and (a.get('mech') or {}).get('reactions', 0) == 3:
            # E3C:1052 ZONE_DEPLETED 'reactionCount >= 3 (TP-only)'; lifecycle E3C:158-161 (3 battles = DEPLETED, the fourth strong battle = FORTRESS): a pressure-zone anchor is gated like a
            # candle zone (G2 round 2 A-16)
            log.append(f"{c['days'][0]} {c['shape']} {direction}: ZONE_DEPLETED - {a.get('name', '')} has 3 reactions (TP only, E3C:1052)"); continue
        if a.get('kind') == 'MoM' and cat in ('Reversal', 'HTF Swing') and (c['shape'] != 'BS' or a.get('tf') == '240'):     # E3C:1032 '4H MoM One-and-Done | Scalp-only at 4H MoM' holds for breakouts too (N-27)
            log.append(f"{c['days'][0]} {c['shape']} {direction}: MOM_REVERSAL - {a.get('label', '')} (FA 7 'Do not take reversal entries on MoM zones'; E2X:239 'scalp only at most')"); continue
        ecands = _entries(a, direction, c['shape'], env, pair)
        if c['shape'] in ('BS', 'PBS') and setups and setups[-1]['shape'] == 'RWL' and setups[-1]['dir'] == ('LONG' if direction == 'up' else 'SHORT') is False:
            pass
        if c.get('role') == 'retest':                        # Law 27 (E3C:438-449): the retest starts where the last swing's TP put price
            ls = next((q for q in reversed(setups) if q.get('role') == 'last-swing' and a['bot'] - 3 * pip <= q.get('tp_level', q['tp']) <= a['top'] + 3 * pip), None)
            if ls is not None:
                ecands = [(ls.get('tp_level', ls['tp']), {'bot': ls.get('tp_level', ls['tp']), 'top': ls.get('tp_level', ls['tp'])}, 'the last swing\'s TP level (Law 27: TP of N = entry of N+1)')]
        prev = next((q for q in reversed(setups) if q['shape'] == 'RWL' and q['days'][-1] == c['days'][0]), None)
        if c['shape'] in ('BS', 'PBS') and prev is not None and c.get('role') != 'transition':
            lvl, pz = prev.get('tp_level', prev['tp']), prev['tp_zone']           # Law 27 (E3C:438-449): TP of the RWL = entry of the BS
            ecands = [(lvl, pz if pz.get('liq') else {'bot': lvl, 'top': lvl}, 'the reverse-whiplash TP level (Law 27: TP of N = entry of N+1)')]
        pbs = next((q for q in reversed(setups) if q['shape'] in ('BS', 'PBS') and q.get('parent_ref') is None), None)
        if c.get('role') in ('rwl', 'rwl0') and not a.get('sweep') and pbs is not None and a['bot'] - 3 * pip <= pbs.get('tp_level', pbs['tp']) <= a['top'] + 3 * pip:
            # Law 27 (E3C:443-449 'BS -> RWL: TP of BS becomes RWL entry zone'): the reversal rests at the breakout's TP from the moment the breakout starts
            ecands = [(pbs.get('tp_level', pbs['tp']), a, "the breakout's TP level (Law 27: TP of N = entry of N+1)")]
            c = dict(c, rest_from=pbs['day'])
        if c.get('role') == 'bs' and E2.get('far_liq') is not None and c.get('from_zone') is not None and c['from_zone'].get('liq') and c.get('role') != 'transition':
            # the breakout's entry stands at the opposing liquidity beyond the range (6.4.2) - during the consolidation that zone is the day's DEEP zone on that side (E3C:115 WorkingDayMap
            # 'deepDemandZoneId'; F1-C 'the deep-demand / deep-supply rule', E3C:190-193): the same order rests there from the first day of the consolidation (D-76)
            ss0 = next((x for x in E2['chain'] if x['shape'] == 'SS'), None)
            if ss0 is not None:
                c = dict(c, rest_from=DAYS[S_[ss0['s0']]['i']])
        if c.get('role') == 'transition':                    # the break of the range boundary itself: a stop order at the failing bound's far edge (GS Law 3 'Breakout: at zone edge (break confirmation)')
            lvl = a['top'] if direction == 'up' else a['bot']
            ecands = [(lvl, {'bot': a['bot'], 'top': a['top']}, 'range boundary break (E3C:457): stop order at the far edge of the failing bound')]
            cat = 'Transition'
        if not ecands and a.get('ip'):
            # a pressure zone with no order block / liquidity rung on it: the liquidity resting directly in front of it is its entry source (E3C:258 'LQZ SHIELD_FUEL (the LQZ acting as shield
            # in front of the S/D)'; E3C:80 'the entry at the anchor's internal-LQZ near/deep edge'): an unswept sweep zone of the trade's side within the canon cluster distance 0.15 of the
            # zone's near edge (P533 zone assembly 'cluster within 0.10-0.15'), TS-1 nearest to approaching price first (D-69)
            side = 'Supply-side' if direction == 'down' else 'Demand-side'
            fr = []
            for l in X['lsz']:
                if l['swept'] or l['side'] != side:
                    continue
                q = {'bot': l['level'] - 0.05 * U, 'top': l['level'], 'sweep': True, 'name': 'Liquidity Sweep Zone'} if direction == 'down' else \
                    {'bot': l['level'], 'top': l['level'] + 0.05 * U, 'sweep': True, 'name': 'Liquidity Sweep Zone'}
                gap = (a['bot'] - q['top']) if direction == 'down' else (q['bot'] - a['top'])
                if -1e-12 <= gap <= 0.15 * U:
                    fr.append(q)
            fr.sort(key=lambda q: q['bot'] if direction == 'down' else -q['top'])
            for q in fr[:1]:
                ecands = [(q['bot'] if direction == 'down' else q['top'], q, 'sweep zone in front of the pressure zone, near edge (TS-1)')]
        if not ecands:
            log.append(f"{c['days'][0]} {c['shape']} {direction}: SOURCE_INVALID - no ORDER_BLOCK / LQZ entry at {a.get('name', '')} (E3C:135)"); continue
        s, why_fail = None, 'TP_NULL'
        for entry, step, how in ecands[:3]:                  # E3C:386 '3 attempts on each anchor (3 E, 3 SL, 3 TP)'
            stop, why_sl = _stop(entry, direction, step if 'bot' in step else a, X, pair, dmin=12.0 if c.get('role') == 'transition' else None, zone=a,   # GS Law 3 table 'Breakout | SL 12-20 pips'
                                 conf=_mirror_conf(c, a, direction, E2))
            if stop is None:
                why_fail = why_sl; continue
            tps = [t for t in _target(dict(c, shape=c.get('shape_tp', c['shape'])), entry, direction, E2, X, env, set(), pair) if ((t[0] < entry) if direction == 'down' else (t[0] > entry))]
            if not tps:
                why_fail = 'TP_NULL: no opposing zone on the way (E3C:1016 honest absence)'; continue
            for tries, (tp, tz, why_tp) in enumerate(tps[:3], 1):
                rrr = abs(tp - entry) / abs(entry - stop)
                if c['shape'] == 'RWL' and floor_rrr - 0.1 <= rrr < floor_rrr:
                    # E3C:196-197 'RWL_HAIR_MISS_RRR_DELTA = 0.1 - setups with RRR in [floor - 0.1, floor) get one repair attempt': the entry pulled 0.2 pips inside (RWL_BOUNCE_INSET_PIPS)
                    e2 = entry + 0.2 * pip if direction == 'down' else entry - 0.2 * pip
                    r2 = abs(tp - e2) / abs(e2 - stop)
                    if r2 >= floor_rrr:
                        entry, rrr, how = e2, r2, how + ' (hair-miss repair: 0.2 pip inside, E3C:196-197)'
                if rrr > MAX_RRR:
                    # E3C:365 'MAX_CHAIN_RRR ceiling: 15.0 (Law-13) - chains beyond 15R fill-and-stop': a stop that tight is the dumb anchor (E3C:369-383 'refineSetup on SAME anchors
                    # (entry FIXED - re-anchor SL/TP only): sl = next-rung's ...'): the next ladder stop outward that brings the RRR under the ceiling (D-75)
                    wider = sorted([q for q in _stop(entry, direction, step if 'bot' in step else a, X, pair, zone=a, every=True) if abs(q[0] - entry) > abs(stop - entry) + 1e-12],
                                   key=lambda q: abs(q[0] - entry))
                    for sl2, why2 in wider:
                        r2 = abs(tp - entry) / abs(entry - sl2)
                        if floor_rrr <= r2 <= MAX_RRR:
                            stop, why_sl, rrr = sl2, why2 + ' (re-anchored outward: RRR over the 15R ceiling, E3C:365)', r2
                            break
                # Fibonacci Spiderwebs (operator): 'Make sure there is a 1.5-2 pip buffer in front of the TP or you will miss it. MANDATORY ... If you skip this you will miss 60% of TPs';
                # E3C:324 'add a 1-2 pip spread so you dont miss the exit'. The order's TP stands TP_BUF pips in front of the target level (a level that already carries the 1-pip
                # spread gets the rest); the level itself stays the Law-27 link to the next trade (D-82). E3C:362 'Emission floor: RRR >= 3.0 ... the gate': the floor is tested on the
                # RRR of the order AS EMITTED, i.e. with the buffered TP (G2 round 2 N-03)
                # the PDF states the buffer for 'SS/Rcvry SCALP moves' (item 4); a swing's strong-zone TP carries its own 1-2 pip spread (E3C:324) and nothing more (G2 round 2 N-21, D-98)
                extra = max(((TP_BUF if c['shape'] in ('SS', 'R') else 0.0) - (1.0 if '+ 1 pip' in why_tp else 0.0)) * pip, 0.0)
                tp_o = tp + extra if direction == 'down' else tp - extra
                rrr_o = abs(tp_o - entry) / abs(entry - stop)
                # E3C:355-357 'Primary RRR ... Blended RRR (3-entry staggered): (rrr1 x 0.33) + (rrr2 x 0.33) + (rrr3 x 0.34)'; E3C:313 'Blended RRR is across the 3 staggered entries';
                # E3C:939 'RRR: [primary/blended]'; E3C:366 'Never distort zone structure to hit a target RR'; E3C:373 'entry FIXED - re-anchor SL/TP only': an entry resolved on a zone
                # (Mechanism A, E3C:1060-1066: front = edge nearest spot + forward spread, middle = the resolved entry, back = edge farthest from spot + forward spread, one SL, one TP)
                # is a 3-entry staggered position, and the RRR of that position is the blended one - it meets the floor before the entry is moved deeper into the zone (D-100)
                bl = None
                if BLEND_GATE and c.get('role') != 'transition' and 'bot' in step and step['top'] > step['bot']:       # also a Law-27 level standing on the edge of a real zone (the reversal at the breakout's target zone) (D-106)
                    edge_ = step['bot'] if direction == 'down' else step['top']
                    fr_ = edge_ - FWD[pair] if direction == 'down' else edge_ + FWD[pair]
                    bk_ = (step['top'] - FWD[pair]) if direction == 'down' else (step['bot'] + FWD[pair])
                    if ((bk_ < stop) if direction == 'down' else (bk_ > stop)) and ((fr_ - 1.5 * pip <= entry <= bk_) if direction == 'down' else (bk_ <= entry <= fr_ + 1.5 * pip)):
                        rr_ = [abs(tp_o - e) / abs(e - stop) for e in (fr_, entry, bk_)]
                        bl = 0.33 * rr_[0] + 0.33 * rr_[1] + 0.34 * rr_[2]
                by_blend = rrr_o < floor_rrr and bl is not None and bl >= floor_rrr
                if (floor_rrr <= rrr_o or by_blend) and rrr <= MAX_RRR:
                    lvl_tp = tp
                    tp, rrr = tp_o, (bl if by_blend else rrr_o)
                    if by_blend:
                        how += f' - staggered front / middle / back, RRR blended (primary {rrr_o:.2f}; E3C:357)'
                    s = {'dir': 'SHORT' if direction == 'down' else 'LONG', 'entry': entry, 'sl': stop, 'tp': tp, 'tp_level': lvl_tp, 'rrr': round(rrr, 2), 'tp_zone': tz, 'attempts': tries,
                         'why': f"entry {how}; SL {why_sl}; TP {why_tp}", 'src': (round(step['bot'], 6), round(step['top'], 6)) if 'bot' in step else None}
                    break
                why_fail = f"RRR {min(rrr, rrr_o) if rrr <= MAX_RRR else rrr:.2f} outside [{floor_rrr}, {MAX_RRR}] (SL {stop:.5f} = {abs(entry - stop) / pip:.1f}p, TP {tp_o:.5f} = {abs(tp_o - entry) / pip:.1f}p: {why_tp[:60]})"
            if s is not None:
                break
        if s is None:
            log.append(f"{c['days'][0]} {c['shape']} {direction}: REJECT {why_fail} (entry {entry:.5f})"); continue
        if c.get('role') != 'transition' and 'Law 27' not in how:
            # E3C:1060-1066 Mechanism A (intra-zone staggered): 'Front | Zone edge nearest spot + forward spread | 33% | First contact'; 'Middle | ... key level from LQZ pattern'; 'Back | Zone edge
            # farthest from spot + forward spread'. The position is met at the FRONT: when price comes within the pair's forward spread (E3C 8.19) of the entry zone's near edge; the setup's
            # entry (the edge itself, or the key level inside the zone: F1-A / F1-C) / SL / TP / RRR stay as resolved. The entry zone = the supply / demand or sweep zone; at a pressure zone
            # (never an entry source, E3C:136) the order block / LQZ rung the entry stands on. Stop orders (transition, reinforcements) and Law-27 level entries have no zone to stagger in (D-62)
            zm = step if ('bot' in step and step['top'] > step['bot']) else a      # the structure the entry is resolved on (rung / order block / the zone itself for a TS-1 edge)
            edge = zm['bot'] if direction == 'down' else zm['top']
            if zm.get('sweep') and abs(edge - s['entry']) > 1e-9:
                edge = s['entry']                             # an entry resolved INSIDE a sweep zone (its middle / its extreme, after the edge failed the RRR floor) is met at that level, not at the edge (D-92)
            front = edge - FWD[pair] if direction == 'down' else edge + FWD[pair]
            back = (zm['top'] - FWD[pair]) if direction == 'down' else (zm['bot'] + FWD[pair])
            if (front <= s['entry']) if direction == 'down' else (front >= s['entry']):
                s['front'] = front
                if (back < s['sl']) if direction == 'down' else (back > s['sl']):
                    s['back'] = back
                    rr = [abs(s['tp'] - e) / abs(e - s['sl']) for e in (front, s['entry'], back)]
                    s['rrr_blended'] = round(0.33 * rr[0] + 0.33 * rr[1] + 0.34 * rr[2], 2)        # E3C:357 'Blended RRR (3-entry staggered)'
        s.update(day=c['days'][0], days=c['days'], shape=c['shape'], category=cat, session=SESSION_WINDOW[cat], sl_pips=round(abs(s['entry'] - s['sl']) / pip, 1),
                 t0=c.get('t0'), t1=c.get('t1'), anchor=a, role=c.get('role'), rest_from=c.get('rest_from'))
        ipz = a if a.get('ip') else _ip_at(a, X)
        # E3C:874-879 'narrativeAligned(setup, model, pair)': the narrative of a setup is its E2 shape day (R3 law: E2 designates the day's shape and direction; Phase 4.1 layer 5
        # 'Day-Shape Alignment'); a swing scalp of a range day is designated in BOTH directions (E3C:96), so neither is misaligned; the week's macro arc is a confidence term
        # (layer 7), not the gate (D-72)
        dday = next((d for d in E2['days'] if d['day'] == c['days'][0]), None)
        story = dday['dir'] if dday is not None else None
        if c['shape'] != 'SS' and c['dir'] in ('up', 'down'):
            story = c['dir']                                 # a directional step is its own designation
        misaligned = story in ('up', 'down') and (story == 'up') != (s['dir'] == 'LONG')
        if misaligned and ipz is not None and ipz['zfp_num'] > 30 and not a.get('sweep'):
            log.append(f"{s['day']} {s['shape']} {s['dir']} {s['entry']:.5f}: NARRATIVE - anchor zone {ipz['name']} ZFP {ipz['zfp_num']}% > 30 (E3C:874-876 'suppress > 30 (WEAK)')"); continue
        # Phase 10 (E3C:723-770): the pair's setup of a chain step is the mirror of the source pair's setup of the SAME step and day - DXY -> EU inverse direction, EU -> GU kept
        # ('GU mirrors ACTIVE EU mirrors, NEVER raw DXY'); a pair setup with no source setup behind it is an emergent trade (10.6) and carries no cascade bonus
        if MIRROR_OF is not None:
            inv_ = {'LONG': 'SHORT', 'SHORT': 'LONG'}
            want = inv_[s['dir']] if pair == 'EURUSD' else s['dir']
            s['cascade'] = (s['shape'], c.get('role'), s['day'], want) in MIRROR_OF
        s['confidence'], s['conf_parts'] = _confidence(s, X, E2, pair)
        if s['confidence'] < INCLUDE:
            log.append(f"{s['day']} {s['shape']} {s['dir']} {s['entry']:.5f}: CONFIDENCE {s['confidence']} < {INCLUDE} (E3C:1011)"); continue
        s['quality'] = 'HIGH' if s['confidence'] >= 80 else 'STANDARD'
        setups.append(s)
        if c['shape'] in ('BS', 'PBS') and c.get('role') != 'transition':
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
        nxt = next((k for k in kept[i + 1:] if abs(k['entry'] - q.get('tp_level', q['tp'])) <= 3 * pip and DAY_IDX[k['day']] >= DAY_IDX[q['day']] and k.get('parent_ref') is None), None)
        if nxt is not None and q.get('depth', 1) < 3:
            nxt['depth'] = q.get('depth', 1) + 1
            nxt['chain'] = q.get('chain') or f"CHAIN-{pair[:2]}{tag}{i + 1}"
            q['chain'] = nxt['chain']
    # a reinforcement whose parent was discarded goes with it; ids last, then each reinforcement names its parent by the parent's final id
    kept = [k for k in kept if k.get('parent_ref') is None or any(k['parent_ref'] is q for q in kept)]
    for i, q in enumerate(kept):
        q['id'] = f"{pair[:2]}{tag}{i + 1}"
    for k in kept:
        if k.get('parent_ref') is not None:
            k['parent'] = k['parent_ref']['id']
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
    # GS Law 6 'Primary -> R1: 20-30 pips | next MoM zone'; 8R.10 'map ALL liquidity zones between entry and TP': the first rocket is the first liquidity step at least 20 pips beyond the primary entry
    ref = s['entry'] - 20 * pip if dn else s['entry'] + 20 * pip
    path = sorted([r for r in real if (((r['bot'] + r['top']) / 2 <= ref and r['bot'] > s.get('tp_level', s['tp'])) if dn else ((r['bot'] + r['top']) / 2 >= ref and r['top'] < s.get('tp_level', s['tp'])))],
                  key=lambda r: -r['top'] if dn else r['bot'])
    # Law 5 / Fibonacci Spiderwebs (operator's grids in golden_week.json: 0 = the retest extreme, 1 = the swing before it): on a breakout that follows a retest the FIRST rocket stands
    # in the 0.786-1.0 band of that leg's grid (E3C:225 '0.786-1.0 | FINAL BLAST. Last chance before full extension') and its stop is the grid's 0.618 level - his three rockets:
    # DXY at level 1.0 / SL at 0.618; EURUSD at 0.786 / SL near 0.618; GBPUSD near 0.85 / SL at 0.618 (D-83; the prices are in memory/03 and memory/08, never here: goal prompt 'oracle numbers never appear in tool code')
    grid = None
    lg = E2.get('legs', [])
    for i_, l_ in enumerate(lg):
        if i_ > 0 and l_['shape'] in ('BS', 'PBS') and E2.get('far_liq') is not None and (l_['dir'] == 'down') == dn and lg[i_ - 1]['dir'] != l_['dir']:
            g0, g1 = lg[i_ - 1]['to'], lg[i_ - 1]['from']
            if abs(g1 - g0) > 5 * pip:
                grid = (g0, g1)
            break
    if grid is not None:
        g0, g1 = grid
        lv = lambda f_: g0 + f_ * (g1 - g0)
        b_lo, b_hi = min(lv(0.786), lv(1.0)) - pip, max(lv(0.786), lv(1.0)) + pip
        band = [r for r in real if b_lo <= (r['bot'] + r['top']) / 2 <= b_hi and (((r['bot'] + r['top']) / 2 < s['entry']) if dn else ((r['bot'] + r['top']) / 2 > s['entry']))]
        if band and path and not any(r is path[0] for r in band):
            # the 20-pip step is not in the band: the first rocket is the band's first step on the way, stopped at the grid's 0.618 (the EURUSD golden rocket, D-83);
            # a 20-pip step already inside the band stays as it is with its ladder stop (the DXY golden rocket, D-83)
            r0 = max(band, key=lambda r: r['top']) if dn else min(band, key=lambda r: r['bot'])
            path = [r0] + [r for r in path if r is not r0 and (((r['bot'] + r['top']) / 2 < (r0['bot'] + r0['top']) / 2) if dn else ((r['bot'] + r['top']) / 2 > (r0['bot'] + r0['top']) / 2))]
            grid = (g0, g1, r0)
        else:
            grid = None
    out, last = [], None
    for r in path:
        if len(out) >= 3:
            break
        e2 = (r['bot'] + r['top']) / 2
        if last is not None and abs(e2 - last) < 20 * pip:
            continue
        sl2, why2 = _stop(e2, 'down' if dn else 'up', r, X, pair)    # the same ladder-step stop as a primary (E3C:247-256; his Thursday rocket's stop stands 1-2 pips inside the 4H band above, D-54)
        if grid is not None and r is grid[2]:
            sl2, why2 = grid[0] + 0.618 * (grid[1] - grid[0]), 'the 0.618 level of the retest-leg Fib grid'
        if sl2 is None:
            log.append(f"reinforcement at {e2:.5f}: REJECT {why2}"); continue
        d2 = abs(sl2 - e2) / pip
        rr = abs(s.get('tp_level', s['tp']) - e2) / abs(e2 - sl2) if e2 != sl2 else 0      # measured to the target level (the TP buffer is an execution detail of the shared TP order)
        if not (GOLD_MIN <= d2 <= SL_CEIL and RRR_FLOOR <= rr <= MAX_RRR):
            log.append(f"reinforcement at {e2:.5f}: REJECT RRR {rr:.2f} / SL {d2:.1f}p"); continue
        if sum(1 for q in out if (min(q['entry'], q['sl']) <= max(s['entry'], s['sl']) and max(q['entry'], q['sl']) >= min(s['entry'], s['sl']))) >= 2:
            log.append(f"reinforcement at {e2:.5f}: REJECT overlapping risk (8R.3)"); continue
        di = min(len(s['days']) - 1, len(out) + 1)
        out.append({'dir': s['dir'], 'entry': e2, 'sl': sl2, 'tp': s['tp'], 'rrr': round(rr, 2), 'day': s['days'][di], 'days': s['days'][di:], 't0': None, 't1': s.get('t1'), 'rest_from': None,   # E3C:625 pending from the parent's start, live once the parent is filled, cancelled at the parent's TP
                    'shape': 'Ladder', 'category': 'Reinforcement', 'session': SESSION_WINDOW['Reinforcement'], 'sl_pips': round(d2, 1), 'parent': None, 'parent_ref': s, 'tp_zone': s['tp_zone'],
                    'anchor': r, 'size': (30, 20, 20)[len(out)], 'confidence': s['confidence'], 'quality': s['quality'],
                    'why': f"reinforcement {len(out) + 1} (stop-limit at the LQZ rung on the TP path; own ladder-step SL; parent TP)"})
        last = e2
    return out


def build(pair, monday, X, E2, source=None):
    """primary chain + the conditional setups of the ALTERNATIVE chain (P533 6.6 Step 4: 'For every primary chain, construct at least one alternative chain that activates if the primary
    fails at a specific Decision Zone'): only its breakout family (RWL / BS / WL) - the swing scalps are the same range for both readings"""
    global MIRROR_OF
    MIRROR_OF = (source or {}).get('keys') if pair != 'DXY' else None
    R = _build(pair, monday, X, E2, '')
    MIRROR_OF = None
    alt = E2.get('alt_chain')
    if ALT_SETUPS and alt is not None:
        A = _build(pair, monday, X, alt, 'A')
        keep = [s for s in A['setups'] if s['shape'] in ('RWL', 'BS', 'PBS', 'WL', 'Ladder')]
        az = (E2.get('alt') or {}).get('zone')
        ad = (E2.get('alt') or {}).get('dir')
        keep = keep if (az and ad) else []
        uniq = []
        for s in keep:                                        # the breakout and its transition entry can resolve to the same order: one of them (E3C:463 duplicate)
            if not any(abs(u['entry'] - s['entry']) < 1e-9 and abs(u['sl'] - s['sl']) < 1e-9 and u['dir'] == s['dir'] for u in uniq):
                uniq.append(s)
        keep = [s for s in uniq if not s.get('parent_ref') or s['parent_ref'] in uniq]
        for s in keep:
            s['alt'] = True
            # P533 6.6 Step 4 'construct at least one alternative chain that activates if the primary fails at a specific Decision Zone': the order is live only after a 1H close
            # beyond the Decision Zone in the alternative's direction
            s['trigger'] = {'dir': ad, 'level': az[1] if ad == 'up' else az[0], 'zone': (E2.get('alt') or {}).get('decision_zone')}
            s['why'] = f"ALTERNATIVE chain - live only after a 1H close {'above' if ad == 'up' else 'below'} {s['trigger']['level']:.5f} ({s['trigger']['zone']}): " + s['why']
        R['setups'] = R['setups'] + keep                      # contingency orders: not counted among the week's trades until triggered (7S.2 'Map the SS->BS Transition Setup as a contingency')
        R['log'] += ['ALT ' + l for l in A['log']]
    b0 = D.boundary_ms(monday)
    ss_days = [DAY_IDX[d['day']] for d in E2['days'] if d['shapes'] == ['SS'] and DAY_IDX[d['day']] < E2.get('n_real', 5)]
    for s in R['setups']:
        day0 = D.week_start_ms(monday) + DAY_IDX[s['day']] * 86400000
        if s.get('rest_from'):
            day0 = D.week_start_ms(monday) + DAY_IDX[s['rest_from']] * 86400000
        s['valid_from'] = max(day0, b0)
        s['valid_to'] = D.week_start_ms(monday) + (DAY_IDX[s['days'][-1]] + 1) * 86400000
    # Phase 1 / 2 / 6.3 (E3C:115 WorkingDayMap per day; E3C:129 'For each (WorkingDay, zone) pair ... generate a trade candidate'; E3C:468 cap key '(pair, anchorBucket, day)': one setup
    # per anchor per DAY; E3C:996 'f(T) Acceptance: ... 8 DXY + 8 EU + 8 GU ... LESS is REJECT'): a swing scalp of a consolidation is one order per anchor for EACH day of the
    # consolidation, bracketed by its day; which day meets which bound is not designated, so both rest every day (D-78)
    wk0 = D.week_start_ms(monday)
    pip_ = D.PIP[pair]
    path_ = E2.get('path') or []

    def reach_ok(day_i, entry):
        # goal prompt law 2 / GS Law 2 + Law 7 ('for each day's predicted shape, determine the expected price travel range ... Only generate setups at zones within the expected range
        # for that day's shape'; SS: 0-30 pips): a swing-scalp order rests on a day only when Engine 2's path of THAT day comes within 30 pips of its entry (G2 round 2 N-18)
        d_ = next((x for x in E2['days'] if DAY_IDX[x['day']] == day_i), None)
        if d_ is None or len(path_) < 2:
            return True
        def at(t):
            for (ta, pa), (tb, pb) in zip(path_, path_[1:]):
                if ta <= t <= tb:
                    return pa + (pb - pa) * ((t - ta) / (tb - ta) if tb > ta else 1.0)
            return path_[-1][1] if t > path_[-1][0] else path_[0][1]
        seg = [p for t, p in path_ if d_['t0'] <= t <= d_['t1']] + [at(d_['t0']), at(d_['t1'])]
        lo_, hi_ = min(seg), max(seg)
        return (0.0 if lo_ <= entry <= hi_ else min(abs(entry - lo_), abs(entry - hi_))) <= 30 * pip_
    out = []
    for s in R['setups']:
        s['anchor_key'] = (s['dir'], round(s['anchor']['bot'], 6), round(s['anchor']['top'], 6)) if 'bot' in s['anchor'] else (s['dir'], round(s['entry'], 6))
        if s['shape'] == 'SS' and s.get('role') != 'last-swing' and DAY_IDX[s['day']] in ss_days:
            run = sorted(d for d in ss_days if all(x in ss_days for x in range(min(d, DAY_IDX[s['day']]), max(d, DAY_IDX[s['day']]) + 1)))
            ok_days = [d for d in run if reach_ok(d, s['entry'])]
            for d in run:
                if d not in ok_days:
                    R['log'].append(f"{DAYS[d]} SS {s['dir']} {s['entry']:.5f}: NOT REACHABLE - the day's path stays more than 30 pips away (law 2)")
            run = ok_days
            for n, d in enumerate(run):
                q = s if n == 0 else dict(s, clone=True, origin=s)
                q.update(day=DAYS[d], days=[DAYS[d]], valid_from=max(wk0 + d * 86400000, b0), valid_to=wk0 + (d + 1) * 86400000)
                q['t0'], q['t1'] = q['valid_from'], q['valid_to']
                out.append(q)
        else:
            out.append(s)
    # L-04 '<= 11 setups per week per pair': a per-day repeat is the SAME setup (same anchor, entry, SL, TP) placed again for its day (E3C:468 cap key '(pair, anchorBucket, day)') -
    # it carries its setup's id with the day and is not a further setup (D-89)
    # ... the week carries at most 11 TRADES per pair, the per-day repeats included (L-04; R-07 'maximum 10 per week ... one to three per day'); reinforcements are not trades (R-10
    # 'These are not normal trades') and are not counted. Over the limit the repeats of the latest days go first, then the latest setups (G2 round 2 N-05, N-32)
    trades = [q for q in out if q.get('category') != 'Reinforcement' and not q.get('alt')]      # an alternative-chain order is a contingency: it becomes a trade only if its Decision Zone trigger fires
    extra = len(trades) - MAX_SETUPS
    if extra > 0:
        raw = lambda q: sum(v for _, v in (q.get('conf_parts') or []))        # the confidence sum before its clamp to 100 separates setups that all read 100
        for q in sorted(trades, key=lambda q: (0 if q.get('clone') else 1, -DAY_IDX[q['day']], q.get('confidence', 0), raw(q)))[:extra]:
            out = [x for x in out if x is not q and x.get('origin') is not q and x.get('parent_ref') is not q]
            R['log'].append(f"{q['day']} {q['shape']} {q['dir']} {q['entry']:.5f}: EMISSION_CAPPED - more than {MAX_SETUPS} trades this week (L-04)")
    out.sort(key=lambda q: (DAY_IDX[q['day']], 0 if q.get('parent_ref') is None else 1))
    pfx = out[0]['id'][:2] if out else ''
    n = 0
    for q in out:
        if q.get('alt') or q.get('clone'):
            continue
        n += 1
        q['id'] = f"{pfx}{n}"
    for q in out:
        if q.get('clone'):
            q['id'] = f"{q['origin']['id']}.{q['day']}"
    for q in out:
        if q.get('parent_ref') is not None:
            q['parent'] = q['parent_ref']['id']
    R['setups'] = out
    # the keys a receiving pair mirrors: every DXY setup; on EUR/USD only its ACTIVE mirrors (E3C:760 'GU mirrors ACTIVE EU mirrors, NEVER raw DXY')
    R['keys'] = {(q['shape'], q.get('role'), q['day'], q['dir']) for q in out if not q.get('alt') and (pair == 'DXY' or q.get('cascade'))}
    return R


def pine(pair, monday, R):
    """R-09: position boxes - red = SL side, green = entry -> TP, entry on their shared edge; each box spans the time Engine 2 gives its leg"""
    g = lambda v: ('%.3f' if pair == 'DXY' else '%.5f') % v
    b0, wk1 = D.boundary_ms(monday), D.week_end_ms(monday)
    o = ['    if show_e3']
    if not R['setups']:
        o.append('        na')
    seen_day, starts, placed = set(), {}, []
    span = (max([max(s['entry'], s['sl'], s['tp']) for s in R['setups']]) - min([min(s['entry'], s['sl'], s['tp']) for s in R['setups']])) if R['setups'] else 0.0
    txt_h = 0.035 * span                                      # one line of label text against the price span the setups cover
    for s in R['setups']:
        day0 = D.week_start_ms(monday) + DAY_IDX[s['day']] * 86400000
        first = s['day'] not in seen_day; seen_day.add(s['day'])
        x0 = max(day0 if first or s.get('t0') is None else s['t0'], b0)   # a setup is a resting order from the start of its day; later setups of the same day follow in leg order
        cond = s['category'] == 'Reinforcement'               # a rocket is a CONDITIONAL order (live only once its parent is filled, E3C:625): dashed outline, lighter fill, 'if <parent>' in its label
        if cond or s.get('rest_from'):                        # a resting order is drawn from the day it starts to rest (D-76), not from the day of its tag
            x0 = max(s.get('valid_from') or x0, b0)
        x1 = min(max(s['t1'] if s.get('t1') is not None else s['valid_to'], x0 + 6 * 3600000), wk1)
        o.append(f"        // {s['id']} {s['day']} {s['shape']} {s['dir']} E {g(s['entry'])} SL {g(s['sl'])} TP {g(s['tp'])} RRR {s['rrr']} | {s['category']} / {s['session']} | {s['why']}")
        o.append(f"        box.new({x0}, {g(max(s['entry'], s['sl']))}, {x1}, {g(min(s['entry'], s['sl']))}, bgcolor=color.new(color.rgb(242,54,69), {92 if (s.get('alt') or cond) else 84}), border_color=color.rgb(242,54,69), border_width=1, border_style={'line.style_dashed' if (s.get('alt') or cond) else 'line.style_solid'}, xloc=xloc.bar_time)")
        if s.get('front') is not None:                       # first-contact band between the front entry and the edge
            o.append(f"        box.new({x0}, {g(max(s['entry'], s['front']))}, {x1}, {g(min(s['entry'], s['front']))}, bgcolor=color.new(color.rgb(8,153,129), 70), border_color=color.new(color.rgb(8,153,129), 40), border_width=1, border_style=line.style_dotted, xloc=xloc.bar_time)")
        o.append(f"        box.new({x0}, {g(max(s['entry'], s['tp']))}, {x1}, {g(min(s['entry'], s['tp']))}, bgcolor=color.new(color.rgb(8,153,129), {94 if (s.get('alt') or cond) else 88}), border_color=color.rgb(8,153,129), border_width=1, border_style={'line.style_dashed' if (s.get('alt') or cond) else 'line.style_solid'}, xloc=xloc.bar_time)")
        k = starts.get(x0, 0); starts[x0] = k + 1             # setups resting from the same bar: labels staggered along the box so they do not print over each other (A13)
        row = (k + (DAY_IDX[s['day']] if s.get('clone') else 0)) % 3     # a per-day repeat steps one row per day so neighbouring days' labels do not run into each other
        ly = s['entry'] + (0.14 + 0.10 * row) * (s['tp'] - s['entry'])   # inside the green box near its own entry edge; three rows for setups that start together
        lx = max(x0 + 2 * 3600000, min(x0 + 3 * 3600000 + k * 9 * 3600000, x1 - 3600000, wk1 - 14 * 3600000))     # kept clear of the chart's right edge
        # no label over another label (A13; outside count 8 'setup labels pile on each other'): a label that would land within 14 hours and one text height of a placed one moves
        # along its box, then one row further into the green side
        for _try in range(8):
            if not any(abs(lx - px) < 14 * 3600000 and abs(ly - py) < txt_h for px, py in placed):
                break
            if _try % 2 == 0 and lx + 15 * 3600000 <= min(x1 - 3600000, wk1 - 14 * 3600000):
                lx += 15 * 3600000
            else:
                ly += 1.1 * txt_h * (1 if s['tp'] > s['entry'] else -1)
        placed.append((lx, ly))
        o.append(f"        label.new({lx}, {g(ly)}, \"{s['id'] if s.get('clone') else (s['id'] + ' ' + ('ALT ' if s.get('alt') else '') + s['shape'] + ' ' + ('S' if s['dir'] == 'SHORT' else 'L') + ' ' + format(s['rrr'], '.1f') + 'R' + ((' if ' + str(s.get('parent'))) if cond else '') + ((' if 1H close ' + ('>' if s['trigger']['dir'] == 'up' else '<') + ' ' + g(s['trigger']['level'])) if s.get('trigger') else ''))}\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.{'gray' if s.get('alt') else 'white'}, size=size.small)")
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
