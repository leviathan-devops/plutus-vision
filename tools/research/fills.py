"""fills.py PAIR MONDAY - what the week's 15m candles did to each Engine 3 setup (for evidence-ledger rows; uses bars AFTER the anchor, so it is never imported by the tool and its output is never a verdict)."""
import sys, os, datetime as dt
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'e1_tool'))
import e1_data as D, plutus

pair, mon = sys.argv[1], sys.argv[2]
X, chain, R, src = plutus.run(pair, mon)
b = [x for x in D.bars(pair, '15') if D.boundary_ms(mon) <= x['time'] < D.week_end_ms(mon)]
f = '%.3f' if pair == 'DXY' else '%.5f'
ts = lambda t: dt.datetime.fromtimestamp(t / 1000, dt.UTC).strftime('%a %H:%M')
print(pair, mon, '| day map:', ' | '.join(f"{d['day']} {'+'.join(d['shapes'])} {d['dir']}" for d in chain['days']))
DAY = 86400000
FILLS, ANCH = {}, {}
h1 = [x for x in D.bars(pair, '60') if D.boundary_ms(mon) <= x['time'] < D.week_end_ms(mon)]
tick = (0.001 if pair == 'DXY' else 0.00001) / 2
for s in R['setups']:
    long = s['dir'] == 'LONG'
    t0, t_end = s['valid_from'], s['valid_to']             # the order's bracket from Engine 3 (R3 law)
    stop_entry = s['category'] in ('Reinforcement', 'Transition')          # a stop-limit fires when price trades THROUGH the rung in the trade's direction
    head = f"  {s['id']:<5}{'ALT ' if s.get('alt') else '    '}{s['day']} {s['shape']:<6} {s['dir']:<5} E {f % s['entry']} SL {f % s['sl']} TP {f % s['tp']} {s['rrr']}R | "
    start = t0
    if s.get('parent'):                                    # a reinforcement is live from its parent's fill to its parent's exit (E3C:625)
        pf = FILLS.get(s['parent'])
        if pf is None or pf[0] is None:
            print(head + f"parent {s['parent']} not filled -> order never live"); continue
        # E3C:625 'Reinforcement ORDERS are placed in London premarket (pending stop-limit orders)': live from the parent's fill when that falls before London opens (Tokyo session),
        # else from the next trading day's start; never before the premarket of the rocket's OWN day; cancelled at the parent's exit
        import e2_chain as E2M
        S = E2M.week_sessions(mon)
        ses = next((x for x in S if x['t0'] <= pf[0] < x['t1']), None)
        start = pf[0] if (ses is None or ses['s'] == 'TKY') else next((x['t0'] for x in S if x['s'] == 'TKY' and x['t0'] > pf[0]), t_end)
        start = max(start, s['valid_from'])
        t_end = pf[1] if pf[1] else t_end
    # one order per anchor per day (E3C:468): the freshness gate at battle time (E3C:150) - a 1H close beyond the anchor zone = VIOLATED, never an entry again; the 4th battle is skipped;
    # each day's order at an anchor is its own setup (cap key '(pair, anchorBucket, day)', E3C:468): it is placed whether or not an earlier day's position from the same anchor is still open (D-101)
    k = s.get('anchor_key')
    a = s['anchor']
    st0 = ANCH.setdefault(k, {'battles': 0, 'busy_until': 0}) if k else None
    day_order = s['shape'] == 'SS' and s.get('role') != 'last-swing'          # the per-day swing-scalp orders of a consolidation (one per anchor per day)
    if st0 is not None and day_order and 'bot' in a:
        # a sweep zone carrying its extension fails when price closes beyond the extended range (P533 7.1 Rule 2.5 'price sweeping through the LSZ signals zone failure')
        lo_, hi_ = (min(a['bot'], a['reach']), max(a['top'], a['reach'])) if a.get('reach') is not None else (a['bot'], a['top'])
        thru = next((x for x in h1 if x['time'] + 3600000 <= start and ((x['close'] < lo_ - tick) if long else (x['close'] > hi_ + tick))), None)
        if thru is not None and not stop_entry:
            print(head + f"void: the anchor zone was closed through on 1H {ts(thru['time'])} (VIOLATED, E3C:150)"); continue
        if st0['battles'] >= 3:
            print(head + "skipped: 4th battle at this anchor (E3C:150 'index i > 2 skipped')"); continue
    st, tf, first, tx = 'not filled', None, True, None
    for x in b:
        if x['time'] < start:
            continue
        if tf is None and x['time'] >= t_end:
            st = 'not filled inside its bracket (order expires)'; break
        if tf is None and first:
            first = False
            if (not stop_entry) and ((long and x['open'] <= s['sl']) or ((not long) and x['open'] >= s['sl'])):
                st = 'void: price already beyond the stop when the order starts'; break
        if tf is None:
            e0 = s.get('front') if s.get('front') is not None else s['entry']       # Mechanism A front entry = first contact (E3C:1064)
            hit = x['low'] - tick <= e0 <= x['high'] + tick    # a touch to the tick is contact (binary float noise must not decide it)
            if not stop_entry:
                hit = hit or (long and x['open'] <= e0) or ((not long) and x['open'] >= e0)
            if hit:
                tf = x['time']; st = 'filled, still open at the week end'
            continue
        if (long and x['low'] <= s['sl']) or ((not long) and x['high'] >= s['sl']):
            st = 'STOPPED ' + ts(x['time']); tx = x['time']; break
        if (long and x['high'] >= s['tp']) or ((not long) and x['low'] <= s['tp']):
            st = 'TP HIT ' + ts(x['time']); tx = x['time']; break
    FILLS[s['id']] = (tf, tx)
    if st0 is not None and tf is not None and day_order:
        st0['battles'] += 1
        st0['busy_until'] = tx if tx is not None else D.week_end_ms(mon)
    print(head + f"filled {ts(tf) if tf else '-'} -> {st}")
for l in R['log']:
    print('  !', l)
