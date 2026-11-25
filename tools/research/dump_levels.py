#!/usr/bin/env python3
"""dump_levels.py - regenerate tools/research/levels.{DXY,EURUSD,GBPUSD}.json (git-ignored) from the Pinebox engine.

DESIGN RESEARCH INPUT ONLY (never a gate). Runs indicator/plutus-vision-engines.pine through the station (tools/pine-probe.py)
on 4H bars with the audit label on, and converts each week's audit text into JSON:
  {pair, week, anchor_ny, asof_ny, spot, levels[{p,src,tag,w,st,bonus,lo,hi,conf,tech,stru,psy,opt,ana,xb,code,optc}],
   sd[{side,bot,top,mit,scale,origin_ny}], cur_zones[{bot,top,name,degree,score,zfp,drivers}]}
Needs Pinebox up (tools/pinebox-bootstrap.sh) and sidecar/out/pine_inputs.*.txt.
usage: python3 tools/research/dump_levels.py
"""
import json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'tools', 'research')
KEYS = ['p', 'src', 'tag', 'w', 'st', 'bonus', 'lo', 'hi', 'conf', 'tech', 'stru', 'psy', 'opt', 'ana', 'xb', 'code', 'optc']


def read(p):
    return open(p).read().strip() if os.path.exists(p) else ''


for pair in ('DXY', 'EURUSD', 'GBPUSD'):
    inputs = {'i_back': 0, 'i_weeks': 60, 'i_showAudit': True, 'i_showE1': False,
              'i_optData': read(f'{ROOT}/sidecar/out/pine_inputs.{pair}.txt'),
              'i_anaData': read(f'{ROOT}/sidecar/out/pine_inputs.analyst.{pair}.txt')}
    raw = f'/tmp/dump_levels_{pair}.json'
    r = subprocess.run([sys.executable, f'{ROOT}/tools/pine-probe.py', f'{ROOT}/indicator/plutus-vision-engines.pine', '--pair', pair,
                        '--tf', '4H', '--limit', '3000', '--show', '0', '--inputs', json.dumps(inputs), '--dump', raw],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(pair, 'probe failed:', (r.stdout + r.stderr)[-400:])
        continue
    d = json.load(open(raw))
    weeks = []
    for l in d.get('data', d)['model']['labels']:
        t = l.get('text', '')
        m = re.search(r'asof (\S+ \S+) NY \| anchor (\S+) (\S+) \| spot (\S+) \| levels (\d+)', t)
        if not m:
            continue
        w = {'pair': pair, 'week': m.group(2), 'anchor_ny': m.group(2) + ' ' + m.group(3), 'asof_ny': m.group(1),
             'spot': float(m.group(4)), 'levels': [], 'sd': [], 'cur_zones': []}
        for ln in t.split('\n'):
            if ln.startswith('L '):
                o = {}
                for k, v in zip(KEYS, ln[2:].split('|')):
                    o[k] = v if k == 'tag' else (float(v) if v not in ('NaN', 'na') else None)
                w['levels'].append(o)
            elif ln.startswith('SD '):
                mm = re.match(r'SD (supply|demand) ([\d.]+)-([\d.]+) mit(\d+) (\d+) (.*)', ln)
                if mm:
                    w['sd'].append({'side': mm.group(1), 'bot': float(mm.group(2)), 'top': float(mm.group(3)), 'mit': int(mm.group(4)),
                                    'scale': int(mm.group(5)), 'origin_ny': mm.group(6)})
            elif ln.startswith('Z '):
                mm = re.match(r'Z ([\d.]+)-([\d.]+) (.*?) (EXTREME|HEAVY|MODERATE-HEAVY|MODERATE|LIGHT|MINIMAL) ([\d.]+) cf([\d.]+) p(\d) T(\d) zfp(\d+) (\d+)R(\d+)X \[(.*)\]', ln)
                if mm:
                    w['cur_zones'].append({'bot': float(mm.group(1)), 'top': float(mm.group(2)), 'name': mm.group(3), 'degree': mm.group(4),
                                           'score': float(mm.group(5)), 'zfp': int(mm.group(9)), 'drivers': mm.group(12)})
        weeks.append(w)
    weeks = [w for w in weeks if w['week'] >= '2026-02-02']
    json.dump(weeks, open(f'{OUT}/levels.{pair}.json', 'w'))
    print(pair, len(weeks), 'weeks', weeks[0]['week'], '->', weeks[-1]['week'])
