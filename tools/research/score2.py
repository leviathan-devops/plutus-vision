"""score2.py - research scorer with the OPERATOR'S definition of a valid zone (rulings L-22..L-25). DESIGN RESEARCH ONLY;
acceptance is a frame opened and looked at in Pinebox.

For each zone (bot, top) fixed at the Monday anchor, the FIRST time price comes to it during the week is classified on 1H bars:

  REJECT       price came to the zone and left on the side it came from      (sharp reaction: wick or body)        VALID
  CONSOLIDATE  price worked in / around the zone for longer than a straight pass takes, whichever side it left     VALID
  SLICED       price went straight through at ordinary speed or faster ("pierced like paper")                      INVALID
  PIVOT0       price was already inside the zone at the anchor (reported separately, not counted)
  UNTOUCHED    price never came to it (reported separately: near = within one mean daily range of the week's extreme, else far)

"Around" the zone = one mean 1H bar range M (measured on the 120 1H bars before the anchor) beyond either edge.
A visit ends when a 1H bar CLOSES more than M beyond an edge. A straight pass of a zone of height H needs about
ceil((H + 2M) / M) bars; a pass that took no more than that (+1) is SLICED, anything slower is CONSOLIDATE.
Nothing here is a tunable target: M is measured from the market, the pass time follows from the zone's own height.

valid_rate = (REJECT + CONSOLIDATE) / (REJECT + CONSOLIDATE + SLICED)      <- the operator's "reacts on first touch"
"""
import math, sys
import score as S


def bar_noise(pair, monday):
    b = S.pre(pair, monday, '60')[-120:]
    return sum(x['high'] - x['low'] for x in b) / len(b)


def daily_range(pair, monday):
    b = S.pre(pair, monday, '240')[-120:]          # 20 trading days of 4H bars
    days = [b[i:i + 6] for i in range(0, len(b), 6)]
    return sum(max(x['high'] for x in d) - min(x['low'] for x in d) for d in days) / len(days)


def judge_week(pair, monday, zones):
    """zones: list of (bot, top). returns list of dicts {bot, top, first, visits[], dwell}"""
    M = bar_noise(pair, monday)
    px = S.post(pair, monday)
    s0 = S.spot(pair, monday)
    hi, lo = max(b['high'] for b in px), min(b['low'] for b in px)
    adr = daily_range(pair, monday)
    out = []
    for bot, top in zones:
        need = 2 * math.ceil((top - bot + 2 * M) / M)      # a pass must take twice a straight pass to count as consolidation
        state = 1 if s0 > top else -1 if s0 < bot else 0
        start_inside = state == 0
        vin, org, n, visits, dwell0 = False, 0, 0, [], None
        for b in px:
            if state == 0:                     # started inside: wait for a close clear of the zone
                if b['close'] > top + M:
                    state = 1
                elif b['close'] < bot - M:
                    state = -1
                continue
            if not vin and b['low'] <= top and b['high'] >= bot:
                vin, org, n = True, state, 0
            if vin:
                n += 1
                end = 1 if b['close'] > top + M else -1 if b['close'] < bot - M else 0
                if end != 0:
                    v = 'REJECT' if end == org else ('SLICED' if n <= need else 'CONSOLIDATE')
                    visits.append(v)
                    if dwell0 is None:
                        dwell0 = n
                    vin, state = False, end
        if vin:                                 # the week ended while price was still working the zone
            visits.append('CONSOLIDATE' if n > need else 'OPEN')
            if dwell0 is None:
                dwell0 = n
        if start_inside:
            first = 'PIVOT0'
        elif visits:
            first = visits[0]
        else:
            gap = (bot - hi) if bot > hi else (lo - top)
            first = 'UNTOUCHED_NEAR' if gap <= adr else 'UNTOUCHED_FAR'
        nr = sum(v in ('REJECT', 'CONSOLIDATE') for v in visits)
        ns = visits.count('SLICED')
        # the whole week, the way the operator reads a chart: VALID = price reacted to the zone at least as often as it ignored it
        week = ('VALID' if nr >= 1 and nr >= ns else 'INVALID' if ns >= 1 else 'VALID' if start_inside else first)
        out.append({'bot': bot, 'top': top, 'first': first, 'week': week, 'visits': visits, 'dwell': dwell0, 'need': need})
    return out


def score(maps):
    t = {k: 0 for k in ('REJECT', 'CONSOLIDATE', 'SLICED', 'OPEN', 'PIVOT0', 'UNTOUCHED_NEAR', 'UNTOUCHED_FAR', 'zones', 'weeks', 'ever_sliced')}
    wk = {}
    for (pair, monday), zones in maps.items():
        t['weeks'] += 1
        for r in judge_week(pair, monday, zones):
            t[r['first']] += 1
            t['zones'] += 1
            t['ever_sliced'] += 'SLICED' in r['visits']
            wk[r['week']] = wk.get(r['week'], 0) + 1
    v = t['REJECT'] + t['CONSOLIDATE']
    V, I, UN, UF = wk.get('VALID', 0), wk.get('INVALID', 0), wk.get('UNTOUCHED_NEAR', 0), wk.get('UNTOUCHED_FAR', 0)
    t.update(week_valid=V, week_invalid=I, week_un=UN, week_uf=UF)
    t['eye_strict'] = round(V / max(1, t['zones']), 3)                 # every drawn zone must earn its place
    t['eye_touched'] = round(V / max(1, V + I), 3)                     # of the zones price came to
    t['eye_lenient'] = round(V / max(1, V + I + UF), 3)                # near-untouched (bounding) zones not counted
    t['valid_rate'] = round(v / max(1, v + t['SLICED']), 3)
    t['never_sliced_rate'] = round(1 - t['ever_sliced'] / max(1, v + t['SLICED']), 3)
    return t


def show(name, maps):
    t = score(maps)
    print('%-40s EYE strict %.3f | lenient %.3f | of touched %.3f || valid %3d invalid %3d untouched near %3d far %3d | first touch valid %.3f | %.1f zones/wk' % (
        name, t['eye_strict'], t['eye_lenient'], t['eye_touched'], t['week_valid'], t['week_invalid'], t['week_un'], t['week_uf'], t['valid_rate'], t['zones'] / max(1, t['weeks'])))
    return t


if __name__ == '__main__':
    gold = [(101.19, 101.29), (100.94, 100.985), (100.545, 100.675)]
    print('operator golden week (his hand-drawn bands):')
    for r in judge_week('DXY', '2026-07-06', gold):
        print('   ', r)
    W14 = {('DXY', '2026-03-30'): [(100.50, 100.65), (100.00, 100.25), (99.30, 99.60), (98.80, 99.10)],
           ('EURUSD', '2026-03-30'): [(1.1600, 1.1640), (1.1545, 1.1575), (1.1495, 1.1515), (1.1430, 1.1460)],
           ('GBPUSD', '2026-03-30'): [(1.3400, 1.3480), (1.3300, 1.3350), (1.3250, 1.3280), (1.3150, 1.3200)]}
    for k, z in W14.items():
        print(k, [(r['first'], r['visits']) for r in judge_week(k[0], k[1], z)])
    show('W14 report bands', W14)
    cur = {(p, w['week']): [(z['bot'], z['top']) for z in w['cur_zones']] for p in S.SYM for w in S.levels(p) if w['week'] in S.DEV}
    show('rejected engine v1 (14 zones/wk) on DEV', cur)
