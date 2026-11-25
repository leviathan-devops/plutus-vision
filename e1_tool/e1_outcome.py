"""e1_outcome.py - plain facts about what the week's candles did at each zone (a description for the frames, NOT an accuracy score).
usage: python3 e1_outcome.py MONDAY PAIR"""
import sys
import e1_data as D, e1_pine as G


def facts(pair, monday, r):
    b0 = D.boundary_ms(monday)
    bars = [x for x in D.bars(pair, '60') if b0 <= x['time'] < b0 + 7 * 86400000]
    pip = D.PIP[pair]
    rows = []
    for z in r['zones'] + [dict(t, name='Gap in-fill', degree='MODERATE') for t in r['infill']]:
        lo, hi = z['bot'], z['top']
        i0 = next((i for i, x in enumerate(bars) if x['low'] <= hi and x['high'] >= lo), None)
        if i0 is None:
            rows.append((z['name'], lo, hi, z['degree'], 'not reached', '')); continue
        from_above = bars[i0]['open'] > hi or (i0 > 0 and bars[i0 - 1]['close'] > hi)
        from_below = bars[i0]['open'] < lo or (i0 > 0 and bars[i0 - 1]['close'] < lo)
        if not (from_above or from_below):
            inside = sum(1 for x in bars if lo <= x['close'] <= hi)
            rows.append((z['name'], lo, hi, z['degree'], 'week opened inside it', f'{inside}h closed inside')); continue
        far = lo if from_above else hi
        j = next((i for i in range(i0, len(bars)) if (bars[i]['close'] < far if from_above else bars[i]['close'] > far)), None)
        seg = bars[i0:(j if j is not None else len(bars))]
        react = ((max(x['high'] for x in seg) - hi) if from_above else (lo - min(x['low'] for x in seg))) / pip if seg else 0
        day = D.ts(bars[i0]['time'])[5:13]
        if j is None:
            rows.append((z['name'], lo, hi, z['degree'], f"reached {day}h from {'above' if from_above else 'below'}, never closed through", f'moved away up to {react:.0f} pips'))
        else:
            rows.append((z['name'], lo, hi, z['degree'], f"reached {day}h from {'above' if from_above else 'below'}, closed through after {j - i0}h", f'best move away before that {react:.0f} pips'))
    return rows


if __name__ == '__main__':
    monday, pair = sys.argv[1], sys.argv[2]
    r = G.run(pair, monday)
    f = '%.2f' if pair == 'DXY' else '%.4f'
    print(f'{pair} week of {monday}')
    for n, lo, hi, d, a, b in facts(pair, monday, r):
        print(f"  {n:<19}{f % lo}-{f % hi}  {d:<15}{a}; {b}")
