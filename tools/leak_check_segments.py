#!/usr/bin/env python3
"""leak_check_segments.py [--switch mod.NAME=V ...] PAIR:MONDAY ... - the temporal anchor for the DRAWN Engine 2 line under daily anchoring (plan memory/16 gate G2 for M2 / D-147).
tools/leak_check.py proves the Pine at the week anchor and each day's ORDER parts; this proves every drawn line segment: for every anchor T of the week (each trading-day open,
each London open 02:00 NY, each cut 10:00 NY) the run on a bar store CUT at T (every bar not closed by T removed) must draw exactly the same segments that START at or before T as
the run on the full store. Exit code 1 on any difference. Separate file so tools/leak_check.py stays as it is."""
import sys, os, io, contextlib, datetime as dt
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.insert(0, os.path.join(ROOT, 'e1_tool'))
import e1_data as D, plutus, e2_chain as E2

args = sys.argv[1:]
while args and args[0] == '--switch':
    k, v = args[1].split('=')
    mod, name = k.split('.')
    m_ = sys.modules.get(mod) or __import__(mod)
    old = getattr(m_, name)
    setattr(m_, name, bool(int(v)) if isinstance(old, bool) else tuple(int(x) for x in v.split(';')) if isinstance(old, tuple) else type(old)(v))
    print(f"switch {mod}.{name} = {getattr(m_, name)!r}")
    args = args[2:]
orig = D.bars
bad = []


def run(cut_at=None):
    D._cache.clear(); plutus._MEMO.clear()
    D.bars = orig if cut_at is None else (lambda p, tf, _o=orig, _t=cut_at: [x for x in _o(p, tf) if x['time'] + D.TFMS[tf] <= _t])
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            ch = plutus.run(pair, monday, daily=True)[1]
    finally:
        D.bars = orig; D._cache.clear(); plutus._MEMO.clear()
    return [[(int(t), round(float(v), 9)) for t, v in sg] for sg in (ch.get('segments') or [])]


for m in args:
    pair, monday = m.split(':')
    full = run()
    m0 = dt.date.fromisoformat(monday)
    anchors = sorted({D.week_start_ms(monday) + i * 86400000 for i in range(1, 5)} | {D.day_anchor_ms(monday, i) for i in range(5)}
                     | {E2._ms(m0 + dt.timedelta(days=i), h) for i in range(5) for h in getattr(E2, 'MICRO_ANCHOR_HOURS', (10,))})
    n_bad = 0
    for T in anchors:
        cut = run(T)
        a = [s for s in full if s and s[0][0] <= T]
        b = [s for s in cut if s and s[0][0] <= T]
        if a != b:
            n_bad += 1
            k = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
            bad.append(f"{pair} {monday}: drawn segments starting by {D.ts(T)} UTC change when the bars after it are removed (first differing segment #{k}: "
                       f"{(a[k][0] if k < len(a) else None)} vs {(b[k][0] if k < len(b) else None)})")
            print('LEAK-SEGMENTS', bad[-1], flush=True)
    if not n_bad:
        print(f"leak_check_segments {pair} {monday}: {len(full)} drawn segments; identical for all {len(anchors)} anchors (trading-day opens, London opens, the micro-path session anchors)", flush=True)
sys.exit(1 if bad else 0)
