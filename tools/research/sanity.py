"""sanity.py [maps...] - BUG LOCATOR ONLY: structural checks on every emitted setup of the given maps (default: every DXY week with a sidecar file from 2026-04-06). No market outcome is read.
Checks: SL / entry / TP order; printed RRR vs the order's own prices (a blended RRR needs the order itself at TP >= 1.2 x SL, E3C:343); SL distance inside [4, 36] pips (E3C:289-294);
two orders of one day and direction within half a pip; more than 11 counted setups (R-07); a Monday limit order already through the anchor price."""
import sys, os, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'e1_tool'))
import plutus, e1_data as D
maps = sys.argv[1:] or ['DXY:' + f[:-5] for f in sorted(os.listdir(os.path.join(HERE, '..', '..', 'sidecar', 'out'))) if f[:4] == '2026' and f[:10] >= '2026-04-06' and f.endswith('.json') and len(f) == 15]
bad = 0
for m in maps:
    pair, mon = m.split(':')
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            X, E2, E3, src = plutus.run(pair, mon)
    except Exception as e:
        print(f"{pair} {mon}: RUN ERROR {e!r}"[:200]); bad += 1; continue
    pip = D.PIP[pair]
    S = [s for s in E3['setups'] if not s.get('clone')]
    out = []
    for s in S:
        e, sl, tp = s['entry'], s['sl'], s['tp']
        lng = s['dir'] == 'LONG'
        if not ((sl < e < tp) if lng else (tp < e < sl)):
            out.append(f"{s['id']}: order of SL / entry / TP wrong ({s['dir']} {e:.5f} / {sl:.5f} / {tp:.5f})"); continue
        own = abs(tp - e) / abs(e - sl)
        if abs(own - s['rrr']) > 0.06 * max(own, s['rrr']) and 'blended' not in s.get('why', ''):
            out.append(f"{s['id']}: printed RRR {s['rrr']} vs prices {own:.2f}")
        if 'blended' in s.get('why', '') and own < 1.2 - 1e-9:
            out.append(f"{s['id']}: blended {s['rrr']} on an order of {own:.2f}")
        d = abs(e - sl) / pip
        if not (4 - 1e-6 <= d <= 36 + 1e-6):
            out.append(f"{s['id']}: SL distance {d:.1f} pips")
        if s['day'] == 'Mon' and not s.get('alt') and s.get('category') not in ('Transition', 'Reinforcement') and ((e > X['spot'] + 0.5 * pip) if lng else (e < X['spot'] - 0.5 * pip)):
            out.append(f"{s['id']}: Monday {s['dir']} limit {e:.5f} already through the anchor price {X['spot']:.5f}")
    for i, a in enumerate(S):
        for b in S[i + 1:]:
            if a['day'] == b['day'] and a['dir'] == b['dir'] and bool(a.get('alt')) == bool(b.get('alt')) and abs(a['entry'] - b['entry']) < 0.5 * pip:
                out.append(f"{a['id']} / {b['id']}: two {a['dir']} orders of {a['day']} at {a['entry']:.5f} (SL {a['sl']:.5f} / {b['sl']:.5f})")
    n = len([s for s in S if not s.get('alt')])
    if n > 11:
        out.append(f"{n} counted setups (> 11)")
    bad += len(out)
    print(f"{pair} {mon}: {len(S)} setups ({n} counted)" + (''.join('\n    ' + o for o in out) if out else ' ok'))
print(f"SANITY findings {bad}")
