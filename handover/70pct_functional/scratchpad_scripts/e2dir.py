import sys, io, contextlib, re
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import plutus, e1_data as D, e2_chain as E
DAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')
tally = {}
for m in sys.argv[1:]:
    pair, mon = m.split(':')
    with contextlib.redirect_stdout(io.StringIO()):
        X, E2, E3, src = plutus.run(pair, mon)
    pip = D.PIP[pair]
    b = [x for x in D.bars(pair, '60') if D.boundary_ms(mon) <= x['time'] < D.week_end_ms(mon)]
    w0 = D.week_start_ms(mon)
    d0 = E2['days'][0]
    lo, hi = d0.get('lo'), d0.get('hi')
    first = None
    for x in b:
        if x['close'] > hi + 5 * pip: first = ('up', DAYS[min(4, (x['time'] - w0) // 86400000)]); break
        if x['close'] < lo - 5 * pip: first = ('down', DAYS[min(4, (x['time'] - w0) // 86400000)]); break
    C = b[-1]['close']
    net = 'up' if C > hi else 'down' if C < lo else 'in'
    tr = E.trend_4h(pair, mon)
    st, why = E.storyline(pair, mon, X['spot'], X['U'])
    pb, votes = E.pressure_bias(pair, mon, D.boundary_ms(mon) - 2 * 86400000)
    B = E.bounds(X)
    chk, v, dis = E.six_check(X, pair, mon, 'up', B, None, {})
    sv = {n.split()[0]: d for n, d in v}
    act = first[0] if first else None
    print(f"{mon} first {first} net {net} | fc_bdir {E2.get('bdir')} | trend4h {tr} story {st} ({why[:28]}) press {pb} | BoM {sv.get('BoM')} sweep {sv.get('liquidity')}")
    if act:
        for k, val in (('trend', tr), ('story', st), ('press', pb), ('bom', sv.get('BoM')), ('sweep', sv.get('liquidity')), ('fc', E2.get('bdir'))):
            t = tally.setdefault(k, [0, 0, 0])
            if val is None: t[2] += 1
            elif val == act: t[0] += 1
            else: t[1] += 1
print({k: f"{v[0]} right / {v[1]} wrong / {v[2]} none" for k, v in tally.items()})
