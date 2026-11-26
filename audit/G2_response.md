# G2 response — disposition of every finding in audit/G2_audit_engines.md

Written 2026-11-26. States: FIXED (commit) / ANSWERED (canon line or decision row that settles it) / PART (some of it built; what is left is named) / OPEN.
A finding is FIXED only where the code was re-opened for it; anything not re-checked against the v2 engines is OPEN. This file is the work list for S1 / S4; a fresh outside audit re-checks all of it.

Commits: 9e44b34 (batch I) · 2717f06 (Engine 2 v2) · 9d7c72b + 38e6a0b (Engine 3 v2) · fbf932c · 103245f.

## A — Engine 2 (canon steps with no code)
| id | state | note |
|---|---|---|
| A-01 | PART | matrix row 4 (WLS) is evaluated in Step 1 (2717f06); no forward WLS leg / E3 universe row yet |
| A-02 | OPEN | variants (DWL, PRWL, RS) and subtypes are not produced |
| A-03 | FIXED 2717f06 | branch per bound chosen by the Zone Reaction Counter (D-34) |
| A-04 | PART | six_check() in Engine 2, reverses at 4+ disagreements (D-34, D-38); the Engine 3 side of the check is OPEN |
| A-05 | FIXED 2717f06 | pressure_bias() (D-37) |
| A-06 | FIXED 2717f06 | '4H Structural Validation' line |
| A-07 | PART | Engine 2 target() takes the source timeframe; Engine 3 TP Timeframe Law (E3C:347-350) OPEN |
| A-08 | PART | expiry cuts of the day as triggers; red-folder events = NO DATA (no calendar source) |
| A-09 | PART | elapsed consolidation drives timing (D-41); Early / Mid / Late phase -> valid setup types OPEN |
| A-10 | FIXED 2717f06 | _strong_4h_near() |
| A-11 | FIXED 2717f06 | every extension goes through the 6.4 / 6.4.1 / 6.4.2 tables |
| A-12 | FIXED 2717f06 | 'Current Shape ... Anchoring Zone ... ZFP' audit line |
| A-13 | PART | alternative chain built and drawn dotted; its Engine 3 setups held back until the Decision Zone trigger exists (cdf817a) |
| A-14 | FIXED 2717f06 | audit trail per extension (shape, trigger, tier, cumulative) |

## A — Engine 3 (canon steps with no code)
| id | state | note |
|---|---|---|
| A-15 | OPEN | no WorkingDayMap object (supply / demand / deep-demand zone per day); < 65% spill not applied |
| A-16 | PART | 'tested 3x or more' gate (FRESHNESS) on E1 S/D anchors; VIOLATED state and battle-time freshness OPEN |
| A-17 | OPEN | Phase 2.5 / 1-2-3 retest timing |
| A-18 | PART | MoM reversal gate (MOM_REVERSAL); E1 e3_status not read |
| A-19 | OPEN | POI tier rule 1 |
| A-20 | PART | layers 3 and 7 inside _confidence(); layers 1, 2, 4, 5, 6 OPEN |
| A-21 | FIXED f723b0b | Phase 5 score with every E3C:392-414 term except the VLM bonus (no VLM: D-42), inclusion >= 65, HIGH / STANDARD (D-52) |
| A-22 | OPEN | fuel state, mirrorConfidenceScore, ZR-6B switch (stop model in force: D-43) |
| A-23 | PART | Law 7 table present (LAW7); used only as the rule (a) / (b) distances of D-43 |
| A-24 | OPEN | computeGoldenSL fallback (only its 4-36 pip envelope is enforced) |
| A-25 | OPEN | Refined Law 14 no-teleport test on the TP path |
| A-26 | FIXED 9d7c72b | MAX_RRR 15 |
| A-27 | PART | Mechanism A FRONT entry built as the first-contact band of zone-edge setups (D-59, E3C:1060-1066); middle / back entries and the blended RRR OPEN |
| A-28 | PART | RWL hair-miss repair built (E3C:196-197); F1-E recovery-shelf adjust OPEN |
| A-29 | OPEN | Fibonacci Spiderweb anchoring (three contexts) |
| A-30 | PART | internal LQZ rung (F1-C); E1 Step 0.6 key levels not passed to TS-1 |
| A-31 | FIXED 9d7c72b | duplicates 5 pips / conflicts 15 pips |
| A-32 | OPEN | Phase 7.1 twelve-step day assignment |
| A-33 | OPEN | red-folder deferral (no calendar data: NO DATA) |
| A-34 | PART | session window per category; liquidityScore filter OPEN |
| A-35 | PART | swing-scalp reach 30 pips; the other shapes' reach table (GS Law 2) OPEN |
| A-36 | OPEN | anchor hit window, label law BE1-BE12 |
| A-37 | OPEN | Phase 10 cascade mirror (pairs run their own chain translated from DXY in Engine 2) |
| A-38 | PART | reason code on every discard; Phase 12 floor invariants as a final pass OPEN |
| A-39 | OPEN | BoS + flip + retest requirement for reversals |
| A-40 | PART | SS->BS Transition Entry built (D-51, f723b0b); scalp-stack / swing-stack compliance as a gate OPEN |
| A-41 | PART | reinforcement orders pending from the first London premarket after the parent's fill and cancelled at the parent's exit (D-54, E3C:625); the 1-2-3 activation test OPEN |
| A-42 | PART | sizing 50 / 30 / 20 noted; trip-wire, rocket type OPEN |
| A-43 | PART | 8R.10 path mapping in _reinforce(); 8R.5, Phase 11 OPEN |
| A-44 | OPEN | acceptance counts |
| A-45 | OPEN | liquidity zone between entry and stop (tested 2026-11-26 with the E1 sweep zones: fails on his golden #1, #2 - needs the V1 band reading) |
| A-46 | PART | reason codes present; ABORT macro text OPEN |
| A-47 | FIXED | RRR floor 2.5 in a week whose chain is SS throughout (E3C 8.20 'Consolidation week (relaxed) | 2.5') |

## A — Supply / demand map
| id | state | note |
|---|---|---|
| A-48 | OPEN | |
| A-49 | OPEN | |
| A-50 | OPEN | |
| A-51 | OPEN | |
| A-52 | OPEN | |

## B — Engine 2 (code contradicting a canon sentence)
| id | state | note |
|---|---|---|
| B-01 | FIXED 2717f06 | shapes classified on 1H bars per session |
| B-02 | FIXED 2717f06 | matrix rows carry their ZFP conditions (reading of an unmet ZFP condition: D-40) |
| B-03 | FIXED 2717f06 | both bounds HOLD -> SS continues |
| B-04 | FIXED 2717f06 | tree applied per bound with its class and counter |
| B-05 | ANSWERED | the pre-breakout leg is the retest of 6.4.2 ('Consolidation ends in price retesting opposing liquidity'), tagged RWL because the operator tags that day SS+RWL+BS (golden Wed); D-34 |
| B-06 | OPEN | not re-checked in v2 |
| B-07 | FIXED 2717f06 | termination under 25% (D-35); later days carry no designation and are not drawn |
| B-08 | FIXED 2717f06 | chain extended step by step (D-34) |
| B-09 | PART | consolidation length from the canon minima + elapsed sessions (D-41); swing phase D-57; Early / Mid / Late phase -> valid setup types OPEN |
| B-10 | OPEN | not re-checked in v2 |
| B-11 | FIXED 2717f06 | bounds carry source + class; no ZFP on non-IP bounds |
| B-12 | FIXED 2717f06 | MoM bounds go through 6.4.2 |
| B-13 | ANSWERED | E2X:27 'next IP zone' read with P452:2082 'strong IP ... = it holds (valid TP). No IP + standalone MoM = it gets pierced' and E2X:140 'pierce through zone until reaching BoM Liquidity': weak (30%+) MoM zones are passed (D-49, D-50, f723b0b); measured move with structural-extreme cross-reference in measured_move() |
| B-14 | OPEN | not re-checked in v2 |
| B-15 | OPEN | Decision Zone trigger |
| B-16 | FIXED 2717f06 | raw / adjusted day (D-41) |
| B-17 | OPEN | not re-checked in v2 |

## B — Engine 3
| id | state | note |
|---|---|---|
| B-18 | FIXED 9d7c72b | candidates per E2 step and zone, both directions on SS |
| B-19 | PART | depth <= 3, link by TP = entry within 3 pips; shape-link whitelist OPEN |
| B-20 | ANSWERED | E3C:443-446 'TP of ONE = ENTRY of NEXT ... SS -> BS: Range boundary break becomes BS entry'; his #5 TP 101.24 -> #6 entry 101.235 |
| B-21 | FIXED 103245f | IP zones are never entry sources; the LQZ rung / order block at them is (D-46) |
| B-22 | PART | sweep zone still enters WL / RWL at its middle (his golden Friday long); other shapes TS-1 near edge (D-30) |
| B-23 | FIXED 9d7c72b | F1-A on the order block itself |
| B-24 | OPEN | Law 3 (no 4H-edge entry) not enforced as a gate |
| B-25 | FIXED 9d7c72b | rule (b) = inside the close edge of the next step (D-43) |
| B-26 | OPEN | choice (a) / (b) by mirrorConfidenceScore; D-43 / D-47 use (b) first (shields walked nearest first). Checked 2026-11-26 against his 23 golden stops (memory/08): neither rule fits all; the fuel-state definition is in DESIGN_BLUEPRINT_v5.2 16.7 / BUILD_WORKFLOW P3.TURN-07 |
| B-27 | PART | 4-36 pip envelope; Law 4 bands per category OPEN |
| B-28 | FIXED 9d7c72b | zone midpoint with an LQZ inside (D-33) |
| B-29 | PART | strong = near edge + 1 pip, liquidity band = near edge (D-45); weak = far edge only where coded for sweep targets |
| B-30 | PART | reversal after a breakout: TP = first liquidity rung 30+ pips along the way (D-56, GS Law 2), then the sweep-zone / pivot targets; WL targets not re-checked |
| B-31 | FIXED 9d7c72b | TP_NULL discard; range-middle fallback removed |
| B-32 | PART | three entry attempts x three TP attempts on the same anchor; SL re-anchor step OPEN |
| B-33 | PART | rockets: first liquidity step 20+ pips beyond the primary, ladder-step stop, pending from the first London premarket after the parent's fill, cancelled with the parent (D-54); Fib 1.382 / 1.618 placement and the trip-wire OPEN |
| B-34 | PART | both directions at the bounds + inner 1H / 4H zones; scalp stack 30m / 15m (E3C:96) OPEN |
| B-35 | OPEN | |
| B-36 | PART | every capped setup is logged; cap key (pair, anchorBucket, day) OPEN |
| B-37 | OPEN | |

## B — Supply / demand map
| id | state | note |
|---|---|---|
| B-38 | ANSWERED | operator notes Forex_SMC_Notes: 'valid order block: inefficiency gap between the before and after candles' (L-38); D-21 |
| B-39 | ANSWERED | D-21: the operator's own EURUSD BoM box is the 30m mother candle |
| B-40 | OPEN | |
| B-41 | OPEN | |
| B-42 | OPEN | |
| B-43 | OPEN | |
| B-44 | OPEN | |
| B-45 | OPEN | |

## C — Engine 2 (constants / rules with no canon sentence)
| id | state | note |
|---|---|---|
| C-01 | FIXED 2717f06 | no invented ZFP on substituted zones |
| C-02 | FIXED 2717f06 | storyline = side of the most recent standing 4H BoM zone (D-36) |
| C-03 | FIXED 2717f06 | replaced by the per-bound branch table |
| C-04 | OPEN | not re-checked in v2 |
| C-05 | ANSWERED | D-35 (E2X:169 needs a percentage) |
| C-06 | PART | D-40 (whiplash merge, FA 9 counts moves); window length OPEN |
| C-07 | ANSWERED | D-57: swings of two sessions (E2X:21 '1-3 trading sessions'), counted back from the transition (6.4.2) or continuing the swing in progress at the anchor; replaces the one-swing-a-day rule |
| C-08 | PART | sessions from P533 2.2.1; remaining intraday constants OPEN |
| C-09 | OPEN | not re-checked in v2 |
| C-10 | OPEN | not re-checked in v2 |
| C-11 | OPEN | grade() thresholds 0.50 / 0.30 U for the candle-zone bound pool are still in bounds() |
| C-12 | OPEN | |
| C-13 | OPEN | |
| C-14 | ANSWERED | D-29 (6.3 'BS -> RWL -> SS -> BS: complete false breakout cycle') |
| C-15 | ANSWERED | D-39 |
| C-16 | FIXED 2717f06 | undesignated days not drawn |

## C — Engine 3
| id | state | note |
|---|---|---|
| C-17 | OPEN | zone-internal Fibonacci levels still serve as rungs for zones with no liquidity band (GS Law 5 / P533 Step 0.6) |
| C-18 | OPEN | |
| C-19 | ANSWERED | E3C:279-293 golden SL 4-9.5 pips: 4 = the measured minimum of his stops |
| C-20 | OPEN | not re-checked in v2 (the word no longer appears in e3_trades.py) |
| C-21 | OPEN | not re-checked in v2 |
| C-22 | OPEN | not re-checked in v2 |
| C-23 | OPEN | |
| C-24 | FIXED 9d7c72b | F1-D inset on RWL only |
| C-25 | ANSWERED | E3C:96 'SS: Swing Scalps (both directions)': which bound is met first is not designated; per-day orders tested 2026-11-26 and reverted (journal) |
| C-26 | OPEN | |

## C — Supply / demand map and V1 harvest
| id | state | note |
|---|---|---|
| C-27 | ANSWERED | D-21 (P452:639-649) |
| C-28 | ANSWERED | D-13 (smallest symmetric fractal; canon gives no count) |
| C-29 | OPEN | |
| C-30 | ANSWERED | D-23 (P452:694-697; 7 of 7 of his visible labels) |
| C-31 | OPEN | |
| C-32 | FIXED 9e44b34 | harvest at the chart's real tick; Python thickness rebuild removed |

## D — Temporal anchor and hardcoding
| id | state | note |
|---|---|---|
| D-01 | FIXED 9e44b34 | tools/leak_check.py in the pre-commit hook |
| D-02 | FIXED 9e44b34 | post-anchor readers moved to tools/research/superseded |
| D-03 | FIXED 9e44b34 | oracle read moved to tools/research/oracle_diff.py |
| D-04 | FIXED 9e44b34 | |
| D-05 | FIXED 9e44b34 | |

## Count
ANSWERED 14 · FIXED 37 · OPEN 50 · PART 33 (of 134). S1 / S4 need OPEN + PART = 0.

- UPDATE 2026-11-26 (late): B-26 / A-22 (ZR-6B stop choice by mirrorConfidenceScore) -> FIXED by D-73; A-15 (per-day designation) PART: D-70 spill-over (E3C:123), D-71 rocket brackets, D-72 narrative gate per E2 day; E1 Step 9.5 gap scan built (D-68), Step 0.45a / 0.45d built (D-64, 93f8d1e).
