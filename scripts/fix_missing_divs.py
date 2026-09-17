import os
import glob
import re

def main():
    html_files = glob.glob('*.html')
    
    # We want to replace:
    # </div>\s*<div id="menuOverlay"
    # with:
    # </div>\n        </div>\n    </div>\n    <div id="menuOverlay"
    
    # We should also make sure we only do it if the file actually has the mobileMenu structure
    # and isn't already closed correctly.
    
    pattern = re.compile(r'(<a href="contact\.html"[^>]*>.*?</a>\s*</div>)\s*<div id="menuOverlay"', re.DOTALL)
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if pattern.search(content):
            new_content = pattern.sub(r'\1\n        </div>\n    </div>\n    <div id="menuOverlay"', content)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {file}")
        else:
            print(f"Skipped {file} (pattern not found or already fixed)")

if __name__ == "__main__":
    main()
