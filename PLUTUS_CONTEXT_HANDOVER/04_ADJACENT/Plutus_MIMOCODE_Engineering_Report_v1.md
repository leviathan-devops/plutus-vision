# PLUTUS Plutus_MIMOCODE — ENGINEERING REPORT v1
**Series:** Plutus_MIMOCODE (the MiMoCode 5.0 port lineage; no parent series)
**Project:** Plutus 5.0 MiMoCode port
**Date:** 2026-09-14
**Author:** primary agent (ses_-ffe5f73f384beffeg7537uiYT)
**Baseline:** fork-spec §1 @ MIMOCODE/Plutus (pre-fork: src absent)
**Commit:** n/a (no git in this lane)
**Container:** n/a · **Image:** n/a (container path blocked — image absent)

## ONE-PARAGRAPH SUMMARY

This report records the design-complete, build-pending state of the Plutus 5.0
MiMoCode port: a 2,726-line spec/bible/plan corpus (361L architecture spec with
§1 preserved-verbatim fork verdict + §2 exec-seam/SUPER_GOAL binding + §3
browser layer; 1,088L pure MathExpr cards bible with E1–E10 meta + MPSE Circuit
research + circuit→kernel→report flow; 500L RuleCard law bible; three ShowMes:
FULL build plan v2, MPSE Circuit blueprint, E-Wave) standing over a measured
source tree (specs/mpse 46/46 fp 8acfe74f… d17 19C/27E; kernel 2,962L with
RRR_FLOOR 2.5 and CASCADE_NO_INVERSE; frozen SHAs byte-verified; TV_Browser_v3
1,405L 38 tools) and a six-wave build plan (W-FORK → W-ENGINES → W-KERNEL ∥
W-HARNESS → W-MPSE → W-CONVERGE) whose terminal gate is full-week 23/23 ±3p
with determinism ×2. No source has been forked yet; every claim below carries
its measurement.

## THE LIFECYCLE MAP

```
┌──────────────────────────────────────────────────────┐
│ FORK (copy+verify) → ENGINES (fix+authority) →       │
│ KERNEL ∥ HARNESS (nodes+proof · agent+goal+browser) →│
│ MPSE (spine+46/46) → CONVERGE (23±3p · ×2 · live)    │
└──────────────────────────────────────────────────────┘
```

## THE ARCHITECTURE (per module)

Per-module law lives in handover App H1–H7 (E1/E2/Card/Kernel/MPSE/upload).
Interfaces: ZoneMap+verdicts (E1) · zone-ID designations (E2) · PlutusCard
(card) · TradeProjection+provenance (kernel) · battery/d17 (substrate).
Failure modes: fail-closed oracles; BLOCKED/WARN/REFINEMENT_EXHAUSTED step
vocabulary; CAP-UNBOUND pre-fire; worst-wins rollup.
Calibration constants: fp 8acfe74f… · tol 3 ("only metric") · RRR 2.5/D-R1 ·
SL 36/4 · f(T)=24 · SL-lmv 91294083… · dedup 33914c89….

## THE BUG LEDGER

The 22-row ledger is handover App I (theatrical M1–M7/X2 + murder-chain 8–14 +
JESL traps 15–17 + defect lessons 18–19 + retracted wave-1 claims 20–22).
Significant: M1 tolerance split (fix: single card, conflict throws); M2
week→Monday (fix: full-window pinned in goal); murder-chain Ea–Ee (fix: one
commit each, oracle-gated); mpse:calibrate cap trap (fix: requiredCaps []).

## THE TESTING LEDGER

| test | scope | how | result |
|---|---|---|---|
| mpse compile | 46 blocks | bun compile.ts | fp 8acfe74f… |
| mpse calibrate | 46 predicates | bun calibrate.ts | exit 0, 19C/27E |
| frozen pair | 2 files | sha256sum | prefixes match |
| report ×2 | 1 artifact | two runs | f8235815 identical |
| full-week | 19 trades | evidence tail | 11W/8L/0O 58% |
| e1 battery | 6 machines | 15,000 assertions | carried green |
| e2/kernel tests | 15 files | bun test | carried green |
| host display/chrome | env | socket/binary ls | alive/present |
| container image | image | docker images | ABSENT (blocker) |

## THE SPEC MANDATE → ENGINEERING MAP

R1 theatrical→re-anchor · R2 D13→compile gate · R3 fork-only→manifest ·
R4 workflows+goal→T1 table · R5 /plutus-pipeline→SUPER_GOAL mapping ·
R6 memory dup→4-file set+hooks · R7 LASME-FIRST→E1/E2/E3 wiring order ·
R8 exec seam→plutus-engine tool · R9 MPSE Circuit→5 nodes+bible §12B ·
R11 zero-dep→all scans green · R13 E-wave order→M1–M7 plan ·
R15 anti-theatrical→goal-embedded gates. (R10 ship-path, R12 honest-data,
R14 show-me: process mandates, evidenced by this pack.)

## THE NUMBERS

spec 361 · bible-2 1088 · bible-1 500 · plans 239+213+195+130 · handover 938+ ·
substrate: compile 270, calibrate 711, registry 394, S-corpus 437, mutants 9,
kernel 2,962, e1 29f, e2 28f, card 7f · JESL core 10/nodes 40/profiles 5 ·
failures-DB 20,322 · MASTER_CONTEXT 77 files · graph nodes 1940/edges 3647.

## THE FILE MANIFEST

```
┌──────────────────────────────────────────────┐
│ PLUTUS/  (this home, migrated diff-r clean) │
├──────────────────────────────────────────────┤
│ ├─ PLUTUS_5.0_MIMOCODE_ARCHITECTURE_SPEC.md  │
│ ├─ PLUTUS_CONTEXT_HANDOVER.md  938L+         │
│ ├─ MASTER_CONTEXT/ (2 bibles)                │
│ ├─ reports/ (4 ShowMes + this report, v1)    │
│ └─ (src/ arrives at W-FORK — absent today)   │
└──────────────────────────────────────────────┘
```

Provenance: all EXISTING (migrated byte-identical) except this report (NEW)
and the handover (NEW).

## WHAT'S NEEDED FROM THE OPERATOR

1. GO on the W-FORK→W-HARNESS DPL1 (the standing "say go" item).
2. Rulings on the 5 open questions (handover §14): old-bible §2 fold;
   S-5 2.5-vs-3.0 authority; Vibe DROP-or-start; bible density; Tier-D SLs.
3. P0 blocker: import plutus-container-testing:master + create the
   plutus-browser volume (unblocks the container browser path).
4. Confirm SUPERSEDED_NOTES.md authorship (recommended content staged in
   checkpoint §5 item 5) or point at handover App F instead.
