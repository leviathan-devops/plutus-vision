# CHECKPOINT MANIFEST — v1-lqz-pin-execution — 2026-10-02 (rev 6: the label fix + the rail fix)

## THE SEAL MODE (ONE mode, declared)
no-lock — fully committed and reproducible from git at the SHA below. NEVER manifest-only.

## THE SHAS
| artifact | sha256[:16] |
|---|---|
| git HEAD | `b0d8940` |
| lqz-luxalgo.pine | `1dbe1ac3bd3dc077` |
| lqz-plutus.pine | `68881deaca0c66a1` |
| plutus-vision-v1.pine | `82da437af969a315` |
| plutus-vision-v0.pine | `605bff82d3539e9e` |
| render vision.mjs | `d032a26721176649` |
| vil-rail.mjs | `1686b1a1ddc73f67` |

## THE TITLES (asserted by the station, one per deliverable)
  LQZ LuxAlgo
  LQZ Plutus — operator candle liquidity
  Plutus Vision v1

## THE FOUR GRIDS — all twelve panels, every one opened and recorded
| panel-grid-IDE-15m | `dcd2598fae0b1d4d` |
| panel-grid-IDE-30m | `71320abb81366f6a` |
| panel-grid-IDE-1H | `d461941e63d491a5` |
| panel-grid-IDE-4H | `8a3f62f26ca9e0e0` |

## THE COUNTS
- tracked (excl. the seal): **873** → sealed: **873**  **MATCH**
- canon: 12 · ship: 5 · artifacts: 14

## THE STATE
- the four grids exist, 4 panels each, built under the composer's FRESHNESS GUARD
- **bars ARE identical** (measured: 400 bars, 2026-06-11T15:00 → 2026-07-06T06:00, three distinct sourceShas)
- **D1's dead label input WIRED** (`grep -c label.new` 0 → 1 real call): the zones now carry their tags
- **D1's label RE-ANCHORED inside the frame** (was 20 bars past the last bar; measured inside: true after)
- **the rail no longer lies** — a timeout is not a refusal; 4.04 s → 0.001–0.005 s on /health
- the operator's measured pair: `luxalgo` 117/36/0 · `both` 117/42/2

## HONEST GAPS
1. **THE OPERATOR HAS NOT RECORDED A VERDICT** — the pin's P8.
2. **THE VIEWPORTS ARE NOT IDENTICAL** across panels (the chart auto-fits per run; no viewport control exists in the CDP composer). A scale-matched comparison is a NAMED residual.
3. **THE STATION IS FLAKY UNDER REPEATED LARGE-FILE COMPILES** — its /health route hangs in the documented half-alive state, and after sustained use it wedges. REMEDY: the launcher's restart (`scripts/pv-ide.sh`). RETRY CONDITION: the rig's four ports answering.
4. **THE NATIVE LUXALGO PRIMITIVES CARRY NO COLOUR** (36 lines with  render via the renderer's BRASS fallback). Same class as the box-fill bug fixed earlier; recorded, NOT yet fixed.
5. No container round. Every verdict is host-live.

## HOW TO RESUME
1. `OPERATING_MANUAL.md` — the three commands, the IDE pipeline, seven traps, §3.1 the durable load
2. `reports/lqz_panel_look_record.md` — every panel, found/missing/wrong, plus D1's three defects
3. `scripts/pv-ide.sh` restarts the rig; `scripts/verify_served_pine.sh` guards the served copies
4. `python3 scripts/lqz_panel_ide.py` recomposes the grids from the ledger
