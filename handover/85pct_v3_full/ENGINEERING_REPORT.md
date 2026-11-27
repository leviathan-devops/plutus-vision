# PLUTUS VISION - ENGINEERING REPORT
## From the "70% functional" package (33f747fc, 2026-11-27 13:49 UTC) to "85% functional - DXY + GU (V3)" and this handover

This report covers everything done since the previous package, in order: every operator message, every answer, every build step and every rejected trial. For each step it gives the code, the canon line it rests on, what was measured, and what was seen on the chart.

It is written so that another agent can take over, reproduce every state and audit every claim. Nothing is summarised away: where a section is short, the full text is in the file it names.

---

## 0. How to audit this report

### Sources of record

Every statement below points to at least one of these:

| Source | What it holds |
|---|---|
| `handover/85pct_v3_full/COMMITS_SINCE_70PCT.md` | the 50+ commits since the 70% package, with full messages and the files each changed |
| `memory/03_DECISION_CHAIN.md` | rows D-129 .. D-145: what, canon citation, code location |
| `memory/07_EVIDENCE_LEDGER.md` | rows 107 .. 115b: the expectation written BEFORE each render, then what the opened frame showed |
| `memory/12_OPERATOR_VERBATIM.md` | M-58 .. M-63, verbatim |
| `memory/04_OPERATOR_RULINGS_LIVE.md` | rulings L-46 .. L-59 |
| `memory/06_LESSONS.md` | lessons L-50x .. L-58x |
| `memory/08_FACTS.md` | "SESSION FACTS 2026-11-27" and "M-61 V3 facts" |
| `memory/05_JOURNAL.md` | every step and every rejected trial, chronological |
| `handover/85pct_v3_full/CODE_CHANGES_SINCE_70PCT.patch` + `CODE_MAP_SINCE_70PCT.md` | every code line changed since 70% |
| `handover/85pct_v3_full/VISUAL_CHECKPOINTS.md` | every frame, embedded |
| `handover/85pct_v3_full/locator_outputs/` | every locator output quoted here |

### Numbers

Numbers from my own scripts are **bug locators, never verdicts** (goal prompt A5). The only grades are the operator's:
- 70% at M-57;
- "80% functional - DXY specific" at M-60;
- DXY / GBPUSD "A-" and EURUSD "a solid C" at M-61;
- "Okay, great" at M-62.

### Abbreviations

| Abbreviation | Source |
|---|---|
| P533 | `canon/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md` |
| P452 | the v4.5.2 prompt (text where P533 says "unchanged") |
| E3C | `canon/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md` |
| FA | `canon/Toolset/Trident_Fractal_Architecture_FirstPrinciples_v2.3.md` |
| GS | `TTE_GOLDEN_STANDARD_COMPLETE_REFERENCE.md` (host bibles) |
| TL | the operator's `Trading Laws.pdf` (winning trade library, `Original_Training_Data/`; text extract in `canon_text_extracts/`) |
| E2X | the Part VI extract |

**Timezones:**
- times are UTC unless marked NY (New York);
- the Monday anchor = Monday 02:00 NY = 06:00 UTC in summer;
- the trading-day open = 17:00 NY of the previous day.

---

## 1. Where the 70% package left the build

From `handover/70pct_functional/00_START_HERE.md`:

**Tool.** One command, `e1_tool/plutus.py`, built Engine 1 (zones), Engine 2 (shape chain) and Engine 3 (orders) at the Monday London-open anchor and wrote one Pine v6 script on top of the sealed V1. Every order was a resting limit fixed at the Monday anchor and copied per day ("per-day repeats").

**Defects the operator named (M-57):**
1. "half of your trades are accurate but slightly too tight on the SL or slightly too early";
2. "the E2 shape chain line ... is ... a generalized watered down basic line".

**Seven open asks to him:** stop rule, anchor rule, E2 line, oracles, data, his DXY feed, counting.

**Success conditions:**
- S2 (golden week) and S6 (one command -> one Pine) held;
- S1, S3, S4, S5 open;
- eleventh outside count: E1 98.5 / E2 81.7 / E3 50.7.

---

## 2. Timeline (2026-11-27, UTC)

| Time | Commit(s) | Event |
|---|---|---|
| 13:49-13:52 | `9ea1467` `9e1d7b5` `ea7da38` | 70% package: manifest, archive checksums, bundle delivered in two parts |
| 14:48 | `6683095` | Package delivered. The operator allowed the event-data hosts; the first fetch was refused by the session's permission check. |
| ~15:00 | `4961cd0` (15:09) | **M-58** (his answer to the seven asks). Rulings L-46 .. L-49. Part 8 = the OmniGraph as its own archive. |
| 15:26 | `555482a` | M-58 item 5: TVC chart correction. Item 1: stop scenarios with charts (`tools/research/stopscen.py`). |
| 15:36 | `b429b8c` | Items 4 (library inventory) and 6 (counting question); item 7 probes; D-129 |
| 15:42 | `7f1babd` | Item 7: Protocols D (Treasury auctions) and G (EIA crude) harvested for all 40 weeks |
| ~15:50 | - | He asked "Do you have all of the data you need from me ...?" I answered with the open list (journal). |
| 16:01-16:02 | `7460b58` `636326e` `a918580` | Item 2: **daily anchoring** (D-131), then made the default |
| 16:14 | `496d4f6` | Library frames `evidence/lib1` (4 GBPUSD weeks); ledger 108 / 108b |
| 16:30 | `58b8a8e` `43c5ae1` | Protocol E (NY Fed ON RRP), after he allowed markets.newyorkfed.org |
| 16:36 | `748c71e` | D-132: alternative chain activates at a day's anchor (6.6 Step 4); ledger 109 / 109b |
| 16:39 | `f4ad3a9` `dace31b` `df37f52` | D-133 tried and reverted; V1 caches; library Pine |
| ~16:45 | `306e94c` (16:51) | **M-59** (answers to six questions). Rulings L-50 .. L-55. |
| 16:52 | `980bcf6` | D-134: no duplicate trades |
| 16:55 | `0451a56` | D-135: stops per L-50 |
| 16:56 | `1024df9` | L-53 design written down before the build |
| 17:13 | `e1eaa21` | D-136: daily zone update at the London open, with chain re-anchor |
| 17:17-17:20 | `e8e095b` `fe24f31` `5c79a80` `6da7ef5` | L-51 session-by-session line (first version); lib3 render FAILED under load (ledger 110b); the day line from the day's own price |
| 17:24-17:30 | `a90eb60` `71fe111` `4a8313c` `8a40708` | V1 caches; D-137 (chain re-anchor OFF for orders); D-138 (re-anchor kept for the drawing) |
| 17:33-17:34 | `b13a452` `aa8d689` | Ledger 111b / 111c (lib4 frames, one render at a time) |
| ~17:45 | `0d4ad41` (17:49) | **M-60**. Checkpoint "80% functional - DXY specific" (code `aa8d689`). |
| ~17:50 | `2f31cf5` (17:52) | He asked that the commit carry code + context + graph: the checkpoint made self-contained (`tools/checkpoint`) |
| 17:56 | `e3860c7` | Whole-week frames of all three pairs (`tools/weekframe`); ledger 112 |
| 17:57-18:02 | `59c98fe` `d642f22` `d48d3e9` `bac6b50` | D-139 (6.10 in hours), D-140 (session ladder); ledger 113 (`evidence/m60b`) |
| ~18:15 | `cea1954` (18:23) | **M-61**. Checkpoint V1 "85% functional - DXY + GU" (code `bac6b50`). |
| 18:27-18:31 | `262fadd` `65ae7fc` `6e4f3f7` | D-141 Thursday fix; V2 frames (ledger 114); checkpoint V2 |
| ~18:35 | - | Context compaction (the summary is the first message of the next window; transcript in archive part 4) |
| 18:59-19:07 | `0bb5182` `ff6be1e` `a8bfce4` `8f834f4` `63d10dc` | V3: EURUSD diagnosis, D-142b + D-144, frames (ledger 115 / 115b), checkpoint V3 |
| ~19:10 | - | V1 / V2 / V3 report to him: nine whole-week frames + `evidence/answers_m61/EURUSD_why_C.md` |
| ~19:40 | - | **M-62**: this package |
| ~19:50 | - | D-145 crash found by the locator re-run, fixed |
| ~20:00 | - | **M-63**: each handover as its own self-contained GitHub branch |

---

## 3. The operator's messages and rulings in this window

All are verbatim in `memory/12`; the rulings are in `memory/04`.

### M-58: his answers to the seven asks of the 70% package

| Item | What he said | Ruling | What I did |
|---|---|---|---|
| 1 | "it is either 2-3 pips outside the entry zone or 1-2 pips inside the next zone. Give me multiple practicals scenarios ..." | L-46 | Section 4.1: scenarios with charts |
| 2 | Daily anchoring "yes if you do this right without grating"; save the checkpoint first | L-47 | The 70% checkpoint was already on GitHub + archives; daily anchoring (section 6) |
| 3 | "illustrate this with multiple different examples" | - | Three pictures + question (section 4.3) |
| 4 | "do you have my winning trade library? ... 20+ distinct trading weeks" | L-48 | Inventory: about 17 pair-weeks; the library = the oracle set (D-129) |
| 5 | "I use TVC - show me exactly" | L-49 | TVC chart, correcting my earlier claim |
| 6 | "explain this question better" | - | `Q6_counting_explained.md` |
| 7 | "I enabled permissions ... Else spawn a subagent on muse spark 1.3 from the opencode go api key and fetch the data that way" | - | Protocols D / E / G built; F blocked (section 5) |

### The follow-up question and M-59

He asked "Do you have all of the data you need from me ...?". I answered with six open points: stop > 9.5 pips; the E2 drawing; whether repeats count; whether zones may be added as they form; Forex Factory; more library weeks.

M-59 answered all six:

| Ruling | Subject | What he ruled |
|---|---|---|
| L-50 | Stops | A good trade takes the WIDER stop; skip only low-probability trades. EUR/USD uses the inside stop "where applicable". The pairs' liquidity mechanics: GBP/USD shield OUTSIDE the S/D zone, EUR/USD liquidity INSIDE it. |
| L-51 | E2 drawing | Box + line; each swing drawn inside a SWING SCALPS box; the line = the price action candle by candle |
| L-52 | Duplicates | NO DUPLICATE TRADES: "explicitly forbidden and banned" |
| L-53 | Zone update | Zones may be re-updated at each London open, without duplicates or "hallucinated slop" |
| L-54 | Forex Factory | "Either make it work or work within the constraints" -> Protocol F = NO DATA |
| L-55 | Library | The library's about 17 weeks are enough |

### M-60

- Checkpoint "80% functional - DXY specific".
- DXY first half accurate.
- DXY E2 Wed-Fri "obviously broken".
- GBPUSD "completely fucked".
- EURUSD missing.
- EVERY report shows ALL THREE pairs, the whole week in one fitted screenshot each (L-56).

Then: "Make sure all context and the graph is submitted with the commit so that everything is self-contained."

### M-61

- DXY and GBPUSD "A-" except Thursday: a LONG where the correct trade is a SHORT at the exact take-profit of Wednesday's long, where the E2 chain predicts the peak.
- EURUSD "a solid C".
- Sequence: V1 = this checkpoint, V2 = after the Thursday fix, V3 = after the EURUSD fix; then report everything (L-57).

### M-62

"Okay, great." Then: this package, "Same level of detail ... Do not water anything down, do not hold anything back." (L-58)

### M-63

Each handover as its own fully self-contained branch on GitHub `leviathan-devops/plutus-vision` (L-59).

---

## 4. Answers delivered for M-58

### 4.1 Item 1: stop scenarios

Files: `evidence/answers_m58/Q1_stop_scenarios.md` and frames `s1/s2/s3_stop_scenario.png`. Generated by `scenario_pine.py`, from `tools/research/stopscen.py`, which finds real cases on the count maps.

Each scenario shows:
- the entry zone;
- the next zone;
- rule (a) "2-3 pips outside the entry zone";
- rule (b) "1-2 pips inside the next zone";
- what price did;
- my decision and the question to him.

His answer (M-59) became L-50.

His sources on stops, read first-hand and quoted in L-46:
- TL "SL should be 1-2 pips OUTSIDE THE BACK EDGE OF THE STOP-LOSS ZONE";
- TL "If thin liquidity zone - move it 1 pip inside the next zone";
- TL "If NY session trades - 2-3 pips | London session 1-2 pips";
- TL "SL inside the next zone always" (stop-limit entries);
- TL scalps "1.5-2.5 pips inside the next 5m liquidity zone";
- TL "If you stop loss ends up sitting inside a liquidity zone - you MUST move it 2 pips outside the back edge of this zone. No exceptions";
- P533:506 "SL correction/reentry exception";
- E3C:247-256.

### 4.2 Item 5: TVC

`evidence/answers_m58/q5_golden_monday_long_TVC_DXY_15m.png` shows his golden Monday long 100.945 / 100.905 / 101.115 on TVC:DXY 15m, with the anchor line. It corrects my earlier statement in the 70% package (section 9.6) that it could not fill.

### 4.3 Item 3: the E2 drawing question

Folder `handover/85pct_v3_full/answers_m58_q3/` (from the scratchpad) holds `Q3_E2_drawing_question.md` and three pictures:
- my golden DXY;
- my EURUSD Oct 5 range week;
- his library GBPUSD Feb 26 - Mar 3 shape boxes.

He answered: option C, box + line, each swing inside SWING SCALPS boxes (L-51).

### 4.4 Item 4: the library

`evidence/answers_m58/Q4_library_inventory.md` reads each picture's date axis:
- GBPUSD Feb 2 - Apr 24 2026: 12 weeks;
- EURUSD Apr 13 / Jul 6 / Jul 13;
- DXY Apr 13-24 / Jul 6.

That is about 17 pair-weeks. The zip is complete (64 entries), unpacked at `/home/user/inputs/trades/WINNING_TRADE_LIBARARY/` (archive part 5).

**D-129:** the former S5 blind-test reserve (Feb 2 - Mar 23) lies inside the library, so it becomes oracle weeks. S5 blind weeks must come from outside the library and outside every week already run.

### 4.5 Item 6: counting

`evidence/answers_m58/Q6_counting_explained.md` explains:
- how outside counters disagree on "obvious trades" (EURUSD Oct 5: counter A 10, counter B 5; all 12 maps 95 vs 67);
- per-day repeats (EU1.Tue-Fri = 2 ideas drawn as 9 boxes).

His answer, L-52, made repeats void.

### 4.6 Item 7: data

Section 5.

---

## 5. Event data: Protocols D, E, G (and F)

Code: `sidecar/protocols.py` (new, 174 lines). Output: `sidecar/out/protocols/<monday>.json`; raw pages are cached in `sidecar/raw/protocols/`. Run for all 40 sidecar weeks. Only data dated or released BEFORE the week's anchor is kept.

| Protocol | Source | Rule (canon) | As-of logic |
|---|---|---|---|
| D: Treasury auctions | `https://www.treasurydirect.gov/TA_WS/securities/search?startDate=..&endDate=..&dateFieldName=competitiveAuctionCloseDate&format=json` (`dateFieldName=auctionDate` gives HTTP 500) | Trigger: bid-to-cover >= 2.6 (P452:1443) | Latest fixed-rate (`floatingRate != Yes`) 2Y / 5Y / 10Y note result closed before the anchor (close date + time ET). The week's coupon auctions announced BEFORE the Monday (`announcementDate < monday`), with their close time. Their results are post-anchor and not stored. |
| E: NY Fed ON RRP | `https://markets.newyorkfed.org/api/rp/reverserepo/propositions/search.json?startDate=..&endDate=..` (host allowed by the operator during the session) | Trigger: a USD 50bn contraction (P452:1444) | The last two operations dated before the Monday. No week of 2026 triggers. |
| G: EIA crude stocks | Series WCESTUS1 `https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=WCESTUS1&f=W`; schedule `https://www.eia.gov/petroleum/supply/weekly/schedule.php` | Trigger: absolute deviation >= 5M barrels (P452:1446) | Only prints released before the anchor. Release Wednesday 10:30 ET, or EIA's alternate date (holiday weeks Thursday 12:00). Deviation = change minus previous change. |
| F: red-folder calendar | www.forexfactory.com | - | **NO DATA**, for three reasons: (1) Cloudflare "Just a moment" (403) to curl; (2) a headless-Chromium load was refused by the session's permission check ("Unauthorized Access") and not retried; (3) his fallback, Muse Spark 1.3 via OpenCode Go, has no web search (one request answered "NO_WEB_SEARCH"). L-54: work within the constraint, do not raise it again. |

**Where it shows:**
- `e2_chain._triggers`: each day's "Triggers" line lists the day's 10:00 NY option cuts, the coupon auctions closing that day and the EIA release of that day;
- an Engine 2 report block "VOLATILITY TRIGGERS (as of the anchor)".

Drawing code was identical on the golden week (only comments changed).

**Rules respected:**
- the OpenCode key is injected by the network proxy for opencode.ai (`Authorization: Bearer proxy-injected`) and was never read or printed;
- nothing after the anchor is stored.

---

## 6. Daily anchoring (D-131 .. D-138): the architecture

His approval: L-47, "yes if you do this right without grating". My reading: without cheating, so each day uses only data closed before its own anchor.

**Canon behind it:**
- Fibonacci Spiderwebs items 3-5: "London Session open position = Trade Setup Anchor";
- E3C:115: `WorkingDayMap.dayOpenSpot`;
- P452 6.6 SESSION-LEVEL SHAPE MAPPING RULES;
- 6.6 Step 4: alternative chains.

### 6.1 The two instants per day

| Instant | Time | Role |
|---|---|---|
| `t_a(i)`, trading-day open | Monday: the week anchor b0 = Mon 02:00 NY. Tue-Fri: 17:00 NY of the previous evening (`DAY_CONFIRM = 'start'`) | The day's orders are confirmed and the line restarts from the real price |
| `t_L(i)`, London open | 02:00 NY of day i (`e1_data.day_anchor_ms`) | Engine 1 is rebuilt as of then and new zones are added |

`t_e(i)` = 17:00 NY of day i (end of the trading day).

**Why the trading-day open and not the London open** (D-131, measured on the 12-map order locator):
- London-open anchoring lost every Asian-session fill, among them his golden Friday long, filled 02:15 UTC. Result: 22 TP / 10 SL.
- Trading-day open: 31 TP / 10 SL.
- The old weekly build: 34 TP / 22 SL. That build's extra stops were repeats on order blocks already closed through.

### 6.2 The algorithm (`plutus.daily_anchor`, run by `plutus.run(pair, monday, daily=True)`)

`daily=True` is the CLI default. `--weekly` gives the old behaviour, byte-identical to before on 4 weeks x 3 pairs when it was introduced.

The Monday Engine 1 map (`_map`) and the Monday chain + orders (`engines`) are built at b0. Then, for each day i = Mon..Fri:

**1. Alternative activation (i > 0, 6.6 Step 4, D-132).** For each alternative of the chain in force:
- its Decision-Zone trigger level comes from `_levels`: the level Engine 3 gave the alternative's orders, else the alternative zone's edge plus its sweep reach;
- a 1H close beyond that level since the chain's anchor means the primary failed;
- the alternative becomes the chain in force (audit line "ALTERNATIVE CHAIN ACTIVE");
- its orders become live, the primary's orders and the other alternative's orders are void, and the <= 11 cap is re-applied.

**2. The day's box and line.**
- The view chain is the drawing chain `vw` (D-138), else the active alternative, else the chain.
- The line = the chain's path cut to [t_a, t_e], with its first point moved to (t_a, open price at t_a).
- For i > 0:
  - a pure swing-scalp day gets `_day_line`: a session path from the day's own price, first swing to the NEARER bound (P533 2.3 "magnetize toward the IL levels", D-41), next swing to the other bound;
  - any other day holds the open price through Asia and joins the chain's legs at t_L (P452 6.6 rules 1 / 6; D-140).

**3. Carry-over (L-52).** On a pure SS day, a swing-scalp order still pending at t_a that passes confirmation keeps resting into the day: its `valid_to` is extended, and no copy is made.

**4. Orders of the day** (orders whose `rest_from` or `day` is day i):
- **Clones** (Engine 3's per-day repeats of an earlier order):
  - if the original is still pending or open at t_a, the clone is "NOT A NEW TRADE"; the original keeps resting, its box extends (D-134);
  - if the original completed, the level may carry a NEW trade for the next move (fresh number);
  - on EURUSD / GBPUSD that new trade also needs the source pair's same-day record (D-142b, section 12).
- **confirm()** (returns the reason when an order is NOT confirmed):
  - a rocket must stand AHEAD of price in the move's direction (D-141: FA 8 trip-wire "trigger zone ... zones ahead"); a rung the move already passed is void;
  - an order block (S/D candle zone) under the order must not have been closed through since b0 (one-time use: P452:699-703, L-38, `e1_sd.valid`);
  - the price at t_a must stand on the order's side of its entry;
  - its parent must have been confirmed.
- **Law-27 trade flow** on the day's line (D-144, section 12).
- `parts[i]` records the open price, the active alternative, the confirmed orders, the number dropped, the line's first point and the day's Phase-10 keys. Leak check part 3 compares exactly these.

**5. London open, i > 0 (L-53, D-136).**
- `Xi = _map_at(pair, monday, t_L)`: Engine 1 rebuilt with `e1_data.ASOF[monday] = t_L`. `boundary_ms` returns ASOF, so every read stops at t_L. The V1 harvest is cached per instant: `e1_tool/cache/v1s/PAIR_TF_MONDAY_<ms>.json`.
- `_new_zones` adds zones not overlapping any zone of their family already drawn:
  - S/D candle zones FORMED SINCE b0 (by origin time);
  - sweep zones (LSZ) of the week's own daily highs / lows, unswept;
  - pressure zones the day's map draws.
- They are drawn from t_L to the week end with "new <Day>" labels (`_new_zones_pine`).
- If the chain in force has failed:
  - `REANCHOR` (orders): **OFF** since D-137;
  - `REANCHOR_DRAW` (line and day boxes): **ON** since D-138. The drawing chain `vw` = Engine 2 + 3 re-run as of t_L on `Xi` (`_engines_at`; the Phase 10 sources at the same instant). It is re-anchored again when `vw` fails at its own Decision Zone.

**After the loop:**
- children of dropped parents are removed;
- the <= 11 trades cap is applied (latest days' weakest first; L-04 / R-07);
- one numbering for the week (DX1.., EU1.., GB1..; alternatives DXA1..);
- dormant alternative orders are removed from the drawing and listed in the report as "CONTINGENCY" lines (D-141).

### 6.3 What was tried and rejected along the way

| Trial | Result |
|---|---|
| Re-running Engine 2 from scratch each morning (first attempt of D-131) | Rejected: each morning re-applies 6.10's +1 day and pushes the golden breakout out of the week (Wed / Thu forecast SS) |
| London-open order confirmation | Rejected: loses Asian fills (6.1) |
| D-133: re-anchoring a failed chain on the FIXED Monday map | Reverted. GBPUSD Apr 13 gave a 300-pip SS range (no zones in the new price area) and a swing-scalp TP 260 pips away. Locator: 77 orders / TP 31 / SL 10 / unfilled 34, against D-132's 61 / 31 / 10 / 19. |
| D-136 chain re-anchor for ORDERS on the rebuilt map | Switched off by D-137. TP 27 -> 23, unfilled 6 -> 13: it cancels resting winners and replaces the alternative's post-breakout orders with range orders that do not fill. Kept for the drawing (D-138). |

### 6.4 Temporal-anchor proof (leak check part 3)

`tools/leak_check.py` has three parts:
1. **Static:** no bar read outside `e1_data.closed()` and its helpers; no week literal in engine code.
2. **Week anchor:** the full output is byte-identical with the bar store cut at the anchor.
3. **Per day:**
   - for every day i, cut the bar store at t_a(i) and then at t_L(i);
   - every day's trading-day-open part decided before the cut must be identical, and likewise its London-open part.

The pre-commit hook (`tools/git-hooks/pre-commit`) runs it on golden DXY + EURUSD whenever `e1_tool/*.py` is staged. In this window it also ran on golden GBPUSD and GBPUSD 2026-10-05 (`locator_outputs/leak_check_4maps_V3.txt`).

It caught one real leak (D-142, section 12).

---

## 7. Stops per L-50 (D-130 -> D-135)

Before L-50, D-130 tried P533:506 ("When trying to catch a CORRECTION/REVERSAL - ALWAYS make sure SL is 1-2 pips INSIDE THE NEXT ZONE ... Standard SL rules (outside the zone) apply for trend-following entries"). It used rule (b) on the first shield for reversal entries (SS / RWL / R / WL).
- Locator: TP 34 -> 33, stopped 22 -> 22. The golden 9.5-pip SL envelope (E3C 12.2) filtered the farther (b) stops.
- Not adopted; the flag stayed off pending his answer.

**L-50 (M-59):** "Take the wider stop ... Don't skip good trades ... Euro USD should use the inside stop too where applicable".

**D-135, in `e3_trades._stop` and `_build`:**
- Reversal entries (`REVERSAL_SHAPES = ('SS','RWL','R','WL')`; not the transition) take rule (b): 1 pip inside the close edge of the next shielding zone, a thick step (FA 2.1 "Thin liquidity zones are NEVER allowed as entry or SL zones"). The 9.5-pip envelope does NOT veto them; the RRR floor still decides.
- When an attempt fails the RRR floor, the next entry attempt must be DEEPER ("potentially even set a better entry"), never shallower (`e_first`).
- EUR/USD keeps rule (a) (`EU_INSIDE = False`): his golden EUR/USD stops measure 0.2-0.4 pips from rule (a); the next-S/D-zone reading lands 2-6.5 pips off and tighter than his.

**Measured (locator, 12 maps, daily, unique):**
- 46 / 28 TP / 10 SL / 7 unfilled -> 43 / 27 / 8 / 6;
- his Apr 20 real long now 98.019 (his 98.02);
- golden GBPUSD stops drift from his (GB1 1.3 -> 8.0 pips): the GBP/USD liquidity-outside mechanics of L-50 are an open item.

---

## 8. The Engine 2 line (L-51): session path, day line, speed, ladders

### 8.1 Swing-scalp steps session by session (`e2_chain._session_path`, flag `SESSION_PATH`)

From P452 6.6 SESSION-LEVEL SHAPE MAPPING RULES (P533 6.6 "unchanged"). Inside an SS step, per day:

| Rule | Session | Drawing |
|---|---|---|
| 1 | Asian | Price "stays within the prior day's range": drawn flat |
| 2 | London, 02:00-08:00 NY | The session's swing to a bound of the range |
| 3 | NY pre-cut, 08:00-10:00 NY | "dealers will pin price to the largest strike": pinned at the day's largest option strike inside the range, when there is one |
| 4 / 5 | 10:01 NY Spring Release, then NY post-cut 10:01-17:00 | "free movement toward the next IP zone": the swing to the other bound |

Swings alternate bound to bound (6.1.1). They are counted back from the step's end, so the last one runs in the chain's direction and ends at the pivot when a retest follows. Engine 3's legs are unchanged (orders identical on the golden week).

### 8.2 The daily-anchored day line (`plutus._day_line`)

Under daily anchoring a pure SS day is redrawn from the day's own price at t_a. The first swing goes to the bound NEARER that price; then the session rules apply.

### 8.3 D-139: 6.10 "2-3 more 4H candles" in hours (flag `SPEED_4H_HOURS`)

**Before:** a 4H element's breakout took `BS_SESSIONS * 2` sessions ("twice as long").

**Now** (P533:2048 "A 4H breakout that appears imminent may take 2-3 more 4H candles to complete than initially predicted"): the breakout runs 12 hours (3 x 4H, the upper figure, as `BS_SESSIONS` takes 6.8's upper figure) past the end of its `BS_SESSIONS` sessions.

**Golden DXY:**
- BS Wed NY .. Fri TKY (5 sessions; was 6, to Fri LON);
- WL + RWL in Fri LON: his Friday WL low (about 100.60) printed in London, and the RWL ran through NY.

Golden trades unchanged on all three pairs.

### 8.4 D-140: breakouts drawn as a session ladder (`e2_chain._ladder_path`)

A BS / PBS step spanning several sessions:
- Asia holds;
- each London / NY session steps toward the target, ending at a mapped level in the way (an IP zone edge, a 1H / 4H S/D edge, a V1 4H band) when one lies within 25% of the span from the proportional target, else at the proportional point;
- the last active session reaches the target.

A non-range day's line holds the day's open through Asia and joins the chain at the London open.

**Golden DXY Wed-Fri, drawn vs candles (UTC):**

| Day | Drawn | Candles |
|---|---|---|
| Wed | Asia flat 101.09; London up to 101.305; NY down to 101.13 | 101.30 / 100.98 |
| Thu | Asia flat 101.07; London 100.85; NY 100.75 | NY 100.84 |
| Fri | Asia flat 100.94; WL to 100.654 by 09:20; RWL to 100.815 by 16:00 | low 100.60 around 08:00; NY 100.97 |

### 8.5 Small Engine 2 changes that daily anchoring needed (D-136)

- `week_sessions` drops sessions that ended before the (re-)anchor.
- The NY-cut cage uses "today" (a cut already past cages nothing).
- `adj_day` is clamped to the chain's first session (no transition timed before its own anchor).
- `E2.pine` draws one line segment list per day (`segments`) and the alternative's dotted segments (`alt_segments`).

---

## 9. Checkpoint "80% functional - DXY specific" (M-60) and the two tools it brought

**Checkpoint:** `0d4ad41` (code `aa8d689`), made self-contained by `2f31cf5`, after his "Make sure all context and the graph is submitted with the commit".

**`tools/checkpoint DIR "TITLE" "VERDICT"`:**
- rebuilds the OmniGraph from `memory/*.md` (`tools/mem/mem rebuild`);
- copies the store directory (`/home/user/.plutus-mem`) into `handover/DIR/omnigraph/graph_store`;
- writes `omnigraph export` -> `graph_export.jsonl`, plus `mem status` / `mem ls`;
- writes `CHECKPOINT.md` (title, code commit, verdict, contents, restore);
- writes `MANIFEST.sha256` of every tracked regular file (gitlink directories skipped: a `[ -f ]` filter, after `sha256sum` errors on gitlinks).

**`tools/weekframe OUTDIR PAIR:MONDAY ...`:**
- one screenshot per map with every layer;
- x-axis exactly Monday 00:00 UTC -> Friday 21:00 UTC;
- price axis fitted (`tools/pbfit`);
- ONE render at a time;
- skips the frame when `pb ide` reports REFUSED / an error.

Built for L-56 / M-60: "I need to see the entire trading week in a single screenshot".

His read of this checkpoint (M-60):
- DXY golden first half accurate;
- DXY Wed-Fri E2 broken: the whole-week frames (ledger 112) showed one straight slide Wed NY -> Fri LON, with WL + RWL squeezed into Fri NY. That diagnosis led to D-139 and D-140.

---

## 10. Checkpoint V1 "85% functional - DXY + GU" (M-61)

`cea1954` (code `bac6b50` = D-139 + D-140). Frames `evidence/m60b/`.

His grades:
- DXY and GBPUSD "A-" except the Thursday trade;
- EURUSD "a solid C".

---

## 11. V2: the Thursday fix (D-141, code `262fadd`)

### Diagnosis

**DXY Thursday.** The drawn "long" was DXA2, the ALTERNATIVE chain's ladder long at 100.98. It was dormant (live only after a 1H close beyond the alternative's Decision Zone) but drawn on Thursday as if it were a live trade, on top of DX7's ladder short.

**The short he expected:** at DX6's TP 101.235 = his #6 Wed S 101.235. It existed (DX4) but was drawn only from the consolidation day, not from the predicted peak.

**GBPUSD:**
- the mirrored ladder long GB5 1.33473 stood 47 pips BELOW Thursday's open: a rung the move had already passed;
- plus the mirrored dormant alternative orders.

### Fix (Law 27 E3C:438-449; 6.6 Step 4; FA 8 rocket trip-wire; L-52)

1. **Contingencies.** An alternative chain's orders are not drawn until the alternative is activated at a day's anchor (D-132). They stay in the report as "CONTINGENCY <id> ... live only after a 1H close above/below <level> (<zone>); not drawn unless activated".
2. **Law-27 start.** A breakout order whose entry is the reverse whiplash's TP ("TP of N = entry of N+1") exists from that whiplash's start (`law27` flag on the setup; `rest_from = prev['day']`, `t0 = prev['t0']`; `valid_from >= t0` in `build`; `E3.pine` x0 = `day_anchor`). DX4 is now drawn from Wed 06:00 at the predicted peak.
3. **Passed rockets void.** At a day's anchor, a rocket the move has already passed is not a new order of that day (confirm()). GBPUSD's Thursday 1.33473 and Friday 1.33888 ladder longs are dropped.

### Result

- DXY Thursday = DX7 ladder short (his #7).
- GBPUSD Thursday = the short at GB4's TP, 1.34254 (his #5).
- DXY otherwise unchanged.
- Frames `evidence/v2/` (ledger 114).

---

## 12. V3: the EURUSD fix (D-142b, D-144; D-143 rejected)

### 12.1 Why EURUSD was a C

Also in `evidence/answers_m61/EURUSD_why_C.md`. Golden EURUSD orders at V2:

| Order | Day / shape / dir | Entry / SL / TP | Outcome | His trade |
|---|---|---|---|---|
| EU1 | Mon SS S | 1.14442 / 1.14508 / 1.14068 | TP | #3 |
| EU2 | Mon SS S | 1.14385 / 1.14451 / 1.14068 | **SL** (by 0.3 pip) | none |
| EU3 | Mon SS L | 1.14018 | never filled | none |
| EU4 | Mon SS L | 1.14095 | TP | #2 |
| EU5 | Tue SS L | 1.14095 (re-entry after EU4's TP) | **SL** | none |
| EU6 | Wed RWL S | 1.14269 | TP | #5 |
| EU7 | Wed BS L | 1.13940 | TP | #6 |
| EU8 | Wed SS L | 1.14018 | TP | #4 |
| EU9 | Thu ladder L | 1.14239 | rocket | #7 |
| EU10 | Fri RWL S | 1.14598 | TP | #8 |

His #1 (Mon S 1.14322 / 1.14408 / 1.14103) traded only in the Asian session. Price sat at 1.1432-1.1441 from Sun 21:00 to Mon 05:30 UTC and never came back to 1.14322 after the 06:00 UTC anchor before its TP at 10:00. It is out of the map's reach by the temporal anchor.

**What separates EURUSD from DXY / GBPUSD: two stop-outs, plus clutter.**

**(a) EU2: a second short for the same move, entered too early.**
- EU2 = the 1H supply BoM 1.14375-1.14421, whose origin is the mirror candle of his DXY 1H MoM. The pressure zone UPPER RESISTANCE 1.14444-1.14533 sits directly above.
- EURUSD pierced the 1H supply and turned at the pressure zone. The 18:45 UTC spike to 1.14454 stopped EU2 by 0.3 pip and filled EU1 (his #3).
- When price reached 1.14385, EU4 (his #2) was still running to its TP 1.14429.
- On DXY the mirror case did not hurt: DXY turned at its 1H supply (101.14, his #2) before its pressure zone, so the stacked second short (101.203) simply never filled.

**(b) EU5: a re-entry the source did not have.**
- DXY had dropped its own Tuesday copy as still open.
- EURUSD mirrored DXY only at the week anchor (Phase 10 cascade not applied per day), so it re-armed its level on its own.
- Wednesday's RWL retest stopped it.

**(c) Clutter:** four Monday boxes, the Tuesday re-entry, the V1 alternative boxes, and overlapping Wednesday labels.

**What does NOT separate EURUSD (locator `scratchpad_scripts/lineerr.py`):** the drawn line's mean miss outside each 1H bar:
- DXY: 6.7% of the week range;
- EURUSD: 7.2%;
- GBPUSD: 5.9%.

### 12.2 Rules rejected before coding, each by a golden counter-example

| Rule | Counter-example |
|---|---|
| "One order per bound: the nearer one" | Keeps the 1.14385 loser and drops his #3 |
| "The bound only" | Drops his DXY #2 (101.14) and EURUSD #2 |
| Count-aware 1:1 mirroring per (shape, day, direction) | E3C 10.6: "Emergent pair-specific trades ON TOP are fine and encouraged" |
| Law-27 consistency without time order | Drops his DXY #2 |
| E3C Phase 6.3 duplicate rule ("same category AND entries within 5 pips") | Does not catch the pair: entries 5.7 pips apart |

### 12.3 D-143: tried, rejected (flag `e3_trades.SL_CLEAR_LQZ = False`)

**Rule tried:** TL "If you stop loss ends up sitting inside a liquidity zone - you MUST move it 2 pips outside the back edge of this zone. No exceptions", applied to rule-(a) stops on the V1 1H rungs / 4H bands (`e3_trades._clear_liq`).

**Result:**
- EU2's stop (1.14451) sits in no rung, so it was unchanged.
- EU1's stop moved 1.14508 -> 1.14532. His 1.14505 sits INSIDE the same rung 1.14484-1.14512.
- EURUSD lost his #6 / #7 / #8 to the moved stops.

His own golden stops contradict this reading on my rungs. Lesson L-56x: his hand outranks my reading.

### 12.4 D-142 / D-142b: Phase 10 cascade under daily anchoring

E3C:723-770: "For each DXY source setup, generate the corresponding EU mirror setup (inverse direction). For each EU mirror setup, generate the corresponding GU mirror setup (kept direction)"; 10.5 "GU mirrors ACTIVE EU mirrors, NEVER raw DXY".

**First version (uncommitted, caught):**
- (1) the receiving pair's week-anchor Engine 3 mirrored the source pair's WHOLE-WEEK daily-confirmed orders;
- (2) a daily re-entry needed the source's matching order that day, read from the same whole-week result.

`tools/leak_check.py` part 3 caught it:

> LEAK-DAILY GBPUSD 2026-07-06: day 0 (trading-day-open part) changes when the bars after the trading-day open of day 1 are removed

Later days' decisions leaked into Monday. The checker's exit code 1 was hidden by my `| tail` wrapper (lesson L-57x); the checker itself is right.

**D-142b (committed `ff6be1e`):**
- The week-anchor build mirrors the source's week-anchor setups (as V2).
- Each day records in `parts[i]['keys']` the (shape, direction) of the primary orders it confirmed at its own trading-day open: every DXY order; on EUR/USD only its active mirrors.
- A re-entry on EURUSD / GBPUSD at day i needs `(shape, mirrored direction)` in the source's day-i record (`plutus._src_days`, flag `PHASE10_REENTRY`). DXY -> EU inverts; EU -> GU keeps.

**Golden result:**
- EURUSD Tue re-entry long 1.14095 gone: DXY's day-1 record is empty, since DXY did not re-arm.
- GBPUSD Tue 1.33333 duplicate (never filled) gone.
- DXY unchanged.

### 12.5 D-144: the Law-27 trade flow on the day's line (`plutus._flow27`, flag `FLOW27`)

**His golden weeks run as ONE Law-27 flow on every pair.** Each trade enters at the previous trade's TP:
- EURUSD: #1 TP 1.14103 -> #2 E 1.14106 -> TP 1.14442 -> #3 E 1.14441 -> TP 1.14004 -> #4 E 1.14012 -> ...;
- DXY and GBPUSD the same (`memory/08`).

E3C 6.2 / 8.21: "TP of trade N = entry of trade N+1", 3-pip tolerance. M-61: "The long on Wednesday that hit take profit, that should literally be the entry of the short at that exact point."

**Rule.** On the day's drawn Engine 2 line (built at the day's trading-day open), take an opposite-direction order A: one of the day's orders, or an earlier one still resting / open at the anchor. If, after A's entry and before A's TP:
- the line reaches order B's entry, AND
- B's entry lies INSIDE A's move, more than 3 pips short of A's TP,

then B trades against the move in progress. It is not the next trade of the flow (that one enters at A's TP), so B is not placed. Rockets ride their parent and are not judged.

**Leak-safe:** it runs inside the per-day loop on that day's line, and its result is part of `parts[i]['orders']`.

**Golden:**
- EURUSD Monday short 1.14385 gone: "the Mon line reaches it 2026-07-06 19:56 UTC while SS LONG 1.14095 runs to its TP 1.14429 (4.4 pips short of it)".
- Kept: DXY DX3 (2.1 pips from DX2's TP, within tolerance) and GBPUSD GB1 (beyond GB2's TP).
- DXY and GBPUSD unchanged.

### 12.6 V3 results

**Order locator, 12 maps, daily (`locator_outputs/orders_12maps_daily_V{2,3}_*.txt`):**

| Version | Orders | TP | SL | Unfilled | Open |
|---|---|---|---|---|---|
| V2 | 44 | 26 | 8 | 8 | 2 |
| V3 | 39 | 26 | 5 | 7 | 1 |

The five orders removed:
- EURUSD golden Mon S 1.14385 (SL);
- EURUSD golden Tue L 1.14095 (SL);
- GBPUSD golden Tue L 1.33333 (unfilled);
- EURUSD 10-05 Wed SS L 1.11710 (open);
- GBPUSD 10-05 Tue SS S 1.32329 (SL).

**Leak check** clean on golden DXY / EURUSD / GBPUSD and GBPUSD 10-05 (week anchor + every day's trading-day open and London open).

**Frames** `evidence/v3/` (ledger 115b):
- EURUSD Monday = one short (his #3) + the two longs;
- both stop-outs gone;
- DXY identical;
- GBPUSD only the unfilled duplicate gone.

**Still visible:** EURUSD Wednesday labels overlap each other and the LSZ / option labels at 1.1400; EURUSD Friday line ends at 1.1444 while the RWL ran to about 1.1415.

---

## 13. D-145: a crash found while building this package

**How it surfaced.** Re-running the 70% package's locators at HEAD, `tools/research/e2loc.py` over every DXY week (Apr - Nov, weekly mode) stopped with:

```
File ".../e1_tool/e3_trades.py", line 702, in _build
    if misaligned and ipz is not None and ipz['zfp_num'] > 30 and not a.get('sweep'):
KeyError: 'zfp_num'
```

(`locator_outputs/e2loc_all_DXY_weeks_weekly_V3code_CRASHED_D145.txt`)

**Root cause.**
- Engine 2's bound / target candidates (`e2_chain.py:330`) are dicts `{'src': 'IP', 'zfp': <num>, 'cls', 'rx', 'ip': <the IP zone dict>}`: the pressure zone is NESTED under `ip`.
- When an alternative chain's step (here an SS `ss_after` step on Friday, after a breakout target) uses such a candidate as its from-zone, `e3_trades._build` took `ipz = a` because `a.get('ip')` is truthy.
- It then read `ipz['zfp_num']` on the candidate itself, which has no such key.

The line is old (2026-11-26) and unchanged since the 70% package. D-139 (section 8.3) changed the alternative chains so that some weeks now reach it.

**Fix** (`e3_trades._build`). The narrative check reads the nested zone: `ipz = (a['ip'] if isinstance(a.get('ip'), dict) else a) if a.get('ip') else _ip_at(a, X)`. That is the zone's own ZFP, as E3C:874-876 narrativeAligned "suppress > 30 (WEAK)" requires. `ipz` is used only by the narrative check (two lines), so nothing else moves.

**Crash sweep** (`scratchpad_scripts/sweep.py`, `sweep_daily.py`; outputs in `locator_outputs/sweep_*`).

Weekly mode, every pair-week with a cached week-anchor V1 harvest (75 maps: DXY 40, EURUSD 19, GBPUSD 16):

| Code | Crashes |
|---|---|
| V3 code (`63d10dc`, scratch worktree) | **3**: DXY 2026-04-27, DXY 2026-06-15, GBPUSD 2026-04-13. The tool writes no Pine there. |
| Fixed code | 0 |

Daily mode, the 15 pair-weeks with per-day V1 caches (5 weeks x 3 pairs):

| Code | 12 maps | 04-13 week | 
|---|---|---|
| V3 code (`sweep_daily_15maps_V3code.txt`) | OK | GBPUSD crashes with the same KeyError. DXY / EURUSD needed Thursday / Friday harvests while the station was down (connection refused). |
| Fixed code | OK (`sweep_daily_15maps_HEAD_D145_station_down_for_0413.txt`) | DXY 2 orders, EURUSD 3, GBPUSD 1, after the Pinebox restart (`sweep_daily_0413_HEAD_D145.txt`). **0 errors.** |

**Consequence for the checkpoints.**
- V1 (`cea1954`), V2 (`6e4f3f7`) and V3 (`8f834f4`) all carry this crash on those maps; the 80% checkpoint (before D-139) does not reach it.
- The golden week, the frames and every number reported for V1-V3 are unaffected: those maps never hit the path.

**Leak check:** passes on golden DXY + EURUSD at the fix commit (pre-commit hook).

---

## 14. Verification state at the handover commit

### 14.1 Golden week against his own trades (daily mode, the product's default)

See `CHECKPOINTS.md` for the full table; sources `locator_outputs/od_v3_daily_*.txt`.

| Pair | His trades matched | Distances | Not matched |
|---|---|---|---|
| DXY | #2 #3 #4 #5 #6 #7 #8 | within 0.0-2.7 pips on entry / SL / TP. DX7 (ladder) vs his #7: entry 0.5, SL 1.3; his TP is not legible. | DX1 is an extra that never fills. His #1 (Mon L 100.945): see `memory/08` on the TVC feed and the 70% package section 9.6, corrected by `q5` (it fills on TVC 15m). |
| EURUSD | #2 #3 #4 #5 #6 #7 #8 | within 0.1-2.0 entry; SL up to 4.4 (EU4); TP up to 6.4 (EU1) | EU2 (1.14018) never fills. #1 is pre-anchor. |
| GBPUSD | #1 #2 #3 #5 | - | Not matched: #4 (reinforcement), #6 (Thu long 1.33829), #7 (Fri short 1.34481) |

### 14.2 Locators re-run at HEAD (weekly mode, like for like with the 70% package)

`locator_outputs/`. Bug locators only.

| Locator | 70% package | Now |
|---|---|---|
| `fills_16maps` (16 maps; weekly mode) | 46 TP / 17 stopped | 41 TP / 16 stopped of 145 setups |
| `legs_12maps` (12 non-anchor maps: 1H legs of 30+ pips caught by a setup) | 18/83 | 16/83 |
| `e2loc_16maps` (day tags vs candles) | 54/80 | 54/80 |
| `e2loc_all_DXY_weeks` (every DXY week Apr 6 - Nov 2) | 75/155 | 75/155 after the fix (`e2loc_all_DXY_weeks_weekly_HEAD_D145.txt`); the V3-code run crashed at DXY 04-27 (D-145) |
| `nearmiss_12maps` | - | 87 primary orders / 32 TP / 18 stopped (9 stop near-misses) / 34 unfilled (7 entry near-misses) |
| `sanity_all_DXY_weeks` | 1 finding | V3 code: 3 = two RUN ERRORs (the D-145 crash weeks DXY 04-27 / 06-15) + the same finding as at 70% (DXY 06-08 DX1, a Monday short limit 100.074 already through the anchor price 100.111). After the fix: 1, that same finding. |

The weekly mode is no longer the product's mode: daily anchoring is the default. It is the mode the old locators measure, kept for comparison with the 70% outputs. The daily-mode measures are the order locator (section 12.6), the golden diffs and the leak check.

---

## 15. Code since the 70% package

11 files, +1,037 / -40 lines, before D-145. Function-level map: `CODE_MAP_SINCE_70PCT.md`. Every line: `CODE_CHANGES_SINCE_70PCT.patch`.

### Flags and their values at the handover

| Flag | Module | Value | Decision |
|---|---|---|---|
| `DAY_CONFIRM` | `plutus` | `'start'` | D-131 |
| `REANCHOR` | `plutus` | `False` | D-137 |
| `REANCHOR_DRAW` | `plutus` | `True` | D-138 |
| `PHASE10_REENTRY` | `plutus` | `True` | D-142b |
| `FLOW27` | `plutus` | `True` | D-144 |
| `SESSION_PATH` | `e2_chain` | `True` | L-51 |
| `SPEED_4H_HOURS` | `e2_chain` | `True` | D-139 |
| `REVERSAL_B` | `e3_trades` | `True` | D-135 |
| `EU_INSIDE` | `e3_trades` | `False` | D-135 |
| `SL_CLEAR_LQZ` | `e3_trades` | `False` | D-143 rejected |

The CLI default is daily; `--weekly` for the Monday-only build.

---

## 16. How to reproduce

```
# environment (see 00_START_HERE.md for the full bootstrap)
tools/pinebox-bootstrap.sh
export PATH=$HOME/.local/bin:$PATH XDG_RUNTIME_DIR=/run/user/0
pinebox list --session plutus-main    # dead after a worker restart -> pinebox down --session plutus-main; pinebox up --session plutus-main --adapter xvfb --pair DXY --tf 1H

# one Pine per week / pair (daily anchoring is the default)
cd e1_tool && python3 plutus.py 2026-07-06 EURUSD out/E1_EURUSD_2026-07-06.pine

# a checkpoint's code
git checkout ff6be1e        # V3 code ; 262fadd = V2 ; bac6b50 = V1 ; aa8d689 = 80%

# golden diff (daily mode) - expected output = locator_outputs/od_v3_daily_<PAIR>.txt
python3 -c "import sys; sys.path.insert(0,'e1_tool'); sys.argv=['tools/research/oracle_diff.py','EURUSD']
import plutus; _r=plutus.run; plutus.run=lambda p,m,daily=True: _r(p,m,daily=True)
__file__='tools/research/oracle_diff.py'; exec(open(__file__).read())"

# order locator (daily) - expected = locator_outputs/orders_12maps_daily_V3_tp_d144c.txt
python3 handover/85pct_v3_full/scratchpad_scripts/tplist.py daily

# temporal-anchor proof (week anchor + every day's two instants)
python3 tools/leak_check.py DXY:2026-07-06 EURUSD:2026-07-06 GBPUSD:2026-07-06 GBPUSD:2026-10-05; echo "exit $?"

# whole-week frames, one render at a time (write the expectation in memory/07 first)
tools/weekframe evidence/<dir> DXY:2026-07-06 EURUSD:2026-07-06 GBPUSD:2026-07-06

# a self-contained checkpoint folder
tools/checkpoint <dir> "<title>" "<verdict>"
```

---

## 17. Incidents and lessons in this window

| Incident | Handling / lesson |
|---|---|
| Pinebox render during a parallel locator run: CDP_TIMEOUT, and the frame tool wrote the previous pass's chart (lib3, ledger 110b) | L-50x: never render while another process uses the station; check the `pb ide` box count before citing |
| Pinebox dead after worker restarts (NO_PAGE / CDP unreachable; station `alive: false`), seen several times, the last while building this package | `pinebox down --session plutus-main; pinebox up --session plutus-main --adapter xvfb --pair DXY --tf 1H` |
| `git stash pop` blocked by tracked `.pyc` files after running Python on HEAD | `git checkout -- e1_tool/__pycache__/`; afterwards `PYTHONDONTWRITEBYTECODE=1` for baseline runs |
| Variable shadowing: the CLI variable `daily` shadowed the function | Renamed `daily_anchor` |
| `tools/checkpoint`: `sha256sum` on gitlink directories | Regular-file filter |
| Forex Factory: Cloudflare; the headless load was refused by the permission check; Muse Spark has no web search | F = NO DATA (L-54) |
| markets.newyorkfed.org blocked by the network policy | Requested; the operator approved; Protocol E built |
| ECC GateGuard "Fact-Forcing" denials on new files / destructive commands | Stated facts (files, what it supersedes, where linked, rollback, his instruction) and retried. Never disabled. |
| The D-142 leak (section 12.4) | L-57x: cross-pair inputs under daily anchoring = the source's record of THAT day; run the leak check on every pair; never hide its exit code |
| The D-145 crash (section 13) | L-58x: after an Engine 2 change, run the tool over every cached pair-week |
| Context compactions (one in this window, ~18:35) | `memory/00_COMPACTION_SURVIVAL.md` read order; the summary + journal carried the state |

---

## 18. Success conditions now, and the open work

### S1-S6

| Condition | State |
|---|---|
| S1 coverage | OPEN. `memory/15`: rows still NOT BUILT / PARTIAL. This window touched E3-P6 (Law 27 as a filter) and E3-P10 (per-day cascade). |
| S2 golden week | HELD and improved: all three pairs' orders against his hand (14.1); the operator's grades DXY / GBPUSD "A-" (M-61), then V2 / V3 fixed what he named |
| S3 four weeks x three pairs by outside count | NOT MET. No outside count in this window. The last is count 11 (70% package). The library weeks (L-48 / L-55) are the oracle set now; first deltas for GBPUSD 03-02 and 04-13 are in ledger 108b / 109b / 111b. |
| S4 outside audit | OPEN (`audit/G2_response2.md`) |
| S5 blind test | NOT RUN. Blind weeks must come from outside the library and outside every week run (D-129). |
| S6 one command -> one Pine | HELD at the handover commit (D-145). It was broken on 3 of 75 cached maps from V1 to V3. |

### Open work, in the order of the standing loop

1. **GBPUSD:**
   - his #6 (Thu long 1.33829 after the reversal short's TP: the pair ran a day ahead of the translated DXY timing and made a second leg up);
   - #7 (Fri short 1.34481);
   - the L-50 liquidity-outside mechanics (GB1 stop 8.0 pips off his).
2. **Engine 2 on the library weeks:** forecasting the breakout day. GBPUSD Apr 13: the break came Monday, my chain says Wednesday. Mar 2: one day late, no reversal after the breakdown.
3. **Presentation:**
   - EURUSD Wednesday labels overlapping;
   - "new <Day>" LSZ labels over candles;
   - the EURUSD Friday RWL line ends high.
4. **The library as oracle files:** his trades / shape boxes / zone labels per week into `context_management/oracle/library/*.json` (task 23).
5. **Coverage rows NOT BUILT:** the spiderweb entry construction (E2-AIR / Law 5), the WorkingDayMap + 12-step day assignment as objects, the per-DXY-setup mirror lane, the master trade setup, ZoC logic, FA rows.
6. **S3 outside counts** on the library weeks, **S4** audit, **S5** blind test.

**Inputs still NO DATA:** Protocol F (red-folder calendar). DX options OI is blocked by the canon itself.
