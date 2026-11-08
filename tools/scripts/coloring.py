"""Coloring pages: upscale, threshold to clean B/W line art, fit onto US Letter + A4 at 300 dpi.
Outputs per page: NN_name_letter.png, NN_name_a4.png ; plus combined PDFs per batch.
Usage: python3 -I coloring.py IN_DIR OUT_DIR BUNDLE_NAME
"""
import sys, glob, os
import numpy as np, torch
from PIL import Image, ImageFilter
from spandrel import ModelLoader

IN, OUT, NAME = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(OUT, exist_ok=True)
torch.set_num_threads(os.cpu_count() or 2)
model = ModelLoader().load_from_file('/home/claude/models/realesr-general-x4v3.pth').eval()

def upscale(img, tile=512, pad=16):
    a = np.asarray(img.convert('RGB')).astype(np.float32) / 255
    h, w, _ = a.shape
    out = np.zeros((h * 4, w * 4, 3), np.float32)
    for y in range(0, h, tile):
        for x in range(0, w, tile):
            y0, x0 = max(y - pad, 0), max(x - pad, 0)
            y1, x1 = min(y + tile + pad, h), min(x + tile + pad, w)
            t = torch.from_numpy(a[y0:y1, x0:x1]).permute(2, 0, 1)[None]
            with torch.no_grad():
                r = model(t)[0].permute(1, 2, 0).clamp(0, 1).numpy()
            yy, xx = (y - y0) * 4, (x - x0) * 4
            th, tw = min(tile, h - y) * 4, min(tile, w - x) * 4
            out[y * 4:y * 4 + th, x * 4:x * 4 + tw] = r[yy:yy + th, xx:xx + tw]
    return Image.fromarray((out * 255).round().astype(np.uint8))

SIZES = {'letter': (2550, 3300), 'a4': (2480, 3508)}
MARGIN = 150  # 0.5 in
pages = {k: [] for k in SIZES}
for f in sorted(glob.glob(os.path.join(IN, '*.png'))):
    base = os.path.splitext(os.path.basename(f))[0]
    src = Image.open(f).convert('L'); g = src.resize((src.width * 3, src.height * 3), Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.2))
    g = g.point(lambda v: 0 if v < 150 else 255).filter(ImageFilter.MedianFilter(3))
    bbox = Image.eval(g, lambda v: 255 - v).getbbox()
    if bbox: g = g.crop(bbox)
    for k, (W, H) in SIZES.items():
        im = g.copy(); im.thumbnail((W - 2 * MARGIN, H - 2 * MARGIN), Image.LANCZOS)
        im = im.point(lambda v: 0 if v < 160 else 255)
        page = Image.new('L', (W, H), 255); page.paste(im, ((W - im.width) // 2, (H - im.height) // 2))
        page = page.convert('1')
        page.save(os.path.join(OUT, f'{base}_{k}.png'), dpi=(300, 300), optimize=True)
        pages[k].append(page)
    print(base, flush=True)
for k, ps in pages.items():
    if ps:
        ps[0].save(os.path.join(OUT, f'{NAME}_{k}.pdf'), save_all=True, append_images=ps[1:], resolution=300)
print('done')
