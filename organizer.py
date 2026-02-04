import sys
from pathlib import Path
import shutil

EXTENSION_CATEGORIES = {
    "Audio": {
        ".mp3", ".flac", ".wav", ".ogg", ".aac", ".m4a", ".opus"
    },
    "Images": {
        ".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tiff"
    },
    "Video": {
        ".mp4", ".mkv", ".avi", ".mov", ".webm", ".flv", ".wmv"
    },
    "Docs": {
        ".pdf", ".txt", ".md", ".rtf",
        ".doc", ".docx",
        ".odt",
        ".xls", ".xlsx",
        ".ods",
        ".ppt", ".pptx"
    },
    "Archives": {
        ".zip", ".tar", ".gz", ".bz2", ".xz",
        ".7z", ".rar"
    },
    "Code": {
        ".py", ".sh", ".js", ".ts", ".c", ".cpp", ".h",
        ".java", ".go", ".rs", ".php", ".html", ".css",
        ".json", ".yaml", ".yml", ".toml"
    }
}

def categorize_files(file: Path):
    for i in range(3):
        pass

def main():
    if len(sys.argv) < 2:
        print("usage: python organizer.py <directory> [--apply]")
        sys.exit()

    apply_changes = "--apply" in sys.argv
    
    target = Path(sys.argv[1])

    if not target.exists() or not target.is_dir():
        print("Error: target must be a directory.")
        sys.exit()

    if apply_changes:
        print("[APPLY MODE] Files will be moved")
    else:
        print("[DRY RUN] NO files will be moved")

    print(f"target: {target.absolute()}")
    print(" ")

    for item in target.iterdir():
        item_extension = item.suffix.lower()
        if item.is_file():
            for category in EXTENSION_CATEGORIES.keys():
                if item_extension in EXTENSION_CATEGORIES[category]:
                    item_key = category
                    category_path = target / category
                    if apply_changes:
                        if not category_path.exists():
                            category_path.mkdir(exist_ok=True)  # only create directories in APPLY MODE, NOT in dry run
                        shutil.move(f"{target.absolute()}/{item.name}", f"{target.absolute()}/{item_key}/")
                        print(f"Moved: {item.name} -> {item_key}/{item.name}")
                    else:
                        print(f"Would move: {item.name} -> {item_key}/")
        if item.is_dir():
            print(f"Skipping Directory: {item.name}")
            continue
            
if __name__ == "__main__":
    main()
