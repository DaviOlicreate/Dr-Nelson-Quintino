import os
import re

file_path = "linktree/index.html"
with open(file_path, "r") as f:
    content = f.read()

# Fix the ID issue in HTML
content = content.replace('id="loc-modal-title-display"', 'id="loc-modal-title"')

# Add back the instagram button in the modal fallback container
old_fallback = """            <div id="loc-modal-fallback" style="display: none; flex-direction: column; gap: 0.75rem;">
                <a id="loc-modal-maps-btn" href="#" target="_blank" style="width: 100%; background-color: #c9a86a; color: #1a1a1a; text-align: center; font-weight: 600; padding: 0.75rem; border-radius: 0.75rem; text-decoration: none; display: block;">
                    Abrir no Google Maps
                </a>
            </div>"""

new_fallback = """            <div id="loc-modal-fallback" style="display: flex; flex-direction: column; gap: 0.75rem; margin-top: 1rem;">
                <a id="loc-modal-maps-btn" href="#" target="_blank" style="width: 100%; background-color: #c9a86a; color: #1a1a1a; text-align: center; font-weight: 600; padding: 0.75rem; border-radius: 0.75rem; text-decoration: none; display: block;">
                    Abrir App do Google Maps
                </a>
                <a id="loc-modal-ig-btn" href="#" target="_blank" style="width: 100%; background-color: transparent; color: #f3f4f6; text-align: center; font-weight: 600; padding: 0.75rem; border-radius: 0.75rem; border: 1px solid rgba(255,255,255,0.1); text-decoration: none; display: flex; align-items: center; justify-content: center; gap: 0.5rem;">
                    <svg class="w-5 h-5" style="width: 1.25rem; height: 1.25rem;" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
                    Acessar Instagram
                </a>
            </div>"""

content = content.replace(old_fallback, new_fallback)

# Now fix the logic in JS
# Since the fallback now has the IG button, we don't want to hide it completely when the iframe shows.
# We just update its visibility or we keep it always visible.

js_old = """            if (data.embed) {
                iframe.src = data.embed;
                iframeContainer.style.display = 'block';
                // Opcional: mudar o texto do botão já que o mapa está visível
                mapsBtn.innerText = "Abrir no app do Google Maps";
            } else {
                iframe.src = '';
                iframeContainer.style.display = 'none';
                mapsBtn.innerText = "Ver Localização no Mapa";
            }"""

js_new = """            if (data.embed) {
                iframe.src = data.embed;
                iframeContainer.style.display = 'block';
                mapsBtn.innerText = "Abrir no app do Google Maps";
            } else {
                iframe.src = '';
                iframeContainer.style.display = 'none';
                mapsBtn.innerText = "Ver Localização no Mapa";
            }"""

content = content.replace(js_old, js_new)

with open(file_path, "w") as f:
    f.write(content)

print("ID and Fallback JS fixed successfully!")
