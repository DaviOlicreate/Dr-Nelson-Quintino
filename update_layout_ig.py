import re

file_path = "index.html"
with open(file_path, "r") as f:
    content = f.read()

# 1. Move #empresas to before the Instagram section
# Extract #empresas block
empresas_match = re.search(r'(<!-- Minhas Empresas -->.*?)(?=<section id="contato")', content, flags=re.DOTALL)
if empresas_match:
    empresas_html = empresas_match.group(1)
    # Remove it from its original place
    content = content.replace(empresas_html, "")
    
    # Insert it before <!-- Sessão 7: Prova Social & Instagram Feed -->
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

# Find all instagram blockquotes and replace their links
import bs4
soup = bs4.BeautifulSoup(content, "html.parser")
blockquotes = soup.find_all("blockquote", class_="instagram-media")

for i, bq in enumerate(blockquotes):
    if i < len(new_links):
        # We need to replace the link in the raw content since BeautifulSoup might mess up formatting
        old_link = bq.get('data-instgrm-permalink')
        if old_link:
            # simple string replace for the link
            content = content.replace(f'data-instgrm-permalink="{old_link}"', f'data-instgrm-permalink="{new_links[i]}"')

with open(file_path, "w") as f:
    f.write(content)

print("Moved #empresas and updated Instagram links.")
