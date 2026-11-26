"""e1_report.py - the Engine 1 audit trail the prompt requires for every step (P533 PART V / P452:1486ff), as plain text.
usage: python3 e1_report.py MONDAY PAIR > out/E1_REPORT_PAIR_MONDAY.txt"""
import sys, json, os
import e1_data as D, e1_pillars as P, e1_synth as S, e1_zones as Z, e1_pine as G


def report(pair, monday):
    r = G.run(pair, monday)
    f = '%.2f' if pair == 'DXY' else '%.4f'
    g = lambda v: f % v
    b0 = D.boundary_ms(monday)
    side = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sidecar', 'out', f'{monday}.json')))
    o = [f"ENGINE 1 - INSTITUTIONAL PRESSURE ZONE MAP - {pair} - week of {monday}", f"Data as-of (temporal boundary): {D.ts(b0)} UTC | spot {g(r['spot'])} (last 1H close before the boundary) | candles: TradingView bar store", '']
    o.append('1. PROTOCOL A - FX OPTION EXPIRIES (investingLive, as-of gated by the sidecar)')
    for s in side.get('sources', [])[:6]:
        if isinstance(s, dict):
            o.append(f"   source: {s.get('url', s.get('source_url', ''))} published {s.get('published_at', '')}")
    exp = side['expiries'].get('EURUSD' if pair == 'DXY' else pair, [])
    if not exp:
        o.append('   NO DATA')
    for e in sorted(exp, key=lambda e: (e.get('cut_date', ''), e['strike'])):
        t = P.tier(e['notional_m'])
        conv = f" -> DXY {P.strike_to_dxy(r['K'], e['strike']):.2f} (band +-{'0.07' if t == 1 else '0.10'})" if pair == 'DXY' else ''
        o.append(f"   {e.get('cut_date', '')} {e['strike']:.4f} {e['notional_m']}M {e.get('ccy', '')} | {'Tier 1 (>=1.5B)' if t == 1 else 'Tier 2 (850M-1.499B)' if t == 2 else 'below 850M - excluded from walls'} | {e.get('state', '')}{conv}")
    if pair == 'DXY':
        h = side['h10']
        o += ['', '2. PILLAR 3/8 - K FACTOR AUDIT', f"   rates (Fed H.10 {h.get('rate_day', '')}, released {h.get('release_date', '')}): {h['rates']}",
              f"   K = 50.14348112 x USDJPY^0.136 x GBPUSD^-0.119 x USDCAD^0.091 x USDSEK^0.042 x USDCHF^0.036 = {r['K']:.4f} ; DXY = K x EURUSD^-0.576"]
    p1 = P.pillar1(pair, monday)
    w = D.weekly(pair, monday)[-1]
    o += ['', '3. PILLAR 1 - PIVOTS', f"   prior week H {g(w['high'])} L {g(w['low'])} C {g(w['close'])}"]
    for var in ('classic', 'fib', 'camarilla'):
        o.append(f"   weekly {var}: " + ' '.join(f"{k} {g(v)}" for k, v in p1['weekly'][var].items()))
    for d in p1['daily']:
        o.append(f"   daily {d['date']} (H {g(d['high'])} L {g(d['low'])} C {g(d['close'])}) classic: " + ' '.join(f"{k} {g(v)}" for k, v in d['classic'].items()))
    o += ['', '4. PILLAR 2 - MA CONFLUENCE GRID (daily closes)'] + [f"   {m['name']:<7}{g(m['p'])}  weight {m['w']}  MAs within 0.15: {m['cluster']}" for m in P.pillar2(pair, monday)]
    o += ['', '5. PILLAR 4 analyst consensus: NO DATA (optional input)   PILLAR 7 ICE/CME positioning: NO DATA (optional input)']
    o += ['', '6. PILLAR 5 STEP 0f - 4H SUPPLY/DEMAND ZONES (origin candle = the candle before the move, wick low to wick high)']
    for z in sorted(r['sd'] + [x for x in r['sd_drop'] if x['origin_time'] >= b0 - 21 * 86400000], key=lambda z: -z['origin_time']):
        oc, nx = z['origin'], z['next']
        o.append(f"   4H Zone Verification: {z['kind']} {z['type']} {g(z['bot'])}-{g(z['top'])} formed {D.ts(z['origin_time'])} | {z['mit']}X mitigated ({z['soft']} soft, {z['hard']} hard)"
                 f" | {'KEPT' if not z['excluded'] else 'EXCLUDED: ' + z['excluded']}")
        o.append(f"      Origin Candle: O={g(oc['open'])} H={g(oc['high'])} L={g(oc['low'])} C={g(oc['close'])} | Next Candle: O={g(nx['open'])} H={g(nx['high'])} L={g(nx['low'])} C={g(nx['close'])}"
                 f" | Directional Move: {'down' if z['type'] == 'Supply' else 'up'} {z['move'] / D.PIP[pair]:.0f} pips{' (>=0.5: strong)' if z['move'] >= P._u(pair, 50) else ''}")
    o += ['', '7. PILLAR 5 STEP 0 / 0.45 / 0.5 - SWING EXTREMES, LIQUIDITY SWEEP ZONES, REPEATED MAGNETS']
    for z in sorted(r['lsz'], key=lambda z: -z['top']):
        o.append(f"   LIQUIDITY SWEEP ZONE: {g(z['bot'])}-{g(z['top'])} | Type: {z['type']} | Source: {z['source']} ({z['grade'] or 'ungraded'}) | Priority: {z['priority']} | {'swept since' if z['swept'] else 'unswept'}")
    for m in P.step05_magnets(pair, r['swings']):
        o.append(f"   {m['kind']} {g(m['price'])} ({m['n']} dates: {', '.join(m['dates'])}) bonus +{m['bonus']}")
    L = r['levels']
    hd = [gp for gp in S.cluster(L, pair) if len(gp) >= 3]
    tight = sum(1 for a, b in zip(L, L[1:]) if a['p'] - b['p'] <= P._u(pair, 10))
    iso = sum(1 for i, x in enumerate(L) if all(abs(x['p'] - y['p']) > P._u(pair, 15) for j, y in enumerate(L) if j != i))
    o += ['', '8. CLUSTERING SCAN', f"   Clustering Scan: {len(L)} total levels | {len(hd)} HIGH-DENSITY ZONES | {tight} TIGHT CONFLUENCES | {iso} ISOLATED LEVELS"]
    o += [f"   HD {g(gp[-1]['p'])}-{g(gp[0]['p'])} ({len(gp)} levels)" for gp in hd]
    o += ['', '9. INSTITUTIONAL PRESSURE ZONE MAP (MODERATE and above)']
    for z in r['zones']:
        d = z['dims']
        o.append(f"   {z['name']:<19}{g(z['bot'])}-{g(z['top'])} | {z['degree']} {z['score']}/14 | ZFP {z['zfp']} ({z['type']}) | {z['tier']}")
        o.append(f"      score: Technical {d['tech']} Options {d['opt']} Analyst {d['ana']} Structural {d['stru']} Psychological {d['psy']} + extreme bonus {d['bonus']} + Regime + POI tier | best level: {z['best']['tag']} {g(z['best']['p'])}")
        for s in z['structs']:
            o.append(f"      candle: {s['kind']} {s['type']} {g(s['bot'])}-{g(s['top'])} {D.ts(s['origin_time'])} {s['mit']}X")
        for s in z['sweeps']:
            o.append(f"      sweep zone: {g(s['bot'])}-{g(s['top'])} {s['source']}")
        o.append('      levels on it: ' + ', '.join(f"{g(x['p'])} {x['tag']}" for x in z['levels'][:40]))
    o += ['', '10. STEP 9.5 GAP SCAN'] + ([f"   Gap In-fill: {g(t['p'])} supported by {' + '.join(t['signals'])} (gap {g(t['gap'][0])}-{g(t['gap'][1])})" for t in r['infill']] or ['   no gap in-fill levels'])
    return '\n'.join(o) + '\n'


if __name__ == '__main__':
    sys.stdout.write(report(sys.argv[2], sys.argv[1]))
