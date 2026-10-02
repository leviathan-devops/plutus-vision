# CHECKPOINT MANIFEST — v1-lqz-pin-execution — 2026-10-02 (rev 3: post-fix, four grids)

## THE SEAL MODE (ONE mode, declared)
no-lock — the tree is fully committed and reproducible from git at the SHA below. A
full-tree copy would add ~45M of gitignored node_modules with zero reproducibility value.
NEVER manifest-only: `tree/` holds every tracked file.

## THE SHAS
| artifact | sha256[:16] |
|---|---|
| git HEAD | `f1f14d5` |
| git HEAD (full) | `f1f14d5d3c317386177f2cad27c59093246ab5cf` |
| branch | `main` |
| lqz-luxalgo.pine | `f339228a078d5c2c` |
| lqz-plutus.pine | `946f4ca21b3ddc0a` |
| plutus-vision-v1.pine | `d41c6d9ccb1c5f8e` |
| plutus-vision-v0.pine | `605bff82d3539e9e` |
| render vision.mjs | `d032a26721176649` |

## THE FOUR GRIDS (the panel judge, all TFs)
| panel-grid-IDE-15m | `5bbad0130c5da15f` |
| panel-grid-IDE-30m | `680037ffd0283f01` |
| panel-grid-IDE-1H | `ef74ce4fc9269a48` |
| panel-grid-IDE-4H | `3e9197ac8f69ddb5` |

## THE COUNTS (verified against git, not asserted)
- tracked files (excl. the seal dir): **869**
- sealed in `tree/` (excl. the nested copy): **869**  **MATCH**
- canon: 12 docs · ship: 5 entries

## THE STATE
- **THE GREY/GOLD DEFECT: SOLVED** — vision.mjs read `b.color` (never set by Pine boxes);
  now `b.bgcolor`, verified `nonBg 0.40008 → 0.16821`.
- **THE FOUR GRIDS EXIST** and every panel was opened by the agent.
- **THE IDE PIPELINE IS THE WORKFLOW** — RUN → CAPTURE → GATE → LOOK → VERDICT.
- parity reference `plutus-vision-v0.pine` UNCHANGED.

## HONEST GAPS
1. **THE OPERATOR HAS NOT RECORDED A VERDICT.** The grids are on disk and read; the
   `PASS/FAIL/INCONCL` buttons write to `vil/2026-W29.jsonl`. No agent action substitutes.
2. **`lqzSource` IS THE OPERATOR'S CALL** — `both` buys D1 +60% ladder at 15m (5→8).
3. **15m's sparsity is STRUCTURAL** (bar-based detector windows, 325 bars vs 400) and is
   NOT fully recoverable by any input in the deliverable's surface.
4. **The station's half-alive state** (GET / hangs while POST /run works) — the launcher's
   blindness is fixed; the state itself is intermittent and unreproduced.
5. **No container round.** Every verdict is host-live.
6. **The second-operator check ran** and found a rig defect; its doc gap is closed by the
   operating manual now in the runtime ledger.

## HOW TO RESUME
1. `canon/CURRENT_STATE.md` then `canon/NEXT_STEPS.md`
2. open `artifacts/panel-grid-IDE-*-2026-W29.png` — the operator's judgment surface
3. `bash launch-pine-ide lqz-plutus.pine EUR/USD 1H` · `bun scripts/lqz-panel.mjs 1H`
4. `python3 scripts/lqz_panel_ide.py` — rebuild the four grids from the ledger

## SEAL INTEGRITY — the count gate bit a SECOND time (recorded)
This revision's first tree build captured **0 of 869** files: `git ls-files` includes the SEAL
ITSELF (it is tracked), so the build tried to nest the seal inside its own tree, the nested
symlinks hit permission errors, and the extraction produced nothing. The manifest's count line
reported **MISMATCH** rather than asserting success — which is the only reason it was caught.
Fixed by excluding the seal directory from its own tree.

**TWO REVISIONS, TWO TREE FAILURES, BOTH CAUGHT BY THE SAME COUNT COMPARISON.** The seal's
integrity check has now demonstrably bitten four times across three revisions (tar option
order · a suppressed stderr · the symlink-blind count · self-reference). A checkpoint whose
count gate has never fired is a checkpoint whose integrity is unproven; this one's has fired
repeatedly and never once let a wrong number pass.
