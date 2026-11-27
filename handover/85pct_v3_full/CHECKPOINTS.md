# Checkpoints since the "70% functional" package (branch AGENT, leviathan-devops/plutus-vision)

Each checkpoint is self-contained (operator, after M-60: "the commit has both the code and the context and the graph"). It holds:
- the code;
- `memory/*.md` (all context);
- the evidence frames;
- a folder `handover/<name>/` with `CHECKPOINT.md`, the OmniGraph rebuilt from memory (`omnigraph/graph_store/` = the store directory, `graph_export.jsonl` = full export, `mem_status.txt`, `mem_ls.txt`) and `MANIFEST.sha256` (SHA-256 of every tracked file at that point).

The folder is built by `tools/checkpoint DIR "TITLE" "VERDICT"`, then committed.

**Restore any checkpoint:**

```
git checkout <code commit>
tools/mem/mem rebuild          # or copy handover/<name>/omnigraph/graph_store to /home/user/.plutus-mem
```

| # | Checkpoint | Checkpoint commit | Code commit | Frames | Operator's verdict (verbatim in `memory/12`) |
|---|---|---|---|---|---|
| 0 | "70% functional" (previous package) | `33f747fc` (+ `9ea1467` manifest, `9e1d7b5` / `ea7da38` archive checksums, `4961cd0` part 8 OmniGraph) | `33f747fc` | `evidence/s3k/` (count 11) | M-57: "This is 70% functional very good work" |
| 1 | "80% functional - DXY specific" | `0d4ad41`, made self-contained by `2f31cf5` | `aa8d689` | `evidence/lib4/` (+ M-60 frames `evidence/m60/`, `e3860c7`) | M-60: "DXY is actually pretty accurate ... Commit the current checkpoint as 80% functional, DXY specific" (GBPUSD "completely fucked"; EURUSD frame missing; DXY E2 Wed-Fri broken) |
| 2 | "85% functional - DXY + GU" (V1) | `cea1954` | `bac6b50` (D-139 + D-140) | `evidence/m60b/` | M-61: DXY and GBPUSD "A-" except the Thursday trade; EURUSD "a solid C" |
| 3 | "85% functional - DXY + GU" V2 (Thursday fix) | `6e4f3f7` | `262fadd` (D-141) | `evidence/v2/` (`65ae7fc`) | V2 ordered by M-61; no separate verdict |
| 4 | "85% functional - DXY + GU" V3 (EURUSD fix) | `8f834f4` | `ff6be1e` (D-142b + D-144) | `evidence/v3/` (`a8bfce4`), Pine `63d10dc` | M-62: "Okay, great." Then he ordered this package. |
| 5 | Handover "85% functional V3 - full package" (this folder) | see `CHECKPOINT_COMMIT.txt` | V3 + D-145 (a crash fix found while building this package) | unchanged from V3 (D-145 does not change the golden week; see `ENGINEERING_REPORT.md` section 13) | - |

## What each checkpoint's code does differently

- **70% → 80%**: daily anchoring (D-131, D-132), with the order anchor at the trading-day open, not the London open. Also:
  - no duplicate trades (D-134);
  - L-50 stops (D-135);
  - daily zone update at the London open (D-136; the chain re-anchor tried, D-133 reverted, D-137 off for orders, D-138 on for the drawing);
  - session-by-session swing-scalp line (L-51 first step);
  - Protocols D / E / G as E2 volatility triggers.
- **80% → V1**: D-139, the 6.10 "2-3 more 4H candles" read as +12 hours. D-140, breakouts drawn as session ladders, with Asia holding the open.
- **V1 → V2**: D-141.
  - Dormant alternative-chain orders are contingencies: not drawn until activated.
  - The Law-27 short at a reverse whiplash's TP exists from the whiplash's start.
  - Rockets the move has already passed are void.
- **V2 → V3**: D-142b, the Phase 10 re-entry check against the source pair's same-day record. D-144, the Law-27 trade flow on the day's drawn line. D-143 (the Trading Laws stop rule) was tried and switched off.
- **V3 → handover**: D-145, a KeyError fix (`ENGINEERING_REPORT.md` section 13). No change on the golden week.

## Golden week (Jul 6-10 2026) at V3, against his own trades

Source: `locator_outputs/od_v3_daily_*.txt`. Distances are pips off his entry / SL / TP.

| Pair | Order | Matched to his | Entry / SL / TP off (pips) |
|---|---|---|---|
| DXY | DX2 Mon SS S 101.138 | #2 | 0.2 / 1.3 / 1.5 |
| DXY | DX3 Mon SS L 100.851 | #3 | 0.6 / 2.7 / 0.6 |
| DXY | DX5 Wed SS S 101.203 | #4 | 1.3 / 0.5 / 2.0 |
| DXY | DX6 Wed RWL L 100.980 | #5 | 0.5 / 0.1 / 0.5 |
| DXY | DX4 Wed BS S 101.235 | #6 | 0.0 / 0.8 / 0.5 |
| DXY | DX7 Thu ladder S 100.980 / 101.077 / 100.685 | #7 (ladder short 100.975 / 101.09; his TP not legible) | entry 0.5, SL 1.3 against #7 |
| DXY | DX8 Fri RWL L 100.628 | #8 | 1.3 / 0.3 / 0.0 |
| DXY | DX1 Mon SS S 101.203 | extra, never fills | - |
| EURUSD | EU3 Mon SS L 1.14095 | #2 | 1.1 / 0.2 / 1.3 |
| EURUSD | EU1 Mon SS S 1.14442 | #3 | 0.1 / 0.3 / 6.4 |
| EURUSD | EU6 Wed SS L 1.14018 | #4 | 0.6 / 0.4 / 2.2 |
| EURUSD | EU4 Wed RWL S 1.14269 | #5 | 0.8 / 4.4 / 1.0 |
| EURUSD | EU5 Wed BS L 1.13940 | #6 | 1.3 / 0.4 / 1.1 |
| EURUSD | EU7 Thu ladder L 1.14239 | #7 | 0.6 / 1.1 / 1.1 |
| EURUSD | EU8 Fri RWL S 1.14598 | #8 | 2.0 / 0.4 / 3.4 |
| EURUSD | EU2 Mon SS L 1.14018 | extra, never fills | - |
| GBPUSD | GB2 Mon SS L 1.33333 | #1 | 0.2 / 1.1 / 1.5 |
| GBPUSD | GB1 Mon SS S 1.33959 | #2 | 2.5 / 8.0 / 0.1 |
| GBPUSD | GB3 Wed BS L 1.33255 | #3 | 7.5 / 7.4 / 0.8 |
| GBPUSD | GB4 Fri RWL S 1.34254 (fills Thu 06:15 UTC) | #5 | 0.8 / 3.6 / 0.6 |

**Not caught:**
- EURUSD #1: traded only in the Asian session before the Monday anchor (`DURABLE_FACTS_SINCE_70PCT.md`).
- GBPUSD #4: reinforcement on #3.
- GBPUSD #6: Thu long 1.33829.
- GBPUSD #7: Fri short 1.34481.
