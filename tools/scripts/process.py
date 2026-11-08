"""Clipart pipeline: upscale x4 (Real-ESRGAN), cut out background, crop, save 300dpi PNG.
Usage: python3 -I process.py IN_DIR OUT_DIR
"""
import sys, glob, os
import numpy as np, torch
from PIL import Image
from spandrel import ModelLoader
from rembg import remove, new_session

IN, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
torch.set_num_threads(os.cpu_count() or 4)
model = ModelLoader().load_from_file('/home/claude/models/realesr-general-x4v3.pth').eval()
sess = new_session('isnet-general-use')

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

for f in sorted(glob.glob(os.path.join(IN, '*.png'))):
    name = os.path.basename(f)
    src = Image.open(f)
    up = upscale(src)
    cut = remove(up, session=sess, post_process_mask=True)
    # union with a 'not background-white' mask so rembg can't delete real artwork
    from PIL import ImageFilter, ImageChops
    rgb = np.asarray(up).astype(np.int16)
    dist = (255 - rgb.min(axis=2))  # 0 for pure white
    keep = Image.fromarray(np.clip((dist - 12) * 12, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.5))
    # flood-fill style: only background white connected to the border is removable
    a = ImageChops.lighter(cut.getchannel('A'), keep)
    cut = up.convert('RGBA'); cut.putalpha(a)
    bbox = cut.getchannel('A').point(lambda v: 255 if v > 20 else 0).getbbox()
    if bbox:
        m = int(0.02 * max(cut.size))
        bbox = (max(bbox[0] - m, 0), max(bbox[1] - m, 0), min(bbox[2] + m, cut.width), min(bbox[3] + m, cut.height))
        cut = cut.crop(bbox)
    if max(cut.size) > 4000:
        s = 4000 / max(cut.size)
        cut = cut.resize((round(cut.width * s), round(cut.height * s)), Image.LANCZOS)
    cut.save(os.path.join(OUT, name), dpi=(300, 300), optimize=True)
    print(name, src.size, '->', cut.size, flush=True)
