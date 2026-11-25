"""proto2.py - E1 v2: <= 4 wide bands from EXTREME-type anchors only (not congestion). usage: python3 proto2.py [DEV|VALID]"""
import re, sys, score as S
LV = {p: {w['week']: w for w in S.levels(p)} for p in S.SYM}

def anchors(w, A, mode):
    out = []   # (price_lo, price_hi, weight, tag)
    for l in w['levels']:
        t = l['tag']
        if t == 'OPT1': out.append((l['p'], l['p'], 3.0, t))
        elif t in ('OPT2', 'OPT3'): out.append((l['p'], l['p'], 2.0, t))
        elif t == 'OPT4': out.append((l['p'], l['p'], 1.0, t))
        elif t in ('PWH', 'PWL'): out.append((l['p'], l['p'], 2.0, t))
        elif t in ('HWC', 'LWC'): out.append((l['p'], l['p'], 1.0, t))
        elif re.match(r'W\w*c[RS]\d', t) and mode != 'nopiv': out.append((l['p'], l['p'], 1.0, 'Wpiv'))
        elif t.startswith(('SwHi', 'SwLo')): out.append((l['lo'], l['hi'], 1.0 + min(1.0, (l['bonus'] or 0)), 'swing'))
        elif re.match(r'D[HL]\d', t): out.append((l['p'], l['p'], 0.5, t[:2]))
    for z in w['sd']:
        if z['top'] - z['bot'] <= 0.4 * A:
            wgt = (3.0 if z['mit'] == 0 else 2.0 if z['mit'] == 1 else 0.0) * (1.0 if z['scale'] == 240 else 0.6)
            if wgt > 0: out.append((z['bot'], z['top'], wgt, 'SD%d' % z['scale']))
    return out

def build(pair, mon, k=0.25, m=0.15, g=0.12, reach=1.0, thr_in=2.0, thr_out=3.0, mode='', n_side=2):
    w = LV[pair][mon]; A = S.awr(pair, mon); sp = w['spot']; W = k * A; an = anchors(w, A, mode); step = 0.02 * A
    bands = []
    for side in (1, -1):
        chosen = []
        for slot in range(n_side):
            thr = thr_in if slot == 0 else thr_out
            best = None; d = m if not chosen else None
            x0 = (sp + m * A) if side > 0 else (sp - m * A - W)
            if chosen:
                x0 = chosen[-1][1] + g * A if side > 0 else chosen[-1][0] - g * A - W
            x = x0
            while (x + W <= sp + reach * A) if side > 0 else (x >= sp - reach * A):
                s = sum(a[2] for a in an if a[0] < x + W and a[1] > x)
                if s >= thr:
                    # slide outward while the score keeps rising (centre the band on the evidence), then stop: nearest qualifying band
                    bx, bs = x, s
                    for j in range(1, int(W / step)):
                        xx = x + side * j * step
                        ss = sum(a[2] for a in an if a[0] < xx + W and a[1] > xx)
                        if ss > bs: bx, bs = xx, ss
                    best = (bx, bx + W, bs); break
                x += side * step
            if not best: break
            chosen.append(best)
        bands += [(b[0], b[1]) for b in chosen]
    return bands

def run(name, fn, weeks):
    maps = {(p, m): fn(p, m) for p in S.SYM for m in weeks}
    t = S.score(maps)
    clean = 0; touched = 0
    for (p, m), b in maps.items():
        for r in S.judge_week(p, m, b)['bands']:
            if r['verdict'] in ('HELD', 'CONTAINS', 'BROKEN'):
                touched += 1; clean += r['verdict'] != 'BROKEN' and 'BROKEN' not in r['visits']
    print('%-40s acc %.3f hold1 %.3f clean %.3f extremes %.3f | HELD %3d CONT %2d BOUND %3d BROKEN %3d FLOAT %3d missed %3d bands %3d (%.1f/wk) wk>=90 %d/%d' % (
        name, t['accuracy'], t['precision_touched'], clean / max(1, touched), t['extreme_recall'], t['HELD'], t['CONTAINS'], t['BOUNDING'], t['BROKEN'], t['FLOATING'], t['missed'], t['bands'], t['bands'] / t['weeks'], t['weeks_at_90'], t['weeks']))

if __name__ == '__main__':
    weeks = S.VALID if len(sys.argv) > 1 and sys.argv[1] == 'VALID' else S.DEV
    for k in (0.20, 0.25, 0.30):
        run(f'anchors k{k} thr 2/3', lambda p, m, k=k: build(p, m, k=k), weeks)
    run('anchors k.25 thr 3/3', lambda p, m: build(p, m, thr_in=3.0), weeks)
    run('anchors k.25 thr 3/4', lambda p, m: build(p, m, thr_in=3.0, thr_out=4.0), weeks)
    run('anchors k.25 thr 4/4', lambda p, m: build(p, m, thr_in=4.0, thr_out=4.0), weeks)
    run('anchors k.25 thr 3/4 reach.7', lambda p, m: build(p, m, thr_in=3.0, thr_out=4.0, reach=0.7), weeks)
    run('anchors k.25 thr 3 one per side', lambda p, m: build(p, m, thr_in=3.0, n_side=1), weeks)
    run('anchors k.30 thr 3 one per side r.7', lambda p, m: build(p, m, k=0.30, thr_in=3.0, n_side=1, reach=0.7), weeks)
    run('anchors k.25 thr 3/4 m.25', lambda p, m: build(p, m, thr_in=3.0, thr_out=4.0, m=0.25), weeks)
