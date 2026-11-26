# Outside G1 count — brief for a fresh reviewer (you did not build this; be strict, the builder may not grade itself)

Repo: /home/user/plutus-vision (branch AGENT). A tool forecasts, from data before Monday 02:00 New York, the week's (E1) zones, (E2) day-by-day shape chain, (E3) trade setups, and draws them on a 1H chart.
Your job: count, per map, how much of each engine the week's candles confirmed. You judge from the FRAMES (pixels). Numbers files are there only to read exact prices.

## Maps (12): pairs DXY, EURUSD, GBPUSD x weeks 2026-07-06, 2026-04-20, 2026-10-05, 2026-05-18
For each map there are two frames in evidence/s3/: `PAIR_MONDAY_zones.png` (candles + zones only) and `PAIR_MONDAY_all.png` (zones + day boxes + yellow path line + position boxes).
The forecast week is the right part of each frame (from the Monday date in the file name to the Friday); candles left of it are history the tool was allowed to see.
Facts files (exact numbers, same order): audit/g1_facts/PAIR_MONDAY.txt = the zone list, the forecast day map with each day's actual high / low / close, every setup with entry / SL / TP and what the 15m candles did to it.
For the week 2026-07-06 the operator's own trades (the trades that count as "obvious" that week) are in context_management/oracle/golden_week.json under each pair's "trades".

## Procedure per map — in this order
1. Open the `_zones` frame FIRST. Before looking at any setup, write down the obvious trades of the week: every clean zone-to-zone move visible on the 1H chart (direction, from about which price to about which price, which day). For 2026-07-06 use the operator's trades instead.
2. E1 count: for every zone price reached during the forecast week: REACTED (sharp rejection OR consolidation in / around it) / PIERCED like paper. Also list obvious turning points of the week that have NO zone, and any zone that is bloated, bunched with others, or floating far from price.
   E1 % = reacted / (zones reached + obvious turning points with no zone).
3. Open the `_all` frame. E2 count: for each of the five days compare the forecast (shape, direction, key zone, the day box and the yellow line) with that day's candles: RIGHT / WRONG with one line why. E2 % = days right / 5.
4. E3 count: for each obvious trade from step 1: CAUGHT (a setup of the same direction at that zone that filled and reached its TP before its SL) / MISSED. Name every stopped-out setup. E3 % = caught / obvious trades.
5. Presentation defects you see (labels over candles or over each other, clutter that hides candles, zones drawn far away).

## Output
Write audit/G1_count_dryrun.md: one section per map with the lists above and the three percentages, then one table of all 12 maps (E1 %, E2 %, E3 %), then the five defects that cost the most across maps, each with the map and the price / day where it shows.
Do not edit any other file. Do not soften: a zone crossed with no reaction is PIERCED; a setup that was stopped is a loss even if price later went to its TP.
