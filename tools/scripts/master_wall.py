"""raw/art_NN.png -> master/art_NN.png (4x ESRGAN blended with Lanczos to keep paint texture)"""
import sys, os, numpy as np
from PIL import Image
sys.argv=[sys.argv[0]]+sys.argv[1:]
import importlib.util
spec=importlib.util.spec_from_file_location('up','/home/claude/scripts/upscale_lib.py'); up=importlib.util.module_from_spec(spec); spec.loader.exec_module(up)
for p in sys.argv[1:]:
    n=os.path.basename(p); out=f'/home/claude/W01/master/{n}'
    if os.path.exists(out): continue
    e=up.up_array(p); l=np.asarray(Image.open(p).convert('RGB').resize((e.shape[1],e.shape[0]),Image.LANCZOS)).astype(np.float32)/255
    m=0.65*e+0.35*l
    Image.fromarray((m*255+0.5).clip(0,255).astype(np.uint8)).save(out); print('ok',n,flush=True)
