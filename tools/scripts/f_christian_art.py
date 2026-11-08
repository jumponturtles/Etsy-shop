"""Christian Bible verse wall art pack of 10 (F01). Usage: python3 -I f_christian_art.py OUT_ROOT"""
import sys, os, io, zipfile, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter
Image.MAX_IMAGE_PIXELS = None
OUT = sys.argv[1]; sys.argv = [sys.argv[0], OUT]
sys.path.insert(0, '/home/claude/scripts')
import xmas_products as X
SRC = '/home/claude/F01/up/'
F = '/home/claude/fonts/'
def play(s, w='Regular', italic=False):
    f = ImageFont.truetype(F + 'PlayfairDisplay.ttf', s)
    try: f.set_variation_by_name(w)
    except Exception: pass
    return f
def cinzel(s):
    f = ImageFont.truetype(F + 'Cinzel.ttf', s)
    try: f.set_variation_by_name('SemiBold')
    except Exception: pass
    return f
INK, CREAM = (52, 42, 36), (250, 244, 232)
V = {  # n: (verse, reference, position, color, short name)
 1: ('The Lord is my shepherd;\nI shall not want.', 'PSALM 23:1', 'top', INK, 'Psalm 23 Still Waters'),
 2: ('Be still, and know\nthat I am God.', 'PSALM 46:10', 'top', INK, 'Be Still Olive Branch'),
 3: ('Behold the fowls of the air...\nyour heavenly Father\nfeedeth them.', 'MATTHEW 6:26', 'top', INK, 'Birds of the Air'),
 4: ('But the fruit of the Spirit\nis love, joy, peace.', 'GALATIANS 5:22', 'top', CREAM, 'Fruit of the Spirit'),
 5: ('Peace, be still.', 'MARK 4:39', 'top', INK, 'Peace Be Still'),
 6: ('This is the day which\nthe Lord hath made; we will\nrejoice and be glad in it.', 'PSALM 118:24', 'bottom', INK, 'This Is the Day'),
 7: ('Trust in the Lord\nwith all thine heart.', 'PROVERBS 3:5', 'top', INK, 'Lion and Lamb'),
 8: ('Consider the lilies\nof the field, how they grow.', 'MATTHEW 6:28', 'bottom', INK, 'Consider the Lilies'),
 9: ('I will lift up mine eyes\nunto the hills, from whence\ncometh my help.', 'PSALM 121:1', 'top', INK, 'Lift Up Mine Eyes'),
 10: ('Thy word is a lamp unto my feet,\nand a light unto my path.', 'PSALM 119:105', 'top', INK, 'Lamp Unto My Feet'),
}
def print_(n, W=3600, H=5400):
    a = X.crop(Image.open(f'{SRC}art_{n:02d}.png').convert('RGB'), W, H); verse, ref, pos, col, _ = V[n]
    lines = verse.split('\n'); sz = int(W * 0.085)
    while True:
        f = play(sz); d0 = ImageDraw.Draw(a)
        if max(d0.textlength(l, font=f) for l in lines) <= W * 0.88: break
        sz -= 8
    lh = int(sz * 1.32); block = lh * len(lines) + int(sz * 0.9)
    y0 = int(H * 0.07) if pos == 'top' else int(H * 0.93) - block
    # soft full-width fade behind the text area
    sc = Image.new('L', (W, H), 0); sd = ImageDraw.Draw(sc)
    top, bot = int(y0 - sz * 1.2), int(y0 + block + sz * 0.9)
    for yy in range(max(0, top), min(H, bot)):
        t = min(1, (yy - top) / (sz * 1.2), (bot - yy) / (sz * 0.9)); sd.line([(0, yy), (W, yy)], fill=int(95 * max(0, t)))
    sc = sc.filter(ImageFilter.GaussianBlur(40)); tint = Image.new('RGB', (W, H), (255, 250, 240) if col == INK else (18, 12, 8)); a.paste(tint, (0, 0), sc)
    d = ImageDraw.Draw(a); y = y0
    for l in lines: X.ctext(d, W / 2, y, l, f, col); y += lh
    rf = cinzel(int(sz * 0.5)); X.ctext(d, W / 2, y + sz * 0.25, ref, rf, col)
    return a
RAT = [('2x3', 3600, 5400, '2x3 ratio: 4x6, 8x12, 12x18, 16x24, 24x36 in'), ('4x5', 3600, 4500, '4x5 ratio: 8x10, 16x20 in'), ('ISO', 3508, 4961, 'ISO: A5, A4, A3, A2')]
def sname(n): return V[n][4].lower().replace(' ', '_')
if __name__ == '__main__':
    files = {}; prev = []
    for n in range(1, 11):
        base = print_(n); prev.append(base)
        for k, w, h, _ in RAT:
            im = base if k == '2x3' else print_(n, w, h)
            b = io.BytesIO(); im.save(b, 'JPEG', quality=86, dpi=(300, 300)); files[f'{k}/{n:02d}_{sname(n)}_{k}.jpg'] = b.getvalue()
        print('ok', n, flush=True)
    imgs = []
    # cover: 3 framed prints on a wall
    bg = X.table_bg((228, 222, 210)); fr = [X.thumb(prev[i], 1300) for i in (0, 6, 9)]
    fr = [Image.new('RGB', (f.width + 60, f.height + 60), (44, 36, 30)) for f in fr], fr
    frames, arts = fr; gap = (3000 - sum(f.width for f in frames)) // 4; x = gap
    for fm, ar in zip(frames, arts): fm.paste(ar, (30, 30)); X.drop(bg, fm, x, 520); x += fm.width + gap
    X.banner(bg, 'Bible Verse Wall Art Set of 10', 'Printable Christian Prints · All Different · Instant Download'); imgs.append(bg)
    imgs.append(X.grid_img(prev, '10 different scripture prints in one download'))
    bg = X.table_bg((236, 230, 220)); fr = [X.thumb(prev[i], 1300) for i in (3, 5, 8)]; gap = (3000 - sum(f.width for f in fr)) // 4; x = gap
    for f in fr: X.drop(bg, f, x, 520); x += f.width + gap
    X.banner(bg, 'Vintage, Boho & Minimal Styles', 'Psalm 23 · Be Still · Proverbs 3:5 · Psalm 121 · and more'); imgs.append(bg)
    imgs.append(X.info_img("What you'll receive", ['10 Bible verse prints, all different', '3 ratios: 2x3, 4x5 and ISO (A-sizes)', 'Prints up to 24x36 in, 300 DPI JPG', 'KJV scripture, beautifully lettered', 'Print at home or at a print shop']))
    X.write('F01-christian_bible_verse_wall_art_10', files, imgs)
