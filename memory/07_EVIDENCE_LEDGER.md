# 07 — EVIDENCE LEDGER (append-only: every frame I looked at. expectation written BEFORE the look; verdict PASS / FAIL / INCONCLUSIVE; named deltas)

Frames live in `evidence/` (committed) or the scratchpad `frames/` (not durable). Name frames for what they prove.

| # | time UTC | frame | what it is | expectation (written first) | what I saw | verdict |
|---|---|---|---|---|---|---|
| 1 | 2026-11-25 10:47 | scratchpad frames/pb_000_boot.png | Pinebox cold boot, DXY 1H, default buffer script (EMA ribbon) | IDE with editor + candle chart of DXY | Editor left, DXY 1h candles Aug-Nov 2026 (98.5-103), EMA 20/50 + cross markers on the last ~2 weeks only, tabs PINE IDE / BACKTEST, status "FIXTURE · DXY · 1H · 5000 bars" | PASS (environment) |
| 2 | 2026-11-25 10:52 | inputs .../Jul_6-10_DXY_Gold_Standard (g1,g4) | Operator's golden-week DXY 1h charting | n/a (oracle read) | see 08_FACTS golden week | oracle |
| 3 | 2026-11-25 10:53 | same folder (g5,g7) | Operator's golden-week EURUSD 1h charting | n/a (oracle read) | see 08_FACTS golden week | oracle |
