"""Engine-2 learning prototype: actual-day shape labeler + doctrine forecaster + comparator."""
import numpy as np
import pandas as pd
from lab import PIP, resample, week_slice, anchor_of
from e1 import zigzag

FAMILY = {"SS": "RANGE", "R": "RANGE", "BS": "DIR", "PBS": "DIR", "WL": "DIR", "RWL": "DIR", "PWL": "DIR"}


# ------------------------------------------------------------------ labeler of ACTUAL price action
def day_stats(seg, A):
    o, c, h, l = seg.open.iloc[0], seg.close.iloc[-1], seg.high.max(), seg.low.min()
    R, net = h - l, c - o
    up, dn = h - o, o - l
    spike_dir = 1 if up >= dn else -1
    E = max(up, dn, 1e-9)
    giveback = (E - spike_dir * net) / E          # 1.0 => closed back at open (or beyond)
    return dict(o=o, c=c, h=h, l=l, R=R, net=net, Rn=R / A, netn=net / A, E=E, spike_dir=spike_dir, giveback=giveback,
                eff=abs(net) / R if R else 0)


def label_days(h1, monday, A):
    out, prev = [], None
    for k in range(5):
        day = pd.Timestamp(monday) + pd.Timedelta(days=k)
        s, e = day - pd.Timedelta(hours=7), day + pd.Timedelta(hours=17)
        seg = h1[(h1.index >= s) & (h1.index < e)]
        if len(seg) < 12:
            out.append(None)
            continue
        st = day_stats(seg, A)
        shape, d = "SS", 0
        if st["E"] >= 0.7 * A and st["giveback"] >= 0.6 and st["R"] >= 0.9 * A:
            shape, d = "WL", st["spike_dir"]
            if prev and prev["shape"] in ("BS", "PBS") and np.sign(st["net"]) == -prev["dir"] and st["eff"] >= 0.4:
                shape, d = "RWL", int(-prev["dir"])
        elif st["eff"] >= 0.5 and st["R"] >= 0.8 * A:
            shape, d = ("PBS" if st["R"] >= 1.6 * A else "BS"), int(np.sign(st["net"]))
            if prev and prev["shape"] in ("BS", "PBS", "WL") and d == -prev["dir"] and shape == "BS":
                shape = "RWL"
        elif st["R"] < 1.0 * A and prev and prev["shape"] in ("BS", "PBS", "WL", "RWL") and st["R"] < 0.8 * A:
            shape, d = "R", int(np.sign(st["net"])) if abs(st["netn"]) > 0.15 else 0
        else:
            shape, d = "SS", 0
        rec = dict(day=day.strftime("%a"), shape=shape, dir=d, **{k_: v for k_, v in st.items() if k_ in ("o", "c", "h", "l", "Rn", "netn", "eff")})
        out.append(rec)
        prev = rec
    return out


def chain_str(labels):
    return " → ".join(f"{x['day']}:{x['shape']}{'' if not x['dir'] else ('↑' if x['dir'] > 0 else '↓')}" if x else "?" for x in labels)


# ------------------------------------------------------------------ forecaster (doctrine rules; deterministic)
def structural(E):
    """AD6: an IP zone must carry a structural anchor (S/D origin or swing LSZ), not pivots alone."""
    keep = []
    for z in E["ips"]:
        fams = " ".join(z.src)
        if any(k in fams for k in ("SD-", "LSZ-")) and z.score >= 4:
            keep.append(z)
    return keep


def pressure_of(E):
    """Recent 4H storyline: direction of last big (2.5 ADR) leg and whether we're in post-leg consolidation."""
    h4 = E["h4"]
    zz = zigzag(h4, 2.5 * E["adr"])
    if len(zz) >= 2:
        last = zz[-1]
        leg_dir = 1 if last[2] == "H" else -1
        bars_since = len(h4) - 1 - last[0]
        # consolidation: last 5 trading days range
        D = E["D"].iloc[-5:]
        rng5 = (D.high.max() - D.low.min()) / E["adr"]
        return dict(leg_dir=leg_dir, bars_since=bars_since, rng5=rng5, zz=zz)
    return dict(leg_dir=0, bars_since=999, rng5=9, zz=zz)


def forecast_week(E):
    """Doctrine v0. Returns dict(days=[(shape,dir)]*5, ceil, floor, notes, target)"""
    spot, A = E["spot"], E["adr"]
    zones = structural(E)
    above = sorted([z for z in zones if z.lo > spot - 0.05 * A], key=lambda z: z.lo)
    below = sorted([z for z in zones if z.hi < spot + 0.05 * A], key=lambda z: -z.hi)
    strong = lambda zs: [z for z in zs if z.score >= 5]
    ceil = (strong(above) or above or [None])[0]
    floor = (strong(below) or below or [None])[0]
    P = pressure_of(E)
    notes = []
    # last two completed daily moves (for post-pierce consolidation rule)
    D = E["D"].iloc[-3:]
    lastd = [(r.close - r.open) / A for r in D.itertuples()]
    strong_moves = sum(1 for x in lastd[-2:] if abs(x) >= 0.55)
    days = [("SS", 0)] * 5
    if ceil is None or floor is None:
        return dict(days=days, ceil=ceil, floor=floor, notes=["no bounding zones"], target=None)
    width = (ceil.lo - floor.hi) / A
    pos = (spot - floor.hi) / max(ceil.lo - floor.hi, 1e-9)
    notes.append(f"range={width:.1f}ADR pos={pos:.2f} ceilZFP={ceil.zfp} floorZFP={floor.zfp} leg={P['leg_dir']:+d} rng5={P['rng5']:.1f}ADR strongMoves2d={strong_moves}")
    # --- decide breakout side: weaker bounding zone fails first; tie -> 4H storyline
    if ceil.zfp > floor.zfp + 5:
        side = 1
    elif floor.zfp > ceil.zfp + 5:
        side = -1
    else:
        side = P["leg_dir"] or (1 if pos > 0.5 else -1)
    # --- liquidity-first rule: whiplash at nearest zone if spot is already within 0.35 ADR of a strong wall
    near_ceil = ceil.lo - spot < 0.35 * A
    near_floor = spot - floor.hi < 0.35 * A
    if width < 1.0:       # tight cage => breakout week
        days = [("SS", 0), ("SS", 0), ("BS", side), ("BS", side), ("R", 0)]
        notes.append("tight cage -> SS,SS then BS")
    elif strong_moves >= 2:   # conservation of energy: 1-2 days consolidation after two piercing moves
        days = [("SS", 0), ("SS", 0), ("SS", 0), ("BS", side), ("R", 0)]
        notes.append("post-pierce consolidation -> SS first")
    else:
        tgt = ceil if side == 1 else floor
        hardwall = tgt.zfp < 20
        d1 = ("SS", 0)
        # Mon/Tue swing scalps inside the range, BS/WL toward the failing side from Wed (+1 day speed rule), then reaction
        react = ("RWL", -side) if hardwall else ("R", 0)
        days = [d1, ("SS", 0), ("WL", side) if hardwall else ("BS", side), react, ("R", 0)]
        notes.append(f"range week: side={side:+d} target ZFP={tgt.zfp} -> {'WL then RWL' if hardwall else 'BS then R'}")
    return dict(days=days, ceil=ceil, floor=floor, notes=notes, target=(ceil if side == 1 else floor), side=side)


# ------------------------------------------------------------------ comparator
def score(fc_days, act):
    """Per-day: family match (RANGE vs DIR) and direction match on directional days. Returns dict."""
    fam_ok = dirs_total = dirs_ok = 0
    n = 0
    for (fs, fd), a in zip(fc_days, act):
        if a is None:
            continue
        n += 1
        fam_ok += (FAMILY[fs] == FAMILY[a["shape"]])
        if FAMILY[a["shape"]] == "DIR":
            dirs_total += 1
            if FAMILY[fs] == "DIR" and fd == a["dir"]:
                dirs_ok += 1
    return dict(n=n, fam_ok=fam_ok, dirs_total=dirs_total, dirs_ok=dirs_ok)
