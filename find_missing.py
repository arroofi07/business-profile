import os
import re

DATA_FILE = r"r:\demo-client\clinic\src\lib\data.ts"

with open(DATA_FILE, 'r', encoding='utf-8') as f:
    text = f.read()

# Find the allProducts array
start_idx = text.find('export const allProducts = [')
if start_idx == -1:
    print("Could not find allProducts array")
    exit(1)

text_from_array = text[start_idx:]
end_idx = text_from_array.find('];')
if end_idx == -1:
    print("Could not find end of allProducts array")
    exit(1)

products_text = text_from_array[:end_idx+2]

missing = []
for line in products_text.split('\n'):
    match = re.search(r"{ id:\s*(\d+),\s*name:\s*'([^']+)'", line)
    if match:
        id_str = match.group(1)
        name = match.group(2)
        if " image:" not in line:
            missing.append(name)

for name in missing:
    print(name)

print(f"\nTotal missing: {len(missing)}")
