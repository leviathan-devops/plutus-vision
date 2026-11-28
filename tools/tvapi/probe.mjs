import fs from 'node:fs';
import { createProxy } from '@mathieuc/tradingview';
import { getCandles } from '@mathieuc/tradingview/data';
const proxy = createProxy(process.env.HTTPS_PROXY, { tls: { ca: fs.readFileSync('/root/.ccr/ca-bundle.crt') } });
const iso = (t) => new Date(t * 1000).toISOString().slice(0, 16);
for (const [sym, tf, from] of [['CME:6E1!', '30', '2026-02-01'], ['CME:6B1!', '30', '2026-02-01'], ['ICEUS:DX1!', '30', '2026-02-01'], ['TVC:US02Y', '60', '2026-02-01'], ['TVC:DE02Y', '60', '2026-02-01'], ['TVC:GB02Y', '60', '2026-02-01'], ['FX:EURUSD', '5', '2026-07-01']]) {
  try {
    const c = await getCandles({ symbol: sym, timeframe: tf, from: new Date(from + 'T00:00:00Z'), clientOptions: proxy });
    console.log('OK  ', sym.padEnd(11), tf.padEnd(3), String(c.length).padStart(6), 'bars', iso(c[0].time), '->', iso(c.at(-1).time), 'vol', c.at(-1).volume);
  } catch (e) { console.log('FAIL', sym, tf, e.code || '', String(e.message).slice(0, 160)); }
}
process.exit(0);
