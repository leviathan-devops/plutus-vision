# Visual checkpoints since the "70% functional" package

Every frame rendered and opened in this window, oldest first. All are Pinebox renders of the generated Pine on top of the sealed V1, except the operator's library pictures, which are named as such.

Rules for these frames:
- The expectation was written in `memory/07_EVIDENCE_LEDGER.md` BEFORE rendering.
- Every frame cited was opened; its row in the ledger says what it showed.
- The `pb ide` box count was checked before a frame was cited (lesson L-50x: a render under load can write the previous pass's chart).

Frames are listed by path relative to the repository root and embedded with relative links.

The three-frame sets (`_zones`, `_all`, `_week`) come from `tools/s3frames`:
- `_zones`: Engine 1 only;
- `_all`: every layer;
- `_week`: every layer, x-axis fitted to the trading week.

The `_fullweek` frames come from `tools/weekframe`: one screenshot per pair, x-axis exactly Monday 00:00 UTC to Friday 21:00 UTC, price axis fitted to the candles and drawings (M-60).

---

## 1. Answers to M-58 (`evidence/answers_m58/`, commits `555482a`, `b429b8c`)

| File | What it is |
|---|---|
| `q5_golden_monday_long_TVC_DXY_15m.png` (+ `q5_golden_monday_long.pine`) | Item 5: his golden Monday long 100.945 / 100.905 / 101.115 on TVC:DXY 15m with the Monday anchor line. A correction of an earlier claim that it could not fill. |
| `s1_stop_scenario.png`, `s2_stop_scenario.png`, `s3_stop_scenario.png` (+ `s1.pine` .. `s3.pine`, `scenario_pine.py`) | Item 1: three practical stop scenarios with the decision making and the questions (`Q1_stop_scenarios.md`). He answered in M-59 (L-50). |
| `Q1_stop_scenarios.md`, `Q4_library_inventory.md`, `Q6_counting_explained.md` | Item 1, item 4 (the winning trade library inventory: about 17 pair-weeks), item 6 (the counting question with its frame of reference). |
| `handover/85pct_v3_full/answers_m58_q3/` (from the scratchpad) | Item 3: the E2 drawing question, illustrated with three pictures: my golden DXY, my EURUSD Oct 5 range week, his library GBPUSD Feb 26 - Mar 3 shape boxes. `Q3_E2_drawing_question.md`. |

![q5](../../evidence/answers_m58/q5_golden_monday_long_TVC_DXY_15m.png)
![s1](../../evidence/answers_m58/s1_stop_scenario.png)
![s2](../../evidence/answers_m58/s2_stop_scenario.png)
![s3](../../evidence/answers_m58/s3_stop_scenario.png)
![q3a](answers_m58_q3/mine_now_DXY_Jul6_golden_week.png)
![q3b](answers_m58_q3/mine_now_EURUSD_Oct5_range_week.png)
![q3c](answers_m58_q3/your_library_GBPUSD_Feb26-Mar3_shape_boxes.png)

## 2. Daily anchoring, first look (`evidence/chk107/`, ledger 107 / 107b, code `7460b58` / `636326e`)

| Map | Files | What it showed |
|---|---|---|
| DXY 2026-05-18 | `DXY_2026-05-18_{zones,all,week}.png` | The four repeat boxes DX1.Tue-Fri (long 99.050 on a 1H demand closed through Mon 21:00 UTC) are gone. The line restarts at each trading-day open. |
| DXY 2026-07-06 | `DXY_2026-07-06_{zones,all,week}.png` | Every golden order kept; the line restarts at each day open. |

![chk107 DXY 05-18](../../evidence/chk107/DXY_2026-05-18_week.png)
![chk107 DXY 07-06](../../evidence/chk107/DXY_2026-07-06_week.png)

## 3. The library weeks, first renders (`evidence/lib1/`, ledger 108 / 108b, commit `496d4f6`)

GBPUSD 2026-02-23, 03-02, 04-06 and 04-13 (`_zones` / `_all` / `_week` each). Weeks formerly reserved for the blind test, now oracle weeks (D-129).

Delta for 03-02 against his chart (ledger 108b):
- my Engine 2 is one day late;
- there is no reversal after the breakdown;
- his Wednesday long 1.3313 / 1.3300 / 1.34015 is missed.

![lib1 02-23](../../evidence/lib1/GBPUSD_2026-02-23_week.png)
![lib1 03-02](../../evidence/lib1/GBPUSD_2026-03-02_week.png)
![lib1 04-06](../../evidence/lib1/GBPUSD_2026-04-06_week.png)
![lib1 04-13](../../evidence/lib1/GBPUSD_2026-04-13_week.png)

## 4. Alternative-chain activation (`evidence/lib2/`, ledger 109 / 109b, commit `748c71e`)

GBPUSD 2026-04-13 against his library chart (R->WL 19-11-49).
- From Tuesday the alternative chain is the chain.
- The GB1 range longs far below price and GBB2 are gone.
- Not met: the Tuesday line still dives 1.350 -> 1.330. The alternative keeps its Monday timing.

![lib2](../../evidence/lib2/GBPUSD_2026-04-13_week.png)

## 5. Daily zone update, render FAILED (`evidence/lib3/`, ledger 110 / 110b, commit `fe24f31`)

The `_all` pass hit CDP_TIMEOUT while the 12-map locator used the Pinebox station. The week shot shows the zones-only pass ("new <Day>" zones drawn from their London opens, no E2 / E3).

Kept as evidence of the incident (lesson L-50x). Not a valid frame.

![lib3 (invalid)](../../evidence/lib3/GBPUSD_2026-04-13_week.png)

## 6. Session line + daily update, one render at a time (`evidence/lib4/`, ledger 111 / 111b / 111c, code `8a40708`; the 80% checkpoint)

**GBPUSD 04-13:**
- New zones Tue / Wed / Thu are drawn.
- Day boxes and lines come from the chain re-anchored at the London opens: Tue box 1.3441-1.3585, Wed-Fri 1.3522-1.3599, where price traded.
- Not met: the Monday breakout. The Tuesday NY leg down did not happen. Thursday's direction is wrong. Every day is tagged SS.

**DXY 07-06:**
- Golden week intact.
- Monday and Tuesday drawn session by session (London to the ceiling, strike pin 08:00-10:00 NY, NY to the floor).

![lib4 GBPUSD](../../evidence/lib4/GBPUSD_2026-04-13_week.png)
![lib4 DXY](../../evidence/lib4/DXY_2026-07-06_week.png)

## 7. M-60 whole-week frames (`evidence/m60/`, ledger 112, commit `e3860c7`, code = the 80% checkpoint)

The first whole-week frames of all three pairs (M-60: "I need to see the entire trading week in a single screenshot"). They are the basis of the diagnosis that the DXY Wed-Fri line was a straight slide from Wed NY to Fri LON, with the WL + RWL squeezed into Fri NY.

![m60 DXY](../../evidence/m60/DXY_2026-07-06_fullweek.png)
![m60 EURUSD](../../evidence/m60/EURUSD_2026-07-06_fullweek.png)
![m60 GBPUSD](../../evidence/m60/GBPUSD_2026-07-06_fullweek.png)

## 8. V1 = checkpoint "85% functional - DXY + GU" (`evidence/m60b/`, ledger 113, commit `bac6b50`, code `d48d3e9` = D-139 + D-140)

The frames the operator graded in M-61:
- DXY and GBPUSD "A-" except Thursday;
- EURUSD "a solid C".

The DXY Wed-Fri line steps with the candles. On every pair the dormant alternative boxes (DXA*, EUA*, GBA*) are still drawn.

![V1 DXY](../../evidence/m60b/DXY_2026-07-06_fullweek.png)
![V1 EURUSD](../../evidence/m60b/EURUSD_2026-07-06_fullweek.png)
![V1 GBPUSD](../../evidence/m60b/GBPUSD_2026-07-06_fullweek.png)

## 9. V2 = the Thursday fix (`evidence/v2/`, ledger 114, commit `65ae7fc`, code `262fadd` = D-141)

- **DXY Thursday:** only DX7, the ladder short (his #7). DX4 (his #6, 101.235 = DX6's TP) is drawn from Wed 06:00.
- **GBPUSD:** the short at Wednesday's TP 1.34254 (his #5). The Thursday / Friday ladder longs under the open are gone.
- **All pairs:** alternative contingencies only in the report.

![V2 DXY](../../evidence/v2/DXY_2026-07-06_fullweek.png)
![V2 EURUSD](../../evidence/v2/EURUSD_2026-07-06_fullweek.png)
![V2 GBPUSD](../../evidence/v2/GBPUSD_2026-07-06_fullweek.png)

## 10. V3 = the EURUSD fix (`evidence/v3/`, ledger 115 / 115b, commit `a8bfce4`, code `ff6be1e` = D-142b + D-144)

`pb ide` boxes: DXY 53, EURUSD 59, GBPUSD 59.

**EURUSD:**
- Monday = one short 1.14442 (his #3) plus the longs 1.14095 (his #2) and 1.14018 (never fills).
- The V2 boxes "EU2 SS S 4.8R" (1.14385, stopped) and "EU5 SS L 5.8R" (Tuesday re-entry, stopped) are gone.

**DXY:** identical to V2.

**GBPUSD:** the Tuesday "GB3 SS L 6.0R" (never filled) is gone.

**Open:**
- The EURUSD Wednesday labels overlap each other and the LSZ / option labels at 1.1400.
- The EURUSD Friday line ends at 1.1444 while the RWL ran to about 1.1415.

![V3 DXY](../../evidence/v3/DXY_2026-07-06_fullweek.png)
![V3 EURUSD](../../evidence/v3/EURUSD_2026-07-06_fullweek.png)
![V3 GBPUSD](../../evidence/v3/GBPUSD_2026-07-06_fullweek.png)

The EURUSD explanation that went with V3: `evidence/answers_m61/EURUSD_why_C.md`.

---

## The operator's own pictures used as oracles in this window

`/home/user/inputs/trades/WINNING_TRADE_LIBARARY/` (archive part 5):
- the golden week `Jul_6-10_DXY_Gold_Standard/` (8 screenshots);
- 38 screenshots in ten shape-chain folders.

Read from each picture's date axis: `evidence/answers_m58/Q4_library_inventory.md`. Contact sheets used to read them are in the scratchpad (`lib/`, archive part 6).
