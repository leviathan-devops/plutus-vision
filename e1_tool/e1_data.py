"""e1_data.py - the tool's "bundled libraries": TradingView candles (mandatory input, L-32) and the week boundary.
No price literals. TV 4H bars are stamped 21:00/01:00/05:00/09:00/13:00/17:00 UTC (17:00 New York session start)."""
import datetime as dt, glob, json, os
from zoneinfo import ZoneInfo

NY = ZoneInfo('America/New_York')
SYM = {'DXY': 'TVC_DXY', 'EURUSD': 'FX_EURUSD', 'GBPUSD': 'FX_GBPUSD'}
PIP = {'DXY': 0.01, 'EURUSD': 0.0001, 'GBPUSD': 0.0001}
TFMS = {'15': 900000, '30': 1800000, '60': 3600000, '240': 14400000}
_cache = {}


def bars(pair, tf):
    k = (pair, tf)
    if k not in _cache:
        b = []
        for f in sorted(glob.glob(os.path.expanduser(f'~/.local/share/pinebox/data/tv-bars/{SYM[pair]}/{tf}/*.json'))):
            b += json.load(open(f))
        _cache[k] = b
    return _cache[k]


def day_anchor_ms(monday, i):
    """London open (02:00 New York) of trading day i (0 = Monday) of the week: the anchor of that day's orders under daily anchoring (L-47, operator M-58 item 2: Tuesday-Friday orders
    and the Engine 2 line from each day's London-open position against the fixed Monday map; Fibonacci Spiderwebs items 3-5 'London Session open position = Trade Setup Anchor';
    E3C:115 WorkingDayMap.dayOpenSpot)"""
    d = dt.date.fromisoformat(monday) + dt.timedelta(days=i)
    return int(dt.datetime(d.year, d.month, d.day, 2, 0, tzinfo=NY).timestamp() * 1000)


def closed_until(pair, tf, ms):
    """bars of timeframe tf that had closed by the instant ms (daily anchoring: a day's London open)"""
    return [b for b in bars(pair, tf) if b['time'] + TFMS[tf] <= ms]


def boundary_ms(monday):
    """THE TEMPORAL ANCHOR = Monday London open of the target week, 02:00 New York (P533 session table: London Open 02:00-05:00 ET; CLAUDE.md hard constraint
    "Temporal anchor = Monday, start of the trading week"; R-15 "rewind to Monday London open"). Nothing stamped at or after it may feed the map."""
    return day_anchor_ms(monday, 0)


def week_start_ms(monday):
    """the trading week opens Sunday 17:00 New York"""
    d = dt.date.fromisoformat(monday) - dt.timedelta(days=1)
    return int(dt.datetime(d.year, d.month, d.day, 17, 0, tzinfo=NY).timestamp() * 1000)


def week_end_ms(monday):
    """Friday 17:00 New York"""
    d = dt.date.fromisoformat(monday) + dt.timedelta(days=4)
    return int(dt.datetime(d.year, d.month, d.day, 17, 0, tzinfo=NY).timestamp() * 1000)


def closed(pair, tf, monday):
    """bars of timeframe tf that had closed by the boundary"""
    b0 = boundary_ms(monday)
    return [b for b in bars(pair, tf) if b['time'] + TFMS[tf] <= b0]


def ts(ms):
    return dt.datetime.fromtimestamp(ms / 1000, dt.timezone.utc).strftime('%Y-%m-%d %H:%M')


def daily(pair, monday):
    """trading days (17:00 NY to 17:00 NY) from closed 1H bars: list of {date, open, high, low, close}"""
    out, key, cur = [], None, None
    for b in closed(pair, '60', monday):
        t = dt.datetime.fromtimestamp(b['time'] / 1000, NY) + dt.timedelta(hours=7)
        k = t.date()
        if k.weekday() >= 5:
            continue
        if k != key:
            if cur:
                out.append(cur)
            key, cur = k, {'date': k.isoformat(), 'open': b['open'], 'high': b['high'], 'low': b['low'], 'close': b['close']}
        else:
            cur['high'] = max(cur['high'], b['high']); cur['low'] = min(cur['low'], b['low']); cur['close'] = b['close']
    if cur:
        out.append(cur)
    # only COMPLETED trading days (a day ends 17:00 New York on its date); the session running at the anchor is not a prior day
    b0 = boundary_ms(monday)
    done = lambda d: int(dt.datetime.combine(dt.date.fromisoformat(d['date']), dt.time(17, 0), NY).timestamp() * 1000) <= b0
    return [d for d in out if done(d)]


def forming(pair, monday):
    """the trading day in progress at the anchor (Sunday 17:00 New York .. Monday London open): {date, open, high, low, close = spot at the anchor}, or None.
    L-05: the map is built from "the data that is available on Monday, London session open"; the D1 series as of that moment ends with this bar (D-25)."""
    w0 = week_start_ms(monday)
    b = [x for x in closed(pair, '60', monday) if x['time'] >= w0]
    if not b:
        return None
    return {'date': monday, 'open': b[0]['open'], 'high': max(x['high'] for x in b), 'low': min(x['low'] for x in b), 'close': b[-1]['close'], 'forming': True}


def weekly(pair, monday):
    """completed trading weeks from the daily bars: list of {monday, high, low, close}"""
    out, key, cur = [], None, None
    for d in daily(pair, monday):
        dd = dt.date.fromisoformat(d['date'])
        k = (dd - dt.timedelta(days=dd.weekday())).isoformat()
        if k != key:
            if cur:
                out.append(cur)
            key, cur = k, {'monday': k, 'high': d['high'], 'low': d['low'], 'close': d['close']}
        else:
            cur['high'] = max(cur['high'], d['high']); cur['low'] = min(cur['low'], d['low']); cur['close'] = d['close']
    if cur:
        out.append(cur)
    return out
