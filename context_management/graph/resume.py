#!/usr/bin/env python3
"""Regain full macro context from the committed graphs. Stdlib only.

  python3 context_management/graph/resume.py              # governance + mission + phase + engines + findings + open questions + decisions
  python3 context_management/graph/resume.py --node E3    # one node, with in/out edges
  python3 context_management/graph/resume.py --type rule  # all nodes of a type (rule|law|element|shape|finding|constraint|artifact|...)
  python3 context_management/graph/resume.py --grep rocket
"""
import json
import pathlib
import signal
import sys
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
import textwrap

H = pathlib.Path(__file__).parent
KG = json.load(open(H / "plutus_knowledge_graph.json"))
DG = json.load(open(H / "plutus_decision_graph.json"))
N = {x["id"]: x for x in KG["nodes"]}
E = KG["edges"]


def txt(x):
    p = x.get("properties", {})
    return p.get("content", "")


def show(i, width=118):
    x = N[i]
    p = x.get("properties", {})
    extra = " ".join(f"{k}={p[k]}" for k in ("status", "confidence", "caveat", "priority") if k in p)
    print(f"[{x['type']}] {i}" + (f"  ({extra})" if extra else ""))
    print(textwrap.fill(txt(x), width, initial_indent="    ", subsequent_indent="    "))
    if p.get("ref"):
        print(f"    ref: {p['ref']}")


def edges_of(i):
    out = [(e["type"], e["target_id"]) for e in E if e["source_id"] == i]
    inn = [(e["type"], e["source_id"]) for e in E if e["target_id"] == i]
    return out, inn


a = sys.argv[1:]
if a[:1] == ["--node"]:
    show(a[1])
    o, i = edges_of(a[1])
    print("  out:", ", ".join(f"-{t}-> {x}" for t, x in o) or "-")
    print("  in :", ", ".join(f"{x} -{t}->" for t, x in i) or "-")
    sys.exit()
if a[:1] == ["--type"]:
    for i, x in N.items():
        if x["type"] == a[1]:
            show(i)
            print()
    sys.exit()
if a[:1] == ["--grep"]:
    k = a[1].lower()
    for i, x in N.items():
        if k in (i + txt(x)).lower():
            show(i)
            print()
    sys.exit()

print("=" * 120)
print("PLUTUS — RESUME CONTEXT (graph:", KG["graph_id"], ")  nodes", len(N), "edges", len(E))
print("=" * 120)
for t, title in (("state", "PHASE"), ("mission", "MISSION"), ("constraint", "GOVERNANCE (obey)")):
    print(f"\n### {title}")
    for i, x in N.items():
        if x["type"] == t:
            show(i)
print("\n### CANON SPINE: elements -> engines -> shapes")
for t in ("element", "engine"):
    for i, x in N.items():
        if x["type"] == t:
            print(f"  {i:7s} {txt(x)[:150]}...")
print("  shapes:", ", ".join(i.replace("SHAPE_", "") for i, x in N.items() if x["type"] == "shape"))
print("  laws  :", ", ".join(i for i, x in N.items() if x["type"] == "law"))
print("  rules :", ", ".join(i for i, x in N.items() if x["type"] == "rule"))
print("  (details: --node <ID> | --type <t> | --grep <word>; sources in canon/Toolset/)")
print("\n### FINDINGS FROM HANDS-ON EXERCISES (read the caveats)")
for i, x in N.items():
    if x["type"] == "finding":
        show(i)
print("\n### OPEN QUESTIONS")
for i, x in N.items():
    if x["type"] in ("open_question", "task"):
        show(i)
print("\n### ARTIFACTS")
for i, x in N.items():
    if x["type"] == "artifact":
        show(i)
print("\n### DECISIONS RECORDED (Semantica context graph)")
for d in DG["nodes"]:
    if d["type"] == "Decision" or "outcome" in d.get("properties", {}):
        p = d["properties"]
        print(f"  - [{p.get('category')}] {p.get('scenario')}\n      => {p.get('outcome')} (conf {p.get('confidence')}): {p.get('reasoning')}")
print("\nNext: read canon/Toolset/* only for the section you need (--node refs point to sections). Do NOT start indicator work without operator permission.")
