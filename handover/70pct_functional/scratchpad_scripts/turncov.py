"""locator: per object class, share of leg turns within TOL pips vs the share of the week's price range such objects cover (+-TOL) - a class is informative only when hits >> coverage"""
import sys, io, contextlib, subprocess, re, os
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import plutus, e1_data as D
TOL = float(os.environ.get('TOL', 3))
agg = {}
for m in sys.argv[1:]:
    pair, mon = m.split(':')
    with contextlib.redirect_stdout(io.StringIO()):
        X, E2, E3, src = plutus.run(pair, mon)
    pip = D.PIP[pair]
    b = [x for x in D.bars(pair, '60') if D.boundary_ms(mon) <= x['time'] < D.week_end_ms(mon)]
    lo, hi = min(x['low'] for x in b), max(x['high'] for x in b)
    out = subprocess.run([sys.executable, '/home/user/plutus-vision/tools/research/legs.py', pair, mon], capture_output=True, text=True).stdout
    turns = []
    for l in out.splitlines():
        mm = re.match(r'\s+(\d+)\. ([LS]) ([\d.]+) (\w{3} \d\d:\d\d)', l)
        if mm and mm.group(4) != 'Mon 06:00': turns.append((mm.group(2), float(mm.group(3))))
    cls = {}
    for z in X['zones']: cls.setdefault('IP', []).append((z['bot'], z['top'], None))
    for q in X['sd']:
        if q.get('broken') is None and q['mit'] <= 1: cls.setdefault('SD' + q['tf'] + q.get('kind', ''), []).append((q['bot'], q['top'], 'S' if q['type'] == 'Supply' else 'L'))
    for tf, v in X['v1'].items():
        for x in v['liquidity']: cls.setdefault('LQ' + tf, []).append((x['bot'], x['top'], None))
        for x in v['order_blocks']: cls.setdefault('OB' + tf, []).append((x['bot'], x['top'], None))
    for l in X['lsz']:
        if not l['swept']: cls.setdefault('LSZ', []).append((l['bot'], l['top'], 'S' if l['side'] == 'Supply-side' else 'L'))
    n = 400
    grid = [lo + (hi - lo) * i / (n - 1) for i in range(n)]
    for k, zs in cls.items():
        cov = sum(1 for p in grid if any(bt - TOL * pip <= p <= tp + TOL * pip for bt, tp, sd in zs)) / n
        hit = sum(1 for sd0, p in turns if any(bt - TOL * pip <= p <= tp + TOL * pip and (sd is None or sd == sd0) for bt, tp, sd in zs))
        a = agg.setdefault(k, [0, 0, 0.0])
        a[0] += hit; a[1] += len(turns); a[2] += cov * len(turns)
for k in sorted(agg, key=lambda k: -(agg[k][0] / max(agg[k][2], 1e-9))):
    h, n_, c = agg[k]
    print(f"{k:<10} turns hit {h:>2}/{n_} = {h / n_:.0%} | chance (coverage) {c / n_:.0%} | lift {h / max(c, 1e-9):.2f}")
