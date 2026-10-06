# VERDICT — PLUTUS VISION · E1 AUTOMATIC (the E1-E2 build)

_The legal-stop record. Written 2026-10-06. A fresh agent resumes from THIS + the checkpoint._

## THE VERDICT: 13/14 gates green · OPEN pending C16

| phase | gate | state |
|---|---|---|
| P0 baseline | the baseline re-measured (no memory numbers) | ✅ |
| P1 spec | the DPL1 spec APPROVED (0/8) + the wave-plan on disk | ✅ |
| P2 preflight | the build package + round-0 checkpoint | ✅ |
| P3 execute | every wave's deliverable on disk, suite green | ✅ |
| P4 runtime | the live render operated first-person (the replay, the play-forward, the video, the mimo verdict) | ✅ |
| P5 adversarial | A1-A7 9/9 PASS; the frontier named | ✅ |
| P6 document | the canon (12) + the 5 ship docs; AUDIT GATE PASS | ✅ |
| P7 checkpoint | src + dist+SHA + docs + manifest + seal | ✅ |
| P8 verdict | **C16 (the operator's look) PENDING** | ⏳ |

## THE RECEIPT (bound to tool results)

### The seal + the artifact
- **v1 seal** `0d20e8314ce992fc23e27f1b97fed76b981c84e78c647bbe6b3d6e1206517bd1` — byte-identical (the HARD-STOP target). Enforced at `scripts/lqz_vision_v2_build.py:1` (`verify_v1_untouched`) → `HARD STOP H1`.
- **v2** `7ebbe95b58217020` — the served copy == the tree == the checkpoint (all in sync).
- The build: `scripts/lqz_vision_v2_build.py:153` (`build_payload`) injects the E1 zones + the E2 path; the render is `plutus-vision-lqz/e1-render.pine:1` + `plutus-vision-lqz/e2-render.pine:1`.
- The engine: `scripts/e2_engine.py:97` (`classify`) · `:342` (`_next_target`) · `:456` (`day_decomposition`) · `:570` (`fine_path`).
- The E2 driver: `scripts/wire_e2.py:35` (`compute_momentum`) · `scripts/wire_e2.py:132` (the week validation).
- The backtest overlay: `scripts/pv-server.py:152` (`/api/v1/e1/zones`) · `pine-ide/ide/renderer/tabs/backtest.js:783` (`drawE1Zones`).

### The suites (this session)
`e1_st_18` 8 · `e1_st_19` 10 · `e1_st_20` 7 · `e1_st_21` 4 · `e1_st_22` 7 · `e1_st_26` 4 · `e2_tests` 36 — **0 failures**.

### C1-C15 (the spec's acceptance — run first-person)
C1 v1 byte-identical · C2 floor 226 · C3 no E3 · C4 the v1-drift refusal (`HARD STOP H1`, exit 1) · C5 the v8 renderer (5 helpers) · C6 anchor computed (0 `timestamp(2026)`) · C7 anchor chart-based (no `now()` call) · C8 the category (2 RES, 3 SUP) · C10 the zones land (6 boxes) · C11 replay-safe (`anchor.from=chart_last_bar`) · C12 the dead-source honesty (exit 0) · C13 no fabrication (144 labelled levels) · C14 the suites green · C15 the LSZ reference. **14/14 PASS.**

### A1-A7 (the adversarial loop — run against the deployed render)
A1 replay rewind (bars 2007→1608, restored) · A2 classify (RES/SUP) · A3 dead arm (exit 0) · A4 floor 226 · A5 seal tamper (exit 1, HARD STOP H1) · A6 empty payload (exit 1, HARD STOP) · A7 Sunday (Sun→Mon; the control Mon→Mon). **9/9 PASS** — the one initial "FAIL" (A7) was a probe error, adjudicated.

### AUDIT GATE
`ocr` (Alibaba OpenCodeReview) on `scripts/e2_engine.py` + `scripts/wire_e2.py`: 2 files, 13 comments, **0 critical**. Every finding fixed or proven a false positive. Recorded in `TESTING_LOG.md`.

## THE RUNTIME SEAT (H1-H7) — what running taught that reading could not
"I am the driver of the PLUTUS_VISION live render (:9851 + :9222 CDP)."
- **The play-forward method** (the operator's): the real DXY 1h bars (1881, Apr→Jul21) from the dashboard's own TV feed, replayed Jul 3 → Jul 11 as a 36-frame video, watched by **mimo-v2.6-flash** (the pinned vision model).
- **The verdict**: the price action **respects the zones** (a floor at the teal support, stall/reject at the orange resistance) — the E1 zones are ACCURATE.
- **The break** (every break is the deliverable): the E2 was a 5-vertex triangle, then a flat squiggle. The play-forward exposed **six defects**, all fixed:
  1. `wire_e2` passed `bars_momentum = 1.0` (a constant) → derived from the bars.
  2. `classify` anchored to the lowest support → the zone nearest the spot.
  3. `_next_target` walked to the adjacent zone → the FAR zone (the week's extreme).
  4. the day y was the zone's top edge → the zone MID.
  5. **my own TZ skew** (a naive `timestamp()`) → the sign had flipped; fixed, the direction now matches the week.
  6. a range shape (SS) anchored at the far support → the mid-range (the Equilibrium).

## THE FRONTIER (the named residual — no unstated gaps)
1. **C16** — the operator's look. The legal stop; cannot be self-certified.
2. **The E2 direction** is the momentum's sign — a weak, lookback-sensitive signal. The TZ fix made it match THIS week; a different week's bar set decides it.
3. **The backtest overlay draws zones at the chart's last bar**, not the room's future week (the room's Vite chart has no `xloc` future drawing) — it shows the levels, not the weekly projection.

## REPLICATION
```
repo   PLUTUS_VISION @ the checkpoint Checkpoints/e1-automatic-polish-2026-10-06/
build  PV2_PAIR=DXY PV2_WEEK=2026-07-06 python3 scripts/lqz_vision_v2_build.py
       -> plutus-vision-v2.pine  7ebbe95b58217020  (v1 verified untouched)
tests  python3 scripts/e1_st_18.py · scripts/e2_tests.py (0 fail)
rig    :9741 pine-station · :9854 VIL rail · :9851 pv-server · :9222 CDP
app    pine-ide  -> the 2-tab dashboard (PINE IDE + BACKTEST), the app on the operator display
```
