# DESIGN BLUEPRINT v1 - PLUTUS VISION: SCALPING ENGINE (ENGINE 3, PHASE 2)

**Status:** BENCHED. Phase 2. No part of this document is built. Build order: Engine 2 first, then this.
**Object:** a Python module of the Plutus tool that emits swing-scalp orders (Scalp Stack) into the generated Pine script.
**Manufacture:** "built" means: on a Pinebox 15m chart of a trading week, every swing-scalp day shows scalp position boxes that fill and reach their take-profit on that day's candles, counted by the replay ledger, with the swing orders of the same week unchanged.
**Authority:** `canon/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md` (P533), `canon/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md` (E3C), `TTE_GOLDEN_STANDARD_COMPLETE_REFERENCE.md` (GS), `canon/Toolset/Trident_Fractal_Architecture_FirstPrinciples_v2.3.md` (FA), operator rulings L-52, L-67, L-68, L-69 (`memory/04_OPERATOR_RULINGS_LIVE.md`).
**Depends on:** Engine 2 intraday line (`memory/19_PLAN_E2_UPDATES.md`), not yet approved.

---

## §0 THE CONSTRAINT AND THE SPLIT IT FORCES

```
+--------------------------------------------------------------------------------------+
|  A PINE SCRIPT CANNOT FETCH. BETWEEN TWO REGENERATIONS THE CHART HOLDS ONLY WHAT      |
|  WAS COMPUTED AT THE LAST REGENERATION, FROM BARS CLOSED BEFORE IT.                   |
+--------------------------------------------------------------------------------------+
```

A swing scalp lives one to six hours. The indicator is regenerated at a small set of fixed instants. A scalp order therefore exists on the chart only as a RESTING ORDER computed at a regeneration instant and valid until the next one.

| Side of the split | Runs where | Runs when | Holds |
|---|---|---|---|
| REGENERATION-TIME | Python tool | each regeneration instant `U_k` | zone map, gate state, scalp range, resting scalp orders for the window `[U_k, U_k+1)` |
| CHART-TIME | Pine, on the chart's own bars | every closed chart bar | fill detection, TP / SL detection, one-at-a-time flow, order expiry, container-break kill switch on a baked level |

Second substrate fact: the bar store holds 15m, 30m, 1H, 4H bars. It holds no 5m bars. The Scalp Stack's 5m refinement layer has no data source.

### §0.1 THE TARGET, VERBATIM

| Source | Line |
|---|---|
| M-73 | "On swing scalps, you should be shifting down to the 30-minute or the 15-minute time frame and catching all of the moves between the ceiling and the floor zone." |
| M-73 | "It's the exact same mechanics as the higher time frame swings ... The only difference is that you're executing them on lower time frames at the speed of a scalping engine." |
| M-73 | "There's a 30-minute supply and a 30-minute demand, and the price is oscillating between the ceiling and floor ... for literally the whole trading day. There's 8 solid trades ... Everything is 3 to 5 risk-reward ratio." |
| M-73 | "It needs to respect the shape chain transition ... the swing scalps don't happen in a vacuum." |
| M-75 | "The scalps can have their own separate trading meter where we can put a limit of 20 per week, specifically on scalps that begin and end on the lower time frames of the 30-minute or the 15-minute." |
| P533:554-562 | "Scalp Stack (Swing Scalps within consolidation): HTF Storyline 30m; Trading Timeframe 15m; Precision / Entry Refinement 5m ... All LTF trade setups are anchored on the 15m." |
| P533:564 | "A Breakout Surge on the Swing Stack (4H->1H->30m) is mechanically identical to a Swing Scalp on the Scalp Stack (30m->15m->5m) ... only the pip scale and SL threshold differ." |
| P533:2079 | "SS | Swing Scalps (both directions) | Scalp Stack | 4-8 swing scalps" |
| GS Part 8 | "TP timeframe >= Entry timeframe. A 15m scalp entry NEVER targets another 15m zone - it always targets at least 30m." |

---

## §1 THE STACK

One dependency direction: each plane consumes only planes below it.

```
   L4  VERIFY     leak check per regeneration instant | replay ledger | frame inspection
        ^
   L3  RENDER     Pinebox chart: scalp position boxes, tag "scalp", toggle show_scalp
        ^
   L2  DELIVER    Pine fragment: baked order table + chart-time state machine
        ^
   L1  COMPUTE    E1 map (locked) -> E2 gate + container -> SCALP: range -> candidates -> orders -> meter
        ^
   L0  DATA       bar store 15m / 30m / 1H / 4H | sealed V1 liquidity harvest | sidecar
```

| Plane | Consumes | Produces | Owner | When absent |
|---|---|---|---|---|
| L0 DATA | TradingView bars, V1 harvest cache | closed bars up to `U_k` | `e1_data`, `e1_v1` | tool refuses the map: `DATA_MISSING` |
| L1 COMPUTE | L0 | `ScalpPlan` per `U_k` | `e1_pine`, `e2_chain`, new `e3_scalp` | no scalp orders; swing orders unaffected |
| L2 DELIVER | `ScalpPlan` | Pine lines inside `if show_scalp` | new `e3_scalp.pine` | fragment omitted; Pine compiles without it |
| L3 RENDER | Pine source | boxes on the chart | Pinebox | no frame; exit code nonzero |
| L4 VERIFY | L1 output, L3 frame | pass / fail per gate | `tools/leak_check*.py`, `tools/research/devset.py` | nothing is adopted |

---

## §2 THE MACRO ARCHITECTURE IT REUSES

The swing engine (`e1_tool/e3_trades.py`, E3C phases 0-12) with the timeframe roles shifted one stack down. No new mechanics.

| Role | Swing Stack (built) | Scalp Stack (this blueprint) | Source |
|---|---|---|---|
| Storyline timeframe | 4H | 30m | P533:546-560 |
| Trading timeframe | 1H | 15m | P533:546-560 |
| Refinement timeframe | 30m | 5m (no data: §5.6) | P533:562 |
| Range frame | day box ceiling / floor (4H / 1H level) | 30m supply / 30m demand inside the day box | M-73 |
| Entry zone | 1H zone edge / V1 1H rung | 15m zone edge at the 30m zone | GS Law 3 |
| TP zone | opposing 1H / 4H zone | opposing 30m zone | GS Part 8, M-73 |
| Weekly cap | 11 per pair (R-07) | 20 per pair, separate meter | M-75 |
| Flow | one trade per move, entry = prior TP (L-52, Law 27) | same | L-52 |

---

## §3 THE PROCESS IT PRESERVES

| Existing behaviour | Preserved | Changed |
|---|---|---|
| Engine 1 map, locked by SHA-256 (`tools/locks`) | yes, read only | nothing |
| Engine 2 chain, day boxes, shape tags | yes, read only | nothing |
| Swing orders: daily confirmation at the trading-day open | yes | nothing; scalps are a second order family |
| Position box drawing from fill to TP (D-146) | yes, reused | tag text "scalp" |
| One trade per move (L-52) | yes | applied inside the scalp family and across families |
| Temporal anchor: nothing after an anchor feeds a level | yes | anchor set = the regeneration instants `U` |
| Cap of 11 swing setups per pair-week | yes | scalps counted on their own meter |

---

## §4 PLANE L0 - DATA

| Component | Consumes | Produces | Invariant | Failure mode -> system action |
|---|---|---|---|---|
| `D.closed_until(pair, tf, U_k)` | bar store JSON | bars with `time + tf <= U_k` | no bar closes after `U_k` | store gap -> `DATA_MISSING`, no scalp plan for the window |
| V1 liquidity harvest (15m not harvested today) | sealed V1 via Pinebox probe | 1H rungs, 4H bands | harvest keyed by the as-of instant | harvest absent -> entries at 15m zone edges only, token `SCALP_NO_RUNG` |
| Option cuts of the day | sidecar JSON | strikes, notionals, cut date | as-of gated | absent -> cage rule not applied, printed `NO DATA` |

---

## §5 PLANE L1 - COMPUTE (the scalp module)

### §5.1 Wiring

```
 E1 map X(U_k) ----+
                   |        +-------------+     +--------------+     +-----------------+     +-------------+
 E2 state(U_k) ----+------> | ScalpGate   | --> | ScalpRange   | --> | ScalpCandidates | --> | ScalpOrders | --+
 (shape in force,           | open/closed |     | 30m ceiling  |     | 15m entry zones |     | E / SL / TP |   |
  container zones)          +-------------+     | 30m floor    |     | both directions |     | confidence  |   |
                                                +--------------+     +-----------------+     +-------------+   |
                                                                                                               v
                                      week ledger (fills so far, from bars closed by U_k) ---------------> ScalpMeter + FlowSequencer --> ScalpPlan
```

### §5.2 Typed schemas

```python
class ScalpGate(TypedDict):
    open: bool                 # True only while the Engine 2 shape in force at U_k is swing scalps (or a recovery in swing-scalp form)
    shape: str                 # 'SS' | 'R'
    chain_pos: str             # 'before-BS' | 'after-BS' | 'after-WL' | 'recovery'   (M-73: never in a vacuum)
    container: tuple[Zone, Zone]   # (floor zone, ceiling zone) of the day box, from Engine 2
    kill_up: float             # baked level: a close beyond the ceiling zone's far edge ends the gate (chart-time)
    kill_down: float           # baked level: a close beyond the floor zone's far edge ends the gate (chart-time)
    reason: str                # failure token when open is False

class ScalpRange(TypedDict):
    ceiling: Zone              # standing 30m SUPPLY inside the container (tf '30' or 'NN Refined 30m' / '30m Refined 1H')
    floor: Zone                # standing 30m DEMAND inside the container
    height: float              # ceiling.bot - floor.top, in price
    reactions: tuple[int, int] # reaction count (floor, ceiling) since each zone formed

class ScalpOrder(TypedDict):
    id: str                    # '<PAIR>S<n>', numbered on the scalp meter
    dir: str                   # 'LONG' | 'SHORT'
    entry: float               # 15m zone edge at the 30m zone, GS Law 3
    sl: float                  # behind the next zone, scalp stop rule
    tp: float                  # opposing 30m zone, near edge
    rrr: float
    confidence: int            # E3C Phase 5 scale
    valid_from: int            # U_k (epoch ms)
    valid_to: int              # U_k+1
    entry_zone: Zone           # 15m zone (trading timeframe)
    frame_zone: Zone           # 30m zone (storyline timeframe)
    stack: str                 # always 'SCALP'
    why: str                   # canon line per decision

class ScalpPlan(TypedDict):
    pair: str
    instant: int               # U_k
    gate: ScalpGate
    range: ScalpRange | None
    orders: list[ScalpOrder]
    meter_used: int            # scalps filled this week before U_k
    log: list[str]             # one line per discarded candidate: token + numbers
```

### §5.3 Component contracts

| Component | Consumes | Produces | Invariant (checkable) | Failure mode -> system action |
|---|---|---|---|---|
| `ScalpGate` | E2 state at `U_k`: shape in force, chain position, container zones | `ScalpGate` | `open` implies shape in {SS, R} and both container zones present | shape is BS / WL / RWL -> `SCALP_GATE_CLOSED`, zero scalp orders, swing engine owns the window |
| `ScalpRange` | E1 `sd` zones with 30m in their timeframe label, inside the container, standing at `U_k` | `ScalpRange` | `floor.top < spot < ceiling.bot`; both zones wholly inside the container | no 30m zone on one side -> `SCALP_RANGE_NONE`; the container zone itself frames that side, logged |
| `ScalpCandidates` | `ScalpRange`, E1 15m zones and V1 rungs overlapping each 30m zone | list of (direction, 15m entry zone, 30m frame zone) | every entry zone overlaps its frame zone; supply -> SHORT, demand -> LONG | no 15m zone in the 30m zone -> entry at the 30m zone's near edge, token `SCALP_ENTRY_HTF_EDGE` |
| `ScalpOrders` | candidates, zone map, pair profile | `ScalpOrder` list | `rrr >= RRR_FLOOR`; `tp` zone timeframe >= entry zone timeframe; SL beyond a zone edge | see §5.5 token table: candidate discarded with a logged token |
| `ScalpMeter` | week ledger of filled scalps before `U_k` | remaining count | `meter_used + len(orders that can still fill) <= 20` | meter full -> `SCALP_METER_FULL`, lowest-confidence orders dropped first |
| `FlowSequencer` | orders of the window, open positions at `U_k` | orders with flow links | at most one open scalp per pair per direction of one oscillation; a scalp never opposes an open swing order inside that swing's move | conflict -> `SCALP_DUP_MOVE` or `SCALP_AGAINST_SWING`, order dropped |

### §5.4 Decision rules, each with its derivation

| Rule | Statement | Derived from |
|---|---|---|
| G1 | Gate open only for SS or R in swing-scalp form, inside the chain | M-73; P533:2079-2082 |
| G2 | Gate closes at chart-time on a close beyond a container zone's far edge | GS Part 6 "ZoC FAILS: ... BS is imminent"; P533 6.6 Step 4 |
| R1 | Range frame = standing 30m supply and 30m demand inside the container | M-73 "a 30-minute supply and a 30-minute demand" |
| R2 | A 30m zone with 3 or more reactions is not an entry side | P533:211 "3+ = depleted (likely to pierce) ... TP targets only" |
| R3 | A virgin MoM zone is not an entry | P533:491 "Virgin MoM zones are DEATH ZONES" |
| E1 | Entry at the 15m zone edge, 0-2 pips inside | GS Law 3 "15m zone edges for scalps: entry at zone boundary +- 2 pips inside" |
| S1 | SL behind the next zone beyond the entry zone; scalp distance 5-8 pips typical | GS Law 3 table (Scalp: SL 5-8 pips); GS Law 4 (behind a liquidity shield) |
| S2 | GBP/USD: the shield is the liquidity beyond the zone; EUR/USD: inside the zone | L-50; FA 10 |
| T1 | One TP at the opposing 30m zone, near edge | M-73; GS Part 8; GS Law 6 "ONE TP" |
| Q1 | `RRR_FLOOR = 3.0` | M-73 "3 to 5 risk-reward ratio"; E3C RRR floor 3.0 |
| Q2 | Confidence >= 65 | R-07 |
| Q3 | Meter = 20 scalps per pair-week | M-75 |
| F1 | One scalp per oscillation; next entry = the previous TP zone | L-52; GS Law 27 trade chaining |
| P1 | London session is the scalp session; NY second half belongs to swings | P533:698-710 |

### §5.5 Failure-token surface

| Token | Raised by | Meaning | System action |
|---|---|---|---|
| `SCALP_GATE_CLOSED` | ScalpGate | shape in force is not swing scalps | no scalp orders this window |
| `SCALP_CONTAINER_BROKEN` | ScalpGate | a bar closed beyond a container zone before `U_k` | gate closed; transition entry belongs to the swing engine |
| `SCALP_RANGE_NONE` | ScalpRange | no standing 30m zone on a side | container zone frames that side |
| `SCALP_RANGE_TOO_NARROW` | ScalpOrders | range height cannot give `RRR_FLOOR` with the stop rule | no orders; logged with the numbers |
| `SCALP_ZONE_DEPLETED` | ScalpCandidates | 30m zone has 3+ reactions | that side is TP only |
| `SCALP_MOM_VIRGIN` | ScalpCandidates | virgin MoM entry zone | candidate discarded |
| `SCALP_ENTRY_HTF_EDGE` | ScalpCandidates | no 15m zone inside the 30m zone | entry at the 30m near edge, confidence penalty per E3C |
| `SCALP_SL_NO_SHIELD` | ScalpOrders | no zone / liquidity behind the entry within the stop envelope | widen to the next shield or discard |
| `SCALP_TP_TF_LOW` | ScalpOrders | only a 15m zone opposes | discarded (GS Part 8) |
| `SCALP_RRR_LOW` | ScalpOrders | `rrr < RRR_FLOOR` | discarded |
| `SCALP_CONF_LOW` | ScalpOrders | confidence < 65 | discarded |
| `SCALP_METER_FULL` | ScalpMeter | 20 filled or resting this week | lowest confidence dropped |
| `SCALP_DUP_MOVE` | FlowSequencer | same oscillation already has an order | dropped |
| `SCALP_AGAINST_SWING` | FlowSequencer | opposes an open swing order inside its move | dropped |
| `SCALP_NO_5M` | ScalpOrders | 5m refinement layer has no data | 15m edge used; printed in the report |
| `SCALP_NO_RUNG` | ScalpCandidates | no V1 rung on 15m | zone edge only |

### §5.6 The degradation contract

| Dependency | Present | Missing | Never |
|---|---|---|---|
| Engine 2 intraday state | gate decided at each `U_k` | gate decided once at the day's London open; windows = one per day | a gate assumed open |
| 30m zones inside the container | 30m frame | container zones frame the range, printed | an invented zone |
| 15m zones inside the 30m zone | 15m entry edge | 30m near edge, token `SCALP_ENTRY_HTF_EDGE` | a mid-zone entry with no level |
| 5m bars | refinement of entry | 15m edge, token `SCALP_NO_5M` in the report | a silent claim of 5m precision |
| V1 15m liquidity | rung entries / shields | 1H rungs only | a fabricated rung |

### §5.7 Production pseudocode

```python
def scalp_plan(pair, monday, U_k, U_next, X, e2_state, ledger):
    log = []
    gate = scalp_gate(e2_state)                                   # G1
    if not gate['open']:
        return plan(pair, U_k, gate, None, [], ledger, log + [gate['reason']])
    rng = scalp_range(X, gate['container'], X['spot'])            # R1
    orders = []
    for side, frame in (('SHORT', rng['ceiling']), ('LONG', rng['floor'])):
        if reactions(frame) >= 3:                                 # R2
            log.append(f"SCALP_ZONE_DEPLETED {side} {frame['bot']}-{frame['top']}"); continue
        for ez in entry_zones_15m(X, frame, side) or [frame]:     # E1; frame itself -> SCALP_ENTRY_HTF_EDGE
            if ez['kind'] == 'MoM' and ez['mit'] == 0:            # R3
                log.append('SCALP_MOM_VIRGIN'); continue
            entry = edge_inside(ez, side)                         # 0-2 pips inside, GS Law 3
            sl, why_sl = scalp_stop(X, pair, ez, side)            # S1, S2
            tp_zone = rng['floor'] if side == 'SHORT' else rng['ceiling']
            if tf_rank(tp_zone) < tf_rank(ez):                    # T1, GS Part 8
                log.append('SCALP_TP_TF_LOW'); continue
            tp = near_edge(tp_zone, side)
            rrr = abs(tp - entry) / abs(entry - sl)
            if rrr < RRR_FLOOR:                                   # Q1
                log.append(f"SCALP_RRR_LOW {rrr:.2f}"); continue
            conf = confidence(X, ez, frame, side)                 # E3C Phase 5
            if conf < 65:                                         # Q2
                log.append(f"SCALP_CONF_LOW {conf}"); continue
            orders.append(order(side, entry, sl, tp, rrr, conf, U_k, U_next, ez, frame, why_sl))
    orders = flow_sequence(orders, ledger, log)                   # F1
    orders = meter(orders, ledger, limit=20, log=log)             # Q3
    return plan(pair, U_k, gate, rng, orders, ledger, log)
```

### §5.8 Constants and their sources

| Constant | Value | Source |
|---|---|---|
| `RRR_FLOOR` | 3.0 | M-73 "3 to 5 risk-reward ratio"; E3C RRR floor |
| `SCALP_METER` | 20 per pair-week | M-75 |
| `CONF_MIN` | 65 | R-07 |
| `DEPLETED_AT` | 3 reactions | P533:211 |
| entry inset | 0-2 pips inside the zone | GS Law 3 |
| scalp stop distance | 5-8 pips typical, behind a shield | GS Law 3 table, GS Law 4 |
| 15m zone width | 5-22 pips | GS Law 1 |
| 30m zone width | 10-35 pips | GS Law 1 |
| expected scalps per swing-scalp day | 4-8 | P533:2079 |
| Refined join distance | 5 pips | GS Part 11 |

---

## §6 PLANE L2 - DELIVER

Pine fragment contract (one block inside the generated script):

```pine
// baked at regeneration U_k - one row per ScalpOrder
// sDir[], sEntry[], sSL[], sTP[], sFrom[], sTo[]     (levels are the anchor's; bars are the chart's)
// sKillUp, sKillDown                                  (container far edges)
var bool sGateLive = true
if isPair and barstate.isconfirmed and time >= U_k and (close > sKillUp or close < sKillDown)
    sGateLive := false                                 // G2: container broken -> resting scalps cancelled from this bar
// per order: fill on touch of sEntry while sGateLive and time in [sFrom, sTo); then SL first, then TP (D-146 rules)
```

| Component | Consumes | Produces | Invariant | Failure mode -> system action |
|---|---|---|---|---|
| `e3_scalp.pine(plan)` | `ScalpPlan` | Pine lines under `if show_scalp` | no literal that is not in the plan; object count within the script's declared budgets (2000 boxes / labels / lines) | budget exceeded -> oldest closed windows drawn as stubs, token `PINE_BUDGET` |
| chart-time state machine | chart bars | fill / exit bars per order | state changes only on confirmed bars; never rewrites a past box | chart timeframe above 30m -> scalp boxes hidden, label "scalps: open a 15m / 30m chart" |

---

## §7 PLANE L3 - RENDER

| Component | Consumes | Produces | Invariant | Failure mode -> system action |
|---|---|---|---|---|
| Pinebox IDE load | generated Pine | chart drawing counts | boxes > 0 when the plan has orders | `REFUSED` / error -> no frame written, nonzero exit |
| Frame capture (15m, one day per frame) | chart | PNG under `evidence/` | whole trading day visible, price axis fitted | truncated axis -> frame rejected by the inspection step |

---

## §8 PLANE L4 - VERIFY

| Gate | Check | Can fail by |
|---|---|---|
| V1 leak | run cut at every `U_k`: orders of windows starting by `U_k` identical to the full run | any difference -> exit 1 |
| V2 swing invariance | swing orders (E / SL / TP list) identical with the scalp module on and off | any difference |
| V3 replay ledger | per pair-week: scalps drawn / filled / TP / SL, on 15m bars, SL first on a double touch | ledger missing a drawn order |
| V4 meter | filled scalps per pair-week <= 20 | 21st fill |
| V5 flow | no two open scalps of one oscillation; none opposing an open swing | overlap found |
| V6 frames | every swing-scalp day frame opened; each box judged filled / TP / SL against candles | unopened frame cited |
| V7 lock | Engine 1 SHA-256 lock clean | hash mismatch |

---

## §9 THE DELIVERY

| Rank | Option | Verdict |
|---|---|---|
| 1 | Resting scalp orders baked at each fixed regeneration instant; fills tracked at chart-time | CHOSEN |
| 2 | Scalp orders baked once a day at the London open (no intraday regeneration) | FALLBACK when Engine 2 has no intraday state: fewer, staler orders |
| 3 | Pine detects 15m / 30m zones live and builds scalps itself | REJECTED: duplicates Engine 1 inside Pine; two zone maps that can disagree |
| 4 | Pine fetches fresh orders from the tool during the session | IMPOSSIBLE: Pine cannot fetch (§0) |

---

## §10 THE LEARN LOOP

```
 replay ledger (V3) --> every SL and every missed oscillation listed with its zone ids
        --> trace to the rule of §5.4 that produced / blocked it
        --> canon line re-read --> rule repaired (never a cap or a filter)
        --> rerun golden week + every week already passed
```

Oracle: the library's "Swing Scalps" folder (`context_management/oracle/library/trades.json`). Additional marked charts arrive only on the operator's schedule.

---

## §11 THE ANTI-PATTERNS - WIRED

| # | Defect class | Mechanical detector |
|---|---|---|
| A1 | Scalp with no 30m frame zone | schema check: `frame_zone.tf` contains '30' or the order carries `SCALP_RANGE_NONE` |
| A2 | Scalp outside the gate (on a BS / WL day) | assert `gate.open` for every order's window |
| A3 | Scalp counted on the swing meter, or swing on the scalp meter | two counters; V4 + swing cap test |
| A4 | Duplicate orders for one oscillation | V5 overlap scan |
| A5 | Level from after the anchor | V1 cut-run comparison |
| A6 | Entry at a 30m / 1H edge sold as 15m precision | token `SCALP_ENTRY_HTF_EDGE` must be present when `entry_zone.tf != '15'` |
| A7 | TP at a 15m zone | assert TP zone timeframe >= 30m |
| A8 | Stop with no zone behind it | assert `sl` lies beyond a zone edge in the map |
| A9 | Scalp module changes swing orders | V2 |
| A10 | Fewer trades presented as a higher win rate | ledger prints drawn / filled / TP / SL and oscillations available per day |
| A11 | Claimed 5m refinement without 5m data | grep the report for `SCALP_NO_5M` whenever the store has no 5m |
| A12 | Engine 1 edited to make scalps fit | V7 |

---

## §12 THE BUILD SEQUENCE

| Phase | Work | Exit that can fail |
|---|---|---|
| P0 | Precondition | Engine 2 intraday line adopted by the operator; else stop |
| P1 | `ScalpGate` + `ScalpRange`, report only | on the golden week and 4 checkpoint weeks: every swing-scalp day prints a range whose two zones exist in the Engine 1 map; V1, V7 pass |
| P2 | `ScalpCandidates` + `ScalpOrders`, behind a switch (off) | V1, V2, V7 pass; every discarded candidate has a token |
| P3 | Meter + flow | V4, V5 pass on all cached pair-weeks |
| P4 | Pine fragment + chart-time state machine | Pinebox renders; box counts equal plan counts; chart-time fills equal the Python replay on 15m bars |
| P5 | Frames + ledger to the operator | operator verdict; nothing adopted before it |

---

## §13 WHAT IT INHERITS

| Inherited | From | State |
|---|---|---|
| Zone map with 15m / 30m supply-demand, BoM / MoM, mitigation, Refined, nested_in | `e1_tool/e1_sd.py` | built, locked |
| Shape in force, container zones, chain position | `e1_tool/e2_chain.py`, `plutus.daily_anchor` | built (daily); intraday pending |
| Stop rules, pair profiles, confidence, RRR | `e1_tool/e3_trades.py` phases 3-5 | built for the Swing Stack |
| Live fill / exit tracking in Pine | `e3_trades.pine_state` | built |
| Leak gates, Engine 1 lock, replay | `tools/leak_check.py`, `tools/locks`, `tools/research/devset.py` | built |

Held for the operator when the build is ordered: the regeneration instants (inherit Engine 2's), and marked swing-scalp charts as oracle.

---

## §14 THE FILE LAYOUT

| Path | Holds |
|---|---|
| `design/BLUEPRINT_SCALP_ENGINE_v1.md` | this document |
| `e1_tool/e3_scalp.py` | new module: gate, range, candidates, orders, meter, flow, pine fragment |
| `e1_tool/plutus.py` | one switch-guarded call after the swing orders |
| `tools/leak_check_scalp.py` | V1 for the scalp plan |
| `tools/research/devset.py` | ledger columns for the scalp family |
| `evidence/scalp/` | frames and ledgers |

---

## §15 THE RISK REGISTER

| Rank | Risk | Severity | Mitigation |
|---|---|---|---|
| 1 | Engine 2 gate wrong (swing scalps forecast on a breakout day): scalps fade a surge | HIGH | chart-time kill switch G2; P0 precondition |
| 2 | Orders stale between regenerations: the oscillation moved to other zones | HIGH | validity window = one regeneration interval; expiry at `U_k+1` |
| 3 | No 5m data: entries less precise than the canon's stack | MEDIUM | `SCALP_NO_5M` printed; 15m edge |
| 4 | 15m zones too dense: many low-quality candidates | MEDIUM | frame requirement (30m), Refined preference, tokens; never a silent cap |
| 5 | Scalp opposes a running swing | MEDIUM | `SCALP_AGAINST_SWING` |
| 6 | Pine object budget on a 15m chart | LOW | stubs for closed windows |
| 7 | Chart opened on 1H: scalps unreadable | LOW | hidden above 30m with a label |

---

## SUMMARY

The scalping engine is the swing engine one stack lower. Because a Pine script cannot fetch, a scalp exists only as a resting order baked at a fixed regeneration instant and tracked live on the chart's own bars. At each instant a gate opens only while Engine 2's shape in force is swing scalps inside the chain; the range is framed by the standing 30-minute supply and demand inside the day's container; entries sit on 15-minute zone edges, stops behind the next zone, one take-profit at the opposing 30-minute zone, risk-reward at least 3, one trade per oscillation, twenty per pair-week on a separate meter. A close beyond the container cancels resting scalps on the chart itself. Every discarded candidate carries a token, every number a source, and nothing changes the swing orders or Engine 1.
