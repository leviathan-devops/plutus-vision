# PLUTUS VISION — read this first (auto-loaded)

**READ `memory/10_FAILURE_RECORD.md` BEFORE ANY E1 WORK: execute the v5.3.3 prompt exactly as written, do only what the operator says, no redesigns.**
**THE CURRENT JOB = `memory/14_GOAL_PROMPT.md` (GOAL PROMPT v2, 2026-11-26 — frozen scope, sources of truth, the seven laws, anti-patterns A1-A18, grading rules, success conditions S1-S6). Read it in full before anything else and obey it literally. Coverage matrix: `memory/15_CANON_COVERAGE.md`. The strategy works; a bad result is a bug in my build. No own ideas, no scope changes, no questions to the operator.**
**After any compaction/reset, read `memory/00_COMPACTION_SURVIVAL.md` FIRST and follow its read order** (state, live operator rulings, task queue, decisions, lessons, facts, journal).
Update `memory/01_CURRENT_STATE.md` + `memory/05_JOURNAL.md` every 3-5 turns and before any long run.
Older graph (foundation phase, still valid for canon concepts): `python3 context_management/graph/resume.py` (`--node E3`, `--grep <word>`).

## The job (operator brief 2026-11-25, in force; build permission GRANTED, fully autonomous)
Build the Plutus Vision Pine indicator: on top of the sealed V1 baseline (LuxAlgo S/D + liquidity — do not touch it),
render **E1** institutional pressure zones, then **E2** shape chain, then **E3** trade setups (corrected E3 spec).
Everything is computed dynamically from market data available at the **Monday London-open anchor** of the week under test.

## Hard constraints
- **No hardcoded values.** No price literals, no per-week constants. Any week, any of DXY/EURUSD/GBPUSD, same accuracy (target >=90%).
- **Temporal anchor = Monday, start of the trading week.** Nothing after the anchor may feed a forecast. Enforced by `tools/anchor_guard.py` + git pre-commit hook.
- **Pinebox is the only test environment.** Render the Pine in Pinebox, LOOK at the chart, judge whether candles react to the render. No headless/script tests as gates.
- **<= 11 trade setups per week per pair.** Zones live on 4H / 1H (30m refinement; 15m precision only).
- E1 = v5.3.3 prompt, every token (R-14). E2 = v5.3.3. E3 = `canon/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md` only (R-16). ZFP = strength only (R-17).
- Render window = active week + one week left (R-36). No caps as a fix (R-37). Canon vocabulary only (R-05).
- Report outcomes faithfully, negatives included. No theatre. No unasked advice.

## Where things are
- Pinebox (IDE + backtest): rebuild with `tools/pinebox-bootstrap.sh`; then `export PATH=$HOME/.local/bin:$PATH XDG_RUNTIME_DIR=/run/user/0`; session `plutus-main`.
  Manual: `/home/user/inputs/pinebox/ship-approved-v2/src/manuals/OPERATOR_MANUAL_pinebox.md`. Bar store: TV bars DXY/EURUSD/GBPUSD x 15m/30m/1H/4H, 2025-02-02 -> 2026-11-06.
- Uploaded packages (unzipped, outside the repo): `/home/user/inputs/{handover,pinebox,canon,trades}`; operator rulings R-01..R-39 are in
  `/home/user/inputs/handover/PLUTUS_VISION_CONTEXT_HANDOVER/00_HANDOVER/PLUTUS_VISION_CONTEXT_HANDOVER.md` (Appendix A).
- Original canon + weekly report oracles: git branch `origin/handover` (worktree `/home/user/handover-branch/Original_Canon_Data`).
- Canon copy in this repo: `canon/Toolset/`. Spec digests + oracle data: `context_management/spec/`, `context_management/oracle/`.
- The indicator: `indicator/` (V1 sealed baseline + engine layers). Evidence frames: `evidence/`.

## Blueprints (operator ruling L-69, 2026-11-28)
When the operator says 'blueprint': load the skill `.claude/skills/design-blueprint/SKILL.md` (his file) FIRST and build a proper CAD-grade design blueprint in `design/` (constraint first, planes, contracts + failure modes, traced numbers, wired anti-patterns, failable exits, risk register, one-paragraph summary). Never a note called a blueprint.
