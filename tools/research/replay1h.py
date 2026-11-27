"""replay1h.py - replays every drawn order on the chart's candles exactly as the D-146 Pine does (fill inside the order's life; rocket after its parent's fill and before its exit; SL first
when one candle touches both), on 1H and on 15m bars. Prints the order table and the counts per pair (golden week). Locator: it counts what the frames show."""
import sys, io, contextlib
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import plutus, e1_data as D, e3_trades as E3
mon = '2026-07-06'
for pair in ('DXY', 'EURUSD', 'GBPUSD'):
    plutus._MEMO.clear()
    with contextlib.redirect_stdout(io.StringIO()):
        X, ch, R, pine = plutus.run(pair, mon, daily=True)
    b0, wk1 = D.boundary_ms(mon), D.week_end_ms(mon)
    f = (lambda v: '%.3f' % v) if pair == 'DXY' else (lambda v: '%.5f' % v)
    out = {}
    for tf in ('60', '15'):
        bars = [x for x in D.bars(pair, tf) if D.week_start_ms(mon) - 86400000 <= x['time'] < wk1 + 3 * 86400000]
        st = {}
        for k, s in enumerate(R['setups']):
            x0 = E3._order_start(s, mon, b0)
            par = s.get('parent_ref'); j = next((i for i, q in enumerate(R['setups']) if q is par), None) if par is not None else None
            lng = s['dir'] == 'LONG'
            rocket = s.get('category') == 'Reinforcement'
            e = x = None; res = 'NOT FILLED'
            for b in bars:
                if e is None:
                    if b['time'] < x0: continue
                    if j is not None:
                        pe, px = st[j][0], st[j][1]
                        if pe is None or b['time'] <= pe or (px is not None and b['time'] > px): continue
                    elif b['time'] >= min(s.get('valid_to') or wk1, wk1): break
                    hit = ((b['low'] <= s['entry']) if lng else (b['high'] >= s['entry'])) if not rocket else ((b['high'] >= s['entry']) if lng else (b['low'] <= s['entry']))
                    if hit: e = b['time']
                    else: continue
                if (b['low'] <= s['sl']) if lng else (b['high'] >= s['sl']):
                    x = b['time']; res = 'SL'; break
                if (b['high'] >= s['tp']) if lng else (b['low'] <= s['tp']):
                    x = b['time']; res = 'TP'; break
            if e is not None and x is None: res = 'OPEN'
            st[k] = (e, x, res, x0)
        out[tf] = st
    print(f"== {pair} golden week: {len(R['setups'])} orders drawn")
    for k, s in enumerate(R['setups']):
        e, x, r, x0 = out['60'][k]; e15, x15, r15, _ = out['15'][k]
        print(f"  {s['id']:<4} {s['day']} {s['shape']:<6} {s['dir']:<5} E {f(s['entry'])} SL {f(s['sl'])} TP {f(s['tp'])} | placed {D.ts(x0)[5:16]} | 1H: {r:<10} fill {D.ts(e)[5:16] if e else '-':<11} exit {D.ts(x)[5:16] if x else '-':<11} | 15m: {r15:<10} fill {D.ts(e15)[5:16] if e15 else '-'}")
    for tf in ('60', '15'):
        rs = [v[2] for v in out[tf].values()]
        print(f"  {'1H ' if tf == '60' else '15m'} counts: drawn {len(rs)} | filled {sum(1 for r in rs if r in ('TP','SL','OPEN'))} | TP {rs.count('TP')} | SL {rs.count('SL')} | open {rs.count('OPEN')} | not filled {rs.count('NOT FILLED')}")
