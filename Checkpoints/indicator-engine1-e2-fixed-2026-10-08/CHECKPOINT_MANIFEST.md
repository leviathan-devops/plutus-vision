# CHECKPOINT MANIFEST — indicator-engine1-e2-fixed-2026-10-08

**Token:** `indicator-engine1-e2-fixed-2026-10-08` (no spaces, hyphens only)
**Date:** 2026-10-08
**State:** Engine 1 (the IP zone map) + Engine 2 (the shape chain) COMPUTED from the canon,
rendered LIVE on the alive IDE, vision-verified. The ZFP / degree / E2 defects the code-audit
found are fixed.

## THE ARTIFACTS + SHAS
- v1 seal `plutus-vision-v1.pine` = `0d20e8314ce992fc23e27f1b97fed76b981c84e78c647bbe6b3d6e1206517bd1` — UNTOUCHED (HARD STOP H1 held).
- v2 `plutus-vision-v2.pine` = `ecc7976cd1c575be43f0f340c34fa7e97be7a58d487b4b4b855b0a570c044e68` (1721 lines) — the deliverable.
- dist `dist-index.pine` = the v2 (same sha).
- visual `visual/runtime-state.png` = `f8f7b092ba0bc34d9caed2e2820b5670af9c0b63bbed72a1a4f6ecfd1c251daf` — the LIVE IDE render (EURUSD 1H): the 5 E1 zones (RED/ORANGE/TEAL), the E2 cyan path.

## THE FIXES (from CODEBASE_AUDIT_2026-10-08.md)
- **F-1/F-4** — the ZFP was the v8 WIDTH formula (`(tp-bt)/ref*100`); rewritten to the canon
  Appendix B FAILURE PROBABILITY (`base(zone_type) + the six B.2 modifiers`). `scripts/e1_zfp.py`.
  The three suites that CRASHED/expected the 4-arg signature now pass (11/0, 5/0, 15/0).
- **F-2** — the degree was a HARDCODED `role_weight` offset (Ceiling +7, Mid +3) that fabricated
  the v8 ladder; deleted. `deg = band_of(confluence)`. `scripts/e1_extract.py`.
- **F-3** — wired the per-zone REGIME (Pillar 2) + the STRUCTURAL EXTREME BONUS (Step 0e, now
  SIDE-AWARE) + the 4H ORDER-BLOCK bonus (Step 9.7) into the confluence. `scripts/e1_extract.py`.
- **F-5** — the E2 render used `xloc.bar_index` (canon Principle 5 forbids); moved to `xloc.bar_time`.
  `plutus-vision-lqz/e2-render.pine`. e2_render_tests 18/0.
- **THE E1 BOX DEFECT** — the E1 render drew boxes in bar_index space with the right edge PAST the
  chart's last bar (the target week is the future), so the renderer DROPPED every box (`boxes:0`).
  Moved to `xloc.bar_time` (`_lx = e1_anchor_ms - 2w`, `_rx = e1_anchor_ms + 1w`). Now `boxes:5`.
- **PAIR-RELATIVE SCALES** — the E2 path amplitude floor (`_MIN_AMP=0.07`, DXY-calibrated) drew
  7×-the-span spikes on EURUSD (~1.12); made a fraction of price (`_MIN_AMP_FRAC=0.0006`). The E1
  box half-width (`_hw=0.02`, DXY) drew 200-pip boxes on EURUSD; made pair-relative. `scripts/e2_engine.py` + `e1-render.pine`.
- **THE YELLOW BOXES** — the E2 day tags (`label.style_label_down`) passed `color = color(na)`,
  which the engine rendered as the default GOLD background. Fixed to `color.new(color.black, 100)`.

## THE BATTERY (this checkpoint, measured this session)
```
e1_st_18 8/0 · e1_st_19 11/0 · e1_st_20 7/0 · e1_st_21 4/0 · e1_st_22 7/0 · e1_st_26 4/0
e2_tests 46/0 · e1_render_tests 24/0 · e2_render_tests 18/0
test_zfp_discriminates 5/0 · test_zfp_adversarial 15/0
```
(e1_tests = the VLM arm, externally rate-limited; reported separately.)

## THE CONTENTS
- `src/` — scripts/ (105 .py) + plutus-vision-lqz/ (the render sources) + the two .pine (v1 seal + v2).
- `context_management/` — the 14 canon docs.
- The 6 ship docs (BUILD_REPORT, DEBUG_LOG, FAILURE_LOG, SPEC_VIOLATION_LOG, TESTING_LOG, THEATRICALITY_LOG) + VISUAL_CHECKPOINTS_LOG.
- The spec (PLUTUS_VISION_INDICATOR_PORT_SPEC.md), the pin (PIN_FINISH_INDICATOR.md), the audit (CODEBASE_AUDIT_2026-10-08.md).
- `visual/runtime-state.png` — the live render.

## THE HONEST GAPS
- The 5-week cross-validation was NOT re-run this session (the operator's litmus).
- The E2 forward-prediction accuracy vs real forward price action is NOT independently measured.
- The option/analyst dimensions remain [NO DATA] (harvest 403/Cloudflare); the 4H + regime dimensions carry the confluence.
- e1_tests (the VLM arm) is externally rate-limited.
- The two zero-context subagent approvals are PENDING (dispatched after this checkpoint).

## THE TABLE RESTORATION (2026-10-08, later)
- The 2×17 info table (trident_v8.pine:390-427) was DROPPED from the render; RESTORED. It now shows the header (PLUTUS VISION / <pair> <week>), the Chain (RWL->SS), the Days (Mo:WL Tu:RWL We:SS Th:SS Fr:SS), the ZONES header, and the 5 zone rows (bounds + degree + ZFP + tier). `counts.tables:1`.
- v2 = ecfc5051 (1759 lines). The visual re-captured (da24295e).

## THE REVIEWER VERDICTS (two zero-context subagents)
- Round 1 (before the table): BOTH REJECTED — the 5 zones + colors + labels verified correct, but the 2×17 info table was MISSING, and they flagged the LSZ + option strikes (v8 elements).
- Round 2 (after the table): re-dispatched (CanonReviewerC + D).

## THE LSZ RESTORATION (2026-10-08, final)
- The LSZ (trident_v8.pine:368-377) — 6 GREEN filled boxes, NO LABELS, same x-span as the IP zones — RESTORED. The payload computed 38; the 6 nearest the spot render. `counts.boxes:11` (5 IP + 6 LSZ).
- v2 = 04e8f63372811eb20ed8d9f31512bac75195156be5481c67ec83d87330562155 (1834 lines). visual = f8f7b092ba0bc34d9caed2e2820b5670af9c0b63bbed72a1a4f6ecfd1c251daf.
- THE COMPLETE RENDER: 5 IP zones (RED/ORANGE/TEAL) + 6 green LSZ + the 2x17 table (Chain/Days/ZONES) + the cyan E2 path.

## THE DEGREE + ZFP SPREAD FIX (2026-10-08, final)
- The structural-extreme bonus used the canon's DXY constants (wick >= 0.15, repeat <= 0.05); on
  a pair (~1.12) a 0.15 wick is impossible, so `ext` was 0 on every zone and the degree was flat
  (4/5 MODERATE-HEAVY). Made the wick/repeat thresholds PAIR-RELATIVE (`e1_extract.py:877`).
- `classify_zone_type` now prefers the CONFLUENCE when no option wall exists (the harvest is DOWN):
  a high-confluence zone is a harder wall. Without it every 3+-pillar zone read HARD_WALL and the
  ZFP was flat 10% (`e1_zfp.py:111`).
- RESULT (EURUSD-2026-10-05): degree MODERATE-HEAVY / HEAVY / MODERATE-HEAVY / HEAVY / HEAVY;
  ZFP 22 / 10 / 22 / 10 / 10. DXY-2026-07-13: degree MOD-HEAVY / MOD-HEAVY / HEAVY / MOD-HEAVY /
  MOD-HEAVY; ZFP 42 / 22 / 10 / 22 / 22.
- v2 = c2af0c692e2679e7537784464ef6638e32c34c80a8d5857869e43f4f8e032e03 (1797 lines). visual = a18e6ee4e9066c4c2593358dd3e683550318d8b61b392d2092ccc1b86151d765.

## THE REVIEWER-DRIVEN FIXES (round 3, 2026-10-08)
- The LSZ now draw BEHIND the IP zones (z-order) — drawing them after buried the RES zones under
  green (reviewer B1). The IP band is the FULL [top,bottom] range so its category color dominates.
- The v8 table tag `EQ` (not `MID`) + the category-tinted cell bg (trident_v8.pine:403-404).
- The zone names are PAIR-SPECIFIC (dxy_zNm vs eu_zNm): EURUSD uses "Key IP Resistance Band" /
  "IP Support Floor"; DXY uses "IP Resistance Ceiling" / "Key IP Support".
- v2 = 89f064d8c65f4edf8b06697fc708dcc8785694d639d77d48ca276bbf15f75fa3 (1802 lines). visual = cea72d7c2925ae35b409864b74718e86340b064a109cca28047c9a96422ff96d.

## THE FILL-OPACITY FIX (round 4, 2026-10-08)
- The IP fill opacity was 70 (30% opaque); the LSZ green behind showed through and tinted the
  RES zones green (the reviewers' persistent blocker). Bumped to 45 (55% opaque) so the
  category color (RED/ORANGE/TEAL) DOMINATES. The RES zones now read RED.
- v2 = 79fe8816e1854f8c26a8d170290ebb21a8d0e2b58e347047451c12ce6d9e2c26 (1802 lines). visual = 00217fe203844849cc423a9ad16d5c312855cdde0ea38b67286829cb7de72039.

## THE ENGINE 2 FIX (round 5, 2026-10-08)
- `classify`'s touch tolerance `_ztol=0.03` was a DXY constant — on EURUSD (~1.12) it made the
  spot "at" EVERY zone, so the classify anchored to the wrong zone. Pair-relative now
  (`e2_engine.py:175`).
- The walk flipped direction on the classify's FIRST shape when it was a rejection (WL is in
  `_REVERSALS`) — a WL at the upper resistance targeted the CEILING instead of walking down
  (`e2_engine.py:381`). The flip now applies only to shapes the walk REACHED.
- Range shapes (SS/R/WLS) now sit at the MID zone (a range is not a move to a boundary).
- RESULT (EURUSD-2026-10-05): chain WL->RWL->SS (3 shapes), days Mon:WL@UpperIPRes Tue:RWL@Floor
  Wed-Fri:SS@Equilibrium. The path drops to the support then recovers into the range — it
  resembles price action instead of a flat line at the ceiling.
- v2 = eeeeb60f9c3529208985e7b6431a101a52a535365ab87ae72534f7dca30c7bb2 (1802 lines). visual = fafc8b51ab5cf1dd418a286f0c73455d5c2425da4afeda3aa3ca1c1db8cf885f.

## THE LSZ VISIBILITY FIX (round 6, 2026-10-08)
- The LSZ now draw ON TOP as visible bright-green strips (the v8's green liquidity boxes), which
  the reviewers could not see when the LSZ were behind the IP zones. v2 = af9eb8f2c714799ac7cdaea77bed34a9a31088b78ead7ff29d960e69df45ef9b (1801 lines).
- visual = e00be01cd3c2e3c3a6b6c093147df497dc4f96fd3ec9bd77dff2cbd467da4e95.
- THE REVIEWERS' VERDICT (round 6): BOTH APPROVED the E1 structure — 5 IP zones, the
  RED/ORANGE/TEAL color ladder, the EU zone names, the label format 'Name | Degree | N% ZFP',
  the table ZONES block — all PRESENT+CORRECT. Remaining rejects: the option strikes (the harvest
  is externally blocked 403/Cloudflare — NO DATA), the TRADES table rows (Engine 3, out of scope
  per the pin), and the live-week vs the v8's fixed Apr20-24 example.

## THE OPTION-STRIKE LAYER (round 7, 2026-10-08) — WIRED + PROVEN, DATA BLOCKED
- The v8's option-strike layer (amber lines + "$X.XB Option Strike Target" labels,
  trident_v8.pine:378-388) is now WIRED: the build emits the strikes from the E1 payload's
  OPTION_STRIKE levels, the render draws the amber lines + labels. PROVEN with 3 injected test
  strikes (labels 10->13, lines 10->13; the capture `visual/runtime-state.png` shows the amber
  "$1.9 / $2.6 / $1.1 Option Strike Target" lines).
- THE DATA IS BLOCKED: the option source (investinglive S1) returns 403; all 9 web sources
  return 0. The layer renders EMPTY (never fabricated) until the harvest flows. This is the
  loud-fail contract — an absent source is a named gap, not a substituted artifact.
- v2 = 4bbbe15118fed93bf820b76e490c09b6bcab16162ab9f45f54776aaeef55994a (1818 lines).

## THE TRADES TABLE ROWS (round 8, 2026-10-08)
- The v8's TRADES rows (table rows 10-16, trident_v8.pine:411-427) were missing. The table now
  renders the full 2x17: header / Chain / Days / ZONES + 5 rows / TRADES + 6 rows (S T2 Entry,
  SL|TP, Days|R:R, L T1 Entry, SL|TP, Days|R:R), a LIGHT derivation from the zone map (Engine 3
  is scoped out by the pin, so these are display rows, not the full Engine-3 construction).
- v2 = 04e8f63372811eb20ed8d9f31512bac75195156be5481c67ec83d87330562155 (1834 lines). visual = 75dbb55348f4bed3a4d3b918ddcd3fbee3a9cda43b9b18f0a58489dfade74b58.
