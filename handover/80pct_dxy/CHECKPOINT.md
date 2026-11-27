# Checkpoint "80% functional — DXY specific" (operator M-60, 2026-11-27)

Code state: branch AGENT, commit aa8d689 (this file is committed on top of it; no code change).
Operator's verdict on the frames of this state: DXY golden week — first half (Mon–Tue) accurate, the trades hit entry and take-profit; the E2 shape chain of the second half (Wed–Fri) is broken; GBPUSD poor; EURUSD not shown.

What this state contains (decision rows in memory/03_DECISION_CHAIN.md):
- D-131 / D-134: daily anchoring by default; one unique order per move (no per-day copies; a pending order keeps resting).
- D-132: a 1H close beyond a Decision Zone activates the alternative chain at the next trading-day open (6.6 Step 4).
- D-135: stops per L-50 (reversal entries 1 pip inside the next shielding zone, no 9.5-pip veto, RRR floor decides, deeper-only fallback; EUR/USD keeps the outside stop).
- D-136 / D-137 / D-138: London-open zone update (zones formed since the week anchor drawn from the London open that found them); after a chain fails, the line and day boxes follow a chain re-anchored on the rebuilt map; orders stay with the chain in force.
- L-51 (first version): range days drawn session by session (Asia flat, London to the nearer bound, NY pre-cut pinned at the day's largest strike, NY post-cut to the other bound).
- Protocols D / E / G harvested (Treasury auctions, NY Fed ON RRP, EIA); Protocol F (calendar) NO DATA.

Frames of this state: evidence/lib4/DXY_2026-07-06_week.png, evidence/lib4/GBPUSD_2026-04-13_week.png.
Run: `python3 e1_tool/plutus.py MONDAY PAIR [out.pine]` (daily anchoring default; `--weekly` = all orders at the Monday anchor).
Restore this exact state: `git checkout aa8d689`.

## Self-contained: code + context + graph (operator, after M-60)
- CODE: the whole repository at this commit (engines e1_tool/*.py, sidecar/ incl. protocols.py and its data, tools/ incl. leak_check.py, indicator/ with the sealed V1).
- CONTEXT: memory/*.md (standing order 14, rulings 04 incl. L-46..L-56, operator verbatim 12 incl. M-57..M-60, decisions 03 incl. D-129..D-138, lessons 06, facts 08 incl. 'SESSION FACTS 2026-11-27', ledger 07 incl. rows 107-111c, journal 05, state 01, coverage 15), evidence/answers_m58/ (Q1, Q4, Q6), evidence/lib1-lib4 + chk107 frames, handover/70pct_functional/ (the previous checkpoint).
- GRAPH: handover/80pct_dxy/omnigraph/graph_store/ (the OmniGraph store as on disk, /home/user/.plutus-mem, rebuilt from memory/*.md at this checkpoint: 1572 nodes, 1029 edges - Fact 1140, Decision 132, Lesson 39, Ruling 54, Task 33, Evidence 157, Artifact 17), graph_export.jsonl (full `omnigraph export`), mem_status.txt, mem_ls.txt.
- Restore the graph elsewhere: copy graph_store/ to /home/user/.plutus-mem, or run `tools/mem/mem rebuild` (the graph is a pure function of memory/*.md + memory/graph_log.jsonl + tools/mem/schema.pg).
- Manifest: handover/80pct_dxy/MANIFEST.sha256 (sha256 of every tracked file at this commit except the manifest itself).
