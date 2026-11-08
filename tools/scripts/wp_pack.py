"""Phone wallpaper pack of 10. Usage: python3 -I wp_pack.py SRC_DIR OUT_ROOT SLUG TITLE SUB"""
import sys, os, glob
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, '/home/claude/scripts')
import xmas_products as X
SRC, OUT, SLUG, TITLE, SUB = sys.argv[1:6]
def fill(im, W, H):
    bg = X.crop(im, W, H).filter(ImageFilter.GaussianBlur(60))
    s = W / im.width; fg = im.resize((W, int(im.height * s)), Image.LANCZOS)
    if fg.height > H: return X.crop(im, W, H)
    y = (H - fg.height) // 2; m = Image.new('L', fg.size, 255); d = ImageDraw.Draw(m); f = 160
    for i in range(f): a = int(255 * i / f); d.line([(0, i), (fg.width, i)], fill=a); d.line([(0, fg.height - 1 - i), (fg.width, fg.height - 1 - i)], fill=a)
    bg.paste(fg, (0, y), m); return bg
fs = sorted(glob.glob(os.path.join(SRC, '*.png')))
files = {}; prev = []
for i, f in enumerate(fs, 1):
    im = Image.open(f).convert('RGB'); n = os.path.splitext(os.path.basename(f))[0].replace('wall_', 'wallpaper_')
    ip = fill(im, 1290, 2796); an = fill(im, 1440, 3200); prev.append(ip)
    files[f'iPhone_1290x2796/{n}_iphone.jpg'] = X.jpg(ip, 92); files[f'Android_1440x3200/{n}_android.jpg'] = X.jpg(an, 92)
X.wall = lambda n, w, h: prev[n] if isinstance(n, int) else n
def phone(img, h=1700):
    sc = X.thumb(img, h - 60); W = sc.width + 60; p = Image.new('RGBA', (W, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(p); d.rounded_rectangle([0, 0, W - 1, h - 1], radius=110, fill=(24, 24, 28))
    m = Image.new('L', sc.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, sc.width - 1, sc.height - 1], radius=85, fill=255)
    p.paste(sc, (30, 30), m); d.rounded_rectangle([W / 2 - 110, 55, W / 2 + 110, 105], radius=25, fill=(10, 10, 12))
    X.ctext(d, W / 2, 190, '9:41', X.pop(110, 'Light'), (255, 255, 255)); return p
def cover(idx):
    bg = X.table_bg((226, 218, 232)); ps = [phone(prev[i], 1650) for i in idx]
    gap = (3000 - sum(p.width for p in ps)) // (len(ps) + 1); x = gap
    for k, p in enumerate(ps): X.drop(bg, p, x, 440 + (50 if k % 2 else 0)); x += p.width + gap
    X.banner(bg, TITLE, SUB); return bg
imgs = [cover([0, 3, 5, 8]) if len(prev) >= 9 else cover([0, 1, 2]), X.grid_img(prev, f'All {len(prev)} wallpapers, every one a different style'), cover([2, 4, 6, 9]) if len(prev) >= 10 else cover([0, 1, 2]),
        X.info_img("What you'll receive", [f'{len(prev)} phone wallpapers, all different', 'iPhone size 1290 x 2796', 'Android size 1440 x 3200', 'Lock screen & home screen ready', 'Instant download, no app needed'])]
X.write(SLUG, files, imgs)
