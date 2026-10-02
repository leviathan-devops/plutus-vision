# CHECKPOINT MANIFEST — v1-lqz-pin-execution — 2026-10-02 (rev 8: the re-verification round)

## THE SEAL MODE (ONE mode, declared)
no-lock — fully committed and reproducible from git at the SHA below. NEVER manifest-only.

## THE SHAS
| artifact | sha256[:16] |
|---|---|
| git HEAD | `b8eb1e4` |
| lqz-luxalgo.pine | `db06b60574125039` |
| lqz-plutus.pine | `68881deaca0c66a1` |
| plutus-vision-v1.pine | `82da437af969a315` |
| plutus-vision-v0.pine | `605bff82d3539e9e` |

## THE RE-VERIFICATION ROUND (every gate re-run on the CURRENT tree)
| gate | result |
|---|---|
| L1 unit — `bun test ./scripts/` | **12 pass . 0 fail** (the PATH form; 'bun test scripts/' is a filter reaching the sealed copies: 24 across 8) |
| L1.5 adversarial — `lqz_adversarial.py` | **7/7 PASS, ZERO confirmed defects** |
| L2 parity — `compare.py` | SMC **195/195** . POOLS **25/25** . VOIDS **380/500** — exact to the baseline; SWEEPS a named engine-era residual (F-XX) |
| L3/L4 the grids | the four TF IDE grids + the W6 grid, every panel opened and recorded |

## THE ROUND'S FIXES
- `f496f9a` the stale test (pinned the pre-guard line since the NA guard landed)
- `bccd247` THE SOURCE-DISTINCTNESS GUARD (A4 proved the frame guard necessary but not sufficient)
- `36373c3` the TMP isolation (the suite was red for the adversary's reason)

## THE COUNTS
- tracked (excl. the seal): **873** → sealed: **873**  **MATCH**

## HONEST GAPS
1. **THE OPERATOR HAS NOT RECORDED A VERDICT** — the pin's P8.
2. **THE SWEEPS STANDALONE LEG** fails on the current engine install (F-XX; the deliverables unaffected; resume condition named).
3. **Viewports differ per panel** (the chart auto-fits per run).
4. **The 36 native LuxAlgo primitives carry no colour** (BRASS fallback; recorded).
5. **The station wedges under sustained large-file compiles** — remedy `scripts/pv-ide.sh`.
