import re

file_path = "index.html"
with open(file_path, "r") as f:
    content = f.read()

# Remove 'hidden md:block' from the instagram posts links
content = content.replace("hidden md:block", "")

with open(file_path, "w") as f:
    f.write(content)

print("Removed 'hidden md:block' to show all 6 posts on mobile.")
