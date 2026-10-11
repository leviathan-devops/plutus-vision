#!/usr/bin/env python3
"""Build the PLUTUS knowledge graph (canon + findings + governance) and decision/context graph.

Output (committed, stdlib-readable JSON; resume with `python3 context_management/graph/resume.py`):
  context_management/graph/plutus_knowledge_graph.json   canon, governance, artifacts, findings, open questions
  context_management/graph/plutus_decision_graph.json    decisions + evidence (Semantica ContextGraph.record_decision)

Rebuild:  pip install semantica && python3 context_management/graph/build_graph.py
Every node carries `ref` = where in the canon/repo the claim lives, so nothing here is a substitute for the source.
"""
import json
import pathlib
from semantica.context import ContextGraph

OUT = pathlib.Path(__file__).parent
CANON = "canon/Toolset/"
FRAC = CANON + "Trident_Fractal_Architecture_FirstPrinciples_v2.3.md"
P533 = CANON + "Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md"
E3C = CANON + "TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md"
PY8 = CANON + "trident_engine3_v8.py"

kg = ContextGraph(advanced_analytics=False)
NODES, EDGES = [], []


def n(i, t, desc, ref="", **p):
    NODES.append(i)
    kg.add_node(i, t, content=desc, ref=ref, **p)


def e(a, b, t="related_to", **p):
    EDGES.append((a, b, t))
    kg.add_edge(a, b, t, **p)


# ============================================================ GOVERNANCE (highest priority — read first)
n("MISSION", "mission",
  "Build the PLUTUS VISION Pine indicator: dynamically renders Engine1 zones + Engine2 shape-chain forecast + Engine3 trade setups on a TradingView chart, "
  "temporally scoped to the most recent bar (works in Bar Replay). Acceptance: 12 random weeks of DXY-basket FX pairs, rewind to Monday London open, replay 10x to Friday close, "
  "compare indicator's E2/E3 visuals with what actually happened; must be >=90-95% accurate. Anything labelled Trident is to be renamed Plutus.",
  "operator brief 2026-10-11")
n("PHASE", "state",
  "FOUNDATION/LEARNING phase. DO NOT START INDICATOR WORK until the operator explicitly gives permission and the handover. Current job: become a Plutus-canon subject-matter expert "
  "via real-chart exercises, keep graphs current, survive compaction.", "operator brief 2026-10-11", priority="critical")
n("FROZEN_E1E2", "constraint",
  "Engine1 and Engine2 of the ORIGINAL v5.3.3 are live-validated (A+ / ~95%). FORBIDDEN to change, disagree, or 'improve' them. Engine3 of the original was broken; "
  "use the CORRECTED E3 spec instead. Operator: obey, do not tell him what is/isn't possible, solve obstacles yourself, don't report problems without having tried to solve them.",
  "operator brief", priority="critical")
n("OP_STYLE", "constraint",
  "Operator is a systems engineer wanting hands-free full-stack execution. Zero tolerance for theatre, slop, 'it works' without evidence, unasked advice. "
  "He has burned 5 months on agents that did not follow instructions. Report outcomes faithfully; solve problems before surfacing them; one honest line on a real blocker.",
  "user preferences + brief")
n("OP_RULINGS", "constraint",
  "Verbatim rulings (DECISION_CHAIN.md): 'no reinventing or customizing', 'Assemble production grade components > build from scratch', 'if i cannot see it - its not real', "
  "'Take the simplest path, don't overthink or over engineer', 'indicators are not interactable, they just render', vision-in-the-loop verification = the agent LOOKS at frames against a written expectation.",
  "context_management/DECISION_CHAIN.md")
n("ANTI_THEATRE", "constraint",
  "Root failure pattern in this repo (FAILURE_LOG F-08..F-17, THEATRICALITY_LOG): a verification SUBSTITUTE (gate line, parity table, 4B VLM judge, recording nobody watched) stood in for verification. "
  "Countermeasure: write expectation BEFORE the render; LOOK at the image yourself; name deltas; parity != correctness; probe the target object not the input; assert served file == source file.",
  "FAILURE_LOG.md F-17; THEATRICALITY_LOG.md")
n("ACCURACY_MECH", "constraint",
  "F-17: 'is it accurate / are zones correct' had NO mechanism. Required: per-drawing semantic read: name a drawing on a named bar -> state its CLAIM -> look at the chart -> verdict + specific delta -> repeat across engines/TFs.",
  "FAILURE_LOG.md F-17")
n("TEMPORAL", "constraint",
  "Temporal boundary: only bars <= analysis point exist (Monday London open ~02:00 ET = 06:00Z in EDT). Forecast for the rest of that week must use nothing later. Bar Replay at any past date must reproduce the same rendering.",
  P533 + " Part I; operator brief")
e("MISSION", "PHASE", "gated_by"); e("FROZEN_E1E2", "MISSION", "constrains"); e("ANTI_THEATRE", "MISSION", "constrains")
e("ACCURACY_MECH", "MISSION", "defines_acceptance_of"); e("TEMPORAL", "MISSION", "constrains"); e("OP_RULINGS", "MISSION", "constrains"); e("OP_STYLE", "MISSION", "constrains")

# ============================================================ FRACTAL ARCHITECTURE — four elements (density axis)
n("EARTH", "element", "LIQUIDITY. LSZ (green sweep zones) = standard Earth; IP zones = HEAVY Earth. Foundation everything anchors to. SL must be shielded by liquidity; thin zones never entry/SL; "
  "rocket SL always 1 full pip outside back edge; thin zones inside a 4H pool count double. Infrastructure: stop-limit mechanics, capital protection, time anchors.", FRAC + " §2.1")
n("FIRE", "element", "SUPPLY & DEMAND (institutional firepower). BoM = hottest Fire (origin), MoM = cooling continuation Fire. Needs Earth as fuel (intrinsically linked). Fire cannot be sustained: "
  "after 2 strong piercing swings expect 1-2 days HTF consolidation. Ignition events: BS, WL, Recovery Surge.", FRAC + " §2.2")
n("WATER", "element", "MACRO SHAPES (BS, WL, R, SS, ...). The wave forms energy materialises into; shape chain = wave prediction; gives structure to Fire. Consolidation = calm pool, SS = ripples, BS = tidal wave. "
  "Engine2 is primarily Water.", FRAC + " §2.3")
n("AIR", "element", "FIBONACCI. No intrinsic density; becomes a SPIDERWEB only when anchored to Earth points (candlewick, swing H/L, zone edges): 'Poorly anchored spiderwebs get blown away and don't exist'. "
  "Air PIERCES FIRE (4H BoM S/D), not Earth; dual nature with Fire: fans it (accelerate) or blows it out (reverse). Self-referential wormholes 0.382->1.382, 0.618->1.618.", FRAC + " §2.4")
n("CYCLE", "concept", "Elemental cycle Earth -> Fire -> Water -> Air -> Earth: liquidity forms; S/D ignites at Earth anchor; energy takes a wave shape; Fib maps the trajectory; "
  "Fib-confirmed levels become new liquidity. Same energy at four states.", FRAC + " §4.1")
for a, b in (("EARTH", "FIRE"), ("FIRE", "WATER"), ("WATER", "AIR"), ("AIR", "EARTH")):
    e(a, b, "flows_into")
e("EARTH", "FIRE", "intrinsically_linked_with")
n("DENSITY_VS_ATTACK", "concept", "TWO AXES: density = what a mechanic IS (Earth/Fire/Water/Air); attack = how a trade ENGAGES (FR = Air tool in Fire-style attack; LR = Earth tool in Water-style attack; "
  "FLR = Air+Earth in Earth-heavy attack). Do not conflate.", FRAC + " §3")
n("TF_DENSITY", "law", "4H->4H: each timeframe's liquidity is its own element/density. 4H pierces 1H/30m but stops at another 4H; 1H and 4H interchangeable (4H dominant); never more than 2 TF dimensions up.", FRAC + " §4.4")
n("CONSERVATION", "law", "Conservation of energy: after 2 strong piercing swing moves expect 1-2 full days of HTF consolidation. WL -> RWL -> Swing Scalps -> BS/WLS/PBS is the recovery cycle. "
  "'Today's move often ends up being tomorrow's.' Assume price moves at 30-50% of the speed you think (Trading Speed Rule, +1 day).", FRAC + " §9; " + P533 + " §6.10")
n("MOM_LADDER_ONLY", "law", "MoM zones are LADDER STEPS ONLY: never reversal entries on MoM, EVER; valid as trend-aligned ladder fuel and as TP for the opposing direction. BoM zones = entry candidates (100% reaction if unmitigated).", FRAC + " §7")
n("SEQ_SWEEP", "law", "Price ALWAYS sweeps liquidity zone by zone in sequential order, never skipping; Law-14 refined: no teleport past UNMITIGATED zones, may pass mitigated ones during BS momentum.", P533 + " §2.0; " + E3C + " §8.3")
n("RECURRENCE", "law", "Zone pressure lifecycle: VIRGIN -> ACTIVE-1 (~80% react) -> ACTIVE-2 (~50%) -> DEPLETED (3+; TP only, 'zones usually fail on the THIRD mitigation') -> FORTRESS (4+ strong, Fire->Earth phase change) -> BROKEN. "
  "4H MoM is one-and-done (minor reaction then pierce).", E3C + " §8.1")
for x in ("TF_DENSITY", "CONSERVATION", "MOM_LADDER_ONLY", "SEQ_SWEEP", "RECURRENCE"):
    e(x, "FROZEN_E1E2" if x in ("CONSERVATION", "RECURRENCE") else "EARTH", "law_of")

# ============================================================ THE THREE ENGINES
n("E1", "engine", "ENGINE 1 = WHERE ARE THE WALLS. Maps Earth (IP + LSZ) and Fire (BoM/MoM S/D). 9-pillar 6-dimension confluence (0-14) -> pressure degree (EXTREME 12-14 <10% ZFP ... MINIMAL <60%+), ZFP, POI tiers, "
  "BoM/MoM, reaction counter, intra-zone key levels (Step 0.6), LSZ scan (Step 0.45), 4H singular-candle zones (Step 0f). Confirmed ~95%. FROZEN.", P533 + " Part III; Part IV")
n("E2", "engine", "ENGINE 2 = WHAT PATH WILL ENERGY TAKE. Macro shape chain (1H primary, 4H validation) + ZFP-conditioned transitions + consolidation phase + day-by-day decomposition (Mon-Fri) + alternative chain. "
  "Max chain length 5; stop if cumulative confidence <25%. Confirmed ~95%. FROZEN.", P533 + " Part VI")
n("E3", "engine", "ENGINE 3 = WHERE DO I SURF. Corrected spec = 12-phase pipeline (E2 designates, E3 obeys; R3 law): universe -> day bridge -> zone selection -> entry -> SL/TP/RRR -> confidence -> multi-setup -> day/session labels -> "
  "blind-execution labels -> reinforcement -> cascade mirror -> avatar state -> 3D audit. UNTESTED live; will be validated by the finished indicator.", E3C)
e("E1", "E2", "feeds"); e("E2", "E3", "feeds"); e("EARTH", "E1", "mapped_by"); e("FIRE", "E1", "mapped_by"); e("WATER", "E2", "mapped_by"); e("AIR", "E2", "mapped_by"); e("AIR", "E3", "mapped_by"); e("EARTH", "E3", "anchors")
e("FROZEN_E1E2", "E1", "protects"); e("FROZEN_E1E2", "E2", "protects")
n("E1_PILLARS", "concept", "9 pillars: P1 multi-TF pivots (classic/fib/camarilla weekly+3 daily), P2 MA confluence, P3 option-strike conversion, P4 analyst commentary, P5 structural extremes + LSZ + 4H S/D + intra-zone, "
  "P6 fib/round grid, P7 derivatives arena, P8 EURUSD-strike->DXY, P9 regime/ZFP/measured move. Dimensions: technical, options, analyst, structural, psychological, regime (+structural-extreme bonus up to +2).", P533 + " Part III")
n("E1_NEEDS_NONOHLC", "finding", "KEY ARCHITECTURE FACT: Pillars 3/4/7/8 need FX option expiries (10am NY cut, >=$1.5B critical / $850M-1.499B significant) and analyst commentary - NOT derivable from OHLC. "
  "A bar-replay Pine indicator can only compute the OHLC-derivable half dynamically (S/D origin candles, swings/LSZ, pivots, MAs, round numbers, touch-density rungs). Option/analyst dimensions need an input channel or are absent.",
  "derived 2026-10-11 from P533 Part III + exercises", confidence="high")
e("E1_PILLARS", "E1", "part_of"); e("E1_NEEDS_NONOHLC", "E1_PILLARS", "qualifies")
n("ZFP_RULES", "rule", "ZFP-conditioned transitions: BS->target ZFP<20% (hard wall) => RWL (NOT R/PBS); 20-40% => R; >60% => PBS; >80% => strong PBS. SS with bounding ZFP>45% => BS; both <30% => SS continues; "
  "WLS => BS (very high); R persisting >1 session => reclassify SS; WL with opposite momentum => RWL else SS.", P533 + " §6.4.1")
n("MOM_TREE", "rule", "MoM decision tree: sharp whiplash instantly => pierced, BS/WL opposite; minor reaction+retest, zone holds => long consolidation (SS 2-4 days); zone breaks but price returns => short consolidation SS->BS/WL; "
  "no pierce => slow consolidation then retest opposing liquidity then pierce to BoM liquidity. BoM zones always react.", P533 + " §6.4.2")
e("ZFP_RULES", "E2", "part_of"); e("MOM_TREE", "E2", "part_of")

# ---- shapes
SHAPES = {
    "SS": "Swing Scalps (NOT 'sideways squeeze'): range between ceiling/floor IP zones, both ZFP<30%; 2-5 sessions; London scalp session; both directions valid; Double-Whiplash subtype.",
    "BS": "Breakout Surge: decisive break of a zone with ZFP>45%; 1-3 sessions toward next zone/structural extreme; NY swing session.",
    "PBS": "Piercing BS: pierces multiple intermediate zones (failing zone ZFP>70%).",
    "R": "Recovery: transitional stabilisation/retrace after BS or WL; <1 session else reclassify SS. RS = Recovery Surge (sharp).",
    "WL": "Whiplash: spike-and-reject at an IP zone (rejection is the key). PWL = piercing variant.",
    "RWL": "Reverse Whiplash: WL opposite to preceding BS; most common follow-on after BS; at hard walls ZFP<20%. PRWL = strongest reversal.",
    "WLS": "Whiplash Storm: 3+ similar-pressure zones in 0.30-0.50 DXY band, violent oscillation 2-5 sessions; almost always resolves into BS."}
for k, v in SHAPES.items():
    n("SHAPE_" + k, "shape", v, P533 + " §6.1", element="WATER")
    e("SHAPE_" + k, "WATER", "is_form_of")
n("CHAINS", "rule", "Observed chain frequency: SS->BS->R->WL (default week), SS->BS, BS->R->RWL, BS->RWL->SS->BS, WL->RWL->SS->BS, R->RWL->SS->BS, BS->RWL->PBS, BS->R->PBS, SS->BS->SS->BS, WLS->BS->WLS, WLS->SS->PBS, PBS->R/SS->PRWL->SS.", P533 + " §6.3")
e("CHAINS", "E2", "part_of")
n("DAY_BRIDGE", "rule", "Day-level bridge: E2 day-by-day decomposition -> E3 DAY/SESSION/SHAPE/CATEGORY/ANCHOR-HIT labels on every setup; +1 day speed shift; SS->London, BS/WL->NY; 'blind-executable' (BE1-BE12).", P533 + " §8.0.2; " + E3C + " §8.6")
e("E2", "DAY_BRIDGE", "emits"); e("DAY_BRIDGE", "E3", "consumed_by")

# ---- E3 corrected
n("E3_R3", "law", "R3 LAW: E2 DESIGNATES, E3 OBEYS. Every anchor traces to an E1 zone id + E2 shape day. E3 never overrides E1/E2 or fabricates levels. Honest absence: no valid SL/TP/RRR => NO emission.", E3C + " §8.0")
n("E3_ENTRY", "rule", "Entry: sniper edge nearest approaching price (SHORT=supply bottom, LONG=demand top); IP zones are NEVER entries (only ORDER_BLOCK or LQZ sources); internal LMV rung near-edge when zone contains one; "
  "never anchor LONG at supply. 4-stage freshness gate (index>2 skipped; any pierce = VIOLATED).", E3C + " §8.1-8.2")
n("E3_SLTP", "rule", "SL: ladder-steps (3p outside back edge OR 1-2p inside next-rung close edge); relevant zone by pressure state; per-pair buffers EU2/GU3/AU3/DXY5; D17 36p ceiling; rocket SL 1 full pip outside back edge. "
  "TP: ONE TP per trade at opposing pressure; strong zone = near edge (+1-2p spread), weak = far edge; Law-14 TP>=1.2xSL. RRR floor 3.0 (norm 4+), refine up to 3 attempts before hard reject (D36).", E3C + " §8.3")
n("E3_ROCKETS", "rule", "Rockets = trip-wire stop-limit orders set in London premarket: FLR (Earth-heavy, 30m Fib trigger, thick buffer 2 thick/2-3 thin), FR (Fire precision, 15m Fib, 2 buffer), LR (Water precision, thin buffer, 20-30% fail ok). "
  "Fib: entry .618-.786, rocket1 1.382-1.786 (cleanest, ~90%), trigger 2.382-2.786, target 3.382-3.786. Max 3/trade (2 recommended), one pair at a time, never reinforce thin zones. Master Trade Setup = E + FLR = Avatar State (all 4 elements).", E3C + " §8.8; " + FRAC + " §5-6")
n("E3_CASCADE", "rule", "Cascade: DXY LONG -> EU SHORT (inverse) -> GU SHORT (kept). Mirror zone CLASS not literal price (80/20 doctrine). >=24 setups/week acceptable, no caps (D38). 35% divergence = flag only.", E3C + " §8.9")
n("E3_RULES", "rule", "BoM/MoM enforcement; 1-2-3 retest timing (no swing before 3rd retest, no scalp before 2nd); 30-min red-folder deferral; close ALL by NY close (Profit Taking Law); NY rockets need >=3p SL; "
  "Direction Validation 6-check (4H trend, BoM alignment, LSZ direction, zone failure cascade, macro shape, counter-trend); 4+ of 6 disagree => reverse.", E3C + " §8.14, §8.18")
for x in ("E3_R3", "E3_ENTRY", "E3_SLTP", "E3_ROCKETS", "E3_CASCADE", "E3_RULES"):
    e(x, "E3", "part_of")

# ---- pair profiles & sessions
n("PAIRS", "concept", "EU Fire-Earth (primary swing, NY focus, PA touches overlap directly, no shield); GU Earth-Water (primary scalp, London focus, liquidity is only thing respected, S/D gets pierced, shields); "
  "AU Earth-dominant 'molasses' (2-4 days/HTF move; chart first); DXY Air-Fire master compass (directional conviction only; never convert DXY prices to pair prices). Chart priority AU>GU>EU.", FRAC + " §10; " + P533 + " Part IX")
n("SESSIONS", "concept", "ET: Tokyo ~17-02 milk the cow; London 02-12 SCALP (SS); NY 12-17 SWING session; claim '95% of NY swings start in 2nd half of NY (after ~14:30 ET)'. Trading day = 17:00->17:00 ET.", P533 + " §2.2.1")
e("PAIRS", "E3", "specialises"); e("SESSIONS", "E3", "times")

# ============================================================ ARTIFACTS
n("A_CANON_DIR", "artifact", "Operator's canon toolset committed in-repo for compaction survival: Fractal Architecture v2.3, original 5.3.3 prompt (4216 lines), CORRECTED E3 spec (1685 lines), trident_engine3_v8.py, report validator, report template.", CANON)
n("A_REPO_INDICATOR", "artifact", "plutus-vision-v0.pine = merge of 4 LuxAlgo scripts (SMC, Sweeps, Voids, Buy/Sellside pools). GEOMETRY ONLY: no E2/E3, no ZFP/pressure/POI. sha 605bff82... Parity SMC 195/195, POOLS 25/25, SWEEPS 258/258. "
  "NOTE: trident_v8.pine (the operator's 'v8 indicator') is NOT in this container/repo; pine-station looks for /home/user/Original_Canon_Data/Pine Scripts/trident_v8.pine (absent). Await handover.", "plutus-vision-v0.pine; CURRENT_STATE.md")
n("A_RIG", "artifact", "Local Pine IDE rig: node pine-station :9741 (PineTS 0.10 engine), vil-rail :9754, pv-server :9851, Chrome CDP :9222; pv-load.mjs loads indicator, station POST /run returns drawings JSON. "
  "WORKS HEADLESS in this cloud container (no X): npm install in pine-ide/pine-station, start 3 services, headless Chromium at /opt/pw-browsers/chromium-1194/chrome-linux/chrome with --remote-debugging-port=9222, then bun scripts/pv-load.mjs <pine> EUR/USD 1H; screenshot via CDP Page.captureScreenshot.", "scripts/pv-ide.sh; context_management/CURRENT_STATE.md")
n("A_FIXTURE", "artifact", "fixtures/bars/2026-07-06.json = REAL TradingView history (tvDatafeed) DXY/EURUSD/GBPUSD x 15m/30m/1H/4H, cut at Mon 2026-07-06 06:00Z (pre-London). Future bars absent by design. "
  "Documented golden prints: DXY Mon high 101.145 / low 100.838; EU Mon low 1.14083, Tue low 1.14001; GU week low 1.33222.", "fixtures/bars/2026-07-06.json")
n("A_LAB", "artifact", "research/e12_lab: my OHLC-only learning harness (lab.py data/clock/plots, e1.py zone detector, e2.py shape labeler+forecaster). NOT product code; exploratory. Real data: PyPI `backtesting` EURUSD 1H Apr2017-Feb2018 (5000 bars) + the fixture.", "research/e12_lab/")
n("A_GRAPH", "artifact", "This graph. Rebuild with context_management/graph/build_graph.py (Semantica ContextGraph). Resume with resume.py (stdlib).", "context_management/graph/")
n("A_SEMANTICA", "artifact", "semantica-agi/semantica (pip semantica 0.7.0, py3.10-3.13): ContextGraph with record_decision, find_precedents, save_to_file/load_from_file. Used as the graph container. "
  "arsumbris/arsumbris = macOS-only Electron typed-knowledge IDE (alpha, no sandbox) - NOT installed; its pattern (typed markdown/yaml graph) informs repo file layout only.", "github.com/semantica-agi/semantica; github.com/arsumbris/arsumbris")

n("REPORT_PIPELINE", "concept",
  "UPSTREAM of everything: the weekly report pipeline = web/VLM data harvest (investinglive OTC option expiries image, Yahoo/TradingView/forex.com/yfinance, FRED, EIA, ForexFactory) -> E1 (9 pillars) -> E2 -> E3 -> ReportLab PDF "
  "(Leviathan_Report_Template_v2.0.py, 52 formatting rules) -> Trident_Report_Validator.py (HTML firewall: setup completeness, DAY/SESSION labels, forbidden phrases e.g. 'Sideways Squeeze', both directions on SS days, BoM/MoM labels, RRR) "
  "-> generated Pine v6 arrays (Part X: hardcoded zone arrays per week, xloc.bar_time, no bar_index, color.new fills, label.style_none, 2x17 table). The old v8 indicator = STATIC render of one week's report arrays; the new Plutus Vision must be DYNAMIC per bar.",
  P533 + " Part III/V/X; canon/Toolset validator+template")
e("REPORT_PIPELINE", "E1", "produced_data_for"); e("REPORT_PIPELINE", "A_REPO_INDICATOR", "contrasts_with")
n("PY_V8_ROLE", "artifact", "trident_engine3_v8.py = sniper-entry E3 reference: consumes PRE-BUILT zones(+key_levels), LSZ, option strikes, pivots, MAs, analyst levels, swings, round numbers, shape_chain (E1/E2 outputs) and emits setups + DXY cascade; "
  "confirms E3 is strictly downstream (R3 law). Keep for sniper entry/SL buffers; its TP1/TP1.5/TP2 and RRR floors (1.2-3.0) are SUPERSEDED by the corrected spec (ONE TP, floor 3.0).", PY8)
e("PY_V8_ROLE", "E3", "reference_for")
# ---- canon contradictions found while reading (implementation hazards; operator to rule, do not silently pick)
CONF = [
 ("CONF_REINFORCE_INSIDE_SL", "Original 5.3.3 8R.1/8R.3: 'AT LEAST 2 reinforcement entries must be inside the SL of the primary trade'. CORRECTED E3 8R.3: '>=2 reinforcements inside primary SL -> REJECT the additional ones (overlapping risk)'. Opposite semantics; possible transcription inversion. Corrected spec is authoritative unless operator says otherwise.",
  P533 + " 8R.1 step7, 8R.3; " + E3C + " 8R.3"),
 ("CONF_RETEST_COUNT", "1-2-3 retest: original 8.4.2: 1st retest = no entry/scalp only if BoM, 2nd = scalp, 3rd+ = swing valid (Rule 7: no swing before 3rd). CORRECTED 8.25 table: 0 virgin=scalp only, 1=scalp+confirm, 2=swing valid, 3+=TP only (off-by-one vs 'zones fail on the third'). Counting convention (touches vs retests) must be fixed before implementing.",
  P533 + " 8.4.2; " + E3C + " 8.25, 8.14 rule 7, 8.1 lifecycle"),
 ("CONF_TP_COUNT", "Original 5.3.3 + v8.py: TP1/TP1.5/TP2 and RRR floors 1.2-5x by quality. CORRECTED E3: ONE TP per trade, RRR floor 3.0 (consolidation weeks 2.5). Corrected wins (operator ruling 2026-07-31).", E3C + " 8.3 Phase 4.3-4.4, 8.20"),
 ("CONF_MIN24_VS_ABSENCE", "Corrected E3 8.13: f(T) acceptance = >=24 setups/week (8 DXY+8 EU+8 GU), LESS is REJECT; but 8.14 rule 16 'Honest Absence': no valid SL/TP/RRR => NO emission, win-rate depends on what the code REFUSES to emit. Tension between quota and refusal.", E3C + " 8.13 vs 8.14"),
 ("CONF_CAPS", "Original: max 3/category, 15 total, confidence>=65. Corrected: NO caps (D38), but MAX_MIRRORS_PER_ANCHOR_PER_DAY=1 and rule 11 still says 'max 3 per category per pair; total unlimited'.", E3C + " 8.5, 8.14 rule 11"),
 ("CONF_SESSION_NY", "Original: London 02-12 ET scalp-only, NY 12-17 ET swings, '95% of NY swings start 2nd half NY'; corrected: day->session defaults (Mon/Wed/Fri London, Tue/Thu London-NY overlap) and category->session (HTF swing = NY Mid). My data (X4) did not support the day-level timing claim.", P533 + " 2.2.1; " + E3C + " 8.6"),
]
for i, d, r in CONF:
    n(i, "canon_conflict", d, r, status="open")
    e(i, "E3", "hazard_for")
n("OQ_CONFLICTS", "open_question", "Operator must rule on CONF_* nodes (see --type canon_conflict) before the E3 renderer is implemented; until then follow the CORRECTED E3 spec literally and flag where a conflict is touched.", "", status="open")
e("OQ_CONFLICTS", "MISSION", "blocks_or_informs")

# ============================================================ ENVIRONMENT FACTS
n("ENV_NET", "finding", "Cloud container egress allowlist: reachable = GitHub/api.github.com, raw.githubusercontent, PyPI, npm. BLOCKED (403 CONNECT): Yahoo, Stooq, Dukascopy, TradingView, Alpha Vantage, TwelveData, Frankfurter, histdata, HuggingFace, Kaggle, Binance, jsDelivr. "
  "No live TradingView session exists (rig/RIG_STATUS.md: no auth cookies). Unlock: operator edits environment Network access (Allowed domains).", "tested 2026-10-11", confidence="high")
n("ENV_DATA", "finding", "Real FX data reachable: PyPI `backtesting` ships EURUSD 1H (UTC, 2017-04-19..2018-02-07, 5000 bars, ~39 usable weeks) + repo fixture (Jul 2026 DXY/EU/GU, pre-anchor only). No GBP/AUD/DXY history for blind-week tests yet.", "tested 2026-10-11", confidence="high")

# ============================================================ EMPIRICAL FINDINGS (my exercises; each carries n + caveat)
F = [
    ("FND_MOM_DECAY", "MoM S/D touch decay (EURUSD 2017-18, my definitions, n=206 touches): reaction rate 62% first touch -> 38% second -> 32% third; pierce 26% -> 58% -> 65%. Consistent with 'MoM one-and-done' and 'zones fail on the third'.", "supported", "n=80/55/31; my BoM/MoM + reaction (>=0.5 ADR away within 12 bars) are approximations"),
    ("FND_BOM_100", "BoM '100% reaction if unmitigated' NOT reproduced: first-touch BoM reaction 58% (n=12) under my definition (BoM = zone at origin of a >=2.5 ADR zigzag leg).", "unresolved", "tiny n; operator's BoM detection and 'reaction' threshold may differ; needs his definition"),
    ("FND_TRANS", "Shape transition frequencies from labelled actual days (n=195, EURUSD 2017-18): SS->SS 50%, BS->R 33%, BS->SS 31%, BS->RWL 17%, WL->RWL 25%, RWL->SS 38%, R->SS 54%, SS->BS 31%. Frequencies: SS 45%, BS 25%, WL 9%, R 9%, RWL 6%, PBS 6%. Qualitatively matches E2 transition table.", "supported", "my day labeler thresholds are mine"),
    ("FND_CONSERVE", "After two consecutive same-direction directional days the next day was RANGE in 6/10 cases (2 continuation, 2 other directional): mild support for conservation-of-energy rule.", "weak-support", "n=10"),
    ("FND_NY_TIMING", "Main directional impulse of directional days started: London 48%, NY-AM 30%, Tokyo 16%, NY 12-17ET 6% (n=81). Does NOT support '95% of NY swings start in 2nd half of NY' as a day-level claim. Operator's claim probably concerns specific swing entries/completions, not day-level impulse origin.", "unresolved", "need operator definition of 'NY swing'; 2017-18 era"),
    ("FND_E1_NULL", "OHLC-only reconstruction of E1 zones (pivot+MA+round+swing+S/D clusters) shows NO edge vs shifted-zone baselines on EURUSD 2017-18: daily-extreme-near-zone lift 0.96-1.07x; touch-conditional react 43% vs 44.7% baseline. "
     "Most likely cause: missing option/analyst/intra-zone dimensions + my crude clustering (zones too dense), NOT evidence against the live canon.", "supported-null", "n=350 extremes / 135 touches; DO NOT cite as evidence canon is wrong"),
    ("FND_FORECAST_V0", "Mechanical doctrine-v0 forecaster on 12 blind weeks (held out, not tuned): day-shape family match 55% vs 65% for 'always range'; direction 3/21. Failure causes: tiny nearest-zone ranges, zone state (depleted/virgin) ignored in ZFP, side selection weak.", "negative-result", "crude v0; do not reuse unmodified"),
    ("FND_RUNG_DENSITY", "Golden entry levels for Jul-2026 EU (1.14083, 1.14001, 1.14020, 1.14010, 1.13935) rank at the 86th-97th percentile of 1H wick-tip touch density over the prior 10 days (1.1403 is the #2 peak; 1.13935 the 97th pct). "
     "Supports: operator 'internal LQZ rungs' = dense touch clusters, deterministic and Pine-computable.", "supported", "one week, five levels; window sensitive (5d weaker)"),
    ("FND_WIDE_CLUSTER", "My coarse E1 cluster (55 pips) CONTAINS all golden EU levels but cannot pinpoint them: precision requires the intra-zone key-level step (Step 0.6 / F1-C internal rung).", "supported", "one week"),
    ("FND_INDICATOR_EU", "Repo indicator at Mon 2026-07-06 pre-London on EURUSD 1H: 122 boxes/24 labels/57 lines; NO live box covers any golden EU level (nearest live OB 1.13689-1.13879 is 5.6-20 pips away). Confirms E1 geometry from LuxAlgo != operator's rung map; E2/E3 absent.", "observed", "single frame, 1H"),
    ("FND_DEPLETED_PIERCE", "Visual read wk 2017-10-02: price sat on top of a stack of DEPLETED/ACTIVE-2 MoM demand zones; the week broke down through them (BS down Mon and Thu). My forecaster predicted up because it ignored zone state: doctrine says depleted zones fail => ZFP must rise with reaction count.", "observed", "single week; visual"),
]
for i, d, status, cav in F:
    n(i, "finding", d, "research/e12_lab; context_management/LEARNING_LOG_2026-10-11.md", status=status, caveat=cav)
e("FND_MOM_DECAY", "RECURRENCE", "supports"); e("FND_BOM_100", "MOM_LADDER_ONLY", "questions"); e("FND_TRANS", "ZFP_RULES", "supports"); e("FND_CONSERVE", "CONSERVATION", "supports")
e("FND_NY_TIMING", "SESSIONS", "questions"); e("FND_E1_NULL", "E1_NEEDS_NONOHLC", "motivates"); e("FND_FORECAST_V0", "E2", "informs"); e("FND_RUNG_DENSITY", "E1", "informs")
e("FND_WIDE_CLUSTER", "E1", "informs"); e("FND_INDICATOR_EU", "A_REPO_INDICATOR", "describes"); e("FND_DEPLETED_PIERCE", "RECURRENCE", "supports")

# ============================================================ OPEN QUESTIONS / NEXT (held until operator permission)
OQ = [
    ("OQ_V8", "Where is trident_v8.pine (the 95%-accurate E1 renderer)? Not in repo/upload. Expect it in the handover; station path /home/user/Original_Canon_Data/Pine Scripts/trident_v8.pine."),
    ("OQ_DYNAMIC", "How will E1/E2/E3 be computed per-bar in Pine for Bar Replay when pillars 3/4/7/8 need option expiries/analyst data? Options: input channel (paste/CSV/hosted), OHLC-derivable subset only, or both."),
    ("OQ_DATA", "Blind-week acceptance needs DXY/EU/GU/AU history with Mon-Fri ground truth. Only EURUSD 2017-18 + Jul-2026 pre-anchor reachable here. Needs network allowlist (e.g. TradingView/Yahoo/Dukascopy) or operator-supplied files."),
    ("OQ_BOM", "Operator's exact BoM detector and 'reaction' definition (needed to reproduce 100% BoM reaction)."),
    ("OQ_NYSWING", "Operator's definition of 'NY swing' for the '95% start in 2nd half NY' claim."),
]
for i, d in OQ:
    n(i, "open_question", d, "", status="open")
    e(i, "MISSION", "blocks_or_informs")
n("NEXT_WHEN_PERMITTED", "task",
  "ON PERMISSION: (1) get handover + trident_v8.pine; (2) write expectations BEFORE renders; (3) render E1 in repo rig and do F-17 per-drawing semantic reads; (4) design E2 shape-chain + E3 setup rendering computable per-bar; "
  "(5) acceptance harness: 12 blind weeks, Mon London open -> Fri close, claim/look/verdict ledger; (6) rename Trident->Plutus; (7) never modify frozen E1/E2 semantics.", "")
e("NEXT_WHEN_PERMITTED", "PHASE", "gated_by")

kg.save_to_file(OUT / "plutus_knowledge_graph.json")

# ============================================================ DECISION / CONTEXT GRAPH (Semantica record_decision)
dg = ContextGraph(advanced_analytics=False)
D = [
    ("environment", "Which real FX data to use when Yahoo/Stooq/Dukascopy/TradingView are blocked?",
     "Only GitHub/PyPI/npm reachable. PyPI package `backtesting` bundles real hourly EURUSD; repo fixture holds real TradingView Jul-2026 bars. Used both; did NOT synthesize or mock bars.",
     "use_backtesting_eurusd_plus_fixture", 0.9, ["ENV_NET", "ENV_DATA"]),
    ("tooling", "Install Ars Umbris (arsumbris/arsumbris)?",
     "macOS-only Electron alpha that runs code with no sandboxing; cannot run on this Linux container and executes arbitrary code. Cloned read-only to learn its typed-graph idea; did not install.",
     "do_not_install_use_semantica_json", 0.9, ["A_SEMANTICA"]),
    ("tooling", "How to persist knowledge/context across compaction?",
     "Semantica ContextGraph persisted as JSON in repo + stdlib resume.py + root CLAUDE.md pointing to it + canon docs copied into repo (container uploads are ephemeral).",
     "repo_committed_graph_plus_claude_md", 0.85, ["A_GRAPH", "A_CANON_DIR"]),
    ("methodology", "How to avoid contaminating the blind test?",
     "Picked 12 weeks by fixed seed, forecast from pre-anchor bars only, scored once, did NOT tune on them. Exploration used other weeks / pooled stats.",
     "hold_out_12_weeks_no_tuning", 0.9, ["FND_FORECAST_V0"]),
    ("methodology", "Report the null/negative results?",
     "OHLC-only E1 shows no edge vs shifted baselines; v0 forecaster underperforms 'always range'. Presented as limits of my reconstruction, not as evidence against live canon (missing options/analyst data).",
     "report_negative_results_honestly", 0.95, ["FND_E1_NULL", "FND_FORECAST_V0"]),
    ("governance", "Start indicator work now?",
     "Operator: do not start until explicit permission. No indicator files were modified; rig run was read-only (LuxAlgo bundle rendered, nothing edited).",
     "hold_indicator_work", 1.0, ["PHASE"]),
]
for cat, scen, why, out, conf, ents in D:
    dg.record_decision(category=cat, scenario=scen, reasoning=why, outcome=out, confidence=conf, entities=ents, decision_maker="claude-session-2026-10-11")
dg.save_to_file(OUT / "plutus_decision_graph.json")
print(f"KG nodes={len(NODES)} edges={len(EDGES)}  decisions={len(D)}  -> {OUT}")
