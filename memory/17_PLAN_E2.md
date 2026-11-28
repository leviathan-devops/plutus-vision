# 17 — ENGINE 2 MICRO-INFRASTRUCTURE PLAN (M-69, 2026-11-28) — AWAITING THE OPERATOR'S APPROVAL; NOTHING IS BUILT BEFORE IT

Context: M-69 / L-64 rejected everything done after the M-67 checkpoint; engine code restored to 9a40e9b (golden output byte-identical; 4 random weeks 30 drawn / 20 filled / 10 TP / 10 SL = 50%).
Spiderwebs are out. Engine 1 stays locked (tools/locks). The macro chain (shapes, bounds, alternatives, day boxes, daily anchoring) stays as it is.

## Where Engine 2 is at the checkpoint (evidence/m67/e2forensic_15maps.txt, 30-minute candles)
| | 4 random weeks (12 maps) | golden |
|---|---|---|
| day shape right | 44 / 60 (73%) | 10 / 15 |
| 30m closes within 10 pips of the line | 46% | 60% |
| mean miss | 18.3 pips | 10.5 pips |
| 30m turns with a line vertex within one candle | 6 / 160 (4%) | 2 / 34 |

What is wrong inside Engine 2:
1. Transitions are scheduled in whole sessions (a shape lasts N sessions) - a turn can only fall on a session boundary, never on its 30m candle.
2. Inside a box the line is a template (London to the nearer bound, NY to the other); it ignores every zone inside the box - no better than a flat line.
3. A shape change the chain did not forecast (Apr 13 Monday breakout) is noticed only at the next trading-day open - up to a day late.
4. The direction of each day's first leg is 'toward the nearer bound' - no pressure reading.

## The micro infrastructure (each part from the canon)
1. Transition detection on 30m closes (P533 6.6 Step 4, :1895 Decision Zone + alternative chain): the alternative computed at the anchor takes over the drawn path at the 30m candle that closes beyond the Decision Zone, not at the next day's open. (failure 3)
2. Transition clock (P452 6.6 rules 1-7; P533:691 10:01 Spring Release; P533:710 'NY swings ... after 2:30 PM ET'; FA:648 'DXY ... breakout doesn't start until 3pm'; 6.6 Step 5(d) the day's option cuts, Treasury auction closes, EIA release): each forecast transition placed on the 30m candle of its canon trigger time. (failure 1)
3. Zone-by-zone path inside each box (P533:215 / :493 'sweeps liquidity zone by zone ... never skips a zone'; :209-212 reaction counter 0 / 1-2 / 3+; :491 BoM unmitigated reacts; FA 8 MoM decision tree; GS Law 2 reach per shape): the line walks the Engine 1 zones inside the box, turning or piercing at each by the canon rule for that zone; every turn a vertex. (failure 2)
4. Leg direction (P533:497 pressure reading: bigger candles, wicks, triangle flat side; 4H storyline tiebreak; P452 rule 2 'a bounding zone from the Asian SS range fails ... as London desks open'): the first leg goes toward the Asian-range bound the pressure says will fail. (failure 4)
5. Pair mechanics on the path (FA 10; L-50): GBP/USD pierces S/D to the liquidity beyond; EUR/USD turns inside the zone.
6. Engine 3 reads the micro path (after Engine 2 passes): orders at the zones where the path turns, TP at the next turn, through the existing Engine 3 gates.

## Measurement and gates
Backtest (tools/research/devset.py) after every step: day shapes; 30m closes within 10 pips; mean miss; turns with a vertex within one 30m candle (his '9:30 -> between 9 and 10:30' window); then Engine 3 win rate and trades per pair-week.
Weeks: the 4 checkpoint weeks + 4 more random weeks; 4 held-out weeks only at the end. A step stays only if the golden trades are identical, the leak check passes and no metric gets worse; frames rendered and opened for all three pairs.
Order: 1 -> 2 -> 3 -> 4 -> 5, then 6. Target = his: the line on ~90-95% of the 30m line chart, turns within one candle.

## Status
Sent to the operator in chat 2026-11-28. Waiting for approval / changes.
