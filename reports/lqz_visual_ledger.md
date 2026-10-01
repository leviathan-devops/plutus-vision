# LQZ VISUAL LEDGER — the panel look, 2026-10-01 (1H, EUR/USD, 1603 bars, display :3)

Every row below is a frame I opened and read MYSELF. No VLM, no count-only verdict.
The frame's sha256 is the evidence; a row without it is not a look.

| # | deliverable | frame | sha256 | status bar | what I SAW |
|---|---|---|---|---|---|
| 1 | D3 plutus-vision-v1 | /tmp/look-now.png | 5c4285258a36d4b6 | 5 boxes · 50 lines · 21 labels | CLEAN. Thin full-width colour-coded lines; candles fully visible; SMC zones subtle (blue 1.1350-1.1375, green band 1.1430-1.1470); SMC labels CHoCH ×5, EQH, EQL, BC. Matches the library signature. |
| 2 | D2 lqz-plutus | /tmp/panel-D2-1H.png | b2b5b5ba552ffc0a | 0 boxes · 58 lines | CLEAN, BEST MATCH. 58 thin full-width lines; ~35 green #3E8A46 below price, ~23 red #7F3613 above; irregular spacing; nothing occludes the candles. This IS the measured library rendering. |
| 3 | D1 lqz-luxalgo | /tmp/panel-D1-1H.png | e7694c1692c68e42 | 117 boxes · 36 lines | WRONG. Large filled blocky zones (green/red/maroon/grey) from the LuxAlgo detectors' OWN primitives dominate; only 36 thin LQZ lines. Reads as three original renders PLUS a layer, not "one display". |

## THE FRAME-SWAP FIX (why these looks are trustworthy)
Operator report: *"the colors are really bright which looks like multiple rounds are stacking on top
of each other."* Root cause: every drawing is `locked` (so the user cannot drag/delete indicator
output) and the store's `remove()` honours that lock — so `clearDrawings()` removed NOTHING and each
compile stacked a fresh frame. **Every visual verdict taken before commit `122eb16` was on
accumulated layers.** Fixed by unlocking before removing.
Evidence: `cleared: 58` (D2) and `cleared: 153` (D1) in the live state after the fix.

## PER-DELIVERABLE VERDICT
- **D2 lqz-plutus — PASS (rendering).** 58 lines, correct palette, correct sides, full width, no stacking.
- **D3 plutus-vision-v1 — PASS (rendering).** Clean; SMC + LQZ coexist; the SMC zone fills still read
  heavier than the library but do not bury the lines.
- **D1 lqz-luxalgo — FAIL (rendering).** The three detectors' own primitives are still drawn.
  OPEN: suppress their `box.new`/`line.new` calls while keeping their DETECTION (the taps), so the
  consolidated LQZ layer is the only display.

## WHAT RUNNING TAUGHT THAT READING COULD NOT
1. A green box count is not a look. D3 read "39 boxes PASS" while the frame was a barcode.
2. A lock that protects the user also blocks the renderer — the two must be separated explicitly.
3. The engine's default 50-line cap silently dropped zones: D2 was drawing 112 zones into 50 lines.
4. `syminfo.mintick` is 1e-16 here, so a tick-based band floor renders invisible bands.
5. A fixed -500 bar left margin is NEGATIVE below 500 bars of history and those boxes are DROPPED
   silently — 15m=325 bars meant boxes=0 with no error.
6. Level volume is not the cluster's problem; 300 vs 1500 levels both gave 0 zones in D1's old form.
