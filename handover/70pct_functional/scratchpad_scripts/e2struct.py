import sys, io, contextlib
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import plutus, e1_data as D, e2_chain as E
DAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')
def struct(pair, mon, k, n=None):
    b = D.closed(pair, '240', mon)
    if n: b = b[-n:]
    hs = [i for i in range(k, len(b) - k) if b[i]['high'] == max(x['high'] for x in b[i - k:i + k + 1])]
    ls = [i for i in range(k, len(b) - k) if b[i]['low'] == min(x['low'] for x in b[i - k:i + k + 1])]
    if len(hs) >= 2 and len(ls) >= 2:
        hh, hl = b[hs[-1]]['high'] > b[hs[-2]]['high'], b[ls[-1]]['low'] > b[ls[-2]]['low']
        return 'up' if hh and hl else 'down' if (not hh and not hl) else None
    return None
tally = {}
rows = []
for m in sys.argv[1:]:
    pair, mon = m.split(':')
    with contextlib.redirect_stdout(io.StringIO()):
        X, E2, E3, src = plutus.run(pair, mon)
    pip = D.PIP[pair]
    b = [x for x in D.bars(pair, '60') if D.boundary_ms(mon) <= x['time'] < D.week_end_ms(mon)]
    d0 = E2['days'][0]; lo, hi = d0.get('lo'), d0.get('hi')
    first = None
    for x in b:
        if x['close'] > hi + 5 * pip: first = 'up'; break
        if x['close'] < lo - 5 * pip: first = 'down'; break
    C = b[-1]['close']
    net = 'up' if C > hi else 'down' if C < lo else None
    wk = 'up' if C - X['spot'] > 20 * pip else 'down' if X['spot'] - C > 20 * pip else None
    r = {f's{k}': struct(pair, mon, k) for k in (2, 3, 5)}
    r['ema'] = E.trend_4h(pair, mon)
    r['story'] = E.storyline(pair, mon, X['spot'], X['U'])[0]
    print(mon, 'first', first, 'net', net, 'wk', wk, r)
    for tgt_name, tgt in (('first', first), ('net', net), ('wk', wk)):
        if tgt:
            for k, v in r.items():
                t = tally.setdefault((tgt_name, k), [0, 0, 0])
                t[2 if v is None else 0 if v == tgt else 1] += 1
for k in sorted(tally): print(k, tally[k])
