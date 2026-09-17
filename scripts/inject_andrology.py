import re

def inject_content(target_file, content_file):
    with open(target_file, 'r', encoding='utf-8') as f:
        target_html = f.read()

    with open(content_file, 'r', encoding='utf-8') as f:
        new_content = f.read()

    # The marker before replacement
    prefix_marker = r'(<div id="menuOverlay"[^>]*></div>)'
    suffix_marker = r'(<!-- Footer -->)'
    
    # We want to replace everything between the prefix and suffix markers.
    pattern = re.compile(prefix_marker + r'.*?' + suffix_marker, re.DOTALL)
    
    # The replacement string needs to include the prefix and suffix.
    # Group 1 is prefix, Group 2 is suffix
    replacement = r'\1\n\n' + new_content.replace('\\', '\\\\') + r'\n\n    \2'
    
    updated_html = pattern.sub(replacement, target_html)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(updated_html)

inject_content('segment-andrology.html', 'andrology_content.html')
print("Injected content into segment-andrology.html")
