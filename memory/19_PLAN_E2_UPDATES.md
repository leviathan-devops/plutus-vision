# 19 - ENGINE 2 PLAN v3 (M-72, 2026-11-28): scheduled intraday updates of the Engine 2 LINE - PLAN ONLY, sent in chat, NO EDITS until he approves (L-67)

## His frame (M-72, verbatim in memory/12)
Target 80-85% first, replicated over multiple weeks, then reassess. Dynamic line adapted to the actual price action, by re-applying the approved daily London-open re-adaptation (L-53) to Engine 2's micro
architecture session by session - LOW frequency (2-4 a day, never more than 6), stable ('earth density'), no EMA follower, as few restarts as possible. E1 zone to E1 zone. Engine 1 is a structure, not a level count.

## Corrections of my last message (facts)
- 'Range bound' = MY word for the two OUTER Engine 1 zones of a swing-scalp day box (canon 6.5 ceiling / floor; e2_chain.bounds + _session_path). The line does go E1 zone to E1 zone - but only between those two, skipping
  the zones between: SS boxes median 88 p tall on the 4 weeks (56 golden; up to 146-218), median 3 pressure / 4H / 1H zones wholly inside; real session move 11-17 p net; NY leg drawn 40 p vs actual 14 p. FLAW IN MY CODE.
  Golden DXY Mon: floor MID-RANGE SUPPORT 100.724-100.815, ceiling UPPER RESISTANCE 101.199-101.262; line 101.025 -> 101.199 -> 100.815; candles turned at 101.145 (1H supply 101.027-101.153 under the 30m BoM supply) and 100.838 (1H demand 100.825-100.851).
- 'A level every 3 pips' flattened the map (counted rungs, bands, sweep levels, strikes, 15m / 30m zones as equals, +-3 p each). By class, inside a ~111-pip week range (15 maps): pressure zones 2.8, S/D 4H 0.7, 1H 2.4, 30m 3.3, 15m 3.1,
  V1 1H rungs 6.5, V1 4H bands 5.1, sweep levels 5.3, strikes 2.1. Session-scale zones (pressure + 4H / 1H S/D) = about one per 18-19 pips = the size of a real session move.

## Research he asked for (evidence/m72/gap_hours.txt; tools/research/m71_gap/gap_hours.py; candles only; recent = Aug 3 - Nov 6 2026, check = Feb - Jul)
- Hour candle size (DXY / EURUSD / GBPUSD pips, recent): quiet 17:00-19:00 (3-6 / 6-7 / 7-11) and 15:00-16:00; London burst 02:00-04:00 (9-11 / 11-14 / 15-16, peak 03:00-04:00); NY burst 08:00-11:00 (16, 13, 13, 11 / 18, 16, 16, 14 / 22, 19, 20, 17; peak the 08:00 hour).
- Update sets: no-forecast line (flat restart) | perfect legs, recent / check:
  17+02 (today) 55 / 47 | 79 / 69;  17/02/05 64 / 54 | 84 / 76;  17/02/10 62 / 54 | 83 / 76;  17/02/05/10 68 / 59 | 87 / 80;  17/02/08/10 65 / 56 | 87 / 80;  17/02/05/12 71 / 62 | 87 / 81;
  17/02/05/10/13 74 / 64 | 90 / 84;  17/02/05/08/10/13 75 / 66 | 92 / 86.

## Proposed design (for his approval)
1. WHAT updates: only the Engine 2 LINE from the update moment to the end of that trading day. Frozen: everything already drawn, Engine 1 zones, day boxes, shape chain, orders (those keep the approved once-a-day cycle).
2. WHEN: fixed times only, 4 a day: 17:00 (day open, exists), 02:00 (London open, exists), 05:00 (after London's first three hours), 10:00 (NY cut / 10:01 release). No market-triggered updates. Optional 5th at 13:00 only if the test shows the need.
3. HOW each update draws: (a) read the 30m candles closed since the last update: which Engine 1 zone price met last and what it did there - REJECTED (touched, 30m close back out on the side it came from) / BROKEN (30m close beyond the far edge) / nothing met;
   (b) direction from that event (rejected at supply / resistance -> down; at demand / support -> up; broken -> on through; nothing -> the leg in force continues, P452 rule 6);
   (c) one leg from the actual price to the NEXT Engine 1 zone that way, same timeframe class (FA 4.4 4H->4H, 1H->1H, 30m->30m; at most two up), hold / fail from the zone's own Engine 1 properties (BoM / MoM, reaction count, ZFP, pressure degree);
   (d) repeated touches of the same zone (his 2-3 vertex hits before a surge) = one state 'at the zone', not flips.
4. MEASURE: tools/research/devset.py line metric always next to the no-forecast line at the same update times; leak check at every update instant; orders identical; switch default off until he approves the result.
5. ORDER: step A the restart at the 4 times with the product's existing legs (expected ~ the no-forecast level); step B next-zone legs; step C event direction; each on golden + the 4 weeks, then 4 new weeks; report after each.
Honest arithmetic: with 4 updates a day perfect legs give 80-87%; 80-85% therefore needs nearly every leg right, or a 5th update (perfect 84-90%).

## v3.1 (2026-11-28, after M-73 / M-74 / M-75) - THE FULL COMPONENT LIST for Engine 2 (sent in chat; still PLAN ONLY, not approved)
'Step B' (30m telescoping inside the swing-scalp box) was one piece. Simple architecture only: fixed-time updates; market-triggered updates and the scalping engine are BENCHED (design/BLUEPRINT_LIVE_TRIGGERS_v1.md, design/BLUEPRINT_SCALP_ENGINE_v1.md).
| # | Component | His source | Coded today | To build |
|---|---|---|---|---|
| 1 | Fixed-time restart of the line (17:00 / 02:00 / 05:00 / 10:00 NY), line only, past frozen | M-72, L-53 | 17:00 only (02:00 in the M-70 example, off) | yes - step A |
| 2 | Telescoped containers, parent constrains child: week (4H) -> day (1H: the day box's ceiling / floor zones) -> session leg (30m zones inside); a child leg does not leave its parent unless the parent's zone has failed | KCE 2.1 / 3.3 / 6A; SMC Top Down | no containment; E2 never reads 30m / 15m zones | yes - step B |
| 3 | Leg end = the NEXT zone of the same timeframe class; hold / fail from the zone's Engine 1 state (BoM / MoM, reactions, ZFP, pressure degree, Refined) | FA 4.4; GS Part 7 / 8; P533:491-493 | outer zones of the day box; class matching only for breakout targets | yes - step B |
| 4 | Direction from what happened at the last zone since the previous update: held -> back toward the opposite zone; failed -> on to the next defensive zone / the opposing BoM; plus the lower timeframe's structure shift at a higher-timeframe zone and alignment with the layer above; pairs follow DXY | GS Part 6 (ZoC); SMC Market Structure + Top Down; M-72 | nearer zone / template; my M-70 pressure reading (57-60%) | yes - step C |
| 5 | Shape transition at an update: the day's ceiling / floor zone failed since the last update -> the alternative chain's shape takes the line at THAT update (today: next trading-day open) | P533:1895; GS Part 6 | next day only | yes - step C |
| 6 | Repeated touches of one zone (2-3 vertex hits before a surge) = one state 'at the zone' | M-72 | not modelled | yes - step C |
| 7 | Session roles and speed: London zone-to-zone, 08:00-10:00 breakout / whiplash triggers, NY swings; moves take longer than expected; two piercing moves -> 1-2 days of swing scalps | GS Part 10; P533 2.2.1; FA 9 | session clock in the template; FA 9 in the chain | reuse, no new rule |
| 8 | The day-level forecast itself (day shape right 44 / 60; candles stay inside the day box on 37 / 65 days): a wrong parent gives a wrong child | - | macro chain (locked) | NOT in this plan - measured after steps A-C, reported |
| 9 | Measurement: line metric next to the no-forecast line at the same instants; leak check per instant; orders identical; switch off until approved | L-65, L-67 | devset + leak tools | each step |
