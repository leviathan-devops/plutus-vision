# G1 outside count 4 (fresh reviewer, strict)

Reviewer: outside reviewer with fresh context. Not the builder. No earlier count, no memory/, no tool code was read.
Inputs used: audit/G1_brief4.md, the 36 frames in evidence/s3d/ (every one opened), audit/g1_facts_d/*.txt (prices, times), context_management/oracle/golden_week.json (operator trades, 2026-07-06 only), 1H bars via `e1_tool/e1_data.py bars()` read-only (to check times, highs/lows, closes). All times UTC (the chart axis is UTC).

## Counting rules applied (so anyone can recount)

Rule G1 verbatim: "One verdict per drawing with its specific delta - zone: reacted (sharp rejection OR consolidation in / around it) / pierced like paper / not reached; day: forecast shape + direction + key zone vs that day's candles; setup: filled? TP before SL? Counting for a week: E1 = zones that reacted / (zones reached + obvious reaction points of the week that have no zone), and none bloated, bunched, floating or missing; E2 = days right / 5; E3 = obvious trades caught / obvious trades that existed (anchor week: his own trades; other weeks: every clean zone-to-zone move visible on the 1H chart, listed BEFORE looking at my setups), every stopped-out setup named."

How I applied it:
- Unit of E1 count = one line of the facts file "ENGINE 1 OBJECTS ON THE CHART" (pressure zones, gap in-fill, supply/demand, sweep zones, V1 liquidity bands). Amber option-strike lines are levels, not zones, and are not counted.
- Forecast week = from the anchor (Mon 06:00 UTC = Mon 02:00 New York) to Friday's close; candles before the anchor are history and do not count for or against any engine.
- Reached = a 1H wick of the forecast week entered the box (for a sweep zone: the box or its dotted reach).
- Verdict = what price did at its FIRST contact with the drawing after the anchor (strict; later visits are not used to rescue a zone that was crossed, and a zone that reacted first keeps REACTED even if crossed later). REACTED = before price got past the far edge (+ ~3 p DXY / ~5 p FX; for a sweep zone, past its dotted reach + that tolerance) it either turned >= 10 p DXY / >= 15 p FX from its extreme, or 3+ 1H candles traded in the box (consolidation); a single candle that wicked past the far edge by at most 10 p and CLOSED back inside counts as a sharp rejection (canon: sweeps 0.05-0.10 beyond the extreme). PIERCED = crossed beyond that without any of these. Times / highs / lows of first contact were read from the 1H bars (read-only `bars()`), with every case cross-checked on the frames; the table gives the hour so anyone can recount.
- Obvious reaction points with no zone = the week's day highs/lows and every 1H swing that turned >= ~20 pips DXY / ~30 pips FX, with no Engine 1 box within ~3 pips DXY / ~5 pips FX. Each adds 1 to the denominator.
- E1 % = reacted / (reached + unzoned reaction points). The second clause ("none bloated, bunched, floating or missing") is reported as a separate gate PASS / FAIL per map; it is not folded into the %.
- E2: a day is RIGHT only if the forecast shape matches what the day's 1H candles did (canon definitions in the brief) AND the forecast direction is the day's direction (the main move; for a compound tag such as BS+WL+RWL the direction is that of the first leg, the later legs being the reversal the tag itself announces). For an SS (range) day the forecast bounds are part of the shape (canon: range bounded by the zones above and below): the day is RIGHT only if its 1H closes stay within ~10 p of the forecast bounds (wicks beyond = sweeps are allowed); 1H closes more than ~10 p outside the range box = the range did not hold = WRONG. The key zone counts as right when the day's turn or target is at it. A day box drawn away from where the day traded is listed as a presentation defect, not a WRONG day (G1 names shape + direction + key zone only).
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
| zone (facts) | verdict at first contact | delta (UTC hour) |
|---|---|---|
| IP UPPER RESISTANCE 101.199-101.262 | REACTED | first contact Wed 01 from below; reacted turn Wed 02 |
| IP EQUILIBRIUM ZONE 100.985-101.077 | REACTED | first contact Mon 06 from below; reacted stall Mon 08 |
| IP MID-RANGE SUPPORT 100.724-100.815 | REACTED | first contact Tue 01 from above; reacted turn Tue 05 |
| IP KEY SUPPORT BAND 100.47-100.53 | not reached | |
| GAP 100.599-100.659 | REACTED | first contact Fri 02 from above; reacted turn Fri 03 |
| 4H (Unmitigated) BoM supply 101.316-101.43 | not reached | |
| 1H (Unmitigated) MoM supply 101.314-101.36 | not reached | |
| 1H (Unmitigated) MoM supply 101.027-101.153 | REACTED | first contact Mon 06 from below; reacted stall Mon 08 |
| 1H (Mitigated 2x) MoM demand 100.825-100.851 | REACTED | first contact Mon 18 from above; reacted stall Mon 22 |
| 1H (Unmitigated) BoM demand 100.654-100.748 | PIERCED | first contact Fri 01 from above; pierced Fri 02 (5.6 p past far edge, close beyond) |
| LSZ supply 101.382-101.432 (reach 101.532) | not reached | |
| LSZ supply 101.38-101.43 (reach 101.53) | not reached | |
| LSZ supply 101.344-101.394 (reach 101.494) | not reached | |
| LSZ demand 101.152-101.202 (reach 101.052) | REACTED | first contact Mon 06 from below; reacted stall Mon 08 |
| LSZ demand 101.071-101.121 (reach 100.971) | REACTED | first contact Mon 06 from below; reacted stall Mon 08 |
| LSZ demand 101.049-101.099 (reach 100.949) | REACTED | first contact Mon 06 from below; reacted stall Mon 08 |
| LSZ supply 100.978-101.028 (reach 101.128) | REACTED | first contact Mon 06 from below; reacted stall Mon 08 |
| LSZ supply 100.942-100.992 (reach 101.092) | REACTED | first contact Mon 06 from below; reacted stall Mon 08 |
| LSZ demand 100.826-100.876 (reach 100.726) | REACTED | first contact Mon 18 from above; reacted stall Mon 20 |
| LSZ demand 100.603-100.653 (reach 100.503) | REACTED | first contact Fri 02 from above; reacted turn Fri 03 |
| LSZ demand 100.558-100.608 (reach 100.458) | REACTED | first contact Fri 02 from above; reacted turn Fri 03 |
| band 101.372-101.432 | not reached | |
| band 101.245-101.305 | REACTED | first contact Wed 11 from below; reacted turn Wed 12 |
| band 101.067-101.127 | REACTED | first contact Mon 06 from below; reacted stall Mon 08 |
| band 100.957-101.017 | REACTED | first contact Mon 06 from above; reacted turn Mon 07 |
| band 100.498-100.558 | not reached | |
Reached 18, reacted 17, pierced 1. Obvious turning points with no zone: none (101.145, 100.803, 101.215, 100.95, 101.275, 100.786, 101.039, 100.598, 100.997 all have a box).
**E1 = 17 / (18 + 0) = 94 %.** Gate: **FAIL - bunched/bloated.** 26 Engine 1 objects plus 3 strike lines cover every price from 100.47 to 101.53 without a gap (zones frame: the whole price axis is boxes); at 101.05-101.20 four boxes overlap (EQUILIBRIUM, 1H MoM supply, two LSZ demand, band). With that coverage a high reaction rate is not evidence of selection. Three LSZ supply boxes 101.344-101.432 are within 4 p of each other.

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
| zone (facts) | verdict at first contact | delta (UTC hour) |
|---|---|---|
| IP UPPER RESISTANCE 1.14444-1.14533 | REACTED | first contact Mon 18 from below; reacted stall Mon 22 |
| IP MID-RANGE SUPPORT 1.13977-1.14053 | REACTED | first contact Tue 21 from above; reacted stall Tue 23 |
| GAP 1.14777-1.14837 | not reached | |
| GAP 1.14593-1.14653 | REACTED | first contact Fri 02 from below; reacted turn Fri 04 |
| GAP 1.1422-1.1428 | REACTED | first contact Mon 06 from above; reacted wick-rejection Mon 07 (5.4 p wick past far edge, closed back) |
| 1H (Unmitigated) BoM supply 1.14738-1.14807 | not reached | |
| 1H (Mitigated 4x) MoM supply 1.14601-1.14677 | REACTED | first contact Fri 02 from below; reacted turn Fri 04 |
| 4H (Mitigated 2x) MoM supply 1.14475-1.14635 | REACTED | first contact Mon 23 from below; reacted turn Tue 05 |
| 1H (Unmitigated) BoM supply 1.14375-1.14421 | REACTED | first contact Mon 17 from below; reacted stall Mon 19 |
| 1H (Unmitigated) MoM demand 1.14004-1.14147 | REACTED | first contact Mon 09 from above; reacted stall Mon 11 |
| 1H (Unmitigated) BoM demand 1.13815-1.13886 | not reached | |
| 4H (Unmitigated) BoM demand 1.13721-1.13832 | not reached | |
| LSZ supply 1.14678-1.14728 (reach 1.14828) | not reached | |
| LSZ supply 1.14573-1.14623 (reach 1.14723) | REACTED | first contact Fri 02 from below; reacted turn Fri 04 |
| LSZ supply 1.1436-1.1441 (reach 1.1451) | REACTED | first contact Mon 17 from below; reacted stall Mon 19 |
| LSZ supply 1.14316-1.14366 (reach 1.14466) | REACTED | first contact Mon 16 from below; reacted stall Mon 18 |
| LSZ supply 1.14255-1.14305 (reach 1.14405) | REACTED | first contact Mon 06 from below; reacted stall Mon 08 |
| LSZ supply 1.14178-1.14228 (reach 1.14328) | REACTED | first contact Mon 06 from above; reacted stall Mon 08 |
| LSZ demand 1.14206-1.14256 (reach 1.14106) | REACTED | first contact Mon 06 from above; reacted stall Mon 08 |
| LSZ demand 1.13826-1.13876 (reach 1.13726) | not reached | |
| LSZ demand 1.1379-1.1384 (reach 1.1369) | not reached | |
| band 1.14658-1.14728 | not reached | |
| band 1.14269-1.14339 | REACTED | first contact Mon 06 from below; reacted stall Mon 08 |
| band 1.14108-1.14178 | REACTED | first contact Mon 07 from above; reacted stall Mon 09 |
| band 1.1381-1.1388 | not reached | |
Reached 16, reacted 16, pierced 0. Unzoned turning points: none (Wed low 1.13911 is 2.5 p above the 1H BoM demand).
**E1 = 16 / (16 + 0) = 100 %.** Gate: **FAIL - bunched/bloated.** 25 objects cover 1.1369-1.1484 with no gap; between 1.1418 and 1.1445 eight boxes overlap (GAP 1.1422, 1H BoM supply, three LSZ supply, LSZ demand, band, upper edge of 1H MoM demand). Every turn of the week lands in some box by construction.

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

## Map 3 - GBPUSD 2026-07-06 (anchor week)

Week action (1H, UTC): Mon chop 1.3329-1.3352 until 13:00, rally to 1.34013 (Mon 22); Tue 1.34015 -> 1.3343 (Tue 22); Wed 1.3366 (06) -> 1.33222 (08) -> 1.34104 (17); Thu 1.33866 -> 1.34308 (05) -> 1.33807 (11) -> 1.34249; Fri 1.34517 (02) -> 1.33918 (14), close 1.33968.

### Step 1 - obvious trades (operator's trades in the window)
| # | operator trade | in window? |
|---|---|---|
| 1 | Mon LONG 1.33331 / 1.33224 / 1.33941 | yes (Mon 06:00-07:00 low 1.33301 / 1.33286 - after 06:00 UTC) |
| 2 | Mon SHORT 1.33934 / 1.34075 / 1.33347 | yes |
| 3 | Wed LONG 1.3333 / 1.33199 / 1.34246 | yes |
| 4 | Wed LONG 1.33629 / 1.33522 / 1.34246 (reinforcement of 3) | yes |
| 5 | Thu SHORT 1.34246 / 1.3436 / 1.33882 | yes |
| 6 | Thu LONG 1.33829 / 1.3375 / 1.34485 | yes |
| 7 | Fri SHORT 1.34481 / 1.34587 / 1.34021 | yes |
Obvious trades in window: 7.

### Step 2 - E1
| zone (facts) | verdict at first contact | delta (UTC hour) |
|---|---|---|
| IP RESISTANCE CEILING 1.34484-1.34548 | REACTED | first contact Fri 02 from below; reacted turn Fri 04 |
| IP UPPER RESISTANCE 1.33933-1.34005 | REACTED | first contact Mon 18 from below; reacted turn Mon 21 |
| IP UPPER RESISTANCE 1.33643-1.33717 | PIERCED | first contact Mon 15 from below; pierced Mon 17 (12.5 p past far edge, close beyond) |
| IP UPPER RESISTANCE 1.33435-1.33521 | REACTED | first contact Mon 07 from below; reacted turn Mon 08 |
| IP MID-RANGE SUPPORT 1.33225-1.33285 | REACTED | first contact Wed 09 from above; reacted turn Wed 09 |
| IP KEY SUPPORT BAND 1.3297-1.33046 | not reached | |
| IP KEY SUPPORT BAND 1.32789-1.32877 | not reached | |
| GAP 1.34234-1.34294 | REACTED | first contact Thu 06 from below; reacted turn Thu 07 |
| GAP 1.34029-1.34089 | REACTED | first contact Wed 17 from below; reacted turn Wed 17 |
| GAP 1.33744-1.33804 | PIERCED | first contact Mon 16 from below; pierced Mon 18 (16.7 p past far edge, close beyond) |
| 1H (Unmitigated) BoM supply 1.34502-1.34599 | REACTED | first contact Fri 02 from below; reacted turn Fri 04 |
| 4H (Unmitigated) BoM supply 1.34264-1.3434 | REACTED | first contact Thu 06 from below; reacted turn Thu 07 |
| 4H (Unmitigated) MoM supply 1.34035-1.34162 | REACTED | first contact Wed 17 from below; reacted turn Wed 17 |
| 1H (Unmitigated) MoM supply 1.33941-1.34032 | REACTED | first contact Mon 18 from below; reacted turn Mon 21 |
| 1H (Unmitigated) BoM supply 1.33623-1.33764 | PIERCED | first contact Mon 15 from below; pierced Mon 17 (7.8 p past far edge, close beyond) |
| 1H (Unmitigated) MoM supply 1.33544-1.33582 | PIERCED | first contact Mon 13 from below; pierced Mon 15 (10.0 p past far edge, close beyond) |
| 1H (Unmitigated) MoM demand 1.33082-1.33333 | REACTED | first contact Mon 06 from above; reacted turn Mon 07 |
| 1H (Unmitigated) MoM demand 1.32862-1.32928 | not reached | |
| 4H (Unmitigated) MoM demand 1.32639-1.32835 | not reached | |
| 1H (Unmitigated) BoM demand 1.32744-1.328 | not reached | |
| LSZ supply 1.33796-1.33846 (reach 1.33946) | REACTED | first contact Mon 17 from below; reacted stall Mon 19 |
| LSZ supply 1.3376-1.3381 (reach 1.3391) | PIERCED | first contact Mon 16 from below; pierced Mon 18 (6.1 p past far edge, close beyond) |
| LSZ supply 1.33516-1.33566 (reach 1.33666) | REACTED | first contact Mon 12 from below; reacted stall Mon 14 |
| LSZ demand 1.33341-1.33391 (reach 1.33241) | REACTED | first contact Mon 06 from above; reacted turn Mon 07 |
| LSZ demand 1.3334-1.3339 (reach 1.3324) | REACTED | first contact Mon 06 from above; reacted turn Mon 07 |
| LSZ supply 1.32871-1.32921 (reach 1.33021) | not reached | |
| LSZ supply 1.32717-1.32767 (reach 1.32867) | not reached | |
| band 1.3454-1.3463 | not reached | |
| band 1.34386-1.34476 | REACTED | first contact Fri 01 from below; reacted stall Fri 03 |
| band 1.34145-1.34235 | PIERCED | first contact Thu 06 from below; pierced Thu 06 (7.3 p past far edge, close beyond) |
| band 1.33976-1.34066 | REACTED | first contact Mon 23 from below; reacted stall Tue 02 |
| band 1.33715-1.33805 | PIERCED | first contact Mon 16 from below; pierced Mon 18 (16.6 p past far edge, close beyond) |
| band 1.33583-1.33673 | PIERCED | first contact Mon 14 from below; pierced Mon 16 (9.3 p past far edge, close beyond) |
| band 1.33406-1.33496 | REACTED | first contact Mon 06 from below; reacted turn Mon 08 |
| band 1.33155-1.33245 | REACTED | first contact Wed 09 from above; reacted turn Wed 09 |
| band 1.32932-1.33022 | not reached | |
Reached 27, reacted 19, pierced 8. Unzoned turning points: none.
**E1 = 19 / (27 + 0) = 70 %.** Gate: **FAIL - bunched/bloated.** 36 objects (7 IP, 3 gap, 10 S/D, 7 LSZ, 9 bands) inside 1.326-1.346; the zones frame is boxes from top to bottom, with labels printed on top of each other (UPPER RESISTANCE / 1H MoM at 1.3400; GAP / 1H BoM / UPPER RESISTANCE at 1.3375; KEY SUPPORT / 1H BoM / 4H MoM at 1.3280). Two identical LSZ demand boxes (1.33341 and 1.33340).

### Step 3 - E2
| day | forecast | candles | verdict |
|---|---|---|---|
| Mon | SS range 1.33082-1.34032, key 1H MoM | floor chop 1.3329-1.3352, then floor -> ceiling 1.34013, inside the box | RIGHT |
| Tue | SS range 1.33082-1.34032 | ceiling 1.34015 -> 1.33487, inside | RIGHT |
| Wed | SS+RWL+BS up, box 1.33155-1.33496, key 4H BoM | 1.3366 -> 1.33222 (whiplash down) -> 1.34104 (BS up), close up | RIGHT |
| Thu | BS up, box 1.33270-1.33825, key 4H BoM | surge 1.33959 -> 1.34308 into the 4H BoM supply, drop to 1.33807, back to 1.3422 | RIGHT (shape, direction, key zone); the day box sits under the day (overlap = one wick, 1.33799-1.33825) |
| Fri | BS+WL+RWL up, box 1.33825-1.34340 | spike 1.34517, reject to 1.33918 | RIGHT |
**E2 = 5 / 5 = 100 %.**

### Step 4 - E3
| operator trade | setup | verdict |
|---|---|---|
| 1 Mon LONG 1.33331 | GB2 LONG 1.33333 / 1.33235 / 1.33941, filled Mon 06:15, TP Mon 18:45 | CAUGHT |
| 2 Mon SHORT 1.33934 | GB1 SHORT 1.33959 / 1.34062 / 1.33333, filled Mon 18:45, TP Wed 09:00 | CAUGHT |
| 3 Wed LONG 1.3333 | GB4 LONG 1.33255 / 1.33125 / 1.34254, filled Wed 09:00, TP Thu 06:15 | CAUGHT (entry 7.5 p deeper than his, inside the same 1H MoM demand) |
| 4 Wed LONG 1.33629 (reinforcement) | no setup; GB5 "if GB4" LONG 1.33473 never filled | MISSED |
| 5 Thu SHORT 1.34246 | GB6 SHORT 1.34254 / 1.34370 / 1.33888, filled Thu 06:15, TP Thu 11:15 | CAUGHT |
| 6 Thu LONG 1.33829 (Thu 11:00 low 1.33807) | GB7 LONG 1.33888 is labelled Fri and "not filled inside its bracket" - no order at Thursday's dip | MISSED |
| 7 Fri SHORT 1.34481 (Fri 1.34517 top) | no setup at the RESISTANCE CEILING / 1H BoM supply | MISSED |
Stopped-out setups: none. GB3 void, GB5 and GB7 not filled.
**E3 = 4 / 7 = 57 %.**

### Step 5 - presentation
- Zones frame: label-on-label collisions at 1.3400, 1.3375, 1.3420 and 1.3280 (two or three white labels printed on the same line); boxes cover the whole chart.
- All/week frames: "GB3 RWL S 4.1R", "Wed SS+RWL+BS" and "GB4 BS L 7.7R" overlap each other on Wed; the purple Fri tag is unreadable over the Friday candles; "GB7 Ladder L 4.0R if GB" is clipped at the right edge.

## Map 4 - DXY 2026-04-20

Week action (1H, UTC): Mon 98.27-98.395 (Mon 04-06) -> 98.006 (Mon 15), stall 98.01-98.16 into Tue 06; Tue up to 98.309, dip 98.123 (13), surge 98.567 (17); Wed 98.211 (05) -> 98.643 (21); Thu 98.737 -> 98.534 (14) -> 98.939 (17); Fri 98.915 (02) -> 98.489 (20). (The spike to 99.33 at the right edge is after Friday's close and is outside the week.)

### Step 1 - obvious trades (written from the `_zones` frame before opening any setup)
Per the brief (S3) the counted obvious trades of this map are the operator's two real trades:
| # | trade | turn |
|---|---|---|
| A | LONG 98.02 / SL 97.87 / TP 98.77 | Mon 15:00 low 98.006 at GAP 97.988-98.048 / 1H MoM demand -> Thu 98.939 |
| B | LONG 98.29 / SL 98.185 / TP 98.77 | Wed 05:00 low 98.211 at GAP 98.220-98.280 -> Thu 98.939 |
For information only (not in the %), the other clean zone-to-zone moves visible on the 1H frame: (c) Mon SHORT 98.395 (1H MoM supply 98.402) -> 98.006, -39 p; (d) Tue SHORT 98.567 (UPPER RESISTANCE 98.456-98.541) -> 98.211, -36 p; (e) Fri SHORT 98.915 (4H BoM supply 98.884) -> 98.489, -43 p.

### Step 2 - E1
| zone (facts) | verdict at first contact | delta (UTC hour) |
|---|---|---|
| IP UPPER RESISTANCE 98.939-99.005 | REACTED | first contact Thu 17 from below; reacted turn Thu 17 |
| IP UPPER RESISTANCE 98.456-98.541 | REACTED | first contact Tue 17 from below; reacted turn Tue 17 |
| IP MID-RANGE SUPPORT 98.058-98.145 | REACTED | first contact Mon 13 from above; reacted turn Mon 14 |
| IP KEY SUPPORT BAND 97.725-97.799 | not reached | |
| GAP 98.806-98.866 | REACTED | first contact Thu 17 from below; reacted wick-rejection Thu 17 (7.3 p wick past far edge, closed back) |
| GAP 98.667-98.727 | REACTED | first contact Thu 00 from below; reacted turn Thu 00 |
| GAP 98.22-98.28 | REACTED | first contact Mon 06 from above; reacted turn Mon 07 |
| GAP 97.988-98.048 | REACTED | first contact Mon 15 from above; reacted stall Mon 17 |
| 4H (Unmitigated) BoM supply 98.884-99.031 | REACTED | first contact Thu 17 from below; reacted turn Thu 17 |
| 1H (Unmitigated) MoM supply 98.675-98.845 | REACTED | first contact Thu 00 from below; reacted turn Thu 00 |
| 1H (Unmitigated) MoM supply 98.402-98.439 | REACTED | first contact Tue 16 from below; reacted turn Tue 17 |
| 1H (Unmitigated) MoM demand 97.937-98.045 | REACTED | first contact Mon 15 from above; reacted stall Mon 17 |
| 1H (Unmitigated) BoM demand 97.632-97.828 | not reached | |
| 4H (Unmitigated) BoM demand 97.576-97.728 | not reached | |
| LSZ supply 98.389-98.439 (reach 98.539) | REACTED | first contact Mon 06 from below; reacted turn Mon 06 |
| LSZ supply 98.345-98.395 (reach 98.495) | REACTED | first contact Mon 06 from below; reacted turn Mon 06 |
| LSZ demand 98.364-98.414 (reach 98.264) | REACTED | first contact Mon 06 from below; reacted turn Mon 06 |
| LSZ supply 98.242-98.292 (reach 98.392) | REACTED | first contact Mon 06 from below; reacted turn Mon 06 |
| LSZ supply 98.241-98.291 (reach 98.391) | REACTED | first contact Mon 06 from below; reacted turn Mon 06 |
| LSZ supply 98.235-98.285 (reach 98.385) | REACTED | first contact Mon 06 from below; reacted turn Mon 06 |
| LSZ demand 98.261-98.311 (reach 98.161) | REACTED | first contact Mon 06 from above; reacted turn Mon 07 |
| LSZ demand 98.005-98.055 (reach 97.905) | REACTED | first contact Mon 15 from above; reacted stall Mon 17 |
| LSZ demand 97.969-98.019 (reach 97.869) | REACTED | first contact Mon 15 from above; reacted turn Mon 18 |
| LSZ demand 97.832-97.882 (reach 97.732) | not reached | |
| LSZ demand 97.632-97.682 (reach 97.532) | not reached | |
| band 98.903-98.967 | REACTED | first contact Thu 17 from below; reacted turn Thu 17 |
| band 98.804-98.868 | REACTED | first contact Thu 17 from below; reacted wick-rejection Thu 17 (7.1 p wick past far edge, closed back) |
| band 98.689-98.753 | REACTED | first contact Thu 00 from below; reacted turn Thu 00 |
| band 98.561-98.625 | REACTED | first contact Tue 17 from below; reacted turn Tue 17 |
| band 98.461-98.525 | REACTED | first contact Tue 17 from below; reacted wick-rejection Tue 17 (4.2 p wick past far edge, closed back) |
| band 98.3-98.364 | REACTED | first contact Mon 06 from below; reacted wick-rejection Mon 06 (3.1 p wick past far edge, closed back) |
| band 98.182-98.246 | REACTED | first contact Mon 07 from above; reacted turn Mon 07 |
| band 98.014-98.078 | REACTED | first contact Mon 15 from above; reacted stall Mon 17 |
| band 97.92-97.984 | not reached | |
| band 97.768-97.832 | not reached | |
| band 97.666-97.73 | not reached | |
Reached 28, reacted 28, pierced 0. Unzoned turning points: none.
**E1 = 28 / (28 + 0) = 100 %.** Gate: **FAIL - bunched/bloated.** 36 objects between 97.53 and 99.03; between 98.18 and 98.44 there are 6 LSZ + 1 gap + 1H MoM supply + 2 bands stacked (three LSZ supply boxes 98.235 / 98.241 / 98.242 are within 0.7 p of each other and should be one box); the labels "LSZ supply-side | sweep to 98.539" and "LSZ demand-side | sweep to 98.264" print over each other at 98.40 in the history half.

### Step 3 - E2
| day | forecast | candles | verdict |
|---|---|---|---|
| Mon | SS range 97.937-98.439, key 1H MoM | ceiling 98.395 -> floor 98.006, stall, inside the box | RIGHT |
| Tue | SS+RWL+BS up, key 4H BoM | range 98.07-98.16, up to 98.309, dip 98.123, surge 98.567, close up | RIGHT |
| Wed | BS up, box 98.064-98.522 | dip 98.211 then surge to 98.643, close 98.616 | RIGHT |
| Thu | BS+RWL up, box 98.522-98.884 | 98.534 -> spike 98.939 -> 98.77, close 98.826 | RIGHT |
| Fri | RWL down, box 98.402-98.801 | steady decline 98.915 -> 98.489, closed at the low, no reversal | WRONG - direction right, but a whiplash (spike that immediately reverses) did not happen; Friday was a one-way decline (BS-type) |
**E2 = 4 / 5 = 80 %.**

### Step 4 - E3
| obvious trade | setup | verdict |
|---|---|---|
| A LONG 98.02 | DX3 LONG 98.019 / 97.939 / 98.874, filled Mon 15:15, TP Thu 17:30 (also DX2 98.045 -> 98.402 TP) | CAUGHT |
| B LONG 98.29 | DX5 LONG 98.270 / 98.104 / 98.874, filled Wed 05:15, TP Thu 17:30 | CAUGHT |
Stopped-out setups: **DX6** LONG 98.660 / 98.615 (filled Thu 00:00, stopped Thu 00:15).
**E3 = 2 / 2 = 100 %.** Information only: of the other three visible moves, (c) Mon short was caught by DX1 (98.415 -> 98.045 TP); (d) Tue short 98.567 and (e) Fri short 98.915 have no setup (both rejected for RRR in the facts).

### Step 5 - presentation
- History half: label collisions at 98.40 ("LSZ supply-side | sweep to 98.539" / "LSZ demand-side | sweep to 98.264") and at 98.92 ("UPPER RESISTANCE" over "4H (Unmitigated) | BoM"); "GAP IN-FILL" label over the Apr 17-18 candles.
- Week frame: DX2 / DX3 / DX4 labels pile up on Monday's low candles; "Tue SS+RWL+BS" and "DX5 Ladder ... if DX3" overlap; purple Thu / Fri tags are drawn over the Thu-Fri candles and are barely legible.

## Map 5 - EURUSD 2026-04-20

Week action (1H, UTC): Mon 1.1747 (04-06) -> 1.1791 (Mon 13 - Tue 00 stall); Tue 1.1791 -> 1.17565 -> 1.17759 -> 1.17187 (Tue 19); Wed 1.17624 (05) -> 1.1703 (21); Thu 1.16921 / 1.16789 (11) -> 1.17165 (14) -> 1.16691 (17); Fri 1.16729 (02) -> 1.1723 (20).

### Step 1 - obvious trades (written from the `_zones` frame before opening any setup)
| # | move | from zone -> to zone |
|---|---|---|
| A | Mon LONG 1.1747 -> 1.1790 (+44 p) | EQUILIBRIUM 1.17497-1.17573 -> 1H MoM supply 1.17847-1.17988 |
| B | Tue SHORT 1.1791 -> 1.1719 (-72 p) | 1H MoM supply -> GAP 1.17203-1.17263 / 1H MoM demand 1.17004-1.17207 |
| C | Tue-Wed LONG 1.1719 -> 1.1762 (+44 p) | GAP 1.17203 / 1H MoM demand -> EQUILIBRIUM / LSZ 1.1758-1.1762 |
| D | Wed-Thu SHORT 1.1762 -> 1.1669 (-93 p; first leg to 1.1692 -70 p) | EQUILIBRIUM -> 4H BoM demand 1.16809-1.16996 / 1H BoM demand 1.16638-1.16754 |
| E | Thu-Fri LONG 1.1669 -> 1.1723 (+54 p) | 1H BoM demand / GAP 1.16744-1.16804 -> GAP 1.17203-1.17263 |
Obvious trades: 5.

### Step 2 - E1
| zone (facts) | verdict at first contact | delta (UTC hour) |
|---|---|---|
| IP UPPER RESISTANCE 1.18213-1.18292 | not reached | |
| IP UPPER RESISTANCE 1.17988-1.18067 | not reached | |
| IP UPPER RESISTANCE 1.17706-1.17791 | REACTED | first contact Mon 07 from below; reacted turn Mon 08 |
| IP EQUILIBRIUM ZONE 1.17497-1.17573 | REACTED | first contact Mon 06 from above; reacted turn Mon 06 |
| IP MID-RANGE SUPPORT 1.16973-1.17033 | REACTED | first contact Wed 20 from above; reacted wick-rejection Thu 00 (5.2 p wick past far edge, closed back) |
| IP KEY SUPPORT BAND 1.1657-1.16638 | not reached | |
| GAP 1.17347-1.17407 | REACTED | first contact Tue 16 from above; reacted turn Tue 17 |
| GAP 1.17203-1.17263 | REACTED | first contact Tue 17 from above; reacted turn Tue 17 |
| GAP 1.16744-1.16804 | REACTED | first contact Thu 10 from above; reacted turn Thu 11 |
| 1H (Unmitigated) BoM supply 1.18239-1.18491 | not reached | |
| 1H (Unmitigated) MoM supply 1.17847-1.17988 | REACTED | first contact Mon 15 from below; reacted stall Mon 17 |
| 1H (Unmitigated) MoM demand 1.17004-1.17207 | REACTED | first contact Tue 17 from above; reacted turn Tue 17 |
| 4H (Unmitigated) BoM demand 1.16809-1.16996 | REACTED | first contact Thu 00 from above; reacted turn Thu 00 |
| 1H (Unmitigated) BoM demand 1.16638-1.16754 | REACTED | first contact Thu 17 from above; reacted turn Thu 17 |
| 4H (Unmitigated) MoM demand 1.16543-1.16748 | REACTED | first contact Thu 17 from above; reacted turn Thu 17 |
| LSZ supply 1.18188-1.18238 (reach 1.18338) | not reached | |
| LSZ supply 1.1806-1.1811 (reach 1.1821) | not reached | |
| LSZ supply 1.1803-1.1808 (reach 1.1818) | not reached | |
| LSZ demand 1.17719-1.17769 (reach 1.17619) | REACTED | first contact Mon 06 from below; reacted turn Mon 08 |
| LSZ demand 1.17668-1.17718 (reach 1.17568) | REACTED | first contact Mon 06 from below; reacted turn Mon 08 |
| LSZ supply 1.17611-1.17661 (reach 1.17761) | REACTED | first contact Mon 06 from below; reacted turn Mon 08 |
| LSZ supply 1.17575-1.17625 (reach 1.17725) | REACTED | first contact Mon 06 from below; reacted turn Mon 08 |
| LSZ demand 1.17592-1.17642 (reach 1.17492) | REACTED | first contact Mon 06 from below; reacted wick-rejection Mon 07 (7.6 p wick past far edge, closed back) |
| LSZ demand 1.17527-1.17577 (reach 1.17427) | REACTED | first contact Mon 06 from above; reacted turn Mon 06 |
| LSZ demand 1.17277-1.17327 (reach 1.17177) | REACTED | first contact Tue 17 from above; reacted turn Tue 17 |
| LSZ demand 1.16638-1.16688 (reach 1.16538) | not reached | |
| band 1.18125-1.18216 | not reached | |
| band 1.17958-1.18049 | not reached | |
| band 1.1771-1.17801 | REACTED | first contact Mon 07 from below; reacted turn Mon 08 |
| band 1.17564-1.17655 | REACTED | first contact Mon 06 from below; reacted wick-rejection Mon 07 (6.3 p wick past far edge, closed back) |
| band 1.17327-1.17418 | REACTED | first contact Tue 15 from above; reacted turn Tue 17 |
| band 1.17126-1.17217 | REACTED | first contact Tue 17 from above; reacted turn Tue 17 |
| band 1.16876-1.16967 | REACTED | first contact Thu 00 from above; reacted turn Thu 00 |
| band 1.16581-1.16672 | not reached | |
Reached 23, reacted 23, pierced 0. Unzoned turning points: none.
**E1 = 23 / (23 + 0) = 100 %.** Gate: **FAIL - bunched/bloated.** 34 objects in 1.1654-1.1849; 1.1750-1.1780 holds 2 IP + 6 LSZ + 2 bands; in the zones frame the two LSZ labels at 1.1760 are printed on top of each other and cannot be read ("LSZ supply-side | sweep to ..." over "LSZ demand-side ...").

### Step 3 - E2
| day | forecast | candles | verdict |
|---|---|---|---|
| Mon | SS range 1.17004-1.17988, key 1H MoM | 1.1747 -> 1.1790, held under the 1H MoM supply, inside the box | RIGHT |
| Tue | SS+RWL+BS down, key 4H BoM | chop 1.1772-1.1786, drop 1.17565, pop 1.17759, break to 1.17187, close down | RIGHT |
| Wed | BS down, box 1.17380-1.17865 | 1.17624 -> 1.1703, close at the low | RIGHT (box sits above most of the day) |
| Thu | BS+RWL down, box 1.16996-1.17380 | 1.16789 -> spike 1.17165 -> 1.16691, close down | RIGHT |
| Fri | RWL up, box 1.17032-1.17207 | one-way rise 1.16729 -> 1.1723, held at the high | WRONG - direction right, but no whiplash (no spike that immediately reversed) |
**E2 = 4 / 5 = 80 %.**

### Step 4 - E3
| obvious trade | setup | verdict |
|---|---|---|
| A Mon LONG 1.1747 | none (EU2 LONG is at 1.17207, not filled) | MISSED |
| B Tue SHORT 1.1791 | EU3 SHORT 1.17920 / 1.17996 / 1.17497 (TP Tue 15:00); EU4 SHORT 1.17920 -> 1.17006 (TP Thu 00:00) | CAUGHT |
| C Tue-Wed LONG 1.1719 | EU2 LONG 1.17207 expired after Monday; Tue 19 traded 1.17187 with no order | MISSED |
| D Wed SHORT 1.1762 | EU5 SHORT 1.17656 not filled (Wed high 1.17624, 3.2 p short) | MISSED |
| E Thu-Fri LONG 1.1669 | none (Thu RWL up rejected for RRR) | MISSED |
Stopped-out setups: none. EU1, EU2, EU5, EU6 not filled.
**E3 = 1 / 5 = 20 %.**

### Step 5 - presentation
- History half: the two LSZ labels at 1.1760 overprint each other; zone labels sit over the Apr 15-18 candles.
- Week frame: "Tue SS+RWL+BS down 33%" is crossed by the yellow path; EU1 / EU3 labels on the Mon-Tue candles; "EU5 Ladder S 12.3R if EU4" over Wed candles; purple "Thu BS+RWL" / "Fri RWL" tags on top of the Thu-Fri candles.

## Map 6 - GBPUSD 2026-04-20

Week action (1H, UTC): a 1.347-1.354 range with ~60 p swings: Mon 1.34818 (05) -> 1.35444 (15); Tue 1.34823 (08) -> 1.35396 (14) -> 1.34744 (20); Wed 1.35353 (08) -> 1.34925 (11) -> 1.35243 -> 1.34789 (Wed 23); Thu 1.35182 (14) -> 1.34476 (17); Fri 1.34532 (02) -> 1.3537 (20).

### Step 1 - obvious trades (written from the `_zones` frame before opening any setup)
| # | move | from zone -> to zone |
|---|---|---|
| A | Mon LONG 1.3482 -> 1.3544 (+62 p) | MID-RANGE SUPPORT 1.34768-1.34846 -> above UPPER RESISTANCE 1.35241-1.35327 |
| B | Mon-Tue SHORT 1.3544 -> 1.3482 (-62 p) | UPPER RESISTANCE -> MID-RANGE SUPPORT |
| C | Tue LONG 1.3482 -> 1.3540 (+57 p) | MID-RANGE SUPPORT -> UPPER RESISTANCE |
| D | Tue SHORT 1.3540 -> 1.3474 (-65 p) | UPPER RESISTANCE -> MID-RANGE SUPPORT / LSZ 1.3474 |
| E | Tue-Wed LONG 1.3474 -> 1.3535 (+61 p) | MID-RANGE SUPPORT -> UPPER RESISTANCE |
| F | Wed SHORT 1.3535 -> 1.3479 (-56 p) | UPPER RESISTANCE -> MID-RANGE SUPPORT |
| G | Thu SHORT 1.3518 -> 1.3448 (-71 p) | LSZ 1.3516 / GAP 1.3505 -> GAP 1.34423-1.34483 / 1H MoM demand |
| H | Thu-Fri LONG 1.3448 -> 1.3537 (+89 p) | GAP 1.3442 / 1H MoM demand -> UPPER RESISTANCE |
Obvious trades: 8.

### Step 2 - E1
| zone (facts) | verdict at first contact | delta (UTC hour) |
|---|---|---|
| IP UPPER RESISTANCE 1.35241-1.35327 | REACTED | first contact Mon 11 from below; reacted turn Mon 12 |
| IP UPPER RESISTANCE 1.34932-1.35019 | PIERCED | first contact Mon 06 from below; pierced Mon 07 (16.9 p past far edge, close beyond) |
| IP MID-RANGE SUPPORT 1.34768-1.34846 | REACTED | first contact Mon 06 from above; reacted turn Mon 06 |
| IP KEY SUPPORT BAND 1.33998-1.34073 | not reached | |
| GAP 1.35047-1.35107 | REACTED | first contact Mon 06 from below; reacted wick-rejection Mon 07 (8.1 p wick past far edge, closed back) |
| GAP 1.3464-1.347 | PIERCED | first contact Thu 17 from above; pierced Thu 17 (16.4 p past far edge, close back inside/above) |
| GAP 1.34423-1.34483 | REACTED | first contact Thu 17 from above; reacted turn Thu 17 |
| GAP 1.34317-1.34377 | not reached | |
| 1H (Unmitigated) MoM demand 1.34345-1.3466 | REACTED | first contact Thu 17 from above; reacted turn Thu 17 |
| 4H (Unmitigated) BoM demand 1.34017-1.34073 | not reached | |
| 1H (Unmitigated) BoM demand 1.33806-1.3396 | not reached | |
| LSZ demand 1.35163-1.35213 (reach 1.35063) | REACTED | first contact Mon 07 from below; reacted turn Mon 07 |
| LSZ supply 1.35036-1.35086 (reach 1.35186) | REACTED | first contact Mon 06 from below; reacted turn Mon 07 |
| LSZ demand 1.35044-1.35094 (reach 1.34944) | REACTED | first contact Mon 06 from below; reacted wick-rejection Mon 07 (9.4 p wick past far edge, closed back) |
| LSZ demand 1.34952-1.35002 (reach 1.34852) | REACTED | first contact Mon 06 from above; reacted turn Mon 06 |
| LSZ demand 1.3474-1.3479 (reach 1.3464) | REACTED | first contact Tue 17 from above; reacted turn Tue 17 |
| LSZ demand 1.33805-1.33855 (reach 1.33705) | not reached | |
| band 1.3522-1.35332 | REACTED | first contact Mon 11 from below; reacted turn Mon 12 |
| band 1.34973-1.35085 | PIERCED | first contact Mon 06 from below; pierced Mon 07 (10.3 p past far edge, close back inside/below) |
| band 1.34691-1.34803 | REACTED | first contact Tue 17 from above; reacted turn Tue 17 |
| band 1.34473-1.34585 | REACTED | first contact Thu 17 from above; reacted turn Thu 17 |
| band 1.34227-1.34339 | not reached | |
| band 1.33983-1.34095 | not reached | |
| band 1.33821-1.33933 | not reached | |
Reached 16, reacted 13, pierced 3. **Unzoned turning points: 2** - Mon 15:00 top 1.35444 (11 p above the highest box, 1.35332) and Tue 14:00 top 1.35396 (6.4 p above it). The facts header itself says the zones stop at 1.35327 while the week traded to 1.35444.
**E1 = 13 / (16 + 2) = 72 %.** Gate: **FAIL - missing + floating + bunched.** Missing: no zone at the 1.3540-1.3545 ceiling that capped Mon and Tue. Floating: KEY SUPPORT BAND, 4H BoM demand, 1H BoM demand, LSZ 1.33805 and two bands sit 40-70 p under the week low. Bunched: 1.3474-1.3533 is covered wall to wall (IP, 3 gaps, 5 LSZ, 4 bands); in the zones frame "KEY SUPPORT BAND" and "4H (Unmitigated) | BoM" labels print over each other at 1.3405, and "LSZ demand-side" over "supply-side" at 1.3495.

### Step 3 - E2
| day | forecast | candles | verdict |
|---|---|---|---|
| Mon | SS range 1.34345-1.35019, key UPPER RESISTANCE | broke out of the box upward: 1.34818 -> 1.35444, close 1.35333 (31 p above the box ceiling) | WRONG |
| Tue | SS+RWL+BS down, box 1.34946-1.35213 | 1.3529 -> 1.34823 -> 1.35396 -> break to 1.34744 -> 1.351, close below open | RIGHT (two-way chop, break down to MID-RANGE SUPPORT, close down) |
| Wed | BS down, box 1.34524-1.35094 | 1.351 -> 1.35353 -> 1.34925 -> 1.35243 -> 1.34789; no decisive break, close -10 p | WRONG - range day, no breakout surge |
| Thu | BS+RWL down, box 1.34073-1.34524, key 1H MoM | chop, then 16:00 break through MID-RANGE SUPPORT to 1.34476 (1H MoM demand), bounce | RIGHT |
| Fri | RWL up, box 1.34174-1.34660 | one-way rise 1.34532 -> 1.3537 (+84 p) | WRONG - no whiplash; also the box ends 70 p below the day's high |
**E2 = 2 / 5 = 40 %.**

### Step 4 - E3
| obvious trade | setup | verdict |
|---|---|---|
| A Mon LONG 1.3482 | GB1 LONG 1.34660 not filled | MISSED |
| B Mon-Tue SHORT 1.3544 | GB2 SHORT 1.35163 / 1.35243 filled Mon 07:15, **STOPPED Mon 11:15** (before the 1.3544 top) | MISSED |
| C Tue LONG 1.3482 | none | MISSED |
| D Tue SHORT 1.3540 | none | MISSED |
| E Tue-Wed LONG 1.3474 | none | MISSED |
| F Wed SHORT 1.3535 | none (GB3 SHORT 1.34818 not filled) | MISSED |
| G Thu SHORT 1.3518 | GB4 SHORT 1.34557 not filled | MISSED |
| H Thu-Fri LONG 1.3448 | GB5 LONG 1.34083 not filled (40 p under the low) | MISSED |
Stopped-out setups: **GB2** SHORT 1.35163 (Mon 07:15 -> stopped Mon 11:15).
**E3 = 0 / 8 = 0 %.**

### Step 5 - presentation
- Week frame: the yellow path dives to 1.3407 on Thursday (price low 1.34476) - the drawn path is 40 p away from the candles for two days; GB5's box sits 1.3399-1.3443, entirely below the candles.
- Labels: "Tue SS+RWL+BS" over Tue candles; "Wed BS down" and the 1.0bn strike label overprint at 1.3500; purple Thu/Fri tags over candles.

## Map 7 - DXY 2026-10-05

Week action (1H, UTC, from the anchor; the Mon 01-05 spike to 102.535 is before the anchor): Mon 06 102.433 -> 102.084 (09) -> 102.372 (14) -> 102.101; Tue 102.285 (05) -> 101.754 (11), stall 101.77-101.89 to Tue 22; Wed 101.952 -> 102.499 (11) -> 102.21; Thu 102.133 (02) -> 102.467 (11) -> 102.033 (14-17); Fri 101.92 (05) -> 102.335 (13) -> 102.2.

### Step 1 - obvious trades (written from the `_zones` frame before opening any setup)
| # | move | from zone -> to zone |
|---|---|---|
| B | Tue SHORT 102.285 -> 101.754 (-53 p) | LSZ supply 102.157-102.207 (reach 102.307) -> KEY SUPPORT BAND 101.750-101.843 |
| C | Tue-Wed LONG 101.754 -> 102.499 (+75 p) | KEY SUPPORT BAND -> LSZ supply 102.485-102.535 |
| D | Wed SHORT 102.499 -> 102.21 (-29 p) | LSZ supply 102.485 -> LSZ supply 102.157-102.207 |
| E | Thu LONG 102.133 -> 102.467 (+33 p) | LSZ supply 102.082-102.132 -> LSZ supply 102.485 |
| F | Thu SHORT 102.467 -> 102.033 (-43 p) | LSZ supply 102.485 -> MID-RANGE SUPPORT 101.961-102.051 |
| G | Fri LONG 101.92 -> 102.335 (+41 p) | 1H MoM demand 101.855-101.926 -> LSZ 102.157-102.207 reach |
Not counted: Mon 102.433 -> 102.084 (starts at the anchor hour itself, no zone at the top) and Mon 102.084 -> 102.372 (choppy, no zone at the top).
Obvious trades: 6.

### Step 2 - E1
| zone (facts) | verdict at first contact | delta (UTC hour) |
|---|---|---|
| IP MID-RANGE SUPPORT 101.961-102.051 | REACTED | first contact Tue 01 from above; reacted turn Tue 02 |
| IP KEY SUPPORT BAND 101.75-101.843 | REACTED | first contact Tue 11 from above; reacted turn Tue 12 |
| 1H (Unmitigated) MoM demand 101.855-101.926 | PIERCED | first contact Tue 11 from above; pierced Tue 11 (7.9 p past far edge, close beyond) |
| 1H (Unmitigated) BoM demand 101.668-101.798 | REACTED | first contact Tue 11 from above; reacted turn Tue 12 |
| LSZ supply 102.485-102.535 (reach 102.635) | REACTED | first contact Wed 12 from below; reacted turn Wed 13 |
| LSZ supply 102.157-102.207 (reach 102.307) | PIERCED | first contact Mon 06 from above; pierced Mon 08 (5.2 p past far edge, close beyond) |
| LSZ supply 102.082-102.132 (reach 102.232) | REACTED | first contact Mon 07 from above; reacted turn Mon 09 |
| LSZ demand 101.855-101.905 (reach 101.755) | REACTED | first contact Tue 11 from above; reacted turn Tue 12 |
| LSZ demand 101.668-101.718 (reach 101.568) | not reached | |
| band 101.916-101.996 | REACTED | first contact Tue 08 from above; reacted stall Tue 10 |
Reached 9, reacted 7, pierced 2. **Unzoned turning points: 2** - Mon 06:00 top 102.433 (-35 p; 5 p under the nearest box) and Mon 14:00 top 102.372 (-27 p; nothing between 102.307 and 102.485).
**E1 = 7 / (9 + 2) = 64 %.** Gate: **FAIL - missing** (no zone in 102.31-102.48 where Monday turned twice). Not bloated: 10 objects, readable.

### Step 3 - E2
| day | forecast | candles | verdict |
|---|---|---|---|
| Mon | SS range 101.855-102.635, key LSZ | 102.433 -> 102.084 -> 102.372 -> 102.10, inside | RIGHT |
| Tue | SS range | 102.285 -> 101.754 (10 p sweep under the floor, inside canon's 0.05-0.10 sweep), stall | RIGHT |
| Wed | SS range | 101.82 -> 102.499 (ceiling) -> 102.21 | RIGHT |
| Thu | SS range | 102.133 -> 102.467 -> 102.033 | RIGHT |
| Fri | SS range | 101.92 -> 102.335 | RIGHT |
**E2 = 5 / 5 = 100 %.** (Note: the same box and tag five times; the yellow path is a fixed zig-zag 101.93 <-> 102.49 that only loosely follows the candles - e.g. it is at 102.49 on Tue 00:00 while price was 102.11.)

### Step 4 - E3
| obvious trade | setup | verdict |
|---|---|---|
| B Tue SHORT 102.285 | none | MISSED |
| C Tue-Wed LONG 101.754 | DX2 LONG 101.926 / 101.825 filled Tue 11:00, **STOPPED Tue 11:30** (low 101.754) | MISSED |
| D Wed SHORT 102.499 | DX1 SHORT 102.485 / 102.565 / 101.926, filled Wed 12:15, TP Fri 05:30 | CAUGHT |
| E Thu LONG 102.133 | none | MISSED |
| F Thu SHORT 102.467 | none new (DX1 already open from Wed) | MISSED |
| G Fri LONG 101.92 | none (DX2 not re-armed after its stop) | MISSED |
Stopped-out setups: **DX2** LONG 101.926 (Tue 11:00 -> 11:30).
**E3 = 1 / 6 = 17 %.**

### Step 5 - presentation
- Zones frame: "LSZ demand-side | sweep to 101.755" is overprinted by "1H (Unmitigated) | MoM" at 101.87; "KEY SUPPORT BAND" label sits on the Oct 2-3 candles.
- All/week frames: one identical grey box per day spanning 101.855-102.635 covers every candle of the week; DX1 / DX2 labels over Monday's candles.

## Map 8 - EURUSD 2026-10-05

Week action (1H, UTC, from the anchor): Mon 06 1.1169 -> 1.12207 (09), chop 1.1186-1.1231 to Tue 03; Tue 1.12028 (05) -> 1.12767 (11), stall 1.1245-1.1269 to Tue 23; Wed 1.12487 -> 1.11645 (12) -> 1.12037 (15); Thu 1.12128 (02) -> 1.11719 (11) -> 1.12267 (14) -> 1.11845 (16) -> 1.12196; Fri 1.12427 (05) -> 1.11874 (16).

### Step 1 - obvious trades (written from the `_zones` frame before opening any setup)
| # | move | from zone -> to zone |
|---|---|---|
| A | Mon LONG 1.1169 -> 1.1221 (+52 p) | LSZ demand 1.11610-1.11660 -> LSZ demand 1.12208-1.12258 |
| B | Tue LONG 1.1203 -> 1.1277 (+74 p) | band 1.12039-1.12149 / LSZ reach 1.12049 -> 1H BoM supply 1.12716-1.12853 |
| C | Tue-Wed SHORT 1.1277 -> 1.1165 (-112 p) | 1H BoM supply -> LSZ demand 1.11610-1.11660 |
| D | Wed-Thu LONG 1.1165 -> 1.1213 (+48 p) | LSZ demand 1.1161 -> band 1.12039-1.12149 |
| E | Thu SHORT 1.1213 -> 1.1172 (-41 p) | band -> LSZ demand area (6 p above the box) |
| F | Thu-Fri LONG 1.1172 -> 1.1243 (+71 p) | LSZ demand area -> UPPER RESISTANCE 1.12451-1.12530 |
| G | Fri SHORT 1.1243 -> 1.1187 (-55 p) | UPPER RESISTANCE -> (no zone at 1.1187) |
Obvious trades: 7.

### Step 2 - E1
| zone (facts) | verdict at first contact | delta (UTC hour) |
|---|---|---|
| IP UPPER RESISTANCE 1.12451-1.1253 | REACTED | first contact Tue 08 from below; reacted stall Tue 10 |
| GAP 1.12806-1.12866 | not reached | |
| GAP 1.12611-1.12671 | REACTED | first contact Tue 11 from below; reacted turn Tue 12 |
| 1H (Unmitigated) BoM supply 1.12716-1.12853 | REACTED | first contact Tue 11 from below; reacted turn Tue 12 |
| 1H (Unmitigated) MoM supply 1.12491-1.12612 | PIERCED | first contact Tue 11 from below; pierced Tue 11 (10.5 p past far edge, close beyond) |
| LSZ supply 1.12803-1.12853 (reach 1.12953) | not reached | |
| LSZ supply 1.12562-1.12612 (reach 1.12712) | REACTED | first contact Tue 11 from below; reacted turn Tue 12 |
| LSZ demand 1.12208-1.12258 (reach 1.12108) | REACTED | first contact Mon 08 from below; reacted turn Mon 10 |
| LSZ demand 1.12149-1.12199 (reach 1.12049) | REACTED | first contact Mon 07 from below; reacted stall Mon 09 |
| LSZ demand 1.1161-1.1166 (reach 1.1151) | REACTED | first contact Wed 12 from above; reacted turn Wed 13 |
| band 1.12039-1.12149 | REACTED | first contact Mon 07 from below; reacted wick-rejection Mon 09 (5.8 p wick past far edge, closed back) |
Reached 9, reacted 8, pierced 1. **Unzoned turning points: 2** - Thu 11:00 low 1.11719 (+55 p after; 5.9 p above the nearest box) and Thu 16:00 low 1.11845 (+35 p after; 18 p from any box).
**E1 = 8 / (9 + 2) = 73 %.** Gate: **FAIL - missing** (nothing between 1.1166 and 1.1204, where price spent Wed 09:00 - Thu 17:00). Not bloated (11 objects).

### Step 3 - E2
| day | forecast | candles | verdict |
|---|---|---|---|
| Mon | SS range 1.11510-1.12612, key 1H MoM | 1.1169 -> 1.12249, inside | RIGHT |
| Tue | SS range | 1.12028 -> 1.12767: breakout surge through the ceiling 1.12612, 1H closes 1.1273-1.1278 (12-17 p over it) for Tue 11:00-16:00 | WRONG - the ceiling did not hold (a BS, not a swing inside the range) |
| Wed | SS range | 1.12629 -> 1.11645 (floor) | RIGHT |
| Thu | SS range | 1.11719 -> 1.12267 -> 1.11845 -> 1.1209 | RIGHT |
| Fri | SS range | 1.12427 -> 1.11874 | RIGHT |
**E2 = 4 / 5 = 80 %.** (Same box and tag all five days; the yellow path is a fixed zig-zag between 1.1166 and 1.1249.)

### Step 4 - E3
| obvious trade | setup | verdict |
|---|---|---|
| A Mon LONG 1.1169 | EU2 LONG 1.11660 not filled on Monday (low 1.1169) | MISSED |
| B Tue LONG 1.1203 | none | MISSED |
| C Tue-Wed SHORT 1.1277 | EU1 SHORT 1.12491 / 1.12642 filled Tue 09:45, **STOPPED Tue 11:15** (high 1.12767) | MISSED |
| D Wed-Thu LONG 1.1165 | EU2 LONG 1.11660 / 1.11580 / 1.12491 filled Wed 12:15 - TP never hit (week high after fill 1.12427), open at week end | MISSED |
| E Thu SHORT 1.1213 | none | MISSED |
| F Thu-Fri LONG 1.1172 | none new (EU2 open, TP missed by 6.4 p) | MISSED |
| G Fri SHORT 1.1243 | none | MISSED |
Stopped-out setups: **EU1** SHORT 1.12491 (Tue 09:45 -> 11:15).
**E3 = 0 / 7 = 0 %.**

### Step 5 - presentation
- History half: "LSZ supply-side | sweep to 1.12953" is overprinted by "GAP IN-FILL" at 1.1280; "GAP IN-FILL" and "1H (Unmitigated) | MoM" collide at 1.1258; labels sit on the Oct 2-3 candles.
- Week frames: five identical day boxes 1.1151-1.1261 cover every candle; "Tue SS 80%" tag sits on Tuesday's high candles.

## Map 9 - GBPUSD 2026-10-05

Week action (1H, UTC, from the anchor): Mon 06 1.32052 -> 1.3239 (09) -> 1.319 (13) -> 1.3229; Tue 1.32013 (05) -> 1.32856 (15), stall 1.3258-1.3283 to Tue 23; Wed 1.32628 -> 1.31935 (11) -> 1.32242; Thu 1.31843 (10) -> 1.32485 (14) -> 1.32037 (16) -> 1.32377; Fri 1.32503 (05) -> 1.32057 (12) -> 1.32443 (18).

### Step 1 - obvious trades (written from the `_zones` frame before opening any setup)
| # | move | from zone -> to zone |
|---|---|---|
| A | Mon SHORT 1.3239 -> 1.3190 (-49 p) | 1H BoM supply 1.32319-1.32395 -> LSZ demand 1.31899-1.31949 |
| B | Tue LONG 1.3201 -> 1.3286 (+84 p) | MID-RANGE SUPPORT 1.31991-1.32051 -> (no zone at 1.3286) |
| C | Tue-Wed SHORT 1.3286 -> 1.3194 (-92 p) | (no zone) -> LSZ demand 1.31899-1.31949 |
| E | Thu LONG 1.3184 -> 1.3249 (+64 p) | LSZ demand 1.31899 (reach 1.31799) -> UPPER RESISTANCE 1.32457-1.32535 |
| F | Thu SHORT 1.3249 -> 1.3204 (-45 p) | UPPER RESISTANCE -> MID-RANGE SUPPORT |
| G | Thu-Fri LONG 1.3204 -> 1.3250 (+47 p) | MID-RANGE SUPPORT -> UPPER RESISTANCE |
| H | Fri SHORT 1.3250 -> 1.3206 (-45 p) | UPPER RESISTANCE -> MID-RANGE SUPPORT |
Obvious trades: 7 (Wed 1.3194 -> 1.3224 and Fri 1.3206 -> 1.3244 are under 40 p and not counted).

### Step 2 - E1
| zone (facts) | verdict at first contact | delta (UTC hour) |
|---|---|---|
| IP UPPER RESISTANCE 1.32457-1.32535 | PIERCED | first contact Tue 09 from below; pierced Tue 11 (28.2 p past far edge, close beyond) |
| IP MID-RANGE SUPPORT 1.31991-1.32051 | PIERCED | first contact Mon 13 from above; pierced Mon 13 (9.1 p past far edge, close beyond) |
| GAP 1.3227-1.3233 | REACTED | first contact Mon 07 from below; reacted wick-rejection Mon 08 (5.1 p wick past far edge, closed back) |
| GAP 1.32124-1.32184 | PIERCED | first contact Mon 06 from below; pierced Mon 07 (11.6 p past far edge, close beyond) |
| 1H (Unmitigated) BoM supply 1.32319-1.32395 | REACTED | first contact Mon 08 from below; reacted turn Mon 09 |
| LSZ supply 1.3253-1.3258 (reach 1.3268) | PIERCED | first contact Tue 11 from below; pierced Tue 11 (13.7 p past far edge, close beyond) |
| LSZ supply 1.3251-1.3256 (reach 1.3266) | PIERCED | first contact Tue 11 from below; pierced Tue 11 (15.7 p past far edge, close beyond) |
| LSZ supply 1.3245-1.325 (reach 1.326) | PIERCED | first contact Tue 09 from below; pierced Tue 11 (21.7 p past far edge, close beyond) |
| LSZ demand 1.32226-1.32276 (reach 1.32126) | PIERCED | first contact Mon 06 from below; pierced Mon 08 (10.5 p past far edge, close beyond) |
| LSZ demand 1.32183-1.32233 (reach 1.32083) | PIERCED | first contact Mon 06 from below; pierced Mon 07 (6.7 p past far edge, close beyond) |
| LSZ demand 1.32021-1.32071 (reach 1.31921) | REACTED | first contact Mon 06 from above; reacted turn Mon 07 |
| LSZ demand 1.31899-1.31949 (reach 1.31799) | REACTED | first contact Mon 13 from above; reacted turn Mon 14 |
| band 1.32526-1.32636 | PIERCED | first contact Tue 11 from below; pierced Tue 11 (18.1 p past far edge, close beyond) |
| band 1.32121-1.32231 | PIERCED | first contact Mon 06 from below; pierced Mon 07 (6.9 p past far edge, close beyond) |
| band 1.31932-1.32042 | REACTED | first contact Mon 13 from above; reacted turn Mon 14 |
Reached 15, reacted 5, pierced 10. **Unzoned turning points: 1** - Tue 15:00 top 1.32856 (-92 p after; 18 p above the highest reach, 1.3268).
**E1 = 5 / (15 + 1) = 31 %.** Gate: **FAIL - missing + bunched.** Missing: the week high 1.3286 (the biggest turn) has no zone. Bunched: UPPER RESISTANCE, three LSZ supply boxes and a band all inside 1.3245-1.3264 (the LSZ boxes 1.32450 / 1.32510 / 1.32530 are within 8 p and should be one box).

### Step 3 - E2
| day | forecast | candles | verdict |
|---|---|---|---|
| Mon | SS range 1.31921-1.32395, key 1H BoM | 1.3239 -> 1.319 -> 1.3229, inside | RIGHT |
| Tue | SS range | breakout: 1.32013 -> 1.32856, closed 1.32742 = 35 p above the box | WRONG |
| Wed | SS range | one-way 82 p decline from above the box (1.32761) to the floor 1.31935 | WRONG - not an oscillation inside the bounds |
| Thu | SS range | 1.31843 -> 1.32485 -> 1.32037 -> 1.3227, both bounds tested | RIGHT |
| Fri | SS range | 1.32503 -> 1.32057 -> 1.32443 | RIGHT |
**E2 = 3 / 5 = 60 %.**

### Step 4 - E3
| obvious trade | setup | verdict |
|---|---|---|
| A Mon SHORT 1.3239 | GB1 SHORT 1.32319 / 1.32425 / 1.31994, filled Mon 07:45, TP Mon 13:30 | CAUGHT |
| B Tue LONG 1.3201 | GB2 (re-armed) LONG 1.32071 / 1.31991 / 1.32309, filled Tue 06:00, TP Tue 07:30 (24 of the 84 p) | CAUGHT |
| C Tue-Wed SHORT 1.3286 | none | MISSED |
| E Thu LONG 1.3184 | none (GB2 stopped Wed, not re-armed) | MISSED |
| F Thu SHORT 1.3249 | none | MISSED |
| G Thu-Fri LONG 1.3204 | none | MISSED |
| H Fri SHORT 1.3250 | none | MISSED |
Stopped-out setups: **GB1 re-armed** SHORT 1.32319 (Tue 01:30 -> stopped Tue 08:30, on the way to 1.3286); **GB2 re-armed (2nd)** LONG 1.32071 (Wed 11:15 -> stopped Wed 12:15).
**E3 = 2 / 7 = 29 %.**

### Step 5 - presentation
- Week frames: the five identical day boxes stop at 1.32395 while Tuesday-Wednesday trade up to 1.3286 - the week's main swing is drawn with nothing on it; "1H (Unmitigated) | BoM" label prints over the "Mon SS 80%" tag; GB1 / GB2 labels over Monday's candles.
- Zones frame: "LSZ supply-side | sweep to 1.32600" and "UPPER RESISTANCE" labels overlap at 1.3250; "LSZ demand-side | sweep to 1.31921" over "MID-RANGE SUPPORT" at 1.3202.

## Map 10 - DXY 2026-05-18

Week action (1H, UTC, from the anchor): Mon 06 99.307 -> 98.98 (12) -> 99.193 (18) -> 98.944 (22); Tue up to 99.434 (14), 99.25-99.33 into Wed; Wed 99.471 (08) -> 99.294 -> 99.472 (14) -> 98.966 (15) -> 99.05-99.20; Thu 99.064 (01) -> 99.356 (07) -> 99.078 (08) -> 99.515 (13) -> 99.092 (17); Fri chop 99.172-99.412.

### Step 1 - obvious trades (written from the `_zones` frame before opening any setup)
| # | move | from zone -> to zone |
|---|---|---|
| A | Mon SHORT 99.307 -> 98.98 (-33 p) | LSZ supply 99.270-99.320 -> MID-RANGE SUPPORT 98.963-99.037 |
| B | Mon-Tue LONG 98.944 -> 99.434 (+49 p) | MID-RANGE SUPPORT / band 98.885-98.939 -> LSZ supply 99.359-99.409 |
| C | Wed SHORT 99.472 -> 98.966 (-51 p) | band 99.449-99.503 / LSZ reach -> MID-RANGE SUPPORT |
| D | Thu LONG 99.078 -> 99.515 (+44 p) | 1H Mitigated demand 99.001-99.097 -> band 99.449-99.503 / LSZ reach 99.509 |
| E | Thu SHORT 99.515 -> 99.092 (-42 p) | band 99.449-99.503 -> 1H Mitigated demand |
Not counted: Thu-Fri 99.092 -> 99.412 (+32 p, choppy, no clean leg). Obvious trades: 5.

### Step 2 - E1
| zone (facts) | verdict at first contact | delta (UTC hour) |
|---|---|---|
| IP MID-RANGE SUPPORT 98.963-99.037 | REACTED | first contact Mon 12 from above; reacted turn Mon 13 |
| 1H (Unmitigated) MoM demand 99.251-99.298 | PIERCED | first contact Mon 06 from above; pierced Mon 06 (8.1 p past far edge, close beyond) |
| 1H (Unmitigated) MoM demand 99.174-99.244 | REACTED | first contact Mon 06 from above; reacted wick-rejection Mon 07 (3.1 p wick past far edge, closed back) |
| 1H (Mitigated 2x) MoM demand 99.001-99.097 | REACTED | first contact Mon 08 from above; reacted turn Mon 10 |
| 1H (Unmitigated) MoM demand 98.844-98.889 | not reached | |
| LSZ supply 99.359-99.409 (reach 99.509) | REACTED | first contact Tue 13 from below; reacted turn Tue 14 |
| LSZ supply 99.27-99.32 (reach 99.42) | REACTED | first contact Mon 06 from below; reacted turn Mon 06 |
| LSZ demand 99.251-99.301 (reach 99.151) | PIERCED | first contact Mon 06 from above; pierced Mon 08 (5.9 p past far edge, close beyond) |
| LSZ supply 98.857-98.907 (reach 99.007) | REACTED | first contact Mon 12 from above; reacted turn Mon 13 |
| LSZ demand 98.844-98.894 (reach 98.744) | not reached | |
| band 99.449-99.503 | REACTED | first contact Wed 08 from below; reacted turn Wed 10 |
| band 99.359-99.413 | REACTED | first contact Tue 13 from below; reacted turn Tue 14 |
| band 99.244-99.298 | PIERCED | first contact Mon 06 from above; pierced Mon 06 (7.4 p past far edge, close beyond) |
| band 99.125-99.179 | PIERCED | first contact Mon 06 from above; pierced Mon 08 (3.3 p past far edge, close beyond) |
| band 98.996-99.05 | REACTED | first contact Mon 12 from above; reacted turn Mon 13 |
| band 98.885-98.939 | not reached | |
Reached 13, reacted 9, pierced 4. Unzoned turning points: none (98.98, 98.944, 99.434, 99.472, 98.966, 99.078, 99.515, 99.092, 99.172 all have a box within 2 p).
**E1 = 9 / (13 + 0) = 69 %.** Gate: **FAIL - bunched.** 99.15-99.32 holds two 1H MoM demand boxes, an LSZ demand, an LSZ supply and two bands (six boxes in 17 p); in the zones frame "LSZ demand-side | sweep to 99.151" is printed under "1H (Unmitigated) | MoM" at 99.27 and is unreadable. The anchor price (99.301) sits inside four of them; three were crossed in the first two hours.

### Step 3 - E2
| day | forecast | candles (facts day) | verdict |
|---|---|---|---|
| Mon | SS range 98.963-99.509, key LSZ | 98.946-99.307, down-up-down inside | RIGHT |
| Tue | SS range | 98.944 -> 99.434 | RIGHT |
| Wed | SS range | 99.472 -> 98.966 -> 99.136 | RIGHT |
| Thu | SS range | 99.064 -> 99.515 (0.6 p over the reach) -> 99.092 | RIGHT |
| Fri | SS range | 99.172-99.412 | RIGHT |
**E2 = 5 / 5 = 100 %.** (A whole-week range read with one identical box and tag per day.)

### Step 4 - E3
| obvious trade | setup | verdict |
|---|---|---|
| A Mon SHORT 99.307 | none (two Mon "SS up" variants rejected for RRR) | MISSED |
| B Mon-Tue LONG 98.944 | DX2 LONG 99.050 / 98.971 / 99.409 filled Mon 11:30, **STOPPED Mon 16:15** (low 98.971) - the real low came at 98.944 Mon 22:00 | MISSED |
| C Wed SHORT 99.472 | DX1 SHORT 99.359 / 99.459 / 99.047 filled Tue 13:15, **STOPPED Wed 08:15** (99.471) - one candle before the 51 p drop | MISSED |
| D Thu LONG 99.078 | none | MISSED |
| E Thu SHORT 99.515 | none | MISSED |
Stopped-out setups: **DX2** LONG 99.050 (Mon 11:30 -> 16:15), **DX1** SHORT 99.359 (Tue 13:15 -> Wed 08:15). Both of the week's only two setups were stopped.
**E3 = 0 / 5 = 0 %.**

### Step 5 - presentation
- History half: "LSZ demand-side | sweep to 99.151" overprinted by "1H (Unmitigated) | MoM"; "LSZ demand-side | sweep to 98.744" overprinted by "1H (Unmitigated) | MoM" at 98.85; "supply-side | sweep to 99.007" clipped at the left edge.
- Week frames: the DX1 label sits on Monday's first candles, DX2's label is hidden behind candles ("DX2 SS L 4.5R" barely legible); five identical day boxes cover all candles.

## Map 11 - EURUSD 2026-05-18

Week action (1H, UTC, from the anchor): Mon 06 1.16219 -> 1.16572 (12) -> 1.16287 (18) -> 1.16617 (22); Tue down to 1.15921 (15); Wed 1.15836 (08) -> 1.15827 (14) -> spike 1.16448 (15) -> 1.1616-1.1636; Thu 1.16352 (01) -> 1.1594 (07) -> 1.16353 (08) -> 1.15762 (13) -> 1.163 (17); Fri chop 1.15882-1.1619.

### Step 1 - obvious trades (written from the `_zones` frame before opening any setup)
| # | move | from zone -> to zone |
|---|---|---|
| A | Mon-Tue SHORT 1.1662 -> 1.1592 (-70 p) | band 1.16604-1.16672 / UPPER RESISTANCE 1.16641 -> MID-RANGE SUPPORT 1.15970-1.16036 |
| C | Wed LONG 1.1583 -> 1.1645 (+62 p) | band 1.15747-1.15815 -> 1H Mitigated supply 1.16456-1.16574 |
| E | Thu SHORT 1.1635 -> 1.1576 (-59 p) | 1H MoM supply 1.16266-1.16356 -> band 1.15747-1.15815 |
| F | Thu LONG 1.1576 -> 1.1630 (+54 p) | band 1.15747-1.15815 -> 1H MoM supply 1.16266-1.16356 |
Not counted: Mon 1.16219 -> 1.16572 (+35 p), Thu 01-08 1.1635 -> 1.1594 -> 1.1635 (two 41 p spike candles, not clean legs). Obvious trades: 4.

### Step 2 - E1
| zone (facts) | verdict at first contact | delta (UTC hour) |
|---|---|---|
| IP UPPER RESISTANCE 1.16641-1.16726 | not reached | |
| IP UPPER RESISTANCE 1.16493-1.16562 | REACTED | first contact Mon 11 from below; reacted stall Mon 13 |
| IP EQUILIBRIUM ZONE 1.16219-1.16296 | PIERCED | first contact Mon 06 from below; pierced Mon 06 (6.9 p past far edge, close beyond) |
| IP MID-RANGE SUPPORT 1.1597-1.16036 | REACTED | first contact Tue 13 from above; reacted turn Tue 14 |
| 1H (Unmitigated) MoM supply 1.16655-1.16726 | not reached | |
| 1H (Mitigated 2x) MoM supply 1.16456-1.16574 | REACTED | first contact Mon 11 from below; reacted stall Mon 13 |
| 1H (Unmitigated) MoM supply 1.16266-1.16356 | PIERCED | first contact Mon 06 from below; pierced Mon 08 (9.5 p past far edge, close beyond) |
| LSZ supply 1.16676-1.16726 (reach 1.16826) | not reached | |
| LSZ demand 1.16657-1.16707 (reach 1.16557) | REACTED | first contact Mon 12 from below; reacted turn Mon 14 |
| LSZ supply 1.16211-1.16261 (reach 1.16361) | PIERCED | first contact Mon 06 from below; pierced Mon 08 (9.0 p past far edge, close beyond) |
| LSZ demand 1.16168-1.16218 (reach 1.16068) | REACTED | first contact Tue 09 from above; reacted stall Tue 11 |
| LSZ demand 1.16083-1.16133 (reach 1.15983) | REACTED | first contact Tue 10 from above; reacted turn Tue 14 |
| band 1.16705-1.16773 | not reached | |
| band 1.16604-1.16672 | REACTED | first contact Mon 20 from below; reacted turn Tue 00 |
| band 1.16477-1.16545 | REACTED | first contact Mon 11 from below; reacted stall Mon 13 |
| band 1.16327-1.16395 | PIERCED | first contact Mon 06 from below; pierced Mon 08 (5.6 p past far edge, close beyond) |
| band 1.16203-1.16271 | PIERCED | first contact Mon 06 from below; pierced Mon 06 (9.4 p past far edge, close beyond) |
| band 1.16094-1.16162 | REACTED | first contact Tue 09 from above; reacted stall Tue 12 |
| band 1.15747-1.15815 | REACTED | first contact Thu 13 from above; reacted turn Thu 13 |
| band 1.15619-1.15687 | not reached | |
| band 1.15503-1.15571 | not reached | |
Reached 15, reacted 10, pierced 5. **Unzoned turning points: 1** - Fri 14:00 low 1.15882 (+31 p after; 6.7 p above the nearest box).
**E1 = 10 / (15 + 1) = 63 %.** Gate: **FAIL - bunched.** 1.1620-1.1640 holds EQUILIBRIUM, 1H MoM supply, an LSZ supply, an LSZ demand and two bands (all five that sit at the anchor price were crossed in the first two hours); 1.1645-1.1673 holds two IP, two S/D, two LSZ and three bands. In the zones frame the labels at 1.1666 and 1.1650 print over each other ("UPPER RESISTANCE | HEAVY" over "1H (Mitigated 2x) | MoM", the 3.7bn / 1.5bn strike labels on top of each other).

### Step 3 - E2
| day | forecast | candles (facts day) | verdict |
|---|---|---|---|
| Mon | SS range 1.15970-1.16562, key UPPER RESISTANCE | 1.16219-1.16608, up-down-up inside (4.6 p over the ceiling) | RIGHT |
| Tue | SS range | 1.16617 -> 1.15921 (ceiling to floor) | RIGHT |
| Wed | SS range | 1.15827 (14 p under the floor, closes up to 9 p under for 6 h) -> 1.16448 | RIGHT (oscillation; floor undercut noted) |
| Thu | SS range | 1.16353 -> 1.15762 (21 p under the floor) -> 1.163 | RIGHT (oscillation; floor undercut noted) |
| Fri | SS range | 1.15882-1.16205 | RIGHT |
**E2 = 5 / 5 = 100 %.**

### Step 4 - E3
| obvious trade | setup | verdict |
|---|---|---|
| A Mon-Tue SHORT 1.1662 | EU1 SHORT 1.16512 / 1.16575 / 1.15970 filled Mon 11:30, **STOPPED Mon 20:15** (1.16608) - 2 h before the top, then price went to the TP | MISSED |
| C Wed LONG 1.1583 | none | MISSED |
| E Thu SHORT 1.1635 | none | MISSED |
| F Thu LONG 1.1576 | none | MISSED |
Stopped-out setups: **EU2** SHORT 1.16297 (Mon 06:00 -> 07:15), **EU1** SHORT 1.16512 (Mon 11:30 -> 20:15). Both of the week's setups were stopped on Monday; nothing was offered Tue-Fri.
**E3 = 0 / 4 = 0 %.**

### Step 5 - presentation
- Zones / all frames: labels at 1.1665 and 1.1650 overprint each other and are unreadable; "LSZ supply-side | sweep to 1.16361" and "LSZ demand-side | sweep to 1.16068" are stacked at 1.1622 over the May 16-18 candles.
- Week frame: "EU1 SS S 8.6R" and "EU2 SS S 3.7R" labels over Monday's candles; two strike labels overlap at 1.1650; day tags "80%" barely visible.

## Map 12 - GBPUSD 2026-05-18

Week action (1H, UTC, from the anchor): Mon 06 1.33217 -> 1.34029 (12) -> 1.33801 (13) -> 1.34494 (16) -> 1.34004 (19) -> 1.34391 (20); Tue stair-step down to 1.33785 (14); Wed 1.3375 (08) -> 1.3463 (15), then 1.343-1.345; Thu 1.34548 (08) -> 1.33904 (13) -> 1.34492 (17); Fri 1.34132 (07) -> 1.34631 (13) -> 1.34177 -> 1.34535 -> 1.34195.

### Step 1 - obvious trades (written from the `_zones` frame before opening any setup)
| # | move | from zone -> to zone |
|---|---|---|
| A1 | Mon LONG 1.3322 -> 1.3403 (+81 p) | GAP 1.33240-1.33300 / LSZ 1.33203 -> UPPER RESISTANCE 1.33950-1.34037 |
| A2 | Mon LONG 1.3380 -> 1.3449 (+69 p) | band 1.33816-1.33933 / LSZ reach 1.3385 -> UPPER RESISTANCE 1.34497-1.34557 |
| C | Mon-Tue SHORT 1.3449 -> 1.3379 (-71 p) | UPPER RESISTANCE 1.34497 -> GAP 1.33720-1.33780 |
| D | Wed LONG 1.3375 -> 1.3463 (+88 p) | GAP 1.33720-1.33780 -> UPPER RESISTANCE 1.34497 (7 p over it) |
| E | Thu SHORT 1.3455 -> 1.3390 (-64 p) | UPPER RESISTANCE 1.34497 -> LSZ demand 1.33950 (reach 1.3385) |
| F | Thu LONG 1.3390 -> 1.3449 (+59 p) | LSZ demand 1.33950 -> UPPER RESISTANCE 1.34497 |
Not counted: Fri 1.3413 -> 1.3463 -> 1.3418 (spike candles out of a 5 h chop). Obvious trades: 6.

### Step 2 - E1
| zone (facts) | verdict at first contact | delta (UTC hour) |
|---|---|---|
| IP UPPER RESISTANCE 1.34497-1.34557 | REACTED | first contact Wed 15 from below; reacted wick-rejection Wed 15 (7.3 p wick past far edge, closed back) |
| IP UPPER RESISTANCE 1.3395-1.34037 | REACTED | first contact Mon 12 from below; reacted turn Mon 13 |
| IP MID-RANGE SUPPORT 1.32995-1.33055 | not reached | |
| IP KEY SUPPORT BAND 1.32484-1.32544 | not reached | |
| GAP 1.34239-1.34299 | PIERCED | first contact Mon 15 from below; pierced Mon 16 (19.5 p past far edge, close back inside/below) |
| GAP 1.3372-1.3378 | REACTED | first contact Mon 08 from below; reacted wick-rejection Mon 08 (6.3 p wick past far edge, closed back) |
| GAP 1.33492-1.33552 | REACTED | first contact Mon 06 from below; reacted turn Mon 07 |
| GAP 1.3324-1.333 | PIERCED | first contact Mon 06 from below; pierced Mon 06 (28.3 p past far edge, close beyond) |
| GAP 1.32668-1.32728 | not reached | |
| 1H (Unmitigated) MoM supply 1.33941-1.34037 | REACTED | first contact Mon 12 from below; reacted turn Mon 13 |
| LSZ supply 1.33987-1.34037 (reach 1.34137) | REACTED | first contact Mon 12 from below; reacted turn Mon 13 |
| LSZ demand 1.3395-1.34 (reach 1.3385) | REACTED | first contact Mon 12 from below; reacted turn Mon 13 |
| LSZ supply 1.33203-1.33253 (reach 1.33353) | PIERCED | first contact Mon 06 from below; pierced Mon 06 (23.0 p past far edge, close beyond) |
| LSZ demand 1.33147-1.33197 (reach 1.33047) | not reached | |
| LSZ demand 1.33022-1.33072 (reach 1.32922) | not reached | |
| band 1.34423-1.3454 | REACTED | first contact Mon 16 from below; reacted turn Mon 16 |
| band 1.34222-1.34339 | PIERCED | first contact Mon 15 from below; pierced Mon 16 (15.5 p past far edge, close back inside/below) |
| band 1.33816-1.33933 | REACTED | first contact Mon 08 from below; reacted turn Mon 09 |
| band 1.33527-1.33644 | REACTED | first contact Mon 06 from below; reacted turn Mon 07 |
| band 1.33264-1.33381 | PIERCED | first contact Mon 06 from below; pierced Mon 06 (20.2 p past far edge, close beyond) |
| band 1.33025-1.33142 | not reached | |
| band 1.32856-1.32973 | not reached | |
| band 1.32569-1.32686 | not reached | |
| band 1.32394-1.32511 | not reached | |
Reached 15, reacted 10, pierced 5. **Unzoned turning points: 3** - Wed 15:00 top 1.3463 (-42 p after; 7.3 p above UPPER RESISTANCE), Fri 13:00 top 1.34631 (-45 p; 7.4 p above it), Fri 07:00 low 1.34132 (+50 p; 9 p under the nearest band).
**E1 = 10 / (15 + 3) = 56 %.** Gate: **FAIL - missing + floating + bunched.** Missing: the 1.3455-1.3465 ceiling that capped Wed, Thu and Fri has only the edge of one box under it, and nothing at the 1.3413 Friday low. Floating: MID-RANGE SUPPORT, KEY SUPPORT BAND, GAP 1.32668, two LSZ demand and five bands (11 objects) sit 15-75 p under the week low (1.33217) and were never reached. Bunched: at 1.3395-1.3414 UPPER RESISTANCE, 1H MoM supply, an LSZ supply and an LSZ demand overlap; their labels print over each other in the zones frame.

### Step 3 - E2
| day | forecast | candles (facts day) | verdict |
|---|---|---|---|
| Mon | SS range 1.33047-1.34037, key 1H MoM supply | breakout up 1.33217 -> 1.34494, 1H closes up to 1.3434 (30 p over the box) | WRONG |
| Tue | SS range | 1.33785-1.34371, closes up to 1.3434 (30 p over the ceiling) | WRONG - range day, but around a level 30 p above the forecast bounds |
| Wed | SS range | BS up 1.3375 -> 1.3463, closes 1.3441 (37 p over) | WRONG |
| Thu | SS range | 1.33904-1.34548, closes 1.3405-1.3443 - above the box all day | WRONG |
| Fri | SS range | 1.34132-1.34631, all closes 1.3419-1.3449 - above the box | WRONG |
**E2 = 0 / 5 = 0 %.** The forecast range was correct only for Monday's first six hours; from Monday 12:00 the week traded above the box.

### Step 4 - E3
| obvious trade | setup | verdict |
|---|---|---|
| A1 Mon LONG 1.3322 | GB2 LONG 1.33197 / 1.33132 / 1.33941, filled Mon 06:00, TP Mon 12:30 | CAUGHT |
| A2 Mon LONG 1.3380 | none (GB2 re-arm never filled) | MISSED |
| C Mon-Tue SHORT 1.3449 | none at 1.3449; GB1 SHORT 1.33983 / 1.34067 filled Mon 12:30, **STOPPED Mon 15:30** | MISSED |
| D Wed LONG 1.3375 | none | MISSED |
| E Thu SHORT 1.3455 | none | MISSED |
| F Thu LONG 1.3390 | none | MISSED |
Stopped-out setups: **GB1** SHORT 1.33983 (Mon 12:30 -> 15:30).
**E3 = 1 / 6 = 17 %.**

### Step 5 - presentation
- Week frames: the five day boxes (1.3305-1.3404) and the yellow zig-zag 1.3320 <-> 1.3395 sit under the candles from Monday 12:00 to Friday - the drawn forecast and the price do not overlap for four days.
- Zones frame: "UPPER RESISTANCE | MODERATE" and "1H (Unmitigated) | MoM" print over each other at 1.3400; "LSZ demand-side | sweep to 1.32922" is hidden under "MID-RANGE SUPPORT" at 1.3302; GB1 label over Monday's candles.

---

## Summary table (all 12 maps)

| map | E1 | E2 | E3 | E1 gate (none bloated / bunched / floating / missing) |
|---|---|---|---|---|
| DXY 2026-07-06 | 17/18 = 94 % | 5/5 = 100 % | 7/7 = 100 % | FAIL (bunched) |
| EURUSD 2026-07-06 | 16/16 = 100 % | 5/5 = 100 % | 6/7 = 86 % | FAIL (bunched) |
| GBPUSD 2026-07-06 | 19/27 = 70 % | 5/5 = 100 % | 4/7 = 57 % | FAIL (bunched) |
| DXY 2026-04-20 | 28/28 = 100 % | 4/5 = 80 % | 2/2 = 100 % | FAIL (bunched) |
| EURUSD 2026-04-20 | 23/23 = 100 % | 4/5 = 80 % | 1/5 = 20 % | FAIL (bunched) |
| GBPUSD 2026-04-20 | 13/18 = 72 % | 2/5 = 40 % | 0/8 = 0 % | FAIL (missing, floating, bunched) |
| DXY 2026-10-05 | 7/11 = 64 % | 5/5 = 100 % | 1/6 = 17 % | FAIL (missing) |
| EURUSD 2026-10-05 | 8/11 = 73 % | 4/5 = 80 % | 0/7 = 0 % | FAIL (missing) |
| GBPUSD 2026-10-05 | 5/16 = 31 % | 3/5 = 60 % | 2/7 = 29 % | FAIL (missing, bunched) |
| DXY 2026-05-18 | 9/13 = 69 % | 5/5 = 100 % | 0/5 = 0 % | FAIL (bunched) |
| EURUSD 2026-05-18 | 10/16 = 63 % | 5/5 = 100 % | 0/4 = 0 % | FAIL (bunched) |
| GBPUSD 2026-05-18 | 10/18 = 56 % | 0/5 = 0 % | 1/6 = 17 % | FAIL (missing, floating, bunched) |
| **All 12 - pooled counts** | **165/215 = 77 %** | **47/60 = 78 %** | **24/71 = 34 %** | 12 / 12 FAIL |
| All 12 - mean of map % | 74 % | 78 % | 35 % | |
| **9 maps outside 2026-07-06 - pooled counts** | **113/154 = 73 %** | **32/45 = 71 %** | **7/50 = 14 %** | 9 / 9 FAIL |
| 9 maps outside 2026-07-06 - mean of map % | 70 % | 71 % | 20 % | |

E1 denominators = zones reached + unzoned turning points. Against the >= 90 % target: E1 reaches it on 4 maps (DXY / EURUSD 07-06 and DXY / EURUSD 04-20 - exactly the maps where boxes cover every price), E2 on 6 maps, E3 on 2 maps (DXY 07-06, DXY 04-20). Outside the anchor week E3 catches 7 of 50 obvious trades.

Stopped-out setups across the 12 maps: EU2 + EU4 re-arm (EURUSD 07-06); DX6 (DXY 04-20); GB2 (GBPUSD 04-20); DX2 (DXY 10-05); EU1 (EURUSD 10-05); GB1 re-arm + GB2 2nd re-arm (GBPUSD 10-05); DX1 + DX2 (DXY 05-18); EU1 + EU2 (EURUSD 05-18); GB1 (GBPUSD 05-18). That is 14 named stops; no stop on DXY 07-06, GBPUSD 07-06, EURUSD 04-20.

## The five defects that cost the most

1. **E3 offers almost nothing after Monday outside the anchor week (cost: 43 of 50 obvious trades missed).** Most non-anchor maps carry 2-6 setups, all built on Monday's range bounds, and none is re-issued after a stop or after price leaves the range. Examples: EURUSD 2026-05-18 - both setups stopped on Monday (EU2 1.16297 Mon 07:15, EU1 1.16512 Mon 20:15), then nothing while 1.1662 -> 1.1592 (Tue), 1.1583 -> 1.1645 (Wed 14-15), 1.1635 -> 1.1576 -> 1.1630 (Thu) ran; GBPUSD 2026-04-20 - 0 of 8 swings of 56-89 p between 1.3474 and 1.3544 (Mon-Fri) traded; EURUSD 2026-10-05 - 0 of 7.
2. **Stops sit inside the sweep reach, so setups at the right zone are stopped minutes to hours before the turn.** DXY 2026-05-18 DX1 SHORT 99.359 / SL 99.459 stopped Wed 08:15 at 99.471, then 99.472 -> 98.966 (Wed 14-15); DX2 LONG 99.050 / SL 98.971 stopped Mon 16:15, true low 98.944 Mon 22:00, then +49 p. EURUSD 2026-05-18 EU1 SL 1.16575 stopped Mon 20:15 at 1.16608; top 1.16617 Mon 22:00, then -70 p to its own TP. DXY 2026-10-05 DX2 LONG 101.926 / SL 101.825 stopped Tue 11:30 at the 101.754 low, then +75 p. GBPUSD 2026-04-20 GB2 SHORT 1.35163 / SL 1.35243 stopped Mon 11:15 before the 1.35444 top. (Canon itself expects the sweep 0.05-0.10 beyond the extreme.)
3. **E2 freezes Monday's range box for all five days and never registers a breakout.** GBPUSD 2026-05-18: box 1.33047-1.34037 every day while price traded above it from Mon 12:00 to Fri close (Mon 1.34494, Wed 1.3463, Fri 1.34631) - 0/5. GBPUSD 2026-10-05: Tue 1.32856 / Wed 1.32761 against a box top of 1.32395 (Tue, Wed WRONG). GBPUSD 2026-04-20 Mon close 1.35333 vs box top 1.35019. EURUSD 2026-10-05 Tue closes 1.1273-1.1278 vs ceiling 1.12612. The day path is a fixed zig-zag (DXY/EURUSD/GBPUSD 10-05 and 05-18) unrelated to the candles.
4. **No zone at the week's biggest turning points (E1 missing).** GBPUSD 2026-10-05 Tue 15:00 top 1.32856 (-92 p after; nothing within 18 p); GBPUSD 2026-04-20 Mon 15:00 1.35444 and Tue 14:00 1.35396 (zones stop at 1.35327 although price traded above); GBPUSD 2026-05-18 Wed 15:00 1.3463 and Fri 13:00 1.34631 plus Fri 07:00 low 1.34132; DXY 2026-10-05 Mon 06:00 102.433 and Mon 14:00 102.372; EURUSD 2026-10-05 Thu 11:00 1.11719 and Thu 16:00 1.11845. At the same time 11 GBPUSD 2026-05-18 objects float 15-75 p under a week low that was never revisited.
5. **E1 bloat / bunching at the anchor price, with unreadable labels.** 24-36 objects per map on 07-06 and 04-20 covering every price (GBPUSD 2026-07-06: 36 objects in 1.326-1.346), un-merged LSZ boxes less than 1 p apart (DXY 2026-04-20 98.235 / 98.241 / 98.242; GBPUSD 2026-07-06 1.33340 / 1.33341), and stacks sitting on the anchor price that were crossed in the first two hours (EURUSD 2026-05-18: EQUILIBRIUM, 1H MoM supply, LSZ supply and two bands at 1.1620-1.1640 pierced Mon 06-08; GBPUSD 2026-10-05: two gaps, two LSZ and a band at 1.3212-1.3233 pierced Mon 06-08; GBPUSD 2026-07-06: six boxes at 1.3354-1.3381 crossed Mon 13-18). Labels overprint each other at EURUSD 2026-04-20 1.1760, DXY 2026-04-20 98.40, GBPUSD 2026-07-06 1.3400 / 1.3375 / 1.3280, EURUSD 2026-05-18 1.1666 / 1.1650, DXY 2026-05-18 99.27.

Also noted (smaller): E2 "RWL" forecast for Fridays that were one-way moves (DXY 2026-04-20 Fri, EURUSD 2026-04-20 Fri, GBPUSD 2026-04-20 Fri); the anchor week's E3 misses are reinforcement / late-week trades (EURUSD Thu 1.14233; GBPUSD Wed 1.33629, Thu 1.33829, Fri 1.34481); purple Thu/Fri day tags are drawn on top of the candles in every 07-06 and 04-20 frame.
