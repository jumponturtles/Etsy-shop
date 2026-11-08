"""Wall art packager. Usage: package_wall.py SPEC.json OUT_ROOT
spec listing: slug, arts:[n...], title_short, ... ; masters at W01/master/art_NN.png (4096x6144)"""
import sys, os, json, zipfile, io
from PIL import Image, ImageDraw, ImageFilter, ImageFont
Image.MAX_IMAGE_PIXELS=None
FD='/usr/share/fonts/truetype/google-fonts/'
def pop(sz,w='Medium'): return ImageFont.truetype(FD+f'Poppins-{w}.ttf',sz)
def lora(sz):
    f=ImageFont.truetype(FD+'Lora-Variable.ttf',sz)
    try: f.set_variation_by_name('Bold')
    except Exception: pass
    return f
RATIOS=[('2x3','2x3 ratio (4x6, 8x12, 12x18, 16x24, 20x30 in)',(4800,7200)),
        ('3x4','3x4 ratio (6x8, 9x12, 12x16, 18x24 in)',(5400,7200)),
        ('4x5','4x5 ratio (8x10, 16x20 in)',(4800,6000)),
        ('11x14','11x14 in',(3300,4200)),
        ('ISO','ISO A-sizes (A5, A4, A3, A2)',(4961,7016))]
def crop_ratio(im,w,h):
    W,H=im.size; r=w/h
    if W/H>r: nw=int(H*r); x=(W-nw)//2; im=im.crop((x,0,x+nw,H))
    else: nh=int(W/r); y=(H-nh)//2; im=im.crop((0,y,W,y+nh))
    return im.resize((w,h),Image.LANCZOS)
def jpg_bytes(im,q=92):
    b=io.BytesIO(); im.save(b,'JPEG',quality=q,dpi=(300,300),optimize=True); return b.getvalue()
def thumb(m,h): return m.resize((int(m.width*h/m.height),h),Image.LANCZOS)
def framed(art,h,frame=(40,32,28),mat=True):
    a=thumb(art,h); fw=max(10,h//28); mw=h//9 if mat else 0
    W=a.width+2*(fw+mw); H=a.height+2*(fw+mw)
    f=Image.new('RGB',(W,H),frame); 
    if mat: f.paste(Image.new('RGB',(a.width+2*mw,a.height+2*mw),(248,246,241)),(fw,fw))
    f.paste(a,(fw+mw,fw+mw)); return f
def wall(W,H,col=(226,219,206)):
    bg=Image.new('RGB',(W,H),col); d=ImageDraw.Draw(bg)
    for y in range(H): 
        k=int(10*y/H); d.line([(0,y),(W,y)],fill=tuple(max(0,c-k) for c in col))
    fl=int(H*0.86); d.rectangle([0,fl,W,H],fill=(176,150,118)); d.line([0,fl,W,fl],fill=(150,126,98),width=6)
    return bg
def put(bg,f,x,y):
    sh=Image.new('RGBA',(f.width+80,f.height+80),(0,0,0,0)); ImageDraw.Draw(sh).rectangle([40,52,f.width+40,f.height+52],fill=(0,0,0,90))
    sh=sh.filter(ImageFilter.GaussianBlur(22)); bg.paste(sh,(x-40,y-40),sh); bg.paste(f,(x,y))
def mockup(arts,W=3000,H=2250):
    bg=wall(W,H)
    if len(arts)==1:
        f=framed(arts[0],1350); put(bg,f,(W-f.width)//2,int(H*0.40)-f.height//2)
    else:
        h=1050
        while True:
            fs=[framed(a,h) for a in arts]; gap=110
            if sum(f.width for f in fs)+gap*(len(fs)-1)<=W-240: break
            h-=40
        gap=110; tot=sum(f.width for f in fs)+gap*(len(fs)-1); x=(W-tot)//2
        for f in fs: put(bg,f,x,int(H*0.40)-f.height//2); x+=f.width+gap
    return bg
def art_only(arts,W=3000,H=2250):
    bg=Image.new('RGB',(W,H),(245,242,236))
    if len(arts)==1:
        a=thumb(arts[0],2000); bg.paste(a,((W-a.width)//2,(H-a.height)//2))
    else:
        th=[thumb(a,1700) for a in arts]; gap=90; tot=sum(t.width for t in th)+gap*(len(th)-1); x=(W-tot)//2
        for t in th: bg.paste(t,(x,(H-t.height)//2)); x+=t.width+gap
    return bg
def detail(art,W=3000,H=2250):
    w,h=art.size; c=art.crop((w//2-w//4,h//2-int(w//4*0.75),w//2+w//4,h//2+int(w//4*0.75)))
    return c.resize((W,H),Image.LANCZOS)
def sizes(title,n_items,W=3000,H=2250):
    im=Image.new('RGB',(W,H),(24,24,27)); d=ImageDraw.Draw(im)
    def ct(y,t,f,c): w=d.textlength(t,font=f); d.text(((W-w)/2,y),t,font=f,fill=c)
    ct(130,'Print-ready sizes',lora(150),(255,255,255))
    ct(330,f'{5*n_items} high-resolution JPG files · 300 DPI' if n_items>1 else '5 high-resolution JPG files · 300 DPI',pop(64),(214,190,140))
    y=560
    for _,lab,(w,h) in RATIOS:
        d.rounded_rectangle([420,y,2580,y+220],radius=40,fill=(40,40,46)); d.text((500,y+60),lab,font=pop(66),fill=(240,240,240))
        y+=260
    ct(1950,'Instant download · print at home, a local print shop or online',pop(52),(170,170,180))
    return im
def details_img(n_items,W=3000,H=2250):
    im=Image.new('RGB',(W,H),(245,242,236)); d=ImageDraw.Draw(im)
    def ct(y,t,f,c): w=d.textlength(t,font=f); d.text(((W-w)/2,y),t,font=f,fill=c)
    ct(200,'What you get',lora(160),(40,36,32))
    rows=[f'{n_items} artwork' + ('s' if n_items>1 else ''),'5 aspect ratios to fit standard frames','High resolution 300 DPI JPG','Instant digital download','No frame included · digital file only']
    y=560
    for r in rows: ct(y,'•  '+r,pop(80),(60,54,48)); y+=230
    return im
if __name__=='__main__':
    SPEC,ROOT=sys.argv[1],sys.argv[2]
    spec=json.load(open(SPEC))
    for sp in spec['listings']:
        folder=os.path.join(ROOT,sp['slug']); os.makedirs(folder,exist_ok=True)
        arts=[Image.open(f'/home/claude/W01/master/art_{n:02d}.png').convert('RGB') for n in sp['arts']]
        # deliverables
        if len(arts)==1:
            for key,_,(w,h) in RATIOS:
                b=jpg_bytes(crop_ratio(arts[0],w,h))
                open(os.path.join(folder,f"{sp['base']}_{key}.jpg"),'wb').write(b)
        else:
            for key,_,(w,h) in RATIOS:
                with zipfile.ZipFile(os.path.join(folder,f"{sp['base']}_{key}.zip"),'w',zipfile.ZIP_STORED) as z:
                    for i,a in enumerate(arts,1): z.writestr(f"{sp['base']}_{i}_{key}.jpg",jpg_bytes(crop_ratio(a,w,h),q=88))
        mockup(arts).save(os.path.join(folder,'01_cover.jpg'),quality=90)
        art_only(arts).save(os.path.join(folder,'02_art.jpg'),quality=90)
        detail(arts[0]).save(os.path.join(folder,'03_detail.jpg'),quality=90)
        sizes(sp['slug'],len(arts)).save(os.path.join(folder,'04_sizes.jpg'),quality=90)
        details_img(len(arts)).save(os.path.join(folder,'05_details.jpg'),quality=90)
        print(sp['slug'],[(f,os.path.getsize(os.path.join(folder,f))//1000000) for f in sorted(os.listdir(folder)) if not f.startswith('0')])
