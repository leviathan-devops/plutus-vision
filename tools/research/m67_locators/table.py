"""table.py BASE.json FINAL.json [HELD.json] -> markdown per pair-week: baseline vs final (trades + line)"""
import json, sys
b = {(r['pair'], r['mon']): r for r in json.load(open(sys.argv[1]))['rows'] if 'error' not in r}
f = {(r['pair'], r['mon']): r for r in json.load(open(sys.argv[2]))['rows'] if 'error' not in r}
def wr(r): return f"{100 * r['TP'] / (r['TP'] + r['SL']):.0f}%" if r['TP'] + r['SL'] else '-'
def ln(r): return f"{100 * r['within10'] / max(1, r['n30']):.0f}% / {r['miss'] / max(1, r['n30']):.1f}p"
print('| Week | Pair | BEFORE drawn / filled / TP / SL | win | line <=10p / miss | AFTER drawn / filled / TP / SL (void) | win | line <=10p / miss | visible moves |')
print('|---|---|---|---|---|---|---|---|---|')
for k in sorted(f, key=lambda k: (k[1], ['DXY', 'EURUSD', 'GBPUSD'].index(k[0]))):
    r1, r2 = b.get(k), f[k]
    a = f"{r1['drawn']} / {r1['filled']} / {r1['TP']} / {r1['SL']}" if r1 else '-'
    print(f"| {k[1]} | {k[0]} | {a} | {wr(r1) if r1 else '-'} | {ln(r1) if r1 else '-'} | {r2['drawn']} / {r2['filled']} / {r2['TP']} / {r2['SL']} ({r2.get('VOID', 0)}) | {wr(r2)} | {ln(r2)} | {r2['moves']} |")
for name, sel in (('DEV (8 weeks x 3)', lambda k: k[1] != '2026-07-06'), ('GOLDEN', lambda k: k[1] == '2026-07-06')):
    for lab, D_ in (('BEFORE', b), ('AFTER', f)):
        rs = [r for k, r in D_.items() if sel(k) and k in f]
        if not rs: continue
        t = {x: sum(r.get(x, 0) for r in rs) for x in ('drawn', 'filled', 'TP', 'SL', 'VOID', 'n30', 'within10', 'miss', 'turns', 'turn1')}
        print(f"\n**{name} {lab}**: {t['drawn']} drawn, {t['filled']} filled ({t['filled'] / len(rs):.1f} per pair-week), {t['TP']} TP, {t['SL']} SL" + (f", {t['VOID']} void" if t['VOID'] else '') +
              f" = {100 * t['TP'] / max(1, t['TP'] + t['SL']):.1f}% | line: {100 * t['within10'] / max(1, t['n30']):.0f}% of 30m closes within 10 pips, mean miss {t['miss'] / max(1, t['n30']):.1f} pips, 30m turns with a line vertex within one candle {t['turn1']} / {t['turns']}")
