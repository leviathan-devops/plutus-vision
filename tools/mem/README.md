# tools/mem: queryable memory graph (a mirror of `memory/*.md`)

**Backend live: OmniGraph 0.16.0** (release binary, CLI only: no server, no embeddings; search is BM25 full-text).
No fallback store is in use. Graph: `/home/user/.plutus-mem/graph.omni` (outside the repo, disposable).
Truth = `memory/*.md` + `memory/graph_log.jsonl` (commit both). The graph is built from them, never the reverse.

## Install (worked here 2026-11-25: root, Ubuntu 24.04 x86_64, behind the egress proxy; ~15 s, no cargo build)
    curl -fsSL https://raw.githubusercontent.com/ModernRelay/omnigraph/main/scripts/install.sh | VERSION=v0.16.0 bash
    export PATH=$HOME/.local/bin:$PATH && omnigraph version      # -> omnigraph 0.16.0
    tools/mem/mem rebuild
Binaries land in `~/.local/bin` (sha256-checked); `mem` looks on PATH, there and at `$OMNIGRAPH_BIN`, else prints this recipe.

## Verbs (`tools/mem/mem <verb>`, python stdlib)
    init                      create /home/user/.plutus-mem and an empty graph (schema.pg)
    sync                      parse memory/*.md + replay graph_log.jsonl -> fresh graph, swapped in (~0.3 s)
    rebuild                   wipe + init + sync + replay graph_log.jsonl
    add <type> <id> <title> <body> [--tags a,b] [--source s] [--date YYYY-MM-DD]
    link <from> <edge> <to>   edge: supports | supersedes | about | blocks | evidences (any type to any type)
    q <text> [-n N] [--type T] [--json]     id, type, score, title, first 200 chars of the body
    get <id>... [--json]      full record + edges out and in
    ls [type]  |  status      ids and titles  |  backend, counts, fresh or stale, sync warnings
Types: fact decision lesson ruling task evidence artifact. `add` and `link` append to `memory/graph_log.jsonl` and
roll the line back if the graph refuses it. `q`, `get`, `ls` re-sync by themselves when a source file changed.

## Ids, and rebuilding after a container reset
Sync makes one node per table row, top-level bullet and heading block with prose; each file is an Artifact
`memory/<file>.md`. Stable ids come from the text: `T3`, `D-06`, `L-05`, `LS-02`, `EV-<#>`, `J-YYYYMMDD-HHMM`. Any other
bullet gets `<file>.<heading>.<hash8>`, which changes when its text changes: link to stable ids or to ids you `add`.
A record citing a stable id gets an `about` edge. `add` refuses ids the markdown owns. Undo = delete the line in
graph_log.jsonl, `mem sync`. After a reset the graph and `~/.local/bin` are gone: run the three install lines above.
