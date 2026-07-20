import os
import re

file_path = "linktree/index.html"
with open(file_path, "r") as f:
    content = f.read()

# 1. Fix Image path (Vercel trailing slash issue)
content = content.replace('src="./profile.jpg"', 'src="/linktree/profile.jpg"')

# 2. Fix Modal Colors
# The modal background is .custom-loc-box with background-color: #1F2937;
content = content.replace('background-color: #1F2937;', 'background-color: #0B1120; border-top: 1px solid rgba(201, 168, 106, 0.2);')

# The close button is .close-btn with background-color: #0F172A; and hover: #1E293B;
content = content.replace('background-color: #0F172A;', 'background-color: #1A1A1A; border: 1px solid rgba(201, 168, 106, 0.3);')
content = content.replace('background-color: #1E293B;', 'background-color: #262626; border: 1px solid rgba(201, 168, 106, 0.5);')

# Optional: Make the drag handle a bit more subtle gold or gray
content = content.replace('background-color: #4B5563;', 'background-color: rgba(201, 168, 106, 0.3);')

with open(file_path, "w") as f:
    f.write(content)

print("Image path and modal colors fixed successfully!")
