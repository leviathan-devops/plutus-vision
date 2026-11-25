"""e3_setups.py - ENGINE 3: TRADE SETUPS. Binding spec: canon/Toolset/TRIDENT_v5.3.3_CORRECTED_E3_ENGINE.md (R-16).
R3 law: E2 designates, E3 obeys - every setup is anchored to an E1 zone + an E2 shape day; E3 only resolves entry / SL / TP geometry.
Implemented phases: 0 setup universe per shape (8.0.1), 1 working-day map (8.0.2), 2 zone selection + freshness gate (8.1), 3 TS-1 entry (8.2),
4 SL ladder-steps rule (a) + TP at the opposing zone with the opposing-rung walk for RRR (8.3), RRR floor 3.0 (8.20), cap 11 per week per pair."""
import e1_data as D, e1_pillars as P

BUF = {'EURUSD': 2, 'GBPUSD': 3, 'DXY': 3}            # per-pair SL buffer, pips (8.3 Law 7; '3 pips outside the back edge')
RRR_FLOOR, SL_MAX_PIPS, CAP = 3.0, 36, 11
DAYMS = 86400000
SESSION = {'Consolidation': ('London', 6, 11), 'Reversal': ('NY', 12, 20), 'HTF Swing': ('NY', 12, 20), 'Transition': ('NY', 12, 20)}   # UTC hours within the trading day


def side(z):
    return z['side']                                   # 'Supply' (short anchor) / 'Demand' (long anchor)


def anchor_band(z, direction, approach_from):
    """F1-C / TS-1: the entry band is the internal structure nearest the approaching price (a 1H candle or the sweep rung); else the zone"""
    bands = [(s['bot'], s['top']) for s in z['structs']] + [(s['bot'], s['top']) for s in z['sweeps']]
    if not bands:
        return z['bot'], z['top']
    return min(bands, key=lambda b: abs((b[0] if direction == 'SHORT' else b[1]) - approach_from))


def build(pair, monday, r):
    pip = D.PIP[pair]
    e2 = r['e2']
    zs = sorted(r['zones'], key=lambda z: z['bot'])
    out, used = [], set()

    def candidate(day, z, direction, category, shape):
        if (direction == 'LONG') != (side(z) == 'Demand'):
            return None                                 # never anchor LONGs at supply / SHORTs at demand (8.1)
        if any(s['mit'] > 2 for s in z['structs']):
            return None                                 # freshness gate: 3rd+ battle = TP target only
        key = (id(z), direction)
        if key in used:
            return None                                 # per-anchor emission cap / dedup identity
        ref = day['path'][0][1]
        lo, hi = anchor_band(z, direction, ref)
        if direction == 'SHORT':
            entry = lo + (pip if z['structs'] else 0)   # TS-1: bottom edge of supply; F1-A: order-block shorts lifted 1 pip
            sl = hi + BUF[pair] * pip
            opp = [t for t in zs if side(t) == 'Demand' and t['top'] < entry][::-1]
        else:
            entry = hi                                  # TS-1: top edge of demand
            sl = lo - BUF[pair] * pip
            opp = [t for t in zs if side(t) == 'Supply' and t['bot'] > entry]
        risk = abs(entry - sl)
        if risk <= 0 or risk > SL_MAX_PIPS * pip:
            return None
        tp = rrr = tz = None
        for t in opp:                                   # Law 14: walk the opposing rungs until the RRR floor is met
            near = t['top'] if direction == 'SHORT' else t['bot']
            strong = t['tier'].startswith('Tier 1') or t['score'] >= 10
            p = near + (pip if direction == 'SHORT' else -pip) if strong else (t['bot'] + t['top']) / 2     # strong zone: near edge + 1 pip spread; else midpoint
            q = abs(p - entry) / risk
            if q >= RRR_FLOOR:
                tp, rrr, tz = p, q, t
                break
        if tp is None:
            return None
        used.add(key)
        ses = SESSION[category]
        return {'day': day['day'], 'dayidx': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'].index(day['day']), 'shape': shape, 'category': category, 'dir': direction, 'zone': z['name'], 'zone_rng': (z['bot'], z['top']),
                'entry': entry, 'sl': sl, 'tp': tp, 'rrr': rrr, 'tp_zone': tz['name'], 'session': ses[0], 't0': day['t0'], 't1': day['t1'], 'tier': z['tier'][:6], 'score': z['score']}

    for day in e2['days']:
        ref = day['path'][0][1]
        # a zone the price is already inside is being mitigated, not approached: entries only at zones price comes to from outside
        above = [z for z in zs if z['bot'] > ref]
        below = [z for z in zs if z['top'] < ref][::-1]
        sup = [z for z in above if side(z) == 'Supply']
        dem = [z for z in below if side(z) == 'Demand']
        sh, dr = day['shape'], day['dir']
        if sh in ('SS', 'WLS') or (sh == 'R' and dr == 'range'):
            # Consolidation: swing scalps both directions at the range boundaries
            for z, d in ((dem[0] if dem else None, 'LONG'), (sup[0] if sup else None, 'SHORT')):
                if z:
                    c = candidate(day, z, d, 'Consolidation', sh)
                    if c: out.append(c)
        elif sh in ('BS', 'PBS'):
            # HTF swing with the move: anchor = the nearest zone behind price on the move's side (demand for up, supply for down)
            z = (dem[0] if dem else None) if dr == 'up' else (sup[0] if sup else None)
            if z:
                c = candidate(day, z, 'LONG' if dr == 'up' else 'SHORT', 'HTF Swing', sh)
                if c: out.append(c)
        elif sh in ('WL', 'RWL', 'R'):
            # Reversal at the zone that rejects: after an up move the short anchors at the supply reached; after a down move the long at the demand reached
            tgt = day['path'][1][1] if sh == 'WL' else day['path'][0][1]
            if (sh == 'WL' and dr == 'up') or (sh != 'WL' and dr == 'down'):
                zz = [z for z in zs if side(z) == 'Supply' and z['top'] >= tgt - 5 * pip]
                d = 'SHORT'
            else:
                zz = [z for z in zs if side(z) == 'Demand' and z['bot'] <= tgt + 5 * pip][::-1]
                d = 'LONG'
            if zz:
                c = candidate(day, zz[0], d, 'Reversal', sh)
                if c: out.append(c)
    out = out[:CAP]
    for i, s in enumerate(out):
        s['n'] = i + 1
    return out


def simulate(pair, monday, setups):
    """what the week's 1H candles did to each setup (post-boundary data; description only). Fill window = from the setup's day to the week's end."""
    b0 = D.boundary_ms(monday)
    bars = [x for x in D.bars(pair, '60') if b0 <= x['time'] < b0 + 7 * DAYMS]
    for s in setups:
        long = s['dir'] == 'LONG'
        st, fill = 'not filled', None
        for x in bars:
            if x['time'] < s['t0']:
                continue
            if fill is None:
                if x['low'] <= s['entry'] <= x['high']:
                    fill = x['time']
                    if (x['low'] <= s['sl']) if long else (x['high'] >= s['sl']):
                        st = 'SL'; break
                continue
            hit_sl = (x['low'] <= s['sl']) if long else (x['high'] >= s['sl'])
            hit_tp = (x['high'] >= s['tp']) if long else (x['low'] <= s['tp'])
            if hit_sl:
                st = 'SL'; break
            if hit_tp:
                st = 'TP'; break
        if fill is not None and st == 'not filled':
            last = bars[-1]['close']
            st = 'open %+.1fR' % (((last - s['entry']) if long else (s['entry'] - last)) / abs(s['entry'] - s['sl']))
        s['result'], s['fill'] = st, fill
    return setups


if __name__ == '__main__':
    import sys, e1_pine as G
    monday, pair = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'DXY'
    r = G.run(pair, monday)
    f = '%.2f' if pair == 'DXY' else '%.4f'
    ss = simulate(pair, monday, build(pair, monday, r))
    print(f"ENGINE 3 {pair} {monday} | E2: {r['e2']['primary']}")
    for s in ss:
        print(f"  #{s['n']} {s['day']} {s['session']:<6} {s['dir']:<5} {s['category']:<13} [{s['shape']}] at {s['zone']} {f % s['zone_rng'][0]}-{f % s['zone_rng'][1]} | E {f % s['entry']} SL {f % s['sl']} TP {f % s['tp']} ({s['tp_zone']}) RRR {s['rrr']:.1f} | {s['result']}{' filled ' + D.ts(s['fill'])[5:13] + 'h' if s['fill'] else ''}")
