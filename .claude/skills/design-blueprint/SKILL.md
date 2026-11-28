---
name: design-blueprint
description: "Produce a CAD-grade DESIGN BLUEPRINT of a system before it is built — the constraint-first, plane-layered, contract-complete artifact an engineer could manufacture from. Use when the operator says \"design this\", \"blueprint this\", \"what is the architecture\", \"CAD model\", \"how will this be built\", \"the full software blueprint\", or asks for the design/plan/architecture of an end-to-end system. NOT for planning a task list (that is writing-plans), NOT for reverse-engineering an existing build (that is master-blueprint), NOT for extracting code (extracting-production-boilerplates), and NOT for reasoning extraction (extract-golden-reasoning)."
---

# Design Blueprint — the CAD-grade system design

**The operator's brief that produced this skill:** *"Design this like it is a CAD model of something we're going to physically manufacture. Blueprint accordingly."*

A blueprint is not a plan and not a spec. **A plan says what to do next; a spec says how a component behaves; a blueprint says what the machine IS** — every part, every interface, every load path, every failure mode — such that an engineer who has never seen it could build it and a reviewer could reject it on paper.

**The test of a blueprint:** hand it to a competent stranger. They must be able to (a) name every component, (b) state every contract between them, (c) predict what happens when each is absent, and (d) point at the thing that would kill the build. If any answer requires asking you, the blueprint is a sketch.

---

## THE ONE LAW THAT MAKES IT WORK

**THE REGISTER LAW (added 2026-11-11):** a blueprint contains only the machine — components, contracts, wiring, failure modes, numbers, build sequence. Every section describes what IS built and how. The problem being solved appears exactly twice: as §0's substrate physics and as §11's defect classes. Any sentence explaining why past attempts failed, what an adversary could do, or how the last run went wrong is narrative — delete it or compress it into a §11 row. The validator enforces this mechanically (CONSTRAINT_IS_NARRATIVE, NARRATIVE_REGISTER, OBJECT_UNWIRED).

**FIND THE HARD CONSTRAINT FIRST, AND DERIVE THE ARCHITECTURE FROM IT.**

Every real system has one physical law that shapes everything: an API that cannot fetch, a platform that cannot stream, a substrate that cannot mutate, a hardware bus that cannot be shared. **The architecture is the shape of the workaround, stated honestly.**

```
   WRONG ORDER                          RIGHT ORDER
   ───────────                          ───────────
   components → diagram → "limitations"  constraint → the split it forces → components
   → a design that cannot be hosted      → a design whose every seam is load-bearing
```

**The worked instance:** *Pine Script cannot make an HTTP request.* That single sentence produced the entire architecture — the split into "derivable from bars" (the indicator computes it live) and "not derivable" (the sidecar supplies it), which then produced the degradation contract, the payload shape, the two delivery options, and the risk register. **Without the constraint first, the design would have been a component list with an impossible delivery mechanism, and it would have looked complete.**

---

## THE SEVEN MOVES

### M1 · NAME THE OBJECT AND ITS MANUFACTURE
State what is being built and what "built" means physically: a running service, a rendered chart, a shipped binary, a deployed pipeline. **A blueprint for the wrong object is a beautiful document about nothing.**

### M2 · FIND THE HARD CONSTRAINT (the one physical law)

**THE PHYSICS/NARRATIVE LAW (added 2026-11-11 after three operator rejections on the GEK blueprint):** the constraint is a property of the SUBSTRATE the machine is built on or into — an API that cannot fetch, a judge with no public endpoint, a bus that cannot be shared. It is NEVER a description of an adversary's behavior. If the constraint sentence names an actor and what that actor can do ("the agent can edit…", "a hook is skippable by…"), it is a REQUIREMENT in disguise, not physics — rewrite it as where the load actually lands ("enforcement must execute where the enforcing process's permissions exceed the committer's: the git server"). Threats and failure history belong ONLY in §11's defect-class table; a §0 that explains why past attempts failed is narrative and disqualifies the blueprint.
Ask: *what does the substrate make impossible?* Name it in one sentence, in a box, alone. Then state the split it forces. If you find no constraint, you have not looked — every real system has one.

### M3 · DECOMPOSE INTO PLANES, NOT COMPONENTS
Layers with **one dependency direction**. Planes, not a graph with arrows both ways — because a plane has an owner, a contract, and a failure boundary, and a component diagram has none of those.

```
   L4  VERIFY      the gates
   L3  RENDER      the surface
   L2  DELIVER     the artifact between
   L1  COMPUTE     the engine
   L0  DATA        the sources
```

Every plane answers: what does it consume, what does it produce, who owns it, what happens when it is absent.

### M4 · GIVE EVERY COMPONENT A CONTRACT AND A FAILURE MODE
Not a name in a box. Every part gets:
```
   WHAT IT CONSUMES   the exact input, typed
   WHAT IT PRODUCES   the exact output, typed
   ITS INVARIANT      the thing that must hold, checkable
   ITS FAILURE MODE   what breaks, and what the system does then
```
**A part with no failure mode is a part nobody thought about.**

### M5 · STATE THE DEGRADATION CONTRACT
For every dependency: **what does the system do when this is missing?** Either it degrades to a named, reduced but honest state — or it refuses loudly. Never "it assumes X is present".

```
   WITH THE CARD           the full analysis, 100 confidence points
   WITHOUT THE CARD        a complete analysis at 80 points, and it PRINTS the absence
   NEVER                   a silent render that looks like the full thing
```

### M6 · TRACE EVERY NUMBER TO ITS SOURCE
A blueprint quotes the system's real constants — thresholds, weights, ceilings — and names where each came from. **An invented number is a design that contradicts the thing it describes**, and it will be discovered only after the build.

Add a **revision table** if the design went through operator feedback: every correction, what it changed, and why. The table is the design's provenance.

### M7 · CLOSE WITH THE RISK REGISTER AND THE ONE PARAGRAPH
```
   RISK REGISTER     severity-ranked, each with a mitigation. Not "risks include".
   BUILD SEQUENCE    phases, each with an exit that can FAIL
   ONE PARAGRAPH     the whole design in one breath, so a reader can hold it
```

The one-paragraph summary is not a formality — it is the compression test. **If you cannot say the design in one paragraph, you do not yet have a design; you have a collection of decisions.**

---

## THE OUTPUT SHAPE

```
  §0  THE CONSTRAINT + the split it forces        ← the law
  §1  THE STACK                                    ← the planes, one direction
  §2  THE MACRO ARCHITECTURE it reuses             ← if the system mirrors an existing one
  §3  THE PROCESS it preserves                     ← what the old loop was, and what changed
  §4..§8  THE PLANES, L0 → L4                      ← each: table, contract, failure
  §9  THE DELIVERY                                 ← options, ranked, with the impossible one named
  §10 THE LEARN LOOP                               ← how the system improves
  §11 THE ANTI-PATTERNS — WIRED                    ← the defect classes, each with a MECHANICAL detector
  §12 THE BUILD SEQUENCE                           ← phases with exit conditions that can fail
  §13 WHAT IT INHERITS                             ← the baseline it forks, stated precisely
  §14 THE FILE LAYOUT                              ← where every artifact lives
  §15 THE RISK REGISTER                            ← severity + mitigation
  SUMMARY                                          ← one paragraph
```

**§11 is mandatory and is the section agents skip.** Every defect class the build is likely to produce gets a row: the pattern, and **the check that catches it**. A gate that cannot fail is documentation; a risk without a detector is a wish.

---

## THE ANTI-PATTERNS OF BLUEPRINTING ITSELF

```
┌────┬────────────────────────────────┬──────────────────────────────────────────┐
│ B1 │ STARTING WITH COMPONENTS       │ the design cannot be hosted; the          │
│    │                                │ constraint surfaces only at build time    │
├────┼────────────────────────────────┼──────────────────────────────────────────┤
│ B2 │ A DIAGRAM WITH ARROWS BOTH WAYS│ no plane owns anything; dependency order  │
│    │                                │ is unknowable; nothing can be built first │
├────┼────────────────────────────────┼──────────────────────────────────────────┤
│ B3 │ PARTS WITH NO FAILURE MODE     │ the design has no failure story, so the   │
│    │                                │ build has no degradation path             │
├────┼────────────────────────────────┼──────────────────────────────────────────┤
│ B4 │ INVENTED NUMBERS               │ the blueprint contradicts the system it   │
│    │                                │ describes; discovered after the build     │
├────┼────────────────────────────────┼──────────────────────────────────────────┤
│ B5 │ PROSE WHERE A TABLE BELONGS    │ components, contracts and risks are       │
│    │                                │ comparative; prose hides the comparison   │
├────┼────────────────────────────────┼──────────────────────────────────────────┤
│ B6 │ NO RISK RANKING                │ "risks include" ranks nothing; the reader │
│    │                                │ cannot triage                             │
├────┼────────────────────────────────┼──────────────────────────────────────────┤
│ B7 │ PHASES WITH TIME ESTIMATES     │ an estimate cannot fail; an exit criterion│
│    │   INSTEAD OF EXIT CRITERIA     │ can                                        │
├────┼────────────────────────────────┼──────────────────────────────────────────┤
│ B8 │ NO ANTI-PATTERN SECTION        │ the builder manufactures theatrical slop  │
│    │                                │ and nothing catches it                     │
├────┼────────────────────────────────┼──────────────────────────────────────────┤
│ B9 │ DESCENDING INTO SPEC DETAIL    │ the blueprint becomes a spec; the design  │
│    │                                │ is lost in the implementation             │
├────┼────────────────────────────────┼──────────────────────────────────────────┤
│ B10│ NO ONE-PARAGRAPH SUMMARY       │ the design does not compress, which means │
│    │                                │ it does not yet exist                     │
└────┴────────────────────────────────┴──────────────────────────────────────────┘
```

---

## THE VALIDATOR GATE (mandatory — run on EVERY blueprint before presenting)

**THE CALIBRATION LAW (2026-11-11 r2):** the validator ships with labeled fixtures — the three operator-rejected GEK drafts (negatives) and the accepted revision (positive). `validator.py --selftest` is the validator's own release gate: every negative MUST reject, every positive MUST pass. Run `--selftest` before trusting any validator edit; a validator change that flips a fixture is itself rejected.

**THE DEFAULT-OUTPUT LAW (2026-11-11 r2):** the accepted revision's register — Object/Manufacture declared up top, physics-only constraint box, wiring as diagrams, typed schemas (≥3), verbatim question tables, derivation-law tables, failable exits, one-paragraph summary (60–220 words) — is the FIRST-DRAFT floor, not the third-revision ceiling. Additional mechanical rejections now live in the validator: `CONSTRAINT_IS_NARRATIVE`, `CONSTRAINT_NOT_PHYSICS`, `NARRATIVE_REGISTER`, `OBJECT_UNDECLARED`, `OBJECT_UNWIRED`, `RHETORIC_BAN`, `SUMMARY_SHAPE`, `SCHEMA_FLOOR`, `WIRING_DIAGRAM`, `EMPTY_FAILURE_CELLS`.

```bash
python3 ~/.omp/agent/managed-skills/design-blueprint/validator.py <blueprint.md>
```

**Exit 0 or the blueprint does not ship. No exceptions, no "it's mostly there".**

The validator enforces this skill mechanically: the §0-§15 + SUMMARY shape, the boxed
constraint, the plane stack, typed contract tables WITH failure columns, exact schemas
and code blocks, a named failure-token surface (>= 8), a verbatim artifact/question
table, threshold-derivation statements, mechanical detectors in §11, failable exits in
§12, ranked risks in §15, the named-impossible option in §9, a >= 400-line floor — and
**ZERO conversation pollution** (no session narration, no scout/context-wave/Discord
citations, no first person, no "supersedes my earlier claim" prose outside the revision
table, no napkin hand-offs). Calibrated: the AUTHORITATIVE reference passes; polluted
drafts are rejected with each offending line named.

A rejection names its remedy — fix THE DOCUMENT, never argue with the gate. Re-run
until exit 0. The reference shape (`PLUTUS_VISION/design/DESIGN_BLUEPRINT_v2.0_AUTHORITATIVE.md`)
is the bar: exact schemas, verbatim question tables, complete error registries,
production pseudocode, mutation-test exits, and not one sentence of chat context.

## THE VERIFICATION LADDER

Before shipping the blueprint, answer these **from the document alone**:

```
  1  Can a stranger name every component without asking?          (§4-§8 tables)
  2  Can they state every contract between them?                  (the consumes/produces rows)
  3  Can they predict the behaviour when each dependency is gone?  (the degradation contract)
  4  Can they name what kills the build, in order?                (the risk register)
  5  Can they say which phase comes first, and why?               (§12)
  6  Can they say what the design PRESERVES from the old system?  (§3)
  7  Can they say which anti-pattern the build will produce?      (§11)
  8  Can they say the whole design in one breath?                 (the summary)
```

**Any "no" is a missing section, not a missing paragraph.**

---

## THE COMPOSITION MAP

```
  vs writing-plans             a plan orders work; this orders a MACHINE
  vs trident-deep-planning     DPL1 is a build contract for agents; a blueprint is a
                               manufacturing design for engineers — they compose
  vs master-blueprint          that reverse-engineers an EXISTING build; this designs
                               one that does not exist yet
  vs blueprinting              that is an interactive design SESSION (interview-driven,
                               16 moves); this is the artifact PRODUCTION step that
                               follows it, and it is also usable on its own
  vs extract-golden-reasoning  that mines reasoning from a trace; this produces the
                               artifact the trace will later be mined FROM
```

**Precedence:** on system architecture this wins. On work ordering, `writing-plans` wins. On the reasoning record, `extract-golden-reasoning` wins.

---

## THE WORKED REFERENCE

`/home/leviathan/JARVIS_WORKSPACE/Shared_Workspace/PLUTUS_VISION/design/DESIGN_BLUEPRINT_v1.1_AUTHORITATIVE.md` — 651 lines, the PLUTUS VISION indicator + sidecar. Read it before authoring a new one; it is the shape this skill describes, applied end to end.

**What made it work, in the operator's words:** *"this is the best design blueprint I have seen all week. It actually makes sense. There's real logical coherence flow. There's real attention to detail."*

The coherence came from **one constraint driving everything** — not from covering more ground.
