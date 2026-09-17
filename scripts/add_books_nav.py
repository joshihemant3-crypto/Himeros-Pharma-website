import os, re, glob

html_files = glob.glob("e:\\himros web\\*.html")

desktop_old = '<a href="blog.html" class="nav-link relative text-sm font-medium text-gray-700 hover:text-brand-600 transition-colors">Blog</a>'
desktop_new = '<a href="blog.html" class="nav-link relative text-sm font-medium text-gray-700 hover:text-brand-600 transition-colors">Blog</a>\n                    <a href="books.html" class="nav-link relative text-sm font-medium text-gray-700 hover:text-brand-600 transition-colors">Books</a>'

mobile_old = 'class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-brand-50 hover:text-brand-600 rounded-lg transition-colors font-medium">Blog</a>'
mobile_new = 'class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-brand-50 hover:text-brand-600 rounded-lg transition-colors font-medium">Blog</a>\n                <a href="books.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-brand-50 hover:text-brand-600 rounded-lg transition-colors font-medium">Books</a>'

updated = 0
skipped = 0

for filepath in html_files:
    basename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "books.html" in content:
        print(f"SKIP (already has books link): {basename}")
        skipped += 1
        continue

    new_content = content.replace(desktop_old, desktop_new)
    new_content = new_content.replace(mobile_old, mobile_new)

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated: {basename}")
        updated += 1
    else:
        print(f"No match: {basename}")

print(f"\nDone. Updated: {updated}, Skipped: {skipped}")
