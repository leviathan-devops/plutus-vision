# G1 count 7 — outside reviewer (brief: audit/G1_brief7.md)

Reviewer did not build the tool and did not read earlier counts, audit/G2_*, memory/ or e1_tool code. All 36 frames in evidence/s3g/ were opened (_zones first per map, then _all and _week). Facts files were used for exact prices/times only; 1H/15m bars were read with `e1_tool/e1_data.bars()` to measure swing extremes, times and closes.

## Counting rules applied (so anyone can recount)

Units: pip = 0.0001 (EURUSD, GBPUSD), 0.01 (DXY). Times UTC. Forecast window = Mon 06:00 UTC (02:00 NY anchor) to Fri 21:00 UTC. Day = 21:00 UTC to 21:00 UTC (Mon starts at the anchor), the same as the facts files' day H/L/C.

Turning points and swings come from a zigzag on 1H highs/lows:
- **Reaction swing** = zigzag(15 pips): a turn of at least 15 pips.
- **Obvious turning point / obvious move** = zigzag(30 pips). A leg that lasts under 3 hours (a 1-2 hour spike-and-back) is not a tradeable move. It is merged into its neighbours, keeping the more extreme pivot. The last point of the week counts as a turning point only if a 30-pip reversal confirmed it.
- **Obvious trades (non-anchor maps)** = every zigzag(30) leg that is left after the merge. These were listed from the _zones frame and bars before the setups were looked at. Every leg starts and ends at or near an Engine 1 zone, because the zones are dense. For 2026-07-06 the obvious trades are the operator's trades in golden_week.json; any trade whose entry was touched only before Mon 06:00 UTC is dropped. For DXY 2026-04-20 they are the operator's two trades named in the brief.

E1:
- **Zone** = a labelled box (top-level line in the facts file). Its area is the box plus its parts' boxes, plus the sweep reach for a top-level sweep zone. Part sweep reaches are not added. Tolerance is 3 pips (DXY 0.03).
- **Reached** = some 1H bar of the window traded within the zone area ±3 pips.
- **REACTED** = either a reaction-swing pivot (zigzag 15) has its extreme inside the zone area ±3 pips (pivots on the anchor bar count), or there are at least 4 consecutive 1H closes inside the area ±3 pips (consolidation). Otherwise the zone is **PIERCED**.
- **Missing** = an obvious turning point with no zone area within 3 pips.
- **E1 %** = reacted / (reached + missing).
- The rule's qualifier ("none bloated, bunched, floating or missing") is reported as PASS/FAIL. It is not folded into the %. Thresholds:
  - bloated: zone area taller than 20 pips;
  - bunched: two zone areas overlap or sit within 3 pips of each other;
  - floating: a zone more than 30 pips from any price of the week.

E2 (day box + yellow line vs that day's candles):
- **SS** RIGHT if the day's H and L stay within the forecast range box ±10 pips and the day has at least one swing reversal of 15 pips or more. Otherwise WRONG (a breakout of more than 10 pips out of the box = WRONG).
- **BS dir** (alone, or as the last part of `X+...+BS`) RIGHT if the day has a leg of at least 20 pips in that direction that crosses a whole Engine 1 zone, and the day closes at least 10 pips in that direction from its open.
- **`BS+WL+RWL` / `BS+RWL`** RIGHT if a BS leg of at least 20 pips is followed in the day by a reversal of at least 20 pips.
- **WL/RWL dir** RIGHT if a spike in the opposite direction is rejected by a leg of at least 20 pips in the tag's direction, and the day closes that way.

E3:
- An obvious trade is CAUGHT when a setup of the same direction meets all of these:
  - it filled at that turn, before the move ended;
  - its entry is within max(10 pips, 25% of the leg) of the turn's extreme (operator trades: same turn, and entry in the same Engine 1 zone or within 4 pips; DXY 04-20: entry within about 3 pips, used as up to 4);
  - its TP was hit before its SL.
- A position opened at an earlier turn does not count as catching a later turn.
- These do not count: still open at week end, void, not filled.
- Stop-outs come from the facts file (15m) and were checked against the frames.

## DXY 2026-07-06 (anchor week)

Obvious trades (the operator's; trade 1 LONG 100.945 is out, because that level traded only before Mon 06:00 UTC): 2 S 101.14 Mon 10:00 | 3 L 100.845 Mon 21:45 | 4 S 101.19 Tue 23:45 | 5 L 100.975 Wed 07:15 | 6 S 101.235 Wed 09:00 | 7 S 100.975 Thu 00:00 | 8 L 100.615 Fri 02:15 = 7.

E1 (reached 5):
- UPPER RESISTANCE 101.199-101.262: REACTED (week high 101.275 Wed 15:00, then -68 pips).
- EQUILIBRIUM 100.985-101.077 (+1H supply part to 101.153): REACTED (Mon high 101.145; Wed lows 100.95 / 101.066 / 101.077).
- 1H Mitigated 100.825-100.851: REACTED (consolidation, 11 closes; low 100.803).
- MID-RANGE SUPPORT 100.724-100.815: REACTED (100.803 Tue, 100.786 Thu).
- GAP IN-FILL 100.599-100.659: REACTED (week low 100.598 Fri 02:00).

Turning points 101.145 / 100.803 / 101.275 / 100.598 all have a zone. Missing 0. **E1 5/5 = 100%.** Qualifier FAIL: bunched, 10 overlapping pairs, with 100.94-101.31 one solid stack; EQUILIBRIUM area 21 p (bloated); floating 101.658-101.900 and 100.154-100.214.

E2:
- Mon SS: RIGHT (100.838-101.145 inside 100.724-101.262).
- Tue SS: RIGHT (100.803-101.126).
- Wed SS+RWL+BS down: WRONG. Close 101.069 vs open 101.088; the day ranged 100.946-101.275, and the break down through EQUILIBRIUM came on Thu.
- Thu BS down: RIGHT (101.071 -> 100.786, close -13 p).
- Fri BS+WL+RWL down: RIGHT (100.934 -> 100.598, then back to 100.997).

**E2 4/5 = 80%.**

E3:
- trade 2: CAUGHT (DX2 101.138, TP Tue 01:30).
- trade 3: CAUGHT (DX3 100.851, TP Tue 23:45).
- trade 4: CAUGHT (DX5 101.203, TP Wed 06:30).
- trade 5: CAUGHT (DX6 100.980, TP Wed 09:00).
- trade 6: CAUGHT (DX4 101.235, TP Fri 02:00).
- trade 7: CAUGHT (DX7 100.980, TP Fri 02:00).
- trade 8: CAUGHT (DX8 100.628, TP Fri 13:00).

**E3 7/7 = 100%.** Stopped: DX2.Tue (filled Tue 19:15, stopped Tue 23:45).

Presentation: setup labels overlap each other inside the week (DX5/DX4 at about 101.18, DX6/DX2.Tue at about 101.0, DX3 over candles). The DX7 label overlaps "1.4bn Option Strike Target". Zone labels in the left half run on over the forecast-week candles (EQUILIBRIUM label to about 101.0).

## EURUSD 2026-07-06 (anchor week)

Obvious trades (the operator's; trade 1 SHORT 1.14322 is out, pre-anchor only): 2 L 1.14106 Mon 10:00 | 3 S 1.14441 Mon 21:45 | 4 L 1.14012 Tue 23:45 | 5 S 1.14277 Wed 07:15 | 6 L 1.13953 Wed 11:30 | 7 L 1.14233 Thu 00:00 | 8 S 1.14578 Fri 02:15 = 7.

E1 (reached 7):
- 1H Mit 4x 1.14601-1.14677: REACTED (week high 1.14608 Fri 02:00).
- UPPER RESISTANCE 1.14444-1.14533: REACTED (1.1448, 1.14494, 1.1446).
- 1H BoM 1.14375-1.14421: REACTED (1.14421 Tue).
- GAP IN-FILL 1.14220-1.14280: REACTED (1.14234, 1.14315, 1.14209).
- liquidity band 1.14108-1.14178: REACTED (1.14083 Mon, 1.14141 Wed, 1.14117 Fri).
- MID-RANGE SUPPORT 1.13977-1.14053: REACTED (1.13983, 1.13961).
- 1H BoM Demand 1.13815-1.13886: REACTED (week low 1.13911, 2.5 p above it).

Missing 0. **E1 7/7 = 100%.** Qualifier FAIL: 13 bunched pairs; 1.1395-1.1473 is covered without a gap; 4H MoM 1.15130 area 20 p; floating 1.14967-1.15264, 1.13245-1.13458.

E2:
- Mon SS: RIGHT.
- Tue SS: RIGHT (1.1408-1.1448 inside 1.13977-1.14533).
- Wed SS+RWL+BS up: WRONG (close 1.1416 vs open 1.14122, +3.8 p; the day ended back in the range).
- Thu BS up: RIGHT (1.1416 -> 1.14494, close +13.9 p).
- Fri BS+WL+RWL up: RIGHT (to 1.14608, then -49 p).

**E2 4/5 = 80%.**

E3:
- trade 2: CAUGHT (EU4 1.14095).
- trade 3: CAUGHT (EU1 1.14442).
- trade 4: CAUGHT (EU7 1.14018).
- trade 5: CAUGHT (EU5 1.14269).
- trade 6: CAUGHT (EU6 1.13940).
- trade 7: CAUGHT (EU8 1.14239).
- trade 8: CAUGHT (EU9 1.14598).

**E3 7/7 = 100%.** Stopped: EU2 (1.14385, Mon 17:15 -> Mon 21:45) and EU4.Tue (1.14095, Tue 19:15 -> 21:30).

Presentation: in the week, EU3 "SS L 7.1R" and EU4 "SS L 5.8R" are printed on top of each other, EU6/EU7 labels collide (illegible), and EU1/EU2 labels sit over candles. In the _all frame the day tags "Wed SS+RWL+BS" and "Thu BS" overlap zone lines.

## GBPUSD 2026-07-06 (anchor week)

Obvious trades (the operator's, all in the window): 1 L 1.33331 Mon 06:15 | 2 S 1.33934 Mon 18:45 | 3 L 1.3333 Wed 09:00 | 4 L 1.33629 Wed (reinforcement) | 5 S 1.34246 Thu 06:15 | 6 L 1.33829 Wed 21:00 | 7 S 1.34481 Fri 02:15 = 7.

E1 (reached 11): all REACTED.
- RESISTANCE CEILING 1.34484 (week high 1.34517)
- liquidity band 1.34386 (1.34373 Fri)
- 4H BoM 1.34264 (1.34308 Thu)
- 4H MoM 1.34035 (1.34104 Wed, 1.34192)
- UPPER RESISTANCE 1.33933 (1.34015, 1.33918)
- GAP 1.33744 (1.33799, 1.33807)
- UPPER RESISTANCE 1.33643 (1.33607, 1.33567)
- 1H MoM 1.33544
- UPPER RESISTANCE 1.33435 (1.33422)
- sweep zone 1.33340 (1.33286)
- MID-RANGE 1.33225 (week low 1.33222)

Missing 0. **E1 11/11 = 100%.** Qualifier FAIL: 20 zones from 1.3199 to 1.3493 form one wall of boxes (16 bunched pairs). Bloated (7 zones): 4H Mit MoM 1.31986-1.32280 area 36 p, KEY SUPPORT 1.32789 29 p, MID-RANGE 1.33225 25 p, 4H MoM 1.32338 25 p, sweep 1.34783 23 p, UPPER RESISTANCE 1.33643 22 p, 4H MoM 1.34035 21 p. Floating: 5 zones below 1.3277.

E2:
- Mon SS: RIGHT (1.33286-1.33972 inside 1.33082-1.34032).
- Tue SS: RIGHT.
- Wed SS+RWL+BS up: RIGHT (dip to 1.33222, then 1.34104, close +28.8 p).
- Thu BS up: RIGHT (1.33877 -> 1.34308, close +20.1 p).
- Fri BS+WL+RWL up: RIGHT (1.34517, then -60 p).

**E2 5/5 = 100%.**

E3:
- trade 1: CAUGHT (GB2 1.33333).
- trade 2: CAUGHT (GB1 1.33959).
- trade 3: CAUGHT (GB4 1.33255: same MID-RANGE SUPPORT zone, but 7.5 p from his entry; under the 4-pip test it would be MISSED).
- trade 4: MISSED (no reinforcement; 1.34154 / 1.34222 / 1.33813 rejected).
- trade 5: CAUGHT (GB6 1.34254).
- trade 6: MISSED (GB7 1.33888 and GB5 1.33473 never filled).
- trade 7: MISSED (no short at 1.3448; RESISTANCE CEILING reached with no order).

**E3 4/7 = 57%.** Stopped: none.

Presentation: the GB3 "RWL S 4.0R" label sits over candles at about 1.3343. Tue/Wed day tags overlap the UPPER RESISTANCE label. The wall of zones hides the candle bodies between 1.3320 and 1.3420.

## DXY 2026-04-20

Obvious trades (the operator's, per S3): LONG 98.02 (Mon low 98.006, Mon 15:00) and LONG 98.29 (Wed low 98.211, Wed 05:00) = 2. For the record, the zigzag(30) moves were: S 98.395 -> 98.006 (Mon), L -> 98.567 (Tue), S -> 98.211 (Wed), L -> 98.939 (Thu), S -> 98.489 (Fri).

E1 (reached 9): all REACTED.
- UPPER RESISTANCE 98.939-99.005 (week high 98.939 Thu 17:00)
- 1H MoM 98.675-98.845 (98.737, 98.803, 98.688)
- liquidity band 98.561-98.625 (98.567 Tue spike, 98.552 Thu)
- UPPER RESISTANCE 98.456-98.541 (98.534, 98.558)
- 1H MoM 98.402-98.439 (anchor-bar high 98.395 + 9-close consolidation)
- liquidity band 98.300-98.364 (98.306 Mon)
- GAP 98.220-98.280 (98.211 Wed)
- MID-RANGE 98.058-98.145 (98.155, 98.006)
- 1H MoM Demand 97.937-98.045 (98.006)

Missing 0. **E1 9/9 = 100%.** Qualifier FAIL: 9 bunched pairs; 1H MoM 98.675 area 20 p; KEY SUPPORT 97.725 area 26 p; floating 97.466-97.682.

E2:
- Mon SS: RIGHT (98.006-98.395 inside 97.869-98.539).
- Tue SS+RWL+BS up: RIGHT (spike 98.123 -> 98.567, close +32.9 p).
- Wed BS up: RIGHT (98.211 -> 98.643, +23 p).
- Thu BS+RWL up: RIGHT (98.534 -> 98.939, then -25 p).
- Fri RWL down: RIGHT (spike 98.915 rejected, -31.5 p).

**E2 5/5 = 100%.**

E3:
- LONG 98.02: CAUGHT (DX1 98.019, filled Mon 15:15, TP 98.869 Thu 17:15).
- LONG 98.29: CAUGHT (DX2 98.270, 2 p off, filled Wed 05:15, TP Thu 17:15).

**E3 2/2 = 100%.** Stopped: DX3 (98.660, filled Thu 00:00, stopped Thu 00:15, 15 minutes later).

Presentation: in _all, the "Tue SS+RWL+BS up 33%" tag is printed over the UPPER RESISTANCE label at about 98.98. The "DX3 Ladder L 4.8R if DX1" label sits over candles.

## EURUSD 2026-04-20

Obvious trades:
1. L 1.17475 -> 1.1791 (Mon)
2. S 1.1791 -> 1.17187 (Mon 23:00 -> Tue)
3. L 1.17187 -> 1.17624 (Wed 05:00)
4. S 1.17624 -> 1.16789 (Thu 11:00)
5. L 1.16789 -> 1.17165 (Thu)
6. S 1.17165 -> 1.16691 (Thu 17:00)
7. L 1.16691 -> 1.1723 (Fri)

= 7.

E1 (reached 12): all REACTED.
- UPPER RESISTANCE 1.17988 (1.1791)
- UPPER RESISTANCE 1.17706 (1.17718 / 1.17755 / 1.17816)
- sweep 1.17575 (1.17624)
- sweep 1.17592
- EQUILIBRIUM 1.17497 (1.17475)
- GAP 1.17347 (1.17318)
- sweep 1.17277 (1.17187)
- GAP 1.17203
- MID-RANGE 1.16973 (1.16921, 1.16789 area)
- liquidity band 1.16876
- GAP 1.16744 (1.16789)
- KEY SUPPORT 1.16570 (week low 1.16691)

Missing 0. **E1 12/12 = 100%.** Qualifier FAIL: 10 bunched pairs; six zones and labels stacked 1.1730-1.1790. Bloated: MID-RANGE area 1.16809-1.17207 = 40 p, UPPER RESISTANCE 1.18213 = 37 p, UPPER RESISTANCE 1.17988 = 26 p, KEY SUPPORT = 21 p. Floating: 7 zones (1.18303-1.19069, 1.15907-1.16377).

E2:
- Mon SS: RIGHT.
- Tue SS+RWL+BS down: RIGHT (1.17759 -> 1.17201, -45.7 p).
- Wed BS down: RIGHT (-37.9 p).
- Thu BS+RWL down: RIGHT (1.1712 -> 1.16789, then +37 p).
- Fri RWL up: RIGHT (dip to 1.16729 rejected, +33.9 p).

**E2 5/5 = 100%.**

E3:
- 1: MISSED (no long at all this week).
- 2: CAUGHT (EU2/EU3 1.17920, TP).
- 3: MISSED.
- 4: MISSED (EU4 1.17656 not filled, high 1.17624).
- 5: MISSED.
- 6: MISSED (EU5 1.17372 not filled).
- 7: MISSED.

**E3 1/7 = 14%.** Stopped: none.

Presentation: zone labels collide in the left half (the "LSZ demand-side | sweep to 1.17492" text runs into the UPPER RESISTANCE / EQUILIBRIUM labels). The "Mon SS 65%" tag overlaps a zone label at about 1.1793.

## GBPUSD 2026-04-20

Obvious trades:
1. L 1.34818 -> 1.35444 (Mon 15:00)
2. S 1.35444 -> 1.34823 (Tue 08:00)
3. L 1.34823 -> 1.35396 (Tue 14:00)
4. S 1.35396 -> 1.3476 (Tue 17:00)
5. L 1.3476 -> 1.35353 (Wed 09:00)
6. S 1.35353 -> 1.34476 (Thu 17:00)
7. L 1.34476 -> 1.3537 (Fri)

= 7.

E1 (reached 7): all REACTED.
- UPPER RESISTANCE 1.35434 (week high 1.35444, 1.35396)
- UPPER RESISTANCE 1.35241 (1.35353)
- sweep 1.35163 (1.35151, 1.35182)
- GAP 1.35047
- UPPER RESISTANCE HEAVY 1.34932 (1.3492)
- MID-RANGE 1.34768 (1.3476 / 1.34772 / 1.34789 / 1.34781)
- 1H MoM 1.34345-1.34660 (week low 1.34476, 1.34532)

Missing 0. **E1 7/7 = 100%.** Qualifier FAIL: 10 bunched pairs. 1H MoM box 31 p tall (area 38 p); UPPER RESISTANCE 1.35719 area 34 p. Floating: 1.35844-1.36008, 1.33806-1.34073.

E2:
- Mon SS: WRONG (H 1.35444, 42 p above the box top 1.35019; closed 1.35333 above it).
- Tue SS+RWL+BS down: RIGHT (1.35396 -> 1.3476, close -26.5 p).
- Wed BS down: WRONG (close -7 p; a 1.349-1.3535 range day).
- Thu BS+RWL down: RIGHT (1.35182 -> 1.34476, then +38 p).
- Fri RWL up: RIGHT (dip 1.34532 rejected, +55.7 p).

**E2 3/5 = 60%.**

E3: 1-7 all MISSED.
- GB2 SHORT 1.35163 was filled Mon 07:15, inside leg 1, and stopped Mon 15:15 (SL 1.35387).
- GB1, GB3, GB4 and GB5 never filled. The forecast path to 1.341 was never traded.

**E3 0/7 = 0%.** Stopped: GB2.

Presentation: in the week frame the Mon SS / Wed BS day tags and the "1.0bn Option Strike Target" label sit over candles (about 1.350-1.352). The tall blue 1H MoM box covers 1.3434-1.3466.

## DXY 2026-10-05

Obvious trades:
1. S 102.433 -> 101.754 (Mon 06:30 -> Tue 12:00)
2. L 101.754 -> 102.499 (Wed 12:00)
3. S 102.499 -> 102.133 (Thu 02:00)
4. L 102.133 -> 102.467 (Thu 11:00)
5. S 102.467 -> 101.92 (Fri 05:00)
6. L 101.92 -> 102.335 (Fri)

= 6.

E1 (reached 6): all REACTED.
- sweep 102.485-102.535 (week high 102.499, 102.467)
- sweep 102.157-102.207 (102.304, 102.285, 102.133)
- sweep 102.082-102.132 (102.084)
- MID-RANGE 101.961-102.051 (102.044, 102.033)
- 1H MoM 101.855-101.926 (101.92)
- KEY SUPPORT 101.750-101.843 (week low 101.754)

Missing: **102.433, the Mon high** (no zone between 102.307 and 102.485). **E1 6/7 = 86%.** Qualifier FAIL:
- 8 bunched pairs;
- KEY SUPPORT HEAVY 100.980 area 40 p (bloated);
- floating: 4 zones 100.98-101.405, 35-54 p below the week low; the zones frame shows a full stack of them under price.

E2: SS every day, box 101.755-102.635 (88 p, larger than the whole week's 74.5 p range). Mon, Tue (low 101.754), Wed, Thu and Fri are all RIGHT. **E2 5/5 = 100%.**

E3:
- 1: MISSED (DX1 102.485 never reached).
- 2: CAUGHT (DX2 101.926, filled Tue 11:00, TP 102.470 Wed 12:15).
- 3: CAUGHT (DX1.Wed 102.485, TP 101.941 Fri 05:30).
- 4: MISSED.
- 5: MISSED (no new order; DX1.Thu not placed because DX1.Wed was still open).
- 6: MISSED (DX2.Fri filled 05:30, still open at week end).

**E3 2/6 = 33%.** Stopped: none.

Presentation: the right half of the zones frame is filled with KEY SUPPORT bands far below price (100.98-101.6).

## EURUSD 2026-10-05

Obvious trades:
1. L 1.1169 -> 1.12207 (Mon)
2. S 1.12207 -> 1.11863 (Mon)
3. L 1.11863 -> 1.12767 (Tue 12:00)
4. S 1.12767 -> 1.11645 (Wed 12:00)
5. L 1.11645 -> 1.12128 (Thu 02:00)
6. S 1.12128 -> 1.11719 (Thu 11:00)
7. L 1.11719 -> 1.12427 (Fri 05:00)
8. S 1.12427 -> 1.11874 (Fri 16:00)

= 8.

E1 (reached 6): all REACTED.
- 1H BoM 1.12716-1.12853 (week high 1.12767)
- GAP 1.12611 (1.12693)
- UPPER RESISTANCE 1.12451 (1.12447, 1.12427)
- sweep 1.12208 (1.12207, 1.12267)
- sweep 1.12149 (1.12128, 1.1201)
- sweep 1.11610-1.11660 (week low 1.11645)

Missing: **1.11863 (Mon 14:00) and 1.11719 (Thu 11:00)**. The 1.117-1.119 floor was tested 4 times (1.11863, 1.11719, 1.11845, 1.11874) and has no zone; the nearest are 1.11660 below and 1.12039 above. **E1 6/8 = 75%.** Qualifier FAIL:
- 10 bunched pairs;
- UPPER RESISTANCE 1.13439 area 38 p and 1.13185 area 34 p (bloated);
- floating: 6 zones 1.13317-1.13911, up to 103 p above the week high.

E2: SS every day, box 1.11510-1.12712 (120 p). All five days are inside ±10 p (Tue 1.12767, +5.5 p). **E2 5/5 = 100%** (Wed is a -63 p top-to-bottom day, still inside the box).

E3:
- 1: MISSED (EU1 1.11660 not filled, low 1.1169).
- 2: MISSED.
- 3: MISSED.
- 4: CAUGHT (EU2.Wed 1.12585, filled Tue 21:00, TP 1.11675 Wed 12:15).
- 5: MISSED (EU1.Wed 1.11660 filled Wed 12:15, TP 1.12476 missed by 4.9 p, open at week end).
- 6: MISSED.
- 7: MISSED.
- 8: MISSED.

**E3 1/8 = 12.5%.** Stopped: EU2 (1.12585, filled Tue 11:15, stopped Tue 12:00 by the 1.12767 high, 2.5 p through SL 1.12742).

Presentation: the top half of the week frame is filled with zones 30-100 p above price. The chart header overlaps the 2.9bn strike line.

## GBPUSD 2026-10-05

Obvious trades:
1. L 1.32052 -> 1.3239 (Mon)
2. S 1.3239 -> 1.319 (Mon 13:00)
3. L 1.319 -> 1.32318 (Tue 01:00)
4. S 1.32318 -> 1.32013 (Tue 06:00)
5. L 1.32013 -> 1.32856 (Tue 15:00)
6. S 1.32856 -> 1.31935 (Wed 12:00)
7. L 1.31935 -> 1.32242 (Wed)
8. S 1.32242 -> 1.31843 (Thu 10:00)
9. L 1.31843 -> 1.32503 (Fri 05:00)
10. S 1.32503 -> 1.32057 (Fri)
11. L 1.32057 -> 1.32443 (Fri)

= 11.

E1 (reached 8): all REACTED.
- 1H BoM 1.32731 (week high 1.32856)
- 4H BoM 1.32610
- UPPER RESISTANCE 1.32457 (1.32485, 1.32503)
- 1H BoM 1.32319 (1.3239, 1.32318)
- GAP 1.32124
- MID-RANGE 1.31991 (1.32013, 1.32057, 1.32037)
- sweep 1.31899 (1.319, 1.31935)
- sweep 1.31806 (week low 1.31843)

Missing 0. **E1 8/8 = 100%.** Qualifier FAIL: 5 bunched pairs; 1H BoM 1.32731-1.32942 box 21 p (area 26 p); 4H BoM area 20 p.

E2: SS every day, box 1.31799-1.32395.
- Mon: RIGHT.
- Tue: WRONG (H 1.32856, 46 p above the box; close 1.32742 above it).
- Wed: WRONG (opened 1.32742 and traded up to 1.32761, 37 p above the box, before falling 62 p).
- Thu: RIGHT (H 1.32485, +9 p).
- Fri: WRONG (H 1.32503, 10.8 p above the box; borderline).

**E2 2/5 = 40%.**

E3:
- 1: MISSED.
- 2: CAUGHT (GB1 1.32329, TP Mon 13:30).
- 3: CAUGHT (GB2 1.31924, filled Mon 13:30, TP 1.32333 Tue 07:30).
- 4: MISSED (GB1.Tue 1.32329 filled Tue 01:30, stopped Tue 08:30; the low 1.32013 came 4.9 p short of TP).
- 5: MISSED.
- 6: MISSED (GB1.Wed void: "anchor zone closed through Tue 08:00").
- 7: CAUGHT (GB2.Wed 1.31924, TP Thu 14:15).
- 8: MISSED.
- 9: MISSED (GB2.Thu 1.31924 "not filled inside its bracket", although Thu traded 1.31843-1.31874 below it).
- 10: MISSED (GB1.Fri void).
- 11: MISSED.

**E3 3/11 = 27%.** Stopped: GB1.Tue.

Presentation: in _all, "GB2 SS L 2.6R" and the MID-RANGE label print over each other at about 1.3200. The Tue spike to 1.3285 is outside every day box.

## DXY 2026-05-18

Obvious trades:
1. S 99.307 -> 98.944 (Mon 22:00)
2. L 98.944 -> 99.515 (Thu 13:00; the Wed 14:00-15:00 one-hour spike 99.472 -> 98.966 is merged)
3. S 99.515 -> 99.092 (Thu 17:00)
4. L 99.092 -> 99.412 (Fri)

= 4.

E1 (reached 6): all REACTED.
- liquidity band 99.449 (99.471, week high 99.515)
- sweep 99.359 (99.434, 99.412)
- 1H MoM 99.251 (anchor-bar high 99.307, 99.234)
- 1H MoM 99.174 (99.172, 99.186)
- MID-RANGE 98.963 (98.971, 98.966, 99.092)
- 1H MoM 98.844 (week low 98.944)

Missing 0. **E1 6/6 = 100%.** Qualifier FAIL: 8 bunched pairs; KEY SUPPORT HEAVY 98.460 area 29 p.

E2: SS every day, box 98.963-99.509. All days are inside ±10 p. **E2 5/5 = 100%.**

E3:
- 1: MISSED (every short was rejected for RRR).
- 2: MISSED. DX1 99.050 filled Mon 11:30 and was stopped Mon 16:15: SL 98.971 sits inside the floor zone and was touched exactly by the 98.971 low. DX1.Tue-Fri were void ("anchor zone closed through on 1H Mon 20:00"), yet MID-RANGE held all week at 98.944 / 98.966 / 99.064 / 99.092.
- 3: MISSED.
- 4: MISSED (void).

**E3 0/4 = 0%.** Stopped: DX1.

Presentation: in the week frame the DX1 label "DX1 SS L 3.7R" is partly hidden by candles at about 99.03. The "4.1bn" strike label overlaps the KEY SUPPORT label in _zones.

## EURUSD 2026-05-18

Obvious trades:
1. L 1.16219 -> 1.16617 (Mon 22:00)
2. S 1.16617 -> 1.15827 (Wed 14:00)
3. L 1.15827 -> 1.16353 (Thu 08:00)
4. S 1.16353 -> 1.15762 (Thu 13:00)
5. L 1.15762 -> 1.163 (Thu 17:00)
6. S 1.163 -> 1.15882 (Fri 14:00)
7. L 1.15882 -> 1.1619 (Fri)

= 7.

E1 (reached 8): all REACTED.
- UPPER RESISTANCE 1.16641 (week high 1.16617)
- UPPER RESISTANCE HEAVY 1.16493 (1.16572, 1.16448)
- liquidity band 1.16327 (1.16353, 1.163)
- EQUILIBRIUM 1.16219 (1.16219 anchor low, 1.16264)
- sweep 1.16168
- sweep 1.16083
- MID-RANGE 1.15970 (1.1594)
- liquidity band 1.15747 (1.15827, week low 1.15762)

Missing: **1.15882 (Fri 14:00)**, between 1.15815 and 1.1597. **E1 8/9 = 89%.** Qualifier FAIL: 8 bunched pairs; 4H MoM 1.17047 area 23 p; floating 1.16939-1.17277 and 1.15390-1.15458.

E2: SS every day, box 1.15747-1.16672. All days are inside. **E2 5/5 = 100%.**

E3:
- 1: MISSED (EU2 SHORT 1.16297 went the other way: filled Mon 06:00, stopped Mon 07:15).
- 2: CAUGHT (EU1 1.16604, TP Tue 14:15).
- 3: MISSED (EU3.Wed 1.15815 not filled, low 1.15827).
- 4: MISSED.
- 5: CAUGHT (EU3.Thu 1.15815, TP Thu 17:45).
- 6: MISSED.
- 7: MISSED (no Friday orders: "EMISSION_CAPPED - more than 11 trades", although the week has 3 setups counted with their daily repeats).

**E3 2/7 = 29%.** Stopped: EU2.

Presentation: "EU1.Thu" is printed over "1.5bn Option Strike Target" at about 1.1648. In _all, the day tags overlap the UPPER RESISTANCE label at about 1.1665.

## GBPUSD 2026-05-18

Obvious trades:
1. L 1.33217 -> 1.34494 (Mon 16:00, 128 p)
2. S 1.34494 -> 1.33871 (Tue 09:00)
3. L 1.33871 -> 1.34196 (Tue)
4. L 1.33785 -> 1.34123 (Tue)
5. S 1.34123 -> 1.3375 (Wed 08:00)
6. L 1.3375 -> 1.3463 (Wed 15:00)
7. S 1.3463 -> 1.33904 (Thu 13:00)
8. L 1.33904 -> 1.34492 (Thu 17:00)
9. S 1.34492 -> 1.34132 (Fri 07:00)
10. L 1.34132 -> 1.34631 (Fri 13:00)
11. S 1.34631 -> 1.34195 (Fri)

= 11. Not counted: the 2-hour Tue 12:00-14:00 drop 1.34196 -> 1.33785, which the merge could not absorb.

E1 (reached 9): all REACTED.
- GAP 1.34628 (1.3463, 1.34631)
- UPPER RESISTANCE 1.34497 (1.34494, 1.34548, 1.34492)
- GAP 1.34239
- UPPER RESISTANCE 1.33950
- liquidity band 1.33816 (1.33871, 1.33904)
- GAP 1.33720 (1.33785, 1.3375)
- GAP 1.33492 (1.33465)
- GAP 1.33240 (anchor low 1.33217)
- sweep 1.33147 (anchor low 1.33217)

Missing: **1.34123 (Tue 17:00) and 1.34132 (Fri 07:00)**. Both are 9-10 p from the nearest zone; the Fri 07:00 low was the start of a 50-p rally. **E1 9/11 = 82%.** Qualifier FAIL: 5 bunched pairs; floating 1.32208-1.32728.

E2: SS every day, box 1.33047-1.34137. The week traded 1.3375-1.3463 from Mon 16:00 on.
- Mon: WRONG (+109 p breakout to 1.34494).
- Tue: WRONG (H 1.34371).
- Wed: WRONG (H 1.3463).
- Thu: WRONG (H 1.34548).
- Fri: WRONG (1.34132-1.34631, the whole day above the box).

**E2 0/5 = 0%.**

E3:
- 1: CAUGHT (GB2 1.33197, filled Mon 06:00, TP Mon 12:30).
- 2: MISSED (GB1 SHORT 1.33983 filled Mon 12:30 mid-rally, stopped Mon 15:45 before the real top at 1.34494).
- 3-11: MISSED (GB1.Tue-Fri void: "anchor zone closed through Mon 15:00"; GB2.Tue-Fri 1.33197 never reached).

**E3 1/11 = 9%.** Stopped: GB1.

Presentation: the day tags (Mon SS ... Fri SS) and the setup labels are printed inside the candle cluster at 1.338-1.342. The yellow path runs 1.332-1.340, under the candles all week.

## Table (12 maps)

| map | E1 | E2 | E3 |
|---|---|---|---|
| DXY 2026-07-06 | 5/5 = 100% | 4/5 = 80% | 7/7 = 100% |
| EURUSD 2026-07-06 | 7/7 = 100% | 4/5 = 80% | 7/7 = 100% |
| GBPUSD 2026-07-06 | 11/11 = 100% | 5/5 = 100% | 4/7 = 57% |
| DXY 2026-04-20 | 9/9 = 100% | 5/5 = 100% | 2/2 = 100% |
| EURUSD 2026-04-20 | 12/12 = 100% | 5/5 = 100% | 1/7 = 14% |
| GBPUSD 2026-04-20 | 7/7 = 100% | 3/5 = 60% | 0/7 = 0% |
| DXY 2026-10-05 | 6/7 = 86% | 5/5 = 100% | 2/6 = 33% |
| EURUSD 2026-10-05 | 6/8 = 75% | 5/5 = 100% | 1/8 = 13% |
| GBPUSD 2026-10-05 | 8/8 = 100% | 2/5 = 40% | 3/11 = 27% |
| DXY 2026-05-18 | 6/6 = 100% | 5/5 = 100% | 0/4 = 0% |
| EURUSD 2026-05-18 | 8/9 = 89% | 5/5 = 100% | 2/7 = 29% |
| GBPUSD 2026-05-18 | 9/11 = 82% | 0/5 = 0% | 1/11 = 9% |
| **Total, all 12** | **94/100 = 94%** | **48/60 = 80%** | **30/84 = 36%** |
| **Total, 9 maps outside 2026-07-06** | **71/77 = 92%** | **35/45 = 78%** | **12/63 = 19%** |

The E1 qualifier ("none bloated, bunched, floating or missing") FAILS on all 12 maps:
- every map has 5-16 bunched zone pairs;
- 11/12 have bloated zones;
- 5 have missing turning points.

Because zone areas cover almost every 10-15 pips of each week's range, the E1 ratio says little; the qualifier is where E1 fails.

## Five defects that cost the most

1. **Too few setups at the turns: E3 is 12 caught of 63 outside the anchor week.** Most weeks carry 1-2 order pairs repeated daily, and most zone-to-zone moves have no order at their turn:
   - GBPUSD 04-20: 0/7. Only GB2 SHORT 1.35163 filled, on Mon 07:15 into the 62-p rally, and it was stopped Mon 15:15.
   - GBPUSD 05-18: 1/11.
   - EURUSD 04-20: 1/7, no long all week although four long legs ran 38-54 p.
2. **Repeat orders voided by "anchor zone closed through on 1H" while the zone kept holding:**
   - DXY 05-18: DX1.Tue-Fri LONG 99.050 void after Mon 20:00, while the floor held at 98.944 / 98.966 / 99.092. E3 0/4.
   - GBPUSD 05-18: GB1.Tue-Fri SHORT 1.33983 void.
   - GBPUSD 10-05: GB1.Wed-Fri SHORT 1.32329 void; the Tue-Fri highs 1.32856 / 1.32503 had no short.
   - GBPUSD 10-05: GB2.Thu 1.31924 also "not filled inside its bracket" while Thu traded 1.31843.
3. **SS range box placed where price did not trade (E2):**
   - GBPUSD 05-18: box 1.33047-1.34137 while price left it Mon (to 1.34494) and spent Tue-Fri at 1.3375-1.3463. E2 0/5.
   - GBPUSD 10-05: Tue/Wed/Fri highs 1.32856 / 1.32761 / 1.32503 above box top 1.32395. E2 2/5.
   - GBPUSD 04-20: Mon high 1.35444 vs box top 1.35019.
   - Where the box did hold (DXY 10-05 88 p, EURUSD 10-05 120 p) it was taller than the whole week's range.
4. **BS days that did not break (E2 composites):**
   - DXY 07-06 Wed "SS+RWL+BS down": close 101.069 vs open 101.088; the break came Thu.
   - EURUSD 07-06 Wed "SS+RWL+BS up": +3.8 p, closed back at 1.1416.
   - GBPUSD 04-20 Wed "BS down": -7 p, a 1.349-1.3535 range day.

   Defects 3 and 4 account for all 12 lost E2 days: 9 from defect 3 and 3 from defect 4.
5. **No Engine 1 zone at repeated turning points / zone walls elsewhere:**
   - EURUSD 10-05 floor 1.1172-1.1187 (lows 1.11863 Mon, 1.11719 Thu, 1.11845 Thu, 1.11874 Fri), with no zone between 1.11660 and 1.12039.
   - DXY 10-05 Mon high 102.433.
   - GBPUSD 05-18: 1.34123 Tue and 1.34132 Fri.
   - EURUSD 05-18: 1.15882 Fri.

   At the same time, zones are stacked without a gap where price is not:
   - GBPUSD 07-06: 20 zones from 1.3199 to 1.3493, 7 of them over 20 p tall (4H 1.31986-1.32280 area 36 p);
   - DXY 10-05: four KEY SUPPORT bands 35-54 p below the week low;
   - EURUSD 10-05: six zones up to 103 p above the week high.

   Labels collide with each other and sit over candles on 11/12 maps (e.g. EURUSD 07-06 EU3/EU4 at about 1.4210, GBPUSD 05-18 day tags at 1.342).

Stopped setups across all maps:
- DXY 07-06: DX2.Tue
- EURUSD 07-06: EU2, EU4.Tue
- DXY 04-20: DX3
- GBPUSD 04-20: GB2
- EURUSD 10-05: EU2
- GBPUSD 10-05: GB1.Tue
- DXY 05-18: DX1
- EURUSD 05-18: EU2
- GBPUSD 05-18: GB1
