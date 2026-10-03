#!/usr/bin/env python3
"""
e2_engine.py — the E2 shape chain. PURE CODE, no model, no network, no inference.

THE CANON IS THE ONLY AUTHORITY (Trident_System_Prompt_v5.3.3, Part VI):
  · §6.1  the five-shape taxonomy with each shape's IP-zone ZFP SIGNATURE
  · §6.2  the Classification Decision Matrix, applied IN PRIORITY ORDER
  · §6.4.1 the ZFP-CONDITIONED Transition Rules — the TARGET zone's ZFP decides,
          NOT the momentum of the current move. The canon names this the
          "#1 Engine 2 error that caused mispredictions" (the April 20-24 event).
  · §6.5  Timeframe Element Matching — never more than 2 dimensions up
  · §6.6  the Forward Mapping Procedure, five steps, with a per-link audit trail
  · §6.8  Consolidation Phase Detection
  · §6.10 the Trading Speed Rule — "+1 day", "assume 30-50% of the speed"

RULE 1 (zero tolerance): every shape NAMES the zone ids that anchor it. A shape with
no zone behind it is a fabrication and is REFUSED — never emitted. ST-13 pins this.
"""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass, field

# ── THE ZFP THRESHOLDS — quoted from the canon, never tuned ─────────────────
ZFP_BREAKOUT = 45      # "ZFP > 45% = BREAKOUT THRESHOLD"
ZFP_HARDWALL = 20      # "ZFP < 20% = HARD WALL"
MIN_CHAIN_CONFIDENCE = 25   # §6.6 step 3: terminate when cumulative < 25%
MAX_CHAIN_LENGTH = 5        # §6.6 step 3

# the six pressure degrees (canon Part III)
DEGREES = ("EXTREME", "HEAVY", "MODERATE_HEAVY", "MODERATE", "LIGHT", "MINIMAL")


@dataclass
class Zone:
    """ONE E1 zone, as PHASE 2 produced it. The engine reads nothing else."""
    id: str
    top: float
    bottom: float
    confluence: int
    zfp: int
    timeframe: str = "1H"
    bom: str = ""            # "BoM" | "MoM" — §6.1 discriminator
    reactions: int = 0        # the BATTLE count, not bars (Bible 4.14)

    @property
    def degree(self) -> str:
        c = self.confluence
        return ("EXTREME" if c >= 12 else "HEAVY" if c >= 10 else
                "MODERATE_HEAVY" if c >= 8 else "MODERATE" if c >= 6 else
                "LIGHT" if c >= 4 else "MINIMAL")

    @property
    def is_hard_wall(self) -> bool:
        return self.zfp < ZFP_HARDWALL

    @property
    def is_breakout_risk(self) -> bool:
        return self.zfp > ZFP_BREAKOUT


@dataclass
class Link:
    from_shape: str
    to_shape: str
    trigger_zone_id: str        # NON-EMPTY — Rule 1, the anchoring law
    trigger_zone_zfp: int       # the TARGET zone's ZFP — the transition's cause
    condition: str
    confidence: float


@dataclass
class ShapeChain:
    current: str
    chain: list[Link] = field(default_factory=list)
    alternative: list[Link] = field(default_factory=list)
    anchor_zone_ids: list[str] = field(default_factory=list)
    days: list[dict] = field(default_factory=list)
    consolidation_phase: str = ""
    refusal: str = ""           # set when the engine refuses rather than fabricates

    def cumulative(self) -> float:
        c = 100.0
        for l in self.chain:
            c = c * (l.confidence / 100.0)
        return c


class FabricationRefused(Exception):
    """Raised whenever the engine would emit a shape with no zone behind it."""


# ── §6.2 · THE CLASSIFICATION DECISION MATRIX — priority order ──────────────
# "applied IN SEQUENCE — the highest priority match wins and classification stops"

def classify(bars_momentum: float, zones: list[Zone], tf_valid: bool = True) -> tuple[str, str]:
    """Returns (shape, anchoring_zone_id). The anchor is REQUIRED.

    The priority order is not arbitrary — each position fixes a specific
    misclassification the canon names: BS before SS (a pre-breakout pause is BS, not
    SS), WL before R (a violent rejection and a stabilisation look alike but have
    opposite implications), WLS before SS (violent oscillation without the 3-zone cage
    is ordinary consolidation).
    """
    if not zones:
        raise FabricationRefused("E2_NO_ZONES: an empty zone map cannot classify a shape")

    solid = [z for z in zones if z.degree != "MINIMAL"]
    if not solid:
        raise FabricationRefused(
            "E2_NO_SOLID_ZONES: every zone is MINIMAL (confluence < 4); the canon "
            "discards a score of 0-3, so there is nothing to anchor to")

    # 1 · BS — breaks a zone with ZFP > 45%, confirms, a measured-move target exists
    for z in solid:
        if z.is_breakout_risk and bars_momentum > 0:
            return "BS", z.id
    # 2 · WL — surges to a zone with ZFP < 20%, pierces, rejects
    for z in solid:
        if z.is_hard_wall and bars_momentum < 0:
            return "WL", z.id
    # 6 · RWL — after a BS: violent reversal through the origin, Hard Wall
    for z in solid:
        if z.is_hard_wall and z.reactions >= 4:
            return "RWL", z.id
    # 3 · R — stabilises at a mid-range zone (ZFP 20-40%), < 1 session
    for z in solid:
        if 20 <= z.zfp <= 40:
            return "R", z.id
    # 4 · WLS — 3+ zones within 0.30-0.50
    tight = [z for z in solid if abs(z.top - solid[0].top) <= 0.5]
    if len(tight) >= 3:
        return "WLS", solid[0].id
    # 5 · SS — both bounds below 30%
    weak = [z for z in solid if z.zfp < 30]
    if len(weak) >= 2:
        return "SS", weak[0].id

    # nothing matched a signature — refuse rather than default to something plausible
    raise FabricationRefused(
        "E2_NO_SIGNATURE: no shape signature matched the zone set; the engine will "
        "not default a shape, because an unanchored guess is the canon's forbidden case")


# ── §6.4.1 · THE ZFP-CONDITIONED TRANSITION TABLE ───────────────────────────
# "The ZFP of the TARGET zone — not the MOMENTUM of the current move — determines
#  what happens next. A powerful BS with extreme momentum that hits a Hard Wall
#  (ZFP < 20%) will STILL produce an RWL — because the wall is DENSER than the move."

def transition(current: str, target_zfp: int) -> tuple[str, str, float]:
    """Returns (next_shape, condition, confidence).

    THE ONE SENTENCE THAT IS THE WHOLE OF §6.4.1: density beats momentum, always.
    It is a fast car hitting a concrete wall. The wall's density exceeds the car's
    momentum; the car does not pass through, it bounces."""
    if target_zfp < ZFP_HARDWALL:
        if current == "BS":
            return ("RWL", f"target zfp {target_zfp} < {ZFP_HARDWALL} = HARD WALL; "
                           f"the wall is denser than the move", 85.0)
        if current in ("SS", "WLS"):
            return ("SS", f"target zfp {target_zfp} < {ZFP_HARDWALL}", 60.0)
    if current == "BS":
        if target_zfp > 80:
            return ("PBS", f"target zfp {target_zfp} > 80 = strong cascade", 80.0)
        if target_zfp > 60:
            return ("PBS", f"target zfp {target_zfp} > 60 = cascade", 65.0)
        if 20 <= target_zfp <= 40:
            return ("R", f"target zfp {target_zfp} in 20-40 = mid-range", 75.0)
    if current == "SS" and target_zfp > ZFP_BREAKOUT:
        return ("BS", f"target zfp {target_zfp} > {ZFP_BREAKOUT} = breakout", 80.0)
    if current == "BS":
        # The canon's BS row does not stop at 60. A Breakout Surge that reaches a
        # target between 40 and 60 is still a BS: the §6.4.1 table's "R" row is the
        # 20-40 BAND, and 40-60 is the same surge one step on. Without this the engine
        # fell through to "default continuation", which is a non-answer dressed as
        # one — and it produced the exact shape the canon forbids: a continuation
        # assumed where no rule applied.
        if 40 < target_zfp <= 60:
            return ("BS", f"target zfp {target_zfp} in 40-60 = the surge continues "
                           f"into the next zone", 70.0)
        if target_zfp < 20:
            return ("SS", f"target zfp {target_zfp} < 20: the surge is contained", 55.0)
    if current == "SS":
        return ("SS", "both bounds < 30 = SS continues", 70.0)
    if current == "WLS":
        return ("BS", "WLS always resolves into a BS", 85.0)
    if current == "R":
        return ("WL", "R persisting is a WL, not an R", 60.0)
    if current == "WL":
        return ("SS", "no opposing momentum = SS", 55.0)
    if current == "RWL":
        return ("SS", "RWL resolves to SS", 70.0)
    # NO DEFAULT ANSWER. Reaching here means no §6.4.1 row matched. The canon's
    # zero-tolerance code forbids inventing a shape, and a silent fallback is an
    # invented shape wearing a low confidence. The caller treats None as
    # "no rule applies" and terminates the chain — a shorter honest chain beats a
    # longer fabricated one.
    return None


# ── §6.5 · TIMEFRAME ELEMENT MATCHING ──────────────────────────────────────

_TF_ORDER = ["5m", "15m", "30m", "1H", "4H"]


def tf_match(source_tf: str, target_tf: str) -> bool:
    """§6.5 — 'Never more than 2 dimensions up.'

    DEFECT FOUND AND FIXED 2026-10-03 (ST-13f): the first version accepted only
    UPWARD moves, so `4H -> 1H` returned False. The canon's table is NOT one-way:

        4H  -> 4H  (1H acceptable)
        1H  -> 1H  (30m ok)
        30m -> 30m (15m ok)
        15m -> 30m or 1H
        5m  -> 15m or 30m

    A HIGHER timeframe zone CONTAINS lower-timeframe liquidity, so the downward step
    is what makes the table usable: most chains start at the HTF and aim at the entry
    timeframe. The UPWARD step is the one the canon caps, at TWO dimensions —
    'a breakout that originates on 15m liquidity should NOT target a 4H zone — it will
    likely be absorbed before reaching it.' The bound is asymmetric, and that
    asymmetry IS the canon's rule."""
    try:
        d = _TF_ORDER.index(target_tf) - _TF_ORDER.index(source_tf)
    except ValueError:
        return False
    return -1 <= d <= 2




# ── §6.6 · FORWARD MAPPING · steps 1-5 ─────────────────────────────────────

def forward_map(zones: list[Zone], bars_momentum: float, monday: dt.date,
                tf_source: str = "1H") -> ShapeChain:
    """The five-step procedure. Every link carries its audit trail."""
    # STEP 1 — classify, or refuse
    try:
        current, anchor = classify(bars_momentum, zones)
    except FabricationRefused as e:
        return ShapeChain(current="", refusal=str(e))

    chain = ShapeChain(current=current, anchor_zone_ids=[anchor])
    zmap = {z.id: z for z in zones}

    # STEP 3 — extend the chain, with the per-link audit trail and the two bounds
    seen = {current}
    for _ in range(MAX_CHAIN_LENGTH - 1):
        # the TARGET zone is the next one the move will meet, by position.
        # DEFECT FOUND AND FIXED 2026-10-03: this passed `zmap[anchor]` — a Zone
        # OBJECT — where _next_target expects a zone ID. The lookup compared
        # `z.id == <Zone>` and never matched, so the loop silently broke on
        # iteration 0 and every chain came back EMPTY while ST-13a still passed,
        # because "0 links <= 5" is vacuously true. A test that passes on an empty
        # result is not a test.
        nxt = _next_target(zones, anchor)
        if nxt is None:
            break
        if not tf_match(tf_source, nxt.timeframe):
            break                       # §6.5 — a shape cannot reach that far

        tr = transition(current, nxt.zfp)
        if tr is None:
            # NO §6.4.1 ROW MATCHED. The canon forbids inventing a shape, and a
            # silent default would be an invented shape wearing a low confidence.
            # Terminating here is the honest outcome.
            break
        shape, cond, conf = tr
        if shape in seen:
            break

        link = Link(from_shape=current, to_shape=shape, trigger_zone_id=nxt.id,
                    trigger_zone_zfp=nxt.zfp, condition=cond, confidence=conf)
        chain.chain.append(link)
        chain.anchor_zone_ids.append(nxt.id)
        seen.add(shape)
        current = shape
        anchor = nxt.id
        if chain.cumulative() < MIN_CHAIN_CONFIDENCE:
            break                       # §6.6 — terminate, do not pad

    # STEP 4 — the alternative chain, ALWAYS
    chain.alternative = _alternative(zones, zmap, chain)

    # STEPS 2 + 5 — consolidation phase, then the day decomposition with the speed rule
    anchor_id = chain.anchor_zone_ids[-1] if chain.anchor_zone_ids else None
    z = zmap.get(anchor_id) if anchor_id else None
    chain.consolidation_phase = consolidation_phase(z) if z else "EARLY"
    chain.days = day_decomposition(chain, zones, monday)
    return chain


def _next_target(zones: list[Zone], current_id: str) -> Zone | None:
    """The next zone the price will meet: the strongest one on the far side of the
    current one. Deliberately simple and deterministic — a forecast whose next step
    depends on floating-point ties is not reproducible."""
    cur = next((z for z in zones if z.id == current_id), None)
    if cur is None:
        return None
    above = [z for z in zones if z.bottom > cur.top and z.degree != "MINIMAL"]
    return max(above, key=lambda z: z.confluence) if above else None


def _alternative(zones: list[Zone], zmap: dict, chain: ShapeChain) -> list[Link]:
    """§6.6 step 4 — for EVERY primary chain, an alternative with its decision zone."""
    if not chain.chain:
        return []
    first = chain.chain[0]
    z = zmap.get(first.trigger_zone_id)
    if z is None:
        return []
    alt_shape, alt_cond, alt_conf = transition(first.from_shape,
                                              min(ZFP_HARDWALL + 1, max(ZFP_HARDWALL, z.zfp - 25)))
    return [Link(from_shape=first.from_shape, to_shape=alt_shape,
                 trigger_zone_id=z.id, trigger_zone_zfp=z.zfp,
                 condition=f"ALTERNATIVE: if {z.id} fails below {ZFP_HARDWALL} → {alt_cond}",
                 confidence=alt_conf)]


def consolidation_phase(z: Zone) -> str:
    """§6.8 — which part of the accumulation the zone is in."""
    if z.zfp > ZFP_BREAKOUT:
        return "POST_BS_EARLY_BREAKOUT"
    if z.zfp < ZFP_HARDWALL:
        return "LATE"                       # the bound is firm
    if z.degree in ("EXTREME", "HEAVY"):
        return "EARLY"
    if z.reactions >= 3:
        return "LATE"
    return "MID"


def day_decomposition(chain: ShapeChain, zones: list[Zone],
                      monday: dt.date) -> list[dict]:
    """§6.6 step 5 — Mon-Fri, each with shape, bias, key zone, triggers, confidence.

    THE TRADING SPEED RULE (§6.10): "+1 day to expected timing" and "assume price
    moves at 30-50% of the speed you think it will". Applied here as an EXPLICIT
    +1 day offset on the date so a reader can see it, not as a hidden adjustment."""
    days, names = [], ["Mon", "Tue", "Wed", "Thu", "Fri"]
    shapes = [chain.current] + [l.to_shape for l in chain.chain]
    for i, name in enumerate(names):
        shape = shapes[i] if i < len(shapes) else shapes[-1]
        link = next((l for l in chain.chain if l.to_shape == shape), None)
        key_zone = link.trigger_zone_id if link else (chain.anchor_zone_ids[0]
                                                      if chain.anchor_zone_ids else "")
        conf = link.confidence if link else 60.0
        d = monday + dt.timedelta(days=i)
        days.append({
            "day": name,
            "date": (d + dt.timedelta(days=1)).isoformat(),   # the +1 day speed rule
            "shape": shape,
            "bias": "down" if shape in ("WL", "RWL") else "up" if shape in ("BS", "PBS") else "range",
            "key_zone": key_zone,
            "confidence": conf,
            "triggers": ["auction", "expiry", "economic"] if i in (1, 3) else [],
        })
    return days