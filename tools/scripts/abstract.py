"""Procedural abstract coloring pages (pure line art, 300 dpi Letter). abstract.py STYLE SEED OUT.png"""
import sys, math, random
import numpy as np, cairo
from shapely.geometry import Polygon, Point, LineString, MultiPolygon, box
from shapely.ops import unary_union
from scipy.spatial import Voronoi
W,H=2550,3300; M=150
LW=5.0
def ctx():
    s=cairo.ImageSurface(cairo.FORMAT_RGB24,W,H); c=cairo.Context(s)
    c.set_source_rgb(1,1,1); c.paint(); c.set_source_rgb(0,0,0)
    c.set_line_join(cairo.LINE_JOIN_ROUND); c.set_line_cap(cairo.LINE_CAP_ROUND); return s,c
def geom_path(c,g):
    if g.is_empty: return
    if g.geom_type in('Polygon',):
        for ring in [g.exterior]+list(g.interiors):
            pts=list(ring.coords); c.move_to(*pts[0]); [c.line_to(*p) for p in pts[1:]]; c.close_path()
    elif g.geom_type in('LineString','LinearRing'):
        pts=list(g.coords); c.move_to(*pts[0]); [c.line_to(*p) for p in pts[1:]]
    elif hasattr(g,'geoms'):
        for h in g.geoms: geom_path(c,h)
def stroke(c,g,w=LW):
    c.set_line_width(w); geom_path(c,g); c.stroke()
FRAME=box(M,M,W-M,H-M)
# ---------- fills clipped to a region ----------
def f_lines(r,rng,step=None,ang=None):
    step=step or rng.uniform(28,55); ang=ang if ang is not None else rng.uniform(0,math.pi)
    x0,y0,x1,y1=r.bounds; cx,cy=(x0+x1)/2,(y0+y1)/2; L=math.hypot(x1-x0,y1-y0)
    out=[]; d=-L/2
    while d<L/2:
        ox,oy=cx+d*math.cos(ang+math.pi/2),cy+d*math.sin(ang+math.pi/2)
        out.append(LineString([(ox-L*math.cos(ang),oy-L*math.sin(ang)),(ox+L*math.cos(ang),oy+L*math.sin(ang))]).intersection(r)); d+=step
    return out
def f_cross(r,rng): a=rng.uniform(0,math.pi); s=rng.uniform(40,70); return f_lines(r,rng,s,a)+f_lines(r,rng,s,a+math.pi/2)
def f_concentric(r,rng):
    out=[]; g=r; step=rng.uniform(22,40)
    for _ in range(60):
        g=g.buffer(-step,join_style=1)
        if g.is_empty or g.area<200: break
        out.append(g.boundary)
    return out
def f_dots(r,rng,circ=False):
    s=rng.uniform(55,90); rad=rng.uniform(.18,.34)*s; x0,y0,x1,y1=r.bounds; out=[]; row=0; y=y0
    while y<y1:
        x=x0+(s/2 if row%2 else 0)
        while x<x1:
            p=Point(x,y)
            if r.contains(p.buffer(rad)): out.append(p.buffer(rad,16).boundary)
            x+=s
        y+=s*0.87; row+=1
    return out
def f_scales(r,rng):
    s=rng.uniform(60,100); x0,y0,x1,y1=r.bounds; out=[]; row=0; y=y0
    while y<y1+s:
        x=x0-s+(s/2 if row%2 else 0)
        while x<x1+s:
            arc=LineString([(x+s/2*math.cos(t),y+s/2*math.sin(t)) for t in np.linspace(0,math.pi,24)])
            out.append(arc.intersection(r)); x+=s
        y+=s/2.2; row+=1
    return out
def f_waves(r,rng):
    s=rng.uniform(35,60); amp=rng.uniform(15,40); wl=rng.uniform(120,260); x0,y0,x1,y1=r.bounds; out=[]; y=y0
    while y<y1+amp:
        xs=np.linspace(x0,x1,200); out.append(LineString(list(zip(xs,y+amp*np.sin(xs/wl*2*math.pi)))).intersection(r)); y+=s
    return out
def f_grid_circles(r,rng):
    s=rng.uniform(80,130); x0,y0,x1,y1=r.bounds; out=[]
    for x in np.arange(x0,x1+s,s):
        for y in np.arange(y0,y1+s,s):
            for k in (0.45,0.28,0.1): out.append(Point(x,y).buffer(s*k,20).boundary.intersection(r))
    return out
def f_triangles(r,rng):
    s=rng.uniform(70,120); h=s*0.866; x0,y0,x1,y1=r.bounds; out=[]
    for j,y in enumerate(np.arange(y0-h,y1+h,h)):
        for x in np.arange(x0-s,x1+s,s):
            ox=x+(s/2 if j%2 else 0)
            out.append(Polygon([(ox,y),(ox+s,y),(ox+s/2,y+h)]).boundary.intersection(r))
            out.append(Polygon([(ox+s/2,y+h),(ox+s*1.5,y+h),(ox+s,y)]).boundary.intersection(r))
    return out
def f_spiral(r,rng):
    c=r.representative_point(); R=math.sqrt(r.area)*0.8; step=rng.uniform(22,34)
    t=np.linspace(0,R/step*2*math.pi,2000); rr=step*t/(2*math.pi)
    return [LineString(list(zip(c.x+rr*np.cos(t),c.y+rr*np.sin(t)))).intersection(r)]
FILLS=[f_lines,f_cross,f_concentric,f_dots,f_scales,f_waves,f_grid_circles,f_triangles,f_spiral]
# ---------- styles ----------
def voronoi_regions(rng,n,bounds=FRAME):
    x0,y0,x1,y1=bounds.bounds
    pts=np.c_[rng.uniform(x0,x1,n),rng.uniform(y0,y1,n)]
    for _ in range(2):  # Lloyd relax
        vor=Voronoi(np.r_[pts,[[-9e3,-9e3],[9e3,-9e3],[-9e3,9e3],[9e3,9e3]]]); new=[]
        for i in range(n):
            reg=vor.regions[vor.point_region[i]]
            if -1 in reg or not reg: new.append(pts[i]); continue
            p=Polygon(vor.vertices[reg]).intersection(bounds); new.append(pts[i] if p.is_empty else [p.centroid.x,p.centroid.y])
        pts=np.array(new)
    vor=Voronoi(np.r_[pts,[[-9e3,-9e3],[9e3,-9e3],[-9e3,9e3],[9e3,9e3]]]); regs=[]
    for i in range(n):
        reg=vor.regions[vor.point_region[i]]
        if -1 in reg or not reg: continue
        p=Polygon(vor.vertices[reg]).intersection(bounds)
        if not p.is_empty: regs.append(p)
    return regs
def s_tangle(c,rng):
    regs=voronoi_regions(rng,int(rng.integers(9,16)))
    for r in regs:
        inner=r.buffer(-14,join_style=1)
        f=FILLS[int(rng.integers(len(FILLS)))]
        for g in f(inner,rng): stroke(c,g,3.6)
        stroke(c,r,9)
def s_cells(c,rng):
    regs=voronoi_regions(rng,int(rng.integers(40,80)))
    for r in regs:
        g=r; k=0; step=rng.uniform(14,24)
        while True:
            g=g.buffer(-step if k==0 else -step*1.5,join_style=1); k+=1
            if g.is_empty or g.area<300: break
            stroke(c,g.boundary,3.8)
        stroke(c,r,7)
def petal(cx,cy,ang,r0,r1,wid):
    pts=[]
    for t in np.linspace(0,1,40):
        rr=r0+(r1-r0)*t; w=wid*math.sin(math.pi*t)
        pts.append((rr,w))
    pts=pts+[(rr,-w) for rr,w in reversed(pts)]
    ca,sa=math.cos(ang),math.sin(ang)
    return Polygon([(cx+x*ca-y*sa,cy+x*sa+y*ca) for x,y in pts])
def s_mandala(c,rng,cx=W/2,cy=H/2,R=1150,bg=True):
    if bg:
        bgfill=FILLS[int(rng.integers(len(FILLS)))]
        region=FRAME.difference(Point(cx,cy).buffer(R+40,96))
        for g in bgfill(region.buffer(-12),rng): stroke(c,g,3.4)
    n=int(rng.choice([8,10,12,16])); r=90
    stroke(c,Point(cx,cy).buffer(r,64).boundary,LW)
    for g in f_concentric(Point(cx,cy).buffer(r,64),rng)[:3]: stroke(c,g,3.5)
    while r<R-60:
        kind=rng.integers(5); w=rng.uniform(80,180); w=min(w,R-r)
        if kind==0:  # petals
            for k in range(n*int(rng.choice([1,2]))):
                a=2*math.pi*k/(n*1.0)+ (math.pi/n if rng.random()<.5 else 0)
                p=petal(cx,cy,a,r,r+w,w*rng.uniform(.25,.45)*(2*math.pi*r/n)/max(w,1)*0.5+20)
                stroke(c,p.boundary,4.2)
                for g in f_concentric(p,rng)[:3]: stroke(c,g,3)
        elif kind==1:  # circle beads
            m=int(2*math.pi*(r+w/2)/(w*0.9)); rr=w*0.42
            for k in range(m):
                a=2*math.pi*k/m; x,y=cx+(r+w/2)*math.cos(a),cy+(r+w/2)*math.sin(a)
                stroke(c,Point(x,y).buffer(rr,32).boundary,4); stroke(c,Point(x,y).buffer(rr*0.45,24).boundary,3)
        elif kind==2:  # band with zigzag
            m=n*int(rng.choice([2,3,4])); pts=[]
            for k in range(m*2+1):
                a=2*math.pi*k/(m*2); rr=r+ (w if k%2 else 0)
                pts.append((cx+rr*math.cos(a),cy+rr*math.sin(a)))
            stroke(c,LineString(pts),4.2)
        elif kind==3:  # scallops
            m=n*int(rng.choice([2,3]))
            for k in range(m):
                a0=2*math.pi*k/m; a1=2*math.pi*(k+1)/m; am=(a0+a1)/2
                pts=[(cx+(r)*math.cos(a0),cy+r*math.sin(a0))]
                for t in np.linspace(0,1,24):
                    a=a0+(a1-a0)*t; rr=r+w*math.sin(math.pi*t)
                    pts.append((cx+rr*math.cos(a),cy+rr*math.sin(a)))
                stroke(c,LineString(pts),4.2)
                stroke(c,LineString([(cx+r*math.cos(am),cy+r*math.sin(am)),(cx+(r+w*0.75)*math.cos(am),cy+(r+w*0.75)*math.sin(am))]),3)
        else:  # ring filled with pattern
            ring=Point(cx,cy).buffer(r+w,128).difference(Point(cx,cy).buffer(r,128))
            for g in FILLS[int(rng.choice([0,3,4,6]))](ring.buffer(-8),rng): stroke(c,g,3)
        r+=w
        stroke(c,Point(cx,cy).buffer(r,180).boundary,LW+1)
def s_kaleido(c,rng):
    cx,cy=W/2,H/2; k=int(rng.choice([6,8,10,12])); wedge=2*math.pi/k
    shapes=[]
    for _ in range(int(rng.integers(14,24))):
        rr=rng.uniform(80,1500); a=rng.uniform(0,wedge/2); x,y=rr*math.cos(a),rr*math.sin(a)
        t=rng.integers(3)
        if t==0: shapes.append(Point(x,y).buffer(rng.uniform(30,160),48).boundary)
        elif t==1:
            n=int(rng.integers(3,7)); s=rng.uniform(50,200); rot=rng.uniform(0,6)
            shapes.append(Polygon([(x+s*math.cos(rot+2*math.pi*i/n),y+s*math.sin(rot+2*math.pi*i/n)) for i in range(n)]).boundary)
        else:
            p=petal(0,0,a,max(0,rr-rng.uniform(100,300)),rr+rng.uniform(50,250),rng.uniform(30,110)); shapes.append(p.boundary)
    for j in range(k):
        for mir in (1,-1):
            ang=j*wedge
            for g in shapes:
                pts=[( (x*math.cos(ang)-mir*y*math.sin(ang))+cx, (x*math.sin(ang)+mir*y*math.cos(ang))+cy) for x,y in g.coords]
                stroke(c,LineString(pts).intersection(FRAME),4.2)
    for rr in rng.uniform(200,1500,int(rng.integers(2,5))): stroke(c,Point(cx,cy).buffer(rr,200).boundary.intersection(FRAME),4.5)
def s_flow(c,rng):
    # smooth noise flow field streamlines
    nx,ny=12,16; ang=rng.uniform(0,2*math.pi,(ny+1,nx+1))
    def field(x,y):
        gx=(x-M)/(W-2*M)*nx; gy=(y-M)/(H-2*M)*ny; i=min(int(gx),nx-1); j=min(int(gy),ny-1); fx=gx-i; fy=gy-j
        a=ang[j,i]*(1-fx)*(1-fy)+ang[j,i+1]*fx*(1-fy)+ang[j+1,i]*(1-fx)*fy+ang[j+1,i+1]*fx*fy; return a
    sep=rng.uniform(26,40); occ={}
    def key(x,y): return (int(x//sep),int(y//sep))
    def free(x,y):
        kx,ky=key(x,y)
        for dx in(-1,0,1):
            for dy in(-1,0,1):
                for (px,py) in occ.get((kx+dx,ky+dy),[]):
                    if (px-x)**2+(py-y)**2<(sep*0.9)**2: return False
        return True
    seeds=[(rng.uniform(M,W-M),rng.uniform(M,H-M)) for _ in range(5000)]
    for sx,sy in seeds:
        if not free(sx,sy): continue
        line=[]
        for d in (1,-1):
            x,y=sx,sy; seg=[]
            for _ in range(500):
                a=field(x,y); x+=d*6*math.cos(a); y+=d*6*math.sin(a)
                if not(M<x<W-M and M<y<H-M) or not free(x,y): break
                seg.append((x,y))
            line=(list(reversed(seg))+[(sx,sy)]) if d==1 else line+seg
            if d==1: line=list(reversed(line))
        if len(line)>20:
            for p in line[::3]: occ.setdefault(key(*p),[]).append(p)
            c.set_line_width(4); c.move_to(*line[0]); [c.line_to(*p) for p in line[1:]]; c.stroke()
def s_rosettes(c,rng):
    for _ in range(int(rng.integers(3,6))):
        cx,cy=rng.uniform(M+300,W-M-300),rng.uniform(M+300,H-M-300); R=rng.uniform(300,800)
        k=int(rng.integers(5,13)); rr=R*rng.uniform(.2,.5); d=rr*rng.uniform(.6,1.4)
        t=np.linspace(0,2*math.pi*int(rng.integers(3,8)),6000)
        Rr=R-rr; x=cx+Rr*np.cos(t)+d*np.cos(Rr/rr*t); y=cy+Rr*np.sin(t)-d*np.sin(Rr/rr*t)
        stroke(c,LineString(list(zip(x,y))).intersection(FRAME),3.4)
STYLES=dict(tangle=s_tangle,cells=s_cells,mandala=s_mandala,kaleido=s_kaleido,flow=s_flow,rosette=s_rosettes)
def render(style,seed,out,frame=True):
    rng=np.random.default_rng(seed); s,c=ctx(); STYLES[style](c,rng)
    if frame: c.set_line_width(12); c.rectangle(M,M,W-2*M,H-2*M); c.stroke()
    s.write_to_png(out)
if __name__=='__main__':
    render(sys.argv[1],int(sys.argv[2]),sys.argv[3])
