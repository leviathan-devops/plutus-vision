// cdp-console.mjs SECONDS ['JS to evaluate after attaching'] - print the page's console/exception/network-failure events (debug aid for Pinebox)
const secs = Number(process.argv[2] || 15), js = process.argv[3] || '';
const tabs = await (await fetch('http://127.0.0.1:9222/json')).json();
const t = tabs.find(x => x.type === 'page' && /pine|9851/.test(x.url)) || tabs[0];
const ws = new WebSocket(t.webSocketDebuggerUrl); let id = 0;
const send = (m, p = {}) => ws.send(JSON.stringify({ id: ++id, method: m, params: p }));
ws.onopen = () => { send('Runtime.enable'); send('Log.enable'); send('Network.enable'); if (js) setTimeout(() => send('Runtime.evaluate', { expression: js, awaitPromise: true }), 500); };
ws.onmessage = (e) => { const d = JSON.parse(e.data);
  if (d.method === 'Runtime.consoleAPICalled' && ['error', 'warning'].includes(d.params.type)) console.log('[console.' + d.params.type + ']', d.params.args.map(a => a.value ?? a.description ?? '').join(' ').slice(0, 400));
  if (d.method === 'Runtime.exceptionThrown') console.log('[exception]', JSON.stringify(d.params.exceptionDetails).slice(0, 500));
  if (d.method === 'Log.entryAdded' && d.params.entry.level === 'error') console.log('[log]', d.params.entry.text.slice(0, 300), d.params.entry.url || '');
  if (d.method === 'Network.requestWillBeSent' && /model|prepare|station/.test(d.params.request.url)) console.log('[req]', d.params.request.method, d.params.request.url, (d.params.request.postData || '').length);
  if (d.method === 'Network.responseReceived' && /model|prepare|station/.test(d.params.response.url)) console.log('[res]', d.params.response.status, d.params.response.url);
  if (d.method === 'Network.loadingFailed') console.log('[netfail]', d.params.errorText, d.params.requestId); };
setTimeout(() => { ws.close(); process.exit(0); }, secs * 1000);
