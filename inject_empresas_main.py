import re

file_path = "index.html"
with open(file_path, "r") as f:
    content = f.read()

empresas_section = """
    <!-- Minhas Empresas -->
    <section id="empresas" class="py-24 bg-brand-dark text-white relative">
        <div class="container mx-auto px-6 lg:px-12 max-w-7xl">
            <div class="text-center mb-16">
                <div class="flex items-center justify-center gap-4 mb-4">
                    <div class="h-[1px] w-8 bg-brand-gold"></div>
                    <span class="text-brand-gold uppercase text-[10px] tracking-widest">Atendimento e Localização</span>
                    <div class="h-[1px] w-8 bg-brand-gold"></div>
                </div>
                <h2 class="text-3xl md:text-4xl font-heading font-light leading-snug">
                    Minhas Empresas e Parceiros
                </h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- SOS Clínica -->
                <button onclick="openLocationModal('sos')" class="text-left bg-white/5 border border-white/10 p-8 rounded-sm hover:border-brand-gold/50 hover:bg-white/10 transition-all duration-300 group">
                    <div class="bg-brand-darker p-3 w-12 h-12 flex items-center justify-center text-brand-gold mb-6 group-hover:scale-110 transition-transform">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                    </div>
                    <h3 class="text-xl font-heading mb-2 group-hover:text-brand-gold transition-colors">SOS Clínica Alagoas</h3>
                    <p class="text-gray-400 text-sm mb-6">@sosclinicaalagoas</p>
                    <span class="text-brand-gold text-[10px] uppercase tracking-widest flex items-center gap-2">
                        Ver Localização <svg class="w-3 h-3 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </span>
                </button>

                <!-- SOS Bem Estar -->
                <button onclick="openLocationModal('bemestar')" class="text-left bg-white/5 border border-white/10 p-8 rounded-sm hover:border-brand-gold/50 hover:bg-white/10 transition-all duration-300 group">
                    <div class="bg-brand-darker p-3 w-12 h-12 flex items-center justify-center text-brand-gold mb-6 group-hover:scale-110 transition-transform">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                    </div>
                    <h3 class="text-xl font-heading mb-2 group-hover:text-brand-gold transition-colors">Clínica SOS Bem Estar</h3>
                    <p class="text-gray-400 text-sm mb-6">@clinica.sosbemestar</p>
                    <span class="text-brand-gold text-[10px] uppercase tracking-widest flex items-center gap-2">
                        Ver Localização <svg class="w-3 h-3 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </span>
                </button>

                <!-- Instituto Ornare -->
                <button onclick="openLocationModal('ornare')" class="text-left bg-white/5 border border-white/10 p-8 rounded-sm hover:border-brand-gold/50 hover:bg-white/10 transition-all duration-300 group">
                    <div class="bg-brand-darker p-3 w-12 h-12 flex items-center justify-center text-brand-gold mb-6 group-hover:scale-110 transition-transform">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                    </div>
                    <h3 class="text-xl font-heading mb-2 group-hover:text-brand-gold transition-colors">Instituto Ornare</h3>
                    <p class="text-gray-400 text-sm mb-6">@institutoornare.io</p>
                    <span class="text-brand-gold text-[10px] uppercase tracking-widest flex items-center gap-2">
                        Ver Localização <svg class="w-3 h-3 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </span>
                </button>

                <!-- Hiperbárica -->
                <button onclick="openLocationModal('hiperbarica')" class="text-left bg-white/5 border border-white/10 p-8 rounded-sm hover:border-brand-gold/50 hover:bg-white/10 transition-all duration-300 group">
                    <div class="bg-brand-darker p-3 w-12 h-12 flex items-center justify-center text-brand-gold mb-6 group-hover:scale-110 transition-transform">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                    </div>
                    <h3 class="text-xl font-heading mb-2 group-hover:text-brand-gold transition-colors">Hiperbárica do Agreste</h3>
                    <p class="text-gray-400 text-sm mb-6">@hiperbaricadoagreste</p>
                    <span class="text-brand-gold text-[10px] uppercase tracking-widest flex items-center gap-2">
                        Ver Localização <svg class="w-3 h-3 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </span>
                </button>
            </div>
        </div>
    </section>
"""

# Insert before <section id="contato"
if '<section id="contato"' in content:
    content = content.replace('<section id="contato"', empresas_section + '\n<section id="contato"')

modal_html_js = """
    <!-- Modal de Localização -->
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
        background-color: #0a0d0b; border-top: 2px solid #bda662; 
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
        background-color: #bda662;
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
        background-color: #050706; border: 1px solid rgba(189,166,98,0.3); color: #bda662;
        text-align: center;
        font-weight: 700;
        font-size: 1rem;
        padding: 1rem;
        border-radius: 1rem;
        cursor: pointer;
        margin-top: 1.5rem;
        transition: background-color 0.2s;
    }
    .close-btn:hover {
        background-color: rgba(189,166,98,0.1); border: 1px solid rgba(189,166,98,0.5); color: #bda662;
    }
    </style>

    <div id="location-modal" class="custom-loc-overlay">
        <div class="custom-loc-box" id="location-modal-content">
            <div class="drag-handle"></div>
            
            <h3 id="loc-modal-title" class="loc-title">Localização</h3>
            
            <div class="loc-desc-container">
                <svg style="width: 1.25rem; height: 1.25rem; color: #9CA3AF; margin-top: 0.125rem; flex-shrink: 0;" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"></path></svg>
                <p id="loc-modal-address" class="loc-desc">Endereço...</p>
            </div>
            
            <div id="loc-modal-iframe-container" style="display: none; width: 100%; border-radius: 0.75rem; overflow: hidden; background-color: #E5E7EB;">
                <iframe id="loc-modal-iframe" width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
            
            <div id="loc-modal-fallback" style="display: flex; flex-direction: column; gap: 0.75rem; margin-top: 1rem;">
                <a id="loc-modal-maps-btn" href="#" target="_blank" style="width: 100%; background-color: #bda662; color: #0a0d0b; text-align: center; font-weight: 600; padding: 0.75rem; border-radius: 0.75rem; text-decoration: none; display: block;">
                    Abrir App do Google Maps
                </a>
                <a id="loc-modal-ig-btn" href="#" target="_blank" style="width: 100%; background-color: transparent; color: #f3f4f6; text-align: center; font-weight: 600; padding: 0.75rem; border-radius: 0.75rem; border: 1px solid rgba(255,255,255,0.1); text-decoration: none; display: flex; align-items: center; justify-content: center; gap: 0.5rem;">
                    <svg class="w-5 h-5" style="width: 1.25rem; height: 1.25rem;" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
                    Acessar Instagram
                </a>
            </div>
            
            <button onclick="closeLocationModal()" class="close-btn">Fechar</button>
        </div>
    </div>

    <script>
        const companiesData = {
            'sos': {
                title: 'SOS Clínica Integrada',
                address: 'Arapiraca - AL',
                maps: 'https://www.google.com/maps/place/SOS+Cl%C3%ADnica+Integrada+Arapiraca+-+AL/@-9.7573837,-36.656806,15z/data=!4m6!3m5!1s0x705d5c443dd9b9b:0xfc88d46705fad62f!8m2!3d-9.7575049!4d-36.656898!16s%2Fg%2F11h18jk4mz?entry=ttu',
                ig: 'https://www.instagram.com/sosclinicaalagoas/',
                embed: 'https://maps.google.com/maps?q=SOS+Cl%C3%ADnica+Integrada+Arapiraca&t=&z=15&ie=UTF8&iwloc=&output=embed'
            },
            'bemestar': {
                title: 'Clínica SOS Bem Estar',
                address: 'Arapiraca - AL',
                maps: 'https://www.google.com/maps/place/SOS+Cl%C3%ADnica+Integrada+Arapiraca+-+AL/@-9.7573837,-36.656806,15z/data=!4m6!3m5!1s0x705d5c443dd9b9b:0xfc88d46705fad62f!8m2!3d-9.7575049!4d-36.656898!16s%2Fg%2F11h18jk4mz?entry=ttu',
                ig: 'https://www.instagram.com/clinica.sosbemestar/',
                embed: 'https://maps.google.com/maps?q=SOS+Cl%C3%ADnica+Integrada+Arapiraca&t=&z=15&ie=UTF8&iwloc=&output=embed'
            },
            'ornare': {
                title: 'Instituto Ornare',
                address: 'Arapiraca - AL',
                maps: 'https://www.google.com/maps/place/SOS+Cl%C3%ADnica+Integrada+Arapiraca+-+AL/@-9.7574996,-36.6594729,17z/data=!3m1!4b1!4m6!3m5!1s0x705d5c443dd9b9b:0xfc88d46705fad62f!8m2!3d-9.7575049!4d-36.656898!16s%2Fg%2F11h18jk4mz?entry=ttu',
                ig: 'https://www.instagram.com/institutoornare.io/',
                embed: 'https://maps.google.com/maps?q=SOS+Cl%C3%ADnica+Integrada+Arapiraca&t=&z=15&ie=UTF8&iwloc=&output=embed'
            },
            'hiperbarica': {
                title: 'Hiperbárica do Agreste',
                address: 'R. Prof. Domingos Correia, 848, Arapiraca - AL',
                maps: 'https://www.google.com/maps/search/?api=1&query=R.+Prof.+Domingos+Correia,+848,+Arapiraca+-+AL',
                ig: 'https://www.instagram.com/hiperbaricadoagreste/',
                embed: 'https://maps.google.com/maps?q=R.+Prof.+Domingos+Correia,+848,+Arapiraca+-+AL&t=&z=15&ie=UTF8&iwloc=&output=embed'
            }
        };

        function openLocationModal(id) {
            const data = companiesData[id];
            
            const titleEl = document.getElementById('loc-modal-title');
            if(titleEl) titleEl.innerText = data.title;
            
            document.getElementById('loc-modal-address').innerText = data.address;
            document.getElementById('loc-modal-maps-btn').href = data.maps;
            document.getElementById('loc-modal-ig-btn').href = data.ig;
            
            const iframeContainer = document.getElementById('loc-modal-iframe-container');
            const iframe = document.getElementById('loc-modal-iframe');
            
            if (data.embed) {
                iframe.src = data.embed;
                iframeContainer.style.display = 'block';
            } else {
                iframe.src = '';
                iframeContainer.style.display = 'none';
            }
            
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
                document.getElementById('loc-modal-iframe').src = '';
            }, 400);
        }

        document.addEventListener('DOMContentLoaded', () => {
            const modal = document.getElementById('location-modal');
            if(modal) {
                modal.addEventListener('click', function(e) {
                    if (e.target === this) {
                        closeLocationModal();
                    }
                });
            }
        });
    </script>
</body>
"""

# Insert modal logic right before </body>
if '</body>' in content:
    content = content.replace('</body>', modal_html_js)

with open(file_path, "w") as f:
    f.write(content)

print("Minhas empresas section added to main index.html")
