# 05 — Trade Structure & Rockets (PART VII / VII-B / VII-C)

Source: `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md` lines 2575–3211.
Scope: PART VII (7.1–7.6), PART VII-B (7S.0–7S.5), PART VII-C (8R.0–8R.9 incl. second 8R.9 Efficient Liquidity Mapping).
No `[unchanged from v4.5.2]` markers appear in this range — no known-gap placeholders required.

---

## 7.1 Entry Precision Rules

Translation layer: IP zones + macro shapes → executable trade construction. Every setup MUST comply.

### RULE 1 (TS-1): ENTRY AT SPECIFIC KEY LEVEL, NOT ZONE EDGE

Entries at a specific key level WITHIN the zone — NEVER the raw zone edge alone. Edge = boundary; key level = where price reacts.

- **LONG from SUPPORT or EQUILIBRIUM:** enter at the **bounce level** = 2nd lowest key level near zone bottom. Absolute lowest = zone floor (too deep — price at floor = zone failing). Bounce = LSZ/structural reaction level just above floor.
- **SHORT from RESISTANCE or EQUILIBRIUM:** enter at the **rejection level** = 2nd highest key level near zone top. Absolute highest = zone ceiling. Rejection = level just below ceiling.
- Operator proof: LONG from MRS entered at 98.02 (LSZ edge = 2nd lowest), NOT 98.00 (floor). SHORT from EQ at 98.44 (option strike = 2nd highest), NOT 98.41 (zone top). The 2-pip difference = win vs loss.

Key level sources (Intra-Zone Key Level Scan, Step 0.6):
1. Pivot levels inside the zone
2. Option strike equivalents inside the zone
3. Swing highs/lows inside the zone
4. Fib retracement levels (0.382, 0.618) of the zone's own range
5. Prior daily closes within the zone
6. Round numbers (.00, .25, .50, .75) within the zone
7. Zone midpoint

Fib spiderweb applicable: nearest fib level TO the zone edge = precise entry. Context 2 scalps: add 0.5–1 pip buffer in front of fib level.

### RULE 2 (TS-2): SL ANCHORED TO NEXT STRUCTURAL DEFENSE LEVEL BEYOND THE ZONE

SL at nearest structural defense beyond the zone — NOT arbitrary buffer from entry.

- **SHORT SL:** nearest big figure (round number) above entry + 2.5 pip buffer. Fallback: next zone boundary + 3 pips, then LSZ supply-side top + 3 pips.
- **LONG SL:** key level of zone below entry − 1 pip. If key level too close (< 5 pips), use next one down. Fallback: LSZ demand-side bottom − 3 pips, then entry zone's own bottom boundary − buffer (EQUILIBRIUM zones where zone below is distant).
- **Minimum SL distance:** 2.5 pips swing (Swing Stack); 1.5 pips scalp (Scalp Stack, 5m precision).
- **Maximum SL distance:** no SL anchor within 30 pips (0.30 DXY) → REJECT setup.
- Operator proof: SHORT SL = 98.525 (big figure 98.50 + 2.5 pips). LONG SL from MRS = 97.87 − 0.01 = 97.86 (zone-below key level − 1 pip). LONG SL from EQ = 98.185 (EQ bottom 98.29 − buffer, zone below distant).

**Correction/Reversal Entry Exception (CRITICAL):** counter-trend CORRECTION/REVERSAL entries → SL 1–2 pips INSIDE the next zone beyond entry (price likely pierces entry zone briefly before reversing). Standard outside-zone SL = trend-following entries only.

### RULE 2.5: LSZ SL PLACEMENT

- SL at LSZ boundary + 3 pip buffer (standard).
- LSZ extended per Bottom Edge Extension (sweep scan 0.05–0.10 DXY below swing highs) → use extended range.
- LSZ boundary = structural defense; sweep through LSZ = zone failure.
- Minimum SL distance: 2.5 pips from LSZ edge.

### RULE 3 (TS-3/TS-9): TP AT MAJOR OPPOSING ZONE / LSZ EDGE — REGIME-CONDITIONAL

#1 cause of v5.0 F-grade setups was Fib wormhole as primary TP in SS regime.

| Regime | Default TP | Rationale |
|:---|:---|:---|
| SS (Swing Scalps) | Nearest MAJOR opposing zone edge OR nearest LSZ edge | SS oscillates between zones; Fib wormhole projects beyond range |
| BS (Breakout Surge) | Fib wormhole (0.618→1.618 or 0.382→1.382) | Directional move has structural backing |
| WL/RWL (Whiplash) | Fib wormhole if anchored to rejection point | Post-rejection move is directional; anchor at rejection |
| R (Recovery) | Nearest IP zone in recovery direction | Recovery transitional — TP at next zone |

SS-specific:
- LONG targets RESISTANCE (skip EQUILIBRIUM — mid-range, not targets).
- SHORT targets SUPPORT (skip EQUILIBRIUM).
- LSZ precision: LSZ edge inside opposing zone closer than zone boundary → use LSZ edge.
- NEVER Fib wormhole as primary TP in SS — extended target ONLY after primary zone-edge TP hit.

TP2: second opposing zone boundary if within 80 pips (0.80 DXY).
Operator proof: SHORT TP = 98.02 (LSZ demand 97.97–98.02 top edge inside opposing SUPPORT). LONG TP = 98.77 (Upper IP Resistance bottom edge).
Override: fib wormhole TP aligned with verified IP zone or reaction level takes priority regardless of regime. Regime logic applies ONLY when fib TP is unanchored.

---

## 7.2 Trade Direction Validation Protocol (6-check, v5.0.0)

v4.5.2 5-check caught trend/BoM/LSZ/zone-failure/macro-shape but missed the Counter-Trend Check. Apr 27–May 1 report went wrong (upside call vs actual downside breakout); Apr 20–24 proposed upside into a Hard Wall.

Checks 1–5:
1. **4H Trend:** HH+HL = bullish (favors LONG); LH+LL = bearish (favors SHORT). 4H = structural truth (days/weeks).
2. **BoM Zone Alignment:** nearest BoM above → SHORT; below → LONG. BoM = 100% guaranteed reaction; direction to nearest BoM = next move.
3. **LSZ Direction:** nearest LSZ below → sweep down first (LONG after sweep); above → sweep up first (SHORT after sweep).
4. **Zone Failure Cascade:** failing support (ZFP trending up toward 45%+) = bearish cascade → SHORT; failing resistance → LONG.
5. **Macro Shape Chain:** Engine 2 chain direction = bias (e.g. BS down → SHORT).

Check 6 — Counter-Trend Hard Wall (P1 postmortem fix, CRITICAL):
- Identify nearest Hard Wall / Institutional Magnet in proposed direction.
- Hard Wall (EXTREME/HEAVY pressure, ZFP < 15%) within 0.30 DXY in proposed direction → trade NOT invalid but REQUIRES: (a) specific wall-failure mechanism (e.g. "option expiry removes cage 10:01 AM Tuesday"); (b) half position size; (c) tighter SL just beyond wall (not standard LSZ distance); (d) explicit statement: "COUNTER-TREND: Hard Wall at [level] with [X]/14 pressure opposes this trade. Mechanism for wall failure: [reason]. Position size reduced by 50%."
- No Hard Wall within 0.30 DXY → Check 6 NEUTRAL.

Mandatory output block (verbatim fields):
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

RULE: 4+ of 6 checks disagree with proposed direction → direction MUST be reversed. No exceptions.

---

## 7.3 Scaled Entry Protocol

High-conviction only (God-Tier, High). 3 entries, 33% each:
1. **Zone First Touch (33%):** first reach of IP zone. Earliest, highest risk, best price.
2. **Zone Mid-Confluence (33%):** most overlapping key levels inside zone. Precision entry — operator's preferred.
3. **Zone Far Edge (33%):** side opposite approach. Confirmation — zone proven holding.

Average entry = weighted average of triggered entries. SL from worst-case entry (First Touch). TP from average entry.

---

## 7.4 Trade Flow Continuity Protocol

Chain setups: TP of Trade N = entry zone of Trade N+1. LONG support → TP resistance → SHORT resistance → TP support → repeat.
1. Chain only setups sharing a structural boundary.
2. Direction flips at each boundary (LONG→SHORT at resistance; SHORT→LONG at support).
3. Each chained trade independently meets minimum RRR.
4. Max 3 trades per chain; then reassess macro shape.
5. Zone failure (breakout) terminates chain; new chain in breakout direction.

---

## 7.5 Minimum RRR Standard

| Setup Quality | Min RRR | Rationale |
|:---|:---|:---|
| God-Tier (85+ conf) | 4x | Highest conviction, tighter threshold |
| High (75–84) | 4.5x | Strong conviction, standard |
| Standard (65–74) | 5x | Lower conviction needs higher compensation |
| Supplementary (flow continuity) | 3x | Compensated by adjacent chain trades |
| Swing Scalp (Scalp Stack) | 3x | Shorter duration, higher frequency |
| Reinforcement entries | 2x | Compensated by sizing + primary RRR |
| Counter-trend in BS/WL | 2.5x | Higher bar in directional regimes |
| Counter-trend in SS | N/A | Both directions trend-valid per TS-6 |

---

## 7.6 Pair-Specific Trade Mechanics (v5.0.0)

For EUR/USD, GBP/USD, AUD/USD via Part IX translation:
- Entry precision uses PAIR-SPECIFIC zone edges/fibs — NOT DXY levels converted.
- SL uses PAIR-SPECIFIC LSZs from pair's own swing structure — NOT DXY LSZs converted.
- TP uses PAIR-SPECIFIC opposing zones/reaction levels — NOT DXY zones converted.
- Pip values: EUR/USD, GBP/USD = $10/pip (standard lot); AUD/USD ≈ $6.50/pip.
- Session timing SAME for all pairs (London/NY drive all three).
- Macro shape chain SAME for all pairs (same shapes, inverted direction per 9.10).

---

## 7S.0 Swing Scalp Purpose

Same mechanics as HTF swings on Scalp Stack (30m/15m/5m) inside consolidation. "Swing scalps" = scalping with swing mechanics: supply↔demand, pressure-zone↔pressure-zone. Only timeframe stack + pip scale differ.
Operator insight: "Inside ONE intraday 6x RR swing, literally 4x additional RR sits inside it just by liquidity sniping the swing scalps that complete the HTF swing." Scalps are the PRIMARY profit engine in consolidation weeks — not secondary.

---

## 7S.1 Swing Scalp Parameters

| Parameter | Swing (HTF) | Swing Scalp (LTF) |
|:---|:---|:---|
| HTF Storyline | 4H | 30m |
| Trading TF | 1H | 15m |
| Precision TF | 30m | 5m |
| Typical SL | 8–15 pips | 3–6 pips |
| Typical TP | 40–100+ pips | 15–30 pips |
| Typical RRR | 4–10x | 4–6x |
| Min RRR | 4x high-conf / 5x standard | 3.0:1 |
| Min SL distance | 2.5 pips | 1.5 pips (5m precision) |
| Entry timing | 3+ retests on 1H | 2+ retests on 15m |
| Session | NY | London + NY |
| Active when | BS/WL/Recovery | SS/WLS/R |
| Pip threshold | 40+ pips to TP | 15–30 pips to TP |

---

## 7S.2 Swing Scalp Setup Types (full procedural)

### TYPE 1: Standard Swing Scalp (consolidation range — MOST COMMON)
1. Mark 30m consolidation ceiling (highest rejection) + floor (lowest bounce) = bounding zones.
2. Map 15m S/D zones inside: classify BoM/MoM, mark reaction counts. BoM = primary entry. MoM = TP targets for opposing direction only.
3. Direction bias via pressure rules (Part II §2.0): which candles bigger, where wicks point.
4. Entry per zone: LONG floor demand at 15m BoM reaction level (2nd retest min); SL 1.5–2 pips below 15m zone edge; TP at 30m ceiling boundary. SHORT ceiling supply mirrored (SL 1.5–2 pips above, TP at 30m floor).
5. 1-2-3 timing: 2+ retests on 15m required. Virgin 15m zones = no entry unless BoM.
6. BoM/MoM enforcement = HTF rules. BoM entry; MoM TP target; virgin MoM reject.
7. Session: London = PRIMARY; NY = SECONDARY.
8. RRR ≥ 3.0:1. Range < 15 pips → REJECT; wait for expansion/breakout.
Both directions co-exist in SS — SHORT ceiling + LONG floor simultaneously (TS-6 at every scale).

### TYPE 2: Double Whiplash Inverse (SS(DWL) compound)
1. Confirm SS(DWL): two whiplashes ≤ 1.5 sessions; both ceiling + floor hit with strong rejections.
2. Leg 1 SHORT at ceiling supply rejection: SL 1.5–2 pips above ceiling edge; TP at floor demand boundary; RRR ≥ 3.0:1 individually.
3. Leg 2 LONG at floor demand reaction IMMEDIATELY after Leg 1 TP: SL 1.5–2 pips below floor edge; TP at ceiling boundary; RRR ≥ 3.0:1 individually.
4. Combined RRR compounds (4:1 + 4:1 = 8:1).
5. Size Leg 2 for floor FAILURE (breakout transition). Leg 2 stopped → SS→BS transition likely → switch to Swing Stack.
Works ONLY with both bounding zones holding. Either zone 3+ reactions (depleted) → expect breakout; map Type 4 contingency.

### TYPE 3: Liquidity Snipe (5m precision inside confirmed 15m move)
1. Wait for 15m confirmation: 15m scalp triggered, price moving to TP. NO sniping before confirmation.
2. Drop to 5m: map ALL unmitigated 5m zones between price and 15m TP.
3. Enter at 5m zone reaction level on reach.
4. SL 1.5 pips outside 5m zone edge.
5. TP = next 5m zone in direction, OR 15m TP if next 5m zone too close.
6. Progressive management: each confirmed snipe → earlier entries' SL to breakeven.
7. Max 2–3 snipes per 15m scalp. >3 = overtrading.
Operator: "The money is made catching movement from one liquidity zone to another. It is already moving." Snipe rides a confirmed move at guaranteed touchpoints — not direction prediction.

### TYPE 4: SS→BS Transition Scalp (consolidation ending)
1. Late-consolidation detect: bounding-zone ZFP rising, repeated one-sided tests, 15m HHs or LLs forming inside range.
2. Breakout trigger: SHORT = 15m close below structure (lower low under floor); LONG = close above (higher high over ceiling).
3. Entry on 15m close beyond structure — NOT 5m (too noisy).
4. SL: opposite side of consolidation range + 2–3 pip buffer.
5. TP: next HTF (1H) liquidity zone in breakout direction, per Timeframe Element Matching (≤ 2 TF dimensions from source). NOT 30m zone; NOT 4H (exceeds 2-dimension limit from 15m).
6. Matching law: 15m-source breakout → TP at 30m or 1H. 4H targets ONLY when breakout source is 1H or 4H.
7. Post-confirmation: switch Scalp Stack → Swing Stack; all reinforcements on Swing Stack.
Rule: "If not right near a strong 4H pressure zone — BS is most likely days away." Map transitions ONLY near HTF zone with rising ZFP.

---

## 7S.3 Swing Scalps within HTF Moves

Every intermediate untested liquidity zone inside an HTF swing WILL be touched = guaranteed scalp entries.
1. Take Engine 3 Phase 0–6 HTF swing (entry → TP).
2. Map ALL intermediate 15m liquidity zones between HTF entry and TP.
3. Each unretested intermediate zone = potential scalp entry at 15m reaction level (Type 1 mechanics).
4. Each scalp TP = NEXT intermediate zone in HTF direction; final scalp TP = HTF TP.
5. Combined scalp RR ≈ 4x the HTF swing RR alone.

---

## 7S.4 Scalp BoM/MoM + Reaction Counter (15m, identical to HTF)

- 15m BoM = PRIMARY scalp entry; 100% guaranteed reaction if unmitigated.
- 15m MoM = TP targets for opposing direction; entry ONLY with exceptions.
- 15m virgin MoM = DEATH ZONE, reject entry.
- 15m depleted (3+ reactions) = TP only, never entry.
- 0 reactions: strongest if BoM; DEATH if MoM. 1–2: active, entries valid if BoM. 3+: depleted, TP only.
- 15m pressure zone with juice between price and 15m BoM target gets liquidated first.

---

## 7S.5 Swing Scalp Output Format (v5.3.3 mandatory fields)

```
SWING SCALP SETUP: S-[#] [Direction] [Quality]
DAY: [Monday/Tuesday/Wednesday/Thursday/Friday] ← v5.3.3 MANDATORY
SESSION WINDOW: [London / NY / Both] ← v5.3.3 MANDATORY
SHAPE TRIGGER: [SS/WLS/R/SS(DWL)] ← v5.3.3 MANDATORY
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

---

## 8R.0 Reinforcement Purpose

Reinforcements turn 1D (single entry/SL/TP, 4–6x) → 2D (entry + reinforcements, 15–25x) → 3D (+ multi-chart DXY master + pairs, 25–30x+).

v5.3.3 Timing Inheritance: reinforcements inherit parent DAY. HTF swing Wednesday NY → rockets SET UP Wednesday London premarket, TRIGGER Wednesday NY, late fills may slip Thursday London (+1 day). Schedule known in advance; Weekly Execution Calendar (§8.5) lists reinforcements under parent DAY.

---

## 8R.1 Liquidity Ladder System (procedural)

1. Confirm primary moving: 1-2-3 retest complete, price left entry zone with momentum.
2. Map ALL intermediate zones entry→TP (Sequential Liquidity Sweep).
3. Stop orders at FAR EDGE of each zone (side opposite approach): reaction+rebound = no fill; breakthrough = fill confirms zone failed, move continues.
4. Classify: BoM intermediate of OPPOSING direction = expect stall → consider TP2/TP1 adjustment. Trend-aligned MoM in path = minor reaction then continuation; do NOT TP there. Depleted (3+) = sliced through; momentum confirmation.
5. SL: Swing Stack 2.5–3 pips outside intermediate zone; Scalp Stack 1.5 pips outside 5m zone. Progressive tightening per confirmation.
6. TP: same TP1 as primary for ALL reinforcements.
7. ≥ 2 reinforcement entries MUST be inside primary SL (critical risk rule).

---

## 8R.2 Fibonacci Rocket System

Standard levels:

| Type | Fib | Purpose | Reaction |
|:---|:---|:---|:---|
| Entry | 0.618–0.786 | Primary entry | — |
| Rocket 1 | 1.382–1.786 | First reinforcement (CLEANEST, 90% accuracy) | Strong pressure zone |
| Trigger | 2.382–2.786 | Second reinforcement / confirmation | Momentum zone |
| Target | 3.382–3.786 | Extended TP | — |

Shorter-move levels: Entry < 0.382 (quick); Rocket 1 0.618–0.786; Trigger 1.382–1.786; Target 2.382–2.786.

Key Level Zones (v5.3.0, from Trading Laws): 0.382 (.382–.5) initial strong reaction / first pressure; 0.618 (.5–.618) transitional; 0.618–0.786 STRONG PRESSURE ZONE, most reliable; 0.786 (.786–1) final blast before full extension.

Mandatory Fib mapping per rocket:
1. Map nearest 15m swing high/low.
2. SELL: entry-zone support = fib "bottom"; nearest pre-consolidation swing high = "top"; Map = DOWN.
3. BUY: entry-zone resistance = "bottom"; nearest pre-consolidation swing low = "top"; Map = UP.
4. 1.382–1.786 = cleanest reinforcement entry ("exact Fib lines line up with 90% accuracy").
5. Trigger ≈ 2.382–2.786.

Three-type classification (full specs §8R.6): FLR = first Fib contact, 30m, THICK buffer (2 thick or 3 thin), Earth Heavy. FR = localized 15m Fibs for LSS/scalps, Fire Precision. LR = subsequent contacts, zone-to-zone, THIN buffer (1 thick or 2–3 thin), Water Precision. Fib + Ladder overlap = strongest reinforcement (dual confluence).
Sequencing law: unmitigated Key 1–2 Fib level → FR (thick buffer). After FR mitigates it → LR (thin buffer).
Tolerances: 20–30% failure ACCEPTABLE; 70–80% success = excellent. NY rockets need ≥ 3 pip SLs or explode.

---

## 8R.3 Multi-Zone Overlapping Risk Management

1. ≥ 2 reinforcements inside primary SL.
2. Before primary SL hits, 2+ reinforcements should have opened.
3. Sizing: primary = full; reinforcements = 50–75% of primary each.

---

## 8R.4 TP Management (operator discretion)

1. 70–80% rule: price at 70–80% of TP + reacting → SL to 65–70% profit.
2. BoM re-entry: post-TP continuation from unmitigated BoM zone.
3. Intermediate opposing BoM strong reaction → move SL beyond reaction zone.
4. Reinforcement trailing → most recent held intermediate zone.

PROFIT TAKING LAW — Air Infrastructure (v5.3.0 MANDATORY): close ALL trades by NY close; no London-mapped trades overnight. Exception: trades OPENED at NY end for Tokyo/London action. Strong analysis → re-enter Tokyo, catch rest of wave. Cannot move everything 30–50% into profit → take ALL profits before close. Mandatory. "Whatever profits are floating at end of day — CLOSE THEM. TAKE ALL THE PROFITS. Re-enter tomorrow. If REALLY winning, re-enter."

---

## 8R.5 4H BoM Cascade (CRITICAL)

"BoM Unmitigated 4H liquidity will usually pierce through everything until it reacts to liquidity of the same element."
1. 4H BoM entry→target: ALL intermediate 1H/30m zones PIERCED. Place reinforcements expecting quick triggers.
2. True TP1 = next 4H zone of same element, NOT nearest 1H zone.
3. SL buffer 3–5 pips minimum for cascade volatility.
4. Density: 3–4 reinforcements (vs normal 2); move travels further.

---

## 8R.6 Three-Type Rocket Architecture (v5.3.0 CRITICAL)

Wrong-type-at-wrong-time = preventable failures. Selection MANDATORY.

**FLR — Fibonacci Liquidity Rocket — Earth Element Heavy Attack.** Air (30m Fib triggers) + Earth (liquidity entry/SL anchors). 30m scale: Fibs = triggers, liquidity zones = entries/SLs. Use: forward-mapping HTF storyline ("Fibonacci Vision highlights highest probability LR setups"). Buffer THICK: 2 thick zones or 2–3 thin; ≥ 1 FULL zone between trigger + entry. Trigger: stop 1–2 pips INSIDE target zone (prevents false sweeps). Entry at Fib-confirmed liquidity edges. SL 1–2 pips OUTSIDE back edge of SL zone. Capacity: ≤ 3 rockets/trade; conscious RAM — ONE pair per FLR session. Definition (verbatim core): extended Fibonacci Zones (1–2 levels) forward-mapping Liquidity Rockets for HTF storyline on 30m; Fibs = triggers, liquidity = entry/SL; liquidity zones = fundamental anchors.

**FR — Fibonacci Rocket — Fire Element Precision Attack.** Air (15m Fibs) + Fire (S/D precision strike). 15m storyline for LSS + 5m scalps. Buffer standard 1–2 zones. Trigger/Entry/SL all from 15m Fib levels; liquidity zones = confluence/precision. SL 1–2 pips outside SL zone. Key Horizontal Lines = "thin zone" anchors. Capacity ≤ 3/trade. Definition (verbatim core): 15m storyline mapping localized 15m Fibs for LSS/5m scalps; Fibs = trigger/entry/SL; Key Horizontal Lines valid anchors.

**LR — Liquidity Rocket — Water Element Precision Attack.** Earth (pure liquidity flow through Earth density channels) — "water through a riverbed". Zone-to-zone during confirmed moves. "Simple & obvious. Built-in 20–30% failure rate." Buffer THIN: 1 thick OR 2–3 thin; NO entry buffer required. Trigger: stop 1–2 pips INSIDE target zone; first zone normal; zone 2+ back-to-back relaxed 0.5 pip inside. Entry pure S/D/L ("fib maps NY move then ignored for LSS setups — pure S/D/L; flow with it"). SL: SL always 1 full pip outside back edge of zone — NO EXCEPTIONS, ESPECIALLY IF THIN (also stated as 1–2 pips outside). Expected RRR 2–4x (lower than Fib rockets). Capacity ≤ 3/trade.
Amplifier: thin zones inside a 4H liquidity pool each count as 2 thin zones.

ROCKET SAFETY (MANDATORY): max 3 rockets/trade (recommended 2). ONE pair at a time for FLR (conscious RAM; plain set-and-forget multi-pair entries fine, FLR needs attention). Reconsider multi-pair only after $1,000,000 live profits. NY rockets ≥ 3 pip SL. London 1–2 pip SL buffer. DO NOT reinforce THIN zones; DO reinforce THICK zones (hold + real fuel).

---

## 8R.7 Stop-Limit Order Mechanics (v5.3.0 CRITICAL, operator-verified)

Trip-wire weapons — precise mechanics, not metaphor: STOP ORDER at trigger zone trips → creates LIMIT ORDER at entry zone → limit = "rocket". Built-in MetaTrader STOP-LIMIT.

Self-executing algorithm:
1. Set primary + ALL rockets SAME TIME (London premarket).
2. Rockets SELF-GENERATE as stops trip — no chart-watching needed.
3. Rocket trips → primary already in profit → SL to breakeven → RISK-FREE reinforcement.
4. Correct analysis: 2–3x upside, risk-free. Wrong: only primary loses — same capital at risk. Rocket fails (20–30%): primary at BE/minor profit offsets.
Manual algorithm: "Instead of coding an algorithm … set it up MANUALLY … one-and-done … Set up in morning, walk away, check 10 PM."

Trigger zone selection: 2–3 zones IN FRONT of entry (direction price must travel); ≥ 1 FULL zone buffer trigger↔entry; thin zones NEVER trigger/entry/SL zones; 2 thin zones in front → 3rd zone = trigger. "90% of rockets self-activate if stop 2–3 zones in front" (Ladder Method).

Trigger precision: stop 1–2 pips INSIDE target zone — NOT edge (defeats false sweeps). Rocket #1: 1–2 pips inside CLOSE edge. Rocket #2/3: 1–2 pips inside FAR edge. LR back-to-back grouped: zone 2+ relaxed 0.5 pip inside.

4-point precision per rocket (MANDATORY): (1) front edge/middle of zone = limit activation; (2) back edge = max entry deviation; (3) front edge of SL zone = min SL distance; (4) middle/back edge of SL zone = thin-liquidity extended SL.

SL: 1–2 pips OUTSIDE BACK EDGE of SL zone; thin zone → SL 1 pip inside next zone (extra buffer); NY 2–3 pips outside, London 1–2; "if not this much distance — rockets blow up in your face." ROCKET SLs ALWAYS 1 FULL PIP OUTSIDE BACK EDGE. NO EXCEPTIONS. ESPECIALLY IF THIN.

Triple Anchor per reinforcement (MANDATORY): (1) stop zone target (trips order); (2) entry zone (fills limit); (3) SL zone (anchors SL).

Fib mapping for reinforcements: nearest 15m swing high/low; entry-zone S/R = fib "bottom"; nearest relevant swing extreme = "top". SELL: entry support = bottom, pre-consolidation swing high = top, DOWN. BUY: entry resistance = bottom, pre-consolidation swing low = top, UP.

---

## 8R.8 VLM-Verified Rocket Mechanics (v5.3.2, corrected audit of 38-chart Winning Trade Library)

6 GBPUSD 15m/30m charts carried T/E/SL labels (first VLM pass misclassified; corrected pass with system rules = authority):
1. T/E/SL all at THICK zones — confirms "thin NEVER entry/SL" compliance on these charts. Nuance (operator): rule-by-design, not unconditional empirical absolute; E placement context-dependent; 6 charts ≠ all edge cases.
2. T↔E buffers VARIABLE: LR = 1 buffer zone (thick or thin); FR = 2 buffer zones (Fib present or structure requires). Matches spec (LR 1 thick / 2–3 thin; FR 2 thick / 2–3 thin); "always 1" claim was wrong.
3. Conditional buffer: thick zone directly in front → 1 buffer suffices; thin in front → 2–3 until thick found ("2 thin in front → 3rd = trigger"). Back-to-back thick = 1 buffer fine.
4. T→E gap 10–20 pips on GU, typically ~15 (zone spacing incl. buffers).
5. E→SL 18–45 pips on GU (15m vs 30m structure; SL at next thick zone = Liquidity Shield).
6. Mixed LR+FR within same trade per local structure; "LR 83%" was misclassification artifact. LSS environments skew LR (fib maps NY move then ignored; setups pure S/D/L); FR where Fibs align.
7. 2–3 rockets/trade (2 charts × 2 groups, 2 × 3 groups, 2 × 1+1) — confirms max-3 (recommended 2).
8. FR/Fib alignment on page16_img1: 0.618/1.618/2.618 + T/E/SL with 2 thick buffers — confirms 1.382–1.786 cleanest entry, 2.382–2.786 trigger.
9. Rockets fill when macro shape confirms; non-fill chart had BS(Reverse)→Recovery transition = 20–30% failure when direction unconfirmed.
10. FLR first-contact: FIRST Fib contact → FR w/ 2 thick or 3 thin buffers; subsequent same-level contacts → LR w/ 1 thick or 2–3 thin. Consistent with mixed LR/FR per trade.

Corrected architecture diagram (verbatim):
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

---

## 8R.9a Master Trade Setup = E + FLR (v5.3.0 HIGH)

Fractal integration of all four elements. E = Earth + Fire (liquidity zone + S/D overlap — firepower meets fuel). FLR = Air + Earth (Fib prediction anchored to liquidity). Four-element convergence = Avatar State = FRACTALLY LOCKED at every scale.
- Earth: entry at liquidity/IP zone. Fire: S/D overlap. Water: macro shape direction/timing. Air: Fib spiderweb entry→TP incl. every rocket point.

Spec:
1. Standard §7.1 entry at BoM S/D (Fire) overlapping liquidity zone (Earth).
2. Macro shape (Water) confirms direction/timing.
3. NY Fib Rocket map — key 1 + 2 Fib levels (Air).
4. Liquidity around 1.382–1.786 + 2.382–2.786 on 15/30m (Earth anchors for Air).
5. ≤ 3 FLR rockets at Fib-confirmed liquidity (Air triggers + Earth entries).
6. Additional LRs at intermediate zones between FLRs (Water through Earth).
7. Total active rockets: up to 7 with hardwired safety, self-managed autonomously.

Profit: "Only decide: TP at NY end, or move all 30–50% into profit and run overnight." Cannot reach 30–50% → take ALL before close. Mandatory (§8R.4).
"Once you have this you have everything." Avatar State — trader as instrument of all four elements.

## 8R.9b Efficient Liquidity Mapping (v5.3.0 HIGH; source labels second 8R.9)

Don't map whole chart — ONLY trade-relevant liquidity.
1. Map NY Fib Rocket setup first — key 1 + 2 Fib levels.
2. Liquidity SPECIFICALLY around them: 15/30m chart, scroll AS FAR LEFT as needed around 1.382–1.786 + 2.382–2.786 ("exact Fib lines line up with 90% accuracy").
3. Ignore liquidity OUTSIDE 0–1 and key 1/2 levels.
4. Fibo tool = speed + precision: lower latency, faster execution, hardwired precision.
Simultaneous build: full setup = Entry + FR + LR; Master = Entry + FLR.

---

## EXECUTION CHECKLIST (7.1 + 7.2 + 8R.7 ordered)

From §7.1 entry/SL/TP:
- [ ] Entry at 2nd-lowest (LONG bounce) / 2nd-highest (SHORT rejection) key level — never raw edge/floor/ceiling. Fib applicable → nearest fib TO edge (+0.5–1 pip Context-2 buffer).
- [ ] SL at next structural defense beyond zone: SHORT big-figure + 2.5 (fallback zone-boundary + 3, LSZ-supply-top + 3); LONG zone-below key − 1 (skip if < 5 pips; fallback LSZ-demand-bottom − 3, EQ-own-bottom − buffer). Counter-trend correction/reversal → SL 1–2 pips INSIDE next zone. LSZ-anchored → boundary + 3 (extended range if extended). Enforce min 2.5 swing / 1.5 scalp; reject if no anchor ≤ 30 pips.
- [ ] TP regime-correct: SS → major opposing zone/LSZ edge (LONG→Resistance, SHORT→Support, skip EQ, LSZ-if-closer, never Fib-primary); BS → Fib wormhole; WL/RWL → Fib from rejection; R → next IP zone. TP2 = 2nd opposing boundary ≤ 80 pips. Fib+zone alignment overrides regime.

From §7.2 direction (all 6, reverse if ≥ 4 disagree):
- [ ] Check 1: 4H trend (HH+HL bull / LH+LL bear).
- [ ] Check 2: nearest BoM above→SHORT / below→LONG.
- [ ] Check 3: nearest LSZ below→sweep-down-then-LONG / above→sweep-up-then-SHORT.
- [ ] Check 4: failing support (ZFP→45%+)→SHORT / failing resistance→LONG.
- [ ] Check 5: Engine 2 chain direction = bias.
- [ ] Check 6: Hard Wall (EXTREME/HEAVY, ZFP < 15%) ≤ 0.30 DXY in direction? If yes → wall-failure mechanism + half size + SL just beyond wall + written COUNTER-TREND statement. Emit full validation block + consensus X/6 + position Full/Half/Quarter.

From §8R.7 rocket placement:
- [ ] Trigger 2–3 zones in front, ≥ 1 FULL zone buffer, thick-only trigger/entry/SL (2 thin in front → 3rd = trigger). Stop 1–2 pips INSIDE zone (#1 close edge; #2/3 far edge; LR back-to-back zone-2+ 0.5 pip).
- [ ] 4-point entry spec (limit point / back edge / SL-zone front / SL-zone mid-back) + Triple Anchor (stop zone / entry zone / SL zone) + Fib map (entry S/R = bottom, swing extreme = top, SELL DOWN / BUY UP).
- [ ] SL 1 full pip outside back edge NO EXCEPTIONS (thin → +1 pip into next zone; NY 2–3 out, London 1–2). Max 3 rockets (2 recommended), one FLR pair at a time, THICK only, ≥ 2 reinforcements inside primary SL, sizing 50–75%.

---

## SOURCE ANCHORS

Every anchor below was verified by printing the referenced line (never fabricated).

- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:2579` — §7.1 Entry Precision Rules
- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:2871` — §8R.0 Reinforcement Architecture purpose
- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:3096` — §8R.8 VLM-verified rocket mechanics
