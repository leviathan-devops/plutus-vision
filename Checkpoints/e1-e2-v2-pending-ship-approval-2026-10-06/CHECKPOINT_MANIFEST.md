# CHECKPOINT — e1-e2-v2-pending-ship-approval-2026-10-06

**STATE: V2 PENDING SHIP APPROVAL.** The operator's own look (C16, 2026-10-06): *"This is very
good progress... Not bad. I like that the engine two is reacting to the engine one — good, that's
how it's supposed to be."* The C16 gate PASSED. The SHIP remains PENDING the 5-week
cross-validation (the next phase).

## THE DIST (the artifact)
| artifact | sha256 |
|---|---|
| `plutus-vision-v2.pine` | `282517ac622769bdb34296ebee94fa8079da28dbab30bff1c27ae2146a74f011` |
| `plutus-vision-v1.pine` | `0d20e8314ce992fc23e27f1b97fed76b981c84e78c647bbe6b3d6e1206517bd1` |

`sha256sum` verified at seal time; the v2 here == the served copy == the tree == the prior
checkpoint's render (ZERO drift).

## THE STATE (what is validated / what is pending)
VALIDATED:
- C1–C15 (14/14) · A1–A7 (9/9) · the ocr AUDIT GATE PASS · the independent re-verification 12/13
  (+1 W5 adjudicated a probe-error).
- The E1/E2 render: 6 labelled institutional-pressure zones + the E2 predicted path, drawn
  together, no wall (drawings scene 846 → 29).
- The E2 accuracy on the TARGET week (Jul 6–11): MAE 0.0979 vs the actual.
- The v1 seal byte-identical (the HARD STOP H1 target).
- C16 — the operator's look: **PASSED**.

PENDING:
- **The 5-week cross-validation** (the operator's directive): pick 5 random trading weeks in the
  last 6 months; rewind to each; verify (1) the dynamic week rendering fires for THAT week and
  (2) the macro-level E1/E2 accuracy across random weeks. THIS is the litmus test before ship.

## THE CONTENTS
| path | content | count |
|---|---|---|
| `src/scripts/` | the full pipeline (e1_week, e1_category, e1_extract, e2_engine, wire_e2, lqz_vision_v2_build, pv-server, the ST suites) | 89 `.py` |
| `src/plutus-vision-lqz/` | the render sources (e1-render.pine, e2-render.pine) | 5 `.pine` |
| `dist/` | the built artifacts + SHA256SUMS | 3 |
| `context_management/` | the full canon | 12 docs |
| the 5 ship docs | BUILD_REPORT (2220) · DEBUG_LOG (2050) · FAILURE_LOG (903) · SPEC_VIOLATION_LOG (283) · TESTING_LOG (1633) | 5 |
| `visual/runtime-state.png` | the live runtime capture (the app: 6 zones + the E2 path) | sha bf0d72dc66652585 |
| `artifacts/package/` | the DPL1 spec + the wave-plan + the blueprint | (the build package) |
| `artifacts/data-snapshot/` | the E1/E2 payloads (the data the render consumed) | 8 |

## THE HONEST GAPS (the unstated-absence rule is satisfied)
1. **The 5-week cross-validation is NOT run** — it is the pending phase (named above).
2. **The E2 direction** is the momentum's sign (a weak signal). The TZ fix made it match the
   target week; whether it generalizes is exactly what the 5-week test will measure.
3. **The BACKTEST overlay** draws the zones at the chart's last bar, not the room's future week
   (the room's Vite chart has no future drawing).
4. The `visual/runtime-state.png` is the operator-display capture; the map's EDGE cases (a replay
   mid-week) are not separately captured.

## THE REPLICATION RECIPE
```
build  PV2_PAIR=DXY PV2_WEEK=<the-week> python3 scripts/lqz_vision_v2_build.py
       -> plutus-vision-v2.pine  (v1 verified untouched -> HARD STOP H1 on any drift)
tests  python3 scripts/e1_st_18.py · scripts/e2_tests.py · scripts/e1_tests.py  (0 fail)
rig    :9741 pine-station · :9851 pv-server · :9222 CDP
app    pine-ide  -> the 2-tab dashboard (PINE IDE + BACKTEST)
```

## THE NEXT WORK (the queued phase)
The 5-week cross-validation: 5 random trading weeks in the last 6 months, each rewound on the
chart, the pipeline run per week, the E1 zones + E2 path rendered, the accuracy measured vs the
actual. The ship decision follows the verdicts.
