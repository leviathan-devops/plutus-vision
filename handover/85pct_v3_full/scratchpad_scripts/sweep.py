"""sweep.py MODE [pairs...] - run the tool on every pair-week that has a cached V1 harvest at the week anchor (no Pinebox needed); print OK / ERROR per map (crash locator only)"""
import sys, os, io, contextlib, traceback, glob
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import plutus
mode = sys.argv[1]
pairs = sys.argv[2:] or ['DXY', 'EURUSD', 'GBPUSD']
maps = sorted({(os.path.basename(f).split('_')[0], os.path.basename(f).split('_')[2].replace('.json', '')) for f in glob.glob('/home/user/plutus-vision/e1_tool/cache/v1s/*_60_*.json') if len(os.path.basename(f).split('_')) == 3})
bad = 0
for pair, mon in maps:
    if pair not in pairs:
        continue
    plutus._MEMO.clear()
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            X, E2, R, pine = plutus.run(pair, mon, daily=(mode == 'daily'))
        print(f"{pair} {mon} {mode}: OK ({len(R['setups'])} orders, {len(pine.splitlines())} Pine lines)", flush=True)
    except Exception as e:
        bad += 1
        tb = traceback.extract_tb(sys.exc_info()[2])[-1]
        print(f"{pair} {mon} {mode}: ERROR {e!r} at {os.path.basename(tb.filename)}:{tb.lineno}", flush=True)
print(f"SWEEP {mode}: {bad} errors")
