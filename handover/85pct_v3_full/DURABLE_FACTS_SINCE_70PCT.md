# Durable facts since the '70% functional' package - verbatim copies from memory/ (the markdown in memory/ stays the source of truth)

Generated from memory/04 (rulings L-46 .. L-59), memory/08 (SESSION FACTS 2026-11-27 + M-61 V3 facts), memory/06 (lessons L-50x .. L-58x), context_management/oracle/golden_week.json (his golden trades) and the environment. Nothing below is paraphrased except section 5.

## 1. Operator rulings L-46 .. L-59 (memory/04_OPERATOR_RULINGS_LIVE.md)

- L-46 (M-58, 2026-11-27) STOP RULE (his words): "it is either 2-3 pips outside the entry zone or 1-2 pips inside the next zone" - WHEN each applies is still open: he asked for multiple practical scenarios with my decision making and questions. His sources on stops (read first-hand 2026-11-27): Trading Laws PDF ("SL should be 1-2 pips OUTSIDE THE BACK EDGE OF THE STOP-LOSS ZONE"; "If thin liquidity zone - move it 1 pip inside the next zone"; "If NY session trades - 2-3 pips | London session 1-2 pips"; "SL inside the next zone always" for stop-limit entries; scalps "1.5-2.5 pips inside the next 5m liquidity zone. No exceptions"; "If your stop loss ends up sitting inside a liquidity zone - you MUST move it 2 pips outside the back edge of this zone. No exceptions"); FA:63-67; E3C:247-256; P533 2.0 "SL correction/reentry exception".
- L-47 (M-58) DAILY ANCHORING APPROVED: "yes if you do this right without grating then sure" (my reading of 'grating': without cheating - each day uses only data closed before that day's London open). Precondition: "Make sure we have the current checkpoint FULLY saved before changing this" - he is away from his computer and cannot download.
- L-48 (M-58) The WINNING TRADE LIBRARY (/home/user/inputs/trades/WINNING_TRADE_LIBARARY: 38 marked screenshots in ten shape-chain folders + the golden week + four training PDFs) is his set of 20+ marked weeks - to be used as the oracle.
- L-49 (M-58) He charts TVC (TVC:DXY). Event-data permissions enabled by him; fallback he named: a sub-agent on Muse Spark 1.3 through the OpenCode Go key to fetch the data.


## 2026-11-27 - M-59, answers to the six open questions (BINDING; verbatim in memory/12)
- L-50 STOPS: a GOOD trade (aligned with the mechanics, risk-reward there) takes the WIDER stop - never skip it for a few extra pips; skip only low-probability trades; 'potentially even set a better entry' (deeper entry). The E3C golden SL envelope (9.5) does not veto a structurally needed stop. EUR/USD uses the inside-the-next-zone stop too where applicable. MECHANICS: GBP/USD - the liquidity shield is often OUTSIDE the supply / demand zone: candles touch the liquidity zone above / below it and react there, the S/D zone itself often untouched; EUR/USD - the liquidity sits INSIDE the S/D zone: price mitigates inside the zone. Same move, different liquidity mechanics per asset.
- L-51 E2 DRAWING = C: the day / shape BOX and the LINE; inside a SWING SCALPS box draw EACH swing. 'The line is supposed to show the actual price action that is going to materialize candle by candle ... as if it's a line chart'. If the candles do not match the line, the line is inaccurate.
- L-52 NO DUPLICATE TRADES (explicitly forbidden and banned): one unique trade per observable move; one trade = one instance where price hits the entry and then the take-profit; a pending order is not copy-pasted per day; follow how he sets up trades in his winning trade library. Per-day repeat clones (D-78 / D-89) are void.
- L-53 DAILY ZONE UPDATE APPROVED: 'synchronously re-update the zones at the beginning of London session each successive day' - new zones may be added as they form, without duplicate garbage or hallucinated slop; the temporal anchor still bounds everything (nothing from after the update instant).
- L-54 DATA: 'Either make it work or work within the constraints' - Forex Factory blocks automated access: work within the constraint (Protocol F = NO DATA), do not raise it again.
- L-55 The library's ~17 pair-weeks are enough: 'Optimize everything based on this.'
- L-56 (M-60, 2026-11-27) CHECKPOINT '80% functional - DXY specific' = commit aa8d689 state (daily anchoring, no duplicates, L-50 stops, London-open zone update, session line, D-138). His read: DXY first half of the golden week accurate (E2 + trades hitting entry and TP); DXY E2 second half (Wed-Fri) 'obviously broken'; GBPUSD 'completely fucked' (one visible trade, the rest unreadable); EURUSD frame missing ('the primary pair'). EVERY report shows ALL THREE PAIRS, the ENTIRE trading week in ONE screenshot per pair, properly fitted (no truncation). Do not make him micromanage obvious mechanics.
- L-57 (M-61, 2026-11-27) CHECKPOINT '85% functional - DXY + GU' = code bac6b50 (D-139 + D-140). His grades on the golden week: DXY and GBPUSD 'A-' - nearly perfect EXCEPT the Thursday trade: a LONG where the correct trade is a SHORT entered at the exact take-profit of Wednesday's long, where the E2 chain itself predicts the peak (same mistake on GBPUSD, mirrored); EURUSD 'a solid C' - explain why and bring it to the level of the other two. Sequence: V1 = this checkpoint; V2 = after the Thursday E3 logic fix (no hardcoding: fix the logic flaw); V3 = after the EURUSD fix; then report back and show everything. Each checkpoint commit carries code + context + OmniGraph.
- L-58 (M-62, 2026-11-27) After the V3 report ('Okay, great'): a FULL UPDATED HANDOVER PACKAGE covering everything since the '70% functional' package, at the same level of detail - all context, every visual checkpoint, the full OmniGraph, all artifacts, durable facts, checkpoints, commits, code files, a full markdown report + an engineering report explaining every single thing done - so another agent can understand, take over, reproduce and audit. 'Do not water anything down, do not hold anything back.' -> handover/85pct_v3_full/ + archives in handover_package/ (PLUTUS_VISION_85pct_V3__*).
- L-59 (M-63, 2026-11-27) Every handover is ALSO committed to his GitHub repo leviathan-devops/plutus-vision ('Brutus Vision' = speech-to-text for Plutus Vision) as its OWN fully self-contained branch: the 70% handover = one branch, the new handover = a second separate branch; 'everything should be pushed through to Git'. Built as branches handover-70pct-functional (from the 70% handover's last commit ea7da38 + the archive parts that were not in git) and handover-85pct-v3-full (from the final AGENT commit + its archive parts); parts split under GitHub's 100 MB file limit with checksums and a reassembly note. The repo is PUBLIC: the session transcripts go there with his email / account identifiers replaced by placeholders (unredacted copy delivered to him privately); every pushed archive scanned for credentials first.

## 2. Session facts (memory/08_FACTS.md, from 'SESSION FACTS 2026-11-27' to the end)

## SESSION FACTS 2026-11-27 (after the 70% handover; checkpoint '80% functional - DXY specific' = code aa8d689, commit 0d4ad41)
### Operator rulings of the day (verbatim in memory/12 M-58 .. M-60; rulings L-46 .. L-56 in memory/04)
- STOPS (L-50): good trade (mechanics aligned, RR there) takes the WIDER stop - never skip it for a few pips; 'potentially even set a better entry'. GBP/USD: the liquidity shield is often OUTSIDE the S/D zone (candles touch the liquidity zone above / below and react there); EUR/USD: the liquidity sits INSIDE the S/D zone (price mitigates inside it). Canon line for WHEN: P533:506 'SL correction/reentry exception: When trying to catch a CORRECTION/REVERSAL - ALWAYS make sure SL is 1-2 pips INSIDE THE NEXT ZONE ... Standard SL rules (outside the zone) apply for trend-following entries.' E3C ZR-6B (conf >= 0.6 RR-tight, else next-rung) and the E3C 12.2 golden envelope 9.5 pips conflict with it; the operator's ruling wins over the envelope.
- Measured on his golden stops: DXY 6 of 7 = inside the next zone (B), #6 (Wed breakdown short, trend-following) = outside (A); EUR/USD golden stops = 'outside the entry zone' (rule (a) matched them within 0.2-0.4 pips; the next-S/D-zone reading was 2-6.5 pips off and tighter) -> EU_INSIDE = False.
- NO DUPLICATES (L-52): one unique trade per observable move; a pending order is not copy-pasted per day; one trade = price hits the entry and then the TP. Explicitly banned.
- E2 DRAWING (L-51): box + line, each swing drawn inside a SWING SCALPS box; the line = the price action candle by candle as a line chart; if the candles do not match the line, the line is wrong.
- DAILY UPDATE (L-47 / L-53): orders and the E2 line from each day's open; zones re-updated at each London open, new zones added without duplicates; nothing from after the update instant.
- DATA (L-54): Forex Factory blocked (Cloudflare challenge to curl; a headless-browser load was REFUSED by the session's permission check; Muse Spark 1.3 via OpenCode Go has NO web search - answers 'NO_WEB_SEARCH') -> Protocol F = NO DATA, do not raise it again.
- LIBRARY (L-48 / L-55): /home/user/inputs/trades/WINNING_TRADE_LIBARARY (zip of 64 entries, complete): ~17 pair-weeks = GBPUSD Feb 2 - Apr 24 2026 (12 weeks), EURUSD Apr 13-17 / Jul 6-10 / Jul 13-17, DXY Apr 13-24 (1H) / Jul 6-10; evidence/answers_m58/Q4_library_inventory.md. These weeks are the optimisation / oracle set; the old S5 blind reserve (Feb 2 - Mar 23) is inside it (D-129) - S5 blind weeks must come from outside the library and outside every week run.
- M-60: checkpoint '80% functional - DXY specific'; DXY golden first half + trades accurate, DXY E2 Wed-Fri broken; GBPUSD poor; EURUSD missing from the report -> every report shows ALL THREE pairs, the WHOLE week in one fitted screenshot each.
### Data sources built (sidecar/protocols.py -> sidecar/out/protocols/<monday>.json; raw cached in sidecar/raw/protocols/)
- D Treasury: https://www.treasurydirect.gov/TA_WS/securities/search?startDate=..&endDate=..&dateFieldName=competitiveAuctionCloseDate&format=json (dateFieldName=auctionDate gives HTTP 500). Latest FIXED-rate (floatingRate != Yes) 2Y / 5Y / 10Y note (originalSecurityTerm) closed before the anchor (close date + time ET); trigger bid-to-cover >= 2.6 (P452:1443). The week's coupon auctions announced BEFORE the Monday (announcementDate < monday) with close time; their results are post-anchor and not stored.
- E NY Fed ON RRP: https://markets.newyorkfed.org/api/rp/reverserepo/propositions/search.json?startDate=..&endDate=.. (host allowed by the operator 2026-11-27); last two operations dated before the Monday, trigger at a USD 50bn contraction (P452:1444). No week of 2026 triggers.
- G EIA: weekly U.S. crude stocks WCESTUS1 https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=WCESTUS1&f=W (week-ending Fridays, thousand barrels); release Wednesday 10:30 ET or the alternate date of https://www.eia.gov/petroleum/supply/weekly/schedule.php (holiday weeks: Thursday 12:00); only prints released before the anchor; deviation = change - previous change, trigger |deviation| >= 5M (P452:1446).
- Shown in the E2 report block 'VOLATILITY TRIGGERS (as of the anchor)' and each day's Triggers line.
### Daily anchoring as built (plutus.daily_anchor; decisions D-131 .. D-138)
- Monday = the week anchor. Each later day: at the TRADING-DAY OPEN (17:00 NY the evening before; London-open anchoring loses every Asian-session fill, e.g. his golden Friday long filled 02:15 UTC): a 1H close beyond a Decision Zone of the chain in force since its anchor activates its alternative (6.6 Step 4); orders of the day confirmed (order block not closed through - one-time use; price on the order's side); a still-pending / open order is not copied (L-52) - a pending swing-scalp order rests into the next PURE range day.
- At the LONDON OPEN (02:00 NY): Engine 1 rebuilt as of it (e1_data.ASOF; V1 harvest cached per instant e1_tool/cache/v1s/PAIR_TF_MONDAY_<ms>.json): zones formed since the week anchor added where no zone of the family is drawn; after a failure the LINE and DAY BOXES follow a chain re-anchored on the rebuilt map (REANCHOR_DRAW, D-138); the ORDERS stay with the chain in force (REANCHOR = False, D-137: re-anchored orders cost winners).
- Rejected: re-running Engine 2 from scratch each morning (the 6.10 +1 day is re-applied every morning -> the golden breakout leaves the week); London-open order confirmation (loses Asian fills); P533:506 stops without the ruling (no gain while the 9.5 envelope filtered them).
- Leak check part 3 (tools/leak_check.py): each day's trading-day-open part identical with the bars cut there; its London-open part identical with the bars cut at the London open. pre-commit runs it on golden DXY + EURUSD.
- Session line (L-51 first version, e2_chain._session_path + plutus._day_line): canon P452 6.6 SESSION-LEVEL SHAPE MAPPING RULES - 1 Asia SS inside the prior day's range (flat), 2 London often triggers BS (swing to a bound, 02:00-08:00 NY; on a range day toward the bound NEARER the day's price, P533 2.3 / D-41), 3 NY pre-cut 08:00-10:00 pinned to the day's largest strike inside the range, 4 10:01 Spring Release, 5 NY post-cut to the next zone (the other bound) by 17:00, 6 day-over-day continuity, 7 Friday expiry effect.
### Locator numbers (12 count maps; my own fill simulation - bug locator only, never a verdict)
- weekly 91 orders / 34 TP / 22 SL / 33 unfilled -> daily + confirmation 70 / 31 / 10 -> + no copies 46 / 28 / 10 / 7 -> + L-50 stops 43 / 27 / 8 / 6 -> + zone update + session line (checkpoint) 44 / 25 / 8 / 9.
### Tooling facts
- Pinebox: a render while another process uses the station (V1 harvests) times out (CDP_TIMEOUT) and s3frames still writes the PREVIOUS pass's chart -> never render in parallel; check the 'pb ide' box count before citing a frame. After a worker restart Pinebox is dead: pinebox up --session plutus-main --adapter xvfb --pair DXY --tf 1H.
- tools/e1render honours PLUTUS_FLAGS (e.g. --weekly). Generated Pine of a frame lands in e1_tool/out/E1_PAIR_MONDAY.pine.
- Running python on HEAD after git stash rewrites tracked .pyc files and blocks git stash pop: use PYTHONDONTWRITEBYTECODE=1 for baseline runs.
### M-61 V3 facts (2026-11-27)
- His golden EURUSD #1 (Mon S 1.14322 / 1.14408 / 1.14103) traded only in the Asian session: price 1.1432-1.1441 from Sun 21:00 to Mon 05:30 UTC, never back at 1.14322 after the 06:00 UTC anchor before its TP (Mon 10:00) - outside the map's reach by the temporal anchor.
- His golden trades as Law-27 chains: EURUSD #1 TP 1.14103 -> #2 E 1.14106 -> TP 1.14442 -> #3 E 1.14441 -> TP 1.14004 -> #4 E 1.14012 -> TP 1.14276 -> #5 E 1.14277 -> TP 1.1395 -> #6 E 1.13953 -> TP 1.14544 -> #8 E 1.14578; DXY #1 TP 101.115 -> #2 E 101.14 -> TP 100.845 -> #3 E 100.845 -> TP 101.19 -> #4 E 101.19 -> TP 100.975 -> #5 E 100.975 -> TP 101.24 -> #6 E 101.235; GBPUSD #1 TP 1.33941 -> #2 E 1.33934 -> TP 1.33347 -> #3 E 1.3333 -> TP 1.34246 -> #5 E 1.34246.
- EURUSD Monday ceiling structure (golden): 1H supply BoM 1.14375-1.14421 (origin Jul 3 17:00 UTC, the mirror candle of his DXY 1H MoM 100.825-100.851), the pressure zone UPPER RESISTANCE 1.14444-1.14533 above it; V1 1H rungs 1.14387-1.14415 and 1.14484-1.14512; EURUSD pierced the 1H supply to 1.14454 (Mon 18:45 UTC) and turned at the pressure zone.

## 3. Lessons of this window (memory/06_LESSONS.md)

- L-50x (2026-11-27): a Pinebox render while another process uses the station (V1 harvests of a locator run) times out (CDP_TIMEOUT) and s3frames still writes a frame - the earlier pass's chart. Never render in parallel with a station user; check the 'pb ide' output (box counts) before citing a frame.
- L-51x (2026-11-27): re-running a whole engine each morning is not 'daily anchoring' - the chain's own timing rules (6.10 +1 day) re-apply every morning and push events out of the week; hold a chain while it holds, act when it fails.
- L-52x (2026-11-27): an order 'existing' only from a day's London open loses the Asian session his trades use (golden Friday long filled 02:15 UTC) - an order's life starts at its trading day's open.
- L-53x (2026-11-27): improving the drawn E2 and improving the orders can pull apart (re-anchored chains: better line, fewer winners) - measure each layer separately before adopting a change for both.
- L-54x (2026-11-27): a report to him always carries all three pairs and the whole week in one fitted frame each (M-60).
- L-55x (2026-11-27): his golden weeks are ONE Law-27 flow on every pair (each entry = the previous trade's TP, within ~3 pips, one trade at a time). A second order for a move that is still running is the defect he sees as 'a C' - check new order logic against that flow before anything else.
- L-56x (2026-11-27): a canon line that reads as universal ('No exceptions') can still contradict his own golden numbers on my data (Trading Laws stop rule vs his stops inside V1 rungs) - measure it on his trades before adopting; his hand outranks my reading.
- L-57x (2026-11-27): a cross-pair input under daily anchoring must be the source pair's record OF THAT DAY (decided at that day's anchor), never the source's whole-week result - the whole-week result carries later days' decisions into Monday. Run tools/leak_check.py on every pair of a change (GBPUSD caught it, DXY / EURUSD did not), and never pipe it through tail without keeping its exit code.
- L-58x (2026-11-27): an Engine 2 change can reach code paths of Engine 3 that the count maps never exercise (D-139 -> alternative chains with an IP-target from-zone -> KeyError on 3 of 75 maps). After every E2 change run the tool over EVERY cached pair-week (scratchpad sweep.py), not only the golden week and the 12 locator maps.

## 4. His golden-week trades (context_management/oracle/golden_week.json) - the S2 oracle

### DXY

| # | Day | Dir | Entry | SL | TP | Tag |
|---|---|---|---|---|---|---|
| 1 | Mon | LONG | 100.945 | 100.905 | 101.115 | SS long @1H LQZ |
| 2 | Mon | SHORT | 101.14 | 101.2 | 100.845 | BS short @1H LQZ |
| 3 | Tue | LONG | 100.845 | 100.77 | 101.19 | SS long @1H MoM |
| 4 | Wed | SHORT | 101.19 | 101.25 | 100.975 | SS short @1H LQZ |
| 5 | Wed | LONG | 100.975 | 100.905 | 101.24 | RWL long @1H LQZ |
| 6 | Wed | SHORT | 101.235 | 101.33 | 100.68 | BS short @4H BoM (g1 shows it as 101.275 / 101.33 / 100.675) |
| 7 | Thu | SHORT | 100.975 | 101.09 | None | ladder short (levels read from g4; TP not legible) |
| 8 | Fri | LONG | 100.615 | 100.545 | 100.94 | WL + RWL long at the floor (g2: entry 100.615, SL 100.545, TP 100.94 = bottom of the pivot band) |

### EURUSD

| # | Day | Dir | Entry | SL | TP | Tag |
|---|---|---|---|---|---|---|
| 1 | Mon | SHORT | 1.14322 | 1.14408 | 1.14103 |  |
| 2 | Mon | LONG | 1.14106 | 1.14039 | 1.14442 |  |
| 3 | Tue | SHORT | 1.14441 | 1.14505 | 1.14004 |  |
| 4 | Wed | LONG | 1.14012 | 1.13964 | 1.14276 |  |
| 5 | Wed | SHORT | 1.14277 | 1.14325 | 1.1395 |  |
| 6 | Wed | LONG | 1.13953 | 1.13868 | 1.14544 |  |
| 7 | Thu | LONG | 1.14233 | 1.14183 | 1.14544 | reinforcement on trade 6 (same TP) |
| 8 | Fri | SHORT | 1.14578 | 1.14649 | 1.14205 |  |

### GBPUSD

| # | Day | Dir | Entry | SL | TP | Tag |
|---|---|---|---|---|---|---|
| 1 | Mon | LONG | 1.33331 | 1.33224 | 1.33941 |  |
| 2 | Mon | SHORT | 1.33934 | 1.34075 | 1.33347 |  |
| 3 | Wed | LONG | 1.3333 | 1.33199 | 1.34246 |  |
| 4 | Wed | LONG | 1.33629 | 1.33522 | 1.34246 | reinforcement on trade 3 (same TP) |
| 5 | Thu | SHORT | 1.34246 | 1.3436 | 1.33882 |  |
| 6 | Thu | LONG | 1.33829 | 1.3375 | 1.34485 |  |
| 7 | Fri | SHORT | 1.34481 | 1.34587 | 1.34021 |  |

## 5. Environment facts (as of the handover)

- Repository: github.com/leviathan-devops/plutus-vision (PUBLIC). Working branch AGENT; handover branches handover-70pct-functional and handover-85pct-v3-full (L-59); branch `handover` = the original canon + weekly report oracles (a branch name `handover/...` is impossible next to it). Tags cannot be pushed (the remote refuses them).
- Pinebox (the only test environment): `tools/pinebox-bootstrap.sh` (needs /home/user/inputs/pinebox, archive part 5); `export PATH=$HOME/.local/bin:$PATH XDG_RUNTIME_DIR=/run/user/0`; session `plutus-main`; after a worker restart the station dies (`pinebox list` shows "alive": false) -> `pinebox down --session plutus-main; pinebox up --session plutus-main --adapter xvfb --pair DXY --tf 1H` (plain `pinebox up` is refused: slot :0 is the operator's). Render ONE map at a time; check the `pb ide` box count before citing a frame. Bar store: TV bars DXY / EURUSD / GBPUSD x 15m / 30m / 1H / 4H, 2025-02-02 -> 2026-11-06 (~/.local/share/pinebox/data/tv-bars, archive part 7).
- V1 harvests are cached in e1_tool/cache/v1s/: PAIR_TF_MONDAY.json (week anchor) and PAIR_TF_MONDAY_<ms>.json (a daily update instant). A run that needs an uncached instant calls the Pinebox station (tools/pine-probe.py -> http://127.0.0.1:9741/model) - 'Connection refused' = the station is down.
- Network: hosts allowed by the operator during the session include www.forexfactory.com, www.treasurydirect.gov, www.newyorkfed.org, markets.newyorkfed.org, www.eia.gov. Forex Factory serves a Cloudflare challenge; a headless-browser load was refused by the session's permission check - Protocol F stays NO DATA (L-54: do not raise it again). The OpenCode key is injected by the network proxy for opencode.ai (send `Authorization: Bearer proxy-injected`); never look for, print or ask for it.
- Hooks: the operator's ECC GateGuard blocks the first write to a new path and destructive commands until the facts are stated (files, what it supersedes, where linked, rollback, his instruction verbatim) - state them and retry; never disable it. The pre-commit hook runs tools/leak_check.py (golden DXY + EURUSD) when e1_tool/*.py is staged. A Stop hook requires everything committed and pushed.
- Python: run with PYTHONDONTWRITEBYTECODE=1 for baseline / comparison runs (tracked .pyc files otherwise change and block stash / checkout).
- Never: edit indicator/plutus-vision-v1.sealed.pine; touch SHIP_PACKAGES or a plutus-browser tree (R-39); put a price literal or per-week constant in Python; feed anything after the anchor into a map; quote a locator number as a verdict.
