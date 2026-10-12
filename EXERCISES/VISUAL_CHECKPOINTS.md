# VISUAL CHECKPOINT CHAIN — Pine IDE (the ONLY accepted success surface)

Law (operator): a success claim is only valid with a screenshot of the rendered Pine script in
the Pine IDE, LOOKED AT, reasoned from first principles, and checked for regression against the
last five checkpoints. Everything else is a preflight.

Chain (oldest → newest). A new checkpoint is only allowed if it is a tangible improvement.

---

## V01 — baseline (empty chart) · `pine_ide/V01_baseline_empty_chart.png`
- Editor held the **placeholder** `EMA Ribbon` smoke script — not the Plutus indicator.
- Chart **empty**, with a named refusal on screen: `FIXTURE_CELL_ABSENT: EUR/USD 1H — the
  fixture carries DXY 1H (HTTP 200)`.
- Verdict: **DEFECT** — wrong script + wrong pair ⇒ nothing rendered.

## V02 — stale capture · `pine_ide/V02_stale_capture.png`
- Byte-identical to V01 (sha `8767a6b8…`).
- Cause found by reading the page, not the image: CDP reported `FIXTURE · DXY · 1H · 508 bars`
  while `import -window` still returned the old frame. **The capture was stale, not the app.**
- I was also driving one Chrome (CDP on `127.0.0.1:9222`) while photographing a **different**
  Chrome window. Two instances were live.
- Verdict: **DEFECT** — instrument error, not render error. Discarded.

## V03 — indicator rendered · `pine_ide/V03_indicator_rendered.png`
- One Chrome instance; killed the strays; loaded `plutus-vision-v2.pine` on DXY 1H.
- Editor holds the real source (`//@version=6`, `plutus-vision-v1`).
- Page state: `COMPILED 1152ms · 2 plots · 5 boxes · 0 lines · 5 labels · 0 markers · 798 segs ·
  1 tables (geometry absent) · bars 508`.
- Chart shows **5 IP zone bands** with labels:
  `IP Resistance Ceiling | Moderate | 37% ZFP` · `Upper IP Resistance | Moderate-Heavy | 27%` ·
  `Equilibrium Zone | Moderate-Heavy | 27%` · `Mid-Range Support | Moderate | 37%` ·
  `Key IP Support | Moderate | 37%`.
- Verdict: **PASS — forward progress.** Rendered indicator, correct script, correct pair.
  Strictly better than V01/V02. No regression.

---

## THE MEASUREMENT THAT MATTERS (V03) — the crux, proved from the engine

Read from the engine's own geometry (`POST :9741/run`, `sourceSha 9edffa88b51b`, pinets 0.10.0),
not inferred from pixels:

| Zone | bt | tp | width (DXY) | **geometric ZFP** | label says |
|---|---|---|---|---|---|
| IP Resistance Ceiling | 101.564 | 101.645 | 0.081 | **5.1%** | 37% |
| Upper IP Resistance | 101.384 | 101.466 | 0.081 | **5.1%** | 27% |
| Equilibrium Zone | 101.148 | 101.229 | 0.081 | **5.1%** | 27% |
| Mid-Range Support | 100.893 | 101.010 | 0.117 | **7.3%** | 37% |
| Key IP Support | 100.539 | 100.619 | 0.080 | **5.0%** | 37% |

Canon §10.8: `ZFP = width / ref × 100`, DXY ref = 1.60. Canon §6.4.1: **ZFP < 20% ⇒ HARD WALL ⇒
a BS reaching it MUST predict RWL (reversal)**.

**Result: every zone is geometrically a HARD WALL (5.0–7.3%) yet is LABELLED "Moderate" /
"Moderate-Heavy" (27–37%).** The label is 5–7× the true value and crosses the 20% threshold in
the wrong direction — so every zone is misclassified out of HARD WALL and into MID-RANGE, which
flips E2's terminal shape on **every** zone.

**The proof it is not width-derived:** Mid-Range Support is 0.117 wide (7.3%) and Key IP Support
is 0.080 (5.0%) — different widths — yet **both print "37%"**. A geometric quantity cannot
produce the same percentage from different widths. The label is degree-derived.
This is `ENGINE1_V8_VS_MINE.md:21`/`:108`, now confirmed by measurement rather than by note.

---

## SEPARATE, LESSER OBSERVATIONS FROM V03 (not yet fixed)

1. **Table geometry absent** — `1 tables (geometry absent)`. The 2×17 info table (E2 chain +
   E3 trade rows) does not paint. Matches the recorded residual.
2. **`0 lines`, `0 markers`** — the LSZ / option-strike layers are not present in the render.
3. Header label reads **"Plutus Vision v1"** while the file is `plutus-vision-v2.pine` — a
   version-label mismatch.
4. Chart title area shows `Plutus Vision v1` as a central watermark; harmless.

---

## RIG FACTS LEARNED (so the next session does not repeat them)

- Display: `agent-display.sh up` → **`:3`** at **1024×600**. The rig's launcher assumes a bigger
  window (1626×931); I launch Chrome at `1020×556` to fit.
- **Chrome MUST get `--ozone-platform=x11`** (plus `env -u WAYLAND_DISPLAY GDK_BACKEND=x11`), or
  it goes Wayland-native and dies with `Failed to initialize Wayland platform`.
- **ONE Chrome instance only.** Two instances both bind 9222 (`127.0.0.1` vs `[::1]`) and you can
  end up driving one while photographing the other. Symptom: "the UI did not update".
- **`pkill -f "<string>"` self-matches the shell running it** (the pattern is in its own cmdline)
  and kills the command mid-flight. Use a bracket pattern (`[d]s-chrome`) or kill by explicit PID.
- **`import -window` can return a stale buffer.** Verify freshness by reading the page's own state
  over CDP and requiring the screenshot to contain that marker text.
- Camera/state instrument: `EXERCISES/cdp.py` (`info` / `eval '<js>'` / `shot <png>`).

---

## SOURCE ANCHORS (each verified by printing the referenced line)

- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:3860` — §10.8, the
  geometric ZFP definition (`zoneW / refRange * 100`) that V03's labels do not satisfy.
- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:1819` — §6.4.1, the
  ZFP-conditioned transition table: `< 20% => RWL (reversal)`. Every V03 zone is < 10%.
- `ENGINE1_V8_VS_MINE.md:21` — the v8-vs-live table row naming `zfp_from_degree(conf)` as the
  substituted quantity.
- `ENGINE1_V8_VS_MINE.md:108` — the same defect stated as the operator's crux point.
- `EXERCISES/EXERCISE_LOG.md:1` — the Phase-A exercise log where the geometric ZFP was first
  tested against real bars.

## WHY THIS DOCUMENT EXISTS

The operator's law for this build: the ONLY accepted success surface is a screenshot of the Pine
script rendered in the Pine IDE, looked at with real reasoning, and compared against the previous
checkpoints for regression. Tests and scripts are permitted as PREFLIGHTS only — they may gate
the work, but they can never be the success condition. A test that passes while the chart renders
nothing is not a result.

Consequence for how work proceeds here:
1. Any claim must name its checkpoint (V-number) and its PNG.
2. The PNG must be LOOKED AT and the found/missing/wrong named.
3. The checkpoint must be a tangible improvement over the previous ones, or it is discarded and
   the defect fixed before continuing.
4. A regression blocks all forward motion until it is repaired and re-photographed.
