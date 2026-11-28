# M-67 / M-68 overnight report (2026-11-28)

Plan followed: `memory/16_PLAN_M67.md` (written before any code; changes to it are logged in its section 10).
All numbers come from the backtest you ordered (`tools/research/devset.py`): every drawn order replayed on the 15-minute candles with the chart's own rules, and the yellow Engine 2 line compared with the 30-minute closes.

## Bottom line
- **Trades: not at 80%.** On the 8 dev weeks x 3 pairs the build wins **13 of 33** filled trades (39%), about 1.4 filled trades per pair-week; the golden week stays **18 of 18**.
  The win rate before tonight read 41.7% (15 / 36), but two of those wins were the same move filled twice (now voided, see D-148).
  At an average winner of 4.3-4.9 R the dev trades still net about +41 R over 36 trades.
- **Engine 2 line: closer to the candles.** 30-minute closes within 10 pips of the line went from **41% to 53%** (golden 60% to 65%), the mean miss from **23.1 to 15.1 pips**, and 30-minute turns with a line vertex within one candle from **16 to 65** of 381. That is better, not your 95%.
- **Nothing regressed:** golden trades identical, Engine 1 byte-for-byte locked, every change behind a switch with its gates passed, leak checks clean.

## What was built (in plan order)
1. **Engine 1 lock** (`tools/locks/`): SHA-256 of the six Engine 1 modules + the sealed V1; the pre-commit hook refuses any commit that changes them.
2. **The backtest** (`tools/research/devset.py`): one command, per pair-week rows, totals, line metrics, trade excursions.
3. **D-147, Engine 2 micro path** (`e2_chain.micro_path`, drawing only):
   - the line restarts at each London open (02:00 NY) and each 10:00 NY cut, from the price closed by then (dotted step);
   - swing-scalp legs end at the 2nd Engine 1 level in their direction within 30 pips (GS Law 2; P533 "zone by zone"; Spiderwebs PDF "Target 2 or 3 levels");
   - other days keep the chain's levels, held inside the shape's Law-2 reach.
   Leak-checked segment by segment (`tools/leak_check_segments.py`).
4. **D-148, one trade per move** (L-52): an order touched while a same-direction trade is open is void (drawn as a stub). It found 3 duplicates on the dev weeks:
   - DXY Mar 23: three shorts at the identical entry 100.067, two of them filled on the same candle;
   - GBPUSD Mar 23: two longs at 1.32625, both filled 10:00;
   - EURUSD Apr 13: two shorts 7 pips apart, both stopped on the same move.

## 8 dev weeks x 3 pairs (before tonight / after tonight)
| Week | Pair | BEFORE drawn / filled / TP / SL | win | line <=10p / miss | AFTER drawn / filled / TP / SL (void) | win | line <=10p / miss | visible moves |
|---|---|---|---|---|---|---|---|---|
| 2026-03-02 | DXY | 2 / 2 / 0 / 2 | 0% | 38% / 26.6p | 2 / 2 / 0 / 2 (0) | 0% | 52% / 14.6p | 10 |
| 2026-03-02 | EURUSD | 1 / 0 / 0 / 0 | - | 20% / 46.9p | 1 / 0 / 0 / 0 (0) | - | 34% / 29.3p | 13 |
| 2026-03-02 | GBPUSD | 1 / 0 / 0 / 0 | - | 29% / 31.7p | 1 / 0 / 0 / 0 (0) | - | 35% / 21.8p | 13 |
| 2026-03-23 | DXY | 4 / 2 / 2 / 0 | 100% | 37% / 22.7p | 4 / 1 / 1 / 0 (1) | 100% | 44% / 17.8p | 6 |
| 2026-03-23 | EURUSD | 7 / 3 / 1 / 2 | 33% | 28% / 29.3p | 7 / 3 / 1 / 2 (0) | 33% | 44% / 19.9p | 10 |
| 2026-03-23 | GBPUSD | 5 / 4 / 2 / 2 | 50% | 22% / 42.0p | 5 / 3 / 1 / 2 (1) | 33% | 35% / 29.3p | 10 |
| 2026-04-13 | DXY | 2 / 1 / 0 / 1 | 0% | 28% / 25.6p | 2 / 1 / 0 / 1 (0) | 0% | 55% / 12.9p | 5 |
| 2026-04-13 | EURUSD | 3 / 2 / 0 / 2 | 0% | 50% / 15.3p | 3 / 1 / 0 / 1 (1) | 0% | 59% / 13.5p | 6 |
| 2026-04-13 | GBPUSD | 1 / 0 / 0 / 0 | - | 39% / 29.5p | 1 / 0 / 0 / 0 (0) | - | 45% / 17.9p | 8 |
| 2026-04-20 | DXY | 3 / 3 / 1 / 2 | 33% | 66% / 9.2p | 3 / 3 / 1 / 2 (0) | 33% | 73% / 8.0p | 4 |
| 2026-04-20 | EURUSD | 4 / 1 / 0 / 1 | 0% | 56% / 12.1p | 4 / 1 / 0 / 1 (0) | 0% | 63% / 9.7p | 6 |
| 2026-04-20 | GBPUSD | 3 / 1 / 0 / 1 | 0% | 44% / 17.7p | 3 / 1 / 0 / 1 (0) | 0% | 45% / 13.8p | 10 |
| 2026-05-18 | DXY | 1 / 0 / 0 / 0 | - | 64% / 9.6p | 1 / 0 / 0 / 0 (0) | - | 68% / 7.6p | 4 |
| 2026-05-18 | EURUSD | 3 / 2 / 1 / 1 | 50% | 39% / 18.9p | 3 / 2 / 1 / 1 (0) | 50% | 54% / 12.3p | 6 |
| 2026-05-18 | GBPUSD | 3 / 3 / 2 / 1 | 67% | 36% / 22.9p | 3 / 3 / 2 / 1 (0) | 67% | 58% / 13.5p | 13 |
| 2026-07-06 | DXY | 8 / 7 / 7 / 0 | 100% | 62% / 8.3p | 8 / 7 / 7 / 0 (0) | 100% | 75% / 6.9p | 3 |
| 2026-07-06 | EURUSD | 8 / 7 / 7 / 0 | 100% | 62% / 9.5p | 8 / 7 / 7 / 0 (0) | 100% | 66% / 8.6p | 5 |
| 2026-07-06 | GBPUSD | 4 / 4 / 4 / 0 | 100% | 56% / 13.8p | 4 / 4 / 4 / 0 (0) | 100% | 54% / 13.7p | 9 |
| 2026-08-31 | DXY | 3 / 1 / 0 / 1 | 0% | 27% / 40.7p | 3 / 1 / 0 / 1 (0) | 0% | 54% / 22.9p | 3 |
| 2026-08-31 | EURUSD | 1 / 0 / 0 / 0 | - | 50% / 17.3p | 1 / 0 / 0 / 0 (0) | - | 58% / 15.5p | 4 |
| 2026-08-31 | GBPUSD | 2 / 1 / 0 / 1 | 0% | 39% / 21.4p | 2 / 1 / 0 / 1 (0) | 0% | 54% / 14.8p | 5 |
| 2026-09-21 | DXY | 1 / 0 / 0 / 0 | - | 56% / 15.0p | 1 / 0 / 0 / 0 (0) | - | 71% / 8.0p | 2 |
| 2026-09-21 | EURUSD | 3 / 3 / 0 / 3 | 0% | 53% / 12.5p | 3 / 3 / 0 / 3 (0) | 0% | 65% / 10.3p | 5 |
| 2026-09-21 | GBPUSD | 1 / 0 / 0 / 0 | - | 27% / 32.7p | 1 / 0 / 0 / 0 (0) | - | 46% / 14.5p | 8 |
| 2026-10-05 | DXY | 2 / 2 / 2 / 0 | 100% | 48% / 14.6p | 2 / 2 / 2 / 0 (0) | 100% | 54% / 11.5p | 6 |
| 2026-10-05 | EURUSD | 2 / 2 / 1 / 1 | 50% | 40% / 21.5p | 2 / 2 / 1 / 1 (0) | 50% | 50% / 14.2p | 10 |
| 2026-10-05 | GBPUSD | 3 / 3 / 3 / 0 | 100% | 40% / 22.3p | 3 / 3 / 3 / 0 (0) | 100% | 53% / 12.0p | 12 |

**DEV (8 weeks x 3) BEFORE**: 61 drawn, 36 filled (1.5 per pair-week), 15 TP, 21 SL = 41.7% | line: 41% of 30m closes within 10 pips, mean miss 23.1 pips, 30m turns with a line vertex within one candle 16 / 381

**DEV (8 weeks x 3) AFTER**: 61 drawn, 33 filled (1.4 per pair-week), 13 TP, 20 SL, 3 void = 39.4% | line: 53% of 30m closes within 10 pips, mean miss 15.1 pips, 30m turns with a line vertex within one candle 65 / 381

**GOLDEN BEFORE**: 20 drawn, 18 filled (6.0 per pair-week), 18 TP, 0 SL = 100.0% | line: 60% of 30m closes within 10 pips, mean miss 10.5 pips, 30m turns with a line vertex within one candle 2 / 34

**GOLDEN AFTER**: 20 drawn, 18 filled (6.0 per pair-week), 18 TP, 0 SL = 100.0% | line: 65% of 30m closes within 10 pips, mean miss 9.8 pips, 30m turns with a line vertex within one candle 6 / 34

## Held-out weeks (never looked at before; run once with the final code)
HELDOUT_PLACEHOLDER

## Golden week Jul 6-10 - trades unchanged, risk-reward of every charted trade
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
| Canon close-out before market close | no change |
| Micro legs as trades | none reaches RRR 3 |

Session facts measured on 420 sessions:
- London takes out one side of the Asian range 94% of the time.
- Which side, and whether the break holds, is 49%.
- NY continues London 44%; a day continues the prior day 49%.

## Where my build is short, and the one thing I need from you
- My build does not yet tell **which zone price will turn at, and in which direction**, before the move: every mechanical rule I could build from the text calls it at chance on the dev weeks.
- Your golden webs (EURUSD 0 = 1.13925, 1 = 1.14315) are drawn on the retest leg; my readings of "nearest non-surge swing high/low" do not reproduce them.
- **Blocker:** mark 2-3 trades on any non-golden week **with the spiderweb anchors you set before entering** (which swing high / low, at what time). That is the missing rule; with it I can build the anchor choice instead of guessing it.

## Frames (whole week, one per map; `evidence/m67b/`; switch-off "before" frames in `evidence/m67b/before/`)
- Golden: DXY, EURUSD, GBPUSD Jul 6.
- Line change: EURUSD Oct 5, GBPUSD May 18, DXY Aug 31.
- Voided duplicates: DXY Mar 23, GBPUSD Mar 23, EURUSD Apr 13.
