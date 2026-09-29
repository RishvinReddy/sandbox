import os
from svg.all_renderers import *
from config import load_config
from github_api import fetch_repositories
import datetime

def get_tech_stack_dict(repos, config):
    allowlist = set([lang.lower() for lang in config.get("tech_stack_allowlist", [])])
    categories = {
        "Languages": ["TypeScript", "JavaScript", "Python", "C++", "C", "SQL", "Solidity", "Java"],
        "Frontend": ["React", "Next.js", "Tailwind CSS"],
        "Backend": ["Node.js", "PostgreSQL", "Supabase", "SQLite", "Redis", "IPFS"],
        "Security / Systems": ["DFIR", "IoT", "MQTT", "Blockchain", "Electron"],
        "Infrastructure": ["Docker", "GitHub Actions", "AWS", "Vercel"]
    }
    result = {}
    for cat, items in categories.items():
        valid = [item for item in items if item.lower() in allowlist]
        if valid:
            result[cat] = valid
    return result

def main():
    print("[INFO] Loading config...")
    config = load_config()
    repos = fetch_repositories() or []
    
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "profile")
    os.makedirs(out_dir, exist_ok=True)
    
    print("[INFO] Generating SVGs...")
    date_str = datetime.datetime.now(datetime.timezone.utc).strftime("%d %b %Y")
    
    sorted_repos = sorted([r for r in repos if not r.get("private") and not r.get("fork")], key=lambda x: x.get("updated_at", ""), reverse=True)
    activities = []
    for r in sorted_repos[:4]:
        date = datetime.datetime.strptime(r['updated_at'], "%Y-%m-%dT%H:%M:%SZ").strftime("%b %d").upper()
        activities.append({
            "date": date,
            "repo": r['name'],
            "desc": (r.get("description") or "Updated")[:40]
        })
        
    stack_dict = get_tech_stack_dict(repos, config)
    stats = {"repos": len(repos)}
    
    for theme in ["light", "dark"]:
        print(f"[INFO] Rendering {theme} theme...")
        
        with open(os.path.join(out_dir, f"hero-{theme}.svg"), "w") as f:
            f.write(render_hero(theme))
            
        with open(os.path.join(out_dir, f"currently-building-{theme}.svg"), "w") as f:
            f.write(render_currently_building(config.get("featured", []), theme))
            
        with open(os.path.join(out_dir, f"flagship-systems-{theme}.svg"), "w") as f:
            f.write(render_flagships(config.get("featured", []), theme))
            
        with open(os.path.join(out_dir, f"domains-{theme}.svg"), "w") as f:
            f.write(render_domains(theme))
            
        with open(os.path.join(out_dir, f"tech-stack-{theme}.svg"), "w") as f:
            f.write(render_stack(stack_dict, theme))
            
        with open(os.path.join(out_dir, f"activity-{theme}.svg"), "w") as f:
            f.write(render_activity(activities, date_str, theme))
            
        with open(os.path.join(out_dir, f"experience-{theme}.svg"), "w") as f:
            f.write(render_experience(theme))
            
        with open(os.path.join(out_dir, f"activity-stats-{theme}.svg"), "w") as f:
            f.write(render_github_activity(stats, theme))
            
        with open(os.path.join(out_dir, f"rishvin-labs-{theme}.svg"), "w") as f:
            f.write(render_labs(theme))
            
        with open(os.path.join(out_dir, f"connect-{theme}.svg"), "w") as f:
            f.write(render_connect(theme))

if __name__ == "__main__":
    main()
