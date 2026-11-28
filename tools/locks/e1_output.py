#!/usr/bin/env python3
"""e1_output.py snapshot|check [PAIR:MONDAY ...] - Engine 1 ZERO REGRESSIONS (charter memory/22 C1 / T1): a SHA-256 of the Engine 1 map (e1_pine.run) of every cached pair-week.
snapshot writes tools/locks/E1_OUTPUT.sha256.json; check recomputes and compares (exit 1 on any difference). The file lock tools/locks/check_e1.sh guards the sources; this guards the output."""
import sys, os, io, json, glob, hashlib, contextlib
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
sys.path.insert(0, os.path.join(ROOT, 'e1_tool'))
import e1_pine as EP, e1_data as D
F = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'E1_OUTPUT.sha256.json')
mode = sys.argv[1]
maps = [a.split(':') for a in sys.argv[2:]]
if not maps and mode == 'check' and os.path.exists(F):
    maps = [k.split(':') for k in sorted(json.load(open(F)))]
if not maps:
    weeks = sorted({os.path.basename(p)[:10] for p in glob.glob(os.path.join(ROOT, 'sidecar', 'out', '20*.json'))})
    maps = [(p, w) for w in weeks for p in ('DXY', 'EURUSD', 'GBPUSD')]
out = {}
for pair, mon in maps:
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            X = EP.run(pair, mon)
        out[f"{pair}:{mon}"] = hashlib.sha256(json.dumps(X, sort_keys=True, default=str).encode()).hexdigest()
    except Exception as ex:
        out[f"{pair}:{mon}"] = 'ERROR ' + type(ex).__name__
    print(pair, mon, out[f"{pair}:{mon}"][:16], flush=True)
if mode == 'snapshot':
    old = json.load(open(F)) if os.path.exists(F) else {}
    old.update(out); json.dump(old, open(F, 'w'), indent=0, sort_keys=True); print('snapshot written', len(out))
else:
    ref = json.load(open(F)); bad = [k for k in ref if out.get(k) != ref[k]]          # only pair-weeks that had an Engine 1 map at the snapshot (the others have no V1 harvest cached)
    print('E1 output:', 'IDENTICAL on %d pair-weeks' % len(ref) if not bad else 'CHANGED on ' + ', '.join(bad))
    sys.exit(1 if bad else 0)
