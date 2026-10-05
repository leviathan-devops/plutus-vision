# CHECKPOINT MANIFEST — v2-working-baseline-2026-10-05

**Date:** 2026-10-05 · **Project:** PLUTUS VISION · **git HEAD:** c5833dd
**Seal mode:** NO-LOCK (mutable working snapshot; the v1 SHA is checked by every build — the H1 guard is the seal)
**Milestone:** THE V2 WORKING BASELINE — the E1 institutional-pressure zones rendered ON TOP OF the
V1 baseline. The operator: "We at least have a working baseline now."

## THE ARTIFACT FINGERPRINTS
| artifact | sha256 (16) | lines |
|---|---|---|
| `dist/plutus-vision-v2.pine` | `5c4db077bc4d089b` | 1664 |
| `dist/plutus-vision-v1.pine` (the sealed baseline) | `0d20e8314ce992fc` | 1270 |
| `visual/runtime-state.png` | `$(sha256sum visual/runtime-state.png | cut -c1-16)` | — |

## THE STATE (what this checkpoint IS)
- `plutus-vision-v2.pine` = the SEALED v1 baseline (candle liquidity + LuxAlgo SMC) + the E1 layer.
- The E1 layer renders the **5 INSTITUTIONAL ROLES** (Trident 5.3.3 §5.2.1): IP Resistance
  Ceiling | Heavy → IP Support Floor | Moderate-Heavy, spread across the week (100.60–101.50), the
  canon colour ladder (RES=red · MID=#FF9800 · SUP=teal), the label at the zone mid, `calcZFP`,
  the LSZ removed.
- The data: the 5 roles from `scripts/e1_extract.py:synthesize_institutional_zones()` (the week's
  own data, week 2026-07-06, spot 101.048).

## THE VALIDATED
- v1 seal intact (`0d20e831…`, HARD STOP H1 not tripped).
- battery 6/6 pass (ST-18 8/0 · ST-19 10/0 · ST-20 7/0 · ST-21 4/0 · ST-26 4/0 · ST-22 7/0).
- container 6/6 (python:3.12-slim, hermetic).
- the full code audit: the verboo lane — the critical (the E1/E2 week-mix) FIXED; round-2 0 criticals.
- the live render: the 5 labeled institutional zones on the DXY chart (census 37 boxes · 20 labels).

## THE CONTENTS
- `src/` — the E1 pipeline (e1_week / e1_category / e1_extract / e1_sources / e1_vlm_options /
  e1_judge / lqz_vision_v2_build + the 6 suites).
- `dist/` — the v2 artifact + the sealed v1.
- `lqz/` — the E1 render layer (`e1-render.pine`).
- `data/` — the E1 payloads (`DXY-2026-07-06.json`, `EURUSD-2026-07-06.json`).
- `context_management/` — the 12 canon docs.
- the 7 ship docs (incl. `VISUAL_CHECKPOINTS_LOG.md`).
- `visual/runtime-state.png` — the LIVE render (the V1 baseline + the 5 E1 zones on DXY).

## THE HONEST GAPS (what is NOT yet done — the operator's active work)
1. **The zones ACCURATE to the week.** The degrees currently follow the canon's STRUCTURAL SHAPE
   (the role weight) + the week's confluence — NOT yet the 9-source engine synthesis.
2. **The ACTIVE-week dynamic render.** The zones are anchored to the fixture's window (2026-07-06),
   not yet the operator's LIVE active trading week.
3. **The ENGINE-2 shape chain.** NOT drawn on the chart yet.

## THE NEXT WORK
See `context_management/NEXT_STEPS.md` — the 3 fronts above.
