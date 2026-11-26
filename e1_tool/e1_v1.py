"""e1_v1.py - the supply/demand + liquidity layer of Engine 1 = the SEALED V1 baseline's own output, taken as data (operator ruling R-30:
"the Liquidity zones are A+ and the S/D are A- ... this already solves 1 side of the coin"; R-04: E1 = supply, demand, liquidity AND IP zones).
The sealed file is never edited: its source is run through the Pinebox engine exactly as the Pine IDE runs it (the IDE's default window = the newest 400 bars),
on the bars CLOSED before the temporal anchor, per timeframe, and its boxes are read back:
  bgColor #3179f5.. = bullish order block (demand)   #f77c80.. = bearish order block (supply)   #2E8B57.. = liquidity band (the green ladder)
usage: python3 e1_v1.py MONDAY PAIR [TF]"""
import json, os, sys, urllib.request
import e1_data as D

HERE = os.path.dirname(os.path.abspath(__file__))
SEALED = os.path.join(HERE, '..', 'indicator', 'plutus-vision-v1.sealed.pine')
STATION = 'http://127.0.0.1:9741/model'
IDE_WINDOW = 400                                   # pinebox pine-ide.mjs: cfg.limit = 400 (the window the operator sees V1 computed on)
TFS = ('240', '60', '30', '15')
TFNAME = {'240': '4H', '60': '1H', '30': '30m', '15': '15m'}
# The station's engine reports syminfo.mintick = 0.01 for every symbol (measured), and the sealed V1 floors its band thickness on max(0.35 x ATR(14), mintick) (:1202-1203)
# and paints [top - max(span, thickness), top] (:1244-1249). On TradingView the tick is DXY 0.001, EUR/USD and GBP/USD 0.00001. The bars are therefore sent scaled by
# 0.01 / tick, so the engine's 0.01 IS the chart's tick, and the boxes are scaled back: every number V1 draws is V1's own (R-30: taken as data, never rebuilt).
TV_TICK = {'DXY': 0.001, 'EURUSD': 0.00001, 'GBPUSD': 0.00001}
ENGINE_TICK = 0.01


def _atr14(bars):
    """Pine ta.atr(14): Wilder's moving average of the true range"""
    tr = [bars[0]['high'] - bars[0]['low']] + [max(b['high'] - b['low'], abs(b['high'] - p['close']), abs(b['low'] - p['close'])) for p, b in zip(bars, bars[1:])]
    a = sum(tr[:14]) / 14
    for x in tr[14:]:
        a = (a * 13 + x) / 14
    return a


def harvest(pair, monday, tf):
    """-> {'tf', 'bars', 'order_blocks': [{side, bot, top, time}], 'liquidity': [{bot, top}]} ; cached on disk (deterministic for closed bars)"""
    cache = os.path.join(HERE, 'cache', 'v1s', f'{pair}_{tf}_{monday}.json')
    if os.path.exists(cache):
        return json.load(open(cache))
    k = ENGINE_TICK / TV_TICK[pair]
    bars = [{**b, 'volume': b.get('volume') or 0} for b in D.closed(pair, tf, monday)[-IDE_WINDOW:]]
    sent = [{**b, 'open': b['open'] * k, 'high': b['high'] * k, 'low': b['low'] * k, 'close': b['close'] * k} for b in bars]
    body = {'source': open(SEALED).read(), 'instanceId': f'e1v1-{pair}-{tf}', 'bars': sent, 'market': {'symbol': pair, 'ticker': pair, 'timeframe': tf}}
    req = urllib.request.Request(STATION, data=json.dumps(body).encode(), headers={'content-type': 'application/json'})
    r = json.load(urllib.request.urlopen(req, timeout=600))
    m = (r.get('data') or r)['model']
    obs, liq = [], []
    for b in m['boxes']:
        c = (b.get('bgColor') or '').lower()
        lo, hi = min(b['top'], b['bottom']) / k, max(b['top'], b['bottom']) / k
        if c.startswith('#3179f5'):
            obs.append({'side': 'Demand', 'bot': lo, 'top': hi, 'time': b['left']})
        elif c.startswith('#f77c80'):
            obs.append({'side': 'Supply', 'bot': lo, 'top': hi, 'time': b['left']})
        elif c.startswith('#2e8b57'):
            liq.append({'bot': lo, 'top': hi})
    out = {'tf': tf, 'bars': len(bars), 'first_bar': bars[0]['time'], 'last_bar': bars[-1]['time'],
           'order_blocks': sorted(obs, key=lambda z: -z['top']), 'liquidity': sorted(liq, key=lambda z: -z['top'])}
    os.makedirs(os.path.dirname(cache), exist_ok=True)
    json.dump(out, open(cache, 'w'))
    return out


def harvest_all(pair, monday):
    return {tf: harvest(pair, monday, tf) for tf in TFS}


if __name__ == '__main__':
    monday, pair = sys.argv[1], sys.argv[2]
    f = '%.3f' if pair == 'DXY' else '%.5f'
    for tf in ([sys.argv[3]] if len(sys.argv) > 3 else TFS):
        h = harvest(pair, monday, tf)
        print(f"{pair} {TFNAME[tf]} | {h['bars']} bars {D.ts(h['first_bar'])} -> {D.ts(h['last_bar'])} | order blocks {len(h['order_blocks'])} | liquidity bands {len(h['liquidity'])}")
        for z in h['order_blocks']:
            print('   OB  %-6s %s - %s  from %s' % (z['side'], f % z['bot'], f % z['top'], D.ts(z['time'])))
        print('   LQ  ' + '  '.join('%s-%s' % (f % z['bot'], f % z['top']) for z in h['liquidity']))
