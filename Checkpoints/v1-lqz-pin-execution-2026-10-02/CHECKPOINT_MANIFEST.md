# CHECKPOINT MANIFEST — v1-lqz-pin-execution — 2026-10-02 (rev 7: the rendering D1, grids rebuilt)

## THE SEAL MODE (ONE mode, declared)
no-lock — fully committed and reproducible from git at the SHA below. NEVER manifest-only.

## THE SHAS
| artifact | sha256[:16] |
|---|---|
| git HEAD | `cace2c0` |
| lqz-luxalgo.pine | `db06b60574125039` |
| lqz-plutus.pine | `68881deaca0c66a1` |
| plutus-vision-v1.pine | `82da437af969a315` |
| plutus-vision-v0.pine | `605bff82d3539e9e` |
| render vision.mjs | `d032a26721176649` |
| vil-rail.mjs | `1686b1a1ddc73f67` |

## THE FOUR GRIDS — D1's panel now carries the deliverable RENDERING
| panel-grid-IDE-15m | `299889060907a1fb` |
| panel-grid-IDE-30m | `c1da1d67e074b9f8` |
| panel-grid-IDE-1H | `e29c0969f8676569` |
| panel-grid-IDE-4H | `444b332a02b77b23` |

## THE D1 ROWS (final sha db06b60574125039)
15m 97/33/1 FAIL · 30m 145/46/2 PASS · 1H 117/42/2 PASS · 4H 216/65/5 PASS

## THE COUNTS
- tracked (excl. the seal): **873** → sealed: **873**  **MATCH**

## THE STATE
- D1 defaults to `lqzSource='both'` — the measured displaying config (the pin's D1 gate demands
  'proper full-width horizontal display'; under 'luxalgo' the emitter admitted no zones on this fixture)
- the zone labels render INSIDE every viewport (-100 anchor); LOOKED AT and confirmed at 1H
- the rail no longer lies (timeout != refusal; 800 ms; three-valued up)
- `plutus-vision-v0.pine` UNCHANGED at `605bff82d3539e9e`

## HONEST GAPS
1. **THE OPERATOR HAS NOT RECORDED A VERDICT** — the pin's P8.
2. **The 15m D1 row reads FAIL** (no deltas) — the reader's verdict on a frame with 1 label and 97 boxes; the operator's eyes are the appeal.
3. **Viewports differ per panel** (the chart auto-fits per run; no viewport control in the CDP composer).
4. **The 36 native LuxAlgo primitives carry no colour** (render via BRASS). Recorded, not yet fixed.
5. **The station wedges under sustained large-file compiles** — remedy `scripts/pv-ide.sh`; retry condition: all four ports answering.
