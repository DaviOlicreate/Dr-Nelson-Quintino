import os
import shutil
import re

# 1. Move the 4 user files to the proper folder with web-friendly names
moves = {
    "Foto principal.jpeg": "hero_novo.jpg",
    "Foto borrada.jpeg": "filosofia1_novo.jpg",
    "Foto que fica ao lado da borrada.jpeg": "filosofia2_novo.jpg",
    "Foto para produção científica.jpeg": "cientifica_novo.jpg"
}

# The filenames might have different unicode normalization for "ç" and "ã" depending on Mac OS
# So we iterate and match the prefix
for f in os.listdir("."):
    if f.startswith("Foto principal"):
        shutil.move(f, f"assets/images/drnelson/hero_novo.jpg")
    elif f.startswith("Foto borrada"):
        shutil.move(f, f"assets/images/drnelson/filosofia1_novo.jpg")
    elif f.startswith("Foto que fica ao lado"):
        shutil.move(f, f"assets/images/drnelson/filosofia2_novo.jpg")
    elif f.startswith("Foto para"):
        shutil.move(f, f"assets/images/drnelson/cientifica_novo.jpg")

# 2. Update index.html
file_path = "index.html"
with open(file_path, "r") as f:
    content = f.read()

# Replace Hero
content = content.replace('src="assets/images/drnelson/foto1.jpg"', 'src="assets/images/drnelson/hero_novo.jpg"')

# Replace Filosofia 1
content = content.replace('src="assets/images/drnelson/foto7.jpg"', 'src="assets/images/drnelson/filosofia1_novo.jpg"')

# Replace Filosofia 2
content = content.replace('src="assets/images/drnelson/foto8.jpg"', 'src="assets/images/drnelson/filosofia2_novo.jpg"')

# Replace Cientifica
content = content.replace('src="assets/images/drnelson/foto10.jpg" onerror=', 'src="assets/images/drnelson/cientifica_novo.jpg" onerror=')

with open(file_path, "w") as f:
    f.write(content)

print("Moved photos and updated index.html")
