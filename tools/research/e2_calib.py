"""e2_calib.py [PAIR:MONDAY ...] - CALIBRATION LOCATOR for the five boundary states (memory/23 steps 6-7). BUILD WEEKS ONLY (never the golden, checkpoint or fresh weeks).
For every Engine 1 zone of the week-anchor map that price reaches from outside during the week (first touch, 30m candles): what did the candles do in the next 4 hours?
  CLEAN_BREAK    a 30m close beyond the far edge and the 4-hour window ends beyond it
  PIERCE_R       price trades beyond the far edge, then the window ends back inside the zone or on the side it came from
  WICK_RWL       never closes inside the zone; back outside the near edge within 3 candles and still outside at the end
  BODY_CONSOL    3 or more closes inside the zone, then out on the side it came from (or still inside at the end)
  BODY_WL        1-2 closes inside the zone, then out on the side it came from
Then: which inputs known AT THE ANCHOR separate the outcomes. Reads later bars to MEASURE; nothing here feeds the tool."""
import sys, os, io, contextlib, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'e1_tool'))
import plutus, e1_data as D, e2_chain as E2, e2_data as ED

BUILD = ('2026-02-02', '2026-02-09', '2026-02-16', '2026-02-23', '2026-03-02', '2026-03-09', '2026-03-16', '2026-03-23', '2026-04-06', '2026-08-17', '2026-08-31', '2026-09-21')
MAPS = [m.split(':') for m in sys.argv[1:]] or [(p, w) for w in BUILD for p in ('DXY', 'EURUSD', 'GBPUSD')]
FORBID = {'2026-07-06', '2026-04-13', '2026-04-20', '2026-05-18', '2026-10-05', '2026-03-30', '2026-05-25', '2026-07-13', '2026-09-28'}
rows = []
for pair, mon in MAPS:
    assert mon not in FORBID, 'test week - not a build week'
    with contextlib.redirect_stdout(io.StringIO()):
        X = plutus._map(pair, mon)
    pip = D.PIP[pair]; b0, w1 = D.boundary_ms(mon), D.week_end_ms(mon)
    bars = [x for x in D.bars(pair, '30') if b0 <= x['time'] < w1]
    P = ED.profile(pair, mon, b0)
    rungs = X['v1']['60']['liquidity']; bands = X['v1']['240']['liquidity']
    walls = [l for l in X['L'] if l['pillar'] == 8 and (l.get('notional_m') or 0) >= 850]
    lsz = [l['level'] for l in X.get('lsz', []) if not l.get('swept')]
    with contextlib.redirect_stdout(io.StringIO()):
        trend = E2.structure_4h(pair, mon)
    allz = [(q['bot'], q['top']) for q in X['zones'] if q.get('drawn')] + [(q['bot'], q['top']) for q in X['sd']] + [(q['bot'], q['top']) for q in bands]
    zs = [dict(z, _k='IP') for z in X['zones'] if z.get('drawn')] + [dict(z, _k='SD' + z['tf']) for z in X['sd'] if z['tf'] in ('240', '60', '30')]
    for z in zs:
        i_ = E2.info(z)
        for j in range(1, len(bars) - 9):
            pb, x = bars[j - 1], bars[j]
            up = pb['high'] < z['bot'] and x['high'] >= z['bot']; dn = pb['low'] > z['top'] and x['low'] <= z['top']
            if not (up or dn): continue
            if z['_k'] != 'IP' and ((up and z['type'] != 'Supply') or (dn and z['type'] != 'Demand')): break      # a supply zone is met from below, a demand zone from above
            near, far = (z['bot'], z['top']) if up else (z['top'], z['bot'])
            win = bars[j:j + 8]
            beyond = lambda v: (v > far) if up else (v < far)
            inside = lambda v: z['bot'] <= v <= z['top']
            outside = lambda v: (v < near) if up else (v > near)
            cl = [y['close'] for y in win]
            ext = max(y['high'] for y in win) if up else min(y['low'] for y in win)
            n_in = sum(inside(c) for c in cl)
            if beyond(cl[-1]) and any(beyond(c) for c in cl): out = 'CLEAN_BREAK'
            elif beyond(ext): out = 'PIERCE_R'
            elif n_in == 0 and all(outside(c) for c in cl[:3][-1:]) and outside(cl[-1]): out = 'WICK_RWL'
            elif n_in >= 3: out = 'BODY_CONSOL'
            elif n_in >= 1 and outside(cl[-1]): out = 'BODY_WL'
            elif n_in == 0: out = 'WICK_RWL'
            else: out = 'BODY_CONSOL'
            zv = ED.zone_volume(P, z) or {}
            w_p = (z['top'] - z['bot']) / pip
            rows.append({'out': out, 'kind': z['_k'], 'cls': i_['cls'], 'counter': i_['counter'], 'zfp': i_['zfp'], 'width': w_p,
                         'rel': zv.get('rel'), 'hvn': bool(zv.get('hvn_inside')), 'rim': (zv.get('rim_below') if up else zv.get('rim_above')),
                         'wall': any(z['bot'] - 3 * pip <= l['p'] <= z['top'] + 3 * pip for l in walls),
                         'rung_near': any(r['bot'] - pip <= near <= r['top'] + pip for r in rungs),
                         'liq_beyond': any((far < v <= far + 10 * pip) if up else (far - 10 * pip <= v < far) for v in lsz + [r['bot'] if up else r['top'] for r in rungs + bands]),
                         'pair': pair, 'day': (x['time'] - D.week_start_ms(mon)) // 86400000,
                         'trend': 'no 4H trend' if trend is None else ('WITH the 4H trend' if (trend == 'up') == up else 'AGAINST the 4H trend'),
                         'ses': (lambda h: 'Asia 17-02' if (h >= 17 or h < 2) else 'London 02-08' if h < 8 else 'NY am 08-12' if h < 12 else 'NY pm 12-17')(__import__('datetime').datetime.fromtimestamp(x['time'] / 1000, D.NY).hour),
                         'stack': sum(1 for a_, b_ in allz if a_ - 3 * pip <= z['top'] and b_ + 3 * pip >= z['bot']) - 1,
                         'refined': bool(z.get('refined')), 'nested': bool(z.get('nested_in')),
                         'run': abs(x['close'] - bars[max(0, j - 8)]['close']) / pip})
            break
OUT = ('WICK_RWL', 'BODY_WL', 'BODY_CONSOL', 'PIERCE_R', 'CLEAN_BREAK')
def table(title, key):
    g = collections.defaultdict(collections.Counter)
    for r in rows: g[key(r)][r['out']] += 1
    print(f"\n{title:<34}" + ''.join(f"{o:>13}" for o in OUT) + '      n   held')
    for k in sorted(g, key=lambda k: str(k)):
        n = sum(g[k].values())
        if n >= 8: print(f"  {str(k):<32}" + ''.join(f"{100 * g[k][o] / n:12.0f}%" for o in OUT) + f"  {n:5d}  {100 * (n - g[k]['CLEAN_BREAK']) / n:4.0f}%")
print(f"build maps {len(MAPS)}, first touches {len(rows)}")
table('ALL', lambda r: 'all')
table('zone kind', lambda r: r['kind'])
table('class | reaction counter', lambda r: (r['kind'][:2], r['cls'], r['counter']))
table('pressure zone ZFP', lambda r: None if r['zfp'] is None else ('ZFP<20' if r['zfp'] < 20 else 'ZFP 20-45' if r['zfp'] <= 45 else 'ZFP>45'))
table('volume inside vs profile mean', lambda r: None if r['rel'] is None else ('rel 0 (untraded)' if r['rel'] == 0 else 'rel<0.5' if r['rel'] < 0.5 else 'rel 0.5-1.5' if r['rel'] < 1.5 else 'rel>=1.5'))
table('high-volume node inside', lambda r: r['hvn'])
table('volume just before the near edge', lambda r: None if r['rim'] is None else ('rim<0.5 (vacuum)' if r['rim'] < 0.5 else 'rim>=0.5'))
table('option wall 850M+ at the zone', lambda r: r['wall'])
table('V1 rung on the near edge', lambda r: r['rung_near'])
table('liquidity within 10 p beyond far', lambda r: r['liq_beyond'])
table('zone width', lambda r: 'w<8p' if r['width'] < 8 else 'w 8-15p' if r['width'] < 15 else 'w>=15p')
table('pair', lambda r: r['pair'])
table('day of week (0 = Mon)', lambda r: int(r['day']))
table('approach vs 4H structure', lambda r: r['trend'])
table('session of the touch', lambda r: r['ses'])
table('other zones overlapping (stack)', lambda r: 'stack 0' if r['stack'] <= 0 else 'stack 1-2' if r['stack'] <= 2 else 'stack 3+')
table('refined / nested (S/D)', lambda r: None if r['kind'] == 'IP' else ('refined' if r['refined'] else 'nested in HTF' if r['nested'] else 'plain'))
table('move into the zone, prior 4 h', lambda r: 'run<10p' if r['run'] < 10 else 'run 10-25p' if r['run'] < 25 else 'run>=25p')
table('trend x session', lambda r: (r['trend'][:7], r['ses'][:6]))
table('trend x stack', lambda r: (r['trend'][:7], 'stack3+' if r['stack'] >= 3 else 'stack<3'))
table('trend x day', lambda r: (r['trend'][:7], int(r['day'])))
