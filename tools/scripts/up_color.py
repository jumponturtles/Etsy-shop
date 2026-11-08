import sys,os,numpy as np
from PIL import Image
sys.path.insert(0,'/home/claude/scripts')
from upscale_lib import up_array
out=sys.argv[1]
for p in sys.argv[2:]:
    o=os.path.join(out,os.path.basename(p))
    if os.path.exists(o): continue
    e=up_array(p); l=np.asarray(Image.open(p).convert('RGB').resize((e.shape[1],e.shape[0]),Image.LANCZOS)).astype(np.float32)/255
    Image.fromarray(((0.7*e+0.3*l)*255+0.5).clip(0,255).astype('uint8')).save(o); print('ok',o,flush=True)
