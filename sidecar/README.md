# PLUTUS VISION sidecar — Engine 1 web inputs, as they stood at the weekly anchor

The Pine indicator forecasts each FX week from what existed at that week's anchor:
**Monday 02:00 America/New_York** (06:00 UTC in US summer time, 07:00 UTC in winter time; computed DST-aware).
This sidecar harvests the web part of Engine 1 for one week, as of that instant, and emits

- `out/<week>.json` — one file per week (`sidecar/run --week 2026-07-06`)
- `out/pine_inputs.json`, `out/pine_inputs.<SYMBOL>.txt` — the dated dataset strings the Pine script takes as inputs (`sidecar/build-inputs`)

Sources and method were proven by the scout: `context_management/spec/SIDECAR_SCOUT.md`. Canon meaning of the data: `context_management/spec/E1_ALGO.md` (P3, P4, P8, section 6).

## Run

```
sidecar/run --week 2026-07-06          # Monday, YYYY-MM-DD  -> out/2026-07-06.json
sidecar/run --week 2026-07-06 --offline  # raw cache only; fails OFFLINE_MISS instead of fetching
sidecar/build-inputs                   # every out/<week>.json -> pine_inputs.*
```

Other flags: `--fresh` (delete the week's durable storage first), `--force-include <post url>` (adds a post to the source set regardless of
its date — exists to demonstrate the refusal below). Environment: `AETHER_HOME` (default `/home/user/inputs/aether/aether_agent_backend_v2`),
`SIDECAR_VERBOSE=1` (print each step), `SIDECAR_NO_MODEL=1` (fail `MODEL_CACHE_MISS` rather than call the model).
Needs `bun`, `python3` with Pillow + numpy, `curl`.

Exit codes: 0 written; 2 bad input / step failure; **3 `ASOF_VIOLATION`**; 4 `MODEL_STEP_FAILED`; 5 `AETHER_MISSING`; 64 usage.

## The three hard rules and where they live

1. **As-of.** Nothing published after the anchor is used. Posts are chosen from the weekly sitemap by `lastmod <= anchor` (a later Monday post
   is not even fetched), then each fetched page's own `article:published_time` is checked. Every datum in the week JSON carries `source_url` +
   `published_at`. `asofGate` (lib.ts) runs in step `asof_gate`, again in `emit` over every source, expiry entry and analyst level, and again in
   `build-inputs`; on a violation it refuses with `ASOF_VIOLATION` and exit 3, nothing is written. Proof command:
   `sidecar/run --week 2026-04-20 --force-include https://investinglive.com/Orders/fx-option-expiries-for-20-april-10am-new-york-cut-20260420/`
   (that post went out 06:08:28Z, 8 minutes after the anchor) → `FAILED ASOF_VIOLATION ... [step asof_gate]`, exit 3.
   H.10: release instant = release date 16:15 New York. Spots: last 1H bar whose close time (`time` + 1h) is `<=` the anchor.
2. **No invention.** A strike/notional is accepted only when two independent model reads show the identical strike, notional, currency and row
   date. Read A = the whole table magnified 2.2x; read B = two magnified halves (4x, cut on detected grid lines). Where A and B differ for a
   pair column, a third read C of that single column (6x) is taken and an entry needs 2 of 3. Everything else is dropped and listed under
   `dropped` with its vote count. A read whose first row date is not the post's cut date is discarded whole. `[UNCLEAR]` never parses, so it
   can never be accepted. Analyst levels: one model read per week, and every level is then verified mechanically — the quote must be a verbatim
   substring of the article body and must contain the price; failures are dropped and logged.
3. **Deterministic.** Outputs are a pure function of the cached raw pages and cached model reads: no clock values in `out/`, sorted keys/rows.
   Re-running a finished week makes 0 requests and 0 model calls and reproduces the file byte for byte.

## Step graph (durable task `sidecar.week`, one phase per step)

```
resolve_anchor → discover → fetch_pages → asof_gate → prepare_views → read_expiries* → reconcile → read_tiebreak* → accept → read_analyst* → convert → emit
                                                                        (* = MODEL step; every other step is plain code)
```

| Step | What it does |
|:--|:--|
| resolve_anchor | Monday 02:00 New York → UTC |
| discover | weekly sitemaps `sitemaps/news/articles/<ISO week>.xml` (anchor week + previous); picks the anchor Monday's expiry post if published by the anchor, the last expiry post of the previous 4 days (normally Friday), and up to 4 analyst candidates (`/forex/`, `/technical-analysis/`, slug names EUR/USD, GBP/USD, DXY/dollar index, published in the 4.5 days before the anchor) |
| fetch_pages | article HTML (only `<head>` meta and `div[data-ref="article-body"]` are parsed — the page sidebar is today's content), Fed H.10 release |
| asof_gate | refuses if any fetched page is later than the anchor |
| prepare_views | table JPEG → grid detection → PNG views A, B1, B2, C0..C7 (`src/views.py`, Pillow, deterministic) |
| read_expiries* | reads A, B1, B2 of each image |
| reconcile | compares A with B per pair column, lists the columns that need a third read |
| read_tiebreak* | read C of each disputed column |
| accept | 2-of-2 or 2-of-3 identical → accepted; else dropped |
| read_analyst* | explicit DXY / EUR/USD / GBP/USD levels from the candidate articles; quotes verified against the text |
| convert | spots from the Pinebox bar store; `k_anchor = DXY_spot × EURUSD_spot^0.576`; union, cluster, tier; `DXY level = k_anchor × strike^(-0.576)` (canon Pillar 8); H.10 K recorded for audit only |
| emit | final as-of gate, writes `out/<week>.json` |

### What runs on aether, what is plain code

The task runs on the framework in `aether_agent_backend_v2`: `@earendil-works/pi-durable` `Harness` + `defineTask` (a durable state machine,
checkpoint committed at every step; a killed run resumes from its last checkpoint on the next `run`), sqlite storage per week, and pi-ai's
`opencode-go` provider. Model pin = the aether default (`opencode-go / muse-spark-1.3-contributor`), thinking level `high`, sent to
`https://opencode.ai/inference/go/openai/v1/responses` with `Authorization: Bearer proxy-injected` (the process only ever holds that literal;
the network proxy substitutes the key) and the provider's `x-opencode-session` header.
There is no agent loop: the model is offered no tools and no system sections. Each model step is one fresh task-owned conversation with one
input and one answer, so reads share no context. All of it sits behind one function, `modelStep` in `src/model.ts`.
`AetherDurableHarness.run()` itself is not used: it is text-only, requires an edit target (`promptFilePath`), installs the coding tools and
routes through a local key-cycler on port 4097 that does not exist here. `src/model.ts` repeats its wiring (models → storage → registry →
`Harness.open` → root → resume) without those parts. Everything else (`src/lib.ts`, `src/views.py`, `src/build-inputs.ts`) is plain code.

## Week JSON

`{week, anchor_utc, sources[{url,published_at,kind}], expiries{PAIR:[...]}, spots, k_anchor, h10, dxy_levels[], analyst_levels{}, read_stats, model, dropped[], log[]}`

Expiry entry: `{strike, notional_m, ccy, cut_date, state, tier, code, reads_agree, reads_total, cluster_of?, source_url, published_at}`.

- **Which rows.** Monday post (if admissible): Monday row and the next-day forward row (Day 2, admissible because it is on the Day-1 page).
  Previous Friday's post: its forward row (Monday) and its own Friday row. Same pair + cut date + strike seen in two posts → the larger notional is kept.
- **state.** `live` = cut date on/after the anchor Monday; `ghost` = cut date before it (canon zone type "Post-Expiry Ghost": the Friday rows that expired at Friday 10am New York).
- **Cluster rule** (canon v4.5.2 line 938, "cluster within 10 pips: aggregate notionals"): within one pair and one cut date, strikes within 10 pips
  (0.0010; 0.10 for JPY pairs) are merged before tiering — notionals summed, strike = notional-weighted mean, members kept in `cluster_of`.
  Clusters are built greedily from the lowest strike and never span more than 10 pips. Strikes below the tier floor take part (the rule is applied before tiering).
- **tier** on the (aggregated) face notional in the currency printed in the table: 1 = ≥ 1.5bn CRITICAL OPTION WALL, 2 = 850m–1.499bn SIGNIFICANT MAGNET, 3 = below (kept in the JSON, never in a dataset).
  No currency conversion to USD is applied (the scout control treats €830m as excluded).
- **code** (dataset): 1 live tier 1, 2 live tier 2, 3 ghost tier 1, 4 ghost tier 2, `null` for tier 3.
- `dxy_levels`: tier 1/2 EUR/USD entries only, `price = k_anchor × strike^(-0.576)`.
- `analyst_levels`: `{price, role, source_url, published_at, quote}` for DXY / EURUSD / GBPUSD. A EUR/USD level is never converted into a DXY level (canon P8: the conversion is for option strikes only).

## Dataset strings (`build-inputs`)

`pine_inputs.json = {"DXY": "...", "EURUSD": "...", "GBPUSD": "...", "analyst": {"DXY": "...", "EURUSD": "...", "GBPUSD": "..."}, "meta": {...}}`.
A dataset is one string of rows `YYYYMMDD|price:code,price:code;` — YYYYMMDD is the anchor Monday, prices ascending in the symbol's own units
(DXY rows from `dxy_levels`, 2 decimals; pair rows from that pair's own strikes, 4 decimals). When two entries print the same price in one week
(e.g. a ghost and a live strike) the lower code is kept. A week with no qualifying level has no row. Analyst rows use code 9 (investinglive is
not in the canon source-tier table, so no canon weight is asserted). `meta.lengths` gives each string's length. `out/read_stats.json` holds the read-agreement counts.

## What is cached

| Path | Content |
|:--|:--|
| `raw/<week>/` | sitemaps, article HTML, table JPEGs, H.10 pages, each with a `.meta.json` (url, fetch time, status). File names follow the scout's, so its saved pages are reused. |
| `cache/views/<image sha>/` | the PNG views and `views.json` (grid lines, crop boxes, zoom) |
| `cache/reads/<key>.json` | every model answer verbatim; key = sha256(model, effort, step kind, prompt, image bytes) |
| `cache/work/<week>.json` | step outputs of the last run of that week |
| `cache/aether/<week>.sqlite` | the durable harness storage: task checkpoints and the full committed transcript of every model step |
| `cache/shared/` | the H.10 release-date index |

## Known blockers and limits

- **Analyst sources.** `www.forex.com` (Cloudflare challenge; no way to list past dates), `think.ing.com` / `www.ing.com`, `www.fxstreet.com`,
  TradingView, `web.archive.org` are blocked or refused by this network. Analyst levels therefore come only from investinglive posts, which rarely
  print DXY or GBP/USD levels in text; chart-image and video levels are not read. Canon's Tier-1 analyst sources are absent.
- **Monday post vs anchor.** investinglive publishes the Monday expiry table between about 05:45Z and 06:20Z. With the anchor at 02:00 New York some
  weeks include Monday's own post and some only Friday's forward row (fewer strikes, earlier notionals, no Tuesday row). `out/read_stats.json`
  lists which posts each week used.
- **Slug years.** From 2026-07-09 the expiry slugs carry no year; the post's year is taken from its publish time.
- **Edits after publication** cannot be detected (the site's `modified_time` was overwritten by its July 2026 migration; no archive access).
  The sitemap files and the H.10 index are today's copies; only entries dated at or before the anchor are used from them.
- **Gateway terms (from the scout, for the operator):** the model entry is flagged `training: true`, not ZDR; the Go plan describes itself as for
  coding-agent traffic. investinglive's `robots.txt` disallows named AI crawlers; the sidecar fetches about 6–10 pages per week, under one request per second, once (cached).
- **Pine string length.** `meta.lengths` — check against the Pine `input.string` size limit before pasting a long history.
- A table whose grid is not detected gets a single view only, so nothing from it can be cross-checked or accepted (logged).
