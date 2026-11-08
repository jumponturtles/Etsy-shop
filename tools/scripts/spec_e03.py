import json
DISC="\n\n—\nMade by Freemans DocHub with the help of digital/AI art tools; every emote is hand-selected, cut out, cleaned up and sized by me."
def desc(intro, n, extra):
    return (f"{intro}\n\nWHAT'S INCLUDED\n• {n} emotes, transparent PNG\n• Twitch sizes: 112px, 56px, 28px\n• 512px hi-res for Discord emoji/stickers, YouTube, Kick, 7TV and BTTV\n• Quick upload guide\n\n{extra}\n\nINSTANT DIGITAL DOWNLOAD. No physical item will be shipped. Because of the nature of digital files, all sales are final, but message me if anything is wrong with your files and I'll make it right.\n\nLICENSE: For use on your own stream, channel or server. Please do not resell, redistribute or claim as your own."+DISC)
BASE=['twitch emotes','discord emotes','emote pack','streamer emotes','sub emotes','youtube emotes','stream assets','chibi emotes','cute emotes','kick emotes']
P=[('reindeer','Christmas Reindeer','reindeer','Jolly, Gift, Cocoa, Cry, Hype, Sleepy',['christmas emotes','reindeer emote','holiday emotes']),
('gingerbread','Gingerbread','gingerbread','Wave, Bite, Love, Rage, LUL, Dance',['christmas emotes','gingerbread emote','holiday emotes']),
('panda','Bamboo Panda','panda','Hi, Bamboo, Cry, Shook, Love, Lazy',['panda emotes','bear emotes','animal emotes']),
('corgi','Corgi Pup','corgi','Zoom, Treat, Cry, Blep, Love, Sleep',['corgi emotes','dog emotes','puppy emotes']),
('penguin','Baby Penguin','penguin','Wave, Slide, Cold, Love, Rage, Fish',['penguin emotes','winter emotes','animal emotes']),
('fox','Autumn Fox','fox','Hi, Smug, Cry, Love, Hype, Sleepy',['fox emotes','autumn emotes','animal emotes']),
('capybara','Chill Capybara','capybara','Chill, Bath, Vibe, Shook, Love, Nap',['capybara emotes','meme emotes','chill emotes']),
('robot','Retro Robot','robot','Beep, Error, Love, Rage, Cry, Low Battery',['robot emotes','retro emotes','gamer emotes']),
('bulldog','Bulldog Mascot','bulldog','Flex, Win, Rage, Cry, Hype, Ref',['sports emotes','bulldog emotes','mascot emotes']),
('sushi','Sushi Buddy','sushi','Hi, Yum, Cry, Spicy, Love, Nap',['sushi emotes','food emotes','kawaii emotes']),
('gamergirl','Gamer Girl','anime gamer girl','GG, Rage, Pog, Cry, Love, Snack',['anime emotes','gamer girl emote','girl gamer emotes']),
('alien','Little Alien','alien','Greet, Abduct, Shook, Love, LUL, Sus',['alien emotes','ufo emotes','sus emote']),
('santacat','Santa Cat','christmas cat','Jolly, Gift, Cookie, Cry, Grinch, Sleepy',['christmas emotes','cat emotes','santa emotes']),
('snowman','Snowman','snowman','Wave, Melt, Love, Cold, LUL, Snowball',['christmas emotes','snowman emote','winter emotes']),
('heartie','Valentine Heart','heart','Love, Hug, Blush, Broken, Kiss, Shy',['valentine emotes','heart emotes','love emotes']),
('avocado','Avocado','avocado','Hi, Toast, Cry, Love, Shook, Flex',['avocado emotes','food emotes','kawaii emotes']),
('octopus','Purple Octopus','octopus','Wave, Ink, Love, Cry, Hype, Sleepy',['octopus emotes','ocean emotes','kawaii emotes']),
('unicorn','Rainbow Unicorn','unicorn','Magic, Love, Cry, Sass, Yay, Sleep',['unicorn emotes','rainbow emotes','pastel emotes']),
('knight','Little Knight','knight','Salute, Victory, Block, Rage, Cry, Rest',['knight emotes','fantasy emotes','rpg emotes']),
('ninjacat','Ninja Cat','ninja cat','Sneak, Throw, Smoke, Rage, LUL, Bow',['ninja emotes','cat emotes','black cat emote']),
('parrot','Pirate Parrot','parrot','Ahoy, Treasure, Squawk, Cry, Sus, Map',['pirate emotes','parrot emotes','bird emotes']),
('cowboydog','Cowboy Dog','cowboy dog','Howdy, Yeehaw, Rage, Cry, Love, Nap',['cowboy emotes','western emotes','dog emotes']),
('bee','Bumblebee','bee','Hi, Honey, Love, Cry, Buzz, Sleepy',['bee emotes','bug emotes','kawaii emotes']),
('mushroom','Little Mushroom','mushroom','Hi, Love, Cry, Shook, Dance, Cozy',['mushroom emotes','cottagecore emote','kawaii emotes']),
('coffee','Coffee Cup','coffee','Morning, Sip, Hype, Cry, Love, Empty',['coffee emotes','food emotes','cozy emotes']),
('hamster','Hamster','hamster','Hi, Snack, Wheel, Cry, Love, Sleep',['hamster emotes','animal emotes','kawaii emotes']),
('cybercat','Cyberpunk Cat','cyberpunk cat','Cool, Hack, Rage, GG, Glitch, Chill',['cyberpunk emotes','neon emotes','gamer emotes']),
('vampbat','Vampire Bat','vampire bat','Bleh, Love, Hang, Cry, Rage, Sleepy',['bat emotes','spooky emotes','halloween emote']),
('cloud','Weather Cloud','cloud','Sunny, Rain, Storm, Love, Rainbow, Sleepy',['cloud emotes','weather emotes','kawaii emotes']),
('pizza','Pizza Slice','pizza','Hi, Yum, Cry, Love, Hype, Sus',['pizza emotes','food emotes','funny emotes'])]
names={p[0]:p[1] for p in P}; names.update({'ghost':'Spooky Ghost','witchcat':'Witch Cat','babydragon':'Baby Dragon'})
B=[('christmas','Christmas Emote Bundle',['reindeer','gingerbread','santacat','snowman'],'24 Christmas Twitch Emotes Bundle, Reindeer Gingerbread Santa Cat Snowman Emote Packs for Twitch Discord YouTube, Holiday Emotes',['christmas emotes','emote bundle','holiday emotes']),
('foodie','Foodie Emote Bundle',['sushi','avocado','coffee','pizza'],'24 Food Twitch Emotes Bundle, Sushi Avocado Coffee Pizza Kawaii Emote Packs for Twitch Discord YouTube, Cute Foodie Streamer Emotes',['food emotes','emote bundle','kawaii emotes']),
('cozycritters','Cozy Critters Emote Bundle',['panda','corgi','fox','hamster'],'24 Cute Animal Twitch Emotes Bundle, Panda Corgi Fox Hamster Emote Packs for Twitch Discord YouTube, Cozy Streamer Emotes',['animal emotes','emote bundle','cozy emotes']),
('gamersquad','Gamer Squad Emote Bundle',['gamergirl','cybercat','robot','bulldog'],'24 Gamer Twitch Emotes Bundle, Anime Gamer Girl Cyberpunk Cat Robot Bulldog Emote Packs for Twitch Discord YouTube, GG Pog Emotes',['gamer emotes','emote bundle','anime emotes']),
('fantasy','Fantasy Emote Bundle',['unicorn','knight','babydragon','octopus'],'24 Fantasy Twitch Emotes Bundle, Unicorn Knight Dragon Octopus Emote Packs for Twitch Discord YouTube, RPG Streamer Emotes',['fantasy emotes','emote bundle','rpg emotes']),
('spooky','Spooky Emote Bundle',['vampbat','ghost','witchcat','alien'],'24 Spooky Twitch Emotes Bundle, Vampire Bat Ghost Witch Cat Alien Emote Packs for Twitch Discord YouTube, Cute Halloween Emotes',['spooky emotes','emote bundle','halloween emote'])]
inb={k:nm for _,nm,ks,_,_ in B for k in ks}
L=[]
for i,(k,name,kind,set_,tags) in enumerate(P,1):
    t=f'{name} Twitch Emotes, 6 Cute {kind.title()} Emote Pack for Twitch Discord YouTube, {set_.replace(",","")} Emotes'
    if len(t)>140: t=f'{name} Twitch Emotes, 6 {kind.title()} Emote Pack for Twitch Discord YouTube, {set_.replace(",","")}'
    extra=(f"Want more? The {inb[k]} is in my shop." if k in inb else "Want more? Check my shop for themed emote bundles.")
    L.append(dict(slug=f'E03-L{i:02d}_{k}',src='E03/out',packs=[k],price=5.49,zipbase=f'{k}_emote_pack',title=t,tags=tags+BASE,
      description=desc(f"A {name} emote pack: 6 original {kind} emotes for your Twitch, Discord or YouTube community. Bold outlines and bright colors keep them readable even at the tiny 28px chat size.\n\nEMOTES: {set_}",6,extra),
      cover_title=f'{name} Emotes',cover_sub='6 emotes · '+set_,details=['6 original emotes','Twitch 112 / 56 / 28 px','512px for Discord & stickers','Transparent PNG','Upload guide included']))
for j,(slug,nm,ks,t,tg) in enumerate(B,31):
    L.append(dict(slug=f'E03-L{j:02d}_{slug}_bundle_24',src='E03/out',packs=ks,price=14.99,zipbase=f'{slug}_emote_bundle_24',title=t,tags=tg+BASE,
      description=desc(f"The {nm}: 4 complete emote packs, 24 emotes in one download: "+', '.join(names[k] for k in ks)+".",24,"BEST VALUE: all 4 packs for less than the price of 3."),
      cover_title=nm,cover_sub='24 emotes · 4 packs',details=['24 emotes (4 full packs)','Twitch 112 / 56 / 28 px','512px for Discord & stickers','Transparent PNG','Upload guide included']))
for x in L:
    t=x['title']; x['tags']=list(dict.fromkeys(x['tags']))
    while len(x['tags'])<13: x['tags'].append(['emote set','twitch sub badge','discord stickers','vtuber emotes'][len(x['tags'])-10])
    x['tags']=x['tags'][:13]
    assert len(x['tags'])==13 and all(len(g)<=20 for g in x['tags']), x['tags']
    assert len(t)<=140 and sum(t.count(c) for c in '%&:')<=1, (len(t),t)
json.dump({'listings':L},open('spec_e03.json','w'),indent=1); print(len(L),'ok')
