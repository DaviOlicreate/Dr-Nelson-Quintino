import re
import os
import shutil

file_path = "index.html"
with open(file_path, "r") as f:
    content = f.read()

# Make the certificates directory
os.makedirs("assets/images/certificados", exist_ok=True)
# Copy some temp photos so the gallery isn't completely broken
try:
    shutil.copy2("assets/images/drnelson/foto4.jpg", "assets/images/certificados/cert1.jpg")
    shutil.copy2("assets/images/drnelson/foto5.jpg", "assets/images/certificados/cert2.jpg")
    shutil.copy2("assets/images/drnelson/foto6.jpg", "assets/images/certificados/cert3.jpg")
except:
    pass

certificados_html = """
        <!-- Certificações Section -->
        <div class="mt-20 border-t border-brand-gold/30 pt-16">
            <div class="text-center mb-12">
                <h3 class="text-3xl font-playfair font-bold text-brand-dark mb-4">Títulos e Certificações</h3>
                <div class="w-16 h-1 bg-brand-gold mx-auto mb-6"></div>
                <p class="text-gray-600 max-w-2xl mx-auto">Reconhecimento oficial e especializações pelas principais instituições médicas do Brasil.</p>
            </div>
            
            <!-- Opção 1: Badges -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16">
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm flex flex-col items-center text-center group hover:border-brand-gold transition-colors duration-300">
                    <div class="w-16 h-16 bg-brand-gold/10 rounded-full flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300">
                        <svg class="w-8 h-8 text-brand-gold" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" /></svg>
                    </div>
                    <h4 class="font-bold text-gray-900 mb-2">Especialista em Otorrinolaringologia</h4>
                    <p class="text-sm text-gray-500">Associação Médica Brasileira (AMB) e ABORL-CCF</p>
                </div>
                
                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm flex flex-col items-center text-center group hover:border-brand-gold transition-colors duration-300">
                    <div class="w-16 h-16 bg-brand-gold/10 rounded-full flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300">
                        <svg class="w-8 h-8 text-brand-gold" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" /></svg>
                    </div>
                    <h4 class="font-bold text-gray-900 mb-2">Rinoplastia Estruturada</h4>
                    <p class="text-sm text-gray-500">Pós-Graduação Lato Sensu pela UNINGÁ</p>
                </div>

                <div class="bg-white p-6 rounded-xl border border-gray-200 shadow-sm flex flex-col items-center text-center group hover:border-brand-gold transition-colors duration-300">
                    <div class="w-16 h-16 bg-brand-gold/10 rounded-full flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300">
                        <svg class="w-8 h-8 text-brand-gold" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" /></svg>
                    </div>
                    <h4 class="font-bold text-gray-900 mb-2">Alergia e Imunoterapia</h4>
                    <p class="text-sm text-gray-500">Instituto Brasileiro de Alergia e Imunoterapia (IBAi)</p>
                </div>
            </div>

            <!-- Opção 2: Galeria de Certificados -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <a href="assets/images/certificados/cert1.jpg" target="_blank" class="block group relative rounded-lg overflow-hidden shadow-md border-4 border-white">
                    <img src="assets/images/certificados/cert1.jpg" alt="Título de Especialista" class="w-full h-48 object-cover object-top transition-transform duration-700 group-hover:scale-110">
                    <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center backdrop-blur-sm">
                        <span class="text-white font-semibold flex items-center gap-2">
                            <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3 0H7" /></svg>
                            Ampliar Documento
                        </span>
                    </div>
                </a>
                <a href="assets/images/certificados/cert2.jpg" target="_blank" class="block group relative rounded-lg overflow-hidden shadow-md border-4 border-white">
                    <img src="assets/images/certificados/cert2.jpg" alt="Rinoplastia Estruturada" class="w-full h-48 object-cover object-top transition-transform duration-700 group-hover:scale-110">
                    <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center backdrop-blur-sm">
                        <span class="text-white font-semibold flex items-center gap-2">
                            <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3 0H7" /></svg>
                            Ampliar Documento
                        </span>
                    </div>
                </a>
                <a href="assets/images/certificados/cert3.jpg" target="_blank" class="block group relative rounded-lg overflow-hidden shadow-md border-4 border-white">
                    <img src="assets/images/certificados/cert3.jpg" alt="Alergia e Imunoterapia" class="w-full h-48 object-cover object-top transition-transform duration-700 group-hover:scale-110">
                    <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center backdrop-blur-sm">
                        <span class="text-white font-semibold flex items-center gap-2">
                            <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3 0H7" /></svg>
                            Ampliar Documento
                        </span>
                    </div>
                </a>
            </div>
        </div>
"""

# Insert before the closing tag of the <section id="sobre">
# We need to find the end of the <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"> which is inside <section id="sobre">
# Alternatively, replace `</section>` with `certificados_html + "\n    </section>"` for only the first match after `<section id="sobre"`

match = re.search(r'(<section id="sobre"[\s\S]*?)(</section>)', content)
if match:
    new_section = match.group(1) + "\n" + certificados_html + "\n    " + match.group(2)
    content = content[:match.start()] + new_section + content[match.end():]
    
    with open(file_path, "w") as f:
        f.write(content)
    print("Injected Certificates successfully!")
else:
    print("Could not find <section id='sobre'>")
