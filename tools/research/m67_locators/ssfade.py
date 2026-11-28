"""ssfade.py MAPS - scratch LOCATOR: inside each day box that the PRODUCT's Engine 2 draws as a range (dir 'range'), every 15m / 30m / 1H S/D zone and V1 liquidity band of the
week-anchor map lying inside the box: supply / band in the upper half -> short at the first touch from below inside that day; demand / band in the lower half -> long.
SL = width + 2 pips clamped 5-15, TP = 3R (tp3) and TP = the box's far side if RR >= 3 (tpfar). Measures only."""
import sys, io, contextlib, collections, pickle, os
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import plutus, e1_data as D
SP = '/tmp/claude-0/-home-user-plutus-vision/b6c77a81-471c-536b-9631-0319cefbf3ab/scratchpad/loc/runs'
os.makedirs(SP, exist_ok=True)
res = collections.defaultdict(lambda: [0, 0, 0])
def go(b15, t0, t1, e, sl, tp, short):
    f = None
    for b in b15:
        if b['time'] < t0: continue
        if f is None:
            if b['time'] >= t1: return None
            if (b['high'] >= e) if short else (b['low'] <= e): f = b['time']
            else: continue
        if (b['high'] >= sl) if short else (b['low'] <= sl): return 'SL'
        if (b['low'] <= tp) if short else (b['high'] >= tp): return 'TP'
    return None if f is None else 'OPEN'
for m in sys.argv[1:]:
    pair, mon = m.split(':')
    pk = f"{SP}/{pair}_{mon}.pkl"
    if os.path.exists(pk):
        X, days = pickle.load(open(pk, 'rb'))
    else:
        plutus._MEMO.clear()
        with contextlib.redirect_stdout(io.StringIO()):
            X, ch, R, pine = plutus.run(pair, mon, daily=True)
        days = [{k: d[k] for k in ('day', 'lo', 'hi', 'dir', 'shapes', 't0', 't1')} for d in ch['days']]
        Xs = {'sd': X['sd'], 'v1': {tf: {'liquidity': h['liquidity']} for tf, h in X['v1'].items()}}
        pickle.dump((Xs, days), open(pk, 'wb')); X = Xs
    pip = D.PIP[pair]
    b15 = D.bars(pair, '15')
    for d in days:
        if d['dir'] != 'range': continue
        lo, hi = d['lo'], d['hi']; mid = (lo + hi) / 2
        t0, t1 = max(d['t0'], D.boundary_ms(mon)), d['t1']
        pre = [b for b in b15 if b['time'] < t0]
        if not pre: continue
        p0 = pre[-1]['close']
        objs = [(f"SD{z['tf']} {z['kind']}", z, z['type'] == 'Supply') for z in X['sd'] if z['tf'] in ('15', '30', '60')]
        objs += [(f"LQ{tf}", z, None) for tf, h in X['v1'].items() for z in h['liquidity']]
        for cls, z, short in objs:
            if not (lo <= z['bot'] and z['top'] <= hi): continue
            up_half = z['bot'] > mid
            if short is None: short = up_half
            if short != up_half: continue
            if short and z['bot'] <= p0: continue
            if (not short) and z['top'] >= p0: continue
            w = (z['top'] - z['bot']) / pip
            sd = min(15, max(5, w + 2)) * pip
            e = z['bot'] - 0.5 * pip if short else z['top'] + 0.5 * pip
            sl = e + sd if short else e - sd
            for tpn, tp in (('tp3', e - 3 * sd if short else e + 3 * sd), ('tpfar', lo + 1.5 * pip if short else hi - 1.5 * pip)):
                if tpn == 'tpfar' and abs(tp - e) < 3 * sd: continue
                r = go(b15, t0, t1, e, sl, tp, short)
                if r is None: continue
                for c in (f"{tpn} {cls}", f"{tpn} ALL"):
                    res[c][0] += 1; res[c][1] += r == 'TP'; res[c][2] += r == 'SL'
for cls in sorted(res):
    n, tp, sl = res[cls]
    print(f"{cls:<22} n {n:4d}  TP {tp:4d}  SL {sl:4d}  win {100 * tp / max(1, tp + sl):5.1f}%")
