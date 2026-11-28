# 16 — THE PLAN FOR M-67 / M-68 (written 2026-11-27 ~23:10 UTC; the operator is asleep; THIS FILE GOVERNS THE WORK UNTIL HE SAYS OTHERWISE)

He: "once we have written down the plan, obey the plan verbatim, religiously, do not fucking deviate from it" (M-67). "Do not fuck anything up while I'm gone ...
Don't regress. Get better. Optimize everything." (M-68). Every step below is done in this order. A step is only changed by writing the change into this file first,
with the reason, before doing it (section 10).

## 1. Goal (L-62, his words in memory/12 M-67 / M-68)
Any 2026 week from February to now, DXY / EURUSD / GBPUSD: >= 80% win rate on FILLED trades, consistently across weeks, WITHOUT fewer trades -
each pair-week has 5-8 high-probability trades and they must be caught ("2 trades at 80% = cheating"). Engine 2 micro-architecture first: shape transitions
predicted to within one 30-minute candle; the forward line traces the actual price path (target ~95% of the line chart of the candles); clear vertices at the turns;
an EMA is only a visual reference - an EMA coded as Engine 2 is FORBIDDEN. Then Engine 3 downstream. Verify with Pinebox frames + a backtest of 8 weeks x 3 pairs with per-week stats.

## 2. Locks (immutable; enforced where a machine can enforce it)
- ENGINE 1 = e1_tool/e1_data.py, e1_pillars.py, e1_sd.py, e1_ip.py, e1_v1.py, e1_pine.py + indicator/plutus-vision-v1.sealed.pine. SHA-256 of each in tools/locks/E1.sha256;
  the pre-commit hook refuses a commit that changes any of them (tools/locks/check_e1.sh). No edit of any kind (his order: "Do not touch anything about Engine 1 at all whatsoever").
- MACRO ARCHITECTURE (no deletion, no recreation, no change of behaviour when the new switches are off):
  plutus.run / engines / daily_anchor (trading-day-open confirmation, alternative activation, London-open zone update, carry-over, no copies, Phase 10 re-entry, Law-27 flow, the <= 11 cap);
  e2_chain.build and everything it calls (current_shape, bounds, branch, target, after_bs, chain, alternatives, day decomposition, _session_path, _ladder_path);
  e3_trades.build / _build / _cands and the phases they run (entries, stops, targets, confidence, cascade, reinforcement, pine, pine_state);
  the Pine assembly; tools/leak_check.py; the flags already set (PHASE10_REENTRY, FLOW27, REANCHOR_DRAW, REANCHOR, DAY_CONFIRM, SESSION_PATH, SPEED_4H_HOURS, SPAN_BOXES, ...).
- What a MICRO change is (the only kind allowed): a NEW function that ADDS to an engine's output (a finer path inside the day boxes Engine 2 already draws; extra legs; extra
  Engine 3 candidates that then pass through the EXISTING gates), or a reading of a canon range that the code leaves open (e.g. "1-2 Fib levels back"), each behind a switch
  that defaults OFF until section 6 passes, each with its canon line and a D-row in memory/03.

## 3. Forensic findings (evidence/m67/e2forensic_15maps.txt, tools/research/e2forensic.py; locators, never verdicts)
- Golden week (in-sample): 20 drawn / 18 filled / 18 TP / 0 SL. Other 12 maps (04-13, 04-20, 05-18, 10-05 x 3): 30 drawn / 20 filled / 10 TP / 10 SL = 50%; 2.5 orders per pair-week.
- The macro day tags are mostly right (other maps 44 / 60) - but 14 of the 15 other pair-weeks are forecast "SS range" all week, and inside those ranges price made 90 visible
  moves (1H zigzag >= 30 pips lasting >= 3 h; ~7.5 per pair-week, his "5-8") of which 7 were caught by a winning order. The macro forecast is not what loses; the MICRO layer is missing:
  Engine 3 only trades the two range bounds (TP = the far bound) and Engine 2's line inside the box is a generic bound-to-bound swing per session.
- The line against 30m closes: golden 60% within 10 pips (mean miss 10.5 p), other 46% (18.3 p); 2h direction agreement 54% / 45%; of 160 30m turns on the other maps the line has a
  vertex of the same kind within one candle at 6 and within three at 12.
- Losses: breakout weeks mistimed (04-13: the break came Monday, the chain timed it Wednesday -> 0 TP / 3 SL); range orders at an inner zone with the TP at the far bound.
- The missing canon layer is named in the coverage matrix: E2-AIR (FA 2.4 / 4.5 / 4.6, Fibonacci Spiderwebs PDF items 2-5, GS Law 5) = NOT BUILT, plus the Sequential Zone Path
  (P533:215, :493, :2266-2270 'Price ALWAYS sweeps liquidity zone by zone ... it NEVER skips a zone. The zones that have NOT been retested yet WILL be retested - this is the entry point').
  His golden trades are spiderweb trades (memory/08 'THE FIBONACCI SPIDERWEB IS HOW HIS TRADES ARE BUILT'): entry at 0.5 / 0.618 / 0.786 of a range between two Earth points, SL 1-2
  levels back, TP one range height from the entry (wormhole), PDF buffers.

## 4. Engine 1 assessment (his ask: flaw / fix / regression risk / blast radius) -> LOCK, NO CHANGE
- Known imperfections: zone density / bunching (count 11 side condition 8 / 12 PASS; joined zones cover a large part of the range), so many E1 objects stand near every turn.
- Any change to E1 moves Engine 2's bounds and targets and every Engine 3 entry / stop / TP, and the golden matches; blast radius = the whole product; regression risk = high.
- What the micro layer needs from E1 is already there (zones, rungs, reaction counts, BoM / MoM, ZFP). Decision: Engine 1 is locked as he ordered; nothing in this plan edits it.

## 5. Build steps (in order; each behind its own switch, default OFF until section 6 passes)
M0  INSTRUMENT (no engine change). One command = the 8-week dev backtest: tools/research/devset.sh -> per pair-week rows (drawn, filled, TP, SL, open, never filled, win rate,
    visible moves, caught) + per-pair and total rows + line metrics (e2forensic). Baseline recorded in memory/05 before M1.
M1  E2-AIR SPIDERWEB (FA 2.4 / 4.5; PDF items 2-5; GS Law 5). New module e1_tool/e2_air.py, called per trading day at its London open (02:00 NY) with bars closed by then only:
    item 4 scalp web on 15m (anchors = the nearest non-surge swing high / low inside the current 15m consolidation range, direction = trend, entry = nearest Fib level + 0.5-1 pip,
    SL 1-2 levels back + 1 (2-3) pips, TP = wormhole of the entry level - 1.5-2 pips); item 3 swing web on 1H for BS / WL days (4H anchors 'deepest + most recent, BoM anchors');
    item 5 mid-swing (30m, nearest swing high / low of the same trading day, SDL first). First as a locator (tools/research/airweb.py) to pick each open reading by the dev set,
    then the same functions in e2_air.py. Each reading = a D-row with the PDF line.
M2  E2 MICRO PATH. The day's line inside the day box Engine 2 already draws follows the day's web: London open position -> entry level -> wormhole TP, vertices at the levels,
    session timing of P452 6.6 rules 1-7, the sequential zone path (every unretested zone between is a vertex / minor TP). Switch e2_chain.MICRO_PATH. Box / chain untouched.
M3  E3 MICRO TRADES. Each micro leg (entry -> TP) becomes an Engine 3 candidate through the existing gates (Law 2 reach, Law 3, Law 4 shield, RRR floor, confidence >= 65,
    Law-27 flow, no duplicates, <= 11). Switch e3_trades.MICRO_TRADES. An existing order for the same move wins (no duplicate, L-52).
M4  TRANSITION TIMING (PDF item 3 'If 4+ SS trades have been presented over 1-2 days - NY session = BS begins'; P533:485 / PDF 'AFTER 2 STRONG PIERCING SWING MOVES - EXPECT 1-2 FULL DAYS
    OF HTF CONSOLIDATION') applied to the micro path / candidate timing only (the macro chain stays).
Then iterate M1-M4 on the dev set (section 7) until the 8-week average >= 80% with >= 5 filled per pair-week, or the night ends; report honestly either way.

## 6. Gates - a switch goes ON only when ALL hold (checked in this order, results in memory/05)
G1 golden week: every golden order and its result unchanged (tools/research/replay_maps.py daily on the golden 3 maps: still 18 filled / 18 TP / 0 SL; oracle_diff matches unchanged); added
   golden orders are allowed only if they win.
G2 leak check: tools/leak_check.py exit code 0 on golden DXY / EURUSD / GBPUSD + one dev week (exit code read directly, never through a pipe).
G3 dev set: total win rate up AND filled count not down; no pair-week worse by more than one losing trade.
G4 crash sweep: the daily build runs on every dev and golden pair-week without an error.
G5 locks: tools/locks/check_e1.sh clean (no Engine 1 byte changed).
G6 pixels: Pinebox frames rendered ONE AT A TIME, the expectation written in memory/07 first, every frame opened; golden 3 pairs + at least one dev week per pair.

## 7. Weeks (seeded draw random.Random(67) over the sidecar weeks, excluding the golden week and the 4 measured weeks; recorded 2026-11-27)
- DEV (8): 2026-03-02, 03-23, 04-13, 04-20, 05-18, 08-31, 09-21, 10-05 (x DXY / EURUSD / GBPUSD = 24 pair-weeks). All readings are chosen on these.
- HELD-OUT (4): 2026-03-30, 05-25, 07-13, 09-28 - run ONCE, at the end, with the final switches; never inspected before.
- Golden 2026-07-06 = the regression gate (G1), not a dev week.

## 8. Metrics per pair-week (printed, never quoted as a verdict on the strategy)
drawn / filled / TP / SL / open / never filled; win rate = TP / (TP + SL); visible moves (1H zigzag 30 p, 3 h) and how many a winning order caught; RRR of every filled trade;
line: closes within 10 pips, mean miss, 2h direction agreement, 30m turns with a vertex within 1 / 3 candles.

## 9. Morning report (<= one screen; numbers from the backtest he ordered)
Per-week table (8 dev weeks x 3 pairs + held-out), the switches adopted and their D-rows, the golden week unchanged, frames (all three pairs, whole week, one fitted frame each),
the RRR of every charted golden trade + average per pair (M-67 ask), the Engine 1 assessment (section 4), what is still short of 80% and where.

## 10. Changes to this plan (append only: date, what, why)
- 2026-11-27 ~23:45 UTC. G3 for a DRAWING-ONLY switch (M2 / D-147 changes only chain['segments'], the orders are identical by construction - devset shows the same 61 / 36 / 15 / 21 on dev and 20 / 18 / 18 / 0 golden): the gate is the line metrics of section 8 improving on the dev set AND not getting worse on the golden week, plus identical orders. Why: G3 as written ('win rate up') cannot move for a change that does not touch Engine 3; the trade gate applies to M3 / M4.
- 2026-11-27 ~23:45 UTC. M1 result: every mechanical reading of the Spiderwebs PDF tried (items 3 / 4 / 5, anchors Asia / 15m swings / same-day 30m / 4H swings, trend 4H / 30m structure, 1-2 levels back) lands at 10-36% on the dev set (golden 0 / 9) - not adopted, recorded in memory/05; M1 stays a locator (tools/research/airweb.py), no e2_air.py module is written (nothing to adopt).
- 2026-11-27 ~23:45 UTC. M3 result (locator scratchpad loc/microtrades.py): the micro legs of M2 are <= 30 pips on swing-scalp days; with a Law-4 stop of >= 5 pips every candidate falls under the 3.0 RRR floor (24 dev maps: 0 candidates pass) - M3 as written produces no trade; not built into Engine 3.
- 2026-11-28 ~00:00 UTC. D-148 (one trade per move) is adopted although G3 as written ('win rate up AND filled count not down') does not hold: it is a correction of how the existing orders are COUNTED and DRAWN under the operator's ruling L-52 ('explicitly forbidden and banned'), not an optimisation - the 2 voided TPs were the second fill of a move already traded. Its gates: golden unchanged (0 voids), Pine renders (frames), replay identical with the switch off.
- 2026-11-28 ~00:30 UTC. M4 result (locator): swing-scalp trades filled in a NY session after 4+ swings (15 / 20 p) in the prior 48 h - TP 3 SL 3 / TP 2 SL 2 - the same split as all others (TP 14 SL 12); the PDF's 'NY session = BS begins' does not separate them on my data - not built. M2 extra readings tried: MICRO_ACTIVE (composite-day legs by the active chain step) no effect - kept OFF; MICRO_ANCHOR_HOURS (2, 8, 10) under test.
- 2026-11-28 ~00:20 UTC. D-147b: session anchors (2, 8, 10) adopted after the same gates (devset dev 59% / 13.1 p / 96 turns; golden 67% / 9.4 p; orders identical; segment leak check; frames).
- 2026-11-28 ~00:55 UTC. ADDED M5 (locator only, no engine change): his winning trade library as the oracle for non-golden weeks (L-48 / L-55 'Optimize everything based on this'; open task 23) - read his marked trades (pair, time, entry, SL, TP, zone labels) into context_management/oracle/library/trades.json, run the product (daily, final switches) on the library weeks, and list per trade whether my build emitted an order within 3 pips of his entry and of his stop / TP, and what it emitted instead. Why: every mechanical reading of the anchor / zone choice measured at chance; his own non-golden trades show the choice directly. Library weeks without per-day V1 caches (GBPUSD needs DXY + EURUSD for the cascade): 2026-02-02, 02-09, 02-16, 02-23, 03-09, 03-16, 04-06 - harvested with output discarded.
- 2026-11-28 ~01:30 UTC. M5 reading from his two printed webs (drawn on the consolidation range; breakouts to 1.618 / 2.618) tested mechanically (tools/research/m67_locators/rangeweb.py; PDF item 2 'Deepest + Most Recent'): dev 12-26%, golden 0 / 9-14 - not built. The blocker stays his timing / anchor choice.
