"""plutus.py - ONE command per week / pair -> ONE Pine v6 script (S6): Engine 1 map + Engine 2 shape chain + Engine 3 trade setups, every number from data closed before the Monday anchor.
usage: python3 plutus.py MONDAY PAIR [out.pine]      (PAIR = DXY | EURUSD | GBPUSD; default output e1_tool/out/PLUTUS_<PAIR>_<MONDAY>.pine)"""
import sys, os
import e1_pine as EP, e2_chain as E2

HERE = os.path.dirname(os.path.abspath(__file__))


_MEMO = {}


def _setups(pair, monday):
    if (pair, monday) not in _MEMO:
        _MEMO[(pair, monday)] = run(pair, monday)[2]
    return _MEMO[(pair, monday)]


def run(pair, monday):
    X = EP.run(pair, monday)
    lead = E2.build('DXY', monday, EP.run('DXY', monday)) if pair != 'DXY' else None      # DXY = master direction (P533:1899-1917; GS Law 7)
    chain = E2.build(pair, monday, X, lead)
    if lead is not None:
        chain['divergence'] = divergence(lead, E2.build(pair, monday, X, None))
        # the pair's alternative chains = the DXY alternatives translated onto the pair's own zones (P533 6.6 v5.0.0 pair translation; Step 4); Decision Zone = the pair's own
        # bound on the failing side (D-110)
        chain['alts'] = []
        for a_ in lead.get('alts') or []:
            pa = E2.build(pair, monday, X, a_['chain'])
            nz = pa.get('near')
            if nz is not None and pa.get('bdir') in ('up', 'down'):
                chain['alts'].append({'alt': {'decision_zone': nz.get('name', ''), 'zone': (nz['bot'], nz['top']), 'reach': nz.get('reach'), 'dir': pa['bdir'], 'threshold': '1H close beyond it',
                                              'text': f"ALTERNATIVE (DXY alternative translated): {' -> '.join(c['shape'] for c in pa['chain'])}"}, 'chain': pa})
    import e3_trades as E3
    source = None
    if pair != 'DXY':
        # Phase 10 (E3C:723-770): DXY is processed first; EUR/USD mirrors the DXY setups, GBP/USD mirrors the active EUR/USD mirrors
        src_pair = 'DXY' if pair == 'EURUSD' else 'EURUSD'
        source = _setups(src_pair, monday)
    setups = E3.build(pair, monday, X, chain, source)
    extra = E2.pine(pair, monday, chain) + (E3.pine(pair, monday, setups) if E3 else []) + table(pair, monday, X, chain, setups)
    # the zones Engine 2 designates (bounds, pivot, targets, the from / to zone of every chain step): a V1 liquidity band among them is drawn by the tool even when it stands alone (D-107)
    des = [chain.get(k) for k in ('ceil', 'floor', 'pivot', 'target', 'target2', 'far_liq', 'near', 'far')] + [st.get(k) for st in chain['chain'] for k in ('frm', 'to')]
    X['e2_zones'] = [(z['bot'], z['top']) for z in des if isinstance(z, dict) and 'bot' in z]
    edges = [d[k] for d in chain['days'] for k in ('lo', 'hi')] + [q['entry'] for q in setups['setups']]      # ... and a band a day box ends on / a setup's entry stands on
    X['e2_zones'] += [(b['bot'], b['top']) for b in X['v1']['240']['liquidity'] if any(b['bot'] - 1e-9 <= e <= b['top'] + 1e-9 for e in edges)]
    src = EP.generate(pair, monday, X, extra, EP.reach(X, chain))
    return X, chain, setups, src + '\n' + '\n'.join('// ' + l for l in report(pair, monday, X, chain, setups)) + '\n'


FAMILY = {'SS': 'SS', 'RWL': 'SS', 'PRWL': 'SS', 'STORM': 'SS', 'BS': 'BS', 'PBS': 'BS', 'R': 'R', 'WL': 'WL', 'WLS': 'WL', 'PWL': 'WL'}
MASTER = ['SS', 'BS', 'R', 'WL']


def divergence(core, own):
    """E3C 10.7 'The 35% Divergence Rule (FLAG ONLY - never override)': per day, the DXY chain's shape family against the pair's OWN chain (the pair's bounds read without the DXY lead):
    'Shape-family alignment (SS~SS/RWL/STORM/PRWL; BS~BS/PBS; R; WL~WL/WLS/PWL) OR +-1 step on master SS->BS->R->WL; divergence = (5-aligned)/5; missing day = not-aligned;
    <= 0.35 -> VALIDATED else -> DIVERGED, flag only'. The DXY translation stays the pair's chain (P533 9.13 'Do NOT override the DXY direction')."""
    cd = {d['day']: d for d in core.get('days', [])}; od = {d['day']: d for d in own.get('days', [])}
    aligned, rows = 0, []
    for day in ('Mon', 'Tue', 'Wed', 'Thu', 'Fri'):
        a, b = cd.get(day), od.get(day)
        ok = False
        if a and b:
            fa, fb = {FAMILY.get(x, x) for x in a['shapes']}, {FAMILY.get(x, x) for x in b['shapes']}
            ok = bool(fa & fb) or any(abs(MASTER.index(x) - MASTER.index(y)) <= 1 for x in fa for y in fb if x in MASTER and y in MASTER)
        aligned += ok
        rows.append(f"{day} {'+'.join(a['shapes']) if a else '-'} / {'+'.join(b['shapes']) if b else '-'}{'' if ok else ' (not aligned)'}")
    dv = (5 - aligned) / 5
    return {'value': dv, 'state': 'VALIDATED' if dv <= 0.35 else 'DIVERGED', 'rows': rows, 'own_dir': own.get('bdir')}


CASCADE = {'DXY': 'native', 'EURUSD': 'DXY->EU', 'GBPUSD': 'EU->GU'}
SES_UTC = {'London Open': '06:00-09:00', 'London/NY Overlap': '12:00-14:00', 'NY Open': '12:30-14:00', 'NY Mid': '14:00-18:00'}      # GS Part 10 session clock (ET) in UTC, EDT weeks


def report(pair, monday, X, chain, R):
    """E3C 8.13 'The E3 Output Format (FULL)' + Phase 8 label law (BE1-BE12): weekly execution calendar (every day covered or 'No qualifying setups - [reason]'), the setups by category with
    DAY / SESSION WINDOW / SHAPE TRIGGER / SETUP CATEGORY / ANCHOR HIT WINDOW (the E2-designated session bracket of the setup's day, R3 law), parent reference on reinforcements (BE9),
    daily session notes with the day's catalysts (BE8), the profit-taking law (BE11), every discard with its reason (Phase 12), weekly stats with the f(T) acceptance line (E3C:996).
    Carried at the end of the Pine as comments: one command -> one file."""
    f = (lambda v: '%.3f' % v) if pair == 'DXY' else (lambda v: '%.5f' % v)
    S = [s for s in R.get('setups', []) if not s.get('clone')]
    rep = {}
    for s in R.get('setups', []):
        if s.get('clone'):
            rep.setdefault(s['origin']['id'], []).append(s['day'])
    days = chain.get('days', [])
    name = lambda a: (a.get('label') or a.get('name') or 'liquidity rung')
    cls = lambda a: (a.get('kind') or (a.get('mech') or {}).get('bom') or ('LSZ' if (a.get('sweep') or a.get('lsz')) else 'LQZ' if (a.get('liq') or 'tf' not in a) else 'IP'))
    o = [f"ENGINE 3 - FULL-SPECTRUM TRADE MAP | WEEK OF {monday} | {PNAME[pair]}", '',
         '=== WEEKLY EXECUTION CALENDAR ===', 'Day | Pair | Dir | Setup Type | Entry | Shape | Session | Conf | Notes']
    for d in days:
        rows = [s for s in S if s['day'] == d['day']]
        for s in rows:
            note = (f"if {s['parent']}" if s.get('parent') else '') + (f" repeated {', '.join(rep[s['id']])}" if rep.get(s['id']) else '') + (f" rests from {s['rest_from']}" if s.get('rest_from') else '')
            o.append(f"{d['day']} | {PNAME[pair]} | {s['dir']} | {s['category']} | {f(s['entry'])} | {s['shape']} | {s['session']} | {s['confidence']} | {s['id']}{' ' + note.strip() if note.strip() else ''}")
        if not rows:
            # E3C 8.13 'every day covered or "No qualifying setups - [reason]"': a day that carries only per-day repeats lists them; a day whose orders fell to the 11-trade limit says so
            reps = [f"{s['origin']['id']} {s['dir']} {f(s['entry'])}" for s in R.get('setups', []) if s.get('clone') and s['day'] == d['day']]
            capped = any(l.startswith(d['day'] + ' ') and 'EMISSION_CAPPED' in l for l in R.get('log', []))
            if reps:
                o.append(f"{d['day']} | {PNAME[pair]} | - | Swing Scalp (repeat) | - | {'+'.join(d['shapes'])} | London Open | - | per-day repeats: {'; '.join(reps)}")
            else:
                why = 'the orders of this day fell to the 11-trade limit of the week (EMISSION_CAPPED, see DISCARDED)' if capped else "no anchor of this day's shape passed the gates (see DISCARDED)"
                o.append(f"{d['day']} | {PNAME[pair]} | - | - | - | {'+'.join(d['shapes'])} | - | - | No qualifying setups - {why}")
    for d_ in ('Mon', 'Tue', 'Wed', 'Thu', 'Fri'):
        if not any(d['day'] == d_ for d in days):
            o.append(f"{d_} | {PNAME[pair]} | - | - | - | - | - | - | No qualifying setups - Engine 2 gives this day no shape (chain confidence under 25%)")
    for title, cats in (('HTF SWING SETUPS', ('HTF Swing', 'Reversal')), ('SWING SCALP SETUPS', ('Swing Scalp',)), ('REINFORCEMENT ENTRIES', ('Reinforcement',)), ('TRANSITION SETUPS', ('Transition',))):
        rows = [s for s in S if s['category'] in cats]
        o += ['', f"--- {title} ---"] + ([] if rows else ['none'])
        for s in rows:
            a = s['anchor']; dd = next((d for d in days if d['day'] == s['day']), None)
            o.append(f"{s['id']} | {PNAME[pair]} | {s['dir']} | {s['category']} | Day: {s['day']} | Session: {s['session']} | Shape: {s['shape']}")
            o.append(f"  Entry: {f(s['entry'])} | SL: {f(s['sl'])} | TP: {f(s['tp'])} | RRR: {s['rrr']:.2f}{(' / blended ' + format(s['rrr_blended'], '.2f')) if s.get('rrr_blended') else ''} | Quality: {s.get('quality', '-')} | Confidence: {s['confidence']}")
            o.append(f"  Anchor Zone: {name(a)} [{cls(a)}{', tested ' + str(a['mit']) + 'x' if a.get('mit') is not None else ''}] | Shape Trigger: {s['shape']} @ {s['day']} {s['session']} | Day Catalysts: {', '.join(dd['triggers']) if dd and dd.get('triggers') else 'none listed'}")
            o.append(f"  Audit Trail: {s['why']} | attempts {s.get('attempts', 1)}")
            o.append(f"  Cascade Source: {CASCADE[pair]} | Parent Trade Ref: {s.get('parent') or '-'} | Anchor Hit Window: {s['day']} {s['session']} {SES_UTC.get(s['session'], '')} UTC" + (f" (order rests from {s['rest_from']})" if s.get('rest_from') else '') + (f" | repeated: {', '.join(rep[s['id']])}" if rep.get(s['id']) else ''))
            # E3C 12.2 floor invariants (checkMirrorFloorV45): 'Floor: RRR >= 2.5 | Session bracket valid | SL envelope (within GOLDEN_SL_MAX_PIPS = 9.5)' - reported per setup as flags
            # (his own golden GBP/USD stops are 10.6-14.1 pips, so the envelope is a flag here, not a discard); E3C 12.3 CS-1: the stop against the day's open of the E2 path
            slp = abs(s['entry'] - s['sl']) / EP.D.PIP[pair] if hasattr(EP, 'D') else s.get('sl_pips', 0)
            if s.get('six'):
                o.append(f"  Direction validation (E3C 8.18): {s['six'][0]} of 6 disagree - " + ', '.join(f"{k}={v or '-'}" for k, v in s['six'][1]))
            o.append(f"  Floor invariants (E3C 12.2): RRR {'>= 2.5 ok' if s['rrr'] >= 2.5 else '< 2.5'} | session bracket = the E2 step's days | SL envelope 9.5p: {'inside' if slp <= 9.5 + 1e-9 else f'OUTSIDE ({slp:.1f}p)'}"
                     + (f" | ALT trigger: 1H close {'above' if s['trigger']['dir'] == 'up' else 'below'} {f(s['trigger']['level'])} ({s['trigger']['zone']})" if s.get('trigger') else ''))
    o += ['', '--- DAILY SESSION NOTES ---']
    for d in days:
        o.append(f"{d['day']}: {'+'.join(d['shapes'])} {d['dir']} | key zone {d['key']} | range {f(d['lo'])}-{f(d['hi'])} | confidence {int(round(100 * d['conf']))}% | catalysts: {', '.join(d.get('triggers') or []) or 'none listed'}")
    o.append('Weekend: Close ALL positions by NY close Friday - per pair')
    dv = chain.get('divergence')
    if dv is not None:
        o += ['', f"--- CASCADE (E3C 10.7, flag only) --- divergence {dv['value']:.2f} -> {dv['state']} | DXY chain / pair's own chain per day: " + ' | '.join(dv['rows'])
              + f" | pair's own breakout direction: {dv['own_dir'] or 'none'}"]
    o += ['', '--- DISCARDED (reason on every discard) ---'] + ([l for l in R.get('log', [])] or ['none'])
    rr = sorted(s['rrr'] for s in S)
    med = (rr[len(rr) // 2] if len(rr) % 2 else (rr[len(rr) // 2 - 1] + rr[len(rr) // 2]) / 2) if rr else 0.0
    n = lambda c: sum(1 for s in S if s['category'] in c)
    o += ['', '--- WEEKLY STATS ---',
          f"Total Setups: {len(S)} | HTF: {n(('HTF Swing', 'Reversal'))} | Scalps: {n(('Swing Scalp',))} | Reinforcements: {n(('Reinforcement',))} | Transitions: {n(('Transition',))}",
          f"Average RRR: {(sum(rr) / len(rr)) if rr else 0.0:.2f} | Median RRR: {med:.2f}",
          f"f(T) Acceptance (E3C:996: 8 per pair minimum): {len(S)} setups on {PNAME[pair]} - {'met' if len(S) >= 8 else 'NOT met'}"]
    return o


ACCENT = {'DXY': ('20,20,40', '100,150,255'), 'EURUSD': ('10,30,60', '80,140,255'), 'GBPUSD': ('40,15,50', '180,100,220')}       # P533 10.10 pair accent colours
PNAME = {'DXY': 'DXY', 'EURUSD': 'EUR/USD', 'GBPUSD': 'GBP/USD'}


def table(pair, monday, X, chain, R):
    """P533 Part X 10.7 'TABLE: 2x17' (position.top_right; background color.new(color.black, 10); border RGB 40,40,45): row 0 header (TRIDENT v8 | pair + week), 1 chain + confidence,
    2 alternative chain + confidence, 3 day-by-day shape, 4 ZONES header, 5-9 IP zones (five rows, top to bottom: PG4), 10 TRADES header, 11-13 short trade (entry / SL | TP / day + RRR),
    14-16 long trade; price format 10.9 (DXY #.##, pairs #.####); PG5 exact row indexing"""
    import datetime as dt
    f = (lambda v: '%.2f' % v) if pair == 'DXY' else (lambda v: '%.4f' % v)
    m0 = dt.date.fromisoformat(monday); m1 = m0 + dt.timedelta(days=4)
    wk = f"{m0.strftime('%b')}{m0.day}-{(m1.strftime('%b') if m1.month != m0.month else '')}{m1.day}"
    ch = chain.get('chain') or []
    alt = chain.get('alt') or {}
    altc = chain.get('alt_chain') or {}
    rows = [('TRIDENT v8', f"{PNAME[pair]} {wk}"),
            ('Chain', (' -> '.join(c['shape'] for c in ch) or '-') + (f" | {int(round(100 * ch[-1]['cum']))}%" if ch else '')),
            ('Alt chain', ((' -> '.join(c['shape'] for c in altc.get('chain', [])) + (f" | {int(round(100 * alt['conf']))}%" if alt.get('conf') is not None else '')) if altc.get('chain') else '-')),
            ('Days', ' | '.join(f"{d['day']} {'+'.join(d['shapes'])}" for d in chain.get('days', [])) or '-'),
            ('ZONES', '')]
    spot = X['spot']
    zs = sorted([z for z in X['zones'] if z.get('drawn')], key=lambda z: min(abs(z['bot'] - spot), abs(z['top'] - spot)))[:5]
    zs.sort(key=lambda z: -z['top'])
    for k in range(5):
        rows.append((zs[k]['name'], f"{f(zs[k]['bot'])}-{f(zs[k]['top'])} | {zs[k]['degree']} | {zs[k]['zfp']} ZFP") if k < len(zs) else ('-', '-'))
    rows.append(('TRADES', ''))
    S = (R or {}).get('setups', []) if isinstance(R, dict) else []
    for side in ('SHORT', 'LONG'):
        t = next((s for s in S if s['dir'] == side and not s.get('clone')), None)
        if t is None:
            rows += [(side.capitalize(), '-'), ('SL | TP', '-'), ('Day | RRR', '-')]
        else:
            rows += [(f"{side.capitalize()} {t['id']}", 'Entry ' + f(t['entry'])), ('SL | TP', f"{f(t['sl'])} | {f(t['tp'])}"), ('Day | RRR', f"{t['day']} {t['shape']} | {t['rrr']:.1f}R")]
    assert len(rows) == 17
    hb, ht = ACCENT[pair]
    o = ['    if show_tbl', '        var table tb = table.new(position.top_right, 2, 17, bgcolor=color.new(color.black, 10), border_color=color.rgb(40,40,45), border_width=1)']
    for i, (a, b) in enumerate(rows):
        head = i in (0, 4, 10)
        bg = f"color.rgb({hb})" if head else 'color.new(color.black, 10)'
        tc = f"color.rgb({ht})" if head else 'color.white'
        for col_, txt in ((0, a), (1, b)):
            o.append(f'        table.cell(tb, {col_}, {i}, "{txt}", text_color={tc}, bgcolor={bg}, text_size=size.small, text_halign=text.align_left)')
    return o


if __name__ == '__main__':
    monday, pair = sys.argv[1], sys.argv[2]
    out = sys.argv[3] if len(sys.argv) > 3 else os.path.join(HERE, 'out', f'PLUTUS_{pair}_{monday}.pine')
    X, chain, setups, src = run(pair, monday)
    open(out, 'w').write(src)
    print(out)
