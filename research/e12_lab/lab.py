"""Plutus lab: data layer, trading-day clock, resampling, chart renderer.

Conventions (from the canon):
  * Trading day = 17:00 ET -> 17:00 ET, labelled by (t_ET + 7h).date  (Sun 17:00 ET => Monday)
  * Analysis point = Monday 02:00 ET (London pre-open; fixture uses 06:00Z = 07:00 BST = 02:00 ET)
  * Temporal boundary: only bars with t <= anchor exist.
  * 4H candles anchored 17:00 ET (TradingView FX session), wall-clock ET.
"""
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

PIP = 0.0001


def load_eurusd_2017():
    from backtesting.test import EURUSD
    d = EURUSD.copy()
    d.index = d.index.tz_localize("UTC").tz_convert("America/New_York").tz_localize(None)
    d.columns = [c.lower() for c in d.columns]
    return d[["open", "high", "low", "close"]]


def load_fixture(pair, tf, path="/home/user/plutus-vision/fixtures/bars/2026-07-06.json"):
    f = json.load(open(path))
    for c in f["cells"]:
        if c["pair"] == pair and c["timeframe"] == tf:
            df = pd.DataFrame(c["bars"])
            break
    else:
        raise KeyError((pair, tf))
    tcol = [k for k in df.columns if k in ("t", "time", "timestamp", "ts")][0]
    t = df[tcol]
    if t.max() > 1e11:
        t = t / 1000.0
    idx = pd.to_datetime(t, unit="s", utc=True).dt.tz_convert("America/New_York").dt.tz_localize(None)
    df.index = idx
    df = df.rename(columns={k: k.lower() for k in df.columns})
    return df[["open", "high", "low", "close"]].sort_index()


def trading_day(idx):
    return (idx + pd.Timedelta(hours=7)).normalize()


def resample(df, rule):
    """rule: '4h' | '1h' | 'D'. Wall-clock ET, 17:00 anchored."""
    if rule == "D":
        key = trading_day(df.index)
        g = df.groupby(key)
    else:
        origin = pd.Timestamp("2000-01-03 17:00")
        g = df.resample(rule, origin=origin)
    o = g.agg({"open": "first", "high": "max", "low": "min", "close": "last"}).dropna()
    return o


def weeks(df):
    """Return list of Monday dates having a full Mon-Fri session in df (trading-day labels)."""
    td = pd.Series(trading_day(df.index), index=df.index)
    days = td.unique()
    mons = [d for d in days if pd.Timestamp(d).dayofweek == 0]
    out = []
    for m in mons:
        m = pd.Timestamp(m)
        need = [m + pd.Timedelta(days=i) for i in range(5)]
        if all(((td == n).sum() >= 18) for n in need):
            out.append(m)
    return out


def anchor_of(monday):
    return pd.Timestamp(monday) + pd.Timedelta(hours=2)  # Monday 02:00 ET


def pre_anchor(df, monday):
    return df[df.index <= anchor_of(monday)]


def week_slice(df, monday):
    m = pd.Timestamp(monday)
    s = m - pd.Timedelta(hours=7)   # Sun 17:00 ET
    e = m + pd.Timedelta(days=4, hours=17)  # Fri 17:00 ET
    return df[(df.index >= s) & (df.index < e)]


# ---------------------------------------------------------------- plotting
def candles(ax, df, width_frac=0.7, up="#2ea39a", dn="#d6453d"):
    if len(df) == 0:
        return
    x = np.arange(len(df))
    for i, (o, h, l, c) in enumerate(zip(df.open, df.high, df.low, df.close)):
        col = up if c >= o else dn
        ax.plot([i, i], [l, h], color=col, lw=0.8, zorder=3)
        ax.add_patch(Rectangle((i - width_frac / 2, min(o, c)), width_frac, max(abs(c - o), 1e-6),
                               facecolor=col, edgecolor=col, zorder=4))


def xpos(df_index, ts):
    """fractional bar position for timestamp ts within df_index."""
    return float(np.searchsorted(df_index.values, np.datetime64(ts), side="left"))


def draw_zone(ax, idx, lo, hi, t0, t1, color, alpha=0.22, label=None, lw=0.8, ls="-", fs=6.5):
    x0 = xpos(idx, t0) if t0 is not None else 0
    x1 = xpos(idx, t1) if t1 is not None else len(idx) + 6
    ax.add_patch(Rectangle((x0 - 0.5, lo), x1 - x0, hi - lo, facecolor=color, alpha=alpha,
                           edgecolor=color, lw=lw, ls=ls, zorder=1))
    if label:
        ax.text(x1 - 0.5, (lo + hi) / 2, label, fontsize=fs, va="center", ha="right", color="#e8e8e8", zorder=6, clip_on=True)


def style_dark(fig, ax):
    fig.patch.set_facecolor("#0e1117")
    ax.set_facecolor("#0e1117")
    ax.tick_params(colors="#9aa0a6", labelsize=7)
    for s in ax.spines.values():
        s.set_color("#30363d")
    ax.grid(color="#1c222b", lw=0.5)


def time_axis(ax, idx, every=6):
    ticks = list(range(0, len(idx), every))
    ax.set_xticks(ticks)
    ax.set_xticklabels([idx[i].strftime("%a %d %H:%M") if idx[i].hour == 17 or i == 0 else idx[i].strftime("%H:%M")
                        for i in ticks], rotation=60, ha="right")
