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

## NEXT STEP (in order)
1. Web sidecar (T5): for each week, as of the Monday anchor: investinglive expiry posts (Mon post if published before the anchor, else Friday's forward row) -> strikes + notionals per pair (vision read, cross-checked),
   Fed H.10 spots -> K; write `sidecar/out/<week>.json` and ONE dated dataset string per chart symbol for a Pine input (`i_optData`): rows `YYYYMMDD|price:tier,...;` in the chart's own price units
   (EURUSD/GBPUSD: their own strikes >= $850M; DXY: EUR/USD strikes via K, tiers by notional >= 1.5bn = 1, 850m-1.499bn = 2). The Pine picks the row of the week being frozen. No values in the source.
2. In the Pine: parse `i_optData` (and `i_anaData`), add src 5 / 6 levels (weight 3 / 2; Options dimension 2; Hard/Standard Wall ZFP), and make IP ZONE vs LSZ a two-tier output:
   IP zone needs an option wall OR >= HEAVY structure OR the outermost ceiling/floor; other structural clusters become unlabeled thin LSZ rungs (toggle).
3. Re-run golden week (Backtest tab, session gw2-dxy-jul06) and Apr 20 (IDE 4H `tools/pb ide indicator/plutus-vision-engines.pine DXY 4H i_back=28`), then EURUSD golden week, then 6+ held-out weeks.
4. Then E2, E3.

## How to render (measured recipes)
- IDE tab, full history: `tools/pb ide FILE PAIR TF [i_back=N ...]` then `tools/pb goto FROM TO` then `tools/pb shot NAME chart`. (IDE default runs only 400 bars - LS-12.)
- Backtest tab: `tools/pb export FILE`, `tools/pb bt-apply "Plutus Vision Engines"`, `tools/pb wait-engine`, `tools/pb goto FROM TO bt`, `tools/pb shot NAME full` / `shotc NAME`.
  Works at cursor Jul 10 (8861 bars); at Nov 6 (10858 bars) the added script never prepared (cause not found) - use the IDE for late dates.
- Preflight only: `tools/pine-probe.py FILE --tf 4H --limit 3000 --inputs '{"i_back":28,"i_showAudit":true}' --dump /tmp/x.json`.
