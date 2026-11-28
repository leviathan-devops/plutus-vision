"""e2grade.py [--maps golden|check|all|PAIR:MONDAY,...] [--out FILE.json] [-v] - THE ENGINE 2 GRADER of the charter (memory/22 S-a, T4; operator M-77: 'time-aligned grading replaces pips ...
everything is based on mechanics'). LOCATOR: it reads the bars after each anchor to measure; never imported by the tool.
A FORECAST TURN = a vertex of the drawn Engine 2 line where its direction reverses: (kind high / low, time span, the Engine 1 zone it stands on).
An ACTUAL TURN = a 30-minute candle whose high (low) is the extreme of the 2 hours before and the 2 hours after it (no pip threshold).
  HIT         an actual turn of the same kind within +-2 h of the vertex, with its extreme inside the vertex's Engine 1 zone (3-pip edge tolerance, goal prompt S2)
  WRONG ZONE  a turn of that kind within +-2 h, at another zone        WRONG TIME  a turn of that kind at that zone the same trading day, outside +-2 h        NONE  neither
Also: of the actual turns, the share that was forecast (same rule); hourly correlation of the line with the hourly closes; weekly net direction; day tags right (e2forensic rule).
PLUTUS_SWITCHES='mod.NAME=1,...' sets module switches (as tools/research/devset.py). Prints an order fingerprint per map (entry / stop / TP list) so two runs can be compared for identical orders."""
import sys, os, io, json, hashlib, contextlib, argparse, datetime as dt
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'e1_tool'))
import plutus, e1_data as D

GOLD = ('2026-07-06',)
CHECK = ('2026-04-13', '2026-04-20', '2026-05-18', '2026-10-05')
PAIRS = ('DXY', 'EURUSD', 'GBPUSD')
H2 = 2 * 3600000
ap = argparse.ArgumentParser()
ap.add_argument('--maps', default='all'); ap.add_argument('--out', default=None); ap.add_argument('-v', action='store_true')
A = ap.parse_args()
weeks = {'golden': GOLD, 'check': CHECK, 'all': GOLD + CHECK}.get(A.maps)
MAPS = [(p, w) for w in weeks for p in PAIRS] if weeks else [tuple(m.split(':')) for m in A.maps.split(',')]
for kv in filter(None, os.environ.get('PLUTUS_SWITCHES', '').split(',')):
    k, v = kv.split('='); mod, name = k.split('.')
    m_ = sys.modules.get(mod) or __import__(mod)
    old = getattr(m_, name)
    setattr(m_, name, bool(int(v)) if isinstance(old, bool) else int(v) if isinstance(old, int) else float(v) if isinstance(old, float) else tuple(int(x) for x in v.split(';')) if isinstance(old, tuple) else v)
    print(f"switch {mod}.{name} = {getattr(m_, name)!r} (was {old!r})")


def zones_of(X):
    """every Engine 1 zone as (bot, top, label), in naming priority: pressure zones, supply / demand 4H -> 15m, V1 4H bands, V1 1H rungs, sweep zones"""
    z = [(q['bot'], q['top'], q['name']) for q in X.get('zones', []) if q.get('drawn')]
    for tf in ('240', '60', '30', '15'):
        z += [(q['bot'], q['top'], q.get('label', tf)) for q in X.get('sd', []) if q['tf'] == tf]
    z += [(b['bot'], b['top'], 'V1 4H liquidity') for b in X['v1']['240']['liquidity']] + [(b['bot'], b['top'], 'V1 1H rung') for b in X['v1']['60']['liquidity']]
    z += [(l['bot'], l['top'], 'sweep zone') for l in X.get('lsz', [])]
    return z


def vertices(segments, nodes=None):
    """the line's turns: (kind, t_from, t_to, price). A flat stretch between an up-move and a down-move is one vertex spanning the stretch."""
    out = []
    for sg in segments:
        pts = [(int(t), float(v)) for t, v in sg]
        moves = []                                           # (t0, t1, p0, p1) of every non-flat piece
        for (ta, pa), (tb, pb) in zip(pts, pts[1:]):
            if abs(pb - pa) > 1e-9: moves.append((ta, tb, pa, pb))
        for (a0, a1, p0, p1), (b0, b1, q0, q1) in zip(moves, moves[1:]):
            if (p1 - p0) * (q1 - q0) < 0:
                out.append(('H' if p1 > p0 else 'L', a1, b0, p1))
    return out


def actual_turns(bars, t0, t1):
    out = []
    for i in range(4, len(bars) - 4):
        x = bars[i]
        if not (t0 <= x['time'] < t1): continue
        w = bars[i - 4:i + 5]
        if x['high'] == max(y['high'] for y in w): out.append(('H', x['time'] + 900000, x['high']))
        if x['low'] == min(y['low'] for y in w): out.append(('L', x['time'] + 900000, x['low']))
    return out


def pearson(a, b):
    n = len(a)
    if n < 3: return None
    ma, mb = sum(a) / n, sum(b) / n
    va, vb = sum((x - ma) ** 2 for x in a), sum((y - mb) ** 2 for y in b)
    return None if va <= 0 or vb <= 0 else sum((x - ma) * (y - mb) for x, y in zip(a, b)) / (va * vb) ** 0.5


rows = []
for pair, mon in MAPS:
    plutus._MEMO.clear()
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            X, ch, R, pine = plutus.run(pair, mon, daily=True)
    except Exception as ex:
        print(f"{pair} {mon}: RUN ERROR {ex!r}"[:200], flush=True); rows.append({'pair': pair, 'mon': mon, 'error': repr(ex)}); continue
    pip = D.PIP[pair]; tol = 3 * pip; b0, w1, w0 = D.boundary_ms(mon), D.week_end_ms(mon), D.week_start_ms(mon)
    f = (lambda v: '%.3f' % v) if pair == 'DXY' else (lambda v: '%.5f' % v)
    b30 = [x for x in D.bars(pair, '30') if b0 - 4 * 3600000 <= x['time'] < w1 + 4 * 3600000]
    b60 = [x for x in D.bars(pair, '60') if b0 <= x['time'] < w1]
    Z = zones_of(X)
    segs = ch.get('segments') or [ch['path']]
    V = vertices(segs)
    T = actual_turns(b30, b0, w1)
    NZ = {round(n['p'], 7): (n['zb'], n['zt'], n['zone']) for n in ch.get('nodes', []) if 'zb' in n}          # a path node names its own Engine 1 zone
    name = lambda p: NZ.get(round(p, 7)) or next(((b, t, n) for b, t, n in Z if b - 1e-12 <= p <= t + 1e-12), None) or min(((b, t, n) for b, t, n in Z), key=lambda z: min(abs(z[0] - p), abs(z[1] - p)), default=None)
    day_of = lambda t: (t - w0) // 86400000
    res = {'HIT': 0, 'WRONG ZONE': 0, 'WRONG TIME': 0, 'NONE': 0, 'NO ZONE': 0}
    detail = []
    for k, ta, tb, p in V:
        z = name(p)
        if z is None or (round(p, 7) not in NZ and min(abs(z[0] - p), abs(z[1] - p), 0 if z[0] <= p <= z[1] else 9e9) > tol):
            res['NO ZONE'] += 1; detail.append((k, ta, p, 'NO ZONE', '-')); continue
        near_t = [x for x in T if x[0] == k and ta - H2 <= x[1] <= tb + H2]
        at_z = lambda x: z[0] - tol <= x[2] <= z[1] + tol
        if any(at_z(x) for x in near_t): r = 'HIT'
        elif near_t: r = 'WRONG ZONE'
        elif any(x[0] == k and at_z(x) and day_of(x[1]) == day_of(ta) for x in T): r = 'WRONG TIME'
        else: r = 'NONE'
        res[r] += 1; detail.append((k, ta, p, r, z[2]))
    covered = 0
    for k, t, p in T:
        covered += any(vk == k and va - H2 <= t <= vb + H2 and (lambda z: z is not None and z[0] - tol <= p <= z[1] + tol)(name(vp)) for vk, va, vb, vp in V)
    pts = sorted((int(t), float(v)) for sg in segs for t, v in sg)
    def lv(t):
        best = None
        for (ta, va), (tb, vb) in zip(pts, pts[1:]):
            if ta <= t <= tb and tb > ta: best = va + (vb - va) * (t - ta) / (tb - ta)
        return best
    pr = [(lv(x['time'] + 3600000), x['close']) for x in b60]
    pr = [(a, b) for a, b in pr if a is not None]
    r_h = pearson([a for a, _ in pr], [b for _, b in pr])
    net_a = (b60[-1]['close'] - b60[0]['open']) if b60 else 0.0
    net_l = (pts[-1][1] - pts[0][1]) if pts else 0.0
    wk = None if abs(net_a) < 10 * pip else ((net_a > 0) == (net_l > 0) and abs(net_l) > pip)
    dok = dn = 0
    for i, day in enumerate(('Mon', 'Tue', 'Wed', 'Thu', 'Fri')):
        xs = [x for x in b60 if w0 + i * 86400000 <= x['time'] < w0 + (i + 1) * 86400000]
        d = next((q for q in ch['days'] if q['day'] == day), None)
        if not xs or d is None: continue
        Hh, L, O, C = max(x['high'] for x in xs), min(x['low'] for x in xs), xs[0]['open'], xs[-1]['close']
        if d['dir'] == 'range': ok = Hh <= d['hi'] + 10 * pip and L >= d['lo'] - 10 * pip
        else:
            sg = 1 if d['dir'] == 'up' else -1
            ok = (C - O) * sg >= 10 * pip or (d['shapes'][-1] in ('RWL', 'WL') and (Hh - L) >= 20 * pip and (C - O) * sg > 0)
        dok += ok; dn += 1
    fp = hashlib.sha256(json.dumps([(s['dir'], round(s['entry'], 6), round(s['sl'], 6), round(s['tp'], 6)) for s in R['setups']]).encode()).hexdigest()[:10]
    row = {'pair': pair, 'mon': mon, 'vertices': len(V), **res, 'turns': len(T), 'covered': covered, 'r': r_h, 'week': wk, 'days_ok': dok, 'days': dn, 'orders': len(R['setups']), 'orders_fp': fp}
    rows.append(row)
    print(f"{pair:<6} {mon}  line turns {len(V):2d}: HIT {res['HIT']:2d}  wrong zone {res['WRONG ZONE']:2d}  wrong time {res['WRONG TIME']:2d}  none {res['NONE']:2d}  no zone {res['NO ZONE']:2d} | "
          f"actual turns {len(T):2d}, forecast {covered:2d} | hourly r {r_h if r_h is None else round(r_h, 2)} | week dir {'-' if wk is None else 'RIGHT' if wk else 'WRONG'} | days {dok}/{dn} | orders {len(R['setups'])} {fp}", flush=True)
    if A.v:
        ny = lambda t: dt.datetime.fromtimestamp(t / 1000, D.NY).strftime('%a %H:%M')
        for k, ta, p, r, zn in detail: print(f"      {k} {ny(ta)} {f(p)} {r:<10} {zn}")


def total(nm, rs):
    rs = [r for r in rs if 'error' not in r]
    if not rs: return
    s = lambda k: sum(r[k] for r in rs)
    rr = [r['r'] for r in rs if r['r'] is not None]; wk = [r['week'] for r in rs if r['week'] is not None]
    print(f"TOTAL {nm:<10} maps {len(rs):2d} | line turns {s('vertices'):3d}: HIT {s('HIT'):3d} = {100 * s('HIT') / max(1, s('vertices')):3.0f}%  (wrong zone {s('WRONG ZONE')}, wrong time {s('WRONG TIME')}, none {s('NONE')}, no zone {s('NO ZONE')}) | "
          f"actual turns {s('turns')}, forecast {s('covered')} = {100 * s('covered') / max(1, s('turns')):3.0f}% | hourly r mean {sum(rr) / max(1, len(rr)):.2f} | week dir {sum(wk)}/{len(wk)} | days {s('days_ok')}/{s('days')} = {100 * s('days_ok') / max(1, s('days')):.0f}%")


print()
total('GOLDEN', [r for r in rows if r.get('mon') in GOLD])
total('OTHER', [r for r in rows if r.get('mon') not in GOLD])
if A.out: json.dump({'rows': rows, 'switches': os.environ.get('PLUTUS_SWITCHES', '')}, open(A.out, 'w'), default=str)
