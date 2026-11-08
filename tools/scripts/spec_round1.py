import json, os
from PIL import Image

AI = ("AI DISCLOSURE: These designs were created by me using AI image generation tools "
      "(I wrote the prompts, selected the results, and edited/finished every file: background removal, "
      "cleanup, upscaling and print preparation).")
LIC = ("LICENSE: Personal use and small commercial use (up to 500 physical products, e.g. stickers, cards, "
       "mugs, shirts). You may NOT resell, share or redistribute the digital files themselves, alone or in "
       "a bundle, or use them in print-on-demand listings as stand-alone clipart.")
NOTE = ("This is an INSTANT DIGITAL DOWNLOAD. No physical item will be shipped. Colors may vary slightly "
        "between screens and printers. Because of the nature of digital files, all sales are final, but "
        "message me if anything is wrong with your files and I'll make it right.")

def clip_desc(name, n, items, extra=''):
    return (f"{name}: {n} hand-painted-style watercolor PNG clipart designs with transparent backgrounds.\n\n"
            f"WHAT'S INCLUDED\n• {n} individual PNG files ({items})\n• Transparent background\n"
            f"• High resolution: about 12 inches on the longest side at 300 DPI (3600 px)\n"
            f"• Delivered as ZIP file(s)\n\nPERFECT FOR\nChristmas cards, invitations, tags, scrapbooking, "
            f"junk journals, stickers, sublimation, planners, crafts, labels and social media graphics.\n\n"
            f"{extra}{NOTE}\n\n{LIC}\n\n{AI}")

def col_desc(n, extra=''):
    return (f"{n} printable Christmas coloring pages for adults and kids — cozy holiday scenes with bold, "
            f"clean line art.\n\nWHAT'S INCLUDED\n• {n} coloring pages\n• US Letter (8.5x11 in) PDF + PNG\n"
            f"• A4 PDF + PNG\n• 300 DPI, print at home as many times as you like\n\n{extra}"
            f"GREAT FOR\nFamily activities, classroom parties, Christmas Eve boxes, kids' table at holiday dinners, "
            f"relaxing adult coloring.\n\n{NOTE}\n\nLICENSE: Personal use, and printing for your own classroom "
            f"or family. Please do not resell or share the files.\n\n{AI}")

A = 'b001b_out'; B = 'b002_out'; C = 'b003_out'
xmas = ['01_cocoa', '02_tree', '03_gift', '04_gingerbread', '05_holly', '06_truck', '07_stocking',
        '08_candy_canes', '09_pinecone', '10_ornament', '11_wreath', '12_cardinal']
wood = ['01_fox', '02_bunny', '03_fawn', '04_owl', '05_hedgehog', '06_bear', '07_raccoon', '08_squirrel',
        '09_chickadee', '10_badger', '11_moose', '12_mouse']
XT = ['christmas clipart', 'watercolor clipart', 'christmas png', 'vintage christmas', 'holiday clipart',
      'cozy christmas', 'clipart bundle', 'transparent png', 'xmas sublimation', 'junk journal',
      'card making', 'scrapbook clipart', 'commercial use']
WT = ['woodland clipart', 'winter animals png', 'christmas animals', 'watercolor animals', 'cute fox clipart',
      'nursery clipart', 'woodland christmas', 'clipart bundle', 'transparent png', 'winter clipart',
      'baby animals png', 'sublimation png', 'commercial use']
CT = ['christmas coloring', 'coloring pages', 'printable coloring', 'kids coloring page', 'adult coloring',
      'holiday activity', 'christmas printable', 'coloring book pdf', 'winter coloring', 'xmas activity',
      'classroom activity', 'christmas eve box', 'instant download']

L = []
def clip(slug, set_, title, price, idx, names, ttl, sub, tags, cname, zipbase, extra=''):
    base = A if set_ == 'xmas' else B
    L.append(dict(slug=slug, set=set_, kind='clipart', title=title, price=price,
                  files=[f'{base}/{names[i]}.png' for i in idx], tags=tags,
                  description=clip_desc(cname, len(idx), ', '.join(names[i][3:].replace('_', ' ') for i in idx), extra),
                  cover_title=ttl, cover_sub=sub, cover_badge='PNG · TRANSPARENT · 300 DPI',
                  cover_foot=f'{len(idx)} high-resolution watercolor clipart files', zipbase=zipbase,
                  details=[f'{len(idx)} individual PNG files', 'Transparent backgrounds', '3600 px · 300 DPI (12 in)',
                           'ZIP download', 'Personal + small commercial use'],
                  category_hint='Craft Supplies & Tools > Visual Arts > Images > Digital Clip Art (digital, Designed by seller, AI-generated: yes)'))

all12 = list(range(12))
clip('R01-L01_xmas_watercolor_bundle12', 'xmas',
     'Vintage Christmas Watercolor Clipart Bundle, 12 PNG, Cozy Holiday Clip Art, Red Truck, Cardinal, Wreath, Transparent, Commercial Use',
     3.79, all12, xmas, 'Vintage Christmas Clipart', '12 Watercolor PNG Designs', XT, 'Vintage Christmas Watercolor Clipart', 'vintage_christmas_clipart_12png')
clip('R01-L02_xmas_cozy_pack4', 'xmas',
     'Cozy Christmas Watercolor Clipart Set, 4 PNG, Hot Cocoa Mug, Gift Box, Knit Stocking, Candy Canes, Transparent Holiday Clip Art',
     2.99, [0, 2, 6, 7], xmas, 'Cozy Christmas Clipart', '4 Watercolor PNG Designs', XT[:12] + ['hot cocoa png'], 'Cozy Christmas Watercolor Clipart', 'cozy_christmas_clipart_4png')
clip('R01-L03_xmas_greenery_pack4', 'xmas',
     'Christmas Greenery Watercolor Clipart, 4 PNG, Holly, Pinecone, Plaid Wreath, Cardinal Bird, Rustic Winter Clip Art, Transparent',
     2.99, [4, 8, 10, 11], xmas, 'Christmas Greenery Clipart', '4 Watercolor PNG Designs', XT[:12] + ['cardinal clipart'], 'Christmas Greenery Watercolor Clipart', 'christmas_greenery_clipart_4png')
clip('R01-L04_xmas_village_pack4', 'xmas',
     'Christmas Tree, Gingerbread House, Red Truck, Ornament Watercolor Clipart, 4 PNG, Vintage Holiday Clip Art, Transparent Background',
     2.99, [1, 3, 5, 9], xmas, 'Christmas Village Clipart', '4 Watercolor PNG Designs', XT[:12] + ['red truck png'], 'Christmas Village Watercolor Clipart', 'christmas_village_clipart_4png')
clip('R01-L05_woodland_bundle12', 'wood',
     'Winter Woodland Animals Watercolor Clipart Bundle, 12 PNG, Christmas Fox, Bunny, Deer, Owl, Bear, Cute Nursery Clip Art, Commercial Use',
     3.79, all12, wood, 'Winter Woodland Animals', '12 Watercolor PNG Designs', WT, 'Winter Woodland Animals Watercolor Clipart', 'winter_woodland_animals_12png')
clip('R01-L06_woodland_babies_pack4', 'wood',
     'Winter Baby Animals Watercolor Clipart, 4 PNG, Fox in Scarf, White Bunny, Christmas Fawn, Snowy Owl, Woodland Nursery Clip Art',
     2.99, [0, 1, 2, 3], wood, 'Winter Baby Animals', '4 Watercolor PNG Designs', WT[:12] + ['snowy owl png'], 'Winter Baby Animals Watercolor Clipart', 'winter_baby_animals_4png')
clip('R01-L07_woodland_critters_pack4', 'wood',
     'Cozy Christmas Critters Watercolor Clipart, 4 PNG, Hedgehog, Bear Cub with Cocoa, Raccoon, Squirrel, Cute Winter Animal Clip Art',
     2.99, [4, 5, 6, 7], wood, 'Cozy Christmas Critters', '4 Watercolor PNG Designs', WT[:12] + ['hedgehog clipart'], 'Cozy Christmas Critters Watercolor Clipart', 'cozy_christmas_critters_4png')
clip('R01-L08_woodland_friends_pack4', 'wood',
     'Winter Friends Watercolor Clipart, 4 PNG, Chickadee, Badger, Moose with Lights, Sleeping Mouse in Teacup, Christmas Animal Clip Art',
     2.99, [8, 9, 10, 11], wood, 'Winter Woodland Friends', '4 Watercolor PNG Designs', WT[:12] + ['moose clipart'], 'Winter Woodland Friends Watercolor Clipart', 'winter_woodland_friends_4png')

# mega bundle (both sets)
L.append(dict(L[0]) | dict(slug='R01-L09_christmas_mega_bundle24', set='mega',
     title='Christmas Watercolor Clipart Mega Bundle, 24 PNG, Vintage Holiday + Winter Woodland Animals, Fox, Cardinal, Truck, Commercial Use',
     price=5.49, files=[f'{A}/{n}.png' for n in xmas] + [f'{B}/{n}.png' for n in wood],
     tags=['christmas clipart', 'clipart bundle', 'woodland clipart', 'watercolor clipart', 'christmas png',
           'winter animals png', 'vintage christmas', 'mega bundle', 'holiday clipart', 'transparent png',
           'sublimation png', 'junk journal', 'commercial use'],
     description=clip_desc('Christmas Watercolor Clipart Mega Bundle', 24,
                           'all 12 Vintage Christmas designs + all 12 Winter Woodland Animals',
                           'BEST VALUE: this bundle includes everything from both of my Christmas clipart sets. Mega bundle files are 3000 px (10 in at 300 DPI).\n\n'),
     long_side=3000, cover_title='Christmas Mega Bundle', cover_sub='24 Watercolor PNG Designs',
     cover_foot='Vintage Christmas + Winter Woodland Animals', zipbase='christmas_watercolor_mega_bundle_24png',
     details=['24 individual PNG files', 'Transparent backgrounds', '3000 px · 300 DPI (10 in)', 'ZIP download', 'Personal + small commercial use']))

def colset(slug, pages, title, price, sub, extra=''):
    files = []
    for p in pages: files += [f'{C}/p{p:02d}_letter.png', f'{C}/p{p:02d}_a4.png']
    # subset pdfs
    os.makedirs(f'{C}/pdf', exist_ok=True)
    for k in ('letter', 'a4'):
        ims = [Image.open(f'{C}/p{p:02d}_{k}.png') for p in pages]
        pdf = f'{C}/pdf/{slug}_{k}.pdf'
        ims[0].save(pdf, save_all=True, append_images=ims[1:], resolution=300)
        files.append(pdf)
    L.append(dict(slug=slug, set='coloring', kind='coloring', title=title, price=price, files=files, tags=CT,
                  description=col_desc(len(pages), extra), cover_title='Christmas Coloring Pages',
                  cover_sub=sub, cover_badge='PRINTABLE PDF + PNG · LETTER & A4',
                  cover_foot='Instant download · print at home', zipbase=slug.split('_', 1)[1],
                  details=[f'{len(pages)} coloring pages', 'US Letter PDF + PNG', 'A4 PDF + PNG',
                           '300 DPI crisp line art', 'Print unlimited at home'],
                  category_hint='Paper & Party Supplies > Paper > Coloring Pages (digital, Designed by seller, AI-generated: yes)'))

colset('R01-L10_christmas_coloring_20', list(range(1, 21)),
       '20 Christmas Coloring Pages, Printable PDF, Cozy Holiday Coloring Book for Kids and Adults, Snowman, Gingerbread, Reindeer, Instant Download',
       3.79, '20 Printable Pages', 'BEST VALUE: the complete 20-page set.\n\n')
colset('R01-L11_christmas_coloring_vol1', list(range(1, 11)),
       '10 Christmas Coloring Pages Vol 1, Printable PDF, Cozy Cottage, Snowman Family, Gingerbread House, Mandala, Kids & Adults Activity',
       2.99, '10 Printable Pages · Vol 1')
colset('R01-L12_christmas_coloring_vol2', list(range(11, 21)),
       '10 Christmas Coloring Pages Vol 2, Printable PDF, Teddy Bear, Cardinals, Sleigh, Kittens, Snow Globe, Holiday Activity for Kids & Adults',
       2.99, '10 Printable Pages · Vol 2')

json.dump({'listings': L}, open('/home/claude/spec_round1.json', 'w'), indent=1)
for l in L: assert len(l['title']) <= 140, (l['slug'], len(l['title'])); assert all(len(t) <= 20 for t in l['tags']), l['slug']; assert len(l['tags']) == 13
print(len(L), 'listings')
