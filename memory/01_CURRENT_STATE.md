# 01 — CURRENT STATE (overwrite; keep under ~60 lines)
Updated: 2026-11-25 ~11:20 UTC

## Where I am
- Phase: SETUP + ABSORB. No indicator code written yet today.
- Pinebox: UP (session plutus-main, xvfb :3). First frame read. Verbs not yet exercised beyond `up` and `shot`.
- Readers running: workflow `plutus-understand` (run id wf_dd57a995-1d1, task w3ou3sid2) -> 8 digest files in `context_management/spec/` and `context_management/oracle/`.
  Journal of results: `/root/.claude/projects/-home-user-plutus-vision/b6c77a81-471c-536b-9631-0319cefbf3ab/subagents/workflows/wf_dd57a995-1d1/journal.jsonl`.
- Operator answered my questions and LEFT (see 04_OPERATOR_RULINGS_LIVE L-06..L-13). Network + OpenCode key approved and measured working.
- Repo: branch AGENT, uncommitted: CLAUDE.md, tools/pinebox-bootstrap.sh, memory/, context_management/archive_2026-10 move.

## NEXT STEP (do these in order)
1. Commit + push memory/ and bootstrap (branch AGENT).
2. Exercise Pinebox verbs myself: load `plutus-vision-v1.pine` on DXY 1H, navigate the IDE chart to Jul 6-10 2026, shot, read; open BACKTEST tab, create a session for Jul 6-10, step, shot.
3. When readers finish: read each digest; verify key claims against the canon first-hand (E1 pillars, zone assembly, anchor time); record conflicts.
4. Spawn side quests (agents): (a) OmniGraph install + `tools/mem` wrapper mirroring memory/; (b) web sidecar design read of aether backend + investinglive dated-expiry fetch probe.
5. Write `tools/anchor_guard.py` + pre-commit hook (task #3), then E1 v0 in `indicator/` and the first golden-week frame.

## Open questions I must resolve myself (operator is away)
- Exact definition of the weekly IP ceiling/floor/equilibrium zones from the canon (await E1_ALGO digest; verify first-hand).
- How the indicator receives the sidecar's weekly JSON inside Pinebox (inputs? pasted array literals generated per week = NOT allowed as hardcode?). Must design so the Pine has zero baked values:
  candidate = sidecar writes a per-week data block that Pinebox injects as `input.*` defaults at load time; the indicator source itself stays constant.
- Whether the Pinebox engine re-runs the script per replay step in the Backtest tab (await PINEBOX_ENGINE_NOTES; then test).
