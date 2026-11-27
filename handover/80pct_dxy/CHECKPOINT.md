# Checkpoint "80% functional — DXY specific" (operator M-60, 2026-11-27)

Code state: branch AGENT, commit aa8d689 (this file is committed on top of it; no code change).
Operator's verdict on the frames of this state: DXY golden week — first half (Mon–Tue) accurate, the trades hit entry and take-profit; the E2 shape chain of the second half (Wed–Fri) is broken; GBPUSD poor; EURUSD not shown.

What this state contains (decision rows in memory/03_DECISION_CHAIN.md):
- D-131 / D-134: daily anchoring by default; one unique order per move (no per-day copies; a pending order keeps resting).
- D-132: a 1H close beyond a Decision Zone activates the alternative chain at the next trading-day open (6.6 Step 4).
- D-135: stops per L-50 (reversal entries 1 pip inside the next shielding zone, no 9.5-pip veto, RRR floor decides, deeper-only fallback; EUR/USD keeps the outside stop).
- D-136 / D-137 / D-138: London-open zone update (zones formed since the week anchor drawn from the London open that found them); after a chain fails, the line and day boxes follow a chain re-anchored on the rebuilt map; orders stay with the chain in force.
- L-51 (first version): range days drawn session by session (Asia flat, London to the nearer bound, NY pre-cut pinned at the day's largest strike, NY post-cut to the other bound).
- Protocols D / E / G harvested (Treasury auctions, NY Fed ON RRP, EIA); Protocol F (calendar) NO DATA.

Frames of this state: evidence/lib4/DXY_2026-07-06_week.png, evidence/lib4/GBPUSD_2026-04-13_week.png.
Run: `python3 e1_tool/plutus.py MONDAY PAIR [out.pine]` (daily anchoring default; `--weekly` = all orders at the Monday anchor).
Restore this exact state: `git checkout aa8d689`.
