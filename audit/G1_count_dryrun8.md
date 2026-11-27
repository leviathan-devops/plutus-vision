# G1 outside count 8 (fresh reviewer, brief audit/G1_brief8.md)

Reviewer: outside reviewer. I did not read the earlier counts, memory/ or the tool's code. I opened all 36 frames in evidence/s3h/ and judged from the pixels. I used audit/g1_facts_h/*.txt only for exact prices and times. I read 1H / 15m bars read-only through `e1_tool/e1_data.py bars()` to check times, closes and every fill / TP / SL the facts file claims. Every claimed outcome matched the 15m bars, apart from the first-contact notes below.

## Counting rules applied (so anyone can recount)

- **Forecast window.** It starts Monday 02:00 New York (06:00 UTC on all four weeks, which are all in summer time) and ends Friday 17:00 NY. A turn, move or touch before 06:00 UTC Monday is history.
- **E1 (zones).** One verdict per drawn ZONE (a labelled box; its dotted parts count as the zone). A discovery line gets its own verdict.
  - REACTED: a sharp rejection, or consolidation in or around the zone, within about 2 pips.
  - PIERCED: crossed with no reaction anywhere in the week.
  - NOT REACHED: price never got there.
  - E1 % = reacted / (reached + obvious turning points of the week with no E1 object within about 5 pips).
  - Side condition (L-28 reference in the brief):
    - **Bunched:** separate labelled zones whose boxes or parts overlap, or sit 0-2 pips apart, and that one candle crossed together. The reference tolerates 3 pips between two pressure zones and parts joined to a zone.
    - **Floating:** a zone more than about 22 pips beyond the week's extreme. That is the reference map's maximum.
    - **Bloated:** taller than about 35 pips (the reference has 34) or packed with candles.
    - Side condition PASS needs none of these.
- **E2 (days).** For 2026-07-06 the operator's tags are the truth; EURUSD / GBPUSD get the inverted direction. A day is RIGHT only if the forecast tag carries all of his shapes. For the other weeks I judged each day from the candles:
  - Directional tag: RIGHT if the day's dominant move has the tagged shape and direction.
  - SS (range) tag: RIGHT if the day ranged without a decisive breakout, closed inside the forecast box, and went no more than 10 pips beyond the box. The box already includes the bounding sweep reach; 10 pips is the canon's 0.05-0.10 sweep allowance.
  - E2 % = right / 5.
- **E3 (trades).** I wrote down the obvious trades from the `_zones` frame and the 1H bars BEFORE reading the setups. These are clean zone-to-zone moves of roughly 30 pips or more inside the window. For 2026-07-06 I used the operator's own trades in the window, and for DXY 2026-04-20 his two real trades.
  - CAUGHT = a setup of the same direction at that zone or turn that filled and reached TP before SL. For his trades, the entry had to be within about 3 pips (one exception is flagged, GBP 07-06).
  - A setup still open at week end, or one whose TP was not reached, is MISSED. A setup that was stopped is a loss even if price later reached its TP.
  - E3 % = caught / obvious trades.
- **First-contact fills.** I accepted the tool's "first contact" fills (the order is met at the zone edge moved by the forward spread). Where the filling 15m bar never actually traded the stated entry, I flag it: DXY 07-06 DX5 (0.9 pip short), DX8 (1.6), EUR 07-06 EU1 (1.5), EU2 (1.6), EU1.Tue (2.0), DXY 10-05 DX2 (1.9), DX1.Thu (1.8), EUR 05-18 EU2 (1.6), GBP 10-05 GB1 (2.9).

Measured density, which explains why the E1 ratios are high: zone boxes and parts (sweep reach excluded) cover this share of each week's post-anchor range.

| Map | Share of the week's range covered |
|---|---|
| DXY 07-06 | 99% |
| DXY 04-20 | 88% |
| DXY 10-05 | 68% |
| DXY 05-18 | 84% |
| EUR 07-06 | 89% |
| EUR 04-20 | 89% |
| EUR 10-05 | 54% |
| EUR 05-18 | 65% |
| GBP 07-06 | 88% |
| GBP 04-20 | 82% |
| GBP 10-05 | 99% |
| GBP 05-18 | 61% |

The drawn span is 118-336 pips against week ranges of 57-141 pips. When zones tile the range, nearly every turn is "at a zone" by construction. The reaction ratio is real but cheap, and the side condition is where the maps fail.

---

## 1. DXY 2026-07-06 (anchor week)

**Obvious trades.** These are the operator's trades in the window: #2-#8. His #1 (LONG 100.945, Monday) was a pre-06:00 turn. Price sat at 100.914-100.95 from 02:00 to 05:00 UTC and left at 06:00. Its later touch (Monday 17:00) ran straight through his SL 100.905, so it is outside the window. That leaves 7 obvious trades.

**E1 (week 100.598-101.275)**

| Zone | Verdict | Evidence |
|---|---|---|
| UPPER RESISTANCE 101.199-101.262 (+ band to 101.305) | REACTED | Wed 01:00 101.215, 09:00 101.239, 11:00 101.256, 15:00 101.275 week top, then sell-off |
| EQUILIBRIUM 100.985-101.077 (parts 100.892-101.171) | REACTED | Mon top 101.145, Wed low 100.95, Thu 101.039, Fri 100.991 |
| 1H Mitigated MoM demand 100.825-100.851 (+ sweep to 100.726) | REACTED | Mon 100.838, Tue 100.803, Thu 100.786 |
| MID-RANGE SUPPORT 100.724-100.815 (+ 1H BoM 100.654-100.748) | REACTED | Thu 100.786, Fri 16:00 100.727 |
| GAP IN-FILL 100.599-100.659 | REACTED | Fri 02:00 100.598, flush low, recovered to 100.997 |

- Not reached: 1H BoM supply 101.658-101.746; UR 101.448-101.537; 4H BoM supply 101.316-101.430; KSB 100.470-100.530; KSB 100.248-100.316; band 100.154-100.214; discovery 102.000.
- Turning points with no zone: none.
- **E1 = 5/5 = 100%. Side condition: FAIL.**
  - Bunched:
    - 1H mitigated demand 100.825-100.851 sits 1 pip above MID-RANGE 100.724-100.815.
    - MID-RANGE's part 100.654-100.748 overlaps the GAP IN-FILL part 100.558-100.703.
    - So three supports form one wall from 100.558 to 100.926, crossed together by the Thursday-night / Friday 02:00 drop.
    - The UR 101.199 band (top 101.305) overlaps the 4H supply's sweep part (bottom 101.294).
  - Floating (the week ranged 100.598-101.275):
    - 1H BoM supply 101.658-101.746 plus sweep reach to 101.90: 38-63 pips above the high.
    - KSB 100.248-100.316: 28-35 below the low.
    - Band 100.154-100.214: 38-44 below.
    - Discovery 102.000: 72 above.
  - Bloated: none.

**E2**

| Day | Forecast | His tag | Verdict |
|---|---|---|---|
| Mon | SS | SS+BS | WRONG: his BS is not carried |
| Tue | SS | SS | RIGHT |
| Wed | SS+RWL+BS down | SS+RWL+BS | RIGHT |
| Thu | BS down | ladder short, the breakdown continuing | RIGHT |
| Fri | BS+WL+RWL down | WL+RWL | RIGHT: carries both of his shapes |

The Thursday day box (100.968-101.247) sat mostly above Thursday's candles (100.786-101.071).

**E2 = 4/5 = 80%.**

**E3**

| His trade | Matching setup | Verdict |
|---|---|---|
| #2 S 101.14 | DX2 S 101.138, TP Tue 01:30 | CAUGHT |
| #3 L 100.845 | DX3 L 100.851, filled Mon 18:30, TP Tue 23:45 | CAUGHT |
| #4 S 101.19 | DX5 S 101.203, TP Wed 06:30 | CAUGHT |
| #5 L 100.975 | DX6 L 100.980, TP Wed 09:00 | CAUGHT |
| #6 S 101.235 | DX4 S 101.235, TP Fri 02:00 | CAUGHT |
| #7 S 100.975 | DX7 S 100.980, TP Fri 02:00 | CAUGHT |
| #8 L 100.615 | DX8 L 100.628, TP Fri 14:00 | CAUGHT |

- **E3 = 7/7 = 100%.**
- Stopped: **DX2.Tue** (S 101.138, filled Tue 19:15, stopped Tue 23:45).
- DX3 survived its SL 100.795 by 0.8 pip (Tue low 100.803).
- DX3 and DX3.Tue were both open at once: the same setup filled twice.

**Presentation**
- `_all` frame: DX4 / DX5 labels sit on top of each other.
- The DX6 label is overprinted by a zone label.
- The Thu / Fri day tags are crossed by the option-strike text and the yellow path.
- Zone labels run across the history candles.

## 2. EURUSD 2026-07-06 (anchor week)

**Obvious trades.** His #2-#8. His #1 (SHORT 1.14322, Monday) was only available at 02:00-04:00 UTC. After 06:00, highs stayed at or below 1.14288 until the afternoon rally ran through his SL. So it is outside the window. That leaves 7 obvious trades.

**E1 (week 1.13911-1.14608)**

| Zone | Verdict | Evidence |
|---|---|---|
| 1H Mitigated 4x supply 1.14601-1.14677 | REACTED | Fri 02:00 1.14608 week top, then -49 |
| UR 1.14444-1.14533 (parts to 1.14723) | REACTED | Mon 23:00 1.1448, Thu 06:00 1.14494, Thu 14:00 1.1446 |
| 1H BoM supply 1.14375-1.14421 | REACTED | Tue 12:00 1.14421, Fri 16:00 1.14412 |
| GAP IN-FILL 1.14220-1.14280 (parts 1.14128-1.14405) | REACTED | Tue 1.14234, Wed 07:00 1.14315, Thu 1.14209 |
| Band 1.14108-1.14178 | REACTED | Mon 1.14083, Wed 21:00 1.14141, Fri 1.14114 |
| MID-RANGE 1.13977-1.14053 | REACTED | Wed 01:00 1.13983 |
| KSB 1.13721-1.13801 (sweep part to 1.13926) | REACTED | Wed 15:00 1.13911 week low |

- Turning points with no zone: none.
- **E1 = 7/7 = 100%. Side condition: FAIL.**
  - Bunched:
    - From 1.13977 to 1.14837, seven separate zones overlap one another: MID-RANGE, band, GAP IN-FILL, 1H BoM supply, UR, 1H mitigated 4x, 1H BoM supply 1.14738. The whole week trades inside one striped wall.
    - UR 1.14967-1.15027, GAP IN-FILL 1.15034-1.15094 and 4H supply 1.15130 (part 1.15064) are 0.7 pip apart.
    - The 1H BoM demand 1.13815-1.13886 lies inside the KSB's sweep part 1.13790-1.13926.
  - Floating (the week ranged 1.13911-1.14608):
    - 4H MoM supply 1.15130-1.15264: 52-66 pips above the high.
    - GAP IN-FILL 1.15034-1.15094 and UR 1.14967-1.15027: 36-49 above.
    - KSB 1.13486-1.13546: 37-43 below the low.
    - 1H BoM demand 1.13333-1.13458: 45-58 below.
    - Band 1.13175-1.13245: 67-74 below.
    - Discovery 1.13000: 91 below.

**E2** (mirror of DXY)

| Day | Forecast | Verdict |
|---|---|---|
| Mon | SS | WRONG: his SS+BS, BS missing |
| Tue | SS | RIGHT |
| Wed | SS+RWL+BS up | RIGHT |
| Thu | BS up | RIGHT (ladder long) |
| Fri | BS+WL+RWL up | RIGHT |

The Thursday box 1.13962-1.14248 sat below the Thursday candles (1.14141-1.14494).

**E2 = 4/5 = 80%.**

**E3**

| His trade | Matching setup | Verdict |
|---|---|---|
| #2 L 1.14106 | EU4 L 1.14095, TP Mon 18:45 | CAUGHT |
| #3 S 1.14441 | EU1 / EU1.Tue S 1.14442, TP Tue 21:15 | CAUGHT |
| #4 L 1.14012 | EU7 L 1.14018, TP Wed 07:15 | CAUGHT |
| #5 S 1.14277 | EU5 S 1.14269, TP Wed 11:30 | CAUGHT |
| #6 L 1.13953 | EU6 L 1.13940, TP Fri 02:00 | CAUGHT |
| #7 L 1.14233 | EU8 L 1.14239, TP Fri 02:00 | CAUGHT |
| #8 S 1.14578 | EU9 S 1.14598 (2.0 pips off), TP Fri 12:45 | CAUGHT |

- **E3 = 7/7 = 100%.**
- Stopped: **EU2** (S 1.14385, Mon 17:15 to 21:45) and **EU4.Tue** (L 1.14095, Tue 19:15 to 21:30).

**Presentation**
- `_all` frame: EU3 / EU4 / EU4.Tue / EU7 labels pile up at 1.1400-1.1415 over candles.
- The EU1 label overlaps the "1H (Unmitigated) | BoM + sweep zone" label.
- `_week` frame: the "EU6 BS L 9.1R" text is printed over candles.

## 3. GBPUSD 2026-07-06 (anchor week)

**Obvious trades.** His #1-#7, all in the window. #1 L 1.33331 filled at Monday 06:00-09:00 lows of 1.33286-1.33312.

**E1 (week 1.33222-1.34517)**

| Zone | Verdict | Evidence |
|---|---|---|
| RESISTANCE CEILING 1.34484-1.34548 | REACTED | Fri 02:00 1.34517 week top, then -60 |
| Band 1.34386-1.34476 | REACTED | Fri 11:00 1.34373, 1.3 pip under; crossed by the Fri 02:00 spike |
| 4H BoM supply 1.34264-1.34340 | REACTED | Thu 06:00 1.34308, Thu 07:00 1.34273 |
| 4H MoM supply 1.34035-1.34162 | REACTED | Wed 17:00 1.34104, Thu 14:00 1.34109, Thu 18:00 1.34192, Fri 08:00 low 1.34085 |
| UR 1.33933-1.34005 | REACTED | Mon 1.33971, Tue 01:00 1.34015, Tue 11:00 1.3394 |
| GAP IN-FILL 1.33744-1.33804 | REACTED | Thu 12:00 1.33807, Wed 21:00 1.33799 |
| UR 1.33643-1.33717 | REACTED | Tue 10:00 1.33693, Wed 08:00 1.33702 |
| 1H MoM supply 1.33544-1.33582 | REACTED | Wed 10:00 1.33568 |
| UR 1.33435-1.33521 | REACTED | Wed 01:00 1.33422, Wed 13:00 1.33402 |
| MID-RANGE 1.33225-1.33285 (part 1.33082-1.33333) | REACTED | Mon 07:00 1.33286, Wed 09:00 1.33222 week low |

- Turning points with no zone: none.
- **E1 = 10/10 = 100%. Side condition: FAIL.**
  - Bunched:
    - UR 1.33435-1.33521, 1H MoM supply 1.33544-1.33582 (2.3 pips), UR 1.33643-1.33717 and GAP IN-FILL 1.33744-1.33804 (2.7 pips) stack with overlapping parts from 1.33340 to 1.33946.
    - The band 1.34386-1.34476 sits 0.8 pip under the RESISTANCE CEILING 1.34484; the Fri 02:00 candle crossed both.
    - Sweep zone supply-side 1.32667-1.32767 and sweep zone demand-side 1.32639-1.32739 overlap, with KSB 1.32789 2 pips above.
  - Floating (the week ranged 1.33222-1.34517):
    - Above: sweep zone 1.34733-1.34833 (22-32 pips above the high); band 1.34910-1.35000 (39-48 above).
    - Below, 35-124 pips under the low: KSB 1.32789-1.32877; both sweep zones 1.32639-1.32767; 4H MoM demand 1.32338-1.32568; 4H Mitigated demand 1.31986-1.32280.

**E2** (mirror)

| Day | Forecast | Verdict |
|---|---|---|
| Mon | SS | WRONG: BS missing |
| Tue | SS | RIGHT |
| Wed | SS+RWL+BS up | RIGHT |
| Thu | BS up | RIGHT |
| Fri | BS+WL+RWL up | RIGHT |

The Wednesday box 1.33155-1.33496 and Thursday box 1.33270-1.33825 sat under the day's candles.

**E2 = 4/5 = 80%.**

**E3**

| His trade | Matching setup | Verdict |
|---|---|---|
| #1 L 1.33331 | GB2 L 1.33333, TP Mon 18:45 | CAUGHT |
| #2 S 1.33934 | GB1 S 1.33959 (2.5 pips off), TP Wed 09:00 | CAUGHT |
| #3 L 1.3333 | GB4 L 1.33255, TP Thu 06:15 | CAUGHT, flagged: same zone and turn (Wed low 1.33222), but 7.5 pips from his entry |
| #4 L 1.33629 (reinforcement) | none; all three reinforcements were rejected for RRR | MISSED |
| #5 S 1.34246 | GB6 S 1.34254, TP Thu 11:15 | CAUGHT |
| #6 L 1.33829 | GB7 L 1.33888 never filled (its box starts Fri; the turn was Thu 12:00 at 1.33807) | MISSED |
| #7 S 1.34481 at the RESISTANCE CEILING | no setup | MISSED |

- **E3 = 4/7 = 57%.**
- Stopped: none.
- GB3 was void and GB5 was not filled.

**Presentation**
- `_all` frame: GB2 / GB4 / GB2.Tue / GB3 labels cluster over the 1.3333-1.3345 candles.
- Three "UPPER RESISTANCE" labels lie within 50 pips of each other.
- The Fri tag and the GB7 label are printed over candles.

## 4. DXY 2026-04-20

**Obvious trades** (the brief, S3): his LONG 98.02 / SL 97.87 / TP 98.77 and LONG 98.29 / SL 98.185 / TP 98.77. That is 2 trades.

**E1 (week 98.006-98.939)**

| Zone | Verdict | Evidence |
|---|---|---|
| UR 98.939-99.005 (+ 4H BoM 98.884-99.031) | REACTED | Thu 17:00 98.939, Fri 03:00 98.915, then -43 |
| 1H MoM supply 98.675-98.845 | REACTED | Thu 98.737, 98.714, 98.803, 98.781; Fri support 98.679 |
| Band 98.561-98.625 | REACTED | Tue 98.567 twice, Thu 07:00 low 98.592 |
| UR 98.456-98.541 | REACTED | Tue 20:00 98.549, Thu 14:00 low 98.534 |
| 1H MoM supply 98.402-98.439 | REACTED | Wed 11:00 98.443 |
| Band 98.300-98.364 | REACTED | Tue 20:00 low 98.311, Wed 11:00 98.301 |
| GAP IN-FILL 98.220-98.280 | REACTED | Wed 05:00 98.211, Tue 15:00 98.249 |
| MID-RANGE 98.058-98.145 | REACTED | Mon 13:00 98.083, Mon-Tue base at 98.01-98.10 |
| 1H MoM demand 97.937-98.045 | REACTED | Mon 15:00 98.006 week low |

- Turning points with no zone: none.
- **E1 = 9/9 = 100%. Side condition: FAIL.**
  - Bunched:
    - GAP IN-FILL 98.220-98.280 (parts 98.182-98.361), band 98.300-98.364, 1H MoM supply 98.402-98.439 (part 98.295-98.439) and UR 98.456-98.541 (part 98.364-98.464) overlap from 98.182 to 98.541. The Tue 16:00-17:00 rally crossed them together.
    - MID-RANGE's part 97.969-98.105 overlaps the 1H MoM demand 97.937-98.045.
    - Sweep zone 97.832-97.932 is 0.5 pip from that demand's band part.
  - Floating: KSB 97.466-97.541 (47-54 pips below the low) and sweep zone 97.355-97.455 (55-65 below).

**E2**

| Day | Forecast | Verdict |
|---|---|---|
| Mon | SS, box 97.869-98.539 | RIGHT: staircase 98.395 to 98.006 between ceiling and floor, inside the box |
| Tue | SS+RWL+BS up | RIGHT: base 98.04-98.16, whiplash 98.309/98.123, then surge to 98.567. The path's dip to 97.97 did not happen |
| Wed | BS up | RIGHT: 98.211 to 98.643 close 98.616 |
| Thu | BS+RWL up | RIGHT: to 98.939 |
| Fri | RWL down | RIGHT: 98.915 to 98.489 (the day's high was 11 pips above the box) |

**E2 = 5/5 = 100%.**

**E3**

| His trade | Matching setup | Verdict |
|---|---|---|
| L 98.02 | DX1 L 98.019, filled Mon 15:15, TP 98.874 Thu 17:30 | CAUGHT |
| L 98.29 | DX2 L 98.270, filled Wed 05:15, TP Thu 17:30 | CAUGHT |

- **E3 = 2/2 = 100%.**
- Stopped: **DX3** (L 98.660, filled Thu 00:00, stopped in the same 15m bar).

**Presentation**
- The `_week` frame is not fitted to the week. Its axis runs 97.2-99.6 for a 98.0-98.94 week, stretched by the post-week spike to 99.35 and the zones down to 97.36.
- `_all` frame: "Tue SS+RWL+BS up 33%" is printed across the UR label.
- The Thu and Fri tags overlap candles.

## 5. EURUSD 2026-04-20

**Obvious trades** (listed before reading setups):

| # | Trade | Move | Size |
|---|---|---|---|
| T0 | L Mon | EQ ~1.1755 to 1H MoM supply ~1.1790 | 35 pips |
| T1 | S Tue | 1.1791 to GAP IN-FILL 1.1720 | 70 pips |
| T2 | L Tue-Wed | 1.1719 to 1.1762 | 43 pips |
| T3 | S Wed | 1.1762 to MID-RANGE 1.1692 / 1.1680 | 70-80 pips |
| T4 | L Fri | 1.1673 to 1.1720 | 50 pips |

**E1 (week 1.16691-1.17910)**

| Zone | Verdict | Evidence |
|---|---|---|
| UR 1.17988-1.18067 (1H part 1.17847-1.17988) | REACTED | Mon 23:00 1.1791 week top, then -72 |
| UR 1.17706-1.17791 | REACTED | Mon 1.17718, 1.17755; Tue 1.1777, 1.17759 |
| Sweep zone 1.17592-1.17692 | REACTED | Tue 11:00 1.17684, Wed 05:00 1.17624 |
| EQ 1.17497-1.17573 | REACTED | Mon 1.17536, 1.17558; Tue 1.1754 |
| GAP IN-FILL 1.17347-1.17407 | REACTED | Tue 23:00 1.17372, Wed 03:00 1.17376, Wed 13:00 1.17431 |
| GAP IN-FILL 1.17203-1.17263 | REACTED | Tue 1.17201, 1.17187; Wed 1.17237 |
| MID-RANGE 1.16973-1.17033 | REACTED | Thu 00:00 1.16921, 03:00 1.16948, Fri 1.16986 |
| Band 1.16876-1.16967 | REACTED | Thu 00:00 1.16921 |
| GAP IN-FILL 1.16744-1.16804 | REACTED | Thu 1.16796, 1.16789, 1.16764; Fri 1.16729 |
| KSB 1.16570-1.16638 (parts to 1.16754) | REACTED | Thu 17:00 1.16691 week low |

- Turning points with no zone: none.
- **E1 = 10/10 = 100%. Side condition: FAIL.**
  - Bunched:
    - UR 1.17706, sweep zone 1.17592 and EQ 1.17497 overlap from 1.17497 to 1.17819: three separate zones.
    - The two GAP IN-FILLs and their parts run continuously from 1.17126 to 1.17418.
    - The band 1.16876-1.16967 sits inside MID-RANGE's 4H part.
    - GAP IN-FILL 1.16744-1.16804 overlaps the KSB parts.
  - Floating (the week ranged 1.16691-1.17910):
    - Above: bands 1.18790-1.18881, 1.18978-1.19069 and 1.19175-1.19266 (88-136 pips above the high); RESISTANCE CEILING 1.18446-1.18506 (54-60 above); band 1.18303-1.18394 (39-48 above); discovery 1.19500 (159 above).
    - Below: bands 1.16286-1.16377 and 1.16071-1.16162 (31-62 below the low); 1H MoM demand 1.15907-1.16004 (69-78 below); discovery 1.16271 (42 below).

**E2**

| Day | Forecast | Verdict |
|---|---|---|
| Mon | SS | RIGHT: inside box 1.17004-1.17988 |
| Tue | SS+RWL+BS down | RIGHT: 1.1791 to 1.17187 |
| Wed | BS down | RIGHT: 1.17624 to 1.1703 close 1.17045 |
| Thu | BS+RWL down | RIGHT: to 1.16691 |
| Fri | RWL up | RIGHT: 1.16729 to 1.1723 |

**E2 = 5/5 = 100%.**

**E3**

| Trade | Setup | Verdict |
|---|---|---|
| T0 | no setup (Mon LONG not emitted) | MISSED |
| T1 | EU2 S 1.17920, filled Mon 23:00, TP Tue 15:00 (EU3 same entry, TP Thu 00:00) | CAUGHT |
| T2 | Tue RWL up rejected (RRR 2.46) | MISSED |
| T3 | EU4 S 1.17656 never filled (Wed high 1.17624) | MISSED |
| T4 | Thu RWL up rejected (RRR 2.12); no Fri setup | MISSED |

- **E3 = 1/5 = 20%.**
- Stopped: none.

**Presentation**
- The discovery line 1.19500 and its label sit on the chart header (`_zones`, `_all`).
- `_week` frame: "Mon SS 65%" is hidden under the UR label text.
- The `_week` axis is not fitted: 1.1595-1.1945 for a 1.1669-1.1791 week.

## 6. GBPUSD 2026-04-20

**Obvious trades** (listed before reading setups):

| # | Trade | Move | Size |
|---|---|---|---|
| T1 | L Mon | MID-RANGE 1.3482 (06:00) to UR 1.3544 (15:00) | 62 pips |
| T2 | S Tue | 1.3540 (14:00) to MID-RANGE 1.3474 (19:00) | 65 pips |
| T3 | S Thu | 1.3518 (14:00) to 1H MoM demand 1.3448 (17:00) | 70 pips |
| T4 | L Thu-Fri | 1.3453 (Fri 03:00) to 1.3537 | 84 pips |

**E1 (week 1.34476-1.35444)**

| Zone | Verdict | Evidence |
|---|---|---|
| UR 1.35434-1.35508 | REACTED | Mon 15:00 1.35444 week top, Tue 14:00 1.35396 |
| UR 1.35241-1.35327 | REACTED | Mon 1.35281, Tue 1.35309, Wed 1.35342, 1.35353 |
| GAP IN-FILL 1.35047-1.35107 | REACTED | Mon 1.35056, 1.35067; Thu highs 1.35105, 1.35076 |
| UR 1.34932-1.35019 HEAVY | REACTED | Mon 08:00 1.34929; Wed 1.34993, 1.3492 |
| MID-RANGE 1.34768-1.34846 | REACTED | Mon 06:00 1.34818, Tue 1.34823, 1.34744; Thu 1.34789, 1.34781 |
| 1H MoM demand 1.34345-1.34660 | REACTED | Thu 17:00 1.34476 week low, Fri 1.34532 |

- Turning points with no zone: none.
- **E1 = 6/6 = 100%. Side condition: FAIL.**
  - Bunched:
    - Five separate "UPPER RESISTANCE" zones plus two GAP IN-FILLs, with parts, run continuously from 1.34932 to 1.36090.
    - UR 1.34932 / GAP IN-FILL 1.35047 overlap; GAP part 1.35144 and UR part 1.35163 are 2 pips apart.
    - UR 1.35434 / GAP 1.35521 / UR 1.35719 overlap.
    - MID-RANGE part 1.34691 overlaps the 1H demand part 1.34700.
  - Floating (the week ranged 1.34476-1.35444):
    - Above: bands 1.36196-1.36308 and 1.36483-1.36595 (75-115 pips above the high); RESISTANCE CEILING 1.35940-1.36008 (50-56 above).
    - Below: KSB 1.33998-1.34073 (40-48 below the low); 1H BoM demand 1.33806-1.33960 (52-67 below).
  - Borderline tall: 1H MoM demand 1.34345-1.34660 is 31.5 pips, 38 with its parts.

**E2**

| Day | Forecast | Verdict |
|---|---|---|
| Mon | SS, box 1.34345-1.35019 | WRONG: a 62-pip rally out of the box to 1.35444 (+42 above it), close 1.35333 outside |
| Tue | SS+RWL+BS down | WRONG: a wide range 1.34744-1.35396 with no decisive breakdown; MID-RANGE held and price closed back at 1.35068 |
| Wed | BS down | WRONG: range 1.34901-1.35353, no breakdown |
| Thu | BS+RWL down | RIGHT: broke down through MID-RANGE to 1.34476 |
| Fri | RWL up | RIGHT: +84 |

**E2 = 2/5 = 40%.**

**E3**

| Trade | Setup | Verdict |
|---|---|---|
| T1 | GB1 L 1.34660 never filled | MISSED |
| T2 | no short at 1.354 | MISSED |
| T3 | GB3 / GB5 shorts never filled | MISSED |
| T4 | GB4 L 1.34083 never filled | MISSED |

- **E3 = 0/4 = 0%.**
- Stopped: **GB2** (Tue BS S 1.35163, rested from Mon 07:15, stopped Mon 15:15, before its own tagged day).

**Presentation**
- `_all` frame: "GB2 BS S 4.8R" is overprinted by the UR label.
- `_week` frame: "Mon SS 65%" and "Wed BS down 33%" are under candles; "1.0bn Option Strike Target" is under candles.
- The yellow path drops to 1.3407 on Thursday, 43 pips below the real low.

## 7. DXY 2026-10-05

**Obvious trades** (listed before reading setups):

| # | Trade | Move |
|---|---|---|
| D1 | S Mon | 102.43 to 102.08 |
| D2 | S Tue | 102.28 to KSB 101.75 |
| D3 | L Tue-Wed | 101.76 to 102.50 |
| D4 | S Wed-Thu | 102.50 to 102.13 |
| D5 | L Thu | 102.13 to 102.47 |
| D6 | S Thu | 102.47 to 102.03 |
| D7 | L Fri | 101.92 to 102.33 |

The week's 102.535 high was at Monday 04:00, before the anchor.

**E1 (post-anchor 101.754-102.499)**

| Zone | Verdict | Evidence |
|---|---|---|
| Sweep zone 102.435-102.535 | REACTED | Mon 06:00 102.433, Wed 12:00 102.499, Thu 11:00 102.467 |
| Sweep zone 102.107-102.207 (reach to 102.307) | REACTED | Tue 06:00 102.285, Thu 02:00 102.133, Thu 18:00 102.202 |
| MID-RANGE 101.961-102.051 | REACTED | Tue 01:00 102.044, Thu 102.033 / 102.035 |
| 1H MoM demand 101.855-101.926 | REACTED | Fri 05:00 101.92; Tue 12:00-21:00 base around it |
| KSB 101.750-101.843 | REACTED | Tue 12:00 101.754 week low |

- **Turning point with no zone:** the 102.365-102.374 level. Mon 13:00 102.372 and 14:00 102.365 formed a double top (-24 pips); Wed 15:00 102.374 was a lower high. It lies in the empty gap between the 102.307 sweep reach and the 102.435 box.
- **E1 = 5/(5+1) = 83%. Side condition: FAIL.**
  - Bunched:
    - MID-RANGE 101.961-102.051, 1H MoM demand 101.855-101.926 (with parts overlapping) and KSB 101.750-101.843 (1.2 pips below) are stacked. The Tue 11:00 candle (102.029 to 101.776) crossed all three: the L-28 "three supports bunched and pierced" pattern exactly.
    - MID-RANGE's part 102.032-102.132 overlaps the separate sweep zone 102.107-102.207.
  - Floating (the week ranged 101.754-102.535):
    - 1H MoM demand 101.374-101.405 (35-38 pips below the low).
    - KSB 101.231-101.308 (45-52 below).
    - KSB 100.980-101.056 (70-77 below).
    - Discovery 103.000 (47 above).

**E2**

| Day | Forecast | Verdict |
|---|---|---|
| Mon-Fri | SS, box 101.755-102.635 | RIGHT on all five: every day inside the box (the Tue low 101.754 is 0.1 pip under it) |

**E2 = 5/5 = 100%.** The box is the whole week range: correct, but it says only "range".

**E3**

| Trade | Setup | Verdict |
|---|---|---|
| D1 | DX1 S 102.435, filled Mon 06:30, TP 101.941 Tue 11:15 | CAUGHT |
| D2 | no setup at the Tue 102.285 turn | MISSED |
| D3 | DX2 L 101.926, filled Tue 11:00, TP 102.420 Wed 12:00 (SL 101.725 survived by 2.9 pips) | CAUGHT |
| D4 | DX1.Wed S, TP Fri 05:30 | CAUGHT |
| D5 | no long at 102.13 | MISSED |
| D6 | DX1.Thu S 102.435 (fill credited 1.8 pips short), TP Fri 05:30 | CAUGHT |
| D7 | DX2.Fri L 101.926 filled Fri 05:30, open at week end, TP not reached | MISSED |

- **E3 = 4/7 = 57%.**
- Stopped: none.

**Presentation**
- `_all` frame: the day-wide setup boxes cover the whole week area.
- "DX1.Thu" and "DX2.Fri" are printed over candles.
- The `_week` axis is not fitted: it runs to 101.25 for a 101.75-102.54 week.

## 8. EURUSD 2026-10-05

**Obvious trades** (listed before reading setups):

| # | Trade | Move |
|---|---|---|
| T1 | L Mon | 1.1169 to 1.1221 |
| T2 | L Tue | 1.1203 to 1.1277 |
| T3 | S Tue-Wed | 1.1277 to 1.1165 |
| T4 | L Wed | 1.1165 to 1.1204 |
| T5 | L Thu | 1.1172 to 1.1227, then 1.1243 |
| T6 | S Fri | 1.1243 to 1.1187 |

**E1 (post-anchor 1.11645-1.12767)**

| Zone | Verdict | Evidence |
|---|---|---|
| 1H BoM supply 1.12716-1.12853 | REACTED | Tue 11:00 1.12717, 12:00 1.12767 week top, then -110 |
| GAP IN-FILL 1.12611-1.12671 | REACTED | Tue 15:00 1.12693, Wed 1.12629 lower highs |
| UR 1.12451-1.12530 | REACTED | Tue 08:00 1.12468, lows 1.12411 / 1.12447, Fri 05:00 1.12427 |
| Discovery 1.12364 | PIERCED | crossed Tue 08:00 with no reaction; Fri traded through it to 1.12427 |
| Sweep zone 1.12208-1.12308 | REACTED | Mon 1.12207, Tue 01:00 1.1231, Tue 08:00 low 1.1226, Thu 14:00 1.12267 |
| Sweep zone 1.12149-1.12249 | REACTED | Mon highs, Thu 17:00 1.12197, Fri 12:00 1.1212 |
| Discovery 1.12000 | REACTED | Tue 06:00 1.12028; Wed 1.12037 twice; Thu 1.12004 / 1.12001; Fri 1.12044 |
| Sweep zone 1.11610-1.11710 | REACTED | Mon 06:00 1.1169, Wed 12:00 1.11645 week low, Thu 1.11719 |

- **Turning point with no zone:** the 1.1180-1.1187 support. It was touched Mon 1.11871 / 1.11863, Wed 1.11815 / 1.11792 / 1.11843, Thu 1.1182 / 1.11799 / 1.11845 and Fri 1.11874. It sits in the empty 29-pip gap between 1.11710 and 1.12000.
- **E1 = 7/(8+1) = 78%. Side condition: FAIL.**
  - Bunched:
    - Two separate demand-side sweep zones, 1.12149-1.12249 and 1.12208-1.12308, overlap. With the band part 1.12039-1.12149 and the two discovery lines 1.12000 / 1.12364, five E1 objects sit inside 36 pips.
    - UR 1.12451-1.12530 (parts to 1.12612), GAP IN-FILL 1.12611-1.12671 (touching) and 1H BoM supply 1.12716 are three resistances in 40 pips, crossed together by the Tue 11:00-12:00 candles.
  - Floating (the week ranged 1.11645-1.12767):
    - Seven zones 1.12942-1.13911, 18-114 pips above the high: UR 1.12942-1.13002, UR 1.13185-1.13253, sweep zone 1.13267-1.13367, 1H MoM supply 1.13373-1.13407, UR 1.13439-1.13532, band 1.13590-1.13700, UR 1.13708-1.13773, band 1.13801-1.13911.
    - Discovery 1.11000, 64 pips below.

**E2**

| Day | Forecast | Verdict |
|---|---|---|
| Mon | SS, box 1.11510-1.12712 | RIGHT |
| Tue | SS | RIGHT: high 1.12767 is 5.5 pips over the box, close 1.12583 inside |
| Wed | SS | RIGHT |
| Thu | SS | RIGHT |
| Fri | SS | RIGHT |

**E2 = 5/5 = 100%.** Again the box is the week range.

**E3**

| Trade | Setup | Verdict |
|---|---|---|
| T1 | EU1 L 1.11710, filled Mon 06:30, TP 1.12476 Tue 09:45 | CAUGHT |
| T2 | no long at the Tue 1.1203 turn | MISSED |
| T3 | EU2.Wed S 1.12585, filled Tue 21:00, TP Wed 12:15 | CAUGHT |
| T4 | EU1.Wed filled Wed 12:15, open at week end | MISSED |
| T5 | EU1.Thu filled Thu 11:30, open at week end; TP 1.12476 missed by 5 pips | MISSED |
| T6 | EU2.Fri never filled | MISSED |

- **E3 = 2/6 = 33%.**
- Stopped: **EU2** (S 1.12585, Tue 11:15 to 12:00).

**Presentation**
- `_week` frame: the chart header covers "2.9bn Option Strike Target" and a sweep-zone label.
- About 40% of the `_week` frame is empty zones above the week (axis to 1.137).
- "Mon SS 80%" is overprinted by the 1H BoM label.

## 9. GBPUSD 2026-10-05

**Obvious trades** (listed before reading setups):

| # | Trade | Move |
|---|---|---|
| G0 | S Mon | 1.3239 to 1.3190 |
| G1 | L Tue | 1.3201 to 1.3283 |
| G2 | S Tue-Wed | 1.3285 to 1.3194 |
| G3 | L Thu | 1.3184 to 1.3249 |
| G4 | S Thu | 1.3249 to 1.3204 |
| G5 | S Fri | 1.3250 to 1.3206 |

**E1 (post-anchor 1.31843-1.32856)**

| Zone | Verdict | Evidence |
|---|---|---|
| 1H BoM supply 1.32731-1.32942 | REACTED | Tue 1.32817, 1.32833, 1.32856 week top |
| 4H BoM supply 1.32610-1.32717 | REACTED | Tue 14:00 low 1.32611, Tue 22:00 1.32761, then the sell-off |
| UR 1.32457-1.32535 | REACTED | Tue 11:00 low 1.32437; Wed 07:00 1.32545; Thu 14:00 1.32485; Fri 1.32503 / 1.32471 |
| 1H BoM supply 1.32319-1.32395 | REACTED | Mon 09:00 1.3239, Tue 01:00 1.32318, Fri 06:00 low 1.32313 |
| GAP IN-FILL 1.32124-1.32184 | REACTED | Mon 1.32159; Wed 1.32195 / 1.32242; Thu 1.32222 / 1.32167 |
| MID-RANGE 1.31991-1.32051 | REACTED | Mon 1.32045, Tue 06:00 1.32013, Wed 1.32034 / 1.31987, Thu 1.3206, Fri 1.32057 |
| Sweep zone 1.31806-1.31914 | REACTED | Mon 13:00 1.319, Thu 07:00 1.31874, Thu 10:00 1.31843 week low |

- Turning points with no zone: none. Zones cover 99% of the range, so none was possible.
- **E1 = 7/7 = 100%. Side condition: FAIL.**
  - Bunched: seven separate zones form one continuous wall from 1.31806 to 1.32988, with overlaps at:
    - 1.31899 (sweep zone / MID-RANGE part);
    - 1.32121 (MID-RANGE part / GAP band);
    - 1.32183-1.32231 (GAP part / 1H BoM sweep part);
    - 1.32395-1.32400 (1H BoM / UR part);
    - 1.32610-1.32636 (UR band / 4H BoM).
  - The Tue 08:00-11:00 rally crossed 1H BoM supply, UR and into 4H BoM together.
  - Floating: zones none; discovery lines 1.31500 (34 pips below the low) and 1.31000 (84 below).

**E2**

| Day | Forecast | Verdict |
|---|---|---|
| Mon | SS, box 1.31799-1.32395 | RIGHT: exact range 1.319-1.3239 |
| Tue | SS | WRONG: broke the ceiling decisively (the tool's own E3 report: "closed through on 1H Tue 08:00") and surged to 1.32856, 46 pips over the box |
| Wed | SS | WRONG: from 1.32761 (+37 over the box) down to 1.31935 |
| Thu | SS | RIGHT: floor held at 1.31843, high 1.32485 (+9), close inside |
| Fri | SS | WRONG: ranged 1.32057-1.32503, upper half above the box (+10.8 pips over the 10-pip limit), on a ceiling the tool had itself voided on Tuesday |

**E2 = 2/5 = 40%.**

**E3**

| Trade | Setup | Verdict |
|---|---|---|
| G0 | GB1 S 1.32329 (fill credited at 07:45, bar high 1.323, 2.9 pips short of entry), TP Mon 13:15 | CAUGHT |
| G1 | GB2.Tue never filled | MISSED |
| G2 | GB1.Wed void | MISSED |
| G3 | GB2.Thu L 1.31899, TP Thu 14:15 | CAUGHT |
| G4 | GB1.Thu void | MISSED |
| G5 | GB1.Fri void | MISSED |

- **E3 = 2/6 = 33%.**
- Stopped: none.

**Presentation**
- The void GB1.Wed, GB1.Thu and GB1.Fri are still drawn with labels.
- `_week` frame: the Tuesday candles run 46 pips out of the drawn day box.
- The Mon / Tue / Fri tags are partly under candles.

## 10. DXY 2026-05-18

**Obvious trades** (listed before reading setups):

| # | Trade | Move |
|---|---|---|
| X1 | S Mon | 99.307 to 98.98 / 98.944 |
| X2 | L Mon-Tue | 98.944 to 99.434 |
| X3 | S Wed | 99.472 to 98.966 (one hour) |
| X4 | L Wed-Thu | 98.97 / 99.055 to 99.356 / 99.515 |
| X5 | S Thu | 99.515 to 99.092 |
| X6 | L Thu-Fri | 99.092 to 99.41 |

**E1 (week 98.944-99.515)**

| Zone | Verdict | Evidence |
|---|---|---|
| Band 99.449-99.503 | REACTED | Wed 99.471 / 99.472 (then -50), Thu 13:00 99.515 then -42 |
| Sweep zone 99.309-99.409 (reach 99.509) | REACTED | Tue 99.434 / 99.422, Fri 99.412 |
| 1H MoM demand 99.251-99.298 | REACTED | Tue 14:00 99.263, Wed 04:00 99.285, Wed 11:00 99.294 |
| 1H MoM demand 99.174-99.244 | REACTED | Mon 06:00 99.17, Tue 12:00 99.177, Thu 99.204, Fri 99.172 / 99.186 |
| MID-RANGE 98.963-99.037 | REACTED | Mon 98.98 / 98.971, Wed 15:00 98.966, Wed-Thu 99.053-99.092 |
| 1H MoM demand 98.844-98.889 (sweep part to 98.944) | REACTED | Mon 22:00 98.944 week low, then +49 |

- Turning points with no zone: none.
- **E1 = 6/6 = 100%. Side condition: FAIL.**
  - Bunched, twice in the L-28 pattern:
    - 1H MoM demand 99.174-99.244 / 1H MoM demand 99.251-99.298 (0.7 pip apart, parts overlapping) / sweep zone 99.309-99.409 (1.1 pip above): three zones in 23 pips.
    - 1H MoM demand 98.844-98.889 / 1H MoM demand 98.808-98.843 (0.1 pip apart) / KSB 98.732-98.792 (1.6 pips): three supports in 16 pips.
  - Floating (the week ranged 98.944-99.515): band 99.956-100.010 (44-50 pips above the high); band 98.613-98.667 (28-33 below the low); KSB 98.460-98.546 (40-48 below, parts to 98.360).

**E2**

| Day | Forecast | Verdict |
|---|---|---|
| Mon-Fri | SS, box 98.963-99.509 | RIGHT on all five: every day inside within 2 pips |

**E2 = 5/5 = 100%.** The box is the week range.

**E3**

| Trade | Setup | Verdict |
|---|---|---|
| X1 | no short | MISSED |
| X2 | DX1 was stopped and its repeats void | MISSED |
| X3 | no short | MISSED |
| X4 | no long | MISSED |
| X5 | no short | MISSED |
| X6 | no long | MISSED |

- **E3 = 0/6 = 0%.**
- Stopped: **DX1** (L 99.050, filled Mon 11:30, stopped Mon 16:15 at exactly its SL 98.971). Price then rallied 49 pips.
- DX1.Tue through DX1.Fri were all void. The tool had four rejected candidates and no other setup all week.

**Presentation**
- The void DX1.Tue / Wed / Thu / Fri are still drawn with labels.
- `_week` frame: "DX1 SS L 3.1R" is under candles.
- The zone labels in the history half run across candles.

## 11. EURUSD 2026-05-18

**Obvious trades** (listed before reading setups):

| # | Trade | Move |
|---|---|---|
| U1 | L Mon | 1.1622 to 1.1657 / 1.1662 |
| U2 | S Tue | 1.1662 to 1.1592 |
| U3 | L Wed | 1.1583 to 1.1645 (one hour) |
| U4 | S Thu | 1.1635 to 1.1576 |
| U5 | L Thu | 1.1576 to 1.1630 |

**E1 (week 1.15762-1.16617)**

| Zone | Verdict | Evidence |
|---|---|---|
| UR 1.16641-1.16726 (band part from 1.16604) | REACTED | Mon 22:00 1.16617 week top, then -70 |
| UR 1.16493-1.16562 | REACTED | Mon 1.16572, 1.1656, 1.16562, 1.1656; Tue 1.16458 |
| Discovery 1.16409 | REACTED | Mon 12:00 low exactly 1.16409; Wed spike top 1.16448 |
| Band 1.16327-1.16395 | REACTED | Mon 1.16333, Tue 1.16335, Wed-Thu highs 1.16352-1.16359 |
| EQ 1.16219-1.16296 | REACTED | Mon 06:00 1.16219, Mon 1.16264 / 1.16287, Tue 1.16222 |
| Sweep zone 1.16083-1.16183 | REACTED | Tue 1.1611, Wed 1.16129 / 1.16158, Thu 1.16159, Fri 1.16183 / 1.1619 |
| MID-RANGE 1.15970-1.16036 | REACTED | Wed highs 1.16055-1.16066, Thu 1.1596, Fri 1.15982 |
| Band 1.15747-1.15815 | REACTED | Wed 1.15836 / 1.15827, Thu 13:00 1.15762 week low |

- Turning points with no zone: none. The 1.1592 lows of Tue / Wed are within 5 pips of MID-RANGE.
- **E1 = 8/8 = 100%. Side condition: FAIL.**
  - Bunched:
    - EQ 1.16219-1.16296 (parts 1.16161-1.16356), sweep zone 1.16083-1.16183 and band 1.16327-1.16395 overlap; MID-RANGE 1.15970 is 4.7 pips below. The Tue 10:00-14:00 drop crossed them together.
    - UR 1.16641 (parts 1.16604-1.16826) overlaps 1H MoM supply 1.16738-1.16785.
    - UR 1.16493 is 3 pips under 1.16604.
  - Floating (the week ranged 1.15762-1.16617):
    - Above: 4H MoM supply 1.17047-1.17214 (43-60 pips above the high); UR 1.16939-1.17026 (32-41 above); band 1.16853-1.16921 (24-30 above).
    - Below: a ladder of five bands 1.15126-1.15571 (19-64 pips below the low); discoveries 1.15500 and 1.15072.

**E2**

| Day | Forecast | Verdict |
|---|---|---|
| Mon-Fri | SS, box 1.15747-1.16672 | RIGHT on all five: every day inside |

**E2 = 5/5 = 100%.**

**E3**

| Trade | Setup | Verdict |
|---|---|---|
| U1 | no long | MISSED |
| U2 | EU1 S 1.16604, filled Mon 20:15, TP 1.15985 Tue 14:15 | CAUGHT |
| U3 | EU3.Wed L 1.15815 not filled (low 1.15827) | MISSED |
| U4 | no short | MISSED |
| U5 | EU3.Thu L 1.15815, filled Thu 13:30, TP Thu 17:45 | CAUGHT |

- **E3 = 2/5 = 40%.**
- Stopped: **EU2** (S 1.16297, Mon 06:00 to 07:15). Its repeats were void.

**Presentation**
- "EU1.Thu" sits on top of "1.5bn Option Strike Target".
- Two option labels at 1.1645 overprint each other ("1.5bn" over another strike).
- "EU1 SS S 6.3R" is under candles.
- The void EU2.Tue / Wed / Thu are still drawn.

## 12. GBPUSD 2026-05-18

**Obvious trades** (listed before reading setups):

| # | Trade | Move |
|---|---|---|
| B1 | L Mon | GAP 1.3322 to 1.3449 |
| B2 | S Mon | 1.3449 to 1.3400 |
| B3 | L Wed | 1.3383 to 1.3463 (one hour) |
| B4 | S Thu | 1.3455 to 1.3390 |
| B5 | L Thu | 1.3390 to 1.3449 |
| B6 | L Fri | 1.3413 to 1.3463 |

**E1 (post-anchor 1.33217-1.34631)**

| Zone | Verdict | Evidence |
|---|---|---|
| GAP IN-FILL 1.34628-1.34688 | REACTED | Wed 15:00 1.3463, Fri 13:00 1.34631 (spike tops) |
| UR 1.34497-1.34557 | REACTED | Mon 1.34494; Wed 1.3454, 1.34509; Thu 1.34548, 1.34492; Fri 1.34535 |
| Discovery 1.34369 | REACTED | Mon 1.34391 / 1.34371, Thu 1.34398, Fri 1.34383 / 1.3437 |
| GAP IN-FILL 1.34239-1.34299 | REACTED | Thu 00:00 1.34282, Wed 18:00 1.34315 |
| UR 1.33950-1.34037 | REACTED | Mon 1.34029 / 1.34016, then the Tue-Wed range around it; Thu 13:00 1.33904 |
| Band 1.33816-1.33933 | REACTED | Mon 1.33812; Tue 1.33871 / 1.3386 / 1.33879; Wed 1.33874 / 1.33812 / 1.33831 |
| GAP IN-FILL 1.33720-1.33780 | REACTED | Mon 09:00 1.33778; Tue-Wed floor 1.3375-1.33785 |
| Discovery 1.33654 | PIERCED | crossed Mon 08:00 and 10:00 with no reaction |
| GAP IN-FILL 1.33492-1.33552 | REACTED | Mon 08:00 1.33501, 10:00 1.33465 |
| GAP IN-FILL 1.33240-1.33300 | REACTED | Mon 06:00 1.33217, start of the +127 rally |

- Turning points with no zone: none. The Thu-Fri floor at 1.3412-1.3420 is 2-10 pips under the GAP IN-FILL 1.34239 band part, counted as "around" it.
- **E1 = 10/11 = 91%. Side condition: FAIL.**
  - Bunched:
    - GAP IN-FILL 1.33720-1.33780, band 1.33816-1.33933 (3.6 pips) and UR 1.33950-1.34037 (0.4 pip): three in 33 pips, crossed together by the Mon 14:00-16:00 rally.
    - GAP IN-FILL 1.33240 (parts 1.33147-1.33381), MID-RANGE 1.32995 (parts to 1.33142, 0.5 pip) and band 1.32856-1.32973 (2.2 pips).
    - Six separate "GAP IN-FILL" zones are drawn as a ladder every 20-30 pips.
  - Floating (the week's absolute low was 1.33022, pre-anchor):
    - KSB 1.32484-1.32544 (48-54 pips below).
    - Bands 1.32208-1.32325 and 1.32011-1.32128 (70-101 below).
    - GAP IN-FILL 1.32668-1.32728 (29-35 below).
    - Discovery 1.32000 (102 below).

**E2** (forecast SS on all five days, box 1.33047-1.34137)

| Day | Verdict |
|---|---|
| Mon | WRONG: broke out to 1.34494 (+36; the tool's own report says "closed through Mon 15:00"), close 1.34322 outside |
| Tue | WRONG: high 1.34371 is 23 pips over the box |
| Wed | WRONG: an 80-pip spike to 1.3463, close 1.34331 outside |
| Thu | WRONG: traded 1.33904-1.34548, close 1.34308 outside |
| Fri | WRONG: the whole day 1.34132-1.34631 was above the box |

**E2 = 0/5 = 0%.**

**E3**

| Trade | Setup | Verdict |
|---|---|---|
| B1 | GB2 L 1.33247, filled Mon 06:00, TP 1.33926 Mon 12:30 | CAUGHT |
| B2 | no short at 1.3449 | MISSED |
| B3 | GB2.Wed never filled | MISSED |
| B4 | GB1.Thu void | MISSED |
| B5 | no long | MISSED |
| B6 | no long | MISSED |

- **E3 = 1/6 = 17%.**
- Stopped: **GB1** (S 1.33983, Mon 12:30 to 15:45). Its four repeats were void.

**Presentation**
- `_week` frame: from Wednesday on, the candles sit entirely above the drawn day boxes.
- The Mon / Thu / Fri tags are under candles.
- The void GB1.Tue through GB1.Fri are still drawn with labels.

---

## Table of the 12 maps

| Map | E1 % | E1 side condition | E2 % | E3 % | Stopped setups |
|---|---|---|---|---|---|
| DXY 2026-07-06 | 100 (5/5) | FAIL (bunched, floating) | 80 (4/5) | 100 (7/7) | DX2.Tue |
| EURUSD 2026-07-06 | 100 (7/7) | FAIL (bunched, floating) | 80 (4/5) | 100 (7/7) | EU2, EU4.Tue |
| GBPUSD 2026-07-06 | 100 (10/10) | FAIL (bunched, floating) | 80 (4/5) | 57 (4/7) | none |
| DXY 2026-04-20 | 100 (9/9) | FAIL (bunched, floating) | 100 (5/5) | 100 (2/2) | DX3 |
| EURUSD 2026-04-20 | 100 (10/10) | FAIL (bunched, floating) | 100 (5/5) | 20 (1/5) | none |
| GBPUSD 2026-04-20 | 100 (6/6) | FAIL (bunched, floating) | 40 (2/5) | 0 (0/4) | GB2 |
| DXY 2026-10-05 | 83 (5/6) | FAIL (bunched, floating) | 100 (5/5) | 57 (4/7) | none |
| EURUSD 2026-10-05 | 78 (7/9) | FAIL (bunched, floating) | 100 (5/5) | 33 (2/6) | EU2 |
| GBPUSD 2026-10-05 | 100 (7/7) | FAIL (bunched) | 40 (2/5) | 33 (2/6) | none |
| DXY 2026-05-18 | 100 (6/6) | FAIL (bunched, floating) | 100 (5/5) | 0 (0/6) | DX1 |
| EURUSD 2026-05-18 | 100 (8/8) | FAIL (bunched, floating) | 100 (5/5) | 40 (2/5) | EU2 |
| GBPUSD 2026-05-18 | 91 (10/11) | FAIL (bunched, floating) | 0 (0/5) | 17 (1/6) | GB1 |
| **All 12, pooled** | **95.7 (90/94)** | **0 / 12 PASS** | **76.7 (46/60)** | **47.1 (32/68)** | 9 stopped |
| All 12, mean of maps | 96.0 | | 76.7 | 46.5 | |
| **9 maps outside 2026-07-06, pooled** | **94.4 (68/72)** | **0 / 9 PASS** | **75.6 (34/45)** | **29.8 (14/47)** | 6 stopped |
| 9 maps outside 2026-07-06, mean of maps | 94.7 | | 75.6 | 33.4 | |

By the rule's wording ("E1 = ... AND none bloated, bunched, floating or missing"), no map meets E1, because the side condition fails on 12 of 12. The reaction ratio alone is 95.7%, but the zones cover 54-99% of each week's range.

## The five defects that cost the most

1. **Separate zones bunched into walls (side condition fails 12/12; E1 reactions become automatic).** Examples:
   - DXY 05-18: 98.732-98.889 holds three supports within 1.6 pips (98.732-98.792 / 98.808-98.843 / 98.844-98.889), and 99.174-99.409 holds three more.
   - DXY 10-05: MID-RANGE 101.961 / 1H demand 101.855 / KSB 101.750, all crossed by the Tue 11:00 candle.
   - GBP 10-05: seven zones tile 1.31806-1.32988 (99% of the week's range).
   - EUR 07-06: seven overlapping zones from 1.13977 to 1.14837.
2. **Floating zones (12/12 maps).** The drawn span is 118-336 pips against week ranges of 57-141 pips. Examples:
   - EUR 04-20: bands 1.18790-1.19266, 88-136 pips above the week high.
   - EUR 10-05: seven zones 1.12942-1.13911, up to 114 pips above.
   - GBP 07-06: 4H Mitigated demand 1.31986-1.32280, 94-124 pips below.
   - EUR 05-18: a ladder of five bands 1.15126-1.15571 below the week.
3. **E3 offers almost nothing beyond one pair of SS anchor orders repeated day after day.** Once the anchor zone is closed through, the repeats go void and nothing replaces them. Turn setups are rejected for RRR.
   - Result: 14/47 obvious trades caught outside the anchor week.
   - DXY 05-18: 0/6; the only setup, DX1 L 99.050, was stopped Mon 16:15 and voided all week.
   - GBP 04-20: 0/4.
   - GBP 05-18: 1/6.
   - EUR 04-20: Tue RWL up (1.17497) and Thu RWL up (1.17006) were rejected while +43 and +50 pip moves followed.
4. **E2 range forecasts on GBP while GBP broke out.** The DXY "range" chain was translated to the pair, ignoring the pair's own breakout. 11 of the 14 wrong days are GBP.
   - GBP 05-18: 0/5; box 1.33047-1.34137 while Mon broke to 1.34494 and Wed-Fri traded entirely above the box.
   - GBP 10-05: Tue/Wed went to 1.32856 against a box ceiling of 1.32395 that the tool's own E3 report voided Tue 08:00.
   - GBP 04-20: Mon SS while price ran +42 above the box.
5. **Nine stopped setups, some caused by timing or edge placement.** All nine are named in the table. Examples:
   - GBP 04-20 GB2 (a Tue BS short filled Mon 07:15, stopped Mon 15:15, before its own day).
   - DXY 05-18 DX1 (stopped at exactly 98.971, then +49).
   - DXY 04-20 DX3 (stopped in its fill bar Thu 00:00).
   - EUR 10-05 EU2 (stopped Tue 12:00 by the 1.12767 top).
   - EUR 05-18 EU2 (stopped within 75 minutes Mon 07:15).

   Related scoring caveat: first-contact fills are credited up to 2.9 pips before the entry price traded (GBP 10-05 GB1, bar high 1.323 against entry 1.32329).

Presentation defects across maps, not scored:
- The `_week` frames are not fitted to the week. DXY 04-20 runs 97.2-99.6 for a 98.0-98.94 week; about 40% of the EUR 10-05 frame is empty zones.
- Day tags are hidden under candles or zone labels (GBP 04-20 Mon / Wed, EUR 04-20 Mon, GBP 05-18 Mon / Thu / Fri).
- Setup labels pile on each other (DXY 07-06 DX4 / DX5, EUR 07-06 EU3 / EU4 / EU4.Tue / EU7, GBP 07-06 GB2 / GB4 / GB2.Tue / GB3).
- Void setups are still drawn with labels (GBP 10-05, DXY 05-18, GBP 05-18, EUR 05-18).
- The EUR 04-20 discovery line 1.19500 is printed into the chart header.
