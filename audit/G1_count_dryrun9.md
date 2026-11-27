# G1 count 9 - outside reviewer (fresh eyes, did not build the tool)

Brief: audit/G1_brief9.md. Sources used: the 36 frames in evidence/s3i/ (all opened and looked at), the facts files audit/g1_facts_i/*.txt (prices / times only), context_management/oracle/golden_week.json (operator trades, week 2026-07-06), 1H bars read-only via e1_tool/e1_data.py `bars(pair,'60')`. Not read: audit/G1_count_dryrun*.md, memory/, tool code.

## Counting rules applied (so anyone can recount)

- Forecast window = Monday 06:00 UTC (02:00 New York) to Friday close. Candles before that are history.
- Pips: EURUSD / GBPUSD 0.0001; DXY 0.01 (so a "40-pip" DXY move = 0.40).
- **E1** = zones REACTED / (zones reached + obvious turning points of the week with no Engine 1 object at them). One verdict per zone (a zone = one labelled box with its parts; a turn at a part = a turn at its zone). REACTED = sharp rejection or consolidation in/around the zone; PIERCED = crossed with no reaction; NOT REACHED = price did not touch the zone or its parts. Each discovery line that price reached gets its own verdict. A turning point counts as "at a zone" if it is inside the zone/parts or within 5 pips of them (canon: institutions sweep 5-10 pips beyond); more than 5 pips away = "no zone" (missing).
- Obvious turning points = 1H swing extremes (+-8 bars) that start/end a leg of >= ~40 pips.
- **E1 side condition** ('none bloated, bunched, floating or missing'), judged against the operator's reference (DXY 04-20 trident_v8: zones 7-34 pips tall, ok; sweep/candle parts joined to a pressure zone are not bunched; zones up to 22 pips beyond the week's range are not floating). BUNCHED = two SEPARATELY LABELLED zones whose drawn extents (incl. their parts) overlap or lie within ~0-4 pips of each other, i.e. the L-28 pattern "separate zones 1-2 pips apart that one candle crossed together". FLOATING = zones drawn well beyond 22 pips from the week's range. MISSING = an obvious turning point with no E1 object (> 5 pips away). Any one of these = FAIL.
- **E2** = days RIGHT / 5. RIGHT = the day's candles show the tagged shape AND direction, and the forecast's key zone / bounds hold within sweep tolerance (<= ~10 pips beyond the box with a close back inside). An SS day on which price broke out of the forecast range and spent hours / closed beyond it is WRONG. Week 2026-07-06: the operator's tags are the truth (DXY Mon SS+BS, Tue SS, Wed SS+RWL+BS, Thu ladder short, Fri WL+RWL; EURUSD / GBPUSD the same shapes, direction inverted); a forecast tag is RIGHT only if it carries his shapes (a tag missing one of his shapes is WRONG).
- **E3** = obvious trades CAUGHT / obvious trades. Obvious trades: week 2026-07-06 = the operator's trades whose entry was available after Mon 06:00 UTC; DXY 2026-04-20 = his two trades; other weeks = every clean zone-to-zone 1H move of >= ~40 pips, listed from the _zones frame + bars BEFORE looking at setups. CAUGHT = a setup of the same direction at that turn/zone that filled and hit TP before SL (for his trades: entry within ~3 pips, see per-map notes where it is wider). A setup that was stopped is a loss even if price later went to TP. Every stopped setup is named.
- Totals are given two ways: pooled (sum of numerators / sum of denominators) and the mean of the per-map percentages.

---

## 1. DXY 2026-07-06 (anchor week)

Obvious trades (operator, golden_week.json). Trade 1 (Mon LONG 100.945) is OUTSIDE the window: 100.945 traded only Mon 02:00-05:00 UTC; after 06:00 Monday's lows were 100.987 / 100.999 / 101.000 until the TP area was passed. In window: 7 trades (2-8).

E1 (6 zones + 1 discovery line):
- 4H BoM Supply 101.316-101.430: NOT REACHED (week high 101.275).
- UPPER RESISTANCE 101.199-101.262 (parts to 101.152 / 101.305): REACTED (Tue 23:00 101.215 -> 100.950 Wed 07:00; Wed 15:00 101.275 -> sell-off to 100.786).
- EQUILIBRIUM 100.985-101.077 (parts 100.942-101.153): REACTED (Mon 10:00 high 101.145 in the MoM-supply part -> -34; Wed 07:00 low 100.950 -> +32; Thu 11:00 101.039 rejection).
- MID-RANGE SUPPORT 100.724-100.815 (parts 100.654-100.876): REACTED (Tue 01:00 low 100.803, Thu 06:00 100.786, Fri 14:00 100.727).
- GAP IN-FILL 100.599-100.659: REACTED (Fri 02:00 low 100.598 -> +40).
- KEY SUPPORT 100.470-100.530 (part to 100.558): NOT REACHED (low 100.598).
- Discovery 100.899 MA: REACTED (consolidation around it Tue 02-14, Thu 06-18).
- Turning points without a zone: none.
- E1 = 5/5 = **100%**.
- Side: **FAIL - bunched.** Six separately labelled zones form one unbroken wall 100.470-101.532: 4H BoM part 101.314 vs UPPER RES part 101.305 (0.9 pip); UPPER RES part 101.152 overlaps EQUILIBRIUM part 101.153; MID-RANGE part 100.654 overlaps GAP 100.653/100.659; GAP part 100.558 = KEY SUPPORT part 100.558. The operator's own map of this week (golden_week.json) has gaps between his zones; this one has none.

E2:
- Mon SS: WRONG - his tag SS+BS; the BS (break down 101.14 -> 100.84) is not in the forecast.
- Tue SS: RIGHT.
- Wed SS+RWL+BS down: RIGHT (his exact tag).
- Thu BS down: RIGHT (his ladder short = the breakout continuing down).
- Fri BS+WL+RWL down: RIGHT by the brief's rule (carries his WL+RWL); note the extra 'down' direction did not happen - the day flushed to 100.598 and closed 100.965 up.
- E2 = 4/5 = **80%**.

E3:
- #2 Mon SHORT 101.14: CAUGHT by DX2 101.138 (filled Mon 09:45, TP Tue 01:30).
- #3 Tue LONG 100.845: CAUGHT by DX3 100.851 (Mon 18:30 -> TP Tue 23:45).
- #4 Wed SHORT 101.19: CAUGHT by DX5 101.203 (Tue 23:45 -> TP Wed 06:30).
- #5 Wed LONG 100.975: CAUGHT by DX6 100.980 (Wed 07:15 -> TP Wed 09:00).
- #6 Wed SHORT 101.235: CAUGHT by DX4 101.235 (Wed 09:00 -> TP Fri 02:00).
- #7 Thu SHORT 100.975: CAUGHT by DX7 100.980 (Thu 00:00 -> TP Fri 02:00).
- #8 Fri LONG 100.615: CAUGHT by DX8 100.628 (Fri 02:00 -> TP Fri 14:00).
- Stopped: **DX2.Tue** (SHORT 101.138, filled Tue 19:15, stopped Tue 23:45).
- E3 = 7/7 = **100%**.

Presentation: day tags staggered on two heights, not one row; setup labels DX1/DX2/DX3/DX1.Tue/DX3.Tue stacked over Monday-Tuesday candles 100.85-101.15 in _all and _week; zone labels run across the forecast week in _all.

## 2. EURUSD 2026-07-06 (anchor week)

Obvious trades: operator #1 (Mon SHORT 1.14322) OUTSIDE the window - 1.14322 traded only Mon 01:00-05:00 UTC (after 06:00 Monday highs 1.14288 / 1.14282 and lower). In window: 7 trades (#2-#8).

E1 (6 zones):
- 1H BoM Supply 1.14738-1.14807: NOT REACHED (high 1.14608).
- 1H MoM Supply (Mitigated 4x) 1.14601-1.14677 (parts 1.14573-1.14728): REACTED (Fri 02:00 1.14608 -> 1.14114).
- UPPER RESISTANCE 1.14444-1.14533 (parts 1.14316-1.14635): REACTED (Mon 23:00 1.14480, Tue 12:00 1.14421, Thu 06:00 1.14494 - all rejected).
- GAP IN-FILL 1.14220-1.14280 (parts 1.14108-1.14339): REACTED (Wed 07:00 1.14315 rejection, Thu 10:00 low 1.14209 bounce, Fri 20:00 low 1.14114).
- MID-RANGE SUPPORT 1.13977-1.14053 (part 1.14004-1.14147): REACTED (Mon 13:00 1.14083, Wed 01:00 1.13983).
- 4H BoM Demand 1.13721-1.13832 (parts to 1.13886): NOT REACHED - Wed 15:00 low 1.13911 stopped 2.5 pips above its part (counted as "at a zone", not missing).
- Turning points without a zone: none.
- E1 = 4/4 = **100%**.
- Side: **FAIL - bunched.** 1H BoM part 1.14738 vs 1H MoM part 1.14728 (1 pip); 1H MoM 1.14573 overlaps UPPER RES part 1.14635; UPPER RES part 1.14316 overlaps GAP part 1.14339; GAP part 1.14108 overlaps MID-RANGE part 1.14147. One unbroken wall 1.13690-1.14837.

E2 (his tags inverted):
- Mon SS: WRONG (his SS+BS; no BS in the tag).
- Tue SS: RIGHT.
- Wed SS+RWL+BS up: RIGHT.
- Thu BS up: RIGHT (ladder long).
- Fri BS+WL+RWL up: RIGHT by the rule (carries WL+RWL); the 'up' did not happen (Fri 1.14608 -> close 1.14147).
- E2 = **80%**.

E3:
- #2 Mon LONG 1.14106: CAUGHT by EU4 1.14095 (Mon 10:00 -> TP Mon 18:45).
- #3 Tue SHORT 1.14441: CAUGHT by EU1 1.14442 (Mon 18:30 -> TP Tue 21:15; its SL 1.14508 survived the 1.14480 high by 2.8 pips).
- #4 Wed LONG 1.14012: CAUGHT by EU7 1.14018 (Tue 21:30 -> TP Wed 07:15).
- #5 Wed SHORT 1.14277: CAUGHT by EU5 1.14269 (Wed 07:15 -> TP Wed 11:30).
- #6 Wed LONG 1.13953: CAUGHT by EU6 1.13940 (Wed 11:30 -> TP Fri 02:00).
- #7 Thu LONG 1.14233: CAUGHT by EU8 1.14239 (Thu 00:00 -> TP Fri 02:00).
- #8 Fri SHORT 1.14578: CAUGHT by EU9 1.14598 (Fri 02:15 -> TP Fri 12:45).
- Stopped: **EU2** (SHORT 1.14385, Mon 17:15 -> stopped Mon 21:45), **EU4.Tue** (LONG 1.14095, Tue 19:15 -> stopped Tue 21:30).
- E3 = 7/7 = **100%**. (Facts also show a Tue SS SHORT 1.14385 discarded as EMISSION_CAPPED.)

Presentation: EU1...EU7 labels piled on top of each other over the Mon-Wed candles (1.1400-1.1445) in _all and _week; 'Mon SS 80%' partly hidden under the 1H MoM zone label.

## 3. GBPUSD 2026-07-06 (anchor week)

Obvious trades: all 7 operator trades are in the window (#1 LONG 1.33331: price traded 1.33301 Mon 06:00 and 1.33286 Mon 07:00).

E1 (8 zones):
- RESISTANCE CEILING 1.34484-1.34548 (parts 1.34386-1.34708): REACTED (Fri 02:00 1.34517 -> 1.33918).
- 4H BoM Supply 1.34264-1.34340 (parts 1.34145-1.34294): REACTED (Thu 06:00 1.34308 -> 1.33807).
- UPPER RESISTANCE 1.33933-1.34005 (parts 1.33941-1.34162): REACTED (Mon 22:00-Tue 01:00 1.34013 / 1.34015 -> decline; Wed 17:00 1.34104).
- UPPER RESISTANCE 1.33643-1.33717 (parts 1.33583-1.33946): REACTED (Tue 05-09 support 1.33751 / 1.33693; Thu 12:00 low 1.33807 in the part -> rally).
- UPPER RESISTANCE 1.33435-1.33521 (parts 1.33340-1.33666): REACTED (Tue 21:00-Wed 05:00 consolidation 1.3342-1.3359).
- MID-RANGE SUPPORT 1.33225-1.33285 (parts 1.33082-1.33333): REACTED (Mon 07:00 1.33286, Wed 09:00 1.33222 -> +88).
- KEY SUPPORT 1.32970-1.33046 and KEY SUPPORT 1.32789-1.32877: NOT REACHED.
- Turning points without a zone: none.
- E1 = 6/6 = **100%**.
- Side: **FAIL - bunched.** Eight zones, 27 parts, one wall 1.32639-1.34708: three separate UPPER RESISTANCE zones whose parts overlap (1.33583-1.33666, 1.33933-1.33946), crossed together by the Tue 13:00-21:00 decline 1.3387 -> 1.3343; UPPER RES part 1.33340 vs MID-RANGE part 1.33333 (0.7 pip); KEY SUPPORT part 1.32932 vs KEY SUPPORT part 1.32928 (0.4 pip); 4H BoM part 1.34145 overlaps UPPER RES part 1.34162.

E2: Mon SS WRONG (no BS); Tue SS RIGHT; Wed SS+RWL+BS up RIGHT; Thu BS up RIGHT; Fri BS+WL+RWL up RIGHT by the rule (the Wed box 1.33155-1.33496 was 61 pips below the day's high 1.34104, the Thu box 1.33270-1.33825 48 pips below 1.34308 - the levels are far off even where the tag is right). E2 = **80%**.

E3:
- #1 Mon LONG 1.33331: CAUGHT by GB2 1.33333 (Mon 06:15 -> TP Mon 18:45).
- #2 Mon SHORT 1.33934: CAUGHT by GB1 1.33959 (Mon 18:45 -> TP Wed 09:00).
- #3 Wed LONG 1.3333: CAUGHT by GB4 1.33255 (Wed 09:00 -> TP Thu 06:15) - same turn, same zone, but the entry is 7.5 pips deeper than his (outside the ~3-pip tolerance); counted CAUGHT under step 4 ("same direction at that zone"), flagged.
- #4 Wed LONG 1.33629 (reinforcement): MISSED - no setup (reinforcements at 1.33813 / 1.34154 / 1.34222 rejected).
- #5 Thu SHORT 1.34246: CAUGHT by GB6 1.34254 (Thu 06:15 -> TP Thu 11:15).
- #6 Thu LONG 1.33829: MISSED - GB7 1.33888 is a Friday order, not live at the Thu 12:00 low 1.33807.
- #7 Fri SHORT 1.34481: MISSED - no setup at the Fri 02:00 top 1.34517.
- Stopped: none (GB3 void).
- E3 = 4/7 = **57%**.

Presentation: in _all, three 'UPPER RESISTANCE ...' labels run through the forecast week candles at 1.3340-1.3400 with GB1/GB2/GB3/GB4 labels on top of them.

## 4. DXY 2026-04-20

Obvious trades (operator, S3): LONG 98.02 / SL 97.87 / TP 98.77 (Mon 15:00 low 98.006) and LONG 98.29 / SL 98.185 / TP 98.77 (Wed 05:00 low 98.211).

E1 (6 zones):
- UPPER RESISTANCE 98.939-99.005 (+4H BoM 98.884-99.031): REACTED (Thu 17:00 98.939 -> 98.688; Fri 03:00 98.915 -> 98.489).
- 1H MoM Supply 98.675-98.845 (parts 98.667-98.868): REACTED (Thu 00:00 98.737 -> 98.584; Thu 10:00 98.803 -> 98.534; consolidation Thu-Fri).
- UPPER RESISTANCE 98.456-98.541 (parts 98.345-98.625): REACTED (Mon 05:00 98.395 in the sweep part; Tue 17:00 98.567 -> 98.211; Thu 14:00 low 98.534 bounce; Fri 20:00 98.489).
- GAP IN-FILL 98.220-98.280 (parts 98.182-98.364): REACTED (Wed 05:00 low 98.211 -> +43).
- MID-RANGE SUPPORT 98.058-98.145 (parts 97.937-98.078): REACTED (Mon 15:00 low 98.006, consolidation Mon 14:00-Tue 06:00).
- KEY SUPPORT 97.725-97.799: NOT REACHED.
- Turning points without a zone: none.
- E1 = 5/5 = **100%** - but note the six zones with their parts cover 97.576-99.031 with no gap wider than 5.5 pips, so the whole week's range 98.006-98.939 lies inside zones; no turn could have been 'missing'.
- Side: **FAIL - bunched.** 1H MoM part 98.868 vs UPPER RES (4H BoM) part 98.884 (1.6 pips), crossed together by the Thu 17:00 candle; UPPER RES 98.456 parts (98.345-98.439) overlap GAP parts (98.300-98.364); GAP part 98.182 vs MID-RANGE 98.145 (3.7 pips); 1H MoM part 98.667 vs UPPER RES part 98.625 (4.2 pips).

E2:
- Mon SS: RIGHT (stayed inside the 97.869-98.539 range; ceiling 98.395 rejected, floor 98.006 held). Note: the day was a single 39-pip leg down then flat, not a series of swings.
- Tue SS+RWL+BS up: RIGHT (range, dip to 98.123, surge to 98.567).
- Wed BS up: RIGHT (98.211 -> 98.643 through the 98.456-98.541 zone).
- Thu BS+RWL up: RIGHT (spike down to 98.534, surge to 98.939).
- Fri RWL down: RIGHT (98.915 -> 98.489).
- E2 = **100%**.

E3:
- Trade 1 LONG 98.02: CAUGHT by DX1 98.019 (Mon 15:15 -> TP 98.874 Thu 17:30).
- Trade 2 LONG 98.29: CAUGHT by DX2 98.270 (2 pips; Wed 05:15 -> TP Thu 17:30).
- Stopped: **DX3** (Thu Ladder LONG 98.660, SL 98.615 = 4.5 pips, filled Thu 00:00, stopped Thu 00:15).
- E3 = 2/2 = **100%**.

Presentation: _week frame axis is not fitted to the week (97.5-99.6) because the next week's open bar (Sun Apr 26 22:00, open 99.332) is in the frame; labels 'GAP IN-FILL ...' and 'MID-RANGE SUPPORT ...' sit over candles (Apr 19-21, 98.1-98.2); 'DX1 BS L 4.8R' over Monday candles.

## 5. EURUSD 2026-04-20

Obvious trades (listed before setups): T1 Mon LONG 1.1747 (EQUILIBRIUM) -> 1.1790 (UPPER RES 1H MoM part); T2 Mon 23:00-Tue SHORT 1.1791 -> 1.1719 (GAP 1.17203-1.17263); T3 Tue 19:00-Wed 05:00 LONG 1.1719 -> 1.1762 (EQUILIBRIUM parts); T4 Wed SHORT 1.1762 -> 1.1692 (MID-RANGE); T5 Thu 14:00-17:00 SHORT 1.1717 -> 1.1669 (KEY SUPPORT parts); T6 Thu/Fri LONG 1.1669 -> 1.1723 (GAP 1.17203-1.17263). 6 trades.

E1 (9 zones):
- UPPER RESISTANCE 1.18213-1.18292: NOT REACHED (high 1.17910).
- UPPER RESISTANCE 1.17988-1.18067 (parts 1.17847-1.18110): REACTED (Mon 13:00-23:00 top 1.17910 in the MoM supply part -> -72).
- UPPER RESISTANCE 1.17706-1.17791: REACTED (capped Mon 05-12 at 1.17718 / 1.17755; Tue 13:00 rally to 1.17759 rejected -> 1.17403).
- EQUILIBRIUM 1.17497-1.17573 (parts to 1.17661): REACTED (Mon low 1.17470; Wed 05:00 1.17624 -> -70).
- GAP IN-FILL 1.17347-1.17407: REACTED (consolidation Tue 21:00-Wed 05:00 1.1732-1.1751).
- GAP IN-FILL 1.17203-1.17263 (parts 1.17126-1.17327): REACTED (Tue 19:00 low 1.17187 -> +44; Thu 14:00 1.17165; Fri 20:00 1.17230).
- MID-RANGE SUPPORT 1.16973-1.17033 (parts 1.16809-1.17207): REACTED (consolidation Wed 17:00-Thu 05:00, low 1.16921).
- GAP IN-FILL 1.16744-1.16804: REACTED (Thu 09:00 1.16789 -> +37).
- KEY SUPPORT 1.16570-1.16638 (parts 1.16543-1.16754): REACTED (Thu 17:00 1.16691, Fri 03:00 1.16729 -> +54).
- Turning points without a zone: none (as for DXY 04-20, the zones cover 1.16543-1.18491 with no real gap).
- E1 = 8/8 = **100%**.
- Side: **FAIL - bunched.** GAP 1.16744-1.16804 sits inside KEY SUPPORT's part 1.16638-1.16754 and 0.5 pip from MID-RANGE's part 1.16809 - three labelled zones touching over 1.16543-1.17207; EQUILIBRIUM part 1.17661 overlaps the 1.17706 zone's part 1.17668; 1.17988 zone part 1.18110 overlaps 1.18213 zone part 1.18125. In the frames the two red supply parts (1.17847-1.17988 and 1.18239-1.18491) read as one red mass 1.1785-1.1849 (64 pips) from Apr 19 on.

E2:
- Mon SS: RIGHT (rise 1.1747 -> 1.1791 stopped under the 1.17988 ceiling; inside the box).
- Tue SS+RWL+BS down: RIGHT (1.1791 -> 1.1719).
- Wed BS down: RIGHT (1.1762 -> 1.1703).
- Thu BS+RWL down: RIGHT (down to 1.16691 with a whip to 1.17165).
- Fri RWL up: RIGHT (1.1673 -> 1.1723).
- E2 = **100%**.

E3:
- T1 Mon LONG: MISSED (no long setup).
- T2 SHORT 1.1791: CAUGHT by EU2 1.17920 (Mon 23:00 -> TP 1.17512 Tue 15:00); EU3 same entry ran to TP 1.17006 Thu 00:00.
- T3 LONG: MISSED. T4 Wed SHORT 1.1762: MISSED (EU4 1.17656 not filled; high 1.17624). T5 Thu SHORT: MISSED (EU5 1.17372 not filled). T6 LONG: MISSED.
- Stopped: none.
- E3 = 1/6 = **17%**.

Presentation: EU1/EU2/EU3 labels stacked over Monday candles (1.1775-1.1785); 'Mon SS 65%' hidden behind the UPPER RES label.

## 6. GBPUSD 2026-04-20

Obvious trades: T1 Mon LONG 1.3482 (MID-RANGE) -> 1.3544; T2 Mon 15:00-Tue 08:00 SHORT 1.3544 -> 1.3482 (MID-RANGE); T3 Tue LONG 1.3482 -> 1.3540 (UPPER RES); T4 Tue SHORT 1.3540 -> 1.3474 (MID-RANGE); T5 Tue 19:00-Wed 09:00 LONG 1.3474 -> 1.3535; T6 Wed 09:00-Thu 17:00 SHORT 1.3535 -> 1.3448 (1H MoM demand); T7 Thu/Fri LONG 1.3448 -> 1.3537. 7 trades (a 60-pip swing week).

E1 (6 zones + 1 discovery):
- UPPER RESISTANCE 1.35241-1.35327 (parts 1.35163-1.35332): REACTED (Tue 14:00 1.35396 -> -65; Wed 09:00 1.35353 -> down; Fri 20:00 1.3537).
- UPPER RESISTANCE (HEAVY) 1.34932-1.35019 (parts to 1.35107): REACTED only as consolidation - price oscillated through it ~10 times all week.
- MID-RANGE SUPPORT 1.34768-1.34846 (parts 1.34691-1.34803): REACTED (lows Mon 1.34818, Tue 08:00 1.34823, Tue 19:00 1.34744, Thu 00:00 1.34789).
- 1H MoM Demand 1.34345-1.34660 (parts 1.34227-1.34700): REACTED (Thu 17:00 1.34476, Fri 03:00 1.34532 -> +84).
- KEY SUPPORT 1.33998-1.34073, sweep zone 1.33805-1.33855, discovery 1.34147: NOT REACHED.
- Turning point without a zone: **Mon 15:00 high 1.35444** (11.7 pips above the top zone's 1.35327; zones beyond are behind the toggle) - MISSING.
- E1 = 4/(4+1) = **80%**.
- Side: **FAIL - missing + bunched.** Missing 1.35444. MID-RANGE part 1.34691-1.34803 overlaps the 1H MoM Demand's part 1.34640-1.34700; UPPER RES part 1.35163 vs HEAVY part 1.35107 (5.6 pips). The 1H MoM Demand box with parts is 47 pips tall (1.34227-1.34700) - borderline bloated against the 34-pip reference.

E2:
- Mon SS (box 1.34345-1.35019): WRONG - broke up through the HEAVY resistance, high 1.35444, closed 1.35333, 31 pips above the box.
- Tue SS+RWL+BS down: WRONG - the swings were there but the BS down never came (dip 1.34744 = 2 pips under MID-RANGE, back to 1.35068).
- Wed BS down: WRONG - range day 1.34901-1.35353, no breakout.
- Thu BS+RWL down: RIGHT (Thu 17:00 break 1.3490 -> 1.34476 into the 1H MoM demand).
- Fri RWL up: RIGHT (1.34532 -> 1.35370; direction and key zone right; box 1.34174-1.34660 far too low).
- E2 = 2/5 = **40%**.

E3:
- All 7 MISSED. GB1 LONG 1.34660 not filled; GB3 SHORT 1.34818, GB4 LONG 1.34083, GB5 SHORT 1.34557 not filled.
- Stopped: **GB2** (Tue BS SHORT 1.35163, filled Mon 07:15, stopped Mon 15:15 by the Monday breakout).
- E3 = 0/7 = **0%**.

Presentation: Mon/Tue/Wed tag labels partly hidden; GB2/GB1/GB3 labels over Tue-Wed candles; the yellow path dives to 1.3408 on Thursday, 40 pips under the actual low.

## 7. DXY 2026-10-05

Window starts Mon 06:00 (the 102.535 high at Mon 04:00 is history). Obvious trades: T1 Mon 06:00-Tue 12:00 SHORT 102.43 -> 101.75 (KEY SUPPORT 101.750-101.843); T2 Tue 12:00-Wed 12:00 LONG 101.75 -> 102.50 (LSZ 102.485-102.535); T3 Wed 12:00-Fri 05:00 SHORT 102.50 / 102.47 -> 101.92 (MID-RANGE parts); T4 Fri LONG 101.92 -> 102.335. 4 trades.

E1 (5 zones + 2 discovery):
- LSZ supply 102.485-102.535: REACTED (Wed 12:00 102.499 -> -37; Thu 11:00 102.467, 1.8 pips under it).
- LSZ supply 102.157-102.207 (reach 102.307): REACTED (Tue 06:00 102.285 -> -53).
- MID-RANGE SUPPORT 101.961-102.051 (parts 101.916-102.132): REACTED (Mon 22:00 102.044; Fri 05:00 101.920 -> +41).
- KEY SUPPORT 101.750-101.843 (parts 101.668-101.926): REACTED (Tue 12:00 101.754 -> +75).
- KEY SUPPORT 101.479-101.565: NOT REACHED.
- Discovery 102.141 MA: REACTED (Thu 02:00 low 102.133 -> +33). Discovery 103.000: NOT REACHED.
- Turning points without a zone: none (Mon 06:00-07:00 high 102.433 is 5.2 pips under the LSZ - counted at the zone, borderline).
- E1 = 5/5 = **100%**.
- Side: **FAIL - bunched.** LSZ 102.157-102.207 vs MID-RANGE's supply-side sweep part 102.082-102.132 (2.5 pips, both supply-side sweep zones that the legend says should be one box) with the 102.141 discovery line between them; MID-RANGE part 101.916-101.996 overlaps KEY SUPPORT part 101.855-101.926; KEY SUPPORT 101.479's sweep reach 101.712 overlaps the upper KEY SUPPORT's part 101.668. All crossed together by the Tue 06:00-12:00 decline.

E2: all five days SS, box 101.755-102.635; the week ranged 101.754-102.499 inside it, swings respecting both bounds every day. Mon RIGHT, Tue RIGHT (floor 101.754 = box bottom), Wed RIGHT, Thu RIGHT, Fri RIGHT. E2 = **100%**.

E3:
- T1 SHORT: CAUGHT by DX1 102.435 (Mon 06:30 -> TP 101.941 Tue 11:15).
- T2 LONG: CAUGHT by DX2 101.926 (Tue 11:00 -> TP 102.420 Wed 12:00; SL 101.725 survived by 2.9 pips).
- T3 SHORT: CAUGHT by DX1.Wed (Wed 12:00 -> TP Fri 05:30); DX1.Thu also TP.
- T4 LONG: MISSED - DX2.Fri filled Fri 05:30 but was still open at the week end (high 102.335, TP 102.420).
- Stopped: none.
- E3 = 3/4 = **75%**.

Presentation: day-wide red/green position boxes 101.73-102.66 cover every candle of the week in _all / _week; DX1.Tue (not filled) and the skipped DX1.Fri are drawn.

## 8. EURUSD 2026-10-05

Obvious trades: T1 Mon LONG 1.1169 (LSZ 1.11610-1.11660) -> 1.1225 (sweep zones 1.12149-1.12258); T2 Tue LONG 1.1203 (sweep 1.12149-1.12199 reach) -> 1.1277 (1H BoM supply); T3 Tue 12:00-Wed 12:00 SHORT 1.1277 -> 1.1165 (LSZ); T4 Wed-Thu LONG 1.1165 -> 1.1213; T5 Thu SHORT 1.1213 -> 1.1172; T6 Thu 11:00-Fri 05:00 LONG 1.1172 -> 1.1243 (UPPER RES); T7 Fri SHORT 1.1243 -> 1.1187. 7 trades.

E1 (5 zones + 4 discovery):
- 1H BoM Supply 1.12716-1.12853 (parts 1.12611-1.12866): REACTED (Tue 12:00 1.12767 -> -112).
- UPPER RESISTANCE 1.12451-1.12530 (parts to 1.12612): REACTED (Tue 13:00-21:00 consolidation; Fri 05:00 1.12427 -> -55).
- Sweep zone 1.12208-1.12258: REACTED (Mon 17:00-Tue 05:00 consolidation; Thu 14:00 1.12267).
- Sweep zone 1.12149-1.12199 (part 1.12039-1.12149): REACTED (Tue 06:00 1.12028 -> +74).
- LSZ demand 1.11610-1.11660: REACTED (Mon 06:00 1.1169; Wed 12:00 1.11645 -> +48).
- Discovery 1.12364 MA: PIERCED (crossed up Tue 05-09 and down Wed 01-05 with no reaction).
- Discovery 1.12137 MA: REACTED (Thu 02:00 1.12128 -> -41). Discovery 1.12000: REACTED (consolidation Wed 13:00-Thu 01:00). Discovery 1.11500: NOT REACHED.
- Turning points without a zone: **Thu 11:00 low 1.11719** (5.9 pips above the LSZ, -41 then +71) and **Fri 16:00 low 1.11874** (12.6 pips under the 1.12000 line, end of a -55 leg) - MISSING.
- E1 = 7/(8+2) = **70%**.
- Side: **FAIL - bunched + missing.** The two demand-side sweep zones 1.12149-1.12199 and 1.12208-1.12258 are 0.9 pip apart yet drawn as two labelled zones (the legend says one box), with discovery lines 1.12137 and 1.12000 inside their reach; their labels overprint each other ('LSZ demand-side | sweep to 1.12049 + 4H liquidity' over 'DISCOVERY ZONE | MA convergence'). Missing 1.11719 and 1.11874.

E2 (SS all week, box 1.11510-1.12712): Mon RIGHT (1.1169 -> 1.1225 inside); Tue RIGHT (ceiling swept 5.5 pips to 1.12767, reversed); Wed RIGHT (1.1263 -> 1.11645 floor); Thu RIGHT; Fri RIGHT. E2 = **100%**.

E3:
- T1 Mon LONG: CAUGHT by EU1 1.11710 (Mon 06:30 -> TP 1.12476 Tue 09:45).
- T2 Tue LONG 1.1203: MISSED (no order at that turn; EU1 was already in).
- T3 SHORT 1.1277: CAUGHT by EU2.Wed 1.12585 (filled Tue 21:00 -> TP Wed 12:15) - after **EU2** (same entry) was stopped Tue 12:00 by the 1.12767 top.
- T4 LONG: MISSED (EU1.Wed filled Wed 12:15, open at the week end; Fri high 1.12427 is 5 pips short of TP).
- T5, T6, T7: MISSED (no setups; EU1.Thu open at week end).
- Stopped: **EU2** (Tue SHORT 1.12585, SL 1.12742, filled Tue 11:15, stopped Tue 12:00).
- E3 = 2/7 = **29%**.

Presentation: 'Mon SS 80%' hidden under the '1H (Unmitigated) | BoM' label; 'EU2 SS S 5.5R' printed over the Tue tag; week-wide position boxes 1.1148-1.1277 cover all candles.

## 9. GBPUSD 2026-10-05

Obvious trades: T1 Mon SHORT 1.3239 (1H BoM supply) -> 1.3190 (MID-RANGE part); T2 Mon 13:00-Tue 01:00 LONG 1.3190 -> 1.3232; T3 Tue 06:00-15:00 LONG 1.3201 -> 1.3286; T4 Tue 15:00-Wed 12:00 SHORT 1.3286 -> 1.3194; T5 Thu LONG 1.3184 (LSZ) -> 1.3249 (UPPER RES); T6 Fri SHORT 1.3250 -> 1.3206 (MID-RANGE part). 6 trades.

E1 (5 zones + 1 discovery):
- UPPER RESISTANCE 1.32457-1.32535 (parts 1.32450-1.32636): REACTED (Thu 14:00 1.32485, Fri 05:00 1.32503 -> -45; pierced on Tuesday's way up).
- 1H BoM Supply 1.32319-1.32395: REACTED (Mon 06:00-09:00 1.32390 -> -49; Tue 01:00 1.32318).
- GAP IN-FILL 1.32124-1.32184 (parts 1.32121-1.32276): REACTED (consolidation Mon, Wed 17:00-Thu 05:00).
- MID-RANGE SUPPORT 1.31991-1.32051 (parts 1.31899-1.32071): REACTED (Mon 13:00 1.31900, Tue 06:00 1.32013, Wed 12:00 1.31935, Fri 12:00 1.32057).
- LSZ 1.31806-1.31864: REACTED (Thu 10:00 1.31843 -> +64).
- Discovery 1.31630: NOT REACHED.
- Turning point without a zone: **Tue 15:00 high 1.32856** (22 pips above the top zone's parts, 18 above its sweep reach) - MISSING.
- E1 = 5/(5+1) = **83%**.
- Side: **FAIL - missing + bunched.** Missing 1.32856. 1H BoM part 1.32270 overlaps GAP part 1.32276; MID-RANGE part 1.31899 vs LSZ 1.31864 (3.5 pips); UPPER RES part 1.32450 vs 1H BoM 1.32395 (5.5 pips). One wall 1.31806-1.32636.

E2 (SS all week, box 1.31799-1.32395):
- Mon RIGHT (1.31900-1.32390, both bounds held).
- Tue WRONG - breakout up 46 pips above the box ceiling to 1.32856, closed 1.32742.
- Wed WRONG - a one-way 82-pip drop from 36 pips above the box back to the floor, not swing scalps inside it.
- Thu RIGHT (floor sweep 1.31843, ceiling overshoot 9 pips at 1.32485, closed back).
- Fri WRONG - ten 1H closes above the 1.32395 ceiling (Fri 01:00-09:00, 18:00-19:00); the day ranged 1.3206-1.3250 under the UPPER RES, not inside the forecast range; the tool itself voided the ceiling order ('closed through Tue 08:00').
- E2 = 2/5 = **40%**.

E3:
- T1 SHORT: CAUGHT by GB1 1.32329 (Mon 07:45 -> TP 1.32014 Mon 13:15).
- T2 LONG: CAUGHT by GB2 1.31899 (Mon 13:45 -> TP 1.32304 Tue 01:30).
- T3 LONG 1.3201 -> 1.3286: MISSED (GB2.Tue at 1.31899 not filled).
- T4 SHORT 1.3286: MISSED (GB1.Wed void).
- T5 LONG: CAUGHT by GB2.Thu 1.31899 (Thu 07:00 -> TP Thu 14:15).
- T6 SHORT: MISSED (GB1.Fri void).
- Stopped: none.
- E3 = 3/6 = **50%**.

Presentation: void orders GB1.Wed / GB1.Thu / GB1.Fri are still drawn with labels; the Tue-Wed spike to 1.3286 is outside every drawing.

## 10. DXY 2026-05-18

Obvious trades: T1 Mon 22:00-Tue 14:00 LONG 98.944 (MID-RANGE) -> 99.434 (LSZ); T2 Wed 14:00-15:00 SHORT 99.472 (LSZ parts) -> 98.966 (MID-RANGE); T3 Wed 15:00-Thu 13:00 LONG 98.966 -> 99.515 (LSZ reach / 99.500); T4 Thu SHORT 99.515 -> 99.092. 4 trades. (Mon 99.307 -> 98.946 is 36 pips, under the threshold.)

E1 (5 zones + 2 discovery):
- LSZ supply 99.359-99.409 (parts to 99.503, reach 99.509): REACTED (Tue 14:00 99.434, Wed 99.471/99.472 -> -51, Thu 13:00 99.515 -> -42, Fri 14:00 99.412).
- 1H MoM Demand 99.251-99.298 (parts 99.251-99.320): REACTED (consolidation all week around the anchor 99.301).
- 1H MoM Demand 99.174-99.244 (parts 99.125-99.298): REACTED (Fri 13:00 99.172 bounce; Thu 18:00-Fri consolidation).
- MID-RANGE SUPPORT 98.963-99.037 (parts to 99.097): REACTED (Mon lows 98.971 / 98.946; Wed 15:00 98.966 -> +55).
- 1H MoM Demand 98.844-98.889 (parts to 98.939): NOT REACHED (low 98.944, 0.5 pip above its part).
- Discovery 99.500: REACTED (Thu 13:00 99.515 -> -42). Discovery 99.695: NOT REACHED.
- Turning points without a zone: none.
- E1 = 5/5 = **100%**.
- Side: **FAIL - bunched.** Two separate '1H (Unmitigated) | MoM' demand zones overlap: 99.251-99.298 and the other's part 99.244-99.298 lie on top of each other (their two labels overprint in the frames); LSZ part 99.359 vs 1H MoM part 99.320 (3.9 pips); 1H MoM part 99.125 vs MID-RANGE part 99.097 (2.8 pips); MID-RANGE 98.963 vs 1H MoM part 98.939 (2.4 pips). One wall 98.744-99.509.

E2 (SS all week, box 98.963-99.509): Mon RIGHT (floor 98.946, 1.7-pip sweep), Tue RIGHT, Wed RIGHT, Thu RIGHT (99.515, 0.6 pip beyond the reach, reversed), Fri RIGHT. E2 = **100%**.

E3:
- T1-T4 all MISSED. The only order, DX1 LONG 99.050, filled Mon 11:30 and was stopped; its four repeats were voided ("anchor zone closed through Mon 20:00"). No short setup at all in a week with three clean tops at the LSZ.
- Stopped: **DX1** (Mon SS LONG 99.050, SL 98.971, filled Mon 11:30, stopped Mon 16:15).
- E3 = 0/4 = **0%**.

Presentation: void repeats DX1.Tue / DX1.Wed / DX1.Thu / DX1.Fri are drawn with labels; the two 1H MoM labels overprint each other at 99.20-99.25.

## 11. EURUSD 2026-05-18

Obvious trades: T1 Mon LONG 1.1622 (EQUILIBRIUM) -> 1.1661 (UPPER RES part); T2 Mon 22:00-Tue 15:00 SHORT 1.1662 -> 1.1592 (MID-RANGE); T3 Wed 14:00-15:00 LONG 1.1583 -> 1.1645 (spike to the 1.16409 line / EXTREME part); T4 Thu 08:00-13:00 SHORT 1.1635 -> 1.1576; T5 Thu 13:00-17:00 LONG 1.1576 -> 1.1630 (EQUILIBRIUM). 5 trades.

E1 (4 zones + 3 discovery):
- UPPER RESISTANCE 1.16641-1.16726 (parts 1.16604-1.16826): REACTED (Mon 22:00 1.16617 -> -70).
- UPPER RESISTANCE (EXTREME) 1.16493-1.16562 (parts 1.16456-1.16574): REACTED (Mon 09:00 1.16572 -> 1.16264; Wed 15:00 1.16448 rejection).
- EQUILIBRIUM 1.16219-1.16296 (parts 1.16168-1.16395): REACTED (Thu 08:00 1.16353 -> -59; consolidation Wed 17:00-Thu 05:00).
- MID-RANGE SUPPORT 1.15970-1.16036 (part 1.16083-1.16133): REACTED (Tue 15:00 1.15921 sweep, consolidation Tue 13:00-Wed 13:00).
- Discovery 1.16409 MA: REACTED (Wed 15:00 spike top 1.16448). Discovery 1.15500, 1.15072: NOT REACHED.
- Turning points without a zone: **Wed 14:00 low 1.15827** (14 pips under MID-RANGE) and **Thu 13:00 low 1.15762** (21 pips under it, the week's low) - MISSING.
- E1 = 5/(5+2) = **71%**.
- Side: **FAIL - missing + bunched.** Missing 1.15827 / 1.15762. UPPER RES part 1.16604 vs EXTREME part 1.16574 (3 pips) - two labelled resistance zones; EQUILIBRIUM part 1.16168 vs MID-RANGE part 1.16133 (3.5 pips).

E2 (SS all week, box 1.15747-1.16672): Mon RIGHT, Tue RIGHT (ceiling to floor), Wed RIGHT, Thu RIGHT (low 1.15762 inside the box by 1.5 pips), Fri RIGHT. E2 = **100%**.

E3:
- T1 LONG: MISSED - instead **EU2** SHORT 1.16297 was filled against it.
- T2 SHORT: CAUGHT by EU1 1.16604 (Mon 20:15 -> TP 1.15985 Tue 14:15); EU1.Tue same.
- T3 LONG: MISSED (EU3.Wed 1.15815 not filled; low 1.15827).
- T4 SHORT: MISSED (EU1.Thu at 1.16604 never reached; EU2.Thu void).
- T5 LONG: CAUGHT by EU3.Thu 1.15815 (Thu 13:30 -> TP 1.16285 Thu 17:45).
- Stopped: **EU2** (Mon SS SHORT 1.16297, filled Mon 06:00, stopped Mon 07:15).
- E3 = 2/5 = **40%**. (Friday setups discarded as EMISSION_CAPPED.)

Presentation: the '2.1bn' and '1.5bn' option-strike labels at ~1.1650 are printed on top of each other; 'EU1.Thu' over them; EU labels on Mon-Tue candles; void EU2.Wed / EU2.Thu drawn.

## 12. GBPUSD 2026-05-18

Obvious trades: T1 Mon 06:00-16:00 LONG 1.3322 (GAP 1.33240-1.33300) -> 1.3449 (UPPER RES); T2 Mon 16:00-Tue 14:00 SHORT 1.3449 -> 1.3379 (GAP 1.33720-1.33780); T3 Wed 08:00-15:00 LONG 1.3375 -> 1.3463; T4 Thu 08:00-13:00 SHORT 1.3455 -> 1.3390 (UPPER RES 1.33950-1.34037); T5 Thu 13:00-17:00 LONG 1.3390 -> 1.3449; T6 Fri 07:00-13:00 LONG 1.3413 -> 1.3463; T7 Fri 13:00-close SHORT 1.3463 -> 1.3420. 7 trades.

E1 (9 zones + 6 discovery):
- UPPER RESISTANCE 1.34497-1.34557 (part 1.34423-1.34540): REACTED (Mon 16:00 1.34494 -> -71; Wed 15:00 1.34630 / Fri 13:00 1.34631 = 7 pips over, reversed; Thu 08:00 1.34548 -> -64).
- GAP IN-FILL 1.34239-1.34299 (part to 1.34339): REACTED (consolidation Wed 17:00-Fri).
- UPPER RESISTANCE 1.33950-1.34037 (parts 1.33816-1.34137): REACTED (ceiling Tue 09-21; Thu 13:00 low 1.33904 -> +59).
- GAP IN-FILL 1.33720-1.33780: REACTED (Tue 14:00 1.33785, Wed 08:00 1.33750 -> +88).
- GAP IN-FILL 1.33492-1.33552: REACTED (Mon 09:00 dip 1.33465 -> +103).
- GAP IN-FILL 1.33240-1.33300 (parts 1.33147-1.33381): REACTED (Mon 06:00 low 1.33217 -> rally).
- MID-RANGE 1.32995-1.33055, GAP 1.32668-1.32728, KEY SUPPORT 1.32484-1.32544: NOT REACHED.
- Discovery 1.34369: REACTED (consolidation around it Tue / Thu-Fri). Discovery 1.33851: REACTED (consolidation Tue-Wed). Discovery 1.33654: PIERCED (crossed up Mon 07:00 and down/up Mon 09:00 with no reaction). Discovery 1.33197, 1.32830, 1.32000: NOT REACHED.
- Turning points without a zone: none.
- E1 = 8/9 = **89%**.
- Side: **FAIL - floating + bunched.** Floating: GAP 1.32668-1.32728 (49 pips under the week low 1.33217), KEY SUPPORT 1.32484-1.32544 (67 pips), discovery 1.32830 (39) and 1.32000 (122 pips) - far beyond the 22-pip reference. Bunched: GAP 1.33240's part 1.33147 overlaps MID-RANGE part 1.33142; UPPER RES part 1.33816 vs GAP 1.33780 (3.6 pips); GAP part 1.33644 vs discovery 1.33654 (1 pip) - Mon 06:00-08:00 candles crossed four labelled objects in one push (1.3315 -> 1.3384); GAP part 1.32569 vs KEY SUPPORT 1.32544 (2.5 pips). 15 labelled objects in 256 pips.

E2 (SS all week, box 1.33047-1.34137):
- Mon WRONG - breakout surge +127 pips, 36 pips over the box ceiling, closed 18 above.
- Tue RIGHT - London/NY swings 1.3379-1.3420 under the 1H MoM ceiling (the 1.34371 high is the Monday-night carry-over).
- Wed WRONG - NY surge +88 to 1.34630, 49 pips above the box, closed 19 above.
- Thu WRONG - the day ranged 1.3390-1.3455, i.e. above the forecast range; the forecast ceiling became the floor.
- Fri WRONG - whole day above the box (low 1.34132 = box top).
- E2 = 1/5 = **20%**. The _week frame shows it plainly: candles sit above the yellow path's top for four days.

E3:
- T1 LONG: CAUGHT by GB2 1.33247 (Mon 06:00 -> TP 1.33926 Mon 12:30).
- T2-T7: MISSED (GB1 short stopped; all later GB1 repeats void; GB2 repeats at 1.33247 never reached).
- Stopped: **GB1** (Mon SS SHORT 1.33983, SL 1.34167, filled Mon 12:30, stopped Mon 15:45).
- E3 = 1/7 = **14%**.

Presentation: void GB1.Tue...GB1.Fri drawn; four discovery lines + 9 zone labels make the 1.3300-1.3460 band a stack of text over the forecast-week candles in _all.

---

## Table of all 12 maps

| Map | E1 % | E1 side condition | E2 % | E3 % | stopped setups |
|---|---|---|---|---|---|
| DXY 2026-07-06 | 100 (5/5) | FAIL (bunched) | 80 (4/5) | 100 (7/7) | DX2.Tue |
| EURUSD 2026-07-06 | 100 (4/4) | FAIL (bunched) | 80 (4/5) | 100 (7/7) | EU2, EU4.Tue |
| GBPUSD 2026-07-06 | 100 (6/6) | FAIL (bunched) | 80 (4/5) | 57 (4/7) | - |
| DXY 2026-04-20 | 100 (5/5) | FAIL (bunched) | 100 (5/5) | 100 (2/2) | DX3 |
| EURUSD 2026-04-20 | 100 (8/8) | FAIL (bunched) | 100 (5/5) | 17 (1/6) | - |
| GBPUSD 2026-04-20 | 80 (4/5) | FAIL (missing, bunched) | 40 (2/5) | 0 (0/7) | GB2 |
| DXY 2026-10-05 | 100 (5/5) | FAIL (bunched) | 100 (5/5) | 75 (3/4) | - |
| EURUSD 2026-10-05 | 70 (7/10) | FAIL (bunched, missing) | 100 (5/5) | 29 (2/7) | EU2 |
| GBPUSD 2026-10-05 | 83 (5/6) | FAIL (missing, bunched) | 40 (2/5) | 50 (3/6) | - |
| DXY 2026-05-18 | 100 (5/5) | FAIL (bunched) | 100 (5/5) | 0 (0/4) | DX1 |
| EURUSD 2026-05-18 | 71 (5/7) | FAIL (missing, bunched) | 100 (5/5) | 40 (2/5) | EU2 |
| GBPUSD 2026-05-18 | 89 (8/9) | FAIL (floating, bunched) | 20 (1/5) | 14 (1/7) | GB1 |

Totals:

| Set | E1 pooled | E1 mean | E2 pooled | E2 mean | E3 pooled | E3 mean | side condition |
|---|---|---|---|---|---|---|---|
| All 12 maps | 89.3% (67/75) | 91.1% | 78.3% (47/60) | 78.3% | 46.4% (32/69) | 48.5% | 0/12 PASS |
| 9 maps outside 2026-07-06 | 86.7% (52/60) | 88.2% | 77.8% (35/45) | 77.8% | 29.2% (14/48) | 36.1% | 0/9 PASS |

Reading of the totals, without softening: the high E1 ratio is not a sign of precise zones. On every map the zones and their parts form one continuous stack over (and beyond) the whole weekly range, so almost every turn "has a zone", and the conjunctive part of the rule ("and none bloated, bunched, floating or missing") is met on 0 of 12 maps. E3 outside the anchor week catches fewer than one obvious trade in three. 9 setups were stopped across the 12 maps.

## The five defects that cost the most

1. **Bunched zone walls (all 12 maps; side condition FAIL 12/12, and it inflates E1).** Separately labelled zones whose parts overlap or sit 0-4 pips apart, stacked into one band over the whole week. Worst: GBPUSD 07-06, three UPPER RESISTANCE zones 1.33340-1.34162 with overlapping parts, crossed together by the Tue 13:00-21:00 decline; DXY 04-20, 1H MoM part 98.868 vs UPPER RES part 98.884 (1.6 pips), both crossed by the Thu 17:00 candle; DXY 05-18, two 1H MoM demand zones on top of each other at 99.244-99.298; EURUSD 10-05, two demand sweep zones 0.9 pip apart (1.12199 / 1.12208) drawn as two boxes against the legend's own one-box rule.
2. **All-week SS range forecasts that missed breakouts (E2).** GBPUSD 05-18: Mon +127 to 1.34494, Wed +88 to 1.34630, Thu-Fri traded above the 1.34137 box top -> E2 20%. GBPUSD 10-05: Tue break to 1.32856 (46 pips over the 1.32395 ceiling), Wed one-way drop, Fri ten 1H closes above the ceiling -> 40%. GBPUSD 04-20: Mon closed 1.35333 above the 1.35019 box and the Tue/Wed BS down never came -> 40%. All the E2 loss outside the anchor week is on GBPUSD.
3. **One fixed pair of range orders, voided for the rest of the week after one close-through (E3).** DXY 05-18: DX1 LONG 99.050 stopped Mon 16:15, DX1.Tue-Fri void, no short at the LSZ that rejected price three times (99.434 Tue, 99.472 Wed, 99.515 Thu) -> 0/4. GBPUSD 05-18: GB1 stopped Mon 15:45, all repeats void -> 1/7. GBPUSD 10-05: GB1.Wed-Fri void, missing the 1.3286 and 1.3250 shorts -> 3/6. EURUSD 04-20: no long setups at all in a week with three clean long legs -> 1/6. GBPUSD 04-20: 0/7.
4. **No zone at the week's extremes (missing).** GBPUSD 10-05 Tue 15:00 high 1.32856 (22 pips above the highest zone part drawn); GBPUSD 04-20 Mon 15:00 high 1.35444 (11.7 pips above); EURUSD 05-18 Wed 14:00 low 1.15827 and Thu 13:00 low 1.15762 (14 and 21 pips under the lowest zone); EURUSD 10-05 Thu 11:00 low 1.11719 and Fri 16:00 low 1.11874. Meanwhile GBPUSD 05-18 draws floating zones 49-122 pips below the week low (1.32484-1.32728, discovery 1.32000).
5. **Setups stopped by the very turn they were trading (9 losses).** DXY 04-20 DX3 (SL 4.5 pips, stopped 15 minutes after the Thu 00:00 fill); EURUSD 10-05 EU2 (SL 1.12742, stopped by the 1.12767 Tue top); EURUSD 05-18 EU2 SHORT 1.16297 (stopped 75 minutes after the Mon 06:00 fill, against the week's first long leg); GBPUSD 04-20 GB2 (stopped by Monday's breakout, Mon 15:15); GBPUSD 05-18 GB1 (Mon 15:45); DXY 05-18 DX1 (Mon 16:15); DXY 07-06 DX2.Tue; EURUSD 07-06 EU2 and EU4.Tue.

Other presentation defects seen in the frames (all maps): zone labels in the _all frames run across the forecast-week candles; setup labels pile up over the first two days (EURUSD 07-06 EU1-EU7, DXY 07-06 DX1-DX3); day tags hidden under zone labels (EURUSD 10-05 'Mon SS', EURUSD 07-06 'Mon SS', EURUSD 04-20 'Mon SS'); option-strike labels printed over each other (EURUSD 05-18 '2.1bn' / '1.5bn' at ~1.1650); void or never-filled repeats still drawn (DXY 05-18 DX1.Tue-Fri, GBPUSD 05-18 GB1.Tue-Fri, GBPUSD 10-05 GB1.Wed-Fri); day-wide position boxes covering every candle of range weeks (DXY 10-05, EURUSD 10-05); day tags staggered on two heights instead of one row (all 07-06 maps); DXY 04-20 _week axis not fitted to the week (the next week's open bar at 99.33 is in the frame).
