# DEEPSEEK_AGENT — WORKSPACE

**Agent:** DEEPSEEK_AGENT (one of 6+ concurrent split-test runs on the same mission).
**Isolation:** this directory is a dedicated `git worktree` on branch `deepseek_agent`
(remote: `origin/deepseek_agent`). The shared tree at `PLUTUS_VISION/` stays on `handover`
and is NOT touched by this run. Every commit from here lands only on `deepseek_agent`.

```
WORKSPACE ROOT : /home/leviathan/JARVIS_WORKSPACE/Shared_Workspace/PLUTUS_VISION/DEEPSEEK_AGENT/
BRANCH         : deepseek_agent   (worktree; parent tree untouched)
CANON SOURCE   : ../Original_Canon_Data/Toolset/   (read-only authority)
```

---

## 1 · MISSION (what the operator actually asked for)

**Phase A (THIS TASK — no permission needed):** absorb the canon. Read the fractal
architecture and the v5.3.3 prompt, become a subject-matter expert, then go onto a **live
chart** and prove the understanding by hand — identify E1 zones, the E2 shape chain, the E3
setups, and the pressure mechanics that generate them, on real price action.

**Phase B (NOT STARTED — explicit operator permission required):** fix the Plutus Vision
indicator so E1 + E2 + E3 all render dynamically on the chart, temporally scoped to the
most recent bar, correct under TradingView bar-replay, verified ≥95% across 12 randomly
picked DXY-basket trading weeks.

**Hard boundary:** E1 and E2 as specified in v5.3.3 are **confirmed live-market validated**
(A+, ~95%). They are **immutable**. Do not change, disagree with, or "improve" them. E3 in
the ORIGINAL v5.3.3 was broken; the fixed engine is the separate
`TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md`, which is as-yet untested live.

---

## 2 · THE THREE ENGINES (one sentence each)

| Engine | Question | Elemental density | Output |
|---|---|---|---|
| **E1** | WHERE ARE THE WALLS? | Earth (liquidity/IP) + Fire (S/D) | IP zone map: zones, pressure degree, **ZFP**, BoM/MoM, LSZs, POI tiers |
| **E2** | WHAT PATH WILL ENERGY TAKE? | Water (macro shapes) + Air (Fib) | Weekly shape chain: SS/BS/WL/R/… day-by-day, with triggers + confidences |
| **E3** | WHERE DO I SURF? | all four converging | TradeSetups: entry/SL/TP/RRR, day+session, anchored to an E1 zone ID + E2 shape day |

**The R3 Law (verbatim):** *E2 DESIGNATES, E3 OBEYS.* E3 never overrides E1/E2 and never
fabricates its own rules. `E1 → E2 → E3`, each builds on the previous; the next engine's data
MUST fit inside the previous engine's architecture. Non-negotiable.

---

## 3 · MACRO CONTEXT (why this project exists)

The operator built this toolset in ~30–48h with a free GLM 5.1 web agent in May 2026. E1+E2
are live-traded, confirmed ~95% accurate. A v8 Pine indicator (`trident_v8.pine`, 668 lines)
renders E1 at ~95% fidelity and ALSO carries an E2 chain summary + E3 trade rows in a 2×17
info table. Five months of agents on better models/harnesses have failed to advance it. This
run is a controlled split-test to find an agent that can actually execute.

**The known crux defect (already diagnosed, understood from first principles):**
ZFP is a **geometric** quantity — `zone_height / pair_weekly_reference × 100`
(DXY ref 1.60 · EU ref 0.0200 · GU ref 0.0200 · AU ref 0.0150). Narrow zone → LOW ZFP → HARD
WALL. The live build replaced it with `zfp_from_degree(confluence)` → a *different quantity* →
which **inverts E2's terminal shape** (a hard-wall Ceiling reads LIGHT/50% and predicts
continuation BS instead of the canonical reversal RWL). Canon §10.8 vs Appendix B.

---

## 4 · WORKSPACE MAP

```
AGENT_WORKSPACE.md                 this file — identity, mission, macro context
CANON/00_FRACTAL_ARCHITECTURE.md   the four elemental densities + the cycle (the foundation)
CANON/01_ENGINE1_ZONES.md          9 pillars → confluence 0-14 → pressure degree → ZFP; LSZ; BoM/MoM
CANON/02_ENGINE2_SHAPE_CHAIN.md    shape taxonomy, chains, ZFP-conditioned transitions
CANON/03_ENGINE3_TRADE_SETUPS.md   the CORRECTED E3 (12 phases, R3 law, entry/SL/TP/RRR)
CANON/04_PRESSURE_AND_LIQUIDITY.md supply/demand/liquidity mechanics + reaction lifecycle
CANON/05_TRADE_STRUCTURE_AND_ROCKETS.md  (desk-extracted) entry precision, rockets, reinforcement
CANON/06_MULTIPAIR_AND_REPORT.md   (desk-extracted) DXY→pair directional conviction, report spec
GRAPH/                             the knowledge graph + context graph (compaction recovery)
EXERCISES/                         live-market chart exercises + verdicts
FINDINGS/                          defects found outside the task scope (gates etc.)
```

**Recovery protocol after compaction:** read `GRAPH/context_graph.md` first (the macro
chain), then the specific `CANON/` file the task touches. `GRAPH/knowledge_graph.json` is the
typed node/edge store; `GRAPH/verify.py` validates it.

---

---

## SOURCE ANCHORS

Every anchor below was verified by printing the referenced line (never fabricated).

- `Original_Canon_Data/Toolset/Trident_Fractal_Architecture_FirstPrinciples_v2.3.md:47` — EARTH DENSITY — the foundation
- `Original_Canon_Data/Toolset/Trident_Fractal_Architecture_FirstPrinciples_v2.3.md:251` — the elemental cycle Earth→Fire→Water→Air→Earth
- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:566` — §2.0.3 The Elemental Density System
- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:3860` — §10.8 ZFP Calculation — Pair-Specific Reference Ranges
- `Original_Canon_Data/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md:76` — the R3 Law — E2 DESIGNATES, E3 OBEYS
- `ENGINE1_V8_VS_MINE.md:108` — the live ZFP defect — degree-band vs width formula
- `GRAPH/verify.py` is the validator; it fails on orphan nodes and dangling edges by design.
