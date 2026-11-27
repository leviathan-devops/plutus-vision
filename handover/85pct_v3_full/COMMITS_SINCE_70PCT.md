# Every commit since the '70% functional' checkpoint (33f747fc) - full messages, files changed

Branch AGENT of leviathan-devops/plutus-vision. Oldest first. Generated with: git log --reverse --stat --format=... 33f747fc..HEAD (the commit that adds this file is listed in CHECKPOINT_COMMIT.txt).

---

## 9ea1467  (2026-11-27T13:49:28+00:00)

full id: 9ea14672d2bdd2cddfcbca0dff5226c373affd1f

```
handover '70% functional': checkpoint commit id + SHA-256 manifest of every tracked file at it

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 handover/70pct_functional/CHECKPOINT_COMMIT.txt | 14 +++++++-------
 handover/70pct_functional/MANIFEST_REPO.sha256  |  6 ++++--
 2 files changed, 11 insertions(+), 9 deletions(-)
---

## 9e1d7b5  (2026-11-27T13:50:42+00:00)

full id: 9e1d7b5c2be0eeaba7cddbf0e1959bcac28035f5

```
handover '70% functional': SHA-256 and size of the seven downloadable archives (built from 9ea1467)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 handover/70pct_functional/ARCHIVES_SHA256SUMS.txt | 9 +++++++++
 1 file changed, 9 insertions(+)
---

## ea7da38  (2026-11-27T13:52:33+00:00)

full id: ea7da3891c9c506f827595a05cb2ed6eba872475

```
handover '70% functional': bundle delivered in two parts (500 MiB upload limit) - rejoin note + part checksums; journal

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 handover/70pct_functional/00_START_HERE.md        | 2 +-
 handover/70pct_functional/ARCHIVES_SHA256SUMS.txt | 3 +++
 memory/05_JOURNAL.md                              | 1 +
 3 files changed, 5 insertions(+), 1 deletion(-)
---

## 6683095  (2026-11-27T14:48:47+00:00)

full id: 6683095c4531222e5aafad7c7adc4b55d3667e69

```
journal + state: package delivered; event-data hosts allowed, first fetch refused by the session permission check - waiting on the operator's answers

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 handover/70pct_functional/00_START_HERE.md | 2 +-
 memory/01_CURRENT_STATE.md                 | 2 +-
 memory/05_JOURNAL.md                       | 1 +
 3 files changed, 3 insertions(+), 2 deletions(-)
---

## 4961cd0  (2026-11-27T15:09:22+00:00)

full id: 4961cd0ed81dcd5582c9960ecac065294c86e7ce

```
operator M-58 verbatim + rulings L-46..L-49 (stop rule, daily anchoring approved, winning trade library = oracle set, TVC); handover part 8 = the OmniGraph on its own (checksum)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 handover/70pct_functional/ARCHIVES_SHA256SUMS.txt |  1 +
 memory/04_OPERATOR_RULINGS_LIVE.md                |  4 ++++
 memory/12_OPERATOR_VERBATIM.md                    | 11 +++++++++++
 3 files changed, 16 insertions(+)
---

## 555482a  (2026-11-27T15:26:17+00:00)

full id: 555482a942089ec19c4ccf750a256a7205a8ad2f

```
answers to M-58: item 5 chart (golden Monday long on TVC:DXY 15m, correction), item 1 stop scenarios S1-S3 with charts and questions; tools/research/stopscen.py locator

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 evidence/answers_m58/Q1_stop_scenarios.md                  |  74 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 evidence/answers_m58/q5_golden_monday_long.pine            |  19 +++++++++++++++++++
 evidence/answers_m58/q5_golden_monday_long_TVC_DXY_15m.png | Bin 0 -> 150603 bytes
 evidence/answers_m58/s1.pine                               |  19 +++++++++++++++++++
 evidence/answers_m58/s1_stop_scenario.png                  | Bin 0 -> 179840 bytes
 evidence/answers_m58/s2.pine                               |  18 ++++++++++++++++++
 evidence/answers_m58/s2_stop_scenario.png                  | Bin 0 -> 166949 bytes
 evidence/answers_m58/s3.pine                               |  17 +++++++++++++++++
 evidence/answers_m58/s3_stop_scenario.png                  | Bin 0 -> 170147 bytes
 evidence/answers_m58/scenario_pine.py                      |  55 +++++++++++++++++++++++++++++++++++++++++++++++++++++++
 tools/research/stopscen.py                                 |  86 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 11 files changed, 288 insertions(+)
---

## b429b8c  (2026-11-27T15:36:29+00:00)

full id: b429b8c07cb52458615a32f4be259492296697b8

```
answers to M-58 items 4 and 6: library inventory (17 pair-weeks, now the oracle set) and the counting question with its frame of reference; item 7 probes journaled; D-129 blind-test reserve -> oracle weeks

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 evidence/answers_m58/Q4_library_inventory.md  | 39 +++++++++++++++++++++++++++++++++++++++
 evidence/answers_m58/Q6_counting_explained.md | 43 +++++++++++++++++++++++++++++++++++++++++++
 memory/03_DECISION_CHAIN.md                   |  1 +
 memory/05_JOURNAL.md                          |  3 +++
 4 files changed, 86 insertions(+)
---

## 7f1babd  (2026-11-27T15:42:25+00:00)

full id: 7f1babd0a346e6a7a5435611cdcf468dd61a3ef3

```
item 7: Protocols D (Treasury auctions) and G (EIA crude stocks) harvested as of each week's anchor for all 40 sidecar weeks; shown in the Engine 2 day Triggers and a volatility-trigger block (P452:1443-1446 'If the Bid-to-Cover ratio is >= 2.6x ... VOLATILITY TRIGGER'; 'If absolute deviation >= 5M barrels ... VOLATILITY TRIGGER'); E and F stay NO DATA (host not allowed / Cloudflare)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/e2_chain.py                      |   23 +++-
 e1_tool/plutus.py                        |   10 ++
 memory/05_JOURNAL.md                     |    1 +
 memory/15_CANON_COVERAGE.md              |    2 +-
 sidecar/out/protocols/2026-02-02.json    |   66 ++++++++++
 sidecar/out/protocols/2026-02-09.json    |   91 +++++++++++++
 sidecar/out/protocols/2026-02-16.json    |   83 ++++++++++++
 sidecar/out/protocols/2026-02-23.json    |   99 ++++++++++++++
 sidecar/out/protocols/2026-03-02.json    |   66 ++++++++++
 sidecar/out/protocols/2026-03-09.json    |   91 +++++++++++++
 sidecar/out/protocols/2026-03-16.json    |   83 ++++++++++++
 sidecar/out/protocols/2026-03-23.json    |   99 ++++++++++++++
 sidecar/out/protocols/2026-03-30.json    |   66 ++++++++++
 sidecar/out/protocols/2026-04-06.json    |   91 +++++++++++++
 sidecar/out/protocols/2026-04-13.json    |   66 ++++++++++
 sidecar/out/protocols/2026-04-20.json    |   83 ++++++++++++
 sidecar/out/protocols/2026-04-27.json    |   99 ++++++++++++++
 sidecar/out/protocols/2026-05-04.json    |   66 ++++++++++
 sidecar/out/protocols/2026-05-11.json    |   91 +++++++++++++
 sidecar/out/protocols/2026-05-18.json    |   83 ++++++++++++
 sidecar/out/protocols/2026-05-25.json    |   99 ++++++++++++++
 sidecar/out/protocols/2026-06-01.json    |   66 ++++++++++
 sidecar/out/protocols/2026-06-08.json    |   91 +++++++++++++
 sidecar/out/protocols/2026-06-15.json    |   83 ++++++++++++
 sidecar/out/protocols/2026-06-22.json    |   99 ++++++++++++++
 sidecar/out/protocols/2026-06-29.json    |   66 ++++++++++
 sidecar/out/protocols/2026-07-06.json    |   91 +++++++++++++
 sidecar/out/protocols/2026-07-13.json    |   66 ++++++++++
 sidecar/out/protocols/2026-07-20.json    |   83 ++++++++++++
 sidecar/out/protocols/2026-07-27.json    |   99 ++++++++++++++
 sidecar/out/protocols/2026-08-03.json    |   66 ++++++++++
 sidecar/out/protocols/2026-08-10.json    |   91 +++++++++++++
 sidecar/out/protocols/2026-08-17.json    |   83 ++++++++++++
 sidecar/out/protocols/2026-08-24.json    |   99 ++++++++++++++
 sidecar/out/protocols/2026-08-31.json    |   66 ++++++++++
 sidecar/out/protocols/2026-09-07.json    |   91 +++++++++++++
 sidecar/out/protocols/2026-09-14.json    |   83 ++++++++++++
 sidecar/out/protocols/2026-09-21.json    |   99 ++++++++++++++
 sidecar/out/protocols/2026-09-28.json    |   66 ++++++++++
 sidecar/out/protocols/2026-10-05.json    |   91 +++++++++++++
 sidecar/out/protocols/2026-10-12.json    |   66 ++++++++++
 sidecar/out/protocols/2026-10-19.json    |   83 ++++++++++++
 sidecar/out/protocols/2026-10-26.json    |   99 ++++++++++++++
 sidecar/out/protocols/2026-11-02.json    |   66 ++++++++++
 sidecar/protocols.py                     |  152 ++++++++++++++++++++++
 sidecar/raw/protocols/eia_schedule.html  | 1075 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 sidecar/raw/protocols/eia_wcestus1.html  |    1 +
 sidecar/raw/protocols/td_2026-02-02.json |    1 +
 sidecar/raw/protocols/td_2026-02-09.json |    1 +
 sidecar/raw/protocols/td_2026-02-16.json |    1 +
 sidecar/raw/protocols/td_2026-02-23.json |    1 +
 sidecar/raw/protocols/td_2026-03-02.json |    1 +
 sidecar/raw/protocols/td_2026-03-09.json |    1 +
 sidecar/raw/protocols/td_2026-03-16.json |    1 +
 sidecar/raw/protocols/td_2026-03-23.json |    1 +
 sidecar/raw/protocols/td_2026-03-30.json |    1 +
 sidecar/raw/protocols/td_2026-04-06.json |    1 +
 sidecar/raw/protocols/td_2026-04-13.json |    1 +
 sidecar/raw/protocols/td_2026-04-20.json |    1 +
 sidecar/raw/protocols/td_2026-04-27.json |    1 +
 sidecar/raw/protocols/td_2026-05-04.json |    1 +
 sidecar/raw/protocols/td_2026-05-11.json |    1 +
 sidecar/raw/protocols/td_2026-05-18.json |    1 +
 sidecar/raw/protocols/td_2026-05-25.json |    1 +
 sidecar/raw/protocols/td_2026-06-01.json |    1 +
 sidecar/raw/protocols/td_2026-06-08.json |    1 +
 sidecar/raw/protocols/td_2026-06-15.json |    1 +
 sidecar/raw/protocols/td_2026-06-22.json |    1 +
 sidecar/raw/protocols/td_2026-06-29.json |    1 +
 sidecar/raw/protocols/td_2026-07-06.json |    1 +
 sidecar/raw/protocols/td_2026-07-13.json |    1 +
 sidecar/raw/protocols/td_2026-07-20.json |    1 +
 sidecar/raw/protocols/td_2026-07-27.json |    1 +
 sidecar/raw/protocols/td_2026-08-03.json |    1 +
 sidecar/raw/protocols/td_2026-08-10.json |    1 +
 sidecar/raw/protocols/td_2026-08-17.json |    1 +
 sidecar/raw/protocols/td_2026-08-24.json |    1 +
 sidecar/raw/protocols/td_2026-08-31.json |    1 +
 sidecar/raw/protocols/td_2026-09-07.json |    1 +
 sidecar/raw/protocols/td_2026-09-14.json |    1 +
 sidecar/raw/protocols/td_2026-09-21.json |    1 +
 sidecar/raw/protocols/td_2026-09-28.json |    1 +
 sidecar/raw/protocols/td_2026-10-05.json |    1 +
 sidecar/raw/protocols/td_2026-10-12.json |    1 +
 sidecar/raw/protocols/td_2026-10-19.json |    1 +
 sidecar/raw/protocols/td_2026-10-26.json |    1 +
 sidecar/raw/protocols/td_2026-11-02.json |    1 +
 87 files changed, 4616 insertions(+), 3 deletions(-)
---

## c84eb24  (2026-11-27T15:44:09+00:00)

full id: c84eb2441fcdfaa0520659b05d35560bd6c1d1dd

```
state: M-58 answered (items 1, 3, 4, 5, 6, 7), building item 2 daily anchoring

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 memory/01_CURRENT_STATE.md | 6 ++++++
 1 file changed, 6 insertions(+)
---

## 7460b58  (2026-11-27T16:01:51+00:00)

full id: 7460b58263a74bc69b2df78b185855cc50611ed6

```
item 2: daily anchoring (plutus.py --daily, D-131) - Monday map and chain fixed; at each trading-day open the line restarts from the actual price and the day's orders are confirmed (order block not closed through, price on the order's side); per-day runtime leak check; P533:506 reversal-stop trial kept behind a flag, off (D-130)

E3C:115 'WorkingDayMap ... dayOpenSpot'; Fibonacci Spiderwebs 'London Session open position = Trade Setup Anchor'; P452:699-703 one-time use.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/__pycache__/e1_data.cpython-313.pyc   | Bin 8094 -> 9049 bytes
 e1_tool/__pycache__/e2_chain.cpython-313.pyc  | Bin 105462 -> 107745 bytes
 e1_tool/__pycache__/e3_trades.cpython-313.pyc | Bin 105363 -> 106120 bytes
 e1_tool/__pycache__/plutus.cpython-313.pyc    | Bin 33796 -> 45091 bytes
 e1_tool/e1_data.py                            |  16 ++++++++++++++--
 e1_tool/e2_chain.py                           |   9 ++++-----
 e1_tool/e3_trades.py                          |  16 ++++++++++++++--
 e1_tool/plutus.py                             | 125 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++------------
 evidence/chk107/DXY_2026-05-18_all.png        | Bin 0 -> 107172 bytes
 evidence/chk107/DXY_2026-05-18_week.png       | Bin 0 -> 94367 bytes
 evidence/chk107/DXY_2026-05-18_zones.png      | Bin 0 -> 82848 bytes
 evidence/chk107/DXY_2026-07-06_all.png        | Bin 0 -> 161866 bytes
 evidence/chk107/DXY_2026-07-06_week.png       | Bin 0 -> 127623 bytes
 evidence/chk107/DXY_2026-07-06_zones.png      | Bin 0 -> 100820 bytes
 memory/03_DECISION_CHAIN.md                   |   2 ++
 memory/05_JOURNAL.md                          |   1 +
 memory/07_EVIDENCE_LEDGER.md                  |   2 ++
 tools/e1render                                |   2 +-
 tools/leak_check.py                           |  24 ++++++++++++++++++++++--
 19 files changed, 173 insertions(+), 24 deletions(-)
---

## 636326e  (2026-11-27T16:02:18+00:00)

full id: 636326e945576df27361c817c401ea0cb9ddb3ff

```
daily anchoring is the default of plutus.py (D-131); --weekly keeps every order at the Monday anchor

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/plutus.py | 5 +++--
 1 file changed, 3 insertions(+), 2 deletions(-)
---

## a918580  (2026-11-27T16:02:57+00:00)

full id: a918580a9085b36eb8c5087ee6708d1e9b3ec3f5

```
state: daily anchoring default; next = library oracle, spiderweb layer, count-11 defects

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 memory/01_CURRENT_STATE.md | 6 ++++++
 1 file changed, 6 insertions(+)
---

## 496d4f6  (2026-11-27T16:14:52+00:00)

full id: 496d4f6bea966e2c366b0ec6a775867dc402b597

```
library comparison started: frames for GBPUSD 02-23, 03-02, 04-06, 04-13 (daily default); ledger 108 / 108b (03-02 delta: Engine 2 a day late, no reversal after the breakdown, his Wednesday 1.3313 long missed)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 evidence/lib1/GBPUSD_2026-02-23_all.png   | Bin 0 -> 141736 bytes
 evidence/lib1/GBPUSD_2026-02-23_week.png  | Bin 0 -> 87853 bytes
 evidence/lib1/GBPUSD_2026-02-23_zones.png | Bin 0 -> 115386 bytes
 evidence/lib1/GBPUSD_2026-03-02_all.png   | Bin 0 -> 145244 bytes
 evidence/lib1/GBPUSD_2026-03-02_week.png  | Bin 0 -> 88390 bytes
 evidence/lib1/GBPUSD_2026-03-02_zones.png | Bin 0 -> 121144 bytes
 evidence/lib1/GBPUSD_2026-04-06_all.png   | Bin 0 -> 128956 bytes
 evidence/lib1/GBPUSD_2026-04-06_week.png  | Bin 0 -> 105316 bytes
 evidence/lib1/GBPUSD_2026-04-06_zones.png | Bin 0 -> 89810 bytes
 evidence/lib1/GBPUSD_2026-04-13_all.png   | Bin 0 -> 173726 bytes
 evidence/lib1/GBPUSD_2026-04-13_week.png  | Bin 0 -> 114216 bytes
 evidence/lib1/GBPUSD_2026-04-13_zones.png | Bin 0 -> 130279 bytes
 memory/07_EVIDENCE_LEDGER.md              |   2 ++
 13 files changed, 2 insertions(+)
---

## 58b8a8e  (2026-11-27T16:30:01+00:00)

full id: 58b8a8ea1e37c36aa5741548d8dc4d7ba434c809

```
item 7: Protocol E (NY Fed ON RRP) harvested for all 40 weeks after the operator allowed markets.newyorkfed.org (P452:1444 'Extract the current session's Accepted Total. Compare against the preceding business day. If contraction >= USD 50 Billion ... VOLATILITY TRIGGER'); report block shows it; only Protocol F stays NO DATA

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/__pycache__/e2_chain.cpython-313.pyc | Bin 107745 -> 107911 bytes
 e1_tool/__pycache__/plutus.cpython-313.pyc   | Bin 45091 -> 45201 bytes
 e1_tool/e2_chain.py                          |   2 +-
 e1_tool/plutus.py                            |   5 ++++-
 memory/05_JOURNAL.md                         |   2 ++
 memory/15_CANON_COVERAGE.md                  |   2 +-
 sidecar/out/protocols/2026-02-02.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-02-09.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-02-16.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-02-23.json        |  16 +++++++++++++---
 sidecar/out/protocols/2026-03-02.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-03-09.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-03-16.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-03-23.json        |  16 +++++++++++++---
 sidecar/out/protocols/2026-03-30.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-04-06.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-04-13.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-04-20.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-04-27.json        |  16 +++++++++++++---
 sidecar/out/protocols/2026-05-04.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-05-11.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-05-18.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-05-25.json        |  16 +++++++++++++---
 sidecar/out/protocols/2026-06-01.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-06-08.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-06-15.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-06-22.json        |  16 +++++++++++++---
 sidecar/out/protocols/2026-06-29.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-07-06.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-07-13.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-07-20.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-07-27.json        |  16 +++++++++++++---
 sidecar/out/protocols/2026-08-03.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-08-10.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-08-17.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-08-24.json        |  16 +++++++++++++---
 sidecar/out/protocols/2026-08-31.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-09-07.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-09-14.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-09-21.json        |  16 +++++++++++++---
 sidecar/out/protocols/2026-09-28.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-10-05.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-10-12.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-10-19.json        |  14 ++++++++++++--
 sidecar/out/protocols/2026-10-26.json        |  16 +++++++++++++---
 sidecar/out/protocols/2026-11-02.json        |  14 ++++++++++++--
 sidecar/protocols.py                         |  28 +++++++++++++++++++++++++---
 sidecar/raw/protocols/rrp_2026-02-02.json    |   1 +
 sidecar/raw/protocols/rrp_2026-02-09.json    |   1 +
 sidecar/raw/protocols/rrp_2026-02-16.json    |   1 +
 sidecar/raw/protocols/rrp_2026-02-23.json    |   1 +
 sidecar/raw/protocols/rrp_2026-03-02.json    |   1 +
 sidecar/raw/protocols/rrp_2026-03-09.json    |   1 +
 sidecar/raw/protocols/rrp_2026-03-16.json    |   1 +
 sidecar/raw/protocols/rrp_2026-03-23.json    |   1 +
 sidecar/raw/protocols/rrp_2026-03-30.json    |   1 +
 sidecar/raw/protocols/rrp_2026-04-06.json    |   1 +
 sidecar/raw/protocols/rrp_2026-04-13.json    |   1 +
 sidecar/raw/protocols/rrp_2026-04-20.json    |   1 +
 sidecar/raw/protocols/rrp_2026-04-27.json    |   1 +
 sidecar/raw/protocols/rrp_2026-05-04.json    |   1 +
 sidecar/raw/protocols/rrp_2026-05-11.json    |   1 +
 sidecar/raw/protocols/rrp_2026-05-18.json    |   1 +
 sidecar/raw/protocols/rrp_2026-05-25.json    |   1 +
 sidecar/raw/protocols/rrp_2026-06-01.json    |   1 +
 sidecar/raw/protocols/rrp_2026-06-08.json    |   1 +
 sidecar/raw/protocols/rrp_2026-06-15.json    |   1 +
 sidecar/raw/protocols/rrp_2026-06-22.json    |   1 +
 sidecar/raw/protocols/rrp_2026-06-29.json    |   1 +
 sidecar/raw/protocols/rrp_2026-07-06.json    |   1 +
 sidecar/raw/protocols/rrp_2026-07-13.json    |   1 +
 sidecar/raw/protocols/rrp_2026-07-20.json    |   1 +
 sidecar/raw/protocols/rrp_2026-07-27.json    |   1 +
 sidecar/raw/protocols/rrp_2026-08-03.json    |   1 +
 sidecar/raw/protocols/rrp_2026-08-10.json    |   1 +
 sidecar/raw/protocols/rrp_2026-08-17.json    |   1 +
 sidecar/raw/protocols/rrp_2026-08-24.json    |   1 +
 sidecar/raw/protocols/rrp_2026-08-31.json    |   1 +
 sidecar/raw/protocols/rrp_2026-09-07.json    |   1 +
 sidecar/raw/protocols/rrp_2026-09-14.json    |   1 +
 sidecar/raw/protocols/rrp_2026-09-21.json    |   1 +
 sidecar/raw/protocols/rrp_2026-09-28.json    |   1 +
 sidecar/raw/protocols/rrp_2026-10-05.json    |   1 +
 sidecar/raw/protocols/rrp_2026-10-12.json    |   1 +
 sidecar/raw/protocols/rrp_2026-10-19.json    |   1 +
 sidecar/raw/protocols/rrp_2026-10-26.json    |   1 +
 sidecar/raw/protocols/rrp_2026-11-02.json    |   1 +
 87 files changed, 562 insertions(+), 95 deletions(-)
---

## 43c5ae1  (2026-11-27T16:30:34+00:00)

full id: 43c5ae18aa6be335b75cf6fb9410bdf80e51e636

```
state: Protocol E built; library comparison started (ledger 108b)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 memory/01_CURRENT_STATE.md | 4 +++-
 1 file changed, 3 insertions(+), 1 deletion(-)
---

## 748c71e  (2026-11-27T16:36:46+00:00)

full id: 748c71e9cb16347b16d5ff40b0240f1b26b1783d

```
daily anchoring: alternative chain activates at the day's anchor once the primary failed at its Decision Zone (6.6 Step 4, D-132); ledger 109 / 109b (GBPUSD Apr 13 vs his library chart)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/__pycache__/plutus.cpython-313.pyc | Bin 45201 -> 52265 bytes
 e1_tool/plutus.py                          |  60 +++++++++++++++++++++++++++++++++++++++++++++++++++++-------
 evidence/lib2/GBPUSD_2026-04-13_all.png    | Bin 0 -> 158345 bytes
 evidence/lib2/GBPUSD_2026-04-13_week.png   | Bin 0 -> 96650 bytes
 evidence/lib2/GBPUSD_2026-04-13_zones.png  | Bin 0 -> 130247 bytes
 memory/03_DECISION_CHAIN.md                |   1 +
 memory/07_EVIDENCE_LEDGER.md               |   2 ++
 7 files changed, 56 insertions(+), 7 deletions(-)
---

## f4ad3a9  (2026-11-27T16:39:37+00:00)

full id: f4ad3a90700971322846bef10a0d1a784dafe84d

```
D-133 tried and reverted (chain re-anchor on the fixed Monday map); open questions to the operator recorded

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 memory/03_DECISION_CHAIN.md | 1 +
 memory/05_JOURNAL.md        | 1 +
 2 files changed, 2 insertions(+)
---

## dace31b  (2026-11-27T16:39:46+00:00)

full id: dace31ba5d0967e6d1b3f6975418fd54ed31ffb7

```
V1 harvest caches for the library weeks (GBPUSD / DXY / EURUSD Feb-Apr 2026, built while running the tool on them)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/cache/v1s/DXY_15_2026-02-02.json     | 1 +
 e1_tool/cache/v1s/DXY_15_2026-02-09.json     | 1 +
 e1_tool/cache/v1s/DXY_15_2026-02-16.json     | 1 +
 e1_tool/cache/v1s/DXY_15_2026-02-23.json     | 1 +
 e1_tool/cache/v1s/DXY_15_2026-03-02.json     | 1 +
 e1_tool/cache/v1s/DXY_15_2026-03-16.json     | 1 +
 e1_tool/cache/v1s/DXY_15_2026-03-23.json     | 1 +
 e1_tool/cache/v1s/DXY_15_2026-03-30.json     | 1 +
 e1_tool/cache/v1s/DXY_240_2026-02-02.json    | 1 +
 e1_tool/cache/v1s/DXY_240_2026-02-09.json    | 1 +
 e1_tool/cache/v1s/DXY_240_2026-02-16.json    | 1 +
 e1_tool/cache/v1s/DXY_240_2026-02-23.json    | 1 +
 e1_tool/cache/v1s/DXY_240_2026-03-02.json    | 1 +
 e1_tool/cache/v1s/DXY_240_2026-03-16.json    | 1 +
 e1_tool/cache/v1s/DXY_240_2026-03-23.json    | 1 +
 e1_tool/cache/v1s/DXY_240_2026-03-30.json    | 1 +
 e1_tool/cache/v1s/DXY_30_2026-02-02.json     | 1 +
 e1_tool/cache/v1s/DXY_30_2026-02-09.json     | 1 +
 e1_tool/cache/v1s/DXY_30_2026-02-16.json     | 1 +
 e1_tool/cache/v1s/DXY_30_2026-02-23.json     | 1 +
 e1_tool/cache/v1s/DXY_30_2026-03-02.json     | 1 +
 e1_tool/cache/v1s/DXY_30_2026-03-16.json     | 1 +
 e1_tool/cache/v1s/DXY_30_2026-03-23.json     | 1 +
 e1_tool/cache/v1s/DXY_30_2026-03-30.json     | 1 +
 e1_tool/cache/v1s/DXY_60_2026-02-02.json     | 1 +
 e1_tool/cache/v1s/DXY_60_2026-02-09.json     | 1 +
 e1_tool/cache/v1s/DXY_60_2026-02-16.json     | 1 +
 e1_tool/cache/v1s/DXY_60_2026-02-23.json     | 1 +
 e1_tool/cache/v1s/DXY_60_2026-03-02.json     | 1 +
 e1_tool/cache/v1s/DXY_60_2026-03-16.json     | 1 +
 e1_tool/cache/v1s/DXY_60_2026-03-23.json     | 1 +
 e1_tool/cache/v1s/DXY_60_2026-03-30.json     | 1 +
 e1_tool/cache/v1s/EURUSD_15_2026-02-02.json  | 1 +
 e1_tool/cache/v1s/EURUSD_15_2026-02-09.json  | 1 +
 e1_tool/cache/v1s/EURUSD_15_2026-02-16.json  | 1 +
 e1_tool/cache/v1s/EURUSD_15_2026-02-23.json  | 1 +
 e1_tool/cache/v1s/EURUSD_15_2026-03-02.json  | 1 +
 e1_tool/cache/v1s/EURUSD_15_2026-03-16.json  | 1 +
 e1_tool/cache/v1s/EURUSD_15_2026-03-23.json  | 1 +
 e1_tool/cache/v1s/EURUSD_15_2026-03-30.json  | 1 +
 e1_tool/cache/v1s/EURUSD_15_2026-04-06.json  | 1 +
 e1_tool/cache/v1s/EURUSD_15_2026-04-13.json  | 1 +
 e1_tool/cache/v1s/EURUSD_240_2026-02-02.json | 1 +
 e1_tool/cache/v1s/EURUSD_240_2026-02-09.json | 1 +
 e1_tool/cache/v1s/EURUSD_240_2026-02-16.json | 1 +
 e1_tool/cache/v1s/EURUSD_240_2026-02-23.json | 1 +
 e1_tool/cache/v1s/EURUSD_240_2026-03-02.json | 1 +
 e1_tool/cache/v1s/EURUSD_240_2026-03-16.json | 1 +
 e1_tool/cache/v1s/EURUSD_240_2026-03-23.json | 1 +
 e1_tool/cache/v1s/EURUSD_240_2026-03-30.json | 1 +
 e1_tool/cache/v1s/EURUSD_240_2026-04-06.json | 1 +
 e1_tool/cache/v1s/EURUSD_240_2026-04-13.json | 1 +
 e1_tool/cache/v1s/EURUSD_30_2026-02-02.json  | 1 +
 e1_tool/cache/v1s/EURUSD_30_2026-02-09.json  | 1 +
 e1_tool/cache/v1s/EURUSD_30_2026-02-16.json  | 1 +
 e1_tool/cache/v1s/EURUSD_30_2026-02-23.json  | 1 +
 e1_tool/cache/v1s/EURUSD_30_2026-03-02.json  | 1 +
 e1_tool/cache/v1s/EURUSD_30_2026-03-16.json  | 1 +
 e1_tool/cache/v1s/EURUSD_30_2026-03-23.json  | 1 +
 e1_tool/cache/v1s/EURUSD_30_2026-03-30.json  | 1 +
 e1_tool/cache/v1s/EURUSD_30_2026-04-06.json  | 1 +
 e1_tool/cache/v1s/EURUSD_30_2026-04-13.json  | 1 +
 e1_tool/cache/v1s/EURUSD_60_2026-02-02.json  | 1 +
 e1_tool/cache/v1s/EURUSD_60_2026-02-09.json  | 1 +
 e1_tool/cache/v1s/EURUSD_60_2026-02-16.json  | 1 +
 e1_tool/cache/v1s/EURUSD_60_2026-02-23.json  | 1 +
 e1_tool/cache/v1s/EURUSD_60_2026-03-02.json  | 1 +
 e1_tool/cache/v1s/EURUSD_60_2026-03-16.json  | 1 +
 e1_tool/cache/v1s/EURUSD_60_2026-03-23.json  | 1 +
 e1_tool/cache/v1s/EURUSD_60_2026-03-30.json  | 1 +
 e1_tool/cache/v1s/EURUSD_60_2026-04-06.json  | 1 +
 e1_tool/cache/v1s/EURUSD_60_2026-04-13.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-02-02.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-02-09.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-02-16.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-02-23.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-03-02.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-03-16.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-03-23.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-03-30.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-04-06.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-04-13.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-02-02.json | 1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-02-09.json | 1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-02-16.json | 1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-02-23.json | 1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-03-02.json | 1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-03-16.json | 1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-03-23.json | 1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-03-30.json | 1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-04-06.json | 1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-04-13.json | 1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-02-02.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-02-09.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-02-16.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-02-23.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-03-02.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-03-16.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-03-23.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-03-30.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-04-06.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-04-13.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-02-02.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-02-09.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-02-16.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-02-23.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-03-02.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-03-16.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-03-23.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-03-30.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-04-06.json  | 1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-04-13.json  | 1 +
 112 files changed, 112 insertions(+)
---

## df37f52  (2026-11-27T16:39:54+00:00)

full id: df37f52d4f315f70787efb4d10f4af39966c004e

```
generated Pine of the library-week frames (evidence/lib1, lib2)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/out/E1_GBPUSD_2026-02-23.pine | 405 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 e1_tool/out/E1_GBPUSD_2026-03-02.pine | 399 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 e1_tool/out/E1_GBPUSD_2026-04-06.pine | 430 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 e1_tool/out/E1_GBPUSD_2026-04-13.pine | 406 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 4 files changed, 1640 insertions(+)
---

## 306e94c  (2026-11-27T16:51:01+00:00)

full id: 306e94c03e841a42d613e7f8b3070811b848bb7d

```
operator M-59 verbatim + rulings L-50..L-55 (wider stop for good trades, EURUSD inside stop; box + swing-by-swing line; no duplicate trades; daily zone update at London open approved; work within the calendar constraint; library weeks are the optimisation set)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 memory/04_OPERATOR_RULINGS_LIVE.md | 8 ++++++++
 memory/12_OPERATOR_VERBATIM.md     | 3 +++
 2 files changed, 11 insertions(+)
---

## 980bcf6  (2026-11-27T16:52:17+00:00)

full id: 980bcf6956b157b6c58860d45cc27613b11cd20f

```
no duplicate trades (L-52, D-134): a repeat of a still-resting or open order is the same trade - the live order keeps resting, no copy; a completed order lets the next move carry a new trade; one numbering per week

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/__pycache__/e1_data.cpython-313.pyc  | Bin 9049 -> 9049 bytes
 e1_tool/__pycache__/e2_chain.cpython-313.pyc | Bin 107911 -> 107911 bytes
 e1_tool/__pycache__/plutus.cpython-313.pyc   | Bin 52265 -> 55944 bytes
 e1_tool/plutus.py                            |  49 +++++++++++++++++++++++++++++++++++++++++++++++++
 memory/03_DECISION_CHAIN.md                  |   1 +
 5 files changed, 50 insertions(+)
---

## 0451a56  (2026-11-27T16:55:01+00:00)

full id: 0451a56f1e8ea94e81c73009e9a452287dfbb275

```
stops per L-50 (D-135): reversal entries take the stop inside the next zone without the 9.5-pip envelope veto, RRR floor decides, fallback entries only deeper; EUR/USD keeps the outside stop (his golden EUR/USD stops measure as outside)

P533:506 'When trying to catch a CORRECTION/REVERSAL - ALWAYS make sure SL is 1-2 pips INSIDE THE NEXT ZONE'.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/__pycache__/e3_trades.cpython-313.pyc | Bin 106120 -> 107440 bytes
 e1_tool/e3_trades.py                          |  23 +++++++++++++++++++----
 memory/03_DECISION_CHAIN.md                   |   1 +
 memory/05_JOURNAL.md                          |   1 +
 4 files changed, 21 insertions(+), 4 deletions(-)
---

## 1024df9  (2026-11-27T16:56:16+00:00)

full id: 1024df99d2ab337fdd3b5f542e9f4209072aa0ec

```
state: L-53 daily zone update design written down before the build

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 memory/01_CURRENT_STATE.md | 6 ++++++
 1 file changed, 6 insertions(+)
---

## e1eaa21  (2026-11-27T17:13:09+00:00)

full id: e1eaa21fb2202a7bd1f614dbf6355c83f15c96b2

```
daily zone update at London open (L-53, D-136): Engine 1 rebuilt as of each London open, zones formed since the week anchor added without duplicates, a failed chain re-anchored on the rebuilt map; trading-day-open confirmation, alternative activation and no-copy rule kept; leak check cuts at both instants

M-59: 'synchronously re-update the zones at the beginning of London session each successive day ... without adding a bunch of duplicate garbage'.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/__pycache__/e1_data.cpython-313.pyc                | Bin 9049 -> 9180 bytes
 e1_tool/__pycache__/e1_v1.cpython-313.pyc                  | Bin 7732 -> 7944 bytes
 e1_tool/__pycache__/e2_chain.cpython-313.pyc               | Bin 107911 -> 108393 bytes
 e1_tool/__pycache__/plutus.cpython-313.pyc                 | Bin 55944 -> 71288 bytes
 e1_tool/cache/v1s/DXY_15_2026-04-13_1776146400000.json     |   1 +
 e1_tool/cache/v1s/DXY_15_2026-04-13_1776232800000.json     |   1 +
 e1_tool/cache/v1s/DXY_15_2026-04-20_1776751200000.json     |   1 +
 e1_tool/cache/v1s/DXY_15_2026-04-20_1776837600000.json     |   1 +
 e1_tool/cache/v1s/DXY_15_2026-04-20_1776924000000.json     |   1 +
 e1_tool/cache/v1s/DXY_15_2026-04-20_1777010400000.json     |   1 +
 e1_tool/cache/v1s/DXY_15_2026-07-06_1783404000000.json     |   1 +
 e1_tool/cache/v1s/DXY_15_2026-07-06_1783490400000.json     |   1 +
 e1_tool/cache/v1s/DXY_15_2026-07-06_1783576800000.json     |   1 +
 e1_tool/cache/v1s/DXY_15_2026-07-06_1783663200000.json     |   1 +
 e1_tool/cache/v1s/DXY_15_2026-10-05_1791266400000.json     |   1 +
 e1_tool/cache/v1s/DXY_15_2026-10-05_1791352800000.json     |   1 +
 e1_tool/cache/v1s/DXY_15_2026-10-05_1791439200000.json     |   1 +
 e1_tool/cache/v1s/DXY_15_2026-10-05_1791525600000.json     |   1 +
 e1_tool/cache/v1s/DXY_240_2026-04-13_1776146400000.json    |   1 +
 e1_tool/cache/v1s/DXY_240_2026-04-13_1776232800000.json    |   1 +
 e1_tool/cache/v1s/DXY_240_2026-04-20_1776751200000.json    |   1 +
 e1_tool/cache/v1s/DXY_240_2026-04-20_1776837600000.json    |   1 +
 e1_tool/cache/v1s/DXY_240_2026-04-20_1776924000000.json    |   1 +
 e1_tool/cache/v1s/DXY_240_2026-04-20_1777010400000.json    |   1 +
 e1_tool/cache/v1s/DXY_240_2026-07-06_1783404000000.json    |   1 +
 e1_tool/cache/v1s/DXY_240_2026-07-06_1783490400000.json    |   1 +
 e1_tool/cache/v1s/DXY_240_2026-07-06_1783576800000.json    |   1 +
 e1_tool/cache/v1s/DXY_240_2026-07-06_1783663200000.json    |   1 +
 e1_tool/cache/v1s/DXY_240_2026-10-05_1791266400000.json    |   1 +
 e1_tool/cache/v1s/DXY_240_2026-10-05_1791352800000.json    |   1 +
 e1_tool/cache/v1s/DXY_240_2026-10-05_1791439200000.json    |   1 +
 e1_tool/cache/v1s/DXY_240_2026-10-05_1791525600000.json    |   1 +
 e1_tool/cache/v1s/DXY_30_2026-04-13_1776146400000.json     |   1 +
 e1_tool/cache/v1s/DXY_30_2026-04-13_1776232800000.json     |   1 +
 e1_tool/cache/v1s/DXY_30_2026-04-20_1776751200000.json     |   1 +
 e1_tool/cache/v1s/DXY_30_2026-04-20_1776837600000.json     |   1 +
 e1_tool/cache/v1s/DXY_30_2026-04-20_1776924000000.json     |   1 +
 e1_tool/cache/v1s/DXY_30_2026-04-20_1777010400000.json     |   1 +
 e1_tool/cache/v1s/DXY_30_2026-07-06_1783404000000.json     |   1 +
 e1_tool/cache/v1s/DXY_30_2026-07-06_1783490400000.json     |   1 +
 e1_tool/cache/v1s/DXY_30_2026-07-06_1783576800000.json     |   1 +
 e1_tool/cache/v1s/DXY_30_2026-07-06_1783663200000.json     |   1 +
 e1_tool/cache/v1s/DXY_30_2026-10-05_1791266400000.json     |   1 +
 e1_tool/cache/v1s/DXY_30_2026-10-05_1791352800000.json     |   1 +
 e1_tool/cache/v1s/DXY_30_2026-10-05_1791439200000.json     |   1 +
 e1_tool/cache/v1s/DXY_30_2026-10-05_1791525600000.json     |   1 +
 e1_tool/cache/v1s/DXY_60_2026-04-13_1776146400000.json     |   1 +
 e1_tool/cache/v1s/DXY_60_2026-04-13_1776232800000.json     |   1 +
 e1_tool/cache/v1s/DXY_60_2026-04-20_1776751200000.json     |   1 +
 e1_tool/cache/v1s/DXY_60_2026-04-20_1776837600000.json     |   1 +
 e1_tool/cache/v1s/DXY_60_2026-04-20_1776924000000.json     |   1 +
 e1_tool/cache/v1s/DXY_60_2026-04-20_1777010400000.json     |   1 +
 e1_tool/cache/v1s/DXY_60_2026-07-06_1783404000000.json     |   1 +
 e1_tool/cache/v1s/DXY_60_2026-07-06_1783490400000.json     |   1 +
 e1_tool/cache/v1s/DXY_60_2026-07-06_1783576800000.json     |   1 +
 e1_tool/cache/v1s/DXY_60_2026-07-06_1783663200000.json     |   1 +
 e1_tool/cache/v1s/DXY_60_2026-10-05_1791266400000.json     |   1 +
 e1_tool/cache/v1s/DXY_60_2026-10-05_1791352800000.json     |   1 +
 e1_tool/cache/v1s/DXY_60_2026-10-05_1791439200000.json     |   1 +
 e1_tool/cache/v1s/DXY_60_2026-10-05_1791525600000.json     |   1 +
 e1_tool/cache/v1s/EURUSD_15_2026-04-13_1776146400000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_15_2026-04-13_1776232800000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_15_2026-04-20_1776751200000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_15_2026-04-20_1776837600000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_15_2026-04-20_1776924000000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_15_2026-04-20_1777010400000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_15_2026-07-06_1783404000000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_15_2026-07-06_1783490400000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_15_2026-07-06_1783576800000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_15_2026-07-06_1783663200000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_15_2026-10-05_1791266400000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_15_2026-10-05_1791352800000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_15_2026-10-05_1791439200000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_15_2026-10-05_1791525600000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_240_2026-04-13_1776146400000.json |   1 +
 e1_tool/cache/v1s/EURUSD_240_2026-04-13_1776232800000.json |   1 +
 e1_tool/cache/v1s/EURUSD_240_2026-04-20_1776751200000.json |   1 +
 e1_tool/cache/v1s/EURUSD_240_2026-04-20_1776837600000.json |   1 +
 e1_tool/cache/v1s/EURUSD_240_2026-04-20_1776924000000.json |   1 +
 e1_tool/cache/v1s/EURUSD_240_2026-04-20_1777010400000.json |   1 +
 e1_tool/cache/v1s/EURUSD_240_2026-07-06_1783404000000.json |   1 +
 e1_tool/cache/v1s/EURUSD_240_2026-07-06_1783490400000.json |   1 +
 e1_tool/cache/v1s/EURUSD_240_2026-07-06_1783576800000.json |   1 +
 e1_tool/cache/v1s/EURUSD_240_2026-07-06_1783663200000.json |   1 +
 e1_tool/cache/v1s/EURUSD_240_2026-10-05_1791266400000.json |   1 +
 e1_tool/cache/v1s/EURUSD_240_2026-10-05_1791352800000.json |   1 +
 e1_tool/cache/v1s/EURUSD_240_2026-10-05_1791439200000.json |   1 +
 e1_tool/cache/v1s/EURUSD_240_2026-10-05_1791525600000.json |   1 +
 e1_tool/cache/v1s/EURUSD_30_2026-04-13_1776146400000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_30_2026-04-13_1776232800000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_30_2026-04-20_1776751200000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_30_2026-04-20_1776837600000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_30_2026-04-20_1776924000000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_30_2026-04-20_1777010400000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_30_2026-07-06_1783404000000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_30_2026-07-06_1783490400000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_30_2026-07-06_1783576800000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_30_2026-07-06_1783663200000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_30_2026-10-05_1791266400000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_30_2026-10-05_1791352800000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_30_2026-10-05_1791439200000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_30_2026-10-05_1791525600000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_60_2026-04-13_1776146400000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_60_2026-04-13_1776232800000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_60_2026-04-20_1776751200000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_60_2026-04-20_1776837600000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_60_2026-04-20_1776924000000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_60_2026-04-20_1777010400000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_60_2026-07-06_1783404000000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_60_2026-07-06_1783490400000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_60_2026-07-06_1783576800000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_60_2026-07-06_1783663200000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_60_2026-10-05_1791266400000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_60_2026-10-05_1791352800000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_60_2026-10-05_1791439200000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_60_2026-10-05_1791525600000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-04-13_1776146400000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-04-13_1776232800000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-04-13_1776319200000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-04-13_1776405600000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-04-20_1776751200000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-04-20_1776837600000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-04-20_1776924000000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-04-20_1777010400000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-07-06_1783404000000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-07-06_1783490400000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-07-06_1783576800000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-07-06_1783663200000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-10-05_1791266400000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-04-13_1776146400000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-04-13_1776232800000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-04-13_1776319200000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-04-13_1776405600000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-04-20_1776751200000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-04-20_1776837600000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-04-20_1776924000000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-04-20_1777010400000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-07-06_1783404000000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-07-06_1783490400000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-07-06_1783576800000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-07-06_1783663200000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-10-05_1791266400000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-10-05_1791352800000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-04-13_1776146400000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-04-13_1776232800000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-04-13_1776319200000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-04-13_1776405600000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-04-20_1776751200000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-04-20_1776837600000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-04-20_1776924000000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-04-20_1777010400000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-07-06_1783404000000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-07-06_1783490400000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-07-06_1783576800000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-07-06_1783663200000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-10-05_1791266400000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-04-13_1776146400000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-04-13_1776232800000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-04-13_1776319200000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-04-13_1776405600000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-04-20_1776751200000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-04-20_1776837600000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-04-20_1776924000000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-04-20_1777010400000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-07-06_1783404000000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-07-06_1783490400000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-07-06_1783576800000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-07-06_1783663200000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-10-05_1791266400000.json  |   1 +
 e1_tool/e1_data.py                                         |   8 +++-
 e1_tool/e1_v1.py                                           |   2 +-
 e1_tool/e2_chain.py                                        |   8 +++-
 e1_tool/plutus.py                                          | 318 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++--------------------------------------
 memory/01_CURRENT_STATE.md                                 |   3 +-
 memory/03_DECISION_CHAIN.md                                |   1 +
 memory/07_EVIDENCE_LEDGER.md                               |   1 +
 tools/leak_check.py                                        |  36 ++++++++-------
 177 files changed, 431 insertions(+), 111 deletions(-)
---

## e8e095b  (2026-11-27T17:17:48+00:00)

full id: e8e095be77eefa081b28aa3a5c0b88f07e14b122

```
L-51 (in progress): the shape-chain line of a swing-scalp step drawn session by session - Asia flat, London swing to a bound, NY pre-cut pinned at the day's largest strike, post-cut swing to the other bound (P452 6.6 SESSION-LEVEL SHAPE MAPPING RULES 1-5); Engine 3 legs unchanged

M-59: 'The line is supposed to show the actual price action that is going to materialize candle by candle'.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/cache/v1s/DXY_15_2026-05-18_1779170400000.json     |  1 +
 e1_tool/cache/v1s/DXY_15_2026-05-18_1779256800000.json     |  1 +
 e1_tool/cache/v1s/DXY_15_2026-05-18_1779343200000.json     |  1 +
 e1_tool/cache/v1s/DXY_240_2026-05-18_1779170400000.json    |  1 +
 e1_tool/cache/v1s/DXY_240_2026-05-18_1779256800000.json    |  1 +
 e1_tool/cache/v1s/DXY_240_2026-05-18_1779343200000.json    |  1 +
 e1_tool/cache/v1s/DXY_240_2026-05-18_1779429600000.json    |  1 +
 e1_tool/cache/v1s/DXY_30_2026-05-18_1779170400000.json     |  1 +
 e1_tool/cache/v1s/DXY_30_2026-05-18_1779256800000.json     |  1 +
 e1_tool/cache/v1s/DXY_30_2026-05-18_1779343200000.json     |  1 +
 e1_tool/cache/v1s/DXY_60_2026-05-18_1779170400000.json     |  1 +
 e1_tool/cache/v1s/DXY_60_2026-05-18_1779256800000.json     |  1 +
 e1_tool/cache/v1s/DXY_60_2026-05-18_1779343200000.json     |  1 +
 e1_tool/cache/v1s/DXY_60_2026-05-18_1779429600000.json     |  1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-10-05_1791352800000.json  |  1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-10-05_1791439200000.json  |  1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-10-05_1791525600000.json  |  1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-10-05_1791439200000.json |  1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-10-05_1791525600000.json |  1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-10-05_1791352800000.json  |  1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-10-05_1791439200000.json  |  1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-10-05_1791525600000.json  |  1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-10-05_1791352800000.json  |  1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-10-05_1791439200000.json  |  1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-10-05_1791525600000.json  |  1 +
 e1_tool/e2_chain.py                                        | 50 ++++++++++++++++++++++++++++++++++++++++++++++++--
 memory/05_JOURNAL.md                                       |  2 ++
 memory/06_LESSONS.md                                       |  1 +
 memory/07_EVIDENCE_LEDGER.md                               |  1 +
 29 files changed, 77 insertions(+), 2 deletions(-)
---

## fe24f31  (2026-11-27T17:18:50+00:00)

full id: fe24f31d4c8617c6df6acfb2490696fc737614aa

```
V1 caches of the daily updates (per London-open instant); lib3 frames (render failed under load - ledger 110b, to be re-rendered)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/__pycache__/e2_chain.cpython-313.pyc               | Bin 108393 -> 112883 bytes
 e1_tool/cache/v1s/DXY_15_2026-05-18_1779429600000.json     |   1 +
 e1_tool/cache/v1s/DXY_30_2026-05-18_1779429600000.json     |   1 +
 e1_tool/cache/v1s/EURUSD_15_2026-05-18_1779170400000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_240_2026-05-18_1779170400000.json |   1 +
 e1_tool/cache/v1s/EURUSD_30_2026-05-18_1779170400000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_60_2026-05-18_1779170400000.json  |   1 +
 e1_tool/out/E1_GBPUSD_2026-04-13.pine                      | 216 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++------------------------------------
 evidence/lib3/GBPUSD_2026-04-13_all.png                    | Bin 0 -> 66493 bytes
 evidence/lib3/GBPUSD_2026-04-13_week.png                   | Bin 0 -> 106459 bytes
 evidence/lib3/GBPUSD_2026-04-13_zones.png                  | Bin 0 -> 43960 bytes
 11 files changed, 164 insertions(+), 58 deletions(-)
---

## 5c79a80  (2026-11-27T17:19:12+00:00)

full id: 5c79a80067d12b140e9ebc1f7d7a853459325115

```
V1 cache (daily update instant) written by the running locator

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/cache/v1s/EURUSD_240_2026-05-18_1779256800000.json | 1 +
 e1_tool/cache/v1s/EURUSD_60_2026-05-18_1779256800000.json  | 1 +
 2 files changed, 2 insertions(+)
---

## 6da7ef5  (2026-11-27T17:20:39+00:00)

full id: 6da7ef55f2339905f419d5bd7e9564e24f6ed47d

```
L-51: a swing-scalp day's line redrawn from the day's own anchor price, session by session - Asia flat, London swing to the nearer bound (P533 2.3 'magnetize toward the IL levels', D-41), NY to the other bound

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/cache/v1s/EURUSD_15_2026-05-18_1779256800000.json  |  1 +
 e1_tool/cache/v1s/EURUSD_15_2026-05-18_1779343200000.json  |  1 +
 e1_tool/cache/v1s/EURUSD_240_2026-05-18_1779343200000.json |  1 +
 e1_tool/cache/v1s/EURUSD_240_2026-05-18_1779429600000.json |  1 +
 e1_tool/cache/v1s/EURUSD_30_2026-05-18_1779256800000.json  |  1 +
 e1_tool/cache/v1s/EURUSD_30_2026-05-18_1779343200000.json  |  1 +
 e1_tool/cache/v1s/EURUSD_60_2026-05-18_1779343200000.json  |  1 +
 e1_tool/cache/v1s/EURUSD_60_2026-05-18_1779429600000.json  |  1 +
 e1_tool/plutus.py                                          | 20 +++++++++++++++++++-
 9 files changed, 27 insertions(+), 1 deletion(-)
---

## a90eb60  (2026-11-27T17:24:17+00:00)

full id: a90eb60b9946327b9789d26ac411168c47c97f4e

```
V1 caches of the daily updates for the 12 locator maps

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/__pycache__/plutus.cpython-313.pyc                 | Bin 71288 -> 73890 bytes
 e1_tool/cache/v1s/EURUSD_15_2026-05-18_1779429600000.json  |   1 +
 e1_tool/cache/v1s/EURUSD_30_2026-05-18_1779429600000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-05-18_1779170400000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-05-18_1779256800000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-05-18_1779343200000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_15_2026-05-18_1779429600000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-05-18_1779170400000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-05-18_1779256800000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-05-18_1779343200000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_240_2026-05-18_1779429600000.json |   1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-05-18_1779170400000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-05-18_1779256800000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-05-18_1779343200000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_30_2026-05-18_1779429600000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-05-18_1779170400000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-05-18_1779256800000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-05-18_1779343200000.json  |   1 +
 e1_tool/cache/v1s/GBPUSD_60_2026-05-18_1779429600000.json  |   1 +
 19 files changed, 18 insertions(+)
---

## 71fe111  (2026-11-27T17:27:00+00:00)

full id: 71fe1112ecd1f5683786df426a853f1559a02b37

```
D-137: chain re-anchor off (it cost winners on the 12-map locator), London-open zone update kept for drawing; per-day session line from each day's own price; a pending swing-scalp order rests into the next pure range day while still valid (L-52, no copies)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/plutus.py           | 11 ++++++++++-
 memory/03_DECISION_CHAIN.md |  1 +
 memory/05_JOURNAL.md        |  1 +
 3 files changed, 12 insertions(+), 1 deletion(-)
---

## 4a8313c  (2026-11-27T17:28:03+00:00)

full id: 4a8313cca2797756ba4f0587a1475d31fc28a4ad

```
bytecode refresh

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/__pycache__/plutus.cpython-313.pyc | Bin 73890 -> 74745 bytes
 1 file changed, 0 insertions(+), 0 deletions(-)
---

## 8a40708  (2026-11-27T17:30:36+00:00)

full id: 8a4070852a79453f7a9b85ff2183415a1c060cdf

```
D-138: after a chain fails, the line and day boxes follow a chain re-anchored at the London open on the rebuilt map; orders stay with the chain in force

M-59: 'if the candles don't match the exact lines that you're drawing, then your lines are not as accurate as they should be'.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/plutus.py            | 26 +++++++++++++++++++++++++-
 memory/03_DECISION_CHAIN.md  |  1 +
 memory/07_EVIDENCE_LEDGER.md |  1 +
 3 files changed, 27 insertions(+), 1 deletion(-)
---

## b13a452  (2026-11-27T17:33:08+00:00)

full id: b13a452e2e67cd37aa242947ba947d25f4229ecb

```
ledger 111b: GBPUSD Apr 13 with the daily line re-anchor vs his library chart (frames evidence/lib4)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/__pycache__/plutus.cpython-313.pyc | Bin 74745 -> 77483 bytes
 e1_tool/out/E1_GBPUSD_2026-04-13.pine      | 140 ++++++++++++++++++++++++++++++++++++++++++++++++++++++--------------------------------------------------------------------------------------
 evidence/lib4/GBPUSD_2026-04-13_all.png    | Bin 0 -> 208372 bytes
 evidence/lib4/GBPUSD_2026-04-13_week.png   | Bin 0 -> 133510 bytes
 evidence/lib4/GBPUSD_2026-04-13_zones.png  | Bin 0 -> 185082 bytes
 memory/07_EVIDENCE_LEDGER.md               |   1 +
 6 files changed, 55 insertions(+), 86 deletions(-)
---

## aa8d689  (2026-11-27T17:34:37+00:00)

full id: aa8d6892793b43f0c66232bb48220a8dd262a8c9

```
ledger 111c: golden DXY with the session line (frames evidence/lib4)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/out/E1_DXY_2026-07-06.pine     | 252 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++---------------------------------------------------------------------
 evidence/lib4/DXY_2026-07-06_all.png   | Bin 0 -> 163942 bytes
 evidence/lib4/DXY_2026-07-06_week.png  | Bin 0 -> 129955 bytes
 evidence/lib4/DXY_2026-07-06_zones.png | Bin 0 -> 100750 bytes
 memory/07_EVIDENCE_LEDGER.md           |   1 +
 5 files changed, 140 insertions(+), 113 deletions(-)
---

## 0d4ad41  (2026-11-27T17:49:49+00:00)

full id: 0d4ad41a74f076c870bb43cd206138c90ba3cceb

```
CHECKPOINT: 80% functional - DXY specific (operator M-60). Code = aa8d689: daily anchoring, unique orders, L-50 stops, London-open zone update, session line; operator: DXY golden first half + trades accurate, DXY E2 second half broken, GBPUSD poor, EURUSD to show

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 handover/80pct_dxy/CHECKPOINT.md   | 16 ++++++++++++++++
 memory/04_OPERATOR_RULINGS_LIVE.md |  1 +
 memory/12_OPERATOR_VERBATIM.md     |  3 +++
 3 files changed, 20 insertions(+)
---

## 2f31cf5  (2026-11-27T17:52:21+00:00)

full id: 2f31cf595ebeb42a1a752481e45d56aacdea810d

```
CHECKPOINT '80% functional - DXY specific' made self-contained: code + context (memory incl. SESSION FACTS 2026-11-27, rulings L-46..L-56, decisions D-129..D-138, lessons, ledger) + the OmniGraph (store rebuilt from memory: 1572 nodes / 1029 edges, full JSONL export) + manifest

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 handover/80pct_dxy/CHECKPOINT.md                                                                                              |    7 +
 handover/80pct_dxy/MANIFEST.sha256                                                                                            | 4750 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 handover/80pct_dxy/omnigraph/export_stderr.txt                                                                                |    1 +
 handover/80pct_dxy/omnigraph/graph_export.jsonl                                                                               | 4173 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 .../graph_store/graph.omni/__history/schemas/90384b18fe613e08dd4bd7a605166fbbebf8330897302b89c6998c542b307e9b.schema          |  Bin 0 -> 52231 bytes
 handover/80pct_dxy/omnigraph/graph_store/graph.omni/__manifest/_transactions/0-31df9f00-c4cc-453a-96d7-e89e2e819691.txn       |  Bin 0 -> 1274 bytes
 handover/80pct_dxy/omnigraph/graph_store/graph.omni/__manifest/_transactions/1-616e0573-6432-434a-af30-5cb576742b6f.txn       |  Bin 0 -> 1276 bytes
 handover/80pct_dxy/omnigraph/graph_store/graph.omni/__manifest/_transactions/2-85e542c7-c3cd-4c94-a49d-1d7f67a003a2.txn       |  Bin 0 -> 1276 bytes
 handover/80pct_dxy/omnigraph/graph_store/graph.omni/__manifest/_versions/18446744073709551612.manifest                        |  Bin 0 -> 2711 bytes
 handover/80pct_dxy/omnigraph/graph_store/graph.omni/__manifest/_versions/18446744073709551613.manifest                        |  Bin 0 -> 2711 bytes
 handover/80pct_dxy/omnigraph/graph_store/graph.omni/__manifest/_versions/18446744073709551614.manifest                        |  Bin 0 -> 2705 bytes
 handover/80pct_dxy/omnigraph/graph_store/graph.omni/__manifest/_versions/latest_version_hint.json                             |    1 +
 handover/80pct_dxy/omnigraph/graph_store/graph.omni/__manifest/data/00001000101001010101011067bf134e71a4b84fe78e3957cd.lance  |  Bin 0 -> 62323 bytes
 handover/80pct_dxy/omnigraph/graph_store/graph.omni/__manifest/data/001000011111001111000000590cbe4202a06fab03106df62c.lance  |  Bin 0 -> 66547 bytes
 handover/80pct_dxy/omnigraph/graph_store/graph.omni/__manifest/data/1000100101111110101101011042db4b31a0db2c1b8421f260.lance  |  Bin 0 -> 67763 bytes
 .../graph_store/graph.omni/edges/000000000000000a-000000000000004c/_transactions/0-3c2f17a7-d971-4fd0-a8e3-d204111a5c06.txn   |    2 +
 .../graph_store/graph.omni/edges/000000000000000a-000000000000004c/_transactions/1-6d22e892-2ee0-4e2f-902a-596af31cc035.txn   |  Bin 0 -> 33135 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000a-000000000000004c/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000a-000000000000004c/_versions/d10083998346664226321.manifest         |  Bin 0 -> 33529 bytes
 .../80pct_dxy/omnigraph/graph_store/graph.omni/edges/000000000000000a-000000000000004c/_versions/latest_version_hint.json     |    1 +
 .../graph.omni/edges/000000000000000a-000000000000004c/data/001010110111101101110000b562dd476e92bb857d35e415aa.lance          |  Bin 0 -> 34418 bytes
 .../graph_store/graph.omni/edges/000000000000000b-000000000000004d/_transactions/0-5f19f927-525d-41e4-9275-91000fec1c61.txn   |    2 +
 .../omnigraph/graph_store/graph.omni/edges/000000000000000b-000000000000004d/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../80pct_dxy/omnigraph/graph_store/graph.omni/edges/000000000000000b-000000000000004d/_versions/latest_version_hint.json     |    1 +
 .../graph_store/graph.omni/edges/000000000000000c-000000000000004e/_transactions/0-bbdb21b9-f0fd-4577-8fe0-012118d920f8.txn   |    2 +
 .../omnigraph/graph_store/graph.omni/edges/000000000000000c-000000000000004e/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../80pct_dxy/omnigraph/graph_store/graph.omni/edges/000000000000000c-000000000000004e/_versions/latest_version_hint.json     |    1 +
 .../graph_store/graph.omni/edges/000000000000000d-000000000000004f/_transactions/0-29fca0b6-6443-461f-bfc0-f89287feba54.txn   |    2 +
 .../omnigraph/graph_store/graph.omni/edges/000000000000000d-000000000000004f/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../80pct_dxy/omnigraph/graph_store/graph.omni/edges/000000000000000d-000000000000004f/_versions/latest_version_hint.json     |    1 +
 .../graph_store/graph.omni/edges/000000000000000e-0000000000000050/_transactions/0-df95cb6c-b3dd-4101-b756-f821b8df0d9b.txn   |    2 +
 .../graph_store/graph.omni/edges/000000000000000e-0000000000000050/_transactions/1-6643dafe-c475-4b5f-862a-6a6b10fff95d.txn   |  Bin 0 -> 33133 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000e-0000000000000050/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000e-0000000000000050/_versions/d18293233000488807391.manifest         |  Bin 0 -> 33521 bytes
 .../80pct_dxy/omnigraph/graph_store/graph.omni/edges/000000000000000e-0000000000000050/_versions/latest_version_hint.json     |    1 +
 .../graph.omni/edges/000000000000000e-0000000000000050/data/001100011101111111011110e5375749479b1603b21ed4d23b.lance          |  Bin 0 -> 733 bytes
 .../graph.omni/nodes/0000000000000002-0000000000000044/_indices/7a848bee-38ea-46d3-992f-0a20c2258db2/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000002-0000000000000044/_indices/7a848bee-38ea-46d3-992f-0a20c2258db2/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000002-0000000000000044/_indices/80dc8fbe-d123-4512-80d8-d2ec94b161a4/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000002-0000000000000044/_indices/80dc8fbe-d123-4512-80d8-d2ec94b161a4/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000002-0000000000000044/_indices/85685cba-c06d-4ff0-98b3-8e006fe9c7b6/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000002-0000000000000044/_indices/85685cba-c06d-4ff0-98b3-8e006fe9c7b6/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_transactions/0-c7712376-15b0-4597-b0f3-e6eac86d0d77.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_transactions/1-a174a46c-297f-4450-bab5-898e3eb60c2c.txn   |  Bin 0 -> 33114 bytes
 .../nodes/0000000000000002-0000000000000044/_transactions/18390541781096887630-f859bce8-9c93-4cdb-a1e0-7fb401553120.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_versions/d17183764136427451290.manifest         |  Bin 0 -> 2159 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_versions/d18390541781096887630.manifest         |  Bin 0 -> 33881 bytes
 .../80pct_dxy/omnigraph/graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_versions/latest_version_hint.json     |    1 +
 .../graph.omni/nodes/0000000000000002-0000000000000044/data/001110101001001001001011bc54a141c5a2575177741a25af.lance          |  Bin 0 -> 31561 bytes
 .../graph.omni/nodes/0000000000000003-0000000000000045/_indices/0bb4405a-3de5-40eb-9916-ef52e8d3ac09/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000003-0000000000000045/_indices/0bb4405a-3de5-40eb-9916-ef52e8d3ac09/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000003-0000000000000045/_indices/c0aa21b7-9ddc-41ff-ac1b-27bb9ded968c/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000003-0000000000000045/_indices/c0aa21b7-9ddc-41ff-ac1b-27bb9ded968c/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000003-0000000000000045/_indices/fe6ded2a-c32b-48f6-a8d4-d8433fbce1ae/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000003-0000000000000045/_indices/fe6ded2a-c32b-48f6-a8d4-d8433fbce1ae/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_transactions/0-3902f456-7778-4fb6-93a6-5be4b9110e8e.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_transactions/1-bf820690-32b0-42d0-bff3-d32ccd5fba00.txn   |  Bin 0 -> 33115 bytes
 .../nodes/0000000000000003-0000000000000045/_transactions/16179062777237315030-d2bbf231-6253-49e2-8ada-385f8fa74313.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_versions/d15545539552415415991.manifest         |  Bin 0 -> 2164 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_versions/d16179062777237315030.manifest         |  Bin 0 -> 33887 bytes
 .../80pct_dxy/omnigraph/graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_versions/latest_version_hint.json     |    1 +
 .../graph.omni/nodes/0000000000000003-0000000000000045/data/1011110111101011100101109c5aaf41508631bc038352ed35.lance          |  Bin 0 -> 92843 bytes
 .../graph.omni/nodes/0000000000000004-0000000000000046/_indices/0babb222-3cb1-4ae4-ac07-2bbda68819fc/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000004-0000000000000046/_indices/0babb222-3cb1-4ae4-ac07-2bbda68819fc/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000004-0000000000000046/_indices/77fffd52-e456-4110-8c15-7a926f41ebf9/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000004-0000000000000046/_indices/77fffd52-e456-4110-8c15-7a926f41ebf9/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_transactions/0-4ba5481c-d03b-4e53-ae1a-e16b8e88298c.txn   |    7 +
 .../graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_transactions/1-be0a8cb8-cd2b-4f22-ba0b-77670af4ce7d.txn   |  Bin 0 -> 33111 bytes
 .../nodes/0000000000000004-0000000000000046/_transactions/16606069130990546960-90ed72f3-74e3-4f30-a118-d0833daf690c.txn       |  Bin 0 -> 581 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_versions/18446744073709551614.manifest          |  Bin 0 -> 990 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_versions/d12138904124088172469.manifest         |  Bin 0 -> 1670 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_versions/d16606069130990546960.manifest         |  Bin 0 -> 33783 bytes
 .../80pct_dxy/omnigraph/graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_versions/latest_version_hint.json     |    1 +
 .../graph.omni/nodes/0000000000000004-0000000000000046/data/0111111000100100011111013fa4e74f2bb605a986e631cd44.lance          |  Bin 0 -> 1184813 bytes
 .../graph.omni/nodes/0000000000000005-0000000000000047/_indices/4aa61965-5d50-41f2-8c20-15b05a92517c/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000005-0000000000000047/_indices/4aa61965-5d50-41f2-8c20-15b05a92517c/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000005-0000000000000047/_indices/c7e590c2-2acc-4750-aa28-f8b47355b5e6/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000005-0000000000000047/_indices/c7e590c2-2acc-4750-aa28-f8b47355b5e6/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000005-0000000000000047/_indices/eb4f85fc-b731-4f89-bafc-bbaa714604b3/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000005-0000000000000047/_indices/eb4f85fc-b731-4f89-bafc-bbaa714604b3/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_transactions/0-4469fec4-cc25-4534-9709-3325d7d68562.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_transactions/1-1bb50f3e-ce06-46f2-a6c5-4338d0212367.txn   |  Bin 0 -> 33115 bytes
 .../nodes/0000000000000005-0000000000000047/_transactions/10687564101123986965-efd75ab4-bff6-4675-b892-0ad8d73a97a4.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_versions/d10298360789686467516.manifest         |  Bin 0 -> 2164 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_versions/d10687564101123986965.manifest         |  Bin 0 -> 33888 bytes
 .../80pct_dxy/omnigraph/graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_versions/latest_version_hint.json     |    1 +
 .../graph.omni/nodes/0000000000000005-0000000000000047/data/0000001110110000110111117b914e4a9eb50cbf9d9cd721c5.lance          |  Bin 0 -> 103097 bytes
 .../graph.omni/nodes/0000000000000006-0000000000000048/_indices/9df1b0f4-3edb-4073-a1a7-c70fc84b53d5/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000006-0000000000000048/_indices/9df1b0f4-3edb-4073-a1a7-c70fc84b53d5/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000006-0000000000000048/_indices/cdca6f07-f96d-47f9-92e8-4abf1ebeb080/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000006-0000000000000048/_indices/cdca6f07-f96d-47f9-92e8-4abf1ebeb080/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000006-0000000000000048/_indices/eb0779bc-d898-400b-8525-82d7e5f14e2a/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000006-0000000000000048/_indices/eb0779bc-d898-400b-8525-82d7e5f14e2a/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_transactions/0-ae945c31-68e0-47f7-bf82-1ecdfc57ee50.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_transactions/1-35cb54d9-019e-4a5c-89a4-5b73cc8d794e.txn   |  Bin 0 -> 33115 bytes
 .../nodes/0000000000000006-0000000000000048/_transactions/10300592904127219424-c3b64eac-efb2-4b23-8955-aee301210e05.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_versions/d10300592904127219424.manifest         |  Bin 0 -> 33888 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_versions/d16250925430167512232.manifest         |  Bin 0 -> 2164 bytes
 .../80pct_dxy/omnigraph/graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_versions/latest_version_hint.json     |    1 +
 .../graph.omni/nodes/0000000000000006-0000000000000048/data/010110111001010010101101c7be2c46198fb68a09675ec68c.lance          |  Bin 0 -> 453198 bytes
 .../graph.omni/nodes/0000000000000007-0000000000000049/_indices/03d2fe07-e282-4b4e-a779-45841d58bec7/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000007-0000000000000049/_indices/03d2fe07-e282-4b4e-a779-45841d58bec7/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000007-0000000000000049/_indices/15bdd3aa-cb37-4328-9813-dc533055193d/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000007-0000000000000049/_indices/15bdd3aa-cb37-4328-9813-dc533055193d/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000007-0000000000000049/_indices/d8631b6a-5c90-4ab9-928a-1b5fcc3260aa/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000007-0000000000000049/_indices/d8631b6a-5c90-4ab9-928a-1b5fcc3260aa/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_transactions/0-bdbb6c3b-50fb-407b-af7c-6b129cacf661.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_transactions/1-d38abd27-fe89-4908-b831-568544e7cac0.txn   |  Bin 0 -> 33114 bytes
 .../nodes/0000000000000007-0000000000000049/_transactions/13839065596565168050-c6815ccb-a454-41f1-9f4c-00858fbd671b.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_versions/d12450232401925146029.manifest         |  Bin 0 -> 2159 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_versions/d13839065596565168050.manifest         |  Bin 0 -> 33882 bytes
 .../80pct_dxy/omnigraph/graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_versions/latest_version_hint.json     |    1 +
 .../graph.omni/nodes/0000000000000007-0000000000000049/data/1101100101011101101011012c35a3452283bb4ce21e922591.lance          |  Bin 0 -> 20121 bytes
 .../graph.omni/nodes/0000000000000008-000000000000004a/_indices/23c4b03f-df09-45d8-8457-3950a0796c86/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000008-000000000000004a/_indices/23c4b03f-df09-45d8-8457-3950a0796c86/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000008-000000000000004a/_indices/48780c67-0b76-489b-b507-ccfd45f4edd7/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000008-000000000000004a/_indices/48780c67-0b76-489b-b507-ccfd45f4edd7/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000008-000000000000004a/_indices/8a9e021f-2bc4-462a-8719-cd1a9f13e465/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000008-000000000000004a/_indices/8a9e021f-2bc4-462a-8719-cd1a9f13e465/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_transactions/0-5d7f1c16-9492-48f0-8d88-aaaa00a6b4b0.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_transactions/1-f40dd0b4-1235-4944-bc0a-9cd068f25979.txn   |  Bin 0 -> 33114 bytes
 .../nodes/0000000000000008-000000000000004a/_transactions/12575180444830862809-1f56b164-c793-4de6-b2bd-2de823b25fff.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_versions/d12575180444830862809.manifest         |  Bin 0 -> 33882 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_versions/d13895845876553589656.manifest         |  Bin 0 -> 2159 bytes
 .../80pct_dxy/omnigraph/graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_versions/latest_version_hint.json     |    1 +
 .../graph.omni/nodes/0000000000000008-000000000000004a/data/010100101111100101110100b4f93d4672bd67b5527d2bcbc0.lance          |  Bin 0 -> 35433 bytes
 .../graph.omni/nodes/0000000000000009-000000000000004b/_indices/206e3c13-ccc1-4758-b4d9-a4c8b6a52abf/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000009-000000000000004b/_indices/206e3c13-ccc1-4758-b4d9-a4c8b6a52abf/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000009-000000000000004b/_indices/9bdb471a-3853-48b0-85e3-da99a0f92c66/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000009-000000000000004b/_indices/9bdb471a-3853-48b0-85e3-da99a0f92c66/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000009-000000000000004b/_indices/b954ce39-baad-4543-afe1-514e79850832/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000009-000000000000004b/_indices/b954ce39-baad-4543-afe1-514e79850832/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_transactions/0-d069e674-d8ab-47c1-82ae-bbdba2d5f782.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_transactions/1-b32304e9-39c3-4de3-9003-ebf769ea7ae5.txn   |  Bin 0 -> 33114 bytes
 .../nodes/0000000000000009-000000000000004b/_transactions/13587739488197583449-d78fec63-8360-439d-af6a-386eb826f6bc.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_versions/d10085657637946760012.manifest         |  Bin 0 -> 2159 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_versions/d13587739488197583449.manifest         |  Bin 0 -> 33882 bytes
 .../80pct_dxy/omnigraph/graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_versions/latest_version_hint.json     |    1 +
 .../graph.omni/nodes/0000000000000009-000000000000004b/data/001101100100010110000101529a2d40c39866e880a0df4d08.lance          |  Bin 0 -> 22603 bytes
 handover/80pct_dxy/omnigraph/graph_store/last_sync.jsonl                                                                      | 4173 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 handover/80pct_dxy/omnigraph/graph_store/state.json                                                                           |   44 +
 handover/80pct_dxy/omnigraph/mem_ls.txt                                                                                       | 1573 ++++++++++++++++++++++
 handover/80pct_dxy/omnigraph/mem_status.txt                                                                                   |   27 +
 memory/01_CURRENT_STATE.md                                                                                                    |    5 +
 memory/05_JOURNAL.md                                                                                                          |    1 +
 memory/06_LESSONS.md                                                                                                          |    4 +
 memory/08_FACTS.md                                                                                                            |   28 +
 154 files changed, 14903 insertions(+)
---

## e3860c7  (2026-11-27T17:56:08+00:00)

full id: e3860c787e677462be1571d681ae799d4a2dee6e

```
M-60 frames: golden week whole-week screenshots for DXY, EURUSD, GBPUSD (tools/weekframe, one render at a time); ledger 112 with the Wed-Fri diagnosis

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/out/E1_EURUSD_2026-07-06.pine       | 233 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++----------------------------------------------------------------
 e1_tool/out/E1_GBPUSD_2026-07-06.pine       | 212 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++----------------------------------------------------------
 evidence/m60/DXY_2026-07-06_fullweek.png    | Bin 0 -> 129871 bytes
 evidence/m60/EURUSD_2026-07-06_fullweek.png | Bin 0 -> 131609 bytes
 evidence/m60/GBPUSD_2026-07-06_fullweek.png | Bin 0 -> 127978 bytes
 memory/07_EVIDENCE_LEDGER.md                |   1 +
 tools/weekframe                             |  13 +++++++++
 7 files changed, 268 insertions(+), 191 deletions(-)
---

## 59c98fe  (2026-11-27T17:57:33+00:00)

full id: 59c98feb1d8ff472ff07944bf4b607e21df41d24

```
D-139: 6.10 '2-3 more 4H candles' as +12 hours instead of doubling the breakout's sessions - golden DXY Friday whiplash + reversal move into Friday London; golden trades unchanged

P533:2048 'A 4H breakout that appears imminent may take 2-3 more 4H candles to complete than initially predicted'.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/e2_chain.py         | 12 ++++++++++--
 memory/03_DECISION_CHAIN.md |  1 +
 2 files changed, 11 insertions(+), 2 deletions(-)
---

## d642f22  (2026-11-27T17:59:22+00:00)

full id: d642f220d2dc1b7cea48382cf467735d5a38de62

```
journal: D-139 locator results (orders 26 TP / 8 SL, day map 54/80 unchanged)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 memory/05_JOURNAL.md | 1 +
 1 file changed, 1 insertion(+)
---

## d48d3e9  (2026-11-27T18:00:24+00:00)

full id: d48d3e9c35d3f6c8fd29eba085729f4063496293

```
D-140: breakouts over several sessions drawn as a session ladder (zone to zone, Asia holds); non-range days hold the open through Asia and join the chain at the London open - golden DXY Wed-Fri line now steps with the candles

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/__pycache__/e2_chain.cpython-313.pyc | Bin 112883 -> 113517 bytes
 e1_tool/e2_chain.py                          |  35 ++++++++++++++++++++++++++++++++++-
 e1_tool/plutus.py                            |   8 +++++++-
 memory/03_DECISION_CHAIN.md                  |   1 +
 4 files changed, 42 insertions(+), 2 deletions(-)
---

## bac6b50  (2026-11-27T18:02:25+00:00)

full id: bac6b502db7e5d96e6db1da59ba6ee1eb2da2fc9

```
ledger 113: golden week whole-week frames after D-139 / D-140 (evidence/m60b)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/__pycache__/e2_chain.cpython-313.pyc | Bin 113517 -> 116972 bytes
 e1_tool/__pycache__/plutus.cpython-313.pyc   | Bin 77483 -> 77754 bytes
 e1_tool/out/E1_DXY_2026-07-06.pine           |  72 ++++++++++++++++++++++++++++++++++++++----------------------------------
 e1_tool/out/E1_EURUSD_2026-07-06.pine        |  64 +++++++++++++++++++++++++++++++++-------------------------------
 e1_tool/out/E1_GBPUSD_2026-07-06.pine        |  68 +++++++++++++++++++++++++++++++++++---------------------------------
 evidence/m60b/DXY_2026-07-06_fullweek.png    | Bin 0 -> 129024 bytes
 evidence/m60b/EURUSD_2026-07-06_fullweek.png | Bin 0 -> 130618 bytes
 evidence/m60b/GBPUSD_2026-07-06_fullweek.png | Bin 0 -> 128653 bytes
 memory/07_EVIDENCE_LEDGER.md                 |   1 +
 9 files changed, 107 insertions(+), 98 deletions(-)
---

## cea1954  (2026-11-27T18:23:08+00:00)

full id: cea1954d5205f7a6065abbb91275a1e6850ac185

```
CHECKPOINT '85% functional - DXY + GU' (V1, operator M-61): code bac6b50 (D-139 + D-140) + context (memory incl. M-61 / L-57) + OmniGraph rebuilt from memory (1579 nodes / 1049 edges, store + full export) + manifest; tools/checkpoint packages each checkpoint the same way

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 handover/85pct_dxy_gu/CHECKPOINT.md                                                                                           |   10 +
 handover/85pct_dxy_gu/MANIFEST.sha256                                                                                         | 4909 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 handover/85pct_dxy_gu/omnigraph/export_stderr.txt                                                                             |    1 +
 handover/85pct_dxy_gu/omnigraph/graph_export.jsonl                                                                            | 4207 +++++++++++++++++++++++++++++++++++++++++++++++++++++++
 .../graph_store/graph.omni/__history/schemas/2cd50cc06bd896be47be3bb9667e3da951d9fb435cb958a1ad83281d02d0d2f7.schema          |  Bin 0 -> 52231 bytes
 handover/85pct_dxy_gu/omnigraph/graph_store/graph.omni/__manifest/_transactions/0-0f9ab7a9-81c2-4ffe-bcdd-562757e0e7b7.txn    |  Bin 0 -> 1274 bytes
 handover/85pct_dxy_gu/omnigraph/graph_store/graph.omni/__manifest/_transactions/1-8caba329-2fb7-419f-b2b1-7b3b14f64570.txn    |  Bin 0 -> 1276 bytes
 handover/85pct_dxy_gu/omnigraph/graph_store/graph.omni/__manifest/_transactions/2-48c842de-125e-421c-8382-4cde26eb0b27.txn    |  Bin 0 -> 1276 bytes
 handover/85pct_dxy_gu/omnigraph/graph_store/graph.omni/__manifest/_versions/18446744073709551612.manifest                     |  Bin 0 -> 2710 bytes
 handover/85pct_dxy_gu/omnigraph/graph_store/graph.omni/__manifest/_versions/18446744073709551613.manifest                     |  Bin 0 -> 2710 bytes
 handover/85pct_dxy_gu/omnigraph/graph_store/graph.omni/__manifest/_versions/18446744073709551614.manifest                     |  Bin 0 -> 2705 bytes
 handover/85pct_dxy_gu/omnigraph/graph_store/graph.omni/__manifest/_versions/latest_version_hint.json                          |    1 +
 .../85pct_dxy_gu/omnigraph/graph_store/graph.omni/__manifest/data/0101000101000000111101105bc0574238af4d86767331c784.lance    |  Bin 0 -> 67699 bytes
 .../85pct_dxy_gu/omnigraph/graph_store/graph.omni/__manifest/data/1010011010110000011100110f2ace4ea2bebc63b1e7d5da37.lance    |  Bin 0 -> 66547 bytes
 .../85pct_dxy_gu/omnigraph/graph_store/graph.omni/__manifest/data/1100110100101101000011104003c04aa2a73e459217c2f82a.lance    |  Bin 0 -> 62323 bytes
 .../graph_store/graph.omni/edges/000000000000000a-000000000000004c/_transactions/0-684ee2a4-ecfd-4760-ba85-64303eee0c48.txn   |    2 +
 .../graph_store/graph.omni/edges/000000000000000a-000000000000004c/_transactions/1-12978b41-12bc-4f9b-9228-f2b96909473d.txn   |  Bin 0 -> 33135 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000a-000000000000004c/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000a-000000000000004c/_versions/d15415407592364153798.manifest         |  Bin 0 -> 33528 bytes
 .../85pct_dxy_gu/omnigraph/graph_store/graph.omni/edges/000000000000000a-000000000000004c/_versions/latest_version_hint.json  |    1 +
 .../graph.omni/edges/000000000000000a-000000000000004c/data/101111010001101100111100984c384ea3b1b990afa03188e0.lance          |  Bin 0 -> 34930 bytes
 .../graph_store/graph.omni/edges/000000000000000b-000000000000004d/_transactions/0-182addc0-83bf-4c6a-8e8e-5272b7886b5e.txn   |    2 +
 .../omnigraph/graph_store/graph.omni/edges/000000000000000b-000000000000004d/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../85pct_dxy_gu/omnigraph/graph_store/graph.omni/edges/000000000000000b-000000000000004d/_versions/latest_version_hint.json  |    1 +
 .../graph_store/graph.omni/edges/000000000000000c-000000000000004e/_transactions/0-c19b23c7-4f26-4ec8-864e-33cb6b9f083c.txn   |    2 +
 .../omnigraph/graph_store/graph.omni/edges/000000000000000c-000000000000004e/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../85pct_dxy_gu/omnigraph/graph_store/graph.omni/edges/000000000000000c-000000000000004e/_versions/latest_version_hint.json  |    1 +
 .../graph_store/graph.omni/edges/000000000000000d-000000000000004f/_transactions/0-7d01f5f9-d8f3-4ee3-88aa-0ab5f588537e.txn   |    2 +
 .../omnigraph/graph_store/graph.omni/edges/000000000000000d-000000000000004f/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../85pct_dxy_gu/omnigraph/graph_store/graph.omni/edges/000000000000000d-000000000000004f/_versions/latest_version_hint.json  |    1 +
 .../graph_store/graph.omni/edges/000000000000000e-0000000000000050/_transactions/0-3262cfe9-fe3d-40ab-8065-03216e4bcda7.txn   |    2 +
 .../graph_store/graph.omni/edges/000000000000000e-0000000000000050/_transactions/1-bb381891-c756-4331-afd4-7b886d628fa9.txn   |  Bin 0 -> 33133 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000e-0000000000000050/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000e-0000000000000050/_versions/d10376435600868714112.manifest         |  Bin 0 -> 33520 bytes
 .../85pct_dxy_gu/omnigraph/graph_store/graph.omni/edges/000000000000000e-0000000000000050/_versions/latest_version_hint.json  |    1 +
 .../graph.omni/edges/000000000000000e-0000000000000050/data/000000010100010001110111b31c5b440a9f5e0da839dbf558.lance          |  Bin 0 -> 733 bytes
 .../graph.omni/nodes/0000000000000002-0000000000000044/_indices/2ed2d068-8696-48b7-953a-26ffd6278d34/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000002-0000000000000044/_indices/2ed2d068-8696-48b7-953a-26ffd6278d34/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000002-0000000000000044/_indices/aec15b5e-5d22-4783-bf35-57c8564658ed/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000002-0000000000000044/_indices/aec15b5e-5d22-4783-bf35-57c8564658ed/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000002-0000000000000044/_indices/f8c87afc-8c62-4f99-94fa-0ae8f73c37f3/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000002-0000000000000044/_indices/f8c87afc-8c62-4f99-94fa-0ae8f73c37f3/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_transactions/0-fa5fce00-ab5a-4113-996c-0cdf58ef6808.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_transactions/1-84378587-cfd0-4517-9d0a-2a73362361b8.txn   |  Bin 0 -> 33114 bytes
 .../nodes/0000000000000002-0000000000000044/_transactions/9845153900348018545-fbc93ec5-975c-4a7e-9fdf-be893a0e0f51.txn        |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_versions/d16173990685065121732.manifest         |  Bin 0 -> 2157 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_versions/d9845153900348018545.manifest          |  Bin 0 -> 33881 bytes
 .../85pct_dxy_gu/omnigraph/graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_versions/latest_version_hint.json  |    1 +
 .../graph.omni/nodes/0000000000000002-0000000000000044/data/0100010000101111101000015d722241269d1b46f960a80f51.lance          |  Bin 0 -> 32393 bytes
 .../graph.omni/nodes/0000000000000003-0000000000000045/_indices/43fcd005-1b63-4da4-8ffc-351d5e4db21a/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000003-0000000000000045/_indices/43fcd005-1b63-4da4-8ffc-351d5e4db21a/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000003-0000000000000045/_indices/9165138f-8976-4ae5-a7a8-a0cc0dcb39a6/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000003-0000000000000045/_indices/9165138f-8976-4ae5-a7a8-a0cc0dcb39a6/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000003-0000000000000045/_indices/af02383b-a1dc-4802-af06-2d7efecc7169/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000003-0000000000000045/_indices/af02383b-a1dc-4802-af06-2d7efecc7169/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_transactions/0-be184ae8-549c-4a60-8f66-0490fa60cd98.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_transactions/1-79025be4-c7ef-4d61-a085-1ace9791e620.txn   |  Bin 0 -> 33115 bytes
 .../nodes/0000000000000003-0000000000000045/_transactions/10620859778894889400-d3dea810-49af-47d6-aeb9-c58146418c69.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_versions/d10620859778894889400.manifest         |  Bin 0 -> 33887 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_versions/d14758049329239704887.manifest         |  Bin 0 -> 2163 bytes
 .../85pct_dxy_gu/omnigraph/graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_versions/latest_version_hint.json  |    1 +
 .../graph.omni/nodes/0000000000000003-0000000000000045/data/101110000111010011010111318dfe4892811baf7195f6ef48.lance          |  Bin 0 -> 94699 bytes
 .../graph.omni/nodes/0000000000000004-0000000000000046/_indices/627f2be1-96c4-4258-85da-629af18786a7/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000004-0000000000000046/_indices/627f2be1-96c4-4258-85da-629af18786a7/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000004-0000000000000046/_indices/84cd2121-4001-4b6c-a444-659a555f6409/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000004-0000000000000046/_indices/84cd2121-4001-4b6c-a444-659a555f6409/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_transactions/0-5df4e818-b1de-48fe-9038-b4a517fb9ebf.txn   |    7 +
 .../graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_transactions/1-16c0c73f-fba5-465b-9a96-d168eeb93e01.txn   |  Bin 0 -> 33111 bytes
 .../nodes/0000000000000004-0000000000000046/_transactions/13686066951790014821-751e5812-dcca-4436-8afe-0196ffa85ccd.txn       |  Bin 0 -> 581 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_versions/18446744073709551614.manifest          |  Bin 0 -> 990 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_versions/d13411282166905338341.manifest         |  Bin 0 -> 1669 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_versions/d13686066951790014821.manifest         |  Bin 0 -> 33783 bytes
 .../85pct_dxy_gu/omnigraph/graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_versions/latest_version_hint.json  |    1 +
 .../graph.omni/nodes/0000000000000004-0000000000000046/data/1010111011110100100000012a4e33465ca2055b90cb40c7c0.lance          |  Bin 0 -> 1211949 bytes
 .../graph.omni/nodes/0000000000000005-0000000000000047/_indices/3eb055c1-5df3-4f74-af5f-368dd42b8237/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000005-0000000000000047/_indices/3eb055c1-5df3-4f74-af5f-368dd42b8237/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000005-0000000000000047/_indices/686e69d1-07cd-471f-bb88-1335bc0bc990/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000005-0000000000000047/_indices/686e69d1-07cd-471f-bb88-1335bc0bc990/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000005-0000000000000047/_indices/ec0cd563-7485-4129-af66-646c3d74a64e/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000005-0000000000000047/_indices/ec0cd563-7485-4129-af66-646c3d74a64e/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_transactions/0-bce5e88a-5978-4cc4-8a11-a411246d5296.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_transactions/1-c2ed8f5c-b7f7-44f8-aafd-9191823ae9ed.txn   |  Bin 0 -> 33115 bytes
 .../nodes/0000000000000005-0000000000000047/_transactions/9319257820653685445-222eabdd-9c31-4d87-9448-b9d133be58b1.txn        |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_versions/d15710944178526707919.manifest         |  Bin 0 -> 2162 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_versions/d9319257820653685445.manifest          |  Bin 0 -> 33887 bytes
 .../85pct_dxy_gu/omnigraph/graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_versions/latest_version_hint.json  |    1 +
 .../graph.omni/nodes/0000000000000005-0000000000000047/data/010000011110100100010101fe143642c6971e6c028af0ff92.lance          |  Bin 0 -> 103289 bytes
 .../graph.omni/nodes/0000000000000006-0000000000000048/_indices/4c023100-1a8d-4e6e-92e5-3a6fff0529c8/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000006-0000000000000048/_indices/4c023100-1a8d-4e6e-92e5-3a6fff0529c8/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000006-0000000000000048/_indices/9cd4a70c-85e7-44dc-ac00-999bfd3e18a1/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000006-0000000000000048/_indices/9cd4a70c-85e7-44dc-ac00-999bfd3e18a1/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000006-0000000000000048/_indices/bb74b7f0-dfd2-418c-b280-80ae785ab0df/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000006-0000000000000048/_indices/bb74b7f0-dfd2-418c-b280-80ae785ab0df/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_transactions/0-50705c30-33ea-432f-87e2-d9df0082e7ce.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_transactions/1-bb9a1e21-7423-4f93-bc23-2161e5d435a9.txn   |  Bin 0 -> 33115 bytes
 .../nodes/0000000000000006-0000000000000048/_transactions/16712796631213845411-c15ad34a-e61a-4378-acfd-91995802e5b0.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_versions/d10763919030539502144.manifest         |  Bin 0 -> 2163 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_versions/d16712796631213845411.manifest         |  Bin 0 -> 33887 bytes
 .../85pct_dxy_gu/omnigraph/graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_versions/latest_version_hint.json  |    1 +
 .../graph.omni/nodes/0000000000000006-0000000000000048/data/001001001111011010010001b3991b4dcb8200a9cd425878eb.lance          |  Bin 0 -> 453006 bytes
 .../graph.omni/nodes/0000000000000007-0000000000000049/_indices/0fa087d5-c1f6-439b-8c15-4f65bc0976fa/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000007-0000000000000049/_indices/0fa087d5-c1f6-439b-8c15-4f65bc0976fa/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000007-0000000000000049/_indices/1d632396-9e79-4c09-8c96-ea14c94933d3/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000007-0000000000000049/_indices/1d632396-9e79-4c09-8c96-ea14c94933d3/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000007-0000000000000049/_indices/49e3da93-778a-40cb-91db-a37e78169616/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000007-0000000000000049/_indices/49e3da93-778a-40cb-91db-a37e78169616/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_transactions/0-dccd0426-cb9c-44c2-8b3b-02762caef8bb.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_transactions/1-d3e25fd2-d78a-494b-b92b-2dabe660c058.txn   |  Bin 0 -> 33114 bytes
 .../nodes/0000000000000007-0000000000000049/_transactions/16131100782619522142-bff7123d-1b32-4bea-ad3a-3a32cead56f7.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_versions/d13527835417743382895.manifest         |  Bin 0 -> 2158 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_versions/d16131100782619522142.manifest         |  Bin 0 -> 33881 bytes
 .../85pct_dxy_gu/omnigraph/graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_versions/latest_version_hint.json  |    1 +
 .../graph.omni/nodes/0000000000000007-0000000000000049/data/10001110010001110111001118db73479d9f98d98d3e379191.lance          |  Bin 0 -> 20121 bytes
 .../graph.omni/nodes/0000000000000008-000000000000004a/_indices/5b391681-5876-41b9-ab05-4209c3bab54b/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000008-000000000000004a/_indices/5b391681-5876-41b9-ab05-4209c3bab54b/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000008-000000000000004a/_indices/93a455f5-0479-4009-baca-7445f27c22af/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000008-000000000000004a/_indices/93a455f5-0479-4009-baca-7445f27c22af/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000008-000000000000004a/_indices/b8ed3d9c-a9d6-4d89-b1dd-ad9664646cde/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000008-000000000000004a/_indices/b8ed3d9c-a9d6-4d89-b1dd-ad9664646cde/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_transactions/0-7d459a2f-e3a4-4c8f-9511-64875275e9d9.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_transactions/1-4ab9e7f2-7685-41b0-9bcc-99ceade308f0.txn   |  Bin 0 -> 33114 bytes
 .../nodes/0000000000000008-000000000000004a/_transactions/12023749703452972081-0bc2ea47-783d-49ef-abdf-b0a8e919ab4d.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_versions/d12023749703452972081.manifest         |  Bin 0 -> 33881 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_versions/d12693207923042981168.manifest         |  Bin 0 -> 2158 bytes
 .../85pct_dxy_gu/omnigraph/graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_versions/latest_version_hint.json  |    1 +
 .../graph.omni/nodes/0000000000000008-000000000000004a/data/1100111001110001000001103c0c9242a0a4b0eb905b72c0cc.lance          |  Bin 0 -> 35433 bytes
 .../graph.omni/nodes/0000000000000009-000000000000004b/_indices/8066314c-9791-4d70-8c20-89ab9a60c56f/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000009-000000000000004b/_indices/8066314c-9791-4d70-8c20-89ab9a60c56f/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000009-000000000000004b/_indices/84680681-854e-486c-b24b-48c6b476a44e/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000009-000000000000004b/_indices/84680681-854e-486c-b24b-48c6b476a44e/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000009-000000000000004b/_indices/e687230f-6b07-46be-b761-edc1dc4031a9/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000009-000000000000004b/_indices/e687230f-6b07-46be-b761-edc1dc4031a9/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_transactions/0-046e0f9d-a6d7-4dbb-9d9a-4d6743452fa3.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_transactions/1-00c53b81-5725-4d8e-8e45-5d87dcf03d14.txn   |  Bin 0 -> 33114 bytes
 .../nodes/0000000000000009-000000000000004b/_transactions/14199068376039637143-4987baa3-bff3-43f2-8f86-591df68ffc52.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_versions/d11753372911981248793.manifest         |  Bin 0 -> 2158 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_versions/d14199068376039637143.manifest         |  Bin 0 -> 33881 bytes
 .../85pct_dxy_gu/omnigraph/graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_versions/latest_version_hint.json  |    1 +
 .../graph.omni/nodes/0000000000000009-000000000000004b/data/01111000001100001010110119b5a54508ac739ce46db95e33.lance          |  Bin 0 -> 23499 bytes
 handover/85pct_dxy_gu/omnigraph/graph_store/last_sync.jsonl                                                                   | 4207 +++++++++++++++++++++++++++++++++++++++++++++++++++++++
 handover/85pct_dxy_gu/omnigraph/graph_store/state.json                                                                        |   44 +
 handover/85pct_dxy_gu/omnigraph/mem_ls.txt                                                                                    | 1580 +++++++++++++++++++++
 handover/85pct_dxy_gu/omnigraph/mem_status.txt                                                                                |   27 +
 handover/85pct_dxy_gu/omnigraph/rebuild_warnings.txt                                                                          |   22 +
 memory/04_OPERATOR_RULINGS_LIVE.md                                                                                            |    1 +
 memory/12_OPERATOR_VERBATIM.md                                                                                                |    3 +
 tools/checkpoint                                                                                                              |   16 +
 154 files changed, 15144 insertions(+)
---

## 262fadd  (2026-11-27T18:27:59+00:00)

full id: 262fadd00b5c7e4745adf4712dea3a1b0d7d1946

```
D-141 Thursday fix: dormant alternative-chain orders are contingencies (report only until activated); the Law-27 short at the reverse whiplash's TP exists from that whiplash's start; rockets the move already passed are not new orders - DXY Thursday = the ladder short only, GBPUSD Thursday = the short at Wednesday's TP

M-61: 'the long on Wednesday that hit take profit, that should literally be the entry of the short at that exact point where the E2 shape chain even predicts a peak'.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/e3_trades.py        | 13 +++++++++++--
 e1_tool/plutus.py           | 19 +++++++++++++++++--
 memory/03_DECISION_CHAIN.md |  1 +
 3 files changed, 29 insertions(+), 4 deletions(-)
---

## 65ae7fc  (2026-11-27T18:31:25+00:00)

full id: 65ae7fc204d1a7cf89f8f0cbb4d1fda68f5659cd

```
V2 frames + ledger 114 (Thursday fix on the golden week, all three pairs)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/__pycache__/e3_trades.cpython-313.pyc | Bin 107440 -> 107878 bytes
 e1_tool/__pycache__/plutus.cpython-313.pyc    | Bin 77754 -> 79267 bytes
 e1_tool/out/E1_DXY_2026-07-06.pine            |  60 +++++++++++++-----------------------------------------------
 e1_tool/out/E1_EURUSD_2026-07-06.pine         | 106 +++++++++++++++++++++++++++++++---------------------------------------------------------------------------
 e1_tool/out/E1_GBPUSD_2026-07-06.pine         | 103 +++++++++++++++++++++----------------------------------------------------------------------------------
 evidence/v2/DXY_2026-07-06_fullweek.png       | Bin 0 -> 117235 bytes
 evidence/v2/EURUSD_2026-07-06_fullweek.png    | Bin 0 -> 114640 bytes
 evidence/v2/GBPUSD_2026-07-06_fullweek.png    | Bin 0 -> 107566 bytes
 memory/05_JOURNAL.md                          |   1 +
 memory/07_EVIDENCE_LEDGER.md                  |   1 +
 10 files changed, 67 insertions(+), 204 deletions(-)
---

## 6e4f3f7  (2026-11-27T18:31:27+00:00)

full id: 6e4f3f70daa2cbaecd9817bf93d8005d88a57d3e

```
CHECKPOINT '85% functional - DXY + GU' V2 (Thursday E3 fix, D-141): code 262fadd + context + OmniGraph rebuilt from memory (store + full export) + manifest

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 handover/85pct_dxy_gu_v2/CHECKPOINT.md                                                                                        |   10 +
 handover/85pct_dxy_gu_v2/MANIFEST.sha256                                                                                      | 5063 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 handover/85pct_dxy_gu_v2/omnigraph/export_stderr.txt                                                                          |    1 +
 handover/85pct_dxy_gu_v2/omnigraph/graph_export.jsonl                                                                         | 4223 ++++++++++++++++++++++++++++++++++++++++++++++++++++++
 .../graph_store/graph.omni/__history/schemas/911dd40ed55479426cd00a5d98aa66c97d5fd19d6d629a75e9aa8ff4449968da.schema          |  Bin 0 -> 52231 bytes
 handover/85pct_dxy_gu_v2/omnigraph/graph_store/graph.omni/__manifest/_transactions/0-b1951476-496b-4f43-a68a-b96a8240832d.txn |  Bin 0 -> 1274 bytes
 handover/85pct_dxy_gu_v2/omnigraph/graph_store/graph.omni/__manifest/_transactions/1-c3fe7c31-822f-4608-9dfe-b6fae554ff05.txn |  Bin 0 -> 1276 bytes
 handover/85pct_dxy_gu_v2/omnigraph/graph_store/graph.omni/__manifest/_transactions/2-5fe8bd1f-653a-41db-8879-deb97df93863.txn |  Bin 0 -> 1276 bytes
 handover/85pct_dxy_gu_v2/omnigraph/graph_store/graph.omni/__manifest/_versions/18446744073709551612.manifest                  |  Bin 0 -> 2711 bytes
 handover/85pct_dxy_gu_v2/omnigraph/graph_store/graph.omni/__manifest/_versions/18446744073709551613.manifest                  |  Bin 0 -> 2711 bytes
 handover/85pct_dxy_gu_v2/omnigraph/graph_store/graph.omni/__manifest/_versions/18446744073709551614.manifest                  |  Bin 0 -> 2705 bytes
 handover/85pct_dxy_gu_v2/omnigraph/graph_store/graph.omni/__manifest/_versions/latest_version_hint.json                       |    1 +
 .../85pct_dxy_gu_v2/omnigraph/graph_store/graph.omni/__manifest/data/00100100011001101111101060a5a34630bccd598677485e2e.lance |  Bin 0 -> 62323 bytes
 .../85pct_dxy_gu_v2/omnigraph/graph_store/graph.omni/__manifest/data/00100110001101000011101165ef44402099e0d3bb2e697c7e.lance |  Bin 0 -> 66547 bytes
 .../85pct_dxy_gu_v2/omnigraph/graph_store/graph.omni/__manifest/data/10001011010001011011000029a18b4be39a2c877d20f0185f.lance |  Bin 0 -> 67763 bytes
 .../graph_store/graph.omni/edges/000000000000000a-000000000000004c/_transactions/0-4725bc9a-47f6-4422-8c42-50b169c0484f.txn   |    2 +
 .../graph_store/graph.omni/edges/000000000000000a-000000000000004c/_transactions/1-34f45515-be1b-4098-a5e1-a40cff69d097.txn   |  Bin 0 -> 33135 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000a-000000000000004c/_versions/18446744073709551614.manifest          |  Bin 0 -> 443 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000a-000000000000004c/_versions/d16146545080639110991.manifest         |  Bin 0 -> 33529 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000a-000000000000004c/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/edges/000000000000000a-000000000000004c/data/0011011011011101110011105353f34fc3b78ef98024fbc8e5.lance          |  Bin 0 -> 35314 bytes
 .../graph_store/graph.omni/edges/000000000000000b-000000000000004d/_transactions/0-af203a5b-68c8-4aca-9535-7f43d93d2f6d.txn   |    2 +
 .../omnigraph/graph_store/graph.omni/edges/000000000000000b-000000000000004d/_versions/18446744073709551614.manifest          |  Bin 0 -> 443 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000b-000000000000004d/_versions/latest_version_hint.json               |    1 +
 .../graph_store/graph.omni/edges/000000000000000c-000000000000004e/_transactions/0-c45d44fb-7a76-494c-a8bd-ff8ccffc12c4.txn   |    2 +
 .../omnigraph/graph_store/graph.omni/edges/000000000000000c-000000000000004e/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000c-000000000000004e/_versions/latest_version_hint.json               |    1 +
 .../graph_store/graph.omni/edges/000000000000000d-000000000000004f/_transactions/0-c0c2e155-d6bc-4526-ad14-97fb2637736d.txn   |    2 +
 .../omnigraph/graph_store/graph.omni/edges/000000000000000d-000000000000004f/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000d-000000000000004f/_versions/latest_version_hint.json               |    1 +
 .../graph_store/graph.omni/edges/000000000000000e-0000000000000050/_transactions/0-33b47680-da3e-4290-a509-267203652120.txn   |    2 +
 .../graph_store/graph.omni/edges/000000000000000e-0000000000000050/_transactions/1-4e00cfd3-3d53-4da5-89a7-e628ec90a66e.txn   |  Bin 0 -> 33133 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000e-0000000000000050/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000e-0000000000000050/_versions/d14391387807825160863.manifest         |  Bin 0 -> 33521 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000e-0000000000000050/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/edges/000000000000000e-0000000000000050/data/001001110011000000011110fbc18f453d95f0c3e66f064ebd.lance          |  Bin 0 -> 733 bytes
 .../graph.omni/nodes/0000000000000002-0000000000000044/_indices/590c6018-3a67-4a2c-b948-c865394e593c/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000002-0000000000000044/_indices/590c6018-3a67-4a2c-b948-c865394e593c/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000002-0000000000000044/_indices/a66e7b83-dd86-4a61-8db4-06b0b317a9f4/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000002-0000000000000044/_indices/a66e7b83-dd86-4a61-8db4-06b0b317a9f4/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000002-0000000000000044/_indices/ae3f9a4a-8239-409e-b5e9-9933315c752a/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000002-0000000000000044/_indices/ae3f9a4a-8239-409e-b5e9-9933315c752a/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_transactions/0-9a0cfce4-e142-4a5f-a4db-c9acf23eaa83.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_transactions/1-c8745d37-7b9b-49bf-ba0a-2dbe3153302d.txn   |  Bin 0 -> 33114 bytes
 .../nodes/0000000000000002-0000000000000044/_transactions/11268717874214913808-4c75a018-7eb2-46ca-ba85-8517512b2ecd.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_versions/18446744073709551614.manifest          |  Bin 0 -> 1185 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_versions/d11268717874214913808.manifest         |  Bin 0 -> 33882 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_versions/d15314988189024088655.manifest         |  Bin 0 -> 2159 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/nodes/0000000000000002-0000000000000044/data/011000000010110000101001e9b9824584b3f8ff44bef90af4.lance          |  Bin 0 -> 31497 bytes
 .../graph.omni/nodes/0000000000000003-0000000000000045/_indices/45cd48f4-8724-4532-a528-cbacd2f32d31/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000003-0000000000000045/_indices/45cd48f4-8724-4532-a528-cbacd2f32d31/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000003-0000000000000045/_indices/fd39ef7a-6a17-42d6-aa29-33f19002b992/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000003-0000000000000045/_indices/fd39ef7a-6a17-42d6-aa29-33f19002b992/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000003-0000000000000045/_indices/fd3db78e-1572-4654-b9c5-505755c7cbcc/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000003-0000000000000045/_indices/fd3db78e-1572-4654-b9c5-505755c7cbcc/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_transactions/0-ab6e1640-d6fa-4873-9336-108f301e3c89.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_transactions/1-89b12b53-9b6a-40ec-bcab-ff46b0179ba0.txn   |  Bin 0 -> 33115 bytes
 .../nodes/0000000000000003-0000000000000045/_transactions/12679274927298930743-85e961f4-b2e3-4d1a-b912-c80fc3db44bb.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_versions/18446744073709551614.manifest          |  Bin 0 -> 1185 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_versions/d12679274927298930743.manifest         |  Bin 0 -> 33888 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_versions/d14960092118297997525.manifest         |  Bin 0 -> 2164 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/nodes/0000000000000003-0000000000000045/data/100110011001000101110110cf664745efb366cba30f0f8f95.lance          |  Bin 0 -> 96043 bytes
 .../graph.omni/nodes/0000000000000004-0000000000000046/_indices/7c86dd04-81f7-40ff-9f9e-6773afa16608/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000004-0000000000000046/_indices/7c86dd04-81f7-40ff-9f9e-6773afa16608/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000004-0000000000000046/_indices/dceabc7a-fcbc-4d94-9fff-b310a90ee7ff/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000004-0000000000000046/_indices/dceabc7a-fcbc-4d94-9fff-b310a90ee7ff/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_transactions/0-18a97aa4-60f5-48cb-8608-ed4fb9e12006.txn   |    7 +
 .../graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_transactions/1-665aeb31-ea34-42fe-8aee-696fd15f53a0.txn   |  Bin 0 -> 33111 bytes
 .../nodes/0000000000000004-0000000000000046/_transactions/15801292564633755588-f780206f-5ff2-4d74-ae29-1fca7b0ec0b5.txn       |  Bin 0 -> 581 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_versions/18446744073709551614.manifest          |  Bin 0 -> 989 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_versions/d15419394861983354417.manifest         |  Bin 0 -> 1670 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_versions/d15801292564633755588.manifest         |  Bin 0 -> 33784 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/nodes/0000000000000004-0000000000000046/data/0100000111100000100111105fd53540c0a693813621282bb6.lance          |  Bin 0 -> 1197421 bytes
 .../graph.omni/nodes/0000000000000005-0000000000000047/_indices/23c37890-059b-49ad-8927-557a88999729/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000005-0000000000000047/_indices/23c37890-059b-49ad-8927-557a88999729/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000005-0000000000000047/_indices/2805ee3b-8abf-4e47-8d5f-aed41b6fe44c/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000005-0000000000000047/_indices/2805ee3b-8abf-4e47-8d5f-aed41b6fe44c/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000005-0000000000000047/_indices/a4ebe722-b970-4662-b804-190ade951274/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000005-0000000000000047/_indices/a4ebe722-b970-4662-b804-190ade951274/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_transactions/0-3a3ebfd6-e59d-46b1-97f9-60765485c161.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_transactions/1-ff2195a8-b747-46c5-8dca-e7ca2ab83718.txn   |  Bin 0 -> 33115 bytes
 .../nodes/0000000000000005-0000000000000047/_transactions/10574394973740978765-f2b8e28c-fb83-44ea-bc0c-b67684a3d577.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_versions/18446744073709551614.manifest          |  Bin 0 -> 1185 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_versions/d10574394973740978765.manifest         |  Bin 0 -> 33888 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_versions/d16586430247640449372.manifest         |  Bin 0 -> 2164 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/nodes/0000000000000005-0000000000000047/data/110110111010000001001011d6d571470aaed75a78a5a5c35c.lance          |  Bin 0 -> 107897 bytes
 .../graph.omni/nodes/0000000000000006-0000000000000048/_indices/0fa357cf-c908-4ade-9c25-b948b7406242/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000006-0000000000000048/_indices/0fa357cf-c908-4ade-9c25-b948b7406242/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000006-0000000000000048/_indices/37e23a0c-2180-4e00-b6b9-6dca7a69bc18/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000006-0000000000000048/_indices/37e23a0c-2180-4e00-b6b9-6dca7a69bc18/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000006-0000000000000048/_indices/f3c548b2-e346-4264-9759-f0c1dc25ab4f/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000006-0000000000000048/_indices/f3c548b2-e346-4264-9759-f0c1dc25ab4f/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_transactions/0-2988e8a0-2b0a-41a6-917f-5f3b951ac631.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_transactions/1-7ca20285-8c3a-498b-a10d-cbe469f4731b.txn   |  Bin 0 -> 33115 bytes
 .../nodes/0000000000000006-0000000000000048/_transactions/16324817002917150012-bdff6173-6c8b-4147-963a-834a5b5fd4e9.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_versions/18446744073709551614.manifest          |  Bin 0 -> 1185 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_versions/d16324817002917150012.manifest         |  Bin 0 -> 33888 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_versions/d17038450808733311738.manifest         |  Bin 0 -> 2164 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/nodes/0000000000000006-0000000000000048/data/100001101010000111100101eb6bab45e0a6d218a4b663586d.lance          |  Bin 0 -> 454414 bytes
 .../graph.omni/nodes/0000000000000007-0000000000000049/_indices/3eaa5213-1341-436a-a3d7-7fc2852cc169/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000007-0000000000000049/_indices/3eaa5213-1341-436a-a3d7-7fc2852cc169/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000007-0000000000000049/_indices/4f27788d-de4e-4193-9471-af26215209ea/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000007-0000000000000049/_indices/4f27788d-de4e-4193-9471-af26215209ea/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000007-0000000000000049/_indices/d5abd494-b3ba-4117-b371-e6703e1f4963/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000007-0000000000000049/_indices/d5abd494-b3ba-4117-b371-e6703e1f4963/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_transactions/0-1c2334ea-4a0a-4fea-a44e-a0f13e743161.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_transactions/1-95e04003-69a5-4ddc-9ec6-66a22b3127e5.txn   |  Bin 0 -> 33114 bytes
 .../nodes/0000000000000007-0000000000000049/_transactions/18424878531885136839-7fe491c8-e2ec-4c94-9d96-3c1f49e5e183.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_versions/18446744073709551614.manifest          |  Bin 0 -> 1185 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_versions/d14682315712959184381.manifest         |  Bin 0 -> 2159 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_versions/d18424878531885136839.manifest         |  Bin 0 -> 33882 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/nodes/0000000000000007-0000000000000049/data/1101101011101111001001001373264aaaa6c77a3bcce92a1c.lance          |  Bin 0 -> 20121 bytes
 .../graph.omni/nodes/0000000000000008-000000000000004a/_indices/7b75f658-e716-4720-8de6-22bef32dbe73/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000008-000000000000004a/_indices/7b75f658-e716-4720-8de6-22bef32dbe73/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000008-000000000000004a/_indices/93d0c47e-97b7-4f08-8044-0b4bda723e93/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000008-000000000000004a/_indices/93d0c47e-97b7-4f08-8044-0b4bda723e93/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000008-000000000000004a/_indices/fdd3c124-0199-4f1c-a331-6d62c7d81429/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000008-000000000000004a/_indices/fdd3c124-0199-4f1c-a331-6d62c7d81429/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_transactions/0-d5e6fbc6-69a8-4d2d-8934-04f83af7d469.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_transactions/1-76ba86e4-994e-49c5-8df2-b74aecf96d8e.txn   |  Bin 0 -> 33114 bytes
 .../nodes/0000000000000008-000000000000004a/_transactions/12330066112501531466-f2d453e9-7752-4566-9e52-7782567db2f8.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_versions/18446744073709551614.manifest          |  Bin 0 -> 1185 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_versions/d11442982091769418494.manifest         |  Bin 0 -> 2159 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_versions/d12330066112501531466.manifest         |  Bin 0 -> 33882 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/nodes/0000000000000008-000000000000004a/data/101001100001001110001001c62bf145aeb8ed1bcce8f58f01.lance          |  Bin 0 -> 35433 bytes
 .../graph.omni/nodes/0000000000000009-000000000000004b/_indices/4c227ab4-349c-42e1-96e7-b2147482f1bd/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000009-000000000000004b/_indices/4c227ab4-349c-42e1-96e7-b2147482f1bd/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000009-000000000000004b/_indices/7dcb1f40-70bb-4edf-a4ae-0183f0fda96e/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000009-000000000000004b/_indices/7dcb1f40-70bb-4edf-a4ae-0183f0fda96e/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000009-000000000000004b/_indices/7f630d74-46b8-43ae-bbd6-2815bdd61cc5/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000009-000000000000004b/_indices/7f630d74-46b8-43ae-bbd6-2815bdd61cc5/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_transactions/0-77a873be-9480-4bae-9c03-b84a98df1f34.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_transactions/1-ad7b8bb8-0d6d-4398-aff8-29154d514a99.txn   |  Bin 0 -> 33114 bytes
 .../nodes/0000000000000009-000000000000004b/_transactions/13661552086213812051-639ae85b-ed69-46b3-b678-93db77eed0ca.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_versions/18446744073709551614.manifest          |  Bin 0 -> 1185 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_versions/d13661552086213812051.manifest         |  Bin 0 -> 33882 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_versions/d16933954821765374660.manifest         |  Bin 0 -> 2159 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/nodes/0000000000000009-000000000000004b/data/11110110100010101000001139161a4604ac2f8ae06c679c18.lance          |  Bin 0 -> 23499 bytes
 handover/85pct_dxy_gu_v2/omnigraph/graph_store/last_sync.jsonl                                                                | 4223 ++++++++++++++++++++++++++++++++++++++++++++++++++++++
 handover/85pct_dxy_gu_v2/omnigraph/graph_store/state.json                                                                     |   44 +
 handover/85pct_dxy_gu_v2/omnigraph/mem_ls.txt                                                                                 | 1583 +++++++++++++++++++++
 handover/85pct_dxy_gu_v2/omnigraph/mem_status.txt                                                                             |   27 +
 handover/85pct_dxy_gu_v2/omnigraph/rebuild_warnings.txt                                                                       |   22 +
 151 files changed, 15313 insertions(+)
---

## 0bb5182  (2026-11-27T18:59:38+00:00)

full id: 0bb5182bd3e691f096ba38df712fce2aad82c347

```
M-61 V3 context: EURUSD diagnosis (why a C), D-142 / D-143 (rejected) / D-144 decisions, ledger 115 expectation, facts, lessons, coverage; evidence/answers_m61/EURUSD_why_C.md

Code for D-142 / D-144 follows in the next commit once the leak check passes.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 evidence/answers_m61/EURUSD_why_C.md | 46 ++++++++++++++++++++++++++++++++++++++++++++++
 memory/01_CURRENT_STATE.md           |  7 +++++++
 memory/03_DECISION_CHAIN.md          |  3 +++
 memory/05_JOURNAL.md                 |  5 +++++
 memory/06_LESSONS.md                 |  2 ++
 memory/07_EVIDENCE_LEDGER.md         |  1 +
 memory/08_FACTS.md                   |  4 ++++
 memory/15_CANON_COVERAGE.md          |  4 ++++
 8 files changed, 72 insertions(+)
---

## ff6be1e  (2026-11-27T19:02:41+00:00)

full id: ff6be1ec4d36917ce7ef111606326f9b149dcac1

```
D-142 + D-144 EURUSD fix (M-61 V3): Phase 10 re-entry check on the source pair's same-day record; Law 27 trade flow on the day's line

E3C:723-770 'For each DXY source setup, generate the corresponding EU mirror setup (inverse direction). For each EU mirror setup, generate the corresponding GU mirror setup (kept direction)':
under daily anchoring a daily re-entry on EURUSD / GBPUSD needs the source pair's matching order CONFIRMED AT THE SAME DAY'S ANCHOR (per-day record parts[i]['keys']);
the week-anchor build mirrors the source's week-anchor setups as before (a first version that mirrored the source's whole-week daily result leaked later days into GBPUSD
Monday - caught by tools/leak_check.py, D-142b)
(golden EURUSD Tue re-entry long 1.14095 - stopped by Wednesday's RWL retest - and GBPUSD Tue 1.33333 duplicate gone; DXY had dropped its own copy as still open).

E3C 6.2 / 8.21 'TP of trade N = entry of trade N+1' (3-pip tolerance); M-61 'The long on Wednesday that hit take profit, that should literally be the entry of the short at that exact point':
an order the day's Engine 2 line (built at the trading-day open) reaches while an opposite order runs to its TP, inside that move by more than 3 pips, is not placed
(golden EURUSD Mon short 1.14385 - 4.4 pips before the Monday long's TP 1.14429, stopped by 0.3 pips at the spike that filled his #3 1.14442 - gone).

D-143 (Trading Laws 'stop inside a liquidity zone -> 2 pips outside its back edge') tried and switched off: his golden stops sit inside those V1 rungs; it lost his EURUSD #6 #7 #8.
Golden: DXY unchanged; EURUSD = his #2 #3 #4 #5 #6 #7 #8 + one long that never fills, no stop-outs; GBPUSD unchanged but the unfilled Tuesday duplicate.
Memory: 01, 03 (D-142b), 05, 06 (context commit 0bb5182 carries the rest).

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/e3_trades.py        | 27 +++++++++++++++++++++++++++
 e1_tool/plutus.py           | 80 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++---
 memory/01_CURRENT_STATE.md  |  2 +-
 memory/03_DECISION_CHAIN.md |  1 +
 memory/05_JOURNAL.md        |  1 +
 memory/06_LESSONS.md        |  1 +
 6 files changed, 108 insertions(+), 4 deletions(-)
---

## a8bfce4  (2026-11-27T19:07:14+00:00)

full id: a8bfce4bd3d0380515194326fd281a29a2088d3d

```
V3 frames + ledger 115b (EURUSD fix on the golden week, all three pairs, whole week each)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 evidence/v3/DXY_2026-07-06_fullweek.png    | Bin 0 -> 117287 bytes
 evidence/v3/EURUSD_2026-07-06_fullweek.png | Bin 0 -> 111965 bytes
 evidence/v3/GBPUSD_2026-07-06_fullweek.png | Bin 0 -> 106296 bytes
 memory/07_EVIDENCE_LEDGER.md               |   1 +
 4 files changed, 1 insertion(+)
---

## 8f834f4  (2026-11-27T19:07:33+00:00)

full id: 8f834f48880cb3ad67d5ae1d62092087b92d9ae0

```
CHECKPOINT '85% functional - DXY + GU' V3 (EURUSD fix, D-142b + D-144): code ff6be1e + frames a8bfce4 + context + OmniGraph rebuilt from memory (1606 nodes / 1102 edges, store + full export) + manifest

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 handover/85pct_dxy_gu_v3/CHECKPOINT.md                                                                                        |   10 +
 handover/85pct_dxy_gu_v3/MANIFEST.sha256                                                                                      | 5218 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 handover/85pct_dxy_gu_v3/omnigraph/export_stderr.txt                                                                          |    1 +
 handover/85pct_dxy_gu_v3/omnigraph/graph_export.jsonl                                                                         | 4314 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 .../graph_store/graph.omni/__history/schemas/f04ab77016cd5aa81db07d13c3e263d536fcc9ebb4182a73160487d2a0b8a14f.schema          |  Bin 0 -> 52231 bytes
 handover/85pct_dxy_gu_v3/omnigraph/graph_store/graph.omni/__manifest/_transactions/0-5748efcd-f819-4d06-94d7-ce0307633417.txn |  Bin 0 -> 1274 bytes
 handover/85pct_dxy_gu_v3/omnigraph/graph_store/graph.omni/__manifest/_transactions/1-6e2bebbd-7b11-4f0c-bb30-84d539d17337.txn |  Bin 0 -> 1276 bytes
 handover/85pct_dxy_gu_v3/omnigraph/graph_store/graph.omni/__manifest/_transactions/2-34dc050a-51b0-4691-823d-78292212263f.txn |  Bin 0 -> 1276 bytes
 handover/85pct_dxy_gu_v3/omnigraph/graph_store/graph.omni/__manifest/_versions/18446744073709551612.manifest                  |  Bin 0 -> 2710 bytes
 handover/85pct_dxy_gu_v3/omnigraph/graph_store/graph.omni/__manifest/_versions/18446744073709551613.manifest                  |  Bin 0 -> 2710 bytes
 handover/85pct_dxy_gu_v3/omnigraph/graph_store/graph.omni/__manifest/_versions/18446744073709551614.manifest                  |  Bin 0 -> 2705 bytes
 handover/85pct_dxy_gu_v3/omnigraph/graph_store/graph.omni/__manifest/_versions/latest_version_hint.json                       |    1 +
 .../85pct_dxy_gu_v3/omnigraph/graph_store/graph.omni/__manifest/data/01101100010100011101111077c4e24c818d5f4f5c98a136bd.lance |  Bin 0 -> 62323 bytes
 .../85pct_dxy_gu_v3/omnigraph/graph_store/graph.omni/__manifest/data/0110111101001010110111119eeaa04971bca02075223a0a84.lance |  Bin 0 -> 67763 bytes
 .../85pct_dxy_gu_v3/omnigraph/graph_store/graph.omni/__manifest/data/110111001010111101000100d3ee844882a7bbbddff154829e.lance |  Bin 0 -> 66547 bytes
 .../graph_store/graph.omni/edges/000000000000000a-000000000000004c/_transactions/0-fdceb9fb-446c-45fa-ad0b-82eedaa0c3f5.txn   |    2 +
 .../graph_store/graph.omni/edges/000000000000000a-000000000000004c/_transactions/1-dcf59bbb-2e58-455b-b1e4-2c495f9eb425.txn   |  Bin 0 -> 33135 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000a-000000000000004c/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000a-000000000000004c/_versions/d18340618489600979524.manifest         |  Bin 0 -> 33528 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000a-000000000000004c/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/edges/000000000000000a-000000000000004c/data/110101101010011111011100ccba4149ffb67d0c96f479f5ee.lance          |  Bin 0 -> 36146 bytes
 .../graph_store/graph.omni/edges/000000000000000b-000000000000004d/_transactions/0-23152b5c-adbb-427d-8849-864604454ba8.txn   |    2 +
 .../omnigraph/graph_store/graph.omni/edges/000000000000000b-000000000000004d/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000b-000000000000004d/_versions/latest_version_hint.json               |    1 +
 .../graph_store/graph.omni/edges/000000000000000c-000000000000004e/_transactions/0-9f2270a2-15ff-44db-a306-09ca83e76c07.txn   |    2 +
 .../omnigraph/graph_store/graph.omni/edges/000000000000000c-000000000000004e/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000c-000000000000004e/_versions/latest_version_hint.json               |    1 +
 .../graph_store/graph.omni/edges/000000000000000d-000000000000004f/_transactions/0-bdbd520a-7726-4b00-b793-7d391b13f6eb.txn   |    2 +
 .../omnigraph/graph_store/graph.omni/edges/000000000000000d-000000000000004f/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000d-000000000000004f/_versions/latest_version_hint.json               |    1 +
 .../graph_store/graph.omni/edges/000000000000000e-0000000000000050/_transactions/0-67e4fa03-761c-4353-9cbc-9d6287743105.txn   |    2 +
 .../graph_store/graph.omni/edges/000000000000000e-0000000000000050/_transactions/1-d4f5ec26-69da-43e5-a512-13bea491ecbf.txn   |  Bin 0 -> 33133 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000e-0000000000000050/_versions/18446744073709551614.manifest          |  Bin 0 -> 444 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000e-0000000000000050/_versions/d14479710918488621507.manifest         |  Bin 0 -> 33520 bytes
 .../omnigraph/graph_store/graph.omni/edges/000000000000000e-0000000000000050/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/edges/000000000000000e-0000000000000050/data/010010010101110001111111c88bd14a619fcc6c2c987d60cc.lance          |  Bin 0 -> 733 bytes
 .../graph.omni/nodes/0000000000000002-0000000000000044/_indices/8d8af540-1f3e-44f7-b737-a598dcae41fb/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000002-0000000000000044/_indices/8d8af540-1f3e-44f7-b737-a598dcae41fb/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000002-0000000000000044/_indices/9b02eaa3-a12f-44c6-b01c-628d78b85880/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000002-0000000000000044/_indices/9b02eaa3-a12f-44c6-b01c-628d78b85880/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000002-0000000000000044/_indices/c9874ca1-268e-441a-b216-38c656a57267/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000002-0000000000000044/_indices/c9874ca1-268e-441a-b216-38c656a57267/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_transactions/0-3b791154-c43f-4aca-b111-42e09008a539.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_transactions/1-5791e3be-fb9b-44c6-8d2a-f4662ae02eca.txn   |  Bin 0 -> 33114 bytes
 .../nodes/0000000000000002-0000000000000044/_transactions/12263436478691768349-0e3dd326-7bcd-45f5-9824-00907f397d56.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_versions/d12263436478691768349.manifest         |  Bin 0 -> 33881 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_versions/d15713717341941311305.manifest         |  Bin 0 -> 2158 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000002-0000000000000044/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/nodes/0000000000000002-0000000000000044/data/10000101000111011100100187f9d8434f8e3364848d9f6c4a.lance          |  Bin 0 -> 32649 bytes
 .../graph.omni/nodes/0000000000000003-0000000000000045/_indices/17844674-349f-4443-92d7-687f3e846455/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000003-0000000000000045/_indices/17844674-349f-4443-92d7-687f3e846455/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000003-0000000000000045/_indices/5e012715-394c-4058-9315-9a2191c80d5d/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000003-0000000000000045/_indices/5e012715-394c-4058-9315-9a2191c80d5d/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000003-0000000000000045/_indices/aa45ac47-a406-43a3-bb76-2a18a1282619/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000003-0000000000000045/_indices/aa45ac47-a406-43a3-bb76-2a18a1282619/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_transactions/0-b9dacc76-a5e4-42ea-823e-7adf1dbf54b9.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_transactions/1-dd85981c-3f8d-47c4-b39e-f669a6bb7a51.txn   |  Bin 0 -> 33115 bytes
 .../nodes/0000000000000003-0000000000000045/_transactions/9741618732374660285-dd6ab4e8-6eb3-4410-b4d9-c7ddab2dcb03.txn        |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_versions/d10848084665587210978.manifest         |  Bin 0 -> 2162 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_versions/d9741618732374660285.manifest          |  Bin 0 -> 33887 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000003-0000000000000045/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/nodes/0000000000000003-0000000000000045/data/110110111101110111111110ff1cfc4c12b810ac31f54d8d76.lance          |  Bin 0 -> 99563 bytes
 .../graph.omni/nodes/0000000000000004-0000000000000046/_indices/17361376-2473-417e-8868-fc390d63316e/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000004-0000000000000046/_indices/17361376-2473-417e-8868-fc390d63316e/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000004-0000000000000046/_indices/dc87446a-965b-460d-b4de-c6c3f2a09e68/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000004-0000000000000046/_indices/dc87446a-965b-460d-b4de-c6c3f2a09e68/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_transactions/0-2372b2dd-2395-4d0b-a064-ec8d8e04100d.txn   |    7 +
 .../graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_transactions/1-77cb99fd-f903-4fab-9bd9-b6c074380bf8.txn   |  Bin 0 -> 33111 bytes
 .../nodes/0000000000000004-0000000000000046/_transactions/14860529860126842475-f334c91b-90f6-4a5a-ad42-8c1613f2aac3.txn       |  Bin 0 -> 581 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_versions/18446744073709551614.manifest          |  Bin 0 -> 990 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_versions/d13562612939295221313.manifest         |  Bin 0 -> 1669 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_versions/d14860529860126842475.manifest         |  Bin 0 -> 33783 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000004-0000000000000046/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/nodes/0000000000000004-0000000000000046/data/0011100001010100001001000468824b26ae77de3f4e6517d6.lance          |  Bin 0 -> 1270445 bytes
 .../graph.omni/nodes/0000000000000005-0000000000000047/_indices/20d73533-5d81-46d6-88ac-0d4bda91a509/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000005-0000000000000047/_indices/20d73533-5d81-46d6-88ac-0d4bda91a509/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000005-0000000000000047/_indices/8ed17b08-6efa-4123-8758-52915ad4ae7b/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000005-0000000000000047/_indices/8ed17b08-6efa-4123-8758-52915ad4ae7b/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000005-0000000000000047/_indices/c8ce11fb-730a-453b-9148-73ea74c47937/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000005-0000000000000047/_indices/c8ce11fb-730a-453b-9148-73ea74c47937/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_transactions/0-5e108fcf-b98f-4f3c-804d-dab23a574990.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_transactions/1-612731ae-23a1-4849-b25b-70113e7d8518.txn   |  Bin 0 -> 33115 bytes
 .../nodes/0000000000000005-0000000000000047/_transactions/10086078339351776837-5d4174b4-0b8d-4ec3-9bab-79cf9fffe1c4.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_versions/d10086078339351776837.manifest         |  Bin 0 -> 33887 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_versions/d14094289893915618989.manifest         |  Bin 0 -> 2163 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000005-0000000000000047/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/nodes/0000000000000005-0000000000000047/data/001011001110010010110111cfc254420686fc086771a68c05.lance          |  Bin 0 -> 107513 bytes
 .../graph.omni/nodes/0000000000000006-0000000000000048/_indices/1c267f7a-7125-4ef3-a0ad-e7ae27719d60/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000006-0000000000000048/_indices/1c267f7a-7125-4ef3-a0ad-e7ae27719d60/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000006-0000000000000048/_indices/3f74db09-a6cd-402e-9f54-e199ee079f0c/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000006-0000000000000048/_indices/3f74db09-a6cd-402e-9f54-e199ee079f0c/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000006-0000000000000048/_indices/d5002d9c-5868-4e8f-889f-5b83d9a53336/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000006-0000000000000048/_indices/d5002d9c-5868-4e8f-889f-5b83d9a53336/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_transactions/0-5a729bf7-024a-4a23-a208-30c40420405c.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_transactions/1-75a1c197-1089-4afd-b80a-0c37e029c917.txn   |  Bin 0 -> 33115 bytes
 .../nodes/0000000000000006-0000000000000048/_transactions/14375396498668837426-27c550d8-45e0-45e8-9040-2110076f102d.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_versions/d14375396498668837426.manifest         |  Bin 0 -> 33887 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_versions/d16500732698818267175.manifest         |  Bin 0 -> 2163 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000006-0000000000000048/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/nodes/0000000000000006-0000000000000048/data/011010011011010010011101b1a91e443d89a53164f391580e.lance          |  Bin 0 -> 462478 bytes
 .../graph.omni/nodes/0000000000000007-0000000000000049/_indices/3c562b8d-2bd9-41a1-9c1e-530112691426/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000007-0000000000000049/_indices/3c562b8d-2bd9-41a1-9c1e-530112691426/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000007-0000000000000049/_indices/933ebd28-c957-4f52-8cb9-3f4587b95e2a/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000007-0000000000000049/_indices/933ebd28-c957-4f52-8cb9-3f4587b95e2a/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000007-0000000000000049/_indices/d8b6fb7d-1411-4115-908b-be20218af30c/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000007-0000000000000049/_indices/d8b6fb7d-1411-4115-908b-be20218af30c/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_transactions/0-58a9b895-6f86-41ca-9cb1-e713ebb7ffba.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_transactions/1-fd3e936c-cd53-4730-8132-667ceaa2e07a.txn   |  Bin 0 -> 33114 bytes
 .../nodes/0000000000000007-0000000000000049/_transactions/10635234497209268680-2f500072-1eb8-4ca5-acf0-7f2399e99961.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_versions/d10635234497209268680.manifest         |  Bin 0 -> 33881 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_versions/d15218106299002976841.manifest         |  Bin 0 -> 2158 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000007-0000000000000049/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/nodes/0000000000000007-0000000000000049/data/010101100000110011111110252bbe4f0481c2875d5ab4482a.lance          |  Bin 0 -> 21529 bytes
 .../graph.omni/nodes/0000000000000008-000000000000004a/_indices/3e2fd56d-a0b9-41e5-9705-21fe695740bd/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000008-000000000000004a/_indices/3e2fd56d-a0b9-41e5-9705-21fe695740bd/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000008-000000000000004a/_indices/b23b7168-0753-46d0-a15e-df5f93dab7c6/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000008-000000000000004a/_indices/b23b7168-0753-46d0-a15e-df5f93dab7c6/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000008-000000000000004a/_indices/c4ee4a58-7245-43e4-9a54-7cefdf92939f/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000008-000000000000004a/_indices/c4ee4a58-7245-43e4-9a54-7cefdf92939f/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_transactions/0-bf092d7b-d752-4461-a9aa-91fad1278651.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_transactions/1-904cdd71-25a4-4b78-949f-68366fabaad7.txn   |  Bin 0 -> 33114 bytes
 .../nodes/0000000000000008-000000000000004a/_transactions/12008759230070430954-7c54afcf-c4a6-416e-9d9c-50a4c33d1bd3.txn       |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_versions/d12008759230070430954.manifest         |  Bin 0 -> 33881 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_versions/d9322698638218850229.manifest          |  Bin 0 -> 2158 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000008-000000000000004a/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/nodes/0000000000000008-000000000000004a/data/010010001001101011011110ff3090425ca066794c0f5b097f.lance          |  Bin 0 -> 35433 bytes
 .../graph.omni/nodes/0000000000000009-000000000000004b/_indices/4b2cead9-1745-4b47-bfbd-6477eb7096cb/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000009-000000000000004b/_indices/4b2cead9-1745-4b47-bfbd-6477eb7096cb/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000009-000000000000004b/_indices/788b6b79-05e2-4994-bb42-04ebd33a94e6/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000009-000000000000004b/_indices/788b6b79-05e2-4994-bb42-04ebd33a94e6/omnigraph_fts_compat.json           |    1 +
 .../graph.omni/nodes/0000000000000009-000000000000004b/_indices/e5088926-5824-4efa-b87a-f59606951736/metadata.lance           |  Bin 0 -> 823 bytes
 .../nodes/0000000000000009-000000000000004b/_indices/e5088926-5824-4efa-b87a-f59606951736/omnigraph_fts_compat.json           |    1 +
 .../graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_transactions/0-1580adc3-8fe8-4f28-8463-905dc54e8234.txn   |    9 +
 .../graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_transactions/1-5eb8980c-412b-4031-8205-069b41c84233.txn   |  Bin 0 -> 33114 bytes
 .../nodes/0000000000000009-000000000000004b/_transactions/9404314059148670498-517291b5-e9fb-439d-ad14-35bde9f0c82c.txn        |  Bin 0 -> 778 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_versions/18446744073709551614.manifest          |  Bin 0 -> 1186 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_versions/d17217138584729883479.manifest         |  Bin 0 -> 2157 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_versions/d9404314059148670498.manifest          |  Bin 0 -> 33881 bytes
 .../omnigraph/graph_store/graph.omni/nodes/0000000000000009-000000000000004b/_versions/latest_version_hint.json               |    1 +
 .../graph.omni/nodes/0000000000000009-000000000000004b/data/111011110111010010111110dbf2ba41c69dd69e5d16ef3571.lance          |  Bin 0 -> 23499 bytes
 handover/85pct_dxy_gu_v3/omnigraph/graph_store/last_sync.jsonl                                                                | 4314 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 handover/85pct_dxy_gu_v3/omnigraph/graph_store/state.json                                                                     |   48 +
 handover/85pct_dxy_gu_v3/omnigraph/mem_ls.txt                                                                                 | 1607 ++++++++++++++++++++
 handover/85pct_dxy_gu_v3/omnigraph/mem_status.txt                                                                             |   31 +
 handover/85pct_dxy_gu_v3/omnigraph/rebuild_warnings.txt                                                                       |   26 +
 memory/01_CURRENT_STATE.md                                                                                                    |    4 +-
 152 files changed, 15688 insertions(+), 2 deletions(-)
---

## 63d10dc  (2026-11-27T19:07:43+00:00)

full id: 63d10dc06d388645fe05d0421ca4e2025c89a1a8

```
V3 generated Pine for the golden EURUSD / GBPUSD frames (DXY unchanged)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Eis2qBbofvMAifYJzweUMT
```

files:

 e1_tool/out/E1_EURUSD_2026-07-06.pine | 95 ++++++++++++++++++++++++++++++++++++-----------------------------------------------------------
 e1_tool/out/E1_GBPUSD_2026-07-06.pine | 37 +++++++++++++------------------------
 2 files changed, 49 insertions(+), 83 deletions(-)
