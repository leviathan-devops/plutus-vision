# G1 count 5 (outside reviewer, fresh count; earlier counts, memory/ and tool code not read)

Sources used: the 36 frames in evidence/s3e/ (each one opened and looked at), audit/g1_facts_e/*.txt for exact prices and setup outcomes, context_management/oracle/golden_week.json for the 07-06 operator trades, and read-only 1H bars from `e1_tool/e1_data.bars(pair,'60')` to check times and closes. Times below are New York unless marked UTC. The forecast week runs from Mon 02:00 NY (06:00 UTC) to Fri close.

## Counting rules applied (so anyone can recount)

**E1 (zones).** One verdict per labelled zone. A zone's extent is its box plus its indented parts (a turn at a part is a turn at its zone). The dotted sweep reach counts only for sweep zones.
- REACTED: on at least one visit there was either a sharp rejection (price left the zone back the way it came, by 10 pips or more for FX, 0.10 for DXY) or consolidation in or around it (3 or more 1H bars) before leaving.
- PIERCED: every visit crossed the zone with no reaction of its own.
- NOT REACHED: price never got to it. A turn that stops within 3 pips in front of a zone (0.03 on DXY) counts as reaching it.
- Obvious turn with no zone: a week swing high or low (a reversal of 30 pips or more on 1H) that is more than 3 pips from every zone extent.
- E1 % = reacted / (zones reached + turns with no zone).
- The G1 qualifier ("none bloated, bunched, floating or missing") is reported separately for each map as PASS or FAIL. It is not folded into the %.

**E2 (days).** One verdict per day: the forecast shape, direction and key zone against that day's candles.
- An SS (range) day is RIGHT if the day stayed inside the forecast range box. It is WRONG if price went more than 10 pips (0.10 DXY) beyond a bound and 1H candles closed beyond it.
- A BS / WL / RWL / Ladder day is RIGHT if the move of the named shape happened in the stated direction. Otherwise it is WRONG.
- E2 % = days right / 5.

**E3 (setups).**
- 2026-07-06: the obvious trades are the operator's trades in the window. A trade whose entry was only available before Mon 06:00 UTC is out: DXY #1 LONG 100.945 and EURUSD #1 SHORT 1.14322 (both sat at the pre-London prices of 00:00-05:00 UTC). All 7 GBPUSD trades are in.
- DXY 2026-04-20: the operator's two trades.
- Other maps: every clean zone-to-zone move of 30 pips or more (0.30 DXY) visible on the 1H chart. I listed these from the `_zones` frame before reading any setup.
- CAUGHT means a setup in the same direction, entered at that turn's zone, that filled and hit TP before SL. Anything else is MISSED.
- Every STOPPED setup is named as a loss, even if price later reached its TP.
- E3 % = caught / obvious trades.

---

## DXY 2026-07-06 (anchor week)

**Obvious trades (operator, in window).**
- #2 S 101.14 Mon
- #3 L 100.845 Tue
- #4 S 101.19 Wed
- #5 L 100.975 Wed
- #6 S 101.235 Wed
- #7 S 100.975 Thu
- #8 L 100.615 Fri

#1 L 100.945 Mon is out: price was at 100.95 only at 03:00-05:00 UTC.

**E1.**
- 4H BoM supply 101.316-101.430: NOT REACHED (week high 101.275).
- UPPER RESISTANCE 101.199-101.262: REACTED (Wed 101.275, sharp sell-off; Mon high 101.145 at its sweep part).
- EQUILIBRIUM 100.985-101.077 (extent 100.942-101.153): REACTED (Wed low 100.946, Thu 101.07).
- 1H Mitigated MoM demand 100.825-100.851: REACTED (Mon 100.838, Tue 100.803).
- MID-RANGE SUPPORT 100.724-100.815: REACTED (Thu 100.786; Fri retests 100.727-100.75).
- GAP IN-FILL 100.599-100.659: REACTED (Fri 100.598, then 100.997).
- KEY SUPPORT 100.470-100.530: NOT REACHED.
- Turns with no zone: none.
- **E1 = 5/5 = 100%.**
- Qualifier FAIL. The EQUILIBRIUM extent is 21 of the week's 68 pips and price sat in it for 56 hours. Seven zones are stacked edge to edge from 100.47 to 101.43.

**E2.**
- Mon SS: RIGHT (range 100.84-101.15, inside the box).
- Tue SS: RIGHT.
- Wed SS+RWL+BS down: RIGHT (dip 100.98, spike 101.275 into UPPER RESISTANCE, sell-off).
- Thu BS down: RIGHT (101.07 to 100.786).
- Fri BS+WL+RWL down: RIGHT (flush 100.598, recovery 100.997).
- **E2 = 5/5 = 100%.**

**E3.**
- #2: CAUGHT by DX2 S 101.138, TP.
- #3: CAUGHT by DX3 L 100.851, TP.
- #4: CAUGHT by DX8 S 101.203, TP.
- #5: CAUGHT by DX9 L 100.980, TP.
- #6: CAUGHT by DX7 S 101.235, TP.
- #7: CAUGHT by DX10 S 100.980, TP.
- #8: CAUGHT by DX11 L 100.628, TP.
- STOPPED: DX5 (S 101.138, Tue).
- **E3 = 7/7 = 100%.**

**Presentation.**
- In `_all`, the setup labels sit on top of each other ("DX1 SS S 7.2R4 SS S 7.2R", "DX2 SS S 6.8R DX5 SS S 6.8R").
- The day tags run together ("Wed SS+RWL+BSThu BS").
- The zone labels in the history half cross the Jul 2-3 candles.

## EURUSD 2026-07-06 (anchor week)

**Obvious trades (operator, in window).**
- #2 L 1.14106 Mon
- #3 S 1.14441 Tue
- #4 L 1.14012 Wed
- #5 S 1.14277 Wed
- #6 L 1.13953 Wed
- #7 L 1.14233 Thu
- #8 S 1.14578 Fri

#1 S 1.14322 is out: that price was only available at 00:00-05:00 UTC.

**E1.**
- 1H BoM supply 1.14738-1.14807: NOT REACHED.
- Sweep supply 1.14678-1.14728: NOT REACHED.
- 1H Mitigated MoM supply (extent 1.14573-1.14728): REACTED (Fri 1.14608, then 1.1411).
- UPPER RESISTANCE (1.14444-1.14635): REACTED (Mon/Tue/Thu highs 1.1445-1.1449).
- 1H BoM supply 1.14316-1.14421: REACTED (Mon-Tue consolidation).
- GAP IN-FILL (1.14178-1.14339): REACTED (Wed high 1.14315).
- Liquidity band 1.14108-1.14178: REACTED (Mon/Tue lows 1.1408).
- MID-RANGE (1.13977-1.14147): REACTED.
- 4H BoM demand (top 1.13886): REACTED. Wed low 1.13911 stopped 2.5 pips in front of it.
- Turns with no zone: none.
- **E1 = 7/7 = 100%.**
- Qualifier FAIL (bunched). Nine zones are stacked contiguously from 1.1372 to 1.1487, so the whole frame is boxed.

**E2.**
- Mon SS: RIGHT.
- Tue SS: RIGHT.
- Wed SS+RWL+BS up: RIGHT (1.14315 down to 1.13911, then up).
- Thu BS up: RIGHT (to 1.14494).
- Fri BS+WL+RWL up: RIGHT (spike 1.14608, then 1.14114).
- **E2 = 5/5 = 100%.**

**E3.**
- #2: CAUGHT by EU4 L 1.14095.
- #3: CAUGHT by EU1 S 1.14442.
- #4: CAUGHT by EU9 L 1.14018.
- #5: CAUGHT by EU7 S 1.14269.
- #6: CAUGHT by EU8 L 1.13940.
- #7: CAUGHT by EU10 L 1.14239.
- #8: CAUGHT by EU11 S 1.14598 (2 pips from his entry).
- STOPPED: EU2 (S 1.14385, Mon) and EU6 (L 1.14095, Tue).
- Two Tue shorts were EMISSION_CAPPED.
- **E3 = 7/7 = 100%.**

**Presentation.**
- "EU1 SS S 5.7R" is printed over the 1H BoM label.
- The day tags run together.
- The option-strike labels sit over the Fri candles.

## GBPUSD 2026-07-06 (anchor week)

**Obvious trades (operator, all 7 in window).**
- #1 L 1.33331 Mon
- #2 S 1.33934 Mon
- #3 L 1.3333 Wed
- #4 L 1.33629 Wed (reinforcement)
- #5 S 1.34246 Thu
- #6 L 1.33829 Thu
- #7 S 1.34481 Fri

**E1.**
- RESISTANCE CEILING (1.34484-1.3463): REACTED (Fri 1.34517, -60 pips).
- Liquidity band 1.34386-1.34476: **PIERCED** (crossed up in one bar Thu 22:00 and back down; the reversal happened at the zone above).
- 4H BoM supply (1.34234-1.3434): REACTED (Thu 1.34308).
- 4H MoM supply (1.34029-1.34235): REACTED (Wed 1.34104).
- UPPER RESISTANCE (1.33933-1.34066): REACTED (Mon 1.33972, Tue 1.34015).
- GAP IN-FILL (1.33744-1.33846): REACTED (Thu 1.33799).
- UPPER RESISTANCE (1.33583-1.33805): REACTED.
- 1H MoM supply 1.33544-1.33582: REACTED (crossed Mon; 18-bar consolidation Tue-Wed).
- UPPER RESISTANCE (1.33406-1.33566): REACTED (Tue low 1.33487).
- Sweep demand 1.3334-1.33391: REACTED.
- MID-RANGE (1.33082-1.33333): REACTED (Mon 1.33286, Wed 1.33222).
- Two KEY SUPPORT zones and one sweep zone: NOT REACHED.
- Turns with no zone: none.
- **E1 = 10/11 = 91%.**
- Qualifier FAIL. Fourteen zones are stacked edge to edge from 1.3264 to 1.3463. The KEY SUPPORT extent is 29 pips.

**E2.**
- Mon SS: RIGHT (1.3329-1.3397, inside the box).
- Tue SS: RIGHT.
- Wed SS+RWL+BS up: RIGHT (1.33222, then 1.34104).
- Thu BS up: RIGHT (to 1.34308; close up).
- Fri BS+WL+RWL: RIGHT (spike 1.34517, then 1.3392).
- **E2 = 5/5 = 100%.**

**E3.**
- #1: CAUGHT by GB2 L 1.33333.
- #2: CAUGHT by GB1 S 1.33959.
- #3: CAUGHT by GB6 L 1.33255. Same turn and zone, but the entry is 7.5 pips from his.
- #4: MISSED (no reinforcement; the candidates were rejected on RRR).
- #5: CAUGHT by GB8 S 1.34254.
- #6: MISSED (GB9 L 1.33888 never filled).
- #7: MISSED (no short at 1.3448).
- STOPPED: none. GB5 was void.
- **E3 = 4/7 = 57%.**

**Presentation.**
- At 1.3345 in `_all`, "GB2 SS L 6.0R GB4 ..." is printed over the UPPER RESISTANCE label and cannot be read.
- "GB1 ... GB3" overlap.
- The day tags run together.

## DXY 2026-04-20

**Obvious trades (operator).**
- L 98.02 / SL 97.87 / TP 98.77 (Mon low 98.006)
- L 98.29 / SL 98.185 / TP 98.77 (Wed dip 98.21-98.24)

The other moves visible on 1H are noted but not counted, because the brief fixes this map's set: the Thu-Fri short 98.94 to 98.49, and the Mon short 98.40 to 98.01.

**E1.**
- UPPER RESISTANCE (98.884-99.031): REACTED (Thu 98.939, Fri 98.915).
- 1H MoM supply (98.667-98.868): REACTED (37-bar consolidation Wed-Fri).
- Liquidity band 98.561-98.625: REACTED (Tue 98.567).
- UPPER RESISTANCE 98.456-98.541: REACTED (Tue top; Fri low 98.489).
- 1H MoM supply (98.345-98.439): REACTED (Mon 98.395).
- Liquidity band 98.300-98.364: REACTED.
- GAP IN-FILL (98.182-98.311): REACTED (Wed low 98.21).
- MID-RANGE (98.014-98.145): REACTED (Mon 98.012).
- 1H MoM demand (97.92-98.055): REACTED (Mon 98.006).
- Two sweep zones and KEY SUPPORT: NOT REACHED.
- Turns with no zone: none.
- **E1 = 9/9 = 100%.**
- Qualifier FAIL (bunched). Twelve zones cover 97.53-99.03 almost without gaps.

**E2.**
- Mon SS: RIGHT (98.395 to 98.006, inside the box).
- Tue SS+RWL+BS up: RIGHT (to 98.567).
- Wed BS up: RIGHT (98.21 to 98.643).
- Thu BS+RWL up: RIGHT (98.939).
- Fri RWL down: RIGHT (98.915 to 98.489).
- **E2 = 5/5 = 100%.**

**E3.**
- L 98.02: CAUGHT by DX3 L 98.019 (TP 98.869 hit Thu; SL 97.939 held).
- L 98.29: CAUGHT by DX5 L 98.270 (TP 98.869).
- STOPPED: DX6 (L 98.660, Thu, stopped in one 15m bar).
- **E3 = 2/2 = 100%.**

**Presentation.**
- A post-week spike to 99.33 at the right edge stretches the price axis of `_week` and `_zones`.
- "DX2 SS... DX4 BS... 10.6R ... DX4 SS L 3.4R" are piled up at 98.07.
- "Thu BS+RWLFri RWL" overlap.

## EURUSD 2026-04-20

**Obvious trades (from `_zones`, before reading setups).**
1. L Mon 1.1750 (EQUILIBRIUM) to 1.1790 (UPPER RESISTANCE)
2. S Mon/Tue 1.1790 to 1.1724 (GAP IN-FILL)
3. L Tue/Wed 1.1724 to 1.1755 (EQUILIBRIUM)
4. S Wed 1.1755 to 1.1700 and on to 1.1670 Thu
5. L Thu/Fri 1.1670 (KEY SUPPORT) to 1.1722 (GAP IN-FILL)

**E1.**
- UPPER RESISTANCE (1.18125-1.18491): NOT REACHED.
- UPPER RESISTANCE (1.17847-1.1811): REACTED (Mon 1.17902).
- UPPER RESISTANCE (1.17668-1.17801): REACTED.
- Sweep supply 1.17575-1.17661: REACTED (Wed 1.17624).
- Sweep demand 1.17592-1.17642: REACTED.
- EQUILIBRIUM (1.17497-1.17655): REACTED.
- GAP IN-FILL (1.17327-1.17418): REACTED.
- Sweep demand 1.17277-1.17327: REACTED (Tue 1.17233).
- GAP IN-FILL (1.17126-1.17263): REACTED (Tue low; Fri high 1.1723).
- MID-RANGE (1.16809-1.17207): REACTED.
- Liquidity band 1.16876-1.16967: REACTED.
- GAP IN-FILL 1.16744-1.16804: REACTED.
- KEY SUPPORT (1.16543-1.16754): REACTED (Thu 1.16691).
- Turns with no zone: none.
- **E1 = 12/12 = 100%.**
- Qualifier FAIL. Thirteen zones are stacked from 1.1654 to 1.1849. Two zones are bloated: MID-RANGE extent 40 pips (1.16809-1.17207) and the top UPPER RESISTANCE at 37 pips. The two sweep zones of opposite sides overlap at 1.1758-1.1766.

**E2.**
- Mon SS: RIGHT (1.17475 to 1.17902, inside the box).
- Tue SS+RWL+BS down: RIGHT (1.1791 to 1.17187).
- Wed BS down: RIGHT (to 1.1703).
- Thu BS+RWL down: RIGHT (to 1.16691).
- Fri RWL up: RIGHT (to 1.1723).
- **E2 = 5/5 = 100%.**

**E3.**
- #1: MISSED (no long).
- #2: CAUGHT by EU3 S 1.17920 (TP 1.17512). EU4, from the same entry, also hit TP 1.17011.
- #3: MISSED.
- #4: MISSED. EU5 S 1.17656 never filled; the Wed high of 1.17624 stopped 3.2 pips short.
- #5: MISSED. EU2 L 1.17207 expired; the Thu RWL up setup was rejected on RRR.
- STOPPED: none.
- **E3 = 1/5 = 20%.**

**Presentation.**
- The "Mon SS" tag sits under the UPPER RESISTANCE label in `_all`.
- "Thu BS+RWLFri RWL" overlap.

## GBPUSD 2026-04-20

**Obvious trades.**
1. L Mon 1.3482 (MID-RANGE) to 1.3544
2. S Mon/Tue 1.3540 to 1.3477 (MID-RANGE)
3. L Tue 1.3477 to 1.3532 Wed (UPPER RESISTANCE)
4. S Wed/Thu 1.3518-1.3532 to 1.3448 (1H MoM demand)
5. L Fri 1.3450 to 1.3537

**E1.**
- UPPER RESISTANCE (1.3522-1.35332): REACTED.
- Sweep demand 1.35163-1.35213: REACTED (Thu 1.35182, then -69 pips).
- GAP IN-FILL (1.35036-1.35107): REACTED.
- UPPER RESISTANCE HEAVY (1.34932-1.35085): REACTED.
- MID-RANGE (1.34691-1.34846): REACTED (Mon 1.34818, Tue 1.34772).
- 1H MoM demand (1.34317-1.347): REACTED (week low 1.34476).
- Liquidity band, KEY SUPPORT and 1H BoM demand: NOT REACHED.
- **Turn with no zone:** the triple top at 1.3537-1.3544 (Mon 1.35444, Tue 1.35396, Fri 1.3537). It is 4-11 pips above the highest zone (1.35332). No zone is drawn above 1.35332.
- **E1 = 6/7 = 86%.**
- Qualifier FAIL. The week top has no zone, and the 1H MoM demand extent is bloated at 38 pips.

**E2.**
- Mon SS (box 1.34345-1.35019): **WRONG**. The day broke out to 1.35444 and closed at 1.35333, above the box.
- Tue SS+RWL+BS down: RIGHT (1.35396 to 1.34744).
- Wed BS down: **WRONG**. The range was 1.3490-1.3535 and the day closed flat; there was no decisive break.
- Thu BS+RWL down: RIGHT (to 1.34476).
- Fri RWL up: RIGHT (+85 pips).
- **E2 = 3/5 = 60%.**

**E3.**
- #1 to #5: all MISSED.
- GB1 L 1.3466 was never reached. GB3, GB4 and GB5 never filled. GB4 L 1.34083 sits 39 pips below the week low.
- STOPPED: GB2 (S 1.35163, SL 1.35243, stopped Mon 11:15; price then fell to 1.3448).
- **E3 = 0/5 = 0%.**

**Presentation.**
- The day tags sit inside and under the UPPER RESISTANCE label ("Tue SS+RWL+BS Wed BS" over the label text).
- "Thu BS+RWLFri RWL" overlap.
- The Thu/Fri setup boxes and the yellow path reach down to 1.3407, about 40 pips below any price of the week.

## DXY 2026-10-05

**Obvious trades.**
1. S Mon 102.43 to 102.08 (sweep supply 102.082)
2. S Tue 102.285 to 101.754 (KEY SUPPORT)
3. L Tue/Wed 101.80 to 102.499 (sweep supply 102.485)
4. S Wed 102.499 to 102.03 Thu / 101.92 Fri (MID-RANGE)
5. L Fri 101.92 to 102.335

**E1.**
- Sweep supply 102.485-102.535: REACTED (Wed 102.499; Thu 102.467 stopped 1.8 pips in front).
- Sweep supply 102.157-102.207: REACTED.
- Sweep supply 102.082-102.132: REACTED (Mon 102.084).
- MID-RANGE (101.916-102.051): REACTED (Thu 102.033, Fri 101.92).
- 1H MoM demand 101.855-101.926: REACTED.
- KEY SUPPORT (101.668-101.843): REACTED (Tue 101.754).
- Sweep demand 101.668-101.718: NOT REACHED.
- Turns with no zone: none.
- **E1 = 6/6 = 100%.**
- Qualifier FAIL (bunched). Two same-side sweep zones 2.5 pips apart (102.082-102.132 and 102.157-102.207) are drawn as separate boxes, against the brief's 5-pip merge rule.

**E2 (all five days SS, box 101.855-102.635).**
- Mon: RIGHT.
- Tue: **WRONG** (down to 101.754 with a 1H close through the floor; a BS down, which the tool itself flags as "closed through Tue 11:00").
- Wed: RIGHT (101.82 to 102.499, rejected at the ceiling).
- Thu: RIGHT.
- Fri: RIGHT.
- **E2 = 4/5 = 80%.**

**E3.**
- #1: MISSED.
- #2: MISSED.
- #3: MISSED. DX4 L 101.926 was stopped at 101.825 in 30 minutes, then price ran to 102.499. DX6, DX8 and DX10 were void after Tue 11:00.
- #4: CAUGHT by DX5 S 102.485 (TP 101.941, Fri).
- #5: MISSED (the longs were void).
- STOPPED: DX4.
- **E3 = 1/5 = 20%.**

**Presentation.**
- In `_week`, the Mon/Tue/Wed day tags are hidden under the OHLC header.
- The setup labels "DX1 SS S 3.0R" and "DX3 ..." collide in `_all`.

## EURUSD 2026-10-05

**Obvious trades.**
1. L Mon 1.1169 (sweep demand 1.1166) to 1.1225
2. L Tue 1.1203 to 1.1277 (1H BoM supply)
3. S Tue/Wed 1.1277 to 1.1165
4. L Wed/Thu 1.1165-1.1172 to 1.1243 Fri (UPPER RESISTANCE)
5. S Fri 1.1243 to 1.1187

**E1.**
- 1H BoM supply (1.12716-1.12866): REACTED (Tue 1.12767).
- GAP IN-FILL (1.12562-1.12671): REACTED.
- UPPER RESISTANCE (1.12451-1.12612): REACTED (Fri 1.12427 stopped 2.4 pips in front).
- Sweep demand 1.12208-1.12258: REACTED (Thu 1.12267).
- Sweep demand (1.12039-1.12199): REACTED (Tue 1.12028).
- Sweep demand 1.1161-1.1166: REACTED (Wed 1.11645).
- **Turn with no zone:** the Thu low of 1.11719, which led a 70-pip rally. No zone is drawn between 1.1166 and 1.12039.
- **E1 = 6/7 = 86%.**
- Qualifier FAIL. Nothing is drawn in the 1.1166-1.1204 gap, where price traded from Wed to Fri.

**E2 (all five days SS, box 1.1151-1.12612).**
- Mon: RIGHT.
- Tue: **WRONG** (surge to 1.12767, 15 pips above the ceiling with 1H closes through it).
- Wed: RIGHT.
- Thu: RIGHT.
- Fri: RIGHT.
- The yellow path is out of phase on Mon (it draws down; the candles went up).
- **E2 = 4/5 = 80%.**

**E3.**
- #1 to #5: all MISSED.
- EU6 L 1.1166 filled Wed and was still open at the week end; its TP of 1.12476 was missed by 5 pips.
- Every short after Tue 11:00 was void.
- STOPPED: EU3 (S 1.12491, SL 1.12642, stopped Tue 11:15; price then fell to 1.1165).
- **E3 = 0/5 = 0%.**

**Presentation.**
- The "Tue SS" tag is covered by the Tue candles in `_week`.
- "EU1 SS S 5.7R" and "EU3" collide.

## GBPUSD 2026-10-05

**Obvious trades.**
1. S Mon 1.3239 (1H BoM supply) to 1.3190
2. L Mon 1.3190 to 1.3224
3. L Tue 1.3201 (MID-RANGE) to 1.3285
4. S Tue/Wed 1.3285 to 1.3194
5. L Thu 1.3184 to 1.3248 (UPPER RESISTANCE)
6. S Fri 1.3250 to 1.3206
7. L Fri 1.3206 to 1.3244

**E1.**
- UPPER RESISTANCE (1.3245-1.32636): REACTED (Thu 1.32485, Fri 1.32503).
- 1H BoM supply (1.3227-1.32395): REACTED (Mon 1.3239).
- GAP IN-FILL (1.32121-1.32276): REACTED.
- MID-RANGE (1.31932-1.32071): REACTED (Tue 1.32013, then +76 pips).
- Sweep demand 1.31899-1.31949: REACTED.
- Sweep demand 1.31806-1.31864: REACTED (Thu 1.31843).
- **Turn with no zone:** the Tue high of 1.32856 (the week high, start of a 91-pip drop). It is 18 pips beyond the top zone extent (1.32636) and beyond its sweep reach (1.3268).
- **E1 = 6/7 = 86%.**
- Qualifier FAIL (week high missing).

**E2 (all five days SS, box 1.31799-1.32395).**
- Mon: RIGHT.
- Tue: **WRONG** (breakout to 1.32856, closes far above the ceiling).
- Wed: **WRONG** (opened above the box at 1.3265 and fell 80 pips back through it, a BS down).
- Thu: RIGHT (high 1.32485, 9 pips over).
- Fri: **WRONG** (high 1.32503, 10.8 pips over, with 1H closes above 1.32395 up to 1.32456).
- **E2 = 2/5 = 40%.**

**E3.**
- #1: CAUGHT by GB1 S 1.32319 (TP 1.31915).
- #2: CAUGHT by GB2 L 1.31924 (TP 1.32333).
- #3: MISSED (GB4 never filled).
- #4: MISSED.
- #5: CAUGHT by GB6 L 1.31924 (TP Thu).
- #6: MISSED (shorts void).
- #7: MISSED.
- STOPPED: GB3 (S 1.32319, stopped Tue 08:30 by the breakout).
- **E3 = 3/7 = 43%.**

**Presentation.**
- At 1.3200, "GB2 ... GB4 ... sweep zone 4H liquidity" is printed over the MID-RANGE label and cannot be read.
- The Tue tag is covered by candles.

## DXY 2026-05-18

**Obvious trades.**
1. S Mon 99.30 to 98.95 (MID-RANGE)
2. L Mon/Tue 98.95 to 99.43 (sweep supply)
3. S Tue/Wed 99.43-99.47 to 99.05 (MID-RANGE)
4. L Wed/Thu 99.05 to 99.515 (liquidity band)
5. S Thu 99.515 to 99.10

**E1.**
- Liquidity band 99.449-99.503: REACTED (Wed 99.472, Thu 99.515).
- Sweep supply 99.359-99.413: REACTED (Tue 99.434, Fri 99.412).
- 1H MoM demand (99.251-99.32): REACTED. It was crossed in one bar at the Mon anchor, but held a consolidation on Tue-Wed.
- 1H MoM demand (99.125-99.298): REACTED.
- MID-RANGE (98.963-99.097): REACTED (Mon 98.944, Wed 99.053, Thu 99.098).
- 1H MoM demand 98.844-98.939: NOT REACHED.
- Turns with no zone: none.
- **E1 = 5/5 = 100%.**
- Qualifier FAIL (bunched). Four zones lie inside 99.125-99.413, and one of them carries a demand-side and a supply-side sweep part at once.

**E2 (all five days SS, box 98.963-99.509).**
- Mon: RIGHT.
- Tue: RIGHT.
- Wed: RIGHT.
- Thu: RIGHT (99.515, 0.6 over).
- Fri: RIGHT.
- **E2 = 5/5 = 100%.**

**E3.**
- #1: MISSED (DX1 never filled).
- #2: MISSED. DX2 L 99.050 was stopped at 98.971 by the 98.944 low, then price rallied to 99.43. DX4, DX6, DX8 and DX10 were void after Mon 20:00.
- #3: CAUGHT by DX3 S 99.409 (TP 99.052, Wed).
- #4: MISSED (longs void).
- #5: MISSED. DX7 S 99.409 filled Thu but was still open at the week end; Thu low 99.098 missed its TP.
- STOPPED: DX2.
- **E3 = 1/5 = 20%.**

**Presentation.**
- In `_week`, the Mon/Tue/Wed tags are hidden under the OHLC header.
- "DX1 SS S 2.8R" and "DX3" collide in `_all`.

## EURUSD 2026-05-18

**Obvious trades.**
1. L Mon 1.1622 (EQUILIBRIUM) to 1.1661 (UPPER RESISTANCE)
2. S Mon/Tue 1.1661 to 1.1595 (MID-RANGE)
3. L Wed 1.1583 to 1.1636
4. S Thu 1.1635 to 1.1576
5. L Thu 1.1576 to 1.1630
6. S Fri 1.1620 to 1.1588

**E1.**
- UPPER RESISTANCE (1.16604-1.16773): REACTED (Mon 1.16617).
- UPPER RESISTANCE HEAVY (1.16456-1.16574): REACTED.
- Liquidity band 1.16327-1.16395: REACTED (Wed 1.16357, Thu 1.16353).
- EQUILIBRIUM (1.16203-1.16356): REACTED.
- Sweep demand 1.16168-1.16218: REACTED.
- Sweep demand (1.16083-1.16162): REACTED.
- MID-RANGE 1.1597-1.16036: REACTED (Tue 1.15948).
- Liquidity band 1.15747-1.15815: REACTED (Wed 1.15827, Thu 1.15762).
- Two liquidity bands: NOT REACHED.
- Turns with no zone: none.
- **E1 = 8/8 = 100%.**
- Qualifier FAIL (bunched). Four zones lie inside 1.16083-1.16395, and the two option-strike labels overlap.

**E2 (all five days SS, box 1.1597-1.16562).**
- Mon: RIGHT.
- Tue: RIGHT.
- Wed: **WRONG** (low 1.15827, 14 pips under the floor, with 1H closes under it).
- Thu: **WRONG** (low 1.15762, 21 pips under, with closes under).
- Fri: RIGHT.
- **E2 = 3/5 = 60%.**

**E3.**
- #1 to #6: all MISSED.
- Every setup of the week is a SHORT. There is no long order at any bound on a map forecast as a 5-day range.
- EU4 to EU10 were void after Mon.
- STOPPED: EU1 (S 1.16512, SL 1.16575; the high of 1.16617 stopped it, then price fell to 1.1595, past its TP of 1.15985), EU2 (S 1.16297, stopped Mon 07:15) and EU3 (S 1.16512, stopped Mon 21:45).
- **E3 = 0/6 = 0%.**

**Presentation.**
- The "Mon SS" tag is over candles.
- The "3.7bn" and "1.5bn" option labels sit on top of each other.
- The "4.1bn" label is over candles.

## GBPUSD 2026-05-18

**Obvious trades.**
1. L Mon 1.3322 to 1.3449 (127 pips)
2. S Mon/Tue 1.3449 to 1.3379
3. L Wed 1.3375 to 1.3463
4. S Thu 1.3455 to 1.3396
5. L Thu 1.3396 to 1.3448
6. L Fri 1.3417 to 1.3451
7. S Fri 1.3451 to 1.3420

**E1.**
- UPPER RESISTANCE (1.34423-1.34557): REACTED.
- GAP IN-FILL (1.34222-1.34339): REACTED.
- UPPER RESISTANCE (1.33941-1.34037): REACTED (support Tue-Wed).
- Liquidity band 1.33816-1.33933: REACTED.
- GAP IN-FILL 1.3372-1.3378: REACTED (Wed 1.3375).
- GAP IN-FILL (1.33492-1.33644): REACTED (Mon retest 1.33465).
- GAP IN-FILL (1.33203-1.33381): REACTED (Mon anchor low 1.33217).
- Five zones below 1.3320: NOT REACHED (they float 10-80 pips under the week).
- **Turn with no zone:** the double top at 1.3463 (Wed 1.3463, Fri 1.34631), 7.4 pips above the top zone (1.34557).
- **E1 = 7/8 = 88%.**
- Qualifier FAIL. The top is missing, and five unreached zones fill the bottom third of the frame.

**E2 (all five days SS, box 1.33047-1.34037).**
- Mon: **WRONG** (BS up to 1.34494).
- Tue: **WRONG** (1.34371 to 1.33785, above the ceiling with closes above).
- Wed: **WRONG** (high 1.3463).
- Thu: **WRONG** (traded 1.33904-1.34548).
- Fri: **WRONG** (the whole day, 1.34132-1.34631, above the box).
- In `_week`, the yellow zigzag runs 1.3320-1.3395 while the candles trade 1.338-1.346 from Tuesday on.
- **E2 = 0/5 = 0%.**

**E3.**
- #1: CAUGHT by GB2 L 1.33197 (TP 1.33926).
- #2 to #7: MISSED. GB3, GB5, GB7 and GB9 were void after Mon 15:00. GB4, GB6, GB8 and GB10 L 1.33197 never filled, because price never came back.
- STOPPED: GB1 (S 1.33983, stopped Mon 15:30 by the breakout).
- **E3 = 1/7 = 14%.**

**Presentation.**
- The day tags are covered by candles.
- At 1.3330, "GB2 SS L 4.0R GB4 ..." collide.

---

## Table (12 maps)

| map | E1 % | E2 % | E3 % | E1 qualifier |
|---|---|---|---|---|
| DXY 2026-07-06 | 100 (5/5) | 100 (5/5) | 100 (7/7) | FAIL bunched/bloated |
| EURUSD 2026-07-06 | 100 (7/7) | 100 (5/5) | 100 (7/7) | FAIL bunched |
| GBPUSD 2026-07-06 | 91 (10/11) | 100 (5/5) | 57 (4/7) | FAIL bunched |
| DXY 2026-04-20 | 100 (9/9) | 100 (5/5) | 100 (2/2) | FAIL bunched |
| EURUSD 2026-04-20 | 100 (12/12) | 100 (5/5) | 20 (1/5) | FAIL bunched/bloated |
| GBPUSD 2026-04-20 | 86 (6/7) | 60 (3/5) | 0 (0/5) | FAIL missing top / bloated |
| DXY 2026-10-05 | 100 (6/6) | 80 (4/5) | 20 (1/5) | FAIL bunched |
| EURUSD 2026-10-05 | 86 (6/7) | 80 (4/5) | 0 (0/5) | FAIL missing |
| GBPUSD 2026-10-05 | 86 (6/7) | 40 (2/5) | 43 (3/7) | FAIL missing top |
| DXY 2026-05-18 | 100 (5/5) | 100 (5/5) | 20 (1/5) | FAIL bunched |
| EURUSD 2026-05-18 | 100 (8/8) | 60 (3/5) | 0 (0/6) | FAIL bunched |
| GBPUSD 2026-05-18 | 88 (7/8) | 0 (0/5) | 14 (1/7) | FAIL missing top / floating |
| **All 12 (pooled)** | **94.6 (87/92)** | **76.7 (46/60)** | **39.7 (27/68)** | 0/12 pass |
| **9 maps outside 2026-07-06** | **94.2 (65/69)** | **68.9 (31/45)** | **19.1 (9/47)** | 0/9 pass |

The anchor week scores 18/21 on E3 (86%). The other nine maps score 9/47 (19%).

The E1 % is high on every map because the zones are stacked edge to edge across nearly the whole weekly range, so almost any turn lands "in" a zone. No map passes the G1 qualifier "none bloated, bunched, floating or missing".

## The five defects that cost the most

1. **E3 orders go void for the rest of the week after one 1H close through the anchor zone (E3C:150), and nothing replaces them.**
   - EURUSD 05-18: EU4-EU10 void from Mon; the week has only shorts and no long at any bound.
   - GBPUSD 05-18: GB3/5/7/9 void after Mon 15:00.
   - DXY 10-05: DX6/8/10 void after Tue 11:00.
   - EURUSD 10-05 and GBPUSD 10-05: every short void after Tue.
   - DXY 05-18: every long void after Mon 20:00.
   - Most of the 38 missed trades outside 07-06 come from this.

2. **E2 holds one static SS range box for all five days and never switches to its breakout branch when price leaves the box.**
   - GBPUSD 05-18: box 1.33047-1.34037 while price traded 1.3375-1.3463 from Monday (E2 0/5).
   - GBPUSD 10-05: Tue breakout to 1.32856, then Wed and Fri also wrong.
   - EURUSD 05-18: Wed 1.15827 and Thu 1.15762 under the floor.
   - Also wrong: EURUSD 10-05 Tue (1.12767), DXY 10-05 Tue (101.754), and GBPUSD 04-20 Mon (SS while price broke out to 1.35444).

3. **The highest and lowest turns of the week have no zone and no setup.**
   - GBPUSD 04-20: triple top 1.3537-1.3544 (Mon/Tue/Fri); nothing is drawn above 1.35332.
   - GBPUSD 05-18: double top 1.3463 (Wed/Fri), above 1.34557.
   - GBPUSD 10-05: Tue high 1.32856, 18 pips above the highest box.
   - EURUSD 10-05: Thu low 1.11719, in an empty 1.1166-1.1204 gap.
   - The largest moves of those weeks (91, 88 and 70 pips) start there and are all missed.

4. **Stops sit inside the normal sweep of the zone, so the right trade is stopped and price then runs to the target.**
   - EURUSD 05-18 EU1 S 1.16512 / SL 1.16575: Mon high 1.16617, then 1.1595 on Tue.
   - DXY 05-18 DX2 L 99.050 / SL 98.971: Mon low 98.944, then 99.43.
   - DXY 10-05 DX4 L 101.926 / SL 101.825: Tue low 101.754, then 102.499.
   - EURUSD 10-05 EU3 S 1.12491 / SL 1.12642: Tue high 1.12767, then 1.1165.
   - GBPUSD 04-20 GB2 S 1.35163 / SL 1.35243: Mon high 1.35444, then 1.3448.

5. **E1 boxes cover the whole chart, so the E1 % says little.**
   - Stacking: EURUSD 04-20 has 13 zones from 1.1654 to 1.1849; GBPUSD 07-06 has 14 zones from 1.3264 to 1.3463.
   - Bloated extents: EURUSD 04-20 MID-RANGE 1.16809-1.17207 (40 pips), GBPUSD 04-20 1H MoM demand 1.34317-1.347 (38 pips), DXY 07-06 EQUILIBRIUM 100.942-101.153 (31% of the week range).
   - Merge rule not applied: DXY 10-05 same-side sweep zones 102.082-102.132 and 102.157-102.207 are 2.5 pips apart and still drawn as two boxes.
   - Clutter that hides candles: overlapping labels on most maps ("Wed SS+RWL+BSThu BS", "Thu BS+RWLFri RWL", "DX1 SS S 7.2R4 SS S 7.2R"), and day tags hidden under the OHLC header in the DXY 10-05 and DXY 05-18 `_week` frames.
   - The DXY 04-20 `_week` price axis is stretched by a post-week spike to 99.33.
