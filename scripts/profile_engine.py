import os
import sys

from config import load_config, README_PATH
from github_api import fetch_repositories
from generate_projects import generate_currently_building, generate_flagship_projects
from generate_tech_stack import generate_tech_stack
from generate_activity import generate_activity
from update_readme import read_readme, write_readme, update_section
import datetime

def main():
    print("[INFO] Starting Profile Engine v2...")
    
    config = load_config()
    if not config:
        sys.exit(1)
        
    print("[INFO] Fetching repository data from GitHub API...")
    repos = fetch_repositories()
    if repos is None:
        print("[ERROR] Failed to fetch repositories.")
        sys.exit(1)
        
    print("[INFO] Reading current README.md...")
    readme_content = read_readme(README_PATH)
    if not readme_content:
        print("[ERROR] README.md not found.")
        sys.exit(1)

    print("[INFO] Generating Currently Building section...")
    currently_building_md = generate_currently_building(config)
    readme_content = update_section(readme_content, "CURRENTLY_BUILDING", currently_building_md)

    print("[INFO] Generating Flagship Systems section...")
    flagship_md = generate_flagship_projects(config)
    readme_content = update_section(readme_content, "FLAGSHIP_PROJECTS", flagship_md)

    print("[INFO] Generating Tech Stack section...")
    tech_stack_md = generate_tech_stack(repos, config)
    readme_content = update_section(readme_content, "TECH_STACK", tech_stack_md)
    
    print("[INFO] Generating Latest Activity section...")
    activity_md = generate_activity(repos, config)
    readme_content = update_section(readme_content, "ACTIVITY", activity_md)

    # Update Last synchronized date at the top of the README
    date_str = datetime.datetime.now(datetime.timezone.utc).strftime("%d %b %Y")
    import re
    readme_content = re.sub(r"_Last synchronized: .*?_", f"_Last synchronized: {date_str}_", readme_content)

    print("[INFO] Writing updated README.md...")
    write_readme(README_PATH, readme_content)
    
    print("[INFO] Profile Engine v2 update complete!")

if __name__ == "__main__":
    main()
