# 23 - ENGINE 2 OVERHAUL: WORKING DESIGN OF STEPS 4-9 (written 2026-11-28 while executing the charter memory/22; update as steps land). First principles from this session's canon + measurements; his Gemini document = context.

## Measured starting point (tools/research/e2grade.py, evidence/e2/grade_step1_baseline.txt)
The product line turns 2-5 times a WEEK; price makes ~35 two-hour turning points a week (~7 a day). HIT (turn at the named zone within +-2 h): golden 5 / 12, four weeks 5 / 40; 'wrong zone' is the dominant miss (29 of 40).
Actual turns that were forecast: 5 / 101 golden, 6 / 430 four weeks. Day tags right 10 / 15 and 44 / 60. So: far too few nodes, and the nodes sit on the wrong zones.

## Where the new code goes (nothing load-bearing deleted or recreated - charter C8)
- e1_tool/e2_data.py (step 3, DONE): profile / zone_volume / delta / yield_spread / positioning / clocks; ext_bars patched by tools/kill_test.py.
- e1_tool/e2_path.py (NEW, steps 6-7): boundary-state classifier + path-node builder. Switch e2_chain.E2_PATH = False. Hook: plutus.daily_anchor, the same place as the M-70 micro hook (which stays, off).
- steps 4-5 (macro lock lifted for these two only): e2_chain.current_shape gets the prior-week terminal state and the continuous classifier behind switches E2_CONTEXT3W / E2_CLASSIFIER (off).
- grader reads ch['nodes'] when present (zone id per vertex) instead of deriving the zone from the price.

## Step 4 - prior-week terminal state (pillar C; canon: P452 6.6 rule 6 day-over-day continuity; FA 9; P533:493 reaction counter)
terminal(pair, monday) from bars closed by the anchor: Friday-close shape in progress (the session-event history current_shape already builds, extended from 6 sessions to the two prior weeks), touches per standing zone in W-2 / W-1
(reaction counts already in Engine 1 - read, not recomputed), the two-pierce recovery lock (FA 9 - exists as n_pierce >= 2), zone freshness (mitigated in W-1 or not). Output feeds current_shape's starting state; realized shape frames of W-1 drawn as hollow white frames inside the R-36 window.

## Step 5 - day-level classifier (pillar A; canon 6.2 matrix; the fallback 'no row matched -> SS' is the deadband)
Continuous classification on Engine 1 strength + causal bar geometry of the last sessions: efficiency ratio (net move / path length), retrace share of the prior leg, alternation count, touch exhaustion, the recovery lock.
Every day's shape anchored to real Engine 1 zone ids. Measure: day tags right (baseline 73% / 67%), chains that say swing scalps all week (9 of 12).

## Steps 6-7 - boundary states + path nodes (pillars B + E; telescoping KCE 2.1; FA 4.4; GS Part 6 ZoC; P533:491-493, :211, :215; 6.4.1)
At an update instant U (day open 17:00, London open 02:00; step 8 adds 05:00 and 10:00), from the ACTUAL price:
 a parent = the day's shape + its container zones (chain); the session leg may not leave the parent unless the parent zone's boundary state is a break.
 b ladder = Engine 1 zones above / below price of the session class (pressure zones + 4H / 1H S/D; 30m inside a swing-scalp container), same-class matching (FA 4.4).
 c last zone event since the previous update (closed 30m candles): zone met + what happened (rejected / broken / consolidating / none) -> direction (held -> back; broken -> on; none -> leg in force continues, rule 6).
 d boundary state at the target zone - one of five, exhaustive, from measurable inputs:
   CLEAN_BREAK   pressure zone ZFP > 45 (6.4.1) or 3+ reactions (P533:493), or a MoM zone in the way of a breakout leg (P533:491), low volume inside   -> node beyond the zone, next ladder zone
   PIERCE_R      volume vacuum at the near rim + liquidity (sweep level / rung) just beyond the far edge (GBP/USD: L-50)                                  -> node at that liquidity beyond the far edge, then back
   WICK_RWL      strong hold: ZFP < 20 or unmitigated BoM, with a defended near edge (V1 rung on it / option wall of 850M+ there)                        -> node at the near edge, immediate turn
   BODY_CONSOL_R holding zone with a high-volume node inside and balanced delta                                                                         -> node mid-zone at the node, dwell (3+ candles), then out
   BODY_WL       any other holding zone                                                                                                                  -> node at the zone's inner level (rung / midpoint), turn
 e time of each node = distance / the pair's own causal session pace (median net displacement per hour of that session over the two prior weeks); clock instants (e2_data.clocks) when a transition falls on one.
 f node = {time, price, zone id, state, timing mode, evidence}; the line = the nodes; drawn orange.
CALIBRATION (locator, build weeks only - never the golden / checkpoint / fresh test weeks): every first touch of a zone -> which of the five outcomes the candles showed -> which inputs separate them. Rules stay canon-grounded; the table shows where the encoding fails.

## Step 8 - fixed-time updates 05:00 and 10:00 NY (line only): steps 6-7 re-run from the actual price; frozen past.   Step 9 - pairs: DXY direction / shapes / clocks, own zones + own data per pair.

## UPDATE after the calibration (memory/08 last section) - the builder's decisions (e1_tool/e2_path.py)
HOLD / BREAK at a zone on the path: BREAK when the S/D zone has 3+ taps (P533:493) or the pressure zone's ZFP > 45 (6.4.1) or the parent shape's leg is a breakout in that direction and the zone is not its target; else HOLD.
NODE when it holds (by width / timeframe, the strongest separator): under 8 pips -> the liquidity within 10 pips beyond the far edge (PIERCE_R), else the far edge; 8-15 pips -> the far edge (BODY_WL); 15+ pips or a 4H S/D zone -> the zone's inner level with dwell (BODY_CONSOL_R).
WICK_RWL (node at the near edge) only for a stacked zone (3+ overlapping) met in the New York morning. LADDER = drawn pressure zones + 4H / 1H / 30m S/D of the side being met. TIME = distance / the pair's causal session pace.
