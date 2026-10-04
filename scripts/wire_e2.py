#!/usr/bin/env python3
"""
wire_e2.py — run the E2 engine over an E1 zone map and emit the Pine payload.

THE PATH THE PIN REQUIRES:
    data/e1/<pair>-<week>.json   (zones, from the fetch layer)
        -> scripts/e2_engine.py  (classify -> chain -> day decomposition)
        -> the build injects day x/y/shape/conf + the alternative ghost

Every value here is COMPUTED by the engine, never invented here. If the engine refuses
— no zones, all-MINIMAL, no signature matched — this script writes an EMPTY payload and
the refusal string, and the render states it on the chart. That is the anti-theatre
contract: a chain with no anchoring zone is never drawn.

    python3 scripts/wire_e2.py [--data DIR] [--week YYYY-MM-DD] [--dry-run]
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from e2_engine import (  # noqa: E402
    Zone, forward_map, consolidation_phase, FabricationRefused)

DAY_MS = 86_400_000


def load_zones(data_dir: pathlib.Path) -> tuple[list[Zone], str]:
    """Read the E1 zone map. Returns (zones, refusal)."""
    files = sorted(data_dir.glob("*.json"))
    if not files:
        return [], "E2_NO_DATA: no E1 data file — run scripts/e1_fetch.py first"
    doc = json.loads(files[0].read_text())
    raw = doc.get("zones", [])
    if not raw:
        return [], ("E2_NO_ZONES: the E1 data file carries no zone array — the fetch layer "
                    "recorded every source as [NO DATA] for this week")
    zones = []
    for z in raw:
        conf = int(z.get("confluence", 0))
        if conf < 4:                      # MINIMAL — the canon discards a score of 0-3
            continue
        zones.append(Zone(
            id=z.get("name", "Z"),
            top=float(z.get("top", 0)),
            bottom=float(z.get("bottom", 0)),
            confluence=conf,
            zfp=int(z.get("zfp", 0)),
            timeframe=z.get("timeframe", "1H"),
            bom=z.get("bom", ""),
            reactions=int(z.get("reactions", 0)),
        ))
    if not zones:
        return [], ("E2_ALL_MINIMAL: every zone scored below 4; the canon discards a "
                    "confluence of 0-3, so there is nothing to anchor a shape to")
    return zones, ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=str(ROOT / "data" / "e1"))
    ap.add_argument("--week", default="", help="the target Monday, ISO (default: from the filename)")
    ap.add_argument("--out", default=str(ROOT / "data" / "e2"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    data_dir = pathlib.Path(args.data)
    files = sorted(data_dir.glob("*.json"))
    week = args.week
    if not week and files:
        for part in files[0].stem.split("-"):
            if len(part) == 4 and part.isdigit():
                week = "-".join(files[0].stem.split("-")[-3:])
                break
    if not week:
        print("  no target week resolved; pass --week YYYY-MM-DD")
        return 2
    monday = dt.date.fromisoformat(week)

    zones, refusal = load_zones(data_dir)
    out = {"week": week, "monday": monday.isoformat(), "zones_in": len(zones),
           "refusal": refusal, "days": [], "ghost": []}

    if not refusal:
        try:
            chain = forward_map(zones, 1.0, monday)
            if chain.refusal:
                out["refusal"] = chain.refusal
            else:
                # The x of each day: the Monday plus the session offset. The +1 day is the
                # canon's §6.10 Trading Speed Rule, already applied by the engine.
                for i, d in enumerate(chain.days):
                    dx = dt.date.fromisoformat(d["date"])
                    out["days"].append({
                        "x": int(dt.datetime(dx.year, dx.month, dx.day).timestamp() * 1000),
                        "shape": d["shape"],
                        "conf": d["confidence"],
                        "zone": d["key_zone"],
                        "day": d["day"],
                    })
                for l in chain.alternative:
                    out["ghost"].append({"zone": l.trigger_zone_id, "to": l.to_shape,
                                         "zfp": l.trigger_zone_zfp, "conf": l.confidence})
                out["chain"] = [f"{l.from_shape}->{l.to_shape}@{l.trigger_zone_id}"
                                for l in chain.chain]
                out["phase"] = chain.consolidation_phase
        except FabricationRefused as e:
            out["refusal"] = str(e)

    if args.dry_run:
        print(json.dumps(out, indent=1))
        return 0

    outdir = pathlib.Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    p = outdir / f"{files[0].stem if files else 'EURUSD'}-e2.json"
    p.write_text(json.dumps(out, indent=1))
    try:
        shown = p.relative_to(ROOT)
    except ValueError:
        shown = p
    print(f"  wrote {shown}")
    print(f"  zones_in={out['zones_in']}  days={len(out['days'])}  "
          f"ghost={len(out['ghost'])}  refusal={out['refusal'] or 'none'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())