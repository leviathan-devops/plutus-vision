"""plutus.py - ONE command per week / pair -> ONE Pine v6 script (S6): Engine 1 map + Engine 2 shape chain + Engine 3 trade setups, every number from data closed before the Monday anchor.
usage: python3 plutus.py MONDAY PAIR [out.pine]      (PAIR = DXY | EURUSD | GBPUSD; default output e1_tool/out/PLUTUS_<PAIR>_<MONDAY>.pine)"""
import sys, os
import e1_pine as EP, e2_chain as E2

HERE = os.path.dirname(os.path.abspath(__file__))


def run(pair, monday):
    X = EP.run(pair, monday)
    lead = E2.build('DXY', monday, EP.run('DXY', monday)) if pair != 'DXY' else None      # DXY = master direction (P533:1899-1917; GS Law 7)
    chain = E2.build(pair, monday, X, lead)
    setups = []
    try:
        import e3_trades as E3
        setups = E3.build(pair, monday, X, chain)
    except ImportError:
        E3 = None
    extra = E2.pine(pair, monday, chain) + (E3.pine(pair, monday, setups) if E3 else []) + table(pair, monday, X, chain, setups)
    return X, chain, setups, EP.generate(pair, monday, X, extra, EP.reach(X, chain))


ACCENT = {'DXY': ('20,20,40', '100,150,255'), 'EURUSD': ('10,30,60', '80,140,255'), 'GBPUSD': ('40,15,50', '180,100,220')}       # P533 10.10 pair accent colours
PNAME = {'DXY': 'DXY', 'EURUSD': 'EUR/USD', 'GBPUSD': 'GBP/USD'}


def table(pair, monday, X, chain, R):
    """P533 Part X 10.7 'TABLE: 2x17' (position.top_right; background color.new(color.black, 10); border RGB 40,40,45): row 0 header (TRIDENT v8 | pair + week), 1 chain + confidence,
    2 alternative chain + confidence, 3 day-by-day shape, 4 ZONES header, 5-9 IP zones (five rows, top to bottom: PG4), 10 TRADES header, 11-13 short trade (entry / SL | TP / day + RRR),
    14-16 long trade; price format 10.9 (DXY #.##, pairs #.####); PG5 exact row indexing"""
    import datetime as dt
    f = (lambda v: '%.2f' % v) if pair == 'DXY' else (lambda v: '%.4f' % v)
    m0 = dt.date.fromisoformat(monday); m1 = m0 + dt.timedelta(days=4)
    wk = f"{m0.strftime('%b')}{m0.day}-{(m1.strftime('%b') if m1.month != m0.month else '')}{m1.day}"
    ch = chain.get('chain') or []
    alt = chain.get('alt') or {}
    altc = chain.get('alt_chain') or {}
    rows = [('TRIDENT v8', f"{PNAME[pair]} {wk}"),
            ('Chain', (' -> '.join(c['shape'] for c in ch) or '-') + (f" | {int(round(100 * ch[-1]['cum']))}%" if ch else '')),
            ('Alt chain', ((' -> '.join(c['shape'] for c in altc.get('chain', [])) + (f" | {int(round(100 * alt['conf']))}%" if alt.get('conf') is not None else '')) if altc.get('chain') else '-')),
            ('Days', ' | '.join(f"{d['day']} {'+'.join(d['shapes'])}" for d in chain.get('days', [])) or '-'),
            ('ZONES', '')]
    spot = X['spot']
    zs = sorted([z for z in X['zones'] if z.get('drawn')], key=lambda z: min(abs(z['bot'] - spot), abs(z['top'] - spot)))[:5]
    zs.sort(key=lambda z: -z['top'])
    for k in range(5):
        rows.append((zs[k]['name'], f"{f(zs[k]['bot'])}-{f(zs[k]['top'])} | {zs[k]['degree']} | {zs[k]['zfp']} ZFP") if k < len(zs) else ('-', '-'))
    rows.append(('TRADES', ''))
    S = (R or {}).get('setups', []) if isinstance(R, dict) else []
    for side in ('SHORT', 'LONG'):
        t = next((s for s in S if s['dir'] == side and not s.get('clone')), None)
        if t is None:
            rows += [(side.capitalize(), '-'), ('SL | TP', '-'), ('Day | RRR', '-')]
        else:
            rows += [(f"{side.capitalize()} {t['id']}", 'Entry ' + f(t['entry'])), ('SL | TP', f"{f(t['sl'])} | {f(t['tp'])}"), ('Day | RRR', f"{t['day']} {t['shape']} | {t['rrr']:.1f}R")]
    assert len(rows) == 17
    hb, ht = ACCENT[pair]
    o = ['    if show_tbl', '        var table tb = table.new(position.top_right, 2, 17, bgcolor=color.new(color.black, 10), border_color=color.rgb(40,40,45), border_width=1)']
    for i, (a, b) in enumerate(rows):
        head = i in (0, 4, 10)
        bg = f"color.rgb({hb})" if head else 'color.new(color.black, 10)'
        tc = f"color.rgb({ht})" if head else 'color.white'
        for col_, txt in ((0, a), (1, b)):
            o.append(f'        table.cell(tb, {col_}, {i}, "{txt}", text_color={tc}, bgcolor={bg}, text_size=size.small, text_halign=text.align_left)')
    return o


if __name__ == '__main__':
    monday, pair = sys.argv[1], sys.argv[2]
    out = sys.argv[3] if len(sys.argv) > 3 else os.path.join(HERE, 'out', f'PLUTUS_{pair}_{monday}.pine')
    X, chain, setups, src = run(pair, monday)
    open(out, 'w').write(src)
    print(out)
