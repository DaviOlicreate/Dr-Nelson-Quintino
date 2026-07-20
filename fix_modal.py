import os
import re

file_path = "linktree/index.html"
with open(file_path, "r") as f:
    content = f.read()

# First, remove the old injected modal block and script.
# We will match from `<!-- Modal de Localização -->` to `</body>`
pattern = r"<!-- Modal de Localização -->.*?</body>"

# And replace with the properly styled version
robust_modal = """
    <!-- Modal de Localização -->
    <style>
    .custom-loc-overlay {
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        z-index: 9999;
        background-color: rgba(0, 0, 0, 0.9);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        display: none; /* hidden by default */
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    .custom-loc-overlay.show-flex {
        display: flex;
    }
    .custom-loc-overlay.active {
        opacity: 1;
    }
    .custom-loc-box {
        background-color: #111111;
        border: 1px solid rgba(201, 168, 106, 0.3);
        border-radius: 1rem;
        width: 90%;
        max-width: 24rem;
        padding: 1.5rem;
        position: relative;
        transform: scale(0.95);
        transition: transform 0.3s ease;
        box-sizing: border-box;
    }
    .custom-loc-overlay.active .custom-loc-box {
        transform: scale(1);
    }
    </style>

    <div id="location-modal" class="custom-loc-overlay">
        <div class="custom-loc-box" id="location-modal-content">
            <button onclick="closeLocationModal()" class="absolute top-4 right-4 text-gray-400 hover:text-white" style="position: absolute; top: 1rem; right: 1rem; background: none; border: none; cursor: pointer; color: #9ca3af;">
                <svg class="w-6 h-6" style="width: 1.5rem; height: 1.5rem;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
            <div class="text-brand-gold mb-4 flex justify-center" style="display: flex; justify-content: center; margin-bottom: 1rem; color: #c9a86a;">
                <svg class="w-10 h-10" style="width: 2.5rem; height: 2.5rem;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
            </div>
            <h3 id="loc-modal-title" style="font-family: 'Fraunces', serif; text-align: center; color: #f3f4f6; font-size: 1.5rem; line-height: 2rem; margin-bottom: 0.5rem; font-weight: 300;">Clínica</h3>
            <p id="loc-modal-address" style="text-align: center; color: #9ca3af; font-size: 0.875rem; font-weight: 300; margin-bottom: 1.5rem;">Endereço...</p>
            
            <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                <a id="loc-modal-maps-btn" href="#" target="_blank" style="width: 100%; background-color: #c9a86a; color: #1a1a1a; text-align: center; font-weight: 600; padding: 0.75rem; border-radius: 0.75rem; text-decoration: none; display: block;">
                    Abrir no Google Maps
                </a>
                <a id="loc-modal-ig-btn" href="#" target="_blank" style="width: 100%; background-color: transparent; color: #f3f4f6; text-align: center; font-weight: 600; padding: 0.75rem; border-radius: 0.75rem; border: 1px solid rgba(255,255,255,0.1); text-decoration: none; display: flex; align-items: center; justify-content: center; gap: 0.5rem;">
                    <svg class="w-5 h-5" style="width: 1.25rem; height: 1.25rem;" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
                    Acessar Instagram
                </a>
            </div>
        </div>
    </div>

    <script>
        const companiesData = {
            'sos': {
                title: 'SOS Clínica Integrada',
                address: 'Arapiraca - AL',
                maps: 'https://www.google.com/maps/place/SOS+Cl%C3%ADnica+Integrada+Arapiraca+-+AL/@-9.7573837,-36.656806,15z/data=!4m6!3m5!1s0x705d5c443dd9b9b:0xfc88d46705fad62f!8m2!3d-9.7575049!4d-36.656898!16s%2Fg%2F11h18jk4mz?entry=ttu',
                ig: 'https://www.instagram.com/sosclinicaalagoas/'
            },
            'bemestar': {
                title: 'Clínica SOS Bem Estar',
                address: 'Arapiraca - AL',
                maps: 'https://www.google.com/maps/place/SOS+Cl%C3%ADnica+Integrada+Arapiraca+-+AL/@-9.7573837,-36.656806,15z/data=!4m6!3m5!1s0x705d5c443dd9b9b:0xfc88d46705fad62f!8m2!3d-9.7575049!4d-36.656898!16s%2Fg%2F11h18jk4mz?entry=ttu',
                ig: 'https://www.instagram.com/clinica.sosbemestar/'
            },
            'ornare': {
                title: 'Instituto Ornare',
                address: 'Arapiraca - AL',
                maps: 'https://www.google.com/maps/place/SOS+Cl%C3%ADnica+Integrada+Arapiraca+-+AL/@-9.7574996,-36.6594729,17z/data=!3m1!4b1!4m6!3m5!1s0x705d5c443dd9b9b:0xfc88d46705fad62f!8m2!3d-9.7575049!4d-36.656898!16s%2Fg%2F11h18jk4mz?entry=ttu',
                ig: 'https://www.instagram.com/institutoornare.io/'
            },
            'hiperbarica': {
                title: 'Hiperbárica do Agreste',
                address: 'R. Prof. Domingos Correia, 848, Arapiraca - AL',
                maps: 'https://www.google.com/maps/search/?api=1&query=R.+Prof.+Domingos+Correia,+848,+Arapiraca+-+AL',
                ig: 'https://www.instagram.com/hiperbaricadoagreste/'
            }
        };

        function openLocationModal(id) {
            const data = companiesData[id];
            document.getElementById('loc-modal-title').innerText = data.title;
            document.getElementById('loc-modal-address').innerText = data.address;
            document.getElementById('loc-modal-maps-btn').href = data.maps;
            document.getElementById('loc-modal-ig-btn').href = data.ig;
            
            const modal = document.getElementById('location-modal');
            modal.classList.add('show-flex');
            requestAnimationFrame(() => {
                modal.classList.add('active');
            });
        }

        function closeLocationModal() {
            const modal = document.getElementById('location-modal');
            modal.classList.remove('active');
            setTimeout(() => {
                modal.classList.remove('show-flex');
            }, 300);
        }

        document.getElementById('location-modal').addEventListener('click', function(e) {
            if (e.target === this) {
                closeLocationModal();
            }
        });
    </script>
</body>
"""

content = re.sub(pattern, robust_modal, content, flags=re.DOTALL)

with open(file_path, "w") as f:
    f.write(content)

print("Modal fixed with inline CSS!")
