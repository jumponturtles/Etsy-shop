import sys,os,numpy as np
from PIL import Image
sys.path.insert(0,'/home/claude/scripts')
from upscale_lib import up_array
for p in sys.argv[1:]:
    o=up_array(p); im=Image.fromarray((o*255+0.5).clip(0,255).astype('uint8')).resize((1024,1536),Image.LANCZOS)
    im.save('/home/claude/W01/raw_up/'+os.path.basename(p)); print('pre',p,flush=True)
