import json
DISC="\n\n—\nMade by Freemans DocHub with the help of digital/AI art tools; every piece is hand-selected, upscaled and print-prepared by me."
CUSTOM="\n\nCUSTOM ORDERS: want a different size, color or theme? Send me a message!"
def desc(intro,n):
    s='s' if n>1 else ''
    files=f"5 high-resolution 300 DPI JPG files" if n==1 else f"5 ZIP files (one per ratio), each with all {n} artworks as 300 DPI JPGs"
    return (f"{intro}\n\nWHAT'S INCLUDED\n• {files}\n• 2x3 ratio: 4x6, 8x12, 12x18, 16x24, 20x30 in\n• 3x4 ratio: 6x8, 9x12, 12x16, 18x24 in\n• 4x5 ratio: 8x10, 16x20 in\n• 11x14 in\n• ISO: A5, A4, A3, A2\n\nHOW IT WORKS\nDownload, then print at home, at a local print shop or with an online print service. Frame not included.\n\nThis is an INSTANT DIGITAL DOWNLOAD. No physical item will be shipped. Colors can vary slightly between screens and printers. Because of the nature of digital files, all sales are final, but message me if anything is wrong with your files and I'll make it right.\n\nLICENSE: Personal use only. Please do not resell or share the files."+CUSTOM+DISC)
P={4:('Italian Christmas Kitchen Print, Panettone and Espresso','panettone, a moka pot espresso maker, oranges and holly on a rustic table'),
 5:('Italian Christmas Citrus Print, Lemons and Blood Oranges','a bowl of lemons and blood oranges with olive branches and red ribbon'),
 6:('Italian Christmas Cookie Print, Pizzelle and Espresso','a plate of pizzelle and biscotti with espresso and a candle'),
 7:('Snowy Cabin Watercolor Print, Cozy Winter Log Cabin','a snowy log cabin in the pines at blue hour with glowing windows'),
 8:('Red Truck Christmas Tree Print, Winter Watercolor','a red vintage pickup truck carrying a Christmas tree down a snowy road'),
 9:('Hot Cocoa Winter Window Print, Cozy Christmas Watercolor','a mug of hot cocoa, a knit blanket and a frosty window'),
 10:('Vintage Holly Botanical Print, Antique Christmas','an antique-style holly branch with red berries on aged paper'),
 11:('Vintage Poinsettia Botanical Print, Antique Christmas','an antique-style poinsettia on aged paper'),
 12:('Vintage Pine Cone Botanical Print, Antique Winter','an antique-style pine branch with pinecones on aged paper'),
 13:('Nutcracker Christmas Print, Vintage Storybook Toy Soldier','a classic red and gold nutcracker beside a decorated tree'),
 14:('Nutcracker Ballerina Print, Vintage Storybook Christmas','a ballerina in a pink tutu dancing among snowflakes'),
 15:('Sugar Plum Christmas Print, Vintage Nutcracker Candy','a sugar plum candy bowl with candy canes and gold ornaments'),
 16:('Cardinal Winter Watercolor Print, Red Bird on Pine','a red cardinal on a snowy pine branch with berries'),
 17:('Chickadee Winter Watercolor Print, Birds on Birch','two chickadees on a snowy birch branch'),
 18:('Snowy Owl Watercolor Print, Winter Bird','a snowy owl perched on a frosted branch')}
SETS=[('italian',[4,5,6],'Italian Christmas Kitchen Print Set of 3','vintage Italian holiday kitchen','retro Italian kitchen',['italian kitchen art','vintage kitchen art','christmas kitchen','espresso print','lemon print']),
 ('cabin',[7,8,9],'Cozy Winter Cabin Print Set of 3, Watercolor','cozy winter cabin watercolor','snowy cabin',['cabin wall art','winter watercolor','red truck print','hot cocoa print','cozy christmas art']),
 ('botanical',[10,11,12],'Vintage Christmas Botanical Print Set of 3, Holly Poinsettia Pine','vintage Christmas botanical','antique botanical',['botanical print','vintage botanical','holly print','poinsettia print','pine cone print']),
 ('nutcracker',[13,14,15],'Nutcracker Christmas Print Set of 3, Vintage Storybook','vintage storybook Nutcracker','nutcracker',['nutcracker print','ballerina print','nutcracker decor','vintage christmas','sugar plum fairy']),
 ('birds',[16,17,18],'Winter Birds Watercolor Print Set of 3, Cardinal Chickadee Owl','winter birds watercolor','winter birds',['bird wall art','cardinal print','chickadee print','snowy owl print','winter bird art'])]
COMMON=['christmas wall art','printable wall art','holiday decor','digital download','christmas print','winter decor','farmhouse christmas','gallery wall']
L=[]
for key,arts,stitle,style,short,tg in SETS:
    tags=(tg+COMMON)[:13]
    L.append(dict(slug=f'W01-{key}-set',arts=arts,base=f'{key}_set_of_3',price=3.99,
      title=f'{stitle}, Printable Christmas Wall Art, Holiday Decor Digital Download',
      tags=tags,description=desc(f'A matching set of 3 {style} prints: '+'; '.join(P[a][1] for a in arts)+'. Hang them together for an instant holiday gallery wall.',3),category_hint='Digital Prints'))
    for a in arts:
        L.append(dict(slug=f'W01-{key}-{a:02d}',arts=[a],base=f'{key}_{a:02d}',price=1.99,
          title=f'{P[a][0]}, Printable Christmas Wall Art, Holiday Decor Digital Download',
          tags=tags,description=desc(f'A {style} print of {P[a][1]}. Also available as a matching set of 3 in my shop.',1),category_hint='Digital Prints'))
for x in L:
    assert len(x['tags'])==13 and all(len(t)<=20 for t in x['tags']),x['tags']
    assert len(x['title'])<=140,(len(x['title']),x['title'])
json.dump({'listings':L},open('spec_w01.json','w'),indent=1);print(len(L))
