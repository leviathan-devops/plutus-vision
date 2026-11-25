"""proto.py - E1 v2 band-map prototypes (design research; DEV/VALID only). usage: python3 proto.py [DEV|VALID]"""
import sys, score as S
LV = {p: {w['week']: w for w in S.levels(p)} for p in S.SYM}

def window_scores(w, A, W, wt):
    """density of evidence in every window [x, x+W] on a grid of 0.02*A"""
    sp = w['spot']; step = 0.02 * A; out = []
    x = sp - 1.6 * A
    while x < sp + 1.6 * A:
        s = sum(wt(l) for l in w['levels'] if x <= l['p'] <= x + W)
        s += sum(1.5 for z in w['sd'] if z['mit'] <= 2 and z['bot'] < x + W and z['top'] > x and z['top'] - z['bot'] <= 0.5 * A)
        out.append((x, s)); x += step
    return out

def density_map(pair, mon, k=0.20, m=0.10, g=0.15, reach=1.0, n_side=2, wt=lambda l: l['w'], pick='best'):
    w = LV[pair][mon]; A = S.awr(pair, mon); sp = w['spot']; W = k * A
    ws = window_scores(w, A, W, wt); bands = []
    for side in (1, -1):
        chosen = []
        for _ in range(n_side):
            cand = []
            for x, s in ws:
                bot, top = x, x + W
                if side > 0 and not (bot >= sp + m * A and top <= sp + reach * A): continue
                if side < 0 and not (top <= sp - m * A and bot >= sp - reach * A): continue
                if any(bot < c[1] + g * A and top > c[0] - g * A for c in chosen): continue
                cand.append((s, -abs((bot + top) / 2 - sp) if pick == 'best' else 0, bot, top))
            if not cand: break
            if pick == 'near':   # nearest window whose density is at least 70% of the best available
                mx = max(c[0] for c in cand)
                cand = [c for c in cand if c[0] >= 0.7 * mx]
                c = min(cand, key=lambda c: abs((c[2] + c[3]) / 2 - sp))
            else:
                c = max(cand)
            chosen.append((c[2], c[3]))
        bands += chosen
    return bands

def geo_map(pair, mon, k=0.20, d1=0.35, d2=0.8):
    A = S.awr(pair, mon); sp = S.spot(pair, mon); W = k * A
    return [(sp + d * A - W / 2, sp + d * A + W / 2) for d in (d1, d2, -d1, -d2)]

def run(name, fn, weeks):
    maps = {(p, m): fn(p, m) for p in S.SYM for m in weeks}
    t = S.score(maps)
    print('%-34s acc %.3f  hold|touch %.3f  extremes %.3f  HELD %3d CONT %2d BOUND %3d BROKEN %3d FLOAT %3d missed %3d  bands %3d  wk>=90 %d/%d' % (
        name, t['accuracy'], t['precision_touched'], t['extreme_recall'], t['HELD'], t['CONTAINS'], t['BOUNDING'], t['BROKEN'], t['FLOATING'], t['missed'], t['bands'], t['weeks_at_90'], t['weeks']))
    return t

if __name__ == '__main__':
    weeks = S.VALID if len(sys.argv) > 1 and sys.argv[1] == 'VALID' else S.DEV
    run('geometry only k.20 d.35/.80', geo_map, weeks)
    run('geometry only k.30 d.35/.80', lambda p, m: geo_map(p, m, k=0.30), weeks)
    for k in (0.15, 0.20, 0.30):
        for pick in ('best', 'near'):
            run(f'density k{k} m.10 g.15 {pick}', lambda p, m, k=k, pick=pick: density_map(p, m, k=k, pick=pick), weeks)
    run('density k.20 reach.7 near', lambda p, m: density_map(p, m, reach=0.7, pick='near'), weeks)
    run('density k.30 reach.7 near', lambda p, m: density_map(p, m, k=0.30, reach=0.7, pick='near'), weeks)
    run('density k.30 reach.7 best', lambda p, m: density_map(p, m, k=0.30, reach=0.7), weeks)
