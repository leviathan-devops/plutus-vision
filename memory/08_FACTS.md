# 08 — DURABLE FACTS (append; cite where each came from; never guess here)

## Inputs (all outside the repo; re-unzip from /root/.claude/uploads/b6c77a81-471c-536b-9631-0319cefbf3ab/ if lost)
- `/home/user/inputs/handover/PLUTUS_VISION_CONTEXT_HANDOVER/` — previous agent's handover (00_HANDOVER primary, 01_BINDING_SPEC, 03_HOST_BIBLES).
- `/home/user/inputs/pinebox/ship-approved-v2/` — Pinebox package (manual: src/manuals/OPERATOR_MANUAL_pinebox.md).
- `/home/user/inputs/canon/Toolset/` — same six canon files as repo `canon/Toolset/`.
- `/home/user/inputs/trades/WINNING_TRADE_LIBARARY/` — operator's annotated screenshots; `Jul_6-10_DXY_Gold_Standard/` = golden-week oracle (8 PNG, DXY + EURUSD 1h); `Original_Training_Data/*.pdf`.
- `/home/user/inputs/aether/aether_agent_backend_v2/` — framework for the embedded agent (L-11).
- `/home/user/handover-branch/` = git worktree of `origin/handover`: `Original_Canon_Data/` has the weekly report oracles
  (`IP Heatmap Reports/*.pdf` for Apr20-24, Apr27-May1, May 4-8, May25-29 2026; `Validated Trade Reports/Trident_Report_2026W14_Mar30-Apr3.md`; `Pine Scripts/trident_v8.pine`).
  Recreate: `git fetch origin && git worktree add -f /home/user/handover-branch origin/handover`.

## Pinebox (measured 2026-11-25)
- Up via `tools/pinebox-bootstrap.sh`; session `plutus-main`, instance 0, adapter xvfb display :3; ports station 9741, rail 9754, server 9851, CDP 9222, room 9443.
- Env for every command: `export PATH=$HOME/.local/bin:$PATH XDG_RUNTIME_DIR=/run/user/0`.
- Verbs: `pinebox shot --session plutus-main --out F.png [--section chart|plot]`, `load --pine F [--pair P --tf T]`, `asset --set EURUSD --tf 4H`, `tf --tf 30m`,
  `chart --op fit|zoom|pan|view`, `tab --to backtest|pine`, `backtest --op create|open|step|date|state ...`, `drive --action click|type|key`.
- Chromium must be wrapped with `--no-sandbox` (root). `ss`, `xdpyinfo` must be installed. The image judge (:8090) is absent -> `pinebox verify` cannot answer WORKS; I judge frames myself.
- Bar store `~/.local/share/pinebox/data/tv-bars/{TVC_DXY,FX_EURUSD,FX_GBPUSD}/{15,30,60,240}/YYYY-MM.json`, 2025-02-02 -> 2026-11-06 (TradingView bars). IDE chart = newest 5000 bars of a cell.
- First frame read (frames/pb_000_boot.png): PINE IDE tab with editor (RUN, CAPTURE, EXPORT TO BACKTEST, GATE buttons), DXY 1h chart Aug->Nov 2026, BACKTEST tab at top.

## Web data + model (measured 2026-11-25)
- `curl https://investinglive.com/` -> 200 (708 kB) with a desktop UA; `https://www.federalreserve.gov/releases/h10/current/` -> 200.
- `curl -H 'Authorization: Bearer proxy-injected' https://opencode.ai/zen/v1/models` -> model list (key is injected by the proxy; never in env).
  Chat base URL reported by the list for chat-completions models: `https://opencode.ai/inference/openai/v1`. Model to use: Muse Spark 1.3 Contributor, reasoning effort high (L-10) — look up its exact id in the list.

## Golden week oracle, first-hand reads of the screenshots (Jul 6-10 2026) — approximate until `context_management/oracle/golden_week.json` lands
- DXY 1h (g1): week frame Mon Jul 6 -> Fri Jul 10. Upper green IP band ~101.19-101.29 (white line 101.24). Lower green band ~100.55-100.675.
  Red "4H (Unmitigated) | BoM" supply ~101.33-101.44 above the ceiling. Blue "1H (Unmitigated) | BoM" demand ~100.65-100.74 at the floor.
  Price: Mon-Tue range/drift up, Wed Jul 8 peak ~101.27 into the ceiling band, sell-off to ~100.62 on Fri Jul 10 (into floor band + 1H BoM), bounce.
  Showcase trade: short ~101.275, SL ~101.33, TP ~100.675.
- DXY 1h (g4): ~16 green liquidity rungs between 100.545 and 101.25 (101.25, 101.24, 101.20, 101.19, 101.14, 101.115, 101.09, 101.00, 100.975, 100.94, 100.905, 100.845, 100.77, 100.68, 100.61, 100.545) and ~8 position-tool trades across the week.
- EURUSD 1h (g5, g7): week range ~1.1393-1.1456; "1H (Unmitigated) | BoM" supply ~1.1446-1.1456 (top), "1H (Unmitigated) | MoM" demand ~1.1400-1.1417 (bottom); ~7 trades; fib grid 0 = 1.13925, 1 = 1.14315, 1.618 = 1.14556.

## Canon structure (v5.3.3 prompt, `canon/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md`)
- Part II context 468-739 · Part III data harvesting 739-1540 · Part IV calculations 1540-1568 · Part V report 1568-1725 · Part VI Engine 2 1725-2058 ·
  Part VI-B Engine 3 (superseded by corrected doc) 2058-2575 · Part IX multi-pair 3257-3688 · Appendix A strike->DXY 4011 · B ZFP 4052 · C pivots 4078.
- Web sources named in Part III: forex.com (14 mentions), investinglive.com (6), tradingview.com, federalreserve.gov (H.10), ice.com.
- Digests (written by reader agents, verify before trusting): `context_management/spec/{E1_ALGO,E2_ALGO,E3_ALGO,HANDOVER_DIGEST,PINEBOX_ENGINE_NOTES,LAWS_DIGEST}.md`, `context_management/oracle/*`.

## E1 canon essentials (from context_management/spec/E1_ALGO.md, cites SP:line = v5.3.3 prompt)
- Assembly SP:1496-1505: collect ALL levels from 9 pillars, never filter by distance to spot (SP:735); score each level on 6 dimensions (0-2 each) + structural-extreme bonus (<=2) = 0-14;
  cluster: 3+ levels within 0.15 DXY = HIGH-DENSITY ZONE, pairs within 0.10 = TIGHT CONFLUENCE; group at 0.10-0.15; zone degree = its highest-scoring level; name the zones.
- Pressure degree: 12-14 EXTREME, 10-11 HEAVY, 8-9 MODERATE-HEAVY, 6-7 MODERATE, 4-5 LIGHT, 0-3 MINIMAL. Synthesis shows MODERATE and above.
- Pivots (P1): classic, fibonacci (0.382/0.618/1.0), camarilla (1.1/12,/6,/4,/2) on prior week HLC and each of the last 3 trading days.
- MA grid (P2): EMA+SMA 9,10,20,50,100,200 (daily by inference); 3+ MAs within 0.15 = cluster; recapture (cross above 50/100/200 within 3 sessions) +2.
- Structural (P5): 90 D1 bars; swing low = lower wick >= 0.15 and close in upper half (mirror for highs); D1 order block = base before a move >= 1.0 lasting >= 5 days;
  repeated extremes within 0.05 on 2+ dates (+1.5 / +2.0), role reversal +2.0; LSZ = 0.05-wide band at the exact swing extreme (extension 0.05-0.10);
  4H S/D = the single 4H origin candle [low, high] before a move >= 0.5 lasting >= 3 trading days, max width 0.40, 60-day scan, drop if > 3 weeks old with no interaction.
- Round numbers (P6): .00/.50 = 2 pts, .25/.75 = 1 pt (DXY). Fib retracements of prior-week range + swings (ratios 0.236/0.382/0.618, ext 1.618).
- Options (P3/P8): strikes from investinglive 10am NY cut; tier 1 >= $1.5B (CRITICAL OPTION WALL), tier 2 $850M-$1.499B (SIGNIFICANT MAGNET), below = excluded.
  EUR/USD strike -> DXY: DXY = K * EURUSD^-0.576, K = 50.14348112 * USDJPY^0.136 * GBPUSD^-0.119 * USDCAD^0.091 * USDSEK^0.042 * USDCHF^0.036 (spots from Fed H.10). NEVER convert DXY zones to pair zones.
- Analysts (P4): explicit S/R levels; tier 1 = ING, forex.com (Matt Weller); 2+ tier-1 agree = 2 pts.
- ZFP (Appendix B): Hard Wall 5-15% (needs option wall >= $1.5B + 3 pillars + confluent floor/ceiling), Standard 15-30%, Soft 30-50%, One-Touch 50-70%; modifiers only add. ZFP by pixel width is banned (R-17).
- POI tier: IP zone overlapping a 4H BoM (0X-1X) = Tier 1; IP only = Tier 2; 4H only = Tier 3.
- Pairs run their OWN full pipeline on their own price; DXY gives direction only (SP:101, 3313, 3639). Pip: DXY 0.01, pairs 0.0001.
- PLACEHOLDERS in v5.3.3 ("unchanged from v4.5.2"): P5 steps 0g/0h/1-5, P6, P7, P8 core, P9 -> full text in the v4.5.2 prompt on the handover branch.

## Pine engine facts (TESTED 2026-11-25 with indicator/probes/probe1.pine through the station /model route)
- Engine: `@luxalgo/vela-pinets` PineEngine in the station (:9741). IDE page and Backtest room both call POST /model {source, instanceId, bars, market, inputs}. Client timeout 90 s (charts/station-engine.js TIMEOUT_MS). Max 20000 bars, 8 MB model.
- WORKS: UDT (`type`), arrays of UDT, `for x in arr`, `var`, input.int/string/time (inputs are passed in the /model body), timeframe.change("W"/"D"), hour()/dayofweek() with "America/New_York",
  box.new with xloc.bar_time + text, label.new, line.new extend, plot, str.format, syminfo.mintick (0.01 on DXY). 5000 1H bars = 42 weeks; probe ran in 1.4 s.
- DOES NOT WORK: `request.security` returns NaN for "D", "W", "240" (no higher-timeframe or other-symbol data) -> ALL higher-timeframe bars (4H, D, W) must be aggregated in-script from chart bars. No cross-symbol data (a EURUSD chart cannot read DXY).
- Tables do not paint (earlier session). `pinebox shot --section plot` refuses on the Backtest tab (use full).
- Sealed V1 (`indicator/plutus-vision-v1.sealed.pine`, sha256 0d20e8314ce992fc...) execution time is ~quadratic in bars: 2500 bars 9.6 s, 5000 bars 37 s, 8750 bars 81 s (this container).
  The Backtest room feeds ALL bars up to the replay cursor (8751 at Jul 6 2026) -> V1 alone sits at the 90 s timeout there and paints nothing (frame bt_004). Weeks before ~May 2026 fit; later weeks time out in the room on this machine.
- V1 at the Jul 6 06:00 anchor (probe, 8750 bars): 65 boxes incl. demand 100.603-100.746 and supply 101.396-101.444, 101.658-101.746 (match the operator's hand-drawn 1H BoM demand ~100.65-100.74 and 4H BoM supply ~101.33-101.44).
- Preflight tool: `tools/pine-probe.py FILE --pair DXY --tf 1H --limit N --until 2026-07-06T06:00` (never a success gate). Chart helper: `tools/pb goto FROM TO [bt]`, `tools/pb shot NAME [chart|plot|full]`, `tools/pb load FILE PAIR TF`, `tools/pb eval JS`.
- TV 4H bars in the store start at 22:00 UTC Sunday in winter (17:00 New York) -> 4H buckets are New-York-17:00 aligned (17, 21, 01, 05, 09, 13 NY).

## E1 ORACLES (from context_management/oracle/REPORT_ORACLES.md — ranked there; read sections 4.2, 4.9, 4.11)
- BEST E1 oracle: week 2026-11-09 DXY, operator-approved SIX zones ("DO NOT ADD ANY MORE ZONES THESE 6 ARE CORRECT ... 3 4 AND 5 NEED REFINEMENT. 1 2 AND 6 ARE CORRECT"):
  1) 102.437-102.535 CORRECT  2) 102.205-102.354 CORRECT (contains Fri close 102.279, prior wk high 102.358)  3) 101.700-101.840 REFINE (too wide; core "from where price traded")
  4) 101.933-102.061 REFINE core 101.97-102.01  5) 101.453-101.601 REFINE core 101.49-101.53  6) 100.986-101.099 CORRECT (prior wk low 101.099 = its top).
  Prior week H 102.358 L 101.099 C 102.279. NOTE (mine): all six sit on DXY quarter figures 102.50 / 102.25 / 102.00 / 101.75 / 101.50 / 101.00. Store has no bars after Nov 6 -> zone-match only, no reaction check.
- GRADED report: week 2026-04-20 DXY (v4.5.2, zones graded A/A+ in the post-mortem). Prior week H 99.18 L 97.63 C 98.10. Zones:
  RESISTANCE CEILING 99.16-99.23 HEAVY 10 (weekly R1 + repeated high 99.18 + round) A+ · UPPER RESISTANCE 98.77-98.99 MOD-HEAVY 8 (daily R1 + 4H BoM supply + fib 38.2) A ·
  EQUILIBRIUM 98.29-98.41 MOD-HEAVY 9 (repeated high magnet 98.29 3x + daily pivots + prior closes) A+ · MID-RANGE SUPPORT 98.00-98.12 MODERATE 7 (prior closes + daily PP/S1 + round 98.00) A ·
  KEY SUPPORT BAND 97.63-97.97 HEAVY 11 (LST 97.63 + 4H BoM demand + weekly S2/S3) B/B+ "far too wide ... should be 97.75-97.97 or split"; post-mortem asks cluster threshold 0.10 not 0.15.
  LSZ: 97.63-97.68, 97.83-97.88, 97.97-98.02, 98.53-98.58 (demand); 98.29-98.34, 99.18-99.23 (supply). Actual week: BUY trend all week (report's SHORT call was wrong). Post-mortem real trades: L 98.02 SL 97.87 TP 98.77; L 98.29 SL 98.185 TP 98.77.
- Other E1 reports (ungraded): 2026-05-25 DXY Leviathan v4.5.2 (6 zones, E1+E2), 2026-04-27 (12 zones), 2026-05-04 (6 zones), 2026-03-30 W14 (hindsight-contaminated), W22 v5.3.3 (mid-week, corrupt K).
- GOLDEN WEEK 2026-07-06: no report E1/E2 exists. E3 oracle = operator's golden DXY trades (3-pip tolerance in the old validator):
  Mon L 100.945 / SL 100.905 / TP 101.115 (SS long @1H LQZ) · Mon S 101.14 / 101.20 / 100.845 (BS short @1H LQZ) · Tue L 100.845 / 100.77 / 101.19 (SS long @1H MoM) ·
  Wed S 101.19 / 101.25 / 100.975 (SS short @1H LQZ) · Wed L 100.975 / 100.905 / 101.24 (RWL long @1H LQZ) · Wed S 101.235 / 101.33 / 100.68 (BS short @4H BoM) · Thu ladder short (no levels) · Fri WL+RWL (no levels).
  Shape tags on those trades: Mon SS+BS, Tue SS, Wed SS+RWL+BS, Thu Ladder, Fri WL+RWL. EURUSD: Wed L 1.1402, Wed L 1.13935 (entries only).
  Prior week (Jun 29-Jul 3) DXY: H 101.595 L 100.558 C 100.878.

## WHY THE PREVIOUS E1 TOOL FAILED (handover section 2.3 — mechanism, do not repeat)
- It pooled 459 levels (88 pivots, 25 MAs, ...) and formed zones as "the 0.15-wide band holding the most levels". HIGH-DENSITY flagged 450 of 459 levels -> every price is dense -> 23 zones, 21 of them 0.115-0.150 wide (the rule fills the width). Then a render cap hid 17 (banned, R-37).
- Zone 2 (approved) scored LIGHT because the prior-close / prior-high anchors (Pillar 5 Steps 1-5, the v4.5.2 placeholder) were not implemented and option walls were converted with week-old H.10 rates.
- Lesson: zones must be seeded by STRUCTURAL ANCHORS scored across dimensions (a pivot/MA/round/option/analyst level scores a dimension when it coincides with the anchor within the canon pip tolerance), not by counting levels in a band. A level with one dimension stays MINIMAL and never becomes a zone. The zone's extent is the confluence itself.

## Memory graph (OmniGraph 0.16.0, live)
- Install: `curl -fsSL https://raw.githubusercontent.com/ModernRelay/omnigraph/main/scripts/install.sh | VERSION=v0.16.0 bash`; then `tools/mem/mem rebuild`. Graph at /home/user/.plutus-mem (rebuilt from memory/*.md + memory/graph_log.jsonl; markdown is the source of truth).
- Use: `tools/mem/mem q "<words>" [-n 5]`, `mem get <id>` (ids: T3, D-06, L-05, LS-02, J-YYYYMMDD-HHMM), `mem add <type> <id> <title> <body>`, `mem link <from> <edge> <to>`, `mem status`. Read verbs auto-sync.
- More engine facts (probe2): timeframe.in_seconds(), time_close, timestamp(tz,...), year/month/dayofmonth/hour/dayofweek with tz, str.format_time, map, matrix, array.sort/median/max all work. DXY week opens Sunday 18:00 New York in the store.

## E1 placeholders RESOLVED from v4.5.2 (context_management/spec/E1_V452_FILL.md; V452 = v4.5.2 prompt on handover branch)
- P5 Step 1 price anchors: prior daily close (last 3-5 days), prior daily HIGH and LOW for EACH of the last 5 trading days, prior weekly close, prior weekly high/low. Step 2 HWC/LWC = highest / lowest WEEKLY CLOSE of a period (calendar year in the example).
  Step 3 recapture of a major MA (50/100/200 within 3 sessions) = key anchor. Step 5: exact anchor match = Structural 2, proximity = 1; bonus LST/SCT +1, repeated 2 dates +1.5, 3+ / role reversal +2, confluent floor/ceiling +2, cap +2.
- P5 Step 0h minor swings: D1 AND 4H, wick >= 0.08, close-position 40% (relaxed reading: low needs close_pos >= 0.40, high <= 0.60), Structural 0.5. Step 0g: 1H zones only nested inside a 4H/D1 zone or as gap-fill (gap >= 0.20).
- P6 fibs: 0.236 / 0.382 / 0.500 / 0.618 measured DOWN from H of (i) prior week H/L and (ii) the most recent significant D1/4H swing high-low (2-4 months); fib within 5 pips + round number = 2 pts, fib only = 1 pt (Technical). Round grid .00 (+2) .50 (+1.5; Synthesis says 2) .25/.75 (+1).
- P9: ZFP = base(zone type) + sum(modifiers), cap 95. Regime dimension: ZFP < 20 -> 2, 20-50 -> 1, > 50 -> 0. Measured move: Raw = Range_High + (Range_High - Range_Low), snap to structural extreme within 0.20. > 45 measured move, > 50 BREAKOUT RISK, 25-45 "sweet spot".
  Modifiers computable from price: momentum toward zone +10-20, cascade (prior zone just broke) +20-30, EMA-200 cross +15-25, repeated-extreme magnet within breakout range +10-15.
- Names (V452:1148-1155): RESISTANCE CEILING = top zone, max selling pressure; UPPER RESISTANCE = secondary selling zone; EQUILIBRIUM = pivot area; MID-RANGE SUPPORT = dip-buyer zone; KEY SUPPORT BAND = max buying pressure.
- Clustering flags: HIGH-DENSITY (3+ within 0.15), TIGHT CONFLUENCE (pair within 0.10), ISOLATED LEVEL (none within 0.15; can still be a zone row). Gap scan: gaps >= 0.20 between zones -> GAP IN-FILL needs 2+ signals (Structural 1).
- POI: Tier 1 (+2, capped at 14) IP zone overlaps 4H BoM 0X-1X; Tier 2 (+1) IP only or MoM overlap; Tier 3 4H BoM only.
- 4H mitigation: soft = wick taps edge and is rejected (barely counts); hard = full bodies enter and consolidate (weakens). Counted over prior 2-3 weeks.
- STILL UNDEFINED IN EVERY VERSION (my decisions needed; record each in 03_DECISION_CHAIN): swing bar-count; "large bodies"; point inside ZFP ranges; zone top/bottom rule; zone width limits; zone count; "strong reaction"; "consolidation"; what a pivot is matched against; pair-unit tolerances.

## Web sidecar scouting RESULT (context_management/spec/SIDECAR_SCOUT.md; raw pages in sidecar/raw/<week>/)
- investinglive (plain curl works): weekly sitemap `https://investinglive.com/sitemaps/news/articles/<ISOYEAR>-W<WW>.xml`; `<lastmod>` == `article:published_time` (mechanical as-of filter).
  Expiry post = "FX option expiries for <date> 10am New York cut"; the table is a 900px JPEG on `investinglive.com/cms/media/` (needs a vision read).
- Fed H.10: `https://www.federalreserve.gov/releases/h10/<YYYYMMDD>/`, dates from `releaseDates.json`; last before the Jul 6 anchor = 2026-06-29.
- Model gateway: model id `muse-spark-1.3-contributor` is listed ONLY at `https://opencode.ai/zen/go/v1/models`; Responses API at `https://opencode.ai/inference/go/openai/v1/responses`; needs header `x-opencode-session`; takes images; effort minimal..xhigh. (`muse-spark-1.3` without -contributor = 402.)
  Its image read at effort high got 23 of 33 table entries right (bold flags missed) -> a single model read is NOT reliable enough; needs a cross-check (second read / crop zoom / my own read).
- BLOCKED by the proxy or bot walls: forex.com (Cloudflare 403 by curl; headed browser gets current pages only), ING, FXStreet, archive.org, Yahoo, TradingView, FRED, CME; ICE has only a spec page. => Pillar 4 analyst levels are limited to investinglive posts here.
- The Monday expiry post is published ~05:47Z (Jul 6) but 06:08Z on Apr 20 -> with a 06:00Z anchor some Mondays' own post is after the anchor; the Friday post's forward row for Monday is always available.
- GOLDEN WEEK option data (scout's read on 4x crops; verify myself before use):
  EUR/USD Mon Jul 6 cut (published 05:47:01Z): 1.1300 EUR830m, 1.1400 EUR2.2bn, 1.1450 EUR1.4bn, 1.1500 EUR2.4bn, 1.1600 EUR1.0bn.
  EUR/USD Fri Jul 3 cut: 1.1300 985m, 1.1325 703m, 1.1350 790m, 1.1370 1.6bn, 1.1375 1.1bn, 1.1380 596m, 1.1400 1.0bn, 1.1430 837m, 1.1450 873m, 1.1500 2.0bn, 1.1600 2.0bn.
  (Operator's hand-drawn EURUSD golden-week zones: demand ~1.1400-1.1417, supply ~1.1446-1.1456 -> they sit ON the 1.1400 (2.2bn) and 1.1450 (1.4bn) strikes.)
- Analyst levels found before the anchor: EUR/USD 1.14 / 1.10 / 1.18 (Jul 2 post); USD/JPY 160.70, 161.84-92, 162.00, 162.80 (Jul 6 05:03Z). None for DXY or GBP/USD.

## W14 baseline report (2026-11-25) and the research scorer
- Report: Trident_Report_2026W14_Mar30-Apr3.pdf (14 pages; uploads dir, id d253d0fc). Page 1 option expiries (investingLive, strikes below $850M excluded), page 2 prior-week closes + TARGET WEEK OHLC + red-folder events,
  page 3 E1 maps (4 bands per pair, see 04 L-17), page 4 E2 chain (EURUSD Mon BS down 85, Tue WL up 80, Wed BS up 70, Thu WL down 80, Fri SS 65), pages 5+ E3.
- Toolset.zip (unzipped /home/user/inputs/toolset_glm/Toolset) = the same 6 files as canon/Toolset (v5.3.3 prompt, corrected E3 doc, fractal architecture, validator, report template, trident_engine3_v8.py).
- Realized W14 (bar store): DXY week H 100.643 L 99.298 (prior week H 100.206 L 98.880 C 100.193); EURUSD H 1.16271 L 1.14430 (prior 1.16395 / 1.14844 / 1.15078); GBPUSD H 1.33462 L 1.31593 (prior 1.34792 / 1.32515 / 1.32515).
- Scorer semantics (tools/research/score.py): band HELD = price entered and left by the side it came from by >= D before running D past the far edge; BROKEN = the reverse; CONTAINS = unresolved but week high/low inside;
  BOUNDING = untouched nearest band within 2D beyond the week extreme; FLOATING = untouched otherwise; missed = week high/low not inside any band (+-3 pips).

## THE LIQUIDITY LADDER = THE SEALED V1's GREEN ZONES (measured 2026-11-26 against the golden-week oracle; this is the Earth layer E3 trades on)
- Run the sealed V1 through the Pinebox engine: `python3 tools/pine-probe.py indicator/plutus-vision-v1.sealed.pine --pair DXY --tf 1H --limit N --until 2026-07-06T06:00 --dump out.json` (11 s at 2500 bars).
  Model -> `boxes`: order blocks bgColor `#3179f533` = bullish / demand, `#f77c8033` = bearish / supply (LuxAlgo internal OBs, extend right); liquidity zones bgColor `#2E8B5773` (+ edge lines `#3FA46A`). Labels: BOS / CHoCH / EQH / EQL / Strong-Weak High-Low.
- V1's liquidity module (sealed file lines 864-1160; "V2 - THE OPERATOR CANDLE DETECTOR (SMC_Liquidity_Notes.md)"): swing pivots (length 5, right 1); a level is touched when price TRADES within 0.5 x ATR(14) of it; second touch = build-up (src 16); wick sweep (wick >= 2 x body, tip beyond, close back) + rejection (same bar, or a close >= 1.5 ATR away within 3 bars) = confirmed (src 8);
  levels kept in a bounded buffer (1500, evict oldest); on the LAST bar all levels are sorted by price ASCENDING and merged into bands (gap <= 0.5 ATR); a band is emitted while fewer than 60 zones exist -> WITH TOO MUCH HISTORY ONLY THE 60 LOWEST-PRICED BANDS ARE DRAWN.
  Measured at the Jul 6 anchor, DXY 1H: 400 bars -> 27 zones 99.42-101.69; 800 bars -> 49 zones 98.93-101.69; 1500 bars -> 60 zones 97.61-100.70 (cap bites, nothing near price); 2500 bars -> 60 zones 96.47-99.47.
- ORACLE MATCH (400 or 800 bars): V1's liquidity zones lie within 3 pips of 15 of the operator's 16 hand-drawn golden-week rungs (missing only 100.61). Bands near price (800 bars), each 2.3 pips thick:
  101.470-101.493, 101.405-101.428, 101.349-101.372, 101.312-101.335, 101.273-101.296, 101.203-101.226, 101.163-101.186, 101.104-101.127, 101.026-101.049, 100.969-100.992, 100.929-100.952, 100.893-100.916, 100.836-100.859, 100.780-100.803, 100.730-100.753, 100.674-100.697, 100.523-100.546.
  V1 order blocks at the anchor: demand 100.603-100.746 (his "1H BoM demand ~100.65-100.74"), supply 101.396-101.444 (his "4H BoM supply ~101.33-101.44"), supply 101.658-101.746; with 800 bars also demand 100.206-100.336 and 99.491-99.536.
- HIS SIX GOLDEN DXY TRADES RUN RUNG TO RUNG ON THIS LADDER (entry / SL / TP vs V1 bands):
  L 100.945 (band 100.929-100.952) SL 100.905 (next band down 100.893-100.916) TP 101.115 (band 101.104-101.127) · S 101.14 (above band 101.104-101.127) SL 101.20 (next band up 101.203-101.226) TP 100.845 (band 100.836-100.859)
  · L 100.845 (band 100.836-100.859) SL 100.77 (below band 100.780-100.803) TP 101.19 (band 101.163-101.186) · S 101.19 (band 101.163-101.186) SL 101.25 (above 101.203-101.226) TP 100.975 (band 100.969-100.992)
  · L 100.975 (band 100.969-100.992) SL 100.905 (band 100.893-100.916) TP 101.24 · S 101.235 (above 101.203-101.226) SL 101.33 (band 101.312-101.335) TP 100.68 (band 100.674-100.697).
  => corrected E3 spec in his own trades: entry at a liquidity rung (LQZ / "LMV rung") near edge, SL at the adjacent ladder step (ladder-steps rule), ONE TP at an opposing rung several steps away (Law-14 opposing-rung walk). E3 is price engineering on the V1 ladder + E1 zones + E2 day shapes.
- CONSEQUENCE: E1-V1 row = harvest V1's order blocks + liquidity bands as data by running the sealed file (never editing it), with a history length that keeps the band count under V1's 60 cap (IDE default window; verify), per timeframe (4H / 1H / 30m / 15m) for the multi-timeframe zone map.

## THE APPROVED-RENDER E1 RECIPE (read first-hand 2026-11-26: /home/user/inputs/handover/.../02_SUPERSEDED_READ_ONLY/e1_run.py, 1072 lines of Python; its render of DXY week 2026-11-09 is the one the operator judged
## "THESE 6 ARE CORRECT ... 3 4 AND 5 NEED REFINEMENT (too wide)". It was shelved only because it used v4.5.2 text for the placeholders - which the operator has since admitted (L-33). It is the record of what produces zones he accepts.)
- Pillar 1 (:162-186): weekly + last 3 daily pivot sets (classic / fib / camarilla) are SEEDS; pivots of historical weeks (last 4 months) overlapping the current range are LEGACY support only (+0.5 where they coincide within 3 pips).
- Pillar 2 (:190-230): EMA + SMA 9/10/20/50/100/200 on 1H, 4H, D1 AND W1; sorted and clustered (span <= 0.15); ONE level per cluster at the weight-averaged price with Technical points 2 (3+ MAs) / 1 (2) / 0.5 (single); recapture of D1 EMA 50/100/200 within 3 sessions flags the level (+2 tally).
- Pillars 3/8 (:234-280): K ANCHORED ON THE BOUNDARY: K = DXY_spot / EURUSD_spot^-0.576 (TradingView closes at the boundary; "the canon holds the other components at CURRENT spot"); tier by USD notional (EUR notional x spot): 1 >= 1.5bn (band 0.07), 2 >= 0.85bn (0.10), 3 below (0.15; only via Step 9.8 structural override);
  other component pairs (>= $500M): DXY_spot x (strike / spot_j)^weight_j.
- Pillar 5 (:304-477): swing low/high = D1 extreme vs 2 bars each side, wick >= 0.15, close position >= / <= 0.5 -> "Liquidity Sweep Target" / "Supply Ceiling Target" struct 2, bonus 1.0 (2.0 + confluent if inside a D1 order block of its type);
  D1 order blocks = base of 1-3 consecutive large-bodied (body >= 50% of range) candles at a 3-bar extreme followed within 5 days by >= 1.0 with the base intact; LSZ = [low, low+0.10] / [high-0.10, high], ACTIVE within 0.30 of spot;
  magnets: 2+ same-side swings within 0.05 (wick-weighted price; bonus 1.5, 2.0 for 3+), role reversal (low vs high within 0.05; 2.0), inside an order block -> institutional magnet 2.0; all struct 2;
  4H zones: single candle (width <= 0.40) at a local extreme (2 bars each side) whose close 18 bars later is >= 0.5 away with the candle intact; BoM if the prior 5-bar move opposed it; touches counted; dropped if it overlaps an opposite 4H zone or had no interaction for 3 weeks; its TOP and BOTTOM edges are levels with struct 1;
  minor swings D1 + 4H (wick >= 0.08, close 0.4 / 0.6) struct 0.5; anchors (struct 2): close, high, low of each of the last 5 days, prior weekly close / high / low, HWC/LWC, structural memory.
- Pillar 6 (:485-510): fibs 23.6/38.2/50/61.8 of the prior week AND of the major swing of the last 63 daily bars (Technical >= 1 within 10 pips); round numbers .00/.50/.25/.75 across the arena.
- SCORE of a candidate price p (:522-575): Technical = best of (pivot within 3 pips 2 / within 10 pips 1; MA cluster within 10 pips -> its points; non-round P6 fib within 10 pips -> at least 1) (+0.5 legacy, capped 2); Options = 2 if a tier-1 strike within max(0.10, band) else 1 for tier 2/overridden tier 3;
  Analyst = 2 if two tier-1 sources within 3 pips else 1; Structural = for each P5 level within 10 pips: its weight if within 3 pips, else 1 if its weight is 2, else its weight (max, capped 2); bonus = max bonus of P5 levels within 10 pips (cap 2);
  Psychological = round_psych(p): p itself within 3 pips of .00 / .50 -> 2, of .25 / .75 -> 1. base = sum. A level is not its own technical match is NOT needed here because only coincidences across pillars lift the score.
- ASSEMBLY (:742-773): seeds = every current level (legacy excluded; tier-3 strikes only with the Step 9.8 override); each seed scored; ordered by (-base, -number of pillars, -option tally, distance to spot); a seed with base < 4 stops the list;
  a seed is taken only if >= 0.15 from every seed already taken ("centres sit at least 0.15 apart, so a zone can never chain into its neighbour"); members = scored levels within +-0.075; zone = [min(members, seed-0.03), max(members, seed+0.03)].
- ZONE MECHANICS (:590-656, canon P533:1145-1161): on the 4H bars of the last 90 days a VISIT = a run of consecutive bars overlapping the zone; STRONG REACTION = price left on the holding side and travelled >= 0.50 before returning; counter Virgin 0 / Active 1-2 / Depleted 3+;
  BoM if the move leaving the zone after its latest visit ran >= 1.00 (no visits: BoM if a 4H BoM / sweep target is a member), else MoM; sweep status Swept / Partial / Unswept; Engine 3 status: BoM -> ENTRY-PRIMARY (TP-TARGET at 3+ reactions); MoM with 0 or 3+ reactions -> REJECT;
  MoM 1-2 reactions -> ENTRY-CONDITIONAL if all four exceptions (>= 1 reaction, trend-aligned, key S/R confluence from pillars 1/4/6, no opposing liquidity within 0.25 beyond the far edge) else TP-TARGET; 4H MoM member -> ENTRY-SCALP-ONLY; ladder step = MoM, trend-aligned, 1-2 reactions.
  Trend = D1 close vs EMA50 vs EMA200 (up / down / range). Step 9.9: +1 if the 12 4H bars before the first visit ranged <= 0.50 (post-consolidation).
- PILLAR 9 (:790-842): type: live wall >= $1.0bn + 3 pillars + confluent -> Hard Wall (base ZFP 10); live wall >= $0.5bn + 2 pillars -> Standard Wall (22); expired wall >= $0.85bn -> Post-Expiry Ghost (20 / 30 / 40 by pillar count); 3+ pillars -> Soft Wall (30); 2 pillars or any wall -> Soft Wall (40); else One-Touch (60).
  Modifiers for zones within half the prior week's range of spot: macro catalyst +15, price approaching with momentum (3-session move >= 0.3 toward it) +15, cross-pair confirmation +15; EMA200 cross in the last 5 sessions +15; magnet within 0.20 of an edge +10. ZFP = min(95, base + mods).
  Regime points 2 if ZFP < 20, 1 if 20-50, 0 if > 50. SCORE = base + regime (+1 post-consolidation). Measured move when ZFP > 45 (:659-680).
- FINAL (:850-874): zones with score >= 6 (MODERATE+); degree table; names: EQUILIBRIUM = the zone containing spot; above spot the highest = RESISTANCE CEILING, others UPPER RESISTANCE; below spot the nearest = MID-RANGE SUPPORT, others KEY SUPPORT BAND;
  POI Tier 1 if a member is a 4H BoM edge 0X-1X; intra-zone levels = round / fib / close levels inside; Key Support Band core = D1 bodies of days wholly inside it; RANK by (-score, -pillars, distance to spot); the first SIX are drawn (operator: "six zones at most").
- What the operator then asked of that render: zones 3, 4, 5 narrower (cores 101.97-102.01 and 101.49-101.53 = the tight level cluster; zone 3 "from where price traded"); labels must carry name, degree and ZFP. In this session he added L-38 (candle zones wick to wick) and L-39 (pressure zone = candle structure + level cluster joined, both visible).
