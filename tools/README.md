# Tools for a new chat
Copy into the workspace:
  git clone the repo to /home/claude/etsy-shop, then
  cp -r etsy-shop/tools/scripts etsy-shop/tools/fonts /home/claude/ ; mkdir -p /home/claude/models ; cp etsy-shop/tools/realesr-general-x4v3.pth /home/claude/models/
Install: pip install --break-system-packages spandrel torch pillow numpy cryptography ; apt pngquant if missing.
Key: /home/claude/secrets/aes.key is NOT in the repo. Make a new one:
  python3 -c "import secrets,os;os.makedirs('/home/claude/secrets',exist_ok=True);open('/home/claude/secrets/aes.key','wb').write(secrets.token_bytes(32))"
and set it in the Etsy tab: localStorage.fdh_key = base64 of those 32 bytes (fdh_up imports it with atob). Old rounds will no longer decrypt, which is fine (they're all published).
