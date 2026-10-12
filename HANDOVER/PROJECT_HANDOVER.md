# PLUTUS VISION — PROJECT HANDOVER (from DEEPSEEK_AGENT)

Written after absorbing the canon and running live-market exercises.
**Phase B (the indicator fix) is NOT started — awaiting explicit operator permission.**

---

## 1 · WHAT THE FINAL ARTIFACT MUST BE

**The Plutus Vision indicator** (currently labelled Trident) must **render E1 + E2 + E3 on the
chart, dynamically and in real time**, for any given trading week, on any DXY-basket instrument.

- E1 → where the institutional pressure zones are (**already renders ~95%**).
- E2 → what price action the week will take, as a shape chain.
- E3 → exactly which trade setups, and where.

**Temporal scoping law:** everything is scoped to the most recent bar. Under TradingView
bar-replay, rewinding to e.g. a Tuesday uses *all data up to that Tuesday* to render the forward
forecast for the rest of that week (Wed–Fri).

**Acceptance test (the operator's own):** across **12 randomly-picked DXY-basket trading weeks** —
rewind to Monday London open, render, play forward at 10× to Friday close, then compare the E2/E3
visuals against what actually happened. **≥95% (operator's bar; 90% stated as the floor elsewhere)
or there is work to do.**

---

## 2 · CURRENT STATE (measured on this branch)

| Component | State |
|---|---|
| E1 zone ladder rendering | **present** — bounds, categories, names, 6-shade fill/border ladders |
| E1 `calcZFP` | ❌ **WRONG QUANTITY** — degree-band instead of `(tp−bt)/ref` |
| E1 `zDeg` | ❌ caps at **5.0/14** (options/analyst/regime all 0) → extremes can never read HEAVY |
| E1 LSZ (6 green boxes) | ❌ absent (an authorized removal) |
| E1 option strikes (7 amber lines) | ❌ absent (no harvest fed) |
| E1 2×17 info table | ❌ absent from the render (data exists; the table does not paint) |
| **E2 shape chain** | ❌ **absent from the render** |
| **E3 trade setups** | ❌ **absent from the render** |
| Reference: `trident_v8.pine` (668 lines) | ✅ renders E1 + an E2 summary + E3 rows — the fidelity target |

Live Pine artifacts on the branch: `plutus-vision-v0.pine` (83 KB), `v1.pine` (76 KB),
`v2.pine` (109 KB), `plutus-vision-e1-automatic.pine` (41 KB).

---

## 3 · THE ONE DEFECT THAT MATTERS MOST

**E1's ZFP is the load-bearing number of the entire system.** It is the *only* E1 output E2
conditions on (the §6.4.1 transition table keys the next shape on the **target zone's ZFP**). So
an error there does not stay in E1 — it silently flips the E2 chain, and therefore every E3 setup.

- **Authority:** `calcZFP(tp,bt,pair) = round((tp−bt)/ref × 100)`, ref ∈ {DXY 1.60, EU 0.0200,
  GU 0.0200, AU 0.0150}. **Geometric: narrow zone → LOW ZFP → HARD WALL.**
- **Live build:** `zfp_from_degree(confluence)` — a *different quantity*.
- **Measured consequence:** v8's Ceiling (height 0.07, true ZFP **4%**) reads **LIGHT ≈ 50%** in
  the live build → E2 predicts **BS continuation** where the canon demands **RWL reversal**.
- **Why it hides:** the two quantities agree at the *extremes* in aggregate statistics and diverge
  per-zone; most zones look plausible, so the error surfaces only at the levels that decide trades.

**I verified this from first principles on real bars, not from a note.** Week 2026-05-04: price
sold off into a ZFP 0% level at `97.632`, printed a low of `97.625` — **0.7 pips through** — and
reversed. The defective reading would have predicted continuation through it.
See `EXERCISES/EXERCISE_LOG.md` §F1/F3.

---

## 4 · THE SECOND SYSTEMIC ISSUE (structural, not a bug)

**The system's correctness is a function of its INPUT DENSITY.** The 9 pillars exist to produce
*dense level clusters*; the zone-assembly algorithm assumes levels landing within 0.10–0.15 so
zones have real height and a meaningful ZFP distribution.

With an incomplete pillar stack (options / analyst / regime absent), the consequence is **not
fewer zones — it is wrong zones**: singletons masquerade as ZFP≈0 "hard walls", and nothing ever
reaches the >45% band where E2's breakout branch lives. This is the *same failure class* as
`zDeg` capping at 5/14, and it is why the live indicator's ceilings can never read HEAVY.

**The trap to avoid:** when you cannot source all pillars, the temptation is to **renormalize the
confluence score** so zones still reach "HEAVY" and the labels look right. That is what the live
build did, and it inverted E2. **The correct behaviour is to keep the absolute scale and let the
verdict be weaker** — never rescale a score until the labels match expectation.

---

## 5 · THE IMMUTABLE RULES (do not touch)

- **E1 and E2 as specified in v5.3.3 are live-market validated** (A+, ~95%) and are **frozen**.
  Do not change, re-derive, or "improve" them. Where the live build disagrees with the spec, the
  **spec wins**.
- **E3's authority is the CORRECTED engine** (`TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md`, 1685 lines).
  The E3 in the original v5.3.3 is broken (18 defects). Corrected E3 is **untested live** — it gets
  validated through the finished indicator.
- **R3 law:** E2 designates, E3 obeys. `E1 → E2 → E3`, each fitting inside the previous engine's
  architecture. Never debug E3 in isolation — trace upward to the earliest wrong engine.
- **Honest absence:** never fabricate a level. `SL_INVALID` / `TP_NULL` / `RRR_BELOW_FLOOR` ⇒ no
  emission. The 90% win rate depends on what the code refuses to emit.

---

## 6 · WHAT I WOULD DO IN PHASE B (proposal only — not started)

Ordered by leverage, each step gated on the one before:

1. **Restore the correct ZFP quantity** (`(tp−bt)/ref`) and prove it: recompute every zone on the
   v8's own reference week (Apr 6 – May 15 2026, `fixtures/bars/2026-04-20.json`) and require the
   Ceiling to read **4%**, matching v8, not 50%.
2. **Pin it with a test** that fails on the degree-band reading (the counterfactual already exists
   as a control in `EXERCISES/test_canon.py`).
3. **Re-verify E2's terminal shape** flips to RWL on that week — the falsifiable acceptance.
4. **Restore E2 rendering** (the chain string + confidence + alternative + day-by-day), fed by the
   existing E2 payload — the anti-fabrication path is to *render what the engine computes*, never
   to compute in Pine what E1/E2 already decided.
5. **Restore E3 rendering** (the trade rows: entries / SL / TP / RRR / day / session).
6. **Then** run the operator's 12-week blind-acceptance protocol.

**Guard for step 4/5:** the canon's own context-bloat finding — a second generation in the same
context degrades into lazy pattern-matching and fabricated numbers. Each week is a **fresh
pipeline run with zero carryover**.

---

## 7 · WHERE THE KNOWLEDGE LIVES (survives compaction)

| Need | File |
|---|---|
| macro chain / recovery entry point | `GRAPH/context_graph.md` ← **read first** |
| the four densities + the cycle | `CANON/00_FRACTAL_ARCHITECTURE.md` |
| E1: pillars, ZFP (crux), LSZ, BoM/MoM | `CANON/01_ENGINE1_ZONES.md` |
| E2: shapes, chains, the ZFP hinge | `CANON/02_ENGINE2_SHAPE_CHAIN.md` |
| E3: 12 phases, entry/SL/TP/RRR | `CANON/03_ENGINE3_TRADE_SETUPS.md` |
| entry precision / rockets (verbatim extract) | `CANON/05_TRADE_STRUCTURE_AND_ROCKETS.md` |
| DXY→pair conviction / report spec | `CANON/06_MULTIPAIR_AND_REPORT.md` |
| **what I proved on real bars** | `EXERCISES/EXERCISE_LOG.md` (+ 7 chart PNGs) |
| defects found & fixed | `FINDINGS/GATE_AND_ENV_DEFECTS.md` |
| typed graph (56 nodes / 64 edges) | `GRAPH/knowledge_graph.json` |
| conformance tests (17, green) | `EXERCISES/test_canon.py` |

**Reproduce everything:**
```bash
python3 GRAPH/build_graph.py && python3 GRAPH/verify.py     # graph
python3 -m pytest EXERCISES/test_canon.py -q                # 17 tests
python3 EXERCISES/lab.py --source pv-long --week 2026-05-04 --render
python3 EXERCISES/zfp_reaction_test.py                      # the reaction measurement
```

---

## 8 · OPEN QUESTIONS FOR THE OPERATOR

1. **`origin/main` is 424 commits behind** `handover`. Should `main` be brought forward, or is
   `handover` the real trunk?
2. **Is the corrected E3 the one to build against**, or does the older E3 spec retain any ruling
   the corrected version dropped? (The corrected doc says it preserved the 14 original
   zero-tolerance rules + added 2, but the original E3's `8R.8 VLM 10 patterns` is carried as a
   reference to "preserved verbatim" without the patterns being inline.)
3. **Options/analyst pillar sourcing** for E1 — the ZFP distribution cannot reach the >45% band
   without them, which is what the E2 breakout branch is conditioned on. Which pillars are
   actually sourceable going forward?

---

## SOURCE ANCHORS

Every anchor below was verified by printing the referenced line (never fabricated).

- `EXERCISES/EXERCISE_LOG.md:1` — what was proved on real bars
- `FINDINGS/GATE_AND_ENV_DEFECTS.md:1` — defects found and fixed
- `CANON/01_ENGINE1_ZONES.md:1` — the E1 contract
- `ENGINE1_V8_VS_MINE.md:108` — the measured statement of the crux defect
- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:3860` — the authority definition the fix must restore
