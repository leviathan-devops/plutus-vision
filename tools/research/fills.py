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
FILLS = {}
for s in R['setups']:
    long = s['dir'] == 'LONG'
    t0, t_end = s['valid_from'], s['valid_to']             # the order's bracket from Engine 3 (R3 law)
    stop_entry = s['category'] in ('Reinforcement', 'Transition')          # a stop-limit fires when price trades THROUGH the rung in the trade's direction
    # a swing scalp of a consolidation is one order per anchor per day (E3C:129 '(WorkingDay, zone) pair', E3C:468 cap key (pair, anchorBucket, day)): after a TP it re-arms at the next
    # trading day's start while its bracket lasts; a stop = the level closed through (VIOLATED, never an entry again); the 4th battle is skipped (E3C:150 'index i > 2 skipped')
    rearm = s['shape'] == 'SS' and s.get('role') != 'last-swing' and (t_end - t0) > DAY
    res, battles, start = [], 0, t0
    if s.get('parent'):                                    # a reinforcement is live from its parent's fill to its parent's exit (E3C:625)
        pf = FILLS.get(s['parent'])
        if pf is None or pf[0] is None:
            print(f"  {s['id']:<5}    {s['day']} {s['shape']:<6} {s['dir']:<5} E {f % s['entry']} SL {f % s['sl']} TP {f % s['tp']} {s['rrr']}R | parent {s['parent']} not filled -> order never live"); continue
        # E3C:625 'Reinforcement ORDERS are placed in London premarket (pending stop-limit orders)': live from the parent's fill when that falls before London opens (Tokyo session),
        # else from the next trading day's start; cancelled at the parent's exit
        import e2_chain as E2M
        S = E2M.week_sessions(mon)
        ses = next((x for x in S if x['t0'] <= pf[0] < x['t1']), None)
        start = pf[0] if (ses is None or ses['s'] == 'TKY') else next((x['t0'] for x in S if x['s'] == 'TKY' and x['t0'] > pf[0]), t_end)
        start = max(start, s['valid_from'])              # ... of the rocket's OWN day (E3C:625 'placed in London premarket'; every order's bracket comes from its designated day, R3 law)
        t_end = pf[1] if pf[1] else t_end
    while True:
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
                tick = (0.001 if pair == 'DXY' else 0.00001) / 2
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
        res.append(f"filled {ts(tf) if tf else '-'} -> {st}")
        if battles == 0:
            FILLS[s['id']] = (tf, tx if st.startswith(('TP HIT', 'STOPPED')) else None)
        battles += 1
        if not (rearm and st.startswith('TP HIT') and battles < 3):
            break
        start = D.week_start_ms(mon) + ((tx - D.week_start_ms(mon)) // DAY + 1) * DAY
        if start >= t_end:
            break
    print(f"  {s['id']:<5}{'ALT ' if s.get('alt') else '    '}{s['day']} {s['shape']:<6} {s['dir']:<5} E {f % s['entry']} SL {f % s['sl']} TP {f % s['tp']} {s['rrr']}R | " + ' || re-armed: '.join(res))
for l in R['log']:
    print('  !', l)
