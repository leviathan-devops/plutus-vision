#!/usr/bin/env python3
"""kill_test.py [--switch mod.NAME=V ...] [PAIR:MONDAY ...] - the charter's kill test (memory/22 T2; operator's context document, invariant 1): a +500-pip shock is added to every bar
that had not closed by an anchor; whatever was decided at that anchor must not change by one byte.
1. Week anchor: the Pine of plutus.run (weekly mode) on the shocked store == on the real store.
2. Daily anchoring: for every trading-day open and London open T of the week, with the shock applied after T: each day's part decided by T (orders, anchor price, alternative state, zone
   adds) and every drawn Engine 2 segment that STARTS by T (cut at T where a later event shortened it) are identical.
tools/leak_check.py removes the later bars; this test corrupts them instead - a tool that reads them cannot pass. Exit code 1 on any difference."""
import sys, os, io, contextlib
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.insert(0, os.path.join(ROOT, 'e1_tool'))
import e1_data as D, plutus, e2_data as E2D

args = sys.argv[1:]
while args and args[0] == '--switch':
    k, v = args[1].split('='); mod, name = k.split('.')
    m_ = sys.modules.get(mod) or __import__(mod); old = getattr(m_, name)
    setattr(m_, name, bool(int(v)) if isinstance(old, bool) else tuple(int(x) for x in v.split(';')) if isinstance(old, tuple) else type(old)(v))
    print(f"switch {mod}.{name} = {getattr(m_, name)!r}"); args = args[2:]
weeks = [a.split(':') for a in args] or [['DXY', '2026-07-06']]
orig = D.bars
orig_ext = E2D.ext_bars
SHOCK = 500
bad = []


def shocked(T, pip):
    d = SHOCK * pip
    def f(p, tf, _o=orig):
        return [x if x['time'] + D.TFMS[tf] <= T else dict(x, open=x['open'] + d, high=x['high'] + d, low=x['low'] + d, close=x['close'] + d, volume=(x.get('volume') or 0) * 7 + 1) for x in _o(p, tf)]
    return f


def run(pair, monday, daily, bars_fn):
    D._cache.clear(); plutus._MEMO.clear(); D.bars = bars_fn
    T_ = getattr(bars_fn, 'T', None)      # the Engine 2 data module's external series (futures, yields, COT) get the same shock: every bar not closed by T is corrupted
    if T_ is not None:
        E2D.ext_bars = lambda sym, tf, _T=T_: [x if x['time'] + E2D.EXT_TFMS[tf] <= _T else dict(x, open=x['open'] * 3 + 1, high=x['high'] * 3 + 1, low=x['low'] * 3 + 1, close=x['close'] * 3 + 1, volume=(x.get('volume') or 0) * 7 + 1) for x in orig_ext(sym, tf)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            r = plutus.run(pair, monday, daily=daily)
    finally:
        D.bars = orig; E2D.ext_bars = orig_ext; D._cache.clear(); plutus._MEMO.clear()
    return r


def segs_by(ch, T):
    out = []
    for sg in (ch.get('segments') or []):
        if sg and sg[0][0] <= T:
            c = plutus._cut([(int(t), float(v)) for t, v in sg], sg[0][0], min(T, sg[-1][0])) if sg[-1][0] > T else [(int(t), float(v)) for t, v in sg]
            out.append([(int(t), round(float(v), 9)) for t, v in c])
    return out


for pair, monday in weeks:
    pip = D.PIP[pair]; b0 = D.boundary_ms(monday); n0 = len(bad)
    # the shock moves every pair's later bars (the DXY master and the Phase 10 source pairs too): each pair by its own pip
    def all_pairs(T):
        fs = {p: shocked(T, D.PIP[p]) for p in D.PIP}
        g = lambda p, tf: fs[p](p, tf)
        g.T = T
        return g
    a = run(pair, monday, False, orig)[3]
    b = run(pair, monday, False, all_pairs(b0))[3]
    if a != b:
        la, lb = a.splitlines(), b.splitlines()
        k = next((i for i, (x, y) in enumerate(zip(la, lb)) if x != y), min(len(la), len(lb)))
        bad.append(f"{pair} {monday}: the week-anchor Pine changes under the shock (first difference at line {k + 1})"); print('KILL', bad[-1], flush=True)
    full = run(pair, monday, True, orig)[1]
    anchors = sorted({D.week_start_ms(monday) + i * 86400000 for i in range(1, 5)} | {D.day_anchor_ms(monday, i) for i in range(1, 5)} | {s[0][0] for s in (full.get('segments') or []) if s and s[0][0] > b0})
    for T in anchors:
        ch = run(pair, monday, True, all_pairs(T))[1]
        i_T = max(0, min(4, (T - D.week_start_ms(monday)) // 86400000))
        for j in range(0, i_T + 1):
            if D.week_start_ms(monday) + j * 86400000 <= T and ch['daily'].get(j) != full['daily'].get(j):
                bad.append(f"{pair} {monday}: day {j} (trading-day-open part) changes under a shock after {D.ts(T)} UTC"); print('KILL', bad[-1], flush=True)
            if j >= 1 and D.day_anchor_ms(monday, j) <= T and ch.get('daily_L', {}).get(j) != full.get('daily_L', {}).get(j):
                bad.append(f"{pair} {monday}: day {j} (London-open part) changes under a shock after {D.ts(T)} UTC"); print('KILL', bad[-1], flush=True)
        if segs_by(ch, T) != segs_by(full, T):
            bad.append(f"{pair} {monday}: drawn segments starting by {D.ts(T)} UTC change under a shock after it"); print('KILL', bad[-1], flush=True)
    if len(bad) == n0:
        print(f"kill_test {pair} {monday}: +{SHOCK}-pip shock after the week anchor and after each of {len(anchors)} later anchors - nothing decided before the shock changed", flush=True)
sys.exit(1 if bad else 0)
