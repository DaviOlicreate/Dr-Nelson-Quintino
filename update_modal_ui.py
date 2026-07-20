import os
import re

file_path = "linktree/index.html"
with open(file_path, "r") as f:
    content = f.read()

# Update the profile picture
content = re.sub(r'src="[^"]*sobre\.jpg[^"]*"', 'src="profile.jpg"', content)

# New Modal CSS & HTML
pattern = r"<!-- Modal de Localização -->.*?</div>\s*</div>\s*</div>"
new_modal = """    <!-- Modal de Localização -->
    <style>
    .custom-loc-overlay {
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        z-index: 9999;
        background-color: rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        display: none;
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    .custom-loc-overlay.show-flex {
        display: block;
    }
    .custom-loc-overlay.active {
        opacity: 1;
    }
    .custom-loc-box {
        background-color: #1F2937; /* Dark slate matching the example */
        border-radius: 1.5rem 1.5rem 0 0;
        width: 100%;
        max-width: 36rem;
        margin: 0 auto;
        padding: 1.5rem;
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        transform: translateY(100%);
        transition: transform 0.4s cubic-bezier(0.32, 0.72, 0, 1);
        box-sizing: border-box;
        box-shadow: 0 -10px 40px rgba(0,0,0,0.5);
    }
    .custom-loc-overlay.active .custom-loc-box {
        transform: translateY(0);
    }
    .drag-handle {
        width: 3rem;
        height: 0.25rem;
        background-color: #4B5563;
        border-radius: 9999px;
        margin: 0 auto 1.5rem auto;
    }
    .loc-title {
        font-family: 'Inter', sans-serif;
        text-align: center;
        color: #FFFFFF;
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .loc-desc-container {
        display: flex;
        align-items: flex-start;
        justify-content: center;
        gap: 0.5rem;
        margin-bottom: 1.5rem;
        padding: 0 1rem;
    }
    .loc-desc {
        text-align: center;
        color: #9CA3AF;
        font-size: 0.875rem;
        font-weight: 400;
        line-height: 1.4;
    }
    .close-btn {
        width: 100%;
        background-color: #0F172A; /* Darker blue/slate */
        color: #FFFFFF;
        text-align: center;
        font-weight: 700;
        font-size: 1rem;
        padding: 1rem;
        border-radius: 1rem;
        border: none;
        cursor: pointer;
        margin-top: 1.5rem;
        transition: background-color 0.2s;
    }
    .close-btn:hover {
        background-color: #1E293B;
    }
    </style>

    <div id="location-modal" class="custom-loc-overlay">
        <div class="custom-loc-box" id="location-modal-content">
            <div class="drag-handle"></div>
            
            <h3 id="loc-modal-title-display" class="loc-title">Localização</h3>
            
            <div class="loc-desc-container">
                <svg class="w-4 h-4 text-gray-400 mt-1 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"></path></svg>
                <p id="loc-modal-address" class="loc-desc">Endereço...</p>
            </div>
            
            <div id="loc-modal-iframe-container" style="display: none; width: 100%; border-radius: 0.75rem; overflow: hidden; background-color: #E5E7EB;">
                <iframe id="loc-modal-iframe" width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
            
            <div id="loc-modal-fallback" style="display: none; flex-direction: column; gap: 0.75rem;">
                <a id="loc-modal-maps-btn" href="#" target="_blank" style="width: 100%; background-color: #c9a86a; color: #1a1a1a; text-align: center; font-weight: 600; padding: 0.75rem; border-radius: 0.75rem; text-decoration: none; display: block;">
                    Abrir no Google Maps
                </a>
            </div>

            <button onclick="closeLocationModal()" class="close-btn">Fechar</button>
        </div>
    </div>"""

# Replace the HTML block
content = re.sub(pattern, new_modal, content, flags=re.DOTALL)

with open(file_path, "w") as f:
    f.write(content)

print("Modal UI updated successfully!")
