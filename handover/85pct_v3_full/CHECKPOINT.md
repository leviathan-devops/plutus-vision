# Checkpoint "85% functional - DXY + GU (V3), FULL HANDOVER PACKAGE (M-62)"

Code state: branch AGENT at 63d10dc (this folder is committed on top of it).

Full handover package for everything since the '70% functional' package: see 00_START_HERE.md and ENGINEERING_REPORT.md in this folder. Code = V3 (ff6be1e) + D-145 (KeyError fix found while building the package).

Contents: the whole repository (code) + memory/*.md (context: standing order, rulings, operator verbatim, decisions, lessons, facts, ledger, journal, state, coverage) + evidence frames + this folder's OmniGraph (graph_store/ = /home/user/.plutus-mem rebuilt from memory at this checkpoint; graph_export.jsonl = full 'omnigraph export'; mem_status.txt; mem_ls.txt) + MANIFEST.sha256.

Graph: 2026-11-27T20:02:29Z  1618 nodes, 1121 edges  (up to date)
Restore: git checkout 63d10dc; copy omnigraph/graph_store to /home/user/.plutus-mem or run tools/mem/mem rebuild.
