import os
import re

file_path = "linktree/index.html"
with open(file_path, "r") as f:
    content = f.read()

# Fix Modal Box Background and Border
# Current: background-color: #0B1120; border-top: 1px solid rgba(201, 168, 106, 0.2);
content = content.replace(
    'background-color: #0B1120; border-top: 1px solid rgba(201, 168, 106, 0.2);',
    'background-color: #0a0d0b; border-top: 2px solid #bda662;'
)

# Fix Close Button
# Current: background-color: #1A1A1A; border: 1px solid rgba(201, 168, 106, 0.3);
content = content.replace(
    'background-color: #1A1A1A; border: 1px solid rgba(201, 168, 106, 0.3);',
    'background-color: #050706; border: 1px solid rgba(189,166,98,0.3); color: #bda662;'
)

# Fix Close Button Hover
# Current: background-color: #262626; border: 1px solid rgba(201, 168, 106, 0.5);
content = content.replace(
    'background-color: #262626; border: 1px solid rgba(201, 168, 106, 0.5);',
    'background-color: rgba(189,166,98,0.1); border: 1px solid rgba(189,166,98,0.5); color: #bda662;'
)

# Fix Drag Handle
# Current: background-color: rgba(201, 168, 106, 0.3);
content = content.replace(
    'background-color: rgba(201, 168, 106, 0.3);',
    'background-color: #bda662;'
)

# Fix "Abrir App do Google Maps" Button
# Current: background-color: #c9a86a; color: #1a1a1a;
content = content.replace(
    'background-color: #c9a86a; color: #1a1a1a;',
    'background-color: #bda662; color: #0a0d0b;'
)

with open(file_path, "w") as f:
    f.write(content)

print("Modal styling updated to black and gold successfully!")
