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
