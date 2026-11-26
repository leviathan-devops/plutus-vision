# G1 outside count, dry run 2 (fresh reviewer, strict)

Sources: the 36 frames in `evidence/s3b/` (all opened and looked at), the facts files `audit/g1_facts_b/*.txt` (exact prices only), `context_management/oracle/golden_week.json` (operator trades, week 2026-07-06), and read-only 1H/15m bars (`e1_data.bars`). Nothing was rendered.

## Counting rules I applied (so anyone can recount)
- **Window:** Monday 06:00 UTC (02:00 New York) to Friday 21:00 UTC (17:00 New York). The Monday 06:00 bar is the anchor price, not a forecast turn, so I do not count it as a turning point.
- **Obvious trades, week 2026-07-06:** the operator's trades. I checked his Monday trades against the 1H bars before excluding any:
  - DXY #1 (LONG 100.945): price went through 100.945 at Mon 01:00-03:00 UTC, and after 06:00 it never came back before its TP. It is outside the window and excluded.
  - EURUSD #1 (SHORT 1.14322): price was at 1.1432-1.1438 at Sun 21:00-Mon 04:00, and after 06:00 the high was 1.14288. It is outside the window and excluded.
  - GBPUSD #1 (LONG 1.33331): first reached by the Mon 06:00 bar (low 1.33301). It is in the window and kept.
- **Obvious trades, other weeks:** I wrote these from the `_zones` frame. I fixed them as the legs of the 1H swing path from the window start: a leg counts when it is at least 30 DXY pips, 35 EURUSD pips or 45 GBPUSD pips. The last leg of the week counts if it reaches that size.
- **E1:** each E1 (IP) zone that price reached gets one verdict, REACTED or PIERCED. A turning point within 6 pips (0.06 on DXY) of an E1 zone edge counts as "at the zone". Any other turning point is a "turning point with no zone".
  - E1 % = reacted / (zones reached + turning points with no zone).
  - V1 S/D and liquidity zones are not E1 and earn nothing.
  - A zone that held on some contacts and was crossed on others is REACTED, and I list the piercings by name.
- **E2, SS days:**
  - The day must stay inside the box. A breach whose 1H closes come back inside counts as inside; a daily close outside does not.
  - Price must swing between the two sides in the order the yellow line draws them.
- **E2, directional days (BS, RWL):** the direction must be right, and the day box must overlap at least about 20% of the day's range.
- **E2, days ending in RWL:** the yellow line puts the extreme at the end of the day, followed by a vertical or steep reversal. If the extreme actually came in Asia or early London and the rest of the day ran the other way, the day is WRONG.
- **E3:**
  - CAUGHT means a setup in the same direction, at the leg's start zone, that filled and hit its TP before its SL.
  - A setup that was stopped is a loss.
  - A setup still open at the end of the week is not caught.
  - I re-checked every fill and exit claim on the 15m bars. All agree with the facts files except GB1 GBPUSD 2026-10-05: its TP of 1.31900 was touched to the tick (Mon 13:45 low 1.31900) but not traded through, so I keep the facts-file verdict of STOPPED.

---

## DXY 2026-07-06
**Obvious trades (operator, in the window), 7:**
1. #2 Mon SHORT 101.14, TP 100.845
2. #3 Tue LONG 100.845, TP 101.19
3. #4 Wed SHORT 101.19, TP 100.975
4. #5 Wed LONG 100.975, TP 101.24
5. #6 Wed SHORT 101.235, TP 100.68
6. #7 Thu SHORT 100.975
7. #8 Fri LONG 100.615, TP 100.94

(#1 is excluded: it filled before 06:00.)

**E1:**
- REACTED:
  - UPPER RESISTANCE 101.199-101.262: Wed high 101.275 was sharply rejected, down to 100.79 on Thu. Mon high 101.145 is 5.4 pips below it.
  - EQUILIBRIUM 100.985-101.077: price consolidated in and around it all week. Wed low 100.946 bounced.
  - MID-RANGE SUPPORT 100.724-100.815: held on Tue (100.803) and Thu (100.786). It was pierced on Fri down to 100.598.
- Turning point with no zone: Fri 02:00 low 100.598, 12.6 pips under MRS. Only V1 zones sit there.
- Bloat / bunching: none serious among the E1 zones. The 1H/4H V1 zones stacked 100.5-101.4 cover most of the frame.
- **E1 = 3/4 = 75%**

**E2:**

| Day | Verdict | Why |
|---|---|---|
| Mon SS | RIGHT | Stayed inside 100.815-101.199 and swung top (101.145) to bottom (100.838). |
| Tue SS | RIGHT | The 100.803 breach closed back inside; swung bottom to top (101.126). |
| Wed SS+RWL+BS | RIGHT | Up 101.2, down 100.946, up 101.275, then down, as drawn; closed down. |
| Thu BS down | RIGHT | Down 101.07 to 100.786; the box overlaps about 36% of the day. |
| Fri BS+WL+RWL | WRONG | The line runs down all day with the reversal drawn as a vertical at the last bar. The low came at Fri 02:00 (100.598), price rose the rest of the day, and the day closed up (100.965). |

**E2 = 4/5 = 80%**

**E3:**
- CAUGHT:
  - #2 by DX2 (filled Mon 10:00, TP Tue 01:30)
  - #3 by DX3 (filled Mon 18:30, TP Tue 23:45)
  - #4 by DX5
  - #5 by DX6
  - #6 by DX4 (TP Fri 02:00)
  - #7 by DX7
  - #8 by DX8
- Stopped setups: none. DX1 was not filled.
- Note: the setup prices nearly copy the operator's levels (DX4 101.235/100.685 vs 101.235/100.68; DX8 TP 100.94 = 100.94). This is the oracle week.
- **E3 = 7/7 = 100%**

**Presentation:**
- The Wed label "Wed SS+RWL+BS down 40%" and "Thu BS down 40%" are printed over "2.2bn Option Strike Target".
- The "Fri BS+WL+RWL down 32%" label sits on the Friday candles.
- The DX7 and DX8 labels sit over candles.
- Four overlapping translucent boxes on Wed-Fri darken the candles between 100.7 and 101.3.

## EURUSD 2026-07-06
**Obvious trades (operator, in the window), 7:**
1. #2 Mon LONG 1.14106
2. #3 Tue SHORT 1.14441
3. #4 Wed LONG 1.14012
4. #5 Wed SHORT 1.14277
5. #6 Wed LONG 1.13953
6. #7 Thu LONG 1.14233 (reinforcement)
7. #8 Fri SHORT 1.14578

(#1 is excluded: it filled before 06:00.)

**E1:**
- REACTED:
  - UPPER RESISTANCE 1.14444-1.14533: rejected Mon 1.14449, Tue 1.14480 and Thu 1.14494.
  - MID-RANGE SUPPORT 1.13977-1.14053: held Mon and Tue at about 1.1408, then consolidated in it Wed 08-16.
- Turning points with no zone:
  - Wed 15:00 low 1.13911 (6.6 pips under MRS)
  - Fri 02:00 high 1.14608 (7.5 pips over UR; only the V1 1H MoM is there)
- **E1 = 2/4 = 50%**

**E2:**

| Day | Verdict | Why |
|---|---|---|
| Mon SS | RIGHT | Inside; swung 1.1408 to 1.1445. |
| Tue SS | RIGHT | The 1.1448 breach closed back inside; swung top to bottom. |
| Wed SS+RWL+BS up | RIGHT | Up 1.14315, down 1.13911, up; closed up. |
| Thu BS up | RIGHT | Closed up; the box overlaps about 31%. |
| Fri BS+WL+RWL up | WRONG | The line climbs all day to 1.1463 with the reversal as a vertical at the last bar. The high came at Fri 02:00 (1.14608) and the day fell to 1.1411, closing down. |

**E2 = 4/5 = 80%**

**E3:**
- CAUGHT:
  - #2 by EU4 (Mon 13:45, TP Mon 18:45)
  - #3 by EU1
  - #4 by EU7
  - #5 by EU5
  - #6 by EU6
  - #7 by EU8 (ladder at 1.14164, 7 pips from his 1.14233, same TP leg)
  - #8 by EU9
- Stopped setups:
  - EU2 SHORT 1.14385 (Mon 21:45)
  - EU4 re-armed LONG 1.14095 (Tue 21:30)
  - EU10 LONG 1.14401 (its SL was touched on the fill bar, Thu 06:15)
- **E3 = 7/7 = 100%**

**Presentation:**
- The "Fri BS+WL+RWL up 32%" label and the EU9 label sit over the Friday high candles.
- EU10's label is cut at the right edge.
- The "Wed SS+RWL+BS up 40%" label sits over candles.

## GBPUSD 2026-07-06
**Obvious trades (operator), 7:**
1. #1 Mon LONG 1.33331 (Mon 06:00 bar, in the window)
2. #2 Mon SHORT 1.33934
3. #3 Wed LONG 1.3333
4. #4 Wed LONG 1.33629 (reinforcement)
5. #5 Thu SHORT 1.34246
6. #6 Thu LONG 1.33829
7. #7 Fri SHORT 1.34481

**E1:**
- REACTED:
  - RESISTANCE CEILING 1.34484-1.34548: Fri 02:00 high 1.34517 was rejected.
  - UPPER RESISTANCE 1.33643-1.33717: Wed 07 rejection from 1.33702. It was crossed with no reaction on Mon 15-16.
  - UPPER RESISTANCE 1.33435-1.33521: consolidation Tue 21-Wed 05.
  - MID-RANGE SUPPORT 1.33225-1.33285: Mon 1.33286 and Wed 1.33222 both held.
- Turning points with no zone:
  - Tue 01:00 high 1.34015
  - Thu 06:00 high 1.34308
  - Thu 12:00 low 1.33807
- Bunching: the two UR zones are 12 pips apart and the two KSB zones are 9 pips apart, stacked with V1 zones from 1.3265 to 1.3405.
- **E1 = 4/7 = 57%**

**E2:**

| Day | Verdict | Why |
|---|---|---|
| Mon SS | RIGHT | Breaches closed back inside; swung floor to ceiling. |
| Tue SS | RIGHT | The 1.34015 breach closed back next bar; fell to 1.33487. |
| Wed SS+RWL+BS up | RIGHT | Up, dip to 1.33222, rally; closed up; box overlap about 31%. |
| Thu BS up | WRONG | Direction right, but the box (1.3327-1.33825) sits under the whole day (1.33799-1.34308; about 5% overlap). |
| Fri BS+WL+RWL up | WRONG | The line climbs to 1.3434 at day end. The high came at Fri 02:00 (1.34517) and the day closed down at 1.33968. |

**E2 = 3/5 = 60%**

**E3:**
- CAUGHT:
  - #1 by GB1 (Mon 06:15, TP Mon 18:45)
  - #3 by GB2 (1.33245, TP Thu 06:15)
- MISSED:
  - #2: no short setup at all.
  - #4: GB3 ladder 1.33473 never filled. GB5 at 1.33888 is a different zone.
  - #5: GB4 SHORT 1.34254 filled Thu 06:15 but its TP of 1.33506 is far below the 1.33807 low, and it was stopped Fri 02:00. The operator's TP of 1.33882 was hit Thu.
  - #6: no setup.
  - #7: no setup.
- Stopped setups: GB4.
- **E3 = 2/7 = 29%**

**Presentation:**
- The purple "Fri BS+WL+RWL" label is printed on the Friday high candles and over the GB4 label.
- "Wed SS+RWL+BS" overlaps the GB2 label.
- The GB1 label sits on Monday candles.

## DXY 2026-04-20
**Obvious trades (from the `_zones` frame), 5:**
1. Mon SHORT 98.395 -> 98.006
2. Mon-Tue LONG 98.006 -> 98.567
3. Tue-Wed SHORT 98.567 -> 98.211
4. Wed-Thu LONG 98.211 -> 98.939
5. Thu-Fri SHORT 98.939 -> 98.489

**E1:**
- REACTED:
  - MID-RANGE SUPPORT 98.058-98.145: consolidation Mon 15-Tue 05 at 98.006-98.16.
  - UPPER RESISTANCE 98.456-98.541: Tue 19 98.567 was rejected; Thu 14 retest at 98.534 held; Fri low 98.489 is inside it.
  - UPPER RESISTANCE 98.939-99.005: Thu 17 high 98.939 at the zone edge was rejected.
- Turning point with no zone: Wed 05:00 low 98.211 (6.6 pips above MRS).
- Bunching: the 98.0-98.4 band is a stack of six V1 green zones plus the 1.4bn line.
- **E1 = 3/4 = 75%**

**E2:**

| Day | Verdict | Why |
|---|---|---|
| Mon SS | WRONG | The line rises to the ceiling. The day fell from 98.395 to 98.006 and closed at the floor (98.050). |
| Tue SS | WRONG | The line falls to the floor. The day rose to 98.567, with 1H closes above the box top (98.535 at 19:00, still outside at 21:00). |
| Wed SS+RWL+BS up | RIGHT | Dip to 98.211, then up; closed up; overlap about 35%. |
| Thu BS up | WRONG | The box (98.02-98.502) lies wholly below the day (98.534-98.939). |
| Fri BS+RWL up | WRONG | The peak is drawn late in the day. The high came at Fri 03:00 (98.915) and the day fell to close at 98.51, down 32 pips. |

**E2 = 1/5 = 20%**

**E3:**
- CAUGHT: leg 2 by DX2 (LONG 98.045, filled Mon 15:15, TP Tue 16:45).
- MISSED:
  - Leg 1: DX1 short 98.415 was not reached Monday.
  - Leg 3: DX1 filled Tue 17:00 and was stopped Tue 17:15.
  - Leg 4: DX5 long was stopped Wed 00:00; DX3 and DX4 were never filled; ladders DX6 and DX7 were never live.
  - Leg 5: no short.
- Stopped setups: DX1, DX5.
- **E3 = 1/5 = 20%**

**Presentation:**
- The labels "Wed SS+RWL+BS up 33%", "Mon SS", "Tue SS 65%" and "DX2 SS L 5.0R" sit on candles.
- The DX5, DX6 and DX7 boxes overlap Wed-Fri and hide the candles.
- The DX3 red stop box is drawn down to 97.82, far from price.

## EURUSD 2026-04-20
**Obvious trades, 7:**
1. Mon LONG 1.17475 -> 1.1791
2. Tue SHORT 1.1791 -> 1.17187
3. Tue-Wed LONG 1.17187 -> 1.17624
4. Wed-Thu SHORT 1.17624 -> 1.16789
5. Thu LONG 1.16789 -> 1.17165
6. Thu SHORT 1.17165 -> 1.16691
7. Thu-Fri LONG 1.16691 -> 1.1723

**E1:**
- REACTED:
  - EQUILIBRIUM 1.17497-1.17573: Mon 06 low 1.17475 bounced; Wed 05 retest from below at 1.17624 was rejected. It was crossed downward on Tue.
  - UPPER RESISTANCE 1.17706-1.17791: rejection on Mon 07, then consolidation around it Mon 15-Tue 03.
  - KEY SUPPORT BAND 1.1657-1.16638: Thu 17 low 1.16691 is 5.3 pips above it, and price bounced.
- Turning points with no zone:
  - Mon 23 high 1.1791 (12 pips above UR)
  - Tue 19 low 1.17187
  - Thu 11 low 1.16789
  - Thu 14 high 1.17165
- Bunching: four UPPER RESISTANCE zones plus the RC fill 1.177-1.185, interleaved with V1 zones.
- **E1 = 3/7 = 43%**

**E2:**

| Day | Verdict | Why |
|---|---|---|
| Mon SS | WRONG | The line falls to the floor 1.1721. The day rose to 1.17902 and closed outside the box at 1.17881. |
| Tue SS | WRONG | The line rises floor to ceiling. The day fell 1.1791 -> 1.17187. |
| Wed SS+RWL+BS down | RIGHT | Rally to 1.17624, then down; closed down; overlap about 21%. |
| Thu BS down | WRONG | The box (1.1738-1.17865) lies wholly above the day (1.16691-1.17165). |
| Fri BS+RWL down | WRONG | The low is drawn late in the day. It came at Fri 03:00 (1.16729), 27 pips under the box, and the day rose to close up at 1.17171. |

**E2 = 1/5 = 20%**

**E3:**
- Nothing filled. EU1, EU2 and EU3 are all SHORT 1.17920, and the week high was 1.17910 (Mon 23 / Tue 00), one pip short. The EU4 and EU5 ladders were never live.
- All 7 legs MISSED. No stopped setups.
- **E3 = 0/7 = 0%**

**Presentation:**
- "Thu BS down 33%" is printed over "1.4bn Option Strike Target".
- "EU4 Ladder S 12.3R" is printed over "1.1bn Option Strike Target".
- "Fri BS+RWL" overlaps the EU5 label.
- "Mon SS" and "Tue SS 65%" sit on candles.

## GBPUSD 2026-04-20
**Obvious trades, 7:**
1. Mon LONG 1.34818 -> 1.35444
2. Mon-Tue SHORT 1.35444 -> 1.34823
3. Tue LONG 1.34823 -> 1.35396
4. Tue SHORT 1.35396 -> 1.34744
5. Tue-Wed LONG 1.34744 -> 1.35353
6. Wed-Thu SHORT 1.35353 -> 1.34476
7. Fri LONG 1.34532 -> 1.3537

**E1:**
- REACTED:
  - UPPER RESISTANCE 1.35241-1.35327: price topped around it repeatedly; Wed 09 high 1.35353 was rejected.
  - UPPER RESISTANCE (HEAVY) 1.34932-1.35019: pivot and consolidation all week.
  - MID-RANGE SUPPORT 1.34768-1.34846: held Mon 06, Tue 08, Tue 19 and Thu 00-13. It was pierced Thu 17, 30 pips through to 1.34476.
- Turning points with no zone:
  - Mon 15 high 1.35444 (11.7 pips over UR)
  - Tue 14 high 1.35396 (6.9 pips over)
  - Thu 17 low 1.34476 (no E1 zone for 40 pips below)
- Bunching: three UPPER RESISTANCE zones plus MRS within 1.3477-1.3533, all overlapped by V1 zones.
- **E1 = 3/6 = 50%**

**E2:**

| Day | Verdict | Why |
|---|---|---|
| Mon SS | WRONG | The 27-pip box (1.3466-1.34932) sits under the day; the day rose to 1.35444 and closed 40 pips above it. |
| Tue SS | WRONG | Closed outside, above, at 1.35068; the floor of 1.3466 was never approached. |
| Wed SS+RWL+BS down | WRONG | 9-pip box (1.34879-1.34973), overlap about 16%. The day rallied 38 pips above it, which the flat-then-down line does not show; it closed only 7 pips down. |
| Thu BS down | RIGHT | Down to 1.34476; closed down; overlap about 56%. |
| Fri BS+RWL down | WRONG | The low is drawn at day end (1.3407). The low was 1.34532 at Fri 03:00, and the day closed 56 pips above the box at 1.35222. |

**E2 = 1/5 = 20%**

**E3:**
- Nothing traded. GB1 LONG 1.3466 was never reached; GB2 was void at its start.
- All 7 legs MISSED. No stopped setups.
- **E3 = 0/7 = 0%**

**Presentation:**
- "Wed SS+RWL+BS down 33%" is printed over "1.0bn Option Strike Target" and over candles.
- "Fri BS+RWL down 26%" sits on Friday candles.
- The GB2 position box and the yellow line run 1.340-1.344, far under every candle of the week.

## DXY 2026-10-05
**Obvious trades, 8:**
1. Mon-Tue SHORT 102.433 -> 101.754
2. Tue-Wed LONG 101.754 -> 102.499
3. Wed-Thu SHORT 102.499 -> 102.133
4. Thu LONG 102.133 -> 102.467
5. Thu SHORT 102.467 -> 102.033
6. Thu LONG 102.033 -> 102.367
7. Thu-Fri SHORT 102.367 -> 101.92
8. Fri LONG 101.92 -> 102.335

**E1:**
- REACTED:
  - KEY SUPPORT BAND 101.750-101.843: Tue 12 low 101.754, consolidation to Tue 22.
  - MID-RANGE SUPPORT 101.961-102.051: held Thu 14 (102.033) and Fri 05 (101.920). On first contact, Tue 08-10, it paused one bar and was pierced to 101.754.
- Turning points with no zone:
  - Wed 12 high 102.499
  - Thu 02 low 102.133
  - Thu 11 high 102.467
  - Thu 16 high 102.367

  There is **no E1 zone above 102.051 at all**, yet the week topped at 102.43-102.50 three times.
- **E1 = 2/6 = 33%**

**E2** (all SS, box 101.926-102.485):

| Day | Verdict | Why |
|---|---|---|
| Mon | WRONG | The line rises to the ceiling. The day fell from 102.433 to 102.084 and never reached the floor. |
| Tue | WRONG | Closed outside, below, at 101.841. |
| Wed | RIGHT | Floor-side to the ceiling 102.499, as drawn. |
| Thu | RIGHT | Up to 102.467, down to 102.033. |
| Fri | RIGHT | The 101.920 breach closed back inside, then up to 102.335. |

**E2 = 3/5 = 60%**

**E3:**
- CAUGHT: leg 3 by DX1 (SHORT 102.485, filled Wed 12:15, TP 101.926 Fri 05:30).
- MISSED:
  - Leg 2: DX2 LONG 101.926 filled Tue 11:00 and was stopped Tue 11:45 by the 101.754 low, 2.2 pips through its SL, before the 75-pip rally.
  - All other legs: no setup.
- Stopped setups: DX2.
- **E3 = 1/8 = 13%**

**Presentation:**
- "Mon SS ... Fri SS 80%" labels run along the top of the box over candles.
- DX1 and DX2 labels sit on candles.
- The DX2 red stop box (101.776-101.926) overprints the V1 "1H (Unmitigated) | MoM" label.

## EURUSD 2026-10-05
**Obvious trades, 8:**
1. Mon-Tue LONG 1.1169 -> 1.12767
2. Tue-Wed SHORT 1.12767 -> 1.11645
3. Wed-Thu LONG 1.11645 -> 1.12128
4. Thu SHORT 1.12128 -> 1.11719
5. Thu LONG 1.11719 -> 1.12267
6. Thu SHORT 1.12267 -> 1.11845
7. Thu-Fri LONG 1.11845 -> 1.12427
8. Fri SHORT 1.12427 -> 1.11874

**E1:**
- REACTED: UPPER RESISTANCE 1.12451-1.12530. It was crossed on Tue 08-12 (to 1.12767), consolidated on top of it Tue 12-Wed 00, and rejected Fri 05 at 1.12427.
- Turning points with no zone (**no E1 zone below price at all**):
  - Tue 12 high 1.12767
  - Wed 12 low 1.11645
  - Thu 02 high 1.12128
  - Thu 11 low 1.11719
  - Thu 14 high 1.12267
  - Thu 16 low 1.11845
- The other four E1 zones (1.1294-1.1506) are far above the week. In the frame only one E1 zone is drawn.
- **E1 = 1/7 = 14%**

**E2** (all SS, box 1.1166-1.12491):

| Day | Verdict | Why |
|---|---|---|
| Mon | WRONG | The line falls to the floor. The day rose from the floor (1.1169) to 1.12249. |
| Tue | WRONG | Closed outside, above, at 1.12583. |
| Wed | RIGHT | Ceiling to floor (1.11645), the breach closed back. |
| Thu | RIGHT | Floor 1.11719 then up to 1.12267. |
| Fri | RIGHT | Up to 1.12427, then down. |

**E2 = 3/5 = 60%**

**E3:**
- EU1 LONG 1.1166 filled Wed 12:15 at the exact week low but was **still open at the week end**: its TP of 1.12491 was 6.4 pips above the Fri high. It is not caught.
- All 8 legs MISSED. No stopped setups.
- **E3 = 0/8 = 0%**

**Presentation:**
- The "Tue SS 80%" label sits on the V1 "1H (Unmitigated) | MoM" label over candles.
- "Thu SS" is printed under "921M Option Strike Target".
- The EU1 label sits on candles.

## GBPUSD 2026-10-05
**Obvious trades, 4:**
1. Mon SHORT 1.3239 -> 1.319
2. Mon-Tue LONG 1.319 -> 1.32856
3. Tue-Thu SHORT 1.32856 -> 1.31843
4. Thu-Fri LONG 1.31843 -> 1.32503

**E1:**
- REACTED:
  - UPPER RESISTANCE 1.32457-1.32535: Wed 01-06 consolidation in it; Thu 14 (1.32485) and Fri 05 (1.32503) rejections. It was pierced upward Tue 09-12.
  - MID-RANGE SUPPORT 1.31991-1.32051: held Mon 05, Tue 06 and Wed 12.
- Turning points with no zone:
  - Mon 09 high 1.3239
  - Mon 13 low 1.3190
  - Tue 15 high 1.32856
  - Thu 10 low 1.31843
- **E1 = 2/6 = 33%**

**E2** (all SS, box 1.31949-1.32319):

| Day | Verdict | Why |
|---|---|---|
| Mon | RIGHT | Breaches closed back inside; reached the floor (1.319) as drawn. |
| Tue | WRONG | Closed outside, 42 pips above, at 1.32742. |
| Wed | RIGHT | Came back inside, ceiling-side down to the floor 1.31935, then up. |
| Thu | RIGHT | Floor (1.31843) to 1.32485. |
| Fri | RIGHT | Ceiling (1.32503) then down. |

On Thu and Fri the 1H closes stayed outside the box for 4-8 hours before returning.

**E2 = 4/5 = 80%**

**E3:**
- CAUGHT:
  - Leg 2 by GB2 (LONG 1.31949, Mon 13:30, TP Tue 01:30)
  - Leg 4 by GB2 re-armed (Wed 12:15, TP Thu 14:15)
- MISSED:
  - Leg 1: GB1 SHORT 1.32319 touched its TP of 1.31900 only to the tick and was stopped Tue 08:30.
  - Leg 3: no short.
- Stopped setups: GB1.
- **E3 = 2/4 = 50%**

**Presentation:**
- The GB1 label sits on candles.
- "GB2 SS L 2.7R" is printed over the "MID-RANGE SUPPORT" E1 label.
- The red stop box 1.3181-1.3195 covers the Thu lows.

## DXY 2026-05-18
**Obvious trades, 6:**
1. Mon SHORT 99.307 -> 98.944
2. Mon-Wed LONG 98.944 -> 99.472
3. Wed SHORT 99.472 -> 98.966
4. Wed-Thu LONG 98.966 -> 99.515
5. Thu SHORT 99.515 -> 99.092
6. Thu-Fri LONG 99.092 -> 99.412

**E1:**
- REACTED: MID-RANGE SUPPORT 98.963-99.037 (Mon 12-Tue 01 consolidation; Wed 15 spike low 98.966 rejected).
- Turning points with no zone: Wed 14 high 99.472 and Thu 13 high 99.515. **There is no E1 zone above 99.037.**
- **E1 = 1/3 = 33%**

**E2** (all SS, box 99.037-99.359):

| Day | Verdict | Why |
|---|---|---|
| Mon | WRONG | Closed outside, below, at 98.983. |
| Tue | RIGHT | Floor to 99.434; breaches closed back inside. |
| Wed | WRONG | Drawn floor then ceiling. The day did the reverse: about 10 hours of 1H closes above 99.359, then a spike to 98.966. |
| Thu | RIGHT | Floor 99.078 to 99.515 and back. |
| Fri | WRONG | 99.172-99.412; the floor was never reached. |

**E2 = 2/5 = 40%**

**E3:**
- CAUGHT:
  - Leg 2 by DX2 (Mon 12:30, TP Tue 14:15)
  - Leg 4 by DX2 re-armed (Wed 15:15, TP Thu 13:15)
- MISSED:
  - Leg 1: no setup.
  - Leg 3: DX1 SHORT 99.359 filled Tue 13:15 and was stopped Wed 08:15 by 99.471, 1.2 pips over its SL; 7 hours later price dropped through its TP.
  - Legs 5 and 6: no setup.
- Stopped setups: DX1.
- **E3 = 2/6 = 33%**

**Presentation:**
- "Tue SS 80%" overlaps the V1 "1H (Unmitigated) | MoM" label.
- "DX2 SS L 3.0R" sits on candles.
- The full-week SS box plus about eight V1 zone fills between 98.85 and 99.45 tint every candle.

## EURUSD 2026-05-18
**Obvious trades, 8:**
1. Mon LONG 1.16219 -> 1.16617
2. Tue-Wed SHORT 1.16617 -> 1.15827
3. Wed LONG 1.15827 -> 1.16448
4. Wed-Thu SHORT 1.16448 -> 1.1594
5. Thu LONG 1.1594 -> 1.16353
6. Thu SHORT 1.16353 -> 1.15762
7. Thu LONG 1.15762 -> 1.163
8. Fri SHORT 1.163 -> 1.15882

**E1:**
- REACTED:
  - EQUILIBRIUM 1.16219-1.16296 (pierced Tue 08-10)
  - UPPER RESISTANCE 1.16493-1.16562
  - UPPER RESISTANCE 1.16641-1.16726 (Mon 22 top at 1.16617)
  - MID-RANGE SUPPORT 1.1597-1.16036
- Turning points with no zone:
  - Wed 14 low 1.15827
  - Thu 13 low 1.15762
- Bunching: four E1 zones, eight V1 zones and two option lines inside 75 pips.
- **E1 = 4/6 = 67%**

**E2** (all SS, 27-pip box 1.16218-1.16493):

| Day | Verdict | Why |
|---|---|---|
| Mon | WRONG | Closed outside at 1.16556. |
| Tue | WRONG | Closed outside at 1.16047. |
| Wed | WRONG | 17 of 24 hours of 1H closes below the floor; low 39 pips under it. |
| Thu | WRONG | Closed outside at 1.16168. |
| Fri | WRONG | The whole day was below the box (high 1.16205). |

**E2 = 0/5 = 0%**

**E3:**
- CAUGHT: leg 1 by EU2 (Mon 06:00, TP Mon 11:30).
- MISSED:
  - Leg 2: EU1 SHORT 1.16512 was stopped Mon 20:15 by 1.16608, 3.3 pips over its SL, before the 70-pip drop that would have hit its TP.
  - All other legs: no setup.
- Stopped setups: EU1; EU2 re-armed (Tue 09:00).
- **E3 = 1/8 = 13%**

**Presentation (worst frame of the 36):**
- At 1.1646-1.1650, "UPPER RESISTANCE | HEAVY | 5-15% ZFP" is printed over "1H (Mitigated 2x) | MoM" and the EU1 label.
- "2.7bn" and "1.5bn Option Strike Target" are overprinted on each other.
- "Mon SS" is hidden under the EU1 label.
- The candles between 1.1600 and 1.1660 are behind more than 10 translucent fills.

## GBPUSD 2026-05-18
**Obvious trades, 5:**
1. Mon LONG 1.33217 -> 1.34494
2. Mon-Wed SHORT 1.34494 -> 1.3375
3. Wed LONG 1.3375 -> 1.3463
4. Wed-Thu SHORT 1.3463 -> 1.33904
5. Thu-Fri LONG 1.33904 -> 1.34631

**E1:**
- REACTED:
  - UPPER RESISTANCE 1.34497-1.34557: Mon 16, Thu 08 and Fri 17 rejections.
  - UPPER RESISTANCE 1.3395-1.34037: Mon 12 pullback; Thu 13 low 1.33904 held.
- Turning points with no zone:
  - Wed 08 low 1.3375 (20 pips under the zone)
  - Wed 15 high 1.3463
  - Fri 13 high 1.34631 (both highs 7.3-7.4 pips over the zone)
- The Mon 06 low 1.33217 is the anchor bar and not counted, but no E1 zone lies within 16 pips of it.
- **E1 = 2/5 = 40%**

**E2** (all SS, box 1.33197-1.33941):

| Day | Verdict | Why |
|---|---|---|
| Mon | WRONG | Ran 55 pips above the ceiling and closed outside at 1.34322. |
| Tue | WRONG | Never went below 1.33785; most 1H closes were above the box. |
| Wed | WRONG | Closed outside at 1.34331. |
| Thu | WRONG | Closed outside. |
| Fri | WRONG | The whole day was above the box. |

**E2 = 0/5 = 0%**

**E3:**
- Nothing caught. GB2 LONG 1.33197 was not filled: the Mon low was 1.33217, two pips away, before the 128-pip rally. GB1 SHORT 1.33983 was stopped Mon 15:45 inside that rally.
- Stopped setups: GB1.
- **E3 = 0/5 = 0%**

**Presentation:**
- The E1 label "UPPER RESISTANCE | MODERATE | 30-50% ZFP" is overprinted by "1H (Unmitigated) | MoM" (garbled text at 1.3400).
- "Mon SS" is overprinted by the V1 label.
- The forecast box fills the empty lower half of the week frame while every candle Tue-Fri sits above it.

---

## Summary: all 12 maps

| Map | E1 reacted / (reached + no-zone turns) | E1 % | E2 days right / 5 | E2 % | E3 caught / obvious | E3 % |
|---|---|---|---|---|---|---|
| DXY 2026-07-06 | 3 / 4 | 75% | 4 / 5 | 80% | 7 / 7 | 100% |
| EURUSD 2026-07-06 | 2 / 4 | 50% | 4 / 5 | 80% | 7 / 7 | 100% |
| GBPUSD 2026-07-06 | 4 / 7 | 57% | 3 / 5 | 60% | 2 / 7 | 29% |
| DXY 2026-04-20 | 3 / 4 | 75% | 1 / 5 | 20% | 1 / 5 | 20% |
| EURUSD 2026-04-20 | 3 / 7 | 43% | 1 / 5 | 20% | 0 / 7 | 0% |
| GBPUSD 2026-04-20 | 3 / 6 | 50% | 1 / 5 | 20% | 0 / 7 | 0% |
| DXY 2026-10-05 | 2 / 6 | 33% | 3 / 5 | 60% | 1 / 8 | 13% |
| EURUSD 2026-10-05 | 1 / 7 | 14% | 3 / 5 | 60% | 0 / 8 | 0% |
| GBPUSD 2026-10-05 | 2 / 6 | 33% | 4 / 5 | 80% | 2 / 4 | 50% |
| DXY 2026-05-18 | 1 / 3 | 33% | 2 / 5 | 40% | 2 / 6 | 33% |
| EURUSD 2026-05-18 | 4 / 6 | 67% | 0 / 5 | 0% | 1 / 8 | 13% |
| GBPUSD 2026-05-18 | 2 / 5 | 40% | 0 / 5 | 0% | 0 / 5 | 0% |
| **All 12** | **30 / 65** | **46%** | **26 / 60** | **43%** | **23 / 79** | **29%** |
| All excluding the oracle week 2026-07-06 (9 maps) | 21 / 50 | 42% | 15 / 45 | 33% | 7 / 58 | 12% |

The two 100% E3 maps are the oracle week. Their setup prices are within one pip of the operator's own entries and TPs (for example DX4 101.235/100.685 against 101.235/100.68, and DX8 TP 100.94 against 100.94). On the three other weeks, E3 is 7/58.

## The five defects that cost the most

1. **SS day box sized or placed off price, so whole weeks of E2 go to zero (13 of the 34 wrong days).**
   - GBPUSD 2026-05-18: box 1.33197-1.33941. Mon ran to 1.34494 and all five days closed above the box.
   - EURUSD 2026-05-18: a 27-pip box 1.16218-1.16493 in a week that ranged 1.1576-1.1662. Four days closed outside and Fri never touched it.
   - GBPUSD 2026-04-20: Mon/Tue box 1.3466-1.3493 (27 pips) while the days traded 1.3474-1.3544; Wed box only 9 pips (1.34879-1.34973).
2. **No E1 zone on the side where the week turned (E1 turning points with no zone, and nothing for E3 to trade).**
   - DXY 2026-10-05: no zone above 102.051 while the week topped at 102.433 (Mon), 102.499 (Wed) and 102.467 (Thu).
   - DXY 2026-05-18: no zone above 99.037; highs 99.472 (Wed) and 99.515 (Thu).
   - EURUSD 2026-10-05: no zone below price; lows 1.11645 (Wed) and 1.11719 (Thu), high 1.12767 (Tue).
3. **Stops a pip or three inside the sweep: the setup is stopped, then price runs through its TP.**
   - DXY 2026-05-18 DX1: SL 99.459, taken by 99.471 Wed 08:00; then 98.966 Wed 15:00.
   - EURUSD 2026-05-18 EU1: SL 1.16575, taken by 1.16608 Mon 20:00; then 1.1592 Tue.
   - DXY 2026-10-05 DX2: SL 101.776, taken by 101.754 Tue 12:00; then +75 pips.
   - DXY 2026-04-20 DX1: SL 98.471, taken by 98.567 Tue 17:00.
   - GBPUSD 2026-07-06 GB4: SL 1.34396, taken by 1.34517 Fri 02:00. It had been 44 pips in profit Thu, but its TP of 1.33506 was far past the operator's 1.33882.
4. **Entries one or two pips short of the turn, so a whole map has no fills and its ladders never go live.**
   - EURUSD 2026-04-20: EU1, EU2 and EU3 all at 1.17920 against a week high of 1.17910 (Mon 23:00), leaving 0 of 7 legs.
   - GBPUSD 2026-05-18: GB2 at 1.33197 against a Mon low of 1.33217, before a 128-pip rally.
   - DXY 2026-04-20: DX1 short 98.415 against a Mon high of 98.395, and DX6/DX7 never live.
   - EURUSD 2026-10-05: EU1 filled at the exact low 1.11645, but its TP of 1.12491 is 6.4 pips past the week high, so the trade was still open at the end.
5. **Friday RWL path draws the extreme at the end of the day; every one came in Asia or early London and the day then ran the other way (6 Fridays WRONG).**
   - DXY 2026-07-06: low 100.598 at 02:00.
   - EURUSD 2026-07-06: high 1.14608 at 02:00.
   - GBPUSD 2026-07-06: high 1.34517 at 02:00.
   - DXY 2026-04-20: high 98.915 at 03:00.
   - EURUSD 2026-04-20: low 1.16729 at 03:00.
   - GBPUSD 2026-04-20: low 1.34532 at 03:00.

   Related: the Thursday BS boxes sit wholly off the day on DXY 2026-04-20 (box 98.02-98.502, day 98.534-98.939), EURUSD 2026-04-20 (box 1.1738-1.17865, day 1.16691-1.17165) and GBPUSD 2026-07-06.

Presentation problems seen on every map but not in the top five:
- Day-shape and setup labels are printed on candles and on each other. The worst case is EURUSD 2026-05-18 at 1.1646-1.1650, where an E1 label, a V1 label, the EU1 label and two option-strike labels are overprinted.
- Stacks of more than 10 translucent fills hide the candles in the active band.

What I could not judge from the frames: exact 1H closes against box edges in the crowded `_week` frames. I read those from the 1H bars instead.
