import os
import shutil
import re

ARTIFACT_DIR = r"C:\Users\RYZEN 5\.gemini\antigravity\brain\afaafeab-e365-4204-b1d7-42ac3d9710d9"
TARGET_DIR = r"r:\demo-client\clinic\static\images\catalog\generated"
DATA_FILE = r"r:\demo-client\clinic\src\lib\data.ts"

os.makedirs(TARGET_DIR, exist_ok=True)

generated_files = [f for f in os.listdir(ARTIFACT_DIR) if f.endswith('.png')]

# Move files
image_map = {}
for file in generated_files:
    # Expected name: base_name_timestamp.png
    parts = file.rsplit('_', 1)
    if len(parts) == 2:
        base_name = parts[0]
        # Clean base_name (e.g. buku_agenda -> bukuagenda)
        norm_name = base_name.replace('_', '').lower()
        
        src_path = os.path.join(ARTIFACT_DIR, file)
        target_name = f"{base_name}.png"
        target_path = os.path.join(TARGET_DIR, target_name)
        
        shutil.copy2(src_path, target_path)
        
        image_map[norm_name] = f"/images/catalog/generated/{target_name}"

# Add fallbacks/overrides for mapping
image_map['usb'] = image_map.get('usbflashdrive')
image_map['pin'] = image_map.get('pincustom')
image_map['bukuagenda'] = image_map.get('bukuagenda')

with open(DATA_FILE, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    match = re.search(r"{ id:\s*\d+,\s*name:\s*'([^']+)'", line)
    if match and " image:" not in line:
        name = match.group(1)
        norm_name = re.sub(r'[^a-z0-9]', '', name.lower())
        
        if norm_name in image_map:
            img_path = image_map[norm_name]
            new_line = re.sub(r"(\s*emoji:)", f" image: '{img_path}',\\1", line)
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open(DATA_FILE, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Processed {len(generated_files)} images and updated data.ts")
