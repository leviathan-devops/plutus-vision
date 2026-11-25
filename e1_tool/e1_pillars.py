"""e1_pillars.py - Engine 1 pillars, one function per prompt step (see E1_PSEUDOCODE.md for the line references)."""
import e1_data as D


# ── PILLAR 1 (P533:967-1059) ─────────────────────────────────────────────────────────────────────
def pivots(H, L, C):
    PP = (H + L + C) / 3
    R = H - L
    classic = {'PP': PP, 'R1': 2 * PP - L, 'S1': 2 * PP - H, 'R2': PP + R, 'S2': PP - R, 'R3': H + 2 * (PP - L), 'S3': L - 2 * (H - PP)}
    fib = {'PP': PP, 'R1': PP + 0.382 * R, 'S1': PP - 0.382 * R, 'R2': PP + 0.618 * R, 'S2': PP - 0.618 * R, 'R3': PP + R, 'S3': PP - R}
    cam = {'R4': C + R * 1.1 / 2, 'S4': C - R * 1.1 / 2, 'R3': C + R * 1.1 / 4, 'S3': C - R * 1.1 / 4,
           'R2': C + R * 1.1 / 6, 'S2': C - R * 1.1 / 6, 'R1': C + R * 1.1 / 12, 'S1': C - R * 1.1 / 12}
    checks = {'formula': abs(classic['R1'] + L - 2 * PP) < 1e-9 and abs(classic['S1'] + H - 2 * PP) < 1e-9,
              'sanity': classic['R2'] > classic['R1'] > PP > classic['S1'] > classic['S2'] > classic['S3'],
              'range': abs((classic['R2'] - classic['S2']) - 2 * R) < 1e-9,
              'fib_symmetry': abs((fib['R1'] - PP) - (PP - fib['S1'])) < 1e-9}
    return {'classic': classic, 'fib': fib, 'camarilla': cam, 'checks': checks}


def pillar1(pair, monday):
    w = D.weekly(pair, monday)[-1]
    days = D.daily(pair, monday)[-5:]
    out = {'weekly': dict(w, **pivots(w['high'], w['low'], w['close'])), 'daily': []}
    for d in days[-3:]:
        out['daily'].append(dict(d, **pivots(d['high'], d['low'], d['close'])))
    out['last5'] = days
    return out


# ── PILLAR 5 STEP 0f: 4H supply/demand = the candle BEFORE the strong move, wick high to wick low (P452:637-745; rulings L-37, L-38)
# A "strong momentum move" is read from the candles the way the operator's notes define a valid order block: the move leaves an
# inefficiency, i.e. a gap between the candle before it and the candle after it. No minimum size (L-37).
def step0f(pair, monday):
    b = D.closed(pair, '240', monday)
    b = [x for x in b if x['time'] >= D.boundary_ms(monday) - 60 * 86400000]         # last 60 calendar days (P452:641)
    zones, i, n = [], 1, len(b)
    while i < n - 1:
        down = b[i + 1]['high'] < b[i - 1]['low']        # gap below the "before" candle -> bearish move -> supply
        up = b[i + 1]['low'] > b[i - 1]['high']          # gap above the "before" candle -> bullish move -> demand
        if down or up:
            o = b[i - 1]
            j = i
            while j < n - 1 and ((b[j + 1]['high'] < b[j - 1]['low']) if down else (b[j + 1]['low'] > b[j - 1]['high'])):
                j += 1                                   # consecutive gaps = the same impulse
            ext = min(x['low'] for x in b[i:j + 1]) if down else max(x['high'] for x in b[i:j + 1])
            zones.append({'type': 'Supply' if down else 'Demand', 'bot': o['low'], 'top': o['high'], 'origin_time': o['time'],
                          'origin': {k: o[k] for k in ('open', 'high', 'low', 'close')},
                          'next': {k: b[i][k] for k in ('open', 'high', 'low', 'close')},
                          'move': abs((o['low'] if down else o['high']) - ext), 'i': i - 1, 'end': j})
            i = j + 1
        else:
            i += 1
    # BoM = the first zone of a leg; MoM = a continuation zone in the same direction as the zone before it (P452:694-697)
    prev = None
    for z in zones:
        z['kind'] = 'MoM' if prev == z['type'] else 'BoM'
        prev = z['type']
    # mitigation: later separate returns into the zone (P452:713-730)
    for z in zones:
        soft = hard = 0
        inside = True
        for x in b[z['end'] + 1:]:
            touch = x['low'] <= z['top'] and x['high'] >= z['bot']
            if touch and not inside:
                body_lo, body_hi = min(x['open'], x['close']), max(x['open'], x['close'])
                if body_lo <= z['top'] and body_hi >= z['bot']:
                    hard += 1
                else:
                    soft += 1
            inside = touch
        z['mit'] = soft + hard; z['soft'] = soft; z['hard'] = hard
    return zones


def _u(pair, pips):
    """the prompt writes thresholds in DXY points (0.15 = 15 pips); on a pair the same number of pips applies"""
    return pips * D.PIP[pair]


# ── PILLAR 5 STEP 0b / 0c: daily swing lows / highs with rejection wicks, 90 daily bars (P533:1217-1232); STEP 0h relaxed (P452:767-781)
def step0_swings(pair, monday):
    d = D.daily(pair, monday)[-90:]
    out = []
    for i in range(1, len(d)):
        x = d[i]
        rng = x['high'] - x['low']
        if rng <= 0:
            continue
        nxt = d[i + 1] if i + 1 < len(d) else None
        body_lo, body_hi = min(x['open'], x['close']), max(x['open'], x['close'])
        pos = (x['close'] - x['low']) / rng
        if x['low'] < d[i - 1]['low'] and (nxt is None or nxt['low'] > x['low']):
            wick = body_lo - x['low']
            grade = 'major' if wick >= _u(pair, 15) and pos >= 0.5 else 'minor' if wick >= _u(pair, 8) and pos >= 0.6 else None
            out.append({'side': 'low', 'price': x['low'], 'date': x['date'], 'wick': wick, 'close_pos': pos, 'grade': grade})
        if x['high'] > d[i - 1]['high'] and (nxt is None or nxt['high'] < x['high']):
            wick = x['high'] - body_hi
            grade = 'major' if wick >= _u(pair, 15) and pos <= 0.5 else 'minor' if wick >= _u(pair, 8) and pos <= 0.4 else None
            out.append({'side': 'high', 'price': x['high'], 'date': x['date'], 'wick': wick, 'close_pos': pos, 'grade': grade})
    return out


# ── STEP 0.45: liquidity sweep zones (P533:1255-1272) and STEP 0.5: repeated extreme magnets (P533:1292-1308)
def step045_lsz(pair, monday, swings, spot):
    out = []
    for s in swings:
        lo, hi = (s['price'], s['price'] + _u(pair, 5)) if s['side'] == 'low' else (s['price'] - _u(pair, 5), s['price'])
        near = min(abs(spot - lo), abs(spot - hi)) <= _u(pair, 30)
        out.append({'bot': lo, 'top': hi, 'type': 'Demand-side' if s['side'] == 'low' else 'Supply-side', 'source': f"D1 swing {s['side']} {s['date']}",
                    'priority': 'ACTIVE SL TRIGGER' if near else 'STANDARD', 'grade': s['grade'], 'date': s['date']})
    return out


def step05_magnets(pair, swings):
    out, used = [], set()
    for i, a in enumerate(swings):
        if i in used:
            continue
        grp = [a]
        for j in range(i + 1, len(swings)):
            if j not in used and abs(swings[j]['price'] - a['price']) <= _u(pair, 5):
                grp.append(swings[j]); used.add(j)
        if len(grp) >= 2:
            sides = {g['side'] for g in grp}
            wsum = sum(max(g['wick'], D.PIP[pair]) for g in grp)
            price = sum(g['price'] * max(g['wick'], D.PIP[pair]) for g in grp) / wsum
            kind = 'Role Reversal Magnet' if len(sides) == 2 else 'Repeated Low Magnet' if 'low' in sides else 'Repeated High Magnet'
            bonus = 2.0 if kind.startswith('Role') or len(grp) >= 3 else 1.5
            out.append({'price': price, 'kind': kind, 'dates': [g['date'] for g in grp], 'n': len(grp), 'bonus': bonus})
    return out


# ── PILLAR 2: MA confluence grid on daily closes (P533:1065-1088)
def pillar2(pair, monday):
    c = [d['close'] for d in D.daily(pair, monday)]
    out = []
    for n, w in ((9, 0.5), (10, 0.5), (20, 1.0), (50, 1.5), (100, 2.0), (200, 3.0)):
        if len(c) >= n:
            out.append({'name': f'SMA{n}', 'p': sum(c[-n:]) / n, 'w': w})
            k, e = 2 / (n + 1), c[0]
            for v in c[1:]:
                e += (v - e) * k
            out.append({'name': f'EMA{n}', 'p': e, 'w': w})
    for m in out:
        m['cluster'] = sum(1 for o in out if abs(o['p'] - m['p']) <= _u(pair, 15))
    return out


# ── PILLAR 6: fib retracements of the prior week range + round numbers (P452:835-862)
def pillar6(pair, monday, lo, hi):
    w = D.weekly(pair, monday)[-1]
    R = w['high'] - w['low']
    fibs = [{'name': f'Wfib{int(r * 1000) / 10}', 'p': w['high'] - r * R} for r in (0.236, 0.382, 0.5, 0.618)]
    step = _u(pair, 25)
    rounds, k = [], int(lo / step)
    while k * step <= hi:
        p = k * step
        if p >= lo:
            kind = 'big' if k % 4 == 0 else 'half' if k % 2 == 0 else 'quarter'
            rounds.append({'name': 'RN-' + kind, 'p': round(p, 6), 'kind': kind})
        k += 1
    return fibs, rounds


# ── PILLAR 3 / 8: K factor and EUR/USD strike -> DXY (P533:928-952; P452:890-950; tiers P533:1443-1447)
def k_factor(rates):
    return 50.14348112 * rates['USDJPY'] ** 0.136 * rates['GBPUSD'] ** -0.119 * rates['USDCAD'] ** 0.091 * rates['USDSEK'] ** 0.042 * rates['USDCHF'] ** 0.036


def strike_to_dxy(K, strike):
    return K * strike ** -0.576


def tier(notional_m):
    return 1 if notional_m >= 1500 else 2 if notional_m >= 850 else 3
