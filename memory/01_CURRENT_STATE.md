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

## RESUME HERE (written 15:00 UTC, just before a usage-limit reset) - exact state and next actions
WHAT IS TRUE
- Operator rejected E1 (04 L-14..L-18). E2/E3 are OFF by default and FORBIDDEN until E1 is approved. Target = W14 report format: <= 4 wide bands per pair.
- A research scorer now exists and AGREES WITH THE OPERATOR'S EYE: `tools/research/score.py` (run `python3 tools/research/score.py`).
  It walks the week's 1H bars and gives each band HELD / BROKEN / CONTAINS / BOUNDING / FLOATING; D = 0.10 x mean weekly range (13 wk).
  accuracy = good / (good + broken + floating + missed week extremes).
  MEASURED 15:00: current engine maps on the 24 DEV weeks x 3 pairs = 35.1% (HELD 273, BOUNDING 110, BROKEN 157, FLOATING 493, missed extremes 59 of 144; 0 weeks >= 90%).
  The W14 report's own bands (written with hindsight, LS-20) score 75% (DXY 4/4, EURUSD 2/4, GBPUSD 3/4).
- Level dumps for research: `tools/research/levels.{DXY,EURUSD,GBPUSD}.json` (git-ignored; regenerate with `python3 tools/research/dump_levels.py`, needs Pinebox up).
- Week split (never show TEST to a design loop; TEST is for my own Pinebox frames): TEST 2026-02-23, 03-23, 04-27, 05-18, 06-15, 07-27, 08-31, 10-05 ·
  VALID 02-16, 03-09, 04-13, 05-11, 06-22, 08-03, 09-14, 10-26 · DEV = the other 24 weeks (list in score.py).
- Frames of the W14 report bands: evidence/oracle_w14_report_zones_{DXY,EURUSD,GBPUSD}_1h.png (outer bands contain week high/low; middle bands crossed).
- Scratch helper for memory writes (hook-friendly): overwrite and run scratchpad/mem_update_1435.py (LS-22).
NEXT ACTIONS (in order)
1. Prototype the E1 v2 band rule in Python against score.py on DEV weeks only (cheap loop): <= 4 bands per week, 2 above spot + 2 below (or one containing spot),
   bands WIDE (DXY ~0.15-0.30, pairs scaled by weekly range), built from: prior-week high/low/close zones, 4H/D1 supply-demand origin bases (BoM/MoM),
   repeated D1 swing extremes, round numbers, option walls (live + ghost). Pick the band nearest price on each side that is strong, then the next one out;
   no band further than the week can reach. Compare against two reference maps: W14-style hindsight ceiling and a naive baseline (prior week high/low bands).
2. Confirm on VALID weeks (no retuning there). If >= 85-90% on the scorer: port into `f_zones` in indicator/plutus-vision-engines.pine (labels: Supply/Demand, BoM/MoM, reactions, ZFP, x/14),
   anchor guard must pass, render 4 TEST weeks x pairs with `tools/pb week`, LOOK, log frames in 07, show the operator.
3. If a multi-agent design search is wanted (ultracode was on): 4 designers with different lenses on DEV + one validator each on VALID, all importing tools/research/score.py.
   NOT launched before the usage reset on purpose (a reset kills running agents, see 06).
4. ZFP must be mechanical (L-16): BoM vs MoM, reaction count over prior 3 weeks, option wall tier, confluence -> canon base range + modifiers; show its parts in the audit.

## STATE 14:35 UTC - READ THIS BLOCK FIRST (operator intervention; see 04 L-14..L-18, 06 LS-19..LS-22)
- E1 is REJECTED by the operator (30-50% by his eye). E2/E3 are FORBIDDEN until E1 is approved; both are OFF by default in the file.
- Target = W14 report format: <= 4 wide bands per pair (2 supply above, 2 demand below; one may contain spot), each with Type, BoM/MoM, Reactions, mechanical ZFP, Confl x/14, key level. No thin stacked zones, no far floating zones. Acceptance: >= 90% on 4 separate weeks, judged by eye in Pinebox.
- The W14 report itself was written with its week's data (LS-20): its format is the target, its numbers are not a forward score. Operator has been told.
- In progress: design search for E1 v2 band selection (research files in scratchpad research/, scorer research/score.py). Then port the winning rule into f_zones (Pine), render TEST weeks, look, iterate.
- Tools: tools/pb week PAIR TF MONDAY NAME [K=V] (IDE render of one week with the pair's dataset); oracle render probe indicator/probes/report_w14_oracle.pine.

## UPDATE 14:05 UTC (supersedes the lines above where they differ)
- E1 held-out strict reaction scores: DXY Feb 9 50, Mar 16 65, Apr 20 92, May 25 75, Jul 13 100, Aug 10 90, Sep 7 70, Sep 28 62, Oct 19 70 (mean ~75); EURUSD Apr 20 75, Sep 7 93. Golden week DXY + EURUSD PASS.
- E1 scope is now the reach band (spot +- mean weekly range of 13 weeks, union prior week range) + outer gap in-fill. Reaction counter = audit only (does not discriminate). `tools/pb week PAIR TF MONDAY NAME [K=V]` renders one week with the pair's dataset.
- E2 v0 is in the file (f_e2) but FAILED its first frame (Apr 20). E3 not started. Sidecar complete (28 weeks).

## NEXT STEP (in order)
1. GBPUSD: 2 held-out weeks (structure only; dataset nearly empty). Then commit.
2. E3 from the corrected doc (read context_management/spec/E3_ALGO.md phases + constants): zone-edge setups as position boxes, <= 11 per week; verify fills on golden week + 3 held-out weeks.
3. E2: rework the walk per E2_ALGO 3.3 (ZFP-conditioned), verify 4 weeks, report measured day accuracy honestly.
4. Single-file delivery `indicator/plutus-vision.pine` (sealed V1 bytes + engines) via tools/build-indicator.sh with sha check of the V1 region.
5. Final report: scorecard table, what passes, what does not.

## OLD NEXT STEP (done or superseded)

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
