import json
DISC="\n\n—\nMade by Freemans DocHub with the help of digital/AI art tools; every design is hand-selected, upscaled, lettered and print-prepared by me."
CUSTOM="\n\nCUSTOM ORDERS: want your own greeting, a family name or a different design? Send me a message!"
def desc(intro, cards):
    return (f"{intro}\n\nTHE 10 DESIGNS\n" + "\n".join(f"• {c}" for c in cards) +
     "\n\nWHAT'S INCLUDED\n• 10 card fronts with greetings (5x7 in, 300 DPI JPG)\n• 10 matching inside message pages\n• 10 no-text fronts, so you can write your own message\n• 1 print-ready PDF (Letter size with crop marks) for every front and inside page\n\nHOW TO USE\nPrint at home on cardstock, trim on the crop marks and fold or pair with an envelope. You can also send the files to a local print shop or an online printer, or text and email the JPGs as digital Christmas cards.\n\nThis is an INSTANT DIGITAL DOWNLOAD. No physical item will be shipped. Colors can vary slightly between screens and printers. Because of the nature of digital files, all sales are final, but message me if anything is wrong with your files and I'll make it right.\n\nLICENSE: Personal use. Print as many as you like for your own family and friends. Please do not resell or share the files."+CUSTOM+DISC)
L=[dict(slug='K01-classic_christmas_cards_10_pack',price=3.99,
 title='Printable Christmas Cards Set of 10, Classic Cozy Holiday Card Pack, Vintage Santa, Nutcracker, Snowman, Gingerbread, 5x7 Instant Download',
 tags=['christmas cards','printable christmas','christmas card set','holiday cards','5x7 christmas card','vintage santa card','nutcracker card','snowman card','gingerbread card','cat christmas card','christmas card pack','xmas card printable','digital christmas'],
 description=desc('Ten completely different printable Christmas cards in one download, so you have the right card for everyone on your list: classic, cozy, cute and elegant. Each card is lettered with its own matching greeting.',
  ['Watercolor Wreath · "Merry Christmas"','Vintage Santa · "Merry Christmas"','Gingerbread House · "Sweet Christmas Wishes"','Snowy Village · "Silent Night"','Watercolor Nutcracker · "Merry Christmas"','Cheerful Snowman · "Let It Snow"','Kitten in a Stocking · "Meowy Christmas"','Woodland Friends · "Merry Christmas"','Navy & Gold Ornaments · "Season\'s Greetings"','Hot Cocoa · "Warm Winter Wishes"'])),
 dict(slug='K01-modern_christmas_cards_10_pack',price=3.99,
 title='Modern Christmas Cards Printable Set of 10, Boho Mid Century Holiday Card Pack, Nativity, Scandinavian, Pink, Plaid, 5x7 Digital Download',
 tags=['christmas cards','modern christmas','boho christmas card','mid century card','christmas card set','nativity card','pink christmas card','plaid christmas','scandinavian card','holiday card pack','5x7 holiday card','printable xmas card','penguin card'],
 description=desc('Ten completely different modern Christmas cards in one download, from retro mid-century and boho to Scandinavian folk, pink Christmas and a peaceful nativity. Each card is lettered with its own matching greeting.',
  ['Mid-Century Trees · "Happy Holidays"','Minimal Pine & Gold · "Season\'s Greetings"','Buffalo Plaid · "Merry Christmas"','Candy Stripe Bow · "Merry & Bright"','Boho Trees · "Happy Holidays"','Nativity · "O Holy Night"','Scandinavian Folk · "God Jul"','Penguin Family · "Merry Christmas"','Retro Pink Christmas · "Merry & Bright"','Holly & Mistletoe · "Season\'s Greetings"']))]
for x in L:
    assert len(x['tags'])==13 and all(len(t)<=20 for t in x['tags']),[t for t in x['tags'] if len(t)>20]
    assert len(x['title'])<=140 and sum(x['title'].count(c) for c in '%&:')<=1,(len(x['title']))
json.dump({x['slug']:{'t':x['title'],'p':'%.2f'%x['price'],'g':','.join(x['tags']),'d':x['description'],'c':True} for x in L},open('/home/claude/k01_fill.json','w'),indent=1);print('ok')
