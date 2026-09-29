from svg.renderer import SVGRenderer

def render_hero(theme="light"):
    # Target structure:
    # 800x300 viewBox
    width = 800
    height = 260
    renderer = SVGRenderer(width, height, theme)
    
    # Outer box
    renderer.add_rect(20, 20, width-40, height-40, fill=renderer.palette['card_bg'], stroke=renderer.palette['border'], rx=8)
    
    # Text content
    font_sans = renderer.fonts['sans']
    font_mono = renderer.fonts['mono']
    
    renderer.add_text("RISHVIN REDDY", 60, 70, font_sans, 24, renderer.palette['text_primary'], font_weight="700", letter_spacing="1")
    renderer.add_text("Cybersecurity × Systems × IoT × Full-Stack", 60, 100, font_sans, 16, renderer.palette['text_secondary'])
    
    renderer.add_text("B.Tech CSE · Woxsen University · Class of 2028", 60, 140, font_sans, 14, renderer.palette['text_secondary'])
    renderer.add_text("Building secure, practical software systems.", 60, 165, font_sans, 14, renderer.palette['text_primary'])
    
    # Tags
    tags = ["Cybersec", "IoT", "Systems"]
    x = 60
    for tag in tags:
        # Box width approx based on text length
        box_w = len(tag) * 8 + 24
        renderer.add_rect(x, 190, box_w, 28, fill=renderer.palette['accent_dim'], stroke="none", rx=4)
        renderer.add_text(tag, x + 12, 209, font_mono, 12, renderer.palette['text_primary'])
        x += box_w + 12
        
    return renderer.render()
