"""Cut a 3x2 emote sheet into transparent emotes. Usage: emotes.py SHEET.png OUTDIR NAME label1,label2,..."""
import sys, os, numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
src, out, name, labels = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4].split(',')
os.makedirs(out, exist_ok=True)
im = Image.open(src).convert('RGB'); a = np.asarray(im).astype(int); H, W, _ = a.shape
nonwhite = (a.min(axis=2) < 235)
# split columns/rows at the emptiest bands near the 1/3, 2/3 and 1/2 lines
def cut(profile, n, L):
    cuts=[0]
    for k in range(1,n):
        c=int(L*k/n); w=int(L*0.12); seg=profile[c-w:c+w]; cuts.append(c-w+int(np.argmin(seg)))
    return cuts+[L]
xs = cut(nonwhite.sum(0), 3, W); ys = cut(nonwhite.sum(1), 2, H)
i = 0
for r in range(2):
    for c in range(3):
        cell = a[ys[r]:ys[r+1], xs[c]:xs[c+1]]
        nw = cell.min(axis=2) < 235
        # background = near-white region connected to cell border
        white = cell.min(axis=2) >= 247
        lab, _ = ndimage.label(white)
        border = set(np.unique(np.concatenate([lab[0], lab[:, 0], lab[:, -1]]))) - {0}
        # bottom-edge white only counts as background if it is also open at the top/sides; otherwise it's an unoutlined body part
        bg = np.isin(lab, list(border))
        # keep only the largest foreground component (+ things close to it)
        fg = ~bg
        lab2, n2 = ndimage.label(ndimage.binary_dilation(fg, iterations=12))
        if n2 > 1:
            sizes = ndimage.sum(fg, lab2, range(1, n2 + 1)); keep = lab2 == (np.argmax(sizes) + 1)
            fg &= keep
        alpha = Image.fromarray((fg * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))
        rgba = Image.fromarray(cell.astype(np.uint8)).convert('RGBA'); rgba.putalpha(alpha)
        bb = Image.fromarray((fg * 255).astype(np.uint8)).getbbox(); rgba = rgba.crop(bb)
        s = max(rgba.size); pad = int(s * 0.04); S = s + 2 * pad
        sq = Image.new('RGBA', (S, S), (0, 0, 0, 0)); sq.paste(rgba, ((S - rgba.width) // 2, (S - rgba.height) // 2), rgba)
        lbl = labels[i]; base = f'{name}_{lbl}'
        for px in (512, 112, 56, 28):
            d = os.path.join(out, f'{px}px'); os.makedirs(d, exist_ok=True)
            sq.resize((px, px), Image.LANCZOS).save(os.path.join(d, f'{base}_{px}.png'), optimize=True)
        i += 1
print(name, xs, ys)
