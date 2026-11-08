"""Rebuild files from @@C<n>@@...@@E@@ chunks in saved tool-result files newer than SINCE.
Payload format: name|base64;name|base64...  Usage: python3 -I reassemble.py OUT_DIR N_CHUNKS SINCE_EPOCH"""
import sys, glob, os, re, json, base64
out, n, since = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
ch = {}
for f in glob.glob('/tmp/claude-tool-results/*/*.txt'):
    if os.path.getmtime(f) < since: continue
    t = open(f).read()
    for m in re.finditer(r'@@C(\d+)@@([A-Za-z0-9+/=|;._\-]*)@@E@@', t): ch[int(m.group(1))] = m.group(2)
miss = [i for i in range(n) if i not in ch]
print('have', len(ch), 'missing', miss)
if not miss:
    os.makedirs(out, exist_ok=True); s = ''.join(ch[i] for i in range(n))
    for item in s.split(';'):
        name, b = item.split('|', 1); p = os.path.join(out, os.path.basename(name)); open(p, 'wb').write(base64.b64decode(b))
    print('wrote', len(s.split(';')), 'files to', out)
