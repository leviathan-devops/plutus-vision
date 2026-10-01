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
