"""Build a document pack: fillable PDFs (Letter + A4), Word (Letter + A4), Excel, quick start, zip, listing images.
Usage: python3 -I build_pack.py MODULE OUTROOT THEME
MODULE defines FORMS, XLSX, PACK = dict(slug, name, short, cover_title, cover_sub, audience)"""
import sys, os, zipfile, shutil, subprocess, importlib, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from forms_engine import pdf_forms, pdf_one, docx_form, THEMES, PDF
from xlsx_engine import build as xbuild
from reportlab.lib.pagesizes import letter, A4
from PIL import Image, ImageDraw, ImageFont, ImageFilter

mod = importlib.import_module(sys.argv[1]); ROOT = sys.argv[2]; THEME = sys.argv[3] if len(sys.argv) > 3 else 'navy'
FORMS, XLSX, P = mod.FORMS, getattr(mod, 'XLSX', []), mod.PACK
BRAND = 'Freemans DocHub'
work = os.path.join(ROOT, 'work', P['slug']); out = os.path.join(ROOT, 'listings', P['slug'])
shutil.rmtree(work, ignore_errors=True); shutil.rmtree(out, ignore_errors=True); os.makedirs(work); os.makedirs(out)
top = os.path.join(work, P['name'].replace(' ', '_'))
dirs = {k: os.path.join(top, v) for k, v in [('pl', '1_Fillable_PDF_US_Letter'), ('pa', '2_Fillable_PDF_A4'), ('wl', '3_Editable_Word_US_Letter'), ('wa', '4_Editable_Word_A4'), ('x', '5_Excel_Calculators')]}
for k, d in dirs.items():
    if k != 'x' or XLSX: os.makedirs(d)

def fname(f): return f"{f['code']}_{f['title'].replace(' & ', '_and_').replace('/', '-').replace(' ', '_')}"
for f in FORMS:
    pdf_one(f, os.path.join(dirs['pl'], fname(f) + '.pdf'), letter, THEME, BRAND)
    pdf_one(f, os.path.join(dirs['pa'], fname(f) + '.pdf'), A4, THEME, BRAND)
    docx_form(f, os.path.join(dirs['wl'], fname(f) + '.docx'), THEME, BRAND, a4=False)
    docx_form(f, os.path.join(dirs['wa'], fname(f) + '.docx'), THEME, BRAND, a4=True)
pdf_forms(FORMS, os.path.join(top, f"{P['name'].replace(' ', '_')}_ALL_FORMS_Letter.pdf"), letter, THEME, BRAND)
pdf_forms(FORMS, os.path.join(top, f"{P['name'].replace(' ', '_')}_ALL_FORMS_A4.pdf"), A4, THEME, BRAND)
for name, sheets in XLSX:
    xbuild(os.path.join(dirs['x'], name), sheets, THEMES[THEME]['acc'].lstrip('#'), THEMES[THEME]['acc2'].lstrip('#'), BRAND)

# quick start (usage notes, not a how-to guide)
qs = dict(code='START', title='Start Here: Quick Start', subtitle=f"{P['name']} · {len(FORMS)} forms" + (f" + {len(XLSX)} Excel calculators" if XLSX else ''), items=[
    ('section', "What's inside"),
    ('table', [('Folder', 2.2), ('What it is', 4)], None, {'first': ['ALL_FORMS PDFs', '1 & 2  Fillable PDF', '3 & 4  Editable Word', '5  Excel calculators' if XLSX else '—'],
     'rh': 22}),
    ('text', '<b>ALL_FORMS PDFs:</b> every form in one file, ready to print as a binder. <b>Fillable PDF:</b> type on screen in free Adobe Acrobat Reader or your browser, then print or save. '
             '<b>Editable Word:</b> change any wording, add your logo and business name, rename columns. Opens in Microsoft Word, Google Docs, Pages and LibreOffice. '
             + ('<b>Excel:</b> totals and calculations fill in automatically. Opens in Excel and Google Sheets. ' if XLSX else '')),
    ('section', 'Add your logo'),
    ('text', 'Word: click "[ Insert your logo here ]" in the top right, then Insert > Pictures. Fillable PDF: type your business name in the box at the top right.'),
    ('section', 'Printing tips'),
    ('text', 'Print at 100% / "Actual size". Choose the US Letter files in the U.S. and Canada, A4 everywhere else. Print one master copy and photocopy it, or reprint as many as you need.'),
    ('section', 'Forms in this pack'),
    ('table', [('Form', 1), ('Title', 5)], None, {'first': [f"{f['code']}   {f['title']}" for f in FORMS], 'rh': 15}),
    ('text', 'These templates are general business forms. They are not legal, medical or professional advice. Check that each form meets the rules for your area and industry, and edit it as needed.'),
    ('text', f'Questions or a custom form? Message {BRAND} on Etsy. Thank you for your purchase!')])
qs['items'][1] = ('table', [('Folder', 2.2), ('What it is', 4)], None, {'first': ['ALL_FORMS PDFs', '1 and 2: Fillable PDF', '3 and 4: Editable Word'] + (['5: Excel calculators'] if XLSX else []), 'rh': 18})
pdf_one(qs, os.path.join(top, '00_START_HERE.pdf'), letter, THEME, BRAND)

# zip
zpath = os.path.join(out, P['slug'] + '.zip')
with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
    for fp in sorted(glob.glob(top + '/**/*', recursive=True)):
        if os.path.isfile(fp): z.write(fp, os.path.relpath(fp, work))
print('zip MB', round(os.path.getsize(zpath) / 1e6, 2))

# ---------- listing images ----------
FD = '/usr/share/fonts/truetype/google-fonts/'
def pop(sz, w='Medium'): return ImageFont.truetype(FD + f'Poppins-{w}.ttf', sz)
acc = THEMES[THEME]['acc']; acc2 = THEMES[THEME]['acc2']
allpdf = os.path.join(top, f"{P['name'].replace(' ', '_')}_ALL_FORMS_Letter.pdf")
pv = os.path.join(work, 'pv'); os.makedirs(pv)
subprocess.run(['pdftoppm', '-r', '110', '-png', allpdf, os.path.join(pv, 'p')], check=True)
pages = [Image.open(f).convert('RGB') for f in sorted(glob.glob(pv + '/p-*.png'))]
# pick first page of each form
from pypdf import PdfReader
txt = [pg.extract_text() or '' for pg in PdfReader(allpdf).pages]
firsts = [pages[i] for i, t in enumerate(txt) if '(continued)' not in t.split('\n')[0]]
W, H = 3000, 2250
def shadowed(bg, im, x, y, rot=0):
    if rot: im = im.rotate(rot, expand=True, resample=Image.BICUBIC, fillcolor=(0, 0, 0, 0)) if im.mode == 'RGBA' else im.convert('RGBA').rotate(rot, expand=True, resample=Image.BICUBIC)
    else: im = im.convert('RGBA')
    sh = Image.new('RGBA', (im.width + 120, im.height + 120), (0, 0, 0, 0)); a = im.split()[3]
    sh.paste((0, 0, 0, 70), (60, 75), a); sh = sh.filter(ImageFilter.GaussianBlur(24))
    bg.paste(sh, (x - 60, y - 60), sh); bg.paste(im, (x, y), im)
def ct(d, y, t, f, c, W=W):
    w = d.textlength(t, font=f); d.text(((W - w) / 2, y), t, font=f, fill=c)
def fit(im, h): return im.resize((int(im.width * h / im.height), h), Image.LANCZOS)
# 1 cover
bg = Image.new('RGB', (W, H), '#F4F1EC'); d = ImageDraw.Draw(bg)
d.rectangle([0, 0, W, 40], fill=acc)
ct(d, 120, P['cover_title'], pop(150, 'Bold'), acc)
ct(d, 320, P['cover_sub'], pop(70), '#333333')
badges = [f"{len(FORMS)} FORMS", 'FILLABLE PDF', 'EDITABLE WORD'] + (['EXCEL'] if XLSX else []) + ['LETTER + A4']
bw = [d.textlength(b, font=pop(46, 'Bold')) + 80 for b in badges]; x = (W - sum(bw) - 30 * (len(bw) - 1)) / 2
for b, w in zip(badges, bw):
    d.rounded_rectangle([x, 450, x + w, 540], radius=45, fill=acc); d.text((x + 40, 466), b, font=pop(46, 'Bold'), fill='white'); x += w + 30
sel = firsts[:5]; ph = 1450
xs = [180, 700, 1180, 1660, 2140]; rots = [6, 3, 0, -3, -6]
order = [0, 4, 1, 3, 2]
for i in order:
    if i < len(sel): shadowed(bg, fit(sel[i], ph), xs[i], 680 + abs(rots[i]) * 12, rots[i])
bg.save(os.path.join(out, '01_cover.jpg'), quality=90)
# 2 everything included grid
bg = Image.new('RGB', (W, H), '#F4F1EC'); d = ImageDraw.Draw(bg)
ct(d, 70, f"Everything included: {len(FORMS)} forms" + (f" + {len(XLSX)} Excel" if XLSX else ''), pop(96, 'Bold'), acc)
n = len(firsts); cols = 7 if n > 14 else 5; rows = (n + cols - 1) // cols
cw = (W - 200) // cols; chh = (H - 330) // rows; th = int(min(chh - 70, cw * 1.3))
for i, im in enumerate(firsts):
    t = fit(im, th)
    if t.width > cw - 30: t = im.resize((cw - 30, int(im.height * (cw - 30) / im.width)), Image.LANCZOS)
    x = 100 + (i % cols) * cw + (cw - t.width) // 2; y = 250 + (i // cols) * chh
    shadowed(bg, t, x, y)
    lab = FORMS[i]['title'] if i < len(FORMS) else ''
    lab = lab if d.textlength(lab, font=pop(26)) < cw - 10 else lab[:int(len(lab) * (cw - 10) / d.textlength(lab, font=pop(26))) - 1] + '…'
    ct(d, y + t.height + 12, lab, pop(26), '#333333') if False else d.text((100 + (i % cols) * cw + (cw - d.textlength(lab, font=pop(26))) / 2, y + t.height + 14), lab, font=pop(26), fill='#333333')
bg.save(os.path.join(out, '02_all_forms.jpg'), quality=90)
# 3 features
bg = Image.new('RGB', (W, H), acc); d = ImageDraw.Draw(bg)
ct(d, 110, 'Why this pack is different', pop(110, 'Bold'), 'white')
feats = P['features']
y = 380
for t1, t2 in feats:
    d.rounded_rectangle([260, y, W - 260, y + 230], radius=30, fill='white')
    d.ellipse([310, y + 65, 410, y + 165], fill=acc2); d.text((339, y + 72), '✓' if False else '+', font=pop(70, 'Bold'), fill=acc)
    d.text((460, y + 38), t1, font=pop(60, 'Bold'), fill=acc); d.text((460, y + 125), t2, font=pop(42), fill='#444444')
    y += 265
bg.save(os.path.join(out, '03_features.jpg'), quality=90)
# 4 close-up of a key form
ki = P.get('hero', 0); im = firsts[ki]
bg = Image.new('RGB', (W, H), '#F4F1EC'); d = ImageDraw.Draw(bg)
crop = im.crop((0, 0, im.width, int(im.width * 0.62))); crop = crop.resize((2300, int(crop.height * 2300 / crop.width)), Image.LANCZOS)
shadowed(bg, crop, 350, 330)
ct(d, 90, P.get('hero_caption', 'Clean, professional layout'), pop(80, 'Bold'), acc)
bg.save(os.path.join(out, '04_closeup.jpg'), quality=90)
# 5 formats
bg = Image.new('RGB', (W, H), '#F4F1EC'); d = ImageDraw.Draw(bg)
ct(d, 110, 'Use it your way', pop(110, 'Bold'), acc)
boxes = [('Fillable PDF', 'Type on screen in Adobe Reader or your browser, then print'), ('Editable Word', 'Change wording, add your logo. Works in Word, Google Docs and Pages'),
         ('US Letter + A4', 'Both paper sizes included for every form')]
if XLSX: boxes.append(('Excel calculators', 'Totals fill in automatically. Works in Excel and Google Sheets'))
bw = (W - 400 - 80 * (len(boxes) - 1)) // len(boxes)
for i, (t1, t2) in enumerate(boxes):
    x = 200 + i * (bw + 80)
    d.rounded_rectangle([x, 520, x + bw, 1300], radius=40, fill='white', outline=acc, width=6)
    d.rounded_rectangle([x, 520, x + bw, 760], radius=40, fill=acc); d.rectangle([x, 700, x + bw, 760], fill=acc)
    tw = d.textlength(t1, font=pop(64, 'Bold')); d.text((x + (bw - tw) / 2, 590), t1, font=pop(64, 'Bold'), fill='white')
    words = t2.split(); lines = []; cur = ''
    for wd in words:
        tt = (cur + ' ' + wd).strip()
        if d.textlength(tt, font=pop(46)) < bw - 80: cur = tt
        else: lines.append(cur); cur = wd
    lines.append(cur)
    for k, ln in enumerate(lines): d.text((x + 40, 850 + k * 70), ln, font=pop(46), fill='#333333')
ct(d, 1480, 'Instant download · print as many copies as you need', pop(56), '#555555')
bg.save(os.path.join(out, '05_formats.jpg'), quality=90)
print('images', sorted(os.listdir(out)))
