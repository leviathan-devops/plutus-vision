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
