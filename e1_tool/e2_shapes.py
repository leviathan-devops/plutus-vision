"""e2_shapes.py - ENGINE 2: MACRO SHAPE CHAIN MAP (P533 PART VI, lines 1725-2057; verbatim in canon_extract/P533_lines_1725-2057_PART_VI_ENGINE2.md).
Primary timeframe 1H, structural validation 4H. Every shape is anchored to an Engine 1 zone and conditioned on that zone's ZFP class (6.4.1).
Canon gives the ZFP conditions as numbers; Engine 1 carries ZFP as the zone type's range (L-35), so the conditions are applied to the type:
  Hard Wall 5-15 (<20: rejects) | Standard Wall 15-30 (<30: holds) | Post-Expiry Ghost 20-40 (mid: pause) | Soft Wall 30-50 (may fail) | One-Touch 50-70 (>45: fails)."""
import e1_data as D, e1_pillars as P

HOLD = {'Hard Wall': 4, 'Standard Wall': 3, 'Post-Expiry Ghost': 2, 'Soft Wall': 1, 'One-Touch': 0}   # how firmly the zone type holds
DAYMS = 86400000


def day_shape(d, prev, adr):
    """6.1 taxonomy applied to one completed trading day (used for the CURRENT shape at the boundary and to describe what a week did)."""
    rng = d['high'] - d['low']
    body = d['close'] - d['open']
    if rng >= 0.8 * adr and abs(body) >= 0.6 * rng:
        return 'BS', 'up' if body > 0 else 'down'                      # decisive directional move
    up_spike, dn_spike = d['high'] - max(d['open'], d['close']), min(d['open'], d['close']) - d['low']
    if rng >= 0.8 * adr and max(up_spike, dn_spike) >= 0.5 * rng:
        return 'WL', 'up' if dn_spike > up_spike else 'down'           # spike and reject; direction = the rejection's direction
    if prev and prev[0] in ('BS', 'WL') and rng < 0.8 * adr:
        return 'R', 'range'
    return 'SS', 'range'


def strength(z):
    return (HOLD[z['type']], z['score'], 1 if z['tier'].startswith('Tier 1') else 0)


def chain(pair, monday, r, force_dir=None, lead_dir=None):
    zs = sorted(r['zones'], key=lambda z: z['bot'])
    spot, b0 = r['spot'], D.boundary_ms(monday)
    days = D.daily(pair, monday)
    adr = sum(x['high'] - x['low'] for x in days[-10:]) / 10
    prev = None
    for i in (-3, -2, -1):
        prev = day_shape(days[i], prev, adr)
    cur_shape, cur_dir = prev
    inside = next((z for z in zs if z['bot'] <= spot <= z['top']), None)
    above = [z for z in zs if z['bot'] > spot]
    below = [z for z in zs if z['top'] < spot][::-1]
    # 4H storyline bias (6.8 pressure reading tiebreaker): the last 20 4H closes
    h4 = D.closed(pair, '240', monday)[-20:]
    bias = 'up' if h4[-1]['close'] > h4[0]['close'] else 'down'
    names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    out, audit = [], []
    pos = spot
    C, F = (above[0] if above else None), (below[0] if below else None)
    # Step 1-2: current shape and the first transition
    audit.append(f"Current Shape: {cur_shape} {cur_dir} | Anchoring Zone: {(inside or C or F or {'name': 'none'})['name']} | spot {spot}")
    # SS: price between a ceiling and a floor (or held by the zone it sits in). Canon: consolidation lasts 2-4 days; 'BS is most likely days away' unless a bounding zone is failing.
    rng_lo = inside['bot'] if inside else (F['top'] if F else pos - adr)
    rng_hi = inside['top'] if inside else (C['bot'] if C else pos + adr)
    if C and F:
        # 6.4.1: the bounding zone whose ZFP class is failing gives the direction; same class on both sides = unclear -> the 4H storyline decides (Pressure Reading Rules)
        hc, hf = HOLD[C['type']], HOLD[F['type']]
        weaker = C if hc < hf else F if hf < hc else (C if bias == 'up' else F)
    else:
        weaker = C or F
    bdir = 'up' if weaker is C else 'down'
    both_hold = C and F and HOLD[C['type']] >= 3 and HOLD[F['type']] >= 3
    if lead_dir and not force_dir:                  # 6.6 pair translation: same shapes as the DXY chain, direction inverted
        bdir, weaker = lead_dir, (C if lead_dir == 'up' else F)
    if force_dir:                                   # Step 4: the alternative chain = the other side of the range gives way
        bdir, weaker, both_hold = force_dir, (C if force_dir == 'up' else F), False
    # a momentum rejection on the last day (WL closing beyond the prior day's close) skips the consolidation: WL -> RWL (6.4.1)
    momentum = cur_shape == 'WL' and ((days[-1]['close'] > days[-2]['close']) if cur_dir == 'up' else (days[-1]['close'] < days[-2]['close'])) and abs(days[-1]['close'] - days[-2]['close']) > 0.25 * adr
    if cur_shape == 'BS':
        ss_days = 1                     # BS -> R (< 1 session) -> next
    elif momentum:
        ss_days = 1
        if not force_dir:
            bdir = cur_dir; weaker = C if bdir == 'up' else F
    else:
        ss_days = 2                     # trading speed rule: today's move is tomorrow's move
    plan = []
    for i in range(ss_days):
        plan.append({'shape': 'R' if (cur_shape == 'BS' and i == 0) else 'SS', 'dir': 'range', 'key': inside or weaker, 'lo': rng_lo, 'hi': rng_hi, 'conf': 'HIGH' if i == 0 else 'MODERATE-HIGH'})
    if both_hold:
        while len(plan) < 5:
            plan.append({'shape': 'SS', 'dir': 'range', 'key': inside or C, 'lo': F['top'], 'hi': C['bot'], 'conf': 'MODERATE'})
        audit.append(f"SS -> [both bounding zones hold: {C['name']} {C['zfp']}, {F['name']} {F['zfp']}] -> SS continues")
    else:
        # Step 3: BS toward the weaker bounding zone, then the target zone's ZFP class decides (6.4.1)
        seq = above if bdir == 'up' else below
        k = 0
        edge = lambda z: (z['bot'] if bdir == 'up' else z['top'])
        far = lambda z: (z['top'] if bdir == 'up' else z['bot'])
        start = pos
        if not seq:
            tgt_price = pos + (adr if bdir == 'up' else -adr) * 1.5
            plan.append({'shape': 'BS', 'dir': bdir, 'key': inside, 'p0': start, 'p1': tgt_price, 'conf': 'MODERATE'})
            audit.append(f"SS -> [no zone {bdir}] -> BS {bdir} to measured move {tgt_price:.4f}")
        else:
            B = seq[0]
            if HOLD[B['type']] >= 3:
                # the bound holds (ZFP < 30): the move into it is rejected (6.2 priority 2): WL at the zone, back into the range
                plan.append({'shape': 'WL', 'dir': bdir, 'key': B, 'p0': start, 'p1': edge(B), 'back': (rng_lo + rng_hi) / 2, 'conf': 'MODERATE-HIGH'})
                audit.append(f"SS -> [Trigger: {B['name']} ZFP {B['zfp']} holds] -> WL at the zone -> SS")
            else:
                T = seq[1] if len(seq) > 1 else None
                tgt = edge(T) if T else far(B) + (adr if bdir == 'up' else -adr)
                # trading speed rule: the 4H move takes twice as long -> the BS spans two days
                mid = far(B)
                plan.append({'shape': 'BS', 'dir': bdir, 'key': B, 'p0': start, 'p1': mid, 'conf': 'MODERATE-HIGH'})
                plan.append({'shape': 'BS', 'dir': bdir, 'key': T or B, 'p0': mid, 'p1': tgt, 'conf': 'MODERATE'})
                audit.append(f"SS -> [Trigger: {B['name']} ZFP {B['zfp']} fails] -> BS {bdir} -> target {(T or B)['name']}")
                if T:
                    h = HOLD[T['type']]
                    nxt = 'RWL' if h == 4 else 'PBS' if h == 0 else 'R'
                    audit.append(f"BS -> [target zone {T['name']} ZFP {T['zfp']}] -> {nxt} (6.4.1)")
                    if nxt == 'RWL':
                        plan.append({'shape': 'RWL', 'dir': 'down' if bdir == 'up' else 'up', 'key': T, 'p0': tgt, 'p1': mid, 'conf': 'MODERATE'})
                    elif nxt == 'PBS':
                        T2 = seq[2] if len(seq) > 2 else None
                        plan.append({'shape': 'PBS', 'dir': bdir, 'key': T2 or T, 'p0': tgt, 'p1': edge(T2) if T2 else far(T) + (adr if bdir == 'up' else -adr), 'conf': 'LOW-MODERATE'})
                    else:
                        plan.append({'shape': 'R', 'dir': 'down' if bdir == 'up' else 'up', 'key': T, 'p0': tgt, 'p1': tgt - 0.382 * (tgt - start), 'conf': 'MODERATE'})
        while len(plan) < 5:
            last = plan[-1]
            c = last.get('back', last.get('p1', pos))
            plan.append({'shape': 'SS', 'dir': 'range', 'key': last['key'], 'lo': c - 0.25 * adr, 'hi': c + 0.25 * adr, 'conf': 'LOW-MODERATE'})
    plan = plan[:5]
    # Step 5: day-by-day decomposition with times and a projected path for the chart
    t0 = b0 + 2 * DAYMS            # Friday 17:00 NY + 48h = Sunday 17:00 NY = start of Monday's trading day
    for i, s in enumerate(plan):
        a, b = t0 + i * DAYMS, t0 + (i + 1) * DAYMS
        if s['shape'] in ('SS',) or (s['shape'] == 'R' and 'lo' in s):
            m = (s['lo'] + s['hi']) / 2
            path = [(a, pos), (a + DAYMS // 3, s['hi']), (a + 2 * DAYMS // 3, s['lo']), (b, m)]
            pos = m
        elif s['shape'] == 'WL':
            path = [(a, pos), (a + DAYMS // 2, s['p1']), (b, s['back'])]
            pos = s['back']
        else:
            path = [(a, s['p0']), (b, s['p1'])]
            pos = s['p1']
        s.update({'day': names[i], 't0': a, 't1': b, 'path': path, 'key_name': s['key']['name'] if s['key'] else 'none'})
        out.append(s)
    primary = ' -> '.join(dict.fromkeys(f"{s['shape']}{'' if s['dir'] == 'range' else ' ' + s['dir']}" for s in out))
    alt_dir = 'down' if bdir == 'up' else 'up'
    dz = (C if bdir == 'up' else F)
    alt = f"DECISION ZONE: {dz['name'] if dz else 'none'} holds -> ALTERNATIVE: SS -> WL at the zone -> BS {alt_dir}"
    res_alt = None
    if not force_dir:
        res_alt = chain(pair, monday, r, force_dir=alt_dir)
        alt = f"DECISION ZONE: {dz['name'] if dz else 'none'} holds -> ALTERNATIVE: {res_alt['primary']}"
    return {'C': C, 'F': F, 'alt_days': res_alt['days'] if res_alt else [], 'bdir': bdir, 'decision_zone': dz['name'] if dz else 'none', 'days': out, 'primary': primary, 'alternative': alt, 'audit': audit, 'current': (cur_shape, cur_dir), 'bias': bias, 'adr': adr}


def actual(pair, monday):
    """what each day of the week did (for comparison against the forecast on the chart; uses post-boundary data, never fed back)"""
    b0 = D.boundary_ms(monday)
    h = [x for x in D.bars(pair, '60') if b0 + 2 * DAYMS <= x['time'] < b0 + 7 * DAYMS]
    days = D.daily(pair, monday)
    adr = sum(x['high'] - x['low'] for x in days[-10:]) / 10
    out, prev = [], None
    for i in range(5):
        seg = [x for x in h if b0 + (2 + i) * DAYMS <= x['time'] < b0 + (3 + i) * DAYMS]
        if not seg:
            continue
        d = {'open': seg[0]['open'], 'close': seg[-1]['close'], 'high': max(x['high'] for x in seg), 'low': min(x['low'] for x in seg)}
        prev = day_shape(d, prev, adr)
        out.append((['Mon', 'Tue', 'Wed', 'Thu', 'Fri'][i], prev[0], prev[1], d))
    return out


if __name__ == '__main__':
    import sys, e1_pine as G
    monday, pair = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'DXY'
    r = G.run(pair, monday)
    e = chain(pair, monday, r)
    print(f"ENGINE 2 {pair} {monday} | Primary Timeframe: 1H | Structural Validation: 4H | 4H bias {e['bias']}")
    for a in e['audit']:
        print('  ', a)
    print('   PRIMARY:', e['primary'], '|', e['alternative'])
    act = {a[0]: a for a in actual(pair, monday)}
    for s in e['days']:
        a = act.get(s['day'])
        print(f"   {s['day']}: {s['shape']} {s['dir']} | Key Zone: {s['key_name']} | Confidence: {s['conf']}    || actual: {a[1] + ' ' + a[2] if a else '-'}")
