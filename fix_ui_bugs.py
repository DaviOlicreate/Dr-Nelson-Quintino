import os
import re

file_path = "linktree/index.html"
with open(file_path, "r") as f:
    content = f.read()

# 1. Fix the Profile Image
# Old profile image container: 
# <div class="w-28 h-28 rounded-full overflow-hidden border-2 border-brand-gold p-1 mb-4 shadow-[0_0_30px_rgba(189,166,98,0.2)] bg-brand-dark">
#     <img src="profile.jpg" alt="Dr. Nelson Quintino" class="w-full h-full object-cover rounded-full object-top">
# </div>

new_profile_img = """<div style="width: 8rem; height: auto; margin-bottom: 1rem; display: flex; justify-content: center; align-items: center;">
                <img src="profile.jpg" alt="Dr. Nelson Quintino" style="width: 100%; height: auto; object-fit: contain;">
            </div>"""

content = re.sub(
    r'<div class="w-28 h-28 rounded-full overflow-hidden border-2 border-brand-gold p-1 mb-4 shadow-\[0_0_30px_rgba\(189,166,98,0\.2\)\] bg-brand-dark">\s*<img src="profile\.jpg"[^>]*>\s*</div>',
    new_profile_img,
    content
)

# 2. Fix the Huge SVG Pin in the Modal
# Old SVG: <svg class="w-4 h-4 text-gray-400 mt-1 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
new_svg = '<svg style="width: 1.25rem; height: 1.25rem; color: #9CA3AF; margin-top: 0.125rem; flex-shrink: 0;" fill="currentColor" viewBox="0 0 20 20">'
content = content.replace('<svg class="w-4 h-4 text-gray-400 mt-1 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">', new_svg)

with open(file_path, "w") as f:
    f.write(content)

print("Profile image and SVG Pin inline CSS fixed successfully!")
