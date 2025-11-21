
import zipfile
import os

zip_file_path = 'dataset.zip'
extract_path = 'dataset'

if not os.path.exists(extract_path):
    os.makedirs(extract_path)

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print(f"Files extracted to {extract_path}")
for root, dirs, files in os.walk(extract_path):
    for file in files:
        print(os.path.join(root, file))
