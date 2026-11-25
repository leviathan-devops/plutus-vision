// build-inputs.ts — MECHANICAL: every out/<week>.json -> out/pine_inputs.json + out/pine_inputs.<SYMBOL>.txt
// Dataset = rows `YYYYMMDD|price:code,price:code;` (YYYYMMDD = the anchor Monday, prices ascending).
// Codes: 1 live >=1.5bn, 2 live 850m-1.499bn, 3 ghost >=1.5bn, 4 ghost 850m-1.499bn; analyst rows use 9.
import * as fs from "node:fs";
import * as path from "node:path";
import { OUT, SidecarError, asofGate, readJson, writeJson } from "./lib.ts";

const SYMS = ["DXY", "EURUSD", "GBPUSD"] as const;
const dec = (s: string) => (s === "DXY" ? 2 : 4);
function row(week: string, sym: string, items: { price: number; code: number }[]): string {
  const best = new Map<string, number>(); // same printed price twice -> keep the strongest (lowest) code
  for (const it of items) { const p = it.price.toFixed(dec(sym)); best.set(p, Math.min(best.get(p) ?? 99, it.code)); }
  if (!best.size) return "";
  return `${week.replace(/-/g, "")}|${[...best.entries()].sort((a, b) => Number(a[0]) - Number(b[0])).map(([p, c]) => `${p}:${c}`).join(",")};`;
}

const weeks = fs.readdirSync(OUT).filter((f) => /^\d{4}-\d{2}-\d{2}\.json$/.test(f)).sort();
if (!weeks.length) { console.error(new SidecarError("NO_WEEKS", "no out/<week>.json found").message); process.exit(2); }
const ds: Record<string, string> = { DXY: "", EURUSD: "", GBPUSD: "" };
const an: Record<string, string> = { DXY: "", EURUSD: "", GBPUSD: "" };
const stats = { weeks: 0, entries_seen: 0, agreed_first_two_reads: 0, accepted: 0, dropped: 0 };
const perWeek: Record<string, unknown> = {};
try {
  for (const f of weeks) {
    const o = readJson(path.join(OUT, f));
    const anchor = Date.parse(o.anchor_utc);
    // the same refusal as the week builder: a week file carrying a post-anchor datum is never turned into an input
    asofGate(anchor, [...o.sources.map((s: any) => ({ ...s, what: `${o.week} ${s.kind}` })),
      ...Object.values(o.expiries).flat().map((e: any) => ({ url: e.source_url, published_at: e.published_at, what: `${o.week} expiry entry` })),
      ...Object.values(o.analyst_levels).flat().map((e: any) => ({ url: e.source_url, published_at: e.published_at, what: `${o.week} analyst level` }))]);
    ds.DXY += row(o.week, "DXY", o.dxy_levels.filter((l: any) => l.code).map((l: any) => ({ price: l.price, code: l.code })));
    for (const p of ["EURUSD", "GBPUSD"]) ds[p] += row(o.week, p, (o.expiries[p] ?? []).filter((l: any) => l.code).map((l: any) => ({ price: l.strike, code: l.code })));
    for (const s of SYMS) an[s] += row(o.week, s, (o.analyst_levels[s] ?? []).map((l: any) => ({ price: l.price, code: 9 })));
    stats.weeks++;
    for (const k of ["entries_seen", "agreed_first_two_reads", "accepted", "dropped"] as const) stats[k] += o.read_stats?.[k] ?? 0;
    perWeek[o.week] = { expiry_posts: o.sources.filter((s: any) => s.kind.startsWith("expiry_post")).map((s: any) => `${s.kind.replace("expiry_post_", "")}@${s.published_at}`), ...o.read_stats };
  }
} catch (e) { console.error(e instanceof SidecarError ? e.message : e); process.exit(e instanceof SidecarError ? e.code : 1); }

writeJson(path.join(OUT, "pine_inputs.json"), { DXY: ds.DXY, EURUSD: ds.EURUSD, GBPUSD: ds.GBPUSD, analyst: an,
  meta: { weeks: weeks.map((f) => f.slice(0, 10)), codes: { "1": "live >= 1.5bn", "2": "live 850m-1.499bn", "3": "ghost >= 1.5bn", "4": "ghost 850m-1.499bn", "9": "analyst level (investinglive; source not in the canon tier table)" },
    lengths: Object.fromEntries(SYMS.map((s) => [s, ds[s].length])) } });
for (const s of SYMS) { fs.writeFileSync(path.join(OUT, `pine_inputs.${s}.txt`), ds[s]); fs.writeFileSync(path.join(OUT, `pine_inputs.analyst.${s}.txt`), an[s]); }
writeJson(path.join(OUT, "read_stats.json"), { ...stats, first_two_reads_agreement: stats.entries_seen ? Number((stats.agreed_first_two_reads / stats.entries_seen).toFixed(4)) : null, per_week: perWeek });
console.log(`pine_inputs: ${stats.weeks} week(s); lengths DXY ${ds.DXY.length}, EURUSD ${ds.EURUSD.length}, GBPUSD ${ds.GBPUSD.length}; reads agree ${stats.agreed_first_two_reads}/${stats.entries_seen}, dropped ${stats.dropped}`);
