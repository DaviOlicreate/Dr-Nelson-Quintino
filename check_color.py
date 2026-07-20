from PIL import Image
import collections

img = Image.open('logo-clean.png').convert("RGBA")
datas = img.getdata()
colors = collections.Counter()

for item in datas:
    r, g, b, a = item
    if a > 0: # Only count pixels that aren't fully transparent
        colors[(r, g, b)] += 1

print(colors.most_common(5))
