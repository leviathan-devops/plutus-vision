# 02 — TASK QUEUE (overwrite as it changes; status: TODO / DOING / DONE / BLOCKED)

| id | status | task | done-when |
|---|---|---|---|
| T1 | DOING | Pinebox running + drivable | I have loaded a script, navigated to a past week in IDE and Backtest tabs, and read the frames |
| T2 | DOING | Absorb canon/handover/oracles into digests; verify first-hand | 8 digest files exist and E1 key claims are checked against the prompt by me |
| T3 | TODO | Anchor guard: `tools/anchor_guard.py` + git pre-commit hook + log | A commit containing a lookahead construct or a price literal in `indicator/*.pine` is refused; refusals logged |
| T4 | DONE | Memory: OmniGraph installed, `tools/mem` add/query, seeded from memory/ | `tools/mem/mem q "<word>"` returns facts; rebuild script works from the repo alone |
| T5 | TODO | Web sidecar (aether + OpenCode Go, Muse Spark 1.3 Contributor, effort high): dated option-strike / analyst / H.10 harvest as of the Monday anchor -> one JSON per week per pair | Golden-week JSON produced from pages dated <= Mon 2026-07-06; anchor check passes |
| T6 | TODO | E1 in Pine on top of V1 (price pillars in Pine; web pillars from the weekly JSON) | Golden week DXY + EURUSD frames read; reaction score >= 90%; no literals |
| T7 | TODO | E1 held-out validation: report weeks + random weeks Feb 2026+ on DXY/EURUSD/GBPUSD | Scorecard with frames; uniform >= 90% or the honest number |
| T8 | TODO | E2 shape chain in Pine | Golden week chain matches realized path; held-out weeks scored |
| T9 | TODO | E3 trade setups (corrected spec), <= 11 per week per pair | Backtest fills: entry hit, SL not hit, TP hit — counted per week |
| T10 | TODO | Final report + publish evidence | Operator can open the indicator in Pinebox and reproduce |

## 2026-11-25 15:55 UTC - queue after the operator's E1 rejection (E2/E3 frozen by L-14)
1. [NEXT, after the usage reset] Multi-agent feature hunt (ultracode is on): can ANY forward rule lift "clean all week" above ~0.70 or week-extreme capture above ~0.55 on DEV and keep it on VALID?
   4 designers, different lenses, each a python prototype importing tools/research/score.py, DEV only: (a) approach dynamics (momentum / day-of-week / how price arrives), (b) option-expiry structure by day (walls, pins, ghosts, prior-week walls),
   (c) cross-pair agreement (DXY vs EURUSD vs GBPUSD bands), (d) higher-timeframe structure with other zone definitions (D1/W1 bases). Then one adversarial validator per design on VALID (lookahead audit + numbers). <= 8 agents.
   Already ruled out by me (do not repeat): confluence density, heavier stacked-anchor thresholds, older weekly extremes, prior-week direction conditioning, daily re-anchoring, per-level-type selection.
2. Whatever the hunt finds: port into f_bands, render the 8 TEST weeks x 3 pairs in Pinebox, look, ledger, show the operator.
3. Waiting on the operator: how he wants accuracy defined given that the W14 baseline was written with hindsight (see 01 STATE 15:45).
