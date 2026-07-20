import os
import shutil
import base64

# Small 1x1 gray pixel PNG
gray_pixel_b64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mMs/wQAAf8A/5D68HMAAAAASUVORK5CYII="

placeholder_path = "placeholder.png"
with open(placeholder_path, "wb") as f:
    f.write(base64.b64decode(gray_pixel_b64))

images_to_replace = [
    'hero-bg.jpg',
    'hero-bg.png',
    'sobre.jpg',
    'collage-1.jpg',
    'collage-2.jpg',
    'drnelson-academic.png',
    'linktree/sobre.jpg',
    'logo-clean.png',
    'logo-gold.png',
    'logo-small.png',
    'flor-de-lis.png'
]

for img in images_to_replace:
    if os.path.exists(img):
        shutil.copy(placeholder_path, img)
        print(f"Replaced {img}")
    elif img == 'drnelson-academic.png' and os.path.exists('drricardo-academic.png'):
        shutil.copy(placeholder_path, 'drricardo-academic.png')
        print("Replaced drricardo-academic.png")
    else:
        print(f"Could not find {img}")

print("Image replacements complete!")
