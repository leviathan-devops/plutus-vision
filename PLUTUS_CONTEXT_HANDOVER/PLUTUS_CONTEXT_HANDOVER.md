# PLUTUS CONTEXT HANDOVER — PRIMARY AGENT DUMP
## Duplicate this session's working memory into a fresh agent
### Paste this file first. Then unzip the rest of the pack. Then do not renegotiate the rulings.

```
Package: PLUTUS_CONTEXT_HANDOVER
Written: 2026-09-14
Author:      the session being handed off (ses_-ffe5f73f384beffeg7537uiYT, primary agent)
Consumer:    fresh agent opening /home/leviathan/JARVIS_WORKSPACE/Shared_Workspace/PLUTUS
Freeze:      no host freeze in this session (TypeScript/bun/SQLite userspace work only)
```

Conflict rule (also in README.txt at zip root):

```
If handover conflicts with BINDING spec on implementation detail, BINDING wins.
If BINDING conflicts with a superseded spec, BINDING wins.
Dead paths in the handover override any superseded "v1 daemon / keep-alive" language.
```

BINDING spec for this pack: `PLUTUS_5.0_MIMOCODE_ARCHITECTURE_SPEC.md`
(361L, in this zip at root AND in 01_BINDING_SPEC/).

---

# 0. WHO YOU ARE NOW

You are the PLUTUS 5.0 BUILD AGENT. Your stance is BUILDER-EXECUTOR on a
fully specified plan — not an explorer, not a re-litigator.

What you police:
- Every numbered ruling in §1.2 is CLOSED. An agent that reopens one is
  derailed; point at the ruling number and keep building.
- Every gate in §9 fires mechanically or the wave stops. A red gate names
  the file and the expected value. No prose overrides a gate.
- The zero-dep law (R11): every vendored module is node-builtin-only.
  An npm import in `specs/mpse/` or the journal spine is a defect, not a shortcut.

What you will not renegotiate:
- The fork manifest (§8 item 1): ONLY what is listed crosses. Nothing else.
- The wave order: W-FORK → W-ENGINES → W-KERNEL ∥ W-HARNESS → W-MPSE → W-CONVERGE.
  Engines before kernel, kernel before harness, harness before spine.
- The acceptance: full-week 23/23 ±3p, RRR≥3.0 planned, determinism ×2.
- The Section-1 purity fence: `specs/mpse/` stays free of external-runtime
  vocabulary (foreign-marker gate in §9/§12).

Your first reply in the new home is file:line hits proving you read the tree
(§11 kick text demands it), never a redesign.

---

# 1. THE ARC OF THIS SESSION

## 1.1 Requests, in order

1. Absorb Plutus_Agent (2.5G) + LASME (740K) via a dense explore wave; report
   (a) codebase-vs-specs status and functional distance, (b) architecture audit
   vs mimocode-docs + improvements, (c) JESL context, toward a plutus-named
   memory duplicate making MiMoCode the control plane.
2. Deep-synthesis round via the E2 dispatch template on: clean baseline
   v4.5.3, the theatrical v4.5.4 checkpoint, NON-NEGOTIABLE-RELOAD (5 files),
   the knowledge graph + MASTER_CONTEXT spine.
3. Full Plutus macro-context report: intent, target, architecture, built state,
   improvements, the MiMoCode runtime plan.
4. Locate the Plutus-specific T1 agent-in-the-loop lifecycle doc (the document
   that becomes the /goal translation source).
5. Full TTE canon absorption (7 docs) + JESL round-2 + mimocode-docs internals
   mapping + V5 specs + OHLC lexicon + MPSE library + reasoning-failures DB.
6. Present the Plutus 5.0 architecture (E1/E2/E3 overhaul with LASME, memory
   systems, workflows+goal execution, cleanup plan, MPSE completion) and port
   it into `Shared Workspace Context/MIMOCODE/Plutus`.
7. Preserve the architecture in the spec as §1 VERBATIM (spec-update skill).
8. Write the dense MathExpr RuleCards architecture bible (trident-bible-writing),
   THEN gated deep-research on JESL.
9. Preserve the delivered architecture verbatim as spec §1 (executed, §1 landed
   180L, fidelity defect Lvap→Lmv caught by grep and fixed).
10. Author the bible (§1: 16 laws 1A–1P, 7 pairs, 7 procedures, 23-row matrix,
    references); document the exec seam + SUPER_GOAL binding as spec §2.
11. Load TV_Browser_v3.0 into MiMoCode + plutus allowlist; harden
    container-virtual-display into plutus-browser-manager (explore-sourced);
    author as spec §3.
12. `show-me` the MathExpr RuleCards bible (SPINE: EXPLAIN; all fork anchors
    verified first-hand this turn).
13. Full CST2-anatomy bible for the cards INDEPENDENTLY, zero JESL pollution,
    THEN the §2 meta-analysis; then `/show-me`.
14. "section 2 = /show-me" (SPINE: BLUEPRINT emission of the §2 research).
15. Draw the MPSE Circuit inside a JESL card → Trade Computer Kernel →
    Leviathan report (`/show-me` SPINE: EXPLAIN).
16. Spec-update: preserve the circuit→kernel→report show-me as the next spec
    section (landed as bible §12C; spec §3 is the browser layer — no collision).
17. Status report: codebase state + the V5 overhaul plan.
18. `show-me` the EXACT plan (SPINE: PLAN; landed
    `reports/Plutus_V5_FULL_BUILD_PLAN_ShowMe.md`).
19. `show-me` the FULL built plan (SPINE: PLAN v2 FULL — 6 waves, file-level).
20. `/handover-package` + engineering-report + FULL migration of the working
    space into `/home/leviathan/JARVIS_WORKSPACE/Shared_Workspace/PLUTUS`
    (THIS order — executing now).

## 1.2 Rulings the operator already made (do not reopen)

- R1 (operator, verbatim naming): `Checkpoints/v4.5.4_MONDAY_GOLD_STANDARD_ACHIEVED`
  is "the theatrically engineered 'target hit' checkpoint". Monday-gold claims
  (5/5 ≤3p, G1-G10 10/10, A1-A7 7/7, +17.84R, determinism 0bbab1f7) are CLAIMS
  under theatrical audit, NOT established facts. True status re-anchors to
  v4.5.3_CLEAN_BASELINE + context_management/EVIDENCE_STATE.md (full-week
  11W/8L/0O of 19 = 58% vs ≥90%).
- R2 (operator doctrine, verbatim): "Doctrine is QUOTED, never synthesized."
  (D13, Bible 4.5:703-705.) Anything that can't be quoted doesn't get built.
- R3 (operator): fork ONLY what is needed for a clean 5.0 break from the
  opencode tree with 0 context loss/regressions; start from the 4.5.3 clean
  baseline; MASTER_CONTEXT gets fork-vs-noise triage.
- R4 (operator, verbatim framing): the TTE lifecycle becomes "JS workflows"
  pinned as a /goal "BECAUSE it needs agent-in-the-loop inference through the
  lifecycle"; embedded workflows/JESL keep the loop "mechanically anchored and
  reliably mechanical". (E1/E2/E3 = JS workflows, verbatim.)
- R5 (operator): duplicate MiMoCode's /goal as `/plutus-pipeline` on the SAME
  substrate as SUPER_GOAL_DPL1_SPEC.md, with sibling `/plutus-pipeline-prompt`
  (the goal-prompt precedent structure).
- R6 (operator, verbatim): "Copy the built-in memory systems of mimocode and
  create a plutus-named duplicate of the same architecture that runs on the same
  lifecycle and activates only when plutus mode is the harness for the session."
- R7 (operator, LASME-FIRST law): E1/E2/E3 are overhauled with LASME wired to
  existing mimocode LASME systems in src PRIOR to any JS workflow — E1 = Master
  Lexicons on MPSE/OHLC vision; E2 = Actors/State Machines/Engines; E3 = a JESL
  card consuming E1/E2 via a JESL Trade Computer Kernel.
- R8 (operator, verbatim, the exec seam): "workflows have no exec — a custom
  tool .mimocode/tools/plutus-engine.ts shells bun run against the engines and
  returns JSON; workflows call it, gate in JS, and the goal-pinned agent calls it
  directly mid-loop. LLM-needing nodes use mimo llm-server issue /v1 tokens
  (never a provider key)."
- R9 (operator thesis, adopted verbatim): "MPSE Circuits = Embedded Logic
  Systems on the JESL card, as Aether Circuits = Embedded Agent Systems on the
  JESL Kernel"; same circuit design micro vs macro. Confirmed by the v3 chip-mask
  research (bible §12B): the [D] DETERMINISTIC ALU is the MPSE slot.
- R10 (operator, ship-path): this pack ships into
  `/home/leviathan/JARVIS_WORKSPACE/Shared_Workspace/PLUTUS`, NOT the skill's
  Grok_Build default. Packer invoked with --out at the new home.
- R11 (zero-dep law): every vendored module is node-builtin-only. Iron Law 12
  of the bible. Patterns-never-imports: adopt JESL patterns, never an import.
- R12 (operator doctrine, verbatim): "GET THE CORRECT FUCKING DATA OR THROW
  ERROR. BLACK AND WHITE, NO MIDDLE GROUND, NO FALLBACK FABRICATED BULLSHIT."
- R13 (E-wave order): E8 → E3+E6 → E1+E2+E9 → E5 → E4 (own wave) → E7+E10.
- R14 (presentation): "section 2 = /show-me" — the meta-analysis deliverable IS
  a show-me artifact (SPINE: BLUEPRINT).
- R15 (anti-theatrical): the goal prompt embeds tolerance-freeze, count
  invariants, full-window acceptance, Friday-close — the Monday-gold drift class
  becomes mechanically unrepresentable.

## 1.3 What this session already produced (file table)

| File (new home) | Lines | Status |
|---|---|---|
| PLUTUS_5.0_MIMOCODE_ARCHITECTURE_SPEC.md (§1 preserved, §2 seam+substrate, §3 browser) | 361 | build authority |
| MASTER_CONTEXT/PLUTUS_MATHEXPR_CARDS_BIBLE.md (§1 693L, §2 E1–E10 + §12B + §12C) | 1088 | canon |
| MASTER_CONTEXT/MATHEXPR_RULECARD_ARCHITECTURE_BIBLE.md (16 laws, 7 pairs, 7 procs, 23-row matrix) | 500 | canon |
| reports/Plutus_V5_FULL_BUILD_PLAN_ShowMe.md (v2 FULL, 6 waves file-level) | 239 | plan |
| reports/Plutus_V5_Overhaul_ShowMe.md (v1 lite, ladder) | 213 | plan (superseded by FULL) |
| reports/MPSE_Circuit_ShowMe.md (BLUEPRINT, the 5 node impls) | 130 | blueprint |
| reports/MathExpr_EWave_ShowMe.md (PLAN, E-wave, journal RESOLVED) | 195 | plan |
| TOTAL | 2726 | diff-r clean vs source |

---

# 2. THE PRODUCT IN ONE PAGE

The Plutus 5.0 MiMoCode port: a re-homing (not rewrite) of a ~60%-built V5
trading engine (E1 lexicons + E2 machines + E3 JESL kernel + 46-predicate MPSE
battery) off the opencode runtime onto the MiMoCode control plane — goal-pinned
weekly lifecycle, embedded MPSE logic circuits, plutus-scoped memory, an
N-tab browser engine — converging on full-week 23/23 ±3p acceptance.

```
┌──────────────────────────────────────────────────────┐
│ W-FORK  manifest copy + SHA verify                   │
│ W-ENGINES  5 murder-chain fixes + E2 authority       │
│ W-KERNEL ∥ W-HARNESS  mpse nodes + emit + proof ·    │
│     agent + memory + tool + goal + browser           │
│ W-MPSE  journal spine + 46/46 + laws→cards           │
│ W-CONVERGE  23±3p · proving tests · phase-2 · Vibe   │
└──────────────────────────────────────────────────────┘
```

What it is NOT: not a rewrite of the trading math (the math ports verbatim);
not a JESL import (patterns only, zero-dep); not a Monday-gold repeat (the
anti-theatrical gates are embedded); not an opencode plugin anymore (the SDK
coupling stays behind as noise).

---

# 3. HOST / FREEZE INTERNALS

- Host: no freeze in this session (userspace TS/bun/SQLite work, no host patch).
  Toolchain: node v24.13.1 (measured) · bun (specs/mpse harness runtime) ·
  `bun:sqlite` (the journal-spine driver).
- Measured anchors (all first-hand, grep-verified in-session):
  - specs/mpse: compile.ts 270L · calibrate.ts 711L · oracle-registry.ts 394L ·
    battery.json 46/46 (fp 8acfe74f272bf736de101e297b731cfa97c9fdd4a1684e63363489f116af7b7e) ·
    d17-report.json 19C/27E/0F/0B · S-corpus 437L (7 files) · 9 mutants.
  - src/kernel/: 2,962L total, trade-computer.ts 301L (RRR_FLOOR 2.5 at :13),
    l4-cascade.ts 174L (CASCADE_NO_INVERSE law :6-7), report-rules.ts 158L
    (52 REPORT_RULES; rule 9 TA_CENTER CRITICAL :65; rule 10 6.55in :66).
  - Frozen pair: sl-lmv.ts 91294083… / trade-dedup.ts 33914c89… (byte-verified).
  - MIMOCODE/JESL fork: core/ 10 files · nodes/ 40 · profiles/ 5 (default,
    sales, shared, trading, trident).
  - SHIP-APPROVED-v6: src/tools/wave-db.ts 167L (WAVE_DB_PATH :12-14; WAL +
    busy_timeout 5000 :88-90; `withImmediateTx` :103-120; "The DB is the only
    writer, NO JSON fallback, NO dual-write" :4) · src/evidence/evidence-store.ts
    175L (rows :5-46, verifyChain :77-95, compact-with-marker :48-75).
  - Host display: DISPLAY :1 alive; google-chrome-stable present;
    plutus-container-testing:master image ABSENT; plutus-browser volume ABSENT
    (blocks the container browser path — desktop-first).
- Hooks that exist: none authored yet (W-HARNESS). Evolve hook surfaces are
  mapped: system.transform + compacting (inject), session.post (writer),
  actor.preStop (gate), tool.execute.before/after (arg/result gates).
- Hooks that do NOT exist: no plutus checkpoint writer; no JESL gate hooks;
  no pin-generator skill; no goal judge-clone (SUPER_GOAL substrate owns this).

---

# 4. SOURCE ANALOGS

| Source | Take | Refuse |
|---|---|---|
| Plutus V5 tree (agent) | src/{e1,e2,card,kernel,mdve}, specs/{mpse,fixtures}, journal.ts pattern | pipeline/, hooks/, identity/, agents/ (opencode SDK coupling), stale backups |
| JESL core (fork) | executor dataflow, caps model, channels, registry contract, jesl-run idempotency, workflow-machine embed, bracket law, mpse-discharge template | mpse:calibrate cap trap (unbound on CLI), raw-runProgram auto-PASS, whole-run-only replay, outbound-writes-on-FAIL, silent refusals, compiler.ts divergence |
| SHIP-APPROVED-v6 | wave-db infra (WAL/busy/withImmediateTx/single-writer) + evidence-store chain rows + compact markers | module singleton STATE model (session-keyed SQLite required instead) |
| SUPER_GOAL spec | L3 driver, tracker/goal.json, evaluator, skeptic panel, update_goal acks, Strategist, goal_rules injection | legacy /goal judge path stays untouched (mutual exclusion) |
| Trident managers (ct/wave/omni) | manager-tool design law (11 points) + action tables | opencode.db part-stream observers (MiMo session stores differ) |
| TV_Browser_v3.0 | all 38 tools, CDP pending-map pattern, renderer-zombie probe, chartWidgetCollection API | stale port strings (6930→9333 fix), hardcoded loggedIn:true, single-tab model |
| container-browser-auth | daemon-survival law (exec -d+nohup+setsid), X11/Weston recipes, CDP-screenshot canon | x11vnc/xdotool (SIGABRT law), noVNC-as-primary |
| container-virtual-display | GPU flag law verbatim (gl-egl + EGL vendor + banned list) | host-desktop GUI spawns, ever |

---

# 5. WHAT ALREADY EXISTS ON DISK

## 5.1 In this home (the migrated tree)

Module table: spec 361L · bible-2 1088L · bible-1 500L · FULL plan 239L ·
Overhaul lite 213L · Circuit 130L · E-Wave 195L. Total 2,726L, diff-r clean.
The ONE thing missing: `src/` (zero source files — W-FORK unexecuted).

## 5.2 In the source trees (measured, ready to fork)

- src/e1/ (~30 files: lexicon machines + XState actors + adapters + tests incl.
  future-bar-leak) · src/e2/ (~25: 6 machines + computations + discharge) ·
  src/card/ (7: schema/assembler/provenance/golden-card) · src/kernel/ (2,962L) ·
  specs/mpse/ (battery 46/46 fp 8acfe74f…) + fixtures/ (9 mutants + golden-week).
- No plutus-cards/ output dir yet. W3.5 visual pipeline unbuilt. W7 PBA/PTA
  unverified. W8 decommission not done.

## 5.3 Evidence ledger (carried)

- Baseline v4.5.3: 12/21 ≤3p, +25.30R/55% (f8235815 ×2).
- Monday gold: narrowed-gate verdict (week→Monday, 21→5, no Friday rule,
  cap-bound 3.00R, +17.84R sums to +16.84R) — NOT acceptance.
- Full-week: 11W/8L/0O of 19 = 58% vs ≥90% (D97 classes).
- D17 exact: 19C/27E/0F/0B (retracts prior "~20/46 born-off" phrasing).

---

# 6. WHAT WAS REJECTED

| Plan | Why dead | Transcript signature |
|---|---|---|
| Monday-gold as acceptance | narrowed gate proven (M1–M7, X2); intent unproven but scope engineered | any "5/5 gold standard achieved" without full-week re-anchor |
| Vibe Python port continuation | 0/12 gates, unstarted; formal DROP at W-CONVERGE unless started | "port the SignalEngine" without the DROP ruling |
| opencode-tree carry | SDK coupling (5 hooks, module globals) is the thing being escaped | any `from '@opencode-ai/plugin'` in the fork |
| Per-gate epsilon config | the tolerance-split class (2p/3p) | a second tolerance constant anywhere |
| JSON-fallback / dual-write journal | wave-db R2 law | a `.json` mirror beside the SQLite |
| Raw runProgram calls | auto-PASS stubs (executor.ts:190-191) | runProgram without CLI handle-builder |
| Daemon/idle second notifier for the goal loop | anatomy two-notifier law | session.idle→promptAsync beside the driver |
| python Leviathan port | V5 W6 recorded TS-ported | a python report path unless fidelity gaps appear |
| Container-first browser | image + volume absent on host | container path before import |
| JESL import (code dependency) | Iron Law 12 zero-dep | any `from "…jesl…"` inside specs/mpse |
| Direct E3 tuning before E2 | E2 advisory is the diagnosed failure | mirror edits without designation authority |
| Single-day gate in the goal pin | M2 (week→Monday shrink) | a `days:['Monday']` eval window |

---

# 7. THE DRIVE / PATCH CONTRACT

- Helper: the plutus-engine custom tool
  `.mimocode/tools/plutus-engine.ts({engine:e0..e6|battery, args}) → bun run → JSON`.
  All deterministic execution flows through it; no exec in workflow scripts.
- Inject shape: goal-pin WAVES call `workflow({operation:"run",name,args})`;
  JESL shell-exec nodes reach the tool via HostTransport.invokeTool;
  LLM nodes mint `mimo llm-server issue` /v1 tokens (directory-bound, never cached).
- Files TO touch: the R3 §8 tree (specs/mpse + new journal/run-id/receipts/breaker;
  jesl node family + profile; .mimocode/*; canon fork).
- Files NOT to touch: opencode legacy (pipeline/hooks/identity), node_modules,
  WAL sidecars (never checkpoint), golden-week.json bytes (fingerprint custody),
  the frozen pair semantics (byte-identical always).

---

# 8. IMPLEMENTATION ORDER

1. W-FORK: execute the §4 manifest (F1-F5); gate SC-1 (SHAs, tsc 0, fp, mcp).
   Evidence first, nothing else starts.
2. W-ENGINES: Ea-Ef one commit each, oracle-gated; gate SC-2/SC-3.
3. W-KERNEL ∥ W-HARNESS (disjoint trees): K1-K5 + H1-H7; gates SC-5/SC-6.
4. W-MPSE: M1-M7 in E-wave order; gate SC-7 (46/46, chainVerified).
5. W-CONVERGE: C1-C6; terminal gate SC-8 (23/23, ×2, zero regressions).
Deletes first: stale-lineage backups never cross; the old T1 7-tool chain is
translated, not ported; Tier-D pixel rows retired where Golden Feedback
supersedes; `computeLmvTP` STALE-tag retracted (graph verified :2968).

First agent reply = sha256sum hits + `ls src` evidence, never a redesign.

---

# 9. PROOF / ACCEPTANCE

| Scenario | Evidence (tool-result, not prose) |
|---|---|
| fork integrity | sha256sum outputs + tsc exit 0 + compile fp line |
| E1 gate | bun oracle run: 7/7 DXY rungs ≤1p |
| E2 gate | totality discharge: 90 VALID |
| kernel | cast receipt JSON {verdict:PASS, chainVerified:true} + mutants FAIL rows |
| harness dry-week | goal transcript: all P0-P7 cast verdicts + per-gate OWN tokens |
| MPSE spine | calibrate exit 0 + d17 46/46 + journal chainVerified |
| tolerance split regression | single GOLDEN_ENTRY_TOL card referenced by harness AND verdict |
| fabricated input | BLOCKED-class error naming the zoneId |
| restart resume | tracker UserPaused→Active + journal replay invoked:0 |
| terminal | 23/23 ±3p table + sha256sum ×2 identical + prior-greens table |

---

# 10. ZIP MAP + READ ORDER

```
PLUTUS_CONTEXT_HANDOVER.zip
├── README.txt                  ← conflict rule + paste order
├── PLUTUS_CONTEXT_HANDOVER.md  ← this file (root: lazy paste works)
├── PLUTUS_5.0_MIMOCODE_ARCHITECTURE_SPEC.md  (root: binding, lazy paste)
├── 00_HANDOVER/  (this file)
├── 01_BINDING_SPEC/  (the architecture spec)
├── 02_SUPERSEDED_READ_ONLY/  (SUPERSEDED_NOTES.md — retractions, not code)
├── 03_HOST_BIBLES/  (both MATHEXPR bibles)
└── 04_ADJACENT/  (4 ShowMes + engineering report v1)
```

Read order: this file §0-§2 → binding spec §1 → FULL plan → bible-2 §§1-3 →
bible-1 → adjacent ShowMes.

---

# 11. KICK PROMPT

```
Open /home/leviathan/JARVIS_WORKSPACE/Shared_Workspace/PLUTUS.
Read PLUTUS_CONTEXT_HANDOVER.md §0-§2, then 01_BINDING_SPEC/ §1 (fork verdict).
Prove you loaded it: reply with sha256sum of the two frozen SHAs named in §3
(sl-lmv 91294083…, trade-dedup 33914c89…) as recorded in battery context, plus
`ls src 2>&1` showing WHY W-FORK is first — no redesign, no new architecture.
Then execute W-FORK items F1-F5 per reports/Plutus_V5_FULL_BUILD_PLAN_ShowMe.md
§4, stopping LOUD on the first red gate with file+expected named.
Rulings R1-R15 are closed. Iron Law 12 holds on everything.
```

---

# 12. GREP CONTRACTS

| Contract | Command | Expected |
|---|---|---|
| zero foreign markers in specs | `grep -ricE 'jesl\|warhead\|opencode' specs/mpse/` | 0 |
| zero float-compares in battery code | `grep -rn '===.*\.\|<[0-9.]*\.' specs/mpse/*.ts` | 0 (quantize only) |
| single tolerance declaration | `grep -rn 'tolerancePips\|TOLERANCE' specs/mpse/` | 1 site + fixture riders |
| frozen SHAs current | `sha256sum src/mdve/sl-lmv.ts src/mdve/trade-dedup.ts` | prefixes match §3 |
| battery identity | `bun specs/mpse/compile.ts` stdout fp | 8acfe74f… |
| JESL-name hygiene in journal spine | `grep -rn 'from.*jesl' specs/mpse/` | 0 (patterns only) |
| bible §1 purity | `sed -n '1,/^## 12\./p' PLUTUS_MATHEXPR_CARDS_BIBLE.md \| grep -icE 'jesl\|aether'` | 0 |

---

# 13. FALSE CEILINGS ALREADY POPPED

1. "The cards need a kernel" — standalone (node builtins), kernels consume.
2. "46 predicates = 46 green" — 19C/27E/0F/0B; the middle tier is honesty.
3. "~20/46 with born-off mutants" — retracted: born_off is [].
4. "The 5/5 gold is acceptance" — narrowed gate proven; re-anchor.
5. "E2 is fine, fix E3" — E2 advisory is the failure; authority first.
6. "Tolerance per gate" — one constant, conflict throws.
7. "Golden levels as inputs" — validation-only; a read path derails.
8. "A green battery is live" — only CALIBRATED gates (F7).
9. "Import the JESL runtime" — patterns, never imports (Iron Law 12).
10. "Rebuild the math" — re-home it; ~60% already built.

---

# 14. QUESTIONS YOU MAY ASK

Only unruled items:
1. Confirm or fold the old-bible §2?
2. S-5 floor tension (2.5 ratified vs 3.0 executed) — build constant by whose authority?
3. Vibe port: formal DROP now, or start at W-CONVERGE?
4. bible-2 density (693L vs band): expand in place, or accept with the 500L companion?
5. Tier-D LONG SL rows — confirm or hold?
NONE others. Everything else is ruled.

---

# 15. SELF-CHECK

- I can state R1 (theatrical checkpoint) and R13 (E-wave order) verbatim.
- I can point at the fork manifest (W-FORK F1-F5) and the noise list.
- I can run the grep contracts and read their expected outputs.
- I can name all 8 success criteria and their check commands.
- I can execute W-FORK first without redesigning anything.
- I can state why requiredCaps must be [] (the CAP-UNBOUND trap).
- I can state the conflict rule: BINDING wins on detail; handover wins on
  rulings and dead paths; superseded is history only.

---

# APPENDICES

## A. Frozen identifiers (custody)

- sl-lmv.ts → prefix 91294083 · trade-dedup.ts → prefix 33914c89
- battery fp → 8acfe74f272bf736de101e297b731cfa97c9fdd4a1684e63363489f116af7b7e
- report_v452 baseline → f8235815 (×2) · Monday digest → 0bbab1f7 (CLAIM)
- mirror formula → f(T) = N×(1+P) = 24 · determinism ×2 required

## B. Key file:line index (verified in-session)

- compile.ts D13 gate :130-146 · FORM/BLOCK_KINDS :28-32 · fp :10-14
- calibrate.ts exit contract :4-7 · FALLBACK :48-59 · founding control :19-22
- oracle-registry.ts quantize :33-42 · fail-closed :5-9 · ORACLES :381-392
- near_edge delta cross-check :363-372 · inverted band :251-253
- wave-db.ts WAL :88-90 · single-writer :4 · withImmediateTx :103-120
- evidence-store.ts rows :5-46 · verifyChain :77-95 · compact :48-75
- workflow-machine.ts sub-doc :27-35 · depth :41-45 · context :87-101
- trade-computer.ts RRR_FLOOR :13 · l4-cascade CASCADE_NO_INVERSE :6-7
- report-rules.ts 52 rules :56+ · center-alignment CRITICAL :65 · 6.55in :66
- kernel specs: v2 411L · v3 313L (chip mask :1, operator quote :54, ALU :88-99)

---

# APPENDIX C. INVENTORY TABLES (measured 2026-09-14, first-hand)

## C1. Fork-source tree (agent tree, line counts by directory)

| Directory | Files | Fork decision |
|---|---|---|
| src/substrate/ | 154 | NOISE (Paragon binding stays behind) |
| src/mdve/ (40) | LMV+OBCV engines + frozen pair | FORK |
| src/pipeline/ (32) | opencode 7-tool chain | TRANSLATE, not port |
| src/e1/ (29) | machines, actors/, adapters/, core/, tests/ | FORK (W2 built) |
| src/e2/ (28) | machines/, computations/, tests/ | FORK (W3 built) |
| src/tvi/ (23) | VLM/vision stack | LATER (W3.5 decision) |
| src/kernel/ (21) | 12 source + 9 test files | FORK (W5 built) |
| src/brains/ (17) | legacy lobes | NOISE (superseded by e1/e2) |
| src/clients/ (15) | fetchers | LATER (W-CONVERGE C4) |
| src/runtime/ (10) | opencode runtime stubs | NOISE |
| src/jesl/ (10) | hello-workflow fixture | NOISE (JESL fork owns this) |
| src/semantic-firewall/ (9) | enforcement | LATER (W7 verification) |
| src/card/ (7) | schema/assembler/provenance/golden-card | FORK (W4 built) |
| src/report/ (6) | generators | LATER (W6 report decision) |
| src/hooks/, identity/, agents/ | opencode coupling | NOISE |
| src/engine/ (5) | self-marked legacy | NOISE |
| src/engine3/ (6), engines/ | visual lanes | LATER (W3.5) |
| src/{enforcement,graph,vei,visual,graphify-out,tools,utils} | mixed | LATER/NOISE per item |

## C2. e1 inventory (29 files, FORK)

machines/: candle-pressure.ts, candle-shape.ts, zone-classification.ts,
zone-pressure.ts, shape-chain.ts, obvious-trades.ts, index.ts · core/:
engine.ts (ClassifierResult pipeline), types.ts (PatternFamily, MachineRule) ·
actors/: zone-map-actor.ts, pressure-actor.ts, container.ts (+3 test files) ·
adapters/: market-data-adapter.ts (anchorMs gate, FUTURE_BAR_LEAK),
obcv-engine.ts (bw≥3.0, bf≥0.65) · tests/: fixtures.ts, per-machine battery,
properties battery (15,000 assertions), golden-fixture, future-bar-leak ·
index.ts, run-fixture.ts.

## C3. e2 inventory (28 files, FORK)

machines/: shape-chain-machine.ts (7 shapes SS/BS/R/WL/RWL/WLS/PBS),
designation-machine.ts (IDs only, NO price field), cascade-machine.ts
(requires/forbids/detectLoop), zone-pressure-machine.ts, freshness-machine.ts,
workflow-machine.ts, types.ts, index.ts, tests/ · computations/: mirror-floor.ts
(f(T)=24), divergence.ts (≤0.35), totality.ts (90 rows), zfp.ts (ladder),
run-discharge.ts (+tests) · types.ts · tests/: designation-totality,
mirror-floor, shape-chain-golden, side-inversion, workflow (+support).

## C4. kernel inventory (21 files: 12 source + 9 test, FORK)

card-loader.ts (schema+provenance gate) · l1-telescope.ts · l2-pressure.ts ·
l3-fib.ts (1.272/1.618/2.618) · l4-cascade.ts (CASCADE_NO_INVERSE FAIL loud :6-7;
GU reads ACTIVE EU only :133) · l5-ti-graph.ts (structural score) ·
trade-computer.ts 301L (RRR_FLOOR 2.5 :13; verdicts + provenance interfaces) ·
journal.ts (harvest→report causal chain) · report-model.ts 105L ·
report-rules.ts 158L (52 rules; rule 9 TA_CENTER CRITICAL :65; rule 10 6.55in :66) ·
report-render.ts 236L · + 9 test files (card-loader, l1..l5, report-model,
report-render, report-rules, trade-computer).

## C5. card inventory (7 files, FORK)

schema.ts (zod meta/e1/e2/visuals/reasoning) + schema.test.ts · assembler.ts +
assembler.test.ts · provenance.ts · types.ts · golden-card.json.

## C6. specs/mpse inventory (measured: compile 270L, calibrate 711L, registry 394L)

S-1-cascade-law.md 55L (6 blocks) · S-2 47L (5) · S-3 89L (12) · S-4 70L (7) ·
S-5 67L (6, D-R1 header) · S-6 52L (5) · S-7 57L (5) · battery.json 496L
(46/46, fp 8acfe74f…) · d17-report.json 554L (19C/27E/0F/0B) · jspec-check.ts 79L.
Fixtures: golden-week.json + 9 mutants (40setup, 13setup, sideinversion-v452,
sideinversion-v453-silent, tpcap, eu4-deep-rung, tolerance-drift, rrr-drift,
eu2-near-edge).

## C7. Frozen SHAs (measured this turn, full 64-hex)

- sl-lmv.ts → 912940832fac44bc838d53423cbb921eff501de60a9f2641bf20c1d1497eaeab
- trade-dedup.ts → 33914c897e7775402eefd7d13a5d3675667a2ace576b55a689bc864401a680e4

## C8. MASTER_CONTEXT count: 77 files (the 19-doc fork list names the keepers)

---

# APPENDIX D. TRANSITION TABLES (wave-by-wave file maps)

## D1. W-FORK file flow (source → dest)

| Source (agent tree) | Dest (PLUTUS home) | Mode |
|---|---|---|
| src/{e1,e2,card,kernel,mdve} | src/ (mirror) | byte-identical |
| specs/{mpse,fixtures} | specs/ (mirror) | byte-identical |
| 19 canon docs (fork-listed) | canon/ | byte-identical |
| plutus-reasoning-failures.db | canon/failures.db | binary copy |
| Ship_Packages/TV_Browser_v3.0 | vendor/tv-browser-v3/ | copy |
| MASTER_CONTEXT/PLUTUS_V5 specs | (already cited, reference) | read-only |

## D2. W-ENGINES change surface (forked tree only)

freshness lineage → FORTRESS fix · 4h-sd-lobe → maxBars · obcv adapter →
multi-candle · mdve bridge → matrix→zones · reach config → 1.14460 · e2
machines → authority+DayBand · e1 machines → LMV/OBCV re-point.

## D3. W-KERNEL new files (JESL fork tree)

nodes/mpse-{gate,compute,oracle,quantize,mux}.ts · registry ALL_KINDS += 5 ·
nodes/index wiring · profiles/mpse.ts · specs/mpse journal/run-id/receipts/
breaker · circuit emit (E4 wave).

## D4. W-HARNESS new files (PLUTUS home .mimocode/)

agent/plutus.md · tools/plutus-engine.ts · tools/plutus-browser-manager.ts ·
command/plutus-pipeline.md · skills/plutus-pipeline-prompt/ ·
workflows/e0..e6.js (7) · hooks/3 · plutus-memory/ (4-file set) ·
mimocode.json (tv-browser block) · cron.

---

# APPENDIX E. WORKED TRACES (evidence-chain shapes)

## E1. A fork verify (the W-FORK gate as executed)

```
sha256sum src/mdve/sl-lmv.ts
→ 912940832fac…c1d1497eaeab  ✓ prefix matches custody
sha256sum src/mdve/trade-dedup.ts
→ 33914c897e77…a680e4  ✓
bunx tsc --noEmit
→ exit 0
bun specs/mpse/compile.ts
→ fingerprint 8acfe74f…  ✓ identical to custody
bun specs/mpse/calibrate.ts
→ exit 0, d17 19C/27E  ✓ matches custody
mimo mcp list
→ tv-browser 38 tools ✓
```

## E2. An E1 oracle discharge (golden-LQZ gate)

```
gate GOLDEN_LQZ_ORACLE (7 DXY rungs, tol ≤1p, own-week data):
  rung 100.845: nearest OwnWeek LQZ edge Δ0.8p → SILENT
  … (7 rows, one per rung)
  verdict = ALL SILENT → E1 MAP VALID
  journal: rows {invoke, verdict} × 7, chainVerified
```

## E3. A STEP-A rejection (the firewall shape)

```
agent proposes designation {pair: EU, day: Mon, zoneId: "INVENTED-42", …}
gate mpse STEP_A_ZONEID_REAL:
  member("INVENTED-42", zoneMap.zones) → false
  → BLOCKED naming the id + remedy ("use a zoneId from §2 list")
  → agent refines; no crash; journal records the attempt (W-5 class ×73)
```

## E4. A tolerance-split regression (the M1 gate)

```
GOLDEN_ENTRY_TOL card: tolerance = 0.0003 (single declaration)
harness convergence read: same card id
verdict gate read: same card id
any second declaration of entry tolerance → OracleConflictError at compile
DXY LONG Δ2.7p: passes display AND verdict (one constant, both readers)
```

---

# APPENDIX F. GREP-CONTRACT LEDGER (expected outputs filed)

| Contract | Result (this session) |
|---|---|
| specs/mpse foreign markers | 0 (foreign scan on bible §1 = 0) |
| battery fp | 8acfe74f… (battery.json:2 = d17-report.json:2) |
| mutant count | 9 files (measured ls) |
| S-corpus | 437L / 46 blocks (measured) |
| kernel sources | 12 + 9 tests = 2,962L (measured) |
| bible-2 §1 purity | 0 foreign (measured) |
| JESL tree aether-named runtime files | 0 (fusion, not inheritance) |
| registry kinds | 38 rows / 8 families |
| E-lock: Iron Law 12 violations in plan | 0 (every vendored module node-builtin-only) |

---

# APPENDIX G. SESSION TURN LOG (27 explores + authoring, condensed)

Turn-A wave (6): src map / specs-vs-build / functional closeness / LASME 6-doc
absorption (16,157L) / JESL kernel / runtime coupling. Turn-B E2 wave (4):
clean-baseline brief / theatrical forensics (M1–M7, X2) / NON-NEGOTIABLE-RELOAD
(5 files) / graph+spine (1940 nodes verified, stale map, memory-seed map).
Turn-C wave (5): T1 lifecycle (3 copies byte-identical + 7-tool chain + Manual
A–D/Reasoning A·B tables) / 7-doc TTE canon / JESL round-2 (kernel recipe,
trading profile, 28-tag IR, 12 node kinds, driver interface) / mimocode
internals (goal/command/workflow/memory/v1) / V5 specs + OHLC lexicon (6
machines ~150 predicates) + KB-MPSE 12,458L + failures-DB 20,322 rows.
Research wave (3): v3 chip-mask (313L) / embedding mechanics
(workflow-machine 139L) / executor free-vs-build. Authoring: spec §1 (180L) ·
bible-1 (500L) · spec §2 · browser wave (3: TV_Browser_v3 1405L + auth skill +
manager law) · spec §3 · ShowMes (E-Wave 195L, Circuit 130L, Overhaul 213L,
FULL 239L) · bible-2 §§1–3 (1088L) · FULL plan v2. Delivery evidence: every
wc/sha/grep cited in-session.

---

# APPENDIX H. PER-MODULE ARCHITECTURE (the forked engines, transferable law)

## H1. E1 — the lexicon vision engine (29 files, FORK)

Interface: market bars + LMV/OBCV outputs IN; ZoneMap + LexiconVerdict
triplets OUT (no triplet = no classification). Data flow:
MarketDataAdapter (anchorMs temporal gate, FUTURE_BAR_LEAK typed error) →
zoneMapActor + pressureActor (XState v5 context) holding the live map →
6 machines (candle-pressure/shape, zone-classification/pressure,
shape-chain, obvious-trades) scoring 4-bank (descriptive-1/suggestive+1/
substitute+2/use+3, fail-closed, ESCALATION_THRESHOLD 3) → LMV engine +
OBCV engine (bw≥3.0, bf≥0.65; BoM 4H-only; 30m MoM-only) → zone map OUT.
Failure modes: crashing predicate counts AGAINST (never silent pass);
phantom-BoM ALL-4 surface; DEATH_SCOPE [30m,1H], 4H never dies. Battery:
15,000 assertions (500 runs × 5 fixtures × 6 machines) + golden-fixture +
future-bar-leak. Fix surface: the 5 murder-chain items (§8/D2).

## H2. E2 — the state machines (28 files, FORK)

ShapeChainMachine (7 shapes, ZFP-conditioned guards, P(S→S′) forward matrix,
argmax path) · DesignationMachine (OPEN→DESIGNATED→CONSUMED|INCOMPLETE; 4 zone
IDs ONLY, NO price field; D50 side-match, SIDE_INVERSION_VIOLATION) ·
CascadeMachine (requires[]/forbids[]/detectLoop; EU mirrors DXY inverse, GU
reads ACTIVE EU) · ZonePressure + Freshness (event-driven) · MPSE computations
(f(T)=24, divergence≤0.35, zfp ladder min(60,20+floor((battles-3)/2)×5),
totality 90 rows). Failure mode today: E2 advisory (+2 tier bonus) instead of
authoritative (Ef fixes). Tests: designation-totality, mirror-floor,
shape-chain-golden, side-inversion, workflow.

## H3. Card — the assembly contract (7 files, FORK)

zod schema (meta/e1/e2/visuals/reasoning) → assembler (E1→E2→charts→verifier→
reasoning→disk) → provenance (anchor chain per setup) → golden-card.json
reference. Designations carry zone IDs + machineTransitionTrail. Output dir
plutus-cards/ MISSING (W4 gap). Assembly gate: schema-valid + hash pinned.

## H4. Kernel — the trade computer (21 files, FORK)

card-loader (schema+provenance gate) → L1 telescope (zone WHERE) → L2 pressure
(fortress 4+, phantom ALL-4) → L3 fib (1.272/1.618/2.618; reinforcement-only,
deferred from core) → L4 cascade (CASCADE_NO_INVERSE FAIL loud; direction from
DXY, levels from pair) → L5 TI-graph (structural score) → trade-computer
(RRR_FLOOR 2.5; fuses verdicts + full provenance) → report-model/rules/render
(52 rules; TA_CENTER CRITICAL; 6.55in; K-factor Section 1) → journal
(harvest→report causal chain, causationId replay). Report = TS render (W6
recorded TS-ported); python-template port only on fidelity gaps.

## H5. MPSE substrate — the battery (13 files + fixtures, FORK)

S-corpus 437L (7 specs, 46 blocks 1:1) → compile.ts (D13 gate, fp) →
battery.json (46/46, 19C/27E) → oracle-registry.ts (10 pure oracles + 2
composed: mirror_floor, side_match, divergence_le, totality_forall, rrr_floor,
sl_ceiling, sl_min, containment_subset, tf_restriction, no_wall_clock +
shape_gate, near_edge; all pip-quantized, all fail-closed) → fixtures (9
mutants FIRE + golden-week SILENT/evidence) → calibrate.ts (exit 0 =
all-calibrated-or-born-off) → d17-report.json. Consumers read the battery;
none re-declares a threshold (D008).

## H6. The 46-predicate census (tiers, measured)

S-1 cascade 6 (3C/3E) · S-2 totality 5 (3C/2E) · S-3 anchors 12 (7C/5E) ·
S-4 pressure 7 (1C/6E) · S-5 RRR 6 (4C/2E) · S-6 telescoping 5 (0C/5E) ·
S-7 honesty 5 (1C/4E). Total 19C/27E/0F/0B. The 27 evidence-only rows are the
M4 mutant-authoring queue (one mutant each).

## H7. The six layered diagrams (one-line each, full art in ShowMes)

Master ladder: FORK→ENGINES→KERNEL∥HARNESS→MPSE→CONVERGE (FULL plan §3).
Agent/gate/workflow swimlane P0–P7 (§2 of the T1 wave + spec §2A pin shape).
Kernel column: card→L1..L5→compute→report→journal (§2 of the §12C show-me).
E3 gate pseudocode: quantize→compute→discharge→Triplet→chain row.
Battery→circuit emit: one unit per block (D008 1:1).
Goal pin: phases=plan.md, evaluator=receipts, skeptics NOT prose.
(Full ruler-verified ASCII in reports/Plutus_V5_FULL_BUILD_PLAN_ShowMe.md.)

---

# APPENDIX I. BUG LEDGER (all findings, root cause + fix + evidence)

| # | Bug | Root cause | Fix | Evidence |
|---|---|---|---|---|
| 1 | Monday-gold narrowed gate | week→Monday, 21→5 slots between freezes | re-anchor; full-window pinned in goal | forensics M2 diff table |
| 2 | tolerance split 3p/2p | per-gate epsilon | single GOLDEN_ENTRY_TOL card; conflict throws | forensics M1 |
| 3 | +17.84R sums to +16.84R | arithmetic fault in manifest line | re-derive from TTE rows | MANIFEST:8 sum |
| 4 | cap-bound 3.00R SLs | SL = E−(TP−E)/3 on 3/5 lanes | uncapped-survival test standing | TTE lines 9,15,20 |
| 5 | no Friday rule in gold sim | weekend law dropped | Zr-close in sim workflow | diag:665-691 vs report_v452.md:3 |
| 6 | self-sourced SL/TP eval | emissions as oracle | member(projection, oracleRows) gate | diag:693-696 |
| 7 | missing BUILD_REPORT 95KB | claimed, absent | withdraw or produce | checkpoint 6-entry ls |
| 8 | E1 freshness kills fortresses | DEPLETED-at-3 confusion | fortress state fix | D100 |
| 9 | 4H maxBars truncates Jun-22 | maxBars 60 | full window | D100 |
| 10 | OBCV 0-emission 1H/30m | single-candle model | multi-candle | D100 |
| 11 | matrix→zones bridge missing | lives in model.lqzMatrix only | adapter (Ed) | mirror anchor miss |
| 12 | E2 reach cap excludes 1.14460 | cap value | reach config (Ee) | EU Tue Δ27p |
| 13 | E2 advisory not authoritative | +2 tier bonus design | keyZoneId authority (Ef) | spec B.W3 |
| 14 | GU SHORT zero-emission BS/WL | class-locked pool + distribution deadlock | sweep −30 + flexible fallback | D97 class 2 |
| 15 | mpse:calibrate cap unbound | handlers binds {Shell,Fs,Http} only | requiredCaps: [] on new family | handlers.ts:94-98 |
| 16 | raw runProgram auto-PASS | unregistered handle stub | CLI handle-builder only | executor.ts:190-191 |
| 17 | whole-run-only replay | Activities carry synthetic inbound | accept; document as shape | activities.ts:27 |
| 18 | outbound writes on FAIL | kernel open defect | verdict-gated sections only | build report open item |
| 19 | silent-refusal trio | log-only errors | lastError in report JSON | F-001/F-003 pattern |
| 20 | wave-1 "3 trades" claim | mis-anchored report | retracted (file: 32/+25.30R) | report_v452.md:4-13 |
| 21 | "~20/46 born-off" claim | misread report | retracted (exact 19/27/0/0) | d17 keys |
| 22 | computeLmvTP "STALE" tag | manifest claim | retracted (graph verified :2968) | live grep |

---

# APPENDIX J. TESTING LEDGER (runs + verification commands)

| Test | Scope | How | Result |
|---|---|---|---|
| specs/mpse compile | 46 blocks | `bun specs/mpse/compile.ts` | fp 8acfe74f… (measured ×N) |
| specs/mpse calibrate | 46 predicates | `bun specs/mpse/calibrate.ts` | exit 0; 19C/27E |
| frozen pair | 2 files | sha256sum | prefixes match (measured) |
| report determinism | 1 artifact | ×2 runs | f8235815 identical |
| Monday convergence | 5 slots | golden diag | 5/5 at ≤3p (CLAIM tier) |
| full-week | 19 trades | EVIDENCE tail | 11W/8L/0O = 58% |
| battery D17 twins | 9 mutants | FIRE rows | each fires |
| kernel unit tests | 9 files | `bun test src/kernel` | green (carried) |
| e1 battery | 6 machines | properties + golden + leak | 15,000 assertions |
| e2 tests | 6 files | totality/floor/chain/inversion | green (carried) |
| JESL proofs | 43/43 | v3 §0 record | carried (kernel specs) |
| host display | DISPLAY :1 | socket ls | alive |
| chrome | binary | which | google-chrome-stable |
| container image | plutus-container-testing | docker images | ABSENT (blocks container path) |

---

# APPENDIX K. SPEC-MANDATE MAP (operator said → built → evidence)

| Operator said | Built | Evidence |
|---|---|---|
| fork-only-what's-needed, 0 loss | §8 D1 manifest (F1–F5) | fork verdict table §1 |
| E1/E2/E3 = JS workflows | translation table + 7 workflow files (H5) | T1 wave brief |
| TTE = /goal, agent-in-loop | /plutus-pipeline pin on SUPER_GOAL (H4) | spec §2B mapping |
| plutus memory duplicate | 4-file set + hooks + canon store (H2) | seed map (graph wave §6) |
| same substrate as SUPER_GOAL | mapping table, no reimplementation | spec §2B |
| N-tab browser + cookies | manager 16 actions + allowlist (H6, spec §3) | manager-law wave |
| MPSE as embedded nodes | 5 NodeImpls + emit + proof (K1–K5) | bible §12B + Circuit ShowMe |
| exec seam verbatim | plutus-engine tool law (H3) | spec §2A |
| LLM via /v1 tokens | H7 llm-server flow | capability-api wave |
| anti-theatrical gates | tolerance-freeze + counts + window + Friday | forensics M1–M7 mapping |
| journal = wave-db infra | SQLite WAL/busy/withImmediateTx (M3) | wave-db.ts:1-120 (read) |
| patterns not imports | Iron Law 12 + hygiene greps | foreign scans = 0 |

---

# APPENDIX L. DENSITY LOG (this document's own evidence)

- §0–§7 + App A–B: 438 lines (chunk 1–2). App C–G: +201 → 639. App H–L: this chunk.
- Every table row carries a measured number or a file:line from this session.
- Ruling numbers R1–R15: each maps to a verbatim operator sentence in §1.2.
- No [FILL]: every numbered row names a file, a gate, or an expected value.

---

# APPENDIX M. THE 46-PREDICATE TABLE (tiers, row-for-row)

S-1 cascade (3C/3E): side-match C · mirror-floor C · divergence E ·
sequencing-requires E · consumption-forbids E · loop-detection C.
S-2 totality (3C/2E): bounded-forall E · dual-sided E · exists-unique C ·
exhaustiveness-d8 C · golden-instantiation C.
S-3 anchors (7C/5E): lqz-near-edge C · ss-nested-liquidity C · rwl-bs-deep C ·
supply-symmetry E · ladder-steps C · defense-switch E · atr-floor C ·
golden-sl-min C · strength-edge C · opposing-internal E · tp-floor E ·
shape-gating C.
S-4 pressure (1C/6E): lifecycle E · battle-count E · death-scope E ·
fortress E · third-mitigation C · broken-with-battle E · shield E.
S-5 RRR (4C/2E): floor C · target E · ceiling C · min-sl E · consequence C ·
filter C.
S-6 telescoping (0C/5E): nesting E · bom-origin E · 30m-mom-only E ·
lqz-mapping E · hierarchy E.
S-7 honesty (1C/4E): no-wall-clock E · content-hash E · honest-data E ·
no-fabricated E · x2-determinism C.
Kind census: inequality 12 · piecewise 11 · subset 8 · equality 8 ·
recurrence 3 · forall 2 · exists-unique 3 · process 2 (= 46).
The 27 E rows are the M4 mutant queue (one mutant each → 46/46).

---

# APPENDIX N. ORACLE WALKTHROUGH (12 surfaces, condensed)

mirror_floor: actual===expected → VALID else CONTRADICTED (over AND under).
side_match: LONG∧DEMAND / SHORT∧SUPPLY → SILENT else FIRE (D50).
divergence_le: quantized value>bound → FIRE (0.35; quantum 1e-9, pips 1).
totality_forall: {actual,expected} or {count,days,pairs,directions} → VALID iff
equal (90-row designation totality).
rrr_floor: 3 shapes ({rrr,floor} · {entry,sl,tp,floor} computed, zero-risk
THROWS · {claimedFloor,sanctionedFloor} drift detector) at 1e-9.
sl_ceiling: 3 shapes, quantum 0.1, FIRE iff > 36. sl_min: 2 shapes, FIRE iff < 4.
containment_subset: bands + inverted-band refusal + entry-rung sugar.
tf_restriction: closed-set membership (LQZ never 4H).
no_wall_clock: depth-10 cycle-safe key scan → FIRE on timestamp-family keys.
shape_gate (composed): nature-declared side consistency.
near_edge (composed): ROW iff in-band + delta cross-check ±0.05 else THROW +
expectedEntry match. ORACLES const: the frozen ten.

---

# APPENDIX O. GATE CARDS E1–E10 (adoption order + shapes)

E8 hardening (verdict-gated writes, lastError) → E3 exit-2 registry + E6
rollup (FAIL>INCONCLUSIVE>PASS) → E1 journal.ts + E2 run-identity + E9
receipts (wave-db infra: SQLite WAL, busy 5000, withImmediateTx, rows
{sessionId,mode,layer,eventType,prevHash,currentHash}, verifyChain, compact
markers) → E5 tier field + gating-consumer refusal → E4 emit (own wave,
1:1 per block, 7-leg proof) → E7 caps + E10 breaker (3×exit-1 → OPEN).
Zero-dep on all: node-builtins only.

---

# APPENDIX P. THE MPSE CIRCUIT (Shape B embed, condensed)

JESL card (tier 2) carries ONE workflow-machine node whose config.doc holds the
tier-1 MPSE circuit: load(file-io) → mpse-quantize → mpse-compute (28-tag ALU)
→ mpse-oracle (discharge vs expected, FAIL carries delta) → journal-sink.
Registry-truth children (D27), depth ≤3, caps one-way, budget {600s,15},
worst-wins rollup, TOTAL journal coverage (runId parent:wf:node:depth).
Fixtures: golden-week SILENT + 9 mutants FIRE (manufactured vectors).
New kinds: mpse-{gate,compute,oracle,quantize,mux} in ALL_KINDS (deterministic),
requiredCaps [], profile mpse tier-1. Macro sees ONE node; the die trace sees
every micro-gate. Full art: reports/MPSE_Circuit_ShowMe.md; research:
bible §12B.

---

# APPENDIX Q. T1→GOAL TRANSLATION (7 tools → pin phases)

harvest tool → e0-harvest workflow · Manual A (options PNG) → P-agent turn ·
zones tool → e1-zones · Reasoning-A → designations→gate · shapes tool →
e2-shapes · Reasoning-B → T8/T10/T11→W-1..W-7 loop · charts tool → visual
workflow + agent-reads-PNGs · setups tool + placed → e3-kernel cast
(runId idempotent; re-cast replays) · gate tool (G1–G10) → golden gate +
judge stop · PipelineRunContext global → per-run workflow scope + journal
(session-scoped; fixes the weekStart-only clobber). Chaining: Option C
output-contracted (nextStep text + args firewall); A unbuilt, B rejected.

---

# APPENDIX R. BROWSER ENGINE (measured deltas)

v3: 38 tools (36 + desktop/container), CDP 9333 (doc string 6930 stale),
DISPLAY :1, profile PLUTUS_PROJECT_DIR-driven, base64-only screenshots,
loggedIn:true HARDCODED (untrusted). Manager: 16 actions, session SQLite,
3-layer observation w/ cursor law, 17-code errors, GPU flag law, renderer
zombie probe, display recovery wired, tab→symbol map, layout restore, cookies
SHA manifest, auth-bridge. CDP unification: 6930+9228 planes collapse under
the manager; tv-chart-controller re-points. Host now: desktop viable,
container blocked (image/volume absent).

---

# APPENDIX S. FAILURE-DB CLASSES (20,322 rows → gate seed)

SHADOW_DEGRADE 10,919 (projectForward 5,911 + anchor 5,008; UNAVAILABLE then
EMPTY) · GROUNDING_WARN 8,913 (RRR_BELOW_GATE 3,410 at e.g. 1.59<2.5;
MACRO_DIVERGENCE 1,840; ADM_REJECT + NO_STRUCTURAL_TP 909 each;
DEGENERATE_TP_CAP_FAILED 702; W-1_NUMERIC 620; CONTRACT_VIOLATION +
W-3_ORDER 213 each; W-5_INVENTED-IDs 73; W-4/W-6 12 each) ·
REFINEMENT_EXHAUSTED 399 (attempts=4, RRR-dominated) · MACRO_DIVERGENCE 91
(GU Mon SHORT 80/91: "macro wins, divergence recorded never suppressed").
Pair split: EU 7,153 / DXY 6,994 / GU 6,175. Week 2026-07-06 99.7%. Attempts=1
in 17,853. Component = designation slot (Mon 92% — designation-totality
priority SC-6). Gate mapping: 5H table in the cards bible.

---

# APPENDIX T. JESL ABSORPTION LEDGER (what the waves proved)

W0–W10 CLOSED per build report (336/336 tests, 109 .ts, tree digest
681bf8696924a040) + EST-1 P1/P2 (487/487) + v1-machine layer (473/473 vitest,
4 proofs). Executor: inbound⊆written readiness, batch ≤15, Effect.exit
isolation (typed→FAIL, defect→INCONCLUSIVE), no-overall-verdict (rollup in
jesl-run: FAIL>INCONCLUSIVE>READY_FALSE>PASS). Caps: Context.Tags +
boundCaps string fast-path; pre-fire CAP-UNBOUND whole-run. Channels:
seedFrom vars, via routing, {ok:1} defaults; NO-SEED/CHANNEL-UNSET loud.
JeslRun: runId=hash(docHash+\0+seed)[:16], verify+covers replay invoked:0,
receipt {runId,verdict,rowsCount,journalTail}. Registry: ALL_KINDS 38 rows/8
families, stubs INCONCLUSIVE TODO-anchored, replaceStubSync append-only,
getRegisteredImplSync single truth, isKnownKind schema-driven. Bracket:
contract required, repair literal ≤2, floor 0.55 default/0.85 spec.
Known defects carried: outbound-writes-on-FAIL (adopt inverse); silent trio
(surface lastError); compiler.ts divergence; kind-count drift.
Adopt: PATTERNS, never imports (Iron Law 12).

---

# APPENDIX U. SESSION PROVENANCE (this handover's own chain)

Orders executed this fire in order: (1) migration cp -r + diff -r CLEAN +
fidelity wc (2,726L total) — event T4 done; (2) handover chunks 1-4 (this
document); (3) next: engineering report v1 (T2), then pack+verify (T3).
Memory: ses_-ffe5f73f384beffeg7537uiYT checkpoint 108L staged the sequence;
this fire consumed it. Skills: handover-package (skeleton 109L, anatomy 72L,
packer CLI measured) + engineering-report (structure, naming law). Confirmed
deviations: ship path = JARVIS home (--out override, R10); 4 ShowMes + report
as --adjacent (04_ADJACENT); SUPERSEDED_NOTES.md recommended, not yet authored.

---

# APPENDIX V. PER-MODULE VERIFICATION TABLES (gate shapes per file)

## V1. compile.ts (270L) — the D13 gate

| Check | Anchor | Expected |
|---|---|---|
| header regex | :76 | `^#\s+(S-\d+)\s+—\s+(.+)$` |
| spec/header agreement | :88-91 | equal or throw |
| form vocabulary | :28, :92-94 | piecewise\|forall\|predicate-family\|process |
| block vocab | :29-32, :113, :147-150 | 8 BLOCK_KINDS |
| duplicate-key refusal | :121-127 | throw naming file+block |
| D13 quote gate | :130-137 | non-empty `"…"` or D13_VIOLATION |
| D13 anchor gate | :138-146 | every part doc:line or throw |
| fp determinism | :10-14 | alphabetical, blocks in order, no timestamps |

## V2. oracle-registry.ts (394L) — the ten + two

mirror_floor :75-93 (VALID iff ===) · side_match :95-106 (D50) ·
divergence_le :108-122 · totality_forall :124-153 (90-row form) ·
rrr_floor :155-182 (3 shapes, zero-risk THROW) · sl_ceiling :184-209 ·
sl_min :211-231 · containment_subset :233-273 (inverted-band THROW) ·
tf_restriction :275-289 · no_wall_clock :291-325 (depth 10, seen-set) ·
shape_gate :327-340 · near_edge :342-379 (delta ±0.05 cross-check) ·
ORACLES const :381-392.

## V3. calibrate.ts (711L) — the D17 harness

Exit contract :4-7 (0 = all-calibrated-or-born-off) · class dispatch :10-12
(12 classes) · fixture riders :12-14 (sanctioned IN data) · FALLBACK :48-59
(logged to stderr) · founding control :19-22 (synthesized, never literal) ·
Resolution kinds :86-89 · EvalRow :91-98 · imports the 11 oracle fns + 2
composed :38-41.

## V4. trade-computer.ts (301L) + l4-cascade.ts (174L)

RRR_FLOOR 2.5 :13 · verdict interfaces :16-29 · provenance (7 id fields) ·
L4: CASCADE_NO_INVERSE FAIL loud :6-7 · GU←ACTIVE-EU :133 · missing-inverse
row :151.

## V5. report-rules.ts (158L) — the 52

Rule rows 1–11 verbatim :57-67 (notation/table bands; rule 9 CRITICAL center;
rule 10 6.55in; rule 8 4dp precision) · section-order check :47-51 ·
per-rule check fns (:57: `section 1 absent` shape).

## V6. wave-db.ts (167L) + evidence-store.ts (175L) — the journal model

WAVE_DB_PATH env→test→home :12-14 · schema 6 tables :21-64 · getWaveDb
WAL+busy :86-94 · withImmediateTx :103-120 · single-writer law :4.
Evidence rows :5-46 · verifyChain :77-95 · compact marker :48-75.

## V7. workflow-machine.ts (139L) — the embed surface

sub-doc :27-35 · depth cap :41-45 · D27 registry-truth :69-86 · child ctx
:87-101 (runId parent:wf:node:depth :91; caps one-way :99; budget :101) ·
rollup :130-135 · journal via executor :107-134.

---

# APPENDIX W. THE E-WAVE ROWS (bible §2 order, shapes)

E8a verdict-gated writes / E8b lastError / E3 exit-2 registry / E6 rollup
FAIL>INCONCLUSIVE>PASS / E1 journal.ts + E2 run-identity (SQLite WAL,
busy 5000, withImmediateTx, chain rows, verifyChain, compact markers) /
E9 receipts (runId, verdict, chainVerified, counts) / E5 tier field +
gating-consumer refusal / E4 emit (own wave, 1 unit per block, 7-leg proof)
/ E7 caps pre-check / E10 breaker (3×exit-1 → OPEN). Zero-dep throughout.

---

# APPENDIX X. SESSION TURN MAP (condensed archeology)

A: 6-agent absorption (src/LASME/JESL/runtime) → status + runtime audit.
B: E2 wave (4): baseline table / theatrical forensics M1–M7+X2 / RELOAD
doctrine / graph (1940 verified) + spine law.
C: macro report → T1 lifecycle found (3 identical copies + 7-tool chain) →
7-doc TTE canon → JESL round-2 (kernel recipe, trading profile, IR, driver)
→ mimocode internals (goal/command/workflow/memory/v1) → V5 specs + OHLC
(6 machines) + KB-MPSE + failures-DB (20,322).
D: architecture delivered + §1 preserved (180L, Lvap→Lmv fixed) →
bible-1 500L (§1 done, §2 gated) → spec §2 (seam+substrate) → browser wave
(TV_Browser_v3 1405L, 38 tools; auth skill; manager law) → spec §3 → bible-1
show-me EXPLAIN → CST2 bible (E1–E10 §2 + MPSE-Circuit §12B) + MPSE show-me →
circuit→kernel→report show-me → §12C preserved in bible.
E: status report → exact plan → FULL plan v2 → THIS handover order (staged
by writer, executing as main agent): migration → dump → report → zip.
