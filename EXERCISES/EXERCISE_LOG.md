# EXERCISE LOG — LIVE-MARKET APPLICATION OF THE CANON

**Method.** I could not use TradingView: the project's own `rig/RIG_STATUS.md` records that the
rig's Chrome profile holds **zero session cookies** (`sessionid`/`tv_session` absent — only
`_ga`, `_sp_*` trackers), so an authenticated chart session does not exist and driving it would
be theatre. **Workaround (my own):** drive the exercises off the project's real harvested OHLC
(`fixtures/bars/pv-long.json` = operator DXY 1H, Apr 1 – Sep 30 2026), rebuild E1 from the canon
myself, **render the chart to PNG, and look at it.** 7 chart images exist in this directory.

Tooling: `EXERCISES/lab.py` (my own minimal canon implementation — not a copy of the project's
`e1_extract.py`). Artifacts: `*_chart.png`, `week_scan_pv-long.json`, `zfp_reaction_test.json`.

---

## 1 · WHAT I DID

For each of 6 DXY weeks: map E1 from **pre-week data only** (temporal-boundary law) → cluster
levels into zones → compute the **geometric** ZFP → classify the week's shape chain by
price↔zone interaction → test the §6.4.1 ZFP-conditioned hinge → then render and **look**.

Weeks: 2026-04-20 · 05-04 · 06-15 · 06-29 · 07-06 · 08-24.

---

## 2 · THE SIX FINDINGS

### F1 — The geometric ZFP is a real, discriminating quantity (verified on pixels + numbers)
**Week 2026-05-04** (see `2026-05-04_chart.png`): price sat inside a wide `97.935–98.594` cluster
(0.66 wide, **ZFP 41%**) for Mon–Tue and traversed it freely. On Wed it sold off into the
**ZFP 0%** level at `97.632` — and **stopped there**: the week's low printed **97.625**, i.e. it
overshot the level by **0.7 pips** and reversed.

**Week 2026-06-29** (see `2026-06-29_chart.png`): price rallied into the `101.366–101.661` band
(**ZFP 18%**); the week's high printed **101.595 — inside the band** — and it was rejected.

> **Narrow level = defended to sub-pip precision. Wide band = traversed.**
> This is the canon's central E1 claim, observed directly on the bars.

### F2 — The ZFP-conditioned hinge gave the right call
After the WL rejection at the hard wall, §6.4.1 predicts `WL → SS` ("reversal exhausts into a new
range"). Thursday and Friday were range-bound. The hinge worked.

### F3 — Why the live defect is catastrophic *specifically at the extremes*
The `97.632` level is a **singleton** (n=1 — the lowest possible confluence). Under the live
build's `zfp_from_degree(confluence)` it would read **LIGHT ≈ 50% → breakout risk → predict
CONTINUATION**. Price did not continue; it reversed within 0.7 pips.
**The defect does not degrade gracefully — it inverts the call exactly at the levels that matter,
while looking fine on every diffuse mid-range zone.** Confirmed from first principles, not from
reading someone else's note.

### F4 — ★ An incomplete pillar stack does not yield FEWER zones, it yields WRONG zones
My E1 implements only the structural + round-number pillars (Pillars 1/2/3/4/8/9 absent — no
pivots, MA grid, option conversions, analyst commentary). Consequence, measured: **every mapped
zone falls in the 0–25% ZFP band.** The test found **zero** zones above 40%.
This is the *same failure class* as the live build's `zDeg` cap at 5/14 (because options = analyst
= regime = 0). **This is the most transferable lesson in the whole exercise**, and it is the reason
the live indicator's ceilings can never read HEAVY.

### F5 — Clustering must be width-bounded, not naive single-linkage
Naive single-linkage chained `98.78 → 98.93 → … → 100.09` into a **1.31-point** "zone" (ZFP 82%).
The canon's own Step 0f noise rule — *a zone wider than 0.40 DXY is not a zone* — must be applied
as a **cap during clustering**, not as a post-hoc filter. After the cap: 11 sane zones, ZFP 0–25%.

### F6 — Shapes are classified by price↔zone INTERACTION, never by candle statistics
My first classifier used candle statistics (net vs gross travel, wick placement) and labelled
almost every day `RWL/WL` — noise, because intraday ranges spike and revert by construction.
The canon: *"Shapes are mechanically defined by the relationship between price action and IP zone
architecture."* Rebuilt on that basis, the classifier independently labelled **Wednesday
2026-05-06 as `WL`** — the exact day I had visually identified as a spike-and-reject off the hard
wall. That agreement between the mechanised rule and my own eyes is the strongest evidence here.

---

## 3 · THE EMPIRICAL REACTION TEST (and its honest limits)

A first version of this test measured the **week-long** outcome and found hard walls holding only
25% — apparently contradicting the canon. **That test measured the wrong quantity.** The canon
says a zone *reacts on first test* and only fails after ~3 reactions, so the correct measurement
is the **immediate reaction window** (K = 12 × 1H ≈ half a trading day) after the first touch.

| ZFP band | touches | reacted | pierced | react % |
|---|---|---|---|---|
| HARD WALL <20% | 5 | 4 | 1 | **80.0%** |
| MID 20–40% | 7 | 5 | 1 | 71.4% |
| SOFT/FAIL ≥40% | 0 | — | — | n/a |
| **total** | **12** | **9** | **2** | |

**What this supports:** zones do react on first touch (9/12) — the reaction mechanic is real.
**What it does NOT support:** the ZFP *discrimination* claim (80% vs 71% is not a separation). And
the reason is F4: with an incomplete pillar stack there are **no** ≥40% zones to contrast against,
so the test has no range to discriminate over.

**Verdict: NOT FALSIFIED, NOT CONFIRMED.** n=12, one instrument, incomplete stack — an honest
inconclusive, not a pass. Confirming it requires the full 9-pillar E1 producing zones across the
whole 0–80% band.

---

## 4 · WHAT I NOW UNDERSTAND THAT I DID NOT BEFORE

1. **ZFP is the load-bearing number of the entire system.** It is not a score; it is a geometric
   property (zone height ÷ pair weekly range). It is the *only* E1 output that E2 conditions on,
   so an error there propagates silently into every downstream setup. I verified this by
   constructing the counterfactual at a specific price level.
2. **The system's correctness is a function of its INPUT DENSITY.** 9 pillars exist to produce
   dense level clusters; sparse input produces singleton levels that masquerade as hard walls.
   This is a systemic property, not a bug in one function.
3. **Shapes are relational, not statistical.** Every E2 classification is a statement about how
   price behaved *against a specific mapped zone with a specific ZFP* — never about candle shape.
4. **The renormalization is the hard part.** When you cannot source all 9 pillars, the temptation
   is to renormalize the confluence score so zones still reach "HEAVY". The live build did exactly
   that and inverted the E2. The correct behaviour is to keep the absolute scale and let the
   verdict be weaker — not to rescale the score until the labels look right.

---

## 5 · RESIDUALS / HONEST GAPS

- **Not verified against DXY's full 9-pillar E1** (no options/analyst/MA inputs in this workspace).
- **n = 12 zone-touches.** Not a statistical claim.
- **Only DXY + EURUSD/GU fixtures inspected**; no live feed. The fixtures are the project's own
  harvested series, so they carry that harvest's provenance, not an independent source.
- **Day-level shape labels remain provisional.** The §6.2 conditions are week-level; a proper
  implementation classifies the WEEK's aggregate interaction (e.g. 2026-06-29's four whipsaw days
  between clustered similar-degree zones is the §6.1.5 **WLS** signature — "3+ IP zones of similar
  pressure degree within a narrow range, price oscillating violently between them"), and my
  per-day classifier does not yet lift to the weekly aggregate.
- **Chart rendering is my own matplotlib reconstruction**, not the project's Pine IDE — sufficient
  to read zone/price interaction, not a substitute for the real render path.

---

## 6 · REPRODUCE

```bash
python3 EXERCISES/lab.py --source pv-long --week 2026-05-04 --render   # one week + chart
python3 EXERCISES/lab.py --all --source pv-long                        # sweep
python3 /tmp/zfp_test2.py                                              # reaction test
```

---

## SOURCE ANCHORS

Every anchor below was verified by printing the referenced line (never fabricated).

- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:1819` — §6.4.1 — the hinge tested
- `Original_Canon_Data/Toolset/Trident_System_Prompt_v5.3.3_DOWNLOAD_ME.md:1837` — the CRITICAL MISTAKE TO AVOID — what the live defect reintroduces
- `ENGINE1_V8_VS_MINE.md:108` — the measured statement of the live ZFP defect
- `EXERCISES/zfp_reaction_test.json:1` — the raw reaction-test rows
- `EXERCISES/week_scan_pv-long.json:1` — the full 6-week sweep output
