"""devset.py [--maps dev|golden|heldout|all|PAIR:MONDAY,...] [--out FILE.json] - THE BACKTEST the operator ordered (M-67: '8 separate trading weeks for each of the 3 pairs and get
clear stats and data on each individual trading week'), plan memory/16 step M0. LOCATOR, never imported by the tool: it reads the bars AFTER each anchor to measure.
Per map it runs the product (plutus.run daily=True, the switches as set in the code / PLUTUS_SWITCHES), replays every DRAWN order on the 15m candles with the D-146 chart rules
(fill inside the order's life; a rocket after its parent's fill and before its exit; an alternative order only after its 1H trigger close; SL first when one candle touches both),
and measures the drawn Engine 2 line against the 30-minute closes. Prints one row per pair-week, totals per pair and per set, and (with -v) every order with its excursions.
PLUTUS_SWITCHES='e3_trades.MICRO_TRADES=1,e2_chain.MICRO_PATH=1' sets module switches before the run (each switch is a module-level name of the tool)."""
import sys, os, io, json, contextlib, argparse
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'e1_tool'))
import plutus, e1_data as D, e3_trades as E3, e2_chain as E2M

DEV = ('2026-03-02', '2026-03-23', '2026-04-13', '2026-04-20', '2026-05-18', '2026-08-31', '2026-09-21', '2026-10-05')
HELD = ('2026-03-30', '2026-05-25', '2026-07-13', '2026-09-28')
GOLD = ('2026-07-06',)
PAIRS = ('DXY', 'EURUSD', 'GBPUSD')
H = 3600000
ap = argparse.ArgumentParser()
ap.add_argument('--maps', default='dev')
ap.add_argument('--out', default=None)
ap.add_argument('-v', action='store_true')
A = ap.parse_args()
if A.maps in ('dev', 'golden', 'heldout', 'all'):
    weeks = {'dev': DEV, 'golden': GOLD, 'heldout': HELD, 'all': GOLD + DEV}[A.maps]
    MAPS = [(p, w) for w in weeks for p in PAIRS]
else:
    MAPS = [tuple(m.split(':')) for m in A.maps.split(',')]
for kv in filter(None, os.environ.get('PLUTUS_SWITCHES', '').split(',')):
    k, v = kv.split('=')
    mod, name = k.split('.')
    m_ = sys.modules.get(mod) or __import__(mod)
    old = getattr(m_, name)                                   # an unknown switch name raises here (no silent typo)
    setattr(m_, name, bool(int(v)) if isinstance(old, bool) else int(v) if isinstance(old, int) else float(v) if isinstance(old, float) else tuple(int(x) for x in v.split(';')) if isinstance(old, tuple) else v)
    print(f"switch {mod}.{name} = {getattr(m_, name)!r} (was {old!r})")


def zigzag(b, thr, hk='high', lk='low'):
    piv, d = [], 0
    hi, lo = (b[0]['time'], b[0][hk]), (b[0]['time'], b[0][lk])
    for x in b[1:]:
        if d >= 0 and x[hk] > hi[1]: hi = (x['time'], x[hk])
        if d <= 0 and x[lk] < lo[1]: lo = (x['time'], x[lk])
        if d == 0:
            if hi[1] - x[lk] >= thr:
                piv.append((hi[0], hi[1], 'H')); d = -1; lo = (x['time'], x[lk])
            elif x[hk] - lo[1] >= thr:
                piv.append((lo[0], lo[1], 'L')); d = 1; hi = (x['time'], x[hk])
        elif d == 1 and hi[1] - x[lk] >= thr:
            piv.append((hi[0], hi[1], 'H')); d = -1; lo = (x['time'], x[lk])
        elif d == -1 and x[hk] - lo[1] >= thr:
            piv.append((lo[0], lo[1], 'L')); d = 1; hi = (x['time'], x[hk])
    return piv


def replay(pair, mon, S):
    """bar by bar over ALL orders in list order - the same evaluation order as the Pine (e3_trades.pine_state): per bar, per order: alternative trigger, fill (a resting limit
    through its entry inside its life; a rocket after its parent's fill bar and before the parent's exit), then SL first / TP on the same bar. With e3_trades.ONE_PER_MOVE a primary
    touched while a same-direction primary is open is void (D-148)."""
    b0, wk1 = D.boundary_ms(mon), D.week_end_ms(mon)
    b15 = [x for x in D.bars(pair, '15') if D.week_start_ms(mon) - 86400000 <= x['time'] < wk1 + 3 * 86400000]
    b60 = [x for x in D.bars(pair, '60') if D.week_start_ms(mon) - 86400000 <= x['time'] < wk1 + 3 * 86400000]
    pip = D.PIP[pair]
    n = len(S)
    E, X, RES, V = [None] * n, [None] * n, ['NOT FILLED'] * n, [False] * n
    mfe, mae = [0.0] * n, [0.0] * n
    x0 = [E3._order_start(s, mon, b0) for s in S]
    par = [next((i for i, q in enumerate(S) if q is s.get('parent_ref')), None) if s.get('parent_ref') is not None else None for s in S]
    trig = [None] * n
    for k, s in enumerate(S):
        if s.get('alt') and s.get('trigger'):
            lv, up = s['trigger']['level'], s['trigger']['dir'] == 'up'
            trig[k] = next((x['time'] + H for x in b60 if x['time'] >= x0[k] and ((x['close'] > lv) if up else (x['close'] < lv))), 'never')
    prim = [s.get('category') != 'Reinforcement' for s in S]
    opm = getattr(E3, 'ONE_PER_MOVE', False)
    for b in b15:
        t = b['time']
        for k, s in enumerate(S):
            lng = s['dir'] == 'LONG'
            if E[k] is None and not V[k]:
                if t < x0[k] or trig[k] == 'never' or (trig[k] is not None and t < trig[k]):
                    continue
                j = par[k]
                if j is not None:
                    if E[j] is None or t <= E[j] or X[j] is not None:
                        continue
                elif t >= min(s.get('valid_to') or wk1, wk1):
                    continue
                rocket = not prim[k]
                hit = ((b['low'] <= s['entry']) if lng else (b['high'] >= s['entry'])) if not rocket else ((b['high'] >= s['entry']) if lng else (b['low'] <= s['entry']))
                if not hit:
                    continue
                if opm and prim[k] and any(i != k and prim[i] and S[i]['dir'] == s['dir'] and E[i] is not None and X[i] is None for i in range(n)):
                    V[k] = True; RES[k] = 'VOID'
                    continue
                E[k] = t
            if E[k] is not None and X[k] is None:
                fav = (b['high'] - s['entry']) if lng else (s['entry'] - b['low'])
                adv = (s['entry'] - b['low']) if lng else (b['high'] - s['entry'])
                if (b['low'] <= s['sl']) if lng else (b['high'] >= s['sl']):
                    X[k] = t; RES[k] = 'SL'; mae[k] = max(mae[k], adv)
                    continue
                mfe[k] = max(mfe[k], fav); mae[k] = max(mae[k], adv)
                if (b['high'] >= s['tp']) if lng else (b['low'] <= s['tp']):
                    X[k] = t; RES[k] = 'TP'
    out = []
    for k, s in enumerate(S):
        res = RES[k] if not (E[k] is not None and X[k] is None) else 'OPEN'
        risk = abs(s['entry'] - s['sl'])
        out.append({'res': res, 'fill': E[k], 'exit': X[k], 'mfe_r': mfe[k] / risk if risk else 0, 'mae_r': mae[k] / risk if risk else 0,
                    'rr': abs(s['tp'] - s['entry']) / risk if risk else 0, 'risk_p': risk / pip})
    return out


def line_metrics(pair, mon, ch):
    pip = D.PIP[pair]; b0, wk1 = D.boundary_ms(mon), D.week_end_ms(mon)
    b30 = [x for x in D.bars(pair, '30') if b0 <= x['time'] < wk1]
    pts = sorted((int(t), float(v)) for sg in (ch.get('segments') or [ch['path']]) for t, v in sg)

    def lv(t):
        best = None
        for (ta, va), (tb, vb) in zip(pts, pts[1:]):
            if ta <= t <= tb and tb > ta: best = va + (vb - va) * (t - ta) / (tb - ta)
        return best
    errs = []
    for x in b30:
        v = lv(x['time'] + 15 * 60000)
        if v is not None: errs.append(abs(x['close'] - v) / pip)
    agree = tot2 = 0
    for i in range(4, len(b30)):
        l1, l0 = lv(b30[i]['time'] + 15 * 60000), lv(b30[i - 4]['time'] + 15 * 60000)
        if l1 is None or l0 is None: continue
        dc, dl = b30[i]['close'] - b30[i - 4]['close'], l1 - l0
        if abs(dc) < 5 * pip: continue
        tot2 += 1; agree += (dc > 0) == (dl > 0) and abs(dl) > 0.5 * pip
    vx = [(pts[i][0], 'H' if pts[i][1] >= max(pts[i - 1][1], pts[i + 1][1]) else 'L') for i in range(1, len(pts) - 1) if (pts[i][1] - pts[i - 1][1]) * (pts[i + 1][1] - pts[i][1]) < 0]
    tps = zigzag(b30, 15 * pip, 'close', 'close') if b30 else []
    w1 = sum(1 for tt, pp, kk in tps if any(v[1] == kk and abs(v[0] - tt) <= 30 * 60000 for v in vx))
    return {'n30': len(errs), 'within10': sum(e <= 10 for e in errs), 'miss': sum(errs), 'dir_ok': agree, 'dir_n': tot2, 'turns': len(tps), 'turn1': w1}


def moves(pair, mon, S, R):
    pip = D.PIP[pair]; b0, wk1 = D.boundary_ms(mon), D.week_end_ms(mon)
    b60 = [x for x in D.bars(pair, '60') if b0 <= x['time'] < wk1]
    piv = zigzag(b60, 30 * pip) if b60 else []
    n = c = 0
    for (ta, pa, _), (tb, pb, _) in zip(piv, piv[1:]):
        if abs(pb - pa) >= 30 * pip and tb - ta >= 3 * H:
            n += 1; up = pb > pa
            c += any(r['res'] == 'TP' and (s['dir'] == 'LONG') == up and ta - 2 * H <= r['fill'] <= tb and abs(s['entry'] - pa) <= 0.5 * abs(pb - pa) for s, r in zip(S, R))
    return n, c


rows, dump = [], []
for pair, mon in MAPS:
    plutus._MEMO.clear()
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            X, ch, Rr, pine = plutus.run(pair, mon, daily=True)
    except Exception as ex:
        print(f"{pair} {mon}: RUN ERROR {ex!r}"[:200], flush=True); rows.append({'pair': pair, 'mon': mon, 'error': repr(ex)}); continue
    S = Rr['setups']
    R = replay(pair, mon, S)
    L = line_metrics(pair, mon, ch)
    nm, cm = moves(pair, mon, S, R)
    row = {'pair': pair, 'mon': mon, 'drawn': len(S), 'filled': sum(r['res'] in ('TP', 'SL', 'OPEN') for r in R), 'TP': sum(r['res'] == 'TP' for r in R),
           'SL': sum(r['res'] == 'SL' for r in R), 'OPEN': sum(r['res'] == 'OPEN' for r in R), 'NF': sum(r['res'] == 'NOT FILLED' for r in R), 'VOID': sum(r['res'] == 'VOID' for r in R),
           'moves': nm, 'caught': cm, 'rr_tp': [r['rr'] for r in R if r['res'] == 'TP'], **L}
    rows.append(row)
    wr = 100 * row['TP'] / max(1, row['TP'] + row['SL'])
    print(f"{pair:<6} {mon}  drawn {row['drawn']:2d}  filled {row['filled']:2d}  TP {row['TP']:2d}  SL {row['SL']:2d}  open {row['OPEN']}  never {row['NF']:2d}  void {row['VOID']}  win {wr:5.1f}%  "
          f"moves {nm:2d} caught {cm:2d}  line<=10p {100 * L['within10'] / max(1, L['n30']):3.0f}%  miss {L['miss'] / max(1, L['n30']):5.1f}p  dir2h {100 * L['dir_ok'] / max(1, L['dir_n']):3.0f}%  "
          f"turns {L['turns']:2d} vtx<=1c {L['turn1']:2d}", flush=True)
    for s, r in zip(S, R):
        d = {'pair': pair, 'mon': mon, 'id': s.get('id'), 'day': s.get('day'), 'shape': s.get('shape'), 'role': s.get('role'), 'dir': s['dir'], 'cat': s.get('category'),
             'entry': s['entry'], 'sl': s['sl'], 'tp': s['tp'], 'micro': bool(s.get('micro')), **{k: v for k, v in r.items()}}
        dump.append(d)
        if A.v:
            print(f"     {s.get('id', ''):<5} {s.get('day', '')} {s.get('shape', ''):<6} {s.get('role') or '':<10} {s['dir']:<5} E {s['entry']:.5f} SL {s['sl']:.5f} TP {s['tp']:.5f} -> {r['res']:<10}"
                  + (f" fill {D.ts(r['fill'])} RR {r['rr']:.1f} MFE {r['mfe_r']:.1f}R MAE {r['mae_r']:.1f}R" if r.get('fill') else ''))


def total(name, rs):
    rs = [r for r in rs if 'error' not in r]
    if not rs: return
    t = {k: sum(r.get(k, 0) for r in rs) for k in ('drawn', 'filled', 'TP', 'SL', 'OPEN', 'NF', 'VOID', 'moves', 'caught', 'n30', 'within10', 'miss', 'dir_ok', 'dir_n', 'turns', 'turn1')}
    rr = [x for r in rs for x in r['rr_tp']]
    wr = [100 * r['TP'] / (r['TP'] + r['SL']) for r in rs if r['TP'] + r['SL']]
    print(f"TOTAL {name:<12} maps {len(rs):2d}  drawn {t['drawn']:3d}  filled {t['filled']:3d} ({t['filled'] / len(rs):.1f}/pair-week)  TP {t['TP']:3d}  SL {t['SL']:3d}  open {t['OPEN']}  never {t['NF']:3d}  void {t['VOID']}  "
          f"win {100 * t['TP'] / max(1, t['TP'] + t['SL']):5.1f}%  (mean of weekly win {sum(wr) / max(1, len(wr)):.1f}% over {len(wr)} maps)  moves caught {t['caught']}/{t['moves']}  "
          f"avg RR of TPs {sum(rr) / max(1, len(rr)):.2f}  line<=10p {100 * t['within10'] / max(1, t['n30']):.0f}%  miss {t['miss'] / max(1, t['n30']):.1f}p  dir2h {100 * t['dir_ok'] / max(1, t['dir_n']):.0f}%  "
          f"turn vtx<=1c {t['turn1']}/{t['turns']}")


print()
for p in PAIRS:
    total(p, [r for r in rows if r.get('pair') == p and r.get('mon') not in GOLD])
total('ALL (no gold)', [r for r in rows if r.get('mon') not in GOLD])
total('GOLDEN', [r for r in rows if r.get('mon') in GOLD])
if A.out:
    json.dump({'rows': rows, 'orders': dump, 'switches': os.environ.get('PLUTUS_SWITCHES', '')}, open(A.out, 'w'), default=str)
