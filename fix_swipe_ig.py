import re

# 1. Update Instagram Links in index.html
file_path = "index.html"
with open(file_path, "r") as f:
    content = f.read()

# Add /?utm_source=ig_embed to all the new links
# The user's links were:
# 1. https://www.instagram.com/p/DPZraiOkRSN/
# 2. https://www.instagram.com/p/Da23OGMgfPq/
# 3. https://www.instagram.com/p/DZyLQ47scKQ/
# 4. https://www.instagram.com/p/DZazje7AODJ/
# 5. https://www.instagram.com/p/DY0dgwdxdim/
# 6. https://www.instagram.com/p/DZCkw6hlNhx/

# Some might actually be reels, let's try replacing /p/ with /reel/ for the bugged ones or just add the embed param.
# I will just add ?utm_source=ig_embed which is the standard fix for Instagram embeds.
def fix_ig_link(match):
    link = match.group(1)
    if "?utm_source=ig_embed" not in link:
        # remove trailing slash if present to avoid //?
        if link.endswith("/"):
            link = link[:-1]
        link = f"{link}/?utm_source=ig_embed"
    return f'data-instgrm-permalink="{link}"'

content = re.sub(r'data-instgrm-permalink="([^"]+)"', fix_ig_link, content)

# 2. Add Touch Events (Swipe to Close) to index.html and linktree/index.html
touch_js = """
        // Swipe to close functionality
        let touchStartY = 0;
        let currentY = 0;
        
        document.addEventListener('DOMContentLoaded', () => {
            const modal = document.getElementById('location-modal');
            const modalBox = document.getElementById('location-modal-content');
            
            if(modal && modalBox) {
                modal.addEventListener('click', function(e) {
                    if (e.target === this) {
                        closeLocationModal();
                    }
                });
                
                modalBox.addEventListener('touchstart', (e) => {
                    touchStartY = e.touches[0].clientY;
                    modalBox.style.transition = 'none';
                }, {passive: true});
                
                modalBox.addEventListener('touchmove', (e) => {
                    currentY = e.touches[0].clientY;
                    let deltaY = currentY - touchStartY;
                    if (deltaY > 0) { // Only drag down
                        modalBox.style.transform = `translateY(${deltaY}px)`;
                    }
                }, {passive: true});
                
                modalBox.addEventListener('touchend', (e) => {
                    modalBox.style.transition = 'transform 0.4s cubic-bezier(0.32, 0.72, 0, 1)';
                    let deltaY = currentY - touchStartY;
                    if (deltaY > 100) {
                        closeLocationModal();
                        setTimeout(() => {
                            modalBox.style.transform = '';
                        }, 400);
                    } else {
                        modalBox.style.transform = 'translateY(0)';
                    }
                });
            }
        });
"""

# Replace the old DOMContentLoaded listener in index.html
old_js = """        document.addEventListener('DOMContentLoaded', () => {
            const modal = document.getElementById('location-modal');
            if(modal) {
                modal.addEventListener('click', function(e) {
                    if (e.target === this) {
                        closeLocationModal();
                    }
                });
            }
        });"""

content = content.replace(old_js, touch_js)

with open(file_path, "w") as f:
    f.write(content)

# Update linktree/index.html
linktree_path = "linktree/index.html"
with open(linktree_path, "r") as f:
    lt_content = f.read()

# Try replacing old_js in linktree
if old_js in lt_content:
    lt_content = lt_content.replace(old_js, touch_js)
else:
    # Look for a different pattern if old_js wasn't exactly that
    # The linktree had:
    lt_old = """        document.getElementById('location-modal').addEventListener('click', function(e) {
            if (e.target === this) {
                closeLocationModal();
            }
        });"""
    if lt_old in lt_content:
         lt_content = lt_content.replace(lt_old, touch_js)

with open(linktree_path, "w") as f:
    f.write(lt_content)

print("Updated Instagram links and added swipe-to-close functionality.")
