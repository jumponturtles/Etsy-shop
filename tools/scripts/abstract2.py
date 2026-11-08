"""Dense abstract coloring pages. abstract2.py STYLE SEED OUT.png"""
import sys, math
import numpy as np, cairo
from shapely.geometry import Polygon, Point, LineString, box
from shapely.ops import unary_union
from scipy.spatial import Voronoi
sys.path.insert(0,'/home/claude/scripts')
from abstract import ctx, stroke, FRAME, W, H, M, voronoi_regions
def lines_at(r,step,ang):
    x0,y0,x1,y1=r.bounds; cx,cy=(x0+x1)/2,(y0+y1)/2; L=math.hypot(x1-x0,y1-y0); out=[]; d=-L/2
    while d<L/2:
        ox,oy=cx+d*math.cos(ang+math.pi/2),cy+d*math.sin(ang+math.pi/2)
        out.append(LineString([(ox-L*math.cos(ang),oy-L*math.sin(ang)),(ox+L*math.cos(ang),oy+L*math.sin(ang))]).intersection(r)); d+=step
    return out
def F_hatch(r,g): return lines_at(r,g.uniform(14,24),g.uniform(0,math.pi))
def F_cross(r,g): a=g.uniform(0,math.pi); s=g.uniform(22,34); return lines_at(r,s,a)+lines_at(r,s,a+math.pi/2)
def F_conc(r,g):
    out=[]; q=r; s=g.uniform(13,22)
    for _ in range(120):
        q=q.buffer(-s,join_style=1)
        if q.is_empty or q.area<80: break
        out.append(q.boundary)
    return out
def F_dots(r,g):
    s=g.uniform(30,48); rad=g.uniform(.25,.36)*s; x0,y0,x1,y1=r.bounds; out=[]; row=0; y=y0
    while y<y1:
        x=x0+(s/2 if row%2 else 0)
        while x<x1:
            c=Point(x,y).buffer(rad,14)
            if r.contains(c): out.append(c.boundary)
            x+=s
        y+=s*.87; row+=1
    return out
def F_scales(r,g):
    s=g.uniform(36,60); x0,y0,x1,y1=r.bounds; out=[]; row=0; y=y0-s
    while y<y1+s:
        x=x0-s+(s/2 if row%2 else 0)
        while x<x1+s:
            for k in (1,.6):
                out.append(LineString([(x+k*s/2*math.cos(t),y+k*s/2*math.sin(t)) for t in np.linspace(0,math.pi,20)]).intersection(r))
            x+=s
        y+=s/2.3; row+=1
    return out
def F_waves(r,g):
    s=g.uniform(16,26); amp=g.uniform(8,22); wl=g.uniform(60,150); ang=g.uniform(0,math.pi); x0,y0,x1,y1=r.bounds
    cx,cy=(x0+x1)/2,(y0+y1)/2; L=math.hypot(x1-x0,y1-y0); out=[]; d=-L/2; ca,sa=math.cos(ang),math.sin(ang)
    while d<L/2:
        t=np.linspace(-L/2,L/2,260); u=t; v=d+amp*np.sin(t/wl*2*math.pi)
        out.append(LineString(list(zip(cx+u*ca-v*sa,cy+u*sa+v*ca))).intersection(r)); d+=s
    return out
def F_pebbles(r,g):
    n=max(6,int(r.area/g.uniform(4000,9000)))
    regs=voronoi_regions(g,min(n,140),r) if r.geom_type=='Polygon' else []
    return [q.buffer(-5,join_style=1).boundary for q in regs if not q.buffer(-5).is_empty]
def F_chevron(r,g):
    s=g.uniform(20,32); w=g.uniform(40,80); x0,y0,x1,y1=r.bounds; out=[]; y=y0-w
    while y<y1+w:
        pts=[]; x=x0-w; k=0
        while x<x1+w: pts.append((x,y+(w*.5 if k%2 else 0))); x+=w; k+=1
        out.append(LineString(pts).intersection(r)); y+=s
    return out
def F_bricks(r,g):
    h=g.uniform(30,46); w=h*g.uniform(1.6,2.4); x0,y0,x1,y1=r.bounds; out=[]; row=0; y=y0
    while y<y1:
        out.append(LineString([(x0,y),(x1,y)]).intersection(r)); x=x0+(w/2 if row%2 else 0)
        while x<x1: out.append(LineString([(x,y),(x,y+h)]).intersection(r)); x+=w
        y+=h; row+=1
    return out
def F_orbs(r,g):
    out=[]; placed=[]
    for _ in range(900):
        p=Point(g.uniform(*r.bounds[0::2]),g.uniform(*r.bounds[1::2])); rad=g.uniform(14,60); c=p.buffer(rad,24)
        if r.contains(c) and all(c.distance(q)>6 for q in placed):
            placed.append(c); out.append(c.boundary)
            if rad>28: out.append(p.buffer(rad*.55,20).boundary)
    return out
def F_petals(r,g):
    out=[]; s=g.uniform(70,110); x0,y0,x1,y1=r.bounds
    for x in np.arange(x0,x1+s,s):
        for y in np.arange(y0,y1+s,s*.87):
            xx=x+(s/2 if int((y-y0)/(s*.87))%2 else 0)
            for k in range(6):
                a=k*math.pi/3; pts=[(xx+ s*.42*t*math.cos(a)-s*.12*math.sin(math.pi*t)*math.sin(a), y+s*.42*t*math.sin(a)+s*.12*math.sin(math.pi*t)*math.cos(a)) for t in np.linspace(0,1,12)]
                pts+=[(xx+ s*.42*t*math.cos(a)+s*.12*math.sin(math.pi*t)*math.sin(a), y+s*.42*t*math.sin(a)-s*.12*math.sin(math.pi*t)*math.cos(a)) for t in np.linspace(1,0,12)]
                out.append(LineString(pts).intersection(r))
            out.append(Point(xx,y).buffer(s*.08,12).boundary.intersection(r))
    return out
def F_spiral(r,g):
    c=r.representative_point(); R=math.sqrt(r.area); s=g.uniform(12,20)
    t=np.linspace(0,R/s*2*math.pi,3000); rr=s*t/(2*math.pi)
    return [LineString(list(zip(c.x+rr*np.cos(t),c.y+rr*np.sin(t)))).intersection(r)]
FILLS=[F_hatch,F_cross,F_conc,F_dots,F_scales,F_waves,F_pebbles,F_chevron,F_bricks,F_orbs,F_petals,F_spiral]
def fill_region(c,r,g,depth):
    if depth>0 and r.area>250000 and g.random()<.6:
        subs=voronoi_regions(g,int(g.integers(3,7)),r)
        for q in subs: fill_region(c,q,g,depth-1)
        stroke(c,r,7); return
    inner=r.buffer(-9,join_style=1)
    if not inner.is_empty:
        f=FILLS[int(g.integers(len(FILLS)))]
        for q in f(inner,g): stroke(c,q,2.8)
    stroke(c,r,6)
def tangle(c,g):
    for r in voronoi_regions(g,int(g.integers(14,24))): fill_region(c,r,g,2)
def bands(c,g):
    # flowing ribbons across page, each ribbon filled
    xs=np.linspace(M-50,W-M+50,400); curves=[]; y=M
    ys=sorted(g.uniform(M+100,H-M-100,int(g.integers(8,14))))
    prev=LineString([(M-60,M-60),(W-M+60,M-60)])
    regions=[]
    for y in ys+[H-M+60]:
        amp=g.uniform(60,220); wl=g.uniform(500,1400); ph=g.uniform(0,6)
        cur=LineString(list(zip(xs,y+amp*np.sin(xs/wl*2*math.pi+ph)))) if y<H-M else LineString([(M-60,H-M+60),(W-M+60,H-M+60)])
        poly=Polygon(list(prev.coords)+list(reversed(cur.coords))).buffer(0).intersection(FRAME)
        regions.append(poly); prev=cur
    for r in regions:
        for q in (r.geoms if hasattr(r,'geoms') else [r]):
            if q.area>1000: fill_region(c,q,g,1)
def rings(c,g):
    cx,cy=g.uniform(W*.3,W*.7),g.uniform(H*.3,H*.7); R=0; regs=[]
    while R<2600:
        w=g.uniform(70,170); ring=Point(cx,cy).buffer(R+w,200).difference(Point(cx,cy).buffer(R,200)).intersection(FRAME)
        n=int(g.choice([6,8,12,16,24]))
        for k in range(n):
            a0,a1=2*math.pi*k/n,2*math.pi*(k+1)/n
            wedge=Polygon([(cx,cy)]+[(cx+4000*math.cos(a),cy+4000*math.sin(a)) for a in np.linspace(a0,a1,8)])
            q=ring.intersection(wedge)
            if not q.is_empty and q.area>500: regs.append(q)
        R+=w
    f1,f2=FILLS[int(g.integers(len(FILLS)))],FILLS[int(g.integers(len(FILLS)))]
    for i,q in enumerate(regs):
        for qq in (q.geoms if hasattr(q,'geoms') else [q]):
            inner=qq.buffer(-7)
            if not inner.is_empty:
                for l in (f1 if i%2 else f2)(inner,g): stroke(c,l,2.6)
            stroke(c,qq,5)
STY=dict(tangle=tangle,bands=bands,rings=rings)
if __name__=='__main__':
    st,seed,out=sys.argv[1],int(sys.argv[2]),sys.argv[3]
    g=np.random.default_rng(seed); s,c=ctx(); STY[st](c,g)
    c.set_line_width(12); c.rectangle(M,M,W-2*M,H-2*M); c.stroke(); s.write_to_png(out)
