import re

file_path = "index.html"
with open(file_path, "r") as f:
    content = f.read()

# Replace /embed" with /embed/captioned" for all 6 iframes
content = content.replace('/embed"', '/embed/captioned"')

with open(file_path, "w") as f:
    f.write(content)

print("Updated all iframe sources to use /embed/captioned.")
