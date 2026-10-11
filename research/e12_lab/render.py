import pandas as pd, numpy as np
from lab import *
DEG_COL={"EXTREME":"#ff4d4d","HEAVY":"#ff8a3d","MODERATE-HEAVY":"#e0b341","MODERATE":"#5aa9e6","LIGHT":"#7a8794","MINIMAL":"#4a525c"}
def render_e1(E, monday, fn, show_week=True, min_deg=("EXTREME","HEAVY","MODERATE-HEAVY","MODERATE"), forecast=None, days=35, title_extra=""):
    h4=E['h4']; a=E['anchor']
    hist=h4[h4.index>a-pd.Timedelta(days=days)]
    fig,ax=plt.subplots(figsize=(21,9)); style_dark(fig,ax)
    full=hist
    if show_week:
        from lab import resample
        wk=week_slice(E['h4_full'],monday); full=pd.concat([hist,wk[wk.index>hist.index[-1]]])
    candles(ax,full); idx=full.index
    ax.axvline(xpos(idx,a),color='#ffd166',lw=1.2,ls='--',zorder=5); ax.text(xpos(idx,a)+0.3,full.high.max(),' ANCHOR',color='#ffd166',fontsize=8,va='top')
    for dday in range(5):
        t=pd.Timestamp(monday)+pd.Timedelta(days=dday)-pd.Timedelta(hours=7)
        if t>idx[0]: ax.axvline(xpos(idx,t),color='#2d333b',lw=0.7,ls=':',zorder=0)
    t0=hist.index[0]; t1=None
    for z in E['ips']:
        if z.degree in min_deg:
            draw_zone(ax,idx,z.lo,z.hi,t0,t1,DEG_COL[z.degree],alpha=0.16 if z.degree!='EXTREME' else 0.28,label=f"{z.degree[:3]} {z.score:.1f}")
    for z in E['lsz']:
        if z.tf=="D1" and not z.touches:
            draw_zone(ax,idx,z.lo,z.hi,z.formed,None,"#3ddc84",alpha=0.35 if z.state=="ACTIVE" else 0.18,label=("LSZ"+("*" if z.state=="ACTIVE" else "")),fs=6)
    for z in E['sd']:
        if z.state!="BROKEN":
            draw_zone(ax,idx,z.lo,z.hi,z.formed,None,"#ff7a1a" if z.side=="supply" else "#1aa7ff",alpha=0.45,lw=1.4,ls='--',
                      label=f"{z.cls} {z.side[:3]} {z.state}")
    if forecast: forecast(ax,idx,E)
    ymin=min(full.low.min(),E['spot']-3*E['adr']); ymax=max(full.high.max(),E['spot']+3*E['adr'])
    pad=0.15*(full.high.max()-full.low.min())
    ax.set_ylim(full.low.min()-0.1*pad, full.high.max()+0.1*pad); ax.set_xlim(-1,len(idx)+8)
    time_axis(ax,idx,every=12)
    ax.set_title(f"EURUSD wk {monday.date()}  spot={E['spot']:.4f} ADR={E['adr']/PIP:.0f}p  | red/orange/yellow/blue=IP pressure, green=LSZ(*=wick), dashed orange=supply S/D, dashed blue=demand S/D {title_extra}",color='#e8e8e8',fontsize=9)
    fig.tight_layout(); fig.savefig(fn,dpi=75); plt.close(fig)
