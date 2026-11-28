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
Sent to the operator in chat 2026-11-28. M-70: example + side-by-side requested before approval.

## THE EXACT TEXT SENT IN CHAT (2026-11-28, logged verbatim on the operator's order M-70)

I've stopped and put the engine back to the checkpoint that scored 50% on the 4 random weeks. All of last night's changes are reverted, and the spiderwebs are dropped. The golden-week output is identical to that checkpoint, and the 4 weeks replay at the same score: 30 orders, 20 filled, 10 TP, 10 SL. Engine 1 stays locked, as you ordered.

Engine 2 plan

Where Engine 2 stands at the checkpoint (measured on 30-minute candles):

| | 4 random weeks | Golden week |
|---|---|---|
| Day shape right | 44 of 60 (73%) | 10 of 15 |
| 30m closes within 10 pips of the line | 46% | 60% |
| Average miss | 18.3 pips | 10.5 pips |
| 30m turns with a line vertex within one candle | 6 of 160 (4%) | 2 of 34 |

What's broken inside Engine 2:
1. Shapes are scheduled in whole sessions, so a turn can only land on a session boundary, never on the 30-minute candle where it actually happens.
2. Inside a day box the line follows a template: London goes to the nearer bound, NY to the other. It ignores every zone inside the box, so it fits the candles no better than a flat line.
3. A shape change the chain didn't forecast (the Apr 13 Monday breakout) is only picked up at the next trading-day open, up to a day late.
4. Each day's first leg simply heads for the nearer bound; there's no pressure reading.

What I'll build. All of it is Engine 2 micro-level and comes from the canon. The macro chain (shapes, bounds, alternative chains, day boxes, daily anchoring) stays exactly as it is.
1. Catch unforecast shape changes within one candle (P533 6.6 Step 4: the Decision Zone and its alternative chain). The alternative chain is already worked out at each anchor. It takes over the drawn line at the 30-minute candle that closes beyond the Decision Zone, instead of at the next day's open. This fixes problem 3.
2. Time each forecast transition to its trigger candle. Sources: P452 6.6 session rules, the 10:01 NY spring release, "NY swings start after 2:30 PM", "DXY breakout doesn't start until 3pm", and that day's option cuts, Treasury auction closes and EIA release. Each forecast transition goes on the 30-minute candle of its trigger time instead of a session boundary. This fixes problem 1.
3. Walk the zones inside each box. Sources: "price sweeps liquidity zone by zone, never skips a zone", the reaction counter (0 / 1-2 / 3+ reactions), unmitigated BoM zones always react, the MoM decision tree, and the Law 2 reach for each shape. The line walks zone to zone and turns or breaks through at each zone by that zone's rule. Every turn becomes a vertex. This fixes problem 2.
4. Set each leg's direction by pressure (candle size, wicks, the flat side of a triangle, with the 4H storyline as tiebreak). London breaks the Asian-range bound that the pressure says will fail. This fixes problem 4.
5. Apply pair mechanics (FA 10 and your L-50): GBP/USD breaks through supply/demand to the liquidity beyond; EUR/USD turns inside the zone.
6. Then feed Engine 3 from the improved line: entries at the zones where the line turns, take-profit at the next turn, through Engine 3's existing gates.

How each step is checked. After every step I rerun the backtest with the same metrics as the table:
- day shapes right;
- 30m closes within 10 pips of the line;
- average miss;
- turns with a vertex within one 30-minute candle (your "shift at 9:30, predicted anywhere from 9:00 to 10:30" window);
- then Engine 3's win rate and trades per pair-week.

The test set is the 4 checkpoint weeks plus 4 new random weeks, with 4 held-out weeks run only once at the end. A step stays only if:
- the golden-week trades are unchanged;
- the leak check passes;
- no metric gets worse;
- frames for all three pairs are rendered and checked.

The order is 1 -> 2 -> 3 -> 4 -> 5, then 6. The target is yours: the line on 90-95% of the 30-minute line chart, with turns within one candle.

Approve this or tell me what to change. I'm building nothing until you answer, and then I'll follow it exactly. The plan is also saved in memory/17_PLAN_E2.md.

## M-70 (2026-11-28): 'This sounds good, this makes sense' - not yet approved; he asked for a practical example of the exact changes, tested, with a side-by-side golden-week visual (previous E2 vs new E2). Built behind the switch e2_chain.E2_MICRO (default OFF): the product is unchanged until he approves.
