# G1 count 3: outside reviewer (fresh context, no earlier count read)

Reviewer: an outside agent with fresh context. It did not build the tool and has not read audit/G1_count_dryrun*.md, memory/ or e1_tool code.
Sources: every frame in evidence/s3c/ (36 PNG, each opened and looked at), audit/g1_facts_c/*.txt for exact prices, 1H/15m bars read-only through e1_tool/e1_data.py bars() to check times, closes and fills.

## Counting rules applied (so anyone can recount)

- **Zone verdict (E1).** Every Engine 1 drawing counts: IP zones, the gap in-fill box, S/D candle zones, LSZ boxes and the unlabelled V1 liquidity bands. Amber option-strike lines are levels, not zones, so they are not counted.
  - REACTED: a sharp rejection, or consolidation in or around the zone, with the turn inside the zone or within about 3 pips (DXY 0.03) of its edge. For an LSZ, the turn may be anywhere inside its dotted sweep reach.
  - PIERCED: price crossed the zone and the turn, if any, came beyond that tolerance or beyond the sweep reach.
  - When a zone was touched several times, the verdict follows the dominant touch, and the other touches are noted.
  - Not reached: zones price never touched. They are left out of the ratio.
- **Missing points.** Obvious 1H turning points of the forecast week with no Engine 1 drawing within that tolerance are added to the denominator.
- **E1 %** = reacted / (reached + missing). A zone that is bloated, bunched (several drawings stacked on one price), or floating is listed as a defect. It is not deducted from the ratio, and the "none bloated / bunched / floating / missing" condition is reported separately as MET or FAILED.
- **E2 (day RIGHT / WRONG).** A day is RIGHT when shape, direction and key move match that day's candles. If the tag's shape is not what the candles did (for example BS tagged and a spike plus full reversal happened), or the direction is wrong, the day is WRONG.
- **E3 (obvious trades).**
  - For 2026-07-06 the obvious trades are the operator's trades in golden_week.json, minus any whose entry was only available before Mon 06:00 UTC (checked on 15m bars).
  - For the other weeks they are the clean zone-to-zone 1H moves, listed from the _zones frame and the bars BEFORE the setups were looked at.
  - CAUGHT means a setup in the same direction at the same turn (entry within about 5 pips of the turn, or at the zone the turn came from) that filled and hit TP before SL, per the 15m outcome in the facts file, spot-checked on the bars.
  - Every stopped setup is named as a loss, even if price later reached its TP.

