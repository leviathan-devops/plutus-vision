# >>> UPDATE 2026-11-26 (read this block first) <<<
- Scope is the FULL indicator again (memory/14_GOAL_PROMPT.md). E1 zones are now worked on 1H candles with the 4H scan as overview (L-40). E2 = e1_tool/e2_shapes.py, E3 = e1_tool/e3_setups.py, all drawn by e1_tool/e1_pine.py (toggles show_e2 / show_e3).
- Anchor week DXY Apr 20-24: all three engines PASS on the chart (evidence/e1tool_DXY_1H_2026-04-20_e23.png, ledger row 50). EURUSD same week: short 1.1786 -> 1.1714 hit, Friday long +3.1R open.
- HONEST OVERALL STATE: across 40 weeks x 3 pairs the zones show no measurable edge beyond chance on first touch, E3 is break-even (about 1 TP per 3 SL at RRR >= 3), E2 day forecasts match about 29% of days, week direction is a coin flip. Aug 17 DXY is a pixel FAIL. See memory/05_JOURNAL.md entries of 2026-11-26.
- The sections below describe the E1-only tool as of 2026-11-25 (4H-candle zones); zone rules there are superseded where the 2026-11-26 journal says so.

# 13 — E1 TOOL STATUS / MORNING REPORT (written 2026-11-25 night, container clock ~22:10 UTC). Read after 10, 11, 12.

## What exists (all in e1_tool/, pushed to branch AGENT)
- `e1_tool/e1 MONDAY PAIR` -> `out/E1_PAIR_MONDAY.pine` (the tool's output: Pine script with that week's map as data, trident_v8 form) + `out/E1_REPORT_PAIR_MONDAY.txt` (audit trail of every step).
- Modules, in prompt order: e1_data.py (TV bar store, temporal boundary = Fri 17:00 NY) · e1_pillars.py (P1 pivots, P2 MA grid, P6 fibs/rounds, P3/P8 K + strike conversion + tiers, P5 Step 0 swings, 0.45 sweep zones, 0.5 magnets, 0f 4H candles, BoM/MoM, mitigation)
  · e1_synth.py (collect all levels; 6-dimension score + structural-extreme bonus; degree table; ZFP ranges)  · e1_zones.py (zone assembly, POI tier, names, Step 9.5 gap scan) · e1_pine.py (generator) · e1_report.py (audit) · e1_outcome.py (facts of what candles did).
- Render in Pinebox: `tools/e1render PAIR MONDAY` -> evidence/e1tool_PAIR_1H_MONDAY.png. Inputs: sidecar/out/<monday>.json (investingLive expiries as-of, Fed H.10 rates) + TV bars. No price literal in the Python.
- Pine form: IP zones red / orange / teal with "Name | DEGREE | ZFP range | Tier"; inside each zone the 4H candle (A) as a dashed white box from its origin bar labelled BoM/MoM + mitigation count, each computed level (B) as a dotted line coloured by pillar
  (blue pivots, purple MAs, white structure, grey fib/round); LSZ green boxes; option strike targets amber lines; gap in-fill levels as thin dashed boxes. Toggles for each layer.

## Reference week (DXY Apr 20-24 2026) — tool vs report
| Role | Tool (TV candles) | Report (yfinance candles) | Same structure? |
| Resistance Ceiling | 99.13-99.18 (repeated swing high sweep) | 99.16-99.23 | yes; tool has no wall inside because K from H.10 (108.155) puts the 1.1600 strike at 99.29, report K 108.0806 -> 99.22 |
| Upper Resistance | 98.82-99.08 (supply candles 04-09 11:00, 04-10 03:00, 04-13 09:00) | 98.77-98.99 | yes (04-13 supply candle; TV wicks 98.884-99.038) |
| Equilibrium | 98.17-98.44 (supply 04-17 03:00 + MoM supply 04-13 23:00 + repeated-high sweep 98.24-98.29) | 98.29-98.41 | yes, wider: includes the 04-17 supply candle the report did not list |
| Mid-Range Support | 97.81-98.12 (BoM demand 04-16 03:00) | 98.00-98.12 | yes (report listed the candle as 97.93-98.11) |
| Key Support Band | 97.63-97.68 (sweep low 04-17) | 97.63-97.97 | partly: the report's "developing" demand 97.63-97.94 is not produced (no completed move by the boundary) |
Candles that week (frame opened): Monday low inside Mid-Range Support then +82 pips; Tue-Wed 44h inside Equilibrium; Thursday high 98.93 inside Upper Resistance then reversal; Ceiling and Key Support not reached. Same behaviour as the original render.

## Other weeks and pairs — HONEST: not at the reference's level everywhere
Frames opened (evidence/e1tool_*): DXY 03-09, 05-18, 06-08, 07-27, 08-17, 10-05 · EURUSD 04-20, 06-22, 09-14 · GBPUSD 04-20, 07-27, 10-26.
- Good: DXY 03-09 (support 98.42-98.59 caught the week low, +195 pips), DXY 06-08 (range between Upper Resistance 100.06-100.16 and the in-fill 99.66-99.70), EURUSD 04-20 (Mid-Range Support caught the week low).
- Mixed: DXY 05-18 (week chopped around the Ceiling), GBPUSD 04-20 (chop inside Equilibrium), GBPUSD 07-27, 10-26, DXY 10-05 (Ceiling 102.16-102.25 pierced at first touch; the week's highs 102.45-102.5 have NO zone; Equilibrium held Tuesday's low).
- Bad: DXY 07-27 (after the Mon-Tue cap at Upper Resistance the sell-off closed through Equilibrium and three stacked supports 100.31-100.80), DXY 08-17 (support 99.36-99.52 held 60h then broke; nothing mapped below, week ended 98.6),
  EURUSD 06-22 and 09-14 (trend-down weeks: all candle zones are behind price, the side price travels into is almost empty).
Facts over all 40 harvested weeks x 3 pairs (e1_tool/out/OUTCOMES_all_weeks.txt, out/outcome_rows.json; a description, NOT an accuracy score): 614 named zones; 325 not reached, 54 week opened inside, 235 reached from outside.
 Of the 235: 77 never closed through all week, 38 held >24h, 56 held 4-24h, 64 closed through within 3 hours.
 Candle-anchored zones: 24 of 150 closed through within 3h. Level-only zones (sweep-level clusters): 40 of 85. Tier 1: 16 of 101. Tier 2: 48 of 134.
 By zone type: Hard Wall 2/14, Standard Wall 6/43, Post-Expiry Ghost 8/30, Soft Wall 48/148 closed through within 3h - in line with the prompt's ZFP ranges (5-15 / 15-30 / 20-40 / 30-50%).
VERDICT: the tool runs for any harvested week and the three pairs and reproduces the reference week's structures; it is NOT "90% everywhere". Do not claim it.

## Assumptions I had to make (the prompt + rulings do not settle them) — for the operator to confirm or correct
- A1 "strong directional move" on 4H = the move leaves an inefficiency gap between the candle before it and the candle after it (his SMC notes); no size minimum (L-37). Legs without such a gap give no zone.
- A2 sweep zones: every D1 swing extreme of the 90 daily bars that passes the wick test (major >=0.15 / minor >=0.08) + every swing of the last 10 days; drawn if recent or still unswept.
- A3 which areas become NAMED zones: every valid 4H candle (joined with the levels on it) + level clusters around an unswept swing extreme of the last 10 days. Plain level clusters with no candle and no swing extreme are NOT zones
  (both reference reports' zones are supply/demand structures; making every 0.15 cluster a zone gave 13-22 bunched zones). Names by position; Equilibrium = the zone at the weekly pivot point.
- A4 a demand candle with price now under it / a supply candle with price now over it is dropped; candles kept only at 0X-1X (his "one-time use"); older than 3 weeks dropped (prompt).
- A5 options: the sidecar's as-of page (Monday page only if published before 06:00Z, else Friday's forward rows); K from the latest Fed H.10 rates before the boundary. The report used the Monday page and its own K.
- Rejected on evidence: "any later close through a candle = broken" (deleted the 04-16 demand candle where Monday Apr 20 reacted); clustering candle zones within 0.10 (merged the report's Ceiling and Upper Resistance); gap in-fill out to weekly R3/S3 (12 lines per chart).

## Open point that is the operator's decision (I did not design around it)
When price leaves the last three weeks' 4H structure (breakout / sell-off weeks) the map ahead of price is empty, because the prompt drops 4H zones older than 3 weeks and A3 does not turn plain level clusters into zones.
Both bad weeks above are this case. Candidates that exist in the prompt: level clusters with a weekly pivot (R2/R3, S2/S3) + round number + option wall; 4H zones older than 3 weeks that are still unmitigated.

## Not built
Step 0d/0e D1 order blocks, Step 0g 1H nested precision, Step 1 HWC/LWC (optional), Pillars 4 and 7 (optional; printed as NO DATA). E2 and E3 untouched (out of scope).
