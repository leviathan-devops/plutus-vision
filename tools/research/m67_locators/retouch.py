"""retouch.py MAPS - scratch LOCATOR for P533:209-212 / :497 ZONE REACTION COUNTER ('0 = virgin, 1-2 = active (has juice), 3+ = depleted'; 'Trend-aligned zones that cause a strong
reaction will almost always have THREE strong reactions before the zone fails'). Every E1 object of the week-anchor map; its touches in the week, in order. A touch = price reaches
the near edge from outside. Trade each touch: limit 0.5 pip in front, SL width + 2 clamped 5-15 (opt --slpad), TP 3R. A new touch counts only after the previous one resolved and
price left the zone. Tally by (touch number, results of the earlier touches)."""
import sys, io, contextlib, collections, argparse
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import plutus, e1_data as D
ap = argparse.ArgumentParser(); ap.add_argument('maps', nargs='+'); ap.add_argument('--rr', type=float, default=3.0); ap.add_argument('--smax', type=float, default=15)
A = ap.parse_args()
res = collections.defaultdict(lambda: [0, 0, 0])
def run_touches(b15, z, short, pip):
    w = (z['top'] - z['bot']) / pip
    sd = min(A.smax, max(5, w + 2)) * pip
    e = z['bot'] - 0.5 * pip if short else z['top'] + 0.5 * pip
    sl = e + sd if short else e - sd
    tp = e - A.rr * sd if short else e + A.rr * sd
    out, k, state = [], 0, 'away'
    if (short and b15[0]['close'] >= e) or ((not short) and b15[0]['close'] <= e): return out
    while k < len(b15):
        b = b15[k]
        if state == 'away':
            if (b['high'] >= e) if short else (b['low'] <= e): state = 'in'; continue
            k += 1; continue
        # in a trade from this bar
        r = None
        while k < len(b15):
            b = b15[k]
            if (b['high'] >= sl) if short else (b['low'] <= sl): r = 'SL'; break
            if (b['low'] <= tp) if short else (b['high'] >= tp): r = 'TP'; break
            k += 1
        if r is None: break
        out.append(r)
        if r == 'SL': break                       # the zone failed: no more trades on it
        # wait until price is back on the outside (it is, after a TP); next touch
        state = 'away'; k += 1
    return out
for m in A.maps:
    pair, mon = m.split(':')
    plutus._MEMO.clear()
    with contextlib.redirect_stdout(io.StringIO()):
        X = plutus._map(pair, mon)
    pip = D.PIP[pair]; b0, wk1 = D.boundary_ms(mon), D.week_end_ms(mon)
    b15 = [x for x in D.bars(pair, '15') if b0 - 15 * 60000 <= x['time'] < wk1]
    spot = b15[0]['close']
    objs = [(f"SD{z['tf']}", z, z['type'] == 'Supply') for z in X['sd']]
    objs += [(f"LQ{tf}", z, z['bot'] > spot) for tf, h in X['v1'].items() for z in h['liquidity']]
    objs += [("IP", z, z['bot'] > spot) for z in X['zones']]
    for cls, z, short in objs:
        if short and z['bot'] < spot: continue
        if (not short) and z['top'] > spot: continue
        seq = run_touches(b15, z, short, pip)
        for i, r in enumerate(seq):
            key = f"touch {i + 1}" + (f" after {i} wins" if i else '')
            for c in (key, f"{cls} {key}"):
                res[c][0] += 1; res[c][1] += r == 'TP'; res[c][2] += r == 'SL'
for cls in sorted(res, key=lambda c: (c.split()[0] != 'touch', c)):
    n, tp, sl = res[cls]
    if n >= 5 or cls.startswith('touch'):
        print(f"{cls:<26} n {n:4d}  TP {tp:4d}  SL {sl:4d}  win {100 * tp / max(1, tp + sl):5.1f}%")
