# LEARNING LOG — 2026-10-11 (foundation phase; no indicator work done)

Graph form of everything below: `python3 context_management/graph/resume.py`. Sources: `canon/Toolset/` (read in full:
Fractal Architecture v2.3, original 5.3.3 prompt 4216 lines, CORRECTED E3 1685 lines, engine3_v8.py (first half), repo handover docs + failure/theatre logs).

## 1. My synthesis of the dynamics (own words; the canon's claims reduced to one mechanism)

**One mechanism: resting orders are fuel, and every structure is a bookkeeping device for how much fuel is left.**

- **Earth (liquidity)** = stops and resting orders clustered at swing extremes, round numbers, option strikes. IP zones are where *many independent reasons* stack (pivots, MAs, structure, psychology, options hedging, analysts). Pressure degree is simply the count/weight of independent reasons for orders to be there.
- **Fire (S/D)** = where institutions hold inventory they must defend or unwind. BoM = where the inventory was *built* (origin of a leg); MoM = a pause midway (less inventory). A move needs both: inventory to push (Fire) and orders to trade against (Earth).
- **Zone life cycle is a fuel gauge**: each touch consumes resting orders. Virgin -> 1st touch (~80%) -> 2nd (~50%) -> 3rd = depleted/fails. This is why MoM is "one-and-done", why a depleted zone below price is a *target*, not support, and why a pressure zone with juice between price and a deeper BoM gets liquidated first.
- **Water (shapes)** is what the fuel consumption looks like through time: SS = both sides slowly re-accumulating stops (swing scalps harvest it); BS = one side's liquidity pool is big and its bounding zone weak (ZFP up) so price drives to the opposite pool; at a *hard wall* (ZFP<20) the surge is absorbed -> WL/RWL (reversal), at a mid zone (20-40) -> R; at a weak zone (>60) -> PBS. ZFP-conditioning is "wall strength vs momentum".
- **Conservation of energy**: after 2 strong piercing moves the extremes' liquidity is spent -> 1-2 days of R/SS while it rebuilds; "today's move is tomorrow's" (price runs ~30-50% of expected speed -> +1 day).
- **Air (Fib)** is a coordinate system that crowds also use; anchored to real swings it is self-fulfilling and re-seeds liquidity (Earth). Wormholes (0.382->1.382, 0.618->1.618) give the entry->TP geometry; rockets sit at 1.382-1.786 (entry) with trip-wire triggers at 2.382-2.786.
- **Option cage/spring (10:00/10:01 NY)** is a *scheduled* liquidity event (hedging pins price, expiry releases it). This is E1 information that is not in OHLC.
- **E3** = geometry on top of E2's designation: sniper edge entry, SL behind a liquidity *shield*, ONE TP at opposing pressure, reinforcements via stop-limit trip-wires so adds only exist once the parent is in profit (same bet at later points of the wave; wrong analysis => only the parent loses).

## 2. Environment facts found (and handled)
- No live TradingView session exists for this container (`rig/RIG_STATUS.md`), and egress is allowlisted: GitHub/PyPI/npm reachable; Yahoo/Stooq/Dukascopy/TradingView/etc. return 403. Workarounds used: PyPI `backtesting` (real EURUSD 1H, 5000 bars) + repo fixture (real TradingView Jul-2026 DXY/EU/GU pre-anchor). **No data was synthesized.**
- The repo's Pine IDE rig runs headless here: `npm install` in `pine-ide/pine-station`; start station :9741, vil-rail :9754, `scripts/pv-server.py` :9851; headless Chromium (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless=new --no-sandbox --remote-debugging-port=9222 http://127.0.0.1:9851/pine.html`); `bun scripts/pv-load.mjs plutus-vision-v0.pine EUR/USD 1H`; screenshot via CDP `Page.captureScreenshot`; drawings as JSON via `POST :9741/run {script,pair,timeframe,limit}`.
- `trident_v8.pine` is not in the repo or upload (station path `/home/user/Original_Canon_Data/Pine Scripts/trident_v8.pine`: absent). `plutus-vision-v0.pine` = LuxAlgo 4-script bundle (geometry only).

## 3. Exercises (all from bars <= Monday 02:00 ET anchor; outcomes only for scoring)
| # | Exercise | Result |
|---|---|---|
| X1 | Raw visual read, wk 2017-06-12 (EURUSD 4H) | Big impulse -> multi-week range -> Mon/Tue SS pocket -> Wed spike through range high into massive rejection (WL) -> RWL/BS down to floor (virgin MoM demand 1.1110-1.1149 held, low 1.1132) -> Fri recovery. = SS -> WL -> RWL -> R. My mechanical E1 had the 1.1270-1.1300 EXTREME/MoM-supply ceiling exactly where the spike printed. |
| X2 | Mechanical E1 + chart overlays, 4 weeks | Zones render plausibly; pivot-only clusters clutter (doctrine AD6 says require structural anchor). |
| X3 | Doctrine-v0 forecaster, 12 blind weeks (seed 11; not tuned) | Day-shape family 55% vs 65% always-range; direction 3/21. **Negative result.** Causes: nearest-zone ranges collapse to 0.1-0.4 ADR; zone state (depleted/virgin) not in ZFP; weak side selection. |
| X4 | Canon claims vs data (EURUSD 2017-18) | MoM decay 62%->38%->32% (supports one-and-done/3rd-touch). BoM 100% not reproduced (58%, n=12; definition unresolved). Shape transitions (n=195) qualitatively match E2 table. After 2 same-direction directional days next day = range 6/10. NY-swing timing claim NOT supported at day level (London 48% of impulse starts vs 6% for 12-17 ET). |
| X5 | E1 edge vs shifted baselines | **No edge** (lift 0.96-1.07x; touch react 43% vs 44.7%). Interpretation: my OHLC-only reconstruction lacks the options/analyst/intra-zone data; says nothing about the live canon. |
| X6 | Real Jul-2026 EU week (pre-anchor chart + golden prints) | Golden levels sit inside my 55-pip cluster; they rank 86th-97th percentile in 10-day wick-tip density => operator "internal LQZ rungs" ~ dense touch clusters (Pine-computable). |
| X7 | Repo indicator on same data | 122 boxes/24 labels/57 lines; no live box covers any golden EU level (nearest 5.6-20 pips away); no E2/E3 drawings. |

## 4. What this means for the (not yet started) indicator job
1. E1 half computable per-bar from OHLC: S/D origin candles (+BoM/MoM, touch counter), swing/LSZ, pivots, MAs, round numbers, **touch-density rungs**. Option-strike + analyst dimensions need an input channel or are absent -> decide with operator.
2. E2 per-bar needs (a) classification of *completed* days into shapes to know the current shape, (b) zone-state-aware ZFP, (c) bounding-zone selection by structural weight, not proximity.
3. Acceptance harness must be the F-17 mechanism: expectation written first -> look -> claim/verdict/delta ledger, on 12 blind weeks Mon London open -> Fri close. Needs DXY/EU/GU/AU history (network allowlist) or operator-supplied files.
4. Open definitions needed from operator: BoM detector, "reaction", "NY swing". (graph: OQ_*)

## 4b. Canon contradictions found while reading (graph: `--type canon_conflict`; operator must rule before E3 is implemented)
Reinforcement-inside-SL rule is inverted between original and corrected spec · 1-2-3 retest counting is off-by-one between 8.4.2 and 8.25 · v8.py TP1/TP1.5/TP2 vs corrected ONE-TP · ">=24 setups/week" quota vs "honest absence" refusal · setup caps · NY-session timing claim.
Also: `trident_engine3_v8.py` consumes PRE-BUILT E1/E2 data (confirms R3 law); the validator/template are the upstream *report* pipeline, whose Pine output was a static per-week render.

## 5. Reproduce
```
pip install backtesting pandas numpy matplotlib semantica
cd research/e12_lab   # lab.py e1.py e2.py render.py weeks12.json ; see graph node A_LAB
python3 context_management/graph/build_graph.py   # rebuild graphs
```
