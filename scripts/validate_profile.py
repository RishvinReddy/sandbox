import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(BASE_DIR, "README.md")

MARKERS = [
    "CURRENTLY_BUILDING",
    "FLAGSHIP_PROJECTS",
    "TECH_STACK",
    "ACTIVITY",
    "GITHUB_ANALYTICS"
]

def main():
    if not os.path.exists(README_PATH):
        print("[ERROR] README.md not found.")
        sys.exit(1)
        
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        
    errors = 0
    
    for marker in MARKERS:
        start_tag = f"<!-- {marker}_START -->"
        end_tag = f"<!-- {marker}_END -->"
        
        if start_tag not in content:
            print(f"[ERROR] Missing start marker: {start_tag}")
            errors += 1
            
        if end_tag not in content:
            print(f"[ERROR] Missing end marker: {end_tag}")
            errors += 1
            
        if start_tag in content and end_tag in content:
            start_idx = content.find(start_tag)
            end_idx = content.find(end_tag)
            if start_idx > end_idx:
                print(f"[ERROR] Markers out of order for {marker}")
                errors += 1
                
    if len(content) < 1000:
        print("[ERROR] README.md is suspiciously short. Possible truncation.")
        errors += 1
        
    if errors > 0:
        print(f"[FAIL] Validation failed with {errors} errors.")
        sys.exit(1)
        
    print("[SUCCESS] README.md validation passed.")

if __name__ == "__main__":
    main()
