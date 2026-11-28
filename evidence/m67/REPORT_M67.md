# M-67 / M-68 overnight report (2026-11-28)

Plan followed: `memory/16_PLAN_M67.md` (written before any code; every change to it is logged in its section 10).
All numbers come from the backtest you ordered (`tools/research/devset.py`): every drawn order replayed on the 15-minute candles with the chart's own rules, and the yellow Engine 2 line compared with the 30-minute closes.

## Bottom line
- **Trades: far from 80%.**
  - 8 dev weeks x 3 pairs: the build wins **13 of 33** filled trades (**39%**), 1.4 filled per pair-week.
  - 4 held-out weeks (run once, never looked at before): **2 of 15 (13%)**.
  - Golden week: still **18 of 18**.
  - Before tonight the dev number read 41.7%, but two of those wins were one move filled twice (now voided, D-148).
- **Engine 2 line: much closer to the candles, the same on unseen weeks.** 30-minute closes within 10 pips of the line:
  - dev **41% -> 59%**, held-out **59%**, golden **60% -> 67%**;
  - mean miss dev **23.1 -> 13.1 pips**;
  - 30-minute turns with a line vertex within one candle **16 -> 96** of 381.

  Better, not your 95%.
- **Where the trades lose (33 stop-outs on dev + held-out):**
  - 18 hit the stop and then reached their TP later that week: direction and target right, stop or entry wrong;
  - 9 more went 1.5R or more our way first;
  - only 6 were the wrong zone or direction.
- **Nothing regressed:** golden trades identical; Engine 1 locked byte for byte; every change behind a switch with its gates passed; leak checks clean.

## What was built (plan order)
1. **Engine 1 lock** (`tools/locks/`): SHA-256 of the six Engine 1 modules + the sealed V1. The pre-commit hook refuses any commit that changes them.
2. **The backtest** (`tools/research/devset.py`): one command, per pair-week rows, totals, line metrics, trade excursions.
3. **D-147, Engine 2 micro path** (drawing only; the orders are untouched):
   - the line restarts at the session anchors from the price closed by then: London open 02:00 NY, the NY option cage 08:00, the cut 10:00 (P452 6.6 rules 2-4), drawn as a dotted step;
   - swing-scalp legs end at the 2nd Engine 1 level in their direction within 30 pips (GS Law 2; P533 "zone by zone"; Spiderwebs PDF "Target 2 or 3 levels");
   - other days keep the chain's levels, held inside the shape's Law-2 reach.

   Leak-checked segment by segment at every anchor (`tools/leak_check_segments.py`, exit 0).
4. **D-148, one trade per move** (your L-52 ban on duplicates): an order touched while a same-direction trade is open is void (drawn as a stub). It found:
   - DXY Mar 23: three shorts at the identical entry 100.067, two filled on the same candle;
   - GBPUSD Mar 23: two longs at 1.32625 filled together;
   - EURUSD Apr 13 and Jul 13: two shorts on one move.

## 8 dev weeks x 3 pairs (before tonight / after tonight)
| Week | Pair | BEFORE drawn / filled / TP / SL | win | line <=10p / miss | AFTER drawn / filled / TP / SL (void) | win | line <=10p / miss | visible moves |
|---|---|---|---|---|---|---|---|---|
| 2026-03-02 | DXY | 2 / 2 / 0 / 2 | 0% | 38% / 26.6p | 2 / 2 / 0 / 2 (0) | 0% | 56% / 13.0p | 10 |
| 2026-03-02 | EURUSD | 1 / 0 / 0 / 0 | - | 20% / 46.9p | 1 / 0 / 0 / 0 (0) | - | 34% / 24.7p | 13 |
| 2026-03-02 | GBPUSD | 1 / 0 / 0 / 0 | - | 29% / 31.7p | 1 / 0 / 0 / 0 (0) | - | 35% / 20.1p | 13 |
| 2026-03-23 | DXY | 4 / 2 / 2 / 0 | 100% | 37% / 22.7p | 4 / 1 / 1 / 0 (1) | 100% | 53% / 14.7p | 6 |
| 2026-03-23 | EURUSD | 7 / 3 / 1 / 2 | 33% | 28% / 29.3p | 7 / 3 / 1 / 2 (0) | 33% | 46% / 18.6p | 10 |
| 2026-03-23 | GBPUSD | 5 / 4 / 2 / 2 | 50% | 22% / 42.0p | 5 / 3 / 1 / 2 (1) | 33% | 38% / 27.1p | 10 |
| 2026-04-13 | DXY | 2 / 1 / 0 / 1 | 0% | 28% / 25.6p | 2 / 1 / 0 / 1 (0) | 0% | 69% / 9.5p | 5 |
| 2026-04-13 | EURUSD | 3 / 2 / 0 / 2 | 0% | 50% / 15.3p | 3 / 1 / 0 / 1 (1) | 0% | 63% / 12.0p | 6 |
| 2026-04-13 | GBPUSD | 1 / 0 / 0 / 0 | - | 39% / 29.5p | 1 / 0 / 0 / 0 (0) | - | 50% / 14.2p | 8 |
| 2026-04-20 | DXY | 3 / 3 / 1 / 2 | 33% | 66% / 9.2p | 3 / 3 / 1 / 2 (0) | 33% | 74% / 7.6p | 4 |
| 2026-04-20 | EURUSD | 4 / 1 / 0 / 1 | 0% | 56% / 12.1p | 4 / 1 / 0 / 1 (0) | 0% | 62% / 9.7p | 6 |
| 2026-04-20 | GBPUSD | 3 / 1 / 0 / 1 | 0% | 44% / 17.7p | 3 / 1 / 0 / 1 (0) | 0% | 54% / 12.1p | 10 |
| 2026-05-18 | DXY | 1 / 0 / 0 / 0 | - | 64% / 9.6p | 1 / 0 / 0 / 0 (0) | - | 79% / 6.2p | 4 |
| 2026-05-18 | EURUSD | 3 / 2 / 1 / 1 | 50% | 39% / 18.9p | 3 / 2 / 1 / 1 (0) | 50% | 66% / 10.2p | 6 |
| 2026-05-18 | GBPUSD | 3 / 3 / 2 / 1 | 67% | 36% / 22.9p | 3 / 3 / 2 / 1 (0) | 67% | 56% / 12.4p | 13 |
| 2026-07-06 | DXY | 8 / 7 / 7 / 0 | 100% | 62% / 8.3p | 8 / 7 / 7 / 0 (0) | 100% | 76% / 6.7p | 3 |
| 2026-07-06 | EURUSD | 8 / 7 / 7 / 0 | 100% | 62% / 9.5p | 8 / 7 / 7 / 0 (0) | 100% | 67% / 8.4p | 5 |
| 2026-07-06 | GBPUSD | 4 / 4 / 4 / 0 | 100% | 56% / 13.8p | 4 / 4 / 4 / 0 (0) | 100% | 58% / 13.1p | 9 |
| 2026-08-31 | DXY | 3 / 1 / 0 / 1 | 0% | 27% / 40.7p | 3 / 1 / 0 / 1 (0) | 0% | 50% / 24.0p | 3 |
| 2026-08-31 | EURUSD | 1 / 0 / 0 / 0 | - | 50% / 17.3p | 1 / 0 / 0 / 0 (0) | - | 61% / 14.7p | 4 |
| 2026-08-31 | GBPUSD | 2 / 1 / 0 / 1 | 0% | 39% / 21.4p | 2 / 1 / 0 / 1 (0) | 0% | 63% / 11.8p | 5 |
| 2026-09-21 | DXY | 1 / 0 / 0 / 0 | - | 56% / 15.0p | 1 / 0 / 0 / 0 (0) | - | 77% / 6.4p | 2 |
| 2026-09-21 | EURUSD | 3 / 3 / 0 / 3 | 0% | 53% / 12.5p | 3 / 3 / 0 / 3 (0) | 0% | 71% / 8.0p | 5 |
| 2026-09-21 | GBPUSD | 1 / 0 / 0 / 0 | - | 27% / 32.7p | 1 / 0 / 0 / 0 (0) | - | 55% / 11.6p | 8 |
| 2026-10-05 | DXY | 2 / 2 / 2 / 0 | 100% | 48% / 14.6p | 2 / 2 / 2 / 0 (0) | 100% | 66% / 9.0p | 6 |
| 2026-10-05 | EURUSD | 2 / 2 / 1 / 1 | 50% | 40% / 21.5p | 2 / 2 / 1 / 1 (0) | 50% | 58% / 11.4p | 10 |
| 2026-10-05 | GBPUSD | 3 / 3 / 3 / 0 | 100% | 40% / 22.3p | 3 / 3 / 3 / 0 (0) | 100% | 69% / 8.2p | 12 |

**DEV (8 weeks x 3) BEFORE**: 61 drawn, 36 filled (1.5 per pair-week), 15 TP, 21 SL = 41.7% | line: 41% of 30m closes within 10 pips, mean miss 23.1 pips, 30m turns with a line vertex within one candle 16 / 381

**DEV (8 weeks x 3) AFTER**: 61 drawn, 33 filled (1.4 per pair-week), 13 TP, 20 SL, 3 void = 39.4% | line: 59% of 30m closes within 10 pips, mean miss 13.1 pips, 30m turns with a line vertex within one candle 96 / 381

**GOLDEN BEFORE**: 20 drawn, 18 filled (6.0 per pair-week), 18 TP, 0 SL = 100.0% | line: 60% of 30m closes within 10 pips, mean miss 10.5 pips, 30m turns with a line vertex within one candle 2 / 34

**GOLDEN AFTER**: 20 drawn, 18 filled (6.0 per pair-week), 18 TP, 0 SL = 100.0% | line: 67% of 30m closes within 10 pips, mean miss 9.4 pips, 30m turns with a line vertex within one candle 9 / 34

## 4 held-out weeks x 3 pairs (blind: harvested and run once with the final code)
| Week | Pair | drawn / filled / TP / SL (void) | win | line <=10p / miss | visible moves |
|---|---|---|---|---|---|
| 2026-03-30 | DXY | 0 / 0 / 0 / 0 (0) | - | 50% / 13.8p | 6 |
| 2026-03-30 | EURUSD | 0 / 0 / 0 / 0 (0) | - | 45% / 18.8p | 10 |
| 2026-03-30 | GBPUSD | 1 / 1 / 0 / 1 (0) | 0% | 50% / 18.6p | 14 |
| 2026-05-25 | DXY | 2 / 1 / 0 / 1 (0) | 0% | 78% / 6.8p | 1 |
| 2026-05-25 | EURUSD | 1 / 1 / 1 / 0 (0) | 100% | 71% / 7.6p | 5 |
| 2026-05-25 | GBPUSD | 2 / 2 / 1 / 1 (0) | 50% | 57% / 11.3p | 7 |
| 2026-07-13 | DXY | 1 / 1 / 0 / 1 (0) | 0% | 70% / 8.6p | 4 |
| 2026-07-13 | EURUSD | 7 / 3 / 0 / 3 (1) | 0% | 59% / 12.4p | 4 |
| 2026-07-13 | GBPUSD | 4 / 3 / 0 / 3 (0) | 0% | 57% / 18.9p | 7 |
| 2026-09-28 | DXY | 1 / 0 / 0 / 0 (0) | - | 59% / 11.1p | 5 |
| 2026-09-28 | EURUSD | 2 / 1 / 0 / 1 (0) | 0% | 55% / 14.9p | 7 |
| 2026-09-28 | GBPUSD | 3 / 2 / 0 / 2 (0) | 0% | 57% / 12.2p | 9 |

**HELD-OUT TOTAL**: 24 drawn, 15 filled (1.2 per pair-week), 2 TP, 13 SL, 1 void = **13%** | line: **59%** of 30m closes within 10 pips, mean miss 12.9 pips, turns with a vertex within one candle 50 / 153

Held-out week Jul 13-17 (the week after the golden week): the chain forecast a breakout DOWN. Both pairs broke UP on Tuesday 12:30 UTC, and four shorts went straight against it (best excursion 0.0R).

## Why the trades lose (all 33 stop-outs, dev + held-out)
| What happened after the stop | Count | Examples |
|---|---|---|
| price hit the stop, then reached the TP later the same week | 14 (+4 that also first went 1.5R+ our way) | EURUSD 03-23 EU1, GBPUSD 03-23 GB1, DXY 04-20 DX3, EURUSD 05-18 EU2 |
| went 1.5R or more our way, then reversed to the stop | 9 | DXY 03-02 DX1, EURUSD 09-21 EU2 / EU3, GBPUSD 04-20 GB1 |
| the zone broke - price ran 2x the risk beyond the stop | 6 | DXY 04-13 DX2, EURUSD 07-13 EU5, GBPUSD 07-13 GB3 |
| no follow-through either way | 4 | EURUSD 04-20 EU4, GBPUSD 05-18 GB1 |

How much wider the stop had to be for the 18 that later reached their TP:
- 4 needed only **0.9-3.5 pips** more (3 of them EURUSD, whose liquidity sits inside the zone - your L-50);
- 4 needed 5-15 pips;
- 10 needed 7-31 pips (those came back much later).

A uniform extra stop buffer, measured on every trade:
| Extra stop | Dev | Held-out | Golden |
|---|---|---|---|
| +0 pips | 39%, +36.5R | 13%, -7.4R | 18/18, +86.5R |
| +3 pips | 45%, +35.7R | 20%, -2.1R | 18/18, +62.6R |
| +5 pips | 45%, +29.5R | 27%, +0.2R | 18/18, +53.1R |

Not adopted: it moves every golden stop away from yours, and your L-50 asks for the wider of the canon's two stop placements, which D-135 already does, not a blanket buffer.

## Golden week Jul 6-10: trades unchanged, risk-reward of every charted trade
| Pair | Trades (all TP) | Average RR |
|---|---|---|
| DXY | DX2 4.1, DX3 3.1, DX4 6.3, DX5 4.0, DX6 3.4, DX7 3.1, DX8 3.9 | 3.98 |
| EURUSD | EU1 5.7, EU3 5.8, EU4 3.3, EU5 9.1, EU6 4.1, EU7 4.7, EU8 6.5 | 5.60 |
| GBPUSD | GB1 3.1, GB2 6.1, GB3 7.7, GB4 2.6 | 4.86 |

## Engine 1 (your ask: flaw / fix / regression risk / blast radius)
- **Flaw:** zone density. Many zones and rungs sit near every turn: the 11th outside count passed the bunching side-condition on only 8 of 12 maps.
- **Fix it would need:** fewer, stronger zones.
- **Risk / blast radius:** any change moves Engine 2's bounds and targets, every Engine 3 entry / SL / TP, and the golden matches - the whole product, high regression risk.
- **Decision:** locked, as you ordered. Nothing tonight touched it.

## What I tried for more / better trades and did NOT adopt (dev weeks; each would have lowered the win rate)
| Reading (canon source) | Win rate |
|---|---|
| Spiderwebs PDF items 3 / 4 / 5 as mechanical rules at each London open (anchors: Asian range, nearest 15m swings, same-day 30m swings, 4H swings; trend: 4H / 30m structure) | 10-36%; golden 0 / 9 |
| Every Engine 1 zone at its first touch, 3R | 26% (1,270 touches) |
| FA 6 "Earth + Fire" confluence, with or without 4H alignment | 19-39% |
| Fades inside the forecast range boxes | 28% |
| Zone reaction counter (2nd touch after a reaction) | 33% |
| Option-pin direction before the cut | 5 of 15 |
| Fading the London sweep of the Asian range | 24-46%, tracking its RR |
| Law 27 reverse at every TP | 4 / 13 |
| "4+ SS trades -> NY breakout" timing | no separation |
| Canon close-out before market close | no change |
| Micro legs as trades | none reaches RRR 3 |

Session facts measured on 420 sessions:
- London takes out one side of the Asian range 94% of the time.
- Which side, and whether the break holds, is 49%.
- NY continues London 44%; a day continues the prior day 49%.

## Where my build is short, and the one thing I need from you
- My build does not yet tell **which zone price turns at, and which way**, before the move: every mechanical rule I could build from the text calls it at chance on these weeks.
- The losers above show the second gap: the stop or entry sits a few pips too tight or early on trades whose direction was right.
- **Blocker:** mark 2-3 trades on any non-golden week with **the spiderweb anchors you set before entering** (which swing high / low, at what time) and **where you put the stop**. With that I can build your anchor and stop choice instead of guessing them.

## Frames (whole week, one per map; `evidence/m67b/`; "before" frames with the switches off in `evidence/m67b/before/`)
- Golden: DXY, EURUSD, GBPUSD Jul 6.
- Line change: EURUSD Oct 5, GBPUSD May 18, DXY Aug 31.
- Voided duplicates: DXY Mar 23, GBPUSD Mar 23, EURUSD Apr 13.
