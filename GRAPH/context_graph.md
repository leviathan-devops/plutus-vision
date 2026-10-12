# CONTEXT GRAPH — MACRO CHAIN (READ THIS FIRST AFTER COMPACTION)

The single document that restores *what we are doing and why*, in causal order. Then pick the
`CANON/` file the task touches. Machine-readable store: `GRAPH/knowledge_graph.json`
(56 nodes / 64 edges; regenerate with `GRAPH/build_graph.py`, validate with `GRAPH/verify.py`).

---

## 0 · IDENTITY / POSITION

I am **DEEPSEEK_AGENT**, one of 6+ concurrent split-test runs on the same mission. My workspace
is a `git worktree` at `PLUTUS_VISION/DEEPSEEK_AGENT` on branch **`deepseek_agent`**
(origin: github.com/leviathan-devops/plutus-vision). The parent tree stays on `handover`; I never
write outside my worktree.

---

## 1 · THE CHAIN (causal order)

```
[1] THE OPERATOR BUILT A TRADING INSTRUMENT (May 2026, free GLM 5.1 web agent, ~30-48h)
      |  E1 + E2 live-traded, ~95% accurate, IMMUTABLE.
      |  A v8 Pine indicator renders E1 at ~95% AND carries an E2 summary + E3 rows.
      v
[2] THE INSTRUMENT'S THEORY: price action IS the waveform of institutional energy flow.
      |  You do not create the wave -- you map it and surf it.
      |  4 elemental densities: EARTH (liquidity) -> FIRE (S/D) -> WATER (shapes) -> AIR (Fib)
      v
[3] E1 ANSWERS "WHERE ARE THE WALLS"
      |  9 pillars x 6 dimensions -> confluence 0-14 -> pressure degree.
      |  ZONE CONSTRUCTION: the SINGLE candle before a strong move (not a cluster).
      |  Every zone: BoM/MoM + reaction count (0/1-2/3+) + mitigation + POI tier.
      |  *** ZFP = zone_height / pair_ref_range x 100  (GEOMETRIC: narrow = HARD WALL) ***
      v
[4] E2 ANSWERS "WHAT PATH WILL ENERGY TAKE"
      |  Classifies the week into macro SHAPES: SS BS WL RWL R WLS PBS PRWL DWL RS PWL.
      |  Chains them from historical frequency (SS->BS->R->WL is HIGHEST).
      |  *** THE HINGE: the NEXT shape is keyed on the TARGET ZONE'S ZFP, not on momentum ***
      |      BS + target ZFP<20% (hard wall)  => RWL  (REVERSAL)   <-- the #1 historical error
      |      BS + target ZFP 20-40%          => R
      |      BS + target ZFP>60%             => PBS  (cascade)
      v
[5] E3 ANSWERS "WHERE DO I SURF"
      |  ORIGINAL v5.3.3 E3 was BROKEN (18 defects). The CORRECTED engine is the authority.
      |  R3 LAW: E2 DESIGNATES, E3 OBEYS -- every anchor traces to an E1 zone id + E2 shape day.
      |  Sniper entry (edge closest to price) -> ladder-steps SL -> ONE regime-conditional TP.
      |  RRR floor 3.0 IRON LAW, enforced in CODE. 3-attempt refine (entry FIXED, SL/TP move).
      |  HONEST ABSENCE: refuse rather than fabricate. The 90% win rate = what the code REFUSES.
      v
[6] THE DELIVERABLE (Phase B -- NOT YET AUTHORIZED)
      |  Make the Plutus Vision indicator render E1 + E2 + E3 dynamically, temporally scoped
      |  to the most recent bar, correct under bar-replay, verified >=95% across 12 random
      |  DXY-basket weeks.
      v
[7] THE KNOWN BLOCKER (already diagnosed, understood from first principles)
         The live build computes ZFP as `zfp_from_degree(confluence)` -- A DIFFERENT QUANTITY.
         Consequence measured: the Ceiling (width 0.07, true ZFP 4% = hard wall) reads
         LIGHT/50% in the live build => E2 predicts BS CONTINUATION instead of RWL REVERSAL.
         A wrong number in E1 does not stay in E1 -- it silently flips the whole chain.
```

**Where we are right now:** step [1]–[5] absorbed; step [6] is the target; step [7] is the
diagnosis that Phase B must fix first. Phase B is **gated on explicit operator permission.**

---

## 2 · THE RULE THAT BINDS EVERYTHING

> **E1 → E2 → E3 each one BUILDS ON TOP of the previous. Previous engine data PROVIDES THE
> STRUCTURE for the next one. Next engine's data MUST FIT WITHIN THE CONSTRAINTS of the previous
> engine's data architecture. Absolutely non-negotiable.**

Practical consequence for any future work: **you cannot debug E3 in isolation.** An E3 defect may
be an E2 misdesignation, which may be an E1 misclassification, which may be a wrong ZFP. Always
trace upward to the earliest engine that is wrong.

---

## 3 · THE FIVE FACTS MOST LIKELY TO BE FORGOTTEN (and most costly)

1. **ZFP is GEOMETRIC** — `zone_height / ref` (DXY 1.60 · EU 0.0200 · GU 0.0200 · AU 0.0150).
   Narrow = hard wall. There is a *second* failure-probability quantity (Appendix B, by zone
   TYPE); they agree at the extremes and diverge in the middle — which is exactly why swapping
   them passes most zones and inverts the extremes.
2. **The next shape is chosen by the TARGET ZONE'S ZFP, not by current momentum.** Hard wall
   (ZFP<20%) after a BS ⇒ **RWL**, never continuation.
3. **IP zones are NEVER entries.** Only `ORDER_BLOCK` and `LQZ` are valid entry anchors. IP zones
   are confluence/ZFP/context + SL/TP rungs.
4. **MoM is ladder-step/TP only.** No reversal entries at MoM, EVER. Virgin MoM = death zone.
5. **RRR floor 3.0 is enforced in CODE, and HONEST REFUSAL is the product.** A setup that cannot
   clear the floor after 3 refinement attempts HARD REJECTS. The 90% win rate depends on what the
   code refuses to emit — never synthesize a level to make a setup pass.

---

## 4 · THE FILE MAP

| Need | File |
|---|---|
| the four densities, the cycle, the conservation laws, Mom law, decision tree | `CANON/00_FRACTAL_ARCHITECTURE.md` |
| pillars, confluence, pressure degree, **ZFP**, LSZ, BoM/MoM, POI tiers, the live defect | `CANON/01_ENGINE1_ZONES.md` |
| shape taxonomy, chains, transitions, **ZFP-conditioned hinge**, day decomposition | `CANON/02_ENGINE2_SHAPE_CHAIN.md` |
| 12 phases, R3 law, sniper entry, ladder SL, single TP, RRR + refine, reinforcement, cascade | `CANON/03_ENGINE3_TRADE_SETUPS.md` |
| entry precision / rockets / ladder (extracted verbatim + checklist) | `CANON/05_TRADE_STRUCTURE_AND_ROCKETS.md` |
| DXY→pair directional conviction, report spec, forbidden list | `CANON/06_MULTIPAIR_AND_REPORT.md` |
| hand-verification on live bars | `EXERCISES/` |
| defects found outside task scope | `FINDINGS/` |

---

## 5 · STANDING ORDERS (operator-mandated)

- **E1 and E2 are immutable.** Do not change, "improve", or disagree with them. They are
  live-market validated.
- **Do not start Phase B** (the indicator fix) without explicit permission.
- **Never report a problem instead of solving it.** Obstacles are mine to resolve.
- **Never fabricate.** Refusal is a valid, correct output. A plausible number is worse than an
  honest absence.
- Context bloat causes lazy derailment (the A+ vs D-grade forensic). Re-read the relevant canon
  per task; treat every analysis as a fresh generation with zero carryover.

---

---

## SOURCE ANCHORS

Every anchor below was verified by printing the referenced line (never fabricated).

- `GRAPH/knowledge_graph.json:1` — the machine-readable store this file summarises
- `CANON/01_ENGINE1_ZONES.md:1` — E1 canon
- `CANON/02_ENGINE2_SHAPE_CHAIN.md:1` — E2 canon
- `CANON/03_ENGINE3_TRADE_SETUPS.md:1` — E3 canon
