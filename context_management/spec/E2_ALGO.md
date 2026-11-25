# E2_ALGO — Engine 2 (Macro Shape Chain) implementable digest

Extraction only. Nothing here is invented: every rule carries a citation; where the sources are silent the text says **UNKNOWN**, where they disagree it says **CONFLICT** and quotes both sides. Sections marked **DERIVED ASSEMBLY** only re-order cited canon rules into a procedure and add no thresholds. Sections marked **OBSERVED** are my own readings of chart images and are approximate.

## 0. Sources and citation keys

| Key | Source | Citation unit |
|:---|:---|:---|
| SP | `/home/user/plutus-vision/canon/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md` (Part VI = lines 1725-2057, Part II = lines 468-737; a few cross-referenced lines outside those ranges are cited where Part VI points at them) | file line |
| FA | `/home/user/plutus-vision/canon/Toolset/Trident_Fractal_Architecture_FirstPrinciples_v2.3.md` (721 lines, read in full) | file line |
| SPEC | `/home/user/handover-branch/Original_Canon_Data/Build Data/Engine2_Spec.pdf` ("Leviathan Engine 2: Macro Shape Chain Map Specification", Version 1.1, May 2026, 17 pages) | line of `pdftotext -layout` output |
| LTE | `/home/user/handover-branch/Original_Canon_Data/Build Data/LTE_Engine_2_Shape_Mapping.pdf` (same document, Version 1.0) | — |
| FB | `/home/user/handover-branch/Original_Canon_Data/Build Data/Leviathan_Engine2_Engine3_Operator_Feedback.pdf` (dated 2026-05-26, 11 pages) | line of `pdftotext -layout` output |
| MSL | `/home/user/inputs/trades/WINNING_TRADE_LIBARARY/Original_Training_Data/Macro Shape Library.pdf` (26 pages, mostly annotated chart screenshots; all 26 pages viewed as images) | PDF page |

LTE vs SPEC: a word-level diff shows the only differences are (a) version 1.0 vs 1.1, (b) SPEC adds the "Report Instrument Scope: DXY | AUD/USD (AU) | GBP/USD (GU) | EUR/USD (EU)" line and section 1.1 "Instrument Scope" (SPEC:19, 40-55), (c) the roadmap section 12.1 wording (LTE lists "(EUR/USD, USD/JPY)" / "multiple component" pairs where SPEC lists the three traded pairs, SPEC:823-830). All shape, matrix, transition, anchoring and procedure text is identical, so SPEC citations cover LTE.

Scope note: canon E2 is written for DXY ("Four base macro shapes describe all DXY price action", SP:1743). SP:119 separately requires "Macro shape chain must be generated PER PAIR, not just DXY. Each pair has its own 4H storyline." and SP:101 "DXY provides DIRECTIONAL CONVICTION only." See CONFLICT C-12.

---

## 1. Shapes

### 1.0 Global framing

- Timeframes: "PRIMARY ANALYSIS TIMEFRAME: 1H" (SP:1729). "1H (PRIMARY): Shape classification, chain construction, day-by-day mapping / 4H (STRUCTURAL): Validates SS range boundaries and BS direction — never primary / 30m (SUPPLEMENTARY): Intra-session detail only — never used for shape classification / D1 (MACRO): Regime context only — weekly trend direction" (SP:1734-1737). Report must state "Primary Timeframe: 1H | Structural Validation: 4H" (SP:1739).
- "Four base macro shapes describe all DXY price action on the Higher Timeframe (HTF: 4H/D1/W1). Every trading session exhibits one of these shapes or a variant thereof. Shapes are mechanically defined by the relationship between price action and IP zone architecture." (SP:1743). CONFLICT C-1: this says HTF = 4H/D1/W1 while SP:1729-1731 says shape classification MUST be on 1H.
- "The distinction between shapes is determined by how price interacts with the IP zones mapped by Engine 1, not by visual pattern recognition alone." (SPEC:82-83)
- Full shape code list found in the sources: **SS, SS (Double Whiplash) / SS(DWL), BS, PBS, R, RS, WL, RWL, PWL, PRWL, WLS, Minor WLS**. Also used in MSL only: "Reverse Breakout Surge", "Reverse Whiplash Storm", "Strong Whiplash Storm", "Strong Breakout Surge", "Major Whiplash Storm", "Recovery Surge" (MSL p1, p3).
- Naming CONFLICT C-2: Part II lists the Water shapes as "Breakout Surge, Whiplash, Recovery, Whiplash Sequence, Pullback Sequence, Swing Scalp" (SP:614; same in FA:127), while Part VI uses "Whiplash Storm (WLS)" (SP:1765) and "Piercing Breakout Surge (PBS)" (SP:1753); SP:2079 expands SS as "SS (Sideways Squeeze)" while SP:1745 says "Swing Scalps (SS)". MSL uses "Whiplash Storm" and "Piercing Breakout Surge" throughout.

### 1.1 Per-shape definition table (canon text)

| Shape | Canon definition | IP-zone signature | Duration | Implies / next |
|:---|:---|:---|:---|:---|
| **SS** Swing Scalps | "Price oscillates within a defined range bounded by IP zones above (resistance ceiling) and below (support floor), forming a series of swing highs and swing lows that respect these boundaries. Each swing typically spans 1-3 trading sessions." (SP:1746). "the upper bound is a Heavy or Extreme pressure resistance zone, and the lower bound is a Heavy or Extreme pressure support zone." (SPEC:89-91) | "Both ceiling and floor IP zones have ZFP below 30%. Option expiry positioning cages price between large strikes." (SP:1747). "Both bounding zones: ZFP < 30%, Confluence ≥ 6" (SP:1879). "The regime classification for both boundary zones is \"Consolidation\" or \"Momentum\" (but not \"Breakout\")." (SPEC:94-95) | "duration > 1 session" (SP:1780); "2-5 sessions" (SP:1935); "Swing Scalps lasting more than one full trading session without a breakout attempt are classified as SS." (SPEC:99-100) | "If both boundary zones hold, SS continues. If one zone ZFP > 45%, prepare for BS transition." (SPEC:441-443). In SS regime "the maximum expected move is to the edge of the nearest opposing zone, NOT through it." (FB:125-126) |
| **SS (Double Whiplash)** | "Two rapid whiplash moves in succession within the range. Labeled \"SS (Double Whiplash)\" — indicates heightened volatility often preceding a breakout attempt." (SP:1748) | same as SS | UNKNOWN | "often preceding a breakout attempt" (SP:1748); "should be flagged ... to signal increased breakout probability" (FB:471-473) |
| **BS** Breakout Surge | "Price breaks decisively through an IP zone, then surges directionally toward the next IP zone or Structural Extreme Magnet. Breakout confirmed by sustained move beyond the zone (15+ minutes)." (SP:1751). "that previously acted as a ceiling (for upside BS) or floor (for downside BS) ... not merely a wick or brief spike." (SPEC:110-113) | "The failing zone has ZFP above 45%, with active breakout pre-conditions." (SP:1752). Pre-conditions: "option expiry timing (Spring Release), macro catalyst alignment, increasing momentum, and/or cascade effect from a prior zone failure." (SPEC:115-116). Target: "always anchored to the nearest Structural Extreme Magnet (Repeated High Magnet, Confluent Ceiling, etc.)" (SPEC:117-118) | "1-3 sessions" (SP:1936-1937). "The initial breakout candle is explosive; the second leg (if present) is often even stronger ... The Breakout Surge ends when price reaches the target IP zone or Structural Extreme Magnet and begins to react." (SPEC:120-122) | Next shape decided by TARGET zone ZFP (section 2.3) |
| **PBS** Piercing Breakout Surge | "A BS so powerful it pierces directly through one or more intermediate IP zones without pausing. Occurs when failing zone ZFP above 70%." (SP:1753) | "All intermediate zones: ZFP > 50%. Target: deep Structural Extreme" (SP:1884). "PBS occurs when the failing zone has ZFP > 60% and the Measured Move points to a distant, verified Structural Extreme. Each intermediate zone it pierces adds momentum (cascade effect)." (SPEC:486-490) | "1-2 sessions" (SP:1938) | "almost always produces a Reverse Whiplash or Whiplash Storm at its termination point." (SPEC:127-128) |
| **R** Recovery | "Temporary stabilization or mild retracement immediately after a BS or Whiplash. Price consolidates or slowly drifts back toward the prior IP zone level. Recovery is always a TRANSITIONAL shape." (SP:1756). "but does not fully reverse the preceding move." (SPEC:133-134) | "Recovery zone: ZFP 20-40%, typically Post-Expiry Ghost" (SP:1881); "mid-range IP zone (Moderate to Moderate-Heavy pressure)" (SPEC:137-138); "Not a Hard Wall." (SPEC:461) | "< 1 session" (SP:1778, 1942); "Half-session to one full session ... if stabilization persists for more than one full session, it is reclassified as Swing Scalps." (SPEC:143-144) | "If the next zone in the direction of the prior BS has ZFP < 30%, expect R --> WL/RWL. If the zone has ZFP > 45%, expect R --> BS (second leg)." (SPEC:455-463) |
| **RS** Recovery Surge | "Instead of slow consolidation, Recovery takes the form of a sharp directional move back toward pre-breakout level." (SP:1757) | Entry "Opposing zone with momentum", target "Prior extreme", ZFP "Variable" (SP:1943) | "< 1 session" (SP:1943) | "signals that the prior directional move may have been a false breakout, increasing the probability of a Reverse Whiplash as the next shape." (SPEC:150-152) |
| **WL** Whiplash | "A rapid, violent directional move that immediately reverses — spike-and-reject pattern. Key characteristic is the rejection at the IP zone, not the initial surge." (SP:1760). "price surges toward an IP zone, briefly pierces it (triggering stops), then is violently rejected back in the opposite direction." (SPEC:157-158) | "Rejection zone: ZFP < 20%, Confluence ≥ 8, LSZ" (SP:1882). "Hard Walls or Standard Walls with ZFP below 20% ... the brief pierce is a liquidity sweep" (SPEC:161-163). "Whiplash is guaranteed at Hard Walls with ZFP < 15%. The Liquidity Sweep Zone designation from Engine 1 is the primary flag." (SPEC:465-470) | "< 1 session" (SP:1939) | Target "Origin zone (return)" (SP:1939). Next: RWL or SS (section 2.2/2.3) |
| **RWL** Reverse Whiplash | "A Whiplash in the opposite direction of the preceding BS. Most common follow-on shape after BS." (SP:1761). "After an upside BS, a RWL is a violent downside rejection. After a downside BS, a RWL is a violent upside rejection." (SPEC:168-169) | Entry "Hard Wall or Institutional Magnet", target "Prior origin", "Rejection zone < 15%" (SP:1940). Matrix: "violent reversal in opposite direction through prior origin; Hard Wall rejection" (SP:1781) | "< 1 session" (SP:1940) | "When the RWL is particularly strong (rejecting back through the prior BS origin), it signals that the BS was a false breakout and the dominant trend has reversed." (SPEC:170-171) |
| **PWL** Piercing Whiplash | "Initial surge so powerful it pierces through multiple IP zones before rejection." (SP:1762) | "The rejection point is typically a Deep Hard Wall or Institutional Magnet" (SPEC:174-175) | UNKNOWN | "indicating extreme volatility" (SPEC:175-176) |
| **PRWL** Piercing Reverse Whiplash | "Reverse Whiplash with piercing characteristics. Strongest reversal signal in the taxonomy." (SP:1763). "the rejection is so violent it pierces back through the BS origin and continues into prior structural levels." (SPEC:179-180) | "Rejection at deep Institutional Magnet or Confluent Floor/Ceiling" (SP:1885); key ZFP "< 10%" (SPEC:810-813) | UNKNOWN | "almost always leads to a new SS phase at a lower (or higher) range, or directly to a Whiplash Storm." (SPEC:180-181) |
| **WLS** Whiplash Storm | "Extended sequence of rapid, explosive Whiplash moves across multiple sessions. On 4H timeframe, WLS appears as Swing Scalps with dramatically increased volatility." (SP:1766). "On every timeframe below 4H, the price action manifests as violent, successive whiplashes in both directions." (SPEC:186-189) | "3+ IP zones within 0.30-0.50 DXY, each ZFP 15-40%" (SP:1883) | "Typically 2-5 sessions. Almost always resolves into a Breakout Surge." (SP:1768) | "The zone most likely to fail is the one with highest ZFP + most breakout pre-conditions active." (SPEC:476-482) |
| **Minor WLS** | "A shorter-duration WLS (1-2 sessions) with less extreme volatility. Minor WLS often appears as a transitional shape between BS and SS, effectively serving as a volatile Recovery phase." (SPEC:202-204) | as WLS | "1-2 sessions" (SP:1779) | → SS (MSL p26 "Minor Whiplash Storm → Swing Scalps") |

### 1.2 OHLC-observable reading of each shape (only what the canon text itself makes observable)

Inputs assumed: E1 zones with `top`, `bot`, `ZFP`, pressure degree, confluence, and wall/LSZ/magnet tags; 1H bars (primary), 4H bars (validation), and bars of 15 minutes or finer for the 15-minute confirmation.

| Shape | Observable test from canon wording | What canon does NOT quantify (UNKNOWN) |
|:---|:---|:---|
| SS | Highs and lows stay between a ceiling zone and a floor zone, both ZFP < 30%, for more than one session (SP:1780); 4H validates the range boundaries (SP:1735) | Minimum number of swings; how far inside the zones a touch must reach; definition of "breakout attempt" |
| SS (Double Whiplash) | Two WL-type spike-and-reject moves in succession inside the SS range (SP:1748) | Time window for "in succession"; minimum spike size |
| BS | Price beyond a zone whose ZFP > 45% and it stays beyond for 15+ minutes; a wick or brief spike does not count (SP:1751, SPEC:112-113, FB:286-287); then travel toward the next zone / Structural Extreme Magnet (SP:1751) | "Sustained" beyond which edge (far edge vs any part of zone); minimum travel; Measured Move formula (see U-3) |
| PBS | BS that passes through ≥1 intermediate IP zone "without pausing" (SP:1753); matrix wording "pierces multiple zones" (SP:1776) | "Without pausing" in bars; CONFLICT C-4 on one vs multiple zones and on the 70/60/50% thresholds |
| R | After a BS or WL, price consolidates or drifts back toward the prior zone, at a zone of ZFP 20-40%, for less than one session, without fully reversing the prior move (SP:1756, 1778; SPEC:133-134) | Maximum retracement fraction for "mild"; range width |
| RS | After BS/WL a sharp directional move back toward the pre-breakout level (SP:1757) | Threshold separating RS from RWL |
| WL | Surge to a zone with ZFP < 20%, brief pierce of the zone, then rejection back toward the origin zone; LSZ present (SP:1777, 1939) | "Briefly" in bars; pierce depth. E1 LSZ geometry gives a sweep band: LSZ "extends 0.05 ABOVE the exact low" / "0.05 BELOW the exact high" (SP:1257, 1261), extended scan "0.05-0.10 DXY" (SP:1286) |
| RWL | After a BS, violent reversal in the opposite direction through the BS origin, rejection at a Hard Wall (SP:1781) | "Violent" in bars or size |
| PWL / PRWL | WL / RWL that pierces multiple IP zones before rejection / pierces back through the BS origin into prior structure (SP:1762-1763; SPEC:179-180) | counts, sizes |
| WLS | ≥3 IP zones inside a 0.30-0.50 DXY band, price oscillating violently between them, 4H shows consolidation (SP:1779); "Minor" if 1-2 sessions | "Violently" not quantified; the 0.30-0.50 band is given in DXY points only, no pair equivalent (U-9) |

"Session" as a duration unit is not defined in the E2 text (U-1).

### 1.3 OBSERVED — dimensions read off the Macro Shape Library DXY examples (approximate, my reading of 220-dpi renders; chart clock is UTC+4)

These are illustrations the operator boxed and labelled by hand. They are not canon thresholds.

| MSL page | Chart | Box label | Approx. duration | Approx. price path |
|:---|:---|:---|:---|:---|
| p7 top (= p22 bottom) | DXY 30m | WL | ~5 bars (~2.5 h) | ~98.55 → high ~98.87 (about +0.30), one dominant candle |
| | | RWL | ~2 bars (~1 h) | ~98.83 → low ~98.67, close ~98.75 (partial retrace only) |
| | | SWING SCALPS | ~24 bars (~12 h) | range ~98.73-98.91 (~0.18) |
| | | BREAKOUT SURGE | ~9 bars (~4.5 h) | ~98.86 → ~98.56 (about -0.30), down through the SS floor and through a "1H (Unmitigated) \| MoM" zone |
| p7 bottom (= p23 top) | DXY 1h | WHIPLASH | ~8 bars | ~98.25 → ~97.75 (about -0.50), one 1H candle ~98.10 → ~97.76 |
| | | REVERSE WHIPLASH | ~9 bars | ~97.70 → ~98.27 (about +0.55; full retrace of the WL) |
| | | SWING SCALPS | ~30 bars | range ~98.02-98.40 (~0.38) |
| | | BREAKOUT SURGE | ~15 bars | ~98.08 → ~98.57 (about +0.47), above the SS ceiling |
| p8 top (= p24 top) | DXY 15m | WHIPLASH STORM | ~7 h | range ~98.15-98.57 (~0.42), several full-range swings |
| | | SWING SCALPS | ~12 h | range ~98.22-98.44 (~0.22) |
| | | BREAKOUT SURGE | ~26 h | ~98.30 → ~98.80 (about +0.50), stair-stepping zone to zone |
| p8 bottom (= p23 bottom) | DXY 15m | WHIPLASH | ~8.5 h | ~98.25 → ~97.67 (about -0.58) |
| | | REVERSE WHIPLASH | ~12 h | ~97.67 → ~98.37 (about +0.70; exceeds the WL origin) |
| | | SWING SCALPS | ~1.5 trading days | range ~98.02-98.40 |
| | | WHIPLASH STORM | ~10 h | range ~98.13-98.55 (~0.42) |
| p14 bottom | DXY 4h | PIERCING BREAKOUT SURGE | ~8 bars | ~98.30 → high ~98.93 (about +0.63) |
| | | WHIPLASH | ~8 bars | ~98.85 → ~98.28, includes one 4H candle whose top is above the visible axis (>99.25) |
| | | REVERSE WHIPLASH | ~7 bars | ~98.25 → ~98.77 (about +0.52) |
| | | SWING SCALPS | ~5 bars | range ~98.57-98.78 (~0.21) |
| | | BREAKOUT SURGE | ~3 bars | ~98.67 → ~98.97, high ~99.05 |
| p21 top | DXY 1h (title says "Piercing Breakout Surge → Recovery/Swing Scalps → Whiplash → Reverse Whiplash"; box says BREAKOUT SURGE) | BREAKOUT SURGE | ~29 bars | ~99.03 → ~97.98 (about -1.05), through two "1H (Unmitigated) \| MoM" zones |
| | | RECOVERY | ~21 bars | range ~98.05-98.27, drifting up |
| | | SWING SCALPS | ~42 bars | range ~97.90-98.28 (~0.38), dips into "4H Liquidity" |
| | | WHIPLASH | ~9 bars | ~98.27 → ~97.70, then sharp reversal toward ~98.20 |

Pair examples with legible numbers: MSL p12 top (EURUSD 30m, Dec 2025): SWING SCALPS box about 2.5 days, range ~1.1614-1.1667 (~53 pips); BREAKOUT SURGE about 22 h, ~1.1660 → ~1.1760 (~100 pips) with one mid-move higher low. MSL p11 top (EURUSD 30m, Dec 2025): SWING SCALPS about 3 trading days, range ~1.1700-1.1758 (~58 pips); "4H Breakout Surge" about +83 pips into a "4H Supply Zone (1x Mitigated) | Start of Trend (Storng Surge - Guaranteed Whiplash Reaction)" [sic], followed by "Minor Whiplash Storm" then "Swing Scalps (Double Whiplash Pattern)" containing two boxes each labelled "Double Whiplash".

Observation relevant to duration units: the library boxes R at ~21 one-hour bars and SS at 12-42 hours, i.e. durations in the examples are fractions of a day up to about two days, shorter than "2-5 sessions" if a session were a full trading day (see U-1).

Legible operator annotations on the library charts (verbatim):
- MSL p12 top: "Higher Low + Break of Structure = INCOMING BREAKOUT SURGE! ENTER INSTINCTUALLY!"
- MSL p12 top: "Weak Reaction to 4H Zone + 2nd Higher Low = 2ND LEG OF BREAKOUT SURGE! THIS ZONE IS GETTING PIERCED"
- MSL p15 bottom: "4H BoM Zone pierced = ALL 4H liquidity near the fallen zone will be swept. Bottom can be predicted this way even if no demand present. War pillaging. ZoC falls = pillage surrounding liquidity."

### 1.4 Other shape-level laws (Part II and Fractal Architecture)

- Conservation / recovery law: "After 2 strong piercing swing moves, expect 1-2 full days of HTF consolidation. Sprints cannot be sustained indefinitely. Liquidity must be absorbed before it can surge again. The chain is WL → RWL → Swing Scalps → BS/WLS/PBS. There MUST be a recovery after high-intensity output. Do not expect whiplash storms on HTFs right after a strong piercing move." (SP:486; FA:576-588)
- "Sequential liquidity sweep: Price ALWAYS sweeps liquidity zone by zone in sequential order. It NEVER skips a zone." (SP:493)
- Reaction counter: "Trend-aligned zones that cause a strong reaction will almost always have THREE strong reactions before the zone fails and gets pierced. 0 reactions = virgin (strongest if BoM), 1-2 = active (still has juice), 3+ = depleted" (SP:495). "If a pressure zone with juice exists between current PA and the BoM zone, price will liquidate that zone first." (SP:495)
- BoM vs MoM: "BoM zones are 100% GUARANTEED to react when touched if unmitigated ... MoM zones tend to get PIERCED" (SP:491).
- "4H BoM Cascade: \"BoM Unmitigated 4H liquidity will usually pierce through everything until it reacts to liquidity of the same element.\" When a move originates from a 4H BoM zone, it will NOT stop at 1H or 30m zones — it will push through to the next 4H zone." (SP:508)
- "A 4H move can pierce through 1H/30m structures but stops at another 4H structure." (SP:661; FA:285)
- Water element: "Swing Scalps within consolidation = Water at its calmest"; "BS/WL after consolidation = Water at its most powerful — tidal wave energy release" (SP:626-627). "Breakout Surges, Whiplashes, Recovery Surges — these are Fire IGNITION events" (SP:609).
- Temporal template: "Earth (liquidity) accumulates Monday-Tuesday during SS. Fire (S/D) ignites Wednesday during BS." (FA:9)
- Pair profiles (SP:675-678; FA:596-648): EUR/USD "HTF consolidation = Swing Scalps. HTF breakout = BS/WL" (FA:600), "primary swing pair"; GBP/USD "Liquidity is the only thing respected (S/D gets pierced)", "primary scalp pair"; AUD/USD "molasses, 2-4 days per move"; DXY "maps master direction, wakes up during NY".

---

## 2. Matrices (verbatim)

### 2.1 SP section 6.2 — Shape Classification Decision Matrix (SP:1770-1781)

"Apply this matrix in SEQUENCE — check the highest-priority condition first. If it matches, assign that shape." (SP:1772)

| Priority | Condition (IP Zone Metrics) | Shape | Confidence |
|:---|:---|:---|:---|
| 1 | Price breaks through zone with ZFP > 45% AND confirms 15+ min; Measured Move target exists | BS (or PBS if pierces multiple zones) | HIGH |
| 2 | Price surges to zone with ZFP < 20%, briefly pierces, then rejects; Liquidity Sweep Target identified | WL (or PWL if multiple zones pierced) | HIGH |
| 3 | After BS/WL: price stabilizes at mid-range zone (ZFP 20-40%); duration < 1 session | R (or RS if sharp retracement) | MODERATE |
| 4 | 3+ IP zones in narrow range (0.30-0.50 DXY); price oscillating violently; 4H shows consolidation | WLS (or Minor WLS if 1-2 sessions) | HIGH |
| 5 | Price oscillating between Heavy/Extreme ceiling and floor zones; both ZFP < 30%; duration > 1 session | SS | HIGH |
| 6 | After BS: violent reversal in opposite direction through prior origin; Hard Wall rejection | RWL (or PRWL if piercing) | MODERATE-HIGH |

SPEC Table 2 and FB section 3.4 are identical except row 6 ends "Hard Wall rejection at origin" (SPEC:239-241; FB:346-348). No fallback row exists for a state matching none of the six (U-2).

Note on numbering: in SP, 6.2 is the classification matrix above; the shape-to-shape transition matrix is SP section 6.4 (next).

### 2.2 SP section 6.4 — Shape Transition Rules (SP:1800-1817)

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

Three further rows exist only in SPEC Table 4 / FB section 3.5 (SPEC:399-403; FB:402-406):

| Current Shape | Next Shape | IP Zone Trigger | Probability |
|:---|:---|:---|:---|
| PBS | R/SS | Piercing move exhausts at distant Structural Extreme | HIGH |
| PBS | PRWL | Piercing move overextends; violent reversal | MODERATE |
| PRWL | SS | Reversal exhausts; new consolidation range established | HIGH |

SPEC wording differences on shared rows: SS→BS "A bounding zone with ZFP > 45% fails with confirmation (15+ min)", probability "HIGH (when ZFP > 60%)" (SPEC:350-352); BS→PBS "MODERATE (at high ZFP)" (SPEC:366-368); BS→R adds "momentum fades" (SPEC:358-360).

### 2.3 SP section 6.4.1 — ZFP-Conditioned Transition Rules (SP:1819-1837)

"**This is the most important Engine 2 correction.** Chain sequencing must be conditioned on the TARGET zone's ZFP, not just the current shape. Without this table, the engine incorrectly predicts R or PBS after a BS hits a Hard Wall, when it should predict RWL." (SP:1821)

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

"**CRITICAL MISTAKE TO AVOID:** When a BS reaches a Hard Wall (ZFP < 20%, confluence ≥ 8), the engine MUST predict RWL, NOT R or PBS. This was the #1 Engine 2 error that caused the April 20-24 misprediction — the engine predicted upside continuation when a Hard Wall sat directly above. The ZFP of the TARGET zone determines the next shape, not the momentum of the current move." (SP:1837)

Gaps in this table (UNKNOWN, U-4): BS with target ZFP in 40-60%; SS with a bounding zone ZFP in 30-45%; "opposing zone near" has no distance; "momentum builds" has no measure.

### 2.4 SP section 6.4.2 — HTF Zone Mechanics Decision Tree (SP:1839-1873, verbatim tree)

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

Branch selection from the E1 reaction counter (SP:1868-1871): "0 reactions (virgin): Most likely MINOR REACTION branch (first test causes reaction but zone holds initially) / 1-2 reactions (active): Could be any branch — assess surrounding liquidity / 3+ reactions (depleted): Most likely PIERCED branch (zone fails)".

"**For BoM zones:** BoM zones are NOT subject to this decision tree — they ALWAYS react (100% guarantee if unmitigated). A BoM zone reaction produces a directional move (BS, WL, or RWL) determined by the Direction Validation 6-check." (SP:1873)

4H MoM One-and-Done (SP:1963): "if 100% unmitigated, there WILL be a reaction on the first retest, but often it is a minor reaction followed by a strong pierce ... the expected shape after touching a 4H MoM is a minor WL followed by BS/PBS through the zone."

### 2.5 Anchoring and quick reference (SP:1875-1885, 1931-1943, verbatim)

| Shape | IP Zone Role | Engine 1 Metrics Required |
|:---|:---|:---|
| SS | Ceiling and Floor zones define the range | Both bounding zones: ZFP < 30%, Confluence ≥ 6 |
| BS | Failing zone triggers BS; target zone determines magnitude | Failing zone: ZFP > 45%. Target: Measured Move |
| R | Mid-range zone provides temporary friction | Recovery zone: ZFP 20-40%, typically Post-Expiry Ghost |
| WL/RWL | Hard Wall or Institutional Magnet rejects the move | Rejection zone: ZFP < 20%, Confluence ≥ 8, LSZ |
| WLS | Cluster of 3+ zones creates oscillation cage | 3+ IP zones within 0.30-0.50 DXY, each ZFP 15-40% |
| PBS | Multiple intermediate zones fail; distant target | All intermediate zones: ZFP > 50%. Target: deep Structural Extreme |
| PRWL | Institutional Magnet at depth of reversal provides rejection anchor | Rejection at deep Institutional Magnet or Confluent Floor/Ceiling |

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

SPEC Table 8 role thresholds (SPEC:768-815): SS Ceiling "< 30%"; SS Floor "< 30%"; BS Trigger Zone "> 45%"; R Stabilization Zone "20-40%"; WL Rejection Zone "< 15%"; WLS Oscillation Cage "15-40% each"; PRWL Rejection Anchor "< 10%".

### 2.6 Chain catalogue

SP section 6.3 (SP:1783-1798), verbatim:

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

Additional chains only in SPEC Table 3 (SPEC:296-336): "4H BS --> Minor WLS --> SS" MODERATE; "PBS --> SS (Minor WLS)" MODERATE; "WLS --> PBS --> PRWL --> SS" LOW-MODERATE; "PBS --> R/SS --> WL --> RWL" LOW-MODERATE; "WLS --> R --> PBS/WL" LOW; "WLS --> R --> SS" LOW. SPEC adds to the first row: "Occurs approximately 2x per week on average (LTF + HTF combined)." (SPEC:260-261) and to WL→RWL→SS→BS: "Often seen at week open when prior week ended at a major IP zone." (SPEC:279-280).

Operator's own lists (MSL p1, verbatim):

Pathway Patterns Noticed:
- Swing scalps --> Breakout Surge
- Breakout Surge --> Recovery/Reverse Whiplash
- Recovery --> Swing Scalps/Whiplash/Reverse Breakout Surge
- Whiplash --> Reverse Whiplash/Reverse Whiplash Storm/Swing Scalps
- Strong Whiplash Storm --> Strong Breakout Surge
- Reverse Whiplash --> Recovery/Whiplash Storm/Swing Scalps

Combinations:
- Swing Scalp --> Breakout Surge --> Recovery --> (Reverse) Whiplash
- Strong Breakout Surge --> Recovery --> Reverse Breakout Surge
- Whiplash --> Reverse Whiplash --> Swing Scalp --> Breakout Surge
- Recovery --> Reverse Whiplash --> Swing Scalp --> Breakout Surge
- Swing Scalp --> Breakout Surge --> Reverse Whiplash --> Piercing Breakout Surge
- Swing Scalp --> Breakout Surge --> Reverse Whiplash --> Recovery --> Piercing Breakout Surge
- Swing Scalp --> Breakout Surge --> Swing Scalp --> Breakout Surge
- 4H Breakout Surge --> Minor Whiplash Storm --> Swing Scalps
- Piercing Breakout Surge --> Swing Scalps (Minor Whiplash Storm)
- Whiplash Storm --> Breakout Surge --> Whiplash Storm

"BREAKOUT SURGE --> RECOVERY --> WHIPLASH REMAINS THE MOST FREQUENTLY OBSERVED PATTERN ON BOTH HTF + LTF (All variations of the shape self contained within this pattern)" (MSL p1). MSL p9 heading: "Swing Scalps → Breakout Surge → Recovery → Whiplash (Original Storyline ~ 2x Weekly Patterns)".

MSL transitions that are absent from SP 6.4: RWL → Recovery, RWL → Whiplash Storm, WL → "Reverse Whiplash Storm", R → "Reverse Breakout Surge" (MSL p1).

Library section headings (all pages): "MASTER SHAPE PATHWAYS" p2-p8: SS→BS→R→WL (MOST FREQUENT PATTERN!); BS→SS/R→WLS; BS→R→PBS; BS→RWL→SS; WL→RWL→SS/Rcvry→BS; WLS→SS→(Piercing) BS; Surge/WL→RWL→SS→WLS. "Backtesting Libraries" p9-p26: SS→BS→R→WL; SS→BS→RWL→R→SS (2x Same Weekly Storyline); SS→BS; SS→BS→SS→BS→R→WL; SS→BS - RWL (Minor Storm); HTF SS→HTF BS→Minor WLS→SS; PBS→WL→RWL→SS→BS; BS→R→(Reverse) WL→SS; BS→R→PBS; BS→SS/R→WLS; BS→1H SS (Double Whiplash, SS, Whiplash Storm, BS); BS→RWL→SS→WLS; BS→RWL→PBS→SS; BS→RWL→SS→WLS→PBS; PBS→R/SS→WL→RWL; PBS→Rcvry/SS→PRWL→SS; WL→RWL; WL→RWL→SS/Rcvry→BS; WL→RWL→SS→WLS; WLS→SS→(Piercing) BS; WLS→PBS→PRWL→SS; WLS→R→PBS/WL; Minor WLS→SS; WLS→R→SS. Instruments shown: EURUSD, GBPUSD, DXY, on 5m/15m/30m/1h/4h.

---

## 3. Forward-mapping walk (SP section 6.6, SP:1887-1917; SPEC section 6, SPEC:504-570)

### 3.1 Canon steps (verbatim)

"The forward mapping procedure is executed after Engine 1 has produced the DXY IP Zone Map for the target week. It takes the IP Zone Map as input and produces a Macro Shape Chain Map as output. The procedure is mechanical, deterministic, and auditable at every step." (SPEC:505-507)

**Step 1: Current Shape Identification.** "Using the IP zone map from Engine 1, identify the current macro shape by applying the Shape Classification Decision Matrix (Section 6.2). Determine which shape best describes the current price-zone relationship. State the current shape, the IP zone anchoring it, and the ZFP of the anchoring zone." (SP:1889)

How the first shape comes from pre-boundary data (SPEC:511-515): "Identify the macro shape that is currently active as of the Friday close (the temporal boundary for the report). This is the starting shape of the chain. Apply the Shape Classification Decision Matrix (Table 2) to the current price position relative to the IP Zone Map. If price is between two Heavy/Extreme zones with low ZFP, the current shape is SS. If price has just broken through a zone with high ZFP, the current shape is BS. If price is at a Hard Wall showing rejection, the current shape is WL or RWL." Dependencies for this step: "IP Zone Map + prior week shape" (SPEC:738-740).

Temporal boundary: "The temporal boundary is the Friday 5:00 PM ET close of the week immediately prior to the target week." (SP:380). "All IP zone data must be pre-week data." (SP:1923). "No in-week price action may be used to adjust the chain map during the target week. Intra-week chain validation is permissible for learning purposes only, not for the published report." (SPEC:701-703). See C-11 for the anchor conflict.

**Step 2: Transition Probability Assessment.** "From the current shape, apply the Shape Transition Rules (Section 6.4) and ZFP-Conditioned Transition Rules (Section 6.4.1) to determine the most probable next shape. Assign confidence based on the transition probability and ZFP conditioning. If the current shape is SS, also assess consolidation phase (Section 6.8 Consolidation Phase Detection)." (SP:1891). SPEC bullets (SPEC:523-533):
- "If a bounding zone has ZFP > 45% with active breakout pre-conditions, the SS --> BS transition probability is HIGH."
- "If the Measured Move target zone is a Hard Wall with ZFP < 20%, the BS --> RWL transition probability is HIGH."
- "If a zone cluster of 3+ zones exists in the current range, the SS --> WLS or WLS continuation probability is HIGH."
- "If the Measured Move target zone has moderate ZFP (20-40%), the BS --> R transition probability is MODERATE-HIGH."

**Step 3: Chain Extension with Audit Trail.** "Extend the shape chain forward, shape by shape, through the trading week. For each extension: document (a) current shape, (b) the IP zone trigger, (c) the transition conditions (ZFP value), (d) predicted next shape, (e) confidence level. Maximum chain length: 5 shapes. Terminate if cumulative confidence drops below 25%. Format: `Shape A → [Trigger: zone name, ZFP X%] → Shape B → [Trigger: ...] → Shape C [confidence: Y%]`" (SP:1893). SPEC stop conditions: "Continue until either (a) the end of the trading week is reached, (b) the chain enters SS with no zone having ZFP > 35% (terminal SS), or (c) the chain prediction confidence drops below MODERATE." (SPEC:539-541)

**Confidence scoring** (SPEC step 4, SPEC:549-557): "The chain confidence is the product of individual transition confidences, adjusted for the historical frequency of the chain. Confidence tiers for individual transitions: HIGH = 0.80, MODERATE-HIGH = 0.65, MODERATE = 0.50, LOW-MODERATE = 0.35, LOW = 0.20. ... If either transition has a confidence below MODERATE, the chain prediction is flagged as [LOW CONFIDENCE - consider alternative chains]." Worked example: "Chain: SS --> BS --> RWL --> SS | Chain Confidence: 0.80 x 0.80 x 0.65 = 41.6% (MODERATE)" (SPEC:680-681). If terminated: remaining week flagged "[DISCOVERY ZONE - insufficient IP zone data for reliable chain extension]" (SPEC:716-719). Numeric value of VERY HIGH and the frequency adjustment are UNKNOWN (U-5).

**Step 4: Alternative Chain Analysis.** "For every primary chain, construct at least one alternative chain that activates if the primary fails at a specific Decision Zone. The Decision Zone is the IP zone whose ZFP determines which chain activates. Document: (a) the Decision Zone, (b) the ZFP threshold that triggers the alternative, (c) the alternative chain, (d) alternative chain confidence. Format: `PRIMARY: A→B→C | DECISION ZONE: [zone] ZFP > [threshold]% → ALTERNATIVE: A→X→Y`" (SP:1895). "The alternative chain shares the same starting shape but diverges at the first transition where an alternative trigger could activate." (SPEC:562-564). Worked example: "The primary chain was BS --> R --> PBS (incorrect). The alternative chain was BS --> RWL --> SS --> WLS (correct). The Decision Zone was 99.43-99.67. If this zone held (ZFP < 30%, Hard Wall), the alternative chain activated. If this zone failed (ZFP > 45%), the primary chain would have activated." (SPEC:566-570)

**Step 5: Session/Day-Level Decomposition.** "Decompose the weekly chain into day-by-day predictions. For each day (Mon-Fri): (a) assign the predicted shape, (b) assign the directional bias (up/down/range), (c) identify the key IP zone for that day, (d) note any volatility triggers (auctions, expiries, economic events), (e) state confidence. Format: `Mon: [SHAPE] [direction] | Key Zone: [name] | Triggers: [list] | Confidence: X%`" (SP:1897)

**Pair translation.** "The SHAPES are the same — only the DIRECTION is inverted. SS remains SS, BS remains BS, WL remains WL. What changes is the direction of each move: DXY up = pair down, DXY down = pair up." (SP:1917). Table (SP:3581-3589): SS Neutral→Neutral; BS up→down; BS down→up; PBS "Up strongly"→"Down strongly"; WL "Up then Down"→"Down then Up"; RWL "Down" (after upside BS)→"Up"; WLS "Neutral/oscillating". "The SPECIFIC PRICE LEVELS for each shape's boundaries come from each pair's own data." (SP:3600)

### 3.2 How each day's shape, direction and zone-to-zone range are chosen — what the canon gives

**Day assignment.** Canon gives no explicit algorithm that maps an N-shape chain onto five days (U-6). The only ingredients are:
- Expected durations per shape (table in 2.5): SS 2-5 sessions, BS 1-3, PBS 1-2, WL/RWL/R/RS < 1, WLS 2-5.
- Trading Speed Rule: "add 1 day to expected timing" (SP:2046), section 4.4.
- Consolidation durations: "Long Consolidation begins (2-4 days)", "Slow Consolidation around POI (2-4 days)" (SP:1852, 1862); "After 2 strong piercing swing moves, expect 1-2 full days of HTF consolidation" (SP:486).
- Proximity rule: "If not right near a strong 4H pressure zone right now — BS is most likely days away. This is swing scalp valley" (SP:1959).
- Catalysts: "Engine 2 should predict R/SS before Red Folder events and potential BS/WL after them" (SP:3247); "RULE 9: No Session Predictions Without Catalyst Identification." (SP:1929)
- Worked templates: Day Bridge table rows "Mon: SS (range)", "Tue: SS (late phase, ZFP rising)", "Wed: BS (breakout)", "Wed: BS → Thu: R", "Thu: R → SS", "Fri: WL/SS→BS", "Fri: R (end of week)" (SP:2106-2113); "If Engine 2 predicts Monday=SS, Tuesday=SS, Wednesday=BS" (SP:17); "DXY: Mon: SS [range] → Tue: BS [up] → Wed: R [consolidation] → Thu: RWL [down] → Fri: SS [range]" (SP:3594); "Earth (liquidity) accumulates Monday-Tuesday during SS. Fire (S/D) ignites Wednesday during BS." (FA:9)

**Direction.** Field values are "up/down/range" (SP:1897); the 9.10 example also uses "[consolidation]" for R (SP:3594).
- SS → range (SP:3583, 3594). WLS → "Neutral/oscillating" (SP:3589).
- BS/PBS → the side of the failing bounding zone: "BS (up) | Resistance zone ZFP > 45%", "BS (down) | Support zone ZFP > 45%" (SP:1936-1937). 4H "Validates ... BS direction" (SP:1735).
- WL → surge toward the rejecting zone, then back: "WL (upward spike then reject down) | Up then Down" (SP:3587).
- RWL → opposite to the preceding BS (SP:1761, 3588).
- WLS → BS direction: "must be justified by identifying the specific bounding zone most likely to fail, including its ZFP, breakout pre-conditions, and the macro catalyst direction." (SPEC:722-725); "the breakout direction is determined by which bounding zone has the highest ZFP + most breakout pre-conditions active." (FB:409-410)
- BoM-zone reaction direction: "determined by the Direction Validation 6-check" (SP:1873).
- When unclear during consolidation, Pressure Reading Rules (SP:1978-1982): "Candle size = pressure direction: Look at which candles are obviously bigger. That is where pressure is building." / "Wick direction = pressure direction: Upper wicks = buying pressure. Lower wicks = selling pressure." / "Triangle shapes: The flat side is receiving pressure. The sharp side is applying pressure." / "4H storyline tiebreaker: When in doubt, the 4H storyline bias decides."
- Structural direction (Part II): "Higher highs and higher lows = bullish bias. Lower highs and lower lows = bearish bias." (SP:476)
- R direction label: UNKNOWN beyond "consolidates or slowly drifts back toward the prior IP zone level" (SP:1756).

**Expected range (zone to zone).**
- SS: ceiling zone to floor zone (SP:1746, 1879); expected move stops at "the edge of the nearest opposing zone, NOT through it" (FB:125-126).
- BS: from the failing zone to "the next IP zone or Structural Extreme Magnet" (SP:1751); "Target is the nearest Structural Extreme Magnet, not a blind projection." (SPEC:448-452); "BS (up) ... Next Resistance or Structural Extreme" (SP:1936). Measured Move is computed only "when ZFP > 45%" and its audit trail must "Show the range height, raw target, and structural extreme anchor" (SP:1457, 398); the formula itself is not in v5.3.3 (U-3).
- PBS: through all intermediate zones with ZFP > 50% to a "Deep Structural Extreme" (SP:1938).
- WL: out to the zone with ZFP < 20% plus a brief pierce, back to the "Origin zone (return)" (SP:1939).
- RWL: from the Hard Wall / Institutional Magnet back to "Prior origin" (SP:1940), "through prior origin" (SP:1781).
- R: at the mid-range zone of ZFP 20-40% (SP:1942), no target.
- WLS: between the 3+ clustered zones inside 0.30-0.50 DXY (SP:1883); exit target "BS resolution target" (SP:1941).
- Path constraints: zone-by-zone sequential sweep, never skipping (SP:493); juice zone before BoM zone (SP:495, 1161); Timeframe Element Matching "4H source → 4H target (1H acceptable ...)", "1H source → 1H target (30m acceptable)", "30m source → 30m target (15m acceptable)", "15m source → 30m or 1H target (up to 2 TF dimensions higher, not more)", "5m source → 15m or 30m target" (SP:1968-1972); "a breakout that originates on 15m liquidity should NOT target a 4H zone" (SP:1974).

**Alternative (ghost) chain.** The word "ghost" is not used for the alternative chain in these sources ("Post-Expiry Ghost" is a zone type, SP:4062). Selection rule: same starting shape, diverge at the first transition where a different trigger could fire, name the Decision Zone and the ZFP threshold (SP:1895; SPEC:562-564). The only worked threshold pair is held "ZFP < 30%, Hard Wall" vs failed "ZFP > 45%" (SPEC:567-569).

### 3.3 DERIVED ASSEMBLY — the walk as a procedure (re-ordering of cited rules; gaps marked)

```
INPUT (all as of the temporal boundary):
  zones[]  : top, bot, pressure degree, confluence 0-14, ZFP %, wall type, LSZ / magnet tags,
             BoM|MoM, source TF, reaction count, measured-move target (if ZFP > 45)
  price    : last price at the boundary
  bars     : pre-boundary 1H (primary), 4H (validation), <=15m (for the 15-min confirmation)
  prior    : prior-week shape                                   (SPEC:738-740)
  calendar : expiries / auctions / red-folder events per day    (non-OHLC; section 7)

STEP 1  current shape S0 = first matching row of matrix 6.2, in priority order 1..6   (SP:1772-1781)
        record anchoring zone and its ZFP                                             (SP:1889)
        4H must confirm or reject the 1H classification                               (SP:1999)
        no row matches -> UNKNOWN (U-2)

STEP 2/3  repeat while (shapes < 5) and (cumulative confidence >= 25%) and (week not ended):
  case S of
    SS : a bounding zone has ZFP > 45            -> BS toward that zone, HIGH          (SP:1829)
         both bounding ZFP < 30                  -> SS continues, HIGH                 (SP:1830)
         3+ zones in narrow range + vol triggers -> WLS, MODERATE                      (SP:1805)
         no zone with ZFP > 35                   -> terminal SS, stop                  (SPEC:540)
         bounding ZFP between 30 and 45          -> UNKNOWN (U-4)
         also classify consolidation phase                                              (SP:1946-1957)
    BS : T = target zone (measured-move target / next zone / structural extreme)
         ZFP(T) < 20                             -> RWL, HIGH                          (SP:1825)
         20 <= ZFP(T) <= 40                      -> R, HIGH                            (SP:1826)
         ZFP(T) > 60                             -> PBS, MODERATE                      (SP:1827)
         ZFP(T) > 80                             -> PBS, HIGH                          (SP:1828)
         40 < ZFP(T) <= 60                       -> UNKNOWN (U-4)
    R  : persists > 1 full session               -> SS, MODERATE-HIGH                  (SP:1832)
         < 1 session and opposing zone near      -> WL or RWL, MODERATE                (SP:1833)
         next zone in prior-BS direction ZFP<30  -> WL/RWL                             (SPEC:455-463)
         next zone in prior-BS direction ZFP>45  -> BS (second leg)                    (SPEC:455-463)
    WL : opposite momentum builds                -> RWL, MODERATE-HIGH                 (SP:1834)
         no opposite momentum                    -> SS, MODERATE                       (SP:1835)
    RWL: reversal exhausts                       -> SS, HIGH                           (SP:1814)
         reversal breaks opposing zone           -> BS (new dir), MODERATE             (SP:1815)
    WLS: a bounding zone fails                   -> BS, VERY HIGH; direction = bounding zone with
                                                    highest ZFP + most pre-conditions  (SP:1831; SPEC:476-482)
         volatility diminishes                   -> SS, MODERATE                       (SP:1817)
    PBS: exhausts at distant structural extreme  -> R/SS, HIGH                         (SPEC:399)
         overextends                             -> PRWL, MODERATE                     (SPEC:401)
    PRWL:                                        -> SS, HIGH                           (SPEC:403)
  overlays applied when the predicted shape reaches a zone:
    MoM zone  -> decision tree 6.4.2, branch by reaction count                         (SP:1843-1871)
    BoM zone  -> always reacts; BS/WL/RWL by Direction Validation                      (SP:1873)
    4H MoM    -> minor WL then BS/PBS through                                          (SP:1963)
    after 2 strong piercing swing moves -> 1-2 full days of consolidation              (SP:486)
  cumulative confidence = product of tier values                                       (SPEC:549-557)
  write audit-trail line for the step                                                  (SP:1893)

STEP 4  alternative chain: same S0, diverge at first transition with a second possible trigger;
        record Decision Zone and ZFP threshold                                         (SP:1895; SPEC:562-564)

STEP 5  map chain onto Mon..Fri: per day shape, direction (up/down/range), key zone, triggers,
        confidence                                                                     (SP:1897)
        chain-to-day mapping rule itself: UNKNOWN (U-6); ingredients in 3.2
        then apply trading speed: raw timing and adjusted (+1 day) timing both reported (SP:2025-2027)
        then translate to pairs: same shapes, inverted direction, pair's own levels    (SP:1917, 3600)
```

### 3.4 Zero-tolerance rules (SP:1919-1929, verbatim)

"RULE 1: No Shape Without IP Zone Anchoring. Every shape prediction must be anchored to at least one specific IP zone." / "RULE 2: No Chain Without Audit Trail. Every chain extension must document current shape, trigger, conditions, prediction, confidence." / "RULE 3: Temporal Boundary Inheritance. All IP zone data must be pre-week data." / "RULE 4: No Behavioral Generalizations. Shape durations and probabilities must be derived from backtested data or specific IP zone metrics." / "RULE 5: Mandatory Alternative Chain. Every primary chain must include at least one alternative chain with a Chain Branch Point." / "RULE 6: No Chain Extension Beyond Moderate Confidence. Terminate chain if cumulative confidence drops below 25%." / "RULE 7: WLS Resolution Direction Must Be Justified with specific bounding zone identification." / "RULE 8: No Fabricated Trade Setups. Every setup must reference specific IP zones with ZFP values." / "RULE 9: No Session Predictions Without Catalyst Identification."

SPEC adds labels: a shape without anchor "is classified as UNANCHORED and may not be included in the primary chain" (SPEC:691-692); a chain without audit trail "is classified as UNVERIFIED" (SPEC:697); a WLS→BS without directional justification "is classified as INCOMPLETE" (SPEC:725).

### 3.5 Consolidation Phase Detection (SP:1946-1959, verbatim)

"For each SS/WLS/R shape identified by Engine 2, classify the **consolidation phase** to determine which setup types are valid:"

| Phase | Condition | Valid Setup Types | Timeframe Stack |
|:---|:---|:---|:---|
| Early consolidation | SS/WLS just started (< 1 session) | Swing Scalps (both directions) | Scalp Stack (30m/15m/5m) |
| Mid consolidation | SS/WLS ongoing (1-3 sessions) | Swing Scalps + Double Whiplash Inverse | Scalp Stack |
| Late consolidation (near HTF zone) | ZFP trending up on bounding zone | Swing Scalps + BS Transition Entry | Both Stacks |
| Post-BS (early breakout) | BS confirmed, move in progress | Reinforcement entries only | Swing Stack |
| Post-BS (recovery) | BS complete, price recovering | Whiplash/Recovery Surge entries | Swing Stack |
| Mid-breakout | Directional move in progress | Reinforcement entries at liquidity zones | Swing Stack |

"**Key rule**: \"If not right near a strong 4H pressure zone right now — BS is most likely days away. This is swing scalp valley — milk the cow on the 15m timeframe.\"" (SP:1959). How "ZFP trending up" is measured: only "moving from 25% toward 40%+" (FB:475).

---

## 4. Day-level decomposition: sessions, timing, conservation of energy, trading speed

### 4.1 Session clock (all times ET)

- "London Session (2:00 AM – 12:00 PM ET)" (SP:698). "NY Session (12:00 PM – 5:00 PM ET)" (SP:707). "Tokyo Session: Milk the cow / sleep. Limited opportunities." (SP:714) — no Tokyo/Asia clock times are given anywhere in the sources (U-7).
- Session windows used for setup labels (SP:13): "London Open 02:00-05:00 ET, London Mid 05:00-08:00 ET, NY Overlap 08:00-10:00 ET, NY Open 08:30-10:00 ET, NY Mid 10:00-14:00 ET, NY Close 14:00-17:00 ET". CONFLICT C-6 with the 12:00 PM NY start above.
- Week close / boundary: "Friday 5:00 PM ET" (SP:380). "Close ALL open trades by NY market close." (SP:87)
- NY Cut: "OTC options expiring daily at 10:00 AM New York time ... Blocks with contract sizes >= USD 1.5 Billion equivalent are classified as Critical Entry Shields ... pinning price within a tight horizontal range." (SP:690). "At exactly 10:01 AM NY ... the market experiences a \"Spring Release\" — violently breaking out or reversing back toward high-timeframe structural anchors. All OTC expiry coordinates become completely invalid at 10:01 AM NY." (SP:691)

### 4.2 Where in the day the move happens

- London: "SCALP ONLY. 95% of NY swings don't even start until the 2nd half of NY session." (SP:699); "DXY moves zone-to-zone during London — breakout doesn't start until ~3:00 PM ET." (SP:701); "Expect London price action to be weak and reactive. Strong moves only come toward end of London once liquidity has been swept and NY is ready." (SP:703); "Catch 10-20 pip swing scalps on the 15m during London" (SP:705); "GU provides 3-4x more London trading opportunities than EU." (SP:702)
- NY: "SWING SESSION. Most setups hit TP during NY session." (SP:708); "95% of NY swings don't start until the 2nd half of NY session (after 2:30 PM ET)." (SP:710); "London entries → NY fireworks." (SP:711); "DXY wakes up during NY session" (FA:646).
- Transition timing: "the NY Cut Spring Release effect (10:00 AM → 10:01 AM) is the primary timing trigger for shape transitions. Transitions cluster around this time because the option cage effect breaks at 10:01 AM." (FB:469-470). The individual scalps inside SS come from the cage: "The option cage effect (NY Cut at 10:00 AM) creates repeated Spring Release bounces that manifest as the individual scalps within the range." (SPEC:96-97)
- Session assignment by shape (Day Bridge, SP:2122-2127): "SS shape → London session (GU/AU scalp focus) / BS/WL shape → NY session (EU/AU swing focus, 95% start 2nd half NY) / R shape → Both sessions possible (recovery is transitional) / SS→BS Transition → London setup, NY activation". Bridge table (SP:2104-2113):

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

- Session-level sub-chains are roadmap only, "NOT part of the current v1.0 specification" (SPEC:820-821): "The Asian session typically manifests SS or Minor WLS; London often triggers BS; NY produces the decisive shape transitions at the 10:01 AM Spring Release." (SPEC:834-836). CONFLICT C-7 with "breakout doesn't start until ~3:00 PM ET".
- Red Folder days (SP:3243-3248): "Pre-event: price tends to consolidate (SS/R) as algorithms reduce exposure / Post-event: price may surge directionally (BS) or whiplash (WL) depending on the data surprise / Engine 2 should predict R/SS before Red Folder events and potential BS/WL after them / The Spring Release Effect (10:01 AM NY) applies to OTC option expiries on Red Folder days — double volatility trigger".

### 4.3 Conservation of energy

- "AFTER 2 STRONG PIERCING SWING MOVES — EXPECT 1-2 FULL DAYS OF HTF CONSOLIDATION. Liquidity must be absorbed before it can surge again. This is a universal mechanic in every form of creation." (FA:576)
- Recovery cycle (FA:580-588): "1. WL = High energy output ... 2. RWL = Partial recovery — Fire attempting to reignite, insufficient Earth (liquidity) fuel 3. Swing Scalps = Full recovery mode — Earth (liquidity) re-accumulating ... 4. BS/WLS/PBS = New energy available".
- "Do not expect whiplash storms on HTFs right after a strong piercing move." (SP:486). CONFLICT C-8 with SPEC:127-128.
- "Fire CANNOT be sustained indefinitely" (SP:606).
- Scale conservation: "a higher-density element can only be contained by a same-density element" (FA:285); "usually never more than 2 dimensions up" (FA:287).

### 4.4 Trading Speed Rule (SP:2040-2054, verbatim)

"**\"Assume price moves at 30-50% of the speed you think it will.\"**"

1. "**Shape chain timing**: \"Today's move\" often ends up being TOMORROW's move. TODAY'S move is the journey TO what you thought \"today's move\" will be. When predicting day-level shape assignments, add 1 day to expected timing."
2. "**4H move duration**: \"The move that I see on the 4H chart — expect it to take twice as long as I think it will.\" A 4H breakout that appears imminent may take 2-3 more 4H candles to complete than initially predicted."
3. "**Reinforcement rocket spacing**: ... reinforcement rockets should be spaced further apart to avoid clustering."
4. "**AUD/USD specific**: \"Molasses. Expect 2-4 days before HTF move completes.\""
5. "**Consolidation duration**: \"If the price does not pierce or sharply whiplash upon testing the zone, expect a slow consolidation around this POI for 2-4 days.\" Consolidation lasts longer than expected."

Enforcement: "BE12 | Trading Speed adjustment applied | Day predictions include +1 day from raw timing per Section 6.10" (SP:1712); Day Bridge step 4 "Apply Trading Speed Rule: shift setups +1 day from initial prediction" (SP:2119). Whether the +1 day shifts every day's shape or only breakout timing, and what fills the vacated day, is UNKNOWN (U-8).

---

## 5. Output format and how accuracy is judged

### 5.1 Output block (SP section 6.9, SP:1990-2036, verbatim)

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

Per-day row contents: **shape, direction (up/down/range), key zone name, triggers (expiries/auctions/events), confidence %** (SP:1897, 2013). The row has no price-range field; the zone-to-zone range lives in the chain audit trail and in the SPEC shape detail block below. "The Day-by-Day Decomposition section is the DIRECT INPUT to Engine 3's Day-Level Bridge (Section 8.0.2). If this section is missing or incomplete, Engine 3 CANNOT assign DAY labels" (SP:2038).

SPEC output blocks (SPEC:652-681, verbatim):

```
MACRO SHAPE CHAIN MAP | WEEK OF [DATE]
Current Shape: [SHAPE] | Confidence: [TIER]
Primary Chain: [SS] --> [BS] --> [R] --> [WL] | Chain Confidence: [X]%
Alternative Chain: [SS] --> [WLS] --> [BS] | Chain Confidence: [X]%
Decision Zone: [ZONE RANGE] | [PRESSURE DEGREE] | ZFP: [X]%

SHAPE: [NAME] | Duration: [ESTIMATED SESSIONS]
Anchor Zone: [ZONE RANGE] | Pressure: [DEGREE] ([X]/14) | ZFP: [X]%
IP Zone Role: [Ceiling/Floor/Trigger/Rejection/Target]
Transition Trigger: [Zone failure / Zone rejection / Catalyst / Time expiry]
Next Shape: [PREDICTED] | Confidence: [TIER]
Decision Zone (if alternative exists): [ZONE] | [Condition for alternative]

AUDIT TRAIL:
Step 1: Current = [SS] | Zone [98.15-98.25] ZFP=22% (holds) + Zone [98.75-98.80] ZFP=52% (fail risk)
--> Prediction: SS --> BS | Confidence: HIGH (ZFP>45% + macro catalyst + option expiry Friday)
Step 2: Current = [BS] | Target = [99.30] (Repeated High Magnet, Apr 1 + Apr 27) | Measured Move Anchored
--> Prediction: BS --> RWL | Confidence: HIGH (target is Hard Wall, ZFP=12%, Institutional Magnet)
Step 3: Current = [RWL] | Stabilization zone = [98.15-98.25] ZFP=22%
--> Prediction: RWL --> SS | Confidence: MODERATE-HIGH (stabilization at mid-range zone)
Chain: SS --> BS --> RWL --> SS | Chain Confidence: 0.80 x 0.80 x 0.65 = 41.6% (MODERATE)
```

### 5.2 How accuracy is judged in the docs

No numeric scoring metric for a chain is defined anywhere in these sources (U-10). What exists:
- Letter grades from the operator postmortem: "Macro Shape Chain | B+/A- (shape identification mostly correct, chain sequencing had errors)" (FB:252); "Engine 2 (Macro Shape Chain) was graded more favorably (A for IP zones, A-/B+ for shape chain)" (FB:39); status "ACTIVE — Macro Shape Chain semi-accurate; operator corrections needed for full accuracy" (FB:15-17).
- Method: "VLM screenshot comparisons of generated reports versus actual market outcomes" (FB:28-29); "systematic comparison of system predictions against actual trading outcomes" (FB:37-38).
- Three axes the operator separated: "SHAPE IDENTIFICATION was mostly correct", "CHAIN SEQUENCING had errors", "TIMING was sometimes off" (FB:462-470).
- Whole-chain match: predicted "BS→R→PBS" vs actual "BS→RWL→SS→WLS" called "WRONG" (FB:254-258); a different report is described as "macro shape chain 100% correct" (SP:97, week of March 30 - April 3, 2026).
- Prescribed validation test: "The May 18-22 case study should be used as a validation test: generate the chain prediction with and without the 99.43-99.67 zone mapped, and verify the corrected chain matches actual outcomes." (FB:553-555)
- Compliance check: "verify that all shape predictions reference specific IP zone triggers with ZFP values." (FB:557-559)
- Basis claim: "Validation ... 8 months of backtested chain observations" (SPEC:73); frequencies are admitted to be "observational" not "statistically rigorous" (SPEC:843-844).

---

## 6. Operator feedback PDF — what the model got wrong and the corrected rule

### 6.1 Engine 2

| # | What was wrong | Corrected rule | Cite |
|:---|:---|:---|:---|
| E2-1 | May 18-22 chain predicted "BS→R→PBS"; actual "BS→RWL→SS→WLS". Cause: "a critical IP zone at 99.43-99.67 was not properly mapped". "The \"Recovery\" that appeared to be forming was actually price approaching this strong IP resistance zone, and the \"PBS\" that appeared to be starting was actually the zone rejecting the surge." | "Chain sequencing must be conditioned on target zone ZFP — if BS target has ZFP < 20%, predict RWL not R/PBS." The zone "had ZFP well below 30%, meaning it was highly likely to HOLD". | FB:40-41, 256-267, 464-467, 531-533 |
| E2-2 | Shapes treated as visual pattern labels | "macro shapes are NOT subjective pattern labels. They are mechanically defined by IP zone interactions. The classification is deterministic once the IP zone metrics are known." Matrix "must be applied IN SEQUENCE — check highest-priority condition first." | FB:268-271, 350-351 |
| E2-3 | Timing: "sometimes misestimated when transitions would happen" | "NY Cut Spring Release timing must be incorporated into shape transition timing predictions." Transitions cluster at 10:00 AM → 10:01 AM. | FB:468-470, 535 |
| E2-4 | "The Double Whiplash Pattern within SS was not being identified" | "two rapid whiplash moves within an SS range often precede a breakout attempt. This micro-pattern should be flagged as \"SS (Double Whiplash)\" to signal increased breakout probability." | FB:471-473, 537 |
| E2-5 | "The WLS→BS transition timing was not being properly predicted" | "when a Whiplash Storm's bounding zone begins showing increasing ZFP (moving from 25% toward 40%+), the breakout is approaching. The ZFP trend within WLS is the leading indicator for breakout direction and timing." Direction = "which bounding zone has the highest ZFP + most breakout pre-conditions active". | FB:474-476, 408-410, 539 |
| E2-6 | R allowed to run on | "R→SS reclassification must be enforced when stabilization persists > 1 full session." "Recovery is transient (half-session to one session), while SS is sustained (multi-session consolidation)." | FB:277-280, 294-296, 541 |
| E2-7 | Alternative chain not always produced | "Alternative chain analysis must always be generated alongside primary chain." | FB:543 |
| E2-8 | Breakouts accepted on wicks | "The 15-minute confirmation is NOT optional. A wick or brief spike through a zone is NOT a breakout. The Measured Move target is always anchored to the nearest Structural Extreme Magnet, NOT a blind projection." | FB:286-287 |
| E2-9 | (emphasis) | "Whiplash is guaranteed at Hard Walls with ZFP below 15%. The Liquidity Sweep Zone designation from Engine 1 is the primary identifier for Whiplash-producing zones." | FB:304-306 |
| E2-10 | Audit trail missing | "Every chain extension MUST document the audit trail: current shape, IP zone evaluated as trigger, specific ZFP and breakout pre-conditions, predicted next shape, and confidence level." | FB:496-498 |
| E2-11 | Zone grades feeding E2 | "IP Zone Mapping A/A+ (4 of 5 zones precise, 1 too wide)"; "LSZ Mapping A+/A (5 of 6 zones accurate, 1 bottom edge off)" | FB:248-250 |

Open review item: "Pillar 7 data (CME FX OI + ICE DXY Options OI) remains NO DATA — confluence floor should be adjusted to 5/12 when Pillar 7 is unavailable." (FB:549-551)

### 6.2 Engine 3 (same PDF; listed because several corrections change how E2 output is consumed)

| # | What was wrong | Corrected rule | Cite |
|:---|:---|:---|:---|
| E3-1 | April 20-24: one setup for the week, "SHORT at the Equilibrium Zone (98.29) with SL at 98.50 and TP at 97.70 (2.8x RRR). This was directionally wrong — the entire week was a BUY trend." 5-Check Direction Validation "returned 5/5 SHORT consensus"; it "is backward-looking by design". | "When DXY is at 98.10, sitting just 13 pips above a Key Support Band with ZFP 12% (a Hard Wall), the probability of a bounce is significantly higher ... needs a COUNTER-TREND CHECK" (Fix P1). TS-4: "When price is within 0.20 DXY of a HEAVY zone (ZFP < 15%), a COUNTER-TREND CHECK must evaluate mean-reversion probability." | FB:51-53, 91-100, 151-153 |
| E3-2 | Single-setup "primary chain" model: "each trade is assumed to follow the previous one" | "In a Swing Scalps regime, MULTIPLE independent setups exist simultaneously at different zones ... every IP zone with ZFP < 30% produces both a zone-rejection trade AND a zone-breakdown trade as independent setups." (Fix P2; TS-5, TS-6) | FB:101-112, 155-161 |
| E3-3 | Entry at zone edge 98.29; SL "zone + 0.09 buffer" at 98.50 | Entry at a specific key level ("98.44 (key level 98.365 inside Equilibrium Zone)"); SL anchored to next key level ("98.525 (1 pip above key level 98.44)"); mandatory "Step 0.6 Intra-Zone Key Level Scan" (TS-1, TS-2, TS-7) | FB:113-121, 137-143, 163-165 |
| E3-4 | TP 97.70 from Fib wormhole "(0.618 retrace to 1.618 extension from the swing high 98.41 to swing low 97.63)" in an SS regime | "In SS regime, the default TP should be the edge of the nearest opposing IP zone or LSZ, with Fib wormhole as a secondary \"extended target\" only if the zone is breached." Correct TP "98.02 (LSZ edge of Mid-Range Support) or 98.00 (zone edge)" (TS-3) | FB:122-131, 145-149 |
| E3-5 | Three missed setups | #1 SHORT 98.44 / SL 98.525 / TP 98.02 / 4.06x / Mon-Tue; #2 LONG 98.02 / 97.87 / 98.77 / 5.0x / Tue-Thu; #3 LONG 98.29 / 98.185 / 98.77 / 4.57x / Wed-Thu | FB:72-88 |
| E3-6 | SL/TP/RRR/limits | TS-8: "for longs, SL = demand-side LSZ bottom edge minus 3 pips buffer. For shorts, SL = supply-side LSZ top edge plus 3 pips buffer. If no LSZ exists within 30 pips, REJECT". TS-9: "TP1 = nearest opposing IP Zone boundary. TP2 = second opposing boundary (if within 80 pips). RRR = (TP1 - Entry) / (Entry - SL). Minimum 2.0:1 for trend, 2.5:1 for counter-trend." TS-10: "Maximum 3 setups per report." | FB:167-177 |
| E3-7 | Shape alignment (Phase 2 of the rebuild) | "BS = directional supported. WL = counter-trend fade supported, directional DOWNGRADED. SS = no directional trade, scalp only. R = counter-trend entry supported. DISAGREEMENT LOG: If Engine 2 contradicts trade direction, note disagreement and reduce confidence by 20 points." | FB:185-188 |
| E3-8 | Six failure modes | Garbage In/Garbage Out → Filter Checkpoint (D1); No Confluence Floor → minimum 6/14; Vague SL/TP → LSZ-anchored SL, IP-zone-anchored TP; No RRR Gate → 2.0:1 / 2.5:1; No Temporal Alignment ("Bullish setup generated when Engine 2 predicted whiplash") → shape alignment check; No Red Folder Deferral → 30-minute deferral | FB:203-236 |

Note: TS-10 "Maximum 3 setups per report" (FB:175) is superseded inside SP by "Total expected setups per week: 8-15+ (vs v5.1's 2-3)" (SP:2085). CONFLICT C-10.

---

## 7. INPUTS NOT IN OHLC

Engine 2 as written consumes Engine 1 fields; most of those are not price-derived. "Protocol A" = OTC FX option expiries feed.

| E2 input | Used for | Non-price ingredient | Cite |
|:---|:---|:---|:---|
| **ZFP per zone** | Every threshold in 2.1-2.5 | Base probability by zone type needs option-wall notional and pillar count: Hard Wall "CRITICAL OPTION WALL (≥$1.5B) + 3+ pillars + Confluent Floor/Ceiling 5-15%"; Standard Wall "SIGNIFICANT MAGNET ($850M–$1.499B) + 2+ pillars 15-30%"; Soft Wall "30-50%"; One-Touch "50-70%"; Post-Expiry Ghost "20-40%". Modifiers: "Option expiry timing (Spring Release) +20-30% (Protocol A timestamps)", "Macro catalyst aligned against zone +15-25% (Protocol F + web search)", "Cross-pair confirmation +15-25% (Protocol A multi-pair)". Price-derivable modifiers: "Increasing momentum toward zone +10-20% (Rate of change in DXY)", "Cascade effect (prior zone broke) +20-30%", "Regime change (EMA 200 cross) +15-25%". The Pillar 9 algorithm itself is a placeholder: "[unchanged from v4.5.2 — ... assigns Zone Failure Probability ...]" | SP:4056-4074, 1457 |
| **Confluence score (0-14)** | SS needs ≥ 6; WL/RWL needs ≥ 8 | Dimensions "Options-Derived" (notional ≥1.5B / $850M-$1.499B) and "Analyst Consensus" (Tier-1 sources) are non-price. Technical, Structural, Psychological (round numbers), Regime/Dynamic are price- or level-derivable. | SP:1465-1484, 1879, 1882 |
| **Pressure degree** (Heavy/Extreme etc.) | SS bounds "Heavy/Extreme" | derived from confluence score (table SP:1487-1494) so inherits the above | SP:1780, 1487-1494 |
| **Hard Wall / Institutional Magnet / Post-Expiry Ghost / Critical Option Wall tags** | BS→RWL, WL, R zone typing | Option notional and expiry state. (Institutional Magnet = Repeated Extreme Magnet inside an HTF Order Block, SP:1310, is price-derivable.) | SP:4058-4062, 1310 |
| **Breakout pre-conditions (Pillar 9)** | SS→BS, WLS direction | "option expiry timing (Spring Release), macro catalyst alignment" are non-price; "increasing momentum", "cascade effect" are price | SPEC:115-116 |
| **Option expiry strikes and sizes; NY Cut cage** | SS cage, 10:01 release | OTC expiry data (Protocol A). The 10:00/10:01 clock time itself is available from bar time. | SP:690-691; SPEC:608-609 |
| **Volatility triggers** | "Triggers" field; BS or WLS amplification | "US Treasury auctions (Bid-to-Cover Ratios >= 2.6x), EIA petroleum supply shocks (deviation >= 5M barrels), and sudden liquidity adjustments inside central bank facilities"; "Treasury auctions, ON RRP, EIA shocks can trigger BS or amplify WLS" | SP:693; SPEC:615-616 |
| **Economic calendar (Red Folder)** | R/SS before, BS/WL after; Rule 9 catalysts | ForexFactory calendar: FOMC, NFP, CPI, GDP, PMI, Retail Sales, ISM, ECI, PCE | SP:3225-3247, 1929 |
| **Regime classification** | SS zone regime; chain confidence | Pillar 9 output; formula not present in v5.3.3 (placeholder) | SPEC:94-95, 611-613; SP:1457 |
| **Measured Move Projection** | BS/PBS target | Pillar 9 Step 4; formula not present in v5.3.3 (inputs named: "range height, raw target, and structural extreme anchor") | SP:398, 1457 |
| **Macro catalyst direction** | WLS→BS direction justification | news / macro | SPEC:722-725 |
| **Analyst commentary** | zone confluence | bank-desk text | SP:729 |
| **Chain frequency data** | "adjusted for the historical frequency of the chain" | operator's 8-month hand-labelled backtest; only tier words exist (HIGHEST … LOW) | SPEC:551-552, 843-844 |
| **Cross-pair confirmation** | ZFP modifier; roadmap confluence score | other symbols' data (price of other pairs is OHLC but multi-symbol); option data per pair | SP:4072; SPEC:823-830 |
| **Prior-week shape** | Step 1 dependency | previous run's label (derivable only if E2 is run on prior data) | SPEC:738-740 |

Price/time-derivable E2 inputs, for completeness: zone edges and LSZ bands from swing highs/lows (SP:1221-1261), BoM/MoM (SP:1147-1149), reaction count (SP:1156-1159), source timeframe of a zone, 1H/4H structure (HH/HL, LH/LL), candle-size and wick pressure reading (SP:1979-1980), session and weekday from bar time, the 15-minute hold beyond a zone (needs bars of 15 minutes or finer).

The only fully price-based ZFP formula in the canon is the Pine helper (SP:3862-3867):

```pine
calcZFP(float tp, float bt, string pair) =>
    float zoneW = tp - bt
    float refRange = pair == "DXY" ? 1.60 : pair == "EUR/USD" ? 0.0200 : pair == "GBP/USD" ? 0.0200 : 0.0150
    int pct = math.round(zoneW / refRange * 100.0)
    pct
```

This is zone width as a percentage of a "Typical ... weekly range" (SP:3873-3876). It is a different quantity from the Appendix B probability (CONFLICT C-3).

---

## 8. CONFLICT register

| ID | Topic | Side A | Side B |
|:---|:---|:---|:---|
| C-1 | Classification timeframe | "All macro shape classification, chain mapping, and session decomposition MUST be performed on the 1H timeframe" (SP:1731) | "Four base macro shapes describe all DXY price action on the Higher Timeframe (HTF: 4H/D1/W1)." (SP:1743) |
| C-2 | Shape names | "Whiplash Sequence, Pullback Sequence" (SP:614; FA:127); "SS (Sideways Squeeze)" (SP:2079) | "Whiplash Storm (WLS)", "Piercing Breakout Surge (PBS)", "Swing Scalps (SS)" (SP:1745, 1753, 1765; MSL) |
| C-3 | What ZFP is | Appendix B: base failure probability by zone type (option-wall notional + pillar count) plus modifiers (SP:4056-4074); also a score-to-probability table "12-14 EXTREME <10% / 10-11 HEAVY 10-25% / 8-9 MODERATE-HEAVY 20-35% / 6-7 MODERATE 30-45% / 4-5 LIGHT 40-60% / 0-3 MINIMAL >60%" (SP:1487-1494) | Pine `calcZFP` = `math.round(zoneW / refRange * 100.0)` with DXY refRange 1.60 (SP:3862-3867) |
| C-4 | PBS thresholds | "Occurs when failing zone ZFP above 70%" (SP:1753); "pierces directly through one or more intermediate IP zones" (SP:1753) | "PBS occurs when the failing zone has ZFP > 60%" (SPEC:486-487); target ZFP "> 60%" MODERATE / "> 80%" HIGH (SP:1827-1828); "All intermediate zones: ZFP > 50%" (SP:1884); "PBS if pierces multiple zones" (SP:1776) |
| C-5 | WL/RWL rejection-zone ZFP and Hard Wall definition | "Rejection zone: ZFP < 20%, Confluence ≥ 8, LSZ" (SP:1882); WL "Rejection zone < 20%" (SP:1939); "Hard Wall (ZFP < 20%, confluence ≥ 8)" (SP:1837) | RWL "Rejection zone < 15%" (SP:1940); WL Rejection Zone "< 15%" (SPEC:794-796); "Hard Wall (EXTREME/HEAVY pressure, ZFP < 15%)" (SP:2664); Appendix B Hard Wall "5-15%" (SP:4058) |
| C-6 | NY session start | "NY Session (12:00 PM – 5:00 PM ET)", London "2:00 AM – 12:00 PM ET" (SP:698, 707) | "NY Overlap 08:00-10:00 ET, NY Open 08:30-10:00 ET, NY Mid 10:00-14:00 ET, NY Close 14:00-17:00 ET" (SP:13). Under side A the 10:01 AM Spring Release falls inside London. |
| C-7 | When breakouts start | "DXY moves zone-to-zone during London — breakout doesn't start until ~3:00 PM ET." (SP:701); "after 2:30 PM ET" (SP:710) | "London often triggers BS; NY produces the decisive shape transitions at the 10:01 AM Spring Release." (SPEC:835-836, roadmap); "Transitions cluster around this time" [10:01 AM] (FB:470) |
| C-8 | After a piercing move | "Do not expect whiplash storms on HTFs right after a strong piercing move." (SP:486) | "PBS ... almost always produces a Reverse Whiplash or Whiplash Storm at its termination point." (SPEC:127-128); PRWL "almost always leads to a new SS phase ..., or directly to a Whiplash Storm." (SPEC:180-181) |
| C-9 | Which week was the "#1 Engine 2 error" | "This was the #1 Engine 2 error that caused the April 20-24 misprediction — the engine predicted upside continuation when a Hard Wall sat directly above." (SP:1837); same claim SP:2661 | The BS→R→PBS vs BS→RWL→SS→WLS error is dated "May 18-22" with zone 99.43-99.67 (FB:40-41, 255-258; SPEC:416-433); and for April 20-24 the same PDF says the system predicted SHORT while "the entire week was a BUY trend" (FB:51-53) |
| C-10 | Chain stop rule and setup cap | "Maximum chain length: 5 shapes. Terminate if cumulative confidence drops below 25%." (SP:1893) | "(a) the end of the trading week is reached, (b) the chain enters SS with no zone having ZFP > 35% (terminal SS), or (c) the chain prediction confidence drops below MODERATE." (SPEC:539-541); "below MODERATE (below 25% cumulative)" (SPEC:716-717) while MODERATE as a transition tier = 0.50 (SPEC:553-554). Separately: "Maximum 3 setups per report" (FB:175) vs "8-15+" (SP:2085). |
| C-11 | Temporal anchor | "The temporal boundary is the Friday 5:00 PM ET close" (SP:380); "as of the Friday close" (SPEC:511) | This session's task list names a "Monday London-open boundary". No E2 source read for this digest states a Monday London-open anchor. Not resolved here. |
| C-12 | DXY-only vs per-pair chain | "No independent shape chain maps are produced for non-traded pairs" and E2 maps DXY as "primary analysis canvas" (SPEC:41-52); pair chains are "translated" with same shapes and timing (SP:1917, 3600) | "Macro shape chain must be generated PER PAIR, not just DXY. Each pair has its own 4H storyline." (SP:119); "Zone levels, shape chains, and trade setups must be constructed from pair-specific price data." (SP:101) |
| C-13 | BS→R confidence | "BS | 20–40% (Mid-range) | R | HIGH" (SP:1826); "BS | R | ... | HIGH" (SP:1806) | "the BS --> R transition probability is MODERATE-HIGH." (SPEC:532-533) |
| C-14 | RWL→SS confidence | "RWL | SS | Reversal exhausts; new range established | HIGH" (SP:1814) | Audit-trail example scores RWL→SS "MODERATE-HIGH" = 0.65 (SPEC:677-681) |
| C-15 | Counter-trend proximity | "within 0.20 DXY of a HEAVY zone (ZFP < 15%)" (FB:151) | "within 0.30 DXY points in the proposed direction" (SP:2664) |
| C-16 | Rule 4 vs the spec's own durations | "No Behavioral Generalizations. Shape durations ... must be derived from backtested data, not from behavioral estimates like \"typically lasts 2-3 sessions\"" (SPEC:704-708) | Durations are given as "Typically 1-3 sessions", "Typically 2-5 sessions" (SPEC:120, 197) with no observation counts |
| C-17 | Most frequent chain wording | "SS → BS → R → WL | HIGHEST" (SP:1787) | "BREAKOUT SURGE --> RECOVERY --> WHIPLASH REMAINS THE MOST FREQUENTLY OBSERVED PATTERN" (MSL p1) — same core, the library omits the leading SS in this sentence |

## 9. UNKNOWN register

| ID | Missing item |
|:---|:---|
| U-1 | Definition of a "session" as a duration unit (trading day vs London/NY session). Text uses "one full trading session" (SPEC:99), "half-session to one full session" (SPEC:143), "2-5 sessions" (SP:1935), and separately "2-4 days" (SP:1852). Library examples show R/SS lasting hours to ~2 days. |
| U-2 | Classification fallback when no row of matrix 6.2 matches (for example price mid-range between zones with ZFP 30-45%). |
| U-3 | Measured Move Projection formula and the Pillar 9 ZFP/regime algorithm: v5.3.3 says "[unchanged from v4.5.2 ...]" (SP:1457); v4.5.2 text is not among the named sources. |
| U-4 | Transition gaps: BS with target ZFP 40-60%; SS with bounding ZFP 30-45%; "opposing zone near" distance; "momentum builds" measure; "extreme momentum"; "volatility diminishes". |
| U-5 | Numeric value of VERY HIGH; the "adjusted for the historical frequency of the chain" formula; how tier words map to the "X%" per-day confidence. |
| U-6 | The rule that maps a chain of up to 5 shapes onto Mon-Fri (which shape occupies which day, how multi-day shapes are split, what a day holding two shapes is labelled). Only durations, templates and the +1-day rule exist. |
| U-7 | Tokyo/Asia session clock times; timezone handling across DST (all times are given as "ET"). |
| U-8 | Mechanics of the +1-day speed adjustment (which rows shift, what fills Monday, what happens to Friday's shape). |
| U-9 | Pair equivalents of DXY-denominated constants: WLS cluster band 0.30-0.50 DXY, LSZ 0.05-0.10 DXY, zone clustering 0.10-0.15 DXY. Only the Pine ZFP reference ranges are given per pair (SP:3865). |
| U-10 | A quantitative accuracy metric for a predicted chain. Only letter grades and whole-chain match/mismatch statements exist. |
| U-11 | Quantities in the shape definitions: "briefly pierces", "violent", "sharp", "mild retracement", "without pausing", minimum swing count for SS, "in succession" for Double Whiplash. |
| U-12 | Durations for PWL, PRWL, SS (Double Whiplash). |
| U-13 | How the "ZFP trend" (rising/stable/falling) is computed pre-week when in-week data is forbidden (SP:2022 vs SP:1923). |
