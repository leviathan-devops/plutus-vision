# Plutus V5 Overhaul — ShowMe (PLAN spine) v1

SPINE: PLAN — the overhaul is unbuilt (landing zone measured: 5 docs / 2,274L,
zero source). Evidence: operator orders this session (verbatim below), V5
FULL_BUILD_SPEC (2,021L) + V5 DETAILED ARCHITECTURE (440L) absorption, the port
specs on disk, JESL fork verified present (core/ complete), specs/mpse measured
first-hand (battery 46/46 fp 8acfe74f…, d17 19C/27E), src/kernel 2,962L built.

## 1 Problem statement (verbatim requirements)

- "port in ONLY what is needed for a clean 5.0 break from the opencode tree w/ 0
  context loss or regressions. start by forking in the 4.5.3 clean baseline"
- "E1/E2/E3 = JS workflows" · "TTE Pipeline = /goal w/ structured JS workflows
  and gates embedded in the goal prompt" · "Copy the built-in memory systems of
  mimocode and create a plutus-named duplicate… activates only when plutus mode
  is the harness"
- "/plutus-pipeline — same substrate as SUPER_GOAL_DPL1_SPEC.md"
- "plutus-browser-manager… N trading view tabs… cookies and session persistence
  long horizon… TV mcp tools across all tabs w/ zero issue"
- "MPSE can become embedded nodes on a JESL card" (bible §12B)
- Acceptance (corpus law): full-week 23/23 ±3p, RRR≥3.0 planned, determinism ×2.

## 2 Core insight

The overhaul is a RE-HOMING, not a rewrite: engines, kernel, and battery are
built (W0–W5 in-tree) — what's missing is the runtime (MiMoCode harness), the
honesty spine (calibration 19/46, theatrical gates unbuilt), and the E1 fixes
that gate everything downstream. Sequence by dependency: fork → engines →
kernel-cards → harness → MPSE spine → convergence. Never engines-after-harness
(E1 broken ⇒ everything broken); never harness-before-kernel (the goal pin
embeds kernel-calling workflows).

## 3 Scope (≤20, ordered = the wave ladder)

| # | Wave | Items |
|---|---|---|
| 1 | W-FORK | copy src/{e1,e2,card,kernel,mdve}+specs/{mpse,fixtures}+19-doc canon+failures.db+tv-browser-v3; mcp register; SHA-verify frozen pair |
| 2 | W-ENGINES | 5 E1 murder fixes (freshness model, 4H maxBars, OBCV multi-candle, matrix→zones bridge, reach cap); E2 authoritative + DayBand; predicate re-point |
| 3 | W-KERNEL | mpse-{gate,compute,oracle,quantize,mux} nodes + registry + profile; battery→circuit emit; 7-leg proof |
| 4 | W-HARNESS | .mimocode: agent/plutus.md + memory-dup hooks + plutus-engine tool + /plutus-pipeline + prompt sibling + 7 workflows + browser-manager + cron |
| 5 | W-MPSE | E-wave rows 1-10 (E8→E3+E6→E1+E2+E9→E5→E7+E10, wave-db journal infra); 27 mutants authored; R1-R34+37 laws→RuleCards |
| 6 | W-CONVERGE | full-week harness; 4 proving tests; phase-2 multi-week; Vibe decision; legacy kill-list |

## 4 Success criteria (command-verifiable)

| # | Criterion | Check |
|---|---|---|
| SC-1 | fork integrity | sha256sum sl-lmv.ts = 91294083…, trade-dedup.ts = 33914c89…; tsc --noEmit 0 |
| SC-2 | E1 gate | golden-LQZ oracle: 7 DXY rungs ≤1p from own-week data (bun run) |
| SC-3 | E2 gate | totality 90 rows (15d×3p×2dir) discharge VALID |
| SC-4 | battery unchanged by port | compile → fingerprint 8acfe74f… |
| SC-5 | kernel cards | cast receipt {verdict:PASS, chainVerified:true}; D17 mutants FAIL, golden PASS |
| SC-6 | harness | /plutus-pipeline <week> pins; plutus agent in Tab cycle; mimo mcp list shows tv-browser (38 tools) |
| SC-7 | MPSE spine | calibrate exit 0 with 46/46 CALIBRATED; journal chainVerified |
| SC-8 | convergence | full-week 23/23 ±3p; determinism ×2 byte-identical |

## 5 Test angles (tool-result-bound tokens)

| Angle | Probe | Pass token | Fail token |
|---|---|---|---|
| STATE | tamper a journal row between runs | chainVerified:false + exit 1 | silent true |
| TOOLS | call plutus-engine {engine:e1} pre-fork | structured error code | prose apology |
| BOUNDARY | float compare without tolerance in a new node | FLOAT_EPSILON_MISSING | accepted |
| LIFECYCLE | restart mid-week; resume goal | tracker UserPaused→Active; journal replay invoked:0 | silent recompute |
| FIREWALL | fabricate a zoneId in STEP-A | BLOCKED-class rejection naming the id | accepted |

## 6 Master graph — the exact ladder with gates

```
┌──────────────────────────────────────────────────────┐
│ W-FORK   manifest copy + SHA verify                  │
│ GATE: frozen pair byte-identical · tsc 0 ·           │
│       battery fp 8acfe74f… · mimo mcp list           │
└──────────────────────────────────────────────────────┘
   │
   ▼
┌──────────────────────────────────────────────────────┐
│ W-ENGINES  E1 murder-chain (5) · E2 authoritative    │
│ GATE: 7 rungs ≤1p · totality 90 VALID ·              │
│       e1/e2 test batteries green                     │
└──────────────────────────────────────────────────────┘
   │
   ▼
┌──────────────────────────────────────────────────────┐
│ W-KERNEL   mpse node family + circuit emit + proof   │
│ GATE: cast PASS chainVerified · mutants FAIL ·       │
│       7-leg harness green                            │
└──────────────────────────────────────────────────────┘
   │
   ▼
┌──────────────────────────────────────────────────────┐
│ W-HARNESS  agent + memory dup + engine tool +        │
│            /plutus-pipeline + workflows + browser    │
│ GATE: pin holds a full dry-week cast · gates fire    │
│       their OWN tokens (no generic preemption)       │
└──────────────────────────────────────────────────────┘
   │
   ▼
┌──────────────────────────────────────────────────────┐
│ W-MPSE     journal spine + tiers + 46/46 + laws      │
│ GATE: calibrate exit 0 · d17 46 CALIBRATED ·         │
│       RuleCard registry covers R1-R34+37             │
└──────────────────────────────────────────────────────┘
   │
   ▼
┌──────────────────────────────────────────────────────┐
│ W-CONVERGE full-week 23±3p · proving tests ·         │
│             phase-2 multi-week · Vibe GO/DROP        │
│ GATE: acceptance + determinism ×2 + zero             │
│       regressions on prior greens                    │
└──────────────────────────────────────────────────────┘
```

## 7 Mechanism pseudocode (the nontrivial blocks)

```
┌──────────────────────────────────────────────┐
│ W-FORK verify (per file, fail-loud)          │
│   for f in frozenPair + canonManifest:       │
│     sha = sha256(f)                          │
│     sha != pinned → STOP, name file+expected │
│   tsc --noEmit → 0 else STOP                │
│   compile.ts → fp == 8acfe74f… else STOP     │
│   mimo mcp list → tv-browser present         │
└──────────────────────────────────────────────┘
```

```
┌──────────────────────────────────────────────┐
│ W-ENGINES E1 fixes (one commit each)         │
│   freshness: fortress ≠ DEPLETED-at-3        │
│     (4+ defenses = FORTRESS state)           │
│   4H maxBars 60 → full window (Jun-22 in)    │
│   OBCV: multi-candle model on 1H/30m         │
│   bridge: model.lqzMatrix → model.zones      │
│   reach cap: 1.14460 reachable               │
│   after each: golden-LQZ oracle re-run       │
└──────────────────────────────────────────────┘
```

```
┌──────────────────────────────────────────────┐
│ W-HARNESS goal pin (the /plutus-pipeline)    │
│   plan.md = P0..P7 phase contract            │
│   evaluator criteria = cast verdicts +       │
│     golden counts + hash ×2 (journal rows)   │
│   skeptic panel reads RECEIPTS not prose     │
│   embedded gates: tolerance-freeze ·         │
│     counts · full-window · Friday-close      │
└──────────────────────────────────────────────┘
```

```
┌──────────────────────────────────────────────┐
│ W-KERNEL node registration (the seam)        │
│   ALL_KINDS += 5 {kind, family:              │
│     "deterministic"}                         │
│   replaceStubSync(kind, impl)                │
│   requiredCaps = [] (trap avoided)           │
│   emit: battery.json → circuit docs (1:1)    │
│   proof: mutants FAIL / golden PASS legs     │
└──────────────────────────────────────────────┘
```

## 8 Target file tree (the end state)

```
┌────────────────────────────────────────────┐
│ MIMOCODE/Plutus/ (end state)              │
├────────────────────────────────────────────┤
│ ├─ src/e1/ e2/ card/ kernel/ mdve/  FORKED │
│ ├─ specs/mpse/ + fixtures/          FORKED │
│ │   + journal.ts run-id.ts receipts.ts NEW │
│ │   + breaker.ts caps-guard.ts       NEW   │
│ ├─ vendor/tv-browser-v3/            FORKED │
│ ├─ canon/ (19 docs + failures.db)   FORKED │
│ ├─ .mimocode/agent/plutus.md        NEW    │
│ │   + tools/plutus-engine.ts        NEW    │
│ │   + tools/plutus-browser-manager   NEW    │
│ │   + command/plutus-pipeline.md    NEW    │
│ │   + skills/plutus-pipeline-prompt NEW    │
│ │   + workflows/e0..e6.js (7)       NEW    │
│ │   + hooks/ (memory-dup inject)    NEW    │
│ │   + plutus-memory/ (4-file set)   NEW    │
│ ├─ MASTER_CONTEXT/ (specs+bibles)   EXISTS │
│ └─ reports/                         EXISTS │
└────────────────────────────────────────────┘
```

## 9 Open decisions (with defaults)

| Fork | Evidence | Default |
|---|---|---|
| W-HARNESS before or after W-MPSE spine? | the goal pin's evaluator wants chain-verified casts | HARNESS first with in-memory chain; journal spine lands W-MPSE (receipts upgrade in place) |
| browser-manager in W-HARNESS or its own wave | desktop path viable now; container path blocked (image absent) | desktop-first in W-HARNESS; container upgrade its own follow-up |
| Leviathan PDF: TS render vs python port | V5 W6 recorded TS-ported | TS render; python port only if rule fidelity gaps appear |
| Vibe port | 0/12 gates | formal DROP at W-CONVERGE unless operator starts it |
| wave dispatch model | session capacity | W-FORK/W-ENGINES sequential; W-KERNEL+W-HARNESS parallelizable after engines (disjoint trees: jesl nodes vs .mimocode) |

Handoff: this DPL1-lite compresses the trident-deep-planning contract; the L2
expansion (per-file hunks, dispatch prompts, container plan verbatim) is the
deep-planning tool's territory on GO. Inputs already on disk: spec §1-§3,
bible §12B/§12C, both ShowMes.

## Self-check

SPINE: PLAN named · ingredients loaded via skill tool in-session (5/5) ·
visuals ruler-passed: ladder boxes inner 54 (borders col 1/56), pseudocode
inner 46, tree inner 46 — all ≤76, arrows terminate at borders · claims
anchored: landing-zone measured this turn (5 docs/2,274L, zero src), frozen
SHAs 91294083…/33914c89… (spec §1), fp 8acfe74f… (measured), d17 19C/27E
(measured), kernel 2,962L (measured), JESL core present (verified this turn) ·
caps: none truncated.
