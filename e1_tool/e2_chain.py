"""e2_chain.py - ENGINE 2: the macro shape chain, forward-mapped at the Monday anchor from the Engine 1 map (P533 Part VI :1725-2057 = E2X; FA 8-9; P533 2.2 / 2.2.1).
Rebuilt 2026-11-26 after the G2 audit (audit/G2_audit_engines.md B-08: the previous version planned a fixed week template). The chain is EXTENDED shape by shape from the canon tables:
  Step 1  current_shape()   matrix 6.2, rows in order with their ZFP conditions, on the 1H bars of the last pre-anchor sessions (E2X:7 'MUST be performed on the 1H timeframe';
                            E2X:165 'identify the current macro shape ... Determine which shape best describes the current price-zone relationship'); FA 9 conservation of energy
  Step 2  bounds(), branch() 6.5 anchoring; 6.4 / 6.4.1 ZFP-conditioned transitions; 6.4.2 MoM decision tree chosen by the Zone Reaction Counter (P533:1154-1161 + E3C:157-162 lifecycle);
                            BoM zones always react (E2X:149); priority rule (P533:1161); key rule 'swing scalp valley' (E2X:235); durations 6.8 / 6.4.2 / FA 9; trading speed 6.10
  Step 3  extend            shape by shape: trigger zone, ZFP, next shape, confidence per extension; max 5 shapes; stop under 25% cumulative confidence (E2X:169); later days stay undesignated
  Step 4  alternative       the Decision Zone, its threshold, the alternative chain and its confidence (E2X:171)
  Step 5  days              shape(s), direction, key zone, triggers (the expiry cuts of the day: P533 2.2 Spring Release), confidence; raw + adjusted timing (E2X:173, :301-302);
                            pairs: same shapes, inverted direction, own zones (E2X:178-196)
Direction when bias is unclear: pressure reading (E2X:253-258), then the 4H storyline tiebreaker, validated by the 6-check (E2X:149 -> E3C:1082-1095).
No price literal; every level is an Engine 1 zone edge, a liquidity band of the sealed V1 or a sweep zone."""
import datetime as dt
import e1_data as D, e1_sd as SD

NY = D.NY
CONF = {'VERY HIGH': 0.90, 'HIGH': 0.80, 'MODERATE-HIGH': 0.65, 'MODERATE': 0.50, 'LOW-MOD': 0.35}    # word tiers of 6.2 / 6.4 / 6.4.1 as the numbers 6.6 Step 3 needs (D-35)
DAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')
TF_RANK = {'15': 0, '30': 1, '60': 2, '240': 3}
SS_SWING = 2                                     # sessions per swing of a consolidation (E2X:21 'Each swing typically spans 1-3 trading sessions')
PIERCING = ('BS', 'PBS', 'WL', 'PWL', 'RWL', 'PRWL')
PIERCE_ORDER = {'FAIL': 0, 'PIERCED': 1, 'BREAK-RETURN': 2, 'SLOW': 3}      # how soon the bound goes (6.4.1 / 6.4.2 branch texts)
SS_MIN_SESSIONS = 2          # 6.8 'SS ... 2-5 sessions'
BS_SESSIONS = 3              # 6.8 'BS 1-3 sessions'; 6.10 'Assume price moves at 30-50% of the speed you think' -> the upper figure
SLOW_DAYS = 2                # 6.4.2 / 6.10.5 'slow consolidation ... 2-4 days'
FA9_DAYS = 1                 # FA 9 'EXPECT 1-2 FULL DAYS OF HTF CONSOLIDATION'


def _ms(d, h, mi=0):
    return int(dt.datetime(d.year, d.month, d.day, h, mi, tzinfo=NY).timestamp() * 1000)


def _skey(t):
    """P533 2.2.1 sessions, New York time: London 02:00-12:00, NY 12:00-17:00; Tokyo 17:00-02:00 belongs to the next trading day"""
    x = dt.datetime.fromtimestamp(t / 1000, NY)
    if 2 <= x.hour < 12:
        return (x.date(), 1, 'LON')
    if 12 <= x.hour < 17:
        return (x.date(), 2, 'NY')
    d = x.date() + dt.timedelta(days=1) if x.hour >= 17 else x.date()
    while d.weekday() >= 5:
        d += dt.timedelta(days=1)
    return (d, 0, 'TKY')


def week_sessions(monday):
    """the sessions after the anchor (Monday London open) to Friday 17:00 NY"""
    m = dt.date.fromisoformat(monday)
    out = []
    for i in range(5):
        d = m + dt.timedelta(days=i)
        if i > 0:
            out.append({'s': 'TKY', 'i': i, 't0': _ms(d - dt.timedelta(days=1), 17), 't1': _ms(d, 2)})
        out.append({'s': 'LON', 'i': i, 't0': _ms(d, 2), 't1': _ms(d, 12)})
        out.append({'s': 'NY', 'i': i, 't0': _ms(d, 12), 't1': _ms(d, 17)})
    return out


def _sidx(S, day, name):
    return next(k for k, s in enumerate(S) if s['i'] == day and s['s'] == name)


def past_sessions(pair, monday, n=6):
    g = {}
    for b in D.closed(pair, '60', monday)[-24 * 8:]:
        g.setdefault(_skey(b['time']), []).append(b)
    return [{'key': k, 'name': f"{k[0].isoformat()[5:]} {k[2]}", 'bars': g[k]} for k in sorted(g)[-n:]]


def session_events(ses, zones):
    """the 6.2 signatures inside one session, on its 1H bars: BS = a 1H CLOSE through a zone from the other side, still beyond at the session close
    (E2X:26 'Breakout confirmed by sustained move beyond the zone (15+ minutes)'); WL = a 1H wick through the zone's far edge with every 1H close back (E2X:35 'spike-and-reject')"""
    b = ses['bars']
    o, c = b[0]['open'], b[-1]['close']
    cl = [x['close'] for x in b]
    lo, hi = min(x['low'] for x in b), max(x['high'] for x in b)
    bs, wl = [], []
    for z in zones:
        if o > z['top'] and c < z['bot'] and any(x < z['bot'] for x in cl):
            bs.append((z, 'down'))
        elif o < z['bot'] and c > z['top'] and any(x > z['top'] for x in cl):
            bs.append((z, 'up'))
        elif o >= z['bot'] and lo < z['bot'] and min(cl) >= z['bot']:
            wl.append((z, 'down'))
        elif o <= z['top'] and hi > z['top'] and max(cl) <= z['top']:
            wl.append((z, 'up'))
    return {'name': ses['name'], 'key': ses['key'], 't0': b[0]['time'], 'o': o, 'c': c, 'lo': lo, 'hi': hi, 'bs': bs, 'wl': wl}


def counter(rx, strong=True):
    """P533:1154-1160 Zone Reaction Counter (strong reactions): 0 Virgin, 1-2 Active, 3+ Depleted; E3C:157-162 lifecycle: 'the fourth+ strong battle -> FORTRESS ... 95% direction flip -
    the immovable liquidity structure' (only where strong reactions are what is counted: IP zones; S/D zones count taps)"""
    if strong and rx >= 4:
        return 'Fortress'
    return 'Virgin' if rx == 0 else 'Active' if rx <= 2 else 'Depleted'


def info(z):
    """the class of an Engine 1 zone as Engine 2 reads it: IP zone (ZFP, BoM/MoM, strong reactions - P533:1145-1161), supply / demand zone (BoM/MoM, taps), sweep zone"""
    if z is None:
        return None
    if z.get('sweep'):
        return {'src': 'LSZ', 'cls': 'LSZ', 'rx': 0, 'counter': 'Virgin', 'zfp': None, 'tf': None}
    if 'kind' in z and 'tf' in z:
        return {'src': 'SD', 'cls': z['kind'], 'rx': z['mit'], 'counter': counter(z['mit'], strong=False), 'zfp': None, 'tf': z['tf']}
    m = z.get('mech', {})
    return {'src': 'IP', 'cls': m.get('bom', 'MoM'), 'rx': m.get('reactions', 0), 'counter': counter(m.get('reactions', 0)), 'zfp': z.get('zfp_num'), 'tf': None}


def _sweep_bound(X, up):
    """a side with no qualifying zone is bounded by its nearest unswept sweep zone wholly beyond spot (P533:1246-1262; P452:968 'Liquidity Sweep Zone ... brief breach then reversal';
    6.5 'LSZ' as rejection anchor). Touching sweep zones are one cluster; its extreme = where the stops end."""
    U, spot = X['U'], X['spot']
    side = 'Supply-side' if up else 'Demand-side'
    # a range is bounded by stops still resting: an extreme a later day already traded through (kept on the map as a recent sweep zone, D-77) has had its stops taken
    lv = sorted([z['level'] for z in X['lsz'] if z['side'] == side and not z['swept'] and not z.get('swept_recent')
                 and ((z['level'] - 0.05 * U > spot) if up else (z['level'] + 0.05 * U < spot))], reverse=not up)
    if not lv:
        return None
    cl = [lv[0]]
    for p in lv[1:]:
        if abs(p - cl[-1]) <= 0.05 * U + 1e-12:
            cl.append(p)
    ext = max(cl) if up else min(cl)
    # 'reach' = Step 0.45a (P533): 'Institutions often sweep 0.05-0.10 beyond the visible extreme before reversing' - how far the brief breach of this bound runs
    return {'bot': lv[0] - 0.05 * U if up else lv[0], 'top': lv[0] if up else lv[0] + 0.05 * U, 'ext': ext, 'reach': ext + 0.10 * U if up else ext - 0.10 * U, 'sweep': True, 'name': 'Liquidity Sweep Zone'}


def bounds(X):
    """6.5 'SS | Ceiling and Floor zones define the range | Both bounding zones: ZFP < 30%, Confluence >= 6' within the swing-scalp reach (GS Law 2: SS 0-30 pips);
    a side with no such IP zone is bounded by the nearest standing 1H / 4H supply-demand zone (an Engine 1 zone, R-04) - its behaviour comes from its class (BoM / MoM, 6.4.2), not from a ZFP number;
    strong first: 4H move >= 0.5 (P533 Step 0f grade, L-37), 1H move >= 0.3 (P452:753); else the nearest unswept sweep zone; else the nearest IP zone. The IP zone holding spot is the pivot."""
    spot, U = X['spot'], X['U']
    above = sorted([z for z in X['zones'] if z['bot'] > spot], key=lambda z: z['bot'])
    below = sorted([z for z in X['zones'] if z['top'] < spot], key=lambda z: -z['top'])
    pivot = next((z for z in X['zones'] if z['bot'] <= spot <= z['top']), None)
    if pivot is None and 'v1' in X:                          # no IP zone holds spot: the pivot area (P452 'EQUILIBRIUM ZONE: Pivot area') is the thick liquidity nearest spot (a V1 4H band; FA 2.1 Earth
        lq = sorted(X['v1']['240']['liquidity'], key=lambda b: 0.0 if b['bot'] <= spot <= b['top'] else min(abs(b['bot'] - spot), abs(b['top'] - spot)))   # = the foundation), within the swing-scalp reach (D-44)
        if lq and (0.0 if lq[0]['bot'] <= spot <= lq[0]['top'] else min(abs(lq[0]['bot'] - spot), abs(lq[0]['top'] - spot))) <= 0.30 * U:
            pivot = {'bot': lq[0]['bot'], 'top': lq[0]['top'], 'name': '4H liquidity (pivot)', 'liq': True}
    sd = [q for q in X['sd'] if q['tf'] in ('240', '60')]
    grade = lambda q: q.get('excursion', 0.0) >= (0.50 if q['tf'] == '240' else 0.30) * U
    pool = [q for q in sd if grade(q)] or sd

    def pick(ips, up):
        z = next((q for q in ips if q['zfp_num'] < 30 and q['score'] >= 6 and min(abs(q['bot'] - spot), abs(q['top'] - spot)) <= 0.30 * U), None)
        if z is not None:
            return z
        cands = sorted([q for q in pool if q['type'] == ('Supply' if up else 'Demand') and ((q['bot'] > spot) if up else (q['top'] < spot))], key=lambda q: q['bot'] if up else -q['top'])
        if cands:
            return dict(cands[0], name=cands[0]['label'])
        # 6.1.1 'bounded by IP zones above (resistance ceiling) and below (support floor)': a BoM pressure zone standing within the swing-scalp reach bounds the side before a sweep zone does
        # (E2X:149 'BoM zones ... ALWAYS react'); a MoM zone of 30%+ does not - it is pierced toward the liquidity behind it (6.4.2 'pierce through zone until reaching BoM Liquidity';
        # P452:2082), so the sweep zone stays the bound there (6.5 names the LSZ as a rejection anchor) (D-63)
        ipn = next((q for q in ips if q.get('mech', {}).get('bom') == 'BoM' and min(abs(q['bot'] - spot), abs(q['top'] - spot)) <= 0.30 * U), None)
        return ipn or _sweep_bound(X, up) or (ips[0] if ips else None)
    return {'ceil': pick(above, True), 'floor': pick(below, False), 'pivot': pivot, 'above': above, 'below': below}


def liquidity_beyond(X, z, up):
    """the opposing liquidity a consolidation retests (6.4.2 'Consolidation ends in price retesting opposing liquidity'): the first liquidity band of the sealed V1 (1H rung or 4H band,
    R-30 / GS Law 4 '1H / 4H LSZ') or unswept sweep zone lying wholly beyond the bound's own entry rung, within the canon cluster distance 0.15 of its far edge"""
    if z is None or 'v1' not in X:
        return None
    U = X['U']
    r1 = [r for r in X['v1']['60']['liquidity'] if r['bot'] <= z['top'] and r['top'] >= z['bot']]
    ref = (min(r1, key=lambda r: r['bot'])['top'] if up else max(r1, key=lambda r: r['top'])['bot']) if r1 else (z['bot'] if up else z['top'])
    bands = [dict(b, tf=tf) for tf in ('60', '240') for b in X['v1'][tf]['liquidity']]
    bands += [{'bot': l['level'] - 0.05 * U, 'top': l['level'], 'tf': None, 'lsz': True} if l['side'] == 'Supply-side' else {'bot': l['level'], 'top': l['level'] + 0.05 * U, 'tf': None, 'lsz': True}
              for l in X['lsz'] if not l['swept']]
    beyond = [b for b in bands if ((b['bot'] > ref and b['bot'] <= z['top'] + 0.15 * U) if up else (b['top'] < ref and b['top'] >= z['bot'] - 0.15 * U))]
    if not beyond:
        return None
    b = min(beyond, key=lambda b: b['bot']) if up else max(beyond, key=lambda b: b['top'])
    nm = 'sweep zone' if b.get('lsz') else f"{SD.TFNAME[b['tf']]} liquidity"
    return {'bot': b['bot'], 'top': b['top'], 'tf': b['tf'], 'liq': True, 'name': f'{nm} (opposing)'}


def branch(z, other, X, up):
    """what the bound will do (E2X:99-111 6.4.1; E2X:117-149 6.4.2; P533:1154-1161; E3C:157-162; P452:968):
    IP zone ZFP > 45 -> FAIL ('SS -> BS: bounding zone ZFP > 45% fails'); sweep zone -> HOLD (brief breach then reversal); BoM -> HOLD (always reacts) unless Depleted -> PIERCED;
    Fortress -> HOLD; MoM Depleted -> PIERCED ('will likely pierce through it to reach the BoM zone'); MoM Virgin -> HOLD-LONG ('Most likely MINOR REACTION branch ... zone holds ... Long Consolidation');
    MoM Active -> 'assess surrounding liquidity': opposing liquidity beyond the other bound -> SLOW (slow consolidation, retest of opposing liquidity, then pierce) else BREAK-RETURN (short consolidation)"""
    i = info(z)
    if i is None:
        return None, None, 'no bound'
    if i['src'] == 'IP' and i['zfp'] is not None and i['zfp'] > 45:
        return 'FAIL', ('HIGH' if i['zfp'] > 60 else 'MODERATE-HIGH'), f"ZFP {i['zfp']}% > 45: the bounding zone fails (6.4.1)"
    if i['cls'] == 'LSZ':
        return 'HOLD', 'HIGH', 'sweep zone: brief breach then reversal (P452 Pillar 9)'
    if i['counter'] == 'Fortress':
        return 'HOLD', 'HIGH', f"{i['rx']} strong reactions = FORTRESS (E3C lifecycle: 95% direction flip)"
    if i['cls'] == 'BoM':
        if i['counter'] == 'Depleted':
            return 'PIERCED', 'MODERATE', f"BoM with {i['rx']} reactions: depleted, likely to fail on the next test (P533:1159)"
        return 'HOLD', 'HIGH', 'BoM zone: always reacts if unmitigated (E2X:149)'
    if i['counter'] == 'Depleted':
        return 'PIERCED', 'MODERATE-HIGH', f"MoM with {i['rx']} reactions: depleted -> PIERCED branch (6.4.2; P533:1159)"
    if i['counter'] == 'Virgin':
        return 'HOLD-LONG', 'MODERATE-HIGH', 'virgin MoM: most likely MINOR REACTION branch - zone holds, long consolidation (6.4.2)'
    liq = liquidity_beyond(X, other, not up) if other is not None else None
    if liq is not None:
        return 'SLOW', 'MODERATE', f"active MoM ({i['rx']} reactions), opposing liquidity {liq['name']} beyond the other bound: slow consolidation ends retesting it, then pierce (6.4.2)"
    return 'BREAK-RETURN', 'MODERATE', f"active MoM ({i['rx']} reactions), no opposing liquidity to retest: zone breaks but price returns, short consolidation (6.4.2)"


def _ema(v, n):
    if len(v) < n:
        return None
    k, e = 2.0 / (n + 1), sum(v[:n]) / n
    for x in v[n:]:
        e += (x - e) * k
    return e


def trend_4h(pair, monday):
    """E3C:1086 '4H Trend: Bullish/Bearish/Ranging': 4H close vs EMA 50 vs EMA 200 (the trend rule Engine 1 applies on D1, here on 4H; D-36)"""
    c = [x['close'] for x in D.closed(pair, '240', monday)]
    e50, e200 = _ema(c, 50), _ema(c, 200)
    if e50 is None or e200 is None:
        return None
    return 'up' if c[-1] > e50 > e200 else 'down' if c[-1] < e50 < e200 else None


def storyline(pair, monday, spot, U):
    """E2X:258 '4H storyline tiebreaker: When in doubt, the 4H storyline bias decides. The weekly trend is identified on the 4H - it takes days and weeks to complete.'
    = the side of the most recent 4H BoM zone still STANDING at the anchor (e1_sd.valid) = the origin of the leg price is in; none standing -> 4H swing structure
    (last two 2-bar swing highs / lows: higher + higher = up, lower + lower = down) (C-02, D-36)"""
    b0 = D.week_start_ms(monday)
    zs = [z for z in SD.scan(pair, monday, '240') if z['kind'] == 'BoM' and SD.valid(z, spot, b0, U)]
    if zs:
        z = max(zs, key=lambda z: z['origin_time'])
        return ('down' if z['type'] == 'Supply' else 'up'), f"standing 4H BoM {z['type']} {z['bot']:.5g}-{z['top']:.5g}"
    b = D.closed(pair, '240', monday)[-90:]
    hs = [i for i in range(2, len(b) - 2) if b[i]['high'] == max(x['high'] for x in b[i - 2:i + 3])]
    ls = [i for i in range(2, len(b) - 2) if b[i]['low'] == min(x['low'] for x in b[i - 2:i + 3])]
    if len(hs) >= 2 and len(ls) >= 2:
        hh, hl = b[hs[-1]]['high'] > b[hs[-2]]['high'], b[ls[-1]]['low'] > b[ls[-2]]['low']
        if hh and hl:
            return 'up', '4H higher highs + higher lows'
        if not hh and not hl:
            return 'down', '4H lower highs + lower lows'
    return None, 'no 4H storyline'


def pressure_bias(pair, monday, since):
    """E2X:253-257 'When directional bias is unclear during consolidation: Candle size = pressure direction ... Wick direction = pressure direction: Upper wicks = buying pressure.
    Lower wicks = selling pressure. Triangle shapes: The flat side is receiving pressure.' Read on the 1H candles of the current consolidation (at most two days); a rule votes only when one side is
    'obviously' bigger (1.5 x) / one side of the triangle is flat (slope under a third of the other) (D-37)."""
    b = [x for x in D.closed(pair, '60', monday) if x['time'] >= since][-48:]
    votes = []
    if len(b) < 6:
        return None, votes
    bull = [x['close'] - x['open'] for x in b if x['close'] > x['open']]
    bear = [x['open'] - x['close'] for x in b if x['close'] < x['open']]
    mb, ms = (sum(bull) / len(bull) if bull else 0.0), (sum(bear) / len(bear) if bear else 0.0)
    votes.append(('candle size', 'up' if mb > 0 and mb >= 1.5 * ms else 'down' if ms > 0 and ms >= 1.5 * mb else None))
    uw = sum(x['high'] - max(x['open'], x['close']) for x in b)
    lw = sum(min(x['open'], x['close']) - x['low'] for x in b)
    votes.append(('wick direction', 'up' if uw >= 1.5 * lw else 'down' if lw >= 1.5 * uw else None))
    n = len(b)
    mx = (n - 1) / 2.0
    den = sum((i - mx) ** 2 for i in range(n))
    slope = lambda ys: sum((i - mx) * (y - sum(ys) / n) for i, y in enumerate(ys)) / den
    sh, sl = slope([x['high'] for x in b]), slope([x['low'] for x in b])
    tri = 'up' if (sl > 0 and abs(sh) <= abs(sl) / 3) else 'down' if (sh < 0 and abs(sl) <= abs(sh) / 3) else None
    votes.append(('triangle', tri))
    v = [d for _, d in votes if d]
    return ('up' if v.count('up') > v.count('down') else 'down' if v.count('down') > v.count('up') else None), votes


def six_check(X, pair, monday, proposed, B, fails, macro):
    """E3C:1084-1093 Trade Direction Validation (E2X:149): 1 4H trend, 2 BoM alignment (nearest BoM above -> short / below -> long), 3 liquidity sweep (nearest LSZ above / below -> initial sweep up / down:
    the big swing follows the other way, NOTES 'Liquidity is ALWAYS swept BEFORE a big swing', D-38), 4 zone failure, 5 macro shape, 6 counter-trend (a hard wall / standing BoM in the way);
    'if 4+ of 6 disagree with the proposed direction -> REVERSE'"""
    spot, U = X['spot'], X['U']
    inv = {'up': 'down', 'down': 'up'}
    v = [('4H trend', trend_4h(pair, monday))]
    boms = [q for q in X['sd'] if q['tf'] in ('240', '60') and q['kind'] == 'BoM' and q['mit'] <= 1]
    ab = [q['bot'] - spot for q in boms if q['type'] == 'Supply' and q['bot'] > spot]
    be = [spot - q['top'] for q in boms if q['type'] == 'Demand' and q['top'] < spot]
    v.append(('BoM alignment', None if not (ab or be) else 'down' if (ab and (not be or min(ab) < min(be))) else 'up'))
    la = [l['level'] - spot for l in X['lsz'] if not l['swept'] and l['level'] > spot]
    lb = [spot - l['level'] for l in X['lsz'] if not l['swept'] and l['level'] < spot]
    v.append(('liquidity sweep', None if not (la or lb) else 'down' if (la and (not lb or min(la) < min(lb))) else 'up'))
    v.append(('zone failure', fails))
    v.append(('macro shape', macro))
    t = B['ceil'] if proposed == 'up' else B['floor']
    wall = [z for z in X['zones'] if z['zfp_num'] < 20 and ((z['bot'] > spot and z['bot'] - spot <= 1.0 * U) if proposed == 'up' else (z['top'] < spot and spot - z['top'] <= 1.0 * U))]
    v.append(('counter-trend', inv[proposed] if wall else None))
    dis = sum(1 for _, d in v if d is not None and d != proposed)
    return (inv[proposed] if dis >= 4 else proposed), v, dis


def target(X, side, bound, src_tf=None):
    """6.1.2 'surges directionally toward the next IP zone or Structural Extreme Magnet'; 6.8 'Next Support / Resistance or Structural Extreme'; 6.4.2 'pierce through zone until reaching BoM Liquidity':
    the first Engine 1 object beyond the failing bound - an IP zone of ANY ZFP (B-13), a standing 1H / 4H supply-demand zone of the opposing type, an unswept sweep zone;
    TF element matching (E2X:244-250): a supply-demand target at most two timeframes above the source (never 4H from 15m) (A-07)"""
    if bound is None:
        return None
    dn = side == 'down'
    U = X['U']
    cands = []
    for z in X['zones']:
        if (z['top'] < bound['bot']) if dn else (z['bot'] > bound['top']):
            m = z.get('mech', {})
            if z['zfp_num'] >= 30 and m.get('bom') != 'BoM':
                continue                                     # P452:2082 'strong IP ... = it holds (valid TP)'; a weak (30%+) zone of class MoM is pierced on the way to BoM liquidity (E2X:140) (D-49)
            cands.append((z['top'] if dn else z['bot'], 2, {'bot': z['bot'], 'top': z['top'], 'name': z['name'], 'src': 'IP', 'zfp': z['zfp_num'], 'cls': m.get('bom'), 'rx': m.get('reactions', 0), 'ip': z}))
    for z in X['sd']:
        if z['tf'] in ('240', '60') and z['type'] == ('Demand' if dn else 'Supply') and ((z['top'] <= bound['top'] and z['bot'] < bound['bot']) if dn else (z['bot'] >= bound['bot'] and z['top'] > bound['top'])):
            if z['kind'] == 'MoM' and not any(q['bot'] <= z['top'] and q['top'] >= z['bot'] and q['zfp_num'] < 30 for q in X['zones']):
                continue                                     # P452:2082 'No IP + standalone MoM = it gets pierced (not valid TP)'; 6.4.2 'pierce through zone until reaching BoM Liquidity' (D-49)
            if src_tf is None or TF_RANK[z['tf']] <= TF_RANK[src_tf] + 2:
                cands.append((z['top'] if dn else z['bot'], 1, {'bot': z['bot'], 'top': z['top'], 'name': z['label'], 'src': 'SD', 'cls': z['kind'], 'rx': z['mit'], 'tf': z['tf'], 'sd': z}))
    for l in X['lsz']:
        if not l['swept'] and l['side'] == ('Demand-side' if dn else 'Supply-side') and ((l['level'] < bound['bot']) if dn else (l['level'] > bound['top'])):
            cands.append((l['level'] + 0.05 * U if dn else l['level'] - 0.05 * U, 0, {'bot': l['level'] if dn else l['level'] - 0.05 * U, 'top': l['level'] + 0.05 * U if dn else l['level'],
                                                                                     'name': 'Liquidity Sweep Zone', 'src': 'LSZ', 'sweep': True, 'ext': l['level']}))
    if not cands:
        return None
    return sorted(cands, key=lambda c: (-c[0] if dn else c[0], c[1]))[0][2]


def measured_move(X, bound, other, side):
    """P452 Pillar 9 Step 4 (MANDATORY when ZFP > 45%): Range = the failing zone to the opposite IL level; Raw = High + Height (down: Low - Height); cross-referenced with the nearest Structural
    Extreme within +-0.20 (anchored; +-0.05 VERY HIGH), else a round number at the target (semi-anchored), else unanchored"""
    U = X['U']
    if bound is None or other is None:
        return None
    if side == 'up':
        h = bound['top'] - other['bot']; raw = bound['top'] + h
        ext = [l['p'] for l in X['L'] if l['pillar'] == 5 and l.get('extreme') and ('High' in l['kind'] or 'Ceiling' in l['kind'] or 'Reversal' in l['kind'])]
    else:
        h = other['top'] - bound['bot']; raw = bound['bot'] - h
        ext = [l['p'] for l in X['L'] if l['pillar'] == 5 and l.get('extreme') and ('Low' in l['kind'] or 'Sweep' in l['kind'] or 'Reversal' in l['kind'])]
    near = sorted(ext, key=lambda p: abs(p - raw))
    if near and abs(near[0] - raw) <= 0.20 * U:
        p, tier = near[0], ('VERY HIGH' if abs(near[0] - raw) <= 0.05 * U else 'HIGH')
        mark = 'Anchored Projection - structural extreme ' + ('at' if tier == 'VERY HIGH' else 'near') + ' target'
    else:
        q = round(raw / (0.25 * U)) * 0.25 * U
        p, tier, mark = (q, 'MODERATE', 'Semi-Anchored Projection - round number at target') if abs(q - raw) <= 0.03 * U else (raw, 'LOW', 'Unanchored Projection - no structural extreme at target level')
    return {'bot': p - 0.05 * U if side == 'up' else p, 'top': p if side == 'up' else p + 0.05 * U, 'name': f'BREAKOUT EXTENSION TARGET ({mark})', 'src': 'MM', 'tier': tier}


def after_bs(t):
    """6.4.1 (E2X:97-111): the TARGET zone decides what follows the Breakout Surge; BoM zones always react (E2X:149); sweep zone: brief breach then reversal (P452) = WL -> RWL (6.4 'WL -> RWL')"""
    if t is None:
        return 'R', 'MODERATE', 'no mapped zone beyond: stabilisation (6.4.1 has no row; D-39)'
    if t['src'] == 'LSZ':
        return 'WL+RWL', 'MODERATE-HIGH', 'sweep zone: brief breach then reversal (P452 Pillar 9) -> WL -> RWL (6.4)'
    if t['src'] == 'MM':
        return 'R', 'HIGH' if t['tier'] in ('VERY HIGH', 'HIGH') else 'MODERATE', 'measured-move target reached (6.4 BS -> R)'
    if t['src'] == 'SD':
        c = counter(t['rx'], strong=False)
        if t['cls'] == 'BoM' and c in ('Virgin', 'Active'):
            return 'RWL', 'HIGH', f"{t['name']}: a BoM zone always reacts (E2X:149) = Hard-Wall class -> RWL (6.4.1)"
        if c == 'Depleted':
            return 'PBS', 'MODERATE', f"{t['name']}: depleted ({t['rx']} taps) -> pierced, cascade (6.4.2; P533:1159)"
        if t['tf'] == '240' and c == 'Virgin':
            return 'R', 'MODERATE', f"{t['name']}: 4H MoM one-and-done - minor reaction, then pierce (E2X:239)"
        return 'R', 'MODERATE', f"{t['name']}: MoM - minor reaction (6.4.2)"
    z = t['zfp']
    if z < 20:
        return 'RWL', 'HIGH', f"{t['name']} ZFP {z}% < 20 (Hard Wall): rejection, NOT R / PBS (6.4.1)"
    if z <= 40:
        return 'R', 'HIGH', f"{t['name']} ZFP {z}% (20-40): stabilisation (6.4.1)"
    if z > 80:
        return 'PBS', 'HIGH', f"{t['name']} ZFP {z}% > 80: strong cascade (6.4.1)"
    if z > 60:
        return 'PBS', 'MODERATE', f"{t['name']} ZFP {z}% > 60: cascade continues (6.4.1)"
    return 'R', 'MODERATE', f"{t['name']} ZFP {z}% (40-60): 6.4.1 has no row; stabilisation (D-39)"


LOWER = {'VERY HIGH': 'HIGH', 'HIGH': 'MODERATE-HIGH', 'MODERATE-HIGH': 'MODERATE', 'MODERATE': 'LOW-MOD', 'LOW-MOD': 'LOW-MOD'}


def current_shape(X, pair, monday, B):
    """6.6 Step 1 (E2X:165): the Shape Classification Decision Matrix 6.2 (E2X:50-57) applied IN ORDER to the 1H bars of the last six pre-anchor sessions; a row whose price-action condition holds
    but whose ZFP condition does not is the best description one tier lower (E2X:165 'which shape best describes', D-40); FA 9 after two piercing sessions -> 1-2 days of consolidation"""
    zones, U, spot = X['zones'], X['U'], X['spot']
    ps = [session_events(s, zones) for s in past_sessions(pair, monday, 6)]
    # E2X:35 a whiplash is ONE 'spike-and-reject' move: a session that crosses back through the zones the previous session pierced is that whiplash's rejection, not a new breakout
    for a, b in zip(ps, ps[1:]):
        pierced = [(z, d) for z, d in a['bs'] + a['wl']]
        back = [(z, d) for z, d in b['bs'] if any(z is q and d != e for q, e in pierced)]
        if back:
            b['bs'] = [x for x in b['bs'] if x not in back]
            if a['bs']:                                      # the earlier breakout + its full return = a whiplash spread over two sessions
                a['wl'] = a['wl'] + a['bs']; a['bs'] = []
            b['rejection'] = True
    rows = []
    for s in reversed(ps[-3:]):                                  # row 1: BS / PBS
        if s['bs']:
            dn = [z for z, d in s['bs'] if d == 'down']
            up = [z for z, d in s['bs'] if d == 'up']
            zs, d = (dn, 'down') if len(dn) >= len(up) else (up, 'up')
            if all((spot < z['bot']) if d == 'down' else (spot > z['top']) for z in zs):
                rows.append({'row': 1, 'shape': 'PBS' if len(zs) >= 2 else 'BS', 'dir': d, 'zone': zs[0], 'full': any(z['zfp_num'] > 45 for z in zs), 'tier': 'HIGH',
                             'why': f"{s['name']}: 1H close through {', '.join(z['name'] for z in zs)} (ZFP {'/'.join(str(z['zfp_num']) for z in zs)}), price still beyond"})
            break
    for s in reversed(ps[-3:]):                                  # row 2: WL / PWL
        if s['wl']:
            z, d = s['wl'][0]
            sweep = any(z['bot'] - 0.10 * U <= l['level'] <= z['top'] + 0.10 * U for l in X['lsz'])
            rows.append({'row': 2, 'shape': 'PWL' if len(s['wl']) >= 2 else 'WL', 'dir': d, 'zone': z, 'full': z['zfp_num'] < 20 and sweep, 'tier': 'HIGH',
                         'why': f"{s['name']}: spike {d} through {z['name']} (ZFP {z['zfp_num']}), every 1H close back{' at a sweep target' if sweep else ''}"})
            break
    if len(ps) > 1 and (ps[-2]['bs'] or ps[-2]['wl']) and not ps[-1]['bs']:      # row 3: R right after a BS / WL ('duration < 1 session')
        hold = [z for z in zones if z['bot'] - 0.05 * U <= spot <= z['top'] + 0.05 * U]
        if hold:
            z = hold[0]
            rows.append({'row': 3, 'shape': 'R', 'dir': 'range', 'zone': z, 'full': 20 <= z['zfp_num'] <= 40, 'tier': 'MODERATE', 'why': f"after {ps[-2]['name']} price stabilises at {z['name']} (ZFP {z['zfp_num']})"})
    near = [z for z in zones if abs((z['bot'] + z['top']) / 2 - spot) <= 0.30 * U]              # row 4: WLS
    if len(near) >= 3:
        span = max(z['top'] for z in near) - min(z['bot'] for z in near)
        ev = [s for s in ps[-5:] if s['bs'] or s['wl']]
        dirs = {d for s in ev for _, d in s['bs'] + s['wl']}
        if span <= 0.50 * U and len(ev) >= 3 and dirs == {'up', 'down'}:
            rows.append({'row': 4, 'shape': 'WLS', 'dir': 'range', 'zone': near[0], 'full': span >= 0.30 * U and all(15 <= z['zfp_num'] <= 40 for z in near), 'tier': 'HIGH',
                         'why': f"{len(near)} IP zones within {span / U:.2f}, {len(ev)} piercing sessions both ways"})
    c, f = B['ceil'], B['floor']
    if c is not None and f is not None and f['top'] < spot < c['bot'] and not ps[-1]['bs'] and not (len(ps) > 1 and ps[-2]['bs']):    # row 5: SS
        ic, if_ = info(c), info(f)
        full = ic['src'] == 'IP' and if_['src'] == 'IP' and ic['zfp'] < 30 and if_['zfp'] < 30
        rows.append({'row': 5, 'shape': 'SS', 'dir': 'range', 'zone': c, 'full': full, 'tier': 'HIGH', 'why': f"price between {f['name']} and {c['name']}, no breakout in the last two sessions"})
    bsp = [s for s in ps[-4:-1] if s['bs']]                                                      # row 6: RWL
    if bsp:
        z, d = bsp[-1]['bs'][0]
        if (spot > z['top']) if d == 'down' else (spot < z['bot']):
            rows.append({'row': 6, 'shape': 'RWL', 'dir': 'up' if d == 'down' else 'down', 'zone': z, 'full': z['zfp_num'] < 20, 'tier': 'MODERATE-HIGH',
                         'why': f"after {bsp[-1]['name']}'s breakout price is back through {z['name']}"})
    rows.sort(key=lambda r: r['row'])
    full = [r for r in rows if r['full']]
    if full:
        s0 = dict(full[0])
    elif rows:
        s0 = dict(rows[0])
        s0['tier'] = LOWER[s0['tier']]
        s0['why'] += ' [the row\'s ZFP condition is not met: best description, one tier lower]'
    else:
        s0 = {'row': 0, 'shape': 'SS', 'dir': 'range', 'zone': B['pivot'] or c, 'full': False, 'tier': 'MODERATE', 'why': 'no matrix row matched: consolidation (D-40)'}
    mv = []                                                  # FA 9 counts piercing MOVES: consecutive sessions piercing in the same direction are one move
    for k, s in enumerate(ps):
        ds = {d for _, d in s['bs'] + s['wl']}
        if ds:
            d = ds.pop() if len(ds) == 1 else 'both'
            if mv and mv[-1][0] == k - 1 and mv[-1][1] == d:
                mv[-1] = (k, d)
            else:
                mv.append((k, d))
    n_pierce = len(mv)
    if n_pierce >= 2:
        s0.update(shape='SS', dir='range', phase='post-energy', why=s0['why'] + f" | FA 9: {n_pierce} piercing sessions -> 'EXPECT 1-2 FULL DAYS OF HTF CONSOLIDATION'")
    ib = [k for k, s in enumerate(ps) if s['bs']]
    el = (len(ps) - 1 - ib[-1]) if ib else len(ps) + 3
    s0.setdefault('phase', 'Early' if el < 1 else 'Mid' if el <= 3 else 'Late')
    last_bs = ps[ib[-1]]['bs'][0][1] if ib else None
    s0.update(history=ps, elapsed=el, n_pierce=n_pierce, last_bs=last_bs)
    return s0


def _strong_4h_near(X):
    """E2X:235 key rule 'If not right near a strong 4H pressure zone right now - BS is most likely days away': a 4H BoM zone (0-1X) or a Tier-1 IP zone within the swing-scalp reach (GS Law 2: 30 pips)"""
    spot, U = X['spot'], X['U']
    dist = lambda z: 0.0 if z['bot'] <= spot <= z['top'] else min(abs(z['bot'] - spot), abs(z['top'] - spot))
    return any(dist(q) <= 0.30 * U for q in X['sd'] if q['tf'] == '240' and q['kind'] == 'BoM' and q['mit'] <= 1) or any(dist(z) <= 0.30 * U for z in X['zones'] if z.get('tier') == 'Tier 1')


def _triggers(X, date):
    """6.6 Step 5 (d) 'note any volatility triggers (auctions, expiries, economic events)': the option cuts of the day (P533 2.2 'Spring Release' at 10:01 NY); red-folder calendar: NO DATA (optional input, L-32)"""
    cut = sorted({(l['strike'], l['notional_m']) for l in X['L'] if l['pillar'] == 8 and l.get('cut') == date}, key=lambda x: -x[1])
    t = [f"10:00 NY cut {s:.4f} {n / 1000:.1f}bn" if n >= 1000 else f"10:00 NY cut {s:.4f} {n}M" for s, n in cut[:3]]
    return t + ['red folder: NO DATA']


def build(pair, monday, X, lead=None, force_dir=None):
    """6.6 Steps 1-5. lead = the DXY chain when translating to a pair (same shapes, inverted direction, the pair's own zones: E2X:178-196); force_dir = the alternative chain (Step 4)"""
    U, spot = X['U'], X['spot']
    S = week_sessions(monday)
    t_anchor = D.boundary_ms(monday)
    inv = {'up': 'down', 'down': 'up', 'range': 'range', None: None}
    B = bounds(X)
    ceil, floor, pivot = B['ceil'], B['floor'], B['pivot']
    s0 = current_shape(X, pair, monday, B)
    story, story_why = storyline(pair, monday, spot, U)
    az = s0.get('zone')
    audit = ['Primary Timeframe: 1H | Structural Validation: 4H',
             f"Current Shape: {s0['shape']} {s0['dir']} ({s0['tier']}) | Anchoring Zone: {az['name'] if az else '-'} | ZFP: {az.get('zfp', az.get('zfp_num', '-')) if az else '-'} | {s0['why']}"]
    bc, bf = branch(ceil, floor, X, True), branch(floor, ceil, X, False)
    for nm, z, b in (('Ceiling', ceil, bc), ('Floor', floor, bf)):
        i = info(z)
        audit.append(f"{nm}: {z['name'] if z else '-'} [{i['src'] + ' ' + str(i['cls']) + ' ' + i['counter'] + (' ZFP ' + str(i['zfp']) if i['zfp'] is not None else '') if i else '-'}] -> {b[0]} ({b[2]})")
    b4 = D.closed(pair, '240', monday)[-6:]
    val = [nm for nm, z in (('ceiling', ceil), ('floor', floor)) if z is not None and any((x['close'] > z['top']) if nm == 'ceiling' else (x['close'] < z['bot']) for x in b4)]
    audit.append('4H Structural Validation: ' + ('rejects - 4H close beyond the ' + ', '.join(val) if val else 'confirms - no 4H close beyond either bound in the last day'))
    mode = lead['mode'] if lead is not None else ('bs0' if (force_dir is None and s0['shape'] in ('BS', 'PBS')) else 'ss')
    # ---------------------------------------------------------------- direction and the plan (session indices into S)
    steps = []
    bdir = kind = near = far = tgt = tgt2 = far_liq = None
    why = ''
    if lead is not None:
        bdir = inv[lead['bdir']]
        why = f"pair translation of the DXY chain ({lead['bdir']} inverted)" if lead['bdir'] else 'pair translation of the DXY chain: DXY ranges all week (Part IX: DXY gives direction and timing, the pair its levels)'
    elif mode == 'bs0':
        bdir, why = s0['dir'], 'breakout in progress at the anchor'
    elif force_dir is not None:
        bdir, why = force_dir, 'ALTERNATIVE chain (6.6 Step 4): the other bound fails'
    else:
        pr = sorted([(PIERCE_ORDER[b[0]], side) for side, b in (('up', bc), ('down', bf)) if b[0] in PIERCE_ORDER])
        if pr and (len(pr) == 1 or pr[0][0] < pr[1][0]):
            bdir = pr[0][1]
            why = f"the {'ceiling' if bdir == 'up' else 'floor'} is the bound that goes: {(bc if bdir == 'up' else bf)[2]}"
        elif pr:
            since = s0['history'][-s0['elapsed']]['t0'] if 0 < s0['elapsed'] < len(s0['history']) else t_anchor - 2 * 86400000      # the current consolidation (since the last BS session)
            pb, votes = pressure_bias(pair, monday, since)
            prop = pb or story
            why = (f"both bounds go the same way ({pr[0][0]}): pressure reading {pb} {[(n, d) for n, d in votes]}" if pb else
                   f"both bounds go the same way, pressure reading unclear {[(n, d) for n, d in votes]}: 4H storyline tiebreaker = {story} ({story_why})")
            bdir = prop
    if bdir in ('up', 'down') and lead is None and mode == 'ss':
        fails = 'up' if bc[0] in ('FAIL', 'PIERCED') else 'down' if bf[0] in ('FAIL', 'PIERCED') else None
        chk, votes, dis = six_check(X, pair, monday, bdir, B, fails, story)
        audit.append(f"Direction Validation 6-check for {bdir}: " + ', '.join(f"{n}={d}" for n, d in votes) + f" -> {dis} disagree" + (f" -> REVERSED to {chk}" if chk != bdir else ''))
        bdir = chk
    if bdir is not None:
        near, far = (ceil, floor) if bdir == 'up' else (floor, ceil)
        kind = (bc if bdir == 'up' else bf)[0] if mode == 'ss' else None
        if lead is not None:
            kind = lead.get('kind')
    audit.append(f"Breakout direction: {bdir or ('none' if lead is not None else 'none - both bounds hold')} | {why}")
    # ---------------------------------------------------------------- Step 3: chain extension
    chain, cum = [], 1.0

    def add(shape, d, a, b, frm, to, tier, trig, same=False, role=None, fixed=None):
        nonlocal cum                                         # same=True: a step of the transition just counted (6.4.2 branch 4 is ONE prediction: retest, then pierce)
        f = 1.0 if same else CONF[tier]
        if fixed is None and (len(chain) >= 5 or cum * f < 0.25) or a >= len(S):
            return False
        cum = fixed if fixed is not None else cum * f
        chain.append({'shape': shape, 'dir': d, 's0': a, 's1': min(b, len(S)), 'frm': frm, 'to': to, 'tier': tier, 'cum': round(cum, 2), 'trigger': trig, 'role': role or shape})
        audit.append(f"  -> {shape} {d} sessions {S[a]['s']} {DAYS[S[a]['i']]} .. {S[min(b, len(S)) - 1]['s']} {DAYS[S[min(b, len(S)) - 1]['i']]} | Trigger: {trig} | {tier} -> cumulative {round(cum, 2)}")
        return True
    raw_day = adj_day = None
    if lead is not None:
        # E2X:178-196: the pair's chain = the DXY shapes on the same sessions, direction inverted; every level from the pair's OWN map (E3C 10.2 'zones of the same element')
        near, far = ((ceil, floor) if bdir == 'up' else (floor, ceil)) if bdir else (None, None)
        roles = {st.get('role') for st in lead['chain']}
        far_liq = liquidity_beyond(X, far, bdir == 'down') if ('retest' in roles and far is not None) else None
        tgt = (measured_move(X, near, far, bdir) if lead.get('kind') == 'FAIL' else target(X, bdir, near, (far_liq or {}).get('tf'))) if near is not None else None
        tgt2 = target(X, bdir, tgt) if (tgt is not None and roles & {'pbs', 'bs2'}) else None
        where = {'consol': (floor, ceil), 'ss_all': (floor, ceil), 'retest': (far, far_liq), 'bs': (far_liq or near, tgt), 'wl': (tgt, tgt), 'rwl': (tgt, near), 'ss_after': (tgt, near),
                 'r': (tgt, tgt), 'pbs': (tgt, tgt2), 'bs2': (tgt or near, tgt2), 'bs0': (None, near), 'rwl0': (near, far), 'wl0': (near, near), 'ss0': (near, far)}
        for st in lead['chain']:
            d = inv.get(st['dir'], st['dir'])
            frm, to = where.get(st.get('role'), (None, None))
            add(st['shape'], d, st['s0'], st['s1'], frm, to, st['tier'], 'DXY: ' + st['trigger'], role=st.get('role'), fixed=st['cum'])
        raw_day, adj_day = lead.get('raw_day'), lead.get('adj_day')
    elif mode == 'bs0':
        tgt = near
        dur = max(1, BS_SESSIONS - 1)
        add(s0['shape'], bdir, 0, dur, None, near, 'HIGH', f"breakout in progress toward {near['name'] if near else '-'} (6.8 BS 1-3 sessions)", role='bs0')
        ti = info(near)
        nx, tier, txt = after_bs({'src': ti['src'], 'zfp': ti['zfp'], 'cls': ti['cls'], 'rx': ti['rx'], 'tf': ti['tf'], 'name': near['name'], 'tier': 'HIGH'} if ti else None)
        if nx in ('RWL', 'WL+RWL'):
            ok = (add('WL', bdir, dur, dur + 1, near, near, tier, txt, role='wl0') and add('RWL', inv[bdir], dur, dur + 1, near, far, tier, txt, same=True, role='rwl0')) if nx == 'WL+RWL' else add('RWL', inv[bdir], dur, dur + 1, near, far, tier, txt, role='rwl0')
            if ok and add('SS', 'range', dur + 1, dur + 1 + 3 * FA9_DAYS + 2, near, far, 'HIGH', 'RWL -> SS: reversal exhausts, new range (6.4)', role='ss0'):
                tgt2 = target(X, bdir, near)
                add('BS', bdir, dur + 3 * FA9_DAYS + 3, len(S), near, tgt2, 'HIGH', "6.3 'BS -> RWL -> SS -> BS: complete false breakout cycle. Second BS often succeeds'", role='bs2')
        elif nx == 'R':
            if add('R', 'range', dur, dur + 1, near, near, tier, txt, role='r'):
                add('RWL', inv[bdir], dur + 1, dur + 2, near, far, 'HIGH', "6.3 'BS -> R -> RWL: ... Signals false breakout'", role='rwl0')
                add('SS', 'range', dur + 2, len(S), near, far, 'HIGH', 'RWL -> SS (6.4)', role='ss0')
        else:
            tgt2 = target(X, bdir, near)
            add('PBS', bdir, dur, dur + 2, near, tgt2, tier, txt, role='pbs')
            add('SS', 'range', dur + 2, len(S), tgt2, near, 'MODERATE', "6.3 'PBS -> R/SS'", role='ss_after')
    elif bdir is None:
        add('SS', 'range', 0, len(S), floor, ceil, 'HIGH', "6.4.1 'SS | All < 30% (both sides hold) | SS continues' - every bound holds", role='ss_all')
    else:
        el = s0['elapsed']
        need = 3 * SLOW_DAYS if kind == 'SLOW' else SS_MIN_SESSIONS
        if not _strong_4h_near(X):
            need = max(need, 3 * SLOW_DAYS)
            audit.append("Key rule (E2X:235): no strong 4H pressure zone within reach -> 'BS is most likely days away. This is swing scalp valley'")
        rem = max(0, need - el)
        raw_day = S[min(rem, len(S) - 1)]['i'] if rem < len(S) else 5
        if s0.get('phase') == 'post-energy':                 # FA 9 'EXPECT 1-2 FULL DAYS OF HTF CONSOLIDATION' after the last piercing session: the first full trading day(s) after it are consolidation
            lp = max((s['key'][0] for s in s0['history'] if s['bs'] or s['wl']), default=None)
            m0 = dt.date.fromisoformat(monday)
            full = sum(1 for k in range(5) if m0 + dt.timedelta(days=k) > lp) if lp else 0
            first_free = next((k for k in range(5) if m0 + dt.timedelta(days=k) > lp), 0) if lp else 0
            raw_day = max(raw_day, first_free + FA9_DAYS)
        adj_day = raw_day + 1
        audit.append(f"Trading Speed (6.10): raw timing = transition on {DAYS[raw_day] if raw_day < 5 else 'next week'} (consolidation {need} sessions, {el} elapsed) -> adjusted +1 day = "
                     f"{DAYS[adj_day] if adj_day < 5 else 'next week'}")
        # The NY Cut Cage (P533:690-691): option walls of $850M+ standing in the range pin price until their 10:00 NY cut; 'At exactly 10:01 AM NY ... the market experiences a Spring Release -
        # violently breaking out or reversing'; Appendix B.2 'Option expiry timing (Spring Release) +20-30%' lifts the caged bound over the 45% of 6.4.1. The LAST cut known at the anchor is the
        # trigger; trading speed adds a day (6.10); FA 9's full day(s) of consolidation remain the floor (D-60)
        m0 = dt.date.fromisoformat(monday)
        lo_c = (floor['bot'] if floor else spot) ; hi_c = (ceil['top'] if ceil else spot)
        cage = [l for l in X['L'] if l.get('cut') and l.get('tier', 9) <= 2 and l['cut'] >= monday and lo_c - l.get('band', 0.0) <= l['p'] <= hi_c + l.get('band', 0.0)]
        if cage:
            k_c = (dt.date.fromisoformat(max(l['cut'] for l in cage)) - m0).days
            if 0 <= k_c <= 4:
                fa9 = raw_day if s0.get('phase') == 'post-energy' else 0
                adj_day = max(k_c + 1, fa9)
                audit.append(f"NY Cut Cage (P533:690-691): {len(cage)} wall(s) of $850M+ inside the range, last 10:00 NY cut {DAYS[k_c]} -> Spring Release {DAYS[k_c]} 10:01 NY, + 1 day (6.10) = transition on "
                             f"{DAYS[adj_day] if adj_day < 5 else 'next week'}")
        if adj_day > 4:
            add('SS', 'range', 0, len(S), floor, ceil, 'HIGH', f"the {'ceiling' if bdir == 'up' else 'floor'} goes, but after this week (6.10): SS continues", role='ss_all')
            bdir = None
        else:
            i_lon, i_ny = _sidx(S, adj_day, 'LON'), _sidx(S, adj_day, 'NY')
            add('SS', 'range', 0, i_lon, floor, ceil, s0['tier'] if s0['shape'] == 'SS' else 'MODERATE-HIGH', f"consolidation ({s0.get('phase')}) between {floor['name'] if floor else '-'} and {ceil['name'] if ceil else '-'}", role='consol')
            far_liq = liquidity_beyond(X, far, bdir == 'down') if kind in ('SLOW', 'BREAK-RETURN') else None
            src_tf = (far_liq or {}).get('tf') or info(near)['tf']
            if far_liq is not None:
                rs = 'RWL' if (s0.get('last_bs') == bdir) else 'SS'
                add(rs, inv[bdir], i_lon, i_ny, far, far_liq, (bc if bdir == 'up' else bf)[1], f"6.4.2 'Consolidation ends in price retesting opposing liquidity' ({far_liq['name']})"
                    + (" - a whiplash against the preceding BS = RWL (6.1.4)" if rs == 'RWL' else ''), role='retest')
                cum /= CONF[(bc if bdir == 'up' else bf)[1]]          # the retest and the pierce are one branch of 6.4.2: its confidence is counted once, on the BS
            # 6.5 'BS | ... target zone determines magnitude | Target: Measured Move'; 6.1.2 'toward the next IP zone or Structural Extreme Magnet': with no zone standing beyond the
            # failing bound the breakout still has its measured-move target (P452 Pillar 9 Step 4) (D-80)
            tgt = measured_move(X, near, far, bdir) if kind == 'FAIL' else (target(X, bdir, near, src_tf) or measured_move(X, near, far, bdir))
            k4 = src_tf == '240' or (tgt is not None and (tgt.get('tf') == '240' or tgt['src'] in ('IP', 'MM')))
            dur = BS_SESSIONS * (2 if k4 else 1)
            ok = add('BS', bdir, i_ny, i_ny + dur, far_liq or near, tgt, (bc if bdir == 'up' else bf)[1],
                     f"{near['name']} goes ({kind}) -> BS toward {tgt['name'] if tgt else '-'} ({dur} sessions{', 4H element: twice as long (6.10)' if k4 else ''})", role='bs')
            nx, tier, txt = after_bs(tgt)
            if nx == 'RWL' and tgt is not None and any((not l['swept']) and l['side'] == ('Demand-side' if bdir == 'down' else 'Supply-side')
                                                       and ((tgt['bot'] - 0.10 * U <= l['level'] <= tgt['top']) if bdir == 'down' else (tgt['bot'] <= l['level'] <= tgt['top'] + 0.10 * U)) for l in X['lsz']):
                nx = 'WL+RWL'                                # unswept stops rest against the target: the surge ends in a whiplash into them (P452:968 'brief breach then reversal'; 6.4 'WL -> RWL')
                txt += ' - an unswept sweep zone lies against the target: the surge ends in a whiplash into it (WL -> RWL)'
            e = i_ny + dur
            if ok and nx in ('RWL', 'WL+RWL'):
                wl = nx == 'WL+RWL' and add('WL', bdir, e, e + 1, tgt, tgt, tier, txt, role='wl')
                if add('RWL', inv[bdir], e, e + 1, tgt, near, tier, txt, same=bool(wl), role='rwl'):
                    add('SS', 'range', e + 1, len(S), tgt, near, 'HIGH', 'RWL -> SS: reversal exhausts, new range (6.4)', role='ss_after')
            elif ok and nx == 'R':
                if add('R', 'range', e, e + 1, tgt, tgt, tier, txt, role='r'):
                    tz = tgt.get('ip') if tgt else None
                    if tz is not None and tz['zfp_num'] > 45:
                        tgt2 = target(X, bdir, tgt)
                        add('BS', bdir, e + 1, e + 1 + BS_SESSIONS, tgt, tgt2, 'MODERATE', "6.4 'R -> BS (2nd leg): Recovery at mid-range zone that also fails'", role='bs2')
                    else:
                        add('SS', 'range', e + 1, len(S), tgt, near, 'MODERATE-HIGH', "6.4.1 'R | Persists > 1 full session | SS (reclassify)'", role='ss_after')
            elif ok and nx == 'PBS':
                tgt2 = target(X, bdir, tgt)
                if add('PBS', bdir, e, e + 2, tgt, tgt2, tier, txt, role='pbs'):
                    add('SS', 'range', e + 2, len(S), tgt2, tgt, 'MODERATE', "6.3 'PBS -> R/SS'", role='ss_after')
    if lead is None and mode == 'ss' and bdir is not None:
        near, far = (ceil, floor) if bdir == 'up' else (floor, ceil)
    # E3C Phase 1 step 6 (E3C:123) 'Trading Speed Adjustment: for each day, if E2's confidence < 65%, propagate the shape to the next day (the predicted shape "spills over" - today's move
    # often becomes tomorrow's move)'; step 7 '5 entries present, no null shape': a chain that ends before Friday (6.6 Step 3: cumulative confidence under 25%) leaves its last shape running
    # into the next trading day when that shape's confidence is under 65% (D-70)
    if chain and lead is None and chain[-1]['s1'] < len(S) and chain[-1]['cum'] < 0.65 and chain[-1]['shape'] != 'SS':
        d_last = S[chain[-1]['s1'] - 1]['i']
        nxt_day = [k for k in range(len(S)) if S[k]['i'] == d_last + 1]
        if nxt_day:
            chain[-1]['s1'] = nxt_day[-1] + 1
            chain[-1]['spill'] = True
            audit.append(f"  spill-over (E3C:123): {chain[-1]['shape']} {chain[-1]['dir']} runs into {DAYS[d_last + 1]} (confidence {chain[-1]['cum']} < 0.65)")
    audit.append('chain: ' + ' -> '.join(f"{c['shape']} [{c['tier']}, cum {c['cum']}]" for c in chain))
    # ---------------------------------------------------------------- Step 5: path + day decomposition
    f_edge = floor['top'] if floor else spot - 0.30 * U
    c_edge = ceil['bot'] if ceil else spot + 0.30 * U
    mid = (pivot['bot'] + pivot['top']) / 2 if pivot else (f_edge + c_edge) / 2
    pts = [(t_anchor, spot)]
    legs = []

    def edge_in(z, d):                                           # the edge price meets first moving in direction d
        return None if z is None else (z['top'] if d == 'down' else z['bot'])

    def edge_out(z, d):
        return None if z is None else (z['bot'] if d == 'down' else z['top'])
    pos, last_dir = spot, None
    for st in chain:
        a, b = st['s0'], st['s1']
        t0, t1 = max(S[a]['t0'], t_anchor), S[b - 1]['t1']
        if st['shape'] in ('SS', 'R'):
            lo, hi = (min(f_edge, c_edge), max(f_edge, c_edge)) if st['shape'] == 'SS' and st['frm'] in (floor, ceil, None) else \
                     (min(edge_in(st['frm'], 'down') or pos, edge_in(st['to'], 'up') or pos), max(edge_in(st['frm'], 'down') or pos, edge_in(st['to'], 'up') or pos))
            days_in = sorted({S[k]['i'] for k in range(a, b)})
            if not days_in:
                continue
            if st['shape'] == 'SS':
                # 6.1.1 'Each swing typically spans 1-3 trading sessions' -> two sessions per swing. Phase: before a transition the swings are counted BACK from it - the last one runs in the
                # breakout direction and ends at the pivot when a retest follows (6.4.2 'Consolidation ends in price retesting opposing liquidity'), else at the failing bound; with no
                # transition this week the first swing continues the one in progress at the anchor (the last pre-anchor session closed in its upper half -> up) (D-57)
                ses = list(range(a, b))
                swings = [ses[k:k + SS_SWING] for k in range(0, len(ses), SS_SWING)]
                idx = chain.index(st)
                nx = chain[idx + 1] if idx + 1 < len(chain) else None
                if nx is not None and bdir in ('up', 'down') and nx['shape'] in ('RWL', 'BS', 'PBS', 'WL'):
                    swings = [ses[max(0, k - SS_SWING):k] for k in range(len(ses), 0, -SS_SWING)][::-1]          # whole swings counted back from the transition
                    dirs = [(bdir if (len(swings) - 1 - j) % 2 == 0 else inv[bdir]) for j in range(len(swings))]
                    end_piv = nx.get('role') == 'retest' and pivot is not None
                else:
                    lp = past_sessions(pair, monday, 1)
                    lb = lp[-1]['bars'] if lp else []
                    up0 = (lb[-1]['close'] >= (max(x['high'] for x in lb) + min(x['low'] for x in lb)) / 2) if lb else (abs(hi - pos) < abs(pos - lo))
                    dirs = [('up' if (j % 2 == 0) == up0 else 'down') for j in range(len(swings))]
                    end_piv = False
                for j, (sw, dj) in enumerate(zip(swings, dirs)):
                    d_end = min(t1, S[sw[-1]]['t1'])
                    nxt = hi if dj == 'up' else lo
                    if end_piv and j == len(swings) - 1:
                        nxt = pivot['bot'] if dj == 'down' else pivot['top']
                    legs.append({'day': DAYS[S[sw[0]]['i']], 'shape': 'SS', 'dir': dj, 'from': pos, 'to': nxt, 'from_zone': None, 'to_zone': ceil if dj == 'up' else floor,
                                 't0': pts[-1][0], 't1': d_end, 'pad': False})
                    pos, last_dir = nxt, dj
                    pts.append((d_end, pos))
                continue
            for j, di in enumerate(days_in):                     # one swing per session-day (6.1.1 'Each swing typically spans 1-3 trading sessions')
                d_end = min(t1, S[max(k for k in range(a, b) if S[k]['i'] == di)]['t1'])
                go_up = (abs(hi - pos) < abs(pos - lo)) if last_dir is None else (last_dir == 'down')   # first swing: toward the nearer bound (P533 2.3 'magnetize toward the IL levels', D-41)
                nxt = hi if go_up else lo
                legs.append({'day': DAYS[di], 'shape': st['shape'], 'dir': 'up' if go_up else 'down', 'from': pos, 'to': nxt, 'from_zone': None,
                             'to_zone': (ceil if go_up else floor) if st['shape'] == 'SS' else st['to'], 't0': pts[-1][0], 't1': d_end, 'pad': False})
                pos, last_dir = nxt, ('up' if go_up else 'down')
                pts.append((d_end, pos))
        else:
            d = st['dir']
            k_st = chain.index(st)
            if st['shape'] in ('WL', 'PWL') and k_st + 1 < len(chain) and chain[k_st + 1]['s0'] == a:
                t1 = t0 + (t1 - t0) // 3                         # the spike and its rejection share one session (6.8 'WL ... < 1 session', 'RWL ... < 1 session'): the spike comes first
            if st['shape'] == 'RWL' and st['to'] is not None and st['to'] is near and st['frm'] is not far:
                nxt = edge_out(st['to'], d)                      # back to the prior origin = the broken bound, its far side (6.8 'RWL ... Prior origin'; role reversal)
            elif st['shape'] == 'WL':
                nxt = st['to'].get('ext', edge_out(st['to'], d)) if st['to'] else pos
            else:
                nxt = edge_in(st['to'], d) if st['to'] is not None else pos
                if st['to'] is not None and st['to'].get('liq'):
                    nxt = edge_out(st['to'], d)
            if nxt is None:
                nxt = pos
            legs.append({'day': DAYS[S[a]['i']], 'shape': st['shape'], 'dir': d, 'from': pos, 'to': nxt, 'from_zone': st['frm'], 'to_zone': st['to'], 't0': max(t0, pts[-1][0]), 't1': t1, 'pad': False})
            pos, last_dir = nxt, d
            pts.append((t1, pos))
    last_t = chain[-1]['s1'] if chain else 0
    n_real = (S[last_t - 1]['i'] + 1) if chain else 0
    days = []
    for i in range(5):
        di = [st for st in chain if any(S[k]['i'] == i for k in range(st['s0'], st['s1']))]
        if not di:
            continue
        shapes = []
        for st in di:
            if not shapes or shapes[-1] != st['shape']:
                shapes.append(st['shape'])
        dt0 = max(_ms(dt.date.fromisoformat(monday) + dt.timedelta(days=i - 1), 17) if i else t_anchor, t_anchor)
        dt1 = _ms(dt.date.fromisoformat(monday) + dt.timedelta(days=i), 17)
        def at(t):                                           # the path's price at time t (linear between its points)
            for (ta, pa), (tb, pb) in zip(pts, pts[1:]):
                if ta <= t <= tb:
                    return pa + (pb - pa) * ((t - ta) / (tb - ta) if tb > ta else 1.0)
            return pts[-1][1] if t > pts[-1][0] else pts[0][1]
        pp = [p for t, p in pts if dt0 <= t <= dt1] + [at(dt0), at(min(dt1, pts[-1][0]))]
        lo, hi = (min(pp), max(pp)) if pp else (f_edge, c_edge)
        if shapes == ['SS']:
            # 6.1.1 'Price oscillates within a defined range bounded by IP zones above ... and below': the day's range runs INTO its bounding zones (to their far edges); a sweep-zone
            # bound is breached briefly, 0.05-0.10 beyond its extreme (P533 Step 0.45a) (D-64)
            # a DEPLETED bound (3 reactions) is pierced until the liquidity beyond it (P533:1159; 6.4.2 'pierce through zone until reaching BoM Liquidity'): the range runs to that liquidity (D-85)
            def far_of(z, up):
                if z.get('reach') is not None:
                    return z['reach']
                lb = liquidity_beyond(X, z, up) if (info(z) or {}).get('counter') == 'Depleted' else None
                return (lb['top'] if up else lb['bot']) if lb is not None else (z['top'] if up else z['bot'])
            f_far = far_of(floor, False) if floor else f_edge; c_far = far_of(ceil, True) if ceil else c_edge
            lo, hi = min(lo, f_edge, f_far), max(hi, c_edge, c_far)
        dirs = [st['dir'] for st in di if st['shape'] in ('BS', 'PBS')] or [st['dir'] for st in di if st['shape'] in ('RWL', 'WL')]
        key = next((z['name'] for st in reversed(di) for z in (st['to'], st['frm']) if z is not None and z.get('name')), '-')
        days.append({'day': DAYS[i], 'date': (dt.date.fromisoformat(monday) + dt.timedelta(days=i)).isoformat(), 'shapes': shapes, 'dir': dirs[-1] if dirs else 'range',
                     'lo': lo, 'hi': hi, 'key': key, 'conf': di[-1]['cum'], 'triggers': _triggers(X, (dt.date.fromisoformat(monday) + dt.timedelta(days=i)).isoformat()), 't0': dt0, 't1': dt1})
    alt = alt_chain = None
    if force_dir is None and lead is None and mode == 'ss':
        if bdir is not None and far is not None:
            ib = info(far)
            thr = f"ZFP {ib['zfp']}% > 45 or a 1H close beyond it" if ib and ib['zfp'] is not None else '1H close beyond it'
            alt_chain = build(pair, monday, X, None, force_dir=inv[bdir])
            alt = {'decision_zone': far['name'], 'dir': inv[bdir], 'threshold': thr, 'conf': alt_chain['chain'][-1]['cum'] if alt_chain['chain'] else None,
                   'text': f"PRIMARY: {' -> '.join(c['shape'] for c in chain)} | DECISION ZONE: {far['name']} {thr} -> ALTERNATIVE: {' -> '.join(c['shape'] for c in alt_chain['chain'])} "
                           f"[confidence {alt_chain['chain'][-1]['cum'] if alt_chain['chain'] else '-'}]"}
        elif bdir is None and ceil is not None and floor is not None:
            cand = sorted([(PIERCE_ORDER.get(b[0], 9), side, z) for side, z, b in (('up', ceil, bc), ('down', floor, bf))], key=lambda x: x[0])[0]
            alt_chain = build(pair, monday, X, None, force_dir=cand[1])
            alt = {'decision_zone': cand[2]['name'], 'dir': cand[1], 'threshold': '1H close beyond it', 'conf': alt_chain['chain'][-1]['cum'] if alt_chain['chain'] else None,
                   'text': f"PRIMARY: SS | DECISION ZONE: {cand[2]['name']} 1H close beyond it -> ALTERNATIVE: {' -> '.join(c['shape'] for c in alt_chain['chain'])}"}
        if alt:
            audit.append(alt['text'])
    return {'pair': pair, 'monday': monday, 's0': s0, 'storyline': story, 'bdir': bdir, 'kind': kind, 'mode': mode, 'chain': chain, 'days': days, 'path': pts, 'legs': legs,
            'alt': alt, 'alt_chain': alt_chain, 'audit': audit, 'ceil': ceil, 'floor': floor, 'pivot': pivot, 'target': tgt, 'target2': tgt2, 'far_liq': far_liq,
            'near': near, 'far': far, 'mid': mid, 'range': (f_edge, c_edge), 'n_real': n_real, 'raw_day': raw_day, 'adj_day': adj_day}


def pine(pair, monday, E2):
    """R-03: the day BOXES, then the LINE; the alternative chain's line dotted (6.6 Step 4); undesignated days are not drawn (C-16)"""
    g = lambda v: ('%.3f' if pair == 'DXY' else '%.5f') % v
    col = {'SS': '120,144,156', 'BS': '255,167,38', 'PBS': '255,112,67', 'WL': '171,71,188', 'PWL': '171,71,188', 'RWL': '171,71,188', 'R': '102,187,106', 'WLS': '255,112,67'}
    arrow = {'up': ' up', 'down': ' down', 'range': ''}
    o = ['    if show_e2']
    # the five day tags stand in ONE row above the week's forecast envelope (clear of the candles: a tag inside a breakout day's box sat on that day's candles, A13)
    y_tag = max((d['hi'] for d in E2['days']), default=0.0)
    y_tag += 0.06 * (y_tag - min((d['lo'] for d in E2['days']), default=y_tag)) + 1e-9
    for d in E2['days']:
        c = col.get(d['shapes'][-1], '200,200,200')
        o.append(f"        box.new({d['t0']}, {g(d['hi'])}, {d['t1']}, {g(d['lo'])}, bgcolor=color.new(color.rgb({c}), 88), border_color=color.new(color.rgb({c}), 20), border_width=1, border_style=line.style_dashed, xloc=xloc.bar_time)")
        o.append(f"        label.new({(d['t0'] + d['t1']) // 2 if d['day'] != 'Fri' else d['t0'] + (d['t1'] - d['t0']) // 4}, {g(y_tag)}, \"{d['day']} {'+'.join(d['shapes'])}\\n{arrow[d['dir']].strip()} {int(d['conf'] * 100)}%\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.rgb({c}), size=size.small)")
    p = E2['path']
    for (t0, p0), (t1, p1) in zip(p, p[1:]):
        o.append(f"        line.new({t0}, {g(p0)}, {t1}, {g(p1)}, xloc=xloc.bar_time, color=color.rgb(255,235,59), width=2)")
    if E2.get('alt_chain'):
        q = E2['alt_chain']['path']
        for (t0, p0), (t1, p1) in zip(q, q[1:]):
            o.append(f"        line.new({t0}, {g(p0)}, {t1}, {g(p1)}, xloc=xloc.bar_time, color=color.new(color.rgb(255,235,59), 55), width=1, style=line.style_dotted)")
    if len(o) == 1:
        o.append('        na')
    return o


if __name__ == '__main__':
    import sys, e1_pine as EP
    monday, pair = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'DXY'
    lead = build('DXY', monday, EP.run('DXY', monday)) if pair != 'DXY' else None
    E2 = build(pair, monday, EP.run(pair, monday), lead)
    f = '%.3f' if pair == 'DXY' else '%.5f'
    for a in E2['audit']:
        print(a)
    for d in E2['days']:
        print(f"  {d['day']} {d['date']}: {' + '.join(d['shapes']):<16} {d['dir']:<5} | Key Zone: {d['key'][:30]:<30} | {f % d['lo']}-{f % d['hi']} | Confidence: {int(d['conf'] * 100)}% | {'; '.join(d['triggers'])}")
    print('path:', ' -> '.join(f % p for _, p in E2['path']))
    for l in E2['legs']:
        print(f"  leg {l['day']} {l['shape']:<4} {l['dir']:<5} {f % l['from']} -> {f % l['to']}")
