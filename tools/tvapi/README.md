# tools/tvapi - TradingView-API (github.com/Mathieu2301/TradingView-API, npm @mathieuc/tradingview 4.1.2), installed 2026-11-28 on the operator's order (M-77)

Install: `cd tools/tvapi && npm install` (needs the environment hosts data.tradingview.com + symbol-search.tradingview.com, allowed 2026-11-28).
Through this session's proxy the library must be given the proxy and its CA: `createProxy(process.env.HTTPS_PROXY, { tls: { ca: fs.readFileSync('/root/.ccr/ca-bundle.crt') } })`, passed as `clientOptions`.
`node probe.mjs` = reachability + depth check. Measured 2026-11-28 (free access, no login):
- CME:6E1!, CME:6B1!, ICEUS:DX1! (futures, real exchange volume): 30m back to 2026-06-11 (~5,500 bars per request), 1H deeper; older intraday history needs the library's replay mode.
- TVC:US02Y / DE02Y / GB02Y (2-year yields): 1H back to 2026-02-02.
- FX:EURUSD 5m: about four weeks back per request.
Temporal anchor: anything fetched here is cut at the anchor instant by the caller, like every other source.
