import re

file_path = "index.html"
with open(file_path, "r") as f:
    content = f.read()

def create_ig_link(post_id, img_file, hidden_class=""):
    return f"""<a href="https://www.instagram.com/p/{post_id}/" target="_blank" rel="noopener noreferrer" class="relative group block w-full h-[540px] rounded-md overflow-hidden bg-black border border-[#333] {hidden_class}">
    <img src="assets/images/instagram/{img_file}" alt="Instagram Post" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105">
    <div class="absolute inset-0 bg-black/40 group-hover:bg-black/10 transition-colors"></div>
    <div class="absolute inset-0 flex items-center justify-center">
        <div class="w-16 h-16 bg-white/20 backdrop-blur-sm rounded-full flex items-center justify-center text-white group-hover:scale-110 group-hover:bg-brand-gold/90 transition-all shadow-xl">
            <svg class="w-8 h-8 ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
        </div>
    </div>
    <div class="absolute bottom-4 left-4 flex items-center gap-2">
        <svg class="w-6 h-6 text-white" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
        <span class="text-white text-sm font-semibold tracking-wide drop-shadow-md">Assistir no Instagram</span>
    </div>
</a>"""

# Replace all iframes
content = re.sub(r'<iframe class="[^"]+" src="https://www.instagram.com/(?:reel|p)/DPZraiOkRSN/embed[^"]*"[^>]+></iframe>', create_ig_link("DPZraiOkRSN", "ig_1.jpg"), content)
content = re.sub(r'<iframe class="[^"]+" src="https://www.instagram.com/(?:reel|p)/Da23OGMgfPq/embed[^"]*"[^>]+></iframe>', create_ig_link("Da23OGMgfPq", "ig_2.jpg"), content)
content = re.sub(r'<iframe class="[^"]+" src="https://www.instagram.com/(?:reel|p)/DZyLQ47scKQ/embed[^"]*"[^>]+></iframe>', create_ig_link("DZyLQ47scKQ", "ig_3.jpg"), content)

content = re.sub(r'<iframe class="[^"]+" src="https://www.instagram.com/(?:reel|p)/DZazje7AODJ/embed[^"]*"[^>]+></iframe>', create_ig_link("DZazje7AODJ", "ig_4.jpg", "hidden md:block"), content)
content = re.sub(r'<iframe class="[^"]+" src="https://www.instagram.com/(?:reel|p)/DY0dgwdxdim/embed[^"]*"[^>]+></iframe>', create_ig_link("DY0dgwdxdim", "ig_5.jpg", "hidden md:block"), content)
content = re.sub(r'<iframe class="[^"]+" src="https://www.instagram.com/(?:reel|p)/DZCkw6hlNhx/embed[^"]*"[^>]+></iframe>', create_ig_link("DZCkw6hlNhx", "ig_6.jpg", "hidden md:block"), content)

with open(file_path, "w") as f:
    f.write(content)

print("Replaced all iframes with image links.")
