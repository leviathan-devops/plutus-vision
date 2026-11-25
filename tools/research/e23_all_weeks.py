import sys, os, re, collections
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import e1_pine as G, e2_shapes as E2, e3_setups as E3
res = collections.Counter(); dm = collections.Counter(); lines = []
for fn in sorted(os.listdir('/home/user/plutus-vision/sidecar/out')):
    m = fn[:-5]
    if not re.match(r'^2026-\d\d-\d\d$', m): continue
    for p in (sys.argv[1:] or ['DXY']):
        r = G.run(p, m)
        act = {a[0]: a for a in E2.actual(p, m)}
        hit = sum(1 for d in r['e2']['days'] if d['day'] in act and (d['shape'], d['dir']) == (act[d['day']][1], act[d['day']][2]))
        dirhit = sum(1 for d in r['e2']['days'] if d['day'] in act and d['dir'] != 'range' and d['dir'] == ('up' if act[d['day']][3]['close'] > act[d['day']][3]['open'] else 'down'))
        dirn = sum(1 for d in r['e2']['days'] if d['day'] in act and d['dir'] != 'range')
        dm['days'] += len(act); dm['shape+dir same'] += hit; dm['directional days'] += dirn; dm['direction right'] += dirhit
        ss = E3.simulate(p, m, r['e3'])
        for s in ss:
            k = 'TP' if s['result'] == 'TP' else 'SL' if s['result'] == 'SL' else 'not filled' if s['result'] == 'not filled' else 'open+' if '+' in s['result'] else 'open-'
            res[k] += 1
        lines.append(f"{p} {m} E2 {r['e2']['primary']:<34} same-day {hit}/5 | E3 " + ' '.join(f"{s['dir'][0]}{s['day']}:{s['result'].split()[0]}" for s in ss))
print('\n'.join(lines)); print(dict(dm)); print(dict(res))
