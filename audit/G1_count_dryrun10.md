# G1 outside count 10 (fresh reviewer, 2026-11-27)

Scope: 12 maps (DXY / EURUSD / GBPUSD x 2026-07-06, 2026-04-20, 2026-10-05, 2026-05-18), frames `evidence/s3j/*_{zones,all,week}.png` (all 36 opened and read), exact prices / times from `audit/g1_facts_j/*.txt`, 1H / 15m closes and extremes checked read-only with `e1_tool/e1_data.py`. No earlier count, no memory/, no tool code read.

## Counting rules applied (so anyone can recount)

- Week = Monday 06:00 UTC (02:00 New York, the anchor) to Friday 21:00 UTC. Bar times below are UTC.
- **E1**: one verdict per labelled zone (parts belong to their zone; a turn at a part is a turn at the zone) and per discovery line. REACTED = sharp rejection, or consolidation in / around it. PIERCED = crossed with no reaction. NOT REACHED = untouched. MISSING = an obvious turning point of the week (a 1H swing that started a move of 30+ pips, 35+ on GBPUSD) with no E1 object within about 5 pips. **E1 % = reacted / (reached + missing)**.
- **Side condition** (from the operator's L-28 words and his two reference maps):
  - bloated = a zone well over his 34-pip reference;
  - bunched (a) = two LABELLED boxes 0-2 pips apart or overlapping, crossed together by one candle;
  - bunched (b) = the same test on full extents with parts (dotted sweep-reach outlines not counted);
  - floating = a labelled zone or discovery line whose near edge is more than about 25 pips beyond the week's post-anchor high / low (his reference allows 22);
  - missing = as above.
  - The PASS / FAIL in the table uses (a) + floating + bloated + the missing points named. (b) is reported per map so the count can be read either way.
- **E2**: a day is RIGHT when its tag's shape, direction and key zone match that day's candles (New York day, 17:00-17:00). 2026-07-06: right only if the tag carries the operator's shapes (DXY: Mon SS+BS, Tue SS, Wed SS+RWL+BS, Thu ladder short, Fri WL+RWL; the pairs take the same shapes with the direction inverted). A day that broke out of a forecast SS box is WRONG.
- **E3 obvious trades**:
  - 2026-07-06: the operator's trades from golden_week.json. His trade 1 on DXY and EURUSD is out of the window: it filled before 06:00 UTC, and price only came back to the entry after the move was over. GBPUSD keeps all 7.
  - DXY 2026-04-20: his two LONGs.
  - Other 8 maps, listed from the candles BEFORE matching setups: every leg of a 1H zigzag with a reversal threshold of 30 pips (35 on GBPUSD) and an amplitude of 30+ (35+) pips whose starting turn is after the anchor. The opening leg is counted from its post-anchor extreme when that leg still runs 30+ (35+) pips.
  - CAUGHT = a setup of the same direction, filled at that turn's zone, that hit TP before SL. A position already open from an earlier turn does not catch a later turn. Every stopped setup is named.
- Totals are given both pooled (sum of numerators / sum of denominators) and as the mean of the per-map percentages.

---

## DXY 2026-07-06 (anchor week)
Week (post-anchor) H 101.275 Wed 15:00, L 100.598 Fri 02:00.

**E1:**
- 4H BoM Supply 101.316-101.430: NOT REACHED (week high 101.275, 4 pips under).
- UPPER RESISTANCE 101.199-101.262 (+LQ to 101.305): REACTED. Wed 01:00 101.215 -> 100.95; Wed 09:00-15:00 highs 101.239 / 101.256 / 101.275 -> sell-off to 100.786.
- EQUILIBRIUM 100.985-101.077 (parts 100.942-101.153): REACTED. Mon 10:00 101.145 -> down; Wed 07:00 100.95 -> up to 101.239; Thu 11:00 101.039 -> down to 100.598.
- MID-RANGE SUPPORT 100.724-100.815 (parts 100.654-100.876): REACTED. Tue 01:00 100.803 and Thu 06:00 100.786 -> rallies. Pierced on Fri 02:00 and recovered.
- GAP IN-FILL 100.599-100.659: REACTED (Fri 02:00 low 100.598 -> 100.991).
- KEY SUPPORT BAND 100.470-100.530: NOT REACHED.
- Discovery 100.899 (MA): PIERCED. Crossed Mon, Tue, Thu and Fri with no turn at it.
- Missing: none.
- **E1 = 4/5 = 80%.**

Side condition:
- Bloated: none (largest full extent 22 pips).
- Bunched (a): none; labelled boxes 5.4 / 12 / 17 / 6.5 / 7 pips apart.
- Bunched (b): yes, the full extents tile 100.470-101.432 with gaps of 0-0.9 pips: 4H S / UR 0.9; UR / EQ touching; MRS / GAP overlap; GAP / KSB touching.
- Floating: none.
- **PASS** (FAIL under b).

**E2:**
- Mon: WRONG. The tag is SS only; his is SS+BS (Mon BS short 101.14 -> 100.84 is not in the tag).
- Tue: RIGHT (SS).
- Wed: RIGHT (SS+RWL+BS down = his).
- Thu: RIGHT (BS down = breakout down continuing).
- Fri: RIGHT (BS+WL+RWL carries WL+RWL).
- **E2 = 4/5 = 80%.**

**E3** (his trades 2-8; trade 1 Mon LONG 100.945 filled 01:15, outside the window):
- T2 SHORT 101.14: CAUGHT by DX2 (101.138, TP Tue 01:30).
- T3 LONG 100.845: CAUGHT by DX3 (100.851, TP Tue 23:45; SL 100.795 vs low 100.803).
- T4 SHORT 101.19: CAUGHT by DX5 (101.203).
- T5 LONG 100.975: CAUGHT by DX6 (100.980).
- T6 SHORT 101.235: CAUGHT by DX4 (101.235).
- T7 SHORT 100.975: CAUGHT by DX7 (100.980; SL 101.077 vs Thu high 101.071).
- T8 LONG 100.615: CAUGHT by DX8 (100.628).
- Stopped: **DX2.Tue** (SHORT 101.138, filled Tue 19:15, stopped Tue 23:45).
- **E3 = 7/7 = 100%.**

Presentation:
- `DX2 SS S 6.8R` sits on the EQUILIBRIUM label, which reads garbled `DX2 SS S 6.8R ... + DX2.Tue ... LSZ, LQ` in `_all`.
- `DX4 BS S 6.3R`, `DX6 RWL L 3.4R` and `DX7 Ladder S 3.1R if DX4` sit on Wed-Thu candles.
- `1.4bn Option Strike Target` overlaps the DX7 label.
- `Fri BS+WL+RWL` overlaps `DXA7` at the right edge.

## EURUSD 2026-07-06 (anchor week)
Week H 1.14608 Fri 02:00, L 1.13911 Wed 15:00.

**E1:**
- 1H BoM Supply 1.14738-1.14807: NOT REACHED.
- 1H Mit4x Supply 1.14601-1.14677: REACTED (Fri 02:00 1.14608 -> 1.14117).
- UPPER RESISTANCE 1.14444-1.14533 (parts 1.14316-1.14635): REACTED. Mon 23:00 1.1448, Thu 06:00 1.14494, Tue 12:00 1.14421, Wed 07:00 1.14315 all rejected.
- GAP IN-FILL 1.14220-1.14280 (parts 1.14108-1.14339): REACTED. Tue 10:00 1.14234, Thu 10:00 1.14209 and Wed 21:00 1.14141 -> rallies.
- MID-RANGE SUPPORT 1.13977-1.14053: REACTED. Wed 01:00 1.13983 -> rally; Wed 09:00-15:00 consolidation 1.13911-1.13961 just under it -> rally.
- 4H BoM Demand 1.13721-1.13832: NOT REACHED.
- Missing: none.
- **E1 = 4/4 = 100%.**

Side condition:
- Bunched (a): none (gaps 6-17 pips).
- Bunched (b): yes, the full extents are continuous 1.13977-1.14728: UR / 1H Mit4x overlap; UR / GAP overlap; GAP / MRS overlap.
- In `_zones` the whole week's candles sit inside one wall of boxes.
- Floating: none.
- **PASS** (FAIL under b).

**E2** (DXY shapes inverted):
- Mon: WRONG (SS only, his SS+BS).
- Tue, Wed, Thu, Fri: RIGHT.
- **E2 = 4/5 = 80%.**

**E3** (his trades 2-8; trade 1 Mon SHORT 1.14322 filled Sun 21:15, outside the window):
- T2: CAUGHT by EU4 (1.14095).
- T3: CAUGHT by EU1 (1.14442).
- T4: CAUGHT by EU7 (1.14018).
- T5: CAUGHT by EU5 (1.14269).
- T6: CAUGHT by EU6 (1.13940).
- T7: CAUGHT by EU8 (1.14239).
- T8: CAUGHT by EU9 (1.14598).
- Stopped:
  - **EU2** (SHORT 1.14385, stopped Mon 21:45);
  - **EU4.Tue** (LONG 1.14095, stopped Tue 21:30).
- Defect: Monday carries two orders per SS bound (EU1+EU2 short, EU3+EU4 long), against the one-order-per-bound-per-day rule; EU2 is the loser.
- **E3 = 7/7 = 100%.**

Presentation:
- Mon-Tue setup labels pile on each other and on candles at 1.1415-1.1440 (EU1 SS / EU1.Tue / EU2 SS / EU3.Tue / EU4 SS / EU3 SS / EU4.Tue / EU7).
- `EUA5 ALT BS ...` and `EUA7 ALT Ladder ...` labels run across Thu-Fri candles.

## GBPUSD 2026-07-06 (anchor week)
Week H 1.34517 Fri 02:00, L 1.33222 Wed 09:00.

**E1:**
- RESISTANCE CEILING 1.34484-1.34548: REACTED (Fri 02:00 1.34517 -> 1.33918).
- 4H BoM Supply 1.34264-1.34340: REACTED (Thu 06:00 1.34308 -> 1.33807; Fri 11:00 1.34373 -> down).
- UPPER RESISTANCE 1.33933-1.34005 (parts to 1.34162): REACTED. Tue 01:00 1.34015 -> down 60; Wed 17:00 1.34104 -> down; Fri 14:00 1.33918 held.
- UPPER RESISTANCE 1.33643-1.33717: REACTED (Wed 08:00 1.33702 -> 1.33222; Tue 14:00 1.33858 at part; Wed 21:00 / Thu 12:00 lows 1.33799 / 1.33807 at part).
- UPPER RESISTANCE 1.33435-1.33521: REACTED (Wed 01:00 1.33422, Wed 13:00 1.33402 lows; Wed 10:00 1.33568 high).
- MID-RANGE SUPPORT 1.33225-1.33285: REACTED (Mon 07:00 1.33286, Wed 09:00 1.33222 -> rallies).
- KEY SUPPORT BAND 1.32970-1.33046: NOT REACHED.
- KEY SUPPORT BAND 1.32789-1.32877: NOT REACHED.
- Missing: none. The stack tiles 1.33082-1.34630, so every turn has a box.
- **E1 = 6/6 = 100%.**

Side condition:
- Bunched (a): none (gaps 9-26 pips).
- Bunched (b): yes; 4H S / UR overlap, UR3 / MRS 0.7, KSB1 / KSB2 0.4.
- Floating: **KEY SUPPORT BAND 1.32789-1.32877 sits 34.5 pips below the week low.**
- Three "UPPER RESISTANCE" boxes stacked inside 57 pips; `_zones` is a wall of 8 labelled boxes + 27 parts.
- **FAIL** (floating).

**E2:**
- Mon: WRONG (SS only; Monday was a 69-pip BS up 1.33286 -> 1.33972).
- Tue, Wed, Thu, Fri: RIGHT.
- **E2 = 4/5 = 80%.**

**E3** (his 7 trades, all in the window):
- T1 LONG 1.33331: CAUGHT by GB2.
- T2 SHORT 1.33934: CAUGHT by GB1 (1.33959).
- T3 LONG 1.3333: CAUGHT by GB4 (1.33255, same Wed 09:00 turn, same TP 1.3425; entry 7.5 pips below his).
- T4 LONG 1.33629 (reinforcement): MISSED (no setup; reinforcement 1.33813 rejected).
- T5 SHORT 1.34246: CAUGHT by GB6.
- T6 LONG 1.33829 (Thu 12:00 low 1.33807): MISSED. GB7 1.33888 was bracketed to Friday and never filled; GB5 1.33473 never filled.
- T7 SHORT 1.34481 (Fri 02:00): MISSED. No setup at the RESISTANCE CEILING.
- Stopped: none (GB3 void).
- **E3 = 4/7 = 57%.**

Presentation: `GB2 SS L 6.0R`, `GB2.Tue` and `GB1.Tue` overlap the three UPPER RESISTANCE labels in `_all`; ALT labels (GBA4, GBA7, GBA8, GBA9) run across candles.

## DXY 2026-04-20
Week H 98.939 Thu 17:00, L 98.006 Mon 15:00.

**E1:**
- UPPER RESISTANCE 98.939-99.005: REACTED (Thu 17:00 98.939 -> 98.688; Fri 03:00 98.915 -> 98.489).
- 1H MoM Supply 98.675-98.845: REACTED (Thu 00:00 98.737 -> 98.552; Thu 11:00 98.803 -> 98.534).
- UPPER RESISTANCE 98.456-98.541 (parts 98.345-98.625): REACTED. Tue 17:00 98.567 -> 98.211; Thu 14:00 98.534 low -> 98.939.
- GAP IN-FILL 98.220-98.280: REACTED (Wed 05:00 98.211 -> up; Tue 08:00 98.309 -> down).
- MID-RANGE SUPPORT 98.058-98.145: REACTED (Mon 15:00 98.006, Tue 14:00 98.123 -> rallies).
- LQ band 97.920-97.984: NOT REACHED.
- KEY SUPPORT BAND 97.725-97.799: NOT REACHED.
- Missing: none.
- **E1 = 5/5 = 100%.**

Side condition:
- Bunched (a): none (gaps 7.4-17.6 pips).
- Bunched (b): yes; 1H S / UR1 1.6 pips, GAP overlaps UR2, LQ band overlaps MRS.
- Floating: none (KSB 20.7 pips below).
- The standalone LQ band 97.920-97.984 is listed as a zone although the legend says a lone band is not drawn by this script.
- **PASS** (FAIL under b).

**E2:**
- Mon: RIGHT (SS; ranged 98.0-98.4 inside box).
- Tue: RIGHT (SS+RWL+BS up; dip 98.123 then surge to 98.567).
- Wed: RIGHT (BS up; broke UR late Wed toward 98.737).
- Thu: RIGHT (BS+RWL up; 98.534 dip, surge to 98.939).
- Fri: RIGHT (RWL down 98.915 -> 98.489).
- **E2 = 5/5 = 100%.**

**E3** (his two trades):
- LONG 98.02 / 97.87 / 98.77: CAUGHT by DX2 (98.029 / 97.839 / 98.874, filled Mon 15:30, TP Thu 17:30).
- LONG 98.29 / 98.185 / 98.77: CAUGHT by DX3 (98.270 / 98.104 / 98.874, filled Wed 05:15, TP Thu 17:30).
- Stopped:
  - **DX1** (SHORT 98.300, stopped Tue 16:30);
  - **DX5** (LONG 98.660, filled Thu 00:00, stopped Thu 00:15).
- **E3 = 2/2 = 100%.**

Presentation: `DX5 Ladder L 4.8R if DX2` and `DX3 Ladder L 3.6R if DX2` sit on Thu candles and on the `1.1bn` / `1.4bn Option Strike Target` texts; `DX1 RWL S 3.8R` overlaps the GAP IN-FILL label.

## EURUSD 2026-04-20
Week H 1.1791 Mon 23:00, L 1.16691 Thu 17:00.

Obvious trades (listed first):
1. LONG 1.17475 (Mon 06:15) -> 1.1791 (Mon 23:00)
2. SHORT 1.1791 -> 1.17187 (Tue 19:00)
3. LONG 1.17187 -> 1.17624 (Wed 05:00)
4. SHORT 1.17624 -> 1.16789 (Thu 11:00)
5. LONG 1.16789 -> 1.17165 (Thu 14:00)
6. SHORT 1.17165 -> 1.16691 (Thu 17:00)
7. LONG 1.16691 -> 1.1723 (Fri 20:00)

**E1:**
- UR 1.18213-1.18292: NOT REACHED.
- UR 1.17988-1.18067 (part 1H S 1.17847-1.17988): REACTED (Mon 23:00 1.1791 -> down 72).
- UR 1.17706-1.17791: REACTED (Tue 14:00 1.17759 -> down 56; Mon consolidation under it).
- EQ 1.17497-1.17573: REACTED (Mon lows 1.17475 / 1.17551; Tue 12:00 1.1754; Wed 05:00 1.17624 -> down 83).
- GAP 1.17347-1.17407: REACTED (Tue 21:00 1.17318 -> up).
- GAP 1.17203-1.17263: REACTED (Tue 19:00 1.17187 -> up 44).
- MRS 1.16973-1.17033: REACTED (Thu 00:00 1.16921; Fri 13:00 1.16986).
- GAP 1.16744-1.16804: REACTED (Thu 11:00 1.16789 -> up 38).
- KSB 1.16570-1.16638 (part 1H D to 1.16754): REACTED (Thu 17:00 1.16691; Fri 03:00 1.16729).
- Missing: none.
- **E1 = 8/8 = 100%.**

Side condition:
- Bunched (a): none.
- Bunched (b): yes; UR1 / UR2 1.5 pips, UR3 / EQ 0.7, GAP2 / MRS overlap, GAP3 / KSB overlap. 9 zones + 23 parts form one continuous wall 1.1654-1.1849.
- Floating: **UR 1.18213-1.18292, 30 pips above the week high.**
- Bloated look: in `_zones` the two supply parts plus UR1 / UR2 read as ONE red block 1.1785-1.1849 (64 pips) starting Apr 18.
- **FAIL** (floating).

**E2:**
- Mon: RIGHT (SS; inside box, up to the ceiling).
- Tue: RIGHT (SS+RWL+BS down; ceiling reject, breakdown to 1.17187).
- Wed: RIGHT (BS down 1.17624 -> 1.1703).
- Thu: RIGHT (BS+RWL down).
- Fri: RIGHT (RWL up 1.16729 -> 1.1723).
- **E2 = 5/5 = 100%.**

**E3:**
- 1: MISSED.
- 2: CAUGHT by EU2 / EU3 (SHORT 1.17920, filled Mon 23:00, TP Tue 15:00 / Thu 00:00).
- 3: MISSED.
- 4: MISSED (EU4 SHORT 1.17656 was 3 pips above the Wed 05:00 high and never filled).
- 5, 6, 7: MISSED.
- Stopped: **EU5** (LONG 1.17006, stopped Thu 17:30).
- **E3 = 1/7 = 14%.**

Presentation: `EU4 Ladder S 12.3R if EU3` is printed over `1.1bn Option Strike Target`; EU1 / EU2 / EU3 labels stack on Mon candles at 1.1775-1.1785.

## GBPUSD 2026-04-20
Week H 1.35444 Mon 15:00, L 1.34476 Thu 17:00.

Obvious trades:
1. LONG 1.34818 (Mon 06:15) -> 1.35444 (Mon 15:00)
2. SHORT -> 1.34823 (Tue 08:00)
3. LONG -> 1.35396 (Tue 14:00)
4. SHORT -> 1.34744 (Tue 19:00)
5. LONG -> 1.35353 (Wed 09:00)
6. SHORT -> 1.34781 (Thu 13:00)
7. LONG -> 1.35182 (Thu 14:00)
8. SHORT -> 1.34476 (Thu 17:00)
9. LONG -> 1.3537 (Fri 20:00)

**E1:**
- UR 1.35241-1.35327: REACTED. Consolidation in / around it Mon-Wed; Wed 05:00 / 09:00 1.35342 / 1.35353 -> down.
- UR 1.34932-1.35019 HEAVY: REACTED (Mon 08:00 1.34929, Wed 13:00 1.3492 lows; Thu 01:00 / 09:00 / 12:00 highs at its parts).
- MRS 1.34768-1.34846: REACTED (Mon 06:00 1.34818, Tue 08:00 1.34823, Tue 17:00 1.3476, Thu lows 1.3478-1.3483).
- 1H MoM Demand 1.34345-1.34660: REACTED (Thu 17:00 1.34476, Fri 03:00 1.34532 -> up 89).
- KSB 1.33998-1.34073: NOT REACHED.
- LSZ 1.33805-1.33855: NOT REACHED.
- Discovery 1.34147: NOT REACHED.
- **MISSING:** the week's highs 1.3540-1.3545 (Mon 15:00 1.35444 -> down 62; Tue 14:00 1.35396 -> down 65) are 7-12 pips above the top zone; nothing is drawn above 1.35332.
- **E1 = 4/5 = 80%.**

Side condition:
- Bunched (a): none.
- Bunched (b): yes; MRS / 1H D overlap, KSB / LSZ overlap.
- Bloated: the 1H demand full extent is 1.34227-1.34700 = 47 pips.
- Floating: **KSB 1.33998-1.34073 (40 pips below the low), LSZ 1.33805-1.33855 (62 pips below), discovery 1.34147 (33 pips below).**
- **FAIL.**

**E2:**
- Mon: WRONG. SS forecast, but Monday broke the box ceiling 1.35019 and ran to 1.35444, closing 1.35333 above the box (BS up).
- Tue: WRONG. The tagged breakout down never came; 60-pip swings both ways, close 1.35068.
- Wed: WRONG. BS down forecast; the day ranged 1.3490-1.3535 and the low 1.34901 held above MRS.
- Thu: RIGHT (BS down to 1.34476 + RWL to 1.34857, key zone 1H D reached).
- Fri: RIGHT (RWL up 1.34532 -> 1.3537).
- **E2 = 2/5 = 40%.**

**E3:**
- All 9 MISSED.
- Stopped:
  - **GB2** (SHORT 1.35163, filled Mon 07:15, stopped Mon 15:15);
  - **GBA2** (SHORT 1.35063, filled Tue 21:00, stopped Wed 05:15).
- GB1 / GB3 / GB4 / GB5 never filled.
- **E3 = 0/9 = 0%.**

Presentation: `GBA2 ALT RWL S ...` is printed over `1.0bn Option Strike Target`; the yellow path dives to 1.3410 Thu while the candles stay above 1.3447.

## DXY 2026-05-18
Week H 99.515 Thu 13:00, L 98.944 Mon 22:00.

Obvious trades:
1. SHORT 99.307 (Mon 06:00) -> 98.944 (Mon 22:00)
2. LONG 98.944 -> 99.472 (Wed 14:00)
3. SHORT 99.472 -> 98.966 (Wed 15:00, one candle)
4. LONG 98.966 -> 99.515 (Thu 13:00)
5. SHORT 99.515 -> 99.092 (Thu 17:00)
6. LONG 99.092 -> 99.412 (Fri 14:00)

**E1:**
- LSZ supply-side 99.359-99.409 (reach 99.509): REACTED. Tue 14:00 99.434, Wed 08:00 / 14:00 99.471 / 99.472, Thu 13:00 99.515 and Fri 14:00 99.412 all turned down.
- 1H MoM Demand 99.251-99.298: REACTED (Tue 18:00 99.234, Wed 04:00 99.285, Wed 11:00 99.294 lows).
- 1H MoM Demand 99.174-99.244: REACTED (Mon 10:00 99.248 high; Tue 12:00 99.177, Fri 13:00 99.172 lows).
- MRS 98.963-99.037: REACTED (Mon 98.98 / 98.971 / 98.944, Wed 15:00 98.966 -> rallies).
- 1H MoM Demand 98.844-98.889: NOT REACHED.
- Discovery 99.500: REACTED (Thu 13:00 99.515 -> down 42).
- Discovery 99.695: NOT REACHED.
- Missing: none.
- **E1 = 5/5 = 100%.**

Side condition:
- **Bunched (a): the two labelled 1H demand boxes 99.174-99.244 and 99.251-99.298 are 0.7 pip apart. The Mon 11:00 candle (99.248 -> 99.059) and the Wed 14:00 candle (99.472 -> 99.124) crossed both together.** Both labels also overlap each other in `_zones`.
- Bunched (b): also yes.
- Floating: none.
- **FAIL.**

**E2:**
- Mon-Fri: all RIGHT. The week was a 98.94-99.52 range inside the SS box 98.963-99.509; Thu's 99.515 is the sweep of the box top.
- **E2 = 5/5 = 100%.**

**E3:**
- All 6 MISSED.
- Stopped: **DX1** (LONG 99.050 / SL 98.971, filled Mon 11:30, stopped Mon 16:15 by the 98.971 low). All its repeats were then voided, so no setup existed for the rest of the week.
- No short was ever placed at the LSZ that turned price four times.
- DXB2 was triggered but never filled.
- **E3 = 0/6 = 0%.**

Presentation: the two 1H labels (`... MoM + LSZ`, `... MoM + LQ`) overlap each other and the candles; `DXA2 ALT BS ...` box floats 99.4-99.65 above the week.

## DXY 2026-10-05
Week H 102.499 Wed 12:00 (post-anchor), L 101.754 Tue 12:00.

Obvious trades:
1. SHORT 102.433 (Mon 06:30) -> 101.754 (Tue 12:00)
2. LONG 101.754 -> 102.499 (Wed 12:00)
3. SHORT -> 102.133 (Thu 02:00)
4. LONG -> 102.467 (Thu 11:00)
5. SHORT -> 102.033 (Thu 14:00)
6. LONG -> 102.367 (Thu 16:00)
7. SHORT -> 101.920 (Fri 05:00)
8. LONG -> 102.335 (Fri 14:00)

**E1:**
- LSZ 102.485-102.535: REACTED (Wed 12:00 102.499 -> down 37; Thu 11:00 102.467 -> down 43).
- LSZ 102.157-102.207 (reach 102.307): REACTED (Tue 06:00 102.285 -> down 53; Wed 09:00 / 15:00 lows 102.198 / 102.223).
- MRS 101.961-102.051: REACTED (Tue 01:00 102.044, Thu 14:00 / 17:00 102.033 / 102.035, Fri 05:00 101.920 at its LQ part).
- KSB 101.750-101.843: REACTED (Tue 12:00 101.754 and Tue 15:00 101.772 -> up 74).
- KSB 101.479-101.565: NOT REACHED.
- Discovery 102.141: REACTED (Thu 02:00 102.133 -> up 33). It sits 1 pip from an MRS part, not in an empty part of the map.
- Discovery 103.000: NOT REACHED.
- **MISSING:** the resistance shelf 102.33-102.39 (Mon 13:00 102.372, Wed 16:00 102.351, Thu 07:00 102.391, Thu 16:00 102.367 -> down 45, Fri 14:00 102.335) has no box, only the dotted reach line 102.307 under it.
- **E1 = 5/6 = 83%.**

Side condition:
- Bunched (a): none.
- Bunched (b): yes; MRS / KSB overlap, LSZ2 / MRS 2.5 pips.
- Floating: **discovery 103.000, 46.5 pips above the week high.**
- **FAIL.**

**E2:**
- Mon-Fri: all RIGHT. A range week 101.75-102.50 inside the SS box 101.755-102.635; Tue's low touched the floor and Wed's high the ceiling LSZ.
- **E2 = 5/5 = 100%.**

**E3:**
- 1: CAUGHT by DX1 (SHORT 102.435, filled Mon 06:30, TP Tue 11:15).
- 2: CAUGHT by DX2 (LONG 101.926, filled Tue 11:00, TP Wed 12:00).
- 3: CAUGHT by DX1.Wed (filled Wed 12:00, TP Fri 05:30).
- 4: MISSED.
- 5: CAUGHT by DX1.Thu (filled Thu 09:45, TP Fri 05:30).
- 6, 7: MISSED.
- 8: MISSED. DX2.Fri filled Fri 05:30 but was still open at the week end; its TP 102.420 was not reached (high 102.335).
- Stopped: none.
- **E3 = 4/8 = 50%.**

Presentation: `DXB2 ALT BS S 3.1R ...` and `DXB3` sit over the Fri candles at the right edge; zone labels in the history half cross the Oct 2-4 candles.

## EURUSD 2026-05-18
Week H 1.16617 Mon 22:00, L 1.15762 Thu 13:00.

Obvious trades:
1. LONG 1.16219 (Mon 06:00) -> 1.16617 (Mon 22:00)
2. SHORT -> 1.15827 (Wed 14:00)
3. LONG -> 1.16448 (Wed 15:00)
4. SHORT -> 1.1594 (Thu 07:00)
5. LONG -> 1.16353 (Thu 08:00)
6. SHORT -> 1.15762 (Thu 13:00)
7. LONG -> 1.163 (Thu 17:00)
8. SHORT -> 1.15882 (Fri 14:00)
9. LONG -> 1.1619 (Fri 17:00)

**E1:**
- UR 1.16641-1.16726: REACTED via its LQ part (Mon 22:00 1.16617 -> down 79).
- UR EXTREME 1.16493-1.16562: REACTED (Mon 12:00 / 16:00 1.16572 / 1.16562; Wed 15:00 1.16448 -> down 51).
- EQ 1.16219-1.16296: REACTED (Mon lows 1.16264 / 1.16287; Wed-Thu highs 1.16352 / 1.16353 at its 1H S part).
- MRS 1.15970-1.16036: REACTED (Tue 15:00 1.15921, Thu 07:00 1.1594 -> rallies).
- LQ band 1.15747-1.15815: REACTED (Wed 08:00 / 14:00 1.15836 / 1.15827, Thu 13:00 1.15762 -> up 62 / 54).
- Discovery 1.16409: PIERCED (crossed Mon, Tue and Wed with no turn at it).
- Discovery 1.15500: NOT REACHED.
- Discovery 1.15072: NOT REACHED.
- Missing: none.
- **E1 = 5/6 = 83%.**

Side condition:
- Bunched (a): none.
- Bunched (b): none within 2 pips (UR1 / UR2 3 pips, EQ / MRS 3.5).
- Floating: **discovery 1.15500 (26 pips below the low) and discovery 1.15072 (69 pips below).**
- **FAIL.**

**E2:**
- Mon-Fri: all RIGHT. A range 1.1576-1.1662 inside the SS box 1.15747-1.16672.
- **E2 = 5/5 = 100%.**

**E3:**
- 1: MISSED.
- 2: CAUGHT by EU1 (SHORT 1.16604, filled Mon 20:15, TP Tue 14:15).
- 3: MISSED (EU3 LONG 1.15815 missed the Wed lows by 1.2 pips).
- 4, 5, 6: MISSED.
- 7: CAUGHT by EU3.Thu (filled Thu 13:30, TP Thu 17:45).
- 8, 9: MISSED.
- Stopped: **EU2** (SHORT 1.16297, filled Mon 06:00, stopped Mon 07:15).
- **E3 = 2/9 = 22%.**

Presentation: the EU1 / EU2 labels on the Mon-Tue candles overlap `3.7bn Option Strike Target` and the DISCOVERY label (`EU1 SS S 6.3R` is unreadable in `_all`); `EUB4 ALT RWL S 9.9R` is drawn over Thu-Fri candles.

## GBPUSD 2026-05-18
Week H 1.34631 Fri 13:00, L (post-anchor) 1.33217 Mon 06:00.

Obvious trades:
1. LONG 1.33217 (Mon 06:00) -> 1.33843 (Mon 08:00)
2. SHORT -> 1.33465 (Mon 10:00)
3. LONG -> 1.34494 (Mon 16:00)
4. SHORT -> 1.34004 (Mon 19:00)
5. LONG -> 1.34391 (Mon 20:00)
6. SHORT -> 1.3375 (Wed 08:00)
7. LONG -> 1.3463 (Wed 15:00)
8. SHORT -> 1.34153 (Thu 07:00)
9. LONG -> 1.34548 (Thu 08:00)
10. SHORT -> 1.33904 (Thu 13:00)
11. LONG -> 1.34492 (Thu 17:00)
12. SHORT -> 1.34132 (Fri 07:00)
13. LONG -> 1.34631 (Fri 13:00)
14. SHORT -> 1.34177 (Fri 14:00)
15. LONG -> 1.34535 (Fri 17:00)

**E1:**
- UR 1.34497-1.34557: REACTED (Mon 16:00 1.34494, Wed 15:00 1.3463, Thu 08:00 1.34548, Fri 13:00 1.34631 -> drops of 45-64 pips).
- GAP 1.34239-1.34299: REACTED, weakly. Consolidation around it; the lows 1.3413-1.3420 sit 2-9 pips under its LQ part.
- UR 1.33950-1.34037: REACTED (Mon 12:00 1.34029; Tue 09:00 1.33871 and Thu 13:00 1.33904 lows).
- GAP 1.33720-1.33780: REACTED (Wed 08:00 1.3375 -> up 88).
- GAP 1.33492-1.33552: REACTED (Mon 10:00 1.33465 -> up 103).
- GAP 1.33240-1.33300: REACTED (Mon 06:00 1.33217 -> up).
- MRS 1.32995-1.33055: NOT REACHED post-anchor.
- GAP 1.32668-1.32728: NOT REACHED.
- KSB 1.32484-1.32544: NOT REACHED.
- Discovery 1.34369: REACTED (highs 1.3438-1.3441 Mon 20:00, Thu 06:00 / 11:00 / 19:00, Fri 08:00).
- Discovery 1.33851: REACTED (Mon 08:00 1.33843).
- Discovery 1.33654: PIERCED.
- Discovery 1.33197: REACTED (Mon 06:00 1.33217). It sits inside the GAP's sweep part, so not in an empty part of the map.
- Discovery 1.32830: NOT REACHED.
- Discovery 1.32000: NOT REACHED.
- Missing: none.
- **E1 = 9/10 = 90%.**

Side condition:
- Bunched (a): none.
- Bunched (b): yes; GAP 1.3324 parts / MRS parts 0.5 pip.
- Floating: **GAP 1.32668-1.32728 (49 pips below the post-anchor low), KSB 1.32484-1.32544 (67 pips), discovery 1.32830 (39 pips), discovery 1.32000 (122 pips).**
- 9 labelled zones + 6 discovery lines in a 220-pip strip; zone labels collide with the discovery labels in `_zones`.
- **FAIL.**

**E2:**
- Mon: WRONG. SS forecast; a 127-pip BS up through the box ceiling 1.34137 to 1.34494, closing 1.34322 above the box.
- Tue: RIGHT (range 1.3378-1.3437; key zone 1H MoM touched).
- Wed: WRONG (88-pip BS up 1.3375 -> 1.3463 out of the box).
- Thu: RIGHT (range, key zone swept at 1.33904 and held).
- Fri: WRONG (the whole day 1.34132-1.34631 lies above the box; the key zone was not reached).
- **E2 = 2/5 = 40%.**

**E3:**
- 1: CAUGHT by GB2 (LONG 1.33247, filled Mon 06:00, TP Mon 12:30).
- 8: CAUGHT by GBB4 ALT (SHORT 1.34487, filled Wed 15:15, TP Thu 13:30; SL 1.34633 vs high 1.3463).
- All others MISSED.
- Stopped:
  - **GB1** (SHORT 1.33983, filled Mon 12:30, stopped Mon 15:45);
  - **GBB3 ALT** (LONG 1.34037, filled Tue 21:00, stopped Tue 21:15).
- After GB1's stop every GB1 repeat was void, and the GB2 repeats at 1.33247 were never reached again. No setup existed in the 1.3375-1.3463 range where the week traded from Tuesday.
- **E3 = 2/15 = 13%.**

Presentation: in `_all` the setup labels GB1.Tue / GB2.Tue / GB1.Wed / GB2.Wed sit inside a stack of 8 zone labels and 4 discovery labels; `GBB4 ALT RWL ...` and `GBB3 ALT BS ...` are printed over Wed-Fri candles.

## EURUSD 2026-10-05
Week H 1.12767 Tue 12:00, L (post-anchor) 1.11645 Wed 12:00.

Obvious trades:
1. LONG 1.1169 (Mon 06:30) -> 1.12207 (Mon 09:00)
2. SHORT -> 1.11863 (Mon 14:00)
3. LONG -> 1.12767 (Tue 12:00)
4. SHORT -> 1.11645 (Wed 12:00)
5. LONG -> 1.12128 (Thu 02:00)
6. SHORT -> 1.11719 (Thu 11:00)
7. LONG -> 1.12267 (Thu 14:00)
8. SHORT -> 1.11845 (Thu 16:00)
9. LONG -> 1.12427 (Fri 05:00)
10. SHORT -> 1.11874 (Fri 16:00)

**E1:**
- 1H BoM Supply 1.12716-1.12853: REACTED (Tue 12:00 1.12767 and 15:00 1.12693 -> down 112).
- UR 1.12451-1.12530: REACTED (Tue 14:00 1.12447 low; Fri 05:00 1.12427 -> down 55).
- LSZ demand 1.12208-1.12258: REACTED (Mon 09:00 1.12207; Thu 14:00 1.12267 -> down).
- LSZ demand 1.12149-1.12199: REACTED (Mon 12:00 / 15:00 highs; Tue 06:00 1.12028 at its LQ part -> up 74).
- LSZ demand 1.11610-1.11660: REACTED (Wed 12:00 1.11645 -> up 48).
- Discovery 1.12364: PIERCED.
- Discovery 1.12137: REACTED (Mon 12:00 1.12135, Thu 02:00 1.12128). It sits inside the LSZ / LQ part, not in an empty part of the map.
- Discovery 1.12000: REACTED (Mon 11:00 / 17:00 lows; Thu 08:00 1.12004 high).
- Discovery 1.11500: NOT REACHED.
- **MISSING:** the support shelf 1.1179-1.1187 (Mon 14:00 1.11863 -> up 90; Wed 08:00 1.11792; Wed 16:00 1.11843; Thu 07:00 1.1182; Thu 16:00 1.11845 -> up 58; Fri 16:00 1.11874) has no box.
- **E1 = 7/9 = 78%.**

Side condition:
- **Bunched (a): the two labelled demand-side LSZ boxes 1.12208-1.12258 and 1.12149-1.12199 are 0.9 pip apart. The 1H candles Oct 6 07:00, Oct 7 07:00 and Oct 8 14:00 crossed both together.** This breaks the legend's own rule ("sweep zones of one side within 5 pips are drawn as one box"), and discovery 1.12137 sits between them.
- Floating: none.
- **FAIL.**

**E2:**
- Mon-Fri: all RIGHT. A range 1.1165-1.1277 inside the SS box 1.11510-1.12712 (Tue sweep 5.5 pips over the box top, rejected).
- **E2 = 5/5 = 100%.**

**E3:**
- 1: CAUGHT by EU1 (LONG 1.11710, filled Mon 06:30, TP Tue 09:45).
- 4: CAUGHT by EU2.Wed (SHORT 1.12585, filled Tue 21:00, TP Wed 12:15).
- 5: MISSED. EU1.Wed filled Wed 12:15 but was open at the week end; TP 1.12476 missed by 5 pips on Fri.
- 7: MISSED. EU1.Thu filled Thu 11:30 but was open at the week end.
- 2, 3, 6, 8, 9, 10: MISSED.
- Stopped: **EU2** (SHORT 1.12585, filled Tue 11:15, stopped Tue 12:00 by the 1.12767 high).
- **E3 = 2/10 = 20%.**

Presentation: three discovery labels and two LSZ labels stack at 1.1200-1.1225 over the Oct 4-6 candles; `EU1 SS L 3.3R` / `EU1.Wed` / `EU1.Thu` sit on the candles of the unmarked 1.118 shelf.

## GBPUSD 2026-10-05
Week H 1.32856 Tue 15:00, L 1.31843 Thu 10:00.

Obvious trades:
1. SHORT 1.3239 (Mon 09:00) -> 1.319 (Mon 13:00)
2. LONG -> 1.32856 (Tue 15:00)
3. SHORT -> 1.31843 (Thu 10:00)
4. LONG -> 1.32485 (Thu 14:00)
5. SHORT -> 1.32037 (Thu 16:00)
6. LONG -> 1.32503 (Fri 05:00)
7. SHORT -> 1.32057 (Fri 12:00)
8. LONG -> 1.32443 (Fri 18:00)

**E1:**
- 4H BoM Supply 1.32610-1.32717: REACTED (Tue 13:00-15:00 1.32833 / 1.32856 just above its parts, Tue 14:00 1.32611 at its floor -> down 101).
- UR 1.32457-1.32535: REACTED (Thu 14:00 1.32485, Fri 05:00 1.32503 -> down 45 each).
- 1H BoM Supply 1.32319-1.32395: REACTED (Mon 09:00 1.3239 -> down 49; Tue 01:00 1.32318 -> down).
- GAP 1.32124-1.32184: REACTED (Wed 15:00 1.32242 and Thu 08:00 1.32125 highs at its parts).
- MRS 1.31991-1.32051: REACTED (Mon 13:00 1.319, Tue 06:00 1.32013, Wed 12:00 1.31935, Thu 16:00 1.32037, Fri 12:00 1.32057 -> rallies).
- LSZ 1.31806-1.31864: REACTED (Thu 10:00 1.31843 -> up 64).
- Discovery 1.32583: PIERCED. It lies inside UR's LQ part, not in an empty part of the map.
- Discovery 1.31630: NOT REACHED.
- Missing: none.
- **E1 = 6/7 = 86%.**

Side condition:
- Bunched (a): none.
- Bunched (b): yes; 4H S / UR overlap, 1H S / GAP overlap.
- Floating: none.
- **PASS** (FAIL under b).

**E2:**
- Mon: RIGHT.
- Tue: WRONG. SS forecast; an 84-pip BS up through the box ceiling 1.32482 to 1.32856, closing 1.32742 above the box.
- Wed: WRONG. The day opened above the box and fell 82 pips through UR / 1H S to the floor: a failed-breakout reversal, not swings respecting the bounds.
- Thu: RIGHT (floor sweep to ceiling).
- Fri: RIGHT.
- **E2 = 3/5 = 60%.**

**E3:**
- 1: CAUGHT by GB1 (SHORT 1.32329, TP Mon 13:15).
- 2: CAUGHT by GB2 (LONG 1.31899, TP Tue 01:30).
- 3: MISSED (no short at the 4H supply; GB1.Wed void).
- 4: CAUGHT by GB2.Thu (TP Thu 14:15).
- 5: MISSED.
- 6: MISSED.
- 7: CAUGHT by GBB3 ALT (SHORT 1.32475, filled Fri 01:30, TP Fri 12:45).
- 8: MISSED.
- Stopped: none.
- **E3 = 4/8 = 50%.**

Presentation: the `1H (Unmitigated) | BoM + IF` label overlaps the Oct 4-5 candles; the GB1.Tue / GB1.Wed / GB1.Thu / GB1.Fri labels sit on candles inside the 1H supply box.

---

## Table of the 12 maps

| Map | E1 % | Side condition (a; b) | E2 % | E3 % |
|---|---|---|---|---|
| DXY 2026-07-06 | 80 (4/5) | PASS (b: FAIL) | 80 | 100 (7/7) |
| EURUSD 2026-07-06 | 100 (4/4) | PASS (b: FAIL) | 80 | 100 (7/7) |
| GBPUSD 2026-07-06 | 100 (6/6) | FAIL: floating KSB 1.32789-1.32877 (b: FAIL) | 80 | 57 (4/7) |
| DXY 2026-04-20 | 100 (5/5) | PASS (b: FAIL) | 100 | 100 (2/2) |
| EURUSD 2026-04-20 | 100 (8/8) | FAIL: floating UR 1.18213-1.18292 (b: FAIL) | 100 | 14 (1/7) |
| GBPUSD 2026-04-20 | 80 (4/5) | FAIL: floating x3, missing 1.3540-1.3545 (b: FAIL) | 40 | 0 (0/9) |
| DXY 2026-05-18 | 100 (5/5) | FAIL: bunched (a) 1H D 99.174-99.244 / 99.251-99.298 | 100 | 0 (0/6) |
| EURUSD 2026-05-18 | 83 (5/6) | FAIL: floating discovery 1.15500, 1.15072 (b: PASS) | 100 | 22 (2/9) |
| GBPUSD 2026-05-18 | 90 (9/10) | FAIL: floating x4 (b: FAIL) | 40 | 13 (2/15) |
| DXY 2026-10-05 | 83 (5/6) | FAIL: floating discovery 103.000, missing 102.33-102.39 (b: FAIL) | 100 | 50 (4/8) |
| EURUSD 2026-10-05 | 78 (7/9) | FAIL: bunched (a) LSZ 1.12208-1.12258 / 1.12149-1.12199, missing 1.1179-1.1187 | 100 | 20 (2/10) |
| GBPUSD 2026-10-05 | 86 (6/7) | PASS (b: FAIL) | 60 | 50 (4/8) |

**Totals, all 12 maps:**
- E1: pooled 68/76 = **89.5%**; mean 90.0%. Side condition PASS 4/12 under (a), 1/12 under (b) (EURUSD 2026-05-18 only, and it fails on floating).
- E2: 49/60 days = **81.7%**.
- E3: pooled 35/95 = **36.8%**; mean 43.9%.

**Totals, the 9 maps outside 2026-07-06:**
- E1: pooled 54/61 = **88.5%**; mean 88.9%. Side condition PASS 2/9.
- E2: 37/45 days = **82.2%**.
- E3: pooled 17/74 = **23.0%**; mean 30.0%.

Stopped-out setups (14):
- DXY 07-06 DX2.Tue
- EURUSD 07-06 EU2, EU4.Tue
- DXY 04-20 DX1, DX5
- EURUSD 04-20 EU5
- GBPUSD 04-20 GB2, GBA2
- DXY 05-18 DX1
- EURUSD 05-18 EU2
- GBPUSD 05-18 GB1, GBB3
- EURUSD 10-05 EU2

## The five defects that cost the most

1. **E3 off the anchor week: the setups cover one or two bounds and then go void or stay unfilled, so most clean swings have no order.**
   - DXY 05-18 is 0/6: DX1 LONG 99.050 was stopped Mon 16:15 at exactly the Mon low 98.971, and all its repeats were then voided. No short ever stood at the LSZ 99.36-99.51 that turned price on Tue 99.434, Wed 99.472, Thu 99.515 and Fri 99.412.
   - GBPUSD 04-20 is 0/9: GB2 SHORT 1.35163 was stopped Mon 15:15 and GBA2 SHORT 1.35063 Wed 05:15; GB1 / GB3 / GB4 / GB5 never filled.
   - GBPUSD 05-18 is 2/15: nothing stood in the 1.3375-1.3463 range from Tuesday.
   - EURUSD 04-20 is 1/7: EU4 SHORT 1.17656 sat 3 pips above the Wed 05:00 high 1.17624.
2. **E2 on GBPUSD: the "DXY ranges all week -> pair SS" translation is blind to GBP's own breakouts.**
   - GBPUSD 05-18: Mon ran +127 pips through the SS box ceiling 1.34137 to 1.34494; Wed +88 to 1.3463; Fri lay wholly above the box.
   - GBPUSD 04-20: Mon broke 1.35019 and ran to 1.35444; Tue and Wed got breakout-down tags but ranged.
   - GBPUSD 10-05: Tue broke 1.32482 and ran to 1.32856; Wed reversed 82 pips.
   - Result: 40 / 40 / 60% on those maps against 100% on DXY and EURUSD.
3. **Floating E1 objects far from the week, while the week's own extremes go unmarked.**
   - GBPUSD 05-18: GAP 1.32668-1.32728 (49 pips below the low), KSB 1.32484-1.32544 (67), discovery 1.32000 (122).
   - GBPUSD 04-20: KSB 1.33998-1.34073 (40 pips below the 1.34476 low), LSZ 1.33805-1.33855 (62), while nothing is drawn at the week's highs 1.3540-1.3545.
   - DXY 10-05: discovery 103.000 (46.5 pips above the high).
   - EURUSD 05-18: discovery 1.15072 (69 pips below).
   - GBPUSD 07-06: KSB 1.32789-1.32877 (34.5 pips below).
4. **Bunched labelled boxes and walls of parts.**
   - DXY 05-18: 1H demand boxes 99.174-99.244 and 99.251-99.298 are 0.7 pip apart and were crossed together by the Mon 11:00 and Wed 14:00 1H candles.
   - EURUSD 10-05: two demand-side LSZ boxes 1.12208-1.12258 and 1.12149-1.12199 are 0.9 pip apart, crossed together by the Oct 6 07:00, Oct 7 07:00 and Oct 8 14:00 candles. This contradicts the legend's own one-box rule for same-side sweep zones within 5 pips.
   - On 11 of 12 maps the full extents with parts tile the whole week's range with 0-2 pip gaps (e.g. EURUSD 04-20: 9 zones + 23 parts from 1.1654 to 1.1849, with a 64-pip red block 1.1785-1.1849). That is why "every turn has a zone" while the map shows no selectivity.
5. **Missing zones at the week's most-used levels, and discovery lines placed inside zones instead of where the map is empty.**
   - Missing: EURUSD 10-05 support 1.1179-1.1187 (six turns, incl. Mon 14:00 -> +90 pips and Thu 16:00 -> +58); DXY 10-05 resistance 102.33-102.39 (five turns, incl. Thu 16:00 -> -45); GBPUSD 04-20 highs 1.3540-1.3545 (two 62-65 pip drops).
   - Discovery lines inside zone parts: DXY 10-05 102.141, EURUSD 10-05 1.12137, GBPUSD 10-05 1.32583, GBPUSD 05-18 1.33197 and 1.33851.

Other defects seen:
- Two orders per SS bound on EURUSD 07-06 Monday (EU1 + EU2 short, EU3 + EU4 long); EU2 was stopped.
- Setup and ALT labels printed over candles and over strike-target texts on every `_all` / `_week` frame (worst: EURUSD 07-06 Mon-Tue, GBPUSD 05-18).
