import os
import re

file_path = "index.html"
with open(file_path, "r") as f:
    content = f.read()

# Define the new section HTML
new_section = """<section id="publicacoes" class="py-24 bg-brand-light relative overflow-hidden">
        <div class="container mx-auto px-6 lg:px-12 relative z-10">
            <div class="text-center mb-16">
                <div class="flex items-center justify-center gap-4 mb-4">
                    <div class="h-[1px] w-8 bg-brand-gold"></div>
                    <span class="text-brand-gold uppercase text-[10px] tracking-widest">Produção Científica</span>
                    <div class="h-[1px] w-8 bg-brand-gold"></div>
                </div>
                <h2 class="text-3xl md:text-4xl font-heading font-light leading-snug max-w-4xl mx-auto text-brand-dark">
                    Autor de artigos científicos e pesquisas na área de Otorrinolaringologia e Cirurgia Cérvico-Facial
                </h2>
            </div>
            <div class="flex flex-col lg:flex-row gap-16 items-start">
                
                <!-- Coluna Imagem -->
                <div class="w-full lg:w-5/12 lg:sticky top-32">
                    <div class="relative aspect-[3/4] overflow-hidden rounded-sm shadow-2xl">
                        <img src="./sobre.jpg" onerror="this.src='https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'" alt="Produção Científica" class="w-full h-full object-cover" style="object-position: top;">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-dark via-brand-dark/60 to-transparent"></div>
                        <div class="absolute bottom-0 left-0 p-8 w-full">
                            <h2 class="text-3xl md:text-5xl font-heading mb-4 font-light leading-snug text-white drop-shadow-lg">Produção<br/><span class="text-brand-gold italic">Científica</span></h2>
                            <p class="text-white/95 font-medium text-sm max-w-sm drop-shadow-md">
                                Contribuição ativa para o avanço da otorrinolaringologia com diversas publicações em revistas e congressos.
                            </p>
                            <a href="http://buscatextual.cnpq.br/buscatextual/visualizacv.do?metodo=apresentar&id=K4717857U5" target="_blank" rel="noopener noreferrer" class="inline-block mt-6 border border-brand-gold text-brand-gold px-6 py-2.5 hover:bg-brand-gold hover:text-brand-dark transition-all uppercase tracking-widest text-[10px] font-semibold">
                                Ver Currículo Lattes
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Coluna Artigos -->
                <div class="w-full lg:w-7/12 space-y-4 pt-4">

                    <details class="group border border-gray-200 bg-white rounded-sm shadow-sm hover:shadow-md transition-shadow" open>
                        <summary class="flex justify-between items-center font-medium cursor-pointer list-none p-6 text-brand-dark hover:text-brand-gold transition-colors duration-300">
                            <span class="text-lg md:text-xl font-heading font-light tracking-wide">Publicações no Brazilian Journal of Otorhinolaryngology</span>
                            <span class="transition group-open:rotate-180 text-brand-gold">
                                <svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                            </span>
                        </summary>
                        <div class="text-brand-dark/70 px-6 pb-6 pt-2 text-sm flex flex-col gap-3 border-t border-gray-100 bg-gray-50/50">

                            <a href="https://aborlccf.org.br/wp-content/uploads/2022/11/BJORL_Volume_82_Suplemento_2016-1.pdf" target="_blank" rel="noopener noreferrer" class="group/link flex justify-between items-center p-4 bg-white hover:bg-gray-100 border border-gray-100 hover:border-brand-gold/50 rounded-sm transition-colors duration-300 shadow-sm">
                                <span class="font-light pr-4 text-brand-dark group-hover/link:text-brand-darker group-hover/link:font-medium transition-all">Rinoplastia para correção da ponta em caixote</span>
                                <span class="text-brand-gold text-[10px] uppercase tracking-widest whitespace-nowrap flex items-center gap-2 group-hover/link:translate-x-1 transition-transform">
                                    BJORL 2016 
                                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                                </span>
                            </a>

                            <a href="https://aborlccf.org.br/wp-content/uploads/2022/11/BJORL_Volume_82_Suplemento_2016-1.pdf" target="_blank" rel="noopener noreferrer" class="group/link flex justify-between items-center p-4 bg-white hover:bg-gray-100 border border-gray-100 hover:border-brand-gold/50 rounded-sm transition-colors duration-300 shadow-sm">
                                <span class="font-light pr-4 text-brand-dark group-hover/link:text-brand-darker group-hover/link:font-medium transition-all">Audiometric Profile of a Specialized Service in Otorhinolaryngology</span>
                                <span class="text-brand-gold text-[10px] uppercase tracking-widest whitespace-nowrap flex items-center gap-2 group-hover/link:translate-x-1 transition-transform">
                                    BJORL 2016 
                                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                                </span>
                            </a>

                            <a href="https://aborlccf.org.br/wp-content/uploads/2022/11/BJORL_Volume_82_Suplemento_2016-1.pdf" target="_blank" rel="noopener noreferrer" class="group/link flex justify-between items-center p-4 bg-white hover:bg-gray-100 border border-gray-100 hover:border-brand-gold/50 rounded-sm transition-colors duration-300 shadow-sm">
                                <span class="font-light pr-4 text-brand-dark group-hover/link:text-brand-darker group-hover/link:font-medium transition-all">Prevalence of incidental sinus disease on Computed Tomography</span>
                                <span class="text-brand-gold text-[10px] uppercase tracking-widest whitespace-nowrap flex items-center gap-2 group-hover/link:translate-x-1 transition-transform">
                                    BJORL 2016 
                                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                                </span>
                            </a>

                            <a href="https://aborlccf.org.br/wp-content/uploads/2022/11/BJORL_Volume_82_Suplemento_2016-1.pdf" target="_blank" rel="noopener noreferrer" class="group/link flex justify-between items-center p-4 bg-white hover:bg-gray-100 border border-gray-100 hover:border-brand-gold/50 rounded-sm transition-colors duration-300 shadow-sm">
                                <span class="font-light pr-4 text-brand-dark group-hover/link:text-brand-darker group-hover/link:font-medium transition-all">Foreign Body in Otorhinolaryngology: Profile of Emergency Care</span>
                                <span class="text-brand-gold text-[10px] uppercase tracking-widest whitespace-nowrap flex items-center gap-2 group-hover/link:translate-x-1 transition-transform">
                                    BJORL 2016 
                                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                                </span>
                            </a>
                            
                            <a href="https://aborlccf.org.br/wp-content/uploads/2022/11/BJORL_vol.80_Supl.02_ANAIS-2015.pdf" target="_blank" rel="noopener noreferrer" class="group/link flex justify-between items-center p-4 bg-white hover:bg-gray-100 border border-gray-100 hover:border-brand-gold/50 rounded-sm transition-colors duration-300 shadow-sm">
                                <span class="font-light pr-4 text-brand-dark group-hover/link:text-brand-darker group-hover/link:font-medium transition-all">Escore clínico e polissonográfico em pacientes com SAHOS: existe correlação?</span>
                                <span class="text-brand-gold text-[10px] uppercase tracking-widest whitespace-nowrap flex items-center gap-2 group-hover/link:translate-x-1 transition-transform">
                                    BJORL 2015
                                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                                </span>
                            </a>

                        </div>
                    </details>

                </div>
            </div>
        </div>
    </section>"""

# Replace the whole section using regex
pattern = re.compile(r'<section id="publicacoes".*?</section>', re.DOTALL)
new_content = re.sub(pattern, new_section, content)

with open(file_path, "w") as f:
    f.write(new_content)

print("Publicacoes section updated successfully!")
