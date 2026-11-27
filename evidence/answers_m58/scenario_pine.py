"""Illustration only (answers to the operator, M-58): builds one small Pine v6 script per stop-loss scenario - the entry zone, the zones behind it, the candidate stops, the TP and
what price did. Prices are the week's own numbers read from tools/research/stopscen.py output (this is an evidence script, not tool code)."""
import datetime as dt, sys, json
U = lambda s: int(dt.datetime.strptime(s, '%Y-%m-%d %H:%M').replace(tzinfo=dt.UTC).timestamp() * 1000)

def pine(title, w0, w1, boxes, lines, labels, fmt):
    o = ['//@version=6', f'indicator("{title}", overlay=true, max_boxes_count=60, max_labels_count=60, max_lines_count=60)', 'if barstate.islast']
    for t0, t1, top, bot, col, tr in boxes:
        o.append(f'    box.new({U(t0)}, {fmt % top}, {U(t1)}, {fmt % bot}, xloc=xloc.bar_time, bgcolor=color.new(color.rgb({col}), {tr}), border_color=color.new(color.rgb({col}), 30), border_width=1)')
    for t0, t1, p, col, sty, wd in lines:
        o.append(f'    line.new({U(t0)}, {fmt % p}, {U(t1)}, {fmt % p}, xloc=xloc.bar_time, color=color.rgb({col}), width={wd}, style=line.style_{sty})')
    xm = U(w0) + int(0.36 * (U(w1) - U(w0)))       # the backtest chart centres a label on its point: one column of labels left of the middle, on a dark background
    for lb in labels:
        t, p, txt, col, sz = lb[:5]
        x_ = U(w0) + int(lb[5] * (U(w1) - U(w0))) if len(lb) > 5 else xm
        o.append(f'    label.new({x_}, {fmt % p}, "{txt}", xloc=xloc.bar_time, style=label.style_label_center, color=color.new(color.rgb(15,17,22), 15), textcolor=color.rgb({col}), size=size.{sz})')
    return '\n'.join(o) + '\n'

SC = {}
# S1 - DXY week 2026-05-18, Monday range-floor long (code DX1)
w0, w1 = '2026-05-18 06:00', '2026-05-19 12:00'; L = '2026-05-18 06:30'; R_ = '2026-05-18 23:30'
SC['s1'] = ('S1 DXY May18 floor long', 'DXY', '2026-05-15', '2026-05-22', '2026-05-18', '2026-05-19T12:00', w0, w1, '%.3f',
  [(w0, w1, 99.097, 99.001, '33,150,243', 82), (w0, w1, 99.050, 98.996, '46,139,87', 80), (w0, w1, 98.939, 98.885, '46,139,87', 70), (w0, w1, 98.944, 98.844, '0,230,118', 88)],
  [(w0, w1, 99.050, '255,255,255', 'dashed', 1), (w0, w1, 98.971, '242,54,69', 'solid', 2), (w0, w1, 98.929, '255,152,0', 'solid', 2), (w0, w1, 99.294, '8,153,129', 'solid', 2), (w0, w1, 98.944, '200,200,200', 'dotted', 1)],
  [(L, 99.103, 'ENTRY ZONE: 1H demand 99.001-99.097 (anchor)', '120,170,255', 'small'), (L, 99.056, 'ENTRY 99.050 = top of 4H band 98.996-99.050 + 1H rung', '255,255,255', 'small'),
   (L, 98.977, 'A (code): SL 98.971 = 3p outside the entry zone - STOPPED Mon 16:15', '255,110,110', 'small'),
   (L, 98.951, 'price low 98.944 (Mon 22:00) = top edge of the daily sweep zone', '220,220,220', 'small'),
   (L, 98.922, 'B: SL 98.929 = 1p inside the next THICK 4H band 98.885-98.939 - survives, TP Tue 10:30, RRR 2.02', '255,170,60', 'small'),
   (L, 98.874, 'daily sweep zone 98.844-98.944 (prior day low 98.844)', '0,230,118', 'small'),
   (L, 99.300, 'TP 99.294 (code: near edge of the sweep-zone ceiling) - price went on to 99.515 Thu', '80,220,170', 'small')])
# S2 - EURUSD week 2026-07-06 (golden week), Monday range-ceiling short (code EU2)
w0, w1 = '2026-07-06 12:00', '2026-07-07 22:00'; L = '2026-07-06 12:30'
SC['s2'] = ('S2 EURUSD Jul06 ceiling short', 'EURUSD', '2026-07-03', '2026-07-10', '2026-07-06', '2026-07-07T22:00', w0, w1, '%.5f',
  [(w0, w1, 1.14421, 1.14375, '242,54,69', 82), (w0, w1, 1.14446, 1.14428, '46,139,87', 80), (w0, w1, 1.14623, 1.14523, '0,230,118', 88), (w0, w1, 1.14728, 1.14658, '46,139,87', 70)],
  [(w0, w1, 1.14385, '255,255,255', 'dashed', 1), (w0, w1, 1.14451, '242,54,69', 'solid', 2), (w0, w1, 1.14533, '255,152,0', 'solid', 2), (w0, w1, 1.14068, '8,153,129', 'solid', 2), (w0, w1, 1.14480, '200,200,200', 'dotted', 1)],
  [(L, 1.14367, 'ENTRY 1.14385 (30m order block bottom + 1p) - ENTRY ZONE: 1H BoM supply 1.14375-1.14421', '255,255,255', 'small'),
   (L, 1.14457, 'A (code): SL 1.14451 = 3p outside the step - STOPPED Mon 21:45', '255,110,110', 'small'),
   (L, 1.14487, 'price high 1.14480 before the drop (9.5p against the entry)', '220,220,220', 'small'),
   (L, 1.14540, 'B: SL 1.14533 = 1p inside the sweep zone 1.14523-1.14623 - survives, TP Tue 21:15, RRR 2.14', '255,170,60', 'small'),
   (L, 1.14735, '4H band 1.14658-1.14728 (B on it: SL 1.14668, RRR 1.12)', '120,200,140', 'small'),
   (L, 1.14060, 'TP 1.14068', '80,220,170', 'small')])
# S3 - EURUSD week 2026-10-05, Tuesday range-ceiling short (code EU2)
w0, w1 = '2026-10-06 06:00', '2026-10-07 14:00'; L = '2026-10-06 06:30'
SC['s3'] = ('S3 EURUSD Oct05 ceiling short', 'EURUSD', '2026-10-02', '2026-10-09', '2026-10-06', '2026-10-07T14:00', w0, w1, '%.5f',
  [(w0, w1, 1.12612, 1.12491, '242,54,69', 84), (w0, w1, 1.12652, 1.12603, '46,139,87', 80), (w0, w1, 1.12853, 1.12753, '0,230,118', 88)],
  [(w0, w1, 1.12585, '255,255,255', 'dashed', 1), (w0, w1, 1.12742, '242,54,69', 'solid', 2), (w0, w1, 1.12773, '255,152,0', 'solid', 2), (w0, w1, 1.12632, '255,110,110', 'dotted', 1), (w0, w1, 1.12767, '200,200,200', 'dotted', 1), (w0, w1, 1.11725, '8,153,129', 'solid', 2)],
  [(L, 1.12470, 'ENTRY 1.12585 (white dashed) - ENTRY ZONE: 1H MoM supply 1.12491-1.12612 (red box)', '255,255,255', 'small', 0.62),
   (L, 1.12655, 'A (2-3p outside the entry zone): SL 1.12632-1.12642 - STOPPED Tue 11:15', '255,110,110', 'small', 0.62),
   (L, 1.12715, 'code: SL 1.12742 = 3p outside the extended sweep range - STOPPED Tue 12:00 (high 1.12767)', '255,110,110', 'small', 0.62),
   (L, 1.12835, 'B: SL 1.12773 = 2p inside the sweep zone 1.12753-1.12853 - survives by 0.6p, TP Wed 12:15, RRR 4.57', '255,170,60', 'small', 0.62),
   (L, 1.11745, 'TP 1.11725 (hit Wed 12:15)', '80,220,170', 'small', 0.40)])
k = sys.argv[1]
t = SC[k]
open(f'/home/user/plutus-vision/evidence/answers_m58/{k}.pine', 'w').write(pine(t[0], t[6], t[7], t[9], t[10], t[11], t[8]))
print(json.dumps({'title': t[0], 'pair': t[1], 'bt_start': t[2] + 'T20:00', 'bt_end': t[3] + 'T20:00', 'date': t[4], 'step_to': t[5], 'w0': t[6], 'w1': t[7]}))
