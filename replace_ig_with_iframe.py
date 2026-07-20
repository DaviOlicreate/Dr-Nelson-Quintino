import re

file_path = "index.html"
with open(file_path, "r") as f:
    content = f.read()

# Replace blockquotes with iframes
replacements = {
    r'<blockquote class="instagram-media w-full" data-instgrm-permalink="https://www.instagram.com/reel/DPZraiOkRSN/\?utm_source=ig_embed"[^>]+></blockquote>': 
    '<iframe class="w-full h-[540px] border border-[#333] rounded-md bg-black" src="https://www.instagram.com/p/DPZraiOkRSN/embed" frameborder="0" scrolling="no" allowtransparency="true"></iframe>',

    r'<blockquote class="instagram-media w-full" data-instgrm-permalink="https://www.instagram.com/p/Da23OGMgfPq/\?utm_source=ig_embed"[^>]+></blockquote>':
    '<iframe class="w-full h-[540px] border border-[#333] rounded-md bg-black" src="https://www.instagram.com/p/Da23OGMgfPq/embed" frameborder="0" scrolling="no" allowtransparency="true"></iframe>',

    r'<blockquote class="instagram-media w-full" data-instgrm-permalink="https://www.instagram.com/reel/DZyLQ47scKQ/\?utm_source=ig_embed"[^>]+></blockquote>':
    '<iframe class="w-full h-[540px] border border-[#333] rounded-md bg-black" src="https://www.instagram.com/p/DZyLQ47scKQ/embed" frameborder="0" scrolling="no" allowtransparency="true"></iframe>',

    r'<blockquote class="instagram-media w-full hidden md:block" data-instgrm-permalink="https://www.instagram.com/p/DZazje7AODJ/\?utm_source=ig_embed"[^>]+></blockquote>':
    '<iframe class="w-full h-[540px] border border-[#333] rounded-md bg-black hidden md:block" src="https://www.instagram.com/p/DZazje7AODJ/embed" frameborder="0" scrolling="no" allowtransparency="true"></iframe>',

    r'<blockquote class="instagram-media w-full hidden md:block" data-instgrm-permalink="https://www.instagram.com/p/DY0dgwdxdim/\?utm_source=ig_embed"[^>]+></blockquote>':
    '<iframe class="w-full h-[540px] border border-[#333] rounded-md bg-black hidden md:block" src="https://www.instagram.com/p/DY0dgwdxdim/embed" frameborder="0" scrolling="no" allowtransparency="true"></iframe>',

    r'<blockquote class="instagram-media w-full hidden md:block" data-instgrm-permalink="https://www.instagram.com/reel/DZCkw6hlNhx/\?utm_source=ig_embed"[^>]+></blockquote>':
    '<iframe class="w-full h-[540px] border border-[#333] rounded-md bg-black hidden md:block" src="https://www.instagram.com/p/DZCkw6hlNhx/embed" frameborder="0" scrolling="no" allowtransparency="true"></iframe>'
}

for pattern, replacement in replacements.items():
    content = re.sub(pattern, replacement, content)

with open(file_path, "w") as f:
    f.write(content)

print("Replaced Instagram blockquotes with bulletproof iframes.")
