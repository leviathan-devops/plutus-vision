"""sweep_daily.py ROOT - daily-mode run on the 15 pair-weeks with per-day V1 caches; OK / ERROR per map (crash locator only)"""
import sys, os, io, contextlib, traceback
root = sys.argv[1]
sys.path.insert(0, os.path.join(root, 'e1_tool'))
import plutus
bad = 0
for mon in ('2026-04-13', '2026-04-20', '2026-05-18', '2026-07-06', '2026-10-05'):
    for pair in ('DXY', 'EURUSD', 'GBPUSD'):
        plutus._MEMO.clear()
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                X, E2, R, pine = plutus.run(pair, mon, daily=True)
            print(f"{pair} {mon} daily: OK ({len(R['setups'])} orders, {len(pine.splitlines())} Pine lines)", flush=True)
        except Exception as e:
            bad += 1
            tb = traceback.extract_tb(sys.exc_info()[2])[-1]
            print(f"{pair} {mon} daily: ERROR {e!r} at {os.path.basename(tb.filename)}:{tb.lineno}", flush=True)
print(f"SWEEP daily: {bad} errors")
