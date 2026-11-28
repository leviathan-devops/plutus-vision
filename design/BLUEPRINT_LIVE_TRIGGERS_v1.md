# DESIGN BLUEPRINT v1 - PLUTUS VISION: LIVE TRIGGER LAYER FOR THE ENGINE 2 LINE ("market-triggered updates")

**Status:** BENCHED. Phase 2, together with the scalping engine. No part of this document is built. The architecture in force is the simple one: fixed-time regeneration only (§9 option 2).
**Object:** a trigger compiler (Python) plus a trigger state machine (Pine) that lets the drawn Engine 2 line change between two fixed regenerations, on a pre-declared price event, without regenerating the indicator.
**Manufacture:** "built" means: one generated Pine per fixed regeneration instant which, replayed bar by bar on a Pinebox chart, draws the primary line until a declared trigger's bar closes and from that bar draws the declared branch; the file on disk does not change between fixed instants; bars already drawn never change.
**Authority:** P533 6.6 Step 4 (Decision Zone, alternative chain), P452 6.6 session rules, GS Part 6 (ZoC), operator rulings L-51, L-53, L-67, L-69 (`memory/04_OPERATOR_RULINGS_LIVE.md`).
**Depends on:** Engine 2 fixed-time line updates (`memory/19_PLAN_E2_UPDATES.md`) built, adopted and replicated first.

---

## §0 THE CONSTRAINT AND THE SPLIT IT FORCES

```
+--------------------------------------------------------------------------------------+
|  A PINE SCRIPT READS ONLY ITS OWN CHART'S BARS. IT CANNOT FETCH AND IT CANNOT RUN     |
|  THE PYTHON ENGINES.                                                                  |
+--------------------------------------------------------------------------------------+
```

A reaction to price between two regenerations is therefore possible in exactly one form: a comparison of a closed chart bar with a level that was baked into the script at the last regeneration, selecting between paths that were also baked then.

| Side of the split | Runs where | Runs when | Holds |
|---|---|---|---|
| COMPILE-TIME | Python tool | each fixed regeneration instant `U_k` | zone map, chain, primary line, the finite list of triggers for the window `[U_k, U_k+1)`, one branch path per trigger |
| CHART-TIME | Pine state machine | every confirmed chart bar inside the window | which trigger fired first, on which bar; which declared path is drawn solid |

Consequence stated once: "market-triggered" never means an unscheduled regeneration. The indicator file is static between fixed instants. A trigger selects among declared paths.

### §0.1 THE TARGET, VERBATIM

| Source | Line |
|---|---|
| M-67 | "We want to be able to detect down to the exact 30-minute candle exactly when the shapes are going to transition." |
| M-72 | "the transition from swing scalp to breakout surge could potentially hit the vertex twice or three times within a 2 to 4 hour period before the breakout surge actually begins." |
| M-72 | "there needs to be some degree of macro stability where the rendered indicator data doesn't change at all ... we need to keep it as stable and earth density as possible." |
| M-72 | "we can't have the fucking indicator changing every 30 minutes." |
| M-75 | "If this is built and engineered and coded correctly, it can obviously work better ... Sketch the blueprint, bench it." |
| P533:1895 | "construct at least one alternative chain that activates if the primary fails at a specific Decision Zone." |
| GS Part 6 | "ZoC FAILS: The front line has been broken ... The victorious army SURGES FORWARD ... ZoC HOLDS: ... Price returns to the trenches (SS)." |

---

## §1 THE STACK

```
   L4  VERIFY     leak per U_k | Pine-vs-Python firing equivalence | no-repaint | budget | lock
        ^
   L3  RENDER     Pinebox chart: primary solid, declared branches dotted; on firing the branch turns solid
        ^
   L2  DELIVER    Pine: trigger table (baked) + state machine (var state, confirmed bars only)
        ^
   L1  COMPILE    E1 map (locked) -> E2 chain + primary line -> TriggerCompiler -> TriggerTable
        ^
   L0  DATA       bar store | sealed V1 harvest | sidecar            (all as of U_k)
```

| Plane | Consumes | Produces | Owner | When absent |
|---|---|---|---|---|
| L0 DATA | bars closed by `U_k` | closed bars | `e1_data` | `DATA_MISSING`: no regeneration |
| L1 COMPILE | L0, E1 map, E2 chain | `TriggerTable` for the window | `e2_chain`, new `e2_triggers` | primary line only (the simple architecture) |
| L2 DELIVER | `TriggerTable` | Pine fragment | new `e2_triggers.pine` | fragment omitted; line static inside the window |
| L3 RENDER | Pine | chart drawings | Pinebox | no frame |
| L4 VERIFY | L1, L2, L3 outputs | pass / fail | `tools/leak_check_segments.py`, new equivalence test | nothing adopted |

---

## §2 THE MACRO ARCHITECTURE IT REUSES

The alternative-chain mechanism that already exists for ORDERS, applied to the LINE.

| Existing part | Where | Reused as |
|---|---|---|
| Decision-Zone trigger level per alternative | `plutus._levels` | level of the container-break triggers |
| Alternative chain computed at the anchor | `e2_chain.build(force_dir=...)` | source of the breakout branch |
| Conditional order live only after a close beyond its trigger | `e3_trades.pine_state` (`e3T<k>` flags) | pattern of the Pine state machine |
| Dotted alternative line | `e2_chain.pine` (`alt_segments`) | the pre-drawn, declared branch |
| Segment leak check | `tools/leak_check_segments.py` | gate V1 |

---

## §3 THE PROCESS IT PRESERVES, AND THE DIFFERENCE FROM THE SIMPLE ARCHITECTURE

| Aspect | Simple architecture (in force) | With the trigger layer (this blueprint) |
|---|---|---|
| When the indicator file changes | at the fixed instants only | at the fixed instants only (identical) |
| When the drawn line can change | at the fixed instants only | also on a declared trigger's bar inside a window |
| What can appear on the chart | the line computed at `U_k` | the line computed at `U_k` plus its declared branches (dotted from `U_k`) |
| A break of the day's ceiling / floor at 11:20 | seen at the next fixed instant | branch drawn solid from the hour close that confirms it |
| Arrival at the leg's target zone earlier / later than drawn | line keeps its drawn timing until the next fixed instant | vertex placed on the arrival bar; line holds at the zone until the next fixed instant |
| Zones, day boxes, orders | once-a-day cycle | unchanged (once-a-day cycle) |
| Past bars | frozen | frozen |
| Moving parts | 1 (scheduled regeneration) | 3 (regeneration, trigger compiler, chart-time state machine) |
| New failure classes | none | repaint, Pine / Python mismatch, chart-timeframe dependence, conflicting triggers |

---

## §4 PLANE L0 - DATA

| Component | Consumes | Produces | Invariant | Failure mode -> system action |
|---|---|---|---|---|
| `D.closed_until(pair, tf, U_k)` | bar store | bars closed by `U_k` | nothing after `U_k` | gap -> `DATA_MISSING` |
| Chart bars (chart-time) | the user's chart | confirmed bars | state machine reads `barstate.isconfirmed` bars only | chart timeframe above 1H -> `TRIG_TF_UNSUPPORTED`, triggers disabled, primary line only |

---

## §5 PLANE L1 - COMPILE

### §5.1 Wiring

```
 E1 map X(U_k) ---+
                  |      +------------------+      +-----------------+      +----------------+
 E2 chain(U_k) ---+----> | primary line for | ---> | TriggerCompiler | ---> | TriggerTable   |
 container zones         | [U_k, day end)   |      | declares <= 3   |      | triggers +     |
 alternative chains      +------------------+      | triggers        |      | branch paths   |
                                                   +-----------------+      +----------------+
```

### §5.2 The finite trigger set

| Kind | Fires when | Bar rule | Branch drawn from the firing bar | Canon |
|---|---|---|---|---|
| `BREAK_UP` | a close above the far (upper) edge of the day container's ceiling zone | the bar that closes on the hour | breakout leg to the next zone above of the same timeframe class, from the alternative chain | P533:1895; GS Part 6 ZoC fails; FA 4.4 |
| `BREAK_DOWN` | a close below the far (lower) edge of the floor zone | the bar that closes on the hour | breakout leg to the next zone below | same |
| `ARRIVAL` | price first touches the near edge of the current leg's target zone | any confirmed chart bar | vertex on that bar; flat hold at the zone until `U_k+1` | P533:215 zone by zone; M-72 repeated vertex hits are one state |

Derivation of the bar rules: the existing Decision-Zone rule for alternative orders is a 1H close beyond the level (`e3_trades.py` D-109); a bar that closes on the hour carries that same close on every chart timeframe at or below 1H, so the firing bar is identical on 15m, 30m and 1H charts. An arrival is a touch, readable on any confirmed bar.

Derivation of the count: a container has two sides, a leg has one target -> at most 3 declared triggers per window; `BREAK_*` is terminal for the window; `ARRIVAL` fires at most once -> at most 2 firings per window.

### §5.3 Typed schemas

```python
class Trigger(TypedDict):
    id: str                 # 'T<window>.<n>'
    kind: str               # 'BREAK_UP' | 'BREAK_DOWN' | 'ARRIVAL'
    level: float            # baked price
    zone: str               # Engine 1 zone label the level belongs to
    bar_rule: str           # 'HOUR_CLOSE' | 'ANY_CONFIRMED_TOUCH'
    valid_from: int         # U_k (epoch ms)
    valid_to: int           # U_k+1
    terminal: bool          # True for BREAK_*: no further firing in the window
    branch: str             # Branch.id
    why: str                # canon line

class Branch(TypedDict):
    id: str
    kind: str               # 'BREAKOUT_LEG' | 'HOLD_AT_ZONE'
    target: float | None    # next zone's near edge (BREAKOUT_LEG); None for HOLD
    target_zone: str | None
    arrive_by: int | None   # end of the chain's breakout duration (6.8 'BS 1-3 sessions'), capped at the day end
    shape: str              # 'BS' | 'PBS' | 'SS'

class TriggerTable(TypedDict):
    pair: str
    instant: int            # U_k
    window_end: int         # U_k+1
    primary: list[tuple[int, float]]      # the line computed at U_k
    triggers: list[Trigger]               # len <= 3
    branches: list[Branch]
    log: list[str]                        # one token line per undeclared / dropped trigger
```

### §5.4 Component contracts

| Component | Consumes | Produces | Invariant (checkable) | Failure mode -> system action |
|---|---|---|---|---|
| `TriggerCompiler` | primary line, container zones, alternative chains, zone map, all as of `U_k` | `TriggerTable` | every level and branch point computed from bars closed by `U_k`; `len(triggers) <= 3` | no container (shape is BS / WL) -> `TRIG_NONE_DECLARED`; table with primary only |
| level derivation | container zone far edge (+ sweep reach when the bound is a sweep zone) | `Trigger.level` | level lies beyond spot on its side at `U_k` | spot already beyond -> `TRIG_LEVEL_PASSED`; trigger not declared, the regeneration itself draws the breakout |
| branch derivation | alternative chain legs, zone map | `Branch` | target lies beyond the level on the trigger's side; target zone exists in the Engine 1 map | no zone beyond within the BS reach (GS Law 2: 100 pips) -> `TRIG_BRANCH_EMPTY`; trigger declared with `HOLD_AT_ZONE` |
| conflict rule | both `BREAK_UP` and `BREAK_DOWN` satisfied by one bar | none fired | never two terminal firings | `TRIG_CONFLICT`: primary kept, logged on the chart label |

### §5.5 Failure-token surface

| Token | Raised by | Meaning | System action |
|---|---|---|---|
| `TRIG_NONE_DECLARED` | compiler | window has no container | primary only |
| `TRIG_LEVEL_PASSED` | compiler | price already beyond the level at `U_k` | not declared |
| `TRIG_BRANCH_EMPTY` | compiler | no target zone beyond the level | hold branch |
| `TRIG_CONFLICT` | state machine | both break triggers on one bar | no firing |
| `TRIG_EXPIRED` | state machine | window ended unfired | branch stays dotted, ends at `U_k+1` |
| `TRIG_TF_UNSUPPORTED` | state machine | chart timeframe above 1H | triggers disabled |
| `TRIG_BUDGET` | pine generator | object count above the declared budget | oldest windows' dotted branches omitted |
| `TRIG_LEAK` | gate V1 | a level / branch changes when bars after `U_k` are removed | build rejected |
| `TRIG_MISMATCH` | gate V2 | Pine firing bar differs from the Python replay | build rejected |
| `TRIG_REPAINT` | gate V3 | a drawing before the replay cursor changed | build rejected |

### §5.6 The degradation contract

| Dependency | Present | Missing | Never |
|---|---|---|---|
| Alternative chain for a side | breakout branch to its target | `HOLD_AT_ZONE` branch, token | a branch to an invented level |
| Container zones | `BREAK_*` declared | `TRIG_NONE_DECLARED`, primary only | a trigger on a level that is not an Engine 1 zone edge |
| Chart timeframe <= 1H | triggers evaluated | disabled with a chart label | an hour-close rule evaluated on 4H bars |
| Trigger layer as a whole | line reacts inside the window | the simple architecture: line static until `U_k+1` | a silent difference between the two modes (the Info Table prints the mode) |

### §5.7 Production pseudocode (compile-time)

```python
def trigger_table(pair, monday, U_k, U_next, X, chain, primary):
    log, trig, br = [], [], []
    cont = container(chain, U_k)                                   # (floor zone, ceiling zone) or None
    if cont is None:
        return table(pair, U_k, U_next, primary, [], [], ['TRIG_NONE_DECLARED'])
    for kind, zone, up in (('BREAK_UP', cont[1], True), ('BREAK_DOWN', cont[0], False)):
        level = far_edge(zone, up)                                 # + sweep reach when the bound is a sweep zone
        if (X['spot'] > level) if up else (X['spot'] < level):
            log.append(f'TRIG_LEVEL_PASSED {kind}'); continue
        alt = alternative(chain, 'up' if up else 'down')           # 6.6 Step 4
        tgt = next_zone_beyond(X, level, up, tf_class(zone)) if alt else None   # FA 4.4
        b = branch('BREAKOUT_LEG', tgt, arrive_by(alt, U_k)) if tgt else branch('HOLD_AT_ZONE', None, None)
        if tgt is None: log.append(f'TRIG_BRANCH_EMPTY {kind}')
        br.append(b); trig.append(trigger(kind, level, zone, 'HOUR_CLOSE', U_k, U_next, True, b))
    leg = current_leg(primary, U_k)
    if leg and leg.target_zone:
        b = branch('HOLD_AT_ZONE', None, None); br.append(b)
        trig.append(trigger('ARRIVAL', near_edge(leg.target_zone, leg.up), leg.target_zone, 'ANY_CONFIRMED_TOUCH', U_k, U_next, False, b))
    return table(pair, U_k, U_next, primary, trig, br, log)
```

### §5.8 Worked trace (DXY, week of Apr 13 2026, Monday; numbers from `evidence/m70/M70_EXAMPLE.md` and the bar store)

| Step | Instant (New York) | Fact | Layer state |
|---|---|---|---|
| 1 | Mon 02:00 `U_k` | shape in force: swing scalps; floor zone = 1H BoM demand, far-edge level 98.525 | `BREAK_DOWN` declared at 98.525, branch `BREAKOUT_LEG` dotted |
| 2 | Mon 02:00 | alternative chain down exists; next zone below of the class = KEY SUPPORT BAND, near edge 98.054 | `Branch.target = 98.054` |
| 3 | Mon 10:00 - 14:30 | closes 98.808, 98.769, 98.603, 98.561, 98.544: all above 98.525 | armed, nothing fired |
| 4 | Mon 15:00 | the bar closing on the hour closes 98.366 < 98.525 | `firedBar` set; branch solid from this bar; primary remainder dim |
| 5 | Mon 15:00 - Tue 08:00 | candles: 98.415 (17:00), 98.343 (Tue 02:00), 98.053 (Tue 08:00) | branch target 98.054 reached |
| 6 | Tue 02:00 `U_k+1` | fixed regeneration: new primary from the actual price, new triggers | previous window's table expired |

The simple architecture draws step 4's change at the next fixed instant instead of on the 15:00 bar. That is the whole difference this layer makes on this day.

### §5.9 Constants and their sources

| Constant | Value | Source |
|---|---|---|
| declared triggers per window | <= 3 | two container sides + one leg target (§5.2 derivation) |
| firings per window | <= 2 | `BREAK_*` terminal, `ARRIVAL` once (§5.2 derivation) |
| break bar rule | close of the bar that ends on the hour | existing Decision-Zone rule: 1H close beyond the level (D-109; P533:1895) |
| break level | far edge of the container zone, plus sweep reach 0.05-0.10 when the bound is a sweep zone | `plutus._levels`; P533 Step 0.45a |
| breakout reach | 100 pips | GS Law 2 (BS / RWL) |
| breakout arrival | chain figure, 6.8 "BS 1-3 sessions" | P533 6.8; `e2_chain.BS_SESSIONS` |
| chart timeframes supported | 15m, 30m, 1H | hour-close visible on each; Pinebox cannot read other timeframes |
| Pine object budgets | 2000 boxes / labels / lines | `e1_pine.py` indicator() declaration |
| regeneration instants `U` | the set approved for the fixed-time line | `memory/19_PLAN_E2_UPDATES.md` |

---

## §6 PLANE L2 - DELIVER

```pine
// baked at U_k:  tKind[], tLevel[], tFrom, tTo, branch point arrays, primary point arrays
var int  firedBar  = na          // bar_index of the first terminal firing in this window
var int  firedId   = na
var int  arrivedBar = na
onHour  = minute(time_close) == 0
inWin   = time >= tFrom and time < tTo
if isPair and barstate.isconfirmed and inWin and na(firedBar)
    up = onHour and close > tLevelUp
    dn = onHour and close < tLevelDown
    if up and not dn
        firedBar := bar_index, firedId := 1
    else if dn and not up
        firedBar := bar_index, firedId := 2
    else if na(arrivedBar) and (legUp ? high >= tArrive : low <= tArrive)
        arrivedBar := bar_index
// drawing (on the last bar): primary solid up to min(firedBar, arrivedBar); declared branches dotted from tFrom;
// the fired branch solid from its firing bar; nothing before a firing bar is redrawn
```

| Component | Consumes | Produces | Invariant | Failure mode -> system action |
|---|---|---|---|---|
| `e2_triggers.pine(table)` | `TriggerTable` | Pine fragment under `if show_e2` | every literal is in the table; object count within the script's declared budgets (2000 boxes / labels / lines) | budget -> `TRIG_BUDGET` |
| state machine | confirmed chart bars | `firedBar`, `firedId`, `arrivedBar` | each variable written at most once per window; written on confirmed bars only | timeframe above 1H -> `TRIG_TF_UNSUPPORTED` |

---

## §7 PLANE L3 - RENDER

| Element | Before any firing | After `ARRIVAL` | After `BREAK_*` |
|---|---|---|---|
| Primary line | solid, as computed at `U_k` | solid up to the arrival bar, vertex on that bar, flat at the zone to `U_k+1` | solid up to the firing bar, remainder dim |
| Declared branches | dotted from `U_k` | unchanged | fired branch solid from the firing bar; the other dotted |
| Day box, zones, orders | unchanged | unchanged | unchanged (the once-a-day cycle updates them) |
| Info Table | mode "triggers: armed (n)" | "arrived <zone> <time>" | "fired <kind> <time>" |

| Component | Consumes | Produces | Invariant | Failure mode -> system action |
|---|---|---|---|---|
| Pinebox render | Pine | chart frame | declared branches visible from `U_k` | render refused -> no frame, nonzero exit |

---

## §8 PLANE L4 - VERIFY

| Gate | Check | Can fail by |
|---|---|---|
| V1 leak | tool run on a store cut at `U_k`: `TriggerTable` identical to the full run | `TRIG_LEAK` |
| V2 equivalence | Python replay of the state machine on 15m, 30m and 1H bars: same firing bar close time as the Pine on each chart | `TRIG_MISMATCH` |
| V3 no-repaint | Pinebox replay stopped at two cursors `c1 < c2`: every drawing ending before `c1` identical | `TRIG_REPAINT` |
| V4 bound | per window: declared <= 3, fired <= 2 | count exceeded |
| V5 invariance | zones, day boxes, orders identical with the layer on and off | any difference |
| V6 measured value | line metric (30m closes within 10 pips) with the layer on vs the simple architecture, same weeks, same instants | not better on the test weeks -> layer stays off |
| V7 lock | Engine 1 SHA-256 lock | mismatch |

---

## §9 THE DELIVERY

| Rank | Option | Verdict |
|---|---|---|
| 1 | Fixed-time regeneration only; line static inside each window | IN FORCE NOW (the simple architecture) |
| 2 | Fixed-time regeneration + declared triggers evaluated by the Pine on chart bars (this blueprint) | BENCHED, phase 2 |
| 3 | An outside watcher regenerates the indicator the moment price crosses a level | REJECTED: the file changes at unpredictable moments (L-67 stability) |
| 4 | The Pine fetches a new line from the tool when a level breaks | IMPOSSIBLE: Pine cannot fetch (§0) |

---

## §10 THE LEARN LOOP

```
 per fired trigger: firing bar, branch target, what the candles did until U_k+1
     --> branch right / wrong / early / late, by kind
     --> wrong branch traced to its derivation row (§5.4) and that row's canon line
     --> repair of the derivation, rerun of every week already measured
```

---

## §11 THE ANTI-PATTERNS - WIRED

| # | Defect class | Mechanical detector |
|---|---|---|
| A1 | Repaint: bars already drawn change after a firing | V3 |
| A2 | Price follower: the line re-anchors to each bar's close | V4 (fired <= 2 per window) + schema: only 3 trigger kinds exist |
| A3 | Undeclared change: a path appears that was not dotted from `U_k` | diff of the drawing set at `U_k` vs after firing: solid paths must be a subset of declared paths |
| A4 | Level from after `U_k` | V1 |
| A5 | Different firing on 15m, 30m, 1H charts | V2 |
| A6 | Trigger on a level that is not an Engine 1 zone edge | assert `Trigger.zone` resolves in the map |
| A7 | Triggers silently on / off | Info Table prints the mode; V5 run in both modes |
| A8 | Layer changes orders, boxes, zones | V5 |
| A9 | Layer kept although it does not improve the measured line | V6 |
| A10 | Engine 1 edited | V7 |

---

## §12 THE BUILD SEQUENCE

| Phase | Work | Exit that can fail |
|---|---|---|
| P0 | Precondition | fixed-time Engine 2 line adopted by the operator and replicated on the test weeks; else stop |
| P1 | `TriggerCompiler` (report only, no Pine) | V1 passes on golden + 4 checkpoint weeks; every window prints <= 3 triggers with zone labels |
| P2 | Python replay of the state machine | V4 passes; firings listed per week |
| P3 | Pine fragment | V2 and V3 pass on 15m, 30m, 1H charts |
| P4 | Measurement | V6: line metric vs the simple architecture on the same weeks |
| P5 | Frames to the operator (simple vs trigger layer, side by side) | operator verdict; nothing adopted before it |

---

## §13 WHAT IT INHERITS

| Inherited | From | State |
|---|---|---|
| Decision-Zone levels, alternative chains | `plutus._levels`, `e2_chain.build` | built |
| Conditional activation pattern in Pine | `e3_trades.pine_state` | built for orders |
| Dotted alternative segments | `e2_chain.pine` | built |
| Fixed regeneration instants and the primary line per window | Engine 2 plan `memory/19` | NOT built: precondition P0 |
| Leak check on drawn segments | `tools/leak_check_segments.py` | built |

---

## §14 THE FILE LAYOUT

| Path | Holds |
|---|---|
| `design/BLUEPRINT_LIVE_TRIGGERS_v1.md` | this document |
| `e1_tool/e2_triggers.py` | new: compiler, schemas, Python replay, Pine fragment |
| `e1_tool/plutus.py` | one switch-guarded call per regeneration |
| `tools/trigger_equivalence.py` | new: gates V2, V3 |
| `evidence/triggers/` | frames, firing ledgers |

---

## §15 THE RISK REGISTER

| Rank | Risk | Severity | Mitigation |
|---|---|---|---|
| 1 | Repaint: the chart shows a past it did not show live | HIGH | confirmed-bar state, write-once variables, gate V3 |
| 2 | Pine and Python disagree on the firing bar (chart timeframe, bar alignment) | HIGH | hour-close rule, gate V2 on three chart timeframes |
| 3 | A false break fires the terminal branch (wick-and-return over the hour close) | HIGH | level = the zone's FAR edge plus sweep reach; measured in V6; layer stays off unless better |
| 4 | Branch target wrong (alternative chain weak) | MEDIUM | `HOLD_AT_ZONE` when no zone beyond; learn loop |
| 5 | Chart clutter from dotted branches | MEDIUM | at most 3 per window; ended at `U_k+1` |
| 6 | The Pinebox engine cannot read another timeframe (`request.security` returns NaN) | MEDIUM | design uses the chart's own bars only |
| 7 | Scope creep into orders | MEDIUM | V5; orders stay on the once-a-day cycle |

---

## SUMMARY

A Pine script reads only its own chart and cannot run the engines, so a reaction to price between two regenerations can exist only as a baked comparison that selects among baked paths. The trigger layer therefore changes nothing about when the indicator is generated: at each fixed instant the tool also declares at most three triggers for the coming window - a close on the hour beyond the day container's ceiling or floor, and the arrival at the current leg's target zone - each with one pre-drawn dotted branch. On the chart, a write-once state machine on confirmed bars turns the fired branch solid from its bar; past bars, zones, boxes and orders never change. Gates prove no leak, identical firing on 15m, 30m and 1H charts, no repaint, and a measured gain over the simple architecture before anything is adopted. The layer is benched until the fixed-time line is proven.
