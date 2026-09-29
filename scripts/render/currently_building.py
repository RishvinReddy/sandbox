from svg.renderer import SVGRenderer

def render_currently_building(projects, theme="light"):
    width = 800
    height = max(140 + len(projects) * 60, 200)
    renderer = SVGRenderer(width, height, theme)
    
    renderer.add_rect(20, 20, width-40, height-40, fill=renderer.palette['card_bg'], stroke=renderer.palette['border'], rx=8)
    
    font_sans = renderer.fonts['sans']
    font_mono = renderer.fonts['mono']
    
    renderer.add_text("CURRENTLY BUILDING", 60, 60, font_sans, 14, renderer.palette['text_primary'], font_weight="bold", letter_spacing="1")
    renderer.add_text("Active engineering projects", 60, 80, font_sans, 12, renderer.palette['text_secondary'])
    
    renderer.add_line(20, 100, width-20, 100, renderer.palette['border'])
    
    y = 130
    for i, proj in enumerate(projects, 1):
        renderer.add_text(f"{i:02d}", 60, y, font_mono, 14, renderer.palette['text_secondary'])
        renderer.add_text(proj['title'], 100, y, font_sans, 16, renderer.palette['text_primary'], font_weight="bold")
        
        # Status active dot
        renderer.add_rect(width - 120, y - 10, 8, 8, fill=renderer.palette['status_active'], rx=4)
        renderer.add_text("ACTIVE", width - 100, y, font_mono, 12, renderer.palette['text_primary'])
        
        renderer.add_text(proj['description'], 100, y + 20, font_sans, 13, renderer.palette['text_secondary'])
        y += 60
        
    return renderer.render()
