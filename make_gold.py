from PIL import Image

# Open the original extracted image
img = Image.open('logo-clean.png').convert("RGBA")

# We want to create a new image that is solid gold, but uses the alpha of the original image.
# Actually, the original image was meant to be used with the SVG filters that turned luminance to alpha.
# SVG Filters: A = 0.2126*R + 0.7152*G + 0.0722*B
# Let's do exactly that to extract the mask, and then color it gold (#bda662 = RGB 189, 166, 98)

datas = img.getdata()
newData = []

for r, g, b, a in datas:
    lum = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # The gold color is R=189, G=166, B=98
    newData.append((189, 166, 98, lum))

img.putdata(newData)

# Now we resize it to 800px width to keep it very sharp on retina displays but small file size
w, h = img.size
ratio = 800.0 / w
new_h = int(h * ratio)
img = img.resize((800, new_h), Image.Resampling.LANCZOS)

# Crop the empty space around it (find bounding box of non-transparent pixels)
bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)

img.save('logo-gold.png', "PNG", optimize=True)
print("Gold logo created successfully!")
