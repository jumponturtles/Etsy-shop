import json
DISC="\n\n—\nMade by Freemans DocHub with the help of digital/AI art tools; every emote is hand-selected, cut out, cleaned up and sized by me."
def desc(intro, n, extra):
    return (f"{intro}\n\nWHAT'S INCLUDED\n• {n} emotes, transparent PNG\n• Twitch sizes: 112px, 56px, 28px\n• 512px hi-res for Discord emoji/stickers, YouTube, Kick, 7TV and BTTV\n• Quick upload guide\n\n{extra}\n\nINSTANT DIGITAL DOWNLOAD. No physical item will be shipped. Because of the nature of digital files, all sales are final, but message me if anything is wrong with your files and I'll make it right.\n\nLICENSE: For use on your own stream, channel or server. Please do not resell, redistribute or claim as your own."+DISC)
BASE=['twitch emotes','discord emotes','emote pack','streamer emotes','sub emotes','youtube emotes','stream assets','chibi emotes','cute emotes','kick emotes']
P=[ # key, name, kind phrase, set, 3 specific tags, bundle name
('gamerskull','Gamer Skull','skull gamer','Rage, LUL, Clutch, RIP, Salute, Sus',['skull emotes','gamer emotes','dark emotes'],'Gamer'),
('pixelslime','Pixel Slime King','pixel art slime','Hi, Hype, Love, Cry, Rage, Sleep',['pixel emotes','retro emotes','slime emote'],'Gamer'),
('magicalgirl','Magical Girl','anime magical girl','Wave, Heart, Blush, Cry, Pout, Magic',['anime emotes','magical girl','pink anime emote'],'Girly'),
('animeboy','Hoodie Boy','anime boy','Cool, Facepalm, Rage, LUL, Thumbs Up, Sleepy',['anime emotes','anime boy emote','facepalm emote'],'Gamer'),
('ghost','Spooky Cute Ghost','ghost','Boo, Love, Scared, Cry, LUL, Cozy',['ghost emotes','spooky emotes','halloween emote'],'Kids'),
('babyrex','Baby T-Rex','dinosaur','Roar, Hug, Cry, Laugh, Hype, Sleep',['dinosaur emotes','trex emote','kids emotes'],'Kids'),
('boba','Boba Buddy','boba tea','Love, Sip, Cry, Hype, Shy, Bye',['boba emotes','bubble tea emote','food emotes'],'Girly'),
('babydragon','Baby Dragon','dragon','Fire, Treasure, Cry, Rage, Love, Nap',['dragon emotes','fantasy emotes','purple dragon'],'Kids'),
('raccoon','Trash Raccoon','raccoon','Gremlin, Snack, Shook, Dead, Chef Kiss, Bonk',['raccoon emotes','meme emotes','funny emotes'],None),
('witchcat','Witch Cat','black cat witch','Spell, Potion, Hiss, Love, Sleepy, Wink',['witch emotes','black cat emote','spooky emotes'],'Girly'),
('bunny','Strawberry Bunny','pink bunny','Hi, Hearts, Cry, Pout, Yay, Carrot',['bunny emotes','pink emotes','pastel emotes'],'Girly'),
('gamerbear','Gamer Bear','bear gamer','GG, Tilted, Pog, Cry, Hype, Gn',['bear emotes','gamer emotes','gg emote'],'Gamer')]
names={p[0]:p[1] for p in P}
B={'Gamer':['gamerskull','gamerbear','animeboy','pixelslime'],'Girly':['magicalgirl','bunny','boba','witchcat'],'Kids':['babyrex','babydragon','pixelslime','ghost']}
L=[]
for i,(k,name,kind,set_,tags,b) in enumerate(P,1):
    t=f'{name} Twitch Emotes, 6 Cute {kind.title()} Emote Pack for Twitch Discord YouTube, {set_.replace(",","")} Emotes'
    if len(t)>140: t=f'{name} Twitch Emotes, 6 {kind.title()} Emote Pack for Twitch Discord YouTube, {set_.replace(",","")}'
    extra=(f"Want more? The {b} Emote Bundle and the 96-emote Mega Bundle are in my shop." if b else "Want more? The 96-emote Mega Bundle is in my shop.")
    L.append(dict(slug=f'E02-L{i:02d}_{k}',src='E02/out',packs=[k],price=5.49,zipbase=f'{k}_emote_pack',title=t,tags=tags+BASE,
      description=desc(f"A {name} emote pack: 6 original {kind} emotes for your Twitch, Discord or YouTube community. Bold outlines and bright colors keep them readable even at the tiny 28px chat size.\n\nEMOTES: {set_}",6,extra),
      cover_title=f'{name} Emotes',cover_sub='6 emotes · '+set_,details=['6 original emotes','Twitch 112 / 56 / 28 px','512px for Discord & stickers','Transparent PNG','Upload guide included']))
BT={'Gamer':('Gamer Emote Bundle','24 Gamer Twitch Emotes Bundle, Skull Bear Anime Boy Pixel Slime Emote Packs for Twitch Discord YouTube, GG Rage Pog Streamer Emotes',['gamer emotes','emote bundle','skull emotes']),
    'Girly':('Girly Kawaii Emote Bundle','24 Kawaii Twitch Emotes Bundle, Magical Girl Bunny Boba Witch Cat Emote Packs for Twitch Discord YouTube, Cute Pink Streamer Emotes',['kawaii emotes','emote bundle','pink emotes']),
    'Kids':('Kid-Friendly Emote Bundle','24 Kid Friendly Twitch Emotes Bundle, Dinosaur Dragon Slime Ghost Emote Packs for Twitch Discord YouTube, Family Streamer Emotes',['kids emotes','emote bundle','dinosaur emotes'])}
for j,(b,ks) in enumerate(B.items(),13):
    nm,t,tg=BT[b]
    L.append(dict(slug=f'E02-L{j:02d}_{b.lower()}_bundle_24',src='E02/out',packs=ks,price=14.99,zipbase=f'{b.lower()}_emote_bundle_24',title=t,tags=tg+BASE,
      description=desc(f"The {nm}: 4 complete emote packs, 24 emotes in one download: "+', '.join(names[k] for k in ks)+".",24,"BEST VALUE: all 4 packs for less than the price of 3. Want everything? The 96-emote Mega Bundle is in my shop."),
      cover_title=nm,cover_sub='24 emotes · 4 packs',details=['24 emotes (4 full packs)','Twitch 112 / 56 / 28 px','512px for Discord & stickers','Transparent PNG','Upload guide included']))
allk=['comfycat','mushfrog','axolotl','shiba']+[p[0] for p in P]
L.append(dict(slug='E02-L16_mega_bundle_96',src='E02/out',packs=allk,price=34.99,zipbase='mega_emote_bundle_96',
  title='96 Twitch Emotes Mega Bundle, 16 Emote Packs, Cute Animal Anime Gamer Kawaii Emotes for Twitch Discord YouTube, Streamer Starter Kit',
  tags=['emote bundle','mega emote pack','96 emotes']+BASE,
  description=desc("The Mega Bundle: ALL 16 of my emote packs, 96 emotes in one purchase. Cute animals, original anime characters, gamer skull and bear, pixel slime, kawaii bunny and boba, spooky ghost and witch cat, baby dragon and dinosaur, and a chaotic trash raccoon. Something for every kind of community.",96,"BEST VALUE: 16 packs for about $2.19 each. Delivered as 2 zip files (Etsy file-size limit)."),
  cover_title='Mega Emote Bundle',cover_sub='96 emotes · 16 packs',details=['96 emotes (16 full packs)','Twitch 112 / 56 / 28 px','512px for Discord & stickers','Transparent PNG','Upload guide included']))
for x in L:
    t=x['title']
    assert len(x['tags'])==13 and all(len(g)<=20 for g in x['tags']) and len(set(x['tags']))==13, x['tags']
    assert len(t)<=140 and sum(t.count(c) for c in '%&:')<=1, (len(t),t)
json.dump({'listings':L},open('spec_e02.json','w'),indent=1); print(len(L),'ok')
for x in L: print(len(x['title']),x['title'])
