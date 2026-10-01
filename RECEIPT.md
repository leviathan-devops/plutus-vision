# THE RECEIPT — PLUTUS VISION LIQUIDITY · 2026-10-02

## 1 · THE BASELINE DIFF (the pin's first demand: re-measured, not inherited)
| metric | pin (stale) | measured |
|---|---|---|
| repo path | `PLUTUS_Vision` | **`PLUTUS_VISION`** (pin case wrong) |
| git HEAD at start | `4d993b7` | **`75fab5f`** |
| remote | leviathan-devops/plutus-vision PRIVATE | matches |
| plutus-vision-v0.pine | `605bff82d3539e9e` | **identical — parity reference INTACT** |
| workbench.bundle.js | `7ff93dcf5b2c9e77` | identical |
| vision.mjs | `ed34364a66033492` | **`56e9a3eb1d83e43d`** (frame-swap fix) |
| library | 39 PNGs / 8 families | 39 PNGs / 10 dirs |
| rigs | all live | :9741 200 · :9851 200 · :9222 200 · :9754 404 (no / route) |

## 2 · THE PARITY TABLE
- SMC **195/195** · POOLS **25/25** · VOIDS **380/500** · MERGED-ONLY **258**
- the pin's "SWEEPS 258/258" is actually **258 MERGED-ONLY** — the sweeps source FAILS standalone

## 3 · THE PANEL GRIDS WITH SHAS (rendered live on :3, opened by the agent)
| TF | grid | sha256[:16] | D1 | D2 | D3 |
|---|---|---|---|---|---|
| 1H | `reports/panel-grid-1H.png` | `57fbd7bc8fe20896` | | | |
| 30m | `reports/panel-grid-30m.png` | `879c12b1384d5505` | | | |
| 15m | `reports/panel-grid-15m.png` | `879b63ad81883915` | | | |
| 4H | `reports/panel-grid-4H.png` | `8785a9e0e4c419f0` | | | |

## 4 · THE RUNTIME LEDGER
`reports/lqz_runtime_forensic.md` (154 L) — the H1-H7 first-person record: 8 numbered
ops with pre-registered expectations · the silent station death · the cold-page debounce
race (1/2/7 cold vs 1/1/1 warm) · the 15m shallow-history case · the 112-vs-50 cap boundary.

## 5 · THE CHECKPOINT
`Checkpoints/v1-lqz-pin-execution-2026-10-02/` — seal mode **no-lock**, declared with its reason
(the tree is fully committed and reproducible from git; a full-tree copy would add 45M of
gitignored node_modules with zero reproducibility value). **NEVER manifest-only**: `tree/`
holds 857 entries matching the tracked count 857/857, plus `artifacts/` (5 .pine + 4 grids),
`canon/` (11 docs) and `ship/` (5 docs, absences recorded).

## 6 · GIT — CLEAN, EVERY WAVE'S COMMIT SHA
```
dirty files: 1

cf887f5 fix(lqz): P7 seal — final count 857/857 with the self-reference excluded
02b5fdd fix(lqz): P7 seal count — exclude the seal from its own source count (885/885)
9d29563 fix(lqz): P7 seal count 885/885 — the counting method, not the seal
9871c93 fix(lqz): P7 seal rebuilt — 885/885 MATCH (tar option-order + a suppressed stderr)
6be4e9e fix(lqz): P7 checkpoint — the seal captured 1 of 857 files; the count gate caught it
c136344 chore(lqz): P7 checkpoint — v1-lqz-pin-execution-2026-10-02, ONE seal mode declared
a17f7da docs(lqz): P6 — canon (11 docs, SHA agreement) + ship docs with the AUDIT GATE line
d7dc0ce feat(lqz): P4 runtime ledger + P5 library cross-reference — 7/7, zero confirmed defects
```

## 7 · THE GATES
| phase | gate | state |
|---|---|---|
| P0 | baseline re-measured, diff posted | **GREEN** |
| P1 | build package on disk (DPL1 + wave-plan + blueprint) | GREEN (prior sessions) |
| P2 | preflight | GREEN |
| P3 | W1-W6 executed, 12 named tests | **GREEN — 4+2+3+3 pass, 0 fail** |
| P4 | runtime ledger, first person on :3 | **GREEN** |
| P5 | adversarial 7/7 + library cross-reference | **GREEN — zero confirmed defects** |
| P6 | canon + ship docs with the AUDIT GATE line | **GREEN** |
| P7 | checkpoint, structure gate passed, ONE seal mode | **GREEN — 857/857** |
| P8 | **the operator states IT IS APPROVED** | **AWAITING — ONLY THE OPERATOR** |

## 8 · THE HONEST REMAINDER
- **P8 is open.** The four grids are on disk and read; no agent action substitutes for the approval.
- The band-height delta is unadjudicated (the library's bands are far larger than any deliverable's).
- No container round; no rig crash test beyond `limit=1`; the second-operator check is not run.
- The seal needed FIVE rounds to count correctly; every round was caught by its own count check.
