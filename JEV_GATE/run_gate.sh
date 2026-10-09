#!/usr/bin/env bash
# JEV_GATE — the ONLY success gate for the PLUTUS VISION indicator port.
# NO person, agent, unit test, exit code, or script decides. JEV decides.
# It is handed the FULL context (spec criteria + ship docs + graph + git + the artifact's
# evidence) and the artifact under test, and returns a single noul:
#   act  (>= 0.8) = YES, pass      noop/escalate = REJECT
#
# USAGE:  bash JEV_GATE/run_gate.sh [ARTIFACT_PATH]
# EXIT:   0 = JEV said YES — anything else = REJECTED
set -euo pipefail
export JM_JUDGE_URL="${JM_JUDGE_URL:-http://127.0.0.1:8090/v1/systemone}"
ROOT="/home/leviathan/JARVIS_WORKSPACE/Shared_Workspace/PLUTUS_VISION"
ART="${1:-$ROOT/pine-ide/ide/renderer/plutus-vision-v2.pine}"
WORK="$(mktemp -d /tmp/jev-gate.XXXXXX)"
CTX="$WORK/context.txt"

# ── ASSEMBLE A DENSE CONTEXT (the judge's payload cap is ~64KB) ──────────────────────────
{
  echo "=== THE MISSION (spec §0.1, verbatim) ==="
  sed -n '/### §0.1/,/### §0.2/p' "$ROOT/PLUTUS_VISION_INDICATOR_PORT_SPEC.md"
  echo; echo "=== THE 8 GOVERNING NON-NEGOTIABLES (spec §4) ==="
  sed -n '/## §4 /,/## §5 /p' "$ROOT/PLUTUS_VISION_INDICATOR_PORT_SPEC.md"
  echo; echo "=== THE SUCCESS CRITERIA (spec §6) ==="
  sed -n '/## §6 /,/## §7 /p' "$ROOT/PLUTUS_VISION_INDICATOR_PORT_SPEC.md"
  echo; echo "=== THE LATEST SHIP-DOC ENTRIES ==="
  for d in BUILD_REPORT DEBUG_LOG FAILURE_LOG SPEC_VIOLATION_LOG TESTING_LOG THEATRICALITY_LOG; do
    echo "--- $d.md (last entry) ---"; awk 'BEGIN{RS="\n\n"} END{print}' "$ROOT/$d.md" 2>/dev/null | head -40
  done
  echo; echo "=== THE GIT HISTORY (last 15) ==="
  git -C "$ROOT" log --oneline -15
  echo; echo "=== THE ARTIFACT EVIDENCE ($ART) ==="
  echo -n "baked-literal zone pushes (SC-19 requires 0): "
  grep -cE 'e1_injected_(top|bottom|cat|degree|zfp)\.push\([0-9]' "$ART" || true
  echo -n "live ta.*/request.security in the file: "
  grep -cE '\bta\.(pivothigh|pivotlow|highest|lowest|sma|ema|atr)|request\.security' "$ART" || true
  echo "sample of the zone arrays in the file:"
  grep -nE 'e1_injected_(top|bottom|cat|degree)\.push' "$ART" | head -8
} > "$CTX"

# cap the payload under the judge's limit (~48KB safe)
head -c 47000 "$CTX" > "$CTX.cap" && mv "$CTX.cap" "$CTX"

python3 - "$CTX" "$WORK/rows.jsonl" <<'PY'
import json, sys
ctx = open(sys.argv[1]).read()
open(sys.argv[2], "w").write(json.dumps({"id": "artifact-under-test",
    "text": "THE ARTIFACT UNDER TEST (with the full build context):\n" + ctx}) + "\n")
PY

jm decision-tree --rows "$WORK/rows.jsonl" --recipe "$ROOT/JEV_GATE/recipe.json" --out "$WORK/out.jsonl" 2>/dev/null

python3 - "$WORK/out.jsonl" <<'PY'
import json, sys
r = json.load(open(sys.argv[1]))[0]
a = r.get("answers", {}).get("pass", {})
print(f"JEV GATE: route={r.get('route')}  noul={a.get('noul')}")
if r.get("route") == "act":
    print("JEV VERDICT: YES — the artifact passes the gate."); sys.exit(0)
print("JEV VERDICT: NO — the artifact is REJECTED (any non-YES is a rejection)."); sys.exit(1)
PY
