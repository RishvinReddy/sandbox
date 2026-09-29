def generate_tech_stack(repos, config):
    allowlist = set([lang.lower() for lang in config.get("tech_stack_allowlist", [])])
    
    languages = set()
    for repo in repos:
        lang = repo.get("language")
        if lang and lang.lower() in allowlist:
            languages.add(lang)
            
    # For now, we can categorize them static or just output the allowed ones we found.
    # To keep it simple but accurate to the user's request:
    
    # Pre-defined categories for known allowed tools
    categories = {
        "Languages": ["TypeScript", "JavaScript", "Python", "C++", "C", "SQL", "Solidity", "Java"],
        "Frontend": ["React", "Next.js", "Tailwind CSS"],
        "Backend": ["Node.js", "PostgreSQL", "Supabase", "SQLite", "Redis", "IPFS"],
        "Security / Systems": ["DFIR", "IoT", "MQTT", "Blockchain", "Electron"],
        "Infrastructure": ["Docker", "GitHub Actions", "AWS", "Vercel"]
    }
    
    lines = []
    
    for cat, items in categories.items():
        # filter items to only those in the allowlist
        valid_items = [item for item in items if item.lower() in allowlist]
        if valid_items:
            lines.append(f"**{cat}**: " + ", ".join(valid_items) + "  ")
            
    return "\n".join(lines).strip()
