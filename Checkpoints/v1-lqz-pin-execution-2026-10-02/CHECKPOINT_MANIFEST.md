# CHECKPOINT MANIFEST — v1-lqz-pin-execution — 2026-10-02 (rev 5: title-fix, durable load, manual)

## THE SEAL MODE (ONE mode, declared)
no-lock — fully committed and reproducible from git at the SHA below. NEVER manifest-only.

## THE SHAS
| artifact | sha256[:16] |
|---|---|
| git HEAD | `686bcec` |
| lqz-luxalgo.pine | `d33c2b75e30da63d` |
| lqz-plutus.pine | `68881deaca0c66a1` |
| plutus-vision-v1.pine | `82da437af969a315` |
| plutus-vision-v0.pine | `605bff82d3539e9e` |
| render vision.mjs | `d032a26721176649` |

## THE TITLES (asserted by the station, one per deliverable)
  LQZ LuxAlgo
  LQZ Plutus — operator candle liquidity
  Plutus Vision v1

## THE FOUR GRIDS — all twelve panels post-fix
| panel-grid-IDE-15m | `dcd2598fae0b1d4d` |
| panel-grid-IDE-30m | `71320abb81366f6a` |
| panel-grid-IDE-1H | `d461941e63d491a5` |
| panel-grid-IDE-4H | `8a3f62f26ca9e0e0` |

## THE COUNTS
- tracked (excl. the seal): **872** → sealed: **872**  **MATCH**
- canon: 12 · ship: 5 · artifacts: 14

## THE STATE
- **AUDIT GATE: PASS** — 7/7, zero confirmed defects
- **CLASS 1 FIXED** — the box fill read `b.color` (never set) → BRASS; `nonBg 0.40008 → 0.16821`
- **CLASS 2 FIXED** — an NA side → NA colour → BRASS at 1px; D2/D3 **0 % → 100 % coloured**
- **CLASS 3 DIAGNOSED** — D1 supply-starved; `lqzSource='both'` measured 0 → 3 coloured
- **D2'S TITLE RESTORED** — a second operator found it dropped by `lqz_assemble.py`'s `--title` default; the grid command now completes `PANEL_GRID_OK`
- **THE DURABLE LOAD FOUND** — `export → reload → import` composes the two remedies
- **the parity reference is UNCHANGED** — `plutus-vision-v0.pine 605bff82d3539e9e`

## HONEST GAPS
1. **THE OPERATOR HAS NOT RECORDED A VERDICT.**
2. **`lqzSource` is the operator's calibration call.**
3. **No container round.** Every verdict is host-live.
4. **D1 has no ladder by design of `lqzSource`**, not by a rendering fault.
5. The composer's mtime freshness test is a WEAK guard (and the sha is an identity, not a
   freshness signal — recorded).

## HOW TO RESUME
1. `OPERATING_MANUAL.md` FIRST — the three commands, the IDE pipeline, seven traps, §3.1
2. `artifacts/panel-grid-IDE-*-2026-W29.png` — the operator's judgment surface
3. `python3 scripts/lqz_panel_ide.py` · `python3 scripts/lqz_adversarial.py`
