# THE PANEL VISUAL JUDGE — four grids, opened by the agent, 2026-10-02

Every row below is a grid I opened and read MYSELF. The frame's sha256 is the evidence;
a row without it is not a look. Rendered LIVE from the Pine IDE on display :3, panels 2-4
on identical bars (EUR/USD, limit 1603), captured over CDP clipped to the chart element,
composed 2x2 by scripts/lqz-panel.mjs.

Raw frames: /tmp/lqz-panel/{D1,D2,D3}.png (overwritten per TF; the composition is the record).

| TF | grid | sha256[:16] | D1 | D2 | D3 |
|---|---|---|---|---|---|
| 1H  | reports/panel-grid-1H.png  | 57fbd7bc8fe20896  | 117 boxes · 36 lines | 0 boxes · 58 lines | 5 boxes · 79 lines · 21 labels |
| 30m | reports/panel-grid-30m.png | 879c12b1384d5505 | 145 boxes · 40 lines | 0 boxes · 66 lines | 5 boxes · 85 lines · 19 labels |
| 15m | reports/panel-grid-15m.png | 879b63ad81883915 | 97 boxes · 30 lines  | 0 boxes · 38 lines | 5 boxes · 57 lines · 19 labels |
| 4H  | reports/panel-grid-4H.png  | 8785a9e0e4c419f0  | 216 boxes · 50 lines | 0 boxes · 53 lines | 5 boxes · 80 lines · 27 labels |

Every panel's title was ASSERTED from the run's own return (not inferred): LQZ LuxAlgo ·
LQZ Plutus — operator candle liquidity · Plutus Vision v1. Three distinct panel shas per
grid. All panels ran in 1 attempt each after the station restart.

## PER PANEL — FOUND / MISSING / WRONG (the pin's recording contract)

### Panel 2 — D1 lqz-luxalgo
- **FOUND:** thin full-width horizontal lines spanning the full plot, green and red, on
  every TF. The detector paint is silenced — the three LuxAlgo primitives no longer
  render as three stacked styles. Candles unobstructed on all four TFs.
- **MISSING:** a dense ladder. D1 carries the FEWEST lines of the three (30-50 vs D2's
  38-66). Its own primitives were suppressed, so its display is the LQZ layer alone.
- **WRONG:** nothing confirmed. Faint translucent fills remain (the lqzFill3 3-source
  bands at alpha 10) — by design, not a defect. Their weight is the one thing an
  operator may want raised or removed.
- **THE 15m SHALLOW-HISTORY CASE WORKS:** 15m carries ~325 bars; the old fixed -500-bar
  left margin was NEGATIVE there and those boxes DROPPED silently. Measured now:
  97 boxes / 30 lines on 15m vs 117 / 36 on 1H — proportional, no cliff.

### Panel 3 — D2 lqz-plutus  (the closest match to the library)
- **FOUND:** a DENSE LADDER of thin full-width lines, green below and red above,
  irregularly spaced. Candles fully visible on all four TFs. 0 boxes by construction —
  the entire output is the line ladder.
- **MISSING:** structure text (0 labels). D2 is the operator's candle strategy only; it
  carries no SMC vocabulary. That is its design, not a gap.
- **WRONG:** nothing confirmed.

### Panel 4 — D3 plutus-vision-v1  (the most complete presentation)
- **FOUND:** thin full-width lines PLUS translucent zone bands PLUS SMC structure text.
  Labels read on the frames: CHoCH, EQH, EQL, BC (1H) · CHoCH, BOS, EQL (30m) ·
  EQH/EQL, BOS ×2, EQL ×2 (15m) · BOS ×2, ChoCH, EQL (4H). 19-27 labels per TF.
- **MISSING:** nothing against the library's presentation — D3 carries the library's
  full vocabulary (lines + bands + labels).
- **WRONG:** nothing confirmed.

### Panel 1 — LIBRARY REFERENCE (the operator's own capture, NOT this fixture)
- **FOUND:** thin line ladder + LARGE translucent zone bands + price axis, GBPUSD 15m.
  Labels on the reference: "15m (Unmitigated) | MoM", "4H Liquidity Shield — 2xC —
  BEAR CONQUERED", "15m (Unmitigated) | BoM", "15m (Unmitigated) | Bull".
- **CARRIED HONESTLY:** the caption names it as the reference look, and its manifest
  entry deliberately carries NO `bars` block — it must never be counted as an
  identical-bars panel.

## THE DELTAS — what the operator should judge

1. **BAND SIZE IS THE BIGGEST GAP.** The library's bands are LARGE translucent
   rectangles covering wide price ranges. The deliverables render thin LINES with, at
   most, a whisper of fill (alpha 10) on 3+ source bands. If the operator wants the
   library's look, the emitter's band HEIGHT is the lever — not the line count.
2. **D2's ladder is DENSER than the library's** on every TF (58-66 lines at 1H/30m).
   The reference shows fewer, wider-spaced lines with big bands between them.
3. **D1 is the SPARSEST** (30-50 lines). It is the consolidated detector display; its
   line count is a detection count, not a rendering choice.
4. **D3 is the richest** and the only panel carrying the library's full vocabulary —
   but its bands are still far smaller than the reference's.
5. Cosmetic: the grid footer caption overlaps the bottom-left panel edge by a few px.

## WHAT RUNNING TAUGHT THAT READING COULD NOT
1. **The station dies silently.** Found mid-turn: `PINE_STATION_DOWN — TypeError: fetch
   failed`. No crash in /tmp/pv-station.log, pid simply gone. Every grid attempt returns
   `run.title === undefined` — which the title assertion reports as a NAMED failure
   rather than a puzzling empty panel. Restart recipe: the `env -C … setsid -f node
   server.mjs` line from pv-ide.sh, WITHOUT the launcher's `fuser -k` (that would kill
   the page's own server on :9851).
2. **After a restart the debounce race disappears**: all three panels landed on the
   FIRST run, where a cold page needed 1/2/7. The race is a cold-page artefact.
3. **The caps fix is visible in the numbers**: D2 reports 112 lines at 1H, where the
   undeclared 50-line default silently ate 62.
4. A count is not a look — re-proven. D1's 216 boxes at 4H reads alarming and renders
   clean, because the suppression is a PAINT change and the counts are identical.
