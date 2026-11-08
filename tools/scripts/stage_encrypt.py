"""Encrypt listing files for the staging repo.
Each file -> <repo>/<round>/<slug>/<name>.enc  = 12-byte IV + AES-256-GCM(ciphertext+tag)
Writes manifest.json (slug -> list of [encpath, original name, mime]) next to them.
Usage: python3 -I stage_encrypt.py SRC_ROUND_DIR REPO_DIR ROUND KEYFILE
"""
import sys, os, json, glob, secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

src, repo, rnd, keyfile = sys.argv[1:5]
if not os.path.exists(keyfile):
    open(keyfile, 'wb').write(secrets.token_bytes(32))
key = open(keyfile, 'rb').read()
aes = AESGCM(key)
man = {}
for folder in sorted(glob.glob(os.path.join(src, '[A-Z][0-9]*'))):
    slug = os.path.basename(folder)
    files = sorted(glob.glob(os.path.join(folder, '0*.jpg'))) + sorted(glob.glob(os.path.join(folder, '*.zip')))
    out = os.path.join(repo, rnd, slug); os.makedirs(out, exist_ok=True)
    man[slug] = []
    for f in files:
        name = os.path.basename(f)
        iv = secrets.token_bytes(12)
        ct = aes.encrypt(iv, open(f, 'rb').read(), None)
        enc = os.path.join(out, name + '.enc')
        open(enc, 'wb').write(iv + ct)
        mime = 'image/jpeg' if name.endswith('.jpg') else 'application/zip'
        man[slug].append([f'{rnd}/{slug}/{name}.enc', name, mime])
json.dump(man, open(os.path.join(repo, rnd, 'manifest.json'), 'w'), indent=1)
print(json.dumps({k: len(v) for k, v in man.items()}))
