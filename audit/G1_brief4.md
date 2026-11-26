# Outside G1 count 4 — brief for a fresh reviewer (you did not build this; be strict, the builder may not grade itself)

Repo: /home/user/plutus-vision (branch AGENT). A tool forecasts, from data before Monday 02:00 New York, the week's (E1) zones, (E2) day-by-day shape chain, (E3) trade setups, and draws them on a 1H chart.
Your job: count, per map, how much of each engine the week's candles confirmed. You judge from the FRAMES (pixels). The facts files are there only to read exact prices and times.
You have not seen any earlier count. Do not read audit/G1_count_dryrun*.md, memory/, or the tool's code.

## Maps (12): pairs DXY, EURUSD, GBPUSD x weeks 2026-07-06, 2026-04-20, 2026-10-05, 2026-05-18
Frames in evidence/s3d/: `PAIR_MONDAY_zones.png` (two weeks, candles + Engine 1 only), `PAIR_MONDAY_all.png` (two weeks, every layer), `PAIR_MONDAY_week.png` (the forecast week only, every layer, price axis fitted to the week).
The forecast week is the right part of each frame (Monday of the file name to Friday); candles left of it are history the tool was allowed to see. Labels sit in the left (history) half of the two-week frames.
Facts: audit/g1_facts_d/PAIR_MONDAY.txt = every Engine 1 object on the chart with its prices, the forecast day map next to each day's actual high / low / close, every setup with entry / SL / TP and what the 15m candles did to it.
For the week 2026-07-06 the operator's own trades (the "obvious trades" of that week) are in context_management/oracle/golden_week.json under each pair's "trades"; a trade whose entry price was only available before Monday 06:00 UTC is outside the forecast window.
For DXY 2026-04-20 the operator's two real trades of that week are known and are that map's obvious trades (project goal, S3): LONG 98.02 / SL 97.87 / TP 98.77 and LONG 98.29 / SL 98.185 / TP 98.77 (his levels come from his own chart; a setup counts as his trade when it is the same direction at the same turn, entry within about 3 pips).
You may read 1H / 15m bars read-only with `e1_tool/e1_data.py` (`bars(pair, '60')`) to check a time or a close.

## What is on the chart (legend)
Engine 1 (the operator's definition: "E1 = the sealed V1 underneath: order blocks (supply/demand) + the liquidity ladder; on top the prompt's E1: IP zones, liquidity sweep zones, canonical 4H / 1H supply/demand"). ALL of these are Engine 1 zones:
- pressure (IP) zones: red (resistance) / orange (equilibrium) / teal (support) boxes, white label `NAME | degree | ZFP | tier`;
- supply / demand candle zones: red (supply) / blue (demand) boxes, white label like `1H (Unmitigated) | MoM`;
- liquidity sweep zones: bright green boxes with a green label `LSZ supply-side | sweep to PRICE`; the dotted outline beyond the box is the sweep reach. Canon: "Liquidity Sweep Zone: level at a prior exact swing low [high] - high probability of brief breach then reversal"; "Institutions often sweep 0.05-0.10 beyond the visible extreme before reversing";
- liquidity bands of the sealed V1 (4H): darker green bands without a label;
- amber lines: option-strike targets (levels, not zones).
Engine 2: one grey box per day with the day's tag (`Mon SS 80%`), and the yellow line = the forecast path (a thin dotted line = the alternative chain). Canon shapes:
- SS (swing scalps): "Price oscillates within a defined range bounded by IP zones above (resistance ceiling) and below (support floor), forming a series of swing highs and swing lows that respect these boundaries. Each swing typically spans 1-3 trading sessions." Direction = range. The box runs into its two bounding zones.
- BS (breakout surge): "Price breaks decisively through an IP zone, then surges directionally toward the next IP zone."
- WL (whiplash): "A rapid, violent directional move that immediately reverses - spike-and-reject." RWL = "a Whiplash in the opposite direction of the preceding BS."
- R (recovery): "Temporary stabilization or mild retracement immediately after a BS or Whiplash."
Engine 3: position boxes - red part = stop side, green part = entry -> take-profit, the entry on their shared edge; a dotted green band on the entry side = the first-contact (front) entry: the order is met there. Label `ID shape S|L RRR`. A box with DASHED outlines and `if ID` in its label is a reinforcement: a conditional order that only exists once its parent setup has filled.
- gap in-fill levels: dashed boxes labelled `GAP IN-FILL | MODERATE | ZFP` (Engine 1). Sweep zones of one side within 5 pips of each other are drawn as one box.

## Counting rules (the project's grading rule G1, verbatim)
"One verdict per drawing with its specific delta - zone: reacted (sharp rejection OR consolidation in / around it) / pierced like paper / not reached; day: forecast shape + direction + key zone vs that day's candles; setup: filled? TP before SL?
Counting for a week: E1 = zones that reacted / (zones reached + obvious reaction points of the week that have no zone), and none bloated, bunched, floating or missing;
E2 = days right / 5; E3 = obvious trades caught / obvious trades that existed (anchor week: his own trades; other weeks: every clean zone-to-zone move visible on the 1H chart, listed BEFORE looking at my setups), every stopped-out setup named."

## Procedure per map - in this order
1. Open the `_zones` frame FIRST. Before looking at any setup, write down the obvious trades of the week: every clean zone-to-zone move visible on the 1H chart (direction, from about which price to about which price, which day). For 2026-07-06 use the operator's trades in the window instead.
2. E1: for every Engine 1 zone (any of the four kinds) that price reached during the forecast week: REACTED / PIERCED like paper (crossed with no reaction). List obvious turning points of the week that have NO Engine 1 zone at them, and any zone that is bloated, bunched with others, or floating far from price. E1 % by the rule above.
3. Open the `_all` and `_week` frames. E2: for each of the five days compare the forecast (shape, direction, key zone; the day box and the yellow line show them) with that day's candles: RIGHT / WRONG with one line why. A day with no designation is WRONG unless nothing happened. E2 % = days right / 5.
4. E3: for each obvious trade from step 1: CAUGHT (a setup of the same direction at that zone that filled and reached its TP before its SL) / MISSED. Name every stopped-out setup. E3 % = caught / obvious trades.
5. Presentation defects (labels over candles or each other, clutter that hides candles, zones drawn far away).

## Output
Write audit/G1_count_dryrun4.md: the counting rules you applied (so anyone can recount), one section per map with the lists above and the three percentages, one table of all 12 maps (E1 %, E2 %, E3 %; totals for all 12 and for the 9 maps outside 2026-07-06), then the five defects that cost the most across maps, each with the map and the price / day where it shows.
Do not edit any other file. Do not soften: a zone crossed with no reaction is PIERCED; a setup that was stopped is a loss even if price later went to its TP; a day whose candles did something else than the tag says is WRONG.
