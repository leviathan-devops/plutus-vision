# E3_ALGO — Engine 3 (Trade Setups) implementable digest, CORRECTED spec

Extracted first-hand. Nothing here is invented. Where the source is silent the entry says UNKNOWN; where sources disagree the entry says CONFLICT and quotes both sides. The corrected spec wins every conflict with the original; conflicts INSIDE the corrected spec are not resolved here, they are listed (section 8.B) for an operator ruling.

**Citation convention**
- `C:n` = `/home/user/plutus-vision/canon/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md` line n (1685 lines; read in full).
- `O:n` = `/home/user/plutus-vision/canon/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md` line n (read 2058-3260 in full: Part VI-B, VII, VII-B, VII-C, VIII). CONTRAST ONLY.
- `T:n` = `/home/user/inputs/handover/PLUTUS_VISION_CONTEXT_HANDOVER/03_HOST_BIBLES/TTE_GOLDEN_STANDARD_COMPLETE_REFERENCE.md` line n (747 lines; read in full).
- `BRIEF` = the operator count rule relayed in this extraction task ("max 1-2 real moves per day, 6-10 per week, never more than 11 per pair per week"). It is NOT present in C, O or T (grep of `context_management/` and the handover found no source line).
- "Derived" = arithmetic or ordering consequence of quoted rules, not a source statement.

---

## 0. Read this first

0.1 **Authority.** C "is a SURGICAL REPLACEMENT of the broken E3 sections of the original v5.3.3 prompt. E1 and E2 are PRESERVED VERBATIM from the original. Only the E3 sections (Parts VI-B, VII, VII-B, VII-C, VIII) are replaced" (C:6). The original Parts VI-B, VII, VII-B, VII-C, VIII are DELETED (C:30-35). Part IX (Pair Translation) and Part X (Pine Script) stay "byte-identical" (C:39) and were not in scope of this digest.

0.2 **What E3 is.** "E3 is NOT a trade generator. E3 is a classification + precision alignment engine that consumes E1's zone map + E2's storyline designation and produces TradeSetups — each one anchored to a specific E1 zone ID + E2 shape day, never fabricating its own rules" (C:74).

0.3 **R3 Law.** "E2 DESIGNATES, E3 OBEYS. Every order leg's session bracket comes from the E2 session label. Every anchor traces to an E1 zone ID + an E2 shape day. E3 never overrides E1/E2 data (the R3 law)" (C:77).

0.4 **Single responsibility (the whole engine in one sentence).** E3 "takes each E2 ShapeDayZone day (which zone, which side, which day/session, how confident, what shape) as authoritative and resolves only the executable geometry — the entry at the anchor's internal-LQZ near/deep edge, the SL at the ZR-1 operative-defense ladder step (or the golden reaction-extreme fallback), the TP at the Law-14 opposing-rung walk — then proves the result through the 3D audit, the RRR repair on the same anchors, the day-native CS-1 and narrative guards, the per-anchor emission cap, the dedup identity, and the session-bracketed fill simulation, never re-designating, never converting prices, never inventing levels" (C:80).

0.5 **Honest absence.** "SL_INVALID / TP_NULL / RRR_BELOW_FLOOR / no-entry-zone / no-structural-wall all yield NO EMISSION — never a fabricated level. The 90% win-rate target depends on what the code REFUSES to emit" (C:1016).

0.6 **Phase count.** C declares an "Explicit canonical 12-Phase pipeline" (C:48) and "12 phases" (C:1671). The body numbers Phase 0, 1, 2, 2.5, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. Reading used here: Phases 1-12 are "the 12", with Phase 0 (universe classification) in front and Phase 2.5 (entry timing) as a sub-phase. C never states this mapping: UNKNOWN which 12 are meant.

0.7 **Functions named but not defined in C** (their bodies are UNKNOWN from the three sources): `computeSL_LMV`, `computeGoldenSL_V452` (only a 4-line summary, C:290-295), `computeLmvTP` (7-line summary, C:333-344), `computeMirrorTP`, `strengthDrivenRungTp`, `bridgedLmvZone`, `refineSetup`, `selectSession`, `computeReachTime`, `deferSessionBy30Min`, `reAnchorMirror`, `retranslateSetup`, `structurallyValid`, `narrativeAligned`, `validateInverseCascadeDirection`, `validateKeptCascadeDirection`, and the audit check lists P1-P8 / C1-C6 / T1-T8 (named only, C:826-828). Terms used but undefined: `liquidityScore` (C:574-576), `anchorBucket` (C:471), `util` (C:292), fuel `INTACT` / `ABSORBED` (C:258-259), "significance walk" ranking (C:335), `vz.confidence` "visual zone confidence from VLM or fallback" (C:393).

---

## 1. The phases in order

Inputs to the whole engine: E1 `ZoneMapSnapshot` (C:1486-1498: `ipZones`, `sdZones`, `lqzZones`, `spot`, `lqzMatrix`, `lmvTable`, `ladder`, `narrative`) and E2 `CascadedShapeChain.days: ShapeDayZone[]` (C:1579-1603). Output: `E3Output` (C:1470-1480).

### Phase 0 — Setup Universe Classification (C:88-107)
- **In:** E2 day-by-day shape decomposition. **Out:** the valid setup types per day.
- **Rule:** the Setup Universe Matrix, section 4.1 below (12 rows, C:96-107).

### Phase 1 — Day-Level Bridge / WorkingDayMap (C:109-125)
- **In:** E2 "`Day-by-Day Decomposition` block (Mon–Fri shape + direction + key zone + triggers + confidence)" (C:114).
- **Out:** "`WorkingDayMap[]` — array of 5 entries, one per trading day, each carrying `{dayIdx, day, shape, direction, keyZoneId, keyZoneType, supplyZoneId, demandZoneId, deepDemandZoneId, dayOpenSpot, session, confidence}`" (C:115). Type at C:1241-1254 (`confidence` is 0-1; `dayIdx` 0-4).
- **Algorithm (8 steps, C:118-125):** steps 1-5 copy Mon..Fri into index 0..4. Step 6: "Apply Trading Speed Adjustment: for each day, if E2's confidence < 65%, propagate the shape to the next day (i.e. the predicted shape "spills over" — today's move often becomes tomorrow's move per the Trading Speed Rule)" (C:123). Step 7: "Validate: 5 entries present, no `null` shape, every `keyZoneId` resolves to an E1 zone in the ZoneMapSnapshot" (C:124). Step 8: emit.
- Note: C says this section is "MERGED INTO Phase 7" as its algorithmic core while Phase 1 "only consumes E2's day-by-day output" (C:111).

### Phase 2 — Zone Selection + Market Structure (C:127-171)
- **Contract:** "For each `(WorkingDay, zone)` pair where the zone is on the correct side of spot per the day's direction, generate a trade candidate. Reject candidates failing the structural gate" (C:129).
- **Direction-appropriate anchor (CRITICAL):** "The LONG mirror → the demandZoneId. The SHORT mirror → the supplyZoneId. The keyZoneId is the fallback. NEVER anchor LONGs at SUPPLY — wrong side, hard error (never silent emission)" (C:132).
- **Entry-anchor sources:** "`STRUCTURAL_ENTRY_SOURCES = ['ORDER_BLOCK', 'LQZ']` (the only valid entry-anchor sources)"; "IP zones (source==='PILLAR') are confluence/ZFP/context + SL/TP rungs — NEVER entries"; "IP classification MUST be `'CONFLUENCE'` — NEVER `'MoM'`"; "Mirror anchor-search skips `source==='PILLAR'`" (C:135-138).
- **Zone selection threshold:** "Zone selection (confluence ≥ 7) generates trade candidates" (C:1022). Zero-tolerance rule 1: "No trade without Tier 1 or Tier 2 POI" (C:1001).
- **Freshness gate (evaluated AT BATTLE TIME):** "(a) index `i > 2` skipped — 4th+ battle is DEPLETED/consumed structure (recurrence ladder UM 100% / 1x 80% / 2x 50% / 3x+ TP-only; trading the 6th touch is the DXY=39 slop). (b) any prior pierced event = VIOLATED terminal: level closed through, never an entry again. Admissibility evaluated on the group earliest clean battle" (C:150). The heading calls it a "4-Stage Freshness Gate" but only (a) and (b) are given.
- **Zone pressure lifecycle (C:153-165):** VIRGIN (0 battles) "the strongest (BoM: 100% reaction; MoM: the DEATH ZONE for counter-trend)"; ACTIVE-1 (1) "~80% reaction rate"; ACTIVE-2 (2) "~50% reaction rate"; DEPLETED (3+) "TP target ONLY"; FORTRESS (4+ strong) "95% direction flip"; BROKEN (VIOLATED) "the terminal state — the level closed through — never offers an entry again — the role reversal (the broken support = the new resistance)".
- **MoM rules kept by name:** rule 6 "BoM/MoM ENFORCEMENT (no entry at MoM unless ALL 4 exceptions)" (C:1006); rule 12 "MoM Zones = Ladder Steps ONLY (no reversal entries at MoM, EVER — supersedes Rule 6 for REVERSAL entries; MoM still CONDITIONAL for trend-aligned with all 4 exceptions)" (C:1012); "4H MoM One-and-Done | Phase 2 | Scalp-only at 4H MoM" (C:1032). The 4 exceptions are listed only in the deleted original: "(a) ≥1 prior strong reaction, (b) trend-aligned, (c) key S/R confluence, (d) opposing liquidity weak or absent" (O:2217).
- **Reversal sub-step (ALL THREE required, C:168-171):** "1. Break of Structure (BoS) — price breaks the most recent opposing swing (lower-high for bullish reversal, higher-low for bearish) 2. Flip — the broken swing's role flips (resistance→support for bullish; support→resistance for bearish) 3. Retest — price retests the flipped level from the new direction; entry at the retest".
- **Direction validation, 6-check (C:1084-1095):** 4H Trend; BoM Alignment; Liquidity Sweep; Zone Failure; Macro Shape; Counter-Trend. "if 4+ of 6 disagree with the proposed direction → REVERSE the direction (or REJECT if no reversal pattern exists)" (C:1093). Position size: "If `counterTrendRisk = HIGH`, position adjustment = Quarter (25% of normal size); if MODERATE, Half (50%); if NONE, Full (100%)" (C:1095). C does not assign this check to a numbered phase (the data model comment says "Phase 8.1", C:1302).
- **Out:** candidates `{WorkingDay, anchor zone, direction}`.

### Phase 2.5 — Entry Timing, 1-2-3 Retest (C:1148-1160)
| Retest Count | Valid Entry | Description (C:1152-1155) |
|---|---|---|
| 0 (Virgin) | Scalp only | "First test — liquidity not yet accumulated" |
| 1 | Scalp + Confirmation | "Second test — early confirmation" |
| 2 | Swing entry valid | "Third test — enough Earth accumulated to fuel swing move" |
| 3+ | TP target only | "Zone depleted — will pierce" |

Zero-tolerance rule 7: "1-2-3 Retest Timing (no swing entry before 3rd retest; no scalp entry before 2nd retest)" (C:1007). See CONFLICT B-8.

### Phase 3 — Entry Identification + Fib anchoring (C:173-229)
- **Contract:** "Resolve the exact entry price for each candidate setup from Phase 2" (C:175).
- Rules: section 3.1 below.

### Phase 4 — Confluence Stack + SL + TP + RRR (C:231-386)
- "entry determines SL determines TP determines RRR" (C:233).
- 4.1 Confluence stack (7 layers): section 3.5. 4.2 SL: section 3.2. 4.3 TP: section 3.3. 4.4 RRR + floor + 3-attempt repair: section 3.4.

### Phase 5 — Confidence Scoring + Quality Classification (C:388-424)
- Section 3.5 below.

### Phase 6 — Multi-Setup Architecture (MANDATORY) (C:426-471)
- **In:** "the list of individually-constructed setups from Phases 2–5". **Out:** "`TradeSetupMatrix` + `TradeFlowChain[]` + `SetupConflict[]`" (C:431-432).
- **6.1 Matrix row:** `{setupId, day, pair, direction, category, quality, entry, sl, tp, rrr, confidence, session, shapeTrigger, anchorZoneId, setupCategory, dayCatalysts, tradeFlowRef}` (C:438-439).
- **6.2 Trade Flow Chains (Law 27):** "1. Sort all setups by `(day, session, entry)` ascending 2. For each setup N, look for setup N+1 whose entry equals (within 3-pip tolerance) setup N's TP 3. If found, link them: `setupN.chainsTo = setupN+1.setupId` 4. Emit the chain: `CHAIN-${rootId}-D${depth}` (max depth = 3 per Law-13)" (C:447-450). Shape links: "BS → R: TP of BS becomes R entry zone"; "BS → WL"; "BS → RWL"; "WL → RWL"; "SS → BS: Range boundary break becomes BS entry" (C:453-457). "Max 3 trades per chain (Law-13 ceiling RRR ≤ 15). TP of trade N = entry of trade N+1" (C:1121).
- **6.3 Conflicts** — "For each pair of setups on the same day, same pair, same session: If `direction` is opposite AND entries within 15 pips → CONFLICT (only the higher-confidence one survives). If `category` is same AND entries within 5 pips → DUPLICATE (dedup by anchor-zone-id; keep first). If both setups reference the same `anchorZoneId` → dedup by anchor bucket + day identity" (C:461-464).
- **Emission cap:** "`MAX_MIRRORS_PER_ANCHOR_PER_DAY = 1` (the GU-x10 destroyer) — cap key `(pair, anchorBucket, day)`, FIRST kept, rest drop `EMISSION_CAPPED` with logged reasons" (C:471). Count rules: section 3.7.

### Phase 7 — DAY Assignment + Session Window + Anchor Hit Window (C:473-596)
- **Contract:** "For each surviving setup, assign the `(DAY, SESSION_WINDOW, SHAPE_TRIGGER, SETUP_CATEGORY, ANCHOR_HIT_WINDOW)` 5-tuple" (C:475).
- **7.1 `assignDay(setup, workingDayMap, economicCalendar)` (C:483-554):**
  1. `anchorZoneId = setup.anchorZoneId`.
  2. `matchingDays` = working days where `keyZoneId`, `supplyZoneId`, `demandZoneId` or `deepDemandZoneId` equals `anchorZoneId`.
  3. none → abort `NO_DAY_ASSIGNABLE`, return REJECTED.
  4. exactly one → `setup.day`, `setup.shapeTrigger` from it; "continue to Phase 7.2".
  5. several → 5a keep days whose shape is in `categoryShapeMap[setup.category]`: `HTF_SWING: ['BS','WL','PBS','RS','RWL','PRWL']`, `SWING_SCALP: ['SS','SS(DWL)','WLS','R']`, `REINFORCEMENT: ['BS','WL','R','RWL']`, `TRANSITION: ['SS→BS']` (C:508-513); one left → assign. 5b several left → highest `confidence` first.
  6-7. For each red-folder event on `setup.day` that `affectsPair(setup.pair)`: `setup.sessionWindow = deferSessionBy30Min(setup.sessionWindow, evt.time)`; push catalyst text.
  8. "if matchingDays[0].confidence < 0.65 && setup.day !== 'Friday': setup.day = nextDay(setup.day)" (C:537-538).
  9. `setup.sessionWindow = selectSession(setup.day, setup.category, setup.pair)`.
  10. `setup.anchorHitWindow = computeAnchorHitWindow(setup, workingDayMap)`.
  11. cascade validation if `cascadeSource` is `'DXY→EU'` or `'EU→GU'`.
  12. emit.
- **7.2 Session window:** section 3.6.
- **7.3 Anchor hit window (C:581-595):** `distance = |spot - setup.entry| / pip`; "Shape→distance heuristic (from 38-trade forensic): SS ±5-30 pips, BS 30-100, WL 50-200, RWL 30-100, R 10-50"; `expectedReachTime = computeReachTime(shape, distance, dayIdx)` (UNKNOWN body); window = `{start: dayStart + expectedReachTime - 30min, end: dayStart + expectedReachTime + 60min, confidence: 0.7}`.

### Phase 8 — Blind-Execution Labeling BE1-BE12 (C:598-617)
- "Every surviving setup MUST carry the 5 blind-execution labels. No label = setup REJECTED" (C:600).
- BE1 DAY label; BE2 SESSION WINDOW ("London Open / London Mid / NY Overlap / NY Open / NY Mid / NY Close"); BE3 SHAPE TRIGGER; BE4 SETUP CATEGORY ("HTF Swing / Swing Scalp / Reinforcement / Transition / Breakout Search"); BE5 Weekly Execution Calendar; BE6 "entry/SL/TP each carry day + session annotation"; BE7 no real-time chart analysis needed; BE8 Day Catalysts; BE9 "Reinforcement entries have parent trade reference | `parentSetupId` field populated"; BE10 all 5 days covered "or explicit "No qualifying setups — [reason]""; BE11 "Profit Taking Law documented | "Close ALL positions by NY close Friday" per pair"; BE12 "Day predictions include +1 day where confidence < 65%" (C:606-617).

### Phase 9 — Reinforcement Architecture 8R.0-8R.10 (C:619-721) and Scaled Entry (C:1056-1080)
- **Contract:** "For each surviving HTF Swing setup of HIGH/GOD_TIER quality, generate 2–3 reinforcement entries at intermediate liquidity zones along the TP path" (C:621). Rules: section 5.

### Phase 10 — Cascade Mirror DXY → EU → GU (C:723-800)
- **Contract:** "For each DXY source setup, generate the corresponding EU mirror setup (inverse direction). For each EU mirror setup, generate the corresponding GU mirror setup (kept direction)" (C:725). Rules: section 6.

### Phase 11 — Master Trade Setup / Avatar State (C:802-816, C:699-714)
- **Contract:** "For each HTF Swing setup of GOD_TIER quality, attempt to construct the Avatar State (E + FLR) by adding Fibonacci Liquidity Rockets at Fib-confirmed Liq zones" (C:804). Rules: section 2.5.

### Phase 12 — 3D Refinement Audit + Final Validation (C:818-879)
- **Contract:** "For each surviving setup (including reinforcements and cascade mirrors), run the 3D refinement audit. Discard or repair failing setups" (C:820).
- **12.1 `auditSetup3D`** (runs "when translatedDays present", C:822): "P1-P8 (Price audit): validate entry/SL/TP against LMV rungs"; "C1-C6 (Cascade audit): validate direction + zone class + role translation"; "T1-T8 (Temporal audit): validate day/session/anchor hit window"; "REJECT_GENUINE: hard-discard"; "RE_TRANSLATE loop — INVERSE lane ONLY"; "KEPT lane DEFERS (no safe BoM-wall substrate — drift 1.33970→1.32822 measured)"; "B1.5: NEVER re-anchor E2-designated — RE_TRANSLATE + e2Designated → E2_DESIGNATION_HELD flag, skip re-anchor, SL/TP repair on E2 zone only"; "R2 doctrine when RRR < floor: refineSetup SAME anchors (entry/SL/TP placement only), up to 3 surgical repair attempts, repaired setup emits with wrench annotation, failed repair → hard-reject with full 3-attempt audit trail (D36) as discard reason" (C:825-847). The individual checks P1..P8, C1..C6, T1..T8 are UNKNOWN.
- **12.2 `checkMirrorFloorV45`:** "Floor: RRR ≥ 2.5"; "Session bracket valid (E2-designated session window)"; "SL envelope (within GOLDEN_SL_MAX_PIPS = 9.5)"; "every discarded setup MUST carry a reason from: EMISSION_CAPPED | CS1 | NARRATIVE | RRR | SL_INVALID | TP_NULL | SOURCE_INVALID" (C:853-858).
- **12.3 CS-1 Day-Native Guard:** "`structurallyValid({sl}, openPrice, direction)` where `openPrice = shapeDay.dayOpenSpot ?? sessionStartPrice`"; flag `CS1_DAY_NATIVE` if from `dayOpenSpot`, `CS1_UNCHECKED` "honest flag if from sessionStartPrice" (C:864-868). The predicate itself is UNKNOWN.
- **12.4 Narrative Gate:** "`narrativeAligned(setup, model, pair)` with ZFP bands: suppress > 30 (WEAK), exempt < 20 (Hard Wall), 20-30 flagged" (C:874-878).
- **Abort macro (C:1039-1054):** "When a setup fails ≥2 zero-tolerance rules simultaneously OR fails the Phase 12 audit hard-discard, emit: `E3 SETUP [${setupId}] ABORT: [reason] — setup marked [REJECTED]. Continuing with remaining setups.`" (source prefixes a warning-sign glyph). Reasons: `NO_DAY_ASSIGNABLE`, `NO_OPPOSING_ZONE`, `NO_LSZ_ANCHOR`, `RRR_BELOW_FLOOR` ("RRR < 3.0 after 3 refinement attempts"), `CASCADE_DRIFT_EXCEEDED` ("divergence > 35% (flag only, but abort if combined with other failures)"), `DIRECTION_VALIDATION_FAILED`, `ZONE_DEPLETED` ("reactionCount ≥ 3 (TP-only)"), `VIRGIN_MOM_DEATH_ZONE`, `NARRATIVE_MISALIGNED`.

Section 8.12 JEV hooks are "Optional in v5.3.3 — required in v6 ... Skip this section if running in pure-deterministic v5.3.3 mode" (C:883). Not needed for the Pine build.

---

## 2. Trade types — what is emitted as a trade and what is not

C never uses the word "draw" for chart objects (Pine rendering is Part X, outside C). What C fixes is which objects carry their own entry/SL/TP. That is recorded here; how each is rendered on the chart is UNKNOWN from these three sources.

2.1 **Category vocabularies (four different ones in C — see CONFLICT B-12).** Enum: `SetupCategory = 'HTF Swing' | 'Swing Scalp' | 'Breakout Search' | 'Reinforcement' | 'Transition'` (C:1193).

| Object | Own E / SL / TP? | Evidence |
|---|---|---|
| **HTF Swing** (standard zone trade on Swing Stack 4H/1H/30m) | YES, one E, one SL, one TP | output block `Entry / SL / TP / RRR` (C:937-944); `TradeSetup` (C:1256-1360) |
| **Swing Scalp** (Scalp Stack 30m/15m/5m) | YES | output block (C:949-954) |
| **Transition** (SS→BS / Post-WL Reverse / DWL-Inverse) | YES | `TransitionSetup` has `entry, sl, tp, rrr` (C:1413-1430) |
| **Breakout Search** | UNKNOWN — in the enum and BE4 only; no definition, no output block, no entry in `categoryShapeMap` | C:609, C:1193 |
| **Reinforcement / rocket (FLR, FR, LR)** | Trigger zone + Entry zone + Stop-Loss zone; NO own TP field | `ReinforcementEntry` = `triggerZone, entryZone, stopLossZone, bufferZones, fibLevelAlignment, combinedRrrWithParent, parentTradeRef` (C:1395-1411). It is an add-on to a parent, never standalone: "Liquidity ladders are REINFORCEMENT entries on an EXISTING primary trade. They are NOT primary entries themselves" (T:100). Deleted original: "Same TP as primary setup. All reinforcements target the same TP1" (O:2899). |
| **Avatar State / Master Trade Setup** | NOT a separate trade. A boolean state on a GOD_TIER HTF Swing plus its FLR rocket list | `TradeSetup.avatarState: boolean` (C:1330); `MasterTradeSetup = {avatarState, eEntry, flrRockets[{fib, entry, sl, tp}], waterMacroShape, profitManagement}` (C:1448-1461) |
| **Trade Flow Chain** | NOT a trade — a link between existing setups | C:1362-1368 |
| **IP zone (PILLAR source)** | NEVER an entry; confluence + SL/TP rung only | C:136 |
| **DEPLETED zone (3+ battles)** | NEVER an entry; "TP target ONLY" | C:160 |

2.2 **HTF Swing.** Shapes BS, WL, PBS, RS (+ RWL, PRWL in `categoryShapeMap`, C:509); "Directional move entries — primary profit drivers"; session NY (C:146). Default session "NY Mid" (C:569).

2.3 **Swing Scalp.** Shapes SS, SS(DWL), WLS, R (C:510); "Range-bound scalps at boundaries, recovery bounces"; session London (C:144). Default "London Open" (C:567). Quality line in the output block: "[STANDARD/CONDITIONAL]" (C:951). The detailed swing-scalp procedure (Types 1-4, parameter table) existed ONLY in original Part VII-B (O:2736-2866), which C deletes (C:33) without a replacement procedure — see CONFLICT A-23. Under C a swing scalp is built by the generic Phases 2-5 on the Scalp Stack with Fib Context 2.

2.4 **Rockets (C:672-678).**

| Rocket Type | Element | Scale | Buffer | Use |
|---|---|---|---|---|
| FLR (Fibonacci Liquidity Rocket) | Earth Heavy Attack | 30m Fib + Liq Zone entry/SL | THICK (2 thick or 2-3 thin zones) | Forward-mapping HTF storyline moves |
| FR (Fibonacci Rocket) | Fire Precision | 15m Fib + S/D strikes | Standard (1-2 zone buffer) | Localized Fib levels for London Session Scalping |
| LR (Liquidity Rocket) | Water Precision | Zone-to-zone during confirmed moves | THIN (1 thick or 2-3 thin zones) | Standard reinforcement, 20-30% failure rate acceptable |

2.5 **Avatar State (C:699-714, C:804-816).** "when ALL FOUR elements converge at a single price level". Conditions: "Earth: Entry at liquidity zone / IP zone"; "Fire: Entry overlaps with S/D zone"; "Water: Macro shape confirms direction and timing"; "Air: Fibonacci spiderweb maps complete pathway from entry to TP". Formula: "`E (Entry) + FLR (Fibonacci Liquidity Rocket) = Avatar State`". Construction: "1. Identify the BoM S/D + Liq Zone overlap (Earth + Fire) 2. Confirm macro shape direction (Water) 3. Map NY Fib Rocket setup with key 1/2 levels (Air) 4. Place up to 3 FLR rockets at Fib-confirmed Liq zones (1.382, 1.618, 2.382 Fib levels) 5. Place additional LR rockets at intermediate Liq zones (cross-zone liquidity ladder) 6. Verify Avatar State (all 4 elements converge) — set `setup.avatarState = true` 7. Emit `MasterTradeSetup` object" (C:807-813). Gate: parent must be GOD_TIER, and GOD_TIER requires `vlmSourced` (C:420) — with no VLM in a Pine indicator GOD_TIER is unreachable as written: UNKNOWN how Avatar is gated without a VLM.

---

## 3. Entry, stop-loss, take-profit, RRR, confidence, session, counts

### 3.1 Entry
- **Which zone.** The E2-designated anchor for the day and direction: LONG → `demandZoneId`, SHORT → `supplyZoneId`, `keyZoneId` fallback (C:132). Only `ORDER_BLOCK` or `LQZ` sources (C:135). Zone must be "on the correct side of spot per the day's direction" (C:129).
- **Which timeframe zone.** Stack by category: "Timeframe Stack Compliance (Swing=4H/1H/30m; Scalp=30m/15m/5m; 5m refinement only)" (C:1009); violation = REJECT (C:242). Golden-standard Law 3: "Entries are NEVER placed at 4H zone edges. They are placed at: 15m zone edges for scalps: entry at zone boundary ± 2 pips inside; 30m zone edges for swings: entry at zone ceiling (SHORT) or floor (LONG); 1H zone edges for HTF swings: entry at nearest key level to zone edge; 4H zones: Directional bias + TP target ONLY. Never direct entry" (T:48-52).
- **Which edge — TS-1 (corrected):** "SNIPER ENTRY = zone edge CLOSEST to approaching price. SHORT from supply: Enter at BOTTOM edge of supply zone. LONG from demand: Enter at TOP edge of demand zone. If key_levels exist within the zone, use the one closest to the approaching edge (within the zone)" (C:178-181). CONFLICT with T:50 (ceiling for SHORT, floor for LONG) — see C-1.
- **F1-A (OB SHORT only):** "For OB SHORT only, lift the entry 1 pip above the supply zone's bottom edge. This places entries in the UPPER half of supply bands (best fill). Without the OB-only scope pin, LQZ-rung lifts move entries into rally wicks (losses)." Evidence lines: "Monday band bottom 101.027 / defEdge 101.092 gave RRR 1.79 → REJECTED"; "Operator 101.14 yields RRR 4.92 at the SAME SL/TP walk" (C:186-188). Arithmetic note (Derived): 101.027 + 1 pip (0.01) = 101.037, not 101.14 — the rule text and its own example do not agree; UNKNOWN which is intended.
- **F1-C (internal rung):** "When the S/D band CONTAINS an internal LMV rung, entry = internal LMV rung NEAR edge (SHORT = rung floor; LONG = rung ceiling) — NOT the zone's defendedEdge (which is the reinforcement level — a separate trade)." Examples "#4 EU Wed RWL LONG E 1.14020 = rung-1.14010 ceiling Δ0.7p"; "#6 EU Wed deep-demand E 1.13935 = deep shield Δ0.2p" (C:191-193).
- **F1-D (RWL bounce inset):** "`RWL_BOUNCE_INSET_PIPS = 0.2` — LONG bounce entries pulled INSIDE the rung CEILING by 0.2 pips"; "`RWL_HAIR_MISS_RRR_DELTA = 0.1` — setups with RRR in [floor − 0.1, floor) get one repair attempt before hard reject" (C:196-197).
- **F1-E (prior-week recovery shelf):** "When the entry zone is a prior-week recovery shelf (deep-wick anchor + DEMAND rungs above anchor + defended bullish transit + ≥2 day-closes inside band), pull the entry to the shelf center: `RWL_SHELF_LONG_ADJUST_PIPS = 1`" (C:200).
- **Order type.** C never states the order type of the primary entry: UNKNOWN (explicit). Implied resting limit at the sniper edge: C speaks of "session-bracketed fill simulation" (C:80) and a staggered "Front / Middle / Back" entry ladder at fixed prices (C:1064-1066); the original says "Do NOT have limit orders open right before news" (O:2534) and T says "ignore price action until it physically intersects with a pre-drawn Zone Map" (T:43). Rockets are explicitly STOP-LIMIT: "Regular Stop: market order on trigger → SLIPPAGE (10-20 pips in fast markets). Stop-Limit: stop detects trigger, then LIMIT placed at predetermined entry zone → fills ONLY at specific price or better" (C:682-683).
- **Scaled entry (Mechanism A, intra-zone, C:1062-1071):** Front "Zone edge nearest spot + forward spread" 33%; Middle "Leftward-facing candle key level from LQZ pattern" 33%; Back "Zone edge farthest from spot + forward spread" 34%. "Entry 2 fills → Entry 1 SL to breakeven (risk-free); Entry 3 fills → Entry 2 SL to breakeven; After all 3 fill: 67% of position risk-free; only Entry 3 (34%) carries risk". Forward spread per pair: DXY 0.02, EUR/USD 1 pip, GBP/USD 2 pips (C:1101-1103). Whether Mechanism A is mandatory for every setup or only HIGH/GOD_TIER (as in O:2690) is UNKNOWN in C.
- **Fib contexts (C:205-209):** 1 = 1H, "BS / WL on 1H shapes", "Fib retracements from prior week's H/L + 0.382→1.382 wormholes"; 2 = 15m, "SS / Recovery / scalps", "15m swing H/L + 0.5/0.618 "golden pocket""; 3 = 30m, "Mid-Swing / same-day", "30m swing + 0.786 deep entry / 1.272 extension TP". Wormholes: 0.382↔1.382, 0.5↔1.5, 0.618↔1.618 ("the strongest"), 0.786↔1.786, 1.0↔2.0 (C:212-216). Primary entry band 0.618–0.786 (C:226).

### 3.2 Stop-loss (Ladder-Steps model)
- **Doctrine (operator verbatim):** ""3 pips outside the back edge of the entry zone, or 1-2 pips inside the close edge of the next rung relevant zone."" (C:249).
- **Rule:** "SL = EITHER: (a) 3 pips OUTSIDE the FAR edge of the CURRENT entry step (entry zone's back edge + 3p) OR (b) 1-2 pips INSIDE the CLOSE edge of the NEXT STEP away (opposite direction of the projected trade direction)" (C:253-255).
- **Which zone is "relevant" (liquidity shield vs S/D):** "If fuel INTACT → LQZ SHIELD_FUEL (the LQZ acting as shield in front of the S/D). If fuel ABSORBED → S/D PRESSURE_STRUCTURE (the S/D itself acting as the backstop). If neither → Golden SL fallback (`computeGoldenSL_V452`)" (C:258-260).
- **Branch (a) vs (b):** "ZR-6B Rule S3 branch: confidence ≥ 0.6 → RR-tight (3p back edge); confidence < 0.6 → safety (next-rung)" (C:284-286), where confidence = `mirrorConfidenceScore`: "base 0.5; +0.2 if shapeConf ≥ 0.65; +0.15 VIRGIN or ACTIVE_1; −0.2 DEPLETED; +0.15 INTACT; −0.2 ABSORBED; +0.1 shapeDay.direction === direction; LMV pressure via bridgedLmvZone" (C:274-282).
- **Golden fallback:** "computeSL_LMV 4-9.5p reaction-extreme + selective util guard tighten iff util < 0.40 + §4.4.3 wick-clear; D17 36p ceiling // GOLDEN_SL_MAX_PIPS = 9.5" (C:291-294). "D17 SL ceiling = 36 pips HARD (the operator-measured golden SLs are 4-9.5 pips; 36 is the safety ceiling)" (C:309).
- **Per-pair buffer (Law 7, C:299-304):** EUR/USD 2 pips; GBP/USD 3 pips; DXY "5 (idx pts)" (AUD/USD 3). Used explicitly in the repair loop: "sl = next-rung's reactionExtreme + Law-7 buffer" (C:379). How Law-7 buffers combine with the 3p / 1-2p ladder rule on the first attempt is UNKNOWN (see B-4). DXY "5 idx pts" with pip = 0.01 (C:1101): whether that is 0.05 or 5.00 is not stated; T gives "SL distance 7-15 index points" for DXY with "Pip value 0.01 (index points)" (T:628-631), which reads as 0.01-units, i.e. 5 idx pts = 0.05 (Derived, not stated).
- **Rocket SL:** ""ROCKET STOP LOSSES ALWAYS 1 FULL PIP OUTSIDE BACK EDGE OF ZONE — NO EXCEPTIONS!!! ESPECIALLY IF THIN!!!!!" + "SL should be 1-2 pips OUTSIDE THE BACK EDGE OF THE STOP-LOSS ZONE!!!"" (C:307).
- **Hard Wall as SL anchor:** "Hard Wall Detection | Phase 4 | SL anchor (ZFP<15%, confluence≥8)" (C:1026). "LSZ Zones (with bottom edge extension) | Phase 4 | SL ladder-steps model" (C:1027).
- **No anchor → no trade:** `NO_LSZ_ANCHOR — no LSZ for SL placement` (C:1048); `SL_INVALID` yields no emission (C:1016).
- **Golden standard (T Law 4):** "SL distance from entry: 5-15 pips (median 12 pips, NEVER above 25 pips for standard entries)"; "SL is placed OUTSIDE the nearest liquidity shield zone"; "If no LSZ between entry and SL → SL widened to next LSZ or setup rejected"; "For deep HTF swings: SL can be 25-50 pips but MUST be behind 4H/8H liquidity shield" (T:67-71).

### 3.3 Take-profit — ONE TP
- "ONE TP per trade. Period. No TP1, TP2, TP3. No partial take-profits. Blended RRR is across the 3 staggered entries, NOT across multiple TPs" (C:313).
- **Placement (Law 11-14, C:316-321):** "1. TP at the opposing pressure — nearest opposing supply/demand zone where the LQZ (liquidity) sits INSIDE the S/D zone (Earth+Fire convergence) 2. For LONG trade: TP at nearest SUPPLY zone above entry; LQZ inside supply = Earth anchor 3. For SHORT trade: TP at nearest DEMAND zone below entry 4. If S/D + LQZ overlap exists (Earth+Fire convergence) → TP at zone MIDPOINT (strong reaction) 5. If no LQZ overlap → TP at zone NEAR EDGE (quick exit) 6. NEVER target FAR edge of distant zone".
- **Strength-driven edge (C:326-329):** STRONG (BoM, high confluence, fortress) → "CLOSE edge (near edge) + 1-2 pip spread"; WEAK (virgin MoM, low confluence) → "FAR edge (maximize catch)". Conflicts with rule 6 above — see B-6.
- **Law-14 walk `computeLmvTP` (C:333-344):** "E2-shapeDay projected opposing zone defendedEdge FIRST; THEN significance walk; fresh-wall zfp ≤ 20 cap; E1-walls strengthDrivenRungTp; weak-shelf pass-through REJECTED by measurement; Fallback: computeMirrorTP; else: TP_NULL discard; Law-14 precondition: TP ≥ 1.2 × SL".
- **No teleport:** "Price cannot teleport past UNMITIGATED zones. Price CAN pass through mitigated zones during BS momentum. The 'no teleport' constraint applies ONLY to zones with reactionCount = 0" (C:347). Rule 8: "Sequential Zone Path (every setup MUST map sequential zone path entry→TP)" (C:1008).
- **TP timeframe:** "TP timeframe must be ≥ entry timeframe; 15m entry → 30m or 1H TP; 1H entry → 4H TP" (C:350-352). Matching table (C:1170-1176): 4H→4H (1H acceptable); 1H→1H (30m acceptable); 30m→30m (15m acceptable); 15m→30m or 1H "(up to 2 TF up) — Cannot target 4H — too far"; 5m→15m or 30m.
- **4H BoM cascade:** "4H BoM zones pierce through everything until they reach the 4H same-element zone on the opposite side" (C:670).
- **No TP → no trade:** `NO_OPPOSING_ZONE`, `TP_NULL` (C:1047, C:1016).

### 3.4 RRR, floor, repair
- "Primary RRR: `|TP - entry| / |entry - SL|`"; "Blended RRR (3-entry staggered): `(rrr1 × 0.33) + (rrr2 × 0.33) + (rrr3 × 0.34)`" (C:356-357).
- **Floor (IRON LAW):** "Emission floor: RRR ≥ 3.0 (all categories) — the gate, code, never model; Executed standard: RRR ≥ 3.5; Norm: RRR ≥ 4.0+ (operator's average is 4.0–6.4×); MAX_CHAIN_RRR ceiling: 15.0 (Law-13) — chains beyond 15R fill-and-stop (GU 1.34957 measured)" (C:362-365). Operator: "MINIMUM 3 RRR NOTHING LESS IS ACCEPTABLE ... ALL MY TRADES ARE 4+ SO 3 IS THE MINIMUM" (C:360).
- Table (C:1108-1115): Consolidation, HTF Swing, Reversal, Reinforcement, Transition all 3.0 / 3.5 / 4.0+; "Consolidation week (relaxed) | 2.5 | 3.0 | 3.5+".
- "RRR is a CONSEQUENCE of zone geometry, never a forced target. Never distort zone structure to hit a target RR" (C:367).
- **3-attempt repair (C:374-383):** `for attempt in 1..3: if rrr >= floor: EMIT; else refineSetup on SAME anchors (entry FIXED — re-anchor SL/TP only); sl = next-rung's reactionExtreme + Law-7 buffer; tp = next-significance-ranked opposing rung's defendedEdge; log "REPAIRED({attempt}): SL re-anchored {old}p→{new}p, RRR {old}→{new}"; if all 3 attempts fail: HARD REJECT with full 3-attempt audit trail`.
- **Per-anchor locks:** "3 attempts on each anchor (3 E, 3 SL, 3 TP refinement attempts each tracked and locked individually per trade ...)" (C:386). Conflicts with "entry FIXED" above — see B-9.

### 3.5 Confluence, confidence gate, quality
- **Confluence stack (Phase 4.1, C:239-245):** L1 "Tier 1/2 POI confluence (overlap with 4H BoM)" +2/+1/0; L2 "Three-Tier Option Classification bonus" +3 (Critical)/+2 (Significant)/0; L3 "Reaction Counter alignment (UM BoM = +5; MoM = -10; Depleted = REJECT)"; L4 "Timeframe Stack Compliance" +3/0 "(violation = REJECT)"; L5 "Day-Shape Alignment (setup matches E2 day shape)" +5/0/-5; L6 "Session Mechanics" +3 (London)/+2 (NY)/0 (Asian); L7 "Storyline Bias Alignment" +5 / -5 "(counter-trend, requires exceptional confluence)". C gives no threshold on the stack total: UNKNOWN how the total is used.
- **Confidence score (Phase 5.1, 0-100, C:393-404):** `base = vz.confidence` ("typically 50-95"); `+ min(15, ipZone.confluence × 1.5)`; `+5 if ipZone.isBoM`; `+8` zone-direction alignment (SUPPLY→SHORT or DEMAND→LONG); `+5` storyline bias alignment; `+7 if vz.source !== 'FALLBACK_IP_EDGE'`; `+5 if rrr ≥ 3, +3 if rrr ≥ 2`; `-10 if slDistancePips > 80, -5 if > 50`; `-8 if distPips > 150, -4 if > 80`; prior-week momentum `+3 if aligned, -8 if misaligned`; clamp [0, 100].
- **SL-distance bands (C:408-410):** "`sl_distance > SL_MAX_PENALTY[pair] → -10 confidence` (EUR 100p, GBP 120p, AUD 100p, DXY 30 idx)"; "`sl_distance < 30p → +10 confidence`"; "`sl_distance < 60p → +5 confidence`".
- "DXY cascade bonus: `+10` if setup is cascade-source (DXY → EU inverse or EU → GU kept)" (C:412). "GU short-squeeze override: `+5` for GBP/USD LONG (short squeeze amplification); NO double penalty for GU SHORT MoM" (C:414).
- **Quality (C:420-424):** GOD_TIER "confidence ≥ 90 AND rrr ≥ 3.0 AND vlmSourced"; HIGH "confidence ≥ 80 AND rrr ≥ 2.0"; STANDARD "confidence ≥ 60 AND rrr ≥ 1.5"; CONDITIONAL "confidence ≥ 50 (conditional zones only)"; REJECTED "confidence < 50".
- **Inclusion gate:** rule 11 "confidence ≥65 required for inclusion" (C:1011). Conflicts with the 50/60 quality bands — see B-10.
- **E2 day confidence gate:** < 65% → +1 day shift (C:123, C:537, C:617); `shapeConf ≥ 0.65` → +0.2 in `mirrorConfidenceScore` (C:276).

### 3.6 Session and timing
- **Source of truth:** "Every order leg's session bracket comes from the E2 session label" (C:77); `WorkingDayMap.session: SessionWindow` (C:1252); floor invariant "Session bracket valid (E2-designated session window)" (C:855).
- **Per-day default (T2 spec §5):** "Mon/Wed/Fri → LONDON; Tue/Thu → LONDON_NY_OVERLAP" (C:560-561).
- **Category default (C:565-571):** SWING_SCALP → London Open; BREAKOUT_SURGE → London/NY Overlap; HTF_SWING → NY Mid; REINFORCEMENT → NY Open; TRANSITION → London/NY Overlap. Setup-category table (C:144-147): Consolidation → London; Reversal → NY; HTF Swing → NY; Reinforcement → NY Open.
- Precedence between the E2 session label, the per-day default and the category default is UNKNOWN (`selectSession` body not given) — see B-11.
- **Liquidity filter:** "`liquidityScore ≥ 7` → allow any session; `liquidityScore ≥ 5` → allow London/NY only; `liquidityScore < 5` → reject ("no wood for the fire")" (C:574-576). `liquidityScore` definition UNKNOWN.
- **Session clock times (only source: T Part 10, T:590-594):** London Open 02:00-05:00 ET (scalp entries, 22/38); London/NY Overlap 08:00-10:00 ET (breakout entries, 15/38); NY Mid 10:00-14:00 ET (HTF swing entries, 18/38); NY Open 08:30-10:00 ET (reinforcement triggers, 8/38); Asian Session rare (3/38). Clock times for "London Mid" and "NY Close" (C:1196): UNKNOWN.
- **Red Folder:** "30-minute deferral on red-folder economic events (CPI, PPI, NFP, FOMC). Setups whose anchor hit window overlaps a red-folder event are deferred by 30 minutes" (C:1125).
- **Trading speed:** ""Assume price moves at 30-50% of the speed you think it will."" "Today's move often becomes tomorrow's move → +1 day to expected timing; 4H move duration: takes 2× as long as expected; Reinforcement rocket spacing: spaced further apart to avoid clustering" (C:1140-1146).
- **Profit taking:** ""Close ALL positions by NY close Friday" — per pair" (C:666, C:616, C:977). Avatar: ""If everything cannot be moved 30-50% in profit we automatically take all profits before market close. Mandatory."" (C:721, C:816).
- **Consolidation phase → valid types (C:1131-1136):** Early (SS/WLS <1 session) → Swing Scalps (both directions); Mid (1-3 sessions) → Swing Scalps + Double Whiplash Inverse; Late (ZFP trending up on bounding zone) → Swing Scalps + BS Transition Entry; Post-BS early breakout → Reinforcement entries only; Post-BS recovery → Whiplash/Recovery Surge entries; Mid-breakout → Reinforcement entries at liquidity zones.
- Rule 5: "Post-pierce consolidation awareness (no whiplash storm setups immediately after 2 strong piercing moves)" (C:1005).

### 3.7 Per-day and per-week counts
- **BRIEF (operator, relayed):** max 1-2 real moves per day, 6-10 per week, never more than 11 per pair per week. Not found in C, O or T.
- **C says no weekly cap:** ""i never said to put a cap. i think you misinterpreted something here." — D10"; ""... max setups should be removed there is no limit on trade setups for a week, there is only filtering of shitty dumb garbage setups" — D38"; ""ALL valid setups should be mapped. The filter will kill retarded/hallucinated setups." — D16" (C:467-469).
- **C per-anchor cap:** `MAX_MIRRORS_PER_ANCHOR_PER_DAY = 1`, key `(pair, anchorBucket, day)` (C:471).
- **C per-category cap:** rule 11 "Max 3 setups per category per pair; total max unlimited (NO CAPS — operator D38); confidence ≥65 required for inclusion" (C:1011).
- **C floor on count:** "f(T) Acceptance: |all_setups| = 24 minimum (8 DXY + 8 EU + 8 GU), MORE is fine, LESS is REJECT" (C:996); ""... MORE than 24 is fine, LESS is not."" (C:785).
- **C expected count per shape-day (C:96-107):** SS 4–8 swing scalps; SS(DWL) 4–8 + 1–2 inverse; BS 1 swing + 2–3 reinforcements; PBS same; R 2–4 swing scalps; RS 1; WL 1; RWL 1; PWL 1; PRWL 1 + 1–2 reinforcements; WLS 4–8 + 1–2 inverse; SS→BS 1 transition + reinforcements.
- **CONFLICT D-1 (BRIEF vs C).** 8 per pair per week (C:996) sits inside the BRIEF's 6-10, but "4–8 swing scalps" for one SS day (C:96) and "no limit" (C:468) contradict "max 1-2 real moves per day" and "never more than 11 per pair per week". C supplies only these ranking handles if a cap must be enforced: higher confidence survives a conflict (C:462), first-kept per anchor per day (C:471), quality tier (C:420-424), confidence ≥ 65 (C:1011). Which handle the operator wants for the 11-cap is UNKNOWN — needs a ruling.

---

## 4. E2 day-shape → permitted trade (R3: E2 designates, E3 obeys)

4.1 **Setup Universe Matrix (verbatim, C:94-107).**

| E2 Shape | Setup Universe | TF Stack | Expected Setup Count |
|---|---|---|---|
| SS (Swing Scalps) | Swing Scalps (both directions) | Scalp Stack (30m/15m/5m) | 4–8 swing scalps |
| SS(DWL) (Double Whiplash) | Swing Scalps + DWL Inverse | Scalp Stack | 4–8 swing scalps + 1–2 inverse |
| BS (Breakout Surge) | HTF Swing + Reinforcements | Swing Stack (4H/1H/30m) | 1 swing + 2–3 reinforcements |
| PBS (Piercing BS — ZFP > 70%) | HTF Swing + Reinforcements | Swing Stack | 1 swing + 2–3 reinforcements (deeper targets) |
| R (Recovery) | Swing Scalps + Recovery Surge | Both Stacks | 2–4 swing scalps |
| RS (Recovery Surge — sharp retracement) | HTF Swing | Swing Stack | 1 swing |
| WL (Whiplash) | HTF Swing | Swing Stack | 1 swing |
| RWL (Reverse Whiplash) | HTF Swing | Swing Stack | 1 swing |
| PWL (Piercing Whiplash) | HTF Swing | Swing Stack | 1 swing |
| PRWL (Piercing Reverse Whiplash — STRONGEST REVERSAL) | HTF Swing + Reinforcements | Swing Stack | 1 swing + 1–2 reinforcements |
| WLS (Whiplash Storm) | Swing Scalps + DWL Inverse | Scalp Stack | 4–8 swing scalps + 1–2 inverse |
| SS→BS Transition | Transition Entry | Both Stacks | 1 transition + reinforcements |

4.2 **Direction.** E3 does not pick a direction. Each E2 day carries `direction: Direction` (C:1245, C:1589). LONG is anchored at that day's `demandZoneId`, SHORT at `supplyZoneId` (C:132). SS-family days are the only ones the matrix marks "both directions" (C:96); C does not say how a both-direction day is expressed through the single `direction` field: UNKNOWN. For BS/PBS/RS/WL/RWL/PWL/PRWL the trade direction = the E2 day `direction`; whether a WL/RWL trade is taken with or against the spike is not stated beyond "Reversal | RWL, R (when reversing) | Counter-move entries at Hard Wall rejections | NY" (C:145): UNKNOWN.

4.3 **Category ↔ shape (C:508-513).** HTF_SWING ⇐ BS, WL, PBS, RS, RWL, PRWL. SWING_SCALP ⇐ SS, SS(DWL), WLS, R. REINFORCEMENT ⇐ BS, WL, R, RWL. TRANSITION ⇐ SS→BS. (PWL is in the matrix but missing from the HTF_SWING list; PRWL/PBS get reinforcements in the matrix but are missing from the REINFORCEMENT list — see B-13.)

4.4 **Alignment scoring.** Day-shape aligned +5 / neutral 0 / misaligned -5 (C:243); storyline bias aligned +5 / counter-trend -5 (C:245); `+0.1 shapeDay.direction === direction` (C:281).

4.5 **Shape → reach distance.** "SS ±5-30 pips, BS 30-100, WL 50-200, RWL 30-100, R 10-50" (C:588). Golden standard Law 2 (T:36-40): SS (Mon-Tue) 0-30 pips, "Scalp entries at nearby zones"; BS (Wed) 30-100 pips in breakout dir, "HTF Swing / Breakout"; WL (Thu-Fri) 50-200 pips at extremes, "Reversal entry after spike"; RWL 30-100, "Counter-direction scalp"; R 10-50, "Reinforcement / Recovery entry". `SHAPE_MAX_DISTANCE = {SS: 30, BS: 100, WL: 200, RWL: 100, R: 50, RS: 80}`, default 60, skip if `distPips > maxDist` (T:256-269). Law 7: "Only generate setups at zones within the expected range for that day's shape"; "If no zone is reachable based on shape prediction → "no actionable setup" for that day" (T:152-153).

4.6 **Chain order.** BS → R, BS → WL, BS → RWL, WL → RWL, SS → BS (C:453-457).

4.7 **Cascade never designates.** "DIVERGED, flag only — pair E2 stands (cascade VALIDATES, never designates)" (C:799). "B1.5: NEVER re-anchor E2-designated" (C:838).

---

## 5. Reinforcement / ladder rules

5.1 **Eligibility.** Only HTF Swing parents of HIGH or GOD_TIER quality; 2–3 reinforcements "at intermediate liquidity zones along the TP path" (C:621). Consolidation-phase gate: "Post-BS (early breakout) → Reinforcement entries only"; "Mid-breakout → Reinforcement entries at liquidity zones" (C:1134, C:1136).

5.2 **Timing (8R.0, reconciled).** "Reinforcement ORDERS are placed in London premarket (pending stop-limit orders). Reinforcement ORDERS become ACTIVE only when the 1-2-3 pattern completes on the primary entry (Phase 2.5). Reinforcement ORDERS that haven't triggered by parent TP are CANCELLED" (C:625).

5.3 **Mechanism B — cross-zone Liquidity Ladder (8R.1).** "Reinforcements at DIFFERENT zones along TP path. Purpose: scale into WINNING trade as it progresses favorably. Trigger: price reaches next MoM zone TOWARD TP." "Position sizing: 50/30/20 (primary/rocket1/rocket2)"; "Each rocket has its OWN SL (no shared SL)"; "SL cascade: Rocket 1 triggers → Primary BE; Rocket 2 triggers → Rocket 1 BE"; "Combined R:R 16–61× with position sizing" (C:631-636).

5.4 **Fib rocket levels (8R.2, C:642-647).** Entry 0.618–0.786 "Primary entry zone (STRONG PRESSURE)"; Rocket 1 1.382–1.786 "CLEANEST entry for reinforcement (90% accuracy with Fib lines)"; Trigger 2.382–2.786 "Second reinforcement (trip-wire placement)"; Target 3.382–3.786 "Extended TP target". Key level zones: 0.382–0.5 initial strong reaction; 0.5–0.618 transitional; 0.618–0.786 "STRONG PRESSURE ZONE"; 0.786–1.0 "FINAL BLAST" (C:653-656).

5.5 **Overlap rule (8R.3).** "≥2 reinforcements inside primary SL → reject the additional ones (overlapping risk)" (C:660). Opposite of the original — see A-14.

5.6 **TP management (8R.4).** "70-80% TP rule: take 70-80% at TP1, run 20-30% for extension"; "BoM re-entry rule: if price retraces to BoM after partial TP, re-enter with remaining position"; Profit Taking Law (C:664-666). Contradicts "ONE TP ... No partial take-profits" (C:313) — see B-5.

5.7 **Stop-limit / trip-wire (8R.7).** "Trip-Wire Concept: detects movement (price reaching trigger zone) but rocket fires at pre-designated target (entry zone). If price never comes back, limit never fills — ZERO additional risk" (C:685). 4-point criteria: "1. Trigger zone identified (the trip-wire zone — typically 2.382–2.786 Fib) 2. Entry zone identified (the limit zone — typically 1.382–1.786 Fib) 3. SL zone identified (1 pip outside back edge of next LQZ rung) 4. TP zone identified (opposing BoM or Fib extension)" (C:688-691). "Triple Anchor Reinforcement: the SL of the rocket is placed inside the entry zone of the parent trade (so if rocket SL hits, parent trade goes to breakeven — risk-free reinforcement)" (C:693).

5.8 **Caps.** "Max 3 rockets per trade (recommended 2). Both Mechanism A and Mechanism B count toward this cap" (C:1080). "Up to 7 active rockets possible with hardwired safety (max 3 per pair, max 3 rockets per trade per §8R.6 Law 1)" (C:718). Avatar: "Place up to 3 FLR rockets" plus "additional LR rockets" (C:810-811).

5.9 **Rocket RRR.** Reinforcement floor 3.0 (C:1113). `combinedRrrWithParent` reported (C:1409).

5.10 **8R.8.** "The 10 VLM-verified rocket patterns from the original v5.3.3 are preserved verbatim" (C:697) — text only at O:3096-3131. Measured there: thick-zone-only T/E/SL; buffers LR 1 zone, FR 2 zones; "T→E GAP: 10-20 PIPS ON GBPUSD (MOST COMMONLY ~15 PIPS)" (O:3112); "E→SL DISTANCE: 18-45 PIPS ON GBPUSD" (O:3115); 2-3 rockets per trade; first Fib contact = FR (2 buffer), later contacts = LR (1 buffer) (O:3131).

5.11 **Golden standard Law 6 ladder (T:102-139).** Primary "At BoM zone, SL 5-15 pips (ONLY risk in the entire ladder)"; Rocket 1 "At next MoM zone (~20-30 pips from primary) → Fib 1.382 extension → When R1 triggers: Primary SL → BREAKEVEN"; Rocket 2 "At next MoM zone (~20-30 more pips) → Fib 1.618 extension → When R2 triggers: R1 SL → BREAKEVEN, Primary SL locks profit"; TP "At opposing BoM / Liquidity Shield zone → Fib 2.382+ extension → Combined R:R = 16-61x (only primary risk counts)". Spacing: Primary→R1 20-30 pips; R1→R2 12-30 pips; R2→TP 25-130 pips (T:122-124). Sizing 50% / 30% / 20%, "Alternative scaling observed: Equal thirds" (T:576-580). Rockets snap to the nearest actual MoM zone, not pure Fib math (T:328-345). Reinforcement entry "At FAR edge of entry zone", SL 10-25 pips (T:60).

5.12 **Efficient liquidity mapping (8R.10).** "for each setup, map ALL liquidity zones (LSZ/LQZ) between entry and TP. Each is a potential reinforcement anchor" (C:718).

---

## 6. Multi-pair cascade DXY → EURUSD (inverse) → GBPUSD (kept)

6.1 **Law.** ""Everything I found on this EU chart maps 1:1 to DXY EXACTLY simply in the inverse direction. ... the only thing that changes are the actual price levels between the pairs."" (C:729). "DXY LONG → EU SHORT (inverse) → GU SHORT (kept); DXY SHORT → EU LONG (inverse) → GU LONG (kept)" (C:733-734).

6.2 **Structural equivalence, never price conversion (C:739-744).** "Cascade matches SAME-ELEMENT zones (BoM→BoM, MoM→MoM, LQZ→LQZ)"; "Role translation: DXY/EU inverse (supply↔demand); EU/GU kept"; "Pair-specific LQZ generated unbiased (never price-converted)"; "Pair's E1 runs FIRST (zones must exist before cascade matches)".

6.3 **80/20 doctrine.** ""The mirror is for the trade setup direction, shape, and zone class of entry + TP. 80%. The remaining 20% like specific entry/SL/TP levels and anchors within the mirror cascade must be optimized for the actual pair being traded on. ... cannot be a blind mirror."" (C:748). ""You are mirroring zone CLASS not literal zone. ... DXY is only giving a SIGNAL with high accuracy not a blind copy paste trade."" (C:750).

6.4 **EU loop (C:755-768).** For each DXY source setup: `srcSignalMs = setup.battleMs ?? sourceFormationMs`; `euDayIdx = floor((srcSignalMs - weekStartMs) / 86400000)`; `euShapeDay = shapeChains.eu.days[clamp(euDayIdx)]`; `reAnchorMirror(setup, euModel, 'EUR/USD', {...ctx, sourceFormationMs: srcSignalMs, shapeDay: euShapeDay})`; "80% signal INVERT direction; 20% pair-native anchor"; "usedEuAnchors + alt-retry with excludedAnchorIds on collision"; "D11 doctrine: Δ≤15p = one signal shares; beyond = distinct must spread".

6.5 **GU loop (C:773-780).** "for m of activeEuMirrors: # GU mirrors ACTIVE EU mirrors, NEVER raw DXY"; `guDayIdx = floor((m.tradeMs - weekStartMs) / 86400000)`; `guShapeDay = shapeChains.gu.days[clamp(guDayIdx)]`; `reAnchorMirror(m, guModel, 'GBP/USD', {...ctx, sourceFormationMs: m.anchorFormationMs, shapeDay: guShapeDay})`; "direction KEPT (NEVER raw DXY) + usedGuAnchors distribution".

6.6 **Emergent lane.** "Mirror lane = guaranteed floor (every DXY setup MUST produce EU + GU mirrors)"; "Emergent lane = additive (pair-native setups from EU's own E1+E2, merged via dedup `(zoneId, reactionEvent.session)`)" (C:787-788).

6.7 **35% divergence (flag only, C:793-799).** "Shape-family alignment (SS≈SS/RWL/STORM/PRWL; BS≈BS/PBS; R; WL≈WL/WLS/PWL) OR ±1 step on master SS→BS→R→WL; divergence = (5-aligned)/5; missing day = not-aligned; ≤ 0.35 → VALIDATED; else → DIVERGED, flag only — pair E2 stands". Derived: (5-aligned)/5 ≤ 0.35 means at least 4 of 5 days aligned (1 miss = 0.20 passes; 2 misses = 0.40 fails).

6.8 **Audit lanes.** RE_TRANSLATE only on the INVERSE (DXY→EU) lane; KEPT (EU→GU) lane defers (C:832-836). Confidence +10 for cascade-source setups (C:412).

6.9 **Pair mechanics (C:1099-1103).** DXY: "Master compass", pip 0.01, buffer 5 idx pts, forward spread 0.02, "Processed FIRST; cascade to FX". EUR/USD: "Primary swing (NY focus)", pip 0.0001, buffer 2, forward spread 1 pip, "NY_FOCUS, DIRECT_ZONE_TEST, NO_SHIELD". GBP/USD: "Primary scalp (London focus)", pip 0.0001, buffer 3, forward spread 2 pips, "SHORT_SQUEEZE, LONDON_DOMINANT, HIGH_GAP_RISK".

---

## 7. Numeric constants (one table)

| Constant | Value | Cite |
|---|---|---|
| Emission RRR floor (all categories) | 3.0 | C:362, C:1108-1114 |
| Executed-standard RRR | 3.5 | C:363 |
| Norm RRR | 4.0+ (operator avg 4.0–6.4×) | C:364 |
| Consolidation-week relaxed floor / executed / norm | 2.5 / 3.0 / 3.5+ | C:1115 |
| `checkMirrorFloorV45` RRR floor | 2.5 | C:854 |
| `MAX_CHAIN_RRR` | 15.0 | C:365 |
| Chain max depth | 3 | C:450, C:1121 |
| Chain link tolerance (TP of N vs entry of N+1) | 3 pips | C:448 |
| RRR repair attempts | 3 | C:375 |
| `RWL_HAIR_MISS_RRR_DELTA` | 0.1 | C:197 |
| Law-14 precondition | TP ≥ 1.2 × SL | C:343 |
| Blended RRR weights | 0.33 / 0.33 / 0.34 | C:357 |
| Staggered entry weights (Front/Middle/Back) | 33% / 33% / 34% | C:1064-1066 |
| SL ladder (a) current step | 3 pips outside far edge | C:254 |
| SL ladder (b) next step | 1-2 pips inside close edge | C:255 |
| SL branch threshold (`mirrorConfidenceScore`) | ≥ 0.6 tight; < 0.6 next-rung | C:285-286 |
| `mirrorConfidenceScore` terms | base 0.5; +0.2 (shapeConf ≥ 0.65); +0.15 (VIRGIN/ACTIVE_1); −0.2 (DEPLETED); +0.15 (INTACT); −0.2 (ABSORBED); +0.1 (direction match) | C:275-281 |
| Golden SL range | 4–9.5 pips | C:291, C:309 |
| `GOLDEN_SL_MAX_PIPS` | 9.5 | C:294, C:856 |
| D17 SL hard ceiling | 36 pips | C:294, C:309 |
| Golden SL util guard | tighten iff util < 0.40 | C:292 |
| Law-7 SL buffer EUR/USD | 2 pips | C:301, C:1102 |
| Law-7 SL buffer GBP/USD | 3 pips | C:302, C:1103 |
| Law-7 SL buffer DXY | 5 idx pts | C:304, C:1101 |
| Rocket SL | 1 full pip outside back edge (also "1-2 pips") | C:307, C:690 |
| Pip size DXY / EURUSD / GBPUSD | 0.01 / 0.0001 / 0.0001 | C:1101-1103 |
| Forward spread DXY / EURUSD / GBPUSD | 0.02 / 1 pip / 2 pips | C:1101-1103; T:725 |
| F1-A OB SHORT entry lift | 1 pip above supply bottom edge | C:186 |
| `RWL_BOUNCE_INSET_PIPS` | 0.2 | C:196 |
| `RWL_SHELF_LONG_ADJUST_PIPS` | 1 | C:200 |
| Shelf qualifier | ≥2 day-closes inside band | C:200 |
| Freshness skip | battle index i > 2 | C:150 |
| Reaction ladder | UM 100% / 1x 80% / 2x 50% / 3x+ TP-only | C:150, C:154-160 |
| FORTRESS | 4+ strong battles, 95% direction flip | C:162 |
| Zone selection confluence | ≥ 7 | C:1022 |
| Hard Wall | ZFP < 15%, confluence ≥ 8 | C:1026 |
| PBS | ZFP > 70% | C:99 |
| Strong-zone TP spread | 1-2 pips | C:328 |
| Fresh-wall TP cap | zfp ≤ 20 | C:336 |
| Narrative ZFP bands | suppress > 30; exempt < 20; 20-30 flagged | C:876-878 |
| Confluence stack scores | L1 +2/+1/0; L2 +3/+2/0; L3 +5/−10/REJECT; L4 +3/0; L5 +5/0/−5; L6 +3/+2/0; L7 +5/−5 | C:239-245 |
| Confidence: IP confluence bonus | min(15, confluence × 1.5) | C:394 |
| Confidence: BoM / zone-direction / storyline / VLM-sourced | +5 / +8 / +5 / +7 | C:395-398 |
| Confidence: RRR bonus | +5 if ≥ 3; +3 if ≥ 2 | C:399 |
| Confidence: SL distance penalty | −10 if > 80 pips; −5 if > 50 | C:400 |
| Confidence: proximity penalty | −8 if > 150 pips; −4 if > 80 | C:401 |
| Confidence: prior-week momentum | +3 aligned; −8 misaligned | C:402 |
| `SL_MAX_PENALTY` | EUR 100p, GBP 120p, AUD 100p, DXY 30 idx → −10 | C:408 |
| SL-distance bonus | < 30p +10; < 60p +5 | C:409-410 |
| Cascade-source bonus | +10 | C:412 |
| GU LONG short-squeeze bonus | +5 | C:414 |
| Quality bands | GOD ≥ 90 & rrr ≥ 3.0 & vlmSourced; HIGH ≥ 80 & rrr ≥ 2.0; STANDARD ≥ 60 & rrr ≥ 1.5; CONDITIONAL ≥ 50; REJECTED < 50 | C:420-424 |
| Inclusion confidence | ≥ 65 | C:1011 |
| E2 day confidence for +1 day shift | < 65% (0.65) | C:123, C:537 |
| Opposite-direction conflict window | 15 pips | C:462 |
| Same-category duplicate window | 5 pips | C:463 |
| `MAX_MIRRORS_PER_ANCHOR_PER_DAY` | 1 | C:471 |
| Max setups per category per pair | 3 | C:1011 |
| Minimum weekly setups | 24 (8 DXY + 8 EU + 8 GU) | C:996 |
| BRIEF: per day / per week / hard max per pair per week | 1-2 / 6-10 / 11 | BRIEF |
| Session liquidity filter | ≥ 7 any; ≥ 5 London/NY; < 5 reject | C:574-576 |
| Anchor hit window | reach − 30 min … reach + 60 min; confidence 0.7 | C:592-594 |
| Shape reach (pips) | SS ±5-30; BS 30-100; WL 50-200; RWL 30-100; R 10-50 | C:588 |
| `SHAPE_MAX_DISTANCE` (pips) | SS 30; BS 100; WL 200; RWL 100; R 50; RS 80; default 60 | T:256-265 |
| Red Folder deferral | 30 min | C:531, C:1125 |
| Direction validation flip | 4+ of 6 disagree | C:1093 |
| Counter-trend sizing | HIGH 25%; MODERATE 50%; NONE 100% | C:1095 |
| Abort trigger | ≥ 2 zero-tolerance rules failed | C:1039 |
| Reinforcements per HIGH/GOD HTF swing | 2–3 | C:621 |
| Max rockets per trade | 3 (recommended 2) | C:1080 |
| Max active rockets (Avatar) | 7 (max 3 per pair) | C:718, C:984 |
| Ladder sizing primary/R1/R2 | 50 / 30 / 20 | C:633; T:576-578 |
| Ladder combined R:R | 16–61× | C:636; T:116 |
| Rocket Fib bands | Entry 0.618–0.786; Rocket 1 1.382–1.786; Trigger 2.382–2.786; Target 3.382–3.786 | C:644-647 |
| Avatar FLR fib levels | 1.382, 1.618, 2.382 | C:810 |
| Fib wormholes | 0.382↔1.382; 0.5↔1.5; 0.618↔1.618; 0.786↔1.786; 1.0↔2.0 | C:212-216 |
| Regular-stop slippage | 10-20 pips | C:682 |
| LR accepted failure rate | 20-30% | C:678 |
| Avatar profit rule | move everything 30-50% in profit or close before market close | C:721 |
| Avatar failure probability | (0.20)^4 = 0.0016 | C:714 |
| D11 shared-signal distance | Δ ≤ 15 pips | C:767 |
| Cascade divergence threshold | ≤ 0.35 validated | C:798 |
| Day length for day index | 86400000 ms | C:757 |
| Trading speed | price moves at 30-50% of expected; 4H move 2× as long | C:1140-1143 |
| Golden-standard SL | 5-15 pips, median 12, never > 25 standard; deep HTF 25-50 | T:67-71 |
| Golden-standard SL distribution (38 imgs) | 5-8p: 11; 8-12p: 14; 12-20p: 8; 20-50p: 5 | T:76-79 |
| Golden-standard entry offset / SL / R:R | Scalp 0-2p inside, 5-8p, 4-6.5x; HTF Swing at edge, 10-15p, 3-10x; Breakout 12-20p, 5-15x; Reinforcement far edge, 10-25p; Whiplash 7-14p, 3.5-9x | T:56-61 |
| Zone width by TF (pips, typical) | 5m 5-8; 15m 8-15; 30m 12-25; 1H 15-35; 4H 30-80; 8H 50-150 | T:21-26 |
| LTF entry-zone proximity | within 30 pips of spot | T:238 |
| Unshielded SL check | no LSZ between entry and SL and SL > 20 pips → widen to next LSZ, else confidence −10 | T:289-298 |
| Ladder spacing (pips) | Primary→R1 20-30; R1→R2 12-30; R2→TP 25-130 | T:122-124 |
| Refined-zone merge tolerance | 5 pips | T:614 |
| Session clocks (ET) | London Open 02:00-05:00; London/NY Overlap 08:00-10:00; NY Mid 10:00-14:00; NY Open 08:30-10:00 | T:590-593 |

---

## 8. CONFLICTS

### 8.A Original (O) vs corrected (C) — C wins

| # | Topic | Original | Corrected |
|---|---|---|---|
| A-1 | Entry level | "Entry = specific KEY LEVEL within the POI zone, NOT the zone edge"; LONG "2nd lowest key level near zone bottom"; SHORT "2nd highest key level near zone top" (O:2225-2227, O:2581-2586) | "SNIPER ENTRY = zone edge CLOSEST to approaching price"; SHORT bottom edge of supply; LONG top edge of demand (C:178-180). Opposite side of the zone. |
| A-2 | SL | SHORT "Nearest big figure above entry + 2.5 pip buffer"; LONG "Key level of zone below entry - 1 pip"; min 2.5 / 1.5 pips; "If no SL anchor within 30 pips (0.30 DXY): REJECT" (O:2234-2238) | Ladder-steps 3p outside / 1-2p inside next step; golden 4–9.5p; 36p ceiling (C:249-309) |
| A-3 | TP | Regime table (SS nearest opposing zone/LSZ edge; BS Fib wormhole; R nearest IP zone; WL/RWL Fib wormhole) + "TP2: Second opposing zone boundary if within 80 pips" (O:2248-2257, O:2637) | "ONE TP per trade. Period. No TP1, TP2, TP3" at the opposing S/D via Law-14 walk (C:313-344). C still calls the phase "Regime-Conditional" (C:311, C:1030) but prints no regime table: UNKNOWN whether the regime table survives. |
| A-4 | RRR floors | God-Tier 4x, High 4.5x, Standard 5x, scalp 3x, reinforcement 2x, counter-trend 2.5x (O:2711-2720) | 3.0 flat floor, all categories (C:362, C:1108-1114) |
| A-5 | Confidence formula | Base (Confluence/12)×40 + option 20 + shape 20 + Red Folder 10 + ZFP 10 ± BoM/MoM; "Minimum 65" (O:2296-2304) | `vz.confidence` base plus bonuses/penalties (C:393-404) |
| A-6 | Quality bands | God-Tier 85+, High 75–84, Standard 65–74, below 65 excluded (O:2307-2310) | 90 / 80 / 60 / 50 with RRR terms (C:420-424) |
| A-7 | Confluence stack | 7 layers with "Required" / +2 / +1; "RRR > 4x Required" (O:2170-2180) | 7 different scored layers (C:239-245) |
| A-8 | Caps | HTF 3, scalps 3 per range, reinforcements 3 per swing, transitions 2, "Total across all categories: Max 15 setups" (O:2377-2382, O:2536); "8-15+" per week (O:2085) | no weekly cap; 3 per category per pair; 24 minimum (C:466-471, C:996, C:1011) |
| A-9 | Dedup key | "(direction, entry at 2-decimal precision) across ALL categories" (O:2385) | anchor-zone-id / anchor bucket + day; `(zoneId, reactionEvent.session)` (C:463-464, C:471, C:788) |
| A-10 | Setup universe | 7 shapes (O:2077-2083) | 12 rows, adds PBS, RS, RWL, PWL, PRWL (C:96-107) |
| A-11 | Trading-speed day shift | "shift setups +1 day from initial prediction" unconditional (O:2119, O:2321) | +1 day only where E2 confidence < 65% (C:123, C:537, C:617) |
| A-12 | 1-2-3 retest | 0 "NO ENTRY unless BoM"; 1 "SCALP ONLY (if BoM)"; 2 "SCALP CONFIRMATION"; 3+ "SWING ENTRY VALID" (O:2336-2339) | 0 "Scalp only"; 1 "Scalp + Confirmation"; 2 "Swing entry valid"; 3+ "TP target only" (C:1152-1155), though headed "preserved verbatim" (C:1148) |
| A-13 | Reinforcement timing | "ONLY valid AFTER the 1-2-3 pattern is complete" (O:2343) vs set up in London premarket (O:2875, O:3044) | Placed premarket as pending stop-limit; ACTIVE only after 1-2-3 completes; cancelled at parent TP (C:625) |
| A-14 | Reinforcements inside primary SL | "At least 2 reinforcement entries must be inside the SL of the primary trade" (O:2900, O:2950) | "≥2 reinforcements inside primary SL → reject the additional ones" (C:660) |
| A-15 | Ladder order placement | "Place stop orders at the FAR EDGE of each zone" (O:2893) | stop-limit trip-wire, limit at entry zone (C:682-691) |
| A-16 | Sizing | "Primary = full size. Reinforcements = 50-75% of primary" (O:2952); scaled entry 33/33/33 (O:2692-2694) | 50/30/20 (C:633); 33/33/34 (C:1064-1066) |
| A-17 | Scaled entry | First touch / mid-confluence / far edge; "SL = based on the worst-case entry"; "TP = based on the average entry price" (O:2692-2696) | Front / Middle / Back with forward spread; SL cascade to breakeven (C:1064-1071) |
| A-18 | 70-80% rule | "Move SL to 65-70% profit when price reaches 70-80% of TP and starts reacting" (O:2955) | "take 70-80% at TP1, run 20-30% for extension" (C:664) |
| A-19 | Profit taking | "Close ALL open trades by NY market close. No London-mapped trades run overnight" — daily (O:2961-2965) | "Close ALL positions by NY close Friday" — weekly (C:666) |
| A-20 | Triple Anchor | three zones: stop zone target, entry zone, stop-loss zone (O:3082-3086) | "the SL of the rocket is placed inside the entry zone of the parent trade" (C:693) |
| A-21 | 4-point entry criteria | front edge/middle, back edge, front edge of SL zone, middle/back edge of SL zone (O:3068-3073) | trigger zone, entry zone, SL zone, TP zone (C:688-691) |
| A-22 | Rocket SL by session | "NY session: 2-3 pips outside. London session: 1-2 pips outside"; "NY session rockets require 3 pip SLs minimum" (O:3078, O:3029) | "1 pip outside back edge of next LQZ rung" (C:690); session split dropped |
| A-23 | Swing-scalp procedure | Part VII-B: Types 1-4, SL "1.5-2 pips" beyond 15m zone edge, TP at 30m opposite boundary, range < 15 pips REJECT, typical SL 3-6 / TP 15-30 pips, 2-3 snipes per move (O:2744-2816) | Deleted (C:33); no replacement procedure |
| A-24 | Reversal pattern | 6 steps incl. "SL = nearest liquidity zone beneath the flipped support", "TP = fib wormhole level" (O:2133-2147) | 3 steps BoS / Flip / Retest (C:168-171) |
| A-25 | Fib anchors | Context 1 "Deepest + Most Recent swing high/low. Must be BoM anchors"; scalp buffers "Entry: 0.5-1 pip buffer; SL: 1 pip buffer; TP: 1.5-2 pip buffer" (O:2157-2166) | Context 1 "Fib retracements from prior week's H/L" (C:207); scalp buffers dropped |
| A-26 | Session assignment | by shape: SS → London; BS/WL → NY ("95% start 2nd half NY"); R both; SS→BS London setup, NY activation (O:2120-2126) | by day default + category default + liquidity score (C:559-576) |
| A-27 | Red Folder events | FOMC, NFP, CPI, GDP, PMI, Retail Sales, ISM, ECI, PCE (O:3226-3235) | "CPI, PPI, NFP, FOMC" (C:1125) |
| A-28 | IP zone as entry | "The broken IP resistance zone FLIPS to support — this is the entry" (O:2137) | IP zones "NEVER entries" (C:136) |
| A-29 | Counter-trend sizing | Hard Wall within 0.30 DXY → "reduced position size (half of normal)" (O:2664-2666) | HIGH → Quarter, MODERATE → Half (C:1095) |
| A-30 | Rocket detail dropped | Shorter-move rocket levels (O:2913-2920); trigger zone "2-3 zones IN FRONT of entry zone" (O:3056); trigger price "1-2 pips INSIDE" (O:3063); "We DO NOT reinforce THIN LIQUIDITY ZONES" (O:3031); "Rockets on ONE pair at a time" (O:3027); 4H cascade "3-4 reinforcements", "SL buffer: 3-5 pips minimum" (O:2972-2973) | Not restated in C. UNKNOWN whether still in force. |
| A-31 | Chain rules | direction flips at each boundary; each trade meets min RRR independently (O:2703-2705) | sort + 3-pip link; depth 3; chain RRR ≤ 15 (C:447-450, C:1121) |
| A-32 | Reinforcement day | "inherit the DAY of their parent trade + 1 day buffer for activation" (O:2507) | parent reference only (C:614); no day rule |

### 8.B Conflicts INSIDE the corrected spec (unresolved — operator ruling needed)

- **B-1 RRR floor.** "Emission floor: RRR ≥ 3.0 (all categories)" (C:362) vs "Floor: RRR ≥ 2.5" in `checkMirrorFloorV45` (C:854) vs "Consolidation week (relaxed) | 2.5" (C:1115) vs quality tiers that admit "rrr ≥ 2.0" and "rrr ≥ 1.5" (C:421-422).
- **B-2 SL size.** "GOLDEN_SL_MAX_PIPS = 9.5" used as the SL envelope (C:856) vs "D17 SL ceiling = 36 pips HARD" (C:309) vs confidence penalties that only start at 50/80 pips and `SL_MAX_PENALTY` EUR 100p (C:400, C:408) vs "95% of SLs < 150 pips and 60-70% < 100 pips" (C:183).
- **B-3 DXY buffer unit.** "DXY | 5 (idx pts)" (C:304) with "Pip 0.01" (C:1101): 0.05 or 5.00 not stated.
- **B-4 SL offset.** 3 pips outside / 1-2 pips inside (C:254-255) vs Law-7 per-pair buffer 2 / 3 / 5 (C:299-304) vs rocket 1 pip (C:307). C never says which applies when.
- **B-5 One TP.** "ONE TP per trade ... No partial take-profits" (C:313) vs "take 70-80% at TP1, run 20-30% for extension" and "after partial TP" (C:664-665).
- **B-6 TP edge.** "NEVER target FAR edge of distant zone" (C:321) vs "WEAK ... → FAR edge (maximize catch)" (C:329); and overlap → "MIDPOINT" (C:319) vs STRONG → "CLOSE edge (near edge) + 1-2 pip spread" (C:328) vs "projected opposing zone defendedEdge FIRST" (C:334).
- **B-7 F1-A.** "lift the entry 1 pip above the supply zone's bottom edge" vs "This places entries in the UPPER half of supply bands" vs example 101.027 → 101.14 (C:186-188).
- **B-8 Retest vs freshness.** VIRGIN is "the strongest (BoM: 100% reaction ...)" (C:154) and the gate only skips battle index > 2 (C:150), vs retest 0 = "Scalp only", swing only at retest 2 (C:1152-1154), vs rule 7 "no scalp entry before 2nd retest" (C:1007).
- **B-9 Repair scope.** "entry FIXED — re-anchor SL/TP only" (C:378) vs "3 E, 3 SL, 3 TP refinement attempts each" (C:386).
- **B-10 Confidence gate.** "confidence ≥65 required for inclusion" (C:1011) vs STANDARD ≥ 60 and CONDITIONAL ≥ 50 emitted tiers (C:422-423). Two confidence scales also coexist: 0-100 (C:404) and 0-1 `mirrorConfidenceScore` (C:274-286).
- **B-11 Session.** E2 session label is law (C:77) vs per-day default Mon/Wed/Fri LONDON, Tue/Thu overlap (C:560-561) vs category default (C:565-571) vs category table London / NY / NY / NY Open (C:144-147).
- **B-12 Category vocabulary.** `Consolidation / Reversal / HTF Swing / Reinforcement` (C:142-147); `HTF_SWING / SWING_SCALP / REINFORCEMENT / TRANSITION` (C:508-512); `SWING_SCALP / BREAKOUT_SURGE / HTF_SWING / REINFORCEMENT / TRANSITION` (C:567-571); enum `'HTF Swing' | 'Swing Scalp' | 'Breakout Search' | 'Reinforcement' | 'Transition'` (C:1193); RRR table adds `Reversal`, `Consolidation` (C:1110-1114).
- **B-13 Shape lists.** Matrix has 12 rows (C:96-107); `MacroShape` has 11 values and no 'SS→BS' (C:1191); `categoryShapeMap` omits PWL everywhere and omits PBS/PRWL from REINFORCEMENT (C:509-512) though the matrix gives them reinforcements (C:99, C:105).
- **B-14 Counts.** "no limit" (C:468) vs "Max 3 setups per category per pair" (C:1011) vs 4–8 swing scalps per SS day (C:96) vs 24 minimum (C:996).
- **B-15 Phase numbering.** Fix table says Multi-Setup "Promoted to formal Phase 10" (C:56), body says Phase 6 (C:426). Note says "5 (RRR)" (C:233), body Phase 5 = Confidence (C:388). Avatar steps cite "Phase 6" for macro shape and "Phase 4.3 Fibonacci Spiderweb" (C:808-809); spiderweb is Phase 3 (C:173). Integration table cites "§8.4.1" (C:1023) which does not exist, and maps "Primary Shape Chain | Phase 1 | §8.0.1" (C:1029) where §8.0.1 is Phase 0.
- **B-16 Trading-speed applied twice.** Phase 1 step 6 propagates the shape (C:123) and Phase 7 step 8 shifts the setup day (C:537), the latter keyed on `matchingDays[0].confidence`, not on the day actually chosen in step 5b.
- **B-17 `assignDay` control flow.** Steps 4 and 5a "continue to Phase 7.2" (C:504, C:520), which skips steps 6-12 (red folder, speed shift, anchor window, cascade validation) for the single-match case.
- **B-18 Cascade ordering.** Phase 7 step 11 validates `cascadeSource` (C:548-551) but mirrors are only generated in Phase 10 (C:725).
- **B-19 Rocket cap wording.** "§8R.6 Law 1" (C:718, C:1058) vs "Law 11 of §8R.6" (C:1079); C's 8R.6 contains no numbered laws.
- **B-20 Entry sources.** IP "NEVER entries" (C:136) vs Avatar "Earth: Entry at liquidity zone / IP zone" (C:704).
- **B-21 Reinforcement sizing vs caps.** 50/30/20 covers primary + 2 rockets (C:633) vs "2–3 reinforcement entries" (C:621) and "Max 3 rockets" (C:1080); no weight for a third rocket.
- **B-22 Reinforcement floor.** Reinforcement RRR floor 3.0 (C:1113) while rocket own-TP is not in `ReinforcementEntry` (C:1395-1411); how a rocket's RRR is computed is UNKNOWN.

### 8.C Golden standard (T) vs corrected (C)

- **C-1 Entry edge.** "30m zone edges for swings: entry at zone ceiling (SHORT) or floor (LONG)" (T:50) vs "SHORT from supply: Enter at BOTTOM edge of supply zone; LONG from demand: Enter at TOP edge of demand zone" (C:179-180).
- **C-2 SL size.** "5-15 pips (median 12 pips, NEVER above 25 pips for standard entries)" (T:67) vs golden 4–9.5 with `GOLDEN_SL_MAX_PIPS = 9.5` as envelope (C:291-294, C:856) and 36 hard ceiling (C:309).
- **C-3 Rocket Fib levels.** R1 1.382, R2 1.618, TP 2.382+ (T:106-115) vs Rocket 1 1.382–1.786, Trigger 2.382–2.786, Target 3.382–3.786 (C:644-647).
- **C-4 Ladder SL.** "All entries share primary SL (or each has own SL behind LSZ)" (T:136) vs "Each rocket has its OWN SL (no shared SL)" (C:634).
- **C-5 Depleted zones.** T allows a breakout entry on a depleted zone "IF a fresh LTF zone exists at the same price" (T:306) vs C "DEPLETED (3+ battles) → TP target ONLY" and abort `ZONE_DEPLETED` (C:160, C:1052).
- **C-6 TP timeframe.** 15m entry → 4H TP observed 8/38 (T:560) vs "15m ... Cannot target 4H — too far" (C:1175).
- **C-7 Fib anchor.** "Swing high = entry zone ceiling, swing low = entry zone floor" (T:97) vs C's three contexts anchored to prior-week / 15m / 30m swings (C:205-209).
- **C-8 Zone state at 1 touch.** T: 1x mitigated = "ENTRY-PRIMARY (tested once, still strong)", 2x = "ENTRY-CONDITIONAL" (T:529-530) vs C retest table where swing entry needs retest count 2 (C:1154).
- **C-9 Candle confirmation.** T lists entry confirmation candles (engulfing 18/38, pin bar 12/38, inside bar 8/38, breakout candle 6/38, piercing wick 5/38; T:543-547) and Law 18 "candle confirmation" (T:713). C has no candle-confirmation step: UNKNOWN whether required.
- **C-10 Blind-execution checks.** "18 blind-execution checks (BE1-BE18)" (T:730) vs BE1–BE12 (C:602).
- Consistent: session-by-category map (T:590-593 vs C:565-571); sizing 50/30/20 (T:576-578 vs C:633); SL cascade to breakeven (T:137-138 vs C:635); TP TF ≥ entry TF (T:564 vs C:350).

### 8.D Operator count rule vs spec
- **D-1** — see section 3.7. BRIEF "max 1-2 real moves per day, 6-10 per week, never more than 11 per pair per week" vs C "no limit" (C:468), "4–8 swing scalps" per SS day (C:96), "24 minimum (8 DXY + 8 EU + 8 GU)" (C:996).

---

## 9. UNKNOWN (source silent) — collected

1. Order type of the PRIMARY entry (limit vs stop) — not stated in C.
2. Bodies of every function in 0.7; contents of audits P1-P8, C1-C6, T1-T8.
3. `liquidityScore`, `anchorBucket` width, `util`, fuel INTACT/ABSORBED test, "significance" ranking, `vz.confidence` source without a VLM.
4. How the Law-7 buffer combines with the 3p / 1-2p ladder offsets; exact value inside "1-2 pips".
5. Whether the original regime-conditional TP table still applies.
6. How a both-direction SS day is represented and how many scalps per SS day survive a per-day cap.
7. Whether WL / RWL / PWL / PRWL trades go with or against the shape spike.
8. Swing-scalp-specific E/SL/TP procedure under C (deleted with Part VII-B).
9. "Breakout Search" category definition.
10. Rocket TP and rocket RRR computation; weight of a third rocket.
11. Clock times of London Mid and NY Close; timezone/DST handling.
12. How Avatar / GOD_TIER is reached without `vlmSourced`.
13. Use of the confluence-stack total (no threshold given).
14. Whether candle confirmation at the zone is required before entry.
15. How any object is rendered on the chart (C is silent; Part X not read here).
16. Source line for the BRIEF's 1-2 / 6-10 / 11 counts.

---

## 10. Derived skeleton (ordering only; every line is a quoted rule; unresolved choices marked)

```
for pair in [DXY, EURUSD, GBPUSD]:                      # DXY "Processed FIRST" (C:1101); pair's E1 runs first (C:744)
  universe = setupUniverse(E2.days)                      # Phase 0, matrix C:96-107
  wdm = buildWorkingDayMap(E2.days)                      # Phase 1, C:118-125; conf<0.65 spill [B-16]
  for day in wdm:
    for dir in directionsAllowed(day):                   # day.direction; SS-family both [UNKNOWN 6]
      anchor = dir==LONG ? day.demandZoneId : day.supplyZoneId   # C:132 (keyZoneId fallback)
      require anchor.source in {ORDER_BLOCK, LQZ}        # C:135
      require anchor on correct side of spot             # C:129
      require battleIndex <= 2 and never pierced         # C:150
      require retest rule for category                   # C:1152-1155 [B-8]
      entry = sniperEdge(anchor, dir)                    # SHORT bottom / LONG top, C:179-180 [C-1]
              then F1-C internal rung, F1-A, F1-D, F1-E  # C:186-200 [B-7]
      sl    = ladderStepsSL(...)                         # C:253-260, branch C:285-286; golden fallback C:291-294 [B-2,B-4]
      tp    = computeLmvTP(...)                          # ONE TP, C:313-344 [B-5,B-6]
      if sl invalid or tp null: no emission              # C:1016
      rrr   = |tp-entry| / |entry-sl|                    # C:356
      repair up to 3x on same anchors until rrr >= 3.0   # C:374-383 [B-1,B-9]
      conf  = confidenceScore(...)                       # C:393-414
      quality = classify(conf, rrr)                      # C:420-424; include only if conf >= 65 (C:1011) [B-10]
  matrix, chains, conflicts = phase6(setups)             # C:447-464; cap 1 per (pair, anchorBucket, day) C:471
  assign day / session / anchor hit window               # Phase 7, C:483-595 [B-11,B-17]
  require 5 labels                                       # Phase 8, C:600
  reinforcements for HIGH/GOD HTF swings (2-3, max 3)    # Phase 9, C:621, C:1080
EU mirrors from DXY (inverse), GU mirrors from ACTIVE EU (kept)  # Phase 10, C:755-780
avatar for GOD_TIER HTF swings                           # Phase 11, C:804-813 [UNKNOWN 12]
3D audit + floor + CS-1 + narrative gate                 # Phase 12, C:825-878
apply operator count rule                                # BRIEF [D-1, unresolved]
```
