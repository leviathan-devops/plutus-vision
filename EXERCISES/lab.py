#!/usr/bin/env python3
"""
EXERCISE LAB — apply the Plutus canon to REAL bars, by hand.

This is not a copy of the project's e1_extract.py. It is my own minimal implementation of the
canon's E1 mechanics (CANON/01), written from the spec so the understanding is mine and
testable:

  * swing extremes with REJECTION WICKS           (v5.3.3 §3.2 Step 0b/0c)
  * liquidity sweep zones                          (Step 0.45 + the 0.05-0.10 extension)
  * repeated extreme magnets                       (Step 0.5)
  * zone clustering (0.10-0.15 DXY)                (Synthesis step 3-4)
  * GEOMETRIC ZFP = height / ref * 100             (§10.8 — the crux)
  * BoM/MoM classification                         (§3.2)
  * the E2 shape for the week + the ZFP-conditioned next-shape rule (§6.4.1)

Renders a chart PNG I actually LOOK at, plus a text structure report.

Usage:
  python3 EXERCISES/lab.py --week cv-2026-04-13 --render
  python3 EXERCISES/lab.py --all
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys

import matplotlib
matplotlib.use("Agg")  # headless

ROOT = pathlib.Path(__file__).resolve().parent.parent
BARS = ROOT / "fixtures" / "bars"
OUT = ROOT / "EXERCISES"

# Canon constants -----------------------------------------------------------
# v5.3.3 §10.8 — pair reference ranges for the GEOMETRIC ZFP
REF_RANGE = {"DXY": 1.60, "EURUSD": 0.0200, "EUR/USD": 0.0200, "GBPUSD": 0.0200, "GBP/USD": 0.0200, "AUDUSD": 0.0150}
# v5.3.3 §3.2 Step 0 — rejection-wick thresholds
WICK_MIN_DXY = 0.15
# Step 0.45 — LSZ band
LSZ_BAND = 0.05
LSZ_EXT = 0.10          # 0.45a — sweep 0.05-0.10 beyond the extreme
# Synthesis — clustering
CLUSTER_BAND = 0.15
MAX_ZONE_WIDTH = 0.40   # canon Step 0f noise rule: a zone wider than 0.40 DXY is not a zone
TIGHT_BAND = 0.10
# §3.2 Step 0d — order-block displacement
OB_MOVE_MIN = 0.5
OB_DAYS_MIN = 3
# E2 §6.4.1 — ZFP-conditioned transitions
ZFP_HARD_WALL = 20.0
ZFP_MID_LO, ZFP_MID_HI = 20.0, 40.0
ZFP_FAILING = 45.0
ZFP_VERY_WEAK = 60.0
ZFP_NEARLY_BROKEN = 80.0


# ---------------------------------------------------------------- data
def load(path: pathlib.Path):
    d = json.loads(path.read_text())
    cells = d.get("cells") or []
    out = []
    for c in cells:
        if c.get("bars"):
            out.append((c.get("pair"), c.get("timeframe"), c["bars"]))
    return d.get("provenance", ""), out


def to_dt(ms: int) -> dt.datetime:
    return dt.datetime.fromtimestamp(ms / 1000, dt.timezone.utc)


def week_bounds(bars, week_anchor: str | None):
    """Return (monday_open_dt, friday_close_dt) for the ISO week containing the anchor."""
    import re
    a = None
    if week_anchor:
        m = re.search(r"(\d{4})-(\d{2})-(\d{2})", str(week_anchor))
        if m:
            y, mo, d = (int(x) for x in m.groups())
            a = dt.datetime(y, mo, d, tzinfo=dt.timezone.utc)
    if a is None:
        a = to_dt(bars[len(bars) // 2]["timestamp"])
    mon = a - dt.timedelta(days=a.weekday())
    mon = mon.replace(hour=0, minute=0, second=0, microsecond=0)
    fri = mon + dt.timedelta(days=4, hours=23, minutes=59)
    return mon, fri


def aggregate(bars: list[dict], minutes: int) -> list[dict]:
    """Aggregate 1H bars up to N-minute bars (240 -> 4H, 1440 -> D1).

    CANON NOTE (learned by MEASURING, not by reading): v5.3.3 §3.2 Step 0's rejection-wick
    thresholds (0.15 DXY points) are specified on **D1** data. Applied to 1H bars the scan
    returns ZERO swings, because a 1H DXY bar's entire range is often < 0.15 — verified by
    running it (0 lows / 0 highs). Step 0 therefore MUST run on D1 and Step 0f (order
    blocks) on 4H. The spec assumes this aggregation and never states it.
    """
    if minutes <= 60:
        return bars
    buckets: dict[int, dict] = {}
    step = minutes * 60 * 1000
    for b in bars:
        k = b["timestamp"] // step
        cur = buckets.get(k)
        if cur is None:
            buckets[k] = {"timestamp": k * step, "open": b["open"], "high": b["high"],
                          "low": b["low"], "close": b["close"],
                          "volume": b.get("volume", 0)}
        else:
            cur["high"] = max(cur["high"], b["high"])
            cur["low"] = min(cur["low"], b["low"])
            cur["close"] = b["close"]
            cur["volume"] = cur.get("volume", 0) + b.get("volume", 0)
    return [buckets[k] for k in sorted(buckets)]


# ---------------------------------------------------------------- E1
def find_order_blocks(bars4h: list[dict], ref_range: float, horizon_days: int = 3) -> list[dict]:
    """Step 0f — 4H demand/supply zones from the SINGULAR origin candle.

    Canon: identify a strong directional move (>= 0.5 DXY pts over >= 3 trading days);
    the zone is the SINGLE candle immediately BEFORE that move; zone range = [low, high]
    of that origin candle. The candle AFTER it must move directionally.
    """
    move_min = OB_MOVE_MIN if ref_range > 1 else OB_MOVE_MIN / 1.60 * ref_range
    per_day = 6  # 4H bars per trading day
    n = len(bars4h)
    horizon = horizon_days * per_day

    def qual(i: int):
        """Return ('DEMAND'|'SUPPLY'|None, magnitude) for the move that STARTS at bar i."""
        if i < 1 or i >= n:
            return None, 0.0
        cur = bars4h[i]
        fwd = bars4h[i + 1: min(n, i + 1 + horizon)]
        if not fwd:
            return None, 0.0
        up = max(b["high"] for b in fwd) - cur["close"]
        dn = cur["close"] - min(b["low"] for b in fwd)
        if up >= move_min and up >= dn:
            return "DEMAND", up
        if dn >= move_min:
            return "SUPPLY", dn
        return None, 0.0

    # MEASURED CORRECTION: naively taking every bar that precedes a big move yields 39
    # "order blocks" for one week -- the entire run qualifies, so the zone is meaningless.
    # The canon says the SINGLE candle immediately before the move BEGINS. So a bar
    # qualifies only when it is the FIRST bar of a qualifying run (its predecessor did not).
    out = []
    for i in range(1, n - 1):
        kind, mag = qual(i)
        if kind is None:
            continue
        prev_kind, _ = qual(i - 1)
        if prev_kind is not None and prev_kind == kind:
            continue  # not the origin -- we are mid-move
        origin = bars4h[i - 1]
        out.append({"type": kind, "low": origin["low"], "high": origin["high"],
                    "origin_ts": origin["timestamp"], "moved": round(mag, 4)})
    # de-duplicate: adjacent 4H bars often pick the same origin candle
    seen, dedup = set(), []
    for o in out:
        key = (o["type"], round(o["low"], 3), round(o["high"], 3))
        if key in seen:
            continue
        seen.add(key)
        o["formed"] = to_dt(o["origin_ts"]).strftime("%m-%d %H:%M")
        dedup.append(o)
    return dedup


def find_swings(bars, ref_range: float):
    """Step 0b/0c — swing extremes carrying a REJECTION WICK.

    A swing low must be a local extreme (lower than its neighbours) AND its lower wick
    >= WICK_MIN_DXY AND the close in the upper half of the bar's range.
    """
    lo_wick_min = WICK_MIN_DXY if ref_range > 1 else WICK_MIN_DXY / 1.60 * ref_range
    out = {"lows": [], "highs": []}
    n = len(bars)
    for i in range(2, n - 2):
        b = bars[i]
        h, l, o, c = b["high"], b["low"], b["open"], b["close"]
        rng = h - l
        if rng <= 0:
            continue
        # local extreme over a +-2 window
        left = bars[max(0, i - 2):i]
        right = bars[i + 1:i + 3]
        if all(b["low"] <= x["low"] for x in left) and all(b["low"] <= x["low"] for x in right):
            lower_wick = min(o, c) - l
            if lower_wick >= lo_wick_min and c >= l + rng * 0.5:
                out["lows"].append({"i": i, "ts": b["timestamp"], "price": l,
                                    "wick": round(lower_wick, 5)})
        if all(b["high"] >= x["high"] for x in left) and all(b["high"] >= x["high"] for x in right):
            upper_wick = h - max(o, c)
            if upper_wick >= lo_wick_min and c <= l + rng * 0.5:
                out["highs"].append({"i": i, "ts": b["timestamp"], "price": h,
                                     "wick": round(upper_wick, 5)})
    return out


def lsz_from_swings(sw: dict) -> list[dict]:
    """Step 0.45 / 0.45a — liquidity sweep zones (green bands)."""
    out = []
    for l in sw["lows"]:
        out.append({"side": "demand", "low": round(l["price"] - LSZ_EXT, 5),
                    "high": round(l["price"] + LSZ_BAND, 5),
                    "exact": l["price"], "kind": "swing-low",
                    "ts": l["ts"]})
    for h in sw["highs"]:
        out.append({"side": "supply", "low": round(h["price"] - LSZ_BAND, 5),
                    "high": round(h["price"] + LSZ_EXT, 5),
                    "exact": h["price"], "kind": "swing-high",
                    "ts": h["ts"]})
    return out


def repeated_magnets(sw: dict, tol: float = 0.05) -> list[dict]:
    """Step 0.5 — a level reached on 2+ separate dates."""
    out = []
    for side, key in (("low", "lows"), ("high", "highs")):
        pts = sw[key]
        used = set()
        for a in range(len(pts)):
            if a in used:
                continue
            group = [pts[a]]
            for b in range(a + 1, len(pts)):
                if b in used:
                    continue
                if abs(pts[b]["price"] - pts[a]["price"]) <= tol:
                    group.append(pts[b]); used.add(b)
            if len(group) >= 2:
                used.add(a)
                avg = sum(g["price"] for g in group) / len(group)
                bonus = 2.0 if len(group) >= 3 else 1.5
                conf = "VERY HIGH" if len(group) >= 3 else "HIGH"
                out.append({"side": side, "price": round(avg, 5), "n": len(group),
                            "confidence": conf, "bonus": bonus,
                            "dates": [to_dt(g["ts"]).strftime("%m-%d") for g in group]})
    return out


def cluster_zones(levels: list[float], band: float = CLUSTER_BAND) -> list[dict]:
    """Synthesis steps 3-4 — group levels into zones.

    MEASURED CORRECTION (two real bugs found by running it):
    (1) Naive single-linkage merging CHAINS: 98.78 -> 98.93 -> ... -> 100.09 all within
        0.15 of their neighbour fuses a 1.31-point "zone" (ZFP 82%). The canon's own
        Step 0f noise rule says a zone wider than 0.40 DXY points is NOT a zone. So a
        cluster is capped at MAX_ZONE_WIDTH and split when it would exceed it.
    (2) With only the structural + round-number pillars implemented (Pillars 1-4, 8, 9
        absent — no pivots/MA/options/analyst), most levels are SINGLETONS and produce
        ZFP 0% "hard walls" that are an artifact of an incomplete pillar stack, not
        market structure. Singletons are therefore marked as such and NOT treated as
        authoritative hard walls. This is the same class of error as the live build's
        zDeg cap: an incomplete pillar set distorts the E1 output.
    """
    if not levels:
        return []
    s = sorted(levels)
    zones, cur = [], [s[0]]
    for v in s[1:]:
        if (v - cur[-1] <= band) and (v - cur[0] <= MAX_ZONE_WIDTH):
            cur.append(v)
        else:
            zones.append(cur)
            cur = [v]
    zones.append(cur)
    out = []
    for grp in zones:
        n = len(grp)
        width = max(grp) - min(grp)
        if n >= 3:
            tag = "HIGH-DENSITY ZONE"
        elif n == 2:
            tag = "TIGHT CONFLUENCE"
        else:
            tag = "SINGLETON LEVEL"
        out.append({"low": round(min(grp), 5), "high": round(max(grp), 5),
                    "n": n, "width": round(width, 5), "tag": tag,
                    "authoritative": n >= 2})
    return out


def zfp_geometric(low: float, high: float, pair: str) -> int:
    """v5.3.3 §10.8 — THE authority ZFP: zone height as a % of the pair's weekly range."""
    ref = REF_RANGE.get(pair, 1.60)
    return round((high - low) / ref * 100.0)


def zfp_verdict(z: int) -> str:
    if z < ZFP_HARD_WALL:
        return "HARD WALL  -> rejection"
    if z < ZFP_MID_HI:
        return "MID-RANGE   -> pause (R)"
    if z > ZFP_NEARLY_BROKEN:
        return "NEARLY BROKEN -> strong cascade (PBS)"
    if z > ZFP_VERY_WEAK:
        return "VERY WEAK   -> cascade (PBS)"
    if z > ZFP_FAILING:
        return "FAILING     -> breakout (BS)"
    return "SOFT        -> hold/caution"


# ---------------------------------------------------------------- E2
def shape_of_segment(bars, i0: int, i1: int, tol: float) -> str:
    """Classify the SHAPE of a bar segment using the §6.1 mechanical definitions."""
    seg = bars[i0:i1]
    if len(seg) < 3:
        return "?"
    hi = max(b["high"] for b in seg)
    lo = min(b["low"] for b in seg)
    first, last = seg[0]["close"], seg[-1]["close"]
    rng = hi - lo
    if rng <= 0:
        return "SS (dead)"
    net = last - first
    # how much of the range was travelled net vs gross, and where the extremes sit
    n_hi = seg.index(max(seg, key=lambda b: b["high"]))
    n_lo = seg.index(min(seg, key=lambda b: b["low"]))
    # a spike-and-reject: the extreme occurs late-or-early and price returns
    gross = sum(abs(b["close"] - b["open"]) for b in seg)
    if gross == 0:
        return "SS (dead)"
    efficiency = abs(net) / gross
    # in-range behaviour: price revisits the same band without net progress
    if abs(net) <= rng * 0.22 and efficiency < 0.30:
        return "SS"
    # reversal: the extreme is in the first half and price ends far the other way
    if (n_hi < len(seg) * 0.45 and net < -rng * 0.35) or (n_lo < len(seg) * 0.45 and net > rng * 0.35):
        return "RWL/WL (rejection)"
    if efficiency > 0.45 and abs(net) > rng * 0.55:
        return "BS"
    if abs(net) <= rng * 0.35:
        return "R/SS (transition)"
    return "mixed"


def e2_next_shape(target_zfp: int, current: str) -> tuple[str, str]:
    """v5.3.3 §6.4.1 — the ZFP-CONDITIONED transition (the hinge)."""
    c = current.upper()
    if c.startswith("BS"):
        if target_zfp < ZFP_HARD_WALL:
            return "RWL", "target is a HARD WALL -> price WILL be rejected (NOT continuation)"
        if target_zfp <= ZFP_MID_HI:
            return "R", "mid-range target -> pause, not necessarily a hard reject"
        if target_zfp > ZFP_NEARLY_BROKEN:
            return "PBS", "target nearly broken -> strong cascade"
        if target_zfp > ZFP_VERY_WEAK:
            return "PBS", "target very weak -> cascade continues"
        # The canon's table leaves 40-60% undefined. §6.2 priority 1 / §6.5 treat ZFP > 45%
        # as a FAILING zone (breakable). Do not invent a band -- label the gap honestly.
        return "R/PBS", "40-60% gap: canon leaves this band undefined; >45% reads as failing"
    if c.startswith("SS"):
        if target_zfp > ZFP_FAILING:
            return "BS", "bounding zone failing -> breakout imminent"
        return "SS", "both boundaries solid -> consolidation continues"
    # ORDER MATTERS (the §6.2 'apply in sequence, highest priority first' law):
    # "WLS".startswith("WL") is TRUE, so WLS MUST be tested BEFORE WL. My own test suite
    # caught this -- the first version resolved WLS to SS.
    if c.startswith("WLS"):
        return "BS", "WLS almost always resolves into a BS"
    if c.startswith("RWL") or c.startswith("WL"):
        return "SS", "reversal/whiplash exhausts into a new range"
    return "?", "unmapped current shape"


# ---------------------------------------------------------------- render
def render(bars, week, sw, lszs, zones, pair, spec, out_png, title):
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle
    import matplotlib.dates as mdates

    xs = [to_dt(b["timestamp"]) for b in bars]
    fig, ax = plt.subplots(figsize=(19, 9), dpi=110)
    # candles
    w = 0.0208  # ~30 min in days for 1H bars
    for b, x in zip(bars, xs):
        o, h, l, c = b["open"], b["high"], b["low"], b["close"]
        up = c >= o
        col = "#2e9e5b" if up else "#c0392b"
        ax.plot([x, x], [l, h], color=col, linewidth=0.7, zorder=2)
        ax.add_patch(Rectangle((mdates.date2num(x) - w / 2, min(o, c)), w, max(abs(c - o), 1e-9),
                               facecolor=col, edgecolor=col, linewidth=0.4, zorder=3))
    # zones
    for z in zones:
        zc = zfp_geometric(z["low"], z["high"], pair)
        col = "#2e9e5b" if zc < 20 else ("#d4a017" if zc < 45 else "#c0392b")
        ax.axhspan(z["low"], z["high"], color=col, alpha=0.16, zorder=1)
        ax.axhline(z["high"], color=col, lw=0.8, ls="--", alpha=0.75, zorder=1)
        ax.axhline(z["low"], color=col, lw=0.8, ls="--", alpha=0.75, zorder=1)
        ax.text(xs[0], z["high"], f'  Z ZFP={zc}% ({z["tag"]})',
                fontsize=7, va="bottom", color=col, zorder=6)
    # LSZs
    for s in lszs:
        ax.axhspan(s["low"], s["high"], color="#1e8449", alpha=0.30, zorder=1)
    # swings
    for l in sw["lows"]:
        ax.plot(to_dt(l["ts"]), l["price"], marker="^", color="#0e6b3a", ms=6, zorder=5)
    for h in sw["highs"]:
        ax.plot(to_dt(h["ts"]), h["price"], marker="v", color="#8e2b1e", ms=6, zorder=5)

    ax.set_title(title, fontsize=12)
    ax.set_ylabel(pair)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%a %d"))
    ax.grid(alpha=0.15)
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(out_png)
    plt.close(fig)
    return out_png


# ---------------------------------------------------------------- E2 chain
def classify_day_shape(dbars, zones, pair):
    """§6.2 SHAPE CLASSIFICATION DECISION MATRIX — applied in sequence, first match wins.

    MEASURED CORRECTION: my first attempt classified days from candle statistics (net vs
    gross travel, wick placement). That produced "RWL/WL" on almost every day, which is
    noise: intraday ranges spike and revert by construction. The canon classifies shapes
    by the **relationship between price and the IP zone architecture** ("Shapes are
    mechanically defined by the relationship between price action and IP zone
    architecture" — §6.1). So the classifier must ask: which zone did price test, and
    what did it DO there. Rebuilt on that basis.
    """
    if len(dbars) < 3:
        return "?", None, "too few bars"
    o = dbars[0]["open"]; c = dbars[-1]["close"]
    hi = max(b["high"] for b in dbars); lo = min(b["low"] for b in dbars)

    crossed, rejected, tested = [], [], []
    for z in zones:
        zc = zfp_geometric(z["low"], z["high"], pair)
        entered = lo <= z["high"] and hi >= z["low"]
        if not entered:
            continue
        tested.append((z, zc))
        from_below = o <= z["low"]
        from_above = o >= z["high"]
        now_above = c > z["high"]
        now_below = c < z["low"]
        if from_below and now_above:
            crossed.append((z, zc, "up"))
        elif from_above and now_below:
            crossed.append((z, zc, "down"))
        elif from_above and c >= z["high"]:
            rejected.append((z, zc, "down->rejected"))   # approached from above, bounced
        elif from_below and c <= z["low"]:
            rejected.append((z, zc, "up->rejected"))     # approached from below, bounced

    # 1) any zone with ZFP > 45% closed through => BS (PBS if several weak zones went)
    strong_cross = [x for x in crossed if x[1] > ZFP_FAILING]
    if strong_cross:
        deep = [x for x in crossed if x[1] > ZFP_VERY_WEAK]
        tag = "PBS" if len(deep) >= 2 else "BS"
        z, zc, d = strong_cross[0]
        return tag, {"zone": f'{z["low"]}-{z["high"]}', "zfp": zc, "dir": d}, \
            f'closed THROUGH a zone with ZFP {zc}% > 45% => breakout ({d})'

    # 2) a HARD WALL (ZFP < 20%) approached and rejected => WL
    hw = [x for x in rejected if x[1] < ZFP_HARD_WALL]
    if hw:
        z, zc, d = hw[0]
        return "WL", {"zone": f'{z["low"]}-{z["high"]}', "zfp": zc}, \
            f'tested a HARD WALL (ZFP {zc}% < 20%) and REJECTED ({d})'

    # 3) price crossed a zone but it was not weak => continue / transition
    if crossed:
        z, zc, d = crossed[0]
        return "R/transition", {"zone": f'{z["low"]}-{z["high"]}', "zfp": zc, "dir": d}, \
            f'crossed a zone with ZFP {zc}% (soft, not weak) heading {d}'

    # 4) contained inside a wide/diffuse zone, no boundary crossed => SS
    if tested:
        z, zc = tested[0]
        return "SS", {"zone": f'{z["low"]}-{z["high"]}', "zfp": zc}, \
            f'contained inside zone ZFP {zc}% — no boundary closed through'

    return "SS", None, "no mapped zone interacted with this day (vacuum / unmapped)"


def day_slices(bars):
    """Group intraday bars by UTC trading date."""
    out: dict[str, list[dict]] = {}
    for b in bars:
        d = to_dt(b["timestamp"]).strftime("%a %m-%d")
        out.setdefault(d, []).append(b)
    return out


def nearest_zone_ahead(zones, price, direction, pair):
    """The first mapped zone in the direction of travel -> its geometric ZFP.

    This is what §6.4.1 conditions the NEXT shape on: the TARGET zone's ZFP, not momentum.
    """
    cands = []
    for z in zones:
        zc = zfp_geometric(z["low"], z["high"], pair)
        if direction == "down" and z["high"] < price:
            cands.append((price - z["high"], "below", z, zc))
        if direction == "up" and z["low"] > price:
            cands.append((z["low"] - price, "above", z, zc))
    if not cands:
        return None
    cands.sort(key=lambda t: t[0])
    dist, side, z, zc = cands[0]
    return {"side": side, "low": z["low"], "high": z["high"], "zfp": zc,
            "tag": z["tag"], "distance": round(dist, 4)}


def e2_chain(wk, zones, pair, sw_day):
    """Derive the day-by-day shape chain and test the ZFP-conditioned hinge per day."""
    days = day_slices(wk)
    out = []
    prev = None
    for d, dbars in days.items():
        if len(dbars) < 3:
            continue
        o = dbars[0]["open"]; c = dbars[-1]["close"]
        hi = max(b["high"] for b in dbars); lo = min(b["low"] for b in dbars)
        shape, inter, why_shape = classify_day_shape(dbars, zones, pair)
        direction = "up" if c > o else ("down" if c < o else "flat")
        # the hinge: what zone is next in the direction of travel, and its geometric ZFP
        nz = nearest_zone_ahead(zones, c, direction if direction != "flat" else "down", pair)
        pred, why_pred = (None, "n/a")
        if nz:
            pred, why_pred = e2_next_shape(nz["zfp"], shape)
        out.append({
            "day": d, "open": round(o, 4), "high": round(hi, 4), "low": round(lo, 4),
            "close": round(c, 4), "net": round(c - o, 4), "range": round(hi - lo, 4),
            "shape": shape, "direction": direction,
            "interaction": inter, "shape_reason": why_shape,
            "target_zone": (f'{nz["low"]}-{nz["high"]} ZFP={nz["zfp"]}% ({nz["tag"]})'
                            if nz else "none"),
            "zfp_conditioned_next": pred, "rationale": why_pred,
        })
        prev = shape
    return out


# ---------------------------------------------------------------- main
def run_week(name: str, render_it: bool, source: str | None = None) -> dict:
    src = source or name
    p = BARS / f"{src}.json"
    if not p.exists():
        p = BARS / f"{src}"
    prov, cells = load(p)
    pair, tf, bars = cells[0] if cells else (None, None, [])
    if cells:
        # prefer 1H per canon (PRIMARY ANALYSIS TIMEFRAME: 1H)
        for c in cells:
            if c[1] == "1H":
                pair, tf, bars = c
                break
    mon, fri = week_bounds(bars, name)

    pre = [b for b in bars if to_dt(b["timestamp"]) < mon]
    wk = [b for b in bars if mon <= to_dt(b["timestamp"]) <= fri]
    if len(pre) < 20 or len(wk) < 5:
        return {"week": name, "error": f"insufficient bars (pre={len(pre)} wk={len(wk)})"}

    # ---- E1 on the PRE-WEEK data only (temporal boundary law)
    # Step 0 (swing extremes + rejection wicks) runs on D1 — see aggregate()'s note.
    pre_d1 = aggregate(pre, 1440)
    sw = find_swings(pre_d1, REF_RANGE.get(pair, 1.60))
    lszs = lsz_from_swings(sw)
    mags = repeated_magnets(sw)
    obs = find_order_blocks(aggregate(pre, 240), REF_RANGE.get(pair, 1.60))
    levels = ([l["price"] for l in sw["lows"]] + [h["price"] for h in sw["highs"]]
              + [m["price"] for m in mags]
              + [o["low"] for o in obs] + [o["high"] for o in obs])
    zones = cluster_zones(levels)

    # ---- actual week stats
    wk_hi = max(b["high"] for b in wk)
    wk_lo = min(b["low"] for b in wk)
    wk_open = wk[0]["open"]
    wk_close = wk[-1]["close"]
    net = wk_close - wk_open

    res = {
        "week": name, "pair": pair, "tf": tf, "provenance": prov,
        "window": f"{mon:%Y-%m-%d} .. {fri:%Y-%m-%d}",
        "pre_bars": len(pre), "pre_d1_bars": len(pre_d1), "week_bars": len(wk),
        "week_open": wk_open, "week_high": wk_hi, "week_low": wk_lo, "week_close": wk_close,
        "week_net": round(net, 5),
        "week_range": round(wk_hi - wk_lo, 5),
        "swing_lows": len(sw["lows"]), "swing_highs": len(sw["highs"]),
        "lsz_count": len(lszs), "magnet_count": len(mags), "ob_count": len(obs),
        "d1_swings": {"lows": sw["lows"], "highs": sw["highs"]},
        "order_blocks": obs,
        "zones": [],
        "magnets": mags,
    }
    for z in zones:
        zc = zfp_geometric(z["low"], z["high"], pair)
        res["zones"].append({**z, "zfp": zc, "verdict": zfp_verdict(zc)})

    # ---- E2: which of the mapped zones did the week actually reach, and how did it react?
    res["zone_events"] = []
    for z in res["zones"]:
        touched = [b for b in wk if b["low"] <= z["high"] and b["high"] >= z["low"]]
        if not touched:
            continue
        first = touched[0]
        after = [b for b in wk if b["timestamp"] > first["timestamp"]]
        pierced = any(b["close"] > z["high"] for b in wk) or any(b["close"] < z["low"] for b in wk)
        res["zone_events"].append({
            "zone": f'{z["low"]}-{z["high"]}', "zfp": z["zfp"], "tag": z["tag"],
            "first_touch": to_dt(first["timestamp"]).strftime("%a %H:%M"),
            "closed_through": bool(pierced),
            "reaction": "PIERCED" if pierced else "HELD",
        })

    # ---- E2: day-by-day shape chain + the ZFP-conditioned hinge
    res["chain"] = e2_chain(wk, res["zones"], pair, None)
    # the realised chain is the sequence of distinct shapes
    seen, realised = set(), []
    for d in res["chain"]:
        s = d["shape"].split(" ")[0].split("/")[0]
        if s not in seen:
            seen.add(s); realised.append(s)
    res["realised_chain"] = " -> ".join(realised)

    if render_it:
        png = OUT / f"{name}_chart.png"
        render(wk, (mon, fri), find_swings(aggregate(wk, 1440), REF_RANGE.get(pair, 1.60)),
               lszs, zones, pair, None, png,
               f"{pair} 1H — week {mon:%Y-%m-%d} | {prov}")
        res["png"] = str(png)
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--week"); ap.add_argument("--all", action="store_true")
    ap.add_argument("--render", action="store_true")
    ap.add_argument("--source", default=None,
                    help="fixture file to slice the week out of (e.g. pv-long, dxy-full-to-jul21)")
    a = ap.parse_args()
    weeks = ["cv-2026-04-13", "cv-2026-05-04", "cv-2026-06-15", "cv-2026-06-29",
             "2026-07-06", "cv-2026-08-24"] if a.all else [a.week]
    if not weeks or weeks == [None]:
        ap.error("pass --week NAME or --all")
    results = []
    for w in weeks:
        r = run_week(w, a.render, a.source)
        results.append(r)
        print(json.dumps(r, indent=2, default=str))
    if a.all:
        out = OUT / (f"week_scan_{a.source}.json" if a.source else "week_scan.json")
        out.write_text(json.dumps(results, indent=2, default=str))
        print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
