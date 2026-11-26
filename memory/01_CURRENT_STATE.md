## STATE (NEWEST, 2026-11-27 ~00:00 UTC, after compaction 11) - FIFTH OUTSIDE COUNT RUNNING (reviewer in the background) on frames evidence/s3e + facts audit/g1_facts_e = code 3b5b52c (D-70..D-84) -> audit/G1_count_dryrun5.md. Ledger 85 = expectation, 85b = my look; add 85c with its numbers. DO NOT touch evidence/s3e or audit/g1_facts_e while it runs.
- Since those frames (HEAD 87e62fd+): D-85 depleted range bound = TP only, entry at the liquidity beyond it (P533:1159, E3C:1052, 6.4.2); D-86 SS TP at a sweep-zone bound = near edge; E2 range box to the liquidity beyond a depleted bound; e1_pine.reach measured-move reach behind flag REACH_MM (OFF).
- Locator (bash tools/research/allfills.sh TAG): 32 TP / 17 stops on 16 maps. Golden three pairs unchanged since b7a2ac5 (python3 tools/research/oracle_diff.py PAIR).
- A SANDBOX COPY of the tool lives in the scratchpad (sb/): trials run there while frames render (never edit e1_tool during a render; `pgrep -f tools/s3frames` must be empty before frames are committed or a reviewer started). A render of 12 maps takes ~7 minutes.
- Tried and rejected tonight (journal): (a)-stops moved outside a sweep level at a candle zone's back edge (breaks golden EURUSD #5 / #8, DXY #3); pressure zones inside the range as scalp anchors (+0 TP / +4 stops); a 'virgin MoM = reject' gate (his own golden longs stand on '1H (Unmitigated) | MoM' zones, memory/08 last section).
- FOUND, NOT DECIDED: the three GBPUSD tops the fourth count called 'no zone' HAVE Engine 1 zones (05-18 1.3463: 4H band + in-fill; 10-05 1.32856: 1H BoM supply 1.32731-1.32942; 04-20 1.35444: pressure zone 1.35434-1.35508) - the reach window (e1_pine.reach) hides them. REACH_MM = True shows them but doubles the drawn zones. Decide with the fifth count's E1 numbers.
- GBPUSD day maps on divergence weeks (04-20, 05-18) are wrong BY CANON 9.13 ('Do NOT override the DXY direction - DXY is the driver'); the canon's own remedy is the PAIR DIVERGENCE flag (- 2 conviction), not built.
- NEXT: read the fifth count -> ledger 85c -> work its defect list (E3 first) -> sixth frame set on the then-current commit. Open canon rows unchanged (memory/15; audit/G2_response.md), then fresh G2 audit (S1 / S4), S5 blind test, S6 checkpoint.

## READ THIS FIRST (2026-11-26 ~23:00 UTC): THE FIBONACCI SPIDERWEB = HIS TRADE CONSTRUCTION, NOT YET IN CODE. memory/08 last section has the PDF's rules and the arithmetic: every golden DXY trade is entry at Fib 0.5 / 0.618 / 0.786 of a range between two Earth points, SL 1-2 Fib levels back, TP exactly one range height away (wormhole). NEXT STEP = build it (coverage E2-AIR / E3-P3 / Law 5): anchors (4H swings for BS / WL; 15m consolidation range for SS; 30m same-day), London-open position per day as the setup anchor, entry / SL / TP from the web with the PDF's buffers; verify on all 23 golden trades first (tools/research/oracle_diff.py), then the 16 maps, then a fifth outside count (frames s3e, brief 5 = brief 4 + joined-zone legend).
- Fourth outside count (ledger 82b): E1 77 / E2 78 / E3 34; outside the golden week 73 / 71 / 14. E3 outside the golden week is the engine to fix; three E3 variants tried tonight added more stops than TP fills (journal): the missing piece is the Fib construction above, which sets stops at 0.17-0.29 of the range and TPs one range away.

## STATE (NEWEST, 2026-11-26 ~22:30 UTC) - fourth outside count RUNNING on frames evidence/s3d (code 591f70c = D-70..D-77) -> audit/G1_count_dryrun4.md (ledger 82 = expectation; add 82b). Since those frames: D-78 per-day swing-scalp setups, D-79 bounds on resting stops, D-80 measured-move fallback, D-81 joined-zone drawing (12 zones + parts instead of 36 drawings), tools/s6shot + ledger 84 (co-render with the sealed V1).
- NEXT after 82b: fifth frame set evidence/s3e + facts audit/g1_facts_e on the current code (brief 5 = brief 4 + legend line for joined zones / parts and for per-day setups), then the count; work its E3 list. Open canon rows that generate setups: R scalps, DWL inverse, mirror / emergent lanes (E3C Phase 10), BREAKOUT EXTENSION TARGET zone (Pillar 9 Step 4) + alternative-chain transition orders (tried: no target beyond the map), Mechanism A middle / back fills, 1-2-3 retest gate, WorkingDayMap object, Phase 7.
- Locator 29 TP fills / 24 stops on 16 maps (scratchpad allfills.sh; scratchpad files do not survive a reset: tools/research/fills.py PAIR MONDAY per map is the durable form).

## STATE (NEWEST, 2026-11-26 ~22:15 UTC) - after the third outside count: D-70 .. D-77 committed. NEXT = fourth outside count on this code (frames evidence/s3d, facts audit/g1_facts_d, brief audit/G1_brief4.md = brief 3 + 'DXY Apr 20: the obvious trades are his two real trades (goal prompt S3)').
- Golden oracle distances now (tools/research/oracle_diff.py PAIR): DXY #2-#6, #8 all within 2.5 pips on entry / SL / TP; EURUSD #2 #3 #4 #6 #8 within ~3 (#5 SL 4.4, #7 rocket 6.9); GBPUSD #1 #2 #5 within 3 pips (#3 entry 7.5 off, #4 #6 #7 not on the map).
- Locator 31 TP fills / 18 stops over 16 maps. Opus sub-agents: 5-hour usage limit hit at ~21:10 UTC, reset 21:40.

## THIRD OUTSIDE G1 COUNT (2026-11-26 late, audit/G1_count_dryrun3.md, ledger 80b): E1 91.7 / E2 68.3 / E3 29.5; outside the golden week 91.2 / 64.4 / 14.0. S3 NOT MET.
WORK ORDER: (1) ENGINE 3 outside the golden week (49 of 57 obvious trades missed): per map list each missed leg with the candidate that should have caught it and its reject reason (facts files audit/g1_facts_c show the '!' reject lines); (2) E1 selection: 20-34 drawings per map, sweep-zone pairs 1 pip apart (merge per P533 0.5 repeated extremes / cluster 0.05), which V1 bands and LTF zones belong on the default view; (3) E2 on GBPUSD (May 18 Monday break of the ceiling; Apr 20), Tuesday breaks in range weeks; (4) labels. Since its frames: D-70 .. D-73 + front fix (commit after f02a8e3). Fourth count only after E3 moves on the locator.

## STATE (NEWEST, 2026-11-26 night, after compaction 10) - THIRD OUTSIDE COUNT BEING PREPARED on commit 5670e41+ (D-62..D-68). Operator order stands: do not stop while S1-S6 are open.
- Since the second count (ledger 79): D-62 Mechanism A front on every zone setup + tick tolerance in fills.py; D-63 a BoM pressure zone in reach bounds a side before a sweep zone; D-64 range boxes into the bounding zones + sweep reach 0.10 (P533 0.45a), sweep zones labelled;
  whiplash / reversal split inside one session; D-65 stop (a) on the entry zone's back edge; D-66 Law 14 no teleport past an unmitigated zone; D-68 E1 Step 9.5 gap scan (in-fill levels = E1 objects only; E2 / E3 do not read them yet).
- 16-map locator: 30 TP fills / 17 stops (allfills.sh in the scratchpad: runs tools/research/fills.py over scratchpad maps.txt). Golden DXY / EURUSD setups unchanged (tools/research/oracle_diff.py DXY).
- Third count: frames evidence/s3c (tools/s3frames, three per map), facts audit/g1_facts_c (tools/g1facts), brief audit/G1_brief3.md (E1 objects defined per goal prompt 4b + legend + G1 rule verbatim) -> the reviewer writes audit/G1_count_dryrun3.md. Ledger row 80 = expectation; add 80b with its numbers.
- OPEN (next, by canon row): (1) in-fill levels in E2 / E3 (bound? target? anchor?) - tried as full zones: E2 targets move onto them, GBPUSD golden crashes; (2) GBPUSD day maps (May 18 Monday rally out of the range; Apr 20); pair bounds;
  (3) BS duration: golden wants 4 sessions, Apr 20 wants 7 (code: 3 x 2); Friday undesignated after the chain ends under 25%; (4) EURUSD May 18: no long at the IP floor (SOURCE_INVALID), shorts stopped 3-5 pips under the week high (Law-7 buffer E3C:297-304 has no code);
  (5) Apr 20 DXY: BS long 97.984 missed Monday's low 98.006 by 0.2 pip beyond the front; RWL short at the BS target rejected RRR 1.99; (6) WorkingDayMap / Phase 7, Mechanism A middle / back fills + blended RRR gate, 1-2-3 retest entry, ZR-6B, Consolidation Phase, rule 11;
  (7) fresh outside G2 audit (S1 / S4), S5 blind test (blind_test/RUN.md), S6.
- TRIED AND REVERTED this step: every pressure zone in reach as a bound; sweep zones inside the range as scalp anchors; re-anchoring the stop tighter in the RRR loop (journal).

## SECOND OUTSIDE G1 COUNT (2026-11-26, audit/G1_count_dryrun2.md, ledger 79): E1 46 / E2 43 / E3 29; outside the golden week 42 / 33 / 12. S3 NOT MET. Frames were of the code before D-60 / D-61.
WORK ORDER: (1) pairs' SS bounds / day boxes (GBPUSD + EURUSD May 18, GBPUSD Apr 20); (2) Friday reversal timing + Thursday breakout boxes (E2X 6.8 / 6.10 durations); (3) E1 zone on the turning side when price sits beyond the map (Step 9.5 gap scan / breakout extension: DXY Oct 5, DXY May 18, EURUSD Oct 5);
(4) entries exactly one forward spread short (front fill at first contact: check fills.py touch rule); (5) stops inside the sweep (ZR-6B); (6) labels. Then brief v3 (audit/G1_brief3.md: E1 objects defined per goal prompt 4b + colour legend), frames evidence/s3c, facts audit/g1_facts_c, third outside count.

## OUTSIDE G1 COUNT (dry run, 2026-11-26, audit/G1_count_dryrun.md): all 12 maps E1 82 / E2 35 / E3 33; outside the golden week 81 / 29 / 17. S3 NOT MET. Golden DXY + EURUSD: E3 100 (7/7 each), E2 60.
WORK ORDER from its defect list: (1) ENGINE 2 - range boxes / zigzag on SS weeks, pair bounds, day boxes of the breakout days; (2) zones the reach filter hides although the week trades there (e1_pine.reach); turns with no zone;
(3) entries one pip beyond the extremes (front-edge entry / forward spread: E3C 8.19 'Forward Spread' DXY 0.02, EUR 1 pip, GBP 2 pips; Mechanism A 'Front = zone edge nearest spot + forward spread'); (4) stops; (5) Pine: label overprint, right-edge labels, SL / TP marking, header.
Re-run the outside count after each batch of fixes (frames -> evidence/s3, facts -> audit/g1_facts, brief audit/G1_brief.md).

## STATE (NEWEST, 2026-11-26 night, fable-5-2) - S2 holds (checkpoint 0f2114b); S3 DRY RUN IN PROGRESS. Operator order stands: do not stop while S1-S6 are open.
- Since the checkpoint: D-54 rockets (20+ pips from the primary, ladder-step stop, premarket timing, parent-link bug fixed), D-55 zones straddling a bound's edge are range anchors (EURUSD his #2), D-56 reversal TP = first rung 30+ pips (EURUSD Fri TP 1.14239).
- In-window anchor-week trades of his caught (fills helper): DXY 7 / 7, EURUSD 7 / 7, GBPUSD 3 / 7 (his DXY #1 and EURUSD #1 are PRE-ANCHOR trades). 16-map locator: 21 TP fills / 19 stops.
- S3 dry run: frames evidence/s3/PAIR_MONDAY_{zones,all}.png for Jul 6, Apr 20, Oct 5, May 18 x DXY / EURUSD / GBPUSD; brief audit/G1_brief.md; facts audit/g1_facts/; the outside reviewer writes audit/G1_count_dryrun.md.
  (frames of EURUSD Jul 6 and DXY May 18 must be re-rendered after D-55 / D-56 before the reviewer starts.) Then: work its defect list, re-run. blind_test/RUN.md = the S5 run package (draft).
- Known open causes: GBPUSD stops fit rule (a) on the entry ZONE (+3 pips) where the tool uses rule (b) (his #5 stopped in my build); ZR-6B confidence switch tested by hand: breaks DXY #2 by 0.5 pip (B-26 stays OPEN);
  Apr 20 breakout legs (no retest beyond the floor that week; 1-2-3 retest entry not built); pairs outside the golden week (bounds = sweep zones 1 pip from spot; soft walls excluded as bounds); narrative gate on GBPUSD (no option data -> every zone 45%).

## S2 CHECKPOINT (2026-11-26, commit tagged s2-checkpoint): anchor week Jul 6-10 2026 holds on DXY + EURUSD by the S2 list - E2 4/5 day tags, E3 his DXY #2-#6 within 3 pips + Thursday rocket + Friday WL+RWL, EURUSD Wed longs 1.14018 / 1.13940,
8 / 9 setups; frames: ledger 76b (1H) and 75b (15m entries, Backtest tab). NOT part of S2 and still open on the anchor week: his DXY #1, EURUSD #1 #2, GBPUSD #2 #6 #7; EURUSD / GBPUSD reversal TPs. NOW: S3 (four weeks x three pairs), S1 / S4 (audit list), S5, S6.

## STATE (NEWEST, 2026-11-26 late, fable-5-2) - OPERATOR: "If the goal is not met, you're not allowed to stop." DO NOT END A TURN WHILE S1-S6 ARE OPEN (no blocker exists). Loop = take the next loser, find the bug in MY build, fix by canon line, re-check all maps.
- Commits since the block below: 9ec23b1 (D-47 stop shields walked nearest first), D-48 (E2 supply/demand bound = first scalp TP), D-49 / D-50 (breakout target passes standalone MoM zones and weak MoM pressure zones, P452:2082),
  Law-27 reversal at the breakout TP, D-51 Transition Entry (E3C:107 / 457), D-52 confidence terms (E3C:407-414), f723b0b. audit/G2_response.md = disposition of all 134 findings (37 FIXED, 13 ANSWERED, 28 PART, 56 OPEN) - update it when a finding closes.
- Fills now (tools/research/fills.py, re-arms SS orders daily): golden DXY 7 TP / 0 SL; golden EURUSD 5 TP / 1 SL; golden GBPUSD 2 TP / 1 SL (his #1, #3 TP, #5 entry within ~1 pip); Apr 20 DXY 1 TP / 2 SL (BS long 97.984 unfilled: no retest dip that week);
  May 18 DXY 2 TP / 1 SL; Oct 5 DXY 1 TP / 1 SL. Weak: Jul 13, Aug 17, Jun 8, Sep 14, every pair map outside the golden week (list with causes: journal entry of this date).
- NEXT (in order): (1) frame + ledger for golden GBPUSD with this code; (2) RWL take-profit (E2X:216 'prior origin') against his three RWL TPs; (3) pairs: the pair's own bound analysis vs the DXY translation (EURUSD May 18 ceiling 'PIERCED' ignored);
  (4) Mechanism A staggered entries (E3C:1056-1070: front = zone edge + spread, middle = key level, back = far edge; blended RRR) - his entries are 'front' entries; (5) E1 Step 9.5 gap scan (Aug 17), Jul 13 direction, Sep 14 freshness on the ceiling;
  (6) outside G1 count on 4 weeks x 3 pairs (Jul 6, Apr 20, Oct 5, May 18) when the pair maps stop losing; (7) fresh outside audit; S5 ship package + blind test.
- Tools (scratchpad, re-create if lost): snap.py TAG PAIR:MONDAY... (zones / chain / setups / log per map), wk.py PAIR MONDAY (forecast day map vs actual daily H/L), stops.py (his 23 golden stops vs structures), scalp.py; tools/research/oracle_diff.py, fills.py.

## STATE (NEWEST, 2026-11-26, after compaction 9; model fable-5-2 since the operator's /model switch) - golden week re-verified on frames with the v2 engines (ledger 71-73); S3 loop next
- Commits this step: fbf932c (D-44 pivot = nearest V1 4H band; D-45 TP at a liquidity-band target = near edge), 103245f (D-46 IP-zone anchors also offer the order blocks lying mostly inside them), 1fb68f9 (Pine labels).
- Golden DXY: 8 setups, 7 TP, 1 unfilled, 0 SL; his #2 #3 #4 #5 #6 #8 + Thu ladder within 3 pips (his #1 Mon L 100.945 missing). Golden EURUSD: 7 setups, 5 TP, 1 SL (EU2 Mon S 1.14385), 1 unfilled; his #3 #4 #6 within 3 pips on entry and SL,
  #5 entry 0.8 / SL 4.4, #8 TP 14 pips short; #1 Mon S 1.14322, #2 Mon L 1.14106, #7 Thu reinforcement 1.14233 missing. Facts about his Monday scalps and the Law-27 chain: journal entry '(after compaction 9)'.
- Tried and reverted: Law-27 re-arm inside SS runs; one SS order per day (journal). Side effect kept: May 18 / Jul 13 each have one more stopped Monday long (D-46).
- NEXT, in order: (1) E3 stop = the canon's own selection (E3C:247-275: mirrorConfidenceScore >= 0.6 -> rule (a), < 0.6 -> rule (b); relevant zone by fuel state ZR-1) - re-check all golden stops, then May 18 / Oct 5 / Jul 13 fills;
  (2) deep-demand zone + Phase 9 staggered entries (E3C Phase 9, WorkingDayMap deepDemandZoneId); (3) scalp-stack (30m/15m) anchors for SS (E3C:96, Phase 4.1 layer 4) -> his Monday scalps; (4) EURUSD #8 TP, #7 reinforcement (Phase 9 at Fib 1.382/1.618);
  (5) E2 open weeks: Jul 13 direction, Aug 17 (E1 Step 9.5 gap scan), Sep 14 timing; (6) GBPUSD golden frame; 15m entries frame via the Backtest tab; (7) audit/G2_response.md, S/D findings, fresh outside audit (opus); (8) S3 four weeks x three pairs counted by outside sub-agents; S5 ship package + blind test.
- Tools: scratchpad snap.py / snap_base.py (old-vs-new setup diff over maps), scalp.py (30m/15m blocks near spot), tools/research/oracle_diff.py, fills.py.

## STATE (NEWEST, 2026-11-26 late, opus-5-5) - ENGINE 3 v2 IN PROGRESS (e1_tool/e3_trades.py rewritten: _cands / _stop / _confidence / _build / _reinforce; old file in git history before this commit)
- E3 v2 = Phase 2 candidates from the E2 chain (SS steps -> BOTH directions at every standing 1H/4H S/D zone inside the range within 30 pips of the bound + the bound itself, LTF zones first;
  other E2 moves -> one candidate at the zone E2 starts them from; retest anchored at the pivot; post-spike RWL at the unswept sweep zone against the target), gates FRESHNESS / MOM_REVERSAL / SOURCE_INVALID /
  NARRATIVE (> 30) / CONFIDENCE (< 65, base = 100 - ZFP midpoint of the anchor's IP zone else 70, D-42), stop = memory/08 refined model (rule (b) first thick step / second thin rung, 1 pip inside; (a) fallback;
  EUR/USD NO_SHIELD -> (a)), TP walk with the E2 zone FIRST, RRR 3-15, Phase 6.3 duplicates / conflicts, Phase 6.2 chain links, Phase 9 up to 3 reinforcements, reason code on every discard.
- UPDATE (later commit): golden DXY now has ALL his leveled forward trades within 3 pips from the canon phases: #2 0.2/1.3/2.0, #3 0.6/2.7/0.1, #4 1.3/0.5/0.5, #5 0.5/0.1/0.5, #6 0.0/0.5/0.5,
  #8 1.3/0.3/0.0 + Thu ladder 100.980/101.059 (his 100.975/101.09) + one extra Mon short 101.203. Fixes: IP-zone role for the zone-direction layer; transition-day last swing into the pivot ('last-swing');
  retest entry = that TP (Law 27); BS entry = the retest TP (Law 27). NEXT: fills check, EURUSD / GBPUSD / Apr 20 / other weeks, frames, ledger, audit/G2_response.md, S/D findings, fresh audit.
- FILLS with E3 v2 (commit 38e6a0b): golden DXY 8 setups 7 TP 1 unfilled 0 SL. EURUSD golden 7 setups: 1 TP (EU5 BS long = his #6 1.3/0.4/1.1), 2 SL, 4 unfilled - the pair's SS candidates sit at
  the wrong zones (his #1 S 1.14322, #2 L 1.14106, #4 L 1.14012, #5 S 1.14277 not produced; the pair needs the same 'last-swing' / retest logic: E2 pair translation gives no pivot role?) and the RWL is a SHORT
  at 1.14484 (should mirror DXY's retest = a short from the pair's pivot?). GBPUSD golden: 1 setup only (check gates in the log). Apr 20 DXY: 2 setups (Mon S stopped, Mon L TP); Oct 5 / May 18: SS all week
  -> only Monday's pair of scalps is generated (the SS step spans the week; candidates exist once per step - fine) but most later swings have no setup; May 18 short stopped by the breach (stop rule (b) at
  99.459 < Thu high 99.515). NEXT: (1) pairs: mirror the DXY E3 roles (last-swing, retest, BS, rwl) on the pair map; (2) GBPUSD gates; (3) SS-all-week weeks: re-arm swing scalps after each TP (Law 27 chain:
  TP of N = entry of N+1 inside the same SS step) so later days carry setups; (4) frames for golden DXY / EURUSD with E3 v2 + ledger; (5) audit/G2_response.md; (6) fresh audit.
- (older) GOLDEN DXY NOW: DX2 Mon S 101.138/101.213/100.825 (his #2), DX3 Mon L 100.851/100.743/101.189 (his #3), DX4 Wed BS S 101.273/101.359/100.685 (his #6: entry 3.8 off), DX5 Thu ladder 100.980/101.059,
  DX6 Fri RWL L 100.628/100.548/100.940 (his #8); 5 TP, 1 unfilled (DX1 101.203). MISSING his #4 (Wed S 101.19/101.25/100.975) and #5 (Wed L 100.975/100.905/101.24).
- NEXT (exact): (1) Wed RWL (retest) candidate rejected by CONFIDENCE 60.5 - print conf_parts, check each part against E3C:392-404; its entry must be the pivot's LOWER rung (Law 27: the TP of the last SS short
  into the pivot); (2) the last SS swing before the retest (transition day) targets the PIVOT (6.4.2: the consolidation ends retesting opposing liquidity from the pivot) -> his #4 TP 100.975; (3) BS entry =
  the RWL TP (Law 27) -> 101.235; (4) re-check EURUSD / GBPUSD / Apr 20 + all weeks (snap.py), frames, ledger; (5) audit/G2_response.md: write every finding's disposition (FIXED commit / ANSWERED canon line /
  OPEN); (6) S/D findings; (7) fresh audit agent (opus).

## STATE (NEWEST, 2026-11-26, model now claude-opus-5-5 after the operator's /model switch) - G2 AUDIT REPORT ARRIVED: audit/G2_audit_engines.md (134 findings: 53 HIGH). WORKING IT.
- Disposition file to keep current: audit/G2_response.md (one row per finding: FIXED <commit> / ANSWERED <refuting canon line> / OPEN). Batch I DONE (commit 9e44b34): C-32 (V1 harvest with bars scaled to the
  chart's real tick: DXY x10, FX x1000; cache dir e1_tool/cache/v1s), D-01 (tools/leak_check.py in the pre-commit hook), D-02/D-04 (superseded modules -> tools/research/superseded/), D-03 (tools/research/oracle_diff.py), D-05.
- THE CENTRAL FINDING (B-08, B-03, B-04, B-05, A-09..A-11, C-07): Engine 2 is a FIXED WEEK TEMPLATE (SS x n -> SS+RWL+BS -> BS -> X; 5 day-maps over 40 weeks) = anti-pattern A2. NEXT = rebuild e2_chain forward mapping
  as a real chain extension: Step 1 matrix 6.2 on 1H (B-01/B-02, with ZFP conditions), Step 2-3 transitions 6.4 / 6.4.1 / 6.4.2 (reaction counter picks the branch, A-03) shape by shape with durations 6.8 and the
  consolidation phase / key rule (A-09/A-10), per-day ZFP with the Pillar 9 expiry-timing modifier (the canon mechanism that says WHEN a bound fails), 6-check direction (A-04), pressure reading (A-05),
  4H validation (A-06), TF element matching (A-07), triggers per day (A-08), termination < 25% with undesignated days not drawn (B-07/C-16), alternative chain with ZFP threshold + confidence, drawn (A-13).
  Then E3 phases (A-15..A-47, B-18..B-37, C-17..C-25), then the S/D findings (A-48..A-52, B-38..B-45, C-27..C-31), then a FRESH audit agent (model opus; the Fable auditor is rate-limited until Dec 2).
- Golden week must still come out (S2): re-check DXY / EURUSD / GBPUSD + Apr 20 after every step with the snapshot tool (scratchpad snap.py) and tools/research/oracle_diff.py.
- DONE (commit 2717f06): ENGINE 2 v2 = canon chain extension (memory/09 design; D-34..D-41). Golden DXY: Mon SS | Tue SS | Wed SS+RWL+BS down | Thu BS down | Fri BS+RWL (his: SS+BS, SS, SS+RWL+BS, ladder, WL+RWL).
  Apr 20: Mon-Tue SS, Wed SS+RWL+BS up, Thu BS up. Pairs mirror DXY on their own zones. Known E2 gaps: Aug 17 (no E1 zone below spot -> floor = sweep zone -> SS all week; E1 Step 9.5 gap scan missing in e1_ip),
  Jul 13 direction (tie -> storyline up; the week broke down), Sep 14 BS a day late. E3 still the old leg-chain code (golden DXY now 4 setups instead of 7).
- NEXT = ENGINE 3 v2 (memory/09 E3 part): candidates = the E2-designated (day, zone, side) tuples (legs) + the opposite side on SS days (E3C:96 'both directions'); Phase 2 gates (freshness, BoM/MoM + exceptions,
  POI tier), Phase 3 entries (F1-A on the OB itself, F1-D RWL only, F1-E), Phase 4 stops = rule (a)/(b) on liquidity steps incl. V1 4H bands (memory/08 stop model) + Law 7 buffers, TP rules (zone midpoint,
  strong/weak, no teleport, TF law, TP_NULL), Phase 5 confidence >= 65, Phase 6 chains/conflicts, Phase 7 sessions, Phase 9 2-3 reinforcements, Phase 10 mirror, Phase 12 reason codes. Keep his golden trades.

## STATE (NEWEST, 2026-11-26 night, after compaction 8) - S2 holds on DXY and now better on EURUSD / GBPUSD; S3 loop continues; G2 audit agent a2349814137719c02 still running (report: audit/G2_audit_engines.md)
- This step (commits 50a6a23, be33e66, 9a9..): E1: pre-anchor session bar as D1 data (D-25), last days scanned in Step 0 (D-26). E2: sweep-zone bound on an empty side (D-27), "MoM bound is the one pierced" (D-28), plan for a breakout running at the anchor (D-29),
  transition-day retest at the opposing liquidity band (6.4.2; e2_chain._opposing_liquidity). E3: TS-1 at a sweep bound + E2 bound as first anchor (D-30), Phase 6.3 dedup + mirror-lane collision retry (D-31), EUR/USD NO_SHIELD stop (D-32), weak-4H-zone TP rule 4 (D-33), RWL TP at the opposing liquidity, BS entry by Law 27.
- Golden week now: DXY 7/7 TP, DX5 BS short 101.235 = his 101.235. EURUSD 6 setups, 4 TP 2 SL: EU5 Wed BS LONG 1.13940 / 1.13872 / 1.14555 = his #6 (1.13953 / 1.13868 / 1.14544), EU3 = his #4. GBPUSD 6 setups, 3 TP 2 SL: GB5 Wed BS LONG 1.33255 / 1.33197 / 1.34254 = his #3 (1.3333 / 1.33199 / 1.34246). Apr 20 DXY unchanged (3 TP).
- FACT (memory/08 last section): his golden trades sit on the sealed V1's 4H LIQUIDITY BANDS (stops = rule (b) "1-2 pips inside the close edge of the next step" literally; TPs / entries at their near edges). E3 still uses 1H rungs only for steps.
- Frames opened + ledger: Oct 5 (66, 66b): top zone on the map, reacted twice; E2 5/5; E3 1 TP 1 SL. May 18 (67, 67b): ceiling + floor both reacted 3-4 times; E2 4/5; E3 0 TP 4 SL.
- DONE since the lines above: (A, part) e1_ip regime-change modifier only against the new regime -> May 18 floor = the wall zone 98.963-99.037; (E) Pine default view = the week's reach (show_far for the rest) + V1 4H liquidity bands (show_lq4); E3 labels next to their entry edge;
  frames opened: golden DXY (68b, unchanged on pixels), golden EURUSD (69b: both of his Wednesday longs present, EU5 = his #6 within 1.3 / 0.4 / 1.1 pips). memory/14b_GOAL_PROMPT_SHORT.md = the goal in 3987 characters (his /goal was refused for length).
  STILL OPEN FOR S2: a 15m frame of the golden-week entries (the IDE tab only loads the newest 5000 15m bars = from mid-September; pine-ide.mjs loadBarsInner has no end date; try the Backtest tab with the replay cursor at Jul 10); GBPUSD golden frame not yet opened with this code.
- NEXT, in order (each from its canon lines; golden week + Apr 20 must stay): (A) E2 floor / ceiling = the HOLDING structure (wall zone / BoM zone), not the MoM zone in front of it - check e1_ip ZFP modifiers (Pillar 9 Step 2) against P452:954-1000: why a Standard Wall gets >= 30;
  (B) E3 stops: code the model written at the end of memory/08 (rule (b), 1 pip inside the close edge of the first thick step = V1 4H band, or of the second thin 1H rung; hand-checked against all seven of his DXY stops) - then re-check every golden number; (C) order validity: void when the TP level trades before the entry (Law 27 sequence); (D) staggered three entries (E3C Phase 9);
  (E) Pine: default view limited to the week's reach (Law 2 / Law 7), far zones behind a toggle (frames are squashed by zones 100+ pips away), draw the V1 4H liquidity bands (his green bands); (F) remaining weak weeks Jun 8, Jul 13, Sep 14, Aug 17 with frames;
  (G) process the G2 audit; (H) S3 four weeks x three pairs with outside counting; (I) ship package + two blind sub-agents. Tool to diff any change: scratchpad snap.py (re-create if lost: prints zones / legs / setups per PAIR:MONDAY).

## STATE (NEWEST, 2026-11-26 late) - S2 holds on DXY (golden week: E1 + E2 + E3 match the oracle, ledger 53-58) and mostly on EURUSD (ledger 59-60). NOW IN THE S3 LOOP: same code on other weeks is still weak.
- Facts per week: `python3 tools/research/fills.py PAIR MONDAY` (day map, setups, what the candles did - for ledger rows only). Frames: `tools/e1render PAIR MONDAY 1H show_lv=false show_lq=false` (E1TAG=_x).
- Good: DXY 2026-07-06 (7/7 TP), DXY 2026-04-20 (3 TP, 0 SL, both of his real trades), EURUSD 2026-07-06 (4 TP, 1 SL). Weak: DXY 07-13, 09-14, 10-05, 08-17, 05-18, 06-08; GBPUSD golden week.
- Frame evidence/e1tool_DXY_1H_2026-07-13_all.png OPENED (not yet in the ledger): the week broke DOWN (Mon rally to 101.3 rejected at Upper Resistance under the unmitigated 4H BoM supply, Wed fell through the 4H BoM demand to Key Support 100.47-100.53 and bounced);
  my primary said BS up (storyline = most recent 4H origin zone = Friday's recovery demand); the ALTERNATIVE chain (decision zone Mid-Range Support fails -> BS down) was the one that played. Monday long 100.946 stopped by a 7-pip wick, then price went to its TP.
- NEXT (ordered): (1) E3 setups for the ALTERNATIVE chain too (canon 6.6 Step 4 mandatory alternative with its Decision Zone; drawn as conditional setups) and a storyline rule that weighs the unmitigated 4H BoM price is rallying INTO (BoM always reacts) - re-read P533 6.4.2, 1961-1983 and FA 8 first;
  (2) plan for S0 = BS in progress (Aug 17); (3) zones above spot when price sits over the whole map (May 18, Jun 8): canon gap scan 9.5 / BREAKOUT EXTENSION TARGET; (4) Law 7 MoM rule in e3 (no reversal swing at a MoM zone; scalps only);
  (5) GBPUSD; (6) four weeks x three pairs with opened frames + ledger rows; (7) outside audit (G2); (8) ship package + two blind sub-agents. Bug list with causes: journal entry "STATE OF THE SAME CODE ON OTHER WEEKS".

## STATE (NEWEST, 2026-11-26) - ALL THREE ENGINES REBUILT; GOLDEN WEEK DXY MATCHES THE ORACLE ON E1, E2 AND E3 (ledger 53-58). One command: `cd e1_tool && python3 plutus.py MONDAY PAIR` ; render `tools/e1render PAIR MONDAY 1H [toggles]`.
- Modules: e1_sd.py (supply/demand map) / e1_ip.py (IP zones) / e1_v1.py (V1 harvest) / e1_pine.py (Pine E1) / e2_chain.py (shape chain, legs) / e3_trades.py (trade chain) / plutus.py (all). Print: `python3 e3_trades.py MONDAY PAIR` (also shows distance to the oracle trades on the golden week).
- OPEN, in order: EURUSD golden week (breakout target + deep-shield entry; frames) -> GBPUSD golden week (bounds without option data) -> Apr 20-24 + two more weeks x 3 pairs (frames opened, ledger rows) -> outside adversarial audit of the code vs canon ->
  remaining coverage rows -> ship package + two blind sub-agents. Read the last three journal entries first.

## STATE (NEWEST, 2026-11-26 after compaction 6) - E1 on the golden week matches the oracle on DXY (zones, bands, rungs); S/D zones exact on EURUSD / GBPUSD too. NOW: E2, then E3, on the golden week (three pairs).
- Run: `cd e1_tool && python3 e1_sd.py MONDAY PAIR` (supply/demand map) / `python3 e1_ip.py MONDAY PAIR` (IP zones) / `python3 e1_v1.py MONDAY PAIR` (V1 harvest) ; render `tools/e1render PAIR MONDAY 1H [input=value ...]` (E1TAG=_x suffix).
- Oracle for all three engines and three pairs: context_management/oracle/golden_week.json (zones, rungs, Fib grids, 8 + 8 + 7 trades). Read the journal entry "(after compaction 6)" first.
- Next steps: (1) e2_tool: canon P533:1725-2057 day map + chain -> day boxes + line (R-03) vs his tags Mon SS+BS, Tue SS, Wed SS+RWL+BS, Thu ladder short, Fri WL+RWL; (2) e3: corrected spec on rungs (V1 bands + zone edges + zone Fib) vs his trades;
  (3) EURUSD / GBPUSD frames; (4) Apr 20-24 and two more weeks; (5) outside audit; (6) ship package + two blind sub-agents.

## STATE (NEWEST - supersedes the block below where they differ) 2026-11-26: steps 1-2 of the list below are DONE (e1_v1.py, anchor = Monday London open); step 3 e1_ip.py is WRITTEN and runs.
Open deltas on the golden week D1 (upper band 9 pips low), D2 (prior-week-low floor scores LIGHT: swing rule excludes the last two days), D3 (green bands vs V1 4H liquidity) - see the last entry of memory/05_JOURNAL.md. Fix each by re-reading its canon lines, then continue with step 4.

## STATE (NEWEST, 2026-11-26, written just before a compaction) - STANDING ORDER = memory/14_GOAL_PROMPT.md v2.1. Tasks: S1 coverage matrix written (memory/15), S2a oracle written; NOW ON S2b = E1 on the golden week Jul 6-10 2026 (DXY, then EURUSD).
READ BEFORE CODING: memory/14 (all), memory/08 sections "THE LIQUIDITY LADDER = THE SEALED V1's GREEN ZONES" and "THE APPROVED-RENDER E1 RECIPE", memory/15, context_management/oracle/golden_week.json.
EXACT NEXT STEPS (in order; each cites its authority; verify each against the oracle with a diff, then on an opened Pinebox frame):
 1. e1_tool/e1_v1.py (row E1-V1; R-30): for a pair + Monday, POST the sealed V1 source + the last 400 CLOSED bars before the anchor to http://127.0.0.1:9741/model (as tools/pine-probe.py does), for timeframes 240 / 60 / 30 / 15;
    parse model.boxes: bgColor #3179f5.. = demand order block, #f77c80.. = supply order block, #2E8B57.. = liquidity band; cache JSON under e1_tool/cache/v1/. Pinebox must be up (recipe in memory/11 section 6).
 2. e1_data.boundary_ms -> the canonical anchor Monday 02:00 New York (sidecar 'anchor_utc'; CLAUDE.md hard constraint; the V1 oracle match used 2026-07-06T06:00Z); daily() / weekly() must return COMPLETED days / weeks only; spot = last 1H close before the anchor.
    Re-check DXY Apr 20-24 afterwards (reference must stay reproduced).
 3. e1_tool/e1_ip.py (rows E1-P1..P9, E1-SY, E1-AS, E1-BM, E1-RC, E1-98): IP zones by the approved-render recipe (memory/08): seeds, score(p) across pillars (pivot 3/10 pips; MA cluster points on 1H/4H/D1/W1; options by tier with band; structural weights 2 / 1 / 0.5; round_psych; bonus),
    best-first with centres >= 0.15 apart, members in the tight band (operator: narrower; canon TIGHT 0.10), zone mechanics on 4H bars of 90 days (visits, strong reactions >= 0.50, BoM if last excursion >= 1.00, Engine 3 status, ladder step), Pillar 9 type + ZFP range (L-35) + regime points,
    MODERATE+ only, names by position vs spot, rank, six drawn; K anchored on the boundary spots (K = DXY / EURUSD^-0.576); pairs use their own strikes and pip scale (e1_pillars._u). Expected on the golden week: zones at ~101.19-101.29 and ~100.555-100.68 among the six.
 4. Supply/demand layer (rows E1-S0f, E1-S0g, E1-MTF, E1-S55; L-37, L-38): 4H Step 0f candles (BoM/MoM, mitigation) + 1H candles nested / precision + V1 order blocks per timeframe; core vs spike; join with IP zones per L-39.
 5. Step 0.6 intra-zone key levels; LSZ; option-strike targets; then e1_pine.py in trident_v8 form drawing: IP zones (name / degree / ZFP), S/D candles with TF + BoM/MoM + mitigation labels, V1 liquidity ladder, LSZ, strike lines. Render DXY Jul 6-10, open the frame, compare with g1 / g4, ledger row.
 6. E2 (boxes + line) vs his day tags; E3 (rung to rung, position boxes) vs his six trades; then EURUSD; then S3-S6.
Existing e1_tool code state: e1_pillars.py / e1_data.py / e1_pine.py reusable; e1_synth.assemble*, e1_zones.build, e2_shapes.py, e3_setups.py = my deviating partial build (replace, do not extend).

## STATE (NEWEST, 2026-11-26 after M-54..M-56) - STANDING ORDER = memory/14_GOAL_PROMPT.md v2. RESTART OF THE BUILD UNDER IT.
- What exists in e1_tool/ (E1 1H zones, e2_shapes.py, e3_setups.py, e1_pine.py) is a PARTIAL build that breaks the seven laws; keep what reproduces the Apr 20-24 E1 report, rebuild E2/E3 by the canon.
- NEXT STEP (goal prompt section 9): build memory/15_CANON_COVERAGE.md by reading, in full and first-hand: TTE_GOLDEN_STANDARD_COMPLETE_REFERENCE.md (Part 7 onward still unread), the corrected E3 spec (all phases + Appendix F), the Fractal Architecture, the Fibonacci Spiderwebs PDF,
  prompt Parts III-VI; then fix the golden-week oracle from his screenshots into context_management/oracle/golden_week.json; then work the anchor week Jul 6-10 2026 (DXY + EURUSD) row by row until S2 holds.
- Do not message the operator except per goal prompt section 11.

## STATE (NEWEST, 2026-11-26 end of this run) - pipeline complete E1+E2+E3, anchor week passes on pixels, but measured edge is at CHANCE level -> goal NOT met; reported to operator
- Read memory/05_JOURNAL.md entries dated 2026-11-26 (KEY FINDING, split test) and the UPDATE block at the top of memory/13.
- Latest commit on AGENT holds: 1H-worked zones with strict one-time use; E2 chain + alternative branch + pair translation; E3 scalps / reversals / transitions with arming and the 4H gate; Pine draws all three.
- If the operator says continue: use the BUILD/VERIFY split for every change (tools/research/e1_split_features.py, e23_all_weeks.py), never tune on all 40 weeks; candidate next source of truth = his WINNING_TRADE_LIBRARY (/home/user/inputs/trades) to check whether the tool's zones cover the entries he actually took.

## STATE (NEWEST, 2026-11-26, later) - ALL THREE ENGINES EXIST AND RENDER; QUALITY OUTSIDE THE ANCHOR WEEK IS LOW -> keep looping (memory/14 goal)
- Code: e1_tool/ e1_zones.py (E1, 1H zones + 4H overview) -> e2_shapes.py (E2 chain + day map + path) -> e3_setups.py (E3 setups + simulate) -> e1_pine.py (one Pine with toggles). Run `e1_tool/e1 MONDAY PAIR`; render `tools/e1render PAIR MONDAY [TF key=value...]` (E1TAG=_x adds a suffix to the frame name).
- Measure (facts for debugging, never quoted as accuracy): `python3 tools/research/e23_all_weeks.py DXY` (E2 day match + E3 results), `python3 tools/research/e1_first_touch_mfe.py DXY`.
- Latest DXY 40-week facts: E2 forecast day = classifier day 66/200, direction right 46/91; E3 18 TP / 38 SL / 65 not filled (after per-day anchor cap + 8.18 direction consensus + MoM trend rule). Anchor week Apr 20-24: E2 path matches the week; E3 LONG 98.05 -> TP 98.75.
- Open work, in order: E2 day shapes anchored to zone events and prior-week behaviour (current logic too crude, always "SS -> BS -> R"); E3 reversal shorts/longs at the BS target (Fri short at 98.75 on the anchor week was lost to the direction filter), reinforcements, entry timing 8.25;
  EURUSD/GBPUSD (pair translation: same shapes, inverted direction); pixel checks on 4 weeks; external adversarial review; ship package + two blind sub-agents (2 unseen weeks each).

## STATE (NEWEST, 2026-11-26) - STANDING ORDER = memory/14_GOAL_PROMPT.md. Phase P1 (E1 on 1H per L-40) in progress: e1_zones.valid_sd now uses 1H candles with 4H overview; reference week re-rendered (evidence/e1tool_DXY_1H_2026-04-20.png, 7 zones, Monday low on the 1H BoM demand 97.94-98.05). Next: finish P1 checks on a few weeks, then P2 (E2) and P3 (E3) on the anchor week DXY Apr 20-24.

## STATE (NEWEST, container clock 2026-11-25 ~22:05 UTC) - E1 PYTHON TOOL RUNS END TO END (see journal entry of the same time for everything)
- Run: `cd e1_tool && python3 e1_zones.py MONDAY PAIR` (zones) / `python3 e1_pine.py MONDAY PAIR > out/E1_PAIR_MONDAY.pine` (the Pine output) / `python3 e1_outcome.py MONDAY PAIR` (facts) ; render `tools/e1render PAIR MONDAY`.
- Zone assembly lives in e1_tool/e1_zones.py build() + gap_scan(); e1_synth.assemble*/__main__ are superseded.
- DXY Apr 20-24 reproduces the report's five zones on the same structures (frame evidence/e1tool_DXY_1H_2026-04-20.png). 13 week/pair frames opened; verdict: NOT uniformly 90% - weak in sell-off/breakout weeks. Never claim 90%.
- Next: e1_report.py audit printout; more weeks; morning report listing assumptions A1-A4 and the bad weeks. E2/E3 untouched (out of scope).

# 01 — CURRENT STATE (overwrite; keep under ~60 lines)
Updated: 2026-11-25 ~12:25 UTC (container clock)

## Where I am
- Phase: E1 BUILD, iterating in Pinebox. File: `indicator/plutus-vision-engines.pine` (engine layer; sealed V1 untouched at `indicator/plutus-vision-v1.sealed.pine`).
- Anchor guard DONE (`tools/anchor_guard.py`, pre-commit hook via core.hooksPath=tools/git-hooks, run-time assert in the script). Memory graph DONE (`tools/mem/mem q ...`).
- E1 engine today: higher-TF bars aggregated in-script; forecast frozen at Monday 02:00 NY; level set from pivots (W + 3 D), daily MA grid, prior-week fibs, price anchors,
  D1 + 4H swing-reaction clusters (repeats / role reversals), HWC/LWC, round grid; confluence-weighted; zones = confluence peaks (suppression = 0.15 from a zone's edges);
  weekly map = zones overlapping the prior week's range + first zone beyond each end; canon gap in-fill (gap >= 0.20); 4H origin-candle S/D by zigzag (0.5 and 0.3); POI tier; ZFP from zone type.
  Inputs: i_anchorHour, i_weeks (2), i_back (look back N weeks), i_showE1, i_showSD, i_showAudit.
- GOLDEN WEEK DXY (frame evidence/bt_017): PASS as a dev oracle - ceiling 101.17-101.29 = week high, floor 100.53-100.63 = week low, EQ 100.92-101.02 pivot, in-fill 100.76-100.81 = Thu low.
- HELD-OUT Apr 20 week DXY 4H (frame evidence/ide_035): 12 zones over 97.4-99.35 = TOO DENSE (report oracle has 5 IP zones + 6 LSZ). My thin zones coincide with the report's LSZ and zone edges
  (98.53-98.58 exact, 97.63-97.72, 97.83-97.93, 97.94-98.03, 98.72-98.77 + 98.91-98.96 = edges of the report's 98.77-98.99) -> I am emitting LSZ-grade structure as IP zones.
- KEY INSIGHT (computed by hand, not yet in code): the golden-week EUR/USD option walls convert to the DXY levels the operator drew:
  K = DXY_spot * EURUSD_spot^0.576 = 101.025 * 1.1423^0.576 ~ 109.07; strike 1.1500 (EUR2.4bn) -> DXY 100.63 = the FLOOR and the week's low; 1.1400 (EUR2.2bn) -> 101.14 = his Monday short level;
  1.1450 (1.4bn) -> 100.89; 1.1300 -> 101.66. So option walls are what separate true IP zones from liquidity rungs. The web sidecar is REQUIRED for accuracy, not optional.

## PROGRESS since the block above (12:55)
- Option-wall dataset input is IN the Pine (`i_optData`, `i_anaData`; rows `YYYYMMDD|price:code,...;`, codes 1 live >=1.5bn, 2 live 850m+, 3 ghost >=1.5bn, 4 ghost 850m+). Walls (codes 1-3) seed zones first;
  structure: HEAVY peaks need only non-overlap, MODERATE-HEAVY peaks need 0.15 clearance; one-pass gap in-fill; ZFP by zone type (Hard 5-15, Standard 15-30, Ghost 20-40, Soft 30-50, One-Touch 50-70).
- Sidecar BUILT by an agent and still filling weeks in the background: `sidecar/run --week YYYY-MM-DD`, `sidecar/build-inputs` -> `sidecar/out/pine_inputs.{DXY,EURUSD,GBPUSD}.txt` (+ analyst). Done so far: 2026-04-20, 05-25, 06-29, 07-06, 11-02.
  Jul 6 output matches the hand-verified control. (Agent id a544407069ad54702 - it reports when finished; check `ls sidecar/out`.)
- FRAMES: golden week DXY with walls = PASS (evidence/bt_040, ide_043); golden week EURUSD = PASS (ide_042); held-out Apr 20 DXY 4H = PASS ~5.5/6 (ide_041); held-out Jul 13 DXY 1H = PASS 5/5 (ide_050).
- Sidecar has 15 weeks compiled (`sidecar/build-inputs` -> DXY/EURUSD strings; GBPUSD nearly empty: few GBP strikes >= 850m). E2 plan written: memory/09_E2_E3_PLAN.md. E2 NOT started.
- Backtest tab fixed (LS-15): V1 removed from this instance's room script store; engine no longer starves.

## BUILD STATUS (update this block as the tool grows) - job spec is memory/11_E1_BUILD_BRIEF.md
- e1_tool/e1_data.py DONE (bars, boundary, daily, weekly). e1_tool/e1_pillars.py: pillar1 DONE + verified; step0f DONE, matches the report's 4H zones structurally (journal 21:45).
- DONE + checked (journal 22:00): step0_swings (0b/0c/0h grades), step045_lsz, step05_magnets, pillar2 (MA grid), pillar6 (fibs, round numbers), k_factor / strike_to_dxy / tier (all 8 report strikes reproduce exactly).
- e1_tool/e1_synth.py WRITTEN, first run OK (journal 22:15): run `cd e1_tool && python3 e1_synth.py 2026-04-20`.
- STATUS 23:10: e1_synth.assemble_anchored() = zones built from structures (closest in kind to the report); finish items a)-e) in journal 23:10, then report printout, Pine generator, Pinebox render + compare, other weeks/pairs, morning report.
- (older) STATUS 22:50: synthesis runs; ceiling matches the report; role selection for the other four zones still off - diagnosis and next fixes in journal 22:50 (equilibrium first at spot; separation on level spans; re-read scoring table).
- NEXT, in this order (details in journal 22:15 and 22:50): (1) 4H zone noise rejection + unmitigated-only joining; (2) five-role naming (A3); (3) sweep zones per A2; (4) Step 0d/0e D1 order blocks + Step 1 HWC/LWC;
  (5) expiry loader with Day-1 page + Day-2 forward rows; (6) e1_report.py printout in the report's section order; (7) e1_pine.py (trident_v8 form + L-39 rendering); (8) render Apr 20-24 DXY in Pinebox, open the frame, compare with the original;
  (9) other weeks and EURUSD / GBPUSD; (10) morning report for the operator: what matches, what differs and why, the assumptions A1-A3, frames.
- Assumptions made so far (list for the operator's morning report): A1 strong move = inefficiency gap (journal 21:45). A2 sweep zones from every D1 swing + last-5-day lows/highs, wick test = grade only (journal 22:00). A3 five-role selection of synthesis zones (journal 22:15).

## STATE (NEWEST) - TASK = TRANSLATE THE PROMPT'S E1 INTO PYTHON (04 L-30..L-34). Read memory/10_FAILURE_RECORD.md first.
- Done: read E1 first-hand in P533 (lines 802-1163, 1163-1340, 1341-1514) and P452 (637-1205). Pseudocode with line refs: `e1_tool/E1_PSEUDOCODE.md` (committed).
- Reference to reproduce: Leviathan_DXY_IL_Report_Apr20-24_2026.pdf (upload 5212e9bd; pages 1-6 read: option tables, K factor, pivots, 5 IP zones, 4 4H zones with origin candle OHLC, 6 LSZ, clustering scan)
  and Original_Canon_Data/Pine Scripts/trident_v8.pine (output form). Frames of the original: evidence/trident_v8_original_*_allzones.png.
- ALL OPEN POINTS ANSWERED (04 L-35..L-39): ZFP shown as the prompt's RANGE; no minimum move size (every 4H leg origin = BoM zone, continuation base = MoM, 0.5/3d and 1.0/5d grade strength);
  S/D zone = the candle BEFORE the strong move, boxed wick high to wick low on TradingView candles; a pressure zone = candle structure + level cluster JOINED, with the levels and the candle part
  drawn distinctly inside it; where levels cluster without an order block, draw the pressure zone AND the sweep zone, colour-coded.
- NEXT: write the Python tool in e1_tool/ from E1_PSEUDOCODE.md, one function per prompt step, TradingView bars (Pinebox store / TV API) + investingLive expiries (sidecar raw data exists for 40 weeks);
  output = report data + Pine in trident_v8.pine form. FIRST TEST = Apr 20-24 2026 vs the report, zone by zone. Nothing else.
- Pinebox dies on every session restart: `pinebox down; pinebox up --session plutus-main --adapter xvfb` before rendering. Price-axis fit snippet is in the journal (setManualScale on resolveScaleHolder).
- E1 v3 code still sits in indicator/plutus-vision-engines.pine (rejected). E2/E3 off. Do not build anything else.

## STATE (NEWEST, after the operator's rejection of E1 v3) - STOP: NO CODE, NO AGENTS until he approves (04 L-27, L-28)
- The workflow wf_13ddfb31-159 (e1-zone-mechanics-redesign) was killed by the operator. Do not resume it unless he asks.
- I gave him the gap analysis: prompt vs GLM W14 report vs my engine (06 LS-25 lists my inventions and the prompt's actual rules with line numbers).
- The Pine file still holds E1 v3 (f_pick: merge touching zones, nearest per side + wall rule, measured ZFP). He rejected it. Leave it until he says what to build.
- When he approves: implement the prompt LITERALLY - Step 0f single-origin-candle S/D zones as real candle [Low, High]; BoM/MoM + reaction counter on every zone; 0.10-0.15 clustering;
  degree = highest-scoring level (6 dimensions + structural-extreme bonus) + POI tier; MODERATE and above only; no trimming / padding / merging / caps of my own.
- Known concrete defects to fix first: (a) Oct 5 DXY demand zone 101.71-101.77 existed in the engine but was cut by my 2-per-side cap; (b) Oct 5 top zone was a LIGHT gap in-fill (score 5) drawn although the prompt
  shows MODERATE+ only, and it got no structural-extreme / round-number / 4H-BoM credit; (c) Jul 27 three supports with 1-2 pip gaps should have been ONE cluster by the 0.10-0.15 rule.

## STATE 16:40 UTC (NEWEST) - E1 v3 is in the Pine file and shown to the operator; waiting for his verdict. E2/E3 OFF.
- RULE NOW IN indicator/plutus-vision-engines.pine (f_pick after f_zones): touching zones merge into one (union of evidence); DRAWN = the zone price sits in + nearest zone each side
  + the next one out on a side only if an option wall sits in it. Switch `i_wallOnly` = only zones holding a tier-1 wall (>= $1.5bn live or ghost).
  Zone extents are the evidence's own (median 10 pips on DXY, like his hand-drawn bands). ZFP = measured share of first tests of that zone class sliced through on the chart before the anchor
  (zTouch/zBreak; bookkeeping after each anchor uses the L-23 definition with m = mean bar range). The fixed-width band code (f_bands) is GONE.
- SCORER THAT MATCHES HIS EYE: tools/research/score2.py (REJECT / CONSOLIDATE / SLICED; week verdict VALID when reactions >= slices). Calibration: his golden bands 3/3 valid; W14 bands 0.90; rejected v1 map 0.37-0.54.
- NUMBERS (4H dump zones, 3 pairs): ALL 40 weeks: touched zones valid 0.957 (308 of 322), lenient 0.951, strict (untouched count against) 0.784, FIRST-TOUCH reaction 0.814, 3.3 zones/week.
  TEST 8 weeks: 69 of 69 touched valid, first-touch 0.75. Tier-1-only: first-touch 0.874 all weeks (0.92 DEV, 1.00 VALID, 0.76 TEST), 1.8 zones/week, GBPUSD almost empty.
  KEY FINDING: a zone holding a tier-1 wall reacts on first touch 95% (n=58, DEV+VALID nearest/second zones); tier-2 81%; no wall 75%. Institutional data is what lifts first-touch.
- FRAMES OPENED AND LOGGED: 07 rows 31-39 (golden 4/4; DXY Aug 31 3/3, Oct 5 3/3, Jun 15 2/3, Jul 27 partial; EURUSD Aug 31 3/3, Jul 27 3/4; GBPUSD Oct 5 pivots). By my eye ~24 of 28 touched zones valid.
- WEAK POINTS TOLD TO THE OPERATOR: breakout/news candles slice zones (Jun 15, Jul 27); after a breakout price trades where nothing is drawn; strict first-touch is 81%, not 90%; GBPUSD has almost no >= $850m strikes;
  only investinglive feeds the walls (forex.com / ING / FXStreet hosts are blocked) - more institutional sources is the lever for first-touch.
- NEXT (after his verdict): if approved -> single-file delivery with sealed V1, then E2. If not -> his specifics. Ultracode feature hunt (02 queue) still available with score2 as the metric.

## STATE 14:15 UTC (container clock; newest) - metric and width rules now come from the operator (04 L-22..L-26)
- Failure = price SLICES THROUGH a zone with no reaction. Sharp rejection OR consolidation in/around the zone = valid. Pivot zones valid. Width = extent of the zone's own evidence, never a constant. Draw only what qualifies.
- So: E1 v2's fixed-width bands (0.3 x weekly range) are rejected; go back to evidence-derived extents (v1 had them) but with far better selection, and score with REJECT / CONSOLIDATE / SLICED.
- TODO now: (1) tools/research/score2 with the L-23 definition, sanity-check on his golden-week bands (101.19-101.29 reject, 100.94-100.985 pivot, 100.545-100.675 reject) and on the W14 bands;
  (2) measure slice-through rate per evidence type with evidence-derived extents; (3) redesign selection; (4) Pine; (5) frames I have actually opened, on 4 unseen weeks, to the operator.
- The blank frame: re-render the golden week and LOOK before sending anything.

## STATE 16:15 UTC - metric fixed by the operator: FIRST-TOUCH REACTION >= 90% (L-19). Width is the open trade-off.
- His hand-drawn bands are ~10-13 pips wide on DXY. Current E1 v2 bands are 0.3 x weekly range (~36 pips): on the golden week mine are 101.25-101.61 / 100.49-100.85 / 99.90-100.26
  vs his 101.19-101.29 / 100.545-100.675 - right places, three times too wide (frame evidence/ide_110_e1v2_dxy_1h_golden.png).
- MEASURED (DEV, reaction = 0.1 x weekly range): thin bands on the week's option walls: total width 0.08 / 0.12 / 0.16 x weekly range -> first-touch 69 / 72 / 78%;
  tier-1 live walls 70 / 74 / 78%; walls confirmed by 2+ price-action structures 74 / 73 / 80%. 90% needs ~0.3 width (or a smaller reaction threshold).
- Asked the operator: (1) width vs hit-rate, (2) what size of bounce counts as a reaction, (3) whether a pivot band (like his middle one) may be drawn. His answers decide the tuning.
- Golden-week walls for reference: 100.64 tier-1 (inside his bottom band), 101.28 ghost tier-1 (inside his top band), 101.14 tier-1, 100.89 tier-2, 101.40 tier-1.

## STATE 15:45 UTC - E1 v2 IS IN THE PINE FILE; IT DOES NOT REACH 90%; operator has been told the measured limits
- indicator/plutus-vision-engines.pine now draws the E1 v2 band map (f_bands / f_band / f_wscore; freeze block calls f_bands; old f_zones is unused code kept for comparison).
  <= 2 bands above + 2 below the anchor price, width 0.3 x mean weekly range, taken at the nearest window (>= 0.15 away) whose extreme-type evidence >= 5
  (fresh 4H origin zone 3/2, tier-1 wall 3, tier-2/ghost wall 2/1, prior-week high/low 2, repeated swing extremes 1-2, daily highs/lows 0.5).
  Label: "R1 Supply | BoM|MoM | n rx | ZFP% | score/14". ZFP = measured: share of first tests of that band role traded through on the chart before the anchor (bTouch/bBreak, Laplace).
  Bookkeeping of band tests runs bar by bar after each anchor and feeds only later weeks. Guard allow-list got 0.3/0.15/0.12/0.02/0.1 (band geometry fractions).
- Scorer numbers for this rule (python prototype tools/research/proto2.py, k.30 thr 5): DEV first-touch hold 0.91, clean-all-week 0.63, week extremes inside a band 0.49, 2.9 bands/week;
  VALID first-touch 0.78, clean 0.44, extremes 0.29. Frames on 4 unseen DXY weeks (07 rows 27-30): 1 PASS, 1 PARTIAL, 2 FAIL.
- Bands fixed DAILY at London open and judged over one day are no better (first-touch 68-81%, clean 47-70%): the limit is scale-free, re-anchoring daily does not fix it.
- OPEN DECISION put to the operator (he must answer): his bar "zones not penetrated, 90-95%" was set by the W14 report, which was written with its week's data. Forward, measured ceiling is ~60-70% clean.
  Untested ideas that might add a few points (not 30): trend/regime conditioning of which side gets bands; multi-month weekly/monthly swing extremes as anchors; a multi-agent feature hunt (ultracode) after the usage reset.
- E2/E3 stay OFF (L-14).

## MEASURED LIMITS (15:25 UTC) - read before designing anything else (24 DEV weeks x 3 pairs, tools/research/score.py)
- A band HOLDS ON FIRST TOUCH ~80-91% of the time wherever it is put within reach (structure-free bands at 0.2-0.5 x weekly range from spot, width 0.2-0.3 x weekly range).
  Best level types (band +-0.125 x weekly range): fresh 4H supply (visited <= 1x) 93%, prior week high 91%, yesterday high 91%, D-2/D-3 lows 91%, MA100 90%, tier-1 option wall 88%, prior week low 87%.
  Worst: MA9 72%, yesterday low 76%, RN 77%, MA20/MA50 78%, role-reversal clusters 79%.
- A band stays UNTRADED-THROUGH ALL WEEK only ~57% of the time (base rate); the best level type reaches 70% (MA50 70, fresh 4H supply 69, tier-1 wall 68). Nothing reaches 90%.
  => "no zone gets penetrated during the week, 90%" is not reachable forward with these features; "reacts on first touch >= 90%" is.
- Touch rate falls with distance: band centre at 0.2 / 0.3 / 0.4 / 0.5 / 0.6 / 0.75 / 0.9 x weekly range from spot is touched 88-96 / 72-81 / 58-62 / 43-53 / 37-40 / 26-31 / 16-20 % of weeks. Bands beyond ~0.5 mostly float.
- My old confluence-density selection was WORSE than structure-free geometry (hold 0.72-0.80 vs 0.85-0.88): dense confluence = congestion = traded through. Do not select by density.
- Reference numbers: structure-free 4-band map (spot +-0.35/+-0.8, width 0.3) scores accuracy 0.52, hold-on-touch 0.875, week extremes inside a band 56%.
  W14 hindsight bands 0.75. Current engine 0.35. Prototypes live in tools/research/proto.py (usage: python3 proto.py DEV|VALID).
- Design direction for E1 v2: <= 4 wide bands; inner pair at ~0.2-0.45 x weekly range (labelled MoM / pivot, ZFP ~ measured), outer pair only where a strong anchor exists
  (fresh 4H BoM supply/demand, tier-1 wall, prior week high/low); ZFP = measured failure frequency of that band role over the prior weeks on the chart itself (self-calibrating, no constants).

## RESUME HERE (written 15:00 UTC, just before a usage-limit reset) - exact state and next actions
WHAT IS TRUE
- Operator rejected E1 (04 L-14..L-18). E2/E3 are OFF by default and FORBIDDEN until E1 is approved. Target = W14 report format: <= 4 wide bands per pair.
- A research scorer now exists and AGREES WITH THE OPERATOR'S EYE: `tools/research/score.py` (run `python3 tools/research/score.py`).
  It walks the week's 1H bars and gives each band HELD / BROKEN / CONTAINS / BOUNDING / FLOATING; D = 0.10 x mean weekly range (13 wk).
  accuracy = good / (good + broken + floating + missed week extremes).
  MEASURED 15:00: current engine maps on the 24 DEV weeks x 3 pairs = 35.1% (HELD 273, BOUNDING 110, BROKEN 157, FLOATING 493, missed extremes 59 of 144; 0 weeks >= 90%).
  The W14 report's own bands (written with hindsight, LS-20) score 75% (DXY 4/4, EURUSD 2/4, GBPUSD 3/4).
- Level dumps for research: `tools/research/levels.{DXY,EURUSD,GBPUSD}.json` (git-ignored; regenerate with `python3 tools/research/dump_levels.py`, needs Pinebox up).
- Week split (never show TEST to a design loop; TEST is for my own Pinebox frames): TEST 2026-02-23, 03-23, 04-27, 05-18, 06-15, 07-27, 08-31, 10-05 ·
  VALID 02-16, 03-09, 04-13, 05-11, 06-22, 08-03, 09-14, 10-26 · DEV = the other 24 weeks (list in score.py).
- Frames of the W14 report bands: evidence/oracle_w14_report_zones_{DXY,EURUSD,GBPUSD}_1h.png (outer bands contain week high/low; middle bands crossed).
- Scratch helper for memory writes (hook-friendly): overwrite and run scratchpad/mem_update_1435.py (LS-22).
NEXT ACTIONS (in order)
1. Prototype the E1 v2 band rule in Python against score.py on DEV weeks only (cheap loop): <= 4 bands per week, 2 above spot + 2 below (or one containing spot),
   bands WIDE (DXY ~0.15-0.30, pairs scaled by weekly range), built from: prior-week high/low/close zones, 4H/D1 supply-demand origin bases (BoM/MoM),
   repeated D1 swing extremes, round numbers, option walls (live + ghost). Pick the band nearest price on each side that is strong, then the next one out;
   no band further than the week can reach. Compare against two reference maps: W14-style hindsight ceiling and a naive baseline (prior week high/low bands).
2. Confirm on VALID weeks (no retuning there). If >= 85-90% on the scorer: port into `f_zones` in indicator/plutus-vision-engines.pine (labels: Supply/Demand, BoM/MoM, reactions, ZFP, x/14),
   anchor guard must pass, render 4 TEST weeks x pairs with `tools/pb week`, LOOK, log frames in 07, show the operator.
3. If a multi-agent design search is wanted (ultracode was on): 4 designers with different lenses on DEV + one validator each on VALID, all importing tools/research/score.py.
   NOT launched before the usage reset on purpose (a reset kills running agents, see 06).
4. ZFP must be mechanical (L-16): BoM vs MoM, reaction count over prior 3 weeks, option wall tier, confluence -> canon base range + modifiers; show its parts in the audit.

## STATE 14:35 UTC - READ THIS BLOCK FIRST (operator intervention; see 04 L-14..L-18, 06 LS-19..LS-22)
- E1 is REJECTED by the operator (30-50% by his eye). E2/E3 are FORBIDDEN until E1 is approved; both are OFF by default in the file.
- Target = W14 report format: <= 4 wide bands per pair (2 supply above, 2 demand below; one may contain spot), each with Type, BoM/MoM, Reactions, mechanical ZFP, Confl x/14, key level. No thin stacked zones, no far floating zones. Acceptance: >= 90% on 4 separate weeks, judged by eye in Pinebox.
- The W14 report itself was written with its week's data (LS-20): its format is the target, its numbers are not a forward score. Operator has been told.
- In progress: design search for E1 v2 band selection (research files in scratchpad research/, scorer research/score.py). Then port the winning rule into f_zones (Pine), render TEST weeks, look, iterate.
- Tools: tools/pb week PAIR TF MONDAY NAME [K=V] (IDE render of one week with the pair's dataset); oracle render probe indicator/probes/report_w14_oracle.pine.

## UPDATE 14:05 UTC (supersedes the lines above where they differ)
- E1 held-out strict reaction scores: DXY Feb 9 50, Mar 16 65, Apr 20 92, May 25 75, Jul 13 100, Aug 10 90, Sep 7 70, Sep 28 62, Oct 19 70 (mean ~75); EURUSD Apr 20 75, Sep 7 93. Golden week DXY + EURUSD PASS.
- E1 scope is now the reach band (spot +- mean weekly range of 13 weeks, union prior week range) + outer gap in-fill. Reaction counter = audit only (does not discriminate). `tools/pb week PAIR TF MONDAY NAME [K=V]` renders one week with the pair's dataset.
- E2 v0 is in the file (f_e2) but FAILED its first frame (Apr 20). E3 not started. Sidecar complete (28 weeks).

## NEXT STEP (in order)
1. GBPUSD: 2 held-out weeks (structure only; dataset nearly empty). Then commit.
2. E3 from the corrected doc (read context_management/spec/E3_ALGO.md phases + constants): zone-edge setups as position boxes, <= 11 per week; verify fills on golden week + 3 held-out weeks.
3. E2: rework the walk per E2_ALGO 3.3 (ZFP-conditioned), verify 4 weeks, report measured day accuracy honestly.
4. Single-file delivery `indicator/plutus-vision.pine` (sealed V1 bytes + engines) via tools/build-indicator.sh with sha check of the V1 region.
5. Final report: scorecard table, what passes, what does not.

## OLD NEXT STEP (done or superseded)

1. When the sidecar finishes: `sidecar/build-inputs`; validate E1 on >= 8 more held-out weeks across DXY / EURUSD / GBPUSD with each pair's own dataset
   (IDE 4H: `DS="$(cat sidecar/out/pine_inputs.DXY.txt)"; tools/pb ide indicator/plutus-vision-engines.pine DXY 4H i_back=N "i_optData=\"$DS\""`; week N weeks before 2026-11-02).
   Score each by reaction (L-07); log every frame in 07_EVIDENCE_LEDGER. Do NOT tune on held-out weeks; mechanism fixes only.
2. EURUSD golden week vs the operator's screenshots (his demand 1.1400-1.1417, supply 1.1446-1.1456; walls 1.1400 2.2bn, 1.1450 1.4bn, 1.1500 2.4bn).
3. Presentation: labels overlap at the left edge of each week; put the label inside the box / right-aligned; LSZ toggle.
4. Build the single-file delivery `indicator/plutus-vision.pine` = sealed V1 bytes + engine layer (script `tools/build-indicator.sh`, sha-check the V1 region).
5. E2 (context_management/spec/E2_ALGO.md): shape chain from E1 zones + ZFP; then E3 (E3_ALGO.md), <= 11 setups/week.

## How to render (measured recipes)
- IDE tab, full history: `tools/pb ide FILE PAIR TF [i_back=N ...]` then `tools/pb goto FROM TO` then `tools/pb shot NAME chart`. (IDE default runs only 400 bars - LS-12.)
- Backtest tab: `tools/pb export FILE`, `tools/pb bt-apply "Plutus Vision Engines"`, `tools/pb wait-engine`, `tools/pb goto FROM TO bt`, `tools/pb shot NAME full` / `shotc NAME`.
  Works at cursor Jul 10 (8861 bars); at Nov 6 (10858 bars) the added script never prepared (cause not found) - use the IDE for late dates.
- Preflight only: `tools/pine-probe.py FILE --tf 4H --limit 3000 --inputs '{"i_back":28,"i_showAudit":true}' --dump /tmp/x.json`.
