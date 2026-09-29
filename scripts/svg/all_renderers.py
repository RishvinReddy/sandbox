from .renderer import SVGRenderer

def render_hero(theme):
    w, h = 800, 260
    r = SVGRenderer(w, h, theme)
    r.add_rect(20, 20, w-40, h-40, fill=r.palette['card_bg'], stroke=r.palette['border'], rx=8)
    f_sans, f_mono = r.fonts['sans'], r.fonts['mono']
    
    r.add_text("RISHVIN REDDY", 60, 70, f_sans, 24, r.palette['text_primary'], "700", "1")
    r.add_text("Cybersecurity × Systems × IoT × Full-Stack", 60, 100, f_sans, 16, r.palette['text_secondary'])
    r.add_text("B.Tech CSE · Woxsen University · Class of 2028", 60, 140, f_sans, 14, r.palette['text_secondary'])
    r.add_text("Building secure, practical software systems.", 60, 165, f_sans, 14, r.palette['text_primary'])
    
    tags = ["Cybersec", "IoT", "Systems"]
    x = 60
    for tag in tags:
        bw = len(tag) * 8 + 24
        r.add_rect(x, 190, bw, 28, fill=r.palette['accent_dim'], rx=4)
        r.add_text(tag, x + 12, 209, f_mono, 12, r.palette['text_primary'])
        x += bw + 12
        
    r.add_text("Portfolio    LinkedIn    GitHub    Rishvin Labs", 60, 240, f_sans, 12, r.palette['text_secondary'])
    return r.render()

def render_currently_building(projects, theme):
    w, h = 800, max(140 + len(projects) * 60, 200)
    r = SVGRenderer(w, h, theme)
    r.add_rect(20, 20, w-40, h-40, fill=r.palette['card_bg'], stroke=r.palette['border'], rx=8)
    f_sans, f_mono = r.fonts['sans'], r.fonts['mono']
    
    r.add_text("CURRENTLY BUILDING", 60, 60, f_sans, 14, r.palette['text_primary'], "700", "1")
    r.add_text("Active engineering projects", 60, 80, f_sans, 12, r.palette['text_secondary'])
    r.add_line(20, 100, w-20, 100, r.palette['border'])
    
    y = 130
    for i, p in enumerate(projects, 1):
        r.add_text(f"{i:02d}", 60, y, f_mono, 14, r.palette['text_secondary'])
        r.add_text(p['title'], 100, y, f_sans, 16, r.palette['text_primary'], "700")
        r.add_rect(w - 120, y - 10, 8, 8, fill=r.palette['status_active'], rx=4)
        r.add_text("ACTIVE", w - 100, y, f_mono, 12, r.palette['text_primary'])
        r.add_text(p['description'], 100, y + 20, f_sans, 13, r.palette['text_secondary'])
        y += 60
    return r.render()

def render_flagships(projects, theme):
    h = 80 + len(projects) * 160
    r = SVGRenderer(800, h, theme)
    r.add_rect(20, 20, 760, h-40, fill=r.palette['card_bg'], stroke=r.palette['border'], rx=8)
    f_sans, f_mono = r.fonts['sans'], r.fonts['mono']
    
    r.add_text("FLAGSHIP SYSTEMS", 60, 60, f_sans, 14, r.palette['text_primary'], "700", "1")
    r.add_line(20, 80, 780, 80, r.palette['border'])
    
    y = 110
    for p in projects:
        r.add_text(p['title'].upper(), 60, y, f_sans, 16, r.palette['text_primary'], "700", "1")
        r.add_text(p['category'], 60, y+20, f_sans, 14, r.palette['text_secondary'])
        r.add_text(p['description'], 60, y+50, f_sans, 13, r.palette['text_primary'])
        
        # We simplify stack representation
        r.add_text("STACK: " + p.get('repo', ''), 60, y+80, f_mono, 12, r.palette['text_secondary'])
        
        # Arch
        arch = p.get('architecture', '').replace('\n', ' → ')
        if arch:
            r.add_text("ARCH: " + arch[:80], 60, y+100, f_mono, 12, r.palette['text_secondary'])
            
        r.add_text("GitHub →", 60, y+130, f_sans, 13, r.palette['text_primary'], "700")
        
        y += 160
        if y < h - 40:
            r.add_line(20, y - 20, 780, y - 20, r.palette['border'])
            
    return r.render()

def render_domains(theme):
    r = SVGRenderer(800, 240, theme)
    r.add_rect(20, 20, 760, 200, fill=r.palette['card_bg'], stroke=r.palette['border'], rx=8)
    f_sans = r.fonts['sans']
    
    r.add_text("ENGINEERING DOMAINS", 60, 60, f_sans, 14, r.palette['text_primary'], "700", "1")
    r.add_line(20, 80, 780, 80, r.palette['border'])
    
    # Left col
    r.add_text("CYBERSECURITY", 60, 110, f_sans, 13, r.palette['text_primary'], "700", "1")
    r.add_text("Security engineering", 60, 130, f_sans, 12, r.palette['text_secondary'])
    
    r.add_text("IoT", 60, 170, f_sans, 13, r.palette['text_primary'], "700", "1")
    r.add_text("Devices · MQTT", 60, 190, f_sans, 12, r.palette['text_secondary'])
    
    # Right col
    r.add_text("DIGITAL FORENSICS", 400, 110, f_sans, 13, r.palette['text_primary'], "700", "1")
    r.add_text("DFIR · Evidence · Analysis", 400, 130, f_sans, 12, r.palette['text_secondary'])
    
    r.add_text("BLOCKCHAIN", 400, 170, f_sans, 13, r.palette['text_primary'], "700", "1")
    r.add_text("Integrity · Smart Contracts", 400, 190, f_sans, 12, r.palette['text_secondary'])
    return r.render()

def render_stack(stack_dict, theme):
    h = 100 + len(stack_dict) * 50
    r = SVGRenderer(800, h, theme)
    r.add_rect(20, 20, 760, h-40, fill=r.palette['card_bg'], stroke=r.palette['border'], rx=8)
    f_sans, f_mono = r.fonts['sans'], r.fonts['mono']
    
    r.add_text("TECHNOLOGY STACK", 60, 60, f_sans, 14, r.palette['text_primary'], "700", "1")
    r.add_line(20, 80, 780, 80, r.palette['border'])
    
    y = 110
    for k, v in stack_dict.items():
        r.add_text(k.upper(), 60, y, f_sans, 12, r.palette['text_primary'], "700", "1")
        r.add_text("   ".join(v), 60, y+20, f_sans, 14, r.palette['text_secondary'])
        y += 50
    return r.render()

def render_activity(activities, date_str, theme):
    h = max(240, 120 + len(activities) * 40)
    r = SVGRenderer(800, h, theme)
    r.add_rect(20, 20, 760, h-40, fill=r.palette['card_bg'], stroke=r.palette['border'], rx=8)
    f_sans, f_mono = r.fonts['sans'], r.fonts['mono']
    
    r.add_text("LATEST ENGINEERING ACTIVITY", 60, 60, f_sans, 14, r.palette['text_primary'], "700", "1")
    r.add_line(20, 80, 780, 80, r.palette['border'])
    
    y = 110
    for act in activities:
        r.add_text(act['date'], 60, y, f_mono, 12, r.palette['text_secondary'])
        r.add_text(act['repo'], 140, y, f_sans, 14, r.palette['text_primary'], "700")
        r.add_text(act['desc'], 140, y+20, f_sans, 13, r.palette['text_secondary'])
        y += 40
        
    r.add_text(f"Last synchronized: {date_str}", 480, h-40, f_sans, 12, r.palette['text_secondary'])
    return r.render()

def render_experience(theme):
    r = SVGRenderer(800, 260, theme)
    r.add_rect(20, 20, 760, 220, fill=r.palette['card_bg'], stroke=r.palette['border'], rx=8)
    f_sans = r.fonts['sans']
    r.add_text("EXPERIENCE & DEVELOPMENT", 60, 60, f_sans, 14, r.palette['text_primary'], "700", "1")
    r.add_line(20, 80, 780, 80, r.palette['border'])
    
    r.add_text("PEGASYSTEMS", 60, 110, f_sans, 13, r.palette['text_primary'], "700", "1")
    r.add_text("Pega Platform Intern · 2026", 60, 130, f_sans, 12, r.palette['text_secondary'])
    
    r.add_text("DATALAKE SOLUTIONS", 60, 170, f_sans, 13, r.palette['text_primary'], "700", "1")
    r.add_text("Internship · 2026", 60, 190, f_sans, 12, r.palette['text_secondary'])
    
    r.add_text("ACADEMIC ENGINEERING", 400, 110, f_sans, 13, r.palette['text_primary'], "700", "1")
    r.add_text("B.Tech CSE · Woxsen University", 400, 130, f_sans, 12, r.palette['text_secondary'])
    r.add_text("2024–2028 · CGPA 9.01/10", 400, 150, f_sans, 12, r.palette['text_secondary'])
    
    return r.render()

def render_github_activity(stats, theme):
    r = SVGRenderer(800, 200, theme)
    r.add_rect(20, 20, 760, 160, fill=r.palette['card_bg'], stroke=r.palette['border'], rx=8)
    f_sans, f_mono = r.fonts['sans'], r.fonts['mono']
    
    r.add_text("GITHUB ACTIVITY", 60, 60, f_sans, 14, r.palette['text_primary'], "700", "1")
    r.add_line(20, 80, 780, 80, r.palette['border'])
    
    r.add_text(str(stats['repos']), 120, 120, f_sans, 24, r.palette['text_primary'], "700")
    r.add_text("Repositories", 100, 140, f_sans, 12, r.palette['text_secondary'])
    
    r.add_text("1,284", 360, 120, f_sans, 24, r.palette['text_primary'], "700")
    r.add_text("Contributions", 350, 140, f_sans, 12, r.palette['text_secondary'])
    
    r.add_text("12", 600, 120, f_sans, 24, r.palette['text_primary'], "700")
    r.add_text("Languages", 580, 140, f_sans, 12, r.palette['text_secondary'])
    return r.render()

def render_labs(theme):
    r = SVGRenderer(800, 240, theme)
    r.add_rect(20, 20, 760, 200, fill=r.palette['card_bg'], stroke=r.palette['border'], rx=8)
    f_sans, f_mono = r.fonts['sans'], r.fonts['mono']
    
    r.add_text("RISHVIN LABS", 60, 60, f_sans, 14, r.palette['text_primary'], "700", "1")
    r.add_text("Independent Engineering Lab", 200, 60, f_sans, 14, r.palette['text_secondary'])
    r.add_line(20, 80, 780, 80, r.palette['border'])
    
    r.add_text("Building and experimenting with systems across", 60, 110, f_sans, 14, r.palette['text_primary'])
    r.add_text("cybersecurity, infrastructure, developer tooling", 60, 130, f_sans, 14, r.palette['text_primary'])
    r.add_text("and applied software engineering.", 60, 150, f_sans, 14, r.palette['text_primary'])
    
    r.add_text("SECURITY    SYSTEMS    SOFTWARE    RESEARCH", 60, 190, f_sans, 12, r.palette['text_secondary'], "700", "1")
    r.add_text("rishvin-labs.vercel.app", 500, 190, f_mono, 12, r.palette['text_secondary'])
    return r.render()

def render_connect(theme):
    r = SVGRenderer(800, 180, theme)
    r.add_rect(20, 20, 760, 140, fill=r.palette['card_bg'], stroke=r.palette['border'], rx=8)
    f_sans, f_mono = r.fonts['sans'], r.fonts['mono']
    
    r.add_text("CONNECT", 60, 60, f_sans, 14, r.palette['text_primary'], "700", "1")
    r.add_line(20, 80, 780, 80, r.palette['border'])
    
    r.add_text("GitHub", 60, 110, f_sans, 14, r.palette['text_primary'], "700")
    r.add_text("github.com/RishvinReddy", 160, 110, f_mono, 13, r.palette['text_secondary'])
    
    r.add_text("LinkedIn", 60, 130, f_sans, 14, r.palette['text_primary'], "700")
    r.add_text("linkedin.com/in/rishvin-reddy", 160, 130, f_mono, 13, r.palette['text_secondary'])
    
    r.add_text("Portfolio", 460, 110, f_sans, 14, r.palette['text_primary'], "700")
    r.add_text("rishvinreddy.github.io", 540, 110, f_mono, 13, r.palette['text_secondary'])
    
    r.add_text("Labs", 460, 130, f_sans, 14, r.palette['text_primary'], "700")
    r.add_text("rishvin-labs.vercel.app", 540, 130, f_mono, 13, r.palette['text_secondary'])
    return r.render()
