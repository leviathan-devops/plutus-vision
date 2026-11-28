"""plutus.py - ONE command per week / pair -> ONE Pine v6 script (S6): Engine 1 map + Engine 2 shape chain + Engine 3 trade setups, every number from data closed before the Monday anchor.
usage: python3 plutus.py MONDAY PAIR [out.pine] [--weekly]      (PAIR = DXY | EURUSD | GBPUSD; default output e1_tool/out/PLUTUS_<PAIR>_<MONDAY>.pine;
daily anchoring by default (D-131), --weekly = every order fixed at the Monday anchor)"""
import sys, os
import e1_pine as EP, e2_chain as E2, e1_data as D

HERE = os.path.dirname(os.path.abspath(__file__))


_MEMO = {}


def _setups(pair, monday):
    """the setups of a source pair for the Phase 10 cascade, at the week anchor"""
    k = ('setups', pair, monday)
    if k not in _MEMO:
        _MEMO[k] = run(pair, monday)[2]
    return _MEMO[k]


def _src_days(pair, monday):
    """the source pair's orders CONFIRMED at each day's anchor under daily anchoring - {day index: {(shape, direction)}} - each decided only from bars closed by that day's
    trading-day open (the source's own daily leak check), so a receiving pair may use day i's record at day i (D-142)"""
    k = ('days', pair, monday)
    if k not in _MEMO:
        _MEMO[k] = {i: set(p.get('keys', ())) for i, p in run(pair, monday, daily=True)[1].get('daily', {}).items()}
    return _MEMO[k]


def _map(pair, monday):
    """the Engine 1 map of the week (built at the Monday anchor, never under a daily update)"""
    k = ('map', pair, monday)
    if k not in _MEMO:
        saved = D.ASOF.pop(monday, None)
        try:
            _MEMO[k] = EP.run(pair, monday)
        finally:
            if saved is not None:
                D.ASOF[monday] = saved
    return _MEMO[k]


def _asof(monday, t, fn):
    saved = D.ASOF.get(monday)
    D.ASOF[monday] = t
    try:
        return fn()
    finally:
        if saved is None:
            D.ASOF.pop(monday, None)
        else:
            D.ASOF[monday] = saved


def _map_at(pair, monday, t):
    """L-53 DAILY ZONE UPDATE: the Engine 1 map rebuilt as of instant t (a day's London open) - only bars closed by t"""
    k = ('map_at', pair, monday, t)
    if k not in _MEMO:
        _MEMO[k] = _asof(monday, t, lambda: EP.run(pair, monday))
    return _MEMO[k]


def _engines_at(pair, monday, t):
    """Engine 2 + 3 re-anchored at instant t on the map of t (D-136); the Phase 10 source pairs re-anchored at the same instant"""
    k = ('eng_at', pair, monday, t)
    if k not in _MEMO:
        import copy
        X = copy.deepcopy(_map_at(pair, monday, t))
        XD = copy.deepcopy(_map_at('DXY', monday, t)) if pair != 'DXY' else None
        _MEMO[k] = _asof(monday, t, lambda: engines(pair, monday, X, XD, t=t))
    return _MEMO[k]


def engines(pair, monday, X, XD=None, t=None):
    """Engine 2 + Engine 3 on the Engine 1 map X (XD = the DXY map: the master direction for a pair)"""
    lead = E2.build('DXY', monday, XD) if pair != 'DXY' else None      # DXY = master direction (P533:1899-1917; GS Law 7)
    chain = E2.build(pair, monday, X, lead)
    if lead is not None:
        chain['divergence'] = divergence(lead, E2.build(pair, monday, X, None))
        # the pair's alternative chains = the DXY alternatives translated onto the pair's own zones (P533 6.6 v5.0.0 pair translation; Step 4); Decision Zone = the pair's own
        # bound on the failing side (D-110)
        chain['alts'] = []
        for a_ in lead.get('alts') or []:
            pa = E2.build(pair, monday, X, a_['chain'])
            nz = pa.get('near')
            if nz is not None and pa.get('bdir') in ('up', 'down'):
                chain['alts'].append({'alt': {'decision_zone': nz.get('name', ''), 'zone': (nz['bot'], nz['top']), 'reach': nz.get('reach'), 'dir': pa['bdir'], 'threshold': '1H close beyond it',
                                              'text': f"ALTERNATIVE (DXY alternative translated): {' -> '.join(c['shape'] for c in pa['chain'])}"}, 'chain': pa})
    import e3_trades as E3
    source = None
    if pair != 'DXY':
        # Phase 10 (E3C:723-770): DXY is processed first; EUR/USD mirrors the DXY setups, GBP/USD mirrors the active EUR/USD mirrors
        src_ = 'DXY' if pair == 'EURUSD' else 'EURUSD'
        source = _setups(src_, monday) if t is None else _engines_at(src_, monday, t)[1]
    return chain, E3.build(pair, monday, X, chain, source)


def _cut(path, t0, t1):
    """the part of a forecast path between t0 and t1, with its ends interpolated"""
    if not path or path[-1][0] < t0 or path[0][0] > t1:
        return []
    def at(t):
        for (ta, pa), (tb, pb) in zip(path, path[1:]):
            if ta <= t <= tb:
                return pa + (pb - pa) * ((t - ta) / (tb - ta) if tb > ta else 1.0)
        return path[-1][1] if t > path[-1][0] else path[0][1]
    a, b = max(t0, path[0][0]), min(t1, path[-1][0])
    return [(a, at(a))] + [(t, p) for t, p in path if a < t < b] + [(b, at(b))]


def _status(s, t_from, t_to, pair):
    """an order's state at instant t_to from the 15m bars closed by then: 'pending' (entry not reached), 'open' (filled, neither SL nor TP), 'done' (filled and resolved)"""
    lng = s['dir'] == 'LONG'
    filled = False
    for x in D.closed_until(pair, '15', t_to):
        if x['time'] < t_from:
            continue
        if not filled:
            if not ((x['low'] <= s['entry']) if lng else (x['high'] >= s['entry'])):
                continue
            filled = True
        if ((x['low'] <= s['sl']) if lng else (x['high'] >= s['sl'])) or ((x['high'] >= s['tp']) if lng else (x['low'] <= s['tp'])):
            return 'done'
    return 'open' if filled else 'pending'


PHASE10_REENTRY = True     # D-142: a re-entry on a receiving pair needs the source pair's matching order that day (E3C Phase 10, L-52)
FLOW27 = True              # D-144: an order the drawn line reaches while an opposite order runs to its TP, inside that move (> 3 pips short of its TP), is not in the trade flow (Law 27)
REANCHOR_DRAW = True       # D-138: once the chain in force has failed, the line and day boxes are drawn from the chain re-anchored at the London open (orders unchanged)
REANCHOR = False           # D-136 chain re-anchor on the rebuilt map: OFF (12-map locator: TP 27 -> 23, unfilled 6 -> 13 - it cancels resting winners and replaces the alternative's orders); the zone update itself stays
DAY_CONFIRM = 'start'      # 'start' = the trading day's open (17:00 New York the evening before) | 'london' = the day's London open (02:00 New York)


def _levels(ch, Rr):
    """the Decision-Zone trigger levels of a chain's alternatives: the level Engine 3 gave the alternative's orders (D-109 / D-110), else the alternative's zone (+ its sweep reach)"""
    lv = {}
    for s in Rr['setups']:
        if s.get('alt') and s.get('trigger'):
            lv.setdefault(s['trigger']['dir'], (s['trigger']['level'], s['trigger'].get('zone')))
    for a_ in (ch.get('alts') or ([{'alt': ch.get('alt'), 'chain': ch.get('alt_chain')}] if ch.get('alt_chain') else [])):
        al = a_.get('alt') or {}
        d_, z_ = al.get('dir'), al.get('zone')
        if d_ in ('up', 'down') and d_ not in lv and z_:
            v = z_[1] if d_ == 'up' else z_[0]
            if al.get('reach') is not None:
                v = max(v, al['reach']) if d_ == 'up' else min(v, al['reach'])
            lv[d_] = (v, al.get('decision_zone'))
    return lv


def _new_zones(Xi, have, b0):
    """L-53 'add new zones each day as they form ... without adding a bunch of duplicate garbage': supply / demand candle zones FORMED SINCE the week anchor, sweep zones of the
    week's own daily highs / lows (unswept) and pressure zones the day's map draws - each only where no zone of its family is drawn yet (price overlap)"""
    out = []
    ov = lambda z, q: z['bot'] <= q['top'] and q['bot'] <= z['top']
    for z in Xi.get('sd', []):
        if z.get('origin_time', 0) >= b0 and not any(ov(z, q) for q in have['sd']):
            out.append(('sd', z)); have['sd'].append(z)
    for l in Xi.get('lsz', []):
        q = {'bot': l['bot'], 'top': l['top']}
        if not l.get('swept') and l.get('source', '')[-10:] >= D.ts(b0)[:10] and not any(ov(q, h) for h in have['lsz']):
            out.append(('lsz', dict(l))); have['lsz'].append(q)
    for z in Xi.get('zones', []):
        if z.get('drawn') and not any(ov(z, q) for q in have['ip']):
            out.append(('ip', z)); have['ip'].append(z)
    return out


def _new_zones_pine(pair, monday, adds):
    """the zones added by the daily updates, drawn from the London open that found them; trident_v8 colours (e1_pine)"""
    g = lambda v: ('%.3f' if pair == 'DXY' else '%.5f') % v
    tsR = D.week_end_ms(monday)
    o = []
    for flag, fam in (('show_sd', 'sd'), ('show_lsz', 'lsz'), ('show_ip', 'ip')):
        rows = [(t, day, z) for t, day, f_, z in adds if f_ == fam and (fam != 'sd' or z['tf'] in ('240', '60'))]
        if fam == 'sd':
            rows_ltf = [(t, day, z) for t, day, f_, z in adds if f_ == fam and z['tf'] in ('30', '15')]
        o.append(f'    if {flag}')
        if not rows:
            o.append('        na')
        for t, day, z in rows:
            if fam == 'sd':
                c = '41,98,255' if z['type'] == 'Demand' else '242,54,69'
                o.append(f"        box.new({t}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({c}), 84), border_color=color.rgb({c}), border_width={2 if z['tf'] == '240' else 1}, xloc=xloc.bar_time)")
                txt = f"{z.get('label', z['type'])} | new {day}"
            elif fam == 'lsz':
                o.append(f"        box.new({t}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb(46,139,87), 70), border_color=color.new(color.rgb(63,164,106), 40), border_width=1, xloc=xloc.bar_time)")
                txt = f"LSZ {z.get('source', '')} | new {day}"
            else:
                c = EP.SHADE[z['cat']][z['degree']]
                o.append(f"        box.new({t}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({c}), 70), border_color=color.rgb({c}), border_width=2, xloc=xloc.bar_time)")
                txt = f"{z['name']} | {z['degree']} | new {day}"
            o.append(f"        label.new({t}, {g((z['top'] + z['bot']) / 2)}, \"{txt}\", xloc=xloc.bar_time, style=label.style_none, textcolor=color.new(color.white, 25), size=size.tiny)")
        if fam == 'sd':
            o.append('    if show_ltf')
            if not rows_ltf:
                o.append('        na')
            for t, day, z in rows_ltf:
                c = '41,98,255' if z['type'] == 'Demand' else '242,54,69'
                o.append(f"        box.new({t}, {g(z['top'])}, {tsR}, {g(z['bot'])}, bgcolor=color.new(color.rgb({c}), 90), border_color=color.rgb({c}), border_width=1, xloc=xloc.bar_time)")
    return o


def _day_line(ch, d, monday, t0, t1, price, X):
    """L-51 + L-53: a swing-scalp day's line redrawn from the day's own anchor price, session by session (e2_chain._session_path, P452 6.6 session rules): the first swing goes to the
    bound NEARER that price (P533 2.3 'magnetize toward the IL levels', D-41), the next to the other bound. Other day shapes keep the chain's own path."""
    if not E2.SESSION_PATH or d is None or d.get('shapes') != ['SS'] or not ch.get('range'):
        return None
    lo, hi = min(ch['range']), max(ch['range'])
    if not (lo < hi):
        return None
    first = 'up' if abs(hi - price) < abs(price - lo) else 'down'
    m0 = __import__('datetime').date.fromisoformat(monday)
    n_slots = sum(1 for k in range(5) for a_, b_ in ((E2._ms(m0 + __import__('datetime').timedelta(days=k), 2), E2._ms(m0 + __import__('datetime').timedelta(days=k), 8)),
                                                      (E2._ms(m0 + __import__('datetime').timedelta(days=k), 10), E2._ms(m0 + __import__('datetime').timedelta(days=k), 17))) if b_ > t0 and a_ < t1)
    last = first if n_slots % 2 == 1 else ('down' if first == 'up' else 'up')
    return [(t0, price)] + E2._session_path(X, monday, t0, t1, price, lo, hi, last, None)


def _flow27(pair, kept, live, seg, t_a, t_e, log, f, day, status):
    """LAW 27 TRADE FLOW (E3C 6.2 / 8.21 'TP of trade N = entry of trade N+1', 3-pip tolerance; operator M-61 'The long on Wednesday that hit take profit, that should literally be
    the entry of the short at that exact point'; L-52 one unique trade per observable move). His golden weeks run as ONE flow on every pair: each trade enters at the previous trade's TP.
    On the day's drawn Engine 2 line (the forecast path built at the day's anchor, GS Law 2 'The shape chain PREDICTS which zones price will reach'): when the line reaches an order's
    entry while an OPPOSITE order is running to its TP - after that order's entry, before its TP - and the entry lies INSIDE that move, more than the 3-pip Law-27 tolerance short of its
    TP, the order trades against the move in progress: it is not the next trade of the flow (the next trade enters at that TP) and is not placed (D-144). Rockets ride their parent's move
    and are not judged here. kept = the day's confirmed orders; live = earlier orders still resting / open at the day's anchor. Returns the day's orders that stay."""
    pip = D.PIP[pair]
    pts = sorted(((int(t), float(v)) for t, v in seg), key=lambda p: p[0])

    def hit(price, up, t0, t1):
        """first time in [t0, t1] the line reaches price - from below (up) or from above"""
        for (ta, va), (tb, vb) in zip(pts, pts[1:]):
            if tb < t0 or ta > t1:
                continue
            if ((va >= price - 1e-12) if up else (va <= price + 1e-12)) and ta >= t0:
                return ta
            if ((va < price <= vb) if up else (va > price >= vb)) and vb != va:
                t = ta + (tb - ta) * (price - va) / (vb - va)
                if t0 <= t <= t1:
                    return t
        return None
    prim = [q for q in kept if q.get('category') != 'Reinforcement' and not q.get('alt')]
    tm = {}
    for q in prim + [q for q in live if q not in prim]:
        lg = q['dir'] == 'LONG'
        th = t_a if (q not in prim and status(q) == 'open') else hit(q['entry'], not lg, max(t_a, q['valid_from'], q.get('day_anchor') or 0), min(t_e, q['valid_to']))
        tt = hit(q['tp'], lg, th, t_e) if th is not None else None
        tm[id(q)] = (th, tt)
    drop = []
    for b in prim:
        tb = tm[id(b)][0]
        if tb is None:
            continue
        for a in prim + [q for q in live if q not in prim]:
            ta, tt = tm[id(a)]
            if a is b or a['dir'] == b['dir'] or ta is None or tt is None or a in drop or not (ta < tb < tt):
                continue
            inside = (a['entry'] < b['entry'] < a['tp']) if a['dir'] == 'LONG' else (a['tp'] < b['entry'] < a['entry'])
            if inside and abs(a['tp'] - b['entry']) > 3 * pip + 1e-12:
                drop.append(b)
                log.append(f"{day} {b['shape']} {b['dir']} {f(b['entry'])}: NOT IN THE TRADE FLOW - the {day} line reaches it {D.ts(int(tb))} UTC while {a['shape']} {a['dir']} {f(a['entry'])} runs to its TP "
                           f"{f(a['tp'])} ({abs(a['tp'] - b['entry']) / pip:.1f} pips short of it; Law 27 'TP of trade N = entry of trade N+1', E3C 6.2 / 8.21)")
                break
    return [q for q in kept if q not in drop and not (q.get('parent_ref') is not None and q['parent_ref'] in drop)]


def _micro_day(pair, monday, i, t_a, t_L, t_e, op, ch, d, X, carry=None):
    """M-70 EXAMPLE (plan memory/17 steps 2-5; switch E2.E2_MICRO, default OFF; drawing only): the day's DRAWN line. Asia (trading-day open -> London open) holds the open price
    (P452 6.6 rule 1 'price stays within the prior day's range'); London + NY are built AT THE LONDON OPEN from bars closed by then (the L-53 anchor; P452 rule 2 reads the Asian
    session): a swing-scalp day walks the Engine 1 zones on the session clock (E2.micro_ss); any other day keeps the chain's own legs, on the trigger clock (E2.micro_clock).
    carry = (arrival, target) of a breakout leg drawn the day before (plan step 1): the Asian session extends it (P452 6.6 rule 6 'if a shape is active at the close of Day N ...
    Day N+1 opens with that shape continuing. The Asian session of Day N+1 typically extends or consolidates the Day N move'). Returns (segments, audit text)."""
    import datetime as _dt
    date = _dt.date.fromisoformat(monday) + _dt.timedelta(days=i)
    out = [[(t_a, op), (t_L, op)]] if i > 0 and t_L > t_a else []
    if out and carry is not None and carry[0] > t_a:
        out = [_cut([(t_a, op), (carry[0], carry[1])], t_a, t_L)]
    pL = X['spot']
    if d is not None and d.get('shapes') == ['SS'] and ch.get('range'):
        f_e, c_e = min(ch['range']), max(ch['range'])
        cap_u = E2.micro_turn(pair, X, ch.get('ceil'), True) or c_e
        cap_d = E2.micro_turn(pair, X, ch.get('floor'), False) or f_e
        cap_u, cap_d = min(cap_u, d['hi']), max(cap_d, d['lo'])
        if 3 in E2.MICRO_STEPS:                                 # GS Law 2 'The day's shape decides which zones are reachable (SS <= 30 pips from spot ...)' (plan step 3)
            cap_u, cap_d = min(cap_u, pL + 0.30 * X['U']), max(cap_d, pL - 0.30 * X['U'])
        nearer = 'up' if abs(cap_u - pL) < abs(pL - cap_d) else 'down'
        if 4 in E2.MICRO_STEPS:
            since = t_a if i > 0 else D.week_start_ms(monday)
            first, why = _asof(monday, t_L, lambda: E2.micro_bias(pair, monday, since, nearer))
        else:
            first, why = nearer, 'toward the nearer bound (D-41; step 4 off)'
        pts, txt = E2.micro_ss(pair, X, date, t_L, t_e, pL, first, cap_u, cap_d)
        txt = f"first leg {first}: {why}; " + txt
    else:
        rest = _cut(ch['path'], t_L, t_e)
        if len(rest) < 2:
            return out, 'no chain leg this day'
        pts = [(t_L, pL)] + rest[1:]
        if 2 in E2.MICRO_STEPS:
            pts = E2.micro_clock(pair, monday, ch, pts, date)
        txt = f"{'+'.join(d['shapes']) if d else '-'}: the chain's legs from the London-open price" + (' on the trigger clock (10:01 release, NY swing time)' if 2 in E2.MICRO_STEPS else '')
    out.append(pts)
    return out, txt


def daily_anchor(pair, monday, chain, R, src_days=None):
    """DAILY ANCHORING (L-47 / L-53; D-131, D-132, D-134, D-136). The Monday map and chain hold while they hold. Every trading day:
    at its TRADING-DAY OPEN (17:00 New York the evening before; the day's orders rest through the Asian session), with only bars closed by then:
      - a 1H close beyond a Decision Zone of the chain in force since its anchor = the chain failed (6.6 Step 4): its alternative is the chain until the next London open;
      - the day's line restarts from that moment's price; each order of the day is CONFIRMED (order block not closed through - one-time use; price on the order's side) or dropped;
        an order still resting / open is not copied (L-52) - it keeps resting;
    at its LONDON OPEN (02:00 New York), with only bars closed by then (L-53 'synchronously re-update the zones at the beginning of London session each successive day'):
      - the map is rebuilt; zones formed since the week anchor are added (no duplicates of drawn zones);
      - a failed chain is RE-ANCHORED on the rebuilt map (Engine 2 + 3 as of the London open): its line, its day boxes and its orders from then on; the failed chain's pending
        orders of the day are cancelled there."""
    DAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')
    f = (lambda v: '%.3f' % v) if pair == 'DXY' else (lambda v: '%.5f' % v)
    import e3_trades as E3
    b0 = D.boundary_ms(monday)
    segs, alt_segs, audit, keep, log, parts, partsL, days, adds = [], [], list(chain['audit']), [], list(R['log']), {}, {}, [], []
    X0 = _map(pair, monday)
    have = {'sd': list(X0.get('sd', [])), 'lsz': [{'bot': l['bot'], 'top': l['top']} for l in X0.get('lsz', []) if not l.get('swept')],
            'ip': [z for z in X0.get('zones', []) if z.get('drawn')]}
    cur = {'chain': chain, 'R': R, 'anchor': b0, 'lvl': _levels(chain, R), 'active': None}
    vw = None          # D-138: the chain the LINE and DAY BOXES are drawn from once the chain in force has failed - re-anchored at a London open on the rebuilt map
    micro, mst = E2.E2_MICRO, {'switched': False, 'X_prev': X0}      # M-70 example (memory/17): the drawn line built by _micro_day - drawing only

    def alts_of(ch):
        return [a_ for a_ in (ch.get('alts') or ([{'alt': ch.get('alt'), 'chain': ch.get('alt_chain')}] if ch.get('alt_chain') else [])) if a_.get('alt') and a_.get('chain')]

    def confirm(s, i, t_a, op, since):
        """None = confirmed, else the reason it is not"""
        if s.get('alt') or i == 0:
            return None
        if s.get('category') == 'Reinforcement':
            # a rocket stands AHEAD of price in the move's direction (FA 8 trip-wire: 'trigger zone 2-4 zones ahead'; GS Law 6 'rockets at the next MoM zones'): a rung the move has
            # already passed by the day's anchor is not a new order of that day (D-141; M-61 GBPUSD: the Thursday ladder long stood 47 pips under Thursday's open)
            if (op >= s['entry']) if s['dir'] == 'LONG' else (op <= s['entry']):
                return f"the move already passed this rung (price {f(op)} beyond the rocket entry {f(s['entry'])}) - rockets stand ahead of price"
            return None
        z = s.get('anchor') or {}
        sd = 'bot' in z and 'top' in z and (z.get('src') == 'SD' or ('tf' in z and not z.get('liq')))     # an order block (supply / demand candle zone): one-time use
        brk = next((x for x in since if ((x['close'] < z['bot']) if s['dir'] == 'LONG' else (x['close'] > z['top']))), None) if sd else None
        if brk is not None:
            return f"anchor zone {f(z['bot'])}-{f(z['top'])} closed through {D.ts(brk['time'] + 3600000)} UTC (one-time use)"
        if (op <= s['entry']) if s['dir'] == 'LONG' else (op >= s['entry']):
            return f"the price at the anchor {f(op)} already on the far side of the entry {f(s['entry'])}"
        return None

    for i in range(5):
        t_a = b0 if i == 0 else (D.week_start_ms(monday) + i * 86400000 if DAY_CONFIRM == 'start' else D.day_anchor_ms(monday, i))
        t_L, t_e = D.day_anchor_ms(monday, i), D.week_start_ms(monday) + (i + 1) * 86400000
        b1 = D.closed_until(pair, '60', t_a)
        op = b1[-1]['close']
        since = [x for x in b1 if x['time'] >= b0]
        # ---- trading-day open: has the chain in force failed at a Decision Zone? (6.6 Step 4) -> its alternative is the chain
        if i > 0 and cur['active'] is None:
            for a_ in alts_of(cur['chain']):
                d_ = a_['alt']['dir']
                lv = cur['lvl'].get(d_)
                brk = next((x for x in b1 if x['time'] >= cur['anchor'] and ((x['close'] > lv[0]) if d_ == 'up' else (x['close'] < lv[0]))), None) if lv else None
                if brk is not None:
                    cur['active'] = dict(a_, level=lv[0], at=brk['time'] + 3600000)
                    audit.append(f"ALTERNATIVE CHAIN ACTIVE from the {DAYS[i]} trading-day open (6.6 Step 4): 1H close {'above' if d_ == 'up' else 'below'} {f(lv[0])} ({a_['alt'].get('decision_zone', '')}) "
                                 f"at {D.ts(cur['active']['at'])} UTC: " + ' -> '.join(c['shape'] for c in a_['chain'].get('chain', [])))
                    break
        view = vw['chain'] if vw is not None else (cur['active']['chain'] if cur['active'] else cur['chain'])
        d = next((x for x in view.get('days', []) if x['day'] == DAYS[i]), None) or next((x for x in chain['days'] if x['day'] == DAYS[i]), None)
        if d is not None:
            days.append(d)
        seg = _cut(view['path'], t_a, t_e)
        if i > 0 and len(seg) > 1:
            seg[0] = (t_a, op)
        if i > 0:
            dl = _day_line(view, d, monday, t_a, t_e, op, X0)
            if dl:
                seg = dl
            elif E2.SESSION_PATH and len(seg) > 1:
                # P452 6.6 rules 1 / 6: the Asian session holds the day's open price ('extends or consolidates the Day N move'); the chain's own legs run from the London open
                rest = _cut(view['path'], t_L, t_e)
                seg = [(t_a, op), (t_L, op)] + rest[1:] if len(rest) > 1 else seg
        if cur['active'] is None and view.get('alt_chain'):
            q = _cut(view['alt_chain']['path'], t_a, t_e)
            if i > 0 and len(q) > 1:
                q[0] = (t_a, op)
            if len(q) > 1:
                alt_segs.append(q)
        if i > 0:
            audit.append(f"DAILY ANCHOR {DAYS[i]} trading-day open {D.ts(t_a)} UTC: price {f(op)}")
        kept, dropped = [], []
        if i > 0 and d is not None and d.get('shapes') == ['SS']:
            # L-52: a swing-scalp order not yet filled keeps resting into the next day of the range - one order until it fills - re-checked at this day's anchor
            # (order block not closed through, price on its side); the copies Engine 3 makes for the day are then the same trade (dropped below)
            for q in keep:
                if q.get('shape') == 'SS' and not q.get('alt') and q.get('category') != 'Reinforcement' and q['valid_to'] >= t_a - 1 and q['valid_to'] < t_e \
                        and _status(q, max(q['valid_from'], q.get('day_anchor') or 0), t_a, pair) == 'pending' and confirm(q, i, t_a, op, since) is None:
                    q['valid_to'] = t_e
                    q['t1'] = max(q.get('t1') or 0, t_e)
        for s in [x for x in cur['R']['setups'] if (x.get('rest_from') or x['day']) == DAYS[i]]:
            why = None
            if cur['active'] is not None and s.get('category') != 'Reinforcement':
                if s.get('alt') and s.get('trigger') and s['trigger']['dir'] == cur['active']['alt']['dir']:
                    s['alt'] = False
                    s['why'] = f"ALTERNATIVE chain ACTIVE since {D.ts(cur['active']['at'])} UTC: " + s['why'].split(': ', 1)[-1]
                    s.pop('trigger', None)
                elif s.get('alt'):
                    why = 'an alternative of another Decision Zone'
                else:
                    why = f"the chain failed at its Decision Zone ({D.ts(cur['active']['at'])} UTC) - its alternative is active"
            if why is None and s.get('clone'):
                live = next((q for q in reversed(keep) if q.get('dir') == s['dir'] and abs(q['entry'] - s['entry']) < 1e-9 and q.get('category') == s.get('category')), None)
                if live is not None and _status(live, max(live['valid_from'], live.get('day_anchor') or 0), t_a, pair) in ('pending', 'open'):
                    live['valid_to'] = max(live['valid_to'], t_e)
                    live['t1'] = max(live.get('t1') or 0, t_e)
                    dropped.append(s)
                    log.append(f"{DAYS[i]} {s['id']} {s['dir']} {f(s['entry'])}: NOT A NEW TRADE - {live['id']} still resting / open: it keeps resting (L-52)")
                    continue
                if PHASE10_REENTRY and src_days is not None and pair != 'DXY':
                    # Phase 10 (E3C:723-770) 'For each DXY source setup, generate the corresponding EU mirror setup' + L-52: a re-entry on a receiving pair is a new setup -
                    # it needs its source pair to have CONFIRMED the matching order at this same day's anchor (DXY -> EU inverse, EU -> GU kept) (D-142)
                    want = ({'LONG': 'SHORT', 'SHORT': 'LONG'}[s['dir']] if pair == 'EURUSD' else s['dir'])
                    if (s['shape'], want) not in src_days.get(i, set()):
                        dropped.append(s)
                        log.append(f"{DAYS[i]} {s['id']} {s['dir']} {f(s['entry'])}: NOT A NEW TRADE - no {DAYS[i]} {s['shape']} {want} order on the source pair to mirror (Phase 10)")
                        continue
                s['clone'] = False
                s.pop('origin', None)
            why = why or confirm(s, i, t_a, op, since)
            if why is None and s.get('parent_ref') is not None and s['parent_ref'] not in kept and s['parent_ref'] not in keep:
                why = 'its parent was not confirmed'
            if why:
                dropped.append(s)
                log.append(f"{DAYS[i]} {s['id']} {s['dir']} {f(s['entry'])}: NOT CONFIRMED at {D.ts(t_a)} UTC - {why}")
            else:
                if i > 0:
                    s['day_anchor'] = t_a
                kept.append(s)
        if FLOW27 and len(seg) > 1:
            # D-144: judged on THIS day's line only (built at the trading-day open from bars closed by then) against the orders of the day and those still resting / open at its anchor
            live_ = [q for q in keep if q.get('category') != 'Reinforcement' and not q.get('alt') and q['valid_to'] > t_a
                     and _status(q, max(q['valid_from'], q.get('day_anchor') or 0), t_a, pair) in ('pending', 'open')]
            kept = _flow27(pair, kept, live_, seg, t_a, t_e, log, f, DAYS[i], lambda q: _status(q, max(q['valid_from'], q.get('day_anchor') or 0), t_a, pair))
        keep += kept
        parts[i] = {'open': op, 'active': None if cur['active'] is None else (cur['active']['alt']['dir'], cur['active']['level'], cur['active']['at']),
                    'orders': [(s['dir'], s['entry'], s['sl'], s['tp']) for s in kept], 'dropped': len(dropped), 'seg0': seg[:1],
                    # D-142: the Phase 10 record of the day - (shape, direction) of the primary orders confirmed at this anchor; every DXY order, on EUR/USD its active mirrors (as e3_trades.build)
                    'keys': sorted({(s['shape'], s['dir']) for s in kept if not s.get('alt') and s.get('category') != 'Reinforcement' and (pair == 'DXY' or s.get('cascade'))})}
        # ---- London open (L-53): the rebuilt map adds the zones formed since the week anchor; a failed chain is re-anchored on it
        if i > 0:
            Xi = _map_at(pair, monday, t_L)
            new = _new_zones(Xi, have, b0)
            adds += [(t_L, DAYS[i], fam, z) for fam, z in new]
            if new:
                audit.append(f"DAILY ZONE UPDATE {DAYS[i]} London open {D.ts(t_L)} UTC (L-53): " + '; '.join(f"{fam} {f(z['bot'])}-{f(z['top'])}" for fam, z in new))
            reanch = None
            if cur['active'] is not None and REANCHOR:
                ch_i, R_i = _engines_at(pair, monday, t_L)
                opL = Xi['spot']
                for s in kept:                                   # the failed chain's orders of the day not yet filled are cancelled at the re-anchor
                    if s.get('category') != 'Reinforcement' and _status(s, max(s['valid_from'], s.get('day_anchor') or 0), t_L, pair) == 'pending':
                        s['valid_to'] = s['t1'] = max(t_L, s['valid_from'])
                        log.append(f"{DAYS[i]} {s['id']} {s['dir']} {f(s['entry'])}: CANCELLED at the {DAYS[i]} London open - the chain is re-anchored")
                audit.append(f"CHAIN RE-ANCHORED at the {DAYS[i]} London open {D.ts(t_L)} UTC on the rebuilt map (D-136), price {f(opL)}: " + ' -> '.join(c['shape'] for c in ch_i.get('chain', [])))
                audit += ['  ' + a for a in ch_i['audit'] if not a.startswith('Primary Timeframe')]
                log += [f"{DAYS[i]} re-anchored run: {l}" for l in R_i['log']]
                cur = {'chain': ch_i, 'R': R_i, 'anchor': t_L, 'lvl': _levels(ch_i, R_i), 'active': None}
                d2 = next((x for x in ch_i.get('days', []) if x['day'] == DAYS[i]), None)
                if d2 is not None:
                    days[-1:] = [d2] if (days and days[-1]['day'] == DAYS[i]) else days[-1:] + [d2]
                seg = _cut(seg, t_a, t_L) if len(seg) > 1 else seg
                seg2 = _day_line(ch_i, d2, monday, t_L, t_e, opL, X0) or _cut(ch_i['path'], t_L, t_e)
                if len(seg2) > 1:
                    segs.append(seg2)
                newk = []
                for s in [x for x in R_i['setups'] if (x.get('rest_from') or x['day']) == DAYS[i] and not x.get('clone')]:
                    why = confirm(s, i, t_L, opL, [x for x in D.closed_until(pair, '60', t_L) if x['time'] >= b0])
                    if why is None and s.get('parent_ref') is not None and s['parent_ref'] not in newk:
                        why = 'its parent was not confirmed'
                    if why:
                        log.append(f"{DAYS[i]} {s['id']} {s['dir']} {f(s['entry'])}: NOT CONFIRMED at the re-anchor {D.ts(t_L)} UTC - {why}")
                    else:
                        s['day_anchor'] = t_L
                        s['valid_from'] = max(s['valid_from'], t_L)
                        newk.append(s)
                keep += newk
                reanch = (t_L, [(s['dir'], s['entry'], s['sl'], s['tp']) for s in newk])
            elif REANCHOR_DRAW and (cur['active'] is not None or vw is not None):
                # D-138: the LINE and the DAY BOXES follow the market once the chain in force has failed (L-51 'if the candles don't match the exact lines that you're drawing,
                # then your lines are not as accurate as they should be'; L-53 daily update at London open): the chain is re-anchored on the rebuilt map for the drawing - again
                # whenever the drawn chain fails at its own Decision Zone; the ORDERS stay with the chain in force (its alternative), none cancelled (D-137: re-anchored orders cost winners)
                failed_vw = False
                if vw is not None:
                    bL = [x for x in D.closed_until(pair, '60', t_L) if x['time'] >= vw['anchor']]
                    failed_vw = any(next((x for x in bL if ((x['close'] > lv[0]) if d_ == 'up' else (x['close'] < lv[0]))), None) is not None for d_, lv in vw['lvl'].items())
                if vw is None or failed_vw:
                    ch_i, R_i = _engines_at(pair, monday, t_L)
                    vw = {'chain': ch_i, 'anchor': t_L, 'lvl': _levels(ch_i, R_i)}
                    audit.append(f"LINE RE-ANCHORED at the {DAYS[i]} London open {D.ts(t_L)} UTC on the rebuilt map (D-138): " + ' -> '.join(c['shape'] for c in ch_i.get('chain', [])))
                    reanch = (t_L, 'draw')
                d2 = next((x for x in vw['chain'].get('days', []) if x['day'] == DAYS[i]), None)
                if d2 is not None:
                    days[-1:] = [d2] if (days and days[-1]['day'] == DAYS[i]) else days[-1:] + [d2]
                seg = _cut(seg, t_a, t_L) if len(seg) > 1 else seg
                seg2 = _day_line(vw['chain'], d2, monday, t_L, t_e, Xi['spot'], X0) or _cut(vw['chain']['path'], t_L, t_e)
                if len(seg2) > 1 and not micro:
                    if seg2[0][0] == t_L:
                        seg2[0] = (t_L, Xi['spot'])
                    segs.append(seg2)
            partsL[i] = {'adds': [(fam, round(z['bot'], 6), round(z['top'], 6)) for fam, z in new], 'reanchor': reanch}
        if micro:
            # M-70 example (plan memory/17): the day's drawn line - Asia at the trading-day open price, London + NY built at the London open (_micro_day); the orders above are untouched
            XL = X0 if i == 0 else Xi
            dL = days[-1] if (days and days[-1]['day'] == DAYS[i]) else d
            ms, txt = _micro_day(pair, monday, i, t_a, t_L, t_e, op, vw['chain'] if vw is not None else view, dL, XL, mst.get('carry'))
            mst['carry'] = None
            if 1 in E2.MICRO_STEPS and cur['active'] is None and not mst['switched'] and cur['lvl']:
                # plan step 1 (6.6 Step 4, P533:1895): the alternative takes over the drawn line AT THE 30m CANDLE that closes beyond the Decision Zone - not at the next day's open
                hit = next(((x['time'] + 1800000, x['close'], d_) for x in D.closed_until(pair, '30', t_e) if x['time'] + 1800000 > max(t_a, cur['anchor'])
                            for d_, lv in cur['lvl'].items() if ((x['close'] > lv[0]) if d_ == 'up' else (x['close'] < lv[0]))), None)
                a_ = next((a for a in alts_of(cur['chain']) if hit is not None and a['alt']['dir'] == hit[2]), None)
                if a_ is not None:
                    tc, c, d_ = hit
                    tgt, shp = E2.micro_target(a_['chain'], d_, c)
                    if tgt is not None:                             # GS Law 2: BS / RWL reach 100 pips
                        tgt = min(tgt, c + XL['U']) if d_ == 'up' else max(tgt, c - XL['U'])
                    pE, zE, whyE = E2.micro_walk(pair, XL if tc >= t_L else mst['X_prev'], c, d_ == 'up', tgt)
                    T_arr = max(E2.micro_arrival(tc, E2.BS_SESSIONS), tc + 1)
                    leg = [(tc, c), (T_arr, pE)]
                    ms = [q for q in (_cut(s, s[0][0], tc) for s in ms if s and s[0][0] < tc) if len(q) > 1] + [_cut(leg, tc, max(t_e, tc + 1))]
                    mst['switched'], mst['carry'] = True, ((T_arr, pE) if T_arr > t_e else None)
                    if days and days[-1]['day'] == DAYS[i]:
                        # the day's forecast box ends at the breaking candle; the alternative's shape gets its own box from that candle (nothing drawn before it uses it)
                        q = days[-1]
                        days[-1] = dict(q, t1=max(q['t0'] + 1, tc))
                        p_e = ms[-1][-1][1]
                        days.append(dict(q, shapes=[shp], dir=d_, lo=min(c, p_e), hi=max(c, p_e), t0=tc, t1=max(t_e, tc + 1), conf=a_['alt'].get('conf') or q['conf'],
                                         key=a_['alt'].get('decision_zone') or q.get('key', '-')))
                    txt += (f" | DECISION ZONE BROKEN: 30m close {f(c)} at {D.ts(tc)} UTC beyond {f(cur['lvl'][d_][0])} ({cur['lvl'][d_][1]}) -> the alternative {shp} {d_} draws the line "
                            f"from that candle toward {f(pE)}, arriving {D.ts(T_arr)} UTC (6.8 BS 1-3 sessions) ({(zE.get('label') or zE.get('name')) if zE else ('its target' if tgt is not None else 'the BS reach')}: {whyE})")
            segs += [s for s in ms if len(s) > 1]
            audit.append(f"MICRO {DAYS[i]} (E2_MICRO example, drawing only): {txt}")
            mst['X_prev'] = XL
        elif len(seg) > 1:
            segs.append(seg)
    keep = [s for s in keep if s.get('parent_ref') is None or s['parent_ref'] in keep]
    trades = [q for q in keep if q.get('category') != 'Reinforcement' and not q.get('alt')]
    if len(trades) > E3.MAX_SETUPS:                               # L-04 / R-07: at most 11 trades a week - the latest days' weakest go first (as e3_trades.build)
        raw = lambda q: sum(v for _, v in (q.get('conf_parts') or []))
        for q in sorted(trades, key=lambda q: (-E3.DAY_IDX[q['day']], q.get('confidence', 0), raw(q)))[:len(trades) - E3.MAX_SETUPS]:
            keep = [x for x in keep if x is not q and x.get('parent_ref') is not q]
            log.append(f"{q['day']} {q['shape']} {q['dir']} {q['entry']:.5f}: EMISSION_CAPPED - more than {E3.MAX_SETUPS} trades this week (L-04)")
    pfx = {'DXY': 'DX', 'EURUSD': 'EU', 'GBPUSD': 'GB'}[pair]     # one numbering for the week: every order a unique trade (L-52)
    keep.sort(key=lambda q: (E3.DAY_IDX[q['day']], q.get('day_anchor') or 0, 0 if q.get('parent_ref') is None else 1))
    n, na = 0, {}
    for q in keep:
        if q.get('alt'):
            tg = q['id'][2] if len(q['id']) > 2 and q['id'][2].isalpha() else 'A'
            na[tg] = na.get(tg, 0) + 1
            q['id'] = f"{pfx}{tg}{na[tg]}"
        else:
            n += 1
            q['id'] = f"{pfx}{n}"
    for q in keep:
        if q.get('parent_ref') is not None:
            q['parent'] = q['parent_ref']['id']
    # D-141: an alternative chain's order is a CONTINGENCY until its Decision Zone breaks (6.6 Step 4; 7S.2 'Map the SS->BS Transition Setup as a contingency') - once the alternative
    # is activated at a day's anchor its orders are drawn as live orders (D-132); a dormant contingency is not drawn as a position (it is not a trade - L-52 'one trade = one instance where
    # price hits the entry and then the take-profit'; M-61: the dormant alternative ladder long drawn on Thursday read as the week's Thursday trade) - it stays in the report
    cont = [q for q in keep if q.get('alt')]
    keep = [q for q in keep if not q.get('alt') and not (q.get('parent_ref') is not None and q['parent_ref'].get('alt'))]
    for q in cont:
        tr = q.get('trigger') or {}
        log.append(f"CONTINGENCY {q['id']} {q['day']} {q['shape']} {q['dir']} E {f(q['entry'])} SL {f(q['sl'])} TP {f(q['tp'])} - live only after a 1H close "
                   f"{'above' if tr.get('dir') == 'up' else 'below'} {f(tr['level']) if tr.get('level') is not None else '-'} ({tr.get('zone', '')}); not drawn unless activated")
    out = dict(chain)
    out.update(days=days, segments=segs, alt_segments=alt_segs, audit=audit, daily=parts, daily_L=partsL, n_real=len(days), zone_adds=adds)
    R2 = dict(R)
    R2.update(setups=keep, log=log, contingent=cont)
    return out, R2


def run(pair, monday, daily=False):
    X = _map(pair, monday)
    XD = _map('DXY', monday) if pair != 'DXY' else None
    chain, setups = engines(pair, monday, X, XD)
    if daily:
        src_days = _src_days('DXY' if pair == 'EURUSD' else 'EURUSD', monday) if pair != 'DXY' else None
        chain, setups = daily_anchor(pair, monday, chain, setups, src_days)
    # the day tags of Engine 2 as label extents (same placement as e2_chain.pine: one row above the envelope, odd days one row higher when a tag is composite; two text lines each;
    # Pinebox draws the text from the label's point to the right, 1.65 one-hour bars per character) - Engine 3's labels keep clear of them
    import e3_trades as E3
    if chain.get('days'):
        y_t = max(d['hi'] for d in chain['days']); lo_t = min(d['lo'] for d in chain['days'])
        y_t += 0.06 * (y_t - lo_t) + 1e-9
        sp_t = y_t - lo_t
        comp = any(len(x['shapes']) > 1 for x in chain['days'])
        setups['avoid'] = []
        for k_, d in enumerate(chain['days']):
            y_d = y_t + (0.09 * sp_t if (k_ % 2 and comp) else 0.0)
            x_d = (d['t0'] + d['t1']) // 2 if d['day'] != 'Fri' else d['t0'] + (d['t1'] - d['t0']) // 4
            w_d = int(1.65 * len(f"{d['day']} {'+'.join(d['shapes'])}") * 3600000)
            setups['avoid'] += [(x_d, w_d, y_d), (x_d, w_d, y_d - 0.05 * sp_t)]
    extra = (_new_zones_pine(pair, monday, chain['zone_adds']) if chain.get('zone_adds') else []) + E2.pine(pair, monday, chain) + (E3.pine(pair, monday, setups) if E3 else []) + table(pair, monday, X, chain, setups)
    # the zones Engine 2 designates (bounds, pivot, targets, the from / to zone of every chain step): a V1 liquidity band among them is drawn by the tool even when it stands alone (D-107)
    des = [chain.get(k) for k in ('ceil', 'floor', 'pivot', 'target', 'target2', 'far_liq', 'near', 'far')] + [st.get(k) for st in chain['chain'] for k in ('frm', 'to')]
    X['e2_zones'] = [(z['bot'], z['top']) for z in des if isinstance(z, dict) and 'bot' in z]
    edges = [d[k] for d in chain['days'] for k in ('lo', 'hi')] + [q['entry'] for q in setups['setups']]      # ... and a band a day box ends on / a setup's entry stands on
    X['e2_zones'] += [(b['bot'], b['top']) for b in X['v1']['240']['liquidity'] if any(b['bot'] - 1e-9 <= e <= b['top'] + 1e-9 for e in edges)]
    src = EP.generate(pair, monday, X, extra, EP.reach(X, chain), pre=(E3.pine_state(pair, monday, setups) if E3 else []))
    return X, chain, setups, src + '\n' + '\n'.join('// ' + l for l in e2_report(pair, monday, chain) + [''] + report(pair, monday, X, chain, setups)) + '\n'


FAMILY = {'SS': 'SS', 'RWL': 'SS', 'PRWL': 'SS', 'STORM': 'SS', 'BS': 'BS', 'PBS': 'BS', 'R': 'R', 'WL': 'WL', 'WLS': 'WL', 'PWL': 'WL'}
MASTER = ['SS', 'BS', 'R', 'WL']


def divergence(core, own):
    """E3C 10.7 'The 35% Divergence Rule (FLAG ONLY - never override)': per day, the DXY chain's shape family against the pair's OWN chain (the pair's bounds read without the DXY lead):
    'Shape-family alignment (SS~SS/RWL/STORM/PRWL; BS~BS/PBS; R; WL~WL/WLS/PWL) OR +-1 step on master SS->BS->R->WL; divergence = (5-aligned)/5; missing day = not-aligned;
    <= 0.35 -> VALIDATED else -> DIVERGED, flag only'. The DXY translation stays the pair's chain (P533 9.13 'Do NOT override the DXY direction')."""
    cd = {d['day']: d for d in core.get('days', [])}; od = {d['day']: d for d in own.get('days', [])}
    aligned, rows = 0, []
    for day in ('Mon', 'Tue', 'Wed', 'Thu', 'Fri'):
        a, b = cd.get(day), od.get(day)
        ok = False
        if a and b:
            fa, fb = {FAMILY.get(x, x) for x in a['shapes']}, {FAMILY.get(x, x) for x in b['shapes']}
            ok = bool(fa & fb) or any(abs(MASTER.index(x) - MASTER.index(y)) <= 1 for x in fa for y in fb if x in MASTER and y in MASTER)
        aligned += ok
        rows.append(f"{day} {'+'.join(a['shapes']) if a else '-'} / {'+'.join(b['shapes']) if b else '-'}{'' if ok else ' (not aligned)'}")
    dv = (5 - aligned) / 5
    return {'value': dv, 'state': 'VALIDATED' if dv <= 0.35 else 'DIVERGED', 'rows': rows, 'own_dir': own.get('bdir')}


CASCADE = {'DXY': 'native', 'EURUSD': 'DXY->EU', 'GBPUSD': 'EU->GU'}
SES_UTC = {'London Open': '06:00-09:00', 'London/NY Overlap': '12:00-14:00', 'NY Open': '12:30-14:00', 'NY Mid': '14:00-18:00'}      # GS Part 10 session clock (ET) in UTC, EDT weeks


def e2_report(pair, monday, chain):
    """P533 6.9 'Engine 2 Output Format (Report Section 17) ... MUST include all of the following components': the audit trail of the chain as Engine 2 wrote it (current shape, bounds,
    4H validation, direction, timing, every extension with its trigger, alternative chains, consolidation phase), the day-by-day decomposition in the canon's line format ('the DIRECT INPUT
    to Engine 3's Day-Level Bridge') and the weekly chain line. Carried in the Pine as comments, in front of the Engine 3 report (6.7 RULE 2 'No Chain Without Audit Trail') (D-126)."""
    o = [f"ENGINE 2 - MACRO SHAPE CHAIN MAP | WEEK OF {monday} | {PNAME[pair]}"]
    o += [a for a in chain.get('audit', [])]
    P = E2.protocols(monday)
    if P is not None:                                     # P533 Part V item 14 'Volatility Trigger Summary' (Protocols D / E / F / G, P452:1443-1446), as of the anchor
        o.append('--- VOLATILITY TRIGGERS (as of the anchor) ---')
        for n in P['D']['latest_notes']:
            o.append(f"Protocol D {n['term']} note: " + (f"{n['close_et']} ET bid-to-cover {n['bid_to_cover']:.2f}" + (' >= 2.6x -> VOLATILITY TRIGGER' if n['trigger'] else '') if 'bid_to_cover' in n else n.get('status', 'NO DATA')))
        o.append('Protocol D auctions this week: ' + ('; '.join(f"{a['close_et']} ET {a['type']} {a.get('original_term') or a['term']}" for a in P['D']['week_auctions']) or 'none announced'))
        g = P['G']['latest']
        o.append('Protocol G EIA crude: ' + (f"week ending {g['week_ending']} change {g['change_mb']:+.3f}M vs previous {g['previous_change_mb']:+.3f}M, deviation {g['deviation_mb']:+.3f}M"
                                             + (' >= 5M -> VOLATILITY TRIGGER' if g['trigger'] else '') if isinstance(g, dict) else str(g)) + f" | this week's release {P['G']['week_release']['release_et']} ET")
        e_ = P['E']
        o.append('Protocol E ON RRP: ' + (f"{e_['current']['date']} accepted USD {e_['current']['accepted_bn']:.3f}bn vs {e_['previous']['date']} USD {e_['previous']['accepted_bn']:.3f}bn, change {e_['change_bn']:+.3f}bn"
                                           + (' - contraction >= USD 50bn -> VOLATILITY TRIGGER' if e_['trigger'] else '') if e_.get('status') == 'OK' else e_.get('status', 'NO DATA'))
                 + ' | Protocol F red folder: ' + P['F']['status'])
    o.append('--- DAY-BY-DAY DECOMPOSITION ---')
    for d in chain.get('days', []):
        o.append(f"{d['day']}: {' + '.join(d['shapes'])} {d['dir']} | Key Zone: {d['key']} | Triggers: {'; '.join(d['triggers'])} | Confidence: {int(round(d['conf'] * 100))}%")
    o.append('--- WEEKLY SHAPE CHAIN VISUALIZATION ---')
    o.append(f"{PNAME[pair]}: " + ' -> '.join(f"{d['day']}: {' + '.join(d['shapes'])} {d['dir']}" for d in chain.get('days', [])))
    return o


def report(pair, monday, X, chain, R):
    """E3C 8.13 'The E3 Output Format (FULL)' + Phase 8 label law (BE1-BE12): weekly execution calendar (every day covered or 'No qualifying setups - [reason]'), the setups by category with
    DAY / SESSION WINDOW / SHAPE TRIGGER / SETUP CATEGORY / ANCHOR HIT WINDOW (the E2-designated session bracket of the setup's day, R3 law), parent reference on reinforcements (BE9),
    daily session notes with the day's catalysts (BE8), the profit-taking law (BE11), every discard with its reason (Phase 12), weekly stats with the f(T) acceptance line (E3C:996).
    Carried at the end of the Pine as comments: one command -> one file."""
    f = (lambda v: '%.3f' % v) if pair == 'DXY' else (lambda v: '%.5f' % v)
    S = [s for s in R.get('setups', []) if not s.get('clone')]
    rep = {}
    for s in R.get('setups', []):
        if s.get('clone'):
            rep.setdefault(s['origin']['id'], []).append(s['day'])
    days = chain.get('days', [])
    name = lambda a: (a.get('label') or a.get('name') or 'liquidity rung')
    cls = lambda a: (a.get('kind') or (a.get('mech') or {}).get('bom') or ('LSZ' if (a.get('sweep') or a.get('lsz')) else 'LQZ' if (a.get('liq') or 'tf' not in a) else 'IP'))
    o = [f"ENGINE 3 - FULL-SPECTRUM TRADE MAP | WEEK OF {monday} | {PNAME[pair]}", '',
         '=== WEEKLY EXECUTION CALENDAR ===', 'Day | Pair | Dir | Setup Type | Entry | Shape | Session | Conf | Notes']
    for d in days:
        rows = [s for s in S if s['day'] == d['day']]
        for s in rows:
            note = (f"if {s['parent']}" if s.get('parent') else '') + (f" repeated {', '.join(rep[s['id']])}" if rep.get(s['id']) else '') + (f" rests from {s['rest_from']}" if s.get('rest_from') else '')
            o.append(f"{d['day']} | {PNAME[pair]} | {s['dir']} | {s['category']} | {f(s['entry'])} | {s['shape']} | {s['session']} | {s['confidence']} | {s['id']}{' ' + note.strip() if note.strip() else ''}")
        if not rows:
            # E3C 8.13 'every day covered or "No qualifying setups - [reason]"': a day that carries only per-day repeats lists them; a day whose orders fell to the 11-trade limit says so
            reps = [f"{s['origin']['id']} {s['dir']} {f(s['entry'])}" for s in R.get('setups', []) if s.get('clone') and s['day'] == d['day']]
            capped = any(l.startswith(d['day'] + ' ') and 'EMISSION_CAPPED' in l for l in R.get('log', []))
            if reps:
                o.append(f"{d['day']} | {PNAME[pair]} | - | Swing Scalp (repeat) | - | {'+'.join(d['shapes'])} | London Open | - | per-day repeats: {'; '.join(reps)}")
            else:
                why = 'the orders of this day fell to the 11-trade limit of the week (EMISSION_CAPPED, see DISCARDED)' if capped else "no anchor of this day's shape passed the gates (see DISCARDED)"
                o.append(f"{d['day']} | {PNAME[pair]} | - | - | - | {'+'.join(d['shapes'])} | - | - | No qualifying setups - {why}")
    for d_ in ('Mon', 'Tue', 'Wed', 'Thu', 'Fri'):
        if not any(d['day'] == d_ for d in days):
            o.append(f"{d_} | {PNAME[pair]} | - | - | - | - | - | - | No qualifying setups - Engine 2 gives this day no shape (chain confidence under 25%)")
    for title, cats in (('HTF SWING SETUPS', ('HTF Swing', 'Reversal')), ('SWING SCALP SETUPS', ('Swing Scalp',)), ('REINFORCEMENT ENTRIES', ('Reinforcement',)), ('TRANSITION SETUPS', ('Transition',))):
        rows = [s for s in S if s['category'] in cats]
        o += ['', f"--- {title} ---"] + ([] if rows else ['none'])
        for s in rows:
            a = s['anchor']; dd = next((d for d in days if d['day'] == s['day']), None)
            o.append(f"{s['id']} | {PNAME[pair]} | {s['dir']} | {s['category']} | Day: {s['day']} | Session: {s['session']} | Shape: {s['shape']}")
            o.append(f"  Entry: {f(s['entry'])} | SL: {f(s['sl'])} | TP: {f(s['tp'])} | RRR: {s['rrr']:.2f}{(' / blended ' + format(s['rrr_blended'], '.2f')) if s.get('rrr_blended') else ''} | Quality: {s.get('quality', '-')} | Confidence: {s['confidence']}")
            o.append(f"  Anchor Zone: {name(a)} [{cls(a)}{', tested ' + str(a['mit']) + 'x' if a.get('mit') is not None else ''}] | Shape Trigger: {s['shape']} @ {s['day']} {s['session']} | Day Catalysts: {', '.join(dd['triggers']) if dd and dd.get('triggers') else 'none listed'}")
            o.append(f"  Audit Trail: {s['why']} | attempts {s.get('attempts', 1)}")
            o.append(f"  Cascade Source: {CASCADE[pair]} | Parent Trade Ref: {s.get('parent') or '-'} | Anchor Hit Window: {s['day']} {s['session']} {SES_UTC.get(s['session'], '')} UTC" + (f" (order rests from {s['rest_from']})" if s.get('rest_from') else '') + (f" | repeated: {', '.join(rep[s['id']])}" if rep.get(s['id']) else ''))
            # E3C 12.2 floor invariants (checkMirrorFloorV45): 'Floor: RRR >= 2.5 | Session bracket valid | SL envelope (within GOLDEN_SL_MAX_PIPS = 9.5)' - reported per setup as flags
            # (his own golden GBP/USD stops are 10.6-14.1 pips, so the envelope is a flag here, not a discard); E3C 12.3 CS-1: the stop against the day's open of the E2 path
            slp = abs(s['entry'] - s['sl']) / EP.D.PIP[pair] if hasattr(EP, 'D') else s.get('sl_pips', 0)
            if s.get('six'):
                o.append(f"  Direction validation (E3C 8.18): {s['six'][0]} of 6 disagree - " + ', '.join(f"{k}={v or '-'}" for k, v in s['six'][1]))
            o.append(f"  Floor invariants (E3C 12.2): RRR {'>= 2.5 ok' if s['rrr'] >= 2.5 else '< 2.5'} | session bracket = the E2 step's days | SL envelope 9.5p: {'inside' if slp <= 9.5 + 1e-9 else f'OUTSIDE ({slp:.1f}p)'}"
                     + (f" | ALT trigger: 1H close {'above' if s['trigger']['dir'] == 'up' else 'below'} {f(s['trigger']['level'])} ({s['trigger']['zone']})" if s.get('trigger') else ''))
    o += ['', '--- DAILY SESSION NOTES ---']
    for d in days:
        o.append(f"{d['day']}: {'+'.join(d['shapes'])} {d['dir']} | key zone {d['key']} | range {f(d['lo'])}-{f(d['hi'])} | confidence {int(round(100 * d['conf']))}% | catalysts: {', '.join(d.get('triggers') or []) or 'none listed'}")
    o.append('Weekend: Close ALL positions by NY close Friday - per pair')
    dv = chain.get('divergence')
    if dv is not None:
        o += ['', f"--- CASCADE (E3C 10.7, flag only) --- divergence {dv['value']:.2f} -> {dv['state']} | DXY chain / pair's own chain per day: " + ' | '.join(dv['rows'])
              + f" | pair's own breakout direction: {dv['own_dir'] or 'none'}"]
    o += ['', '--- DISCARDED (reason on every discard) ---'] + ([l for l in R.get('log', [])] or ['none'])
    rr = sorted(s['rrr'] for s in S)
    med = (rr[len(rr) // 2] if len(rr) % 2 else (rr[len(rr) // 2 - 1] + rr[len(rr) // 2]) / 2) if rr else 0.0
    n = lambda c: sum(1 for s in S if s['category'] in c)
    o += ['', '--- WEEKLY STATS ---',
          f"Total Setups: {len(S)} | HTF: {n(('HTF Swing', 'Reversal'))} | Scalps: {n(('Swing Scalp',))} | Reinforcements: {n(('Reinforcement',))} | Transitions: {n(('Transition',))}",
          f"Average RRR: {(sum(rr) / len(rr)) if rr else 0.0:.2f} | Median RRR: {med:.2f}",
          f"f(T) Acceptance (E3C:996: 8 per pair minimum): {len(S)} setups on {PNAME[pair]} - {'met' if len(S) >= 8 else 'NOT met'}"]
    return o


ACCENT = {'DXY': ('20,20,40', '100,150,255'), 'EURUSD': ('10,30,60', '80,140,255'), 'GBPUSD': ('40,15,50', '180,100,220')}       # P533 10.10 pair accent colours
PNAME = {'DXY': 'DXY', 'EURUSD': 'EUR/USD', 'GBPUSD': 'GBP/USD'}


def table(pair, monday, X, chain, R):
    """P533 Part X 10.7 'TABLE: 2x17' (position.top_right; background color.new(color.black, 10); border RGB 40,40,45): row 0 header (TRIDENT v8 | pair + week), 1 chain + confidence,
    2 alternative chain + confidence, 3 day-by-day shape, 4 ZONES header, 5-9 IP zones (five rows, top to bottom: PG4), 10 TRADES header, 11-13 short trade (entry / SL | TP / day + RRR),
    14-16 long trade; price format 10.9 (DXY #.##, pairs #.####); PG5 exact row indexing"""
    import datetime as dt
    f = (lambda v: '%.2f' % v) if pair == 'DXY' else (lambda v: '%.4f' % v)
    m0 = dt.date.fromisoformat(monday); m1 = m0 + dt.timedelta(days=4)
    wk = f"{m0.strftime('%b')}{m0.day}-{(m1.strftime('%b') if m1.month != m0.month else '')}{m1.day}"
    ch = chain.get('chain') or []
    alt = chain.get('alt') or {}
    altc = chain.get('alt_chain') or {}
    rows = [('TRIDENT v8', f"{PNAME[pair]} {wk}"),
            ('Chain', (' -> '.join(c['shape'] for c in ch) or '-') + (f" | {int(round(100 * ch[-1]['cum']))}%" if ch else '')),
            ('Alt chain', ((' -> '.join(c['shape'] for c in altc.get('chain', [])) + (f" | {int(round(100 * alt['conf']))}%" if alt.get('conf') is not None else '')) if altc.get('chain') else '-')),
            ('Days', ' | '.join(f"{d['day']} {'+'.join(d['shapes'])}" for d in chain.get('days', [])) or '-'),
            ('ZONES', '')]
    spot = X['spot']
    zs = sorted([z for z in X['zones'] if z.get('drawn')], key=lambda z: min(abs(z['bot'] - spot), abs(z['top'] - spot)))[:5]
    zs.sort(key=lambda z: -z['top'])
    for k in range(5):
        rows.append((zs[k]['name'], f"{f(zs[k]['bot'])}-{f(zs[k]['top'])} | {zs[k]['degree']} | {zs[k]['zfp']} ZFP") if k < len(zs) else ('-', '-'))
    rows.append(('TRADES', ''))
    S = (R or {}).get('setups', []) if isinstance(R, dict) else []
    for side in ('SHORT', 'LONG'):
        t = next((s for s in S if s['dir'] == side and not s.get('clone')), None)
        if t is None:
            rows += [(side.capitalize(), '-'), ('SL | TP', '-'), ('Day | RRR', '-')]
        else:
            rows += [(f"{side.capitalize()} {t['id']}", 'Entry ' + f(t['entry'])), ('SL | TP', f"{f(t['sl'])} | {f(t['tp'])}"), ('Day | RRR', f"{t['day']} {t['shape']} | {t['rrr']:.1f}R")]
    assert len(rows) == 17
    hb, ht = ACCENT[pair]
    o = ['    if show_tbl', '        var table tb = table.new(position.top_right, 2, 17, bgcolor=color.new(color.black, 10), border_color=color.rgb(40,40,45), border_width=1)']
    for i, (a, b) in enumerate(rows):
        head = i in (0, 4, 10)
        bg = f"color.rgb({hb})" if head else 'color.new(color.black, 10)'
        tc = f"color.rgb({ht})" if head else 'color.white'
        for col_, txt in ((0, a), (1, b)):
            o.append(f'        table.cell(tb, {col_}, {i}, "{txt}", text_color={tc}, bgcolor={bg}, text_size=size.small, text_halign=text.align_left)')
    return o


if __name__ == '__main__':
    monday, pair = sys.argv[1], sys.argv[2]
    args_ = [a for a in sys.argv[1:] if not a.startswith('--')]
    out = args_[2] if len(args_) > 2 else os.path.join(HERE, 'out', f'PLUTUS_{pair}_{monday}.pine')
    daily = '--weekly' not in sys.argv              # daily anchoring is the default (D-131, L-47); --weekly = every order fixed at the Monday anchor
    X, chain, setups, src = run(pair, monday, daily=daily)
    open(out, 'w').write(src)
    print(out)
