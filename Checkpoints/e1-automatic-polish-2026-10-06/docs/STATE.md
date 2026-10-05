# PLUTUS VISION · E1 automatic — polish checkpoint (2026-10-06)

## ARTIFACT UNDER SEAL
- v1 seal (unchanged): 0d20e8314ce992fc23e27f1b97fed76b981c84e78c647bbe6b3d6e1206517bd1
- v2 (the render): 04d7a89ae57d1f9f29e8dbb428d93a306c3d66301b7c1a9e177d09abac65642b  (1735 lines)
- the served render: http://127.0.0.1:9851/plutus-vision-v2.pine (DXY, 1740 bars)

## WHAT THIS CHECKPOINT CARRIES (vs the 2026-10-05 ship checkpoint)
- E2 path: a CONTINUOUS jagged price line — fine_path() enabled (11 points/day-expansion), the
  render loops all segments (was a 5-vertex triangle).
- E1 zones: all 6 render (the price scale now spans the full zone range — the prediction band).
- Both layers coexist (the prior "cannot paint together" residual is resolved: the over-draw was
  the xloc=bar_time+loop form, not a renderer limit).
- census: 2 plots · 6 boxes · 101 lines · 2006 labels · 798 segs · bars 1740

## OPERATOR VERDICT (2026-10-06)
- "All right, not that this looks much better. Save the current checkpoints. We obviously still
  need to improve this. The E2 shape shade is improving, but still not there. ... The E1 zones
  look better ... fix the E2 shape chain line drawing."
- THE METHOD (operator): play forward the price action for the rest of the trading week, then map
  backwards to the E2 shape chain.

## OPEN (the next build)
1. Fix the E2 shape chain line drawing (the operator: "still not there").
2. Verify the E1 zone accuracy.
3. Close all gaps.

## 2026-10-06 (later) — THE E2 ROOT-CAUSE FIX + THE PLAY-FORWARD VERDICT
- THE OPERATOR'S METHOD (play the price forward, map the E2 back) FOUND TWO HARDCODED DEFECTS:
  1. wire_e2.py passed bars_momentum = 1.0 (a CONSTANT). Now derived from the chart's own bars
     (net move of the last 20 / mean true range): measured -0.1047 for DXY.
  2. classify() anchored to the FIRST zfp-20-40 zone (the LOWEST support) -> the walk could only
     travel UP and the E2 oscillated in the support band, never reaching the resistance the week
     actually rallied to (101.275). Now anchors to the mid-range zone nearest the spot (the EQ).
- THE ACTUAL WEEK (from the real TV feed): Mon 100.87 / Tue 101.19 / Wed high 101.275 (REJECTED at
  the Upper Resistance 101.28) / Thu 100.91 / Fri low 100.598 (BOUNCED off Key Support).
- mimo v2.6 flash VERDICT: the price action RESPECTS the zones (floor at the teal support,
  stall/reject at the orange resistance) - E1 zones ACCURATE. The E2 remains the open defect.
- v2 now: 6b3b4bf55522258d25b0a524e27085c7a0c3bc27963c136b3f7f6d0ed554da0a
- EVIDENCE: e2_tests pass=36 fail=0 · e1_st pass=8 fail=0 · v1 0d20e8314ce992fc
  · evidence/play-forward-DXY-jul6-11.mp4 (36 frames)
