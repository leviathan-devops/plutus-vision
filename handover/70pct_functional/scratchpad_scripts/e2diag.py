import sys, io, contextlib
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import plutus, e1_data as D
for m in sys.argv[1:]:
    pair, mon = m.split(':')
    with contextlib.redirect_stdout(io.StringIO()):
        X, E2, E3, src = plutus.run(pair, mon)
    pip = D.PIP[pair]
    b = [x for x in D.bars(pair, '60') if D.boundary_ms(mon) <= x['time'] < D.week_end_ms(mon)]
    w0 = D.week_start_ms(mon)
    print('=====', pair, mon, 'spot', X.get('spot'))
    for a in E2["audit"]:
        if any(k in a for k in ('Ceiling', 'Floor', 'ceiling', 'floor', 'Breakout direction', 'Current', 'Trading Speed', 'Key rule', '->', 'Cage', 'bound')):
            print('   ', a[:330])
    for i, day in enumerate(('Mon', 'Tue', 'Wed', 'Thu', 'Fri')):
        xs = [x for x in b if w0 + i * 86400000 <= x['time'] < w0 + (i + 1) * 86400000]
        d = next((q for q in E2['days'] if q['day'] == day), None)
        if xs and d:
            print(f"   {day} {'+'.join(d['shapes'])} {d['dir']} box {d.get('lo')}-{d.get('hi')} | O {xs[0]['open']} H {max(x['high'] for x in xs)} L {min(x['low'] for x in xs)} C {xs[-1]['close']}")
