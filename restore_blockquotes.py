import re

file_path = "index.html"
with open(file_path, "r") as f:
    content = f.read()

# Post 2
content = re.sub(
    r'<a href="https://www.instagram.com/p/Da23OGMgfPq/".*?</a>',
    r'<blockquote class="instagram-media w-full" data-instgrm-permalink="https://www.instagram.com/p/Da23OGMgfPq/?utm_source=ig_embed" data-instgrm-version="14" style="background:#000; border:1px solid #333; border-radius:3px; margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"></blockquote>',
    content,
    flags=re.DOTALL
)

# Post 4
content = re.sub(
    r'<a href="https://www.instagram.com/p/DZazje7AODJ/".*?</a>',
    r'<blockquote class="instagram-media w-full hidden md:block" data-instgrm-permalink="https://www.instagram.com/p/DZazje7AODJ/?utm_source=ig_embed" data-instgrm-version="14" style="background:#000; border:1px solid #333; border-radius:3px; margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"></blockquote>',
    content,
    flags=re.DOTALL
)

# Post 5
content = re.sub(
    r'<a href="https://www.instagram.com/p/DY0dgwdxdim/".*?</a>',
    r'<blockquote class="instagram-media w-full hidden md:block" data-instgrm-permalink="https://www.instagram.com/p/DY0dgwdxdim/?utm_source=ig_embed" data-instgrm-version="14" style="background:#000; border:1px solid #333; border-radius:3px; margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"></blockquote>',
    content,
    flags=re.DOTALL
)

with open(file_path, "w") as f:
    f.write(content)

print("Restored blockquotes for posts 2, 4, 5.")
