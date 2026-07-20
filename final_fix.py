import os
import re

file_path = "linktree/index.html"
with open(file_path, "r") as f:
    content = f.read()

# 1. Restore the circular profile image container
old_profile = r'<div style="width: 8rem; height: auto; margin-bottom: 1rem; display: flex; justify-content: center; align-items: center;">\s*<img src="profile\.jpg" alt="Dr\. Nelson Quintino" style="width: 100%; height: auto; object-fit: contain;">\s*</div>'

restored_profile = """<div class="w-32 h-32 rounded-full overflow-hidden border-2 border-brand-gold p-1 mb-4 shadow-[0_0_30px_rgba(189,166,98,0.2)] bg-brand-dark mx-auto" style="width: 8rem; height: 8rem; border-radius: 50%; overflow: hidden; border: 2px solid #c9a86a; padding: 0.25rem; margin-bottom: 1rem; background-color: #0B1120; box-shadow: 0 0 30px rgba(189,166,98,0.2);">
                <img src="./profile.jpg" alt="Dr. Nelson Quintino" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%; object-position: top;">
            </div>"""

content = re.sub(old_profile, restored_profile, content)


# 2. Update the JS to actually show the map iframe and include all embed links
script_pattern = r"<script>\s*const companiesData.*?</script>"
new_script = """<script>
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
            
            // Check which ID is currently being used in HTML to avoid errors
            const titleEl = document.getElementById('loc-modal-title') || document.getElementById('loc-modal-title-display');
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

        document.getElementById('location-modal').addEventListener('click', function(e) {
            if (e.target === this) {
                closeLocationModal();
            }
        });
    </script>"""

content = re.sub(script_pattern, new_script, content, flags=re.DOTALL)

with open(file_path, "w") as f:
    f.write(content)

print("Profile and logic script updated successfully!")
