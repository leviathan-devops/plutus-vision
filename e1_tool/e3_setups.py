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

    def candidate(day, z, direction, category, shape, designated=False):
        if (direction == 'LONG') != (side(z) == 'Demand'):
            return None                                 # never anchor LONGs at supply / SHORTs at demand (8.1)
        if any(s['mit'] > 2 for s in z['structs']):
            return None                                 # freshness gate: 3rd+ battle = TP target only
        key = (id(z), day['day'])
        if key in used:
            return None                                 # MAX_MIRRORS_PER_ANCHOR_PER_DAY = 1 (8.5): cap key = (pair, anchor, day)
        # 8.18 direction validation (the checks Engine 1/2 can answer): 4H trend, nearest 4H BoM, macro shape day direction, chain direction
        want_up = direction == 'LONG'
        boms = [t for t in zs if any(q.get('h4bom') for q in t['structs'])]
        nb = min(boms, key=lambda t: min(abs(t['bot'] - day['path'][0][1]), abs(t['top'] - day['path'][0][1]))) if boms else None
        checks = [e2['bias'] == ('up' if want_up else 'down')]
        if nb is not None:
            checks.append((side(nb) == 'Demand') == want_up)
        if day['dir'] != 'range':
            checks.append((day['dir'] == 'up') == want_up)
        cd = next((d['dir'] for d in day.get('_chain', e2['days']) if d['shape'] in ('BS', 'PBS')), None)
        if cd:
            checks.append((cd == 'up') == want_up)
        if not designated and sum(1 for c in checks if not c) > len(checks) / 2:
            return None                                 # consensus against the direction -> reject
        # MoM zones are ladder steps for trend-aligned trades only; never a reversal entry against the 4H storyline (Trading Laws via P533 change 2)
        is_bom = any(q.get('h4bom') for q in z['structs'])
        if not designated and not checks[0]:            # 8.18 check 1 as a gate: no entry against the 4H trend unless E2 designates the reversal at this zone
            return None
        if not designated and z['structs'] and not is_bom and not checks[0]:
            return None
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

    def retest(day, B, direction, chain_days):
        """Law 27: SS -> BS, the range boundary break becomes the BS entry. The broken zone is retested from the other side (8.1 lifecycle: broken resistance = new support).
        Armed only after a 1H close beyond the zone (6.2: breakout confirmed by a sustained move beyond the zone)."""
        key = (id(B), day['day'], 'retest')
        if key in used:
            return None
        if direction == 'LONG':
            entry, lvl = B['top'], B['top']
            bands = [(q['bot'], q['top']) for q in B['structs']] or [(B['bot'], B['top'])]
            lo = max(bands, key=lambda q: q[1])[0]
            sl = lo - BUF[pair] * pip
            opp = [t for t in zs if t['bot'] > entry + 5 * pip]
        else:
            entry, lvl = B['bot'], B['bot']
            bands = [(q['bot'], q['top']) for q in B['structs']] or [(B['bot'], B['top'])]
            hi = min(bands, key=lambda q: q[0])[1]
            sl = hi + BUF[pair] * pip
            opp = [t for t in zs if t['top'] < entry - 5 * pip][::-1]
        risk = abs(entry - sl)
        if risk <= 0 or risk > SL_MAX_PIPS * pip:
            return None
        for t in opp:
            p = (t['bot'] - pip) if direction == 'LONG' else (t['top'] + pip)
            if abs(p - entry) / risk >= RRR_FLOOR:
                used.add(key)
                return {'day': day['day'], 'dayidx': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'].index(day['day']), 'shape': 'SS->BS', 'category': 'Transition', 'dir': direction, 'zone': B['name'], 'zone_rng': (B['bot'], B['top']),
                        'entry': entry, 'sl': sl, 'tp': p, 'rrr': abs(p - entry) / risk, 'tp_zone': t['name'], 'session': 'NY', 't0': e2['days'][0]['t0'], 't1': day['t1'], 'tier': B['tier'][:6], 'score': B['score'],
                        'arm': ('up' if direction == 'LONG' else 'down', lvl)}
        return None

    branches = [('PRIMARY', d) for d in e2['days']] + [('ALT', d) for d in e2.get('alt_days', [])]
    for d in e2.get('alt_days', []):
        d['_chain'] = e2['alt_days']
    for branch, day in branches:
        n_before = len(out)
        ref = day['path'][0][1]
        # a zone the price is already inside is being mitigated, not approached: entries only at zones price comes to from outside
        above = [z for z in zs if z['bot'] > ref]
        below = [z for z in zs if z['top'] < ref][::-1]
        sup = [z for z in above if side(z) == 'Supply']
        dem = [z for z in below if side(z) == 'Demand']
        sh, dr = day['shape'], day['dir']
        if branch == 'ALT' and (sh in ('SS', 'WLS') or (sh == 'R' and dr == 'range')):
            continue                                    # range scalps belong to the range, not to a branch: mapped once (primary days)
        if sh in ('SS', 'WLS') or (sh == 'R' and dr == 'range'):
            # Consolidation: swing scalps both directions at the range boundaries
            for z, d in ((dem[0] if dem else None, 'LONG'), (sup[0] if sup else None, 'SHORT')):
                if z:
                    c = candidate(day, z, d, 'Consolidation', sh)
                    if c: out.append(c)
        elif sh in ('BS', 'PBS'):
            chain_days = e2['days'] if branch == 'PRIMARY' else e2['alt_days']
            first_bs = next(d for d in chain_days if d['shape'] in ('BS', 'PBS'))
            pass        # with-the-move entries = 8R reinforcement stop-limits (not built yet); the retest-of-broken-zone entry was measured 0 TP / 9 SL and removed
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
                c = candidate(day, zz[0], d, 'Reversal', sh, designated=True)      # E2 designates the reversal at this zone, E3 obeys (R3 law)
                if c:
                    chain_days = e2['days'] if branch == 'PRIMARY' else e2['alt_days']
                    fb = next((x for x in chain_days if x['shape'] in ('BS', 'PBS') and x['key'] is not None), None)
                    if fb:
                        c['arm'] = (fb['dir'], fb['key']['top'] if fb['dir'] == 'up' else fb['key']['bot'])
                        c['t0'] = e2['days'][0]['t0']
                    out.append(c)
        for c in out[n_before:]:
            c['branch'] = branch
            c['trigger'] = (f"{e2['decision_zone']} gives way" if branch == 'PRIMARY' else f"{e2['decision_zone']} holds") if day['shape'] not in ('SS',) else 'range holds'
    # SS -> BS transition (8.0.1 'Transition Entry'; Law 27: the range boundary break becomes the BS entry). One per side of the range:
    # a stop entry just beyond the bounding zone, armed by a 1H close beyond it (6.2), stop on the other side of the broken zone,
    # target = Pillar 9 Step 4 measured move (failing level -/+ range height), pulled to an unswept sweep extreme within 0.20, or the first firm zone on the way.
    C, F = e2.get('C'), e2.get('F')
    if C and F:
        height = C['bot'] - F['top']
        for B, direction in ((F, 'SHORT'), (C, 'LONG')):
            dn = direction == 'SHORT'
            entry = B['bot'] - 2 * pip if dn else B['top'] + 2 * pip
            sl = B['top'] + BUF[pair] * pip if dn else B['bot'] - BUF[pair] * pip
            risk = abs(entry - sl)
            if risk > SL_MAX_PIPS * pip:
                continue
            raw = (B['bot'] - height) if dn else (B['top'] + height)
            mags = [q['price'] for q in r['lsz'] if not q['swept'] and abs(q['price'] - raw) <= 20 * pip and ((q['price'] < entry) if dn else (q['price'] > entry))]
            tp, tpn = (min(mags, key=lambda v: abs(v - raw)), 'measured move @ sweep extreme') if mags else (raw, 'measured move (unanchored)')
            firm = [t for t in zs if ((t['top'] < entry and t['top'] > tp) if dn else (t['bot'] > entry and t['bot'] < tp)) and t['type'] in ('Hard Wall', 'Standard Wall')]
            if firm:
                t = max(firm, key=lambda t: t['top']) if dn else min(firm, key=lambda t: t['bot'])
                tp, tpn = (t['top'] + pip if dn else t['bot'] - pip), t['name']
            if abs(tp - entry) / risk < RRR_FLOOR:
                continue
            pri = (e2['bdir'] == 'down') == dn
            out.append({'day': 'Mon', 'dayidx': 0, 'shape': 'SS->BS', 'category': 'Transition', 'dir': direction, 'zone': B['name'], 'zone_rng': (B['bot'], B['top']), 'entry': entry, 'sl': sl, 'tp': tp,
                        'rrr': abs(tp - entry) / risk, 'tp_zone': tpn, 'session': 'NY', 't0': e2['days'][0]['t0'], 't1': e2['days'][-1]['t1'], 'tier': B['tier'][:6], 'score': B['score'],
                        'arm': ('down' if dn else 'up', B['bot'] if dn else B['top']), 'stop_entry': True, 'branch': 'PRIMARY' if pri else 'ALT', 'trigger': f"{B['name']} gives way"})
    # primary-branch setups first, then the alternative branch, in day order; cap 11 per week per pair (CLAUDE.md hard constraint)
    out.sort(key=lambda c: (c['dayidx'], c['branch'] != 'PRIMARY'))
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
        armed = 'arm' not in s
        for x in bars:
            if x['time'] < s['t0']:
                continue
            if not armed:
                if (x['close'] > s['arm'][1]) if s['arm'][0] == 'up' else (x['close'] < s['arm'][1]):
                    armed = True
                continue
            if fill is None:
                if x['low'] <= s['entry'] <= x['high'] or (s.get('stop_entry') and ((x['open'] < s['entry']) if s['dir'] == 'SHORT' else (x['open'] > s['entry']))):
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
        if not s['fill'] and s['result'] == 'not filled' and 'arm' in s:
            s['result'] = 'not filled (armed by 1H close %s %s)' % ('above' if s['arm'][0] == 'up' else 'below', f % s['arm'][1])
        print(f"  #{s['n']} {s['branch'][:3]} {s['day']} {s['session']:<6} {s['dir']:<5} {s['category']:<13} [{s['shape']}] at {s['zone']} {f % s['zone_rng'][0]}-{f % s['zone_rng'][1]} | E {f % s['entry']} SL {f % s['sl']} TP {f % s['tp']} ({s['tp_zone']}) RRR {s['rrr']:.1f} | {s['result']}{' filled ' + D.ts(s['fill'])[5:13] + 'h' if s['fill'] else ''}")
