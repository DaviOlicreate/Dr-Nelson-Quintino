import os

file_path = "linktree/index.html"
with open(file_path, "r") as f:
    content = f.read()

# The JS script and Modal to inject before </body>
injection_js_modal = """
    <!-- Modal de Localização -->
    <div id="location-modal" class="fixed inset-0 z-[100] hidden bg-black/90 backdrop-blur-md flex items-center justify-center opacity-0 transition-opacity duration-300 p-4">
        <div class="bg-[#111111] border border-brand-gold/30 rounded-2xl w-full max-w-sm p-6 relative transform scale-95 transition-transform duration-300" id="location-modal-content">
            <button onclick="closeLocationModal()" class="absolute top-4 right-4 text-gray-400 hover:text-white">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
            <div class="text-brand-gold mb-4 flex justify-center">
                <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
            </div>
            <h3 id="loc-modal-title" class="text-2xl font-heading text-center text-brand-light mb-2">Clínica</h3>
            <p id="loc-modal-address" class="text-gray-400 text-sm text-center mb-6 font-light">Endereço...</p>
            
            <div class="flex flex-col gap-3">
                <a id="loc-modal-maps-btn" href="#" target="_blank" class="w-full bg-brand-gold text-brand-dark text-center font-semibold py-3 rounded-xl hover:bg-white transition-colors">
                    Abrir no Google Maps
                </a>
                <a id="loc-modal-ig-btn" href="#" target="_blank" class="w-full bg-transparent text-brand-light text-center font-semibold py-3 rounded-xl border border-white/10 hover:bg-white/5 transition-colors flex items-center justify-center gap-2">
                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
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
            const content = document.getElementById('location-modal-content');
            
            modal.classList.remove('hidden');
            // Allow display block to apply before animating opacity
            requestAnimationFrame(() => {
                modal.classList.remove('opacity-0');
                content.classList.remove('scale-95');
                content.classList.add('scale-100');
            });
        }

        function closeLocationModal() {
            const modal = document.getElementById('location-modal');
            const content = document.getElementById('location-modal-content');
            
            modal.classList.add('opacity-0');
            content.classList.remove('scale-100');
            content.classList.add('scale-95');
            
            setTimeout(() => {
                modal.classList.add('hidden');
            }, 300);
        }

        // Fechar ao clicar fora
        document.getElementById('location-modal').addEventListener('click', function(e) {
            if (e.target === this) {
                closeLocationModal();
            }
        });
    </script>
</body>
"""

content = content.replace("</body>", injection_js_modal)

# The new HTML block for the buttons
companies_block = """
            <h2 class="text-xs uppercase tracking-[0.2em] text-brand-gold text-center mb-6 mt-10">Minhas Empresas</h2>

            <!-- SOS Clínica -->
            <button onclick="openLocationModal('sos')"
               class="glass-btn w-full flex items-center justify-between p-4 rounded-xl transition-all duration-300 group mb-3">
                <div class="flex items-center gap-4">
                    <div class="bg-white/5 p-2 rounded-lg text-brand-gold group-hover:bg-brand-gold/10 transition-colors">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                    </div>
                    <div class="text-left">
                        <p class="font-semibold text-brand-light text-base">SOS Clínica Alagoas</p>
                        <p class="text-gray-400 text-[11px]">@sosclinicaalagoas</p>
                    </div>
                </div>
                <svg class="w-5 h-5 text-gray-500 group-hover:text-brand-gold group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </button>

            <!-- SOS Bem Estar -->
            <button onclick="openLocationModal('bemestar')"
               class="glass-btn w-full flex items-center justify-between p-4 rounded-xl transition-all duration-300 group mb-3">
                <div class="flex items-center gap-4">
                    <div class="bg-white/5 p-2 rounded-lg text-brand-gold group-hover:bg-brand-gold/10 transition-colors">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                    </div>
                    <div class="text-left">
                        <p class="font-semibold text-brand-light text-base">Clínica SOS Bem Estar</p>
                        <p class="text-gray-400 text-[11px]">@clinica.sosbemestar</p>
                    </div>
                </div>
                <svg class="w-5 h-5 text-gray-500 group-hover:text-brand-gold group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </button>

            <!-- Instituto Ornare -->
            <button onclick="openLocationModal('ornare')"
               class="glass-btn w-full flex items-center justify-between p-4 rounded-xl transition-all duration-300 group mb-3">
                <div class="flex items-center gap-4">
                    <div class="bg-white/5 p-2 rounded-lg text-brand-gold group-hover:bg-brand-gold/10 transition-colors">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                    </div>
                    <div class="text-left">
                        <p class="font-semibold text-brand-light text-base">Instituto Ornare</p>
                        <p class="text-gray-400 text-[11px]">@institutoornare.io</p>
                    </div>
                </div>
                <svg class="w-5 h-5 text-gray-500 group-hover:text-brand-gold group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </button>

            <!-- Hiperbárica -->
            <button onclick="openLocationModal('hiperbarica')"
               class="glass-btn w-full flex items-center justify-between p-4 rounded-xl transition-all duration-300 group mb-8">
                <div class="flex items-center gap-4">
                    <div class="bg-white/5 p-2 rounded-lg text-brand-gold group-hover:bg-brand-gold/10 transition-colors">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                    </div>
                    <div class="text-left">
                        <p class="font-semibold text-brand-light text-base">Hiperbárica do Agreste</p>
                        <p class="text-gray-400 text-[11px]">@hiperbaricadoagreste</p>
                    </div>
                </div>
                <svg class="w-5 h-5 text-gray-500 group-hover:text-brand-gold group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </button>
        </div>

        <!-- Perguntas Frequentes (FAQ Simplificado) -->
"""

import re
# We need to replace the old Instituto Ornare block with our new Minhas Empresas block
# We will match from `<!-- Instagram Instituto -->` down to `<!-- Perguntas Frequentes`

pattern = r"<!-- Instagram Instituto -->.*?<!-- Perguntas Frequentes \(FAQ Simplificado\) -->"
content = re.sub(pattern, companies_block, content, flags=re.DOTALL)

with open(file_path, "w") as f:
    f.write(content)

print("Linktree updated with companies modal!")
