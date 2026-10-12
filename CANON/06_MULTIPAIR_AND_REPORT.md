# 06 — MULTIPAIR TRANSLATION & REPORT OUTPUT SPEC
Source: Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md :: Part V (ll.1568-1725), Part IX (ll.3257-3688)

---

## PART V: REPORT OUTPUT SPECIFICATION

### 5.1 Mandatory Report Header

Every report MUST begin with:

```
LEVIATHAN DXY INSTITUTIONAL LIQUIDITY REPORT
Target Week: [Monday date] – [Friday date]
Data As-Of: [Friday date] 17:00 ET — All data is pre-market-open for the target week of [Monday date].
DXY Spot at Report Time: [value] (Source: [URL])
Generated: [timestamp]
Engine Version: Trident v5.2.1
```

The "Data As-Of" line is MANDATORY and certifies compliance with the Temporal Boundary Rule. Its absence invalidates the entire report.

### 5.2 Mandatory Sections

1. **OTC FX Option Expiry Summary** (Protocol A output — with Filter Checkpoint and Filter Audit Line)
2. **DXY Institutional Pressure Zone Map** (Protocol B output — 9-Pillar synthesis)
3. **DXY Institutional Pressure Zone Map — Synthesis** (dedicated clean synthesis section)
4. **4H Zone Classification Overlay Summary** (Step 9.7)
5. **Liquidity Sweep Zone Summary** (Step 0.45)
6. **Pivot Verification Audit Trail** (from Pillar 1 Step 8)
7. **K Factor Audit Trail** (from Pillar 8 Step 3)
8. **Clustering Scan Results** (from Zone Assembly Step 3)
9. **4H Zone Verification Audit Trail** (from Step 0f)
10. **Treasury Auction Analysis** (Protocol D output)
11. **ON RRP Facility Status** (Protocol E output)
12. **Economic Calendar & Red Folder Time-Locks** (Protocol F output)
13. **EIA Petroleum Status** (Protocol G output)
14. **Volatility Trigger Summary** (consolidated — column headers: Strike Time, Context, Analysis)
15. **Breakout Risk Alerts** (any zone with ZFP > 50%)
16. **Missing Data Log** (explicit list of all [NO DATA] sections)
17. **Macro Shape Chain Map** (Engine 2 output)
18. **Trade Setup Architecture** (Engine 3 output — with Weekly Execution Calendar + Multi-Setup Architecture + DAY labels)
19. **Compliance Sweep Results** (v5.0.0 — mandatory post-generation verification)
20. **Filter Checkpoint Summary** (v5.0.0 — consolidated filter checkpoint results across all protocols)

**v5.0.0 MULTI-PAIR SECTIONS (21-36):**

21. **EUR/USD Layer 1 Translation** (DXY zones translated to EUR/USD via Structural Equivalence)
22. **EUR/USD Layer 2 Verification** (pair-specific data cross-validation)
23. **EUR/USD Institutional Pressure Zone Map — Pair Synthesis**
24. **GBP/USD Layer 1 Translation**
25. **GBP/USD Layer 2 Verification**
26. **GBP/USD Institutional Pressure Zone Map — Pair Synthesis**
27. **AUD/USD Layer 1 Translation**
28. **AUD/USD Layer 2 Verification**
29. **AUD/USD Institutional Pressure Zone Map — Pair Synthesis**
30. **EUR/USD Trade Setup Architecture** (pair-specific trade setups)
31. **GBP/USD Trade Setup Architecture**
32. **AUD/USD Trade Setup Architecture**
33. **Cross-Pair Comparison Matrix** (v5.0.0 — see format below)
34. **Macro Shape Chain Translation** (v5.0.0 — weekly shape chain visualization for each pair)
35. **Pair Translation Audit Trail** (v5.0.0 — complete audit of every translated level)
36. **Pair Translation Compliance Verification** (v5.0.0 — confirms no mathematical conversion used)

### 5.2.1 SECTION 3 FORMAT: DXY INSTITUTIONAL PRESSURE ZONE MAP — SYNTHESIS

**v5.3.3 — COMPLETE FORMAT (replaces "[unchanged from v4.5.2]" placeholder):**

The DXY IP Zone Map Synthesis is the clean synthesis section showing only MODERATE and above zones, with the following columns:

| Column | Description |
|:---|:---|
| Zone Name | Descriptive name (e.g., "Key Resistance 103.80-104.20") |
| Range | DXY price range |
| Pressure Degree | Extreme / Heavy / Moderate-Heavy / Moderate / Light / Minimal |
| POI Tier | 1 / 2 / 3 (based on confluence score) |
| ZFP | Zone Failure Probability percentage |
| BoM Fresh Flag | BoM=Fresh origin zone, MoM=Continuation zone |
| Liquidity Sweep Status | Swept / Unswept / Partial |
| Ladder Step Status | Valid ladder step for trend-aligned reinforcement (Y/N) |
| Engine 3 Status | ENTRY-PRIMARY / ENTRY-CONDITIONAL / TP-TARGET / REJECT |
| Primary Trade Setup | Reference to Engine 3 setup that uses this zone (if any) |

**MODERATE and above zones only.** Light and Minimal zones are excluded from synthesis but remain in the full protocol output for reference.

### 5.3 Missing Data Log Requirement

**v5.3.3 — COMPLETE FORMAT (replaces "[unchanged from v4.5.2]" placeholder):**

Every report MUST include an explicit Missing Data Log listing all sections where data could not be obtained:

```
═══════════════════════════════════════════════════
MISSING DATA LOG
═══════════════════════════════════════════════════
Protocol | Section | Reason | Impact | Mitigation
─────────|─────────|────────|────────|──────────
A        | OTC Tue | Source inaccessible | Missing Tue expiries | Use Mon/Wed interpolation
B        | Pillar 5| No analyst data | Reduced confluence scoring | Rely on Pillar 1-4 only
D        | Treasury| No auction this week | None | N/A
═══════════════════════════════════════════════════
```

**Impact Assessment**: Each missing data point must be classified as:
- **CRITICAL**: Missing data affects trade setup construction (zone may be wrong)
- **SIGNIFICANT**: Missing data reduces confidence scoring (less confluence)
- **MINOR**: Missing data is supplementary only (does not affect setup quality)

### 5.4 Cross-Pair Comparison Matrix Format (v5.0.0)

```
═══════════════════════════════════════════════════════════════
CROSS-PAIR COMPARISON MATRIX | WEEK OF [DATE]
═══════════════════════════════════════════════════════════════
Zone Role | DXY Range | EUR/USD Range | GBP/USD Range | AUD/USD Range | Pressure | DXY Dir | Pair Dir
───────────────────────────────────────────────────────────────
Resist. Ceiling | [range] | [range] | [range] | [range] | [DEGREE] | Up | Down
Upper Resist.   | [range] | [range] | [range] | [range] | [DEGREE] | Up | Down
Equilibrium     | [range] | [range] | [range] | [range] | [DEGREE] | — | —
Mid-Range Supt. | [range] | [range] | [range] | [range] | [DEGREE] | Down | Up
Key Support     | [range] | [range] | [range] | [range] | [DEGREE] | Down | Up
LSZ             | [range] | [range] | [range] | [range] | SPECIAL  | — | —
Breakout Target | [range] | [range] | [range] | [range] | TARGET   | [dir] | [inv dir]
───────────────────────────────────────────────────────────────
Translation Method: Structural Equivalence (Approach B)
All pair levels sourced from pair-specific data — NO mathematical conversion from DXY
Verification: Layer 2 cross-validated against [X]+ sources per pair
═══════════════════════════════════════════════════════════════
```

### 5.5 Report Blind-Execution Protocol (v5.3.3 — CRITICAL — NEW)

**THE REPORT MUST BE FULLY SELF-CONTAINED AND BLINDLY EXECUTABLE.** The trader must be able to execute an entire week's worth of trades purely from the report without looking at any other data source, chart, or analysis. If the trader cannot do this, the report is INCOMPLETE.

**Mandatory Verification Checklist (execute BEFORE delivering the report):**

| # | Check | Pass Condition | Failure Action |
|:---|:---|:---|:---|
| BE1 | Every trade setup has a DAY label | All setups in Section 18 specify Mon/Tue/Wed/Thu/Fri | Add DAY assignment via Section 8.0.2 bridge |
| BE2 | Every trade setup has a SESSION WINDOW | All setups specify London/NY with time window | Assign session based on shape type + pair role |
| BE3 | Every trade setup has a SHAPE TRIGGER | All setups reference which macro shape activates them | Map from Engine 2 day-by-day decomposition |
| BE4 | Every trade setup has a SETUP CATEGORY | All setups labeled as HTF Swing / Swing Scalp / Breakout Search / Reinforcement / Transition | Classify per Section 8.0.1 |
| BE5 | Weekly Execution Calendar is populated | Section 18 starts with day-by-day calendar showing ALL setups | Populate from Engine 2→3 day bridge |
| BE6 | All anchor points have WHEN + WHERE | Every IP zone / liquidity zone that is an entry trigger specifies WHEN it's expected to be hit | Assign anchor hit window per Section 8.0.2 |
| BE7 | No setup requires real-time chart analysis | All entries are described with exact levels + conditions that can be pre-set | Add missing entry conditions or remove setup |
| BE8 | Day Catalysts are listed | Each setup's day shows relevant expiries / economic events / auctions | Cross-reference Protocol A/F/D outputs |
| BE9 | Reinforcement entries have parent trade reference | Each reinforcement specifies which primary trade it reinforces + DAY of primary | Add parent reference + day inheritance |
| BE10 | All 5 trading days are covered | Calendar shows at least 1 setup per day, OR explicitly states "No qualifying setups — [reason]" | If no setups on a day, state why (e.g., "Red Folder Thursday — all setups deferred") |
| BE11 | Profit Taking Law is documented | Report states "Close ALL positions by NY close Friday" for each pair | Add to Daily Session Notes |
| BE12 | Trading Speed adjustment applied | Day predictions include +1 day from raw timing per Section 6.10 | Apply speed adjustment to all DAY assignments |

**If ANY check fails, the report is INCOMPLETE and MUST be revised before delivery.** The trader is deploying real capital based on this document. A missing DAY label means a missed trade or an unprepared trade. Zero tolerance.

**Additional Self-Containedness Requirements:**
- Every zone mentioned in a trade setup must appear in the IP Zone Map (Section 3) with full properties
- Every shape trigger must appear in the Engine 2 Day-by-Day Decomposition (Section 17)
- Every reinforcement must reference a parent trade with matching entry level
- The Pine Script indicator (Section 36) must contain ALL zones from ALL setups
- The report must NOT reference any external resource for trade execution (no "check TradingView for confirmation")

---

## PART IX: MULTI-PAIR TRANSLATION PROTOCOL (v5.0.0 — NEW — MOST CRITICAL ADDITION)

This part defines the complete protocol for translating DXY analysis to EUR/USD (EU), GBP/USD (GU), and AUD/USD (AU) pairs. It is the MOST CRITICAL addition in v5.0.0 because it prevents the catastrophic failure that occurred when v4.5.2 attempted pair expansion using mathematical conversion.

### 9.0 Architecture Overview

The multi-pair translation follows a strict 4-phase architecture:

```
Phase 1: DXY Report (Engines 1-3)
  → Complete DXY analysis with all 9 Pillars, Engine 2, Engine 3
  → This phase is UNCHANGED from v4.5.2 — DXY analysis quality must remain A+

Phase 2: Layer 1 Translation (Directional Conviction Transfer)
  → Translate DXY directional conviction to each pair
  → DXY zones → pair direction assignments (NOT pair price levels)
  → This is the STRUCTURAL EQUIVALENCE method

Phase 3: Layer 2 Verification (Pair-Specific Data Cross-Validation)
  → For each translated zone, verify against pair-specific data
  → Each pair level MUST come from the pair's own data sources
  → Cross-validation: every translated zone must be within 100 pips of a verified structural level on that pair

Phase 4: Cross-Pair Comparison Matrix
  → Assemble the comparison matrix showing all pairs side by side
  → Identify pair divergences (where one pair's technicals contradict DXY direction)
  → Flag divergences as RISK FACTORS, not invalidations
```

**CRITICAL PRINCIPLE:** Phase 1 (DXY report) must be COMPLETE and VERIFIED before Phase 2 begins. The DXY report quality must NOT degrade because of pair translation work. The DXY report is the foundation — pair translation is built on top of it.

### 9.1 DXY→Pair Causality Principle

**The causal chain is ONE-DIRECTIONAL:**

```
USD Macro Forces (Fed policy, US data, risk sentiment)
  ↓
DXY (measures USD strength)
  ↓
EUR/USD, GBP/USD, AUD/USD (each pair responds to USD forces, but with its own dynamics)
```

**What this means in practice:**
- DXY going UP → USD strengthening → EU/GU/AU likely going DOWN (inverse)
- DXY going DOWN → USD weakening → EU/GU/AU likely going UP (inverse)
- The MAGNITUDE of the pair move depends on the pair's own dynamics (ECB policy for EU, BOE for GU, RBA for AU, commodity exposure for AU, etc.)
- DXY is the DRIVER; the pairs are the RESPONDERS

**What this does NOT mean:**
- DXY price levels do NOT determine pair price levels
- A DXY support zone at 98.50 does NOT compute to a EUR/USD resistance at some formula-derived level
- The relationship is CAUSAL (same driver, different instruments) not ARITHMETIC (same scale, different units)

### 9.2 The CRITICAL Rule — Directional Conviction Only

**DXY provides DIRECTION. The PAIR provides LEVELS.**

This is the single most important rule in Part IX. Violation of this rule produces reports that are 355-710 pips off from reality.

**What DXY provides:**
- Which zones MATTER (the DXY zones with highest pressure are the zones that will drive pair movement)
- Which DIRECTION the pair will move (DXY up = pair down, DXY down = pair up)
- The TIMING of moves (macro shape chain timing applies to all instruments)
- The CONVICTION level (HEAVY/EXTREME DXY zones = high-conviction pair zones)

**What the PAIR provides (from its OWN data sources):**
- The exact PRICE LEVELS for support and resistance
- The 200-day MA value (from TradingView for that pair)
- The swing structure (prior week high/low/close for that pair)
- The options data (if EU/GU/AU strikes exist in Protocol A)
- The institutional commentary (pair-specific analyst levels)
- The MA confluence grid (for that specific pair)

**The translation is:**
- DXY resistance zone (HIGH conviction that DXY will struggle to go higher) → EUR/USD SUPPORT zone (HIGH conviction that EU will struggle to go lower)
- DXY support zone (HIGH conviction that DXY will find buyers) → EUR/USD RESISTANCE zone (HIGH conviction that EU will find sellers)
- The CONFIDENCE transfers. The PRICE LEVELS come from the pair.

### 9.3 PROHIBITED Methods

The following methods are **ABSOLUTELY PROHIBITED** for translating DXY levels to pair levels. Using any of these methods constitutes a CRITICAL FAILURE equivalent to data fabrication:

❌ **PROHIBITED: Mathematical Conversion**
- Computing pair levels from DXY levels using the DXY formula in reverse
- Example: DXY support at 98.50 → computing EUR/USD = (K/98.50)^1.7361 = 1.1295 (WRONG — this was the v4.5.2 failure)

❌ **PROHIBITED: Inverse Correlation Ratio**
- Applying a fixed multiplier or ratio to convert DXY ranges to pair ranges
- Example: "DXY zone is 0.25 points wide, so EUR/USD zone is 0.25 × 100 = 25 pips" (WRONG — pair zone widths are determined by the pair's own structure)

❌ **PROHIBITED: Arithmetic Inversion of DXY Prices**
- Subtracting DXY levels from some constant to get pair levels
- Example: "100 - 98.50 = 1.50, so EUR/USD resistance = 1.1500" (WRONG — there is no arithmetic relationship)

❌ **PROHIBITED: Percentage-Based Conversion**
- Applying a percentage of DXY move to pair price
- Example: "DXY dropped 0.5%, so EUR/USD rises 0.5% from spot" (WRONG — pair magnitudes are pair-specific)

❌ **PROHIBITED: Pip Equivalence Conversion**
- Converting DXY points to "equivalent pips" on the pair
- Example: "0.25 DXY points ≈ 50 EUR/USD pips" (MISLEADING — the pip equivalence varies with spot rate and is not a valid translation method)

**WHY these methods fail:** They treat the DXY↔pair relationship as an arithmetic conversion between two scales measuring the same thing. In reality, DXY and EUR/USD are DIFFERENT INSTRUMENTS responding to the SAME DRIVER. A thermometer reading (DXY) tells you it's hot, but it doesn't tell you the patient's (pair's) blood pressure — you need a separate instrument for that.

### 9.4 APPROACH B — Structural Equivalence Methodology (MANDATORY)

This is the ONLY approved method for translating DXY analysis to pair analysis. It works by transferring DIRECTIONAL CONVICTION from DXY zones to pair-specific price levels.

**Step-by-step procedure:**

**Step 1: Complete DXY Report (Phase 1)**
- Execute Engines 1, 2, 3 for DXY as per Parts III-VIII
- Identify all DXY IP zones with their Pressure Degrees, ZFPs, and structural roles
- Identify the macro shape chain with its direction
- Identify the primary trade setup direction
- This step is UNCHANGED from v4.5.2

**Step 2: Map DXY Zones to Pair Direction Assignments (Phase 2 — Layer 1)**
- For each DXY zone, determine the PAIR-SPECIFIC direction implication:
  - DXY resistance → pair support (when DXY can't go higher, pair stops falling)
  - DXY support → pair resistance (when DXY bounces, pair reverses from highs)
  - DXY LSZ (demand-side) → pair supply-side zone
  - DXY LSZ (supply-side) → pair demand-side zone
  - DXY breakout target (upside) → pair breakdown target (downside)
  - DXY breakout target (downside) → pair breakout target (upside)

**Step 3: Harvest Pair-Specific Data (Phase 2 — Layer 1 data collection)**
- For EACH pair (EU, GU, AU), fetch:
  - TradingView technicals (EMA/SMA values, buy/sell signal counts)
  - forex.com institutional research (HWC/LWC, S/R levels)
  - yfinance 4H OHLC data (for zone scanning)
  - Web search for pair-specific institutional commentary
  - Protocol A pair-specific options data (if available)
- See Section 9.7 for complete data requirements per pair

**Step 4: Identify Pair-Specific Zones (Phase 2 — Layer 1 zone construction)**
- Using the pair-specific data from Step 3, identify:
  - Pair MA confluence clusters (from TradingView)
  - Pair swing structure (from yfinance 4H data — prior week H/L/C, 90-day extremes)
  - Pair institutional S/R levels (from forex.com + web search)
  - Pair options data (from Protocol A if pair strikes are present)
  - Pair fib levels (from pair's own swing points)
  - Pair round numbers (for pairs, big figures are 1.1000, 1.1500, etc.)

**Step 5: Match DXY Directional Conviction to Pair Levels (Phase 2 — Layer 1 matching)**
- For each DXY zone with a directional implication:
  1. Note the DXY zone's Pressure Degree and structural role
  2. Note the DXY zone's direction implication for the pair (support/resistance)
  3. Find the NEAREST pair-specific level that serves that role
  4. Transfer the DXY zone's conviction score to the pair level
  5. Record the pair level with its OWN data source

**Example:**
```
DXY Zone: RESISTANCE CEILING at 99.50-99.65 | EXTREME (12/14) | ZFP: 8%
Direction Implication for EUR/USD: SUPPORT (when DXY can't go higher, EU stops falling)
Pair-Specific Level Search:
  - TradingView EUR/USD: EMA 200 at 1.1518
  - forex.com EUR/USD research: "Key support at 1.1500-1.1520"
  - Prior week EUR/USD low: 1.1495
  - Web search ING: "EUR/USD support at 1.1510"
Match: EUR/USD SUPPORT at 1.1495-1.1520 | Conviction: EXTREME (transferred from DXY)
Data Source: TradingView + forex.com + yfinance + ING
```

**Step 6: Cross-Validate (Phase 3 — Layer 2 Verification)**
- For each matched pair level, verify against Layer 2 requirements (Section 9.6)
- If a level fails verification, downgrade its conviction and flag as "UNVERIFIED — pair data insufficient"
- If a level passes verification, it becomes a CONFIRMED TRANSLATED ZONE

**Step 7: Assemble Cross-Pair Comparison Matrix (Phase 4)**
- Using the confirmed translated zones, assemble the matrix per Section 5.4
- Identify pair divergences
- Flag risks

### 9.5 Layer 1 Translation Rules

**Zone-by-zone translation mapping table:**

| DXY Zone Role | DXY Direction Implication | Pair Zone Role | Pair Direction Implication | Conviction Transfer |
|:---|:---|:---|:---|:---|
| RESISTANCE CEILING | DXY struggles to go higher | SUPPORT FLOOR | Pair struggles to go lower | DIRECT — same conviction score |
| UPPER RESISTANCE | DXY faces selling pressure | LOWER SUPPORT | Pair faces buying pressure | DIRECT — same conviction score |
| EQUILIBRIUM ZONE | DXY neutral/pivot | EQUILIBRIUM ZONE | Pair neutral/pivot | NEUTRAL — conviction = DXY score minus 2 (minimum 0) |
| MID-RANGE SUPPORT | DXY finds buyers | MID-RANGE RESISTANCE | Pair finds sellers | INVERTED — same conviction score |
| KEY SUPPORT BAND | DXY has strong buying | KEY RESISTANCE BAND | Pair has strong selling | INVERTED — same conviction score |
| LSZ (demand-side) | DXY sweeps lows then bounces | LSZ (supply-side) | Pair sweeps highs then rejects | INVERTED — same conviction score |
| LSZ (supply-side) | DXY sweeps highs then rejects | LSZ (demand-side) | Pair sweeps lows then bounces | INVERTED — same conviction score |
| BREAKOUT TARGET (up) | DXY target if resistance breaks | BREAKDOWN TARGET (down) | Pair target if support breaks | INVERTED — same conviction score |
| BREAKOUT TARGET (down) | DXY target if support breaks | BREAKOUT TARGET (up) | Pair target if resistance breaks | INVERTED — same conviction score |
| DISCOVERY ZONE | DXY level to watch | DISCOVERY ZONE | Pair level to watch | NEUTRAL — reduced confidence |

### 9.6 Layer 2 Verification Protocol (MANDATORY)

Every translated zone MUST pass Layer 2 verification before inclusion in the pair report. Layer 2 verification requires PAIR-SPECIFIC data that CONFIRMS the translated level is structurally valid on that pair.

**Layer 2 Data Requirements (per pair, per translated zone):**

| Requirement | Data Source | Minimum Standard |
|:---|:---|:---|
| 1. Verified spot price from 2+ independent sources | Yahoo Finance + TradingView | 2 sources must agree within 5 pips |
| 2. 200-day MA value from web data | TradingView technicals | Must have value from at least 1 source |
| 3. At least 3 institutional S/R levels from web sources | forex.com + web search (ING, FXStreet, VT Markets) | 3 explicit levels from at least 2 independent sources |
| 4. MA signal consensus (Buy/Sell count) | TradingView technicals or Investing.com | Must have signal count from at least 1 source |
| 5. Recent swing structure (prior week H/L/C) | yfinance 4H data | Must have H, L, C for prior week |
| 6. Pair-specific options data (if available) | Protocol A (if pair strikes exist) | If no pair options data, mark as [NO PAIR OPTIONS DATA] — not a failure |
| 7. Cross-validation: translated zone within 100 pips of verified structural level | All of the above | Every translated zone must be within 100 pips of at least ONE verified structural level on that pair |

**Verification Scoring:**

| Requirements Met | Verification Status | Report Treatment |
|:---|:---|:---|
| 7/7 | VERIFIED — HIGH CONFIDENCE | Include with full conviction score |
| 5-6/7 | VERIFIED — MODERATE CONFIDENCE | Include with conviction score minus 1 |
| 3-4/7 | PARTIALLY VERIFIED | Include with conviction score minus 2 and flag as "PARTIALLY VERIFIED" |
| < 3/7 | UNVERIFIED | EXCLUDE from pair synthesis — flag as "UNVERIFIED — pair data insufficient for translation" |

**Verification Output (mandatory for each pair):**
```
Layer 2 Verification: [PAIR]
  Spot Price: [value] (Sources: [URL1], [URL2]) | Agreement: [within 5 pips / DISCREPANCY]
  200-day MA: [value] (Source: [URL]) | Status: [OBTAINED / MISSING]
  Institutional S/R Levels: [list 3+ levels with sources] | Status: [3+ from 2+ sources / INSUFFICIENT]
  MA Signal Consensus: [Buy: X / Sell: Y / Neutral: Z] (Source: [URL]) | Status: [OBTAINED / MISSING]
  Prior Week H/L/C: [H] / [L] / [C] (Source: yfinance) | Status: [OBTAINED / MISSING]
  Pair Options Data: [list strikes or "NO PAIR OPTIONS DATA"] | Status: [OBTAINED / NOT AVAILABLE]
  Cross-Validation: [X] of [Y] translated zones within 100 pips of verified level | Status: [PASS / FAIL]
  Overall: [VERIFIED HIGH / VERIFIED MODERATE / PARTIALLY VERIFIED / UNVERIFIED]
```

### 9.7 Pair-Specific Data Harvesting Requirements

**EUR/USD (EU):**

| Data Point | Source | Access Method |
|:---|:---|:---|
| EMA/SMA values, Buy/Sell signals | TradingView EUR/USD Technicals | `z-ai page_reader --url "https://www.tradingview.com/symbols/EURUSD/technicals/"` |
| HWC/LWC, S/R levels | forex.com EUR/USD Research | `z-ai page_reader --url "https://www.forex.com/en-us/market-analysis/latest-research/"` then search for EUR/USD |
| 4H OHLC data | yfinance | `yfinance.download('EURUSD=X', interval='1h', period='60d')` then aggregate to 4H |
| Institutional commentary | Web Search | `"EUR/USD outlook [month year]"`, `"EUR/USD forecast support resistance ING FXStreet"` |
| Options data | Protocol A | Filter for EUR/USD strikes ≥$850M |
| Verified spot price | Yahoo Finance + TradingView | 2 independent sources |

**GBP/USD (GU):**

| Data Point | Source | Access Method |
|:---|:---|:---|
| EMA/SMA values, Buy/Sell signals | TradingView GBP/USD Technicals | `z-ai page_reader --url "https://www.tradingview.com/symbols/GBPUSD/technicals/"` |
| HWC/LWC, S/R levels | forex.com GBP/USD Research | `z-ai page_reader --url "https://www.forex.com/en-us/market-analysis/latest-research/"` then search for GBP/USD |
| 4H OHLC data | yfinance | `yfinance.download('GBPUSD=X', interval='1h', period='60d')` then aggregate to 4H |
| Institutional commentary | Web Search | `"GBP/USD outlook [month year]"`, `"GBP/USD forecast support resistance ING FXStreet"` |
| Options data | Protocol A | Filter for GBP/USD strikes ≥$850M |
| Verified spot price | Yahoo Finance + TradingView | 2 independent sources |

**AUD/USD (AU):**

| Data Point | Source | Access Method |
|:---|:---|:---|
| EMA/SMA values, Buy/Sell signals | TradingView AUD/USD Technicals | `z-ai page_reader --url "https://www.tradingview.com/symbols/AUDUSD/technicals/"` |
| HWC/LWC, S/R levels | forex.com AUD/USD Research | `z-ai page_reader --url "https://www.forex.com/en-us/market-analysis/latest-research/"` then search for AUD/USD |
| 4H OHLC data | yfinance | `yfinance.download('AUDUSD=X', interval='1h', period='60d')` then aggregate to 4H |
| Institutional commentary | Web Search | `"AUD/USD outlook [month year]"`, `"AUD/USD forecast support resistance ING FXStreet"` |
| Options data | Protocol A | Filter for AUD/USD strikes ≥$850M |
| Verified spot price | Yahoo Finance + TradingView | 2 independent sources |

### 9.8 Zone Translation Mapping (with Examples)

**DXY RESISTANCE → PAIR SUPPORT:**

When DXY has a RESISTANCE CEILING at 99.50-99.65 with EXTREME pressure (12/14), this means:
- DXY is HIGHLY LIKELY to be rejected at this zone
- If DXY is rejected downward, EUR/USD will be pushed UPWARD
- But the EUR/USD level where it finds support (stops falling) is NOT computed from 99.50
- Instead, EUR/USD will find support at its OWN structural levels that align with the "DXY rejection" scenario

**Example Translation:**
```
DXY Zone: RESISTANCE CEILING | 99.50-99.65 | EXTREME (12/14) | ZFP: 8%
Direction: DXY likely to be rejected DOWN here → EUR/USD likely to find SUPPORT

EUR/USD Pair-Specific Levels in the "support" role (from pair data):
  - 200-day SMA: 1.1520 (TradingView)
  - Prior swing low: 1.1495 (yfinance)
  - forex.com key support: 1.1500-1.1520
  - ING commentary: "1.1510 is key support"
  - EMA 100: 1.1505 (TradingView)

TRANSLATED ZONE: EUR/USD SUPPORT at 1.1495-1.1520 | EXTREME (12/14 transferred)
Source: Pair-specific data from TradingView + forex.com + yfinance + ING
NOT computed from DXY 99.50 via any formula
```

**DXY SUPPORT → PAIR RESISTANCE:**

```
DXY Zone: KEY SUPPORT BAND | 98.00-98.15 | HEAVY (10/14) | ZFP: 12%
Direction: DXY likely to find buyers here → EUR/USD likely to find RESISTANCE

EUR/USD Pair-Specific Levels in the "resistance" role:
  - Prior swing high: 1.1630 (yfinance)
  - EMA 50: 1.1625 (TradingView)
  - FXStreet: "1.1635 is key resistance"
  - Round number: 1.1650 (psychological)

TRANSLATED ZONE: EUR/USD RESISTANCE at 1.1625-1.1650 | HEAVY (10/14 transferred)
Source: Pair-specific data
```

### 9.9 LSZ Direction Inversion Rules

Liquidity Sweep Zones invert their direction when translated from DXY to pairs:

| DXY LSZ Type | Pair LSZ Type | Example |
|:---|:---|:---|
| Demand-side LSZ (below swing low, stops for longs) | Supply-side LSZ (above swing high, stops for shorts) | DXY LSZ at 97.80-97.85 (demand) → EUR/USD LSZ at 1.1700-1.1710 (supply) |
| Supply-side LSZ (above swing high, stops for shorts) | Demand-side LSZ (below swing low, stops for longs) | DXY LSZ at 99.90-99.95 (supply) → EUR/USD LSZ at 1.1400-1.1410 (demand) |

**CRITICAL:** The pair LSZ price levels come from the PAIR's own swing structure, NOT from DXY LSZ levels. The DXY LSZ tells you WHERE liquidity sits in DXY terms. The pair LSZ tells you where liquidity sits in PAIR terms. They are at completely different price levels on completely different scales.

### 9.10 Macro Shape Chain Translation

The macro shape chain translates to pairs with the SAME SHAPES but INVERTED DIRECTION:

| DXY Shape | DXY Direction | Pair Shape | Pair Direction |
|:---|:---|:---|:---|
| SS (range-bound) | Neutral | SS (range-bound) | Neutral |
| BS (upside breakout) | Up | BS (downside breakout) | Down |
| BS (downside breakout) | Down | BS (upside breakout) | Up |
| PBS (upside piercing) | Up strongly | PBS (downside piercing) | Down strongly |
| WL (upward spike then reject down) | Up then Down | WL (downward spike then reject up) | Down then Up |
| RWL (downward reversal after upside BS) | Down | RWL (upward reversal after downside BS) | Up |
| WLS (violent oscillation) | Neutral/oscillating | WLS (violent oscillation) | Neutral/oscillating |

**Weekly Shape Chain Visualization Translation:**

```
DXY: Mon: SS [range] → Tue: BS [up] → Wed: R [consolidation] → Thu: RWL [down] → Fri: SS [range]
EUR/USD: Mon: SS [range] → Tue: BS [down] → Wed: R [consolidation] → Thu: RWL [up] → Fri: SS [range]
GBP/USD: Mon: SS [range] → Tue: BS [down] → Wed: R [consolidation] → Thu: RWL [up] → Fri: SS [range]
AUD/USD: Mon: SS [range] → Tue: BS [down] → Wed: R [consolidation] → Thu: RWL [up] → Fri: SS [range]
```

**IMPORTANT:** The shapes and timing are the same for all three pairs because they all respond to the same USD macro forces. The DIRECTION inverts. The SPECIFIC PRICE LEVELS for each shape's boundaries come from each pair's own data.

### 9.11 Volatility Trigger Translation

Volatility triggers (Treasury auctions, ON RRP, EIA data) affect ALL instruments simultaneously because they are USD-denominated macro events. No translation is needed — the trigger applies equally to DXY and all pairs.

**However, the PAIR-SPECIFIC IMPACT may differ:**
- A strong Treasury auction (high bid-to-cover) strengthens USD → DXY up, EU/GU/AU down
- But AUD/USD may be MORE affected if the trigger also impacts commodity prices (iron ore, etc.)
- And GBP/USD may be LESS affected if BOE is simultaneously hawkish

**Translation rule:** Apply the same volatility trigger framework to each pair, but adjust the impact magnitude based on pair-specific factors. Document any pair-specific amplification or dampening.

### 9.12 Institutional Commentary Translation

Institutional commentary is harvested PAIR-SPECIFICALLY — there is no translation needed because each pair gets its own commentary from its own sources.

**However, DXY commentary can provide ADDITIONAL directional conviction for pairs:**
- If ING says "DXY likely to test 99.50 resistance" → this supports EUR/USD finding support
- If forex.com says "DXY support at 98.00 is key" → this supports EUR/USD facing resistance

**Translation rule:** Include pair-specific commentary as PRIMARY source. Include DXY commentary as SECONDARY directional conviction amplifier. Clearly label the source and role of each.

### 9.13 Cross-Pair Comparison Matrix Format

[See Section 5.4 for the complete format]

**Pair Divergence Rules:**

If a pair's own technicals CONTRADICT the DXY directional implication:

1. **Flag as DIVERGENCE:** "⚠ PAIR DIVERGENCE: [Pair] own technicals suggest [direction] but DXY directional conviction suggests [opposite direction]"
2. **Do NOT override the DXY direction** — DXY is the driver
3. **Note the risk:** "Pair divergence increases uncertainty. DXY direction is primary but this pair may underperform/overperform relative to DXY signal."
4. **Reduce conviction by 2 points** for that pair's translated zone
5. **Example:** If DXY says EUR/USD should find support but EUR/USD is below its 200-day MA with bearish MA consensus → the support zone is still identified but with reduced conviction and a divergence flag

### 9.14 Pair Translation Zero-Tolerance Rules

**RULE T1: NO MATHEMATICAL CONVERSION.** Under NO circumstances may DXY price levels be arithmetically converted to pair price levels. This includes the DXY formula, inverse correlation ratios, pip equivalence, and any other mathematical method. Every pair level in the report MUST come from a pair-specific data source.

**RULE T2: DIRECTION TRANSFERS, NOT LEVELS.** The ONLY thing transferred from DXY to the pair is directional conviction (which zones matter, which direction the move will take). Price levels are ALWAYS pair-specific.

**RULE T3: LAYER 2 VERIFICATION IS MANDATORY.** No translated zone may appear in the pair synthesis without passing Layer 2 verification. Unverified zones are EXCLUDED, not included with reduced confidence.

**RULE T4: CROSS-VALIDATION WITHIN 100 PIPS.** Every translated zone must be within 100 pips of at least one verified structural level on that pair. If a translated zone is more than 100 pips from any verified level, it is UNVERIFIED and EXCLUDED.

**RULE T5: PAIR DATA OVERRIDES DXY DIRECTION AT ZONE EDGES.** If DXY says "support" but the pair's own 200-day MA, swing structure, and institutional commentary all indicate "resistance" at that same structural location, the pair data takes precedence for the ZONE ROLE assignment. DXY still provides directional conviction for the OVERALL direction, but the specific zone classification (support vs resistance) is determined by pair data.

**RULE T6: TEMPORAL BOUNDARY APPLIES TO PAIR DATA.** All pair-specific data must be published before the temporal boundary. This includes pair MA values, pair analyst commentary, and pair spot prices. Pair data published after the boundary is EXCLUDED.

**RULE T7: PAIR TRANSLATION AUDIT TRAIL.** Every translated zone in the report must include:
- The DXY source zone (name, range, pressure degree)
- The translation rule applied (from Section 9.5 mapping table)
- The pair-specific data source(s) for the pair level
- The Layer 2 verification status
- Whether any divergence exists between DXY direction and pair technicals

**Violation of any of these rules is a CRITICAL FAILURE.** The pair translation sections of the report must be regenerated if any zero-tolerance rule is violated.

### 9.15 Pair Translation Audit Trail Requirements

Every translated zone in the report MUST include the following audit trail:

```
TRANSLATED ZONE AUDIT:
  DXY Source: [Zone Name] | [Range] | [Pressure Degree] ([Score]/14) | ZFP: [X]%
  Translation Rule: [from Section 9.5 — e.g., "DXY Resistance → Pair Support"]
  Direction Transfer: [DXY direction] → [Pair direction] (INVERTED/DIRECT/NEUTRAL)
  Conviction Transfer: [DXY score] → [Pair score] ([adjustments if any])
  Pair Level: [Range] | Role: [Support/Resistance/LSZ/etc.]
  Pair Data Sources:
    - MA Confluence: [value] from [TradingView URL]
    - Swing Structure: [H/L/C] from [yfinance]
    - Institutional S/R: [level] from [forex.com URL] + [level] from [ING URL]
    - Options: [strike/notional or "NO PAIR OPTIONS DATA"] from Protocol A
    - Round Number: [level] from [pair price scale]
  Layer 2 Verification: [X]/7 requirements met | Status: [VERIFIED HIGH / VERIFIED MODERATE / PARTIALLY VERIFIED / UNVERIFIED]
  Cross-Validation: Nearest verified structural level = [level], [X] pips from translated zone | Status: [PASS / FAIL]
  Divergence: [None / ⚠ PAIR DIVERGENCE: description]
  Final Status: [INCLUDED / EXCLUDED] | Final Conviction: [score]/14
```

This audit trail is MANDATORY for every translated zone. Its absence is equivalent to data fabrication — the reader must be able to verify every pair level against its pair-specific source.

---

## FORBIDDEN

- Computing pair levels from DXY levels using the DXY formula in reverse (e.g., DXY 98.50 → EUR/USD = (K/98.50)^1.7361 = 1.1295)
- Applying a fixed multiplier or ratio to convert DXY ranges to pair ranges (e.g., 0.25 DXY points × 100 = 25 pips)
- Subtracting DXY levels from a constant to get pair levels (e.g., 100 − 98.50 = 1.50 → EUR/USD 1.1500)
- Applying a percentage of a DXY move to a pair price (e.g., DXY −0.5% → pair +0.5% from spot)
- Converting DXY points to "equivalent pips" on a pair (e.g., 0.25 DXY points ≈ 50 pips)
- Including any translated zone in pair synthesis without passing Layer 2 verification
- Including a translated zone more than 100 pips from any verified structural level on that pair
- Using pair data published after the temporal boundary (all pair MA values, commentary, spot prices)
- Omitting the Translated Zone Audit (Sec 9.15) for any translated zone — absence equals data fabrication
- Treating a pair divergence as an invalidation or overriding DXY direction with pair technicals (divergences are RISK FACTORS only; reduce conviction by 2, flag, do not override)
- Delivering a report missing the Data As-Of line (invalidates the entire report)
- Delivering a report that fails ANY Blind-Execution check BE1–BE12 without revision
- Referencing any external resource for trade execution (e.g., "check TradingView for confirmation")

---

## SOURCE ANCHORS

Every anchor below was verified by printing the referenced line (never fabricated).

- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:1693` — §5.5 Blind-Execution Protocol
- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:3257` — Part IX — Multi-Pair Translation Protocol
- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:3336` — §9.3 PROHIBITED methods
