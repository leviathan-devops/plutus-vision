"""microtrades.py MAPS - scratch LOCATOR for plan M3: Engine 2 micro legs (switch e2_chain.MICRO_PATH on) as trades by Law 27 (E3C 8.21 'TP of trade N = entry of trade N+1'):
in every drawn piece, the level where a leg ENDS (a zone / band edge) is a limit entry for the next leg's direction, TP = the next leg's end level - 1.5 p, SL = beyond the entry level by
max(5 p, 1/3 of the TP distance) clamped to 15 p (GS Law 4); live from the piece's anchor to the leg's planned end time + 2 h; filtered RR >= 3 (swing scalp floor)."""
import sys, io, contextlib, collections
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import plutus, e1_data as D, e2_chain as E2
E2.MICRO_PATH = True
H = 3600000
tot = collections.Counter()
for m in sys.argv[1:]:
    pair, mon = m.split(':')
    plutus._MEMO.clear()
    with contextlib.redirect_stdout(io.StringIO()):
        X, ch, R, pine = plutus.run(pair, mon, daily=True)
    pip = D.PIP[pair]; b15 = D.bars(pair, '15')
    row = collections.Counter()
    for seg in ch['segments']:
        pts = seg
        for (t0, v0), (t1, v1), (t2, v2) in zip(pts, pts[1:], pts[2:]):
            if abs(v1 - v0) < 0.5 * pip or abs(v2 - v1) < 3 * pip or (v1 - v0) * (v2 - v1) >= 0:
                continue                                       # need a turn at v1
            up = v2 > v1
            e = v1 + (0.5 * pip if up else -0.5 * pip)
            tp = v2 - (1.5 * pip if up else -1.5 * pip)
            sd = min(15 * pip, max(5 * pip, abs(tp - e) / 3))
            sl = e - sd if up else e + sd
            if abs(tp - e) / sd < 3: row['rr<3'] += 1; continue
            f = None; r = None
            for b in b15:
                if b['time'] < pts[0][0]: continue
                if f is None:
                    if b['time'] >= t1 + 2 * H: r = 'NF'; break
                    if (b['low'] <= e) if up else (b['high'] >= e): f = b['time']
                    else: continue
                if (b['low'] <= sl) if up else (b['high'] >= sl): r = 'SL'; break
                if (b['high'] >= tp) if up else (b['low'] <= tp): r = 'TP'; break
            row[r or 'OPEN'] += 1
    print(pair, mon, dict(row), flush=True)
    tot.update(row)
print('TOTAL', dict(tot), 'win %.0f%%' % (100 * tot['TP'] / max(1, tot['TP'] + tot['SL'])))
