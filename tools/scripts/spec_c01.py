import json, os
from pypdf import PdfReader, PdfWriter
O='C01/out'; os.makedirs(O+'/pdf',exist_ok=True)
DISC="\n\n—\nMade by Freemans DocHub with the help of digital/AI art tools; every page is hand-selected, cleaned up and print-prepared by me."
def sub(name, pages):
    for k in ('letter','a4'):
        r=PdfReader(f'{O}/cozy_cottage_cafe_coloring_{k}.pdf'); w=PdfWriter()
        for p in pages: w.add_page(r.pages[p-1])
        w.write(f'{O}/pdf/{name}_{k}.pdf')
    files=[]
    for p in pages: files+= [f'{O}/page_{p:02d}_letter.png', f'{O}/page_{p:02d}_a4.png']
    return files+[f'{O}/pdf/{name}_letter.pdf', f'{O}/pdf/{name}_a4.pdf']
BASE_TAGS=['coloring pages','printable coloring','adult coloring','cozy coloring','coloring book pdf','relaxing activity','instant download']
def desc(intro,n,extra):
    return (f"{intro}\n\nWHAT'S INCLUDED\n• {n} coloring pages\n• US Letter (8.5x11 in) PDF + PNG\n• A4 PDF + PNG\n• 300 DPI crisp black line art, print at home as many times as you like\n\n{extra}\n\nGREAT FOR\nRelaxing evenings, mindful coloring with markers or colored pencils, cozy gifts, teens and adults, rainy-day activities.\n\nThis is an INSTANT DIGITAL DOWNLOAD. No physical item will be shipped. Because of the nature of digital files, all sales are final, but message me if anything is wrong with your files and I'll make it right.\n\nLICENSE: Personal use, and printing for your own family or classroom. Please do not resell or share the files."+DISC)
L=[]
all12=list(range(1,13)); cafe=[2,3,4,6,11]; homes=[1,5,7,8,9,10,12]
L.append(dict(slug='C01-L01_cozy_cottage_cafe_12',set='coloring',kind='coloring',price=3.29,
 files=sub('cozy_cottage_cafe_12',all12),
 title='Cozy Cottage Coloring Pages, 12 Printable Cozy Coloring Book PDF, Cafe, Bakery, Reading Nook, Mushroom House, Adult Coloring',
 tags=['cottagecore coloring','cozy cottage','cafe coloring page','bakery coloring','mushroom house']+BASE_TAGS+['bold easy coloring'],
 description=desc('12 printable cozy coloring pages: little cottages, a corner cafe, a bakery counter, a rainy-day reading nook, a mushroom house and more, drawn in bold, clean, relaxing line art.',12,'BEST VALUE: the complete 12-page Cozy Cottage & Cafe collection.'),
 cover_title='Cozy Cottage & Cafe',cover_sub='12 Printable Coloring Pages',cover_badge='PRINTABLE PDF + PNG · LETTER & A4',cover_foot='Instant download · print at home',
 zipbase='cozy_cottage_cafe_coloring_12',details=['12 cozy coloring pages','US Letter PDF + PNG','A4 PDF + PNG','300 DPI crisp line art','Print unlimited at home'],
 category_hint='Coloring Pages'))
L.append(dict(slug='C01-L02_cozy_cafe_bakery_5',set='coloring',kind='coloring',price=1.99,
 files=sub('cozy_cafe_bakery_5',cafe),
 title='Cozy Cafe and Bakery Coloring Pages, 5 Printable Coffee Shop Coloring Sheets, Kitchen, Reading Nook, Adult Coloring PDF',
 tags=['cafe coloring page','bakery coloring','coffee coloring','kitchen coloring','reading nook']+BASE_TAGS+['cozy coffee shop'],
 description=desc('5 printable cozy coloring pages: a corner cafe, a farmhouse kitchen, a reading nook with a sleeping cat, a bakery counter full of treats and a latte-and-cake table, in bold, relaxing line art.',5,'Want more? The full 12-page Cozy Cottage & Cafe collection is in my shop.'),
 cover_title='Cozy Cafe & Bakery',cover_sub='5 Printable Coloring Pages',cover_badge='PRINTABLE PDF + PNG · LETTER & A4',cover_foot='Instant download · print at home',
 zipbase='cozy_cafe_bakery_coloring_5',details=['5 cozy coloring pages','US Letter PDF + PNG','A4 PDF + PNG','300 DPI crisp line art','Print unlimited at home'],
 category_hint='Coloring Pages'))
L.append(dict(slug='C01-L03_cottage_homes_7',set='coloring',kind='coloring',price=2.49,
 files=sub('cottage_homes_7',homes),
 title='Cottagecore Coloring Pages, 7 Printable Cottage House Coloring Sheets, Mushroom House, Treehouse, Winter Cottage, Adult Coloring PDF',
 tags=['cottagecore coloring','cottage coloring','mushroom house','treehouse coloring','house coloring page']+BASE_TAGS+['garden coloring'],
 description=desc('7 printable cottagecore coloring pages: a stone cottage with a cat, a mushroom house, a garden gate, a treehouse, an attic bedroom, a riverside cottage and a snowy winter cottage, in bold, relaxing line art.',7,'Want more? The full 12-page Cozy Cottage & Cafe collection is in my shop.'),
 cover_title='Cottagecore Homes',cover_sub='7 Printable Coloring Pages',cover_badge='PRINTABLE PDF + PNG · LETTER & A4',cover_foot='Instant download · print at home',
 zipbase='cottage_homes_coloring_7',details=['7 cozy coloring pages','US Letter PDF + PNG','A4 PDF + PNG','300 DPI crisp line art','Print unlimited at home'],
 category_hint='Coloring Pages'))
for x in L:
    assert len(x['tags'])==13 and all(len(t)<=20 for t in x['tags']), x['tags']
    assert len(x['title'])<=140 and sum(x['title'].count(c) for c in '%&:')<=1, x['title']
json.dump({'listings':L},open('spec_c01.json','w'),indent=1)
print('ok')
