# CONTEXT INJECTION: ENGINE 2 MICRO-INFRASTRUCTURE OVERHAUL (E1–E2–E3 ARCHITECTURE)

## 1. The Core Bottleneck (Why Macro E2 Tops Out on Out-of-Sample Weeks)
In the baseline three-engine architecture (E1 Zones -> E2 Shape Chain -> E3 Trade Setups), Engine 1 and Engine 2 currently operate at a macro working baseline:
- **Engine 2 drives 60–70% of Engine 3's performance**, while Engine 1 drives the remaining 30–40%. Structurally, **Engine 1 defines where the walls and stop-loss shields live, while Engine 2 defines where price transitions, enters, and takes profit.**
- **The exact failure mode of macro-only E2:** Macro E2 tells you price will travel from 4H Supply to 4H Demand and assigns a macro shape label (`SS`, `BS`, `R`, `WL`, `RWL`, etc.), **but it says nothing about the micro-transition structure when price actually reaches that zone boundary**:
  - Will it pierce through to the bottom of the zone and consolidate upwards?
  - Will it immediately reverse-whiplash off the top edge?
  - Will it wick halfway into the zone and snap back (`RWL`)?
  - Will it fill 40–50% of the zone with a solid candle body and consolidate into a Recovery (`R`)?
  - Or will it slice straight through (`PBS`) and invalidate every counter-trend setup?
- Without predicting the **micro-level transition structure** at each zone boundary, E3 is forced to guess entry depth, reaction timing, and reversal vs. breakout—which produces great results on clean textbook weeks but collapses to ~50% out-of-sample on varied multi-week tests.
- **Core Thesis:** If E1 extracts the full structural + microstructure data cleanly, these boundary transitions are **mappable, traceable, and predictable**—turning Engine 2 from rough macro boxes into a high-precision forward price-time trajectory that makes Engine 3 dramatically more reliable.

---

## 2. The 7 Breakthrough Pillars of the Engine 2 Overhaul

### Pillar A — Hybrid Deadband-Free Macro Shape Classifier
- **Problem to eliminate:** Rigid ZFP bucket thresholds (e.g. deadband gaps between `30–45%` for `SS` and `40–60%` for `BS`) produce `UNCLASSIFIED` voids that kill entire weeks and zero out downstream E3 setups.
- **First-principles solution:** Replace brittle threshold gaps with a **continuous hybrid classifier** that fuses E1 structural strength/ZFP with strictly causal bar geometry:
  - Efficiency Ratio (`ER`), swing retrace/extension bands (`SS` low-ER compression, `BS` high-ER expansion, `R`/`RS` 44–78% recovery, `RWL` 63–90% sharp reversal, `WL` 80–112% full sweep, `PWL` >= 2.382x piercing extension, `WLS` >= 3 alternating sweeps),
  - `1-2-3` touch exhaustion tracking,
  - `2`-pierce `energyRecoveryLock` (forcing energy recovery / consolidation after consecutive zone pierces).
- Preserve structural integrity: every day's shape must anchor to real E1 zone IDs (never fabricated price levels).

### Pillar B — The 5-State Exhaustive Micro-Transition State Machine (Core Pendulum Swing)
Every time the E2 forward trajectory reaches an E1 zone boundary, classify the boundary interaction into one of **5 mutually exclusive, collectively exhaustive micro-transition states** (zero unclassified fallthroughs). Each transition is driven strictly by measurable E1 + microstructure inputs (`ZFP`, Liquidity Matrix `defendedEdge` vs. outer `reactionExtreme`, `$850M+` FX Option Strike walls, MA confluence grid, Volume Profile HVN/LVN, CVD/Delta absorption, and DXY alignment):

1. **`WICK_RWL` (Immediate Wick Sweep & Reverse Whiplash)**
   - **Physics:** Low `ZFP (< 20%)` + `$850M+` Option Strike Wall or strong Liquidity `defendedEdge` + strong counter-Delta absorption.
   - **Price behavior:** Single-bar wick sweep tagging the defended edge followed by `<= 3`-bar reclaim back out of the zone.
   - **E3 implication:** Sniper limit entry at/near `defendedEdge`; tight stop behind liquidity shield.

2. **`BODY_WL` (Mid-Zone Body Fill & Engulfing Whiplash)**
   - **Physics:** Moderate-low `ZFP (15–30%)` + unmitigated `BoM` Order Block + stacked MA confluence + aligned DXY bias.
   - **Price behavior:** Candle body fills ~40–50% into the zone, absorbs resting orders, then snaps out via an engulfing reversal.
   - **E3 implication:** Do not front-run the outer rim—anchor entry deeper at the OB/MA midpoint to avoid premature stop-outs.

3. **`BODY_CONSOL_R` (Mid-Zone Consolidation into Recovery)**
   - **Physics:** `ZFP 20–40%` + High Volume Node (`HVN`) inside the zone + balanced Delta (neither side absorbing decisively).
   - **Price behavior:** Price enters the zone and prints `>= 3` short-wick consolidation bars (`SHORT_WICK_CONSOL`) absorbing liquidity before rotating into Recovery (`R`).
   - **E3 implication:** Expect time delay before departure; wait for consolidation build/retest rather than chasing bar 1.

4. **`PIERCE_R` (Outer Rim Pierce & Stop-Pool Reclaim)**
   - **Physics:** Low Volume Node (`LVN`) vacuum at the zone rim + exposed liquidity stop pool sitting just behind the edge.
   - **Price behavior:** Price slices cleanly past the front edge through the vacuum, sweeps the stop pool at the outer `reactionExtreme`, then reclaims back inside for Recovery.
   - **E3 implication:** Front-edge entries get stopped out—stop-loss MUST sit behind the outer `reactionExtreme` (or enter on the post-sweep reclaim).

5. **`CLEAN_BREAK_PBS` (Full-Body Breakout Surge — Reversal Blocked)**
   - **Physics:** High `ZFP (> 55%)` OR Option Cut / macro release + strong directional `CVD` + `LVN` vacuum ahead of the zone.
   - **Price behavior:** Full-body candle close cleanly through the zone with follow-through (`PBS` / `BS`).
   - **E3 implication:** Hard-block counter-trend reversal setups at this zone; flip to continuation / breakout-retest logic.

### Pillar C — 3-Week Rolling Structural Context Window (`W-2, W-1 -> W0`)
- **Problem to eliminate:** Forecasting Monday `W0` from a cold start throws away ~60% of the actual structural signal.
- **First-principles solution:** Engine 2 is a **continuous multi-week storyline**, not an isolated Monday reset:
  - Map the **two prior completed trading weeks (`W-2` and `W-1`)** directly onto the historical candles already visible on the chart (realized E1 zones + realized E2 shape boxes + realized transitions).
  - Extract the **Friday close terminal state** from `W-1`: active shape in progress, exhaustion / touch count, `energyRecoveryLock` state, and mitigated vs. unmitigated zone freshness ledger.
  - Continue the shape chain **causally** from that exact `W-1` terminal state into the upcoming week `W0` (pre-Monday-open cutoff).

### Pillar D — Forward Line-Chart Trajectory Polyline Inside Hollow White Macro Frames
- **Visual & functional contract:** Think of converting the chart from candles to a **line chart** and projecting the exact path price will trace across the trading week:
  - Draw a continuous **`2px` solid Blacksmith Orange (`#E85D04`)** forward polyline (`PathNode[]` waypoints) starting from the current/cutoff candle and tracing every predicted Mon -> Tue -> Wed -> Thu -> Fri swing pivot, boundary transition, and continuation leg inside hollow white macro shape boxes.
  - **Strict line grammar:** Zero dashed lines and zero dotted lines anywhere on the chart (solid lines only).
  - **Direct backtest visual oracle:** When you rewind Backtest replay to Monday `00:00 UTC` (with all Mon–Fri candles hidden), the full sealed pre-Monday forecast (E1 zones + E2 orange path + E3 setups) is visible. When you press Play through Friday close, the real candles should physically track along the projected E2 path and trigger the E3 boxes anchored on its vertices.

### Pillar E — Precision Target Envelope (`±1–3p` Price & Dual Timing Physics)
- **Price Precision (`±1–3 pips` margin of error):**
  - Never interpolate arbitrary midpoints, synthetic sine/wave templates, or fixed pip clamps (e.g. `±36p` caps that break on 100–200p trend weeks).
  - Quantize every E2 vertex strictly onto real structural intersections: `OB/S&D ∩ 15m/30m/1H Liquidity defendedEdge ∩ FX Option Wall / VPOC ∩ MA confluence`.
- **Dual Timing Regime (Pre-Week vs. Live Trigger):**
  1. **`CLOCK_ANCHORED` (`±5m` precision):** Pivots aligned to deterministic institutional events—London Open (`08:00 UTC`), NY Open (`08:30 UTC`), NY Option Cut (`10:00 NY`), ECB Fix (`13:15 UTC`), London Fix (`16:00 London`).
  2. **`UNSCHEDULED` Pre-Week Pivots (`±30m` candle granularity):** Pre-week forecasts should resolve to the 30-minute candle window (e.g. `10:00`, `10:30`, or `11:00 UTC`). Once live price enters the target zone intraday, timing upgrades to **`PRICE_TRIGGERED_LIVE_5M_LOCK`** based on the live micro-transition trigger.
- Every `PathNode` waypoint should carry explicit metadata: `{ time, price, anchor_zone_id, transition_type, timing_mode, window_tol_min, price_tol_pips, transition_evidence }`.

### Pillar F — `$0` Free Microstructure Expansion (`9L6D -> 9L6D+`)
To power the 5-state `MicroTransition` engine without spending a single dollar (paid APIs like Databento are strictly forbidden), expand the original 9-pillar data foundation with **three `$0` microstructure pillars**:
- **`P10` — Futures Volume Profile (`VPOC`, `HVN`, `LVN`) & Cumulative Volume Delta (`CVD`):** Spot FX lacks a centralized order book/DOM; solve this at `$0` by pulling CME currency futures proxies (**`6E`** for EURUSD, **`6B`** for GBPUSD, **`DX`** for DXY) basis-adjusted to spot (via free TradingView / MT5 tick feeds) to distinguish HVN absorption zones from LVN sweep vacuums and confirm counter-delta absorption vs. breakout momentum.
- **`P11` — Deterministic Institutional Clocks & Option Cut Windows:** Hard-wired session opens, option-cut release windows, and fixing clocks driving `CLOCK_ANCHORED` pivots.
- **`P12` — Sovereign 2Y Yield Differentials & Positioning:** `US02Y–DE02Y` (EURUSD), `US02Y–GB02Y` (GBPUSD), and weekly CFTC COT positioning from free public feeds (Fed H.10 / CFTC / TradingView) to reinforce directional conviction and prevent fighting macro trend weeks.

### Pillar G — Parallel Multi-Pair Fan-Out (`DXY -> [EURUSD || GBPUSD]`)
- **Problem to eliminate:** Running sequential `DXY -> EURUSD -> GBPUSD` (or mirroring EURUSD levels onto GBPUSD) breaks down because GBPUSD zones frequently sit 40–50 pips displaced from EURUSD with distinct volatility and heavy **67–80% Front Liquidity Shield** front-running behavior.
- **First-principles solution (Two-Stage Parallel Triangle):**
  - **Stage A (`DXY` Master):** Computes DXY's E1 + 3-week E2 chain and emits a **coordinate-free DXY Compass** (directional bias, 3-week shape chain, key institutional turn clocks — **zero EURUSD/GBPUSD prices**).
  - **Stage B (Isolated Parallel Workers `EURUSD || GBPUSD`):** EURUSD and GBPUSD run concurrently and independently, each combining the coordinate-free DXY Compass (inverse correlation) with **its own native E1 zones, option strikes, futures VP/CVD, and pair-specific liquidity behavior** (EURUSD `S/D ∩ LMV` overlap vs. GBPUSD Front Liquidity Shield).

---

## 3. Non-Negotiable Mathematical, Causal & Verification Invariants
1. **Strict Zero-Lookahead Causality (`bar.time < cutoff`):**
   - Every calculation for `W0` (including `W-2`/`W-1` extraction, `P10–P12`, E2 transitions, and E3 anchoring) MUST strictly exclude every bar with `bar.time >= Monday 00:00 UTC` (remember candle timestamps are open times, so `bar.time == cutoff` covers `[00:00, 01:00)` and is post-cutoff!).
   - **Mandatory Kill Test:** Inject a `+500 pip` shock into every bar `>= cutoff` across DXY, EURUSD, and GBPUSD and assert a **0-byte diff** across the entire pre-Monday forecast (E1, E2, E3, and rendered Pine output).
2. **Honest Time-Aligned Out-of-Sample Grading (No Cheats):**
   - Grade E2 trajectories strictly on **time-aligned price error** (comparing predicted path vs. actual candles inside tight `±2h` windows, plus hourly Pearson correlation `r` and true weekly net direction sign)—never time-agnostic "did price touch this level anywhere during the week?" cheats.
   - Grade E3 setups bar-by-bar with **conservative SL-before-TP tie-breaking** whenever a single bar touches both SL and TP.
   - Verify E2/E3 alignment: **zero direction conflicts** between an E3 setup and the E2 leg it is anchored on, and every E3 entry/TP window stays cleanly inside `W0` (`Mon -> Fri`).
3. **Live Chart Replay Verification:**
   - Do not optimize blindly in backend numbers alone—compile and inspect the actual rendered chart (Monday-open sealed forecast overlaid with replayed Mon–Fri real candles) across DXY, EURUSD, and GBPUSD on both anchor weeks and blind out-of-sample weeks.
