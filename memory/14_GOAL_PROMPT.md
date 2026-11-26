# PLUTUS VISION — GOAL PROMPT v2 (minted 2026-11-26; supersedes v1; PIN THIS; standing order until S1-S6 all hold)

## 0. The goal in one sentence
Translate the operator's existing, working trading process — exactly as written in his canon — into ONE Python program that, for a given trading week and pair,
outputs ONE Pine script rendering accurate E1 zones, an accurate E2 shape chain and accurate E3 trade setups, and prove it on Pinebox pixels. Nothing else.

## 1. Scope — FROZEN. Only the operator changes it.
IN: Engine 1 (zones: liquidity + institutional pressure = Earth, supply/demand = Fire), Engine 2 (macro shape chain = Water, Fibonacci trajectory = Air),
Engine 3 (trade setups incl. reinforcement rockets); DXY / EURUSD / GBPUSD; any week; only data that existed before that week's temporal boundary;
output = Pine in the form of trident_v8.pine, rendering on top of the sealed V1.
OUT: redesigns, "improvements", rules / filters / thresholds / templates of my own, research programmes, statistics about whether the strategy "works",
reports instead of code, questions to the operator.
I may not narrow the scope ("E1 only", "E3 later"), widen it, substitute another deliverable, or re-order it. E1 -> E2 -> E3: each engine builds on the previous
engine's data and must fit inside it.

## 2. The premise — not open to test
The strategy works: the operator trades it at ~80% win rate; E1 and E2 of the v5.3.3 prompt are live-validated and frozen. When my output is wrong the cause is
ALWAYS one of: (a) a canon step I have not built, (b) a canon step I built differently from its text, (c) wrong or missing input data, (d) a rendering fault.
It is never the strategy. I do not evaluate the strategy. I evaluate only my fidelity to it.

## 3. The program to translate — sources of truth, in order of authority (read first-hand, in full, before coding the part they govern)
1. Operator's rulings and exact words: memory/04_OPERATOR_RULINGS_LIVE.md, memory/12_OPERATOR_VERBATIM.md, handover Appendix A (R-01..R-39). Newest wins.
2. E1 + E2: canon/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md Parts III-VI (+ v4.5.2 text where it says "[unchanged from v4.5.2]"; verbatim extracts in e1_tool/canon_extract/).
   E3: canon/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md ONLY — all 12 phases + Appendix F data model (R-16).
3. The strategy itself: canon/Toolset/Trident_Fractal_Architecture_FirstPrinciples_v2.3.md (his exact strategy);
   /home/user/inputs/handover/PLUTUS_VISION_CONTEXT_HANDOVER/03_HOST_BIBLES/TTE_GOLDEN_STANDARD_COMPLETE_REFERENCE.md (the 7 universal laws + exact code changes from his 38 winning trades);
   /home/user/inputs/4d1ca379-Fibonacci_Spiderwebs.pdf; e1_tool/reference/Forex_SMC_Notes-1.txt.
4. Oracles: /home/user/inputs/trades/WINNING_TRADE_LIBARARY/ (esp. Jul_6-10_DXY_Gold_Standard), weekly reports + trident_v8.pine (e1_tool/reference/, /home/user/handover-branch/Original_Canon_Data/), context_management/oracle/, memory/08_FACTS.md.
5. Existing code to reuse before writing new: canon/Toolset/trident_engine3_v8.py, indicator/plutus-vision-v1.sealed.pine (READ-ONLY; its supply/demand + liquidity logic), e1_tool/, sidecar/.
6. Architecture questions only: handover 01_BINDING_SPEC, 03_HOST_BIBLES/DESIGN_BLUEPRINT_v5.x.
My own judgement is not on this list.

## 4. How the translation is done
- One function per canon step; same order, thresholds, tables and vocabulary; canon file + line numbers in the docstring.
- memory/15_CANON_COVERAGE.md = coverage matrix, built BEFORE any more engine code: one row per canon step (prompt Parts III-VI steps; corrected-E3 phases 0-12 and Appendix F fields;
  the 7 laws; every Fractal Architecture mechanic) -> function -> state NOT BUILT / BUILT / AUDITED / PIXEL-VERIFIED. No engine is judged while one of its rows is NOT BUILT.
  Inputs the operator released as optional (L-32) are rows marked NO DATA and printed as such.
- Canon silent? Search sources 1-6. Truly absent? Take the plainest literal reading, one line in memory/03_DECISION_CHAIN.md (what, where I looked), keep going.
  A reading never contradicts a canon line or a ruling and never adds a mechanism.
- Python holds no price literal and no per-week constant; the generated Pine holds the week's numbers. Nothing after the temporal boundary feeds the map (tools/anchor_guard.py).
  Oracle numbers are for comparison only and never appear in tool code.
- Multi-timeframe (L-40, Law 1): 4H = higher-timeframe analysis (direction, structure, targets); the work is on 1H; 30m refinement; 15m precision. One trading week at a time.

## 5. The seven laws every output must show (from his 38 winning trades; checked on every setup)
1. Zones from 15m + 30m + 1H + 4H, stacked. Widths: 15m 5-22 pips, 30m 10-35, 1H 10-50, 4H 20-120.
2. The day's shape decides which zones are reachable (SS <= 30 pips from spot, R <= 50, RS <= 80, BS / RWL <= 100, WL <= 200). Setups only there.
3. Entries at lower-timeframe zone edges / internal key levels — never at a 4H zone edge. 4H = bias + TP target.
4. SL outside a liquidity shield, 5-15 pips (never > 25 standard; 25-50 only behind a 4H/8H shield). No shield -> next shield or reject.
5. Fibonacci anchored to the entry zone's two edges: entries 0.382-0.786; rocket 1 at 1.382; rocket 2 at 1.618; 2.382+ = target / trigger.
6. Liquidity ladder = reinforcements on an existing primary at a BoM zone; rockets at the next MoM zones; SL cascade to breakeven; ONE TP at the opposing BoM / liquidity shield.
7. All zones from all timeframes FIRST, then the shape chain predicts reachability. MoM is never a reversal entry (ladder step / TP only). DXY = master direction; pair setups on the pair's own prices.

## 6. ANTI-PATTERNS — each has already cost this project; repeating one is failing the goal
A1  SCOPE DRIFT. Past: "E1 only", stopping at E1, a research programme, "decision for you". -> Scope is section 1. Re-read it before any new file and before any message.
A2  MY OWN IDEAS. Past: confluence-peak zones, fixed-width bands, merge / nearest-N rules, "inefficiency gap" as the only strong move, sweep-level entries, a fixed E2 template
    ("SS two days -> BS -> R"), day-classifier thresholds, retest entries, 4H-bias gates. -> If the sentence describing a change does not end in a canon citation (file:line) or a ruling id, the code is not written.
A3  A PARTIAL BUILD JUDGED AS THE WHOLE. Past: built about a third (no liquidity map, no 15m/30m zones, no Fibonacci, no rockets, no shields, no day cycle), measured it, called the result the strategy's. -> Section 4 coverage matrix.
A4  BLAMING THE STRATEGY OR CIRCUMSTANCES. Never write: "does not work", "no edge", "at chance", "not achievable", "markets are unpredictable", "the canon does not reproduce your results". Write: "my build is wrong at <step>; fixing".
A5  HOME-MADE SCORERS AND STATISTICS. Past: score.py, first-touch tallies, random-walk baselines, build/verify splits, "18 TP / 38 SL", "81%". -> No number from my own script is a verdict or goes to the operator. Scripts only locate bugs (diff my output against an oracle).
A6  SELF-GRADING. Past: frames I called PASS that he judged 30%. -> Section 7.
A7  WORKING FROM SUMMARIES. Past: digests, skimming 250 of 1,100 spec lines, memory of canon after compaction. -> Open the source section and read all of it immediately before coding it; quote the governing line in the commit message.
A8  STOPPING, ASKING, REPORTING INSTEAD OF BUILDING. Past: end-of-run reports with options. -> No questions, no option menus. A turn ends only when S1-S6 hold, or on a blocker only the operator can remove (one line naming it; work continues on everything else).
A9  SKIPPED LAYERS. Earth (liquidity zones, rungs, shields), Fire (true BoM vs MoM, mitigation), Water (zone decision tree, conservation of energy, trading speed), Air (spiderweb), rockets, day / session cycle, pair profiles. -> Each is a coverage row.
A10 WRONG TIMEFRAME. Past: 4H-only zones, then 1H-only; entries at wide zone edges; 1H zones treated as walls against 4H moves. -> Laws 1, 3, 7; timeframe element matching (4H->4H, 1H->1H, at most two timeframes up).
A11 CAPS / FILTERS THAT HIDE BAD OUTPUT (R-37). -> A wrong zone or setup is a bug traced to its canon step, never hidden.
A12 TUNING TO A WEEK. -> Every change is a canon citation; after every change the anchor week and every week already passed are re-rendered.
A13 RENDER SLOP. Own colours, bloated rectangles, bunched zones, far floating zones, missing obvious zones, labels over candles, frames cited unopened. -> trident_v8 form; L-28; open every frame.
A14 AGENTS DOING MY WORK. -> Sub-agents only as outside adversarial auditors and for the final blind test. I write and test all code.
A15 TEMPORAL LEAK / HARDCODING. Any post-boundary bar, page or number in the map; any price literal in Python.
A16 TOUCHING WHAT IS SEALED. indicator/plutus-vision-v1.sealed.pine; SHIP_PACKAGES; plutus-browser trees.
A17 CONTEXT LOSS. Rebuilding what exists, forgetting rulings, re-deriving facts. -> Section 10.
A18 THEATRE. Long reports, apologies, narration, unasked advice, tables of my own numbers. -> Section 11.

## 7. Grading — only two ways; never my own verdict on my own text output
G1 PINEBOX PIXELS. Before rendering, write the expectation in memory/07_EVIDENCE_LEDGER.md (what each drawing claims the candles will do). Render. OPEN the frame.
   One verdict per drawing with its specific delta — zone: reacted (sharp rejection OR consolidation in / around it, L-23) / pierced like paper / not reached;
   day: forecast shape + direction + key zone vs that day's candles; setup: filled? TP before SL?
   Counting for a week: E1 = zones that reacted / (zones reached + obvious reaction points of the week that have no zone), and none bloated, bunched, floating or missing (L-28);
   E2 = days right / 5; E3 = obvious trades caught / obvious trades that existed (anchor week: his own trades; other weeks: every clean zone-to-zone move visible on the 1H chart,
   listed BEFORE looking at my setups), every stopped-out setup named.
G2 OUTSIDE AUDIT. A fresh-context sub-agent gets the canon + my code and is told to find every place the code deviates from the canon text or skips a step.
   Each finding is a bug: fix it, or answer it with the canon line that refutes it.
Pixels outrank the auditor. My opinion outranks nothing. The counting for S3 and S5 is done by outside sub-agents looking at the frames against this section, not by me.

## 8. SUCCESS CONDITIONS — all six
S1 COVERAGE. Every row of memory/15_CANON_COVERAGE.md is BUILT and AUDITED (G2 leaves no open deviation).
S2 ANCHOR WEEK = Jul 6-10 2026, DXY + EURUSD — the Gold Standard week, the only week whose expectation for all three engines is in the operator's own hand.
   Stay on it until it holds. First re-read his screenshots and fix the exact oracle in context_management/oracle/golden_week.json (numbers below are the reads in memory/08). Tool fed pre-boundary data only.
   E1: his structure is on my chart within 3 pips — 4H BoM supply ~101.33-101.44; 1H BoM demand ~100.65-100.74; IP bands ~101.19-101.29 and ~100.55-100.675; >= 90% of his liquidity rungs
       (101.25 101.24 101.20 101.19 101.14 101.115 101.09 101.00 100.975 100.94 100.905 100.845 100.77 100.68 100.61 100.545); EURUSD supply ~1.1446-1.1456, demand ~1.1400-1.1417.
   E2: the day map equals his tags on >= 4 of 5 days — Mon SS+BS, Tue SS, Wed SS+RWL+BS, Thu ladder short, Fri WL+RWL.
   E3: the tool emits his trades within 3 pips on entry, SL and TP, >= 5 of 6 — Mon L 100.945 / 100.905 / 101.115; Mon S 101.14 / 101.20 / 100.845; Tue L 100.845 / 100.77 / 101.19;
       Wed S 101.19 / 101.25 / 100.975; Wed L 100.975 / 100.905 / 101.24; Wed S 101.235 / 101.33 / 100.68 — plus a Thursday ladder short and a Friday WL + RWL pair;
       EURUSD Wednesday longs 1.1402 and 1.13935; <= 11 setups per pair; no setup breaking a law of section 5.
   Verified on opened Pinebox frames (1H, and 15m for entries); ledger rows written; commit recorded as the checkpoint.
S3 SAME CODE, FOUR WEEKS. The identical commit, only week / pair inputs changed, on >= 4 different weeks (anchor; Apr 20-24 2026 — E1 report + his two real trades
   L 98.02 / 97.87 / 98.77 and L 98.29 / 98.185 / 98.77; two more) across DXY / EURUSD / GBPUSD: E1, E2 and E3 each 80-90% by G1 counting; no week under 70; a drop like 90 -> 30 is a bug in my code to find.
S4 OUTSIDE AUDIT of the final code against canon: zero open deviations.
S5 BLIND TEST. Ship package (tool + run instructions + section 7) -> two fresh sub-agents, two weeks each that I have never rendered or inspected, each in its own Pinebox instance;
   they render, look, count by G1, report. Their numbers replicate S3. If not: debug, fix by canon, redo S3-S5.
S6 DEPLOYABLE. One command per week / pair -> one Pine (v6) that renders in Pinebox on top of the sealed V1: zones, shape chain, setups, toggles; trident_v8 colours and labels.

## 9. The loop (never leave the anchor week before S2 holds; never "improve" a passing step)
1. Take the next NOT BUILT or failing coverage row, in engine order.   2. Read its canon text in full.   3. Write / repair the function (citation in the docstring).
4. Write the expectation.   5. Generate the Pine, render in Pinebox, open the frame.   6. Compare with the oracle / the candles by G1; ledger row with deltas.
7. Delta -> trace to the canon step -> back to 2.   8. Commit + push; update memory/01, 05, 15; `tools/mem/mem rebuild`.
Before writing any code I can state: which coverage row, which canon lines, which law of section 5 it serves. If not, I read instead.

## 10. Context discipline
After every compaction: this file first, then memory/00's read order (10, 13, 11, 12 tail, 04, 01, 08, 09, 06, 05 tail, 07 tail) — all of it, including 08 and 09.
Persist every few steps: facts -> 08, rulings -> 04, decisions -> 03, lessons -> 06, frames -> 07, coverage -> 15, state -> 01, journal -> 05; rebuild OmniGraph; commit + push to AGENT.

## 11. Communication
No message to the operator except: an answer to a direct question (<= 5 lines); one checkpoint line with its frame when a success condition flips; one line for a blocker only he can remove.
No apologies, no explanations unless asked, no options, no advice, no numbers from my own scripts.
Before ending any turn: are S1-S6 all met? If not, the turn does not end — continue the loop. Does the message contain a question, an option list, a statistic of mine or a judgement of the strategy? Delete it.
