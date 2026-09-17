# NOTE: written for the pre-restructure layout (items/ + Gallery/ at repo root, pre 2026-09-16).
# Do not re-run as-is: it would inject broken image paths. Layout is now assets/ + docs/.
import re
import os

def process_file(filepath, img_src):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to find everything from <!-- Breadcrumb --> to just before <!-- Footer -->
    pattern = re.compile(r'<!-- Breadcrumb -->.*?<!-- Footer -->', re.DOTALL)
    
    replacement = f'''<!-- Image Only -->
    <section class="bg-white">
        <img src="items/{img_src}" alt="{img_src.split('.')[0].capitalize()}" class="w-full object-cover">
    </section>

    <!-- Footer -->'''
    
    new_content = pattern.sub(replacement, content)
    
    # For sexology, handle the fact that Breadcrumb might already be replaced.
    if '<!-- Breadcrumb -->' not in content:
        # sexology case where it's <!-- Image Only --> ... <!-- Footer -->
        pattern2 = re.compile(r'<!-- Hero -->.*?<!-- Footer -->', re.DOTALL)
        new_content = pattern2.sub('<!-- Footer -->', new_content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

process_file('segment-sexology.html', 'sexology.png')
process_file('segment-nephrology.html', 'nephrology.jpg')
process_file('segment-gynecology.html', 'gynecology.jpg')
print('Done processing all three files.')
