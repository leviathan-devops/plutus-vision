# G2 outside audit, round 2: code vs canon (Engine 2, Engine 3, S/D map, drawing, entry point)

Auditor: independent, read-only. This audit checks fidelity only: the canon is taken as correct, and the strategy is not judged.
Baseline: commit **9cdfbc0**. Every file was read through `git show 9cdfbc0:<path>`, and every code line number refers to that commit.
`e1_tool/e1_sd.py` is byte-identical to the round-1 baseline (md5 5f57756b…). Its round-1 line numbers still hold.

Abbreviations:
- **P533** = canon/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md (Part VI = lines 1725-2057).
- **E3C** = canon/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md.
- **P452** = e1_tool/canon_extract/P452_FULL_Trident_System_Prompt_v4.5.2.md.
- **GS** = handover 03_HOST_BIBLES/TTE_GOLDEN_STANDARD_COMPLETE_REFERENCE.md.
- **SPW** = /home/user/inputs/4d1ca379-Fibonacci_Spiderwebs.pdf (read with pdftotext).
- **RUL** = memory/04_OPERATOR_RULINGS_LIVE.md. **GP** = memory/14_GOAL_PROMPT.md.
- **R-07 / R-10** = handover Appendix A (00_HANDOVER/PLUTUS_VISION_CONTEXT_HANDOVER.md:717-735).
- Code file names: e2 = e1_tool/e2_chain.py, e3 = e1_tool/e3_trades.py, sd = e1_tool/e1_sd.py, pine = e1_tool/e1_pine.py.

Verdicts:
- **CLOSED**: the defect named in round 1 is gone from the code.
- **PARTLY**: something was built; what is still missing is named.
- **STILL OPEN**: no effective change.

---

## Section 1 — earlier findings (round 1 = audit/G2_audit_engines.md; builder's state from audit/G2_response.md in brackets)

### A — canon steps with no code

| id | verdict | deciding code / canon |
|---|---|---|
| A-01 [PART] | PARTLY | WLS is only a Step-1 label (e2 423-430). It never becomes a chain step: e2 506 treats it as 'ss' mode. P533:1816 'WLS → BS VERY HIGH' and Rule 7 (P533:1927) have no code. E3 CAT (e3 23) has no WLS row (E3C:106). |
| A-02 [OPEN] | STILL OPEN | Only 'PWL' exists, as a Step-1 label (e2 415). SS(DWL), RS and PRWL are never produced. The universe rows E3C:97, :101, :105 cannot be reached. |
| A-03 [FIXED] | CLOSED | branch() e2 187-212 reads the counter through info() (e2 98-107), per P533:1868-1871. |
| A-04 [PART] | PARTLY | six_check() (e2 280-300) runs only for mode 'ss' with a chosen bdir (e2 530). E3C:1084 says "For every setup, run the 6-check", but E3 has none. The "or REJECT if no reversal pattern exists" (E3C:1093) and the size adjustment (E3C:1095) are missing. |
| A-05 [FIXED] | CLOSED | pressure_bias() e2 254-277 is used at e2 523-529 (thresholds: N-30). |
| A-06 [FIXED] | PARTLY | e2 503-505 only writes an audit string. Neither the bounds nor the Step-1 shape change when 4H "rejects". P533:1735 says "Validates SS range boundaries and BS direction". |
| A-07 [PART] | PARTLY | The E2 test (e2 322) contradicts P533:1969 (see N-11) and is skipped when src_tf is None. E3 _target has no TP-timeframe test (E3C:350, :1033). |
| A-08 [PART] | PARTLY | _triggers e2 479-483 gives the expiry cuts plus 'red folder: NO DATA'. Auctions (P533:693) are neither read nor marked NO DATA. |
| A-09 [PART] | PARTLY | A phase is computed (e2 466), but Late is defined wrongly (N-17). e3_trades.py never reads a phase, so no setup type is restricted (E3C:1129-1136). |
| A-10 [FIXED] | CLOSED | _strong_4h_near e2 472-476, used at e2 592-594. |
| A-11 [FIXED] | PARTLY | Coded: R→BS 2nd leg (e2 652-654), WL→RWL, RWL→SS. Not coded: RWL→BS new dir, R→WL/RWL "Recovery reaches opposing IP zone", WL→SS, SS→WLS, WLS→BS/SS, BS→PBS "extreme momentum" (P533:1805-1817). |
| A-12 [FIXED] | CLOSED | e2 498. |
| A-13 [PART] | PARTLY | The alternative chain is built (e2 787-802). E3 ALT_SETUPS = False (e3 17), so E3C:1035 is not served. |
| A-14 [FIXED] | CLOSED | e2 551 (per-extension trail) and e2 604 (raw/adjusted). |
| A-15 [PART] | PARTLY | There is no WorkingDayMap and no keyZoneId validation (E3C:115, :124). The spill-over (e2 666-672) applies to the last chain step only. E3C:123 says "for each day". |
| A-16 [PART] | PARTLY | e3 440-441 gates only supply/demand anchors (mit ≥ 3). The reactions of IP-zone anchors are not gated. The battle-time test is outside the tool. |
| A-17 [OPEN] | STILL OPEN | No retest count. E3C:1007 and E3C:1150-1155 have no code. |
| A-18 [PART] | PARTLY | e3 442 gates Reversal / HTF non-BS at MoM only. mech['e3_status'] and mech['mom_exceptions'] are never read in e3. Swing scalps and BS at MoM pass with no "ALL 4 exceptions" test (E3C:1006). |
| A-19 [OPEN] | STILL OPEN | z['tier'] is read only by e2 476. E3 has no POI-tier gate (E3C:1001). |
| A-20 [PART] | PARTLY | e3 319-322 (layer 3) and e3 326-328 (layer 7, but +5 / 0 instead of the +5 / −5 of E3C:245). Layers 1, 2, 4, 5 and 6 are missing. |
| A-21 [FIXED] | PARTLY | Score and gate at e3 308-343 and 563. Quality at e3 565 emits STANDARD (N-04). GOD_TIER is unreachable. |
| A-22 [FIXED] | PARTLY | mirror score e3 223-236 and ZR-6B e3 290-299 exist. Fuel never selects the relevant zone, against E3C:258-260 ("fuel INTACT → LQZ SHIELD_FUEL / ABSORBED → S/D PRESSURE_STRUCTURE"). RR-tight includes (b) shields (e3 294), whereas E3C:285 says "RR-tight (3p back edge)". |
| A-23 [PART] | STILL OPEN | LAW7 (e3 202) is never referenced. All buffers are the fixed 3 / 1 pip of e3 264, 269, 276, 282. The response's claim ("used as the rule (a)/(b) distances") is not true at 9cdfbc0. |
| A-24 [OPEN] | STILL OPEN | No reaction-extreme / util-guard / wick-clear fallback (E3C:289-294). |
| A-25 [FIXED] | PARTLY | The Law-14 blocker exists only in the SS/R TP branch (e3 174-180). The BS, RWL and WL branches (e3 103-144) have no sequential-path test, although E3C:1008 says "every setup MUST map sequential zone path". IP zones with 0 reactions are never blockers. |
| A-26 [FIXED] | CLOSED | MAX_RRR at e3 205 and 506-516; reinforcements at e3 655. |
| A-27 [PART] | PARTLY | front / back / blended RRR are recorded (e3 532-548). There are no middle or back fills, no SL cascade, and no gate on the blended RRR. |
| A-28 [PART] | PARTLY | The hair-miss repair (e3 500-505) is applied to RWL only. F1-E has no code. |
| A-29 [OPEN] | STILL OPEN | No Fibonacci spiderweb in the three contexts (E3C:205-209). |
| A-30 [PART] | PARTLY | The F1-C rung is used (e3 87-90). E1 intra-zone key levels ('intra') are not read anywhere in e3 (grep). |
| A-31 [FIXED] | CLOSED | e3 572-582. |
| A-32 [OPEN] | STILL OPEN | day = c['days'][0] (e3 549). The 12-step assignDay (E3C:483-555) is absent. |
| A-33 [OPEN] | STILL OPEN | No deferral. Setups do not carry the NO DATA marker. |
| A-34 [PART] | PARTLY | The label exists (e3 208, 549). Validity covers the whole day (e3 684-688, 700). There is no session bracket (E3C:77) and no liquidityScore filter (E3C:573-576). |
| A-35 [PART] | PARTLY | The reach is measured from the bound edge, not from spot (N-18). Non-SS shapes have no reach table (GS:36-40). |
| A-36 [OPEN] | STILL OPEN | No anchor-hit window, calendar or BE labels (E3C:578-617). |
| A-37 [OPEN] | STILL OPEN | No Phase 10, yet a cascade bonus is applied (N-07). |
| A-38 [PART] | PARTLY | Reason codes are logged. The 9.5-pip envelope (E3C:856), CS-1 and the 3D audit are absent. |
| A-39 [OPEN] | STILL OPEN | No BoS / flip / retest condition on RWL setups (E3C:168-171). |
| A-40 [PART] | PARTLY | Transition is built (e3 412-415, 466-469). There is no stack-compliance gate (E3C:242, :1009). |
| A-41 [PART] | PARTLY | No 1-2-3 activation (E3C:625). |
| A-42 [PART] | PARTLY | Sizes (30,20,20) at e3 662. No trip-wire and no rocket type (E3C:672-692). |
| A-43 [PART] | PARTLY | 1H rungs only (e3 611-616). No LSZ in the mapping. No 8R.5 and no Phase 11. |
| A-44 [OPEN] | STILL OPEN | No acceptance test (E3C:996) and no per-category maximum (N-26). |
| A-45 [OPEN] | STILL OPEN | _stop needs no liquidity zone between entry and SL (GS:69). |
| A-46 [PART] | PARTLY | No ABORT macro text (E3C:1042). |
| A-47 [FIXED] | CLOSED | e3 429 (E3C:1115). |
| A-48 … A-52 [OPEN] | STILL OPEN (×5) | sd unchanged (same md5). |

### B — code contradicting a canon sentence

| id | verdict | deciding code / canon |
|---|---|---|
| B-01 [FIXED] | CLOSED | session_events on 1H bars (e2 70-87). |
| B-02 [FIXED] | PARTLY | Rows carry 'full' flags (e2 408-440), but a row whose ZFP condition fails still assigns its shape one tier lower (e2 443-449). P533:1772 says "If it matches, assign that shape". |
| B-03 [FIXED] | PARTLY | Both HOLD → SS (e2 587-588). An IP bound with ZFP < 30% that is classed MoM / Active is still made to "go" (e2 209-212, 519-522), against P533:1830 "SS \| All < 30% … SS continues". |
| B-04 [FIXED] | CLOSED | Branch per bound (e2 499). |
| B-05 [ANSWERED] | CLOSED | The retest is tagged RWL only when the preceding pre-anchor BS ran the other way (e2 628), consistent with P533:1761. |
| B-06 [OPEN] | CLOSED | WL+RWL now emits a WL and an RWL step (e2 646-647). The WL upgrade rule itself is N-13. |
| B-07 [FIXED] | CLOSED | add() refuses past 5 steps or 25% (e2 547). |
| B-08 [FIXED] | PARTLY | 'ss' mode extends step by step. 'bs0' mode still hard-wires 6.3 frequency chains (e2 576-586), including a second BS through the bound just classed as rejecting (C-14). |
| B-09 [PART] | PARTLY | See A-09 and N-17. |
| B-10 [OPEN] | STILL OPEN | A Step-1 R is run as 'ss' consolidation (e2 506). P533:1833 "R \| < 1 session, opposing zone near \| WL or RWL" is never tested. |
| B-11 [FIXED] | PARTLY | The invented ZFP is gone. Supply/demand and sweep zones still bound the range ahead of the BoM IP zones (e2 149-156), with no 6.5 metrics (P533:1879). |
| B-12 [FIXED] | PARTLY | MoM bounds go through branch(). E3 swing scalps still enter at MoM bounds with no exceptions (e3 384-386, 442). |
| B-13 [ANSWERED] | PARTLY | The answer rests on P452:2082, a superseded E3 Fibonacci-wormhole line (N-14). target() takes the nearest of IP / SD / sweep zones (e2 330), not "next IP zone or Structural Extreme Magnet" (P533:1751). |
| B-14 [OPEN] | PARTLY | Depleted is excluded (e2 367). BoM zones with 2 taps still count as "always react" (e2 365), whereas P533:1873 says "if unmitigated". |
| B-15 [OPEN] | STILL OPEN | The Decision Zone may be a supply/demand or sweep bound with the trigger '1H close beyond it' (e2 791, 799). P533:1895 requires "the IP zone whose ZFP determines". |
| B-16 [FIXED] | CLOSED | e2 596-605 (but overridden by N-15). |
| B-17 [OPEN] | STILL OPEN | Days carry several shapes (e2 757-760), against the single-shape format of P533:1897. |
| B-18 [FIXED] | PARTLY | Only SS steps enumerate zones (e3 357-386). The other steps take one E2 zone. WL and R take none (N-06). |
| B-19 [PART] | PARTLY | Depth ≤ 3 (e3 589). No shape-link whitelist (E3C:452-457). |
| B-20 [ANSWERED] | CLOSED | The link uses tp_level (e3 453), under the general rule E3C:444 "TP of ONE = ENTRY of NEXT". |
| B-21 [FIXED] | PARTLY | The IP gate is at e3 69-80, but the transition entry overrides it at the IP bound's edge (N-10). |
| B-22 [PART] | PARTLY | Sweep zones are still entry anchors (e3 58-66, 406-407, 470-486), against E3C:135. |
| B-23 [FIXED] | PARTLY | The lift is applied only to nested / IP-attached order blocks. A supply/demand supply anchor gets its bare bottom edge (e3 91) (N-20). |
| B-24 [OPEN] | STILL OPEN | N-19. |
| B-25 [FIXED] | CLOSED | e3 282. |
| B-26 [FIXED] | PARTLY | See A-22: RR-tight ≠ "3p back edge". |
| B-27 [PART] | PARTLY | A 4-36 pip envelope (e3 286), against GS:67 "NEVER above 25 pips for standard entries" and GS:71 (4H/8H shield). |
| B-28 [FIXED] | PARTLY | Fibonacci pseudo-rungs satisfy "LQZ inside" (e3 106-112, see C-17). The SS walk uses the rung midpoint, not the zone midpoint (e3 183-184). |
| B-29 [PART] | PARTLY | 1H BoM targets get a rung midpoint (e3 111-113). Weak zones get the far edge only at the pivot (e3 193-198). |
| B-30 [PART] | PARTLY | RWL TP = the first rung 30-100 pips along the way (e3 123-130), not the nearest opposing supply/demand zone (E3C:316). |
| B-31 [FIXED] | CLOSED | e3 496-497. |
| B-32 [PART] | PARTLY | The SL is re-anchored only above 15R (e3 506-515). Below the floor nothing is re-anchored, though E3C:379 says "sl = next-rung's reactionExtreme + Law-7 buffer". There is no REPAIRED log. |
| B-33 [PART] | PARTLY | See N-08 and N-09. Rockets sit on 1H rungs, not the "next MoM zone" (E3C:631, GS:106). |
| B-34 [PART] | PARTLY | 1H / 4H anchors only. No scalp stack (E3C:96). |
| B-35 [OPEN] | STILL OPEN | 'Reversal' category (e3 23); 'Ladder' as a shape (e3 661). |
| B-36 [FIXED] | PARTLY | Per-day clones are exempt from the 11 (N-05). _build still truncates by list position (e3 600-603). |
| B-37 [OPEN] | STILL OPEN | Consumers use ±0.05 (e2 126, 176-177, 326; e3 406-407, 479-480; pine 73) while e1_ip 126-134 builds the inward ±0.10. An outward 'reach' is added instead (N-01). |
| B-38 [ANSWERED] | CLOSED | RUL:100 (L-38) "valid order block needs a gap (inefficiency) between the before and after candles". |
| B-39 [ANSWERED] | STILL OPEN | sd 52-56. The answer is an oracle box (D-21), not a canon line. P452:645 "SINGULAR candle … NOT from a cluster" stands. |
| B-40 … B-45 [OPEN] | STILL OPEN (×6) | sd unchanged. |

### C — inventions

| id | verdict | deciding code / canon |
|---|---|---|
| C-01 [FIXED] | CLOSED | info() zfp None (e2 103, 105). |
| C-02 [FIXED] | PARTLY | Standing-zone test added (e2 238). The definition ("most recent standing 4H BoM; else 2-bar swings") still has no canon sentence. |
| C-03 [FIXED] | CLOSED | — |
| C-04 [OPEN] | CLOSED | The 'down' default is gone. No bias → bdir None (e2 526-529). |
| C-05 [ANSWERED] | PARTLY | Logged as D-35. The numbers 0.90 / 0.80 / 0.65 / 0.50 / 0.35 (e2 17) remain invented. |
| C-06 [PART] | PARTLY | 6-session window (e2 391); move merge (e2 452-463). |
| C-07 [ANSWERED] | PARTLY | E3 now trades both directions (e3 361). E2 path parity (e2 704-712) and the "upper half → up" rule (e2 711) have no canon. |
| C-08 [PART] | PARTLY | e2 736 (t1 / 3), e2 576 (dur + 3·FA9 + 2), e3 746 (6 h minimum). |
| C-09 [OPEN] | PARTLY | e2 675-677 (range middle; spot ± 0.30U) is still live. e2 137-140 adds a V1-band pivot (N-23). |
| C-10 [OPEN] | STILL OPEN | e2 737-746 leg end points. |
| C-11 [OPEN] | STILL OPEN | e2 142-143. |
| C-12 [OPEN] | CLOSED | No stretch in target() (e2 303-330). |
| C-13 [OPEN] | STILL OPEN | liquidity_beyond (e2 167-184), 0.15 limit. |
| C-14 [ANSWERED] | STILL OPEN | e2 576-578: second BS through `near` with no 6.4/6.4.1 test. P533:1790 is a frequency table, not a transition rule. |
| C-15 [ANSWERED] | CLOSED | Gap reading logged (D-39), permitted by GP:43. |
| C-16 [FIXED] | CLOSED | e2 754-756. |
| C-17 [OPEN] | STILL OPEN | e3 30-38. Pseudo-rungs are used as TP levels (e3 106-112, 138, 182-184, 195). GS Law 5 / P533 Step 0.6 (P533:2594) name 0.382 / 0.618 key levels of IP zones, not liquidity rungs of supply/demand zones. |
| C-18 [OPEN] | CLOSED | Replaced by the reach rule (N-01). |
| C-19 [ANSWERED] | PARTLY | The 4-9.5 range of E3C:291 belongs to the golden fallback. The code applies the 4 pips as a minimum to every candidate (e3 286) and does not enforce the 9.5 envelope (E3C:856). |
| C-20 [OPEN] | CLOSED | used = set() always (e3 495). |
| C-21 [OPEN] | CLOSED | No anchor repair in _build. |
| C-22 [OPEN] | CLOSED | No pair-only collision retry. |
| C-23 [OPEN] | STILL OPEN | e3 80 [:3], 85 [:1], 89 [:1], 74 (0.5 overlap), 138 / 195 (2-pip), 133 (0.10U). |
| C-24 [FIXED] | CLOSED | e3 57 (RWL, long side only). |
| C-25 [ANSWERED] | CLOSED | Replaced by per-day clones (N-05). |
| C-26 [OPEN] | STILL OPEN | pine 121, 128, 139 (prior week ± 10-day ADR) plus reach() hiding (N-24). |
| C-27 [ANSWERED] | STILL OPEN | The 0.5 body ratio (sd 48) is in no canon line. D-21 cites P452:639-649, which has no such test. |
| C-28 [ANSWERED] | CLOSED | Plainest reading, permitted by GP:43. |
| C-29 [OPEN] | STILL OPEN | sd 125-134. 'reactions' on supply/demand zones is still never read (e2 105 and e3 230 read 'mit'). |
| C-30 [ANSWERED] | STILL OPEN | sd 93-97. Leg end by opposite-type BoS zone and "first zone = BoM" have no canon sentence. Matching 7 labels is oracle evidence. |
| C-31 [OPEN] | STILL OPEN | sd 105-106. |
| C-32 [FIXED] | CLOSED | Based on the e1_v1.py header comment (line 16) only. The harvest function was not re-read line by line. |

### D — temporal anchor / hardcoding

| id | verdict | deciding code / canon |
|---|---|---|
| D-01 | CLOSED | tools/git-hooks/pre-commit runs tools/leak_check.py for every staged e1_tool/*.py. |
| D-02 | CLOSED | e1_outcome.py, e2_shapes.py and e3_setups.py are not in the 9cdfbc0 tree (only stale .pyc files). |
| D-03 | CLOSED | e3 __main__ (e3 760-771) has no week literal. |
| D-04 | CLOSED | e1_synth.py and e1_zones.py are absent. No week literal in e1_tool/*.py (git grep). |
| D-05 | STILL OPEN | Oracle prices moved into e3 comments: e3 149, 258-259, 619, 634-635, 648. GP:46 says "Oracle numbers … never appear in tool code." |

**Section 1 totals (134): CLOSED 36 · STILL OPEN 43 · PARTLY 55.** Of the 51 the builder marked FIXED, 22 are not closed.

---

## Section 2 — NEW findings

### (b) code contradicts a canon sentence

**N-01 · LSZ extension built outward instead of inward**
- Canon: P533:1286 — "Extend the liquidity sweep zone scan 0.05-0.10 DXY **below swing highs** (for supply-side LSZs) and 0.05-0.10 DXY **above swing lows** (for demand-side LSZs)". P533:2616 repeats it: "sweep scan 0.05-0.10 DXY below swing highs".
- Code: 'reach' = extreme ± 0.10U *beyond* the extreme:
  - e2 126: `'reach': ext + 0.10 * U if up else ext - 0.10 * U`
  - e2 163, 176-177
  - pine 178 (the dotted reach box)
- It drives:
  - the stop "1 pip outside the extended sweep range" (e3 261-267, D-84 / D-87 / D-90);
  - the SS day box (e2 774-782);
  - which shields are discarded (e3 265-266).
- Engine 1's own LSZ (e1_ip 126-134) extends inward, as the canon says.

**N-03 · Emitted RRR can fall below the floor**
- Canon: E3C:362 — "Emission floor: RRR ≥ 3.0 (all categories) — the gate, code, never model". The relaxed floor is 2.5 (E3C:1115).
- Code: e3 516 tests the floor, then e3 520-523 moves the TP 1.5 pips toward entry and recomputes `rrr`. There is no second check.
- Example: a 5-pip stop with a 15.5-pip target passes at 3.1 and is emitted at 2.8.

**N-04 · STANDARD setups emitted**
- Canon: R-07 — "God tier and high is the new normal. Everything else is rejected. I don't even want to see it on my chart."; GP:54 "only GOD_TIER / HIGH (R-07)".
- Code: e3 565 `s['quality'] = 'HIGH' if s['confidence'] >= 80 else 'STANDARD'`, and every setup ≥ 65 is kept (e3 563-566).

**N-05 · Per-day repeats escape the weekly limit**
- Canon: RUL:16 (L-04) — "There should not be more than 11 trade setups per week per pair". R-07 — "maximum 10 per week … one to three per day".
- Code: e3 696-702 clones every swing scalp onto each SS day of its run; e3 707 `uniq = [q for q in out if not q.get('clone')]` excludes the clones from the count.
- Every clone is drawn as its own position box (e3 739-756).
- E3C:471 (`MAX_MIRRORS_PER_ANCHOR_PER_DAY = 1`) is a maximum of one per anchor per day. It does not exempt anything from the weekly count.

**N-06 · WL and R steps yield no setups**
- Canon: E3C:102 "WL (Whiplash) | HTF Swing | Swing Stack | 1 swing"; E3C:100 "R (Recovery) | Swing Scalps + Recovery Surge | … | 2–4 swing scalps".
- Code: e3 387-388 (`elif st['shape'] in ('WL', 'PWL'): continue`) and e3 389-390 (R: log, continue).

**N-07 · Cascade bonus on every pair setup**
- Canon: E3C:412 — "`+10` if setup is cascade-source (DXY → EU inverse or EU → GU kept)".
- Code: e3 334-335 adds +10 to every EURUSD / GBPUSD setup. No Phase 10 mirror exists (A-37), so no setup is a cascade source. The term moves pair setups across the 65 gate.

**N-08 · First rocket placed in the 0.786-1.0 band of a retest grid, stop at 0.618**
- Canon: E3C:227 — "Rocket 1 (FLR reinforcement) | 1.382–1.786"; E3C:689-690 "Entry zone … typically 1.382–1.786 Fib / SL zone … 1 pip outside back edge of next LQZ rung"; GP:61 "rocket 1 at 1.382".
- Code: e3 617-650. The comment's citation E3C:225 ("0.786–1.0 FINAL BLAST") describes a sub-range character, not a rocket placement.
- The rule is fitted to golden-week values written in the comment (e3 619, 634-635), which is anti-pattern A12 and breaks GP:46.

**N-09 · Rockets generated for every breakout primary**
- Canon: E3C:621 — "For each surviving HTF Swing setup of HIGH/GOD_TIER quality, generate 2–3 reinforcement entries".
- Code: e3 567-568 calls _reinforce for any BS/PBS primary that is not a transition, STANDARD included.
- e3 662 copies the parent's confidence and quality to each rocket without scoring it.

**N-10 · Transition entry at an IP-zone edge, in any phase**
- Canon: E3C:136 — "IP zones (source==='PILLAR') are … SL/TP rungs — NEVER entries". E3C:1133 / P533:1954 allow "BS Transition Entry" only in "Late consolidation … ZFP trending up on bounding zone".
- Code:
  - e3 466-469: entry = the far edge of `a` = E2['near'] (e3 414-415), which can be an IP zone. This overrides the `ip` gate set at e3 436-437.
  - e3 412 emits the transition whenever the chain holds an SS and a 'bs' step, with no phase test.

**N-11 · Timeframe element matching allows two timeframes up for every source**
- Canon: P533:1968-1971 — "4H source → 4H target (1H acceptable) / 1H source → 1H target (30m acceptable) / … / 15m source → 30m or 1H target (up to 2 TF dimensions higher…)". The two-up allowance is stated only for 15m and 5m sources.
- Code: e2 322 `TF_RANK[z['tf']] <= TF_RANK[src_tf] + 2`, so a 1H source accepts a 4H target.
- IP and sweep candidates (e2 312-327) are never filtered, and with src_tf None (an IP or sweep near bound, e2 626) nothing is filtered at all.

**N-12 · 4H MoM target → R**
- Canon: P533:1963 — "the expected shape after touching a 4H MoM is a minor WL followed by BS/PBS through the zone."
- Code: e2 369-370 returns 'R' MODERATE. Because tgt has no 'ip' key, the R step is then followed by SS (e2 655-656), never by BS/PBS.

**N-13 · After a breakout into a BoM candle zone: RWL as "Hard-Wall class", plus a WL upgrade**
- Canon: P533:1825 — RWL is the row for a target with "ZFP < 20% (Hard Wall)". P533:1873 — "A BoM zone reaction produces a directional move (BS, WL, or RWL) determined by the Direction Validation 6-check."
- Code:
  - e2 365-366 maps every Virgin / Active BoM candle zone to RWL HIGH. No 6-check is run there.
  - e2 640-643 upgrades RWL to WL+RWL when an unswept sweep level lies within 0.10U of the target. No canon sentence states this.

**N-16 · 6-check items 5 and 6 read the wrong inputs**
- Canon: E3C:1090 "Macro Shape: chain description → expected direction"; E3C:1091 "Counter-Trend: hard wall level → counter-trend risk HIGH/MODERATE/NONE"; E3C:1095 (risk → size).
- Code:
  - e2 295: the 4H storyline is passed as 'macro shape' (e2 532), so the storyline that may already have been the tiebreaker (e2 526-529) votes twice.
  - e2 296-298 turns counter-trend into a direction vote, with an invented 1.0U radius.

**N-17 · "Late" consolidation defined by elapsed sessions**
- Canon: P533:1954 — "Late consolidation (near HTF zone) | ZFP trending up on bounding zone".
- Code: e2 465-466 sets Late when elapsed > 3 sessions; with no BS in the 6-session history, el = len(ps) + 3 forces Late.

**N-19 · 4H zone edges used as entries**
- Canon: GS:48 "Entries are NEVER placed at 4H zone edges"; GS:52; GP:59.
- Code: e3 367 admits tf '240' SS anchors, and e3 91 enters at the TS-1 edge of any non-IP anchor.

**N-20 · F1-A missing on supply/demand supply anchors**
- Canon: E3C:186 — "For OB SHORT only, lift the entry 1 pip above the supply zone's bottom edge."
- Code: e3 91 `anchor['bot']` for a short at an E1 supply zone (an order block). Only nested V1 blocks (e3 86) and IP-attached blocks (e3 78) get the lift.

**N-27 · Breakouts exempted from the MoM gate**
- Canon: P533:1152 — "4H MoM … Not valid for swing entries"; E3C:1032 "4H MoM One-and-Done | Phase 2 | Scalp-only at 4H MoM"; E3C:1006.
- Code: e3 442 `… and c['shape'] != 'BS'`. BS (HTF Swing) and Transition anchors at MoM, including 4H MoM, pass.

**N-28 · Direction of the PIERCED branch** (reading uncertain; flagged for checking)
- Canon: P533:1845-1848 — "SHARP WHIPLASH/REVERSAL instantly … Zone is PIERCED … Next shape: BS or WL in OPPOSITE direction".
- Code: a Depleted MoM bound → 'PIERCED' → the breakout goes *through* that bound in its own direction (e2 205-206, 519-522, 531).
- The canon text names the opposite direction. I could not settle which direction "opposite" refers to.

**N-29 · BoM bounds run through the decision-tree counter**
- Canon: P533:1873 — "BoM zones are NOT subject to this decision tree — they ALWAYS react".
- Code: e2 201-203 makes a BoM bound with 3+ reactions 'PIERCED' (a breakout). The cited P533:1159 is about IP-zone entries / TPs ("Use for TP targeting only — NOT for entries"), not about a BoM bound breaking.

**N-32 · Rockets counted among the 11 trades**
- Canon: R-10 — "These are not normal trades."
- Code: e3 600-603 and e3 707-712 count the 'Reinforcement' entries in the 11 and can cap real setups to make room for them.

### (c) behaviour with no canon sentence behind it

**N-02 · Citations that do not say what the comment claims (the operator proof and the stop buffer)**
- e3 258-260 cites "P533 7.1 operator proof 'LONG SL … = 97.87 - 0.01 = 97.86'" as "the end of the extension". P533:2610 reads "LONG SL from MRS = 97.87 - 0.01 = 97.86 (**key level 97.87 of zone below - 1 pip**)". That is Rule 2, not an LSZ extension.
- P533:2615 (Rule 2.5) gives "LSZ boundary + 3 pip buffer". The code uses 1 pip (e3 264, D-87).
- "E3C:304 '1-2 pips OUTSIDE THE BACK EDGE OF THE STOP-LOSS ZONE'" is E3C:307, the *Rocket* SL doctrine, applied to primary stops.
- Every P533 Part VII citation (7.1 Rule 2.5, 7.1 Rule 3 in e3 191 / D-86, the operator proof) is in the E3 text that R-16 supersedes.

**N-14 · P452:2082 is a superseded Engine-3 Fibonacci line, used as a general target filter**
- P452:2082 sits in v4.5.2 "PART VI-B: ENGINE 3 … 8.2 Fibonacci Spiderweb … Fib Wormhole Mechanics": "strong IP **at a fib level** = it holds (valid TP). No IP + standalone MoM = it gets pierced".
- It is used to drop every 30%+ MoM IP zone and every standalone MoM candle zone from the E2 breakout targets (e2 315-321) and from the E3 Law-14 blockers (e3 172-174). These are D-49 / D-50 / D-74, and it is also the basis of the B-13 answer.

**N-15 · NY Cut Cage sets the transition day**
- e2 606-618: the last 10:00 NY cut known at the anchor + 1 day replaces adj_day (e2 616). This can move the breakout earlier than the key rule / SLOW minimum (e2 591-595, P533:1959, :2054 "2-4 days").
- P533:690-691 describes an intraday pin before 10:00 and a release at 10:01 on that day. It does not say which day a range breaks.
- The code's threshold is tier ≤ 2 (≥ $850M, e2 611), but P533:690 names ">= USD 1.5 Billion … Critical Entry Shields".

**N-18 · Swing-scalp reach measured from the bound**
- GS:36 "Zone Distance from Spot | 0-30 pips"; GS:152.
- e3 364-369 measures 0.30U from the bound's edge. The bound itself is unlimited when it is a supply/demand pool zone (e2 149-151), a sweep zone, or `ips[0]` (e2 156).
- Clones (e3 696-702) rest each day regardless of where price is.

**N-21 · TP buffer applied to every target**
- SPW item 4 "For SS/Rcvry SCALP moves … Make sure there is a 1.5-2 pip buffer in front of the TP" on the "Fib wormhole" TP; P452:2084-2087 "MANDATORY Buffers for Scalp Entries (Context 2)".
- e3 204 and 516-523 apply 1.5 pips to every TP: BS, RWL, transition, weak-zone far edges.

**N-22 · JOIN_TP (e3 146-156, D-91)**
- L-39 (RUL:104-110) rules on how a pressure zone is *drawn*. It is used here to move a TP to the nearest edge of any overlapping IP / candle zone.
- EUR/USD is exempted by reading "DIRECT_ZONE_TEST", a label that E3C:1102 lists without any definition.

**N-23 · Pivot = V1 4H band within 0.30U**
- e2 137-140 (D-44). The cited "P452 'EQUILIBRIUM ZONE: Pivot area'" names an IP zone, not a liquidity band.
- The pivot sets SS leg ends (e2 717-718), the retest entry (e3 398) and RWL targets (e3 409).

**N-24 · Engine 1 visibility depends on the Engine 2 forecast**
- pine 27-58 and 100, plus the near/far split at pine 146-151, 163-171, 187-192: E1 zones outside the E2 day envelope are hidden behind `show_far` (default false).
- GS:152 speaks of where *setups* are generated. R-37 forbids hiding output. GP:13-14 builds E2 on E1, not E1 on E2.

**N-30 · Unlogged or uncited constants that shape output** (no canon number for any of them)
- e2 20 SS_SWING 2; e2 24 BS_SESSIONS 3 and ×2 (e2 636); e2 591 `3 * SLOW_DAYS` (3 sessions per day); e2 576 `dur + 3*FA9_DAYS + 2`.
- e2 265-274: pressure votes at 1.5× and slope 1/3; e2 258: 48 bars.
- e2 297: 1.0U wall radius.
- e2 414: 0.10U sweep tolerance (row 2); e2 419: 0.05U (row 3); e2 423: 0.30U midpoint (row 4).
- e2 350-351: 0.25U round grid with 0.03U tolerance (P452:1023 gives none).
- e2 228-230: EMA 50 / 200 4H trend.
- e3 491: transition dmin 12 with no 20-pip maximum (GS:59 "12-20").
- e3 482: 0.15U sweep-in-front distance (D-69).
- e3 614 and 646: 20-pip rocket spacing applied as a minimum.
- e3 659: rocket day = parent day index k+1.
- e3 233: fuel "ABSORBED = visits ≥ 3".

**N-31 · Orders resting before their designated day**
- e3 460-465: the BS entry rests from the first SS day (D-76). e3 456-459: the RWL rests from the BS day.
- R3 law E3C:77: "Every order leg's session bracket comes from the E2 session label". No canon line moves the bracket earlier.

**N-33 · Confidence terms not as written**
- e3 324-325: +8 "zone-direction alignment" granted to sweep / liquidity anchors (E3C:396: "SUPPLY→SHORT or DEMAND→LONG" only).
- e3 328: storyline counter-trend scores 0, but E3C:245 says −5.
- e3 314: no-IP base 70, which is not the middle of the "typically 50-95" cited (D-42).
- e3 340-342: "prior-week momentum" = weekly close vs mid-range, a definition the canon does not give.

### (a) canon step with no code

**N-25 · Two Phase 2 / Phase 4 gates.** E3C:1022 "IP Zone Map | Phase 2 | Zone selection (confluence ≥ 7)" and E3C:1026 "Hard Wall Detection | Phase 4 | SL anchor (ZFP<15%, confluence≥8)" have no code in e3.

**N-26 · Per-category maximum.** E3C:1011 "Max 3 setups per category per pair" has no code.

**New findings: (a) 2 · (b) 20 · (c) 11 = 33.**

---

## Section 3 — the ten findings most likely to change the output (most severe first)

1. **N-01** — The sweep-zone "reach" runs 0.10 *beyond* the extreme; the canon (P533:1286, :2616) extends *inward*. This moves stops (e3 261-267), range boxes (e2 774-782) and shield choice.
2. **N-03** — RRR is checked before the 1.5-pip TP buffer, so setups below 3.0 / 2.5 RRR are emitted (e3 516-523).
3. **N-05** — Per-day swing-scalp clones are not counted toward the 11 (e3 707). The chart can carry far more than 11 position boxes, against L-04 / R-07.
4. **N-04** — STANDARD (65-79) setups are emitted (e3 565), against R-07 "Everything else is rejected".
5. **N-14 / B-13** — A superseded v4.5.2 E3 Fibonacci line (P452:2082) decides which zones are breakout targets and Law-14 blockers (e2 315-321, e3 172-174).
6. **N-07** — An unconditional +10 cascade bonus on every EURUSD / GBPUSD setup (e3 334-335) changes which pair setups pass the 65 gate.
7. **N-06** — WL and R chain steps produce no setups (e3 387-390), against E3C:100 / :102.
8. **N-15** — The NY Cut Cage rule rewrites the breakout day (e2 606-618), using an $850M threshold where the canon says 1.5bn, and overrides the key-rule timing.
9. **N-12 / N-13** — The next shape after a breakout: 4H MoM → R (canon: WL then BS/PBS); BoM candle zone → RWL with no 6-check; the invented WL upgrade (e2 365-370, 640-643).
10. **C-17** — Fibonacci pseudo-rungs inside supply/demand zones act as "LQZ inside the zone", setting TP midpoints and walk levels (e3 30-38, 106-112, 182-184).

Next in line: **N-10** (transition entries at IP edges, in any phase), **N-11** (two-up timeframe matching for 1H sources), **A-23** (LAW7 pair buffers never used), **N-08** (rocket at 0.786-1.0 instead of 1.382).

Not verified:
- e1_v1.py (C-32) beyond its header.
- How often each path fires: nothing was run, by instruction.
- N-28 depends on a reading of "opposite direction" that I could not settle from the text.
