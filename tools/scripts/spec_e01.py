import json
DISC="\n\n—\nMade by Freemans DocHub with the help of digital/AI art tools; every emote is hand-selected, cut out, cleaned up and sized by me."
def desc(intro, n, extra):
    return (f"{intro}\n\nWHAT'S INCLUDED\n• {n} emotes, transparent PNG\n• Twitch sizes: 112px, 56px, 28px\n• 512px hi-res for Discord emoji/stickers, YouTube, Kick, 7TV and BTTV\n• Quick upload guide\n\n{extra}\n\nINSTANT DIGITAL DOWNLOAD. No physical item will be shipped. Because of the nature of digital files, all sales are final, but message me if anything is wrong with your files and I'll make it right.\n\nLICENSE: For use on your own stream, channel or server. Please do not resell, redistribute or claim as your own."+DISC)
BASE=['twitch emotes','discord emotes','emote pack','cute emotes','streamer emotes','sub emotes','kawaii emotes','chibi emotes','youtube emotes','stream assets']
P={'comfycat':('Comfy Cat','orange cat','Love, LUL, Cry, Rage, Hype, Comfy',['cat emotes','orange cat emote','cozy cat']),
   'mushfrog':('Mushroom Frog','frog','Love, LUL, Sad, Shook, GG, Sleepy',['frog emotes','mushroom frog','cottagecore emote']),
   'axolotl':('Pastel Axolotl','axolotl','Wave, Blush, Pog, Cry, Angry, Cozy',['axolotl emotes','pink emotes','pastel emotes']),
   'shiba':('Shiba Pup','shiba dog','Hi, LUL, Sus, Sad, Hype, Snack',['dog emotes','shiba emotes','puppy emotes'])}
L=[]
for i,(k,(name,animal,set_,extra)) in enumerate(P.items(),1):
    L.append(dict(slug=f'E01-L{i:02d}_{k}',src='E01/out',packs=[k],price=5.49,zipbase=f'{k}_emote_pack',
      title=f'{name} Twitch Emotes, 6 Cute Chibi {animal.title()} Emote Pack for Twitch Discord YouTube, {set_.replace(", "," ")}, Streamer Emotes',
      tags=extra+BASE,
      description=desc(f"A cute {name} emote pack: 6 original chibi {animal} emotes for your Twitch, Discord or YouTube community. Bold outlines and bright colors keep them readable even at the tiny 28px chat size.\n\nEMOTES: {set_}",6,"Want all 24? The 4-pack Critter Bundle (Comfy Cat, Mushroom Frog, Pastel Axolotl, Shiba Pup) is in my shop."),
      cover_title=f'{name} Emotes',cover_sub='6 emotes · '+set_,details=['6 cute chibi emotes','Twitch 112 / 56 / 28 px','512px for Discord & stickers','Transparent PNG','Upload guide included']))
L.append(dict(slug='E01-L05_critter_bundle_24',src='E01/out',packs=list(P),price=14.99,zipbase='critter_emote_bundle_24',
  title='24 Cute Animal Twitch Emotes Bundle, Chibi Cat Frog Axolotl Shiba Emote Pack for Twitch Discord YouTube, Kawaii Streamer Emotes',
  tags=['animal emotes','emote bundle','cat emotes','frog emotes']+BASE[:9],
  description=desc("The Critter Bundle: 4 complete emote packs, 24 cute chibi emotes in one download. Comfy Cat, Mushroom Frog, Pastel Axolotl and Shiba Pup, each with Love/Laugh/Cry/Hype-style reactions your chat will actually use.",24,"BEST VALUE: all 4 packs for less than the price of 3."),
  cover_title='Critter Emote Bundle',cover_sub='24 emotes · 4 packs',details=['24 cute chibi emotes (4 packs)','Twitch 112 / 56 / 28 px','512px for Discord & stickers','Transparent PNG','Upload guide included']))
for x in L:
    t=x['title']
    assert len(x['tags'])==13 and all(len(g)<=20 for g in x['tags']), x['tags']
    assert len(t)<=140 and sum(t.count(c) for c in '%&:')<=1, (len(t),t)
json.dump({'listings':L},open('spec_e01.json','w'),indent=1); print('ok')
