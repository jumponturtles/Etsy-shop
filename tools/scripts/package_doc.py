"""Package a multi-page printable PDF product into Etsy listings (bundle + single-page spin-offs).
Usage: python3 -I package_doc.py SPEC.json OUT_ROOT
SPEC: {"letter": path, "a4": path, "listings": [{slug, pages:[1-based], title, price, tags, desc, cover_title, cover_sub, zipbase}]}
"""
import sys, os, json, zipfile, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pdf2image import convert_from_path
from pypdf import PdfReader, PdfWriter

spec = json.load(open(sys.argv[1])); ROOT = sys.argv[2]
FD = '/usr/share/fonts/truetype/google-fonts/'
def lora(s):
    f = ImageFont.truetype(FD + 'Lora-Variable.ttf', s)
    try: f.set_variation_by_name('Bold')
    except Exception: pass
    return f
def pop(s, w='Medium'): return ImageFont.truetype(FD + f'Poppins-{w}.ttf', s)
CREAM, INK, RED, GREEN, GOLD = (250, 245, 236), (52, 40, 34), (160, 48, 48), (46, 84, 66), (196, 150, 72)
W, H = 3000, 2250
pages = convert_from_path(spec['letter'], dpi=200)

def shadowed(p, mw, mh):
    p = p.copy(); p.thumbnail((mw, mh))
    sh = Image.new('RGBA', (p.width + 60, p.height + 60), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle([30, 30, p.width + 30, p.height + 30], fill=(0, 0, 0, 80))
    return p, sh.filter(ImageFilter.GaussianBlur(14))

def centered(d, y, t, f, fill):
    d.text(((W - d.textlength(t, font=f)) / 2, y), t, font=f, fill=fill)

def cover(sel, sp, path):
    im = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(im)
    d.rectangle([40, 40, W - 41, H - 41], outline=GREEN, width=6)
    show = sel[:5] if len(sel) >= 5 else sel
    n = len(show); ph = 1560 if n > 1 else 1640; pw = int(ph * 8.5 / 11)
    step = min((2720 - pw) / max(n - 1, 1), pw * 0.82) if n > 1 else 0
    total = pw + step * (n - 1); x0 = (W - total) / 2
    for i, idx in reversed(list(enumerate(show))):
        p, sh = shadowed(pages[idx - 1], pw, ph)
        x = int(x0 + i * step); y = 560 + (0 if i % 2 else 30)
        im.paste(sh, (x - 25, y - 15), sh); im.paste(p, (x, y))
    centered(d, 110, sp['cover_title'], lora(140), INK)
    centered(d, 310, sp['cover_sub'], pop(76), RED)
    centered(d, 430, 'PRINTABLE PDF · US LETTER & A4 · INSTANT DOWNLOAD', pop(54, 'Regular'), GREEN)
    im.save(path, quality=90)

def grid(sel, sp, path):
    im = Image.new('RGB', (W, H), (234, 230, 222)); d = ImageDraw.Draw(im)
    n = len(sel); cols = min(n, 7 if n > 10 else 5 if n > 4 else n); rows = math.ceil(n / cols)
    cw, ch = (W - 160) / cols, (H - 330) / rows
    for i, idx in enumerate(sel):
        p = pages[idx - 1].copy(); p.thumbnail((int(cw * 0.9), int(ch * 0.9)))
        im.paste(p, (int(80 + (i % cols) * cw + (cw - p.width) / 2), int(250 + (i // cols) * ch + (ch - p.height) / 2)))
    centered(d, 80, f"{n} printable page{'s' if n > 1 else ''} included", lora(110), INK)
    im.save(path, quality=90)

def closeups(sel, path_a, path_b):
    for k, path in enumerate([path_a, path_b]):
        idx = sel[min(k * max(len(sel) // 2, 1), len(sel) - 1)] if len(sel) > 1 else sel[0]
        im = Image.new('RGB', (W, H), (60, 70, 66))
        p, sh = shadowed(pages[idx - 1], 1600, 2050)
        x, y = (W - p.width) // 2, (H - p.height) // 2
        im.paste(sh, (x - 25, y - 15), sh); im.paste(p, (x, y)); im.save(path, quality=90)

def details(sp, n, path):
    im = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(im)
    centered(d, 150, "What you'll receive", lora(130), INK)
    lines = [f'{n} page{"s" if n > 1 else ""} · PDF', 'US Letter (8.5 x 11 in)', 'A4 (210 x 297 mm)', 'Print at home or at a print shop', 'Print as many copies as you need']
    y = 470
    for t in lines:
        d.ellipse([560, y + 30, 600, y + 70], fill=RED); d.text((660, y), t, font=pop(80, 'Regular'), fill=INK); y += 190
    centered(d, H - 260, 'Instant digital download · No physical item is shipped', pop(62), GREEN)
    im.save(path, quality=90)

def subset(src, sel, out):
    r = PdfReader(src); w = PdfWriter()
    for i in sel: w.add_page(r.pages[i - 1])
    with open(out, 'wb') as f: w.write(f)

for sp in spec['listings']:
    folder = os.path.join(ROOT, sp['slug']); os.makedirs(folder, exist_ok=True)
    sel = sp['pages']
    lp, ap = os.path.join(folder, sp['zipbase'] + '_letter.pdf'), os.path.join(folder, sp['zipbase'] + '_a4.pdf')
    subset(spec['letter'], sel, lp); subset(spec['a4'], sel, ap)
    z = os.path.join(folder, sp['zipbase'] + '.zip')
    with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(lp, os.path.basename(lp)); zf.write(ap, os.path.basename(ap))
    os.remove(lp); os.remove(ap)
    cover(sel, sp, os.path.join(folder, '01_cover.jpg'))
    grid(sel, sp, os.path.join(folder, '02_all_items.jpg'))
    closeups(sel, os.path.join(folder, '03_preview.jpg'), os.path.join(folder, '04_preview2.jpg'))
    details(sp, len(sel), os.path.join(folder, '05_details.jpg'))
    json.dump({k: sp[k] for k in ('title', 'price', 'tags', 'desc')}, open(os.path.join(folder, 'listing.json'), 'w'), indent=1)
    print(sp['slug'], os.path.getsize(z) // 1024, 'KB')
