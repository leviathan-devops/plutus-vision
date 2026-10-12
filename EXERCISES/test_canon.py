"""CANON CONFORMANCE TESTS — the invariants my exercise lab must uphold.

These are real assertions against the canon, not smoke tests. Each one pins a rule that,
if it drifted, would silently corrupt every downstream derived result. Several are written
as MUST-FIRE controls: they assert the code REJECTS the wrong thing, because a verifier
that has never failed is not a verifier.

Run:  python3 -m pytest EXERCISES/test_canon.py -q
"""
from __future__ import annotations

import json
import pathlib
import sys

import pytest

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import lab  # noqa: E402


# ---------------------------------------------------------------- ZFP (§10.8)
def test_zfp_geometric_matches_canon_pine():
    """v5.3.3 §10.8: pct = round(zoneW / refRange * 100)."""
    # the v8's own Ceiling: 99.23 - 99.16 = 0.07 over the DXY ref 1.60
    assert lab.zfp_geometric(99.16, 99.23, "DXY") == 4
    # a 0.34-wide zone -> 21%
    assert lab.zfp_geometric(97.63, 97.97, "DXY") == 21
    # EUR/USD ref is 0.0200 (200 pips) -> a 20-pip zone = 10%
    assert lab.zfp_geometric(1.1000, 1.1020, "EUR/USD") == 10
    # AUD ref is 0.0150
    assert lab.zfp_geometric(0.7000, 0.7030, "AUDUSD") == 20


def test_zfp_is_geometric_not_a_confluence_band():
    """THE CRUX. Two zones with the SAME (absent) confluence but different heights MUST
    produce different ZFP. If ZFP were derived from a confluence score this would fail --
    which is exactly how the live build inverts E2."""
    narrow = lab.zfp_geometric(100.000, 100.100, "DXY")   # 0.10 tall
    wide = lab.zfp_geometric(100.000, 100.800, "DXY")     # 0.80 tall
    assert narrow < wide
    assert narrow < lab.ZFP_HARD_WALL < wide


def test_narrow_zone_is_a_hard_wall():
    z = lab.zfp_geometric(97.632, 97.632 + 0.05, "DXY")
    assert z < lab.ZFP_HARD_WALL
    assert "HARD WALL" in lab.zfp_verdict(z)


# ---------------------------------------------------------------- E2 hinge (§6.4.1)
def test_hinge_hard_wall_yields_reversal_not_continuation():
    """The #1 historical E2 error. BS + target ZFP < 20% MUST produce RWL."""
    nxt, why = lab.e2_next_shape(4, "BS")
    assert nxt == "RWL"
    assert "HARD WALL" in why


def test_hinge_midrange_yields_recovery():
    assert lab.e2_next_shape(30, "BS")[0] == "R"


def test_hinge_weak_zone_yields_cascade():
    assert lab.e2_next_shape(70, "BS")[0] == "PBS"
    assert lab.e2_next_shape(90, "BS")[0] == "PBS"


def test_hinge_bounding_zone_failure_yields_breakout():
    assert lab.e2_next_shape(50, "SS")[0] == "BS"


def test_hinge_both_boundaries_hold_continues_ss():
    assert lab.e2_next_shape(10, "SS")[0] == "SS"


def test_hinge_wls_almost_always_resolves_to_bs():
    assert lab.e2_next_shape(50, "WLS")[0] == "BS"


# ---------------------------------------------------------------- clustering
def test_clustering_caps_zone_width():
    """The measured bug: single-linkage chained 98.78..100.09 into a 1.31-point 'zone'."""
    levels = [round(98.78 + 0.10 * i, 2) for i in range(14)]  # a chained ladder
    zones = lab.cluster_zones(levels)
    for z in zones:
        assert z["width"] <= lab.MAX_ZONE_WIDTH + 1e-9, f"zone too wide: {z}"


def test_clustering_groups_a_real_cluster():
    zones = lab.cluster_zones([100.00, 100.05, 100.08, 100.12])
    assert len(zones) == 1
    assert zones[0]["n"] == 4
    assert zones[0]["tag"] == "HIGH-DENSITY ZONE"


def test_singleton_is_marked_non_authoritative():
    """A single level must NOT masquerade as an authoritative hard wall."""
    zones = lab.cluster_zones([100.00])
    assert zones[0]["n"] == 1
    assert zones[0]["authoritative"] is False


# ---------------------------------------------------------------- invariants
def test_rrr_floor_is_three():
    """Operator IRON LAW 2026-07-31. Enforced in code, never by the model."""
    # the lab does not emit setups yet; the constant is pinned where it will be used
    import re
    src = (ROOT / "CANON" / "03_ENGINE3_TRADE_SETUPS.md").read_text()
    assert "RRR ≥ 3.0" in src or "RRR >= 3.0" in src
    assert "MAX_CHAIN_RRR" in src


def test_graph_has_no_dangling_edges():
    doc = json.loads((ROOT / "GRAPH" / "knowledge_graph.json").read_text())
    ids = {n["id"] for n in doc["nodes"]}
    bad = [e for e in doc["edges"] if e["from"] not in ids or e["to"] not in ids]
    assert bad == []


def test_graph_pins_the_crux():
    """If a rebuild loses this edge the graph has failed its purpose."""
    doc = json.loads((ROOT / "GRAPH" / "knowledge_graph.json").read_text())
    assert any(e["from"] == "q.zfp_geometric" and e["to"] == "engine.e2"
               and e["type"] == "conditions" for e in doc["edges"])


# ---------------------------------------------------------------- MUST-FIRE controls
def test_control_hinge_rejects_a_bad_zfp_reading():
    """CONTROL: the defect's reading (a hard wall masquerading as ~50%) DOES produce the
    wrong answer. This is the counterfactual that proves the crux matters.

    The assertion is on the MEANINGFUL property -- the defect must lose the reversal --
    not on a specific label the canon never specifies: §6.4.1 legitimately leaves the
    40-60% band undefined, and the honest implementation says so rather than inventing one.
    """
    correct, why_c = lab.e2_next_shape(4, "BS")      # true geometric ZFP of a hard wall
    defective, why_d = lab.e2_next_shape(50, "BS")   # what the degree-band substitution says
    assert correct == "RWL"                          # the truth: reversal
    assert "HARD WALL" in why_c
    assert defective != "RWL"                        # the defect LOSES the reversal
    assert "undefined" in why_d or "failing" in why_d


def test_control_cluster_cap_bites():
    """CONTROL: without the cap this ladder WOULD fuse into one over-wide zone."""
    levels = [round(98.78 + 0.10 * i, 2) for i in range(14)]
    assert max(levels) - min(levels) > lab.MAX_ZONE_WIDTH  # the raw span exceeds the cap
    assert len(lab.cluster_zones(levels)) > 1              # so it must have been split
