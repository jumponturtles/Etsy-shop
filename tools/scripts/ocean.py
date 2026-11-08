"""Ocean abstract coloring book: wavy ripple backgrounds + unique simple sea creatures.
Usage: ocean.py BOOK_SEED OUT_DIR [PAGES]"""
import sys, os, math, random
import numpy as np, cairo
from shapely.geometry import Polygon, Point, LineString, MultiLineString, box
from shapely.ops import unary_union
from shapely import affinity
W,H=2550,3300; M=150; FRAME=box(M,M,W-M,H-M)

def draw(c,g,w):
    if g is None or g.is_empty: return
    c.set_line_width(w)
    def path(h):
        if h.geom_type=='Polygon':
            for ring in [h.exterior]+list(h.interiors):
                p=list(ring.coords); c.move_to(*p[0]); [c.line_to(*q) for q in p[1:]]; c.close_path()
        elif h.geom_type in('LineString','LinearRing'):
            p=list(h.coords)
            if len(p)<2: return
            c.move_to(*p[0]); [c.line_to(*q) for q in p[1:]]
        elif hasattr(h,'geoms'):
            for k in h.geoms: path(k)
    path(g); c.stroke()

def curve(pts,n=60):
    """smooth Catmull-Rom through pts"""
    pts=np.array(pts,float); out=[]
    P=np.vstack([pts[0],pts,pts[-1]])
    for i in range(1,len(P)-2):
        p0,p1,p2,p3=P[i-1],P[i],P[i+1],P[i+2]
        for t in np.linspace(0,1,n//max(1,len(pts)-1)+2)[:-1]:
            t2,t3=t*t,t*t*t
            out.append(0.5*((2*p1)+(-p0+p2)*t+(2*p0-5*p1+4*p2-p3)*t2+(-p0+3*p1-3*p2+p3)*t3))
    out.append(pts[-1]); return out

# ---------------- creature builders: return (outline_polys, inner_lines) in unit-ish coords ----------------
def fish(r):
    L=1.0; Hh=r.uniform(.28,.55); tail=r.choice(['fork','fan','round']); nose=r.uniform(.0,.12)
    top=[(-.5,0),(-.35,Hh*.8),(0,Hh),(.3,Hh*.75),(.5,nose)]
    bot=[(.5,-nose*0.3),(.3,-Hh*.7),(0,-Hh*.9),(-.35,-Hh*.7),(-.5,0)]
    body=Polygon(curve(top)+curve(bot)).buffer(0)
    tw=r.uniform(.25,.45)
    if tail=='fork': t=Polygon([(-.45,0),(-.5-tw,Hh*.9),(-.5-tw*.55,0),(-.5-tw,-Hh*.9)])
    elif tail=='fan': t=Polygon(curve([(-.45,0),(-.5-tw,Hh*.8),(-.5-tw*1.1,0),(-.5-tw,-Hh*.8),(-.45,0)]))
    else: t=Point(-.5-tw*.5,0).buffer(tw*.55,24)
    fin=Polygon(curve([(-.15,Hh*.85),(r.uniform(-.1,.15),Hh+r.uniform(.12,.3)),(.2,Hh*.7)]))
    parts=[body,t.buffer(0),fin.buffer(0)]
    if r.random()<.6: parts.append(Polygon(curve([(0,-Hh*.85),(.05,-Hh-r.uniform(.08,.2)),(.18,-Hh*.6)])).buffer(0))
    lines=[]
    ns=int(r.integers(2,5)); kind=r.integers(3)
    for k in range(ns):
        x=-.3+ (k+1)*.6/(ns+1)
        if kind==0: lines.append(LineString(curve([(x-.05,Hh),(x+.03,0),(x-.05,-Hh)])).intersection(body))
        elif kind==1: lines.append(LineString([(x,-Hh),(x+.08,0),(x,Hh)]).intersection(body))
        else: lines.append(Point(x,r.uniform(-.1,.1)*Hh).buffer(Hh*r.uniform(.15,.3),20).boundary.intersection(body))
    lines.append(LineString(curve([(.25,Hh*.6),(.2,0),(.25,-Hh*.5)])).intersection(body))  # gill
    return parts,lines
def jelly(r):
    w=.5; h=r.uniform(.3,.5); sc=int(r.integers(4,8))
    top=[(-w+2*w*t, h*math.sin(math.pi*t)**r.uniform(.6,1.2)) for t in np.linspace(0,1,40)]
    bot=[]
    for k in range(sc):
        a=-w+2*w*k/sc; b=a+2*w/sc
        bot+= [(b-(b-a)*t, -0.06*math.sin(math.pi*t)) for t in np.linspace(0,1,10)]
    dome=Polygon(list(reversed(top))[::-1]+bot[::-1]).buffer(0)
    dome=Polygon(top+[(p[0],p[1]) for p in reversed(bot)][::-1]).buffer(0) if dome.is_empty else dome
    lines=[LineString(curve([(-w*.7,h*.15),(0,h*.35),(w*.7,h*.15)])).intersection(dome)]
    tent=[]; nt=int(r.integers(3,7)); ln=r.uniform(.6,1.1)
    for k in range(nt):
        x=-w*.75+1.5*w*k/max(1,nt-1); ph=r.uniform(0,6); amp=r.uniform(.03,.07)
        ys=np.linspace(-.05,-ln*r.uniform(.7,1),30)
        tent.append(LineString([(x+amp*math.sin(ph+y*14),y) for y in ys]).buffer(r.uniform(.012,.03),cap_style=1))
    return [dome]+tent,lines
def star(r):
    n=int(r.choice([5,5,6])); R=.5; rr=R*r.uniform(.35,.5); pts=[]
    for k in range(n*2):
        a=math.pi*k/n+r.uniform(-.06,.06); rad=R*r.uniform(.9,1.05) if k%2==0 else rr
        pts.append((rad*math.cos(a),rad*math.sin(a)))
    p=Polygon(curve(pts+[pts[0]],120)).buffer(.03).buffer(-.03)
    lines=[p.buffer(-.07,join_style=1).boundary]
    for k in range(0,n*2,2): lines.append(LineString([(0,0),pts[k]]).intersection(p.buffer(-.1)))
    return [p],lines
def shell(r):
    n=int(r.integers(6,11)); spread=r.uniform(1.6,2.4); R=.5
    fan=[(0,-.35)]
    for k in range(n*6+1):
        a=math.pi/2-spread/2+spread*k/(n*6); bump=1+0.06*math.cos(math.pi*2*k/6)
        fan.append((R*bump*math.cos(a),-.35+R*1.2*bump*math.sin(a)))
    p=Polygon(fan).buffer(0)
    lines=[]
    for k in range(1,n):
        a=math.pi/2-spread/2+spread*k/n
        lines.append(LineString([(0,-.35),(R*1.3*math.cos(a),-.35+R*1.5*math.sin(a))]).intersection(p))
    base=Polygon([(-.12,-.35),(.12,-.35),(.07,-.45),(-.07,-.45)])
    return [p,base],lines
def spiral_shell(r):
    pts=[]; turns=r.uniform(2.2,3.2); a0=r.uniform(.02,.05)
    for t in np.linspace(0,turns*2*math.pi,300):
        rad=a0*math.exp(.18*t); pts.append((rad*math.cos(t),rad*math.sin(t)))
    pts=np.array(pts); pts/=np.abs(pts).max()*2
    outer=Polygon(pts[-150:].tolist()+[tuple(pts[-150])]).buffer(.02)
    body=unary_union([outer,LineString(pts.tolist()).buffer(.02)]).convex_hull.buffer(0)
    return [body],[LineString(pts.tolist()).intersection(body)]
def whale(r):
    Hh=r.uniform(.22,.32)
    top=[(-.5,.02),(-.2,Hh*.9),(.2,Hh),(.45,Hh*.6),(.5,0)]
    bot=[(.5,0),(.4,-Hh*.75),(0,-Hh*.85),(-.4,-Hh*.4),(-.5,.02)]
    body=Polygon(curve(top)+curve(bot)).buffer(0)
    tail=Polygon(curve([(-.45,.02),(-.62,.2),(-.58,.06),(-.7,0),(-.58,-.02),(-.62,-.14),(-.45,0)])).buffer(0)
    belly=LineString(curve([(.45,-Hh*.2),(0,-Hh*.45),(-.35,-Hh*.25)])).intersection(body)
    grooves=[LineString(curve([(.4,-Hh*(.3+.1*k)),(0,-Hh*(.55+.08*k)),(-.25,-Hh*(.35+.05*k))])).intersection(body) for k in range(int(r.integers(1,4)))]
    fin=Polygon(curve([(.05,-Hh*.4),(-.05,-Hh*1.3),(-.12,-Hh*.5)])).buffer(0)
    return [body,tail,fin],[belly]+grooves
def octo(r):
    head=Polygon(curve([(-.22,0),(-.25,.3),(0,.5),(.25,.3),(.22,0)])+[(.22,0),(-.22,0)]).buffer(.02)
    arms=[]
    for k in range(int(r.choice([6,8]))):
        x0=-.2+.4*k/7; dirn=-1 if x0<0 else 1; ln=r.uniform(.35,.6); ph=r.uniform(0,6)
        pts=[(x0+dirn*.5*t*ln+.04*math.sin(ph+t*9), -t*ln) for t in np.linspace(0,1,30)]
        arms.append(LineString(pts).buffer(.04*(1)-0.0,cap_style=1))
    arms=[unary_union(arms)]
    spots=[Point(r.uniform(-.12,.12),r.uniform(.15,.4)).buffer(r.uniform(.03,.06),16).boundary for _ in range(int(r.integers(2,5)))]
    return [head]+arms,spots
def turtle(r):
    sh=Point(0,0).buffer(.3,48); sh=affinity.scale(sh,1.25,1)
    head=Point(.48,0).buffer(.09,24)
    fl=[affinity.rotate(affinity.scale(Point(0,0).buffer(.1,24),1.9,.7),a) for a in (35,-35,145,-145)]
    fl=[affinity.translate(f,.25*math.cos(math.radians(a))*1.3,.25*math.sin(math.radians(a))) for f,a in zip(fl,(35,-35,145,-145))]
    lines=[sh.buffer(-.06).boundary]
    for k in range(6):
        a=math.pi/3*k; lines.append(LineString([(0,0),(.4*math.cos(a)*1.25,.4*math.sin(a))]).intersection(sh.buffer(-.06)))
    lines.append(Point(0,0).buffer(.1,6).boundary)
    return [sh,head]+fl,lines
def ray(r):
    s=r.uniform(.25,.4)
    p=Polygon(curve([(0,.3),(.5,s*.2),(.15,-.15),(0,-.2),(-.15,-.15),(-.5,s*.2),(0,.3)],120)).buffer(0)
    tail=LineString(curve([(0,-.18),(.05,-.45),(-.03,-.7)])).buffer(.015)
    lines=[LineString(curve([(-.35,.05),(0,.1),(.35,.05)])).intersection(p),LineString([(0,.25),(0,-.15)])]
    return [p,tail],lines
def crab(r):
    body=affinity.scale(Point(0,0).buffer(.25,40),1.4,.8)
    legs=[]
    for s in(-1,1):
        for k in range(3):
            y=-.05-.07*k; legs.append(LineString([(s*.3,y),(s*.45,y+.05),(s*.55,y-.12)]).buffer(.025,cap_style=1))
        arm=LineString([(s*.25,.12),(s*.35,.3),(s*.3,.42)]).buffer(.03)
        claw=Polygon([(s*.3,.4),(s*.42,.55),(s*.32,.5),(s*.22,.58),(s*.2,.45)]).buffer(.02)
        legs+= [arm,claw]
    lines=[LineString(curve([(-.2,0),(0,.08),(.2,0)])).intersection(body),LineString(curve([(-.15,-.08),(0,-.02),(.15,-.08)])).intersection(body)]
    return [body]+legs,lines
def seaweed(r):
    parts=[]; nb=int(r.integers(2,4))
    for b in range(nb):
        x0=r.uniform(-.2,.2); ph=r.uniform(0,6); ln=r.uniform(.6,1.0)
        pts=[(x0+.06*math.sin(ph+t*7),-.5+t*ln) for t in np.linspace(0,1,40)]
        parts.append(LineString(pts).buffer(r.uniform(.03,.05),cap_style=1))
        for k in range(int(r.integers(3,6))):
            t=r.uniform(.2,.9); px,py=pts[int(t*39)]; s=r.choice([-1,1])
            parts.append(affinity.rotate(affinity.scale(Point(px+s*.06,py).buffer(.05,20),1.6,.6),s*30,origin=(px,py)))
    return [unary_union(parts)],[]
def coral(r):
    segs=[]
    def grow(x,y,a,l,d):
        if d==0 or l<.05: return
        x2,y2=x+l*math.cos(a),y+l*math.sin(a); segs.append(LineString([(x,y),(x2,y2)]).buffer(.035*(d/4+.4),cap_style=1))
        for da in (r.uniform(.25,.6),-r.uniform(.25,.6)): grow(x2,y2,a+da,l*r.uniform(.6,.8),d-1)
    grow(0,-.5,math.pi/2,.28,int(r.integers(3,5)))
    return [unary_union(segs)],[]
def bubbles(r):
    parts=[]
    for k in range(int(r.integers(3,7))):
        parts.append(Point(r.uniform(-.3,.3),r.uniform(-.5,.5)).buffer(r.uniform(.04,.13),32))
    return parts,[]
KINDS=dict(fish=fish,jelly=jelly,star=star,shell=shell,snail=spiral_shell,whale=whale,octo=octo,turtle=turtle,ray=ray,crab=crab,coral=coral,bubbles=bubbles)

def place(parts,lines,cx,cy,size,ang,flip):
    def T(g):
        g=affinity.scale(g,size*(-1 if flip else 1),-size,origin=(0,0))
        g=affinity.rotate(g,ang,origin=(0,0)); return affinity.translate(g,cx,cy)
    return [T(p) for p in parts],[T(l) for l in lines]

# ---------------- backgrounds ----------------
def bg_waves(rng,clip):
    out=[]; step=rng.uniform(30,46); amp=rng.uniform(20,70); wl=rng.uniform(250,600); drift=rng.uniform(-.4,.4)
    y=M-amp
    ph=rng.uniform(0,6)
    while y<H-M+amp*2:
        xs=np.linspace(M,W-M,300)
        out.append(LineString(list(zip(xs,y+drift*(xs-M)*.2+amp*np.sin(xs/wl*2*math.pi+ph+y*.004)))))
        y+=step
    return [g.intersection(clip) for g in out]
def bg_ripples(rng,clip):
    out=[]
    for _ in range(int(rng.integers(4,8))):
        cx,cy=rng.uniform(M,W-M),rng.uniform(M,H-M); step=rng.uniform(30,45)
        for k in range(1,60): out.append(Point(cx,cy).buffer(k*step,96).boundary)
    # union-free: draw each ring only where it is not inside a later center's nearer ring -> use voronoi-like assignment
    return [g.intersection(clip) for g in out]
def bg_ripple_cells(rng,clip):
    cs=[(rng.uniform(M,W-M),rng.uniform(M,H-M)) for _ in range(int(rng.integers(5,9)))]
    from scipy.spatial import Voronoi
    pts=np.array(cs+[(-9e3,-9e3),(9e3,-9e3),(-9e3,9e3),(9e3,9e3)]); vor=Voronoi(pts); out=[]
    for i,(cx,cy) in enumerate(cs):
        reg=vor.regions[vor.point_region[i]]
        cell=Polygon(vor.vertices[reg]).intersection(clip); step=rng.uniform(28,42)
        out.append(cell.boundary)
        for k in range(1,80):
            ring=Point(cx,cy).buffer(k*step,96).boundary.intersection(cell)
            if ring.is_empty and k>5: break
            out.append(ring)
    return out
def bg_currents(rng,clip):
    out=[]; n=int(rng.integers(5,9))
    bands=sorted(rng.uniform(M,H-M,n))
    for i in range(n):
        y0=bands[i]; amp=rng.uniform(60,180); wl=rng.uniform(500,1100); ph=rng.uniform(0,6)
        xs=np.linspace(M,W-M,300); base=y0+amp*np.sin(xs/wl*2*math.pi+ph)
        for k in range(int(rng.integers(4,9))):
            out.append(LineString(list(zip(xs,base+k*rng.uniform(18,26)))))
    return [g.intersection(clip) for g in out]
def bg_bands(rng,clip):
    out=[]; y=M; xs=np.linspace(M,W-M,300)
    prev=np.full_like(xs,M-80.0)
    while y<H-M+200:
        amp=rng.uniform(25,90); wl=rng.uniform(300,800); ph=rng.uniform(0,6); step=rng.uniform(26,40)
        for k in range(int(rng.integers(5,10))):
            yy=y+k*step+amp*np.sin(xs/wl*2*math.pi+ph)
            out.append(LineString(list(zip(xs,yy))))
        y+=int(rng.integers(5,10))*step*0.9
    return [g.intersection(clip) for g in out]
BGS=[bg_waves,bg_ripple_cells,bg_bands]

def page(rng,used,out,kinds_pool):
    s=cairo.ImageSurface(cairo.FORMAT_RGB24,W,H); c=cairo.Context(s)
    c.set_source_rgb(1,1,1); c.paint(); c.set_source_rgb(0,0,0)
    c.set_line_join(cairo.LINE_JOIN_ROUND); c.set_line_cap(cairo.LINE_CAP_ROUND)
    n=int(rng.integers(4,6)); kinds=list(rng.choice(kinds_pool,size=n,replace=False))
    placed=[]; holes=[]
    for k in kinds:
        for attempt in range(300):
            seed=int(rng.integers(1e9))
            if (k,seed) in used: continue
            r=np.random.default_rng(seed)
            parts,lines=KINDS[k](r)
            size=rng.uniform(700,1100) if k not in('bubbles','star','shell','snail') else rng.uniform(450,700)
            if k in('whale','turtle','octo'): size*=1.25
            cx,cy=rng.uniform(M+size*.4,W-M-size*.4),rng.uniform(M+size*.4,H-M-size*.4)
            ang=rng.uniform(-35,35) if k in('fish','whale','ray','turtle') else rng.uniform(-15,15)
            P,Ls=place(parts,lines,cx,cy,size,ang,rng.random()<.5)
            shape=unary_union(P).buffer(0)
            if not FRAME.buffer(-20).contains(shape): continue
            if any(shape.buffer(60).intersects(h) for h in holes): size*=0.97; continue
            used.add((k,seed)); holes.append(shape); placed.append((P,Ls)); break
    clip=FRAME.difference(unary_union(holes).buffer(22)) if holes else FRAME
    bg=BGS[int(rng.integers(len(BGS)))]
    for g in bg(rng,clip): draw(c,g,4)
    for P,Ls in placed:
        u=unary_union(P).buffer(0)
        draw(c,u.boundary if u.geom_type!='MultiPolygon' else MultiLineString([g.exterior for g in u.geoms]),8)
        for g in Ls: draw(c,g,5)
    c.set_line_width(12); c.rectangle(M,M,W-2*M,H-2*M); c.stroke()
    s.write_to_png(out)
    return kinds

if __name__=='__main__':
    seed=int(sys.argv[1]); od=sys.argv[2]; N=int(sys.argv[3]) if len(sys.argv)>3 else 20
    os.makedirs(od,exist_ok=True); rng=np.random.default_rng(seed); used=set()
    pool=list(KINDS)
    for i in range(1,N+1):
        k=page(rng,used,f'{od}/page_{i:02d}.png',pool); print(i,k,flush=True)
