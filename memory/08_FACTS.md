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

## MULTI-TIMEFRAME V1 HARVEST AT THE GOLDEN-WEEK ANCHOR (e1_tool/e1_v1.py, 400 closed bars per timeframe, anchor Mon 2026-07-06 06:00Z; cache e1_tool/cache/v1/) - his entries sit on these zones
- 4H: supply OB 101.378-101.444 (his 4H BoM supply; Step 0f candle 101.316-101.43); liquidity bands incl. 101.245-101.305 (his upper green band / white 101.24), 101.067-101.127, 100.957-101.017, 100.498-100.558 (his lower band, prior-week low).
- 1H: supply OBs 101.658-101.746, 101.396-101.444; demand OB 100.603-100.746 (his "1H BoM"); 27 liquidity bands = the rung ladder (15/16 of his rungs).
- 30m: demand OB 100.825-100.846 from Jul 3 18:00 (his "1H (Unmitigated) | MoM" 100.82-100.845; his Tue LONG entry 100.845 = its TOP edge, TS-1), demand 100.704-100.783, supply 101.128-101.205 (his Mon SHORT entry 101.14 = its bottom edge + 1 pip, F1-A; SL 101.20 = its top), supply 101.357-101.402, 101.701-101.746.
- 15m: demand OB 100.929-100.950 from Jul 6 04:15 (his Mon LONG entry 100.945; SL 100.905 = the 15m liquidity band 100.905-100.916 below it), 100.825-100.846, 100.779-100.814, 100.704-100.734, 100.654-100.723 (bottom 100.654 = the bottom of his 1H BoM demand box).
=> Law 3 / TS-1 confirmed on his own trades: entry = near edge of a lower-timeframe V1 order block (LONG top edge, SHORT bottom edge + 1 pip), SL = far side / adjacent liquidity band, TP = opposing band several steps away. E3 must be built on this harvest.
- e1_data: the anchor is now Monday 02:00 New York (boundary_ms); daily()/weekly() return completed days/weeks only; week_start_ms / week_end_ms added. Spot at the golden anchor = 101.025 (Friday close was 100.878).

## HIS GOLDEN TRADES vs THE SEALED V1's 4H LIQUIDITY BANDS (measured 2026-11-26 late; e1_v1.harvest_all '240'; the 4H bands are the "4H Liquidity Shields" of GS Law 4 and his hand-drawn green bands, L-21)
- DXY 4H bands at the golden anchor: 100.254-100.314, 100.498-100.558, 100.957-101.017, 101.067-101.127, 101.245-101.305, 101.372-101.432. EURUSD: 1.13686-1.13756, 1.1381-1.1388, 1.14108-1.14178, 1.14269-1.14339, 1.14658-1.14728.
  GBPUSD: 1.32932-1.33022, 1.33155-1.33245, 1.33406-1.33496, 1.33583-1.33673, 1.33715-1.33805, 1.33976-1.34066, 1.34145-1.34235, 1.34386-1.34476, 1.3454-1.3463.
- Canon SL rule (b) "1-2 pips INSIDE the CLOSE edge of the NEXT STEP" (E3C:252-256) fits his stops LITERALLY when the steps are liquidity bands (1H rung or 4H band):
  DXY #4 Wed S 101.19 SL 101.25 = 0.5 pip inside the close edge 101.245 of the 4H band; #8 Fri L SL 100.545 = 1.3 pips inside the close edge 100.558 of the 4H band; #1 Mon L SL 100.905 and #5 Wed L SL 100.905 = 1.1 pips inside the
  close edge 100.916 of the 1H rung 100.893-100.916 (the nearer rung 100.929-100.952 is under 4 pips away: skipped); #6 Wed S 101.235 SL 101.33 = rule (a) "3 pips outside the far edge of the current step" on the 4H band (101.305 + 0.03);
  EURUSD #6 Wed L 1.13953 SL 1.13868 = 1.2 pips inside the close edge 1.1388 of the 4H band; #3 Tue L 100.845 SL 100.77 = 1 pip outside the back edge of the 1H rung 100.780-100.803 (the exception).
- TPs / entries on the 4H bands: DXY #5 Wed RWL L TP 101.24 = near edge 101.245 of the 4H band minus 0.5 pip; #6 Wed BS S entry 101.235 = 1 pip before that band (Law 27: TP of the RWL = entry of the BS); #8 Fri L TP 100.94 = 1.7 pips before the 4H band 100.957;
  EURUSD #4 Wed SS L TP 1.14276 and #5 Wed RWL S entry 1.14277 = near edge 1.14269 of the 4H band (+0.7 pip); #1 Mon S TP 1.14103 / #2 Mon L entry 1.14106 = the bottom of the 4H band 1.14108-1.14178.
- THE TRANSITION DAY (6.4.2 "consolidation ends in price retesting opposing liquidity"): the retest (RWL) ends at the liquidity band in front of the unmitigated BoM zone beyond the range bound, band timeframe = zone timeframe:
  DXY: 4H BoM supply 101.316-101.43 -> 4H band 101.245-101.305 -> RWL TP 101.24, BS short 101.235. EURUSD: 1H BoM demand 1.13815-1.13886 -> 1H rung 1.13902-1.1393 ("deep shield") -> RWL TP 1.1395, BS long 1.13953 (spec F1-C: 1.13935).
- THE STOP MODEL THAT FITS ALL OF HIS GOLDEN DXY STOPS (hand-checked 2026-11-26 night; NOT yet in code - e3_trades._stops still uses "1 pip outside the back edge of the next 1H rung"):
  canon rule (b) "1-2 pips INSIDE the CLOSE edge of the next rung RELEVANT zone" (E3C:247-256) + FA 2.1 "Thin liquidity zones are NEVER allowed as entry or SL zones ... each thin zone counts as 2 thin zones [inside a 4H pool]" + 8R.6 buffers
  ("THICK = 2 thick or 2-3 thin zones"): the relevant step = the first THICK liquidity zone beyond the entry (a V1 4H band) or the SECOND of two thin ones (V1 1H rungs), whichever comes first; stop = 1 pip inside its close edge.
  Check: #2 Mon S 101.14 -> 2nd rung 101.203-101.226 -> 101.213 (his 101.20); #4 Wed S 101.19 -> 4H band 101.245 -> 101.255 (101.25); #5 Wed L 100.975 -> 2nd rung 100.893-100.916 -> 100.906 (100.905); #6 Wed S 101.235 -> 2nd rung 101.312-101.335 -> 101.322 (101.33);
  #7 Thu S 100.975 -> 4H band 101.067 -> 101.077 (101.09); #8 Fri L 100.615 -> 4H band 100.558 -> 100.548 (100.545); #3 Tue L 100.845 -> 2nd rung 100.730-100.753 -> 100.743 (100.77, 2.7 pips: the weakest fit).
  RISK when coding it: wider stops lower the RRR; DX4 (RWL long 100.990 / 100.906 / 101.235) lands at 2.92 - needs the spec's hair-miss repair (RWL_HAIR_MISS_RRR_DELTA 0.1, F1-D inset) or the deeper entry candidate; re-check every golden number after the change.
- STOP MODEL REFINED (hand-checked on all 7 of his golden DXY stops, 2026-11-26): current step = the SMALLEST liquidity step containing the entry (V1 1H rung or V1 4H band; none if the entry sits between rungs);
  the shield = the first THICK step (a V1 4H band) or the SECOND thin 1H rung beyond the current step, whichever is nearer (FA 2.1 'Thin liquidity zones are NEVER allowed as entry or SL zones ... each thin zone counts
  as 2 thin zones' inside a 4H pool); SL = 1 pip INSIDE the shield's close edge (E3C:255 rule (b)). Distances to his stops: #2 1.3, #3 2.7, #4 0.5, #5 0.1, #6 2.9 (rule (a) on the 4H band 0.5), #7 1.3, #8 0.3 pips.

## HIS 23 GOLDEN STOPS ON THREE PAIRS vs E1 STRUCTURES (measured 2026-11-26 with scratchpad stops.py = for each trade: structures holding the entry, structure edges within 2.5 pips of the SL; bug locator)
- Stop distances: DXY 4.0 / 6.0 / 7.5 / 6.0 / 7.0 / 9.5 / 11.5 / 7.0 pips; EURUSD 8.6 / 6.7 / 6.4 / 4.8 / 4.8 / 8.5 / 5.0 / 7.1; GBPUSD 10.7 / 14.1 / 13.1 / 10.7 / 11.4 / 7.9 / 10.6. (E3C:279-293 golden SL 4-9.5 pips fits DXY + EURUSD; GBPUSD runs 8-14.)
- DXY + EURUSD stops sit on an edge of a liquidity band of SOME timeframe (15m / 30m / 1H / 4H) or of the order block above / below the entry:
  DXY #1 = 15m band 100.905-100.916 bottom (0.0); #2 = top of the 30m supply OB he entered (101.205, -0.5) = 1H rung bottom 101.203 (-0.3); #3 = bottom of the 15m demand OB 100.779-100.814 (-0.9); #4 = 4H band bottom 101.245 (+0.5);
  #5 = same 15m band as #1; #6 = 1H rung top (-0.5); #8 = bottom of the 15m BoM demand 100.546-100.663 (-0.1) = 4H band top 100.558 (-1.3).
  EURUSD #1 = top of the 30m / 15m supply OB 1.1441 (-0.2); #3 = bottom of the next 15m supply OB 1.14505 (0.0); #4 = inside the 15m band (bot +0.7); #5 = bottom of the 30m supply OB above (-0.2) = 4H band top -1.4;
  #6 = 4H band top 1.1388 (-1.2); #7 = 4H band top 1.14178 (+0.5) = 1H rung top (+0.5); #8 = 4H band bottom 1.14658 (-0.9).
- GBPUSD stops match almost no structure edge within 2.5 pips (#1 = bottom of an IP zone -0.1; #2 = 4H band top +0.9; #4 = 15m band bottom 0.0; #3, #5 none): on GBPUSD the tool's ladder is too sparse / different from what he used.
  Tool vs his GBPUSD Monday long: entry 1.33333 identical, tool stop 25 pips (rule (b) on the 4H band) vs his 10.7 -> RRR 2.39 -> rejected. E2 range 1.33333-1.33941 = his Monday pair L 1.33331 -> 1.33941, S 1.33934 -> 1.33347 to the pip.
- Entries: every DXY / EURUSD entry lies inside a 15m / 30m / 1H band or a 15m / 30m order block (scalp-stack structure); GBPUSD #1 / #3 = top edge of the 1H MoM demand 1.33082-1.33333 (TS-1), #2 = bottom edge of the IP / supply 1.33933, #5 inside the V1 4H supply OB.

## THE FIBONACCI SPIDERWEB IS HOW HIS TRADES ARE BUILT (read first-hand 2026-11-26 late: /home/user/inputs/4d1ca379-Fibonacci_Spiderwebs.pdf, 4 pages; GS Law 5 lines 81-97) - NOT YET IN CODE
Source text (operator's own document): 1. Map W/D BoM S/D zones. 2. Fib-anchor price action on the 4H: same anchors as Fib rockets, swing low + swing high, 'Deepest + Most Recent', 'BoM Anchors - NOT subsequent market structure HL/LH'.
3. BS / WL SWING moves: 1H price action; 'London Session open position = Trade Setup Anchor (use this confirm direction as well. Strong pressure = session move)'; 'Nearest Fib level = entry'; '1-2 Fib levels back = SL';
   'Fib wormhole anchor of entry level = TP (0.618 -> 1.618, etc)'; 'If price has been consolidating/SS for 1+ days, BS is likely imminent. If 4+ SS trades have been presented over 1-2 days - NY session = BS begins'; 'Target 2 or 3 levels for swings from a SS anchor point'.
4. SS / Recovery SCALP moves: 15m price action; 'Anchor to nearest NON-SURGE swing high/swing low ... the fib anchors are inside a 15m consolidation range. NOT anchored to previous BS/WL anchors'; 'Trade with the trend. Direction = Trend';
   London Session open position = Trade Setup Anchor; nearest Fib level = entry with 'a 0.5-1 pip buffer in front of the entry ... MANDATORY'; '1-2 Fib levels back = SL', 'Add a 1 pip buffer to the SL from the exact fib level. 2-3 is safer';
   'Fib wormhole anchor of entry level = TP (0.382 -> 1.382, etc)' with 'a 1.5-2 pip buffer in front of the TP or you will miss it. MANDATORY ... If you skip this you will miss 60% of TPs'.
5. Price in the MIDDLE OF A SWING at London open: 'Default to SDL mechanics - spiderweb is secondary'; 30m; 'ANCHOR THE NEAREST SWING HIGH/LOW FROM THE SAME TRADING DAY'; map the 30m SDL entry to the corresponding fib level; wormhole = TP.
'Spiderwebs can pierce UM 4H BoM zones.' 'AFTER 2 STRONG PIERCING SWING MOVES - EXPECT 1-2 FULL DAYS OF HTF CONSOLIDATION ... the chain is WL -> RWL -> SWING SCALPS -> BS/WLS/PBS'.
WORKED AGAINST HIS GOLDEN DXY TRADES (my arithmetic; R = range height between two Earth points, retracement r measured from the range end the trade moves away from; TP = entry +- R exactly = the wormhole r -> 1 + r):
- #1 Mon L 100.945 / 100.905 / 101.115: range 100.840-101.010 (R 17.0): entry 0.618, SL 0.382 (one level back), TP 1.618 - all three to the pip.
- #2 Mon S 101.14 / 101.20 / 100.845: range 100.908-101.203 (R 29.5): entry 0.786, SL 1.0 = range high 101.203 (= the 1H rung bottom), TP 1.786.
- #3 Tue L 100.845 / 100.77 / 101.19: range 100.771-101.116 (R 34.5; hi = #1's TP rung 101.115): entry 0.786, SL 1.0 = range low, TP 1.786.
- #4 Wed S 101.19 / 101.25 / 100.975: range 101.0825-101.2975 (R 21.5; lo = rung 101.09, hi = band top 101.29): entry 0.5, SL 0.786 (two levels back), TP 1.5.
- #5 Wed L 100.975 / 100.905 / 101.24: range 100.8425-101.1075 (R 26.5; lo = rung 100.845): entry 0.5, SL 0.786 (0.6 pip off his), TP 1.5.
- #6 Wed S 101.235 / 101.33 / 100.68: range 100.892-101.447 (R 55.5; hi = his 4H BoM supply top 101.44): entry 0.618, SL 0.786, TP 1.618.
- #8 Fri L 100.615 / 100.545 / 100.94: range 100.5455-100.8705 (R 32.5; lo = 15m BoM demand bottom / 4H band top): entry 0.786, SL 1.0 = range low, TP 1.786.
So: entry at retracement 0.5 / 0.618 / 0.786 of a range anchored on two Earth points, SL 1-2 Fib levels back (0.168-0.286 R -> RRR 3.5-6, his measured 4-6), TP exactly one range height from the entry. My E3 reproduces his numbers only because
those Fib levels coincide with rungs / zone edges on that week; on other weeks my stops (ladder steps) and TPs (far bound) are NOT his construction. THIS IS THE UNBUILT LAYER (goal prompt Law 5, anti-pattern A9 'Air (spiderweb)', coverage row E2-AIR / E3-P3).
BUILD NEXT (canon order): (1) spider anchors: 4H swing low / high (deepest + most recent, BoM anchors) for BS / WL swings; 15m consolidation-range swing high / low (non-surge) for SS / recovery scalps; same-day 30m swing for mid-swing days;
(2) the day's London-open position = the setup anchor (Monday = the forecast anchor itself; later days = the E2 path's day-open position, E3C WorkingDayMap dayOpenSpot); (3) entry = nearest Fib level in the trend direction (0.5-1 pip in front),
SL = 1-2 levels back + 1 pip, TP = wormhole - 1.5 to 2 pips; (4) check all 23 golden trades (DXY above; do EURUSD / GBPUSD the same way) before touching other weeks.
CORRECTION (same night, after fitting all 23 trades): the per-trade ranges above are NOT uniquely identified - with rungs / zone edges every few pips and seven Fib levels, several (range, level) pairs fit each trade within a pip. What IS solid:
(a) HIS OWN GRIDS in context_management/oracle/golden_week.json: EURUSD 0 = 1.13925 (Wednesday's low), 1 = 1.14315 (swing high before Wednesday's drop); GBPUSD 0 = 1.33225, 1 = 1.33703 - i.e. the grid is drawn on the RETEST LEG of the week (rule 5: nearest swing high / low of the same trading day), and against them:
    EURUSD #4 L 1.14012 = 0.236 (1.14017); #7 rocket L 1.14233 = 0.786 (1.14231), its SL 1.14183 = 0.618 (1.14166) + 1.7; #6 / #7 TP 1.14544 = 1.618 (1.14556) - 1.2; #8 Fri S 1.14578 = 1.618 + 2.2, SL 1.14649 = 1.786 (1.14621) + 2.8; #5 Wed S: SL 1.14325 = level 1 + 1.0, TP 1.13950 = level 0 + 2.5;
    GBPUSD #3 L 1.3333 = 0.236 (1.33338), SL 1.33199 = level 0 - 2.6; #4 rocket: SL 1.33522 = 0.618 (1.33521); #5 Thu S: SL 1.3436 = 2.382 (1.34364), TP 1.33882 = 1.382 (1.33886); #6 TP 1.34485 = 2.618 (1.34476); #7 Fri S 1.34481 = 2.618, SL 1.34587 = 2.786 (1.34557) + 3.0, TP 1.34021 = 1.618 (1.33998) + 2.3.
(b) the buffers of the PDF show in his numbers: stops 1-3 pips beyond the Fib level, TPs 0-2.5 pips in front of it.
(c) SL / R ratios of the 23 trades lie between 0.12 and 0.39 (RRR 2.5-8).
So the build is: the Fib grid on the E2-forecast retest leg (0 = the retest extreme = opposing liquidity, 1 = the swing before it) for the breakout family - entry 0.236 (and the deep entry near 0), rocket 0.786 with SL 0.618, TP 1.618 (the BoM zone 'sits at the 1.382-1.618 extension'), reversal at 1.618 / 2.618 with SL one level on + 2-3 pips and TP one range back; plus the PDF's buffers everywhere.

## VIRGIN 1H MoM ZONES AND HIS OWN ENTRIES (checked 2026-11-26 night, golden_week.json zone labels vs his trades) - why no 'virgin MoM = reject' gate stands on swing scalps
His own chart labels (the sealed V1's): GBPUSD demand '1H (Unmitigated) | MoM' 1.33081-1.3334 -> his #1 long 1.3333 stands on it (rung 1.33335); EURUSD demand '1H (Unmitigated) | MoM' 1.13999-1.14144 -> his #2 long ~1.1410 (rung 1.1411);
DXY demand '1H (Unmitigated) | MoM' 100.822-100.85 -> his #3 long 100.845 (rung 100.845). So he DOES take swing scalps at unmitigated 1H MoM zones - at the liquidity rung in them (F1-C).
Canon lines that say otherwise for ENTRY zones in general: P533:1157 / 2218 ('MoM (virgin) | ENTRY-REJECT'), E3C 8.14 rule 6 ('no entry at MoM unless ALL 4 exceptions'), E3C:1053 VIRGIN_MOM_DEATH_ZONE ('on counter-trend').
Measured on the 16 locator maps: setups on virgin 1H MoM zones = 6 TP / 6 stops; 'counter-trend = against the E2 storyline' would delete GBPUSD golden #2 and keep 5 of the 6 losers. NOT BUILT as a gate; the open question is what separates
his MoM entries (a rung inside the zone, range day) from the losers (zone edge / 30m block, no rung: DXY Oct 5 101.926, EURUSD Oct 5 1.12491 - both pierced to the BoM zone right behind them, P533:1161 priority rule).

## PINEBOX LABEL QUIRKS (measured 2026-11-27, ledger 98b / 99b / 100b / 102b)
- label.style_none: the text STARTS at the label's x (it is not centred on it). label.style_label_right: drawn to the RIGHT of its point as well. To make a label end at a time, put its point the text's width before it.
- The x axis is bar-indexed: the weekend takes no width, so offsets must be counted in 1H bars, not clock hours. size.small text = about 6.5 px per character = 1.65 one-hour bars on the two-week 1H frame of tools/s3frames.

## SESSION FACTS 2026-11-27 (after the 70% handover; checkpoint '80% functional - DXY specific' = code aa8d689, commit 0d4ad41)
### Operator rulings of the day (verbatim in memory/12 M-58 .. M-60; rulings L-46 .. L-56 in memory/04)
- STOPS (L-50): good trade (mechanics aligned, RR there) takes the WIDER stop - never skip it for a few pips; 'potentially even set a better entry'. GBP/USD: the liquidity shield is often OUTSIDE the S/D zone (candles touch the liquidity zone above / below and react there); EUR/USD: the liquidity sits INSIDE the S/D zone (price mitigates inside it). Canon line for WHEN: P533:506 'SL correction/reentry exception: When trying to catch a CORRECTION/REVERSAL - ALWAYS make sure SL is 1-2 pips INSIDE THE NEXT ZONE ... Standard SL rules (outside the zone) apply for trend-following entries.' E3C ZR-6B (conf >= 0.6 RR-tight, else next-rung) and the E3C 12.2 golden envelope 9.5 pips conflict with it; the operator's ruling wins over the envelope.
- Measured on his golden stops: DXY 6 of 7 = inside the next zone (B), #6 (Wed breakdown short, trend-following) = outside (A); EUR/USD golden stops = 'outside the entry zone' (rule (a) matched them within 0.2-0.4 pips; the next-S/D-zone reading was 2-6.5 pips off and tighter) -> EU_INSIDE = False.
- NO DUPLICATES (L-52): one unique trade per observable move; a pending order is not copy-pasted per day; one trade = price hits the entry and then the TP. Explicitly banned.
- E2 DRAWING (L-51): box + line, each swing drawn inside a SWING SCALPS box; the line = the price action candle by candle as a line chart; if the candles do not match the line, the line is wrong.
- DAILY UPDATE (L-47 / L-53): orders and the E2 line from each day's open; zones re-updated at each London open, new zones added without duplicates; nothing from after the update instant.
- DATA (L-54): Forex Factory blocked (Cloudflare challenge to curl; a headless-browser load was REFUSED by the session's permission check; Muse Spark 1.3 via OpenCode Go has NO web search - answers 'NO_WEB_SEARCH') -> Protocol F = NO DATA, do not raise it again.
- LIBRARY (L-48 / L-55): /home/user/inputs/trades/WINNING_TRADE_LIBARARY (zip of 64 entries, complete): ~17 pair-weeks = GBPUSD Feb 2 - Apr 24 2026 (12 weeks), EURUSD Apr 13-17 / Jul 6-10 / Jul 13-17, DXY Apr 13-24 (1H) / Jul 6-10; evidence/answers_m58/Q4_library_inventory.md. These weeks are the optimisation / oracle set; the old S5 blind reserve (Feb 2 - Mar 23) is inside it (D-129) - S5 blind weeks must come from outside the library and outside every week run.
- M-60: checkpoint '80% functional - DXY specific'; DXY golden first half + trades accurate, DXY E2 Wed-Fri broken; GBPUSD poor; EURUSD missing from the report -> every report shows ALL THREE pairs, the WHOLE week in one fitted screenshot each.
### Data sources built (sidecar/protocols.py -> sidecar/out/protocols/<monday>.json; raw cached in sidecar/raw/protocols/)
- D Treasury: https://www.treasurydirect.gov/TA_WS/securities/search?startDate=..&endDate=..&dateFieldName=competitiveAuctionCloseDate&format=json (dateFieldName=auctionDate gives HTTP 500). Latest FIXED-rate (floatingRate != Yes) 2Y / 5Y / 10Y note (originalSecurityTerm) closed before the anchor (close date + time ET); trigger bid-to-cover >= 2.6 (P452:1443). The week's coupon auctions announced BEFORE the Monday (announcementDate < monday) with close time; their results are post-anchor and not stored.
- E NY Fed ON RRP: https://markets.newyorkfed.org/api/rp/reverserepo/propositions/search.json?startDate=..&endDate=.. (host allowed by the operator 2026-11-27); last two operations dated before the Monday, trigger at a USD 50bn contraction (P452:1444). No week of 2026 triggers.
- G EIA: weekly U.S. crude stocks WCESTUS1 https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=WCESTUS1&f=W (week-ending Fridays, thousand barrels); release Wednesday 10:30 ET or the alternate date of https://www.eia.gov/petroleum/supply/weekly/schedule.php (holiday weeks: Thursday 12:00); only prints released before the anchor; deviation = change - previous change, trigger |deviation| >= 5M (P452:1446).
- Shown in the E2 report block 'VOLATILITY TRIGGERS (as of the anchor)' and each day's Triggers line.
### Daily anchoring as built (plutus.daily_anchor; decisions D-131 .. D-138)
- Monday = the week anchor. Each later day: at the TRADING-DAY OPEN (17:00 NY the evening before; London-open anchoring loses every Asian-session fill, e.g. his golden Friday long filled 02:15 UTC): a 1H close beyond a Decision Zone of the chain in force since its anchor activates its alternative (6.6 Step 4); orders of the day confirmed (order block not closed through - one-time use; price on the order's side); a still-pending / open order is not copied (L-52) - a pending swing-scalp order rests into the next PURE range day.
- At the LONDON OPEN (02:00 NY): Engine 1 rebuilt as of it (e1_data.ASOF; V1 harvest cached per instant e1_tool/cache/v1s/PAIR_TF_MONDAY_<ms>.json): zones formed since the week anchor added where no zone of the family is drawn; after a failure the LINE and DAY BOXES follow a chain re-anchored on the rebuilt map (REANCHOR_DRAW, D-138); the ORDERS stay with the chain in force (REANCHOR = False, D-137: re-anchored orders cost winners).
- Rejected: re-running Engine 2 from scratch each morning (the 6.10 +1 day is re-applied every morning -> the golden breakout leaves the week); London-open order confirmation (loses Asian fills); P533:506 stops without the ruling (no gain while the 9.5 envelope filtered them).
- Leak check part 3 (tools/leak_check.py): each day's trading-day-open part identical with the bars cut there; its London-open part identical with the bars cut at the London open. pre-commit runs it on golden DXY + EURUSD.
- Session line (L-51 first version, e2_chain._session_path + plutus._day_line): canon P452 6.6 SESSION-LEVEL SHAPE MAPPING RULES - 1 Asia SS inside the prior day's range (flat), 2 London often triggers BS (swing to a bound, 02:00-08:00 NY; on a range day toward the bound NEARER the day's price, P533 2.3 / D-41), 3 NY pre-cut 08:00-10:00 pinned to the day's largest strike inside the range, 4 10:01 Spring Release, 5 NY post-cut to the next zone (the other bound) by 17:00, 6 day-over-day continuity, 7 Friday expiry effect.
### Locator numbers (12 count maps; my own fill simulation - bug locator only, never a verdict)
- weekly 91 orders / 34 TP / 22 SL / 33 unfilled -> daily + confirmation 70 / 31 / 10 -> + no copies 46 / 28 / 10 / 7 -> + L-50 stops 43 / 27 / 8 / 6 -> + zone update + session line (checkpoint) 44 / 25 / 8 / 9.
### Tooling facts
- Pinebox: a render while another process uses the station (V1 harvests) times out (CDP_TIMEOUT) and s3frames still writes the PREVIOUS pass's chart -> never render in parallel; check the 'pb ide' box count before citing a frame. After a worker restart Pinebox is dead: pinebox up --session plutus-main --adapter xvfb --pair DXY --tf 1H.
- tools/e1render honours PLUTUS_FLAGS (e.g. --weekly). Generated Pine of a frame lands in e1_tool/out/E1_PAIR_MONDAY.pine.
- Running python on HEAD after git stash rewrites tracked .pyc files and blocks git stash pop: use PYTHONDONTWRITEBYTECODE=1 for baseline runs.
### M-61 V3 facts (2026-11-27)
- His golden EURUSD #1 (Mon S 1.14322 / 1.14408 / 1.14103) traded only in the Asian session: price 1.1432-1.1441 from Sun 21:00 to Mon 05:30 UTC, never back at 1.14322 after the 06:00 UTC anchor before its TP (Mon 10:00) - outside the map's reach by the temporal anchor.
- His golden trades as Law-27 chains: EURUSD #1 TP 1.14103 -> #2 E 1.14106 -> TP 1.14442 -> #3 E 1.14441 -> TP 1.14004 -> #4 E 1.14012 -> TP 1.14276 -> #5 E 1.14277 -> TP 1.1395 -> #6 E 1.13953 -> TP 1.14544 -> #8 E 1.14578; DXY #1 TP 101.115 -> #2 E 101.14 -> TP 100.845 -> #3 E 100.845 -> TP 101.19 -> #4 E 101.19 -> TP 100.975 -> #5 E 100.975 -> TP 101.24 -> #6 E 101.235; GBPUSD #1 TP 1.33941 -> #2 E 1.33934 -> TP 1.33347 -> #3 E 1.3333 -> TP 1.34246 -> #5 E 1.34246.
- EURUSD Monday ceiling structure (golden): 1H supply BoM 1.14375-1.14421 (origin Jul 3 17:00 UTC, the mirror candle of his DXY 1H MoM 100.825-100.851), the pressure zone UPPER RESISTANCE 1.14444-1.14533 above it; V1 1H rungs 1.14387-1.14415 and 1.14484-1.14512; EURUSD pierced the 1H supply to 1.14454 (Mon 18:45 UTC) and turned at the pressure zone.
- (2026-11-27) Chat file upload (SendUserFile): a 450 MiB file was refused ('exceeds the upload limit'); 236 MB and 304 MB files passed - split deliveries at <= 225 MiB. GitHub: files must stay under 100 MiB (95 MiB pieces accepted with a 'larger than 50 MB' warning); the repo leviathan-devops/plutus-vision is PUBLIC.
