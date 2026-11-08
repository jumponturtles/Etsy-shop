"""Christmas cards, gift tags and phone wallpapers from W01 masters.
Usage: python3 -I xmas_products.py OUT_ROOT
"""
import sys, os, io, zipfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter
Image.MAX_IMAGE_PIXELS = None
OUT = sys.argv[1]
F = '/home/claude/fonts/'; G = '/usr/share/fonts/truetype/google-fonts/'
def vibes(s): return ImageFont.truetype(F + 'GreatVibes-Regular.ttf.ttf', s)
def play(s, w='Bold'):
    f = ImageFont.truetype(F + 'PlayfairDisplay.ttf', s)
    try: f.set_variation_by_name(w)
    except Exception: pass
    return f
def pop(s, w='Medium'): return ImageFont.truetype(G + f'Poppins-{w}.ttf', s)
def lora(s):
    f = ImageFont.truetype(G + 'Lora-Variable.ttf', s)
    try: f.set_variation_by_name('Bold')
    except Exception: pass
    return f

ART = {4: 'italian', 5: 'italian', 6: 'italian', 7: 'cabin', 8: 'cabin', 9: 'cabin', 10: 'botanical', 11: 'botanical', 12: 'botanical'}
NAME = {4: 'Panettone & Espresso', 5: 'Citrus & Olive', 6: 'Pizzelle & Espresso', 7: 'Snowy Cabin', 8: 'Red Truck', 9: 'Hot Cocoa',
        10: 'Holly', 11: 'Poinsettia', 12: 'Pine Cone'}
GREET = {'italian': 'Buon Natale', 'cabin': 'Merry Christmas', 'botanical': "Season's Greetings"}
INSIDE = {'italian': 'Wishing you a Christmas full of good food,\nwarm company and sweet moments.',
          'cabin': 'Wishing you a cozy Christmas\nand a bright, happy New Year.',
          'botanical': 'Wishing you peace, joy and every\nblessing of the season.'}
CREAM, INK, RED, GREEN, GOLD = (250, 246, 238), (46, 38, 34), (150, 36, 40), (44, 78, 58), (176, 140, 72)
_cache = {}
def art(n):
    if n not in _cache: _cache[n] = Image.open(f'/home/claude/W01/master/art_{n:02d}.png').convert('RGB')
    return _cache[n]
def crop(im, w, h, yb=0.5):
    W, H = im.size; r = w / h
    if W / H > r: nw = int(H * r); x = (W - nw) // 2; im = im.crop((x, 0, x + nw, H))
    else: nh = int(W / r); y = int((H - nh) * yb); im = im.crop((0, y, W, y + nh))
    return im.resize((w, h), Image.LANCZOS)
def ctext(d, cx, y, t, f, fill):
    w = d.textlength(t, font=f); d.text((cx - w / 2, y), t, font=f, fill=fill)
def jpg(im, q=93):
    b = io.BytesIO(); im.save(b, 'JPEG', quality=q, dpi=(300, 300)); return b.getvalue()
def pdf(pages):
    b = io.BytesIO(); pages[0].save(b, 'PDF', resolution=300, save_all=True, append_images=pages[1:]); return b.getvalue()

# ---------- CARDS (5x7 in @300dpi) ----------
def card_front(n, text=True):
    W, H = 1500, 2100
    if not text: return crop(art(n), W, H)
    c = Image.new('RGB', (W, H), CREAM); band = 430
    c.paste(crop(art(n), W - 120, H - band - 60), (60, 60))
    d = ImageDraw.Draw(c); s = ART[n]
    ctext(d, W / 2, H - band + 50, GREET[s], vibes(190), RED if s != 'botanical' else GREEN)
    d.line([(W / 2 - 160, H - 95), (W / 2 + 160, H - 95)], fill=GOLD, width=4)
    return c
def card_inside(n):
    W, H = 1500, 2100; c = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(c); s = ART[n]
    y = 820
    for line in INSIDE[s].split('\n'): ctext(d, W / 2, y, line, play(64, 'Regular'), INK); y += 100
    ctext(d, W / 2, y + 60, '♥', pop(60), RED)
    return c
def letter_sheet(img):  # 5x7 centered on US Letter with crop marks
    W, H = 2550, 3300; p = Image.new('RGB', (W, H), 'white'); x, y = (W - img.width) // 2, (H - img.height) // 2
    p.paste(img, (x, y)); d = ImageDraw.Draw(p); L = 60
    for cx in (x, x + img.width):
        for cy in (y, y + img.height):
            d.line([(cx, cy - L - 20 if cy == y else cy + 20), (cx, cy - 20 if cy == y else cy + L + 20)], fill=(120, 120, 120), width=2)
            d.line([(cx - L - 20 if cx == x else cx + 20, cy), (cx - 20 if cx == x else cx + L + 20, cy)], fill=(120, 120, 120), width=2)
    return p
def card_files(n):
    f, nt, ins = card_front(n), card_front(n, False), card_inside(n)
    b = f"christmas_card_{NAME[n].lower().replace(' & ','_').replace(' ','_')}"
    return {f'{b}_front_5x7.jpg': jpg(f), f'{b}_front_no_text_5x7.jpg': jpg(nt), f'{b}_inside_5x7.jpg': jpg(ins),
            f'{b}_print_on_letter.pdf': pdf([letter_sheet(f), letter_sheet(ins)])}

# ---------- GIFT TAGS (2.5 x 4 in, 6 per letter sheet) ----------
def tag(n, variant):
    W, H = 750, 1200; t = Image.new('RGB', (W, H), CREAM); s = ART[n]
    t.paste(crop(art(n), W - 60, 640), (30, 150))
    d = ImageDraw.Draw(t); d.ellipse([W / 2 - 28, 45, W / 2 + 28, 101], outline=(140, 130, 120), width=4)
    if variant == 'to':
        d.text((70, 835), 'To:', font=play(54), fill=INK); d.line([(170, 885), (W - 70, 885)], fill=GOLD, width=3)
        d.text((70, 950), 'From:', font=play(54), fill=INK); d.line([(230, 1000), (W - 70, 1000)], fill=GOLD, width=3)
        ctext(d, W / 2, 1060, GREET[s], vibes(80), RED if s != 'botanical' else GREEN)
    else:
        ctext(d, W / 2, 860, GREET[s], vibes(118), RED if s != 'botanical' else GREEN)
        d.line([(W / 2 - 110, 1040), (W / 2 + 110, 1040)], fill=GOLD, width=3)
    d.rectangle([0, 0, W - 1, H - 1], outline=(200, 190, 175), width=3)
    return t
def tag_sheet(items):  # items: list of 6 tag images
    W, H = 2550, 3300; p = Image.new('RGB', (W, H), 'white'); gx, gy = (W - 3 * 750) // 2, (H - 2 * 1200) // 2
    for i, im in enumerate(items): p.paste(im, (gx + (i % 3) * 750, gy + (i // 3) * 1200))
    return p
def tag_files(arts, base):
    out = {}; pages = []
    for v in ('to', 'greet'):
        items = [tag(n, v) for n in arts]; items = (items * 6)[:6] if len(arts) < 6 else items[:6]
        if len(arts) == 3: items = [tag(n, v) for n in arts] * 2
        pages.append(tag_sheet(items))
    if len(arts) > 6:  # bundle: one sheet per design pair
        pages = []
        for v in ('to', 'greet'):
            for k in range(0, len(arts), 3):
                grp = arts[k:k + 3]; pages.append(tag_sheet([tag(n, v) for n in grp] * 2))
    out[f'{base}_print_on_letter.pdf'] = pdf(pages)
    for n in arts:
        for v in ('to', 'greet'): out[f'{base}_{NAME[n].lower().replace(" & ","_").replace(" ","_")}_{v}_tag_2.5x4.png'] = None
    # individual PNGs
    files = {}
    for n in arts:
        for v in ('to', 'greet'):
            b = io.BytesIO(); tag(n, v).save(b, 'PNG', dpi=(300, 300)); files[f'{NAME[n].lower().replace(" & ","_").replace(" ","_")}_{v}_tag.png'] = b.getvalue()
    return {f'{base}_print_on_letter.pdf': out[f'{base}_print_on_letter.pdf'], **files}

# ---------- PHONE WALLPAPERS ----------
def wall(n, w, h): return crop(art(n), w, h)
def wallpaper_files(arts):
    files = {}
    for n in arts:
        nm = NAME[n].lower().replace(' & ', '_').replace(' ', '_')
        files[f'{nm}_iphone_1290x2796.jpg'] = jpg(wall(n, 1290, 2796), 92)
        files[f'{nm}_android_1440x3200.jpg'] = jpg(wall(n, 1440, 3200), 92)
    return files

# ---------- LISTING IMAGES (3000x2250) ----------
LW, LH = 3000, 2250
def table_bg(col=(232, 224, 212)):
    bg = Image.new('RGB', (LW, LH), col); d = ImageDraw.Draw(bg)
    for y in range(LH): k = int(14 * y / LH); d.line([(0, y), (LW, y)], fill=tuple(max(0, c - k) for c in col))
    return bg
def drop(bg, im, x, y, rot=0, blur=24, alpha=95):
    if rot: im = im.convert('RGBA').rotate(rot, expand=True, resample=Image.BICUBIC)
    else: im = im.convert('RGBA')
    sh = Image.new('RGBA', (im.width + 120, im.height + 120), (0, 0, 0, 0))
    m = im.split()[3]; sh.paste(Image.new('RGBA', im.size, (0, 0, 0, alpha)), (60, 75), m)
    sh = sh.filter(ImageFilter.GaussianBlur(blur)); bg.paste(sh, (x - 60, y - 60), sh); bg.paste(im, (x, y), im)
def thumb(im, h): return im.resize((int(im.width * h / im.height), h), Image.LANCZOS)
def banner(bg, title, sub):
    d = ImageDraw.Draw(bg); d.rectangle([0, 0, LW, 300], fill=(255, 255, 255))
    ctext(d, LW / 2, 40, title, play(120), INK); ctext(d, LW / 2, 200, sub, pop(58), RED)
def env(w, h, col=(196, 40, 46)):
    e = Image.new('RGB', (w, h), col); d = ImageDraw.Draw(e)
    d.polygon([(0, 0), (w / 2, h * 0.55), (w, 0)], outline=tuple(int(c * 0.8) for c in col), width=6); return e
def card_cover(arts, title, sub):
    bg = table_bg(); fr = [thumb(card_front(n), 1500 if len(arts) == 1 else 1150) for n in arts]
    if len(arts) == 1:
        drop(bg, env(1150, 800), 1500, 1050, rot=-8); drop(bg, fr[0], 520, 470, rot=3)
    else:
        sel = fr[:3] if len(fr) >= 3 else fr; tot = sum(f.width for f in sel) + 90 * (len(sel) - 1); x = (LW - tot) // 2
        for i, f in enumerate(sel): drop(bg, f, x, 560 + (40 if i % 2 else 0), rot=(-3, 2, -2)[i % 3]); x += f.width + 90
    banner(bg, title, sub); return bg
def tag_cover(arts, title, sub):
    bg = table_bg((205, 180, 150)); tags = [thumb(tag(n, v), 760) for n in arts for v in ('to', 'greet')]
    tags = tags[:6] if len(tags) >= 6 else tags; x = 230
    for i, t in enumerate(tags): drop(bg, t, x + i * 430, 560 + (0 if i % 2 else 230), rot=(-6, 4, -3, 5, -5, 3)[i % 6]);
    d = ImageDraw.Draw(bg)
    banner(bg, title, sub); return bg
def phone(n, h=1750):
    sc = thumb(wall(n, 1290, 2796), h - 60); W = sc.width + 60; p = Image.new('RGBA', (W, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(p); d.rounded_rectangle([0, 0, W - 1, h - 1], radius=110, fill=(24, 24, 28))
    m = Image.new('L', sc.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, sc.width - 1, sc.height - 1], radius=85, fill=255)
    p.paste(sc, (30, 30), m); d.rounded_rectangle([W / 2 - 110, 55, W / 2 + 110, 105], radius=25, fill=(10, 10, 12))
    ctext(d, W / 2, 200, '9:41', pop(110, 'Light'), (255, 255, 255)); return p
def wall_cover(arts, title, sub):
    bg = table_bg((226, 218, 232)); ps = [phone(n, 1700 if len(arts) <= 3 else 1500) for n in arts[:3]]
    tot = sum(p.width for p in ps) + 120 * (len(ps) - 1); x = (LW - tot) // 2
    for i, p in enumerate(ps): drop(bg, p, x, 420 + (60 if i % 2 else 0)); x += p.width + 120
    banner(bg, title, sub); return bg
def grid_img(ims, title):
    bg = Image.new('RGB', (LW, LH), (245, 241, 234)); n = len(ims); cols = min(n, 5 if n > 6 else n); rows = (n + cols - 1) // cols
    cw, ch = (LW - 200) / cols, (LH - 420) / rows
    for i, im in enumerate(ims):
        t = im.copy(); t.thumbnail((int(cw * 0.9), int(ch * 0.9))); drop(bg, t, int(100 + (i % cols) * cw + (cw - t.width) / 2), int(360 + (i // cols) * ch + (ch - t.height) / 2), blur=12, alpha=60)
    d = ImageDraw.Draw(bg); ctext(d, LW / 2, 90, title, play(110), INK); return bg
def info_img(title, rows):
    im = Image.new('RGB', (LW, LH), CREAM); d = ImageDraw.Draw(im); ctext(d, LW / 2, 150, title, play(130), INK); y = 470
    for r in rows: d.ellipse([430, y + 32, 470, y + 72], fill=RED); d.text((530, y), r, font=pop(76, 'Regular'), fill=INK); y += 200
    ctext(d, LW / 2, LH - 250, 'Instant digital download · No physical item is shipped', pop(60), GREEN); return im

def write(slug, files, imgs):
    fo = os.path.join(OUT, slug); os.makedirs(fo, exist_ok=True)
    for i, im in enumerate(imgs, 1): im.convert('RGB').save(os.path.join(fo, f'0{i}_img.jpg'), quality=88)
    base = slug.split("_", 1)[1]; parts, cur, sz = [], {}, 0
    for k, v in files.items():
        if cur and sz + len(v) > 18_500_000: parts.append(cur); cur, sz = {}, 0
        cur[k] = v; sz += len(v)
    parts.append(cur)
    for i, pt in enumerate(parts, 1):
        nm = f'{base}.zip' if len(parts) == 1 else f'{base}_part{i}of{len(parts)}.zip'
        with zipfile.ZipFile(os.path.join(fo, nm), 'w', zipfile.ZIP_DEFLATED) as z:
            for k, v in pt.items(): z.writestr(k, v)
    print(slug, len(parts), 'zip(s)', flush=True)

SETS = {'italian': [4, 5, 6], 'cabin': [7, 8, 9], 'botanical': [10, 11, 12]}
SETNAME = {'italian': 'Italian Christmas Kitchen', 'cabin': 'Cozy Winter Cabin', 'botanical': 'Vintage Christmas Botanical'}
if __name__ == '__main__':
    what = sys.argv[2:] or ['cards', 'tags', 'walls']
    ALL = [4, 5, 6, 7, 8, 9, 10, 11, 12]
    if 'cards' in what:
        for n in ALL:
            files = card_files(n); s = ART[n]
            write(f'X1-card{n:02d}_christmas_card_{n:02d}', files,
                  [card_cover([n], 'Printable Christmas Card', f'{NAME[n]} · 5x7 · Instant Download'), thumb(card_front(n), LH).resize((LH * 1500 // 2100, LH)) if False else grid_img([card_front(n), card_inside(n), card_front(n, False)], 'Front, inside & no-text version'),
                   info_img("What you'll receive", ['5x7 card front (with greeting)', '5x7 card front (no text)', '5x7 inside message page', 'Print-ready Letter PDF with crop marks', 'Print at home or at a print shop'])])
        for s, arts in SETS.items():
            files = {}
            for n in arts: files.update(card_files(n))
            write(f'X1-cardset_{s}_christmas_cards_set', files,
                  [card_cover(arts, f'{SETNAME[s]} Christmas Cards', 'Set of 3 · Printable 5x7 · Instant Download'), grid_img([card_front(n) for n in arts] + [card_inside(arts[0])], '3 card designs + inside page'),
                   info_img("What you'll receive", ['3 card designs, 5x7 fronts', 'No-text versions of every front', 'Matching inside message pages', 'Print-ready Letter PDFs with crop marks', 'Print as many as you need'])])
        files = {}
        for n in ALL: files.update(card_files(n))
        write('X1-cardall_christmas_cards_bundle_9', files,
              [card_cover([4, 8, 11], 'Christmas Card Bundle', '9 Printable 5x7 Designs · Instant Download'), grid_img([card_front(n) for n in ALL], 'All 9 card designs'),
               info_img("What you'll receive", ['9 Christmas card designs, 5x7', 'No-text versions of every front', 'Inside message pages', 'Print-ready Letter PDFs with crop marks', 'Print unlimited for your own use'])])
    if 'tags' in what:
        for s, arts in SETS.items():
            write(f'X1-tags_{s}_christmas_gift_tags', tag_files(arts, f'{s}_gift_tags'),
                  [tag_cover(arts, f'{SETNAME[s]} Gift Tags', 'Printable Christmas Tags · Instant Download'), grid_img([tag(n, v) for n in arts for v in ('to', 'greet')], '6 tag designs: To/From + greeting'),
                   tag_sheet([tag(n, 'to') for n in arts] * 2).resize((LH * 2550 // 3300, LH)).crop((0, 0, LH * 2550 // 3300, LH)) if False else info_img("What you'll receive", ['6 tag designs (3 To/From + 3 greeting)', '2.5 x 4 in tags, 6 per Letter sheet', 'Print-ready PDF + individual PNGs', 'Punch a hole and tie with twine', 'Print as many as you need'])])
        write('X1-tagsall_christmas_gift_tags_bundle', tag_files([4, 5, 6, 7, 8, 9, 10, 11, 12], 'christmas_gift_tags_bundle'),
              [tag_cover([4, 8, 11], 'Christmas Gift Tag Bundle', '18 Printable Tag Designs · Instant Download'), grid_img([tag(n, 'to') for n in [4, 5, 6, 7, 8, 9, 10, 11, 12]], '9 artworks, 2 styles each'),
               info_img("What you'll receive", ['18 tag designs (9 To/From + 9 greeting)', '2.5 x 4 in tags, 6 per Letter sheet', 'Print-ready PDF + individual PNGs', 'Punch a hole and tie with twine', 'Print as many as you need'])])
    if 'walls' in what:
        for s, arts in SETS.items():
            write(f'X1-wp_{s}_christmas_phone_wallpaper', wallpaper_files(arts),
                  [wall_cover(arts, f'{SETNAME[s]} Phone Wallpapers', 'Set of 3 · iPhone & Android · Instant Download'), grid_img([wall(n, 1290, 2796) for n in arts], '3 wallpapers, 2 sizes each'),
                   info_img("What you'll receive", ['3 Christmas phone wallpapers', 'iPhone size 1290 x 2796', 'Android size 1440 x 3200', 'Works as lock or home screen', 'Instant download, no app needed'])])
        write('X1-wpall_christmas_phone_wallpaper_bundle_9', wallpaper_files([4, 5, 6, 7, 8, 9, 10, 11, 12]),
              [wall_cover([7, 8, 11], 'Christmas Phone Wallpaper Bundle', '9 Wallpapers · iPhone & Android'), grid_img([wall(n, 1290, 2796) for n in [4, 5, 6, 7, 8, 9, 10, 11, 12]], 'All 9 wallpapers'),
               info_img("What you'll receive", ['9 Christmas phone wallpapers', 'iPhone size 1290 x 2796', 'Android size 1440 x 3200', 'Works as lock or home screen', 'Instant download, no app needed'])])
