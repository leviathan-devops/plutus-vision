# Checkpoint "85% functional - DXY + GU (V3: EURUSD fix)"

Code state: branch AGENT at a8bfce4 (this folder is committed on top of it).

Operator M-61 asked for V3 after the EURUSD fix ('Euro USD is like a solid C ... fix Euro USD, get it at the same level, and then you can commit that as V3 of the same checkpoint'). Why EURUSD was a C: evidence/answers_m61/EURUSD_why_C.md - two stop-outs the other pairs did not have (a second Monday short 1.14385 entered while his Monday long still ran to its TP; a Tuesday re-entry long DXY had not mirrored) plus box clutter. V3 = D-142/D-142b (E3C Phase 10 under daily anchoring: a re-entry on EURUSD / GBPUSD needs the source pair's matching order confirmed at the same day's anchor) + D-144 (Law 27 'TP of trade N = entry of trade N+1' on the day's drawn Engine 2 line: an order the line reaches while an opposite order runs to its TP, inside that move by more than 3 pips, is not placed). Golden week: EURUSD = his #2 #3 #4 #5 #6 #7 #8 + one long that never fills, no stop-outs; DXY unchanged; GBPUSD unchanged but the never-filled Tuesday duplicate. Frames: evidence/v3 (V1 = evidence/m60b, V2 = evidence/v2). Leak check (trading-day open + London open per day) passes on the golden DXY / EURUSD / GBPUSD and GBPUSD 2026-10-05.

Contents: the whole repository (code) + memory/*.md (context: standing order, rulings, operator verbatim, decisions, lessons, facts, ledger, journal, state, coverage) + evidence frames + this folder's OmniGraph (graph_store/ = /home/user/.plutus-mem rebuilt from memory at this checkpoint; graph_export.jsonl = full 'omnigraph export'; mem_status.txt; mem_ls.txt) + MANIFEST.sha256.

Graph: 2026-11-27T19:07:22Z  1606 nodes, 1102 edges  (up to date)
Restore: git checkout a8bfce4; copy omnigraph/graph_store to /home/user/.plutus-mem or run tools/mem/mem rebuild.
