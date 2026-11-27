# Why EURUSD was a C on the golden week (V1 / V2), and what V3 changes

Your EURUSD trades (golden week Jul 6-10) run as one chain: each entry sits at the previous trade's TP.
#1 TP 1.14103 -> #2 entry 1.14106 -> TP 1.14442 -> #3 entry 1.14441 -> TP 1.14004 -> #4 entry 1.14012 -> TP 1.14276 -> #5 entry 1.14277 -> TP 1.13950 -> #6 entry 1.13953 -> ...
DXY and GBPUSD follow the same pattern.

## What was wrong on EURUSD and not on the other two pairs

1. **A second short for the same move, entered too early (stopped out).**
   - Monday had two shorts at the ceiling:
     - 1.14385, at the 1H supply 1.14375-1.14421;
     - 1.14442, at the pressure zone directly above it (1.1444-1.1453), which is your #3.
   - EURUSD pierced the 1H supply and turned at the pressure zone. The 18:45 UTC spike to 1.14454 stopped the 1.14385 short by 0.3 pips and filled 1.14442.
   - When price reached 1.14385, your Monday long (#2, 1.14106) was still running to its TP at 1.14442. The 1.14385 short traded against the move in progress, 4.4 pips before that TP.
   - My Engine 3 used Law 27 ("TP of trade N = entry of trade N+1", E3C 6.2 / 8.21) only to link trades. It never refused an order that sits inside the move of an open trade.
   - DXY did not show this defect: its Monday turned at the 1H supply (101.14, your #2) before reaching the pressure zone, so the second short there (101.203) never filled.

2. **A Tuesday re-entry that DXY did not have (stopped out).**
   - The Monday long 1.14095 was re-armed on Tuesday after it hit TP, and Wednesday's RWL retest stopped it.
   - The DXY source had dropped its own Tuesday copy (still open). EURUSD mirrored DXY only at the Monday anchor, not DXY's daily-confirmed orders (E3C Phase 10 cascade). So it re-armed the level on its own.

3. **Clutter.**
   - Four Monday position boxes plus the Tuesday re-entry.
   - In V1, four dormant alternative-chain boxes as well. V2 removed those on all pairs.
   - Overlapping labels on Wednesday.

Your #1 (Mon short 1.14322) traded only in the Asian session, before the Monday London-open anchor. Price never came back to 1.14322 after 06:00 UTC before its TP at 10:00. The map cannot carry it.

## V3 changes (no price or week constants)

- **D-142, E3C Phase 10** ("For each DXY source setup, generate the corresponding EU mirror setup ... for each EU mirror setup, the corresponding GU mirror setup"):
  - each pair mirrors its source pair's daily-confirmed orders;
  - a re-entry on EURUSD / GBPUSD needs the source pair's matching order on that day.
- **D-144, Law 27** (E3C 6.2 / 8.21; your M-61 "the long ... that hit take profit, that should literally be the entry of the short"):
  - the check runs on the day's drawn Engine 2 line;
  - an order is not placed when the line reaches it while an opposite order is running to its TP, inside that move by more than the 3-pip Law-27 tolerance.

## Golden week after V3

**EURUSD:**
- Orders: your #2, #3, #4, #5, #6, #7 (rocket) and #8, plus one Monday long that never fills (1.14018).
- Both stop-outs are gone.

**DXY:** unchanged.

**GBPUSD:** only the never-filled Tuesday duplicate long is gone. GB1 / GB2 / GB3 / GB4 = your #2 / #1 / #3 / #5.
