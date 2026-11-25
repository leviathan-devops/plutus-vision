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
