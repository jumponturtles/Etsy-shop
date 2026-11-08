import json, glob
O='C04/out'
DISC="\n\n—\nMade by Freemans DocHub with the help of digital/AI art tools; every page is hand-selected, cleaned up and print-prepared by me."
CUSTOM="\n\nCUSTOM ORDERS: want a custom coloring page or a theme you don't see? Send me a message!"
def desc(intro,n,extra):
    return (f"{intro}\n\nWHAT'S INCLUDED\n• {n} coloring pages\n• US Letter (8.5x11 in) PDF + PNG\n• A4 PDF + PNG\n• 300 DPI crisp black line art, print at home as many times as you like\n\n{extra}\n\nGREAT FOR\nRelaxing evenings, mindful coloring with markers, gel pens or colored pencils, ocean lovers, beach house fun, teens and adults.\n\nThis is an INSTANT DIGITAL DOWNLOAD. No physical item will be shipped. Because of the nature of digital files, all sales are final, but message me if anything is wrong with your files and I'll make it right.\n\nLICENSE: Personal use, and printing for your own family or classroom. Please do not resell or share the files."+CUSTOM+DISC)
files=sorted(glob.glob(O+'/page_*_letter.png'))+sorted(glob.glob(O+'/page_*_a4.png'))+[O+'/ocean_abstract_coloring_letter.pdf',O+'/ocean_abstract_coloring_a4.pdf']
L=[dict(slug='C04-L01_ocean_abstract_12',set='coloring',kind='coloring',price=3.29,files=files,
 title='Ocean Coloring Pages for Adults, 12 Printable Zentangle Sea Life Coloring Book PDF, Turtle, Octopus, Whale, Jellyfish, Mandala',
 tags=['ocean coloring','sea life coloring','zentangle coloring','mandala coloring','adult coloring','coloring book pdf','printable coloring','sea turtle coloring','octopus coloring','whale coloring','jellyfish coloring','beach coloring page','instant download'],
 description=desc('12 printable ocean coloring pages full of intricate zentangle and mandala-style detail: crashing waves, a seashell mandala, a sea turtle, a coral reef, a lacy jellyfish, a patterned whale, a seashell collection, a swirling octopus, a spiral school of fish, seahorses in kelp, a stained-glass reef and a manta ray over the sand.',12,'Detailed enough to keep you coloring for hours, with clean closed outlines that work with any medium.'),
 cover_title='Ocean Dreams',cover_sub='12 Detailed Coloring Pages',cover_badge='PRINTABLE PDF + PNG · LETTER & A4',cover_foot='Instant download · print at home',
 zipbase='ocean_coloring_12',details=['12 detailed ocean pages','US Letter PDF + PNG','A4 PDF + PNG','300 DPI crisp line art','Print unlimited at home'],category_hint='Coloring Pages')]
for x in L:
    assert len(x['tags'])==13 and all(len(t)<=20 for t in x['tags']), x['tags']
    assert len(x['title'])<=140 and sum(x['title'].count(c) for c in '%&:')<=1, x['title']
json.dump({'listings':L},open('spec_c04.json','w'),indent=1); print('ok', len(files))
