#!/usr/bin/env python3
"""
GRAPH PRODUCER — DEEPSEEK_AGENT knowledge graph for the Plutus/Trident canon.

Emits GRAPH/knowledge_graph.json: a typed node/edge store encoding the CAUSAL STRUCTURE
of the E1->E2->E3 system, not a list of facts.

Design rules (learned the hard way):
  * every edge is typed and carries a `why` -- an untyped edge is a decoration.
  * every node names its SOURCE (canon file + section) so a claim can be re-verified.
  * the graph is REGENERATED from this script, never hand-edited. The script is the
    producer; the JSON is the artifact. (Evidence-drift law: a checked-in artifact with
    no in-repo producer rots.)

Run:  python3 GRAPH/build_graph.py
"""
from __future__ import annotations
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "knowledge_graph.json"

# ---------------------------------------------------------------- nodes
# id -> (type, label, source, note)
NODES: dict[str, tuple[str, str, str, str]] = {}


def N(nid: str, ntype: str, label: str, source: str, note: str = "") -> None:
    if nid in NODES:
        raise ValueError(f"duplicate node id: {nid}")
    NODES[nid] = (ntype, label, source, note)


# ---- the three engines
N("engine.e1", "engine", "Engine 1 — Zone Map", "v5.3.3 Part II/III",
  "WHERE ARE THE WALLS. Live-validated ~95%. IMMUTABLE.")
N("engine.e2", "engine", "Engine 2 — Shape Chain", "v5.3.3 Part VI",
  "WHAT PATH WILL ENERGY TAKE. Live-validated ~95%. IMMUTABLE.")
N("engine.e3", "engine", "Engine 3 — Trade Setups", "CORRECTED_E3 (1685 lines)",
  "WHERE DO I SURF. ORIGINAL v5.3.3 E3 was BROKEN (18 defects). Fixed engine UNTESTED live.")

# ---- elemental densities
for eid, label, note in [
    ("earth", "EARTH — Liquidity & Institutional Pressure",
     "The foundation. IP zones = HEAVY earth (bedrock); LSZs = standard (soil). Everything anchors to Earth."),
    ("fire", "FIRE — Supply & Demand",
     "Firepower + direction. BoM = hottest (100% reaction if unmitigated). MoM = cooling, tends to pierce."),
    ("water", "WATER — Macro Shapes",
     "The visible wave forms. Gives Fire structure; without it S/D is untradeable chaos."),
    ("air", "AIR — Fibonacci (the Spiderweb)",
     "No intrinsic density. Becomes a STRUCTURE only when anchored to Earth points. Pierces FIRE, not Earth."),
]:
    N(f"elem.{eid}", "elemental_density", label, "Fractal Architecture v2.3 §2", note)

# ---- preconditions / coupling laws
N("law.r3", "law", "R3 LAW — E2 DESIGNATES, E3 OBEYS",
  "CORRECTED_E3 §8.0", "E3 never overrides E1/E2; every anchor traces to an E1 zone id + E2 shape day.")
N("law.earth_fire_link", "law", "Earth and Fire are intrinsically linked",
  "Fractal Architecture §4.3",
  "Fire w/o Earth = no fuel; Earth w/o Fire = no direction. A move needs BOTH.")
N("law.mom_ladder_only", "law", "MoM zones = LADDER STEPS ONLY",
  "Fractal Architecture §7", "No reversal entries at MoM, EVER. Virgin MoM = DEATH ZONE.")
N("law.conservation", "law", "Conservation of energy — after 2 piercing moves, 1-2 days consolidation",
  "Fractal Architecture §9", "The universal recovery law. Second Law of Thermodynamics applied to markets.")
N("law.speed_3050", "law", "Trading speed rule — price moves at 30-50% of expected speed",
  "v5.3.3 §6.10", "Add +1 day to timing; today's move becomes tomorrow's.")
N("law.rrr_floor", "law", "RRR floor 3.0 (IRON LAW)",
  "CORRECTED_E3 §8.20", "Enforced in CODE, never by the model. Executed standard 3.5; norm 4.0+; chain ceiling 15.0.")
N("law.sequential_sweep", "law", "Price ALWAYS sweeps liquidity zone by zone, in sequence",
  "v5.3.3 §2.0", "It never skips a zone. Unretested zones WILL be retested.")
N("law.singular_candle", "law", "Singular-candle zone construction (zero tolerance)",
  "v5.3.3 §3.2 Step 0f", "Zone = the SINGLE candle immediately before a strong directional move.")
N("law.honest_absence", "law", "HONEST ABSENCE — never fabricate a level",
  "CORRECTED_E3 §8.14 r16",
  "SL_INVALID/TP_NULL/RRR_BELOW_FLOOR => NO EMISSION. The 90% win rate depends on what the code REFUSES to emit.")

# ---- E1 quantities
N("q.zfp_geometric", "quantity", "ZFP (geometric) = zone_height / pair_ref_range x 100",
  "v5.3.3 §10.8",
  "THE quantity E2 consumes. Narrow zone -> LOW ZFP -> HARD WALL. DXY ref 1.60 / EU 0.0200 / GU 0.0200 / AU 0.0150.")
N("q.zfp_fundamental", "quantity", "Failure probability (fundamental) by zone TYPE",
  "v5.3.3 Appendix B",
  "Hard Wall 5-15% ... One-Touch 50-70%. Agrees with the geometric ZFP at the EXTREMES only.")
N("q.confluence", "quantity", "Confluence score 0-14 (6 dimensions x2 + extreme bonus +2)",
  "v5.3.3 §3.2 Synthesis")
N("q.pressure_degree", "quantity", "Pressure degree (EXTREME/HEAVY/MOD-HEAVY/MODERATE/LIGHT/MINIMAL)",
  "v5.3.3 §3.2 Synthesis", "12-14 EXTREME ... 0-3 MINIMAL. Carries its OWN failure-probability column.")
N("q.reaction_count", "quantity", "Zone reaction counter 0/1-2/3+",
  "v5.3.3 §3.2 + CORRECTED_E3 §8.1",
  "0 virgin (strongest if BoM, DEATH if MoM) / 1-2 active / 3+ depleted = TP only.")
N("q.bom_mom", "quantity", "BoM / MoM classification", "v5.3.3 §3.2")
N("q.poi_tier", "quantity", "POI tier 1/2/3 (confluent / IP-only / 4H-only)", "v5.3.3 §3.2 Step 9.7")
N("q.zfp_band_wrong", "defect", "LIVE DEFECT — zfp_from_degree(confluence) substituted for the geometric ZFP",
  "ENGINE1_V8_VS_MINE.md",
  "Different quantity. Inverts E2's terminal shape at the extremes: a hard-wall Ceiling reads LIGHT/50% -> predicts BS continuation instead of RWL reversal.")

# ---- E2 shapes
SHAPES = {
    "ss": ("SS — Swing Scalps", "Range-bound oscillation. Both bounding zones ZFP<30%."),
    "bs": ("BS — Breakout Surge", "Decisive break + directional surge. Failing zone ZFP>45%; 15+min confirmation."),
    "pbs": ("PBS — Piercing BS", "BS that pierces intermediate zones. Failing zone ZFP>70%."),
    "r": ("R — Recovery", "Always transitional. Mid-range zone ZFP 20-40%."),
    "rs": ("RS — Recovery Surge", "Sharp directional retrace instead of slow consolidation."),
    "wl": ("WL — Whiplash", "Spike-and-reject. The rejection is the signal, not the surge. Rejection zone ZFP<20%."),
    "rwl": ("RWL — Reverse Whiplash", "WL opposite the preceding BS. Most common follow-on after a BS."),
    "pwl": ("PWL — Piercing WL", "Pierces multiple zones before rejection."),
    "prwl": ("PRWL — Piercing Reverse Whiplash", "STRONGEST reversal signal in the taxonomy."),
    "wls": ("WLS — Whiplash Storm", "2-5 sessions of violent oscillation. Almost always resolves into a BS."),
    "dwl": ("SS(DWL) — Double Whiplash", "Two rapid whipsaws in the range; volatility precedes a breakout attempt."),
}
for sid, (label, note) in SHAPES.items():
    N(f"shape.{sid}", "macro_shape", label, "v5.3.3 §6.1", note)

# ---- E2 chains
N("chain.default", "chain", "SS -> BS -> R -> WL (HIGHEST frequency)", "v5.3.3 §6.3",
  "The default weekly storyline: SS builds positioning pressure, the zone fails, BS, recovery, WL at target.")
N("chain.false_breakout", "chain", "BS -> RWL -> SS -> BS", "v5.3.3 §6.3",
  "Complete false-breakout cycle. The SECOND BS often succeeds.")
N("chain.wls_resolve", "chain", "WLS -> BS (VERY HIGH)", "v5.3.3 §6.4", "WLS almost always resolves into a BS; only the direction is in question.")

# ---- E3 constructs
N("e3.entry_ts1", "rule", "TS-1 SNIPER ENTRY = the zone edge CLOSEST to approaching price",
  "CORRECTED_E3 §8.2", "SHORT from supply -> bottom edge. LONG from demand -> top edge.")
N("e3.sl_ladder", "rule", "SL Ladder-Steps — 3p outside the back edge, OR 1-2p inside the next rung's close edge",
  "CORRECTED_E3 §8.2", "Relevant zone keyed on pressure state: INTACT -> LQZ shield / ABSORBED -> S/D / else golden SL.")
N("e3.tp_single", "rule", "ONE TP per trade — regime-conditional, never partial",
  "CORRECTED_E3 §8.3", "Strong zone -> near edge + 1-2p spread. Weak zone -> far edge. Law-14: TP >= 1.2 x SL.")
N("e3.lifecycle", "rule", "Zone pressure lifecycle VIRGIN->ACTIVE-1->ACTIVE-2->DEPLETED->FORTRESS->BROKEN",
  "CORRECTED_E3 §8.1",
  "100% / 80% / 50% / TP-only / 95% direction flip / never again. 4th+ battle is skipped.")
N("e3.freshness", "rule", "4-Stage Freshness Gate (index i>2 skipped; any pierce = VIOLATED terminal)",
  "CORRECTED_E3 §8.1")
N("e3.rrr_refine", "rule", "3-attempt refinement loop — ENTRY FIXED, re-anchor SL/TP only",
  "CORRECTED_E3 §8.4", "The entry is the hard-won insight; SL/TP are engineering.")
N("e3.avatar", "rule", "Master Trade Setup = E + FLR (Avatar State)",
  "CORRECTED_E3 §8.9", "P(all four elements wrong) = 0.2^4 = 0.16%. Probability INTERSECTION, not addition.")
N("e3.rocket", "rule", "Stop-limit trip-wire: trigger detects, the LIMIT fires at the entry zone",
  "CORRECTED_E3 §8.7", "If price never returns the limit never fills => ZERO additional risk.")
N("e3.ip_never_entry", "rule", "IP zones are NEVER entries (STRUCTURAL_ENTRY_SOURCES = ORDER_BLOCK, LQZ)",
  "CORRECTED_E3 §8.1", "IP = confluence/ZFP/context + SL/TP rungs only. Mirror search SKIPS source=='PILLAR'.")

# ---- pairs
for pid, label, note in [
    ("dxy", "DXY — Air-Fire dominant, MASTER COMPASS",
     "Directional conviction ONLY. Never arithmetically converted to pair levels (355-710 pip error class)."),
    ("eu", "EUR/USD — Fire-Earth dominant",
     "Primary swing pair. 62.4% of DXY. PA touches the S/D-liquidity overlap DIRECTLY (NO liquidity shield)."),
    ("gu", "GBP/USD — Earth-Water dominant",
     "Primary scalp pair. 'Liquidity is the only thing respected' -- S/D gets pierced. Earth LIQUIDITY SHIELDS form in front of Fire."),
    ("au", "AUD/USD — Earth dominant (slow)",
     "Secondary swing. Molasses: 2-4 days per HTF move. Map the ladder and surf."),
]:
    N(f"pair.{pid}", "pair_profile", label, "Fractal Architecture §10 / v5.3.3 §2.0.3", note)

# ---- research instruments
N("instr.v8pine", "artifact", "trident_v8.pine (668 lines) — GLM 5.1 reference indicator",
  "Original_Canon_Data/Pine Scripts/",
  "Renders E1 (5 zones + 6 LSZ + 7 option strikes) AND carries E2 chain summary + E3 trade rows in a 2x17 info table.")
N("instr.livepine", "artifact", "plutus-vision-v0/v1/v2.pine — the LIVE build",
  "PLUTUS_VISION/ (handover)",
  "E1 zones render, but calcZFP is the degree-band, zDeg caps at 5/14, LSZ removed, options absent, E2+E3 absent from the render.")
N("instr.engine3py", "artifact", "trident_engine3_v8.py (58KB)", "Original_Canon_Data/Toolset/")
N("instr.pineide", "artifact", "pine-ide / PLUTUS VISION IDE rig", "PLUTUS_VISION/pine-ide")
N("instr.exerciselab", "artifact", "LIVE CHART EXERCISE LAB (this workspace)", "DEEPSEEK_AGENT/EXERCISES")

# ---------------------------------------------------------------- edges
EDGES: list[dict] = []


def E(src: str, dst: str, etype: str, why: str) -> None:
    if src not in NODES:
        raise ValueError(f"edge from unknown node: {src}")
    if dst not in NODES:
        raise ValueError(f"edge to unknown node: {dst}")
    EDGES.append({"from": src, "to": dst, "type": etype, "why": why})


# engine pipeline
E("engine.e1", "engine.e2", "produces_input_for",
  "E2 forward-maps shape chains ANCHORED to the E1 zone map; a shape without an IP-zone anchor is illegal (E2 RULE 1).")
E("engine.e2", "engine.e3", "produces_input_for",
  "E3's Phase 1 consumes E2's day-by-day decomposition; without it E3 cannot assign DAY labels.")
E("law.r3", "engine.e3", "constrains", "E3 obeys E1+E2; never re-designates, never invents levels.")

# the critical coupling
E("q.zfp_geometric", "engine.e2", "conditions",
  "E2's ZFP-CONDITIONED TRANSITION table keys the next shape on the TARGET zone's ZFP. This is the single highest-leverage edge in the system.")
E("q.zfp_fundamental", "q.zfp_geometric", "correlates_with",
  "Agree at the extremes (<20% hard wall, >45% failing) and diverge in the middle -- which is why substituting one for the other passes most zones and INVERTS the extremes.")
E("q.zfp_band_wrong", "q.zfp_geometric", "substituted_for",
  "THE DEFECT. A wrong quantity in E1 silently flips the E2 chain, and therefore every downstream E3 setup.")

# E1 internals
E("q.confluence", "q.pressure_degree", "determines", "Score 0-14 maps to the pressure-degree band.")
E("q.reaction_count", "e3.lifecycle", "instantiates", "The counter IS the lifecycle state.")
E("q.bom_mom", "law.mom_ladder_only", "is_governed_by", "BoM may be an entry; MoM is ladder-step/TP only.")
E("law.singular_candle", "q.bom_mom", "enables", "You cannot classify BoM/MoM without a real origin candle.")
E("q.poi_tier", "e3.ip_never_entry", "reinforces",
  "Tier-1 confluent POI is the primary location, but the ENTRY anchor is still an order block / LQZ, not the IP zone.")

# elemental wiring
E("elem.earth", "elem.fire", "fuels", "Fire needs Earth: an S/D zone with no liquidity cannot react with force.")
E("elem.fire", "elem.water", "materializes_as", "Energy released by Fire flowing through Earth channels becomes the visible shape.")
E("elem.water", "elem.air", "is_predicted_by", "The Fib spiderweb maps the wave's trajectory before it happens.")
E("elem.air", "elem.earth", "creates", "Algorithms act on Fib levels; those levels become new liquidity. The cycle closes.")
E("law.earth_fire_link", "elem.earth", "explains", "Why the strongest entries are at S/D + liquidity overlap.")
E("elem.air", "elem.fire", "pierces_then_reverses",
  "Air pierces FIRE (4H BoM S/D), not Earth -- and the pierce is what triggers the whiplash reaction.")

# shape transition wiring (the ZFP-conditioned table)
E("q.zfp_geometric", "shape.rwl", "selects_when_hard_wall",
  "BS reaching a target zone with ZFP<20% MUST predict RWL. The #1 historical E2 error was predicting continuation here.")
E("q.zfp_geometric", "shape.pbs", "selects_when_weak",
  "BS reaching a zone with ZFP>60% (>=80% strong cascade) predicts PBS.")
E("q.zfp_geometric", "shape.r", "selects_when_midrange",
  "BS reaching a zone with ZFP 20-40% predicts R (stabilisation), not rejection.")
E("q.zfp_geometric", "shape.bs", "selects_when_bounding_fails",
  "SS with a bounding zone ZFP>45% predicts BS -- breakout imminent.")
E("q.zfp_geometric", "shape.ss", "selects_when_both_hold",
  "SS with all bounding zones ZFP<30% predicts SS continues.")
E("shape.wls", "shape.bs", "resolves_into", "VERY HIGH: WLS almost always resolves into a BS -- only the direction is open.")
E("shape.bs", "shape.rwl", "most_common_followon", "RWL is the most common follow-on after a BS.")
E("shape.bs", "shape.r", "transitions_to", "BS -> R when price reaches a Measured Move target (ZFP 20-40%).")
E("shape.r", "shape.ss", "reclassifies_to", "If stabilisation persists > 1 session it IS consolidation -- reclassify.")
E("law.conservation", "shape.wls", "bounds", "No whiplash storm immediately after 2 strong piercing moves.")
E("law.speed_3050", "chain.default", "time_shifts", "Add +1 day; today's move becomes tomorrow's, so the chain slips.")

# shape-family wiring (variant -> base shape), so no shape node is an orphan
E("shape.wl", "shape.rwl", "varies_into", "RWL is a WL in the opposite direction of the preceding BS.")
E("shape.wl", "shape.pwl", "varies_into", "PWL is a WL whose surge pierces multiple zones before rejection.")
E("shape.rwl", "shape.prwl", "varies_into", "PRWL adds piercing characteristics -- the strongest reversal signal.")
E("shape.bs", "shape.pbs", "varies_into", "PBS is a BS powerful enough to pierce intermediate zones without pausing.")
E("shape.r", "shape.rs", "varies_into", "RS replaces slow consolidation with a sharp directional retrace.")
E("shape.ss", "shape.dwl", "varies_into", "SS(DWL) is two rapid whipsaws inside the SS range.")
E("chain.wls_resolve", "shape.wls", "resolves", "The WLS->BS resolution is the chain this node names.")
E("shape.wl", "engine.e2", "is_classified_by", "WL is a taxonomy entry E2 must emit, anchored to an E1 zone.")
E("shape.prwl", "law.conservation", "exhausts_into", "The strongest reversal is followed by the mandatory recovery phase.")

# laws that needed a home
E("law.sequential_sweep", "elem.water", "is_the_water_law",
  "Water flows through EVERY channel: price sweeps liquidity zone by zone, in order, and never skips one.")
E("law.sequential_sweep", "e3.tp_single", "constrains",
  "The TP must be the NEAREST opposing structure on the walk -- a distant target would require skipping zones.")

# E3 internals
E("e3.sl_ladder", "e3.entry_ts1", "anchors_to", "SL distance is measured FROM the TS-1 sniper entry.")
E("e3.sl_ladder", "e3.lifecycle", "reads", "The operative-defense zone is keyed on the zone's pressure state (INTACT vs ABSORBED).")

# pairs
E("pair.au", "law.speed_3050", "is_the_extreme_case",
  "AU is 'molasses' -- 2-4 days per HTF move, the clearest instance of the 30-50% speed rule.")
E("pair.au", "elem.earth", "dominated_by", "Pure Earth dominance: map the liquidity ladder and surf the shapes.")
E("instr.pineide", "instr.livepine", "renders", "The Pine IDE is the rig that loads and renders the live build.")
E("instr.v8pine", "q.zfp_geometric", "implements",
  "v8's calcZFP(tp,bt,pair) is the authority implementation of the geometric ZFP.")

# pattern chains
E("chain.default", "shape.ss", "starts_with", "SS builds positioning pressure first.")
E("chain.false_breakout", "shape.rwl", "pivots_on", "The RWL reject is what makes the breakout false.")

# E3 wiring
E("e3.lifecycle", "e3.freshness", "is_enforced_by", "The 4-stage gate reads the lifecycle to decide admissibility.")
E("law.mom_ladder_only", "e3.ip_never_entry", "aligns_with", "Both forbid treating a weak/continuation structure as a reversal entry.")
E("law.rrr_floor", "e3.rrr_refine", "gates", "The floor is the gate; the refinement loop is how a good entry survives a bad anchor.")
E("e3.entry_ts1", "e3.tp_single", "determines", "Entry determines SL determines TP determines RRR -- an interlocking triangle.")
E("e3.rocket", "e3.avatar", "composes", "E + FLR is the literal composition of the Avatar State.")
E("law.honest_absence", "e3.rrr_refine", "bounds", "After 3 attempts the setup HARD REJECTS -- never a fabricated level to pass the floor.")
E("law.honest_absence", "law.rrr_floor", "protects", "The floor is only meaningful if refusal is honest.")

# pairs
E("pair.dxy", "pair.eu", "cascades_inverse", "DXY up => EU down. Structural equivalence, NEVER arithmetic conversion.")
E("pair.dxy", "pair.gu", "cascades_to", "GU mirror keeps direction; EU mirror inverts.")
E("pair.eu", "pair.gu", "shares_mechanics", "Same shapes/zones/setups -- only price levels differ.")
E("pair.gu", "elem.earth", "dominated_by", "On GU liquidity is the only thing respected; Earth shields protect Fire.")

# instruments
E("instr.v8pine", "instr.livepine", "is_the_reference_for",
  "The live build must reach the v8's render fidelity and then exceed it with E2+E3.")
E("instr.livepine", "q.zfp_band_wrong", "exhibits", "The live build computes the wrong ZFP quantity.")
E("instr.engine3py", "instr.v8pine", "generates", "The v8 Python engine emits the data the v8 pine renders.")
E("instr.exerciselab", "engine.e1", "exercises", "Hand-identification of E1 zones on live bars.")
E("instr.exerciselab", "engine.e2", "exercises", "Hand-derivation of the shape chain from live bars.")
E("instr.exerciselab", "engine.e3", "exercises", "Hand-construction of setups from the derived zones+shapes.")

# ---------------------------------------------------------------- emit
def main() -> int:
    nodes = [
        {"id": nid, "type": t, "label": lab, "source": src, "note": note}
        for nid, (t, lab, src, note) in NODES.items()
    ]
    doc = {
        "schema": "plutus-canon-graph/1",
        "producer": "GRAPH/build_graph.py",
        "node_count": len(nodes),
        "edge_count": len(EDGES),
        "nodes": nodes,
        "edges": EDGES,
    }
    OUT.write_text(json.dumps(doc, indent=2) + "\n")
    types: dict[str, int] = {}
    for n in nodes:
        types[n["type"]] = types.get(n["type"], 0) + 1
    print(f"wrote {OUT}")
    print(f"nodes={len(nodes)} edges={len(EDGES)}")
    for t, c in sorted(types.items(), key=lambda kv: -kv[1]):
        print(f"  {t:20s} {c}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
