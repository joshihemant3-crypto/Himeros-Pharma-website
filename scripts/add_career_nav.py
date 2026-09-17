"""
Script to add Career nav link to all HTML files in the project.
Handles both single-line and multi-line Contact Us patterns.
"""

import os
import glob
import re

HTML_DIR = r"e:\himros web"
html_files = glob.glob(os.path.join(HTML_DIR, "*.html"))

CAREER_DESKTOP = '                    <a href="career.html" class="nav-link relative text-sm font-medium text-gray-700 hover:text-brand-600 transition-colors">Career</a>'
CAREER_MOBILE  = '                <a href="career.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-brand-50 hover:text-brand-600 rounded-lg transition-colors font-medium">Career</a>'
CAREER_FOOTER  = '                        <li><a href="career.html" class="text-gray-400 text-sm hover:text-green-400 transition-colors">Career</a></li>'

updated = 0
skipped = 0

for filepath in sorted(html_files):
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    if 'href="career.html"' in content:
        print(f"  SKIP (already has career): {filename}")
        skipped += 1
        continue

    new_content = content
    changed = False

    # --- Desktop nav: handle both single-line and multi-line Contact Us ---
    # Pattern: <a href="contact.html" class="nav-link ...">Contact Us</a>  (single line)
    def insert_after_desktop(text):
        pattern = r'(<a href="contact\.html"\s+class="nav-link[^"]*"[^>]*>Contact[\s\S]*?Us</a>)'
        match = re.search(pattern, text)
        if match:
            end = match.end()
            return text[:end] + '\n' + CAREER_DESKTOP + text[end:], True
        return text, False

    # --- Mobile nav: handle both single-line and multi-line Contact Us ---
    def insert_after_mobile(text):
        pattern = r'(<a href="contact\.html"\s+class="mobile-nav-link[^"]*"[^>]*>Contact[\s\S]*?Us</a>)'
        match = re.search(pattern, text)
        if match:
            end = match.end()
            return text[:end] + '\n' + CAREER_MOBILE + text[end:], True
        return text, False

    # --- Footer: ---
    def insert_after_footer(text):
        pattern = r'(<a href="contact\.html"\s+class="text-gray-400 text-sm[^"]*"[^>]*>Contact Us</a></li>)'
        match = re.search(pattern, text)
        if match:
            end = match.end()
            return text[:end] + '\n' + CAREER_FOOTER + text[end:], True
        return text, False

    new_content, ch1 = insert_after_desktop(new_content)
    new_content, ch2 = insert_after_mobile(new_content)
    new_content, ch3 = insert_after_footer(new_content)
    changed = ch1 or ch2 or ch3

    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  UPDATED: {filename} (desktop={ch1}, mobile={ch2}, footer={ch3})")
        updated += 1
    else:
        print(f"  NO MATCH: {filename}")
        skipped += 1

print(f"\nDone! Updated: {updated}, Skipped/No-match: {skipped}")
