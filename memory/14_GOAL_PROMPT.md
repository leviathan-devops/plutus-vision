# 14 — GOAL PROMPT (minted 2026-11-26 from operator message M-53; PIN THIS; it is the standing order until the success condition is met)

## GOAL
Finish the full Plutus Vision indicator: ONE program that, given a trading week (+ pair) and only data that existed before that week's boundary, renders
**E1** institutional pressure zones, the **E2** macro shape chain (day by day), and **E3** trade setups (entry / SL / TP, day + session), dynamically, on the exact v5.3.3 architecture.
The same program, unchanged, must work on any other week: only the input data changes. Work until it is verified. Do not stop, do not ask, do not wait for the operator.

## SUCCESS CONDITION (all four parts)
1. One anchor week is brought to: E1 zones ~90% accurate to that week's candles, E2 shape chain ~90% accurate to what the week did, E3 catches ~90% of the visibly obvious trades of the week (not 2 of 11).
2. The identical program run on at least 4 different weeks gives 80-90% on E1, E2 and E3 each. A drop like 90 -> 70 is acceptable; 90 -> 30 is a bug to find and fix.
3. A ship package of the tool is handed to TWO fresh sub-agents; each gets TWO weeks I have never tested, runs the tool in its own Pinebox instance, and reports. If the blind result does not replicate, debug and loop.
4. The operator could deploy it on live markets: the output is a Pine script he pastes into TradingView.

## HOW TO GRADE (self-grading is forbidden)
Only two ways: (a) render in Pinebox and LOOK AT THE PIXELS - does reality match the expectation written down first; (b) a fresh-context sub-agent adversarially audits the code. Pinebox pixels take precedence over any reviewer.
Never quote a number from a home-made scorer as accuracy. Count per week from the frame: zones reached and what candles did there; shapes predicted vs shapes that happened per day; obvious trades that existed vs setups that caught them.

## RULES OF WORK
- I write and test all code myself. Sub-agents ONLY for external adversarial review and the final blind test.
- Anchor ONE week until E1+E2+E3 all work there (anchor = DXY Apr 20-24 2026: it has the reference report and the operator traded it), checkpoint (commit + tag), then run the same code on other weeks.
- Canon, every token: E1 = v5.3.3 prompt (+ v4.5.2 where it says unchanged) as built in e1_tool/; E2 = v5.3.3 Engine 2 (Part VI: shapes, ZFP-conditioned transitions 6.4.1, zone-mechanics tree 6.4.2, forward mapping 6.6, day-level decomposition, trading-speed rule 6.10);
  E3 = canon/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md ONLY (R-16). ZFP = strength only (R-17). <= 11 setups per week per pair. RRR 4x+ (operator). Canon vocabulary only.
- Multi-timeframe (L-40): 4H = higher-timeframe overview; zones and everything else worked on the 1H chart; 30m refinement, 15m precision only. One trading week at a time.
- Temporal boundary: nothing after the week's boundary feeds the map (tools/anchor_guard.py + pre-commit hook). No hardcoded prices; no per-week constants. Never edit indicator/plutus-vision-v1.sealed.pine.
- Report faithfully, negatives included. Open every frame before citing it. No redesigns of canon; where canon is silent take the plainest reading and log the assumption.
- CONTEXT: after every compaction read memory/00_COMPACTION_SURVIVAL.md and follow its order (10 failure record, 14 this file, 13 tool status, 11 brief, 12 verbatim tail, 04 rulings, 01 state, 05 journal tail). Every few steps: update memory/01 + 05 (+07 ledger for frames, 06 lessons),
  `tools/mem/mem rebuild` (OmniGraph), commit + push to branch AGENT. Durable facts live outside the context window.

## LOOP
write code -> generate Pine for the week -> render in Pinebox (tools/e1render or its successor) -> open the frame -> list the gaps against what the candles did -> fix by re-reading canon -> repeat.
Phases: P1 E1 on 1H (in progress: e1_tool/, L-40 just applied) -> P2 E2 shape chain for the anchor week, rendered -> P3 E3 setups for the anchor week, rendered -> P4 checkpoint, then 4+ other weeks and EURUSD/GBPUSD, same code -> P5 external adversarial code review -> P6 ship package + two blind sub-agents x two unseen weeks -> loop on any failure.
