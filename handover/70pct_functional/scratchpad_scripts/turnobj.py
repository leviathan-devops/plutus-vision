"""locator: for each leg start of legs.py (1H zigzag 30 pips, 3+ hours), which Engine 1 objects stood at the turn (within TOL pips, correct side)"""
import sys, io, contextlib, subprocess, re, os
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import plutus, e1_data as D
TOL = float(os.environ.get('TOL', 4))
tot = {}
N = 0
for m in sys.argv[1:]:
    pair, mon = m.split(':')
    with contextlib.redirect_stdout(io.StringIO()):
        X, E2, E3, src = plutus.run(pair, mon)
    pip = D.PIP[pair]
    out = subprocess.run([sys.executable, '/home/user/plutus-vision/tools/research/legs.py', pair, mon], capture_output=True, text=True).stdout
    objs = []
    for z in X['zones']: objs.append(('IP', z['bot'], z['top'], None))
    for z in X.get('infill', []): objs.append(('IF', z['bot'], z['top'], None))
    for q in X['sd']:
        if q.get('broken') is None: objs.append((f"SD{q['tf']}{q['kind'] if 'kind' in q else ''}", q['bot'], q['top'], 'S' if q['type'] == 'Supply' else 'L'))
    for tf, v in X['v1'].items():
        for b in v['liquidity']: objs.append((f"LQ{tf}", b['bot'], b['top'], None))
        for b in v['order_blocks']: objs.append((f"OB{tf}", b['bot'], b['top'], None))
    for l in X['lsz']:
        if not l['swept']: objs.append(('LSZ', l['bot'], l['top'], 'S' if l['side'] == 'Supply-side' else 'L'))
    for d in X.get('discovery', []):
        p = d.get('p', d.get('level'))
        if p is not None: objs.append(('DISC', p, p, None))
    print(f"== {pair} {mon}")
    for l in out.splitlines():
        mm = re.match(r'\s+(\d+)\. ([LS]) ([\d.]+) (\w{3} \d\d:\d\d) -> ([\d.]+) .*?\((\d+)p\)\s+(CAUGHT|MISSED)', l)
        if not mm: continue
        side, p, t, sz, res = mm.group(2), float(mm.group(3)), mm.group(4), int(mm.group(6)), mm.group(7)
        if t == 'Mon 06:00': continue                      # the leg running at the anchor
        N += 1
        near = [(n, b, tp) for n, b, tp, sd in objs if b - TOL * pip <= p <= tp + TOL * pip and (sd is None or sd == side)]
        kinds = sorted({n for n, _, _ in near})
        for k in {re.sub(r'\d+', '', n) if not n.startswith(('SD', 'LQ', 'OB')) else n[:2] for n in kinds}: tot[k] = tot.get(k, 0) + 1
        tot['ANY'] = tot.get('ANY', 0) + (1 if near else 0)
        tot['CAUGHT'] = tot.get('CAUGHT', 0) + (res == 'CAUGHT')
        print(f"  {side} {p} {t} {sz}p {res}: {kinds if kinds else 'NO OBJECT'}")
print('legs', N, tot)
