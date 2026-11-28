# 20 - BLUEPRINT: SCALPING ENGINE (Engine 3, phase 2) - minted 2026-11-28 on the operator's offer (M-73 / L-68). NOT BUILT. Lower priority than Engine 2. Build only on his order.

## What it is (his words, M-73)
'On swing scalps, you should be shifting down to the 30-minute or the 15-minute time frame and catching all of the moves between the ceiling and the floor zone ... the exact same mechanics as the higher time frame swings ...
executed on lower time frames at the speed of a scalping engine.' 'There's a 30-minute supply and a 30-minute demand, and the price is oscillating between the ceiling and floor ... the whole trading day. There's 8 solid
trades ... 3 to 5 risk-reward ratio.' '6 to 10 trades in a single day just on the 30-minute time frame.' 'It needs to respect the shape chain transition ... swing scalps don't happen in a vacuum.'
Master pattern: swing scalps -> breakout surge -> recovery -> whiplash -> repeat (recovery can itself be swing scalps).

## Canon it is built from (read in full before coding)
- P533:544-564 Timeframe Stacks: Scalp Stack = 30m storyline -> 15m trading timeframe -> 5m refinement ONLY; 'All LTF trade setups are anchored on the 15m'; 'A Breakout Surge on the Swing Stack is mechanically identical to a
  Swing Scalp on the Scalp Stack ... only the pip scale and SL threshold differ'.
- P533:2077-2083 setup universe per shape: SS -> 'Swing Scalps (both directions) | Scalp Stack | 4-8 swing scalps'; R -> 2-4 swing scalps; SS->BS transition -> 1 transition entry + reinforcements.
- P533:1952-1953 consolidation phase: early / mid consolidation -> swing scalps on the Scalp Stack. P533:698-704 London = scalp session ('Catch 10-20 pip swing scalps on the 15m during London'; GU 3-4x the opportunities of EU).
- Trading Laws PDF (scalp stops: '1.5-2.5 pips inside the next 5m liquidity zone'); FA 10 pair profiles (GBP/USD 'Swing Scalp friendly', liquidity outside the zone; EUR/USD inside); GS laws 1-7; E3C phases 0-12 (same phases, Scalp Stack parameters).
- Oracle: WINNING_TRADE_LIBARARY 'Swing Scalps' folder (context_management/oracle/library/trades.json) + screenshots he offered from his latest week (2 swing-scalp days, 16 untaken trades) - ask for them when the build starts.

## Structure (same mechanics as the swing engine, one stack lower)
1. GATE = Engine 2: active only while the shape in force is swing scalps (or a recovery in swing-scalp form), inside the chain (after BS / after WL / before BS). A 30m close beyond the container's ceiling / floor
   (the Decision Zone) ends it: transition entry, hand back to the swing engine.
2. CONTAINER = the day's ceiling and floor zones from Engine 2 (4H / 1H level). INSIDE it, on the 30m: the standing 30m supply = scalp ceiling, the standing 30m demand = scalp floor (Engine 1 already maps 30m and 15m
   supply / demand, BoM / MoM, mitigation, 'Refined', nested_in).
3. SETUPS on the 15m (trading timeframe): entry at the 15m zone / liquidity rung at the 30m zone's edge, stop behind the next zone (scalp stop rule), ONE TP at the opposite 30m zone; RRR 3-5; both directions; one trade per
   oscillation (L-52), next entry = the previous TP zone (Law 27 flow).
4. ZONE USE: BoM unmitigated reacts; each reaction counted (3+ = depleted -> stop fading that side: breakout watch); MoM = ladder step / TP only.
5. DRAWING: position boxes like the swing trades (D-146), a distinct tag ('scalp').

## Dependencies / open points (decide when the build is ordered)
- Needs Engine 2's intraday line (plan memory/19): which zones are the 30m ceiling / floor today and whether swing scalps are still in force. Engine 2 first.
- Bar store has 15m and 30m; 5m is NOT in the store (refinement only, per canon) - 15m edges until 5m data exists.
- CLAUDE.md hard constraint '<= 11 trade setups per week per pair' (R-07): 6-10 scalps a DAY exceeds it -> needs his ruling whether scalps are counted apart from the 11 swing setups.
- Intraday orders need intraday updates of orders (today orders update once a day) - ties to the stability rule of L-67.
