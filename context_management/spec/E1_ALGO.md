# E1_ALGO — Engine 1 (Institutional Pressure Zone Map) implementable digest

Extracted first-hand from canon. Nothing here is invented. Where canon is silent the entry says UNKNOWN; where canon disagrees with itself the entry says CONFLICT and quotes both sides.

**Citation convention**
- `SP:n` = `/home/user/plutus-vision/canon/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md` line n (4216 lines; read in full: 1-1725, 3257-4216, plus targeted reads of 1725-1784, 1944-1963, 2176-2225, 2549-2642, 2720-2731).
- `FA:n` = `/home/user/plutus-vision/canon/Toolset/Trident_Fractal_Architecture_FirstPrinciples_v2.3.md` line n (721 lines; read in full).
- `E3PY:n` = `/home/user/plutus-vision/canon/Toolset/trident_engine3_v8.py` line n. NOT one of the two named sources; quoted only as supplementary evidence where SP is silent, always labelled.
- "Derived" = arithmetic consequence of quoted rules, not a canon statement.

---

## 0. Read this first — what canon does and does not contain

0.1 **Engine 1 definition.** "Engine 1 (9-Pillar 6D Hybrid System + 4H Zone Overlay + POI Tier Classification + Zone Reaction Counter + BoM/MoM Classification): Maps Institutional Pressure (IP) zones, classifies POIs by overlap quality, tracks zone reaction counts, and classifies each zone as BoM or MoM" (SP:348).

0.2 **Units in canon are DXY points.** Every numeric tolerance in Pillars 1-9 and the Synthesis Engine is written in "DXY points" or "pips". DXY 1 pip = 0.01: "LONG SL from MRS = 97.87 - 0.01 = 97.86 (key level 97.87 of zone below - 1 pip)" (SP:2610); "30 pips (0.30 DXY)" (SP:2608); "80 pips (0.80 DXY)" (SP:2637). Pair 1 pip = 0.0001: "EUR/USD | 0.0200 (200 pips)" (SP:3874), "AUD/USD | 0.0150 (150 pips)" (SP:3876).

0.3 **Seven parts of E1 are placeholders in the source.** The text says "[unchanged from v4.5.2 ...]" and gives only a one-line summary. The v4.5.2 document is not in `canon/Toolset/` (the directory holds 6 files; none contains the missing text). These are UNKNOWN beyond the quoted one-liners:

| Part | Placeholder line | What the one-liner says |
|:---|:---|:---|
| Pillar 4 header | SP:1171 | "web search for DXY institutional commentary, extract explicit S/R levels, classify by source tier, temporal boundary applies" (procedure IS then given, SP:1173-1199) |
| Pillar 5 Step 0g | SP:1401 | "1H zones serve two purposes only: Nested Precision inside 4H/D1 zones, and Gap-Fill only" |
| Pillar 5 Step 0h | SP:1405 | "relaxed criteria for swing levels that did not meet Step 0 thresholds, fill gaps between major zones" |
| Pillar 5 Steps 1-5 | SP:1409 | "extract price anchors, HWC/LWC from forex.com, detect recapture phenomenon, structural extreme memory, scoring" |
| Pillar 6 | SP:1426 | "Fibonacci retracements from prior week range + extended swing points, round number levels with confluence bonus, scoring" |
| Pillar 7 | SP:1432 | "defines wide pressure arena, attempts ICE and CME supplementary data, fallback to 9-Pillar primary mapping" |
| Pillar 8 core | SP:1438 | "converts EUR/USD OTC option expiry strikes directly to DXY levels using the simplified formula, with confidence weighting proportional to option notional" |
| Pillar 9 | SP:1457 | "classifies each IL zone by structural strength, detects breakout pre-conditions, assigns Zone Failure Probability, computes Measured Move Projection when ZFP > 45%, classifies overall market regime, generates breakout risk alerts with trade structure recommendations" |

0.4 **Spot is not a filter.** "Never filter, discard, or deprioritize any computed IL level based on its distance from the current spot price." (SP:735). Repeated at SP:1015 and SP:1497.

0.5 **No estimated ranges.** "Every floor and ceiling level MUST come from exact, date-stamped, verifiable historical price data." (SP:1209). "Zone ranges MUST be anchored to actual price structure: 4H candle origins, swing H/L, option strikes, MA crossovers. Generic ranges like "1.1480-1.1520" not traceable to a specific price event are FORBIDDEN." (SP:111).

---

## 1. The nine pillars

Six dimensions the pillars feed (SP:954-963): Technical (price-derived), Options-Derived, Analyst Consensus, Structural, Psychological, Regime/Dynamic.

### P1 — Multi-Timeframe Pivot Engine (SP:967-1059)

1.1.1 Inputs: "Prior week + prior day DXY High, Low, Close" (SP:971). Extended depth: "Last 4-8 weeks of weekly OHLC for structural pivot levels" (SP:972); "Any prior week where DXY traded near the current range (search backwards up to 4 months)" (SP:973); "On 4H timeframe, occasionally need data from up to 4 years prior (rare but documented)" (SP:974). Step 3: "Check if current DXY range overlaps with any historical range from the past 2-4 months. If yes, retrieve that period's OHLC for additional pivot calculations." (SP:985).

1.1.2 Classic (SP:989-992):
```
PP = (H + L + C) / 3
R1 = 2 × PP - L      S1 = 2 × PP - H
R2 = PP + (H - L)     S2 = PP - (H - L)
R3 = H + 2 × (PP - L) S3 = L - 2 × (H - PP)
```
1.1.3 Fibonacci (SP:997-1000):
```
PP = (H + L + C) / 3
R1 = PP + 0.382 × (H - L)   S1 = PP - 0.382 × (H - L)
R2 = PP + 0.618 × (H - L)   S2 = PP - 0.618 × (H - L)
R3 = PP + 1.000 × (H - L)   S3 = PP - 1.000 × (H - L)
```
1.1.4 Camarilla (SP:1005-1008) — no PP:
```
R4 = C + (H - L) × 1.1 / 2     S4 = C - (H - L) × 1.1 / 2
R3 = C + (H - L) × 1.1 / 4     S3 = C - (H - L) × 1.1 / 4
R2 = C + (H - L) × 1.1 / 6     S2 = C - (H - L) × 1.1 / 6
R1 = C + (H - L) × 1.1 / 12    S1 = C - (H - L) × 1.1 / 12
```
1.1.5 Timeframes to compute (SP:1011-1015): "Weekly timeframe (3 variants) using the prior week's H, L, C"; "Daily timeframe (3 variants) for EACH of the last 3 trading days (not just the last day)"; "Any historical weeks identified in step 3"; "DO NOT filter by spot proximity. Retain ALL calculated levels."

1.1.6 CONFLICT (daily depth): Step 2 says "Extract daily OHLC for EACH of the last 5 trading days of the prior week." (SP:983); Step 7 says pivots "for EACH of the last 3 trading days" (SP:1013). Extract 5, compute 3 is the literal reading.

1.1.7 CONFLICT (level count): "3 pivot variants × 2 timeframes = 6 complete pivot sets (42 calculated levels)" (SP:969). Derived from the formulas: Classic 7 + Fibonacci 7 + Camarilla 8 = 22 per timeframe = 44 for 2 timeframes, and more once 3 daily sets are computed.

1.1.8 Verification (SP:1021-1050, Appendix C SP:4082-4096): R1+L = 2×PP; S1+H = 2×PP; R2−PP = H−L; PP−S2 = H−L; Fibonacci symmetry R1−PP = PP−S1; ordering R1>PP>S1, R2>R1>PP, S1>S2>S3; Classic R2−S2 = 2×(H−L); Fibonacci R2−S2 = 1.236×(H−L); Camarilla R4−S4 = (H−L)×1.1; Camarilla ordering "R4 > R3 > R2 > R1 > C and C > S1 > S2 > S3 > S4" (SP:4095). "Classic Pivots are ASYMMETRIC by design." (SP:1036).

1.1.9 Scoring: "Exact match within 3 pips = 2 pts (Technical dimension); Zone match within 10 pips = 1 pt. Levels from extended historical data that coincide with current levels get a LEGACY BONUS of +0.5." (SP:1059). In DXY: 0.03 / 0.10. UNKNOWN: what the pivot is matched against (canon does not name the reference level set).

1.1.10 Output: list of pivot levels tagged timeframe + variant + H/L/C audit line (SP:1054-1056).

### P2 — Moving Average Confluence Grid (SP:1065-1088)

1.2.1 Inputs: "Extract ALL available MA values: EMA/SMA 9, 10, 20, 50, 100, 200." (SP:1073). Source: "TradingView DXY Technicals (`tradingview.com/symbols/TVC-DXY/technicals/`) | EMA/SMA values for MA Confluence Grid" (SP:757). The data-source block inside Pillar 2 itself is missing (a stray code fence at SP:1069).

1.2.2 MA timeframe: UNKNOWN as an explicit statement in Pillar 2. Evidence it is daily: "EMA/SMA 100 | 2.0 | Long-term trend — 5 months of price history" (SP:1081); "The 200-day MA value (from TradingView for that pair)" (SP:3325); "200-day MA value from web data" (SP:3459).

1.2.3 Cluster: "Detect confluence clusters where 3+ MAs converge within 0.15 DXY points." (SP:1075).

1.2.4 Weights (SP:1078-1084): EMA/SMA 200 = 3.0; EMA/SMA 100 = 2.0; EMA/SMA 50 = 1.5; EMA/SMA 20 = 1.0; EMA 9/10 = 0.5. UNKNOWN: no formula in the source consumes these weights.

1.2.5 Recapture: "If price recently (within 3 sessions) crossed above a major MA (50, 100, 200), flag that level as RECAPTURE ZONE with +2 bonus to confluence score. The recaptured MA becomes the most important support level." (SP:1086).

1.2.6 Scoring: "Triple+ cluster = 2 pts (Technical dimension); Double cluster = 1 pt; Single MA = 0.5 pts." (SP:1088). UNKNOWN: tolerance for a "Double cluster" (only the 3+ / 0.15 rule is stated).

1.2.7 Output: MA levels, cluster bands, RECAPTURE ZONE flags.

### P3 — Component Pair Option Expiry Conversion (SP:1092-1165)

1.3.1 Formula (SP:930): `DXY = 50.14348112 × EURUSD^(-0.576) × USDJPY^(0.136) × GBPUSD^(-0.119) × USDCAD^(0.091) × USDSEK^(0.042) × USDCHF^(0.036)`.

1.3.2 Per-pip DXY impact table (SP:936-941): EUR/USD ~0.048 pts/pip (62.4%); USD/JPY ~0.009 (11.9%); GBP/USD ~0.009 (11.3%); USD/CAD ~0.006 (8.4%); USD/SEK ~0.0004 (0.5%); USD/CHF ~0.004 (5.4%).

1.3.3 Inputs: Protocol A OTC expiry strikes (investinglive.com image, VLM) + Fed H.10 spot rates (SP:1098-1107).

1.3.4 Conversion: "For each LARGE expiry (>= USD 500M equivalent), calculate DXY equivalent: Hold all other pairs at current spot; Vary ONLY the pair with the expiry to its strike price; Calculate: `DXY_equiv = 50.14348112 × strike_EURUSD^(-0.576) × spot_USDJPY^(0.136) × ...`" (SP:1121-1124).

1.3.5 Tiers (SP:1129-1133): Tier 1 "≥ $1.5B equivalent" CRITICAL OPTION WALL; Tier 2 "$850M – $1.499B equivalent" SIGNIFICANT MAGNET; Tier 3 "< $850M equivalent" EXCLUDED, "Override ONLY with 3+ pillar confluence + Pillar 5 Step 0/0.5 validation".

1.3.6 CONFLICT (conversion floor): "For each LARGE expiry (>= USD 500M equivalent)" (SP:1121) vs "The threshold is now $850M, not $500M." (SP:1135).

1.3.7 Confluence adjustments (SP:1138-1140): Tier 1 "Options-Derived dimension score = 2 (maximum), confluence score +3"; Tier 2 "Options-Derived dimension score = 2, confluence score +2"; Tier 3 Override "Options-Derived dimension score = 1, confluence score +1".

1.3.8 Role: "SECONDARY to Pillar 8 for EUR/USD, and PRIMARY for the other 5 pairs" (SP:1094); the other 5 "collectively account for only 37.6% of per-pip DXY sensitivity" (SP:1165).

1.3.9 Output: DXY-equivalent levels per qualifying strike with tier.

### P4 — Institutional Commentary Harvesting (SP:1169-1199)

1.4.1 Inputs: three web searches (SP:1181-1183). "Extract EXPLICIT S/R levels only." (SP:1186).

1.4.2 Source tiers (SP:1193-1195): Tier 1 "ING Economics, forex.com (Matt Weller CMT)" weight 3.0; Tier 2 "FXStreet, TradingView Community, VT Markets" 2.0; Tier 3 "Continuum Economics, OneUpTrader" 1.0.

1.4.3 "Flag levels appearing in 2+ independent sources as ANALYST CONSENSUS." (SP:1197).

1.4.4 Scoring: "2+ Tier-1 sources agree = 2 pts (Analyst dimension); 1 source = 1 pt; no coverage = 0 pts." (SP:1199).

### P5 — Structural Extreme Scan, Price Anchors & Liquidity Engineering (SP:1205-1420)

Data: "TradingView OHLC (90-day 4H/D1 historical) + forex.com institutional research + web search for macro events." (SP:1211).

**Step 0 — 90-day structural extreme scan (SP:1213-1244)**

1.5.1 0a: "Retrieve 90 days of DXY daily (D1) OHLC data" (SP:1217).

1.5.2 180-day extension: "If the current DXY range overlaps with a range from 90-180 days ago (i.e., current DXY is within 1.0 points of a level that was a significant swing extreme in that period), extend the scan to 180 days. Prior swing levels from that extended period receive a LEGACY BONUS of +0.5." (SP:1219).

1.5.3 0b swing lows = Liquidity Sweep Targets: "The lower wick must be ≥ 0.15 DXY points AND the close must be in the upper 50% of the daily range." (SP:1223). "The exact price of a prior swing low is the PRIMARY liquidity sweep target. Not a range, not an estimate — the EXACT price." (SP:1226). Record "exact price, date, wick size, and the subsequent price action" (SP:1224).

1.5.4 0c swing highs = Supply Ceiling Targets: "The upper wick must be ≥ 0.15 DXY points AND the close must be in the lower 50% of the daily range." (SP:1230).

1.5.5 UNKNOWN: the bar-count definition of a "swing low/high" (left/right bars). Canon gives only the wick + close-position criteria. UNKNOWN: whether "wick" is measured from min(O,C) or from C.

1.5.6 0d D1 order blocks: Demand = "the base of strong bullish candle clusters (1-3 consecutive bullish candles with large bodies) that preceded a sustained rally of ≥ 1.0 DXY points lasting ≥ 5 trading days. Record the zone as [Low of base, High of base]" (SP:1235). Supply = "the top of strong bearish candle clusters (1-3 consecutive bearish candles with large bodies) that preceded a sustained decline of ≥ 1.0 DXY points lasting ≥ 5 trading days. Record the zone as [Low of top, High of top]" (SP:1236). "If the move from the order block was ≥ 2.0 DXY points and lasted ≥ 10 trading days, tag as "High-Conviction Order Block."" (SP:1237). UNKNOWN: numeric threshold for "large bodies".

1.5.7 CONFLICT (order-block candle colour): Step 0d requires "bullish candles" for demand / "bearish candles" for supply (SP:1235-1236); Part II says "An order block is the LAST SHORT candle before a BIG impulsive swing. Candle color does NOT matter." (SP:482); changelog v4.5.2 "(4) Order Block definition corrected — candle color does NOT matter" (SP:343).

1.5.8 0e: Liquidity Sweep Target inside a Demand Zone = "Confluent Floor"; Supply Ceiling Target inside a Supply Zone = "Confluent Ceiling"; "These confluent levels receive Structural dimension score of 2 (maximum) PLUS a Structural Extreme Bonus of +2." (SP:1240-1242).

**Step 0.45 — Liquidity Sweep Zone (LSZ) scan (SP:1246-1286)**

1.5.9 Demand-side: "Liquidity Sweep Zone: [exact low] to [exact low + 0.05]" — extends 0.05 ABOVE the exact low" (SP:1257).

1.5.10 Supply-side: "Liquidity Sweep Zone: [exact high - 0.05] to [exact high]" — extends 0.05 BELOW the exact high" (SP:1261).

1.5.11 Hidden zones: "For any gap >= 0.15 DXY points between adjacent IP zones that has NO structural level: Check if the gap contains a prior swing extreme from the 4H timeframe that didn't meet D1 criteria; Check if the gap aligns with a 4H BoM zone from Step 0f; If yes: Flag as "Hidden Liquidity Zone"" (SP:1264-1267).

1.5.12 LSZ overlapping a 4H BoM zone: "CONFLUENT LIQUIDITY SWEEP + BoM ZONE" — this is the HIGHEST PRIORITY zone for trade construction" (SP:1270).

1.5.13 "Any liquidity sweep zone within 0.30 DXY points of the current spot price gets flagged as "ACTIVE SL TRIGGER."" (SP:1272). Priority enum: "[ACTIVE SL TRIGGER / STANDARD / HIDDEN]" (SP:1279). Type enum: "[Demand-side/Supply-side]" (SP:1276).

1.5.14 Extension (P5 fix): "Extend the liquidity sweep zone scan 0.05-0.10 DXY below swing highs (for supply-side LSZs) and 0.05-0.10 DXY above swing lows (for demand-side LSZs). The prior version only extended 0.05 in one direction. Institutions often sweep 0.05-0.10 beyond the visible extreme before reversing." (SP:1286).

1.5.15 CONFLICT (which side of the extreme the LSZ sits): SP:1257/1261/1286 put the band INSIDE the extreme (above a low, below a high); the same line SP:1286 justifies it with sweeps "beyond the visible extreme" and the record format says "sweep scan 0.05-0.10 DXY beyond swing [high/low]"; Part IX says "Demand-side LSZ (below swing low, stops for longs)" and "Supply-side LSZ (above swing high, stops for shorts)" (SP:3572-3573). Operator proof of a real LSZ: "LSZ demand 97.97-98.02" (SP:2639), width 0.05.

**Step 0.5 — Repeated Extreme Magnets (SP:1288-1310)**

1.5.16 "If two swing lows are within 0.05 DXY points of each other, they are a "repeated level."" Same threshold for highs. "Also check if any swing low coincides with a prior swing high (or vice versa) — these "role reversal" levels are extremely powerful." (SP:1293-1295).

1.5.17 Magnet price = "average of the occurrences, weighted by wick size" (SP:1298). Types: "Repeated Low Magnet, Repeated High Magnet, Role Reversal Magnet" (SP:1300).

1.5.18 Bonus (SP:1306-1308): 2 separate dates = HIGH, +1.5; 3+ separate dates = VERY HIGH, +2.0; Role Reversal = EXTREME, "+2.0 (independent of occurrence count)".

1.5.19 "If a Repeated Extreme Magnet falls inside a HTF Order Block from Step 0d, tag as "Institutional Magnet" with maximum Structural dimension score." (SP:1310).

**Step 0.6 — Intra-zone key level scan (SP:1312-1339)**

1.5.20 "For each IP zone with Pressure Degree MODERATE or above, scan the zone interior for: 1H demand/supply zones from the prior 1-2 weeks that sit INSIDE the IP zone; Fib retracement levels (0.382, 0.618) of the zone's own range that align with price reactions; Prior daily closes within the zone range; Round number levels (.00, .25, .50, .75) that fall within the zone" (SP:1320-1324).

1.5.21 Tags: "Intra-Zone Precision Floor" (bottom 40%), "Intra-Zone Precision Ceiling" (top 40%), "Intra-Zone Mid-Anchor" (middle 20%) (SP:1327-1329). "Intra-zone key levels receive Structural dimension score = 0.5" (SP:1333).

1.5.22 Key-level source list used downstream (SP:2590-2597): pivot levels inside the zone; option strike equivalents inside the zone; swing highs/lows inside the zone; fib 0.382/0.618 of the zone's own range; prior daily closes; round numbers (.00, .25, .50, .75); zone midpoint.

**Step 0f — 4H demand/supply zone scan (SP:1341-1397)**

1.5.23 Data: "4H OHLC data retrieved via Python `yfinance` library using `interval='1h'` for the last 60 calendar days, then aggregated to 4H candles." (SP:1345). UNKNOWN: 4H bucket alignment.

1.5.24 Construction (SP:1352-1355): "Identify a strong directional move on the 4H chart (>= 0.5 DXY points, lasting >= 3 trading days)."; "Locate the SINGLE candle immediately before that move began. This is the "origin candle.""; "The zone range = [Low of origin candle, High of origin candle]"; "DATE-STAMP the origin candle."

1.5.25 Prohibited (SP:1358-1362): zone not matching a real 4H candle; supply overlapping demand at the same timeframe; estimated/rounded levels; "a zone that spans more than 0.40 DXY points without explicit verification"; BoM/MoM label with no visible candle.

1.5.26 Classification (SP:1373-1374): BoM "STRONGEST | The zone at the exact origin of a primary directional move. Only the initial origin counts."; MoM "WEAKEST | A continuation zone formed DURING the move. Valid only as ladder step entry." Hierarchy: "Zone Type > Mitigation Level > Trend Context. An unmitigated MoM in an opposing trend is WEAKER than a 2X mitigated BoM." (SP:1376).

1.5.27 Mitigation table (SP:1381-1385): 0X Fortress "100% reaction for BoM. Will hold."; 1X "~Unmitigated | Still very strong."; 2X "Weakened | Context-dependent."; 3X "Likely to fail"; "4-5X still holding | PARADOX SIGNAL | Extremely strong pressure behind zone."

1.5.28 Noise rejection — exclude if ANY (SP:1388-1391): "Zone wider than 0.40 DXY points"; "MoM zone with 3X+ hard mitigations in opposing trend"; "Zone from more than 3 weeks ago with no recent price interaction"; "Zone that does not overlap with any IP zone within 0.50 DXY points AND is not a BoM zone with 0X-1X mitigation".

1.5.29 Output string: "[TYPE] [MITIGATION] 4H [Demand/Supply] Zone [range] formed [dates]" (SP:1395).

**Step 5.5 — Key Support Band tightening (SP:1411-1420)**

1.5.30 "Zone Core: The range of candle BODIES within the zone"; "Zone Spike: Wicks that extend beyond the core" (SP:1415-1416). "Zone Core receives full Structural dimension score. Zone Spike receives half score and is tagged as "LSZ extension."" (SP:1420).

**Steps 0g, 0h, 1-5:** UNKNOWN beyond SP:1401, SP:1405, SP:1409. "HWC/LWC" is never expanded in either source (appears at SP:730, 758, 961, 1207, 1409) — UNKNOWN.

### P6 — Fibonacci Retracement & Round Number Grid (SP:1424-1426)

1.6.1 Full procedure UNKNOWN (placeholder). Known fragments:
- Anchors: "Fibonacci retracements from prior week range + extended swing points" (SP:1426). Audit: "Show the swing high, swing low, and the retracement percentage" (SP:396).
- Ratios stated elsewhere: "Institutional Reload Retracements: 0.236 and 0.382 depths. Master Structural Targets: 1.618 extensions." (SP:684-685); intra-zone "0.382, 0.618" (SP:1322). The Pillar 6 ratio list itself is UNKNOWN.
- Round numbers (DXY): "Major big figure (.00, .50)" = 2 pts, "Quarter figure (.25, .75)" = 1 pt (SP:1473). Derived grid step 0.25.
- Round numbers (pairs): "for pairs, big figures are 1.1000, 1.1500, etc." (SP:3400); example "Round number: 1.1650 (psychological)" (SP:3560). Grid step for pairs UNKNOWN.
- "round number levels with confluence bonus" (SP:1426) — bonus size UNKNOWN.

### P7 — Derivatives Arena Boundary (SP:1430-1432)

1.7.1 UNKNOWN beyond SP:1432. Sources ICE/CME are flagged UNSTABLE/BLOCKED (SP:768-773). Stated fallback: "fallback to 9-Pillar primary mapping" (SP:1432).

### P8 — EUR/USD Strike-to-DXY Primary Conversion (SP:1436-1451, Appendix A SP:4011-4048)

1.8.1 Formula (SP:947-951): `DXY = K × EURUSD^(-0.576)`; `K = 50.14348112 × USDJPY^(0.136) × GBPUSD^(-0.119) × USDCAD^(0.091) × USDSEK^(0.042) × USDCHF^(0.036)`; reverse `EURUSD_strike = (K / DXY_target)^(1/0.576) = (K / DXY_target)^1.7361`.

1.8.2 Reference table "K ≈ 107.6, typical rates" (SP:4013-4029): 1.1200→100.79; 1.1250→100.54; 1.1300→100.28; 1.1350→100.03; 1.1400→99.77; 1.1450→99.52; 1.1500→99.27; 1.1550→99.02; 1.1600→98.78; 1.1650→98.53; 1.1700→98.29; 1.1750→98.05; 1.1800→97.81.

1.8.3 Confidence bands (SP:1445-1447): "≥ 1.5B EUR | 1 | CRITICAL OPTION WALL | ±0.07 DXY"; "$850M – $1.499B EUR | 2 | SIGNIFICANT MAGNET | ±0.10 DXY"; "< $850M EUR | 3 | EXCLUDED (override possible) | ±0.15 DXY if overridden".

1.8.4 H.10 fallback widening (SP:1116-1118): 1 supplementary pair +0.03 DXY; 2 pairs +0.07 DXY; 3+ pairs "Pillar 8 confidence degrades to LOW".

1.8.5 "This appendix is for DXY-level computation ONLY (Pillar 8). It must NEVER be used to convert DXY zone levels to EUR/USD zone levels." (SP:4048).

### P9 — Regime Detection, Zone Failure Prediction & Breakout Magnitude (SP:1455-1457)

1.9.1 Procedure UNKNOWN (placeholder). ZFP table is in Appendix B (see §5). Measured Move: computed "when ZFP > 45%" (SP:1457); audit must "Show the range height, raw target, and structural extreme anchor" (SP:398); formula UNKNOWN. Regime classes: only the Regime/Dynamic scoring row is given (§4.1).

---

## 2. Input-by-input: computable from the instrument's own OHLC?

| # | Input | Pillar | OHLC-only | If NO: what it is | Degradation rule in canon |
|:---|:---|:---|:---|:---|:---|
| 1 | Prior week H/L/C | P1 | YES | — | — |
| 2 | Daily H/L/C, last 3 (or 5) trading days | P1 | YES | — | — |
| 3 | Weekly OHLC last 4-8 weeks; overlap weeks up to 4 months | P1 | YES | — | — |
| 4 | EMA/SMA 9,10,20,50,100,200 | P2 | YES (values computable; canon harvests them from the TradingView technicals page, SP:757) | — | — |
| 5 | MA recapture within 3 sessions | P2 | YES | — | — |
| 6 | OTC option strikes + notionals (10am NY cut) | P3, P8 | NO | investinglive.com expiry image via VLM (SP:810-853) | "Only the options-derived dimension (Pillar 3 and Pillar 8) is degraded for that specific day." "IL levels for this day are derived from structural pillars only (no options-derived dimension)." (SP:896-897). Dimension table recovery: "Technical + Structural" (SP:959). Score row "No positioning" = 0 (SP:1470). |
| 7 | Spot of 6 DXY components | P3, P8 | NO (other instruments) | Fed H.10 (SP:1107) | Fallback SP:1109-1119; "NEVER fabricate a spot rate." |
| 8 | Analyst S/R levels | P4 | NO | web search, ING / forex.com / FXStreet etc. | Score "No analyst coverage" = 0 (SP:1471); recovery "Technical + Options" (SP:960); Missing Data Log example "No analyst data | Reduced confluence scoring | Rely on Pillar 1-4 only" (SP:1661). |
| 9 | D1 OHLC 90 days (180 conditional) | P5 Step 0 | YES | — | — |
| 10 | Swing lows/highs with rejection wicks | P5 0b/0c | YES | — | — |
| 11 | D1 order blocks | P5 0d | YES ("large bodies" threshold UNKNOWN) | — | — |
| 12 | LSZ bands | P5 0.45 | YES | — | — |
| 13 | Repeated extreme / role reversal magnets | P5 0.5 | YES | — | — |
| 14 | Intra-zone key levels | P5 0.6 | YES except option-strike equivalents | — | — |
| 15 | 4H origin-candle S/D zones (60 days) | P5 0f | YES | — | — |
| 16 | 1H precision anchors, minor swings | P5 0g/0h | YES in principle; criteria UNKNOWN | — | — |
| 17 | HWC/LWC | P5 Steps 1-5 | UNKNOWN (term undefined; canon harvests it from forex.com, SP:758) | forex.com research | UNKNOWN |
| 18 | Prior session closes / price anchors | P5 Steps 1-5 | YES in principle; procedure UNKNOWN | — | — |
| 19 | Fib retracements of prior week range / swings | P6 | YES; ratio list UNKNOWN | — | — |
| 20 | Round numbers | P6 | YES (no data needed) | — | — |
| 21 | ICE / CME OI arena | P7 | NO | ICE EOD, CME QuikStrike (SP:768-769) | "fallback to 9-Pillar primary mapping" (SP:1432); blocked sources: "mark that protocol `[NO DATA — source blocked from this environment]` immediately" (SP:776). |
| 22 | Regime (consolidation / momentum / breakout) | P9 | YES in principle; classifier UNKNOWN | — | — |
| 23 | ZFP base (zone type) | P9 / App. B | PARTIAL: pillar count + Confluent Floor/Ceiling YES; option-wall tier NO | — | No-option branch exists: "Soft Wall | No option wall (EXCLUDED tier, <$850M) or 1-2 pillars only | 30-50%"; "One-Touch | Only 1 pillar, no option wall | 50-70%" (SP:4060-4061). |
| 24 | ZFP modifiers | P9 / App. B | momentum, cascade, EMA-200 cross: YES; expiry timing, macro catalyst, cross-pair: NO (SP:4069-4074 name Protocol A / F / web search) | — | UNKNOWN |

General rules for missing data: "Mark it `[NO DATA]` and move on." (SP:369); "Do NOT halt the entire report. Mark that section `[NO DATA]` and proceed with remaining protocols." (SP:373); Missing Data Log with CRITICAL / SIGNIFICANT / MINOR impact classes (SP:1652-1669).

Derived: with inputs 6, 7, 8, 21 absent, Options-Derived and Analyst Consensus dimensions score 0, so the base score ceiling is 4 dimensions × 2 = 8, plus Structural Extreme Bonus 2 = 10.

---

## 3. Zone assembly procedure

Verbatim algorithm (SP:1496-1505):

3.1 "Collect all levels from all 9 pillars. Sort from highest to lowest. DO NOT filter by spot proximity."
3.2 "Score each level across 6 dimensions (0-2 pts each, max = 12) PLUS Structural Extreme Bonus (up to +2, max total = 14)."
3.3 "MANDATORY LEVEL CLUSTERING SCAN: Sort all levels. For each level, count how many other levels fall within 0.15 DXY points. A "cluster" is 3+ levels within a 0.15 DXY band. Flag every cluster as "HIGH-DENSITY ZONE." Flag pairs within 0.10 DXY as "TIGHT CONFLUENCE.""
3.4 "Group into zones where levels cluster within 0.10-0.15 DXY points."
3.5 "Assign pressure degrees based on the group's highest-scoring level."
3.6 "Assign ZFP from Pillar 9 and Measured Move Projection for ZFP > 45%."
3.7 "Name each zone (RESISTANCE CEILING, UPPER RESISTANCE, EQUILIBRIUM ZONE, MID-RANGE SUPPORT, KEY SUPPORT BAND, LIQUIDITY SWEEP ZONE, BREAKOUT EXTENSION TARGET)."
3.8 "Flag any zone with ZFP > 50% as BREAKOUT RISK."
3.9 "Zone Strength from Consolidation Modifier (v5.2.0 — NEW): Add +1 to confluence score for zones that formed AFTER a period of consolidation (observed on 4H timeframe). ... Tag as "POST-CONSOLIDATION ZONE" in the zone properties."

Post-steps:

3.10 Step 9.5 gap scan: "Identify gaps ≥ 0.20 DXY between adjacent zones. Check 4H zones, 1H zones, round numbers, option conversions, daily pivots, minor swing levels, and extended closes as gap-fill candidates. If 2+ supporting signals exist, flag as "GAP IN-FILL LEVEL."" (SP:1507).
3.11 Step 9.7 4H overlay → POI tier (see §4.5) (SP:1509-1514).
3.12 Step 9.8 re-verification: zones citing an option strike must have strike "≥ $850M notional AND from an R1-qualified pair (EU/GU/AU)", else "DOWNGRADE the zone's Options-Derived dimension score to 0 and remove the option-related confluence bonus" (SP:1520).
3.13 BoM/MoM classification per IP zone (SP:1147-1152) and Zone Reaction Counter per IP zone (SP:1156-1161) — see §4.6, §4.7.

**Tolerances (DXY units, as written)**

| Constant | Value | Cite |
|:---|:---|:---|
| Cluster band (HIGH-DENSITY ZONE, 3+ levels) | 0.15 | SP:1499 |
| TIGHT CONFLUENCE pair | 0.10 | SP:1499 |
| Grouping into a zone | 0.10-0.15 | SP:1500 |
| MA cluster (3+ MAs) | 0.15 | SP:1075 |
| Technical exact / zone match | 3 pips / 10 pips | SP:1059, SP:1469 |
| Repeated extreme | 0.05 | SP:1293 |
| LSZ width | 0.05 (extension 0.05-0.10) | SP:1257, 1261, 1286 |
| Liquidity gap for hidden zone | ≥ 0.15 | SP:1264 |
| Post-map gap scan | ≥ 0.20 | SP:1507 |
| ACTIVE SL TRIGGER distance to spot | 0.30 | SP:1272 |
| 4H S/D zone max width | 0.40 | SP:1361, SP:1388 |
| 4H zone must be within X of an IP zone (unless BoM 0X-1X) | 0.50 | SP:1391 |
| Rejection wick minimum | 0.15 | SP:1223, SP:1230 |
| 4H strong move | ≥ 0.5, ≥ 3 trading days | SP:1352 |
| D1 order-block move | ≥ 1.0 / ≥ 5 days; high-conviction ≥ 2.0 / ≥ 10 days | SP:1235-1237 |
| 180-day extension proximity | 1.0 | SP:1219 |

**Per-instrument tolerances for EURUSD / GBPUSD: UNKNOWN in the two named sources.** Canon forbids deriving pair zone widths by ratio: "DXY zone is 0.25 points wide, so EUR/USD zone is 0.25 × 100 = 25 pips" (WRONG — pair zone widths are determined by the pair's own structure)" (SP:3346). Two candidate scalings exist and disagree:
- Supplementary (outside named sources) `E3PY:666-669`: DXY `tol_near, tol_close, tol_analyst, tol_swing, tol_round = 0.10, 0.20, 0.15, 0.15, 0.05`; pairs `10*pip_size, 20*pip_size`, `15*pip_size, 15*pip_size, 5*pip_size` — i.e. 0.01 DXY ≡ 1 pip. `E3PY:228-231` pip_size DXY 0.01, EUR/USD 0.0001, GBP/USD 0.0001, AUD/USD 0.0001.
- Appendix A.2 (SP:4035-4039): 0.050 DXY ≈ ~10 EUR/USD pips; 0.075 ≈ ~15; 0.100 ≈ ~21; 0.175 ≈ ~36; 0.250 ≈ ~52 — i.e. 0.01 DXY ≈ 2 pips; but scoped "for DXY-level computation ONLY" (SP:4048).

**Zone top / bottom rule: UNKNOWN as an explicit rule.** Canon only says levels are grouped (SP:1500) and ranges must trace to real price events (SP:111). Canon examples of finished zones: DXY "RESISTANCE CEILING at 99.50-99.65" (SP:3412), "KEY SUPPORT BAND | 98.00-98.15" (SP:3553), "Key Resistance 103.80-104.20" (SP:1635); EUR/USD "SUPPORT at 1.1495-1.1520" built from the min and max of its member levels 1.1495 / 1.1500-1.1520 / 1.1510 / 1.1518 (SP:3415-3419), "RESISTANCE at 1.1625-1.1650" (SP:3562), "1.1430-1.1460 (anchored to Mar 13 low)" (SP:111).

**Max / min IP zone width: UNKNOWN.** Only the 4H S/D zone has a stated cap (0.40 DXY). Pine check: "LSZ zone widths are similar to IP zone widths for the same pair" (SP:3956).

**How many zones: UNKNOWN as a rule.** Evidence: Pine table "5-9: IP Zones (5 rows)" (SP:3855); "5 IP zones = rows 5-9, 6 LSZ = 6 boxes" (SP:3932); Cross-Pair matrix has 5 IP roles + LSZ + Breakout Target (SP:1679-1685); "No table in the report may exceed 15 data rows" with the full IP Zone Map exempt (SP:1530-1536); synthesis shows "MODERATE and above zones only" (SP:1646).

**Zone names / roles**
- Assembly names (SP:1503): RESISTANCE CEILING, UPPER RESISTANCE, EQUILIBRIUM ZONE, MID-RANGE SUPPORT, KEY SUPPORT BAND, LIQUIDITY SWEEP ZONE, BREAKOUT EXTENSION TARGET.
- Translation-table roles add "DISCOVERY ZONE" and split LSZ into demand-side / supply-side and BREAKOUT TARGET into up / down (SP:3439-3448).
- Other flags: HIGH-DENSITY ZONE, TIGHT CONFLUENCE (SP:1499), POST-CONSOLIDATION ZONE (SP:1505), GAP IN-FILL LEVEL (SP:1507), Hidden Liquidity Zone (SP:1267), BREAKOUT RISK (SP:1504), RECAPTURE ZONE (SP:1086).
- Abbreviations in operator proofs: "MRS" and "EQ" (SP:2588, 2610); "Upper IP Resistance" (SP:2639).
- Pine categories: "RES", "MID", "SUP" (SP:3795); colour families "IP Resistance", "IP Equilibrium", "IP Support" (SP:3777-3779).
- UNKNOWN: the rule that decides which grouped zone gets which name (no ordering/position rule is stated beyond "RESISTANCE at top, SUPPORT at bottom", SP:3909).

---

## 4. Scoring

### 4.1 Six dimensions (SP:1467-1474)

| Dimension | 2 Points | 1 Point | 0 Points |
|:---|:---|:---|:---|
| Technical | Exact match (within 3 pips) | Zone match (within 10 pips) | No match |
| Options-Derived | Critical Option Wall (≥1.5B) or Pillar 8 high-confidence | Significant Magnet ($850M-$1.499B) or Pillar 8 moderate | No positioning |
| Analyst Consensus | 2+ Tier-1 sources agree | 1 source identifies | No analyst coverage |
| Structural | Exact price anchor + structural extreme | Proximity to anchor or structural extreme | No structural event |
| Psychological | Major big figure (.00, .50) | Quarter figure (.25, .75) | No round number |
| Regime/Dynamic | Zone in consolidation, will hold | Zone in momentum, may hold or fail | Zone in breakout, likely to fail |

CONFLICT (Options dimension for Tier 2): table gives Significant Magnet = 1 point (SP:1470); Pillar 3 gives "Tier 2 (SIGNIFICANT MAGNET): Options-Derived dimension score = 2" (SP:1139).

UNKNOWN: how P1 (pip-match scoring, SP:1059) and P2 (cluster scoring, SP:1088) combine inside the single Technical dimension.

### 4.2 Structural Extreme Bonus (SP:1477-1484)

| Condition | Bonus |
|:---|:---|
| Liquidity Sweep Target or Supply Ceiling Target from Step 0 | +1.0 |
| Repeated Extreme Magnet (2 dates) from Step 0.5 | +1.5 |
| Repeated Extreme Magnet (3+ dates) or Role Reversal from Step 0.5 | +2.0 |
| Confluent Floor/Ceiling from Step 0e | +2.0 |
| Institutional Magnet from Step 0.5d | +2.0 |

"Maximum Structural Extreme Bonus: +2.0. Maximum total score: 12 (base) + 2 (extreme bonus) = 14." (SP:1484).

### 4.3 Other additive modifiers stated in canon

| Modifier | Value | Cite |
|:---|:---|:---|
| Pivot LEGACY BONUS | +0.5 | SP:1059 |
| 180-day swing LEGACY BONUS | +0.5 | SP:1219 |
| MA RECAPTURE ZONE | "+2 bonus to confluence score" | SP:1086 |
| Option tier | "confluence score +3" / "+2" / "+1" | SP:1138-1140 |
| POST-CONSOLIDATION ZONE | +1 | SP:1505, SP:502 |
| POI Tier 1 / Tier 2 | "+2 confluence" / "+1 confluence" | SP:1512-1513 |
| Intra-zone key level | Structural = 0.5 | SP:1333 |
| Zone Spike | half Structural score | SP:1420 |

CONFLICT (cap): "max total = 14" (SP:1498, SP:1484) vs the additive modifiers above, which canon never reconciles with the 14 cap.

### 4.4 Pressure degree (SP:1487-1494)

| Score | Pressure Degree | Failure Probability |
|:---|:---|:---|
| 12-14 | EXTREME | <10% |
| 10-11 | HEAVY | 10-25% |
| 8-9 | MODERATE-HEAVY | 20-35% |
| 6-7 | MODERATE | 30-45% |
| 4-5 | LIGHT | 40-60% |
| 0-3 | MINIMAL | >60% |

Zone degree = "the group's highest-scoring level" (SP:1501). Labels must be spelled in full: ""MODERATE-HEAVY" is spelled out fully" (SP:3917). Examples: "EXTREME (12/14) | ZFP: 8%" (SP:3412); "HEAVY (10/14) | ZFP: 12%" (SP:3553).

### 4.5 POI tiers (SP:1510-1514)

| POI Tier | Condition | Action |
|:---|:---|:---|
| Tier 1 — Confluent POI | IP zone OVERLAPS with 4H BoM S/D (0X-1X) | Primary trade location. +2 confluence. |
| Tier 2 — IP-Only POI | IP zone exists but NO overlapping 4H BoM | Secondary trade location. +1 confluence. |
| Tier 3 — 4H-Only Level | 4H BoM exists but NO overlapping IP zone | Informational only. No primary trades. |

CONFLICT: synthesis column says "POI Tier | 1 / 2 / 3 (based on confluence score)" (SP:1638) vs the overlap-based definition above. Pine stores only "T1" or "T2" (SP:3797).

### 4.6 BoM / MoM per zone

- BoM: "The zone that ORIGINATED the directional move — the FIRST zone at the start of a trend leg. Identified by: zone is at the beginning of a clear impulse move, price left the zone with momentum, the zone is the "source" of the move." (SP:1148). → `ENTRY-PRIMARY` (SP:1150).
- MoM: "A zone that formed MID-MOVE as a continuation ... Identified by: zone formed during an ongoing move, not at the start, price paused here then continued." (SP:1149). → `TP-TARGET` (SP:1151). "4H MoM specific: Mark as `ONE-AND-DONE`" (SP:1152).
- FA: "BoM (Beginning of Move) supply/demand zones are the hottest Fire — the origin point of the move"; "MoM (Middle of Move) supply/demand zones are cooling Fire — continuation zones formed during the move" (FA:99-101). "MoM zones are ONLY to be used as LADDER STEPS for trend-aligned trades" (FA:521).
- Engine 3 Status mapping (SP:2216-2220): BoM → ENTRY-PRIMARY; MoM (tested, S/R aligned) → ENTRY-CONDITIONAL; MoM (virgin) → ENTRY-REJECT; MoM (depleted, 3+ reactions) → ENTRY-REJECT; 4H MoM → ENTRY-SCALP-ONLY. Column enum in the synthesis table: "ENTRY-PRIMARY / ENTRY-CONDITIONAL / TP-TARGET / REJECT" (SP:1643).
- CONFLICT (labels on chart): BoM/MoM is classified "For every IP zone" (SP:1147) vs "BoM/MoM tags belong to S/D zones only (which are not mapped on chart). IP zones use only the pressure degree label" (SP:287).

### 4.7 Zone reaction counter (SP:1156-1161; SP:495)

- "0 reactions (Virgin)": "Strongest if BoM (100% guaranteed reaction). DEATH ZONE if MoM".
- "1-2 reactions (Active)": "Zone still has juice."
- "3+ reactions (Depleted)": "Use for TP targeting only — NOT for entries."
- Priority rule: "If a pressure zone with juice (1-2 reactions) exists between current PA and the BoM zone, assume price will fully liquidate this initial pressure zone before touching the BoM zone." (SP:1161).
- UNKNOWN: the numeric definition of a "strong reaction". FA contains no reaction-counter definition (only the MoM-test decision tree, FA:545-562).

### 4.8 Definitions from the Fractal Architecture doc

- Liquidity = Earth: "All liquidity is Earth density. Liquidity Sweep Zones (LSZs, the green zones, the green blocks where liquidity sweeps happen) are standard Earth density. Institutional Pressure Zones are HEAVY Earth density — even denser, even stronger than normal liquidity zones." (FA:49).
- Engine 1 scope: "Maps the Earth density (liquidity + institutional pressure) and Fire density (supply/demand zones)" (FA:37); "Engine 1 maps Earth density (IP zones as HEAVY Earth, LSZs as standard Earth)" (FA:77); "Engine 1 maps Fire density (BoM/MoM S/D zones as Fire density structures)" (FA:115).
- Supply/demand = Fire: "Both supply and demand are Fire density." (FA:91). "the most powerful entries are at S/D + Liquidity overlap zones" (FA:279).
- Timeframe density: "A 4H move can pierce through 1H and 30m structures but will stop at another 4H structure." (FA:285).
- Thin vs thick liquidity: "Thin liquidity zones are NEVER allowed as entry or SL zones" (FA:65); numeric definition of thin/thick UNKNOWN.

---

## 5. Zone Failure Probability (ZFP) — zone strength

5.1 Base by zone type (Appendix B.1, SP:4056-4063):

| Zone Type | Criteria | Base Failure Prob |
|:---|:---|:---|
| Hard Wall | CRITICAL OPTION WALL (≥$1.5B) + 3+ pillars + Confluent Floor/Ceiling | 5-15% |
| Standard Wall | SIGNIFICANT MAGNET ($850M–$1.499B) + 2+ pillars | 15-30% |
| Soft Wall | No option wall (EXCLUDED tier, <$850M) or 1-2 pillars only | 30-50% |
| One-Touch | Only 1 pillar, no option wall | 50-70% |
| Post-Expiry Ghost | Option expired, structural memory remains | 20-40% |
| Liquidity Sweep Zone | Level at prior exact swing low from Step 0 | Special: brief breach then reversal |

5.2 Modifiers (Appendix B.2, SP:4067-4074):

| Signal | Modifier | Detection Method |
|:---|:---|:---|
| Option expiry timing (Spring Release) | +20-30% | Protocol A timestamps |
| Macro catalyst aligned against zone | +15-25% | Protocol F + web search |
| Increasing momentum toward zone | +10-20% | Rate of change in DXY |
| Cross-pair confirmation | +15-25% | Protocol A multi-pair |
| Cascade effect (prior zone broke) | +20-30% | Sequential zone failure |
| Regime change (EMA 200 cross) | +15-25% | Pillar 2 recapture detection |

5.3 Audit requirement: "Zone Failure Probability: Show the base probability and each modifier applied" (SP:397). UNKNOWN: how a point value is chosen inside each range; whether modifiers add or compound; any cap. All modifiers listed only increase ZFP.

5.4 Second table: the pressure-degree table also carries a "Failure Probability" column (§4.4, SP:1487-1494). Relationship to Appendix B is UNKNOWN (two separate mappings to the same quantity).

5.5 CONFLICT (third definition, Pine): `calcZFP` = `math.round(zoneW / refRange * 100.0)` with `refRange` DXY 1.60, EUR/USD 0.0200, GBP/USD 0.0200, AUD/USD 0.0150 (SP:3863-3867, table SP:3873-3876). This is zone width over a typical weekly range, unrelated to Appendix B. Changelog: "Zone Failure Probability percentage uses pair-specific reference ranges (DXY=1.60, EU/GU=0.0200, AU=0.0150) instead of a single fixed denominator." (SP:293).

5.6 ZFP thresholds consumed downstream: > 45% Measured Move (SP:1502); > 50% BREAKOUT RISK (SP:1504); SS bounds both < 30% (SP:1747); BS failing zone > 45%, PBS > 70% (SP:1752-1753); WL rejection zone < 20% (SP:1777); R zone 20-40% (SP:1778).

5.7 CONFLICT (Hard Wall threshold): "Hard Wall (ZFP < 20%, confluence ≥ 8)" (SP:1837) vs "Hard Wall Detection (ZFP<15%, confluence≥8)" (SP:2559) vs "Hard Wall (EXTREME/HEAVY pressure, ZFP < 15%)" (SP:2664) vs Appendix B Hard Wall base "5-15%" requiring a ≥$1.5B option wall (SP:4058).

5.8 Zone types named in canon: Hard Wall, Standard Wall, Soft Wall, One-Touch, Post-Expiry Ghost, Liquidity Sweep Zone (SP:4058-4063). Related tags: Institutional Magnet (SP:1310), Confluent Floor / Confluent Ceiling (SP:1240-1241).

---

## 6. Temporal anchor

6.1 Canon boundary: "The temporal boundary is the Friday 5:00 PM ET close of the week immediately prior to the target week." (SP:380). Header line: "Data As-Of: [Friday date] 17:00 ET — All data is pre-market-open for the target week of [Monday date]." (SP:1577). Timezone: ET.

6.2 Forbidden: "in-week daily OHLC data, in-week analyst reports, in-week economic data releases, in-week price action, in-week option expiry results" (SP:381). "If you are uncertain whether a data point existed before the temporal boundary, exclude it." (SP:383).

6.3 Operating moment: "If operating as the morning of Day 1 of the target week" (SP:903) — option data for Day 1 included if published by the boundary; Day 2 only if on the Day 1 page; Day 3+ excluded (SP:904-907).

6.4 CONFLICT (canon vs repo governance, outside the named sources): canon anchors at Friday 17:00 ET; the repo graph states "only bars <= analysis point exist (Monday London open ~02:00 ET = 06:00Z in EDT)" (`context_management/graph/build_graph.py:65`). FX bars between Sunday reopen and Monday 02:00 ET exist at the operator's anchor but are outside canon's boundary.

6.5 Data windows per timeframe

| Use | Window | Cite |
|:---|:---|:---|
| Weekly pivots | prior week H/L/C | SP:1012 |
| Daily pivots | each of last 3 trading days (extract last 5) | SP:1013, SP:983 |
| Extended weekly | last 4-8 weeks; overlap search up to 4 months (2-4 months in Step 3) | SP:972-973, SP:985 |
| 4H rare lookback | "up to 4 years prior" | SP:974 |
| D1 structural scan | 90 days; 180 if within 1.0 of a 90-180-day extreme | SP:1217-1219 |
| 4H S/D scan | 1H bars, last 60 calendar days, aggregated to 4H | SP:1345 |
| 4H zone age cut | "more than 3 weeks ago with no recent price interaction" | SP:1390 |
| 1H intra-zone zones | "prior 1-2 weeks" | SP:1321 |
| MA recapture | within 3 sessions | SP:1086 |
| Pine draw span | `tsL` = data-week Monday − 14 days; `tsR` = data-week Friday + 21 days | SP:3765-3766 |

6.6 Session clock used elsewhere: "London Session (2:00 AM – 12:00 PM ET)", "NY Session (12:00 PM – 5:00 PM ET)" (SP:698, SP:707); OTC cut "10:00 AM New York time" (SP:690).

---

## 7. Per-instrument differences

7.1 DXY is the only instrument for which Pillars 1-9 are written. P3 and P8 are DXY-only by construction (they turn component strikes into DXY levels).

7.2 Pairs get their own levels: "DXY provides DIRECTION. The PAIR provides LEVELS." (SP:3313). "Under NO circumstances may DXY price levels be arithmetically converted to pair price levels." (SP:3639). "The engine MUST run the complete 3-engine pipeline (Zone Map + Shape Chain + Trade Map) for each pair independently. DXY provides DIRECTIONAL CONVICTION only." (SP:101).

7.3 Pair zone ingredients (SP:3394-3400): "Pair MA confluence clusters (from TradingView)"; "Pair swing structure (from yfinance 4H data — prior week H/L/C, 90-day extremes)"; "Pair institutional S/R levels"; "Pair options data (from Protocol A if pair strikes are present)"; "Pair fib levels (from pair's own swing points)"; "Pair round numbers (for pairs, big figures are 1.1000, 1.1500, etc.)". Pair options are the pair's own strikes, "≥$850M" (SP:3498, SP:3509).

7.4 Role inversion and conviction transfer (SP:3439-3448): DXY RESISTANCE CEILING → pair SUPPORT FLOOR (same score); UPPER RESISTANCE → LOWER SUPPORT (same); EQUILIBRIUM ZONE → EQUILIBRIUM ZONE ("conviction = DXY score minus 2 (minimum 0)"); MID-RANGE SUPPORT → MID-RANGE RESISTANCE (same); KEY SUPPORT BAND → KEY RESISTANCE BAND (same); LSZ demand-side ↔ supply-side; BREAKOUT TARGET up ↔ BREAKDOWN TARGET down; DISCOVERY ZONE → DISCOVERY ZONE (reduced confidence). Matching rule: "Find the NEAREST pair-specific level that serves that role"; "Transfer the DXY zone's conviction score to the pair level" (SP:3406-3407).

7.5 AMBIGUOUS: SP:101 (full independent pipeline per pair) and SP:3407 (pair level inherits the DXY zone's score) describe two different ways a pair zone gets its pressure degree. Canon does not say which wins when a pair's own 9-pillar score differs from the transferred score.

7.6 Adjustments on pairs: Layer 2 verification 7/7 full score; 5-6/7 "conviction score minus 1"; 3-4/7 "minus 2"; <3/7 EXCLUDE (SP:3470-3473). Divergence: "Reduce conviction by 2 points" (SP:3634). "translated zone within 100 pips of verified structural level" (SP:3464). Zone-role override: "the pair data takes precedence for the ZONE ROLE assignment" (SP:3647). Most Layer 2 requirements are external data (2 spot sources, analyst levels, MA signal counts, SP:3458-3463).

7.7 Pair LSZ: "The pair LSZ price levels come from the PAIR's own swing structure, NOT from DXY LSZ levels." (SP:3575). Examples are 10 pips wide: "EUR/USD LSZ at 1.1700-1.1710 (supply)", "1.1400-1.1410 (demand)" (SP:3572-3573).

7.8 Constants that differ by instrument

| Item | DXY | EUR/USD | GBP/USD | AUD/USD | Cite |
|:---|:---|:---|:---|:---|:---|
| Pip | 0.01 | 0.0001 | 0.0001 | 0.0001 | SP:2610; SP:3874-3876 |
| Price format | "#.##" | "#.####" | "#.####" | "#.####" | SP:3882-3885 |
| Pine ZFP reference range | 1.60 | 0.0200 | 0.0200 | 0.0150 | SP:3873-3876 |
| Ticker match | "DXY", "DX-Y.NYB", contains "DXY" | "EURUSD", "EURUSD=X" | "GBPUSD", "GBPUSD=X" | "AUDUSD", "AUDUSD=X" | SP:3745-3748 |
| Sanity: zone prices within 3% of verified spot | — | yes | yes | yes | SP:3952 |

7.9 Behavioural profiles: EUR/USD "PA directly touches S/D-liquidity overlap (no Earth/Liquidity Shield between Fire and Earth), primary swing pair" (SP:675); GBP/USD "Earth/Liquidity is the only thing respected (S/D gets pierced), Liquidity Shields (Earth) protect unmitigated S/D (Fire) zones, primary scalp pair" (SP:676); DXY "maps master direction, wakes up during NY" (SP:678). FA:596-648 repeats these.

7.10 Clustering / wick / LSZ / move-size tolerances in pair units: UNKNOWN (see §3).

---

## 8. E1 report output — what a zone row contains

8.1 Synthesis table columns, MODERATE and above only (SP:1633-1646): Zone Name; Range; Pressure Degree ("Extreme / Heavy / Moderate-Heavy / Moderate / Light / Minimal"); POI Tier ("1 / 2 / 3"); ZFP; BoM Fresh Flag ("BoM=Fresh origin zone, MoM=Continuation zone"); Liquidity Sweep Status ("Swept / Unswept / Partial"); Ladder Step Status ("Y/N"); Engine 3 Status ("ENTRY-PRIMARY / ENTRY-CONDITIONAL / TP-TARGET / REJECT"); Primary Trade Setup.

8.2 Engine 3 Status column is mandatory in every IP zone table (SP:103).

8.3 Zone audit string format used in canon: "[Zone Name] | [Range] | [Pressure Degree] ([Score]/14) | ZFP: [X]%" (SP:3666).

8.4 Other E1 report sections (SP:1587-1602): 2 Zone Map; 3 Synthesis; 4 4H Zone Classification Overlay Summary; 5 Liquidity Sweep Zone Summary; 6 Pivot Verification Audit Trail; 7 K Factor Audit Trail; 8 Clustering Scan Results; 9 4H Zone Verification Audit Trail; 15 Breakout Risk Alerts; 16 Missing Data Log. Pair sections 21-29 (SP:1610-1618).

8.5 LSZ row (SP:1276-1279): range | Type | Source | Confluent with | Function | Priority.

8.6 4H zone row (SP:1395): type, mitigation, Demand/Supply, range, formed dates.

8.7 Intra-zone row (SP:1337-1338): Level | Type | Source.

8.8 Pine data per zone (SP:3793-3802): `zTp`, `zBt`, `zCat` ("RES", "MID", "SUP"), `zDeg`, `zTir` ("T1" or "T2"), `zNm`; LSZ `xTp`, `xBt`, `xPri` ("ACTIVE" or "STANDARD"). Label: ""{ZoneName} | {PressureDegree} | {ZFP}% ZFP"" centred at `(tsMid, (tp+bt)/2)` (SP:3831-3832). Fills `color.new(base_color, 70)` (SP:3784); Equilibrium base `#FF9800` (SP:3778); Resistance RED "RGB 180,40,30 → 240,160,90", Support TEAL "RGB 0,150,150 → 80,210,200" (SP:3777-3779); LSZ GREEN "RGB 40,180,80", Active "RGB 80,230,100" (SP:3780-3781); LSZ has no labels (SP:3836). Sort "highest price to lowest price" (SP:3909). S/D zones are not drawn (SP:3714).

8.9 Supplementary (outside named sources): `IPZone` dataclass fields `name, top, bottom, category, pressure, tier, confluence, zfp, key_levels, sd_type, sd_fresh, reaction_count, sd_overlap, formed_after_consolidation` (E3PY:128-145).

---

## 9. MINIMUM OHLC-ONLY E1

Everything below is computable from the instrument's own OHLC history that exists at the anchor. Constants are in DXY units as canon writes them; pair-unit equivalents are UNKNOWN (§3) and must be decided by the operator/orchestrator, not assumed.

**9.1 Data cut.** Use only bars closed at or before the boundary: canon "Friday 5:00 PM ET" (SP:380). (Repo governance says Monday ~02:00 ET — CONFLICT §6.4.)

**9.2 Level sources**

| # | Level set | Rule | Constants | Cite |
|:---|:---|:---|:---|:---|
| A | Weekly pivots ×3 variants | prior week H/L/C | formulas §1.1.2-1.1.4; 0.382, 0.618, 1.000; 1.1/2, 1.1/4, 1.1/6, 1.1/12 | SP:989-1012 |
| B | Daily pivots ×3 variants | each of last 3 trading days of prior week | same formulas | SP:1013 |
| C | Historical-week pivots | weeks whose range overlaps current range, past 2-4 months | — | SP:985, SP:1014 |
| D | MA grid | EMA and SMA 9, 10, 20, 50, 100, 200 (daily by inference §1.2.2) | cluster 3+ within 0.15; weights 3.0/2.0/1.5/1.0/0.5 | SP:1073-1084 |
| E | MA recapture | close crossed above MA 50/100/200 within 3 sessions | +2 | SP:1086 |
| F | D1 swing lows (Liquidity Sweep Targets) | 90 D1 bars; lower wick ≥ 0.15 and close in upper 50% of range | 90; 0.15; 50% | SP:1217, SP:1223 |
| G | D1 swing highs (Supply Ceiling Targets) | upper wick ≥ 0.15 and close in lower 50% | 0.15; 50% | SP:1230 |
| H | 180-day extension | if current price within 1.0 of a 90-180-day swing extreme | 1.0; +0.5 legacy | SP:1219 |
| I | D1 order blocks | 1-3 consecutive same-direction large-body candles before a move ≥ 1.0 lasting ≥ 5 trading days; zone = [Low, High] of base | 1.0/5; high-conviction 2.0/10 | SP:1235-1237 |
| J | Confluent Floor / Ceiling | F inside demand OB; G inside supply OB | Structural 2 + bonus +2 | SP:1240-1242 |
| K | LSZ | [low, low+0.05]; [high−0.05, high]; extension 0.05-0.10 (direction CONFLICT §1.5.15) | 0.05; 0.05-0.10 | SP:1257, 1261, 1286 |
| L | Repeated Extreme Magnets | swing extremes within 0.05 on 2+ dates; role reversal low≈high | 0.05; +1.5 / +2.0 / +2.0 | SP:1293-1308 |
| M | Institutional Magnet | L inside I | max Structural | SP:1310 |
| N | 4H S/D zones | 1H→4H, last 60 calendar days; move ≥ 0.5 lasting ≥ 3 trading days; origin candle [Low, High]; reject if width > 0.40, age > 3 weeks w/o interaction, MoM 3X+ in opposing trend, or > 0.50 from any IP zone unless BoM 0X-1X | 60; 0.5/3; 0.40; 3 weeks; 0.50 | SP:1345-1391 |
| O | Mitigation count per 4H zone | 0X/1X/2X/3X/4-5X | table §1.5.27 | SP:1381-1385 |
| P | Round numbers | .00 and .50 = 2 pts; .25 and .75 = 1 pt (DXY) | step 0.25 (derived) | SP:1473 |
| Q | Prior daily closes | intra-zone key levels | — | SP:1323 |
| R | Fib of prior-week range | ratio list UNKNOWN for P6; 0.382 / 0.618 documented for intra-zone; 0.236 / 0.382 / 1.618 in Dimension 2 | — | SP:1426, 1322, 684-685 |

**9.3 Scoring available without external data** (dimension table SP:1467-1474)
- Technical: 2 if within 3 pips, 1 if within 10 pips (SP:1469); MA triple+ cluster 2 / double 1 / single 0.5 (SP:1088).
- Structural: 2 "Exact price anchor + structural extreme"; 1 "Proximity to anchor or structural extreme" (SP:1472).
- Psychological: 2 for .00/.50; 1 for .25/.75 (SP:1473).
- Regime/Dynamic: 2 consolidation / 1 momentum / 0 breakout (SP:1474); classifier UNKNOWN.
- Options-Derived = 0 "No positioning" (SP:1470); Analyst Consensus = 0 "No analyst coverage" (SP:1471).
- Structural Extreme Bonus up to +2.0 (SP:1479-1484).
- Post-consolidation +1 (SP:1505); POI tier +2 / +1 (SP:1512-1513).
- Derived ceiling: 8 base + 2 bonus = 10 → HEAVY at most under the strict 14-point scale; EXTREME (12-14) is unreachable without options/analyst unless the extra modifiers of §4.3 are counted (CONFLICT §4.3).

**9.4 Assembly** (SP:1497-1505): sort high→low; cluster 3+ within 0.15 = HIGH-DENSITY ZONE; pairs within 0.10 = TIGHT CONFLUENCE; group at 0.10-0.15; zone degree = highest-scoring member; pressure table §4.4; names from SP:1503; gap scan ≥ 0.20 with 2+ signals = GAP IN-FILL LEVEL (SP:1507); hidden liquidity for gaps ≥ 0.15 (SP:1264); POI tier by 4H BoM (0X-1X) overlap (SP:1512-1514).

**9.5 ZFP without options** (SP:4060-4061, 4067-4074): base "Soft Wall ... 30-50%" (no option wall or 1-2 pillars) or "One-Touch ... 50-70%" (1 pillar); OHLC-detectable modifiers: momentum toward zone +10-20%, cascade +20-30%, EMA-200 cross +15-25%. Hard Wall (5-15%) and Standard Wall (15-30%) both require an option wall by their stated criteria, so they are not reachable from OHLC alone. Alternative mapping from score: pressure-degree failure column §4.4.

**9.6 Per-zone properties computable from OHLC:** top, bottom, category, score, pressure degree, POI tier, BoM/MoM (SP:1148-1149), mitigation / reaction count (definition of "strong reaction" UNKNOWN), LSZ status, POST-CONSOLIDATION flag (consolidation detector UNKNOWN), intra-zone key levels (SP:1320-1329).

**9.7 Not computable from OHLC (drop, score 0, log as missing):** P3, P4, P7, P8; Layer 2 requirements 1, 3, 4, 6 (SP:3458-3463); ZFP modifiers for expiry timing, macro catalyst, cross-pair (SP:4069-4072).

---

## 10. E1-related changelog entries (SP:7-360)

| Version | Entry | Cite |
|:---|:---|:---|
| v5.3.3 #8 | Section 5.2.1 synthesis format and 5.3 Missing Data Log filled | SP:27 |
| v5.3.1 #1 | "EARTH = LIQUIDITY ... IP Zones ... = HEAVY Earth density"; S/D zones are Fire | SP:45-47 |
| v5.3.0 #3 | HTF zone mechanics decision tree "bridges Engine 1 zone classification with Engine 2 shape prediction" | SP:69 |
| v5.2.3 #3 | Engine 3 Status column mandatory in every IP zone table | SP:103 |
| v5.2.3 #7 | No generic zone ranges; anchor to 4H candle origins, swing H/L, option strikes, MA crossovers | SP:111 |
| v5.2.1 #8 | "+1 confluence bonus for zones formed after consolidation. Tagged as "POST-CONSOLIDATION ZONE"" | SP:173 |
| v5.2.0 #2 | BoM = entry candidates; MoM = TP targets; virgin MoM = death zones | SP:187-192 |
| v5.2.0 #5 | Zone Reaction Counter: "0 = virgin, 1-2 = active (has juice), 3+ = depleted (likely to pierce)" | SP:209-212 |
| v5.2.0 #11 | 4H MoM one-and-done | SP:246-249 |
| v5.2.0 #15 | CRITICAL OPTION WALL ≥$1.5B; SIGNIFICANT MAGNET $850M–$1.499B; EXCLUDED <$850M | SP:269-273 |
| v5.1.0 #2 | S/D zones excluded from chart mapping; only IP zones, LSZ, option strikes auto-mapped | SP:279 |
| v5.1.0 #3 | Zone date range 2 weeks back + 3 weeks forward; `xloc.bar_time` only | SP:281 |
| v5.1.0 #4 | BoM/MoM terminology codified | SP:283 |
| v5.1.0 #5 | Equilibrium colour #FF9800 | SP:285 |
| v5.1.0 #6 | No BoM/MoM labels on IP zones; pressure degree label only | SP:287 |
| v5.1.0 #9 | ZFP pair-specific reference ranges DXY=1.60, EU/GU=0.0200, AU=0.0150 | SP:293 |
| v5.0.0 D1-D6 | Filter checkpoint, three-tier classification, audit line, zone synthesis re-verification, max table density, compliance sweep | SP:310-315 |
| v5.0.0 P3 | Intra-Zone Key Level Scan (Step 0.6) | SP:320 |
| v5.0.0 P5 | "LSZ Bottom Edge Extension — sweep scan 0.05-0.10 DXY below swing highs" | SP:322 |
| v5.0.0 P6 | Key Support Band tightening — core vs spike | SP:323 |
| v4.5.2 | "POI Tier Classification replaces AGREE/DISAGREE/DECISION overlay"; "Order Block definition corrected — candle color does NOT matter"; "Noise rejection threshold raised for DXY (0.30→0.50), BoM 0X-1X exception added" | SP:343 |
| v4.5.1 | "4H zone construction from singular candle preceding strong move"; "Dedicated liquidity sweep scan"; "Dedicated Synthesis section" | SP:345 |

---

## 11. Consolidated CONFLICT / UNKNOWN register

**CONFLICT**
1. Daily pivot depth: extract 5 days (SP:983) vs compute 3 days (SP:1013).
2. Pivot count "42" (SP:969) vs 22 per timeframe from the formulas.
3. Option conversion floor ≥$500M (SP:1121) vs threshold $850M (SP:1135).
4. Options dimension for Significant Magnet: 1 pt (SP:1470) vs 2 (SP:1139).
5. Order-block candle colour: bullish/bearish required (SP:1235-1236) vs "Candle color does NOT matter" (SP:482, SP:343).
6. LSZ side of the extreme: inside (SP:1257, 1261) vs beyond/below-low/above-high (SP:1286, SP:3572-3573).
7. POI Tier basis: 4H BoM overlap (SP:1510-1514) vs "based on confluence score" (SP:1638).
8. Score cap 14 (SP:1484) vs unreconciled additive modifiers (§4.3).
9. ZFP: Appendix B (SP:4056-4074) vs pressure-degree column (SP:1487-1494) vs Pine width ratio (SP:3863-3867).
10. Hard Wall threshold: ZFP <20% (SP:1837) vs <15% (SP:2559, SP:2664) vs option-wall criteria (SP:4058).
11. BoM/MoM on IP zones: classify every IP zone (SP:1147) vs tags belong to S/D zones only (SP:287).
12. Temporal anchor: canon Friday 17:00 ET (SP:380) vs repo graph Monday ~02:00 ET (`context_management/graph/build_graph.py:65`).
13. Pair tolerance scaling: 0.01 DXY ≡ 1 pip (E3PY:666-669, supplementary) vs ≈2 pips (SP:4035-4039, scoped to Pillar 8 only).

**UNKNOWN (not in the named sources)**
1. Pillar 6 procedure: fib ratio list, anchors beyond "prior week range + extended swing points", round-number confluence bonus, pair round-number step.
2. Pillar 9 procedure: regime classifier, breakout pre-conditions, Measured Move formula, how ZFP point values and modifiers are combined.
3. Pillar 7 procedure; Pillar 8 confidence-weighting detail; Pillar 5 Steps 0g, 0h, 1-5; meaning of HWC/LWC.
4. Bar-count definition of a swing high/low; "large bodies" threshold; wick measurement basis.
5. MA timeframe (daily by inference only); how MA weights are used; double-cluster tolerance.
6. What a pivot is "matched" against for Technical scoring; how P1 and P2 combine in the Technical dimension.
7. Zone top/bottom rule; min/max IP zone width; number of zones; rule assigning the seven names.
8. All tolerances in EURUSD / GBPUSD price units.
9. Numeric definition of a "strong reaction", of "consolidation" for the +1 modifier, and of thin vs thick liquidity.
10. 4H bucket alignment for the 1H→4H aggregation.
11. Which pair pressure score wins: pair's own pipeline (SP:101) or the transferred DXY score (SP:3407).
