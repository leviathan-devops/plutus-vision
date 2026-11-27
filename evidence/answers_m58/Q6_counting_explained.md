# Q6 — The counting question, with its frame of reference

## Where the question comes from
Your goal (M-53): "You should be able to catch 90% of the visibly obvious trades that actually occurred during that trade week.
It doesn't mean that you catch two trades and count that as 90% accurate when there were 11 trades that were visibly obvious."

So my E3 number = trades my map caught / obvious trades that existed that week.
- Golden week (Jul 6-10): the bottom of that fraction is YOUR trades. Clear.
- Every other week: nobody had marked the trades. So a fresh outside agent (never saw my code) looks at the 1H chart
  and writes down "every clean zone-to-zone move" BEFORE it looks at my orders. My reported E3 numbers (50.7%, 34.8% outside the golden week) come from that list.

The problem: the list depends on who writes it.

## Example 1 — EURUSD, week of Oct 5 2026 (frame: evidence/s3k/EURUSD_2026-10-05_all.png)
Range week: floor ~1.1165-1.1172, ceiling ~1.1250-1.1277. Same code, same orders, two outside counters:

| Counter A (tenth count) - 10 obvious trades | Counter B (eleventh count) - 5 obvious trades |
|---|---|
| Mon L 1.1169 -> 1.1221 | Mon L 1.1169 -> 1.1225 |
| Mon S -> 1.1186 | Tue L 1.1203 -> 1.1277 |
| Tue L -> 1.1277 | Tue-Wed S 1.1277 -> 1.1165 |
| Wed S -> 1.1165 | Thu L 1.1172 -> 1.1227 |
| Thu L -> 1.1213 | Fri S 1.1243 -> 1.1187 |
| Thu S -> 1.1172 | |
| Thu L -> 1.1227 | |
| Thu S -> 1.1185 | |
| Fri L -> 1.1243 | |
| Fri S -> 1.1187 | |

My map caught 2 in both cases -> E3 = 20% for A, 40% for B. Across all 12 test maps A listed 95 obvious trades, B listed 67.
A counts every swing; B counts only moves that start at a zone and end at the next zone.

**6a. Which list is right in your eyes - every swing (A), zone-to-zone moves only (B), or something else?**
Your library answers this without you writing anything: the trades you marked on those weeks ARE the obvious trades.
Unless you say otherwise, I now count my orders against your marked trades on the library weeks, and drop the outside counters' own lists there.

## Example 2 — repeats (same frame)
My code places one range-floor long (EU1 LONG 1.11710) on Monday and re-arms it every day it stays valid:
EU1.Tue, EU1.Wed, EU1.Thu, EU1.Fri = four more boxes at the same price. Same for the ceiling short EU2 (EU2.Wed, EU2.Thu, EU2.Fri).
On the chart that is 2 trade ideas drawn as 9 boxes.

**6b. (i) Does each daily re-arm count as its own setup toward "<= 11 per pair per week" / "6-10 per week, 1-3 per day" (R-07)?
(ii) If the floor holds three times and three re-armed longs win, is that 3 trades or 1?**
