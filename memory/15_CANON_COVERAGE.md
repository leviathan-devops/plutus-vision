# 15 — CANON COVERAGE MATRIX (goal prompt v2, section 4). One row per canon step -> function -> state.
States: NB not built · PB partial / deviates from text (rebuild) · B built, believed literal · A audited by outside agent · PV pixel-verified · ND no data (optional input, L-32).
Refs: P533 = canon/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md · P452 = e1_tool/canon_extract/P452_FULL... · E3C = canon/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md ·
GS = handover 03_HOST_BIBLES/TTE_GOLDEN_STANDARD_COMPLETE_REFERENCE.md · FA = canon/Toolset/Trident_Fractal_Architecture_FirstPrinciples_v2.3.md · R-xx = handover rulings (01_BINDING_SPEC bundle lines 23-205) · L-xx = memory/04.
RULE: re-read the cited lines in full before coding a row. A row is not "B" unless every sentence of its text has code.

## 0. Operator rulings that shape the build (read first-hand 2026-11-26)
| id | ruling | consequence |
|---|---|---|
| R-04 | E1 = supply, demand, liquidity AND IP zones; E2 = shape chain computed from E1 data; E3 = trade setups. "E1 correct -> E2 obvious -> E3 obvious." | engine boundaries |
| R-30 | Entire E1 rendered ON TOP of the sealed V1 (LuxAlgo liquidity = A+, S/D = A-, "one side of the coin"); E1 canon from the prompt = the second side | V1's S/D + liquidity zones are E1 data (row E1-V1) |
| R-03 | Phases: E1 zone model (face A) -> S/D/L on top (face B) -> E2 phase one = the BOXES -> E2 face B = the LINE. "the chain leads and the shapes follow" | E2 render = day boxes, then the line |
| R-09 | Trades are drawn as POSITION BOXES (red = SL side, green = entry->TP, entry at their shared edge), not full-width rectangles (those are zones). 1H is the authoritative source for the AI. | E3 render grammar |
| R-10 | Rocket markings in his screenshots are not trades | oracle reading |
| R-07 | <= 8 real trades per pair per week on 1H (6-10; 1-2 per day); inclusion gate confidence 65; only GOD_TIER and HIGH shown | E3 gate (with CLAUDE.md <= 11, E3C f(T) >= 8 per pair) |
| R-13 | Only test: render in Pinebox, look, "do the candles react ... yes or no" | grading |
| R-14 | E1 = the v5.3.3 prompt, every token | E1 rows below |
| R-15 | Acceptance: golden week Jul 6-10 first (visual oracle), then random weeks, uniform. "THERE IS NO FLAW IN THE STRATEGY ... THE ISSUE IS ALWAYS YOUR SHITTY CODE." | anchor week = golden week |
| R-16 | E3 authority = corrected E3 spec; v8 python = historical reference only | trident_engine3_v8.py is reference, not authority |
| R-17 / L-35 | ZFP = strength only; shown as the zone type's range | |
| R-36 / R-37 | two-week render window; no caps as a fix | |
| L-37 / L-38 / L-39 / L-40 | no minimum move for S/D; zone = candle before the strong move, wick to wick; pressure zone = structure + levels joined, both visible; 4H = higher-timeframe analysis, work on 1H | |
| L-23 / L-28 | reaction = sharp rejection or consolidation in/around; precise zones, no bloat / bunching / floating / missing | grading |

## 1. The seven laws + golden-standard construction rules (GS; from his 38 winning trades)
| id | ref | requirement | function | state |
|---|---|---|---|---|
| LAW1 | GS:9-28 | zones from 15m+30m+1H+4H(+8H) simultaneously; widths 5m 3-12 / 15m 5-22 / 30m 10-35 / 1H 10-50 / 4H 20-120 / 8H 30-200 pips | zone map per TF | NB |
| LAW2 | GS:30-45, 250-270 | shape -> max entry distance from spot: SS 30, R 50, RS 80, BS 100, RWL 100, WL 200 (default 60); setups only at zones the day's shape reaches | e3 reachability | NB |
| LAW3 | GS:47-61 | entry never at a 4H edge: 15m edge (scalp, 0-2 pips inside), 30m edge (swing), 1H edge (HTF swing, nearest key level); 4H = bias + TP only; reinforcement at FAR edge | e3 entry | NB |
| LAW4 | GS:63-79, 272-300 | SL outside the nearest liquidity shield; 5-15 pips (median 12; never > 25 standard; 25-50 only behind 4H/8H shield); no LSZ between entry and SL -> widen to next LSZ or reject | e3 sl | NB |
| LAW5 | GS:81-97 | Fib anchored to entry zone ceiling/floor: entries .382/.5/.618(.786); rocket 1 = 1.382; rocket 2 = 1.618; 2.382 TP / rocket-3 trigger; 2.786 extended | e3 fib |PB (built: Fib levels of a supply / demand zone as its internal steps, e3_trades._env; first rocket on the retest-leg grid 0.786 with SL 0.618, D-83; PDF TP buffer 1.5. NOT built: the spiderweb as entry construction - PDF re-read first-hand 2026-11-27, a mechanical anchoring of the Monday scalp web was probed and rejected, journal) |
| LAW6 | GS:99-139, 325-358 | ladder = reinforcements on an existing primary at a BoM zone; rockets at next MoM zones 20-30 pips apart snapped to Fib 1.382 / 1.618; SL cascade (R1 -> primary BE; R2 -> R1 BE); TP at opposing BoM / liquidity shield | e3 rockets |PB (built: reinforcements on a BS primary at intermediate rungs 20+ pips apart, own ladder stop, parent TP, premarket bracket, cancelled with the parent; NOT built: SL cascade to breakeven, trip-wire, rocket types) |
| LAW7 | GS:141-154 | build ALL zones from ALL TFs before any setup; per day's shape the expected travel range; no reachable zone -> "no actionable setup" | pipeline order | NB |
| GS-C1 | GS:222-248 | per 4H zone: 15m zones within, 30m within/near, 1H overlapping; LTF zone edge = entry, LTF opposite edge + buffer = SL, 4H opposing zone = TP, Fib from LTF range; no LTF zone within 30 pips -> 4H edge flagged "HTF-only" | e3 construct | NB |
| GS-C4 | GS:302-323 | depleted zone allowed as BREAKOUT entry if a fresh 15m/30m zone sits at the same price | e3 | NB |
| GS-TAX | GS:506-535 | labels: BoM/MoM (Unmitigated / Mitigated Nx), MoM (Shielded), LSZ / Liquidity Shield (Bear/Bull Conquered, Contesting = ZoC), "15m Refined 30m" etc.; states -> entry validity (UM, 1x = ENTRY-PRIMARY; 2x conditional; 3x+ TP only; Shielded higher priority) | zone states | NB |
| GS-CND | GS:537-549 | entry confirmation candle patterns at zone touch (engulfing, pin bar, inside bar, breakout candle, piercing wick) | e3 | NB |
| GS-TPH | GS:553-566 | TP zone timeframe >= entry zone timeframe; a 15m entry never targets a 15m zone | e3 tp | NB |
| GS-SIZ | GS:570-582 | ladder sizing 50/30/20 (or thirds) shown | e3 | NB |
| GS-SES | GS:586-596 | London Open scalps; London/NY overlap breakouts; NY Mid HTF swings; NY Open reinforcement triggers | e3 session | NB |
| GS-REF | GS:600-618 | zones of adjacent TFs overlapping within 5 pips = ONE "Refined" zone: width = the narrower, status = the fresher, label "15m Refined 30m" | zone map | NB |
| GS-DXY | GS:622-634 | DXY: zone width 5-20 pips, SL 7-15, master direction | | NB |
| GS-WAR | GS:437-503 | ZoC (3+ TF overlap): holds -> back to SS; fails -> BS to the opposing BoM, WL there, then R | e2 | NB |
| GS-V4 | GS:703-730 | telescope 4H -> 1H -> 30m -> 15m with merge; ATR(14) Wilder; path-based setup: spot -> entry LQZ -> next zone (SL) -> demand+liquidity (TP); 3-entry staggered with forward spreads (EUR 1 pip, GBP 2, DXY 0.02); DXY cascade hard filter; trade chaining | pipeline | NB |

## 2. Engine 1 (P533 Part III-V; P452 where "unchanged")
| id | ref | requirement (short) | function | state |
|---|---|---|---|---|
| E1-V1 | R-30, R-04 | supply/demand + liquidity zones = the sealed V1's output; the tool takes them as data without editing V1 | e1_v1.harvest / harvest_all (sealed V1 + last 400 closed bars -> station /model -> boxes by colour); MEASURED: 15/16 of his golden rungs, his entries on 15m/30m order blocks | B |
| E1-MTF | GS LAW1, GS-REF, L-40 | per-timeframe zone sets 4H / 1H / 30m / 15m, nested + refined | e1_sd.scan / zone_map (11 of his 12 golden-week boxes exact on three pairs) | B |
| E1-A | P533:808-921 | Protocol A: investingLive expiries, temporal boundary, tiers >= 1.5B / 850M-1.499B / excluded | sidecar/, e1_pillars.tier | B |
| E1-P1 | P533:967-1064 | pivots classic / fib / camarilla, weekly + last 3 days, verification checks | e1_pillars.pivots, pillar1 | B |
| E1-P2 | P533:1065-1091 | MA grid EMA/SMA 9,10,20,50,100,200; clusters; recapture | e1_ip.levels Pillar 2 (EMA + SMA on 1H / 4H / D1 / W1, clusters, recapture of EMA 50 / 100 / 200) | B |
| E1-P3 | P533:1092-1144 | component-pair strike conversion | k_factor, strike_to_dxy | PB (only EUR/USD strikes) |
| E1-BM | P533:1145-1153 | EVERY IP zone classified BoM (origin of the impulse) / MoM (mid-move); BoM = ENTRY-PRIMARY; MoM = TP-TARGET / exceptions; 4H MoM = ONE-AND-DONE | e1_ip.mechanics (BoM / MoM per IP zone, Engine 3 status), e1_sd (BoM / MoM per candle zone) | B |
| E1-RC | P533:1154-1161 | reaction counter per IP zone: 0 virgin / 1-2 active / 3+ depleted; priority rule: a zone with juice between price and the BoM is liquidated first | e1_ip.mechanics (visits, strong reactions, counter); e2_chain.counter / branch read it | B (priority rule = 6.4.2 branch in E2) |
| E1-P4 | P533:1169-1204 | analyst commentary | e1_ip.levels Pillar 4 + score() Analyst dimension | PB (D-104: sidecar analyst_levels of the pair, 1 point per named level; DXY lists empty = NO DATA; no Tier-1 sources, consensus flag not built) |
| E1-S0 | P533:1213-1245 | 90-day scan: 0b/0c swing lows/highs (wick >= 0.15, close position), 0d D1 order blocks (base before >= 1.0 / >= 5 days), 0e confluent floor / ceiling | e1_ip.levels (0b / 0c swings incl. the last days D-13, 0d D1 order blocks, 0e confluent flag) | B |
| E1-S045 | P533:1246-1283 | LSZ at every swing extreme [low, low+0.05] / [high-0.05, high]; hidden liquidity in gaps >= 0.15 (4H swings / 4H BoM); confluent sweep + BoM flag; ACTIVE SL TRIGGER within 0.30 | e1_ip.levels lsz (0.45a / b, daily extremes of the last 5 days, swept flag, 0.45e ACTIVE SL TRIGGER) | PB (0.45c hidden liquidity in gaps missing: "gap with NO structural level" needs a reading; 0.45d confluent sweep + 4H BoM flag built, labelled) |
| E1-S045a | P533:1284-1287 | LSZ extended 0.05-0.10 beyond the extreme | e1_pine (dotted reach box + label), e2_chain._sweep_bound reach (D-64) | B |
| E1-S05 | P533:1288-1311 | repeated extreme magnets within 0.05 on 2+ dates; role reversal; institutional magnet | e1_ip.levels magnets (repeated 2x / 3x, role reversal, institutional magnet inside a D1 order block) | B |
| E1-S06 | P533:1312-1340 | intra-zone key levels for every MODERATE+ zone: 1H S/D of the prior 1-2 weeks inside it, fib .382/.618 of the zone's own range, prior daily closes inside, round numbers inside; tags precision floor (bottom 40%) / ceiling (top 40%) / mid-anchor; Structural 0.5 | e1_ip.intra_zone | B (not yet drawn) |
| E1-S0f | P533:1341-1398, P452:637-745; L-37, L-38 | 4H S/D = the single candle before the strong move [low, high]; verification trail; BoM/MoM; mitigation soft/hard; noise rejection (4 rules) | e1_sd.scan (origin candle, base, mitigation soft/hard, broken, structure break, BoM/MoM over valid zones) | B |
| E1-S0g | P533:1399-1402, P452:749-765 | 1H zones only nested inside a 4H/D1 zone (precision) or as gap-fill; never standalone IP levels | e1_sd.zone_map (1H zones drawn as supply/demand boxes, never as IP levels; nested_in flag) | B (per L-40 and his charts 1H zones stand on their own as S/D boxes) |
| E1-S0h | P533:1403-1406, P452:767-781 | minor swings D1 AND 4H, wick >= 0.08, 40% close; Structural 0.5 | e1_ip.levels (minor swings on D1 and 4H) | B |
| E1-S15 | P533:1407-1410, P452:785-833 | anchors: prior daily closes / highs / lows (5 days), weekly close/high/low, HWC/LWC, MA recapture, structural extreme memory, scoring | e1_ip.levels (daily closes / highs / lows of 5 days, weekly close / high / low, session high / low to the anchor, recapture) | PB (HWC / LWC: source = forex.com research, optional -> ND; structural extreme memory beyond 90 days: ND) |
| E1-S55 | P533:1411-1423 | Key Support Band: core (candle bodies) vs spike (wicks = LSZ extension, half score) | | NB |
| E1-P6 | P533:1424-1429, P452:835-862 | fib retracements of prior week AND of the last significant D1/4H swing; round grid | e1_ip.levels Pillar 6 (fibs of the prior week and of the major 63-day swing, round grid) | B |
| E1-P7 | P533:1430-1435 | derivatives arena | | ND |
| E1-P8 | P533:1436-1454, P452:890-950 | EUR/USD strike -> DXY primary conversion, K audit, bands | strike_to_dxy | B |
| E1-P9 | P533:1455-1460, P452:954-1071 | zone types + ZFP = base + modifiers; regime dimension; measured move for ZFP > 45 | e1_ip.build typify (types, base ZFP, modifiers: momentum approach, regime change EMA200, structural extreme magnet; regime dimension); e2_chain.measured_move (Step 4) | PB (modifiers expiry timing = D-60 in E2 only, macro catalyst ND, cross-pair, volume, cascade missing; BREAKOUT RISK flag / BREAKOUT EXTENSION TARGET zone not drawn) |
| E1-SY | P533:1461-1495 | six dimensions 0-2 + structural-extreme bonus <= 2; degree table | score_level, degree | B |
| E1-AS | P533:1496-1506, P452:1116-1157; L-39 | collect all -> score -> clustering scan -> group -> degree = best level -> ZFP -> names | e1_ip.build (approved-render recipe: score, best-first assembly, mechanics, Pillar 9, names, rank) | PB (runs; golden-week deltas D1-D3 open, journal 2026-11-26) |
| E1-95 | P533:1507, P452:1159-1184 | gap scan >= 0.20, in-fill with 2+ signals | e1_ip.gap_scan (D-68); drawn + listed; E2 / E3 do not read in-fill levels yet | PB |
| E1-97 | P533:1509-1515, P452:1186-1215 | 4H overlay: POI Tier 1 / 2 / 3, hierarchy rule, ladder-step identification | in build | PB (Tier 3 "4H-only", ladder steps missing) |
| E1-DISC | P452:1220-1230 | Dynamic Discovery Protocol: pre-week discovery flags (gaps > 0.15, major round numbers, HWC / LWC not traded, EMA convergence, structural extremes); intra-week promotion | e1_ip.discovery, e1_pine.discovery_drawn | B (D-103; pre-week flags built and pixel-checked, ledger 91b; intra-week promotion NOT RUN: post-anchor candles) |
| E1-98 | P533:1516-1527 | synthesis re-verification (option strike >= 850M from R1 pair; score recompute; cross-reference) | | NB |
| E1-IV | P533:1540-1567 | Part IV: extraction / filtering, tactical calculations, volatility triggers, red-folder fences | | NB (not yet read) |
| E1-V | P533:1568-1724 | report sections + Engine 3 Status column + blind-execution protocol | e1_report | PB |
| E1-IX | P533:3257-3688 | multi-pair translation: each pair runs its own pipeline on its own prices; DXY = direction | e1_pine.run | PB (not yet read in full) |
| E1-X | P533 Part X + Appendix E | Pine v6 code generation protocol (the form of trident_v8.pine) | e1_pine.generate, plutus.table | PB (read first-hand 2026-11-27. Built: pair detection by ticker, xloc.bar_time everywhere, pressure-ladder colours, LSZ green, amber option lines + '... Option Strike Target', label.style_none, toggles incl. Info Table, 2 x 17 table D-94, limits 2000. Different BY RULING: one pair per script (goal prompt: one Pine per week / pair), S/D zones drawn (goal prompt 4b / L-39 against Principle 4), window = active week + one week left (R-36 against 10.4), sweep zones labelled (D-64, against 10.7 'NO LABELS on LSZ zones' - reviewer-driven, to re-decide), IP label carries tier / class / parts. Pinebox does not paint tables: ledger 88) |

## 3. Engine 2 (P533:1725-2057) — REBUILT 2026-11-26 in e1_tool/e2_chain.py (current_shape, _bounds, _target, _after_bs, build, pine); golden week DXY pixel-checked (ledger 55-56). Rows below: 61 / 62 / 64 / 641 / 642 / 65 / 66 / 69 / 610 / R03 = B; 63 / 67 / 68 / CP / 1D / TFM / PR / TRV / ZOC / AIR = partly (see file docstrings), to be completed and audited
| id | ref | requirement (short) | state |
|---|---|---|---|
| E2-61 | 1741-1769 | taxonomy SS / BS (PBS) / R (RS) / WL (RWL, PWL, PRWL) / WLS with IP-zone signatures | PB |
| E2-62 | 1770-1782 | classification matrix applied in priority order 1-6 (zone-anchored conditions) | NB |
| E2-63 | 1783-1799 | observed chains by frequency (SS->BS->R->WL highest) | NB |
| E2-64 | 1800-1818 | transition rules table | PB |
| E2-641 | 1819-1838 | ZFP-conditioned transitions (BS at Hard Wall -> RWL; 20-40 -> R; > 60 -> PBS; SS both < 30 -> SS; R > 1 session -> SS ...) | PB |
| E2-642 | 1839-1874; FA:541-572 | MoM-zone decision tree by reaction; reaction count selects the branch; BoM always reacts | NB |
| E2-65 | 1875-1886 | anchoring rules by shape (required E1 metrics) | NB |
| E2-66 | 1887-1918 | forward mapping steps 1-5: current shape, transition assessment, chain extension with audit trail (max 5, stop < 25%), alternative chain with decision zone, day decomposition; pair translation (same shapes, inverted direction) | PB |
| E2-67 | 1919-1930 | zero-tolerance rules 1-9 | NB |
| E2-68 | 1931-1945 | shape-to-zone quick reference (durations) | NB |
| E2-CP | 1946-1960 | consolidation phase detection -> valid setup types | NB |
| E2-1D | 1961-1964 | 4H MoM one-and-done: minor WL then BS/PBS through it | NB |
| E2-TFM | 1965-1975; FA:281-287 | timeframe element matching (4H->4H, 1H->1H, 15m -> at most 1H) | NB |
| E2-PR | 1976-1983 | pressure reading rules; 4H storyline tiebreaker | PB |
| E2-69 | 1984-2039 | output format incl. day-by-day decomposition (feeds E3) | PB |
| E2-610 | 2040-2057; FA:574-590 | trading speed rule; conservation of energy (after 2 strong piercing moves 1-2 days of consolidation) | PB |
| E2-TRV | GS LAW2 | expected travel per shape per day | NB |
| E2-ZOC | GS-WAR | ZoC holds / fails logic drives the chain | NB |
| E2-AIR | FA:169-209, 289-303; Fibonacci_Spiderwebs.pdf | Fibonacci spiderweb anchored to Earth points maps the trajectory | NB (PDF read 2026-11-26: rules + golden arithmetic in memory/08 last section; build = next step) |
| E2-R03 | R-03 | render: day BOXES first, then the LINE | NB (line only) |

## 4. Engine 3 (E3C; R-16) — REBUILT 2026-11-26 in e1_tool/e3_trades.py (chain along the E2 legs; TS-1 / F1-A / F1-C / F1-D entries, ladder-step stops, single TP, RRR floor with three attempts, BS reinforcement, position boxes); golden week DXY: his trades within 3 pips (ledger 57-58). Built: P0 (per shape), P2 (entry sources), P3, P42, P43, P44, P6 (chains), P9 (one reinforcement), R09. Not yet built: P1 confidence spill, P25, P41, P5, P7 (sessions as labels only), P8 labels, P10 (pairs run their own chain with the inverted DXY shapes), P11, P12, OUT, ZT, DIR, F
| id | ref | requirement (short) | state |
|---|---|---|---|
| E3-P0 | E3C:88-107 | setup universe per shape (12 shapes) | PB (built: SS both directions, BS swing + reinforcements, RWL / WL reversal, SS->BS transition entry D-51; not built: SS(DWL) inverse, WLS, R scalps, RS, PWL / PRWL) |
| E3-P1 | E3C:109-125 | WorkingDayMap {dayIdx, day, shape, direction, keyZoneId, keyZoneType, supplyZoneId, demandZoneId, deepDemandZoneId, dayOpenSpot, session, confidence}; conf < 65% -> shape spills to next day | PB (no WorkingDayMap object: the day's zones come from the E2 chain step; built: confidence < 65% spill-over D-70, deep-zone order through the consolidation D-76; not built: per-day supply / demand / deep zone ids from dayOpenSpot) |
| E3-P2 | E3C:127-173 | direction-appropriate anchor; entry sources ORDER_BLOCK / LQZ only (IP = confluence + SL/TP rungs, never entries); 4 categories; freshness gate (battle index > 2 skipped; pierced = VIOLATED); lifecycle; BoS + flip + retest | PB (built: direction-appropriate anchors, ORDER_BLOCK / LQZ entry sources incl. the sweep zone in front of a pressure zone D-69, categories, freshness mit >= 3, MoM reversal gate, ZONE_DEPLETED on a range bound with 3 reactions -> entry at the liquidity beyond it D-85; not built: BoS + flip + retest pattern, VIOLATED state inside the week, rule 6 'no entry at MoM unless ALL 4 exceptions' / VIRGIN_MOM_DEATH_ZONE as a gate - his own golden longs stand on '1H (Unmitigated) | MoM' zones, memory/08 last section) |
| E3-P25 | E3C:1148-1160 | 1-2-3 retest timing (0 = scalp only; 1 = scalp + confirmation; 2 = swing; 3+ = TP only); reinforcement order timing | PB (built: reinforcement order timing D-71; not built: 1-2-3 retest count gating of entries) |
| E3-P3 | E3C:175-230 | TS-1 sniper entry; F1-A OB-short lift 1 pip; F1-C internal LMV rung near edge; F1-D RWL inset 0.2; F1-E recovery shelf +1; Fib spiderweb 3 contexts, wormholes, key-level zones | PB (built: TS-1, F1-A, F1-C, F1-D, Mechanism A front D-62; not built: F1-E recovery shelf, Fib spiderweb contexts / wormholes) |
| E3-P41 | E3C:233-245 | 7-layer confluence stack | PB (layers 1, 3, 5, 7 as confidence terms; layers 2, 4, 6 not scored) |
| E3-P42 | E3C:247-292 | SL ladder-steps: 3 pips outside the far edge of the current step OR 1-2 pips inside the close edge of the next step; relevant zone by fuel state (LQZ SHIELD_FUEL / S/D PRESSURE_STRUCTURE / golden fallback 4-9.5 pips); confidence >= 0.6 tight; buffers EU 2 / GU 3 / DXY 5 idx; ceiling 36 | PB (built: ladder steps (a) / (b), ZR-6B switch by mirror confidence D-73, shield walk D-47, entry-zone back edge D-65, 15R re-anchor D-75, D17 ceiling 36, golden minimum 4, extended sweep range for sweep-zone anchors D-84 (P533 7.1 Rule 2.5, E3C:1027); not built: computeGoldenSL fallback, Law-7 buffers in refineSetup) |
| E3-P43 | E3C:294-352 | ONE TP at the opposing pressure (S/D + LQZ overlap -> midpoint; else near edge; strong zone -> near edge + 1-2 pips); Law-14 walk; no teleport past unmitigated zones; TP TF >= entry TF | PB (built: one TP, E2 zone first, midpoint / near edge / + 1 pip rules, Law 14 D-66 / D-74, reversal TP D-56, TP order 1.5 pips in front D-82, sweep-zone bound near edge D-86; not built: fresh-wall zfp <= 20 cap, TP timeframe law as a gate) |
| E3-P44 | E3C:354-386 | RRR primary / blended; floor 3.0, norm 4+, ceiling 15; 3-attempt refinement on the same anchors; per-anchor lock | PB (built: floor 3.0 / 2.5 consolidation week, ceiling 15, 3 entry x 3 TP attempts, hair-miss repair; the emission floor is met by the blended RRR of the 3-entry staggered position before the entry is moved (D-100); per-anchor lock state machine not built) |
| E3-P5 | E3C:388-424 | confidence sum + three-band SL-distance, cascade bonus; quality classes | PB (built: confidence sum with SL bands, cascade, GU long, proximity, momentum; inclusion 65; not built: VLM base, GOD_TIER class) |
| E3-P6 | E3C:426-471 | setup matrix; trade-flow chains (TP of N = entry of N+1, max depth 3); conflicts; one mirror per anchor per day | PB (built: Law 27 chains depth 3, duplicates 5 pips, conflicts 15 pips; not built: setup matrix, rule 11 max 3 per category) |
| E3-P7 | E3C:473-596 | 12-step day assignment; session selection + liquidityScore filter; anchor hit window | PB (day = the E2 step's day, session by category; not built: 12-step assignDay, liquidityScore session filter, anchor hit window, red-folder deferral ND) |
| E3-P8 | E3C:598-617 | blind-execution labels BE1-BE12 | PB (D-95 report in the Pine's trailing comments: BE1-BE5, BE8-BE11 present; BE6 per-anchor WHEN = the setup's day + session only; BE12 = D-70 spill-over; red-folder catalysts NO DATA) |
| E3-P9 | E3C:619-721, 1056-1080 | reinforcement: ladder (50/30/20, own SLs, cascade), Fib rockets, overlap risk rule, TP management, 4H BoM cascade, three rocket types, stop-limit trip-wire mechanics, intra-zone staggered 3 entries | PB (built: cross-zone ladder rockets 20+ pips apart with own ladder stop, overlap rule, parent TP, brackets D-71, conditional drawing; Mechanism A front; not built: Fib rocket levels, trip-wire trigger zone, SL cascade to breakeven, middle / back staggered fills) |
| E3-P10 | E3C:723-800 | cascade mirror DXY -> EU (inverse) -> GU (kept): zone CLASS matched on the pair's own map; emergent pair trades; 35% divergence flag | PB (the pair's setups come from the DXY chain translated onto the pair's own zones; 35% divergence flag computed against the pair's own chain and reported (plutus.divergence, flag only: 0.00 on all eight pair maps of the four weeks); not built: mirror lane per DXY setup, emergent lane) |
| E3-P11 | E3C:802-816 | master trade setup E + FLR | NB |
| E3-P12 | E3C:818-879 | 3D audit; floor invariants (SL envelope 9.5 pips, every discard has a reason); CS-1 day-native guard; narrative gate | PB (built: reason code on every discard, narrative gate per E2 day D-72, RRR floor; not built: 3D audit P / C / T, CS-1 day-native guard, SL envelope invariant) |
| E3-OUT | E3C:927-997 | output format; weekly execution calendar; f(T) >= 8 setups per pair | PB (D-95: calendar, category sections, session notes, discards, stats, f(T) line reported met / NOT met; not built: confluence stack layers 1-7, 3D audit P / C / T tables, master setups) |
| E3-ZT | E3C:999-1016 | zero-tolerance rules 1-16 (Tier 1/2 POI; 6-check; BoM/MoM; sequential zone path; confidence >= 65; honest absence) | PB (rules 5, 7, 11, 13, 14 without code) |
| E3-DIR | E3C:1082-1095 | 6-check direction validation (4+ disagree -> reverse or reject) | PB (6-check runs in E2 for the breakout direction; not per setup) |
| E3-PAIR | E3C:1097-1104 | pair mechanics (buffers, forward spreads, special rules) | PB (built: forward spreads, EUR/USD NO_SHIELD, GU long bonus; Law-7 buffers defined, unused) |
| E3-F | E3C:1180-1669 | Appendix F data model: enums, interfaces, ZoneMapSnapshot, ShapePredictionSnapshot, WallMap | PB (F.2 WorkingDayMap / TradeSetup and F.4 ShapeDayZone read; the tool's dicts do not carry the model's field names) |
| E3-R09 | R-09 | render setups as position boxes | B (position boxes; rockets dashed + 'if parent') |

## 5. Fractal Architecture mechanics (FA) not already covered above
| id | ref | mechanic | state |
|---|---|---|---|
| FA-EARTH | FA:47-87 | setup anchored to liquidity; SL shielded by a liquid pressure zone; thin liquidity zones never entry or SL; thin zones inside a 4H pool count double | NB |
| FA-FIRE | FA:89-123 | BoM hottest / MoM cooling; 95% of NY swings start in the 2nd half of NY; NY rockets need >= 3 pip SL | NB |
| FA-WATER | FA:125-167 | price sweeps liquidity zone by zone in sequential order | NB |
| FA-ROCKET | FA:325-489 | trip-wire stop-limit: trigger zone 2-4 zones ahead, limit at the rocket entry zone, primary to BE; FLR / FR / LR buffers; Fib key levels | NB |
| FA-MOM | FA:517-539 | MoM = ladder steps for trend-aligned trades + TP targets only | PB |
| FA-PAIR | FA:592-650 | EU: price touches the overlap (no shield); GU: liquidity only respected, S/D pierced, shields; DXY: direction, zone-to-zone in London, breakout after 3pm | NB |

## 6. Order of work (anchor week Jul 6-10 2026 until S2 holds)
1. Still to read first-hand: E3C Appendix F; Fibonacci_Spiderwebs.pdf; P533 Part IV, IX, X; M1 execution contract (bundle 6118-6432); sealed V1 (what it draws); DESIGN_BLUEPRINT_v5.2 sections 2, 3, 9, 19.
2. Oracle: golden_week.json from his screenshots (task S2a).
3. E1 rows in this order: E1-V1 -> E1-MTF -> E1-S0f/BM/RC (true BoM/MoM, reactions) -> E1-S06 -> E1-AS (+ L-39) -> remaining PB rows -> render, compare with his chart.
4. E2 rows 61 -> 610 + TRV/ZOC/AIR, render boxes + line, compare with his day tags.
5. E3 rows P0 -> P12, render position boxes, compare with his six trades.

## 7. Changes of 2026-11-26 night (after compaction 8) - read with the rows above (states: B built, PB partial, NB not built)
| id | what changed | state |
|---|---|---|
| E1-S0 | Step 0b / 0c scan the last days and the D1 bar in progress with the neighbours that exist (D-26); 0d order blocks + 0e confluent flags exist in e1_ip.levels | B |
| E1-S045 | sweep zones also at the pre-anchor session high / low (D-25); 0.45e ACTIVE SL TRIGGER flag; 0.45c hidden gaps, 0.45d BoM confluence flag still missing | PB |
| E1-S15 | anchors: + session high / low to the anchor; HWC / LWC still missing | PB |
| E1-P9 | regime-change modifier only for zones standing against the new regime (P452:981-992); expiry-timing, macro, cross-pair, cascade modifiers and the measured move per zone still missing | PB |
| E1-95 | Step 9.5 gap scan is NOT in e1_ip.build (the old gap_scan lived in e1_zones.py, superseded) | NB |
| E1-V1 | V1 4H liquidity bands drawn (show_lq4) and used for the transition-day retest; 30m / 15m bands harvested, not yet used as steps | PB |
| E1-X | Pine: default view = the week's reach (e1_pine.reach, GS Law 2 / 7), far zones behind show_far | B |
| E2-64 / 641 / 642 | direction: failing bound (> 45) -> the MoM bound is the one pierced (6.4.2) -> 4H storyline; a breakout running at the anchor: BS -> 6.4.1 at the next zone -> SS -> second BS (6.3) | B |
| E2-65 | SS bounds: wall / pressure zone under 30% within the scalp reach -> graded 1H / 4H supply-demand zone -> nearest unswept sweep zone beyond spot (D-27) -> measured move | B |
| E2-66 | transition day: the retest reaches the opposing liquidity band (V1 1H rung / 4H band against the far bound, e2_chain._opposing_liquidity) | B |
| E2-CP | consolidation phase detection / "ZFP trend on the bounding zone" (expiry roll-off) decides WHEN the range breaks: not built - the plan always breaks on day 3-4 | NB |
| E3-P2 | first anchor: nearest 1H / 4H zone against the leg, else the E2 bound (R3 law) | B |
| E3-P3 | TS-1 at a sweep-zone bound (near edge); WL keeps the zone middle | B |
| E3-P42 | EUR/USD NO_SHIELD -> rule (a); the confidence switch ZR-6B (>= 0.6 tight / < 0.6 next rung) and rule (b) on 4H liquidity steps (facts in memory/08) not built | PB |
| E3-P43 | RWL TP = opposing liquidity near edge + 1 pip; 4H BoM target -> near edge + 1 pip, 4H MoM with LQZ inside -> zone midpoint (rule 4) | PB |
| E3-P6 | Law 27: BS entry = RWL TP (band = entry step); Phase 6.3 same-anchor-same-day dedup with log; opposite-direction conflict rule (needs Phase 5 confidence) not built | PB |
| E3-P10 | mirror lane: collision retry on the next liquidity step (deep shield); the full DXY -> EU -> GU re-anchoring of every DXY setup is still approximated by running the pair's own chain on the inverted DXY shapes | PB |
| E3-P5 / P7 / P8 / P9 (staggered entries, rockets) / P11 / P12 / OUT / ZT / F | not built; Phases 5-7 and 10 read first-hand this step, 8 / 9 / 11 / 12 / F still unread | NB |

## 8. Changes of 2026-11-26 (Engine 2 v2, Engine 3 v2 and the fixes after them; decisions D-34..D-56) - states: B built, PB partial, NB not built
| id | what changed | state |
|---|---|---|
| E2-62 | Step 1 on 1H sessions with the matrix rows in order and their ZFP conditions (D-40) | B |
| E2-64 / 641 / 642 | chain extended step by step: per-bound branch by the Zone Reaction Counter, direction by the 6-check + pressure reading + 4H storyline, timing by the canon minima + 1 day (D-34..D-41) | B |
| E2-TGT | breakout target = first BoM / strong object beyond the failing bound; weak (30%+) MoM pressure zones and standalone MoM candle zones are passed (D-49, D-50; P452:2082) | B |
| E2-WL | the surge ends in a whiplash when unswept stops rest against the target (P452:968; 6.4) | B |
| E2-ALT | alternative chain built and drawn dotted; its Engine 3 setups wait for the Decision Zone trigger | PB |
| E2-CP | consolidation phase Early / Mid / Late -> valid setup types (E3C 8.23) | NB |
| E2-PAIR | pairs = the DXY shapes inverted on the pair's own zones (P533 6.6 v5.0.0 addition) | B |
| E3-P0 | setup universe: SS scalps both directions, BS swing + rockets, RWL reversal, SS->BS Transition Entry (D-51); scalp-stack / swing-stack compliance gate | PB |
| E3-P1 / P7 | WorkingDayMap (one supply / demand / deep-demand zone per day) and the 12-step day assignment | NB |
| E3-P2 | candidates per E2 step and zone incl. zones straddling a bound (D-55); FRESHNESS (3+ tests), MOM_REVERSAL, narrative gate on misaligned setups only (D-53); POI tier rule 1, 1-2-3 retest timing | PB |
| E3-P3 | TS-1, F1-A, F1-C, F1-D + hair-miss repair; order blocks at a pressure zone as entry sources (D-46); F1-E shelf, Fibonacci contexts | PB |
| E3-P42 | stop = ladder steps: rule (b) on shields walked nearest first (D-43, D-47), rule (a) fallback, EUR/USD NO_SHIELD rule (a); the ZR-6B confidence switch and the fuel-state relevant zone | PB |
| E3-P43 | TP: E2 zone first (IP under 30%, candle-zone bound D-48, liquidity band D-45), 4H BoM near edge + 1, LQZ midpoint, reversal TP = first rung 30+ pips (D-56); Refined Law 14, TP timeframe law | PB |
| E3-P44 | RRR 3.0-15.0, consolidation week 2.5 (A-47), three entry x three TP attempts | B |
| E3-P5 | confidence with every E3C:392-414 term but the VLM bonus (D-42, D-52); inclusion >= 65 | B |
| E3-P6 | duplicates 5 pips, conflicts 15 pips, chains depth 3 (Law 27), rule 11 (max 3 per category) not applied (journal) | PB |
| E3-P9 | rockets: 20+ pips beyond the primary, ladder-step stop, premarket timing, cancelled with the parent (D-54); Mechanism A staggered entries, Fib 1.382 / 1.618 placement, trip-wire | PB |
| E3-P10 | cascade mirror DXY -> EU -> GU as its own lane | NB |
| E3-P12 | reason code on every discard; narrative gate; CS-1 day-native guard, floor invariants pass | PB |
| OUT | one command -> one Pine (plutus.py); 1H frames via tools/e1render; 15m / 30m frames of past weeks via the Backtest tab (ledger 75b) | B |
