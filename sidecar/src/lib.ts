// lib.ts — every MECHANICAL piece of the sidecar (no model calls in this file).
import * as fs from "node:fs";
import * as path from "node:path";
import { createHash } from "node:crypto";

export const SIDECAR = path.resolve(import.meta.dir, "..");
export const RAW = path.join(SIDECAR, "raw");
export const CACHE = path.join(SIDECAR, "cache");
export const OUT = path.join(SIDECAR, "out");
export const UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36";
export const BARS = path.join(process.env.HOME ?? "/root", ".local/share/pinebox/data/tv-bars");

/** Named, exit-coded refusal. The CLI maps `code` to the process exit status. */
export class SidecarError extends Error {
  constructor(public name: string, message: string, public code = 2) { super(`${name}: ${message}`); }
}
export const sha = (s: string | Buffer) => createHash("sha256").update(s).digest("hex");
export const iso = (ms: number) => new Date(ms).toISOString().replace(".000Z", "Z");
export function writeJson(file: string, v: unknown) {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, JSON.stringify(v, null, 1) + "\n");
}
export const readJson = (file: string) => JSON.parse(fs.readFileSync(file, "utf8"));

// ── STEP resolve_anchor ───────────────────────────────────────────────────────
/** Monday 02:00 America/New_York of the given Monday (YYYY-MM-DD), as UTC ms. DST-aware. */
export function anchorUtc(week: string): number {
  const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(week);
  if (!m) throw new SidecarError("BAD_WEEK", `--week must be YYYY-MM-DD, got ${week}`);
  const [y, mo, d] = [Number(m[1]), Number(m[2]), Number(m[3])];
  if (new Date(Date.UTC(y, mo - 1, d)).getUTCDay() !== 1) throw new SidecarError("BAD_WEEK", `${week} is not a Monday`);
  const fmt = new Intl.DateTimeFormat("en-US", { timeZone: "America/New_York", hour12: false, year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit" });
  for (const off of [4, 5]) {
    const t = Date.UTC(y, mo - 1, d, 2 + off, 0, 0);
    const p = Object.fromEntries(fmt.formatToParts(new Date(t)).map((x) => [x.type, x.value]));
    if (Number(p.hour) % 24 === 2 && Number(p.day) === d && Number(p.minute) === 0) return t;
  }
  throw new SidecarError("ANCHOR_UNRESOLVED", `no UTC instant maps to 02:00 New York on ${week}`);
}
/** Instant of HH:MM America/New_York on a calendar date, as UTC ms. */
export function nyInstant(y: number, mo: number, d: number, hh: number, mm: number): number {
  const fmt = new Intl.DateTimeFormat("en-US", { timeZone: "America/New_York", hour12: false, hour: "2-digit", day: "2-digit" });
  for (const off of [4, 5]) {
    const t = Date.UTC(y, mo - 1, d, hh + off, mm, 0);
    const p = Object.fromEntries(fmt.formatToParts(new Date(t)).map((x) => [x.type, x.value]));
    if (Number(p.hour) % 24 === hh && Number(p.day) === d) return t;
  }
  throw new SidecarError("ANCHOR_UNRESOLVED", `no NY instant for ${y}-${mo}-${d} ${hh}:${mm}`);
}
export function isoWeek(ms: number): string {
  const d = new Date(ms); const t = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate()));
  const dow = t.getUTCDay() || 7; t.setUTCDate(t.getUTCDate() + 4 - dow);
  const y0 = Date.UTC(t.getUTCFullYear(), 0, 1);
  const wk = Math.ceil(((t.getTime() - y0) / 86400000 + 1) / 7);
  return `${t.getUTCFullYear()}-W${String(wk).padStart(2, "0")}`;
}
export const ymd = (ms: number) => new Date(ms).toISOString().slice(0, 10);

// ── fetch with raw cache (curl; the proxy env is inherited) ───────────────────
export const net = { offline: false, requests: 0 };
export function fetchCached(url: string, file: string, extraMeta: Record<string, unknown> = {}): { file: string; cached: boolean } {
  const meta = file.replace(/\.[a-z0-9]+$/i, "") + ".meta.json";
  if (fs.existsSync(file) && fs.statSync(file).size > 0) return { file, cached: true };
  if (net.offline) throw new SidecarError("OFFLINE_MISS", `${url} is not in the raw cache (${file})`);
  fs.mkdirSync(path.dirname(file), { recursive: true });
  const tmp = file + ".part";
  const r = Bun.spawnSync(["curl", "-sS", "-L", "--max-time", "90", "-A", UA, "-o", tmp, "-w", "%{http_code}", url]);
  net.requests++;
  const status = r.stdout.toString().trim();
  Bun.sleepSync(900); // politeness: under ~1 request/second
  if (r.exitCode !== 0 || status !== "200") {
    try { fs.unlinkSync(tmp); } catch {}
    throw new SidecarError("FETCH_FAILED", `${url} -> http ${status || "?"} curl exit ${r.exitCode} ${r.stderr.toString().slice(0, 200)}`);
  }
  fs.renameSync(tmp, file);
  if (!fs.existsSync(meta)) writeJson(meta, { url, fetched_at: new Date().toISOString(), http_status: status, bytes: fs.statSync(file).size, ...extraMeta });
  return { file, cached: false };
}

// ── STEP discover (weekly sitemaps) ───────────────────────────────────────────
export type SitemapEntry = { loc: string; lastmod: string; t: number };
export function loadSitemap(rawDir: string, wk: string): SitemapEntry[] {
  const f = fetchCached(`https://investinglive.com/sitemaps/news/articles/${wk}.xml`, path.join(rawDir, `investinglive_sitemap_${wk}.xml`)).file;
  const xml = fs.readFileSync(f, "utf8");
  const out: SitemapEntry[] = [];
  for (const u of xml.split("<url>").slice(1)) { // two layouts exist: compact (pre July 2026) and multi-line with xhtml:link alternates
    const loc = /<loc>([^<]+)<\/loc>/.exec(u)?.[1].trim(), lastmod = /<lastmod>([^<]+)<\/lastmod>/.exec(u)?.[1].trim();
    if (loc && lastmod && Number.isFinite(Date.parse(lastmod))) out.push({ loc, lastmod, t: Date.parse(lastmod) });
  }
  return out.sort((a, b) => a.t - b.t || a.loc.localeCompare(b.loc));
}
const MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"];
/** Cut date (YYYY-MM-DD) named by an expiry post slug; the year comes from the publish instant. */
export function expirySlugDate(e: SitemapEntry): string | null {
  const m = /fx-option-expiries-for-(\d{1,2})-([a-z]+)/i.exec(e.loc);
  if (!m) return null;
  const mo = MONTHS.indexOf(m[2].toLowerCase());
  if (mo < 0) return null;
  let y = new Date(e.t).getUTCFullYear();
  if (mo === 0 && new Date(e.t).getUTCMonth() === 11) y++;
  return `${y}-${String(mo + 1).padStart(2, "0")}-${String(Number(m[1])).padStart(2, "0")}`;
}
export function rawName(url: string): string {
  const u = new URL(url);
  const parts = u.pathname.split("/").filter(Boolean);
  if (u.hostname.endsWith("investinglive.com")) return `investinglive_${parts.slice(0, -1).join("_").toLowerCase()}_${parts[parts.length - 1]}`;
  return `${u.hostname}_${parts.join("_")}`;
}

// ── article parsing (head meta + div[data-ref="article-body"] ONLY) ───────────
export type Article = { url: string; file: string; published_at: string; t: number; title: string; body_html: string; text: string; images: string[] };
export function parseArticle(url: string, file: string): Article {
  const h = fs.readFileSync(file, "utf8");
  const pm = /<meta property="article:published_time" content="([^"]+)"/.exec(h);
  if (!pm) throw new SidecarError("NO_PUBLISH_TIME", `${url}: no article:published_time meta`);
  const t = Date.parse(pm[1]);
  if (!Number.isFinite(t)) throw new SidecarError("NO_PUBLISH_TIME", `${url}: unparsable publish time ${pm[1]}`);
  const title = (/<meta property="og:title" content="([^"]*)"/.exec(h)?.[1] ?? "").replace(/&amp;/g, "&");
  const mk = h.indexOf('data-ref="article-body"');
  let body = "";
  if (mk >= 0) {
    const start = h.lastIndexOf("<div", mk);
    const re = /<(\/?)div\b/g; re.lastIndex = start;
    let depth = 0, end = h.length;
    for (let m = re.exec(h); m; m = re.exec(h)) { depth += m[1] ? -1 : 1; if (depth === 0) { end = m.index; break; } }
    body = h.slice(start, end);
  }
  const images = [...body.matchAll(/<img[^>]+src="(https:\/\/investinglive\.com\/cms\/media\/[^"?]+)/g)].map((m) => m[1]);
  const text = body.replace(/<(script|style)[\s\S]*?<\/\1>/g, " ").replace(/<\/(p|li|h\d|div|figure|tr)>/g, "\n").replace(/<[^>]+>/g, " ")
    .replace(/&amp;/g, "&").replace(/&nbsp;/g, " ").replace(/&#x27;|&#39;|&rsquo;|&lsquo;/g, "'").replace(/&quot;|&ldquo;|&rdquo;/g, '"').replace(/&gt;/g, ">").replace(/&lt;/g, "<")
    .replace(/[ \t]+/g, " ").replace(/\s*\n\s*/g, "\n").trim();
  return { url, file, published_at: iso(Math.floor(t / 1000) * 1000), t, title, body_html: body, text, images };
}

// ── STEP h10 (audit only) ─────────────────────────────────────────────────────
export function h10ReleaseFor(datesFile: string, anchor: number): { date: string; published: number } | null {
  const all: string[] = [];
  for (const y of readJson(datesFile)) for (const mo of y.Months ?? []) for (const d of mo.Dates ?? []) all.push(String(d));
  let best: { date: string; published: number } | null = null;
  for (const d of all.sort()) {
    const pub = nyInstant(Number(d.slice(0, 4)), Number(d.slice(4, 6)), Number(d.slice(6, 8)), 16, 15);
    if (pub < anchor) best = { date: d, published: pub };
  }
  return best;
}
const H10_ROWS: Record<string, RegExp> = { EURUSD: /EMU MEMBERS/, USDJPY: /JAPAN/, GBPUSD: /UNITED KINGDOM/, USDCAD: /CANADA/, USDSEK: /SWEDEN/, USDCHF: /SWITZERLAND/ };
export function parseH10(file: string) {
  const h = fs.readFileSync(file, "utf8");
  const days = [...h.matchAll(/<th[^>]*id="a[3-7]"[^>]*>([^<]+)</g)].map((m) => m[1].replace(/\s+/g, " ").trim());
  const cols: Record<string, (number | null)[]> = {};
  for (const tr of h.split(/<tr>/)) {
    const th = /<th[^>]*>([^<]+)<\/th>/.exec(tr)?.[1] ?? "";
    for (const [k, re] of Object.entries(H10_ROWS)) if (re.test(th) && !cols[k]) {
      const tds = [...tr.matchAll(/<td[^>]*>([^<]*)<\/td>/g)].map((m) => m[1].trim()).slice(1);
      cols[k] = tds.map((v) => (/^\d+(\.\d+)?$/.test(v) ? Number(v) : null));
    }
  }
  const keys = Object.keys(H10_ROWS);
  if (keys.some((k) => !cols[k])) return null;
  for (let i = 4; i >= 0; i--) if (keys.every((k) => cols[k][i] != null)) {
    const r = Object.fromEntries(keys.map((k) => [k, cols[k][i] as number]));
    const k_h10 = 50.14348112 * r.USDJPY ** 0.136 * r.GBPUSD ** -0.119 * r.USDCAD ** 0.091 * r.USDSEK ** 0.042 * r.USDCHF ** 0.036;
    return { rate_day: days[i] ?? `col${i + 1}`, rates: r, k_h10: Number(k_h10.toFixed(6)), dxy_h10: Number((k_h10 * r.EURUSD ** -0.576).toFixed(4)) };
  }
  return null;
}

// ── STEP spots (Pinebox bar store, last 1H close before the anchor) ───────────
export function spotBefore(sym: string, anchor: number): { close: number; bar_time: number; file: string } {
  for (let back = 0; back < 2; back++) {
    const d = new Date(anchor); d.setUTCDate(1); d.setUTCMonth(d.getUTCMonth() - back);
    const f = path.join(BARS, sym, "60", `${d.toISOString().slice(0, 7)}.json`);
    if (!fs.existsSync(f)) continue;
    const bars: { time: number; close: number }[] = readJson(f);
    let best: { time: number; close: number } | null = null;
    for (const b of bars) if (b.time + 3600000 <= anchor && (!best || b.time > best.time)) best = b;
    if (best) return { close: best.close, bar_time: best.time, file: f };
  }
  throw new SidecarError("NO_SPOT", `no 1H bar of ${sym} closes at or before ${iso(anchor)} in ${BARS}`);
}

// ── expiry read parsing / reconcile / cluster / tier ──────────────────────────
export const pipOf = (pair: string) => (pair.endsWith("JPY") ? 0.01 : 0.0001);
export const decOf = (pair: string) => (pair.endsWith("JPY") ? 2 : 4);
const CCY: Record<string, string> = { "€": "EUR", "£": "GBP", "$": "USD", "A$": "AUD", "NZ$": "NZD", "C$": "CAD", "¥": "JPY" };
export type RawEntry = { pair: string; date: string; strike: string; notional_m: number; ccy: string };
export type ParsedRead = { ok: boolean; error?: string; pairs: string[]; spot: Record<string, string>; rowDates: string[]; entries: RawEntry[] };
export function parseNotional(s: string, pair: string): { m: number; ccy: string } | null {
  const x = /^(NZ\$|A\$|C\$|€|£|\$|¥)?\s*(\d+(?:[.,]\d+)?)\s*(bn|b|m|mn)$/i.exec(s.replace(/[()\s]/g, ""));
  if (!x) return null;
  const v = Number(x[2].replace(",", "."));
  const m = /^b/i.test(x[3]) ? Math.round(v * 1000) : Math.round(v);
  return { m, ccy: x[1] ? CCY[x[1].toUpperCase()] ?? CCY[x[1]] : pair.slice(0, 3) };
}
/** Parse one model read (JSON text) into normalised entries. Never repairs a value: unparsable -> skipped. */
export function parseRead(text: string, year: number): ParsedRead {
  const bad = (error: string): ParsedRead => ({ ok: false, error, pairs: [], spot: {}, rowDates: [], entries: [] });
  const a = text.indexOf("{"), b = text.lastIndexOf("}");
  if (a < 0 || b <= a) return bad("no JSON object in answer");
  let j: any;
  try { j = JSON.parse(text.slice(a, b + 1)); } catch (e) { return bad(`JSON parse: ${String(e).slice(0, 80)}`); }
  const norm = (p: string) => String(p).toUpperCase().replace(/[^A-Z]/g, "");
  const pairs = (Array.isArray(j.pairs) ? j.pairs : []).map(norm).filter((p: string) => p.length === 6);
  const spot: Record<string, string> = {};
  for (const [k, v] of Object.entries(j.spot ?? {})) if (/^\d+(\.\d+)?$/.test(String(v))) spot[norm(k)] = String(v);
  const rowDates: string[] = [], entries: RawEntry[] = [];
  for (const row of Array.isArray(j.rows) ? j.rows : []) {
    const dm = /(\d{1,2})\s*\/\s*(\d{1,2})/.exec(String(row.date ?? row.label ?? ""));
    if (!dm) continue;
    const date = `${year}-${dm[2].padStart(2, "0")}-${dm[1].padStart(2, "0")}`;
    rowDates.push(date);
    for (const [pk, cell] of Object.entries(row.cells ?? {})) {
      const pair = norm(pk);
      if (pair.length !== 6 || !Array.isArray(cell)) continue;
      for (const it of cell) {
        const st = String(it?.strike ?? "").trim();
        const no = parseNotional(String(it?.notional ?? ""), pair);
        if (!/^\d+\.\d+$/.test(st) || !no) continue; // includes "[UNCLEAR]" -> never accepted
        let canon = Number(st).toFixed(5); // canonical text: at least the pair's pip decimals, no extra trailing zeros
        while (canon.split(".")[1].length > decOf(pair) && canon.endsWith("0")) canon = canon.slice(0, -1);
        entries.push({ pair, date, strike: canon, notional_m: no.m, ccy: no.ccy });
      }
    }
  }
  return { ok: true, pairs, spot, rowDates, entries };
}
export const entryKey = (e: RawEntry) => `${e.pair}|${e.date}|${e.strike}|${e.notional_m}|${e.ccy}`;

export type Accepted = RawEntry & { reads_agree: number; reads_total: number; source_url: string; published_at: string };
export type Level = { strike: number; notional_m: number; ccy: string; cut_date: string; state: "live" | "ghost"; tier: 1 | 2 | 3; code: number | null;
  reads_agree: number; reads_total: number; members: { strike: number; notional_m: number }[]; source_url: string; published_at: string };
/** Canon cluster rule (v4.5.2:938): strikes of one pair and one cut date within 10 pips aggregate. Greedy from the
 *  lowest strike; a cluster's span never exceeds 10 pips. Tier is taken on the aggregated face notional. */
export function clusterAndTier(pair: string, acc: Accepted[], anchorDate: string): Level[] {
  const out: Level[] = [];
  const byDate = new Map<string, Accepted[]>();
  for (const e of acc) byDate.set(e.date, [...(byDate.get(e.date) ?? []), e]);
  for (const date of [...byDate.keys()].sort()) {
    const list = byDate.get(date)!.sort((x, y) => Number(x.strike) - Number(y.strike));
    let i = 0;
    while (i < list.length) {
      let j = i;
      while (j + 1 < list.length && Number(list[j + 1].strike) - Number(list[i].strike) <= 10 * pipOf(pair) + 1e-9) j++;
      const mem = list.slice(i, j + 1);
      const tot = mem.reduce((s, e) => s + e.notional_m, 0);
      const wk = mem.reduce((s, e) => s + Number(e.strike) * e.notional_m, 0) / tot;
      const state = date >= anchorDate ? "live" : "ghost";
      const tier = tot >= 1500 ? 1 : tot >= 850 ? 2 : 3;
      const lead = mem.reduce((p, c) => (c.notional_m > p.notional_m ? c : p));
      out.push({ strike: Number(wk.toFixed(decOf(pair) + 1)), notional_m: tot, ccy: mem[0].ccy, cut_date: date, state, tier,
        code: tier === 3 ? null : state === "live" ? tier : tier + 2,
        reads_agree: Math.min(...mem.map((e) => e.reads_agree)), reads_total: Math.max(...mem.map((e) => e.reads_total)),
        members: mem.map((e) => ({ strike: Number(e.strike), notional_m: e.notional_m })), source_url: lead.source_url, published_at: lead.published_at });
      i = j + 1;
    }
  }
  return out;
}

// ── STEP asof_gate ────────────────────────────────────────────────────────────
/** REFUSES (throws ASOF_VIOLATION, exit 3) when any used datum was published after the anchor. */
export function asofGate(anchor: number, data: { url: string; published_at: string; what?: string }[]) {
  const late = data.filter((d) => !(Date.parse(d.published_at) <= anchor));
  if (late.length) throw new SidecarError("ASOF_VIOLATION", `${late.length} datum(s) published after the anchor ${iso(anchor)}: ` +
    late.slice(0, 5).map((d) => `${d.what ?? "source"} ${d.url} @ ${d.published_at}`).join("; "), 3);
}
