import datetime

def generate_activity(repos, config):
    # Sort repos by updated_at
    sorted_repos = sorted(
        [r for r in repos if not r.get("private") and not r.get("fork")],
        key=lambda x: x.get("updated_at", ""),
        reverse=True
    )
    
    lines = []
    featured_repos = [p["repo"].lower() for p in config.get("featured", [])]
    count = 0
    
    for repo in sorted_repos:
        if count >= 3:
            break
        name = repo.get("name")
        desc = repo.get("description") or "Updated"
        if len(desc) > 50:
            desc = desc[:47] + "..."
            
        lines.append(f"**[{name}]({repo.get('html_url')})** — {desc}  ")
        count += 1
        
    date_str = datetime.datetime.now(datetime.timezone.utc).strftime("%d %b %Y")
    lines.append(f"  \n_Last synchronized: {date_str}_")
    
    return "\n".join(lines)
