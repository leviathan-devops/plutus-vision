# THE CHARTER — PLUTUS_VISION knowledge graph

**Project root:** `/home/leviathan/JARVIS_WORKSPACE/Shared_Workspace/PLUTUS_VISION`
**Chartered:** 2026-10-05 (the operator's order: "/skill:create-knowledge-graphs plutus vision repo")

## THE SCOPE (the corpus — the operator's ruling)

The PLUTUS_VISION project tree, honoring the SHARED WALK-SKIP law (never walked:
`node_modules/`, `.git/`, `dist/`, `build/`, `.gi/`, `Checkpoints/`, `pine-ide/node_modules/`,
`*.pyc`, `Original_Canon_Data/` third-party reference PDFs).

The load-bearing subtrees (the laws + the build):
- `plutus-vision-v1.pine` — THE V1 BASELINE (the sealed operator candle-liquidity + LuxAlgo SMC).
- `plutus-vision-lqz/` + `plutus-vision-v2.pine` — THE E1 LAYER (the E1 institutional-pressure render).
- `plutus-vision-e1-automatic.pine` — the canon `trident_v8` IP block, LSZ removed.
- `context_management/` — the 11 canon docs (the laws + the state).
- `scripts/` — the E1 data pipeline (week/category/extract/sources/vlm/judge/build).
- `data/e1/` · `fixtures/` — the payload + the bars.
- `packages/plutus-vision-e1-automatic/` — the build package (DPL1 spec / wave-plan / blueprint).
- `Original_Canon_Data/` — the canon: the v5.3.3 prompt + `trident_v8.pine` + the handover.

## THE LAYERS

**BOTH** — L1 (semantica, the fast automatic semantic walk) + L2 (arsumbris, the curated typed graph).

## THE TYPES (the L2 card shapes)

slug · kind · quote · source (file:line) · mechanics · links — the standard arsumbris card.

## THE TRUTH (what this graph exists to hold)

1. **THE V1 BASELINE IS SACRED.** `plutus-vision-v1.pine` sha256
   `0d20e8314ce992fc23e27f1b97fed76b…` (1270 lines). ANY build that drifts it is `HARD STOP H1`.
2. **THE DELIVERABLE = V1 BASELINE + E1 ON TOP, rendered TOGETHER** (never E1 alone — that
   drops the baseline).
3. **THE E1 DATA IS DYNAMIC** — adapted to the current trading week; NO stale/hardcoded week.
4. **THE CANON RENDER IS VERBATIM** — `trident_v8.pine`'s IP block (zfill/zbord/pressureLbl/
   calcZFP, 15 colours × 6 tiers, labels at tsMid), the ONLY change: LSZ rendering REMOVED.
5. **THE 5.3.3 PROMPT IS THE BINDING AUTHORITY** —
   `Original_Canon_Data/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md`.
6. **SOURCES ARE AUTO-HANDLED** — no manual agent data-fetching in the render path.

## THE REVIEW CONTRACT

- **the diagnostic sweep.** `diagnostic_counts` -> 0 for this corpus. Drive to 0 by fixing
  CARDS, never by editing the engine (diagnostics are lint; saves always land).
- **the anchor sweep.** Every card's `source` / `anchor` resolves:
  `grep -n "<the quoted string>" <the anchored file>` -> a hit, or FIXED/FLAGGED.
- **the scope sweep.** The corpus is `PLUTUS_VISION` only; never widened, never shrunk.
- **the map.** `reports/Knowledge_Graph_Map.md` (the ToC + the per-card sections + the links).

## THE FAILURE MODES (each measured)

| the symptom | the cause | the fix |
|---|---|---|
| `entities=0` on a real corpus | the dict-vs-LIST shape assumption | the script's list mapping; assert >0 |
| diagnostics fire on a fresh repo | missing repo.yaml / README / type/ (singular) | the scaffolding checklist |
| `refinement-bad-shape` | a bare regex (no slashes) or a `/` in a char class | slash-delimit; keep `/` out of classes |
| `navigational-target-not-found` | a wikilink to an ID (not the FILENAME) | link the filename |
| the kernel dies with the shell | nohup from a tool shell | supervise it (systemd/hub/detached) |

## THE DELIVERABLE THIS GRAPH HOLDS

The graph exists to make the E1 deliverable unambiguous across sessions: the **V1 baseline +
the engine-one institutional-pressure zones, rendered TOGETHER**, the E1 data **dynamic to the
current trading week**, the canon render **verbatim with the LSZ removed**. See
`laws/LAW-02-v1-plus-e1-together.md:1` and `laws/LAW-03-e1-dynamic-week.md:1`.

## THE ANCHORS

- context_management/CURRENT_STATE.md:1 — the state this charter tracks.
- context_management/NEXT_STEPS.md:1 — the active task.
- reports/Knowledge_Graph_Map.md:1 — the map.
- README.md:1 — the corpus front door.

## THE LAYER OUTPUTS

- L1 output: `.omp/graph-intelligence/layers/semantica/kg.json` (the entities + relationships).
- L2 output: the daemon's live typed graph, served on the Unix socket.
- L3 output: the OMP tools surfaced by the `plutus-vision-au` binding.
- L4 output: `reports/Knowledge_Graph_Map.md` (the human map).

## THE VERBS

The read verbs over the socket: `diagnostics` (the lint), `type_counts` (the registered types),
`instances_of` (the cards of a type). The write path: author cards under the kind dirs, then the
daemon picks them up (restart if cached). verification: the daemon `diagnostics: 0`.

## THE MAINTENANCE

Re-ingest L1 after corpus changes (`Graph_Intelligence/scripts/semantica-ingest.py`). Re-probe
the daemon after card changes (restart if the cache is stale). Regenerate the map after either.
SEE `context_management/CANON_MANIFEST.md:1`.

## THE PROVENANCE

Proven on this host: the PLUTUS graph (`PLUTUS/MASTER_CONTEXT`, 703 nodes, 649 cards) and the
GI stores. This instance follows the same process — the L1 semantica + the L2 arsumbris + the
binding + the reviews + the map.

SEE reports/Knowledge_Graph_Map.md:1 for the map; SEE laws/LAW-01-v1-sacred.md:1 for the first law.
