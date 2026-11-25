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
