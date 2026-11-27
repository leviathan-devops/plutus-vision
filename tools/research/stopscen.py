"""stopscen.py PAIR MONDAY SETUP_ID - BUG LOCATOR / ILLUSTRATION ONLY (reads the week's bars; never imported by the tool; never a verdict). For one emitted setup: the Engine 1
objects behind the entry (within 30 pips), the stop the code chose and why, the two stop families of the operator's rule (M-58: '2-3 pips outside the entry zone or 1-2 pips inside the
next zone'; Trading Laws; E3C:247-256), and for each candidate stop: distance, RRR with the code's TP, and what the 15m candles did after the fill (TP first / SL first)."""
import sys, os, io, contextlib, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'e1_tool'))
import plutus, e1_data as D
pair, mon, sid = sys.argv[1], sys.argv[2], sys.argv[3]
with contextlib.redirect_stdout(io.StringIO()):
    X, E2, R, src = plutus.run(pair, mon)
pip = D.PIP[pair]; f = (lambda v: '%.3f' % v) if pair == 'DXY' else (lambda v: '%.5f' % v)
ts = lambda t: dt.datetime.fromtimestamp(t / 1000, dt.UTC).strftime('%a %H:%M')
s = next(q for q in R['setups'] if q['id'] == sid and not q.get('clone'))
lng = s['dir'] == 'LONG'; e, sl, tp = s['entry'], s['sl'], s['tp']
a = s['anchor']
print(f"{pair} {mon} {sid} {s['day']} {s['shape']} {s['dir']}  E {f(e)}  SL {f(sl)} ({abs(e - sl) / pip:.1f}p)  TP {f(tp)} ({abs(tp - e) / pip:.1f}p)  RRR {s['rrr']}")
print(f"  code: {s['why'][:400]}")
print(f"  anchor zone: {a.get('label') or a.get('name')} {f(a['bot'])}-{f(a['top'])}" if 'bot' in a else f"  anchor: {a}")
objs = []
for z in X['zones']:
    objs.append(('IP ' + z['name'], z['bot'], z['top'], 'zone'))
for q in X['sd']:
    if q.get('broken') is None and q['tf'] in ('15', '30', '60', '240'):
        objs.append((f"S/D {q['tf']} {q['type']} {q.get('kind', '')} mit{q['mit']}", q['bot'], q['top'], 'zone'))
for tf, v in X['v1'].items():
    for b in v['liquidity']:
        objs.append((f"LQ {tf} ({'THICK 4H band' if tf == '240' else 'thin rung'})", b['bot'], b['top'], 'thick' if tf == '240' else 'thin'))
for l in X['lsz']:
    if not l['swept']:
        objs.append((f"LSZ {l['side']} level {f(l['level'])} ({l['source']})", l['bot'], l['top'], 'lsz'))
behind = lambda o: (o[2] < e + 1e-12) if lng else (o[1] > e - 1e-12)
holding = [o for o in objs if o[1] - 1e-12 <= e <= o[2] + 1e-12]
near = sorted([o for o in objs if behind(o) and not (o[1] - 1e-12 <= e <= o[2] + 1e-12) and ((e - o[2]) if lng else (o[1] - e)) <= 30 * pip], key=lambda o: (e - o[2]) if lng else (o[1] - e))
print('  objects HOLDING the entry:')
for o in holding:
    print(f"     {o[0]:<62} {f(o[1])}-{f(o[2])}")
print('  objects BEHIND the entry (nearest first, within 30 pips):')
for o in near:
    print(f"     {o[0]:<62} {f(o[1])}-{f(o[2])}   close edge {((e - o[2]) if lng else (o[1] - e)) / pip:5.1f}p from entry")
b15 = [x for x in D.bars(pair, '15') if s['valid_from'] <= x['time'] < D.week_end_ms(mon)]
fill = next((x for x in b15 if ((x['low'] <= e) if lng else (x['high'] >= e))), None)
def outcome(stop):
    if fill is None:
        return 'not filled'
    for x in [y for y in b15 if y['time'] >= fill['time']]:
        if (x['low'] <= stop) if lng else (x['high'] >= stop):
            return f"STOPPED {ts(x['time'])}"
        if (x['high'] >= tp) if lng else (x['low'] <= tp):
            return f"TP {ts(x['time'])}"
    return 'open at week end'
if fill is not None:
    after = [y for y in b15 if y['time'] >= fill['time']]
    hit = next((i for i, y in enumerate(after) if ((y['high'] >= tp) if lng else (y['low'] <= tp))), None)
    seg = after[:hit + 1] if hit is not None else after
    ext = min(y['low'] for y in seg) if lng else max(y['high'] for y in seg)
    print(f"  15m: filled {ts(fill['time'])}; worst price before the TP {f(ext)} ({abs(e - ext) / pip:.1f}p against the entry); TP reached {ts(after[hit]['time']) if hit is not None else 'never'}")
cands = [('CODE  ' + s['why'].split('SL ')[1].split(';')[0][:60], sl)]
back_zone = (a['bot'] if lng else a['top']) if 'bot' in a else None
if back_zone is not None:
    for k in (2, 3):
        cands.append((f"A  {k} pips outside the entry zone's back edge {f(back_zone)}", back_zone - k * pip if lng else back_zone + k * pip))
for o in holding:
    if o[3] in ('thick', 'thin'):
        bz = o[1] if lng else o[2]
        cands.append((f"A' 2 pips outside the back edge of the liquidity step holding the entry ({o[0][:20]} {f(o[1])}-{f(o[2])})", bz - 2 * pip if lng else bz + 2 * pip))
liq_hold = [o for o in holding if o[3] in ('thick', 'thin')]
step = min(liq_hold, key=lambda o: o[2] - o[1]) if liq_hold else None
outer = max(liq_hold, key=lambda o: o[2] - o[1]) if liq_hold else None
ref = (min(o[1] for o in liq_hold) if lng else max(o[2] for o in liq_hold)) if liq_hold else e   # beyond EVERY liquidity band holding the entry
beyond = lambda o: (o[2] < ref - 1e-12) if lng else (o[1] > ref + 1e-12)
dist = lambda o: (e - o[2]) if lng else (o[1] - e)
thin = sorted([o for o in near if o[3] == 'thin' and beyond(o)], key=dist)
thick = sorted([o for o in near if o[3] == 'thick' and beyond(o)], key=dist)
lsz = sorted([o for o in near if o[3] == 'lsz' and beyond(o)], key=dist)
picks = [('1st thin rung beyond the bands holding the entry', thin[0] if thin else None), ('2nd thin rung beyond them', thin[1] if len(thin) > 1 else None),
         ('1st THICK 4H band beyond them', thick[0] if thick else None), ('1st unswept sweep zone beyond them', lsz[0] if lsz else None)]
for nm, o in picks:
    if o is None:
        continue
    ce = o[2] if lng else o[1]
    for k in (1, 2):
        cands.append((f"B  {k}p inside the close edge {f(ce)} of the {nm} ({o[0][:22]} {f(o[1])}-{f(o[2])})", ce - k * pip if lng else ce + k * pip))
print('  candidate stops:')
for nm, st in cands:
    d = abs(e - st) / pip
    print(f"     {nm:<92} SL {f(st)}  {d:5.1f}p  RRR {abs(tp - e) / abs(e - st):4.2f}  -> {outcome(st)}")
