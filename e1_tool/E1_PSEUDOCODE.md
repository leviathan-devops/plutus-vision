# E1 — the prompt's Engine 1, as pseudocode (translation only; nothing added)

Sources (line numbers refer to these files):
- **P533** = `canon/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md`
- **P452** = `Original_Canon_Data/TTE System Prompts/Trident_Trading_Engine_System_Prompt_v4.5.2 (1).md` (used where P533 says "[unchanged from v4.5.2]")
- **REPORT** = `Leviathan_DXY_IL_Report_Apr20-24_2026.pdf` (the output this program must reproduce for that week)
Operator rulings: mandatory inputs = investingLive option expiries, TradingView OHLC, the whole 9-pillar / 6-dimension computation. Anything else: fetch if reachable, else `NO DATA` as the report does.

```
INPUT  : target_week (Monday date), symbol = DXY
BOUNDARY = Friday 17:00 ET before the target week for price data (REPORT p.1 "Data As-Of");
           option data: Day-1 page published on/before the boundary morning + Day-2 forward rows on that page (P533:899-916)

# ── PROTOCOL A  OTC FX option expiries (P533:808-918) ─────────────────────────────────────────
A1  fetch investingLive "fx-option-expiries-for-DD-MMM-10am-new-york-cut-YYYYMMDD" page for Day 1          (P533:817-829)
A2  read the table image three times; a value is CONFIRMED when >= 2 of 3 reads agree, else UNCLEAR/dropped   (P533:836-853)
A3  pair filter R1: EUR/USD, GBP/USD, AUD/USD go to the expiry summary; other pairs go to Pillar 3 only       (P533:859)
A4  notional filter R2: Tier 1 >= $1.5B CRITICAL OPTION WALL · Tier 2 $850M-$1.499B SIGNIFICANT MAGNET · Tier 3 < $850M EXCLUDED  (P533:861-867)
A5  missing day -> "[NO DATA ...]", never reuse another day's data                                            (P533:889-897)
A6  temporal audit line per day: source URL, published time, INCLUDED / EXCLUDED                              (P533:909-916)

# ── PROTOCOL B  9 pillars (P533:922-1459, P452 for placeholders) ──────────────────────────────
PILLAR 1  pivots (P533:967-1059)
  weekly H,L,C of the prior week; daily H,L,C of EACH of the last 5 trading days (pivots computed for each of the last 3)
  classic  PP=(H+L+C)/3  R1=2PP-L S1=2PP-H  R2=PP+(H-L) S2=PP-(H-L)  R3=H+2(PP-L) S3=L-2(H-PP)
  fib      R1/S1=PP±0.382(H-L)  R2/S2=PP±0.618(H-L)  R3/S3=PP±1.000(H-L)
  camarilla R4/S4=C±(H-L)*1.1/2  R3/S3=C±(H-L)*1.1/4  R2/S2=C±(H-L)*1.1/6  R1/S1=C±(H-L)*1.1/12
  keep ALL levels (no spot-proximity filter); run the four verification checks and print them (P533:1017-1057)
  score: exact match within 3 pips = 2 (Technical); zone match within 10 pips = 1                              (P533:1059)

PILLAR 2  MA confluence grid (P533:1065-1088)
  EMA and SMA 9, 10, 20, 50, 100, 200 (daily); weights 200=3.0, 100=2.0, 50=1.5, 20=1.0, 9/10=0.5
  cluster = 3+ MAs within 0.15; recapture: price crossed above MA 50/100/200 within 3 sessions -> RECAPTURE ZONE, +2
  score: triple+ cluster = 2 (Technical), double = 1, single MA = 0.5

PILLAR 3  component-pair strike -> DXY (P533:1092-1165)
  DXY = 50.14348112 * EURUSD^-0.576 * USDJPY^0.136 * GBPUSD^-0.119 * USDCAD^0.091 * USDSEK^0.042 * USDCHF^0.036
  spot rates for the 6 pairs (Fed H.10; supplementary source allowed and flagged, band widened +0.03 / +0.07)   (P533:1107-1119)
  for each large expiry: vary only that pair to its strike, others at spot -> DXY equivalent
  tiers as A4; confluence +3 (tier 1), +2 (tier 2), +1 (tier-3 override)                                      (P533:1127-1140)

PILLAR 4  institutional commentary (P533:1169-1199)  OPTIONAL per operator -> fetch if reachable, else NO DATA
  explicit S/R levels only; tier weights 3.0 / 2.0 / 1.0; 2+ tier-1 sources agree = 2 (Analyst), 1 source = 1

PILLAR 5  structural extremes, anchors, liquidity engineering
  STEP 0   90 daily bars (P533:1213-1244)
    0b  swing LOW with lower wick >= 0.15 AND close in the upper 50% of the day's range -> "Liquidity Sweep Target", exact price + date
    0c  swing HIGH with upper wick >= 0.15 AND close in the lower 50% -> "Supply Ceiling Target"
    0d  D1 order blocks: base of 1-3 consecutive large-bodied bullish (bearish) candles before a rally (decline) >= 1.0 lasting >= 5 trading days
        zone = [low of base, high of base]; >= 2.0 and >= 10 days -> "High-Conviction Order Block"
    0e  sweep target inside a demand zone = "Confluent Floor"; ceiling target inside a supply zone = "Confluent Ceiling" (Structural 2, bonus +2)
  STEP 0.45  liquidity sweep zones (P533:1246-1286)
    each swing low  -> LSZ [low, low+0.05] demand-side ; each swing high -> LSZ [high-0.05, high] supply-side
    hidden liquidity zone: gap >= 0.15 between IP zones holding a 4H swing extreme or a 4H BoM zone
    LSZ overlapping a 4H BoM zone -> "CONFLUENT LIQUIDITY SWEEP + BoM ZONE"; LSZ within 0.30 of spot -> "ACTIVE SL TRIGGER"
  STEP 0.5  repeated extreme magnets (P533:1288-1310)
    two swing lows (or highs) within 0.05 = repeated level; low coinciding with a prior high = role reversal
    price = average weighted by wick size; bonus 2 dates +1.5, 3+ dates +2.0, role reversal +2.0; inside a D1 order block = "Institutional Magnet"
  STEP 0f  4H supply/demand (P452:637-745)
    4H bars for the last 60 calendar days
    find a directional move >= 0.5 lasting >= 3 trading days; the SINGLE candle immediately before it = origin candle
    zone = [Low, High] of that candle, date-stamped; verify: matches a real candle, next candle moved directionally, no overlap with an opposite zone
    move >= 1.0 and >= 5 days -> "High-Conviction 4H OB"
    BoM = where the move began; MoM = continuation base during the move; when in doubt MoM
    mitigation count over the prior 2-3 weeks: soft (wick taps edge, rejected) / hard (bodies enter and consolidate)
    reject: wider than 0.40 · MoM with 3X+ hard mitigations in opposing trend · older than 3 weeks with no recent interaction ·
            no IP zone within 0.50 unless BoM 0X-1X (kept, flagged "4H-Only Level")
    print the audit trail (origin OHLC, move, next candle, overlap check)
  STEP 0g  1H precision anchors (P452:749-763): only (A) nested inside a 4H/D1 zone, or (B) filling a >= 0.20 gap; 2-3 candle base before >= 0.3 lasting >= 1 day
  STEP 0h  minor swing levels (P452:767-781): wick >= 0.08 and close in upper/lower 40%, D1 and 4H; Structural 0.5
  STEPS 1-5 (P452:785-831)
    1  anchors: prior daily close (last 3-5 days), prior daily high/low for each of the last 5 days, prior weekly close, prior weekly high/low
    2  HWC / LWC (highest / lowest weekly close of the period)        [source forex.com: optional; computable from weekly closes]
    3  recapture: price recently crossed EMA 200 or another major MA
    4  structural extreme memory beyond 90 days (web search)           OPTIONAL -> NO DATA if unreachable
    5  scoring: exact anchor = 2, proximity = 1 (Structural); bonuses as in the synthesis table, max +2

PILLAR 6  fib + round numbers (P452:835-862)
  fib 23.6 / 38.2 / 50.0 / 61.8 % of the prior week range (H - r*(H-L)); same from the most recent significant swing high/low
  round numbers .00, .50, .25/.75; bonus +2 / +1.5 / +1; score: fib within 5 pips + round number = 2, fib only = 1

PILLAR 7  derivatives arena (P452:866-886)  OPTIONAL -> "[NO DATA — DX options OI supplementary feed inaccessible; 9-Pillar primary mapping active]"

PILLAR 8  EUR/USD strike -> DXY, primary (P452:890-950 with P533:1436-1451 tiers)
  K = 50.14348112 * USDJPY^0.136 * GBPUSD^-0.119 * USDCAD^0.091 * USDSEK^0.042 * USDCHF^0.036 ; DXY_level = K * strike^-0.576
  tiers: >= 1.5B tier 1 band ±0.07 · 850M-1.499B tier 2 band ±0.10 · below: excluded (override ±0.15)
  expiries within 10 pips aggregate (total >= 2B = one 2B+ expiry); union across included days; print K audit trail and reverse validation

PILLAR 9  ZFP (P452:954-1071)
  base by zone type: Hard Wall 5-15 · Standard Wall 15-30 · Soft Wall 30-50 · One-Touch 50-70 · Post-Expiry Ghost 20-40 · LSZ special
  + modifiers (expiry timing, macro catalyst, momentum, cross-pair, cascade, EMA-200 regime change, extreme-magnet proximity), cap 95
  measured move when ZFP > 45; regime: consolidation / momentum / breakout / regime change
  Regime dimension: ZFP < 20 in consolidation = 2 · 20-50 = 1 · > 50 = 0

# ── SYNTHESIS (P452:1075-1205 = P533:1461-1514) ───────────────────────────────────────────────
S1  collect ALL levels from all pillars, sort high to low, no spot filter
S2  score each level: Technical, Options, Analyst, Structural, Psychological, Regime (0-2 each) + structural-extreme bonus (max +2) = 0-14
S3  clustering scan: for each level count others within 0.15; 3+ = HIGH-DENSITY ZONE; pair within 0.10 = TIGHT CONFLUENCE; none within 0.15 = ISOLATED; print it
S4  group into zones where levels cluster within 0.10-0.15
S5  zone pressure degree = its highest-scoring level: 12-14 EXTREME · 10-11 HEAVY · 8-9 MODERATE-HEAVY · 6-7 MODERATE · 4-5 LIGHT · 0-3 MINIMAL
S6  ZFP from Pillar 9; measured move if > 45; > 50 flagged BREAKOUT RISK
S7  name: RESISTANCE CEILING, UPPER RESISTANCE, EQUILIBRIUM ZONE, MID-RANGE SUPPORT, KEY SUPPORT BAND (+ LSZ, BREAKOUT EXTENSION TARGET)
S8  gap scan (Step 9.5): gaps >= 0.20 between zones; candidate with 2+ supporting signals = GAP IN-FILL LEVEL (Structural 1)
S9  4H overlay (Step 9.7): IP zone overlapping a 4H BoM 0X-1X = Tier 1 (+2, cap 14); no BoM overlap = Tier 2 (+1); 4H BoM without IP zone = Tier 3
S10 report table: MODERATE and above only — Zone, Range, Pressure, Score, ZFP, POI Tier, Key Drivers; per-zone detail: 4H overlay, BoM fresh, LSZ, ladder step

OUTPUT : the report's sections 1-9 as data  ->  a Pine script in the form of Original_Canon_Data/Pine Scripts/trident_v8.pine
         (IP zones red / orange / teal by RES / MID / SUP, LSZ green, option strike lines amber)
```
