# whiten long straight horizontal/vertical lines near page edges (sheet-crop artifacts)
import sys,glob,os,numpy as np
from PIL import Image
for f in sys.argv[1:]:
    a=np.array(Image.open(f).convert('L')); h,w=a.shape; d=a<128; hit=[]
    for y in list(range(0,int(h*.08)))+list(range(int(h*.92),h)):
        if d[y].mean()>0.7: a[y]=255; hit.append(('r',y))
    for x in list(range(0,int(w*.08)))+list(range(int(w*.92),w)):
        if d[:,x].mean()>0.7: a[:,x]=255; hit.append(('c',x))
    if hit: Image.fromarray(a).save(f); print(os.path.basename(f),len(hit))
