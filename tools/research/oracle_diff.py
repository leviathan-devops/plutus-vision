"""oracle_diff.py PAIR [MONDAY=2026-07-06] - bug locator only (never a verdict, A5): distance of each setup of the tool to the operator's own golden-week trades
(context_management/oracle/golden_week.json). Moved out of e3_trades.py (G2 audit D-03: no week literal and no oracle read inside an engine module)."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'e1_tool'))
import e1_data as D, plutus

pair = sys.argv[1]
monday = sys.argv[2] if len(sys.argv) > 2 else '2026-07-06'
O = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'context_management', 'oracle', 'golden_week.json')))[pair]
X, E2, R, src = plutus.run(pair, monday)
pip = D.PIP[pair]
f = '%.3f' if pair == 'DXY' else '%.5f'
print(f'{pair} {monday}: nearest oracle trade per setup (pips off: entry / SL / TP)')
for s in R['setups']:
    best = min((t for t in O['trades'] if t['dir'] == s['dir'] and t.get('tp')), key=lambda t: abs(t['entry'] - s['entry']) + abs(t['tp'] - s['tp']), default=None)
    if best:
        print(f"  {s['id']} {s['day']} {s['shape']:<6} {s['dir']:<5} {f % s['entry']} / {f % s['sl']} / {f % s['tp']} vs #{best['n']} {best['day']}: "
              f"{abs(best['entry'] - s['entry']) / pip:5.1f} / {abs(best['sl'] - s['sl']) / pip:5.1f} / {abs(best['tp'] - s['tp']) / pip:5.1f}")
