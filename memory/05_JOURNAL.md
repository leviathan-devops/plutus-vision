# 05 — JOURNAL (append-only stream: what I did, what I think, why; newest at the bottom)

## 2026-11-25
- 10:40 New brief on Fable 5.2: build E1 (then E2/E3) in Pine on top of V1, dynamic, Monday anchor, Pinebox-only verification. Container is fresh (old scratchpad gone; repo at d071f6c intact).
- 10:42 Unzipped 4 packages to /home/user/inputs. Pinebox = big bash CLI over "computer-use v2" + forked Pine IDE + backtest room + TradingView bar store (2025-02 -> 2026-11-06).
- 10:47 Installed Pinebox by hand (deploy.sh is git-gated): rsync 3 trees, bar store from pinebox-cloud/dist-web/data/bars, npm ci in pine-station, Chromium build 1734920 via @puppeteer/browsers.
  Blockers hit and fixed: `ss` missing (iproute2), `xdpyinfo` missing (x11-utils), Chromium refuses root (wrapper with --no-sandbox). `pinebox up --adapter xvfb` -> READY. Frame read.
- 10:50 Read operator rulings R-01..R-39 first-hand. Found the real oracles: golden-week screenshots (read 4 of 8 myself) and weekly reports on branch origin/handover.
- 10:55 Thought: the previous agents built Python pipelines and scored them with scripts; the operator's test is the chart. My loop must be: write Pine -> load in Pinebox -> shot -> read candles vs zones.
- 11:00 Launched 8 readers (workflow plutus-understand). Asked the operator 3+3 questions in his 5-minute window; answers in 04. Key correction: historical web data IS online (investinglive archives all 2026 expiries); I must build a fetching sidecar, not price-only E1.
- 11:10 Network hosts approved; OpenCode Go key saved (proxy-injected). investinglive/fed/opencode all answer 200.
- 11:20 Memory folder created. Reasoning on the "no hardcode" vs "web data" tension: the indicator source must hold no values; weekly external data enters as inputs written by the sidecar for the week being viewed.
  Unknown yet: how Pinebox passes inputs. To test.
- 11:30 Pinebox verbs exercised first-hand. IDE: `load` v1 on DXY 1H -> 20 boxes / 28 labels / 42 lines, all near the LAST bar (Nov 2026); navigating the IDE chart back to Jul 6-10 shows candles only (frame evidence/v1_baseline_DXY_1H_golden_week.png) -> an indicator that only draws "current state" is invisible on past weeks in the IDE tab.
  Backtest tab: `backtest --op create --name gw-dxy-jul06 --symbol DXY --start 2026-07-06T06:00 --end 2026-07-11 --tf 1H` puts the replay cursor at Mon Jul 6 06:00Z (bar 8751/10879) with all earlier bars visible = the Monday anchor simulated natively.
  EXPORT TO BACKTEST (IDE button at x=247,y=771) -> script appears in the room "ON CHART" (Indicators dialog), but V1 drew NOTHING on the room chart at the cursor (frame bt_003). Cause unknown yet (await PINEBOX_ENGINE_NOTES).
  Range buttons (1D/7D/1M...) under the charts CHANGE THE TIMEFRAME (1M -> 30m). Do not use them; use `tools/pb goto FROM TO [bt]`.
- 11:40 Read E1_ALGO.md digest in full (652 lines). Big findings: (a) seven E1 pillar blocks in v5.3.3 are "[unchanged from v4.5.2]" placeholders -> the missing text is in
  /home/user/handover-branch/Original_Canon_Data/TTE System Prompts/Trident_Trading_Engine_System_Prompt_v4.5.2 (1).md; (b) all tolerances are written in DXY points (cluster 0.15, tight 0.10, LSZ 0.05, wick 0.15, 4H zone max 0.40, 4H move >=0.5/3 days, D1 OB >=1.0/5 days); pair-unit tolerances are not in canon;
  (c) canon's own data boundary is Friday 17:00 ET; operator's live ruling is Monday London open (operator wins, both forbid in-week data); (d) zone names: RESISTANCE CEILING, UPPER RESISTANCE, EQUILIBRIUM ZONE, MID-RANGE SUPPORT, KEY SUPPORT BAND, LIQUIDITY SWEEP ZONE, BREAKOUT EXTENSION TARGET; score 0-14 -> EXTREME/HEAVY/MODERATE-HEAVY/MODERATE/LIGHT/MINIMAL.
  (e) Without options/analyst data the score ceiling is 10 (HEAVY) -> the web sidecar is what lifts zones to EXTREME; consistent with the operator's order to fetch it.
- 12:05 Read report oracles + handover 2.3. Design reasoning for E1 v0 (mine): candidate = structural price anchor (D1 swing extremes with rejection wick, repeated extremes/role reversals, prior week H/L/C, prior daily closes, 4H origin-candle S/D edges, D1 order blocks).
  Score each candidate on the six canon dimensions by coincidence: Technical 2 if a pivot/MA within 3 pips, 1 if within 10 pips; Psychological 2 on .00/.50, 1 on .25/.75; Structural 2 exact anchor + extreme, 1 proximity; Options/Analyst from the sidecar week file; Regime from the P9 classifier (await v4.5.2 text); + structural-extreme bonus <= 2.
  Zone = the anchor plus the levels that scored it (so width is the confluence, typically 0.05-0.15), kept when degree >= MODERATE (6). No count cap anywhere.
  All higher-TF data aggregated in-script; forecast frozen at the Monday 02:00 NY bar; drawn for `weeks to draw` (default 2 = R-36); IDE on 4H has full history (2832 bars) for walk-forward viewing of every week; Backtest tab for exact replay.
- 12:10 Waiting on: v4.5.2 fill (P5 steps 1-5, P6, P9), handover digest, engine notes, golden-week numeric read, laws digest, sidecar scout, omnigraph. Starting the Pine scaffold now (aggregation, anchor, week frame) — it does not depend on them.
- 11:25 USAGE LIMIT hit ~12:30 (5-hour window, reset 14:00 UTC). Lost mid-run: workflow readers handover-digest, pinebox-engine, laws-digest, oracle-golden (no files written) and the sidecar scout agent (partial work under sidecar/raw/).
  Landed: E1_ALGO, E2_ALGO, E3_ALGO, REPORT_ORACLES(+json), E1_V452_FILL, tools/mem (OmniGraph live). Lesson: 8 parallel high-effort readers burned ~1.9M tokens; run at most 2-3 agents at a time and keep them narrow.
  Engine facts I already measured myself (08_FACTS) so pinebox-engine reader is NOT needed. Still wanted: golden-week numeric read (I have my own approximate read), laws digest (by-eye procedure), handover digest (I read 2.3 + rulings first-hand).
- E1 v0 (strict canon scoring, zone = levels within 3 pips of a seed) on the golden week gave 2 zones (101.00-101.05, 99.50-99.55) and MISSED the operator's ceiling (101.19-101.29) and floor (100.55-100.675).
  Audit dump shows why: 158 levels in ~300 pips, a level every 1-2 pips; Technical = 2 for every level (88 pivots blanket the range); Structural = 2 for all 18 Step-1 price anchors. Scores are flat 3-5: the six dimensions cannot discriminate in a dense field.
  This is the same mechanism that sank the previous tool ("HIGH-DENSITY 450 of 459"). Literal canon + the constant offsets (POI +1, Regime +1) would flood, not select.
  DESIGN v1 (mine, D-10): zones are the LOCAL MAXIMA of weighted multi-pillar confluence, with the canon's 0.15 cluster band as the suppression radius. Confluence weight per evidence: structural reaction cluster = st + bonus (repeated extremes / role reversals from D1 AND 4H swings, distinct days), price anchors 1 (week H/L/C 2), weekly pivot 1, daily pivot 0.5, MA by the canon's MA weights (200:3 100:2 50:1.5 20:1 9/10:0.5), fib 1, round .00 2 / .50 1.5 / .25 .75 1, option tier 3/2, analyst tier 3/2/1, inside a 4H BoM S/D zone +2.
  Kernel: full weight within 3 pips, half within 10 pips. The canon 6D score/degree is still computed for the label and the MODERATE gate. Count emerges from range/spacing; no cap.
  Also adding canon 4H S/D (Step 0f) via a 0.5 zigzag on 4H bars (origin candle [low, high], reject > 0.40 wide, mitigation count), POI tier, regime dimension from ZFP.
- ENGINE QUIRK (cost 20 min): `x[1]` inside an `if` block returns the CURRENT value in vela-pinets. `nz(close[1], open)` inside the freeze block would have read the anchor bar's own close = a lookahead. All history reads now live at global scope (tClose1, close1, ...). The run-time assert f_assertAnchor caught it.

## 2026-11-25 ~14:05 UTC — E1 held-out scorecard grows; scope mechanism changed; reaction counter tested
- E2 v0 first frame (Apr 20) = FAIL. Parked E2 to finish E1 validation first.
- Rendered 6 more held-out DXY weeks + 2 EUR/USD weeks (tools/pb week PAIR TF MONDAY NAME). Strict reaction score: Feb 9 50, Mar 16 65, May 25 75, Aug 10 90, Sep 7 70, Sep 28 62 (DXY); EURUSD Apr 20 75, Sep 7 93. With earlier Apr 20 92, Jul 13 100, Oct 19 70: DXY held-out mean ~75%.
- Pattern: range weeks ~90%+; weeks with an impulse day run through stacked mid zones (not knowable at the anchor); two weeks travelled beyond the old scope.
- Mechanism changes (not tuned per week): (1) weekly map = zones inside the reach band [min(prior week low, spot - AWR), max(prior week high, spot + AWR)], AWR = mean weekly range of the last 13 weeks; outer gaps >= 0.20 filled repeatedly, interior gaps one pass; "first zone beyond" dropped. (2) Zone Reaction Counter (holds / crossings over prior 90 4H bars) computed per zone, audit only: checked against 10 scored weeks, 3+ reactions does NOT separate holding zones from pivots, so it gates nothing. (3) analyst code 9 (investinglive, not a canon tier-1 source) now weighted as one source, not two.
- Sidecar finished: 28 weeks (2026-02-02 .. 2026-11-02), `sidecar/build-inputs` rebuilt. GBPUSD has 5 rows only.

## 2026-11-25 ~14:35 UTC - operator rejects E1; W14 baseline handed over; redesign of E1 selection starts
- E3 v1 (zone-rejection setups, bar-by-bar outcome tracking, position boxes) was built and rendered (ide_090: golden week short 101.14 TP +3.5R, long 100.89 SL, long 100.64 Fri close). Preflight over 30 DXY weeks: 52 filled, 13 TP, 36 SL, +27.9R. Operator: decent but RRR must be 4x+, and STOP: E1 first. E2/E3 default OFF now.
- Rendered the W14 report zones as-is (indicator/probes/report_w14_oracle.pine; frames evidence/oracle_w14_report_zones_{DXY,EURUSD,GBPUSD}_1h.png). Outer bands contain week high/low on all three pairs; middle bands are crossed several times. The report was written with the week's own data (LS-20).
- Research inputs in the scratchpad research/ (regenerable: tools/pine-probe.py with i_showAudit=true, i_weeks=60 on 4H per pair): levels.{DXY,EURUSD,GBPUSD}.json = per week every candidate level with its fields + S/D zones + current zones. The audit label prints all levels ("L p|src|tag|w|st|bonus|lo|hi|conf|tech|stru|psy|opt|ana|xb|code|optc").
- E1 changes made today before the rejection: reach band (largest weekly range of 13 weeks either side of spot) + outer gap fill; reaction counter + reaction extremes (audit); analyst code 9 = one source.
- NEXT: E1 v2 = W14 format (<= 4 wide bands per pair, Supply/Demand, BoM/MoM, reactions, mechanical ZFP), forward-only. Design search on DEV weeks with a shared first-passage scorer, validation on VALID weeks, my own visual check in Pinebox on TEST weeks never shown to the design agents.
  TEST (mine): 2026-02-23, 03-23, 04-27, 05-18, 06-15, 07-27, 08-31, 10-05. VALID: 02-16, 03-09, 04-13, 05-11, 06-22, 08-03, 09-14, 10-26. DEV: the other 24.

## 2026-11-25 ~15:00 UTC - scorer built; baseline measured; persisting before a usage-limit reset
- tools/research/score.py + dump_levels.py committed. Current engine = 35.1% on DEV by the scorer (operator said 30-50% by eye: the scorer matches his eye). W14 hindsight bands = 75%.
- Biggest losses of the current engine: FLOATING bands (493 of 1038: the reach band made this worse), week extremes not inside any band (59 of 144), BROKEN thin mid zones (157).
- Operator asked to store all context before the 5-hour limit and to continue afterwards without stopping. Design workflow deliberately not launched before the reset.

## 2026-11-25 ~15:25 UTC - what is and is not predictable (measured)
- First-touch hold of a wide band is ~85-90% almost regardless of placement; clean-all-week is ~57% base, 70% best type. See 01 "MEASURED LIMITS". Told the operator.
- Old confluence-density selection picks congestion (worse than no information). E1 v2 must not select by density.

## 2026-11-25 ~15:45 UTC - E1 v2 ported and looked at; honest result
- Ported the 4-band map into Pine, rendered 4 unseen DXY weeks: Apr 27 looks like the W14 report (both bands contain the turns); Jul 27 partial; Jun 15 and Oct 5 fail (breakout / pivot weeks).
- Daily re-anchoring measured: no better. Heavier confluence thresholds: first-touch up to 0.92 on DEV, clean stays ~0.60, VALID worse. This is a property of the market at these scales, not of one rule.
- Reported to the operator with the numbers and the W14 hindsight evidence; asked how he wants accuracy defined given that.

## 2026-11-25 ~16:40 UTC - E1 v3 built on the operator's own definition; first frames that resemble his drawing
- After his answers (L-22..L-26) I rebuilt the scorer (score2) and found the old map's real defect: relevance, not validity. Evidence-derived zones near price are valid ~95% of the weeks price reaches them.
- Tier-1 option walls are the one feature that separates zones on first touch (95% vs 75% without a wall).
- Pinebox had died with the worker restart (pinebox list alive:false) -> pinebox down/up. A stale dump file fooled me for one step: always check the probe printed "/model/boxes" before reading its dump.
- Sent him: golden week, 4 unseen DXY weeks, 2 EUR/USD, 1 GBP/USD - every frame opened first.

## 2026-11-25 ~21:45 UTC - E1 TOOL build started (e1_tool/), operator asleep, autonomous
- Written: e1_tool/e1_data.py (TV bar loader, Friday 17:00 NY boundary, daily/weekly aggregation), e1_tool/e1_pillars.py (pivots + checks = Pillar 1; step0f = 4H supply/demand).
- step0f reading (assumption A1, to report to the operator): a "strong move" = a move that leaves an inefficiency gap between the candle before it and the candle after it (his notes' valid-order-block rule);
  zone = the candle before it, wick low to wick high; consecutive gaps = one impulse; BoM = first zone after a direction change, MoM = same direction as the previous zone; mitigation = later separate returns (hard if a body enters, else soft).
- CHECK vs the Apr 20-24 report (DXY, TV candles): BoM Supply 98.884-99.038 @04-13 09:00 (report 98.77-98.99 @04-13) · MoM Supply 98.327-98.414 @04-13 23:00 (report 98.34-98.42 @04-13 20:00)
  · BoM Demand 97.832-98.092 @04-16 03:00 (report 97.93-98.11 @04-16 00:00). MATCHES the report's structure. Not reproduced yet: the report's "developing" BoM Demand 97.63-97.94 at the Apr 17 low
  (no gap had formed by Friday's close); mine instead has BoM Supply 98.194-98.291 @04-17 03:00 before Friday's drop. 49 zones in 60 days: the prompt's noise-rejection rules (P452:741-745) still to apply.
- Data-source difference: TV prior week H 99.183 L 97.632 C 98.226; report (yfinance) C 98.10 -> pivots differ by ~0.05 (PP 98.35 vs 98.30). Logic identical (all four verification checks pass).
- Sidecar 2026-04-20 has the Friday Apr 17 page's forward rows only; the report used the Monday Apr 20 page (06:08Z). Raw pages are under sidecar/raw/2026-04-20/ (incl. `_boundary_0608Z`).
- NEXT: Pillar 2 (MA grid), Pillar 5 Step 0/0.45/0.5/0h + anchors, Pillar 6, Pillar 3/8 (K, strike->DXY), Pillar 9 type/range, synthesis (collect, score, cluster, zones per L-39, names, gap scan, 9.7 tiers), report printout, Pine generator, render.

## 2026-11-25 ~22:00 UTC - e1_tool: Step 0 swings, 0.45 LSZ, 0.5 magnets, Pillar 2, Pillar 6, Pillar 3/8 conversion written (e1_tool/e1_pillars.py) and checked vs the Apr 20-24 report
- strike_to_dxy(K=108.0806): 1.1600->99.22, 1.1750->98.49, 1.1785->98.32, 1.1900->97.78, 1.1675->98.86, 1.1760->98.44, 1.1800->98.25, 1.1810->98.20 = EXACT match with the report, all 8.
- K from the sidecar's H.10 rates (Apr 10 rate day) = 108.1552; report K = 108.0806 used USDJPY 158.93 GBPUSD 1.349 USDCAD 1.3897 USDSEK 9.1921 USDCHF 0.7828 (mixed sources). Difference is input rates, not logic.
  For K use the pairs' TradingView closes at the boundary where bars exist (GBPUSD) and H.10 for the rest; print the audit line with sources (P452:919).
- Spot at boundary on TV = 98.226 (report 98.10 from yfinance DX-Y.NYB).
- Daily swings found (TV): low 97.632 04-17 (wick 0.58, close pos 0.90 = major) · low 97.969 04-14 (wick 0.13) · low 98.525 04-08 (wick 0.51, close pos 0.44) · high 99.183 04-13 (minor) · high 98.292 04-16.
  Report LSZ: lows 04-17 97.63, 04-16 97.83, 04-14 97.97, 04-08 98.53; highs 98.29-98.34 (04-15/16/17, 3x), 99.18-99.23 (04-08/13, 2x).
  => the report listed EVERY recent daily low/high as a sweep zone, without enforcing the wick >= 0.15 / close-position test, and 04-16's low is not even a 3-bar swing low (04-17 went lower).
  ASSUMPTION A2 (for the morning report): build LSZ from every D1 swing low/high of Step 0 AND the last 5 days' lows/highs (Step 1 anchors), each tagged major / minor / anchor, so the report's six are reproduced; the wick test only sets the grade.
- Repeated magnets on TV: 97.98 (3 dates incl. 04-14), 98.51 (3 dates incl. 04-08), 98.26 (2, incl. 04-16), 98.87, 99.29 ... (role reversals). Report had repeated high 98.29 (3x) and 99.18 (2x).
- MAs (daily, TV): SMA/EMA 9-10 98.58-98.72, SMA50 98.72, SMA100 98.51, SMA200 98.53, EMA200 99.23, SMA20 99.28, EMA20 98.94 (the bar store starts 2025-02-02, so 200-day values exist from ~Nov 2025).
- NEXT: Pillar 9 type->range, synthesis (collect all levels with their dimension scores; clustering scan; zones = candle structure + cluster joined per L-39; names; gap scan; tiers; 4H noise rejection), report printout, Pine generator, render, compare.

## 2026-11-25 ~22:15 UTC - e1_tool/e1_synth.py first run (collect -> score -> cluster -> zones with candle structures joined)
- `cd e1_tool && python3 e1_synth.py 2026-04-20` prints the zones. 186 levels, 18 clusters of 3+ levels. It WORKS mechanically; three things are still not what the prompt says, fix them in this order:
  1. 4H zone filter NOT applied yet. step0f returns 49 zones over 60 days, many 5-10X mitigated, and assemble() joins ALL overlapping ones -> zones bloat to 40-60 pips (e.g. 98.97-99.56).
     Apply the prompt's noise rejection (P452:741-745: drop > 0.40 wide; MoM with 3X+ hard mitigations; older than 3 weeks with no recent interaction; no IP zone within 0.50 unless BoM 0X-1X)
     and the order-block rule from his notes (one-time use: only UNMITIGATED / 0X-1X zones count; Tier 1 needs BoM 0X-1X, P452:1201). Join into a pressure zone only the surviving S/D zones.
  2. Role naming: the synthesis has FIVE standard names (P452:1148-1153). ASSUMPTION A3: Equilibrium = the MODERATE+ zone at / nearest spot; above spot the two highest-scoring zones (upper one = RESISTANCE CEILING, lower = UPPER RESISTANCE);
     below spot the two highest-scoring (nearer = MID-RANGE SUPPORT, the other = KEY SUPPORT BAND). All other clusters stay in the audit (clustering scan) but are not synthesis zones.
  3. Sweep zones per A2 (every recent daily low/high) - currently only wick-graded swings of the last 10 days are passed in.
- Already right vs the report: cluster 99.18-99.31 holds the 1.1600 €1.9bn wall (99.22) = Hard Wall, HEAVY 11 (report CEILING 99.16-99.23 HEAVY 10); cluster 98.29-98.44 holds MoM Supply 98.33-98.41 (0X) = the report's EQUILIBRIUM 98.29-98.41;
  clusters 97.50-97.83 hold the sweep zone 97.63-97.68 = KEY SUPPORT BAND area; 98.00-98.14 with BoM Demand 97.83-98.09 (1X) = MID-RANGE SUPPORT 98.00-98.12.
- Scoring as coded (score_level): Technical 2 if a pivot/MA/fib within 3 pips, 1 within 10; Options 2 if a tier-1 strike within ±0.07 or tier-2 within ±0.10; Structural 2 if an anchor AND an extreme within 3 pips, 1 if either within 10;
  Psychological 2 for .00/.50 within 3 pips, 1 for quarters; bonus = best extreme bonus within 3 pips (max 2); Regime 2 Hard Wall / 1 / 0 One-Touch; tier +2 (fresh BoM overlap) / +1; cap 14. Zone type -> ZFP range table per P452:964-972.
- THEN: e1_report.py (print the report's sections 1-9 for the week), e1_pine.py (trident_v8 form; per L-39 draw inside each zone the candle part and every level line, LSZ green, strikes amber; labels inside the week),
  render DXY Apr 20-24 in Pinebox (recipe in 11 §6), OPEN the frame, compare with evidence/trident_v8_original_DXY_1h_apr20_allzones.png, then other weeks/pairs. Expiry loader must include the Monday page rows (Day 1) + Day-2 forward rows.

## 2026-11-25 ~22:30 UTC - e1_synth.py with 4H noise rejection + five named roles: result for DXY Apr 20-24 and what is still off
Output now (TV candles):  RESISTANCE CEILING 99.13-99.31 HEAVY 11 Hard Wall 5-15% (report 99.16-99.23 HEAVY 10)  = MATCH
 UPPER RESISTANCE 98.46-98.78 EXTREME 12 (cluster 98.46-98.59 + BoM Demand 98.56-98.78 + sweep 98.53-98.58)   (report 98.77-98.99 = the supply candle)  = DIFFERENT ZONE
 EQUILIBRIUM 98.19-98.44 MOD-HEAVY 8 (cluster 98.29-98.44 + MoM Supply 98.33-98.41 + BoM Supply 98.19-98.29 + sweep 98.24-98.29)  (report 98.29-98.41 MOD-HEAVY 9) = MATCH (wider by the joined 04-17 supply candle)
 MID-RANGE SUPPORT 97.83-98.14 HEAVY 11 (cluster 98.00-98.14 + BoM Demand 97.83-98.09 + sweep 97.97-98.02)  (report 98.00-98.12 MODERATE 7) = MATCH in place, score higher
 KEY SUPPORT BAND 97.83-98.09 (cluster 97.84-97.98 + the SAME BoM Demand)  (report 97.63-97.97 HEAVY 11 with sweep 97.63-97.68) = WRONG: overlaps Mid-Range Support.
4H zones kept after the filter include BoM Supply 98.884-99.038 (04-13 09:00, 0X), MoM Supply 98.327-98.414, BoM Demand 97.832-98.092 (04-16), BoM Supply 98.194-98.291 (04-17), plus older 0X-1X zones above 99.3.
Sweep zones (graded swings only, last 10 days): 98.53-98.58, 99.13-99.18, 97.97-98.02, 98.24-98.29, 97.63-97.68.
STILL TO FIX (re-read the prompt text for each before coding; do not tune):
 F1. A candle structure must belong to ONE zone only and named zones must not overlap: attach each S/D zone / sweep zone to the cluster it overlaps most (or whose levels sit inside it); then no two zones share a structure.
 F2. The report's Upper Resistance is the BoM supply candle zone (cluster 98.80-98.94 here, score 8, joined with BoM Supply 98.884-99.038) - my role pick took the denser cluster 98.46-98.59 instead (score 12).
     Check the scoring of 98.46-98.59 against the prompt: 19 levels there are mostly daily pivots + MAs (Technical only). Pressure degree = the group's HIGHEST-SCORING LEVEL on six dimensions - make sure Technical cannot exceed 2 and that
     Options/Structural/Psychological are not being credited from levels 10 pips away. Also the +2 tier credit came from a 04-10 demand zone (98.56-98.78, 1X) that the report did not have.
     Role order in the report follows position: ceiling (top) > upper resistance > equilibrium > mid-range support > key support (lowest) - consider taking, on each side, the zones in ORDER OF POSITION among those that are MODERATE+ AND hold a candle
     structure or a wall, rather than by raw score. Decide by the prompt's naming text (P452:1148-1153) and note it as assumption A3'.
 F3. Key Support Band should be the zone around the 97.63 sweep target (cluster 97.50-97.83 + sweep 97.63-97.68) - it lost to the duplicate above; F1 fixes this.
 F4. The report's "developing" BoM Demand at the Apr 17 low (97.63-97.94) has no gap yet at the boundary -> not produced by A1. Leave as is; list it in the morning report.

## 2026-11-25 ~22:40 UTC - F1 done (one structure -> one zone); A3' (nearest two per side) tried and REJECTED by me: it bunches the five zones around spot (98.56-98.78 / 98.46-98.59 / 98.14-98.29 / 97.97-98.14 / 97.83-98.09)
- That is the same bunching failure the operator trashed. The report's five zones are SPREAD: 99.16-99.23 / 98.77-98.99 / 98.29-98.41 / 98.00-98.12 / 97.63-97.97 (about 0.3-0.5 apart).
- Why mine bunch: 186 levels over ~3 points -> 18 contiguous 0.15 clusters, nearly all scoring 10-12 (Technical 2 almost everywhere from ~60 pivot levels; Structural 1 from last-5-day anchors within 10 pips). The report: 126 levels, 22 clusters, 13 high-density, scores 7-11.
- NEXT TRY (A3''), grounded in Step 9.5 (the prompt treats adjacent mapped zones as >= 0.20 apart - anything closer is the same area): rank MODERATE+ clusters by score, take them greedily, skipping any cluster whose span lies within 0.20 of one already taken
  (tie -> the one holding a candle structure / wall, then nearer to spot); the zone at/nearest spot is the Equilibrium; name the two taken zones above it by position (ceiling, upper resistance) and the two below (mid-range support, key support band).
  Then re-check the per-level scoring against the prompt's table so one dense pivot area cannot outscore a wall + structure zone: Technical is ONE dimension (max 2) - verify nothing else is inflated (e.g. Structural from mere proximity to daily highs/lows).
- Expected after that for Apr 20-24: ceiling ~99.13-99.31 (wall 99.22), upper resistance = the cluster joined to BoM Supply 98.884-99.038, equilibrium ~98.29-98.44 (+ MoM Supply 98.33-98.41), mid-range support ~98.00-98.14 (+ BoM Demand 97.83-98.09), key support ~97.50-97.83 (+ sweep 97.63-97.68).
- Code state: e1_tool/e1_synth.py has owner() (F1) and the A3' block (replace it with A3''). `python3 e1_synth.py 2026-04-20` prints named zones + the report line.

## 2026-11-25 ~22:50 UTC - A3'' (score-ranked, zones >= 0.20 apart, structure/wall clusters first) coded in e1_tool/e1_synth.py; result for DXY Apr 20-24
 RESISTANCE CEILING 99.13-99.31 HEAVY 11 Hard Wall (= report)  ·  UPPER RESISTANCE 98.46-98.59 (wall 1.1750 -> 98.49 + sweep 98.53-98.58)  ·  EQUILIBRIUM 97.83-98.09 (BoM Demand 04-16)  ·  KEY SUPPORT 97.36-97.49.
 Spread is right now (no bunching), the ceiling matches, but three roles land on other clusters than the report's (98.77-98.99 / 98.29-98.41 / 98.00-98.12 / 97.63-97.97).
WHY (diagnosed, not yet fixed):
 - the 0.20 separation is measured on JOINED extents, so the supply-candle zone (levels 98.80-98.94 + BoM Supply 98.884-99.038 -> top 99.04) is rejected for being 0.09 under the ceiling zone (99.13). Measure separation between LEVEL spans or let touching zones coexist when each holds its own structure.
 - nearly every cluster scores 10-11, so the order is decided by ties. The scoring needs an honest re-read against the prompt table: per-level Technical should need THIS level to be a pivot/MA/fib match, Structural 2 needs an exact anchor + extreme; check that
   daily highs/lows of the last 5 days within 10 pips are not handing Structural 1 to everything, and that the tier +2 only comes from a BoM 0X-1X overlap. The report's scores were 7-11 with clear separation.
 - the Equilibrium should be the zone AT spot (98.226): cluster 98.14-98.29 / 98.29-98.44 (+ MoM Supply 98.33-98.41, BoM Supply 98.19-98.29); it was skipped because a higher-ranked neighbour within 0.20 was taken first.
   Consider fixing the Equilibrium FIRST (the MODERATE+ cluster at / nearest spot), then taking the others outward with the 0.20 separation.
 - The report's implicit rule, visible in its key drivers: every named zone sits on a candle structure or sweep target (supply candle, MoM supply, BoM demand, sweep 97.63) or a wall (99.22). Prefer that reading (it is also L-39).
NEXT STEPS UNCHANGED after this: report printout, Pine generator (trident_v8 form + levels inside zones), Pinebox render of Apr 20-24, open the frame, compare with the original; then other weeks / pairs; morning report with assumptions A1-A3.

## 2026-11-25 ~23:00 UTC - equilibrium-first + separation on level spans: DXY Apr 20-24 now gives five SPREAD zones
 CEILING 99.13-99.31 HEAVY 11 Hard Wall (matches report) · UPPER RESISTANCE 98.56-98.78 (BoM Demand 04-10; report: 98.77-98.99 supply candle) · EQUILIBRIUM 98.14-98.29 (BoM Supply 04-17 + sweep 98.24-98.29; report 98.29-98.41)
 · MID-RANGE SUPPORT 97.68-97.83 (report 98.00-98.12) · KEY SUPPORT 97.15-97.25 (report 97.63-97.97).
 Honest status: structure of the output is right (5 named, spread, each with type / range ZFP / tier / drivers), ONE of five zones matches the report; the other four sit one cluster away from the report's.
 Known causes still open: (1) clusters are cut every 0.15 from the top level down, so cluster boundaries are arbitrary - the prompt says count, for EACH level, the others within 0.15 (density), i.e. clusters should be centred on density peaks, not sliced;
 (2) score ties (almost everything 10-11) - re-read the scoring table and tighten to the literal text; (3) TV spot 98.226 vs report 98.10 moves the equilibrium; (4) the candle structure should anchor the zone (report: supply candle = Upper Resistance,
 MoM supply = Equilibrium, BoM demand 04-16 = Mid-Range Support, sweep 97.63 + demand = Key Support) - try: build the named zones FROM the kept 4H structures and sweep targets / walls first, attach to each the levels within 0.15, score, then name by position.
 That last reading is the most literal match to both the report's key drivers and ruling L-39 ("C in the shape of A plus B") - implement it next, compare all five, then go on to the report printout and the Pine generator.

## 2026-11-25 ~23:10 UTC - assemble_anchored() added to e1_tool/e1_synth.py (zones built FROM structures: kept 4H S/D candles + sweep zones + tier-1/2 walls; overlapping anchors merged; levels within 0.10 attached and scored)
Result DXY Apr 20-24: CEILING 99.23-99.31 (wall at 99.29: sidecar K 108.155 puts the 1.1600 strike at 99.29, report K 108.0806 -> 99.22) · UPPER RESISTANCE 98.44-98.94 (TOO WIDE: two demand candles + sweep + walls chained into one anchor 98.53-98.84)
 · EQUILIBRIUM 98.10-98.39 (anchor BoM Supply 98.19-98.29 + sweep; report 98.29-98.41) · KEY SUPPORT 97.63-97.75 (anchor sweep 97.63-97.68; report 97.63-97.97) · no Mid-Range Support taken.
This reading is closer in KIND to the report (each zone sits on a structure) than the cluster-first one. To finish it:
 a) do NOT chain-merge anchors: merge only anchors that overlap by more than half of the smaller one, otherwise keep them as separate candidate zones (bloat came from chaining);
 b) the zone's own extent = the anchor span joined with the levels INSIDE or touching it (not everything within 0.10 beyond it) - the 0.10 band is for SCORING only;
 c) the K factor: use each component pair's rate at the boundary (TV close for GBPUSD; H.10 for the rest) and print the audit; the report's wall levels are reproduced exactly when its K is used;
 d) the expiry list must come from the Day-1 page + Day-2 forward rows (the sidecar file for 04-20 holds the Friday page rows: 1.1783 €1.409bn etc.); parse sidecar/raw/2026-04-20 Monday page or re-run the sidecar with the report's boundary rule;
 e) then names by position with equilibrium at spot and 0.20 separation, and compare all five again.
Call: `cd e1_tool && python3 -c "import json,e1_data as D,e1_pillars as P,e1_synth as S; m='2026-04-20'; sp=D.closed('DXY','60',m)[-1]['close']; sd=json.load(open('../sidecar/out/'+m+'.json')); r=S.assemble_anchored('DXY',m,sd['expiries']['EURUSD'],P.k_factor(sd['h10']['rates']),sp); print([(z['name'],round(z['bot'],2),round(z['top'],2)) for z in r['named']])"`

## 2026-11-25 (container clock 21:50 UTC) - e1_zones.py + e1_pine.py: FIRST TOOL RENDER of DXY Apr 20-24 in Pinebox (frame opened: evidence/e1tool_DXY_1h_2026-04-20_b.png)
Tool chain now: `cd e1_tool && python3 e1_zones.py MONDAY PAIR [K]` (prints named zones) ; `python3 e1_pine.py MONDAY PAIR > out/E1_PAIR_MONDAY.pine` ; render: `tools/pb ide FILE PAIR 1H; tools/pb goto FROM TO; tools/pbfit; tools/pb shot NAME chart`.
Zone rule in force (e1_zones.build) - assumptions A3/A4 to list for the operator:
 - seeds = (i) every 4H supply/demand candle from Step 0f that survives noise rejection (<=0.40 wide, <=3 weeks old, <=1X mitigated) and A4 (demand candle with spot below it / supply candle with spot above it = broken, dropped);
   overlapping same-side candles = one structure; (ii) every UNSWEPT D1 swing extreme of the last 10 days on its own side of spot that is not inside a candle (level zone = levels within 0.05 of the extreme).
 - zone extent = candle + levels within 3 pips of it (L-39 A+B); same-side zones that overlap/touch = one zone; score = best level in the 0.10 band + regime + POI tier; MODERATE+ shown.
 - names by position: Equilibrium = zone holding/nearest the weekly classic PP ("pivot area"); above: top = Resistance Ceiling, rest Upper Resistance; below: lowest = Key Support Band, rest Mid-Range Support.
 - REJECTED variant of A4 ("any later 4H close through the candle = broken"): it deleted the 04-16 demand candle 97.83-98.09, which is exactly where the Monday Apr 20 low reacted.
Result DXY Apr 20-24 (TV candles, sidecar K 108.155, sidecar expiries = Friday page forward rows) vs report:
 CEILING 99.13-99.18 (report 99.16-99.23) · UPPER RES 98.82-99.08, 3 supply candles 04-09/04-10/04-13 (report 98.77-98.99) · EQUILIBRIUM 98.17-98.44, supply candles 04-17 03:00 + MoM 04-13 23:00 + repeated-high sweep (report 98.29-98.41)
 · MID-RANGE SUPPORT 97.81-98.12, BoM demand 04-16 03:00 1X (report 98.00-98.12) · KEY SUPPORT 97.63-97.68, sweep low 04-17 (report 97.63-97.97). All five roles land on the report's structures.
What the candles did that week (seen in the frame): Mon low ~98.0 inside Mid-Range Support then rally; Tue-Wed consolidation inside Equilibrium; Thu high ~98.93 inside Upper Resistance then reversal; Ceiling and Key Support not reached.
Differences that are data-source, not logic: wall 1.1600 lands at 99.29 with sidecar K (99.22 with report K) so the ceiling zone has no wall inside; expiries differ (Friday page vs the report's Monday page); TV candle wicks vs yfinance.
Visual to improve: level lines are dense (37-39 levels in two zones), labels sit on the zone's top edge.

## 2026-11-25 (container clock ~22:05 UTC) - E1 TOOL WORKS END TO END; 13 week/pair renders made and opened; honest status
TOOL (all in e1_tool/): e1_data.py (bars, boundary) -> e1_pillars.py (pivots, MAs, fibs, K, Step 0 swings, 0.45 LSZ, 0.5 magnets, 0f 4H candles) -> e1_synth.py (collect levels + 6-dimension scoring; its assemble()/assemble_anchored() are superseded, kept only because e1_zones imports collect/score_level/degree)
 -> e1_zones.py build() = THE zone assembly + gap_scan() (Step 9.5) -> e1_pine.py (generator; `python3 e1_pine.py MONDAY PAIR > out/E1_PAIR_MONDAY.pine`) ; e1_outcome.py prints plain facts of what the week's candles did at each zone.
One command per render: `tools/e1render PAIR MONDAY` -> evidence/e1tool_PAIR_1H_MONDAY.png (tools/pbfit fits the axis around visible candles +-60%).
RULES ADDED SINCE THE LAST ENTRY (each from re-reading the prompt): sweep targets = ALL graded D1 swings in 90 daily bars (I had wrongly cut to 10 days) + every swing of the last 10 days; drawn LSZ = recent 10 days + older unswept;
 level zones of one side within 0.10 = one cluster (<=0.40 wide); candle zones NOT clustered (it merged the report's Ceiling + Upper Resistance - tried, reverted);
 Step 9.5 gap in-fill: only BETWEEN mapped zones, 2+ supporting signals within 3 pips, >=0.20 from zones and each other (an earlier version with map edges at weekly R3/S3 and 0.15 spacing spammed 12 lines per chart - removed).
FRAMES OPENED (evidence/e1tool_*): DXY 03-09, 04-20, 05-18, 06-08, 07-27, 08-17, 10-05; EURUSD 04-20, 06-22, 09-14; GBPUSD 04-20, 07-27, 10-26.
WHAT THE CANDLES DID (facts from e1_outcome.py + frames; NOT an accuracy score):
 - DXY 04-20 (reference week): Mid-Range Support 97.81-98.12 caught Monday's low, +82 pips; Equilibrium held price 44h; Upper Resistance 98.82-99.08 capped the week high (reversal 33 pips); Ceiling and lower zones not reached. Matches the original's behaviour.
 - DXY 03-09: support 98.42-98.59 caught the week low, +195 pips; Upper Resistance 99.15-99.44 was closed through within 1h; Ceiling 99.63-99.85 stalled price then broke (trend week).
 - DXY 05-18: week chopped around the Ceiling 99.27-99.36 (34h inside); lows reacted at the gap in-fill 99.00-99.04; all other zones far below, not reached.
 - DXY 06-08: range between Upper Resistance 100.06-100.16 (repeated highs) and gap in-fill 99.66-99.70 (lows, never closed through).
 - DXY 07-27: Upper Resistance 101.49-101.59 capped Mon-Tue (week high 101.62) then the sell-off closed through Equilibrium (2h) and three stacked supports 100.31-100.80 (bunched, pierced on Jul 30) - BAD, same complaint as before.
 - DXY 08-17: Mid-Range Support 99.36-99.52 held 60h then broke; Key Support 99.12-99.21 closed through in 1h; nothing mapped below 99.12 where the week ended (98.6) - BAD.
 - DXY 10-05: Ceiling 102.16-102.25 (MODERATE) pierced at first touch, price chopped around it; Equilibrium 101.59-101.92 held the Tuesday low; highs 102.45-102.5 had no zone; seven far supports never reached.
 - EURUSD 04-20: Mid-Range Support 1.1659-1.1701 caught the week low; Upper Resistance untouched by 5 pips. EURUSD 06-22 / 09-14: trend-down weeks, candle zones all above price, lower side nearly empty.
 - GBPUSD 04-20: chop inside Equilibrium all week. GBPUSD 07-27, 10-26: mixed.
HONEST VERDICT: the reference week reproduces (five zones on the report's structures, candles react as in the original). Across other weeks it is NOT uniformly at the reference's level: strong when the week trades inside recent 4H structure,
 weak in break-out / sell-off weeks (zones behind price, stacked supports pierced, empty space ahead). Do not claim 90%.
ASSUMPTIONS TO TELL THE OPERATOR: A1 strong move = inefficiency gap (b[i+1] vs b[i-1]); A2 sweep zones from every graded D1 swing + last-10-day swings; A3 named zones = valid 4H candles + unswept sweep-level clusters (not every level cluster), names by position, Equilibrium = zone at the weekly PP;
 A4 demand candle below spot's reach (spot under it) / supply candle with spot over it = dropped; one-time use = keep <=1X; expiries = sidecar's as-of page (Friday forward rows when Monday's page is published after 06:00Z), K from Fed H.10 rates in the sidecar.
NOT BUILT YET: e1_report.py (the report's audit sections), Step 0d/0e D1 order blocks, Step 0g 1H nested precision, Step 1 HWC/LWC (optional), Pillar 4/7 (optional -> NO DATA).

## 2026-11-25 (container ~22:20 UTC) - Step 0d/0e attempt REVERTED (git checkout); memory/13 written; all-weeks facts
- Tried Step 0d (D1 order blocks) as "daily candle before a close beyond it, move >=1.0 over >=5 days" + 0e (swing inside block = Confluent Floor/Ceiling, Structural 2 + bonus 2). Result: every candle of a trend became a block (20+ overlapping blocks),
  nearly every swing became "confluent", scores inflated, the reference week went from 5 zones to 8. Wrong reading -> reverted. If redone: only the ORIGIN base of each D1 move (not continuation candles), and check the reference week stays at its five zones.
- memory/13_E1_TOOL_STATUS.md = the morning report (what exists, reference comparison, honest per-week verdict, assumptions A1-A5, the open point: nothing mapped ahead of price in breakout / sell-off weeks).
- Facts over 120 week/pair maps in e1_tool/out/OUTCOMES_all_weeks.txt + outcome_rows.json (breakdown script was in the scratchpad; numbers copied into memory/13).
- Tool state at this entry = commit "memory: E1 tool status / morning report (13)..." on AGENT. e1_tool/e1 MONDAY PAIR is the entry point.

## 2026-11-26 - L-40 applied (1H zones, 4H overview); E2 v1 built and rendered on the anchor week
- e1_zones.valid_sd: 4H Step 0f = overview; zones = 1H candles (prior 14 days, same candle rule, <=1X, not broken); 1H candle inside a kept 4H zone inherits BoM/MoM and Tier 1 if 4H BoM. Anchor week DXY Apr 20-24 now 7 zones:
  Ceiling 99.08-99.18, Upper Res 98.87-99.06, Upper Res 98.66-98.85, Equilibrium 98.17-98.47, Mid Support 97.93-98.06 (1H BoM demand 04-17 17:00: Monday's low lands on it), Mid Support 97.68-97.84, Key Support 97.63-97.68.
- e1_tool/e2_shapes.py = ENGINE 2 (canon extract: e1_tool/canon_extract/P533_lines_1725-2057_PART_VI_ENGINE2.md). chain(): current shape from the last 3 days (day_shape: BS = range>=0.8 ADR & body>=60%; WL = range>=0.8 ADR & wick>=50%; R after BS/WL; else SS - thresholds are MY assumption E2-A1),
  SS 2 days (trading speed rule) unless last day was BS (then R 1 day) or a momentum WL; BS toward the WEAKER bounding zone (ZFP class of the zone type, then score, then tier; tie -> last shape direction / 4H bias); bound holds (Hard/Standard) -> WL at it;
  bound fails (Soft/One-Touch/Ghost) -> BS over 2 days to the next zone; target zone class decides next (Hard -> RWL, One-Touch -> PBS, else R) per 6.4.1. Output: days[] with path waypoints, primary chain, alternative, audit.
- Pine: E2 drawn as white dashed projected path + day labels (toggle show_e2). First frame (anchor week): path = Mon-Tue SS inside Equilibrium, Wed-Thu BS up into Upper Resistance, Fri R down - the candles did Mon dip/SS, Tue-Wed up, Thu high in Upper Resistance, Fri down. Direction and sequence match; timing ~1 day early at the start.
- e2 text check on other weeks: Jul 27 DXY 4/5 days same shape as my day classifier; Apr 27 and Aug 17 poor (predicted SS / BS up; week sold off). To investigate after E3 exists on the anchor week.
- E3 canon extract saved: e1_tool/canon_extract/P533_lines_2058-3210_ENGINE3_and_trade_structure.md; binding E3 spec = canon/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md (R-16).

## 2026-11-26 - E3 v1 built (e1_tool/e3_setups.py), wired into the Pine (show_e3), first run on the anchor week
- build(): per E2 day -> setup universe (SS/R-range: Consolidation LONG at nearest demand zone below + SHORT at nearest supply above; BS/PBS: HTF Swing with the move from the zone behind price; WL/RWL/R: Reversal at the zone reached).
  Entry TS-1 = near edge of the internal band (1H candle / sweep rung) closest to approaching price (+1 pip lift for order-block shorts, F1-A); SL = 3 pips (EU 2, GU 3, DXY 3) outside that band's far edge (ladder rule a), max 36 pips;
  TP = opposing-zone walk until RRR >= 3.0 (strong zone: near edge + 1 pip; else midpoint); freshness: no zone with a candle >2X; one setup per zone per direction; cap 11. Sessions: Consolidation = London, others = NY.
- simulate(): fill from the setup's day to week end on 1H bars; SL counted first on an ambiguous bar. Description only.
- Anchor week DXY Apr 20-24: #1 Mon LONG at Mid-Range Support E 98.05 SL 97.91 TP 98.75 RRR 5.1 -> TP hit; #2 Mon SHORT in Equilibrium E 98.25 -> SL; #3 Fri SHORT at Upper Resistance E 98.75 TP 98.07 -> filled, open +2.4R at week end.
  Only 3 setups: the BS days produce none because the demand zone was already used by #1 (dedup). Jul 27: 2 setups (1 SL, 1 not filled). NEXT: more of the spec (reinforcements on BS days, re-entry rules, SS scalps inside the range on 30m/15m), then pixel check.
- Entry point for everything is still `e1_tool/e1 MONDAY PAIR` / `tools/e1render PAIR MONDAY` (Pine now carries E1 + E2 + E3 with toggles).

## 2026-11-26 - E2 v1 / E3 v1 measured over all 40 DXY weeks: FAR from the goal (facts, not accuracy claims)
- Script (scratchpad, re-creatable): loops sidecar weeks, G.run -> E2.actual() day classifier vs forecast, E3.simulate().
- E2: forecast day shape+direction equal to my day classifier on 66 of 200 days; on directional forecast days the day closed in the forecast direction 46 of 91 (coin flip). Typical output is always "SS -> BS x -> R" - the engine barely discriminates weeks.
- E3: 84 setups in 40 weeks (about 2 per week - far below "catch the obvious trades"); 8 TP, 40 SL, 33 not filled, 3 open. Anchor week Apr 20-24: LONG 98.05 -> TP 98.75 hit; the SHORT inside the zone price sat in was removed by a fix (no entries at zones price is already inside).
- Fixes applied this round: E2 direction = failing ZFP class, same class -> 4H storyline (score/tier tiebreak removed); E3 skips zones containing price.
- DIAGNOSIS TO DO NEXT (in this order): (1) E3 stop-outs: measure on first touch of each E1 zone how far price runs in favour before it trades 3 pips past the entry band / past the whole zone - decides tight SL (rule a) vs next-rung SL (rule b) per the spec's confidence rule,
  and whether entries should wait for the spec's Phase 2.5 "1-2-3 retest" entry timing (canon 8.25) instead of a resting limit at the edge; (2) E3 count: SS days need scalps at BOTH range bounds every SS day and BS days need the with-move entry + reinforcements - currently dedup kills them;
  (3) E2: the current-shape step and the day classifier are crude (thresholds mine); re-read 6.2 priority order and anchor each day's shape to zone events (broke / rejected / inside) instead of candle body ratios; use the previous week's actual zone interactions.
- Frames: evidence/e1tool_DXY_1H_2026-04-20.png (E1+E2+E3 all layers), evidence/e1tool_DXY_1H_2026-04-20_e23.png (levels/LSZ/options hidden; not yet opened).

## 2026-11-26 - WHY E3 stops out: first-touch facts for E1 zones (tools/research/e1_first_touch_mfe.py PAIR; tools/research/e23_all_weeks.py PAIR)
- DXY, 40 weeks, 1H-worked zones: 110 first touches from outside (about 2.75 per week). Limit entry at the near edge of the entry band (1H candle / sweep rung), stop 3 pips past the band (median risk 10 pips):
  price ran >=1R on 60, >=2R on 43, >=3R on 29, >=4R on 19; 50 were stopped before 1R. With the stop past the whole zone (median risk 15.7 pips): >=3R on 18.
- By class (>=3R / touches): with the 4H storyline 21/65, against it 8/45. 4H-BoM with 4H 4/23, MoM with 4H 10/26, level zones with 4H 4/7, 1H-only BoM against 4H 0/12. By type: Soft Wall 17/56, Standard 7/21, Hard 2/10, Ghost 3/23.
- Reading: a resting limit at the zone edge with a tight stop wins about 1 in 4 at 3R - break-even, nowhere near the goal. Counter-storyline entries are clearly worse (canon: MoM = ladder steps for trend-aligned trades only; 6-check direction validation 8.18).
- E3 spec facts read first-hand this round: cap key is (pair, anchor, DAY) - one setup per anchor per day, the same zone may be used on several days (I dedup per week - wrong); spec says no weekly cap ("ALL valid setups should be mapped") but CLAUDE.md hard constraint says <= 11/week/pair - keep 11;
  8.25 entry timing: 0 retests = scalp only, 1 = scalp + confirmation, 2 = swing entry valid, 3+ = TP target only; Law 27 trade-flow chains: TP of one setup = entry of the next (BS->R, BS->WL, WL->RWL, SS->BS at the range boundary break).
- NEXT: (a) E3: per-day anchor cap, direction validation with the 4H storyline (counter-storyline only at 4H BoM 0X-1X), entry timing by retest count; (b) re-measure; (c) E2 day shapes anchored to zone events; (d) EURUSD/GBPUSD runs; (e) frames for 4 weeks; (f) external review; (g) ship package + blind test.

## 2026-11-26 - FACT: the week's net direction is not predictable from simple pre-week signals (120 week/pair cases: DXY, EURUSD, GBPUSD x 40 weeks)
- Agreement of each signal with the week's net direction (Friday close vs boundary spot): 4H 20-bar slope 56/120, 4H 60-bar 62, prior-week direction 49, last-day direction 54, spot vs weekly PP 51, upper/lower half of prior week 51, above D1 SMA20 64, above D1 SMA50 63. All near a coin flip.
- 52 of 120 weeks moved at least one average daily range net.
- CONSEQUENCE for E2: a single-direction weekly chain cannot reach 80-90%. Canon already says so: Step 4 MANDATORY alternative chain with a DECISION ZONE; R3 law; SS scalps both directions. So E2 must be rendered and graded as a CONDITIONAL map:
  primary path + alternative path, each tied to "zone X holds / fails", and E3 must carry setups for both branches (the setup is valid only when its branch's trigger happens). The day forecast is then judged by: did price follow one of the two mapped branches, and did the branch switch at the decision zone.
- E3 current facts DXY 40 weeks: 18 TP / 38 SL / 65 not filled.
- NEXT: implement the alternative chain as a second path (dashed grey) with its decision zone label; E3 setups per branch with the trigger written on the label; then pixel-check the anchor week + 3 more weeks.

## 2026-11-26 - alternative branch added (E2 alt_days, E3 branch=ALT, grey path in Pine); facts got WORSE until setups are gated on their trigger
- e2_shapes.chain(force_dir) builds the other-direction chain; result keys: days, alt_days, bdir, decision_zone, primary, alternative. e3 builds setups for both branches (label "(ALT)"), sorted by day, cap 11.
- DXY 40 weeks now: 20 TP / 58 SL / 108 not filled. The ALT setups and the BS-day "with the move" setups are resting orders with no condition: they fill when the OTHER branch is playing out and stop.
- FIX NEXT: (1) every non-SS setup carries an activation condition taken from its branch: PRIMARY BS up = "1H close above the decision zone's far edge", ALT = "decision zone rejected: 1H close back below its near edge after a touch" (canon 6.2: BS confirmed by a sustained move beyond the zone, 15+ min);
  simulate() must only arm a setup after its condition is met, and the Pine label must state the condition. (2) BS-day entry anchor = the broken zone itself retested from the other side (role reversal: broken resistance = new support, spec 8.1 lifecycle BROKEN) - Law 27 "SS -> BS: range boundary break becomes BS entry";
  not the far demand zone behind price. (3) keep SS scalps unconditional at the range bounds.

## 2026-11-26 - E3 gating + retest entries implemented; breakdown of results (DXY 40 weeks; facts for debugging)
- e3_setups: retest() = Transition entry at the broken decision zone's far edge, armed by a 1H close beyond it; Reversal setups armed by their branch's break; simulate() honours 'arm'. Pine labels state the condition.
- Totals: 18 TP / 49 SL / 93 not filled / 3 open. By category: Consolidation/PRIMARY 13 TP / 24 SL; Consolidation/ALT 2 / 9; Reversal/PRIMARY 2 / 1; Reversal/ALT 1 / 6; Transition (retest of the broken zone) 0 TP / 9 SL.
  With the 4H storyline 13 TP / 36 SL; against 5 / 13. Monday fills 7 TP / 17 SL.
- Reading: the only setup family with positive expectancy so far is the SS scalp at the nearest zone on the primary side (RRR ~4-5, ~35% hit). Retest-of-broken-zone with a tight stop fails every time -> wrong geometry (re-read spec 8.8 reinforcement / 8R ladder: reinforcements are STOP-LIMIT orders at liquidity zones 2-3 zones ahead in the direction of the move, not retests).
  ALT-branch consolidation scalps should not exist (SS scalps belong to the range, they are branch-independent) - they are duplicates on the other side taken on days the alt chain calls SS.
- Anchor week now: #1/#2 LONG 98.05 -> TP 98.75 (Mon, Tue), #3 ALT reversal long not armed. The Friday short from Upper Resistance (the week's obvious short) is missing: lost to direction validation (4H bias up) - Reversal at the BS target must be exempt from the trend check when the chain itself predicts R/RWL there (E2 designates, E3 obeys).
- TODO next round: (1) drop ALT consolidation duplicates; (2) exempt chain-designated reversals from the 8.18 consensus; (3) replace retest() with 8R reinforcement stop-limit logic or drop it; (4) pixel-check anchor week + Jul 27 + Aug 17 + Oct 5; (5) EURUSD / GBPUSD.

## 2026-11-26 - zone names by side; Aug 17 pixel FAIL logged; transition (range-break) setups coded but emit nothing
- e1_zones naming: supply-side = RESISTANCE (top = Ceiling), demand-side = SUPPORT (lowest = Key Support Band), EQUILIBRIUM = zone containing spot (else the adjacent zone holding the weekly PP). Anchor week unchanged.
- Frame evidence/e1tool_DXY_1H_2026-08-17_e23.png OPENED: FAIL. Primary path BS up; candles: Mon-Wed consolidation 99.5-99.65 around Mid-Range Support (Hard Wall) then Thursday crash to 98.7 through Key Support; alt path (grey, down) far too shallow; nothing mapped below 99.36; no short taken; ALT long stopped.
- e3_setups: Transition setups (stop entry 2 pips beyond the bounding zone, armed by a 1H close beyond it, SL the other side of the broken zone + buffer, TP = P9 Step 4 measured move = failing level -/+ range height, snapped to an unswept sweep extreme within 0.20 or the first Hard/Standard zone on the way).
  They never pass RRR >= 3: e.g. Aug 17 short E 99.45 SL 99.62 (17 pips) target 99.22 -> 1.35. Either the stop must follow the spec's rule (b) "1-2 pips inside the close edge of the next step" (i.e. just back inside the broken zone, ~5 pips) or the target must be the next mapped zone beyond the measured move. Not decided; test both against the spec text 8.3 Phase 4.2 before choosing.
- Tag e123-anchor-apr20 exists LOCALLY only (pushing tags is refused with 403; branch pushes work). Checkpoint commit = the one with message "ledger: anchor week all three engines PASS frame".
- Three-pair facts file: e1_tool/out/e23_all_weeks_3pairs.txt (written by tools/research/e23_all_weeks.py DXY EURUSD GBPUSD; last two lines = totals).
