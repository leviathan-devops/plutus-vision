# G1 outside count 4 (fresh reviewer, strict)

Reviewer: outside reviewer with fresh context. Not the builder. No earlier count, no memory/, no tool code was read.
Inputs used: audit/G1_brief4.md, the 36 frames in evidence/s3d/ (every one opened), audit/g1_facts_d/*.txt (prices, times), context_management/oracle/golden_week.json (operator trades, 2026-07-06 only), 1H bars via `e1_tool/e1_data.py bars()` read-only (to check times, highs/lows, closes). All times UTC (the chart axis is UTC).

## Counting rules applied (so anyone can recount)

Rule G1 verbatim: "One verdict per drawing with its specific delta - zone: reacted (sharp rejection OR consolidation in / around it) / pierced like paper / not reached; day: forecast shape + direction + key zone vs that day's candles; setup: filled? TP before SL? Counting for a week: E1 = zones that reacted / (zones reached + obvious reaction points of the week that have no zone), and none bloated, bunched, floating or missing; E2 = days right / 5; E3 = obvious trades caught / obvious trades that existed (anchor week: his own trades; other weeks: every clean zone-to-zone move visible on the 1H chart, listed BEFORE looking at my setups), every stopped-out setup named."

How I applied it:
- Unit of E1 count = one line of the facts file "ENGINE 1 OBJECTS ON THE CHART" (pressure zones, gap in-fill, supply/demand, sweep zones, V1 liquidity bands). Amber option-strike lines are levels, not zones, and are not counted.
- Reached = a 1H wick of the forecast week (Mon 00:00 - Fri 21:00 UTC) entered the box (for a sweep zone: the box or its dotted reach).
- REACTED = within the box (or within ~3 pips DXY / ~5 pips FX beyond its far edge; for a sweep zone, within its dotted reach) price turned by at least ~10 pips DXY / ~15 pips FX, or stalled there for 3+ 1H candles. PIERCED = price crossed the whole box (and a sweep zone's reach) without such a turn or stall. A zone that reacted once and was later crossed counts as REACTED (first verdict wins) but the later piercing is noted.
- Obvious reaction points with no zone = the week's day highs/lows and every 1H swing that turned >= ~20 pips DXY / ~30 pips FX, with no Engine 1 box within ~3 pips DXY / ~5 pips FX. Each adds 1 to the denominator.
- E1 % = reacted / (reached + unzoned reaction points). The second clause ("none bloated, bunched, floating or missing") is reported as a separate gate PASS / FAIL per map; it is not folded into the %.
- E2: a day is RIGHT only if the forecast shape matches what the day's 1H candles did (canon definitions in the brief) AND the forecast direction is the day's direction (the main move; for a compound tag such as BS+WL+RWL the direction is that of the first leg, the later legs being the reversal the tag itself announces). A key zone or box placed away from the day's action is noted; it makes the day WRONG when the box does not overlap where the day traded.
- E3 (2026-07-06): obvious trades = the operator's trades in golden_week.json whose entry was reachable after Mon 06:00 UTC (Mon 02:00 New York). Other weeks: every clean zone-to-zone move >= ~25 pips DXY / ~40 pips FX visible on the 1H `_zones` frame, written down BEFORE opening `_all`/`_week`. CAUGHT = a setup of the same direction at that turn (entry within ~3 pips DXY / ~5 pips FX of the turn's zone, or within the zone the move started from) that filled and hit TP before SL (from the facts file's 15m result). A stopped setup is a loss even if price later reached its TP.

---

## Map 1 - DXY 2026-07-06 (anchor week)

Week action (1H, UTC): Mon 05:00 up from 100.95 to 101.145 (10:00), down to 100.838 (16-19:00); Tue low 100.803 (01:00), up to 101.196 (Tue 22:00); Wed 101.215 (01:00) -> 100.95 (07:00) -> 101.275 (13:00) -> 100.946; Thu 101.0 -> 100.786 (05:00) -> 101.039 (10:00) -> 100.806; Fri flush to 100.598 (02:00), recovery to 100.997.

### Step 1 - obvious trades (operator's trades in the window)
| # | operator trade | in window? |
|---|---|---|
| 1 | Mon LONG 100.945 / SL 100.905 / TP 101.115 | NO - price was at 100.945 only Mon 03:00-05:00 UTC (before Mon 06:00 UTC); after 06:00 Monday never came back to it before the TP. Excluded. |
| 2 | Mon SHORT 101.14 / 101.20 / 100.845 | yes |
| 3 | Tue LONG 100.845 / 100.77 / 101.19 | yes |
| 4 | Wed SHORT 101.19 / 101.25 / 100.975 | yes |
| 5 | Wed LONG 100.975 / 100.905 / 101.24 | yes |
| 6 | Wed SHORT 101.235 / 101.33 / 100.68 | yes |
| 7 | Thu SHORT 100.975 / 101.09 / (TP illegible) | yes |
| 8 | Fri LONG 100.615 / 100.545 / 100.94 | yes |
Obvious trades in window: 7.

### Step 2 - E1
| zone (facts) | verdict | delta |
|---|---|---|
| IP UPPER RESISTANCE 101.199-101.262 | REACTED | Wed high 101.275 (1.3 p beyond), sell-off to 100.946 |
| IP EQUILIBRIUM 100.985-101.077 | REACTED | Mon 05-08 stall inside; Wed/Thu chop around it |
| IP MID-RANGE SUPPORT 100.724-100.815 | REACTED | Tue low 100.803, Thu low 100.786 both bounced; Fri crossed it (flush) |
| IP KEY SUPPORT BAND 100.470-100.530 | not reached | week low 100.598 |
| GAP IN-FILL 100.599-100.659 | REACTED | Fri low 100.598 -> +40 p |
| 4H BoM supply 101.316-101.430 | not reached | |
| 1H MoM supply 101.314-101.360 | not reached | |
| 1H MoM supply 101.027-101.153 | REACTED | Mon top 101.145 inside -> -30 p (crossed Tue 22:00) |
| 1H Mitigated demand 100.825-100.851 | REACTED | Mon 16-22 stall at 100.838-100.85 |
| 1H BoM demand 100.654-100.748 | REACTED | Fri wick 5.6 p below, Fri 02-07 held 100.696+ |
| LSZ supply 101.382-101.432 / 101.380-101.430 / 101.344-101.394 (3) | not reached | |
| LSZ demand 101.152-101.202 (reach 101.052) | REACTED (weak) | Tue 22 - Wed 03 stall inside; then fell 10 p beyond its reach |
| LSZ demand 101.071-101.121 (reach 100.971) | REACTED | Wed 07:00 low 100.95 (2 p beyond reach) -> 101.275 |
| LSZ demand 101.049-101.099 (reach 100.949) | REACTED | Wed low 100.95 = reach -> +32 p |
| LSZ supply 100.978-101.028 (reach 101.128) | REACTED | Mon high 101.145 (1.7 p beyond reach) -> -30 p |
| LSZ supply 100.942-100.992 (reach 101.092) | REACTED | Tue 10:00 101.0 and Thu 04:00 101.0 -> -15/-21 p |
| LSZ demand 100.826-100.876 (reach 100.726) | REACTED | Tue 100.803 -> +39 p |
| LSZ demand 100.603-100.653 (reach 100.503) | REACTED | Fri 100.598 |
| LSZ demand 100.558-100.608 (reach 100.458) | REACTED | Fri 100.598 |
| band 101.372-101.432 | not reached | |
| band 101.245-101.305 | REACTED | Wed top 101.275 |
| band 101.067-101.127 | REACTED | Mon 08-14 stall |
| band 100.957-101.017 | REACTED | Wed 100.95 low / Thu chop |
| band 100.498-100.558 | not reached | |
Reached 18, reacted 18, pierced 0. Obvious turning points with no zone: none (101.145, 100.803, 101.215, 100.95, 101.275, 100.786, 101.039, 100.598, 100.997 all have a box).
**E1 = 18 / 18 = 100 %.** Gate (none bloated / bunched / floating): **FAIL - bunched/bloated.** 26 Engine 1 objects plus 3 strike lines cover every price from 100.47 to 101.53 without a gap (zones frame: the whole price axis is boxes); at 101.05-101.20 four boxes overlap (EQUILIBRIUM, 1H MoM supply, two LSZ demand, band). With that coverage a 100 % reaction rate is not evidence of selection. Three LSZ supply boxes 101.344-101.432 are within 4 p of each other.

### Step 3 - E2
| day | forecast | candles | verdict |
|---|---|---|---|
| Mon | SS range 100.724-101.262, key UPPER RESISTANCE | 100.838-101.145 inside the box, up then down | RIGHT |
| Tue | SS range 100.724-101.262 | 100.803 floor test -> 101.126, inside the box | RIGHT |
| Wed | SS+RWL+BS down, box 100.985-101.305 | 101.215 -> 100.95 -> 101.275 -> 100.946, close below open | RIGHT (key zone named "1H (Unmitigated) BoM" has no box inside 100.985-101.305) |
| Thu | BS down, box 100.968-101.247 | broke 100.985, surged to 100.786 (05:00), full retrace to 101.039, close 100.937 | RIGHT (shape+direction); box sits mostly above the day's range |
| Fri | BS+WL+RWL down, box 100.654-100.968, key MID-RANGE SUPPORT | flush to 100.598 then recovery to 100.997 | RIGHT |
**E2 = 5 / 5 = 100 %.**

### Step 4 - E3
| operator trade | setup | verdict |
|---|---|---|
| 2 Mon SHORT 101.14 | DX2 SHORT 101.138 / 101.183 / 100.825, filled Mon 09:45, TP Tue 01:30 | CAUGHT |
| 3 Tue LONG 100.845 | DX3 LONG 100.851 / 100.795 / 101.189, filled Mon 18:30, TP Tue 23:45 (Tue low 100.803 = 0.8 p above SL) | CAUGHT |
| 4 Wed SHORT 101.19 | DX5 SHORT 101.203 / 101.255 / 100.980, TP Wed 07:15 | CAUGHT |
| 5 Wed LONG 100.975 | DX6 LONG 100.980 / 100.906 / 101.235, TP Wed 09:00 | CAUGHT |
| 6 Wed SHORT 101.235 | DX4 SHORT 101.235 / 101.322 / 100.685, TP Fri 02:00 | CAUGHT |
| 7 Thu SHORT 100.975 | DX7 SHORT 100.980 / 101.077 / 100.685, TP Fri 02:00 (Thu high 101.071 = 0.6 p below SL) | CAUGHT |
| 8 Fri LONG 100.615 | DX8 LONG 100.628 / 100.548 / 100.940, TP Fri 14:00 | CAUGHT |
Stopped-out setups: none. DX1 SHORT 101.203 not filled (expired). **E3 = 7 / 7 = 100 %.**

### Step 5 - presentation
- History half: zone labels sit on top of the Jul 2-3 candles ("EQUILIBRIUM ZONE ...", "1H (Unmitigated) | MoM", "MID-RANGE SUPPORT ..."), and the stacked boxes tint every candle of the frame.
- Week frame: setup labels DX1/DX2/DX5/DX4 and the Mon/Tue/Wed day tags are drawn over Mon-Wed candles; the Fri tag "Fri BS+WL+RWL down 32%" is drawn over Friday's candles in purple and is hard to read; the DX7 label "if DX4" overlaps the Thu candles.

## Map 2 - EURUSD 2026-07-06 (anchor week)

Week action (1H, UTC): Mon 1.1433 -> 1.14083 (Mon 09-15) -> 1.1448 (Mon 22 / Tue 01); Tue down to 1.14001 (Tue 22); Wed 1.13983 (01) -> 1.14315 (07) -> 1.13911 (13) -> 1.14303; Thu 1.14199 -> 1.14494 (05) -> 1.14209 (10) -> 1.1446; Fri spike 1.14608 (01-02) -> 1.14114 (19).

### Step 1 - obvious trades (operator's trades in the window)
| # | operator trade | in window? |
|---|---|---|
| 1 | Mon SHORT 1.14322 / 1.14408 / 1.14103 | NO - 1.14322 traded only Mon 00:00-04:00 UTC; after 06:00 the high was 1.14288 until the TP level traded (Mon 09:00). Excluded. |
| 2 | Mon LONG 1.14106 / 1.14039 / 1.14442 | yes |
| 3 | Tue SHORT 1.14441 / 1.14505 / 1.14004 | yes |
| 4 | Wed LONG 1.14012 / 1.13964 / 1.14276 | yes |
| 5 | Wed SHORT 1.14277 / 1.14325 / 1.1395 | yes |
| 6 | Wed LONG 1.13953 / 1.13868 / 1.14544 | yes |
| 7 | Thu LONG 1.14233 / 1.14183 / 1.14544 (reinforcement of 6) | yes |
| 8 | Fri SHORT 1.14578 / 1.14649 / 1.14205 | yes |
Obvious trades in window: 7.

### Step 2 - E1
| zone (facts) | verdict | delta |
|---|---|---|
| IP UPPER RESISTANCE 1.14444-1.14533 | REACTED | Mon 22-Tue 01 top 1.1448 -> -48 p; Thu 1.14494 -> -29 p |
| IP MID-RANGE SUPPORT 1.13977-1.14053 | REACTED | Tue 22 1.14001 / Wed 01 1.13983 -> +33 p; Wed 13:00 wick 6.6 p below |
| GAP 1.14777-1.14837 | not reached | |
| GAP 1.14593-1.14653 | REACTED | Fri 1.14608 -> -49 p |
| GAP 1.14220-1.14280 | REACTED | Mon 05-08 stall, Thu 10 low 1.14209 bounce |
| 1H BoM supply 1.14738-1.14807 | not reached | |
| 1H Mit 4x supply 1.14601-1.14677 | REACTED | Fri 1.14608 |
| 4H Mit 2x supply 1.14475-1.14635 | REACTED | Tue 1.1448, Thu 1.14494, Fri 1.14608 all turned |
| 1H BoM supply 1.14375-1.14421 | REACTED | Mon 19-Tue 03 stall; Tue 10-13 highs 1.14421 / 1.14418 -> down |
| 1H MoM demand 1.14004-1.14147 | REACTED | Mon 1.14083 -> +37 p |
| 1H BoM demand 1.13815-1.13886 | not reached | Wed low 1.13911 turned 2.5 p above it |
| 4H BoM demand 1.13721-1.13832 | not reached | |
| LSZ supply 1.14678-1.14728 | not reached | |
| LSZ supply 1.14573-1.14623 (reach 1.14723) | REACTED | Fri 1.14608 |
| LSZ supply 1.14360-1.14410 (reach 1.1451) | REACTED | Mon/Tue tops 1.1448 within reach |
| LSZ supply 1.14316-1.14366 (reach 1.14466) | REACTED | Tue 10-13 1.1442 -> down |
| LSZ supply 1.14255-1.14305 (reach 1.14405) | REACTED | Wed 07 1.14315 -> -40 p |
| LSZ supply 1.14178-1.14228 (reach 1.14328) | REACTED | Wed 07 1.14315 within reach |
| LSZ demand 1.14206-1.14256 (reach 1.14106) | REACTED | Mon 1.14083 (2.3 p beyond reach) -> up |
| LSZ demand 1.13826-1.13876 / 1.13790-1.13840 | not reached | |
| band 1.14658-1.14728 | not reached | |
| band 1.14269-1.14339 | REACTED | Wed 07 1.14315, Thu chop |
| band 1.14108-1.14178 | REACTED | Wed 19 1.14141, Fri 1.14114 |
| band 1.13810-1.13880 | not reached | |
Reached 16, reacted 16, pierced 0. Unzoned turning points: none (Wed low 1.13911 is 2.5 p above the 1H BoM demand).
**E1 = 16 / 16 = 100 %.** Gate: **FAIL - bunched/bloated.** 25 objects cover 1.1369-1.1484 with no gap; between 1.1418 and 1.1445 eight boxes overlap (GAP 1.1422, 1H BoM supply, three LSZ supply, LSZ demand, band, upper edge of 1H MoM demand). Every turn of the week lands in some box by construction.

### Step 3 - E2
| day | forecast | candles | verdict |
|---|---|---|---|
| Mon | SS range 1.13977-1.14533 | 1.14083-1.14449, down then up, inside the box | RIGHT |
| Tue | SS range 1.13977-1.14533 | ceiling 1.1448 then down to 1.1408, inside | RIGHT |
| Wed | SS+RWL+BS up, box 1.13902-1.14339, key 4H Mit 2x MoM | 1.1408 -> 1.14315 -> 1.13911 -> 1.14289 (BS up from 16:00) | RIGHT (key zone 1.14475-1.14635 is outside the day's box) |
| Thu | BS up, box 1.13962-1.14248 | surge 1.14256 -> 1.14494 (04-05), retrace, close 1.14299 | RIGHT on shape + direction; box sits below the day (overlap only 1.1414-1.1425) |
| Fri | BS+WL+RWL up, box 1.14248-1.14635, key UPPER RESISTANCE | spike to 1.14608, reject, down to 1.14114 | RIGHT |
**E2 = 5 / 5 = 100 %.**

### Step 4 - E3
| operator trade | setup | verdict |
|---|---|---|
| 2 Mon LONG 1.14106 | EU4 LONG 1.14095 / 1.14037 / 1.14434, filled Mon 10:00, TP Mon 18:45 | CAUGHT |
| 3 Tue SHORT 1.14441 | EU1 SHORT 1.14442 / 1.14508 / 1.14063, filled Mon 18:30, TP Tue 21:15 | CAUGHT |
| 4 Wed LONG 1.14012 | EU7 LONG 1.14018 / 1.13960 / 1.14269, filled Tue 21:30, TP Wed 07:15 | CAUGHT |
| 5 Wed SHORT 1.14277 | EU5 SHORT 1.14269 / 1.14369 / 1.13940, filled Wed 07:15, TP Wed 11:30 | CAUGHT |
| 6 Wed LONG 1.13953 | EU6 LONG 1.13940 / 1.13872 / 1.14555, filled Wed 11:30, TP Fri 02:00 | CAUGHT |
| 7 Thu LONG 1.14233 (Thu 10:00 dip 1.14209) | none at that turn. EU8 LONG 1.14164 filled Wed 21:00 at the Wed-evening dip (6.9 p away, a different turn) | MISSED |
| 8 Fri SHORT 1.14578 | EU9 SHORT 1.14598 / 1.14653 / 1.14239, filled Fri 02:15, TP Fri 12:45 | CAUGHT |
Stopped-out setups: **EU2** SHORT 1.14385 (filled Mon 17:15, stopped Mon 21:45 at 1.14451); **EU4 re-armed** LONG 1.14095 (filled Tue 19:15, stopped Tue 21:30). EU3 not filled. Extras that won: EU8, EU10.
**E3 = 6 / 7 = 86 %.**

### Step 5 - presentation
- Boxes fill the entire chart height; the history labels ("UPPER RESISTANCE", "LSZ supply-side | sweep to 1.14510", "GAP IN-FILL", "1H (Unmitigated) | MoM") sit over the Jul 2-3 candles.
- Week frame: EU1/EU2/EU4/EU3/EU7/EU5 labels overlap the Mon-Wed candles; "EU10 Ladder L 3.5R if E" is clipped at the right edge; the purple "Fri BS+WL+RWL up 32%" tag sits over the Friday spike candles.
