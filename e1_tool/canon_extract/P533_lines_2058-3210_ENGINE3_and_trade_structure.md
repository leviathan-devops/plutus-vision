## PART VI-B: ENGINE 3 — TRADE SETUP ARCHITECTURE

### 8.0 Engine 3 Purpose & Dependency

Engine 3 is the third prong of the Trident Trading Engine. It does NOT operate independently — it is built entirely on Engine 1 (IP zones + POI tiers) and Engine 2 (macro shape chains). Engine 1 answers "Where are the walls?" Engine 2 answers "What path will price take?" Engine 3 answers "Where exactly do I enter, where is my stop, and where is my target?"

Engine 3 transforms structural analysis into executable trade architecture.

**v5.0.0:** Engine 3 now operates on DXY AND on each translated pair (EUR/USD, GBP/USD, AUD/USD) via Part IX. Pair-specific trade setups use pair-specific entry/SL/TP levels from pair data, NOT converted DXY levels.


### 8.0.1 Phase 0: Setup Universe Classification (NEW)

Before building any individual setup, classify the WEEK into setup zones based on Engine 2 output:

**For each shape identified by Engine 2, generate the corresponding setup universe:**

| Engine 2 Shape | Setup Universe | Timeframe Stack | Expected Setup Count |
|:---|:---|:---|:---|
| BS (Breakout Surge) | HTF Swing + Reinforcements | Swing Stack | 1 swing + 2-3 reinforcements |
| WL (Whiplash) | HTF Swing | Swing Stack | 1 swing |
| SS (Sideways Squeeze) | Swing Scalps (both directions) | Scalp Stack | 4-8 swing scalps |
| SS(DWL) (Double Whiplash) | Swing Scalps + DWL Inverse | Scalp Stack | 4-8 swing scalps + 1-2 inverse |
| WLS (Whiplash Storm) | Swing Scalps + DWL Inverse | Scalp Stack | 4-8 swing scalps + 1-2 inverse |
| R (Recovery) | Swing Scalps + Recovery Surge | Both Stacks | 2-4 swing scalps |
| SS→BS Transition | Transition Entry | Both Stacks | 1 transition + reinforcements |

**Total expected setups per week**: 8-15+ (vs v5.1's 2-3).

### 8.0.2 Day-Level Bridge: Engine 2 → Engine 3 (v5.3.3 — CRITICAL)

**THE DAY BRIDGE IS THE MOST IMPORTANT INTEGRATION POINT IN THE ENTIRE SYSTEM.** Without it, Engine 3 produces trade setups without DAY labels — making the report USELESS for weekly execution planning. The trader cannot execute trades if they don't know which DAY a setup hits.

**Formal Bridge Specification:**

Engine 2's Day-Level Decomposition (Section 6.6 Step 5) produces a day-by-day shape prediction:
```
Mon: [SHAPE] [direction] | Key Zone: [name] | Triggers: [list] | Confidence: X%
Tue: [SHAPE] [direction] | Key Zone: [name] | Triggers: [list] | Confidence: X%
Wed: [SHAPE] [direction] | Key Zone: [name] | Triggers: [list] | Confidence: X%
Thu: [SHAPE] [direction] | Key Zone: [name] | Triggers: [list] | Confidence: X%
Fri: [SHAPE] [direction] | Key Zone: [name] | Triggers: [list] | Confidence: X%
```

Engine 3 MUST consume this decomposition and assign every setup to its corresponding day:

| Engine 2 Day Prediction | Engine 3 Setup Type | DAY Assignment | Session Window |
|:---|:---|:---|:---|
| Mon: SS (range) | Swing Scalps at ceiling + floor | Monday | London (primary scalp session) |
| Mon: SS → Tue: SS | Swing Scalps continue | Monday + Tuesday | London both days |
| Tue: SS (late phase, ZFP rising) | Breakout Search + Swing Scalps | Tuesday + Wednesday | Tuesday London (scalps), Wednesday NY (breakout) |
| Wed: BS (breakout) | HTF Swing + Reinforcements | Wednesday | Wednesday NY Mid (primary swing session) |
| Wed: BS → Thu: R | HTF Swing + Recovery reinforcements | Wednesday + Thursday | Wednesday NY (entry), Thursday London (reinforcement) |
| Thu: R → SS | Swing Scalps resume | Thursday | Thursday London |
| Fri: WL/SS→BS | Transition + HTF Swing | Friday | Friday NY (if breakout confirms) |
| Fri: R (end of week) | Close all positions | Friday | Close by NY session end |

**DAY ASSIGNMENT ALGORITHM:**
1. Read Engine 2 Step 5 output (day-by-day shape prediction)
2. For each day's predicted shape, look up the setup universe from Section 8.0.1
3. Assign the corresponding setup type to that day
4. Apply Trading Speed Rule: shift setups +1 day from initial prediction
5. Apply Session-Specific Rules: SS shapes → London session (scalp), BS/WL shapes → NY session (swing)
6. Cross-reference with economic calendar (Section 12) for day-specific catalysts
7. Assign SESSION WINDOW based on shape type + pair role:
   - SS shape → London session (GU/AU scalp focus)
   - BS/WL shape → NY session (EU/AU swing focus, 95% start 2nd half NY)
   - R shape → Both sessions possible (recovery is transitional)
   - SS→BS Transition → London setup, NY activation
8. Assign ANCHOR HIT WINDOW: when the entry's IP zone / liquidity zone is expected to be reached, based on the shape prediction timing

**MANDATORY OUTPUT**: The Weekly Execution Calendar (Section 8.5) MUST be populated from this bridge. Every row in the calendar maps directly from Engine 2's day-by-day prediction through this bridge into Engine 3's setup construction.

### 8.1 Market Structure + IP Interaction for Reversals

**Bullish reversal from bearish trend:**
1. Bearish trend produces higher lows in the downtrend
2. Price reaches a Tier 1 POI (IP zone overlapping 4H BoM demand) with WEAK IP resistance above and HIGH ZFP
3. The weak resistance zone BREAKS — this is the bullish Break of Structure (BoS)
4. The broken IP resistance zone FLIPS to support — this is the entry
5. SL = nearest liquidity zone beneath the flipped support
6. TP = fib wormhole level from correctly anchored spiderweb

**Bearish reversal from bullish trend (mirror):**
1. Bullish trend produces lower highs in the uptrend
2. Price reaches a Tier 1 POI (IP zone overlapping 4H BoM supply) with WEAK IP support below and HIGH ZFP
3. The weak support zone BREAKS — this is the bearish BoS
4. The broken IP support zone FLIPS to resistance — this is the entry
5. SL = nearest liquidity zone above the flipped resistance
6. TP = fib wormhole level

**CRITICAL:** The BoS + flip is the confirmation. Without it, the zone is just a level — not a trade.

### 8.2 Fibonacci Spiderweb Anchoring Rules

**Three anchoring contexts by trade type:**

| Context | Trade Type | Anchor Timeframe | Anchor Selection | Frequency |
|:---|:---|:---|:---|:---|
| **Context 1** | BS/WL Swing Moves | **1H** (NOT 4H) | Deepest + Most Recent swing high/low. Must be BoM anchors. | ~40% |
| **Context 2** | SS/Recovery Scalp Moves | 15m | Nearest NON-SURGE swing high/low inside 15m consolidation. | ~40% |
| **Context 3** | Mid-Swing Path Revelation | 30m | Nearest swing high/low FROM THE SAME TRADING DAY. | ~20% |

**GOOD ANCHOR:** Deepest swing, most recent, clear reversal, aligned with BoM S/D zone edges, NOT an intermediate HL/LH.
**BAD ANCHOR:** Intermediate HL/LH, no reversal, not deepest/recent, at surge point, subsequent structure instead of origin.

**Fib Wormhole Mechanics:** 0.382 retracement → 1.382 extension (TP); 0.618 retracement → 1.618 extension (TP). IP zones determine which level holds vs pierces.

**MANDATORY Buffers for Scalp Entries (Context 2):** Entry: 0.5-1 pip buffer; SL: 1 pip buffer; TP: 1.5-2 pip buffer in front of fib TP level.

### 8.3 Confluence Stack for Trade Setup Quality

| Layer | Criterion | Weight | Description |
|:---|:---|:---|:---|
| 1 | Strong IP zone | Required | Confluence score ≥ 6/14 |
| 2 | Overlapping 4H BoM S/D with low mitigation | Required | Tier 1 Confluent POI (0X-1X) |
| 3 | Macro-shape anchor aligns with POI | +2 | Engine 2 predicted path goes through this zone |
| 4 | Fib spiderweb shows clear entry→TP pathway | +2 | Correctly anchored fib reveals entry, wormhole reveals TP |
| 5 | IP/news data supports direction | +1 | Options data, analyst consensus, or volatility triggers align |
| 6 | RRR > 4x | Required | Risk/reward meets minimum threshold |
| 7 | No blind spots | Required | SL at verified liquidity zone, TP at verified reaction level |

**Quality Classification:** God-Tier (7/7), High (Layers 1-3 + 2 of 4-7), Standard (Layers 1-2 + 1 of 4-7), Supplementary (Layer 1 only + RRR > 3x)


**BoM/MoM Confluence Modifiers (NEW):**

| Zone Classification | Modifier | Rationale |
|:---|:---|:---|
| BoM zone | +2 | Strongest entry type — 100% reaction guarantee |
| MoM (tested + S/R aligned) | +0 | Neutral — conditional entry |
| MoM (virgin) | -3 | Death zone — likely to pierce |
| MoM (depleted, 3+ reactions) | -2 | Zone about to fail |

**Zone Reaction Modifiers (NEW):**

| Reaction Count | Modifier | Rationale |
|:---|:---|:---|
| 0 reactions (virgin BoM) | +1 | Untouched — full reaction expected |
| 1-2 reactions (active) | +0 | Zone is active — normal |
| 3+ reactions (depleted) | -2 | Zone about to fail — reduced confidence |

### 8.4 Trade Setup Construction Protocol

For each Tier 1 and Tier 2 POI identified by Engine 1, Engine 3 constructs trade setups as follows:

**Step 1: Direction Determination**
- Apply the 6-check Direction Validation Protocol (Section 7.2) — this is MANDATORY (v5.0.0: upgraded from 5-check to 6-check with Counter-Trend Check)
- If 4+ of 6 checks disagree with proposed direction, REVERSE the direction
- Market structure + IP direction takes precedence over candle-level analysis


**BoM/MoM ENFORCEMENT (CRITICAL — 90% WIN RATE RULE):**

For each zone candidate, apply the BoM/MoM classification from Engine 1:

| Zone Type | Entry Status | Rules |
|:---|:---|:---|
| **BoM** | **ENTRY-PRIMARY** | 100% guaranteed reaction if unmitigated. Highest priority entry. |
| **MoM (tested, S/R aligned)** | **ENTRY-CONDITIONAL** | Valid ONLY if: (a) ≥1 prior strong reaction, (b) trend-aligned, (c) key S/R confluence, (d) opposing liquidity weak or absent. |
| **MoM (virgin)** | **ENTRY-REJECT** | DEATH ZONE. Automatic reject. No exceptions. Virgin MoM zones are for TP targeting only. |
| **MoM (depleted, 3+ reactions)** | **ENTRY-REJECT** | Zone about to fail. Use as TP target for opposing direction. |
| **4H MoM** | **ENTRY-SCALP-ONLY** | One-and-done: minor reaction then pierce. Maximum scalp entry, no swing. |

**MoM → TP redirect**: All rejected MoM zones are automatically assigned as TP targets for the OPPOSING direction. When going LONG in a bearish correction, MoM supply zones are TP targets. When going SHORT in a bullish correction, MoM demand zones are TP targets.

**Step 2: Entry Identification (TS-1 — CRITICAL)**
- Entry = specific KEY LEVEL within the POI zone, NOT the zone edge (per Section 7.1 Rule 1)
- **LONG from SUPPORT/EQUILIBRIUM**: Enter at bounce level (2nd lowest key level near zone bottom)
- **SHORT from RESISTANCE/EQUILIBRIUM**: Enter at rejection level (2nd highest key level near zone top)
- If fib spiderweb is applicable, the nearest fib level TO the zone edge is the precise entry
- For Context 2 scalps: add 0.5-1 pip buffer in front of the fib level
- **v5.0.0:** Check Intra-Zone Key Levels from Step 0.6 for additional entry precision
- **Operator proof:** LONG from MRS at 98.02 (LSZ edge = 2nd lowest key level), NOT 98.00 (zone floor)

**Step 3: Stop Loss Placement (TS-2/TS-8 — CRITICAL)**
- SL anchored to nearest structural defense level beyond the zone (per Section 7.1 Rule 2)
- **SHORT SL**: Nearest big figure above entry + 2.5 pip buffer. Fallback: next zone boundary + 3 pips, then LSZ supply-side top + 3 pips.
- **LONG SL**: Key level of zone below entry - 1 pip. If too close (< 5 pips), next key level down. Fallback: LSZ demand-side bottom - 3 pips, then entry zone bottom - buffer.
- **Minimum SL distance**: 2.5 pips (Swing Stack), 1.5 pips (Scalp Stack)
- **If no SL anchor within 30 pips (0.30 DXY)**: REJECT the setup
- **Correction entry exception**: SL 1-2 pips INSIDE the next zone (not outside) for counter-trend entries
- **Liquidity Shield SL**: SL must be anchored to a key level that IS a liquidity pressure zone (a "shield"). Unshielded SLs are vulnerable. GU: liquidity zone in front of S/D can serve as shield. EU: PA often touches directly, no shield.
- For Context 2 scalps: add 1 pip buffer from the exact fib level
- **v5.0.0:** Consider LSZ Bottom Edge Extension (Step 0.45a) for wider sweep ranges

**Step 4: Take Profit Identification — REGIME-CONDITIONAL TP LOGIC (v5.0.0 — P4 POSTMORTEM FIX):**

The default TP logic depends on the macro shape regime:

| Regime | Default TP Method | Rationale |
|:---|:---|:---|
| **Swing Scalps (SS)** | Nearest opposing zone edge OR nearest LSZ edge | In SS, price oscillates between zones. Fib wormhole targets are too ambitious for SS — they project beyond the range. Use the nearest opposing zone/LSZ edge as the realistic TP. |
| **Breakout Surge (BS)** | Fib wormhole (0.618→1.618 or 0.382→1.382) | In BS, the directional move has structural backing. Fib wormhole targets are appropriate because price is moving directionally. |
| **Recovery (R)** | Nearest IP zone in recovery direction | Recovery is transitional — take profit at the next zone. |
| **Whiplash (WL/RWL)** | Fib wormhole if anchored to rejection point | After a whiplash rejection, the move is directional. Fib wormhole from the rejection anchor is valid. |

**Override:** If the fib wormhole TP aligns with a verified IP zone or reaction level, it takes priority regardless of regime. The regime-conditional logic applies ONLY when the fib TP is unanchored (no zone or reaction level at the fib target).

**Fallback:** Prior swing high/low, Structural Extreme Magnet, or Measured Move target — in that priority order.


**Liquidity Shield SL Rule (NEW — v5.2.0):**
- SL must be anchored to a key level that IS a liquidity pressure zone (a "shield").
- Unshielded SLs (no liquidity density at the SL anchor) are vulnerable to being pierced.
- GU-specific: the liquidity zone in FRONT of a S/D zone can serve as SL shield anchor.
- EU-specific: PA often directly touches the overlap point — no shield, direct zone test.

**Sequential Zone Path Mapping (NEW — v5.2.0):**
- Map ALL unmitigated liquidity zones between entry and TP as intermediate targets.
- Each intermediate zone = either a reinforcement entry point (Part VII-C) or a minor TP.
- Price ALWAYS sweeps liquidity zone by zone in sequential order — it NEVER skips a zone.
- This replaces the "entry→TP teleport" model with a realistic path.

**Timeframe Element Matching for TP (NEW — v5.2.0):**
- Breakout source TF → target same TF element (see Engine 2 Timeframe Element Matching).
- 4H source → 4H target (1H acceptable substitute).
- 15m source → 30m or 1H target (up to 2 TF dimensions, not more).
- 1H/4H can be used interchangeably with 4H being the dominant pressure zone.

**Minimum RRR by Setup Type (UPDATED — v5.2.0):**
- HTF Swing setups: 4x (high-confluence), 5x (standard)
- Swing Scalp setups: 3.0:1 minimum
- Reinforcement entries: 2.0:1 minimum (compensated by position sizing)
- Supplementary with flow continuity: 3x

**Step 5: RRR Calculation**
- RRR = (TP - Entry) / (Entry - SL) for longs; RRR = (Entry - TP) / (SL - Entry) for shorts
- Minimum: 4x (high-confluence setups), 5x (standard)
- Target: 5x+ for standard setups, 8-10x for god-tier

**Step 6: Confluence Scoring + Confidence Calculation**
- Apply the confluence stack (Section 8.3) and classify the setup quality
- Apply BoM/MoM Confluence Modifiers and Zone Reaction Modifiers (Section 8.3)
- Report the setup quality classification in the output

**Confidence Score Formula (0–100 scale — MANDATORY):**

| Component | Max Points | Calculation |
|:---|:---|:---|
| Base | 40 | (Confluence / 12) × 40 — denominator is max achievable without P7 |
| Option bonus | 20 | (Max notional at zone / 3.5B) × 20 |
| Shape alignment | 20 | 20 if aligned with Engine 2 shape, 0 if conflict |
| Red Folder clearance | 10 | 10 if clear of Red Folder events, 0 if within 30 min of one |
| ZFP bonus | 10 | (1 - ZFP%) × 10 (lower ZFP = stronger zone = higher score) |
| BoM/MoM bonus/penalty | ±10 | BoM zone entry: +5. MoM zone entry: -10 (unless all 4 exceptions met). 3+ retests: +5. |
| **Total** | **100 (max)** | **Minimum 65 to include in report** |

**Quality Classification:**
- God-Tier: 85+ (highest conviction, full position size)
- High: 75–84 (strong conviction, standard position size)
- Standard: 65–74 (moderate conviction, reduced position size)
- Below 65: EXCLUDED ("No qualifying setups")

**RRR Minimum by Quality:**
- God-Tier: 4x minimum
- High: 4.5x minimum
- Standard: 5x minimum
- Counter-trend in directional regimes: 2.5x minimum applies ONLY to BS/WL directional setups, NOT to SS (both directions are valid in SS per TS-6)

**Step 7: DAY Assignment via Day-Level Bridge (v5.3.3 — MANDATORY)**
- Using the Day-Level Bridge (Section 8.0.2), assign the DAY, SESSION WINDOW, SHAPE TRIGGER, SETUP CATEGORY, and ANCHOR HIT WINDOW for this setup
- Read Engine 2's Day-by-Day Decomposition (Section 6.6 Step 5) to determine which day this setup's shape is predicted
- Apply Trading Speed Rule (Section 6.10): shift +1 day from raw prediction
- Apply Session-Specific Rules: SS shapes → London session, BS/WL shapes → NY session
- Cross-reference economic calendar (Section 12) for day-specific catalysts
- If the setup spans multiple days, assign the MOST LIKELY day with alternative (e.g., "Monday (alt: Tuesday)")
- **A setup WITHOUT a DAY assignment is INCOMPLETE and CANNOT be included in the report (Rule 13)**


### 8.4.2 Phase 2.5: Entry Timing Protocol (NEW — 1-2-3 Retest)

**This is the timing mechanism that prevents premature entries.**

For each zone candidate that passed Phase 1 and Phase 2, assess the retest status:

| Retest Count | Entry Validity | Setup Type | Notes |
|:---|:---|:---|:---|
| 0 (Virgin) | NO ENTRY unless BoM | — | Virgin MoM = DEATH ZONE. Virgin BoM = 100% reaction — valid but tight SL. |
| 1 (1st retest) | SCALP ONLY (if BoM) | Scalp only | Do not enter for swing. Minor reaction likely. Wait for confirmation. |
| 2 (2nd retest) | SCALP CONFIRMATION | Scalp | Zone has confirmed it can hold. Tight but valid entry. |
| 3+ (3rd retest) | SWING ENTRY VALID | Swing | Zone has proven itself through multiple tests. Full move expected. |

**"Wait for the bounce" rule**: Never predict the entry — let price action confirm it. When price approaches a zone, WAIT for it to react (bounce or reject) before entering. The reaction confirms the zone is active.

**Reinforcement timing**: Reinforcement entries are ONLY valid AFTER the 1-2-3 pattern is complete and the full move has started. Reinforcing before the 3 is confirmed is early and will likely get stopped out.

### 8.4.1 MULTI-SETUP ARCHITECTURE (v5.0.0 — P2 POSTMORTEM FIX — CRITICAL)

**The Apr 20-24 report produced only ONE primary trade setup, missing multiple valid setups at other zones.** This is a critical failure because the user needs to see ALL valid trade opportunities across ALL zones, not just the single highest-scoring one.

**New Protocol (MANDATORY):**

1. **Generate ALL valid setups** across ALL zones with Pressure Degree MODERATE or above.
2. **Classify each setup** by quality (God-Tier/High/Standard/Supplementary).
3. **Present ALL God-Tier and High setups as PRIMARY setups** — the user chooses which to execute.
4. **Present Standard setups as SECONDARY** — valid but lower conviction.
5. **Present Supplementary setups as TERTIARY** — informational only.
6. **Build a Trade Setup Matrix** showing all setups side by side:

```
TRADE SETUP MATRIX (v5.3.3 — INCLUDES DAY + SESSION):
───────────────────────────────────────────────────────────────
# | Zone | Dir | Quality | Day | Session | Entry | SL | TP | RRR | Shape | Conf
1 | Zone #3 | SHORT | God-Tier | Wed | NY Mid | [level] | [level] | [level] | 8.2x | BS | 7/7
2 | Zone #5 | LONG | High | Mon | London | [level] | [level] | [level] | 5.6x | SS | 5/7
3 | Zone #7 | SHORT | Standard | Tue | London | [level] | [level] | [level] | 4.3x | SS | 4/7
4 | Zone #9 | LONG | Standard | Thu | NY | [level] | [level] | [level] | 4.1x | R | 4/7
───────────────────────────────────────────────────────────────
Primary Setups: #1, #2 | Secondary: #3, #4 | Tertiary: none
```

7. **Build Trade Flow Chains** for each PRIMARY setup, showing the sequence of trades if that setup is executed first.
8. **Identify Setup Conflicts** — if two primary setups have opposing directions, flag them as conflicting and explain which macro shape chain branch would activate each.

### 8.5 Engine 3 Output Format (Report Section 18)

**v5.2.0 FULL-SPECTRUM OUTPUT — replaces "Max 3 setups" with complete trade universe:**

**Maximum setups per category:**
- HTF Swing Setups: Max 3 (sorted by confidence descending)
- Swing Scalp Setups: Max 3 per consolidation range (sorted by confidence)
- Reinforcement Entries: Max 3 per confirmed HTF swing
- Transition Setups: Max 2
- **Total across all categories: Max 15 setups**
- **Confidence threshold: 65+ to include** in any category
- **If zero setups qualify in a category:** State "No qualifying [category] setups this week — [reason]"
- **Deduplication:** By (direction, entry at 2-decimal precision) across ALL categories

The Engine 3 output is now organized into FIVE categories, preceded by the WEEKLY EXECUTION CALENDAR:

```
═══════════════════════════════════════════════════════════════
ENGINE 3 — FULL-SPECTRUM TRADE MAP | WEEK OF [DATE]
═══════════════════════════════════════════════════════════════

═══ WEEKLY EXECUTION CALENDAR (v5.3.3 — MANDATORY) ═══
Day       | Pair    | Dir  | Setup Type     | Entry   | Shape   | Session | Conf | Notes
──────────|─────────|──────|────────────────|─────────|─────────|─────────|──────|──────
Monday    | GU      | SHORT| Swing Scalp    | 1.3320  | SS      | London  | 82   | Range ceiling test
Monday    | EU      | LONG | Swing Scalp    | 1.0840  | SS      | London  | 78   | Floor demand bounce
Tuesday   | GU      | SHORT| Swing Scalp    | 1.3310  | SS      | London  | 75   | 2nd ceiling retest
Tuesday   | AU      | LONG | Swing Scalp    | 0.6420  | SS      | NY      | 80   | Floor demand 2nd test
Wednesday | GU      | SHORT| Breakout Search| 1.3280  | BS      | NY Mid  | 88   | Ceiling ZFP>45% failing
Wednesday | GU      | SHORT| Reinforcement 1| 1.3310  | BS cont.| NY      | 82   | LR at ceiling zone
Wednesday | EU      | LONG | HTF Swing      | 1.0820  | BS      | NY Mid  | 90   | BoM demand + IP overlap
Thursday  | EU      | LONG | Reinforcement 1| 1.0840  | R       | London  | 78   | LR at mid-zone
Thursday  | AU      | LONG | HTF Swing      | 0.6390  | WL      | NY      | 85   | Whiplash at ceiling
Friday    | EU      | SHORT| Transition     | 1.0880  | SS→BS   | NY      | 72   | SS→BS if ceiling breaks
──────────|─────────|──────|────────────────|─────────|─────────|─────────|──────|──────
Total: 10 setups across 5 days | HTF Swings: 2 | Swing Scalps: 4 | Reinforcements: 2 | Transition: 1 | Breakout Search: 1
═══════════════════════════════════════════════════════════════

─── HTF SWING SETUPS (Swing Stack: 4H/1H/30m) ───
[1-N swing setups per Engine 3 Phase 0-6, WITH DAY LABELS]

─── SWING SCALP SETUPS (Scalp Stack: 30m/15m/5m) ───
[4-8 swing scalp setups per Part VII-B, per consolidation zone, WITH DAY LABELS]

─── REINFORCEMENT ENTRIES ───
[2-3 reinforcement entries per confirmed HTF swing, per Part VII-C, WITH DAY + PARENT TRADE REFERENCE]

**Reinforcement Entry Format (v5.3.3 — MANDATORY):**
```
REINFORCEMENT ENTRY: R-[#] [Direction] [Rocket Type: LR/FR/FLR]
DAY: [Monday/Tuesday/Wednesday/Thursday/Friday] ← v5.3.3 MANDATORY — inherited from parent trade
SESSION WINDOW: [London / NY] ← v5.3.3 MANDATORY
SHAPE TRIGGER: [BS continuation / R / WL] ← v5.3.3 MANDATORY
SETUP CATEGORY: Reinforcement ← v5.3.3 MANDATORY
PARENT TRADE: [#] [parent trade setup ID] ← v5.3.3 MANDATORY — reference to the primary HTF swing
Trigger Zone: [zone name] | Trigger Price: [exact level] (1-2 pips inside close/far edge)
Entry Zone: [zone name] | Entry Price: [exact level] (limit order at thick liquidity zone)
Stop Loss Zone: [zone name] | SL Price: [exact level] (1-2 pips outside back edge)
Buffer Zones: [1 zone for LR / 2 zones for FR] | Zone Thickness: [thick/thin]
Rocket Type: LR=Water Precision / FR=Fire Precision / FLR=Earth Heavy
Fib Level Alignment: [if FR/FLR — which Fib level triggers this rocket]
Combined RRR with Parent: [X]x (calculated across primary + all reinforcements)
Audit Trail: [trigger calculation, entry calculation, SL calculation]
```

─── TRANSITION SETUPS ───
[SS→BS transition entries, post-whiplash reverse entries, WITH DAY LABELS]

**Transition Entry Format (v5.3.3 — MANDATORY):**
```
TRANSITION SETUP: T-[#] [Direction] [Transition Type: SS→BS / Post-WL Reverse / DWL-Inverse]
DAY: [Monday/Tuesday/Wednesday/Thursday/Friday] ← v5.3.3 MANDATORY
SESSION WINDOW: [London / NY] ← v5.3.3 MANDATORY
SHAPE TRIGGER: [SS→BS / WL→RWL / DWL-Inverse] ← v5.3.3 MANDATORY
SETUP CATEGORY: Transition ← v5.3.3 MANDATORY
ANCHOR HIT WINDOW: [when the transition trigger is expected] ← v5.3.3 MANDATORY
Preceding Shape: [the shape that must complete before this transition activates]
Entry Condition: [what confirms the transition — e.g., "break of 30m lower high", "whiplash rejection candle"]
Entry: [exact level] ([zone edge / fib level])
SL: [exact level] ([anchor: zone edge + buffer])
TP: [exact level] ([target: next opposing zone])
RRR: [X]x
Confidence: [score]/100
Day Catalysts: [expiries / events on this day] ← v5.3.3 MANDATORY
```

─── DAILY SESSION NOTES ───
Monday: [X] scalp setups | London focus: GU/AU | NY focus: EU/AU
Tuesday: [X] scalp setups | London focus: GU/AU | NY focus: EU
Wednesday: [X] swing + breakout setups | NY = primary execution day
Thursday: [X] reinforcement + recovery setups | NY = swing execution
Friday: [X] transition setups | Close all positions by NY close
═══════════════════════════════════════════════════════════════
```

**Individual Setup Format (UPDATED — v5.3.3 — MANDATORY DAY + SESSION + SHAPE LABELS):**

**v5.3.3 CRITICAL CHANGE**: Every trade setup MUST include DAY, SESSION WINDOW, SHAPE TRIGGER, and SETUP CATEGORY. A report without these fields is INCOMPLETE and CANNOT be blindly executed. The trader must know WHEN a trade hits (day + session), not just WHERE it hits (entry level). Without DAY labels, the trader cannot plan the week. This is the single most important formatting change in v5.3.3.

Direction Validation now shows 6 checks (added Counter-Trend Check).
Trade Setup Matrix added at the end of Section 18.
Intra-Zone Key Level referenced in entry identification where applicable.
BoM/MoM classification and Zone Reaction Count now shown per setup.

```
TRADE SETUP: [#] [Direction] [Quality]
DAY: [Monday/Tuesday/Wednesday/Thursday/Friday] ← v5.3.3 MANDATORY
SESSION WINDOW: [London Open / London Mid / NY Overlap / NY Open / NY Mid / NY Close] ← v5.3.3 MANDATORY
SHAPE TRIGGER: [BS/WL/R/SS/WLS/PBS/RWL/SS→BS Transition] ← v5.3.3 MANDATORY — which macro shape activates this setup
SETUP CATEGORY: [HTF Swing / Swing Scalp / Breakout Search / Reinforcement / Transition] ← v5.3.3 MANDATORY
ANCHOR HIT WINDOW: [when the entry anchor point is expected to be reached — e.g., "London Open when GU tests 1.3320 ceiling"] ← v5.3.3 MANDATORY
POI: [Zone Name] | POI Tier: [1/2/3] | Range: [DXY range]
Direction Validation: [X]/6 checks agree → [Long/Short]
  Check 1 (4H Trend): [result]
  Check 2 (BoM Alignment): [result]
  Check 3 (Liquidity Sweep): [result]
  Check 4 (Zone Failure): [result]
  Check 5 (Macro Shape): [result]
  Check 6 (Counter-Trend): [result]
Entry: [exact DXY level] ([zone edge / fib 0.618 / intra-zone key level / etc.])
Stop Loss: [exact DXY level] ([liquidity zone name] + [X] pip buffer)
Take Profit: [exact DXY level] ([regime-conditional: nearest opposing zone / fib wormhole / etc.])
RRR: [X]x
Fib Spiderweb: [Context 1/2/3] | Anchor: [1H/15m/30m] | Anchor Type: [type]
Confluence Stack: Layer 1=[Y/N] ... Layer 7=[Y/N] | Score: [X]/7
Trade Flow: This setup → [next setup name] (on [DAY]) ← v5.3.3: include day of next setup
Day Catalysts: [expiries / economic events / auctions hitting this day] ← v5.3.3 MANDATORY
Audit Trail: [entry calculation, SL calculation, TP calculation with inputs]
```

**DAY ASSIGNMENT RULES (v5.3.3 — CRITICAL):**
1. Every setup inherits its DAY from Engine 2's Day-Level Decomposition (Section 6.6 Step 5)
2. If Engine 2 predicts Mon=SS, Tue=SS, Wed=BS → swing scalps on Mon/Tue, breakout search on Wed
3. Apply Trading Speed Rule (Section 6.10): add +1 day to expected timing. "Today's move" = tomorrow's move.
4. Reinforcement entries inherit the DAY of their parent trade + 1 day buffer for activation
5. If a setup spans multiple days (e.g., SS range persists 2-3 days), assign the MOST LIKELY day with alternative: "Day: Monday (alt: Tuesday if SS persists)"
6. Transition setups are assigned to the day AFTER the preceding shape completes: SS→BS on Wednesday means the BS happens Wednesday, the transition entry is late Tuesday / early Wednesday
7. NEVER leave a setup without a DAY. A setup without a DAY is an INCOMPLETE setup that CANNOT be executed.

### 8.6 Engine 3 Zero-Tolerance Rules

**RULE 1:** No trade without Tier 1 or Tier 2 POI. A trade setup requires at minimum a Tier 2 POI (IP zone with confluence ≥ 6). Tier 3 POIs are supplementary only — never the basis for a standalone trade.

**RULE 2:** Direction validation is MANDATORY. Every trade setup must pass the 6-Check Direction Validation Protocol (Section 7.2). If 4+ of 6 checks disagree with the proposed direction, the direction MUST be reversed. No exceptions.

**RULE 3:** Fib anchoring must follow rules. Every fib spiderweb must be anchored per Section 8.2 rules. Context 1 uses 1H anchors for BS/WL swings. Context 2 uses 15m anchors for scalp moves. Context 3 uses 30m anchors for same-day moves. BAD anchors (intermediate HL/LH, surge points, non-origin swings) are FORBIDDEN.

**RULE 4:** Temporal Boundary Inheritance. All IP zone data, analyst levels, and option expiry data must be pre-week data. In-week data is FORBIDDEN. The Data As-Of timestamp must be included and verified.

**RULE 5:** Post-pierce consolidation awareness. After 2 strong piercing swing moves, expect 1-2 full days of HTF consolidation. Do not construct whiplash storm setups immediately after strong piercing moves. Default to swing scalp setups during post-pierce consolidation.

**v5.2.0 ADDITIONAL ZERO-TOLERANCE RULES:**

**RULE 6: BoM/MoM ENFORCEMENT.** No entry at MoM zones unless ALL 4 exceptions are met. Virgin MoM = automatic reject. 4H MoM = scalp only. This rule is NOT optional — it is the single highest-impact rule for win rate.

**RULE 7: 1-2-3 RETEST TIMING.** No swing entry before 3rd retest. No scalp entry before 2nd retest. Virgin zones = no entry unless BoM. "Wait for the bounce" — never predict, always confirm.

**RULE 8: SEQUENTIAL ZONE PATH.** Every trade setup MUST map the sequential zone path between entry and TP. No "entry→TP teleport" — map every intermediate zone.

**RULE 9: TIMEFRAME STACK COMPLIANCE.** Every setup MUST declare its Timeframe Stack (Swing or Scalp). Swing Stack setups use 4H/1H/30m. Scalp Stack setups use 30m/15m/5m. Never mix stacks within a single setup. 5m is for refinement ONLY — never the trading timeframe.

**RULE 10: 30-MINUTE RED FOLDER DEFERRAL.** No trade entry within 30 minutes of a Red Folder economic event (high-impact designation on the economic calendar). If a qualifying setup's entry window overlaps with a Red Folder event, the setup is DEFERRED until 30 minutes after the event. Mark the trade status as `DEFERRED until [time]` in the output. Red Folder events include: FOMC rate decisions, NFP, CPI, GDP (advance), PMI (manufacturing/services flash). Do NOT have limit orders open right before news — you do NOT know what price will do. Open positions with SLs in profit are acceptable.

**RULE 11: MAXIMUM 3 SETUPS PER CATEGORY.** No more than 3 HTF swing setups, 3 swing scalps per consolidation range, 3 reinforcements per swing, 2 transitions. Total max 15 setups across all categories. Confidence ≥ 65 required. If zero qualify: explicitly state "No qualifying setups."

**RULE 12: MoM ZONES ARE LADDER STEPS ONLY (v5.3.0 — CRITICAL).** From Trading Laws: "Do not take reversal entries on MoM zones. EVER. Guaranteed loss. MoM zones are ONLY to be used as LADDER STEPS for trend-aligned trades that surf existing momentum. This is the ONLY use case." This supersedes the previous Rule 6 MoM 4-exception conditional entry for REVERSAL entries. Specifically:
- MoM zones are FORBIDDEN as primary entry points for REVERSAL trades (direction change)
- MoM zones in the PATH of a confirmed trend-aligned move are VALID as reinforcement ladder steps (Section 8R.1)
- MoM zones remain VALID as TP targets for opposing direction trades
- MoM zones remain CONDITIONAL for trend-aligned entries when ALL 4 exceptions are met (prior strong reaction + trend alignment + S/R confluence + weak opposing liquidity)
- The ONLY unconditional use case for MoM zones: ladder step reinforcements in confirmed moves

**RULE 13: MANDATORY DAY + SESSION + SHAPE LABELS (v5.3.3 — CRITICAL).** Every trade setup — HTF swing, swing scalp, reinforcement, and transition — MUST include: (a) DAY of the week (Mon/Tue/Wed/Thu/Fri), (b) SESSION WINDOW, (c) SHAPE TRIGGER, (d) SETUP CATEGORY, (e) ANCHOR HIT WINDOW. A setup without a DAY label is INCOMPLETE and CANNOT be included in the report. This is enforced by the Report Blind-Execution Protocol (Section 5.5, checks BE1-BE4). No exceptions.

**RULE 14: WEEKLY EXECUTION CALENDAR MANDATORY (v5.3.3 — CRITICAL).** Section 18 of the report MUST begin with a Weekly Execution Calendar showing ALL setups organized by day. The calendar MUST cover all 5 trading days. If no setups qualify for a day, explicitly state the reason (e.g., "No qualifying setups — Red Folder deferral"). This is enforced by Section 5.5 checks BE5 and BE10.

### 8.7 Engine Integration: How Engines 1+2 Feed Engine 3

| Engine 1 Output | Engine 3 Usage | Integration Point |
|:---|:---|:---|
| IP Zone Map (all zones with pressure degree, ZFP, confluence) | Phase 1: Zone Selection — ALL qualifying zones (confluence ≥ 7) generate trade candidates | Section 8.4 Step 1 |
| Intra-Zone Key Levels (Step 0.6) | Phase 2: Entry Identification — bounce level / rejection level from key levels | Section 8.4 Step 2 |
| LSZ Zones (with bottom edge extension) | Phase 4: SL/TP Anchoring — SL at LSZ boundary, TP at opposing LSZ edge | Section 8.4 Steps 3-4 |
| Three-Tier Option Classification | Phase 3: Confluence Scoring — Option bonus for Critical Option Walls | Section 8.4 Step 6 |
| Zone Reaction Counter | Phase 2.5: Entry Timing — 0=virgin, 1-2=active, 3+=depleted | Section 8.4.2 |
| BoM/MoM Classification | Phase 1: Zone Selection — BoM=entry, MoM=TP target, virgin MoM=reject | Section 8.4 Step 1 |
| Hard Wall Detection (ZFP<15%, confluence≥8) | Direction Validation: Check 6 Counter-Trend | Section 7.2 Check 6 |

| Engine 2 Output | Engine 3 Usage | Integration Point |
|:---|:---|:---|
| Primary Shape Chain | Phase 2: Shape Alignment — which setup types are valid | Section 8.4 Step 1 |
| ZFP-Conditioned Transition Rules | Phase 4: TP Targeting — regime-conditional TP logic | Section 8.4 Step 4 |
| Consolidation Phase Detection | Phase 0: Setup Universe Classification — SS/WLS/R → Swing Scalps | Section 8.0.1 |
| 4H MoM One-and-Done | Phase 1: Zone Selection — 4H MoM = scalp only | Section 8.4 Step 1 |
| Timeframe Element Matching | Phase 4: TP Targeting — source TF → target TF matching | Section 8.4 Step 4 |
| Forward Mapping (day-by-day) | Phase 0.2: Day-Level Bridge — DAY assignment for all setups | Section 8.0.2 (v5.3.3) |
| Forward Mapping (day-by-day) | Output: Session notes + DAY labels for each setup | Section 8.5 |
| Forward Mapping (day-by-day) | Weekly Execution Calendar population | Section 8.5 (v5.3.3) |
| Alternative Chain | Output: Setup Conflicts — opposing direction setups | Section 8.4.1 |

---

## PART VII: TRADE STRUCTURE PROTOCOL

This part governs how IP zones and macro shapes translate into tradeable setups. It is the translation layer between zone identification and executable trade construction. Every trade setup in the report MUST comply with these rules.

### 7.1 Entry Precision Rules

**RULE 1 (TS-1): ENTRY AT SPECIFIC KEY LEVEL, NOT ZONE EDGE.**

Entries are placed at a specific key level within the zone — NEVER at the raw zone edge alone. The zone edge is the boundary; the key level is where price actually reacts.

- **LONG from SUPPORT or EQUILIBRIUM**: Enter at the **bounce level** (2nd lowest key level near zone bottom). The absolute lowest key level is the zone floor (too deep — if price is at the floor, the zone is failing). The bounce happens at the LSZ/structural reaction level just above the floor.
- **SHORT from RESISTANCE or EQUILIBRIUM**: Enter at the **rejection level** (2nd highest key level near zone top). The absolute highest key level is the zone ceiling. The rejection happens at the level just below the ceiling.

**Operator proof:** LONG from MRS entered at 98.02 (LSZ edge = 2nd lowest key level), NOT 98.00 (zone floor). SHORT from EQ entered at 98.44 (option strike = 2nd highest key level), NOT 98.41 (zone top). This 2-pip precision difference is the difference between a winning and losing entry.

**Key level sources (from Intra-Zone Key Level Scan, Step 0.6):**
1. Pivot levels inside the zone
2. Option strike equivalents inside the zone
3. Swing highs/lows inside the zone
4. Fib retracement levels (0.382, 0.618) of the zone's own range
5. Prior daily closes within the zone
6. Round number levels (.00, .25, .50, .75) within the zone
7. Zone midpoint

**If fib spiderweb is applicable:** The nearest fib level TO the zone edge is the precise entry. For Context 2 scalps: add 0.5-1 pip buffer in front of the fib level.

**RULE 2 (TS-2): SL ANCHORED TO NEXT STRUCTURAL DEFENSE LEVEL BEYOND THE ZONE.**

The SL is placed at the nearest structural defense level beyond the zone — NOT at an arbitrary buffer distance from the entry.

- **SHORT SL**: Nearest big figure (round number) above entry + 2.5 pip buffer. Fallback: next zone boundary + 3 pips, then LSZ supply-side top + 3 pips.
- **LONG SL**: Key level of zone below entry - 1 pip. If key level is too close (< 5 pips), use the next one down. Fallback: LSZ demand-side bottom - 3 pips, then entry zone's own bottom boundary - buffer (for EQUILIBRIUM zones where the zone below is distant).
- **Minimum SL distance**: 2.5 pips for swing entries (Swing Stack). 1.5 pips for scalp entries (Scalp Stack, 5m precision).
- **Maximum SL distance**: If no SL anchor within 30 pips (0.30 DXY), REJECT the setup.

**Operator proof:** SHORT SL = 98.525 (big figure 98.50 + 2.5 pips). LONG SL from MRS = 97.87 - 0.01 = 97.86 (key level 97.87 of zone below - 1 pip). LONG SL from EQ = 98.185 (EQ zone bottom 98.29 - buffer, since zone below is distant).

**Correction/Reversal Entry Exception (CRITICAL):** When entering for a CORRECTION or REVERSAL trade (counter-trend), place SL 1-2 pips INSIDE the next zone beyond the entry. This is because price is likely to briefly pierce the entry zone before reversing. Standard SL rules (outside the zone) apply for trend-following entries only.

**RULE 2.5: LIQUIDITY SWEEP ZONE SL PLACEMENT.** For LSZ-anchored stop losses:
- Place SL at the LSZ boundary + 3 pip buffer (standard)
- If the LSZ has been extended per LSZ Bottom Edge Extension (sweep scan 0.05-0.10 DXY below swing highs), use the extended range for SL placement
- The LSZ boundary is the structural defense — price sweeping through the LSZ signals zone failure
- Minimum SL distance: 2.5 pips from LSZ edge

**RULE 3 (TS-3/TS-9): TAKE PROFIT AT MAJOR OPPOSING ZONE / LSZ EDGE — REGIME-CONDITIONAL.**

The TP target depends on the macro shape regime (this was the #1 cause of the F-grade trade setups in v5.0 — using Fib wormhole as primary TP in SS regime):

| Regime | Default TP Method | Rationale |
|:---|:---|:---|
| **SS (Swing Scalps)** | Nearest MAJOR opposing zone edge OR nearest LSZ edge | In SS, price oscillates between zones. Fib wormhole targets project beyond the range — use zone/LSZ edge instead. |
| **BS (Breakout Surge)** | Fib wormhole (0.618→1.618 or 0.382→1.382) | In BS, the directional move has structural backing. Fib wormhole is appropriate. |
| **WL/RWL (Whiplash)** | Fib wormhole if anchored to rejection point | After whiplash rejection, the move is directional. Fib wormhole from rejection anchor is valid. |
| **R (Recovery)** | Nearest IP zone in recovery direction | Recovery is transitional — TP at next zone. |

**SS-specific rules:**
- LONG targets RESISTANCE (skip EQUILIBRIUM zones — they're mid-range, not targets)
- SHORT targets SUPPORT (skip EQUILIBRIUM zones)
- LSZ precision: If LSZ edge inside the opposing zone is closer than zone boundary, use LSZ edge
- **NEVER use Fib wormhole as primary TP in SS regime** — it is ONLY acceptable as extended target AFTER primary zone-edge TP is hit

**TP2:** Second opposing zone boundary if within 80 pips (0.80 DXY).

**Operator proof:** SHORT TP = 98.02 (LSZ demand 97.97-98.02 top edge, inside opposing SUPPORT zone). LONG TP = 98.77 (Upper IP Resistance bottom edge).

**Override:** If the fib wormhole TP aligns with a verified IP zone or reaction level, it takes priority regardless of regime. The regime-conditional logic applies ONLY when the fib TP is unanchored (no zone or reaction level at the fib target).

### 7.2 Trade Direction Validation Protocol (v5.0.0 — UPGRADED TO 6-CHECK)

The Apr 27–May 1 report got the trade direction WRONG — the actual move was a downside breakout surge, not an upside move. The v4.5.2 5-check protocol caught trend/BoM/LSZ/zone failure/macro shape, but missed the **Counter-Trend Check** that explicitly tests whether the proposed direction is fighting a hard wall.

**DIRECTION VALIDATION CHECKLIST (mandatory for EVERY trade setup — NOW 6 CHECKS):**

**Check 1: 4H Trend Direction.** Determine the 4H trend: higher highs + higher lows = bullish (favors LONG), lower highs + lower lows = bearish (favors SHORT). The 4H trend is the structural truth — it takes days/weeks to complete, not hours.

**Check 2: BoM Zone Alignment.** Is the nearest BoM zone above (favors SHORT) or below (favors LONG) current price? BoM zones have 100% guaranteed reaction — the direction to the nearest BoM is the direction of the next move.

**Check 3: Liquidity Sweep Zone Direction.** The nearest LSZ determines the initial sweep direction. LSZ below = price sweeps down first (favors LONG entry after sweep). LSZ above = price sweeps up first (favors SHORT entry after sweep).

**Check 4: Zone Failure Cascade Direction.** Which zones are failing (ZFP trending up, approaching 45%+)? Failing support = bearish cascade (favors SHORT). Failing resistance = bullish cascade (favors LONG).

**Check 5: Macro Shape Chain Direction.** What direction does the Engine 2 shape chain predict? The chain maps the path — if it predicts BS down, the directional bias is SHORT.

**Check 6: Counter-Trend Hard Wall Check (v5.0.0 — P1 POSTMORTEM FIX — CRITICAL):**

This check prevents the most expensive direction error: proposing a directional trade when a Hard Wall exists in that direction. The Apr 20-24 report proposed an upside breakout when a Hard Wall (EXTREME pressure, ZFP < 10%) sat directly above — price could NOT go up.

- **Identify the nearest Hard Wall or Institutional Magnet in the proposed trade direction.**
- **If a Hard Wall (EXTREME/HEAVY pressure, ZFP < 15%) exists within 0.30 DXY points in the proposed direction:** The proposed direction is COUNTER-TREND to the hard wall. The trade is NOT invalid, but it REQUIRES:
  - A specific mechanism for how the hard wall will fail (e.g., "option expiry removes the cage at 10:01 AM Tuesday, allowing BS through the wall")
  - A reduced position size (half of normal)
  - A tighter SL (just beyond the hard wall, not the standard LSZ distance)
  - An explicit risk statement: "COUNTER-TREND: Hard Wall at [level] with [X]/14 pressure opposes this trade. Mechanism for wall failure: [specific reason]. Position size reduced by 50%."

- **If NO Hard Wall exists within 0.30 DXY points in the proposed direction:** Check 6 is NEUTRAL — no counter-trend concern.

**DIRECTION VALIDATION OUTPUT (mandatory for every trade setup):**
```
Trade Direction Validation:
  4H Trend: [Bullish/Bearish/Ranging] → Favors: [Long/Short/Neutral]
  BoM Alignment: Nearest opposing BoM is [above/below] → Favors: [Short/Long]
  Liquidity Sweep: Nearest LSZ is [above/below] → Initial sweep direction: [Up/Down]
  Zone Failure: [Support/Resistance] zone failing → Direction: [Down/Up]
  Macro Shape: [Shape chain with direction]
  Counter-Trend: Hard Wall at [level/None within 0.30] → [Counter-trend risk: HIGH/MODERATE/NONE]
  CONSENSUS: [Long/Short] ([X]/6 checks agree)
  If counter-trend: Justification: [explicit reason]
  Position Adjustment: [Full/Half/Quarter based on counter-trend risk]
```

**RULE:** If 4 or more of 6 checks disagree with the proposed trade direction, the direction MUST be reversed. No exceptions.

### 7.3 Scaled Entry Protocol

For high-conviction setups (God-Tier and High), scale into the position using 3 entry points:

1. **Zone First Touch (33% of position):** Enter when price first reaches the IP zone. This is the earliest entry — highest risk but lowest price.
2. **Zone Mid-Confluence (33% of position):** Enter at the zone's mid-confluence level (where the most key levels overlap inside the zone). This is the precision entry — the operator's preferred level.
3. **Zone Far Edge (33% of position):** Enter at the far edge of the zone (the side opposite the approach direction). This is the confirmation entry — price has proven the zone is holding.

**Average entry price** = weighted average of all triggered entries. **SL** = based on the worst-case entry (Zone First Touch). **TP** = based on the average entry price.

### 7.4 Trade Flow Continuity Protocol

Trade setups should be chained into continuous flow sequences. The TP of Trade N becomes the entry zone of Trade N+1. This creates a seamless flow: LONG from support → TP at resistance → SHORT from resistance → TP at support → repeat.

**Rules:**
1. Only chain setups that share a structural boundary (the TP zone of one is the entry zone of the next).
2. The direction flips at each zone boundary (LONG→SHORT at resistance, SHORT→LONG at support).
3. Each trade in the chain must independently meet the minimum RRR threshold.
4. Chain length: maximum 3 trades per chain. After 3, reassess the macro shape.
5. If a zone fails (breakout), the chain terminates and a new chain begins in the breakout direction.

### 7.5 Minimum RRR Standard

| Setup Quality | Minimum RRR | Rationale |
|:---|:---|:---|
| God-Tier (85+ confidence) | 4x | Highest conviction allows tighter RRR threshold |
| High (75-84 confidence) | 4.5x | Strong conviction, standard threshold |
| Standard (65-74 confidence) | 5x | Lower conviction requires higher RRR compensation |
| Supplementary (with flow continuity) | 3x | Part of a trade chain, compensated by adjacent trades |
| Swing Scalp (Scalp Stack) | 3x | Shorter-duration, higher-frequency setups |
| Reinforcement entries | 2x | Compensated by position sizing and primary trade RRR |
| Counter-trend in BS/WL regimes | 2.5x | Higher threshold for counter-trend in directional regimes |
| Counter-trend in SS regime | N/A | Both directions are trend-valid in SS per TS-6 |

### 7.6 Pair-Specific Trade Mechanics Note (v5.0.0)

When constructing trade setups for EUR/USD, GBP/USD, or AUD/USD (via Part IX translation):

- **Entry precision** uses PAIR-SPECIFIC zone edges and fib levels — NOT DXY zone edges converted to pair levels
- **SL placement** uses PAIR-SPECIFIC liquidity sweep zones from the pair's own swing structure — NOT DXY LSZs converted
- **TP identification** uses PAIR-SPECIFIC opposing zones and reaction levels — NOT DXY zones converted
- **Pip values** differ by pair: EUR/USD and GBP/USD = $10/pip (standard lot), AUD/USD ≈ $6.50/pip
- **Session timing** is the SAME for all pairs (London/NY sessions drive all three)
- **The macro shape chain** is the SAME for all pairs (same shapes, inverted direction per Part IX Section 9.10)

---


## PART VII-B: SWING SCALP SUB-MODULE

### 7S.0 Purpose

Swing Scalps are the SAME MECHANICS as HTF swings, executed on the Scalp Timeframe Stack (30m/15m/5m) within consolidation ranges. The operator named them "swing scalps" because they are scalping using the same mechanics as swing moves — supply to demand, demand to supply, institutional pressure zone to institutional pressure zone. The only difference is the timeframe stack and pip scale.

**Critical operator insight**: "Inside of ONE intraday 6x RR swing, there is literally 4x additional RR sitting inside it just by liquidity sniping the swing scalps that complete the HTF swing." This means swing scalps are NOT secondary trades — they are the PRIMARY profit engine during consolidation weeks.

### 7S.1 Swing Scalp Parameters

| Parameter | Swing (HTF) | Swing Scalp (LTF) |
|:---|:---|:---|
| HTF Storyline | 4H | 30m |
| Trading Timeframe | 1H | 15m |
| Precision TF | 30m | 5m |
| Typical SL | 8-15 pips | 3-6 pips |
| Typical TP | 40-100+ pips | 15-30 pips |
| Typical RRR | 4-10x | 4-6x |
| Min RRR | 4x (high-conf), 5x (standard) | 3.0:1 |
| Min SL distance | 2.5 pips | 1.5 pips (5m precision) |
| Entry timing | 3+ retests on 1H | 2+ retests on 15m |
| Session | NY | London + NY |
| Active when | BS/WL/Recovery shapes | SS/WLS/R shapes |
| Pip threshold | 40+ pips to TP | 15-30 pips to TP |

### 7S.2 Swing Scalp Setup Types — Full Procedural Specification

**TYPE 1: Standard Swing Scalp (consolidation range — MOST COMMON)**

*Procedural Steps:*
1. **Identify the consolidation range** on the 30m: Mark the ceiling (highest rejection level) and floor (lowest bounce level). These are the bounding zones.
2. **Map 15m S/D zones within the range**: For each S/D zone within the consolidation, classify as BoM or MoM. Mark reaction counts. BoM zones = primary entry. MoM zones = TP targets for opposing direction only.
3. **Determine direction bias**: Use pressure reading rules (Part II, 2.0). Which candles are bigger? Where are wicks pointing?
4. **Entry construction (per zone)**:
   - **LONG at floor demand**: Enter at 15m BoM demand zone reaction level (2nd retest minimum). SL 1.5-2 pips below the 15m zone edge. TP at the 30m ceiling zone boundary.
   - **SHORT at ceiling supply**: Enter at 15m BoM supply zone reaction level (2nd retest minimum). SL 1.5-2 pips above the 15m zone edge. TP at the 30m floor zone boundary.
5. **Apply 1-2-3 retest timing**: On the 15m timeframe, 2+ retests required for entry. Virgin 15m zones = no entry unless BoM.
6. **Apply BoM/MoM enforcement**: Same rules as HTF. BoM = entry. MoM = TP target. Virgin MoM = reject.
7. **Session tagging**: London session = scalp setups are PRIMARY. NY session = scalp setups are SECONDARY.
8. **RRR check**: Minimum 3.0:1 for swing scalps. If consolidation range is too narrow (<15 pips), REJECT and wait for range expansion or breakout.

*Both directions are valid in SS* — SHORT from ceiling supply and LONG from floor demand are CO-EXISTING setups (TS-6 applies at every scale).

**TYPE 2: Double Whiplash Inverse (SS(DWL) compound setup)**

*Procedural Steps:*
1. **Confirm SS(DWL)**: Two whiplash moves observed in ≤1.5 sessions. Price has hit both ceiling and floor at least once with strong rejections at both.
2. **Leg 1 — SHORT on supply zone hit**:
   - Entry: At ceiling supply zone rejection. SL: 1.5-2 pips above ceiling supply zone edge. TP: At floor demand zone boundary. RRR: Must meet 3.0:1 individually.
3. **Leg 2 — LONG on demand zone reaction** (entered IMMEDIATELY after Leg 1 TP hits):
   - Entry: At floor demand zone reaction. SL: 1.5-2 pips below floor demand zone edge. TP: At ceiling supply zone boundary. RRR: Must meet 3.0:1 individually.
4. **Combined RRR**: Both legs compound. If Leg 1 = 4:1 and Leg 2 = 4:1, combined = 8:1.
5. **Risk management**: Position sizing for Leg 2 should account for the possibility that the floor zone FAILS (breakout transition). If Leg 2 gets stopped out, the SS→BS transition is likely activating — switch to Swing Stack.

*Key rule*: The Double Whiplash Inverse ONLY works when both bounding zones are holding. If either zone shows 3+ reactions (depleted), expect a breakout instead. Map the SS→BS Transition Setup (Type 4) as a contingency.

**TYPE 3: Liquidity Snipe (5m precision within confirmed 15m move)**

*Procedural Steps:*
1. **Wait for 15m confirmation**: A 15m swing scalp entry has triggered and price is moving toward TP. Do NOT snipe before confirmation.
2. **Drop to 5m for zone mapping**: Identify ALL unmitigated 5m liquidity zones between current price and the 15m TP.
3. **Entry at 5m zone reaction**: When price reaches a 5m zone, wait for a brief reaction. Enter at the zone reaction level.
4. **SL**: 1.5 pips outside the 5m zone edge.
5. **TP**: Next 5m zone in the trade direction, OR the 15m TP target if the next 5m zone is too close.
6. **Progressive SL management**: As each snipe confirms, move SL on earlier entries to breakeven.
7. **Maximum snipes per move**: 2-3 per 15m swing scalp. More than 3 = overtrading.

*Key operator quote*: "The money is made catching movement from one liquidity zone to another. It is already moving." The snipe is NOT predicting direction — it is riding a confirmed move and entering at each guaranteed touchpoint along the path.

**TYPE 4: SS→BS Transition Scalp (consolidation ending)**

*Procedural Steps:*
1. **Detect late consolidation**: ZFP trending up on the bounding zone, price testing one side of the range repeatedly, 15m shows higher highs or lower lows forming within the range.
2. **Set breakout trigger**: Identify the structure level that must break. For SHORT: a lower low below the consolidation floor. For LONG: a higher high above the consolidation ceiling.
3. **Entry**: On the close below/above the structure level on the 15m (NOT the 5m — 5m is too noisy for breakout confirmation).
4. **SL**: Opposite side of the consolidation range + 2-3 pip buffer.
5. **TP**: Next HTF (1H) liquidity zone in the breakout direction, per Timeframe Element Matching (up to 2 TF dimensions from source). NOT the 30m zone — breakout surges target higher-TF zones. NOT 4H — that exceeds the 2-dimension limit from 15m source.
6. **Timeframe Element Matching**: Breakout originating from 15m liquidity → TP at 30m or 1H zone (up to 2 TF dimensions higher, NOT 4H). 4H targets are ONLY valid when the breakout source is 1H or 4H.
7. **Transition from Scalp Stack to Swing Stack**: Once the breakout confirms, all subsequent entries (reinforcements) use the Swing Stack.

*Key rule*: "If not right near a strong 4H pressure zone right now — BS is most likely days away." Only map transition setups when price is ACTUALLY near an HTF zone with rising ZFP.

### 7S.3 Swing Scalp within HTF Moves

Inside of ONE intraday 6x RR swing, there is literally 4x additional RR sitting inside it just by liquidity sniping the swing scalps that complete the HTF swing. Every intermediate liquidity zone that price has not yet touched since beginning the move WILL be touched — these are guaranteed swing scalp entries.

**Mapping procedure for swing scalps within HTF moves:**
1. Identify the HTF swing setup (Engine 3 Phase 0-6 output).
2. Map ALL intermediate liquidity zones on the 15m between entry and TP of the HTF swing.
3. Each intermediate zone that price has NOT yet retested = a potential swing scalp entry.
4. The entry on the 15m is at the zone reaction level (same mechanics as Standard Swing Scalp).
5. The TP for each swing scalp = the NEXT intermediate zone in the HTF trade direction.
6. The final swing scalp TP = the HTF swing's TP target.
7. Combined RR of all swing scalps within the HTF move typically = 4x the HTF swing RR alone.

### 7S.4 Swing Scalp BoM/MoM and Reaction Counter Rules

All BoM/MoM enforcement rules apply identically at the 15m level:
- **15m BoM zones**: PRIMARY entry source for swing scalps. 100% guaranteed reaction if unmitigated.
- **15m MoM zones**: TP targets for opposing direction. Entry ONLY with exceptions.
- **15m virgin MoM zones**: DEATH ZONE. Reject for entry.
- **15m depleted zones (3+ reactions)**: TP targets only. Zone about to fail.

Zone reaction counter also applies at 15m:
- 0 reactions (virgin) = strongest if BoM; DEATH ZONE if MoM
- 1-2 reactions = active, still has juice, valid for entries if BoM
- 3+ reactions = depleted, use for TP only, NOT entry
- If a 15m pressure zone with juice exists between current PA and the 15m BoM zone, price will liquidate that zone first

### 7S.5 Swing Scalp Output Format

**v5.3.3 UPDATE — MANDATORY DAY + SESSION + SHAPE FIELDS:**

```
SWING SCALP SETUP: S-[#] [Direction] [Quality]
DAY: [Monday/Tuesday/Wednesday/Thursday/Friday] ← v5.3.3 MANDATORY
SESSION WINDOW: [London / NY / Both] ← v5.3.3 MANDATORY
SHAPE TRIGGER: [SS/WLS/R/SS(DWL)] ← v5.3.3 MANDATORY — which consolidation shape activates this scalp
SETUP CATEGORY: Swing Scalp ← v5.3.3 MANDATORY
ANCHOR HIT WINDOW: [when the 15m zone is expected to be reached] ← v5.3.3 MANDATORY
Consolidation Range: [X.XX–X.XX] | Phase: [Early/Mid/Late]
Scalp Stack: 30m/15m/5m | Engine 2 Shape: [SS/WLS/R]
POI: [15m Zone Name] | BoM/MoM: [classification] | Reactions: [count]
Entry: [exact level] — [15m zone reaction level]
SL: [exact level] — [anchor: 15m zone edge + buffer]
TP: [exact level] — [opposing 30m zone boundary]
Sequential 15m Zone Path: [list intermediate 15m zones between entry and TP]
RRR: [X]:1
Confidence: [score]/100
Day Catalysts: [expiries / events / auctions on this day] ← v5.3.3 MANDATORY
```


## PART VII-C: REINFORCEMENT ARCHITECTURE

### 8R.0 Purpose
Reinforcements transform a 1D trade (single entry/SL/TP) into a 2D trade (entry + reinforcements) or 3D trade (entry + reinforcements + multi-chart execution). The combined R:R of a reinforced trade can reach 25-30x vs the single-entry 4-6x.

**v5.3.3 ADDITION — Reinforcement Timing Inheritance:** Reinforcement entries inherit the DAY of their parent trade. If the primary HTF swing is mapped to Wednesday NY session, then:
- Reinforcement rockets are SET UP during Wednesday London premarket (the standard setup window)
- Reinforcement rockets TRIGGER during Wednesday NY session (when price reaches trigger zones)
- Reinforcement rockets that don't trigger by NY close Wednesday may trigger Thursday London (shift +1 day)
- This means the reinforcement schedule is known IN ADVANCE — the trader sets up all rockets Wednesday morning and knows which ones are expected to fire by end of day
- The Weekly Execution Calendar (Section 8.5) must list reinforcements under the SAME DAY as their parent trade

**Dimension Classification:**
- **1D Trade**: Linear — Entry, SL, TP. Single position. R:R typically 4-6x.
- **2D Trade**: Add liquidity reinforcements to the linear setup. Multiple entries at intermediate zones. Combined R:R typically 15-25x.
- **3D Trade**: Add multi-chart execution (DXY master + pair charts). Combined R:R typically 25-30x+.

### 8R.1 Liquidity Ladder System — Full Procedural Specification

Once an initial entry is confirmed and starts moving toward TP, additional entries are placed at each intermediate liquidity zone along the trade path.

**Procedural Steps:**
1. **Confirm the primary entry is moving**: The 1-2-3 retest is complete. Price has left the entry zone with momentum.
2. **Map ALL intermediate liquidity zones between entry and TP**: Apply Sequential Liquidity Sweep rule.
3. **Place stop orders at the FAR EDGE of each zone**: The far edge is the side OPPOSITE to where price is approaching from. This ensures: if price reaches zone, reacts, and rebounds — we do NOT enter. If price BREAKS THROUGH — stop order triggers, confirming zone failed and move continues.
4. **Classify each reinforcement entry**:
   - **BoM intermediate zones**: Expect STRONG reaction. Move may stall. If a BoM zone of the OPPOSING direction is in the path, consider it a TP2 or TP1 adjustment.
   - **MoM intermediate zones**: Expect minor reaction then continuation. Do NOT set TP at MoM zones in the trade path if trend-aligned — they'll be pierced.
   - **Depleted zones (3+ reactions)**: Price will slice through. Minimal reaction. Use as momentum confirmation.
5. **SL for reinforcement entries**: Swing Stack = 2.5-3 pips outside intermediate zone. Scalp Stack = 1.5 pips outside 5m zone. Progressive SL tightening as each reinforcement confirms.
6. **TP for reinforcement entries**: Same TP as primary setup. All reinforcements target the same TP1.
7. **At least 2 reinforcement entries must be inside the SL of the primary trade**: Critical risk management rule.

### 8R.2 Fibonacci Rocket System

**Standard Rocket Levels:**

| Level Type | Fibonacci Level | Purpose | Reaction Type |
|:---|:---|:---|:---|
| Entry | 0.618 – 0.786 | Primary entry zone | — |
| Rocket 1 | 1.382 – 1.786 | First reinforcement (CLEANEST entry — 90% accuracy) | Strong pressure zone |
| Trigger | 2.382 – 2.786 | Second reinforcement / confirmation | Momentum zone |
| Target | 3.382 – 3.786 | Extended TP target | — |

**Shorter Move Rocket Levels:**

| Level Type | Fibonacci Level | Purpose |
|:---|:---|:---|
| Entry | < 0.382 | Quick entry |
| Rocket 1 | 0.618 – 0.786 | First reinforcement |
| Trigger | 1.382 – 1.786 | Second reinforcement |
| Target | 2.382 – 2.786 | Extended TP target |

**Fibonacci Key Level Zones (v5.3.0 — From Trading Laws):**

| Level | Sub-Range | Character |
|:---|:---|:---|
| **0.382** | .382 – .5 | Initial strong reaction. First sign of pressure. |
| **0.618** | .5 – .618 | Transitional pressure. |
| **0.618 – 0.786** | .618 – .786 | **STRONG PRESSURE ZONE**. Most reliable reaction range. |
| **0.786** | .786 – 1 | **Final blast**. Last chance before full extension. |

**Initial Fib Mapping Procedure (MANDATORY for every Fibonacci Rocket):**
1. Map the nearest swing high/low on the 15m chart
2. For a SELL move: Use the support level of entry zone as the "bottom" of the Fib tool. Nearest swing high prior to consolidation = "top". Fibonacci Map = DOWN.
3. For a BUY move: Use the resistance level of entry zone as the "bottom" of the Fib tool. Nearest swing low prior to consolidation = "top". Fibonacci Map = UP.
4. The 1.382–1.786 level is the **cleanest entry for a reinforcement rocket**. "The exact Fib lines should line up with 90% accuracy to the actual entry."
5. The trigger zone should be around the 2.382–2.786 level.

**Three-Type Rocket Classification (v5.3.0 — See Section 8R.6 for full specs):**
- **FLR (Fibonacci Liquidity Rocket)**: First time price contacts a Fib level. 30m scale. THICK buffer (2 thick or 3 thin zones). Earth Element Heavy Attack.
- **FR (Fibonacci Rocket)**: Localized Fib levels on 15m for LSS/scalps. Fire Element Precision Attack.
- **LR (Liquidity Rocket)**: Subsequent contacts. Zone-to-zone. THIN buffer (1 thick or 2-3 thin zones). Water Element Precision Attack.
- **When Fib levels and Liquidity Ladders overlap**: Strongest reinforcement entry — dual confluence.

**If a Key 1-2 Fibonacci level is UNMITIGATED — setup as FR (Fibonacci Rocket with thick buffer). After the Fib level has been mitigated by an FR setup — then it can be setup as LR (Liquidity Rocket with thin buffer).**

**20-30% failure rate is ACCEPTABLE.** 70-80% success rate is excellent.
**NY session rockets require 3 pip SLs minimum** or they explode.

### 8R.3 Multi-Zone Overlapping — Risk Management
1. At least 2 reinforcement entries must be inside the SL of the primary trade.
2. Before SL hits on the primary, 2+ reinforcements should have opened.
3. Position sizing: Primary = full size. Reinforcements = 50-75% of primary.

### 8R.4 TP Management (Trade Management — Operator Discretion)
1. **70-80% TP rule**: Move SL to 65-70% profit when price reaches 70-80% of TP and starts reacting.
2. **BoM re-entry**: After TP hit, re-enter from BoM zone for continuation if unmitigated.
3. **SL adjustment at intermediate BoM zones**: Move SL beyond reaction zone if BoM opposing zone causes strong reaction.
4. **Reinforcement SL trailing**: Trail SL to most recent intermediate zone that held.

**PROFIT TAKING LAW — Air Element Infrastructure (v5.3.0 — MANDATORY):**
- Close ALL open trades by NY market close. No London-mapped trades run overnight.
- The only exception: trades OPENED at NY market end for Tokyo/London price action.
- If trade analysis is strong, re-enter during Tokyo and catch the rest of the wave.
- If everything cannot be moved 30-50% in profit, automatically take ALL profits before market close. Mandatory.
- "Whatever profits are floating at the end of the day from open trade — CLOSE THEM. TAKE ALL THE PROFITS. You can re-enter tomorrow. If it is REALLY a winning trade, you can re-enter."

### 8R.5 4H BoM Cascade Rule (CRITICAL)
**"BoM Unmitigated 4H liquidity will usually pierce through everything until it reacts to liquidity of the same element."**

1. Reinforcements between 4H BoM entry and 4H target: All intermediate 1H and 30m zones will be PIERCED. Place reinforcements expecting quick triggers.
2. TP targeting for 4H BoM cascade: Move only stops at next 4H zone of same element. True TP1 = next 4H zone, NOT nearest 1H zone.
3. SL buffer: 3-5 pips minimum for 4H BoM cascade volatility.
4. Reinforcement density: 3-4 reinforcements (vs normal 2) because move travels further.

### 8R.6 Three-Type Rocket Architecture (v5.3.0 — CRITICAL — From Trading Laws + Trading Infrastructure)

Reinforcement rockets are classified into three types, each with a distinct elemental profile, buffer requirement, trigger mechanism, and use case. Selecting the correct rocket type is MANDATORY — using the wrong type at the wrong time causes preventable failures.

**FLR (Fibonacci Liquidity Rocket) — Earth Element Heavy Attack**

| Property | Specification |
|:---|:---|
| **Elements** | Air (30m Fib triggers) + Earth (Liquidity Zone entry/SL anchors) — Earth Heavy Attack combining Air prediction with Earth density anchoring |
| **Scale** | 30m Fibonacci Levels as Trigger points, Liquidity Zones as Entry/SL points |
| **Use** | Forward-mapping HTF storyline moves. "Fibonacci Vision highlights highest probability LR setups." |
| **Buffer** | THICK — 2 Thick Zones or 2-3 Thin Zones between trigger and entry. At least one FULL zone buffer between trigger + entry zone. |
| **Trigger** | Stop price 1-2 pips INSIDE the target liquidity zone (prevents false sweeps) |
| **Entry** | At Liquidity Zone edges confirmed by Fib levels |
| **SL** | 1-2 pips OUTSIDE back edge of SL zone |
| **Rocket Capacity** | Part of max 3 rockets per trade. Conscious RAM required — ONE pair only per FLR session. |

**Definition:** "When I am using extended Fibonacci Zones (1-2 levels) to forward map Liquidity Rockets for the HTF storyline on the 30m chart. Fibonacci Vision highlights highest probability LR setups. In FLR I am using 30m Fibonacci Levels as Trigger points and Liquidity Zones as entry/SL points. Liquidity zones are fundamental anchor points for trade setups."

**FR (Fibonacci Rocket) — Fire Element Precision Attack**

| Property | Specification |
|:---|:---|
| **Elements** | Air (15m Fib levels) + Fire (precision strike on S/D zones) — Fire-style attack using Air targeting to engage Fire (S/D) density |
| **Scale** | 15m storyline for LSS (London Session Scalping) and 5m Swing Scalps |
| **Use** | Localized Fib levels on the 15m chart for London Session Scalping and 5m swing scalps |
| **Buffer** | Standard — 1-2 zone buffer |
| **Trigger** | 15m Fibonacci Levels as Trigger, Entry, and Stop Loss Points |
| **Entry** | At Fib-confirmed zone edges on 15m |
| **SL** | 1-2 pips outside SL zone. Key Horizontal Lines count as "thin zone" for trade setups. |
| **Rocket Capacity** | Part of max 3 rockets per trade |

**Definition:** "When I am using the 15m storyline to map localized Fib levels on the 15m chart for LSS or 5m Swing Scalps. In FR I am using 15m Fibonacci Levels as Trigger, Entry, and Stop Loss Points. Liquidity zones provide confluence and precision for trade execution. Key Horizontal Lines are valid anchor points for trade execution — count as a 'thin zone' for trade setups."

**LR (Liquidity Rocket) — Water Element Precision Attack**

| Property | Specification |
|:---|:---|
| **Elements** | Earth (pure liquidity flow through Earth density channels) — Water-style attack flowing through Earth (liquidity) channels like water through a riverbed |
| **Scale** | Zone-to-zone during confirmed moves |
| **Use** | Standard reinforcement rockets based on price action mechanics. "Simple & obvious. Built-in 20-30% failure rate." |
| **Buffer** | THIN — 1 Thick Zone OR 2-3 Thin Zones. NO entry buffer zone required. |
| **Trigger** | Stop price 1-2 pips INSIDE target liquidity zone. First zone = normal rules. Zone 2 onwards = optional relaxed trigger (0.5 pips inside instead of 1 pip for back-to-back rockets). |
| **Entry** | Pure S/D/L mechanics — "During swing scalps (LSS prime environment), the fib is used to map the NY session move and then ignored for any LSS trade setups. LSS trade setups are pure S/D/L mechanics. Flow with it." |
| **SL** | 1-2 pips outside SL zone's back edge. ALWAYS 1 FULL PIP OUTSIDE BACK EDGE. NO EXCEPTIONS. ESPECIALLY IF THIN. |
| **Expected RRR** | 2-4x (lower than Fib Rockets) |
| **Rocket Capacity** | Part of max 3 rockets per trade |

**If thin zones sit inside a 4H liquidity pool — each thin zone counts as "2 thin zones" for Liquidity Rockets.** The 4H container amplifies the thin zone's effective density.

**ROCKET SAFETY RULES (MANDATORY):**
- **Maximum 3 rockets per trade (recommended 2).** Exceeding this concentrates too much risk in one direction.
- **Rockets on ONE pair at a time.** Conscious RAM must be allocated to manage rocket-enhanced trade setups. Simple set-it-and-forget-it entries on multiple pairs are fine, but FLR targets require conscious attention.
- **After $1,000,000 of live profits have been caught, this rule may be reconsidered.**
- **NY session rockets require 3 pip SLs minimum** or they explode.
- **London session rockets: 1-2 pip SL buffer.**
- **We DO NOT reinforce THIN LIQUIDITY ZONES.** We DO reinforce THICK LIQUIDITY ZONES — they are much more likely to hold and provide real fuel.

### 8R.7 Stop-Limit Order Mechanics for Rockets (v5.3.0 — CRITICAL — From Trading Laws — OPERATOR VERIFIED)

**Reinforcement rockets are named after a BATTLEFIELD CONCEPT — trip-wire activated weapons.** This is NOT a metaphor. It is a PRECISE mechanical description:

- The **trip-wire** is a STOP ORDER placed at a specific price level (the trigger zone)
- When price action "trips the wire" (hits the stop price), the stop order activates
- The stop order creates a LIMIT ORDER at a different price level (the entry zone)
- The limit order is the "rocket" — it fires when the trip-wire is triggered
- This is a STOP-LIMIT ORDER — a BUILT-IN MetaTrader mechanic

**How the self-executing algorithm works:**
1. You set up the primary entry AND all reinforcement rockets at the SAME TIME (London session premarket)
2. The rockets SELF-GENERATE as price action triggers the stop orders — you don't need to be on the chart
3. By the time a rocket triggers, the primary entry is already in profit → move SL to breakeven → COMPLETELY RISK-FREE reinforcement
4. If analysis is CORRECT: doubled or tripled upside, risk-free
5. If analysis is WRONG: only the primary entry takes a loss — same capital at risk, no additional risk
6. If rockets trigger but fail (20-30%): primary entry already in profit at BE or minor profit — loss is offset

**Instead of coding an algorithm to detect price action and putting it in MetaTrader, you set up that algorithm MANUALLY based on price action analysis and stop-limit orders. It's a one-and-done algorithmic reinforcement specific to this one instance.** Set it up in the morning, walk away, come back at 10 PM and check the results. The trades take care of themselves.

**Complete procedural specification for reinforcement rocket placement using stop-limit orders:**

**Trigger Zone Selection:**
1. Trigger zones should be 2-3 zones IN FRONT of entry zone (in the direction price must travel to reach the entry)
2. At least ONE FULL zone buffer between trigger + entry zone
3. Thin liquidity zones are NEVER allowed as trigger zones, entry zones, or stop loss zones
4. If there are 2 thin zones in front of the entry zone — make the 3rd zone the trigger zone
5. "90% of rockets will self-activate if stop is placed 2-3 zones in front of the entry" — Ladder Method

**Trigger Price Precision:**
1. Stop price must be 1-2 pips INSIDE the target liquidity zone — NOT on the edge. This prevents false sweeps from triggering the limit order.
2. For Rocket #1: Trigger price is 1-2 pips inside the CLOSE EDGE of the trigger zone
3. For Rocket #2/3: Trigger price is 1-2 pips inside the FAR EDGE of the trigger zone
4. For LR back-to-back rockets on grouped zones: Zone 2+ can use 0.5 pip inside instead of 1 pip (relaxed trigger)

**Entry Criteria — 4-Point Precision (MANDATORY for every rocket):**
Every rocket entry must specify:
1. **Front edge/middle of the zone** — Where the limit order activates
2. **Back edge of the zone** — Maximum entry deviation
3. **Front edge of the SL zone** — Minimum SL distance
4. **Middle/back edge of SL zone** — SL placement for thin liquidity with extended SL

**Stop Loss Placement:**
1. SL 1-2 pips OUTSIDE THE BACK EDGE of the stop-loss zone
2. If thin liquidity zone — move SL 1 pip inside the next zone (extra buffer)
3. NY session: 2-3 pips outside. London session: 1-2 pips outside
4. "If there is not this much distance — the rockets will likely blow up in your face"
5. ROCKET STOP LOSSES ALWAYS 1 FULL PIP OUTSIDE BACK EDGE OF ZONE. NO EXCEPTIONS. ESPECIALLY IF THIN.

**Triple Anchor Reinforcement (MANDATORY):**
Each reinforcement must be anchored to THREE zones:
1. **Stop zone target** — The zone that triggers the stop-limit order
2. **Entry zone** — The zone where the limit order fills
3. **Stop Loss zone** — The zone that anchors the SL

**Fibonacci Tool Mapping:**
Use the Fibonacci Tool to map reinforcement points:
- Map the nearest swing high/low on the 15m
- Support/resistance level of entry zone = "bottom" of fib tool
- Nearest relevant swing high/low = "top"
- Sell move: Support of entry = bottom, nearest swing high prior to consolidation = top, Fib Map = down
- Buy move: Resistance of entry = bottom, nearest swing low prior to consolidation = top, Fib Map = up

### 8R.8 VLM-Verified Rocket Mechanics from Winning Trade Library (v5.3.2 — CRITICAL — OPERATOR VERIFIED VIA VLM ANALYSIS — AUDITED AND CORRECTED)

**EMPIRICAL VERIFICATION**: Deep VLM analysis of 38 chart images from the Winning Trade Library identified 6 charts with T (Trigger), E (Entry), SL (Stop Loss) labels — direct visual evidence of reinforcement rockets deployed on live winning trades. All 6 charts are GBPUSD on 15m/30m (the primary scalp pair on execution timeframes). Initial VLM analysis contained classification errors (VLM was not given correct system context). A second audit pass was run with correct system rules provided to VLM. Findings below are from the CORRECTED audit:

**VLM-VERIFIED PATTERN 1 — T, E, AND SL CONSISTENTLY AT THICK LIQUIDITY ZONES (RULE-CONFIRMED):**
Every Trigger, Entry, and Stop Loss label across all 6 charts sits at a THICK (high-density) liquidity zone. This directly confirms the source document rule: "Thin liquidity zones are NEVER allowed to be entry zones or stop loss zones." The corrected audit confirms the rule was followed on all 6 winning trade charts. **Important nuance (operator guidance):** While the system rule states thin zones are NEVER entry/SL zones (making E effectively at thick zones by rule), this should not be stated as an unconditional empirical absolute — it is a RULE that is followed by design, and the VLM evidence confirms rule compliance on these specific charts. The operator has indicated that E placement is context-dependent and should not be oversimplified as "always thick" or "always thin" in absolute terms — the rule is the rule, but reality may present edge cases not captured in 6 charts.

**VLM-VERIFIED PATTERN 2 — BUFFER ZONES BETWEEN T AND E ARE VARIABLE (NOT FIXED AT 1):**
The corrected audit shows BOTH 1-zone buffers AND 2-zone buffers between T and E, depending on zone thickness and rocket type:
- **LR (Liquidity Rocket)**: 1 buffer zone between T and E — confirmed on multiple groups. Buffer can be thick or thin.
- **FR (Fibonacci Rocket)**: 2 buffer zones between T and E — confirmed on groups where Fibonacci levels are present or zone structure requires it.
This directly matches the source document specifications: LR = "1 Thick Zone OR 2-3 Thin Zones" buffer; FR = "2 Thick Zones or 2-3 Thin Zones" buffer. The initial VLM claim of "always 1 zone buffer" was incorrect — it varied by rocket type.

**VLM-VERIFIED PATTERN 3 — CONDITIONAL BUFFER LOGIC CONFIRMED (THICK vs THIN ZONES):**
The source document rule is confirmed by VLM evidence: when the zone directly in front of the entry is THICK, 1 zone buffer is sufficient. When the zones in front are THIN, 2-3 zones are needed to reach a thick zone for the trigger. "If there are 2 thin zones in front of the entry zone - make the 3rd zone the trigger zone." Multiple thick zones back-to-back = 1 zone buffer is fine. This is NOT a fixed number — it is CONDITIONAL on zone thickness.

**VLM-VERIFIED PATTERN 4 — T→E GAP: 10-20 PIPS ON GBPUSD (MOST COMMONLY ~15 PIPS):**
The trigger-to-entry distance (the "tripwire gap") consistently measures 10-20 pips on GBPUSD across all 6 charts, with ~15 pips being the most common. This provides a concrete pip-range benchmark for rocket placement on GU. This distance reflects the zone-to-zone spacing including buffer zones.

**VLM-VERIFIED PATTERN 5 — E→SL DISTANCE: 18-45 PIPS ON GBPUSD:**
The entry-to-stop-loss distance varies from 18-45 pips depending on zone structure. This reflects the zone-to-zone spacing on the specific timeframe (15m vs 30m). The SL is at the next thick zone beyond the entry, providing the Liquidity Shield.

**VLM-VERIFIED PATTERN 6 — BOTH LR AND FR PRESENT ON WINNING TRADES:**
The corrected audit shows that winning trades use BOTH rocket types — not just LR. Within the same trade, some rocket groups are LR (1 buffer) and some are FR (2 buffers), depending on the zone structure at each specific rocket placement point. The initial claim of "LR dominates 83%" was an artifact of incorrect VLM classification, not a real pattern. The source document confirms: "During swing scalps (LSS prime environment) — the fib is used to map the NY session move and then ignored for any LSS trade setups. LSS trade setups are pure S/D/L mechanics." LR is more common in LSS environments, but FR is used when Fibonacci levels align with the zone structure.

**VLM-VERIFIED PATTERN 7 — 2-3 ROCKETS PER TRADE (CONFIRMS MAX 3 RULE):**
2 charts have 2 rocket groups, 2 charts have 3 rocket groups, 2 charts have 1+1 (primary + 1 reinforcement). All within the "max 3 rockets per trade, recommended 2" rule from Section 8R.6.

**VLM-VERIFIED PATTERN 8 — FR/FLR FIBONACCI ALIGNMENT CONFIRMED ON 1 CHART:**
One chart (page16_img1) shows Fibonacci levels (0.618, 1.618, 2.618) alongside T/E/SL labels with 2 thick buffer zones between T and E — a clear FR setup. The T and E positions align with Fib levels, confirming the system's claim that 1.382-1.786 = cleanest entry for reinforcement rocket and 2.382-2.786 = trigger zone.

**VLM-VERIFIED PATTERN 9 — ROCKETS FILL WHEN MACRO SHAPE CONFIRMS DIRECTION:**
All charts where the macro shape confirmed direction showed successful rocket fills. The chart where rockets did NOT fill had a BS(Reverse) → Recovery Surge transition — the 20-30% failure rate in action, occurring when direction is not yet fully confirmed.

**VLM-VERIFIED PATTERN 10 — FLR FIRST-CONTACT RULE CONFIRMED:**
The source document rule is: "When mapping FLR - the FIRST point of contact with Fibonacci levels must be mapped as a Fibonacci Rocket w/ 2 thick or 3 thin liquidity zone buffers. Subsequent points of contact with the same fib level can be mapped as Liquidity rockets with only 1 thick or 2-3 thin zone buffers." This is consistent with the VLM evidence showing mixed LR/FR within the same trade — the first Fib contact uses FR (2 buffer), subsequent contacts use LR (1 buffer).

**CORRECTED ROCKET ARCHITECTURE DIAGRAM:**
```
THICK Liquidity Zone (Earth - High Density)
├── T (Trigger) = STOP ORDER placed 1-2 pips inside close edge
│   │   When price hits T → stop order activates
│   │
│   └── [BUFFER ZONE(S)] — 1 zone for LR, 2 zones for FR
│       │   Buffer zones can be thick or thin
│       │   If buffer is thin → need MORE zones until thick zone found
│       │   "If 2 thin zones in front → make the 3rd zone the trigger"
│       │
│       └── THICK Liquidity Zone (Earth - High Density)
│           ├── E (Entry) = LIMIT ORDER placed at thick zone
│           │   Price fills the limit order here
│           │   Thin zones are NEVER entry zones
│           │
│           └── Next THICK Liquidity Zone (Earth - Shield)
│               └── SL (Stop Loss) = 1-2 pips outside back edge
│                   Thick zone provides Liquidity Shield protection
│                   Thin zones are NEVER SL zones
```

### 8R.9 Master Trade Setup = E + FLR (v5.3.0 — HIGH — From Trading Infrastructure)

**The Master Trade Setup is the ultimate expression of fractal integration — a trade architecture that unifies ALL FOUR elemental densities into a single executable position.**

**E (Entry)** = Earth + Fire — Entry at a liquidity zone (Earth) with supply/demand overlap (Fire). The entry is where institutional firepower (Fire) meets institutional liquidity (Earth). Fire needs Earth — the move ignites because S/D (Fire) has the fuel of liquidity (Earth) at the same price level.

**FLR (Fibonacci Liquidity Rocket)** = Air + Earth — Fibonacci-anchored prediction (Air) with liquidity zone validation (Earth). The rocket entry points are predicted by Air (Fib spiderweb anchored to Earth density points) and the entries/SLs are at Earth (liquidity zones).

**The Master Trade Setup creates a trade where:**
- **Earth**: Entry is at a liquidity zone / IP zone (institutional pressure, foundational anchoring)
- **Fire**: Entry overlaps with S/D zone (institutional firepower, directional energy)
- **Water**: Macro shape confirms the direction and timing (wave form alignment)
- **Air**: Fibonacci spiderweb maps the complete pathway from entry to TP, including every rocket reinforcement point (predictive trajectory)

When all four elements converge = Avatar State. The signal is FRACTALLY LOCKED — it exists at every scale simultaneously.

**Specification:**
1. Begin with a standard entry (Section 7.1) at a BoM S/D zone (Fire) overlapping with a liquidity zone (Earth)
2. Identify the macro shape (Water) — confirm the direction and timing of the wave
3. Map the NY Fibonacci Rocket setup — identify key 1 and 2 Fib levels (Air)
4. Map liquidity specifically around the 1.382-1.786 and 2.382-2.786 zones using 15/30m chart (Earth anchors for Air prediction)
5. Place up to 3 FLR rockets at the Fib-confirmed liquidity zones (Air triggers + Earth entries)
6. Place additional LR rockets at intermediate liquidity zones between FLR positions (Water flow through Earth channels)
7. Total active rockets: Up to 7 with hardwired safety and risk management self-managed autonomously

**Profit Management for Master Trade Setup:**
- "I only need to decide if I TP at the end of NY session, or move everything into 30-50% profit and let it run overnight."
- "If everything cannot be moved 30-50% in profit we automatically take all profits before market close. Mandatory."
- See Section 8R.4 for full TP management rules.

**"Once you have this you have everything."** The Master Trade Setup is the full expression of the Trident's fractal architecture — Earth (liquidity anchor), Fire (S/D firepower), Water (macro shape), Air (Fibonacci trajectory) all converge into a single position that is nearly impossible to fail because it is anchored at every scale simultaneously. This is the Avatar State — the trader becomes the instrument through which all four elements flow.

### 8R.9 Efficient Liquidity Mapping (v5.3.0 — HIGH — From Trading Infrastructure)

**Don't map the entire chart. Map ONLY what matters for the trade setup.**

**Procedure:**
1. Map the NY Fibonacci Rocket Trade Setup first — identify key 1 and 2 Fib levels
2. Map the liquidity SPECIFICALLY around these zones:
   - Use the 15/30m chart
   - Scroll AS FAR LEFT as needed to find all liquidity zones around the 1.382-1.786 and 2.382-2.786 levels
   - "Remember this is the cleanest entry for a reinforcement rocket. The exact Fib lines should line up with 90% accuracy to the actual entry."
3. Liquidity OUTSIDE the 0-1 and key 1/2 levels can mostly be ignored
   - We don't need to map the entire chart — just the surrounding area of the key levels
4. Fibo tool powers efficient liquidity mapping:
   - Reduces trade setup latency
   - Faster execution
   - Increased hardwired precision

**Fibonacci Rockets + Liquidity Rockets Simultaneously:**
When mapping FLR, the Fibo tool reveals both the Fib entry points AND the liquidity zones in the same view. Engineer both together:
- Full trade setup = Entry + FR + LR
- Master Trade Setup = Entry + FLR

---

