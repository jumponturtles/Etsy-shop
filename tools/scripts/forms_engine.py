"""Business form engine: one spec -> fillable PDF (Letter/A4) + editable DOCX.
Form spec: dict(code, title, subtitle, landscape, items=[...elements]).
Elements:
  ('section', 'Title')
  ('fields', ['Label', ...], ncols)                 label + fill line rows
  ('table', [('Col', w), ...], nrows|'fill', {'check': [colidx], 'first': [...prefilled col0 values]})
  ('checklist', ['item', ...], ['Col', ...])          item rows + checkbox columns
  ('box', 'Title', height_pt)                         multi-line notes box
  ('ref', 'text with <b>bold</b>')                    shaded reference panel
  ('sign', ['Completed by', 'Manager sign-off', 'Date'])
  ('text', 'paragraph')
"""
import os, re
from reportlab.lib.pagesizes import letter, A4, landscape as LS
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

FD = '/usr/share/fonts/truetype/google-fonts/'
for n, f in [('Pop', 'Poppins-Regular.ttf'), ('PopM', 'Poppins-Medium.ttf'), ('PopB', 'Poppins-Bold.ttf')]:
    try: pdfmetrics.registerFont(TTFont(n, FD + f))
    except Exception: pass

THEMES = {
    'navy':  dict(acc='#1F3A5F', acc2='#E8EEF5', line='#9AA8B8', name='Navy'),
    'teal':  dict(acc='#1E5E5B', acc2='#E3F0EE', line='#93AFAC', name='Teal'),
    'plum':  dict(acc='#5A2D4F', acc2='#F2E7EF', line='#B39AAD', name='Plum'),
    'slate': dict(acc='#33393F', acc2='#ECEEF0', line='#A3A9AF', name='Slate'),
}
REV = 'Rev. 11/2026'

class PDF:
    def __init__(self, path, size, theme, brand, landscape=False):
        self.size = LS(size) if landscape else size
        self.c = canvas.Canvas(path, pagesize=self.size)
        self.W, self.H = self.size
        self.t = {k: HexColor(v) if v.startswith('#') else v for k, v in THEMES[theme].items()}
        self.brand = brand; self.m = 36; self.n = 0; self.fid = 0
    def fname(self, p): self.fid += 1; return f'{p}{self.fid}'
    def header(self, f, cont=False):
        c, W, H, m = self.c, self.W, self.H, self.m
        c.setFillColor(self.t['acc']); c.rect(0, H - 10, W, 10, stroke=0, fill=1)
        c.setFillColor(black); c.setFont('PopB', 17 if not cont else 13)
        c.drawString(m, H - 46, f['title'] + (' (continued)' if cont else ''))
        if f.get('subtitle') and not cont:
            c.setFont('Pop', 8.5); c.setFillColor(HexColor('#555555')); c.drawString(m, H - 60, f['subtitle'])
        # logo slot + business line
        lw, lh = 118, 38
        c.setStrokeColor(self.t['line']); c.setDash(3, 2); c.setLineWidth(0.7)
        c.rect(W - m - lw, H - 62, lw, lh, stroke=1, fill=0); c.setDash()
        c.setFont('Pop', 7); c.setFillColor(self.t['line']); c.drawCentredString(W - m - lw / 2, H - 45, 'YOUR LOGO / BUSINESS NAME')
        self.c.acroForm.textfield(name=self.fname('biz'), x=W - m - lw + 3, y=H - 60, width=lw - 6, height=12,
                                  borderWidth=0, fillColor=None, fontSize=8, fontName='Helvetica', tooltip='Business name')
        c.setStrokeColor(self.t['acc']); c.setLineWidth(1.2); c.line(m, H - 70, W - m, H - 70)
        self.y = H - 82
    def footer(self, f):
        c = self.c; self.n += 1
        c.setFont('Pop', 6.5); c.setFillColor(HexColor('#777777'))
        c.drawString(self.m, 18, f"Form {f['code']}  ·  {REV}  ·  {self.brand}")
        c.drawRightString(self.W - self.m, 18, f'Page {self.n}')
    def need(self, h, f):
        if self.y - h < 34:
            self.footer(f); self.c.showPage(); self.header(f, cont=True)
    def section(self, txt, f):
        self.need(30, f); c = self.c
        c.setFillColor(self.t['acc2']); c.rect(self.m, self.y - 16, self.W - 2 * self.m, 16, stroke=0, fill=1)
        c.setFillColor(self.t['acc']); c.setFont('PopB', 9); c.drawString(self.m + 6, self.y - 11.5, txt.upper())
        self.y -= 24
    def fields(self, labels, ncols, f):
        c = self.c; cw = (self.W - 2 * self.m) / ncols; rh = 22
        for i in range(0, len(labels), ncols):
            self.need(rh, f)
            for j, lab in enumerate(labels[i:i + ncols]):
                x = self.m + j * cw; c.setFont('PopM', 7.5); c.setFillColor(HexColor('#333333'))
                c.drawString(x, self.y - 8, lab); tw = c.stringWidth(lab, 'PopM', 7.5) + 6
                c.setStrokeColor(self.t['line']); c.setLineWidth(0.6); c.line(x + tw, self.y - 10, x + cw - 10, self.y - 10)
                c.acroForm.textfield(name=self.fname('f'), x=x + tw, y=self.y - 11, width=cw - 10 - tw, height=12,
                                     borderWidth=0, fillColor=None, fontSize=8, tooltip=lab)
            self.y -= rh
        self.y -= 4
    def table(self, cols, nrows, opt, f, rh=17):
        c = self.c; TW = self.W - 2 * self.m; tot = sum(w for _, w in cols)
        ws = [TW * w / tot for _, w in cols]; checks = set(opt.get('check', [])); first = opt.get('first')
        hh = 26 if any(len(n) > 14 for n, _ in cols) else 18
        def head():
            x = self.m; c.setFillColor(self.t['acc']); c.rect(self.m, self.y - hh, TW, hh, stroke=0, fill=1)
            c.setFillColor(white)
            for (n, _), w in zip(cols, ws):
                fs = 7 if c.stringWidth(n, 'PopB', 7.2) < w - 4 else 6
                lines = wrap(c, n, 'PopB', fs, w - 4)[:2]
                for k, ln in enumerate(lines):
                    c.setFont('PopB', fs); c.drawCentredString(x + w / 2, self.y - hh / 2 + 2 - (k - (len(lines) - 1) / 2) * (fs + 1) - fs / 2 + 1, ln)
                x += w
            self.y -= hh
        if nrows == 'fill':
            nrows = max(3, int((self.y - 40 - hh - opt.get('reserve', 0)) // rh))
        if first:
            nrows = len(first); avail = self.y - 40 - hh - opt.get('reserve', 0)
            if nrows * rh > avail and nrows * 10 <= avail: rh = avail / nrows
        self.need(hh + rh * min(3, nrows), f); head()
        for r in range(nrows):
            if self.y - rh < 34:
                self.footer(f); c.showPage(); self.header(f, cont=True); head()
            x = self.m
            if r % 2: c.setFillColor(HexColor('#FAFAFA')); c.rect(self.m, self.y - rh, TW, rh, stroke=0, fill=1)
            for ci, w in enumerate(ws):
                c.setStrokeColor(self.t['line']); c.setLineWidth(0.5); c.rect(x, self.y - rh, w, rh, stroke=1, fill=0)
                if ci == 0 and first:
                    c.setFillColor(black); c.setFont('Pop', 7.5 if c.stringWidth(first[r], 'Pop', 7.5) < w - 6 else 6.3)
                    c.drawString(x + 4, self.y - rh / 2 - 2.5, first[r])
                elif ci in checks:
                    s = min(10, rh - 6)
                    c.acroForm.checkbox(name=self.fname('cb'), x=x + w / 2 - s / 2, y=self.y - rh / 2 - s / 2, size=s,
                                        buttonStyle='check', borderWidth=0.6, borderColor=self.t['acc'], fillColor=white, textColor=black)
                else:
                    c.acroForm.textfield(name=self.fname('t'), x=x + 1.5, y=self.y - rh + 1.5, width=w - 3, height=rh - 3,
                                         borderWidth=0, fillColor=None, fontSize=8 if rh >= 16 else 7)
                x += w
            self.y -= rh
        self.y -= 10
    def checklist(self, items, cols, f, itemw=None, rh=17):
        tot = len(cols); iw = itemw or (6 if tot <= 3 else 4)
        self.table([('Task', iw)] + [(c_, 1) for c_ in cols], None, {'first': items, 'check': list(range(1, tot + 1))}, f, rh=rh)
    def box(self, title, h, f):
        self.need(h + 14, f); c = self.c
        c.setFont('PopM', 8); c.setFillColor(HexColor('#333333')); c.drawString(self.m, self.y - 8, title)
        c.setStrokeColor(self.t['line']); c.setLineWidth(0.6); c.roundRect(self.m, self.y - 12 - h, self.W - 2 * self.m, h, 4, stroke=1, fill=0)
        c.acroForm.textfield(name=self.fname('b'), x=self.m + 2, y=self.y - 10 - h, width=self.W - 2 * self.m - 4, height=h - 4,
                             borderWidth=0, fillColor=None, fontSize=8, fieldFlags='multiline')
        self.y -= h + 20
    def ref(self, txt, f):
        st = ParagraphStyle('r', fontName='Pop', fontSize=7.3, leading=9.6, textColor=HexColor('#222222'))
        p = Paragraph(txt, st); w = self.W - 2 * self.m - 16; _, h = p.wrap(w, 1000)
        self.need(h + 14, f); c = self.c
        c.setFillColor(self.t['acc2']); c.setStrokeColor(self.t['acc']); c.setLineWidth(0.8)
        c.roundRect(self.m, self.y - h - 10, self.W - 2 * self.m, h + 10, 4, stroke=1, fill=1)
        p.drawOn(c, self.m + 8, self.y - h - 5); self.y -= h + 18
    def text(self, txt, f):
        st = ParagraphStyle('t', fontName='Pop', fontSize=8, leading=10.5)
        p = Paragraph(txt, st); w = self.W - 2 * self.m; _, h = p.wrap(w, 1000)
        self.need(h + 6, f); p.drawOn(self.c, self.m, self.y - h); self.y -= h + 8
    def sign(self, labels, f):
        self.need(34, f); c = self.c; n = len(labels); cw = (self.W - 2 * self.m) / n
        self.y -= 14
        for i, lab in enumerate(labels):
            x = self.m + i * cw
            c.setStrokeColor(black); c.setLineWidth(0.7); c.line(x, self.y, x + cw - 16, self.y)
            c.acroForm.textfield(name=self.fname('s'), x=x, y=self.y + 1, width=cw - 16, height=13, borderWidth=0, fillColor=None, fontSize=8)
            c.setFont('Pop', 7); c.setFillColor(HexColor('#555555')); c.drawString(x, self.y - 9, lab)
        self.y -= 22
    def cards(self, ncols, nrows, title, lines, f):
        c = self.c; gap = 10; cw = (self.W - 2 * self.m - gap * (ncols - 1)) / ncols
        ch = (self.y - 40 - gap * (nrows - 1)) / nrows
        for r in range(nrows):
            for k in range(ncols):
                x = self.m + k * (cw + gap); top = self.y - r * (ch + gap)
                c.setStrokeColor(self.t['line']); c.setDash(4, 3); c.setLineWidth(0.7); c.roundRect(x, top - ch, cw, ch, 6, stroke=1, fill=0); c.setDash()
                c.setFillColor(self.t['acc']); c.roundRect(x, top - 20, cw, 20, 6, stroke=0, fill=1); c.rect(x, top - 20, cw, 8, stroke=0, fill=1)
                c.setFillColor(white); c.setFont('PopB', 9); c.drawString(x + 8, top - 14, title)
                yy = top - 38; lh = min(30, (ch - 44) / max(1, len(lines)))
                for lab in lines:
                    if lab.startswith('[]'):
                        xx = x + 8
                        for opt in lab[2:].split('|'):
                            c.acroForm.checkbox(name=self.fname('cc'), x=xx, y=yy - 2, size=8, buttonStyle='check', borderWidth=0.6, borderColor=self.t['acc'], fillColor=white)
                            c.setFillColor(HexColor('#333333')); c.setFont('Pop', 7); c.drawString(xx + 11, yy, opt); xx += c.stringWidth(opt, 'Pop', 7) + 22
                    else:
                        c.setFillColor(HexColor('#333333')); c.setFont('PopM', 7); c.drawString(x + 8, yy, lab)
                        tw = c.stringWidth(lab, 'PopM', 7) + 12
                        c.setStrokeColor(self.t['line']); c.line(x + tw, yy - 2, x + cw - 8, yy - 2)
                        c.acroForm.textfield(name=self.fname('cf'), x=x + tw, y=yy - 3, width=cw - 8 - tw, height=11, borderWidth=0, fillColor=None, fontSize=7)
                    yy -= lh
        self.y -= nrows * (ch + gap)
    def render(self, f):
        self.header(f)
        for el in f['items']:
            k = el[0]
            if k == 'section': self.section(el[1], f)
            elif k == 'fields': self.fields(el[1], el[2] if len(el) > 2 else 2, f)
            elif k == 'table': self.table(el[1], el[2], el[3] if len(el) > 3 else {}, f, rh=(el[3] or {}).get('rh', 17) if len(el) > 3 else 17)
            elif k == 'checklist': self.checklist(el[1], el[2], f, el[3] if len(el) > 3 else None, el[4] if len(el) > 4 else 17)
            elif k == 'box': self.box(el[1], el[2], f)
            elif k == 'ref': self.ref(el[1], f)
            elif k == 'text': self.text(el[1], f)
            elif k == 'sign': self.sign(el[1], f)
            elif k == 'cards': self.cards(el[1], el[2], el[3], el[4], f)
        self.footer(f); self.c.showPage()
    def save(self): self.c.save()

def wrap(c, s, font, fs, w):
    words = s.split(); lines = []; cur = ''
    for wd in words:
        t = (cur + ' ' + wd).strip()
        if c.stringWidth(t, font, fs) <= w or not cur: cur = t
        else: lines.append(cur); cur = wd
    if cur: lines.append(cur)
    return lines

def pdf_forms(forms, path, size, theme, brand):
    """Render many forms into one PDF (each starts on a new page)."""
    pages = []
    p = None
    for f in forms:
        q = PDF(path + f".{f['code']}.tmp.pdf", size, theme, brand, f.get('landscape', False))
        q.render(f); q.save(); pages.append(path + f".{f['code']}.tmp.pdf")
    from pypdf import PdfWriter, PdfReader
    w = PdfWriter()
    for pg in pages:
        w.append(PdfReader(pg))
    w.write(path)
    for pg in pages: os.remove(pg)

def pdf_one(f, path, size, theme, brand):
    q = PDF(path, size, theme, brand, f.get('landscape', False)); q.render(f); q.save()

# ---------------- DOCX ----------------
from docx import Document
from docx.shared import Pt, RGBColor, Inches, Mm
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def _shade(cell, hexcol):
    tcPr = cell._tc.get_or_add_tcPr(); sh = OxmlElement('w:shd')
    sh.set(qn('w:val'), 'clear'); sh.set(qn('w:color'), 'auto'); sh.set(qn('w:fill'), hexcol.lstrip('#')); tcPr.append(sh)
def _borders(table, col='9AA8B8'):
    tbl = table._tbl; tblPr = tbl.tblPr; b = OxmlElement('w:tblBorders')
    for e in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        el = OxmlElement(f'w:{e}'); el.set(qn('w:val'), 'single'); el.set(qn('w:sz'), '4'); el.set(qn('w:color'), col); b.append(el)
    tblPr.append(b)
def _noborders(table):
    tblPr = table._tbl.tblPr; b = OxmlElement('w:tblBorders')
    for e in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        el = OxmlElement(f'w:{e}'); el.set(qn('w:val'), 'nil'); b.append(el)
    tblPr.append(b)
def _grid(table, widths):
    table.autofit = False
    tblPr = table._tbl.tblPr; lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr.append(lay)
    grid = table._tbl.tblGrid
    for gc, w in zip(grid.findall(qn('w:gridCol')), widths): gc.set(qn('w:w'), str(int(w / 635)))
    for row in table.rows:
        for cell, w in zip(row.cells, widths): cell.width = int(w)
def _gap(d, pt=4):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(0); p.paragraph_format.space_before = Pt(0)
    r = p.add_run(''); r.font.size = Pt(pt); p.paragraph_format.line_spacing = Pt(pt)
def _run(p, txt, size=9, bold=False, color=None, font='Calibri'):
    r = p.add_run(txt); r.font.size = Pt(size); r.bold = bold; r.font.name = font
    if color: r.font.color.rgb = RGBColor.from_string(color.lstrip('#'))
    return r
def _rowh(row, pt):
    trPr = row._tr.get_or_add_trPr(); h = OxmlElement('w:trHeight'); h.set(qn('w:val'), str(int(pt * 20))); h.set(qn('w:hRule'), 'atLeast'); trPr.append(h)

def docx_form(f, path, theme, brand, a4=False):
    T = THEMES[theme]; acc = T['acc']; d = Document()
    s = d.sections[0]
    if a4: s.page_width, s.page_height = Mm(210), Mm(297)
    else: s.page_width, s.page_height = Inches(8.5), Inches(11)
    if f.get('landscape'):
        s.orientation = WD_ORIENT.LANDSCAPE; s.page_width, s.page_height = s.page_height, s.page_width
    for side in ('left_margin', 'right_margin'): setattr(s, side, Inches(0.5))
    s.top_margin = Inches(0.45); s.bottom_margin = Inches(0.5)
    st = d.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(9)
    st.paragraph_format.space_after = Pt(2)
    usable = s.page_width - s.left_margin - s.right_margin
    # header: title left, logo slot right
    ht = d.add_table(rows=1, cols=2); ht.alignment = WD_TABLE_ALIGNMENT.CENTER
    c0, c1 = ht.rows[0].cells
    c0.width = int(usable * 0.7); c1.width = int(usable * 0.3)
    p = c0.paragraphs[0]; _run(p, f['title'], 17, True, '#111111')
    if f.get('subtitle'): _run(c0.add_paragraph(), f['subtitle'], 8.5, False, '#555555')
    p = c1.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER; _run(p, '[ Insert your logo here ]', 8, False, T['line'])
    _run(c1.add_paragraph(), 'Business name', 8, False, '#777777').italic = True
    c1.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    _noborders(ht); _grid(ht, [usable * 0.7, usable * 0.3])
    bar = d.add_paragraph(); pPr = bar._p.get_or_add_pPr(); bd = OxmlElement('w:pBdr'); bt = OxmlElement('w:bottom')
    bt.set(qn('w:val'), 'single'); bt.set(qn('w:sz'), '12'); bt.set(qn('w:color'), acc.lstrip('#')); bd.append(bt); pPr.append(bd)
    for el in f['items']:
        k = el[0]
        if k == 'section':
            t = d.add_table(rows=1, cols=1); cell = t.rows[0].cells[0]; _shade(cell, T['acc2'])
            _run(cell.paragraphs[0], el[1].upper(), 9, True, acc); _noborders(t); _grid(t, [usable]); _gap(d, 3)
        elif k == 'fields':
            labs = el[1]; n = el[2] if len(el) > 2 else 2
            t = d.add_table(rows=(len(labs) + n - 1) // n, cols=n)
            for i, lab in enumerate(labs):
                cell = t.rows[i // n].cells[i % n]; p = cell.paragraphs[0]
                _run(p, lab + ' ', 8.5, True, '#333333'); _run(p, '_' * max(8, int((95 if f.get('landscape') else 70) / n) - len(lab)), 8.5, False, T['line'])
            _noborders(t); _grid(t, [usable / n] * n); _gap(d)
        elif k in ('table', 'checklist'):
            if k == 'checklist':
                items, cols_ = el[1], el[2]; iw = el[3] if len(el) > 3 and el[3] else (6 if len(cols_) <= 3 else 4)
                cols = [('Task', iw)] + [(c_, 1) for c_ in cols_]; opt = {'first': items, 'check': list(range(1, len(cols_) + 1))}; nrows = len(items)
                if len(el) > 4: opt['docx_rh'] = max(13, el[4] * 0.85)
            else:
                cols, nrows = el[1], el[2]; opt = el[3] if len(el) > 3 else {}
                if opt.get('first'): nrows = len(opt['first'])
                elif nrows == 'fill': nrows = opt.get('docx_rows', 18)
            tot = sum(w for _, w in cols); t = d.add_table(rows=nrows + 1, cols=len(cols)); _borders(t, T['line'].lstrip('#'))
            _grid(t, [usable * w / tot for _, w in cols]); rhd = opt.get('docx_rh', 12.5 if f.get('landscape') else 15)
            for ci, (n, w) in enumerate(cols):
                cell = t.rows[0].cells[ci]; cell.width = int(usable * w / tot); _shade(cell, acc)
                p = cell.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER; _run(p, n, 7.5, True, '#FFFFFF')
            checks = set(opt.get('check', [])); first = opt.get('first')
            for r in range(nrows):
                row = t.rows[r + 1]; _rowh(row, rhd)
                for ci, (n, w) in enumerate(cols):
                    cell = row.cells[ci]; cell.width = int(usable * w / tot)
                    cell.paragraphs[0].paragraph_format.space_after = Pt(0)
                    if ci == 0 and first: _run(cell.paragraphs[0], first[r], 8)
                    elif ci in checks:
                        p = cell.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER; _run(p, '☐', 10, False, acc, 'Segoe UI Symbol')
            _gap(d)
        elif k == 'box':
            _run(d.add_paragraph(), el[1], 8.5, True, '#333333')
            t = d.add_table(rows=1, cols=1); _borders(t, T['line'].lstrip('#')); _rowh(t.rows[0], el[2] * 0.95); _grid(t, [usable]); _gap(d)
        elif k == 'ref':
            t = d.add_table(rows=1, cols=1); cell = t.rows[0].cells[0]; _shade(cell, T['acc2']); _borders(t, acc.lstrip('#'))
            _grid(t, [usable]); p = cell.paragraphs[0]
            for part in re.split(r'(<b>.*?</b>|<br/>)', el[1]):
                if not part: continue
                if part == '<br/>': p = cell.add_paragraph(); continue
                b = part.startswith('<b>'); _run(p, re.sub('<.*?>', '', part), 8, b)
            d.add_paragraph()
        elif k == 'text':
            p = d.add_paragraph(); _run(p, re.sub('<.*?>', '', el[1]), 9)
        elif k == 'cards':
            nc, nr, title, lines = el[1], el[2], el[3], el[4]; t = d.add_table(rows=nr, cols=nc); _borders(t, T['line'].lstrip('#'))
            _grid(t, [usable / nc] * nc)
            for r in range(nr):
                for k2 in range(nc):
                    cell = t.rows[r].cells[k2]; p = cell.paragraphs[0]; _run(p, title, 10, True, acc)
                    for lab in lines:
                        q = cell.add_paragraph(); q.paragraph_format.space_after = Pt(3)
                        if lab.startswith('[]'): _run(q, '   '.join('☐ ' + o for o in lab[2:].split('|')), 8)
                        else: _run(q, lab + ' ', 8, True, '#333333'); _run(q, '_' * max(6, 34 - len(lab)), 8, False, T['line'])
        elif k == 'sign':
            n = len(el[1]); t = d.add_table(rows=2, cols=n)
            for i, lab in enumerate(el[1]):
                _run(t.rows[0].cells[i].paragraphs[0], '_' * int(90 / n), 9, False, '#000000')
                _run(t.rows[1].cells[i].paragraphs[0], lab, 7.5, False, '#555555')
            _noborders(t); _grid(t, [usable / n] * n)
    fp = s.footer.paragraphs[0]; _run(fp, f"Form {f['code']}  ·  {REV}  ·  {brand}", 7, False, '#777777')
    d.save(path)
