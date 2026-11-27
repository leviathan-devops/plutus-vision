# PLUTUS VISION - HANDOVER PACKAGE "85% functional - DXY + GU (V3)", full

**Date:** 2026-11-27.
**Repository:** `leviathan-devops/plutus-vision`, working branch `AGENT`.
**This package:**
- tracked folder `handover/85pct_v3_full/`;
- downloadable archives `PLUTUS_VISION_85pct_V3__<n>_<PART>`;
- its own self-contained branch **`handover-85pct-v3-full`** (operator M-63 / ruling L-59).

The previous package ("70% functional") is on branch **`handover-70pct-functional`**.

The handover commit ids are in `CHECKPOINT_COMMIT.txt` next to this file. `MANIFEST_REPO.sha256` (SHA-256 of every tracked file at the handover) and `ARCHIVES_SHA256SUMS.txt` (the archives) are added by the commits right after it.

**This package covers everything since the 70% package:**
- every operator message M-58 .. M-63 and the rulings L-46 .. L-59;
- every build step D-129 .. D-145 with its canon line and measurements, including every rejected trial;
- five checkpoints: 80%, 85% V1 / V2 / V3, and this one;
- every frame, every commit, the full OmniGraph, every locator output and the raw session records.

**Nothing is summarised away:**
- `memory/` holds the originals: standing order, rulings, operator verbatim, decisions, lessons, facts, ledger, journal, state, coverage;
- the documents here point into it line by line.

**The operator's own grades in this window:**
- **M-60:** "80% functional, DXY specific";
- **M-61:** DXY and GBPUSD "A-" except the Thursday trade, EURUSD "a solid C";
- **V2 and V3 fixed exactly those:**
  - the Thursday trade on DXY / GBPUSD;
  - EURUSD's two stop-outs;
- **M-62:** "Okay, great."

---

## 1. What is in the package

### 1.1 Documents in this folder (tracked; also on both branches where they belong)

| File | Content |
|---|---|
| `00_START_HERE.md` | This file |
| `ENGINEERING_REPORT.md` | **The full engineering report: every single thing done since the 70% package, in order, with code, canon citation, measurements, rejected trials, incidents, reproduction and open work** |
| `COMMITS_SINCE_70PCT.md` | Every commit since `33f747fc` with its full message and the files it changed |
| `CHECKPOINTS.md` | The checkpoints (80%, V1, V2, V3, this one): commit ids, code ids, frames, his verdicts, the golden-week table against his trades |
| `VISUAL_CHECKPOINTS.md` | Every frame rendered and opened in this window, embedded, with its ledger row |
| `DURABLE_FACTS_SINCE_70PCT.md` | Rulings L-46 .. L-59, session facts, lessons and his golden trades, copied verbatim from `memory/`; plus the environment facts |
| `CODE_MAP_SINCE_70PCT.md` | Every function and flag added or changed, with decision id and canon line |
| `CODE_CHANGES_SINCE_70PCT.patch` | Every code line changed since the 70% package |
| `locator_outputs/` | Every locator re-run at the handover: golden diffs, order locator V2 / V3, fills, legs, Engine 2 day maps, near-misses, sanity, crash sweeps, leak check. **Locators, never verdicts.** |
| `scratchpad_scripts/` | The scratch scripts used: `tplist.py`, `lineerr.py`, `sweep.py`, `sweep_daily.py` |
| `answers_m58_q3/` | The M-58 item 3 question and its three pictures (from the scratchpad) |
| `canon_text_extracts/Trading_Laws_pdftotext.txt` | Text of his Trading Laws PDF (`pdftotext -layout`), read first-hand for D-143 |
| `omnigraph/` | The OmniGraph rebuilt from `memory/*.md` at the handover: `graph_store/` (the store directory as on disk), `graph_export.jsonl` (full export), `mem_status.txt`, `mem_ls.txt` |
| `MANIFEST_REPO.sha256`, `CHECKPOINT_COMMIT.txt`, `ARCHIVES_SHA256SUMS.txt` | Manifest, commit ids, archive checksums |

Earlier checkpoint folders of this window (each self-contained, built by `tools/checkpoint`):

| Folder | Checkpoint |
|---|---|
| `handover/80pct_dxy/` | 80% |
| `handover/85pct_dxy_gu/` | V1 |
| `handover/85pct_dxy_gu_v2/` | V2 |
| `handover/85pct_dxy_gu_v3/` | V3 |

### 1.2 Downloadable archives

Built in `handover_package/` (git-ignored) and sent with the chat's file upload. Checksums in `ARCHIVES_SHA256SUMS.txt`.

| Part | File | Content |
|---|---|---|
| 1 | `PLUTUS_VISION_85pct_V3__1_CORE.zip` | The whole repository tree at the handover commit (`git archive`), except `sidecar/raw` + `sidecar/cache` (part 2). Plus the git-ignored content files `memory/anchor_guard.log` and `tools/research/levels.{DXY,EURUSD,GBPUSD}.json`. |
| 2 | `..._2_SIDECAR_DATA.zip` | `sidecar/raw` + `sidecar/cache` (tracked): every as-of web page / model read, incl. the new `sidecar/raw/protocols/` (Treasury / NY Fed / EIA) |
| 3 | `..._3_GIT_HISTORY.bundle` (in parts `.part00`, `.part01`, ... under 500 MiB) | `git bundle --all`: every branch with full history. Rejoin with `cat ...part* > ..._3_GIT_HISTORY.bundle`, check `git bundle verify`, then `git clone`. |
| 4 | `..._4_TRANSCRIPTS.zip` | Raw session records, UNREDACTED (private delivery only): `~/.claude/projects/-home-user-plutus-vision/` = this session's transcript (every prompt, tool call and result, incl. the window before the context compaction), the earlier sessions' transcripts, the session folder (sub-agent transcripts, tool results, workflows); plus the session's `images/` and `tasks/`. Snapshot taken while the session ran: the final messages are not in it. |
| 5 | `..._5_INPUTS.zip` | `/home/user/inputs` as unpacked: the uploaded handover package (binding spec with R-01..R-39, host bibles incl. the Golden Standard), canon, toolset, his winning trade library (incl. the four training PDFs), Pinebox `ship-approved-v2` (test bench + bar store source), the aether backend. Read-only copy; no SHIP_PACKAGES / plutus-browser tree (R-39). |
| 6 | `..._6_SCRATCHPAD.zip` | The session scratchpad without its bulk copies of the repository (`sb/`, `pin/`, `pin2/`, `snap_*`, `hp/`, scratch worktrees): every probe, baseline, locator output and trial frame |
| 7 | `..._7_TESTBENCH_STATE.zip` | `~/.local/share/pinebox` without `runtime/` (rebuilt by `tools/pinebox-bootstrap.sh`): the TradingView bar store the tool reads, the Pinebox CLI, stages, store, judge, test, fork |
| 8 | `..._8_OMNIGRAPH.zip` | This folder's `omnigraph/` on its own |

**Not packaged, and why:**
- the OmniGraph / uv binaries in `~/.local/bin` (reinstalled with the one-liner in `tools/mem/README.md`);
- Pinebox `runtime/` (rebuilt by the bootstrap);
- the scratchpad's full repository copies (identical to part 1 + the history).

### 1.3 The two self-contained GitHub branches (M-63 / L-59)

| Branch | Built from | Adds |
|---|---|---|
| `handover-70pct-functional` | `ea7da38` (the last commit of the 70% handover: checkpoint `33f747fc` + manifest + archive checksums) | `handover/70pct_functional/archives/`: the 70% package's parts that were not in git (4 transcripts, 5 inputs, 6 scratchpad, 7 test-bench state, 8 OmniGraph), split under GitHub's 100 MB file limit, with `SHA256SUMS` and `REASSEMBLE.md` |
| `handover-85pct-v3-full` | The final `AGENT` commit of this handover | `handover/85pct_v3_full/archives/`: parts 4-8 of this package, split the same way |

Parts 1-3 need no copy on a branch:
- the branch's tree IS part 1 + part 2;
- its history IS part 3 for that line.

**The repository is PUBLIC.** On both branches the transcripts (part 4) are a REDACTED copy:
- the operator's e-mail address and account identifiers from the session context are replaced by placeholders;
- the unredacted transcripts exist only in the privately delivered archive part 4.

Every archive pushed to a branch was scanned for credentials (API keys, tokens, private keys) before the push; see `archives/REDACTION_AND_SCAN.md` on each branch.

---

## 2. The objective and where it stands

The standing order is `memory/14_GOAL_PROMPT.md` (goal prompt v2.1): translate the operator's canon into ONE Python program that, for a week and a pair, outputs ONE Pine v6 script with:
- E1 zones;
- the E2 shape chain;
- E3 trade setups.

It is computed only from data before the Monday London-open anchor (Monday 02:00 New York), extended by his approval to daily anchoring (each day from its own anchor, L-47 / L-53), and proven on Pinebox pixels.

| | Condition | State at this handover |
|---|---|---|
| S1 | Every coverage row built and audited | OPEN (`memory/15`; this window built E3-P6 Law 27 as a filter and E3-P10 per-day cascade) |
| S2 | Anchor week Jul 6-10 2026 against his own hand | HELD and improved. DXY: his #2-#8 matched (0.0-2.7 pips). EURUSD: his #2-#8 matched (#1 traded before the anchor). GBPUSD: his #1 #2 #3 #5 matched (#4 reinforcement, #6, #7 open). His grades M-61 then V2 / V3 fixes. `CHECKPOINTS.md` |
| S3 | Same commit, >= 4 weeks x 3 pairs, outside counts 80-90% | NOT MET. No outside count in this window (last = count 11 in the 70% package). His winning trade library is the oracle set now (L-48 / L-55). |
| S4 | Outside audit: zero open deviations | OPEN (`audit/G2_response2.md`) |
| S5 | Blind test | NOT RUN. Blind weeks must come from outside the library and outside every week already run (D-129). |
| S6 | One command -> one Pine | HELD at this handover (D-145 fixed a crash that broke 3 of 75 cached maps from V1 to V3) |

---

## 3. How the tool is built

```
e1_tool/plutus.py      one command: E1 -> E2 -> E3 -> Pine + reports; DAILY ANCHORING (daily_anchor) is the default, --weekly = Monday-only build
e1_tool/e1_data.py     bars from the Pinebox bar store; boundary_ms (Monday 02:00 NY, or ASOF during a daily update), day_anchor_ms, closed_until
e1_tool/e1_pillars.py  canon Pillars 1-7, Step 0 swings, Step 0.45 sweep zones, Step 0.5 magnets
e1_tool/e1_sd.py       supply / demand candle zones per timeframe (BoM / MoM, mitigation, Refined zones)
e1_tool/e1_v1.py       harvest of the SEALED V1's order blocks + liquidity bands through the Pinebox engine (tools/pine-probe.py), cached per instant in e1_tool/cache/v1s/
e1_tool/e1_ip.py       pressure (IP) zones: levels -> score -> assembly -> mechanics -> Pillar 9 -> Step 9.5 / 5.5 / 9.8 -> discovery flags
e1_tool/e1_pine.py     Pine generator for Engine 1 (trident_v8 form), joined zones (L-39), labels
e1_tool/e2_chain.py    Engine 2: current shape, bounds, branches, direction, timing (6.8, 6.10 in hours D-139, FA 9, NY cut cage), chain, alternatives, consolidation phase, days,
                       PATH = session path for swing scalps (_session_path, L-51) and session ladders for breakouts (_ladder_path, D-140); volatility triggers incl. Protocols D / E / G
e1_tool/e3_trades.py   Engine 3 (corrected E3 spec only, R-16): candidates per (day, zone), entries, ladder-step stops (L-50 reversal stops D-135), Law-14 TP walk, RRR floor + blend,
                       confidence, Phase 6 dedup / conflicts / caps, reinforcements, alternative-chain orders, Law-27 starts (D-141), Pine
indicator/plutus-vision-v1.sealed.pine   the sealed V1 baseline - READ ONLY, never edited
sidecar/               as-of web harvest per week -> sidecar/out/<MONDAY>.json; sidecar/protocols.py -> sidecar/out/protocols/<MONDAY>.json (Protocols D / E / G)
tools/                 pinebox-bootstrap.sh, pb / pbfit / pbzoom, e1render, s3frames, weekframe (whole week per pair), checkpoint (self-contained checkpoint folder), g1facts, s6shot,
                       anchor_guard.py + leak_check.py + git pre-commit hook, mem/ (OmniGraph wrapper)
tools/research/        locators (never imported by the tool)
```

**Decisions:** `memory/03_DECISION_CHAIN.md`, D-01 .. D-145. Every code comment that implements a canon line quotes it with file:line.

**Flags at the handover:**

| Module | Flag | Value |
|---|---|---|
| `plutus` | `DAY_CONFIRM` | `'start'` |
| `plutus` | `REANCHOR` | `False` |
| `plutus` | `REANCHOR_DRAW` | `True` |
| `plutus` | `PHASE10_REENTRY` | `True` |
| `plutus` | `FLOW27` | `True` |
| `e2_chain` | `SESSION_PATH` | `True` |
| `e2_chain` | `SPEED_4H_HOURS` | `True` |
| `e3_trades` | `REVERSAL_B` | `True` |
| `e3_trades` | `EU_INSIDE` | `False` |
| `e3_trades` | `SL_CLEAR_LQZ` | `False` |

---

## 4. How to run it

```
# test bench (Pinebox is the only test environment)
tools/pinebox-bootstrap.sh                       # needs /home/user/inputs/pinebox (archive part 5)
export PATH=$HOME/.local/bin:$PATH XDG_RUNTIME_DIR=/run/user/0
pinebox list --session plutus-main               # "alive": false after a worker restart ->
pinebox down --session plutus-main; pinebox up --session plutus-main --adapter xvfb --pair DXY --tf 1H

# one command per week / pair -> one Pine (daily anchoring is the default; --weekly = Monday-only)
cd e1_tool && python3 plutus.py 2026-07-06 EURUSD out/E1_EURUSD_2026-07-06.pine

# frames: write the expectation in memory/07 FIRST, render ONE map at a time, open every frame you cite
tools/weekframe evidence/<dir> DXY:2026-07-06 EURUSD:2026-07-06 GBPUSD:2026-07-06

# proofs and locators
python3 tools/leak_check.py DXY:2026-07-06 EURUSD:2026-07-06 GBPUSD:2026-07-06; echo "exit $?"   # temporal anchor: week anchor + every day's two instants
python3 handover/85pct_v3_full/scratchpad_scripts/tplist.py daily                                 # order locator, 12 maps
tools/checkpoint <dir> "<title>" "<verdict>"                                                       # a self-contained checkpoint folder

# as-of web inputs for a new week
sidecar/run --week YYYY-MM-DD          # OpenCode key injected by the network proxy for opencode.ai: send `Authorization: Bearer proxy-injected`; never print or ask for the key
python3 sidecar/protocols.py           # Protocols D / E / G for every sidecar week (as of each anchor)
```

**Rules that bind whoever continues** (all in `CLAUDE.md`, `memory/14_GOAL_PROMPT.md`, `memory/04_OPERATOR_RULINGS_LIVE.md`):
- no hardcoded prices or per-week constants in Python;
- nothing after the anchor feeds a map (each day: nothing after its own anchor), enforced by `tools/leak_check.py` and the pre-commit hook;
- never edit the sealed V1;
- never touch SHIP_PACKAGES or any plutus-browser tree (R-39);
- develop on `AGENT`; handover branches only by the operator's order (L-59);
- do not disable the ECC GateGuard hook: state the facts it asks for and retry;
- sub-agents only as outside reviewers;
- no verdict from one's own scripts;
- canon vocabulary only;
- <= 11 setups per week per pair;
- one unique trade per observable move (L-52);
- every report shows all three pairs, the whole week in one fitted frame each (L-56).

**Read order for a new agent** (`memory/00_COMPACTION_SURVIVAL.md`):
1. `memory/14` in full;
2. `10`, `11`, `12` (tail: M-58 .. M-63), `01`, `04` (L-46 .. L-59), `02`, `03` (D-129 .. D-145), `06`, `08` (to the end), `09`, `05` (tail), `07` (tail: 107 .. 115b), `13`, `15`;
3. then this folder's `ENGINEERING_REPORT.md`.

---

## 5. What was done in this window (detail: `ENGINEERING_REPORT.md`)

| Step | Decisions | One line |
|---|---|---|
| Answers to M-58 | D-129 | Stop scenarios with charts, TVC correction, E2 drawing question, library inventory (about 17 pair-weeks, now the oracle set), counting explained |
| Event data | - | Protocols D (Treasury auctions), E (NY Fed ON RRP), G (EIA crude) as of each anchor, shown as E2 volatility triggers; F (Forex Factory) NO DATA |
| Daily anchoring | D-131 .. D-138 | Trading-day-open confirmation (one-time order blocks, price side), alternative activation (6.6 Step 4), no duplicate trades (L-52), daily zone update at the London open (L-53), chain re-anchor for the drawing only; leak check per day |
| Stops | D-130, D-135 | Reversal entries 1 pip inside the next shielding zone, no 9.5 envelope veto, deeper-only fallback; EUR/USD keeps "outside the entry zone" (his golden EUR/USD stops) |
| E2 line | L-51, D-139, D-140 | Swing scalps session by session (P452 6.6 rules); breakouts as session ladders; 6.10 "2-3 more 4H candles" = +12 h |
| 80% checkpoint | M-60 | `tools/weekframe`, `tools/checkpoint`; whole-week frames of all three pairs |
| V1 | M-61 | His grades: DXY / GBPUSD A- except Thursday, EURUSD C |
| V2 | D-141 | Thursday: dormant alternative orders are contingencies; the Law-27 short at the whiplash TP from the whiplash start; passed rockets void |
| V3 | D-142b, D-144 (D-143 rejected) | EURUSD: Phase 10 re-entry check on the source's same-day record; Law-27 trade flow on the day's line; both EURUSD stop-outs gone |
| Handover | D-145 | A KeyError on 3 of 75 cached maps (V1-V3) found by re-running the locators, fixed |

---

## 6. Where his named defects stand

### M-57 (70%)

**(1) "slightly too tight on the SL or slightly too early".**
- Stops: D-135 (wider reversal stops, never skipped for a few pips; L-50).
- "Too early": daily anchoring (orders confirmed per day, re-armed only as new trades) and the Law-27 flow (D-144: no entry against a move still running).
- Open: GBP/USD liquidity-outside mechanics. GB1's stop is 8.0 pips off his.

**(2) "a generalized watered down basic line".**
- Session-by-session swing scalps and session ladders (L-51, D-140).
- The line restarts from each day's real price.
- After a failure the line follows a chain re-anchored on the day's rebuilt map (D-138).
- Open: the Engine 2 forecast itself on the library weeks (the breakout day).

### M-60

| Defect | State |
|---|---|
| DXY E2 Wed-Fri | Fixed (D-139 / D-140; ledger 113) |
| GBPUSD | Moved to "A-" (M-61) |
| EURUSD missing | Every report now shows all three pairs |

### M-61

| Defect | State |
|---|---|
| Thursday trade | Fixed (V2) |
| EURUSD C | Fixed (V3; `evidence/answers_m61/EURUSD_why_C.md`) |

---

## 7. Open work, in the order of the standing loop

1. **GBPUSD:**
   - his #6 (Thu long 1.33829) and #7 (Fri short 1.34481);
   - the L-50 liquidity-outside stop mechanics.
2. **Engine 2 on the library weeks:**
   - GBPUSD Apr 13: the breakout came Monday, my chain says Wednesday;
   - GBPUSD Mar 2: one day late, no reversal after the breakdown.
3. **Presentation:**
   - EURUSD Wednesday labels overlap;
   - "new <Day>" labels over candles;
   - the EURUSD Friday RWL line ends high.
4. **The library as oracle files:** `context_management/oracle/library/*.json`.
5. **Coverage rows NOT BUILT** (`memory/15`):
   - spiderweb entry construction;
   - the WorkingDayMap / 12-step day assignment as objects;
   - the per-DXY-setup mirror lane;
   - the master trade setup;
   - ZoC;
   - FA rows.
6. **S3 outside counts** on the library weeks, then the **S4** audit and the **S5** blind test.

**Inputs still NO DATA:** Protocol F (red-folder calendar; L-54).

---

## 8. Locators at the handover (never verdicts, never sent as results)

| Output (`locator_outputs/`) | What it lists |
|---|---|
| `od_v3_daily_*.txt`, `od_v3_weekly_*.txt` | My orders against his golden trades (entry / SL / TP distances), daily (product) and weekly mode |
| `orders_12maps_daily_V2_tp_d141.txt`, `orders_12maps_daily_V3_tp_d144c.txt` | Daily-mode fill / TP / SL per order, 12 maps, V2 vs V3 |
| `fills_16maps_weekly_HEADV3.txt` + tally | Weekly-mode setups and what the 15m candles did |
| `legs_12maps_weekly_HEADV3.txt` + tally | 1H legs of 30+ pips and the setup that caught each |
| `e2loc_16maps_weekly_HEADV3.txt`, `e2loc_all_DXY_weeks_weekly_HEAD_D145.txt` | Forecast day tags against each day's candles |
| `nearmiss_12maps_weekly_HEADV3.txt` | Stops overshot before the TP, entries missed by a few pips |
| `sanity_all_DXY_weeks_weekly_*.txt` | Structural checks on every setup |
| `sweep_*` | Crash sweeps over every cached pair-week (D-145) |
| `leak_check_4maps_V3.txt` | Temporal-anchor proof |
