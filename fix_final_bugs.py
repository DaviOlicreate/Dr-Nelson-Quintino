import re

# 1. Update index.html
file_path = "index.html"
with open(file_path, "r") as f:
    content = f.read()

# Fix Instagram Reels URLs
content = content.replace("instagram.com/p/DPZraiOkRSN", "instagram.com/reel/DPZraiOkRSN")
content = content.replace("instagram.com/p/DZyLQ47scKQ", "instagram.com/reel/DZyLQ47scKQ")
content = content.replace("instagram.com/p/DZCkw6hlNhx", "instagram.com/reel/DZCkw6hlNhx")

# Fix touchmove
old_touchmove = """                modalBox.addEventListener('touchmove', (e) => {
                    currentY = e.touches[0].clientY;
                    let deltaY = currentY - touchStartY;
                    if (deltaY > 0) { // Only drag down
                        modalBox.style.transform = `translateY(${deltaY}px)`;
                    }
                }, {passive: true});"""

new_touchmove = """                modalBox.addEventListener('touchmove', (e) => {
                    currentY = e.touches[0].clientY;
                    let deltaY = currentY - touchStartY;
                    if (deltaY > 0) { // Only drag down
                        modalBox.style.transform = `translateY(${deltaY}px)`;
                        if (e.cancelable) e.preventDefault(); // Stop page from scrolling
                    }
                }, {passive: false});"""

content = content.replace(old_touchmove, new_touchmove)

with open(file_path, "w") as f:
    f.write(content)

# 2. Update linktree/index.html
linktree_path = "linktree/index.html"
with open(linktree_path, "r") as f:
    lt_content = f.read()

if old_touchmove in lt_content:
    lt_content = lt_content.replace(old_touchmove, new_touchmove)
    with open(linktree_path, "w") as f:
        f.write(lt_content)

print("Bugfixes applied successfully.")
