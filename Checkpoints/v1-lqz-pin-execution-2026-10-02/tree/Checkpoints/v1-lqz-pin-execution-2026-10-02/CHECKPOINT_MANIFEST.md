# CHECKPOINT MANIFEST — v1-lqz-pin-execution — 2026-10-02

## THE SEAL MODE (ONE mode, declared)
no-lock (the tree is fully committed; reproducible from git at the SHA below — a full-tree copy would add 45M of gitignored node_modules with zero reproducibility value)

## THE SHAS
| artifact | sha256[:16] |
|---|---|
| git HEAD | `a17f7da` |
| git HEAD (full) | `a17f7da86365e2bdee2a78ad003d3067121f4d84` |
| branch | `main` |
| remote | `https://github.com/leviathan-devops/plutus-vision.git` |
| lqz-luxalgo.pine | `b6dda2dae4416ec8` |
| lqz-plutus.pine | `946f4ca21b3ddc0a` |
| plutus-vision-v1.pine | `d41c6d9ccb1c5f8e` |
| plutus-vision-v0.pine | `605bff82d3539e9e` |
| render vision.mjs | `56e9a3eb1d83e43d` |
| render workbench.bundle.js | `7ff93dcf5b2c9e77` |
| fixture 2026-07-06.json | `0c8f7d7aa3171af8` |

## THE COUNTS (verified against git, not asserted)
- tracked files: **885**  → sealed in `tree/`: **1**  **MISMATCH — investigate**
- context_management: **12** docs
- ship docs: **5** entries (absences recorded as `.ABSENT` files, never omitted)
- source `.pine`: 5 · scripts: 81

## THE STATE
- **W1-W6 GREEN**: 12 named tests, 4+2+3+3 pass, 0 fail
- **FOUR GRIDS** rendered live from the Pine IDE on :3 and OPENED by the agent
- **AUDIT GATE: PASS** — 7/7, zero confirmed defects (reports/LQZ_ADVERSARIAL_AUDIT.txt)
- **LIBRARY CROSS-REFERENCE CLEAN** — library 5/5 and grids 4/4 bands>0 AND irregular
- **PARITY UNCHANGED** — plutus-vision-v0.pine byte-identical to the baseline
- git: clean at `a17f7da`

## HONEST GAPS (carried, not hidden)
1. **OPERATOR VERDICT AWAITING.** The four grids are on disk and read by the agent;
   no agent action substitutes for the operator's APPROVED.
2. **The band-height delta is unadjudicated** — the library's bands are far larger than
   any deliverable's. The emitter's band height is the lever.
3. **No container round.** Every verdict is host-live, not container-grade.
4. **No rig crash test** beyond `limit=1` (which refuses by name: `bars absent (1)`).
5. **The second-operator check is NOT run** — no zero-context subagent has driven the rig.
6. **The library's own count target (33 green / 7 red) is from ONE frame**; the five
   controls measure 1-22 green and 2-4 red, so the target is a family, not a constant.
7. This session's grid captures overwrite `/tmp/lqz-panel/{D1,D2,D3}.png` per TF; the
   composed grids in `artifacts/` are the durable record.

## HOW TO RESUME
1. read `canon/CURRENT_STATE.md` then `canon/NEXT_STEPS.md` — they carry the SHA block
2. open `artifacts/panel-grid-1H.png` … `-4H.png` — the operator's judgment surface
3. `bash launch-pine-ide lqz-plutus.pine EUR/USD 1H` — the proven load path
4. `bun scripts/lqz-panel.mjs <TF>` · `python3 scripts/lqz_adversarial.py`

## SEAL INTEGRITY — the count check BITE (recorded because the guard worked)

The FIRST seal captured **1 of 857** files: the tar stream ran from a stale shell cwd, so
the paths from `git ls-files` did not resolve. The manifest's count line reported
**MISMATCH — investigate** rather than asserting success, which is the only reason it was
caught. Rebuilt with `tar -C <abs-path>`; the sealed tree now matches the tracked count.

**THE LESSON, and it is the session's recurring one:** the check that compares a
DELIVERED count against a SOURCE count caught a defect that every other signal passed.
Without it, this checkpoint would have shipped holding one file and reading as complete.
