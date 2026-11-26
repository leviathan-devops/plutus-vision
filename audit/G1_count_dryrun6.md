# G1 count 6 — independent outside count (reviewer did not build the tool)

Inputs used: the 36 frames in `evidence/s3f/` (each opened), `audit/g1_facts_f/*.txt` (exact prices and times only), `context_management/oracle/golden_week.json` (operator trades, 2026-07-06), the brief's DXY 2026-04-20 operator trades, and 1H / 15m bars read through `e1_tool/e1_data.bars()` to check times and closes. Earlier counts, `memory/` and the tool's code were not read.

## Counting rules applied (so anyone can recount)

General
- Forecast window = Monday 06:00 UTC (02:00 New York, all four weeks are EDT) to Friday 21:00 UTC. Times in the facts files are UTC (checked against bars: e.g. DXY 07-06 DX2 "filled Mon 09:45" = 1H Mon 09:00 high 101.136).
- Pip = 0.01 for DXY, 0.0001 for EURUSD / GBPUSD. "Week range" = forecast-window high - low.
- Proximity tolerance = 5 pips everywhere (a turn, a close, a touch within 5 pips of an object's edge is "at" it; more than 5 pips away is not).

Obvious turns and obvious trades (mechanical, so they do not depend on the setups)
- Obvious turn = a 1H swing extreme from which price moved at least 30 % of the week range before taking out that extreme (zigzag on 1H highs / lows, 30 % threshold). Turns within 5 pips of each other count as one reaction point (one level).
- Obvious trade (weeks other than 2026-07-06 and DXY 2026-04-20) = each zigzag leg between two obvious turns that is >= 30 % of the week range and takes >= 3 1H bars. A leg of <= 2 bars is a spike: it is not a trade, and the legs either side of it are joined. A final leg into Friday counts if it already reached 30 %.
- 2026-07-06: the operator's trades from golden_week.json; a trade whose entry was only available before Mon 06:00 UTC is out of the window (DXY trade 1 at 100.945 and EURUSD trade 1 at 1.14322 both filled and finished before / at the anchor and were never re-offered without stopping -> excluded). DXY 2026-04-20: the operator's two trades from the brief.
- The lists were fixed from the `_zones` frame and this rule before the setups were compared.

E1
- Zone = one labelled box (facts line with its indented parts). A touch / turn at a part or inside a sweep zone's dotted reach is a touch / turn at the zone.
- Reached = price touched the box or one of its parts during the window.
- REACTED = at some contact in the week price either turned from it by >= 15 % of the week range, or held 3+ consecutive 1H bars in / at it (consolidation). PIERCED = every contact was a clean cross. (No reached zone in the 12 maps was pierced on every contact.)
- Bunched = two labelled boxes overlapping or with a gap <= 3 pips. A bunched chain is counted as ONE zone (one entry in numerator and denominator) and listed as a defect — this removes double counting without crediting the stack twice.
- Bloated = labelled box taller than 25 % of the week range; a reached bloated zone counts in the denominator and NOT in the numerator.
- Floating = drawn but more than one week-range from every price of the week: none on these charts (the tool only shows zones inside a price window).
- Missing = an obvious turn (level) with no E1 object within 5 pips; each adds 1 to the denominator.
- E1 % = valid reacted zones / (reached zones + missing levels).

E2
- Trading day = 17:00 New York to 17:00 New York (Mon starts at the anchor), as in the facts' actual H / L / C.
- SS day RIGHT if no 1H close lies more than 5 pips outside the forecast SS box during that day; otherwise WRONG (the range broke).
- BS / WL / RWL / R day (or composite tag) RIGHT if (a) the day's candles enter the forecast box, (b) the day's net move (open -> close) is in the tagged direction, and (c) the defining feature of the last component is present (BS: a 1H close beyond an IP zone in that direction; WL / RWL: spike and rejection; R: small retrace). Otherwise WRONG.
- E2 % = days right / 5.

E3
- CAUGHT = a setup of the same direction, at the zone where the move started (inside that E1 zone or its parts, or for operator trades within ~3 pips of his entry at the same turn), filled on that turn, TP hit before SL, TP covering >= 50 % of the move. A position that is still open at week end, or that filled on an earlier turn, does not catch a later move. Fill rules (front-entry band) taken as the facts file states them.
- E3 % = caught / obvious trades. Every stopped setup is named.

---

## 1. DXY 2026-07-06 (anchor week) — range 100.598-101.275 (67.7 p)

Obvious trades (operator, in window): T2 Mon S 101.14->100.845; T3 Tue L 100.845->101.19; T4 Wed S 101.19->100.975; T5 Wed L 100.975->101.24; T6 Wed S 101.235->100.68; T7 Thu S 100.975 (TP n/a); T8 Fri L 100.615->100.94. (T1 Mon L 100.945 = pre-anchor, out.) = 7.

E1 (7 zones):
- 4H BoM Supply 101.316-101.430: not reached.
- UPPER RESISTANCE 101.199-101.262: REACTED (Wed 01:00 101.215 and Wed 15:00 101.275 rejected, down to 100.95 / 100.786).
- EQUILIBRIUM 100.985-101.077 (+1H supply part to 101.153): REACTED (Mon 10:00 high 101.145 turned; Wed 07:00 low 100.95 turned; Thu 11:00 101.039, Fri 14:00 100.991 tops).
- 1H Mitigated 100.825-100.851 + MID-RANGE SUPPORT 100.724-100.815: BUNCHED (1.0 p gap) -> one zone: REACTED (Tue 01:00 100.803, Thu 06:00 100.786, Fri 16:00 100.727).
- GAP IN-FILL 100.599-100.659: REACTED (Fri 02:00 low 100.598, +40 p).
- KEY SUPPORT BAND 100.470-100.530: not reached.
- Missing turns: none. Bloated / floating: none.
- E1 = 4/4 = **100 %**.

E2: Mon SS RIGHT (100.838-101.145 inside box); Tue SS RIGHT (inside); Wed SS+RWL+BS down RIGHT (dip 100.95, spike 101.275 rejected, 1H close 100.970 below EQ at 19:00); Thu BS down RIGHT (closed through EQ, low 100.786 at MID-RANGE); Fri BS+WL+RWL down RIGHT (100.598 spike, back to 100.997). = 5/5 **100 %**.

E3: T2 CAUGHT (DX2 101.138, TP Tue 01:30); T3 CAUGHT (DX3 100.851, TP Tue 23:45); T4 CAUGHT (DX5 101.203, TP Wed 06:30); T5 CAUGHT (DX6 100.980, TP Wed 09:00); T6 CAUGHT (DX4 101.235, TP Fri 02:00); T7 CAUGHT (DX7 100.980, TP Fri 02:00); T8 CAUGHT (DX8 100.628, TP Fri 13:00). = 7/7 **100 %**. Stopped: **DX2.Tue** (101.138, Tue 19:15 -> Tue 23:45).

Presentation: day tags "Wed SS+RWL+BS" and "Thu BS" run into each other; DX5 / DX4 / DX6 labels overprint each other and the Wed candles at 101.0-101.2; EQUILIBRIUM label and "1.4bn Option Strike Target" overprint DX7 label.

## 2. EURUSD 2026-07-06 (anchor week) — range 1.13911-1.14608 (69.7 p)

Obvious trades (operator, in window): T2 Mon L 1.14106->1.14442; T3 Tue S 1.14441->1.14004; T4 Wed L 1.14012->1.14276; T5 Wed S 1.14277->1.1395; T6 Wed L 1.13953->1.14544; T7 Thu L 1.14233->1.14544; T8 Fri S 1.14578->1.14205. (T1 Mon S 1.14322 = pre-anchor, out.) = 7.

E1 (9 zones):
- 1H BoM Supply 1.14738-1.14807 + LSZ 1.14678-1.14728 + 1H Mitigated 4x 1.14601-1.14677: BUNCHED chain -> one zone: REACTED (Fri 02:00 1.14608, -49 p).
- UPPER RESISTANCE 1.14444-1.14533 + 1H BoM Supply 1.14375-1.14421: BUNCHED (2.3 p) -> one zone: REACTED (Mon 23:00 1.1448, Thu 06:00 1.14494, Tue 12:00 1.14421).
- GAP IN-FILL 1.14220-1.14280: REACTED (Wed 07:00 1.14315 top, Thu 10:00 1.14209 low, Tue 06-10 lows 1.1423-1.1425).
- 4H liquidity band 1.14108-1.14178: REACTED (Mon 13:00 1.14083, Fri 14:00 1.14117).
- MID-RANGE SUPPORT 1.13977-1.14053: REACTED (Wed 01:00 1.13983, Wed 08:00 1.14004).
- 4H BoM Demand 1.13721-1.13832: not reached.
- Missing: Wed 15:00 low 1.13911 (6.6 p below MID-RANGE, no object) -> +1.
- E1 = 5/6 = **83 %**.

E2: Mon SS RIGHT; Tue SS RIGHT; Wed SS+RWL+BS up RIGHT (1.14315 -> 1.13911 -> closes 1.1418-1.1428 above MID-RANGE / liq band); Thu BS up RIGHT (surge to 1.14494 = UPPER RESISTANCE, close 1.14299 > open 1.1416); Fri BS+WL+RWL up RIGHT (1.14608 then rejected to 1.14114). = 5/5 **100 %**.

E3: T2 CAUGHT (EU4 1.14095, TP Mon 18:45); T3 CAUGHT (EU1 1.14442, TP Tue 21:15); T4 CAUGHT (EU7 1.14018, TP Wed 07:15); T5 CAUGHT (EU5 1.14269, TP Wed 11:30); T6 CAUGHT (EU6 1.13940, TP Fri 02:00); T7 CAUGHT (EU8 1.14239, TP Fri 02:00); T8 CAUGHT (EU9 1.14598, TP Fri 12:30). = 7/7 **100 %**. Stopped: **EU2** (1.14385, Mon 17:15 -> Mon 21:45), **EU4.Tue** (1.14095, Tue 19:15 -> Tue 21:30).

Presentation: EU1 / EU2 / EU3 / EU4 / EU1.Tue / EU2.Tue labels pile on each other and on the Mon-Tue candles at 1.1410-1.1435 (several unreadable); day tags "Wed SS+RWL+BS" / "Thu BS" touch.

## 3. GBPUSD 2026-07-06 (anchor week) — range 1.33222-1.34517 (129.5 p)

Obvious trades (operator, all in window: trade 1 entry 1.33331 was traded at Mon 06:00, low 1.33301): T1 Mon L 1.33331->1.33941; T2 Mon S 1.33934->1.33347; T3 Wed L 1.3333->1.34246; T4 Wed L 1.33629->1.34246 (reinforcement); T5 Thu S 1.34246->1.33882; T6 Thu L 1.33829->1.34485; T7 Fri S 1.34481->1.34021. = 7.

E1 (14 zones):
- RESISTANCE CEILING 1.34484-1.34548 + liq band 1.34386-1.34476: BUNCHED (0.8 p) -> REACTED (Fri 02:00 1.34517, -60 p).
- 4H BoM Supply 1.34264-1.34340: REACTED (Thu 06:00 1.34308, -50 p).
- 4H MoM Supply 1.34035-1.34162 + UPPER RESISTANCE 1.33933-1.34005: BUNCHED (3.0 p) -> REACTED (Tue 01:00 1.34015, Wed 17:00 1.34104).
- GAP IN-FILL 1.33744-1.33804 + UPPER RESISTANCE 1.33643-1.33717: BUNCHED (2.7 p) -> REACTED (Tue 06-07 1.3375, Thu 12:00 1.33807, Wed 07-08 1.337 top).
- 1H MoM Supply 1.33544-1.33582 + UPPER RESISTANCE 1.33435-1.33521: BUNCHED (2.3 p) -> REACTED (Mon 07-10 held under 1.335; Tue 19-Wed 01 lows 1.3342-1.3349).
- LSZ demand 1.33340-1.33391: REACTED (Mon 06-09 lows 1.33286-1.33312 in its reach).
- MID-RANGE SUPPORT 1.33225-1.33285: REACTED (Wed 09:00 1.33222, +88 p).
- KEY SUPPORT 1.32970-1.33046, KEY SUPPORT 1.32789-1.32877, LSZ 1.32717-1.32767: not reached.
- Missing: none. 14 zones + 20 parts in a 130-pip week: one drawing every ~4 pips (see defects).
- E1 = 7/7 = **100 %**.

E2: Mon SS RIGHT (1.33286 -> 1.33972, inside 1.33082-1.34032); Tue SS RIGHT; Wed SS+RWL+BS up RIGHT (spike to 1.337, flush to 1.33222, breakout to 1.34104); Thu BS up RIGHT (1.34308 at the 4H BoM key zone; box 1.3327-1.33825 only touched at 1.33799); Fri BS+WL+RWL up RIGHT (1.34517 then 1.33918). = 5/5 **100 %**.

E3: T1 CAUGHT (GB2 1.33333, TP Mon 18:45); T2 CAUGHT (GB1 1.33959, TP Wed 09:00); T3 CAUGHT (GB4 1.33255 in MID-RANGE, TP Thu 06:15); T4 MISSED (no setup at 1.3363; reinforcements rejected); T5 CAUGHT (GB6 1.34254, a "Fri" setup filled Thu 06:15, TP Thu 11:00); T6 MISSED (GB7 1.33888 not filled; low 1.33807); T7 MISSED (no short at 1.3448 RESISTANCE CEILING). = 4/7 **57 %**. Stopped: none. (GB3 void, GB5 / GB7 unfilled.)

Presentation: three labels named "UPPER RESISTANCE" and two "KEY SUPPORT BAND"; 14 boxes + parts stacked 1.327-1.346 make the history half a wall of lines; GB3 / GB2.Tue labels overprint candles at 1.335.

## 4. DXY 2026-04-20 — range 98.006-98.939 (93.3 p)

Obvious trades (operator): O1 L 98.02 / SL 97.87 / TP 98.77 (Mon low 98.006); O2 L 98.29 / SL 98.185 / TP 98.77 (Wed 05:00 low 98.211). = 2.

E1 (12 zones):
- UPPER RESISTANCE 98.939-99.005: REACTED (Thu 17:00 98.939 spike rejected; Fri 03:00 98.915 -> 98.489).
- 1H MoM Supply 98.675-98.845: REACTED (Thu 00:00 98.737, Thu 10-11 98.80 -> 98.534; Thu 19-Fri 01 consolidation).
- liq band 98.561-98.625 + UPPER RESISTANCE 98.456-98.541 + 1H MoM Supply 98.402-98.439: BUNCHED chain (2.0 / 1.7 p) -> REACTED (Tue 17/19 98.567 rejected; Wed 12-13 98.50 rejected; Thu 14 98.534 and Fri 15-20 98.49-98.53 held).
- liq band 98.300-98.364 + GAP IN-FILL 98.220-98.280: BUNCHED (2.0 p) -> REACTED (Wed 05:00 98.211 -> rally; Mon 06-10 consolidation).
- MID-RANGE SUPPORT 98.058-98.145 + 1H MoM Demand 97.937-98.045: BUNCHED (1.3 p) -> REACTED (Mon 15:00 98.006 week low, Tue 14:00 98.123).
- LSZ 97.832-97.882, KEY SUPPORT 97.725-97.799, LSZ 97.632-97.682: not reached.
- Missing: none.
- E1 = 5/5 = **100 %**.

E2: Mon SS RIGHT (98.395 -> 98.006 inside 97.869-98.539); Tue SS+RWL+BS up RIGHT (base 98.04-98.16, close 98.535 at 19:00 above 1H supply, day +33 p; the forecast RWL dip to ~97.97 did not happen); Wed BS up RIGHT (98.211 -> 98.643 through UPPER RESISTANCE); Thu BS+RWL up RIGHT (98.80, dip 98.534, spike 98.939, close 98.826); Fri RWL down RIGHT (98.915 -> 98.489). = 5/5 **100 %**.

E3: O1 CAUGHT (DX1 98.019, a "Tue BS" setup filled Mon 15:15, TP 98.869 Thu 17:15); O2 CAUGHT (DX2 98.270, filled Wed 05:15, TP Thu 17:15). = 2/2 **100 %**. Stopped: **DX3** (98.660, filled Thu 00:00, stopped Thu 00:15 — 4.5-pip stop, 15 minutes).

Presentation: "Tue SS+RWL+BS" / "Wed BS" and "Thu BS+RWL" / "Fri RWL" tags run into each other; the 1H MoM sweep-zone label and the GAP IN-FILL label sit on the forecast-week candles at 98.2-98.4; roughly 20 horizontal lines between 98.0 and 98.6.

## 5. EURUSD 2026-04-20 — range 1.16691-1.1791 (121.9 p)

Obvious trades (zigzag 30 % = 36.6 p): T1 Mon L 1.1748->1.1791; T2 Mon/Tue S 1.1791->1.1719; T3 Tue/Wed L 1.1719->1.1762; T4 Wed/Thu S 1.1762->1.1679 (Thu 14 / Thu 17 spikes joined); T5 Thu/Fri L 1.1669-1.1673->1.1723. = 5.

E1 (13 zones):
- UPPER RESISTANCE 1.18213-1.18292: not reached.
- UPPER RESISTANCE 1.17988-1.18067 (reached via its 1H supply part 1.17847-1.17988): REACTED (Mon 15-Tue 01 held 1.1779-1.1791, then -72 p).
- UPPER RESISTANCE 1.17706-1.17791: REACTED (Tue 00-02 support 1.1777-1.1781; Tue 14:00 1.17759 rejected).
- LSZ 1.17575-1.17661 + LSZ 1.17592-1.17642 + EQUILIBRIUM 1.17497-1.17573: BUNCHED -> REACTED (Mon 06-12 consolidation; Wed 05:00 1.17624 rejected).
- GAP IN-FILL 1.17347-1.17407 + LSZ 1.17277-1.17327 + GAP IN-FILL 1.17203-1.17263: BUNCHED chain -> REACTED (Tue 19:00 1.17187 -> +44 p; Tue 21-Wed 04 consolidation).
- MID-RANGE SUPPORT 1.16973-1.17033 + liq band 1.16876-1.16967: BUNCHED (0.6 p) -> REACTED (Wed 20-23 1.1703, Thu 05-08 1.170-1.171).
- GAP IN-FILL 1.16744-1.16804: REACTED (Thu 10-11 1.16789 -> 1.17165).
- KEY SUPPORT 1.16570-1.16638 (reached via 1H demand part 1.16638-1.16754): REACTED (Thu 17:00 1.16691, Fri 03:00 1.16729).
- Missing: none.
- E1 = 7/7 = **100 %**.

E2: Mon SS RIGHT; Tue SS+RWL+BS down RIGHT (1.1791 -> 1.17187, closes below EQUILIBRIUM); Wed BS down RIGHT (1.17624 -> 1.1703); Thu BS+RWL down RIGHT (1.16789, spike 1.17165, 1.16691, close below open); Fri RWL up RIGHT (1.16729 -> 1.1723). = 5/5 **100 %**.

E3: T1 MISSED (EU2 long 1.17207 never filled); T2 CAUGHT (EU3 / EU4 short 1.17920, filled Mon 23:00, TPs Tue 15:00 / Thu 00:00); T3 MISSED (no long); T4 MISSED (EU5 short 1.17656 not filled — Wed 05:00 high 1.17624); T5 MISSED (no long). = 1/5 **20 %**. Stopped: none.

Presentation: "Tue SS+RWL+BSWed BS" and "Thu BS+RWLFri RWL" tags merge into one string; EU1 / EU3 labels overprint each other at 1.1785; LSZ labels in green on green bands are hard to read.

## 6. GBPUSD 2026-04-20 — range 1.34476-1.35444 (96.8 p)

Obvious trades (zigzag 30 % = 29 p): T1 Mon L 1.3482->1.3544; T2 Mon/Tue S 1.3544->1.3482; T3 Tue L 1.3482->1.3540; T4 Tue S 1.3540->1.3474; T5 Tue/Wed L 1.3474->1.3535; T6 Wed/Thu S 1.3535->1.3479; T7 Thu L 1.3479->1.3518; T8 Thu S 1.3518->1.3457; T9 Fri L 1.3453->1.3537. = 9.

E1 (9 zones):
- UPPER RESISTANCE 1.35241-1.35327 + LSZ 1.35163-1.35213: BUNCHED (2.8 p) -> REACTED (Wed 08-09 1.3535 rejected; Thu 14:00 1.35182).
- GAP IN-FILL 1.35047-1.35107 + UPPER RESISTANCE HEAVY 1.34932-1.35019: BUNCHED (2.8 p) -> REACTED (Wed 13-23 consolidation 1.3492-1.3511).
- MID-RANGE SUPPORT 1.34768-1.34846: REACTED (Mon 06:00 1.34818, Tue 08:00 1.34823, Tue 19:00 1.34744).
- 1H MoM Demand 1.34345-1.34660 (+ liq band 1.34227-1.34339, bunched): reached, reacted (Thu 17:00 1.34476, Fri 03:00 1.34532) but **BLOATED** (31.5 p box > 25 % of 96.8 p) -> not credited.
- KEY SUPPORT 1.33998-1.34073, 1H BoM Demand 1.33806-1.33960: not reached.
- Missing: Mon 15:00 high 1.35444 (11 p above the top drawing 1.35332); Tue 14:00 high 1.35396 (6.4 p above) -> +2.
- E1 = 3/6 = **50 %**.

E2: Mon SS WRONG (box top 1.35019; 1H closes up to 1.35401, trend day to 1.35444); Tue SS+RWL+BS down RIGHT (close 1.34818 at 19:00 below UPPER RESISTANCE HEAVY, day -26 p, though it whipped back); Wed BS down WRONG (no 1H close below 1.34932, day -7 p, high 1.35353 first); Thu BS+RWL down RIGHT (closes below MID-RANGE, low 1.34476); Fri RWL up RIGHT. = 3/5 **60 %**. (Yellow path dives to ~1.3407 on Thu; price never went below 1.34476.)

E3: T1-T9 all MISSED. GB1 1.34660 / GB3 1.34818 / GB4 1.34083 / GB5 1.34557 never filled; GB2 (Tue BS short 1.35163) filled Mon 07:15 and was stopped. = 0/9 **0 %**. Stopped: **GB2** (1.35163, Mon 07:15 -> Mon 15:15 at 1.35387).

Presentation: "Tue SS+RWL+BSWed BS" / "Thu BS+RWLFri RWL" merged tags; GB2 label overprints the UPPER RESISTANCE HEAVY label and candles at 1.3500; top of the zone window (1.35327) cuts below three of the week's highs.

## 7. DXY 2026-10-05 — range 101.754-102.499 (74.5 p)

Obvious trades (zigzag 30 % = 22.3 p): T1 Mon S 102.43->102.08; T2 Mon L 102.08->102.37; T3 Mon/Tue S 102.37->102.04; T4 Tue L 102.04->102.28; T5 Tue S 102.28->101.75; T6 Tue/Wed L 101.75->102.50; T7 Wed/Thu S 102.50->102.13; T8 Thu L 102.13->102.47; T9 Thu/Fri S 102.47->101.92 (Thu 14-16 2-bar spike joined); T10 Fri L 101.92->102.335. = 10.

E1 (8 zones):
- LSZ supply 102.485-102.535: REACTED (Wed 12:00 102.499 -> -37 p; Thu 11:00 102.467).
- LSZ 102.157-102.207 + LSZ 102.082-102.132: BUNCHED (2.5 p) -> REACTED (Mon 09:00 102.084 turn; Mon 07-12 and Thu 00-04 consolidation; Tue 07:00 102.285 inside reach).
- MID-RANGE SUPPORT 101.961-102.051: REACTED (Tue 01:00 102.044, Thu 14:00 102.033, Fri 01-07 hold).
- 1H MoM Demand 101.855-101.926 + KEY SUPPORT 101.750-101.843: BUNCHED (1.2 p) -> REACTED (Tue 12:00 101.754, Tue 13-22 consolidation).
- LSZ 101.668-101.718, KEY SUPPORT 101.479-101.565: not reached.
- Missing: Mon 06:00 high 102.433 (5.2 p below the 102.485 LSZ); 102.37 level (Mon 13:00 102.372 and Thu 16:00 102.367, 6.5 p above the 102.307 sweep reach) -> +2.
- E1 = 4/6 = **67 %**.

E2: SS every day, box 101.755-102.635. No 1H close outside on any day (low 101.754 Tue 12:00, high 102.499 Wed 12:00). Mon-Fri RIGHT = 5/5 **100 %**.

E3: T6 CAUGHT (DX2.Tue long 101.926, filled Tue 11:00, TP 102.470 Wed 12:15); T7 CAUGHT (DX1.Wed short 102.485, filled Wed 12:15, TP 101.941 Fri 05:30); T10 MISSED (DX2.Fri long 101.926 filled Fri 05:30, still open, Fri high 102.335 < TP 102.470); T1-T5, T8, T9 MISSED (no setup inside the range). = 2/10 **20 %**. Stopped: none.

Presentation: setup labels DX1.Tue / DX1.Wed / DX2.Thu / DX2.Fri sit on the candles; day tags sit inside the red box over candles at 102.6; green LSZ labels on green bands are hard to read.

## 8. EURUSD 2026-10-05 — range 1.11645-1.12767 (112.2 p)

Obvious trades (zigzag 30 % = 33.7 p): T1 Mon L 1.1169->1.1221; T2 Mon S 1.1221->1.1186; T3 Mon/Tue L 1.1186->1.1277; T4 Tue/Wed S 1.1277->1.1165; T5 Wed/Thu L 1.1165->1.1213; T6 Thu S 1.1213->1.1172; T7 Thu/Fri L 1.1172->1.1243 (Thu 14-16 spike joined); T8 Fri S 1.1243->1.1187. = 8.

E1 (6 zones):
- 1H BoM Supply 1.12716-1.12853: REACTED (Tue 12:00 1.12767 -> -30 p, later -112 p).
- GAP IN-FILL 1.12611-1.12671: REACTED (Tue 12-22 consolidation 1.1254-1.1269).
- UPPER RESISTANCE 1.12451-1.12530: REACTED (Tue 08-10 hold below, Tue 13-14 support; Fri 05:00 1.12427).
- LSZ 1.12208-1.12258 + LSZ 1.12149-1.12199: BUNCHED (0.9 p) -> REACTED (Mon 09:00 1.12207; Thu 02:00 1.12128; Thu 14:00 1.12267).
- LSZ 1.11610-1.11660: REACTED (Wed 12:00 1.11645 -> +48 p; Mon 06:00 1.1169).
- Missing: 1.1186 level (Mon 14:00 1.11863, Thu 16:00 1.11845, Fri 16:00 1.11874 — 17 p below the next object); Thu 11:00 1.11719 (5.9 p above the LSZ) -> +2.
- E1 = 5/7 = **71 %**.

E2: SS every day, box 1.1151-1.12712. Highest close 1.12681 (Tue 11:00), lowest 1.11734: all inside. 5/5 **100 %**.

E3: T4 CAUGHT (EU1.Wed short 1.12585, filled Tue 21:00, TP 1.11675 Wed 12:15); T5 MISSED and T7 MISSED (EU2.Wed long 1.11660 filled Wed 12:15, still open at week end — Fri high 1.12427 vs TP 1.12476); T1 MISSED (EU2 1.1166 not reached, low 1.1169); T2, T3, T6, T8 MISSED. = 1/8 **12.5 %**. Stopped: **EU1.Tue** (1.12585, Tue 11:15 -> Tue 12:00, 1.12767 spike).

Presentation: "1H (Unmitigated) | BoM + in-fill" label overprinted by the "Mon SS" / "Tue SS" tags at 1.1275; setup labels EU1.Tue / EU2.Wed / EU2.Thu on candles.

## 9. GBPUSD 2026-10-05 — range 1.31843-1.32856 (101.3 p)

Obvious trades (zigzag 30 % = 30.4 p): T1 Mon L 1.3205->1.3239; T2 Mon S 1.3239->1.3190; T3 Mon/Tue L 1.3190->1.3232; T4 Tue S 1.3232->1.3201; T5 Tue L 1.3201->1.3286; T6 Tue/Wed S 1.3286->1.3194; T7 Wed L 1.3194->1.3224; T8 Wed/Thu S 1.3224->1.3184; T9 Thu/Fri L 1.3184->1.3250 (Thu 14-16 spike joined); T10 Fri S 1.3250->1.3206; T11 Fri L 1.3206->1.3244. = 11.

E1 (6 zones):
- UPPER RESISTANCE 1.32457-1.32535: REACTED (Thu 14:00 1.32485 and Fri 05:00 1.32503 rejected; Wed 04-06 held). (Tue 10-11 it was crossed in one bar.)
- 1H BoM Supply 1.32319-1.32395: REACTED (Mon 08-09 1.3239 -> -49 p; Tue 01:00 1.32318).
- GAP IN-FILL 1.32124-1.32184: REACTED (Mon 15-Tue 05 consolidation; Wed 15:00 1.32242 in its sweep part).
- MID-RANGE SUPPORT 1.31991-1.32051: REACTED (Mon 06:00 1.32052, Tue 06:00 1.32013 -> +84 p, Fri 12:00 1.32057).
- LSZ 1.31899-1.31949: REACTED (Mon 13:00 1.319, Wed 12:00 1.31935).
- LSZ 1.31806-1.31864: REACTED (Thu 10:00 1.31843).
- Missing: Tue 15:00 week high 1.32856 (18 p above the highest drawing, sweep reach 1.3268) -> +1.
- E1 = 6/7 = **86 %**.

E2: SS every day, box 1.31799-1.32395. Mon RIGHT; Tue WRONG (closes 1.3242-1.3279 from Tue 08:00, +84 p breakout); Wed WRONG (Wed opened above the box, closes 1.3240-1.3262 until 08:00, 80-p drop back in); Thu RIGHT (Thu 14:00 spike 1.32485 closed 1.32253); Fri WRONG (closes 1.32435-1.32456 Fri 01-07, up to 6.1 p above the box). = 2/5 **40 %**.

E3: T2 CAUGHT (GB1 short 1.32319, Mon 07:45 -> TP 1.31964 Mon 13:30); T3 CAUGHT (GB2 long 1.31949, Mon 13:30 -> TP 1.32361 Tue 07:45); T7 CAUGHT (GB2.Wed long 1.31949, Wed 12:15 -> TP Thu 14:15); T4 MISSED (GB1.Tue stopped); T1, T5, T6, T8, T9, T10, T11 MISSED. = 3/11 **27 %**. Stopped: **GB1.Tue** (1.32319, Tue 01:30 -> Tue 08:30). Note GB2 carries 2.57R, below the 3.0R floor the tool uses to reject other setups.

Presentation: Tue-Wed candles drawn far above the SS box (box visibly wrong); setup labels GB1.Tue / GB1.Wed / GB2.Thu over candles; tags "Mon SS ... Fri SS" overprinted by candles at 1.3240.

## 10. DXY 2026-05-18 — range 98.944-99.515 (57.1 p)

Obvious trades (zigzag 30 % = 17.1 p): T1 Mon S 99.31->98.94; T2 Mon/Tue L 98.94->99.43; T3 Tue S 99.43->99.23; T4 Tue/Wed L 99.23->99.47; T5 Wed S 99.47->98.97; T6 Wed/Thu L 98.97->99.52 (Thu 07-08 spike joined); T7 Thu S 99.52->99.09; T8 Thu/Fri L 99.09->99.41; T9 Fri S 99.41->99.19. = 9.

E1 (6 zones):
- liq band 99.449-99.503: REACTED (Wed 08:00 99.471, Wed 14:00 99.472, Thu 13:00 99.515 rejected).
- LSZ supply 99.359-99.409: REACTED (Tue 14:00 99.434, Fri 14:00 99.412).
- 1H MoM Demand 99.251-99.298 + 1H MoM Demand 99.174-99.244: BUNCHED (0.7 p) -> REACTED (Mon 06:00 99.307 turn, Tue 17-18 99.234, Fri lows 99.21).
- MID-RANGE SUPPORT 98.963-99.037: REACTED (Mon 22:00 98.944, Wed 15:00 98.966).
- 1H MoM Demand 98.844-98.889: not reached.
- Missing: none.
- E1 = 4/4 = **100 %**.

E2: SS every day, box 98.963-99.509; lowest close 98.956 (0.7 p out), highest 99.443. 5/5 **100 %**.

E3: T3 CAUGHT (DX1.Tue short "99.409", met at the 99.355 front edge Tue 13:15, TP 99.052 Wed 15:15); T2 MISSED (DX2 long 99.050 stopped Mon 16:15 before the Mon 22:00 low; DX2.Tue-Fri void); T7 MISSED (DX1.Thu filled Thu 07:15 at 99.356, open at week end); T1, T4, T5, T6, T8, T9 MISSED. = 1/9 **11 %**. Stopped: **DX2** (99.050, Mon 11:30 -> Mon 16:15).

Presentation: DX1.Tue / DX1.Wed / DX1.Thu / DX1.Fri labels sit across the candles at 99.3; two 1H labels overprint each other at 99.2-99.25; DX1 is labelled E 99.409 / 3.2R but fills at 99.355 (true R ~1.9).

## 11. EURUSD 2026-05-18 — range 1.15762-1.16617 (85.5 p)

Obvious trades (zigzag 30 % = 25.6 p): T1 Mon L 1.1622->1.1657; T2 Mon S 1.1657->1.1629; T3 Mon L 1.1629->1.1662; T4 Tue/Wed S 1.1662->1.1583; T5 Wed/Thu S 1.1645->1.1594 (from the Wed 15:00 spike high); T6 Thu S 1.1635->1.1576; T7 Thu L 1.1576->1.1630; T8 Thu/Fri S 1.1630->1.1588; T9 Fri L 1.1588->1.1619. = 9.

E1 (11 zones):
- 1H MoM Supply 1.16738-1.16785 + UPPER RESISTANCE 1.16641-1.16726: BUNCHED (1.2 p) -> reached via liq band part 1.16604-1.16672: REACTED (Mon 20-22 1.1661-1.1662 -> -79 p).
- UPPER RESISTANCE HEAVY 1.16493-1.16562: REACTED (Mon 12-16 1.1656-1.1657 rejected; Wed 15:00 1.16448 at its part).
- liq band 1.16327-1.16395: REACTED (Wed 18-19, Thu 01, Thu 08 tops 1.1635).
- EQUILIBRIUM 1.16219-1.16296 + LSZ 1.16168-1.16218: BUNCHED -> REACTED (Mon 06:00 1.16219; Wed 16-Thu 06 consolidation).
- LSZ 1.16083-1.16133: REACTED (Tue 09-12 and Fri 00-08 consolidation).
- MID-RANGE SUPPORT 1.15970-1.16036: REACTED (Tue 14-Wed 07 lows 1.1592-1.1597).
- liq band 1.15747-1.15815: REACTED (Thu 13:00 1.15762 -> +54 p; Wed 14:00 1.15827).
- liq bands 1.15619-1.15687, 1.15503-1.15571: not reached.
- Missing: Fri 14:00 low 1.15882 (8.8 p below MID-RANGE, 6.7 p above the liq band) -> +1.
- E1 = 7/8 = **88 %**.

E2: SS every day, box 1.15747-1.16672; all closes inside. 5/5 **100 %**.

E3: T4 CAUGHT (EU1 short 1.16604, Mon 20:15 -> TP 1.15985 Tue 14:15); T7 MISSED (EU3.Thu long 1.15815, Thu 13:30, open at week end — TP 1.16478, high after fill 1.163); T1-T3, T5, T6, T8, T9 MISSED. = 1/9 **11 %**. Stopped: **EU2** (1.16297, Mon 06:00 -> Mon 07:15).

Presentation: "2.5bn" and "1.5bn Option Strike Target" labels printed on top of each other at 1.1649 (with EU1.Thu over them); EU2 label overprints the EQUILIBRIUM label; Mon-Fri tags behind candles in the `_all` frame.

## 12. GBPUSD 2026-05-18 — range 1.33217-1.34631 (141.4 p)

Obvious trades (zigzag 30 % = 42.4 p): T1 Mon L 1.3322->1.3449; T2 Mon-Wed S 1.3449->1.3375; T3 Wed L 1.3375->1.3463; T4 Wed/Thu S 1.3463->1.3390; T5 Thu/Fri L 1.3390->1.3463. (Fri 13-14 one-bar spike: not a trade.) = 5.

E1 (12 zones):
- UPPER RESISTANCE 1.34497-1.34557: REACTED (Mon 16:00 1.34494 -> -49 p; Thu 08:00 1.34548; Fri 17:00 1.34535).
- GAP IN-FILL 1.34239-1.34299: REACTED (Mon 17-23, Wed 20-Thu 06, Fri consolidation).
- UPPER RESISTANCE 1.33950-1.34037 + liq band 1.33816-1.33933: BUNCHED (1.7 p) -> REACTED (Mon 12-14 stall, Mon 18-19 1.3400 support, Thu 13:00 1.33904).
- GAP IN-FILL 1.33720-1.33780: REACTED (Wed 06/08 1.3376 / 1.3375 -> +88 p).
- GAP IN-FILL 1.33492-1.33552: REACTED (Mon 10:00 1.33465 -> up).
- GAP IN-FILL 1.33240-1.33300: REACTED (Mon 06:00 1.33217 week low).
- LSZ 1.33147-1.33197, MID-RANGE 1.32995-1.33055, liq band 1.32856-1.32973, GAP 1.32668-1.32728, KEY SUPPORT 1.32484-1.32544: not reached.
- Missing: 1.3463 level (Wed 15:00 1.34630, Fri 13:00 1.34631 — 7.3 p above the top drawing 1.34557) -> +1.
- E1 = 6/7 = **86 %**.

E2: SS every day, box 1.33047-1.34137. Mon WRONG (closes above 1.34137 from Mon 15:00, +128-p trend); Tue WRONG (day opens with closes 1.3420-1.3434 above the box); Wed WRONG (closes 1.3433-1.3442 from 14:00); Thu WRONG (most closes 1.3425-1.3443); Fri WRONG (closes 1.3419-1.3449). = 0/5 **0 %**.

E3: T1 CAUGHT (GB2 long 1.33197, Mon 06:00 -> TP 1.33926 Mon 12:30); T2 MISSED (GB1 short 1.33983 filled Mon 12:30 and stopped; GB1.Tue-Fri void); T3, T4, T5 MISSED. = 1/5 **20 %**. Stopped: **GB1** (1.33983, Mon 12:30 -> Mon 15:45).

Presentation: SS box and its zig-zag path drawn below where price spent Wed-Fri; four "GAP IN-FILL" labels stacked 1.333-1.343; Mon-Fri tags overprinted by candles at 1.340.

---

## Table — all 12 maps

| Map | E1 | E1 % | E2 | E2 % | E3 | E3 % |
|---|---|---|---|---|---|---|
| DXY 2026-07-06 | 4/4 | 100 | 5/5 | 100 | 7/7 | 100 |
| EURUSD 2026-07-06 | 5/6 | 83 | 5/5 | 100 | 7/7 | 100 |
| GBPUSD 2026-07-06 | 7/7 | 100 | 5/5 | 100 | 4/7 | 57 |
| DXY 2026-04-20 | 5/5 | 100 | 5/5 | 100 | 2/2 | 100 |
| EURUSD 2026-04-20 | 7/7 | 100 | 5/5 | 100 | 1/5 | 20 |
| GBPUSD 2026-04-20 | 3/6 | 50 | 3/5 | 60 | 0/9 | 0 |
| DXY 2026-10-05 | 4/6 | 67 | 5/5 | 100 | 2/10 | 20 |
| EURUSD 2026-10-05 | 5/7 | 71 | 5/5 | 100 | 1/8 | 13 |
| GBPUSD 2026-10-05 | 6/7 | 86 | 2/5 | 40 | 3/11 | 27 |
| DXY 2026-05-18 | 4/4 | 100 | 5/5 | 100 | 1/9 | 11 |
| EURUSD 2026-05-18 | 7/8 | 88 | 5/5 | 100 | 1/9 | 11 |
| GBPUSD 2026-05-18 | 6/7 | 86 | 0/5 | 0 | 1/5 | 20 |
| **Total, all 12 (pooled)** | **63/74** | **85.1** | **50/60** | **83.3** | **30/89** | **33.7** |
| **Total, 9 maps outside 2026-07-06** | **47/57** | **82.5** | **35/45** | **77.8** | **12/68** | **17.6** |

Mean of map percentages (for reference): all 12 — E1 85.9, E2 83.3, E3 39.9; outside 07-06 — E1 83.0, E2 77.8, E3 24.7.

The anchor week 2026-07-06 scores 18/21 on E3; the nine other maps score 12/68.

## The five defects that cost the most

1. **SS-range weeks get only two resting orders per day, at the far range edges, repeated as the same setup** (costs the most E3). The swing legs inside the range get no setup: DXY 10-05 (2/10: nothing at Mon 102.43 / 102.08 / 102.37, Tue 102.04 / 102.28, Thu 102.13 / 102.47), EURUSD 10-05 (1/8: nothing at 1.1186 Mon / Thu / Fri), GBPUSD 10-05 (3/11), DXY 05-18 (1/9), EURUSD 05-18 (1/9), GBPUSD 05-18 (1/5). The TPs sit at the opposite range edge, so fills at a real turn stay open: EURUSD 10-05 EU2.Wed long 1.11660 (TP 1.12476, Fri high 1.12427), EURUSD 05-18 EU3.Thu long 1.15815 (TP 1.16478, high 1.163), DXY 05-18 DX1.Thu short (TP 99.052, low 99.092), DXY 10-05 DX2.Fri long (TP 102.470, high 102.335).
2. **GBPUSD 2026-04-20: wrong week forecast and no usable setup** — E3 0/9, E2 3/5, E1 50 %. The engine expected BS down from a 1.3435-1.3502 SS box; price ranged 1.3448-1.3544 with nine swing legs. Setups at 1.34660 / 1.34818 / 1.34083 / 1.34557 never filled; the only fill, GB2 short 1.35163 (a Tue setup filled Mon 07:15), was stopped Mon 15:15 at 1.35387. The yellow path dives to ~1.3407 on Thu; the low was 1.34476.
3. **GBPUSD SS boxes broken by trending days (E2)** — GBPUSD 05-18 SS box 1.33047-1.34137 on all five days while price broke out Mon 15:00 and held 1.340-1.346 to Friday (0/5); GBPUSD 10-05 SS box 1.31799-1.32395 broken Tue 08:00 to 1.32856, Wed spent above it, Fri closes 1.3244-1.3246 (2/5); GBPUSD 04-20 Mon box top 1.35019 broken to 1.35444.
4. **No E1 object at the week's extremes / key turns** (E1 missing points): GBPUSD 04-20 1.35444 (Mon) and 1.35396 (Tue) above the top zone 1.35327; GBPUSD 10-05 Tue high 1.32856 (top drawing 1.3268); GBPUSD 05-18 1.3463 (Wed, Fri; top 1.34557); DXY 10-05 102.37 (Mon, Thu) and 102.433 (Mon); EURUSD 10-05 1.1186 (Mon / Thu / Fri) and 1.1172 (Thu); EURUSD 07-06 1.13911 (Wed); EURUSD 05-18 1.15882 (Fri). In three maps the facts header calls the zone window "the week's reach" while the week went beyond it.
5. **Stops / fills that don't match the drawn setup**: DXY 04-20 DX3 stopped in 15 minutes (Thu 00:00 -> 00:15, 4.5-pip stop at 98.660); DXY 05-18 DX1 is labelled E 99.409 / 3.2R but fills at the 99.355 front edge (Tue 13:15, Thu 07:15), so it is really ~1.9R; setups tagged for one day fill on another (GBPUSD 04-20 GB2 "Tue" filled Mon 07:15 and stopped; DXY 04-20 DX1 "Tue" filled Mon 15:15; GBPUSD 07-06 GB6 "Fri" filled Thu 06:15); GBPUSD 10-05 GB2 is 2.57R, under the 3.0R floor used to reject others. The single stops on the other maps are the same kind of issue: EURUSD 10-05 EU1.Tue (1.12585, stopped Tue 12:00 by 1.12767), DXY 05-18 DX2 (99.050, Mon 16:15), EURUSD 05-18 EU2 (1.16297, 75 min after the anchor), GBPUSD 05-18 GB1 (1.33983, Mon 15:45).

Presentation defects common to every map: dense stacks of horizontal lines (zones plus parts plus liquidity bands; e.g. GBPUSD 07-06 has 14 zones and 20 parts in 130 pips, DXY 04-20 about 20 lines between 98.0 and 98.6); stacked zones also make "reacted" easy to earn. Composite day tags run together ("Tue SS+RWL+BSWed BS", "Thu BS+RWLFri RWL") on the 07-06 and 04-20 maps. Setup labels overprint each other and the candles (EURUSD 07-06 Mon-Tue at 1.141-1.1435; DXY 07-06 Wed at 101.0-101.2). Option-strike labels overprint each other (EURUSD 05-18 at 1.1649).
