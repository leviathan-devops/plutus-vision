# 09 — E2 / E3 IMPLEMENTATION PLAN (mine; written 2026-11-25 before coding E2; update as it changes)

Canon digests: `context_management/spec/E2_ALGO.md` (read §2.1-2.5, §3, §4 first-hand), `E3_ALGO.md` (not yet read first-hand).

## E2 — shape chain, computed at the Monday anchor from the frozen E1 map + pre-anchor bars
Inputs available in the Pine at the freeze: `Zone[]` (top, bot, zfp, score, side, name), spot, completed D1 arrays (dO/dH/dL/dC), prior weeks' forecasts (`fcs`).
1. S0 (current shape as of the anchor) — matrix 6.2, ZONE-ANCHORED (canon Rule 1/4: no behavioural constants):
   classify each of the last completed days against the PREVIOUS week's zone map: BS = the day closed beyond a zone it opened on the other side of; WL = it pierced a zone and closed back;
   else range day. S0 = BS/WL if the last completed day was one (RWL if it reversed the prior BS through its origin); R if the day after a BS/WL is a range day; SS if 2+ range days between two holding zones.
2. Walk (max 5 shapes; stop when cumulative confidence < 25%; tiers HIGH .80, MOD-HIGH .65, MODERATE .50, LOW-MOD .35):
   SS: a bounding zone ZFP > 45 -> BS toward it (HIGH); both < 30 -> SS continues (HIGH); otherwise SS, bias to the weaker (higher-ZFP) side (MODERATE).
   BS(dir): T = next zone in dir. ZFP(T) < 20 -> RWL (HIGH); 20-40 -> R (HIGH); > 60 -> PBS (MODERATE; > 80 HIGH); 40-60 -> R (MODERATE).
   R -> SS (MOD-HIGH) | if the next zone in the prior BS direction has ZFP > 45 -> BS second leg (MODERATE). WL -> RWL (MOD-HIGH) else SS. RWL -> SS (HIGH). WLS -> BS (VERY HIGH). PBS -> R/SS (HIGH).
   Conservation of energy: after 2 piercing shapes insert SS for 1-2 days. Alternative chain: same S0, flip the first ZFP-conditioned decision; record the decision zone.
3. Days: SS = 2 days when it opens the chain (Mon-Tue "liquidity accumulates"), every other shape 1 day, the last shape fills the rest; +1 day trading-speed shift applies to the first breakout.
   Session: SS -> London; BS/WL -> second half of New York (after 14:30 NY).
4. Render (R-03: "the chain leads and the shapes follow" — boxes first, then the line): one box per day spanning the expected zone-to-zone range (SS: floor edge .. ceiling edge; BS: failing zone .. target zone edge;
   R: the target zone; WL/RWL: wall .. origin), label "Mon: SS [range] | <key zone> | conf"; then a path line through the day boxes; alternative chain dotted. Two-week window (R-36).
5. Verify in Pinebox by eye: do the candles of each day stay inside that day's box and move in the stated direction? Golden-week operator tags: Mon SS+BS, Tue SS, Wed SS+RWL+BS, Thu ladder short, Fri WL+RWL.
   Golden week realized (DXY): Mon range 100.84-101.14, Tue up to 101.20, Wed spike 101.27 then down (RWL), Thu down to 100.80 / range, Fri flush to 100.60 then recovery (WL at the floor).

## E3 — corrected spec only (R-16), <= 11 setups per week per pair (L-04), drawn as position boxes (R-09): red = SL side, green = entry->TP, entry at their shared edge
- E2 designates, E3 obeys: SS day -> swing scalps at the range's floor and ceiling zone edges; BS day -> one swing entry at the failing zone toward the target zone; RWL/WL -> entry at the wall toward the origin.
- Sniper entry at the zone edge facing price; SL behind the next liquidity shield (zone/LSZ beyond) + 1 pip; ONE TP at the near edge of the opposing zone; RRR floor 3.0 (confidence gate: high only).
- Golden-week oracle trades (3-pip tolerance): see 08_FACTS (L 100.945/100.905/101.115; S 101.14/101.20/100.845; L 100.845/100.77/101.19; S 101.19/101.25/100.975; L 100.975/100.905/101.24; S 101.235/101.33/100.68).
  Note how they map to my E1 map with walls: short 101.14 = wall zone 101.05-101.17; TP 100.68 = floor top 100.67; long 100.845 = teal 100.86-100.92 low edge; TP 101.19/101.24 = just under the ghost zone 101.25.
- Read E3_ALGO.md §phases + constants table before coding; resolve canon conflicts by the corrected doc.
