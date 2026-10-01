#!/usr/bin/env python3
"""lqz_luxalgo_build.py — DELIVERABLE 1: the three LuxAlgo liquidity detectors bundled
behind ONE full-width display.

Design: plutus-vision-v0.pine is the base, so the three detectors are the ORIGINAL LuxAlgo
code, byte-identical. Three scalar taps are injected adjacent to the sites where each
detector acts; the detectors keep drawing their own primitives (their detection and their
own visuals are untouched — that is what keeps them at parity), and the taps feed the
shared lqzSink so LQZ can emit ONE consolidated full-width zone where they concur.

  python3 scripts/lqz_luxalgo_build.py [out.pine]
"""
import pathlib, re, sys

W = pathlib.Path(__file__).resolve().parent.parent
SRC = W / "plutus-vision-v0.pine"
CORE = (W / "plutus-vision-lqz/lqz-core.pine").read_text()
RENDER = (W / "plutus-vision-lqz/lqz-render.pine").read_text()

# scalars the taps write and the accessors read
SCALARS = """
// ═════════════════════════════════════════════════════════════════════════════
// LQZ V1 TAPS — the LuxAlgo detectors keep their own detection AND their own
// drawings; these scalars record the price each one acted on so the shared
// cluster can emit ONE consolidated full-width zone where they concur.
var float lqzV1Mid  = na
var float lqzV1Rail = na
var float lqzV1Swp  = na
var float lqzV1VLo  = na
var float lqzV1VHi  = na

lqzV1PoolMid()  => lqzV1Mid
lqzV1PoolRail() => lqzV1Rail
lqzV1SweepPrc() => lqzV1Swp
lqzV1VoidLo()   => lqzV1VLo
lqzV1VoidHi()   => lqzV1VHi
"""

TAIL = """
// ── consolidate: one full-width zone per confirmed level cluster ──────────────
if barstate.islast
    f_lqzRender()
"""


def inject(t: str, anchor: str, before: str, name: str, want: int = 1) -> str:
    got = t.count(anchor)
    if got != want:
        raise SystemExit(f"tap {name}: anchor matched {got}x, need exactly {want}")
    return t.replace(anchor, before + anchor)


def build(out: pathlib.Path) -> str:
    t = SRC.read_text()

    # the LQZ source selector must not shadow v0's own LuxAlgo detectors
    t = t.replace('indicator(\'Plutus Vision v0\'', 'indicator(\'LQZ LuxAlgo — three liquidity detectors, one display\'', 1)

    # ── POOLS: capture the clustered pivot's zone centre and margin ─────────────
    t = inject(t,
        "            if not na(bsl_getB.bx) and bsl_st_B == bsl_getB.bx.get_left()",
        "            if not na(bsl_minP)\n"
        "                lqzV1Mid := math.avg(bsl_minP, bsl_maxP)\n"
        "                lqzV1Rail := bsl_atr / bsl_liqMar\n",
        "POOLS", want=2)

    # ── VOIDS: capture the unfilled FVG's two edges ────────────────────────────
    t = inject(t,
        "    if voi_bull \n",
        "    if voi_bull and not voi_bull[1]\n"
        "        lqzV1VLo := voi_b.l[1]\n"
        "        lqzV1VHi := voi_b.h[2]\n"
        "    if voi_bull \n",
        "VOIDS-bull")
    t = inject(t,
        "    if voi_bear\n",
        "    if voi_bear and not voi_bear[1]\n"
        "        lqzV1VLo := voi_b.l[1]\n"
        "        lqzV1VHi := voi_b.h[2]\n"
        "    if voi_bear\n",
        "VOIDS-bear")

    # ── SWEEPS: capture the swept pivot price ─────────────────────────────────
    # the state machine marks a pivot taken inside swp_update; tapping that method
    # body keeps the capture exactly where the sweep is recognised.
    anchor = "method swp_line(swp_piv swp_get, color c, string s='sd') => \n"
    t = inject(t, anchor,
        anchor + "    lqzV1Swp := swp_get.prc\n",
        "SWEEPS")

    # ── drop the CORE's own input block; v0 already owns those names ──────────
    t = re.sub(r'lqzSource\s*=\s*input\.string\("both",[^\n]*\n', 'lqzSource = "both"\n', t)
    t = re.sub(r'lqzTol\s*=\s*input\.float\([^\n]*\n', 'lqzTol = 0.5\n', t)
    t = re.sub(r'lqzMinAgree\s*=\s*input\.int\([^\n]*\n', 'lqzMinAgree = 2\n', t)
    t = re.sub(r'lqzMaxZones\s*=\s*input\.int\([^\n]*\n', 'lqzMaxZones = 60\n', t)
    t = re.sub(r'lqzMaxLevels\s*=\s*input\.int\([^\n]*\n', 'lqzMaxLevels = 1500\n', t)
    for pat in (r'lqzSwingLen\s*=\s*input\.int\([^\n]*\n', r'lqzWickMult\s*=\s*input\.float\([^\n]*\n',
                r'lqzReject\s*=\s*input\.float\([^\n]*\n', r'lqzRejectWin\s*=\s*input\.int\([^\n]*\n'):
        t = re.sub(pat, "", t)

    return t + CORE[CORE.index("\n// ════", CORE.index("// THE CONFIRMATION")):] if False else _join(t, CORE, RENDER)


def _join(t: str, core: str, render: str) -> str:
    # core's header comment is redundant here; keep the state + V2 + V1 + cluster
    # Keep core's INPUT declarations: the header slice would otherwise drop
    # lqzSource/lqzTol/lqzMinAgree/lqzMaxZones/lqzMaxLevels and the file fails
    # at runtime with "lqzTol is not defined".
    body = core[core.index("// ── inputs ──"):]
    # v0 is already 'both'; the V1 tap inside core is unused (scalars feed it instead)
    body = re.sub(r"lqzV1Enabled = lqzSource == \"luxalgo\" or lqzSource == \"both\"\nif lqzV1Enabled\n(?:.+\n)*?\n", "", body, count=1)
    # SCALARS must be emitted HERE: v0 has no LQZ header marker, so injecting into
    # `t` was a silent no-op and the accessors stayed undefined -> the run failed at
    # runtime with "lqzV1SweepPrc is not defined".
    return SCALARS + "\n" + t + "\n" + body + "\n" + render + TAIL


if __name__ == "__main__":
    out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else W / "lqz-luxalgo.pine"
    out.write_text(build(out))
    print(f"wrote {out.name}  {len(out.read_text().splitlines())} lines")