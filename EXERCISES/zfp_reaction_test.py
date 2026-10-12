import sys, json
sys.path.insert(0,"EXERCISES")
import lab
from lab import (load, aggregate, find_swings, repeated_magnets, find_order_blocks,
                 cluster_zones, zfp_geometric, week_bounds, to_dt, REF_RANGE)

weeks=["2026-04-20","2026-05-04","2026-06-15","2026-06-29","2026-07-06","2026-08-24"]
prov,cells = load(lab.BARS/"pv-long.json")
pair,tf,bars = next(c for c in cells if c[1]=="1H")
K = 12  # 12 x 1H = half a trading day — the "immediate reaction window"

print("="*110)
print("EMPIRICAL TEST v2 — does the GEOMETRIC ZFP predict the IMMEDIATE REACTION at the touch?")
print("The first test measured the WEEK-LONG outcome, which is the wrong quantity: the canon says a")
print("zone REACTS on first test and only fails after ~3 reactions. So we measure the reaction in")
print("the K=12 bars (~half a day) after the FIRST touch, not the week's final state.")
print("="*110)
rows=[]
for w in weeks:
    mon,fri = week_bounds(bars,w)
    pre=[b for b in bars if to_dt(b["timestamp"])<mon]
    wk =[b for b in bars if mon<=to_dt(b["timestamp"])<=fri]
    sw  = find_swings(aggregate(pre,1440), REF_RANGE[pair])
    mags= repeated_magnets(sw); obs=find_order_blocks(aggregate(pre,240), REF_RANGE[pair])
    lv  = ([l["price"] for l in sw["lows"]]+[h["price"] for h in sw["highs"]]
           +[m["price"] for m in mags]+[o["low"] for o in obs]+[o["high"] for o in obs])
    for z in cluster_zones(lv):
        if z["n"]<2: continue
        zc=zfp_geometric(z["low"],z["high"],pair)
        touch_i=None
        for i,b in enumerate(wk):
            if b["low"]<=z["high"] and b["high"]>=z["low"] and i>=1:
                touch_i=i; break
        if touch_i is None: continue
        prev=[b for b in wk[:touch_i]]
        side = "above" if (prev and prev[-1]["close"]>z["high"]) else "below"
        win = wk[touch_i:touch_i+K+1]
        through = any((b["close"]<z["low"] if side=="above" else b["close"]>z["high"]) for b in win)
        # reaction = price returned OUT of the zone on the entry side before closing through
        back = False
        for b in win:
            if side=="above" and b["close"]>z["high"]: back=True; break
            if side=="below" and b["close"]<z["low"]:  back=True; break
        verdict = "PIERCED" if through and not back else ("REACTED" if back else "INSIDE")
        rows.append({"week":w,"zone":f'{z["low"]:.3f}-{z["high"]:.3f}',"n":z["n"],"zfp":zc,
                     "side":side,"verdict":verdict,"week_range":round(fri.month*1.0,0)})
print(f"\n{'ZFP BAND':18s} {'TOUCHES':>8s} {'REACTED':>8s} {'PIERCED':>8s} {'INSIDE':>7s} {'REACT%':>8s}")
print("-"*62)
def rep(lbl,f):
    sub=[r for r in rows if f(r["zfp"])]
    if not sub: print(f"{lbl:18s} {0:>8d} {'-':>8s} {'-':>8s} {'-':>7s} {'n/a':>8s}"); return
    a=sum(1 for r in sub if r["verdict"]=="REACTED"); p=sum(1 for r in sub if r["verdict"]=="PIERCED")
    ins=len(sub)-a-p
    print(f"{lbl:18s} {len(sub):>8d} {a:>8d} {p:>8d} {ins:>7d} {100*a/len(sub):>7.1f}%")
rep("HARD WALL  <20%", lambda z: z<20)
rep("MID 20-40%",      lambda z: 20<=z<40)
rep("SOFT/FAIL >=40%", lambda z: z>=40)
print("-"*62)
print(f"{'TOTAL':18s} {len(rows):>8d} {sum(1 for r in rows if r['verdict']=='REACTED'):>8d} "
      f"{sum(1 for r in rows if r['verdict']=='PIERCED'):>8d} "
      f"{sum(1 for r in rows if r['verdict']=='INSIDE'):>7d}")
print("\nDETAIL:")
for r in rows:
    print(f"  {r['week']}  {r['zone']:16s} n={r['n']:2d} ZFP={r['zfp']:3d}% from {r['side']:5s} -> {r['verdict']}")
json.dump(rows, open("EXERCISES/zfp_reaction_test.json","w"), indent=2)
print(f"\nn={len(rows)} touches across {len(weeks)} weeks.")
