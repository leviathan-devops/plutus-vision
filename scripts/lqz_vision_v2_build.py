#!/usr/bin/env python3
"""
lqz_vision_v2_build.py — DELIVERABLE: plutus-vision-v2.pine.

THE INVARIANT: v1 IS NOT TOUCHED. The pin says "ADD ONLY — the V1 baseline is
untouchable. `ST-9` / `ST-9b` are the mechanism; intention is not a control."

So this is NOT the v1 build with extra modules bolted on. It is a SEPARATE artifact
that CONTAINS v1 verbatim and then adds the two engines:

    plutus-vision-v1.pine   (sealed, sha 0d20e8314ce992fc — READ ONLY, never rewritten)
      + plutus-vision-lqz/e1-render.pine     the institutional pressure map
      + plutus-vision-lqz/e2-render.pine     the predicted price path

v1's three protected layer counts (LuxAlgo SMC 226 · SMC order blocks 6 · LQZ
bands 4) must read identically in v2 — that is ST-9, and ST-9b diffs the two
v1 modules against the sealed checkpoint byte-for-byte.

THE E1/E2 PAYLOADS: the engines are PYTHON. This script injects their OUTPUT as
Pine literals at build time, so the shipped .pine is self-contained and Pine never
computes a confluence or a shape. An empty payload renders nothing and says why —
it never invents a zone or a path.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

V1 = ROOT / "plutus-vision-v1.pine"
E1 = ROOT / "plutus-vision-lqz" / "e1-render.pine"
E2 = ROOT / "plutus-vision-lqz" / "e2-render.pine"
OUT = ROOT / "plutus-vision-v2.pine"
DATA = pathlib.Path(os.environ.get("PV2_DATA_DIR", ROOT / "data" / "e1"))

# the v1 seal. The build REFUSES to run if v1 has drifted.
V1_SEALED_SHA = "0d20e8314ce992fc23e27f1b97fed76b981c84e78c647bbe6b3d6e1206517bd1"
V1_FLOOR = {"smc": 226, "ob": 6, "lqz": 4}


def _lines_matching(text: str, pattern: str) -> int:
    import re
    rx = re.compile(pattern)
    return sum(1 for ln in text.splitlines() if rx.search(ln))


def verify_v1_untouched() -> str:
    import hashlib
    raw = V1.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    if sha != V1_SEALED_SHA:
        raise SystemExit(
            f"HARD STOP H1 — v1 HAS MOVED.\n  sealed: {V1_SEALED_SHA}\n  on disk: {sha}\n"
            f"  The pin's rule is ADD ONLY. v1 is never rewritten by this build; if it "
            f"drifted, another process changed it, and this build will not paper over that.")
    txt = raw.decode()
    counts = {
        "smc": _lines_matching(txt, r"pv_alerts|smc_"),
        "ob": _lines_matching(txt, r"smc_storeOrdeBlock|smc_drawOrderBlocks"),
        "lqz": _lines_matching(txt, r"lqzColorLq|f_lqzRender"),
    }
    bad = {k: (v, V1_FLOOR[k]) for k, v in counts.items() if v != V1_FLOOR[k]}
    if bad:
        raise SystemExit(f"HARD STOP H1 — v1 layer counts moved: {bad}")
    return sha


def _pin(name: str) -> str:
    """Read the injected literal for `name`, or an empty array when the engine
    produced nothing. EMPTY IS A VALID ANSWER — the engine refusing is not a build
    failure, it is a result, and the render shows the refusal on the chart."""
    return f"{name} = array.from({DATA.joinpath('injected.txt').read_text().strip()})" \
        if (DATA / "injected.txt").exists() else f"{name} = array.from(_empty_payload)"


def build_payload() -> tuple[str, str]:
    """Assemble the E1/E2 payload as TYPED ARRAYS plus a refusal string.

    AN EMPTY OR MISSING INPUT PRODUCES EMPTY ARRAYS AND A REFUSAL — never a
    placeholder. A placeholder zone on a trading chart is a fabrication with a
    coordinate.

    TYPED ARRAYS, NOT `array.from([...])`. Measured 2026-10-03: an injected
    `array.from([])` literal FAILS the PineTS transpiler with "Syntax error at input
    '['" — an empty list carries no element type to infer from. v1 already compiles
    using `array.new<T>()` + push, so the payload uses exactly that shape."""
    zones: list[dict] = []
    refusal = ""
    for f in sorted(DATA.glob("*.json")):
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        zones.extend(d.get("zones", []))
        if not d.get("zones") and not refusal:
            refusal = ("E2_NO_ZONES: the E1 data file carries no zone array — the "
                       "fetch layer recorded every source as [NO DATA] for this week")
        break

    decls: list[str] = []
    pushes: list[str] = []

    def add(name: str, ty: str, vals) -> None:
        decls.append(f"var array<{ty}> {name} = array.new<{ty}>()")
        for v in vals:
            pushes.append(f"{name}.push({v})")

    add("e1_injected_top", "float", [z.get("top", 0) for z in zones])
    add("e1_injected_bottom", "float", [z.get("bottom", 0) for z in zones])
    add("e1_injected_confluence", "int", [int(z.get("confluence", 0)) for z in zones])
    add("e1_injected_zfp", "int", [int(z.get("zfp", 0)) for z in zones])
    add("e1_injected_id", "string", [f'"{z.get("name", "Z")}"' for z in zones])

    # the E2 arrays start EMPTY unless the engine ran. The refusal is carried as a
    # string, so an absent chain is stated on the chart instead of silently vanishing.
    for n, ty in (("e2_injected_x", "float"), ("e2_injected_y", "float"),
                   ("e2_injected_shape", "string"), ("e2_injected_conf", "int"),
                   ("e2_injected_ghost_x", "float"), ("e2_injected_ghost_y", "float")):
        decls.append(f"var array<{ty}> {n} = array.new<{ty}>()")

    # THE ANCHOR is computed HERE, in Python, because the PineTS transpiler has
    # neither `str.split` nor `tonumber` (measured 2026-10-03: "tonumber is not
    # defined", and v1 has zero uses of either). The engine owns the calendar; Pine
    # only draws. The Monday is derived from the target week's ISO date, never
    # hard-coded — a pinned timestamp makes the indicator right for one week only.
    anchor_ms, week_tag = _monday_anchor()
    decls.append(f"e1_injected_anchor_ms = {anchor_ms}")
    decls.append(f'e1_injected_week_tag = "{week_tag}"')

    # THE REFUSAL STRING. The E2 module READS it, so it must be declared even when
    # the engine produced a chain. An absent chain is STATED on the chart, never
    # silently swallowed — a silently empty chart reads as "the engine found nothing",
    # which is a different claim from "the engine refused to guess".
    refusal_lit = refusal or (
        "E2_NO_CHAIN: run scripts/e2_engine.py against a populated zone map; the "
        "forecast path stays empty until it has zones to anchor to")
    decls.append(f'e2_injected_refusal = "{refusal_lit}"')
    return "\n".join(decls), "\n".join(pushes)


def _monday_anchor() -> tuple[int, str]:
    """The target Monday in milliseconds, and its ISO week tag.

    Read from data/e1/<pair>-<week>.json when present (PHASE 1 wrote it); otherwise
    derived from the newest file name on disk. NEVER a literal — the whole point of
    the change is that a pinned date is the Temporal Boundary violation."""
    import datetime as _dt
    tag = ""
    files = sorted(DATA.glob("*.json"))
    if files:
        m = re.search(r"(\d{4}-\d{2}-\d{2})", files[0].stem)
        if m:
            tag = m.group(1)
    if not tag:
        return 0, "no anchor"
    d = _dt.date.fromisoformat(tag)
    mon = d - _dt.timedelta(days=d.weekday())          # the Monday of that week
    iso = mon.isocalendar()
    ms = int(_dt.datetime(mon.year, mon.month, mon.day).timestamp() * 1000)
    return ms, f"{iso[0]}-W{iso[1]:02d}"

def strip_decl(src: str, names: list[str]) -> str:
    import re
    out = []
    for ln in src.split("\n"):
        if any(re.match(rf"^{n}\s*=\s*array\.from\(", ln) for n in names):
            continue
        out.append(ln)
    return "\n".join(out)


E1_NAMES = ["e1_injected_top", "e1_injected_bottom", "e1_injected_confluence",
            "e1_injected_zfp", "e1_injected_id"]
E2_NAMES = ["e2_injected_x", "e2_injected_y", "e2_injected_shape", "e2_injected_conf",
            "e2_injected_ghost_x", "e2_injected_ghost_y", "e2_injected_refusal"]


def build() -> str:
    sha = verify_v1_untouched()
    v1 = V1.read_text()
    e1 = strip_decl(E1.read_text(), E1_NAMES)
    e2 = strip_decl(E2.read_text(), E2_NAMES)
    decls, pushes = build_payload()
    return (
        v1.rstrip() + "\n"
        + "\n// ═════════════ E1 — the institutional pressure map (ADDED 2026-10-03) ═════════════\n"
        + "// The payload below is produced by e1_fetch/e2_engine and injected at build time.\n"
        + "// Typed arrays (array.new<T>() + push), NOT array.from([...]) — an empty list\n"
        + "// literal carries no element type and the PineTS transpiler rejects it.\n"
        + f"{decls}\n"
        + (f"\n{pushes}\n" if pushes else "")
        + "\n"
        + e1 + "\n\n"
        + "// ═════════════ E2 — the predicted price path (ADDED 2026-10-03) ═════════════\n"
        + e2 + "\n"
    )


if __name__ == "__main__":
    out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else OUT
    txt = build()
    out.write_text(txt)
    print(f"wrote {out.name}  {len(txt.splitlines())} lines  (v1 verified untouched)")