import os
import shutil

source_dir = "Fotos Dr. Nelson"
target_dir = "assets/images/drnelson"

os.makedirs(target_dir, exist_ok=True)

# List all files
files = sorted([f for f in os.listdir(source_dir) if f.endswith(".jpeg") or f.endswith(".jpg")])

for i, filename in enumerate(files, start=1):
    src = os.path.join(source_dir, filename)
    dst = os.path.join(target_dir, f"foto{i}.jpg")
    shutil.copy2(src, dst)
    print(f"Copied {filename} to {dst}")
