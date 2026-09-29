import os
import re

def update_section(content, section_name, new_text):
    """
    Updates the content inside <!-- {section_name}_START --> and <!-- {section_name}_END -->
    """
    start_marker = f"<!-- {section_name}_START -->"
    end_marker = f"<!-- {section_name}_END -->"
    
    pattern = re.compile(f"({start_marker}).*?({end_marker})", re.DOTALL)
    if not pattern.search(content):
        print(f"[WARNING] Markers for {section_name} not found.")
        return content

    new_content = f"\\1\n{new_text}\n\\2"
    return pattern.sub(new_content, content)

def read_readme(path):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_readme(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
