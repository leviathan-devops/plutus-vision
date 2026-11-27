import sys, io, contextlib, re
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import plutus, e1_data as D
DAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')
for m in sys.argv[1:]:
    pair, mon = m.split(':')
    with contextlib.redirect_stdout(io.StringIO()):
        X, E2, E3, src = plutus.run(pair, mon)
    pip = D.PIP[pair]
    b = [x for x in D.bars(pair, '60') if D.boundary_ms(mon) <= x['time'] < D.week_end_ms(mon)]
    w0 = D.week_start_ms(mon)
    A = E2['audit']
    ce = next((a for a in A if a.startswith('Ceiling')), '')
    fl = next((a for a in A if a.startswith('Floor')), '')
    bd = next((a for a in A if a.startswith('Breakout direction')), '')
    cs = next((a for a in A if a.startswith('Current Shape')), '')
    d0 = E2['days'][0]
    lo, hi = d0.get('lo'), d0.get('hi')
    ev = []
    if lo is not None and hi is not None:
        for x in b:
            day = DAYS[min(4, (x['time'] - w0) // 86400000)]
            if x['close'] > hi + 5 * pip and not any(e[0] == 'UP' for e in ev):
                ev.append(('UP', day))
            if x['close'] < lo - 5 * pip and not any(e[0] == 'DN' for e in ev):
                ev.append(('DN', day))
    H, L, C = max(x['high'] for x in b), min(x['low'] for x in b), b[-1]['close']
    fc = ' '.join('+'.join(d['shapes']) + ('' if d['dir'] == 'range' else d['dir'][0]) for d in E2['days'])
    cm = re.search(r'\[(.*?)\] -> (\S+)', ce); fm = re.search(r'\[(.*?)\] -> (\S+)', fl)
    print(f"{mon} box {lo:.3f}-{hi:.3f} ({(hi-lo)/pip:.0f}p) spot {X['spot']:.3f} | C[{cm.group(1) if cm else '?'}]->{cm.group(2) if cm else '?'} F[{fm.group(1) if fm else '?'}]->{fm.group(2) if fm else '?'} | fc: {fc} | ACT: breaks {ev} H+{(H-hi)/pip:.0f} L-{(lo-L)/pip:.0f} close {'above' if C > hi else 'below' if C < lo else 'in'} | {cs[15:60]}")
