"""e2_calib_dir.py - BUILD-WEEK LOCATOR (memory/23): at the London open (02:00 NY) and the New York cut (10:00 NY) of every build day, with the week-anchor Engine 1 map:
(1) which fact known at that instant lines up with the direction of the session that follows (London 02:00-08:00, New York 10:00-17:00);
(2) at which ladder zone, counted from the price, the session's move ended - for three ladder definitions. Reads later bars to MEASURE only."""
import sys, os, io, contextlib, collections, datetime as dt
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'e1_tool'))
import plutus, e1_data as D, e2_chain as E2, e2_path as EP
BUILD = ('2026-02-02', '2026-02-09', '2026-02-16', '2026-02-23', '2026-03-02', '2026-03-09', '2026-03-16', '2026-03-23', '2026-04-06', '2026-08-17', '2026-08-31', '2026-09-21')
R = collections.defaultdict(lambda: [0, 0]); K = collections.defaultdict(collections.Counter); n_s = 0
for mon in BUILD:
    m0 = dt.date.fromisoformat(mon)
    for pair in ('DXY', 'EURUSD', 'GBPUSD'):
        with contextlib.redirect_stdout(io.StringIO()):
            X = plutus._map(pair, mon); trend = E2.structure_4h(pair, mon)
        pip = D.PIP[pair]; B = D.bars(pair, '30'); at = {x['time']: x for x in B}
        for k in range(5):
            dd = m0 + dt.timedelta(days=k)
            for ses, h0, h1 in (('London', 2, 8), ('NY', 10, 17)):
                u0, u1 = E2._ms(dd, h0), E2._ms(dd, h1)
                if u0 < D.boundary_ms(mon): continue
                pre = [at[t] for t in range(u0 - 8 * 1800000, u0, 1800000) if t in at]
                seg = [at[t] for t in range(u0, u1, 1800000) if t in at]
                if len(pre) < 6 or len(seg) < 8: continue
                p0 = pre[-1]['close']; net = seg[-1]['close'] - p0
                if abs(net) < 5 * pip: continue                       # a session that went nowhere has no direction to grade
                up = net > 0; n_s += 1
                def rec(name, pred):
                    if pred is None: return
                    R[(ses, name)][1] += 1; R[(ses, name)][0] += (pred == ('up' if up else 'down'))
                lad_u = sorted([z for z in EP.ladder(X, True) if z['bot'] > p0], key=lambda z: z['bot']); lad_d = sorted([z for z in EP.ladder(X, False) if z['top'] < p0], key=lambda z: -z['top'])
                du = (lad_u[0]['bot'] - p0) if lad_u else None; ddn = (p0 - lad_d[0]['top']) if lad_d else None
                rec('toward the NEARER ladder zone', None if du is None or ddn is None else ('up' if du < ddn else 'down'))
                rec('toward the FARTHER ladder zone (room to move)', None if du is None or ddn is None else ('up' if du > ddn else 'down'))
                ev = EP.last_event(pair, X, u0, p0)
                rec('last zone event, away direction (rejected / inside)', None if ev is None or ev[0] == 'broken' else ev[2])
                rec('last zone event = broken -> onward', None if ev is None or ev[0] != 'broken' else ev[2])
                mom = pre[-1]['close'] - pre[-5]['close']
                rec('same as the last 2 hours', None if abs(mom) < 3 * pip else ('up' if mom > 0 else 'down'))
                rec('against the last 2 hours', None if abs(mom) < 3 * pip else ('down' if mom > 0 else 'up'))
                mom8 = pre[-1]['close'] - pre[0]['open']
                rec('same as the last 4 hours', None if abs(mom8) < 5 * pip else ('up' if mom8 > 0 else 'down'))
                rec('4H structure direction', trend)
                inside = next((z for z in EP.ladder(X, True) + EP.ladder(X, False) if z['bot'] <= p0 <= z['top']), None)
                rec('price INSIDE a supply zone -> down / demand zone -> up', None if inside is None or inside['_k'] == 'IP' else ('down' if inside['type'] == 'Supply' else 'up'))
                hug_u = du is not None and du <= 3 * pip; hug_d = ddn is not None and ddn <= 3 * pip
                rec('pressing within 3 pips under a zone -> up into it / over a zone -> down into it', 'up' if (hug_u and not hug_d) else 'down' if (hug_d and not hug_u) else None)
                import e2_data as ED
                dl = ED.delta(pair, u0, u0 - 4 * 3600000)
                cvd = dl[-1][2] if dl else 0.0
                rec('delta proxy of the last 4 hours (buying -> up)', None if not dl or cvd == 0 else ('up' if cvd > 0 else 'down'))
                rec('price vs delta DIVERGENCE over 4 hours (price up, delta down -> down)', None if not dl or cvd == 0 or abs(mom8) < 5 * pip or (mom8 > 0) == (cvd > 0) else ('down' if mom8 > 0 else 'up'))
                ys = ED.yield_spread(pair, u0)
                usd = None if not ys or ys['d1w'] == 0 else ('up' if ys['d1w'] > 0 else 'down')       # dollar direction
                rec('2Y spread change over the week (dollar side)', None if usd is None else (usd if pair == 'DXY' else ('down' if usd == 'up' else 'up')))
                wk0 = next((at[t]['open'] for t in range(D.boundary_ms(mon), u0, 1800000) if t in at), None)
                rec('same as the week so far', None if wk0 is None or abs(p0 - wk0) < 10 * pip else ('up' if p0 > wk0 else 'down'))
                day0 = at.get(E2._ms(dd - dt.timedelta(days=1), 17)); 
                rec('same as the day so far (since 17:00)', None if day0 is None or abs(p0 - day0['open']) < 5 * pip else ('up' if p0 > day0['open'] else 'down'))
                rec('against the day so far (since 17:00)', None if day0 is None or abs(p0 - day0['open']) < 5 * pip else ('down' if p0 > day0['open'] else 'up'))
                if pair != 'DXY':
                    dx = {x['time']: x for x in D.bars('DXY', '30') if u0 - 5 * 3600000 <= x['time'] < u0}
                    dk = sorted(dx)
                    if len(dk) >= 6:
                        dm = dx[dk[-1]]['close'] - dx[dk[-5]]['close']
                        rec('inverse of DXY, last 2 hours', None if abs(dm) < 0.03 else ('down' if dm > 0 else 'up'))
                # (2) where the session's move ended, counted in ladder zones from the price
                ext = max(x['high'] for x in seg) if up else min(x['low'] for x in seg)
                for nm, keep in (('pressure + 4H/1H/30m S/D', lambda z: True), ('pressure + 4H/1H S/D', lambda z: z['_k'] == 'IP' or z.get('tf') in ('240', '60')), ('pressure zones only', lambda z: z['_k'] == 'IP')):
                    lad = [z for z in (lad_u if up else lad_d) if keep(z)]
                    reached = sum(1 for z in lad if ((ext >= z['bot']) if up else (ext <= z['top'])))
                    K[(ses, nm)][min(reached, 5)] += 1
print(f"build sessions graded: {n_s}")
print("\n(1) NEXT-SESSION DIRECTION from a fact known at the update instant: right / cases")
for k in sorted(R, key=lambda k: (k[0], -R[k][0] / max(1, R[k][1]))):
    a, n = R[k]
    if n >= 15: print(f"  {k[0]:<7} {k[1]:<82} {a:4d}/{n:4d} = {100 * a / n:3.0f}%")
print("\n(2) LADDER ZONES REACHED by the session's move (0 = turned before the first zone ... 5 = five or more): share of sessions")
for k in sorted(K):
    n = sum(K[k].values()); print(f"  {k[0]:<7} {k[1]:<28} " + '  '.join(f"{j}: {100 * K[k][j] / n:3.0f}%" for j in range(6)) + f"   n={n}")
