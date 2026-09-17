import glob

files = glob.glob('*.html')
count = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    original = content
    # Look for the exact broken string and fix it
    broken = 'transition-colors"\n                            <svg'
    broken2 = 'transition-colors"\r\n                            <svg'
    
    fixed = 'transition-colors">\n                            <svg'
    
    content = content.replace(broken, fixed).replace(broken2, fixed)
    
    # Also clean up duplicate > if any exist: transition-colors">>\n -> transition-colors">\n
    content = content.replace('transition-colors">>\n', 'transition-colors">\n')
    content = content.replace('transition-colors">>\r\n', 'transition-colors">\n')
    
    if content != original:
        with open(f, 'w', encoding='utf-8') as out:
            out.write(content)
        count += 1

print(f'Fixed missing > in {count} files.')
