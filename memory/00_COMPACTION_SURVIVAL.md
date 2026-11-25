# 00 — COMPACTION SURVIVAL (read this first, every new context window)

You are the engineer on PLUTUS VISION. Your working memory lives in this folder, not in your context.
After a compaction or a container reset, do exactly this, in order, before any other work:

1. Read `memory/01_CURRENT_STATE.md` (what is true right now, what you were doing, the very next step).
2. Read `memory/04_OPERATOR_RULINGS_LIVE.md` (the operator's live instructions and answers — do not renegotiate).
3. Read `memory/02_TASK_QUEUE.md`, then `memory/03_DECISION_CHAIN.md`, then `memory/06_LESSONS.md`.
4. Read `memory/08_FACTS.md` (durable semantic facts: canon rules, oracle numbers, engine quirks).
5. Skim the tail (last ~60 lines) of `memory/05_JOURNAL.md` and of `memory/07_EVIDENCE_LEDGER.md`.
6. Check the machine: `export PATH=$HOME/.local/bin:$PATH XDG_RUNTIME_DIR=/run/user/0; pinebox list --session plutus-main`.
   - empty list or command missing -> the container was reset: run `tools/pinebox-bootstrap.sh` (needs `/home/user/inputs/pinebox`; if `/home/user/inputs` is gone, re-unzip the uploads in `/root/.claude/uploads/*/` — see 08_FACTS "Inputs").
7. Only then continue from "NEXT STEP" in 01_CURRENT_STATE.

## Write discipline (so compaction is only a garbage collector)
- Every 3-5 turns, and ALWAYS before a long tool run or a workflow: update 01_CURRENT_STATE (overwrite) and append to 05_JOURNAL.
- A decision -> one row in 03_DECISION_CHAIN. A mistake or a measured surprise -> 06_LESSONS. A frame you looked at -> 07_EVIDENCE_LEDGER.
- A durable fact you would hate to re-derive (a canon constant, an oracle price, an engine quirk) -> 08_FACTS.
- Commit `memory/` with every code commit; push to branch `AGENT` (the only thing that survives a container reset).
- The OmniGraph store (`tools/mem`) mirrors these files for query; the markdown is the source of truth.

## Things that silently bite
- Hooks (the operator's ECC GateGuard) block the first Bash call, every first Write to a new path, and destructive commands,
  asking for "facts". State them in 3-4 plain lines and retry the same call. Do not disable the hook.
- `pkill -f` / `pgrep -f` patterns can match your own shell. Kill by pid.
- The shell cwd resets to the repo root after every Bash call; use absolute paths.
- Only files under `/home/user/plutus-vision` and the scratchpad can be shown to the operator.
