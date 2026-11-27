# Response to the outside G2 audit, round 2 (audit/G2_audit2.md, baseline 9cdfbc0)

Written 2026-11-27. States: FIXED (commit) / ANSWERED (the canon line, ruling or oracle pixel that settles it) / PART (what is built, what is left) / OPEN.
Rule (goal prompt section 7, G2): each finding is a bug - fix it, or answer it with the line that refutes it. Pixels outrank the auditor. This file is the S1 / S4 work list; a later outside audit re-checks it.

## New findings N-01 .. N-33
| id | state | note |
|---|---|---|
| N-01 | ANSWERED | The outward 'reach' is the same paragraph's third and fourth sentences: P533:1286 "Institutions often sweep 0.05-0.10 beyond the visible extreme before reversing. Record as 'LSZ Extended: ... - sweep scan 0.05-0.10 DXY beyond swing [high/low]'". The first sentence (the zone widened inward) is what Engine 1 draws as the LSZ box. Pixels: DXY 2026-10-05 Tuesday low 101.754 against extreme - 0.10 = 101.755; DXY 2026-05-18 Thursday high 99.515 against 99.509 (ledger 86, frames evidence/s3f). |
| N-02 | FIXED (D-96) | buffer back to Rule 2.5's 3 pips; the '97.87 - 0.01' proof and 'E3C:304' citations removed. OPEN part: Rule 2.5 / Rule 3 are P533 Part VII lines (E3 text superseded by R-16); E3C's own line for the rule is E3C:1027 'LSZ Zones (with bottom edge extension) | Phase 4 | SL ladder-steps model'. |
| N-03 | FIXED (D-96) | the floor is tested on the emitted order (buffered TP). |
| N-04 | ANSWERED / PART | R-07 "65 the inclusion gate? Yes, 100%. I don't want anything that is less than high confidence" + E3C:1011 'confidence >= 65 required for inclusion': 65 is the gate he set. His own golden DXY trades #3 (Tue long 100.845) and #5 (Wed long 100.975) score 75 and 78 in this scorer (no VLM base, no VLM bonus): an 80 gate deletes them. Left: the class NAME of 65-79 is still 'STANDARD' (E3C 5.2 table). |
| N-05 | FIXED (D-96) | per-day repeats count toward the 11. |
| N-06 | PART | WL: the one swing of a whiplash step is the reversal entry after the spike (GS:39 'WL | ... | Reversal entry after spike'), emitted as the RWL setup of the same session. R: its 2-4 swing scalps + recovery surge are not built. |
| N-07 | FIXED (D-96) | +10 only on the mirror of a source setup of the same chain step and day (DXY -> EUR/USD inverse, EUR/USD active mirrors -> GBP/USD kept). |
| N-08 | OPEN | the first-rocket band (D-83) was derived from his three rockets and his own grids; E3C:227 / 689 name 1.382-1.786 as the rocket entry zone with a 2.382-2.786 trip-wire. To rebuild from E3C 8R.7 alone. |
| N-09 | ANSWERED with N-04 | every included setup is at or above his inclusion gate; rockets copy the parent's confidence (not scored on their own: OPEN). |
| N-10 | OPEN | transition entry at an IP-zone edge; no Late-consolidation test. |
| N-11 | OPEN | two timeframes up allowed for every source. |
| N-12 | OPEN | 4H MoM target -> R instead of minor WL then BS / PBS through it (P533:1963). |
| N-13 | OPEN | BoM candle-zone target -> RWL without the 6-check; WL upgrade at an unswept sweep level has no canon sentence. |
| N-14 | OPEN | P452:2082 as the basis of D-49 / D-50 / D-74. |
| N-15 | PART | threshold now USD 1.5bn (P533:690); the +1-day reading of the Spring Release as the week's transition day stays D-60 (no canon sentence names the day): OPEN. |
| N-16 | OPEN | 6-check items 5 and 6. |
| N-17 | OPEN | Late consolidation by elapsed sessions. |
| N-18 | FIXED (D-96) | a swing-scalp order rests only on days whose E2 path comes within 30 pips of its entry. |
| N-19 | ANSWERED | his golden GBPUSD #5 (Thursday short 1.34246 / 1.3436 / 1.33882) stands on the bottom edge of the 4H BoM supply 1.34272-1.34347 he drew himself (golden_week.json); the tool's GB6 is that trade. Left: swing scalps at inner 4H zones enter at the edge when no rung / block is inside (OPEN). |
| N-20 | FIXED (D-96) | F1-A lift on a supply-zone short. |
| N-21 | OPEN | TP buffer on every target (the PDF states it for scalp wormhole TPs). |
| N-22 | OPEN | JOIN_TP (D-91) rests on L-39 (a drawing ruling) and an undefined label. |
| N-23 | OPEN | pivot = V1 4H band within 0.30. |
| N-24 | PART | the window now also runs to each bound's measured-move target (D-93); zones beyond stay behind show_far. |
| N-25 | OPEN | Phase 2 confluence >= 7 selection; Hard Wall SL anchor. |
| N-26 | ANSWERED | E3C:1011 itself: 'total max unlimited (NO CAPS - operator D38)'; E3C:461-466 D10 / D16 / D38 verbatims; the weekly limit is L-04 / R-07. |
| N-27 | FIXED (D-96) | no breakout entry at a 4H MoM zone. |
| N-28 | OPEN | direction of the PIERCED branch. |
| N-29 | OPEN | BoM bound with 3+ reactions run through the counter. |
| N-30 | OPEN | uncited constants (list in the audit). |
| N-31 | ANSWERED / PART | his real DXY trade of 2026-04-20 (long 98.02) filled on Monday, the day before the breakout day; his golden GBPUSD #5 filled Thursday, the day the breakout reached its target: the order rests from the start of the step that leads to it (E3C:625 pending orders placed ahead). No E3C sentence states it for primaries: PART. |
| N-32 | FIXED (D-96) | reinforcements are not counted among the 11. |
| N-33 | PART | alignment bonus fixed; storyline counter-trend now -5 (E3C:245); no-IP base 70 and the prior-week momentum definition OPEN. |

## Earlier findings (A-xx, B-xx, C-xx): the audit's Section 1 is the current list. Changed since the baseline:
| id | state | note |
|---|---|---|
| A-16 | PART | pressure-zone anchors with 3 reactions are gated (ZONE_DEPLETED); battle-time test still outside the tool. |
| A-20 | PART | layer 7 scores +5 / -5; layers 1, 2, 4, 5, 6 OPEN. |
| A-21 | see N-04 | |
| A-36 | PART | D-95: DAY / SESSION / SHAPE TRIGGER / CATEGORY / anchor hit window (= the session bracket) in the report. |
| A-37 | PART | mirror keys per chain step (N-07) and the 10.7 divergence flag; per-setup re-anchoring lane OPEN. |
| A-44 | PART | f(T) line reported met / NOT met (D-95). |
| E1-X | PART | Part X read; info table D-94. |
