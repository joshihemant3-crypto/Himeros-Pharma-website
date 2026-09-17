import glob, os, re

os.chdir(r'E:\himros web')

# Files that still have barUp keyframes or .leaving .bar rules
files = ['about.html', 'awards.html', 'blog.html', 'contact.html', 'index.html', 'products.html', 'segment.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    modified = False
    
    # Remove @keyframes barUp block (any format)
    content = re.sub(
        r'        @keyframes barUp \{[^}]*0%[^}]*100%[^}]*\}',
        '', content, flags=re.DOTALL
    )
    if 'barUp' not in content and 'barUp' not in content:
        pass  # This check doesn't help; let's just track modifications differently
    
    # Remove .leaving .bar block (expanded format with indentation)
    old = '        .page-transition-overlay.leaving .bar {\n            transform: translateY(-100%);\n            animation: barUp 0.5s cubic-bezier(0.4, 0, 0.2, 1) forwards;\n            animation-delay: 0s !important;\n        }\n        \n'
    if old in content:
        content = content.replace(old, '')
        modified = True
    
    old2 = '        .page-transition-overlay.leaving .bar {\n            transform: translateY(-100%);\n            animation: barUp 0.5s cubic-bezier(0.4, 0, 0.2, 1) forwards;\n            animation-delay: 0s !important;\n        }\n'
    if old2 in content:
        content = content.replace(old2, '')
        modified = True
    
    # For homepage: different indentation
    old3 = '        .page-transition-overlay.leaving .bar {\n            transform: translateY(-100%);\n            animation: barUp 0.5s cubic-bezier(0.4, 0, 0.2, 1) forwards;\n            animation-delay: 0s !important;\n        }\n\n        \n\n'
    if old3 in content:
        content = content.replace(old3, '')
        modified = True
    
    # Clean up blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    if modified:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        print(f'Fixed: {f}')

# Check final state
print()
for f in sorted(glob.glob('*.html')):
    with open(f) as fh:
        content = fh.read()
    has = 'barUp' in content or 'leaving .bar' in content
    if has:
        print(f'STILL HAS: {f}')
print('Done.')
