# PLUTUS VISION — HANDOVER PACKAGE "70% functional"

Checkpoint of 2026-11-27. Branch `AGENT` of `leviathan-devops/plutus-vision`. The checkpoint commit is named in `CHECKPOINT_COMMIT.txt` next to this file; that file and `MANIFEST_REPO.sha256` (SHA-256 of every tracked file at the checkpoint) are added by the commit right after it, and `ARCHIVES_SHA256SUMS.txt` (checksums of the downloadable archives) by the last commit of the handover.
Operator's verdict on this checkpoint (M-57, verbatim in `memory/12_OPERATOR_VERBATIM.md`): **"This is 70% functional very good work"**, with two named defects:

1. "half of your trades are accurate but slightly too tight on the SL or slightly too early and cause misses/losses"
2. "the E2 shape chain line is highly accurate in some and medium in others and also does not always fully reflect the ACTUAL price action but is instead a generalized watered down basic line"

Both are true of this build. Section 6 says exactly where each one lives in the code and what was measured. Nothing in this package is summarised away: the memory files, the journal with every rejected trial, every outside count and the graph are the originals.

---

## 1. What is in the package

Seven downloadable archives, built in `handover_package/` of the working directory (git-ignored) and sent to the operator; checksums in `ARCHIVES_SHA256SUMS.txt`.
**Durability:** the archives exist only in the build container until downloaded - the container is reclaimed after inactivity. Everything tracked (parts 1-3) is also on GitHub, branch `AGENT`. Parts 4-7 are NOT on GitHub.

| Part | File | Content |
|---|---|---|
| 1 | `PLUTUS_VISION_70pct_functional__1_CORE.zip` | The whole repository tree at the checkpoint (`git archive`) EXCEPT `sidecar/raw` and `sidecar/cache` (part 2): the tool (`e1_tool/`), the sealed V1 (`indicator/`), all memory (`memory/`), all audits, briefs, facts files and outside counts (`audit/`), all evidence frames (`evidence/`), canon copy (`canon/`), spec digests and oracle (`context_management/`), `tools/`, sidecar source + week files (`sidecar/src`, `sidecar/out`), the blind-test run sheet, `CLAUDE.md`, and this folder `handover/70pct_functional/` (this document, the OmniGraph store + export, locator outputs, scratchpad research scripts, the file manifest). Plus the four git-ignored files of the working tree that carry content: `memory/anchor_guard.log` (the temporal-anchor guard's log) and `tools/research/levels.{DXY,EURUSD,GBPUSD}.json` (research dumps). Only `.ruff_cache/` and `__pycache__` noise is left out. |
| 2 | `PLUTUS_VISION_70pct_functional__2_SIDECAR_DATA.zip` | `sidecar/raw` + `sidecar/cache` (tracked, 1,880 files): every web page, image, sitemap and model read the as-of harvest used, per week - the evidence that nothing published after the Monday anchor fed a map. |
| 3 | `PLUTUS_VISION_70pct_functional__3_GIT_HISTORY.bundle` | `git bundle --all` of the repository: every branch (incl. `AGENT` up to the checkpoint, `handover` = original canon + weekly report oracles, `main`, the older agent branches) with full history. `git clone PLUTUS_VISION_70pct_functional__3_GIT_HISTORY.bundle plutus-vision && cd plutus-vision && git checkout AGENT` restores it untampered; `git bundle verify` checks it. Every commit message carries the canon line it rests on. Delivered in two pieces (`...bundle.part00`, `...bundle.part01`) because of the 500 MiB upload limit: `cat ...part00 ...part01 > PLUTUS_VISION_70pct_functional__3_GIT_HISTORY.bundle`, then compare its SHA-256 with `ARCHIVES_SHA256SUMS.txt`. |
| 4 | `PLUTUS_VISION_70pct_functional__4_TRANSCRIPTS.zip` | The raw session records: `-home-user-plutus-vision/*.jsonl` (this session's transcript - every prompt, tool call and tool result - and the earlier sessions of the project), the session folder (52 sub-agent transcript files, among them the outside G1 reviewers and the G2 auditors; tool results; workflows), and the session's `images/`, `tasks/` folders. Snapshot taken while the session ran: the final messages (sending this package) are not in it. Not pushed to GitHub: the transcripts carry account details from the session context. |
| 5 | `PLUTUS_VISION_70pct_functional__5_INPUTS.zip` | `/home/user/inputs` exactly as unpacked in the build container: the uploaded handover package (binding spec bundle with R-01..R-39, host bibles incl. the Golden Standard reference), canon, toolset, the winning-trade library, the Fibonacci Spiderwebs PDF, Pinebox `ship-approved-v2` (source of the test bench and of the TradingView bar store), the aether backend. Read-only copy. No SHIP_PACKAGES or plutus-browser tree exists there (R-39 checked). |
| 6 | `PLUTUS_VISION_70pct_functional__6_SCRATCHPAD.zip` | The session scratchpad without its bulk copies of the repository (`sb/`, `pin/`, `pin2/`, `snap_*`, `hp/`): every probe, baseline (`od_d99_*` golden baselines, `fills_*`, `legs_*`, `e2loc_*`), facts dumps and frames of trials. Not needed to continue; included so nothing is withheld. |
| 7 | `PLUTUS_VISION_70pct_functional__7_TESTBENCH_STATE.zip` | `~/.local/share/pinebox` of the build container without `runtime/` (rebuilt by `tools/pinebox-bootstrap.sh`): the TradingView bar store the tool reads (`data/tv-bars/` - DXY / EURUSD / GBPUSD x 15m / 30m / 1H / 4H, Feb 2025 - Nov 2026; byte-identical to the copy inside part 5's Pinebox package), the Pinebox CLI, stages, store, judge, test, fork. With part 5 a new container can run the tool without re-running the bootstrap's bar copy. |

Not packaged, and why: the OmniGraph / uv binaries in `~/.local/bin` (261 MB; reinstalled with the documented one-liner in `tools/mem/README.md`), Pinebox `runtime/` (694 MB; rebuilt by `tools/pinebox-bootstrap.sh`), the scratchpad's full copies of the repository (identical to part 1 + git history).

Inside this folder (`handover/70pct_functional/`, tracked in git and in part 1):

- `00_START_HERE.md` - this file.
- `CHECKPOINT_COMMIT.txt` - checkpoint commit id, date, `git status`, last commits.
- `MANIFEST_REPO.sha256` - SHA-256 of every tracked file at the checkpoint.
- `ARCHIVES_SHA256SUMS.txt` - SHA-256 and size of the seven archives.
- `omnigraph/graph_store/` - the OmniGraph store directory exactly as on disk (`/home/user/.plutus-mem`: `graph.omni/` incl. `__history`, `last_sync.jsonl`, `state.json`; only the empty `.lock` file left out), rebuilt from `memory/*.md` at the checkpoint with `tools/mem/mem rebuild` (1,471 nodes, 895 edges).
- `omnigraph/graph_export.jsonl` - `omnigraph export` of the full graph (every node and edge, JSONL). `omnigraph/mem_status.txt`, `omnigraph/mem_ls.txt` - counts and the id list.
  The graph is a pure function of `memory/*.md` + `memory/graph_log.jsonl` + `tools/mem/schema.pg`; the markdown is the source of truth (`tools/mem/README.md`). Query: `tools/mem/mem q <text>`, `mem get <id>`.
- `locator_outputs/` - the outputs of every bug locator at the checkpoint (section 8). They are locators, never verdicts.
- `scratchpad_scripts/` - the sandbox runner and the diagnostics named in the journal (`sbrun.sh`, `qall.sh`, `e2diag*.py`, `e2dir.py`, `e2struct.py`, `e2own.py`, `turnobj.py`, `turncov.py`).

---

## 2. The objective and where it stands

Standing order: `memory/14_GOAL_PROMPT.md` (goal prompt v2.1) — translate the operator's canon into ONE Python program that, for a week and a pair, outputs ONE Pine v6 script with E1 zones, the E2 shape chain and E3 trade setups, computed only from data before the Monday London-open anchor (Monday 02:00 New York), proven on Pinebox pixels. Success conditions S1-S6:

| | Condition | State at this checkpoint |
|---|---|---|
| S1 | every coverage row built and audited | OPEN. `memory/15_CANON_COVERAGE.md`: 18 rows still NOT BUILT, many PARTIAL (section 7). |
| S2 | anchor week Jul 6-10 2026 (his own trades / tags) | HELD. DXY: his trades within 3 pips; EURUSD likewise; frames in `evidence/`, ledger rows 57-58, 90, 97b. Checked after every change with `tools/research/oracle_diff.py`. |
| S3 | same commit on >= 4 weeks x 3 pairs, each engine 80-90% by outside count, no week under 70 | NOT MET. Eleventh outside count: E1 98.5 / E2 81.7 / E3 50.7; outside the anchor week 98.0 / 82.2 / 34.8. E1 side condition passes on 8 of 12 maps. |
| S4 | outside audit of the final code: zero open deviations | OPEN. `audit/G2_audit2.md` + `audit/G2_response2.md` (rows OPEN / PART listed there). |
| S5 | blind test on weeks never rendered or inspected | NOT RUN. Reserved, untouched weeks: 2026-02-02, 02-09, 02-16, 02-23, 03-02, 03-16, 03-23 (never run the tool or a locator on them before the test). Run sheet: `blind_test/RUN.md`. |
| S6 | one command -> one Pine on top of the sealed V1 | HELD. `python3 e1_tool/plutus.py MONDAY PAIR` -> `e1_tool/out/PLUTUS_<PAIR>_<MONDAY>.pine`; ledger 84, 90, 97b. |

### Every outside count (reviewers with no access to the code or earlier counts; files `audit/G1_count_dryrun*.md`)

| Count | Code | All 12 maps E1 / E2 / E3 | Outside the anchor week E1 / E2 / E3 |
|---|---|---|---|
| 1 | early | 82 / 35 / 33 | 81 / 29 / 17 |
| 2 | before D-60 | 46 / 43 / 29 | 42 / 33 / 12 |
| 3 | 5670e41+ | 91.7 / 68.3 / 29.5 | 91.2 / 64.4 / 14.0 |
| 4 | 591f70c | 77 / 78 / 34 | 73 / 71 / 14 |
| 5 | 3b5b52c | 94.6 / 76.7 / 39.7 | 94.2 / 68.9 / 19.1 |
| 6 | 6bd3e3e | 85.1 / 83.3 / 33.7 | see file |
| 7 | e329ece | 94 / 80 / 36 | 92 / 78 / 19 |
| 8 | d05031f | 95.7 / 76.7 / 47.1 | 94.4 / 75.6 / 29.8 |
| 9 | d4afa85 | 89.3 / 78.3 / 46.4 | 86.7 / 77.8 / 29.2 |
| 10 | 5e016e5 | 89.5 / 81.7 / 36.8 | 88.5 / 82.2 / 23.0 |
| 11 | 366ce81 | 98.5 / 81.7 / 50.7 | 98.0 / 82.2 / 34.8 |

The reviewers differ in how many "obvious trades" they list per map (count 10: 95, count 11: 67), so the E3 column moves with the reviewer as well as with the code. Reviewer 11's own caveat on E1: zones plus their parts cover almost the whole week's range on every map, so nearly every turn lands in some zone.

Maps of the counts: DXY / EURUSD / GBPUSD x weeks 2026-07-06 (anchor), 2026-04-20, 2026-10-05, 2026-05-18. Frames of count 11: `evidence/s3k/`; facts: `audit/g1_facts_k/`; brief: `audit/G1_brief11.md`.

---

## 3. How the tool is built (files)

```
e1_tool/plutus.py      one command: E1 -> E2 -> E3 -> Pine + reports (run(pair, monday))
e1_tool/e1_data.py     bars from the Pinebox bar store, anchor / week boundaries (boundary_ms = Monday 02:00 New York)
e1_tool/e1_pillars.py  canon Pillars 1-7, Step 0 swings, Step 0.45 sweep zones, Step 0.5 magnets
e1_tool/e1_sd.py       supply / demand candle zones per timeframe (BoM / MoM, mitigation, Refined zones)
e1_tool/e1_v1.py       harvest of the SEALED V1's order blocks + liquidity bands through the Pinebox engine (tools/pine-probe.py), 400 closed bars per timeframe
e1_tool/e1_ip.py       pressure (IP) zones: levels -> score -> assembly -> zone mechanics -> Pillar 9 (types, ZFP, modifiers) -> Step 9.5 gap scan -> Step 5.5 core/spike -> Step 9.8 re-verification -> discovery flags
e1_tool/e1_pine.py     Pine generator for Engine 1 (trident_v8 form), joined zones (L-39), chart reach, labels
e1_tool/e2_chain.py    Engine 2: current shape (6.2), bounds (6.5), branch per bound (6.4 / 6.4.1 / 6.4.2), direction (pressure reading, 4H structure, 6-check), timing (6.8, 6.10, FA 9, NY cut cage), chain extension, alternative chains, consolidation phase, day decomposition, path, Pine
e1_tool/e3_trades.py   Engine 3 (corrected E3 spec only, R-16): candidates per (day, zone), entries (TS-1, F1-A/C/D), ladder-step stops (ZR-6B), Law-14 TP walk, RRR floor + blended gate, confidence, Phase 6 dedup / conflicts / caps, reinforcements, alternative-chain conditional orders, Pine
indicator/plutus-vision-v1.sealed.pine   the sealed V1 baseline - READ ONLY, never edited
sidecar/               as-of web harvest (option expiries, analyst levels, Fed H.10) per week -> sidecar/out/<MONDAY>.json
tools/                 pinebox-bootstrap.sh, pb / pbfit / pbzoom (drive Pinebox), e1render, s3frames (three frames per map), g1facts (facts files for outside counts), s6shot, anchor_guard.py + git pre-commit hook (leak check), mem/ (OmniGraph wrapper)
tools/research/        locators (section 8) - never imported by the tool
```

Decisions: `memory/03_DECISION_CHAIN.md` (D-01 .. D-128, one row each: what, canon citation, what it replaced). Every code comment that implements a canon line quotes it with file:line (P533 = v5.3.3 prompt, P452 = v4.5.2 prompt, E3C = corrected E3 spec, E2X = extract of Part VI, FA = Fractal Architecture, GS = Golden Standard).

---

## 4. How to run it

```
# test bench (Pinebox is the only test environment)
tools/pinebox-bootstrap.sh                       # needs /home/user/inputs/pinebox (part 5)
export PATH=$HOME/.local/bin:$PATH XDG_RUNTIME_DIR=/run/user/0
pinebox list --session plutus-main               # after a worker restart: pinebox up --session plutus-main --adapter xvfb --pair DXY --tf 1H   (plain `pinebox up` is refused: slot :0)

# one command per week / pair -> one Pine
python3 e1_tool/plutus.py 2026-07-06 DXY         # -> e1_tool/out/PLUTUS_DXY_2026-07-06.pine

# frames (expectation row in memory/07 BEFORE rendering; open every frame you cite)
tools/s3frames evidence/<dir> PAIR:MONDAY ...    # at most six maps per call (10-minute limit); _zones, _all, _week frames
tools/g1facts audit/<dir> PAIR:MONDAY ...        # facts files for an outside count

# as-of web inputs for a new week
sidecar/run --week YYYY-MM-DD                    # OpenCode key is injected by the network proxy for host opencode.ai: send `Authorization: Bearer proxy-injected`, never print or ask for the key
```

Rules that bind whoever continues (all in `CLAUDE.md`, `memory/14_GOAL_PROMPT.md`, `memory/04_OPERATOR_RULINGS_LIVE.md`):
no hardcoded prices or per-week constants in Python; nothing after the Monday anchor feeds a map (`tools/anchor_guard.py`, pre-commit hook); never edit the sealed V1; never touch SHIP_PACKAGES or any plutus-browser tree (R-39); develop on branch `AGENT` only; do not disable the ECC GateGuard hook (state the facts it asks for and retry); sub-agents only as outside reviewers; no verdict from one's own scripts; canon vocabulary only; <= 11 setups per week per pair.

Read order for a new agent (`memory/00_COMPACTION_SURVIVAL.md`): `memory/14` in full -> `10`, `11`, `12` (tail), `01`, `04`, `02`, `03`, `06`, `08` (to the end), `09`, `05` (tail), `07` (tail), `13`, `15` -> `audit/G2_audit2.md`, `audit/G2_response2.md` -> `audit/G1_count_dryrun11.md`.

---

## 5. What changed in the last working window (D-113 .. D-128)

Everything is in `memory/03` and `memory/05`; in short: 4H trend / storyline = swing structure (D-115, P533:2649); blended-RRR middle entry, Law-14 precondition, stop side for breakouts through a sweep zone, blend guard (D-116, D-118, D-119); same-order cap (D-120); breakout target not a MoM zone lying against the failing bound (D-121); spill-over day to day (D-122); consolidation phase per the canon table + Transition Entry only in the Late phase (D-125); Engine 2 Section 17 inside the Pine (D-126); E1 Step 9.8 / Step 5.5 / Part IV 4.2 (D-117); gap scan beyond the outermost zone (D-114); drawing rules and labels (D-113, D-127, D-128). The golden-week primaries were unchanged through all of them.

---

## 6. The operator's two defects — where they live

### 6.1 "slightly too tight on the SL or slightly too early"

Measured on the 12 count maps with `tools/research/nearmiss.py` (locator; output `locator_outputs/nearmiss_12maps.txt`; simpler fill rules than the facts script):
of the primary orders that were stopped, more than half went on to their take-profit after overshooting the stop, several by under 3 pips; and a number of unfilled orders had price turn within 0-6 pips of the entry and then reach the take-profit. Named cases:

- DXY 05-18 floor long E 99.050 / SL 98.971: price went 2.7 pips beyond the stop to 98.944 - exactly the top edge of the daily sweep zone 98.844-98.944 lying under the floor - then ran to the TP and 57 pips.
- EURUSD 07-06 Monday short SL 1.14451: 2.9 pips beyond, then TP. EURUSD 10-05 Tuesday short: 2.5 pips beyond, then TP.
- EURUSD 04-20 shorts E 1.17920: price turned 1.0-1.8 pips short of the entry. DXY 10-05 short 102.435: 0.2 pip short. GBPUSD 10-05 long 1.31899: 0.1 pip short. EURUSD 05-18 long 1.15815: 1.2 pips short. DXY 05-18 Thursday long: 1.4 pips short.

Where it comes from in the code:

- **Stop choice** - `e3_trades._stop`. Rule (a) "3 pips OUTSIDE the FAR edge of the CURRENT entry step" vs rule (b) "1-2 pips INSIDE the CLOSE edge of the NEXT STEP away" (E3C:247-256), switched by ZR-6B on the mirror confidence (>= 0.6 -> RR-tight, E3C:284-286; D-73). Nearly every range order scores >= 0.6, so nearly every stop is the tight one, 3 pips behind the entry zone. The 9.5-pip envelope (D-111) then prefers stops inside 9.5 pips. Unswept stops resting just beyond the entry zone (a sweep level within 5-10 pips) are not looked at unless the sweep zone is the anchor itself or lies inside the bound (D-84, D-87, D-88).
  What a wider stop costs: with the TP at the first unmitigated opposing zone (Law 14, D-97) and the RRR floor (2.5, R-07; E3C says 3.0), a stop 5 pips wider turns most of these orders into RRR rejects. That trade-off - stop beyond the sweep vs the RRR floor vs a deeper entry - is not settled by any line I found, and every variant I tried on it lost on the anchor week (journal: stops outside a sweep level at a candle zone's back edge; SWEEP_EXT off; tighter re-anchoring in the RRR loop; bounds up to ZFP 45).
- **Entry level** - `e3_trades._entries` + Mechanism A front (D-62): the order is met at first contact = zone edge + the pair's forward spread (DXY 0.02, EUR 1 pip, GBP 2 pips). Where the entry is a level inside the zone (F1-A lift, F1-C internal rung) or the zone edge of a wide zone, price can turn 1-2 pips before it.
- **Too early** - orders are resting limits from the start of their day (D-78); there is no confirmation at the zone (E3C 8.25 retest count, GS candle confirmation, "entry AFTER the spike") because every level and bracket is fixed at the Monday anchor. His own construction (Fibonacci Spiderwebs PDF, items 3-5) anchors each day's trade on the London-open position of THAT day.

### 6.2 "a generalized watered down basic line"

`e2_chain.build`, Step 5 (path): for a consolidation the line is a zigzag between the two bounds with `SS_SWING = 2` sessions per swing, counted back from the transition; a breakout is one straight segment from the bound to the target over `BS_SESSIONS` (doubled for a 4H element); a whiplash is one spike. The line is therefore a schematic of the chain, not a path through the liquidity between the bounds: it does not stop at the intermediate rungs / zones, it has no day-level open positions, and it is drawn once at the anchor. Where the week follows the chain (DXY 04-20, the anchor week) it looks accurate; where the week ranges inside a wider box or breaks earlier / later it is the template.
On every DXY week from April to November the day-map locator (`e2loc.py`) agrees with about half of the days - clearly below the count maps; 14 of 31 weeks are forecast "SS all week" and the range held in 6. The canon's own breakout triggers are mostly inputs this build does not have (red-folder calendar, auctions) or modifiers not yet built (cascade, cross-pair; trials X / X2 in the journal).

---

## 7. Open work, in the order of the standing loop

1. Count 11's defect list (ledger 105c): range orders die after the first touch / no order at the bound that holds; GBPUSD range boxes; GBPUSD 04-20 (pair ranges while the translated DXY chain breaks out); entries a few pips beyond the turn; floating objects at the end of a wrong forecast path; labels in the day-tag band; void orders still drawn; repeat orders filling while the parent is open.
2. Engine 2 beyond the count maps (section 6.2).
3. Coverage rows NOT BUILT (`memory/15`): Fibonacci spiderweb as entry construction (E2-AIR / Law 5 - the largest), WorkingDayMap + 12-step day assignment as explicit objects (E3-P1 / P7), cascade mirror lane (E3-P10), master trade setup (E3-P11), ZoC logic (GS-WAR / E2-ZOC), DWL inverse, R scalps, WLS, trip-wire rockets per 8R alone (FA-ROCKET), GS-C4, GS-CND, FA-EARTH / FIRE / WATER / PAIR rows, Pillar 9 cascade + cross-pair modifiers, Part IV 4.3 / 4.4.
4. Audit list `audit/G2_response2.md`: every OPEN / PART row; then a fresh outside audit (S4).
5. S5 blind test once S3 holds.

Inputs recorded NO DATA (ruling L-32): red-folder calendar (forexfactory.com), Treasury auctions (treasurydirect.gov), ON RRP (newyorkfed.org) - all refused by the build environment's network policy; investinglive's weekly outlook is published after the summer anchor. DX options OI (CME) is blocked by the canon itself.

---

## 8. Locators (never verdicts, never sent as results)

| Script | What it lists | Output at the checkpoint |
|---|---|---|
| `tools/research/oracle_diff.py PAIR` | my setups against his golden trades (entry / SL / TP distances) | `locator_outputs/od_fin_*.txt` (baseline `od_d99_*`; compare primaries, ALT rows aside) |
| `tools/research/fills.py PAIR MONDAY`, `allfills.sh TAG` | every setup and what the 15m candles did to it | `fills_16maps_HEAD.txt` |
| `tools/research/legs.py`, `alllegs.sh TAG` | 1H zigzag legs of 30 pips / 3+ hours and the setup that caught each | `legs_12maps_HEAD.txt` |
| `tools/research/e2loc.py [maps]` | forecast day tags against each day's candles | `e2loc_16maps_HEAD.txt`, `e2loc_all_DXY_weeks_HEAD.txt` |
| `tools/research/qual.py PAIR MONDAY` | E1 side condition (bloated / bunched / floating / missing) | run per map (`scratchpad_scripts/qall.sh`) |
| `tools/research/sanity.py [maps]` | structural checks on every setup (no market outcome) | `sanity_all_DXY_weeks_HEAD.txt` |
| `tools/research/nearmiss.py [maps]` | stops overshot before the TP, entries missed by a few pips | `nearmiss_12maps.txt` |
| `tools/research/week_facts.py` | every drawn object with prices (facts files) | `audit/g1_facts_k/` |

Sandbox pattern used for every trial: copy `e1_tool` + `tools/research` to a scratch directory, patch there, run fills + legs + golden diff (`scratchpad_scripts/sbrun.sh`), adopt only with the golden primaries unchanged and a canon citation; every rejected trial is one journal entry in `memory/05_JOURNAL.md`.

---

## 9. What is needed from the operator to finish (also given in the chat)

1. **Stops**: his rule when unswept stops rest a few pips beyond the entry zone - stop beyond that sweep (and then which RRR floor applies: R-07 says 2.5 for HIGH, E3C says 3.0), or a deeper entry, or the tight stop as now. Two or three of his own range-week trades with their stops marked would settle it.
2. **Entry timing / the anchor rule**: may the Pine build or confirm Tuesday-Friday orders from each day's London-open position against the fixed Monday map (his Spiderwebs items 3-5), or must every order stay fixed at Monday's anchor? This decides whether "too early" can be fixed at all, and whether the E2 line may be redrawn per day.
3. **E2 line**: what the line must show on a range week - the swing-by-swing path through named rungs per session, or the day boxes with a schematic line as now.
4. **Oracles beyond the anchor week**: his hand-marked charts (zones, day tags, trades with SL / TP) for at least two more weeks - one range week and one week where GBPUSD diverged from DXY. One week in his hand is all the build has.
5. **Data**: network access to (or exports of) the red-folder calendar for the test weeks; optionally Treasury auctions and ON RRP.
6. **His DXY feed**: on the TVC:DXY 1H bars in the store his golden Monday long 100.945 / SL 100.905 cannot fill before the 17:00 UTC bar (Monday's low until then 100.956), and that bar runs on to 100.897 - through his stop. Which DXY symbol / feed he charts decides whether every DXY level here sits a few pips off his.
7. **Counting**: his definition of an "obvious trade" for the outside counts (reviewers list 67 to 95 on the same 12 maps), and whether per-day repeats of a range order count toward the 11.
