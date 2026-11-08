"""Build Etsy-ready listing folders from processed PNGs.
Each listing folder: files_*.zip (<=19MB each, max 5), 01_cover.jpg, 02_all_items.jpg, 03_transparent.jpg, 04_details.jpg, listing.json
Usage: python3 -I package.py SPEC.json OUT_ROOT
"""
import sys, os, json, glob, zipfile, subprocess, shutil, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SPEC, ROOT = sys.argv[1], sys.argv[2]
FD = '/usr/share/fonts/truetype/google-fonts/'
def lora(sz, bold=True):
    f = ImageFont.truetype(FD + 'Lora-Variable.ttf', sz)
    try: f.set_variation_by_name('Bold' if bold else 'Regular')
    except Exception: pass
    return f
def pop(sz, w='Medium'): return ImageFont.truetype(FD + f'Poppins-{w}.ttf', sz)

CREAM, INK, RED, GREEN = (250, 245, 236), (52, 40, 34), (150, 38, 38), (62, 92, 70)
W, H = 3000, 2250  # 4:3 Etsy listing image

def finals(srcs, dst, long_side=3600):
    os.makedirs(dst, exist_ok=True); out = []
    for f in srcs:
        o = os.path.join(dst, os.path.basename(f))
        if not os.path.exists(o):
            im = Image.open(f); s = long_side / max(im.size)
            if s < 1: im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
            tmp = o + '.tmp.png'; im.save(tmp, dpi=(300, 300))
            r = subprocess.run(['pngquant', '--quality=65-95', '--speed', '3', '--strip', '-f', '-o', o, tmp])
            if r.returncode != 0: shutil.copy(tmp, o)
            os.remove(tmp)
            Image.open(o).save(o, dpi=(300, 300), optimize=True) if False else None
        out.append(o)
    return out

def zips(files, folder, base, limit=19_000_000):
    parts, cur, size = [], [], 0
    for f in files:
        s = os.path.getsize(f)
        if cur and size + s > limit: parts.append(cur); cur, size = [], 0
        cur.append(f); size += s
    if cur: parts.append(cur)
    assert len(parts) <= 5, f'{base}: {len(parts)} zip parts > 5'
    names = []
    for i, p in enumerate(parts, 1):
        n = f'{base}_part{i}of{len(parts)}.zip' if len(parts) > 1 else f'{base}.zip'
        with zipfile.ZipFile(os.path.join(folder, n), 'w', zipfile.ZIP_STORED) as z:
            for f in p: z.write(f, os.path.basename(f))
        names.append(n)
    return names

def grid(files, box, bg=None, checker=False):
    x0, y0, x1, y1 = box; n = len(files)
    cols = min(n, 6 if n > 12 else 4 if n > 6 else max(1, n))
    if n in (5, 6): cols = 3
    rows = math.ceil(n / cols)
    cw, ch = (x1 - x0) / cols, (y1 - y0) / rows
    layer = Image.new('RGBA', (x1 - x0, y1 - y0), (0, 0, 0, 0))
    for i, f in enumerate(files):
        im = Image.open(f).convert('RGBA'); im.thumbnail((int(cw * 0.88), int(ch * 0.88)), Image.LANCZOS)
        cx, cy = (i % cols) * cw + cw / 2, (i // cols) * ch + ch / 2
        if n % cols and i // cols == rows - 1:  # center the last row
            cx += (cols - n % cols) * cw / 2
        layer.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))
    return layer

def checker(size, s=60):
    im = Image.new('RGB', size, (255, 255, 255)); d = ImageDraw.Draw(im)
    for y in range(0, size[1], s):
        for x in range(0, size[0], s):
            if (x // s + y // s) % 2: d.rectangle([x, y, x + s - 1, y + s - 1], fill=(228, 228, 228))
    return im

def centered(d, y, text, font, fill):
    w = d.textlength(text, font=font); d.text(((W - w) / 2, y), text, font=font, fill=fill)

def cover(files, sp, path):
    im = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(im)
    d.rectangle([40, 40, W - 41, H - 41], outline=GREEN, width=6)
    if sp['kind'] == 'coloring':
        pages = [Image.open(f).convert('RGB') for f in files[:5]]
        for i, p in enumerate(pages):
            p.thumbnail((700, 905)); sh = Image.new('RGBA', (p.width + 30, p.height + 30), (0, 0, 0, 0))
            ImageDraw.Draw(sh).rectangle([15, 15, p.width + 15, p.height + 15], fill=(0, 0, 0, 70))
            sh = sh.filter(ImageFilter.GaussianBlur(10))
            x = 110 + i * 520; y = 700 + (0 if i % 2 else 60)
            im.paste(sh, (x - 5, y + 5), sh); im.paste(p, (x, y))
    else:
        g = grid(files[:12] if len(files) > 12 else files, (180, 640, W - 180, H - 230))
        im.paste(g, (180, 640), g)
    centered(d, 120, sp['cover_title'], lora(150), INK)
    centered(d, 330, sp['cover_sub'], pop(78, 'Medium'), RED)
    centered(d, 450, sp['cover_badge'], pop(60, 'Regular'), GREEN)
    centered(d, H - 190, sp['cover_foot'], pop(60, 'Medium'), INK)
    im.save(path, quality=90)

def all_items(files, sp, path):
    if sp['kind'] == 'coloring':
        im = Image.new('RGB', (W, H), (236, 236, 236)); d = ImageDraw.Draw(im)
        n = len(files); cols = n if n <= 5 else math.ceil(n / 2) if n <= 12 else math.ceil(n / 3); rows = math.ceil(n / cols)
        cw, ch = (W - 200) / cols, (H - 360) / rows
        for i, f in enumerate(files):
            p = Image.open(f).convert('RGB'); p.thumbnail((int(cw * 0.9), int(ch * 0.9)))
            im.paste(p, (int(100 + (i % cols) * cw + (cw - p.width) / 2), int(260 + (i // cols) * ch + (ch - p.height) / 2)))
        centered(d, 90, f"All {n} pages included", lora(110), INK)
    else:
        im = Image.new('RGB', (W, H), (255, 255, 255)); d = ImageDraw.Draw(im)
        g = grid(files, (120, 300, W - 120, H - 80)); im.paste(g, (120, 300), g)
        centered(d, 90, f"All {len(files)} designs included", lora(110), INK)
    im.save(path, quality=90)

def transparent(files, sp, path):
    if sp['kind'] == 'coloring':
        f = files[0]; p = Image.open(f).convert('RGB'); im = Image.new('RGB', (W, H), (60, 70, 66))
        p.thumbnail((1500, 1940)); im.paste(p, ((W - p.width) // 2, (H - p.height) // 2))
        d = ImageDraw.Draw(im); d.text((120, 120), "Crisp 300 DPI line art", font=lora(90), fill=(255, 255, 255))
    else:
        im = checker((W, H)); pick = files[:3]
        g = grid(pick, (150, 380, W - 150, H - 150)); im.paste(g, (150, 380), g)
        d = ImageDraw.Draw(im); centered(d, 120, "Transparent background PNG", lora(110), INK)
    im.save(path, quality=90)

def details(sp, path):
    im = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(im)
    centered(d, 150, "What you'll receive", lora(130), INK)
    y = 470
    for line in sp['details']:
        d.ellipse([480, y + 30, 520, y + 70], fill=RED)
        d.text((580, y), line, font=pop(80, 'Regular'), fill=INK); y += 190
    centered(d, H - 260, "Instant digital download · No physical item is shipped", pop(62, 'Medium'), GREEN)
    im.save(path, quality=90)

spec = json.load(open(SPEC))
for sp in spec['listings']:
    if os.path.exists(os.path.join(ROOT, sp['slug'], 'listing.json')): print('skip', sp['slug']); continue
    folder = os.path.join(ROOT, sp['slug']); os.makedirs(folder, exist_ok=True)
    srcs = []
    for pat in sp['files']: srcs += sorted(glob.glob(pat))
    if sp['kind'] == 'coloring':
        fl = srcs  # already final print files (png pages + pdfs)
        preview = [f for f in srcs if f.endswith('_letter.png')]
        deliver = [f for f in srcs if f.endswith('.pdf')] if sp.get('pdf_only') else srcs
    else:
        ls_ = sp.get('long_side', 3600); fl = finals(srcs, os.path.join(ROOT, '_finals', f"{sp['set']}_{ls_}"), ls_)
        preview = fl; deliver = fl
    names = zips(deliver, folder, sp['zipbase'])
    cover(preview, sp, os.path.join(folder, '01_cover.jpg'))
    all_items(preview, sp, os.path.join(folder, '02_all_items.jpg'))
    transparent(preview, sp, os.path.join(folder, '03_preview.jpg'))
    details(sp, os.path.join(folder, '04_details.jpg'))
    json.dump({k: sp[k] for k in ('title', 'price', 'tags', 'description', 'category_hint')} | {'files': names},
              open(os.path.join(folder, 'listing.json'), 'w'), indent=2)
    print(sp['slug'], names, flush=True)
