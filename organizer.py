import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("usage: python organizer.py <directory> [--apply]")
        sys.exit()

    target = Path(sys.argv[1])

    if not target.exists() or not target.is_dir():
        print("Error: target must be a directory.")
        sys.exit()

    for item in target.iterdir():
        if item.is_file():
            print(item.name)

if __name__ == "__main__":
    main()