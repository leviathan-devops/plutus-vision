# E1_V452_FILL — the text behind the seven "[unchanged from v4.5.2]" placeholders of Engine 1

Companion to `E1_ALGO.md`. Fills its section 0.3 / section 11 UNKNOWNs from the predecessor prompts. Nothing here is invented: every rule is quoted or closely paraphrased with a line citation. Anything that is an arithmetic or mirror-image consequence is labelled **Derived**. Where the predecessors are also silent the entry says **STILL UNKNOWN**.

**Citation convention**

| Tag | File | Lines read |
|:---|:---|:---|
| `V452:n` | `/home/user/handover-branch/Original_Canon_Data/TTE System Prompts/Trident_Trading_Engine_System_Prompt_v4.5.2 (1).md` (2430 lines) | in full: 1-165, 250-1260, 1436-1465, 1500-1598, 1736-1750, 1945-2018, 2326-2430; grep over the rest |
| `SP:n` | `/home/user/plutus-vision/canon/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md` | 1396-1523 + line-diff of Protocol B against V452 |
| `L44:n` | `.../LTE System Prompts/Leviathan_Quant_System_Prompt_v4.4_GLM.md` | line-diff of 521-900 against V452:785-1256 |
| `L42H:n` | `.../LTE System Prompts/Leviathan_Quant_Full_Handover_v4.2.md` | 70-80, 118-134, 705-740 |
| `V500` / `V510` / `V520` | `.../TTE System Prompts/Trident_Trading_Engine_System_Prompt_v5.0.0.md`, `..._v5.1.0.md`, `Trident_System_Prompt_v5.2.0.md` | placeholder scan + diff of Synthesis and Pillar 8 blocks |

**Chain result.** v4.5.2 is the end of the chain: it contains the real text for every block and has zero "[unchanged from ...]" placeholders. v5.0.0, v5.1.0 and v5.2.0 carry the *same* placeholders as v5.3.3 (V500:642/872/876/880/897/903/909/928, V510:679/909/913/917/934/940/946/965, V520:873/1103/1107/1111/1128/1134/1140/1159), so they add nothing. Leviathan v4.4 GLM has Pillar 5 Steps 1-5 and Pillars 6, 7, 9 word-for-word identical to v4.5.2 (diff empty for those blocks); it differs only in the Pillar 8 tier table, the breakout-alert trade block, the "Decision Zone" label and the absence of Steps 9.5 / 9.7. Steps 0f / 0g / 0h do not exist before v4.5.x. `Leviathan_Quant_System_Prompt_v4.5.docx` is a 27 KB change-request note, not a prompt; it contains none of the pillar procedures.

**Units.** v4.5.2 is DXY-only: "EU/GU pair-specific logic will be added in future iterations but is NOT active in v4.5.2." (V452:81). Every number below is in DXY points; "pips" in a DXY context means 0.01.

---

## 0. Pillar 5 step order (answers "any step numbering between them")

Order in v4.5.2: Step 0 (0a-0e) V452:531 → Step 0.45 (0.45a-0.45e) V452:566 → Step 0.5 (0.5a-0.5d) V452:611 → Step 0f V452:637 → **Step 0g** V452:749 → **Step 0h** V452:767 → **Steps 1-5** V452:785 → Pillar 6 V452:835. There is no step between 0h and Step 1, and none between Step 5 and Pillar 6.
v5.3.3 inserts three v5.0.0 steps around them: Step 0.45a (LSZ extension, SP:1284-1286) and Step 0.6 (intra-zone scan, SP:1312) before 0f; Step 5.5 (Key Support Band tightening, SP:1411) after Step 5. v4.5.2 says "TWO mandatory pre-computation steps (Step 0 and Step 0.5)" (V452:519).

---

## 1. Pillar 5 — Steps 0g, 0h, 1-5

### 1.1 Step 0g — 1H Precision Anchor Scan (CONDITIONAL) — V452:749-763

- "1H zones are NOT standalone indicators. They serve two specific purposes only. **FORBIDDEN: Presenting a standalone 1H zone as an IP level.** A single London session can create a 1H "demand zone" that means nothing by NY open." (V452:751)
- **Condition A — Nested Precision** (V452:753): "A 1H demand zone that sits INSIDE a 4H or D1 zone refines the zone boundaries. The 4H zone defines the institutional zone; the 1H zone identifies the exact floor/ceiling within it. Both zones are retained — 4H as primary boundary, 1H as nested precision anchor. Criteria: 2-3 candle base on 1H preceding >= 0.3 DXY move lasting >= 1 trading day."
- **Condition B — Gap-Fill Only** (V452:755): "If a 0.20+ DXY gap exists between mapped zones and no 4H/D1 level fills it, a 1H zone from the prior week may be included as a MINOR REACTION LEVEL with Confidence: MODERATE. Tag as "Gap-Fill Anchor.""
- "**EXCLUDED:** 1H zones that do NOT meet Condition A or B. The false positive rate is too high." (V452:757)
- Output strings (V452:761-762): `"1H Precision Floor [97.72-97.78] nested inside 4H BoM Demand [97.65-97.95]"` / `"1H Gap-Fill Anchor [98.24-98.27] in unfilled gap [98.20-98.30]"`.
- Downstream: zone-map row field "Nested 1H Precision: [range or "none"]" (V452:1242); gap-scan candidate "1H demand/supply zone from prior 1-2 weeks IF inside a 4H/D1 zone (from Step 0g Condition A) or filling the gap (Condition B)" (V452:1167).

Code-ready constants: 1H base = 2-3 candles; move after base ≥ 0.30 DXY lasting ≥ 1 trading day; gap threshold ≥ 0.20; lookback "prior week" (0g) / "prior 1-2 weeks" (9.5b).
Gaps in the text: Condition A is written for demand only (supply is the mirror — **Derived**; the output example says "Floor", and the row field is direction-neutral). The 1H zone's [low, high] construction (which of the 2-3 base candles) is **STILL UNKNOWN**; a score for a 1H anchor is not stated (v5.3.3 Step 0.6 gives intra-zone levels Structural = 0.5, SP:1333).

### 1.2 Step 0h — Minor Swing Level Identification (MANDATORY) — V452:767-781

- "Relaxed criteria for swing levels that did not meet Step 0 thresholds. These fill gaps between major zones and create reaction points." (V452:769)
- 0h-a "Scan D1 and 4H data for swing lows/highs with:" (V452:771-774)
  - "Rejection wick >= 0.08 DXY points (reduced from 0.15)"
  - "Close in upper/lower 40% of range (reduced from 50%)"
  - "OR: Clear 1H/4H demand/supply zone reaction at this level"
- 0h-b "Tag each as "Minor Swing Level" with:" exact price, date, timeframe (D1 or 4H); "Why it did not meet Step 0 criteria (e.g., "wick 0.12, close 47th%")"; "Whether price subsequently reacted at this level" (V452:776-779)
- 0h-c "**Scoring:** Minor Swing Levels receive Structural dimension score = 0.5 (half the weight of full swing extremes, but still included in map)." (V452:781)

Code-ready constants: wick ≥ 0.08; close-position number 40 (was 50); timeframes D1 **and 4H** (Step 0 is D1 only); applies to bars that failed Step 0 (wick ≥ 0.15 and close in upper/lower 50%, V452:541/548). With `close_pos = (C-L)/(H-L)` the close test has two readings:
- Reading R (relaxed threshold): swing low needs `close_pos >= 0.40`, swing high needs `close_pos <= 0.60`.
- Reading L (literal "upper/lower 40%"): swing low needs `close_pos >= 0.60`, swing high needs `close_pos <= 0.40`.

Text evidence: the step is titled "Relaxed criteria" (V452:769); the number is "(reduced from 50%)" in parallel with the wick "(reduced from 0.15)" (V452:772-773); the example of a bar that failed Step 0 and belongs here is "wick 0.12, close 47th%" (V452:778) — that bar passes under R and fails under L. Reading L would make 0h stricter than Step 0, which contradicts "relaxed". The sentence itself still says "upper/lower 40%". **AMBIGUOUS wording (V452:773 vs V452:769/778); R is the reading consistent with the step's own example. Operator confirmation needed before coding.**
The alternative criterion ("Clear 1H/4H demand/supply zone reaction at this level") has no numeric definition — **STILL UNKNOWN**.

### 1.3 Steps 1-5 — Price anchors, HWC/LWC, recapture, structural extreme memory, scoring — V452:785-831

**Step 1 — "Extract price anchors:"** (V452:787-791)
- "Prior daily close (each of the last 3-5 trading days)"
- "**Prior daily high/low for EACH of the last 5 trading days** (not just the last trading day — each day's H/L reveals potential levels that may be missed by weekly pivots alone)"
- "Prior weekly close"
- "Prior weekly high/low"
- Cross-reference: gap scan uses "Extended daily close from 6-10 days ago (beyond the 5-day window from Step 1)" (V452:1172) — so the Step 1 close window is treated as 5 days.

**Step 2 — "Extract HWC/LWC from forex.com research (if accessible):"** (V452:793-796)
- "**High-Week Close (HWC): The highest weekly close in a given period**"
- "**Low-Week Close (LWC): The lowest weekly close in a given period**"
- "Multi-year confluences (HWC from one year overlapping with LWC from another) are the most powerful structural levels"
- Worked example of the "period": "forex.com 99.49 KEY resistance (2026 HWC + 2024 LWC confluence) mapped the ceiling zone" (L42H:717) — period = calendar year in the only example.
- Source row: "forex.com Institutional Research ... Weekly DXY forecast with HWC/LWC levels" (V452:135).
- **Derived:** HWC/LWC are computable from the instrument's own weekly closes (max / min weekly close per calendar year). Canon harvests them instead of computing them; the overlap tolerance for a "multi-year confluence" is **STILL UNKNOWN**.

**Step 3 — "Detect recapture phenomenon:"** "If price recently crossed EMA 200 or another major MA, the recapture level is a KEY anchor." (V452:798). "Recently" is defined in Pillar 2: "within 3 sessions ... crossed above a major MA (50, 100, 200)" → RECAPTURE ZONE, "+2 bonus to confluence score" (V452:419). Step 3 says "crossed" (either direction); Pillar 2 says "crossed above".

**Step 4 — STRUCTURAL EXTREME MEMORY** (V452:800-821). "The AI MUST search for and recall major structural extremes beyond the 90-day scan. These are macro-scale events ... that may not show up as swing lows/highs but still create lasting institutional memory".
- 4a web searches "in the past 6-12 months": `"DXY dollar index major events [year]"`, `"dollar index tariff [year]"`, `"DXY structural break [year]"` (V452:802-807).
- 4b categories (V452:810-817):

| Category | Examples | DXY Impact | Duration |
|:---|:---|:---|:---|
| Trade policy shocks | Tariff announcements, trade deal breakdowns | 5+ points | Months |
| Central bank interventions | BoJ at USD/JPY 160, SNB floor removal | 1-3 points | Weeks-Months |
| Major data surprises | CPI >0.5% deviation, NFP >100K miss | 0.5-2 points | Days-Weeks |
| Technical structural breaks | EMA 200 crossovers, multi-month highs/lows | 0.5-1 point | Weeks |
| Prior year extremes | 2022 high 114.78, 2021 low 89.20 | Creates magnet levels | Years |
| Option expiry ghosts | Levels where massive options expired in prior weeks | 0.2-0.5 points | Days-Weeks |

- 4c "When a predicted IL level coincides with a structural extreme from Step 0, Step 0.5, OR this macro scan, upgrade its Structural dimension score and add the appropriate flag." (V452:819)
- 4d "If the current DXY range includes a level that was a major structural extreme, the AI MUST proactively mention this in the analysis" (V452:821)
- OHLC-only: rows "Technical structural breaks" and "Prior year extremes" are computable; the rest are web-search inputs.

**Step 5 — SCORING** (V452:823-831)
- "Exact anchor match = 2 pts (Structural dimension)"
- "Proximity to anchor = 1 pt (Structural dimension)"
- "Structural Extreme from Step 0 (Liquidity Sweep Target or Supply Ceiling Target) = +1 bonus"
- "Repeated Extreme Magnet from Step 0.5 = +1.5 bonus (2 dates) or +2.0 bonus (3+ dates / Role Reversal)"
- "Confluent Floor/Ceiling (Step 0e: swing extreme inside order block) = +2.0 bonus"
- "Institutional Magnet (Step 0.5d: Repeated Magnet inside Order Block) = +2.0 bonus (maximum)"
- "**Maximum Structural Extreme Bonus:** +2.0 (cannot exceed this regardless of how many flags apply)"
- "**Maximum total Structural dimension score:** 2 (base) + 2 (extreme bonus) = 4 pts"
- Numeric tolerance for "exact" vs "proximity" is not given in Pillar 5 — **STILL UNKNOWN** (Technical uses 3 / 10 pips, V452:1083; Fib uses 5 pips, V452:862; Dynamic Discovery uses "within 5 pips", V452:1230).

---

## 2. Pillar 6 — Fibonacci Retracement & Round Number Grid — V452:835-862

"Fibonacci retracements from prior week range + psychological round numbers. Independently captures 3-4/11 levels." (V452:837). "**Data Source:** Calculated from prior week OHLC (same data as Pillar 1) + extended swing point data." (V452:839)

**Step 1 — prior-week retracements** (V452:843-849), H and L = prior week high / low:
```
Fib_23.6% = H - 0.236 × (H - L)
Fib_38.2% = H - 0.382 × (H - L)
Fib_50.0% = H - 0.500 × (H - L)
Fib_61.8% = H - 0.618 × (H - L)
```
**Exact ratio list = {0.236, 0.382, 0.500, 0.618}, all measured DOWN from H.** No 0.786, no 0.705, no extensions.

**Step 2 — major-swing retracements** (V452:851): "Calculate Fibonacci retracements from major swing points (identify the most recent significant swing high and swing low on the daily/4H chart, even if they are 2-4 months old). Use extended historical data from Pillar 1." Same four ratios implied (no other list given). "Significant" has no numeric definition — **STILL UNKNOWN**. Audit: "Fibonacci levels: Show the swing high, swing low, and the retracement percentage" (V452:51).

**Extensions.** Pillar 6 has none. The only extension ratios in v4.5.2 are outside Engine 1: "Master Structural Targets: 1.618 extensions" in the 4D stack (V452:88) and the Engine 3 wormhole pairs "0.382 retracement → 1.382 extension", "0.618 retracement → 1.618 extension" (V452:2080-2081).

**Step 3 — round numbers** (V452:853): "Identify round number levels: .00 (big figure), .50 (half figure), .25/.75 (quarter figure)." Grid step 0.25 DXY.

**Step 4 — round number confluence bonus** (V452:855-860):

| Level Type | Examples | Bonus |
|:---|:---|:---|
| Major Big Figure | 99.00, 100.00 | +2 (Psychological dimension) |
| Half Big Figure | 99.50, 100.50 | +1.5 |
| Quarter Figure | 99.25, 99.75 | +1 |

**Step 5 — scoring** (V452:862): "Fib match within 5 pips + round number = 2 pts (Technical + Psychological); Fib match only = 1 pt (Technical)." 5 pips = 0.05 DXY.

CONFLICT (inside v4.5.2, carried into v5.3.3): Pillar 6 gives a half figure +1.5; the Synthesis Psychological row gives ".00, .50" = 2 points and ".25, .75" = 1 point (V452:1087 = SP:1473). The Psychological dimension is capped at 2 either way.
What a fib is "matched" against is not stated (same gap as pivots, see section 7 row 6).

---

## 3. Pillar 7 — Derivatives Arena Boundary Definition — V452:866-886

- "Defines the WIDE pressure arena within which Pillars 1-6 and 8 provide precision levels. Does NOT provide individual levels — only macro-zone context." (V452:868)
- "**Data Source:** Attempt ICE DXY Options + CME QuikStrike (unstable)." (V452:870)
- Step 1: attempt `https://www.theice.com/products/1216/US-Dollar-Index-Options` (V452:874-877). Step 2: attempt `https://www.cmegroup.com/markets/fx/g10/us-dollar-index.quikstrike.html` (V452:879-882). Both listed UNSTABLE (V452:137-138).
- Step 3 (V452:884): "**If DX options OI data IS accessible:** Overlay as ALL-DAY MACRO TARGETS on the zone map. Top 3 Put OI + Top 3 Call OI strikes."
- Step 4 fallback (V452:886): "**If ALL supplementary DX options sources fail:** The 9-Pillar system operates independently. Mark supplementary DX OI as `[NO DATA — DX options OI supplementary feed inaccessible; 9-Pillar primary mapping active]`."
- Context: "exchange-traded options OI clusters ... remain structurally **Valid All Day** and act as continuous spatial magnets confirming Fibonacci 1.618 extensions." (V452:95)

That is the whole pillar. The "arena" is defined only as the six strikes (top-3 put OI, top-3 call OI) overlaid on the map. No formula turns them into an upper/lower boundary, no score is attached, and no level is excluded for being outside the arena. **Derived:** with no DX options feed (the OHLC-only case) Pillar 7 contributes nothing and the stated fallback string is logged.

---

## 4. Pillar 8 — EUR/USD Strike-to-DXY Primary Conversion — V452:890-950

Rationale: "EUR/USD option strikes → Delta hedging flows → EUR/USD price pinning → DXY level formation → IL level observation" (V452:896). "Ceteris paribus error is small: Holding other 5 pairs constant introduces only ±0.07-0.14 DXY points of error" (V452:900). Data: "Pillar 3 EUR/USD component pair data (Protocol A + Fed H.10 spot rates)" (V452:902).

Procedure (V452:906-944):
1. "From Pillar 3 output, extract ALL EUR/USD option expiry strikes and notionals. If Pillar 3 has not yet executed, WAIT for it."
2. K factor at current spot of the other five pairs: `K = 50.14348112 × USDJPY^(0.136) × GBPUSD^(-0.119) × USDCAD^(0.091) × USDSEK^(0.042) × USDCHF^(0.036)` (V452:910)
3. Missing H.10 pair → "Apply the H.10 Component Data Fallback Procedure from Pillar 3 Step 3"; "Adjust confidence bands per Pillar 3 Step 3c rules" (+0.03 for 1 supplementary pair, +0.07 for 2, 3+ → "Pillar 8 confidence degrades to LOW", V452:449-451); K audit string `"K=[value] | USDJPY=[value](H.10) GBPUSD=[value](supplementary:[URL]) ... | Confidence band: ±[X] DXY"` (V452:915-919).
4. "For each EUR/USD expiry strike with notional >= 500M EUR, calculate DXY equivalent: `DXY_level = K × EURUSD_strike^(-0.576)`"; audit `"EUR/USD [strike] × [notional] → DXY [level] | K=[value] | Formula: K × strike^(-0.576)"` (V452:921-925). **Floor superseded by v5.3.3 ($850M).**
5. Confidence weighting by notional (V452:929-934) — **v4.5.2 four-tier table, SUPERSEDED by v5.3.3 SP:1445-1447**:

| EUR/USD Expiry Notional | Tier | Options-Derived Score | Confidence Band | Description |
|:---|:---|:---|:---|:---|
| >= 1.0B EUR | 1 | 2 | ±0.07 DXY | CRITICAL — High confidence |
| 900M - 1.0B EUR | 2 | 2 | ±0.10 DXY | SIGNIFICANT — Moderate-high confidence |
| 500M - 900M EUR | 3 | 1 (if override) | ±0.15 DXY | CONDITIONAL — Only with structural override |
| < 500M EUR | 4 | 0 (use Pillar 3 only) | N/A | EXCLUDED — Insufficient magnet effect |

   Override (V452:936): "Tier 3 may be included if the converted DXY level coincides with a Pillar 5 Step 0/0.5 verified reaction level OR has 3+ pillar confluence. Tier 4 may be included ONLY if 3+ pillars confirm AND the level was validated as a price reaction in the prior 90 days."
   **Effective table to implement (v5.3.3 bands + v4.5.2 score column, Derived merge):** ≥ 1.5B → Tier 1, score 2, ±0.07; $850M–$1.499B → Tier 2, score 2 (Pillar 8) — but Synthesis row says 1 (E1_ALGO CONFLICT 4), ±0.10; < $850M → EXCLUDED, score 1 and ±0.15 only if overridden.
6. "When multiple expiries cluster within 10 pips: Aggregate notionals. If total ≥ 2B, treat as single 2B+ expiry." (V452:938). The "2B+" class is a leftover of the v4.4 table ("≥ 2B EUR | 2+ (enhanced) | ±0.05 DXY | Very high confidence", L44:669); v4.5.2 and v5.3.3 tables have no 2B row. 10 pips here = 0.0010 EUR/USD.
7. "When expiries are on different days within the week: Take the UNION of all days' converted strikes. Friday expiries have the strongest weekly effect (they pin price for the entire week leading up to expiry)." (V452:940)
8. "**Fallback behavior:** If EUR/USD has NO expiries >= 500M, Pillar 8 defaults entirely to Pillar 3's multi-pair approach." (V452:942)
9. "Pillar 8 supersedes Pillar 3 for the EUR/USD component. ... When both Pillar 3 and Pillar 8 produce levels for the same DXY range, Pillar 8 takes 70% weight, Pillar 3 takes 30%." (V452:944). What quantity is weighted (level price or score) is not stated — **STILL UNKNOWN**.
- Reverse check (V452:946-950): `EURUSD_strike = (K / DXY_target)^1.7361`; "If the implied strike is within 10 pips of a known EUR/USD option expiry, it confirms the level."
- Appendix A (V452:2330-2366) is identical to v5.3.3 Appendix A (K ≈ 107.6 table, spacing table, reverse formula).

OHLC-only: Pillar 8 needs option notionals and five other spot rates — not computable; Options-Derived = 0.

---

## 5. Pillar 9 — Regime Detection, Zone Failure Prediction & Breakout Magnitude — V452:954-1071

"Detects when the market is in a regime that makes IL zone failures likely, assigns a Zone Failure Probability (0-100%) to each mapped IL zone, AND projects how far a breakout will carry once a zone fails." (V452:956). Data: "Protocol A (option expiry timing), Protocol F (economic calendar), web search for macro catalysts, Pillar 2 (MA momentum), cross-pair analysis from Protocol A, Pillar 5 Step 0/0.5 (Structural Extreme Magnets)." (V452:960)

### 5.1 Step 1 — classify each IL zone by structural strength (V452:964-972)

| Zone Type | Criteria (v4.5.2) | Base Failure Probability |
|:---|:---|:---|
| Hard Wall | Option wall ≥ 1B + 3+ pillar confirmation + Confluent Floor/Ceiling | 5-15% |
| Standard Wall | Option wall ≥ 500M + 2+ pillar confirmation | 15-30% |
| Soft Wall | Small option (<500M) or 1-2 pillar confirmation | 30-50% |
| One-Touch | Only 1 pillar, no option wall | 50-70% |
| Post-Expiry Ghost | The option has expired but structural memory remains | 20-40% |
| Liquidity Sweep Zone | Level at a prior exact swing low from Pillar 5 Step 0 | Special: high probability of brief breach then reversal |

Thresholds superseded by v5.3.3 Appendix B (≥$1.5B / $850M–$1.499B / <$850M, SP:4058-4060); ranges unchanged.
**How the point value inside a range is chosen: STILL UNKNOWN.** No rule in V452, L44, V500, V510, V520 or SP. Only instruction: "Zone Failure Probability: Show the base probability and each modifier applied" (V452:52).

### 5.2 Step 2 — breakout pre-conditions that increase failure probability (V452:974-985)

| Signal | Effect on Failure Probability | Detection Method |
|:---|:---|:---|
| Option expiry timing (10:01 NY Spring Release) | +20-30% near expiry time | Protocol A expiry timestamps |
| Macro catalyst aligned against zone | +15-25% | Protocol F + web search |
| Price approaching with increasing momentum | +10-20% | Rate of change in DXY price |
| Cross-pair confirmation (EUR + GBP both breaking) | +15-25% | Protocol A multi-pair analysis |
| **Volume/momentum divergence** | **+10-15%** | Price testing zone with increasing volume = fail likely |
| Cascade effect (prior zone just broke) | +20-30% | Sequential zone failure detection |
| Regime change (EMA 200 cross) | +15-25% | Pillar 2 recapture detection |
| **Structural Extreme Magnet proximity** | **+10-15%** | If a Repeated Extreme Magnet from Pillar 5 Step 0.5 is within the projected breakout range, institutions will target it |

Eight signals. The two in bold are missing from Appendix B.2 of both v4.5.2 (V452:2385-2392) and v5.3.3 (SP:4067-4074), which list six. The Pillar 9 body is the procedure; Appendix B is titled "QUICK REFERENCE". Numeric definition of "increasing momentum" / "rate of change" and the point value inside each modifier range: **STILL UNKNOWN**. OHLC-computable signals: momentum, cascade, EMA-200 cross, magnet proximity (volume divergence needs volume).

### 5.3 Step 3 — combine (V452:987-994)
```
Base_Probability (from zone type)
+ Signal_1_Modifier (if applicable)
+ Signal_2_Modifier (if applicable)
+ ...
= Final_Zone_Failure_Probability (capped at 95%)
```
**Modifiers ADD (percentage points). Cap = 95%.** No floor, no decreasing modifier, no multiplicative term.

### 5.4 Step 4 — Measured Move Projection, "MANDATORY when ZFP > 45%" (V452:996-1026)
4a consolidation range (V452:1000-1005):
```
Range_Low = Lowest IL level below the failing zone (or the verified floor from Pillar 5 Step 0)
Range_High = The failing zone level
Range_Height = Range_High - Range_Low
```
4b raw measured move (V452:1007-1010):
```
Raw_Target = Range_High + Range_Height
```
4c anchor (V452:1012-1016): "Scan upward (for upside breakout) or downward (for downside breakout) from the raw target"; "Find the nearest Supply Ceiling Target, Repeated High Magnet, or Confluent Ceiling from Pillar 5 Step 0/0.5"; "If a Structural Extreme Magnet exists within ±0.20 DXY of the raw target: The projection target is the Structural Extreme Magnet, NOT the raw target."; "If NO Structural Extreme Magnet exists within ±0.20 DXY of the raw target: Use the raw measured move as the target with reduced confidence (mark as "Unanchored Projection — no structural extreme at target level")."
4d confidence tiers (V452:1018-1024):

| Condition | Confidence | Mark As |
|:---|:---|:---|
| Structural Extreme Magnet within ±0.05 of raw target | VERY HIGH | "Anchored Projection — structural extreme at target" |
| Structural Extreme Magnet within ±0.20 of raw target | HIGH | "Anchored Projection — structural extreme near target" |
| No structural extreme within ±0.20, but round number at target | MODERATE | "Semi-Anchored Projection — round number at target" |
| No structural extreme or round number at target | LOW | "Unanchored Projection — no structural extreme at target" |

4e (V452:1026): "The system is FORBIDDEN from inventing a "likely target" based on behavioral generalizations. Only mathematically derived measured moves cross-referenced with verified historical levels are permitted."
The formulas are written for an upside break of a ceiling only. **Derived mirror for a downside break:** `Range_High = highest IL level above the failing zone (or verified ceiling)`, `Range_Low = failing zone level`, `Raw_Target = Range_Low − Range_Height`, anchors = Liquidity Sweep Target / Repeated Low Magnet / Confluent Floor. "Failing zone level" for a zone that is a range (top, bottom or mid) is **STILL UNKNOWN**. Result names the BREAKOUT EXTENSION TARGET zone (V452:1155).

### 5.5 Step 5 — overall market regime (V452:1028-1034)

| Regime | Criteria | IL Zone Behavior |
|:---|:---|:---|
| Consolidation | Low volatility, no macro catalysts, options cage active | Zones HOLD — trade mean-reversion |
| Momentum | Directional momentum + macro catalyst + options still active | Zones HOLD until catalyst hits, then may fail |
| Breakout | Prior zone just failed + momentum increasing + cross-pair confirmation | Zones FAIL sequentially — trade breakout toward Measured Move target |
| Regime Change | EMA 200 cross + major macro shift + option expiry | Old zones DISSOLVE, new zones form — restructure |

**Four regimes, not three.** The criteria are these word lists and nothing else: no volatility number, no momentum formula. Numeric classifier: **STILL UNKNOWN**. OHLC-observable parts: "low volatility", "directional momentum", "prior zone just failed", "momentum increasing", "EMA 200 cross"; the rest (catalysts, options cage, cross-pair, option expiry) are external.

### 5.6 Step 6 — breakout risk alerts (V452:1036-1064)
"Any zone with Failure Probability > 50% gets flagged as:"
```
⚠ BREAKOUT RISK: [ZONE] at [LEVEL] — Failure Probability: [X]%
Triggers: [list of active signals increasing failure probability]
If breaks: Measured Move Target = [projected level] ([confidence tier])
Structural Anchor: [nearest Pillar 5 Step 0/0.5 extreme, if applicable]

TRADE STRUCTURE:
  Direction: [LONG/SHORT] (if zone fails)
  Entry Trigger: Zone failure confirmation (15+ min sustained break)
  Entry Zone: [level range where breakout entry is placed]
  Stop Loss: [failing zone level — if breakout is real, this level will NOT be retested]
  Take Profit: [Measured Move target or nearest Structural Extreme Magnet]
  R:R: [calculated]
  Scaled Entries: [list up to 3 entry levels within the entry zone]
  Flow Continuity: [what trade follows if this TP is reached]

If zone HOLDS (alternative):
  Direction: [LONG/SHORT] (zone rejection)
  Entry: [zone edge where rejection is expected]
  Stop Loss: [just beyond the zone, above/below the Liquidity Sweep Target]
  Take Profit: [opposite zone boundary or next IP zone]
  R:R: [calculated]
  Flow Continuity: [what trade follows]
```
"**BREAKOUT SWEET SPOT (25-45% ZFP):** When a zone has Failure Probability between 25-45%, this is the "sweet spot" for zone failure that leads to significant breakouts. The report MUST explicitly flag these zones as HIGH-PRIORITY SETUP with a recommended trade structure anchored to that zone" (V452:1064). Not present anywhere in v5.3.3 (grep "sweet spot" = 0 hits).
Thresholds: > 45% → Measured Move; > 50% → BREAKOUT RISK; 25-45% → HIGH-PRIORITY SETUP; zone-failure confirmation = "15+ min sustained break".

### 5.7 Step 7 — Regime/Dynamic dimension score (V452:1066-1071)

| Condition | Score (0-2) |
|:---|:---|
| Zone in consolidation regime, failure prob < 20% | 2 (zone will hold) |
| Zone in momentum regime, failure prob 20-50% | 1 (zone may hold or fail) |
| Zone in breakout/regime change, failure prob > 50% | 0 (zone likely to fail) |

This ties the sixth dimension to numbers: ZFP < 20 → 2, 20-50 → 1, > 50 → 0. The case where regime and ZFP band disagree is not covered.

---

## 6. Synthesis / zone assembly — what v4.5.2 says beyond SP:1496-1520

SP:1496-1505 is a compression of V452:1116-1157. Everything below is in v4.5.2 and missing or shortened in v5.3.3.

**6.1 Clustering scan sub-steps** (V452:1122-1138) — v5.3.3 kept only b, c, d:
- "a. Sort all levels from highest to lowest."
- "b. For each level, count how many other levels fall within 0.15 DXY points. A "cluster" is 3+ levels within a 0.15 DXY band."
- "c. Flag every cluster of 3+ levels as a "HIGH-DENSITY ZONE" — these are the most important areas on the map where multiple independent pillars converge."
- "d. Flag every pair of levels within 0.10 DXY points as a "TIGHT CONFLUENCE" — even if only 2 levels, their proximity strengthens both."
- "e. Flag any individual level that has NO other level within 0.15 DXY points as an "ISOLATED LEVEL" — it may still be valid but lacks multi-pillar confirmation."
- "f. Check for micro-gaps: If two adjacent levels are 0.10-0.20 DXY apart and neither is part of a cluster, check whether any daily pivot level from Pillar 1 Step 8 (multiple daily computation) or any option strike conversion from Pillar 3/8 fills the gap."
- "g. Output the clustering scan results": `Clustering Scan: [X] total levels | [Y] HIGH-DENSITY ZONES | [Z] TIGHT CONFLUENCES | [W] ISOLATED LEVELS` + lists.
- The scan runs "After collecting all levels but BEFORE grouping into zones" (V452:1124). Row field: `Clustering: [HIGH-DENSITY ZONE (X levels) / TIGHT CONFLUENCE (2 levels) / ISOLATED LEVEL]` (V452:1241) — so a single isolated level can be a zone row.

**6.2 Zone top/bottom rule.** Not stated. v4.5.2 adds only the row format `ZONE: [NAME] | [RANGE] | PRESSURE: [DEGREE] ([X]/14)` followed by `Levels: [exact DXY values]` and `Primary Driver: [Pillar creating this zone]` (V452:1234-1236), and Step 4 "Group into zones where levels cluster within 0.10-0.15 DXY points." (V452:1140). **STILL UNKNOWN as a rule.**

**6.3 Zone width limits.** None for IP zones in v4.5.2. Only the 4H S/D cap of 0.40 (V452:657, 742). **STILL UNKNOWN.**

**6.4 How many zones.** No rule. Evidence: the Synthesis section shows "MODERATE AND ABOVE PRESSURE ZONES ONLY (Light/Minimal excluded)", split "RESISTANCE (from highest to lowest)" / "SUPPORT (from highest to lowest)", numbered `Zone #[N]`, with two example slots each (V452:1534-1564); a past report had at least a "Zone #8" (V452:1588); "Failed/invalid zones ... MUST be excluded" (V452:1588). **STILL UNKNOWN as a rule.**

**6.5 Name assignment** (V452:1148-1155) — v5.3.3 kept only the bare list:
- "RESISTANCE CEILING: Top zone, maximum selling pressure"
- "UPPER RESISTANCE: Secondary selling zone"
- "EQUILIBRIUM ZONE: Pivot area (classify POI Tier independently — do NOT use legacy "Decision Zone" label)"
- "MID-RANGE SUPPORT: Dip buyer zone"
- "KEY SUPPORT BAND: Maximum buying pressure"
- "LIQUIDITY SWEEP ZONE: Level at a prior exact swing low — high probability of brief breach then reversal"
- "BREAKOUT EXTENSION TARGET: Projected target from Measured Move Projection"

So: RESISTANCE CEILING = the top zone; KEY SUPPORT BAND = the support zone of maximum buying pressure; LSZ = from Pillar 5 Step 0 / 0.45; BREAKOUT EXTENSION TARGET = Pillar 9 Step 4 output. What separates resistance from support (spot? the pivot?) and what happens with more than five zones is **STILL UNKNOWN**. The Synthesis block reports `SPOT POSITION: [Between Zone #[X] and Zone #[Y]]` (V452:1571) but spot is explicitly not a mapping input (V452:100-111).

**6.6 Step 9.5 gap scan in full** (V452:1159-1184):
- 9.5a "Identify all gaps >= 0.20 DXY points between adjacent mapped zones that are NOT already flagged as discovery zones."
- 9.5b candidates: "4H demand/supply zone from prior 2-3 weeks (from Pillar 5 Step 0f)"; 1H zone (0g A or B); "Round number level (.00, .25, .50, .75) from Pillar 6"; "EUR/USD option strike conversion (Tier 3/4 from Pillar 8) in the gap"; "Daily pivot level from Pillar 1 (any of the 5 daily sets)"; "Minor swing level from Pillar 5 Step 0h"; "Extended daily close from 6-10 days ago (beyond the 5-day window from Step 1)".
- 9.5c "If any gap-region level has 2+ supporting signals: Flag as "GAP IN-FILL LEVEL" with Confidence: MODERATE; Include in the zone map with Structural dimension score = 1; Add audit trail: "Gap In-fill: [level] supported by [signal 1] + [signal 2]""
- 9.5d output; unfilled gaps are "flagged as Discovery Zones".

**6.7 Step 9.7 POI overlay in full** (V452:1186-1218):
- Metadata added: "Zone Type: BoM / MoM"; "Mitigation: [X]X mitigated ([Y] soft, [Z] hard)"; "Directional Context: [Buy trend / Sell trend / Ranging]".
- Tier 1: "IP zone OVERLAPS with 4H BoM S/D (unmitigated or 0X-1X mitigated)" → "Add +2 to confluence score **(capped at 14)**. No trade against it unless macro shape chain explicitly overrides."
- Tier 2: "IP zone exists but NO overlapping 4H BoM S/D **(or only MoM overlap)**" → "Add +1 to confluence score. Requires Engine 2 macro shape confirmation before trading."
- Tier 3: "4H BoM S/D exists but NO overlapping IP zone" → "Informational only ... May serve as SL anchor or discovery zone. **No confluence bonus.**"
- "SPECIAL EXCEPTION: BoM 0X-1X zones. A 4H BoM zone with 0X-1X mitigation that does NOT overlap with an IP zone ... is classified as Tier 3 for trade construction but flagged as "BoM Fresh — structural quality high, institutional confirmation pending." This flag is informational and does NOT upgrade the tier."
- Ladder step: "In a sell trend: 4H MoM Supply = valid ladder step entry; In a buy trend: 4H MoM Demand ...; Ladder step is ONLY valid while the trend is intact. Once opposing BoM is reached, MoM ladder steps lose validity."
- This settles E1_ALGO CONFLICT 7 in favour of the overlap definition, and gives one data point for CONFLICT 8: the POI bonus is "capped at 14".

**6.8 Dynamic Discovery Protocol** (V452:1220-1230) — absent from v5.3.3 E1 text: "Identify gaps > 0.15 DXY points between predicted levels — these are "discovery zones.""; flag zones near ".00, .50", "near prior HWC/LWC where price has not yet traded", "EMA convergence zones", "structural extremes from Pillar 5's memory database". Promotion: "price sustains for 15+ minutes at a level within a pre-identified discovery zone, AND at least 1 other pillar is within 5 pips".

**6.9 Zone row output format** (V452:1232-1245): NAME, RANGE, PRESSURE (X/14), Levels, Primary Driver, six Dimension Scores + Structural Extreme Bonus, Failure Probability + regime (four values), Measured Move Target + tier + anchor, Structural Extreme flag, Clustering, POI Tier / 4H Overlay / Ladder Step / Nested 1H Precision, Audit Trail, Discovery Zones.

**6.10 Pressure-degree table** carries a fourth column in v4.5.2, "Institutional Significance" (V452:1107-1114): EXTREME = "Institutional "wall" with structural extreme confirmation — equivalent to CRITICAL ENTRY SHIELD"; HEAVY = "Strong magnet — price will struggle to break through"; MODERATE-HEAVY = "Meaningful friction with structural support"; MODERATE = "Meaningful friction — price may stall but can break"; LIGHT = "Minor friction — price usually passes through"; MINIMAL = "Free transit — likely to fail under pressure".

**6.11 Bar-count definition of a swing high/low.** Not in v4.5.2, v5.0.0, v5.1.0, v5.2.0, v5.3.3, Leviathan v4.2/v4.3/v4.4 (all carry the same wick + close-position sentence; grep for bar-count wording = 0 hits). **STILL UNKNOWN.** Nearest statements: "Higher highs and higher lows = bullish bias" (V452:69); SS swings "typically span 1-3 trading sessions" (V452:1624).

**6.12 "Strong reaction".** The reaction counter is a v5.2.0 addition; the term does not occur in v4.5.2 Engine 1. Nearest v4.5.2 definitions, all for 4H S/D zones: "Soft Mitigation | Wicks tap zone edge, immediately rejected. Brief contact, no penetration. | Barely counts. 1X soft ~ unmitigated." and "Hard Mitigation | Full candle bodies enter zone and consolidate inside it. Real absorption. | Meaningful. Each hard mitigation weakens the zone." counted "in the prior 2-3 weeks" (V452:715-722). **STILL UNKNOWN as a number.**

**6.13 "Consolidation".** The +1 POST-CONSOLIDATION modifier is v5.2.0 (absent from V452, V500, V510). v4.5.2 uses the word three ways, none numeric: the regime row "Low volatility, no macro catalysts, options cage active" (V452:1031); the Measured Move "consolidation range" = [Range_Low, Range_High] of section 5.4 (V452:1000-1005); "After 2 strong piercing swing moves, expect 1-2 full days of HTF consolidation" (V452:79). **STILL UNKNOWN as a number.**

**6.14 Other v4.5.2 text that v5.3.3 shortened (outside the placeholders, same meaning unless noted)**
- 4H aggregation: "combine every 4 consecutive 1H candles: Open from first, High from max, Low from min, Close from last" (V452:641). The anchor hour of the first bucket is not given.
- 4H context: zone "from the prior 1-3 weeks"; "on 4H it is a clear 2-4 candle base that preceded a directional move" (V452:639) — while the construction rule is the SINGULAR origin candle (V452:645-651).
- 4H criteria: demand / supply = origin candle before a move "≥ 0.5 DXY points lasting ≥ 3 trading days"; "If move >= 1.0 DXY points and >= 5 days: tag "High-Conviction 4H OB"" (V452:678-686).
- "Classification rule: ... When in doubt, classify as MoM — the system rewards conservative classification." (V452:697)
- Noise-rejection exception: "BoM zones with 0X-1X mitigation are retained regardless of IP overlap and flagged as "4H-Only Level" ... MoM zones and BoM zones with 2X+ mitigation without IP overlap are excluded as standalone noise." (V452:745)
- "If ANY verification check fails, the zone is EXCLUDED and marked `[FAILED VERIFICATION — excluded from map]`." (V452:676)
- Order block: "the LAST SHORT candle before a BIG impulsive swing. Candle color does NOT matter ... (1) a short candle (small body relative to the subsequent move), followed by (2) a large impulsive displacement. The short candle defines the zone edges." (V452:75)
- Pillar 2 data source that v5.3.3 dropped: "Barchart DXY Cheat Sheet + TradingView DXY Technicals" (V452:398).
- Origin of "match": the pillar capture rates ("Independently captures 8/11 verified levels", V452:298) come from a backtest against the operator's own levels — "11 target levels: 99.52, 99.475, 99.4, 99.35, 99.285, 99.25, 99.2, 99.1, 99.05, 99, 98.95" → "11/11 level capture, 8/11 exact within 3 pips" (L42H:710-714). "Exact match within 3 pips" is the wording of that validation. No forward-looking match target is defined in any version.

---

## 7. E1_ALGO section 11 "UNKNOWN" register — status after this pass

Versions checked for every STILL UNKNOWN row: v4.5.2 (primary, read in full for Protocol B), v5.0.0, v5.1.0, v5.2.0, v5.3.3, Leviathan v4.4 GLM (diffed), plus grep over Leviathan v4.2, v4.2 Handover, v4.3, v4.3 changelog, v4.4 DeepSeek, DeepSeek Master v4.3.

| # | Item | Status | Value / note | Cite |
|:---|:---|:---|:---|:---|
| 1a | P6 fib ratio list | RESOLVED | 0.236, 0.382, 0.500, 0.618 as `H − r×(H−L)`; no extensions | V452:843-849 |
| 1b | P6 anchors | RESOLVED | (i) prior week H/L; (ii) "most recent significant swing high and swing low on the daily/4H chart, even if they are 2-4 months old" ("significant" undefined) | V452:843, 851 |
| 1c | P6 round-number bonus | RESOLVED | big figure +2, half figure +1.5, quarter figure +1; fib within 5 pips + round = 2 pts, fib only = 1 pt | V452:855-862 |
| 1d | Pair round-number step | STILL UNKNOWN | v4.5.2 is DXY-only | V452:81 |
| 2a | P9 regime classifier | PARTIAL | four regimes with word-list criteria; no numeric thresholds | V452:1028-1034 |
| 2b | P9 breakout pre-conditions | RESOLVED | eight additive signals with ranges (two more than Appendix B) | V452:974-985 |
| 2c | Measured Move formula | RESOLVED | `Raw_Target = Range_High + (Range_High − Range_Low)`; snap to structural extreme within ±0.20; four confidence tiers; downside mirror Derived | V452:996-1026 |
| 2d | How ZFP modifiers combine; cap | RESOLVED | sum of base + modifiers, "capped at 95%" | V452:987-994 |
| 2e | Point value inside a base range / modifier range | STILL UNKNOWN | only "Show the base probability and each modifier applied" | V452:52 |
| 3a | P7 procedure | RESOLVED | top-3 put OI + top-3 call OI DX strikes overlaid as ALL-DAY MACRO TARGETS; no boundary formula, no score; fallback string | V452:866-886 |
| 3b | P8 confidence weighting | RESOLVED (tiers superseded) | score 2 / 2 / 1-if-override / 0, bands ±0.07 / ±0.10 / ±0.15; cluster within 10 pips aggregates; union across days; 70/30 vs Pillar 3 | V452:921-944 |
| 3c | P5 Step 0g | RESOLVED | Condition A nested (2-3 candle 1H base, ≥0.3 move, ≥1 day) / Condition B gap-fill (gap ≥0.20, prior week, MODERATE) | V452:749-763 |
| 3d | P5 Step 0h | RESOLVED (one internal ambiguity) | wick ≥ 0.08, close in upper/lower 40%, D1 + 4H, Structural = 0.5 | V452:767-781 |
| 3e | P5 Steps 1-5 | RESOLVED | anchors list; HWC/LWC; recapture; memory table; scoring caps | V452:785-831 |
| 3f | Meaning of HWC / LWC | RESOLVED | High-Week Close = highest weekly close in a given period; Low-Week Close = lowest weekly close in a given period; period = year in the worked example | V452:794-796; L42H:717 |
| 4a | Bar-count definition of swing high/low | STILL UNKNOWN | no version defines it | — |
| 4b | "large bodies" threshold | STILL UNKNOWN | same sentence in all versions (V452:553-554) | — |
| 4c | Wick measurement basis | STILL UNKNOWN | "the candle body closes significantly above the low" is the only gloss | V452:540 |
| 5a | MA timeframe | PARTIAL | sources are the Barchart cheat sheet + TradingView technicals page; "EMA/SMA 100 ... 5 months of price history" → daily by inference, never stated | V452:398-402, 414 |
| 5b | How MA weights are used | STILL UNKNOWN | table identical, no consuming formula | V452:410-417 |
| 5c | Double-cluster tolerance | STILL UNKNOWN | only "3+ MAs converge within 0.15" | V452:408, 421 |
| 6a | What a pivot is "matched" against | STILL UNKNOWN (origin found) | wording comes from the backtest against the operator's 11 target levels; no forward reference set defined | V452:390; L42H:710-714 |
| 6b | How P1 and P2 combine in Technical | STILL UNKNOWN | — | — |
| 7a | Zone top/bottom rule | STILL UNKNOWN | only row format `[RANGE]` + `Levels: [exact DXY values]` | V452:1234-1235 |
| 7b | Min/max IP zone width | STILL UNKNOWN | — | — |
| 7c | Number of zones | STILL UNKNOWN | Synthesis = all zones MODERATE and above, resistance list + support list | V452:1534-1564, 1587 |
| 7d | Rule assigning the seven names | PARTIAL | one-line role definition per name (top zone / secondary selling / pivot area / dip buyer / maximum buying pressure / prior exact swing low / measured-move target); no positional algorithm | V452:1148-1155 |
| 8 | Tolerances in EURUSD / GBPUSD units | STILL UNKNOWN | v4.5.2 is DXY-only; Appendix A.2 identical | V452:81, 2350-2358 |
| 9a | Numeric "strong reaction" | STILL UNKNOWN | nearest: soft vs hard mitigation definitions | V452:715-722 |
| 9b | Numeric "consolidation" for the +1 modifier | STILL UNKNOWN | modifier is v5.2.0; no definition in any version | — |
| 9c | Thin vs thick liquidity | STILL UNKNOWN | terms absent from v4.5.2 | — |
| 10 | 4H bucket alignment | PARTIAL | "combine every 4 consecutive 1H candles: Open from first, High from max, Low from min, Close from last"; anchor hour not given | V452:641 |
| 11 | Which pair pressure score wins | STILL UNKNOWN | pair logic not active in v4.5.2 | V452:81 |

Newly found gaps (not in the E1_ALGO register): 1H zone [low, high] construction; Step 0h "upper/lower 40%" vs "close 47th%" example; "exact" vs "proximity" tolerance for the Structural dimension; what the Pillar 8 / Pillar 3 70/30 weight applies to; "failing zone level" for a ranged zone; behaviour when regime and ZFP band disagree in the Regime dimension.

---

## 8. Where v4.5.2 CONTRADICTS v5.3.3 (v5.3.3 wins)

| # | Topic | v4.5.2 | v5.3.3 |
|:---|:---|:---|:---|
| 1 | Option tier system | four tiers: ≥1.0B CRITICAL OPTION WALL / 900M-1.0B SIGNIFICANT MAGNET / 500M-900M CONDITIONAL MAGNET / <500M NOISE (V452:462-467, 929-934) | three tiers: ≥$1.5B / $850M–$1.499B / <$850M EXCLUDED (SP:1129-1135, 1445-1447) |
| 2 | Pillar 8 conversion floor and fallback | "notional >= 500M EUR" (V452:921, 942) | $850M ("The threshold is now $850M, not $500M", SP:1135) |
| 3 | Override logic | Tier 3: Pillar 5 reaction level **OR** 3+ pillars; Tier 4 (score 0.5, +0.5): 3+ pillars AND 90-day reaction (V452:466-473, 936) | single override: "3+ pillar confluence **+** Pillar 5 Step 0/0.5 validation"; no Tier 4 (SP:1133, 1140) |
| 4 | ZFP zone-type thresholds | Hard Wall "≥ 1B", Standard Wall "≥ 500M", Soft Wall "<500M" (V452:967-969, 2376-2378) | "≥$1.5B", "$850M–$1.499B", "<$850M" (SP:4058-4060) |
| 5 | Synthesis Options-Derived row | "Critical Option Wall (>=1B)" / "Significant Magnet (>=500M)" (V452:1084) | "(≥1.5B)" / "($850M-$1.499B)" (SP:1470) |
| 6 | Critical Entry Shield size | ">= USD 1.0 Billion" (V452:93, 1440) | ">= USD 1.5 Billion" (SP:690) |
| 7 | Gap-scan option candidate | "EUR/USD option strike conversion (Tier 3/4 from Pillar 8)" (V452:1169) | "option conversions" (SP:1507); sub-$850M strikes cited as primary driver are downgraded by Step 9.8 (SP:1520) |
| 8 | LSZ width | 0.05 only (V452:579, 584) | 0.05 plus Step 0.45a extension 0.05-0.10 (SP:1284-1286) |
| 9 | OHLC / MA data source | Yahoo Finance + Barchart + TradingView (V452:300, 398, 523, 535) | TradingView only (SP:1211, 1217; Barchart rows removed) |
| 10 | Pillar 5 pre-computation steps | "TWO mandatory pre-computation steps (Step 0 and Step 0.5)" (V452:519) | "Step 0, Step 0.5, Step 0.6" (SP:1207) |
| 11 | Scope | DXY only, pair logic "NOT active" (V452:81) | pair translation and pair pipelines active |
| 12 | BoM/MoM and reaction counting | BoM/MoM and soft/hard mitigation counts belong to 4H S/D zones only (V452:688-730) | BoM/MoM + Zone Reaction Counter also applied "For every IP zone" (SP:1147-1161) |
| 13 | ZFP modifier list | eight signals in the Pillar 9 body (V452:974-985) | Pillar 9 body is a placeholder; Appendix B lists six (SP:4067-4074). Not a true contradiction — v5.3.3 declares Pillar 9 "unchanged from v4.5.2" (SP:1457) — but the two tables differ |
| 14 | "Decision Zone" label | "do NOT use legacy "Decision Zone" label" for the equilibrium zone (V452:1151) | "Decision Zone" reused as an Engine 2 chain-branch term (SP:1895, 2006) |
| 15 | Post-consolidation +1 | absent | Zone Assembly step 9 (SP:1505) |

Items present in v4.5.2 and silently absent from v5.3.3 (no v5.3.3 statement contradicts them): BREAKOUT SWEET SPOT 25-45% (V452:1064); ISOLATED LEVEL flag and micro-gap check (V452:1130-1131); Dynamic Discovery Protocol (V452:1220-1230); "(capped at 14)" on the POI bonus and "(or only MoM overlap)" in Tier 2 (V452:1201-1202); Gap In-fill "Structural dimension score = 1" (V452:1176).
