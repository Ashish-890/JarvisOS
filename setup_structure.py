from pathlib import Path

# Root project directory
ROOT = Path(__file__).parent

# Folders to create
folders = [
    "app/actions",
    "app/router",
    "app/config",
    "app/utils",
    "app/memory",
    "app/vision",
    "app/plugins",
    "docs",
    "assets",
]

# Files to create
files = [
    "app/actions/__init__.py",
    "app/actions/apps.py",
    "app/actions/browser.py",
    "app/actions/system.py",
    "app/actions/media.py",
    "app/actions/files.py",
    "app/actions/dispatcher.py",

    "app/router/__init__.py",
    "app/router/intent.py",
    "app/router/classifier.py",
    "app/router/router.py",

    "app/config/__init__.py",
    "app/config/settings.py",

    "app/utils/__init__.py",
    "app/utils/logger.py",

    "app/memory/__init__.py",
    "app/memory/memory.py",

    "app/vision/__init__.py",
    "app/vision/vision.py",

    "app/plugins/__init__.py",
]

# Create folders
for folder in folders:
    path = ROOT / folder
    path.mkdir(parents=True, exist_ok=True)
    print(f"Created folder: {folder}")

# Create files
for file in files:
    path = ROOT / file

    if not path.exists():
        path.touch()
        print(f"Created file: {file}")
    else:
        print(f"Already exists: {file}")

print("\n✅ JarvisOS project structure created successfully!")