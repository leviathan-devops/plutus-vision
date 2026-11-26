# G1 outside count (dry run), 12 maps

Reviewer: fresh context. I did not build the tool. I judged from the 24 frames in `evidence/s3/`. I took exact prices from `audit/g1_facts/*.txt` and from the 1H bar store (read-only). Times are UTC. The forecast window starts Monday 06:00 UTC (02:00 New York). A trading day runs 21:00 to 21:00 UTC, which matches the facts files' day highs and lows.

## Counting rules (one rule set for all 12 maps)
- **E1.** I count the zones the frame labels: the named IP zones plus the labelled `1H/4H (...) | MoM/BoM` boxes. Overlapping labelled boxes count as one cluster. The unlabelled green bands (V1 baseline) are not E1. The one exception is an unlabelled band that sits exactly on the E2 range bound called "Liquidity Sweep Zone"; I count that as the E1 floor or ceiling.
  - A zone is REACTED if most of its visits gave a sharp rejection or a consolidation in or around it. A sweep beyond the zone by less than the zone's width, followed by a reversal, counts as a reaction.
  - A turning point with no labelled zone within one zone-width counts against E1.
- **E2.** A day is RIGHT only if all of these hold: the shape and direction happened, the day traded inside (or broke out of) its box as forecast, and the yellow line did not end the day at the opposite side from where price ended.
  - On an SS day, a range broken by more than ~15 pips (DXY ~15 pts) and/or a close outside the box is WRONG.
- **E3.** A trade is CAUGHT only by a setup in the same direction, at the same zone, that filled and hit its TP before its SL. A setup that stopped is a loss even if price later reached its TP. A setup still open at week end is not caught.

**The 2026-07-06 operator trades.** His DXY #1 (LONG 100.945, TP 101.115) and EURUSD #1 (SHORT 1.14322, TP 1.14103) fall outside the window.
- **DXY #1:** 100.945 traded only in Mon 02:00-04:00 UTC. After 06:00, price did not come back down to 100.945 until Mon 16:00-17:00, and that hour also hit his SL (100.905). His TP was hit by Mon 09:00.
- **EURUSD #1:** 1.1428-1.1441 traded only in Mon 00:00-04:00. After 06:00, price was back at 1.14322 only at Mon 17:00, and Mon 18:00 then took his SL (1.14408). His TP was hit Mon 10:00.
- Both are therefore excluded, which leaves 7 obvious trades per pair for that week. GBPUSD #1 (1.33331) is inside the window: it filled Mon 06:00-07:00.

---

## DXY 2026-07-06
**Obvious trades** (operator, in window): #2 Mon S 101.14→100.845 · #3 Tue L 100.845→101.19 · #4 Wed S 101.19→100.975 · #5 Wed L 100.975→101.24 · #6 Wed S 101.235→100.68 · #7 Thu S 100.975 (ladder) · #8 Fri L 100.615→100.94. (#1 Mon L 100.945 is pre-06:00, excluded.)

**E1** (zones reached):
- UR 101.199-101.262: REACTED. Rejections Wed 01:00 (101.215) and Wed 15:00 (101.275, 1.3 pip sweep then down to 100.946).
- 1H Unmitigated MoM box ~100.97-101.15 + EQ 100.985-101.077: REACTED. The Mon high 101.145 is at the box top, with repeated consolidations Tue 15-18, Wed 17-23 and Thu 00-12.
- MRS 100.724-100.815 (+ 1H Mitigated 2x MoM): REACTED. Bounces Tue 01:00 (100.803) and Thu 06:00 (100.786). It was then PIERCED Fri 01-02, down to 100.598.
- 1H Unmitigated BoM ~100.655-100.74: REACTED. A 5-pip sweep to 100.598 on Fri 02:00, then a rally to 100.997.
- Not reached: 4H BoM 101.31-101.43, UR 101.448, KSB 100.248, KSB 99.495.
- Turning points with no zone: none.
- Bloat: 100.5-101.45 is covered almost pixel-for-pixel by about 10 stacked bands, so "reacted" is close to automatic here.

**E1 = 4/4 = 100%**

**E2:**

| Day | Verdict | Why |
|---|---|---|
| Mon | RIGHT | SS 100.815-101.199 held (H 101.145 / L 100.838). The line went top, then bottom, and price did the same. |
| Tue | WRONG | The range held, but the line ends Tue at the floor (100.82) while price rallied from 100.803 to close at 101.092, near the ceiling. |
| Wed | RIGHT | SS+RWL+BS down: spike to 101.275 at Wed 15:00 (line peak ~101.30, same hour), then down to 100.946. |
| Thu | RIGHT | BS down: broke the Wed low, 100.786 Thu 06:00, closed down at 100.937, and the line descends with it. |
| Fri | WRONG | Forecast "down" with the line ending at the floor (~100.68). Price made its low 100.598 at Fri 02:00 and then rallied to close at the top, 100.965. |

**E2 = 3/5 = 60%**

**E3:**
- #2 CAUGHT (DX2 S 101.138, TP Tue 01:30)
- #3 CAUGHT (DX3 L 100.851, TP Tue 23:45)
- #4 CAUGHT (DX5 S 101.203, TP Wed 07:15)
- #5 CAUGHT (DX6 L 100.980, TP Wed 09:00)
- #6 CAUGHT (DX4 S 101.235, TP Fri 02:00)
- #7 CAUGHT (DX7 S 100.980, TP Fri 02:00)
- #8 CAUGHT (DX8 L 100.628, TP Fri 14:00)
- Stopped setups: none. DX1 never filled.

**E3 = 7/7 = 100%**

**Presentation:**
- The header OHLC shows 102.284/102.326/102.267/102.279, which is not this week's price (the same header appears on all four DXY frames).
- Overlapping labels:
  - "DX1 SS S 7.3R" over "DX2 SS S 4.2R" and over "1H (Unmitigated) | MoM".
  - "Wed SS+RWL+BS down 40%" over "2.2bn Option Strike Target".
  - "1.4bn Option Strike Target" over "DX6 RWL".
- The Fri day label is cut off by the price axis.
- The Mon and Tue day labels are faded and drawn over candles.
- Setups have no TP/SL outcome marking, so wins and losses cannot be told apart on the chart.

## EURUSD 2026-07-06
**Obvious trades** (operator, in window): #2 Mon L 1.14106→1.14442 · #3 Tue S 1.14441→1.14004 · #4 Wed L 1.14012→1.14276 · #5 Wed S 1.14277→1.1395 · #6 Wed L 1.13953→1.14544 · #7 Thu L 1.14233→1.14544 (reinforcement) · #8 Fri S 1.14578→1.14205. (#1 Mon S 1.14322 is pre-06:00, excluded.)

**E1:**
- UR 1.14444-1.14533 (+ 4H Mitigated 2x MoM, 1H Unmitigated BoM ~1.1437-1.1442): REACTED. Consolidation Mon 18:00-Tue 02:00 at 1.1445-1.1448, then rejection Thu 06:00 at 1.14494.
- 1H Mitigated 4x MoM ~1.1457-1.1462: REACTED. Fri 02:00 top at 1.14608, then a fall to 1.14114.
- 1H Unmitigated MoM ~1.1405-1.1414: REACTED (Mon 13:00 1.14083, Fri 14:00 1.14117).
- MRS 1.13977-1.14053: REACTED (Tue 23:00 1.14001; Wed 15:00 sweep to 1.13911, then +40 pips).
- Turning point with no E1 zone: **1.1430**. Wed 07:00 at 1.14315 dropped 40 pips, and Wed 19:00 / Thu 00:00 1.1430 was a double top. Only an unlabelled V1 band is there; the operator shorted 1.14277.
- Not reached: 1H BoM 1.1475-1.1481, 1H BoM 1.1381-1.1388, 4H BoM 1.1372-1.1380.
- Bloat: 1.1372-1.1481 is covered almost continuously.

**E1 = 4/5 = 80%**

**E2:**

| Day | Verdict | Why |
|---|---|---|
| Mon | RIGHT | SS 1.14053-1.14444 held. The line went floor then top, and so did price (low 13:00, high 18:00). |
| Tue | WRONG | The line ends Tue at the ceiling (1.1445), but price fell from 1.1448 to 1.1408 and closed at 1.14122. |
| Wed | RIGHT | The line dips to 1.1390 at Wed ~16:00; the actual low was 1.13911 at Wed 15:00, then it went up and closed up. |
| Thu | RIGHT | BS up: broke the Wed high and reached 1.14494, closing up at 1.14299. The box was too low, but the direction and breakout were right. |
| Fri | WRONG | Forecast "up" with the line ending at the top (1.1462). Price spiked to 1.14608 at Fri 02:00, then fell all day to close at 1.14147, 10 pips under the box. |

**E2 = 3/5 = 60%**

**E3:**
- #2 CAUGHT (EU4 L 1.14095, TP Mon 18:45)
- #3 CAUGHT (EU1 S 1.14442, TP Tue 21:15)
- #4 CAUGHT (EU7 L 1.14018, TP Wed 07:15)
- #5 CAUGHT (EU5 S 1.14269, TP Wed 11:30)
- #6 CAUGHT (EU6 L 1.13940, TP Fri 02:00)
- #7 CAUGHT (EU8 L 1.14164, 7 pips under his 1.14233, same leg and same TP; TP Fri 02:00)
- #8 CAUGHT (EU9 S 1.14598, TP Fri 12:45)
- **Stopped:** EU2 S 1.14385 (Mon 17:30 → SL Mon 21:45); EU4 re-armed L 1.14095 (Tue 19:15 → SL Tue 21:30); EU10 L 1.14401 (Thu 06:15 → SL Thu 07:00).

**E3 = 7/7 = 100%**

**Presentation:**
- The header OHLC shows 1.11420 (not this week; it appears on all EURUSD frames).
- Overlapping labels: "EU1 SS S 5.7R" over "1H (Unmitigated) | BoM"; "EU3 SS L 7.2R" over "1H (Unmitigated) | MoM".
- The Fri day label and "EU10 Ladder L" are cut off at the right edge.
- EU3 never filled but is still labelled like the others.

## GBPUSD 2026-07-06
**Obvious trades** (operator, all in window): #1 Mon L 1.33331→1.33941 · #2 Mon S 1.33934→1.33347 · #3 Wed L 1.3333→1.34246 · #4 Wed L 1.33629 (reinforcement) · #5 Thu S 1.34246→1.33882 · #6 Thu L 1.33829→1.34485 · #7 Fri S 1.34481→1.34021.

**E1:**
- RC 1.34484-1.34548: REACTED (Fri 02:00 1.34517, then -60 pips).
- 4H Unmitigated BoM ~1.3422-1.3426: REACTED (Thu 06:00 1.34308 sweep, then -50 pips).
- 4H/1H Unmitigated MoM ~1.3396-1.3404: REACTED (Mon 23:00 / Tue 01:00 1.3401 top; Fri 14:00 1.33918 low).
- UR 1.33643-1.33717: REACTED, but mixed. It was pierced like paper Mon 15:00; support Tue 13-18; rejection Wed 07:00 at 1.33700.
- UR 1.33435-1.33521: REACTED (consolidation Mon 07-13 and Tue 21:00-Wed 05:00).
- MRS 1.33225-1.33285: REACTED (Mon 07:00 1.33286; Wed 09:00 1.33222).
- Turning point with no E1 zone: **Thu 12:00 low 1.33807**. Only a V1 band is there; this is the operator's #6 long.
- Not reached: KSB 1.32970 and KSB 1.32789.

**E1 = 6/7 = 86%**

**E2:**

| Day | Verdict | Why |
|---|---|---|
| Mon | RIGHT | SS held (1.33286-1.33972). The line went floor then up, and price did the same. |
| Tue | WRONG | The line ends Tue at the ceiling 1.3394; price fell from 1.3401 to close at 1.33589. |
| Wed | RIGHT | Low 1.33222 at Wed 09:00 (the line low is ~7 h later and 7 pips deeper), then BS up to 1.34104. |
| Thu | WRONG | The box 1.33270-1.33825 and the line (1.3335→1.3385) sat under price all day; price traded 1.33799-1.34308. |
| Fri | WRONG | Forecast "up" with the line ending at the top. Price peaked at 1.34517 at Fri 02:00 and closed near the low at 1.33968. |

**E2 = 2/5 = 40%**

**E3:**
- #1 CAUGHT (GB1 L 1.33333, TP Mon 18:45)
- #2 MISSED (no short at 1.3393; his trade reached its TP Wed 09:00)
- #3 CAUGHT (GB2 L 1.33245, TP Thu 06:15)
- #4 MISSED (GB3 at 1.33473 never filled; GB5 is at 1.33888, a different zone)
- #5 MISSED: GB4 S 1.34254 filled Thu 06:15 and was **STOPPED Fri 02:00**. Its TP 1.33506 was too far; his TP 1.33882 was hit Thu 11:00.
- #6 MISSED (no long at 1.3383 on Thu)
- #7 MISSED (no short at 1.3448)
- **Stopped:** GB4.

**E3 = 2/7 = 29%**

**Presentation:**
- "1H (Unmitigated) | BoM" is printed over the "UPPER RESISTANCE" label at 1.3366.
- "GB1 SS L 6.2R" sits over "1H (Unmitigated) | MoM".
- The Fri label and "GB5 Ladder L" are clipped at the right edge.
- The Mon and Tue labels are faded over candles.

---

## DXY 2026-04-20
**Obvious trades** (from the zones frame, before opening the full frame):
- T1 Mon S 98.39 (1H MoM / 1.4bn) → 98.01 (MRS), Mon 06-15
- T2 Mon-Tue L 98.05 (MRS) → 98.50 (UR 98.456), Mon 15 → Tue 17
- T3 Wed L 98.21 → 98.64, Wed 05-20
- T4 Thu L 98.54 (UR 98.456-98.541 retest) → 98.94 (UR 98.939), Thu 14-17
- T5 Fri S 98.90 (UR 98.939) → 98.50, Fri 03-20

**E1:**
- UR 98.939-99.005 (+ 4H BoM): REACTED (Thu 17:00 98.939 touch, then -25; Fri 03:00 98.915, then -43).
- 1H Unmitigated MoM ~98.68-98.86: REACTED (Thu-Fri consolidation).
- UR 98.456-98.541 (+ 1.1bn): REACTED (Tue 17/19 98.567 rejections; Thu 14:00 98.534 support; Fri close 98.49-98.53).
- 1H Unmitigated MoM ~98.37-98.43 (+ 1.4bn): REACTED (Mon 06:00 98.395 top; Tue 16:00-Wed 04:00 consolidation).
- MRS 98.058-98.145: REACTED (Mon 13:00 98.083; Mon 15:00-Tue 06:00 consolidation 98.01-98.10).
- 1H Unmitigated MoM ~97.94-98.03: REACTED (Mon 15:00 low 98.006).
- Turning point with no E1 zone: **Wed 05:00 low 98.211**, which started the 43-pip leg up. Only a V1 band is there.
- Not reached: KSB 97.725, KSB 97.466, RC 99.217. RC 99.217 is in the facts list but **is not drawn** on the frame.

**E1 = 6/7 = 86%**

**E2:**

| Day | Verdict | Why |
|---|---|---|
| Mon | RIGHT | SS 98.045-98.402 held (98.006-98.395). The line went top then floor, and so did price. |
| Tue | WRONG | Broke the ceiling by 16.5 pts (98.567); the line ends at the floor while price closed at 98.383, near the top. |
| Wed | WRONG | The forecast RWL dip to 97.92 never came (low 98.211). Price broke out above the box and closed 21 pts over it at 98.616. |
| Thu | WRONG | Direction "up" was right, but the box 98.020-98.502 and the line were under the whole day (98.534-98.939). |
| Fri | WRONG | Forecast "up". The high came at Fri 03:00 (98.915) and the day closed down at 98.510; the line peak is ~14 h late. |

**E2 = 1/5 = 20%**

**E3:**
- T1 MISSED (DX1 S 98.415 was above the Mon high 98.395)
- T2 CAUGHT (DX2 L 98.045, TP Tue 16:45)
- T3 MISSED
- T4 MISSED (DX6 and DX7 never live)
- T5 MISSED
- **Stopped:** DX1 S 98.415 (Tue 17:00 → SL Tue 17:15); DX5 L 98.439 (Tue 21:15 → SL Wed 00:00). DX3 and DX4 never filled.

**E3 = 1/5 = 20%**

**Presentation:**
- Overlapping labels:
  - "Wed SS+RWL+BS up 33%" under "1.4bn Option Strike Target".
  - "Thu BS up 33%" under "DX5 BS L 5.1R".
  - "DX2 SS L 5.0R" over "MID-RANGE SUPPORT" and over "DX4 SS L 3.6R".
- Stray dotted lines fan down to 97.6.
- RC 99.217 is not drawn.
- A spike to 99.33 after the week end, at the right edge, distorts the scale.

## EURUSD 2026-04-20
**Obvious trades:**
- T1 Mon L 1.1748 (EQ) → 1.1790 (1H MoM), Mon 06 → Tue 00
- T2 Tue S 1.1790 → 1.1720 (1H MoM navy top), Tue 00-19
- T3 Wed S 1.1756-1.1762 (EQ / V1) → 1.1703, Wed 05-20
- T4 Thu S 1.1716 → 1.1669, Thu 14-17
- T5 Fri L 1.1673 (1H BoM) → 1.1723, Fri 03-20

**E1:**
- 1H Unmitigated MoM ~1.1785-1.1797: REACTED (Mon 15:00-Tue 00:00 top 1.1790-1.1791).
- UR 1.17706-1.17791: REACTED (Mon 10-14 consolidation; Tue 03-06 support).
- EQ 1.17497-1.17573: REACTED (Mon 06:00 1.17475 low; Wed 05:00 1.17624 rejection).
- 1H Unmitigated MoM ~1.1700-1.1722: REACTED (Tue 19:00 1.17187 bounce; Wed 14:00-Thu 08:00 consolidation; Thu 14:00 1.17165 rejection).
- 4H BoM / 1H BoM stack 1.1667-1.1696: REACTED (Thu 10-13 consolidation; Thu 17:00 1.16691 and Fri 03:00 1.16729 lows).
- Turning points with no zone: none.
- Not reached: UR 1.17988, KSB 1.16570. UR 1.18213 and RC 1.18446 are in the facts list but **not drawn**.
- Bunching: 4H BoM, 1H BoM, 4H MoM and KSB are stacked inside 1.1655-1.1696.

**E1 = 5/5 = 100%**

**E2:**

| Day | Verdict | Why |
|---|---|---|
| Mon | RIGHT | SS 1.17207-1.17847, high 5.5 pips over. The line rose to the top, and so did price. |
| Tue | RIGHT | Top early, then down to 1.17187 at the floor; the line ends at the floor. |
| Wed | WRONG | The line rises to 1.1797 (RWL), but the actual high was only 1.17624. The day ended 65 pips under the line at 1.17045, 18 pips under the box. |
| Thu | WRONG | Direction "down" was right, but the whole day (1.16691-1.17165) was under the box 1.17380-1.17865 and under the line. |
| Fri | WRONG | Forecast "down". Price made its low early at 1.16729 and closed up 34 pips at 1.17171. |

**E2 = 2/5 = 40%**

**E3:** all five trades MISSED. EU1, EU2 and EU3 are all SHORT at 1.17920, 1 pip above the week high 1.17910, so no setup filled all week. EU4 and EU5 were never live. There was no long setup at all.
- Stopped: none.

**E3 = 0/5 = 0%**

**Presentation:**
- "Mon SS 65%" sits under "1H (Unmitigated) | MoM" and "EU1 SS S 9.4R".
- "Thu BS down 33%" overlaps "1.4bn Option Strike Target".
- "EU4 Ladder S 12.3R" overlaps "1.1bn Option Strike Target".
- The Fri day label is drawn over candles.
- UR 1.18213 and RC 1.18446 are not drawn.

## GBPUSD 2026-04-20
**Obvious trades:**
- T1 Mon L 1.3482-1.3490 (MRS / UR hard wall) → 1.3533 (UR), Mon 06-13
- T2 Mon-Tue S 1.3540 → 1.3483 (MRS), Mon 15 → Tue 08
- T3 Tue L 1.3475 (MRS) → 1.3534 (UR), Tue 19 → Wed 05/09
- T4 Wed S 1.3534 (UR) → 1.3492, Wed 09-12
- T5 Thu S 1.3490 → 1.3448 (1H MoM), Thu 16-17
- T6 Fri L 1.3455 → 1.3537 (UR), Fri 03-20

**E1:**
- UR 1.35241-1.35327: REACTED (Mon 13:00 1.35365; Wed 05/09 1.3534-1.3535; Fri 20:00 1.35370 rejection).
- UR 1.34932-1.35019 Hard Wall: REACTED (consolidation around it all week).
- MRS 1.34768-1.34846: REACTED (Tue 08:00 1.34823; Tue 19:00 1.34744; Thu 00/13 1.3478-1.3479). It was PIERCED Thu 17:00.
- 1H Unmitigated MoM ~1.3437-1.3466: REACTED (Thu 17:00 1.34476; consolidation to Fri 06:00).
- Turning point with no zone: **Mon 15-17 high 1.35444**, 11 pips over the UR top with nothing drawn above it until 1.357.
- Not reached: KSB 1.33998. UR 1.35719 and RC 1.35940 are in the facts list but **not drawn**.

**E1 = 4/5 = 80%**

**E2:**

| Day | Verdict | Why |
|---|---|---|
| Mon | WRONG | SS box 1.34660-1.34932; price went 51 pips above it (1.35444) and closed at 1.35333. |
| Tue | WRONG | Price traded mostly above the box (to 1.35396). |
| Wed | WRONG | The whole day (1.34901-1.35353) was above the box, with no breakdown. |
| Thu | RIGHT | BS down to 1.34476 inside the box, closing down at 1.34665; the line descends. |
| Fri | WRONG | Forecast "down". Price rallied 56 pips to 1.35370; the line ends with a vertical spike. |

**E2 = 1/5 = 20%**

**E3:** all six trades MISSED. GB1 L 1.34660 never filled; GB2 S 1.34399 was void.
- Stopped: none.

**E3 = 0/6 = 0%**

**Presentation:**
- "KEY SUPPORT BAND..." is overprinted by "4H (Unmitigated) | BoM", so it is illegible.
- The ".0bn Option Strike Target" label is cut at the left and drawn over candles.
- The Mon and Tue labels are faded over candles.
- The Fri yellow line ends in a vertical jump.

---

## DXY 2026-10-05
**Obvious trades:**
- T1 Mon S 102.43 → 102.08, Mon 06-09
- T2 Tue S 102.28 → 101.76 (KSB), Tue 07-12
- T3 Tue-Wed L 101.76 (KSB) → 102.50 (top band / LSZ), Tue 12 → Wed 12
- T4 Wed-Thu S 102.47-102.50 → 102.03 (MRS), Thu 11 → Thu 14/17
- T5 Fri L 101.92 (MRS) → 102.33, Fri 05-16

**E1:**
- Top band 102.50-102.53 (E2 ceiling, LSZ): REACTED (Wed 12:00 102.499; Thu 11:00 102.467).
- MRS 101.961-102.051: REACTED (Tue 08-10 consolidation; Thu 14:00 102.033; Fri 05:00 101.920 sweep).
- 1H Unmitigated MoM ~101.86-101.93: REACTED (Tue 12-22 consolidation).
- KSB 101.750-101.843 + 1H Unmitigated BoM 101.67-101.79: REACTED (Tue 11-15 lows 101.754-101.776).
- Turning points with no E1 zone: **Mon 06:00 102.433** (7 pts under the top band) and **Tue 06-07 102.285** (only a V1 band 9 pts below).
- KSB 101.479, 101.231, 100.980 and 100.470 are in the facts list but **not drawn**, although 101.479 is inside the frame's price range.

**E1 = 4/6 = 67%**

**E2** (SS range 101.926-102.485 all week; the line is a fixed zigzag):

| Day | Verdict | Why |
|---|---|---|
| Mon | WRONG | The line ends at the ceiling; price closed near the low at 102.113. |
| Tue | WRONG | The floor broke by 17 pts (101.754) and the day closed below it at 101.841. |
| Wed | RIGHT | Up to 102.499 at the ceiling, as the line shows. |
| Thu | RIGHT | Down to 102.033, as the line shows. |
| Fri | RIGHT | Low 101.920 at the floor, then up to 102.335. |

**E2 = 3/5 = 60%**

**E3:**
- T1 MISSED
- T2 MISSED
- T3 MISSED. DX2 L 101.926 filled Tue 11:15 and was **STOPPED Tue 11:45**, before the move.
- T4 CAUGHT (DX1 S 102.485, filled Wed 12:15, TP Fri 05:30)
- T5 MISSED
- **Stopped:** DX2.

**E3 = 1/5 = 20%**

**Presentation:**
- The day labels sit over the week's top candles.
- The "1H (Unmitigated) | MoM" label is hidden behind candles.
- The four KSBs are not drawn.

## EURUSD 2026-10-05
**Obvious trades:**
- T1 Mon L 1.1169 → 1.1225, Mon 06-20
- T2 Tue L 1.1203 → 1.1277 (1H BoM), Tue 07-12
- T3 Tue-Wed S 1.1250-1.1277 (UR / BoM) → 1.1165 (floor band), Tue 12 → Wed 12
- T4 Wed-Thu L 1.1165 → 1.1227/1.1243, Wed 12 → Fri 05
- T5 Fri S 1.1243 (UR) → 1.1187, Fri 05-16

**E1:**
- UR 1.12451-1.12530 (+ 1H MoM): REACTED (Tue 08-10 under it; Tue 13-14 retest from above; Fri 05:00 1.12427 rejection).
- 1H Unmitigated BoM ~1.1272-1.1280: REACTED (Tue 12:00 1.12767 top).
- Floor band 1.1162-1.1167 (E2 floor, LSZ): REACTED (Wed 12:00 1.11645 low; Mon 06:00 1.11690).
- Turning points with no E1 zone: **1.1225** (Mon 20:00 1.12249 / Thu 14:00 1.12267 highs) and **1.1203** (Tue 06:00 low before the 70-pip rally). Both have only V1 bands.
- UR 1.12942, 1.13185, 1.13708, 1.13942 and RC 1.14997 are in the facts list but **not drawn** (1.12942-1.13708 are inside the frame's range).

**E1 = 3/5 = 60%**

**E2** (SS 1.11660-1.12491):

| Day | Verdict | Why |
|---|---|---|
| Mon | WRONG | The line ends at the floor; price closed at the high, 1.12218. |
| Tue | WRONG | The ceiling broke by 28 pips (1.12767) and the day closed above it. |
| Wed | RIGHT | Down to the floor at 1.11645, as the line shows. |
| Thu | RIGHT | Up from 1.1172 to 1.1227, as the line shows. |
| Fri | RIGHT | Down from 1.12427 to 1.1187, as the line shows. |

**E2 = 3/5 = 60%**

**E3:** all five trades MISSED. EU1 L 1.11660 was 3 pips under the Mon low (unfilled Mon). It filled Wed 12:15 but its TP 1.12491 was 6.4 pips above the Fri high 1.12427, so it was still open at week end and is not caught. There was no short setup.
- Stopped: none.

**E3 = 0/5 = 0%**

**Presentation:**
- The day labels overlap the zone labels.
- "921M Option Strike Target" is printed over "Thu SS".
- "1H (Unmitigated) | MoM" is half hidden by candles.

## GBPUSD 2026-10-05
**Obvious trades:**
- T1 Mon S 1.3238 (1H BoM) → 1.3190 (floor band), Mon 08-13
- T2 Mon-Tue L 1.3190 → 1.3240 (and on to 1.3285), Mon 13 → Tue 08
- T3 Tue-Wed S 1.3285 → 1.3194, Tue 15 → Wed 12
- T4 Wed-Thu L 1.3184-1.3194 → 1.3249 (UR), Wed 12 → Thu 14
- T5 Fri S 1.3250 (UR) → 1.3206, Fri 05-12

**E1:**
- UR 1.32457-1.32535: REACTED (Wed 02-06 support; Thu 14:00 1.32485 and Fri 05:00 1.32503 rejections).
- 1H Unmitigated BoM ~1.3232-1.3240: REACTED (Mon 08-09 1.3238-1.3239).
- MRS 1.31991-1.32051 + floor band 1.3190-1.3195: REACTED (Mon 13:00 1.31900; Tue 06:00 1.32013; Wed 12:00 1.31935; Thu 10:00 1.31843; Fri 12:00 1.32057).
- Turning point with no zone: **Tue 15:00 week high 1.32856**. Nothing is drawn between 1.3264 and the top of the frame, and it was the start of a 92-pip fall.

**E1 = 3/4 = 75%**

**E2** (SS 1.31949-1.32319):

| Day | Verdict | Why |
|---|---|---|
| Mon | WRONG | The line ends at the floor; price closed in the upper part at 1.32211. |
| Tue | WRONG | The ceiling broke by 54 pips (1.32856) and the day closed 42 pips above it. |
| Wed | RIGHT | Down to 1.31935, as the line shows. |
| Thu | RIGHT | Up to 1.32485, as the line shows. |
| Fri | WRONG | High 1.32503, 18 pips over the ceiling; the line ends at the floor while price closed at 1.32242. |

**E2 = 2/5 = 40%**

**E3:**
- T1 MISSED. GB1 S 1.32319 filled Mon 08:00 and was **STOPPED Tue 08:30**; its TP 1.31900 was missed by 0.1 pip on 15m.
- T2 CAUGHT (GB2 L 1.31949, TP Tue 07:45)
- T3 MISSED
- T4 CAUGHT (GB2 re-armed, filled Wed 12:15, TP Thu 14:30)
- T5 MISSED
- **Stopped:** GB1.

**E3 = 2/5 = 40%**

**Presentation:**
- "GB1 SS S 3.5R" overlaps the BoM band label.
- The day labels sit over candles.
- A red SL box down to 1.3182 is drawn across the whole week.

---

## DXY 2026-05-18
**Obvious trades:**
- T1 Mon S 99.30 → 98.96 (MRS), Mon 06-20
- T2 Mon-Tue L 98.95 (MRS) → 99.40 (top band), Mon 20 → Tue 14
- T3 Wed S 99.47 → 98.97 (MRS), Wed 14-15
- T4 Wed-Thu L 98.97-99.06 → 99.5, Wed 15 → Thu 13
- T5 Thu S 99.5 → 99.09 (1H MoM), Thu 13-17

**E1:**
- Top band 99.36-99.41 (E2 ceiling, LSZ): REACTED (Tue 14:00 99.434; Wed 08/14 99.47; Thu 13:00 99.515; Fri 14:00 99.412). These are sweeps of 2-10 pts above it, then reversals.
- 1H Unmitigated MoM ~99.18-99.27: REACTED (Mon 10:00 99.248 rejection; Thu-Fri consolidation).
- 1H Unmitigated MoM ~99.04-99.10: REACTED (Wed 15-19 99.053-99.064; Thu 01:00 99.064; Thu 17:00 99.092).
- MRS 98.963-99.037 (+ 1H Mitigated 2x MoM, 1.0bn): REACTED (Mon 12/16 98.97-98.98; Mon 20-22 98.944; Wed 15:00 98.966).
- Turning points with no zone: none.
- KSB 98.732, 98.460, 98.240, 97.959 and 97.720 are in the facts list but **not drawn**.
- Bloat: 98.96-99.41 is covered by 7 stacked bands.

**E1 = 4/4 = 100%**

**E2** (SS 99.037-99.359; the zigzag line is in the wrong phase):

| Day | Verdict | Why |
|---|---|---|
| Mon | WRONG | The line ends at the ceiling; price closed at the low, 98.983. |
| Tue | WRONG | The line ends at the floor; price closed near the top, 99.315 (high 99.434). |
| Wed | WRONG | The line ends at the ceiling; price collapsed from 99.472 to close at 99.136. |
| Thu | WRONG | The line goes down to the floor, but the day closed up (99.124 → 99.203). |
| Fri | RIGHT | The line goes up; price closed up at 99.319. |

The SS range as a weekly frame did hold to within 10-16 pts.

**E2 = 1/5 = 20%**

**E3:**
- T1 MISSED
- T2 CAUGHT (DX2 L 99.038, TP Tue 14:15)
- T3 MISSED. DX1 S 99.359 filled Tue 13:30 and was **STOPPED Wed 08:15**, before the drop.
- T4 CAUGHT (DX2 re-armed, filled Wed 15:15, TP Thu 13:15)
- T5 MISSED
- **Stopped:** DX1, and DX3 L 99.097 (Mon 08:30 → SL Mon 12:30).

**E3 = 2/5 = 40%**

**Presentation:**
- "DX1 SS S 3.1R" sits over "1H (Unmitigated) | MoM".
- "DX3 SS L 5.5R" sits over "DX2 SS L 3.4R" and "1H (Mitigated 2x) | MoM".
- The day labels run over candles at 99.36.

## EURUSD 2026-05-18
**Obvious trades:**
- T1 Mon L 1.1622 (EQ) → 1.1660, Mon 06-22
- T2 Tue S 1.1660 → 1.1592 (MRS), Mon 22 → Tue 15
- T3 Wed L 1.1583 → 1.1645 (UR hard wall), Wed 14-15
- T4 Thu S 1.1635 (1H MoM) → 1.1576, Thu 08-13
- T5 Thu L 1.1576 → 1.1630, Thu 13-17

**E1:**
- UR 1.16641-1.16726 (+ 1H MoM): REACTED. The Mon 20-22 tops at 1.16601-1.16617 are 2.4 pips short of it.
- UR 1.16493-1.16562 Hard Wall: REACTED (Mon 12-17 consolidation; Wed 15:00 1.16448 rejection).
- 1H Unmitigated MoM ~1.1630-1.1635: REACTED (Wed 18-19, Thu 01/08/17 rejections).
- EQ 1.16219-1.16296: REACTED (Mon 06:00 1.16219; Mon 10/18; Tue 08-12 consolidation).
- MRS 1.15970-1.16036: REACTED (Tue 15:00 1.15921; Wed consolidation). It was PIERCED Wed 08:00 (1.15836) and Thu 13:00 (1.15762).
- Turning point with no zone: **1.1576-1.1584** (Wed 14:00 1.15827, then +62 pips; Thu 13:00 1.15762, then +54 pips). Nothing is drawn under the MRS.
- UR 1.16939 is in the facts list but **not drawn**.

**E1 = 5/6 = 83%**

**E2** (SS 1.16218-1.16493):

| Day | Verdict | Why |
|---|---|---|
| Mon | WRONG | The line ends at the floor; price closed above the ceiling at 1.16556. |
| Tue | WRONG | The line ends at the ceiling; price fell 57 pips and closed under the floor at 1.16047. |
| Wed | WRONG | The range broke 39 pips below (1.15827). |
| Thu | WRONG | The range broke 46 pips below (1.15762), and the day closed under the floor. |
| Fri | WRONG | The whole day (1.15882-1.16205) was below the box. |

**E2 = 0/5 = 0%**

**E3:** all five trades MISSED.
- EU2 L 1.16218 was 0.1 pip under the Mon low 1.16219, so it did not fill Mon. It filled Tue 09:00 and was **STOPPED Tue 09:15**.
- EU1 S 1.16512 filled Mon 12:30 and was **STOPPED Mon 20:15**, before the Tue drop.
- **Stopped:** EU1 and EU2.

**E3 = 0/5 = 0%**

**Presentation (this is the worst frame; it cannot be judged without the facts file):**
- In 1.1630-1.1665, about six labels are printed on top of each other:
  - "UPPER RESISTANCE | MODERATE..." under "1H (Unmitigated) | MoM".
  - "UPPER RESISTANCE | HEAVY..." under "1H (Mitigated 2x) | MoM" and "EU1 SS S 5.7R".
  - "EQUILIBRIUM ZONE..." under "EU2 SS L 5.8R".
  - "2.2bn" on top of "1.5bn Option Strike Target", on top of "Fri SS".
- The Mon, Tue and Thu day labels are unreadable.
- The yellow line is barely visible against the stacked bands.
- I could not tell from the pixels which band belongs to which label.

## GBPUSD 2026-05-18
**Obvious trades:**
- T1 Mon L 1.3322 (floor band) → 1.3400 (UR) / 1.3449, Mon 06-16
- T2 Mon-Tue S 1.3449 → 1.3379, Mon 16 → Tue 14
- T3 Wed L 1.3375-1.3385 → 1.3463, Wed 08-15
- T4 Thu S 1.3455 → 1.3390 (UR), Thu 08-13
- T5 Thu L 1.3390 (UR) → 1.3449/1.3463, Thu 13 → Fri 13

**E1:**
- UR 1.33950-1.34037 (+ 1H MoM): REACTED (Mon 12-14 resistance; Tue-Wed consolidation; Thu 13:00 1.33904 support).
- Floor band 1.3320-1.3336 (E2 floor, LSZ): REACTED (Mon 06:00 1.33217, then +128 pips).
- Turning point with no drawn zone: **1.3449-1.3463**, the week's ceiling, tested four times (Mon 16:00 1.34494, Wed 15:00 1.34630, Thu 08:00 1.34548, Fri 13:00 1.34631). The facts list has UR 1.34497-1.34557 right there, but **it is not drawn on the frame**. UR 1.34774 and RC 1.35705 are not drawn either.
- Not reached: MRS 1.32995, KSB 1.32484.

**E1 = 2/3 = 67%**

**E2** (SS 1.33197-1.33941):

| Day | Verdict | Why |
|---|---|---|
| Mon | WRONG | The ceiling broke by 55 pips (1.34494) and the day closed 38 pips above it. |
| Tue | WRONG | The day traded 1.3379-1.3437, mostly above the box; the line climbs from the floor, which price never came near. |
| Wed | WRONG | The line ends at the floor; price went to 1.34630 and closed at 1.34331. |
| Thu | WRONG | The whole day was above the box. |
| Fri | WRONG | The whole day was above the box (low 1.34132). |

**E2 = 0/5 = 0%**

**E3:** all five trades MISSED. GB2 L 1.33197 was 2 pips under the Mon low 1.33217, so it never filled. GB1 S 1.33983 filled Mon 12:30 and was **STOPPED Mon 15:45**.
- **Stopped:** GB1.

**E3 = 0/5 = 0%**

**Presentation:**
- "UPPER RESISTANCE | MODERATE | 30-50%..." is overprinted with "1H (Unmitigated) | MoM", so it is illegible.
- "Mon SS 80%" sits under "GB1 SS S 3.5R".
- The zone the week actually traded at (1.3450) is missing from the chart.

---

## Summary table

| Map | E1 % | E2 % | E3 % |
|---|---|---|---|
| DXY 2026-07-06 | 100 (4/4) | 60 (3/5) | 100 (7/7) |
| EURUSD 2026-07-06 | 80 (4/5) | 60 (3/5) | 100 (7/7) |
| GBPUSD 2026-07-06 | 86 (6/7) | 40 (2/5) | 29 (2/7) |
| DXY 2026-04-20 | 86 (6/7) | 20 (1/5) | 20 (1/5) |
| EURUSD 2026-04-20 | 100 (5/5) | 40 (2/5) | 0 (0/5) |
| GBPUSD 2026-04-20 | 80 (4/5) | 20 (1/5) | 0 (0/6) |
| DXY 2026-10-05 | 67 (4/6) | 60 (3/5) | 20 (1/5) |
| EURUSD 2026-10-05 | 60 (3/5) | 60 (3/5) | 0 (0/5) |
| GBPUSD 2026-10-05 | 75 (3/4) | 40 (2/5) | 40 (2/5) |
| DXY 2026-05-18 | 100 (4/4) | 20 (1/5) | 40 (2/5) |
| EURUSD 2026-05-18 | 83 (5/6) | 0 (0/5) | 0 (0/5) |
| GBPUSD 2026-05-18 | 67 (2/3) | 0 (0/5) | 0 (0/5) |
| **All 12 (pooled)** | **82 (50/61)** | **35 (21/60)** | **33 (22/67)** |
| 9 maps outside the golden week | 81 (36/44) | 29 (13/45) | 17 (8/46) |

How to read these numbers:
- The E1 % is inflated by zone density. On most frames the labelled and V1 bands cover nearly every price in the weekly range, so most turns land on some band.
- E3 is 14/14 on DXY and EURUSD in 2026-07-06, the week for which the operator's trades exist, against 8/46 on the other weeks.
- Nothing reaches the 90% target except E1, and that only with the density caveat.

## The five defects that cost the most

1. **E2 SS range boxes are frozen at pre-anchor levels while price leaves them, and the SS yellow line is a fixed alternating zigzag that does not follow price.** This is behind 39 of the 60 WRONG/RIGHT day calls going wrong.
   - GBPUSD 05-18: box 1.33197-1.33941; Mon broke 55 pips above (H 1.34494) and Thu-Fri traded entirely above it (Fri L 1.34132).
   - EURUSD 05-18: box 1.16218-1.16493; Tue-Fri broke under, to 1.15762 on Thu.
   - GBPUSD 04-20: box 1.34660-1.34932; Mon H 1.35444 and Wed entirely above.
   - DXY 05-18: the zigzag is in the opposite phase Mon-Thu (the line ends Mon at the 99.359 ceiling while the Mon close is 98.983).
   - Directional days have the same problem: on GBPUSD 07-06 Thu, DXY 04-20 Thu and EURUSD 04-20 Thu, the box and line sit 20-50 pips away from the day's whole range.

2. **E3 entries rest just beyond the week's extremes, so most weeks have zero or one fill, and there is no setup on most obvious moves.** Outside the golden week, 8 of 46 obvious trades were caught.
   - EURUSD 04-20: EU1, EU2 and EU3 are all SHORT 1.17920 against a week high of 1.17910, so there were no fills all week and no long setup at all.
   - EURUSD 05-18: EU2 1.16218 against a Mon low of 1.16219.
   - GBPUSD 05-18: GB2 1.33197 against a Mon low of 1.33217.
   - EURUSD 10-05: EU1 1.11660 against a Mon low of 1.11690, and its TP 1.12491 against a Fri high of 1.12427 (open at week end).
   - GBPUSD 04-20: GB1 was never filled and GB2 was void.

3. **Setups that stopped out on the week's breakouts (all losses).**
   - GBPUSD 05-18: GB1 S 1.33983, stopped Mon 15:45 (Mon ran to 1.34494).
   - EURUSD 05-18: EU1 S 1.16512, stopped Mon 20:15; EU2 L 1.16218, stopped Tue 09:15.
   - DXY 04-20: DX1 S 98.415, stopped Tue 17:15; DX5 L 98.439, stopped Wed 00:00.
   - DXY 10-05: DX2 L 101.926, stopped Tue 11:45.
   - GBPUSD 10-05: GB1 S 1.32319, stopped Tue 08:30 (its TP 1.31900 was missed by 0.1 pip).
   - DXY 05-18: DX1 S 99.359, stopped Wed 08:15; DX3 L 99.097, stopped Mon 12:30.
   - GBPUSD 07-06: GB4 S 1.34254, stopped Fri 02:00. Its TP 1.33506 was too far; the operator's TP 1.33882 on the same short was hit Thu 11:00.

4. **About half of each map's E1 zone list is not drawn on the chart, including zones the week traded at.**
   - GBPUSD 05-18: UR 1.34497-1.34557 is in the facts list and the week topped there four times (1.34494 Mon, 1.34630 Wed, 1.34548 Thu, 1.34631 Fri), but the frame shows nothing above 1.3404.
   - Also missing, though inside or near the frame's price range:
     - DXY 10-05: KSB 101.479 / 101.231.
     - EURUSD 10-05: UR 1.12942 / 1.13185 / 1.13708.
     - DXY 04-20: RC 99.217.
     - EURUSD 04-20: UR 1.18213 and RC 1.18446.
     - GBPUSD 04-20: UR 1.35719.
     - DXY 05-18: KSB 98.732 and below.
     - EURUSD 05-18: UR 1.16939.
     - DXY 07-06: UR 101.448.
   - Meanwhile, obvious turns had no zone at all:
     - GBPUSD 10-05: the 1.32856 week high on Tue.
     - EURUSD 10-05: 1.1203 Tue and 1.1225 Mon/Thu.
     - EURUSD 05-18: 1.1576-1.1584 Wed/Thu.
     - EURUSD 07-06: 1.1430 Wed.
     - GBPUSD 07-06: 1.33807 Thu.
     - DXY 04-20: 98.211 Wed.

5. **Clutter and overprinting make frames unreadable.**
   - EURUSD 05-18, 1.1630-1.1665: about six labels are stacked, so the zone names, setup labels and the Mon/Tue/Thu day labels cannot be read. The yellow line is lost under 7+ translucent bands, and I had to fall back to the facts file to identify zones.
   - The same overprinting appears on GBPUSD 05-18 at 1.3400 (UR label under "1H (Unmitigated) | MoM"), GBPUSD 04-20 at 1.3405 (KSB label under "4H BoM") and GBPUSD 07-06 at 1.3366.
   - On every frame: the header OHLC shows another date's prices (DXY 102.284, EURUSD 1.11420); the Fri day label and the last ladder label are clipped at the right edge; and setups carry no TP/SL outcome marking, so wins and stops cannot be told apart from the picture.
