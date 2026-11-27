"""e2loc.py [maps...] - BUG LOCATOR ONLY for Engine 2 (uses the week's bars; never imported by the tool, never a verdict): per map, the forecast day tags against that day's candles with
a plain reading of the outside reviewers' rules - SS: the day's high / low stay inside the forecast box +-10 pips; a directional tag (last shape of the day BS / PBS / RWL / WL / R with
a direction): the day closes at least 10 pips from its open in that direction, or (a composite ending in RWL / WL) shows a 20-pip leg that way."""
import sys, os, io, contextlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'e1_tool'))
import plutus, e1_data as D
maps = sys.argv[1:] or open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'maps16.txt')).read().split()
tot = [0, 0]
for m in maps:
    pair, mon = m.split(':')
    with contextlib.redirect_stdout(io.StringIO()):
        X, E2, E3, src = plutus.run(pair, mon)
    pip = D.PIP[pair]
    b = [x for x in D.bars(pair, '60') if D.boundary_ms(mon) <= x['time'] < D.week_end_ms(mon)]
    w0 = D.week_start_ms(mon)
    row, ok_n = [], 0
    for i, day in enumerate(('Mon', 'Tue', 'Wed', 'Thu', 'Fri')):
        xs = [x for x in b if w0 + i * 86400000 <= x['time'] < w0 + (i + 1) * 86400000]
        d = next((q for q in E2['days'] if q['day'] == day), None)
        if not xs or d is None:
            row.append(f"{day} -"); continue
        H, L, O, C = max(x['high'] for x in xs), min(x['low'] for x in xs), xs[0]['open'], xs[-1]['close']
        if d['dir'] == 'range':
            ok = H <= d['hi'] + 10 * pip and L >= d['lo'] - 10 * pip
        else:
            sgn = 1 if d['dir'] == 'up' else -1
            leg = (H - L) >= 20 * pip
            ok = (C - O) * sgn >= 10 * pip or (d['shapes'][-1] in ('RWL', 'WL') and leg and (C - O) * sgn > 0)
        ok_n += ok
        row.append(f"{day} {'+'.join(d['shapes'])}{'' if d['dir'] == 'range' else ' ' + d['dir']} {'ok' if ok else 'X'}")
    tot[0] += ok_n; tot[1] += 5
    print(f"{pair} {mon}: {ok_n}/5 | " + ' | '.join(row))
print(f"E2 LOCATOR {tot[0]}/{tot[1]}")
