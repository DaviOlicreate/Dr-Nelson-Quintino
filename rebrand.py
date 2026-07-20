import os

def replace_in_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Replacements
    replacements = [
        ("Ricardo Wathson", "Nelson Quintino"),
        ("Ricardo Whatson", "Nelson Quintino"),
        ("RICARDO WATHSON", "NELSON QUINTINO"),
        ("RICARDO", "NELSON"),
        ("Ricardo", "Nelson"),
        ("Wathson", "Quintino"),
        ("Whatson", "Quintino"),
        ("drricardowathson", "drnelsonquintino"),
        ("dr.ricardowathson", "dr.nelsonquintino"),
        ("ricardorwfc@gmail.com", "contato@drnelsonquintino.com.br") # Placeholder email
    ]

    new_content = content
    for old, new in replacements:
        new_content = new_content.replace(old, new)

    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

# Update HTML files
replace_in_file('index.html')
replace_in_file('linktree/index.html')

# Rename directories and files
import glob

def rename_recursive(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            new_name = name.replace("Ricardo", "Nelson").replace("Whatson", "Quintino").replace("Wathson", "Quintino").replace("drricardowathson", "drnelsonquintino")
            if new_name != name:
                os.rename(os.path.join(root, name), os.path.join(root, new_name))
        for name in dirs:
            if name == '.git': continue
            new_name = name.replace("Ricardo", "Nelson").replace("Whatson", "Quintino").replace("Wathson", "Quintino").replace("drricardowathson", "drnelsonquintino")
            if new_name != name:
                os.rename(os.path.join(root, name), os.path.join(root, new_name))

rename_recursive('.')
print("Done renaming!")
