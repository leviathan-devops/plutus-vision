# CHECKPOINT MANIFEST — v1-lqz-pin-execution — 2026-10-02 (rev 9: the drills + the re-verification)

## THE SEAL MODE (ONE mode, declared)
no-lock — fully committed and reproducible from git at the SHA below. NEVER manifest-only.

## THE SHAS
| artifact | sha256[:16] |
|---|---|
| git HEAD | `1c64f20` |
| lqz-luxalgo.pine | `db06b60574125039` |
| lqz-plutus.pine | `68881deaca0c66a1` |
| plutus-vision-v1.pine | `82da437af969a315` |
| plutus-vision-v0.pine | `605bff82d3539e9e` |

## THE EVIDENCE, condensed
- unit `bun test ./scripts/`: **12 pass . 0 fail** · adversarial: **7/7, ZERO confirmed defects**
- parity: SMC **195/195** . POOLS **25/25** . VOIDS **380/500** exact to the baseline · SWEEPS named (F-XX)
- the starvation drill: **no fallback band** at 2-5 bars (D1/D2 zero; D3 zero boxes)
- the lqzLabel toggle: **labels 2 -> 0**, the pre-registered expectation met
- the settings-dialog op: **UNRUN, NAMED** (the exposed renderer surface lacks the dialog internals)

## THE COUNTS
- tracked (excl. the seal): **873** → sealed: **873**  **MATCH**

## THE JUDGMENT SURFACES
- `panel-grid-1H.png`  `6c01eec3592c75b2`
- `panel-grid-IDE-15m-2026-W29.png`  `299889060907a1fb`
- `panel-grid-IDE-1H-2026-W29.png`  `e29c0969f8676569`
- `panel-grid-IDE-30m-2026-W29.png`  `c1da1d67e074b9f8`
- `panel-grid-IDE-4H-2026-W29.png`  `444b332a02b77b23`
- `panel-grid-IDE-4TF-2026-W29.png`  `2cbc46a8a75e7537`

## HONEST GAPS
1. **THE OPERATOR HAS NOT RECORDED A VERDICT** — the pin's P8.
2. **THE SETTINGS DIALOG OP IS UNRUN** — H2's op, attempted, unreachable via the exposed surface; the mechanical equivalent is the evidence.
3. **THE SWEEPS STANDALONE LEG** fails on the current engine install (F-XX; the deliverables unaffected).
4. **D3's structure labels at starvation carry null prices** — dead geometry the counts still census (recorded).
5. **Viewports differ per panel**; the 36 native LuxAlgo primitives render via BRASS; the station wedges under sustained compiles (remedy `scripts/pv-ide.sh`).
