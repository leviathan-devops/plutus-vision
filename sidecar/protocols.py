#!/usr/bin/env python3
"""sidecar/protocols.py - canon Protocols D / E / F / G (P452:1278-1376, P452:1443-1446; P533:693 'Volatility Triggers'), as they stood at the week's anchor.

  D  US Treasury auctions  - source www.treasurydirect.gov (TA_WS JSON of the auction tables P452:1280 points at):
       latest 2Y / 5Y / 10Y note results closed before the anchor; 'If the Bid-to-Cover ratio is >= 2.6x, classify as a VOLATILITY TRIGGER' (P452:1443);
       the auctions of the forecast week that were ANNOUNCED before the anchor (close date + time only - their results are after the anchor and are not kept).
  E  NY Fed ON RRP         - markets.newyorkfed.org (the data behind www.newyorkfed.org/markets/desk-operations/reverse-repo): the last two operations dated before the
                              Monday; 'If contraction >= USD 50 Billion, classify as a VOLATILITY TRIGGER' (P452:1444).
  F  Economic calendar     - www.forexfactory.com answers automated requests with a Cloudflare challenge: NO DATA (L-32).
  G  EIA petroleum status  - source www.eia.gov: weekly U.S. crude oil stocks (WCESTUS1); 'Extract the weekly crude oil stock change. Calculate deviation against the
       previous week's print. If absolute deviation >= 5M barrels, classify as a VOLATILITY TRIGGER' (P452:1446); only prints RELEASED before the anchor
       (Wednesday 10:30 ET, or the alternate date of EIA's published release schedule); the forecast week's release slot.

Plain code, no model. Raw responses are cached under sidecar/raw/protocols/ so a re-run makes no request and reproduces the file byte for byte.
usage: sidecar/protocols.py --week YYYY-MM-DD   -> sidecar/out/protocols/<week>.json
"""
import argparse, datetime as dt, html, json, os, re, subprocess, sys
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'e1_tool'))
import e1_data as D                                            # noqa: E402  (boundary_ms = the temporal anchor)

NY = ZoneInfo('America/New_York')
RAW = os.path.join(ROOT, 'sidecar', 'raw', 'protocols')
OUT = os.path.join(ROOT, 'sidecar', 'out', 'protocols')
TD = 'https://www.treasurydirect.gov/TA_WS/securities/search?startDate={a}&endDate={b}&dateFieldName=competitiveAuctionCloseDate&format=json'
EIA_STOCKS = 'https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=WCESTUS1&f=W'
EIA_SCHED = 'https://www.eia.gov/petroleum/supply/weekly/schedule.php'
BTC_TRIGGER = 2.6          # P452:1443
EIA_TRIGGER_MB = 5.0       # P452:1446 (million barrels)
NOTE_TERMS = ('2-Year', '5-Year', '10-Year')   # P452:1443 '2Y, 5Y, and 10Y notes'; a reopening counts under its original term


def fetch(url, name):
    """cached GET (generic client name, no personal data in the request)"""
    os.makedirs(RAW, exist_ok=True)
    p = os.path.join(RAW, name)
    if not os.path.exists(p):
        r = subprocess.run(['curl', '-sS', '-m', '90', '-f', '-A', 'Mozilla/5.0 (compatible; data-harvest)', '-o', p, url], capture_output=True, text=True)
        if r.returncode != 0:
            if os.path.exists(p):
                os.remove(p)
            raise RuntimeError(f'fetch failed {url}: {r.stderr.strip()}')
    with open(p, encoding='utf-8', errors='replace') as f:
        return f.read()


def et(day, hhmm):
    """'2026-07-08', '01:00 PM' -> epoch ms of that New York time"""
    t = dt.datetime.strptime(hhmm.strip().upper(), '%I:%M %p').time()
    d = dt.date.fromisoformat(day[:10])
    return int(dt.datetime(d.year, d.month, d.day, t.hour, t.minute, tzinfo=NY).timestamp() * 1000)


def protocol_d(monday, anchor):
    m = dt.date.fromisoformat(monday)
    rows = json.loads(fetch(TD.format(a=m - dt.timedelta(days=70), b=m + dt.timedelta(days=4)), f'td_{monday}.json'))
    done = [r for r in rows if r.get('competitiveAuctionCloseDate') and r.get('competitiveAuctionCloseTime') and et(r['competitiveAuctionCloseDate'], r['competitiveAuctionCloseTime']) < anchor]
    latest = []
    for term in NOTE_TERMS:
        c = [r for r in done if r['securityType'] == 'Note' and r.get('floatingRate') != 'Yes' and (r.get('originalSecurityTerm') or r['securityTerm']) == term and r.get('bidToCoverRatio')]   # fixed-rate notes (an FRN is a 'Note' too)
        if not c:
            latest.append({'term': term, 'status': 'NO RECENT AUCTION DATA'})
            continue
        r = max(c, key=lambda r: et(r['competitiveAuctionCloseDate'], r['competitiveAuctionCloseTime']))
        btc = float(r['bidToCoverRatio'])
        latest.append({'term': term, 'security_term': r['securityTerm'], 'close_et': r['competitiveAuctionCloseDate'][:10] + ' ' + r['competitiveAuctionCloseTime'],
                       'bid_to_cover': btc, 'high_yield': r.get('highYield') or None, 'trigger': btc >= BTC_TRIGGER,
                       'source_url': 'https://www.treasurydirect.gov/auctions/announcements-data-results/', 'results_file': r.get('treasuryAuctionResultsPressReleaseFileName')})
    week = []
    for r in rows:
        cd = (r.get('competitiveAuctionCloseDate') or '')[:10]
        if not cd or not (m <= dt.date.fromisoformat(cd) <= m + dt.timedelta(days=4)):
            continue
        if not r.get('announcementDate') or dt.date.fromisoformat(r['announcementDate'][:10]) >= m:   # announced on the anchor Monday = after 02:00 New York
            continue
        if r['securityType'] not in ('Note', 'Bond', 'TIPS', 'FRN'):                                    # the coupon auctions; bills are weekly routine
            continue
        week.append({'type': 'FRN' if r.get('floatingRate') == 'Yes' else r['securityType'], 'term': r['securityTerm'], 'original_term': r.get('originalSecurityTerm'), 'close_et': cd + ' ' + r['competitiveAuctionCloseTime'],
                     'close_ms': et(cd, r['competitiveAuctionCloseTime']), 'announced': r['announcementDate'][:10]})
    week.sort(key=lambda x: x['close_ms'])
    return {'latest_notes': latest, 'week_auctions': week}


def eia_alternates():
    """EIA's published schedule: 'Data for the week ending | Alternate release date | Release day | Release time | Holiday'"""
    s = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', fetch(EIA_SCHED, 'eia_schedule.html'))))
    alt = {}
    for we, rd, tm in re.findall(r'([A-Z][a-z]+ \d{1,2}, \d{4}) ([A-Z][a-z]+ \d{1,2}, \d{4}) [A-Z][a-z]+day (\d{1,2}:\d{2} [ap])\.m\.', s):
        alt[dt.datetime.strptime(we, '%B %d, %Y').date()] = (dt.datetime.strptime(rd, '%B %d, %Y').date(), tm.upper() + 'M')
    return alt


def release(we, alt):
    """release instant of the print for the week ending `we` (a Friday): Wednesday 10:30 ET after it, or EIA's alternate date"""
    d, t = alt.get(we, (we + dt.timedelta(days=5), '10:30 AM'))
    return d, t, et(d.isoformat(), t)


RRP = 'https://markets.newyorkfed.org/api/rp/reverserepo/propositions/search.json?startDate={a}&endDate={b}'
RRP_TRIGGER_BN = 50.0      # P452:1444 'If contraction >= USD 50 Billion, classify as a VOLATILITY TRIGGER'


def protocol_e(monday, anchor):
    """P452:1444 'Extract the current session's Accepted Total. Compare against the preceding business day.' As of the anchor (Monday 02:00 New York) the current session is the last
    operation dated before the Monday (the Monday's own operation closes in the New York afternoon)"""
    m = dt.date.fromisoformat(monday)
    d = json.loads(fetch(RRP.format(a=m - dt.timedelta(days=14), b=m - dt.timedelta(days=1)), f'rrp_{monday}.json'))
    ops = sorted([o for o in d.get('repo', {}).get('operations', []) if o.get('operationDate') and o['operationDate'] < monday and o.get('totalAmtAccepted') is not None],
                 key=lambda o: o['operationDate'])
    out = {'source_url': 'https://www.newyorkfed.org/markets/desk-operations/reverse-repo'}
    if len(ops) < 2:
        out['status'] = 'NO DATA'
        return out
    cur, prev = ops[-1], ops[-2]
    a, b = cur['totalAmtAccepted'] / 1e9, prev['totalAmtAccepted'] / 1e9
    out.update(status='OK', current={'date': cur['operationDate'], 'accepted_bn': round(a, 3)}, previous={'date': prev['operationDate'], 'accepted_bn': round(b, 3)},
               change_bn=round(a - b, 3), trigger=(b - a) >= RRP_TRIGGER_BN)
    return out


def protocol_g(monday, anchor):
    t = fetch(EIA_STOCKS, 'eia_wcestus1.html')
    alt = eia_alternates()
    pts = []
    for row in re.findall(r'<tr>(.*?)</tr>', t, re.S):
        cells = [html.unescape(re.sub(r'<[^>]+>', '', c)).replace('\xa0', ' ').strip() for c in re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)]
        if not cells or not re.match(r'\d{4}-[A-Z][a-z]{2}$', cells[0]):
            continue
        yr = int(cells[0][:4])
        for md, v in zip(cells[1::2], cells[2::2]):
            if re.match(r'\d{2}/\d{2}$', md) and re.match(r'[\d,]+$', v):
                mo, dy = int(md[:2]), int(md[3:])
                y = yr - 1 if (cells[0].endswith('Jan') and mo == 12) else yr
                pts.append((dt.date(y, mo, dy), int(v.replace(',', ''))))
    pts.sort()
    known = [(we, v) for we, v in pts if release(we, alt)[2] < anchor]
    out = {'source_url': EIA_STOCKS, 'schedule_url': EIA_SCHED}
    if len(known) < 3:
        out['latest'] = 'NO DATA'
    else:
        (w0, v0), (w1, v1), (w2, v2) = known[-3:]
        ch, prev = (v2 - v1) / 1000.0, (v1 - v0) / 1000.0
        rd, rt, _ = release(w2, alt)
        out['latest'] = {'week_ending': w2.isoformat(), 'released_et': rd.isoformat() + ' ' + rt, 'stocks_kb': v2, 'change_mb': round(ch, 3),
                         'previous_change_mb': round(prev, 3), 'deviation_mb': round(ch - prev, 3), 'trigger': abs(ch - prev) >= EIA_TRIGGER_MB}
    m = dt.date.fromisoformat(monday)
    we = m - dt.timedelta(days=3)                                  # the forecast week's release reports the week that ended the Friday before it
    rd, rt, ms = release(we, alt)
    out['week_release'] = {'week_ending': we.isoformat(), 'release_et': rd.isoformat() + ' ' + rt, 'release_ms': ms,
                           'in_week': m <= rd <= m + dt.timedelta(days=4)}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--week', required=True)
    a = ap.parse_args()
    anchor = D.boundary_ms(a.week)
    res = {'week': a.week, 'anchor_ms': anchor,
           'D': protocol_d(a.week, anchor),
           'E': protocol_e(a.week, anchor),
           'F': {'status': 'NO DATA', 'why': 'www.forexfactory.com answers automated requests with a Cloudflare challenge'},
           'G': protocol_g(a.week, anchor)}
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, a.week + '.json')
    with open(p, 'w') as f:
        json.dump(res, f, indent=1, sort_keys=True)
    print(p)


if __name__ == '__main__':
    main()
