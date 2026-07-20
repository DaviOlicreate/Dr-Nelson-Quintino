import os
import re

file_path = "linktree/index.html"
with open(file_path, "r") as f:
    content = f.read()

# 1. Add iframe container to the modal HTML
# We find: `<div style="display: flex; flex-direction: column; gap: 0.75rem;">`
# And inject the iframe container right before it.

iframe_html = """
            <div id="loc-modal-iframe-container" style="display: none; margin-bottom: 1.5rem; width: 100%; border-radius: 0.75rem; overflow: hidden; border: 1px solid rgba(255,255,255,0.1);">
                <iframe id="loc-modal-iframe" width="100%" height="250" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
            <div style="display: flex; flex-direction: column; gap: 0.75rem;">
"""

content = content.replace('<div style="display: flex; flex-direction: column; gap: 0.75rem;">', iframe_html)

# 2. Update the JS `companiesData` and `openLocationModal` function
# We need to replace the `companiesData` JS block

js_replacement = """        const companiesData = {
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
                embed: null
            },
            'ornare': {
                title: 'Instituto Ornare',
                address: 'Arapiraca - AL',
                maps: 'https://www.google.com/maps/place/SOS+Cl%C3%ADnica+Integrada+Arapiraca+-+AL/@-9.7574996,-36.6594729,17z/data=!3m1!4b1!4m6!3m5!1s0x705d5c443dd9b9b:0xfc88d46705fad62f!8m2!3d-9.7575049!4d-36.656898!16s%2Fg%2F11h18jk4mz?entry=ttu',
                ig: 'https://www.instagram.com/institutoornare.io/',
                embed: null
            },
            'hiperbarica': {
                title: 'Hiperbárica do Agreste',
                address: 'R. Prof. Domingos Correia, 848, Arapiraca - AL',
                maps: 'https://www.google.com/maps/search/?api=1&query=R.+Prof.+Domingos+Correia,+848,+Arapiraca+-+AL',
                ig: 'https://www.instagram.com/hiperbaricadoagreste/',
                embed: null
            }
        };

        function openLocationModal(id) {
            const data = companiesData[id];
            document.getElementById('loc-modal-title').innerText = data.title;
            document.getElementById('loc-modal-address').innerText = data.address;
            document.getElementById('loc-modal-maps-btn').href = data.maps;
            document.getElementById('loc-modal-ig-btn').href = data.ig;
            
            const iframeContainer = document.getElementById('loc-modal-iframe-container');
            const iframe = document.getElementById('loc-modal-iframe');
            const mapsBtn = document.getElementById('loc-modal-maps-btn');
            
            if (data.embed) {
                iframe.src = data.embed;
                iframeContainer.style.display = 'block';
                // Opcional: mudar o texto do botão já que o mapa está visível
                mapsBtn.innerText = "Abrir no app do Google Maps";
            } else {
                iframe.src = '';
                iframeContainer.style.display = 'none';
                mapsBtn.innerText = "Ver Localização no Mapa";
            }
            
            const modal = document.getElementById('location-modal');
            const content = document.getElementById('location-modal-content');"""

old_js_pattern = r"const companiesData = \{.*const content = document\.getElementById\('location-modal-content'\);"
content = re.sub(old_js_pattern, js_replacement, content, flags=re.DOTALL)

with open(file_path, "w") as f:
    f.write(content)

print("Modal updated with embedded map test!")
