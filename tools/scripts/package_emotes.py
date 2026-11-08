"""Emote listing packager. Usage: package_emotes.py SPEC.json OUT_ROOT"""
import sys, os, json, glob, zipfile
from PIL import Image, ImageDraw, ImageFont
SPEC, ROOT = sys.argv[1], sys.argv[2]
FD='/usr/share/fonts/truetype/google-fonts/'
def pop(sz,w='Medium'): return ImageFont.truetype(FD+f'Poppins-{w}.ttf',sz)
def lora(sz):
    f=ImageFont.truetype(FD+'Lora-Variable.ttf',sz)
    try: f.set_variation_by_name('Bold')
    except Exception: pass
    return f
W,H=3000,2250; DARK=(24,24,27); PURP=(145,70,255)
def ctext(d,y,t,f,fill): w=d.textlength(t,font=f); d.text(((W-w)/2,y),t,font=f,fill=fill)
def emotes(k): return sorted(glob.glob(f"{sp['src']}/{k}/512px/*.png"))
def paste_grid(im, files, box, cols):
    x0,y0,x1,y1=box; n=len(files); rows=-(-n//cols); cw=(x1-x0)/cols; ch=(y1-y0)/rows; s=int(min(cw,ch)*0.9)
    for i,f in enumerate(files):
        e=Image.open(f).resize((s,s),Image.LANCZOS)
        im.paste(e,(int(x0+(i%cols)*cw+(cw-s)/2),int(y0+(i//cols)*ch+(ch-s)/2)),e)
spec=json.load(open(SPEC))
for sp in spec['listings']:
    folder=os.path.join(ROOT,sp['slug']); os.makedirs(folder,exist_ok=True)
    files=[f for k in sp['packs'] for f in emotes(k)]
    # zip: sizes folders
    # zips: split by pack so each part stays under ~19MB (Etsy 20MB/file, max 5 files)
    import io
    def pack_bytes(k):
        b=io.BytesIO()
        with zipfile.ZipFile(b,'w',zipfile.ZIP_DEFLATED) as z:
            for px in (28,56,112,512):
                for f in sorted(glob.glob(f"{sp['src']}/{k}/{px}px/*.png")):
                    z.write(f,'x')
        return len(b.getvalue())
    groups=[]; cur=[]; size=0
    for k in sp['packs']:
        s_=pack_bytes(k)
        if cur and size+s_>18_500_000: groups.append(cur); cur=[]; size=0
        cur.append(k); size+=s_
    groups.append(cur)
    assert len(groups)<=5
    for gi,g in enumerate(groups,1):
        zn=sp['zipbase']+(f'_part{gi}of{len(groups)}' if len(groups)>1 else '')+'.zip'
        with zipfile.ZipFile(os.path.join(folder,zn),'w',zipfile.ZIP_DEFLATED) as z:
            for k in g:
                for px in (28,56,112,512):
                    for f in sorted(glob.glob(f"{sp['src']}/{k}/{px}px/*.png")):
                        sub='Twitch' if px<=112 else 'Discord_Sticker_HiRes'
                        z.write(f, f"{sp['zipbase']}/{sub}/{px}px/{os.path.basename(f)}")
            z.writestr(f"{sp['zipbase']}/README.txt", "Thank you for your purchase!\n\nTwitch: upload the 112px, 56px and 28px files (Creator Dashboard > Viewer Rewards > Emotes).\nDiscord: Server Settings > Emoji: upload the 112px or 512px file. Stickers: use the 512px file.\nYouTube / Kick / 7TV / BTTV: use 112px (or 512px where allowed).\n\nLicense: for use on YOUR OWN channel/server. Please do not resell or share the files.\n")
    # 1 cover
    im=Image.new('RGB',(W,H),DARK); d=ImageDraw.Draw(im)
    ctext(d,110,sp['cover_title'],lora(150),(255,255,255)); ctext(d,320,sp['cover_sub'],pop(80),(190,160,255))
    cols=3 if len(files)<=6 else 8
    paste_grid(im,(files if len(files)<=24 else files[::max(1,len(files)//32)][:32]),(350 if cols==3 else 150,470,W-(350 if cols==3 else 150),H-250),cols)
    ctext(d,H-200,'TWITCH · DISCORD · YOUTUBE · KICK',pop(64),(170,170,180))
    im.save(os.path.join(folder,'01_cover.jpg'),quality=90)
    # 2 chat mock
    im=Image.new('RGB',(W,H),(14,14,16)); d=ImageDraw.Draw(im)
    ctext(d,90,'How they look in chat',lora(120),(255,255,255))
    d.rounded_rectangle([500,330,2500,2080],40,fill=DARK)
    names=['nightowl_77','pixel_mage','cozygamer','tacoboss','luna.exe','frogfan']; cols_=[(255,120,120),(120,200,255),(140,255,160),(255,200,90),(220,140,255),(120,255,230)]
    y=400
    for i,f in enumerate(files[:6]):
        d.text((560,y+10),names[i]+':',font=pop(58,'Medium'),fill=cols_[i]); x=560+d.textlength(names[i]+': ',font=pop(58,'Medium'))
        for r in range(3 if i%2==0 else 1):
            e=Image.open(f).resize((112,112),Image.LANCZOS); im.paste(e,(int(x)+r*125,y),e)
        y+=270
    im.save(os.path.join(folder,'02_chat_preview.jpg'),quality=90)
    # 3 sizes
    im=Image.new('RGB',(W,H),(245,243,250)); d=ImageDraw.Draw(im)
    ctext(d,110,'Every size included',lora(130),(30,30,40))
    f=files[0]; x=380
    for px,show in ((512,900),(112,336),(56,168),(28,84)):
        e=Image.open(f).resize((show,show),Image.LANCZOS); im.paste(e,(x,1050-show//2),e)
        d.text((x+show//2-80,1600),f'{px}px',font=pop(70),fill=PURP); x+=show+220
    ctext(d,1850,'Transparent PNG · Ready to upload',pop(70),(60,60,70))
    im.save(os.path.join(folder,'03_sizes.jpg'),quality=90)
    # 4 details
    im=Image.new('RGB',(W,H),(245,243,250)); d=ImageDraw.Draw(im)
    ctext(d,150,"What you'll receive",lora(130),(30,30,40)); y=470
    for line in sp['details']:
        d.ellipse([480,y+30,520,y+70],fill=PURP); d.text((580,y),line,font=pop(78,'Regular'),fill=(30,30,40)); y+=190
    ctext(d,H-250,'Instant digital download · No physical item is shipped',pop(62),PURP)
    im.save(os.path.join(folder,'04_details.jpg'),quality=90)
    print(sp['slug'], [ (f,os.path.getsize(os.path.join(folder,f))) for f in sorted(os.listdir(folder)) if f.endswith('.zip')])
