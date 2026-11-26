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
for s in R['setups']:
    long = s['dir'] == 'LONG'
    day0 = D.week_start_ms(mon) + {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4}[s['day']] * 86400000
    t0, st, tf = max(day0, D.boundary_ms(mon)), 'not filled', None      # a resting order from the start of its day
    stop_entry = s['category'] == 'Reinforcement'          # a stop-limit fires when price trades THROUGH the rung in the trade's direction
    t_end = day0 + (1 + len(s.get('days', [1])) - 1) * 86400000     # the entry is valid inside its own day(s) only (R3 law: the order's bracket comes from the E2 day)
    for x in b:
        if x['time'] < t0:
            continue
        if tf is None and x['time'] >= t_end:
            st = 'not filled in its day (order expires)'; break
        if tf is None and x['time'] == next(y['time'] for y in b if y['time'] >= t0):
            if (not stop_entry) and ((long and x['open'] <= s['sl']) or ((not long) and x['open'] >= s['sl'])):
                st = 'void: price already beyond the stop at the start of its day'; break
        if tf is None:
            hit = x['low'] <= s['entry'] <= x['high']
            if not stop_entry:
                hit = hit or (long and x['open'] <= s['entry']) or ((not long) and x['open'] >= s['entry'])
            if hit:
                tf = x['time']; st = 'filled, still open at the week end'
            continue
        if (long and x['low'] <= s['sl']) or ((not long) and x['high'] >= s['sl']):
            st = 'STOPPED ' + ts(x['time']); break
        if (long and x['high'] >= s['tp']) or ((not long) and x['low'] <= s['tp']):
            st = 'TP HIT ' + ts(x['time']); break
    print(f"  {s['id']} {s['day']} {s['shape']:<6} {s['dir']:<5} E {f % s['entry']} SL {f % s['sl']} TP {f % s['tp']} {s['rrr']}R | filled {ts(tf) if tf else '-'} -> {st}")
for l in R['log']:
    print('  !', l)
