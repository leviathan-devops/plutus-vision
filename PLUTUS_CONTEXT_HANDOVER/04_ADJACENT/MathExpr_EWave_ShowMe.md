# MathExpr E-Wave — ShowMe (PLAN spine) v1

Spine: PLAN — the bible §2 enhancement architecture (E1–E10) does not exist yet.
Evidence: specs/mpse read first-hand this session (compile.ts 270L, calibrate.ts
711L, oracle-registry.ts 394L, battery.json 46/46 fp 8acfe74f…, d17-report.json
19C/27E/0F/0B, S-corpus 437L, total 2,941L wc) + PLUTUS_MATHEXPR_CARDS_BIBLE.md
§2 (728L file, fence at :614).

## 1 Problem statement (verbatim requirements)

Operator: "you do a META ANALYSIS of section 1 and write in section 2 any
proposed areas of enhancement where JESL architecture could make it better" —
done (bible §2, E1–E10). This plan BUILDS that adoption. Governing law (bible
§2 closing): "Adopt patterns, not dependencies — every proposal below must
preserve Iron Law 12 (zero-dep)" and "each vendored module is node-builtin-only
by contract."

## 2 Core insight

The pure substrate already owns law-form (cards), law-identity (fingerprint),
and law-proof (calibration exit codes). What it lacks is RUN-TRUTH: its verdicts
are files, its reruns are re-executions, its consumer contract is trust. The
E-wave adds run-truth with three small node-builtin modules — a hash-chained
journal (E1), an idempotent run identity (E2), receipts (E9) — plus tier
enforcement (E5) and a two-tier exit contract (E3/E6), without touching the
S-corpus or the oracle semantics.

## 3 Scope (loaded items, in adoption order per bible §2)

| # | Item | Files touched |
|---|---|---|
| 1 | E8a verdict-gated evidence writes | calibrate.ts |
| 2 | E8b lastError surfaced in report JSON | calibrate.ts |
| 3 | E3 exit-2 refusal tier + code registry | compile.ts, calibrate.ts |
| 4 | E6 explicit rollup FAIL>INCONCLUSIVE>PASS | calibrate.ts |
| 5 | E1 journal (wave-db infra model, operator-resolved) | NEW specs/mpse/journal.ts + SQLite (PLUTUS_MPSE_DB) |
| 6 | E2 run-identity.ts (runId, replay) | NEW specs/mpse/run-identity.ts |
| 7 | E9 receipts.ts (run manifest) | NEW specs/mpse/receipts.ts |
| 8 | E5 tier field + gating-consumer check | compile.ts + consumers |
| 9 | E7 caps pre-check (fixture count, budget) | calibrate.ts |
| 10 | E10 breaker.ts (3×exit-1 → OPEN) | NEW specs/mpse/breaker.ts |
| 11 | E4 emit/ executable units (OWN WAVE) | NEW specs/mpse/emit/ |

## 4 Master graph (every box → its scope row)

```
┌────────────────────────────────────────────────────┐
│ S-CORPUS S-1..S-7 — 46 cards, LAW SOURCE           │
│ (never machine-edited)                             │
└────────────────────────────────────────────────────┘
   │
   ▼  compile.ts unchanged parse + D13
┌────────────────────────────────────────────────────┐
│ +E3 exit 2 refusal tier (malformed law)            │
│ +E5 per-predicate tier field emitted               │
└────────────────────────────────────────────────────┘
   │
   ▼
┌────────────────────────────────────────────────────┐
│ battery.json — 46/46, fingerprint 8acfe74f…        │
│ predicates[] + tier {gating|recorded}              │
└────────────────────────────────────────────────────┘
   │
   ▼  calibrate.ts + E6 rollup + E7 caps + E8
┌────────────────────────────────────────────────────┐
│ journal.ts NEW (E1) — per-verdict rows,            │
│ self = sha256(payload + \0 + prev.self)            │
└────────────────────────────────────────────────────┘
   │
   ▼
┌────────────────────────────────────────────────────┐
│ run-identity.ts NEW (E2) — runId =                 │
│ hash(batteryFp + \0 + seed)[0:16]; replay          │
│ covered runs (invoked: 0)                          │
└────────────────────────────────────────────────────┘
   │
   ▼
┌────────────────────────────────────────────────────┐
│ d17-report.json + E9 receipts manifest             │
│ (runId, verdict, chainVerified, counts)            │
└────────────────────────────────────────────────────┘
   │
   ▼  E4 — OWN WAVE (scope row 11)
┌────────────────────────────────────────────────────┐
│ emit/ NEW — one executable unit per block;         │
│ 7-leg proof = the promotion gate                   │
└────────────────────────────────────────────────────┘

OVERLAYS (always-on): E7 caps refuse the half-run ·
E10 breaker: 3 consecutive exit-1 on the same
fingerprint → OPEN → promotion blocked until reset.
```

## 5 Mechanism pseudocode (the three new modules)

```
┌──────────────────────────────────────────────┐
│ journal.ts (E1)                              │
│   on verdict row                             │
│     payload = canonicalSerialize(row)        │
│       sorted keys, skip self                 │
│     row.self = sha256(payload + \0 + prev)   │
│     append row; prev = row                   │
│   verifyChain()                              │
│     recompute all self hashes in order       │
│     any mismatch → chainVerified false       │
└──────────────────────────────────────────────┘
```

```
┌──────────────────────────────────────────────┐
│ run-identity.ts (E2)                         │
│   runId = sha256(batteryFp + \0 + seed)      │
│           [0:16]                             │
│   if journal covers(runId)                   │
│     emit replay receipt (invoked: 0)         │
│   else                                       │
│     discharge every predicate (E6 rollup)    │
│     seal journal + receipt (E9)              │
└──────────────────────────────────────────────┘
```

```
┌──────────────────────────────────────────────┐
│ tier check (E5, consumer-side)               │
│   for each referenced predicate id           │
│     if consumer.tier == gating               │
│        and battery.tier != calibrated        │
│       refuse EXIT 2 NOT_CALIBRATED           │
│       (zero artifacts — refuse-before-spend) │
└──────────────────────────────────────────────┘
```

## 6 File tree (the enhanced substrate)

```
┌────────────────────────────────────────────┐
│ specs/mpse/ (enhanced)                     │
├────────────────────────────────────────────┤
│ ├─ S-*.md 437L unchanged (law source)      │
│ ├─ compile.ts +E3 tiers +E5 field          │
│ ├─ oracle-registry.ts 394L UNCHANGED       │
│ ├─ journal.ts NEW ~60L (E1 node:crypto)    │
│ ├─ run-identity.ts NEW ~40L (E2)           │
│ ├─ receipts.ts NEW ~50L (E9)               │
│ ├─ breaker.ts NEW ~40L (E10)               │
│ ├─ calibrate.ts +E6 +E7 +E8                │
│ └─ emit/ NEW (E4 — own wave)               │
└────────────────────────────────────────────┘
```

## 7 Success criteria (command-verifiable)

| # | Criterion | Check |
|---|---|---|
| SC-1 | tsc 0 on the enhanced tree | `bunx tsc --noEmit` exit 0 |
| SC-2 | battery identity unchanged by E3/E5 additions | compile → fingerprint still 8acfe74f… (fields added, ids+quotes untouched) |
| SC-3 | journal verifies | calibrate run → report `"chainVerified": true` |
| SC-4 | idempotent replay | same `--seed` twice → second receipt `"invoked": 0`, exit 0 |
| SC-5 | refusal tier distinct | corrupt one S-file quote → exit **2** + code D13_VIOLATION; verdict mismatch → exit **1** |
| SC-6 | rollup explicit | battery with ≥1 mismatch + no mismatch but evidence-only → report `verdict: FAIL` vs `INCONCLUSIVE` |
| SC-7 | tier enforcement | gating consumer refs S-1/B-3-divergence (evidence-only) → exit 2 NOT_CALIBRATED |
| SC-8 | zero-dep preserved | `grep -r "from \"npm:\|require(" specs/mpse/*.ts` → only node: imports |

## 8 Test angles (tool-result-bound tokens)

| Angle | Probe | Pass token (tool result) | Fail token |
|---|---|---|---|
| STATE | corrupt journal row between runs | `chainVerified: false` + exit 1 | silent `true` |
| BOUNDARY | seed omitted vs provided | default seed 0 recorded in receipt | crash / undefined seed |
| CONCURRENCY | two calibrate runs same seed interleaved | second run replays invoked:0 | double discharge rows |
| LIFECYCLE | breaker: force 3 exit-1 runs | `breaker: OPEN` + promotion blocked | 4th run still promoting |

## 9 Open decisions

| Fork | Evidence | Default |
|---|---|---|
| journal location | RESOLVED by operator: model the wave-manager infra (SHIP-APPROVED-v6, read first-hand: wave-db.ts 167L + evidence-store.ts 175L) | the wave-db pattern: single SQLite via `bun:sqlite`; path = env `PLUTUS_MPSE_DB` → test isolation (`BUN_TEST=1` → /tmp) → default `MIMOCODE/Plutus/.mpse/mpse.sqlite`; WAL + busy_timeout 5000 + 3× write-retry + `withImmediateTx` (wave-db.ts:18-120); "The DB is the only writer, NO JSON fallback, NO dual-write" (wave-db.ts:4); chain rows per evidence-store.ts:5-46 {sessionId, mode, layer, eventType, payload, previousHash, currentHash} + verifyChain (:77-95) + compact-with-aggregate-marker (:48-75) |
| E4 unit format | guard-card pattern minus external names | `{id, load, invoke, assert, sink}` JSON, one per block, D008 1:1 |
| seed source | CLI ergonomics | explicit `--seed` arg, default 0, recorded in receipt |
| E5 tier of evidence-only today | d17 19C/27E | recorded; only calibrated may be gating |
| E10 reset path | operator control | manual reset verb; no auto-close |

Handoff: this DPL1-lite stops at the plan contract; the L2 detailed workflow
(expansion of rows 1–10 into waves with per-file hunks) is the
trident-deep-planning tool's territory on GO.

## Self-check

Spine: PLAN named. Ingredients: ascii-diagrams/graph/visualize/simulator +
trident-deep-planning — all loaded via skill tool in-session. Visuals
ruler-passed: master-graph boxes inner width 52 (right border col 54),
pseudocode boxes inner 46, tree inner 44 — all ≤76. Claims anchored: every
number from this session's measured runs (wc 2,941L; 46/46; 19C/27E; fp
8acfe74f…; fence :614). Caps: none truncated.
