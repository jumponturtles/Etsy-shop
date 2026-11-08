import json
DISC="\n\n—\nMade by Freemans DocHub with the help of digital/AI art tools; every emote is hand-selected, cut out, cleaned up and sized by me."
def desc(intro, n, extra):
    return (f"{intro}\n\nWHAT'S INCLUDED\n• {n} emotes, transparent PNG\n• Twitch sizes: 112px, 56px, 28px\n• 512px hi-res for Discord emoji/stickers, YouTube, Kick, 7TV and BTTV\n• Quick upload guide\n\n{extra}\n\nINSTANT DIGITAL DOWNLOAD. No physical item will be shipped. Because of the nature of digital files, all sales are final, but message me if anything is wrong with your files and I'll make it right.\n\nLICENSE: For use on your own stream, channel or server. Please do not resell, redistribute or claim as your own."+DISC)
BASE=['twitch emotes','discord emotes','emote pack','streamer emotes','sub emotes','youtube emotes','stream assets','chibi emotes','cute emotes','kick emotes']
P=[('skater','Skater Boy','skater boy','Hi, Kickflip, Rage, Cry, Hype, Chill',['skater emotes','boy streamer emote','anime emotes']),
('mermaid','Mermaid Girl','mermaid','Hi, Splash, Love, Cry, Shook, Sleepy',['mermaid emotes','ocean emotes','girly emotes']),
('astronaut','Astronaut Kid','astronaut','Hi, Float, Rocket, Love, Cry, Wow',['space emotes','astronaut emote','kids emotes']),
('chefbear','Chef Bear','chef bear','Hi, Yum, Chef Kiss, Rage, Cry, Love',['chef emotes','bear emotes','food emotes']),
('yeti','Baby Yeti','yeti','Hi, Snowball, Cozy, Rage, Cry, Love',['yeti emotes','winter emotes','christmas emotes']),
('sloth','Lazy Sloth','sloth','Hi, Hang, Sleepy, Love, Cry, Chill',['sloth emotes','chill emotes','animal emotes']),
('koala','Baby Koala','koala','Hi, Hug, Sleepy, Love, Cry, Munch',['koala emotes','animal emotes','kawaii emotes']),
('lioncub','Lion Cub','lion cub','Hi, Roar, King, Cry, Love, Nap',['lion emotes','animal emotes','king emote']),
('wolfpup','Wolf Pup','wolf','Hi, Howl, Rage, Cry, Love, Sleepy',['wolf emotes','animal emotes','howl emote']),
('gothgirl','Goth Girl','goth girl','Hi, Smirk, Love, Cry, Rage, Bored',['goth emotes','girly emotes','anime emotes']),
('lumberjack','Lumberjack','bearded guy','Hi, Flex, Coffee, Rage, Cry, Thumbs Up',['beard emotes','guy emotes','flannel emote'])]
names={p[0]:p[1] for p in P}; names.update({'coffee':'Coffee Cup','penguin':'Baby Penguin','snowman':'Snowman','reindeer':'Christmas Reindeer'})
B=[('charactersquad','Character Squad Emote Bundle',['skater','gothgirl','mermaid','astronaut'],'24 Chibi Character Twitch Emotes Bundle, Skater Boy Goth Girl Mermaid Astronaut Emote Packs for Twitch Discord YouTube',['anime emotes','emote bundle','chibi characters']),
('wildcubs','Wild Cubs Emote Bundle',['lioncub','wolfpup','koala','sloth'],'24 Cute Animal Twitch Emotes Bundle, Lion Cub Wolf Pup Koala Sloth Emote Packs for Twitch Discord YouTube, Kawaii Animal Emotes',['animal emotes','emote bundle','kawaii emotes']),
('cozycrew','Cozy Crew Emote Bundle',['chefbear','yeti','lumberjack','coffee'],'24 Cozy Twitch Emotes Bundle, Chef Bear Baby Yeti Lumberjack Coffee Emote Packs for Twitch Discord YouTube, Chill Streamer Emotes',['cozy emotes','emote bundle','chill emotes']),
('winter','Winter Wonderland Emote Bundle',['yeti','penguin','snowman','reindeer'],'24 Winter Twitch Emotes Bundle, Yeti Penguin Snowman Reindeer Emote Packs for Twitch Discord YouTube, Christmas Holiday Emotes',['winter emotes','emote bundle','christmas emotes'])]
inb={k:nm for _,nm,ks,_,_ in B for k in ks}
L=[]
for i,(k,name,kind,set_,tags) in enumerate(P,1):
    t=f'{name} Twitch Emotes, 6 Cute {kind.title()} Emote Pack for Twitch Discord YouTube, {set_.replace(",","")} Emotes'
    if len(t)>140: t=f'{name} Twitch Emotes, 6 {kind.title()} Emote Pack for Twitch Discord YouTube, {set_.replace(",","")}'
    extra=(f"Want more? The {inb[k]} is in my shop." if k in inb else "Want more? Check my shop for themed emote bundles.")
    L.append(dict(slug=f'E04-L{i:02d}_{k}',src='E04/out',packs=[k],price=5.49,zipbase=f'{k}_emote_pack',title=t,tags=tags+BASE,
      description=desc(f"A {name} emote pack: 6 original {kind} emotes for your Twitch, Discord or YouTube community. Bold outlines and bright colors keep them readable even at the tiny 28px chat size.\n\nEMOTES: {set_}",6,extra),
      cover_title=f'{name} Emotes',cover_sub='6 emotes · '+set_,details=['6 original emotes','Twitch 112 / 56 / 28 px','512px for Discord & stickers','Transparent PNG','Upload guide included']))
for j,(slug,nm,ks,t,tg) in enumerate(B,12):
    L.append(dict(slug=f'E04-L{j:02d}_{slug}_bundle_24',src='E04/out',packs=ks,price=14.99,zipbase=f'{slug}_emote_bundle_24',title=t,tags=tg+BASE,
      description=desc(f"The {nm}: 4 complete emote packs, 24 emotes in one download: "+', '.join(names[k] for k in ks)+".",24,"BEST VALUE: all 4 packs for less than the price of 3."),
      cover_title=nm,cover_sub='24 emotes · 4 packs',details=['24 emotes (4 full packs)','Twitch 112 / 56 / 28 px','512px for Discord & stickers','Transparent PNG','Upload guide included']))
allk=[p[0] for p in P]
L.append(dict(slug='E04-L16_mega_bundle_66',src='E04/out',packs=allk,price=27.99,zipbase='mega_emote_bundle_66',
  title='66 Twitch Emotes Mega Bundle, 11 Emote Packs, Cute Animal Chibi Character Emotes for Twitch Discord YouTube, Streamer Starter Kit',
  tags=['emote bundle','mega emote pack','66 emotes']+BASE,
  description=desc("The Mega Bundle: 11 emote packs, 66 emotes in one purchase. Skater boy, goth girl, mermaid, astronaut kid, chef bear, baby yeti, lumberjack, lion cub, wolf pup, koala and sloth. Something for every kind of community.",66,"BEST VALUE: 11 packs for about $2.54 each. May arrive as more than one zip file (Etsy file-size limit)."),
  cover_title='Mega Emote Bundle',cover_sub='66 emotes · 11 packs',details=['66 emotes (11 full packs)','Twitch 112 / 56 / 28 px','512px for Discord & stickers','Transparent PNG','Upload guide included']))
for x in L:
    t=x['title']; x['tags']=list(dict.fromkeys(x['tags']))
    while len(x['tags'])<13: x['tags'].append(['emote set','twitch sub badge','discord stickers','vtuber emotes'][len(x['tags'])-10])
    x['tags']=x['tags'][:13]
    assert len(x['tags'])==13 and all(len(g)<=20 for g in x['tags']), x['tags']
    assert len(t)<=140 and sum(t.count(c) for c in '%&:')<=1, (len(t),t)
json.dump({'listings':L},open('spec_e04.json','w'),indent=1); print(len(L),'ok')
