"""asiasweep.py - scratch LOCATOR: at each London open, a sell limit k pips above the Asian high and a buy limit k pips below the Asian low (the session's liquidity pools,
P452 6.6 rule 2 / LSZ 'brief breach then reversal'), SL s pips beyond the entry, TP = the opposite Asian extreme (or rr x SL). Orders live 02:00-12:00 NY; OCO (the first fill
cancels the other). Weeks: all 2026 sidecar weeks to 10-26 except the held-out four; or --weeks dev."""
import sys, glob, os, argparse
sys.path.insert(0, '/home/user/plutus-vision/e1_tool')
import e1_data as D
ap = argparse.ArgumentParser(); ap.add_argument('--k', type=float, default=3); ap.add_argument('--s', type=float, default=10); ap.add_argument('--rr', type=float, default=0)
ap.add_argument('--weeks', default='all'); ap.add_argument('--life', type=int, default=10)
A = ap.parse_args()
H = 3600000
held = {'2026-03-30', '2026-05-25', '2026-07-13', '2026-09-28'}
dev = ['2026-03-02', '2026-03-23', '2026-04-13', '2026-04-20', '2026-05-18', '2026-08-31', '2026-09-21', '2026-10-05']
weeks = dev if A.weeks == 'dev' else [w for w in sorted(os.path.basename(f)[:-5] for f in glob.glob('/home/user/plutus-vision/sidecar/out/2026-*.json')) if w not in held and w <= '2026-10-26']
tot = {}
for pair in ('DXY', 'EURUSD', 'GBPUSD'):
    pip = D.PIP[pair]; b15 = D.bars(pair, '15')
    t = tot.setdefault(pair, [0, 0, 0, 0])
    for w in weeks:
        for i in range(5):
            tL = D.day_anchor_ms(w, i); ta = tL - 9 * H
            asia = [b for b in b15 if ta <= b['time'] < tL]
            day = [b for b in b15 if tL <= b['time'] < tL + 5 * 24 * H]
            if len(asia) < 20 or not day: continue
            ah, al = max(b['high'] for b in asia), min(b['low'] for b in asia)
            R = ah - al
            es, el = ah + A.k * pip, al - A.k * pip
            o = [('S', es, es + A.s * pip, (es - A.rr * A.s * pip) if A.rr else al + 1.5 * pip), ('L', el, el - A.s * pip, (el + A.rr * A.s * pip) if A.rr else ah - 1.5 * pip)]
            f = None
            for b in day:
                if f is None:
                    if b['time'] >= tL + A.life * H: break
                    hs, hl = b['high'] >= es, b['low'] <= el
                    if hs and hl: f = None; break                    # both in one candle: skip (ambiguous)
                    if hs: f = o[0]
                    elif hl: f = o[1]
                    else: continue
                side, e, sl, tp = f
                if (b['high'] >= sl) if side == 'S' else (b['low'] <= sl): r = 'SL'; break
                if (b['low'] <= tp) if side == 'S' else (b['high'] >= tp): r = 'TP'; break
            else:
                r = 'OPEN' if f else None
            if f is None: continue
            t[0] += 1; t[1] += r == 'TP'; t[2] += r == 'SL'; t[3] += abs(f[3] - f[1]) / abs(f[1] - f[2])
for pair, (n, tp, sl, rrs) in tot.items():
    print(f"{pair:<7} k {A.k} s {A.s} rr {A.rr or 'asia'}: trades {n:3d}  TP {tp:3d}  SL {sl:3d}  win {100 * tp / max(1, tp + sl):5.1f}%  avg RR {rrs / max(1, n):.2f}")
n = sum(v[0] for v in tot.values()); tp = sum(v[1] for v in tot.values()); sl = sum(v[2] for v in tot.values())
print(f"ALL     trades {n} TP {tp} SL {sl} win {100 * tp / max(1, tp + sl):.1f}%")
