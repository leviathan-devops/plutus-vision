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

---
## 5. EURUSD 2026-04-20

Week: Mon 1.17902/1.17475 | Tue 1.17910/1.17187 | Wed 1.17624/1.17030 | Thu 1.17165/1.16691 | Fri 1.17230/1.16729.

**Obvious trades.** These were listed before the setups were read.

| # | Trade |
|---|---|
| T1 | Mon LONG 1.1748-1.1755 (EQUILIBRIUM 1.17497-1.17573) -> 1.1789 (1H supply 1.17847-1.17988), Mon 06:00-15:00 |
| T2 | Tue SHORT 1.1785-1.1791 (1H supply) -> 1.1720 (gap 1.17203-1.17263), Tue 19:00 |
| T3 | Tue-Wed LONG 1.1719-1.1724 (gap 1.172) -> 1.1762 (LSZ 1.17575-1.17625), Wed 05:00 |
| T4 | Wed SHORT 1.1756-1.1762 -> 1.1703 (MID-RANGE SUPPORT 1.16973-1.17033), Wed 20:00 |
| T5 | Thu SHORT 1.1716 (band 1.17126-1.17217, Thu 14:00) -> 1.1669 (1H BoM demand 1.16638-1.16754), Thu 17:00 |
| T6 | Fri LONG 1.1673-1.1680 (gap 1.16744-1.16804) -> 1.1720-1.1723 (gap 1.17203), Fri 20:00 |

**E1 zones reached (range 1.16691-1.17910)**

| Zone | Verdict |
|---|---|
| UPPER RESISTANCE 1.17706-1.17791 | REACTED (Mon 07:00 1.17718 -> 1.17551; Tue 02:00-06:00 shelf) |
| EQUILIBRIUM 1.17497-1.17573 | REACTED (Mon 06:00 low 1.1747 -> 1.1791; Tue 08:00-14:00 shelf) |
| MID-RANGE SUPPORT 1.16973-1.17033 | REACTED (Wed 20:00 1.1703; Thu 00:00-08:00 chop; Fri 13:00 1.16986) |
| GAP 1.17347-1.17407 | REACTED (Tue 21:00-Wed 04:00 base) |
| GAP 1.17203-1.17263 | REACTED (Tue 19:00 1.17187 -> 1.17624; Wed 13:00 1.17237) |
| GAP 1.16744-1.16804 | REACTED (Thu 10:00-11:00 1.1679 -> 1.17165; Fri 03:00 1.16729) |
| 1H MoM supply 1.17847-1.17988 | REACTED (Mon 15:00-Tue 01:00 top 1.1791 -> 1.17187) |
| 1H MoM demand 1.17004-1.17207 | REACTED (Tue 1.17187; Wed 15:00-23:00 base) |
| 4H BoM demand 1.16809-1.16996 | REACTED (Thu 02:00-04:00 1.1695; Thu 18:00-Fri 09:00 base) |
| 1H BoM demand 1.16638-1.16754 | REACTED (Thu 17:00 1.16691) |
| 4H MoM demand 1.16543-1.16748 | REACTED (Thu 17:00 1.16691) |
| LSZ supply 1.17575-1.17625 (reach 1.17725) | REACTED (Mon 07:00 1.17718; Wed 05:00 1.17624 -> 1.1703) |
| LSZ demand 1.17592-1.17642 (reach 1.17492) | REACTED (Tue 08:00-13:00 lows 1.1754-1.1757) |
| LSZ demand 1.17527-1.17577 (reach 1.17427) | REACTED (Mon 1.1747) |
| LSZ demand 1.17277-1.17327 (reach 1.17177) | REACTED (Tue 1.17187) |
| LSZ demand 1.16638-1.16688 (reach 1.16538) | REACTED (Thu 1.16691) |
| V1 bands 1.17710-1.17801, 1.17564-1.17655, 1.17327-1.17418, 1.17126-1.17217, 1.16876-1.16967 | all REACTED (5) |

- Not reached: RESISTANCE CEILING, UPPER RESISTANCE 1.18213-1.18292, UPPER RESISTANCE 1.17988-1.18067, KEY SUPPORT, 1H BoM supply 1.18239-1.18491, LSZ 1.18441-1.18491, bands 1.18303, 1.18125, 1.17958, 1.16581.
- Missing turning points: none.

**E1 = 21 / 21 = 100%.** The "none bloated / bunched" condition FAILED:
- 31 drawings cover 1.1654-1.1860.
- 1.1749-1.1766 holds EQUILIBRIUM, 3 LSZ and a band (5 stacked).
- 1.1654-1.1700 holds 4 demand zones, a gap, an LSZ, KEY SUPPORT and a band (8 stacked).

**E2**

| Day | Verdict |
|---|---|
| Mon SS | RIGHT. 1.17475-1.17902 inside 1.17004-1.17988. |
| Tue SS+RWL+BS down | RIGHT. Drop to 1.1756, RWL to 1.17759, then BS down to 1.17187. |
| Wed BS down | RIGHT. 1.17624 -> 1.1703. |
| Thu BS+RWL down | RIGHT. Break to 1.1679, RWL 1.17165, down to 1.16691. |
| Fri | WRONG. "no designation", while Friday rallied 50 pips, 1.16729 -> 1.1723. |

**E2 = 4 / 5 = 80%.**

**E3**

| Trade | Verdict |
|---|---|
| T1 Mon LONG 1.1748 | MISSED. There was no long; the tool's "Mon SS LONG 1.17207" was suppressed, and it sat at the wrong zone anyway. |
| T2 | CAUGHT. EU1 SHORT 1.17920, TP 1.17207 Tue 17:15. EU2 and EU3 at the same entry also won. |
| T3 Tue-Wed LONG 1.1719 | MISSED. "Tue RWL up" was rejected (SL_INVALID). |
| T4 Wed SHORT 1.1762 | MISSED. The Wed setup EU4 (1.17656) had already filled Tue 07:45 and been STOPPED Tue 13:30. There was no live order at Wednesday's 1.17624 top. EU3 (entered Monday) rode through, but it is not an entry at this turn. |
| T5 Thu SHORT 1.1716 | MISSED. The Thu setup EU5 (1.17372) had filled Tue 17:00 and been STOPPED Tue 17:30. |
| T6 Fri LONG 1.1673 | MISSED. There was no Friday designation and no setup. |

Stopped setups (losses):
- **EU4** "Wed Ladder" SHORT 1.17656: it filled on Tuesday, one day early, and was stopped Tue 13:30.
- **EU5** "Thu Ladder" SHORT 1.17372: it filled on Tuesday, two days early, and was stopped Tue 17:30 after 30 minutes.

**E3 = 1 / 6 = 17%.** There are 2 losses.

**Presentation**
- Three LSZ labels print on top of each other at 1.1755-1.1765 ("sweep to 1.17492" / "sweep to 1.17725" / "sweep to 1.17427").
- The LSZ supply label overlaps the RESISTANCE CEILING label.
- "1H (Unmitigated) | BoM", "4H (Unmitigated) | MoM" and "KEY SUPPORT BAND" are stacked unreadably at 1.1660-1.1668.
- The EU1 / Mon SS labels overlap, and "EU4 Ladder S 12.3R" is covered by candles.
- The Thu tag (purple) is illegible.

---
## 6. GBPUSD 2026-04-20

Week: Mon 1.35444/1.34818 | Tue 1.35396/1.34744 | Wed 1.35353/1.34901 | Thu 1.35182/1.34476 | Fri 1.35370/1.34532.

**Obvious trades.** These were listed before the setups were read.

| # | Trade |
|---|---|
| T1 | Mon LONG 1.3482-1.3490 (MID-RANGE SUPPORT 1.34768-1.34846) -> 1.3544 (1H supply 1.35400-1.35538), Mon 06:00-15:00 |
| T2 | Mon-Tue SHORT 1.3544 -> 1.3482 (MID-RANGE SUPPORT), Tue 08:00 |
| T3 | Tue LONG 1.3482 -> 1.3540 (1H supply), Tue 08:00-14:00 |
| T4 | Tue SHORT 1.3540 -> 1.3475 (MID-RANGE SUPPORT / LSZ 1.34740), Tue 19:00 |
| T5 | Tue-Wed LONG 1.3475 -> 1.3535 (UPPER RESISTANCE 1.35241-1.35327), Wed 05:00-09:00 |
| T6 | Wed SHORT 1.3533-1.3535 -> 1.3492 (UPPER RESISTANCE 1.34932-1.35019), Wed 12:00 |
| T7 | Thu SHORT 1.3518 (Thu 14:00) -> 1.3448 (gap 1.34423-1.34483 / 1H demand), Thu 17:00 |
| T8 | Fri LONG 1.3453-1.3448 (1H demand 1.34345-1.34660) -> 1.3537 (UPPER RESISTANCE 1.35241-1.35327), Fri 20:00 |

**E1 zones reached (range 1.34476-1.35444)**

| Zone | Verdict |
|---|---|
| UPPER RESISTANCE 1.35434-1.35508 | REACTED (Mon 15:00-17:00 triple top 1.3544 -> 1.3482) |
| UPPER RESISTANCE 1.35241-1.35327 | REACTED (Mon 18:00-Tue 01:00 shelf; Wed 05:00-09:00 caps 1.3532-1.3535) |
| UPPER RESISTANCE 1.34932-1.35019 | REACTED (Wed 12:00 1.34925, Wed 21:00 1.34931; week-long chop around it) |
| MID-RANGE SUPPORT 1.34768-1.34846 | REACTED (Mon 06:00 1.34818 -> 1.3544; Tue 08:00 1.34823; Tue 19:00 1.34744; Thu 1.3478). Thu 17:00 broke it. |
| GAP 1.35047-1.35107 | REACTED (chop / consolidation Tue-Wed) |
| GAP 1.34640-1.34700 | REACTED (Thu 19:00-Fri 01:00 shelf) |
| GAP 1.34423-1.34483 | REACTED (Thu 17:00 low 1.34476 -> 1.3537) |
| 1H MoM supply 1.35400-1.35538 | REACTED (Mon 15:00-17:00; Tue 14:00 1.35396) |
| 1H MoM demand 1.34345-1.34660 | REACTED (Thu 17:00 1.34476, Fri 03:00 1.34532) |
| LSZ demand 1.35044-1.35094 (reach 1.34944) | PIERCED (Mon 06:00 1.34818, Tue 08:00 1.34823, Tue 19:00 1.34744: 12-20 pips past the reach three times; it held only on Wed) |
| LSZ demand 1.34952-1.35002 (reach 1.34852) | REACTED (Tue 08:00 1.34823; Thu 02:00-07:00 1.3482-1.3485). Tue 19:00 ran 11 pips past reach. |
| LSZ demand 1.34740-1.34790 (reach 1.34640) | REACTED (Tue 19:00 1.34744; Thu 1.34781). Thu 17:00 ran 16 pips past reach. |
| V1 bands 1.35220-1.35332, 1.34973-1.35085, 1.34691-1.34803, 1.34473-1.34585 | all REACTED (4) |

- Not reached: RESISTANCE CEILING, UPPER RESISTANCE 1.35719-1.35805, KEY SUPPORT, gaps 1.35521 and 1.34317, 4H BoM supply 1.35610-1.35948, 4H BoM demand, 1H BoM demand, LSZ 1.35945 and 1.33805, bands 1.35782, 1.35547, 1.34227, 1.33983, 1.33821.
- Missing turning point: Thu 14:00 high 1.35182, the top of the 70-pip T7 drop. The nearest drawing is band 1.35220 (3.8 pips) or gap top 1.35107 (7.5 pips), so it counts as missing.

**E1 = 15 / (16 + 1) = 88%.** The "none bloated / bunched" condition FAILED:
- 32 drawings cover 1.3371-1.3610.
- There are four UPPER RESISTANCE zones.
- 1.3474-1.3510 holds 9 overlapping drawings: UPPER RESISTANCE, MID-RANGE SUPPORT, gap, 3 LSZ and 3 bands.

**E2**

| Day | Verdict |
|---|---|
| Mon SS (range 1.34345-1.35019) | WRONG. Monday broke the ceiling and ran 42 pips above it to 1.35444 (closing 1.35333). That was a breakout up, not a range. |
| Tue SS+RWL+BS down (box 1.34879-1.34973) | WRONG. The box is only 9 pips tall. The candles whipsawed 1.3474-1.3540, and there was no break-and-surge down: the day closed 1.35068, back above the floor. |
| Wed BS down (box 1.34429-1.34879) | WRONG. Wednesday never went below 1.34901; it ranged 1.349-1.3535. |
| Thu BS+RWL down | RIGHT. Break of MID-RANGE SUPPORT to 1.34476, then recovery. |
| Fri | WRONG. "no designation", while Friday rallied 84 pips, 1.34532 -> 1.3537. |

**E2 = 1 / 5 = 20%.**

**E3**
- Only two setups exist for the whole week:
  - GB1 LONG 1.34660 never filled.
  - GB2 SHORT 1.34399 was void (price was already beyond its stop).
- Every other candidate was rejected:
  - Mon / Tue SS down: RRR;
  - Tue RWL up: TP_NULL;
  - Thu RWL LONG 1.34083: NARRATIVE.
- T1-T8 are all MISSED.

**E3 = 0 / 8 = 0%.** No stopped setups.

**Presentation**
- Labels overlap:
  - "4H (Unmitigated) | BoM" over the "UPPER RESISTANCE ... Tier 1 MoM" label;
  - "1H (Unmitigated) | MoM" over the "UPPER RESISTANCE ... Tier 2 MoM" label;
  - "4H (Unmitigated) | BoM" over "KEY SUPPORT BAND";
  - "GB2 BS S 3.8R" over "GAP IN-FILL";
  - "GB1 SS L 3.1R" over a gap label.
- The Tue day box is a 9-pip sliver that does not describe the day.
- The option-strike label is covered by candles.
- The Thu tag is illegible.

---
## 7. DXY 2026-10-05

Week from Mon 06:00 UTC: Mon 102.433/102.084 | Tue 102.285/101.754 | Wed 102.499/~101.90 | Thu 102.467/102.033 | Fri 102.335/101.920. Monday's 02:00-04:00 spike to 102.535 was before the anchor.

**Obvious trades.** These were listed before the setups were read.

| # | Trade |
|---|---|
| T1 | Mon SHORT 102.43 (Mon 06:00) -> 102.08-102.10 (LSZ 102.082-102.132), Mon 09:00 |
| T2 | Tue SHORT 102.28 (Tue 06:00-07:00, LSZ 102.157-102.207 reach) -> 101.75 (KEY SUPPORT 101.750-101.843), Tue 12:00 |
| T3 | Tue-Wed LONG 101.75-101.80 (KEY SUPPORT / 1H BoM demand) -> 102.50 (LSZ 102.485-102.535), Wed 12:00 |
| T4 | Wed SHORT 102.50 -> 102.13-102.21, Wed 15:00-Thu 02:00 |
| T5 | Thu LONG 102.13 (LSZ 102.082-102.132) -> 102.467, Thu 11:00 |
| T6 | Thu SHORT 102.467 -> 102.03 (Thu 14:00) / 101.92 (MID-RANGE SUPPORT / band, Fri 05:00) |
| T7 | Fri LONG 101.92-102.00 (MID-RANGE SUPPORT) -> 102.33, Fri 12:00-16:00 |

**E1 zones reached.** There are 10 drawings in total.

| Zone | Verdict |
|---|---|
| MID-RANGE SUPPORT 101.961-102.051 | REACTED (Tue 07:00-10:00 shelf 101.99-102.01; Thu 14:00/17:00 102.033-102.035; Fri 05:00 101.92 -> 102.335). Tue 11:00 broke it. |
| KEY SUPPORT 101.750-101.843 | REACTED (Tue 12:00 101.754, base Tue 12:00-22:00, then +75 pips) |
| 1H MoM demand 101.855-101.926 | REACTED (Tue 12:00-22:00 base; Fri 05:00 101.92) |
| 1H BoM demand 101.668-101.798 | REACTED (Tue 101.754) |
| LSZ supply 102.485-102.535 (reach 102.635) | REACTED (Wed 12:00 102.499 -> 102.13) |
| LSZ supply 102.157-102.207 (reach 102.307) | REACTED (Tue 06:00-07:00 102.285 -> 101.754; Fri 12:00-16:00 cap 102.33). Wed 07:00 went through it. |
| LSZ supply 102.082-102.132 (reach 102.232) | PIERCED (Wed 07:00 102.07 -> 102.32 in one bar; Fri 10:00-12:00 102.09 -> 102.33; no reaction from below) |
| LSZ demand 101.855-101.905 (reach 101.755) | REACTED (Tue 101.754) |
| V1 band 101.916-101.996 | REACTED (Tue 08:00-10:00 101.97-101.99; Fri 05:00 101.92) |

- Not reached: LSZ demand 101.668-101.718.
- Missing turning point: Mon 06:00 high 102.433, which led to T1's 35-pip drop. The nearest drawings are LSZ reach 102.307 (13 pips) and LSZ 102.485 (5 pips).
- Above 102.05 the week traded for four days with no pressure zone and no supply zone at all, only LSZ boxes.

**E1 = 8 / (9 + 1) = 80%.** The "none missing" condition FAILED: there is no resistance structure above 102.05. Mild bunching at 101.85-102.05 (1H demand, LSZ, band and MID-RANGE SUPPORT overlap).

**E2.** The forecast is the same "SS 80%" box, 101.855-102.635 (78 pips, the whole week's reach), on all five days.

| Day | Verdict |
|---|---|
| Mon | RIGHT. 102.084-102.433 inside the box. |
| Tue | WRONG. A 53-pip break down through MID-RANGE SUPPORT and out of the floor (low 101.754, 10 pips under the 101.855 floor; close 101.841 below it). That is a BS down, not a range. |
| Wed | RIGHT. Floor-to-ceiling swing 101.90 -> 102.499 inside the box. |
| Thu | RIGHT. 102.033-102.467 inside. |
| Fri | RIGHT. 101.92-102.335 inside. |

**E2 = 4 / 5 = 80%.** The "chain" is a single SS repeated five times with a box as wide as the whole week, so the 80% says little.

**E3.** There are only two setups.

| Trade | Verdict |
|---|---|
| T1 | MISSED. DX1 (SHORT 102.485) did not fill on Monday (the Mon 06:00 high was 102.433). |
| T2 | MISSED. There was no short. |
| T3 | MISSED. DX2 LONG 101.926 filled Tue 11:00 and was STOPPED Tue 11:45 (SL 101.776; low 101.754), 15 minutes before the 75-pip rally began. |
| T4 | CAUGHT. DX1 SHORT 102.485 filled Wed 12:15 and hit TP 101.926 Fri 05:30 (SL 102.565; Thu high 102.467). |
| T5 | MISSED. |
| T6 | MISSED. DX1 was still open, but there was no entry at the Thu 102.467 top. Same rule as EURUSD 04-20 T4. |
| T7 | MISSED. |

- Stopped setup: **DX2** LONG 101.926 (Tue 11:45).

**E3 = 1 / 7 = 14%.** There is 1 loss.

**Presentation**
- Five identical "SS 80%" day boxes with a zig-zag yellow line stretched over the full 78-pip range, which carries no daily information.
- The "1H (Unmitigated) | MoM" label is hidden behind candles at 101.86.
- The KEY SUPPORT label is overlapped by candles.
- The upper half of the chart, where the week traded, has only green LSZ strips and no named zones.

---
## 8. EURUSD 2026-10-05

Week from Mon 06:00: Mon 1.12249/1.11690 | Tue 1.12767/1.12028 | Wed 1.12629/1.11645 | Thu 1.12267/1.11719 | Fri 1.12427/1.11874. Monday's 02:00 crash to 1.1161 was before the anchor.

**Obvious trades.** These were listed before the setups were read.

| # | Trade |
|---|---|
| T1 | Mon LONG 1.1169-1.1175 (Mon 06:00 low, near LSZ 1.11610-1.11660) -> 1.1220 (LSZ 1.12208-1.12258), Mon 09:00 |
| T2 | Tue LONG 1.1203-1.1210 (band 1.12039-1.12149) -> 1.1272-1.1277 (1H BoM supply 1.12716-1.12853), Tue 06:00-12:00 |
| T3 | Tue-Wed SHORT 1.1265-1.1277 (1H BoM supply / gap 1.12611-1.12671) -> 1.1165 (LSZ 1.11610-1.11660), Wed 12:00, ~100 pips |
| T4 | Wed LONG 1.1165 -> 1.1203 (band), Wed 17:00-18:00 |
| T5 | Thu LONG 1.1172 (Thu 11:00) -> 1.1225-1.1243 (Thu 14:00 / Fri 05:00) |
| T6 | Fri SHORT 1.1243 (UPPER RESISTANCE 1.12451-1.12530) -> 1.1187, Fri 16:00 |

**E1 zones reached.** There are 11 drawings in total.

| Zone | Verdict |
|---|---|
| UPPER RESISTANCE 1.12451-1.12530 | REACTED (Tue 08:00-10:00 cap 1.1247-1.1249; Tue 13:00-14:00 support 1.1245; Fri 05:00 1.12427 -> 1.11874). Tue 11:00 and Wed 00:00 went through it. |
| GAP 1.12611-1.12671 | REACTED (Tue 15:00-22:00 shelf, then -100 pips) |
| 1H BoM supply 1.12716-1.12853 | REACTED (Tue 11:00-12:00 1.12717/1.12767 = week high) |
| 1H MoM supply 1.12491-1.12612 | REACTED (Tue 13:00-22:00 shelf) |
| LSZ supply 1.12562-1.12612 (reach 1.12712) | REACTED (Tue 15:00-22:00 tops inside reach). Tue 12:00 spiked 5.5 pips past reach. |
| LSZ demand 1.12208-1.12258 (reach 1.12108) | PIERCED (Tue 06:00 ran 8 pips past reach; Wed 07:00 and Fri 08:00-10:00 crossed it in a straight line) |
| LSZ demand 1.12149-1.12199 (reach 1.12049) | REACTED (Tue 06:00 1.12028 -> 1.12767). Wed 07:00 crossed it. |
| LSZ demand 1.11610-1.11660 (reach 1.11510) | REACTED (Wed 12:00 1.11645 -> 1.1203; Mon 06:00 1.1169) |
| V1 band 1.12039-1.12149 | REACTED (Tue 06:00 1.12028; Wed 17:00-18:00 cap 1.1203) |

- Not reached: gap 1.12806-1.12866, LSZ 1.12803-1.12853.
- Missing turning point: Thu 11:00 low 1.11719, the origin of T5's 55-pip rally. The nearest drawing is LSZ top 1.11660 (5.9 pips).
- Price spent Wed 12:00-Thu 13:00 in 1.1165-1.1203, a 38-pip band with no drawing at all.

**E1 = 8 / (9 + 1) = 80%.** The "none missing" condition FAILED. There is no structure between 1.1166 and 1.1204, and no IP support anywhere: the only pressure zone on the map is one UPPER RESISTANCE.

**E2.** "SS 80%" five times, box 1.11510-1.12612 (110 pips).

| Day | Verdict |
|---|---|
| Mon | RIGHT. Inside the box. |
| Tue | WRONG. A 74-pip one-way breakout from the band through UPPER RESISTANCE into the 1H BoM supply, to 1.12767, 15 pips above the box ceiling. That is the canon BS definition, not a range. |
| Wed | RIGHT. Ceiling-to-floor swing inside the box. |
| Thu | RIGHT. Inside the box. |
| Fri | RIGHT. Inside the box. |

**E2 = 4 / 5 = 80%.** As on DXY, a single SS box the size of the week is a weak forecast.

**E3.** There are only two setups.

| Trade | Verdict |
|---|---|
| T1 | MISSED. EU2 LONG 1.11660 did not fill on Monday. |
| T2 | MISSED. There was no long. Instead EU1 SHORT 1.12491 filled Tue 09:45 into the breakout and was STOPPED Tue 11:15 (SL 1.12642). |
| T3 | MISSED. The only short was already stopped one bar before the real top. |
| T4 | MISSED. EU2 LONG 1.11660 filled Wed 12:15 (low 1.11645), but its TP 1.12491 was never hit; it is still open at the week end. The Fri high 1.12427 fell 6 pips short. |
| T5 | MISSED. There was no new entry. |
| T6 | MISSED. There was no short. |

- Stopped setup: **EU1** SHORT 1.12491 (Tue 11:15).

**E3 = 0 / 6 = 0%.** There is 1 loss.

**Presentation**
- "1H (Unmitigated) | MoM" is drawn over candles at 1.1253.
- The "Tue SS" tag is partly hidden by candles.
- The two LSZ demand labels at 1.1210-1.1215 overlap ("sweep to 1.12108" / "sweep to 1.12049").
- In _week the zone labels are cut to "ATE | 30-50% ZFP".
- The yellow zig-zag sweeps the whole box every day, regardless of what the candles did.

---
## 9. GBPUSD 2026-10-05

Week from Mon 06:00: Mon 1.32390/1.31900 | Tue 1.32856/1.32013 | Wed 1.32761/1.31935 | Thu 1.32485/1.31843 | Fri 1.32503/1.32057.

**Obvious trades.** These were listed before the setups were read.

| # | Trade |
|---|---|
| T1 | Mon LONG 1.3205 (MID-RANGE SUPPORT 1.31991-1.32051) -> 1.3238 (1H BoM supply 1.32319-1.32395), Mon 06:00-09:00 |
| T2 | Mon SHORT 1.3238 (1H BoM supply) -> 1.3190 (LSZ 1.31899-1.31949), Mon 13:00 |
| T3 | Tue LONG 1.3201 (MID-RANGE SUPPORT) -> 1.3283-1.3286, Tue 11:00-15:00 (84 pips) |
| T4 | Tue-Wed SHORT 1.3275-1.3286 -> 1.3194 (LSZ / MID-RANGE SUPPORT), Wed 12:00 (~90 pips) |
| T5 | Wed-Thu LONG 1.3184-1.3194 (LSZ 1.31814-1.31949) -> 1.3248 (UPPER RESISTANCE 1.32457-1.32535), Thu 14:00 |
| T6 | Fri SHORT 1.3248-1.3250 (UPPER RESISTANCE) -> 1.3206 (MID-RANGE SUPPORT), Fri 12:00 |
| T7 | Fri LONG 1.3206 -> 1.3244, Fri 18:00 |

**E1 zones reached.** All 13 drawings were reached.

| Zone | Verdict |
|---|---|
| UPPER RESISTANCE 1.32457-1.32535 | REACTED (Wed 02:00-06:00 shelf; Thu 14:00 1.32485 -> 1.32037; Fri 05:00 1.32503 -> 1.32057). Tue 11:00 broke through it. |
| MID-RANGE SUPPORT 1.31991-1.32051 | REACTED (Mon 06:00 1.32052; Tue 06:00 1.32013 -> +84 pips; Fri 12:00 1.32057) |
| GAP 1.32270-1.32330 | REACTED (Mon 08:00-11:00 caps; Thu 17:00-Fri 00:00 shelf) |
| GAP 1.32124-1.32184 | REACTED (Mon 12:00-Tue 06:00 chop) |
| 1H BoM supply 1.32319-1.32395 | REACTED (Mon 08:00-09:00 1.3239 -> 1.3190). Tue 07:00 broke it. |
| LSZ supply 1.32510-1.32560 (reach 1.32660) | PIERCED (Tue 11:00 ran to 1.32817-1.32856, 16-20 pips past reach, and held there 10 hours) |
| LSZ supply 1.32450-1.32500 (reach 1.32600) | REACTED (Thu 14:00 1.32485, Fri 05:00 1.32503). Tue 11:00 pierced it. |
| LSZ demand 1.31899-1.31949 (reach 1.31799) | REACTED (Mon 13:00 1.319; Wed 12:00 1.31935; Thu 1.31843) |
| LSZ demand 1.31814-1.31864 (reach 1.31714) | REACTED (Thu 10:00 1.31843) |
| LSZ demand 1.31806-1.31856 (reach 1.31706) | REACTED. A duplicate of the box above (0.8 pip apart; the two labels print on top of each other). |
| V1 band 1.32526-1.32636 | REACTED (Tue 21:00-Wed 01:00 shelf 1.3257-1.3261) |
| V1 band 1.32121-1.32231 | REACTED (chop) |
| V1 band 1.31932-1.32042 | REACTED (Tue 06:00, Wed 12:00-13:00) |

- Missing turning point: the week high 1.32856 (Tue 11:00-20:00 top, origin of the 90-pip T4 drop). There is no drawing above 1.3266. The facts file says "zones between 1.31799 and 1.32535 (the week's reach)", but the week actually reached 1.32856.

**E1 = 12 / (13 + 1) = 86%.** The "none missing / bunched" condition FAILED:
- the top of the week has no zone;
- the duplicate LSZ pair;
- 1.3180-1.3205 holds 3 LSZ, MID-RANGE SUPPORT and a band.

**E2.** "SS 80%" five times, box 1.31799-1.32395 (60 pips).

| Day | Verdict |
|---|---|
| Mon | RIGHT. 1.319-1.3239 inside. |
| Tue | WRONG. Broke the 1.32395 ceiling, ran 46 pips above it to 1.32856 and closed 1.32742 above the box. That is a BS up. |
| Wed | WRONG. Opened 25 pips above the box and fell 82 pips through UPPER RESISTANCE and both gaps to the floor. That is a directional drop, not a range inside the bounds. |
| Thu | RIGHT. Floor 1.31843 to a 9-pip poke over the ceiling, back inside. |
| Fri | RIGHT. 1.3206-1.3250 range; the ceiling was poked by 11 pips. |

**E2 = 3 / 5 = 60%.**

**E3.** There are two setups.

| Trade | Verdict |
|---|---|
| T1 | MISSED. |
| T2 | MISSED. GB1 SHORT 1.32319 filled Mon 07:45. Its TP 1.31900 was touched to the pip (Mon 13:00 low 1.31900) but not hit by the simulation. It was STOPPED Tue 08:30 (SL 1.32437) by the T3 rally. It counts as a loss. |
| T3 | MISSED. Tue 06:00 low 1.32013 did not reach GB2 (1.31949). |
| T4 | MISSED. There was no short. |
| T5 | CAUGHT. GB2 (re-armed) LONG 1.31949 filled Wed 12:15 at the same demand cluster, survived the Thu 10:00 low 1.31843 (SL 1.31814, 3 pips spare) and hit TP 1.32309 Thu 14:15. GB2's first fill (Mon 13:30 -> TP Tue 01:30) also won, but on a 35-pip leg that was not on the list. |
| T6 | MISSED. There was no short. |
| T7 | MISSED. GB2's second re-arm never filled. |

- Stopped setup: **GB1** SHORT 1.32319 (Tue 08:30).

**E3 = 1 / 7 = 14%.** There is 1 loss.

**Presentation**
- The duplicate LSZ labels "sweep to 1.31714" / "sweep to 1.31706" are printed on top of each other, making them illegible.
- The "1H (Unmitigated) | BoM" label overlaps the "Wed SS" tag.
- "GB1 SS S 3.5R" is printed over "GAP IN-FILL".
- "GB2 SS L 2.7R" is printed over "MID-RANGE SUPPORT".
- The Tue-Wed top of the week (1.3266-1.3286) sits in empty space above every drawing.

---
## 10. DXY 2026-05-18

Week from Mon 06:00: Mon 99.307/98.946 | Tue 99.434/98.944 | Wed 99.472/98.966 | Thu 99.515/99.064 | Fri 99.412/99.172. The whole week sat in a 57-pip box.

**Obvious trades.** These were listed before the setups were read.

| # | Trade |
|---|---|
| T1 | Mon SHORT 99.30 (LSZ 99.270-99.320) -> 98.95-98.98 (MID-RANGE SUPPORT 98.963-99.037), Mon 06:00-21:00 |
| T2 | Mon-Tue LONG 98.95-99.00 (MID-RANGE SUPPORT) -> 99.43 (LSZ / band 99.359-99.413), Tue 14:00 |
| T3 | Wed SHORT 99.45-99.47 (band 99.449-99.503) -> 98.97 (MID-RANGE SUPPORT), Wed 14:00-15:00 |
| T4 | Wed-Thu LONG 99.0-99.09 (1H demand 99.001-99.097) -> 99.47-99.51 (band 99.449-99.503), Thu 13:00 |
| T5 | Thu SHORT 99.47-99.51 -> 99.09 (1H demand), Thu 17:00 |

Friday was 99.17-99.41 chop with no clean leg.

**E1 zones reached**

| Zone | Verdict |
|---|---|
| MID-RANGE SUPPORT 98.963-99.037 | REACTED (Mon 20:00-22:00 98.944-98.952 -> +49; Wed 15:00 98.966 -> 99.515) |
| 1H MoM demand 99.251-99.298 | REACTED (Tue 16:00-23:00 shelf; Wed 03:00-04:00 99.285). Mon 06:00 crossed it. |
| 1H MoM demand 99.174-99.244 | REACTED (Mon 06:00-07:00 99.143-99.17 -> 99.248; Thu 02:00-06:00 shelf; Fri 13:00 99.172) |
| 1H Mitigated 2x demand 99.001-99.097 | REACTED (Mon 11:00-17:00 base; Wed 16:00-19:00 99.053; Thu 08:00-09:00 99.078 -> 99.515) |
| LSZ supply 99.359-99.409 (reach 99.509) | REACTED (Tue 14:00 99.434; Wed 14:00 99.472 -> 98.966; Thu 13:00 99.515, 0.6 pip past reach) |
| LSZ supply 99.270-99.320 (reach 99.420) | REACTED (Mon 06:00 99.307 -> 98.946) |
| LSZ demand 99.251-99.301 (reach 99.151) | REACTED (Mon 07:00 99.143; Fri). Mon 08:00 went 6 pips past reach. |
| V1 bands 99.449-99.503, 99.359-99.413, 99.244-99.298, 99.125-99.179, 98.996-99.050 | all REACTED (5) |

- Not reached: 1H demand 98.844-98.889, LSZ 98.844-98.894, band 98.885-98.939.
- Missing turning points: none.

**E1 = 12 / 12 = 100%.** The "none bloated / bunched" condition FAILED:
- 15 drawings fill 98.74-99.51 without a gap, so every candle of the week sits in a box.
- 99.24-99.32 stacks a 1H demand, an LSZ supply, an LSZ demand and a band.
- There are no IP resistances at all; the ceiling is an LSZ.
- The 100% reflects coverage, not selection.

**E2.** "SS 80%" five times, box 98.963-99.509, which is exactly the week's range.

| Day | Verdict |
|---|---|
| Mon | RIGHT. Inside the box. |
| Tue | RIGHT. Inside the box. |
| Wed | RIGHT. Inside the box. |
| Thu | RIGHT. Inside the box. |
| Fri | RIGHT. Inside the box. |

**E2 = 5 / 5 = 100%.** This is a genuine range week, so the SS call is correct. But the day boxes carry no daily direction or key-zone information beyond "the week range".

**E3.** There is one setup, DX1 LONG 99.050 (SL 98.929, TP 99.409), re-armed twice.

| Trade | Verdict |
|---|---|
| T1 | MISSED. There was no short: "Mon SS down" was rejected (RRR 2.07). |
| T2 | CAUGHT. DX1 filled Mon 08:30 at the first-contact band of the 1H demand (Mon 08:00 low 99.092), survived the Mon 98.944 low by 1.5 pips, and hit TP Tue 14:15. |
| T3 | MISSED. There was no short. |
| T4 | CAUGHT. DX1 re-armed, filled Wed 15:15, survived 98.966, and hit TP Thu 13:15. |
| T5 | MISSED. There was no short. |

- Stopped setups: none.

**E3 = 2 / 5 = 40%.** The tool caught only the long side of a two-sided range.

**Presentation**
- The LSZ labels "sweep to 99.420" and "sweep to 99.151" are printed on top of each other.
- "1H (Unmitigated) | MoM" is printed over candles twice.
- "DX1 SS L 3.0R" is half covered by "1H (Mitigated 2x) | MoM".
- In _week the zone labels sit under candles ("1H (Unmit...ed) | MoM").
- The chart is one green-blue block from 98.74 to 99.51.

---
## 11. EURUSD 2026-05-18

Week from Mon 06:00: Mon 1.16608/1.16219 | Tue 1.16617/1.15921 | Wed 1.16448/1.15827 | Thu 1.16353/1.15762 | Fri 1.16205/1.15882.

**Obvious trades.** These were listed before the setups were read.

| # | Trade |
|---|---|
| T1 | Mon LONG 1.1622 (EQUILIBRIUM 1.16219-1.16296) -> 1.1656-1.1661 (UPPER RESISTANCE 1.16493-1.16562 / band 1.16604-1.16672), Mon 06:00-22:00 |
| T2 | Tue SHORT 1.1658-1.1661 -> 1.1592-1.1597 (MID-RANGE SUPPORT 1.15970-1.16036), Tue 14:00-15:00 (69 pips) |
| T3 | Wed LONG 1.1583-1.1590 (band 1.15747-1.15815) -> 1.1645 (1H Mitigated supply 1.16456-1.16574), Wed 14:00-15:00 |
| T4 | Wed-Thu SHORT 1.1630-1.1645 (1H supply 1.16266-1.16356 / 1.16456) -> 1.1576 (band 1.15747-1.15815), Thu 13:00 |
| T5 | Thu LONG 1.1576-1.1584 (band) -> 1.1630 (1H supply 1.16266-1.16356), Thu 17:00 |

Friday was 1.1588-1.1620 chop.

**E1 zones reached.** There are 22 drawings; 14 were reached.

| Zone | Verdict |
|---|---|
| UPPER RESISTANCE 1.16493-1.16562 | REACTED (Mon 12:00-17:00 shelf 1.1641-1.1657; Mon 20:00-22:00 4.6 pips over, then -69 pips) |
| EQUILIBRIUM 1.16219-1.16296 | REACTED (Mon 06:00 1.16219 -> +40; Tue 08:00-12:00 shelf; Wed 15:00-Thu 06:00 shelf) |
| MID-RANGE SUPPORT 1.15970-1.16036 | REACTED (Tue 15:00-Wed 13:00 consolidation around it). Wed 08:00 went 13 pips under it, and Thu 13:00 went 21 pips under it. |
| 1H Mitigated 2x supply 1.16456-1.16574 | REACTED (Mon shelf; Wed 15:00 1.16448 -> -69) |
| 1H MoM supply 1.16266-1.16356 | REACTED (Wed 16:00-Thu 01:00 caps 1.1631-1.1636; Thu 08:00 1.16353; Thu 17:00 1.163) |
| LSZ supply 1.16211-1.16261 (reach 1.16361) | REACTED (Wed-Thu caps inside reach) |
| LSZ demand 1.16168-1.16218 (reach 1.16068) | REACTED (Tue 09:00-12:00 lows 1.1611-1.1616; Thu 02:00-06:00 1.1616-1.1618). Tue 13:00 and Thu 07:00 crossed it. |
| LSZ demand 1.16083-1.16133 (reach 1.15983) | PIERCED (Tue 14:00-15:00 1.15921, 6 pips past reach; Fri 14:00 1.15882, 10 pips past) |
| V1 bands 1.16604-1.16672, 1.16477-1.16545, 1.16327-1.16395, 1.16203-1.16271, 1.16094-1.16162, 1.15747-1.15815 | all REACTED (6). The 1.15747-1.15815 band held the Wed 14:00 1.15827 and Thu 13:00 1.15762 lows. |

- Not reached: UPPER RESISTANCE 1.16641-1.16726 (2.4 pips above the high), 1H supply 1.16655-1.16726, LSZ 1.16676-1.16726, bands 1.16705, 1.15619, 1.15503.
- Missing turning points: none.

**E1 = 13 / 14 = 93%.** The "none bloated / bunched" condition FAILED:
- 1.1608-1.1636 stacks EQUILIBRIUM, a 1H supply, 3 LSZ and 3 bands (8 drawings over 28 pips).
- Two UPPER RESISTANCE zones and two supplies overlap at 1.1645-1.1673.
- The two lows of the week were held by an unlabelled V1 band 14-21 pips below the drawn MID-RANGE SUPPORT, not by an IP zone.

**E2.** "SS 80%" five times, box 1.15970-1.16562.

| Day | Verdict |
|---|---|
| Mon | RIGHT. |
| Tue | RIGHT. Ceiling-to-floor swing, 4.9-pip floor poke. |
| Wed | RIGHT. 14-pip sweep under the floor, then back up to 1.16448. |
| Thu | WRONG. A spike-down whiplash 21 pips through the floor to 1.15762 (twice the 10-pip LSZ sweep reach), then +54. The range boundary did not hold, and the tag does not name the move. |
| Fri | RIGHT. |

**E2 = 4 / 5 = 80%.**

**E3.** There are two setups, and both lost.

| Trade | Verdict |
|---|---|
| T1 | MISSED. "Mon SS up" was rejected (SOURCE_INVALID). |
| T2 | MISSED. EU1 SHORT 1.16512 (SL 1.16575) filled Mon 08:30 and was STOPPED Mon 20:15 by the 1.16608 poke, 3 pips over its stop. Price then fell 69 pips to its TP. Still a loss. |
| T3 | MISSED. |
| T4 | MISSED. |
| T5 | MISSED. |

Stopped setups (losses):
- **EU2** SHORT 1.16297, filled Mon 06:00 and stopped Mon 07:15 (75 minutes).
- **EU1** SHORT 1.16512, stopped Mon 20:15.

**E3 = 0 / 5 = 0%.** There are 2 losses.

**Presentation**
- At 1.1650-1.1667 the labels "UPPER RESISTANCE ... HEAVY", "1H (Mitigated 2x) | MoM", "1H (Unmitigated) | MoM" and the two option-strike labels ("3.7bn" / "1.5bn") print on top of each other.
- Three LSZ labels at 1.1596-1.1636 overlap.
- "EU1 SS S 8.6R" and "EU2 SS S 3.7R" sit under zone labels and candles.
- The day tags "Tue/Wed/Thu/Fri SS 80%" are drawn under the candles and option-strike lines.

---
## 12. GBPUSD 2026-05-18

Week from Mon 06:00: Mon 1.34494/1.33217 | Tue 1.34371/1.33785 | Wed 1.34630/1.33750 | Thu 1.34548/1.33904 | Fri 1.34631/1.34132.

**Obvious trades.** These were listed before the setups were read.

| # | Trade |
|---|---|
| T1 | Mon LONG 1.3322-1.3330 (gap 1.33240-1.33300 / LSZ 1.33147-1.33197) -> 1.3395-1.3403 (UPPER RESISTANCE 1.33950-1.34037), Mon 06:00-12:00 |
| T2 | Mon LONG continuation 1.3382-1.3395 (Mon 13:00-14:00 base) -> 1.3449 (UPPER RESISTANCE 1.34497-1.34557), Mon 15:00-16:00 |
| T3 | Mon-Tue SHORT 1.3449 -> 1.3379-1.3387 (band 1.33816-1.33933 / gap 1.3372-1.3378), Tue 09:00-14:00 |
| T4 | Wed LONG 1.3375-1.3378 (gap 1.33720-1.33780) -> 1.3455-1.3463 (UPPER RESISTANCE 1.34497), Wed 08:00 -> 15:00 |
| T5 | Thu SHORT 1.3455 (Thu 08:00) -> 1.3390 (UPPER RESISTANCE 1.33950), Thu 13:00 |
| T6 | Thu LONG 1.3390-1.3396 -> 1.3449, Thu 17:00 |

Friday was 1.3413-1.3463 chop.

**E1 zones reached.** There are 27 drawings; 15 were reached.

| Zone | Verdict |
|---|---|
| UPPER RESISTANCE 1.34497-1.34557 | REACTED (Mon 16:00 1.34494 -> -70; Wed 15:00-19:00 cap; Thu 08:00 1.34548 -> -65; Fri 13:00 spike rejected) |
| UPPER RESISTANCE 1.33950-1.34037 | REACTED (Mon 12:00-14:00 cap, then break; Tue-Wed floor 1.3379-1.3395; Thu 13:00 1.33904 -> +59) |
| GAP 1.34239-1.34299 | REACTED (Mon 17:00-Tue 00:00 shelf; Wed-Fri chop) |
| GAP 1.33720-1.33780 | REACTED (Wed 01:00/06:00/08:00 lows 1.3375-1.3378 -> +88) |
| GAP 1.33492-1.33552 | REACTED (Mon 10:00-11:00 pullback low 1.33465 -> +100) |
| GAP 1.33240-1.33300 | REACTED (Mon 06:00 low 1.33217) |
| 1H MoM supply 1.33941-1.34037 | REACTED (same as UPPER RESISTANCE 1.3395) |
| LSZ supply 1.33987-1.34037 (reach 1.34137) | PIERCED (Mon 15:00-16:00 ran 36 pips past reach to 1.34494) |
| LSZ supply 1.33203-1.33253 (reach 1.33353) | PIERCED (Mon 06:00 bar went straight through it, 1.33217 -> 1.33583) |
| LSZ demand 1.33147-1.33197 (reach 1.33047) | REACTED (Mon 06:00 1.33217) |
| V1 bands 1.34423-1.34540, 1.34222-1.34339, 1.33816-1.33933, 1.33527-1.33644 | REACTED (4) |
| V1 band 1.33264-1.33381 | PIERCED (crossed up in the Mon 06:00 bar) |

- Not reached after the anchor: MID-RANGE SUPPORT 1.32995-1.33055, KEY SUPPORT, gap 1.32668, LSZ 1.33022-1.33072, bands 1.33025, 1.32856, 1.32569, 1.32394.
- Missing turning points: none.

**E1 = 12 / 15 = 80%.** The "none bloated / bunched" condition FAILED:
- 27 drawings fill 1.3239-1.3456.
- 1.3314-1.3338 stacks a gap, 2 LSZ and 2 bands.
- Five gap in-fill boxes are spread over 180 pips.
- Below 1.3322 there are 11 drawings that price never reached after the anchor.

**E2.** "SS 80%" five times, box 1.33047-1.34037.

| Day | Verdict |
|---|---|
| Mon | WRONG. A 128-pip breakout up (BS) through the 1.34037 ceiling to 1.34494, closing 28 pips above the box. |
| Tue | WRONG. The day traded 1.3379-1.3437, 33 pips above the box ceiling. The bounds are off the day. |
| Wed | WRONG. An 88-pip surge from 1.3375 to 1.3463, closing above the box. |
| Thu | WRONG. 1.3390-1.3455, all above the ceiling. |
| Fri | WRONG. 1.3413-1.3463, entirely above the box. |

**E2 = 0 / 5 = 0%.** The tool called "both bounds hold" and a 1H MoM ceiling "HOLD-LONG". That ceiling broke in the first six hours of the week, and price never returned under it.

**E3.** There are two setups.

| Trade | Verdict |
|---|---|
| T1 | CAUGHT. GB2 LONG 1.33197 filled Mon 06:00 (first contact; low 1.33217), TP 1.33941 Mon 12:30. |
| T2 | MISSED. GB1 SHORT 1.33983 (SL 1.34232) filled Mon 12:30 against the breakout and was STOPPED Mon 15:45. |
| T3 | MISSED. |
| T4 | MISSED. GB2's re-arm never filled. |
| T5 | MISSED. |
| T6 | MISSED. |

- Stopped setup: **GB1** SHORT 1.33983 (Mon 15:45).

**E3 = 1 / 6 = 17%.** There is 1 loss.

**Presentation**
- "UPPER RESISTANCE ... Tier 2 MoM" and "1H (Unmitigated) | MoM" print on top of each other at 1.3400 ("30-50% ZFP | Tier 1H (Unmit...").
- Three LSZ labels overlap at 1.3305-1.3330 ("sweep to 1.33353" / "sweep to 1.33047" / a third, unreadable).
- "GB1 SS S 3.5R" is printed over "GAP IN-FILL".
- In _all the day tags "Tue SS 80%" etc. are under candles.
- The day boxes sit below the whole Tue-Fri price action.

