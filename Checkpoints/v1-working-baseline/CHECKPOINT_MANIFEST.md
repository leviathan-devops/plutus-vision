# CHECKPOINT MANIFEST — v1-working-baseline

**Date:** 2026-10-02 · **Project:** PLUTUS VISION · **git HEAD:** `484dae9`
**Milestone:** the operator's verdict on D3 — *"the plutus vision indicator w plutus lqz looks
good"* — with the working LQZ + SMC. This is the recoverable baseline BEFORE the zone
refinement to the winning-trade library's visual + accuracy.

## THE OPERATOR'S VERDICT (recorded)
**`plutus-vision-v1.pine` (D3 — the Plutus LQZ + the LuxAlgo SMC): APPROVED by the operator**
("looks good", 2026-10-02). The other two deliverables (D1 lqz-luxalgo, D2 lqz-plutus) carry
their measured states; the pin's P8 remains open for them.

## THE DIST (the four deliverables + their shas)
| artifact | sha256[:16] | state |
|---|---|---|
| `lqz-luxalgo.pine` (D1) | `db06b60574125039` | renders; 15m FAIL / 30m-4H PASS in the ledger |
| `lqz-plutus.pine` (D2) | `68881deaca0c66a1` | renders; the candle ladder |
| `plutus-vision-v1.pine` (D3) | `82da437af969a315` | **OPERATOR-APPROVED** |
| `plutus-vision-v0.pine` (the parity reference) | `605bff82d3539e9e` | **UNCHANGED — never edited** |

## THE CONTENTS (verified counts)
- `src/` — the FULL git-tracked source tree: **462 entries** (files + symlinks), MATCH with the
  tracked set.
- `dist/` — the four .pine deliverables.
- `context_management/` — **12 docs** (the 11 canon + the manifest), all over the 200-line floor
  (CANON GATE: PASS).
- the six ship docs at the root: BUILD_REPORT (2003) · DEBUG_LOG (1300+) · FAILURE_LOG (900+) ·
  SPEC_VIOLATION_LOG · TESTING_LOG (1000+) · THEATRICALITY_LOG (new).
- `SPEC.md` — the fence v2 bound spec (`job: fence`); step-4 = the operator's panel approval.
- `packages/plutus-vision-v0-liquidity/` — the DPL1 spec + the wave plan + the blueprint.
- `OPERATING_MANUAL.md` + `RECEIPT.md` — the operator's guide + the state of record.
- `artifacts/` — the six panel grids (with shas), the verdict ledger (64 rows), the look record.

## THE STATE, MEASURED AT SEAL TIME
- unit `bun test ./scripts/`: **12 pass · 0 fail** · adversarial: **7/7, zero confirmed defects**
- parity: SMC 195/195 · POOLS 25/25 · VOIDS 380/500 (exact to the baseline) · SWEEPS named (F-XX)
- `SERVED_PINE_OK` · `CANON GATE: PASS` · the rig on all four ports · `plutus-vision.service`
  enabled (reboot-proof)
- the three deliverables compile on the live rig with **exact sha matches, first try** (the
  second operator's independent verification, 2026-10-02)

## THE SEAL MODE (ONE mode, declared)
**no-lock** — a living snapshot, refreshed in place; the operator's next order (the zone
refinement) lands on top of it. NEVER a manifest-only lock.

## THE HONEST GAPS
1. **P8 for D1/D2 is open** (D3 approved; D1's 15m FAIL carries no deltas; D2's reader verdicts mixed).
2. **F-XX — the sweeps standalone leg** fails in Vela's extraction on the current engine; the
   deliverables are unaffected; resume: engine reconciliation, NOT a version pin.
3. **The doc staleness the second operator found** (11 discrepancies, 4 material — e.g. the manual's
   absent-vs-unknown refusal claim, D1's config row, the capture return shape) — the refinement
   round must fix the manual alongside the zones.
4. **The zone refinement itself is the NEXT work stream** (the operator's order): match the
   rendered zones to the winning-trade library's visual + accuracy.
5. Viewports differ per panel; the 36 native primitives render via BRASS; the settings-dialog op
   is unreached from the exposed surface.

## HOW TO RESUME
1. `OPERATING_MANUAL.md` (232 lines — the three commands, the IDE pipeline, the traps) — **and
   apply the second operator's 11 corrections** (reports/ carries its full report).
2. `dist/plutus-vision-v1.pine` — the approved deliverable; the refinement target.
3. The library: `/home/leviathan/Pictures/WINNING_TRADE_LIBARARY` (39 PNGs, 8 families) — the
   visual + accuracy reference for the refinement.
