import sys, torch, numpy as np
from PIL import Image
from spandrel import ModelLoader
torch.set_num_threads(2)
m=ModelLoader().load_from_file('/home/claude/models/realesr-general-x4v3.pth').eval()
def up(path,out,tile=256,pad=16):
    im=np.asarray(Image.open(path).convert('RGB')).astype(np.float32)/255
    H,W,_=im.shape; o=np.zeros((H*4,W*4,3),np.float32)
    t=torch.from_numpy(im).permute(2,0,1)[None]
    with torch.no_grad():
        for y in range(0,H,tile):
            for x in range(0,W,tile):
                y0,x0=max(y-pad,0),max(x-pad,0); y1,x1=min(y+tile+pad,H),min(x+tile+pad,W)
                r=m(t[:,:,y0:y1,x0:x1])[0].permute(1,2,0).clamp(0,1).numpy()
                oy,ox=(y-y0)*4,(x-x0)*4; hh=min(tile,H-y)*4; ww=min(tile,W-x)*4
                o[y*4:y*4+hh,x*4:x*4+ww]=r[oy:oy+hh,ox:ox+ww]
    Image.fromarray((o*255+0.5).astype(np.uint8)).save(out)
for a in sys.argv[1:]:
    up(a, a.replace('raw/','up/'))
