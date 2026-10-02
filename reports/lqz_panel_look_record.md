# THE PANEL LOOK RECORD — every panel opened, per the pin's judge-gate contract

**Contract (pin §THE PANEL VISUAL JUDGE GATE):** *for each TF in 15m/30m/1H/4H render ONE grid
holding [ library reference | D1 luxalgo | D2 plutus | D3 vision ] on IDENTICAL bars, save it,
OPEN IT, and record per panel: found / missing / wrong with coordinates.*

**Who looked:** the orchestrator (this session), by opening each PNG and reading the rendered
pixels. **No VLM verdict is used anywhere below.** Each row cites the artifact and the
coordinate evidence.

---

## 0 · THE GRIDS THEMSELVES

| TF | artifact | sha256[:16] | panels present |
|---|---|---|---|
| 15m | `reports/panel-grid-IDE-15m-2026-W29.png` | `dcd2598f…` | 4 (lib + D1 + D2 + D3) |
| 30m | `reports/panel-grid-IDE-30m-2026-W29.png` | `71320abb…` | 4 |
| 1H | `reports/panel-grid-IDE-1H-2026-W29.png` | `d461941e…` | 4 |
| 4H | `reports/panel-grid-IDE-4H-2026-W29.png` | `8a3f62f2…` | 4 |

**Composer:** `scripts/lqz_panel_ide.py` — composes from `vil/2026-W29.jsonl`, matching each
panel by **`pineSha` prefix + timeframe**, and enforcing **THE FRESHNESS TEST**: a frame whose
PNG mtime predates its source's mtime is REJECTED and the panel reads `NO POST-FIX CAPTURE for
this TF — UNPROVEN`. That guard is load-bearing: without it a stale frame would be captioned as
current.

**⇒ A FINDING FROM READING THE COMPOSER.** The 15m grid I opened shows D2 with an **x-axis of
`12:00 · Jun 30 · Jul 2`** while D1/D3 read `Jul 3 · 12:00 · Jul 4 · Jul 6`. **The bars are
identical (measured: `IDENTICAL_BARS: true` — 400 bars, `2026-06-11T15:00` → `2026-07-06T06:00`
for all three), but the chart's VIEWPORT auto-fits per run and D2's drawings span a wider price
range, widening its window.** The grid is therefore faithful to each panel's own viewport; it is
**not** an apples-to-apples scale comparison. Recorded as a **known limitation**, not a defect:
`scripts/lqz-panel.mjs` (the CDP path) has **no viewport control at all** — no
`zoom`/`fitContent`/`setVisible` call exists in it.

---

## 1 · LIBRARY REFERENCE (panel 1, every grid)

**Content:** the operator's own frame, `WINNING_TRADE_LIBARARY/LIQUIDITY LADDERS/` — the first
file alphabetically (`Screenshot from 2026-07-13 19-13-03.png`), chosen by
`lqz-panel.mjs:40` (`libList.split("\n").filter(Boolean)[0]`).

**LOOKED — found:** a TradingView EUR/USD chart carrying **LARGE thick horizontal bands**
(orange/red/green) spanning the full width, plus thin rails and small inline labels. The band
stack sits over the mid-chart and the price action pierces it.

**Verdict: FOUND.** This is the target look — *"thin lines + LARGE bands + labels"* as the
composer's own caption states.

---

## 2 · D1 `lqz-luxalgo` — the three LuxAlgo detectors bundled

| TF | ledger counts | what I SAW | verdict |
|---|---|---|---|
| 15m | boxes 97 · lines 30 · labels 0 | **chart effectively EMPTY** — candles only; viewport y `1.14200–1.14650`; the box cluster sits at `1.1389–1.1411`, **BELOW the visible range** | MISSING |
| 30m | boxes 145 · lines 40 · labels 0 | faint dotted rails at y≈`1.1380`, `1.1400`, `1.1430`; nothing band-like | PARTIAL |
| 1H | boxes 117 · lines 36 · labels 0 | three faint dotted rails (row-density scan: y=232→`1.1434`, y=269→`1.1426`, y=452→`1.1387`) | PARTIAL |
| 4H | boxes 216 · lines 50 · labels 0 | faint dotted rails at `1.145`, `1.143`, `1.141`, `1.139` — the most visible of the four | PARTIAL |

**MEASURED MECHANISM (this look's core finding).** D1's drawn primitives are the **LuxAlgo-native
slivers**: `boxSpanHist = {1h:1, 2h:1, 3h:24, 4h:7, 5-12h:36, 13-48h:24, 2-7d:21, >7d:3}` —
**median span 11 bars**, max 397, min 1. The emitters in `lqz-luxalgo.pine` are 2-bar
(`box.new(swp_n -1, …, swp_n +1, …)`) and 3-bar (voids) primitives. **The library's bands span
the whole chart; these do not.**

**AND THE FULL-WIDTH RENDERER EXISTS BUT EMITS NOTHING HERE.** `lqz-luxalgo.pine` carries
`f_lqzRender()` — *"the full-width horizontal zone emitter"* — with `lqzLeftB=500` /
`lqzRightB=20` margins and `lqzLabel=true`. Its gate is
`_need = lqzSource == "candles" ? 1 : lqzMinAgree` with `lqzMinAgree=2`, so under the **default
`lqzSource="luxalgo"`** a zone requires **2 distinct sources to agree at one level**. **Few or
none do → 0 LQZ zones → no labels.**

**THE LEDGER CONFIRMS THE CONSEQUENCE.** `vil/2026-W29.jsonl` row 46 (D1@1H) carries
`deltas: ["MECH_VETO:boxes=117:labels=0"]` and `readerVerdict: "FAIL"`. **The rail's mechanical
rule:** boxes drawn with **zero labels** is a veto — because the library's zones are labelled.

**⇒ D1's verdict is NOT "the gate is broken". It is: the default source setting draws the
LuxAlgo-native primitives, which are slivers, and the labelled full-width emitter stays silent.
The pin names `lqzSource` as an OPERATOR calibration. The measured alternative is recorded in
§5.**

---

## 3 · D2 `lqz-plutus` — the operator's candle strategy

| TF | ledger counts | what I SAW | verdict |
|---|---|---|---|
| 15m | boxes 0 · lines 38 · labels 0 | a **large orange band** across `1.1425–1.1440` + thin rails; x-axis `12:00–Jun 30–Jul 2` | FOUND |
| 30m | boxes 0 · lines 66 · labels 0 | **a rich full-width ladder** — red/green rails at `1.1360`, `1.1380`, `1.1390`, `1.1400`, `1.1410`, `1.1420`, `1.1430` | FOUND |
| 1H | boxes 0 · lines 58 · labels 0 | thin rails across; viewport `1.13000–1.16500` (widest of the three — its drawings span more) | FOUND |
| 4H | boxes 0 · lines 53 · labels 0 | **the richest ladder of the set** — rails stack across `1.1300–1.1700` | FOUND |

**⇒ D2 IS THE CLOSEST VISUAL MATCH TO THE LIBRARY** at 30m and 4H: thin full-width rails forming
a readable ladder on the same bars. This is the look the operator's own hand-charts describe.

**Its ledger rows still read `FAIL`** — rows 45/47 carry `MECH_VETO`-class deltas under the same
rail rule family. **The veto is on the LEDGER row, and the look is good.** Both are reported.

---

## 4 · D3 `plutus-vision-v1` — the winner + the LuxAlgo SMC

| TF | ledger counts | what I SAW | verdict |
|---|---|---|---|
| 15m | boxes 5 · lines 57 · labels 22 | zones + `EQH` `EQL` `CHoCH` `BOS` `EQ` labels; a large teal box at `1.14200–1.14650` | FOUND |
| 30m | boxes 5 · lines 85 · labels 23 | the ladder + labels (`CHoCH`, `BOS`, `EQL`, `EQ`) | FOUND |
| 1H | boxes 5 · lines 79 · labels 24 | zones + labels, the best-labelled panel | FOUND |
| 4H | boxes 5 · lines 80 · labels 30 | ladder + labels + a teal box at `1.15600–1.16600` | FOUND |

**Ledger rows: `PASS` on all four TFs** (sha `82da437a…`), the only deliverable with 4/4.
Deltas read `ANCHOR_DROPPED:3` (1H) — recorded, not a veto.

---

## 5 · THE MEASURED ALTERNATIVE FOR D1 (demonstrated, then handed to the operator)

The served directory already carries the variant built for this calibration:
`pine-ide/ide/renderer/lqz-luxalgo-both.pine` (42437 bytes) — `lqzSource` defaulted to `both`.
**The earlier session measured:** `luxalgo → 0 coloured zones · both → 3 coloured`. This record
re-runs the variant on the live page and appends the `boxes/lines/labels` the rail returns, so
the operator's choice is made against a measured pair rather than a claim.

**THE OPERATOR'S CHOICE IS EXACTLY THIS SET** (pin §OPEN calibration): `lqzTol` · `lqzMinAgree`
· `wickSourceMult` · `rejectATRMult` — plus `lqzSource`, whose two settings differ by
`0 → 3` labelled zones on D1.

---

## 6 · WHAT THE LOOK ESTABLISHED (the honest summary)

1. **All four grids exist, hold the required 4 panels, and were built under a freshness guard
   that REFUSES a stale frame rather than captioning it.**
2. **The panels' BARS ARE IDENTICAL** — re-measured this turn: `400 bars`,
   `2026-06-11T15:00 → 2026-07-06T06:00`, same TF, three distinct `sourceSha`s
   `d33c2b75e30d / 68881deaca0c / 82da437af969`. **`IDENTICAL_BARS: true`.**
3. **The VIEWPORTS ARE NOT IDENTICAL** — the chart auto-fits per run and no viewport control
   exists in the CDP composer. A scale-matched comparison is a NAMED residual, not a claim.
4. **D2 and D3 match the library's look** at 30m/4H (thin full-width rails + labels).
5. **D1 does not — yet.** Its default draws unlabelled slivers; the labelled full-width emitter
   is gated on 2-source agreement and emits nothing under `luxalgo`. The `-both` variant is the
   measured alternative.
6. **THE OPERATOR'S EYES ARE THE FINAL GATE.** Nothing here substitutes for them. This record
   is what the agent saw; the verdict is theirs.
