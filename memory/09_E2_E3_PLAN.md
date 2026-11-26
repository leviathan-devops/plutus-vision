# 09 — E2 / E3 REBUILD PLAN after the G2 audit (2026-11-26, model opus-5-5). Supersedes the 2026-11-25 plan. Every rule below cites its canon line; D-rows in memory/03.

## Why (audit/G2_audit_engines.md)
B-08 / B-03 / B-04 / B-05 / C-07: Engine 2 was a FIXED WEEK TEMPLATE (SS x n -> SS+RWL+BS -> BS -> X) = anti-pattern A2. Engine 3 built ONE trade per E2 leg (B-18) instead of Phase 2's
"for each (WorkingDay, zone) pair ... generate a trade candidate", and most E3 phases had no code (A-15..A-47).

## ENGINE 2 (e2_chain.py) = a day map produced by the canon chain, not a template
- Sessions (P533 2.2.1): Tokyo 17:00-02:00 ET, London 02:00-12:00 ET, NY 12:00-17:00 ET. Week after the anchor = Mon LON, Mon NY, then TKY/LON/NY Tue..Fri (14 sessions).
  BS starts in NY 2nd half (P533 2.2.1 "95% of NY swings don't start until after 2:30 PM ET"; FA 10 "DXY ... breakout doesn't start until 3pm").
- Step 1 current shape on 1H (B-01): 1H bars of the last 6 pre-anchor sessions vs ALL MODERATE+ IP zones; matrix 6.2 rows IN ORDER WITH their ZFP conditions (B-02):
  1 BS (1H close through a zone ZFP > 45, price still beyond; PBS if >= 2 zones) / 2 WL (zone ZFP < 20 pierced by a wick, 1H close back; sweep target) / 3 R (after BS/WL, stabilises at zone ZFP 20-40, < 1 session)
  / 4 WLS (3+ IP zones within 0.30-0.50 of each other around spot, >= 3 crossings in 2-5 sessions) / 5 SS (between ceiling and floor both ZFP < 30, > 1 session) / 6 RWL (after BS, reversal through the origin).
  No row -> SS MODERATE with the audit note "no matrix row matched" (D-row). FA 9: two piercing sessions -> SS 'post-energy' 1-2 days. State the anchoring zone + its ZFP (A-12).
- Bounds (6.5): IP zones ZFP < 30 + confluence >= 6 within the SS reach; else the standing 1H / 4H S/D zone (an E1 zone, R-04) WITHOUT an invented ZFP: its behaviour comes from its class
  (BoM unmitigated always reacts; MoM -> 6.4.2 by reaction count) (C-01, B-11); else the unswept sweep zone (P452 "brief breach then reversal"). Each bound: source, class BoM/MoM, reactions, ZFP (IP only).
  IP zones carry BoM/MoM + reaction counter from e1_ip.mechanics (P533:1145-1161).
- Branch per bound (6.4.2 + 6.4.1 + BoM rule):  IP ZFP > 45 -> FAIL (SS -> BS, 6.4.1) | MoM 3+ reactions -> PIERCED | MoM 0 -> HOLD-LONG (minor reaction, long consolidation 2-4 days)
  | MoM 1-2 -> "assess surrounding liquidity": unswept liquidity beyond the OTHER bound -> SLOW-THEN-PIERCE (branch 4: consolidation ends retesting opposing liquidity, then pierce to BoM liquidity), else BREAK-RETURN (short consolidation, SS -> BS/WL)
  | BoM (unmitigated) -> HOLD (always reacts) | LSZ -> HOLD with breach. Both bounds HOLD -> SS continues all week (6.4.1 "SS all < 30% -> SS continues", B-03).
  Both pierce-type -> the earlier one (PIERCED/FAIL before BREAK-RETURN before SLOW); tie -> 6-check direction validation (A-04, E3C:1082-1095).
- Key rule (A-10): no strong 4H pressure zone (4H BoM 0-1X / Tier-1 IP zone) within the SS reach (GS Law 2: 30 pips) -> "BS most likely days away" -> the consolidation lasts its maximum.
- Durations: SS 2-5 sessions (6.8); slow consolidation 2-4 days (6.4.2, 6.10.5); FA 9 post-energy 1-2 days; raw timing = the minimum of the applicable figure minus the elapsed consolidation;
  adjusted timing = raw + 1 day (6.10.1) for the breakout; both printed (A-14). Consolidation phase Early/Mid/Late from elapsed sessions + bound ZFP trend (A-09).
- ZFP by day (the canon's breakout clock): an option wall holds until its cut (P533 2.2 "pinning ... pre-10:00 AM NY"; 10:01 "Spring Release ... All OTC expiry coordinates become completely invalid");
  P452 Pillar 9 step 2 "Option expiry timing (10:01 NY Spring Release) +20-30% near expiry time" (low end +20, D-row); after the cut the zone is re-typed without that wall (Post-Expiry Ghost 20-40).
- BS target (B-13): first zone beyond the failing bound (IP zone of ANY ZFP, standing 1H/4H S/D zone, unswept LSZ / magnet), TF element matching (A-07: target TF <= source TF + 2, never 4H from a 15m source);
  6.4.2 pierce continues to BoM liquidity through intermediate zones via the 6.4.1 rows; measured move (P452 Pillar 9 step 4 a-d, anchored to a structural extreme within 0.20, confidence tier) when the failing zone is ZFP > 45.
- After BS (6.4.1 on the TARGET): ZFP < 20 or BoM 0-1X -> RWL (preceded by the WL spike when the target is a sweep zone: "WL -> RWL", 6.4) | 20-40 -> R | > 60 -> PBS | > 80 -> PBS HIGH | 40-60 -> R MODERATE (D-row, C-15).
  R -> SS (> 1 session) / WL-RWL (< 1 session, opposing zone near) / BS 2nd leg (recovery zone also fails). RWL -> SS (HIGH) / BS new dir. WL -> RWL / SS. WLS -> BS (VERY HIGH) / SS.
- Chain: max 5 shapes; cumulative confidence (tier numbers, D-row for C-05) < 25% -> stop; later days = NO DESIGNATION (not drawn as SS) (B-07, C-16). Each extension logs shape, trigger zone, ZFP, next, confidence (A-14).
- Alternative chain (A-13): the Decision Zone = the bound whose branch decides the primary; its ZFP threshold; alternative confidence; drawn dotted; E3 builds its setups as conditional (activation = 1H close beyond the Decision Zone).
- Day decomposition: per day shape(s), direction, key zone, triggers (expiry cuts of the day from the sidecar with notional; red folder NO DATA), confidence (A-08). Pairs: DXY shapes, inverted direction, own zones (P533:1899-1917).
- 4H structural validation (A-06): bounds respected by 4H closes; BS direction vs 4H trend -> "confirms / rejects" line.
- Pressure reading (A-05) when bias unclear: 1H candles of the current consolidation: body size, wick direction (canon: "Upper wicks = buying pressure"), triangle flat side; tiebreak 4H storyline (C-02: a still-valid 4H BoM zone's side, else 4H swing structure).

## ENGINE 3 (e3_trades.py) = Phases 0-12 on the E2 day map
- Phase 0 setup universe per day shape; Phase 1 WorkingDayMap (12 fields; < 65% spills to the next day, A-15); Phase 2 candidates for EVERY (day, zone) on the correct side (B-18): SS both directions at the bounds' LTF zones,
  BS at the retest / failing-zone breakout point, WL/RWL at the rejection zone, R scalps; entry sources ORDER_BLOCK / LQZ only (B-21, B-22: a sweep zone is SL / TP / confluence, not an entry);
  freshness gate (battle index > 2 skipped; VIOLATED = closed through; A-16); BoM/MoM enforcement with E1's e3_status (A-18); POI tier rule (A-19); reversal = BoS + flip + retest (A-39).
- Phase 3 TS-1 / F1-A (on the OB short itself, B-23) / F1-C / F1-D (RWL only, C-24) / F1-E (A-28) / intra-zone key level (A-30) / Fib context (A-29); Law 3 no 4H-edge entry (B-24).
- Phase 4: confluence stack 7 layers (A-20); SL ladder-steps (a) 3 pips outside the entry zone's back edge / (b) 1-2 pips INSIDE the close edge of the next step (B-25), chosen by confidence >= 0.6 (B-26), Law 7 buffers per pair (A-23),
  LSZ between entry and SL or widen / reject (A-45); facts in memory/08 (his stops = rule (b) on V1 4H bands / second 1H rung). TP: zone MIDPOINT with LQZ inside (B-28), strong = near edge + 1-2 pips, weak = far edge (B-29),
  Refined Law 14 no teleport past unmitigated zones (A-25), TP TF >= entry TF (A-07), honest absence TP_NULL (B-31). RRR floor 3.0 / consolidation week 2.5 (A-47), MAX_CHAIN_RRR 15 (A-26), refinement on SAME entry (B-32), hair-miss (A-28).
- Phase 5 confidence + classes, inclusion >= 65 (A-21); Phase 6 matrix, chains depth <= 3 with the canon links only (B-19), conflicts 15 pips / duplicates 5 pips (A-31), cap key (pair, anchorBucket, day) (B-36);
  Phase 7 day assignment 12 steps + session windows + anchor hit window (A-32, A-34); Phase 8 labels BE1-BE12 (A-36); Phase 9 2-3 reinforcements at intermediate liquidity / MoM zones at Fib 1.382 / 1.618 with trip-wire, sizing 50/30/20, BE cascade (B-33, A-41..A-43);
  Phase 10 cascade mirror DXY -> EU (inverse, same-element zone class) -> GU (kept, from EU) + emergent lane + divergence flag (A-37); Phase 12 floor invariants (SL envelope, every discard has a reason code) (A-38, A-46).
- Then the S/D findings (A-48..A-52, B-38..B-45, C-27..C-31) and a fresh outside audit (model opus).
