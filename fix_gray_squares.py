import re

file_path = "index.html"
with open(file_path, "r") as f:
    content = f.read()

# Replace all the broken placeholder paths with actual photos of Dr Nelson
content = content.replace('src="./hero-bg.jpg"', 'src="assets/images/drnelson/foto1.jpg"')
content = content.replace('src="./collage-1.jpg"', 'src="assets/images/drnelson/foto7.jpg"')
content = content.replace('src="./collage-2.jpg"', 'src="assets/images/drnelson/foto8.jpg"')
# Use foto9.jpg for the first sobre.jpg (About section) and foto10.jpg for the second sobre.jpg (Scientific section)
# We can do this with a function or just replace all and then fix
# Let's replace one by one
content = re.sub(r'src="\./sobre\.jpg" alt="Dr\. Nelson Quintino"', 'src="assets/images/drnelson/foto9.jpg" alt="Dr. Nelson Quintino"', content)
content = re.sub(r'src="\./sobre\.jpg" onerror=', 'src="assets/images/drnelson/foto10.jpg" onerror=', content)

with open(file_path, "w") as f:
    f.write(content)

print("Fixed the 5 gray squares with Dr Nelson photos!")
