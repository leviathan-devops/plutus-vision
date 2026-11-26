# G1 outside count 4 (fresh reviewer, strict)

Reviewer: outside reviewer with fresh context. Not the builder. No earlier count, no memory/, no tool code was read.
Inputs used: audit/G1_brief4.md, the 36 frames in evidence/s3d/ (every one opened), audit/g1_facts_d/*.txt (prices, times), context_management/oracle/golden_week.json (operator trades, 2026-07-06 only), 1H bars via `e1_tool/e1_data.py bars()` read-only (to check times, highs/lows, closes). All times UTC (the chart axis is UTC).

## Counting rules applied (so anyone can recount)

Rule G1 verbatim: "One verdict per drawing with its specific delta - zone: reacted (sharp rejection OR consolidation in / around it) / pierced like paper / not reached; day: forecast shape + direction + key zone vs that day's candles; setup: filled? TP before SL? Counting for a week: E1 = zones that reacted / (zones reached + obvious reaction points of the week that have no zone), and none bloated, bunched, floating or missing; E2 = days right / 5; E3 = obvious trades caught / obvious trades that existed (anchor week: his own trades; other weeks: every clean zone-to-zone move visible on the 1H chart, listed BEFORE looking at my setups), every stopped-out setup named."

How I applied it:
- Unit of E1 count = one line of the facts file "ENGINE 1 OBJECTS ON THE CHART" (pressure zones, gap in-fill, supply/demand, sweep zones, V1 liquidity bands). Amber option-strike lines are levels, not zones, and are not counted.
- Forecast week = from the anchor (Mon 06:00 UTC = Mon 02:00 New York) to Friday's close; candles before the anchor are history and do not count for or against any engine.
- Reached = a 1H wick of the forecast week entered the box (for a sweep zone: the box or its dotted reach).
- REACTED = within the box (or within ~3 pips DXY / ~5 pips FX beyond its far edge; for a sweep zone, within its dotted reach) price turned by at least ~10 pips DXY / ~15 pips FX, or stalled there for 3+ 1H candles. PIERCED = price crossed the whole box (and a sweep zone's reach) without such a turn or stall. A zone that reacted once and was later crossed counts as REACTED (first verdict wins) but the later piercing is noted.
- Obvious reaction points with no zone = the week's day highs/lows and every 1H swing that turned >= ~20 pips DXY / ~30 pips FX, with no Engine 1 box within ~3 pips DXY / ~5 pips FX. Each adds 1 to the denominator.
- E1 % = reacted / (reached + unzoned reaction points). The second clause ("none bloated, bunched, floating or missing") is reported as a separate gate PASS / FAIL per map; it is not folded into the %.
- E2: a day is RIGHT only if the forecast shape matches what the day's 1H candles did (canon definitions in the brief) AND the forecast direction is the day's direction (the main move; for a compound tag such as BS+WL+RWL the direction is that of the first leg, the later legs being the reversal the tag itself announces). The key zone counts as right when the day's turn or target is at it. A day box drawn away from where the day traded is listed as a presentation defect, not a WRONG day (G1 names shape + direction + key zone only).
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
| zone (facts) | verdict | delta |
|---|---|---|
| IP RESISTANCE CEILING 1.34484-1.34548 | REACTED | Fri 1.34517 -> -60 p |
| IP UPPER RESISTANCE 1.33933-1.34005 | REACTED | Mon 22 / Tue 01 top 1.34015 -> -58 p; Fri low 1.33918 |
| IP UPPER RESISTANCE 1.33643-1.33717 | REACTED | Tue 13-19 stall 1.3360-1.3376; Wed 06 1.33702 -> -48 p |
| IP UPPER RESISTANCE 1.33435-1.33521 | REACTED | Mon 07-12 highs 1.33502 / 1.33516; Tue 22-Wed 01 lows 1.3343 |
| IP MID-RANGE SUPPORT 1.33225-1.33285 | REACTED | Wed 08 1.33222 -> +88 p |
| IP KEY SUPPORT BAND 1.32970-1.33046 / 1.32789-1.32877 | not reached | |
| GAP 1.34234-1.34294 | REACTED | Thu 05 1.34308 -> -50 p |
| GAP 1.34029-1.34089 | REACTED | Wed 17 1.34104 -> -30 p |
| GAP 1.33744-1.33804 | REACTED | Tue 04-09 lows 1.3375; Thu 11 1.33807 -> +44 p |
| 1H BoM supply 1.34502-1.34599 | REACTED | Fri 1.34517 |
| 4H BoM supply 1.34264-1.34340 | REACTED | Thu 1.34308 |
| 4H MoM supply 1.34035-1.34162 | REACTED | Wed 17 1.34104 |
| 1H MoM supply 1.33941-1.34032 | REACTED | Mon/Tue 1.34015 |
| 1H BoM supply 1.33623-1.33764 | REACTED | Wed 06 1.33702 |
| 1H MoM supply 1.33544-1.33582 | REACTED | Mon 00 1.33566; Wed 01-10 1.33593 / 1.33568 |
| 1H MoM demand 1.33082-1.33333 | REACTED | Mon 07 1.33286, Wed 08 1.33222 |
| demand 1.32862-1.32928 / 4H 1.32639-1.32835 / 1H BoM 1.32744-1.32800 | not reached | |
| LSZ supply 1.33796-1.33846 (reach 1.33946) | REACTED | Mon top 1.34013 (6.7 p beyond reach) then Mon 19-Tue 12 stall 1.3375-1.3401 |
| LSZ supply 1.33760-1.33810 (reach 1.33910) | REACTED (weak) | crossed Mon 16-17 without a stop; only the Tue stall around it |
| LSZ supply 1.33516-1.33566 (reach 1.33666) | REACTED | Wed 06 1.3366 -> down |
| LSZ demand 1.33341-1.33391 / 1.33340-1.33390 (reach 1.3324) (2) | REACTED (2) | Mon 06 1.33301; Wed 1.33222 (1.8 p beyond reach) -> up |
| LSZ supply 1.32871-1.32921 / 1.32717-1.32767 | not reached | |
| band 1.34540-1.34630 | not reached | Fri high 1.34517 |
| band 1.34386-1.34476 | REACTED | Fri reversal at 1.34517 (4 p above it) |
| band 1.34145-1.34235 | REACTED | Thu 16-Fri 05 lows 1.3415-1.3422 |
| band 1.33976-1.34066 | REACTED | Mon/Tue top, Fri low 1.33918 |
| band 1.33715-1.33805 | REACTED | Tue lows, Thu 1.33807 |
| band 1.33583-1.33673 | REACTED | Tue 13-19 stall |
| band 1.33406-1.33496 | REACTED | Mon chop, Wed 01 low 1.33422 |
| band 1.33155-1.33245 | REACTED | Wed 1.33222 |
| band 1.32932-1.33022 | not reached | |
Reached 27, reacted 27, pierced 0. Unzoned turning points: none.
**E1 = 27 / 27 = 100 %.** Gate: **FAIL - bunched/bloated.** 36 objects (7 IP, 3 gap, 10 S/D, 7 LSZ, 9 bands) inside 1.326-1.346; the zones frame is boxes from top to bottom, with labels printed on top of each other (UPPER RESISTANCE / 1H MoM at 1.3400; GAP / 1H BoM / UPPER RESISTANCE at 1.3375; KEY SUPPORT / 1H BoM / 4H MoM at 1.3280). Two identical LSZ demand boxes (1.33341 and 1.33340).

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
| zone (facts) | verdict | delta |
|---|---|---|
| IP UPPER RESISTANCE 98.939-99.005 | REACTED | Thu 17 high 98.939 = lower edge -> -18 p; Fri 98.915 -> -43 p |
| IP UPPER RESISTANCE 98.456-98.541 | REACTED | Tue 17 98.567 (2.6 p beyond) -> -36 p; Fri 16-20 stall 98.49-98.52 |
| IP MID-RANGE SUPPORT 98.058-98.145 | REACTED | Mon 16 - Tue 06 stall 98.01-98.16 |
| IP KEY SUPPORT BAND 97.725-97.799 | not reached | |
| GAP 98.806-98.866 | REACTED | Thu 19 - Fri 06 stall 98.76-98.915 |
| GAP 98.667-98.727 | REACTED | Wed 22 - Thu 10 stall |
| GAP 98.220-98.280 | REACTED | Wed 05 98.211 -> +73 p |
| GAP 97.988-98.048 | REACTED | Mon 15 98.006 -> stall, then +56 p |
| 4H BoM supply 98.884-99.031 | REACTED | Thu 98.939, Fri 98.915 |
| 1H MoM supply 98.675-98.845 | REACTED | Thu 10 98.803 -> 98.534 |
| 1H MoM supply 98.402-98.439 | REACTED | Mon 04-06 98.395 (0.7 p below) -> -39 p |
| 1H MoM demand 97.937-98.045 | REACTED | Mon 98.006 |
| 1H BoM demand 97.632-97.828 / 4H BoM demand 97.576-97.728 | not reached | |
| LSZ supply 98.389-98.439 / 98.345-98.395 (2) | REACTED (2) | Mon 98.395 |
| LSZ demand 98.364-98.414 (reach 98.264) | REACTED | Tue 22 - Wed 03 stall 98.31-98.41 (then Wed wick 98.211, 5 p beyond reach) |
| LSZ supply 98.242-98.292 / 98.241-98.291 / 98.235-98.285 (3) | REACTED (3) | Mon 01-06 chop, high 98.395 at the reach |
| LSZ demand 98.261-98.311 (reach 98.161) | REACTED | Mon 07-12 stall 98.155-98.34 (crossed Mon 13 to 98.006); Wed 98.211 bounce |
| LSZ demand 98.005-98.055 / 97.969-98.019 (2) | REACTED (2) | Mon 98.006 |
| LSZ demand 97.832-97.882 / 97.632-97.682 | not reached | |
| bands 98.903-98.967, 98.804-98.868, 98.689-98.753, 98.561-98.625, 98.461-98.525, 98.300-98.364, 98.182-98.246, 98.014-98.078 (8) | REACTED (8) | each at a turn or stall listed above |
| bands 97.920-97.984, 97.768-97.832, 97.666-97.730 | not reached | |
Reached 28, reacted 28, pierced 0. Unzoned turning points: none.
**E1 = 28 / 28 = 100 %.** Gate: **FAIL - bunched/bloated.** 36 objects between 97.53 and 99.03; between 98.18 and 98.44 there are 6 LSZ + 1 gap + 1H MoM supply + 2 bands stacked (three LSZ supply boxes 98.235 / 98.241 / 98.242 are within 0.7 p of each other and should be one box); the labels "LSZ supply-side | sweep to 98.539" and "LSZ demand-side | sweep to 98.264" print over each other at 98.40 in the history half.

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
| zone (facts) | verdict | delta |
|---|---|---|
| IP UPPER RESISTANCE 1.18213-1.18292 / 1.17988-1.18067 | not reached | week high 1.1791 |
| IP UPPER RESISTANCE 1.17706-1.17791 | REACTED | Mon 07-12 highs 1.17718 / 1.17755 stall; Tue 01-07 lows 1.1772-1.1773 stall |
| IP EQUILIBRIUM 1.17497-1.17573 | REACTED | Mon 04 1.1747 -> +44 p; Wed 05 1.17624 (5 p above) -> -93 p |
| IP MID-RANGE SUPPORT 1.16973-1.17033 | REACTED | Wed 19 - Thu 09 chop 1.1690-1.1713 |
| IP KEY SUPPORT BAND 1.16570-1.16638 | not reached | week low 1.16691 |
| GAP 1.17347-1.17407 | REACTED | Tue 22 - Wed 03 stall |
| GAP 1.17203-1.17263 | REACTED | Tue 17-20 lows 1.17201 / 1.17187 -> +44 p; Fri top 1.1723 |
| GAP 1.16744-1.16804 | REACTED | Thu 11 1.16789; Fri 01-07 stall 1.1673-1.1676 |
| 1H BoM supply 1.18239-1.18491 | not reached | |
| 1H MoM supply 1.17847-1.17988 | REACTED | Mon 13 - Tue 00 stall at 1.178-1.1791 -> -72 p |
| 1H MoM demand 1.17004-1.17207 | REACTED | Tue 19 1.17187 -> +44 p (crossed Wed 21) |
| 4H BoM demand 1.16809-1.16996 | REACTED | Wed 22 1.16921, Thu 11 1.16789 stall |
| 1H BoM demand 1.16638-1.16754 | REACTED | Thu 17 1.16691 -> +54 p |
| 4H MoM demand 1.16543-1.16748 | REACTED | Thu 17 1.16691 |
| LSZ supply 1.18188-1.18238 / 1.18060-1.18110 / 1.18030-1.18080 | not reached | |
| LSZ demand 1.17719-1.17769 (reach 1.17619) | REACTED | Tue 01-06 stall at its lower edge |
| LSZ demand 1.17668-1.17718 (reach 1.17568) | REACTED | Tue 07 1.17565 = reach -> stall |
| LSZ supply 1.17611-1.17661 (reach 1.17761) | REACTED | Mon 07-12 stall under 1.17755; Wed 1.17624 |
| LSZ supply 1.17575-1.17625 (reach 1.17725) | REACTED | Wed 05 1.17624 -> down |
| LSZ demand 1.17592-1.17642 (reach 1.17492) | REACTED | Tue 10-13 1.1754 stall |
| LSZ demand 1.17527-1.17577 (reach 1.17427) | REACTED | Mon 04 1.1747 |
| LSZ demand 1.17277-1.17327 (reach 1.17177) | REACTED | Tue 19 1.17187 |
| LSZ demand 1.16638-1.16688 | not reached | Thu low 1.16691, 0.3 p above |
| bands 1.18125-1.18216, 1.17958-1.18049 | not reached | |
| bands 1.17710-1.17801, 1.17564-1.17655, 1.17327-1.17418, 1.17126-1.17217, 1.16876-1.16967 (5) | REACTED (5) | at the turns / stalls above |
| band 1.16581-1.16672 | not reached | |
Reached 23, reacted 23, pierced 0. Unzoned turning points: none.
**E1 = 23 / 23 = 100 %.** Gate: **FAIL - bunched/bloated.** 34 objects in 1.1654-1.1849; 1.1750-1.1780 holds 2 IP + 6 LSZ + 2 bands; in the zones frame the two LSZ labels at 1.1760 are printed on top of each other and cannot be read ("LSZ supply-side | sweep to ..." over "LSZ demand-side ...").

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
| zone (facts) | verdict | delta |
|---|---|---|
| IP UPPER RESISTANCE 1.35241-1.35327 | REACTED | Mon 16 - Tue 06 stall 1.3515-1.3544 around it; Wed 1.35353, Fri 1.3537 just above |
| IP UPPER RESISTANCE (HEAVY) 1.34932-1.35019 | REACTED | Wed 10-21 lows 1.3492-1.3493 |
| IP MID-RANGE SUPPORT 1.34768-1.34846 | REACTED | Mon 1.34818, Tue 1.34823 / 1.34744, Wed 23 1.34789 -> each +55-60 p; crossed Thu 16 |
| IP KEY SUPPORT BAND 1.33998-1.34073 | not reached | |
| GAP 1.35047-1.35107 | REACTED | Mon 01-06 stall, Tue/Wed chop |
| GAP 1.34640-1.34700 | REACTED | Thu 19 - Fri 06 stall 1.3457-1.3473 |
| GAP 1.34423-1.34483 | REACTED | Thu 17 1.34476 -> +89 p |
| GAP 1.34317-1.34377 | not reached | |
| 1H MoM demand 1.34345-1.34660 | REACTED | Thu 1.34476 |
| 4H BoM demand 1.34017-1.34073 / 1H BoM demand 1.33806-1.33960 | not reached | |
| LSZ demand 1.35163-1.35213 (reach 1.35063) | REACTED | Tue 01-06 stall at 1.3515 (then Tue 07 fell 24 p beyond its reach) |
| LSZ supply 1.35036-1.35086 (reach 1.35186) | REACTED | Mon 01-06 stall under 1.35086 (then crossed to 1.35444) |
| LSZ demand 1.35044-1.35094 (reach 1.34944) | REACTED | Wed 11 1.34925 |
| LSZ demand 1.34952-1.35002 (reach 1.34852) | REACTED | Wed/Thu lows 1.3479-1.3483 |
| LSZ demand 1.34740-1.34790 (reach 1.34640) | REACTED | Tue 20 1.34744 |
| LSZ demand 1.33805-1.33855 | not reached | |
| bands 1.35220-1.35332, 1.34973-1.35085, 1.34691-1.34803, 1.34473-1.34585 (4) | REACTED (4) | |
| bands 1.34227-1.34339, 1.33983-1.34095, 1.33821-1.33933 | not reached | |
Reached 16, reacted 16, pierced 0. **Unzoned turning points: 2** - Mon 15:00 top 1.35444 (11 p above the highest box, 1.35332) and Tue 14:00 top 1.35396 (6.4 p above it). The facts header itself says the zones stop at 1.35327 while the week traded to 1.35444.
**E1 = 16 / 18 = 89 %.** Gate: **FAIL - missing + floating + bunched.** Missing: no zone at the 1.3540-1.3545 ceiling that capped Mon and Tue. Floating: KEY SUPPORT BAND, 4H BoM demand, 1H BoM demand, LSZ 1.33805 and two bands sit 40-70 p under the week low. Bunched: 1.3474-1.3533 is covered wall to wall (IP, 3 gaps, 5 LSZ, 4 bands); in the zones frame "KEY SUPPORT BAND" and "4H (Unmitigated) | BoM" labels print over each other at 1.3405, and "LSZ demand-side" over "supply-side" at 1.3495.

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
| zone (facts) | verdict | delta |
|---|---|---|
| IP MID-RANGE SUPPORT 101.961-102.051 | REACTED | Wed 01-03 stall; Thu 14-17 lows 102.033 / 102.035 -> +33 p; Fri 101.978 |
| IP KEY SUPPORT BAND 101.750-101.843 | REACTED | Tue 11 101.754 -> 12 h stall -> +75 p |
| 1H MoM demand 101.855-101.926 | REACTED | Tue stall; Fri 05 101.92 -> +41 p |
| 1H BoM demand 101.668-101.798 | REACTED | Tue 101.754 inside |
| LSZ supply 102.485-102.535 (reach 102.635) | REACTED | Wed 11 102.499 -> -29 p; Thu 102.467 (1.8 p under) -> -43 p |
| LSZ supply 102.157-102.207 (reach 102.307) | REACTED | Tue 05 102.285 -> -53 p |
| LSZ supply 102.082-102.132 (reach 102.232) | REACTED | Mon 09 102.084, Thu 02 102.133 bounces |
| LSZ demand 101.855-101.905 (reach 101.755) | REACTED | Tue 101.754 = reach |
| LSZ demand 101.668-101.718 | not reached | |
| band 101.916-101.996 | REACTED | Tue/Wed/Fri |
Reached 9, reacted 9, pierced 0. **Unzoned turning points: 2** - Mon 06:00 top 102.433 (-35 p; 5 p under the nearest box) and Mon 14:00 top 102.372 (-27 p; nothing between 102.307 and 102.485).
**E1 = 9 / 11 = 82 %.** Gate: **FAIL - missing** (no zone in 102.31-102.48 where Monday turned twice). Not bloated: 10 objects, readable.

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
