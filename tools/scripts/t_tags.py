"""10 printable Christmas gift tag sets (T03). Usage: python3 -I t_tags.py OUT_ROOT"""
import sys, os, io
from PIL import Image, ImageDraw
OUT = sys.argv[1]; sys.argv = [sys.argv[0], OUT]
sys.path.insert(0, '/home/claude/scripts')
import xmas_products as X
SRC = '/home/claude/T03/up/'
INK, RED, GOLD, GREEN = (52, 40, 34), (160, 34, 40), (214, 178, 96), (40, 80, 56)
T = {1: ('Watercolor Tree', 'Merry Christmas', RED), 2: ('Vintage Santa', 'Ho Ho Ho!', RED), 3: ('Buffalo Plaid & Kraft', 'Merry Christmas', RED),
     4: ('Nutcracker', 'Merry & Bright', RED), 5: ('Woodland Fox', 'Happy Holidays', GREEN), 6: ('Gingerbread Man', 'Sweet Christmas', (150, 70, 30)),
     7: ('Emerald & Gold', "Season's Greetings", GOLD), 8: ('Red Truck', 'Home for the Holidays', RED), 9: ('Scandinavian Reindeer', 'God Jul', RED),
     10: ('Mid-Century Ornaments', 'Happy Holidays', (196, 80, 60))}
def tag(n, v):
    W, H = 750, 1200; t = X.crop(Image.open(f'{SRC}tag_{n:02d}.png').convert('RGB'), W, H); d = ImageDraw.Draw(t)
    name, g, col = T[n]; ink = GOLD if n == 7 else INK; line = GOLD if n == 7 else (120, 100, 80)
    if v == 'to':
        d.text((70, 850), 'To:', font=X.play(58), fill=ink); d.line([(180, 905), (W - 70, 905)], fill=line, width=4)
        d.text((70, 975), 'From:', font=X.play(58), fill=ink); d.line([(250, 1030), (W - 70, 1030)], fill=line, width=4)
    else:
        sz = 130
        while d.textlength(g, font=X.vibes(sz)) > W - 110: sz -= 6
        X.ctext(d, W / 2, 900, g, X.vibes(sz), col)
    d.ellipse([W / 2 - 26, 40, W / 2 + 26, 92], fill=(255, 255, 255), outline=(150, 140, 130), width=4)
    d.rectangle([0, 0, W - 1, H - 1], outline=(200, 190, 175), width=3); return t
def sname(n): return T[n][0].lower().replace(' & ', '_').replace(' ', '_').replace('-', '_')
if __name__ == '__main__':
    files = {}; pages = []
    for n in range(1, 11):
        a, b = tag(n, 'to'), tag(n, 'greet')
        for v, im in (('to_from', a), ('greeting', b)):
            bb = io.BytesIO(); im.save(bb, 'PNG', dpi=(300, 300)); files[f'individual_tags_png/{n:02d}_{sname(n)}_{v}.png'] = bb.getvalue()
        sheet = X.tag_sheet([a, a, a, b, b, b]); pages.append(sheet)
        files[f'print_sheets_letter/{n:02d}_{sname(n)}_sheet.pdf'] = X.pdf([sheet])
    files['print_all_10_sets_letter.pdf'] = X.pdf(pages)
    prev = [tag(n, v) for n in range(1, 11) for v in ('greet',)]
    bg = X.table_bg((205, 180, 150)); sel = [X.thumb(tag(n, v), 760) for n, v in ((2, 'greet'), (4, 'to'), (5, 'greet'), (8, 'to'), (7, 'greet'), (9, 'to'))]
    gap = (3000 - 6 * sel[0].width) // 7
    for i, t in enumerate(sel): X.drop(bg, t, gap + i * (t.width + gap), 600 + (0 if i % 2 else 230), rot=(-4, 3, -2, 4, -3, 2)[i])
    X.banner(bg, 'Christmas Gift Tags · 10 Sets', 'Printable Tags · 10 Different Styles · Instant Download')
    imgs = [bg, X.grid_img(prev, '10 different tag designs'), X.grid_img([tag(n, 'to') for n in range(1, 11)], 'Every design also comes as a To / From tag'),
            X.info_img("What you'll receive", ['10 tag designs x 2 styles = 20 tags', 'To/From + greeting version of each', '2.5 x 4 in, 6 per Letter sheet (PDF)', 'Individual 300 DPI PNGs too', 'Print, cut, punch & tie'])]
    X.write('T03-christmas_gift_tags_10_sets', files, imgs)
