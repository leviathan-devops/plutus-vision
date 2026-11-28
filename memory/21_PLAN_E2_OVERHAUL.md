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
