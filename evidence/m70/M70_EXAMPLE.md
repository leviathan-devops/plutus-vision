# M-70: Engine 2 micro path, a practical example (plan `memory/17`, NOT adopted)

Everything below sits behind the switch `e2_chain.E2_MICRO`, which is **off** by default. With the switch off, the product is byte-identical to the checkpoint (golden Pine hashes `d3b7566dc53a3f0c` / `5f7eb11be2b4577f` / `92ac9af99b4f8b0b`, unchanged). With the switch on, **only the drawn yellow Engine 2 line changes**. The chain, day boxes, zones and orders stay identical on all 15 tested pair-weeks. The only exception: on a day where step 1 fires, the day box ends at the breaking candle and a new box starts there.

Exact code: `evidence/m70/M70_code.diff` (e2_chain.py +168 lines, plutus.py +75 / -2, tools/leak_check_segments.py +12 / -2; nothing else in the engine changed).

## What changes, step by step (each rule carries its canon line in the code)

| Step | What the new line does | Canon | Code |
|---|---|---|---|
| skeleton | Each day: Asia held at the trading-day open price; London + NY rebuilt **at the London open**, from bars closed by then, starting at the actual price | P452 6.6 rule 1; L-53 anchor | `plutus._micro_day` |
| skeleton | NY pre-cut 08:00-10:00: price held where it is (cage). Pinned to the day's largest strike only when that strike is within 7.5 pips (half the 5-15 pip cage range) | P452 rule 3; P533 2.2 | `e2_chain.micro_ss` |
| 1 | A **30-minute close beyond the Decision Zone** hands the line to the alternative chain **at that candle** (not at the next day's open). The leg runs toward the alternative's breakout target, arriving after 3 sessions; the next day's Asia extends it | 6.6 Step 4 (P533:1895); 6.8 'BS 1-3 sessions'; rule 6 | `plutus.daily_anchor` (step-1 block), `micro_target`, `micro_arrival` |
| 2 | Transitions on the trigger clock: a chain turn scheduled at 12:00 NY is drawn at 08:00 + held to the **10:01 release**; a BS leg through NY waits for **14:30** (DXY **15:00**) or an earlier auction close / EIA release | P452 rules 3-4; P533 2.2.1 '95% of NY swings ... after 2:30 PM'; FA 10 'DXY breakout ... 3pm'; 6.6 Step 5(d) | `micro_clock` |
| 3 | Inside a swing-scalp box the legs walk the Engine 1 zones in order. The first **opposing** zone that reacts turns the line: a BoM not yet depleted, or a pressure zone with 1-2 reactions. MoM / depleted / ZFP > 45 zones are pierced. Legs stay inside GS Law 2's SS reach (30 pips) | P533:215 / :491 / :493 / :211; 6.4.1; GS Law 2 | `micro_reacts`, `micro_walk` |
| 4 | Direction of the London leg = the **pressure** of the Asian session's 1H candles (bigger candles, wicks, triangle flat side); unclear -> 4H storyline; then the nearer bound | P452 rule 2; P533:497 / :499 | `micro_bias` |
| 5 | Where the line turns at a zone: DXY at the zone edge; EURUSD inside the zone at the liquidity rung overlapping it; GBPUSD beyond an S/D zone at the liquidity behind it | FA 10; your L-50 | `micro_turn` |

## Test: 15 pair-weeks (golden week + the 4 checkpoint weeks Apr 13 / Apr 20 / May 18 / Oct 5), each step added cumulatively

Measured on the 30-minute candles after each anchor (tools/research/devset.py): **within 10 p** = 30m closes within 10 pips of the drawn line; **miss** = average distance; **turns** = 30m turning points (15-pip swings) that have a line vertex of the same kind within one 30m candle.

| Variant (cumulative) | 4 checkpoint weeks (12 pair-weeks) | Golden week (3 pairs) | Golden DXY / EURUSD / GBPUSD within 10 p |
|---|---|---|---|
| **Previous E2 (product)** | 46% / 18.3 p / 6 of 160 | 60% / 10.5 p / 2 of 34 | 62 / 62 / 56% |
| skeleton (London-open restart, cage reading) | 45% / 18.9 p / 6 | 64% / 9.8 p / 4 | 72 / 63 / 57% |
| + steps 1-2 (Decision-Zone switch, trigger clock) | 45% / 18.2 p / 8 | 61% / 10.2 p / 2 | 72 / 61 / 50% |
| + step 3 (zone walk + Law 2 reach) | 50% / 15.2 p / 8 | 62% / 10.4 p / 2 | 76 / 59 / 51% |
| + step 4 (pressure direction) | 51% / 14.4 p / 8 | 62% / 10.4 p / 2 | 76 / 59 / 51% |
| **+ step 5 = the whole new E2** | **50% / 14.5 p / 8** | **62% / 10.6 p / 2** | **76 / 60 / 49%** |

Per pair-week (previous -> new, within 10 p / miss): golden DXY 62 -> 76% / 8.3 -> 6.8 p, EURUSD 62 -> 60% / 9.5 -> 9.0 p, GBPUSD 56 -> 49% / 13.8 -> 15.8 p; Apr 13 DXY 28 -> 47% / 25.6 -> 15.1 p, EURUSD 50 -> 45% / 15.3 -> 14.0 p, GBPUSD 39 -> 45% / 29.5 -> 17.3 p; Apr 20 DXY 66 -> 61% / 9.2 -> 10.8 p, EURUSD 56 -> 59%, GBPUSD 44 -> 50% / 17.7 -> 13.9 p; May 18 DXY 64 -> 63%, EURUSD 39 -> 52% / 18.9 -> 14.3 p, GBPUSD 36 -> 48% / 22.9 -> 17.3 p; Oct 5 DXY 48 -> 48%, EURUSD 40 -> 41%, GBPUSD 40 -> 43% / 22.3 -> 14.7 p.
Better on 9 of 15 pair-weeks, about the same on 3, worse on 3 (GBPUSD golden, DXY Apr 20, EURUSD Apr 13 on 'within 10 p').

Orders: identical in every variant (4 weeks: 30 drawn / 20 filled / 10 TP / 10 SL; golden: 20 / 18 / 18 / 0).
Leak check of the drawn segments (`tools/leak_check_segments.py`, every segment start is an anchor, incl. the 30m break): **clean** on golden DXY / EURUSD / GBPUSD (14 anchors each) and on DXY Apr 13 where step 1 fires (15 anchors). Outputs: `evidence/m70/leak/`; raw backtest rows: `evidence/m70/backtest/`.

## Golden week, previous E2 vs new E2 (frames `evidence/m70/*_side_by_side.png`)

Left = previous E2 (the product), right = new E2. Same candles, zones, day boxes and orders. Only the yellow line differs (Pine diff: 31 `line.new` statements on DXY, nothing else).

- **DXY Mon** (better): London top 101.151 on the 30m BoM supply (candle high 101.145), held through the cage, 10:01 release down to the floor 100.815 (candle low 100.838). The previous line went to 101.199, then dropped at 08:30 to the 1.1450 strike 100.977 while the candles stayed at 101.09-101.11 until 10:00.
- **DXY Tue** (wrong direction): the Asian-session pressure read DOWN, so London goes down to 100.864; the candles went up to 100.976. NY up to 101.038 (close 101.092).
- **DXY Wed**: the chain's RWL up / BS down on the trigger clock. Top 101.305 reached by 08:00, drop held until the 10:30 EIA release. The candles topped near 12:00 and dropped 12:00-14:30.
- **DXY Thu / Fri**: the line restarts at the London-open price (Thu 100.935, Fri 100.778; the previous line held 101.069 / 100.937). Thu's BS leg reaches 100.851 by 08:00 while the candles were at 100.979 (worse at 08:00). Fri's WL spike is drawn at 05:20; the candles made it in the Asian session.
- **EURUSD**: small changes. Mon London to the floor 1.14053 (candles 1.1412-1.1415), NY to 1.14387 (close 1.14413). Tue London 1.14388 (candles 1.14324-1.14362), NY 1.14189 (close 1.14122). Wednesday's low comes at 08:00 instead of 12:00.
- **GBPUSD Mon** (worse): the NY leg stops at 1.33435, UPPER RESISTANCE, a pressure zone with 1 reaction that step 3 reads as 'turns the line'. The candles ran through it to 1.3394, where the previous line ended. **GBPUSD Tue** better (London 1.33922 vs candles 1.33880). **GBPUSD Fri** worse: the London arrival at 08:00 (1.33941) is early; the candles were at 1.34261.

## Step 1 on a real case (it does not fire on the golden week)

Frame `evidence/m70/DXY_2026-04-13_side_by_side.png` (the Apr 13 Monday breakout = problem 3 of the plan). The Decision Zone (1H BoM demand, level 98.525) breaks on the **30m close 98.366 at Mon 15:00 NY**. The new line hands over to the alternative's BS down **at that candle** (new box 'Mon BS down'), toward the KEY SUPPORT BAND 98.054, arriving after 3 sessions. Tuesday's Asia extends it (Tue 02:00: line 98.244, candles 98.343). The previous line kept the SS range until Tuesday's open and then swung 100+ pips across a 145-pip range all week. With the GS Law 2 reach (SS 30 pips) the new line stays near the candles: Apr 13 DXY within 10 p 28 -> 47%, miss 25.6 -> 15.1 p.

## Issues found (for your audit)

1. **Step 3, P533:211** ('a pressure zone with juice ... price will liquidate that zone first ... use it for entries/TPs'): I read it as 'the line turns at that zone'. GBPUSD golden Monday shows price going straight through such a zone (1 reaction) to the range top, so this reading cost that day.
2. **Step 4** (pressure of the Asian 1H candles) picked the wrong London direction on DXY golden Tuesday (line down, candles up to 100.976) and DXY Apr 13 Wednesday (line down, candles up to 98.215). On the 15 pair-weeks it moved the 4 weeks from 50% to 51% (miss 15.2 -> 14.4 p) and changed nothing on golden.
3. **Step 2** (trigger clock) added turn hits on the 4 weeks (6 -> 8 within one candle) but made golden worse (64 -> 61%; GBPUSD 57 -> 50%): Wednesday's real turn was ~12:00 and the drop came before 14:30.
4. **Step 5** (pair mechanics) changed little (4 weeks 51 -> 50%, golden GBPUSD 51 -> 49%).
5. **Fixed during the test, before this report**: step 1's leg turned back into the range when the alternative's target lay behind the breaking close; the leg reached its target in 2 hours; and the GS Law 2 SS reach named in step 3 was not yet applied. All three are fixed above (D-149b).
6. **Distance to the target**: the whole new E2 puts 50% (4 weeks) / 62% (golden) of 30m closes within 10 pips of the line, with 8 of 160 / 2 of 34 turns within one candle. Your target is 90-95% with turns inside one candle. The biggest single gain is step 3 (zone walk + Law 2 reach: miss 18.2 -> 15.2 p on the 4 weeks).

The product is unchanged and the switch stays OFF until you approve.
