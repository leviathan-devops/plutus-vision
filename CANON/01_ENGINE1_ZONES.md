# CANON 01 — ENGINE 1: THE ZONE MAP (WHERE ARE THE WALLS?)

Authority: `Trident_System_Prompt_v5.3.3` Part II (2.0–2.3), Part III §3.2 Protocol B,
§10.6–10.7, Appendix B. E1 is **live-market validated, ~95% accurate, IMMUTABLE.**

E1 answers one question: **where are the walls, and how strong is each one?** It produces an
*Institutional Pressure Zone Map* — an ordered ladder of price zones, each with a pressure
degree, a failure probability, a BoM/MoM classification, a reaction count, and a POI tier.

---

## 1 · THE FIRST PRINCIPLE — ZONES ARE MEMORY, NOT LINES

> A zone is not a line on a chart — it is a **memory of institutional intent.**

When price returns to where banks previously built large positions, those positions are either
**defended** (the zone holds) or **unwound** (the zone fails). Zone strength = how much volume
was transacted there × how much of it remains unmitigated.

Corollary — **IL LEVELS ARE CAUSE, NOT EFFECT**: the current spot price does NOT determine the
levels; the levels determine where spot will go. The spot price exists only to say where price
is right now. **Therefore: NEVER filter, discard or deprioritise a level because it is far from
spot.** All levels from all pillars are retained and scored on their own merits.

---

## 2 · THE 9-PILLAR / 6-DIMENSION ENGINE

DXY has no 10am daily FX option expiry, so its pressure map is built from **9 pillars across 6
independent dimensions** plus a Structural Extreme Bonus. The UUP ETF proxy is **permanently
terminated** — never substitute an equity ETF.

| Pillar | Name | Captures | Typical yield |
|---|---|---|---|
| 1 | **Multi-Timeframe Pivot Engine** | 3 pivot variants × 2 TFs (42 levels). Class. Fib. Camarilla. | **8/11 verified levels** (the single most powerful pillar) |
| 2 | **Moving Average Confluence Grid** | EMA/SMA 9,10,20,50,100,200; clusters | 3–4/11 |
| 3 | **Component-Pair Option-Expiry Conversion** | expiry strikes → DXY equivalents via the formula | secondary (primary for the non-EUR pairs) |
| 4 | **Institutional Commentary Harvesting** | explicit S/R from analyst desks, tier-weighted | — |
| 5 | **Structural Extreme Scan + Liquidity Engineering** | swings, order blocks, magnets, HWC/LWC, LSZs | the structural backbone |
| 6 | **Fibonacci Retracement & Round-Number Grid** | prior-week range Fibs + big figures | — |
| 7 | **Derivatives Arena Boundary** | ICE/CME supplementary, fallback to 9-pillar | — |
| 8 | **EUR/USD Strike→DXY Primary Conversion** | exploits EUR's 62.4% DXY weight | primary options signal |
| 9 | **Regime Detection, Zone Failure Prediction & Breakout Magnitude** | assigns **ZFP**, Measured Move projection, regime, breakout alerts | the predictor |

**The 6 dimensions of independence** (each has a failure mode + a recovery partner — this is a
redundancy architecture, not a checklist):
Technical (regime change→options+analyst) · Options-Derived (low-volume days→technical+structural)
· Analyst Consensus (herding/lag→technical+options) · Structural (obsolete levels→options+
psychological) · Psychological (volatility override→technical+structural) · Regime/Dynamic
(false breakout→technical+options).

### 2.1 DXY formula and why it dominates the design
```
DXY = 50.14348112 × EURUSD^(-0.576) × USDJPY^(0.136) × GBPUSD^(-0.119)
      × USDCAD^(0.091) × USDSEK^(0.042) × USDCHF^(0.036)
```
EUR/USD carries **62.4%** of the index and is **5.2× more impactful per pip** than the next
component. That single fact is why Pillar 8 exists as its own pillar.

**CATEGORICAL ERROR TO NEVER REPEAT (v4.5.2):** DXY price levels **cannot** be arithmetically
converted into pair price levels. The v4.5.2 report did this and produced levels **355–710 pips
off reality**. DXY provides **DIRECTIONAL CONVICTION**; the pair provides **ITS OWN PRICE
LEVELS** from its own structure. See CANON/06 for the full prohibition list.

---

## 3 · ZONE CONSTRUCTION — THE SINGULAR CANDLE LAW (zero tolerance)

S/D zones are constructed from the **SINGULAR candle immediately preceding a strong directional
move** — *not* a cluster, *not* an interpolated range, *never* fabricated.

```
1. Identify a strong directional move (≥0.5 DXY pts, ≥3 trading days)
2. Locate the SINGLE candle immediately BEFORE that move  → the "origin candle"
3. Zone range = [Low of origin candle, High of origin candle]
4. Date-stamp the origin candle
```

**PROHIBITED (each = data fabrication):** a range matching no real candle; a supply zone
overlapping a demand zone at the same TF; zones from rounded estimates; a zone >0.40 DXY wide
without explicit verification; inventing a BoM/MoM label with no visible candle.

**Mandatory verification per zone:** range matches a real candle exactly; the candle *after* it
moved directionally; no same-TF opposite overlap; the date is a real trading date.

**Order block, defined correctly:** the LAST SHORT candle before a BIG impulsive swing. **Candle
colour does not matter.** What defines it is (1) a short candle relative to the subsequent move,
then (2) large impulsive displacement. Direction comes from market structure + IP zone
direction, **not** from the candle's colour — a bearish candle before a bullish impulse can be a
bullish order block.

### 3.1 BoM / MoM classification
- **BoM** — the zone that ORIGINATED the directional move; first zone at the start of a trend
  leg; price left with momentum. `ENTRY-PRIMARY`. **100% guaranteed reaction if unmitigated.**
- **MoM** — formed MID-MOVE as a continuation; a reaction point along the path, not the origin.
  `TP-TARGET` for the opposing direction. Entry only via the strict exceptions.
- **4H MoM = ONE-AND-DONE** — first retest gives a minor reaction, then a strong pierce.

**Hierarchy rule (zero tolerance):** **Zone Type > Mitigation Level > Trend Context.** An
unmitigated MoM in an opposing trend is *weaker* than a 2X-mitigated BoM.

### 3.2 Mitigation tracking
| Count | Strength | Expected behaviour |
|---|---|---|
| 0X (unmitigated) | **Fortress** | 100% reaction for BoM. Will hold. |
| 1X | ~unmitigated | Still very strong |
| 2X | weakened | Context-dependent |
| 3X | likely to fail | Expect failure |
| 4–5X still holding | **PARADOX SIGNAL** | Extremely strong pressure behind the zone |

### 3.3 4H zone noise rejection — exclude if ANY applies
Zone wider than 0.40 DXY · MoM with 3X+ hard mitigations in an opposing trend · older than 3
weeks with no recent interaction · does not overlap any IP zone within 0.50 DXY AND is not a BoM
with 0X–1X mitigation.

---

## 4 · THE STRUCTURAL SCANS (Pillar 5) — WHERE THE LIQUIDITY ACTUALLY IS

### 4.1 Step 0 — 90-day structural extreme scan (runs FIRST)
Swing lows/highs with **rejection wicks**:
- Swing **low** = lower wick ≥ **0.15 DXY pts** AND close in the **upper 50%** of the daily range
  → tag **"Liquidity Sweep Target"**.
- Swing **high** = upper wick ≥ 0.15 pts AND close in the **lower 50%** → tag **"Supply Ceiling
  Target"**.

**The exact price of a prior swing extreme is the primary sweep target — not a range, not an
estimate — the EXACT price.** (180-day conditional extension if the current range overlaps a
90–180-day-old range; those get a LEGACY BONUS +0.5.)

Order blocks (0d): D1 demand = base of 1–3 large bullish candles preceding a rally ≥1.0 pt over
≥5 days; supply = mirror. ≥2.0 pts over ≥10 days = **"High-Conviction Order Block."**

Cross-reference (0e): a sweep target *inside* an order block = **"Confluent Floor" / "Confluent
Ceiling"** — the highest structural confidence tier (Structural score 2 + Extreme Bonus +2).

### 4.2 Step 0.45 / 0.45a — Liquidity Sweep Zones (the green boxes)
- From each swing **low**: LSZ = `[exact low, exact low + 0.05]` (extends *above* the low).
- From each swing **high**: LSZ = `[exact high − 0.05, exact high]` (extends *below* the high).
- **0.45a extension:** institutions sweep **0.05–0.10 beyond** the visible extreme, so extend
  the scan 0.05–0.10 further before assuming the level is defended.
- LSZ serves three functions: **SL placement** (the nearest LSZ above a short / below a long is
  the structurally correct stop), **TP target**, and **direction confirmation**.
- A LSZ overlapping a 4H BoM = **"CONFLUENT LIQUIDITY SWEEP + BoM ZONE"** = the HIGHEST priority
  zone for trade construction.
- A LSZ within 0.30 DXY of spot = flagged **"ACTIVE SL TRIGGER."**
- **CRITICAL:** every trade setup MUST reference at least one LSZ for its stop placement.

### 4.3 Step 0.5 — Repeated Extreme Magnets
A price level reached on **multiple separate dates** becomes a magnet (institutions know stops
clustered there). Compare lows to lows and highs to highs within **0.05**; **also** check a low
coinciding with a prior high — a **"Role Reversal Magnet"**.
| Occurrences | Confidence | Extreme Bonus |
|---|---|---|
| 2 separate dates | HIGH | +1.5 |
| 3+ separate dates | VERY HIGH | +2.0 |
| Role Reversal | **EXTREME** | +2.0 (regardless of count) |
A magnet inside an HTF order block = **"Institutional Magnet"** — maximum Structural score.

### 4.4 Step 0.6 — Intra-zone key levels (precision inside the wall)
For every zone MODERATE or above, scan its interior for 1H S/D zones, the zone's own 0.382/0.618
Fibs, prior daily closes inside the range, and round numbers (.00/.25/.50/.75).
Classify by position: bottom 40% = **Precision Floor**, top 40% = **Precision Ceiling**, middle
20% = **Mid-Anchor**. (Score 0.5 — half a full structural level, but they are what makes an
entry precise.)

### 4.5 Step 5.5 — Zone Core vs Zone Spike
- **Core** = the range of candle **bodies** within the zone — the real institutional defence.
- **Spike** = wicks beyond the core — brief excursions; these are **LSZ targets**, not defence.
Core gets full structural score; spike gets half and is tagged "LSZ extension."

---

## 5 · CONFLUENCE SCORING → PRESSURE DEGREE → **ZFP**

### 5.1 The score (0–14)
Six dimensions × **0–2 points** each (max 12) **plus a Structural Extreme Bonus up to +2**.

| Dimension | 2 pts | 1 pt | 0 pts |
|---|---|---|---|
| Technical | exact match (≤3 pips) | zone match (≤10 pips) | no match |
| Options-Derived | Critical Option Wall ≥$1.5B / Pillar-8 high-conf | Significant Magnet $850M–$1.499B / Pillar-8 moderate | no positioning |
| Analyst Consensus | 2+ Tier-1 sources agree | 1 source | none |
| Structural | exact price anchor + structural extreme | proximity to anchor/extreme | no structural event |
| Psychological | major big figure (.00/.50) | quarter figure (.25/.75) | none |
| Regime/Dynamic | zone in consolidation, will hold | in momentum, may hold or fail | in breakout, likely to fail |

**Structural Extreme Bonus (max +2):** sweep/ceiling target +1.0 · magnet (2 dates) +1.5 ·
magnet (3+) or role reversal +2.0 · confluent floor/ceiling +2.0 · institutional magnet +2.0.

### 5.2 Pressure degree & failure probability
| Score | Pressure Degree | Failure Probability |
|---|---|---|
| 12–14 | **EXTREME** | <10% |
| 10–11 | **HEAVY** | 10–25% |
| 8–9 | MODERATE-HEAVY | 20–35% |
| 6–7 | MODERATE | 30–45% |
| 4–5 | LIGHT | 40–60% |
| 0–3 | MINIMAL | >60% |

### 5.3 ★ ZFP — THE TWO QUANTITIES THAT MUST NOT BE CONFUSED (THE CRUX)

There are **two different "failure" numbers** in the canon. They are correlated at the extremes
(which is why the confusion hides) but they are **different quantities**.

**(a) The geometric ZFP — the one the indicator uses and E2 consumes** (§10.8, verbatim Pine):
```pine
calcZFP(float tp, float bt, string pair) =>
    float zoneW = tp - bt
    float refRange = pair == "DXY" ? 1.60 : pair == "EUR/USD" ? 0.0200 : pair == "GBP/USD" ? 0.0200 : 0.0150
    int pct = math.round(zoneW / refRange * 100.0)
```
| Pair | Reference range | Rationale |
|---|---|---|
| DXY | 1.60 pts | typical DXY weekly range |
| EUR/USD | 0.0200 (200 pips) | typical EU weekly range |
| GBP/USD | 0.0200 (200 pips) | typical GU weekly range |
| AUD/USD | 0.0150 (150 pips) | narrower — commodity currency |

**Reading:** zone **height as a fraction of a typical weekly range**. **NARROW zone → LOW ZFP →
HARD WALL.** A tight, precisely-defended level is a fortress. A tall, diffuse band is not
defended at a single price → likely to fail. Physical, not statistical.

**(b) The fundamental failure probability** (Appendix B) — derived from zone *type*:
| Zone Type | Criteria | Base failure prob |
|---|---|---|
| Hard Wall | CRITICAL OPTION WALL ≥$1.5B + 3+ pillars + confluent F/C | 5–15% |
| Standard Wall | SIGNIFICANT MAGNET $850M–$1.499B + 2+ pillars | 15–30% |
| Soft Wall | no option wall, or 1–2 pillars | 30–50% |
| One-Touch | 1 pillar, no option wall | 50–70% |
| Post-Expiry Ghost | option expired, structural memory remains | 20–40% |
| LSZ | prior exact swing low | special: brief breach then reversal |

Modifiers: Spring Release expiry timing **+20–30%** · macro catalyst against the zone **+15–25%**
· momentum increasing toward the zone **+10–20%** · cross-pair confirmation **+15–25%** · cascade
(prior zone broke) **+20–30%** · regime change (EMA200 cross) **+15–25%**.

Both agree at the extremes: **<20% = hard wall**, **>45% = failing**. That agreement is why a
substitution of one for the other *looks* fine on most zones and **catastrophically inverts the
extremes** — exactly the live defect (see §7).

---

## 6 · ZONE ASSEMBLY (the output of E1)

1. Collect all levels from all 9 pillars. Sort high→low. **DO NOT filter by spot proximity.**
2. Score each across 6 dimensions + extreme bonus (max 14).
3. **Mandatory clustering scan:** 3+ levels within a 0.15 band = **HIGH-DENSITY ZONE**; a pair
   within 0.10 = **TIGHT CONFLUENCE**.
4. Group into zones where levels cluster within 0.10–0.15.
5. Assign pressure degree from the group's **highest-scoring level**.
6. Assign ZFP + Measured Move projection for ZFP > 45%.
7. Name each zone: RESISTANCE CEILING · UPPER RESISTANCE · EQUILIBRIUM ZONE · MID-RANGE
   SUPPORT · KEY SUPPORT BAND · LIQUIDITY SWEEP ZONE · BREAKOUT EXTENSION TARGET.
8. Flag any zone with ZFP > 50% as **BREAKOUT RISK**.
9. **Post-consolidation modifier:** +1 confluence for zones formed AFTER a period of
   consolidation (on 4H) — zones formed after consolidation are usually **stronger** than zones
   formed at the peak of a sweep. Tag "POST-CONSOLIDATION ZONE."

**9.5 Gap scan:** gaps ≥0.20 DXY between adjacent zones; if 2+ supporting signals exist, flag
**"GAP IN-FILL LEVEL."**

**9.7 POI tier overlay (the tier that decides whether you trade it):**
| Tier | Condition | Action |
|---|---|---|
| **Tier 1 — Confluent POI** | IP zone **OVERLAPS** a 4H BoM S/D (0X–1X) | Primary trade location. **+2 confluence.** |
| Tier 2 — IP-Only POI | IP zone, no overlapping 4H BoM | Secondary. +1. |
| Tier 3 — 4H-Only Level | 4H BoM, no overlapping IP zone | Informational only. No primary trades. |

**9.8 Re-verification (mandatory):** re-check every zone's option-strike citation against the
≥$850M threshold and R1-qualified pairs; recompute any contaminated pressure score; verify
Section-3 synthesis zones match Section-2 zone map exactly. Emit the count line.

**Density rule:** no summary table >15 rows (the full IP Zone Map and pivot tables are exempt).

---

## 7 · ★ THE LIVE DEFECT (understood from first principles — for Phase B, not now)

Measured on the current tree (`ENGINE1_V8_VS_MINE.md`, 2026-10-07):

| Field | v8 authority | live build | verdict |
|---|---|---|---|
| **`calcZFP`** | `(tp−bt)/ref × 100` — geometric | `zfp_from_degree(conf)` — confluence band | ❌ **WRONG QUANTITY** |
| `zDeg` | reaches HEAVY (extremes) | caps at **5.0/14** (options=0, analyst=0, regime=0) | ❌ never HEAVY |
| `zTir` | literal T1/T2 | different band | ⚠️ |
| LSZ (6 green boxes) | present | absent (authorized removal) | ⚠️ |
| option strikes (7 amber lines) | present | absent (no harvest) | ⚠️ |
| 2×17 info table (chain + days + zones + trades) | present | absent | ❌ |

**The mechanism of harm.** v8's Ceiling: width 0.07 → ZFP **4%** → §6.4.1 says
`BS + target ZFP < 20 → RWL` = **REVERSAL**. The live build: Ceiling reads LIGHT → 50% →
`is_breakout_risk` → **BS** = **CONTINUATION**. **The wrong ZFP inverts E2's terminal shape.**
A wrong number in E1 does not stay in E1 — it silently flips the E2 chain, and therefore every E3
setup downstream. This is the single most important defect in the project.

---

---

## SOURCE ANCHORS

Every anchor below was verified by printing the referenced line (never fabricated).

- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:566` — §2.0.3 elemental density (Earth = liquidity/IP)
- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:1145` — BoM/MoM Zone Classification
- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:1154` — Zone Reaction Counter
- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:1223` — Step 0 rejection-wick criteria (0.15 DXY on D1)
- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:1509` — Step 9.7 4H zone overlay — the POI tier table
- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:3860` — §10.8 ZFP Calculation (the geometric definition)
- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:3865` — the refRange line: DXY 1.60 / EU 0.0200 / GU 0.0200 / AU 0.0150
- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:4052` — Appendix B — the SECOND failure-probability quantity
- `ENGINE1_V8_VS_MINE.md:21` — the v8-vs-live table row for calcZFP
