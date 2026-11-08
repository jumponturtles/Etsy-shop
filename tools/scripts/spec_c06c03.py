import json, glob
DISC="\n\n—\nMade by Freemans DocHub with the help of digital/AI art tools; every page is hand-selected, cleaned up and print-prepared by me."
CUSTOM="\n\nCUSTOM ORDERS: want a custom coloring page or a theme you don't see? Send me a message!"
def desc(intro,n,extra,great):
    return (f"{intro}\n\nWHAT'S INCLUDED\n• {n} coloring pages\n• US Letter (8.5x11 in) PDF + PNG\n• A4 PDF + PNG\n• 300 DPI crisp black line art, print at home as many times as you like\n\n{extra}\n\nGREAT FOR\n{great}\n\nThis is an INSTANT DIGITAL DOWNLOAD. No physical item will be shipped. Because of the nature of digital files, all sales are final, but message me if anything is wrong with your files and I'll make it right.\n\nLICENSE: Personal use, and printing for your own family or classroom. Please do not resell or share the files."+CUSTOM+DISC)
def files(O,name): return sorted(glob.glob(O+'/page_*_letter.png'))+sorted(glob.glob(O+'/page_*_a4.png'))+[f'{O}/{name}_letter.pdf',f'{O}/{name}_a4.pdf']
L=[dict(slug='C06-L01_celestial_20',set='coloring',kind='coloring',price=4.00,files=files('C06/out','celestial_coloring'),
 title='Celestial Coloring Pages for Adults, 20 Printable Sun Moon Stars Mandala Coloring Book PDF, Zodiac, Mystical Boho Coloring Sheets',
 tags=['celestial coloring','moon coloring page','sun and moon','zodiac coloring','mandala coloring','adult coloring','coloring book pdf','printable coloring','boho coloring page','mystical coloring','star coloring page','witchy coloring','instant download'],
 description=desc('20 printable celestial coloring pages packed with mandala and paisley detail: a sun and moon mandala, moon phases, a crescent moon with hanging stars, a swirling galaxy, a star map, a moon moth, a shooting star, an owl on the moon, an armillary sphere, a stained-glass sun, a hand holding the moon, a whale swimming through space, a sleeping moon cat, crystals under the stars, a hot air balloon, moonflowers, a zodiac wheel and a starlit lighthouse.',20,'Intricate enough to keep you coloring for hours, with clean closed outlines for markers, gel pens or colored pencils.','Relaxing evenings, mindful coloring, celestial and boho lovers, teens and adults, a cozy self-care gift.'),
 cover_title='Celestial Dreams',cover_sub='20 Detailed Coloring Pages',cover_badge='PRINTABLE PDF + PNG · LETTER & A4',cover_foot='Instant download · print at home',
 zipbase='celestial_coloring_20',details=['20 detailed celestial pages','US Letter PDF + PNG','A4 PDF + PNG','300 DPI crisp line art','Print unlimited at home'],category_hint='Coloring Pages'),
 dict(slug='C03-L01_sampler_20',set='coloring',kind='coloring',price=0.75,files=files('C03/out','variety_sampler_coloring'),
 title='Adult Coloring Pages Sampler, 20 Printable Fantasy Animal Coloring Sheets PDF, Dragon, Phoenix, Mermaid, Castle, Owl, Mandala',
 tags=['coloring sampler','adult coloring','fantasy coloring','dragon coloring page','mermaid coloring','animal coloring','coloring book pdf','printable coloring','mandala coloring','castle coloring','coloring sheets','phoenix coloring','instant download'],
 description=desc('A 20-page sampler of our detailed coloring styles: a patterned mandala, a sleeping dragon, a phoenix, an enchanted forest, a fairy-tale castle, a mandala elephant, a wolf dreamcatcher, a steampunk clock, a mushroom cottage, a mermaid, an astronaut in space, a sugar skull, a cat on books, an eastern dragon, a forest deer, a waterfall castle, an angel, a sea turtle, a nautical compass and a butterfly.',20,'A great way to try a little of everything before picking a full themed book.','Trying out adult coloring, gifts, rainy days, teens and adults who like variety.'),
 cover_title='Coloring Sampler',cover_sub='20 Pages · Lots of Styles',cover_badge='PRINTABLE PDF + PNG · LETTER & A4',cover_foot='Instant download · print at home',
 zipbase='coloring_sampler_20',details=['20 pages, 20 different themes','US Letter PDF + PNG','A4 PDF + PNG','300 DPI crisp line art','Print unlimited at home'],category_hint='Coloring Pages')]
for x in L:
    assert len(x['tags'])==13 and all(len(t)<=20 for t in x['tags']), x['tags']
    assert len(x['title'])<=140 and sum(x['title'].count(c) for c in '%&:')<=1, (len(x['title']),x['title'])
json.dump({'listings':L},open('spec_c06c03.json','w'),indent=1); print('ok')
