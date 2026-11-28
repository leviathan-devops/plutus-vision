"""cache the product's Engine 2 output (switch off) + the Engine 1 levels per map, so the gap forensics can iterate without re-running the engines"""
import sys, io, contextlib, pickle, os
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import plutus, e2_chain as E2, e1_data as D
for m in sys.argv[1:]:
    pair, mon = m.split(':')
    fn = f'gap/{pair}_{mon}.pkl'
    if os.path.exists(fn): continue
    plutus._MEMO.clear()
    with contextlib.redirect_stdout(io.StringIO()):
        X, ch, R, src = plutus.run(pair, mon, daily=True)
    lv = []
    for z in X['zones']:
        if z.get('drawn'): lv.append(('IP', z['bot'], z['top'], E2.info(z)))
    for z in X['sd']:
        lv.append(('SD' + z['tf'], z['bot'], z['top'], E2.info(z) | {'type': z['type']}))
    for tf in ('60', '240'):
        for z in X['v1'][tf]['liquidity']: lv.append(('LQ' + tf, z['bot'], z['top'], None))
    for l in X['lsz']:
        if not l['swept']: lv.append(('LSZ', l['level'], l['level'], None))
    for l in X['L']:
        if l['pillar'] == 8: lv.append(('OPT', l['p'], l['p'], {'cut': l.get('cut'), 'n': l.get('notional_m')}))
    days = [{k: d[k] for k in ('day', 'shapes', 'dir', 'lo', 'hi', 't0', 't1')} for d in ch['days']]
    pickle.dump({'pair': pair, 'mon': mon, 'segments': ch['segments'], 'days': days, 'levels': lv, 'U': X['U'], 'spot': X['spot'],
                 'chain': [(c['shape'], c['dir']) for c in ch['chain']]}, open(fn, 'wb'))
    print(pair, mon, len(ch['segments']), 'segs', len(lv), 'levels', flush=True)
