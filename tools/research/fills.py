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
for s in R['setups']:
    long = s['dir'] == 'LONG'
    t0, t_end = s['valid_from'], s['valid_to']             # the order's bracket from Engine 3 (R3 law)
    stop_entry = s['category'] in ('Reinforcement', 'Transition')          # a stop-limit fires when price trades THROUGH the rung in the trade's direction
    # a swing scalp of a consolidation is one order per anchor per day (E3C:129 '(WorkingDay, zone) pair', E3C:468 cap key (pair, anchorBucket, day)): after a TP it re-arms at the next
    # trading day's start while its bracket lasts; a stop = the level closed through (VIOLATED, never an entry again); the 4th battle is skipped (E3C:150 'index i > 2 skipped')
    rearm = s['shape'] == 'SS' and s.get('role') != 'last-swing' and (t_end - t0) > DAY
    res, battles, start = [], 0, t0
    while True:
        st, tf, first = 'not filled', None, True
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
                hit = x['low'] <= s['entry'] <= x['high']
                if not stop_entry:
                    hit = hit or (long and x['open'] <= s['entry']) or ((not long) and x['open'] >= s['entry'])
                if hit:
                    tf = x['time']; st = 'filled, still open at the week end'
                continue
            if (long and x['low'] <= s['sl']) or ((not long) and x['high'] >= s['sl']):
                st = 'STOPPED ' + ts(x['time']); tx = x['time']; break
            if (long and x['high'] >= s['tp']) or ((not long) and x['low'] <= s['tp']):
                st = 'TP HIT ' + ts(x['time']); tx = x['time']; break
        res.append(f"filled {ts(tf) if tf else '-'} -> {st}")
        battles += 1
        if not (rearm and st.startswith('TP HIT') and battles < 3):
            break
        start = D.week_start_ms(mon) + ((tx - D.week_start_ms(mon)) // DAY + 1) * DAY
        if start >= t_end:
            break
    print(f"  {s['id']:<5}{'ALT ' if s.get('alt') else '    '}{s['day']} {s['shape']:<6} {s['dir']:<5} E {f % s['entry']} SL {f % s['sl']} TP {f % s['tp']} {s['rrr']}R | " + ' || re-armed: '.join(res))
for l in R['log']:
    print('  !', l)
