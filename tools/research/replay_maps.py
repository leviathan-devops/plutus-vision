"""replay_maps.py MODE [PAIR:MONDAY ...] - LOCATOR (never a verdict): run the tool on each map (MODE daily = the product, weekly = Monday-anchor build) and replay every DRAWN
order on the 15m candles with the D-146 chart rules (fill inside the order's life; a rocket after its parent's fill and before its exit; an alternative order only after its 1H trigger
close; SL first when one candle touches both). Prints per map and totals (drawn / filled / TP / SL / open / never filled). Default maps: every pair-week with a cached V1 harvest."""
import sys, os, io, glob, contextlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'e1_tool'))
import plutus, e1_data as D, e3_trades as E3
mode = sys.argv[1]
maps = [m.split(':') for m in sys.argv[2:]] or sorted({(os.path.basename(f).split('_')[0], os.path.basename(f).split('_')[2][:-5]) for f in
                                                       glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'e1_tool', 'cache', 'v1s', '*_60_*.json')) if len(os.path.basename(f).split('_')) == 3})
tot = {}
for pair, mon in maps:
    plutus._MEMO.clear()
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            X, ch, R, pine = plutus.run(pair, mon, daily=(mode == 'daily'))
    except Exception as e:
        print(f"{pair} {mon}: RUN ERROR {e!r}"[:160], flush=True); continue
    b0, wk1 = D.boundary_ms(mon), D.week_end_ms(mon)
    b15 = [x for x in D.bars(pair, '15') if D.week_start_ms(mon) - 86400000 <= x['time'] < wk1 + 3 * 86400000]
    b60 = [x for x in D.bars(pair, '60') if D.week_start_ms(mon) - 86400000 <= x['time'] < wk1 + 3 * 86400000]
    st, row = {}, {'drawn': 0, 'filled': 0, 'TP': 0, 'SL': 0, 'OPEN': 0, 'NOT FILLED': 0}
    S = R['setups']
    for k, s in enumerate(S):
        x0 = E3._order_start(s, mon, b0)
        par = s.get('parent_ref'); j = next((i for i, q in enumerate(S) if q is par), None) if par is not None else None
        lng = s['dir'] == 'LONG'; rocket = s.get('category') == 'Reinforcement'
        trig = None
        if s.get('alt') and s.get('trigger'):
            lv, up = s['trigger']['level'], s['trigger']['dir'] == 'up'
            trig = next((x['time'] + 3600000 for x in b60 if x['time'] >= x0 and ((x['close'] > lv) if up else (x['close'] < lv))), None)
            if trig is None:
                st[k] = (None, None, 'NOT FILLED'); row['drawn'] += 1; row['NOT FILLED'] += 1; continue
        e = x = None; res = 'NOT FILLED'
        for b in b15:
            if e is None:
                if b['time'] < x0 or (trig is not None and b['time'] < trig): continue
                if j is not None:
                    pe, px, _ = st[j]
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
        st[k] = (e, x, res)
        row['drawn'] += 1; row[res] += 1; row['filled'] += 1 if e is not None else 0
    print(f"{pair} {mon} {mode}: drawn {row['drawn']} | filled {row['filled']} | TP {row['TP']} | SL {row['SL']} | open {row['OPEN']} | never filled {row['NOT FILLED']}", flush=True)
    for grp in ('ALL', pair, 'GOLDEN' if mon == '2026-07-06' else 'NOT GOLDEN'):
        t = tot.setdefault(grp, {kk: 0 for kk in row} | {'maps': 0})
        t['maps'] += 1
        for kk in row: t[kk] += row[kk]
for grp, t in tot.items():
    res = t['TP'] + t['SL']
    print(f"TOTAL {grp:<10} maps {t['maps']:>3} | drawn {t['drawn']:>4} | filled {t['filled']:>4} | TP {t['TP']:>4} | SL {t['SL']:>4} | open {t['OPEN']:>3} | never filled {t['NOT FILLED']:>4} | TP share of resolved {100 * t['TP'] / res if res else 0:.0f}%")
