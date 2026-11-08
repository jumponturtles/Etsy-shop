"""Add KJV verses as outlined (colorable) lettering into the empty banners/frames of C08 pages."""
import os
from PIL import Image, ImageDraw, ImageFont
F = '/home/claude/fonts/'
def font(name, s, var):
    f = ImageFont.truetype(F + name, s)
    try: f.set_variation_by_name(var)
    except Exception: pass
    return f
# n: (lines, reference, box (x0,y0,x1,y1) as fractions)
P = {
 1: (['I can do all things', 'through Christ which', 'strengtheneth me.'], 'PHILIPPIANS 4:13', (0.27, 0.33, 0.73, 0.62)),
 2: (['Thy word is', 'a lamp unto', 'my feet,', '', 'and a light', 'unto my', 'path.'], 'PSALM 119:105', None),
 3: (['The Lord is my shepherd'], 'PSALM 23:1', (0.24, 0.055, 0.76, 0.125)),
 4: (['For God so loved the world'], 'JOHN 3:16', (0.17, 0.80, 0.83, 0.885)),
 5: (['Peace I leave with you,', 'my peace I give unto you.'], 'JOHN 14:27', (0.13, 0.705, 0.87, 0.825)),
 6: (['Be strong and of a good courage'], 'JOSHUA 1:9', (0.17, 0.81, 0.83, 0.895)),
 7: (['Ye are the light of the world'], 'MATTHEW 5:14', (0.25, 0.085, 0.75, 0.155)),
 8: (['The fruit of the Spirit is love'], 'GALATIANS 5:22', (0.22, 0.075, 0.78, 0.15)),
 9: (['Consider the lilies', 'of the field,', 'how they grow.'], 'MATTHEW 6:28', (0.27, 0.42, 0.73, 0.63)),
 10: (['Faith as a grain of mustard seed'], 'MATTHEW 17:20', (0.19, 0.815, 0.81, 0.895)),
}
def wraps(text, n):
    words = text.split(); 
    if n == 1: return [text]
    best = None
    import itertools
    for cuts in itertools.combinations(range(1, len(words)), n - 1):
        parts = [' '.join(words[a:b]) for a, b in zip((0,) + cuts, cuts + (len(words),))]
        m = max(len(p) for p in parts)
        if best is None or m < best[0]: best = (m, parts)
    return best[1] if best else [text]
def layout(d, lines, ref, W, H):
    sz = int(H)
    while sz > 10:
        f = font('PlayfairDisplay.ttf', sz, 'Black'); rf = font('Cinzel.ttf', max(10, int(sz * 0.42)), 'Bold')
        lh = sz * 1.1; rh = sz * 0.55 if ref else 0
        tw = max([d.textlength(l, font=f) for l in lines] + ([d.textlength(ref, font=rf)] if ref else []))
        th = lh * len(lines) + rh
        if tw <= W and th <= H: return sz, f, rf, lh, th
        sz -= 2
    return sz, f, rf, lh, th
def fit_block(d, lines, ref, x0, y0, x1, y1):
    W, H = x1 - x0, y1 - y0; text = ' '.join(lines); best = None
    for n in range(1, 5):
        if n > len(text.split()): break
        L = wraps(text, n); r = layout(d, L, ref, W, H)
        if best is None or r[0] > best[0][0]: best = (r, L)
    (sz, f, rf, lh, th), lines = best
    y = y0 + (H - th) / 2; sw = max(2, sz // 14)
    for l in lines:
        w = d.textlength(l, font=f); d.text((x0 + (W - w) / 2, y), l, font=f, fill='white', stroke_width=sw, stroke_fill='black'); y += lh
    if ref: w = d.textlength(ref, font=rf); d.text((x0 + (W - w) / 2, y + sz * 0.06), ref, font=rf, fill='black')
import numpy as np
def max_rect(mask):
    # mask: True = empty. returns (r0,c0,r1,c1) of the largest all-empty rectangle
    R, C = mask.shape; h = [0] * C; best = (0, (0, 0, 0, 0))
    for r in range(R):
        for c in range(C): h[c] = h[c] + 1 if mask[r, c] else 0
        st = []
        for c in range(C + 1):
            cur = h[c] if c < C else 0; start = c
            while st and st[-1][1] >= cur:
                s0, hh = st.pop(); area = hh * (c - s0)
                if area > best[0]: best = (area, (r - hh + 1, s0, r + 1, c))
                start = s0
            st.append((start, cur))
    return best[1]
def find_box(im, win):
    a = np.array(im) < 200; Wd, Hd = im.size; x0, y0, x1, y1 = int(Wd * win[0]), int(Hd * win[1]), int(Wd * win[2]), int(Hd * win[3]); cs = 8
    sub = a[y0:y1, x0:x1]; R, C = sub.shape[0] // cs, sub.shape[1] // cs
    g = ~sub[:R * cs, :C * cs].reshape(R, cs, C, cs).any(axis=(1, 3))
    r0, c0, r1, c1 = max_rect(g); bx = (x0 + c0 * cs, y0 + r0 * cs, x0 + c1 * cs, y0 + r1 * cs)
    mw, mh = (bx[2] - bx[0]) * 0.07, (bx[3] - bx[1]) * 0.12
    return (int(bx[0] + mw), int(bx[1] + mh), int(bx[2] - mw), int(bx[3] - mh))
WIN = {1: (0.15, 0.25, 0.85, 0.72), 3: (0.15, 0.0, 0.85, 0.2), 4: (0.2, 0.76, 0.85, 0.92), 5: (0.05, 0.62, 0.95, 0.9), 6: (0.1, 0.75, 0.9, 0.97),
       7: (0.15, 0.03, 0.85, 0.22), 8: (0.15, 0.03, 0.85, 0.22), 9: (0.15, 0.35, 0.85, 0.72), 10: (0.1, 0.75, 0.9, 0.97)}
os.makedirs('/home/claude/C08/lettered', exist_ok=True)
for n, (lines, ref, box) in P.items():
    im = Image.open(f'/home/claude/C08/raw/page_{n:02d}.png').convert('L'); im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
    d = ImageDraw.Draw(im); Wd, Hd = im.size
    if box is None:  # open book: split across the two pages
        L = lines[:3]; R = lines[4:]
        fit_block(d, L, '', *find_box(im, (0.04, 0.33, 0.5, 0.62)))
        fit_block(d, R, ref, *find_box(im, (0.5, 0.33, 0.96, 0.62)))
    else:
        bx = find_box(im, WIN[n]) if n != 4 else (int(Wd*0.14), int(Hd*0.775), int(Wd*0.86), int(Hd*0.87)); fit_block(d, lines, ref, *bx)
    im.save(f'/home/claude/C08/lettered/page_{n:02d}.png'); print('ok', n)
