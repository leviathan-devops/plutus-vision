"""e2_path.py - ENGINE 2 PATH NODES (charter memory/22, plan memory/21 v5 steps 6-7, design memory/23). A NEW module: nothing of Engine 1 / the chain is edited; switch e2_chain.E2_PATH (off).
The forward line of one window [t0, t1) is a list of NODES, built at t0 from the actual price and only bars closed by t0:
  ladder    the Engine 1 zones the leg meets, in sequence (P533:215 'sweeps liquidity zone by zone ... NEVER skips a zone'): drawn pressure zones + the 4H / 1H / 30m supply zones (going up) /
            demand zones (going down) - 4H overview, 1H work, 30m refinement (L-40; KCE 2.1 telescoping); the leg stays inside its parent container (KCE 3.3 'child timeframes cannot break
            parent range') unless the parent's zone breaks
  boundary  at each zone, one of five states (memory/23; calibrated on build weeks, memory/08):
            CLEAN_BREAK    S/D zone with 3+ taps (P533:493 'depleted') or pressure zone ZFP > 45 (6.4.1) -> through it, on to the next zone
            PIERCE_R       narrow zone (under 8 pips): price trades through its far edge to the liquidity just beyond, then returns (P533 Step 0.45a sweep; L-50)
            WICK_RWL       zone stacked with 3+ others, met in the New York morning: turn at the near edge (GS Law 1 'near-impenetrable walls')
            BODY_CONSOL_R  wide zone (15+ pips) or a 4H supply / demand zone: price works inside it, then leaves (FA 8 'minor reaction + retest, zone holds')
            BODY_WL        any other zone that holds: turn at its far edge
  direction the last zone event in the closed 30m candles before t0: rejected (touched, closed back out) -> away from that zone; closed through -> onward; none -> the move in force
            continues (P452 6.6 rule 6)
  time      distance / the pair's own pace in that session (median net move per hour of the same session over the two prior weeks - causal)
Each node: {'t', 'p', 'zone', 'state', 'why'}."""
import datetime as dt
import e1_data as D
import e2_chain as E2

NARROW, WIDE = 8, 15            # pips: the calibration's width classes (memory/08): under 8 pierce-through, 15+ work-inside
STACK = 3                       # GS Law 1: zones from 3+ sources overlapping = a wall
DWELL_BARS = 3                  # his context document: consolidation = 3+ candles (30m)
SES = (('asia', 17, 2), ('london', 2, 8), ('precut', 8, 10), ('ny', 10, 17))


def _ses(t):
    h = dt.datetime.fromtimestamp(t / 1000, D.NY).hour
    return 'asia' if (h >= 17 or h < 2) else 'london' if h < 8 else 'precut' if h < 10 else 'ny'


def pace(pair, t0):
    """the pair's net move per hour in each session, from the 30m bars of the two weeks closed before t0: {'asia': price per hour, ...}"""
    bars = [x for x in D.closed_until(pair, '30', t0) if x['time'] >= t0 - 14 * 86400000]
    by = {}
    for x in bars:
        k = (_ses(x['time']), dt.datetime.fromtimestamp((x['time'] - (7 * 3600000 if _ses(x['time']) == 'asia' else 0)) / 1000, D.NY).date())
        by.setdefault(k, []).append(x)
    out = {}
    for s in ('asia', 'london', 'precut', 'ny'):
        v = sorted(abs(b[-1]['close'] - b[0]['open']) / max(0.5, len(b) / 2.0) for (k, _), b in by.items() if k == s and len(b) >= 3)
        out[s] = v[len(v) // 2] if v else None
    return out


def ladder(X, up, lo=None, hi=None):
    """the zones a leg meets going up (supply side) or down (demand side), nearest first is decided by the caller; each with its class and stack count"""
    ip = [dict(z, _k='IP', _lab=z['name']) for z in X.get('zones', []) if z.get('drawn')]
    sd = [dict(z, _k='SD', _lab=z.get('label', z['tf'])) for z in X.get('sd', []) if z['tf'] in ('240', '60', '30') and z['type'] == ('Supply' if up else 'Demand')]
    allz = [(q['bot'], q['top']) for q in X.get('zones', []) if q.get('drawn')] + [(q['bot'], q['top']) for q in X.get('sd', [])] + [(b['bot'], b['top']) for b in X['v1']['240']['liquidity']]
    pip = X['U'] / 100.0
    out = []
    for z in ip + sd:
        if (lo is not None and z['top'] < lo - 1e-12) or (hi is not None and z['bot'] > hi + 1e-12):
            continue
        z['_stack'] = sum(1 for a, b in allz if a - 3 * pip <= z['top'] and b + 3 * pip >= z['bot']) - 1
        out.append(z)
    return out


def boundary(X, z, up, t):
    """the boundary state of zone z met going up / down at about time t: (state, node price, dwell in 30m bars, why)"""
    pip = X['U'] / 100.0
    i = E2.info(z)
    near, far = (z['bot'], z['top']) if up else (z['top'], z['bot'])
    w = (z['top'] - z['bot']) / pip
    if z['_k'] == 'SD' and i['counter'] == 'Depleted':
        return 'CLEAN_BREAK', far, 0, f"{i['rx']} taps: depleted (P533:493)"
    if z['_k'] == 'IP' and i['zfp'] is not None and i['zfp'] > 45:
        return 'CLEAN_BREAK', far, 0, f"ZFP {i['zfp']}% > 45 (6.4.1)"
    if z['_stack'] >= STACK and _ses(t) in ('precut', 'ny') and dt.datetime.fromtimestamp(t / 1000, D.NY).hour < 12:
        return 'WICK_RWL', near, 0, f"stacked with {z['_stack']} zones, New York morning (GS Law 1)"
    if w >= WIDE or (z['_k'] == 'SD' and z.get('tf') == '240'):
        rung = [r for r in X['v1']['60']['liquidity'] if r['bot'] >= z['bot'] and r['top'] <= z['top']]
        inner = (min(rung, key=lambda r: abs((r['bot'] + r['top']) / 2 - (z['bot'] + z['top']) / 2))['bot' if up else 'top'] if rung else (z['bot'] + z['top']) / 2)
        return 'BODY_CONSOL_R', inner, DWELL_BARS, 'wide / 4H zone: price works inside it (FA 8)'
    if w < NARROW:
        liq = [l['level'] for l in X.get('lsz', []) if not l.get('swept')] + [(r['bot'] if up else r['top']) for r in X['v1']['60']['liquidity'] + X['v1']['240']['liquidity']]
        beyond = [v for v in liq if ((far < v <= far + 10 * pip) if up else (far - 10 * pip <= v < far))]
        if beyond:
            return 'PIERCE_R', (min(beyond) if up else max(beyond)), 0, 'narrow zone: through to the liquidity beyond its far edge (Step 0.45a)'
        return 'PIERCE_R', far, 0, 'narrow zone: to its far edge'
    return 'BODY_WL', far, 0, 'zone holds: turn at its far edge'


def last_event(pair, X, t0, price, lookback=8):
    """what the closed 30m candles before t0 did at the last zone they met: ('rejected' | 'broken', zone, away direction) or None"""
    bars = D.closed_until(pair, '30', t0)[-lookback:]
    if len(bars) < 2:
        return None
    for up in (True, False):
        for z in sorted(ladder(X, up), key=lambda q: abs(((q['bot'] if up else q['top'])) - price)):
            near, far = (z['bot'], z['top']) if up else (z['top'], z['bot'])
            touched = [k for k, x in enumerate(bars) if ((x['high'] >= near) if up else (x['low'] <= near))]
            if not touched:
                continue
            c = bars[-1]['close']
            if (c > far) if up else (c < far):
                return 'broken', z, 'up' if up else 'down'
            if (c < near) if up else (c > near):
                return 'rejected', z, 'down' if up else 'up'
            return 'inside', z, 'down' if up else 'up'
    return None


def window(pair, X, t0, t1, price, first_dir, lo=None, hi=None, max_nodes=8):
    """the nodes of [t0, t1): from `price` in `first_dir`, zone to zone, each boundary state deciding where the node sits and which way the line leaves; time by the session pace"""
    pc = pace(pair, t0)
    nodes = [{'t': t0, 'p': price, 'zone': None, 'state': 'START', 'why': ''}]
    p, t, up = price, t0, first_dir == 'up'
    for _ in range(max_nodes):
        zs = [z for z in ladder(X, up, lo, hi) if ((z['bot'] > p + 1e-12) if up else (z['top'] < p - 1e-12))]
        zs.sort(key=lambda z: z['bot'] if up else -z['top'])
        if not zs:
            break
        z = zs[0]
        st, node_p, dwell, why = boundary(X, z, up, t)
        k = 0
        while st == 'CLEAN_BREAK' and k + 1 < len(zs):                # through it, on to the next zone (zone by zone)
            k += 1; z = zs[k]
            st, node_p, dwell, why = boundary(X, z, up, t)
        if lo is not None and hi is not None:
            node_p = min(max(node_p, lo), hi)                          # the parent container
        v = pc.get(_ses(t)) or next((x for x in pc.values() if x), None)
        if not v or abs(node_p - p) < 1e-12:
            break
        ta = t + int(abs(node_p - p) / v * 3600000)
        if ta >= t1:
            frac = (t1 - t) / (ta - t)
            nodes.append({'t': t1, 'p': p + (node_p - p) * frac, 'zone': z['_lab'], 'state': 'EN ROUTE', 'why': why})
            return nodes
        nodes.append({'t': ta, 'p': node_p, 'zone': z['_lab'], 'state': st, 'why': why, 'zb': z['bot'], 'zt': z['top']})
        t, p = ta, node_p
        if dwell:
            td = min(t1, t + dwell * 1800000)
            nodes.append({'t': td, 'p': p, 'zone': z['_lab'], 'state': st, 'why': 'dwell', 'zb': z['bot'], 'zt': z['top']})
            t = td
            if t >= t1:
                return nodes
        up = up if st == 'CLEAN_BREAK' else (not up)
    if nodes[-1]['t'] < t1:
        nodes.append({'t': t1, 'p': nodes[-1]['p'], 'zone': nodes[-1]['zone'], 'state': 'HOLD', 'why': 'no further zone inside the container'})
    return nodes
