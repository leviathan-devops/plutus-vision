# PLUTUS 5.0 — FULL BUILD PLAN (ShowMe PLAN-spine, v2 FULL)

SPINE: PLAN. The full plan: W-FORK → W-ENGINES → W-KERNEL → W-HARNESS →
W-MPSE → W-CONVERGE, file-by-file, gate-by-gate. Supersedes the v1 lite
(`Plutus_V5_Overhaul_ShowMe.md`, wave ladder only). Evidence: operator orders
verbatim (§1) · specs/mpse measured first-hand (compile 270L, calibrate 711L,
registry 394L, battery 46/46 fp 8acfe74f…, d17 19C/27E) · kernel 2,962L built ·
landing zone 6 docs/2,487L/src-absent (this turn) · JESL core 10/nodes 40/
profiles 5 present · bible §12B MPSE-Circuit research.

## 1 Problem statement (verbatim requirements)

- "port in ONLY what is needed for a clean 5.0 break from the opencode tree
  w/ 0 context loss or regressions. start by forking in the 4.5.3 clean baseline"
- "E1/E2/E3 = JS workflows" · "TTE Pipeline = /goal w/ structured JS workflows
  and gates embedded in the goal prompt"
- "Copy the built-in memory systems of mimocode… plutus-named duplicate…
  activates only when plutus mode is the harness"
- "/plutus-pipeline — same substrate as SUPER_GOAL_DPL1_SPEC.md"
- "plutus-browser-manager… N tabs… cookies long horizon… TV tools across all tabs"
- "MPSE Circuits = Embedded Logic Systems on the JESL card, as Aether Circuits
  = Embedded Agent Systems on the JESL kernel" (bible §12B thesis, adopted)
- Acceptance: full-week 23/23 ±3p · RRR≥3.0 planned · determinism ×2.

## 2 Core insight

Re-homing, not rewriting: engines + kernel + battery are BUILT in the agent
tree (~60% of W0–W5); missing = the MiMoCode runtime, the honesty spine
(19/46 calibrated), the E1 fixes. Order by dependency: fork → engines →
kernel ∥ harness → MPSE spine → converge. Never engines-after-harness
(E1 broken ⇒ everything broken); never harness-before-kernel (the goal pin
embeds kernel-calling workflows).

## 3 Master graph (every box → its §; gates inline)

```
┌──────────────────────────────────────────────────────┐
│ W-FORK §4 — manifest copy + SHA verify               │
│ GATE: frozen SHAs · tsc 0 · fp · mcp listed          │
└──────────────────────────────────────────────────────┘
   │
   ▼
┌──────────────────────────────────────────────────────┐
│ W-ENGINES §5 — 5 murder-chain fixes + E2 authority   │
│ GATE: 7 rungs ≤1p · totality 90 VALID · bat green    │
└──────────────────────────────────────────────────────┘
   │ parallel fork (disjoint trees)
   ├─────────────────────────────┐
   ▼                             ▼
┌──────────────────────┐  ┌──────────────────────┐
│ W-KERNEL §6 — mpse   │  │ W-HARNESS §7 — agent │
│ family + emit + proof│  │ + memory + tool +    │
│ GATE: cast PASS      │  │ goal + workflows +   │
│ chainVerified        │  │ browser + cron       │
└──────────┬───────────┘  └──────────┬───────────┘
           │ rejoin on both green    │
           ▼                         ▼
┌──────────────────────────────────────────────────────┐
│ W-MPSE §8 — journal spine + 46/46 + laws→cards       │
│ GATE: calibrate 0 · chainVerified · full registry    │
└──────────────────────────────────────────────────────┘
   │
   ▼
┌──────────────────────────────────────────────────────┐
│ W-CONVERGE §9 — 23±3p · proving tests · phase-2 ·    │
│ Vibe GO/DROP · kill-list                             │
│ GATE: acceptance + determinism ×2 + zero regressions │
└──────────────────────────────────────────────────────┘
```

## 4 W-FORK — the manifest (1 session, sequential)

```
┌──────────────────────────────────────────────┐
│ MIMOCODE/Plutus/  (end state)                │
├──────────────────────────────────────────────┤
│ ├─ src/e1/ e2/ card/ kernel/ mdve/ FORKED   │
│ ├─ specs/mpse/ + fixtures/        FORKED    │
│ ├─ vendor/tv-browser-v3/          FORKED    │
│ ├─ canon/ (19 docs + failures.db) FORKED    │
│ └─ .mimocode/* (wave 4)           NEW       │
└──────────────────────────────────────────────┘
```

| # | Item | Exact action |
|---|---|---|
| F1 | tree | copy src/{e1(~30f),e2(~25f),card(7f),kernel(2,962L),mdve}+specs/{mpse,fixtures} |
| F2 | canon | 19 docs → canon/ + plutus-reasoning-failures.db (20,322 rows) + TV_Browser_v3.0 → vendor/ |
| F3 | verify | sha256sum sl-lmv.ts=91294083… + trade-dedup.ts=33914c89… + tsc 0 + compile fp 8acfe74f… + calibrate exit 0 (19C/27E expected) |
| F4 | deps | package.json (effect,xstate,zod,bun:sqlite) + bun install |
| F5 | mcp | .mimocode/mimocode.json tv-browser block (timeout 600000, PLUTUS_PROJECT_DIR) |

GATE SC-1: SHAs byte-identical · tsc 0 · fp unchanged · `mimo mcp list` shows
38 tools. Noise left behind: stale-lineage backups, engine/ legacy, pipeline/
chain, hooks/identity/agents, VIBE, kronos, v4.2–v4.5 logs, root report_v452.

## 5 W-ENGINES — the five murder-chain fixes + authority (2–3 sessions)

```
┌──────────────────────────────────────────────┐
│ E1 FIX ORDER (one commit each, oracle first) │
│   freshness: 4+ defenses = FORTRESS          │
│   4H maxBars 60 → full window (Jun-22 in)    │
│   OBCV: multi-candle model on 1H/30m         │
│   bridge: model.lqzMatrix → model.zones      │
│   reach cap → 1.14460 reachable              │
│   E2 authoritative + DayBand London-open     │
└──────────────────────────────────────────────┘
```

| # | Fix | Files | Gate after |
|---|---|---|---|
| Ea | freshness model (fortress ≠ DEPLETED-at-3) | e1 pressure + mdve/freshness lineage | oracle re-run |
| Eb | 4H maxBars → full window | 4h-sd-lobe lineage | oracle re-run |
| Ec | OBCV multi-candle on 1H/30m | obcv adapter | zone count > 0 |
| Ed | matrix→zones bridge | mdve bridge | anchors see rungs |
| Ee | reach cap → 1.14460; predicates re-point LMV/OBCV | reach config + e1 machines | EU Tue row |
| Ef | E2 authoritative + DayBand (contract built — verify+wire) | e2 machines | totality 90 |

GATE SC-2/3: golden-LQZ oracle 7/7 DXY rungs ≤1p own-week · totality
∀(day,dir)∃! designation (90 rows) VALID · e1/e2 batteries green · tsc 0.

## 6 W-KERNEL — the mpse family + emit + proof (2 sessions, ∥ harness)

```
┌──────────────────────────────────────────────┐
│ registry (ALL_KINDS += 5 deterministic)      │
│   mpse-gate · mpse-compute · mpse-oracle     │
│   mpse-quantize · mpse-mux                   │
│ impl: replaceStubSync, requiredCaps: []      │
│ (the CAP-UNBOUND trap — handlers.ts:94-98    │
│  binds only Shell/Fs/Http; non-empty         │
│  unbound cap kills the run pre-fire)         │
└──────────────────────────────────────────────┘
   │
   ▼
┌──────────────────────────────────────────────┐
│ profiles/mpse.ts {caps:[], defaultTier:1} +  │
│ battery.json → circuit docs (1:1, D008)      │
│ proof: 7 legs (mutants FAIL / golden PASS)   │
└──────────────────────────────────────────────┘
   │
   ▼
┌──────────────────────────────────────────────┐
│ Trade Computer card: load → L1..L5 →         │
│ trade-compute → report → journal-sink        │
│ MPSE circuit embedded (Shape B: one          │
│ workflow-machine node, config.doc)           │
└──────────────────────────────────────────────┘
```

| # | Item | Shape |
|---|---|---|
| K1 | 5 node impls (NodeImpl, Effect.exit isolation free) | gate=assert · compute=28-tag ALU · oracle=discharge · quantize=int buckets · mux=oracle select |
| K2 | registry + wiring | ALL_KINDS rows + nodes/index wiring authority |
| K3 | emit | battery.json → circuit docs (E4); Shape A flat first, Shape B microprocessor on resolve |
| K4 | proof | golden SILENT + 9 mutants FIRE + concurrency (one FAIL beside PASS) |
| K5 | cast | runJeslWorkflow, runId=hash(docHash:seed); replay invoked:0 |

GATE SC-5: cast receipt {verdict:PASS, chainVerified:true} · 7-leg green ·
NO executor/channels/journal/caps changes.

## 7 W-HARNESS — the MiMoCode surface (2–3 sessions, ∥ kernel)

```
┌───────────┬──────────────────┬──────────────────┬───────────────┐
│ PHASE     │ WORKFLOW (math)  │ AGENT (judgment) │ GATE (JESL)   │
├───────────┼──────────────────┼──────────────────┼───────────────┤
│ P0 HARV   │ e0-harvest       │ Step A: options  │ SPAN + NOGAPS │
│ P1 E1     │ e1-zones         │ map vs charts    │ 7 rungs ≤1pip │
│ P2 STEP-A │ — (agent)        │ designations     │ IDs ∈ E1 map  │
│ P3 E2     │ e2-shapes        │ storyline judge  │ totality 90   │
│ P4 STEP-B │ — (agent)        │ T8/T10/T11       │ W-1..W-7 clean│
│ P5 E3     │ e3-kernel cast   │ refine loop 3×   │ RRR≥3 + counts│
│ P6 REPORT │ e6-report        │ review + sign    │ 23@±3p · ×2   │
│ P7 JUDGE  │ —                │ stop verify      │ ALL GREEN     │
└───────────┴──────────────────┴──────────────────┴───────────────┘
```

| # | Item | Shape |
|---|---|---|
| H1 | `.mimocode/agent/plutus.md` mode:primary | tool_allowlist: 38 tv-* + plutus-engine/browser-manager/workflow/task/read/write/glob/grep |
| H2 | plutus memory duplicate | 4-file set (seed map + exclusions, Bible §6 seed map) + hooks (system.transform/compacting inject gated agent==plutus; session.post writer) + canon store: forked shared.db 5,674 cards, read-only by symbol |
| H3 | exec seam `tools/plutus-engine.ts` | {engine:e0..e6\|battery,args} → bun run → JSON; workflows + pinned agent + JESL shell-exec all call it; NO exec in workflow scripts (sandbox law) |
| H4 | `/plutus-pipeline` + `-prompt` sibling | command + skill (goal-prompt precedent structure); pin on SUPER_GOAL substrate: phases=plan.md, evaluator=cast verdicts+hashes, skeptics read RECEIPTS, 4 anti-theatrical gates embedded |
| H5 | 7 workflows `.mimocode/workflows/e*.js` | meta+default, plutus-engine nodes, JS gating, schema returns |
| H6 | `tools/plutus-browser-manager.ts` | 16 actions (from the manager-law wave: display/Chromium/CDP/tab-N/symbol-map/cookies/persistence/GPU-verify/capture-per-tab/watchdog/state); stale-"6930" doc fix → 9333; loggedIn hardcoded untrusted |
| H7 | cron Monday ~06:00 London | /plutus-pipeline kickoff; LLM nodes via `mimo llm-server issue` /v1 tokens (never provider keys) |

GATE SC-6: full DRY-WEEK cast under the pin · every gate fires its OWN token
· plutus in Tab cycle · memory injects only in plutus mode.

## 8 W-MPSE — the honesty spine (2 sessions, after both tracks)

E-wave adoption (bible §2): E8 → E3+E6 → E1+E2+E9 → E5 → E7+E10.
| # | Item | Shape |
|---|---|---|
| M1 | E8 hardening | verdict-gated evidence writes + lastError in report JSON |
| M2 | tiers | exit-2 refusal + rollup FAIL>INCONCLUSIVE>PASS + gating-consumer check |
| M3 | journal spine | wave-db infra: SQLite PLUTUS_MPSE_DB (WAL, busy_timeout 5000, withImmediateTx) + hash-chain rows + runIds + receipts |
| M4 | calibration | 27 mutants authored (one per evidence-only row) → **46/46 CALIBRATED** |
| M5 | laws→cards | R1–R34 + 37 laws + 18 derailments via PATH-B → oracle-registry (verbatim provenance) |
| M6 | count invariants as data | f(T)≥24 · mirror floor · emitted+rejected=oracle-total |
| M7 | bounds | caps pre-check + breaker (3×exit-1 → OPEN) |

GATE SC-7: calibrate exit 0 · d17 46/46 · chainVerified · registry covers corpus.
Zero-dep preserved: every vendored module node-builtin-only.

## 9 W-CONVERGE — acceptance (2+ sessions)

C1 full-week 23-trade ±3p standing kernel fixture · C2 the 4 proving tests
standing (tolerance restate 2p/3p · Friday-close recount · uncapped-SL
survival · Tue–Fri holdout) · C3 phase-2 multi-week · C4 live-bars path
(e0 end-to-end) · C5 legacy kill-list executed · C6 Vibe GO/DROP recorded.
GATE SC-8: 23/23 ±3p · RRR≥3.0 planned · determinism ×2 · zero regressions.

## 10 Dispatch model + open decisions

Waves dispatch after gates: W2→{W3∥W4} parallel subagent waves (disjoint:
jesl/nodes vs .mimocode); red gate stops the wave, names the file.
| Fork | Default |
|---|---|
| harness-before-spine | HARNESS first with in-memory chain; journal spine lands W-MPSE (receipts upgrade in place) |
| Shape A vs B timing | A flat immediately (each gate a node); B microprocessor when E4 emit lands |
| Leviathan PDF | TS render (V5 W6 recorded TS-ported); python port only on fidelity gaps |
| browser container path | desktop-first (image absent on host); container upgrade follow-up |
| Vibe | formal DROP at W-CONVERGE unless started |

L2 expansion (per-file hunks + verbatim container plan) is the deep-planning
tool's territory on GO. Inputs: spec §1–§3, bible §§1–3, three prior ShowMes.

## Self-check

SPINE: PLAN · ingredients 5/5 loaded in-session via skill tool · ruler:
ladder/graph boxes inner 54 (borders col 56), swimlane 68 (widest, col 1/68,
≤76 ✓), file-tree inner 46, pseudocode inner 46 · arrows at borders · claims
anchored: landing-zone + core/nodes/profiles/agent-tree measured this turn;
SHAs/fp/d17/kernel-2,962L from session measurements; SUPER_GOAL/manager-law
from adoption waves · caps: none truncated.
