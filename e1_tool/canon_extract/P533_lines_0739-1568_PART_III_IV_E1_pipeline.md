## PART III: DATA HARVESTING PIPELINE — BROWSER + VLM ARCHITECTURE

### 3.1 Execution Model: Single-Agent Sequential Pipeline

**DO NOT use subagents.** Subagent cold-start overhead (30-60s each × 7 agents) makes parallel execution *slower* than sequential. Run all protocols in a single agent, one after another.

**Source Pre-Classification (HARDCODED — do not re-discover at runtime):**

| Status | Source | Reason |
|:---|:---|:---|
| ✅ ACCESSIBLE | investinglive.com (via `z-ai page_reader` API) | Returns HTML; extract image URL, download image, VLM |
| ✅ ACCESSIBLE | TreasuryDirect API (`/TA_WS/securities/auctioned`) | JSON API, no auth needed |
| ✅ ACCESSIBLE | FRED CSV (`fredgraph.csv?id=RRPONTTLD`) | Public CSV download |
| ✅ ACCESSIBLE | EIA WPSR Summary (`ir.eia.gov/wpsr/wpsrsummary.pdf`) | Public PDF |
| ✅ ACCESSIBLE | ForexFactory (via `z-ai page_reader` API) | Returns HTML |
| ✅ ACCESSIBLE | Fed H.10 Exchange Rates (`federalreserve.gov/releases/h10/current`) | Returns HTML with 5-day rates for all DXY components |
| ✅ ACCESSIBLE | Yahoo Finance DXY Historical (`finance.yahoo.com/quote/DX-Y.NYB/history`) | Prior week AND prior day HLC for pivot calculations |
| ✅ ACCESSIBLE | yfinance Python library (`DX-Y.NYB`, `interval='1h'`, aggregate to 4H) | 4H OHLC data for 4H zone scanning (Step 0f) — programmatic extraction |
| ✅ ACCESSIBLE | TradingView DXY Technicals (`tradingview.com/symbols/TVC-DXY/technicals/`) | EMA/SMA values for MA Confluence Grid |
| ✅ ACCESSIBLE | forex.com Institutional Research (`forex.com/en-us/market-analysis/latest-research/`) | Weekly DXY forecast with HWC/LWC levels |
| ✅ ACCESSIBLE | Web Search via z-ai | Institutional commentary from ING, FXStreet, VT Markets, Continuum Economics |
| ✅ ACCESSIBLE | TradingView EUR/USD Technicals (`tradingview.com/symbols/EURUSD/technicals/`) | EMA/SMA values for EUR/USD |
| ✅ ACCESSIBLE | TradingView GBP/USD Technicals (`tradingview.com/symbols/GBPUSD/technicals/`) | EMA/SMA values for GBP/USD |
| ✅ ACCESSIBLE | TradingView AUD/USD Technicals (`tradingview.com/symbols/AUDUSD/technicals/`) | EMA/SMA values for AUD/USD |
| ✅ ACCESSIBLE | forex.com EUR/USD Research (`forex.com/en-us/market-analysis/latest-research/`) | Weekly EUR/USD forecast |
| ✅ ACCESSIBLE | forex.com GBP/USD Research (`forex.com/en-us/market-analysis/latest-research/`) | Weekly GBP/USD forecast |
| ✅ ACCESSIBLE | forex.com AUD/USD Research (`forex.com/en-us/market-analysis/latest-research/`) | Weekly AUD/USD forecast |
| ✅ ACCESSIBLE | yfinance Python library for pairs (`EURUSD=X`, `GBPUSD=X`, `AUDUSD=X`, `interval='1h'`) | 4H OHLC data for pair zone scanning |
| ✅ ACCESSIBLE | Web Search for pair institutional commentary | ING, FXStreet, VT Markets commentary on EUR/USD, GBP/USD, AUD/USD |
| ⚠️ UNSTABLE | ICE Futures US — DXY EOD Report (`ice.com/products/1216/US-Dollar-Index-Options`) | Supplementary to Protocol B; attempt via page_reader first |
| ⚠️ UNSTABLE | CME QuikStrike API / Barchart Institutional Feed (`DX` contract root) | May return 403 or require paid API; attempt via page_reader first |
| 🔴 BLOCKED | CME Group direct (403 IP block) | Do NOT attempt — instant fail |
| 🔴 BLOCKED | Barchart retail (CDN block + paid API) | Do NOT attempt — instant fail |
| 🔴 BLOCKED | Investing.com (Cloudflare block) | Do NOT attempt — instant fail |
| 🔴 BLOCKED | CME Daily Bulletin S3 (AccessDenied) | Do NOT attempt — instant fail |
| 🔴 BLOCKED | Yahoo Finance UUP ETF options | **PERMANENTLY TERMINATED** — UUP is NOT DXY |

**Blocked source rule:** If a source is marked BLOCKED above, mark that protocol `[NO DATA — source blocked from this environment]` immediately. Do NOT attempt to find alternatives. Zero retry. Zero exploration. Move on.

**Execution Sequence (must follow this exact order):**

| Step | Protocol | Method | Target Time |
|:---|:---|:---|:---|
| 1 | A — OTC FX Expiries | page_reader → image download → VLM 3-pass → **Filter Checkpoint** | 2 min |
| 2 | B — DXY 9-Pillar 6D Hybrid Zone Map | page_reader → multi-source extraction → convert Protocol A strikes → Structural Extreme Scan + 4H Zone Scan + Regime Detection + Measured Move + 4H Overlay | 5 min |
| 3 | C1/C2/C3 — CME FX OI | SKIP (BLOCKED) | 0 sec |
| 4 | D — Treasury Auctions | TreasuryDirect API (curl) | 30 sec |
| 5 | E — ON RRP | FRED CSV (curl) | 30 sec |
| 6 | F — Economic Calendar | page_reader (ForexFactory) | 30 sec |
| 7 | G — EIA Petroleum | EIA PDF (curl) | 30 sec |
| 8 | Reconcile + Calculate offsets | In-memory | 15 sec |
| 9 | Engine 2 — Macro Shape Chain Map | Forward Mapping Procedure + Session/Day Decomposition | 2-3 min |
| 9.5 | Engine 3 — Trade Setup Architecture | POI filtering + Direction Validation + Entry/SL/TP + Confluence Scoring + Multi-Setup Architecture | 2 min |
| 10 | **Pair Data Harvesting (v5.0.0)** | TradingView + forex.com + web search + yfinance for each pair | 4 min |
| 11 | **Layer 1 Translation (v5.0.0)** | Apply Part IX translation rules to each pair | 2 min |
| 12 | **Layer 2 Verification (v5.0.0)** | Cross-validate translated levels against pair-specific data | 2 min |
| 13 | **Cross-Pair Matrix (v5.0.0)** | Assemble comparison matrix | 1 min |
| 14 | Generate PDF | Pre-built ReportLab template | 30 sec |
| 15 | **Compliance Sweep (v5.0.0)** | Post-generation verification | 1 min |
| 16 | **Pine Script Code Generation (v5.1.0)** | Generate v6 Pine Script from verified report data | 1 min |
| 17 | **Pine Script Verification (v5.1.0)** | 8-point verification check on generated code | 30 sec |
| **Total** | | | **~26 min** |

### 3.2 Protocol-Specific Extraction Procedures

Each protocol below specifies: the website, how to navigate it, how to extract data (browser snapshot vs. VLM image reading vs. static HTML), and how to construct the verified source URL.

---

#### PROTOCOL A — OTC FX OPTION EXPIRIES (PRIMARY SOURCE)

**Source:** `https://investinglive.com/Orders/`
**Data Format:** Embedded image on a date-specific sub-page
**Extraction Method:** `z-ai page_reader` → image URL extraction → image download → VLM 3-pass → **Filter Checkpoint (v5.0.0)**
**DO NOT use `agent-browser`** — investinglive.com blocks headless browsers with 403/CloudFront. Use `z-ai page_reader` API instead.

**Step-by-step procedure:**

1. **Fetch the Orders index page via page_reader:**
   ```bash
   z-ai page_reader --url "https://investinglive.com/Orders/" --output /tmp/protocol_a_index.json
   ```
   Parse the output for links matching the target date pattern:
   `fx-option-expiries-for-DD-MMM-10am-new-york-cut-YYYYMMDD`
   Example: `fx-option-expiries-for-22-may-10am-new-york-cut-20260522`

2. **Fetch the date-specific sub-page via page_reader:**
   ```bash
   z-ai page_reader --url "https://investinglive.com/Orders/fx-option-expiries-for-[DD]-[MMM]-10am-new-york-cut-[YYYYMMDD]/" --output /tmp/protocol_a_page.json
   ```
   The exact URL becomes the source URL for the report.

3. **Extract the embedded data image URL** from the page content. Download it:
   ```bash
   curl -sL "[IMAGE_URL]" -o /tmp/protocol_a_table.png
   ```

4. **VLM 3-Pass Extraction (MANDATORY — do NOT skip any pass):**

   **Pass 1 — Full Table Extraction:**
   ```bash
   z-ai vision -p "You are a quant analyst performing OCR on an FX option expiries table. Extract ALL data from this image with pixel-perfect accuracy. For every row, extract: the currency pair, the strike price, and the notional amount (in billions or millions as shown). Output as a structured table. Do NOT hallucinate any values — only include what is actually visible in the image. If a value is unclear, mark it as [UNCLEAR]." -i /tmp/protocol_a_table.png
   ```

   **Pass 2 — Targeted Verification:**
   ```bash
   z-ai vision -p "Verify these specific data points from the image. Answer ONLY with the exact digits you see — no guessing: 1) List every EUR/USD strike and its exact notional. 2) List every USD/JPY strike and its exact notional. 3) List every GBP/USD strike and its exact notional. 4) List every AUD/USD strike and its exact notional. 5) List every NZD/USD strike and its exact notional. 6) List every USD/CAD strike and its exact notional. 7) List every USD/CHF strike and its exact notional. 8) List every EUR/GBP strike and its exact notional. 9) What spot prices are shown for each pair? For each, state the exact value or say NOT VISIBLE." -i /tmp/protocol_a_table.png
   ```

   **Pass 3 — Cross-Check:**
   ```bash
   z-ai vision -p "Cross-check this image for the following specific data points. For each, confirm EXACTLY what you see, or state DOES NOT EXIST if the item is not present: 1) Is there a strike at [each strike from Pass 1]? What notional? 2) Are there any strikes I missed in Pass 1? 3) For any pair that showed no expiries, confirm: are there truly no expiries, or did I miss them?" -i /tmp/protocol_a_table.png
   ```

5. **Reconcile the 3 passes.** A data point is CONFIRMED only if at least 2 of 3 passes agree. If passes conflict, mark the data point `[UNCLEAR — NEEDS MANUAL CONFIRM]` and do NOT include it in calculations.

6. **⚠ FILTER CHECKPOINT (v5.0.0 — MANDATORY — Execute BEFORE data entry):**

   After reconciling VLM passes and BEFORE entering any data into report structures:

   **Step 6a — Pair Filter (R1):** Isolate ONLY EUR/USD, GBP/USD, AUD/USD strikes for OTC expiry summary tables. All other pairs (USD/JPY, USD/CAD, USD/CHF, USD/SEK, NZD/USD, EUR/GBP) are routed to Pillar 3 conversion ONLY — they do NOT appear in the OTC expiry summary.

   **Step 6b — Notional Filter (R2):** Apply the three-tier classification:

   | Tier | Notional Range | Classification | Report Treatment |
   |:---|:---|:---|:---|
   | 1 | ≥ $1.5B equivalent | **CRITICAL OPTION WALL** | INCLUDED in all tables and zone maps |
   | 2 | $850M – $1.499B equivalent | **SIGNIFICANT MAGNET** | INCLUDED in all tables and zone maps |
   | 3 | < $850M equivalent | **EXCLUDED** | NOT included in summary tables. Routed to Pillar 3 conversion only. Override possible ONLY with 3+ pillar confluence + Pillar 5 Step 0/0.5 validation (document justification). |

   **Step 6c — Record Filter Checkpoint:**
   ```
   Filter Checkpoint: [Day] [Date]
   Raw strikes from VLM: [X] strikes across [Y] pairs
   After Pair Filter (R1): [A] strikes (EU/GU/AU only)
   After Notional Filter (R2): [B] strikes (≥$850M only)
   Excluded: [C] strikes below $850M, [D] strikes from non-R1 pairs
   Override inclusions: [E] strikes (list each with justification)
   Final included: [F] strikes
   ```

7. **Filter Audit Line (v5.0.0 — MANDATORY on every expiry table):**

   Every OTC expiry table in the report MUST include this audit line as the LAST row:
   ```
   ─────────────────────────────────────────────────────────────────
   FILTER AUDIT: [X] raw → [Y] after pair filter (EU/GU/AU only) → [Z] after ≥$850M filter → [W] final | Excluded: [list excluded strikes with pairs and notionals]
   ─────────────────────────────────────────────────────────────────
   ```

**MISSING DAY HANDLING RULE:**

OTC option expiry images are published for each individual trading day (Monday through Friday). If no expiry image exists for a specific day within the target week:

- **Mark that day as `[NO DATA — No OTC expiry data available for [day name]]`.**
- **NEVER assume or fabricate what the expiry data might contain.**
- **NEVER use the previous day's expiry data as a proxy for the missing day.**
- **State explicitly in the report:** "No option cage exists for [day name] based on available data. IL levels for this day are derived from structural pillars only (no options-derived dimension)."
- **If the missing day is within the target week:** The structural pillars (Pillar 1 pivots, Pillar 2 MAs, Pillar 5 extremes, etc.) still apply. Only the options-derived dimension (Pillar 3 and Pillar 8) is degraded for that specific day.

**⚠ TEMPORAL BOUNDARY ENFORCEMENT FOR FX OPTIONS (v4.5.1 FIX #5 — ZERO TOLERANCE):**

The temporal boundary applies STRICTLY to FX option expiry data. Only data published on or before the temporal boundary date may be included.

**Rule:** If operating as the morning of Day 1 of the target week:
- **Day 1 (Monday) expiry data:** INCLUDED if published on the boundary date or before
- **Day 2 (Tuesday) expiry data:** INCLUDED ONLY IF the Day 1 page contains forward-looking data for Day 2
- **Day 3+ (Wed-Fri) expiry data:** EXCLUDED unless the Day 1 page explicitly contains forward-looking data for those days
- **If only Day 1 and Day 2 data exists at the temporal boundary:** Mark Day 3-5 as `[NO DATA — option expiry not yet published for [day name] as of temporal boundary]`

**AUDIT TRAIL for each day's option data:**
```
[Day Name] Option Data: [INCLUDED/EXCLUDED]
  Source: [exact URL of the page where data was found]
  Published Date: [date the page was published]
  Temporal Boundary: [boundary date]
  Status: [published before boundary = INCLUDED / published after boundary = EXCLUDED / forward data on boundary page = INCLUDED]
```

**Output:** Verified OTC expiry table + exact source URL + Filter Checkpoint + Filter Audit Line + explicit notation of any missing days + temporal boundary audit trail for each day's data.

---

#### PROTOCOL B — DXY INSTITUTIONAL PRESSURE ZONE MAP (9-PILLAR 6D HYBRID SYSTEM WITH LIQUIDITY ENGINEERING)

**METHODOLOGY OVERVIEW:** DXY has no 10am daily FX option expiry like other pairs. Institutional pressure zones are mapped using a 9-Pillar approach across 6 independent dimensions (Technical, Options-Derived, Analyst Consensus, Structural, Psychological, Regime/Dynamic) plus a Structural Extreme Bonus system.

**The UUP ETF proxy is permanently terminated.** Do NOT substitute any equity ETF at any step.

**DXY FORMULA (for component pair conversion):**
```
DXY = 50.14348112 × EURUSD^(-0.576) × USDJPY^(0.136) × GBPUSD^(-0.119) × USDCAD^(0.091) × USDSEK^(0.042) × USDCHF^(0.036)
```

**Component Pair Weights:**
| Pair | Weight | Direction | Per-Pip DXY Impact | % of Total |
|:---|:---|:---|:---|:---|
| EUR/USD | -0.576 (57.6%) | Inverse | ~0.048 pts/pip | **62.4%** |
| USD/JPY | +0.136 (13.6%) | Direct | ~0.009 pts/pip | 11.9% |
| GBP/USD | -0.119 (11.9%) | Inverse | ~0.009 pts/pip | 11.3% |
| USD/CAD | +0.091 (9.1%) | Direct | ~0.006 pts/pip | 8.4% |
| USD/SEK | +0.042 (4.2%) | Direct | ~0.0004 pts/pip | 0.5% |
| USD/CHF | +0.036 (3.6%) | Direct | ~0.004 pts/pip | 5.4% |

**EUR/USD DOMINANCE:** EUR/USD is 5.2× more impactful per pip than the next component (USD/JPY). This is why Pillar 8 exists — to exploit this dominance.

**Simplified DXY formula for EUR/USD primary conversion:**
```
DXY = K × EURUSD^(-0.576)

Where K = 50.14348112 × USDJPY^(0.136) × GBPUSD^(-0.119) × USDCAD^(0.091) × USDSEK^(0.042) × USDCHF^(0.036)

Reverse: EURUSD_strike = (K / DXY_target)^(1/0.576) = (K / DXY_target)^1.7361
```

**6 DIMENSIONS OF INDEPENDENCE:**

| Dimension | Data Source | Failure Mode | Recovery |
|:---|:---|:---|:---|
| Technical (price-derived) | Prior OHLC (extended history) | Regime change | Options + Analyst |
| Options-Derived (positioning-derived) | OTC strikes, EUR/USD primary | Low volume days | Technical + Structural |
| Analyst Consensus (intelligence-derived) | Institutional research | Herding/lag | Technical + Options |
| Structural (microstructure-derived) | Prior closes, HWC/LWC, extremes | Obsolete levels | Options + Psychological |
| Psychological (behavior-derived) | Round numbers | Volatility override | Technical + Structural |
| Regime/Dynamic | Macro catalysts, momentum, cross-pair | False breakout | Technical + Options |

---

**PILLAR 1: MULTI-TIMEFRAME PIVOT ENGINE (EXTENDED DEPTH + MULTIPLE DAILY COMPUTATION)**

The single most powerful pillar. 3 pivot variants × 2 timeframes = 6 complete pivot sets (42 calculated levels). Independently captures 8/11 verified levels.

**Data Source:** Prior week + prior day DXY High, Low, Close from Yahoo Finance. For extended depth, also retrieve:
- Last 4-8 weeks of weekly OHLC for structural pivot levels
- Any prior week where DXY traded near the current range (search backwards up to 4 months)
- On 4H timeframe, occasionally need data from up to 4 years prior (rare but documented)
```bash
z-ai page_reader --url "https://finance.yahoo.com/quote/DX-Y.NYB/history" --output /tmp/protocol_b_yahoo.json
```

**Step-by-step procedure:**

1. **Extract prior week AND prior day DXY OHLC** (H, L, C for each timeframe).

2. **Extract daily OHLC for EACH of the last 5 trading days of the prior week.** Do NOT limit daily data extraction to only the last trading day. Each day's H, L, C produces a distinct set of daily pivot levels that may reveal levels missed by the weekly pivot set. Record each day's H, L, C separately.

3. **Check if current DXY range overlaps with any historical range from the past 2-4 months.** If yes, retrieve that period's OHLC for additional pivot calculations.

4. **Calculate Classic Pivots:**
   ```
   PP = (H + L + C) / 3
   R1 = 2 × PP - L      S1 = 2 × PP - H
   R2 = PP + (H - L)     S2 = PP - (H - L)
   R3 = H + 2 × (PP - L) S3 = L - 2 × (H - PP)
   ```

5. **Calculate Fibonacci Pivots:**
   ```
   PP = (H + L + C) / 3
   R1 = PP + 0.382 × (H - L)   S1 = PP - 0.382 × (H - L)
   R2 = PP + 0.618 × (H - L)   S2 = PP - 0.618 × (H - L)
   R3 = PP + 1.000 × (H - L)   S3 = PP - 1.000 × (H - L)
   ```

6. **Calculate Camarilla Pivots:**
   ```
   R4 = C + (H - L) × 1.1 / 2     S4 = C - (H - L) × 1.1 / 2
   R3 = C + (H - L) × 1.1 / 4     S3 = C - (H - L) × 1.1 / 4
   R2 = C + (H - L) × 1.1 / 6     S2 = C - (H - L) × 1.1 / 6
   R1 = C + (H - L) × 1.1 / 12    S1 = C - (H - L) × 1.1 / 12
   ```

7. **Calculate ALL pivot sets for:**
   - Weekly timeframe (3 variants) using the prior week's H, L, C
   - Daily timeframe (3 variants) for EACH of the last 3 trading days (not just the last day)
   - Any historical weeks identified in step 3
   - **DO NOT filter by spot proximity.** Retain ALL calculated levels. The spot price is irrelevant to level validity (see Section 2.3).

8. **MANDATORY PIVOT VERIFICATION (CRITICAL — DO NOT SKIP):**

   After computing each pivot set, you MUST verify the arithmetic using these checks. If ANY check fails, recompute the entire set from scratch.

   **Formula Verification Check (ALL variants):**
   ```
   For each computed level, verify the formula was applied correctly:
   - R1 = 2×PP - L  →  confirm R1 + L = 2×PP
   - S1 = 2×PP - H  →  confirm S1 + H = 2×PP
   - R2 = PP + (H-L)  →  confirm R2 - PP = H - L
   - S2 = PP - (H-L)  →  confirm PP - S2 = H - L
   ```
   This catches the most common errors: swapping R1/S1 formulas, using H-L instead of PP-L.

   **Symmetry Check (Fibonacci ONLY — does NOT apply to Classic Pivots):**
   ```
   For Fibonacci Pivots: R1 - PP MUST equal PP - S1 (both equal 0.382 × (H-L))
   For Fibonacci Pivots: R2 - PP MUST equal PP - S2 (both equal 0.618 × (H-L))
   ```
   ⚠ CRITICAL: Classic Pivots are ASYMMETRIC by design. Do NOT flag a Classic pivot as wrong based on R1-PP ≠ PP-S1.

   **Sanity Check (ALL variants):**
   ```
   R1 > PP > S1  (must be true for all pivot variants)
   R2 > R1 > PP  (must be true for all pivot variants)
   S1 > S2 > S3  (must be true for all pivot variants)
   ```

   **Range Consistency Check:**
   ```
   For Classic Pivots: R2 - S2 MUST equal 2 × (H - L)
   For Fibonacci Pivots: R2 - S2 MUST equal 1.236 × (H - L)
   For Camarilla Pivots: R4 - S4 MUST equal (H - L) × 1.1
   ```

   **Output the verification results** as part of the audit trail:
   ```
   Pivot Verification: [timeframe] [variant] — H=[H] L=[L] C=[C]
   PP=[PP] R1=[R1] S1=[S1] | R1+L=[val] 2×PP=[val] | FORMULA: [PASS/FAIL]
   R1>PP>S1: [PASS/FAIL] | R2-S2=[range] 2×(H-L)=[prior_range] | RANGE CHECK: [PASS/FAIL]
   ```

9. **Scoring:** Exact match within 3 pips = 2 pts (Technical dimension); Zone match within 10 pips = 1 pt. Levels from extended historical data that coincide with current levels get a LEGACY BONUS of +0.5.

---

‖‖‖ **PAGE BREAK** ‖‖‖

**PILLAR 2: MOVING AVERAGE CONFLUENCE GRID**

Full MA stack with weighted confluence scoring and recapture detection. Independently captures 3-4/11 levels.

```

**Step-by-step procedure:**

1. **Extract ALL available MA values:** EMA/SMA 9, 10, 20, 50, 100, 200.

2. **Detect confluence clusters** where 3+ MAs converge within 0.15 DXY points.

3. **MA Weighting System:**
   | MA | Weight | Rationale |
   |:---|:---|:---|
   | EMA/SMA 200 | 3.0 | Structural anchor — bull/bear separator |
   | EMA/SMA 100 | 2.0 | Long-term trend — 5 months of price history |
   | EMA/SMA 50 | 1.5 | Institutional position builder |
   | EMA/SMA 20 | 1.0 | Smart money average |
   | EMA 9/10 | 0.5 | Short-term momentum |

4. **Recapture Detection:** If price recently (within 3 sessions) crossed above a major MA (50, 100, 200), flag that level as RECAPTURE ZONE with +2 bonus to confluence score. The recaptured MA becomes the most important support level.

5. **Scoring:** Triple+ cluster = 2 pts (Technical dimension); Double cluster = 1 pt; Single MA = 0.5 pts.

---

**PILLAR 3: COMPONENT PAIR OPTION EXPIRY CONVERSION (SECONDARY)**

Converts major option expiry strikes from DXY component pairs into DXY equivalents using the formula. Serves as SECONDARY to Pillar 8 for EUR/USD, and PRIMARY for the other 5 pairs.

**Pillar 3 is mandatory.** If rate limits prevent execution, WAIT for rate limit reset. Pillar 3 data (especially EUR/USD option expiry strikes) is the primary input for Pillar 8.

**Data Source:** Re-use Protocol A OTC expiry data (investinglive.com) + Fed H.10 spot rates.
```bash
z-ai page_reader --url "https://www.federalreserve.gov/releases/h10/current" --output /tmp/protocol_b_h10.json
```

**Step-by-step procedure:**

1. **From Protocol A data, isolate DXY component pair strikes** (EUR/USD, USD/JPY, GBP/USD, USD/CAD, USD/CHF, USD/SEK).

2. **Get spot prices for all 6 component pairs from Fed H.10.**

3. **H.10 COMPONENT DATA FALLBACK PROCEDURE:**

   The Fed H.10 publication provides 5-day rolling rates but may occasionally be missing data for specific component pairs. If H.10 data is incomplete:

   a. **Search for supplementary spot rates** via web search: `"GBP/USD spot rate [current date]"` or `"USD/CHF exchange rate today"`
   b. **Use the supplementary rate for K factor computation** but flag the source
   c. **Widen the confidence band proportionally** for any Pillar 8 conversions that rely on a supplementary rate:
      - 1 pair using supplementary data: Widen confidence band by +0.03 DXY points
      - 2 pairs using supplementary data: Widen confidence band by +0.07 DXY points
      - 3+ pairs using supplementary data: Pillar 8 confidence degrades to LOW
   d. **NEVER fabricate a spot rate.**

4. **For each LARGE expiry (>= USD 500M equivalent), calculate DXY equivalent:**
   - Hold all other pairs at current spot
   - Vary ONLY the pair with the expiry to its strike price
   - Calculate: `DXY_equiv = 50.14348112 × strike_EURUSD^(-0.576) × spot_USDJPY^(0.136) × ...`
   - This produces the DXY level where that option wall exerts maximum magnetic pull

5. **Classify by notional size — THREE-TIER SYSTEM (v5.0.0 DERAILMENT FIX D2):**

| Tier | Notional | Classification | Default |
|:---|:---|:---|:---|
| 1 | ≥ $1.5B equivalent | **CRITICAL OPTION WALL** | INCLUDE — always |
| 2 | $850M – $1.499B equivalent | **SIGNIFICANT MAGNET** | INCLUDE — always |
| 3 | < $850M equivalent | **EXCLUDED** | EXCLUDE from summary tables and zone maps. Override ONLY with 3+ pillar confluence + Pillar 5 Step 0/0.5 validation |

**⚠ CRITICAL CHANGE FROM v4.5.2:** The old Tier 2 ("SIGNIFICANT MAGNET", $900M-$1.0B) and Tier 3 ("CONDITIONAL MAGNET", $500M-$900M) have been REPLACED. The threshold is now $850M, not $500M. The label "SIGNIFICANT MAGNET" now applies to $850M-$1.499B (previously $900M-$1.0B in v4.5.2, then $850M-$999M in v5.0.0; v5.2.0 expands range to $850M-$1.499B after CRITICAL OPTION WALL threshold raised from ≥$1B to ≥$1.5B). Strikes below $850M are EXCLUDED by default — they are NOT "CONDITIONAL MAGNET" and they are NOT "NOISE" — they are simply EXCLUDED unless they meet the strict override criteria. This prevents the over-inclusion bias that caused the May 25-29 derailment.

**Confluence Score Adjustments:**
- Tier 1 (CRITICAL OPTION WALL): Options-Derived dimension score = 2 (maximum), confluence score +3
- Tier 2 (SIGNIFICANT MAGNET): Options-Derived dimension score = 2, confluence score +2
- Tier 3 Override (EXCLUDED but overridden): Options-Derived dimension score = 1, confluence score +1

**AUDIT TRAIL:** For any Tier 3 inclusion via override, the report MUST state: "[STRIKE] [NOTIONAL] included via structural override: [Pillar 5 validation] + [X] pillar confluence"


### BoM/MoM Zone Classification (NEW — CRITICAL)

For every IP zone, classify as **BoM (Beginning of Move)** or **MoM (Middle of Move)**:
- **BoM**: The zone that ORIGINATED the directional move — the FIRST zone at the start of a trend leg. Identified by: zone is at the beginning of a clear impulse move, price left the zone with momentum, the zone is the "source" of the move.
- **MoM**: A zone that formed MID-MOVE as a continuation — not the origin, but a reaction point along the path. Identified by: zone formed during an ongoing move, not at the start, price paused here then continued.
- **BoM zones**: Mark as `ENTRY-PRIMARY` in Engine 3. 100% guaranteed reaction if unmitigated.
- **MoM zones**: Mark as `TP-TARGET` for opposing direction in Engine 3. Entry ONLY with exceptions (see Engine 3 Phase 1).
- **4H MoM specific**: Mark as `ONE-AND-DONE` — first retest = minor reaction, then likely strong pierce. Not valid for swing entries.

### Zone Reaction Counter (NEW — CRITICAL)

For each IP zone, track the number of strong reactions observed:
- **0 reactions (Virgin)**: Zone has never been tested. Strongest if BoM (100% guaranteed reaction). DEATH ZONE if MoM (unpredictable reaction — could be minor then pierce).
- **1-2 reactions (Active)**: Zone still has juice. Valid for entries if BoM. Valid for entries if MoM with exceptions. Still likely to cause a reaction.
- **3+ reactions (Depleted)**: Zone is likely to fail on next test. Use for TP targeting only — NOT for entries. If zone is at 3+ reactions and is between current PA and a deeper BoM zone, price will likely pierce through it to reach the BoM zone.

**Priority rule**: If a pressure zone with juice (1-2 reactions) exists between current PA and the BoM zone, assume price will fully liquidate this initial pressure zone before touching the BoM zone. Use the pressure zone with juice for entries/TPs. Leave the deeper BoM zone for later.

6. **CRITICAL:** EUR/USD strikes calculated here are the PRIMARY input for Pillar 8. Do NOT treat EUR/USD conversion output from Pillar 3 as the final word — feed it into Pillar 8 for primary weighting.

7. **For the other 5 pairs** (USD/JPY, GBP/USD, USD/CAD, USD/CHF, USD/SEK), Pillar 3 remains the primary options-derived signal. These pairs collectively account for only 37.6% of per-pip DXY sensitivity, so their conversion provides secondary zone awareness only.

---

**PILLAR 4: INSTITUTIONAL COMMENTARY HARVESTING**

[unchanged from v4.5.2 — web search for DXY institutional commentary, extract explicit S/R levels, classify by source tier, temporal boundary applies]

**Data Source:** Web search for institutional DXY research.

**TEMPORAL BOUNDARY APPLIES:** Only use analyst commentary that was published BEFORE the temporal boundary.

**Step-by-step procedure:**

1. **Execute web searches for DXY institutional commentary:**
   ```
   Search 1: "DXY dollar index outlook [current month year]" — prioritize results from ING, forex.com
   Search 2: "US dollar index forecast support resistance" — prioritize results from FXStreet, VT Markets, TradingView
   Search 3: "DXY technical analysis weekly" — prioritize results from forex.com, Continuum Economics
   ```

2. **Extract EXPLICIT S/R levels only.** Only include levels that are explicitly stated by the analyst. Do NOT infer levels from narrative descriptions.

3. **Record exact source URL for every extracted level.**

4. **Classify each level by source tier:**
   | Tier | Source | Weight |
   |:---|:---|:---|
   | 1 (Primary) | ING Economics, forex.com (Matt Weller CMT) | 3.0 |
   | 2 (Secondary) | FXStreet, TradingView Community, VT Markets | 2.0 |
   | 3 (Supplementary) | Continuum Economics, OneUpTrader | 1.0 |

5. **Flag levels appearing in 2+ independent sources as ANALYST CONSENSUS.**

6. **Scoring:** 2+ Tier-1 sources agree = 2 pts (Analyst dimension); 1 source = 1 pt; no coverage = 0 pts.

---

‖‖‖ **PAGE BREAK** ‖‖‖

**PILLAR 5: STRUCTURAL EXTREME SCAN, PRICE ANCHORS & LIQUIDITY ENGINEERING**

Harvests exact prior swing lows/highs, HTF order blocks, repeated extreme magnets, prior session closes, HWC/LWC confluences, AND structural extreme memory. This pillar has mandatory pre-computation steps (Step 0, Step 0.5, Step 0.6) that run BEFORE all other Pillar 5 steps.

**ANTI-SLOP RULE:** The system is FORBIDDEN from estimating behavioral ranges (e.g., "often sweeps 10-20 pips", "typically extends 0.5-1.0 of the range"). Every floor and ceiling level MUST come from exact, date-stamped, verifiable historical price data.

**Data Source:** TradingView OHLC (90-day 4H/D1 historical) + forex.com institutional research + web search for macro events.

**STEP 0: 90-DAY STRUCTURAL EXTREME SCAN (MANDATORY — RUN FIRST, BEFORE ALL OTHER STEPS)**

This step is MANDATORY and must execute before any other Pillar 5 computation. It identifies the exact prior swing lows and highs that institutions use as liquidity sweep targets and breakout extension targets.

0a. **Retrieve 90 days of DXY daily (D1) OHLC data** from Trading View. Record every day's Open, High, Low, Close.

**180-DAY CONDITIONAL EXTENSION:** If the current DXY range overlaps with a range from 90-180 days ago (i.e., current DXY is within 1.0 points of a level that was a significant swing extreme in that period), extend the scan to 180 days. Prior swing levels from that extended period receive a LEGACY BONUS of +0.5.

0b. **Identify Swing Lows with Rejection Wicks (Liquidity Sweep Targets):**
   - Scan the 90-day D1 data for all swing lows where the daily low has a significant rejection wick (the candle body closes significantly above the low, indicating buying pressure rejected the move lower).
   - **Rejection wick criteria:** The lower wick must be ≥ 0.15 DXY points AND the close must be in the upper 50% of the daily range.
   - For each identified swing low, record: exact price, date, wick size, and the subsequent price action.
   - **Tag each as "Liquidity Sweep Target"** — these are the exact prices where institutions previously defended support.
   - **CRITICAL:** The exact price of a prior swing low is the PRIMARY liquidity sweep target. Not a range, not an estimate — the EXACT price.

0c. **Identify Swing Highs with Rejection Wicks (Supply Ceiling Targets):**
   - Scan the 90-day D1 data for all swing highs where the daily high has a significant rejection wick.
   - **Rejection wick criteria:** The upper wick must be ≥ 0.15 DXY points AND the close must be in the lower 50% of the daily range.
   - For each identified swing high, record: exact price, date, wick size, and the subsequent price action.
   - **Tag each as "Supply Ceiling Target"** — these are the exact prices where institutions previously defended resistance.

0d. **Identify HTF Order Blocks (4H/D1 Demand and Supply Zones):**
   - On the Daily (D1) timeframe, identify **Demand Zones**: the base of strong bullish candle clusters (1-3 consecutive bullish candles with large bodies) that preceded a sustained rally of ≥ 1.0 DXY points lasting ≥ 5 trading days. Record the zone as [Low of base, High of base] with start and end dates.
   - On the Daily (D1) timeframe, identify **Supply Zones**: the top of strong bearish candle clusters (1-3 consecutive bearish candles with large bodies) that preceded a sustained decline of ≥ 1.0 DXY points lasting ≥ 5 trading days. Record the zone as [Low of top, High of top] with start and end dates.
   - **Tag with conviction level:** If the move from the order block was ≥ 2.0 DXY points and lasted ≥ 10 trading days, tag as "High-Conviction Order Block."

0e. **Cross-Reference Swing Extremes with Order Blocks:**
   - If a Liquidity Sweep Target (prior swing low) falls INSIDE a Demand Zone, flag it as **"Confluent Floor"** — the highest structural confidence tier for support.
   - If a Supply Ceiling Target (prior swing high) falls INSIDE a Supply Zone, flag it as **"Confluent Ceiling"** — the highest structural confidence tier for resistance.
   - These confluent levels receive Structural dimension score of 2 (maximum) PLUS a Structural Extreme Bonus of +2.

**Output of Step 0:** A verified list of exact prior swing lows, swing highs, demand zones, and supply zones with dates, conviction levels, and confluent flags.

**STEP 0.45: DEDICATED LIQUIDITY SWEEP ZONE SCAN (MANDATORY — v4.5.1 FIX #3)**

**Purpose:** Identify ALL zones where institutional stop-loss orders are clustered — these are the exact prices where price is likely to spike before reversing. Liquidity sweep zones serve three critical functions:
1. **Stop-Loss Placement:** The nearest liquidity sweep zone ABOVE an entry (for shorts) or BELOW an entry (for longs) is the structurally correct stop-loss level.
2. **Take-Profit Target:** A liquidity sweep zone below a demand zone or above a supply zone is a high-probability TP target for breakout trades.
3. **Trade Direction Signal:** When a breakout target aligns with a liquidity sweep zone, the direction of the trade is confirmed by structural liquidity engineering.

**Scan Procedure:**

0.45a. **Scan ALL prior swing lows from Step 0 where stops would cluster.** For each swing low:
   - The exact swing low price is where retail/institutional stop-loss orders are placed
   - Record as "Liquidity Sweep Zone: [exact low] to [exact low + 0.05]" — extends 0.05 ABOVE the exact low
   - Tag each with the date(s)

0.45b. **Scan ALL prior swing highs from Step 0 where stops would cluster.** For each swing high:
   - Record as "Liquidity Sweep Zone: [exact high - 0.05] to [exact high]" — extends 0.05 BELOW the exact high
   - Tag each with the date(s)

0.45c. **Scan for LIQUIDITY GAPS between mapped zones.** For any gap >= 0.15 DXY points between adjacent IP zones that has NO structural level:
   - Check if the gap contains a prior swing extreme from the 4H timeframe that didn't meet D1 criteria
   - Check if the gap aligns with a 4H BoM zone from Step 0f
   - If yes: Flag as "Hidden Liquidity Zone"

0.45d. **Cross-reference with 4H BoM zones from Step 0f.** When a liquidity sweep zone overlaps with a 4H BoM demand/supply zone:
   - Flag as "CONFLUENT LIQUIDITY SWEEP + BoM ZONE" — this is the HIGHEST PRIORITY zone for trade construction

0.45e. **Special scan for stop-loss trigger zones near the current price.** Any liquidity sweep zone within 0.30 DXY points of the current spot price gets flagged as "ACTIVE SL TRIGGER."

**OUTPUT FORMAT:**
```
LIQUIDITY SWEEP ZONE: [range] | Type: [Demand-side/Supply-side] | Source: [D1 swing low [date] / 4H swing [date] / Hidden gap]
  Confluent with: [4H BoM zone range if overlapping, or "None"]
  Function: [SL for longs / SL for shorts / TP for downside BS / TP for upside BS]
  Priority: [ACTIVE SL TRIGGER / STANDARD / HIDDEN]
```

**CRITICAL:** Every trade setup in the report MUST reference at least one Liquidity Sweep Zone for its stop-loss placement.

**STEP 0.45a: LSZ BOTTOM EDGE EXTENSION (v5.0.0 — P5 POSTMORTEM FIX):**

Extend the liquidity sweep zone scan 0.05-0.10 DXY below swing highs (for supply-side LSZs) and 0.05-0.10 DXY above swing lows (for demand-side LSZs). The prior version only extended 0.05 in one direction. Institutions often sweep 0.05-0.10 beyond the visible extreme before reversing. Record as "LSZ Extended: [original range] extended to [new range] — sweep scan 0.05-0.10 DXY beyond swing [high/low]"

**STEP 0.5: REPEATED EXTREME MAGNET DETECTION (MANDATORY — RUN AFTER STEP 0)**

Institutional algorithms scan for price levels where stops have clustered from prior touches. When the exact same price level has been reached on multiple separate dates, it becomes a magnet for future price action.

0.5a. **Scan the Step 0 output for price levels that appear on 2+ separate dates.**
   - Compare every swing low against every other swing low. If two swing lows are within 0.05 DXY points of each other, they are a "repeated level."
   - Compare every swing high against every other swing high. Same threshold.
   - Also check if any swing low coincides with a prior swing high (or vice versa) — these "role reversal" levels are extremely powerful.

0.5b. **Tag each repeated level as a "Repeated Extreme Magnet"** with:
   - The exact price (average of the occurrences, weighted by wick size)
   - The dates of each occurrence
   - The type (Repeated Low Magnet, Repeated High Magnet, Role Reversal Magnet)
   - The number of occurrences

0.5c. **Confidence escalation by occurrence count:**
   | Occurrences | Confidence | Structural Extreme Bonus |
   |:---|:---|:---|
   | 2 separate dates | HIGH | +1.5 |
   | 3+ separate dates | VERY HIGH | +2.0 |
   | Role Reversal | EXTREME | +2.0 (independent of occurrence count) |

0.5d. **Integration with Order Blocks:** If a Repeated Extreme Magnet falls inside a HTF Order Block from Step 0d, tag as **"Institutional Magnet"** with maximum Structural dimension score.

**STEP 0.6: INTRA-ZONE KEY LEVEL SCAN (v5.0.0 — P3 POSTMORTEM FIX — MANDATORY)**

This step was added because the Apr 20-24 report treated each IP zone as a monolithic block, missing critical micro-levels within zones. Intra-zone levels often serve as the precise entry or the precise rejection point.

**Purpose:** Identify micro-levels within each mapped IP zone that provide additional precision for entry and SL placement.

**Scan Procedure:**

0.6a. **For each IP zone with Pressure Degree MODERATE or above**, scan the zone interior for:
   - 1H demand/supply zones from the prior 1-2 weeks that sit INSIDE the IP zone
   - Fib retracement levels (0.382, 0.618) of the zone's own range that align with price reactions
   - Prior daily closes within the zone range (each close is a potential reaction level)
   - Round number levels (.00, .25, .50, .75) that fall within the zone

0.6b. **Tag each intra-zone level as:**
   - "Intra-Zone Precision Floor" (if the level is within the bottom 40% of the zone range)
   - "Intra-Zone Precision Ceiling" (if the level is within the top 40% of the zone range)
   - "Intra-Zone Mid-Anchor" (if the level is in the middle 20%)

0.6c. **Record the data source for each intra-zone level** (1H zone, fib level, prior close, round number).

0.6d. **Scoring:** Intra-zone key levels receive Structural dimension score = 0.5 (half the weight of full zone-level structural extremes, but they refine entry precision within zones).

**OUTPUT FORMAT:**
```
Intra-Zone Key Levels for Zone #[N] ([RANGE]):
  [Level] | Type: [Precision Floor/Ceiling/Mid-Anchor] | Source: [1H zone / Fib 0.618 / Prior close [date] / Round number]
```

**STEP 0f: 4H DEMAND-SUPPLY ZONE SCAN (MANDATORY)**

This step is MANDATORY. It fills the single largest structural blind spot in the system — the absence of 4H timeframe order block identification.

**Data Source:** 4H OHLC data retrieved via Python `yfinance` library using `interval='1h'` for the last 60 calendar days, then aggregated to 4H candles. Symbol: `DX-Y.NYB`.

**⚠ CRITICAL: SINGULAR CANDLE CONSTRUCTION RULE (v4.5.1 FIX #2 — ZERO TOLERANCE)**

Supply/Demand zones are constructed from the **SINGULAR candle that immediately precedes a strong directional move** — NOT from a cluster of candles, NOT from interpolated ranges, and NEVER from fabricated price levels.

**Construction Procedure:**
1. **Identify a strong directional move** on the 4H chart (>= 0.5 DXY points, lasting >= 3 trading days).
2. **Locate the SINGLE candle immediately before that move began.** This is the "origin candle."
3. **The zone range = [Low of origin candle, High of origin candle]** for demand zones or supply zones.
4. **DATE-STAMP the origin candle.**

**PROHIBITED CONSTRUCTIONS (violations = data fabrication):**
- ❌ Fabricating a zone range that does not correspond to ANY actual 4H candle
- ❌ Constructing a supply zone whose range overlaps with a demand zone at the same timeframe
- ❌ Constructing zones from estimated or rounded price levels
- ❌ Constructing a zone that spans more than 0.40 DXY points without explicit verification
- ❌ Inventing a "BoM" or "MoM" label for a zone with no visible corresponding candle

**Verification Protocol (MANDATORY for every 4H zone):**
1. The zone range [Low, High] exactly matches a real 4H candle's Low and High
2. The candle immediately AFTER the zone candle moved directionally
3. The zone does not overlap with a zone of the opposite type at the same timeframe
4. The date stamp corresponds to a real trading date

**ZONE CLASSIFICATION:**
| Zone Type | Abbreviation | Strength | Behavior |
|:---|:---|:---|:---|
| Beginning of Move | BoM | STRONGEST | The zone at the exact origin of a primary directional move. Only the initial origin counts. |
| Middle of Move | MoM | WEAKEST | A continuation zone formed DURING the move. Valid only as ladder step entry. |

**CRITICAL HIERARCHY RULE (ZERO TOLERANCE):** Zone Type > Mitigation Level > Trend Context. An unmitigated MoM in an opposing trend is WEAKER than a 2X mitigated BoM.

**MITIGATION LEVEL TRACKING:**
| Count | Strength | Expected Behavior |
|:---|:---|:---|
| 0X (Unmitigated) | Fortress | 100% reaction for BoM. Will hold. |
| 1X mitigated | ~Unmitigated | Still very strong. |
| 2X mitigated | Weakened | Context-dependent. |
| 3X mitigated | Likely to fail | Expect failure. |
| 4-5X still holding | PARADOX SIGNAL | Extremely strong pressure behind zone. |

**4H zone noise rejection criteria (exclude zone if ANY applies):**
- Zone wider than 0.40 DXY points
- MoM zone with 3X+ hard mitigations in opposing trend
- Zone from more than 3 weeks ago with no recent price interaction
- Zone that does not overlap with any IP zone within 0.50 DXY points AND is not a BoM zone with 0X-1X mitigation

**OUTPUT FORMAT:**
```
[TYPE] [MITIGATION] 4H [Demand/Supply] Zone [range] formed [dates]
```
Example: "BoM 0X mitigated 4H Demand Zone [97.80-97.95] formed Apr 28-29"

**STEP 0g: 1H PRECISION ANCHOR SCAN (CONDITIONAL)**

[unchanged from v4.5.2 — 1H zones serve two purposes only: Nested Precision inside 4H/D1 zones, and Gap-Fill only]

**STEP 0h: MINOR SWING LEVEL IDENTIFICATION (MANDATORY)**

[unchanged from v4.5.2 — relaxed criteria for swing levels that did not meet Step 0 thresholds, fill gaps between major zones]

**STEPS 1-5 (PRICE ANCHORS, HWC/LWC, STRUCTURAL EXTREME MEMORY):**

[unchanged from v4.5.2 — extract price anchors, HWC/LWC from forex.com, detect recapture phenomenon, structural extreme memory, scoring]

**STEP 5.5: KEY SUPPORT BAND TIGHTENING (v5.0.0 — P6 POSTMORTEM FIX):**

When a zone is classified as "KEY SUPPORT BAND," distinguish between the zone CORE and the zone SPIKE:

- **Zone Core:** The range of candle BODIES within the zone (the range where most trading occurred). This is the primary support level.
- **Zone Spike:** Wicks that extend beyond the core (the range of brief price excursions). These are secondary — they represent liquidity sweep targets, not institutional defense levels.

**Output format:** `"KEY SUPPORT BAND: [core range] (core) | [spike range] (spike extends to [low/high]) | Core = primary support, Spike = LSZ target"`

**Scoring:** Zone Core receives full Structural dimension score. Zone Spike receives half score and is tagged as "LSZ extension."

---

**PILLAR 6: FIBONACCI RETRACEMENT & ROUND NUMBER GRID**

[unchanged from v4.5.2 — Fibonacci retracements from prior week range + extended swing points, round number levels with confluence bonus, scoring]

---

**PILLAR 7: DERIVATIVES ARENA BOUNDARY DEFINITION**

[unchanged from v4.5.2 — defines wide pressure arena, attempts ICE and CME supplementary data, fallback to 9-Pillar primary mapping]

---

**PILLAR 8: EUR/USD STRIKE-TO-DXY PRIMARY CONVERSION**

[unchanged from v4.5.2 core logic — converts EUR/USD OTC option expiry strikes directly to DXY levels using the simplified formula, with confidence weighting proportional to option notional. Applies the v5.0.0 three-tier classification (CRITICAL OPTION WALL / SIGNIFICANT MAGNET / EXCLUDED) instead of the old four-tier system.]

**Key updates for v5.0.0:**

- **Tier thresholds updated** to match the three-tier system:
  | EUR/USD Expiry Notional | Tier | Classification | Confidence Band |
  |:---|:---|:---|:---|
  | ≥ 1.5B EUR | 1 | CRITICAL OPTION WALL | ±0.07 DXY |
  | $850M – $1.499B EUR | 2 | SIGNIFICANT MAGNET | ±0.10 DXY |
  | < $850M EUR | 3 | EXCLUDED (override possible) | ±0.15 DXY if overridden |

- **K Factor audit trail requirement unchanged.**

- **All other Pillar 8 procedures unchanged from v4.5.2.**

---

**PILLAR 9: REGIME DETECTION, ZONE FAILURE PREDICTION & BREAKOUT MAGNITUDE PROJECTION**

[unchanged from v4.5.2 — classifies each IL zone by structural strength, detects breakout pre-conditions, assigns Zone Failure Probability, computes Measured Move Projection when ZFP > 45%, classifies overall market regime, generates breakout risk alerts with trade structure recommendations]

---

**SYNTHESIS ENGINE: CONFLUENCE SCORING & ZONE ASSEMBLY**

After all 9 Pillars produce their levels, assemble the DXY Institutional Pressure Zone Map:

**CONFLUENCE SCORING (0-14 scale across 6 dimensions + Structural Extreme Bonus):**

| Dimension | 2 Points | 1 Point | 0 Points |
|:---|:---|:---|:---|
| Technical | Exact match (within 3 pips) | Zone match (within 10 pips) | No match |
| Options-Derived | Critical Option Wall (≥1.5B) or Pillar 8 high-confidence | Significant Magnet ($850M-$1.499B) or Pillar 8 moderate | No positioning |
| Analyst Consensus | 2+ Tier-1 sources agree | 1 source identifies | No analyst coverage |
| Structural | Exact price anchor + structural extreme | Proximity to anchor or structural extreme | No structural event |
| Psychological | Major big figure (.00, .50) | Quarter figure (.25, .75) | No round number |
| Regime/Dynamic | Zone in consolidation, will hold | Zone in momentum, may hold or fail | Zone in breakout, likely to fail |

**STRUCTURAL EXTREME BONUS (up to +2):**
| Condition | Bonus |
|:---|:---|
| Liquidity Sweep Target or Supply Ceiling Target from Step 0 | +1.0 |
| Repeated Extreme Magnet (2 dates) from Step 0.5 | +1.5 |
| Repeated Extreme Magnet (3+ dates) or Role Reversal from Step 0.5 | +2.0 |
| Confluent Floor/Ceiling from Step 0e | +2.0 |
| Institutional Magnet from Step 0.5d | +2.0 |
Maximum Structural Extreme Bonus: +2.0. Maximum total score: 12 (base) + 2 (extreme bonus) = 14.

**PRESSURE DEGREE ASSIGNMENT:**
| Score | Pressure Degree | Failure Probability |
|:---|:---|:---|
| 12-14 | EXTREME | <10% |
| 10-11 | HEAVY | 10-25% |
| 8-9 | MODERATE-HEAVY | 20-35% |
| 6-7 | MODERATE | 30-45% |
| 4-5 | LIGHT | 40-60% |
| 0-3 | MINIMAL | >60% |

**ZONE ASSEMBLY ALGORITHM:**
1. Collect all levels from all 9 pillars. Sort from highest to lowest. **DO NOT filter by spot proximity.**
2. Score each level across 6 dimensions (0-2 pts each, max = 12) PLUS Structural Extreme Bonus (up to +2, max total = 14).
3. **MANDATORY LEVEL CLUSTERING SCAN:** Sort all levels. For each level, count how many other levels fall within 0.15 DXY points. A "cluster" is 3+ levels within a 0.15 DXY band. Flag every cluster as "HIGH-DENSITY ZONE." Flag pairs within 0.10 DXY as "TIGHT CONFLUENCE."
4. Group into zones where levels cluster within 0.10-0.15 DXY points.
5. Assign pressure degrees based on the group's highest-scoring level.
6. Assign ZFP from Pillar 9 and Measured Move Projection for ZFP > 45%.
7. Name each zone (RESISTANCE CEILING, UPPER RESISTANCE, EQUILIBRIUM ZONE, MID-RANGE SUPPORT, KEY SUPPORT BAND, LIQUIDITY SWEEP ZONE, BREAKOUT EXTENSION TARGET).
8. Flag any zone with ZFP > 50% as BREAKOUT RISK.
9. **Zone Strength from Consolidation Modifier (v5.2.0 — NEW):** Add +1 to confluence score for zones that formed AFTER a period of consolidation (observed on 4H timeframe). Zones formed during/after consolidation are USUALLY stronger than zones formed at the peak of a liquidity sweep. Tag as "POST-CONSOLIDATION ZONE" in the zone properties.

**STEP 9.5: POST-ZONE-MAP GAP SCAN (MANDATORY)** — Identify gaps ≥ 0.20 DXY between adjacent zones. Check 4H zones, 1H zones, round numbers, option conversions, daily pivots, minor swing levels, and extended closes as gap-fill candidates. If 2+ supporting signals exist, flag as "GAP IN-FILL LEVEL."

**STEP 9.7: 4H ZONE CLASSIFICATION OVERLAY (MANDATORY)** — Overlay 4H zone data onto IP zones. POI Tier Classification:
| POI Tier | Condition | Action |
|:---|:---|:---|
| **Tier 1 — Confluent POI** | IP zone OVERLAPS with 4H BoM S/D (0X-1X) | Primary trade location. +2 confluence. |
| **Tier 2 — IP-Only POI** | IP zone exists but NO overlapping 4H BoM | Secondary trade location. +1 confluence. |
| **Tier 3 — 4H-Only Level** | 4H BoM exists but NO overlapping IP zone | Informational only. No primary trades. |

**STEP 9.8: ZONE SYNTHESIS RE-VERIFICATION (v5.0.0 — D4 DERAILMENT FIX — MANDATORY):**

After the zone map is assembled and zones are named, perform a re-verification scan to catch any contamination from unfiltered data:

1. **Option Strike Verification:** For every zone that cites an option strike as a primary driver, verify that the strike is ≥ $850M notional AND from an R1-qualified pair (EU/GU/AU). If a zone cites a sub-threshold or non-R1 pair strike as primary driver, DOWNGRADE the zone's Options-Derived dimension score to 0 and remove the option-related confluence bonus.

2. **Zone Pressure Score Verification:** For every zone, verify that the Zone Pressure Score is computed from filtered, verified data only. If any input to the score computation came from sub-threshold strikes, recompute the score without that input.

3. **Cross-Reference Consistency:** Verify that every zone in the Synthesis section (Section 3 of the report) matches exactly with the corresponding zone in the full IP Zone Map (Section 2). Any discrepancy is a synthesis error — the Synthesis section must be regenerated.

**Output:** `"Zone Synthesis Re-verification: [X] zones verified | [Y] zones corrected | [Z] zones unchanged | Corrections: [list any corrections made]"`

**MAXIMUM TABLE DENSITY RULE (v5.0.0 — D5 DERAILMENT FIX):**

No table in the report may exceed 15 data rows. If a table exceeds 15 rows, it contains unfiltered data that should have been removed by the Filter Checkpoint. Tables that exceed this limit MUST be split or filtered before inclusion. This applies to:
- OTC expiry summary tables
- Option conversion tables
- Zone map tables
- Any data presentation table

Exception: The full IP Zone Map (Section 2) and Pivot tables are exempt from this rule because they are reference tables, not summary tables.

---

## PART IV: EXTRACTION, FILTERING, & TACTICAL CALCULATIONS

### 4.1 Extraction & Filtering Logic

- **Protocol A (OTC Expiries):** Extract ALL pairs visible in the image. **Apply Filter Checkpoint (v5.0.0) BEFORE data entry.** Primary report focus: EUR/USD, GBP/USD, AUD/USD, DXY. **Three-tier classification: CRITICAL OPTION WALL (≥$1.5B) / SIGNIFICANT MAGNET ($850M-$1.499B) / EXCLUDED (<$850M).** Sub-threshold strikes are NOT included in summary tables — they go to Pillar 3 conversion only.
- **Protocol B (DXY IP Zone Map):** Execute all 9 Pillars sequentially with mandatory pre-computation steps. **Apply Zone Synthesis Re-verification (Step 9.8) after assembly.** Maximum Table Density rule applies to all summary tables.
- **Protocols C1, C2, C3 (CME FX Options):** PERMANENTLY BLOCKED — skip entirely.
- **Protocol D (Treasury Auctions):** [unchanged from v4.5.2]
- **Protocol E (NY Fed ON RRP):** [unchanged from v4.5.2]
- **Protocol F (Economic Calendar):** [unchanged from v4.5.2]
- **Protocol G (EIA Petroleum Data):** [unchanged from v4.5.2]

### 4.2 Tactical Mathematical Calculations (Mandatory Post-Processing)

[unchanged from v4.5.2 — recommended stop loss zone calculation, take profit front-running calculation]

### 4.3 Volatility Trigger Framework (Mandatory 3-Step Processing)

[unchanged from v4.5.2 — What Is Happening → When Is It Hitting → Execution Play. Column names UPDATED for v5.0.0: "When Is It Hitting" → **"Strike Time"**, "What Is Happening" → **"Context"**, "Execution Play" → **"Analysis"**]

### 4.4 High-Impact Macro Fences (Red Folder Time-Locks)

[unchanged from v4.5.2 — pre-event lock 5 minutes prior, post-event release 15 minutes after, holiday desk clearance warning]

**Additional rule (v5.2.0):** You should NOT have limit orders open right before news hits — you do NOT know what price will do. It is okay to have open positions with SLs in profit, but having limit orders on the chart right before news is asking to have capital wiped.

---

## PART V: REPORT OUTPUT SPECIFICATION
