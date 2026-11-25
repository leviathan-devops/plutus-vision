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

## STATE (NEWEST) - TASK = TRANSLATE THE PROMPT'S E1 INTO PYTHON (04 L-30..L-34). Read memory/10_FAILURE_RECORD.md first.
- Done: read E1 first-hand in P533 (lines 802-1163, 1163-1340, 1341-1514) and P452 (637-1205). Pseudocode with line refs: `e1_tool/E1_PSEUDOCODE.md` (committed).
- Reference to reproduce: Leviathan_DXY_IL_Report_Apr20-24_2026.pdf (upload 5212e9bd; pages 1-6 read: option tables, K factor, pivots, 5 IP zones, 4 4H zones with origin candle OHLC, 6 LSZ, clustering scan)
  and Original_Canon_Data/Pine Scripts/trident_v8.pine (output form). Frames of the original: evidence/trident_v8_original_*_allzones.png.
- NOT started: the Python tool (e1_tool/). Waiting on the operator's answers to 3 points where the report's practice differs from the prompt's text
  (4H move threshold: report kept zones with 0.35/2d, 0.26 intraday, 0.12 continuation vs prompt >= 0.5 / >= 3 days; how the point inside a ZFP range and a zone's edges are chosen: the prompt gives ranges / "cluster within 0.10-0.15", the LLM picked).
- Pinebox dies on every session restart: `pinebox down; pinebox up --session plutus-main --adapter xvfb` before rendering. Price-axis fit snippet is in the journal (setManualScale on resolveScaleHolder).
- E1 v3 code still sits in indicator/plutus-vision-engines.pine (rejected). E2/E3 off. Do not build anything else.

## STATE (NEWEST, after the operator's rejection of E1 v3) - STOP: NO CODE, NO AGENTS until he approves (04 L-27, L-28)
- The workflow wf_13ddfb31-159 (e1-zone-mechanics-redesign) was killed by the operator. Do not resume it unless he asks.
- I gave him the gap analysis: prompt vs GLM W14 report vs my engine (06 LS-25 lists my inventions and the prompt's actual rules with line numbers).
- The Pine file still holds E1 v3 (f_pick: merge touching zones, nearest per side + wall rule, measured ZFP). He rejected it. Leave it until he says what to build.
- When he approves: implement the prompt LITERALLY - Step 0f single-origin-candle S/D zones as real candle [Low, High]; BoM/MoM + reaction counter on every zone; 0.10-0.15 clustering;
  degree = highest-scoring level (6 dimensions + structural-extreme bonus) + POI tier; MODERATE and above only; no trimming / padding / merging / caps of my own.
- Known concrete defects to fix first: (a) Oct 5 DXY demand zone 101.71-101.77 existed in the engine but was cut by my 2-per-side cap; (b) Oct 5 top zone was a LIGHT gap in-fill (score 5) drawn although the prompt
  shows MODERATE+ only, and it got no structural-extreme / round-number / 4H-BoM credit; (c) Jul 27 three supports with 1-2 pip gaps should have been ONE cluster by the 0.10-0.15 rule.

## STATE 16:40 UTC (NEWEST) - E1 v3 is in the Pine file and shown to the operator; waiting for his verdict. E2/E3 OFF.
- RULE NOW IN indicator/plutus-vision-engines.pine (f_pick after f_zones): touching zones merge into one (union of evidence); DRAWN = the zone price sits in + nearest zone each side
  + the next one out on a side only if an option wall sits in it. Switch `i_wallOnly` = only zones holding a tier-1 wall (>= $1.5bn live or ghost).
  Zone extents are the evidence's own (median 10 pips on DXY, like his hand-drawn bands). ZFP = measured share of first tests of that zone class sliced through on the chart before the anchor
  (zTouch/zBreak; bookkeeping after each anchor uses the L-23 definition with m = mean bar range). The fixed-width band code (f_bands) is GONE.
- SCORER THAT MATCHES HIS EYE: tools/research/score2.py (REJECT / CONSOLIDATE / SLICED; week verdict VALID when reactions >= slices). Calibration: his golden bands 3/3 valid; W14 bands 0.90; rejected v1 map 0.37-0.54.
- NUMBERS (4H dump zones, 3 pairs): ALL 40 weeks: touched zones valid 0.957 (308 of 322), lenient 0.951, strict (untouched count against) 0.784, FIRST-TOUCH reaction 0.814, 3.3 zones/week.
  TEST 8 weeks: 69 of 69 touched valid, first-touch 0.75. Tier-1-only: first-touch 0.874 all weeks (0.92 DEV, 1.00 VALID, 0.76 TEST), 1.8 zones/week, GBPUSD almost empty.
  KEY FINDING: a zone holding a tier-1 wall reacts on first touch 95% (n=58, DEV+VALID nearest/second zones); tier-2 81%; no wall 75%. Institutional data is what lifts first-touch.
- FRAMES OPENED AND LOGGED: 07 rows 31-39 (golden 4/4; DXY Aug 31 3/3, Oct 5 3/3, Jun 15 2/3, Jul 27 partial; EURUSD Aug 31 3/3, Jul 27 3/4; GBPUSD Oct 5 pivots). By my eye ~24 of 28 touched zones valid.
- WEAK POINTS TOLD TO THE OPERATOR: breakout/news candles slice zones (Jun 15, Jul 27); after a breakout price trades where nothing is drawn; strict first-touch is 81%, not 90%; GBPUSD has almost no >= $850m strikes;
  only investinglive feeds the walls (forex.com / ING / FXStreet hosts are blocked) - more institutional sources is the lever for first-touch.
- NEXT (after his verdict): if approved -> single-file delivery with sealed V1, then E2. If not -> his specifics. Ultracode feature hunt (02 queue) still available with score2 as the metric.

## STATE 14:15 UTC (container clock; newest) - metric and width rules now come from the operator (04 L-22..L-26)
- Failure = price SLICES THROUGH a zone with no reaction. Sharp rejection OR consolidation in/around the zone = valid. Pivot zones valid. Width = extent of the zone's own evidence, never a constant. Draw only what qualifies.
- So: E1 v2's fixed-width bands (0.3 x weekly range) are rejected; go back to evidence-derived extents (v1 had them) but with far better selection, and score with REJECT / CONSOLIDATE / SLICED.
- TODO now: (1) tools/research/score2 with the L-23 definition, sanity-check on his golden-week bands (101.19-101.29 reject, 100.94-100.985 pivot, 100.545-100.675 reject) and on the W14 bands;
  (2) measure slice-through rate per evidence type with evidence-derived extents; (3) redesign selection; (4) Pine; (5) frames I have actually opened, on 4 unseen weeks, to the operator.
- The blank frame: re-render the golden week and LOOK before sending anything.

## STATE 16:15 UTC - metric fixed by the operator: FIRST-TOUCH REACTION >= 90% (L-19). Width is the open trade-off.
- His hand-drawn bands are ~10-13 pips wide on DXY. Current E1 v2 bands are 0.3 x weekly range (~36 pips): on the golden week mine are 101.25-101.61 / 100.49-100.85 / 99.90-100.26
  vs his 101.19-101.29 / 100.545-100.675 - right places, three times too wide (frame evidence/ide_110_e1v2_dxy_1h_golden.png).
- MEASURED (DEV, reaction = 0.1 x weekly range): thin bands on the week's option walls: total width 0.08 / 0.12 / 0.16 x weekly range -> first-touch 69 / 72 / 78%;
  tier-1 live walls 70 / 74 / 78%; walls confirmed by 2+ price-action structures 74 / 73 / 80%. 90% needs ~0.3 width (or a smaller reaction threshold).
- Asked the operator: (1) width vs hit-rate, (2) what size of bounce counts as a reaction, (3) whether a pivot band (like his middle one) may be drawn. His answers decide the tuning.
- Golden-week walls for reference: 100.64 tier-1 (inside his bottom band), 101.28 ghost tier-1 (inside his top band), 101.14 tier-1, 100.89 tier-2, 101.40 tier-1.

## STATE 15:45 UTC - E1 v2 IS IN THE PINE FILE; IT DOES NOT REACH 90%; operator has been told the measured limits
- indicator/plutus-vision-engines.pine now draws the E1 v2 band map (f_bands / f_band / f_wscore; freeze block calls f_bands; old f_zones is unused code kept for comparison).
  <= 2 bands above + 2 below the anchor price, width 0.3 x mean weekly range, taken at the nearest window (>= 0.15 away) whose extreme-type evidence >= 5
  (fresh 4H origin zone 3/2, tier-1 wall 3, tier-2/ghost wall 2/1, prior-week high/low 2, repeated swing extremes 1-2, daily highs/lows 0.5).
  Label: "R1 Supply | BoM|MoM | n rx | ZFP% | score/14". ZFP = measured: share of first tests of that band role traded through on the chart before the anchor (bTouch/bBreak, Laplace).
  Bookkeeping of band tests runs bar by bar after each anchor and feeds only later weeks. Guard allow-list got 0.3/0.15/0.12/0.02/0.1 (band geometry fractions).
- Scorer numbers for this rule (python prototype tools/research/proto2.py, k.30 thr 5): DEV first-touch hold 0.91, clean-all-week 0.63, week extremes inside a band 0.49, 2.9 bands/week;
  VALID first-touch 0.78, clean 0.44, extremes 0.29. Frames on 4 unseen DXY weeks (07 rows 27-30): 1 PASS, 1 PARTIAL, 2 FAIL.
- Bands fixed DAILY at London open and judged over one day are no better (first-touch 68-81%, clean 47-70%): the limit is scale-free, re-anchoring daily does not fix it.
- OPEN DECISION put to the operator (he must answer): his bar "zones not penetrated, 90-95%" was set by the W14 report, which was written with its week's data. Forward, measured ceiling is ~60-70% clean.
  Untested ideas that might add a few points (not 30): trend/regime conditioning of which side gets bands; multi-month weekly/monthly swing extremes as anchors; a multi-agent feature hunt (ultracode) after the usage reset.
- E2/E3 stay OFF (L-14).

## MEASURED LIMITS (15:25 UTC) - read before designing anything else (24 DEV weeks x 3 pairs, tools/research/score.py)
- A band HOLDS ON FIRST TOUCH ~80-91% of the time wherever it is put within reach (structure-free bands at 0.2-0.5 x weekly range from spot, width 0.2-0.3 x weekly range).
  Best level types (band +-0.125 x weekly range): fresh 4H supply (visited <= 1x) 93%, prior week high 91%, yesterday high 91%, D-2/D-3 lows 91%, MA100 90%, tier-1 option wall 88%, prior week low 87%.
  Worst: MA9 72%, yesterday low 76%, RN 77%, MA20/MA50 78%, role-reversal clusters 79%.
- A band stays UNTRADED-THROUGH ALL WEEK only ~57% of the time (base rate); the best level type reaches 70% (MA50 70, fresh 4H supply 69, tier-1 wall 68). Nothing reaches 90%.
  => "no zone gets penetrated during the week, 90%" is not reachable forward with these features; "reacts on first touch >= 90%" is.
- Touch rate falls with distance: band centre at 0.2 / 0.3 / 0.4 / 0.5 / 0.6 / 0.75 / 0.9 x weekly range from spot is touched 88-96 / 72-81 / 58-62 / 43-53 / 37-40 / 26-31 / 16-20 % of weeks. Bands beyond ~0.5 mostly float.
- My old confluence-density selection was WORSE than structure-free geometry (hold 0.72-0.80 vs 0.85-0.88): dense confluence = congestion = traded through. Do not select by density.
- Reference numbers: structure-free 4-band map (spot +-0.35/+-0.8, width 0.3) scores accuracy 0.52, hold-on-touch 0.875, week extremes inside a band 56%.
  W14 hindsight bands 0.75. Current engine 0.35. Prototypes live in tools/research/proto.py (usage: python3 proto.py DEV|VALID).
- Design direction for E1 v2: <= 4 wide bands; inner pair at ~0.2-0.45 x weekly range (labelled MoM / pivot, ZFP ~ measured), outer pair only where a strong anchor exists
  (fresh 4H BoM supply/demand, tier-1 wall, prior week high/low); ZFP = measured failure frequency of that band role over the prior weeks on the chart itself (self-calibrating, no constants).

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
