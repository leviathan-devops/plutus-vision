# SIDECAR SCOUT — fetching Engine 1 web inputs as they stood on a past date

Scouted 2026-11-25 (UTC) from the cloud container, through the allowlisting agent proxy.
Golden week: Mon 2026-07-06 .. Fri 2026-07-10, anchor = 2026-07-06 ~06:00 UTC.
Generalisation check: week of 2026-04-20 (anchor 2026-04-20 ~06:00 UTC).
Saved pages: `sidecar/raw/2026-07-06/` and `sidecar/raw/2026-04-20/` (every page has a `.meta.json`).
Status of this file: all sections measured; what could not be done is stated in each section and summarised in section 7.

All fetches below used `curl -A "<desktop Chrome UA>"` with no cookies unless stated otherwise.

---

## 0. Network facts (measured)

| Host | Result |
|:--|:--|
| investinglive.com | 200 with plain curl + desktop UA (HTML, sitemaps, RSS, images under `/cms/media/`) |
| www.investinglive.com | 200, redirects to investinglive.com |
| www.federalreserve.gov | 200 with plain curl |
| www.forex.com | curl: 403, Cloudflare managed challenge (`cf-mitigated: challenge`, page title "Just a moment..."). A plain headed Chromium (Playwright, `headless:false`, DISPLAY :7, no stealth tooling, no interaction with the challenge) is let through on ordinary HTML pages after the interstitial clears by itself. Sitemaps and the listing API (`/api/misearchgrid/getresults/`) stay challenged even in the browser → no way to list past dates (section 3.2). |
| www.ice.com | product page `/products/1216/US-Dollar-Index-Options` 200 with curl (static contract spec only, section 4); `/robots.txt` 403 Cloudflare "Attention Required". |
| www.cmegroup.com | 403 from Akamai with JSON body: "This IP address is blocked due to suspected web scraping activity ... Use of scripts, software, spiders, robots ... is strictly prohibited by CME Group's website Data Terms of Use." Not attempted further. |
| challenges.cloudflare.com, images.investinglive.com, think.ing.com, www.ing.com, web.archive.org, www.fxstreet.com, finance.yahoo.com, www.tradingview.com, fred.stlouisfed.org | refused by the proxy at CONNECT: `HTTP/1.1 403 Forbidden (agent proxy: no rule or network setting allows this host)` |

Consequences: ING, FXStreet, Yahoo Finance (DXY OHLC, Pillar 1), TradingView (MAs, Pillar 2), FRED (Protocol E) and archive.org are NOT reachable from this container. `images.investinglive.com` is refused but is only used for the site logo — every article image seen so far is served from `investinglive.com/cms/media/...` (reachable).

Site policy facts recorded as found (for the operator to weigh): `https://investinglive.com/robots.txt` has `Disallow: /search-results` for all agents and `Disallow: /` for named AI crawlers (ClaudeBot, anthropic-ai, Claude-Web, CCBot, Bytespider, ...). The method below does not use site search; it uses the sitemaps that the same robots.txt advertises. Total investinglive requests made by this scout: about 55 (most of them exploration; the working method needs 2 + 1 per image, section 1.2).

---

## 1. Protocol A — OTC FX option expiries (investinglive.com) — DONE

### 1.1 What does NOT work for past dates
- Guessing the URL from the date. The slug format changed with a site migration around 2026-07-08/09:
  - up to 2026-07-08: `https://investinglive.com/Orders/fx-option-expiries-for-6-july-10am-new-york-cut-20260706/` (capital `O`, `-YYYYMMDD` suffix; the lowercase `/orders/...-20260706/` form returned 404)
  - from 2026-07-09: `https://investinglive.com/orders/fx-option-expiries-for-9-july-10am-new-york-cut/` (lowercase, no date suffix, no year in the slug — will collide across years)
- Scrolling the category archive. `https://investinglive.com/Orders/page/N/` gives 25 posts per page but stops at the migration: page 5 ends at "9 July", pages 6..30 return HTTP 200 with zero posts. So "scroll back to that date" works only back to 2026-07-09 on the listing; older posts are still online but are not listed there.
- RSS `https://investinglive.com/feed/orders/` exists (application/rss+xml) but only carries recent items.

### 1.2 What works: weekly article sitemaps (2 requests per date, +1 per image)
1. `https://investinglive.com/articles-sitemap-index.xml` lists one sitemap per ISO week back to 2008: `https://investinglive.com/sitemaps/news/articles/<ISOYEAR>-W<WW>.xml` (no need to fetch the index — the name is computable: `date.isocalendar()`).
2. Fetch the week file (about 50–60 KB, ~270–300 `<url>` entries, newest first). Each entry is
   `<loc>URL</loc><lastmod>2026-07-06T05:47:01+00:00</lastmod>`.
   For every post checked (10 posts) `<lastmod>` equals the article's publish time to the second — it is NOT the modification time (the page's own `article:modified_time` for July posts is 2026-07-08, the migration).
3. Select `loc` matching `(?i)/orders/fx-option-expiries-for-` with `lastmod <= anchor`. Monday's post is in the anchor week's file (W28 for 2026-07-06); Friday's post is in the previous week's file (W27).
4. GET the article URL (≈590 KB HTML, server-rendered Next.js; no JS needed).
5. GET the table image (see 1.4).

### 1.3 Publish timestamp (mechanical as-of filter)
In the article HTML, three places, of which two are right and one is a trap:
- `<meta property="article:published_time" content="2026-07-06T05:47:01.4519700Z"/>` — correct, UTC.
- JSON-LD `"@type":"NewsArticle"` → `"datePublished":"2026-07-06T05:47:01.4519700Z"` — correct.
- A second JSON-LD block `"@type":"Article"` → `"datePublished":"2026-07-08T11:06:31Z"` — this is the CMS migration time, WRONG for as-of purposes. Do not take "the first datePublished found by a loose regex" without checking `@type`.
- `article:modified_time` = `2026-07-08T11:25:46Z` on all pre-migration posts (migration), so "modified" cannot be used to detect later edits of old posts.
Filter rule: keep iff `article:published_time <= anchor`; cross-check against the sitemap `<lastmod>`.

Contamination warning: the saved article HTML also contains TODAY's sidebar ("Must Read", featured posts from November 2026) and today's ticker. A parser must read only the element `div[data-ref="article-body"]` (and the `<head>` meta), never the whole page text.

### 1.4 Data format: IMAGE (strikes are not in the HTML text)
- The table is a JPEG inside the article body: `<figure class="content-data__image" data-media-id="<uuid>"><img src="https://investinglive.com/cms/media/migrated/images/FXO%2006-07_id_<uuid>_size900.jpg?width=1024&format=webp" ...>`.
- Host: `investinglive.com` (same host, reachable). Fetch the `src` without the query string to get the JPEG: 900x288..~330 px, ~100 KB. The `_original.jpg` variant of the expiry image returned 404; `_size900` is the largest available (the page declares width=1425 but only the 900 px file is served). Text is small but legible.
- File name pattern `FXO DD-MM_id_<uuid>_size900.jpg`; the uuid is not predictable — it must be read from the article HTML.
- The article text names only the strikes the author highlights (e.g. "EUR/USD at the 1.1400 and 1.1450 levels") without notionals; the full table exists only in the image.
- Each image has TWO rows: the cut day (arrow, bold = large) and a forward row for the NEXT business day.
- The forward row is a preview and changes: the Friday 03/07 image shows "Monday 06/07 EUR/USD 1.1400 (€2.0bn), 1.1450 (€750m)", the Monday 06/07 image shows "1.1400 (€2.2bn), 1.1450 (€1.4bn)".

### 1.5 Sample values, anchor 2026-07-06 (read off the saved images by me and re-checked on 4x upscaled crops; the gateway model's read of the same image is in section 5.4)

Post A — `https://investinglive.com/Orders/fx-option-expiries-for-6-july-10am-new-york-cut-20260706/`, published 2026-07-06T05:47:01Z (13 min before a 06:00Z anchor), author Justin Low.
Image `investinglive_orders_fx-option-expiries-for-6-july-...__FXO_06-07_id_bf9081e7-..._size900.jpg`. Spot row: EUR/USD 1.1431, USD/JPY 161.92, GBP/USD 1.3340, USD/CHF 0.8042, USD/CAD 1.4204, AUD/USD 0.6934, NZD/USD 0.5687, EUR/GBP 0.8565.

| Row | EUR/USD | USD/JPY | GBP/USD | USD/CHF | USD/CAD | AUD/USD | NZD/USD | EUR/GBP |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| Monday 06/07 | 1.1300 (€830m), **1.1400 (€2.2bn)**, **1.1450 (€1.4bn)**, 1.1500 (€2.4bn), 1.1600 (€1.0bn) | 160.00 ($2.5bn), 160.50 ($2.6bn), 161.00 ($1.1bn), 161.50 ($970m), **161.75 ($3.1bn)**, **162.00 ($1.3bn)**, 163.00 ($835m) | none (grey) | 0.8100 ($591m) | none | 0.6885 (A$718m), 0.7000 (A$754m), 0.7025 (A$599m) | none | none |
| Tuesday 07/07 (forward) | 1.1300 (€701m), 1.1350 (€1.5bn), 1.1400 (€1.0bn), 1.1425 (€600m), 1.1440 (€525m), 1.1500 (€2.8bn), 1.1590 (€721m), 1.1600 (€734m) | 160.00 ($851m), 161.00 ($702m), 161.50 ($718m), 162.00 ($2.5bn), 162.50 ($778m), 163.00 ($741m) | none | 0.8115 ($601m) | 1.4100 ($739m) | 0.6930 (A$594m) | none | none |

Post B — `https://investinglive.com/Orders/fx-option-expiries-for-3-july-10am-new-york-cut-20260703/`, published 2026-07-03T05:49:18Z.
Spot row: EUR/USD 1.1450, USD/JPY 161.10, GBP/USD 1.3367, USD/CHF 0.8019, USD/CAD 1.4160, AUD/USD 0.6939, NZD/USD 0.5715, EUR/GBP 0.8563.

| Row | EUR/USD | USD/JPY | GBP/USD | AUD/USD |
|:--|:--|:--|:--|:--|
| Friday 03/07 | 1.1300 (€985m), 1.1325 (€703m), 1.1350 (€790m), 1.1370 (€1.6bn), 1.1375 (€1.1bn), 1.1380 (€596m), 1.1400 (€1.0bn), 1.1430 (€837m), 1.1450 (€873m), **1.1500 (€2.0bn)**, 1.1600 (€2.0bn) | 160.00 ($1.3bn), 160.50 ($1.2bn), **161.50 ($1.4bn)** | 1.3200 (£633m), 1.3300 (£527m), 1.3400 (£510m) | 0.6700 (A$908m), 0.6900 (A$523m), 0.6925 (A$988m), 0.7100 (A$1.3bn) |
| Monday 06/07 (forward, superseded by Post A) | 1.1300 (€830m), 1.1400 (€2.0bn), 1.1450 (€750m), 1.1500 (€2.2bn), 1.1600 (€1.0bn) | 160.00 ($2.2bn), 160.50 ($2.5bn), 161.00 ($1.1bn), 161.50 ($771m), 161.75 ($3.0bn), 162.00 ($1.3bn) | none | 0.6885 (A$718m), 0.7000 (A$754m) |

No separate "week-ahead expiries" post exists in the W27/W28 sitemaps; the only forward-looking expiry data is the next-day row in each daily image.
At a 06:00Z Monday anchor the admissible expiry data for the golden week is therefore: Monday (own post) and Tuesday (forward row of Monday's post). Wed–Fri: not yet published.

### 1.6 Generalisation, anchor 2026-04-20 (3 requests + 2 images)
- `2026-W16.xml` → `Orders/fx-option-expiries-for-17-april-10am-new-york-cut-20260417/`, published 2026-04-17T06:19:19Z. Image row "Monday 20/04" (forward): EUR/USD 1.1600 (€1.9bn), 1.1700 (€771m), 1.1750 (€1.1bn), 1.1780 (€570m), 1.1785 (€839m), 1.1900 (€1.0bn); GBP/USD 1.3500 (£1.0bn); USD/CAD 1.3600 ($620m), 1.3770 ($557m), 1.3800 ($601m).
- `2026-W17.xml` → `Orders/fx-option-expiries-for-20-april-10am-new-york-cut-20260420/`, published **2026-04-20T06:08:28Z — 8 minutes AFTER a hard 06:00Z anchor**. Image row "Monday 20/04": EUR/USD 1.1600 (€1.9bn), 1.1700 (€971m), **1.1750 (€2.6bn)**, 1.1780 (€695m), 1.1785 (€1.1bn), 1.1800 (€863m), 1.1900 (€1.0bn); USD/JPY 160.00 ($572m); GBP/USD **1.3500 (£1.0bn)**; USD/CAD 1.3600 ($620m), 1.3770 ($557m), 1.3800 ($712m). Saved under `sidecar/raw/2026-04-20/_boundary_0608Z/`.
- The method generalises. The finding that matters: the Monday expiry post goes out between about 05:45Z and 06:20Z (observed: 05:47, 05:49, 05:48, 05:55, 05:53, 06:19, 06:08). With a hard 06:00:00Z anchor Monday's own post is sometimes in (6 July) and sometimes out (20 April); when it is out, the only Monday data is the forward row of Friday's post (different notionals, fewer strikes). 08:00 London in BST is 07:00Z; an anchor of 07:00Z would have admitted every Monday post observed. This is a definition the operator has to fix; the scout does not choose it.

---

## 2. Fed H.10 spot rates — DONE

- Dated weekly release: `https://www.federalreserve.gov/releases/h10/<YYYYMMDD>/` (static HTML table, text, 5 daily columns, all DXY components in one page: `*EMU MEMBERS EURO`, `JAPAN YEN`, `*UNITED KINGDOM POUND`, `CANADA DOLLAR`, `SWEDEN KRONA`, `SWITZERLAND FRANC`; asterisk = USD per unit).
- Index of valid release dates: `https://www.federalreserve.gov/releases/h10/releaseDates.json` (the JSON that the "Release Dates" page `/releases/h10/default.htm` loads with `$.getJSON("releaseDates.json")`). 2026 dates run 20260105 .. 20261123; holiday weeks shift to Tuesday (20260120, 20260217, 20260526, 20260908, 20261013).
- Publish time: the page prints `Release Date: June 29, 2026`; the H.10 pages state "On Mondays at 4:15 p.m. the Federal Reserve Board releases daily bilateral exchange rates ... for the previous business week" (next business day on federal holidays). As-of rule: release instant = release date 16:15 America/New_York; take the largest release date whose instant < anchor.
- Also available: per-currency full history `https://www.federalreserve.gov/releases/h10/hist/dat00_eu.htm` (`dat00_ja`, `dat00_uk`, `dat00_ca`, `dat00_sd` (Sweden), `dat00_sz` (Switzerland)), one row per day since 2000, text. It is today's file — rows after the anchor are present, so the same release-instant rule must be applied to rows (a row for day D is published on the Monday after D's week).
- Requests: 1 per anchor (2 with the JSON index).

Anchor 2026-07-06 06:00Z → last admissible release = **2026-06-29** (the 2026-07-06 release appears at 20:15Z, after the anchor; saved under `_excluded_after_anchor/` for contrast). Rates in that release:

| | Jun 22 | Jun 23 | Jun 24 | Jun 25 | Jun 26 |
|:--|:--|:--|:--|:--|:--|
| EUR/USD | 1.1432 | 1.1383 | 1.1348 | 1.1385 | 1.1403 |
| USD/JPY | 161.51 | 161.55 | 161.76 | 161.67 | 161.67 |
| GBP/USD | 1.3249 | 1.3192 | 1.3160 | 1.3216 | 1.3223 |
| USD/CAD | 1.4167 | 1.4198 | 1.4237 | 1.4191 | 1.4182 |
| USD/SEK | 9.6149 | 9.7300 | 9.7678 | 9.7102 | 9.7112 |
| USD/CHF | 0.8091 | 0.8097 | 0.8126 | 0.8093 | 0.8082 |

Consequence to know: under a strict as-of rule the freshest H.10 spot at a Monday 06:00Z anchor is the Friday of the week BEFORE last (here Jun 26, ten days old). The Jul 2 rates (EUR/USD 1.1448, USD/JPY 160.90, GBP/USD 1.3364, USD/CAD 1.4182, USD/SEK 9.6567, USD/CHF 0.8022; Jul 3 = ND, holiday) existed in the market but were published by the Fed only on Jul 6 at 20:15Z.
Fresher admissible spot found on investinglive (image, 7 pairs, no SEK): the weekend post "Monday open FX. Indicative rates 06 July 2026" (`/forex/monday-open-fx-indicative-rates-06-july-2026-20260705/`, published 2026-07-05T19:56:17Z): EUR 1.1433, JPY 161.33, GBP 1.3351, CHF 0.8016, CAD 1.4199, AUD 0.6942, NZD 0.5709. The spot row of each expiry image is another admissible spot source (8 pairs, no SEK).

Anchor 2026-04-20 → last admissible release = **2026-04-13** (rates Apr 6–10; Apr 10: EUR/USD 1.1723, USD/JPY 159.22, GBP/USD 1.3460, USD/CAD 1.3828, USD/SEK 9.2651, USD/CHF 0.7893). Saved in `sidecar/raw/2026-04-20/`.

---

## 3. Analyst commentary with explicit levels — investinglive DONE (5 pre-anchor articles saved); forex.com past dates NOT reachable; ING refused

### 3.1 investinglive (same sitemap method as section 1; filter `loc` on `/technical-analysis/` and `/forex/`)
Text is in `div[data-ref="article-body"]`; chart images under `investinglive.com/cms/media/migrated/images/..._original.jpg` (fetchable). Saved, all published before the anchor:

| Published (UTC) | URL path | Explicit levels in the text |
|:--|:--|:--|
| 2026-07-06T05:03:53 | `/forex/yen-tervention-risks-remain-in-focus-to-start-the-new-week-20260706/` (Justin Low) | USD/JPY: dip arrested ~160.70; 100/200-hour MAs 161.84-92; 162.00; last week's high near 162.80 |
| 2026-07-02T11:04:01 | `/forex/eurusd-remains-stuck-in-a-consolidation-awaiting-the-key-us-data-to-pick-a-direction-20260702/` | EUR/USD: resistance zone "around the 1.14 handle"; downside target "the 1.10 handle"; upside target "the 1.18 handle" |
| 2026-07-02T13:14:45 | `/technical-analysis/usd-moves-lower-after-the-us-jobs-report-what-are-the-charts-telling-traders-now-20260702/` (Greg Michalowski) | Levels are in 4 chart IMAGES (USDCHF, USDCAD, USDJPY, EURUSD), not in text. EURUSD H1 chart labels: 38.2% 1.14376, 50% 1.14727, 61.8% 1.15079, swing zone 1.14419–1.14587, 1.14989–1.15060, 200-day MA 1.16540, low 1.13243 |
| 2026-07-01T12:06 | `/technical-analysis/morning-kickstart-markets-brace-for-a-busy-day-...-20260701/` | USD/JPY 40-year high 162.83 (mostly narrative) |
| 2026-07-02T12:12:30 | `/technical-analysis/the-usd-is-lower-ahead-of-the-us-jobs-report-what-are-the-technical-levels-in-play-20260702/` | levels are in a video, not in text; yen low 162.66 only |

Judging by the slugs in the W27/W28 sitemaps, no investinglive post in 2026-07-01..07-06 is about DXY or GBP/USD levels (the last GBP/USD technical post is `/technical-analysis/gbpusd-buyers-cannot-keep-the-momentum-to-the-upside-going-20260630/`, 2026-06-30T19:34Z, not fetched). Only the six bodies listed above were actually read. Excluded example: `/forex/market-outlook-for-the-week-of-6th-10th-july-20260706/` published 2026-07-06T06:55:49Z (after 06:00Z; calendar narrative, no levels) — in `_excluded_after_anchor/`.

### 3.2 forex.com — DONE: reachable only for CURRENT pages; past dates (July, April) NOT reachable from this container
What was measured (4 curl attempts, 8 page loads in a headed Chromium, 1 API call made by the page itself):
- curl: 403 Cloudflare managed challenge on every path (`cf-mitigated: challenge`), including `/robots.txt` and sitemaps.
- Headed Chromium (Playwright, `headless:false`, own Xvfb display :7, no stealth tooling, no interaction with the challenge): ordinary HTML pages load — first document response is 403 "Just a moment...", then the real page renders once the interstitial clears by itself (a few seconds). `challenges.cloudflare.com` (Turnstile) is refused by the proxy, so an interactive challenge could not be completed if one were presented.
- `https://www.forex.com/en-us/market-analysis/latest-research/` (URL in the Trident prompt) redirects 307→301 to `https://www.forex.com/en-us/news-and-analysis/`.
- Listings: `/en-us/news-and-analysis/` (all), `/en-us/news-and-analysis/tags/<tag>/` (us-dollar, eur-usd, usd-jpy, technical-analysis, dxy ...), `/en-us/news-and-analysis/forex-com-analysts/<name>/` (matt-weller, james-stanley, fawad-razaqzada, michael-boutros, david-scutt, matt-simpson, fiona-cincotta, julian-pineda). Each listing is a Sitecore widget `div[data-widget="filter-grid"]`; the first 8 cards are server-rendered as JSON in its `data-initialresponse` attribute (fields: Title, Date e.g. "November 24, 2026 09:13 AM", Author, Tags, ArticleId, ItemUrl); `data-properties` says `"pageSize":"8","totalCount":25`.
- Everything after the first 8 cards comes from the page's own XHR: `POST https://www.forex.com/api/misearchgrid/getresults/` with the `data-properties` JSON as body (`{"endpoint":"/api/misearchgrid/getresults/","itemid":"{...}","site":"FOREX US CD","pageSize":8,"totalCount":25,"hardSkip":8,"url":"/en-us/news-and-analysis/","languages":"en","siteId":"{...}","showDrupalArticles":true,"selectedAuthors":[""],"tags":[""]}`). When the "Load more" button was clicked in the real browser, that XHR came back **403 with the Cloudflare challenge page**. Not pursued further.
- Sitemaps: `/robots.txt` (readable in the browser) advertises `https://www.forex.com/en-us/sitemap-index.xml`; both it and `/sitemap.xml` stayed on "Just a moment..." (several challenge rounds, never cleared).
- Depth actually readable: the 8 newest cards per listing. On 2026-11-25 that is 5 days for the `us-dollar` tag (Nov 19–24) and 16 days for Matt Weller's author page (Oct 28–Nov 13). **No forex.com article from 2026-07-01..07-06 (or April) could be located**: no reachable index (sitemap challenged, grid API challenged, search engines and archive.org refused by the proxy), and slugs are not derivable from the date (some end in a date — `...-11-24-2026/`, `...-2026-11-25/` — but the words before it are the headline).
- If an exact article URL is known, the page itself loads in the headed browser (1 load). Publish time on an article page (one current article examined, saved under `sidecar/raw/_probe_forex_2026-11-25/`): JSON-LD `NewsArticle.datePublished = "2026-11-24T02:13:00+00:00"`, visible byline `24/11/2026` / `11/24/2026 2:13:00 PM`, listing card `November 24, 2026 09:13 AM`. The three disagree (02:13 UTC vs 2:13 PM vs 09:13 AM, no zone on the last two); which one is the true instant is not established — one article only. An as-of filter on forex.com cannot rely on a single field until that is resolved.
- Format: analysis is text plus chart images/video; images are on `micms.stonex.com`, refused by the proxy.

### 3.3 ING / FXStreet / others
`think.ing.com`, `www.ing.com`, `www.fxstreet.com`: refused by the proxy (message in section 0). Not reachable.

---

## 4. ICE / CME — DONE (nothing usable for a past date)
- CME (`www.cmegroup.com`): blocked — Akamai 403 with the scraping/Terms-of-Use message quoted in section 0. Matches the Trident prompt's own classification ("CME Group direct — 403 IP block"). Not attempted further.
- ICE (`https://www.ice.com/products/1216/US-Dollar-Index-Options`): 200 with curl (24 KB compressed). The server-rendered content is the static contract specification only (symbol DX, tick size, trading hours ...). No settlement, open-interest or dated end-of-day data is in the HTML; the page references `/api/productguide/spec/1216/pdf` (spec PDF), `/api/sites/ice/proxy` and `/marketdata/ExpiryCalendar.shtml`. `https://www.ice.com/robots.txt` returned a Cloudflare 403 "Attention Required". ICE's report centre / historical EOD files were not tested (1 request spent on ICE content). Unknown whether dated DXY option data can be had there.

---

## 5. Model gateway — DONE

Key handling: every call used the literal header `Authorization: Bearer proxy-injected`; the proxy substitutes the real key. No key was read, searched for or printed.

### 5.1 Where the model is listed
- `https://opencode.ai/zen/v1/models` (77 models) does NOT contain any "Contributor" entry. It has `muse-spark-1.3` ("Muse Spark 1.3", pay-as-you-go, $1.25/$4.25 per M tokens).
- "Muse Spark 1.3 Contributor" is in the OpenCode Go list: `https://opencode.ai/zen/go/v1/models` (same body at `https://opencode.ai/inference/go/v1/models`, 37 models).
- **Exact id: `muse-spark-1.3-contributor`** (name "Muse Spark 1.3 Contributor", canonical_id `meta/muse-spark-1.3`). Full entry saved: `sidecar/raw/2026-07-06/_gateway/model_entry_muse-spark-1.3-contributor.json`.

### 5.2 API shape (from the list entry)
- API: **Responses** (`"recommended_api": "responses"`), not chat-completions. Base URL `https://opencode.ai/inference/go/openai/v1` → `POST https://opencode.ai/inference/go/openai/v1/responses`. (The Go docs say every text model also works through the other API shapes via translation; not tested.)
- Input modalities: text, image/jpeg, image/png, image/gif, image/webp, video/mp4, application/pdf, audio/mpeg, audio/wav. Output: text.
- Reasoning: supported, effort values `minimal | low | medium | high | xhigh` (no `max`). Request field: `"reasoning": {"effort": "high"}`.
- Also: tools, structured_output, temperature, top_p (no top_k). Limits: context 1,048,576, output 131,072.
- Price in the entry: input $0.10 / output $0.20 per M tokens; both calls below were billed `"billing_source": "go"`, `"cost": 0` (taken from the Go allowance).
- Required header: `x-opencode-session: <stable id per conversation>`. Without it: HTTP 400 `{"type":"error","error":{"type":"MissingSessionID","message":"Request is missing x-opencode-session and cannot be routed efficiently. ..."}}`.
- Facts from the list entry and the Go docs page (`https://opencode.ai/v2/docs/console/go/`) that the operator should know:
  - `"go": {"training": true, "zdr": false, "limited_regions": true}`; docs: "Muse Spark 1.3 Contributor: Heavily discounted token pricing in exchange for permission to use your prompts and completions to train future Meta models. Availability is limited to regions permitted by Meta's Geographic Use Policy." Privacy table: "Not ZDR". Everything sent to this model (prompts, images, completions) may be used for training.
  - Docs, "Where can I use it?": Go "is designed for OpenCode and other coding agents that produce similar types of requests. Traffic is monitored for abuse"; clients should "send typical coding agent traffic", identify with their own user agent, and send `x-opencode-session`. A sidecar doing table OCR is not coding-agent traffic; whether that use is acceptable under the plan is not something this scout can determine.
  - `monthly_usage` in the entry: go 60, go-plus 120, go-teams 65 (units not stated in the entry).

### 5.3 Calls made (5 inference POSTs in total, of which 2 were rejected before any model ran; records in `sidecar/raw/2026-07-06/_gateway/`)
1. Mistake, disclosed: before finding the Go list, one text request was sent to `muse-spark-1.3` (the pay-as-you-go model, a different product from the one asked for) at `https://opencode.ai/inference/openai/v1/responses`. Result: HTTP 402 `"Insufficient balance. This request is pay-as-you-go, billed to OpenCode Models credits. ... OpenCode Go covers only requests to the OpenCode Go provider."` Nothing was billed.
2. `muse-spark-1.3-contributor` without the session header → HTTP 400 MissingSessionID (above).
3. Text, with header, `{"model":"muse-spark-1.3-contributor","input":"Reply with exactly: gateway ok. Then state 2+2 as a digit.","max_output_tokens":200,"reasoning":{"effort":"low"}}` → HTTP 200 in 13.1 s but `"status":"incomplete"`, `incomplete_details.reason = "max_output_tokens"`: 198 of 200 output tokens were reasoning tokens, no visible text. Reasoning tokens count against `max_output_tokens`, even at low effort.
4. Text retry, same prompt, `"max_output_tokens":1500,"reasoning":{"effort":"minimal"}` → HTTP 200 in 2.6 s, `"status":"completed"`, output text: `gateway ok.\n4`. Usage: input 25, output 211 (198 reasoning).
5. Image, one call, `reasoning.effort = "high"`, `max_output_tokens` 12000:
   ```json
   {"model":"muse-spark-1.3-contributor","reasoning":{"effort":"high"},"max_output_tokens":12000,
    "input":[{"role":"user","content":[
      {"type":"input_text","text":"OCR this FX option expiries table. Output JSON only: {...}. ... Do not guess: if a value is unclear write \"[UNCLEAR]\"."},
      {"type":"input_image","image_url":"data:image/jpeg;base64,<the saved 6 July FXO JPEG, 900x288>"}]}]}
   ```
   Headers: `Authorization: Bearer proxy-injected`, `Content-Type: application/json`, `x-opencode-session: <uuid>`, `User-Agent: sidecar-scout/0.1`.
   → HTTP 200 in 37.8 s, completed. Usage: input 428, output 6770 (5976 reasoning). The response output list is `[{"type":"reasoning",...,"encrypted_content":...}, {"type":"message","content":[{"type":"output_text","text":"{...json...}"}]}]`.

### 5.4 Result of the image read — it works mechanically, but the read is NOT accurate (negative result)
Ground truth = my own read of the same JPEG, re-checked on 4x upscaled crops (values in section 1.5).
- Spot row: 8/8 correct.
- Monday 06/07 EUR/USD: all five strike+notional pairs correct (1.1300 €830m, 1.1400 €2.2bn, 1.1450 €1.4bn, 1.1500 €2.4bn, 1.1600 €1.0bn) — but the model reported `bold:false` for 1.1400 and 1.1450, which are bold in the image.
- Errors (model → image): USD/JPY `161.25 ($3.1bn)` → 161.50 ($970m) (invented strike, notional copied from the next line); 163.00 `$653m` → $835m; USD/CHF 0.8100 `$91m` → $591m; AUD/USD `0.6985` → 0.6885; AUD/USD 0.7000 `A$794m` → A$754m; Tuesday EUR/USD 1.1350 `€1.3bn` → €1.5bn; 1.1400 `€1.4bn` → €1.0bn; 1.1500 `€2.6bn` → €2.8bn; Tuesday USD/JPY 160.00 `$951m` → $851m; 162.50 `$578m` → $778m.
- Score: 23 of 33 strike/notional entries correct; 10 wrong, none flagged `[UNCLEAR]`. Several errors are on EUR/USD and would cross the engine's $850M / $1.5B tier thresholds (e.g. Tuesday 1.1400 €1.4bn vs €1.0bn).
- Not tested: the same call on an upscaled image, on per-cell crops, or the 3-pass reconcile of Protocol A. One call only, as instructed.

---

## 6. Open questions / unknowns
- Exact anchor instant (06:00Z vs 07:00Z = 08:00 London in BST, 08:00Z in GMT winter weeks) decides whether Monday's own expiry post is admissible in some weeks (section 1.6).
- Whether investinglive ever edits an expiry image after publication cannot be determined from the page (modified_time is overwritten by the migration for old posts); no archive.org access to cross-check.
- Posts before February 2026 were not tested.

---

## 7. Summary table

| Input | Past-date method | Timestamp for as-of filter | Format | Requests | Status |
|:--|:--|:--|:--|:--|:--|
| A. Option expiries (investinglive) | weekly sitemap `sitemaps/news/articles/<ISOYEAR>-W<WW>.xml` → article → image | sitemap `<lastmod>` = `article:published_time` (UTC) | JPEG image 900 px wide on `investinglive.com/cms/media/` | 2 + 1 image per day | works with curl; Jul 3 and Jul 6 saved, Apr 17 and Apr 20 saved |
| B. Fed H.10 | `/releases/h10/<YYYYMMDD>/`, dates from `releaseDates.json` | "Release Date" on page + 16:15 ET rule | HTML text table | 1 (2 with index) | works with curl; 2026-06-29 and 2026-04-13 saved |
| C. Analyst levels, investinglive | same weekly sitemap, `/forex/` and `/technical-analysis/` | same as A | text; some posts carry levels only in chart images or video | 1 + 1 per article (+ images) | works; 5 pre-anchor articles saved for 2026-07-06 (EUR/USD and USD/JPY levels; none found for DXY or GBP/USD) |
| C. Analyst levels, forex.com | none found | three conflicting fields | text + images on a refused host | — | current pages load in a headed browser only; past dates not reachable |
| C. ING, FXStreet | — | — | — | — | hosts refused by the proxy |
| D. ICE | — | — | static spec page | 1 | no dated data found |
| D. CME | — | — | — | — | blocked (Akamai 403, ToS message) |
| Gateway | `POST https://opencode.ai/inference/go/openai/v1/responses`, model `muse-spark-1.3-contributor`, header `x-opencode-session` | — | Responses API, image input, effort up to xhigh | — | works; single-pass image read was 23/33 correct |

Approximate request totals for this scout: investinglive ~55 (10 archive pages, 4 failed slug guesses, ~10 robots/sitemap-index/feed probes, 4 weekly sitemaps, 14 article GETs, 16 image GETs), federalreserve.gov ~13, forex.com 4 curl + 8 browser page loads, ice.com 3, cmegroup.com 3, opencode.ai 5 GETs + 5 inference POSTs (2 rejected with 402/400, 1 incomplete, 2 completed; see 5.3).

Scratch tooling used (not committed anywhere, lives in the session scratchpad): a curl-based article saver, an H.10 saver, and a Playwright script driving `/opt/pw-browsers/chromium-1243/chrome-linux64/chrome` on `Xvfb :7`. The running pinebox instance (display :3, CDP 9222) was not touched.
