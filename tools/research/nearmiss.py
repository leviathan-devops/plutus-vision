"""nearmiss.py [maps...] - BUG LOCATOR ONLY (reads the week's bars; never imported by the tool; its tally is never a verdict). For every primary order of a map (no ALT orders, no
reinforcements) on the 15m bars of its bracket:
  STOP NEAR-MISS  = filled, stopped, and price then reached the TP within the week: how many pips beyond the stop price went first (the stop was that much too tight);
  ENTRY NEAR-MISS = never filled, price came within 6 pips of the entry inside the bracket and then reached the TP before the SL: how many pips the entry stood too far.
Written for the operator's verdict of 2026-11-27 (M-57): 'half of your trades are accurate but slightly too tight on the SL or slightly too early'."""
import sys, os, io, contextlib, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'e1_tool'))
import plutus, e1_data as D
maps = sys.argv[1:] or open(os.path.join(HERE, 'maps16.txt')).read().split()[:12]
ts = lambda t: dt.datetime.fromtimestamp(t / 1000, dt.UTC).strftime('%a %H:%M')
T = {'orders': 0, 'tp': 0, 'stopped': 0, 'stop_nm': 0, 'unfilled': 0, 'entry_nm': 0}
for m in maps:
    pair, mon = m.split(':')
    with contextlib.redirect_stdout(io.StringIO()):
        X, E2, R, src = plutus.run(pair, mon)
    pip = D.PIP[pair]; f = '%.3f' if pair == 'DXY' else '%.5f'
    b15 = [x for x in D.bars(pair, '15') if D.boundary_ms(mon) <= x['time'] < D.week_end_ms(mon)]
    print(f"== {pair} {mon}")
    for s in R['setups']:
        if s.get('alt') or s.get('category') == 'Reinforcement':
            continue
        T['orders'] += 1
        lng = s['dir'] == 'LONG'; e, sl, tp = s['entry'], s['sl'], s['tp']
        win = [x for x in b15 if s['valid_from'] <= x['time'] < s['valid_to']]
        fill = next((x for x in win if ((x['low'] <= e) if lng else (x['high'] >= e))), None)
        tag = f"{s['id']:<9} {s['day']} {s['shape']:<4} {s['dir']:<5} E {f % e} SL {f % sl} ({abs(e - sl) / pip:.1f}p) TP {f % tp}"
        if fill is None:
            T['unfilled'] += 1
            if not win:
                continue
            gap = min(((x['low'] - e) if lng else (e - x['high'])) for x in win) / pip
            near = min(win, key=lambda x: (x['low'] - e) if lng else (e - x['high']))
            if gap <= 6:
                after = [x for x in b15 if x['time'] >= near['time']]
                turn = near['low'] if lng else near['high']
                hit = None
                for x in after:
                    if (x['low'] < turn - abs(e - sl)) if lng else (x['high'] > turn + abs(e - sl)):
                        hit = 'sl'; break
                    if (x['high'] >= tp) if lng else (x['low'] <= tp):
                        hit = 'tp'; break
                if hit == 'tp':
                    T['entry_nm'] += 1
                    print(f"   ENTRY NEAR-MISS {tag} | price turned {gap:.1f} pips short of the entry at {f % turn} ({ts(near['time'])}) and reached the TP")
            continue
        after = [x for x in b15 if x['time'] >= fill['time']]
        out = None
        for i, x in enumerate(after):
            if (x['low'] <= sl) if lng else (x['high'] >= sl):
                out = ('sl', i); break
            if (x['high'] >= tp) if lng else (x['low'] <= tp):
                out = ('tp', i); break
        if out is None:
            continue
        if out[0] == 'tp':
            T['tp'] += 1; continue
        T['stopped'] += 1
        worst = sl
        for x in after[out[1]:]:
            worst = min(worst, x['low']) if lng else max(worst, x['high'])
            if (x['high'] >= tp) if lng else (x['low'] <= tp):
                T['stop_nm'] += 1
                print(f"   STOP NEAR-MISS  {tag} | filled {ts(fill['time'])}, stopped {ts(after[out[1]]['time'])}; price went {abs(worst - sl) / pip:.1f} pips beyond the stop to {f % worst}, then reached the TP {ts(x['time'])}")
                break
print(f"NEARMISS (locator): primary orders {T['orders']} | TP {T['tp']} | stopped {T['stopped']}, of them stop near-misses {T['stop_nm']} | unfilled {T['unfilled']}, of them entry near-misses {T['entry_nm']}")
