"""confl.py MAPS - scratch LOCATOR: FA 6 'E = Earth + Fire': first touch of an S/D zone (BoM / MoM) that overlaps a V1 liquidity band (any TF) vs one that does not;
split by alignment with the 4H structure at the anchor (P533:2649, e2_chain.structure_4h). Trade = limit 0.5 pip in front, SL zone width + 2 clamped 5-15 pips, TP 3R."""
import sys, io, contextlib, collections
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import plutus, e1_data as D, e2_chain as E2M
res = collections.defaultdict(lambda: [0, 0, 0])
def trade(b15, z, short, pip, sdmax=15):
    w = (z['top'] - z['bot']) / pip
    sd = min(sdmax, max(5, w + 2)) * pip
    e = z['bot'] - 0.5 * pip if short else z['top'] + 0.5 * pip
    sl = e + sd if short else e - sd
    tp = e - 3 * sd if short else e + 3 * sd
    if (short and b15[0]['close'] >= e) or ((not short) and b15[0]['close'] <= e): return None
    f = None
    for b in b15[1:]:
        if f is None:
            if (b['high'] >= e) if short else (b['low'] <= e): f = 1
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
    b15 = [x for x in D.bars(pair, '15') if b0 - 15 * 60000 <= x['time'] < wk1 + 2 * 86400000]
    spot = b15[0]['close']
    st = E2M.structure_4h(pair, mon)
    bands = [b for tf, h in X['v1'].items() for b in h['liquidity']]
    for z in X['sd']:
        short = z['type'] == 'Supply'
        if short and z['bot'] < spot: continue
        if (not short) and z['top'] > spot: continue
        ov = any(b['bot'] <= z['top'] and b['top'] >= z['bot'] for b in bands)
        al = 'aligned' if st and ((st == 'down') == short) else ('counter' if st else 'mixed')
        r = trade(b15, z, short, pip)
        if r is None: continue
        for cls in (f"{z['kind']} {'+LQ' if ov else 'noLQ'}", f"{z['kind']} {'+LQ' if ov else 'noLQ'} {al}", f"{z['kind']} {'UM' if not z.get('mit') else 'M'} {'+LQ' if ov else 'noLQ'} {al}", 'ALL'):
            res[cls][0] += 1; res[cls][1] += r == 'TP'; res[cls][2] += r == 'SL'
for cls in sorted(res):
    n, tp, sl = res[cls]
    print(f"{cls:<28} touched {n:4d}  TP {tp:4d}  SL {sl:4d}  win {100 * tp / max(1, tp + sl):5.1f}%")
