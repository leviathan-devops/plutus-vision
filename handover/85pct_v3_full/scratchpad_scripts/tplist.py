import sys, os, io, contextlib
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import plutus, e1_data as D
daily = sys.argv[1] == 'daily'
maps = open('/home/user/plutus-vision/tools/research/maps16.txt').read().split()[:12]
for m in maps:
    pair, mon = m.split(':')
    with contextlib.redirect_stdout(io.StringIO()):
        X, E2, R, src = plutus.run(pair, mon, daily=daily)
    b15 = [x for x in D.bars(pair, '15') if D.boundary_ms(mon) <= x['time'] < D.week_end_ms(mon)]
    for s in R['setups']:
        if s.get('alt') or s.get('category') == 'Reinforcement':
            continue
        lng = s['dir'] == 'LONG'; e, sl, tp = s['entry'], s['sl'], s['tp']
        t0 = max(s['valid_from'], s.get('day_anchor') or 0)
        win = [x for x in b15 if t0 <= x['time'] < s['valid_to']]
        fill = next((x for x in win if ((x['low'] <= e) if lng else (x['high'] >= e))), None)
        res = 'UNFILLED'
        if fill:
            after = [x for x in b15 if x['time'] >= fill['time']]
            for x in after:
                hs = (x['low'] <= sl) if lng else (x['high'] >= sl)
                ht = (x['high'] >= tp) if lng else (x['low'] <= tp)
                if hs: res = 'SL'; break
                if ht: res = 'TP'; break
            else: res = 'OPEN'
        print(f"{pair} {mon} {s['id']:<9} {s['day']} {s['shape']:<4} {s['dir']:<5} {e:.5f} {res} fill={D.ts(fill['time']) if fill else '-'}")
