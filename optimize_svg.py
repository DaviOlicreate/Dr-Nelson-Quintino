import re

# Read the small base64 string
with open('logo-small.b64', 'r') as f:
    small_b64 = f.read().strip()

# Read the huge SVG
with open('logo-transparent.svg', 'r') as f:
    svg_data = f.read()

# Replace the base64 payload
new_svg_data = re.sub(
    r'data:image/png;base64,[^"]+',
    f'data:image/png;base64,{small_b64}',
    svg_data
)

# Also update the width/height of the <image> tag if necessary, but CSS contain should handle it.
# Wait, the original image was width="1857". Let's change the width to 400 (since we resized it).
# But since it's inside a transform="matrix(...)", if we change the <image> width without changing the matrix, it might break.
# Wait, if we keep the SVG exactly the same, but the inner PNG is 400px, we should probably set the <image> width/height to its new dimensions OR scale it so it fills the same space!
# Actually, the SVG has: `<image x="0" y="0" width="1857" xlink:href="data:...`
# If we change the width="1857" to width="400", it will shrink.
# To keep the same size, we should add `preserveAspectRatio="none"` or just not change the width="1857" attribute! 
# If the PNG is 400px but the image tag is width="1857", SVG will stretch the PNG to 1857px. This is exactly what we want!

with open('logo-transparent-optimized.svg', 'w') as f:
    f.write(new_svg_data)
    
print("Optimized SVG created!")
