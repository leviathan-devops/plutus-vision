# Code map: every function and flag added or changed since the "70% functional" package (33f747fc)

Every line of the change is in `CODE_CHANGES_SINCE_70PCT.patch`:

```
git diff 33f747fc..<handover commit> -- 'e1_tool/*.py' 'tools/*' 'sidecar/*.py' 'sidecar/src/*' CLAUDE.md
```

Size of the change: 11 files, +1,037 / -40 lines up to V3, plus the D-145 line pair. Each entry gives the decision id (`memory/03`) and the canon line the code quotes in its own docstring / comment.

## e1_tool/plutus.py (one command: E1 -> E2 -> E3 -> Pine; +520 lines)

| Function / flag | New / changed | What it does | Decision / canon |
|---|---|---|---|
| `_setups(pair, monday)` | changed and back | The source pair's week-anchor setups for the Phase 10 cascade, memoised. A daily variant was tried and leaked; reverted in D-142b. | E3C:723-770 |
| `_src_days(pair, monday)` | new | The source pair's per-day record `{day index: {(shape, direction)}}` of the primary orders confirmed at each day's trading-day open (from `run(..., daily=True)[1]['daily'][i]['keys']`) | D-142b, E3C Phase 10, L-52 |
| `_map(pair, monday)` | new | The Engine 1 map at the week anchor; any ASOF override is popped while building | D-136 |
| `_asof(monday, t, fn)` | new | Runs `fn` with `e1_data.ASOF[monday] = t` (every bar read stops at t), restoring after | D-136, L-53 |
| `_map_at(pair, monday, t)` | new | Engine 1 rebuilt as of instant t (a day's London open) | D-136, L-53 |
| `_engines_at(pair, monday, t)` | new | Engine 2 + 3 re-anchored at t on the map of t; the Phase 10 source pairs at the same instant | D-136 / D-138 |
| `engines(pair, monday, X, XD=None, t=None)` | new (split out of `run`) | Builds the DXY lead chain, the pair's chain, its divergence, the pair's alternatives (DXY alternatives translated, D-110) and the Phase 10 source, then `E3.build` | P533:1899-1917, GS Law 7, E3C Phase 10 |
| `_cut(path, t0, t1)` | new | The part of a forecast path between t0 and t1, ends interpolated | D-131 |
| `_status(s, t_from, t_to, pair)` | new | An order's state at t_to from the 15m bars closed by then: pending / open / done | D-134 |
| `_levels(ch, Rr)` | new | The Decision-Zone trigger level per direction of a chain's alternatives: the level Engine 3 gave the alternative's orders, else the zone's edge plus its sweep reach | D-132, 6.6 Step 4 |
| `_new_zones(Xi, have, b0)` | new | Zones formed since the week anchor (S/D by origin time, LSZ of the week's daily highs / lows, IP zones drawn), only where no zone of the family is drawn | D-136, L-53 |
| `_new_zones_pine(pair, monday, adds)` | new | Draws them from the London open that found them, with "new <Day>" labels, trident_v8 colours | D-136 |
| `_day_line(ch, d, monday, t0, t1, price, X)` | new | A pure swing-scalp day's line from the day's own price, session by session, first swing to the nearer bound | L-51, P533 2.3, D-41 |
| `_flow27(pair, kept, live, seg, t_a, t_e, log, f, day, status)` | new | Law-27 trade flow on the day's line: an order the line reaches while an opposite order runs to its TP, inside that move by more than 3 pips, is not placed | D-144, E3C 6.2 / 8.21, M-61 |
| `daily_anchor(pair, monday, chain, R, src_days=None)` | new | Daily anchoring: alternative activation, day boxes + line, carry-over, order confirmation (`confirm`), clones / no copies, Phase 10 re-entry check, `_flow27`, `parts[i]`, London-open zone update + drawing re-anchor (`partsL[i]`), the <= 11 cap, numbering, contingencies. Algorithm: `ENGINEERING_REPORT.md` 6.2. | D-131 .. D-138, D-141, D-142b, D-144 |
| `run(pair, monday, daily=False)` | changed | Week-anchor engines, then `daily_anchor` when `daily`. The CLI passes `daily = '--weekly' not in sys.argv`. | D-131 |
| `DAY_CONFIRM = 'start'` | new flag | The trading-day open (17:00 NY the evening before); `'london'` = 02:00 NY (rejected: loses Asian fills) | D-131 |
| `REANCHOR = False` | new flag | Chain re-anchor for ORDERS (off) | D-136 / D-137 |
| `REANCHOR_DRAW = True` | new flag | Chain re-anchor for the LINE and DAY BOXES (on) | D-138 |
| `PHASE10_REENTRY = True` | new flag | The per-day re-entry check on receiving pairs | D-142b |
| `FLOW27 = True` | new flag | The Law-27 trade-flow check | D-144 |

## e1_tool/e2_chain.py (Engine 2; +137 / -?)

| Function / flag | New / changed | What it does | Decision / canon |
|---|---|---|---|
| `week_sessions(monday)` | changed | Drops sessions that ended before the (re-)anchor | D-136 |
| `SESSION_PATH = True` | new flag | Session-by-session drawing | L-51 |
| `_session_path(X, monday, t0, t1, pos, lo, hi, last_dir, end_at)` | new | Swing-scalp path: Asia flat; London swing to a bound; NY pre-cut 08:00-10:00 pinned at the day's largest strike inside the range; post-cut swing to the other bound; counted back from the step's end | P452 6.6 SESSION-LEVEL SHAPE MAPPING RULES 1-5, L-51 |
| `_ladder_path(X, S, a, b, t0, t1, pos, nxt, d)` | new | A breakout over several sessions drawn as a ladder: Asia holds, each London / NY session steps to a mapped level near the proportional target, the last reaches the target | D-140, P452 6.6 rules 1 / 2 / 5 / 6, GS Law 6, FA 2.1 |
| `protocols(monday)` | new | Loads `sidecar/out/protocols/<monday>.json` | Protocols D / E / G |
| `_triggers(X, date)` | changed | The day's option cuts + the coupon auctions closing that day + the EIA release of that day; NO DATA lines for F (and E when missing) | 6.6 Step 5 (d), P533:693, P452:1278-1376 |
| `build(...)` | changed | NY-cut cage uses "today"; `adj_day` clamped to the chain's first session (D-136); the 4H breakout duration in hours (`SPEED_4H_HOURS`, D-139); SS steps through `_session_path`; BS / PBS steps over several sessions through `_ladder_path` | D-136, D-139, D-140, L-51 |
| `SPEED_4H_HOURS = True` | new flag | +12 h past `BS_SESSIONS` instead of doubling | D-139, P533:2048 |
| `pine(pair, monday, E2)` | changed | Draws per-day `segments` and dotted `alt_segments` | D-131 |
| `e2_report` / `current_shape` / `_strong_4h_near` | touched | Report block "VOLATILITY TRIGGERS (as of the anchor)"; small changes | Protocols D / E / G |

## e1_tool/e3_trades.py (Engine 3; +73 / -?, + D-145)

| Function / flag | New / changed | What it does | Decision / canon |
|---|---|---|---|
| `REVERSAL_B = True`, `REVERSAL_SHAPES = ('SS','RWL','R','WL')` | new flags | Reversal entries take rule (b): 1 pip inside the close edge of the next shielding zone | D-130 -> D-135, P533:506, L-50 |
| `EU_INSIDE = False` | new flag | EUR/USD keeps rule (a): his golden EUR/USD stops measure as (a) | D-135, L-50 |
| `_stop(..., reversal=False)` | changed | The reversal branch is not vetoed by the 9.5-pip envelope; the EUR/USD inside branch exists behind `EU_INSIDE` | D-135 |
| `_build(...)` | changed | Entry attempts only deeper after an RRR failure (`e_first`); the Law-27 start (`law27`, `rest_from`, `t0` of the whiplash); **D-145**: the narrative check reads the pressure zone nested under `ip` | D-135, D-141, D-145 |
| `build(...)` | changed | `valid_from >= t0` for Law-27 entries; the cascade keys | D-141 |
| `pine(...)` | changed | A position box starts at the order's `day_anchor` | D-131 / D-141 |
| `_clear_liq(sl, entry, dn, steps, pip)` + `SL_CLEAR_LQZ = False` | new, OFF | The Trading Laws "stop inside a liquidity zone -> 2 pips outside" rule, tried and rejected | D-143 |
| `_steps`, `_mirror_conf` | touched | Small changes (see patch) | - |

## e1_tool/e1_data.py (+24)

| Function / flag | New / changed | What it does |
|---|---|---|
| `day_anchor_ms(monday, i)` | new | The London open (02:00 NY) of trading day i |
| `closed_until(pair, tf, ms)` | new | Bars of tf closed by instant ms |
| `ASOF = {}` | new | monday -> epoch ms; `boundary_ms` returns it during a daily update |
| `boundary_ms(monday)` | changed | Returns `ASOF[monday]` when set, else Monday's London open |

## e1_tool/e1_v1.py (+1)

The V1 harvest cache key includes the ASOF instant: `PAIR_TF_MONDAY_<ms>.json` (D-136).

## sidecar/protocols.py (new, 174 lines)

Protocols D (TreasuryDirect TA_WS), E (NY Fed ON RRP) and G (EIA WCESTUS1 + schedule), harvested as of each week's anchor.

Functions:
- `fetch` (cached raw);
- `et`;
- `protocol_d`;
- `eia_alternates`;
- `release`;
- `protocol_e`;
- `protocol_g`;
- `main`.

Triggers from P452:1443-1446: `BTC_TRIGGER` 2.6, `RRP_TRIGGER_BN` 50, `EIA_TRIGGER_MB` 5. Output `sidecar/out/protocols/<monday>.json`; raw pages in `sidecar/raw/protocols/`.

## tools

| File | New / changed | What it does |
|---|---|---|
| `tools/leak_check.py` | changed (+30) | Part 3: every day's trading-day-open and London-open parts identical with the bar store cut at each instant; `plutus._MEMO` cleared between runs |
| `tools/e1render` | changed | Honours `PLUTUS_FLAGS` (e.g. `--weekly`) |
| `tools/weekframe` | new | Whole-week frame per pair, one render at a time (M-60) |
| `tools/checkpoint` | new | Self-contained checkpoint folder: OmniGraph rebuilt + store copy + export, `CHECKPOINT.md`, `MANIFEST.sha256` (after M-60) |
| `tools/research/stopscen.py` | new | Locator for the M-58 item 1 stop scenarios |

## Scratch scripts used in this window (`handover/85pct_v3_full/scratchpad_scripts/`)

| Script | What it does |
|---|---|
| `tplist.py` | Daily order locator (12 maps): fill / TP / SL on 15m bars from `max(valid_from, day_anchor)` to `valid_to` |
| `lineerr.py` | Mean miss of the drawn E2 line outside each 1H bar, per pair and day |
| `sweep.py` / `sweep_daily.py` | Crash locator over every cached pair-week (D-145) |
