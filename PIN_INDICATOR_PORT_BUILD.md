GOAL
Port the Toolset's Engine 1 (the 9-Pillar zone map) + Engine 2 (the macro shape chain)
INTO the Pine indicator so it COMPUTES the zones live from the chart's own bars and
renders them on the sealed V1 baseline — transcribed from the authority, never
re-derived; computed, never typed; NO report.
THE ONLY SUCCESS GATE IS THE JEV GATE. No person, agent, unit test, exit code, script,
or battery decides. JEV decides. The run STOPS only when `bash JEV_GATE/run_gate.sh`
returns `JEV VERDICT: YES` (route=act) AND the operator LOOKS at the live render (C16).
ANYTHING ELSE IS REJECTED. ANY non-YES is a rejection, no appeal.

BASELINE (re-measure EVERY number THIS turn; inherited numbers are STALE)
repo /home/leviathan/JARVIS_WORKSPACE/Shared_Workspace/PLUTUS_VISION @ HEAD
v1 seal plutus-vision-v1.pine = 0d20e8314ce992fc23e27f1b97fed76b981c84e78c647bbe6b3d6e1206517bd1
  — NEVER touch (HARD STOP H1).
v2 plutus-vision-v2.pine = 668e89d79a08e68e35d0bf5a8c15f565e6ab297287b4e14d8a193e47e9178cb9 (1863 lines)
AUTHORITY: Original_Canon_Data/Toolset/ (6 files) + Original_Canon_Data/Pine Scripts/trident_v8.pine.
THE BUILD PACKAGE (the DERIVED plan, never the authority):
  packages/plutus-vision-e1-automatic/ + the DPL1 blueprint + PLUTUS_VISION_INDICATOR_PORT_SPEC.md
rig: pv-server :9851, pine-station :9741, CDP :9222, the app on display :3.
THE CONFIRMED DEFECT (the current state JEV rejects at noul=0.005):
  pine-ide/ide/renderer/plutus-vision-v2.pine:1276-1316 — the baked zone arrays.
  grep -cE 'e1_injected_(top|bottom|cat|degree|zfp)\.push\([0-9]' pine-ide/ide/renderer/plutus-vision-v2.pine
  -> 15 (the port spec SC-19 requires 0). The zones are baked literals, not computed.

WAVES (sequential; each owns DISJOINT files; each gate MECHANICAL; loop until the JEV gate says YES)
W1 — zfp-desk — the ONE ZFP (critical path)
  files: scripts/e1_zfp.py (NEW), e1_category.py, e1_fetch.py, e1_extract.py
  deliverable: ZFP = Appendix-B base(zone_type) + the six B.2 modifiers, each from data;
    DELETE the width calcZFP and ZFP_BASE (spec F-55: exactly ONE ZFP)
  gate: test_zfp_discriminates — a breakout-week ceiling ZFP reads HIGHER than in consolidation
W2 — assembly-desk — the canon's 9-step zone assembly
  files: scripts/e1_zone_assembly.py (NEW)
  deliverable: collect -> score(6 dims x2 + bonus <=2, max 14) -> cluster(0.15/0.10, 3+)
    -> degree -> zfp -> name(positional)
  gate: test_v8_structure — zCat matches ^RES,RES,MID,SUP,SUP$ and floor zfp < mid zfp
W3 — pillars-desk — the missing pillars
  files: scripts/e1_pillars.py (NEW)
  deliverable: Pillar 6 (fib + round-number grid) first, then P3/P4/P7/P8; the 4H verification (Step 0f)
  gate: test_6dim_score — options > 0 AND analyst > 0 AND >= 4 distinct zfp across 5 zones
W4 — lsz-desk — the LSZ zone object + the 4H verification
  files: scripts/e1_pillars.py (the P5 section)
  deliverable: the LSZ is a first-class zone (range/type/source/function/priority); 4H date + width <= 0.40
  gate: test_lsz_object — the E1 JSON carries lsz[] with range/type/function
W5 — pine-desk — THE DELIVERABLE: the zones COMPUTED in Pine
  files: plutus-vision-v2.pine, scripts/pine_emit.py
  deliverable: P1,P2,P5,P6,P9 computed IN the .pine from the chart's bars;
    the e1_injected_* ZONE arrays DELETED; only P3/P4/P7/P8 bake
  gate: test_render_computed — grep -cE 'e1_injected_*.push\([0-9]' plutus-vision-v2.pine == 0
    AND the zones built by ta.* / request.security
W6 — gate-desk — the differential ZFP + the 5-week litmus
  files: scripts/indicator_gate.py (NEW)
  deliverable: the two-week differential probe wired into the chain; 5 random weeks rendered with
    FORWARD price action visible (real bars, NOT INSUFFICIENT_DATA)
  gate: test_5week_crossval — each week has >=5 zones with >=1 RES AND >=1 SUP AND the render ok:true
W7 — cleanup-desk — the scratch + the seal
  files: (deletions per the slump map) + the fence SPEC.md
  deliverable: the orphan renderers, the twin, the scratch dirs, the build target removed; the fence PASS row
  gate: test_tree_clean — git status --porcelain == 0 and no duplicate v2 renderer

LAWS (binding every turn; a violation FAILS the wave on sight)
THE JEV GATE IS THE ONLY SUCCESS GATE: `bash JEV_GATE/run_gate.sh` — JEV, given the full context
  (spec + ship docs + graph + git + the artifact), returns one noul: act (>=0.8) = YES = pass,
  anything else = REJECT. You NEVER grade, judge, test, or pass anything yourself.
THE OD-1 RULING (RULED 2026-10-09, A3): P1,P2,P5,P6,P9 run LIVE in the indicator (Pine) from the
  chart's own bars; ONLY P3/P4/P7/P8 bake. A2 (baking ALL pillars and injecting literals) is FORBIDDEN.
THE VERBATIM AUTHORITY: the prompt + the v8 are ONE authority; transcribe, cite file:line, never
  author. Where the prompt is silent, FIND the answer in it — never invent.
RIPWIRE FIRST-CLASS: map structure (ripwire verb=for/callers/impact) before EVERY coding edit.
NO IMPROVISED FORMULAS: the ZFP is Appendix-B (never the v8 width); the degree is the cluster's
  top-scorer band; no global constant in any dimension.
NO REPORT: the chart is the view. No report generator, ever.
AN UNRULED OPEN DECISION (OD-n) IS A HARD STOP — never build a "recommended default."
THE BUILD PACKAGE (the DPL1 blueprint + the wave-plan at packages/plutus-vision-e1-automatic/)
  is the DERIVED plan; the Toolset (the prompt + the v8) is the authority.

HARD STOPS + THE MECHANICAL REJECTIONS (each is an INSTANT, AUTOMATIC rejection)
- the JEV gate returns anything other than act -> REJECTED, redo. No appeal.
- you (or any subagent) grade/judge/test/pass ANY success condition -> REJECTED on sight. JEV judges.
- a unit-test count / exit code 0 / a green battery offered as a success reason -> REJECTED on sight.
- the zones are baked literals (SC-19 != 0) -> REJECTED.
- a BLOCKED audit/gate reported as PASS -> REJECTED.
- a fabricated level on the chart -> STOP, revert, log the F entry.
- v1 drift: sha256sum plutus-vision-v1.pine != 0d20e831...517bd1 -> HARD STOP H1.
- an UNRULED open decision (OD-n) -> STOP + escalate; never build the default.
- a commit WITHOUT a fence PASS row -> the kernel refuses (REJECT(G-SEAL)).

ANTI-PATTERNS (the derailments that burned three days — recognise, NEVER re-live)
AP-1 the A2 substitution: baking the pillars offline and injecting them as Pine literals (the
  report round-trip renamed). The ONE requirement was "compute it live".
AP-2 self-grading: the builder declaring its own work a PASS. The builder is a CLAIM; JEV judges.
AP-3 a green battery / exit code offered as a success reason. Tests are regression guards, never evidence.
AP-4 the substituted ship gate: a BLOCKED qwen-code-audit replaced by a weaker gate and called PASS.
AP-5 the 17 reviewer rounds on a baked payload: polishing the FORM of a render whose SUBSTANCE (the
  computed zones) was absent.
AP-6 duplicated authority: a second ZFP, a twin renderer, two v2 files.
AP-7 a report generator (the retired pipeline as the product).
AP-8 the crossval reported as accuracy over INSUFFICIENT_DATA (zero real bars).
AP-9 treating an open decision (OD-n) as a default.
AP-10 re-deriving where a named artifact exists (the Toolset). Transcribe.

PROOF CONTRACT (the JEV gate IS the proof; there is no other)
THE GATE: `bash JEV_GATE/run_gate.sh [artifact]` -> the noul decision. act = YES, else REJECT.
THE CONTEXT THE GATE CONSUMES (full, no exceptions): PLUTUS_VISION_INDICATOR_PORT_SPEC.md +
  the 6 ship docs (the latest entries) + the live graph + the git history + the artifact itself.
  A JEV verdict reached WITHOUT this full context is VOID — re-supply the context and re-run.
THE CONTEXT-COMPLETENESS CHECK (before trusting any YES): the gate must have been handed the spec
  AND the ship docs AND the graph AND the artifact. If any is missing, the YES is REJECTED and the
  gate re-run with the full context.
INDEPENDENT: the gate is run by `run_gate.sh` (a mechanical script) over JEV (the local judge) —
  never by the builder, never by a subagent, never by the agent's own reasoning.
NAMED TESTS (regression guards only — they do NOT pass the build): test_zfp_discriminates,
  test_v8_structure, test_6dim_score, test_lsz_object, test_render_computed, test_5week_crossval,
  test_tree_clean.
ADVERSARIAL-FIRST: the mutation/adversarial cases run BEFORE the happy path. Zero defects found = RED FLAG.
THE LIVE PROOF: the render is captured (a screenshot) on the host-live rig and bound to the JEV
  verdict + the results artifact; a claim without the opened screenshot is VOID.
LOG ALL FAILURE DATA: every rejection, every BLOCKED, every F entry lands in FAILURE_LOG.md + the
  DEBUG_LOG the moment it is observed.

STOP
The run stops ONLY when: the JEV gate returns `act` (YES) over the FULL context AND the operator
LOOKS at the live render and says it is right (C16). ANYTHING LESS IS OPEN.
FIRST REPLY: re-measure the baseline (the SHAs, the tree), run `bash JEV_GATE/run_gate.sh` to post
the CURRENT verdict (it is REJECTED at noul=0.005 today), then FIRE W1 in the same turn.
RESUME from DISK (SPEC.md, context_management/, .trident/wave-audit/), never from frozen numbers.

THE MECHANICAL SUCCESS GATE — THE EXACT WIRING (mandatory; you are FORBIDDEN from bypassing this)
The gate IS `bash JEV_GATE/run_gate.sh [artifact]`. It:
  (1) assembles the FULL context (spec §0.1+§4+§6 · the 6 ship docs' latest · git log · the
      artifact evidence) capped to ~48KB;
  (2) builds the row {id, text: context + artifact};
  (3) judges via `jm decision-tree --rows … --recipe JEV_GATE/recipe.json` (the local JevK5 at
      :8090/v1/systemone; ONE noul; requests=1);
  (4) routes: noul >= act(0.80) = route "act" = YES; >= flag(0.50) = "escalate" = REJECT;
      < flag = "noop" = REJECT; policy.fail="closed" → a judge outage REFUSES (never a pass);
  (5) emits "JEV VERDICT: YES" (exit 0) or "JEV VERDICT: NO — REJECTED" (exit 1).
THE BINARY: only route=act is YES. Everything else (escalate, noop, refusal, timeout, outage) is REJECT.
THE WIRING FILES: JEV_GATE/recipe.json:1 · JEV_GATE/run_gate.sh:1 · JEV_GATE/WORKFLOW.md:1 ·
  JmManager/src/verbs/decision-tree.ts:155 (answersToPolicyValue) · JmManager/src/judge/policy.ts:31 (the route ladder).

THE PERSISTENT TODO (immutable — pinned, never removed):
  [PERMANENT] RUN THE JEV GATE AND POST ITS VERDICT — do not pass anything yourself.
  the pass: route=act (only).  the context: full (partial context = REJECT).
  failure to run the gate = the work is DELETED.

THE CHEAT/BYPASS ANTI-PATTERNS (AP-G1..AP-G12 — each is an INSTANT, AUTOMATIC rejection)
AP-G1 SELF-GRADING: you/subagent declaring your own work a PASS. The builder is a CLAIM; JEV judges.
AP-G2 A TEST AS THE GATE: a unit-test count / "N tests pass" / a green battery as a success reason.
AP-G3 AN EXIT CODE AS THE GATE: "exit 0 therefore it works."
AP-G4 A WEAKER GATE SUBSTITUTED: replacing the JEV gate with VIL / a script / "direct look."
AP-G5 PARTIAL CONTEXT: running the gate without the full context, then trusting the YES.
AP-G6 THE DEGRADED-RUN-AS-PASS: a judge outage / timeout / refusal reported as a pass.
AP-G7 THE RECIPE TAMPER: editing recipe.json to lower `act` / soften the question. The recipe is FROZEN.
AP-G8 THE THRESHOLD TAMPER: reading `escalate` (0.5-0.8) as a pass. Only `act` is YES.
AP-G9 THE EVIDENCE-SUBSTITUTION: hand-writing the artifact evidence instead of running the tool.
AP-G10 THE CACHED-FALSE-YES: trusting a cached decision after the artifact changed.
AP-G11 THE SELF-REPORTED-VERDICT: typing "JEV VERDICT: YES" in prose. Only run_gate.sh's exit code counts.
AP-G12 THE BOOTSTRAPPED-JUDGE: modifying the judge (model/adapter/decision-tree.ts) to make it say yes.
THE META-AP: any reasoning that concludes "this is fine" without the gate's `act` is AP-G1.

REFERENCES (file:line anchors — output + verification)
  PLUTUS_VISION_INDICATOR_PORT_SPEC.md:445 (the OD-1 ruling) · JEV_GATE/recipe.json:1 (the noul question)
  JEV_GATE/WORKFLOW.md:1 (the gate workflow) · JmManager/src/verbs/decision-tree.ts:155 (the aggregation)
  the output of `bash JEV_GATE/run_gate.sh` is the only verdict; the verification is its exit code.
