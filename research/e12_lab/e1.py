"""Engine-1 learning prototype (zones). Scale-free: every threshold is a multiple of ADR / ATR4H.

Missing dimensions in this sandbox (no data source reachable): option expiries, analyst commentary.
They score 0 and are flagged MISSING; pressure degree thresholds are re-calibrated for the reduced max score.
"""
from dataclasses import dataclass, field
import numpy as np
import pandas as pd
from lab import PIP, resample, trading_day


# ------------------------------------------------------------------ helpers
def adr(D, n=20):
    r = (D.high - D.low).iloc[-n:]
    return float(r.mean())


def atr(df, n=30):
    pc = df.close.shift()
    tr = pd.concat([df.high - df.low, (df.high - pc).abs(), (df.low - pc).abs()], axis=1).max(axis=1)
    return float(tr.iloc[-n:].mean())


def fractal_pivots(df, n):
    h, l = df.high.values, df.low.values
    ph, pl = [], []
    for i in range(n, len(df) - n):
        if h[i] == max(h[i - n:i + n + 1]) and h[i] > max(np.r_[h[i - n:i], h[i + 1:i + n + 1]]):
            ph.append(i)
        if l[i] == min(l[i - n:i + n + 1]) and l[i] < min(np.r_[l[i - n:i], l[i + 1:i + n + 1]]):
            pl.append(i)
    return ph, pl


def zigzag(df, thr):
    """Standard threshold zigzag on high/low. Returns [(idx, price, 'H'|'L')], alternating."""
    h, l = df.high.values, df.low.values
    n = len(df)
    pts = []
    if n < 3:
        return pts
    hi_i = lo_i = 0
    trend = 0
    for i in range(1, n):
        if trend == 0:
            if h[i] > h[hi_i]:
                hi_i = i
            if l[i] < l[lo_i]:
                lo_i = i
            if h[hi_i] - l[lo_i] >= thr:
                if lo_i < hi_i:
                    pts.append((lo_i, l[lo_i], "L"))
                    trend = 1
                else:
                    pts.append((hi_i, h[hi_i], "H"))
                    trend = -1
                hi_i = lo_i = i
                if trend == 1:
                    hi_i = int(np.argmax(h[pts[-1][0]:i + 1])) + pts[-1][0]
                else:
                    lo_i = int(np.argmin(l[pts[-1][0]:i + 1])) + pts[-1][0]
        elif trend == 1:
            if h[i] > h[hi_i]:
                hi_i = i
            if h[hi_i] - l[i] >= thr:
                pts.append((hi_i, h[hi_i], "H"))
                trend = -1
                lo_i = int(np.argmin(l[hi_i:i + 1])) + hi_i
        else:
            if l[i] < l[lo_i]:
                lo_i = i
            if h[i] - l[lo_i] >= thr:
                pts.append((lo_i, l[lo_i], "L"))
                trend = 1
                hi_i = int(np.argmax(h[lo_i:i + 1])) + lo_i
    return pts


# ------------------------------------------------------------------ zone objects
@dataclass
class Zone:
    kind: str                 # 'IP' | 'LSZ' | 'SD'
    lo: float
    hi: float
    side: str = ""            # 'supply' | 'demand' | 'mid'
    cls: str = ""             # BoM | MoM | ''
    state: str = ""           # VIRGIN | ACTIVE-1 | ACTIVE-2 | DEPLETED | BROKEN
    touches: int = 0
    reactions: int = 0
    formed: pd.Timestamp = None
    tf: str = "4H"
    score: float = 0.0
    degree: str = ""
    zfp: float = 50.0
    src: list = field(default_factory=list)
    name: str = ""
    events: list = field(default_factory=list)

    @property
    def mid(self):
        return (self.lo + self.hi) / 2


# ------------------------------------------------------------------ S/D (Fire)
def sd_zones(h4, A, atr4):
    """4H origin-candle supply/demand with BoM/MoM and mitigation tracking."""
    small = zigzag(h4, 1.0 * A)
    big = zigzag(h4, 2.5 * A)
    big_idx = [p[0] for p in big]
    zones = []
    for k, (i0, p0, kind) in enumerate(small):
        if i0 < 2 or i0 > len(h4) - 4:
            continue
        direction = 1 if kind == "L" else -1
        # first impulse candle j
        j = None
        for jj in range(max(i0 - 1, 0), min(i0 + 6, len(h4))):
            o, c = h4.open.iloc[jj], h4.close.iloc[jj]
            if direction * (c - o) >= 0.9 * atr4:
                j = jj
                break
        o_i = (j - 1) if j is not None else i0
        o_i = max(i0 - 1, min(o_i, i0 + 4))
        row = h4.iloc[o_i]
        lo, hi = float(row.low), float(row.high)
        if hi - lo > 0.8 * A or hi - lo < 0.02 * A:
            continue
        near_big = any(abs(i0 - b) <= 3 for b in big_idx)
        z = Zone("SD", lo, hi, side="demand" if direction == 1 else "supply",
                 cls="BoM" if near_big else "MoM", formed=h4.index[o_i], src=[f"4H-origin@{h4.index[o_i]:%m-%d %H:%M}"])
        # mitigation scan after the leg has left: start after first bar beyond impulse
        start = (j if j is not None else i0) + 2
        touches, reactions, broken = 0, 0, False
        events = []
        inside = False
        t = start
        while t < len(h4):
            r = h4.iloc[t]
            overlap = (r.low <= hi) and (r.high >= lo)
            far_edge_break = (r.close < lo) if z.side == "demand" else (r.close > hi)
            if overlap and not inside:
                inside = True
                touches += 1
                # reaction = moves away >=0.5A within next 12 bars w/o closing through far edge
                seg = h4.iloc[t:t + 13]
                if z.side == "demand":
                    away = seg.high.max() - hi
                    thru = (seg.close < lo).any()
                else:
                    away = lo - seg.low.min()
                    thru = (seg.close > hi).any()
                react_ = bool(away >= 0.5 * A and not thru)
                events.append(dict(n=touches, t=h4.index[t], react=react_, pierce=bool(thru)))
                if react_:
                    reactions += 1
            if not overlap:
                inside = False
            if far_edge_break:
                broken = True
                break
            t += 1
        z.touches, z.reactions = touches, reactions
        z.events = events
        z.state = "BROKEN" if broken else ("VIRGIN" if touches == 0 else "ACTIVE-1" if touches == 1 else
                                           "ACTIVE-2" if touches == 2 else "DEPLETED")
        zones.append(z)
    return zones


# ------------------------------------------------------------------ LSZ (Earth)
def lsz_zones(D, h4, A):
    """Liquidity sweep zones from D1 rejection swings (Step 0) + 4H minor swings (Step 0h)."""
    zs = []
    ph, pl = fractal_pivots(D.iloc[-95:], 2)
    Dd = D.iloc[-95:]
    for i in pl:
        r = Dd.iloc[i]
        wick = min(r.open, r.close) - r.low
        close_upper = (r.close - r.low) >= 0.5 * (r.high - r.low)
        pri = "ACTIVE" if (wick >= 0.3 * A and close_upper) else "STANDARD"
        zs.append(Zone("LSZ", float(r.low), float(r.low + 0.12 * A), side="demand", state=pri,
                       formed=Dd.index[i], tf="D1", src=[f"D1-swing-low {Dd.index[i]:%m-%d}" + ("+wick" if pri == "ACTIVE" else "")]))
    for i in ph:
        r = Dd.iloc[i]
        wick = r.high - max(r.open, r.close)
        close_lower = (r.high - r.close) >= 0.5 * (r.high - r.low)
        pri = "ACTIVE" if (wick >= 0.3 * A and close_lower) else "STANDARD"
        zs.append(Zone("LSZ", float(r.high - 0.12 * A), float(r.high), side="supply", state=pri,
                       formed=Dd.index[i], tf="D1", src=[f"D1-swing-high {Dd.index[i]:%m-%d}" + ("+wick" if pri == "ACTIVE" else "")]))
    # minor 4H swings
    h = h4.iloc[-400:]
    ph4, pl4 = fractal_pivots(h, 4)
    for i in pl4:
        r = h.iloc[i]
        zs.append(Zone("LSZ", float(r.low), float(r.low + 0.10 * A), side="demand", state="MINOR", formed=h.index[i], tf="4H",
                       src=[f"4H-swing-low {h.index[i]:%m-%d %H}"]))
    for i in ph4:
        r = h.iloc[i]
        zs.append(Zone("LSZ", float(r.high - 0.10 * A), float(r.high), side="supply", state="MINOR", formed=h.index[i], tf="4H",
                       src=[f"4H-swing-high {h.index[i]:%m-%d %H}"]))
    # swept? a zone is SWEPT if price traded through its extreme after formation (then it's spent)
    for z in zs:
        after = h4[h4.index > z.formed]
        if len(after):
            if z.side == "demand" and after.low.min() < z.lo - 0.02 * A:
                z.touches = 1  # swept
            if z.side == "supply" and after.high.max() > z.hi + 0.02 * A:
                z.touches = 1
    return zs


# ------------------------------------------------------------------ pivots / rounds / MAs (technical)
def pivot_levels(D, anchor_day_idx=None):
    """Weekly pivots from the previous completed trading week + daily pivots from last 3 completed days."""
    out = []
    # weekly: group trading days into Monday-labelled weeks
    wk_key = D.index - pd.to_timedelta(D.index.dayofweek, unit="D")
    W = D.groupby(wk_key).agg({"open": "first", "high": "max", "low": "min", "close": "last"})
    last_w = W.iloc[-1]  # D already truncated to completed days; last week may be partial (current Monday) -> use previous if partial
    cur_monday = wk_key[-1]
    prev = W[W.index < cur_monday].iloc[-1] if (W.index < cur_monday).any() else last_w

    def sets(H, L, C, tag):
        PP = (H + L + C) / 3
        rng = H - L
        res = []
        res += [(PP, f"{tag}-cPP"), (2 * PP - L, f"{tag}-cR1"), (2 * PP - H, f"{tag}-cS1"), (PP + rng, f"{tag}-cR2"), (PP - rng, f"{tag}-cS2")]
        res += [(PP + 0.382 * rng, f"{tag}-fR1"), (PP - 0.382 * rng, f"{tag}-fS1"), (PP + 0.618 * rng, f"{tag}-fR2"), (PP - 0.618 * rng, f"{tag}-fS2")]
        res += [(C + rng * 1.1 / 4, f"{tag}-camR3"), (C - rng * 1.1 / 4, f"{tag}-camS3"), (C + rng * 1.1 / 2, f"{tag}-camR4"), (C - rng * 1.1 / 2, f"{tag}-camS4")]
        return res
    out += sets(prev.high, prev.low, prev.close, "W")
    for k in (1, 2, 3):
        if len(D) >= k:
            r = D.iloc[-k]
            out += sets(r.high, r.low, r.close, f"D{k}")
    out += [(float(prev.high), "prevWeekHigh"), (float(prev.low), "prevWeekLow"), (float(prev.close), "prevWeekClose")]
    return out


def round_levels(lo, hi):
    out = []
    p = np.floor(lo / 0.0025) * 0.0025
    while p <= hi:
        pips = round(p / PIP)
        if pips % 100 == 0:
            out.append((p, "big-figure", 2.0))
        elif pips % 50 == 0:
            out.append((p, "half-figure", 2.0))
        elif pips % 25 == 0:
            out.append((p, "quarter-figure", 1.0))
        p += 0.0025
    return out


def ma_levels(h4):
    out = []
    for n in (50, 100, 200):
        if len(h4) >= n:
            out.append((float(h4.close.ewm(span=n, adjust=False).mean().iloc[-1]), f"EMA{n}-4H"))
    return out


# ------------------------------------------------------------------ assembly
def degree(score):
    # recalibrated: options+analyst dimensions are MISSING here, so max reachable ~ 9-10 not 14
    if score >= 8: return "EXTREME"
    if score >= 6.5: return "HEAVY"
    if score >= 5: return "MODERATE-HEAVY"
    if score >= 4: return "MODERATE"
    if score >= 2.5: return "LIGHT"
    return "MINIMAL"


ZFP_BY_DEG = {"EXTREME": 8, "HEAVY": 18, "MODERATE-HEAVY": 28, "MODERATE": 38, "LIGHT": 50, "MINIMAL": 65}


def build_e1(h1, monday, verbose=False):
    """Everything computed strictly from bars <= Monday 02:00 ET."""
    from lab import anchor_of
    a = anchor_of(monday)
    h1 = h1[h1.index <= a]
    h4 = resample(h1, "4h")
    D = resample(h1, "D")
    D = D[D.index < pd.Timestamp(monday)]            # completed trading days only
    A = adr(D)
    at4 = atr(h4)
    spot = float(h1.close.iloc[-1])
    sd = sd_zones(h4, A, at4)
    lsz = lsz_zones(D, h4, A)
    piv = pivot_levels(D)
    rounds = round_levels(spot - 5 * A, spot + 5 * A)
    mas = ma_levels(h4)

    # ---- clustering of levels
    levels = []   # (price, family, label, weight)
    for z in sd:
        if z.state == "BROKEN":
            continue
        for p in (z.lo, z.hi):
            levels.append((p, "struct", f"SD-{z.cls}-{z.side}", 2.0 if z.cls == "BoM" else 1.0, z))
    for z in lsz:
        if z.touches:  # swept
            continue
        w = 2.0 if z.state == "ACTIVE" else (1.0 if z.state == "STANDARD" else 0.5)
        levels.append((z.lo, "struct", f"LSZ-{z.side}", w, z))
        levels.append((z.hi, "struct", f"LSZ-{z.side}", w, z))
    for p, lab in piv:
        levels.append((p, "tech", lab, 1.0, None))
    for p, lab in mas:
        levels.append((p, "tech", lab, 1.0, None))
    for p, lab, w in rounds:
        levels.append((p, "psy", lab, w, None))
    levels = [l for l in levels if spot - 4 * A <= l[0] <= spot + 4 * A]
    levels.sort(key=lambda x: x[0])
    clusters, cur = [], []
    gap = 0.10 * A
    for l in levels:
        if cur and l[0] - cur[-1][0] > gap:
            clusters.append(cur)
            cur = []
        cur.append(l)
    if cur:
        clusters.append(cur)

    ips = []
    for cl in clusters:
        fam = {}
        for p, f, lab, w, z in cl:
            fam.setdefault(f, []).append((p, lab, w, z))
        ntech = len({lab for p, lab, w, z in fam.get("tech", [])})
        tech = 0 if ntech == 0 else (1 if ntech == 1 else 2)
        st_w = max([w for p, lab, w, z in fam.get("struct", [])], default=0)
        struct = 2 if st_w >= 2 else (1 if st_w >= 1 else (0.5 if st_w > 0 else 0))
        psy = max([w for p, lab, w, z in fam.get("psy", [])], default=0)
        # repeated magnets: >=2 distinct dated swing sources
        swing_dates = {z.formed.normalize() for p, lab, w, z in fam.get("struct", []) if z is not None and z.kind == "LSZ"}
        bonus = 0.0
        if len(swing_dates) >= 3:
            bonus = 2.0
        elif len(swing_dates) == 2:
            bonus = 1.5
        # tier-1 overlap: LSZ cluster overlapping an unbroken BoM S/D
        kinds = {(z.kind, z.cls) for p, lab, w, z in fam.get("struct", []) if z is not None}
        if ("LSZ", "") in kinds and ("SD", "BoM") in kinds:
            bonus += 1.0
        score = tech + struct + psy + 1.0 + bonus        # +1 regime neutral; options/analyst MISSING
        lo = min(p for p, *_ in cl)
        hi = max(p for p, *_ in cl)
        if hi - lo < 0.06 * A:
            c = (hi + lo) / 2
            lo, hi = c - 0.03 * A, c + 0.03 * A
        srcs = sorted({lab for p, f, lab, w, z in cl})
        # reaction-depleted S/D reduce strength
        dep = sum(1 for p, f, lab, w, z in cl if z is not None and z.kind == "SD" and z.state == "DEPLETED")
        score -= 0.5 * dep
        z = Zone("IP", lo, hi, side="mid", score=score, degree=degree(score), zfp=ZFP_BY_DEG[degree(score)], src=srcs)
        z.name = f"{z.degree[:4]} {lo:.4f}-{hi:.4f}"
        ips.append(z)
    return dict(spot=spot, adr=A, atr4=at4, h4=h4, D=D, h1=h1, sd=sd, lsz=lsz, ips=ips, anchor=a,
                tech=dict(piv=piv, mas=mas))
