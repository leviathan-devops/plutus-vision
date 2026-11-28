"""e2_data.py - ENGINE 2 DATA MODULE (charter memory/22, plan memory/21 v5 step 3; operator M-77 'you should build a volume profile and delta proxy ... everything that is mentioned in this
context, you should build for Engine 2'). A NEW module beside the locked Engine 1: it edits nothing of Engine 1 and Engine 1 never imports it.
Sources, all cut at an explicit as-of instant t (only bars CLOSED by t are read - charter C2):
  spot candles with tick volume   the Pinebox bar store through e1_data.closed_until (every week since Feb 2025)
  futures with exchange volume    data/tvapi  CME:6E1! (EURUSD), CME:6B1! (GBPUSD), ICEUS:DX1! (DXY) - TradingView-API (tools/tvapi/fetch.mjs); intraday depth limited (README there)
  2-year yields                   data/tvapi  TVC:US02Y / DE02Y / GB02Y
  positioning (COT)               data/tvapi  COT:<code>_F_NCP_L / _S, weekly; usable only from its PUBLICATION (the Friday after the report date), not from its bar date
What it gives Engine 2 (his context document, pillar F, as context - definitions are the standard ones, no tuned threshold):
  volume profile   volume at price over the two prior completed weeks + the week so far (pillar C window): each bar's volume spread evenly over its low-high range;
                   VPOC = the price bin with the most volume; HVN / LVN = local maxima / minima of the profile
  delta proxy      per bar: volume x (close - open) / (high - low) (buying volume minus selling volume estimated from where the bar closed in its range); CVD = its running sum
  yield spread     US 2Y minus the pair's own 2Y, and its change over one and two weeks
  positioning      net noncommercial (long - short) and its weekly change, as published by t
  clocks           the day's institutional instants in LOCAL time (daylight-saving safe)
'Delta' here is a PROXY from candle volume, not order flow (stated in the charter)."""
import os, json, datetime as dt
from zoneinfo import ZoneInfo
import e1_data as D

HERE = os.path.dirname(os.path.abspath(__file__))
EXT_DIR = os.path.join(HERE, '..', 'data', 'tvapi')
FUT = {'EURUSD': 'CME:6E1!', 'GBPUSD': 'CME:6B1!', 'DXY': 'ICEUS:DX1!'}
Y2 = {'EURUSD': 'TVC:DE02Y', 'GBPUSD': 'TVC:GB02Y'}
COT = {'EURUSD': '099741', 'GBPUSD': '096742', 'DXY': '098662'}
EXT_TFMS = {'15': 900000, '30': 1800000, '60': 3600000, '240': 14400000, 'D': 86400000, 'W': 7 * 86400000}
COT_PUBLISH_MS = 5 * 86400000        # a weekly COT bar is stamped at its week's Monday; the report (Tuesday data) is published that Friday afternoon -> usable from the Saturday 00:00 UTC after it
WEEK_MS = 7 * 86400000
_ext = {}


def ext_bars(symbol, tf):
    """every stored bar of an external series (tests patch this function to cut / shock the store)"""
    k = (symbol, tf)
    if k not in _ext:
        p = os.path.join(EXT_DIR, f"{symbol.replace(':', '_').replace('!', '_')}__{tf}.json")
        _ext[k] = json.load(open(p))['bars'] if os.path.exists(p) else []
    return _ext[k]


def ext_closed(symbol, tf, t, lag=0):
    """bars of an external series closed by t (bar open time + its length + lag <= t)"""
    return [x for x in ext_bars(symbol, tf) if x['time'] + EXT_TFMS[tf] + lag <= t]


def _window(pair, monday, t):
    """pillar C window: from the start of the second-last completed week before `monday` to t"""
    return D.week_start_ms(monday) - 2 * WEEK_MS


def profile(pair, monday, t, source='auto'):
    """volume at price: {'step', 'bins': {index: volume}, 'vpoc', 'hvn': [prices], 'lvn': [prices], 'source', 'n'} from 15m spot bars (tick volume) or the 30m / 1H futures bars
    (exchange volume, where the store reaches back to the window; else None). One bin = one pip of the pair."""
    t0 = _window(pair, monday, t)
    step = D.PIP[pair]
    if source == 'auto':                 # the pair's own spot candles when they carry volume (EUR/USD, GBP/USD); TVC:DXY is an index without volume -> its future
        return profile(pair, monday, t, 'spot') or profile(pair, monday, t, 'fut')
    if source == 'spot':
        bars = [x for x in D.closed_until(pair, '15', t) if x['time'] >= t0]
    else:
        bars = next((b for b in ([x for x in ext_closed(FUT[pair], tf, t) if x['time'] >= t0] for tf in ('30', '60'))
                     if b and b[0]['time'] <= t0 + 2 * 86400000), [])
    if len(bars) < 50:
        return None
    if source != 'spot':                 # a future trades at a basis to spot: its prices are moved onto the spot scale by the median close difference of the bars both have in the window
        sp = {x['time']: x['close'] for tf in ('30', '60') for x in D.closed_until(pair, tf, t) if x['time'] >= t0}
        df = sorted(x['close'] - sp[x['time']] for x in bars if x['time'] in sp)
        if df:
            basis = df[len(df) // 2]
            bars = [dict(x, low=x['low'] - basis, high=x['high'] - basis, open=x['open'] - basis, close=x['close'] - basis) for x in bars]
    bins = {}
    for x in bars:
        v = float(x.get('volume') or 0.0)
        if v <= 0:
            continue
        a, b = int(round(x['low'] / step)), int(round(x['high'] / step))
        share = v / (b - a + 1)
        for k in range(a, b + 1):
            bins[k] = bins.get(k, 0.0) + share
    if not bins:
        return None
    ks = list(range(min(bins), max(bins) + 1))
    raw = [bins.get(k, 0.0) for k in ks]
    sm = [sum(raw[max(0, i - 2):i + 3]) / len(raw[max(0, i - 2):i + 3]) for i in range(len(raw))]      # 5-pip running mean: a node is a feature of the profile, not of one pip
    hvn = [ks[i] * step for i in range(2, len(sm) - 2) if sm[i] == max(sm[i - 2:i + 3]) and sm[i] > sm[i - 2] and sm[i] > sm[i + 2]]
    lvn = [ks[i] * step for i in range(2, len(sm) - 2) if sm[i] == min(sm[i - 2:i + 3]) and sm[i] < sm[i - 2] and sm[i] < sm[i + 2]]
    return {'step': step, 'bins': bins, 'smooth': dict(zip(ks, sm)), 'vpoc': ks[max(range(len(sm)), key=lambda i: sm[i])] * step, 'hvn': hvn, 'lvn': lvn, 'source': source, 'n': len(bars)}


def zone_volume(P, z):
    """how a zone sits in the profile: its mean volume per pip against the whole profile's mean ('rel'), the nodes inside it, and the lowest-volume pip just outside each edge
    (5 pips) - a vacuum at the rim. P = profile(); z = any Engine 1 zone with bot / top."""
    if P is None:
        return None
    step, sm = P['step'], P['smooth']
    a, b = int(round(z['bot'] / step)), int(round(z['top'] / step))
    inside = [sm.get(k, 0.0) for k in range(a, b + 1)]
    mean_all = sum(sm.values()) / max(1, len(sm))
    rim = lambda ks: min((sm.get(k, 0.0) for k in ks), default=0.0) / mean_all if mean_all > 0 else None
    return {'rel': (sum(inside) / max(1, len(inside))) / mean_all if mean_all > 0 else None,
            'hvn_inside': [p for p in P['hvn'] if z['bot'] <= p <= z['top']], 'lvn_inside': [p for p in P['lvn'] if z['bot'] <= p <= z['top']],
            'rim_below': rim(range(a - 5, a)), 'rim_above': rim(range(b + 1, b + 6))}


def delta(pair, t, since, source='auto'):
    """the delta proxy: list of (bar close time, bar delta, running CVD) since `since`, from 15m spot bars or the futures bars closed by t"""
    if source == 'auto':
        out = delta(pair, t, since, 'spot')
        return out if any(d for _, d, _ in out) else delta(pair, t, since, 'fut')
    bars = [x for x in D.closed_until(pair, '15', t) if x['time'] >= since] if source == 'spot' else \
        next((b for b in ([x for x in ext_closed(FUT[pair], tf, t) if x['time'] >= since] for tf in ('30', '60')) if b), [])
    tf_ms = 900000 if source == 'spot' else (bars[1]['time'] - bars[0]['time'] if len(bars) > 1 else 1800000)
    out, cvd = [], 0.0
    for x in bars:
        rng = x['high'] - x['low']
        d = float(x.get('volume') or 0.0) * ((x['close'] - x['open']) / rng if rng > 0 else 0.0)
        cvd += d
        out.append((x['time'] + tf_ms, d, cvd))
    return out


def yield_spread(pair, t):
    """US 2Y minus the pair's 2Y at t and its change over one and two weeks: {'spread', 'd1w', 'd2w'}; a rising spread = pressure toward the dollar. DXY: the mean of the two spreads."""
    def one(sym):
        us, ot = ext_closed('TVC:US02Y', 'D', t), ext_closed(sym, 'D', t)
        if len(us) < 12 or len(ot) < 12:
            return None
        at = lambda rows, tt: next((x['close'] for x in reversed(rows) if x['time'] + EXT_TFMS['D'] <= tt), None)
        s = lambda tt: (lambda a, b: None if a is None or b is None else a - b)(at(us, tt), at(ot, tt))
        s0, s1, s2 = s(t), s(t - WEEK_MS), s(t - 2 * WEEK_MS)
        return None if None in (s0, s1, s2) else {'spread': s0, 'd1w': s0 - s1, 'd2w': s0 - s2}
    if pair in Y2:
        return one(Y2[pair])
    both = [r for r in (one(Y2['EURUSD']), one(Y2['GBPUSD'])) if r]
    return {k: sum(r[k] for r in both) / len(both) for k in ('spread', 'd1w', 'd2w')} if both else None


def positioning(pair, t):
    """net noncommercial positions (long - short) of the pair's future as PUBLISHED by t, and the change against the report before: {'net', 'd1w', 'week'}"""
    c = COT[pair]
    L, S = ext_closed(f'COT:{c}_F_NCP_L', 'W', t, COT_PUBLISH_MS - EXT_TFMS['W']), ext_closed(f'COT:{c}_F_NCP_S', 'W', t, COT_PUBLISH_MS - EXT_TFMS['W'])
    if len(L) < 2 or len(S) < 2:
        return None
    net = lambda i: L[i]['close'] - S[i]['close']
    return {'net': net(-1), 'd1w': net(-1) - net(-2), 'week': D.ts(L[-1]['time'])[:10]}


def clocks(date):
    """the day's institutional instants (epoch ms), in local time: London open 08:00 London, New York 08:30, the 10:00 New York option cut, the ECB reference rate 14:15 Frankfurt,
    the London fix 16:00 London (his context document, pillar E 'CLOCK_ANCHORED'; P533 2.2 for the cut)"""
    def ms(tz, h, mi=0):
        return int(dt.datetime(date.year, date.month, date.day, h, mi, tzinfo=ZoneInfo(tz)).timestamp() * 1000)
    return {'london_open': ms('Europe/London', 8), 'ny_open': ms('America/New_York', 8, 30), 'ny_cut': ms('America/New_York', 10), 'ecb_fix': ms('Europe/Berlin', 14, 15),
            'london_fix': ms('Europe/London', 16)}
