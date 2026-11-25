# 01 — CURRENT STATE (overwrite; keep under ~60 lines)
Updated: 2026-11-25 ~12:25 UTC (container clock)

## Where I am
- Phase: E1 BUILD, iterating in Pinebox. File: `indicator/plutus-vision-engines.pine` (engine layer; sealed V1 untouched at `indicator/plutus-vision-v1.sealed.pine`).
- Anchor guard DONE (`tools/anchor_guard.py`, pre-commit hook via core.hooksPath=tools/git-hooks, run-time assert in the script). Memory graph DONE (`tools/mem/mem q ...`).
- E1 engine today: higher-TF bars aggregated in-script; forecast frozen at Monday 02:00 NY; level set from pivots (W + 3 D), daily MA grid, prior-week fibs, price anchors,
  D1 + 4H swing-reaction clusters (repeats / role reversals), HWC/LWC, round grid; confluence-weighted; zones = confluence peaks (suppression = 0.15 from a zone's edges);
  weekly map = zones overlapping the prior week's range + first zone beyond each end; canon gap in-fill (gap >= 0.20); 4H origin-candle S/D by zigzag (0.5 and 0.3); POI tier; ZFP from zone type.
  Inputs: i_anchorHour, i_weeks (2), i_back (look back N weeks), i_showE1, i_showSD, i_showAudit.
- GOLDEN WEEK DXY (frame evidence/bt_017): PASS as a dev oracle - ceiling 101.17-101.29 = week high, floor 100.53-100.63 = week low, EQ 100.92-101.02 pivot, in-fill 100.76-100.81 = Thu low.
- HELD-OUT Apr 20 week DXY 4H (frame evidence/ide_035): 12 zones over 97.4-99.35 = TOO DENSE (report oracle has 5 IP zones + 6 LSZ). My thin zones coincide with the report's LSZ and zone edges
  (98.53-98.58 exact, 97.63-97.72, 97.83-97.93, 97.94-98.03, 98.72-98.77 + 98.91-98.96 = edges of the report's 98.77-98.99) -> I am emitting LSZ-grade structure as IP zones.
- KEY INSIGHT (computed by hand, not yet in code): the golden-week EUR/USD option walls convert to the DXY levels the operator drew:
  K = DXY_spot * EURUSD_spot^0.576 = 101.025 * 1.1423^0.576 ~ 109.07; strike 1.1500 (EUR2.4bn) -> DXY 100.63 = the FLOOR and the week's low; 1.1400 (EUR2.2bn) -> 101.14 = his Monday short level;
  1.1450 (1.4bn) -> 100.89; 1.1300 -> 101.66. So option walls are what separate true IP zones from liquidity rungs. The web sidecar is REQUIRED for accuracy, not optional.

## PROGRESS since the block above (12:55)
- Option-wall dataset input is IN the Pine (`i_optData`, `i_anaData`; rows `YYYYMMDD|price:code,...;`, codes 1 live >=1.5bn, 2 live 850m+, 3 ghost >=1.5bn, 4 ghost 850m+). Walls (codes 1-3) seed zones first;
  structure: HEAVY peaks need only non-overlap, MODERATE-HEAVY peaks need 0.15 clearance; one-pass gap in-fill; ZFP by zone type (Hard 5-15, Standard 15-30, Ghost 20-40, Soft 30-50, One-Touch 50-70).
- Sidecar BUILT by an agent and still filling weeks in the background: `sidecar/run --week YYYY-MM-DD`, `sidecar/build-inputs` -> `sidecar/out/pine_inputs.{DXY,EURUSD,GBPUSD}.txt` (+ analyst). Done so far: 2026-04-20, 05-25, 06-29, 07-06, 11-02.
  Jul 6 output matches the hand-verified control. (Agent id a544407069ad54702 - it reports when finished; check `ls sidecar/out`.)
- FRAMES: golden week DXY with walls = PASS (evidence/bt_040, ide_043); golden week EURUSD = PASS (ide_042); held-out Apr 20 DXY 4H = PASS ~5.5/6 (ide_041); held-out Jul 13 DXY 1H = PASS 5/5 (ide_050).
- Sidecar has 15 weeks compiled (`sidecar/build-inputs` -> DXY/EURUSD strings; GBPUSD nearly empty: few GBP strikes >= 850m). E2 plan written: memory/09_E2_E3_PLAN.md. E2 NOT started.
- Backtest tab fixed (LS-15): V1 removed from this instance's room script store; engine no longer starves.

## NEXT STEP (in order)
1. When the sidecar finishes: `sidecar/build-inputs`; validate E1 on >= 8 more held-out weeks across DXY / EURUSD / GBPUSD with each pair's own dataset
   (IDE 4H: `DS="$(cat sidecar/out/pine_inputs.DXY.txt)"; tools/pb ide indicator/plutus-vision-engines.pine DXY 4H i_back=N "i_optData=\"$DS\""`; week N weeks before 2026-11-02).
   Score each by reaction (L-07); log every frame in 07_EVIDENCE_LEDGER. Do NOT tune on held-out weeks; mechanism fixes only.
2. EURUSD golden week vs the operator's screenshots (his demand 1.1400-1.1417, supply 1.1446-1.1456; walls 1.1400 2.2bn, 1.1450 1.4bn, 1.1500 2.4bn).
3. Presentation: labels overlap at the left edge of each week; put the label inside the box / right-aligned; LSZ toggle.
4. Build the single-file delivery `indicator/plutus-vision.pine` = sealed V1 bytes + engine layer (script `tools/build-indicator.sh`, sha-check the V1 region).
5. E2 (context_management/spec/E2_ALGO.md): shape chain from E1 zones + ZFP; then E3 (E3_ALGO.md), <= 11 setups/week.

## How to render (measured recipes)
- IDE tab, full history: `tools/pb ide FILE PAIR TF [i_back=N ...]` then `tools/pb goto FROM TO` then `tools/pb shot NAME chart`. (IDE default runs only 400 bars - LS-12.)
- Backtest tab: `tools/pb export FILE`, `tools/pb bt-apply "Plutus Vision Engines"`, `tools/pb wait-engine`, `tools/pb goto FROM TO bt`, `tools/pb shot NAME full` / `shotc NAME`.
  Works at cursor Jul 10 (8861 bars); at Nov 6 (10858 bars) the added script never prepared (cause not found) - use the IDE for late dates.
- Preflight only: `tools/pine-probe.py FILE --tf 4H --limit 3000 --inputs '{"i_back":28,"i_showAudit":true}' --dump /tmp/x.json`.
