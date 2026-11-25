# REPORT ORACLES - weekly-report ground truth for Engine 1 / Engine 2 / Engine 3

Extracted first-hand on 2026-11-25. Machine-readable twin: `context_management/oracle/report_oracles.json` (same content plus options tables, LSZ, 4H zones, pivots, MAs, every caveat with citations).

**Citation form** `KEY:line`. PDF line numbers are lines of `pdftotext -layout <pdf>`; page images were rendered and read for W22 (p.3, 5, 6) and Apr27 (p.5, 6) to confirm the text layer is faithful.

| key | file |
|---|---|
| W14 | `/home/user/handover-branch/Original_Canon_Data/Validated Trade Reports/Trident_Report_2026W14_Mar30-Apr3.md (line numbers = file lines)` |
| A20 | `/home/user/handover-branch/Original_Canon_Data/IP Heatmap Reports/Leviathan_DXY_IL_Report_Apr20-24_2026.pdf (line numbers = `pdftotext -layout` output lines)` |
| PM20 | `/home/user/handover-branch/Original_Canon_Data/Failure Logs + Changelog Requests/Leviathan_PostMortem_Apr20-24_2026.pdf (pdftotext -layout lines) -- NOT in the task's source list; read because it grades the Apr20-24 report` |
| A27 | `/home/user/handover-branch/Original_Canon_Data/IP Heatmap Reports/Leviathan_DXY_IL_Report_Apr27-May1_2026.pdf (pdftotext -layout lines)` |
| M04 | `/home/user/handover-branch/Original_Canon_Data/IP Heatmap Reports/Leviathan_DXY_IL_Report_May05-04_2026.pdf (pdftotext -layout lines)` |
| M25 | `/home/user/handover-branch/Original_Canon_Data/IP Heatmap Reports/Leviathan_DXY_IP_Report_May25-29_2026.pdf (pdftotext -layout lines)` |
| W22 | `/home/user/handover-branch/Original_Canon_Data/IP Heatmap Reports/Trident_Report_2026W22_May25-29_v5.pdf (pdftotext -layout lines)` |
| V7 | `/home/user/handover-branch/Original_Canon_Data/Pine Scripts/trident_v7 (2).pine (file lines)` |
| V8 | `/home/user/handover-branch/Original_Canon_Data/Pine Scripts/trident_v8.pine (file lines)` |
| APPR | `/home/user/inputs/handover/PLUTUS_VISION_CONTEXT_HANDOVER/00_HANDOVER/approved-2026-11-09-DXY.json (file lines)` |
| HO | `/home/user/inputs/handover/PLUTUS_VISION_CONTEXT_HANDOVER/00_HANDOVER/PLUTUS_VISION_CONTEXT_HANDOVER.md (file lines)` |
| CHK | `/home/user/inputs/handover/PLUTUS_VISION_CONTEXT_HANDOVER/00_HANDOVER/checks.md (file lines)` |
| VAL | `/home/user/handover-branch/Original_Canon_Data/trident_e3_validator_FINAL.py (file lines)` |
| E3C | `/home/user/handover-branch/Original_Canon_Data/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md (file lines; byte-identical copy in Toolset/)` |
| HARV | `/home/user/handover-branch/fixtures/bars/2026-07-06.validated-harvest.json (JSON keys)` |
| E1J | `/home/user/handover-branch/data/e1/DXY-2026-07-06.json, data/e1/EURUSD-2026-07-06.json (JSON keys)` |
| E2J | `/home/user/handover-branch/data/e2/DXY-2026-07-06-e2.json, data/e2/EURUSD-2026-07-06-e2.json (JSON keys)` |
| V6V | `/home/user/handover-branch/Original_Canon_Data/Build Data/Trident_Engine3_v6_Verification_May18-22.md (file lines) -- NOT in source list; used only to cross-check the prior-week DXY OHLC of the two May25-29 reports` |

## 1. What is actually usable as an oracle (ranked)

- 1. 2026-11-09 DXY - operator-approved E1 zones (3 CORRECT, 3 REFINE). E1 only.
- 2. 2026-07-06 DXY - operator's golden trades (6 priced E3 setups + LQZ/BoM/MoM levels); R-15 'golden week'. E3 only; no report-derived E1/E2 for this week exists on disk.
- 3. 2026-04-20 DXY (v4.5.2) - the only LLM report with a written grade: zones A/A+, LSZ A+/A, trades D, direction F; post-mortem supplies 3 corrected trades.
- 4. 2026-05-25 DXY Leviathan (v4.5.2, E3 disabled) - E1+E2 with arithmetically sound pivots/K factor and a full MA grid (minor oddities listed in its caveats); ungraded; generated after Monday's close.
- 5. 2026-04-27 (Quant Analytics v2) and 2026-05-04 (v4.4) DXY - ungraded; Apr27 breaches its own temporal boundary on options; May04 scores do not sum.
- 6. 2026-03-30 W14 (v5.2.2) - 4 pairs, full E1/E2/E3, but hindsight-contaminated (prints and quotes the target week's own OHLC).
- 7. 2026-05-25 W22 (v5.3.3) - the ONLY v5.3.3 report, but mid-week, with a corrupt K factor/DXY equivalents, templated scores and conflicting inputs versus the Leviathan report of the same week.
- 8. trident_v7/v8.pine - re-encodings of #3 for DXY; v8's EU/GU/AU blocks are unverified/likely synthetic.
- 9. handover-branch/data/e1|e2 2026-07-06 - previous agent's tool output; NOT an oracle.

## 2. Cross-report CONFLICT / UNKNOWN register

- CONFLICT: no two reports use the same zone template - v5.2.2 W14: 4 zones/pair (R1,R2,D1,D2; Supply/Demand + BoM/MoM); v4.5.2 Apr20: 5 zones (>= MODERATE only); 'Quant Analytics v2' Apr27: 12 zones incl. LIGHT/MINIMAL; v4.4 May04: 6 zones incl. LIGHT; v4.5.2 May25 and v5.3.3 W22: 6 zones (#1 Ceiling .. #6 Deep Support); operator Nov09: exactly 6.
- CONFLICT: zone widths - Apr20 0.07-0.34; Apr27 0.10-0.15; May04 0.20-0.36; May25 0.07-0.20; W22 DXY 0.05-0.36; operator-approved Nov09 0.098-0.149 with three of those 'too wide'. Post-mortem asks for a 0.10 clustering threshold instead of 0.15 (PM20:85-86).
- CONFLICT: the two reports for week 2026-05-25 disagree on the prior-week OHLC, MAs, option strikes, PCE day and 5 of 6 DXY zones (see W22 cross_report_conflicts).
- CONFLICT: supply-side LSZ convention [high, high+0.05] (Apr20) vs [high-0.05, high] (May25).
- CONFLICT: ZFP - reports print a strength-based ZFP per zone; trident_v7/v8.pine compute a WIDTH-based ZFP (width / 1.60) that contradicts the report values (e.g. Key Support 12% in the report vs 21% in pine).
- UNKNOWN: operator grades for every report except Apr20-24; actual outcomes for Apr27, May04, May25 weeks (not in the listed sources).
- UNKNOWN: E1 zones and E2 chain for the golden week 2026-07-06 from any validated report; EU/GU golden trades with SL/TP; 'PLUTUS_GOLDEN_CASCADE_23.md' and 'Golden_Operator_Trade_Feedback_EU_GU.md' are referenced but absent.
- UNKNOWN: zone names and ZFP for the six operator-approved 2026-11-09 zones (the approved render carried only the degree).
- UNKNOWN: provenance of trident_v8.pine EUR/USD, GBP/USD, AUD/USD levels and of the 'Wed > Thu-Fri' / 'Thu > Fri' trade-day labels in v7/v8.

## 3. Index

| # | week (Mon) | source | prompt version | pairs | E1 zones | E2 chain | E3 setups | grade on disk |
|---|---|---|---|---|---|---|---|---|
| 1 | 2026-03-30 | `Trident_Report_2026W14_Mar30-Apr3.md` | Trident Trading Engine v5.2.2 (W14:1) | DXY, EURUSD, GBPUSD, AUDUSD | 4/4/4/4 | 5/5/5/5 | 4/15/8/6 | E1 zones / E2 chain / E3 setups all present for 4 pairs, but HINDSIGHT-CONTAMINATED (see caveats). No operator grade found in the file. |
| 2 | 2026-04-20 | `Leviathan_DXY_IL_Report_Apr20-24_2026.pdf` | Trident Trading Engine v4.5.2 (A20:3) | DXY | 5 | 5 | 7 | ONLY report with an explicit grade on disk: post-mortem 'IP ZONES A/A+ (4 of 5 zones precise, 1 too wide)', 'LSZ MAPPING A+/A', 'TRADE SETUPS D (1 set... |
| 3 | 2026-04-20 | `trident_v7 (2).pine` | hardcoded Pine render of the v4.5.2 Apr20-24 report (indicator title ' | DXY | 5 | 5 | 2 | Derivative of the Apr20-24 report (same grades apply). Adds nothing new for DXY except renamed zones and day labels of unknown provenance. |
| 4 | 2026-04-20 | `trident_v8.pine` | hardcoded Pine render (indicator title 'TRIDENT v8 - 4-Pair Master') | DXY, EURUSD, GBPUSD, AUDUSD | 5/5/5/5 | 5/5/5/5 | 2/2/2/2 | DXY block = v7 = the Apr20-24 report. EUR/USD, GBP/USD, AUD/USD blocks have NO source report on disk (the Apr20-24 report is DXY-only) and fail cross-... |
| 5 | 2026-04-27 | `Leviathan_DXY_IL_Report_Apr27-May1_2026.pdf` | UNKNOWN prompt version; cover prints 'Engine: Leviathan Quant Analytic | DXY | 12 | 5 | 4 | No operator grade found. E3 is a 3-row 'Trade Flow Map' that self-reports 'Minimum RRR Threshold Check FAIL for primary (4.0x < 5.0x)' (A27:607). |
| 6 | 2026-05-04 | `Leviathan_DXY_IL_Report_May05-04_2026.pdf` | Leviathan v4.4 (Dual-Engine: 9-Pillar 6D Hybrid + Macro Shape Chain Ma | DXY, EURUSD, GBPUSD, AUDUSD | 6/0/0/0 | 5/5/1/1 | 3/0/0/0 | No operator grade found. Dual-engine version: NO Engine 3 section; trade setups appear only inside the Monday day-map and the weekly visualization. |
| 7 | 2026-05-25 | `Leviathan_DXY_IP_Report_May25-29_2026.pdf` | Leviathan Ultra-Quant v4.5.2 \| Engine 3 DISABLED (M25:3) | DXY | 6 | 5 | 0 | No operator grade found on disk. E1 + E2 only (Engine 3 disabled). Monday's shape is post-hoc (generated after Monday's close); Tue-Fri are genuine fo... |
| 8 | 2026-05-25 | `Trident_Report_2026W22_May25-29_v5.pdf` | Trident Trading Engine v5.3.3 \| Full-Spectrum Architecture (W22:4). F | DXY, EURUSD, GBPUSD, AUDUSD | 6/6/6/6 | 5/5/5/5 | 0/5/6/6 | No operator grade found on disk. Mid-week report: Mon/Tue shapes and the Mon/Tue calendar setups are RETROSPECTIVE (built from the realised Mon/Tue ra... |
| 9 | 2026-07-06 | `trident_e3_validator_FINAL.py (GOLDEN_DXY_TRADES etc.) + TRIDENT_v5.3.` | operator's own manual trades ('The 8 golden DXY trades (operator's Jul | DXY, EURUSD, GBPUSD | 0/0/0 | 0/0/0 | 8/2/0 | OPERATOR GROUND TRUTH for E3 (entries/SL/TP) on the 'golden week' used by ruling R-15. NO weekly LLM report for this week exists in /home/user/handove... |
| 10 | 2026-07-06 | `handover-branch/data/e1/DXY-2026-07-06.json, data/e1/EURUSD-2026-07-06` | NOT A REPORT - output of the previous agent's mechanical E1/E2 Python  | DXY, EURUSD | 5/6 | 5/5 | 0/0 | NOT AN ORACLE. Included only because the task asked for every zone data set found for this week. Not report-derived, not operator-approved; web harves... |
| 11 | 2026-11-09 | `approved-2026-11-09-DXY.json (+ PLUTUS_VISION_CONTEXT_HANDOVER.md sect` | v5.3.3 E1 ('5.3.3. NOTHING ELSE' - the only authority is the 5.3.3 pro | DXY | 6 | 0 | 0 | OPERATOR-APPROVED E1 TARGET (the strongest E1 oracle on disk): 'DO NOT ADD ANY MORE FUCKING ZONES THESE 6 ARE CORRECT ... ZONES 3 4 AND 5 NEED REFINEM... |

Counts are per pair in the order listed. `rrr_computed` / `rrr_arith_ok` in the JSON are computed here, not in the sources.

## 4. Per-week detail

### 4.1  Week of 2026-03-30 - `Trident_Report_2026W14_Mar30-Apr3.md`

- **Prompt version:** Trident Trading Engine v5.2.2 (W14:1)
- **Data as-of:** Friday, March 27, 2026 17:00 ET (W14:7)
- **Generated:** UNKNOWN in the .md; the sibling PDF's metadata CreationDate is 'Tue May 26 21:40:53 2026 UTC' (pdfinfo) i.e. ~8 weeks AFTER the target week
- **Oracle grade:** E1 zones / E2 chain / E3 setups all present for 4 pairs, but HINDSIGHT-CONTAMINATED (see caveats). No operator grade found in the file.

**Data the report used (pillars with real data).** Options: investingLive 10am NY cut Mon-Thu, qualitative notionals only (W14:13-42). OHLC: myfxbook (FX), DealPlexus/WSJ/Yahoo (DXY) (W14:77). Calendar: ForexFactory/TradingCharts/LiteFinance (W14:93). Analyst levels EU: RoboForex/FOREX.com 'MODERATE' confidence (W14:388). 52wk high: CNBC (W14:385). Pillars 1/2/3/6/7/8 (pivots, MAs, component conversion, fib grid, derivatives, K-factor) show NO printed data in this report.

#### DXY - spot at analysis: 100.15

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| R1 | 100.50 | 100.65 | 0.15 | RES | EXTREME | 9 | 10 | Supply / BoM / Reactions 0 / Confl 9/14 / Key Level '52-week high 100.64' / 'HARD WALL - EXTREME pressure, ZFP<15%. Counter-trend check triggers.' (W14:134). Degree taken from that status text; the table has... |
| R2 | 100.00 | 100.25 | 0.25 | RES | - | 6 | 25 | Supply / MoM / Reactions 2 / Confl 6/14 / 'Psychological 100.00' / 'TP-TARGET for DXY LONGS after break' (W14:135) |
| D1 | 99.30 | 99.60 | 0.30 | SUP | - | 6 | 30 | Demand / MoM / Reactions 1 / Confl 6/14 / 'Prior week mid-range' / 'TP-TARGET for DXY SHORTS' (W14:136) |
| D2 | 98.80 | 99.10 | 0.30 | SUP | - | 7 | 20 | Demand / BoM / Reactions 0-1 / Confl 7/14 / 'Prior week BoM origin' / 'ENTRY-PRIMARY (DXY LONG = pair SHORT)' (W14:137) |

Key levels: 52-week high (W14:134) 100.64; Psychological (W14:135) 100.00

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | BS | UP | - | - | W14:169 'All 3 pairs follow the INVERSE of DXY. DXY: BS up Mon -> WL down Tue -> BS down Wed -> WL up Thu -> SS Fri. Pairs: BS down Mon -> WL up Tue -> BS up Wed -> WL down Thu -> SS Fri.' |
| Tue | WL | DOWN | - | - | DXY hits 52wk high 100.64 -> reverses (W14:148) |
| Wed | BS | DOWN | - | - | W14:169 |
| Thu | WL | UP | - | - | W14:169 |
| Fri | SS | RANGE | - | - | W14:169; Good Friday thin liquidity (W14:151) |

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | type |
|---|---|---|---|---|---|---|---|
| Tue | S | 100.52 | 100.75 | 99.60 / 99.10 | 4 | 4 | HTF Swing #1 (WL down Tue) at R1 BoM Supply |
| Thu | L | 99.45 | 99.15 | 100.25 / 100.55 | 2.7 | 2.67 | HTF Swing #2 (BS up Thu) at D1 MoM Demand - CONDITIONAL |
| - | S | 100.05 | 100.25 | 99.10 | 2.3 | 4.75 **MISMATCH** | Reinforcement R1 for #1 - Liquidity Ladder |
| - | S | 99.65 | 99.85 | 99.10 | 2.2 | 2.75 **MISMATCH** | Reinforcement R2 for #1 - Fib Rocket FLR |

#### EURUSD - spot at analysis: 1.15123

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| R2 | 1.1600 | 1.1640 | 0.0040 | RES | - | 9 | 15 | Supply / BoM / Reactions 1 / Confl 9/14 / Option '1.1600 Apr 1 SIG MAG' / ENTRY-PRIMARY (SHORT) (W14:101) |
| R1 | 1.1545 | 1.1575 | 0.0030 | RES | - | 7 | 30 | Supply / MoM / Reactions 1-2 / Confl 7/14 / Option '1.1550 Mar 30 SIG MAG' / ENTRY-CONDITIONAL (SHORT) 3/4 exceptions (W14:102) |
| D1 | 1.1495 | 1.1515 | 0.0020 | SUP | - | 8 | 35 | Demand / MoM / Reactions 1-2 / Confl 8/14 / Option '1.1500 Mar 31 CRIT WALL + Apr 2 SIG MAG' / TP-TARGET for SHORTS, NOT entry (2/4 = REJECT) (W14:103) |
| D2 | 1.1430 | 1.1460 | 0.0030 | SUP | - | 8 | 20 | Demand / BoM / Reactions 0-1 / Confl 8/14 / 'Prior weekly support' / ENTRY-PRIMARY (LONG) - 'BoM 100% guaranteed reaction' (W14:104) |

Key levels: Option Mon SIG MAG 1.1550; Option Tue CRIT WALL / Thu SIG MAG 1.1500; Option Wed SIG MAG 1.1600; Nearest LSZ below (W14:191) 1.1410; Fri consolidation range low (W14:201) 1.1510; Fri consolidation range high (W14:201) 1.15491

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | BS | DOWN | zone 1.1545-1.1575 | zone 1.1430-1.1460 | Conf 85%. 'D2 BoM Demand 1.1430-60 target. R1 MoM Supply 1.1545-75 ceiling.' (W14:147) |
| Tue | WL | UP | zone 1.1430-1.1460 | zone 1.1545-1.1575 | Conf 80%. 'D2 BoM Demand HOLDS at 1.14431/1.14475. TP at R1 1.1545-75.' (W14:148) [in-week actual lows quoted] |
| Wed | BS | UP | zone 1.1545-1.1575 | zone 1.1600-1.1640 | Conf 70%. 'R1 MoM Supply 1.1545-75 PIERCES. Target R2 BoM Supply 1.1600-40.' (W14:149) |
| Thu | WL | DOWN | zone 1.1600-1.1640 | zone 1.1495-1.1515 | Conf 80%. 'R2 BoM Supply 1.1600-40 REJECTS at 1.16272. Target D1 MoM Demand 1.1495-15.' (W14:150) [in-week actual high quoted] |
| Fri | SS | RANGE | 1.1500 | 1.1550 | Conf 65%. 'Range: 1.1500-1.1550. D1/D2 demand floor, R1 supply ceiling.' (W14:151) |

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | type |
|---|---|---|---|---|---|---|---|
| Tue | L | 1.1450 | 1.1425 | 1.1550 / 1.1600 / 1.1630 | 4 | 4 | HTF Swing #1 (WL up Tue) at D2 BoM Demand - BoM PRIMARY |
| Thu | S | 1.1610 | 1.1650 | 1.1500 / 1.1450 | 2.75 | 2.75 | HTF Swing #2 (WL down Thu) at R2 BoM Supply - BoM PRIMARY |
| Mon | S | 1.1535 | 1.1580 | 1.1450 | 1.9 | 1.89 | HTF Swing #3 (BS down Mon) at R1 MoM Supply - MoM CONDITIONAL(3/4) |
| Fri | L | 1.1515 | 1.1495 | 1.1540 | 4.2 | 1.25 **MISMATCH** | Swing Scalp S1 (15m BoM demand at range floor) London+NY |
| Fri | S | 1.1540 | 1.1555 | 1.1515 | 3.7 | 1.67 **MISMATCH** | Swing Scalp S2 (15m MoM supply at range ceiling) London+NY |
| Fri | L | 1.1505 | 1.1490 | 1.1545 | 2.9 | 2.67 | Swing Scalp S3 (15m MoM demand at D1 zone) NY only, NFP deferral until 09:00 ET |
| Mon/Tue | S | 1.1505 | 1.1530 | 1.1450 | 4 | 2.2 **MISMATCH** | Double Whiplash Inverse Leg 1 (R1 MoM rejection) |
| Tue | L | 1.1450 | 1.1425 | 1.1550 | 4 | 4 | Double Whiplash Inverse Leg 2 (D2 BoM reaction) |
| - | L | 1.1500 | 1.1475 | 1.1600 | 2.5 | 4 **MISMATCH** | Reinforcement R1 for #1 - Liquidity Ladder |
| - | L | 1.1555 | 1.1530 | 1.1600 | 2.8 | 1.8 **MISMATCH** | Reinforcement R2 for #1 - Fib Rocket FLR (1.382 ext from 1.14431 = 1.1556) |
| - | L | 1.1580 | 1.1555 | 1.1630 | 2.5 | 2 **MISMATCH** | Reinforcement R3 for #1 - Fib Rocket LR (1.618 ext = 1.1581) |
| - | S | 1.1550 | 1.1575 | 1.1450 | 2 | 4 **MISMATCH** | Reinforcement R4 for #2 - Liquidity Ladder |
| - | S | 1.1500 | 1.1525 | 1.1450 | 2 | 2 | Reinforcement R5 for #2 - Fib Rocket FLR (Fib 1.382 from 1.16272 = 1.1500) |
| Fri | S | 1.1490 | 1.1530 | 1.1400 | 3.3 | 2.25 **MISMATCH** | Transition T1 SS->BS: trigger 'Break below 1.1490 (15m)' |
| Thu/Fri | L | 1.1560 | 1.1520 | 1.1630 | 3.7 | 1.75 **MISMATCH** | Transition T2 Post-WL Reverse: trigger 'Break above 1.1560 (15m)' |

#### GBPUSD - spot at analysis: 1.32691

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| R2 | 1.3400 | 1.3480 | 0.0080 | RES | - | 8 | 12 | Supply / BoM / Reactions 1 / Confl 8/14 / no option confluence / ENTRY-PRIMARY (SHORT) (W14:112) |
| R1 | 1.3300 | 1.3350 | 0.0050 | RES | - | 6 | 28 | Supply / MoM / Reactions 1-2 / Confl 6/14 / ENTRY-CONDITIONAL (SHORT) 3/4 (W14:113) |
| D2 | 1.3250 | 1.3280 | 0.0030 | SUP | - | 5 | 32 | Demand / MoM / Reactions 2 / Confl 5/14 / 'TP-TARGET for SHORTS. MoM demand with 2 reactions = approaching depletion' (W14:115) |
| D1 | 1.3150 | 1.3200 | 0.0050 | SUP | - | 7 | 22 | Demand / BoM / Reactions 0-1 / Confl 7/14 / 'ENTRY-PRIMARY (LONG) - BoM zone, fresh' (W14:114) |

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | BS | DOWN | - | - | W14:169 'All 3 pairs follow the INVERSE of DXY. DXY: BS up Mon -> WL down Tue -> BS down Wed -> WL up Thu -> SS Fri. Pairs: BS down Mon -> WL up Tue -> BS up Wed -> WL down Thu -> SS Fri.' |
| Tue | WL | UP | - | - | W14:169 |
| Wed | BS | UP | - | - | W14:169 |
| Thu | WL | DOWN | - | - | W14:169 |
| Fri | SS | RANGE | - | - | W14:169; 'GU amplifies moves (3-4x more London ops)' |

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | type |
|---|---|---|---|---|---|---|---|
| Tue | L | 1.3165 | 1.3135 | 1.3260 / 1.3320 | 3.3 | 3.17 | HTF Swing #1 (WL up Tue) at D1 BoM Demand |
| Thu | S | 1.3325 | 1.3360 | 1.3200 / 1.3160 | 3.6 | 3.57 | HTF Swing #2 (WL down Thu) at R1 MoM Supply - CONDITIONAL(3/4) |
| Thu | S | 1.3410 | 1.3455 | 1.3260 / 1.3160 | 3.3 | 3.33 | HTF Swing #3 (WL down Thu) at R2 BoM Supply |
| - | L | 1.3210 | 1.3180 | 1.3320 | 2.7 | 3.67 **MISMATCH** | Reinforcement R1 for #1 - Liquidity Ladder |
| - | L | 1.3270 | 1.3240 | 1.3320 | 2.3 | 1.67 **MISMATCH** | Reinforcement R2 for #1 - Fib Rocket (1.382 from 1.31595 low) |
| - | S | 1.3260 | 1.3290 | 1.3160 | 2 | 3.33 **MISMATCH** | Reinforcement R3 for #2 - Liquidity Ladder |
| Fri | L | 1.3190 | 1.3170 | 1.3230 | 4 | 2 **MISMATCH** | Swing Scalp S1 (15m BoM demand 1.3180-200 range floor) London PRIMARY |
| Fri | S | 1.3230 | 1.3250 | 1.3190 | 4 | 2 **MISMATCH** | Swing Scalp S2 (15m supply 1.3220-40 range ceiling) London PRIMARY |

#### AUDUSD - spot at analysis: 0.6878

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| R2 | 0.6990 | 0.7060 | 0.0070 | RES | - | 7 | 18 | Supply / BoM / Reactions 1 / Confl 7/14 / ENTRY-PRIMARY (SHORT) (W14:123) |
| R1 | 0.6930 | 0.6970 | 0.0040 | RES | - | 5 | 30 | Supply / MoM / Reactions 1-2 / Confl 5/14 / TP-TARGET for LONGS (W14:124) |
| D2 | 0.6870 | 0.6910 | 0.0040 | SUP | - | 5 | 35 | Demand / MoM / Reactions 2 / Confl 5/14 / TP-TARGET for SHORTS (W14:126) |
| D1 | 0.6830 | 0.6865 | 0.0035 | SUP | - | 7 | 25 | Demand / BoM / Reactions 0-1 / Confl 7/14 / Option '0.6825 Mar 31 SIG MAG' / ENTRY-PRIMARY (LONG) (W14:125) |

Key levels: Option Tue SIG MAG 0.6825; 100-DMA (W14:32) 0.6818

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | BS | DOWN | - | - | W14:169 'All 3 pairs follow the INVERSE of DXY. DXY: BS up Mon -> WL down Tue -> BS down Wed -> WL up Thu -> SS Fri. Pairs: BS down Mon -> WL up Tue -> BS up Wed -> WL down Thu -> SS Fri.' |
| Tue | WL | UP | - | - | W14:169 |
| Wed | BS | UP | - | - | W14:169 |
| Thu | WL | DOWN | - | - | W14:169 |
| Fri | SS | RANGE | - | - | W14:169; 'AU tracks EU with commodity overlay' |

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | type |
|---|---|---|---|---|---|---|---|
| Tue | L | 0.6845 | 0.6820 | 0.6900 / 0.6940 | 3.6 | 2.2 **MISMATCH** | HTF Swing #1 (WL up Tue) at D1 BoM Demand + 0.6825 option |
| Thu | S | 0.6935 | 0.6970 | 0.6860 / 0.6835 | 2.1 | 2.14 | HTF Swing #2 (WL down Thu) at R1 MoM Supply - CONDITIONAL |
| - | L | 0.6885 | 0.6860 | 0.6940 | 2.2 | 2.2 | Reinforcement R1 for #1 - Liquidity Ladder |
| - | L | 0.6910 | 0.6885 | 0.6940 | 2.1 | 1.2 **MISMATCH** | Reinforcement R2 for #1 - Fib Rocket (1.382 from 0.68330 low) |
| Fri | L | 0.6885 | 0.6870 | 0.6910 | 3.7 | 1.67 **MISMATCH** | Swing Scalp S1 (15m demand at range floor 0.6875-90) NY |
| Fri | S | 0.6910 | 0.6925 | 0.6885 | 3.7 | 1.67 **MISMATCH** | Swing Scalp S2 (15m supply at range ceiling 0.6910-25) London+NY |

**Caveats / CONFLICT / UNKNOWN:**

- HINDSIGHT: the report prints the TARGET WEEK's own OHLC (W14:65-73) and its E2 rationale quotes in-week actual prints: 'D2 BoM Demand HOLDS at 1.14431/1.14475' (W14:148; these are the actual Mon/Tue lows of W14:69-70), 'R2 BoM Supply 1.1600-40 REJECTS at 1.16272' (W14:150; actual Wed high W14:71), 'NFP ... MASSIVE surprise +178K vs +53K consensus' (W14:50). The compliance sweep nevertheless claims 'Temporal Boundary PASS - All data pre-March 30 market open. In-week OHLC used for validation only, not as forward-looking data' (W14:408). CONFLICT.
- Option notionals are qualitative only ('Modest', 'LARGE', 'Notable') - no numbers (W14:19,31-38).
- No pivots, MAs, K-factor or per-dimension scores are printed; zones are Supply/Demand + BoM/MoM + Reactions + ZFP% + Confl. x/14 only (W14:99-137).
- Zone numbering is not monotonic: DXY R1 (100.50-100.65) is ABOVE R2 (100.00-100.25) (W14:134-135); GBP/USD D2 (1.3250-1.3280) is ABOVE D1 (1.3150-1.3200) (W14:114-115); AUD/USD D2 (0.6870-0.6910) is ABOVE D1 (0.6830-0.6865) (W14:125-126).
- Several stated RRRs do not equal |TP-entry|/|entry-SL| (see rrr_arith_ok=false rows), e.g. EU scalp S1 LONG 1.1515/1.1495/1.1540 stated 4.2x (W14:205), arithmetic 1.25.
- EU HTF #3 CONFLICT: table gives TP2 '-' and RRR '1.9x/4.7x' (W14:181) while its audit text says 'TP2 at 1.1400 = 5.3x' (W14:181) and the cross-pair matrix lists TP(best) 1.1400, 5.3x (W14:336).
- Setup count CONFLICT: '18 total tradeable setups' (W14:173) vs '15 setups above threshold' + '8 reinforcement entries (R1-R8)' + '23 tradeable positions' (W14:346); the tables list 12 reinforcements (EU R1-R5, GU R1-R3, AU R1-R2, DXY R1-R2).

### 4.2  Week of 2026-04-20 - `Leviathan_DXY_IL_Report_Apr20-24_2026.pdf`

- **Prompt version:** Trident Trading Engine v4.5.2 (A20:3)
- **Data as-of:** April 17, 2026 17:00 ET (A20:7); option boundary = Apr 20 morning (A20:32)
- **Generated:** 2026-05-25 19:32 UTC (A20:11) - a retro-run ~5 weeks after the target week, with a declared temporal boundary
- **Oracle grade:** ONLY report with an explicit grade on disk: post-mortem 'IP ZONES A/A+ (4 of 5 zones precise, 1 too wide)', 'LSZ MAPPING A+/A', 'TRADE SETUPS D (1 setup, wrong direction, missed 3 valid trades)', 'DIRECTION CALL F (SHORT consensus vs. actual BUY trend week)' (PM20:18-24). => E1 zones are a usable oracle; E2 direction and E3 setups of this report are NOT ground truth; the post-mortem's 3 'actual trades' are.

**Data the report used (pillars with real data).** REAL: Pillar 1 pivots (weekly Classic+Fibonacci from H=99.18 L=97.63 C=98.10, daily pivots cited) (A20:99-107); Pillar 3/8 K-factor 108.0806 from USDJPY/GBPUSD/USDCAD/USDSEK/USDCHF and EUR/USD strike->DXY (A20:94-96); Pillar 5 D1 swing highs/lows, repeated-high magnets, LSZ (A20:187-206); Pillar 6 fib 38.2% + round numbers (A20:119-133); 4H BoM/MoM overlay with origin candles (A20:236-263); Protocol A options Mon+Tue from investinglive (A20:30-88); Protocol E ON RRP (A20:351); Protocol F calendar (A20:358-380). APPROXIMATED: Pillar 2 MAs ('calculated MA approximations', A20:424-426) and no MA appears among zone key drivers. ABSENT/NO DATA: Pillar 4 analyst commentary (no section printed - UNKNOWN whether harvested), Pillar 7 (ICE/CME), Protocols C1-C3, D, G; Wed-Fri options.

#### DXY - spot at analysis: 98.10

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| RESISTANCE CEILING | 99.16 | 99.23 | 0.07 | RES | HEAVY | 10 | 15 | POI Tier 2: IP-Only. Drivers: P1-Weekly R1, P5-SH 99.18 (Repeated High 2x), P6-Round 99.00 area (A20:119-121). 4H overlay: none; BoM fresh: No; Ladder step: No (A20:142-149) |
| UPPER RESISTANCE | 98.77 | 98.99 | 0.22 | RES | MODERATE-HEAVY | 8 | 25 | POI Tier 1: Confluent. Drivers: P1-Daily Classic R1 (Apr 13), P5-4H BoM Supply, P6-Fib 38.2% (A20:123-125). 4H overlay: BoM 1X mitigated (1S); Ladder step: Yes (sell trend MoM ladder) (A20:151-158) |
| EQUILIBRIUM ZONE | 98.29 | 98.41 | 0.12 | EQ | MODERATE-HEAVY | 9 | 20 | POI Tier 2: IP-Only. Drivers: P5-Repeated High Magnet 98.29 (3x dates), P1-Daily pivots cluster, P5-Prior daily closes (A20:127-129). 4H overlay: MoM 1X mitigated (1S) Supply at 98.34-98.42; LSZ 98.29-98.34;... |
| MID-RANGE SUPPORT | 98.00 | 98.12 | 0.12 | SUP | MODERATE | 7 | 30 | POI Tier 2: IP-Only. Drivers: P5-Prior daily closes cluster, P1-Daily pivot PP/S1 cluster, P6-Round 98.00 (A20:131-133). 4H BoM Demand 97.93-98.11 overlaps lower edge (A20:168-175). 'BREAKOUT SWEET SPOT (25-... |
| KEY SUPPORT BAND | 97.63 | 97.97 | 0.34 | SUP | HEAVY | 11 | 12 | POI Tier 1: Confluent. Drivers: P5-Liquidity Sweep Target 97.63, P5-4H BoM Demand 97.63-97.94, P1-Weekly S2/S3 cluster (A20:135-139). BoM 0X mitigated Demand; BoM Fresh: Yes; LSZ 97.63-97.68 ACTIVE SL TRIGGE... |

LSZ: 97.63-97.68 (Demand-side, ACTIVE SL TRIGGER); 97.83-97.88 (Demand-side, STANDARD); 97.97-98.02 (Demand-side, STANDARD); 98.53-98.58 (Demand-side, STANDARD); 98.29-98.34 (Supply-side, STANDARD); 99.18-99.23 (Supply-side, STANDARD)

4H zones: BoM Demand 97.93-98.11 [0X]; BoM Supply 98.77-98.99 [1X mitigated (1S)]; BoM Demand 97.63-97.94 [0X]; MoM Supply 98.34-98.42 [1X mitigated (1S)]

Key levels: Prior week (Apr 13-17) High 99.18; Prior week Low 97.63; Prior week Close 98.10; Weekly Classic R3 100.53; Weekly Classic R2 99.85; Weekly Classic R1 98.98; Weekly Classic PP 98.30; Weekly Classic S1 97.43; Weekly Classic S2 96.75; Weekly Classic S3 95.88; Weekly Fibonacci R3 99.85; Weekly Fibonacci R2 99.26; Weekly Fibonacci R1 98.90; Weekly Fibonacci PP 98.30; Weekly Fibonacci S1 97.71; Weekly Fibonacci S2 97.35; Weekly Fibonacci S3 96.75; Repeated High Magnet (3x dates) 98.29; Swing high repeated 2x 99.18; Liquidity Sweep Target 97.63

E2 current shape: SS (Swing Scalps); Anchor Zone 97.63-98.41; Confidence HIGH (A20:436-440)

E2 primary chain: SS -> BS -> R -> WL (52%) (A20:442)

E2 alternative chain: SS -> WLS -> BS (35%) (A20:444)

ACTUAL outcome: post-mortem: 'BUY trend all week' / 'SHORT consensus vs. actual BUY trend week' (PM20:24,150) - the primary chain direction (DOWN) was wrong

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | SS | RANGE | 97.95 | 98.20 | Confidence HIGH. Asian 'Range 97.95-98.20'; option cage EUR/USD 1.1750 pins DXY near 98.10 (A20:470-489) |
| Tue | SS -> BS (Downside potential) | DOWN | 98.29 | 97.63 | Confidence MODERATE-HIGH. 'If BS triggered: directional move toward Key Support Band 97.63-97.97. If SS continues: range 97.90-98.25.' (A20:504-524) |
| Wed | BS (Downside) / R (Recovery) | CONTINGENT | - | - | Confidence MODERATE. CPI: 'if hot: DXY surges toward 98.50-99.00 (R -> WL scenario). If cool: DXY drops toward 97.63 support (BS continues).' (A20:538-556) |
| Thu | R (Recovery) / SS | RANGE | - | - | Confidence MODERATE. 'Recovery day likely after 2 directional days (Tue/Wed)' (A20:571-590) |
| Fri | SS / WL | RANGE/WHIP | - | - | Confidence MODERATE. 'WL - Final resolution of the week.' (A20:604-623) |

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | type |
|---|---|---|---|---|---|---|---|
| - | S | 98.29 | 98.50 | 97.70 | 2.8 | 2.81 | Trade Setup 1: SHORT High at EQUILIBRIUM ZONE (Tier 2: IP-Only) |
| - | L | 97.85 | 97.55 | 98.65 | 4 | 2.67 **MISMATCH** | Trade Setup 2: LONG High at KEY SUPPORT BAND (Tier 1: Confluent) |
| Mon | L | 97.85 (97.85/97.75/97.68) | 97.58 | 98.25 | 2.5 | 1.48 (range 1.48-5.7) | Day trade: SS range bounce at floor zone (LONG DXY) |
| Tue | S | 98.25 (98.25/98.15/98.05) | 98.45 | 97.70 | 2.7 | 2.75 (range 0.87-2.75) | Day trade: BS downside from Equilibrium zone failure (SHORT DXY) - 'Highest-Confidence Trade' (A20:640) |
| Wed | - | 97.95 (97.95/97.80/97.68) | 97.55 | 98.25 | 3 | 0.75 (range 0.75-4.38) | Day trade: R/BS continuation - CPI-dependent ('CONTINGENT - If CPI cool: SHORT DXY. If CPI hot: LONG DXY.') |
| Thu | - | 97.90 (97.90/97.80/97.70) | 97.55 | 98.25 | 2.7 | 1 (range 1-3.67) | Day trade: R/SS range trade at mid-range support ('LONG DXY (if at support) / SHORT (if at resistance)') |
| Fri | - | 98.10 (98.10/98.00/97.85) | 97.55 | 98.45 | 2.2 | 0.64 (range 0.64-2) | Day trade: SS range trade / WL at key level ('CONTINGENT - React to Friday option data when available.') |

**Post-mortem (PM20 (generated 2026-05-25 21:00 UTC, PM20:13)).** Zone grades: RESISTANCE CEILING 99.16-99.23 = A+; UPPER RESISTANCE 98.77-98.99 = A; EQUILIBRIUM ZONE 98.29-98.41 = A+; MID-RANGE SUPPORT 98.00-98.12 = A; KEY SUPPORT BAND 97.63-97.97 = B/B+. LSZ grades: 97.63-97.68 = A+; 97.83-97.88 = A; 97.97-98.02 = A; 98.53-98.58 = A; 98.29-98.34 = A; 99.18-99.23 = A-/B+. System trade: SHORT 98.29 / SL 98.50 / TP 97.70 -> 'Loss (SL hit)'; 'BUY trend all week' (PM20:148-168).

Post-mortem 'actual trades that were available' (PM20:172-193):

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | note |
|---|---|---|---|---|---|---|---|
| Mon-Tue | S | 98.44 | 98.525 | 98.02 | 4.06 | 4.94 **MISMATCH** | CONFLICT in text: 'Entry at key 98.365 level' (PM20:179) vs Entry column 98.44; 98.44 is ABOVE the Equilibrium zone top 98.41. Arithmetic abs(98.02-98.44)/abs(98.44-98.525) = 4.94, not 4.06; (98.365-98.02)/(98.525-98.44) = 4.06 mixes the 98.365 key level as en |
| Tue-Thu | L | 98.02 | 97.87 | 98.77 | 5 | 5 | post-mortem actual trade #2: entry at LSZ edge (98.02) of Mid-Range Support, SL 1 pip inside next LSZ, TP at edge of Upper Resistance |
| Wed-Thu | L | 98.29 | 98.185 | 98.77 | 4.57 | 4.57 | post-mortem actual trade #3: reinforcement LONG from the Equilibrium Zone, SL 1 pip below zone, TP resistance edge |

**Caveats / CONFLICT / UNKNOWN:**

- DXY only - no pair zones in this report.
- Options: only Mon Apr 20 + Tue Apr 21 (forward data) included; 'Wednesday April 22 - Friday April 24 Option Data: EXCLUDED' (A20:38-39).
- Missing data log (A20:416-430): CME FX Futures OI C1/C2/C3 'PERMANENTLY BLOCKED'; Treasury auctions none; EIA none; 'Barchart MA Data ... Page reader timeout - using calculated MA approximations'; 'TradingView Technicals ... timeout'; ICE DXY Options OI + CME QuikStrike inaccessible.
- Post-mortem: KEY SUPPORT BAND 97.63-97.97 'Far too wide at 0.34 DXY span ... Should have been compressed to 97.75-97.97 or split into two sub-zones' (PM20:57-61); recommends 'tighter clustering threshold (0.10 DXY instead of 0.15) for zone assembly and treat spike extremes as separate LSZ entries' (PM20:85-86).
- Post-mortem: LSZ 99.18-99.23 'Bottom edge too high. Should be 99.13 - 99.23' (PM20:113-115).
- Internal inconsistency: Zone-detail LSZ for RESISTANCE CEILING (99.16-99.23) is printed as '98.29-98.34 (Supply-side, STANDARD)' (A20:147) which is the Equilibrium LSZ; the LSZ table has 99.18-99.23 for that area (A20:205).
- Reverse validation: 'DXY 98.10 -> implied EUR/USD = 1.1832 (actual spot: 1.1753, delta: 0.0079)' (A20:304) - a 79-pip miss against a stated '+/-0.07 DXY' band.
- Calendar oddities (not verified): 'Wed Apr 22 08:30 ET CPI (MoM) (Apr)' and 'Thu Apr 23 S&P Global ... PMI (May)' (A20:367-375).

### 4.3  Week of 2026-04-20 - `trident_v7 (2).pine`

- **Prompt version:** hardcoded Pine render of the v4.5.2 Apr20-24 report (indicator title 'TRIDENT v7')
- **Week identification:** table header literal 'DXY Apr20-24' (V7:309); comment 'Data week Apr 20-24 is the center; extends back to Apr 6, forward to May 15' (V7:34); tsL = timestamp(2026, 4, 6, 0, 0, 0), tsR = timestamp(2026, 5, 15, 23, 59, 59) (V7:36-37). CONFLICT inside the file: header comment 'ZONE DATE RANGE: Locked Apr 20 -> May 1 (2 weeks only)' (V7:15) vs the code's Apr 6 -> May 15.
- **Oracle grade:** Derivative of the Apr20-24 report (same grades apply). Adds nothing new for DXY except renamed zones and day labels of unknown provenance.

**Data the report used (pillars with real data).** No computation: every level is a literal array (V7:170-200). '4H Supply/Demand: REMOVED (data unreliable)' (V7:11); pivots removed (V7:12); trade setups table-only (V7:13).

#### DXY - spot at analysis: -

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| IP Resistance Ceiling | 99.16 | 99.23 | 0.07 | RES | HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T2. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/1.6*100) = 4% (differs from the report's ZFP; width-ZFP is deleted by ruling R-17) |
| Upper IP Resistance | 98.77 | 98.99 | 0.22 | RES | MODERATE-HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T1. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/1.6*100) = 14% (differs from the report's ZFP; width-ZFP is deleted by ruling R-17) |
| Equilibrium Zone | 98.29 | 98.41 | 0.12 | EQ | MODERATE-HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T2. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/1.6*100) = 7% (differs from the report's ZFP; width-ZFP is deleted by ruling R-17) |
| Mid-Range Support | 98.00 | 98.12 | 0.12 | SUP | MODERATE | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T2. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/1.6*100) = 8% (differs from the report's ZFP; width-ZFP is deleted by ruling R-17) |
| Key IP Support | 97.63 | 97.97 | 0.34 | SUP | HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T1. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/1.6*100) = 21% (differs from the report's ZFP; width-ZFP is deleted by ruling R-17) |

LSZ: 97.63-97.68 (ACTIVE); 97.83-97.88 (STANDARD); 97.97-98.02 (STANDARD); 98.53-98.58 (STANDARD); 98.29-98.34 (STANDARD); 99.18-99.23 (STANDARD)

Key levels: Option Strike Target 1.9bn 99.22; Option Strike Target 2.6bn 98.49; Option Strike Target 1.1bn 98.32; Option Strike Target 1.0bn 97.78; Option Strike Target 1.8bn 98.86; Option Strike Target 1.1bn 98.44; Option Strike Target 1.8bn 98.25

E2 primary chain: SS>BS>R>WL 52%

E2 alternative chain: SS>WLS>BS 35%

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | SS/H | - | - | - | table 'Days' string: 'M:SS/H T:SS-BS W:BS-R Th:R-SS F:SS-WL' ('H' is not expanded anywhere in the script - UNKNOWN meaning) |
| Tue | SS-BS | - | - | - |  |
| Wed | BS-R | - | - | - |  |
| Thu | R-SS | - | - | - |  |
| Fri | SS-WL | - | - | - |  |

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | type |
|---|---|---|---|---|---|---|---|
| Wed | S | 98.29 (98.29/98.05) | 98.50 | 97.70 | 2.8 | 2.81 (range 0.78-2.81) | table trade 'S T2' entry range 98.29 - 98.05; days 'Wed > Thu-Fri' |
| Thu | L | 97.85 (97.85/97.68) | 97.55 | 98.65 | 4 | 2.67 (range 2.67-7.46) | table trade 'L T1' entry range 97.85 - 97.68; days 'Thu > Fri' |

### 4.4  Week of 2026-04-20 - `trident_v8.pine`

- **Prompt version:** hardcoded Pine render (indicator title 'TRIDENT v8 - 4-Pair Master')
- **Week identification:** section comments 'DATA - DXY (Apr 20-24 2026)', 'DATA - EUR/USD (Apr 20-24 2026)', 'DATA - GBP/USD (Apr 20-24 2026)', 'DATA - AUD/USD (Apr 20-24 2026)' (V8:184,216,251,284); table headers 'DXY Apr20-24' etc. (V8:392,473,554,635); tsL = timestamp(2026, 4, 6, ...), tsR = timestamp(2026, 5, 15, ...) (V8:35-36). Both v7 and v8 encode the SAME week: 2026-04-20.
- **Oracle grade:** DXY block = v7 = the Apr20-24 report. EUR/USD, GBP/USD, AUD/USD blocks have NO source report on disk (the Apr20-24 report is DXY-only) and fail cross-checks -> treat as UNVERIFIED / likely synthetic, NOT as oracle.

**Data the report used (pillars with real data).** No computation: literal arrays only (V8:187-314). '4H S/D Zones: REMOVED (user maps manually)' (V8:11). 'NO mathematical conversion between pairs' (V8:20).

#### DXY - spot at analysis: -

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| IP Resistance Ceiling | 99.16 | 99.23 | 0.07 | RES | HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T2. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/1.6*100) = 4% (differs from the report's ZFP; width-ZFP is deleted by ruling R-17) |
| Upper IP Resistance | 98.77 | 98.99 | 0.22 | RES | MODERATE-HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T1. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/1.6*100) = 14% (differs from the report's ZFP; width-ZFP is deleted by ruling R-17) |
| Equilibrium Zone | 98.29 | 98.41 | 0.12 | EQ | MODERATE-HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T2. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/1.6*100) = 7% (differs from the report's ZFP; width-ZFP is deleted by ruling R-17) |
| Mid-Range Support | 98.00 | 98.12 | 0.12 | SUP | MODERATE | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T2. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/1.6*100) = 8% (differs from the report's ZFP; width-ZFP is deleted by ruling R-17) |
| Key IP Support | 97.63 | 97.97 | 0.34 | SUP | HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T1. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/1.6*100) = 21% (differs from the report's ZFP; width-ZFP is deleted by ruling R-17) |

LSZ: 97.63-97.68 (ACTIVE); 97.83-97.88 (STANDARD); 97.97-98.02 (STANDARD); 98.53-98.58 (STANDARD); 98.29-98.34 (STANDARD); 99.18-99.23 (STANDARD)

Key levels: Option Strike Target 1.9bn 99.22; Option Strike Target 2.6bn 98.49; Option Strike Target 1.1bn 98.32; Option Strike Target 1.0bn 97.78; Option Strike Target 1.8bn 98.86; Option Strike Target 1.1bn 98.44; Option Strike Target 1.8bn 98.25

E2 primary chain: SS>BS>R>WL 52%

E2 alternative chain: SS>WLS>BS 35%

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | SS/H | - | - | - | table 'Days' string: 'M:SS/H T:SS-BS W:BS-R Th:R-SS F:SS-WL' ('H' is not expanded anywhere in the script - UNKNOWN meaning) |
| Tue | SS-BS | - | - | - |  |
| Wed | BS-R | - | - | - |  |
| Thu | R-SS | - | - | - |  |
| Fri | SS-WL | - | - | - |  |

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | type |
|---|---|---|---|---|---|---|---|
| Wed | S | 98.29 (98.29/98.05) | 98.50 | 97.70 | 2.8 | 2.81 (range 0.78-2.81) | table trade 'S T2' entry range 98.29 - 98.05; days 'Wed > Thu-Fri' |
| Thu | L | 97.85 (97.85/97.68) | 97.55 | 98.65 | 4 | 2.67 (range 2.67-7.46) | table trade 'L T1' entry range 97.85 - 97.68; days 'Thu > Fri' |

#### EURUSD - spot at analysis: -

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| Key IP Resistance Band | 1.1700 | 1.1720 | 0.0020 | RES | HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T2. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/0.02*100) = 10% (differs from the report's ZFP; width-ZFP is deleted by ruling R... |
| Upper IP Resistance | 1.1660 | 1.1685 | 0.0025 | RES | MODERATE-HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T1. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/0.02*100) = 13% (differs from the report's ZFP; width-ZFP is deleted by ruling R... |
| Equilibrium Zone | 1.1610 | 1.1635 | 0.0025 | EQ | MODERATE-HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T2. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/0.02*100) = 12% (differs from the report's ZFP; width-ZFP is deleted by ruling R... |
| Mid-Range Support | 1.1570 | 1.1595 | 0.0025 | SUP | MODERATE | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T2. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/0.02*100) = 12% (differs from the report's ZFP; width-ZFP is deleted by ruling R... |
| IP Support Floor | 1.1520 | 1.1555 | 0.0035 | SUP | HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T1. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/0.02*100) = 18% (differs from the report's ZFP; width-ZFP is deleted by ruling R... |

LSZ: 1.1480-1.1500 (ACTIVE); 1.1545-1.1560 (STANDARD); 1.1590-1.1605 (STANDARD); 1.1675-1.1690 (STANDARD); 1.1645-1.1660 (STANDARD); 1.1700-1.1715 (STANDARD)

Key levels: Option Strike Target 1.9bn 1.1700; Option Strike Target 2.6bn 1.1625; Option Strike Target 1.1bn 1.1600; Option Strike Target 1.0bn 1.1500; Option Strike Target 1.8bn 1.1650; Option Strike Target 1.1bn 1.1610; Option Strike Target 1.8bn 1.1595

E2 primary chain: SS>BS>R>WL 52%

E2 alternative chain: SS>WLS>BS 35%

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | SS/H | - | - | - | table 'Days' string: 'M:SS/H T:SS-BS W:BS-R Th:R-SS F:SS-WL' ('H' is not expanded anywhere in the script - UNKNOWN meaning) |
| Tue | SS-BS | - | - | - |  |
| Wed | BS-R | - | - | - |  |
| Thu | R-SS | - | - | - |  |
| Fri | SS-WL | - | - | - |  |

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | type |
|---|---|---|---|---|---|---|---|
| Wed | S | 1.1595 (1.1595/1.1570) | 1.1650 | 1.1520 | 2.6 | 1.36 (range 0.63-1.36) **MISMATCH** | table trade 'S T2' entry range 1.1595 - 1.157; days 'Wed > Thu-Fri' |
| Thu | L | 1.1530 (1.1530/1.1505) | 1.1480 | 1.1680 | 3.5 | 3 (range 3-7) | table trade 'L T1' entry range 1.153 - 1.1505; days 'Thu > Fri' |

#### GBPUSD - spot at analysis: -

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| Key IP Resistance Band | 1.3555 | 1.3580 | 0.0025 | RES | HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T2. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/0.02*100) = 13% (differs from the report's ZFP; width-ZFP is deleted by ruling R... |
| Upper IP Resistance | 1.3510 | 1.3540 | 0.0030 | RES | MODERATE-HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T1. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/0.02*100) = 15% (differs from the report's ZFP; width-ZFP is deleted by ruling R... |
| Equilibrium Zone | 1.3460 | 1.3485 | 0.0025 | EQ | MODERATE-HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T2. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/0.02*100) = 12% (differs from the report's ZFP; width-ZFP is deleted by ruling R... |
| Mid-Range Support | 1.3410 | 1.3440 | 0.0030 | SUP | MODERATE | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T2. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/0.02*100) = 15% (differs from the report's ZFP; width-ZFP is deleted by ruling R... |
| IP Support Floor | 1.3360 | 1.3395 | 0.0035 | SUP | HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T1. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/0.02*100) = 17% (differs from the report's ZFP; width-ZFP is deleted by ruling R... |

LSZ: 1.3320-1.3340 (ACTIVE); 1.3395-1.3415 (STANDARD); 1.3435-1.3455 (STANDARD); 1.3510-1.3530 (STANDARD); 1.3480-1.3500 (STANDARD); 1.3555-1.3570 (STANDARD)

Key levels: Option Strike Target 0.9bn 1.3560; Option Strike Target 1.2bn 1.3495; Option Strike Target 0.8bn 1.3470; Option Strike Target 1.0bn 1.3350; Option Strike Target 1.1bn 1.3525; Option Strike Target 0.7bn 1.3480; Option Strike Target 0.9bn 1.3465

E2 primary chain: SS>BS>R>WL 52%

E2 alternative chain: SS>WLS>BS 35%

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | SS/H | - | - | - | table 'Days' string: 'M:SS/H T:SS-BS W:BS-R Th:R-SS F:SS-WL' ('H' is not expanded anywhere in the script - UNKNOWN meaning) |
| Tue | SS-BS | - | - | - |  |
| Wed | BS-R | - | - | - |  |
| Thu | R-SS | - | - | - |  |
| Fri | SS-WL | - | - | - |  |

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | type |
|---|---|---|---|---|---|---|---|
| Wed | S | 1.3440 (1.3440/1.3410) | 1.3500 | 1.3360 | 2.4 | 1.33 (range 0.56-1.33) **MISMATCH** | table trade 'S T2' entry range 1.344 - 1.341; days 'Wed > Thu-Fri' |
| Thu | L | 1.3370 (1.3370/1.3345) | 1.3320 | 1.3540 | 3.2 | 3.4 (range 3.4-7.8) | table trade 'L T1' entry range 1.337 - 1.3345; days 'Thu > Fri' |

#### AUDUSD - spot at analysis: -

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| Key IP Resistance Band | 0.7255 | 0.7280 | 0.0025 | RES | HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T2. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/0.015*100) = 17% (differs from the report's ZFP; width-ZFP is deleted by ruling ... |
| Upper IP Resistance | 0.7210 | 0.7240 | 0.0030 | RES | MODERATE-HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T1. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/0.015*100) = 20% (differs from the report's ZFP; width-ZFP is deleted by ruling ... |
| Equilibrium Zone | 0.7160 | 0.7185 | 0.0025 | EQ | MODERATE-HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T2. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/0.015*100) = 17% (differs from the report's ZFP; width-ZFP is deleted by ruling ... |
| Mid-Range Support | 0.7110 | 0.7140 | 0.0030 | SUP | MODERATE | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T2. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/0.015*100) = 20% (differs from the report's ZFP; width-ZFP is deleted by ruling ... |
| IP Support Floor | 0.7060 | 0.7095 | 0.0035 | SUP | HEAVY | - | - | pine arrays zTp/zBt/zCat/zDeg/zTir/zNm; tier T1. ZFP is NOT stored: the script computes a WIDTH-based ZFP = round((top-bottom)/0.015*100) = 23% (differs from the report's ZFP; width-ZFP is deleted by ruling ... |

LSZ: 0.7020-0.7040 (ACTIVE); 0.7095-0.7115 (STANDARD); 0.7135-0.7155 (STANDARD); 0.7210-0.7230 (STANDARD); 0.7180-0.7200 (STANDARD); 0.7255-0.7270 (STANDARD)

Key levels: Option Strike Target 0.8bn 0.7260; Option Strike Target 1.1bn 0.7195; Option Strike Target 0.7bn 0.7170; Option Strike Target 0.9bn 0.7050; Option Strike Target 1.0bn 0.7225; Option Strike Target 0.6bn 0.7180; Option Strike Target 0.8bn 0.7165

E2 primary chain: SS>BS>R>WL 52%

E2 alternative chain: SS>WLS>BS 35%

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | SS/H | - | - | - | table 'Days' string: 'M:SS/H T:SS-BS W:BS-R Th:R-SS F:SS-WL' ('H' is not expanded anywhere in the script - UNKNOWN meaning) |
| Tue | SS-BS | - | - | - |  |
| Wed | BS-R | - | - | - |  |
| Thu | R-SS | - | - | - |  |
| Fri | SS-WL | - | - | - |  |

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | type |
|---|---|---|---|---|---|---|---|
| Wed | S | 0.7140 (0.7140/0.7110) | 0.7200 | 0.7060 | 2.3 | 1.33 (range 0.56-1.33) **MISMATCH** | table trade 'S T2' entry range 0.714 - 0.711; days 'Wed > Thu-Fri' |
| Thu | L | 0.7070 (0.7070/0.7045) | 0.7020 | 0.7240 | 3.1 | 3.4 (range 3.4-7.8) **MISMATCH** | table trade 'L T1' entry range 0.707 - 0.7045; days 'Thu > Fri' |

**Caveats / CONFLICT / UNKNOWN:**

- EU/GU/AU provenance UNKNOWN: comment says 'Structurally equivalent zones from pair-specific data sources ... Price levels from EU's own MA structure, swing levels, institutional commentary' (V8:217-219) but no such data exists in any listed report. handover-branch/data/e1/EURUSD-2026-04-20.json labels the same EU numbers 'CANON - the v8's exact EU example (transcribed)' with spot 1.163.
- CONFLICT (EU level sanity): the Apr20-24 report gives EUR/USD 'actual spot: 1.1753' (A20:304) and option strikes 1.1600-1.1900 (A20:47-82); v8's EU zone ladder spans 1.1520-1.1720 with Equilibrium 1.1610-1.1635, i.e. the whole ladder sits below the report's EUR/USD spot.
- CONFLICT (EU options): v8 eu_oPr = 1.1700/1.1625/1.1600/1.1500/1.1650/1.1610/1.1595 carrying notionals 1.9bn/2.6bn/1.1bn/1.0bn/1.8bn/1.1bn/1.8bn (V8:233-234). The report's real EUR/USD strikes for those notionals are 1.1600/1.1750/1.1785/1.1900/1.1675/1.1760/1.1800 (A20:47-80). Same notionals, different strikes -> the v8 EU option levels are not the report's data.
- GU/AU options (V8:266-267, 299-300) have no counterpart: the report lists only GBP/USD 1.3500 (GBP 1.0bn) Mon and 1.3300 (GBP 1.0bn) Tue (A20:56,85) and no AUD/USD strikes.
- Pair zone widths are a fixed template (EU 20/25/25/25/35 pips; GU 25/30/25/30/35; AU 25/30/25/30/35) with degrees/tiers/chain/day labels copied verbatim from DXY; pair trade DIRECTIONS are copied from DXY (S first, L second) rather than inverted, contradicting the comment 'DXY RESISTANCE -> EU SUPPORT, DXY SUPPORT -> EU RESISTANCE' (V8:218).
- ZFP in v8 is width-based: calcZFP = round(zoneW / refRange * 100), refRange DXY 1.60, EUR/USD 0.0200, GBP/USD 0.0200, AUD/USD 0.0150 (V8:334-338).

### 4.5  Week of 2026-04-27 - `Leviathan_DXY_IL_Report_Apr27-May1_2026.pdf`

- **Prompt version:** UNKNOWN prompt version; cover prints 'Engine: Leviathan Quant Analytics v2' (A27:28). PDF Creator 'Leviathan Quant Analytics Engine', Producer pypdf (pdfinfo). Different template from the other Leviathan reports (12 numbered zones incl. LIGHT/MINIMAL, 3-decimal prices, no POI tiers, no per-zone ZFP).
- **Data as-of:** April 24, 2026 17:00 ET (A27:27)
- **Generated:** UNKNOWN (no generation timestamp printed; PDF has no CreationDate in pdfinfo)
- **Oracle grade:** No operator grade found. E3 is a 3-row 'Trade Flow Map' that self-reports 'Minimum RRR Threshold Check FAIL for primary (4.0x < 5.0x)' (A27:607).

**Data the report used (pillars with real data).** REAL (as printed): Protocol A options all 5 days from investinglive incl. DISPUTED rows (A27:109-242, 527-529); Pillar 1 weekly Classic/Fibonacci/Camarilla from H=98.940 L=98.010 C=98.510 + daily pivots (A27:345-353); Pillar 2 MAs named in drivers (SMA9/EMA9/SMA10, EMA20, SMA20, EMA50, EMA100) (A27:279-289); Pillar 3/8 K=108.085515 from yfinance component rates (A27:249-250, 359-371); Pillar 4 analyst = one 'FXStreet Res 99.35' + 'Analyst=1.0' tags (A27:269-275); Pillar 5 swing highs/lows + prior-week H/L liquidity sweeps; Pillar 6 90d Fib + figures; 4H BoM/MoM overlay (A27:316-339); Protocol D Treasury B/C (A27:402-415); Protocol E ON RRP $0.082B (A27:420-435); Protocol F calendar; Protocol G EIA -6.2M (A27:462-472). NO DATA: CME FX OI C1/C2/C3 'ALL BLOCKED'; ICE DXY options 'Not attempted' (A27:519-523).

#### DXY - spot at analysis: 98.51

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| Upper Resistance | 99.893 | 100.00 | 0.107 | RES | MINIMAL | 3 | - | Major Big Figure 100.00; Wk Classic R3 99.893; Tech=1.0 Psych=2.0 |
| Resistance | 99.60 | 99.725 | 0.125 | RES | MINIMAL | 3 | - | EUR/USD 1.1500 DXY 99.725 (Fri SIGNIFICANT); 90d Fib 23.6% 99.600; Tech=0.5 Options=1.5 Struct=1.0 |
| Resistance | 99.393 | 99.50 | 0.107 | RES | LIGHT | 4.5 | - | Half Figure 99.50; Swing High 99.440; Wk Classic R2 99.417; Tech=2.0 Struct=1.0 Psych=1.5 |
| Resistance | 99.22 | 99.35 | 0.13 | RES | LIGHT | 4 | - | FXStreet Res 99.35; EUR/USD 1.1600 DXY 99.229 (Tue 3.5bn CRITICAL); Daily R3 99.220; Tech=1.0 Options=2.0 Analyst=1.0 |
| Resistance | 99.055 | 99.18 | 0.125 | RES | LIGHT | 4 | - | 2026 High 99.18; Swing High 99.180; Thu Fib R3 99.167; Fri Fib R3 99.070; Tech=2.0 Analyst=1.0 Struct=1.0 |
| Upper Equilibrium / Decision Zone | 98.92 | 99.022 | 0.102 | EQ | MODERATE-HEAVY | 8 | 25-35 | Wk Cam R4 99.022; Major Fig 99.00; 90d Fib 38.2% 98.997; EUR/USD 1.1650 DXY 98.991 (Mon-Wed 7.7bn CRITICAL); SMA9/EMA9/SMA10 cluster; Prior Wk High 98.940; Tech=2.0 Options=2.0 Struct=2.0 Psych=2.0 |
| Equilibrium | 98.721 | 98.842 | 0.121 | EQ | LIGHT | 4 | - | Wk Fib R1 98.842; EUR/USD 1.1680 DXY 98.837 (Tue 1.7bn CRITICAL); EMA20 98.804; Daily R1 98.790; Tech=2.0 Options=2.0 |
| Mid-Range Support / Equilibrium | 98.529 | 98.673 | 0.144 | SUP | MODERATE | 7 | - | EMA100 98.673; Daily PP 98.640; SMA20 98.631; EUR/USD 1.1725 DXY 98.619 (Tue-Thu 4.5bn CRITICAL); EMA50 98.734; Tech=2.0 Options=2.0 Analyst=1.0 Struct=2.0. [dual label; zone lies ABOVE spot 98.510; side set... |
| Key Support Band | 98.353 | 98.50 | 0.147 | SUP | MODERATE | 7.5 | - | Half Fig 98.50; Apr 24 Daily Low 98.490; Wk Classic PP 98.480; Wk Fib 50% 98.475; EUR/USD 1.1755 DXY 98.473 (Tue 4.5bn CRITICAL); BoM Supply [98.14-98.29] 0X; Tech=2.0 Options=2.0 Struct=2.0 Psych=1.5 |
| Support | 98.131 | 98.257 | 0.126 | SUP | LIGHT | 5 | - | EUR/USD 1.1800 DXY 98.257 (Tue-Thu 2.8bn CRITICAL); Wk Fib S1 98.131; 90d Fib 61.8% 98.133; Tech=2.0 Options=2.0 Struct=1.0 |
| Lower Support / Liquidity Sweep | 97.93 | 98.033 | 0.103 | SUP | MODERATE-HEAVY | 8.5 | 20-30 | Wk Classic S1 98.033; EUR/USD 1.1850 DXY 98.018 (Fri 964m SIGNIFICANT); Prior Wk Low 98.010 LIQ SWEEP; Major Fig 98.00; Fri Classic S3 97.930; BoM Demand [98.01-98.23] 0X; Tech=2.0 Options=1.5 Analyst=1.0 St... |
| Deep Support | 97.50 | 97.63 | 0.13 | SUP | LIGHT | 4.5 | - | Swing Low 97.630 (Apr 17) LIQ SWEEP; Wk Classic S2 97.557; Half Fig 97.50; Tech=1.0 Struct=1.0 Psych=1.5 +Bonus 1.0 |

4H zones: BoM Demand 98.01-98.23 [0X]; MoM Supply 98.88-99.18 [1X (1S)]; BoM Supply 98.14-98.29 [0X]; BoM Supply 99.92-100.16 [1X (1S)]; MoM Demand 99.45-99.72 [2X (1S,1H)]

Key levels: Prior week (Apr 20-24) High 98.94; Prior week Low 98.01; Prior week Close 98.51; Weekly Classic PP 98.487; Weekly Classic R1 98.963; Weekly Classic R2 99.417; Weekly Classic R3 99.893; Weekly Classic S1 98.033; Weekly Classic S2 97.557; Weekly Classic S3 97.103; Weekly Fibonacci R1 98.842; Weekly Fibonacci R2 99.061; Weekly Fibonacci R3 99.417; Weekly Fibonacci S1 98.131; Weekly Fibonacci S2 97.912; Weekly Fibonacci S3 97.557; Weekly Camarilla R1 98.595; Weekly Camarilla R2 98.681; Weekly Camarilla R3 98.766; Weekly Camarilla R4 99.022; Weekly Camarilla S1 98.425; Weekly Camarilla S2 98.34; Weekly Camarilla S3 98.254; Weekly Camarilla S4 97.999; EUR/USD 1.1500 -> DXY 99.725; EUR/USD 1.1600 -> DXY 99.229; EUR/USD 1.1650 -> DXY 98.991; EUR/USD 1.1680 -> DXY 98.837; EUR/USD 1.1725 -> DXY 98.619; EUR/USD 1.1755 -> DXY 98.473; EUR/USD 1.1800 -> DXY 98.257; EUR/USD 1.1850 -> DXY 98.018; EMA100 98.673; SMA20 98.631; EMA50 98.734; EMA20 98.804; 2026 High / Swing High 99.18; Swing High 99.44; Swing Low (Apr 17) LIQ SWEEP 97.63; Prior Wk Low LIQ SWEEP 98.01

E2 current shape: SS (Swing Scalps). 'Price oscillating between Heavy ceiling (~99.00) and Moderate floor (~98.50). Both boundary zones have ZFP < 35%. Prior week range: 98.010-98.940 (93 pip range).' (A27:535-537)

E2 primary chain: SS -> BS -> R -> WL, 52%, trigger 'FOMC decision triggers BS directionally' (A27:541)

E2 alternative chain: SS -> WLS -> BS, 35%, 'FOMC hold + mixed GDP/PCE -> WLS, resolves into BS on Fri' (A27:543)

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | SS | RANGE | 98.35 | 98.70 | Asian SS (range-bound 98.35-98.70) / London SS -> potential BS if CPI surprise / NY Pre-Cut SS (pinned near 98.50-98.65 option zone); 'If CPI hot -> BS up toward 98.92-99.00; If CPI soft -> SS continues' (A27:552-555) |
| Tue | SS -> possible BS | - | 98.50 | 98.80 | Asian SS (98.50-98.80) / London SS -> possible BS initiation / NY Pre-Cut PINNED to 98.99 (EUR/USD 1.1650 7.7bn) or 98.62 (EUR/USD 1.1725 4.5bn); Spring Release 'CRITICAL ... MoM Supply [98.88-99.18] = potential ladder step in ... |
| Wed | SS (pre-FOMC) -> BS conditional | CONTINGENT | - | - | 'If hold (expected): SS continues with mild BS toward ceiling. If dovish surprise: BS DOWN through 98.50 toward 98.00. If hawkish surprise: BS UP through 99.00 toward 99.35-99.50.' (A27:565-568) |
| Thu | BS UP continuation or RWL | CONTINGENT | - | - | 'If hot GDP: BS UP continuation from FOMC. If weak GDP: RWL (reversal of any Wed BS). ... Key: 98.00 support must hold for bullish bias.' (A27:571-573) |
| Fri | SS range or WL at target | CONTINGENT | 98.35 | 98.70 | 'If SS all week: Friday range 98.35-98.70. If BS occurred: WL at target zone.' (A27:579-581) |

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | type |
|---|---|---|---|---|---|---|---|
| - | L | 98.50 (98.50/98.40/98.35) | 98.25 | 98.67 | 3.2 | 0.68 (range 0.68-3.8) | Trade 1 LONG 'SS floor bounce', entry zone 98.35-98.50, TP 98.67-98.73 |
| Wed (post-FOMC) | L | 98.50 (98.50/98.60/98.70) | 98.25 | 98.92 | 4.9 | 1.68 (range 0.49-2) **MISMATCH** | Trade 2 LONG 'post-FOMC directional', TP 98.92-99.00 |
| - | S | 99.00 (99.00/98.95/98.92) | 99.15 | 98.50 | 3.8 | 3.33 (range 1.83-3.33) **MISMATCH** | Trade 3 SHORT 'ceiling rejection', entry zone 98.92-99.00 |
| Wed (if FOMC dovish) | S | 98.50 | 98.75 | 98.00 | 2 | 2 | Alternative Trade 2 SHORT (supplementary) |

**Caveats / CONFLICT / UNKNOWN:**

- TEMPORAL-BOUNDARY CONFLICT: 'Data As-Of: April 24, 2026 17:00 ET' (A27:27) yet the option tables cover every day Mon Apr 27 - Fri May 1 (A27:109-240) from 'investinglive.com FX Option Expiries (Apr 27 - May 1, 2026, 10am NY Cut)' (A27:242). Daily investinglive pages are published on the day; the Apr20-24 report explicitly EXCLUDED Wed-Fri for this reason (A20:38-39). Wed/Thu/Fri strikes feed zone scores here (e.g. zone 2 'Fri SIGNIFICANT', zone 11 'Fri 964m', zones 8/10 'Tue-Thu').
- ZFP is given for only 2 of 12 zones, as ranges (zone 6 ~25-35%, zone 11 ~20-30%) (A27:496,504); all other zones zfp = null.
- 4H overlay rows contradict the zone table geometry: 'BoM Supply [98.14-98.29] 0X AGREE Zone 9 ceiling' (A27:327) but zone 9 is 98.353-98.500; 'BoM Demand [98.01-98.23] 0X AGREE Zone 11 floor' (A27:321-322) but zone 11 is 97.930-98.033.
- Arithmetic: zone 6 driver 'EUR/USD 1.1650 ... (Mon-Wed 7.7bn CRITICAL)' (A27:279); the tables give 1.1650 = 2.3bn Mon + 2.7bn Tue + 1.7bn Wed = 6.7bn (A27:112,137,178).
- Scores are fractional (x.0/x.5 of 14) with dimension sums printed in drivers (e.g. zone 6: 2.0+2.0+2.0+2.0 = 8.0; zone 11: 2.0+1.5+1.0+1.0+2.0+1.0 bonus = 8.5).
- Calendar oddity (not verified): 'Mon Apr 27 07:30 Core CPI (USD) RED FOLDER' (A27:443) while the prior report placed CPI on Wed Apr 22 (A20:367).

### 4.6  Week of 2026-05-04 - `Leviathan_DXY_IL_Report_May05-04_2026.pdf`

- **Prompt version:** Leviathan v4.4 (Dual-Engine: 9-Pillar 6D Hybrid + Macro Shape Chain Map) (M04:6)
- **Data as-of:** May 1, 2026 17:00 ET (M04:3); options from the May 4 investinglive page
- **Generated:** CONFLICT: printed 'Generated: May 4, 2026 06:00 GMT (Pre-London Session Open)' (M04:5) vs PDF metadata 'CreationDate: Sun May 24 19:24:30 2026 UTC' (pdfinfo). File name says 'May05-04'; title/body say 'Week of May 4-8, 2026'.
- **Oracle grade:** No operator grade found. Dual-engine version: NO Engine 3 section; trade setups appear only inside the Monday day-map and the weekly visualization.

**Data the report used (pillars with real data).** REAL: Protocol A options Mon May 4 + Tue May 5 forward data, investinglive, 'VLM 3-Pass' (M04:12-80); Pillar 1 weekly Classic/Fibonacci/Camarilla from H=99.34 L=97.72 C=98.21 + 3 daily pivot sets (M04:108-138); Pillar 8 K=107.6077 with verification 'K x 1.1731^(-0.576) = 98.15 | Actual DXY May 1 close: 98.21 | Delta: 0.06' (M04:165-168); Pillar 4 forex.com (Matt Weller CMT) levels 98.49 / 99.49 / 100.16-42 / 97.50-65 / 96.88-98 (M04:207-226); Pillar 5 swing lows/highs + repeated magnets (M04:233-259); Pillar 6 fib + round numbers (M04:264-280); Pillar 9 regime 'MOMENTUM (bearish)' (M04:285); Protocol D Treasury (2Y B/C 2.65x = VOLATILITY TRIGGER) (M04:361-377); Protocol F calendar (M04:390-403). ESTIMATED: Pillar 2 MAs. PARTIAL: Protocol E ON RRP (M04:382-385). NO DATA: CME C1/C2/C3 'PERMANENTLY BLOCKED', Pillar 7 ICE DXY options, EIA, May 5-8 option pages, USD/SEK spot (H.10 supplementary) (M04:446-456). No 4H BoM/MoM overlay and no LSZ table in this version.

#### DXY - spot at analysis: 98.21

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| RESISTANCE CEILING | 99.05 | 99.34 | 0.29 | RES | HEAVY | 10 | 12 | Levels: 99.34 (P5 Supply Ceiling), 99.09 (P5 Supply Ceiling), 99.13 (P1 Classic R1), 99.05 (P5 Swing High), 99.00 (P6 Round #). Primary Driver: Pillar 5 + Pillar 4. Structural Extreme: Supply Ceiling Target ... |
| UPPER RESISTANCE | 98.49 | 98.70 | 0.21 | RES | HEAVY | 12 | 10 | Levels: 98.49 (P4 Analyst), 98.51 (P1 Cam R2), 98.50 (P2 SMA 100), 98.55 (P2 SMA 200), 98.55 (P8 EUR/USD 1.1650), 98.62 (P8 EUR/USD 1.1635 TUE), 98.70 (P2 SMA 50). Primary Driver: Pillar 2 (MA Confluence) + ... |
| EQUILIBRIUM / DECISION ZONE | 98.06 | 98.42 | 0.36 | EQ | MODERATE-HEAVY | 9 | 22 | Levels: 98.42 (P1 Weekly PP), 98.40 (P2 SMA 20 RECAPTURE), 98.39 (P1 Daily R1 May1), 98.30 (P8 EUR/USD 1.1700 MON), 98.30 (P8 EUR/USD 1.1700 TUE), 98.21 (P5 Prior Close), 98.06 (P1 Cam S1), 98.06 (P8 EUR/USD... |
| MID-RANGE SUPPORT | 97.80 | 98.00 | 0.20 | SUP | MODERATE | 7 | 30 | Levels: 97.87 (P1 Daily S1 May1), 97.82 (P8 EUR/USD 1.1800 MON/TUE), 97.80 (P1 Fib S1), 98.00 (P6 Round Number), 98.01 (P5 Demand Zone Apr30). Structural Extreme: Repeated Extreme Magnet (98.00). Clustering:... |
| KEY SUPPORT BAND | 97.50 | 97.72 | 0.22 | SUP | HEAVY | 11 | 15 | Levels: 97.51 (P1 Classic S1), 97.63 (P5 Liquidity Sweep Apr17), 97.72 (P5 Liquidity Sweep May1), 97.65 (P4 Analyst Key Support), 97.50 (P4 Analyst Key Support + P6 Half Figure), 97.54 (P1 Daily S2 May1). Ex... |
| BREAKDOWN EXTENSION TARGET | 96.80 | 97.00 | 0.20 | SUP | LIGHT | 5 | 55 | Levels: 96.80 (P1 Classic S2), 96.88 (P4 Analyst Support), 97.00 (P6 Round Number). Clustering: TIGHT CONFLUENCE (3 levels). Measured Move: If 97.50-72 fails: 97.72 - (99.34-97.72) = 96.10 (Anchored to 95.55... |

Key levels: Prior week High 99.34; Prior week Low 97.72; Prior week Close 98.21; Weekly Classic R3 100.75; Weekly Classic R2 100.04; Weekly Classic R1 99.13; Weekly PP 98.42; Weekly Classic S1 97.51; Weekly Classic S2 96.80; Weekly Classic S3 95.89; Weekly Fibonacci R3 100.04; Weekly Fibonacci R2 99.42; Weekly Fibonacci R1 99.04; Weekly Fibonacci S1 97.80; Weekly Fibonacci S2 97.42; Weekly Fibonacci S3 96.80; Weekly Camarilla R3 98.66; Weekly Camarilla R2 98.51; Weekly Camarilla R1 98.36; Weekly Camarilla PP (printed) 98.21; Weekly Camarilla S1 98.06; Weekly Camarilla S2 97.91; Weekly Camarilla S3 97.76; Weekly Camarilla S4 97.32; Daily PP Apr 29 98.85; Daily PP Apr 30 98.39; Daily PP May 1 98.06; Daily R1 May 1 98.39; Daily S1 May 1 97.87; Daily R2 May 1 98.58; Daily S2 May 1 97.54; EMA 9 (~) 98.10; SMA 20 (~) RECAPTURE ZONE 98.40; SMA 50 (~) 98.70; SMA 100 (~) 98.50; SMA 200 (~) 98.55; Analyst resistance forex.com (Weller) 98.49; Analyst key resistance 99.49; Analyst key support low 97.50; Analyst key support high 97.65; 52W Low 95.55; 52W High 100.64; Swing low May 1 (Liquidity Sweep Target) 97.72; Swing low Apr 17 (Liquidity Sweep Target) 97.63; Swing low Apr 30 (Demand Zone Base) 98.01; Swing high Apr 27 (Supply Ceiling Target) 99.34; Swing high Apr 30 (Supply Ceiling Target) 99.09; Fib 23.6% 98.96; Fib 38.2% 98.72; Fib 50.0% 98.53; Fib 61.8% 98.34

E2 current shape: SWING SCALPS (SS) | Confidence: HIGH | Anchor Zone: Upper Resistance 98.49-98.70 (HEAVY, 12/14) to KEY SUPPORT 97.50-97.72 (HEAVY, 11/14) (M04:468-473)

E2 primary chain: SS -> BS (downside) -> R -> WL | Chain Confidence: 26% (M04:494)

E2 alternative chain: SS -> WLS -> BS (upside) | Chain Confidence: 15%; Decision Zone UPPER RESISTANCE 98.49-98.70 (M04:514-519)

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | SS | RANGE | 97.80 | 98.50 | Confidence HIGH. 'SS continuation most likely. Free movement within 97.80-98.50 band.' Option cage EUR/USD 1.1700 + 1.1750 = DXY 98.06-98.30. Anchor ceiling 98.49-98.70, floor 97.80-98.00 (M04:524-533) |
| Tue | SS -> Possible WLS | RANGE | 97.82 | 98.62 | Confidence MODERATE. 'Anchor Points: Ceiling: 98.55-98.62 (option wall, 11.6B EUR) / Floor: 97.82 (option wall, 2.3B EUR)' (M04:540-546) |
| Wed | SS | RANGE | - | - | Confidence MODERATE-HIGH. '[NO OTC EXPIRY DATA]'; 'SS continues in the 97.80-98.50 band' unless Tue cleared 98.50-98.55 (M04:549-553). Visualization gives 'Wed: SS/R'. |
| Thu | BS Trigger Window | CONTINGENT | - | - | Confidence MODERATE. 'If GDP misses expectations: SS -> BS (downside) toward 97.50-97.72. ... If GDP/PCE beats expectations: SS -> BS (upside) toward 99.05-99.34.' (M04:556-562) |
| Fri | R or WL | CONTINGENT | - | - | Confidence MODERATE. 'If Thursday produced BS (downside), Friday sees Recovery at 97.50-72 or continued BS toward 96.88-97.00. If ... (upside), Friday sees WL rejection at 99.05-99.34 or continued BS toward 99.49.' (M04:565-568) |

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | type |
|---|---|---|---|---|---|---|---|
| Mon | S | 98.45 (98.45/98.50) | 98.72 | 98.06 | R:R = 0.44:1 to 1.9:1 | 1.44 (range 1.44-2) | Trade Setup A (Primary): 'If DXY rallies to 98.45-98.50 and stalls at SMA 100/200 confluence. SHORT DXY.' |
| Mon | L | 97.85 | 97.65 | 98.30 | 2 | 2.25 | Trade Setup B (Alternative): 'If DXY drops to 97.80-97.90 at London open. LONG DXY.' |
| Thu | S | 98.30 (98.30/98.50) | 98.72 | 97.65 | - | 1.55 (range 1.55-3.86) | Highest-Confidence Trade Setup: 'Thu GDP/PCE miss -> SHORT DXY from 98.30-98.50, stop 98.72, target 97.65' |

#### EURUSD - spot at analysis: 1.1731

Zones: none in this source. Pair section is narrative only - no pair IP zones (M04:600-609).

Key levels: Option Mon CRITICAL (1.13B) 1.1700; Option Mon CRITICAL (1.6B) 1.1750; Option Tue cluster low (11.6B CRITICAL) 1.1635; Option Tue cluster high 1.1650; Option Tue CRITICAL (2.3B) 1.1800; 200-day MA (investinglive) 1.1675

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | SS | RANGE | 1.1700 | 1.1750 | 'Mon: SS pinned between 1.1700-1.1750.' (M04:607) |
| Tue | WLS | RANGE | 1.1635 | 1.1800 | 'Tue: WLS between 1.1635-1.1800.' |
| Wed | R | - | - | - | 'Wed: R from Tue's expiry resolution.' |
| Thu | BS | CONTINGENT | - | - | 'Thu: BS triggered by GDP/PCE (if USD data misses, EU rallies toward 1.1800-1.1850; if beats, EU drops toward 1.1635-1.1675).' (M04:607-609) |
| Fri | WL or R | CONTINGENT | - | - | 'Fri: WL or R depending on Thu's direction.' |

#### GBPUSD - spot at analysis: 1.3590

Zones: none in this source. Narrative only (M04:591-597).

Key levels: Option Tue SIGNIFICANT (604M) 1.3575; Key resistance low (recent highs) 1.3650; Key resistance high 1.3700; Support low (H.10 data support) 1.3480; Support high 1.3500

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon-Fri | SS with upside bias | - | - | - | 'Macro Shape: SS with upside bias. Bailey speech on Thursday is the directional catalyst. If hawkish: BS toward 1.3700+. If dovish: WL rejection at 1.3650, reversal to 1.3480.' (M04:596-597). No per-day decomposition. |

#### AUDUSD - spot at analysis: 0.7206

Zones: none in this source. Narrative only (M04:581-588).

Key levels: Option Mon CRITICAL (A$1.5B) 0.7065; Option Mon (A$725M) 0.7160; Option Mon CRITICAL (A$1.0B) 0.7200; Option Mon (A$810M) 0.7250

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon-Fri | SS early week | - | - | - | 'Macro Shape: SS early week, with Tuesday CPI as the directional trigger. Upside BS toward 0.7250-0.7300 if hot CPI. Downside BS toward 0.7100-0.7065 if soft CPI.' (M04:587-588) |

**Caveats / CONFLICT / UNKNOWN:**

- Stated zone scores do not equal the printed dimension sums for 4 of 6 zones: UPPER RESISTANCE 12/14 vs T2+O2+A2+S2+P1+R1 = 10 (M04:300,304); EQUILIBRIUM 9/14 vs 8 (M04:310,314); KEY SUPPORT BAND 11/14 vs 9 + 1.5 bonus = 10.5 (M04:330,334); BREAKDOWN EXTENSION 5/14 vs 4 (M04:341,345).
- Zones are wide: 0.29 / 0.21 / 0.36 / 0.20 / 0.22 / 0.20 DXY (cf. the later 0.15 clustering cap and the Apr20-24 post-mortem's 'too wide at 0.34').
- Chain confidence: 'PRIMARY CHAIN ... Chain Confidence: 26%' and 'ALTERNATIVE CHAIN ... 15%' (M04:494,514) - far below the 52%/35% of the Apr20/Apr27 reports.
- Mon Setup A prints 'R:R = 0.44:1 to 1.9:1' (M04:535); arithmetic for entry 98.45-98.50 / stop 98.72 / target 98.06 is 1.44 to 2.0.
- MAs are estimates ('~98.10' etc., 'estimated as of May 1, 2026 close') (M04:143-155).
- 'May 8 (Fri) USD Nonfarm Payrolls (if scheduled)' (M04:403) - calendar uncertainty stated by the report itself.
- GU pair text labels a GBP/USD strike '604M EUR' (M04:592) - unit slip.

### 4.7  Week of 2026-05-25 - `Leviathan_DXY_IP_Report_May25-29_2026.pdf`

- **Prompt version:** Leviathan Ultra-Quant v4.5.2 | Engine 3 DISABLED (M25:3)
- **Data as-of:** May 25, 2026 (current as of report generation) - 'Temporal boundary is current time' (M25:7-8); spot = 'Yahoo Finance DX-Y.NYB May 25 close' (M25:10)
- **Generated:** 2026-05-25 23:34 UTC (M25:12) - i.e. AFTER Monday's session; 'FIRST LIVE FORWARD TEST' (M25:15)
- **Oracle grade:** No operator grade found on disk. E1 + E2 only (Engine 3 disabled). Monday's shape is post-hoc (generated after Monday's close); Tue-Fri are genuine forward predictions.

**Data the report used (pillars with real data).** REAL: Protocol A options Mon May 25 + Tue May 26 forward (investinglive, VLM 3-pass) (M25:32-51); Pillar 1 weekly Classic/Fibonacci/Camarilla from H=99.52 L=98.95 C=99.32 + three daily Classic sets (M25:64-80; arithmetic checks out: PP 99.26, R1 99.58, S1 99.01, R2 99.83, S2 98.69); Pillar 2 full 11-MA grid with two clusters (M25:86-110); Pillar 8 K=108.0356 (M25:56-57, 117-126); Pillar 4 forex.com (Matt Simpson), Barchart, OneUpTrader, Cambridge (M25:129-153); Pillar 5 nine swing lows + seven swing highs with wick sizes, repeated magnets, role reversals (M25:155-211); Pillar 6 round/quarter figures + fibs; 4H BoM/MoM overlay, 7 zones (M25:355-367); Protocol F calendar (M25:372-395). NO DATA: Protocols C1/C2/C3 (CME), D (Treasury), E (ON RRP), G (EIA 'Not attempted'), Wed-Fri options, GBP/USD options, Pillar 7 ICE DXY options OI (M25:399-415).

#### DXY - spot at analysis: 99.24

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| #1 Resistance Ceiling | 99.45 | 99.52 | 0.07 | RES | HEAVY | 10 | 25 | POI Tier A. Drivers: P1 Weekly R1, P8 EUR/USD 1.1540 (EUR 1.1bn Tue), P5 Repeated High Magnet (4x), P6 99.50 Round Number (M25:217-221). 4H overlay: BoM Supply 1X(1S) [99.31-99.41] + MoM Supply 0X [99.26-99.... |
| #2 Upper Resistance | 99.15 | 99.25 | 0.10 | RES | MODERATE-HEAVY | 8 | 20 | POI Tier A-. Drivers: P8 EUR/USD 1.1600 (EUR 1.1bn Mon + EUR 3.5bn Tue), P1 Daily PP cluster, P5 Swing Low 99.16, P6 99.25 Quarter (M25:223-227). 4H overlay: MoM Demand 0X [99.14-99.36] DISAGREE = Decision Z... |
| #3 Equilibrium Zone | 98.92 | 99.05 | 0.13 | EQ | MODERATE | 7 | 15 | POI Tier B+. Drivers: P2 MA Cluster (SMA 50=98.94, SMA 10=99.00), P5 Swing Low May 25 (98.92), P1 Daily S1 cluster (M25:229-233). 4H overlay: MoM Demand 1X(1S) [98.98-99.12] AGREE; LSZ 98.92-98.97 ACTIVE SL ... |
| #4 Mid-Range Support | 98.53 | 98.68 | 0.15 | SUP | HEAVY | 9 | 10 | POI Tier A. Drivers: P2 MA Mega-Cluster (5 MAs), P5 Swing Low Apr 08 (98.53), P6 Fib 23.6%, P4 Analyst 98.50 (M25:235-239). 4H overlay: BoM Demand 0X [98.42-98.55] AGREE; Repeated Low Magnet Mar 10 (98.49) +... |
| #5 Key Support Band | 97.96 | 98.16 | 0.20 | SUP | HEAVY | 10 | 8 | POI Tier A+. Drivers: 4H BoM Demand (0X mitigated), P5 Swing Lows cluster, P6 Fib 61.8%, P1 Weekly S2=98.69 nearby (M25:241-245). 4H overlay: BoM Demand 0X [97.96-98.16] 'IMPERVIOUS (AGREE + BoM unmitigated)... |
| #6 Deep Support | 97.63 | 97.82 | 0.19 | SUP | EXTREME | 11 | 5 | POI Tier A+. Drivers: P5 Repeated Low (2x exact 97.63), 4H BoM Demand, P5 Swing Low Apr 17+May 06, Role Reversal (M25:247-249). 'No direct 4H zone'; LSZ 97.63-97.68 + 97.72-97.77; bonus +1.5 (M25:308-319) |

LSZ: 99.47-99.52 (Supply-side, ACTIVE SL TRIGGER); 99.42-99.47 (Supply-side, ACTIVE SL TRIGGER); 99.39-99.44 (Supply-side, ACTIVE SL TRIGGER); 99.04-99.09 (Supply-side, STANDARD); 98.92-98.97 (Demand-side, ACTIVE SL TRIGGER); 98.49-98.54 (Demand-side, STANDARD); 97.63-97.68 (Demand-side, STANDARD)

4H zones: BoM Demand 97.96-98.16 [0X]; BoM Demand 98.42-98.55 [0X]; BoM Supply 99.31-99.41 [1X (1S)]; MoM Demand 98.98-99.12 [1X (1S)]; BoM Supply 99.29-99.47 [1X (1H)]; MoM Demand 99.14-99.36 [0X]; MoM Supply 99.26-99.51 [0X]

Key levels: Prior week (May 18-22) High 99.52; Prior week Low 98.95; Prior week Close 99.32; Classic W R3 100.15; Classic W R2 99.83; Classic W R1 99.58; Classic W PP 99.26; Classic W S1 99.01; Classic W S2 98.69; Classic W S3 98.44; Fibonacci W R3 99.83; Fibonacci W R2 99.62; Fibonacci W R1 99.48; Fibonacci W S1 99.05; Fibonacci W S2 98.91; Fibonacci W S3 98.69; Camarilla W R3 99.48; Camarilla W R2 99.42; Camarilla W R1 99.37; Camarilla W S1 (as printed) 99.27; Camarilla W S2 99.22; Camarilla W S3 99.16; Classic D (May 25) PP 99.09; Classic D (May 25) R1 99.27; Classic D (May 25) R2 99.29; Classic D (May 25) S1 99.07; Classic D (May 25) S2 98.89; Classic D (May 22) PP 99.30; Classic D (May 21) PP 99.26; SMA 200 98.56; SMA 100 98.53; EMA 200 98.61; SMA 50 98.94; EMA 50 98.74; SMA 20 98.64; EMA 20 98.83; SMA 10 99.00; EMA 10 99.01; SMA 9 99.08; EMA 9 99.04; EMA 100 (zone detail) 98.68; EUR/USD 1.1600 -> DXY (EUR 4.6bn aggregate) 99.18; EUR/USD 1.1540 -> DXY 99.48; EUR/USD 1.1650 -> DXY 98.94; Analyst forex.com resistance (May retest target) 99.50; Analyst forex.com support (Fibonacci + wedge) 98.98; Analyst forex.com 52-week MA (~) 98.90; Analyst forex.com resistance (prior structure) 100.16; Analyst forex.com support 98.50; Analyst forex.com deep support 97.35; Swing low May 25 98.92; Swing low May 07 97.82; Swing low May 06 97.63; Swing low May 01 97.72; Swing low Apr 17 97.63; Swing low Apr 16 97.83; Swing low Apr 08 98.53; Swing low Mar 11 98.70; Swing low Mar 10 98.49; Swing high May 21 99.52; Swing high May 20 99.47; Swing high Mar 09 99.70; Swing high Mar 06 99.44; Swing high Mar 03 99.68; Swing high Apr 07 100.16; Swing high Mar 23 100.15; Upside BS target low (3x Repeated High Magnet) 100.12; Upside BS target high 100.16; BS ceiling breakout confirmation 99.55; BS floor breakdown confirmation 98.89

E2 current shape: SWING SCALP (SS); Anchor Zone #2 Upper Resistance (99.15-99.25); MODERATE-HEAVY (8/14); ZFP 20%; 'DXY has been consolidating in a 98.92-99.52 range for the past 5 sessions' (M25:421-431). Primary Timeframe: 1H | Structural Validation: 4H (M25:417).

E2 primary chain: SS -> WL (at ceiling) -> R -> SS -> BS (direction depends on Friday PCE); 'Chain Confidence: 0.50 x 0.65 x 0.65 = ~21% cumulative' (M25:458-459)

E2 alternative chain: SS -> BS (upside breakout through ceiling); 'Sustained break above 99.55 for 15+ min: Upside BS activates. Target: 100.12-100.16 ... Measured move from 99.52 ceiling to 98.92 floor = 0.60 range -> target 99.52 + 0.60 = 100.12' (M25:489-497)

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | SS (consolidation) | RANGE | 98.95 | 99.20 | Confidence HIGH. Asian 'Range-bound between 98.95-99.20'; NY Pre-Cut pinning near 99.18; Post-Cut 'Price likely settles near 99.15-99.25'. Anchor ceiling Zone #1 (99.45-99.52), floor Zone #3 (98.92-99.05) (M25:501-519) |
| Tue | SS -> potential WL at ceiling | UP then REJECT | 99.18 | 99.48 | Confidence MODERATE-HIGH. 'If price was pinned near 99.18: likely Spring Release UP toward 99.43-99.48. ... WL or SS - Key test of 99.47-99.52 ceiling. 4x Repeated High Magnet makes rejection likely' (M25:521-546) |
| Wed | R (recovery) or SS | RANGE | zone 98.92-99.05 | zone 99.15-99.25 | Confidence MODERATE. 'Floor: Zone #3 (98.92-99.05) / Ceiling: Zone #2 (99.15-99.25)'; 'If WL occurred, R is likely. If SS continued, SS persists' (M25:548-562) |
| Thu | SS (building tension before PCE) | RANGE | zone 98.92-99.05 | zone 99.15-99.25 | Confidence MODERATE. Same floor/ceiling as Wed (M25:563-575) |
| Fri | BS (BREAKOUT SURGE) | TRIGGER-DEPENDENT | - | - | Confidence TRIGGER-DEPENDENT. 'Hot PCE -> DXY surges through Zone #1 ceiling (99.52) toward 100.12-100.16'; 'Cool PCE -> DXY breaks through Zone #3 floor (98.92) toward Zone #4 (98.53-98.68)'; 'BS ceiling: 99.55 (breakout confi... |

E3 setups: none. ENGINE 3 DISABLED - No trade setups in this report (M25:24)

**Caveats / CONFLICT / UNKNOWN:**

- Generated after the Monday close: the Monday low 98.92 is already used as a structural anchor / LSZ (M25:158, 277, 340).
- Zone #2 'Upper Resistance' 99.15-99.25 contains spot 99.24 and its 4H overlay is a DEMAND zone: 'MoM Demand 0X [99.14-99.36] - DISAGREE (IP supply, 4H demand) = Decision Zone' (M25:264).
- Zone #5 key driver 'P1 Weekly S2=98.69 nearby' (M25:243-245) - 98.69 is 0.53 above the zone top 98.16; zone #5's fib 'Fib 61.8% = 98.35 (near zone top)' is 0.19 above it (M25:304).
- Camarilla W row prints PP 99.26 with S1 99.27 (S1 above PP) (M25:71).
- Supply-side LSZ convention differs from the Apr20-24 report: here [high-0.05, high] (99.47-99.52 for the May 21 high 99.52; 99.42-99.47 for 99.47; 99.39-99.44 for 99.44; 99.04-99.09 for 99.09) (M25:326-337); Apr20-24 used [high, high+0.05] (98.29-98.34 for high 98.29; 99.18-99.23 for 99.18) (A20:200-206). Demand-side is [low, low+0.05] in both.
- Chain confidence '0.50 x 0.65 x 0.65 = ~21% cumulative - drops below 25% at R step' (M25:459).
- CONFLICT with the v5.3.3 W22 report of the same week: see week entry 'Trident_Report_2026W22_May25-29_v5.pdf' -> cross_report_conflicts.

### 4.8  Week of 2026-05-25 - `Trident_Report_2026W22_May25-29_v5.pdf`

- **Prompt version:** Trident Trading Engine v5.3.3 | Full-Spectrum Architecture (W22:4). File name says '_v5'. THE ONLY v5.3.3-labelled report on disk.
- **Data as-of:** May 27, 2026 06:00 GMT - 'Temporal boundary is current time' (W22:8-9)
- **Generated:** May 27, 2026 06:00 UTC (W22:12) - WEDNESDAY morning of the target week. Mon/Tue are already 'Settled' (W22:87, 98).
- **Oracle grade:** No operator grade found on disk. Mid-week report: Mon/Tue shapes and the Mon/Tue calendar setups are RETROSPECTIVE (built from the realised Mon/Tue ranges, W22:539-543), only Wed-Fri are forward. The DXY numeric layer fails basic arithmetic/cross-checks (see caveats) -> use with extreme caution as an E1 oracle.

**Data the report used (pillars with real data).** As printed: Protocol A 'CME/Barchart option positioning, investingLive pre-market data' with corrupt DXY equivalents (W22:53-107); Pillar 1 weekly Classic/Fibonacci/Camarilla + one daily set (internally inconsistent) (W22:111-125); Pillar 2 nine MAs (conflict with M25) (W22:130-154); Pillar 4 four one-line entries (Barchart 98.90, forex.com EUR/USD 1.1650, investingLive AUD/USD 0.7180, Yahoo 99.09) (W22:159-167); Pillar 5 four swing lows + three swing highs with wick sizes in 'ticks' (W22:169-197); Pillar 8 table = the corrupt equivalents (W22:200-208); 4H BoM/MoM table (W22:340-358). Pair layers: Yahoo Finance OHLC + Barchart 20d/50d SMA/EMA; 'NO mathematical conversion of DXY prices to pair prices' (W22:1332-1333). NOT PRESENT: Pillar 3 component conversion audit, Pillar 6 fib grid, Pillar 7, Pillar 9 regime table, Treasury/ON RRP/EIA protocols, LSZ wick audit.

#### DXY - spot at analysis: 99.09

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| #1 Ceiling | 99.45 | 99.52 | 0.07 | RES | EXTREME | 12 | 15 | POI Tier A+. Drivers: 'May 21 high, triple-tested' (W22:215). 4H: BoM Supply - origin of May 21 rejection from 99.52. Stops cluster above 99.55. '3 reactions (May 15, May 20, May 21) - ACTIVE but DEPLETING. ... |
| #2 Resistance | 99.25 | 99.30 | 0.05 | RES | HEAVY | 10 | 25 | POI Tier A. Drivers: 'Pivot R1 + SMA 20 cluster' (W22:217). 4H: MoM zone formed during May 20 push. 'MoM zone - LIKELY TO BE PIERCED in bullish continuation. TP for shorts, NOT entry for shorts. ENTRY for lo... |
| #3 Equilibrium | 98.95 | 99.10 | 0.15 | EQ | MODERATE | 7 | 15 | POI Tier B+. Drivers: 'Current zone, Mon close area' (W22:219). 'Neutral zone - not a primary entry or TP.' Reaction count N/A (W22:257-268). Spot 99.09 inside. |
| #4 Mid Support | 98.90 | 98.97 | 0.07 | SUP | HEAVY | 9 | 10 | POI Tier A. Drivers: 'Double-tested support (May 19+22)' (W22:221). 4H: BoM Demand - origin of May 22 bounce from 98.90. 'BoM zone - PRIMARY ENTRY for longs on pullback.' '2 reactions (May 19, May 22) - ACTI... |
| #5 Key Support | 98.50 | 98.68 | 0.18 | SUP | HEAVY | 10 | 8 | POI Tier A+. Drivers: '5-MA mega-cluster zone' (W22:223). 4H: BoM Demand. '1 reaction (May 15 bounce from 98.50) - ACTIVE. 2nd retest = swing entry valid.' (W22:289-300) |
| #6 Deep Support | 97.80 | 98.16 | 0.36 | SUP | EXTREME | 11 | 5 | POI Tier A+. Drivers: 'Structural floor, BoM demand' (W22:225). SMA 200 (97.80) at zone bottom, EMA 200 (98.16) at zone top. '0 reactions in current cycle - VIRGIN.' (W22:305-316) |

LSZ: 99.52-99.55 (Supply-side, ACTIVE SL TRIGGER); 99.25-99.30 (Demand-side, STANDARD); 98.90-98.97 (Demand-side, ACTIVE SL TRIGGER); 98.50-98.68 (Demand-side, STANDARD)

4H zones: BoM Supply 99.45-99.52 [Unmitigated]; MoM Supply 99.25-99.30 [Unmitigated]; BoM Demand 98.90-98.97 [Unmitigated]; MoM Demand 99.05-99.15 [Unmitigated]; BoM Demand 98.50-98.68 [Unmitigated]; MoM Supply 99.55-99.65 [Unmitigated]

Key levels: Prior week (May 18-22) High 99.52; Prior week Low (CONFLICT with M25 98.95) 98.90; Prior week Close (CONFLICT with M25 99.32) 99.09; Classic W R3 (as printed) 100.29; Classic W R2 (as printed) 99.90; Classic W R1 (as printed; formula gives 99.44) 99.71; Classic W PP 99.17; Classic W S1 (as printed) 98.63; Classic W S2 (as printed) 98.44; Classic W S3 (as printed) 98.05; Fibonacci W R1 (as printed) 99.69; Fibonacci W S1 (as printed) 98.65; Camarilla W R3 99.34; Camarilla W R2 99.26; Camarilla W R1 99.17; Camarilla W S1 99.00; Camarilla W S2 98.92; Camarilla W S3 98.83; Classic D (May 22) R2 99.41; Classic D (May 22) R1 99.25; Classic D (May 22) PP 99.09; Classic D (May 22) S1 98.93; Classic D (May 22) S2 98.77; SMA 200 (as printed) 97.80; SMA 100 98.50; EMA 200 98.16; SMA 50 98.90; EMA 50 98.97; SMA 20 99.25; EMA 20 99.30; SMA 10 99.35; EMA 9 99.38; Ceiling Break trigger 99.52; Double Bottom Break trigger 98.90; Pivot PP Support 99.17

E2 current shape: SS (Swing Scalps) - Consolidating within 98.90-99.52 range. 5+ sessions of ranging. Prior Shape: R (Recovery). ZFP at 99.52: 15%. (W22:420-429). 4H Storyline Bias: CONSOLIDATION (neutral-bearish tilt) (W22:414)

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | SS | RANGE | 98.92 | 99.11 | 'Option cage + no catalyst. Range 98.92-99.11.' Key transition time 'All session' (W22:451-452) [RETROSPECTIVE: Monday already settled] |
| Tue | SS | RANGE | 98.90 | 99.25 | 'Compressed 98.90-99.25. Recovery from Mon low.' London 07:00-09:00 (W22:454-455) [RETROSPECTIVE] |
| Wed | SS/WL | - | - | - | 'EUR options mega-day + Australia CPI. Tension building.' NY 12:00+ (W22:457-458) |
| Thu | BS directional | TRIGGER-DEPENDENT | - | - | 'RED FOLDER: PCE+GDP+Durable Goods. PRIMARY CATALYST.' NY 12:30+ (after 30-min deferral) (W22:460-461). 'Hot PCE = BS through 99.52 toward 100.00. Cool PCE = DWL through 98.90 toward 98.50.' (W22:470-471) |
| Fri | R/SS | - | - | - | 'PCE aftermath + CME option expiry. Resolution.' (W22:463) |

E3 setups: none. NO DXY trade setups: the Weekly Execution Calendar lists only GBP/USD, AUD/USD, EUR/USD rows (W22:503-535). DXY is the 'Master' compass.

#### EURUSD - spot at analysis: 1.1648

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| #1 Ceiling | 1.1680 | 1.1700 | 0.0020 | RES | HEAVY | 10 | 25 | POI Tier A. E3 Status TP-TARGET. Drivers: 20-day SMA resistance zone (W22:1146) |
| #2 Resistance | 1.1640 | 1.1660 | 0.0020 | RES | MODERATE-HEAVY | 8 | 20 | POI Tier A-. E3 Status ENTRY-COND. Drivers: 50-day SMA/EMA resistance. Spot 1.1648 inside. (W22:1148) |
| #3 Equilibrium | 1.1610 | 1.1635 | 0.0025 | EQ | MODERATE | 7 | 15 | POI Tier B+. E3 Status ENTRY-COND. Drivers: Current zone area (W22:1150) |
| #4 Mid Support | 1.1570 | 1.1590 | 0.0020 | SUP | HEAVY | 9 | 10 | POI Tier A. E3 Status ENTRY-PRIMARY. Drivers: BoM demand zone (W22:1152) |
| #5 Key Support | 1.1540 | 1.1560 | 0.0020 | SUP | HEAVY | 10 | 8 | POI Tier A+. E3 Status ENTRY-PRIMARY. Drivers: Structural demand (W22:1154) |
| #6 Deep Support | 1.1470 | 1.1500 | 0.0030 | SUP | EXTREME | 11 | 5 | POI Tier A+. E3 Status ENTRY-PRIMARY. Drivers: Structural floor + option wall (W22:1156) |

Key levels: 20-day SMA 1.1687; 50-day SMA 1.1661; 50-day EMA 1.1666; Mon-Tue consolidation low 1.1617; Mon-Tue consolidation high 1.1655; Nearest LSZ (demand) 1.1590; Option Wed/Thu SIGNIFICANT MAGNET 1.1650; Option SIGNIFICANT MAGNET 1.1500

E2 primary chain: SS -> SS -> SS/WL -> BS -> BS/R (W22:1184)

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | SS | RANGE | - | - | 'Range 30 pips. Below all MAs. Range too tight for 3:1 scalps.' ZFP ceiling 18% / floor 15%; SS cont. 80% (W22:1171) |
| Tue | SS | RANGE | - | - | 'Range 23 pips. Grinding up but below all MAs.' 16% / 18%; SS 75%, BS 15% (W22:1173) |
| Wed | SS/WL | - | - | - | 'EUR options mega-day creates tension. Massive walls above at 1.1740-50.' 15% / 22%; SS 55%, WL 30% (W22:1175-1176) |
| Thu | BS dir. | DOWN if hot PCE | - | 1.1555 | 'PCE + option expiries amplify. Hot PCE = EUR drop toward 1.1555.' 12% / 28%; BS 70%, WL 15% (W22:1178-1179) |
| Fri | BS/R | - | - | - | 'Fri option expiries at 1.1500 = floor protection.' 18% / 20%; BS 45%, R 35% (W22:1181) |

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | type |
|---|---|---|---|---|---|---|---|
| Wed | S | 1.1655 | 1.1680 | 1.1600 | 2.2 | 2.2 | Breakout Search - NY Mid 10:00-14:00 ET, shape SS/WL |
| Thu | S | 1.1660 | 1.1695 | 1.1630 / 1.1590 / 1.1555 | 3 | 0.86 **MISMATCH** | HTF Swing #3 / EU HTF Swing #1 - NY Open 08:30 ET, shape BS; '1st retest of Zone #2 Upper Resistance' |
| Fri | S | 1.1620 | 1.1640 | 1.1580 | 2 | 2 | Swing Scalp - London 02:00-05:00 ET, shape R/SS |
| Thu | S | 1.1600 | 1.1580 | - | - | - | Reinforcement LR #1 (Liquidity): trigger 1.1620 (Zone #3) |
| Thu | S | 1.1570 | 1.1555 | - | - | - | Reinforcement FR #2 (Fibonacci): trigger 1.1590 (Fib 1.618) |

#### GBPUSD - spot at analysis: 1.3445

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| #1 Ceiling | 1.3495 | 1.3508 | 0.0013 | RES | HEAVY | 10 | 25 | POI Tier A. E3 Status TP-TARGET. Drivers: Triple-rejection ceiling, 3 tests (W22:993) |
| #2 Resistance | 1.3450 | 1.3460 | 0.0010 | RES | MODERATE-HEAVY | 8 | 20 | POI Tier A-. E3 Status ENTRY-COND. Drivers: Supply zone above equilibrium (W22:995) |
| #3 Equilibrium | 1.3430 | 1.3445 | 0.0015 | EQ | MODERATE | 7 | 15 | POI Tier B+. E3 Status ENTRY-COND. Drivers: Current zone, 50-day SMA (W22:997) |
| #4 Mid Support | 1.3380 | 1.3400 | 0.0020 | SUP | HEAVY | 9 | 10 | POI Tier A. E3 Status ENTRY-PRIMARY. Drivers: 200-day EMA, BoM demand (W22:999) |
| #5 Key Support | 1.3340 | 1.3370 | 0.0030 | SUP | HEAVY | 10 | 8 | POI Tier A+. E3 Status ENTRY-PRIMARY. Drivers: Structural demand zone (W22:1001) |
| #6 Deep Support | 1.3280 | 1.3310 | 0.0030 | SUP | EXTREME | 11 | 5 | POI Tier A+. E3 Status ENTRY-PRIMARY. Drivers: Structural floor, BoM demand (W22:1003) |

Key levels: 20-day SMA 1.3500; 50-day SMA 1.3441; 50-day EMA 1.3453; Mon-Tue consolidation low 1.3436; Mon-Tue consolidation high 1.3497; Nearest LSZ (Mon low, demand) 1.3436

E2 primary chain: SS -> SS -> SS/DWL -> BS -> R/SS (W22:1033)

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | SS | RANGE | 1.3436 | 1.3497 | 'Big range 61 pips. Failed 1.3500 ceiling. BOTH directions valid.' ZFP ceiling 22% / floor 12%; SS cont. 75% (W22:1019) [RETROSPECTIVE] |
| Tue | SS | RANGE | - | - | 'Compressed to 16 pips. Classic pre-breakout squeeze.' 20% / 15%; SS 65%, BS soon 25% (W22:1021-1022) [RETROSPECTIVE] |
| Wed | SS/DWL | - | - | - | 'Compression after failed ceiling. DWL risk if 1.3500 tested 3rd time.' 18% / 18%; SS 55%, DWL 30% (W22:1024-1025) |
| Thu | BS dir. | TRIGGER-DEPENDENT | - | - | 'PCE catalyst. Cool PCE = GBP rallies. Hot PCE = GBP drops to 200d EMA.' 15% / 22%; BS 65%, WL 20% (W22:1027-1028) |
| Fri | R/SS | - | - | - | 'Resolution day. Fri option expiries.' 20% / 18%; R 50%, SS 35% (W22:1030) |

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | type |
|---|---|---|---|---|---|---|---|
| Mon | S | 1.3495 | 1.3510 | 1.3440 | 3.7 | 3.67 | Swing Scalp #1 - London 02:00-05:00 ET, shape SS |
| Mon | L | 1.3440 | 1.3425 | 1.3495 | 3.7 | 3.67 | Swing Scalp #2 - London 05:00-08:00 ET, shape SS |
| Wed | S | 1.3490 | 1.3508 | 1.3445 | 2.8 | 2.5 **MISMATCH** | Swing Scalp - London 02:00-05:00 ET, shape SS/WL; 'above 3rd test of 1.3500' |
| Thu | L | 1.3380 | 1.3345 | 1.3445 / 1.3495 / 1.3550 | 3 | 1.86 **MISMATCH** | HTF Swing #2 / GU HTF Swing #1 - NY Mid 10:00-14:00 ET, shape BS; '2nd retest of BoM Demand at Zone #4, 200-day EMA s... |
| Thu | L | 1.3420 | 1.3400 | - | - | - | Reinforcement LR #1 (Liquidity): trigger 1.3455 (Zone #2) |
| Thu | L | 1.3440 | 1.3425 | - | - | - | Reinforcement FLR #2 (Fib-Liq): trigger 1.3480 (Fib 2.382) |

#### AUDUSD - spot at analysis: 0.7141

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| #1 Ceiling | 0.7270 | 0.7280 | 0.0010 | RES | HEAVY | 10 | 25 | POI Tier A. E3 Status TP-TARGET. Drivers: 20-day SMA resistance zone [NB: 20-day SMA is printed as 0.7186 at W22:909] (W22:890) |
| #2 Resistance | 0.7180 | 0.7186 | 0.0006 | RES | MODERATE-HEAVY | 8 | 20 | POI Tier A-. E3 Status TP-TARGET. Drivers: Tue high + supply ceiling (W22:892-893) |
| #3 Equilibrium | 0.7130 | 0.7155 | 0.0025 | EQ | MODERATE | 7 | 15 | POI Tier B+. E3 Status ENTRY-COND. Drivers: Current zone, 50-day EMA support (W22:895-896) |
| #4 Mid Support | 0.7090 | 0.7110 | 0.0020 | SUP | HEAVY | 9 | 10 | POI Tier A. E3 Status ENTRY-PRIMARY. Drivers: 50-day SMA + BoM demand (W22:898-899) |
| #5 Key Support | 0.7020 | 0.7050 | 0.0030 | SUP | HEAVY | 10 | 8 | POI Tier A+. E3 Status ENTRY-PRIMARY. Drivers: Structural demand zone (W22:901-902) |
| #6 Deep Support | 0.6940 | 0.6970 | 0.0030 | SUP | EXTREME | 11 | 5 | POI Tier A+. E3 Status ENTRY-PRIMARY. Drivers: Structural floor, BoM demand (W22:904-905) |

Key levels: 20-day SMA 0.7186; 50-day SMA 0.7100; Mon-Tue consolidation low 0.7138; Mon-Tue consolidation high 0.7182; Nearest LSZ (Tue low, demand) 0.7138

E2 primary chain: SS -> SS -> SS/BS(dn) -> BS -> R/SS (W22:933)

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | SS | RANGE | - | - | 'Tested ceiling 0.7176, closed near high. Range 19 pips = too narrow for 3:1 RRR' ZFP ceiling 20% / floor 12%; SS cont. 80% (W22:919-920) [RETROSPECTIVE] |
| Tue | SS | RANGE | 0.7138 | 0.7182 | 'Expanded range 44 pips. Selling pressure dominant - closed near low 0.7141' 18% / 15%; SS 70%, BS risk 20% (W22:922-923) [RETROSPECTIVE] |
| Wed | SS/BS dn | DOWN risk | - | - | 'Australia CPI catalyst. Cool CPI = AUD weakness. Below 20d SMA pressure' 15% / 20%; SS 55%, BS 35% (W22:925-926) |
| Thu | BS dir. | TRIGGER-DEPENDENT | - | - | 'PCE impact on USD. If hot PCE + cool CPI = strong AUD sell-off' 12% / 25%; BS 65%, WL 20% (W22:928) |
| Fri | R/SS | - | - | - | 'Resolution + CME option expiry' 18% / 18%; R 45%, SS 40% (W22:930) |

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | type |
|---|---|---|---|---|---|---|---|
| Tue | S | 0.7178 | 0.7192 | 0.7142 | 3.2 | 2.57 **MISMATCH** | Swing Scalp #1 - London 02:00-05:00 ET, shape SS |
| Tue | L | 0.7142 | 0.7128 | 0.7178 | 3.2 | 2.57 **MISMATCH** | Swing Scalp #2 - London 05:00-08:00 ET, shape SS; 'below 15m BoM demand' |
| Wed | L | 0.7135 | 0.7120 | 0.7180 | 3.2 | 3 | Swing Scalp - London 05:00-08:00 ET, shape SS |
| Thu | L | 0.7100 | 0.7075 | 0.7155 / 0.7180 / 0.7270 | 3.6 | 2.2 **MISMATCH** | HTF Swing #1 - NY Mid 10:00-14:00 ET, shape BS; '2nd retest of BoM Demand at Zone #4, 50-day SMA support' |
| Fri | L | 0.7130 | 0.7115 | 0.7180 | 3.6 | 3.33 **MISMATCH** | Reinforcement - NY Open 08:30 ET, shape R/SS; 'LR at Zone #3 if Thu HTF swing confirmed' |
| Thu | L | 0.7160 | 0.7145 | - | - | - | Reinforcement FR #2 (Fibonacci): trigger 0.7180 (Fib 1.382) |

**Conflicts between this report and `Leviathan_DXY_IP_Report_May25-29_2026.pdf` (same week):**

| field | this report (W22) | Leviathan (M25) | note |
|---|---|---|---|
| Prior-week (May 18-22) DXY H/L/C | H=99.52 L=98.90 C=99.09 (W22:111) | H=99.52 L=98.95 C=99.32 (M25:64) | Trident_Engine3_v6_Verification_May18-22.md 'DXY Actuals': Mon low 98.95, Fri close ~99.20, 'Weekly High: ~99.52 / Weekly Low: ~98.95' (V6V:9-17). W22's C=99.09 equals its own May 27 spot. |
| SMA 200 / SMA 100 / SMA 50 / SMA 20 | 97.80 / 98.50 / 98.90 / 99.25 (W22:132-142) | 98.56 / 98.53 / 98.94 / 98.64 (M25:86-96) |  |
| Mon May 25 EUR/USD expiries | 1.1500 EUR 1.1 bn; 1.1600 EUR 870 mn (W22:92-94) | 1.1600 EUR 1.1bn only (M25:40) |  |
| Tue May 26 EUR/USD expiries | 1.1550 EUR 950 mn (+ GBP/USD 1.3450 GBP 720 mn) (W22:103-105) | 1.1540 EUR 1.1bn; 1.1600 EUR 3.5bn; 1.1650 EUR 1.18bn (M25:47-51) |  |
| Recent swing highs/lows | lows May 22 98.90, May 19 98.92, May 15 98.50, May 8 98.16; highs May 21 99.52, May 20 99.41, May 15 99.30 (W22:173-190) | lows May 25 98.92, May 07 97.82, May 06 97.63 ...; highs May 21 99.52, May 20 99.47 (M25:158-191) |  |
| Core PCE day | Thu May 28 12:30 GMT 'Core PCE QoQ' + GDP 2nd est. (W22:375-377) | Friday May 29 8:30 AM 'PCE Price Index (Apr)' (M25:384-386) |  |
| DXY zones (same week, same engine family) | #1 99.45-99.52 EXTREME 12/14 15% / #2 99.25-99.30 HEAVY 10/14 25% / #3 98.95-99.10 MOD 7/14 15% / #4 98.90-98.97 HEAVY 9/14 10% / #5 98.50-98.68 HEAVY 10/14 8% / #6 97.80-98.16 EXTREME 11/14 5% | #1 99.45-99.52 HEAVY 10/14 25% / #2 99.15-99.25 MOD-HEAVY 8/14 20% / #3 98.92-99.05 MOD 7/14 15% / #4 98.53-98.68 HEAVY 9/14 10% / #5 97.96-98.16 HEAVY 10/14 8% / #6 97.63-97.82 EXTREME 11/14 5% | Only zone #1's range is identical. The Score/ZFP/POI-tier columns of zones #3-#6 are IDENTICAL across the two reports (7/15/B+, 9/10/A, 10/8/A+, 11/5/A+) although the ranges differ, and the same six-row Score/ZFP/tier template (10/25/A, 8/20/A-, 7/15/B+, 9/10/A, 10/8/A+, 11/5/A+) is reused verbatim for AUD/USD, GBP/USD and EUR/USD in W22 (W22:890-904, 993-1003, 1146-1156) -> scores/ZFPs in W22 look templated, not computed. |

**Caveats / CONFLICT / UNKNOWN:**

- K FACTOR CORRUPT: 'K Factor Audit: K=6.35 | USDJPY=149.50 GBPUSD=1.3445 USDCAD=1.3650 USDSEK=10.82 USDCHF=0.7950 | Confidence band: +/-0.25 DXY' (W22:71-72). The Leviathan report for the same week prints 'K=108.0356 | USDJPY=158.87 GBPUSD=1.3503 USDCAD=1.3801 USDSEK=9.2785 USDCHF=0.7825 | +/-0.07' (M25:56-57).
- DXY EQUIVALENTS CORRUPT: 'EUR/USD 1.1650 ... DXY Equiv. 108.04' (W22:64, 81, 204, 208), '1.1500 -> 99.87' (W22:66), '1.1600 -> 101.36' (W22:94), '1.1550 -> 100.10' (W22:103), 'AUD/USD 0.7150 -> 99.40' (W22:68). Leviathan: 1.1600 -> 99.18, 1.1650 -> 98.94, 1.1540 -> 99.48 (M25:40-51). The volatility table even lists 'EUR/USD 1.1650 Expiry | 108.04 DXY' (W22:485).
- WEEKDAY LABELS WRONG in Section 1: 'Wednesday, May 28' (W22:59) and 'Thursday, May 29' (W22:75); the calendar section has 'Wed May 27 / Thu May 28 / Fri May 29' (W22:371-383). May 27, 2026 is the Wednesday (the report's own generation day).
- PIVOTS INCONSISTENT: from H=99.52 L=98.90 C=99.09, PP=99.17 is right but Classic R1 is printed 99.71 while the audit line computes 'R1=2xPP-L=2x99.17-98.90=99.44 (adjusted to 99.71 on weekly variant)' (W22:115, 124-125). Classic S1 printed 98.63 (formula 98.82), R2 printed 99.90 (formula PP+(H-L)=99.79).
- MA TABLE INCONSISTENT: 'SMA 20 99.25 | Below (-0.16)', 'EMA 20 99.30 Below (-0.21)', 'SMA 10 99.35', 'EMA 9 99.38' are all ABOVE spot 99.09 yet labelled 'Below' and described as 'MA support' (W22:142-152). 'CLUSTER 1: 98.90-99.38 (5 MAs: ...)' lists six MAs (W22:151).
- FILTER SELF-CONTRADICTION: 'EUR/USD 1.1600 EUR 870 mn ... EXCLUDED (<$850M)' (W22:94) - 870mn is above 850M; compliance sweep says 'Notional Filter PASS - No strikes below $850M in summary tables' (W22:1324) while three sub-850M rows are printed (W22:68, 83, 105).
- Zones #3 (98.95-99.10) and #4 (98.90-98.97) OVERLAP by 0.02 (W22:219-221). Zone #5 4H overlay text: '5-MA mega-cluster (SMA 100 at 98.50, EMA 200 at 98.16)' (W22:290) - EMA 200 at 98.16 is outside zone #5 (98.50-98.68).
- Reaction counts disagree: header 'May 21 high, triple-tested' / '3 reactions (May 15, May 20, May 21)' (W22:215, 239) but the swing-high table gives May 15 high = 99.30 and May 20 high = 99.41, neither inside 99.45-99.52 (W22:186-190).
- ZFP narrative conflict: Zone #1 ZFP 15% (W22:215, 426) vs 'ZFP on ceiling falling (25%>22%>20%). Breakout risk rising.' (W22:469).
- Thursday timing conflict: 'All Thursday setups DEFERRED until 13:00 GMT' / 'HTF Swing setups only after 9:00 AM ET' (W22:386-387, 546-547) vs calendar row 'Thu EUR/USD SHORT HTF Swing ... NY Open 08:30 ET' (W22:531).
- RRR arithmetic: many stated RRRs do not equal |TP-entry|/|entry-SL| (see rrr_arith_ok=false), e.g. EU HTF 'RRR (TP1) 3.0x (35 pips risk / 30 pips reward)' (W22:632) = 0.86; GU HTF 3.0x (35 risk / 65 reward) (W22:602) = 1.86; AU HTF 3.6x (25 / 55) (W22:568) = 2.2.
- 'Missing Data Log ... N/A - Data fully populated' (W22:395) while GBP/USD options 'NO DATA FOUND', CME OI 'INACCESSIBLE', DXY London tick data 'INACCESSIBLE' (W22:404-411).

### 4.9  Week of 2026-07-06 - `trident_e3_validator_FINAL.py (GOLDEN_DXY_TRADES etc.) + TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md`

- **Prompt version:** operator's own manual trades ('The 8 golden DXY trades (operator's July 6-10 2026 levels)', VAL:201), encoded as the E3 oracle of the corrected v5.3.3 E3 engine
- **Data as-of:** week July 6-10, 2026 ('evalWeek ... "2026-07-06->10"', E3C:1654)
- **Generated:** validator dated 2026-09-24 (VAL:38)
- **Oracle grade:** OPERATOR GROUND TRUTH for E3 (entries/SL/TP) on the 'golden week' used by ruling R-15. NO weekly LLM report for this week exists in /home/user/handover-branch: no E1 pressure-zone table and no E2 day chain from a report. The 'PLUTUS_GOLDEN_CASCADE_23.md' and 'Golden_Operator_Trade_Feedback_EU_GU.md' documents cited by the fixture are NOT present anywhere under /home/user.

**Data the report used (pillars with real data).** Operator chart work, not a pillar harvest. Bars for the week: fixtures/bars/2026-07-06.validated-harvest.json (TradingView via tvDatafeed, fetched 2026-09-24; DXY=TVC, EUR/USD=ICE, GBP/USD=OANDA; 15m/30m/1H/4H; every bar t <= anchor 2026-07-06T06:00:00Z).

#### DXY - spot at analysis: -

Zones: none in this source. No E1 pressure zones for this week from any report. Operator level sets below are LQZ/BoM/MoM execution levels, not E1 IP zones.

Key levels: GOLDEN_DXY_LQZ_LEVELS (the LMV oracle) 100.845, 100.945, 100.975, 101.14, 101.19, 101.235, 101.24; GOLDEN_DXY_BOM_LEVELS '1H demand' 100.68; GOLDEN_DXY_BOM_LEVELS '4H supply' 101.33; GOLDEN_DXY_MOM_LEVELS (1H) 100.845; Documented print: DXY Monday high at 10:00Z 101.145; Documented print: DXY Monday low 100.838; Monday band bottom (rejected entry, RRR 1.79) 101.027; Monday defEdge (rejected) 101.092; Wed shelf ceiling 100.972; Mon shelf center 100.949

E2 chain: none. No E2 chain in the oracle source. Shape tags carried by the golden trades (NOT a day chain): Mon SS + BS, Tue SS, Wed SS + RWL + BS, Thu Ladder, Fri WL+RWL (VAL:203-210).

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | type |
|---|---|---|---|---|---|---|---|
| Monday | L | 100.945 | 100.905 | 101.115 | 4.25 | 4.25 | SS Long @ 1H LQZ |
| Monday | S | 101.14 | 101.20 | 100.845 | 4.92 | 4.92 | BS Short @ 1H LQZ |
| Tuesday | L | 100.845 | 100.77 | 101.19 | 4.6 | 4.6 | SS Long @ 1H MoM |
| Wednesday | S | 101.19 | 101.25 | 100.975 | 3.58 | 3.58 | SS Short @ 1H LQZ |
| Wednesday | L | 100.975 | 100.905 | 101.24 | 3.79 | 3.79 | RWL Long @ 1H LQZ |
| Wednesday | S | 101.235 | 101.33 | 100.68 | 5.84 | 5.84 | BS Short @ 4H BoM |
| Thursday | S | - | - | - | - | - | Ladder Short @ 1H LQZ |
| Friday | - | - | - | - | - | - | WL+RWL @ 1H LQZ |

#### EURUSD - spot at analysis: -

Zones: none in this source. 

Key levels: GOLDEN_EU_AXIS (Tier B - operator's drawn levels) 1.14649, 1.14578, 1.14544, 1.14505, 1.14442, 1.14441, 1.14408, 1.14353, 1.14325, 1.14322, 1.14277, 1.14276, 1.1425, 1.14233, 1.14205, 1.14183, 1.1415, 1.14106, 1.14103, 1.14039, 1.14012, 1.14004, 1.13964, 1.13953, 1.1395, 1.1390, 1.13868, 1.1385; Documented print: EU Monday low 1.14083; Documented print: EU Tuesday low 1.14001

| day | dir | entry | SL | TP | stated RRR | arithmetic RRR | type |
|---|---|---|---|---|---|---|---|
| Wed | L | 1.1402 | - | - | - | - | '#4 EU Wed RWL LONG E 1.14020 = rung-1.14010 ceiling' (entry only) |
| Wed | L | 1.13935 | - | - | - | - | '#6 EU Wed deep-demand E 1.13935 = deep shield' (entry only; direction implied by 'deep-demand') |

#### GBPUSD - spot at analysis: -

Zones: none in this source. 

Key levels: GOLDEN_GU_AXIS (Tier B) 1.34587, 1.34485, 1.34481, 1.3436, 1.34246, 1.34244, 1.3410, 1.34075, 1.34021, 1.33941, 1.33934, 1.33882, 1.33839, 1.33829, 1.3375, 1.33629, 1.3360, 1.33522, 1.33347, 1.33331, 1.3333, 1.33224, 1.33199; Documented print: GU week low 1.33222

E3 setups: none. No GU golden trades with levels found. UNKNOWN.

**Caveats / CONFLICT / UNKNOWN:**

- Only 6 of the 8 golden DXY trades carry levels; Thursday 'Ladder Short' and Friday 'WL+RWL' are entry/sl/tp = None (VAL:209-210).
- All 6 priced trades are arithmetically consistent with their stated RRR (see rrr_arith_ok).
- EU/GU 'axis labels (Tier B - operator's drawn levels)' are bare price lists without direction/day (VAL:218-232).
- Matching tolerance in the validator: 'GOLDEN_LEVEL_TOLERANCE_PIPS = 3  # 3-pip count; precision is the ONLY metric' (VAL:235).

### 4.10  Week of 2026-07-06 - `handover-branch/data/e1/DXY-2026-07-06.json, data/e1/EURUSD-2026-07-06.json, data/e2/DXY-2026-07-06-e2.json, data/e2/EURUSD-2026-07-06-e2.json`

- **Prompt version:** NOT A REPORT - output of the previous agent's mechanical E1/E2 Python tool (schema 'trident-e1/1')
- **Data as-of:** DXY file data_as_of '2026-10-07'; EURUSD file '2026-10-05'; temporal_boundary_utc is the empty string in both
- **Generated:** 2026-10 (previous build)
- **Oracle grade:** NOT AN ORACLE. Included only because the task asked for every zone data set found for this week. Not report-derived, not operator-approved; web harvest was DOWN ('web_harvest': {'status': 'DOWN', 'label': '[NO DATA]'}), so no options/analyst pillars.

**Data the report used (pillars with real data).** Pillar 1 pivots (12 sets from weekly H=101.595 L=100.558 C=100.878) and Pillar 2 MA grid (12 MAs) from the local 1H fixture only; web harvest DOWN.

#### DXY - spot at analysis: 100.872

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| IP Resistance Ceiling | 101.605 | 101.605 | 0.00 | RES | MODERATE | 6 | 37 | tool zone; zone_type SOFT_WALL; ladder_name MODE_SUPPLY_101.60; 1 level |
| Upper IP Resistance | 101.397 | 101.453 | 0.055 | RES | MODERATE-HEAVY | 8 | 27 | tool zone; STANDARD_WALL; MODE_SUPPLY_101.45; 7 levels |
| Equilibrium Zone | 101.163 | 101.213 | 0.05 | EQ | MODERATE-HEAVY | 9 | 27 | tool zone; STANDARD_WALL; MODE_SUPPLY_101.21; 6 levels |
| Mid-Range Support | 100.893 | 101.01 | 0.117 | SUP | MODERATE | 7 | 37 | tool zone; SOFT_WALL; MODE_SUPPLY_101.01; 9 levels |
| Key IP Support | 100.544 | 100.614 | 0.07 | SUP | MODERATE | 6 | 37 | tool zone; SOFT_WALL; MODE_DEMAND_100.61; 4 levels |

Key levels: tool weekly pivot input High 101.595; tool weekly pivot input Low 100.558; tool weekly pivot input Close 100.878

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | R | - | - | - | conf 60; zone 'Equilibrium Zone' |
| Tue | SS | - | - | - | conf 60; zone 'Mid-Range Support' |
| Wed | SS | - | - | - | conf 60; zone 'Mid-Range Support' |
| Thu | BS | - | - | - | conf 80; zone 'Key IP Support' |
| Fri | BS | - | - | - | conf 80; zone 'Key IP Support' |

Computed here (not in any source): operator golden levels (VAL:214-215) falling INSIDE a tool zone: LQZ 100.945 in 'Mid-Range Support'; LQZ 100.975 in 'Mid-Range Support'; LQZ 101.190 in 'Equilibrium Zone'. OUTSIDE every tool zone: LQZ 100.845; LQZ 101.140; LQZ 101.235; LQZ 101.240; BoM 100.680; BoM 101.330.

#### EURUSD - spot at analysis: 1.1423

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| MODE_DEMAND_1.14 | 1.13486 | 1.1363 | 0.00144 | SUP | MODERATE | 6 | 40 | tool zone; SOFT_WALL; 6 levels |
| MODE_DEMAND_1.14 | 1.13644 | 1.1378 | 0.00136 | SUP | MODERATE | 6 | 40 | tool zone; 13 levels |
| LIGH_DEMAND_1.14 | 1.13798 | 1.13943 | 0.00145 | SUP | LIGHT | 5 | 40 | tool zone; 15 levels |
| LIGH_DEMAND_1.14 | 1.13954 | 1.1410 | 0.00146 | SUP | LIGHT | 4 | 40 | tool zone; 20 levels |
| MODE_SUPPLY_1.14 | 1.14105 | 1.14253 | 0.00148 | EQ | MODERATE | 6 | 40 | tool zone; zCat MID; 23 levels |
| LIGH_SUPPLY_1.14 | 1.14261 | 1.14405 | 0.00144 | RES | LIGHT | 4 | 40 | tool zone; 27 levels |

Key levels: tool weekly pivot input High 1.14728; tool weekly pivot input Low 1.13617; tool weekly pivot input Close 1.14329

| day | shape | direction | from | to | note |
|---|---|---|---|---|---|
| Mon | R | - | - | - | conf 60; zone 'LIGH_DEMAND_100.83' [DXY-scale name in an EURUSD file] |
| Tue | WL | - | - | - | conf 60; zone 'LIGH_DEMAND_100.85' |
| Wed | SS | - | - | - | conf 55; zone 'LIGH_DEMAND_100.92' |
| Thu | SS | - | - | - | conf 55 |
| Fri | SS | - | - | - | conf 55 |

**Caveats / CONFLICT / UNKNOWN:**

- DXY zone 'IP Resistance Ceiling' has top == bottom == 101.60467 (zero width, 1 level).
- EURUSD E2 file references zone names on the DXY price scale ('LIGH_DEMAND_100.83', 'LIGH_DEMAND_100.85', 'LIGH_DEMAND_100.92') - cross-pair contamination.
- EURUSD zone names are all 'MODE_DEMAND_1.14' / 'LIGH_DEMAND_1.14' / ... (rounded label collision); every EU zfp is 40.
- data/e1-cv/DXY-2026-07-06.json is the same map with two confluence values lowered (Equilibrium 9 -> 8, Mid-Range Support 7 -> 6); data/e2-cv copy is identical to data/e2.
- Other files found for this week: fixtures/bars/2026-07-06.json (DXY 1H, 382 bars, window -14d/+8d - INCLUDES forward bars), fixtures/bars/2026-07-06.validated-harvest.json (bars only, cut at the anchor), evidence/w5/wk-2026-07-06.png and evidence/cv-renders/cv-2026-07-06.png (renders of this tool output), Checkpoints/*/DXY-2026-07-06*.json (older snapshots). No file named golden*, cascade* or e1_injected* exists under /home/user/handover-branch; 'e1_injected_*' is the name of Pine literal arrays in plutus-vision-v2.pine, and 'golden cascade' is a reference to the absent PLUTUS_GOLDEN_CASCADE_23.md.

### 4.11  Week of 2026-11-09 - `approved-2026-11-09-DXY.json (+ PLUTUS_VISION_CONTEXT_HANDOVER.md sections 2.3 and Appendix B section 3)`

- **Prompt version:** v5.3.3 E1 ('5.3.3. NOTHING ELSE' - the only authority is the 5.3.3 prompt, HO:886); zones are those of an earlier E1 run's render (e1/runs/2026-11-09-DXY, 'the run of 2026-11-06..08') that the operator judged - not a weekly LLM report PDF; how that run computed them is UNKNOWN from the files read
- **Data as-of:** week Monday 2026-11-09 to Friday 2026-11-13 (HO:889); prior weekly bar H=102.358 L=101.099 C=102.279 (audit.md:6)
- **Generated:** operator verdict recorded 2026-11-24 on render 'e1/runs/2026-11-09-DXY/render-2026-11-24-final.png' (APPR:4; HO:918)
- **Oracle grade:** OPERATOR-APPROVED E1 TARGET (the strongest E1 oracle on disk): 'DO NOT ADD ANY MORE FUCKING ZONES THESE 6 ARE CORRECT ... ZONES 3 4 AND 5 NEED REFINEMENT. 1 2 AND 6 ARE CORRECT' (HO:885; APPR:4). E1 only - no E2 chain, no E3 setups.

**Data the report used (pillars with real data).** Not a report. The approved render came from the E1 run 'e1/runs/2026-11-09-DXY' (HO:918); the build rules bars to come from TradingView / Pinebox store TVC_DXY (R-23, HO:902); analyst evidence was 'captured at report time (the run of 2026-11-06..08 ...)' (2026-11-09-DXY.analyst-evidence.json: fxstreet, think.ing.com, forex.com, continuumeconomics). Handover notes zone 2 'stood on the prior daily close 102.279 and high 102.358 and on three USD/JPY walls at 102.237 / 102.326 / 102.414' in the approved run (HO:226-227). Option board for the later tool run: 'Raw strikes from VLM: 15 strikes across 7 pairs ... Final included: 0 strikes' (audit.md:337-342). K = 108.576806 (audit.md:212).

#### DXY - spot at analysis: 102.279

| zone | bottom | top | width | side | degree | score/14 | ZFP % | key facts |
|---|---|---|---|---|---|---|---|---|
| target 1 | 102.437 | 102.535 | 0.098 | (RES inferred) | HEAVY | - | - | **CORRECT**. verdict CORRECT (APPR:7; HO:910). Tool's nearest: 102.393-102.535 drawn, '0.044 wider at the bottom' (HO:215) |
| target 2 | 102.205 | 102.354 | 0.149 | (EQ (contains spot) inferred) | MODERATE-HEAVY | - | - | **CORRECT**. verdict CORRECT; 'contains the Friday-night close 102.279' (APPR:8; HO:911). Tool's nearest: 102.164-102.311, LIGHT, rank 17, not drawn (HO:216) |
| target 3 | 101.70 | 101.84 | 0.14 | (SUP inferred) | MODERATE-HEAVY | - | - | **REFINE**. verdict REFINE - 'too wide, refine'; no tight cluster (APPR:9; HO:912, 917). Tool's nearest: 101.674-101.815, rank 9, not drawn (HO:217) |
| target 4 | 101.933 | 102.061 | 0.128 | (SUP inferred) | MODERATE-HEAVY | - | - | **REFINE** core 101.97-102.01. verdict REFINE - core 101.97-102.01 (APPR:10; HO:913, 917). Tool's nearest: 101.860-102.008, HEAVY, drawn, 'centre 0.063 away' (HO:218) |
| target 5 | 101.453 | 101.601 | 0.148 | (SUP inferred) | MODERATE-HEAVY | - | - | **REFINE** core 101.49-101.53. verdict REFINE - core 101.49-101.53 (APPR:11; HO:914, 917). Tool's nearest: 101.412-101.544, drawn, 'narrower' (HO:219) |
| target 6 | 100.986 | 101.099 | 0.113 | (SUP inferred) | MODERATE-HEAVY | - | - | **CORRECT**. verdict CORRECT (APPR:12; HO:915). Tool's nearest: 100.986-101.136, drawn, '0.037 wider at the top' (HO:220) |

Key levels: Prior week High 102.358; Prior week Low 101.099; Prior week / Friday close 102.279; USD/JPY wall (approved run) 102.237, 102.326, 102.414

**Caveats / CONFLICT / UNKNOWN:**

- Zones 3, 4, 5 are 'too wide, refine' (HO:912-914): the true target is NARROWER than the listed range. Cores: zone 4 core 101.97-102.01; zone 5 core 101.49-101.53; 'zone 3 has no tight level cluster (its core must come from where price traded)' (HO:917; APPR:9-11).
- 'The labels on that render carried only the degree; the operator requires name, degree and ZFP.' (HO:918) -> names and ZFP for these six are UNKNOWN in the oracle.
- Degrees are 'degree in the approved render' (HO:908), i.e. from the tool render the operator approved, not separately confirmed per zone.
- No side (RES/EQ/SUP) is recorded in the source; 'side_inferred' below is derived here from spot 102.279 (CHK:7) and is NOT in the source.
- The later tool run does NOT reproduce the target: 'REFUSED TARGET_MISMATCH: 9 differences' (HO:211); it produced 23 zones, 21 of them 0.115-0.150 wide (HO:232-235).
