import glob
import re

excluded = ["googlee546091a53d65633.html", "universe.html", "IDE.html", "index.html", "_footer.html", "_header.html"]

files = [f for f in glob.glob("*.html") if f not in excluded]

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # Check what kind of CTA exists
    if "ULTIMATE CTA" in content:
        cta_type = "ULTIMATE"
    elif "Pre-footer CTA Banner" in content:
        cta_type = "PRE-FOOTER V2"
    elif "Pre-Footer CTA" in content:
        cta_type = "PRE-FOOTER OLD"
    else:
        cta_type = "NONE"
        
    print(f"{f}: {cta_type}")

