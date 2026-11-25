# 08 — DURABLE FACTS (append; cite where each came from; never guess here)

## Inputs (all outside the repo; re-unzip from /root/.claude/uploads/b6c77a81-471c-536b-9631-0319cefbf3ab/ if lost)
- `/home/user/inputs/handover/PLUTUS_VISION_CONTEXT_HANDOVER/` — previous agent's handover (00_HANDOVER primary, 01_BINDING_SPEC, 03_HOST_BIBLES).
- `/home/user/inputs/pinebox/ship-approved-v2/` — Pinebox package (manual: src/manuals/OPERATOR_MANUAL_pinebox.md).
- `/home/user/inputs/canon/Toolset/` — same six canon files as repo `canon/Toolset/`.
- `/home/user/inputs/trades/WINNING_TRADE_LIBARARY/` — operator's annotated screenshots; `Jul_6-10_DXY_Gold_Standard/` = golden-week oracle (8 PNG, DXY + EURUSD 1h); `Original_Training_Data/*.pdf`.
- `/home/user/inputs/aether/aether_agent_backend_v2/` — framework for the embedded agent (L-11).
- `/home/user/handover-branch/` = git worktree of `origin/handover`: `Original_Canon_Data/` has the weekly report oracles
  (`IP Heatmap Reports/*.pdf` for Apr20-24, Apr27-May1, May 4-8, May25-29 2026; `Validated Trade Reports/Trident_Report_2026W14_Mar30-Apr3.md`; `Pine Scripts/trident_v8.pine`).
  Recreate: `git fetch origin && git worktree add -f /home/user/handover-branch origin/handover`.

## Pinebox (measured 2026-11-25)
- Up via `tools/pinebox-bootstrap.sh`; session `plutus-main`, instance 0, adapter xvfb display :3; ports station 9741, rail 9754, server 9851, CDP 9222, room 9443.
- Env for every command: `export PATH=$HOME/.local/bin:$PATH XDG_RUNTIME_DIR=/run/user/0`.
- Verbs: `pinebox shot --session plutus-main --out F.png [--section chart|plot]`, `load --pine F [--pair P --tf T]`, `asset --set EURUSD --tf 4H`, `tf --tf 30m`,
  `chart --op fit|zoom|pan|view`, `tab --to backtest|pine`, `backtest --op create|open|step|date|state ...`, `drive --action click|type|key`.
- Chromium must be wrapped with `--no-sandbox` (root). `ss`, `xdpyinfo` must be installed. The image judge (:8090) is absent -> `pinebox verify` cannot answer WORKS; I judge frames myself.
- Bar store `~/.local/share/pinebox/data/tv-bars/{TVC_DXY,FX_EURUSD,FX_GBPUSD}/{15,30,60,240}/YYYY-MM.json`, 2025-02-02 -> 2026-11-06 (TradingView bars). IDE chart = newest 5000 bars of a cell.
- First frame read (frames/pb_000_boot.png): PINE IDE tab with editor (RUN, CAPTURE, EXPORT TO BACKTEST, GATE buttons), DXY 1h chart Aug->Nov 2026, BACKTEST tab at top.

## Web data + model (measured 2026-11-25)
- `curl https://investinglive.com/` -> 200 (708 kB) with a desktop UA; `https://www.federalreserve.gov/releases/h10/current/` -> 200.
- `curl -H 'Authorization: Bearer proxy-injected' https://opencode.ai/zen/v1/models` -> model list (key is injected by the proxy; never in env).
  Chat base URL reported by the list for chat-completions models: `https://opencode.ai/inference/openai/v1`. Model to use: Muse Spark 1.3 Contributor, reasoning effort high (L-10) — look up its exact id in the list.

## Golden week oracle, first-hand reads of the screenshots (Jul 6-10 2026) — approximate until `context_management/oracle/golden_week.json` lands
- DXY 1h (g1): week frame Mon Jul 6 -> Fri Jul 10. Upper green IP band ~101.19-101.29 (white line 101.24). Lower green band ~100.55-100.675.
  Red "4H (Unmitigated) | BoM" supply ~101.33-101.44 above the ceiling. Blue "1H (Unmitigated) | BoM" demand ~100.65-100.74 at the floor.
  Price: Mon-Tue range/drift up, Wed Jul 8 peak ~101.27 into the ceiling band, sell-off to ~100.62 on Fri Jul 10 (into floor band + 1H BoM), bounce.
  Showcase trade: short ~101.275, SL ~101.33, TP ~100.675.
- DXY 1h (g4): ~16 green liquidity rungs between 100.545 and 101.25 (101.25, 101.24, 101.20, 101.19, 101.14, 101.115, 101.09, 101.00, 100.975, 100.94, 100.905, 100.845, 100.77, 100.68, 100.61, 100.545) and ~8 position-tool trades across the week.
- EURUSD 1h (g5, g7): week range ~1.1393-1.1456; "1H (Unmitigated) | BoM" supply ~1.1446-1.1456 (top), "1H (Unmitigated) | MoM" demand ~1.1400-1.1417 (bottom); ~7 trades; fib grid 0 = 1.13925, 1 = 1.14315, 1.618 = 1.14556.

## Canon structure (v5.3.3 prompt, `canon/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md`)
- Part II context 468-739 · Part III data harvesting 739-1540 · Part IV calculations 1540-1568 · Part V report 1568-1725 · Part VI Engine 2 1725-2058 ·
  Part VI-B Engine 3 (superseded by corrected doc) 2058-2575 · Part IX multi-pair 3257-3688 · Appendix A strike->DXY 4011 · B ZFP 4052 · C pivots 4078.
- Web sources named in Part III: forex.com (14 mentions), investinglive.com (6), tradingview.com, federalreserve.gov (H.10), ice.com.
- Digests (written by reader agents, verify before trusting): `context_management/spec/{E1_ALGO,E2_ALGO,E3_ALGO,HANDOVER_DIGEST,PINEBOX_ENGINE_NOTES,LAWS_DIGEST}.md`, `context_management/oracle/*`.

## E1 canon essentials (from context_management/spec/E1_ALGO.md, cites SP:line = v5.3.3 prompt)
- Assembly SP:1496-1505: collect ALL levels from 9 pillars, never filter by distance to spot (SP:735); score each level on 6 dimensions (0-2 each) + structural-extreme bonus (<=2) = 0-14;
  cluster: 3+ levels within 0.15 DXY = HIGH-DENSITY ZONE, pairs within 0.10 = TIGHT CONFLUENCE; group at 0.10-0.15; zone degree = its highest-scoring level; name the zones.
- Pressure degree: 12-14 EXTREME, 10-11 HEAVY, 8-9 MODERATE-HEAVY, 6-7 MODERATE, 4-5 LIGHT, 0-3 MINIMAL. Synthesis shows MODERATE and above.
- Pivots (P1): classic, fibonacci (0.382/0.618/1.0), camarilla (1.1/12,/6,/4,/2) on prior week HLC and each of the last 3 trading days.
- MA grid (P2): EMA+SMA 9,10,20,50,100,200 (daily by inference); 3+ MAs within 0.15 = cluster; recapture (cross above 50/100/200 within 3 sessions) +2.
- Structural (P5): 90 D1 bars; swing low = lower wick >= 0.15 and close in upper half (mirror for highs); D1 order block = base before a move >= 1.0 lasting >= 5 days;
  repeated extremes within 0.05 on 2+ dates (+1.5 / +2.0), role reversal +2.0; LSZ = 0.05-wide band at the exact swing extreme (extension 0.05-0.10);
  4H S/D = the single 4H origin candle [low, high] before a move >= 0.5 lasting >= 3 trading days, max width 0.40, 60-day scan, drop if > 3 weeks old with no interaction.
- Round numbers (P6): .00/.50 = 2 pts, .25/.75 = 1 pt (DXY). Fib retracements of prior-week range + swings (ratios 0.236/0.382/0.618, ext 1.618).
- Options (P3/P8): strikes from investinglive 10am NY cut; tier 1 >= $1.5B (CRITICAL OPTION WALL), tier 2 $850M-$1.499B (SIGNIFICANT MAGNET), below = excluded.
  EUR/USD strike -> DXY: DXY = K * EURUSD^-0.576, K = 50.14348112 * USDJPY^0.136 * GBPUSD^-0.119 * USDCAD^0.091 * USDSEK^0.042 * USDCHF^0.036 (spots from Fed H.10). NEVER convert DXY zones to pair zones.
- Analysts (P4): explicit S/R levels; tier 1 = ING, forex.com (Matt Weller); 2+ tier-1 agree = 2 pts.
- ZFP (Appendix B): Hard Wall 5-15% (needs option wall >= $1.5B + 3 pillars + confluent floor/ceiling), Standard 15-30%, Soft 30-50%, One-Touch 50-70%; modifiers only add. ZFP by pixel width is banned (R-17).
- POI tier: IP zone overlapping a 4H BoM (0X-1X) = Tier 1; IP only = Tier 2; 4H only = Tier 3.
- Pairs run their OWN full pipeline on their own price; DXY gives direction only (SP:101, 3313, 3639). Pip: DXY 0.01, pairs 0.0001.
- PLACEHOLDERS in v5.3.3 ("unchanged from v4.5.2"): P5 steps 0g/0h/1-5, P6, P7, P8 core, P9 -> full text in the v4.5.2 prompt on the handover branch.
