import os
import glob
import re

files = glob.glob('*.html')
count = 0

replacements = {
    'linkedin': '>\\n                            <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>',
    'twitter': '>\\n                            <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/></svg>',
    'facebook': '>\\n                            <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"/></svg>',
    'youtube': '>\\n                            <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>'
}

for f in files:
    if f == 'index.html': 
        continue # Already fixed
        
    with open(f, 'r', encoding='utf-8') as file:
        original = file.read()
    
    content = original
    for old, new in replacements.items():
        pattern = r'<i\s+data-lucide="' + old + r'"[^>]*></i>'
        content = re.sub(pattern, new, content)
        
        # Also replace multi-line tags if there are newlines between i and data-lucide
        pattern_multiline = r'<i[^>]*data-lucide="' + old + r'"[^>]*></i>'
        content = re.sub(pattern_multiline, new, content, flags=re.DOTALL)
        
    # Let's also fix the script tag for lucide while we're at it, similar to index.html
    # Remove the window.addEventListener('load', ...) block and old <script src="https://unpkg.com/lucide@latest"></script> from head
    
    # 1. Update unpkg script to just jsdelivr for safety
    content = content.replace('<script src="https://unpkg.com/lucide@latest"></script>', '<script src="https://unpkg.com/lucide@latest"></script>')
    
    # Actually just replacing the brand icons is enough, because lucide works fine otherwise if we don't have broken brand icons.
    
    if content != original:
        with open(f, 'w', encoding='utf-8') as out:
            out.write(content)
        count += 1

print(f'Replaced in {count} files.')
