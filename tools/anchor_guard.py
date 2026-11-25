#!/usr/bin/env python3
"""anchor_guard.py - the mechanical guard of the two hard constraints on indicator/*.pine (engine files):

  A. TEMPORAL ANCHOR: a week's forecast may only read bars closed at or before the Monday anchor.
  B. NO HARDCODED VALUES: no price literal, no date literal, no per-week constant.

It is a static check (run by the git pre-commit hook, tools/git-hooks/pre-commit) plus, with --run, a run of the script
through the Pinebox engine that proves every drawn week reports asof <= anchor. Refusals are appended to
memory/anchor_guard.log. Exit 0 = clean, 1 = refused.

usage: tools/anchor_guard.py [--run] FILE.pine [FILE.pine ...]
The sealed V1 baseline (indicator/plutus-vision-v1.sealed.pine) and indicator/probes/ are not engine files and are skipped;
the sealed file is instead checked for its sha256.
"""
import datetime, hashlib, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEALED = 'indicator/plutus-vision-v1.sealed.pine'
SEALED_SHA = '0d20e8314ce992fc23e27f1b97fed76b981c84e78c647bbe6b3d6e1206517bd1'

# decimal literals the canon itself defines (ratios, weights, scores) - anything else with decimals is a suspect
CANON_DECIMALS = {
    '0.0', '0.5', '1.0', '1.5', '2.0', '3.0', '4.0', '5.0', '6.0', '14.0', '20.0', '50.0', '95.0',
    '0.236', '0.382', '0.618', '1.1',          # fib ratios, camarilla factor (SP:997-1008, V452:843-849)
    '0.4', '0.6',                              # close-position thresholds (SP:1223, V452:773)
}
FORBIDDEN = [
    (r'\brequest\s*\.', 'request.* (other-symbol / higher-timeframe data can leak the future and is dead in Pinebox)'),
    (r'\blookahead\b', 'lookahead'),
    (r'\[\s*-', 'negative history offset'),
    (r'\bbarstate\.isrealtime\b', 'barstate.isrealtime (behaviour must not differ between replay and live)'),
    (r'\btimestamp\s*\(\s*(?:"[^"]*"\s*,\s*)?20\d\d\b', 'timestamp() with a literal year (a hardcoded date)'),
    (r'\b20[2-3]\d\s*[-,]\s*\d{1,2}\s*[-,]\s*\d{1,2}\b', 'a literal calendar date'),
]
REQUIRED = [
    ('f_assertAnchor(asof, anchorTs)', 'the run-time anchor assertion call'),
    ('runtime.error("ANCHOR VIOLATION', 'the run-time anchor violation error'),
    ('time_close > anchorTs', 'the freeze condition (first bar that closes after the anchor)'),
]


def strip(line):
    """drop string literals and the trailing comment"""
    out, i, n, q = [], 0, len(line), None
    while i < n:
        c = line[i]
        if q:
            if c == '\\':
                i += 2
                continue
            if c == q:
                q = None
            i += 1
            continue
        if c in '"\'':
            q = c
            out.append('""')
            i += 1
            continue
        if c == '/' and i + 1 < n and line[i + 1] == '/':
            break
        out.append(c)
        i += 1
    return ''.join(out)


def check(path):
    bad = []
    src = open(path, encoding='utf-8').read()
    for needle, what in REQUIRED:
        if needle not in src:
            bad.append((0, f'missing {what}: `{needle}`'))
    for no, raw in enumerate(src.split('\n'), 1):
        line = strip(raw)
        if not line.strip():
            continue
        for rx, what in FORBIDDEN:
            if re.search(rx, line):
                bad.append((no, f'{what}: {raw.strip()[:110]}'))
        # history reads only at global scope (inside a block this engine returns x[0] - LS-09)
        if raw[:1] in ' \t' and re.search(r'[A-Za-z_][\w.]*\s*\[\s*[^\]\s][^\]]*\]', line):
            bad.append((no, f'history/index read `x[n]` inside a block (read history at global scope only): {raw.strip()[:110]}'))
        # numeric literals
        for m in re.finditer(r'(?<![\w.])(\d+\.\d+)(?![\w.])', line):
            lit = m.group(1)
            val = float(lit)
            dec = len(lit.split('.')[1])
            if lit in CANON_DECIMALS:
                continue
            if val >= 20 or dec >= 4 or (dec >= 3 and val >= 0.7):
                bad.append((no, f'price-like literal {lit}: {raw.strip()[:110]}'))
            else:
                bad.append((no, f'decimal literal {lit} is not in the canon allow-list (add it to CANON_DECIMALS with its citation, or derive it): {raw.strip()[:110]}'))
    return bad


def run_check(path):
    """every drawn week must report asof <= anchor (the script prints both in its audit label)"""
    bad = []
    probe = os.path.join(ROOT, 'tools', 'pine-probe.py')
    for pair, tf in (('DXY', '1H'), ('EURUSD', '4H')):
        dump = f'/tmp/anchor_guard_{pair}_{tf}.json'
        r = subprocess.run([sys.executable, probe, path, '--pair', pair, '--tf', tf, '--limit', '6000', '--show', '0',
                            '--inputs', '{"i_showAudit":true,"i_weeks":40}', '--dump', dump], capture_output=True, text=True)
        if r.returncode != 0:
            bad.append((0, f'engine run failed on {pair} {tf}: {(r.stdout + r.stderr).strip()[:300]}'))
            continue
        d = json.load(open(dump))
        labels = d.get('data', d)['model']['labels']
        weeks = 0
        for l in labels:
            m = re.match(r'asof (\S+ \S+) NY \| anchor (\S+ \S+)', l.get('text', ''))
            if m:
                weeks += 1
                if m.group(1) > m.group(2):
                    bad.append((0, f'{pair} {tf}: week anchored {m.group(2)} read data as of {m.group(1)}'))
        if weeks == 0:
            bad.append((0, f'{pair} {tf}: no week audit label found (cannot prove asof <= anchor)'))
        else:
            print(f'  run {pair} {tf}: {weeks} weeks checked')
    return bad


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    do_run = '--run' in sys.argv
    refused = False
    log = []
    for f in args:
        rel = os.path.relpath(os.path.abspath(f), ROOT)
        if rel == SEALED:
            sha = hashlib.sha256(open(f, 'rb').read()).hexdigest()
            if sha != SEALED_SHA:
                refused = True
                log.append(f'{rel}: the sealed V1 baseline was modified (sha {sha[:16]} != {SEALED_SHA[:16]})')
            continue
        if not rel.startswith('indicator/') or '/probes/' in rel or not rel.endswith('.pine'):
            continue
        bad = check(f)
        if do_run and not bad:
            bad += run_check(f)
        for no, msg in bad:
            refused = True
            log.append(f'{rel}:{no}: {msg}')
        if not bad:
            print(f'anchor_guard: {rel} clean' + (' (static + engine run)' if do_run else ' (static)'))
    if refused:
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        with open(os.path.join(ROOT, 'memory', 'anchor_guard.log'), 'a') as fh:
            for l in log:
                fh.write(f'{stamp} REFUSED {l}\n')
        print('anchor_guard: REFUSED', file=sys.stderr)
        for l in log:
            print('  ' + l, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
