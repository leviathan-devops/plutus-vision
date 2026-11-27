#!/usr/bin/env python3
"""leak_check.py [PAIR:MONDAY ...] - the temporal anchor, enforced mechanically on the Python tool (L-05; CLAUDE.md "Nothing after the anchor may feed a forecast"; G2 audit D-01).
1. STATIC: no module of the tool (e1_tool/*.py) may read bars except through e1_data.closed() and the helpers built on it - a call to D.bars( / bars( outside e1_data.py fails;
   no week literal ('20YY-MM-DD') may appear in an engine module.
2. RUNTIME: plutus.run() is executed twice for each PAIR:MONDAY - once on the full bar store, once on a bar store CUT at the anchor (every bar that had not closed by the
   anchor removed). The two Pine scripts must be byte-identical; any difference = something after the anchor fed the map.
Exit code 1 on any failure. Run by tools/git-hooks/pre-commit when e1_tool/*.py is staged."""
import sys, os, re, glob
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
TOOL = os.path.join(ROOT, 'e1_tool')
sys.path.insert(0, TOOL)
bad = []
for f in sorted(glob.glob(os.path.join(TOOL, '*.py'))):
    name = os.path.basename(f)
    src = open(f).read()
    if name != 'e1_data.py':
        for i, line in enumerate(src.splitlines(), 1):
            code = line.split('#')[0]
            if re.search(r'\bD\.bars\(|\bdata\.bars\(', code):
                bad.append(f'{name}:{i}: reads bars directly (use D.closed / D.daily / D.weekly / D.forming): {line.strip()[:100]}')
            if re.search(r"['\"]20\d\d-\d\d-\d\d['\"]", code):
                bad.append(f'{name}:{i}: week literal in tool code: {line.strip()[:100]}')
for b in bad:
    print('LEAK-STATIC', b)
import e1_data as D
weeks = [a.split(':') for a in sys.argv[1:]] or [['DXY', '2026-07-06']]
orig = D.bars
for pair, monday in weeks:
    import importlib, plutus
    D._cache.clear(); D.bars = orig; plutus._MEMO.clear()
    a = plutus.run(pair, monday)[3]
    b0 = D.boundary_ms(monday)

    def cut(p, tf, _o=orig, _b0=b0):
        return [x for x in _o(p, tf) if x['time'] + D.TFMS[tf] <= _b0]
    D._cache.clear(); D.bars = cut; plutus._MEMO.clear()
    b = plutus.run(pair, monday)[3]
    D.bars = orig; D._cache.clear()
    if a != b:
        la, lb = a.splitlines(), b.splitlines()
        first = next((i for i, (x, y) in enumerate(zip(la, lb)) if x != y), min(len(la), len(lb)))
        bad.append(f'{pair} {monday}: output changes when the bars after the anchor are removed (first difference at Pine line {first + 1})')
        print('LEAK-RUNTIME', bad[-1])
    else:
        print(f'leak_check {pair} {monday}: identical output with the bar store cut at the anchor ({len(la) if False else len(a.splitlines())} Pine lines)')
# 3. DAILY ANCHORING (L-47): each day's part of the daily output (its anchor price, its line segment, its confirmed and dropped orders) must be identical when the bar store is cut at
#    that day's anchor - nothing after a day's anchor may feed that day.
for pair, monday in weeks:
    import plutus
    D._cache.clear(); D.bars = orig; plutus._MEMO.clear()
    full = plutus.run(pair, monday, daily=True)[1]['daily']
    for i in range(1, 5):
        t_a = D.week_start_ms(monday) + i * 86400000 if plutus.DAY_CONFIRM == 'start' else D.day_anchor_ms(monday, i)

        def cut2(p, tf, _o=orig, _t=t_a):
            return [x for x in _o(p, tf) if x['time'] + D.TFMS[tf] <= _t]
        D._cache.clear(); D.bars = cut2; plutus._MEMO.clear()
        part = plutus.run(pair, monday, daily=True)[1]['daily']
        D.bars = orig; D._cache.clear(); plutus._MEMO.clear()
        for j in range(0, i + 1):
            if part[j] != full[j]:
                bad.append(f'{pair} {monday}: day {j} of the daily output changes when the bars after day {i}\'s anchor are removed')
                print('LEAK-DAILY', bad[-1])
    if not [b for b in bad if b.startswith(f'{pair} {monday}: day')]:
        print(f'leak_check {pair} {monday} daily: every day identical with the bar store cut at its anchor')
sys.exit(1 if bad else 0)
