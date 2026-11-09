"""Full-size wall art sets. Usage: large_wall.py SPEC.json OUT_ROOT  (spec: listings[{slug, arts:[paths], base}])"""
import sys, os, json, zipfile
sys.path.insert(0, os.path.dirname(__file__))
from package_wall import *
SPEC, ROOT = sys.argv[1], sys.argv[2]
for sp in json.load(open(SPEC))['listings']:
    folder = os.path.join(ROOT, sp['slug']); os.makedirs(folder, exist_ok=True)
    arts = [Image.open(p).convert('RGB') for p in sp['arts']]
    for key, lab, (w, h) in [(k, l, (int(a * .75), int(b * .75))) for k, l, (a, b) in RATIOS]:
        with zipfile.ZipFile(os.path.join(folder, f"{sp['base']}_{key}.zip"), 'w', zipfile.ZIP_STORED) as z:
            for i, a in enumerate(arts, 1): z.writestr(f"{sp['base']}_{i}_{key}.jpg", jpg_bytes(crop_ratio(a, w, h), q=88))
    mockup([thumb(a, 2400) for a in arts[:3]]).save(os.path.join(folder, '01_cover.jpg'), quality=90)
    art_only([thumb(a, 2400) for a in arts]).save(os.path.join(folder, '02_art.jpg'), quality=90)
    detail(arts[0]).save(os.path.join(folder, '03_detail.jpg'), quality=90)
    sizes(sp['title'], len(arts)).save(os.path.join(folder, '04_sizes.jpg'), quality=90)
    details_img(len(arts)).save(os.path.join(folder, '05_details.jpg'), quality=90)
    print(sp['slug'], [(f, round(os.path.getsize(os.path.join(folder, f)) / 1e6, 1)) for f in sorted(os.listdir(folder))])
