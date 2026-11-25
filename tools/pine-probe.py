#!/usr/bin/env python3
"""pine-probe.py - PREFLIGHT ONLY (never a success gate): run a .pine through the Pinebox station engine (/model, the same
route the IDE page uses) on bars from the Pinebox bar store, and print compile errors + drawing counts + texts.
Acceptance is always a frame looked at in Pinebox.
usage: tools/pine-probe.py FILE [--pair DXY] [--tf 1H] [--limit 5000] [--until 2026-07-06T06:00] [--show 12] [--inputs '{"k":v}'] [--dump out.json]"""
import argparse, glob, json, os, sys, urllib.request, urllib.error, datetime
ap = argparse.ArgumentParser(); ap.add_argument('file'); ap.add_argument('--pair', default='DXY'); ap.add_argument('--tf', default='1H')
ap.add_argument('--limit', type=int, default=5000); ap.add_argument('--until'); ap.add_argument('--show', type=int, default=12)
ap.add_argument('--inputs'); ap.add_argument('--dump')
a = ap.parse_args()
SYM = {'DXY': 'TVC_DXY', 'EURUSD': 'FX_EURUSD', 'GBPUSD': 'FX_GBPUSD'}[a.pair]; TF = {'15m': '15', '30m': '30', '1H': '60', '4H': '240'}[a.tf]
bars = []
for f in sorted(glob.glob(os.path.expanduser(f'~/.local/share/pinebox/data/tv-bars/{SYM}/{TF}/*.json'))):
    bars += json.load(open(f))
if a.until:
    cut = int(datetime.datetime.fromisoformat(a.until).replace(tzinfo=datetime.timezone.utc).timestamp() * 1000)
    bars = [b for b in bars if b['time'] < cut]
bars = [{**b, 'volume': b.get('volume') or 0} for b in bars[-a.limit:]]
body = {'source': open(a.file).read(), 'instanceId': 'probe', 'bars': bars,
        'market': {'symbol': a.pair, 'ticker': a.pair, 'timeframe': TF}}
if a.inputs: body['inputs'] = json.loads(a.inputs)
req = urllib.request.Request('http://127.0.0.1:9741/model', data=json.dumps(body).encode(), headers={'content-type': 'application/json'})
try:
    r = json.load(urllib.request.urlopen(req, timeout=600))
except urllib.error.HTTPError as e:
    print('HTTP', e.code, e.read()[:3000].decode()); sys.exit(1)
if a.dump: json.dump(r, open(a.dump, 'w'))
if not r.get('success', True) or r.get('error'):
    print('FAIL', json.dumps(r)[:3000]); sys.exit(1)
d = r.get('data', r)
def brief(o, depth=0):
    if isinstance(o, dict): return {k: (brief(v, depth + 1) if depth < 1 else (f'{type(v).__name__}[{len(v)}]' if isinstance(v, (list, dict)) else v)) for k, v in o.items()}
    if isinstance(o, list): return f'list[{len(o)}]'
    return o
print('bars', len(bars), datetime.datetime.utcfromtimestamp(bars[0]['time'] / 1000), '->', datetime.datetime.utcfromtimestamp(bars[-1]['time'] / 1000))
print(json.dumps(brief(d))[:1500])
def walk(o, path=''):
    if isinstance(o, dict):
        for k, v in o.items(): walk(v, path + '/' + k)
    elif isinstance(o, list) and o and isinstance(o[0], dict) and any(x in path.lower() for x in ('label', 'box', 'line', 'table', 'poly')):
        print(f'-- {path} ({len(o)})')
        for it in o[:a.show]: print('  ', json.dumps(it)[:460])
walk(d)
