"""locator: pair day maps - the DXY chain translated (current) vs the pair's own Engine 2 chain (lead=None)"""
import sys, io, contextlib
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import plutus, e1_data as D, e1_pine as EP, e2_chain as E
def score(pair, mon, E2):
    pip = D.PIP[pair]
    b = [x for x in D.bars(pair, '60') if D.boundary_ms(mon) <= x['time'] < D.week_end_ms(mon)]
    w0 = D.week_start_ms(mon); row = []; n = 0
    for i, day in enumerate(('Mon', 'Tue', 'Wed', 'Thu', 'Fri')):
        xs = [x for x in b if w0 + i * 86400000 <= x['time'] < w0 + (i + 1) * 86400000]
        d = next((q for q in E2['days'] if q['day'] == day), None)
        if not xs or d is None: row.append('-'); continue
        H, L, O, C = max(x['high'] for x in xs), min(x['low'] for x in xs), xs[0]['open'], xs[-1]['close']
        if d['dir'] == 'range': ok = H <= d['hi'] + 10 * pip and L >= d['lo'] - 10 * pip
        else:
            sgn = 1 if d['dir'] == 'up' else -1
            ok = (C - O) * sgn >= 10 * pip or (d['shapes'][-1] in ('RWL', 'WL') and (H - L) >= 20 * pip and (C - O) * sgn > 0)
        n += ok; row.append('+'.join(d['shapes']) + ('' if d['dir'] == 'range' else d['dir'][0]) + (' ok' if ok else ' X'))
    return n, ' | '.join(row)
ta = tb = tn = 0
for m in sys.argv[1:]:
    pair, mon = m.split(':')
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            X, E2, E3, src = plutus.run(pair, mon)
            own = E.build(pair, mon, X, None)
    except Exception as e:
        print(pair, mon, 'ERR', repr(e)[:80]); continue
    a, ra = score(pair, mon, E2); b_, rb = score(pair, mon, own)
    ta += a; tb += b_; tn += 5
    print(f"{pair} {mon}: translated {a}/5 [{ra}]\n{'':>19}own        {b_}/5 [{rb}]")
print(f"translated {ta}/{tn} | own {tb}/{tn}")
