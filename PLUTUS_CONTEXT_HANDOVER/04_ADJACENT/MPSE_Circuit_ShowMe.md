# MPSE Circuit — ShowMe (BLUEPRINT spine) v1

SPINE: BLUEPRINT — the MPSE Circuit (embedded logic system on the JESL card)
needs designing before anyone commits. Evidence: the chip-mask doctrine
(JESL_MASTER_KERNEL_SPEC_v3.md, 313L, read 100% by the wave), the execution
layer (executor/caps/channels/registry/jesl-run, 1,198L read full), the
embedding surface (workflow-machine.ts 139L read full), the existing precedent
node (mpse-discharge.ts), and the pure substrate (specs/mpse, 2,941L measured,
battery 46/46 fp 8acfe74f…). Bible §12B is the research record.

## 1 Master view — the macro circuit embeds the micro circuit

```
┌────────────────────────────────────────────────────┐
│ JESL KERNEL CARD — tier 2, the macro circuit       │
│ seed → prompt(bracket) → merge → schema-gate →     │
│ journal-sink                                        │
│ (Aether intelligence: agent NodeImpl blocks        │
│  behind pin contracts — v3:76, fusion :73)         │
└────────────────────────────────────────────────────┘
   │
   │  config.doc  (one workflow-machine node,
   │  caps inherit one-way, depth ≤ 3)
   ▼
┌────────────────────────────────────────────────────┐
│ EMBEDDED MPSE CIRCUIT — tier 1, the micro die      │
│ load → mpse-quantize → mpse-compute                │
│ → mpse-oracle → journal-sink                       │
│ (MathExpr law gates: oracle NodeImpl blocks        │
│  behind pin contracts — the SAME mechanism,        │
│  one level down)                                   │
└────────────────────────────────────────────────────┘
   both levels: one electricity (Effect substrate) · one
   clock (runProgram) · one journal (the sha256 chain —
   micro rows land namespaced parent:wf:node:depth)
```

The doctrine it implements (operator, verbatim, v3:54): "the effect program
structure is electricity, the aether machine is intelligence nodes — design the
circuit board." The compression law (this blueprint's thesis): the Aether
machine is embedded AGENTS at the macro level; MPSE is embedded LAW at the
micro level — and the separation law holds at both (v3:77): the die never
contains a model; no gate compares a float without tolerance.

## 2 Core mechanism — one micro-gate's lifecycle (mpse-gate)

```
┌──────────────────────────────────────────────┐
│ mpse-gate fires (executor hands it inbound)  │
│   inbound arrives via named channel         │
│   parse cfg {expr, expected, tolerance,     │
│     oracleKey, provenance}                  │
│   quantize — integer buckets ONLY           │
│   computeExprLocal (the 28-tag ALU)         │
│   discharge vs expected                     │
│     FAIL carries the delta                  │
│     SILENT is the pass state                │
│   Triplet {pattern, state, anchor} emitted  │
│   verdict row lands in the PARENT chain     │
│   Effect.exit wraps — siblings unaffected   │
└──────────────────────────────────────────────┘
```

## 3 Component/file tree — the shape of the build

```
┌──────────────────────────────────────────────┐
│ MIMOCODE/JESL/jesl/ (the extension surface) │
├──────────────────────────────────────────────┤
│ ├─ nodes/mpse-gate.ts      NEW assert gate   │
│ ├─ nodes/mpse-compute.ts   NEW MathExpr ALU  │
│ ├─ nodes/mpse-oracle.ts    NEW discharge     │
│ ├─ nodes/mpse-quantize.ts  NEW pip-quantizer │
│ ├─ nodes/mpse-mux.ts       NEW oracle select │
│ ├─ core/registry.ts        +5 ALL_KINDS rows │
│ ├─ nodes/index.ts          wiring authority  │
│ ├─ profiles/mpse.ts        NEW tier-1 module │
│ └─ nodes/mpse-discharge.ts PRECEDENT (149)   │
└──────────────────────────────────────────────┘
```

## 4 Interfaces table (contracts the implementation must honor)

| Export | Type | Contract | Anchor |
|---|---|---|---|
| mpseGateNode | NodeImpl | cfg {expr, expected, tolerance, oracleKey, provenance} → verdict FAIL(delta)/SILENT; requiredCaps: [] | mpse-discharge.ts:70-147 template |
| mpseComputeNode | NodeImpl | cfg {expr: MathExpr} → outputs.rrr/quantized; NO_EXPR → INCONCLUSIVE | math-eval.ts:115 |
| mpseQuantizeNode | NodeImpl | cfg {value, quantum} → outputs.bucket = round(v/q); non-finite → FAIL | oracle-registry.ts:34-42 |
| mpseOracleNode | NodeImpl | cfg {ruleId, expected} + inbound actual → PASS/FAIL/CONTRADICTED→FAIL, UNVERIFIABLE→INCONCLUSIVE | oracle-gate.ts:16-23 |
| ALL_KINDS rows | 5 entries | {kind:"mpse-*", family:"deterministic"} — append-only | registry.ts:34-73 |
| profiles/mpse | DomainModule | {name:"mpse", caps:[], kinds:[5+mpse-discharge], defaultTier:1, brackets:{}} | profiles/shared.ts:10-16 |
| CALIBRATED constants | named | MPSE_DEPTH_LIMIT 256 · MPSE_DOMAIN_LIMIT 10000 · sanctionedTolerancePips 3 · f(T)=24 · RRR floor 2.5 (D-R1) · SL ceiling 36 / min 4 | parser.ts:3-4; calibrate.ts:51-59 |

## 5 Failure modes (per component)

| Component | Failure mode | Behavior (fail-closed) |
|---|---|---|
| mpse-gate | malformed cfg (no expected) | FAIL, refusal-style, zero artifacts (ORACLE-MISSING class) |
| mpse-quantize | NaN/non-finite input | FAIL naming the field — a crashing predicate counts AGAINST |
| mpse-compute | unbound symbol / div-zero | INCONCLUSIVE NO_EXPR/undefined — never a silent pass |
| mpse-oracle | verdict CONTRADICTED | rolls up FAIL (worst-wins FAIL>INCONCLUSIVE>PASS) |
| embedded cast | depth ≥ 3 | FAIL DEPTH_EXCEEDED (workflow-machine.ts:41-45) |
| embedded cast | child kind unregistered | [JESL UNKNOWN-NODE] at build (D27 — no pass-through) |
| whole run | cap string non-empty + unbound | [JESL CAP-UNBOUND] pre-fire — keep requiredCaps: [] |
| circuit doc | cycle / dangling edge | [JESL CYCLE] pre-fire (graph.ts:129-195) |

## 6 Open decisions (with defaults)

| Fork | Evidence | Default |
|---|---|---|
| Shape A (flat kinds on parent) vs Shape B (one embedded workflow-machine node) | both verified; B is the literal microprocessor | B for whole-battery embeds; A for single-predicate gates on tier-2 cards |
| circuit compiler source | battery.json already carries id/kind/oracle/fixtures | compile battery → circuit doc (the E4 emit, one wave) |
| fixtures as vars vs file-io load | golden-week.json single-line | vars for mutants, file-io for golden-week |
| journal for standalone casts | wave-db infra (operator-resolved earlier) | SQLite per PLUTUS_MPSE_DB; embedded casts ride the parent chain |
| tier of an mpse card containing a bracket slot | tier law: generation requires tier 2 | pure MPSE cards stay tier 1 — bracket slots forbidden on them by construction |

Handoff: the L2 wave expansion (5 node impls + registry + profile + tests + the
battery→circuit emit) is the trident-deep-planning tool's territory on GO.

## Self-check

SPINE: BLUEPRINT named · ingredients loaded via skill tool in-session
(ascii-diagrams, ascii-graph, ascii-visualize, ascii-simulator,
trident-deep-planning) · visuals ruler-passed: master boxes inner 52 (borders
col 1/54), mechanism box inner 46, tree inner 46 — all lines ≤76, arrows
terminate at borders · claims anchored: v3:54/:73/:75-77/:88-99,
executor.ts:107-134/147-155/159-178/179-224, workflow-machine.ts:27-45/69-101,
registry.ts:34-73/104-119, mpse-discharge.ts:70-149, oracle-registry.ts:34-42,
profiles/shared.ts:10-16, battery 46/46 fp 8acfe74f… (measured) · caps: none
truncated.
