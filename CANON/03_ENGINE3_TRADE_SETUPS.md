# CANON 03 — ENGINE 3 (CORRECTED): TRADE SETUP ARCHITECTURE (WHERE DO I SURF?)

Authority: `Original_Canon_Data/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md` (1685 lines).
**The E3 in the ORIGINAL v5.3.3 was broken (18 breakage points). THIS is the fixed engine.
It is UNTESTED live** — it gets validated through the finished indicator.

---

## 1 · WHAT E3 IS (and what it is not)

> **E3 is NOT a trade generator. E3 is a classification + precision-alignment engine** that
> consumes E1's zone map + E2's storyline designation and produces `TradeSetup`s — each anchored
> to a specific **E1 zone ID** + an **E2 shape day**, never fabricating its own rules.

**The R3 LAW (verbatim, operator 2026-08-04):**
> **E2 DESIGNATES, E3 OBEYS.** Every order leg's session bracket comes from the E2 session label.
> Every anchor traces to an E1 zone ID + an E2 shape day. E3 never overrides E1/E2 data.

**The E1→E2→E3 architecture (verbatim):** each engine BUILDS ON the previous; previous engine
data PROVIDES THE STRUCTURE for the next; the next engine's data MUST FIT WITHIN THE CONSTRAINTS
of the previous engine's data architecture. **Absolutely non-negotiable.**

**The E3-NEVER rule:** E3 is not permitted to override pre-existing E1/E2 data architecture, nor
to randomly fabricate its own rules.

**E3's single responsibility (verbatim):** it takes each E2 ShapeDayZone day (which zone, which
side, which day/session, how confident, what shape) as **authoritative** and resolves ONLY the
executable geometry — the entry at the anchor's internal-LQZ near/deep edge, the SL at the ZR-1
operative-defense ladder step (or golden reaction-extreme fallback), the TP at the Law-14
opposing-rung walk — then proves it through the 3D audit, the RRR repair on the same anchors, the
day-native CS-1 and narrative guards, the per-anchor emission cap, the dedup identity, and the
session-bracketed fill simulation. **Never re-designating. Never converting prices. Never
inventing levels.**

---

## 2 · THE 12-PHASE PIPELINE

```
Phase 0  Setup Universe Classification   (E2 day shapes → which setup types are valid)
Phase 1  Day-Level Bridge                (E2 day decomposition → WorkingDayMap[])
Phase 2  Zone Selection + Market Structure + Reversal detection
Phase 3  Entry Identification + Fib Spiderweb Anchoring
Phase 4  Confluence Stack + SL + TP + RRR
Phase 5  Confidence Scoring + Quality Classification
Phase 6  Multi-Setup Architecture        (matrix + trade-flow chains + conflicts)  [MANDATORY]
Phase 7  DAY + Session Window + Anchor Hit Window assignment
Phase 8  Blind-Execution Labeling        (BE1–BE12)
Phase 9  Reinforcement Architecture      (8R.0–8R.10)
Phase 10 Cascade Mirror                  (DXY → EU → GU)
Phase 11 Master Trade Setup Construction (Avatar State)
Phase 12 3D Refinement Audit + Final Validation
```

---

## 3 · PHASE 0 — THE SETUP UNIVERSE (≥12 shapes)

| E2 shape | Setup universe | TF stack | Expected count |
|---|---|---|---|
| SS | swing scalps (both directions) | Scalp 30m/15m/5m | 4–8 |
| SS(DWL) | swing scalps + DWL Inverse | Scalp | 4–8 + 1–2 |
| BS | HTF swing + reinforcements | Swing 4H/1H/30m | 1 + 2–3 |
| PBS (ZFP > 70%) | HTF swing + reinforcements | Swing | 1 + 2–3 (deeper targets) |
| R | swing scalps + recovery surge | both | 2–4 |
| RS | HTF swing | Swing | 1 |
| WL | HTF swing | Swing | 1 |
| RWL | HTF swing | Swing | 1 |
| PWL | HTF swing | Swing | 1 |
| PRWL — **strongest reversal** | HTF swing + reinforcements | Swing | 1 + 1–2 |
| WLS | swing scalps + DWL Inverse | Scalp | 4–8 + 1–2 |
| SS→BS transition | transition entry | both | 1 + reinforcements |

**The 4 setup categories:**
| Category | Shapes | Session |
|---|---|---|
| Consolidation | SS, R, WLS | London |
| Reversal | RWL, R (when reversing) | NY |
| HTF Swing | BS, WL, PBS, RS | NY |
| Reinforcement | ladder/rocket add-ons | NY Open |

---

## 4 · PHASE 1 — THE DAY-LEVEL BRIDGE

**Input:** E2's day-by-day decomposition (Mon–Fri: shape + direction + key zone + triggers + conf).
**Output:** `WorkingDayMap[]` — 5 entries of
`{dayIdx, day, shape, direction, keyZoneId, keyZoneType, supplyZoneId, demandZoneId,
deepDemandZoneId, dayOpenSpot, session, confidence}`.

Steps: read E2's Mon…Fri entries into slots 0…4 → apply the **Trading Speed Adjustment** (if E2
confidence < 65%, the shape *spills over* to the next day — today's move becomes tomorrow's) →
validate (5 entries, no null shape, every `keyZoneId` resolves to an E1 zone) → emit.

**This is the direct E2→E3 coupling.** If E2's day decomposition is missing, E3 cannot assign
DAYs and the output is non-executable.

---

## 5 · PHASE 2 — ZONE SELECTION, STRUCTURE, REVERSALS

**The direction-appropriate anchor (decisive fix):**
> The **LONG** mirror → the `demandZoneId`. The **SHORT** mirror → the `supplyZoneId`. The
> `keyZoneId` is the fallback. **NEVER anchor a LONG at SUPPLY** — wrong side, hard error, never
> a silent emission.

**DECISION-1 — IP zones are NEVER entries.**
- `STRUCTURAL_ENTRY_SOURCES = ['ORDER_BLOCK', 'LQZ']` — the only valid entry-anchor sources.
- IP zones (`source === 'PILLAR'`) are confluence / ZFP / context + SL & TP rungs — **never
  entries**. The mirror anchor-search **skips** `source === 'PILLAR'`.
- IP classification must be `'CONFLUENCE'`, **never** `'MoM'` (that would drag IP into S/D
  battle semantics and the virgin-MoM death rule).

**The 4-stage Freshness Gate (freshness AT BATTLE TIME — not model freshness):**
- Index `i > 2` is **skipped** — the 4th+ battle is DEPLETED/consumed structure.
  Recurrence ladder: **UM 100% · 1x 80% · 2x 50% · 3x+ TP-only.** (Trading the 6th touch is the
  "DXY=39" slop.)
- Any prior **pierced** event = **VIOLATED terminal** — the level closed through; never an entry
  again. Admissibility is evaluated on the group's **earliest clean battle**.

**The zone pressure lifecycle (Architecture Bible §15.1):**
```
VIRGIN (0 battles)      → the UM zone — strongest (BoM: 100% reaction; MoM: DEATH ZONE counter-trend)
   ↓ first battle
ACTIVE-1 (1 battle)     → ~80% reaction rate — has juice
   ↓ second battle
ACTIVE-2 (2 battles)    → ~50% — weakening
   ↓ third battle
DEPLETED (3+ battles)   → TP TARGET ONLY — the zone will fail
   ↓ fourth+ strong battle
FORTRESS (4+ strong)    → the Fire→Earth phase transition — 95% direction flip — immovable
   ↓ pierce with a battle
BROKEN (VIOLATED)       → terminal — the level closed through — never offers an entry again
                          (role reversal: broken support becomes the new resistance)
```

**The reversal pattern (ALL THREE required):**
1. **Break of Structure (BoS)** — price breaks the most recent opposing swing (lower-high for a
   bullish reversal; higher-low for a bearish reversal).
2. **Flip** — the broken swing's role flips (resistance→support for bullish; support→resistance
   for bearish).
3. **Retest** — price retests the flipped level from the new direction; **entry at the retest**.

---

## 6 · PHASE 3 — ENTRY IDENTIFICATION

**TS-1 — THE SNIPER ENTRY (the operator's #1 fix in the v8 Python engine):**
> **SNIPER ENTRY = the zone edge CLOSEST to the approaching price.**
> - SHORT from supply → enter at the **BOTTOM** edge of the supply zone.
> - LONG from demand → enter at the **TOP** edge of the demand zone.
> - If key levels exist inside the zone, use the one closest to the approaching edge.

Rationale: it minimises SL distance while keeping structural safety. The operator's real trading
has **95% of SLs < 150 pips, 60–70% < 100 pips**, average **RRR 4–6×**.

**Operator-measured entry refinements (never generalise beyond their scope):**
- **F1-A Short-Entry Edge Lift** — *OB SHORT only*: lift the entry **1 pip above** the supply
  zone's bottom edge (places the fill in the upper half of the band). Without the OB-only scope
  pin, LQZ-rung lifts move entries into rally wicks (losses). Measured: Monday band bottom
  101.027 / defEdge 101.092 → RRR 1.79 (rejected); operator 101.14 → **RRR 4.92** at the same
  SL/TP walk.
- **F1-C Internal-Rung Entry** — when the S/D band *contains* an internal LMV rung, entry = the
  internal rung's **near** edge (SHORT = rung floor, LONG = rung ceiling) — **not** the zone's
  `defendedEdge` (that is the *reinforcement* level, a different trade).
- **F1-D RWL Bounce-Inset** — `RWL_BOUNCE_INSET_PIPS = 0.2`: LONG bounce entries pulled inside
  the rung ceiling by 0.2 pips. Without it the Wed shelf ceiling 100.972 → RRR 2.97 (a hair miss
  of the 3.0 floor). With it, RRR passes. `RWL_HAIR_MISS_RRR_DELTA = 0.1` — setups with RRR in
  `[floor − 0.1, floor)` get **one repair attempt** before hard reject.
- **F1-E Prior-Week Recovery Shelf** — when the entry zone is a prior-week recovery shelf
  (deep-wick anchor + DEMAND rungs above + defended bullish transit + ≥2 day-closes inside the
  band), pull the entry to the shelf centre: `RWL_SHELF_LONG_ADJUST_PIPS = 1`.

**Fibonacci Spiderweb anchoring — 3 contexts:**
| Context | TF | Use case | Anchor source |
|---|---|---|---|
| 1 | 1H | BS / WL on 1H shapes | Fibs from prior-week H/L + 0.382→1.382 wormholes |
| 2 | 15m | SS / recovery / scalps | Fibs from 15m swing H/L + 0.5/0.618 golden pocket |
| 3 | 30m | mid-swing / same-day | Fibs from 30m swing + 0.786 deep entry / 1.272 extension TP |

**Fib wormholes:** 0.382↔1.382 · 0.5↔1.5 · **0.618↔1.618 (strongest — highest-frequency reaction
point)** · 0.786↔1.786 · 1.0↔2.0.

---

## 7 · PHASE 4 — CONFLUENCE, SL, TP, RRR (the interlocking triangle)

### 7.1 Confluence stack (7 layers)
| Layer | Captures | Score |
|---|---|---|
| 1 | Tier 1/2 POI confluence (overlap with 4H BoM) | +2 / +1 / 0 |
| 2 | Three-tier option classification | +3 critical / +2 significant / 0 |
| 3 | Reaction counter alignment | **UM BoM +5 · MoM −10 · Depleted REJECT** |
| 4 | Timeframe stack compliance | +3 / 0 (violation = REJECT) |
| 5 | Day-shape alignment | +5 aligned / 0 / **−5 misaligned** |
| 6 | Session mechanics | +3 London / +2 NY / 0 Asian |
| 7 | Storyline bias alignment | +5 aligned / −5 counter-trend (needs exceptional confluence) |

### 7.2 SL PLACEMENT (TS-2 / TS-8 — the ladder-steps model)
> **"3 pips outside the back edge of the entry zone, or 1–2 pips inside the close edge of the
> next rung relevant zone."** — operator verbatim

SL = **either** (a) 3 pips outside the **far** edge of the current entry step, **or** (b) 1–2 pips
inside the **close** edge of the **next step away** (opposite the trade direction).

**Which zone is "relevant" is chosen by the pressure state of *that* trade:**
- fuel **INTACT** → the LQZ acting as shield in front of the S/D (`LQZ SHIELD_FUEL`)
- fuel **ABSORBED** → the S/D itself as backstop (`S/D PRESSURE_STRUCTURE`)
- neither → the **Golden SL** fallback (`computeGoldenSL_V452`)

**Golden SL fallback:** `computeSL_LMV` 4–9.5p reaction-extreme + selective util guard tighten
iff util < 0.40 + wick-clear. **D17 ceiling = 36 pips HARD** (the measured golden SLs are
4–9.5 pips; 36 is the safety ceiling).

**Per-pair SL buffer (Law 7):** EUR/USD **2** (tightest spread, deepest liquidity, shallow 1–2p
hunts) · GBP/USD **3** (wider spread, ATR 1H 10–18p, deeper 2–3p hunts) · AUD/USD **3** ·
DXY **5 index points**.

**Rocket SL doctrine (verbatim):** *"ROCKET STOP LOSSES ALWAYS 1 FULL PIP OUTSIDE BACK EDGE OF
ZONE — NO EXCEPTIONS!!! ESPECIALLY IF THIN!!!!!"*

**Mirror confidence score:** base 0.5 `+0.2` if shapeConf ≥ 0.65 · `+0.15` VIRGIN or ACTIVE_1 ·
`−0.2` DEPLETED · `+0.15` INTACT · `−0.2` ABSORBED · `+0.1` if shapeDay direction matches.
**ZR-6B S3 branch:** confidence ≥ 0.6 → RR-tight (3p back edge); < 0.6 → safety (next-rung).

### 7.3 TP IDENTIFICATION — REGIME-CONDITIONAL, **SINGLE TP**
> **ONE TP per trade. Period. No TP1/TP2/TP3, no partial take-profits.** The blended RRR is
> across the 3 staggered *entries*, not across multiple TPs.

Rules (Laws 11–14): TP at the **opposing pressure** — the nearest opposing S/D zone where the LQZ
sits **inside** the S/D zone (Earth+Fire convergence). LONG → nearest SUPPLY above; SHORT →
nearest DEMAND below. If S/D ∩ LQZ overlap exists → TP at the zone **MIDPOINT**. If **no** LQZ
overlap → TP at the zone **NEAR EDGE** (quick exit). **NEVER** target the far edge of a distant
zone.

**Strength-driven edge (operator verbatim):** *"the stronger the pressure of the zone, the weaker
the mitigation will be prior to the reaction. Strong pressure zones = near instant reaction —
exit on the closest zone edge and even potentially add a 1–2 pip spread so you don't miss the
exit. Weak pressure zones = delayed reaction — maximize the profits you catch from these while
the candles are still inside of them."*
| Zone strength | TP placement |
|---|---|
| STRONG (BoM, high confluence, fortress) | **CLOSE/near edge** + 1–2 pip spread |
| WEAK (virgin MoM, low confluence) | **FAR edge** (maximise the catch) |

**Law-14 TP walk:** the E2-shapeDay projected opposing zone's `defendedEdge` is tried FIRST, then
a significance walk; fresh-wall **zfp ≤ 20 cap**; then the E1 wall strength-driven rung TP. Weak
shelf pass-through is **REJECTED by measurement**. Fallback `computeMirrorTP`; else `TP_NULL`
discard. **Precondition: `TP ≥ 1.2 × SL`.**

**Refined Law 14 (verbatim):** *"Price cannot teleport past UNMITIGATED zones. Price CAN pass
through mitigated zones during BS momentum. The 'no teleport' constraint applies ONLY to zones
with reactionCount = 0."*

**TP timeframe law:** TP timeframe ≥ entry timeframe. 15m entry → 30m or 1H TP. 1H entry → 4H TP.

### 7.4 RRR
`Primary = |TP − entry| / |entry − SL|`. `Blended (3 staggered) = rrr1×0.33 + rrr2×0.33 + rrr3×0.34`.

**IRON LAW (operator 2026-07-31):** *"MINIMUM 3 RRR NOTHING LESS IS ACCEPTABLE… ALL MY TRADES ARE
4+ SO 3 IS THE MINIMUM."*
- **Emission floor: RRR ≥ 3.0** (all categories) — enforced **in code, never by the model**.
- Executed standard 3.5 · norm 4.0+ (operator's average 4.0–6.4×).
- Consolidation week (relaxed): floor 2.5 · standard 3.0.
- **`MAX_CHAIN_RRR = 15.0`** (Law-13) — chains past 15R fill-and-stop.
- **RRR is a CONSEQUENCE of zone geometry, never a forced target.** Never distort zone structure
  to hit an RR.

**RRR-Failed ≠ Hard Reject (D36, operator verbatim):** *"When a trade setup is rejected it should
not immediately hard reject. It should give context WHY, force an IMPROVED setup for the same
trade that does not derail from principles, and try again up to twice. Often it is just a dumb
SL/TP making a trade 1.8 vs 3.6 vs 4.5 RRR. If the trade fails 3 times then hard reject."* —
*"A rejected setup is not a dead setup. **The entry is the hard-won insight; SL/TP are
engineering.** A 1.8-RRR trade with a valid entry is a good trade with a dumb anchor."*

**The 3-attempt refinement loop:** attempt → if RRR ≥ floor EMIT; else `refineSetup` on the SAME
anchors (**entry FIXED — re-anchor SL/TP only**): SL = next-rung reactionExtreme + Law-7 buffer,
TP = next-significance-ranked opposing rung defendedEdge; log
`🔧 REPAIRED(n): SL re-anchored {old}p→{new}p, RRR {old}→{new}`. After 3 failures → HARD REJECT
with the full audit trail. **Per-anchor lock discipline:** 3 attempts per EACH anchor, tracked
and locked individually per trade — a dynamic state machine that locks what has exceeded its
3-turn limit while allowing attempts on the others.

---

## 8 · PHASE 5 — CONFIDENCE

```
base = vz.confidence (VLM visual zone confidence, typically 50–95)
 + min(15, ipZone.confluence × 1.5)          IP confluence bonus
 + 5   if ipZone.isBoM
 + 8   zone-direction alignment (SUPPLY→SHORT / DEMAND→LONG)
 + 5   storyline bias alignment
 + 7   if vz.source !== 'FALLBACK_IP_EDGE'   VLM-sourced bonus
 + 5   if rrr ≥ 3 ;  +3 if rrr ≥ 2
 − 10  if slDistancePips > 80 ;  −5 if > 50
 − 8   if distPips > 150 ;  −4 if > 80
 + 3   prior-week momentum aligned ;  −8 if misaligned
clamp [0, 100]
```
**Three-band SL-distance ±** (from the Python E3 v8 — a falsifiable feedback loop):
`sl > SL_MAX_PENALTY[pair] → −10` (EUR 100p · GBP 120p · AUD 100p · DXY 30 idx) ·
`sl < 30p → +10` · `sl < 60p → +5`.
**DXY cascade bonus** `+10` if the setup is cascade-source. **GU short-squeeze override** `+5`
for GBP/USD LONG (no double penalty on GU SHORT MoM — already penalised by the MoM modifier).

**Quality classification:** `GOD_TIER` conf ≥ 90 AND rrr ≥ 3.0 AND vlmSourced · `HIGH` conf ≥ 80
AND rrr ≥ 2.0 · `STANDARD` conf ≥ 60 AND rrr ≥ 1.5 · `CONDITIONAL` conf ≥ 50 (conditional zones
only) · `REJECTED` conf < 50.

---

## 9 · PHASE 6 — MULTI-SETUP (mandatory)

Build the `TradeSetupMatrix` (one row per setup: setupId, day, pair, direction, category, quality,
entry, sl, tp, rrr, confidence, session, shapeTrigger, anchorZoneId, dayCatalysts, tradeFlowRef).

**Trade Flow Chains (Law 27): "TP of ONE = ENTRY of NEXT."** Sort by (day, session, entry); link
setup N to N+1 when N+1's entry equals N's TP within 3 pips; emit `CHAIN-{root}-D{depth}`, **max
depth 3 (Law-13)**. Shape links: BS→R, BS→WL, BS→RWL, WL→RWL, SS→BS (range-boundary break becomes
the BS entry).

**Conflicts:** same day+pair+session with opposite direction and entries within 15 pips =
CONFLICT (higher confidence survives); same category within 5 pips = DUPLICATE (dedup by
anchor-zone-id, keep first); same `anchorZoneId` = dedup by anchor bucket + day identity.

**THE CAP RULE (operator verbatim):** *"I explicitly said… max setups should be removed — there is
no limit on trade setups for a week, there is only filtering of shitty dumb garbage setups."*
*"ALL valid setups should be mapped. The filter will kill retarded/hallucinated setups."*
→ **No setup count cap.** The only cap is **`MAX_MIRRORS_PER_ANCHOR_PER_DAY = 1`** (the "GU-x10
destroyer") — key `(pair, anchorBucket, day)`, first kept, rest dropped `EMISSION_CAPPED` with
logged reasons.

---

## 10 · PHASE 7 — DAY / SESSION / ANCHOR-HIT-WINDOW

**The 12-step DAY assignment** (`assignDay`): read the setup's `anchorZoneId` → find WorkingDays
where that zone is the key/supply/demand/deep-demand zone → **0 matches ⇒ ABORT
`NO_DAY_ASSIGNABLE`** → exactly 1 ⇒ assign → multiple ⇒ tie-break: (5a) prefer the day whose
shape matches the setup category:
```
HTF_SWING:     ['BS','WL','PBS','RS','RWL','PRWL']
SWING_SCALP:   ['SS','SS(DWL)','WLS','R']
REINFORCEMENT: ['BS','WL','R','RWL']
TRANSITION:    ['SS→BS']
```
…then (5b) prefer the earlier day, (5c) prefer higher shape confidence.

**Session windows:** London Open / London Mid / NY Overlap / NY Open / NY Mid / NY Close.
**Anchor Hit Window:** the day+session time range in which the anchor is expected to be hit.

---

## 11 · PHASE 8 — BLIND-EXECUTION LABELS (BE1–BE12)

Every surviving setup carries **five** labels; **no label = REJECTED**. The 12 checks:
BE1 DAY · BE2 SESSION WINDOW · BE3 SHAPE TRIGGER (+@day @session) · BE4 SETUP CATEGORY ·
BE5 weekly execution calendar populated · BE6 **every** anchor point has WHEN + WHERE (entry/SL/TP
each carry day+session) · BE7 no setup requires real-time chart analysis (the labels suffice for
blind execution) · BE8 day catalysts listed · BE9 reinforcement entries carry `parentSetupId` ·
BE10 all 5 days covered or an explicit "No qualifying setups — [reason]" · BE11 Profit-Taking Law
documented ("Close ALL positions by NY close Friday", per pair) · BE12 trading-speed adjustment
applied (+1 day where confidence < 65%).

---

## 12 · PHASE 9 — REINFORCEMENT ARCHITECTURE

**8R.0 Timing inheritance (the reconciliation):** reinforcement ORDERS are placed in **London
premarket** as pending stop-limit orders; they become **ACTIVE only when the 1-2-3 pattern
completes on the primary entry**; orders untriggered by parent TP are **CANCELLED**.

**8R.1 Liquidity Ladder (Mechanism B, cross-zone):** reinforcements at *different* zones along the
TP path, scaling into a winning trade as it progresses. Sizing **50/30/20**; **each rocket has its
OWN SL**; SL cascade Rocket1→Primary BE, Rocket2→Rocket1 BE; combined R:R **16–61×**.

**8R.2 Fibonacci Rocket levels:** Entry **0.618–0.786** · Rocket 1 **1.382–1.786** (cleanest,
90% Fib accuracy) · Trigger **2.382–2.786** (trip-wire) · Target **3.382–3.786**.

**8R.3 Multi-zone overlapping risk:** ≥2 reinforcements inside the primary SL → reject the extra
ones.

**8R.4 TP management:** 70–80% at TP1, run 20–30% for extension; BoM re-entry if price retraces to
BoM after partial TP; **close ALL positions by NY close Friday**.

**8R.5 4H BoM cascade:** 4H BoM zones pierce through everything until they reach the 4H
same-element zone on the opposite side. They are the immovable force.

**8R.7 Stop-limit mechanics (NOT regular stops):** a regular stop is a market order on trigger →
slippage 10–20 pips in fast markets. A **stop-limit** detects the trigger, then places a **limit**
at the predetermined entry zone — it fills only at that price or better. **Trip-wire concept:**
the trigger zone detects movement; the rocket fires at the pre-designated entry zone. **If price
never comes back, the limit never fills — ZERO additional risk.**

**4-point precision entry criteria:** (1) trigger zone (the trip-wire, typically 2.382–2.786 Fib)
(2) entry zone (the limit, typically 1.382–1.786 Fib) (3) SL zone (1 pip outside the back edge of
the next LQZ rung) (4) TP zone (opposing BoM or Fib extension).

**Triple-anchor reinforcement:** the rocket's SL is placed **inside the parent trade's entry zone**
— so if the rocket's SL hits, the parent trade goes to breakeven. **Risk-free reinforcement.**

**8R.9 Master Trade Setup = E + FLR (Avatar State):** Earth (liquidity/IP anchor) + Fire (S/D
overlap) + Water (macro shape confirms direction & timing) + Air (Fib web maps the full path to
TP). **`E (Entry) + FLR = Avatar State`.** Mathematical reasoning: if each element independently
confirms at ~80%, `P(all four wrong) = 0.2^4 = 0.0016 = 0.16%` — probability INTERSECTION, not
addition.

**8R.10 Efficient liquidity mapping:** map ALL liquidity zones between entry and TP — each is a
potential reinforcement anchor. **Up to 7 active rockets** with hardwired safety (max 3 per pair;
max 3 rockets per trade). **Profit management (verbatim):** *"If everything cannot be moved 30–50%
in profit we automatically take all profits before market close. Mandatory."*

---

## 13 · PHASE 10 — CASCADE MIRROR (DXY → EU → GU)

**The Cascade Law (operator verbatim):** *"Everything I found on this EU chart maps 1:1 to DXY
EXACTLY simply in the inverse direction. All the zone elements are the same, shapes, trade setups,
etc — LITERALLY EVERYTHING IS THE SAME, the only thing that changes are the actual price levels
between the pairs."*

- **Full-direction cascade:** DXY source → EU mirror (**inverse** direction) → GU mirror (**kept**
  direction).
- **80/20 mirror doctrine:** the mirror is structural equivalence, **NOT** mathematical
  conversion.
- **The 35% divergence rule: FLAG ONLY — never override.**
- **Emergent trades** may be constructed on top of the cascade (trades that exist on the mirror
  but not on the source).

---

## 14 · PHASE 12 — 3D AUDIT + FLOOR INVARIANTS + GUARDS

- **3D audit** (P1–P8 / C1–C6 / T1–T8) runs when `translatedDays` is present.
- **Floor invariants** (`checkMirrorFloorV45`).
- **CS-1 day-native guard:** `CS1_DAY_NATIVE` flag if `openPrice` came from
  `shapeDay.dayOpenSpot`; `CS1_UNCHECKED` honest flag if from `sessionStartPrice`.
- **Narrative gate:** suppress >30 ZFP band unless a Hard Wall exemption applies.

---

## 15 · E3 ZERO-TOLERANCE RULES (16)

1. No trade without a Tier 1 or Tier 2 POI.
2. Direction validation MANDATORY (6-check; 4+ of 6 disagree → REVERSE).
3. Fib anchoring must follow the 3 contexts (1H/BS-WL · 15m/scalps · 30m/same-day).
4. Temporal boundary inheritance.
5. Post-pierce consolidation awareness (no WLS setups immediately after 2 strong piercing moves).
6. BoM/MoM enforcement (no entry at MoM unless ALL 4 exceptions).
7. 1-2-3 retest timing (no swing entry before the 3rd retest; no scalp entry before the 2nd).
8. Sequential zone path (every setup maps the zone path entry→TP).
9. Timeframe stack compliance (Swing 4H/1H/30m · Scalp 30m/15m/5m · 5m refinement only).
10. 30-minute red-folder deferral.
11. **Max 3 setups per category per pair; NO total cap** (operator D38); confidence ≥ 65 to qualify.
12. MoM zones = ladder steps ONLY — no reversal entries at MoM, EVER (supersedes Rule 6 for
    reversals).
13. Mandatory DAY + SESSION + SHAPE + CATEGORY + ANCHOR-HIT-WINDOW labels.
14. Weekly Execution Calendar mandatory.
15. **R3 LAW** — E3 never overrides E1/E2; never fabricates levels.
16. **HONEST ABSENCE** — `SL_INVALID` / `TP_NULL` / `RRR_BELOW_FLOOR` / no-entry-zone /
    no-structural-wall all yield **NO EMISSION**, never a fabricated level.
    **The 90% win-rate target depends on what the code REFUSES to emit.**

**Standard abort reasons:** `NO_DAY_ASSIGNABLE` · `NO_OPPOSING_ZONE` · `NO_LSZ_ANCHOR` ·
`RRR_BELOW_FLOOR` · `CASCADE_DRIFT_EXCEEDED` · `DIRECTION_VALIDATION_FAILED` · `ZONE_DEPLETED` ·
`VIRGIN_MOM_DEATH_ZONE` · `NARRATIVE_MISALIGNED`.

---

## 16 · DIRECTION VALIDATION — THE 6-CHECK

1. **4H trend** — bullish/bearish/ranging → favors long/short/neutral.
2. **BoM alignment** — nearest BoM above/below → favors short/long.
3. **Liquidity sweep** — nearest LSZ above/below → initial sweep up/down.
4. **Zone failure** — failing support/resistance → direction down/up.
5. **Macro shape** — chain description → expected direction.
6. **Counter-trend** — hard wall level → counter-trend risk HIGH/MODERATE/NONE.

**Consensus:** 4+ of 6 disagreeing with the proposed direction → **REVERSE** it (or reject if no
reversal pattern exists).
**Counter-trend sizing:** HIGH risk → quarter size · MODERATE → half · NONE → full.

---

## 17 · E3 OUTPUT FORMAT (the full contract)

```
ENGINE 3 — FULL-SPECTRUM TRADE MAP | WEEK OF [DATE]

═══ WEEKLY EXECUTION CALENDAR (MANDATORY) ═══
Day | Pair | Dir | Setup Type | Entry | Shape | Session | Conf | Notes   [5 rows or explicit "none"]

─── HTF SWING SETUPS ───
#1 | Pair | LONG/SHORT | HTF Swing | Day | Session | Shape
  Entry | SL (anchor zone) | TP (anchor zone)
  RRR primary/blended | Quality | Confidence
  Anchor Zone: id + name + classification (BoM/MoM/IP/LSZ) + reaction count
  Shape Trigger | Day Catalysts | Confluence Stack 1..7
  Audit Trail: entry/SL/TP method + RRR vs floor + repair annotation
  Cascade Source: native / DXY→EU / EU→GU | Parent Trade Ref | Anchor Hit Window

─── SWING SCALP SETUPS ───  (same shape, + Consolidation Phase)
─── REINFORCEMENT ENTRIES ───
R-1 | Direction | Rocket Type FLR/FR/LR | Day | Session | Shape Trigger | Parent Trade Ref
  Trigger Zone | Entry Zone | SL Zone | Buffer Zones (count + thick/thin)
  Fib Level Alignment | Combined RRR With Parent | Audit Trail (trip-wire + limit + risk-free mechanics)
─── TRANSITION SETUPS ───  T-1 | … | Transition Type SS→BS / Post-WL Reverse / DWL-Inverse
─── DAILY SESSION NOTES ─── Mon…Fri + Weekend: "Close ALL positions by NY close Friday"
─── MASTER TRADE SETUPS (Avatar State) ───  M-1 | Direction | Avatar TRUE/FALSE | E | FLR | Water
─── 3D AUDIT RESULTS ───  per setup P1-P8/C1-C6/T1-T8 + discards with reasons
─── WEEKLY STATS ───
Total | HTF | Scalps | Reinforcements | Transitions
Win rate target 90%+ | Average RRR | Median RRR
Cascade coverage: DXY [n] → EU [n] → GU [n]
f(T) acceptance: |all_setups| = 24 minimum (8 DXY + 8 EU + 8 GU). MORE is fine, LESS is REJECT.
```

---

---

## SOURCE ANCHORS

Every anchor below was verified by printing the referenced line (never fabricated).

- `Original_Canon_Data/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md:76` — the R3 Law
- `Original_Canon_Data/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md:152` — the zone pressure lifecycle VIRGIN→…→BROKEN
- `Original_Canon_Data/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md:177` — TS-1 sniper entry — the zone edge closest to price
- `Original_Canon_Data/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md:359` — the RRR floor IRON LAW
- `Original_Canon_Data/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md:999` — §8.14 the 16 zero-tolerance rules
