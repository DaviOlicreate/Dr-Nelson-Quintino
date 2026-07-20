import re

file_path = "index.html"
with open(file_path, "r") as f:
    content = f.read()

content = content.replace('src="https://www.instagram.com/p/DPZraiOkRSN/embed"', 'src="https://www.instagram.com/reel/DPZraiOkRSN/embed"')
content = content.replace('src="https://www.instagram.com/p/DZyLQ47scKQ/embed"', 'src="https://www.instagram.com/reel/DZyLQ47scKQ/embed"')
content = content.replace('src="https://www.instagram.com/p/DZCkw6hlNhx/embed"', 'src="https://www.instagram.com/reel/DZCkw6hlNhx/embed"')

with open(file_path, "w") as f:
    f.write(content)

print("Updated 1st, 3rd, and 6th posts to use /reel/ in the embed URL.")
