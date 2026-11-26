# G2 outside audit — code vs canon text (Engine 2, Engine 3, supply/demand map, entry point)

Audit date 2026-11-26. Read-only on code. Fidelity only: the canon is taken as correct; nothing here judges the strategy or proposes a mechanism.

## Baseline (what the line numbers refer to)

The repository changed five times while this audit ran (17b6f75 → 50a6a23 → be33e66 → fe2be41 → 76cdde2 → f155664). **Every code line number below is for commit `fe2be41`.** The three engine files are byte-identical at HEAD `f155664`:

| file | lines | md5 |
|---|---|---|
| e1_tool/e1_sd.py | 172 | 5f57756bf9257c642475c33eba2cf5ca |
| e1_tool/e2_chain.py | 386 | 14935d6554782be793c694fc84c419c9 |
| e1_tool/e3_trades.py | 398 | 9228fbb4d6da435adc093d534bca52fd |
| e1_tool/plutus.py | 28 | db2bcefbe172211c9103268508bce69b |
| e1_tool/e1_pine.py | 123 | cdd701a6071577d4ef45bafb4ed19458 |

`plutus.py` and `e1_pine.py` had uncommitted edits in the working tree at 14:35 UTC (a new `reach()` filter); see the addendum at the end. They are not counted.

## Abbreviations

- **E2X** = `e1_tool/canon_extract/P533_lines_1725-2057_PART_VI_ENGINE2.md`, line numbers of the extract file (P533 line = extract line + 1724).
- **E3C** = `canon/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md`.
- **P452** = `e1_tool/canon_extract/P452_FULL_Trident_System_Prompt_v4.5.2.md`.
- **P533** = `canon/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md` (only where a step lies outside the Part VI extract).
- **NOTES** = `e1_tool/reference/Forex_SMC_Notes-1.txt`.
- **GS** = `/home/user/inputs/handover/PLUTUS_VISION_CONTEXT_HANDOVER/03_HOST_BIBLES/TTE_GOLDEN_STANDARD_COMPLETE_REFERENCE.md`.
- **FA** = `canon/Toolset/Trident_Fractal_Architecture_FirstPrinciples_v2.3.md` (authoritative context per L-24 / L-42).
- **RUL** = `memory/04_OPERATOR_RULINGS_LIVE.md`. **GP** = `memory/14_GOAL_PROMPT.md` (the standing order named in CLAUDE.md).
- U = 1.00 DXY point scaled to the pair (100 pips), as in the code.

## Where the counts and examples come from

Counts such as "N of 40 weeks" were obtained by running the committed code unchanged, read-only, from a copy outside the repository, on the 40 weeks that have a sidecar file (Engine 1 + Engine 2 only, so `_opposing_liquidity` did not run there). Setup examples come from the 11 week / pair runs that have a cached V1 harvest (DXY 04-20, 05-18, 06-08, 07-06, 07-13, 08-17, 09-14, 10-05; EURUSD 04-20, 07-06; GBPUSD 07-06). They say which code path fired. They say nothing about outcomes.

Severity: HIGH = changes which setups / shapes / zones come out; MEDIUM = changes a level, a label that the canon makes mandatory, or a rule that fires rarely; LOW = wording, logging, cosmetic.

---

# A. Canon steps with NO code at all

## A — Engine 2 (`e1_tool/e2_chain.py`)

**A-01 · HIGH — Whiplash Storm does not exist**
- Canon: E2X:55 — “| 4 | 3+ IP zones in narrow range (0.30-0.50 DXY); price oscillating violently; 4H shows consolidation | WLS (or Minor WLS if 1-2 sessions) | HIGH |” (also E2X:41-44, :81, :92-93, :107, :159, :203).
- Code: `classify_day()` 30-46 returns only PBS / BS / WL / R / SS; `build()` 238-255 plans only SS / RWL / BS / WL / R / PBS.
- Gap: matrix priority 4, the transitions SS→WLS, WLS→BS, WLS→SS, the WLS anchoring row and Rule 7 have no code. WLS can never be a current shape or a chain step.

**A-02 · MEDIUM — Variants and subtype never produced**
- Canon: E2X:24 — “**Subtype — Double Whiplash Pattern:** Two rapid whiplash moves in succession within the range. Labeled "SS (Double Whiplash)" …”; E2X:33 (RS), :38 (PWL), :39 (PRWL); E2X:57 — “| 6 | After BS: violent reversal in opposite direction through prior origin; Hard Wall rejection | RWL (or PRWL if piercing) | MODERATE-HIGH |”.
- Code: `classify_day()` 39-43 emits 'WL' only; `PIERCING` (16) lists 'RWL' but no branch returns it.
- Gap: SS(DWL), RS, PWL, PRWL and a classified RWL cannot come out of Step 1, so the Setup Universe rows E3C:97, :101, :104, :105 are unreachable.

**A-03 · HIGH — Decision-tree branch not chosen by the reaction counter**
- Canon: E2X:144 — “… The zone's reaction count (from Engine 1 Zone Reaction Counter) helps predict which branch activates:”; E2X:145 — “- 0 reactions (virgin): Most likely MINOR REACTION branch (first test causes reaction but zone holds initially)”.
- Code: `build()` 207-214, 246-255. No read of `z['mech']` (reactions / counter) or of a bound's mitigation count when choosing a branch.
- Gap: the reaction counter computed in `e1_ip.mechanics()` is not consumed by Engine 2. The branch is fixed in code (B-04).

**A-04 · HIGH — Direction Validation 6-check (Engine 2 and Engine 3)**
- Canon: E2X:149 — “… A BoM zone reaction produces a directional move (BS, WL, or RWL) determined by the Direction Validation 6-check.”; E3C:1093 — “**Consensus rule:** if 4+ of 6 disagree with the proposed direction → REVERSE the direction (or REJECT if no reversal pattern exists).” (checks E3C:1086-1091; Rule 2 E3C:1002).
- Code: none. `e2_chain._after_bs()` 177-178 returns 'WL+RWL' for every always-reacting target; `e3_trades._build()` 251-320 takes each leg's direction as given.
- Gap: no function computes the six checks, the consensus, the reversal, or the counter-trend size adjustment (E3C:1095).

**A-05 · HIGH — Pressure Reading Rules 1-3**
- Canon: E2X:255 — “- **Candle size = pressure direction**: Look at which candles are obviously bigger. That is where pressure is building.” (+ E2X:256 wick direction, :257 triangle shapes).
- Code: `build()` 199-216.
- Gap: when bias is unclear the code uses its own MoM-asymmetry rule and then the 4H tiebreaker; candle size, wick direction and triangle shape are never read. Direction decided by: 4H storyline 20, MoM-asymmetry 15, running BS 5, failing bound 0 of 40 DXY weeks.

**A-06 · MEDIUM — 4H structural validation**
- Canon: E2X:11 — “- **4H (STRUCTURAL):** Validates SS range boundaries and BS direction — never primary”; E2X:275 — “4H Structural Validation: [confirms/rejects 1H classification]”.
- Code: `_bounds()` 74-95; `current_shape()` 49-71; `storyline()` 20-27.
- Gap: no step validates the range bounds or the Step 1 classification on 4H. The 4H scan is read only as a direction tiebreaker.

**A-07 · HIGH — Timeframe Element Matching / TP Timeframe Law**
- Canon: E2X:250 — “This refines TP targeting: a breakout that originates on 15m liquidity should NOT target a 4H zone — it will likely be absorbed before reaching it. …”; E3C:350 — “- TP timeframe must be ≥ entry timeframe” (E3C:1172-1176; GS:564).
- Code: `e2_chain._target()` 115-148 (candidates ranked by distance, 142); `e3_trades._target()` 125-190.
- Gap: neither engine compares the timeframe of the source / entry zone with that of the target. Targets can be sweep zones, IP zones, LQZ rungs or Fib levels that carry no timeframe.

**A-08 · MEDIUM — Volatility triggers per day**
- Canon: E2X:173 — “… (d) note any volatility triggers (auctions, expiries, economic events), (e) state confidence.”; E2X:205 — “**RULE 9:** No Session Predictions Without Catalyst Identification.”
- Code: `build()` day dicts 295-339 (fields: shapes, dir, lo, hi, key, conf).
- Gap: no trigger field. The expiry cut dates already in the sidecar file are not attached to days, so E3 BE8 and the Red Folder deferral have no input.

**A-09 · HIGH — Consolidation Phase Detection → valid setup types**
- Canon: E2X:224 — “For each SS/WLS/R shape identified by Engine 2, classify the **consolidation phase** to determine which setup types are valid:”; E2X:231 — “| Post-BS (early breakout) | BS confirmed, move in progress | Reinforcement entries only | Swing Stack |” (E3C:1031, :1131-1136).
- Code: `current_shape()` 61-69 sets its own `phase` strings ('post-energy', 'late', 'recovery'); `e3_trades.py` never reads a phase.
- Gap: Early / Mid by elapsed sessions, Late by ZFP trend, the two Post-BS phases and Mid-breakout are not detected, and no phase restricts setup types. With a BS running at the anchor the code still builds an HTF-Swing primary (DXY 2026-08-17 log “Mon BS down: rejected”).

**A-10 · HIGH — Key rule on breakout timing**
- Canon: E2X:235 — “**Key rule**: "If not right near a strong 4H pressure zone right now — BS is most likely days away. This is swing scalp valley — milk the cow on the 15m timeframe."”
- Code: `build()` 247-250.
- Gap: no test of the distance to a strong 4H pressure zone. The breakout day comes from `n_ss` (1 or 2): all 35 consolidation weeks of 40 (DXY) place the BS on Tuesday or Wednesday.

**A-11 · HIGH — Transition rules never evaluated**
- Canon: E2X:86 — “| R | WL/RWL | Recovery reaches opposing IP zone | MODERATE |”; E2X:88 — “| WL | RWL | Whiplash rejected at zone; opposite momentum builds | MODERATE-HIGH |”; also E2X:84, :87, :91, :109-110.
- Code: `current_shape()` 63-67; `_after_bs()` 173-183 (the only transition computed).
- Gap: R→BS (2nd leg), R→WL/RWL, WL→RWL, RWL→BS (new direction), BS→PBS (“extreme momentum; distant target”) and SS→WLS are not coded. A last-session WL or R is mapped straight to SS.

**A-12 · MEDIUM — Step 1 statement**
- Canon: E2X:165 — “… State the current shape, the IP zone anchoring it, and the ZFP of the anchoring zone.”
- Code: `current_shape()` 58-71 (s0 = shape, dir, phase, why, history).
- Gap: no anchoring zone and no ZFP is attached to the current shape. The default SS (69) is tied to no zone (Rule 1, E2X:197).

**A-13 · MEDIUM — Step 4 items; the alternative is not used**
- Canon: E2X:171 — “… Document: (a) the Decision Zone, (b) the ZFP threshold that triggers the alternative, (c) the alternative chain, (d) alternative chain confidence.”
- Code: `build()` 341-351; `pine()` 357-370; `e3_trades.py` 17 (`ALT_SETUPS = False`), 212-221.
- Gap: (b) and (d) are not produced. The alternative chain is not drawn and yields no setups (E3C:1035), and none is built when a BS is running (350).

**A-14 · LOW — Audit trail and output blocks**
- Canon: E2X:169 — “… For each extension: document (a) current shape, (b) the IP zone trigger, (c) the transition conditions (ZFP value), (d) predicted next shape, (e) confidence level.”; E2X:301-302 (Raw timing / Adjusted timing); E2X:15.
- Code: `build()` audit list 192, 217, 245, 254-255, 348; `pine()` label 366.
- Gap: three or four free-text lines replace the per-extension trail. No raw-versus-adjusted timing, no “Primary Timeframe: 1H | Structural Validation: 4H” line. The chart label carries day + shapes only (no key zone, triggers, confidence).

## A — Engine 3 (`e1_tool/e3_trades.py`)

**A-15 · HIGH — Phase 1 WorkingDayMap and its speed adjustment**
- Canon: E3C:115 (the twelve fields); E3C:123 — “6. Apply Trading Speed Adjustment: for each day, if E2's confidence < 65%, propagate the shape to the next day …”; E3C:124.
- Code: `_build()` 242-253 (consumes `E2['legs']`).
- Gap: no WorkingDayMap (supplyZoneId, demandZoneId, deepDemandZoneId, dayOpenSpot, session, confidence), no check that every keyZoneId resolves to an E1 zone. The <65% rule is absent although Engine 2 emits 52% / 42% / 33% on breakout and final days (BE12, E3C:617).

**A-16 · HIGH — Freshness gate / lifecycle / depleted zones**
- Canon: E3C:150 — “… (a) index `i > 2` skipped — 4th+ battle is DEPLETED/consumed structure …”; E3C:160 — “DEPLETED (3+ battles)     → TP target ONLY — the zone will fail ("zones usually fail on the THIRD mitigation")”; E3C:1052.
- Code: none. `_first_anchor()` 193-200 and `_entries()` 49-83 never read `mit`, `mech['reactions']` or `mech['counter']`.
- Gap: no battle index, no depletion test. DXY 2026-09-14 DX1 (Mon SS) and DX2 (Tue RWL) enter at “1H (Mitigated 3x) | MoM” supply.

**A-17 · HIGH — Phase 2.5, 1-2-3 retest timing**
- Canon: E3C:1152 — “| 0 (Virgin) | Scalp only | First test — liquidity not yet accumulated |”; E3C:1154 — “| 2 | Swing entry valid | Third test — enough Earth accumulated to fuel swing move |”; Rule 7 E3C:1007.
- Code: none (`CAT` 21; `_build()` 273-320).
- Gap: retests are not counted. HTF-Swing and Reversal setups are emitted at unmitigated zones (DXY 2026-04-20 DX5, WL SHORT at “4H (Unmitigated) | BoM”).

**A-18 · HIGH — BoM/MoM enforcement; Engine 1's `e3_status` is ignored**
- Canon: E3C:1006 — “6. BoM/MoM ENFORCEMENT (no entry at MoM unless ALL 4 exceptions)”; E3C:1012 — “12. MoM Zones = Ladder Steps ONLY (no reversal entries at MoM, EVER …”; E3C:1025; E3C:1053.
- Code: none. `e3_trades.py` never reads `kind`, `mech['bom']`, `mech['e3_status']`, `mech['mom_exceptions']`.
- Gap: nothing separates ENTRY-PRIMARY / CONDITIONAL / TP-TARGET / REJECT. Golden week DXY DX3 enters at IP “UPPER RESISTANCE”, which Engine 1 itself marks MoM / TP-TARGET; DX1 and DX2 enter at 1H MoM zones; DXY 2026-09-14 DX2 is a “Reversal” at a MoM supply zone; EURUSD 2026-04-20 EU3 is a “Reversal” at an IP zone marked MoM / TP-TARGET.

**A-19 · HIGH — Rule 1, POI tier**
- Canon: E3C:1001 — “1. No trade without Tier 1 or Tier 2 POI”.
- Code: none (`z['tier']`, set in `e1_ip.build()`, is never read).
- Gap: anchors are candle zones, LQZ rungs, V1 liquidity bands or sweep zones with no POI-tier test.

**A-20 · HIGH — Phase 4.1 confluence stack**
- Canon: E3C:241 — “| 3 | Reaction Counter alignment (UM BoM = +5; MoM = -10; Depleted = REJECT) | +5 / -10 / REJECT |”; E3C:242 (TF stack violation = REJECT); table E3C:237-245.
- Code: none.
- Gap: the seven layers, including both REJECT conditions, have no code.

**A-21 · HIGH — Phase 5 confidence, quality classes, inclusion gate**
- Canon: E3C:1011 — “11. Max 3 setups per category per pair; total max unlimited (NO CAPS — operator D38); confidence ≥65 required for inclusion”; scoring E3C:392-404; classes E3C:420-424.
- Code: none. The setup dict (`_build()` 305-317) has no confidence and no quality.
- Gap: every setup with RRR ≥ 3 is emitted. Nothing is scored, classified or gated at 65.

**A-22 · HIGH — Fuel state, mirrorConfidenceScore, ZR-6B inputs**
- Canon: E3C:258 — “- If fuel INTACT → LQZ SHIELD_FUEL (the LQZ acting as shield in front of the S/D)”; E3C:259-260; E3C:274-286.
- Code: `_stops()` 94-99.
- Gap: no fuel state exists. “Current step” is always the element the entry sits on (rung, nested block, band), so for a rung entry the stop is 3 pips beyond the rung and lands inside the anchor zone, although E3C:254 reads “(entry zone's back edge + 3p)”. Golden week DX3: entry 101.203, stop 101.256, zone top 101.262.

**A-23 · MEDIUM — Law 7 buffers and pair mechanics**
- Canon: E3C:301 — “| EUR/USD | 2 | Tightest spread (0.1-0.3), deepest liquidity ($2.5T daily), shallow hunts (1-2p) |” (+ :302, :304); E3C:1101-1103 (forward spread, special rules).
- Code: `_stops()` 95, 99 (3 pips / 1 pip for every pair); `NO_SHIELD` 103, 295-297.
- Gap: no pair-specific buffer and no forward spread. Of the special rules only EUR/USD NO_SHIELD has code; NY_FOCUS, DIRECT_ZONE_TEST, SHORT_SQUEEZE, LONDON_DOMINANT, HIGH_GAP_RISK have none.

**A-24 · MEDIUM — Golden SL fallback computation**
- Canon: E3C:291-293 — “computeSL_LMV 4-9.5p reaction-extreme” / “+ selective util guard tighten iff util < 0.40” / “+ §4.4.3 wick-clear”.
- Code: none (constants only, 16).
- Gap: the reaction-extreme stop, the utilisation guard and the wick-clear are not computed (how 4 and 9.5 are used instead: C-19).

**A-25 · HIGH — Refined Law 14 / sequential zone path**
- Canon: E3C:347 — “"Price cannot teleport past UNMITIGATED zones. Price CAN pass through mitigated zones during BS momentum. …”; Rule 8 E3C:1008.
- Code: `_target()` 133-145 (the BS branch goes straight to the E2 target).
- Gap: zones between entry and TP are not walked and no reaction count is tested. DXY 2026-04-20 DX3: BS LONG with the TP 82 pips away, beyond the range ceiling the code itself labels “1H (Unmitigated)”.

**A-26 · MEDIUM — MAX_CHAIN_RRR**
- Canon: E3C:365 — “- **MAX_CHAIN_RRR ceiling:** 15.0 (Law-13) — chains beyond 15R fill-and-stop (GU 1.34957 measured)”.
- Code: none (`_build()` 303-306).
- Gap: no ceiling. Emitted: DXY 2026-04-20 DX3 19.47; DXY 2026-09-14 DX3 18.34 and DX5 15.67; GBPUSD 2026-07-06 GB5 17.37.

**A-27 · MEDIUM — Blended RRR and Scaled Entry Protocol (Mechanism A)**
- Canon: E3C:357 — “**Blended RRR (3-entry staggered):** `(rrr1 × 0.33) + (rrr2 × 0.33) + (rrr3 × 0.34)`”; E3C:1064-1066; E3C:1069-1071.
- Code: none.
- Gap: one entry per trade. No Front / Middle / Back entries, no forward spread, no blended RRR, no intra-zone SL cascade.

**A-28 · MEDIUM — F1-E recovery shelf; RWL hair-miss repair**
- Canon: E3C:200 — “… pull the entry to the shelf center: `RWL_SHELF_LONG_ADJUST_PIPS = 1`.”; E3C:197 — “`RWL_HAIR_MISS_RRR_DELTA = 0.1` — setups with RRR in [floor − 0.1, floor) get one repair attempt before hard reject.”
- Code: none (`_entries()` 49-83).
- Gap: neither rule exists.

**A-29 · HIGH — Fibonacci Spiderweb anchoring**
- Canon: E3C:207 — “| 1 | 1H | BS / WL on 1H shapes | Fib retracements from prior week's H/L + 0.382→1.382 wormholes |” (+ :208-209, :212-216, :226-229); Rule 3 E3C:1003.
- Code: none in `e3_trades.py` (its only Fibonacci arithmetic is `_env()` 30-36, see C-17) and none in `e2_chain.py`.
- Gap: no retracement of prior-week / 15m / 30m swings, no wormhole target, no Fib entry or TP.

**A-30 · MEDIUM — Intra-zone key levels for TS-1**
- Canon: E3C:181 — “> - If key_levels exist within the zone, use the one closest to the approaching edge (within the zone)”; E3C:1028.
- Code: `_entries()` 64-71, 82.
- Gap: `z['intra']` (from `e1_ip.intra_zone()`) is never read by Engine 3 and is not drawn by `e1_pine.generate()`.

**A-31 · MEDIUM — Phase 6.3 conflict and duplicate rules**
- Canon: E3C:462 — “- If `direction` is opposite AND entries within 15 pips → CONFLICT (only the higher-confidence one survives)”; E3C:463 — “- If `category` is same AND entries within 5 pips → DUPLICATE (dedup by anchor-zone-id; keep first)”.
- Code: `_build()` 340-354 covers only “same entry step + same day + same direction”.
- Gap: the 15-pip opposite-direction conflict and the 5-pip same-category duplicate have no code (the cap key: B-36).

**A-32 · MEDIUM — Phase 7.1 day assignment**
- Canon: E3C:496-498 (NO_DAY_ASSIGNABLE); E3C:537 — “if matchingDays[0].confidence < 0.65 && setup.day !== 'Friday':”; E3C:508-525; E3C:548-551.
- Code: `_build()` 316 (`day=leg['days'][0]`).
- Gap: the 12-step algorithm is replaced by “the day of the leg”. No abort, tiebreak, speed adjustment or cascade check.

**A-33 · MEDIUM — Red Folder deferral**
- Canon: E3C:1125 — “30-minute deferral on red-folder economic events (CPI, PPI, NFP, FOMC). Setups whose anchor hit window overlaps a red-folder event are deferred by 30 minutes.”; Rule 10 E3C:1010.
- Code: none. `e1_tool` has no economic-calendar input.
- Gap: no deferral, no day catalysts.

**A-34 · MEDIUM — Session bracket, session selection, liquidityScore filter**
- Canon: E3C:77 — “… Every order leg's session bracket comes from the E2 session label. …”; E3C:560-561; E3C:574-576.
- Code: `SESSION` 22 (a label); `build()` 222-232 and `pine()` 367-370 (validity = whole day(s) or the whole SS run).
- Gap: the session is written into a Pine comment only. Orders are not bracketed by a session window. The per-day default and the liquidityScore filter have no code.

**A-35 · HIGH — Shape-based reachability of setups (Law 2 / Law 7)**
- Canon: GS:152 — “3. Only generate setups at zones within the expected range for that day's shape”; GS:36 — “| SS (Mon-Tue) | ±5-30 pips (consolidation) | 0-30 pips | Scalp entries at nearby zones |”; E3C:588.
- Code: `_first_anchor()` 193-200; `_build()` 255-320.
- Gap: no distance test between spot, entry and the day's shape. DXY 2026-06-08 DX1 “Mon SS”: entry 78 pips from spot, target 78 pips; DX3 “Wed SS”: 87 pips from spot. EURUSD 2026-04-20 EU1 “Mon SS”: target 64 pips.

**A-36 · MEDIUM — Anchor hit window and the label law**
- Canon: E3C:600 — “> **Phase 8 contract:** Every surviving setup MUST carry the 5 blind-execution labels. No label = setup REJECTED.”; E3C:581-596; BE5 / BE8 / BE10 / BE11 E3C:610-616; Rules 13-14 E3C:1013-1014.
- Code: `_build()` 316-317; `pine()` 371-374.
- Gap: no anchor hit window, no weekly execution calendar, no day catalysts, no “No qualifying setups — [reason]” for empty days, no Friday close rule. The on-chart label is id + shape + direction + RRR.

**A-37 · HIGH — Phase 10 cascade mirror**
- Canon: E3C:787 — “- Mirror lane = guaranteed floor (every DXY setup MUST produce EU + GU mirrors)”; E3C:773 — “for m of activeEuMirrors:  # GU mirrors ACTIVE EU mirrors, NEVER raw DXY”; E3C:741; E3C:796-799.
- Code: `plutus.run()` 10-16; `e3_trades.build()` 209-233.
- Gap: each pair's setups are built from its own legs. No setup-level mirror, no same-element class matching, no GU-from-EU loop (GBPUSD is driven by the raw DXY chain, `plutus.py` 11), no divergence computation. Golden week: DXY 7 setups, EURUSD 6, GBPUSD 6.

**A-38 · HIGH — Phase 12 audit and final gates**
- Canon: E3C:856 — “# SL envelope (within GOLDEN_SL_MAX_PIPS = 9.5)”; E3C:864 — “structurallyValid({sl}, openPrice, direction)”; E3C:876 — “suppress > 30 (WEAK)”.
- Code: none (a rejection is one free-text log line, `_build()` 311).
- Gap: no 3D audit, no floor invariants, no CS-1 day-native guard, no narrative gate. Stops beyond 9.5 pips pass: DXY 2026-04-20 DX5 17.3; EURUSD 2026-04-20 EU3 10.6; DXY 2026-06-08 DX4 10.0.

**A-39 · HIGH — Reversal pattern requirement**
- Canon: E3C:168 — “A reversal setup requires (ALL THREE):”; E3C:171 — “3. Retest — price retests the flipped level from the new direction; entry at the retest”.
- Code: `CAT` 21 ('RWL': 'Reversal'); `_build()` 273-320.
- Gap: “Reversal” setups are plain resting orders at the previous TP zone. No break of structure, flip or retest condition is attached.

**A-40 · MEDIUM — Setup Universe rows and stack compliance**
- Canon: E3C:107 — “| SS→BS Transition | Transition Entry | Both Stacks | 1 transition + reinforcements |”; E3C:97, :100-101, :105-106; Rule 9 E3C:1009.
- Code: `CAT` 21.
- Gap: no Transition Entry, DWL Inverse or Recovery Surge. A setup carries no timeframe stack, so stack compliance cannot be tested.

**A-41 · MEDIUM — Reinforcement timing inheritance**
- Canon: E3C:625 — “> Reinforcement ORDERS are placed in London premarket (pending stop-limit orders). Reinforcement ORDERS become ACTIVE only when the 1-2-3 pattern completes on the primary entry (Phase 2.5). …”
- Code: `_build()` 335-339.
- Gap: the rocket is a plain box from the start of the leg's second day. No activation condition, no cancellation at parent TP.

**A-42 · MEDIUM — Trip-wire mechanics, rocket type, sizing**
- Canon: E3C:688 — “1. Trigger zone identified (the trip-wire zone — typically 2.382–2.786 Fib)”; E3C:676-678 (FLR / FR / LR with buffers); E3C:633-635 (50/30/20, SL cascade).
- Code: `_build()` 321-339.
- Gap: no trigger zone, no rocket type, no buffer-zone count, no sizing, no break-even cascade.

**A-43 · MEDIUM — 8R.10, 8R.5, Phase 11**
- Canon: E3C:718 — “… for each setup, map ALL liquidity zones (LSZ/LQZ) between entry and TP. Each is a potential reinforcement anchor. …”; E3C:670; E3C:804.
- Code: `_build()` 325-328 (first rung only).
- Gap: liquidity zones along the TP path are not mapped; no 4H-BoM cascade rule; no Master Trade Setup / Avatar State.

**A-44 · MEDIUM — Acceptance counts**
- Canon: E3C:996 — “f(T) Acceptance: |all_setups| = 24 minimum (8 DXY + 8 EU + 8 GU), MORE is fine, LESS is REJECT”; E3C:1011 (max 3 per category).
- Code: none.
- Gap: no check. The 11 cached runs emit 2 to 7 setups per pair. The per-category maximum is not enforced either.

**A-45 · MEDIUM — A liquidity zone between entry and stop**
- Canon: GS:69 — “3. If no LSZ between entry and SL → SL widened to next LSZ or setup rejected”; E3C:1048 — “- `NO_LSZ_ANCHOR` — no LSZ for SL placement”; E3C:1026-1027.
- Code: `_stops()` 94-99; `_pick_stop()` 110-117.
- Gap: the “3 pips outside the current step” stop needs no liquidity zone between entry and stop, and a swing scalp always takes the tightest candidate (114-115). `X['lsz']` is consulted for stops only on sweep-zone entries.

**A-46 · LOW — ABORT macro and reason codes**
- Canon: E3C:1042 — “⚠ E3 SETUP [${setupId}] ABORT: [reason] — setup marked [REJECTED]. Continuing with remaining setups.”
- Code: `_build()` 258, 311.
- Gap: one message for every failure (“no TP with RRR >= 3.0 in three attempts”, also when the cause is no stop or no target). No reason code, no three-attempt trail.

**A-47 · LOW — Consolidation-week floor**
- Canon: E3C:1115 — “| Consolidation week (relaxed) | 2.5 | 3.0 | 3.5+ |”.
- Code: `RRR_FLOOR` 16.
- Gap: one floor (3.0) for every week.

## A — Supply / demand map (`e1_tool/e1_sd.py`)

**A-48 · MEDIUM — Noise rejection rule 4 and the “4H-Only Level” flag**
- Canon: P452:745 — “- Zone that does not overlap with any IP zone within 0.50 DXY points AND is not a BoM zone with 0X-1X mitigation. …”
- Code: `valid()` 101-109; `zone_map()` 117-160.
- Gap: MoM zones and 2X+ BoM zones with no IP zone within 0.50 stay in the map and are used by Engines 2 and 3. No “4H-Only Level” flag.

**A-49 · MEDIUM — Verification check 2 and the audit trail**
- Canon: P452:663 — “2. The candle immediately AFTER the zone candle moved directionally (confirming the zone as origin)”; P452:676.
- Code: `scan()` 57-59 (`z['next']` is stored and never tested).
- Gap: no verification step and no per-zone trail. 519 of 2,130 valid DXY zone-instances (40 weeks, four timeframes) have an inside bar as the candle after the zone candle (see B-39).

**A-50 · MEDIUM — Zone quality: momentum, depth, time**
- Canon: NOTES:88 — “If price goes more than half or all the way into the zone,”; NOTES:95 — “The longer the prices spends consolidating in a zone, the higher”; RUL:101 (L-38) — “Zone quality: more momentum = better; sharp reaction = valid, consolidating around it / more than halfway in / long time inside = likely to fail.”
- Code: `scan()` 62-83.
- Gap: a visit is only “soft” or “hard”. Penetration beyond half and time spent inside are not measured. `z['move']` (61) is never used to grade a zone.

**A-51 · LOW — High-conviction tag, count format, paradox signal**
- Canon: P452:681 — “- If move >= 1.0 DXY points and >= 5 days: tag "High-Conviction 4H OB"”; P452:722; P452:730.
- Code: `scan()`; `state()` 112-114.
- Gap: no tag, no “[X]X mitigated ([Y] soft, [Z] hard)” label, no 4-5X handling.

**A-52 · LOW — Step 0g outputs; Step 0h alternative criterion** (the 0h part sits in `e1_ip.py`, outside the five listed files)
- Canon: P452:755 — “**Condition B — Gap-Fill Only:** If a 0.20+ DXY gap exists between mapped zones and no 4H/D1 level fills it, …”; P452:774 — “- OR: Clear 1H/4H demand/supply zone reaction at this level”.
- Code: `zone_map()` 157-158 (`nested_in` computed, never output); `e1_ip.levels()` minor-swing block.
- Gap: no Gap-Fill Anchor, no “1H Precision Floor … nested inside …” output, no reaction-based minor swing, no 0h-b tags.

---

# B. Code that contradicts a canon sentence

## B — Engine 2

**B-01 · HIGH — Shapes are classified on D1 session candles**
- Canon: E2X:7 — “All macro shape classification, chain mapping, and session decomposition MUST be performed on the 1H timeframe as the primary analysis layer.”; E2X:13 — “- **D1 (MACRO):** Regime context only — weekly trend direction”.
- Code: `classify_day()` 33-46; `current_shape()` 52.
- Deviation: Step 1 reads four numbers per session (daily open / high / low / close from `X['daily']`). No 1H structure enters the classification.

**B-02 · HIGH — Matrix conditions dropped**
- Canon: E2X:52 — “| 1 | Price breaks through zone with ZFP > 45% AND confirms 15+ min; Measured Move target exists | BS (or PBS if pierces multiple zones) | HIGH |”; E2X:53 (WL: ZFP < 20%, Liquidity Sweep Target identified); E2X:54 (R: mid-range zone ZFP 20-40%); E2X:56 (SS: Heavy/Extreme ceiling and floor, both ZFP < 30%).
- Code: `classify_day()` 34-46.
- Deviation: BS = the daily body crossed any MODERATE+ zone (no ZFP > 45, no measured-move test). WL = a wick through any zone (no ZFP < 20, no sweep target). R = “the session after a piercing one” (no zone, no ZFP 20-40; direction from candle colour). SS = whatever is left. PBS = two zones, without “ZFP above 70%” (E2X:29).

**B-03 · HIGH — SS → BS is forecast while both bounds hold**
- Canon: E2X:106 — “| SS | All < 30% (both sides hold) | **SS continues** | HIGH | Both bounding zones are solid — consolidation continues. |”
- Code: `build()` 213-214 (its own text: “both bounding zones hold”), then 246-255.
- Deviation: a breakout is planned every week. No bound has ZFP > 45 in any of the 40 DXY weeks, yet all 35 consolidation weeks get SS → BS. In 9 of them both bounds are IP zones under 30% (2026-07-06 among them).

**B-04 · HIGH — Decision tree applied with no tested zone, no reaction, no zone class**
- Canon: E2X:117 — “When a MoM zone is tested during the shape chain, the reaction determines the subsequent shape. …”; E2X:149 — “**For BoM zones:** BoM zones are NOT subject to this decision tree — they ALWAYS react (100% guarantee if unmitigated). …”
- Code: `build()` 218, 248, 254, 308-314.
- Deviation: the fourth branch (retest opposing liquidity, then pierce) is the plan of every consolidation week, whatever the bounds are (IP zones, BoM zones, sweep zones) and before any test has happened.

**B-05 · HIGH — “RWL” placed before the breakout**
- Canon: E2X:37 — “**Variant — Reverse Whiplash (RWL):** A Whiplash in the opposite direction of the preceding BS. Most common follow-on shape after BS.”; E2X:80-81 (the only transitions out of SS are BS and WLS); E2X:158.
- Code: `build()` 248 (`['SS', 'RWL', 'BS']`), 312.
- Deviation: every consolidation week contains SS → RWL → BS. That RWL follows no BS, and its rejection zone is not tested against the 6.5 metrics (ZFP < 20%, Confluence ≥ 8, LSZ). It yields a “Reversal” setup in Engine 3 each week.

**B-06 · MEDIUM — Hard-Wall target gives “WL+RWL” with a WL leg**
- Canon: E2X:101 — “| BS | < 20% (Hard Wall) | **RWL** (rejection, NOT R/PBS) | HIGH | Zone is a Hard Wall — price WILL be rejected. Do NOT predict continuation. |”
- Code: `_after_bs()` 177-178; `build()` 244, 250, 322-327.
- Deviation: the next shape is a two-shape token. The day is labelled “WL + RWL” and the only leg emitted is 'WL' (category HTF Swing in Engine 3). There is no RWL leg.

**B-07 · MEDIUM — Chain termination has no effect**
- Canon: E2X:169 — “… Maximum chain length: 5 shapes. Terminate if cumulative confidence drops below 25%. …”; Rule 6 E2X:202.
- Code: `build()` 260-265.
- Deviation: the `break` only stops the audit list, after the low step has been appended. Plan, days and legs are untouched. (With the code's numbers the product is 0.42 or 0.33 in all 40 weeks.)

**B-08 · HIGH — Fixed week templates instead of step-by-step extension**
- Canon: E2X:169 — “**Step 3: Chain Extension with Audit Trail.** Extend the shape chain forward, shape by shape, through the trading week. …”; Rule 4 E2X:200.
- Code: `build()` 242-255.
- Deviation: two hard-wired templates, `SS×n → SS+RWL+BS → BS → X` and `BS → X → SS → SS → SS+BS`; only X comes from a table. The 40 DXY weeks give five day-maps (20 / 12 / 3 / 3 / 2). GP:67-68 lists “a fixed E2 template” as an own idea.

**B-09 · HIGH — Consolidation phase and length**
- Canon: E2X:230 — “| Late consolidation (near HTF zone) | ZFP trending up on bounding zone | Swing Scalps + BS Transition Entry | Both Stacks |”; E2X:211 (SS: 2-5 sessions); E2X:330 — “… expect a slow consolidation around this POI for 2-4 days." Consolidation lasts longer than expected.”
- Code: `current_shape()` 63-65, 68-69; `build()` 247-249.
- Deviation: 'late' is assigned whenever the last session was SS or WL (no ZFP trend, no session count) and cuts the consolidation to one SS day, so the breakout lands on Tuesday (12 of 40 DXY weeks).

**B-10 · MEDIUM — Recovery reclassified after one session**
- Canon: E2X:108 — “| R | Persists > 1 full session | **SS** (reclassify, NOT continue R) | MODERATE-HIGH | …”; E2X:109 — “| R | < 1 session, opposing zone near | **WL or RWL** | MODERATE | Brief pause then rejection at opposing zone. |”
- Code: `classify_day()` 44-45; `current_shape()` 66-67.
- Deviation: R is by construction the single session after a piercing one and is turned into SS at once. The “< 1 session, opposing zone near” row is never tested.

**B-11 · HIGH — Range bounds that are not IP zones meeting the 6.5 metrics**
- Canon: E2X:155 — “| SS | Ceiling and Floor zones define the range | Both bounding zones: ZFP < 30%, Confluence ≥ 6 |”; E2X:22.
- Code: `_bounds()` 82-95; `_sweep_bound()` 98-112.
- Deviation: when no IP zone under 30% lies within 30 pips, a candle zone or a sweep zone becomes the bound and is handed an invented ZFP and score (C-01). Of 80 DXY bounds: 24 IP zones, 46 candle zones (28 MoM, 5 with ≥ 3 mitigations), 10 sweep zones. GBPUSD: 1 IP zone of 80.

**B-12 · HIGH — MoM zones as holding bounds and reversal anchors**
- Canon: E2X:239 — “… Do NOT enter for swing at 4H MoM zones — scalp only at most. …”; FA:519 — “From Trading Laws: “Do not take reversal entries on MoM zones. EVER. Guaranteed loss.””
- Code: `_bounds()` 91-94 (the pool holds 4H / 1H zones of either kind); `build()` 218, 312.
- Deviation: when both bounds are MoM, or the MoM one is `far`, the MoM zone is the level the RWL “rejects” from and the edge the SS swings turn at. Engine 3 then anchors Reversal / HTF-Swing entries there (DXY 2026-04-20, 2026-09-14).

**B-13 · HIGH — Breakout target**
- Canon: E2X:27 — “… then surges directionally toward the next IP zone or Structural Extreme Magnet. …”; E2X:156 — “| BS | Failing zone triggers BS; target zone determines magnitude | Failing zone: ZFP > 45%. Target: Measured Move |”; P452:1015.
- Code: `_target()` 121-142; `build()` 220-223.
- Deviation: IP zones with ZFP ≥ 30 are skipped as targets; a BoM candle zone, the nearest sweep level or an IP zone under 30% is taken, nearest first. The 6.4.1 rows for 20-40 / > 60 / > 80 targets are reachable only through the fallback (next shape after BS: WL+RWL 35, R 5, PBS 0 of 40). The measured move is a last resort computed as bound ± range height with no structural-extreme cross-reference and no confidence tier (P452:1012-1024); DXY 2026-06-08 DX4 takes its TP there, 150 pips away.

**B-14 · MEDIUM — “Always reacts” without the unmitigated test**
- Canon: E2X:149 — “… they ALWAYS react (100% guarantee if unmitigated). …”; P452:729 — “| 3X mitigated | Likely to fail | Expect failure. Especially MoM. |”
- Code: `_target()` 122-125 (no test of `z['mit']`); contrast `build()` 232, where the running-BS branch does test `mit <= 1`.
- Deviation: any BoM candle zone beyond the bound is an always-reacting, Hard-Wall-class target whatever its mitigation count.

**B-15 · MEDIUM — Decision Zone trigger**
- Canon: E2X:171 — “… The Decision Zone is the IP zone whose ZFP determines which chain activates. …”
- Code: `build()` 345-347.
- Deviation: the trigger written is “fails (1H close beyond it)”, and the zone may be a candle or sweep bound. No ZFP threshold.

**B-16 · MEDIUM — Trading Speed Rule**
- Canon: E2X:322 — “… When predicting day-level shape assignments, add 1 day to expected timing.”
- Code: `build()` 316-320 (the only place that cites 6.10).
- Deviation: no raw timing is computed and shifted. The rule is replaced by a path shape (“a continuation day reaches the bound; the day after pierces it”).

**B-17 · LOW — One shape per day; tiers; pair chain text**
- Canon: E2X:173 — “… Format: `Mon: [SHAPE] [direction] | Key Zone: [name] | Triggers: [list] | Confidence: X%`”; E2X:80 (“HIGH (ZFP > 60%)”); E2X:104 (> 80% → PBS, HIGH).
- Code: `build()` 244, 248, 257-259, 235, 238-241; `_after_bs()` 181-182; day confidences 307, 321, 327, 336, 339.
- Deviation: days carry up to three shapes. SS→BS is HIGH for any ZFP > 45 and MODERATE-HIGH when nothing fails; PBS is MODERATE for every ZFP > 60. In 'bs0' mode the day confidences are read from the wrong chain positions. For pairs the chain / alternative text uses the pair's own next shape while the day map copies DXY's (they differ in 7 EURUSD and 5 GBPUSD weeks of 40).

## B — Engine 3

**B-18 · HIGH — Candidate generation**
- Canon: E3C:129 — “> **Phase 2 contract:** For each `(WorkingDay, zone)` pair where the zone is on the correct side of spot per the day's direction, generate a trade candidate. Reject candidates failing the structural gate.”; E3C:469.
- Code: `_build()` 250-320; `_first_anchor()` 193-200.
- Deviation: exactly one candidate per Engine 2 leg. Its anchor is the previous trade's TP zone (first trade: the nearest 1H / 4H candle zone beyond spot). Zones are never enumerated per day and then filtered.

**B-19 · HIGH — Trade-flow chain depth and links**
- Canon: E3C:450 — “4. Emit the chain: `CHAIN-${rootId}-D${depth}` (max depth = 3 per Law-13)”; E3C:1121; links E3C:453-457.
- Code: `_build()` 320 (`anchor = s['tp_zone']`), 275-280.
- Deviation: Law 27 generates every anchor after the first, giving one chain per week (golden week DXY: DX1→DX2→DX3→DX4→DX5→DX7, six links) with links the canon list does not contain (SS→SS, SS→RWL, RWL→BS).

**B-20 · MEDIUM — Breakout entry copied from the previous TP price**
- Canon: E3C:457 — “- SS → BS: Range boundary break becomes BS entry”; E3C:178 — “> **SNIPER ENTRY = zone edge CLOSEST to approaching price.**”
- Code: `_build()` 277-280; `_target()` 146-150.
- Deviation: after an RWL the BS entry is the RWL's TP price itself, including that TP's 1-pip exit spread: 1 pip short of the liquidity band's near edge (golden week DX5 101.235 against a band starting at 101.245), or the middle of the far bound when no band is found (149). It is not the break of the range boundary.

**B-21 · HIGH — IP zone used as an entry**
- Canon: E3C:136 — “- IP zones (source==='PILLAR') are confluence/ZFP/context + SL/TP rungs — NEVER entries”.
- Code: `_entries()` 69-70; `_build()` 260-261.
- Deviation: with no LQZ rung overlapping it, the IP zone's own edge is the entry (EURUSD 2026-04-20 EU3: RWL LONG at 1.17573, the top edge of IP “EQUILIBRIUM ZONE”). The `ip` flag is also set on Engine 2's candle and sweep bounds (they carry `zfp_num` and no `tf`), which removes their F1-A / F1-C handling.

**B-22 · HIGH — Sweep zone as entry source; midpoint entry**
- Canon: E3C:135 — “- `STRUCTURAL_ENTRY_SOURCES = ['ORDER_BLOCK', 'LQZ']` (the only valid entry-anchor sources)”; E3C:178.
- Code: `_entries()` 56-61; `_build()` 262-272; `_bound_anchor()` 203-206.
- Deviation: a liquidity sweep zone is an entry anchor. WL enters at its middle; other shapes at its near edge, then its middle. DXY 2026-10-05 DX1 / DX3 / DX4; DXY 2026-05-18 DX1 / DX2 / DX6; golden week DX7. GP:67 lists “sweep-level entries” as an own idea.

**B-23 · MEDIUM — F1-A**
- Canon: E3C:186 — “> For OB SHORT only, lift the entry 1 pip above the supply zone's bottom edge. …”
- Code: `_entries()` 73-77, 82.
- Deviation: the lift is applied to a different object, the bottom of a lower-timeframe V1 order block nested in the anchor, and only if one exists. A short entered at the anchor order block itself (82) gets no lift.

**B-24 · MEDIUM — Law 3**
- Canon: GS:48 — “Entries are NEVER placed at 4H zone edges. They are placed at:”; GS:52 — “- **4H zones**: Directional bias + TP target ONLY. Never direct entry.”
- Code: `_first_anchor()` 198 ('240' allowed); `_entries()` 82.
- Deviation: nothing prevents a TS-1 entry on a 4H zone edge. Longs have no lower-timeframe refinement at all.

**B-25 · HIGH — Ladder-step option (b)**
- Canon: E3C:255 — “- OR (b) 1-2 pips INSIDE the CLOSE edge of the NEXT STEP away (opposite direction of the projected trade direction)”.
- Code: `_stops()` 96-99.
- Deviation: the stop is 1 pip OUTSIDE the BACK edge of the next rung (and of the two rungs after it). The sentence the code quotes (E3C:307) is the rocket SL doctrine.

**B-26 · HIGH — Which stop is chosen**
- Canon: E3C:285-286 — “confidence ≥ 0.6 → RR-tight (3p back edge)” / “confidence < 0.6 → safety (next-rung)”.
- Code: `_pick_stop()` 106-117.
- Deviation: the choice is made by category. Swing Scalp = tightest candidate in 4-9.5 pips; everything else = nearest “rung” stop up to 36 pips.

**B-27 · MEDIUM — Law 4 distances**
- Canon: GS:67 — “1. SL distance from entry: 5-15 pips (median 12 pips, NEVER above 25 pips for standard entries)”; GS:71 — “5. For deep HTF swings: SL can be 25-50 pips but MUST be behind 4H/8H liquidity shield”.
- Code: `_pick_stop()` 111-113, 116-117; `_env()` 27 (rungs = 1H bands only).
- Deviation: any stop from 4 to 36 pips is accepted behind a 1H band or a Fib pseudo-rung. There is no 4H / 8H shield test for stops above 25 pips.

**B-28 · MEDIUM — TP “midpoint”**
- Canon: E3C:319 — “4. If S/D + LQZ overlap exists (Earth+Fire convergence) → TP at zone **MIDPOINT** (strong reaction)”.
- Code: `_target()` 142, 162, 175, 180, 188.
- Deviation: the TP is the midpoint of the LQZ rung, not of the zone. Only a 4H non-BoM target zone gets the zone midpoint (139-140).

**B-29 · MEDIUM — Strong / weak edge**
- Canon: E3C:328 — “| STRONG (BoM, high confluence, fortress) | CLOSE edge (near edge) + 1-2 pip spread |”; E3C:329 — “| WEAK (virgin MoM, low confluence) | FAR edge (maximize catch) |”.
- Code: `_target()` 137-143, 182-189.
- Deviation: on breakout legs only a 4H BoM zone is “strong”; a 1H BoM target gets a rung midpoint, and no weak zone gets the far edge. On SS / R legs strength is `zfp_num < 30`, and Engine 2 target dicts carry `zfp`, not `zfp_num`, so every target on an R leg defaults to 40 = weak = far edge.

**B-30 · MEDIUM — RWL and WL targets**
- Canon: E3C:316 — “1. TP at the **opposing pressure** — nearest opposing supply/demand zone where the LQZ (liquidity) sits INSIDE the S/D zone (Earth+Fire convergence)”; E3C:320.
- Code: `_target()` 146-151, 152-166.
- Deviation: RWL targets the near edge of a V1 band picked by Engine 2 (C-13), else the midpoint of Engine 2's far bound with no LQZ-overlap test. WL targets the first unswept opposite sweep zone within `end ± 0.10·U`, then the pivot edge. Neither is the nearest opposing supply / demand zone.

**B-31 · HIGH — A TP when no opposing zone exists**
- Canon: E3C:1016 — “16. **NEW** — Honest Absence: SL_INVALID / TP_NULL / RRR_BELOW_FLOOR / no-entry-zone / no-structural-wall all yield NO EMISSION — never a fabricated level. …”; E3C:1047.
- Code: `_target()` 177-180.
- Deviation: with no to-zone the TP becomes the midpoint of whichever V1 rung is nearest to the leg's end, and that end is the arithmetic middle of the range when no IP zone holds spot (`e2_chain` 270, 286). Emitted: DXY 2026-04-20 DX2, 2026-06-08 DX3, 2026-07-13 DX2, 2026-10-05 DX3; EURUSD 2026-07-06 EU3.

**B-32 · HIGH — Refinement loop**
- Canon: E3C:378 — “refineSetup on SAME anchors (entry FIXED — re-anchor SL/TP only)”; E3C:379 — “sl = next-rung's reactionExtreme + Law-7 buffer”.
- Code: `_build()` 292-309.
- Deviation: the loop changes the ENTRY (up to three) and walks three TPs per entry. The stop is chosen once per entry and never re-anchored. No “REPAIRED” annotation.

**B-33 · HIGH — Reinforcement count, condition and placement**
- Canon: E3C:621 — “> **Phase 9 contract:** For each surviving HTF Swing setup of HIGH/GOD_TIER quality, generate 2–3 reinforcement entries at intermediate liquidity zones along the TP path.”; E3C:631; E3C:645; GS:60.
- Code: `_build()` 321-339.
- Deviation: at most one rocket, only when a BS trade spans more than one day, at the midpoint of the first rung beyond the Monday pivot (or the range's arithmetic middle). That rung can be a Fib pseudo-rung (DXY 2026-05-18 DX5, GBPUSD 2026-07-06 GB6). It is not a MoM zone, not a 1.382 / 1.618 level, not the far edge of an entry zone. WL / RWL / PRWL swings get none.

**B-34 · HIGH — Swing scalps**
- Canon: E3C:96 — “| SS (Swing Scalps) | Swing Scalps (both directions) | Scalp Stack (30m/15m/5m) | 4–8 swing scalps |”.
- Code: `_build()` 251-320; `_first_anchor()` 198; `_env()` 27.
- Deviation: one scalp per SS day, in the single direction Engine 2's alternation gives (C-07), anchored on 1H / 4H zones with 1H rungs. The 11 runs emit 1 to 3 per week.

**B-35 · LOW — Session and category vocabulary**
- Canon: E3C:567 — “| SWING_SCALP | London Open |”; E3C:569 — “| HTF_SWING | NY Mid |”; BE2 E3C:607; BE4 E3C:609.
- Code: `CAT` / `SESSION` 21-22; 337.
- Deviation: 'London' and 'NY' are not session windows. 'Reversal' is not a BE4 setup category. 'Ladder' is used as a shape.

**B-36 · LOW — Emission cap key and silent truncation**
- Canon: E3C:471 — “… cap key `(pair, anchorBucket, day)`, FIRST kept, rest drop `EMISSION_CAPPED` with logged reasons.”; E3C:857.
- Code: `_build()` 340-355; `build()` 220.
- Deviation: the key is (day, direction, exact entry step) and it runs after the chain was built, so later trades can stand on the TP zone of a dropped one. Setups beyond 11 are cut by list position with no log line (the limit itself is RUL:16, L-04).

**B-37 · LOW — Sweep-zone width**
- Canon: E3C:1027 — “| LSZ Zones (with bottom edge extension) | Phase 4 | §8.3 | SL ladder-steps model |”.
- Code: `e3_trades` 158, 270-272; `e2_chain` 105-112, 129; `e1_pine.generate()` 76.
- Deviation: every consumer uses level ± 0.05, while `e1_ip.levels()` builds the extended ± 0.10 zone. The extension is computed and then dropped.

## B — Supply / demand map (`e1_tool/e1_sd.py`)

**B-38 · HIGH — A strong move is a three-candle gap, nothing else**
- Canon: RUL:97-98 (L-37) — “Confirmed reading: the origin candle of every distinct 4H leg is a zone (BoM), every continuation base inside a leg is a zone (MoM); …”; NOTES:31 — “Look out for strong momentum moves in price (big fat candles - lots of pips)”.
- Code: `scan()` 35-39.
- Deviation: a zone exists only where the candles before and after a candle do not overlap. A leg that starts without that gap gives no zone. (The gap is an order-block validity test in NOTES:137 and L-38; GP:67 lists “"inefficiency gap" as the only strong move” as an own idea.)

**B-39 · HIGH — Mother-candle substitution**
- Canon: P452:645 — “Supply/Demand zones are constructed from the **SINGULAR candle that immediately precedes a strong directional move** — NOT from a cluster of candles, …”; P452:649 — “2. **Locate the SINGLE candle immediately before that move began.** This is the "origin candle."”
- Code: `scan()` 52-56.
- Deviation: when the candle before the move is an inside bar, the zone is taken from an earlier containing candle, up to three bars back. The candle after the zone candle is then an inside bar, which fails P452:663. 519 of 2,130 valid DXY zone-instances are built this way.

**B-40 · HIGH — Validity versus the mitigation table**
- Canon: P452:728 — “| 2X mitigated | Weakened | Context-dependent. Not weak but not strong. |”; P452:703 — “An unmitigated MoM in an opposing trend is WEAKER than a 2X mitigated BoM. …”; NOTES:147.
- Code: `valid()` 103.
- Deviation: one hard mitigation removes a zone from the map, BoM included, while any number of soft taps keeps it (174 valid DXY zone-instances have ≥ 3). Neither the P452 table nor the notes' one-time use is what is coded.

**B-41 · MEDIUM — “Soft” includes closes inside the zone**
- Canon: P452:719 — “| Soft Mitigation | Wicks tap zone edge, immediately rejected. Brief contact, no penetration. | Barely counts. 1X soft ~ unmitigated. |”
- Code: `scan()` 68-76.
- Deviation: a visit is hard only when a whole candle body lies inside the zone. A candle that closes inside it, or a body that crosses it, counts as soft.

**B-42 · MEDIUM — Scan and staleness windows on lower timeframes**
- Canon: P452:755 — “… a 1H zone from the prior week may be included …”; P533:1321 — “- 1H demand/supply zones from the prior 1-2 weeks that sit INSIDE the IP zone”; NOTES:107.
- Code: `SCAN_DAYS` / `STALE_DAYS` 18-19; `scan()` 29; `valid()` 109.
- Deviation: the 4H figures (60-day scan, three-week staleness) are applied unchanged to 1H, 30m and 15m.

**B-43 · MEDIUM — Width limit on pairs and lower timeframes**
- Canon: P452:742 — “- Zone wider than 0.40 DXY points (too broad to be actionable)”; GS:25 — “| 4H | 30-80 pips | 20-120 | Directional bias, TP target, major liquidity shield |”.
- Code: `valid()` 107; `zone_map()` 119.
- Deviation: the DXY-point limit is applied as 40 pips to EURUSD / GBPUSD and to every timeframe. 31 unbroken, structure-valid EURUSD 4H zone-instances exceed it over the 40 weeks.

**B-44 · MEDIUM — Refined merge**
- Canon: GS:614 — “… When a 15m zone overlaps with a 30m zone (within 5 pips), MERGE them into a single "Refined" zone with combined properties:”; GS:618 — “- Label = "15m Refined 30m"”; P452:697.
- Code: `zone_map()` 146-150, 156.
- Deviation: the merge needs BOTH edges within 5 pips. The merged kind is BoM if either is BoM (P452:697: “When in doubt, classify as MoM”). The drawn label is built from tf / state / kind and never shows “Refined”.

**B-45 · MEDIUM — Break of structure “by the anchor”**
- Canon: NOTES:140 — “It must create break of structure”.
- Code: `scan()` 80-90.
- Deviation: any later price action before the anchor that passes the prior swing counts (`far` keeps updating until the zone breaks). A zone with no prior swing in the 60-day window is accepted outright (89-90).

---

# C. Rules, thresholds and constants with no canon sentence or ruling behind them

## C — Engine 2

**C-01 · HIGH — Invented ZFP and score numbers on substituted zones**
- Ruling it conflicts with: RUL:94 (L-35) — “ZFP is shown as the prompt's RANGE (e.g. "5-15%"), never a single invented number.”; Rule 4 E2X:200.
- Code: `_bounds()` 86 (15 / 30 / score 6); `_sweep_bound()` 112 (15 / 6); `_target()` 125, 129, 136 (10 / 15 / 30 / 70); `_opposing_liquidity()` 165 (15 / 6); `build()` 223 (30), 231.
- What it does: these literals feed `failing` (196), `_after_bs()` (177-183) and Engine 3's strong / weak test. DXY 2026-05-11: a “1H (Mitigated 5x) | BoM” bound gets 15 → Hard-Wall class → WL+RWL. DXY 2026-03-02: a MoM bound gets 30 → R.

**C-02 · HIGH — Definition of the “4H storyline”**
- Canon the code cites: E2X:258 — “- **4H storyline tiebreaker**: When in doubt, the 4H storyline bias decides. The weekly trend is identified on the 4H — it takes days and weeks to complete.”
- Code: `storyline()` 20-27; used at `build()` 213-214.
- What it does: the bias is the type of the last gap-detected 4H BoM zone whose move passed a 2-bar swing in the 60-day scan, with no test that the zone still stands (it was already broken or hard-mitigated at the anchor in 5 of 40 DXY weeks). It decides the direction in 20 of 40 DXY weeks. No canon sentence defines the storyline this way.

**C-03 · HIGH — MoM-asymmetry direction rule**
- Canon the code cites: E2X:140 — “└── Then pierce through zone until reaching BoM Liquidity”; E2X:239; FA 7. Against it: E2X:145 (0 reactions → the zone-holds branch).
- Code: `build()` 207-212; `_mom()` 168-170 (logged as D-28).
- What it does: “exactly one bound is a MoM candle zone → the breakout goes through it”. It is in no table. It reads only substituted candle bounds (an IP bound that Engine 1 classifies MoM is ignored), covers 1H as well as 4H zones, and decides 15 of 40 DXY weeks.

**C-04 · MEDIUM — Default direction**
- Canon: none. Rule 7 E2X:203 asks that a resolution direction be justified.
- Code: `build()` 215-216.
- What it does: with no storyline the breakout direction is set to 'down'.

**C-05 · MEDIUM — Numeric confidence scale and fixed tier assignment**
- Canon: the tables give words only (E2X:50-57, :78-93, :99-111); E2X:169 gives only the 25% stop.
- Code: `CONF` 15; `build()` 257-259.
- What it does: HIGH = 0.80, MODERATE-HIGH = 0.65, MODERATE = 0.50 … and a fixed three- or four-step tier list. Not in `memory/03_DECISION_CHAIN.md`.

**C-06 · MEDIUM — History window and “two piercing sessions”**
- Canon the code cites: FA:576 — “AFTER 2 STRONG PIERCING SWING MOVES — EXPECT 1-2 FULL DAYS OF HTF CONSOLIDATION. …”
- Code: `current_shape()` 52, 57, 60-62.
- What it does: looks at the last four sessions only and reads “two strong piercing swing moves” as “the last two daily candles each classified BS / PBS / WL by the B-02 test”.

**C-07 · HIGH — Direction of each SS swing by parity**
- Canon: for an SS day the direction is “range” (E2X:173 — “(b) assign the directional bias (up/down/range)”).
- Code: `build()` 299-306.
- What it does: the direction of every SS leg is set by counting SS days back from the breakout day (odd → toward the far bound). This alone decides whether Monday's scalp is long or short.

**C-08 · MEDIUM — Intraday timing constants**
- Canon: Rule 9 E2X:205; Rule 4 E2X:200.
- Code: `build()` 306, 311-313, 320, 325-326, 330, 335, 338 (d0 + 7 h, d0 + 14 h, d0 + 10 h, d1 − 3 h, d1 − 4 h); `e3_trades.pine()` 370 (minimum 6 h).
- What it does: fixed hours place the end of every leg inside its day. They set the yellow path and the time span of each Engine 3 box.

**C-09 · HIGH — Computed levels that are not zone edges**
- Canon: Rule 1 E2X:197; E3C:1015 — “15. **NEW** — R3 Law: E3 NEVER overrides E1/E2 data; never fabricates levels (every anchor traces to E1 zone + E2 shape day)”.
- Code: `build()` 270 and 286 (`mid = (f_edge + c_edge) / 2`, `piv_far = mid` when no IP zone holds spot); 267-268 (`spot ∓ 0.3 * U` when a bound is missing); 289 (a zero-length leg gets direction 'down').
- What it does: legs, day boxes and Engine 3 targets end at the arithmetic middle of the range in the 27 of 40 DXY weeks without a pivot zone. The ±30-pip edge and the zero-length direction did not fire in the 40 weeks at this commit; they are live code.

**C-10 · MEDIUM — Path rules of the BS and WL days**
- Canon the code cites: E2X:322 (6.10); E2X:215 — “| WL | Zone ZFP < 20% (Hard Wall) | Origin zone (return) | Rejection zone < 20% | < 1 session |”.
- Code: `build()` 313 (the first BS leg ends at `mid`), 316-320, 323-326.
- What it does: a continuation day stops at the bound's near edge; the whiplash returns to the pivot's breakout-side edge. Neither end-point is stated in the canon.

**C-11 · MEDIUM — Grade for the candle-zone bound pool**
- Canon the code cites: P452:753 — “… Criteria: 2-3 candle base on 1H preceding >= 0.3 DXY move lasting >= 1 trading day.”
- Code: `_bounds()` 90-92.
- What it does: the 0g nested-precision criterion for 1H zones is reused, without “≥ 1 trading day”, as a strength grade for both 4H and 1H bounds, with a fallback to every zone when none passes. The grades L-37 names for 4H are 0.5 / 3 days and 1.0 / 5 days.

**C-12 · MEDIUM — Sweep levels joined into the target**
- Canon the code cites: P533:1269 — “0.45d. **Cross-reference with 4H BoM zones from Step 0f.** When a liquidity sweep zone overlaps with a 4H BoM demand/supply zone:”.
- Code: `_target()` 143-147.
- What it does: any target (IP zone, 1H zone, sweep target) is stretched to sweep levels up to 0.15 beyond its far edge and flipped to always-reacting, ZFP ≤ 15. The canon speaks of overlap with a 4H BoM zone; 0.15 is the IP clustering distance.

**C-13 · MEDIUM — “Opposing liquidity” band**
- Canon the code cites: E2X:139 — “└── Consolidation ends in price retesting opposing liquidity”.
- Code: `_opposing_liquidity()` 151-165; `build()` 277-279, 312-313.
- What it does: the retest is made to end at the next V1 1H rung or 4H band “wholly beyond the far bound's own entry rung” and within 0.15 of its far edge. The canon names no band-selection rule. The docstring (154) justifies it with the operator's golden-week prices.

**C-14 · MEDIUM — Plan for a breakout running at the anchor**
- Canon the code cites: E2X:66 — “| BS → RWL → SS → BS | HIGH | Complete false breakout cycle. Second BS often succeeds. |”.
- Code: `build()` 224-234, 244, 332-336 (logged as D-29).
- What it does: the running BS is given the near bound itself as target, and the week always ends with a second BS in the same direction on Friday, also after R (“BS → R → SS → BS” is not a 6.3 chain). The bound just classed as rejecting is the one forecast to fail.

**C-15 · LOW — Gaps filled in `_after_bs()`; tie rule**
- Canon: E2X:101-104 has no row for 40-60% and none for “no target”.
- Code: `_after_bs()` 175-176, 183; `build()` 195-197.
- What it does: no target → R / MODERATE; 40-60% → R / MODERATE; when both bounds fail the floor wins.

**C-16 · LOW — Padded days drawn as “SS”**
- Canon: E2X:173 (each day gets its predicted shape).
- Code: `build()` 251-253; `pine()` 363-366.
- What it does: days after the chain end are declared to “carry no designation”, yet they are drawn as SS day boxes with a label (12 day-boxes over the 40 DXY weeks).

## C — Engine 3

**C-17 · HIGH — Zone-internal Fibonacci levels promoted to liquidity rungs**
- Canon the code cites: GS Law 5 and Step 0.6. GS:87 — “| 0.382 | Primary entry (retracement) | 8/38 images |”; GS:68 — “2. SL is placed OUTSIDE the nearest liquidity shield zone”.
- Code: `_env()` 30-36; used by `_stops()` 96-99, `_target()` 136, 141-142, 160, 173-175, 178-180, 186-188 and the reinforcement block 325-333.
- What it does: 0.382 / 0.5 / 0.618 / 0.786 of any 4H / 1H candle zone holding no V1 band become zero-width “rungs” that serve as stop shields, TP levels and rocket entries, never as entries. Step 0.6 concerns IP zones and names 0.382 / 0.618 only.

**C-18 · MEDIUM — Sweep-entry stop and sweep clustering**
- Canon the code cites: E3C:307 (rocket SL doctrine, “1-2 pips OUTSIDE THE BACK EDGE”).
- Code: `_stops()` 90-92; `_build()` 265-272; `e2_chain._sweep_bound()` 108-112.
- What it does: the stop is 1.3 (then 2.0) pips beyond the extreme of a cluster formed by chaining sweep levels that lie within 0.05 of one another.

**C-19 · MEDIUM — 4 pips as a hard minimum stop**
- Canon: E3C:291 and E3C:309 describe the reaction-extreme fallback and the measured golden stops (“4-9.5 pips”).
- Code: constants 16; `_pick_stop()` 110-117; 296; 334.
- What it does: every stop candidate closer than 4 pips is discarded, and 4-9.5 is used as an acceptance band for ladder-step stops.

**C-20 · MEDIUM — “Consumed” zones**
- Canon: none; against E3C:347 (only real mitigation lets price pass).
- Code: `_target()` 168; `_build()` 319.
- What it does: a zone used as an anchor by an earlier forecast trade of the chain is skipped as a TP for later trades. A fill that has not happened is treated as mitigation.

**C-21 · MEDIUM — Anchor repair after a rejection**
- Canon: none.
- Code: `_build()` 312-314, 255-256.
- What it does: the next leg is anchored at the first TP candidate of the rejected leg; if that is the opposing-liquidity band, at Engine 2's far bound; if there is none, the “first trade” rule is re-run against Monday's spot in mid-week.

**C-22 · MEDIUM — Collision retry on pairs only**
- Canon the code cites: E3C:766 — “# usedEuAnchors + alt-retry with excludedAnchorIds on collision”; E3C:767 — “# D11 doctrine: Δ≤15p = one signal shares; beyond = distinct must spread”.
- Code: `_build()` 281-291 (logged as D-31).
- What it does: on EURUSD / GBPUSD an entry step already used that day in that direction is replaced by the near edge of the next rung beyond it. No mirror of a DXY setup exists for this to belong to; DXY gets no such retry. EURUSD 2026-04-20 EU4.

**C-23 · LOW — Candidate counts and tolerances**
- Canon: none.
- Code: 98 (next three rungs), 76 (one nested block), 67 (three overlapping rungs), 160 / 186 / 325 (2-pip rung matching), 155 (0.10·U window).

**C-24 · LOW — F1-D inset on WL**
- Canon: E3C:196 — “`RWL_BOUNCE_INSET_PIPS = 0.2` — LONG bounce entries pulled INSIDE the rung CEILING by 0.2 pips. …”
- Code: `_entries()` 55; `_build()` 276.
- What it does: the inset is applied to WL legs as well as RWL.

**C-25 · LOW — Order validity over the whole SS run**
- Canon the code cites: E3C:96 (“both directions”).
- Code: `build()` 228-232; `pine()` 370.
- What it does: an SS setup is declared valid for the whole run of SS days. It is stored on the setup only; `pine()` does not draw it.

**C-26 · LOW — Rendering filters**
- Canon: none.
- Code: `e1_pine.generate()` 29-30, 42, 50, 84.
- What it does: rungs and order blocks are drawn only inside the prior-week range ± a 10-day average range, while Engine 3 uses all rungs. Engine 2 uses IP zones beyond rank 6 that are not drawn (a bound or pivot is undrawn in 2 of 40 DXY weeks).

## C — Supply / demand map and V1 harvest

**C-27 · HIGH — Origin-candle walk-back**
- Canon: P452:649 (the single candle immediately before the move).
- Code: `scan()` 43-51 (logged as D-21).
- What it does: candles whose body is ≥ 50% of their range in the move's direction are skipped backwards as “part of the move”. The 0.5 is in neither the canon nor the notes.

**C-28 · MEDIUM — Two-bar swing fractal**
- Canon: none gives a bar count (logged as D-13).
- Code: `scan()` 31-32.
- What it does: a swing = the extreme of its bar and two bars each side. It decides every break-of-structure test, hence validity and BoM / MoM.

**C-29 · HIGH — Same-type overlap removal**
- Canon the code cites: P452:699-703 (a strength hierarchy). The canon forbids only supply / demand overlap (P452:655).
- Code: `zone_map()` 125-134.
- What it does: of overlapping same-type zones on one timeframe one is kept (BoM, then fewer taps, then fresher). 257 DXY and 336 EURUSD zone-instances are absorbed over the 40 weeks; `memory/05_JOURNAL.md`:380 records one of the operator's own golden-week boxes removed this way. The `reactions` counter it increments is never read.

**C-30 · HIGH — BoM / MoM by type alternation**
- Canon: P452:694 — “… Only the initial origin counts as BoM. Continuation bases within the move are MoM. …”; P452:697.
- Code: `scan()` 93-97 (logged as D-23).
- What it does: a leg ends whenever an opposite-type gap zone that passed a 2-bar swing appears, so after any such pullback the next continuation zone is BoM again. The first zone in the 60-day window is BoM by default. Engine 2 targets and “always reacts” depend on this label.

**C-31 · MEDIUM — “Own side of spot” test**
- Canon: none.
- Code: `valid()` 105-106.
- What it does: a standing zone that contains spot at the anchor is dropped (12 DXY and 15 EURUSD zone-instances over the 40 weeks).

**C-32 · MEDIUM — FX liquidity-band thickness rebuilt in Python** (`e1_v1.py`, outside the five listed files; logged as D-24)
- Ruling: V1 is taken as data, unedited (R-30). Sealed file :1203 — `lqzThick   = math.max(lqzThickE * nz(ta.atr(14), 0.0), nz(lqzMinTick, 0.0))`.
- Code: `e1_v1.harvest()` 47-55.
- What it does: every FX band returned 0.01 thick is rewritten to exactly 0.35 × ATR(14). V1 draws max(span, 0.35 ATR), so merged bands whose span exceeds 0.35 ATR come out thinner than V1 would draw them. These bands are Engine 3's rungs on EURUSD / GBPUSD.

---

# D. Temporal-anchor and hardcoding

Checked with no finding: the `plutus.py` path (e1_pine.run → e1_ip.build / e1_v1.harvest_all / e1_sd; e2_chain; e3_trades) reads bars only through `D.closed()` and the helpers built on it (`daily`, `weekly`, `forming`); all 432 sources in the 40 sidecar files are stamped at or before their anchor; the five audited files hold no price literal.

**D-01 · MEDIUM — The anchor guard and the pre-commit hook do not cover the tool**
- Ruling: RUL:18 (L-05) — “… That is a hard mechanical constraint. Put whatever git hooks and git logs need to be put in so that you cannot violate this."”; CLAUDE.md:16 — “… Nothing after the anchor may feed a forecast. Enforced by `tools/anchor_guard.py` + git pre-commit hook.”
- Code: `tools/git-hooks/pre-commit` 5 (`grep -E '^indicator/.*\.pine$'`); `tools/anchor_guard.py` `main()` 138.
- Violation: only `indicator/*.pine` is checked. `e1_tool/*.py` and `e1_tool/out/*.pine` are never inspected, so the temporal rule in the tool rests on the habit of calling `D.closed()`.

**D-02 · MEDIUM — Post-anchor bars read inside `e1_tool`**
- Ruling: CLAUDE.md:16 (as above); GP:45.
- Code: `e1_outcome.facts()` 9, 12; `e2_shapes.actual()` 153; `e3_setups.simulate()` 200. Each calls `D.bars()` and keeps `b0 <= time < b0 + 7 days`.
- Violation: three modules of the tool package read the forecast week's own candles (outcome descriptions, fill simulation). None is imported by `plutus.py`, `e1_pine.py`, `e2_chain.py` or `e3_trades.py`.

**D-03 · LOW — Week literal and oracle read in `e3_trades.py`**
- Ruling: CLAUDE.md:15 — “- **No hardcoded values.** No price literals, no per-week constants. …”; GP:46.
- Code: `e3_trades.py` `__main__` 390-398 (`if monday == '2026-07-06'`, opens `context_management/oracle/golden_week.json`).
- Violation: a week-specific branch in an engine module loads the operator's golden-week trades and prints distances. It does not feed the setups.

**D-04 · LOW — Default week literals**
- Ruling: CLAUDE.md:15.
- Code: `e1_synth.py` 166; `e1_zones.py` 202 (`'2026-04-20'`).
- Violation: a fixed week is the default argument of two tool modules.

**D-05 · LOW — Oracle prices in a tool docstring**
- Ruling: GP:46 — “Oracle numbers are for comparison only and never appear in tool code.”
- Code: `e2_chain._opposing_liquidity()` 154 (“DXY 4H band 101.245-101.305 (RWL TP 101.24, BS short 101.235), EURUSD 1H rung 1.13902-1.1393 …”).
- Violation: the operator's golden-week levels are written into the engine file as the justification of a rule (C-13). They are not executed.

---

# Addendum — working-tree edits seen at 14:35 UTC, uncommitted, not counted

`e1_tool/e1_pine.py` gained `reach(X, E2)` and `plutus.run()` passes it to `generate()`: Engine 1 zones, sweep zones, strike lines and 4H bands outside the envelope of the Engine 2 day map (extended to the first mapped zone beyond each end) are moved behind a new input `show_far`, default false. The code cites GS Law 2 / Law 7 and L-28. GS:152 is about where setups are generated (“3. Only generate setups at zones within the expected range for that day's shape”); it says nothing about hiding Engine 1 zones, and this makes what Engine 1 shows by default depend on Engine 2's forecast. Not audited line by line.

---

# Totals

| group | HIGH | MEDIUM | LOW | total |
|---|---|---|---|---|
| A. canon steps with no code | 22 | 25 | 5 | 52 |
| B. contradictions | 22 | 19 | 4 | 45 |
| C. inventions | 9 | 17 | 6 | 32 |
| D. temporal anchor / hardcoding | 0 | 2 | 3 | 5 |
| all | 53 | 63 | 18 | 134 |
