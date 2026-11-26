# G1 count 3: outside reviewer (fresh context, no earlier count read)

Reviewer: an outside agent with fresh context. It did not build the tool and has not read audit/G1_count_dryrun*.md, memory/ or e1_tool code.
Sources: every frame in evidence/s3c/ (36 PNG, each opened and looked at), audit/g1_facts_c/*.txt for exact prices, 1H/15m bars read-only through e1_tool/e1_data.py bars() to check times, closes and fills.

## Counting rules applied (so anyone can recount)

- **Zone verdict (E1).** Every Engine 1 drawing counts: IP zones, the gap in-fill box, S/D candle zones, LSZ boxes and the unlabelled V1 liquidity bands. Amber option-strike lines are levels, not zones, so they are not counted.
  - REACTED: a sharp rejection, or consolidation in or around the zone, with the turn inside the zone or within about 3 pips (DXY 0.03) of its edge. For an LSZ, the turn may be anywhere inside its dotted sweep reach.
  - PIERCED: price crossed the zone and the turn, if any, came beyond that tolerance or beyond the sweep reach.
  - When a zone was touched several times, the verdict follows the dominant touch, and the other touches are noted.
  - Not reached: zones price never touched. They are left out of the ratio.
- **Missing points.** Obvious 1H turning points of the forecast week with no Engine 1 drawing within that tolerance are added to the denominator.
- **E1 %** = reacted / (reached + missing). A zone that is bloated, bunched (several drawings stacked on one price), or floating is listed as a defect. It is not deducted from the ratio, and the "none bloated / bunched / floating / missing" condition is reported separately as MET or FAILED.
- **E2 (day RIGHT / WRONG).** A day is RIGHT when shape, direction and key move match that day's candles. If the tag's shape is not what the candles did (for example BS tagged and a spike plus full reversal happened), or the direction is wrong, the day is WRONG.
- **E3 (obvious trades).**
  - For 2026-07-06 the obvious trades are the operator's trades in golden_week.json, minus any whose entry was only available before Mon 06:00 UTC (checked on 15m bars).
  - For the other weeks they are the clean zone-to-zone 1H moves, listed from the _zones frame and the bars BEFORE the setups were looked at.
  - CAUGHT means a setup in the same direction at the same turn (entry within about 5 pips of the turn, or at the zone the turn came from) that filled and hit TP before SL, per the 15m outcome in the facts file, spot-checked on the bars.
  - Every stopped setup is named as a loss, even if price later reached its TP.

---
## 1. DXY 2026-07-06 (anchor week)

Week: Mon H 101.145 L 100.838 | Tue 101.126/100.803 | Wed 101.275/100.946 | Thu 101.071/100.786 | Fri 100.997/100.598.

**Obvious trades (operator, golden_week.json), written before looking at the setups.**
- Trade 1 (Mon LONG 100.945) is OUT of the window. 100.945 traded only from 01:15 to 05:30 UTC. After 06:00 price stayed above 100.987 until the TP area was reached.
- In-window trades (7):

| # | Trade |
|---|---|
| op2 | Mon SHORT 101.14 -> 100.845 |
| op3 | Tue LONG 100.845 -> 101.19 |
| op4 | Wed SHORT 101.19 -> 100.975 |
| op5 | Wed LONG 100.975 -> 101.24 |
| op6 | Wed SHORT 101.235 -> 100.68 |
| op7 | Thu SHORT 100.975 (ladder) |
| op8 | Fri LONG 100.615 -> 100.94 |

**E1 zones reached**

| Zone | Verdict |
|---|---|
| UPPER RESISTANCE 101.199-101.262 | REACTED (Wed 01:00 high 101.215 -> 100.95; Wed 15:00 high 101.275 -> 100.946) |
| EQUILIBRIUM 100.985-101.077 | REACTED (Thu 10:00-11:00 rejection 101.039; Wed 07:00 dip 100.95 bounce; consolidation Thu night). Mon 06:00 crossed up through it with no reaction. |
| MID-RANGE SUPPORT 100.724-100.815 | REACTED (Thu 06:00 low 100.786 -> 101.03). Fri 02:00 crossed it down like paper. |
| GAP IN-FILL 100.599-100.659 | REACTED (Fri 02:00 low 100.598 = week low -> 100.997) |
| 1H MoM supply 101.027-101.153 | REACTED (Mon high 101.145 -> 100.838). Wed broke through. |
| 1H Mitigated 2x demand 100.825-100.851 | REACTED (Mon 18:00 low 100.838; Tue 02:00 low 100.816 -> 101.196) |
| 1H BoM demand 100.654-100.748 | PIERCED (Fri 02:00 crossed the whole box; turn 100.598 is 5.6 pips below it; 2H close 100.625 below) |
| LSZ supply 100.978-101.028 (reach 101.128) | REACTED (Mon turn 101.145, 1.7 pips past reach) |
| LSZ supply 100.942-100.992 (reach 101.092) | PIERCED (Mon ran 5 pips past reach before turning) |
| LSZ demand 100.826-100.876 (reach 100.726) | REACTED (Tue 100.803, Thu 100.786 inside reach) |
| LSZ demand 100.603-100.653 (reach 100.503) | REACTED (Fri 100.598) |
| LSZ demand 100.558-100.608 (reach 100.458) | REACTED (Fri 100.598) |
| V1 band 101.245-101.305 | REACTED (Wed high 101.275) |
| V1 band 101.067-101.127 | REACTED (Mon 08:00-15:00 consolidation under 101.145) |
| V1 band 100.957-101.017 | REACTED (Wed 07:00 low 100.95/100.97; Thu consolidation) |

- Not reached: KEY SUPPORT 100.470-100.530, 4H BoM supply 101.316-101.430, 1H MoM supply 101.314-101.360, LSZ 101.380-101.430, band 101.372-101.432, band 100.498-100.558.
- Missing turning points: none. Every turn (101.145, 100.803, 101.215, 100.95, 101.275, 100.786, 101.039, 100.598) has a drawing.

**E1 = 13 / 15 = 87%.** The "none bloated / bunched" condition FAILED:
- 21 Engine 1 drawings tile the whole 100.47-101.53 range with almost no gap.
- 100.94-101.13 holds 5 stacked drawings (EQUILIBRIUM, 2 LSZ, 2 bands, 1H supply).
- 100.56-100.66 holds 3 (gap in-fill and 2 LSZ).
- A zone at every price makes "no missing point" trivially true.

**E2**

| Day | Verdict |
|---|---|
| Mon SS range 100.724-101.262 | RIGHT. 100.84-101.145 oscillation inside the bounds. |
| Tue SS | RIGHT. 100.803-101.126 inside the bounds. |
| Wed SS+RWL+BS down | RIGHT. Dip 100.95, surge 101.275, sell-off to 100.946; the operator's own tag is the same. |
| Thu BS down (box 100.968-101.247, key 1H BoM) | WRONG. The candles were a drop 100.97 -> 100.786 at 06:00, then a full recovery to 101.039 by 11:00, closing 100.937: spike-and-recover, not a decisive break that surges to the next zone. The day box sits above Thursday's price, and the key zone (1H BoM 100.654-100.748) was not reached. |
| Fri BS+WL+RWL | RIGHT. Flush to 100.598, recovery to 100.997. |

**E2 = 4 / 5 = 80%.**

**E3**

| Trade | Verdict |
|---|---|
| op2 | CAUGHT. DX2 SHORT 101.138, TP 100.825 Tue 01:30. |
| op3 | CAUGHT. DX3 LONG 100.851, TP 101.189 Tue 23:45. |
| op4 | CAUGHT. DX5 SHORT 101.203, Wed 01:00 high 101.215, TP 100.980 Wed 07:15. |
| op5 | CAUGHT. DX6 LONG 100.980, TP 101.235 Wed 09:00 high 101.239. |
| op6 | CAUGHT. DX4 SHORT 101.235, SL 101.322 untouched (week high 101.275), TP 100.685 Fri 02:00. |
| op7 | CAUGHT. DX7 SHORT 100.980, SL 101.077 (Thu high 101.039; it survived by 4 pips), TP Fri 02:00. |
| op8 | CAUGHT. DX8 LONG 100.628, TP 100.940 Fri 14:00. |

- Stopped setups: none.
- DX1 (SHORT 101.203) never filled.
- DX2 is listed as filled Mon 06:00, but price first reached 101.138 at Mon 09:45-10:00. The "first-contact" band at the zone front edge (~101.03) is what filled at 06:00, so the real fill price is ~11 pips below the printed entry. The outcome is unchanged.

**E3 = 7 / 7 = 100%.**

**Presentation**
- In both two-week frames the chart is a wall of overlapping boxes, and candles in the history half are hard to read.
- Several labels overlap one another:
  - the EQUILIBRIUM ZONE label runs over candles and over the "1H (Unmitigated) | MoM" label;
  - "DX1 SS S 7.3R" overlaps "DX2 SS S 4.2R";
  - "Thu BS down 40%" collides with "2.2bn Option Strike Target";
  - the Fri tag (purple, "Fri BS+WL+RWL down 32%") overlaps "1.4bn Option Strike Target" and is barely legible.
- In _week the GAP IN-FILL label is cut to "ATE | 30-50% ZFP".

---
## 2. EURUSD 2026-07-06 (anchor week)

Week: Mon 1.14449/1.14083 | Tue 1.14480/1.14080 | Wed 1.14315/1.13911 | Thu 1.14494/1.14141 | Fri 1.14608/1.14114.

**Obvious trades (operator).**
- op1 (Mon SHORT 1.14322 -> 1.14103) is OUT of the window. Its entry was the 00:00-04:00 UTC drift at 1.1432-1.1441. After 06:00 the next print at 1.1432 was Mon 16:00, and by then the move to 1.14103 had already happened (Mon 10:00).
- In-window trades (7):

| # | Trade |
|---|---|
| op2 | Mon LONG 1.14106 -> 1.14442 |
| op3 | Tue SHORT 1.14441 -> 1.14004 |
| op4 | Wed LONG 1.14012 -> 1.14276 |
| op5 | Wed SHORT 1.14277 -> 1.1395 |
| op6 | Wed LONG 1.13953 -> 1.14544 |
| op7 | Thu LONG 1.14233 -> 1.14544 (reinforcement) |
| op8 | Fri SHORT 1.14578 -> 1.14205 |

**E1 zones reached**

| Zone | Verdict |
|---|---|
| UPPER RESISTANCE 1.14444-1.14533 | REACTED (Mon 18:00-Tue 01:00 cap 1.1445-1.1448 -> 1.1408; Thu 06:00 1.14494 -> 1.14209). Fri 02:00 broke it to 1.14608. |
| MID-RANGE SUPPORT 1.13977-1.14053 | REACTED (Tue 23:00-Wed 01:00 lows 1.14001/1.13983 -> 1.14315; Wed 09:00-15:00 base 1.1391-1.1396 just under it -> 1.14303) |
| GAP IN-FILL 1.14593-1.14653 | REACTED (Fri high 1.14608 -> 1.14114) |
| GAP IN-FILL 1.14220-1.14280 | REACTED (Tue 06:00-09:00 floor 1.14246; Wed 07:00 cap 1.14315 just above it; Thu 10:00 low 1.14209) |
| 1H Mitigated 4x supply 1.14601-1.14677 | REACTED (Fri 1.14608) |
| 4H Mitigated 2x supply 1.14475-1.14635 | REACTED (Mon 23:00 1.1448, Thu 1.14494, Fri 1.14608) |
| 1H BoM supply 1.14375-1.14421 | REACTED (Tue 12:00 1.14421 -> 1.1418; Thu 15:00-17:00 caps 1.1440-1.1441) |
| 1H MoM demand 1.14004-1.14147 | REACTED (Mon 09:00-14:00 base 1.14083 -> 1.14449; Tue 21:00 1.14013; Fri 14:00 1.14117) |
| 1H BoM demand 1.13815-1.13886 | REACTED (Wed 15:00 low 1.13911, 2.5 pips above its top -> 1.14303) |
| LSZ supply 1.14573-1.14623 (reach 1.14723) | REACTED (Fri 1.14608) |
| LSZ supply 1.14360-1.14410 (reach 1.14510) | REACTED (Mon-Tue run to 1.1448 inside reach, then down; Thu 1.14494) |
| LSZ demand 1.14206-1.14256 (reach 1.14106) | REACTED (Mon low 1.14083, 2.3 pips past reach; Thu 1.14209). Tue 19:00-21:00 ran 2.6-9 pips past the reach. |
| V1 band 1.14269-1.14339 | REACTED (Wed 07:00 cap 1.14315, Wed 19:00 cap 1.14303) |
| V1 band 1.14108-1.14178 | REACTED (Mon base 1.14083-1.14111; Wed 20:00-21:00 1.1414-1.1415) |

- Not reached: GAP 1.14777-1.14837, 1H BoM supply 1.14738-1.14807, 4H BoM demand 1.13721-1.13832, LSZ 1.14678-1.14728, band 1.14658-1.14728, band 1.13810-1.13880.
- Missing turning points: none.

**E1 = 14 / 14 = 100%.** The "none bloated / bunched" condition FAILED:
- 20 drawings tile 1.1372-1.1484. There is barely a price without a box.
- 1.1436-1.1465 holds 8 overlapping drawings (UPPER RESISTANCE, 4H supply, 1H supply x2, gap, LSZ x2, band).
- The ratio is inflated by coverage, not by selection.

**E2**

| Day | Verdict |
|---|---|
| Mon SS | RIGHT. 1.14083-1.14449 inside 1.13977-1.14533. |
| Tue SS | RIGHT. 1.1408-1.1448 inside the bounds. |
| Wed SS+RWL+BS up | RIGHT. Up to 1.14315, drop to 1.13911, rally to 1.14303. |
| Thu BS up (box 1.13962-1.14248, key 4H supply) | WRONG. Spike to 1.14494 at 06:00, back to 1.14209 by 10:00, then chop 1.1423-1.1446. There was no decisive break-and-surge, and the box sits below the day's price. |
| Fri BS+WL+RWL up | RIGHT. Spike 1.14608 into the 4H / gap supply, then rejection to 1.14114. |

**E2 = 4 / 5 = 80%.**

**E3**

| Trade | Verdict |
|---|---|
| op2 | CAUGHT. EU4 LONG 1.14095, TP 1.14434 Mon 18:45, SL 1.14037 untouched. |
| op3 | CAUGHT. EU1 SHORT 1.14442, TP 1.14063 Tue 21:15, SL 1.14508 untouched (high 1.1448). |
| op4 | CAUGHT. EU7 LONG 1.14018, TP 1.14269 Wed 07:15. |
| op5 | CAUGHT. EU5 SHORT 1.14269, TP 1.13940 Wed 11:30. |
| op6 | CAUGHT. EU6 LONG 1.13940, TP 1.14555 Fri 02:00 (SL 1.13872; Wed low 1.13911). |
| op7 | MISSED. Thursday's reinforcement dip (Thu 10:00 low 1.14209, operator entry 1.14233) had no order. EU8 (Thu Ladder LONG 1.14164) filled Wed 21:00 in a different zone (band 1.14108-1.14178), 7 pips below. Price never came back to it on Thursday. |
| op8 | CAUGHT. EU9 SHORT 1.14598, TP 1.14239 Fri 12:45 (SL 1.14653; high 1.14608). |

Stopped setups (losses):
- **EU2** SHORT 1.14385 (Mon 17:15 -> SL 1.14451 Mon 21:45).
- **EU4 re-armed** LONG 1.14095 (Tue 19:00 -> SL Tue 21:30).
- **EU10** "Fri Ladder" LONG 1.14401: it filled on THURSDAY 06:15 and was stopped Thu 07:00. A Friday setup was live and lost a day early.

**E3 = 6 / 7 = 86%.** There are 3 losses.

**Presentation**
- Same wall of boxes as DXY.
- Overlapping labels:
  - "GAP IN-FILL" is printed on top of "1H (Mitigated 4x) | MoM";
  - the UPPER RESISTANCE and MID-RANGE SUPPORT labels run across candles;
  - the "LSZ demand-side" label is half hidden by candles.
- In _all, "EU10 Ladder L 3" is cut off at the right edge, and "Thu BS up 40%" overlaps the EU8 label.
- The Fri tag is purple on red and illegible.
- In _week three labels are cut to "ATE | 30-50% ZFP".

---
## 3. GBPUSD 2026-07-06 (anchor week)

Week: Mon 1.33972/1.33286 | Tue 1.34015/1.33487 | Wed 1.34104/1.33222 | Thu 1.34308/1.33799 | Fri 1.34517/1.33917.

**Obvious trades (operator).** All 7 are in the window. op1's 1.33331 traded again Mon 06:15-07:00, after 06:00.

| # | Trade |
|---|---|
| op1 | Mon LONG 1.33331 -> 1.33941 |
| op2 | Mon SHORT 1.33934 -> 1.33347 |
| op3 | Wed LONG 1.3333 -> 1.34246 |
| op4 | Wed LONG 1.33629 -> 1.34246 (reinforcement) |
| op5 | Thu SHORT 1.34246 -> 1.33882 |
| op6 | Thu LONG 1.33829 -> 1.34485 |
| op7 | Fri SHORT 1.34481 -> 1.34021 |

**E1 zones reached.** There are 34 drawings; 27 were reached.

| Zone | Verdict |
|---|---|
| RESISTANCE CEILING 1.34484-1.34548 | REACTED (Fri 02:00 high 1.34517 -> 1.33918) |
| UPPER RESISTANCE 1.33933-1.34005 | REACTED (Mon 18:00-Tue 02:00 cap 1.3397-1.34015 -> 1.33487) |
| UPPER RESISTANCE 1.33643-1.33717 | REACTED (Wed 06:00-07:00 cap 1.337 -> 1.33222; Tue floor 1.3360-1.3369). Mon 15:00 crossed up with no reaction. |
| UPPER RESISTANCE 1.33435-1.33521 | REACTED (Mon cap 1.33502-1.33516; Tue 21:00-Wed 05:00 floor 1.3342-1.3345) |
| MID-RANGE SUPPORT 1.33225-1.33285 | REACTED (Wed 09:00 low 1.33222 -> 1.34104; Mon 07:00 1.33286) |
| GAP 1.34234-1.34294 | REACTED (Thu 06:00 1.34308 -> 1.33807; Fri 04:00-07:00 base 1.3420-1.3427) |
| GAP 1.34029-1.34089 | REACTED (Wed 17:00-19:00 caps 1.3406-1.3410; Fri 08:00-09:00 low 1.34085) |
| GAP 1.33744-1.33804 | REACTED (Tue 06:00-07:00 1.3375, Wed 21:00 1.33799, Thu 12:00 1.33807) |
| 1H BoM supply 1.34502-1.34599 | REACTED (Fri 1.34517) |
| 4H BoM supply 1.34264-1.34340 | REACTED (Thu 06:00 1.34308) |
| 4H MoM supply 1.34035-1.34162 | REACTED (Wed 17:00-19:00 caps) |
| 1H MoM supply 1.33941-1.34032 | REACTED (Mon-Tue cap) |
| 1H BoM supply 1.33623-1.33764 | REACTED (Wed 07:00 cap 1.337). Mon crossed it. |
| 1H MoM supply 1.33544-1.33582 | REACTED (Tue 20:00-Wed 05:00 caps 1.3355-1.3359) |
| 1H MoM demand 1.33082-1.33333 | REACTED (Mon 06:00-09:00 1.33286-1.33312; Wed 1.33222) |
| LSZ supply 1.33796-1.33846 (reach 1.33946) | PIERCED (Mon-Tue went to 1.34015, 7 pips past reach) |
| LSZ supply 1.33760-1.33810 (reach 1.33910) | PIERCED (same run, 10 pips past reach) |
| LSZ supply 1.33516-1.33566 (reach 1.33666) | REACTED (Tue-Wed caps 1.3355-1.3359; Wed 07:00 1.337 -> 1.33222) |
| LSZ demand 1.33341-1.33391 (reach 1.33241) | REACTED (Mon 1.33286; Wed 1.33222) |
| LSZ demand 1.33340-1.33390 (reach 1.33240) | REACTED. A duplicate of the box above (1 pip apart; two identical labels on the chart). |
| V1 band 1.34386-1.34476 | REACTED (Fri top 1.3437-1.3452) |
| V1 band 1.34145-1.34235 | REACTED (Thu 07:00-09:00 / Fri 05:00-07:00 bases) |
| V1 band 1.33976-1.34066 | REACTED (Mon-Tue cap) |
| V1 band 1.33715-1.33805 | REACTED (Tue 1.3375) |
| V1 band 1.33583-1.33673 | REACTED (Tue 14:00-19:00 lows 1.3360) |
| V1 band 1.33406-1.33496 | REACTED (Wed 00:00-01:00 1.3342) |
| V1 band 1.33155-1.33245 | REACTED (Wed 1.33222) |

- Not reached: both KEY SUPPORT BANDs, 1H MoM demand 1.32862-1.32928, 4H MoM demand 1.32639-1.32835, 1H BoM demand 1.32744-1.32800, bands 1.34540-1.34630 and 1.32932-1.33022.
- Missing turning points: none.

**E1 = 25 / 27 = 93%.** The "none bloated / bunched" condition FAILED:
- 34 drawings tile 1.3264-1.3463, with a box at every price.
- There are three UPPER RESISTANCE zones stacked within 57 pips.
- A duplicate LSZ pair sits at 1.3334/1.3334.
- Five drawings are stacked at 1.3393-1.3410.
- Seven drawings are stacked at 1.3374-1.3385.

**E2**

| Day | Verdict |
|---|---|
| Mon SS (1.33082-1.34032) | RIGHT. Floor 1.33286 to ceiling 1.33972 inside the bounds. |
| Tue SS | RIGHT. 1.33487-1.34015 inside the bounds. |
| Wed SS+RWL+BS up | RIGHT. Dip 1.33222, then a surge to 1.34104. |
| Thu BS up (box 1.33270-1.33825) | WRONG. Spike to 1.34308 at 06:00, rejected to 1.33807, then chop. That is a spike-and-reject, not a sustained BS. The day box lies entirely below Thursday's candles (Thu low 1.33799 = box top). |
| Fri BS+WL+RWL up | RIGHT. Spike to 1.34517, rejection to 1.33918. |

**E2 = 4 / 5 = 80%.**

**E3**

| Trade | Verdict |
|---|---|
| op1 | CAUGHT. GB1 LONG 1.33333, TP 1.33941 Mon 18:45. |
| op2 Mon SHORT 1.33934 | MISSED. The tool suppressed its own "Mon SS SHORT 1.33959" (NARRATIVE, ZFP 45 > 30). Price then fell 45 pips. |
| op3 | CAUGHT. GB2 LONG 1.33245, TP 1.34254 Thu 06:15 (SL 1.33012). |
| op4 Wed LONG 1.33629 | MISSED. There was no order at 1.336, and GB3 (1.33473) never filled. |
| op5 Thu SHORT 1.34246 | MISSED. GB4 SHORT 1.34254 filled Thu 06:15, but its TP was 1.33506, 30 pips below the actual 1.33807 turn. It was STOPPED Fri 02:00 at 1.34396. |
| op6 Thu LONG 1.33829 | MISSED. There was no order at the Thu 12:00 low 1.33807. GB5 (1.33888) had already filled and been used Wed 21:00. |
| op7 Fri SHORT 1.34481 | MISSED. There was no short at the 1.3448-1.3455 ceiling; the only short (GB4) was stopped by this very rally. |

- Stopped setups: **GB4** "Fri RWL" SHORT 1.34254. It filled Thursday (a Friday setup live a day early) and was stopped Fri 02:00.
- GB5 (labelled "Fri Ladder") also filled on Wednesday, two days before its day. It won, but the day label is meaningless.

**E3 = 2 / 7 = 29%.** There is 1 loss.

**Presentation**
- The _zones frame is the most cluttered of the three: 34 boxes.
- Labels print on top of each other:
  - at 1.3400-1.3405: "4H (Unmitigated) | MoM", "GAP IN-FILL", "1H (Unmitigated) | MoM", "UPPER RESISTANCE";
  - the two LSZ labels "sweep to 1.33946" and "sweep to 1.33910";
  - "1H (Unmitigated) | BoM" over "4H (Unmitigated) | MoM" at 1.3275;
  - "1H (Unmitigated) | BoM" over "RESISTANCE CEILING".
- The "LSZ demand-side | sweep to 1.33241" label is drawn twice on the same spot.
- GB1 / GB2 labels sit under zone labels.
- "GB5 Ladder L 4." is cut at the right edge.
- The Fri tag is illegible.

---
## 4. DXY 2026-04-20

Week: Mon 98.395/98.006 | Tue 98.567/98.041 | Wed 98.643/98.211 | Thu 98.939/98.534 | Fri 98.915/98.489.

**Obvious trades.** These were listed from the _zones frame and the 1H bars before the setups were read.

| # | Trade |
|---|---|
| T1 | Mon SHORT 98.39 (Mon 05:00-06:00 top, LSZ / band 98.30-98.40) -> 98.01 (MID-RANGE SUPPORT / gap 97.988-98.048), Mon 15:00 |
| T2 | Mon-Tue LONG 98.01-98.05 (base Mon 15:00-Tue 00:00) -> 98.55 (UPPER RESISTANCE 98.456-98.541), Tue 17:00 |
| T3 | Tue SHORT 98.55-98.57 (UPPER RESISTANCE) -> 98.21 (gap 98.220-98.280), Wed 05:00 |
| T4 | Wed LONG 98.21 (gap 98.22-98.28) -> 98.64 Wed 20:00 / 98.80 Thu 10:00 |
| T5 | Thu SHORT 98.80 (1H supply 98.675-98.845) -> 98.534 (UPPER RESISTANCE / band 98.46-98.56), Thu 14:00 |
| T6 | Thu LONG 98.534-98.55 -> 98.90-98.94 (4H BoM supply 98.884-99.031), Thu 17:00 |
| T7 | Fri SHORT 98.90-98.94 (4H BoM / UPPER RESISTANCE 98.939) -> 98.49-98.53 (UPPER RESISTANCE 98.456-98.541), Fri 15:00-20:00 |

**E1 zones reached (range 98.006-98.939)**

| Zone | Verdict |
|---|---|
| UPPER RESISTANCE 98.939-99.005 | REACTED (Thu 17:00 98.939 -> 98.688; Fri 03:00 98.915 -> 98.489) |
| UPPER RESISTANCE 98.456-98.541 | REACTED (Tue 17:00/19:00 cap 98.567 -> 98.211; Thu 14:00 low 98.534; Fri close 98.49-98.53). Wed 15:00 broke up through it. |
| MID-RANGE SUPPORT 98.058-98.145 | REACTED (Mon 15:00-Tue 06:00 consolidation 98.01-98.16) |
| GAP 98.806-98.866 | REACTED (Thu 19:00-Fri 01:00 consolidation) |
| GAP 98.667-98.727 | REACTED (Thu 02:00-04:00 cap 98.714; Thu 11:00-13:00 consolidation) |
| GAP 98.220-98.280 | REACTED (Mon 06:00-12:00 consolidation; Wed 05:00 low 98.211 -> 98.643) |
| GAP 97.988-98.048 | REACTED (Mon 15:00 low 98.006) |
| 4H BoM supply 98.884-99.031 | REACTED (Thu 17:00, Fri 03:00) |
| 1H MoM supply 98.675-98.845 | REACTED (Thu 10:00 98.803 -> 98.534) |
| 1H MoM supply 98.402-98.439 | REACTED (Tue 21:00-Wed 04:00 consolidation under it) |
| 1H MoM demand 97.937-98.045 | REACTED (Mon 98.006) |
| LSZ supply 98.389-98.439 (reach 98.539) | REACTED (Tue 98.567, 2.8 pips past reach) |
| LSZ supply 98.345-98.395 (reach 98.495) | REACTED (Mon 06:00 top 98.395 -> 98.006). Tue ran 7 pips past reach. |
| LSZ supply 98.242-98.292 (reach 98.392) | REACTED (Tue 08:00-13:00 caps 98.29-98.31 -> 98.12) |
| LSZ supply 98.241-98.291 (reach 98.391) | REACTED. A duplicate of the box above (1 pip apart). |
| LSZ demand 98.261-98.311 (reach 98.161) | REACTED (Wed 05:00 98.211). Mon 13:00 ran 8 pips past reach. |
| V1 bands 98.903-98.967, 98.804-98.868, 98.689-98.753, 98.561-98.625, 98.461-98.525, 98.300-98.364, 98.182-98.246, 98.014-98.078 | all REACTED (8) |

- Not reached: KEY SUPPORT 97.725-97.799, 1H BoM demand 97.632-97.828, 4H BoM demand 97.576-97.728, LSZ demand 97.632-97.682, bands 97.920-97.984, 97.768-97.832, 97.666-97.730.
- Missing turning points: none (98.395, 98.006, 98.567, 98.211, 98.643, 98.553, 98.803, 98.534, 98.939, 98.915, 98.489 all sit in a drawing).

**E1 = 24 / 24 = 100%.** The "none bloated / bunched" condition FAILED:
- 31 drawings tile 97.53-99.03, every 5-10 pips.
- 98.24-98.44 holds 4 overlapping supply LSZ (two of them identical), a demand LSZ, a 1H supply, a gap and a band.
- In the _zones frame the green LSZ stack at 98.25-98.40 hides the candles.
- The 100% is a coverage artefact: a zone exists wherever price turns because a zone exists at nearly every price.

**E2**

| Day | Verdict |
|---|---|
| Mon SS (97.937-98.439) | RIGHT. 98.006-98.395 inside the bounds. |
| Tue SS+RWL+BS up | RIGHT. Asian range, then a break up to 98.567. The drawn RWL dip to 97.92 never came, but shape and direction held. |
| Wed BS up | RIGHT. 98.211 -> through UPPER RESISTANCE to 98.643. |
| Thu BS+RWL up | RIGHT. Up to 98.80, RWL dip 98.534, then up to 98.939 (the 4H BoM supply). |
| Fri | WRONG. "no designation (chain ended)", while Friday dropped 43 pips, 98.915 -> 98.489. |

**E2 = 4 / 5 = 80%.**

**E3**

| Trade | Verdict |
|---|---|
| T1 | CAUGHT. DX1 SHORT 98.415, filled Mon 06:15 (first contact), TP 98.045 Mon 15:15. |
| T2 | CAUGHT. DX2 LONG 98.045, TP 98.402 Tue 16:45. DX4 LONG 98.045 also hit TP 98.300. |
| T3 Tue SHORT 98.55 | MISSED. The "Tue RWL down" was rejected (RRR 1.79). |
| T4 Wed LONG 98.21 | MISSED. DX5 (Wed Ladder LONG 98.215) is drawn on the chart, but "parent DX3 not filled -> order never live". |
| T5 Thu SHORT 98.80 | MISSED. There was no setup. |
| T6 Thu LONG 98.54 | MISSED. DX6 (Thu Ladder LONG 98.660) is drawn, but never live (same parent rule). |
| T7 Fri SHORT 98.90 | MISSED. There was no setup: the "Thu RWL down" was rejected (RRR 1.99), and there is no Friday designation. |

- Stopped setups: none.
- DX3 never filled.
- DX5 and DX6 are drawn as position boxes on the chart but were never live orders. The chart shows two trades that the tool says do not exist.

**E3 = 2 / 7 = 29%.**

**Presentation**
- The _week frame's price axis is not fitted to the week: it runs 97.5-99.3 because of a spike candle after Friday's close, which squashes the week's candles.
- The DX3 / DX2 / DX4 labels are printed on top of one another at 98.05-98.10.
- The Tue day tag overlaps candles and the DX5 label.
- The Thu tag (purple) is illegible over the candles.
- The alternative-chain dotted lines dive to 97.62, far below anything price did.
- The LSZ labels at 98.25-98.40 overlap each other ("sweep to 98.161" over "sweep to 98.392").

