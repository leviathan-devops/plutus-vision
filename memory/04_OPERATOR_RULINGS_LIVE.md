# 04 — OPERATOR RULINGS, LIVE (this session; newest last; these override older handover rulings where they conflict)

Older rulings R-01..R-39: `/home/user/inputs/handover/PLUTUS_VISION_CONTEXT_HANDOVER/00_HANDOVER/PLUTUS_VISION_CONTEXT_HANDOVER.md` Appendix A (lines 685-865).
Still in force from there: R-05 canon vocabulary only · R-09 position boxes vs zones · R-10 rockets are not trades · R-13 only test = Pinebox + chart ·
R-14 E1 = v5.3.3 prompt every token · R-16 E3 = corrected E3 doc · R-17 ZFP = strength only · R-30 E1 layered on top of v1 baseline (v1 unedited) ·
R-36 two-week render window · R-37 no caps as a fix · R-35 no book reports (mechanism + evidence).
Superseded today: R-12 (operator-driven turn by turn) -> now FULLY AUTONOMOUS. R-34 (no subagents) -> lifted, see L-06.

## 2026-11-25 brief (verbatim essentials)
- L-01 Deliverable: Pine indicator. V1 baseline (S/D + liquidity) is A-; "Don't touch a single thing" on liquidity; S/D "good enough".
  E1 institutional pressure zones rendered ON TOP of V1, accurate to price action >= 90%. Then E2 and E3 "if you're capable". "Don't come back until everything is actually tangibly done."
- L-02 "The hard constraint, no hard-coded fucking values." E1/E2/E3 "dynamically calculated for the specific trading week based on the market data available at the beginning of that week" —
  any random week, same accuracy. "It's not going to be 90% accuracy on the one week that you optimize all of the hard-coded trash for."
- L-03 Pinebox is the IDE. "paste the PineScript into the Pinebox IDE, run it ... export to backtest ... navigate any date". "No headless script tests. Fuck your bullshit Python scripts. Forbidden."
  Verify by LOOKING: "Are the candles reacting to your zones? Are the candles following your E2 shape chain? Are the candles actually filling your trade setups and hitting take profit without hitting stop loss?"
- L-04 "There should not be more than 11 trade setups per week per pair." Timeframes: 4H, 1H, 30m (15m for precision only).
- L-05 Temporal anchor: "Monday, the very start of the trading week ... forward predict the E1, E2, E3 data of the trading week based on the data that is available on Monday, London session open
  of that trading week and whatever historical data exists before that. Period. That is a hard mechanical constraint. Put whatever git hooks and git logs need to be put in so that you cannot violate this."
- Start with the golden week Jul 6-10 2026 "based on the Oracle references", then other weeks. E3 uses the UPDATED (corrected) prompt.
- "If you have any questions, ask me."  Then: "I expect you to fully autonomously complete everything and run Pinebox as the integrated development environment."

## 2026-11-25 answers to my questions (verbatim)
- L-06 Subagents: "use them freely just dont be fucking retarded or delegate primary responsibilties i put that constraint on inferior models to force them to work correctly"
- L-07 Scoring of the 90%: "Reaction at the zone" — a zone is right if price turns/stalls at it when touched (or it correctly bounds the week untouched);
  wrong if price runs through with no reaction, or a real turning point of the week has no zone. Score = right / (zones + missed turns).
- L-08 E1 web data (option strikes, analyst levels, H.10): "you need to fetch that data from the web and build that in code with an embedded agent system. i can provide an api key"
- L-09 Historical web data: "they are online. they are never gone ... literally jsut scroll back to that date and it is still there. esepcially investing lvie for fx options stirke targets
  it has ALL the data for 2026 (only 2026 data is relelvant dont go further back than feb 2026 for your testing)"  => TEST WEEKS: Feb 2026 onward only. I was wrong to say the data was gone.
- L-10 Model for the embedded agent: OpenCode Go key saved on the environment for host `opencode.ai` (proxy-injected; send `Authorization: Bearer proxy-injected`).
  "on go use muse spark 1.3 contributor on reasoning effort high". Cloudflare also offered if needed.
- L-11 Embedded agent framework: "use this for embedded agent systems" = `/home/user/inputs/aether/aether_agent_backend_v2` (uploaded zip eaf17adc-aether_agent_backend_v2.zip).
- L-12 Network: operator approved hosts investinglive.com, www.investinglive.com, www.forex.com, www.federalreserve.gov, www.ice.com, www.cmegroup.com, opencode.ai, api.cloudflare.com (measured 200 on investinglive, fed, opencode models).
- L-13 Memory: set up OmniGraph (github.com/modernrelay/omnigraph) + 5-10 markdown files (decision chain, task queue, current state, compaction survival, journal, reasoning chain);
  persist durable facts every 3-5 turns; "This is going to take at least 10 to 15 compactions". He then left: "I'm going to leave you alone after this."

## 2026-11-25 ~14:30 UTC - operator intervention after looking at my frames (BINDING, supersedes my E2/E3 plans)
- L-14 E1 FIRST AND ONLY. "Don't even touch E2 or E3 until E1 is fixed." Order is zones -> shapes -> trades; forbidden to move forward until each works. E2/E3 code stays in the file but OFF by default.
- L-15 His verdict on my frames: ~30% of zones right, the rest "completely penetrated", plus "random zones floating off in empty space"; best frame ~50%. "I do not want to see zones rendered on the chart that are not accurate." No "17 random zones".
- L-16 Acceptance: "Verify across 4 separate weeks that the E1 zones are actually 90% accurate" (he wants 95%). Each rendered zone must fit: correct pressure, correct direction, correct ZFP "based on the price action mechanics", not invented.
- L-17 Baseline to replicate then exceed: Trident_Report_2026W14_Mar30-Apr3.pdf (upload: /root/.claude/uploads/*/d253d0fc-Trident_Report_2026W14_Mar30-Apr3.pdf) made by GLM 5.1 with the Toolset (same files as canon/Toolset; unzipped copy /home/user/inputs/toolset_glm). The PDF step is gone: compute the same data and render it directly in Pine.
  Its E1 format = FOUR wide bands per pair (R2, R1 supply; D1, D2 demand), columns Range | Type Supply/Demand | BoM/MoM | Reactions | ZFP% | Confl x/14 | option/key level | status.
  W14 numbers: DXY R1 100.50-100.65 BoM 0 rx 10% 9/14 ; R2 100.00-100.25 MoM 2 rx 25% 6/14 ; D1 99.30-99.60 MoM 1 rx 30% 6/14 ; D2 98.80-99.10 BoM 0-1 rx 20% 7/14.
  EURUSD R2 1.1600-1.1640 BoM 15% 9/14 ; R1 1.1545-1.1575 MoM 30% 7/14 ; D1 1.1495-1.1515 MoM 35% 8/14 ; D2 1.1430-1.1460 BoM 20% 8/14.
  GBPUSD R2 1.3400-1.3480 BoM 12% ; R1 1.3300-1.3350 MoM 28% ; D2 1.3250-1.3280 MoM 32% ; D1 1.3150-1.3200 BoM 22%.
- L-18 E3 remark (for later, not now): his setups need RRR 4x+.

## 2026-11-25 ~16:10 UTC - operator answers the accuracy question (BINDING)
- L-19 Acceptance metric for E1 = "Reacts on first touch at 90% or better" (his pick from my three options).
- L-20 He accepts that the W14 report may have had forward data ("whatever makes sense. I can understand"). He still wants to SEE the W14 zones rendered so we look at the same thing
  (frames evidence/oracle_w14_report_zones_{DXY,EURUSD,GBPUSD}_1h.png were sent; resend when asked).
- L-21 His three reference screenshots (golden week Jul 6-10, DXY 1h/1h/4h, manual charting "at the beginning of a week", saved under the session images dir 1.webp/2.webp/3.webp):
  green bands 101.19-101.29 (white mid line 101.24), 100.94-100.985 (thin pivot band), 100.545-100.675 (white mid line 100.61); red "4H (Unmitigated) | BoM" supply 101.33-101.44;
  blue "1H (Unmitigated) | BoM" demand 100.655-100.74; blue "4H (Unmitigated) | MoM" demand 100.24-100.34; white box = the week. Circles mark the candle each band was drawn from
  (Jul 1 candle at 101.24; Jul 3 low wick at 100.56-100.66). Week high 101.27 turned inside the top band, Friday low 100.60 bounced inside the bottom band, the middle band was a pivot crossed all week.
  HIS WORDS: those bands are "based purely on price action candles", already covered by the V1 baseline (S/D + liquidity). E1 = "the other side of the coin, the institutional pressure zones
  rendered on top of this based on all of the data available from the web fetch sources that are spoken in the prompt". Same degree of accuracy as his drawing, any random week, Monday London-open data only.
