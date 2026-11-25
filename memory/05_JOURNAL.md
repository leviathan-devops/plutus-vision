# 05 — JOURNAL (append-only stream: what I did, what I think, why; newest at the bottom)

## 2026-11-25
- 10:40 New brief on Fable 5.2: build E1 (then E2/E3) in Pine on top of V1, dynamic, Monday anchor, Pinebox-only verification. Container is fresh (old scratchpad gone; repo at d071f6c intact).
- 10:42 Unzipped 4 packages to /home/user/inputs. Pinebox = big bash CLI over "computer-use v2" + forked Pine IDE + backtest room + TradingView bar store (2025-02 -> 2026-11-06).
- 10:47 Installed Pinebox by hand (deploy.sh is git-gated): rsync 3 trees, bar store from pinebox-cloud/dist-web/data/bars, npm ci in pine-station, Chromium build 1734920 via @puppeteer/browsers.
  Blockers hit and fixed: `ss` missing (iproute2), `xdpyinfo` missing (x11-utils), Chromium refuses root (wrapper with --no-sandbox). `pinebox up --adapter xvfb` -> READY. Frame read.
- 10:50 Read operator rulings R-01..R-39 first-hand. Found the real oracles: golden-week screenshots (read 4 of 8 myself) and weekly reports on branch origin/handover.
- 10:55 Thought: the previous agents built Python pipelines and scored them with scripts; the operator's test is the chart. My loop must be: write Pine -> load in Pinebox -> shot -> read candles vs zones.
- 11:00 Launched 8 readers (workflow plutus-understand). Asked the operator 3+3 questions in his 5-minute window; answers in 04. Key correction: historical web data IS online (investinglive archives all 2026 expiries); I must build a fetching sidecar, not price-only E1.
- 11:10 Network hosts approved; OpenCode Go key saved (proxy-injected). investinglive/fed/opencode all answer 200.
- 11:20 Memory folder created. Reasoning on the "no hardcode" vs "web data" tension: the indicator source must hold no values; weekly external data enters as inputs written by the sidecar for the week being viewed.
  Unknown yet: how Pinebox passes inputs. To test.
- 11:30 Pinebox verbs exercised first-hand. IDE: `load` v1 on DXY 1H -> 20 boxes / 28 labels / 42 lines, all near the LAST bar (Nov 2026); navigating the IDE chart back to Jul 6-10 shows candles only (frame evidence/v1_baseline_DXY_1H_golden_week.png) -> an indicator that only draws "current state" is invisible on past weeks in the IDE tab.
  Backtest tab: `backtest --op create --name gw-dxy-jul06 --symbol DXY --start 2026-07-06T06:00 --end 2026-07-11 --tf 1H` puts the replay cursor at Mon Jul 6 06:00Z (bar 8751/10879) with all earlier bars visible = the Monday anchor simulated natively.
  EXPORT TO BACKTEST (IDE button at x=247,y=771) -> script appears in the room "ON CHART" (Indicators dialog), but V1 drew NOTHING on the room chart at the cursor (frame bt_003). Cause unknown yet (await PINEBOX_ENGINE_NOTES).
  Range buttons (1D/7D/1M...) under the charts CHANGE THE TIMEFRAME (1M -> 30m). Do not use them; use `tools/pb goto FROM TO [bt]`.
- 11:40 Read E1_ALGO.md digest in full (652 lines). Big findings: (a) seven E1 pillar blocks in v5.3.3 are "[unchanged from v4.5.2]" placeholders -> the missing text is in
  /home/user/handover-branch/Original_Canon_Data/TTE System Prompts/Trident_Trading_Engine_System_Prompt_v4.5.2 (1).md; (b) all tolerances are written in DXY points (cluster 0.15, tight 0.10, LSZ 0.05, wick 0.15, 4H zone max 0.40, 4H move >=0.5/3 days, D1 OB >=1.0/5 days); pair-unit tolerances are not in canon;
  (c) canon's own data boundary is Friday 17:00 ET; operator's live ruling is Monday London open (operator wins, both forbid in-week data); (d) zone names: RESISTANCE CEILING, UPPER RESISTANCE, EQUILIBRIUM ZONE, MID-RANGE SUPPORT, KEY SUPPORT BAND, LIQUIDITY SWEEP ZONE, BREAKOUT EXTENSION TARGET; score 0-14 -> EXTREME/HEAVY/MODERATE-HEAVY/MODERATE/LIGHT/MINIMAL.
  (e) Without options/analyst data the score ceiling is 10 (HEAVY) -> the web sidecar is what lifts zones to EXTREME; consistent with the operator's order to fetch it.
- 12:05 Read report oracles + handover 2.3. Design reasoning for E1 v0 (mine): candidate = structural price anchor (D1 swing extremes with rejection wick, repeated extremes/role reversals, prior week H/L/C, prior daily closes, 4H origin-candle S/D edges, D1 order blocks).
  Score each candidate on the six canon dimensions by coincidence: Technical 2 if a pivot/MA within 3 pips, 1 if within 10 pips; Psychological 2 on .00/.50, 1 on .25/.75; Structural 2 exact anchor + extreme, 1 proximity; Options/Analyst from the sidecar week file; Regime from the P9 classifier (await v4.5.2 text); + structural-extreme bonus <= 2.
  Zone = the anchor plus the levels that scored it (so width is the confluence, typically 0.05-0.15), kept when degree >= MODERATE (6). No count cap anywhere.
  All higher-TF data aggregated in-script; forecast frozen at the Monday 02:00 NY bar; drawn for `weeks to draw` (default 2 = R-36); IDE on 4H has full history (2832 bars) for walk-forward viewing of every week; Backtest tab for exact replay.
- 12:10 Waiting on: v4.5.2 fill (P5 steps 1-5, P6, P9), handover digest, engine notes, golden-week numeric read, laws digest, sidecar scout, omnigraph. Starting the Pine scaffold now (aggregation, anchor, week frame) — it does not depend on them.
