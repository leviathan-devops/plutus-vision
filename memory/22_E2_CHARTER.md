# 22 - ENGINE 2 OVERHAUL CHARTER (M-78, 2026-11-28) - APPROVED BY THE OPERATOR (M-79: 'Good. Persist this exact plan to disk. Make sure you don't derail from this. Persist all durable facts and begin. Complete the full objective as you laid it out here.'). THE GOVERNING PLAN - obey it verbatim; no deviation. READ BEFORE EVERY STEP. Plan detail: memory/21 (v5). Gap data: memory/18. His context document: canon/operator_uploads_2026-11-28/.

## GOAL
Engine 2's forward line shows what price will do before it happens: zone to zone, shape by shape, every turn at the right Engine 1 zone at the right time. Measured with time-aligned, mechanics-based grading it reaches 80-85%,
replicated on multiple weeks and all three pairs (DXY, EURUSD, GBPUSD); then reassess. Drawn as an orange solid line inside hollow white shape frames. Downstream purpose (not this phase): Engine 3 on top of it wins >= 80% without fewer trades.

## IMMUTABLE CONSTRAINTS
C1 Engine 1: zero regressions - no Engine 1 file edited (tools/locks SHA-256), Engine 1 output byte-identical on every cached pair-week.
C2 Temporal anchor: nothing after an anchor instant feeds anything drawn from it (Monday London open; each day's open and London open; the fixed update times). COT counts from its PUBLICATION time, not its report date.
C3 No hardcoded values: no price literal, no per-week constant; the same code for any week and pair.
C4 This phase changes the Engine 2 LINE (and, with the lifted lock, the shape classifier + the three-week context). Engine 3 orders, the golden-week trades, zones and the once-a-day cycle stay identical.
C5 Stability: the indicator changes only at fixed times - 17:00 / 02:00 / 05:00 / 10:00 New York, never more than 6 a day; what is already drawn never changes.
C6 Simple architecture: no market-triggered updates, no scalping engine (both benched, design/).
C7 Pine cannot fetch; Pinebox is the test environment; frames are opened.
C8 Load-bearing parts not named in C4 are not deleted, recreated or re-ordered.
C9 11 swing setups per pair-week; canon vocabulary (swing scalps, never 'range day').

## RULES
R1 Do exactly what he says, inside his constraints; no ideas of my own. Every rule in code cites its source (canon file:line, ruling id, or his documents). His Gemini document is context, not authority; build from first principles; this session's infrastructure governs.
R2 One step at a time. Each step behind a switch (default off). After each step: report with before / after grades and frames, negatives included. Adoption only on his word.
R3 Grade with the time-aligned grader; when a step restarts the line, show the no-forecast line at the same times next to it.
R4 Every step: Engine 1 lock + byte-identity, kill test, leak check at every anchor / update instant, golden orders identical, crash sweep over all cached pair-weeks.
R5 All three pairs, the whole trading week in one fitted frame each.
R6 Memory + journal updated, committed and pushed to AGENT after every step.
R7 'Blueprint' = the design-blueprint skill.

## FORBIDDEN
F1 Editing Engine 1, the sealed V1, SHIP_PACKAGES / plutus-browser trees.  F2 A line that follows price (EMA-style), restarts outside the fixed times, or repaints.
F3 Hardcoding, tuning to a week, caps / filters that hide bad output, fewer trades for a higher rate.  F4 Any post-anchor data; oracle numbers inside tool code.
F5 My own number presented as a verdict; blaming the strategy or circumstances.  F6 Scope changes; building benched items; raising the swing-scalp screenshots; copying Gemini's work.
F7 Paid data; working around Forex Factory.  F8 Sub-agents doing the build (outside review only).  F9 Pull requests, other branches, commits of secrets.

## PLAN (memory/21 v5): 1 grader + kill test + baseline -> 2 the orange / white look -> 3 data module (new file) -> 4 prior-week terminal state -> 5 day-level classifier -> 6 boundary states (5) -> 7 path nodes + telescoping -> 8 fixed-time updates -> 9 pairs.
PROCESS PER STEP: read the governing source text in full -> write the ledger expectation -> code behind a switch -> R4 gates -> grader before / after (golden + 4 checkpoint weeks) -> Pinebox frames side by side, opened -> report -> his verdict -> adopt or revert.

## TESTS
T1 Engine 1 lock clean + Engine 1 output byte-identical (all cached pair-weeks).  T2 Kill test: +500 pips on every bar at / after the anchor -> generated output byte-identical; leak check with the store cut at every anchor / update instant.
T3 Golden-week orders identical (entry / stop / TP lists, 3 pairs).  T4 Time-aligned grader, before vs after, same weeks.  T5 Crash sweep: every cached pair-week runs.
T6 Frames: previous vs new, 3 pairs, opened.  T7 Weeks: golden + Apr 13 / Apr 20 / May 18 / Oct 5 while building; 4 fresh weeks to confirm; held-out weeks once at the end.

## SUCCESS CONDITIONS
S-a Grader (proposed definition, his to confirm): of the turns Engine 2 forecasts, >= 80% happen at the named Engine 1 zone within +-2 hours; of the turns price actually makes, the share that was forecast is reported beside it; day shapes right >= 80%; weekly direction right; hourly correlation reported.
S-b The same on the checkpoint weeks AND fresh weeks, each pair, no week collapsing (no 85-vs-15 gaps).  S-c T1, T2, T3, T5 pass at every step.  S-d At most 4 line updates a day; nothing repaints.  S-e His verdict on the frames.

## ORACLES
O1 The candles after each anchor (TradingView bar store, 30m / 1H): where and when price actually turned.
O2 The golden week Jul 6-10 2026: his shape tags (Mon SS+BS, Tue SS, Wed SS+RWL+BS, Thu ladder short, Fri WL+RWL) and his trades (context_management/oracle/golden_week.json).
O3 The winning trade library: his shape frames and trades on ~17 pair-weeks (context_management/oracle/library/trades.json) - shape sequences and the look.
O4 His eye on the frames - final.   Control (not an oracle): the no-forecast line at the same update times.
Rule sources: P533 / P452, Fractal Architecture, Golden Standard reference, corrected E3 spec, his SMC notes, his telescoping document.

## DATA IN THE ENVIRONMENT (fetched 2026-11-28, data/tvapi/, 30 series via tools/tvapi/fetch.mjs)
Futures CME:6E1! / CME:6B1! / ICEUS:DX1! with exchange volume: 15m from 2026-09-14, 30m from 2026-06-11, 1H from 2026-01, 4H + D from 2025-02. 2Y yields US / DE / GB: 1H + D from 2025-02. COT (noncommercial long / short, open interest) euro / pound / dollar index: weekly from 2025-02.
Spot candles with tick volume: the Pinebox bar store (unchanged). Limits: intraday futures older than the dates above need the library's replay mode or the 1H series; 'delta' is a proxy built from candle volume, not true order flow.
