# PLUTUS VISION — read this first (auto-loaded)

**Regain full context in one command (stdlib, no install):**
```
python3 context_management/graph/resume.py            # governance, mission, phase, canon spine, findings, open questions, decisions
python3 context_management/graph/resume.py --node E3  # drill into any node; --type rule|law|finding ; --grep <word>
```
Canon sources (read only the section a node points to): `canon/Toolset/`. Repo handover: `context_management/*.md`. Learning log: `context_management/LEARNING_LOG_2026-10-11.md`.

## Non-negotiables (from the operator; details in the graph)
- **Phase gate:** do NOT start indicator work until the operator explicitly gives permission + handover.
- **E1 and E2 (original v5.3.3) are frozen** — never change/disagree. E3 = `canon/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md` (untested live).
- **Solve obstacles yourself.** No theatre: write the expectation first, LOOK at the rendered frame yourself, name deltas; parity != correctness (FAILURE_LOG F-17).
- Report outcomes faithfully (negative results included). No unasked advice. Trident -> Plutus rename later.
- Keep the graph current: when you learn/decide something durable, edit `context_management/graph/build_graph.py`, rerun it, commit.
- Do not touch ports 9430/9441/9444/9448 (another session). Rig needs: see graph node `A_RIG`.
