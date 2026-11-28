"""zonehold.py MAPS... - scratch LOCATOR: every Engine 1 object of the week-anchor map, its FIRST touch in the week (approached from outside), traded as a limit 0.5 pip in front of
the near edge, SL = zone width + 2 pips clamped to 5-15 pips (GS Law 4), TP = 3 x SL (RRR floor 3.0). Per class: touches, TP, SL. Bars after the anchor = measurement only."""
import sys, os, io, contextlib, collections
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import plutus, e1_data as D
H = 3600000
res = collections.defaultdict(lambda: [0, 0, 0])
def trade(b15, i0, z, short, pip, cls):
    w = (z['top'] - z['bot']) / pip
    sd = min(15, max(5, w + 2)) * pip
    if short:
        e = z['bot'] - 0.5 * pip; sl = e + sd; tp = e - 3 * sd
    else:
        e = z['top'] + 0.5 * pip; sl = e - sd; tp = e + 3 * sd
    # first touch from outside after i0
    prev = b15[i0 - 1]['close'] if i0 > 0 else None
    if prev is None or (short and prev >= e) or ((not short) and prev <= e):
        return None
    f = None
    for k in range(i0, len(b15)):
        b = b15[k]
        if f is None:
            if (b['high'] >= e) if short else (b['low'] <= e): f = k
            else: continue
        if (b['high'] >= sl) if short else (b['low'] <= sl): return 'SL'
        if (b['low'] <= tp) if short else (b['high'] >= tp): return 'TP'
    return None if f is None else 'OPEN'
for m in sys.argv[1:]:
    pair, mon = m.split(':')
    plutus._MEMO.clear()
    with contextlib.redirect_stdout(io.StringIO()):
        X = plutus._map(pair, mon)
    pip = D.PIP[pair]; b0, wk1 = D.boundary_ms(mon), D.week_end_ms(mon)
    allb = D.bars(pair, '15')
    b15 = [x for x in allb if b0 - 15 * 60000 <= x['time'] < wk1 + 2 * 86400000]
    i0 = 1
    spot = b15[0]['close']
    objs = []
    for z in X['sd']:
        objs.append((f"SD {z['tf']:>3} {z['kind']} {'UM' if not z.get('mit') else 'M%d' % min(z['mit'], 3)}", z, z['type'] == 'Supply'))
    for tf, h in X['v1'].items():
        for z in h['liquidity']:
            objs.append((f"V1LQ {tf:>3}", z, z['bot'] > spot))
        for z in h['order_blocks']:
            objs.append((f"V1OB {tf:>3}", z, z['side'] == 'Supply'))
    for z in X['zones']:
        objs.append((f"IP {z['mech']['counter']} {z['mech']['bom']}", z, z['bot'] > spot))
    for z in X['lsz']:
        if not z['swept']:
            objs.append(("LSZ unswept", z, z['side'] == 'Supply-side'))
    for cls, z, short in objs:
        if short and z['bot'] < spot: continue
        if (not short) and z['top'] > spot: continue
        r = trade(b15, i0, z, short, pip, cls)
        if r is None: continue
        res[cls][0] += 1; res[cls][1] += r == 'TP'; res[cls][2] += r == 'SL'
        res['ALL'][0] += 1; res['ALL'][1] += r == 'TP'; res['ALL'][2] += r == 'SL'
for cls in sorted(res):
    n, tp, sl = res[cls]
    print(f"{cls:<24} touched {n:4d}  TP {tp:4d}  SL {sl:4d}  win {100 * tp / max(1, tp + sl):5.1f}%")
