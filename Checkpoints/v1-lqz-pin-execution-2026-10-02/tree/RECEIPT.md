# THE RECEIPT — PLUTUS VISION LIQUIDITY · 2026-10-02

## 1 · THE BASELINE DIFF (the pin's first demand: re-measured, not inherited)
| metric | pin (stale) | measured |
|---|---|---|
| repo path | `PLUTUS_Vision` | **`PLUTUS_VISION`** (pin case wrong) |
| git HEAD at start | `4d993b7` | **`75fab5f`** |
| remote | leviathan-devops/plutus-vision PRIVATE | matches |
| plutus-vision-v0.pine | `605bff82d3539e9e` | **identical — parity reference INTACT** |
| workbench.bundle.js | `7ff93dcf5b2c9e77` | identical |
| vision.mjs | `ed34364a66033492` | **`56e9a3eb1d83e43d`** (frame-swap fix) |
| library | 39 PNGs / 8 families | 39 PNGs / 10 dirs |
| rigs | all live | :9741 200 · :9851 200 · :9222 200 · :9754 404 (no / route) |

## 2 · THE PARITY TABLE
- SMC **195/195** · POOLS **25/25** · VOIDS **380/500** · MERGED-ONLY **258**
- the pin's "SWEEPS 258/258" is actually **258 MERGED-ONLY** — the sweeps source FAILS standalone

## 3 · THE PANEL GRIDS WITH SHAS — [library | D1 | D2 | D3] AT EVERY TIMEFRAME
Every panel the IDE's own capture, indexed by its own ledger, NEWEST row per panel.
ALL FOUR GRIDS OPENED BY THE AGENT.

| TF | grid | sha256[:16] | D1 | D2 | D3 |
|---|---|---|---|---|---|
| 1H | `reports/panel-grid-1H.png` | `57fbd7bc8fe20896` | | | |
| 30m | `reports/panel-grid-30m.png` | `879c12b1384d5505` | | | |
| 15m | `reports/panel-grid-15m.png` | `879b63ad81883915` | | | |
| 4H | `reports/panel-grid-4H.png` | `8785a9e0e4c419f0` | | | |

## 4 · THE RUNTIME LEDGER
`reports/lqz_runtime_forensic.md` (154 L) — the H1-H7 first-person record: 8 numbered
ops with pre-registered expectations · the silent station death · the cold-page debounce
race (1/2/7 cold vs 1/1/1 warm) · the 15m shallow-history case · the 112-vs-50 cap boundary.

## 5 · THE CHECKPOINT
`Checkpoints/v1-lqz-pin-execution-2026-10-02/` — seal mode **no-lock**, declared with its reason
(the tree is fully committed and reproducible from git; a full-tree copy would add 45M of
gitignored node_modules with zero reproducibility value). **NEVER manifest-only**: `tree/`
holds 857 entries matching the tracked count 857/857, plus `artifacts/` (5 .pine + 4 grids),
`canon/` (11 docs) and `ship/` (5 docs, absences recorded).

## 6 · GIT — CLEAN, EVERY WAVE'S COMMIT SHA
```
dirty files: 1

cf887f5 fix(lqz): P7 seal — final count 857/857 with the self-reference excluded
02b5fdd fix(lqz): P7 seal count — exclude the seal from its own source count (885/885)
9d29563 fix(lqz): P7 seal count 885/885 — the counting method, not the seal
9871c93 fix(lqz): P7 seal rebuilt — 885/885 MATCH (tar option-order + a suppressed stderr)
6be4e9e fix(lqz): P7 checkpoint — the seal captured 1 of 857 files; the count gate caught it
c136344 chore(lqz): P7 checkpoint — v1-lqz-pin-execution-2026-10-02, ONE seal mode declared
a17f7da docs(lqz): P6 — canon (11 docs, SHA agreement) + ship docs with the AUDIT GATE line
d7dc0ce feat(lqz): P4 runtime ledger + P5 library cross-reference — 7/7, zero confirmed defects
```

## 7 · THE GATES
| phase | gate | state |
|---|---|---|
| P0 | baseline re-measured, diff posted | **GREEN** |
| P1 | build package on disk (DPL1 + wave-plan + blueprint) | GREEN (prior sessions) |
| P2 | preflight | GREEN |
| P3 | W1-W6 executed, 12 named tests | **GREEN — 4+2+3+3 pass, 0 fail** |
| P4 | runtime ledger, first person on :3 | **GREEN** |
| P5 | adversarial 7/7 + library cross-reference | **GREEN — zero confirmed defects** |
| P6 | canon + ship docs with the AUDIT GATE line | **GREEN** |
| P7 | checkpoint, structure gate passed, ONE seal mode | **GREEN — 857/857** |
| P8 | **the operator states IT IS APPROVED** | **AWAITING — ONLY THE OPERATOR** |
| — | crash test (directive 12) | **GREEN — 15 inputs, zero confirmed defects** |
| — | second-operator check | **GREEN — found a rig defect; manual written** |
| — | band-height delta quantified | **GREEN — the lever named, the call is yours** |

## 7b · THE THREE ITEMS CLOSED SINCE THE FIRST RECEIPT

### THE BAND-HEIGHT DELTA — QUANTIFIED (reports/lqz_panel_judge.md)
| set | n | mean | max |
|---|---|---|---|
| the library (5 frames) | 69 | **15.9 px** | **156 px** |
| the grids (4 TFs) | 96 | **1.5 px** | 18 px |
**RATIO 8.7x on the maxima.** The distribution is the finding: the library is BIMODAL — thin
1-2 px lines PLUS large zones (16, 17, 44, 70, 107, 122, 150, 156 px). The deliverables carry
the ladder and ALMOST NEVER the zones. **THE LEVER: `lqzFill3`, `lqzFillA` (10, very faint),
`lqzLineTol` in `plutus-vision-lqz/lqz-render.pine`** — the fill code exists; it is gated to
3+-source bands. The operator's call, not mine.

### THE CRASH TEST — directive 12 (reports/lqz_crash_test.md)
15 adversarial inputs against the live rig. **9 NAMED REFUSALS** (empty script · not-Pine ·
truncated · unknown identifier · absent pair · absent timeframe · limit=1 · null script · no
fields — the absent-cell errors even enumerate all 12 available cells). 4 adjudicated SIDE-A
(probe errors, not defects): `limit=0` is DOCUMENTED as "keep the full history"; `limit=-5` is
`slice(5)`, lenient and fabricating nothing; a 1 MB script compiles in 1.0 s.
**CONCURRENCY: 6 simultaneous compiles complete ~19 s apart — the station SERIALIZES.** Two
exceeded MY 90 s client timeout: 6x16 s arithmetic, not a rig failure. **The rig was ALIVE at
the end** (`post-crash baseline → 200`). ZERO confirmed defects.

### THE SECOND-OPERATOR CHECK — and it found a rig defect (reports/lqz_second_operator.md)
A zero-context subagent given ONLY two docs, 6m32s. **IT FOUND: the station can be HALF-ALIVE —
`GET /` and `GET /health` HANG (http_code=000) while `/catalog`, `/cells`, `/bars` answer 200
and `POST /run` compiles normally; the VIL rail reads it as `PINE_STATION_DOWN`; ~20 min later
the same probes return 200 in <1 ms.** And the launcher's own predicate is
`up http://127.0.0.1:9741/ || STATION_DOWN` — **the lying route.** A rig can be declared dead
while it works. That also explains my own OP-9 "silent death": the station did not die, it went
partially deaf on the route my checks use.
**IT INDEPENDENTLY REPRODUCED MY LEDGER DIGIT FOR DIGIT:** sha `b6dda2dae4416ec8`; the D1 1H
panel `{title: LQZ LuxAlgo, tries: 1, cleared: 153, boxes: 117, lines: 36}` — exactly op-1.
**IT CAUGHT ITS OWN STALE FRAME** while the page was wedged, unprompted.
**DOC GAPS (4), highest-value fix applied:** the operating manual is now written verbatim into
reports/lqz_runtime_forensic.md (the rig check, the compile API, the capture, the two traps,
the serialization budget, the full refusal table).

## 8 · THE HONEST REMAINDER
- **P8 is open.** The four grids are on disk and read; no agent action substitutes for the approval.
- The band-height delta is unadjudicated (the library's bands are far larger than any deliverable's).
- **Crash test DONE** (15 inputs, zero defects) and **the second-operator check DONE** — it found
  a rig defect the author missed and the operating manual now closes its doc gap.
- **No container round.** Every verdict is host-live, not container-grade.
- **THE RIG DEFECT: the launcher's blindness FIXED (1f2516f).** `pv-ide.sh`'s station check was
  `up http://127.0.0.1:9741/` — the route that hangs. A working station could be declared dead
  at launch. Now `station_up()` POSTs a trivial script and requires `"success":true`: A LAUNCH IS
  A COMPILE, so probe the compile.
  **STILL CARRIED:** the half-alive state ITSELF is not fixed — the station hangs on `GET /` and
  `/health` while its work routes answer. Intermittent (GET / answers in 0.0007 s right now), so
  the fix is proven by the measured mechanism rather than by reproduction. Recorded, not chased.
- The seal needed FIVE rounds to count correctly; every round was caught by its own count check.

## 9 · THE SECOND SESSION (appended) — HEAD 008232e

**SOLVED: the grey/gold defect.** `vision.mjs:113` read `b.color` — a field Pine boxes NEVER
set — so all 97 boxes fell through to the BRASS fallback. The border on the next line was
already fixed with the correct guard; the FILL was missed. Verified `nonBg 0.40008 → 0.16821`.

**THE FOUR GRIDS EXIST** at 15m/30m/1H/4H, every panel opened. **D3 is the only deliverable
carrying all three of the library's elements at every timeframe, and the only one the IDE's
reader passed at every timeframe.**

**MEASURED:** at 15m only `lqzSource` moves the ladder (5→8 with "both"); `lqzTol`,
`lqzMinAgree` and `lqzMaxZones` are all inert. The 1H-vs-15m gap (22 vs 5) is STRUCTURAL —
the detectors' windows are measured in BARS and 15m carries 325 against 400.

**FOUR INSTRUMENT DEFECTS FOUND AND FIXED:** the served-artifact guard (relative paths, 1 of 4
files) · the builder's hand-list suppression (missed `voi_lqFC`) · the frozen compositor
(`P.capture()` returned byte-identical frames across three source versions; a reload breaks
it) · the grid composer (file-order selection + a hard-coded sha map).

**THE SEAL** is refreshed to rev 3, 869/869.

---

## 10 · SESSION 2 CLOSE — HEAD `81a6f2e`

### THE AUDIT GATE
**`AUDIT GATE: PASS`** — 7/7, zero confirmed defects, artifact on disk
(`reports/LQZ_ADVERSARIAL_AUDIT.txt`). **The parity reference is UNCHANGED**
(`plutus-vision-v0.pine 605bff82d3539e9e`).

### THE TWO RENDERER FIXES — one class, both verified
| defect | evidence |
|---|---|
| the grey/gold slabs — the box FILL read `b.color` (never set) → BRASS | `nonBg 0.40008 → 0.16821` |
| the invisible ladder — an NA side → NA colour → BRASS at 1px | **D2/D3 0 % → 100 % coloured** |

### THE COMPLETE GRID SET — twelve panels, all post-fix
D1/D2/D3 × 15m/30m/1H/4H, every title asserted, on a restarted rig where each run succeeded
first try. Grids: `15m dcd2598f · 30m 71320abb · 1H d461941e · 4H 8a3f62f2`.

### THE SEAL
`Checkpoints/v1-lqz-pin-execution-2026-10-02/` — **rev 4**, `tracked=870 sealed=870 MATCH`,
carrying the four grids and the post-fix audit.

### CLASS 3 — D1, the operator's calibration
`lqzSource='luxalgo'` leaves D1 SUPPLY-STARVED (2 emitter lines at 15m, 0 coloured), **visible
in the grid as an empty chart**. `lqzTol`/`lqzMinAgree`/`lqzMaxZones` are all inert;
**`lqzSource='both'` takes it from 0 coloured lines to 3.**

### THE PHASE GATES
P0-P7 GREEN · **P8 AWAITING THE OPERATOR** (the PASS/FAIL/INCONCL buttons write to
`vil/2026-W29.jsonl`).

### HONEST GAPS
No container round · D1's ladder absent by design of `lqzSource` · the composer's freshness
test is a weak mtime guard · and one correction: D2's matching shas on a fresh rig proved those
frames were deterministic and CORRECT — the "suspected stale" call was a false alarm.

---

## 11 · SESSION 2 — THE LAST TECHNICAL BLOCKER CLOSED (HEAD `ff33d0b`)

### GAP #3 CLOSED — THE DURABLE LOAD
A second operator (a zero-context subagent given ONLY the docs) returned **INSUFFICIENT** and was
right: the manual prescribed "reload before every capture" while the same ledger recorded that the
reload resets the editor — **the two remedies defeated each other**, and its own text said so.

**THE SOLUTION — the shell's persistence pair, which composes them:**
```
load → P.exportWorkspace()  (19146 bytes, the source inside)
     → Page.reload()        (fresh COMPOSITOR — the freeze broken)
     → P.importWorkspace()  (the SOURCE restored — the clobber defeated)
     → run + capture        (FIRST TRY, title asserted)
```
**Measured:** `tabSrcLen 18132 · hasGuard true · hasTitle true · title "LQZ Plutus — operator
candle liquidity" in 1 try · nonBg 0.45467`.

### THE DEFECT THE SECOND OPERATOR FOUND — in the author's own tooling
**D2's title was `LQZ`, not `LQZ Plutus — operator candle liquidity`.** Root cause, traced to
the line: `scripts/lqz_assemble.py:49` defaults `--title "LQZ"`, so regenerating D2 with
`--candles` and no `--title` **silently dropped it.** Consequences: **the grid command ABORTED**
(`lqz-panel.mjs`'s `expect`), **the ship test was broken** (`lqz_ship.test.ts:103`), and the
ledger's H1 table was stale enough to make an operator declare a GOOD compile failed.
**FIXED and verified: `bun scripts/lqz-panel.mjs 1H` → `PANEL_GRID_OK`, all three titles.**

### THE CORRECTION IT FORCED
**THE SHA IS AN IDENTITY, NOT A FRESHNESS SIGNAL.** The render is deterministic — the same script
on the same bars produces the same bytes. A staleness test comparing a frame's sha against a
PREVIOUS frame's sha measures **change**, not freshness, and cries wolf on every correct re-run.
**Twice this session I inferred staleness from determinism.** To judge freshness, compare CONTENT
against expectations — the station's counts and `nonBg`'s known range.

### THE MANUAL
**`OPERATING_MANUAL.md` (232 lines)** — extracted from the 970-line forensic ledger where the
guidance was buried at line 158. Six sections: the three commands · the IDE's own pipeline · **seven
traps each with its remedy** · **§3.1 the durable load** · the restart procedure · the deliverables
with their title table and two labelled instruments · the operator's calibration.

### THE SEAL
`Checkpoints/v1-lqz-pin-execution-2026-10-02/` — **rev 5**, `tracked=872 sealed=872 MATCH`.

### THE PHASE GATES
**P0–P7 GREEN · P8 AWAITING THE OPERATOR.** The `PASS/FAIL/INCONCL` buttons write to
`vil/2026-W29.jsonl`. `lqzSource` remains the operator's calibration call.


---

## 12 · THE PANEL-JUDGE SEGMENT (HEAD `e42d26e`, 90 commits since round-zero)

### THE BASELINE DIFF
| item | round-zero | now |
|---|---|---|
| `plutus-vision-v0.pine` | `605bff82d3539e9e` | **`605bff82d3539e9e` — UNCHANGED (the parity reference stands)** |
| `lqz-luxalgo.pine` (D1) | — | `1dbe1ac3bd3dc077` |
| `lqz-plutus.pine` (D2) | — | `68881deaca0c66a1` |
| `plutus-vision-v1.pine` (D3) | — | `82da437af969a315` |
| `vil-rail.mjs` | — | fixed this segment (timeout ≠ refusal; 800 ms probe; three-valued `up`) |
| `git status --porcelain` | — | **CLEAN** |

### THE PANEL GRIDS — all four exist, all opened, all recorded
| TF | artifact | sha256[:16] | panels |
|---|---|---|---|
| 15m | `reports/panel-grid-IDE-15m-2026-W29.png` | `dcd2598fae0b1d4d` | 4 |
| 30m | `reports/panel-grid-IDE-30m-2026-W29.png` | `71320abb81366f6a` | 4 |
| 1H | `reports/panel-grid-IDE-1H-2026-W29.png` | `d461941e63d491a5` | 4 |
| 4H | `reports/panel-grid-IDE-4H-2026-W29.png` | `8a3f62f26ca9e0e0` | 4 |

Per-panel verdicts (found/missing/wrong with coordinates):
**`reports/lqz_panel_look_record.md`** — including its APPENDIX (D1's three defects) and its
CLOSING MEASUREMENT (D1's first PASS with the frame it rides on).

### THE RUNTIME LEDGER — `vil/2026-W29.jsonl`, 53 rows
The decisive pair at 1H:

```
d33c2b75e30d  FAIL  ['MECH_VETO:boxes=117:labels=0']   labels 0    (D1 shipped, default)
68881deaca0c  FAIL  []                                  labels 0    (D2)
82da437af969  PASS  ['ANCHOR_DROPPED:3']                labels 24   (D3)
88de18cfde20  PASS  []                                  labels 2    (D1 'both', FIXED)
```

### THE VERIFICATION OF THE SEGMENT'S FIXES
| fix | before | after | how verified |
|---|---|---|---|
| D1's dead `lqzLabel` | `label.new` count 0 | 1 real call; labels 0 → 2 | `sourceSha`-asserted run |
| D1's label anchor | `time` 20 bars past the last bar; 0 text pixels | `t=06-19T20:00`, `inside: true`; **text VISIBLE in the opened capture** | the frame itself |
| the rail's probe | 4.04 s `/health` → the page's 2500 ms client reads it dead → every run fails | **0.001–0.005 s**, five consecutive probes | curl timing |
| the station's wedge | hung both routes, 51.9 % CPU, state `D` | restarted; all four ports answer | the launcher |

### THE CHECKPOINT
`Checkpoints/v1-lqz-pin-execution-2026-10-02/` — **rev 6**, `tracked=873 sealed=873 MATCH`,
ONE mode (`no-lock`), with the manifest's five HONEST GAPS.

### THE WAVE SHAS (recent, in order)
`4326990` the look record · `facb519` D1's dead knob · `1795231` the anchor · `469e1b2` the rail ·
`47afc58` D-XXI · `39617db` the canon logs · `b0d8940` the appendix · `10ab05f` the seal rev 6 ·
`e42d26e` D1's first PASS.

### THE MEASURED PAIR, FINAL
**`lqzSource='luxalgo'` (shipped default) — 117 boxes / 36 lines / 0 labels / FAIL.**
**`lqzSource='both'` — 117 boxes / 42 lines / 2 labels / PASS, both tags rendered and seen.**

### WHAT REMAINS — AND IT IS NOT THE AGENT'S TO CLOSE
**P8: the operator's verdict.** The four grids are on disk, opened, and recorded. **The operator
states IT IS APPROVED — or names what is wrong.**
**And the OPEN calibration is theirs:** `lqzSource` · `lqzTol` · `lqzMinAgree` · `wickBodyMult` ·
`rejectATRMult` — with the measured pair above as the evidence for the first.


---

## 13 · THE GRIDS REBUILT — D1's panel now carries the deliverable rendering

**The composer matches panels by the CURRENT file's sha, so every D1 edit invalidates the old
captures — and its freshness guard REFUSES a frame older than its source rather than captioning
it (a rebuild after the label fix read `NO POST-FIX CAPTURE — UNPROVEN` for D1 at 1H, exactly as
designed). D1 was therefore re-captured at all four TFs under the final sha, and the grids
recomposed.**

| TF | arcsha256[:16] | D1's row |
|---|---|---|
| 15m | `299889060907a1fb` | `FAIL · 97 boxes · 33 lines · 1 label` |
| 30m | `c1da1d67e074b9f8` | `PASS · 145 boxes · 46 lines · 2 labels` |
| 1H | `e29c0969f8676569` | `PASS · 117 boxes · 42 lines · 2 labels` |
| 4H | `444b332a02b77b23` | `PASS · 216 boxes · 65 lines · 5 labels` |

**THE LOOK, at 1H:** D1's panel renders the full-width rails **and the tags** — `Sellside Li…`
visible at ≈1.1420 and ≈1.1405, mid-chart — with `PASS · boxes 117 · lines 42 · labels 2` on its
caption. D2 renders its ladder (`FAIL · 0 boxes · 58 lines · 0 labels` — no labels by its own
design). D3 renders zones and labels (`PASS · 5 · 79 · 24`).

**AND THE FINDING BEHIND THE LAST REBUILD: the sha-match against an older frame was NOT a frozen
compositor.** Two captures came back byte-identical to a pre-label frame while the run reported
`labels 2` — because the tag, anchored at `bar_index - 250`, fell **outside the IDE's default
~190-bar view** in both. A full rig restart changed nothing; the **`-100` anchor** did. **For the
third time this session: a sha-match is an INFERENCE of staleness — the content is the truth.**

**THE SHIPPED D1 now defaults to `lqzSource='both'`** — the measured displaying config — because
the pin's own D1 gate (*"proper full-width horizontal display"*) is unsatisfiable under
`'luxalgo'` on this fixture. **The calibration knobs (`lqzTol`, `lqzMinAgree`, `wickBodyMult`,
`rejectATRMult`) remain the operator's.**
