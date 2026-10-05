# CHECKPOINT MANIFEST — v2-working-baseline-2026-10-05 (updated)

**Date:** 2026-10-05 · **Project:** PLUTUS VISION · **git HEAD:** e64f1fa
**Seal mode:** NO-LOCK (mutable working snapshot; the v1 SHA is checked by every build — the H1 guard is the seal)
**Milestone:** THE E1 ZONES RENDER WITH LABELS — the v2 working baseline, the E1 label defect
fixed (the E2 path loop was suppressing the label pass; the SMC filled the budget).

## THE ARTIFACT FINGERPRINTS
| artifact | sha256 (16) | what |
|---|---|---|
| `dist/plutus-vision-v2.pine` | `37f430b8aac30f92` | v1 + the E1 layer + the E2 path (default OFF) |
| `dist/plutus-vision-v1.pine` (the sealed baseline) | `0d20e8314ce992fc` | UNCHANGED — HARD STOP H1 guard |
| `lqz/e1-render.pine` | the E1 render source | the 5 role labels + the box loop |
| `lqz/e2-render.pine` | the E2 render source | the path (loop UNROLLED; default OFF) |
| `visual/e1-labels-render.png` | `49f47f0f037e4d48` | the live render (looked) |
| `desktop/pine-ide` | the Tauri desktop launcher | ONE-COMMAND, 2.9x lighter than Chrome |

## THE STATE (what this checkpoint IS)
- `plutus-vision-v2.pine` = the SEALED v1 baseline + the E1 institutional-pressure layer +
  the E2 predicted path (togglable).
- The E1 zones render as **5 DISTINCT bands** (no stacking) with the **5.3.3 §5.2.1 role
  labels**: IP Resistance Ceiling · Upper IP Resistance · Equilibrium Zone · Mid-Range Support ·
  IP Support Floor.
- The E1 data derives from the chart's own last bar (the anchor law), not a hardcoded week.
- A first-class DESKTOP app (Tauri) launches the IDE from the terminal on the operator's session.

## THE VALIDATED (measured this session)
- v1 seal intact (`0d20e8314ce992fc`, HARD STOP H1 not tripped).
- battery: ST-18 8/0 · ST-19 10/0 · ST-20 7/0 (the E1 gates green).
- the live render (looked): the 5 labelled zones on the DXY chart, census 34 boxes · 28 lines ·
  6 labels (E2 off).
- the desktop app: `pine-ide` from any cwd; 572 MB RSS vs Chrome 1685 MB.

## THE KNOWN CONSTRAINT (named)
- The vela PineTS renderer cannot paint the E2 path lines AND the E1 zone labels together — the
  line geometry suppresses the label pass. `e2Enabled` defaults FALSE; the E1 map (with labels)
  is the default. See DEBUG_LOG EN-104/105.
