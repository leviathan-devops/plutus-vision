# 21 - ENGINE 2 OVERHAUL PLAN v4 (M-76 / L-70, 2026-11-28) - his 7-pillar architecture mapped onto this codebase. PLAN ONLY, sent in chat, waiting for his answers. Supersedes the component list of memory/19 v3.1 where they overlap.
Source: canon/operator_uploads_2026-11-28/ENGINE_2_MICRO_INFRASTRUCTURE_OVERHAUL_CONTEXT_INJECTION.md (read in full before coding any pillar).

## Pillar -> what is coded today -> gap
| Pillar | Coded today | Gap |
|---|---|---|
| A classifier | e2_chain.current_shape: 6.2 matrix rows with ZFP conditions, fallback 'no row matched -> SS'; reaction counter; FA 9 two piercing sessions -> SS (= an energy lock) | no Efficiency Ratio, no retrace / extension bands; the fallback is the deadband (9 of 12 non-golden chains = swing scalps all week) |
| B 5-state boundary machine | e2_chain.branch at the two day-box bounds only: HOLD / FAIL / PIERCED / SLOW / BREAK-RETURN | no wick vs body vs consolidation vs rim-pierce vs clean-break state at each zone the line reaches; nothing passed to Engine 3 about entry depth |
| C 3-week context | last 6 sessions before the anchor; render window = active week + one week left (R-36) | no W-1 Friday terminal state object (shape in progress, touch counts, lock, freshness ledger); no realized shapes on W-2 / W-1 |
| D drawing | yellow solid line, dashed coloured day boxes, dotted alternative line | orange #E85D04 2px solid, hollow white frames, zero dashed / dotted |
| E precision | vertices at zone edges, times from the session clock | no quantizing on intersections (S/D x liquidity edge x option wall x MA), no timing modes, no PathNode metadata |
| F data | P11 partial (10:00 cut, auctions, EIA); bar store carries per-bar tick VOLUME for the 3 spot symbols | P10: no futures (6E / 6B / DX), no delta; P12: no 2Y yields, no COT (sidecar has H.10 FX rates only); fixes (ECB 13:15 UTC, London 16:00) not in the clock |
| G pairs | Engine 2: DXY chain as lead + the pair's own zones; Engine 3 Phase 10 mirrors DXY -> EU -> GU | GBPUSD still derived through EURUSD in Engine 3; no explicit coordinate-free DXY compass object |
| Invariants | leak check = bar store cut at each anchor; SL-first replay; Pinebox frames | +500-pip shock kill test not built; time-aligned grader (+-2h, hourly Pearson r, weekly sign) not built |

## Proposed order (nothing starts before his answers)
0. Verification instruments of his section 3 (shock kill test, time-aligned grader, replay frames) + baseline of the current product with them. Tools only.
1. Design blueprint of the overhaul on this codebase (design-blueprint skill) for his approval.
2. Pillar F data layer as a NEW module beside the locked Engine 1 (no Engine 1 file edited).
3. Pillar C -> Pillar A (the day-level forecast) -> Pillar B (boundary states) -> Pillar E (PathNodes) -> Pillar D (drawing) -> Pillar G; each behind a switch, graded with step 0, golden + checkpoint weeks + blind weeks, frames opened.

## Questions sent to him
Q1 code / spec from the Gemini build available? Q2 locks: Engine 1 locked + macro architecture frozen (M-67) vs Pillars A / C / F. Q3 timing model: sealed pre-Monday (00:00 UTC) week forecast vs Monday London-open anchor + daily London-open update + the fixed intraday times. Q4 data: spot tick volume as first proxy vs a futures feed; sources for 2Y yields / COT. Q5 drawing change replaces the trident_v8 look? alternative line? Q6 grading: his time-aligned grading replaces my 10-pip figure; how the 80-85% is measured. Q7 clock typos (London Open 08:00 UTC, NY Open 08:30 UTC). Q8 Pillar G applies to Engine 3's Phase 10 too?

## v5 (2026-11-28, after M-77 / L-71) - THE EXECUTION PLAN sent in chat (waiting for his go). This session's infrastructure governs; his document is context.
Gates on EVERY step: behind a switch (default off) | Engine 1 lock clean AND Engine 1 output byte-identical on every cached pair-week (zero regressions) | shock kill test + leak check | golden orders identical | graded with step 1 before / after | frames opened | reported; adopted only on his word.
1. GRADER + KILL TEST (tools only). Time-aligned, mechanics-based: each forecast vertex = (Engine 1 zone, time, kind) -> an actual turning point of that kind at that zone within +-2h? (hit / wrong zone / none); each actual turn -> forecast?; hourly correlation line vs hourly closes; weekly net direction; day shapes right. Kill test: +500 pips on every bar at / after the anchor -> output byte-identical. Baseline of the product on golden + 4 checkpoint weeks.
2. LOOK: orange #E85D04 2px solid line, hollow white frames per shape, no dashed / dotted; the alternative chain stays in the text report, not drawn. Side-by-side frames, 3 pairs; orders identical.
3. DATA MODULE (new file; Engine 1 untouched): volume profile (high- / low-volume areas at each zone) + delta proxy from the bar store's tick volume, futures volume (CME:6E1! / 6B1! / ICEUS:DX1!) and 2Y differentials through tools/tvapi; institutional clocks in local time (London 08:00, New York 08:30, cut 10:00 NY, ECB reference 14:15 Frankfurt, London fix 16:00). Everything cut at the anchor.
4. PRIOR-WEEK TERMINAL STATE (pillar C): Friday-close shape in progress, touches per zone, two-pierce recovery lock, zone freshness -> the chain continues from it; realized shape frames on the visible prior week (R-36 window kept).
5. DAY-LEVEL CLASSIFIER (pillar A): continuous classification on Engine 1 strength + causal bar geometry; no fall-through to swing scalps.
6. BOUNDARY STATES (pillar B): at every zone the line reaches, one of five states (wick reverse / body whiplash / consolidation into recovery / rim pierce + reclaim / clean break) from the zone's Engine 1 properties + step-3 data -> where the vertex sits in the zone, how long price stays, which way it leaves.
7. PATH NODES (pillar E + telescoping): the line built from nodes on zone intersections, each with zone id, state, timing mode; week -> day -> session containment.
8. FIXED-TIME UPDATES (17:00 / 02:00 / 05:00 / 10:00 NY), line only: steps 6-7 re-run from the actual price. (Simple architecture; market triggers stay benched.)
9. PAIRS (pillar G, common sense): DXY gives direction, shapes, clocks; each pair its own zones and data; Engine 3's mirroring left as is unless the grader shows it hurts (golden trades protected).
Later, his call: Engine 3 reads the boundary states (entry depth, stop side, blocked reversals); scalping engine; live triggers.
