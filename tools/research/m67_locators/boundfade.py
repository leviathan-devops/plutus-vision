"""boundfade.py - scratch LOCATOR: the PRODUCT's Engine 2 range day boxes (cached by ssfade.py): every touch of a box's ceiling / floor inside its day, traded 0.5 pip in front,
SL s pips beyond the bound, TP rr x SL; touches in order per bound per week (a new touch after the previous trade resolved). Tally by touch number."""
import sys, pickle, glob, os, collections
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import e1_data as D
SP = '/tmp/claude-0/-home-user-plutus-vision/b6c77a81-471c-536b-9631-0319cefbf3ab/scratchpad/loc/runs'
s_p = float(sys.argv[1]); rr = float(sys.argv[2])
res = collections.defaultdict(lambda: [0, 0, 0])
for f in sorted(glob.glob(f'{SP}/*.pkl')):
    pair, mon = os.path.basename(f)[:-4].split('_')
    if mon == '2026-07-06': continue
    X, days = pickle.load(open(f, 'rb'))
    pip = D.PIP[pair]; b15 = D.bars(pair, '15')
    for side in ('ceil', 'floor'):
        n = 0
        for d in days:
            if d['dir'] != 'range': continue
            lv = d['hi'] if side == 'ceil' else d['lo']
            short = side == 'ceil'
            e = lv - 0.5 * pip if short else lv + 0.5 * pip
            sl = lv + s_p * pip if short else lv - s_p * pip
            tp = e - rr * abs(sl - e) if short else e + rr * abs(sl - e)
            bars = [b for b in b15 if max(d['t0'], D.boundary_ms(mon)) <= b['time'] < d['t1']]
            k = 0; state = 'away'
            if not bars: continue
            if (short and bars[0]['close'] >= e) or ((not short) and bars[0]['close'] <= e): continue
            while k < len(bars):
                b = bars[k]
                if (b['high'] >= e) if short else (b['low'] <= e):
                    r = None
                    for b2 in b15[b15.index(b):]:
                        if (b2['high'] >= sl) if short else (b2['low'] <= sl): r = 'SL'; break
                        if (b2['low'] <= tp) if short else (b2['high'] >= tp): r = 'TP'; break
                    n += 1
                    key = f"touch {min(n, 3)}"
                    res[key][0] += 1; res[key][1] += r == 'TP'; res[key][2] += r == 'SL'
                    res['ALL'][0] += 1; res['ALL'][1] += r == 'TP'; res['ALL'][2] += r == 'SL'
                    # skip to the bar after the resolution
                    t_res = next((b2['time'] for b2 in b15[b15.index(b):] if ((b2['high'] >= sl) if short else (b2['low'] <= sl)) or ((b2['low'] <= tp) if short else (b2['high'] >= tp))), None)
                    if r == 'SL' or t_res is None: break
                    while k < len(bars) and bars[k]['time'] <= t_res: k += 1
                    continue
                k += 1
for c in sorted(res):
    n, tp, sl = res[c]
    print(f"s {s_p} rr {rr} {c:<8} n {n:3d} TP {tp:3d} SL {sl:3d} win {100 * tp / max(1, tp + sl):5.1f}%")
