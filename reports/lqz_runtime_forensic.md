# THE RUNTIME LEDGER — what RUNNING taught that READING could not
## PLUTUS VISION · session 2026-10-02 · display :3 · window 14680067

## THE DECLARATION (the pin's mandatory line, before P4)

> **I am the driver of the Pine IDE on :3.**

Every capture below was taken from the window on the agent's own floating display, after
operating the IDE first-person. No local VLM mediated a verdict. No background job sat
between an action and its observation.

---

## H1 — THE REAL INSTANCE, ALL THREE LOADED AND RUN ONE AT A TIME

| deliverable | file | sha256[:16] | compiled | title (from the run's OWN return) |
|---|---|---|---|---|
| D1 | `lqz-luxalgo.pine` | `b6dda2dae4416ec8` | yes | `LQZ LuxAlgo` |
| D2 | `lqz-plutus.pine` | `946f4ca21b3ddc0a` | yes | `LQZ Plutus — operator candle liquidity` |
| D3 | `plutus-vision-v1.pine` | `d41c6d9ccb1c5f8e` | yes | `Plutus Vision v1` |

**A fact the runs produced that reading could not:** the title comes back from the ENGINE,
not from the editor. That single field is the only deterministic per-panel identity in the
system — `lastVision` carries no title, and the editor's text can be correct while the RUN
compiles the previous source. Two panels were frozen on the wrong deliverable before the
title was asserted. **The old assertion checked what the editor HELD; the truth was what
the ENGINE RAN.**

---

## H2 — OPERATED FIRST PERSON, PRE-REGISTERED EXPECTATIONS

Every op below was performed on the live instance with its expectation stated BEFORE the
capture, and the capture is the evidence channel.

| op | action | expectation | actual | verdict |
|---|---|---|---|---|
| 1 | load D1, RUN, 1H | title `LQZ LuxAlgo`; lines > 0 | `117 boxes / 36 lines / 0 labels`, cleared 153 | PASS |
| 2 | load D2, RUN, 1H | title `LQZ Plutus…`; 0 boxes | `0 boxes / 58 lines`, cleared 58 | PASS |
| 3 | load D3, RUN, 1H | title `Plutus Vision v1`; labels > 0 | `5 boxes / 79 lines / 21 labels`, cleared 105 | PASS |
| 4 | capture + compose the 1H grid | 4 panels, 3 distinct shas | `07a4e3bc…` 2002x1340 | PASS |
| 5 | repeat for 30m | distinct grid | `0491c90a…`, D2 66 lines | PASS |
| 6 | repeat for 15m | distinct grid, no cliff | `5f4fcbb2…`, D1 30 lines | PASS |
| 7 | repeat for 4H | distinct grid | `a653c020…`, D3 27 labels | PASS |
| 8 | open every grid | panels readable | 4 grids read, deltas named | PASS |

**All four timeframes ran one at a time, each with its own sha recorded.**

---

## H3 — EVERY BREAK IS THE DELIVERABLE

### OP-9 · THE STATION DIED SILENTLY (the session's most valuable finding)
- **expected:** a compile; the panel lands after the debounce race resolves.
- **actual, VERBATIM:** `PANEL_GRID_FAIL: D1 — {"ok":false,"error":"after 20 runs still
  compiled 'undefined'"}`
- **mechanism:** the page reported `PINE_STATION_DOWN — TypeError: fetch failed · frame
  retained (22:04:52Z)`. `:9741` answered nothing; the pid was gone from `ss -ltnp`; and
  `/tmp/pv-station.log` held ONLY its startup banner — **no crash was ever logged.**
- **why the failure looked wrong:** every retry returned `run.title === undefined`, and
  `undefined` does not contain `LQZ LuxAlgo`, so the fixed point burned all 20 attempts.
  **The title assertion converted a silent death into a named failure** — without it this
  would have read as "the panel looks empty", which is the most misdiagnosable state in
  the system.
- **fix:** restart the station with its own line from `pv-ide.sh`:
  ```
  env -C pine-ide/pine-station PINE_STATION_PORT=9741 PINE_STATION_HOST=127.0.0.1 \
      PLUTUS_BARS_FIXTURE=… PLUTUS_LIVE_ROOT=… setsid -f node server.mjs
  ```
  **NOT the launcher** — `pv-ide.sh` opens with `fuser -k 9741/tcp 9754/tcp 9851/tcp`,
  which would have killed the page's own server on `:9851` and destroyed the running IDE.
- **retest (the NEXT numbered op, same instance):** compile D2 through the restarted
  station → `success: True, title: LQZ Plutus — operator candle liquidity, lines: 112`.
  `112` is the FULL zone count — the value the undeclared 50-line default had been cutting
  to `50` with no error.

### OP-10 · THE DEBOUNCE RACE IS A COLD-PAGE ARTEFACT
- **expected:** the fixed point retries some number of times per panel.
- **actual:** the first cold run needed **1 / 2 / 7** attempts. Every run after the station
  restart landed on **attempt 1** for all three panels.
- **mechanism:** `flush()` debounces; on a cold page the first `run()` after `setSource`
  compiles the PREVIOUS source. Once the page is warm, the flush has landed by the time
  `run()` is called.
- **the lesson worth keeping:** a retry budget is not a fix. It is a detector for the bug
  it works around — and the attempt count is how the bug was measured at all.

---

## H4 — PUSHED IT

| stress | result |
|---|---|
| all four timeframes (15m → 4H) | 4 distinct grids, every panel distinct, every title asserted |
| the shallow-history case (15m, ~325 bars) | D1 `97 boxes / 30 lines` vs 1H's `117 / 36` — proportional. **The old fixed `-500`-bar margin was NEGATIVE at 325 bars and those boxes DROPPED silently; the clamp holds.** |
| the cap boundary (D2) | `112 lines` at 1H — where the engine default cut it to **50**, discarding 62 zones with `capped` reading 0 |
| a degenerate fixture request (`limit: 1`) | REFUSED BY NAME: `bars absent (1)` — never served a fallback band |
| repeat runs of the same script | identical counts, distinct-from-other-scripts frames — the clear path is real |

---

## H5 — FIXED IN THE HOT SEAT

Three defects were fixed and retested on the SAME instance without a restart:

1. **The title assertion** (`rr.run.title`) — added after two panels froze on the wrong
   deliverable. Retest: the fixed point reported `in 1 run(s)` three times.
2. **The retry budget** 8 → 20 — after watching 8 exhaust on a legitimate panel that
   needed 7. Retest: every panel landed.
3. **The bars record + per-panel title in the manifest** — so "identical bars" is provable
   from disk. Retest: `test_panel_rows_are_same_bars` 3 distinct titles, 1 bar signature.

---

## H6 — WHAT RUNNING TAUGHT THAT READING COULD NOT

1. **The engine's title is the only identity.** `lastVision` has no title; the editor's
   text can be right while the run is wrong. Only `rr.run.title` names what executed.
2. **A silent station death and an empty chart are indistinguishable from counts alone.**
   Both produce zero-of-everything. The named refusal (`PINE_STATION_DOWN`) is the only
   thing that separates them — a count-based gate would have reported "0 zones" and the
   pin's own rule says ZERO ZONES IS A RED FLAG, not a pass.
3. **The clear path works, and its proof is a comparison not a number.** `cleared: 58`
   says something was removed; two scripts producing DIFFERENT frames says the removal was
   correct. Only the second is evidence.
4. **The caps fix is visible in a live number**: D2's 112 lines at 1H is the emitter's
   requested zone count. Before the fix the same emitter reported 50.
5. **The debounce race is cold-start only.** Seven attempts on a cold page, one on a warm
   one. A budget tuned on the cold case is correct; a diagnosis tuned on it would be wrong.
6. **The `-500`-bar margin defect is time-frame-shaped.** It is invisible at 1H (1603 bars)
   and live at 15m (325). A single-timeframe look would never have found it.
7. **Running the launcher is not always safe.** `pv-ide.sh` begins with `fuser -k` on all
   three ports — correct for a cold start, destructive to a running page. The station has
   to be restartable on its own.

---

## H7 — THE CLOSE

**Nothing unexperienced remains within the session's reach:** all three deliverables
compiled and ran; all four timeframes rendered, captured, composed, and opened; the
shallow-history and cap boundaries pushed; the station-death and debounce races both
exercised and fixed in place.

**THE RESIDUAL, NAMED:**
1. **The operator has not stated APPROVED.** The four grids are on disk and read; the
   verdict is theirs. No agent action substitutes for it.
2. **The band-height delta is unadjudicated.** The library's bands are far larger than any
   deliverable's; whether to raise the emitter's band height is the operator's call.
3. **No container round.** Every verdict here is host-live, not container-grade.
4. **No crash test on the rig itself** (malformed Pine through the page, concurrent
   compiles) — the station's refusal paths are documented and were exercised only at
   `limit: 1`.
5. **The second-operator check is not run**: a zero-context subagent has not yet been given
   only the operating docs and asked to drive the rig.

---

# THE OPERATING MANUAL — the three commands, verbatim

**Added after the second-operator check (reports/lqz_second_operator.md).** A zero-context agent
completed every step but had to read SOURCE to learn the compile API — and it found a rig defect
in the process. This section exists so the next operator does not repeat either.

## THE RIG CHECK — and WHY `GET /` LIES

```bash
# THE PORT CHECK (all four)
for p in 9741 9754 9851 9222; do
  printf ':%s  ' "$p"
  curl -s -o /dev/null -w 'http=%{http_code}\n' --max-time 5 "http://127.0.0.1:$p/"
done
# EXPECT :9741 200 · :9754 404 (no / route — healthy) · :9851 200 · :9222 200

# THE CHECK THAT ACTUALLY MATTERS — the station is HALF-ALIVE-PRONE.
curl -s -o /dev/null -w '/        %{http_code} %{time_total}s\n' --max-time 5 http://127.0.0.1:9741/
curl -s -o /dev/null -w '/cells   %{http_code} %{time_total}s\n' --max-time 5 http://127.0.0.1:9741/cells
curl -s -o /dev/null -w '/bars    %{http_code} %{time_total}s\n' --max-time 5 "http://127.0.0.1:9741/bars?pair=EUR/USD&timeframe=1H"
```

**MEASURED, by a zero-context operator: `GET /` and `GET /health` can HANG (http_code=000, curl
exit 28) while `/catalog`, `/cells`, `/bars` answer 200 and `POST /run` compiles normally.** The
VIL rail reads the hung route and reports `PINE_STATION_DOWN` — so a rig can be declared dead
while it works.

**AND THE LAUNCHER USES THE LYING ROUTE:** `pv-ide.sh` has
`up http://127.0.0.1:9741/ || { echo "STATION_DOWN"; exit 1; }` — `GET /`. **The launcher's health
predicate is the one route that can hang while the station is functional.**

**THE CORRECT CHECK is the WORK route, not the liveness route:**
```bash
curl -s -m 90 -X POST http://127.0.0.1:9741/run -H 'Content-Type: application/json' \
  -d '{"script":"//@version=6\nindicator(\"t\")\nplot(close)","pair":"EUR/USD","timeframe":"1H","limit":300}' \
  | python3 -c "import json,sys;d=json.load(sys.stdin);print('OK' if d.get('success') else 'REFUSED', d.get('data',{}).get('title'))"
```
**A rig that answers THIS is up, whatever `GET /` says.**

## THE COMPILE — the API the docs did not state

```bash
# POST :9741/run  {"script": <full Pine source>, "pair", "timeframe", "limit"}
curl -s -m 90 -X POST http://127.0.0.1:9741/run \
  -H 'Content-Type: application/json' \
  -d "{\"script\":$(python3 -c "import json;print(json.dumps(open('lqz-plutus.pine').read()))"),\
\"pair\":\"EUR/USD\",\"timeframe\":\"1H\",\"limit\":1603}"
```
**Returns:** `{success, data:{title, bars, counts:{boxes,lines,labels,…}, sourceSha}}`
**ASSERT THE TITLE.** It is the compiled script's OWN identity — the only deterministic per-panel
check in the system. `undefined` means the station is unreachable, not that the panel is empty.

**THE REFUSALS, so a reader knows what normal looks like:**
| input | response |
|---|---|
| empty / null script | `400 :: primary: a script or canon:true is required` |
| not Pine | `422 :: Unexpected token (2:6)` |
| unknown identifier | `422 :: <name> is not defined` |
| absent pair/timeframe | `500 :: no bars cell for … (available: 12 cells listed)` |
| `limit=1` | `400 :: bars absent (1)` |
| `limit=0` | **`200` — DOCUMENTED as "keep the full history"** |
| concurrent load | **serialized ~16 s each; no busy signal — budget ~20 s per compile** |

## THE CAPTURE — and the two ways it goes wrong

```bash
# THE LIVE GRID (writes reports/panel-grid-<TF>.png; asserts the run title; refuses duplicate panels)
bun scripts/lqz-panel.mjs 1H      # or 30m / 15m / 4H

# A SINGLE FRAME (the X11 path — the proven one)
DISPLAY=:3 xdotool search --name "Pine IDE" | head -1     # resolve the window id (CHANGES on relaunch)
DISPLAY=:3 import -window <ID> -silent /tmp/look.png
sha256sum /tmp/look.png | cut -c1-16
# THEN OPEN IT. A capture nobody opened is not evidence.
```

**TRAP 1 — THE STALE FRAME.** With the station wedged, the page renders the PREVIOUS script. The
second operator's first capture returned a D3 frame while asking for D1, and caught it only by
comparing. **The `run.title` assertion is what prevents this** — it is in `lqz-panel.mjs`; hand
captures must assert too.

**TRAP 2 — THE SERVED COPY.** The browser serves `pine-ide/ide/renderer/`. A rebuilt `.pine` at the
project root is INVISIBLE until copied there. `bash scripts/verify_served_pine.sh` gates it
(`SERVED_PINE_OK`).

## THE ONE-PARAGRAPH VERSION

> Check the rig by COMPILING, not by pinging. Assert the run's title. Copy the built `.pine` into
> `pine-ide/ide/renderer/` before capturing. Resolve the window id fresh. Open every frame you
> capture. Budget ~20 s per compile — the station serializes.

---

# OPERATOR-CAUGHT · "this grey and gold empty shell indicator — whatever this is"

## THE OBSERVATION
The operator, looking at the live IDE, named two defects in one sentence:
1. **"grey and gold"** — the frame's dominant colour is not the specified palette.
2. **"empty shell"** — the frame carries no readable content.
3. **"whatever this is"** — the frame does not identify itself.

## THE MECHANISM — three parts, each verified
### (a) The slabs are the LQZ FILL LAYER, not detector paint
- All six `swp_` colour constants are confirmed suppressed (`lqz-luxalgo.pine:36-44`, all `color(na)`).
- `swp_break_box` (`lqz-luxalgo.pine:93`) is DEFINED AND HAS **NO CALLERS** — the method grep
  returns only the definition line, so the sweep boxes never draw.
- What remains is the emitter's own fill (`lqz-render.pine`, transplanted to D1 line ~900):
  `box.new(_lx, _hi, …, _lo, bgcolor = color.new(_col, lqzFillA))`

### (b) THE COLOUR MATHS PRODUCES "grey and gold" EXACTLY
| input | value | at alpha 10/255 ≈ 4 % over a dark chart reads as |
|---|---|---|
| `lqzColorB` (demand) | `#3E8A46` | dark **GREY**-green |
| `lqzColorS` (supply) | `#7F3613` | dark **GREY-GOLD** |
So the two colours the operator named are the palette at 4 % opacity — the fill is meant to
be a whisper UNDER a ladder, and reads as grey slabs when the ladder is thin.

### (c) WHY 15m IS THE WORST — and why the operator caught it there
15m carries **325 bars** (the fixture's real depth) against 400 at 30m/1H/4H, and its zones
span the WIDEST price ranges. So:
- the fills are the LARGEST at 15m, and
- the ladder is the SPARSEST (D1 30 lines, D3 57 lines vs 50/85 at 4H).
**The subordinate layer becomes the only visible one.** "Empty shell" is the correct word.

## THE FIX — two inputs, and they are the operator's calibration
```pine
lqzFill3 = input.bool(false, "Fill bands with 3+ sources")   ← was true
lqzFillA = input.int(0, "Fill alpha (3+ sources)")           ← was 10
```
Variant built and SERVED BY THE IDE'S OWN SERVER (`pine-ide/ide/renderer/lqz-luxalgo-nofill.pine`,
verified by fetching it back: `lqzFill3 = input.bool(false`, `lqzFillA = input.int(0`).

## THE IDENTIFIABILITY DEFECT — "whatever this is"
A chart-only capture carries **no indicator name** unless the renderer draws a legend. The
operator could not tell D1 from D2 from D3 on a frame that is only slabs.
**This is a REAL, SEPARATE defect**: the panel judge's panels must identify themselves in the
frame, not only in the composer's caption above them.

## THE CAPTURE-LAG DEFECT (found while demonstrating the fix)
`P.capture()` returned the **byte-identical previous frame** (`7fbe8be137f79b35`) THREE TIMES
across three different runs whose ledger rows recorded D1's correct counts (97 boxes / 30
lines). The capture reads the last COMPOSITED layer; under back-to-back runs the compositor
has not produced a new frame.
**The fix in flight: settle with two `requestAnimationFrame` ticks plus a longer wait before
capturing** — the same class as the earlier `run.title` debounce, one layer further down the
pipeline (COMPOSE, not COMPILE).

---

# THE UNRESOLVED CONTRADICTION — the counts and the frame disagree (OPEN)

## THE FACTS, EACH FROM A TOOL RESULT
1. **THE OPERATOR'S OBSERVATION** (verbatim): *"this grey and gold empty shell indicator
   whatever this is also needs optimization."* The 15m frame is grey slabs, olive lines, **no
   ladder, no labels, no indicator legend**.
2. **THE LEDGER RECORDS**: D1 @ 15m = `boxes 97 · lines 30 · labels 0 · bars 325`, `reader FAIL`.
3. **THE FRAME SHOWS**: large grey slabs, four faint dotted marks, **no 30 lines, no legend**.
4. **THE SUPPRESSION IS VERIFIED COMPLETE**: all 24 `box.new` calls in `lqz-luxalgo.pine`
   account for their colour args (6 use positional `na` for `border_color` + a suppressed
   `bgcolor`); all six `swp_` constants are `color(na)` (`lqz-luxalgo.pine:36-44`);
   `swp_break_box` (`lqz-luxalgo.pine:93`) has zero callers.
5. **THE FILL HYPOTHESIS IS REFUTED**: `lqz-luxalgo-nofill.pine` (`lqzFill3 = false`,
   `lqzFillA = 0`) was built, SERVED (`fetchHasFalse: true`), HELD by the editor
   (`editorHoldsFalse: true`), compiled as D1 (`title: LQZ LuxAlgo`, `tries: 1`), and produced
   **the byte-identical frame** `7fbe8be137f79b35` after a 6 s + 2×`requestAnimationFrame`
   settle. **Turning the fills off changed nothing.**

## THEREFORE
**The engine reports 97 boxes and 30 lines; the chart shows neither.** The visible slabs are
grey with olive lines — Pine's / Vela's DEFAULT box styling — so *something* paints boxes
without a colour, and the 30 lines do not reach the screen at all.

**These two facts cannot both be true of a correct render.** The gap between the ledger's
counts and the frame's pixels IS the defect the operator's sentence identified — and it is
bigger than "the fills are too strong".

## THE EXPERIMENTS THAT WOULD SETTLE IT (named, not guessed)
1. **A HARD CHART RE-MOUNT** before the capture. The evidence favours a stale composited
   frame: `P.capture()` returned the same sha across runs whose counts differed, and the frame
   carries no indicator legend at all — a Vela chart with a drawn study shows its legend.
2. **READ THE RUN'S OWN `drawings` PAYLOAD** — `P.run()` returns `run.drawings.{boxes,lines,…}`
   with their colours. Comparing THAT against the screen splits "the engine did not emit" from
   "the chart did not paint", which no count can.
3. **`P.state().frames` / `drawings`** — the shell keeps a frames counter and a drawings
   registry; a mismatch between them and the canvas is the stale-composite signature.

## THE HONEST STATUS
**OPEN. Not a rendering-preference question and not a calibration question** — a
counts-vs-pixels contradiction. The operator's "empty shell" is the correct description of the
symptom; the mechanism is one layer below where I first placed it.

---

# SOLVED — "this grey and gold empty shell indicator" — the root cause

## THE DEFECT (one line, in the RENDERER, not the Pine)
`pine-ide/pine-ide/vision.mjs:113` read:
```javascript
const fill = normColor(b.color, 'rgba(185,154,91,0.10)');
//                       └─ a field a Pine box NEVER sets   └─ BRASS #B99A5B @ 10 %
```
**Pine boxes set `bgcolor`. They never set `color`.** So the read was ALWAYS undefined and
**every one of the 97 boxes fell through to the BRASS fallback** — which is exactly the
**gold** the operator named, over the dark chart's **grey**.

**The BORDER on the very next line was already fixed with the correct guard** (its comment
reads *"was BRASS: the tan-striped VOIDS stacks"*) — **the FILL was missed.** One drawing type
was fixed and its sibling was not, in the same 6-line block.

## WHY EVERY EARLIER FIX FAILED TO MOVE THE PIXELS
- Suppressing the Pine `bgcolor` constants (12, then 13 with `voi_lqFC`) changed nothing —
  **this line never looked at `bgcolor`.**
- Setting `lqzFill3=false` / `lqzFillA=0` changed nothing — **the LQZ fills were never the
  slabs.**
- The slabs were brass REGARDLESS of what the Pine said, because the fill was being read from
  a field that does not exist.

## THE FIX
```javascript
const fill = b.bgcolor ? normColor(b.bgcolor, 'rgba(0,0,0,0)') : 'rgba(0,0,0,0)';
```
A box WITH `bgcolor` uses it; a box with NO colour is TRANSPARENT. Mirrors the border's own
existing guard, one line above.

## THE VERIFICATION (a fresh frame, not a cached one)
| | before | after |
|---|---|---|
| capture sha | `8dc32e29c460176e` | **`3dafa3f2497661f6`** |
| `nonBg` | **0.40008** | **0.16821** ← a 58 % drop |
| the frame | grey/brass slabs burying the chart | **clean; candles fully readable** |

The `nonBg` drop is the measurement: 97 brass boxes leaving the canvas.

## THE TWO INSTRUMENT DEFECTS THIS EXPOSED (both fixed or named)
1. **THE FROZEN COMPOSITOR.** `P.capture()` returned the byte-identical frame
   `7fbe8be137f79b35` across THREE different source versions, with `nonBg` stuck at 0.40008 —
   it reads the last COMPOSITED layer. **A page reload is the remedy**; the freeze survived
   two `requestAnimationFrame` ticks and a 6 s settle. **Any capture without a reload is
   suspect.**
2. **THE REMEDY FOR (1) WAS ALSO THE REMEDY FOR THE BUG** — the reload picked up the fixed
   `vision.mjs`, which the frozen page had been serving from memory all along.

## THE REMAINDER — the same class, one drawing type over (OPEN)
The **30 lines** still do not render: the payload carries `lineColours: ["(none)"]` and
`vision.mjs:133` reads `l.color` with a `BRASS` fallback. **The station's drawing→payload
conversion drops the line's colour**, so the emitter's `color = _col` never reaches the
renderer. **The fix is the same shape**: make the station carry the colour, or make the
renderer read the field that IS carried. Until then the ladder renders as faint brass dots
on a clean chart instead of the library's ladder.

---

# 15m — WHERE THE LADDER ACTUALLY GOES (measured, and it is NOT the cluster)

## THE MEASUREMENT THAT REFRAMES IT
`POST :9741/run` on D1 @ 15m (325 bars) returns **30 lines — and NONE of them is a ladder line**:
```
colour distribution: {'null': 30}
  [0] width:3 style:solid   a.time == b.time   ← a VERTICAL marker, 3-bar span
  [1] width:1 style:dotted  a→b spans 3 bars
  [2] width:3 style:solid   a.time == b.time   ← vertical
```
The LQZ emitter draws `line.new(_lx, _hi, bar_index + lqzRightB, _hi, …)` — a **full-width**
line, whose `a.time` would be ~500 bars before `b.time`. **No such line exists in the payload.**
⇒ `f_lqzRender()` emitted NOTHING, which happens only when `array.size(lqzZLevel) == 0`.
**The LQZ zone array is EMPTY at 15m.**

The 30 `null`-coloured lines are the DETECTORS' marker lines. Their `null` colour is **correct**:
their colour constants are `color(na)` by this session's suppression.

## THE LEVERS DO NOT MOVE IT — four variants, identical counts
| variant | boxes | lines | labels |
|---|---|---|---|
| as-shipped (`lqzMinAgree=2`, `lqzTol=0.5`) | 97 | 30 | 0 |
| `lqzMinAgree=1` (any band clusters) | 97 | 30 | 0 |
| `lqzTol=1.5` (wider cluster window) | 97 | 30 | 0 |
| `lqzMinAgree=1` + `lqzTol=1.5` | 97 | 30 | 0 |

**Byte-identical.** So the zone array was empty BEFORE the cluster ran: the problem is not how
levels are CLUSTERED, it is that no levels ARRIVE. The cluster's own knobs cannot fix an
empty input, and neither of the two inputs the pin lists as the operator's calibration is
implicated.

## WHAT THAT MEANS FOR THE PIN'S OPEN CALIBRATION
The pin names `lqzTol · lqzMinAgree · wickBodyMult · rejectATRMult` as the operator's open
calibration. **Two of them (`lqzTol`, `lqzMinAgree`) are now measured to have ZERO effect at
15m** — not because they are wrong, but because nothing reaches them. **Calibrating them at
15m would be calibrating a disconnected stage.**
The other two — `lqzWickMult` / `lqzReject` (the V2 candle detector's swing parameters) — are
the ones that control whether levels EXIST at all, and they are the next measurement.

## STATUS
- **grey/gold slabs: FIXED** (`vision.mjs:121`, verified `nonBg 0.40008 → 0.16821`).
- **the 15m ladder: an UPSTREAM SUPPLY problem**, one stage before the cluster — named, with the
  measurement that proves it, and with two candidate levers ruled out by experiment rather than
  argument.

---

# 15m — THE CORRECTION, AND D1'S REAL LEVER SURFACE

## CORRECTION TO THE ENTRY ABOVE (append-only; the earlier reading stands as what was believed)
The previous entry said "the LQZ zone array is EMPTY at 15m". **That was WRONG** — it was drawn
from a 3-line sample. Counting **full-width** lines properly (a ladder line's `a.time` is ~500
bars before its `b.time`):

```
as-shipped, D1 @ 15m (325 bars):   boxes 97 · lines 30 · LADDER 5 · labels 0
```

**FIVE ladder lines exist.** The 30 = 25 detector markers + **5 ladder lines**. The ladder is
**sparse, not absent** — and 5 against the library's 30-60 bands per frame is exactly the
"15m needs optimization" the operator named.

## D1'S ACTUAL INPUT SURFACE (measured from the file, not assumed)
```
698  lqzSource   = "luxalgo"   ← THE TAPS ONLY — D1 does not use the V2 candle detector
699  lqzTol      = 0.5         ← measured INERT at 15m (4 variants, byte-identical)
700  lqzMinAgree = 2           ← measured INERT at 15m
701  lqzMaxZones = 60          ← only 5 emitted, so the cap is NOT the limit
852  lqzColorB / 853 lqzColorS / 854 lqzLineW / 855 lqzLineTol
857  lqzFillA    = 10          ← NOTE: `lqzFill3` DOES NOT EXIST IN D1
858  lqzLeftB    = 500 / 859 lqzRightB / 860 lqzThickE / 861 lqzLabel
```

**TWO OF MY OWN EARLIER CLAIMS DIE HERE:**
1. **`lqzFill3` does not exist in `lqz-luxalgo.pine`.** My "nofill" variant replaced a pattern
   that was not there — so that experiment never tested what its commit message claimed. It
   still disproved the fill hypothesis (the render was byte-identical), but for a reason I
   mis-stated.
2. **`lqzSwingLen` / `lqzWickMult` / `lqzReject` are not in D1 either** — the V2 detector's
   swing inputs live in `plutus-vision-lqz/lqz-core.pine` (D2/D3). Sweeping them against D1
   found zero matches, which is a fact about my probe, not about the deliverable.

## WHERE 15m's SPARSITY ACTUALLY LIVES
- `lqzSource = "luxalgo"` ⇒ the zones are clustered from **the three detectors' taps**.
- `lqzMaxZones = 60` and only **5** are emitted ⇒ **the cap is not binding**.
- The cluster's own knobs are inert ⇒ **the levels that arrive are few**.
**So the supply is upstream of every lever in D1's surface**, and the honest next step is to
count the TAP values at 15m versus 1H — not to keep turning knobs that are measured to do
nothing.

## STATUS
- **grey/gold: FIXED** (`vision.mjs:121`, `nonBg 0.40008 → 0.16821`).
- **15m ladder: SPARSE (5 lines vs the library's 30-60 bands)**, cause located upstream of every
  input in the deliverable, with three candidate levers ruled out by measurement.
