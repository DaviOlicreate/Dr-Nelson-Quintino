import re

file_path = "index.html"
with open(file_path, "r") as f:
    content = f.read()

# 1. Move #empresas to before the Instagram section
empresas_match = re.search(r'(<!-- Minhas Empresas -->.*?)(?=<section id="contato")', content, flags=re.DOTALL)
if empresas_match:
    empresas_html = empresas_match.group(1)
    content = content.replace(empresas_html, "")
    target = "<!-- Sessão 7: Prova Social & Instagram Feed -->"
    content = content.replace(target, empresas_html + "\n    " + target)

# 2. Update Instagram links
new_links = [
    "https://www.instagram.com/p/DPZraiOkRSN/",
    "https://www.instagram.com/p/Da23OGMgfPq/",
    "https://www.instagram.com/p/DZyLQ47scKQ/",
    "https://www.instagram.com/p/DZazje7AODJ/",
    "https://www.instagram.com/p/DY0dgwdxdim/",
    "https://www.instagram.com/p/DZCkw6hlNhx/"
]

# Find all instagram blockquotes using regex
blockquote_pattern = re.compile(r'data-instgrm-permalink="([^"]+)"')
matches = blockquote_pattern.findall(content)

for i, old_link in enumerate(matches):
    if i < len(new_links):
        content = content.replace(f'data-instgrm-permalink="{old_link}"', f'data-instgrm-permalink="{new_links[i]}"', 1)

with open(file_path, "w") as f:
    f.write(content)

print("Moved #empresas and updated Instagram links using pure Python regex.")
