def generate_currently_building(config):
    lines = [
        "| Project | Focus | Status |",
        "|---|---|---|"
    ]
    for proj in config.get("featured", []):
        url = f"https://github.com/RishvinReddy/{proj['repo']}"
        lines.append(f"| **[{proj['title']}]({url})** | {proj['category']} | {proj['status']} |")
    return "\n".join(lines)

def generate_flagship_projects(config):
    lines = []
    for i, proj in enumerate(config.get("featured", []), start=1):
        lines.append(f"### {i:02d} — {proj['title']}")
        lines.append(f"**{proj['category']}**\n")
        lines.append(f"{proj['description']}\n")
        
        # We can add badges, stats here in the future
        # lines.append(f"*Metrics*: ...\n")
        
        url = f"https://github.com/RishvinReddy/{proj['repo']}"
        lines.append(f"[Repository]({url})\n")
        
        if proj.get('architecture'):
            lines.append("<details>")
            lines.append("<summary><b>Architecture</b></summary>\n")
            lines.append("```text\n" + proj['architecture'] + "\n```")
            lines.append("</details>\n")
        
        lines.append("---\n")
    
    return "\n".join(lines).strip()
