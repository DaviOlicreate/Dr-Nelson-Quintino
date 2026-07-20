from PIL import Image

# Open the small logo
img = Image.open('logo-small.png').convert("RGBA")
datas = img.getdata()

newData = []
# The image is probably black and white, or gold and black.
# We want to make the background transparent. 
# Let's inspect the top-left pixel to find the background color.
bg_color = datas[0]

for item in datas:
    # If the pixel is very close to the background color, make it transparent
    # Let's just use luminance to alpha if it's black on white or white on black.
    # Actually, the SVG filter `0.2126 0.7152 0.0722 0 0` takes luminance and puts it in the alpha channel!
    # Let's do exactly what the SVG filter did:
    # R' = 1, G' = 1, B' = 1
    # A' = 0.2126*R + 0.7152*G + 0.0722*B
    
    r, g, b, a = item
    
    # Calculate luminance
    lum = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    
    # The first filter in the SVG was:
    # R=1, G=1, B=1, A=R
    # Wait, the SVG was:
    # a413c61f07: A = 0.2126*R + 0.7152*G + 0.0722*B (luminance to alpha, RGB becomes white)
    # e7336385fb: R=1, G=1, B=1, A=R (takes the R channel and puts it in A)
    # Basically it's creating a mask where bright pixels are opaque and dark pixels are transparent, or vice versa.
    # Let's just make the image white with the luminance as alpha.
    newData.append((255, 255, 255, lum))

img.putdata(newData)
img.save('logo-small-alpha.png', "PNG")
print("Converted to alpha mask!")
