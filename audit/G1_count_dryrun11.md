# G1 count 11 — outside reviewer (fresh; no earlier count, memory/ or tool code read)

Sources used: `audit/G1_brief11.md`; the 36 frames in `evidence/s3k/` (all present and readable; every one opened); the 12 facts files in `audit/g1_facts_k/` (all present and readable); `context_management/oracle/golden_week.json` (operator trades, 2026-07-06 only); 1H closes/highs/lows read-only through `e1_tool/e1_data.bars(pair,'60')` to check times and turning prices. Facts-file times are UTC (checked against the bars: e.g. DXY 07-06 DX6 fill "Wed 07:15" = 1H bar Wed 07:00 UTC low 100.950). Anchor = Monday 06:00 UTC (02:00 New York, EDT in all four weeks).

## Counting rules applied (so anyone can recount)

- **Pip**: 0.0001 for EURUSD/GBPUSD, 0.01 for DXY (brief: "levels within 0.05" = 5 pips).
- **E1** = zones REACTED / (zones REACHED + obvious turning points of the week with no Engine 1 object). One verdict per labelled zone (parts belong to their zone; a turn at a part is a turn at its zone). Discovery lines get their own verdict if reached. REACTED = sharp rejection or consolidation in / around it at least once during the forecast week (Mon 06:00 UTC to Fri close); PIERCED = crossed with no reaction at any touch; NOT REACHED = price never inside the zone's full extent. A turning point counts as "at a zone" if it lies inside or within about 5 pips of the zone's full extent (the legend's own join distance), or inside a drawn sweep reach.
- **E1 side condition** (PASS / FAIL): *bloated* = labelled box taller than the operator's reference (> ~35 pips) or "40 pips with 200 candles inside"; *bunched* = (a) two LABELLED boxes 0-2 pips apart / overlapping crossed together by one 1H candle, (b) the same with full extents including parts (a wick crossing both counts); *floating* = an Engine 1 object whose near edge lies more than 22 pips (the reference map's maximum) beyond the week's high / low; *missing* = an obvious turning point with no Engine 1 object. Any of these = FAIL. Where a FAIL rests only on a zone the legend itself puts there (alternative-chain target, discovery line), I say so.
- **E2** = days RIGHT / 5. For 2026-07-06 the operator's day tags are the truth (DXY Mon SS+BS, Tue SS, Wed SS+RWL+BS, Thu ladder short = breakout down continuing, Fri WL+RWL; pairs mirrored). Read literally, "carries his shapes" means all of them: a forecast that lacks one of his shapes is WRONG (this costs Monday on all three 07-06 maps; the lenient count is given too). Other weeks: shape + direction + key zone vs the day's candles. For an SS (range) day the day's candles must stay inside the forecast range box (sweep reach included, ~5 pips tolerance); a day that breaks out of the box and holds, or trades a range outside it, is WRONG.
- **E3** = obvious trades CAUGHT / obvious trades. 07-06: operator trades in the window (DXY trade 1 at 100.945 was only available Mon 00:00-04:00 UTC, before the anchor: excluded; EURUSD trade 1 at 1.14322 only before 06:00: excluded; GBPUSD trade 1 1.33331 was available after 06:00 (low 1.33286 at 06:00-08:00): included). DXY 04-20: the operator's two trades. Other weeks: clean zone-to-zone moves on the 1H chart, listed from the `_zones` frame BEFORE any setup was looked at. CAUGHT = a setup of the same direction at that zone (same turn) that filled and reached its TP before its SL. A position that rode through two of my listed legs catches only the leg whose zone it was entered at. Stopped setups are named; a stopped setup is a loss even if price later reached TP.

---

## 1. DXY 2026-07-06 (anchor week)

**Obvious trades (operator, in window)**: T2 Mon SHORT 101.14→100.845; T3 Tue LONG 100.845→101.19; T4 Wed SHORT 101.19→100.975; T5 Wed LONG 100.975→101.24; T6 Wed SHORT 101.235→100.68; T7 Thu ladder SHORT 100.975; T8 Fri LONG 100.615→100.94. (T1 Mon LONG 100.945 = pre-anchor, excluded.) = 7.

**E1** (6 zones):
- 4H BoM Supply 101.316-101.430: NOT REACHED (week high 101.275).
- UPPER RESISTANCE 101.199-101.262 (+LQ to 101.305, LSZ 101.152): REACTED (Wed 00:00 101.215 and Wed 14:00 101.275 both rejected to ~100.95).
- EQUILIBRIUM 100.985-101.077 (parts 100.942-101.153): REACTED (Mon high 101.145 in its 1H-supply part; Wed 07:00 low 100.950 and Wed 18:00 100.946 bounced).
- MID-RANGE SUPPORT 100.724-100.815 (parts 100.654-100.876): REACTED (Mon low 100.838, Tue 100.803, Thu 100.786 all bounced).
- GAP IN-FILL 100.599-100.659: REACTED (Fri 02:00 low 100.598 → 100.997).
- KEY SUPPORT BAND 100.470-100.530: NOT REACHED.
- Turning points with no zone: none.
- **E1 = 4/4 = 100%**. Side: no bloated (largest labelled 9 pips; full EQ 21), (a) no labelled boxes within 2 pips (closest 4H supply / UR 5.4); (b) full extents near-contiguous (UR-full 101.152 / EQ-full 101.153; MRS-full 100.654 / GAP 100.659) but no candle crossed two together (Fri 02:00 candle went 100.742→100.598 and turned inside the gap). Floating: none (KSB 6.8 below low, 4H supply 4.1 above high). **PASS / PASS**.

**E2**: Mon SS vs his SS+BS — WRONG (literal: lacks his BS; candles did the range swing 100.87→101.145→100.84); Tue SS — RIGHT; Wed SS+RWL+BS down — RIGHT; Thu BS down vs ladder short — RIGHT; Fri BS+WL+RWL down vs WL+RWL — RIGHT (carries both). **E2 = 4/5 = 80%** (lenient 5/5).

**E3**: T2 CAUGHT (DX2 101.138, TP 100.830 Tue 01:30); T3 CAUGHT (DX3 100.851 filled Mon 18:30 at the same Mon-Tue base, TP 101.184 Tue 23:45); T4 CAUGHT (DX5 101.203 → TP 100.995); T5 CAUGHT (DX6 100.980 → 101.235); T6 CAUGHT (DX4 101.235, SL 101.322 above the 101.275 high, TP 100.685 Fri 02:00); T7 CAUGHT (DX7 100.980 → 100.685); T8 CAUGHT (DX8 100.628 → 100.940). **E3 = 7/7 = 100%**. Stopped: **DX2.Tue** (filled Tue 19:15, stopped Tue 23:45). Note: DX3.Tue filled Mon 21:00 while DX3 was already open (same order filled twice).

Presentation: setup labels sit on Monday-Tuesday candles (DX1/DX2/DX3 labels over bodies); ALT labels (DXA4, DXA6) over candles; DXA7 label cut at the right edge; zone boxes + parts cover 100.47-101.43 wall-to-wall.

## 2. EURUSD 2026-07-06 (anchor week)

**Obvious trades (operator, in window)**: T2 Mon LONG 1.14106→1.14442; T3 Tue SHORT 1.14441→1.14004; T4 Wed LONG 1.14012→1.14276; T5 Wed SHORT 1.14277→1.1395; T6 Wed LONG 1.13953→1.14544; T7 Thu LONG 1.14233→1.14544; T8 Fri SHORT 1.14578→1.14205. (T1 Mon SHORT 1.14322: price there only Mon 00:00-04:00, excluded.) = 7.

**E1** (6 zones): 1H BoM Supply 1.14738-1.14807 NOT REACHED (high 1.14608); 1H MoM Supply 1.14601-1.14677 REACTED (Fri 02:00 1.14608 → 1.14117); UPPER RESISTANCE 1.14444-1.14533 REACTED (Mon/Tue 1.1448 and Thu 1.14494 rejected); GAP 1.14220-1.14280 REACTED (week-long consolidation, Wed 06:00 1.14315 rejected at its LSZ part); MID-RANGE SUPPORT 1.13977-1.14053 REACTED (Tue 22:00-Wed 00:00 1.13983-1.14001, Wed 14:00 sweep to 1.13911 then rally); 4H BoM Demand 1.13721-1.13832 NOT REACHED. Missing turning points: none. **E1 = 4/4 = 100%**. Side: (a) closest labelled gap 6 pips; (b) full extents overlap (1.14573-1.14635, 1.14316-1.14339, 1.14108-1.14147) — no pair crossed together; floating none. **PASS / PASS**. (Visual: 17 parts make the whole 1.1372-1.1484 band a solid wall of outlines.)

**E2**: same tags as DXY mirrored: Mon WRONG (lacks BS), Tue-Fri RIGHT. **E2 = 4/5 = 80%** (lenient 5/5).

**E3**: T2 CAUGHT (EU4 1.14095 → 1.14429); T3 CAUGHT (EU1 1.14442, SL 1.14508 above 1.1448, TP 1.14068); T4 CAUGHT (EU7 1.14018 → 1.14254); T5 CAUGHT (EU5 1.14269 → 1.13940); T6 CAUGHT (EU6 1.13940, SL 1.13872 below 1.13911, TP 1.14555); T7 CAUGHT (EU8 1.14239 → 1.14555); T8 CAUGHT (EU9 1.14598 → 1.14239). **E3 = 7/7 = 100%**. Stopped: **EU2** (Mon 17:15 → Mon 21:45), **EU4.Tue** (Tue 19:15 → Tue 21:30). EU1.Tue filled Mon 21:00 while EU1 was open (double fill).

Presentation: EU1/EU1.Tue/EU2/EU3.Tue labels stacked on Monday-Tuesday candles; EUA5/EUA7/EUA8 ALT labels run across candles; EUA9 cut at the edge.

## 3. GBPUSD 2026-07-06 (anchor week)

**Obvious trades (operator, in window)**: T1 Mon LONG 1.33331→1.33941; T2 Mon SHORT 1.33934→1.33347; T3 Wed LONG 1.3333→1.34246; T4 Wed LONG 1.33629→1.34246 (reinforcement); T5 Thu SHORT 1.34246→1.33882; T6 Thu LONG 1.33829→1.34485; T7 Fri SHORT 1.34481→1.34021. = 7.

**E1** (8 zones): RESISTANCE CEILING 1.34484-1.34548 REACTED (Fri 02:00 1.34517 → 1.339); 4H BoM Supply 1.34264-1.34340 REACTED (Thu 06:00 1.34308 → 1.33845; Fri consolidation 1.342-1.344); UPPER RESISTANCE 1.33933-1.34005 REACTED (Mon 22:00-Tue 00:00 1.34013-1.34015 → 1.3322; Wed 16:00 1.34104 rejected); UPPER RESISTANCE 1.33643-1.33717 REACTED (Tue 12-18 consolidation, Wed 12:00 1.33779 rejected, Thu low 1.33807 at its LSZ part); UPPER RESISTANCE 1.33435-1.33521 REACTED (Tue 20:00-Wed 04:00 lows 1.33422-1.33451 held); MID-RANGE SUPPORT 1.33225-1.33285 REACTED (Mon 1.33286, Wed 1.33222 both bounced); KEY SUPPORT BAND 1.32970-1.33046 NOT REACHED; KEY SUPPORT BAND 1.32789-1.32877 NOT REACHED. Missing: none (Fri low 1.33918 is 1.5 pips under UR 1.33933). **E1 = 6/6 = 100%**.
Side: bloated none; (a) PASS (closest labelled 9.3 pips); (b) full extents touch (UR 1.33340-1.33582 / 1.33583-1.33846; 4H-full / UR-full overlap 1.34145-1.34162) but no candle crossed two together (Wed 08:00 1.33702→1.33375 stopped inside the lower one). Floating: **KEY SUPPORT BAND 1.32789-1.32877 is 34.5 pips below the week low 1.33222** (it is the zone at the alternative chain's target 1.32737, which the legend says is drawn at any distance). **FAIL** (PASS if the alternative-target zone is exempted).

**E2**: Mon WRONG (lacks BS), Tue-Fri RIGHT by the operator's tags (note: the Wed box 1.33155-1.33496 did not contain Wed's 1.34104 high). **E2 = 4/5 = 80%** (lenient 5/5).

**E3**: T1 CAUGHT (GB2 1.33333 → 1.33926); T2 CAUGHT (GB1 1.33959, SL 1.34062 above 1.34015, TP 1.33348 Wed 09:00); T3 CAUGHT (GB4 1.33255 at the same MRS turn → 1.34254); T4 MISSED (no long at 1.336; reinforcement 1.33813 rejected); T5 CAUGHT (GB6 1.34254 → 1.33888); T6 MISSED (GB7 1.33888 is Friday-only; Thu low 1.33807 untouched by any active order; GB5 1.33473 never reached); T7 MISSED (no short at the 1.3448-1.3452 ceiling). **E3 = 4/7 = 57.1%**. Stopped: none (GB3 void).

Presentation: GBA3 / GBA5 / GBA6 / GBA7 ALT labels across candles; "GB4 BS L 7.7R" and "GB5 Ladder" over Wednesday candles; the Fri day tag sits over the Friday high candles.

## 4. DXY 2026-04-20

**Obvious trades (operator's two, per brief S3)**: O1 LONG 98.02 / 97.87 / 98.77 (Mon-Tue base); O2 LONG 98.29 / 98.185 / 98.77 (Wed dip). (Visible from the `_zones` frame also: Mon down 98.39→98.01, Tue up 98.12→98.57, Wed up 98.21→98.64, Thu spike 98.94, Fri down 98.92→98.49 — not used as denominator.)

**E1** (7 zones): UPPER RESISTANCE 98.939-99.005 REACTED (Thu 17:00 98.939 → 98.688; Fri 98.915 → 98.489); 1H MoM Supply 98.675-98.845 REACTED (Thu-Fri consolidation in it); UPPER RESISTANCE 98.456-98.541 REACTED (Tue 98.567 rejected to 98.311; Wed-Thu consolidation; Fri lows 98.489-98.517 held); GAP 98.271-98.331 REACTED (Tue 08:00 98.309 rejected; Wed low 98.211 in its LQ part bounced); MID-RANGE SUPPORT 98.058-98.145 REACTED (Mon low 98.006 in its parts, 12 h consolidation, then rally); liquidity band 97.920-97.984 NOT REACHED (2.2 pips); KEY SUPPORT BAND 97.725-97.799 NOT REACHED. Missing: none. **E1 = 5/5 = 100%**.
Side: bloated none (largest labelled 17 pips; KSB full 97.576-97.883 = 31); (a) PASS (closest 7.4); (b) PASS (UR-full / 1H-full 1.6 pips apart but the Thu 17:00 candle 98.653→98.939 turned inside UR); floating none (KSB 20.7 below low). **PASS / PASS**. Defect: the stand-alone liquidity band 97.920-97.984 is drawn without a label (legend says a stand-alone band is not drawn by this script).

**E2**: Mon SS (range 97.869-98.539) — RIGHT (swing from the gap to the floor 98.006, held, all inside the box); Tue SS+RWL+BS up — RIGHT (range, dip 98.123, surge through the gap / UR to 98.567, close up); Wed BS up — RIGHT (through UR 98.54, close 98.616); Thu BS+RWL up — RIGHT (dip 98.534 then 98.939 spike, close up); Fri RWL down — RIGHT (98.915 spike rejected, close 98.510). **E2 = 5/5 = 100%**.

**E3**: O1 CAUGHT (DX2 LONG 98.029, SL 97.839, filled Mon 15:30, TP 98.874 Thu 17:30); O2 CAUGHT (DX3 LONG 98.270, filled Wed 05:15, SL 98.104 below the 98.211 low, TP 98.874). **E3 = 2/2 = 100%**. Stopped: **DX1** SHORT 98.300 (Tue 08:00 → Tue 16:30), **DX5** LONG 98.660 (Thu 00:00 → Thu 00:15). (DX4 SHORT 98.874 → 98.510 also won — extra.)

Presentation: "DX1 RWL S 3.8R" and "DX2 BS L 4.5R" over Monday-Tuesday candles; "DX3 Ladder ... if DX2" over the 1.4bn option-strike label; DXA1 ALT label across the lower boxes.

## 5. EURUSD 2026-04-20

**Obvious trades (from `_zones`, before setups)**: T1 Mon LONG 1.1748 (EQ) → 1.1790 (UR 1.1799 part); T2 Mon-Tue SHORT 1.1790 → 1.1719 (gap 1.1720); T3 Tue-Wed LONG 1.1719 → 1.1762 (EQ part); T4 Wed SHORT 1.1762 → 1.1703 (MRS); T5 Thu SHORT 1.1716 (gap part) → 1.1669 (KSB part); T6 Fri LONG 1.1673 → 1.1723 (gap). = 6.

**E1** (9 zones): UR 1.18213-1.18292 NOT REACHED (high 1.1791); UR 1.17988-1.18067 REACTED (Mon 14:00-22:00 1.17895-1.1791 in its 1H-supply part, then 70-pip fall); UR 1.17706-1.17791 REACTED (Tue 00-06 held 1.1773-1.1782, then broke); EQUILIBRIUM 1.17497-1.17573 REACTED (Mon 1.1747 low, Tue 1.1754-1.1757 lows, Wed 04:00 1.17624 rejected); GAP 1.17365-1.17425 REACTED (Tue 22-Wed 02 lows 1.17372-1.17386); GAP 1.17203-1.17263 REACTED (Tue 1.17187-1.17201 lows; Thu 1.17165 rejected); MRS 1.16973-1.17033 REACTED (Wed-Thu consolidation); GAP 1.16744-1.16804 REACTED (Thu 1.16789, Fri 1.16729 bounced); KSB 1.16570-1.16638 REACTED (Thu 17:00 low 1.16691 in its 1H-demand part). Missing: none. **E1 = 8/8 = 100%**.
Side: bloated none (UR's 1H BoM part 1.18239-1.18491 is 25 pips); (a) PASS (closest 7.2); (b) **bunched: MRS-full 1.16809-1.17207 and GAP 1.16744-1.16804 (0.5 pip apart) crossed together by the Thu 17:00 wick 1.17027→1.16691**; floating: **UR 1.18213-1.18292 30 pips above the week high 1.1791, its part reaching 1.18491 (58 pips)**. **FAIL** ((a) reading: FAIL on floating alone).

**E2**: Mon SS — RIGHT (EQ→ceiling swing inside 1.17004-1.17988); Tue SS+RWL+BS down — RIGHT (range then breakdown through EQ to 1.17187); Wed BS down — RIGHT (1.17624 → 1.1703 close 1.17045); Thu BS+RWL down — RIGHT (spike 1.17165 rejected, low 1.16691, close down); Fri RWL up — RIGHT (1.16729 → 1.1723 sharp reversal, key 1H MoM zone reached). **E2 = 5/5 = 100%**.

**E3**: T1 MISSED (no long); T2 CAUGHT (EU2 SHORT 1.17920 filled Mon 23:00, SL 1.17996, TP 1.17006 Thu 00:00); T3 MISSED (no long); T4 MISSED (EU3 SHORT 1.17656 never filled — high 1.17624, 3 pips short); T5 MISSED (EU5 1.17372 never reached); T6 MISSED (no Friday long). **E3 = 1/6 = 16.7%**. Stopped: **EU4** LONG 1.17006 (Thu 00:00 → Thu 17:30).

Presentation: "EU3 Ladder S 12.3R if EU2" overprinted on the 1.1bn option-strike label (illegible); EU1/EU2 labels on Monday candles; a red 1H BoM part box 1.1785-1.1849 dominates the top of the chart above where the week trades.

## 6. GBPUSD 2026-04-20

**Obvious trades (from `_zones`, before setups)**: T1 Mon LONG 1.3482 (MRS) → 1.3544 (above UR); T2 Tue SHORT 1.3540 → 1.3474 (MRS); T3 Tue-Wed LONG 1.3474 → 1.3535 (UR); T4 Wed SHORT 1.3535 → 1.3492 (UR2); T5 Thu SHORT 1.3518 (UR part) → 1.3448 (1H demand); T6 Fri LONG 1.3453 → 1.3537 (UR). = 6.

**E1** (6 zones + 1 discovery): UR 1.35241-1.35327 REACTED (Mon-Tue consolidation around it; Wed 08:00 1.35353 → 1.3492; Thu 1.35182 at its part rejected); UR 1.34932-1.35019 REACTED (Wed lows 1.3492-1.34943 held; consolidation); MRS 1.34768-1.34846 REACTED (Mon 1.34818, Tue 1.34744, Thu 00:00 1.34789 bounced; Thu 18:00 retest from below rejected); 1H MoM Demand 1.34345-1.34660 REACTED (Thu 1.34476, Fri 1.34532 bounced); KSB 1.33998-1.34073 NOT REACHED; LSZ 1.33805-1.33855 NOT REACHED; discovery 1.34147 NOT REACHED. Missing: **the week high 1.3539-1.3544 (Mon 14:00 1.35444, Mon 16:00 1.35443, Tue 14:00 1.35396, Fri 1.3537) — 7-12 pips above UR's top 1.35327 with no sweep zone above it** (price held above the zone for a day: not a wick sweep). **E1 = 4/(4+1) = 80%**.
Side: bloated none (1H demand labelled 31.5 pips; full 47 pips but few candles inside); (a) PASS; (b) PASS; floating: **KSB 1.33998-1.34073 40 pips below the week low 1.34476, LSZ 1.33805-1.33855 62 pips below, discovery 1.34147 33 pips below**; missing: the 1.3544 top. **FAIL**.

**E2**: Mon SS (box 1.34399-1.35019) — WRONG (broke out to 1.35444, closed 1.35333 above the box); Tue SS+RWL+BS down — RIGHT (range, break through UR2 to MRS 1.34744, close down; marginal: recovered to 1.3509); Wed BS down — WRONG (no breakdown: 1.3492-1.3535 range, low held at UR2); Thu BS+RWL down — RIGHT (1.35182 spike rejected, crash to 1.34476); Fri RWL up — RIGHT (1.34532 → 1.3537). **E2 = 3/5 = 60%**.

**E3**: T1-T6 all MISSED (no long ever filled; GB1 1.34660 / GB4 1.34083 never reached; GB3 / GB5 shorts never reached). **E3 = 0/6 = 0%**. Stopped: **GB2** SHORT 1.35163 (Mon 07:15 → Mon 11:15), **GBA2** ALT SHORT 1.35063 (Tue 21:00 → Wed 05:15).

Presentation: the forecast path dives to 1.3407 on Thursday, 40 pips under the candles; boxes GB3/GB4/GB5 and the KSB / LSZ / discovery objects fill the lower half of the frame where price never went; "Mon SS" tag and "GB2 BS S 13.5R" sit on Monday candles.

## 7. DXY 2026-10-05

**Obvious trades (from `_zones`, before setups)**: T1 Mon SHORT 102.43 → 102.08 (MRS LSZ part); T2 Tue SHORT 102.285 → 101.754 (KSB); T3 Tue-Wed LONG 101.754 → 102.499 (LSZ supply); T4 Wed-Thu SHORT 102.47-102.50 → 102.033 (MRS); T5 Fri LONG 101.92 → 102.335 (gap). = 5.

**E1** (6 zones): LSZ 102.485-102.535 REACTED (Wed 12:00 102.499, Thu 10:00 102.467 rejected); GAP 102.314-102.374 REACTED (Mon 12:00 102.372 rejected; Fri 102.331-102.335 top); LSZ 102.157-102.207 (reach 102.307) REACTED (Tue 06:00 102.285 → 101.776; Wed 18-Thu 00 lows held); MRS 101.961-102.051 REACTED (Mon 102.084, Thu 102.033, Fri 101.920 bounced); KSB 101.750-101.843 REACTED (Tue 101.754, afternoon consolidation, rally); KSB 101.479-101.565 NOT REACHED. Missing: none (Mon 06:00 102.433 lies 5.2 pips under the LSZ — counted at it). **E1 = 5/5 = 100%**. Side: bloated none; (a) PASS (closest 10.6); (b) PASS; floating none (KSB2 19 pips below low). **PASS / PASS**.

**E2**: all five days SS, box 101.755-102.635: Mon 102.08-102.43 RIGHT; Tue 101.754-102.285 RIGHT (swing to the floor, held); Wed 101.822-102.499 RIGHT; Thu 102.033-102.467 RIGHT; Fri 101.920-102.335 RIGHT. **E2 = 5/5 = 100%**.

**E3**: T1 CAUGHT (DX1 SHORT 102.435 filled Mon 06:30, TP 101.941 Tue 11:15); T2 MISSED (no short at the 102.2-102.3 Tuesday turn; DX1 was entered at the Monday zone); T3 CAUGHT (DX2 LONG 101.926 Tue 11:00 → 102.420 Wed 12:00); T4 CAUGHT (DX1.Wed SHORT 102.435 Wed 12:00 → 101.941 Fri 05:30); T5 MISSED (DX2.Fri filled Fri 05:30, TP 102.420 not reached — high 102.335, still open). **E3 = 3/5 = 60%**. Stopped: none. Double fills: DX2.Wed filled Tue 21:00 while DX2 open; DX1.Thu filled while DX1.Wed open.

Presentation: DXA2 ALT box drawn up to 103.155 (75 pips above the week), stretching the `_all` price axis; DXA2 / DXB2 labels cut at the right edge; DX labels over candles.

## 8. EURUSD 2026-10-05

**Obvious trades (from `_zones`, before setups)**: T1 Mon LONG 1.1169 (gap) → 1.1225 (LSZ); T2 Tue LONG 1.1203 (LSZ reach / LQ) → 1.1277 (1H BoM supply); T3 Tue-Wed SHORT 1.1277 → 1.1165 (LSZ); T4 Thu LONG 1.1172 (gap) → 1.1227 (LSZ); T5 Fri SHORT 1.1243 (UR) → 1.1187 (gap). = 5.

**E1** (6 zones + 3 discovery): 1H BoM Supply 1.12716-1.12853 REACTED (Tue 12:00 1.12767); UR 1.12451-1.12530 REACTED (Tue 12-22 consolidation; Fri 1.12427 rejected); LSZ 1.12149-1.12199 REACTED (Mon 18-Tue 04 consolidation; Thu 1.12267 rejected); GAP 1.11862-1.11922 REACTED (Mon 1.11863, Fri 1.11874; Wed consolidation); GAP 1.11720-1.11780 REACTED (Mon 06:00 1.1169, Thu 1.11719); LSZ 1.11610-1.11660 REACTED (Wed 12:00 1.11645); discovery 1.12364 REACTED (Wed 00-04 consolidation 1.1227-1.1239 at it; Tue crossed it without pause); discovery 1.12000 REACTED (Mon and Wed-Thu consolidation around it); discovery 1.11500 NOT REACHED. Missing: none. **E1 = 8/8 = 100%**. Side: (a) PASS (closest 6); (b) PASS (supply-full / UR-full touch at 1.12611-1.12612, no candle through both); floating none (1.115 is 14.5 pips below low). **PASS / PASS**.

**E2**: all SS, box 1.11510-1.12712: Mon RIGHT; Tue RIGHT (high 1.12767 = 5.5-pip sweep of the ceiling, reversed); Wed RIGHT (ceiling-to-floor swing, held 1.11645); Thu RIGHT; Fri RIGHT. **E2 = 5/5 = 100%**.

**E3**: T1 CAUGHT (EU1 LONG 1.11710 Mon 06:30 → 1.12476 Tue 09:45); T2 MISSED (no long at 1.1203); T3 CAUGHT (EU2.Wed SHORT 1.12585 filled Tue 21:00 → 1.11725 Wed 12:15); T4 MISSED (EU1.Thu filled Thu 11:30, TP 1.12476 never reached, open at week end); T5 MISSED (EU2.Fri 1.12585 never reached). **E3 = 2/5 = 40%**. Stopped: **EU2** SHORT 1.12585 (Tue 11:15 → Tue 12:00). EU1.Wed and EU1.Thu both open at the week end (not losses, not wins).

Presentation: EU labels stacked over candles; EUB3 / EUB4 ALT labels cut at the right edge; discovery label "DISCOVERY ZONE | MA convergence" printed under the UR label inside candles.

## 9. GBPUSD 2026-10-05

**Obvious trades (from `_zones`, before setups)**: T1 Mon SHORT 1.3239 (1H BoM supply) → 1.3190 (LSZ part); T2 Mon LONG 1.3190 → 1.3229; T3 Tue LONG 1.3201 (MRS) → 1.3286 (4H supply); T4 Tue-Wed SHORT 1.3285 → 1.3194 (LSZ part); T5 Thu LONG 1.3184 (LSZ) → 1.3249 (UR); T6 Fri SHORT 1.3250 (UR) → 1.3206 (MRS). = 6.

**E1** (6 zones + 1 discovery): 4H BoM Supply 1.32610-1.32717 REACTED (Tue 10-18 consolidation, top 1.32856 3 pips past its reach); UR 1.32457-1.32535 REACTED (Wed 02-06 support; Thu 1.32485, Fri 1.32503 rejected); 1H BoM Supply 1.32319-1.32395 REACTED (Mon 08:00 1.3239 → 1.319); GAP 1.32124-1.32184 REACTED (Mon 16-Tue 04 consolidation); MRS 1.31991-1.32051 REACTED (Tue 1.32013, Fri 1.32057); LSZ 1.31806-1.31864 REACTED (Mon 1.319 at its part, Thu 1.31843); discovery 1.31630 NOT REACHED (and not visible in the frames). Missing: none. **E1 = 6/6 = 100%**. Side: (a) PASS (closest 6.2); (b) PASS; floating none (1.3163 is 21 pips below low). **PASS / PASS**.

**E2**: all SS, box 1.31799-1.32482: Mon RIGHT; Tue WRONG (broke the ceiling, held above for 12 h to 1.32856, closed 1.32742 — a breakout, the ALT trigger fired Tue 09:00); Wed WRONG (opened 18 pips above the box and fell 82 pips to the floor — the reversal of Tuesday's breakout, not a range); Thu RIGHT; Fri RIGHT. **E2 = 3/5 = 60%**.

**E3**: T1 CAUGHT (GB1 SHORT 1.32329 → 1.32014); T2 CAUGHT (GB2 LONG 1.31899 → 1.32304); T3 MISSED; T4 MISSED (GB1.Wed void; GBB3 only filled Friday); T5 CAUGHT (GB2.Thu 1.31899 → 1.32304); T6 CAUGHT (GBB3 ALT SHORT 1.32475 Fri 01:30 → 1.32097). **E3 = 4/6 = 66.7%**. Stopped: none.

Presentation: void orders GB1.Wed/Thu/Fri still drawn as boxes with labels; GBB3 label cut at the right edge; day tags overlapped by Tuesday candles in the `_all` frame.

## 10. DXY 2026-05-18

**Obvious trades (from `_zones`, before setups)**: T1 Mon SHORT 99.30 → 98.95 (MRS); T2 Tue LONG 98.945 → 99.434 (LSZ); T3 Wed SHORT 99.47 → 98.966 (MRS); T4 Thu LONG 99.064 → 99.515 (LSZ reach); T5 Thu SHORT 99.515 → 99.092. = 5.

**E1** (4 zones + 1 discovery): LSZ 99.359-99.409 (reach 99.509) REACTED (Tue 99.434, Wed 99.472, Thu 99.515, Fri 99.412 all turned there); 1H MoM Demand 99.174-99.244 REACTED (Tue 16-22 support, Wed 16-Thu 04 resistance, Fri lows 99.172-99.24); MRS 98.963-99.037 REACTED (Mon 12-22 consolidation, Wed 15:00 98.966 bounce); 1H MoM Demand 98.844-98.889 NOT REACHED (low 98.944, 0.5 pip above its LQ part); discovery 99.695 NOT REACHED. Missing: none. **E1 = 3/3 = 100%**. Side: (a) PASS; (b) PASS (LSZ-full / 1H-full 3.9 pips apart — the Wed 14:00 candle 99.472→99.124 crossed both, but they are not within 2 pips); floating none (discovery 18 pips above high). **PASS / PASS**.

**E2**: all SS, box 98.963-99.509: Mon RIGHT (swing to the floor, 98.946); Tue RIGHT; Wed RIGHT; Thu RIGHT (99.515 = sweep of the reach); Fri RIGHT. **E2 = 5/5 = 100%**.

**E3**: all five MISSED: the only primary order DX1 LONG 99.050 filled Mon 11:30 and was STOPPED Mon 16:15 (low 98.971 = its SL); every repeat DX1.Tue-Fri voided ("anchor zone closed through Mon 20:00"); no short order existed at the LSZ ceiling that turned price four times; DXB2 never filled, DXA2 never triggered. **E3 = 0/5 = 0%**. Stopped: **DX1**.

Presentation: void DX1.Tue-Fri boxes still drawn; the DXA2 ALT box (to 99.635) drawn over the top of the week; "DISCOVERY ZONE | Supply Ceiling Target" label printed in the chart header in the `_zones` frame.

## 11. EURUSD 2026-05-18

**Obvious trades (from `_zones`, before setups)**: T1 Mon LONG 1.1622 (EQ) → 1.1661 (UR part); T2 Tue SHORT 1.1661 → 1.1592 (MRS); T3 Wed LONG 1.1583 (LQ) → 1.1645 (UR2); T4 Thu SHORT 1.1635 (EQ part) → 1.1576 (LQ); T5 Thu LONG 1.1576 → 1.1630 (EQ). = 5.

**E1** (5 zones + 1 discovery): UR 1.16641-1.16726 REACTED (Mon 20-22 1.16608-1.16617 at its LQ part → 70-pip fall); UR EXTREME 1.16493-1.16562 REACTED (Mon 12-18 consolidation; Wed 14:00 spike 1.16448 rejected); EQ 1.16219-1.16296 REACTED (Wed 16-Thu 04 consolidation; Thu 1.16353, 1.163 rejected); MRS 1.15970-1.16036 REACTED (Tue 1.15921, Tue-Wed consolidation); liquidity band 1.15747-1.15815 REACTED (Wed 1.15827, Thu 1.15762); discovery 1.15500 NOT REACHED. Missing: none. **E1 = 5/5 = 100%**.
Side: (a) PASS (closest 7.9); (b) PASS (closest 3); bloated none; floating: **discovery line 1.15500 is 26 pips below the week low 1.15762** (discovery line only). Unlabelled objects: the stand-alone band 1.15747-1.15815 carries no label, and a second unlabelled box at about 1.1563-1.1570 is drawn in the `_zones` frame that the facts file does not list. **FAIL** (PASS if discovery lines are exempt from 'floating').

**E2**: all SS, box 1.15747-1.16672: all five days' ranges inside the box (Mon 1.16219-1.16608, Tue 1.15921-1.16617, Wed 1.15827-1.16448, Thu 1.15762-1.16353, Fri 1.15882-1.16205). **E2 = 5/5 = 100%**.

**E3**: T1 MISSED (the only Monday order at EQ was EU2 SHORT — opposite); T2 CAUGHT (EU1 SHORT 1.16604 Mon 20:15 → 1.15985 Tue 14:15); T3 MISSED (EU3.Wed LONG 1.15815 not filled — low 1.15827, 1.2 pips short); T4 MISSED (no short at EQ on Thursday); T5 CAUGHT (EU3.Thu LONG 1.15815 Thu 13:30 → 1.16285). **E3 = 2/5 = 40%**. Stopped: **EU2** SHORT 1.16297 (Mon 06:00 → Mon 07:15).

Presentation: "EU1 SS S 6.3R" printed on top of the "3.7bn Option Strike Target" label and "EU1.Thu" on top of the same label (both illegible); "EU3 SS L 4.8R" over candles; EUB4 label cut at the right edge.

## 12. GBPUSD 2026-05-18

**Obvious trades (from `_zones`, before setups)**: T1 Mon LONG 1.3322 (gap) → 1.3449 (UR); T2 Mon-Tue SHORT 1.3449 → 1.3379 (gap); T3 Wed LONG 1.3375 (gap) → 1.3463; T4 Thu SHORT 1.3455 (UR) → 1.3390 (UR2); T5 Thu LONG 1.3390 → 1.3449; T6 Fri LONG 1.3413 (UR2 reach) → 1.3463. = 6.

**E1** (7 zones): UR 1.34497-1.34557 REACTED (Mon 1.34494, Wed 1.3454, Thu 1.34548 / 1.34492, Fri 1.34535; Wed / Fri wicks to 1.3463 reversed at once); GAP 1.34239-1.34299 REACTED (Mon 18-Tue 00 and Thu-Fri consolidation); UR 1.33950-1.34037 REACTED (Tue-Wed range around it; Thu 12:00 1.33904 bounce); GAP 1.33720-1.33780 REACTED (Mon 08:00 1.33843 → 1.33465; Tue 1.33785, Wed 1.3375-1.3376 bounced); GAP 1.33492-1.33552 REACTED (Mon 10:00 1.33465 bounce); GAP 1.33240-1.33300 REACTED (Mon 06:00 1.33217 start of the rally); MRS 1.32995-1.33055 NOT REACHED in the window. Missing: none. **E1 = 6/6 = 100%**. Side: (a) PASS (all labelled boxes 17-20 pips apart); (b) PASS; floating none (MRS 16 below low). **PASS / PASS**.

**E2**: all SS, box 1.33047-1.34137: Mon WRONG (breakout 1.33217 → 1.34494, closed above the box); Tue RIGHT (range 1.33785-1.34196 under the ceiling after the Mon spill-over); Wed WRONG (spike out to 1.3463, closed 1.34331 above the box); Thu WRONG (range 1.339-1.3455, mostly above the box ceiling); Fri WRONG (whole day 1.34132-1.34631 above the box). The forecast path oscillates 1.3325-1.3394 under the candles all week. **E2 = 1/5 = 20%**.

**E3**: T1 CAUGHT (GB2 LONG 1.33247 Mon 06:00 → 1.33926); T2 MISSED (GB1 short stopped before, repeats void); T3 MISSED (GB2.Wed 1.33247 not reached); T4 CAUGHT (GBB4 ALT SHORT 1.34487 filled Wed 15:15, SL 1.34633 above the 1.3463 / 1.34548 highs, TP 1.33924 Thu 13:30); T5 MISSED; T6 MISSED. **E3 = 2/6 = 33.3%**. Stopped: **GB1** SHORT 1.33983 (Mon 12:30 → Mon 15:45), **GBB3** ALT LONG 1.34037 (Tue 21:00 → Tue 21:15).

Presentation: void GB1.Tue-Fri boxes and labels still drawn; GBB3 / GBB4 ALT labels across candles; day tags "Mon SS ... Fri SS" overprinted by candles in the `_all` frame.

---

## Table — all 12 maps

| Map | E1 (reacted / reached+missing) | E2 (days) | E3 (caught / obvious) | E1 side condition |
|---|---|---|---|---|
| DXY 2026-07-06 | 4/4 = 100% | 4/5 = 80% | 7/7 = 100% | PASS |
| EURUSD 2026-07-06 | 4/4 = 100% | 4/5 = 80% | 7/7 = 100% | PASS |
| GBPUSD 2026-07-06 | 6/6 = 100% | 4/5 = 80% | 4/7 = 57.1% | FAIL (floating KSB 1.32789-1.32877, alt-target zone) |
| DXY 2026-04-20 | 5/5 = 100% | 5/5 = 100% | 2/2 = 100% | PASS |
| EURUSD 2026-04-20 | 8/8 = 100% | 5/5 = 100% | 1/6 = 16.7% | FAIL (floating UR 1.18213-1.18292; bunched (b) MRS-full/GAP 1.16744-1.16804) |
| GBPUSD 2026-04-20 | 4/5 = 80% | 3/5 = 60% | 0/6 = 0% | FAIL (floating KSB, LSZ, discovery; missing 1.3544 top) |
| DXY 2026-10-05 | 5/5 = 100% | 5/5 = 100% | 3/5 = 60% | PASS |
| EURUSD 2026-10-05 | 8/8 = 100% | 5/5 = 100% | 2/5 = 40% | PASS |
| GBPUSD 2026-10-05 | 6/6 = 100% | 3/5 = 60% | 4/6 = 66.7% | PASS |
| DXY 2026-05-18 | 3/3 = 100% | 5/5 = 100% | 0/5 = 0% | PASS |
| EURUSD 2026-05-18 | 5/5 = 100% | 5/5 = 100% | 2/5 = 40% | FAIL (floating discovery 1.15500 only) |
| GBPUSD 2026-05-18 | 6/6 = 100% | 1/5 = 20% | 2/6 = 33.3% | PASS |
| **Total, all 12** | **64/65 = 98.5%** | **49/60 = 81.7%** | **34/67 = 50.7%** | **8 PASS / 4 FAIL** |
| **Total, 9 maps outside 2026-07-06** | **50/51 = 98.0%** | **37/45 = 82.2%** | **16/46 = 34.8%** | **6 PASS / 3 FAIL** |

Alternative readings: E2 with the lenient 07-06 Monday (forecast SS counted as carrying his SS+BS): 52/60 = 86.7% (9-map total unchanged). Side condition with alternative-target zones and discovery lines exempt from 'floating': 10 PASS / 2 FAIL (EURUSD 04-20, GBPUSD 04-20); with bunching read as (a) only, EURUSD 04-20 still FAILs on its floating UR.

Note on E1: the near-100% reflects that the zone map (with parts) covers almost the entire week's range on every map (e.g. EURUSD 07-06 1.1372-1.1484, DXY 07-06 100.47-101.43, GBPUSD 05-18 1.3300-1.3456 as an evenly spaced ladder), so almost every turn lands in some zone; the rule does not penalise that, but the frames are visibly crowded.

## The five defects that cost the most

1. **E3 range orders die after the first touch — repeats void, no order at the bound that actually holds.** DXY 05-18: DX1 LONG 99.050 stopped Mon 16:15 (low 98.971), then DX1.Tue-Fri void "anchor zone closed through Mon 20:00"; the LSZ ceiling 99.36-99.51 turned price Tue 99.434 / Wed 99.472 / Thu 99.515 with no short order there → 0/5. Same pattern GBPUSD 05-18 (GB1 1.33983 stopped Mon 15:45, GB1.Tue-Fri void) and GBPUSD 10-05 (GB1.Wed-Fri void → the 92-pip Tue-Wed short 1.3285→1.3194 missed).
2. **E2 range box held at the pre-week range while the week breaks out of it.** GBPUSD 05-18: box 1.33047-1.34137, Monday broke to 1.34494 and the week traded 1.3375-1.3463; the yellow path oscillates 1.3325-1.3394 under the candles all week (E2 1/5, and the long orders at 1.33247 never fill again). Also GBPUSD 04-20 Mon (1.35444 vs ceiling 1.35019) and GBPUSD 10-05 Tue (1.32856 vs ceiling 1.32482).
3. **GBPUSD 04-20 — the whole E3 sheet built on a breakdown that never came.** Orders sat at 1.35163 / 1.35063 (shorts, both stopped: GB2 Mon 11:15, GBA2 Wed 05:15) and at 1.34083-1.34818 / 1.34557 (never reached); no long at MRS 1.3474-1.3482, which held on Mon, Tue and Thu; forecast path to 1.3407 on Thursday, 40 pips under the week low → E3 0/6.
4. **Entries placed a few pips beyond the real turn, or on the wrong day.** EURUSD 04-20 EU3 SHORT 1.17656 vs Wed high 1.17624 (missed the 59-pip Wed short); EURUSD 05-18 EU3.Wed LONG 1.15815 vs Wed low 1.15827 (missed the 62-pip spike); GBPUSD 07-06 GB7 LONG 1.33888 active Friday only while the turn was Thu 1.33807; DXY 10-05 DX2.Fri TP 102.420 vs Fri high 102.335 (open at week end); EURUSD 10-05 EU1.Thu TP 1.12476 vs Thu high 1.12267.
5. **Floating / missing Engine 1 objects and crowded presentation.** GBPUSD 04-20: KSB 1.33998-1.34073 (40 pips below the low 1.34476), LSZ 1.33805-1.33855 (62 pips), discovery 1.34147 (33 pips), and no zone at the repeated week top 1.3539-1.3544; EURUSD 04-20 UR 1.18213-1.18292 30 pips above the high with a part to 1.18491; GBPUSD 07-06 KSB 1.32789-1.32877 34.5 pips below. On every map position labels sit on the week's candles, void orders stay drawn, ALT labels are cut at the right edge, and labels overprint each other (EURUSD 05-18 "EU1 SS S 6.3R" on "3.7bn Option Strike Target"; EURUSD 04-20 "EU3 Ladder" on "1.1bn Option Strike Target").

Other defects seen (lower cost): resting repeat orders fill while their parent is still open (DXY 07-06 DX3.Tue Mon 21:00, EURUSD 07-06 EU1.Tue Mon 21:00, DXY 10-05 DX2.Wed Tue 21:00) — double exposure; unlabelled stand-alone liquidity bands (DXY 04-20 97.920-97.984, EURUSD 05-18 1.15747-1.15815) and an unlabelled box at about 1.1563-1.1570 on EURUSD 05-18 that the facts file does not list; the date axis labels look shifted by about a day (e.g. "Apr 19" under the Friday candles before the 04-20 week).
