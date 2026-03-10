import os
import re

DATA_FILE = r"r:\demo-client\clinic\src\lib\data.ts"
IMG_DIR = r"r:\demo-client\clinic\static\images\catalog"

# Collect all jpg paths relative to static
image_paths = []
for root, dirs, files in os.walk(IMG_DIR):
    for f in files:
        if f.lower().endswith('.jpg'):
            rel_path = os.path.relpath(os.path.join(root, f), r"r:\demo-client\clinic\static").replace('\\', '/')
            image_paths.append((f.replace('.jpg', ''), "/" + rel_path))

def normalize_name(name):
    return re.sub(r'[^a-z0-9]', '', name.lower())

image_map = {normalize_name(name): path for name, path in image_paths}
# Add manual overrides for slight naming differences
# e.g., 'Giannt Banner' -> 'Giant Banner'
image_map['giantbanner'] = image_map.get('gianntbanner')
image_map['tripodbanner'] = image_map.get('tripodbaner')
image_map['rollupbanner'] = image_map.get('rolupbanner')
image_map['wallpaper'] = image_map.get('wallpaperdinding')
image_map['cuttingsticker'] = image_map.get('cuttingstiker')
image_map['undangan'] = image_map.get('undanganpernikahan')
image_map['amplop'] = image_map.get('amplopcustom')
image_map['katalog'] = image_map.get('katalogproduk')
image_map['pen'] = image_map.get('penpulpen')

with open(DATA_FILE, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    match = re.search(r"{ id:\s*\d+,\s*name:\s*'([^']+)'", line)
    if match:
        name = match.group(1)
        norm_name = normalize_name(name)
        if norm_name in image_map and image_map[norm_name]:
            img_path = image_map[norm_name]
            # insert image property before emoji
            new_line = re.sub(r"(\s*emoji:)", f" image: '{img_path}',\\1", line)
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open(DATA_FILE, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Updated {DATA_FILE}")
