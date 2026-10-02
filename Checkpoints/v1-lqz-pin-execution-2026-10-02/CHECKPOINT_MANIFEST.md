# CHECKPOINT MANIFEST — v1-lqz-pin-execution — 2026-10-02 (rev 4: post-fix, twelve panels)

## THE SEAL MODE (ONE mode, declared)
no-lock — the tree is fully committed and reproducible from git at the SHA below.
NEVER manifest-only: `tree/` holds every tracked file.

## THE SHAS
| artifact | sha256[:16] |
|---|---|
| git HEAD | `f5325f3` |
| lqz-luxalgo.pine | `d33c2b75e30da63d` |
| lqz-plutus.pine | `5295b34e1f9fe2e0` |
| plutus-vision-v1.pine | `82da437af969a315` |
| plutus-vision-v0.pine | `605bff82d3539e9e` |
| render vision.mjs | `d032a26721176649` |

## THE FOUR GRIDS — all twelve panels post-fix
| panel-grid-IDE-15m | `dcd2598fae0b1d4d` |
| panel-grid-IDE-30m | `71320abb81366f6a` |
| panel-grid-IDE-1H | `d461941e63d491a5` |
| panel-grid-IDE-4H | `8a3f62f26ca9e0e0` |

## THE COUNTS (verified against git)
- tracked (excl. the seal): **870** → sealed: **870**  **MATCH**
- canon: 12 · ship: 5 · artifacts: 13

## THE STATE
- **AUDIT GATE: PASS** — 7/7, zero confirmed defects (reports/LQZ_ADVERSARIAL_AUDIT.txt)
- **CLASS 1 FIXED** — the box fill read `b.color` (never set) → BRASS; now `b.bgcolor`. `nonBg 0.40008 → 0.16821`
- **CLASS 2 FIXED** — an NA side → NA colour → BRASS at 1px; now guarded. D2/D3 0 % → **100 % coloured**
- **CLASS 3 DIAGNOSED** — D1 supply-starved by `lqzSource='luxalgo'`; `both` measured 0 → 3 coloured
- **the parity reference is UNCHANGED** — `plutus-vision-v0.pine 605bff82d3539e9e`

## HONEST GAPS
1. **THE OPERATOR HAS NOT RECORDED A VERDICT** — the PASS/FAIL/INCONCL buttons write to
   `vil/2026-W29.jsonl`. No agent action substitutes.
2. **`lqzSource` is the operator's calibration call.**
3. **No container round.** Every verdict is host-live.
4. **D1 has no ladder by design of `lqzSource`**, not by a rendering fault.
5. The composer's freshness test is a WEAK guard (mtime-based).

## HOW TO RESUME
1. `canon/CURRENT_STATE.md` then `canon/NEXT_STEPS.md`
2. open `artifacts/panel-grid-IDE-*-2026-W29.png` — the operator's judgment surface
3. `bash launch-pine-ide lqz-plutus.pine EUR/USD 1H` · `python3 scripts/lqz_panel_ide.py`
4. `python3 scripts/lqz_adversarial.py` — the guards must still bite
