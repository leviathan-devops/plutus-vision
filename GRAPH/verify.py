#!/usr/bin/env python3
"""
GRAPH VERIFIER — validates knowledge_graph.json.

A graph nobody validates is a decoration. This checks the properties that make the graph
USEFUL for compaction recovery, with MUST-FIRE controls (the two-sided adjudication law:
a verifier that has never failed is not a verifier).

Checks:
  V1  schema + counts are internally consistent
  V2  referential integrity -- every edge endpoint exists as a node
  V3  no orphan nodes (every node has >=1 edge) -- an unconnected node recovers nothing
  V4  every node carries a non-empty source (a claim must be re-verifiable)
  V5  every edge carries a non-empty `why` (an untyped/unexplained edge is decoration)
  V6  no duplicate ids
  V7  the CRUX is present: the zfp_geometric -> engine.e2 `conditions` edge exists,
      and q.zfp_band_wrong is linked to it (this is the single most valuable fact in
      the graph -- if a rebuild loses it, the graph has failed its purpose)
  V8  MUST-FIRE control: injecting a dangling edge MUST be detected.

Run:  python3 GRAPH/verify.py
"""
from __future__ import annotations
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
GRAPH = HERE / "knowledge_graph.json"

failures: list[str] = []


def check(cond: bool, label: str) -> None:
    if cond:
        print(f"  PASS  {label}")
    else:
        print(f"  FAIL  {label}")
        failures.append(label)


def validate(doc: dict) -> list[str]:
    """Return a list of problems. Pure function so the must-fire control can reuse it."""
    problems: list[str] = []
    nodes = doc.get("nodes", [])
    edges = doc.get("edges", [])

    ids = [n.get("id") for n in nodes]
    if len(ids) != len(set(ids)):
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        problems.append(f"V6 duplicate node ids: {dupes}")
    if doc.get("node_count") != len(nodes):
        problems.append(f"V1 node_count {doc.get('node_count')} != {len(nodes)}")
    if doc.get("edge_count") != len(edges):
        problems.append(f"V1 edge_count {doc.get('edge_count')} != {len(edges)}")

    idset = set(ids)
    for e in edges:
        if e.get("from") not in idset or e.get("to") not in idset:
            problems.append(f"V2 dangling edge {e.get('from')} -> {e.get('to')}")

    touched: set[str] = set()
    for e in edges:
        touched.add(e.get("from"))
        touched.add(e.get("to"))
    orphans = sorted(idset - touched)
    if orphans:
        problems.append(f"V3 orphan nodes (no edges): {orphans}")

    for n in nodes:
        if not str(n.get("source", "")).strip():
            problems.append(f"V4 node {n.get('id')} has no source")
    for e in edges:
        if not str(e.get("why", "")).strip():
            problems.append(f"V5 edge {e.get('from')}->{e.get('to')} has no why")

    crux = any(
        e.get("from") == "q.zfp_geometric"
        and e.get("to") == "engine.e2"
        and e.get("type") == "conditions"
        for e in edges
    )
    if not crux:
        problems.append("V7 CRUX MISSING: q.zfp_geometric -> engine.e2 [conditions]")
    defect = any(
        e.get("from") == "q.zfp_band_wrong"
        and e.get("to") == "q.zfp_geometric"
        for e in edges
    )
    if not defect:
        problems.append("V7 CRUX MISSING: q.zfp_band_wrong -> q.zfp_geometric")
    return problems


def main() -> int:
    if not GRAPH.exists():
        print(f"FATAL: {GRAPH} not found -- run GRAPH/build_graph.py first")
        return 2
    doc = json.loads(GRAPH.read_text())
    nodes = doc.get("nodes", [])
    edges = doc.get("edges", [])

    print("=" * 68)
    print("GRAPH VERIFY — schema plutus-canon-graph/1")
    print("=" * 68)
    check(doc.get("schema") == "plutus-canon-graph/1", "V1 schema id")
    check(len(nodes) > 0, f"V1 nodes present ({len(nodes)})")
    check(len(edges) > 0, f"V1 edges present ({len(edges)})")

    problems = validate(doc)
    # strip the V-prefix to report by group
    for tag, label in [
        ("V2", "V2 referential integrity (no dangling edges)"),
        ("V3", "V3 no orphan nodes"),
        ("V4", "V4 every node has a source"),
        ("V5", "V5 every edge has a why"),
        ("V6", "V6 no duplicate ids"),
        ("V1", "V1 counts consistent"),
        ("V7", "V7 CRUX present (the ZFP coupling + its defect)"),
    ]:
        hit = [p for p in problems if p.startswith(tag)]
        check(not hit, label)
        for h in hit:
            print(f"        {h}")

    # ---------------- MUST-FIRE CONTROL ----------------
    # Inject a dangling edge; validate() MUST report it. If it does not, the verifier
    # is blind and every PASS above is worthless.
    print("-" * 68)
    print("MUST-FIRE CONTROL — inject a dangling edge, verifier must catch it")
    broken = json.loads(json.dumps(doc))
    broken["nodes"] = list(broken["nodes"])
    broken["node_count"] = len(broken["nodes"])
    broken["edges"] = list(broken["edges"]) + [
        {"from": "engine.e1", "to": "node.that.does.not.exist", "type": "t", "why": "control"}
    ]
    broken["edge_count"] = len(broken["edges"])
    control_hits = validate(broken)
    caught = any("V2 dangling edge" in p for p in control_hits)
    check(caught, "CONTROL: dangling edge detected (verifier is not blind)")

    print("-" * 68)
    if failures:
        print(f"VERDICT: FAIL — {len(failures)} check(s) failed")
        return 1
    print(f"VERDICT: PASS — {len(nodes)} nodes / {len(edges)} edges, integrity + crux + control OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
