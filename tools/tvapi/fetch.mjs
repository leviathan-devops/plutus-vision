// fetch.mjs - pull the Engine 2 data-module inputs through TradingView-API into data/tvapi/ (one JSON per symbol + timeframe).
// Bars are stored as the Pinebox bar store stores them: {time (epoch ms, bar OPEN time), open, high, low, close, volume}. The engines cut everything at the anchor.
import fs from 'node:fs';
import path from 'node:path';
import { createProxy } from '@mathieuc/tradingview';
import { getCandles } from '@mathieuc/tradingview/data';
const OUT = path.resolve(import.meta.dirname, '../../data/tvapi');
const proxy = process.env.HTTPS_PROXY ? createProxy(process.env.HTTPS_PROXY, { tls: { ca: fs.readFileSync('/root/.ccr/ca-bundle.crt') } }) : {};
const FROM = new Date('2025-02-01T00:00:00Z');
const FUT = ['CME:6E1!', 'CME:6B1!', 'ICEUS:DX1!'];
const YLD = ['TVC:US02Y', 'TVC:DE02Y', 'TVC:GB02Y'];
const COT = ['099741', '096742', '098662'].flatMap((c) => ['F_NCP_L', 'F_NCP_S', 'F_OI'].map((k) => `COT:${c}_${k}`));
const JOBS = [...FUT.flatMap((s) => ['15', '30', '60', '240', 'D'].map((tf) => [s, tf])), ...YLD.flatMap((s) => ['60', 'D'].map((tf) => [s, tf])), ...COT.map((s) => [s, 'W'])];
const only = process.argv.slice(2);
const index = {};
for (const [symbol, tf] of JOBS) {
  if (only.length && !only.some((o) => symbol.includes(o))) continue;
  const file = path.join(OUT, `${symbol.replace(/[:!]/g, '_')}__${tf}.json`);
  try {
    const c = await getCandles({ symbol, timeframe: tf, from: FROM, clientOptions: proxy });
    const bars = c.map((x) => ({ time: x.time * 1000, open: x.open, high: x.high, low: x.low, close: x.close, volume: x.volume ?? 0 }));
    const meta = { symbol, tf, count: bars.length, first: new Date(bars[0].time).toISOString(), last: new Date(bars.at(-1).time).toISOString(), fetchedAt: new Date().toISOString(), source: 'TradingView-API (@mathieuc/tradingview), free access' };
    fs.writeFileSync(file, JSON.stringify({ ...meta, bars }));
    index[`${symbol}|${tf}`] = meta;
    console.log('OK  ', symbol.padEnd(22), tf.padEnd(4), String(bars.length).padStart(6), meta.first.slice(0, 16), '->', meta.last.slice(0, 16));
  } catch (e) {
    console.log('FAIL', symbol, tf, e.code || '', String(e.message).slice(0, 200));
  }
}
const ixf = path.join(OUT, 'index.json');
const old = fs.existsSync(ixf) ? JSON.parse(fs.readFileSync(ixf, 'utf8')) : {};
fs.writeFileSync(ixf, JSON.stringify({ ...old, ...index }, null, 1));
process.exit(0);
