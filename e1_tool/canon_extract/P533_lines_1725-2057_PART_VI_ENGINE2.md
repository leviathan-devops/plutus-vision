## PART VI: ENGINE 2 — MACRO SHAPE CHAIN MAP

Engine 2 forward-maps the shape of the coming week's price action by identifying which macro shape chain will dominate, anchored to the IP zones produced by Engine 1. Engine 1 answers: "Where are the walls?" Engine 2 answers: "What path will price take through those walls?"

**PRIMARY ANALYSIS TIMEFRAME: 1H**

All macro shape classification, chain mapping, and session decomposition MUST be performed on the 1H timeframe as the primary analysis layer.

**Timeframe Hierarchy:**
- **1H (PRIMARY):** Shape classification, chain construction, day-by-day mapping
- **4H (STRUCTURAL):** Validates SS range boundaries and BS direction — never primary
- **30m (SUPPLEMENTARY):** Intra-session detail only — never used for shape classification
- **D1 (MACRO):** Regime context only — weekly trend direction

**MANDATORY:** The weekly shape chain visualization MUST be derived from 1H analysis. The report MUST state: "Primary Timeframe: 1H | Structural Validation: 4H"

### 6.1 Macro Shape Taxonomy

Four base macro shapes describe all DXY price action on the Higher Timeframe (HTF: 4H/D1/W1). Every trading session exhibits one of these shapes or a variant thereof. Shapes are mechanically defined by the relationship between price action and IP zone architecture.

#### 6.1.1 Swing Scalps (SS)
**Definition:** Price oscillates within a defined range bounded by IP zones above (resistance ceiling) and below (support floor), forming a series of swing highs and swing lows that respect these boundaries. Each swing typically spans 1-3 trading sessions.
**IP Zone Signature:** Both ceiling and floor IP zones have ZFP below 30%. Option expiry positioning cages price between large strikes.
**Subtype — Double Whiplash Pattern:** Two rapid whiplash moves in succession within the range. Labeled "SS (Double Whiplash)" — indicates heightened volatility often preceding a breakout attempt.

#### 6.1.2 Breakout Surge (BS)
**Definition:** Price breaks decisively through an IP zone, then surges directionally toward the next IP zone or Structural Extreme Magnet. Breakout confirmed by sustained move beyond the zone (15+ minutes).
**IP Zone Signature:** The failing zone has ZFP above 45%, with active breakout pre-conditions.
**Variant — Piercing Breakout Surge (PBS):** A BS so powerful it pierces directly through one or more intermediate IP zones without pausing. Occurs when failing zone ZFP above 70%.

#### 6.1.3 Recovery (R)
**Definition:** Temporary stabilization or mild retracement immediately after a BS or Whiplash. Price consolidates or slowly drifts back toward the prior IP zone level. Recovery is always a TRANSITIONAL shape.
**Variant — Recovery Surge (RS):** Instead of slow consolidation, Recovery takes the form of a sharp directional move back toward pre-breakout level.

#### 6.1.4 Whiplash (WL)
**Definition:** A rapid, violent directional move that immediately reverses — spike-and-reject pattern. Key characteristic is the rejection at the IP zone, not the initial surge.
**Variant — Reverse Whiplash (RWL):** A Whiplash in the opposite direction of the preceding BS. Most common follow-on shape after BS.
**Variant — Piercing Whiplash (PWL):** Initial surge so powerful it pierces through multiple IP zones before rejection.
**Variant — Piercing Reverse Whiplash (PRWL):** Reverse Whiplash with piercing characteristics. Strongest reversal signal in the taxonomy.

#### 6.1.5 Whiplash Storm (WLS)
**Definition:** Extended sequence of rapid, explosive Whiplash moves across multiple sessions. On 4H timeframe, WLS appears as Swing Scalps with dramatically increased volatility.
**IP Zone Signature:** Multiple IP zones of similar pressure degree within a narrow range, price oscillating violently between them.
**Duration:** Typically 2-5 sessions. Almost always resolves into a Breakout Surge.

### 6.2 Shape Classification Decision Matrix

Apply this matrix in SEQUENCE — check the highest-priority condition first. If it matches, assign that shape.

| Priority | Condition (IP Zone Metrics) | Shape | Confidence |
|:---|:---|:---|:---|
| 1 | Price breaks through zone with ZFP > 45% AND confirms 15+ min; Measured Move target exists | BS (or PBS if pierces multiple zones) | HIGH |
| 2 | Price surges to zone with ZFP < 20%, briefly pierces, then rejects; Liquidity Sweep Target identified | WL (or PWL if multiple zones pierced) | HIGH |
| 3 | After BS/WL: price stabilizes at mid-range zone (ZFP 20-40%); duration < 1 session | R (or RS if sharp retracement) | MODERATE |
| 4 | 3+ IP zones in narrow range (0.30-0.50 DXY); price oscillating violently; 4H shows consolidation | WLS (or Minor WLS if 1-2 sessions) | HIGH |
| 5 | Price oscillating between Heavy/Extreme ceiling and floor zones; both ZFP < 30%; duration > 1 session | SS | HIGH |
| 6 | After BS: violent reversal in opposite direction through prior origin; Hard Wall rejection | RWL (or PRWL if piercing) | MODERATE-HIGH |

### 6.3 Observed Macro Shape Chains (by Frequency)

| Chain | Frequency | Description |
|:---|:---|:---|
| SS → BS → R → WL | HIGHEST | Default weekly storyline. SS builds positioning pressure, zone fails, BS, R at mid-range, WL at target. |
| SS → BS | VERY HIGH | Abbreviated default. Week ends before R/WL materialize. |
| BS → R → RWL | HIGH | Week opens with BS. Recovery follows, then RWL rejects. Signals false breakout. |
| BS → RWL → SS → BS | HIGH | Complete false breakout cycle. Second BS often succeeds. |
| WL → RWL → SS → BS | MODERATE | Opening Whiplash reversed, consolidation, then breakout. |
| R → RWL → SS → BS | MODERATE | Recovery from prior week BS reversed, new consolidation and breakout. |
| BS → RWL → PBS | MODERATE | Initial BS reversed, but reversal triggers even more powerful PBS. |
| BS → R → PBS | MODERATE | BS followed by Recovery, then even stronger second leg. |
| SS → BS → SS → BS | MODERATE | Double consolidation-breakout. |
| WLS → BS → WLS | MODERATE | WLS resolves into BS, triggers another WLS. |
| WLS → SS → PBS | MODERATE | WLS exhausts into SS, then Piercing BS breaks out. |
| PBS → R/SS → PRWL → SS | LOW-MOD | PBS reversed by PRWL, then settles. |

### 6.4 Shape Transition Rules

| Current Shape | Next Shape | IP Zone Trigger | Probability |
|:---|:---|:---|:---|
| SS | BS | Bounding zone ZFP > 45% fails with confirmation | HIGH (ZFP > 60%) |
| SS | WLS | 3+ zones in narrow range; volatility triggers amplify | MODERATE |
| BS | R | Price reaches Measured Move target zone (ZFP 20-40%) | HIGH |
| BS | RWL | Price reaches Hard Wall / Institutional Magnet | HIGH (at Hard Walls) |
| BS | PBS | Zone fails with extreme momentum; distant target | MODERATE |
| R | SS | Stabilization persists > 1 session; both bounding zones hold | MODERATE-HIGH |
| R | WL/RWL | Recovery reaches opposing IP zone | MODERATE |
| R | BS (2nd leg) | Recovery at mid-range zone that also fails | MODERATE |
| WL | RWL | Whiplash rejected at zone; opposite momentum builds | MODERATE-HIGH |
| WL | SS | Whiplash exhausts; consolidation near rejection point | MODERATE |
| RWL | SS | Reversal exhausts; new range established | HIGH |
| RWL | BS (new dir) | Reversal breaks through opposing zone | MODERATE |
| WLS | BS | Bounding zone of the storm finally fails | VERY HIGH |
| WLS | SS | Volatility diminishes; oscillation range narrows | MODERATE |

### 6.4.1 ZFP-Conditioned Transition Rules (OPERATOR CORRECTION — CRITICAL)

**This is the most important Engine 2 correction.** Chain sequencing must be conditioned on the TARGET zone's ZFP, not just the current shape. Without this table, the engine incorrectly predicts R or PBS after a BS hits a Hard Wall, when it should predict RWL.

| Current Shape | Target Zone ZFP | Predicted Next Shape | Confidence | Rationale |
|:---|:---|:---|:---|:---|
| BS | < 20% (Hard Wall) | **RWL** (rejection, NOT R/PBS) | HIGH | Zone is a Hard Wall — price WILL be rejected. Do NOT predict continuation. |
| BS | 20–40% (Mid-range) | **R** (stabilization) | HIGH | Zone has moderate strength — price will pause but not necessarily reject hard. |
| BS | > 60% (Very weak zone) | **PBS** (cascade continues) | MODERATE | Zone is failing — price will punch through to next zone. |
| BS | > 80% (Nearly broken) | **PBS** (strong cascade) | HIGH | Zone is effectively broken — continuation with momentum. |
| SS | > 45% (bounding zone failing) | **BS** (breakout imminent) | HIGH | One side of the range is failing — breakout is next. |
| SS | All < 30% (both sides hold) | **SS continues** | HIGH | Both bounding zones are solid — consolidation continues. |
| WLS | Any (bounding zone fails) | **BS** | VERY HIGH | WLS almost always resolves into BS — the only question is direction. |
| R | Persists > 1 full session | **SS** (reclassify, NOT continue R) | MODERATE-HIGH | If stabilization persists, it IS consolidation now. Reclassify to SS and map swing scalps. |
| R | < 1 session, opposing zone near | **WL or RWL** | MODERATE | Brief pause then rejection at opposing zone. |
| WL | Rejection momentum builds in opposite dir | **RWL** | MODERATE-HIGH | Whiplash rejection is the entry for reverse move. |
| WL | No opposite momentum | **SS** (consolidation) | MODERATE | Whiplash exhausts into range. |

**CRITICAL MISTAKE TO AVOID:** When a BS reaches a Hard Wall (ZFP < 20%, confluence ≥ 8), the engine MUST predict RWL, NOT R or PBS. This was the #1 Engine 2 error that caused the April 20-24 misprediction — the engine predicted upside continuation when a Hard Wall sat directly above. The ZFP of the TARGET zone determines the next shape, not the momentum of the current move.

### 6.4.2 HTF Zone Mechanics Decision Tree (v5.3.0 — CRITICAL — From Trading Laws)

When a MoM zone is tested during the shape chain, the reaction determines the subsequent shape. This decision tree BRIDGES Engine 1 (zone classification) with Engine 2 (shape prediction):

```
MoM zone tested (unmitigated):
  ├── SHARP WHIPLASH/REVERSAL instantly
  │   └── All liquidity drained at this level
  │   └── Zone is PIERCED
  │   └── Next shape: BS or WL in OPPOSITE direction
  │
  ├── MINOR REACTION + retest, zone HOLDS
  │   └── Zone absorbs the test
  │   └── Long Consolidation begins (2-4 days)
  │   └── Next shape: SS (Swing Scalps)
  │   └── Map swing scalp setups within consolidation range
  │
  ├── Zone BREAKS but price RETURNS
  │   └── Short Consolidation
  │   └── Next shape: SS → BS or SS → WL
  │   └── Transition setup: entry on the break of consolidation
  │
  └── NO PIERCE or sharp whiplash
      └── Slow Consolidation around POI (2-4 days)
      └── Consolidation ends in price retesting opposing liquidity
      └── Then pierce through zone until reaching BoM Liquidity
      └── Next shape: SS → BS (breakout to BoM target)
```

**Application in Shape Chain:** When Engine 2 predicts a shape that involves price reaching a MoM zone, apply this decision tree to determine the NEXT shape. The zone's reaction count (from Engine 1 Zone Reaction Counter) helps predict which branch activates:
- 0 reactions (virgin): Most likely MINOR REACTION branch (first test causes reaction but zone holds initially)
- 1-2 reactions (active): Could be any branch — assess surrounding liquidity
- 3+ reactions (depleted): Most likely PIERCED branch (zone fails)

**For BoM zones:** BoM zones are NOT subject to this decision tree — they ALWAYS react (100% guarantee if unmitigated). A BoM zone reaction produces a directional move (BS, WL, or RWL) determined by the Direction Validation 6-check.

### 6.5 IP Zone Anchoring Rules by Shape

| Shape | IP Zone Role | Engine 1 Metrics Required |
|:---|:---|:---|
| SS | Ceiling and Floor zones define the range | Both bounding zones: ZFP < 30%, Confluence ≥ 6 |
| BS | Failing zone triggers BS; target zone determines magnitude | Failing zone: ZFP > 45%. Target: Measured Move |
| R | Mid-range zone provides temporary friction | Recovery zone: ZFP 20-40%, typically Post-Expiry Ghost |
| WL/RWL | Hard Wall or Institutional Magnet rejects the move | Rejection zone: ZFP < 20%, Confluence ≥ 8, LSZ |
| WLS | Cluster of 3+ zones creates oscillation cage | 3+ IP zones within 0.30-0.50 DXY, each ZFP 15-40% |
| PBS | Multiple intermediate zones fail; distant target | All intermediate zones: ZFP > 50%. Target: deep Structural Extreme |
| PRWL | Institutional Magnet at depth of reversal provides rejection anchor | Rejection at deep Institutional Magnet or Confluent Floor/Ceiling |

### 6.6 Forward Mapping Procedure (MANDATORY — Execute After Engine 1 Completes)

**Step 1: Current Shape Identification.** Using the IP zone map from Engine 1, identify the current macro shape by applying the Shape Classification Decision Matrix (Section 6.2). Determine which shape best describes the current price-zone relationship. State the current shape, the IP zone anchoring it, and the ZFP of the anchoring zone.

**Step 2: Transition Probability Assessment.** From the current shape, apply the Shape Transition Rules (Section 6.4) and ZFP-Conditioned Transition Rules (Section 6.4.1) to determine the most probable next shape. Assign confidence based on the transition probability and ZFP conditioning. If the current shape is SS, also assess consolidation phase (Section 6.8 Consolidation Phase Detection).

**Step 3: Chain Extension with Audit Trail.** Extend the shape chain forward, shape by shape, through the trading week. For each extension: document (a) current shape, (b) the IP zone trigger, (c) the transition conditions (ZFP value), (d) predicted next shape, (e) confidence level. Maximum chain length: 5 shapes. Terminate if cumulative confidence drops below 25%. Format: `Shape A → [Trigger: zone name, ZFP X%] → Shape B → [Trigger: ...] → Shape C [confidence: Y%]`

**Step 4: Alternative Chain Analysis.** For every primary chain, construct at least one alternative chain that activates if the primary fails at a specific Decision Zone. The Decision Zone is the IP zone whose ZFP determines which chain activates. Document: (a) the Decision Zone, (b) the ZFP threshold that triggers the alternative, (c) the alternative chain, (d) alternative chain confidence. Format: `PRIMARY: A→B→C | DECISION ZONE: [zone] ZFP > [threshold]% → ALTERNATIVE: A→X→Y`

**Step 5: Session/Day-Level Decomposition.** Decompose the weekly chain into day-by-day predictions. For each day (Mon-Fri): (a) assign the predicted shape, (b) assign the directional bias (up/down/range), (c) identify the key IP zone for that day, (d) note any volatility triggers (auctions, expiries, economic events), (e) state confidence. Format: `Mon: [SHAPE] [direction] | Key Zone: [name] | Triggers: [list] | Confidence: X%`

**v5.0.0 ADDITION — Pair Translation of Weekly Shape Chain Visualization:**

The weekly shape chain visualization at the end of Section 6.6 Step 5 must be reproduced for each pair with inverted direction:

```
DXY Weekly Shape Chain:
Mon: [SHAPE] [direction: up/down/range] → Tue: [SHAPE] [direction] → ... → Fri: [SHAPE] [direction]

EUR/USD Weekly Shape Chain (translated):
Mon: [SAME SHAPE] [direction: INVERTED] → Tue: [SAME SHAPE] [direction: INVERTED] → ... → Fri: [SAME SHAPE] [direction: INVERTED]

GBP/USD Weekly Shape Chain (translated):
[Same format — same shapes, inverted direction]

AUD/USD Weekly Shape Chain (translated):
[Same format — same shapes, inverted direction]
```

**CRITICAL:** The SHAPES are the same — only the DIRECTION is inverted. SS remains SS, BS remains BS, WL remains WL. What changes is the direction of each move: DXY up = pair down, DXY down = pair up. This is the directional conviction principle from Part IX Section 9.2.

### 6.7 Engine 2 Zero-Tolerance Rules

**RULE 1:** No Shape Without IP Zone Anchoring. Every shape prediction must be anchored to at least one specific IP zone.
**RULE 2:** No Chain Without Audit Trail. Every chain extension must document current shape, trigger, conditions, prediction, confidence.
**RULE 3:** Temporal Boundary Inheritance. All IP zone data must be pre-week data.
**RULE 4:** No Behavioral Generalizations. Shape durations and probabilities must be derived from backtested data or specific IP zone metrics.
**RULE 5:** Mandatory Alternative Chain. Every primary chain must include at least one alternative chain with a Chain Branch Point.
**RULE 6:** No Chain Extension Beyond Moderate Confidence. Terminate chain if cumulative confidence drops below 25%.
**RULE 7:** WLS Resolution Direction Must Be Justified with specific bounding zone identification.
**RULE 8:** No Fabricated Trade Setups. Every setup must reference specific IP zones with ZFP values.
**RULE 9:** No Session Predictions Without Catalyst Identification.

### 6.8 Shape-to-Zone Classification Quick Reference

| Shape | Zone Type at Entry | Zone Type at Target | Key ZFP Range | Expected Duration |
|:---|:---|:---|:---|:---|
| SS | Both bounding zones ZFP < 30% | N/A (range-bound) | Ceiling < 30%, Floor < 30% | 2-5 sessions |
| BS (up) | Resistance zone ZFP > 45% | Next Resistance or Structural Extreme | Source > 45% | 1-3 sessions |
| BS (down) | Support zone ZFP > 45% | Next Support or Structural Extreme | Source > 45% | 1-3 sessions |
| PBS | Multiple zones ZFP > 50% | Deep Structural Extreme | All intermediate > 50% | 1-2 sessions |
| WL | Zone ZFP < 20% (Hard Wall) | Origin zone (return) | Rejection zone < 20% | < 1 session |
| RWL | Hard Wall or Institutional Magnet | Prior origin | Rejection zone < 15% | < 1 session |
| WLS | 3+ zones ZFP 15-40% each | BS resolution target | Cluster 15-40% | 2-5 sessions |
| R | Mid-range zone ZFP 20-40% | N/A (transitional) | 20-40% | < 1 session |
| RS | Opposing zone with momentum | Prior extreme | Variable | < 1 session |


### Consolidation Phase Detection (NEW — CRITICAL for Swing Scalp Mapping)

For each SS/WLS/R shape identified by Engine 2, classify the **consolidation phase** to determine which setup types are valid:

| Phase | Condition | Valid Setup Types | Timeframe Stack |
|:---|:---|:---|:---|
| Early consolidation | SS/WLS just started (< 1 session) | Swing Scalps (both directions) | Scalp Stack (30m/15m/5m) |
| Mid consolidation | SS/WLS ongoing (1-3 sessions) | Swing Scalps + Double Whiplash Inverse | Scalp Stack |
| Late consolidation (near HTF zone) | ZFP trending up on bounding zone | Swing Scalps + BS Transition Entry | Both Stacks |
| Post-BS (early breakout) | BS confirmed, move in progress | Reinforcement entries only | Swing Stack |
| Post-BS (recovery) | BS complete, price recovering | Whiplash/Recovery Surge entries | Swing Stack |
| Mid-breakout | Directional move in progress | Reinforcement entries at liquidity zones | Swing Stack |

**Key rule**: "If not right near a strong 4H pressure zone right now — BS is most likely days away. This is swing scalp valley — milk the cow on the 15m timeframe."

### 4H MoM One-and-Done Rule (NEW — Engine 2 Correction)

4H MoM zones are "one and done": if 100% unmitigated, there WILL be a reaction on the first retest, but often it is a minor reaction followed by a strong pierce. Do NOT enter for swing at 4H MoM zones — scalp only at most. If a counter-trend reaction is happening from a 4H MoM zone, expect the zone to pierce after the minor bounce. This directly affects Engine 2 shape prediction at 4H MoM zones: the expected shape after touching a 4H MoM is a minor WL followed by BS/PBS through the zone.

### Timeframe Element Matching (NEW — Shapes at Cross-TF Zones)

Each timeframe's liquidity is its own element. Moves originating from a specific TF's zone tend to target the same TF's zone on the other side:
- **4H source → 4H target** (1H acceptable as similar element — they react interchangeably with 4H being dominant)
- **1H source → 1H target** (30m acceptable)
- **30m source → 30m target** (15m acceptable)
- **15m source → 30m or 1H target** (up to 2 TF dimensions higher, not more)
- **5m source → 15m or 30m target** (up to 2 TF dimensions higher)

This refines TP targeting: a breakout that originates on 15m liquidity should NOT target a 4H zone — it will likely be absorbed before reaching it. Target the same element (30m or 1H at most).

### Pressure Reading Rules (NEW — Engine 2 Directional Bias)

When directional bias is unclear during consolidation:
- **Candle size = pressure direction**: Look at which candles are obviously bigger. That is where pressure is building.
- **Wick direction = pressure direction**: Upper wicks = buying pressure. Lower wicks = selling pressure.
- **Triangle shapes**: The flat side is receiving pressure. The sharp side is applying pressure.
- **4H storyline tiebreaker**: When in doubt, the 4H storyline bias decides. The weekly trend is identified on the 4H — it takes days and weeks to complete.

### 6.9 Engine 2 Output Format (Report Section 17)

**v5.3.3 — COMPLETE FORMAT (replaces "[unchanged from v4.5.2]" placeholder):**

Engine 2 output is Section 17 of the report and MUST include all of the following components:

```
═══════════════════════════════════════════════════════════════
ENGINE 2 — MACRO SHAPE CHAIN MAP | WEEK OF [DATE]
Primary Timeframe: 1H | Structural Validation: 4H
═══════════════════════════════════════════════════════════════

─── CURRENT SHAPE IDENTIFICATION ───
Current Shape: [SS/BS/WL/R/WLS] | Anchoring Zone: [name] | ZFP: [X%]
1H Structure: [description of current 1H price-zone relationship]
4H Structural Validation: [confirms/rejects 1H classification]

─── PRIMARY SHAPE CHAIN (with Audit Trail) ───
Shape A → [Trigger: zone name, ZFP X%] → Shape B → [Trigger: zone name, ZFP X%] → Shape C [cumulative confidence: Y%]
[Maximum chain length: 5 shapes. Terminate if cumulative confidence < 25%.]

─── ALTERNATIVE CHAIN ───
PRIMARY: A→B→C | DECISION ZONE: [zone] ZFP > [threshold]% → ALTERNATIVE: A→X→Y [confidence: Z%]

─── ZFP-CONDITIONED TRANSITIONS (from Section 6.4.1) ───
For each chain extension, document the ZFP conditioning:
BS → [target zone ZFP X%] → [predicted next shape per Section 6.4.1 table]

─── DAY-BY-DAY DECOMPOSITION (v5.3.3 — CRITICAL — Feeds Engine 3 Day Bridge) ───
Mon: [SHAPE] [direction: up/down/range] | Key Zone: [name] | Triggers: [expiries/auctions/events] | Confidence: X%
Tue: [SHAPE] [direction] | Key Zone: [name] | Triggers: [list] | Confidence: X%
Wed: [SHAPE] [direction] | Key Zone: [name] | Triggers: [list] | Confidence: X%
Thu: [SHAPE] [direction] | Key Zone: [name] | Triggers: [list] | Confidence: X%
Fri: [SHAPE] [direction] | Key Zone: [name] | Triggers: [list] | Confidence: X%

─── CONSOLIDATION PHASE DETECTION (if SS/WLS/R predicted) ───
Phase: [Early/Mid/Late] | Bounding Zones: Ceiling=[name, ZFP X%], Floor=[name, ZFP Y%]
Valid Setup Types: [Swing Scalps / Swing Scalps + DWL Inverse / Swing Scalps + BS Transition]
ZFP Trend on Bounding Zone: [rising/stable/falling] — [breakout imminent / consolidation continues]

─── TRADING SPEED ADJUSTMENT (Section 6.10) ───
Raw timing: [day predictions before speed adjustment]
Adjusted timing: [day predictions after +1 day speed adjustment]
"Today's move" = tomorrow's move. 4H moves take 2x as long as expected.

─── WEEKLY SHAPE CHAIN VISUALIZATION ───
DXY: Mon: [SHAPE] [dir] → Tue: [SHAPE] [dir] → Wed: [SHAPE] [dir] → Thu: [SHAPE] [dir] → Fri: [SHAPE] [dir]

EUR/USD (translated): Mon: [SAME SHAPE] [INVERTED dir] → ... → Fri: [SAME SHAPE] [INVERTED dir]
GBP/USD (translated): Mon: [SAME SHAPE] [INVERTED dir] → ... → Fri: [SAME SHAPE] [INVERTED dir]
AUD/USD (translated): Mon: [SAME SHAPE] [INVERTED dir] → ... → Fri: [SAME SHAPE] [INVERTED dir]
═══════════════════════════════════════════════════════════════
```

**CRITICAL**: The Day-by-Day Decomposition section is the DIRECT INPUT to Engine 3's Day-Level Bridge (Section 8.0.2). If this section is missing or incomplete, Engine 3 CANNOT assign DAY labels to trade setups, making the entire report non-executable.

### 6.10 Trading Speed Rule (v5.3.0 — HIGH — From Trading Laws)

**"Assume price moves at 30-50% of the speed you think it will."**

This rule affects every aspect of the shape chain and reinforcement architecture:

1. **Shape chain timing**: "Today's move" often ends up being TOMORROW's move. TODAY'S move is the journey TO what you thought "today's move" will be. When predicting day-level shape assignments, add 1 day to expected timing.

2. **4H move duration**: "The move that I see on the 4H chart — expect it to take twice as long as I think it will." A 4H breakout that appears imminent may take 2-3 more 4H candles to complete than initially predicted.

3. **Reinforcement rocket spacing**: Because price moves slower than expected, reinforcement rockets should be spaced further apart to avoid clustering. If rockets are too close together, they all trigger at once (good for position building but bad for risk management if the move stalls).

4. **AUD/USD specific**: "Molasses. Expect 2-4 days before HTF move completes." AU is the slowest pair — plan accordingly.

5. **Consolidation duration**: "If the price does not pierce or sharply whiplash upon testing the zone, expect a slow consolidation around this POI for 2-4 days." Consolidation lasts longer than expected.

---

