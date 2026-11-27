"""e2forensic.py [PAIR:MONDAY ...] - FORENSIC LOCATOR (reads the week's bars; never imported by the tool; never a verdict). Per map, PRODUCT mode (daily anchoring):
 1 day tags vs candles (e2loc rules); 2 the week's visible moves (1H zigzag 30 pips, 3+ hours - the outside reviewers' 'obvious trades') and whether a same-direction order filled near
 the move's start and took its TP inside the move; 3 every drawn order: day tag right?, outcome (15m, D-146 chart rules); 4 the drawn E2 line against the 30-minute closes: mean miss,
 share of 30m closes within 10 pips of the line, direction agreement of 2-hour changes, and every 30m turning point (zigzag 15 pips) against the nearest line vertex of the same kind:
 timing error in 30-minute candles and price error in pips."""
import sys, os, io, contextlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'e1_tool'))
import plutus, e1_data as D, e3_trades as E3
MAPS = [m.split(':') for m in sys.argv[1:]] or [(p, w) for w in ('2026-07-06', '2026-04-13', '2026-04-20', '2026-05-18', '2026-10-05') for p in ('DXY', 'EURUSD', 'GBPUSD')]
H = 3600000


def zigzag(b, thr, hk='high', lk='low'):
    piv, d = [], 0
    hi, lo = (b[0]['time'], b[0][hk]), (b[0]['time'], b[0][lk])
    for x in b[1:]:
        if d >= 0 and x[hk] > hi[1]: hi = (x['time'], x[hk])
        if d <= 0 and x[lk] < lo[1]: lo = (x['time'], x[lk])
        if d == 0:
            if hi[1] - x[lk] >= thr and hi[0] <= x['time']:
                piv.append((hi[0], hi[1], 'H')); d = -1; lo = (x['time'], x[lk])
            elif x[hk] - lo[1] >= thr:
                piv.append((lo[0], lo[1], 'L')); d = 1; hi = (x['time'], x[hk])
        elif d == 1 and hi[1] - x[lk] >= thr:
            piv.append((hi[0], hi[1], 'H')); d = -1; lo = (x['time'], x[lk])
        elif d == -1 and x[hk] - lo[1] >= thr:
            piv.append((lo[0], lo[1], 'L')); d = 1; hi = (x['time'], x[hk])
    return piv


agg = {}
for pair, mon in MAPS:
    plutus._MEMO.clear()
    with contextlib.redirect_stdout(io.StringIO()):
        X, ch, R, pine = plutus.run(pair, mon, daily=True)
    pip = D.PIP[pair]; b0, wk1, w0 = D.boundary_ms(mon), D.week_end_ms(mon), D.week_start_ms(mon)
    b15 = [x for x in D.bars(pair, '15') if w0 - 86400000 <= x['time'] < wk1 + 3 * 86400000]
    b30 = [x for x in D.bars(pair, '30') if b0 <= x['time'] < wk1]
    b60 = [x for x in D.bars(pair, '60') if b0 <= x['time'] < wk1]
    G = 'GOLDEN' if mon == '2026-07-06' else 'OTHER'
    A = agg.setdefault(G, {'days': [0, 0], 'legs': [0, 0], 'ord': {'drawn': 0, 'filled': 0, 'TP': 0, 'SL': 0}, 'tp_daytag': [0, 0], 'sl_daytag': [0, 0], 'within10': [0, 0], 'dir2h': [0, 0], 'turn_err_c': [], 'turn_err_p': [], 'miss': []})
    # 1 day tags
    tags = {}
    for i, day in enumerate(('Mon', 'Tue', 'Wed', 'Thu', 'Fri')):
        xs = [x for x in b60 if w0 + i * 86400000 <= x['time'] < w0 + (i + 1) * 86400000]
        d = next((q for q in ch['days'] if q['day'] == day), None)
        if not xs or d is None: tags[day] = None; continue
        Hh, L, O, C = max(x['high'] for x in xs), min(x['low'] for x in xs), xs[0]['open'], xs[-1]['close']
        if d['dir'] == 'range':
            ok = Hh <= d['hi'] + 10 * pip and L >= d['lo'] - 10 * pip
        else:
            sg = 1 if d['dir'] == 'up' else -1
            ok = (C - O) * sg >= 10 * pip or (d['shapes'][-1] in ('RWL', 'WL') and (Hh - L) >= 20 * pip and (C - O) * sg > 0)
        tags[day] = (ok, '+'.join(d['shapes']) + ('' if d['dir'] == 'range' else ' ' + d['dir']), f"actual O {O:.5f} C {C:.5f} H {Hh:.5f} L {L:.5f}" if pair != 'DXY' else f"actual O {O:.3f} C {C:.3f} H {Hh:.3f} L {L:.3f}")
        A['days'][0] += ok; A['days'][1] += 1
    # 3 orders (D-146 rules on 15m)
    st, orders = {}, []
    for k, s in enumerate(R['setups']):
        x0 = E3._order_start(s, mon, b0); par = s.get('parent_ref'); j = next((i for i, q in enumerate(R['setups']) if q is par), None) if par is not None else None
        lng = s['dir'] == 'LONG'; rk = s.get('category') == 'Reinforcement'; e = x = None; r = 'NOT FILLED'
        for b in b15:
            if e is None:
                if b['time'] < x0: continue
                if j is not None:
                    pe, px, _ = st[j]
                    if pe is None or b['time'] <= pe or (px is not None and b['time'] > px): continue
                elif b['time'] >= min(s.get('valid_to') or wk1, wk1): break
                if (((b['low'] <= s['entry']) if lng else (b['high'] >= s['entry'])) if not rk else ((b['high'] >= s['entry']) if lng else (b['low'] <= s['entry']))): e = b['time']
                else: continue
            if (b['low'] <= s['sl']) if lng else (b['high'] >= s['sl']): x = b['time']; r = 'SL'; break
            if (b['high'] >= s['tp']) if lng else (b['low'] <= s['tp']): x = b['time']; r = 'TP'; break
        if e is not None and x is None: r = 'OPEN'
        st[k] = (e, x, r)
        dayt = tags.get(D.ts(e)[0:10] and ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')[min(4, max(0, (e - w0) // 86400000))] if e else s['day'])
        orders.append((s, r, e, x, dayt))
        A['ord']['drawn'] += 1; A['ord']['filled'] += e is not None
        if r in ('TP', 'SL'):
            A['ord'][r] += 1
            if dayt is not None:
                A['tp_daytag' if r == 'TP' else 'sl_daytag'][0] += dayt[0]; A['tp_daytag' if r == 'TP' else 'sl_daytag'][1] += 1
    # 2 visible moves (legs)
    piv = zigzag(b60, 30 * pip)
    legs = []
    for (ta, pa, ka), (tb, pb, kb) in zip(piv, piv[1:]):
        if abs(pb - pa) >= 30 * pip and tb - ta >= 3 * H:
            up = pb > pa
            caught = next((o for o in orders if o[1] == 'TP' and (o[0]['dir'] == 'LONG') == up and ta - 2 * H <= o[2] <= tb and abs(o[0]['entry'] - pa) <= 0.5 * abs(pb - pa)), None)
            legs.append((ta, tb, pa, pb, caught))
    A['legs'][0] += sum(1 for l in legs if l[4]); A['legs'][1] += len(legs)
    # 4 line vs 30m closes
    pts = []
    for sg in (ch.get('segments') or [ch['path']]):
        for t, v in sg: pts.append((int(t), float(v)))
    pts.sort()
    def lv(t):
        best = None
        for (ta, va), (tb, vb) in zip(pts, pts[1:]):
            if ta <= t <= tb and tb > ta: best = va + (vb - va) * (t - ta) / (tb - ta)
        return best
    errs, near = [], 0
    for x in b30:
        v = lv(x['time'] + 15 * 60000)
        if v is None: continue
        e_ = abs(x['close'] - v) / pip; errs.append(e_); near += e_ <= 10
    A['within10'][0] += near; A['within10'][1] += len(errs); A['miss'] += errs
    agree = tot2 = 0
    for i in range(4, len(b30)):
        t1_, t0_ = b30[i]['time'], b30[i - 4]['time']
        l1, l0 = lv(t1_ + 15 * 60000), lv(t0_ + 15 * 60000)
        if l1 is None or l0 is None: continue
        dc, dl = b30[i]['close'] - b30[i - 4]['close'], l1 - l0
        if abs(dc) < 5 * pip: continue
        tot2 += 1; agree += (dc > 0) == (dl > 0) and abs(dl) > 0.5 * pip
    A['dir2h'][0] += agree; A['dir2h'][1] += tot2
    # turning points: 30m zigzag 15 pips vs line vertices
    vx = [(pts[i][0], pts[i][1], 'H' if pts[i][1] >= max(pts[i - 1][1], pts[i + 1][1]) else 'L') for i in range(1, len(pts) - 1)
          if (pts[i][1] - pts[i - 1][1]) * (pts[i + 1][1] - pts[i][1]) < 0]
    tps = zigzag(b30, 15 * pip, 'close', 'close')
    terr = []
    for (tt, pp, kk) in tps:
        cand = [v for v in vx if v[2] == kk and abs(v[0] - tt) <= 12 * H]
        if not cand: terr.append(None); continue
        v = min(cand, key=lambda v: abs(v[0] - tt))
        terr.append((abs(v[0] - tt) / (30 * 60000), abs(v[1] - pp) / pip))
    A['turn_err_c'] += [t[0] if t else 99 for t in terr]; A['turn_err_p'] += [t[1] for t in terr if t]
    # print
    print(f"=== {pair} {mon} ({G}) chain: " + ' | '.join(f"{c['shape']} {c.get('dir')}" for c in ch['chain']))
    for day, tg in tags.items():
        if tg: print(f"   {day}: forecast {tg[1]:<18} {'RIGHT' if tg[0] else 'WRONG'}  ({tg[2]})")
    for s, r, e, x, dayt in orders:
        print(f"   order {s['id']:<4} {s['day']} {s['shape']:<6} {s['dir']:<5} E {s['entry']:.5f} -> {r:<10} filled {D.ts(e)[5:16] if e else '-':<11} (fill-day tag {'RIGHT' if dayt and dayt[0] else ('WRONG' if dayt else '-')})")
    print(f"   visible moves (1H 30p, 3h+): {len(legs)}, caught by a TP order: {sum(1 for l in legs if l[4])}")
    for ta, tb, pa, pb, c in legs:
        print(f"      {D.ts(ta)[5:16]} -> {D.ts(tb)[5:16]} {'UP  ' if pb > pa else 'DOWN'} {abs(pb - pa) / pip:5.0f}p  {'caught by ' + c[0]['id'] if c else 'MISSED'}")
    nt = len(terr); w1 = sum(1 for t in terr if t and t[0] <= 1); w2 = sum(1 for t in terr if t and t[0] <= 3)
    print(f"   line vs 30m closes: mean miss {sum(errs) / max(1, len(errs)):.1f}p | closes within 10p of the line {100 * near / max(1, len(errs)):.0f}% | 2h direction agreement {100 * agree / max(1, tot2):.0f}% | "
          f"30m turns {nt}: line vertex of the same kind within 1 candle {w1}, within 3 candles {w2}, none within 12h {sum(1 for t in terr if t is None)}")
print()
for G, A in agg.items():
    tc = A['turn_err_c']
    print(f"TOTAL {G}: day tags right {A['days'][0]}/{A['days'][1]} | visible moves caught {A['legs'][0]}/{A['legs'][1]} | orders drawn {A['ord']['drawn']} filled {A['ord']['filled']} TP {A['ord']['TP']} SL {A['ord']['SL']} | "
          f"fill-day tag right: TP {A['tp_daytag'][0]}/{A['tp_daytag'][1]}, SL {A['sl_daytag'][0]}/{A['sl_daytag'][1]} | line: closes within 10p {100 * A['within10'][0] / max(1, A['within10'][1]):.0f}%, "
          f"mean miss {sum(A['miss']) / max(1, len(A['miss'])):.1f}p, 2h direction agreement {100 * A['dir2h'][0] / max(1, A['dir2h'][1]):.0f}% | 30m turns {len(tc)}: vertex within 1 candle {sum(1 for t in tc if t <= 1)}, within 3 {sum(1 for t in tc if t <= 3)}")
