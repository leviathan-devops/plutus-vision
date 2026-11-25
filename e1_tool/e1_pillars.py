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
