# PLUTUS VISION GOAL (short form; full text memory/14_GOAL_PROMPT.md stays binding)

GOAL: translate the operator's working trading process, exactly as written in his canon, into ONE Python program that for a trading week + pair outputs ONE Pine v6 script
(trident_v8 form, on top of the sealed V1) with accurate Engine 1 zones, an accurate Engine 2 shape chain and accurate Engine 3 trade setups, proven on Pinebox pixels. Nothing else.

SCOPE (frozen): E1 (liquidity + institutional pressure + supply/demand), E2 (shape chain), E3 (setups incl. reinforcement); DXY / EURUSD / GBPUSD; any week; only data before the Monday
London-open anchor. No redesigns, no own rules / filters / thresholds, no research programmes, no statistics about whether the strategy works, no reports instead of code, no questions.

PREMISE (not open to test): the strategy works. A bad result is always my build: a canon step not built, built differently from its text, wrong / missing data, or a render fault.

SOURCES in order of authority, read first-hand before coding the part they govern: (1) operator rulings memory/04, memory/12, R-01..R-39; (2) E1 + E2 = v5.3.3 prompt Parts III-VI
(+ v4.5.2 text); E3 = TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md only; (3) Fractal Architecture v2.3, TTE Golden Standard reference (7 laws), Fibonacci Spiderwebs, his SMC notes;
(4) oracles (golden week Jul 6-10 2026, weekly reports); (5) existing code. My own judgement is not a source.

METHOD: one function per canon step with file:line in the docstring; coverage matrix memory/15; no price literal in Python; nothing after the anchor feeds the map; canon silent ->
plainest literal reading + one line in memory/03.

ANTI-PATTERNS (each already cost this project): scope drift; own ideas (no code without a canon citation or ruling id); judging a partial build as the whole; blaming the strategy
("does not work / no edge / at chance"); home-made scorers as verdicts; self-grading; working from summaries; stopping / asking / reporting instead of building; skipped layers;
wrong timeframe; caps or filters that hide bad output; tuning to a week; render slop; sub-agents doing my work (they are outside auditors and blind testers only);
temporal leak / hardcoding; touching the sealed V1, SHIP_PACKAGES or plutus-browser; context loss; theatre.

GRADING (only two ways): G1 Pinebox pixels - write the expectation in memory/07 BEFORE rendering, render, OPEN the frame, one verdict per drawing; G2 outside fresh-context audit
of code vs canon. Pixels outrank the auditor; my opinion outranks nothing. Counting for S3 / S5 is done by outside sub-agents.

SUCCESS = all six: S1 every coverage row built + audited. S2 golden week Jul 6-10 2026 DXY + EURUSD: his zones within 3 pips, day tags >= 4 of 5, his trades within 3 pips on entry /
SL / TP (>= 5 of 6 + Thursday ladder short + Friday WL), EURUSD Wednesday longs 1.1402 and 1.13935, <= 11 setups, verified on opened frames. S3 the identical commit on >= 4 weeks
(golden, Apr 20-24, two more) x DXY / EURUSD / GBPUSD: each engine 80-90%, none under 70. S4 outside audit: zero open deviations. S5 ship package -> two fresh sub-agents x two unseen
weeks each replicate S3. S6 one command -> one Pine v6 with toggles.

LOOP: next failing coverage row -> read its canon text -> write / repair the function -> expectation row -> render -> open the frame -> ledger -> trace deltas to their canon step ->
commit + push to AGENT; update memory. Never "improve" a passing step; after every change re-check the golden week and the weeks already passed.

CONTEXT: after every compaction read memory/14 in full, then memory/00's read order; persist state every few steps.

COMMUNICATION: no message to the operator except an answer to a direct question (<= 5 lines), one checkpoint line with its frame when a success condition flips, or one line for a
blocker only he can remove. No apologies, options, advice or numbers from my own scripts. The turn does not end until S1-S6 hold.
