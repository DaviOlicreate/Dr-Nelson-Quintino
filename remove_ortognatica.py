import os

file_path = "index.html"
with open(file_path, "r") as f:
    lines = f.readlines()

new_lines = []
skip = False

for i, line in enumerate(lines):
    # 1. Remove Card Ortognática (line 359 to 373 originally)
    if "<!-- Card Ortognática -->" in line:
        skip = True
    
    # 2. Remove Modal Ortognática (line 2616 to 2781 originally)
    if "<!-- Modal Ortognática -->" in line:
        skip = True
        
    if not skip:
        # 3. Replace text in the bio
        if "Lifting Facial, Lipo de Papada, Mentoplastia e Ortognática" in line:
            line = line.replace(
                "Lifting Facial, Lipo de Papada, Mentoplastia e Ortognática.", 
                "Lifting Facial, Lipo de Papada e Mentoplastia."
            )
        new_lines.append(line)
        
    # Find the end of the skipped blocks
    if skip:
        # The Card block ends right before <!-- Card Cirurgias combinadas -->
        if "<!-- Card Cirurgias combinadas -->" in lines[i+1] if i+1 < len(lines) else False:
            skip = False
        # The Modal block ends right before <!-- Modal Cirurgias combinadas -->
        if "<!-- Modal Cirurgias combinadas -->" in lines[i+1] if i+1 < len(lines) else False:
            skip = False

with open(file_path, "w") as f:
    f.writelines(new_lines)

print("Ortognática section removed successfully.")
