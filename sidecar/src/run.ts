// run.ts — the durable task `sidecar.week` (a mechanical step graph; phases = steps) and its CLI.
// Steps marked MODEL call `modelStep` (model.ts); every other step is plain code (lib.ts).
import * as fs from "node:fs";
import * as path from "node:path";
import { SIDECAR, RAW, CACHE, OUT, SidecarError, anchorUtc, isoWeek, iso, ymd, net, fetchCached, loadSitemap, expirySlugDate, rawName,
  parseArticle, h10ReleaseFor, parseH10, spotBefore, parseRead, entryKey, clusterAndTier, asofGate, decOf, readJson, writeJson, sha,
  type Accepted, type ParsedRead, type RawEntry } from "./lib.ts";
import { openSidecarHarness, modelSteps, stats, MODEL, EFFORT, GATEWAY_BASE, AETHER_HOME } from "./model.ts";

export const STEPS = ["resolve_anchor", "discover", "fetch_pages", "asof_gate", "prepare_views", "read_expiries", "reconcile",
  "read_tiebreak", "accept", "read_analyst", "convert", "emit"] as const;
const MODEL_STEPS = new Set(["read_expiries", "read_tiebreak", "read_analyst"]);
type Input = { week: string; force?: string[] };
const workFile = (week: string) => path.join(CACHE, "work", `${week}.json`);
const readText = (key: string): string => readJson(path.join(CACHE, "reads", `${key}.json`)).text;

const READ_PROMPT = (note: string) => `You are transcribing one image of a table of FX option expiries (10am New York cut). Transcribe ONLY what is printed in the image.
Layout: a header row of currency pairs; a "Spot Price" row; then one row per expiry day, whose label is a weekday and a date DD/MM. Each cell lists lines "- <strike> (<notional>)". Grey cells are empty.
${note}
Return JSON only, no prose, exactly this shape:
{"pairs":["<pair as printed>", ...in column order],"spot":{"<pair>":"<spot as printed>"},"rows":[{"label":"<weekday>","date":"<DD/MM>","cells":{"<pair>":[{"strike":"<strike>","notional":"<notional>"}]}}]}
Rules: copy every digit character by character; work cell by cell, line by line, top to bottom; count the printed lines of each cell and output exactly that many items; include every pair column shown, with [] for an empty or grey cell; keep the currency symbol and the unit (m or bn) exactly as printed; never infer, round, reorder or fill a value from a neighbouring line; if any character of a strike or notional is not clearly legible write "[UNCLEAR]" for that field.`;
const NOTE: Record<string, string> = {
  A: "This image is the complete table (all pair columns).",
  B: "This image is a magnified part of the table: the row-label column followed by only some of the pair columns. Transcribe only the columns shown.",
  C: "This image is a strongly magnified single pair column next to the row-label column. Transcribe only that one column.",
};
const ANALYST_PROMPT = (anchor: string, arts: string) => `Below are market commentary articles, all published before ${anchor}. Extract ONLY explicit support/resistance or technical price levels that the text itself states for these instruments: DXY (US dollar index), EUR/USD, GBP/USD. Ignore every other instrument.
Return JSON only: {"levels":[{"article":<n>,"instrument":"DXY"|"EURUSD"|"GBPUSD","price":"<the number exactly as written>","role":"support"|"resistance"|"level","quote":"<verbatim excerpt of that article, at most 200 characters, containing the number>"}]}
Rules: quotes must be copied verbatim from the text (no paraphrase, no corrections); a level must be a number printed in the text; add nothing from your own knowledge; an article with no such level contributes nothing; an empty list is a valid answer.

${arts}`;

type Post = { role: string; url: string; lastmod: string; cut_date: string; file?: string; published_at?: string; image_url?: string | null;
  image_file?: string; views?: any; views_dir?: string; reads?: Record<string, string>; tiebreak?: number[] };
type Work = { week: string; anchor: number; log: string[]; dropped: any[]; posts: Post[]; analyst: { url: string; lastmod: string; file?: string; published_at?: string }[];
  h10: any; accepted: Accepted[]; analyst_levels: Record<string, any[]>; stats: Record<string, number>; out?: any; analyst_key?: string; h10_src?: any };

function tally(p: Post, final: boolean) {
  const year = Number(p.cut_date.slice(0, 4));
  const rd = (k?: string): ParsedRead | null => (k ? parseRead(readText(k), year) : null);
  const ok = (r: ParsedRead | null): r is ParsedRead => !!r && r.ok && r.rowDates[0] === p.cut_date;
  const A = rd(p.reads?.A), B1 = rd(p.reads?.B1), B2 = rd(p.reads?.B2);
  const bPairs = [...(B1?.pairs ?? []), ...(B2?.pairs ?? [])];
  const pairs = ok(A) && A.pairs.length ? A.pairs : bPairs;
  const notes: string[] = [];
  if (!ok(A)) notes.push(`read A unusable (${A?.error ?? `row date ${A?.rowDates[0]} != ${p.cut_date}`})`);
  if (ok(A) && bPairs.length && A.pairs.join() !== bPairs.join()) notes.push(`pair headers differ A=[${A.pairs}] B=[${bPairs}]`);
  const res = { pairs, notes, disputes: [] as number[], accepted: [] as (RawEntry & { reads_agree: number; reads_total: number })[], dropped: [] as any[], union: 0, agreed2: 0 };
  pairs.forEach((pair, i) => {
    const B = B1?.pairs.includes(pair) ? B1 : B2?.pairs.includes(pair) ? B2 : null;
    const C = final ? rd(p.reads?.[`C${i}`]) : null;
    const readers = [ok(A) ? A : null, ok(B) ? B : null, C && ok(C) ? C : null];
    const sets = readers.map((r) => (r ? new Map(r.entries.filter((e) => e.pair === pair).map((e) => [entryKey(e), e])) : null));
    const keys = new Map<string, RawEntry>();
    for (const s of sets) if (s) for (const [k, e] of s) keys.set(k, e);
    const eq = !!sets[0] && !!sets[1] && sets[0].size === sets[1].size && [...sets[0].keys()].every((k) => sets[1]!.has(k));
    if (!eq) res.disputes.push(i);
    const total = sets.filter(Boolean).length;
    const spots = readers.filter(Boolean).map((r) => Number(r!.spot[pair])).filter((x) => x > 0);
    const spot = spots.length >= 2 && spots.every((x) => x === spots[0]) ? spots[0] : null;
    for (const [k, e] of keys) {
      const votes = sets.filter((s) => s?.has(k)).length;
      res.union++;
      if (sets[0]?.has(k) && sets[1]?.has(k)) res.agreed2++;
      const implausible = spot !== null && Math.abs(Number(e.strike) / spot - 1) > 0.12;
      if (votes >= 2 && !implausible) res.accepted.push({ ...e, reads_agree: votes, reads_total: total });
      else res.dropped.push({ ...e, votes, reads: total, post: p.url, reason: implausible ? `strike more than 12% from the printed spot ${spot}` : `only ${votes} of ${total} reads show this strike+notional` });
    }
  });
  return res;
}

const STEP: Record<string, (w: Work, rt: any, ctx: any, input: Input) => Promise<void>> = {
  async resolve_anchor(w, _rt, _ctx, input) {
    const anchor = anchorUtc(input.week);
    Object.assign(w, { week: input.week, anchor, log: [], dropped: [], posts: [], analyst: [], h10: null, accepted: [], analyst_levels: { DXY: [], EURUSD: [], GBPUSD: [] }, stats: {} });
    w.log.push(`anchor = Monday 02:00 America/New_York = ${iso(anchor)}`);
  },
  async discover(w, _rt, _ctx, input) {
    const rawDir = path.join(RAW, w.week);
    const all = [...loadSitemap(rawDir, isoWeek(w.anchor - 7 * 86400000)), ...loadSitemap(rawDir, isoWeek(w.anchor))];
    const exp = all.filter((e) => /\/orders\/fx-option-expiries-for-/i.test(e.loc)).map((e) => ({ e, d: expirySlugDate(e) })).filter((x) => x.d);
    const mon = exp.filter((x) => x.d === w.week && ymd(x.e.t) === w.week).pop();
    if (mon && mon.e.t <= w.anchor) w.posts.push({ role: "monday", url: mon.e.loc, lastmod: mon.e.lastmod, cut_date: w.week });
    else w.log.push(mon ? `Monday expiry post ${mon.e.loc} published ${mon.e.lastmod} is AFTER the anchor: excluded, not fetched` : "no Monday expiry post in the sitemap for this date");
    const prior = exp.filter((x) => x.d! < w.week && x.e.t <= w.anchor && x.d! >= ymd(w.anchor - 4 * 86400000) && ymd(x.e.t) === x.d).sort((a, b) => a.d!.localeCompare(b.d!)).pop();
    if (prior) w.posts.push({ role: "prior", url: prior.e.loc, lastmod: prior.e.lastmod, cut_date: prior.d! });
    else w.log.push("no expiry post in the 4 days before the anchor Monday");
    for (const u of input.force ?? []) {
      const e = all.find((x) => x.loc === u);
      w.posts.push({ role: "forced", url: u, lastmod: e?.lastmod ?? "unknown", cut_date: (e && expirySlugDate(e)) || w.week });
      w.log.push(`--force-include ${u}`);
    }
    const score = (loc: string) => (/eur-?usd|gbp-?usd|dxy|dollar-index|\beuro\b|pound|sterling|cable/i.test(loc) ? 3 : 0) + (/technical|levels|charts|support|resistance/i.test(loc) ? 2 : 0) + (/usd|dollar/i.test(loc) ? 1 : 0);
    w.analyst = all.filter((e) => e.t <= w.anchor && e.t >= w.anchor - 4.5 * 86400000 && /\/(technical-analysis|forex)\//i.test(e.loc) && !/option-expir|indicative-rates|monday-open/i.test(e.loc))
      .map((e) => ({ e, s: score(e.loc) })).filter((x) => x.s >= 3).sort((a, b) => b.s - a.s || b.e.t - a.e.t || a.e.loc.localeCompare(b.e.loc)).slice(0, 4)
      .map((x) => ({ url: x.e.loc, lastmod: x.e.lastmod }));
    w.log.push(`discover: ${w.posts.length} expiry post(s), ${w.analyst.length} analyst candidate(s) from sitemaps ${isoWeek(w.anchor - 7 * 86400000)}, ${isoWeek(w.anchor)}`);
  },
  async fetch_pages(w) {
    const rawDir = path.join(RAW, w.week);
    for (const p of w.posts) {
      p.file = fetchCached(p.url, path.join(rawDir, rawName(p.url) + ".html")).file;
      const a = parseArticle(p.url, p.file);
      p.published_at = a.published_at;
      p.image_url = a.images.find((u) => /FXO/i.test(u)) ?? a.images[0] ?? null;
      if (!p.image_url) w.log.push(`${p.url}: no table image in the article body`);
      if (p.lastmod !== "unknown" && Math.abs(Date.parse(p.lastmod) - a.t) > 300000) w.log.push(`${p.url}: sitemap lastmod ${p.lastmod} differs from article:published_time ${a.published_at}`);
    }
    const kept: Work["analyst"] = [];
    for (const c of w.analyst) {
      try { c.file = fetchCached(c.url, path.join(rawDir, rawName(c.url) + ".html")).file; c.published_at = parseArticle(c.url, c.file).published_at; kept.push(c); }
      catch (e) { w.log.push(`analyst candidate skipped: ${String((e as Error).message).slice(0, 160)}`); }
    }
    w.analyst = kept;
    const dates = path.join(rawDir, "fed_h10_releaseDates.json");
    if (!fs.existsSync(dates)) {
      const shared = path.join(CACHE, "shared", "fed_h10_releaseDates.json");
      if (!fs.existsSync(shared)) fetchCached("https://www.federalreserve.gov/releases/h10/releaseDates.json", shared);
      fs.mkdirSync(rawDir, { recursive: true }); fs.copyFileSync(shared, dates);
    }
    const rel = h10ReleaseFor(dates, w.anchor);
    if (rel) {
      const url = `https://www.federalreserve.gov/releases/h10/${rel.date}/`;
      try {
        const f = fetchCached(url, path.join(rawDir, `fed_h10_release_${rel.date}.html`)).file;
        const parsed = parseH10(f);
        w.h10_src = { url, published_at: iso(rel.published), kind: "h10_release" };
        w.h10 = parsed ? { release_date: `${rel.date.slice(0, 4)}-${rel.date.slice(4, 6)}-${rel.date.slice(6, 8)}`, published_at: iso(rel.published), source_url: url, ...parsed } : null;
        if (!parsed) w.log.push(`H.10 ${rel.date}: table not parsed`);
      } catch (e) { w.log.push(`H.10 skipped: ${String((e as Error).message).slice(0, 160)}`); }
    } else w.log.push("no H.10 release before the anchor");
  },
  async asof_gate(w) {
    asofGate(w.anchor, [
      ...w.posts.map((p) => ({ url: p.url, published_at: p.published_at!, what: "expiry post" })),
      ...w.analyst.map((a) => ({ url: a.url, published_at: a.published_at!, what: "analyst post" })),
      ...(w.h10_src ? [{ ...w.h10_src, what: "H.10 release" }] : []),
    ]);
    w.log.push("asof_gate: every fetched page was published at or before the anchor");
  },
  async prepare_views(w) {
    const rawDir = path.join(RAW, w.week);
    for (const p of w.posts) {
      if (!p.image_url) continue;
      const name = decodeURIComponent(p.image_url.split("/").pop()!).replace(/ /g, "_");
      p.image_file = fetchCached(p.image_url, path.join(rawDir, `${rawName(p.url)}__${name}`)).file;
      p.views_dir = path.join(CACHE, "views", sha(fs.readFileSync(p.image_file)).slice(0, 16));
      const r = Bun.spawnSync(["python3", path.join(SIDECAR, "src/views.py"), p.image_file, p.views_dir]);
      if (r.exitCode !== 0) throw new SidecarError("VIEWS_FAILED", `${p.image_file}: ${r.stderr.toString().slice(0, 300)}`);
      p.views = JSON.parse(r.stdout.toString());
      if (!p.views.grid_ok) w.log.push(`${p.url}: table grid not detected -> only one view, nothing can be cross-checked`);
    }
  },
  async read_expiries(w, rt, ctx) { // MODEL
    for (const p of w.posts) {
      if (!p.views) continue;
      const names = ["A", "B1", "B2"].filter((n) => p.views.views[n]);
      const rs = await modelSteps(rt, ctx, names.map((n) => ({ kind: `expiry_read_${n}`, prompt: READ_PROMPT(NOTE[n[0]]), imagePath: path.join(p.views_dir!, p.views.views[n].file) })));
      p.reads = Object.fromEntries(names.map((n, i) => [n, rs[i].key]));
    }
  },
  async reconcile(w) {
    for (const p of w.posts) if (p.reads) {
      const t = tally(p, false);
      p.tiebreak = p.views.grid_ok ? t.disputes.filter((i) => p.views.views[`C${i}`]) : [];
      w.log.push(`${p.url}: reads A/B agree on ${t.agreed2} of ${t.union} entries; third read for columns [${p.tiebreak.map((i) => t.pairs[i]).join(", ")}]`);
    }
  },
  async read_tiebreak(w, rt, ctx) { // MODEL
    for (const p of w.posts) if (p.reads && p.tiebreak?.length) {
      const rs = await modelSteps(rt, ctx, p.tiebreak.map((i) => ({ kind: `expiry_read_C${i}`, prompt: READ_PROMPT(NOTE.C), imagePath: path.join(p.views_dir!, p.views.views[`C${i}`].file) })));
      p.tiebreak.forEach((i, k) => { p.reads![`C${i}`] = rs[k].key; });
    }
  },
  async accept(w) {
    const s = { entries_seen: 0, agreed_first_two_reads: 0, accepted: 0, dropped: 0 };
    for (const p of w.posts) if (p.reads) {
      const t = tally(p, true);
      for (const n of t.notes) w.log.push(`${p.url}: ${n}`);
      s.entries_seen += t.union; s.agreed_first_two_reads += t.agreed2; s.accepted += t.accepted.length; s.dropped += t.dropped.length;
      for (const e of t.accepted) w.accepted.push({ ...e, source_url: p.url, published_at: p.published_at! });
      w.dropped.push(...t.dropped);
    }
    w.stats = s;
    w.log.push(`accept: ${s.accepted} strike/notional entries accepted (2+ reads identical), ${s.dropped} dropped`);
  },
  async read_analyst(w, rt, ctx) { // MODEL + mechanical verification of every quote against the article text
    const arts = w.analyst.map((a) => ({ ...a, text: parseArticle(a.url, a.file!).text })).filter((a) => a.text.length > 200);
    if (!arts.length) { w.log.push("read_analyst: no candidate article with text"); return; }
    const body = arts.map((a, i) => `[ARTICLE ${i + 1}] published ${a.published_at}\n${a.text.slice(0, 6000)}`).join("\n\n");
    const [r] = await modelSteps(rt, ctx, [{ kind: "analyst_levels", prompt: ANALYST_PROMPT(iso(w.anchor), body) }]);
    w.analyst_key = r.key;
    const norm = (s: string) => s.replace(/[‘’]/g, "'").replace(/[“”]/g, '"').replace(/\s+/g, " ").trim().toLowerCase();
    let j: any = {};
    try { j = JSON.parse(r.text.slice(r.text.indexOf("{"), r.text.lastIndexOf("}") + 1)); } catch { w.log.push("read_analyst: answer was not JSON, no levels taken"); }
    const range: Record<string, [number, number]> = { DXY: [70, 130], EURUSD: [0.8, 1.6], GBPUSD: [1.0, 2.0] };
    for (const l of Array.isArray(j.levels) ? j.levels : []) {
      const a = arts[Number(l.article) - 1], ins = String(l.instrument), price = Number(l.price), q = String(l.quote ?? "");
      const why = !a ? "unknown article" : !range[ins] ? "instrument out of scope" : !(price >= range[ins][0] && price <= range[ins][1]) ? "price outside the instrument's range"
        : !norm(a.text).includes(norm(q)) || q.length < 8 ? "quote is not verbatim in the article" : !q.includes(String(l.price)) ? "price not present in the quote" : "";
      if (why) { w.dropped.push({ kind: "analyst_level", instrument: ins, price: l.price, quote: q.slice(0, 200), reason: why }); continue; }
      if (!w.analyst_levels[ins].some((x) => x.price === price && x.source_url === a.url))
        w.analyst_levels[ins].push({ price, role: ["support", "resistance"].includes(l.role) ? l.role : "level", source_url: a.url, published_at: a.published_at, quote: q });
    }
    for (const k of Object.keys(w.analyst_levels)) w.analyst_levels[k].sort((x, y) => x.price - y.price || x.source_url.localeCompare(y.source_url));
  },
  async convert(w) {
    const sp = { DXY: spotBefore("TVC_DXY", w.anchor), EURUSD: spotBefore("FX_EURUSD", w.anchor), GBPUSD: spotBefore("FX_GBPUSD", w.anchor) };
    const k = sp.DXY.close * sp.EURUSD.close ** 0.576;
    // union across posts: same pair + cut date + strike -> keep the larger notional
    const best = new Map<string, Accepted>();
    for (const e of w.accepted) { const key = `${e.pair}|${e.date}|${e.strike}`; const c = best.get(key); if (!c || e.notional_m > c.notional_m) best.set(key, e); }
    const pairs = [...new Set([...best.values()].map((e) => e.pair))].sort((a, b) => { const o = ["EURUSD", "GBPUSD", "USDJPY"]; return (o.indexOf(a) + 9) % 9 - (o.indexOf(b) + 9) % 9 || a.localeCompare(b); });
    const expiries: Record<string, any[]> = {};
    for (const pair of ["EURUSD", "GBPUSD", "USDJPY", ...pairs.filter((p) => !["EURUSD", "GBPUSD", "USDJPY"].includes(p))]) {
      expiries[pair] = clusterAndTier(pair, [...best.values()].filter((e) => e.pair === pair), w.week).map((l) => ({ strike: l.strike, notional_m: l.notional_m, ccy: l.ccy, cut_date: l.cut_date,
        state: l.state, tier: l.tier, code: l.code, reads_agree: l.reads_agree, reads_total: l.reads_total, ...(l.members.length > 1 ? { cluster_of: l.members } : {}), source_url: l.source_url, published_at: l.published_at }));
    }
    const dxy_levels = expiries.EURUSD.filter((l) => l.tier <= 2).map((l) => ({ price: Number((k * l.strike ** -0.576).toFixed(4)), from_pair: "EURUSD", strike: l.strike, notional_m: l.notional_m, tier: l.tier, state: l.state, code: l.code, cut_date: l.cut_date }));
    const bar = (s: keyof typeof sp, sym: string) => ({ url: `pinebox-bar-store:${sym}/60/${path.basename(sp[s].file)}#time=${sp[s].bar_time}`, published_at: iso(sp[s].bar_time + 3600000), kind: "spot_bar" });
    w.out = {
      week: w.week, anchor_utc: iso(w.anchor),
      sources: [...w.posts.flatMap((p) => [{ url: p.url, published_at: p.published_at, kind: `expiry_post_${p.role}` }, ...(p.image_url ? [{ url: p.image_url, published_at: p.published_at, kind: "expiry_image" }] : [])]),
        ...w.analyst.map((a) => ({ url: a.url, published_at: a.published_at, kind: "analyst_post" })), ...(w.h10_src ? [w.h10_src] : []), bar("DXY", "TVC_DXY"), bar("EURUSD", "FX_EURUSD"), bar("GBPUSD", "FX_GBPUSD")],
      expiries,
      spots: { from: "pinebox bar store, last 1H close before the anchor", bar_close_utc: iso(sp.DXY.bar_time + 3600000), DXY: sp.DXY.close, EURUSD: sp.EURUSD.close, GBPUSD: sp.GBPUSD.close },
      k_anchor: Number(k.toFixed(6)), h10: w.h10, dxy_levels, analyst_levels: w.analyst_levels, read_stats: w.stats,
      model: { id: MODEL.modelId, effort: EFFORT, gateway: `${GATEWAY_BASE}/responses`, runtime: "aether_agent_backend_v2 / pi-durable task sidecar.week" },
      dropped: w.dropped, log: w.log,
    };
  },
  async emit(w) {
    const o = w.out;
    asofGate(w.anchor, [...o.sources.map((s: any) => ({ ...s, what: s.kind })),
      ...Object.values(o.expiries).flat().map((e: any) => ({ url: e.source_url, published_at: e.published_at, what: "expiry entry" })),
      ...Object.values(o.analyst_levels).flat().map((e: any) => ({ url: e.source_url, published_at: e.published_at, what: "analyst level" }))]);
    o.log.push(`emit: as-of gate passed for ${o.sources.length} sources and every datum`);
    writeJson(path.join(OUT, `${w.week}.json`), o);
  },
};

/** The durable task: one phase per step; the checkpoint is the step name, step outputs live in cache/work/<week>.json. */
function weekTask(D: any) {
  const phases: Record<string, any> = {};
  STEPS.forEach((name, i) => {
    phases[name] = async (task: any, rt: any, ctx: any) => {
      const input: Input = task.input;
      const w: Work = name === "resolve_anchor" ? ({} as Work) : readJson(workFile(input.week));
      try {
        if (process.env.SIDECAR_VERBOSE) console.error(`[step] ${name}${MODEL_STEPS.has(name) ? " (MODEL)" : ""}`);
        await STEP[name](w, rt, ctx, input);
      } catch (e) {
        const se = e instanceof SidecarError ? e : new SidecarError("STEP_FAILED", String((e as Error)?.stack ?? e).slice(0, 600));
        await rt.commit(() => ({ status: "terminal", outcome: { status: "failed", error: { message: se.message, detail: { step: name, name: se.name, code: se.code } } } }), ctx);
        return;
      }
      writeJson(workFile(input.week), w);
      const next = STEPS[i + 1];
      await rt.commit(() => (next ? { status: "running", checkpoint: { phase: next } } : { status: "terminal", outcome: { status: "completed", result: { out: `out/${input.week}.json` } } }), ctx);
    };
  });
  return D.defineTask({ name: "sidecar.week", version: 1, initial: (_: Input) => ({ phase: STEPS[0] }), phases,
    abort: async (_t: any, rt: any, ctx: any) => { await rt.commit(() => ({ status: "terminal", outcome: { status: "aborted" } }), ctx); } });
}

async function main() {
  const argv = process.argv.slice(2);
  const arg = (n: string) => { const i = argv.indexOf(n); return i >= 0 ? argv[i + 1] : undefined; };
  const week = arg("--week");
  if (!week) { console.error("usage: sidecar/run --week YYYY-MM-DD(Monday) [--offline] [--force-include <post url>] [--fresh]"); process.exit(64); }
  anchorUtc(week); // validates before anything is opened
  net.offline = argv.includes("--offline");
  const force = argv.flatMap((a, i) => (a === "--force-include" ? [argv[i + 1]] : []));
  if (!fs.existsSync(`${AETHER_HOME}/node_modules/@earendil-works/pi-durable`)) throw new SidecarError("AETHER_MISSING", `pi-durable not found under ${AETHER_HOME} (set AETHER_HOME)`, 5);
  const storage = path.join(CACHE, "aether", `${week}.sqlite`);
  if (argv.includes("--fresh")) for (const s of ["", "-wal", "-shm"]) try { fs.unlinkSync(storage + s); } catch {}
  const h = await openSidecarHarness(storage, (D) => [weekTask(D)]);
  let code = 0;
  try {
    // a task left unfinished by a killed process resumes from its last checkpoint; otherwise a new task is created
    const live = Object.values((await h.harness.taskGraph(h.ctx)).value.tasks as Record<string, any>).find((t: any) => t.kind === "sidecar.week" && !force.length);
    let id = live?.id;
    if (id === undefined) await h.root.commit(async (tx: any) => { id = await tx.createTask(h.defs[0], { week, force }, { ownership: { kind: "conversation" } }); }, h.ctx);
    else console.error(`[sidecar] resuming unfinished task ${id}`);
    h.harness.resume();
    const done = await h.harness.waitForTask(id, h.ctx);
    const oc = done.state.outcome;
    if (oc.status === "completed") console.log(`${week}: wrote sidecar/out/${week}.json  (model calls ${stats.calls}, cached reads ${stats.cached}, http requests ${net.requests})`);
    else { console.error(`${week}: ${oc.status.toUpperCase()} ${oc.error?.message ?? oc.reason ?? ""} [step ${oc.error?.detail?.step ?? "?"}]`); code = oc.error?.detail?.code ?? 2; }
  } finally { await h.harness.close(h.ctx).catch(() => {}); }
  process.exit(code);
}
if (import.meta.main) main().catch((e) => { console.error(e instanceof SidecarError ? e.message : e); process.exit(e instanceof SidecarError ? e.code : 1); });
