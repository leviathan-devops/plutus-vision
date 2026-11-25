# 11 — E1 TOOL BUILD BRIEF (the job, complete; written 2026-11-25 night; READ FULLY AFTER EVERY COMPACTION)

Operator is asleep ~10 h from 2026-11-25 ~21:30 UTC (container clock). Work autonomously, do not wait, do not stop until done. Verify everything yourself in Pinebox.

## 0. Read order after a compaction (do not skip, do not skim)
1. `memory/10_FAILURE_RECORD.md`  (why everything before was rejected; the rule)
2. THIS FILE
3. `memory/12_OPERATOR_VERBATIM.md` — the last ~25 messages (his exact words; they define the task)
4. `memory/04_OPERATOR_RULINGS_LIVE.md` L-27..L-39
5. `e1_tool/E1_PSEUDOCODE.md`, then the SOURCE TEXT it maps to: `e1_tool/canon_extract/*` (verbatim prompt sections) — read the source, never a summary
6. `e1_tool/reference/Leviathan_DXY_IL_Report_Apr20-24_2026.txt` (the output to reproduce) and `e1_tool/reference/trident_v8.pine` (the output form)
7. `memory/01_CURRENT_STATE.md` (where the build stands), tail of `memory/05_JOURNAL.md`
Graph: `tools/mem/mem q "<words>"` searches all of memory/*.md.

## 1. The task (operator's words, condensed; full text in 12)
"The prompt is a working software program written in English. Rewrite the exact same program in Python. Do not change a single thing. All we're doing is changing the compiler from an agent to mechanical code."
- Scope: ENGINE 1 ONLY. E2 and E3 are out. No redesigns, no scorers, no tuning, no ideas of my own.
- Process: prompt prose -> pseudocode (done: `e1_tool/E1_PSEUDOCODE.md`) -> Python, one function per prompt step, same order, same thresholds/tables.
- Tool input: a trading week (+ pair). It fetches its own data at run time ("bundled libraries").
- Tool output: a PINE SCRIPT with that week's zones as data, in the form/colours/labels of `e1_tool/reference/trident_v8.pine`, to paste into the indicator. The generated Pine holds the week's numbers (allowed); the Python must hold no price literals.
- Acceptance: any week, DXY / EURUSD / GBPUSD, zones as accurate to the candles as the Apr 20-24 reference (~90%), judged BY LOOKING at the render in Pinebox. First: reproduce Apr 20-24 vs the report zone by zone. Then other weeks and pairs.

## 2. Mandatory vs optional inputs (L-32)
MANDATORY: (a) investingLive FX option expiries (Protocol A); (b) TradingView OHLC candles — the Pinebox bar store `~/.local/share/pinebox/data/tv-bars/{TVC_DXY,FX_EURUSD,FX_GBPUSD}/{15,30,60,240}/*.json`
(2025-02-02 -> 2026-11-06) or https://github.com/Mathieu2301/TradingView-API (yfinance is REPLACED); (c) the entire 9-pillar / 6-dimension computation incl. the MA confluence grid.
OPTIONAL: everything else (Pillar 4 analyst commentary, Pillar 7 ICE/CME, HWC/LWC from forex.com, structural-extreme-memory web search, Fed H.10). Fetch if reachable without error; otherwise print "NO DATA" exactly as the report does. Anything the Apr 20-24 report did not absorb can be marked superseded.
Existing data plumbing to REUSE (do not rebuild): `sidecar/` already harvested investingLive expiries for 40 weeks 2026-02-02..2026-11-02 with as-of gating:
`sidecar/out/<monday>.json` = {expiries{PAIR:[{strike, notional_m, ccy, cut_date, state, tier, code,...}]}, spots, k_anchor, h10, dxy_levels, ...}; `sidecar/run --week YYYY-MM-DD` for a new week; README at sidecar/README.md.
NOTE 2026-04-20 in the sidecar has only the Friday forward row (the Monday post was published 06:08Z, after the 06:00Z anchor) while the REPORT includes the Monday Apr 20 page (it treats "Apr 20 morning" as the boundary). For reproducing the report use the report's boundary rule (Day-1 page included + Day-2 forward rows, P533:899-916).

## 3. Rulings that resolve what the prompt leaves open (all from the operator, binding)
- L-37 NO minimum move size for a supply/demand zone. Origin candle of every distinct 4H leg = zone (BoM); every continuation base inside a leg = zone (MoM). The prompt's 0.5/3-day and 1.0/5-day figures GRADE strength ("High-Conviction"), not existence.
- L-38 A S/D / order-block zone = the candle BEFORE the strong move, boxed WICK HIGH to WICK LOW, on the TradingView candle, exactly. (His notes: e1_tool/reference/Forex_SMC_Notes-1.txt/.pdf — strong momentum move; candle before it; box around its wicks; any size.
  Valid order block: inefficiency gap between the before and after candles; creates a break of structure; one-time use = unmitigated. Quality: more momentum = better; sharp reaction = valid; consolidating around it / price more than halfway in / long time inside = likely to fail.)
  Example measured on TV 4H bars: the candle before the Apr 13 2026 drop is 04-13 09:00 UTC, O 98.977 H 99.038 L 98.884 C 98.908 -> zone 98.884-99.038 (the report's 98.77-98.99 came from a yfinance candle and he judged it only ~80% fitted).
- L-39 A PRESSURE ZONE = the candle structure (A) + the cluster of computed levels (B) JOINED into one zone (C), but inside it A and B stay visibly distinct and colour-coded, each level marked individually.
  "It's C in the shape of A plus B." The point of E1 for him: SEE the data levels he cannot see on the chart. Where levels cluster with no order block: draw BOTH the pressure zone across the levels AND the sweep zone, colour-coded.
  Equilibrium zone context: gets pierced in a breakout surge, then carries weight in the recovery / swing-scalp consolidation or as a mid-surge reinforcement; the liquidity zone normally sits inside it.
- L-35 ZFP is shown as the prompt's RANGE for the zone type (e.g. "5-15%"), never one invented number.
- L-33 Steps P533 leaves "[unchanged from v4.5.2]" come from P452 (full file in e1_tool/canon_extract/).
- Visual: the original script's scheme — IP Resistance red, Equilibrium orange #FF9800, IP Support teal, LSZ green filled boxes (no labels), option strike targets amber lines + labels. He confirmed that render is what he remembers.
- Earlier standing rules still in force: Monday anchor / no data after the boundary feeds the map; Pinebox is the only test environment (look at the chart); report faithfully; no unasked advice; never touch the sealed V1 file.
- Valid reaction (L-23): sharp rejection OR consolidation in/around the zone; pivots valid; invalid = pierced like paper. Precise zones, no bloat, no bunching, no far floating zones, no missing obvious zones (L-28).

## 4. The reference to reproduce first (Apr 20-24 2026, DXY) — full text in e1_tool/reference/Leviathan_DXY_IL_Report_Apr20-24_2026.txt
Header: Trident Trading Engine v4.5.2; Data As-Of Apr 17 2026 17:00 ET; DXY spot 98.10 (Apr 17 close); generated 2026-05-25.
Options (investingLive page for Apr 20, published 2026-04-20T06:08:28Z; Mon + Tue forward rows included; Wed-Fri EXCLUDED/NO DATA):
 Mon EUR/USD 1.1600 €1.9bn -> 99.22 · 1.1750 €2.6bn -> 98.49 · 1.1785 €1.1bn -> 98.32 · 1.1900 €1.0bn -> 97.78 ; GBP/USD 1.3500 £1.0bn
 Tue EUR/USD 1.1600 €929M -> 99.22 · 1.1655 €722M -> 98.95 · 1.1675 €1.8bn -> 98.86 · 1.1760 €1.1bn -> 98.44 · 1.1780 €883M -> 98.35 · 1.1800 €1.8bn -> 98.25 · 1.1810 €1.0bn -> 98.20 ; GBP/USD 1.3300 £1.0bn
K = 108.0806 (USDJPY 158.93, GBPUSD 1.349, USDCAD 1.3897, USDSEK 9.1921, USDCHF 0.7828), band ±0.07. Reverse check: DXY 98.10 -> EUR/USD 1.1832 (actual 1.1753).
Prior week Apr 13-17: H 99.18 L 97.63 C 98.10. Classic PP 98.30 R1 98.98 R2 99.85 R3 100.53 S1 97.43 S2 96.75 S3 95.88. Fib PP 98.30 R1 98.90 R2 99.26 R3 99.85 S1 97.71 S2 97.35 S3 96.75.
IP zones (MODERATE and above): RESISTANCE CEILING 99.16-99.23 HEAVY 10/14 ZFP 15% Tier 2 [P1 weekly R1, P5 SH 99.18 repeated high 2x, P6 round 99.00 area]
 UPPER RESISTANCE 98.77-98.99 MOD-HEAVY 8/14 25% Tier 1 [P1 daily classic R1 (Apr 13), P5 4H BoM supply, P6 fib 38.2%]
 EQUILIBRIUM ZONE 98.29-98.41 MOD-HEAVY 9/14 20% Tier 2 [P5 repeated high magnet 98.29 (3 dates), P1 daily pivots cluster, P5 prior daily closes]
 MID-RANGE SUPPORT 98.00-98.12 MODERATE 7/14 30% Tier 2 [P5 prior daily closes cluster, P1 daily pivot PP/S1 cluster, P6 round 98.00]
 KEY SUPPORT BAND 97.63-97.97 HEAVY 11/14 12% Tier 1 [P5 liquidity sweep target 97.63, P5 4H BoM demand 97.63-97.94, P1 weekly S2/S3 cluster]
4H zones (origin candle OHLC from yfinance): BoM Demand 97.93-98.11 (2026-04-16 00:00, 0X, up 0.35 over 2 days) · BoM Supply 98.77-98.99 (04-13 04:00, 1X(1S), down 0.62 over 3 days)
 · BoM Demand 97.63-97.94 (04-17 08:00, 0X, up 0.26 intraday developing) · MoM Supply 98.34-98.42 (04-13 20:00, 1X(1S), down 0.12 continuation)
LSZ: 97.63-97.68 (D1 swing low 04-17, ACTIVE SL TRIGGER) · 97.83-97.88 (low 04-16) · 97.97-98.02 (low 04-14) · 98.53-98.58 (low 04-08) · 98.29-98.34 (swing high 04-15/16/17, 3x) · 99.18-99.23 (swing high 04-08/13, 2x)
Clustering: 126 levels, 22 clusters; HD-1 99.16-99.27 (8) · HD-2 98.90-99.04 (6) · HD-3 98.77-98.89 (5) · HD-4 98.53-98.67 (10) · HD-5 98.37-98.51 (19).
trident_v8.pine DXY arrays: zTp 99.23,98.99,98.41,98.12,97.97 / zBt 99.16,98.77,98.29,98.00,97.63 / cat RES,RES,MID,SUP,SUP / names IP Resistance Ceiling, Upper IP Resistance, Equilibrium Zone, Mid-Range Support, Key IP Support;
 LSZ xTp 97.68,97.88,98.02,98.58,98.34,99.23 / xBt 97.63,97.83,97.97,98.53,98.29,99.18; option lines 99.22,98.49,98.32,97.78,98.86,98.44,98.25 with notionals.
With TradingView candles the S/D zones will sit on TV wicks (L-38), so numbers differ by a few pips from the report; the STRUCTURE (which candles, which levels, which zones) must match. Report which numbers differ and why.
How that week traded (TV bars, seen in the frames): Mon dip stops in the Key Support Band and the week's rally starts there; stall in the Equilibrium Zone; week high ~98.93 inside Upper Resistance; ceiling 99.16-99.23 untouched during the week.

## 5. Where everything is (artifact index)
- Verbatim prompt sections: `e1_tool/canon_extract/P533_lines_0739-1568_PART_III_IV_E1_pipeline.md` (Protocol A, pillars 1-9, 0f, synthesis, 9.5, 9.7), `P533_lines_1568-1725_PART_V_report_output.md`,
  `P533_lines_4011-4216_appendices.md`, `P452_FULL_Trident_System_Prompt_v4.5.2.md` (Protocol B from line 250; Pillar 5 from 517; 0f 637; 0g 749; 0h 767; steps 1-5 785; P6 835; P7 866; P8 890; P9 954; synthesis 1075; assembly 1116; 9.5 1159; 9.7 1186; report spec 1486).
- Reference outputs: `e1_tool/reference/` — both reports (pdf + txt), trident_v8.pine, trident_v7, Forex_SMC_Notes-1 (pdf + txt), Fractal Architecture v2.3.
- Original files: `/home/user/handover-branch/Original_Canon_Data/` (git worktree of origin/handover), `/home/user/inputs/{handover,pinebox,canon,trades,aether,toolset_glm}`, uploads `/root/.claude/uploads/b6c77a81-*/`.
- Operator's golden-week screenshots: session images dir `/tmp/claude-0/-home-user-plutus-vision/b6c77a81-*/images/{1,2,3}.webp`; trade library `/home/user/inputs/trades/WINNING_TRADE_LIBARARY/` (his S/D boxes sit on exact wick edges of order-block candles).
- Frames: `evidence/trident_v8_original_{DXY,EURUSD,GBPUSD}_1h_apr20_allzones.png` (the reference render, all zones in frame); `evidence/question_case{1,2,3}_dxy_4h.png` (zone-edge cases he ruled on); `evidence/w14_report_exact_*`.
- Rejected work (do not reuse as design): indicator/plutus-vision-engines.pine (E1 v1-v3, E2 v0, E3 v1), tools/research/* (scorers, prototypes). Sealed V1: indicator/plutus-vision-v1.sealed.pine (never edit).

## 6. Working recipes (measured; they save hours)
- Pinebox DIES whenever the session worker restarts. Before any render: `export PATH=$HOME/.local/bin:$PATH XDG_RUNTIME_DIR=/run/user/0; pinebox list --session plutus-main | grep -q '"alive":true' || { pinebox down --session plutus-main; sleep 2; pinebox up --session plutus-main --adapter xvfb; sleep 8; }`
  If `pinebox` is missing entirely: `tools/pinebox-bootstrap.sh`.
- Render a Pine file in the IDE: `tools/pb ide FILE PAIR TF [input=value ...]` (prints boxes/labels/lines counts — 0 boxes = failed render), `tools/pb goto FROM TO`, then fit the price axis so every drawing is in frame:
  `tools/pb eval "(function(){const P=window.PlutusPineShell; const r=P.chart.rendererControl.renderer; const d=P.chart.drawings.toJSON().drawings; let lo=Infinity,hi=-Infinity; for(const x of d){ if(x.type==='box'||x.type==='line'){ for(const a of x.anchors){ if(typeof a.price==='number'){ lo=Math.min(lo,a.price); hi=Math.max(hi,a.price);} } } } const vr=P.chart.getVisibleRange(); for(const b of r.bars){ if(b.time>=vr.from&&b.time<=vr.to){ lo=Math.min(lo,b.low); hi=Math.max(hi,b.high);} } const pad=(hi-lo)*0.04; const res=r.resolveScaleHolder(r.coords.widthPx-20,200)||r.resolveScaleHolder(400,200); r.setManualScale(res.holder,{min:lo-pad,max:hi+pad,invert:false}); return {lo,hi};})()"`
  then `tools/pb shot NAME chart` -> evidence/NAME.png. ALWAYS open the frame (Read) before citing or sending it.
- Engine quirks (Pinebox Pine): `request.security` returns NaN; history `x[1]` only at global scope; both ternary branches are evaluated (and `a and b` evaluates b); names `fill`, `to`, `from`, single-letter `A` clash; tables do not show in the IDE frame; labels placed at mid-span get cut off (place labels inside the visible week).
- The ECC hook: first Bash/first Write to a NEW path is refused once — state 3 lines of facts and retry; long compound Bash is refused ("work budget") — keep commands short; writing new files via `cat > file <<'EOF'` in Bash works.
- Commit + push to branch AGENT after every step (`git push -u origin AGENT`). Stop hook complains about untracked files — commit them.
- Bars helper for Python: `tools/research/score.py` has `bars(pair, tf)`, `pre(pair, monday, tf)` (bars closed by the anchor). TV 4H bars are stamped at 21:00/01:00/05:00/09:00/13:00/17:00 UTC (17:00 New York session start).

## 7. Build plan (do in this order; verify each step against the report before the next)
1. `e1_tool/` Python package: data loaders (TV bars; sidecar expiry JSON), then one module/function per prompt step in the pseudocode's order, each printing the report's audit trail for that step.
2. Run for DXY week 2026-04-20; diff every section against the report text (options table + DXY equivalents, K, pivots, 4H zones, LSZ, clustering, zones). Explain each difference (data source vs logic). Fix logic differences only by re-reading the prompt text.
3. Pine generator in trident_v8 form + the L-39 rendering (levels marked inside zones, candle part vs level part colour-coded, LSZ green, strikes amber). Render in Pinebox on DXY Apr 20-24, fit the axis, OPEN the frame, compare with evidence/trident_v8_original_DXY_1h_apr20_allzones.png.
4. Other weeks and pairs (EURUSD, GBPUSD use each pair's own candles and strikes): render, open, describe what each zone did, honestly. Ledger rows in 07 with frames.
5. Keep memory current (01 state, 05 journal, 07 ledger) every few steps; `tools/mem/mem rebuild`.
Do not ask the operator anything unless truly blocked; he is asleep. Do not invent. When the prompt is silent and no ruling covers it, take the plainest literal reading, write it in the journal as an assumption, and list it for him in the morning report.
