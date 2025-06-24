import os

# Project root folder name
project_name = "finance-tracker"

# Folder structure to create
folders = [
    f"templates",
    f"static/css",
    f"static/js",
    f"utils",
]

# Empty file names to touch (optional)
files = [
    f"app.py",
    f"models.py",
    f"forms.py",
    f"requirements.txt",
    f"README.md",
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create empty files
for file_path in files:
    open(file_path, 'a').close()

print(f"✅ Created minimal folder structure for '{project_name}'")
