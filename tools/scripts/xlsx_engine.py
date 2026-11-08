"""Excel log builder with formulas. spec: dict(title, sheet, fields=[...], cols=[(name,width,kind,formula)], rows, totals={col_letter:'SUM'}, notes)
kind: 'text'|'num'|'money'|'date'|'formula'. formula uses {r} for row number."""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule

def build(path, sheets, theme_hex='1F3A5F', light='E8EEF5', brand='Freemans DocHub'):
    wb = Workbook(); wb.remove(wb.active)
    thin = Side(style='thin', color='9AA8B8'); B = Border(left=thin, right=thin, top=thin, bottom=thin)
    for sp in sheets:
        ws = wb.create_sheet(sp['sheet'][:31]); ncol = len(sp['cols'])
        ws.sheet_view.showGridLines = False
        ws['A1'] = sp['title']; ws['A1'].font = Font(name='Calibri', size=16, bold=True, color=theme_hex)
        ws['A2'] = sp.get('subtitle', ''); ws['A2'].font = Font(size=9, italic=True, color='666666')
        r = 3
        for i, fl in enumerate(sp.get('fields', [])):
            c = 1 + (i % 2) * 3; rr = r + i // 2
            ws.cell(rr, c, fl).font = Font(bold=True, size=9)
            cell = ws.cell(rr, c + 1); cell.border = Border(bottom=thin)
        r += (len(sp.get('fields', [])) + 1) // 2 + 1
        hr = r
        for ci, (n, w, kind, fm) in enumerate(sp['cols'], 1):
            c = ws.cell(hr, ci, n); c.font = Font(bold=True, color='FFFFFF', size=9)
            c.fill = PatternFill('solid', fgColor=theme_hex); c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True); c.border = B
            ws.column_dimensions[get_column_letter(ci)].width = w
        ws.row_dimensions[hr].height = 30
        first = hr + 1; last = hr + sp['rows']
        for rr in range(first, last + 1):
            for ci, (n, w, kind, fm) in enumerate(sp['cols'], 1):
                c = ws.cell(rr, ci); c.border = B; c.font = Font(size=9)
                if (rr - first) % 2: c.fill = PatternFill('solid', fgColor='F7F9FB')
                if kind == 'money': c.number_format = '$#,##0.00'
                elif kind == 'num': c.number_format = '#,##0.##'
                elif kind == 'date': c.number_format = 'mm/dd/yyyy'
                if fm:
                    c.value = '=' + fm.format(r=rr)
                    if kind in ('money',): c.number_format = '$#,##0.00'
                    c.fill = PatternFill('solid', fgColor=light)
        if sp.get('totals'):
            tr = last + 1
            ws.cell(tr, 1, 'TOTAL').font = Font(bold=True)
            for col, fn in sp['totals'].items():
                ci = ord(col) - 64; c = ws.cell(tr, ci, f'={fn}({col}{first}:{col}{last})')
                c.font = Font(bold=True); c.number_format = '$#,##0.00' if sp['cols'][ci - 1][2] in ('money',) or 'money' in str(sp['cols'][ci - 1]) else '#,##0.##'
                c.border = B; c.fill = PatternFill('solid', fgColor=light)
        for rule in sp.get('cond', []):  # (range_cols, formula, fill_hex)
            rng = f'{rule[0][0]}{first}:{rule[0][1]}{last}'
            ws.conditional_formatting.add(rng, FormulaRule(formula=[rule[1].format(r=first)], fill=PatternFill('solid', fgColor=rule[2]), font=Font(bold=True)))
        for dvspec in sp.get('lists', []):  # (col_letter, 'a,b,c')
            dv = DataValidation(type='list', formula1=f'"{dvspec[1]}"', allow_blank=True); ws.add_data_validation(dv)
            dv.add(f'{dvspec[0]}{first}:{dvspec[0]}{last}')
        for cell, val, fmt, bold in sp.get('extra', []):
            c = ws[cell]; c.value = val; c.font = Font(bold=bold, size=10 if bold else 9)
            if fmt: c.number_format = fmt
            if isinstance(val, str) and val.startswith('='): c.fill = PatternFill('solid', fgColor=light); c.border = B
        if sp['rows']: ws.freeze_panes = ws.cell(first, 1)
        import re as _re
        n = max([last + (3 if sp.get('totals') else 2)] + [int(_re.sub(r'[A-Z]', '', e[0])) + 2 for e in sp.get('extra', [])])
        for note in sp.get('notes', []):
            ws.cell(n, 1, note).font = Font(size=8, italic=True, color='666666'); n += 1
        ws.cell(n + 1, 1, f'{brand} · Rev. 11/2026').font = Font(size=7, color='999999')
        ws.page_setup.orientation = 'landscape' if ncol > 7 else 'portrait'; ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 0
        ws.sheet_properties.pageSetUpPr.fitToPage = True; ws.print_title_rows = f'{hr}:{hr}'
    wb.save(path)
