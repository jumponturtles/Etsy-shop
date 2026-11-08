"""Small-print wall art sets (4x6 + 5x7). Usage: small_wall.py SPEC.json OUT_ROOT"""
import sys, os, json, zipfile
sys.path.insert(0, os.path.dirname(__file__))
from package_wall import *
SMALL=[('4x6','4x6 in',(1200,1800)),('5x7','5x7 in',(1500,2100))]
def sizes_small(n,W=3000,H=2250):
    im=Image.new('RGB',(W,H),(24,24,27)); d=ImageDraw.Draw(im)
    def ct(y,t,f,c): w=d.textlength(t,font=f); d.text(((W-w)/2,y),t,font=f,fill=c)
    ct(200,'Small print sizes',lora(150),(255,255,255))
    ct(420,f'{2*n} JPG files · print-ready',pop(64),(214,190,140))
    y=700
    for _,lab,_ in SMALL:
        d.rounded_rectangle([700,y,2300,y+260],radius=40,fill=(40,40,46)); w=d.textlength(lab,font=pop(90)); d.text(((W-w)/2,y+70),lab,font=pop(90),fill=(240,240,240)); y+=330
    ct(1500,'Perfect for small frames, shelves, gallery walls & cards',pop(58),(200,200,210))
    ct(1950,'Instant download · print at home or at a photo lab',pop(52),(170,170,180))
    return im
def details_small(n,W=3000,H=2250):
    im=Image.new('RGB',(W,H),(245,242,236)); d=ImageDraw.Draw(im)
    def ct(y,t,f,c): w=d.textlength(t,font=f); d.text(((W-w)/2,y),t,font=f,fill=c)
    ct(200,'What you get',lora(160),(40,36,32))
    for i,r in enumerate([f'{n} matching artworks','4x6 and 5x7 sizes','Print-ready JPG files','Instant digital download','No frame included · digital file only']):
        ct(560+i*230,'•  '+r,pop(80),(60,54,48))
    return im
SPEC,ROOT=sys.argv[1],sys.argv[2]
for sp in json.load(open(SPEC))['listings']:
    folder=os.path.join(ROOT,sp['slug']); os.makedirs(folder,exist_ok=True)
    arts=[Image.open(f'/home/claude/W01/master/art_{n:02d}.png').convert('RGB') for n in sp['arts']]
    with zipfile.ZipFile(os.path.join(folder,f"{sp['base']}_4x6_5x7.zip"),'w',zipfile.ZIP_STORED) as z:
        for i,a in enumerate(arts,1):
            for key,_,(w,h) in SMALL: z.writestr(f"{sp['base']}_{i}_{key}.jpg",jpg_bytes(crop_ratio(a,w,h),q=92))
    mockup([thumb(a,2400) for a in arts]).save(os.path.join(folder,'01_cover.jpg'),quality=90)
    art_only([thumb(a,2400) for a in arts]).save(os.path.join(folder,'02_art.jpg'),quality=90)
    sizes_small(len(arts)).save(os.path.join(folder,'03_sizes.jpg'),quality=90)
    details_small(len(arts)).save(os.path.join(folder,'04_details.jpg'),quality=90)
    print(sp['slug'],sorted(os.listdir(folder)))
