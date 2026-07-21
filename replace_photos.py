import re

# 1. UPDATE MAIN IMAGES IN INDEX.HTML
file_path = "index.html"
with open(file_path, "r") as f:
    content = f.read()

# Replace Hero Image
# background-image: url('assets/hero-bg.jpg') or something similar
content = re.sub(r"url\(['\"]?assets/hero-bg\.(jpg|png)['\"]?\)", "url('assets/images/drnelson/foto1.jpg')", content)
content = re.sub(r'src=["\']assets/hero-bg\.(jpg|png)["\']', 'src="assets/images/drnelson/foto1.jpg"', content)

# Replace About Image
content = re.sub(r'src=["\']assets/sobre\.(jpg|png)["\']', 'src="assets/images/drnelson/foto2.jpg"', content)

with open(file_path, "w") as f:
    f.write(content)

# 2. UPDATE LINKTREE AVATAR
lt_path = "linktree/index.html"
try:
    with open(lt_path, "r") as f:
        lt_content = f.read()
    
    # The avatar might be logo-gold.png or drricardo-academic.png
    lt_content = re.sub(r'src=["\']\.\./assets/(drricardo-academic|logo-gold)\.(png|jpg)["\']', 'src="../assets/images/drnelson/foto3.jpg"', lt_content)
    
    with open(lt_path, "w") as f:
        f.write(lt_content)
except Exception as e:
    print("Linktree update error:", e)

print("Images replaced.")
