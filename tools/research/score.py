"""score.py - shared research scorer for E1 band maps (DESIGN RESEARCH ONLY - acceptance is a frame looked at in Pinebox).

A "map" is, for one pair and one week, a short list of price bands (bot, top) fixed at the Monday anchor
(Monday 02:00 America/New_York). The scorer walks the 1H bars of that week (anchor .. Friday 17:00 New York) and
gives each band the verdict a trader looking at the chart would give:

  HELD      price came into the band and went back out the side it came from by >= D, without first running D beyond the far edge
  BROKEN    price ran D beyond the far edge first (the band was traded through)
  CONTAINS  the visit never resolved, but the week's high or low sits inside the band (the turn is in the band)
  BOUNDING  never touched, but it is the nearest band beyond the week's extreme and the extreme stopped within 2*D of it
  FLOATING  never touched and not bounding (a band in empty space = noise)
  PIVOT     price started the week inside the band and never gave a resolved test (neutral, not counted)
  OPEN      touched, unresolved, no extreme inside (neutral, not counted)

D = 0.10 x the mean weekly range of the 13 completed weeks before the anchor (about 10 pips on DXY).
accuracy = (HELD + CONTAINS + BOUNDING) / (HELD + CONTAINS + BOUNDING + BROKEN + FLOATING + missed week extremes)
A week extreme is "missed" when the week's high (low) is not inside any band widened by 3 pips.

Everything a design may read for a week must come from pre(...) (bars closed by the anchor) and the level dumps.
post(...) is for the scorer only; TEST weeks are locked.
"""
import datetime as dt, glob, json, os
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
NY = ZoneInfo('America/New_York')
SYM = {'DXY': 'TVC_DXY', 'EURUSD': 'FX_EURUSD', 'GBPUSD': 'FX_GBPUSD'}
PIP = {'DXY': 0.01, 'EURUSD': 0.0001, 'GBPUSD': 0.0001}
TFMS = {'15': 900000, '30': 1800000, '60': 3600000, '240': 14400000}
ALL_WEEKS = [(dt.date(2026, 2, 2) + dt.timedelta(days=7 * i)).isoformat() for i in range(40)]
TEST = ['2026-02-23', '2026-03-23', '2026-04-27', '2026-05-18', '2026-06-15', '2026-07-27', '2026-08-31', '2026-10-05']
VALID = ['2026-02-16', '2026-03-09', '2026-04-13', '2026-05-11', '2026-06-22', '2026-08-03', '2026-09-14', '2026-10-26']
DEV = [w for w in ALL_WEEKS if w not in TEST and w not in VALID]
_cache = {}


def bars(pair, tf='60'):
    k = (pair, tf)
    if k not in _cache:
        b = []
        for f in sorted(glob.glob(os.path.expanduser(f'~/.local/share/pinebox/data/tv-bars/{SYM[pair]}/{tf}/*.json'))):
            b += json.load(open(f))
        _cache[k] = b
    return _cache[k]


def anchor_ms(monday):
    d = dt.date.fromisoformat(monday)
    return int(dt.datetime(d.year, d.month, d.day, 2, 0, tzinfo=NY).timestamp() * 1000)


def end_ms(monday):
    d = dt.date.fromisoformat(monday) + dt.timedelta(days=4)
    return int(dt.datetime(d.year, d.month, d.day, 17, 0, tzinfo=NY).timestamp() * 1000)


def pre(pair, monday, tf='240'):
    """bars of timeframe tf that had CLOSED by the Monday anchor - the only market data a design may read for that week"""
    a = anchor_ms(monday)
    return [b for b in bars(pair, tf) if b['time'] + TFMS[tf] <= a]


def post(pair, monday):
    """1H bars of the week under test (scorer only)"""
    if monday in TEST:
        raise RuntimeError('TEST weeks are locked')
    a, e = anchor_ms(monday), end_ms(monday)
    return [b for b in bars(pair, '60') if a <= b['time'] < e]


def spot(pair, monday):
    return pre(pair, monday, '60')[-1]['close']


def weekly_ranges(pair, monday, n=13):
    """(high, low, close) of the n completed trading weeks before the anchor, oldest first (week = Sun 17:00 NY .. Fri 17:00 NY)"""
    out, cur, key = [], None, None
    for b in pre(pair, monday, '240'):
        t = dt.datetime.fromtimestamp(b['time'] / 1000, NY) + dt.timedelta(hours=7)
        k = t.isocalendar()[:2]
        if k != key:
            if cur:
                out.append(cur)
            cur, key = [b['high'], b['low'], b['close']], k
        else:
            cur[0], cur[1], cur[2] = max(cur[0], b['high']), min(cur[1], b['low']), b['close']
    # cur is the Sunday-evening stub of the week under test when it exists; keep completed weeks only
    wk_of_anchor = (dt.datetime.fromtimestamp(anchor_ms(monday) / 1000, NY) + dt.timedelta(hours=7)).isocalendar()[:2]
    if cur and key != wk_of_anchor:
        out.append(cur)
    return out[-n:]


def awr(pair, monday, n=13):
    w = weekly_ranges(pair, monday, n)
    return sum(h - l for h, l, _ in w) / len(w)


def levels(pair):
    """the engine's level dump: list of weeks {week, spot, levels[], sd[], cur_zones[]} (all computed at the anchor)"""
    return json.load(open(os.path.join(HERE, f'levels.{pair}.json')))


def judge_week(pair, monday, bands):
    """bands: list of (bot, top). returns {'bands': [{bot, top, verdict, visits, first}], 'hi', 'lo', 'missed', 'D'}"""
    P, D = PIP[pair], 0.10 * awr(pair, monday)
    px = post(pair, monday)
    s0 = spot(pair, monday)
    hi, lo = max(b['high'] for b in px), min(b['low'] for b in px)
    res = []
    for bot, top in bands:
        state = 'above' if s0 > top else 'below' if s0 < bot else 'inside'
        started_inside = state == 'inside'
        touched, in_visit, origin, entry_i, verdicts = False, False, None, -1, []
        for i, b in enumerate(px):
            if state == 'inside':
                touched = True
                if b['close'] > top:
                    state = 'above'
                elif b['close'] < bot:
                    state = 'below'
                continue
            if not in_visit and b['low'] <= top and b['high'] >= bot:
                in_visit, origin, entry_i, touched = True, state, i, True
            if in_visit:
                if origin == 'below':
                    if b['high'] >= top + D:
                        verdicts.append('BROKEN'); in_visit = False; state = 'above'
                    elif (i > entry_i and b['low'] <= bot - D) or b['close'] <= bot - D:
                        verdicts.append('HELD'); in_visit = False
                else:
                    if b['low'] <= bot - D:
                        verdicts.append('BROKEN'); in_visit = False; state = 'below'
                    elif (i > entry_i and b['high'] >= top + D) or b['close'] >= top + D:
                        verdicts.append('HELD'); in_visit = False
        contains = (bot - 3 * P <= hi <= top + 3 * P) or (bot - 3 * P <= lo <= top + 3 * P)
        if verdicts:
            v = verdicts[0]
        elif touched:
            v = 'CONTAINS' if contains else ('PIVOT' if started_inside else 'OPEN')
        else:
            v = 'UNTOUCHED'
        res.append({'bot': bot, 'top': top, 'verdict': v, 'visits': verdicts})
    # untouched: bounding (nearest beyond the extreme, within 2D) or floating
    up = sorted([r for r in res if r['verdict'] == 'UNTOUCHED' and r['bot'] > hi], key=lambda r: r['bot'])
    dn = sorted([r for r in res if r['verdict'] == 'UNTOUCHED' and r['top'] < lo], key=lambda r: -r['top'])
    for k, r in enumerate(up):
        r['verdict'] = 'BOUNDING' if k == 0 and r['bot'] - hi <= 2 * D else 'FLOATING'
    for k, r in enumerate(dn):
        r['verdict'] = 'BOUNDING' if k == 0 and lo - r['top'] <= 2 * D else 'FLOATING'
    for r in res:
        if r['verdict'] == 'UNTOUCHED':
            r['verdict'] = 'FLOATING'
    missed = 0
    for x in (hi, lo):
        if not any(r['bot'] - 3 * P <= x <= r['top'] + 3 * P for r in res):
            missed += 1
    return {'bands': res, 'hi': hi, 'lo': lo, 'missed': missed, 'D': D, 'spot': s0}


def score(maps):
    """maps: {(pair, monday): [(bot, top), ...]} -> totals + accuracy"""
    t = {k: 0 for k in ('HELD', 'CONTAINS', 'BOUNDING', 'BROKEN', 'FLOATING', 'PIVOT', 'OPEN', 'missed', 'bands', 'weeks', 'later_breaks')}
    per = {}
    for (pair, monday), bands in maps.items():
        j = judge_week(pair, monday, bands)
        t['weeks'] += 1
        t['missed'] += j['missed']
        g = b = 0
        for r in j['bands']:
            t[r['verdict']] += 1
            t['bands'] += 1
            t['later_breaks'] += 1 if r['verdict'] == 'HELD' and 'BROKEN' in r['visits'] else 0
            g += r['verdict'] in ('HELD', 'CONTAINS', 'BOUNDING')
            b += r['verdict'] in ('BROKEN', 'FLOATING')
        per[(pair, monday)] = (g, b + j['missed'])
    good = t['HELD'] + t['CONTAINS'] + t['BOUNDING']
    bad = t['BROKEN'] + t['FLOATING'] + t['missed']
    t['accuracy'] = round(good / (good + bad), 3) if good + bad else None
    t['precision_touched'] = round((t['HELD'] + t['CONTAINS']) / max(1, t['HELD'] + t['CONTAINS'] + t['BROKEN']), 3)
    t['extreme_recall'] = round(1 - t['missed'] / (2 * max(1, t['weeks'])), 3)
    t['weeks_at_90'] = sum(1 for g, b in per.values() if g + b and g / (g + b) >= 0.9)
    t['per_week'] = {f'{p} {m}': f'{g}/{g + b}' for (p, m), (g, b) in sorted(per.items(), key=lambda x: (x[0][1], x[0][0]))}
    return t


if __name__ == '__main__':
    W14 = {('DXY', '2026-03-30'): [(100.50, 100.65), (100.00, 100.25), (99.30, 99.60), (98.80, 99.10)],
           ('EURUSD', '2026-03-30'): [(1.1600, 1.1640), (1.1545, 1.1575), (1.1495, 1.1515), (1.1430, 1.1460)],
           ('GBPUSD', '2026-03-30'): [(1.3400, 1.3480), (1.3300, 1.3350), (1.3250, 1.3280), (1.3150, 1.3200)]}
    for k, v in W14.items():
        j = judge_week(k[0], k[1], v)
        print(k, 'spot', j['spot'], 'hi', j['hi'], 'lo', j['lo'], 'D', round(j['D'], 5), 'missed', j['missed'])
        for r in j['bands']:
            print('   ', r['bot'], r['top'], r['verdict'], r['visits'])
    s = score(W14)
    print({k: v for k, v in s.items() if k != 'per_week'}, s['per_week'])
    # the engine's current map, for reference
    cur = {}
    for pair in SYM:
        for w in levels(pair):
            if w['week'] in DEV:
                cur[(pair, w['week'])] = [(z['bot'], z['top']) for z in w['cur_zones']]
    s = score(cur)
    print('CURRENT ENGINE on DEV:', {k: v for k, v in s.items() if k != 'per_week'})
