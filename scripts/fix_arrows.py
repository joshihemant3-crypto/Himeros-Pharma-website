import os
import glob

files = glob.glob('*.html')
count = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We replace the specific stray ">" before the svg.
    # The exact string added was:
    # >\n                            <svg class="w-4 h-4 text-white"
    
    original = content
    content = content.replace('>\n                            <svg class="w-4 h-4 text-white"', '\n                            <svg class="w-4 h-4 text-white"')
    
    # Also in case there are carriage returns (\r\n)
    content = content.replace('>\r\n                            <svg class="w-4 h-4 text-white"', '\n                            <svg class="w-4 h-4 text-white"')
    
    if content != original:
        with open(f, 'w', encoding='utf-8') as out:
            out.write(content)
        count += 1

print(f'Fixed in {count} files.')
