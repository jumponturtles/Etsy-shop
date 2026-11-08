"""Printable Christmas card packs of 10 (K01). Usage: python3 -I k_cards.py OUT_ROOT"""
import sys, os, io, zipfile
from PIL import Image, ImageDraw, ImageFilter
Image.MAX_IMAGE_PIXELS = None
sys.path.insert(0, '/home/claude/scripts')
import xmas_products as X
OUT = sys.argv[1]; SRC = '/home/claude/K01/up/'
CREAM, INK, RED, GREEN, GOLD, NAVY, WHITE = X.CREAM, X.INK, X.RED, X.GREEN, X.GOLD, (30, 42, 78), (255, 255, 255)
# card: (file, short name, greeting, font, color, band color or None for overlay-on-art, inside message)
C = {
 1: ('Watercolor Wreath', 'Merry Christmas', 'vibes', RED, CREAM, 'Wishing you love, peace and joy\nthis Christmas and always.'),
 2: ('Vintage Santa', 'Merry Christmas', 'play', RED, CREAM, 'Wishing you a jolly Christmas\nand a Happy New Year!'),
 3: ('Mid-Century Trees', 'Happy Holidays', 'play', (196, 62, 44), CREAM, 'Wishing you a bright and\nhappy holiday season.'),
 4: ('Minimal Pine & Gold', "Season's Greetings", 'vibes', (150, 112, 48), CREAM, 'Warmest wishes for a peaceful\nholiday and a joyful New Year.'),
 5: ('Gingerbread House', 'Sweet Christmas Wishes', 'vibes', RED, CREAM, 'Wishing you a Christmas as sweet\nas a gingerbread house!'),
 6: ('Snowy Village', 'Silent Night', 'vibes', NAVY, CREAM, 'May the peace of this holy season\nfill your home with light.'),
 7: ('Buffalo Plaid', 'Merry Christmas', 'vibes', RED, CREAM, 'Wishing you a cozy Christmas\nfilled with family and fun.'),
 8: ('Candy Stripe Bow', 'Merry & Bright', 'play', RED, CREAM, 'Wishing you the merriest\nChristmas and a bright New Year!'),
 9: ('Watercolor Nutcracker', 'Merry Christmas', 'vibes', RED, CREAM, 'Wishing you a magical Christmas\nand a wonderful New Year.'),
 10: ('Cheerful Snowman', 'Let It Snow', 'vibes', RED, CREAM, 'Wishing you a snow-much-fun\nChristmas and a happy New Year!'),
 11: ('Boho Trees', 'Happy Holidays', 'vibes', (176, 98, 66), CREAM, 'Wishing you a calm and cozy\nholiday season.'),
 12: ('Kitten in a Stocking', 'Meowy Christmas', 'vibes', RED, CREAM, 'Wishing you a purr-fectly\ncozy Christmas!'),
 13: ('Woodland Friends', 'Merry Christmas', 'vibes', GREEN, CREAM, 'Wishing you a Christmas full of\nwonder and woodland magic.'),
 14: ('Nativity', 'O Holy Night', 'vibes', GOLD, NAVY, 'For unto us a Child is born.\nWishing you a blessed Christmas.'),
 15: ('Scandinavian Folk', 'God Jul', 'play', RED, CREAM, 'Merry Christmas! Wishing you\na warm and hygge holiday season.'),
 16: ('Navy & Gold Ornaments', "Season's Greetings", 'vibes', GOLD, NAVY, 'Wishing you an elegant holiday\nseason and a sparkling New Year.'),
 17: ('Penguin Family', 'Merry Christmas', 'vibes', (52, 96, 140), CREAM, 'Wishing you a cozy Christmas\nwith the ones you love.'),
 18: ('Retro Pink Christmas', 'Merry & Bright', 'vibes', (196, 70, 120), (253, 236, 240), 'Wishing you the prettiest, merriest\nChristmas ever!'),
 19: ('Hot Cocoa', 'Warm Winter Wishes', 'vibes', RED, CREAM, 'Wishing you a cozy Christmas\nfull of warm moments.'),
 20: ('Holly & Mistletoe', "Season's Greetings", 'vibes', GREEN, CREAM, 'Wishing you peace, joy and every\nblessing of the season.'),
}
PACKS = {'classic': [1, 2, 5, 6, 9, 10, 12, 13, 16, 19], 'modern': [3, 4, 7, 8, 11, 14, 15, 17, 18, 20]}
def art(n): return Image.open(f'{SRC}card_{n:02d}.png').convert('RGB')
def front(n, text=True):
    W, H = 1500, 2100; name, g, f, col, band, _ = C[n]; a = art(n)
    if not text: return X.crop(a, W, H)
    sz = 185 if f == 'vibes' else 124
    while True:
        font = X.vibes(sz) if f == 'vibes' else X.play(sz)
        if ImageDraw.Draw(Image.new('RGB', (1, 1))).textlength(g, font=font) <= W - 200: break
        sz -= 6
    if band is None:  # greeting over the calm lower area of the art, with a soft white glow
        c = X.crop(a, W, H); d = ImageDraw.Draw(c); w = d.textlength(g, font=font)
        glow = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(glow).text(((W - w) / 2, H - 400), g, font=font, fill=(255, 255, 255, 230))
        glow = glow.filter(ImageFilter.GaussianBlur(14)); c.paste(glow, (0, 0), glow); c.paste(glow, (0, 0), glow)
        d = ImageDraw.Draw(c); d.text(((W - w) / 2, H - 400), g, font=font, fill=col); return c
    c = Image.new('RGB', (W, H), band); bh = 400
    c.paste(X.crop(a, W - 120, H - bh - 60), (60, 60)); d = ImageDraw.Draw(c)
    X.ctext(d, W / 2, H - bh + (55 if f == 'vibes' else 110), g, font, col)
    return c
def inside(n):
    W, H = 1500, 2100; c = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(c); y = 840
    for line in C[n][5].split('\n'): X.ctext(d, W / 2, y, line, X.play(62, 'Regular'), INK); y += 100
    X.ctext(d, W / 2, y + 70, '— with love —', X.vibes(80), C[n][3] if C[n][3] != GOLD else RED); return c
def slugname(n): return C[n][0].lower().replace(' & ', '_').replace(' ', '_').replace('-', '_')
def files_for(ns):
    fl = {}
    for i, n in enumerate(ns, 1):
        fr, nt, ins = front(n), front(n, False), inside(n); b = f'{i:02d}_{slugname(n)}'
        fl[f'5x7_card_fronts/{b}_front.jpg'] = X.jpg(fr); fl[f'5x7_no_text_fronts/{b}_front_no_text.jpg'] = X.jpg(nt)
        fl[f'5x7_inside_pages/{b}_inside.jpg'] = X.jpg(ins)
    pages = []
    for n in ns: pages += [X.letter_sheet(front(n)), X.letter_sheet(inside(n))]
    fl['print_all_cards_on_letter_paper.pdf'] = X.pdf(pages)
    return fl
def cover(ns, title, sub):
    bg = X.table_bg(); picks = ns[:3]; fr = [X.thumb(front(n), 1330) for n in picks]
    gap = (3000 - 3 * fr[0].width) // 4; rots = [-4, 0, 4]
    for i, f in enumerate(fr): X.drop(bg, f, gap + i * (f.width + gap) - 40, 520 + (0 if i == 1 else 60), rot=rots[i])
    X.banner(bg, title, sub); return bg
def grid10(ns, title):
    return X.grid_img([front(n) for n in ns], title)
def trio(n):
    return X.grid_img([front(n), inside(n), front(n, False)], 'Every card: front, inside page & no-text version')
if __name__ == '__main__':
    meta = {'classic': ('Classic & Cozy Christmas Cards', '10 Printable 5x7 Cards · All Different · Instant Download'),
            'modern': ('Modern & Boho Christmas Cards', '10 Printable 5x7 Cards · All Different · Instant Download')}
    for key, ns in PACKS.items():
        imgs = [cover(ns, *meta[key]), grid10(ns, '10 different card designs in one download'), trio(ns[0]),
                X.info_img("What you'll receive", ['10 Christmas card designs, 5x7 in', '10 matching inside message pages', 'No-text versions of every front', 'One print-ready PDF with crop marks', 'Print as many as you like'])]
        X.write(f'K01-{key}_christmas_cards_10_pack', files_for(ns), imgs)
