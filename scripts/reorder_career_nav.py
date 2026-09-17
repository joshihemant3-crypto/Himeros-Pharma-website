"""
Reorder nav: move Career link to between Gallery and Contact Us.
Current:  ... Gallery | Contact Us | Career
Target:   ... Gallery | Career | Contact Us
"""

import os
import glob
import re

HTML_DIR = r"e:\himros web"
html_files = glob.glob(os.path.join(HTML_DIR, "*.html"))

def swap_career_before_contact(text):
    """
    In both desktop and mobile nav, move the Career <a> tag
    to appear before the Contact Us <a> tag.
    Works by finding the Contact Us block and the Career block,
    then placing Career right before Contact Us.
    """

    # --- DESKTOP nav ---
    # Find the Contact Us desktop link (may be multi-line)
    desktop_contact_pat = re.compile(
        r'(<a href="contact\.html"\s+class="nav-link[^"]*"[^>]*>Contact[\s\S]*?Us</a>)'
    )
    # Find the Career desktop link
    desktop_career_pat = re.compile(
        r'\n\s*<a href="career\.html" class="nav-link[^"]*">Career</a>'
    )

    career_desktop_match = desktop_career_pat.search(text)
    contact_desktop_match = desktop_contact_pat.search(text)

    if career_desktop_match and contact_desktop_match:
        career_str = career_desktop_match.group(0)
        # Remove career from current position
        text = text[:career_desktop_match.start()] + text[career_desktop_match.end():]
        # Re-find contact position after removal
        contact_desktop_match = desktop_contact_pat.search(text)
        if contact_desktop_match:
            insert_pos = contact_desktop_match.start()
            text = text[:insert_pos] + career_str + '\n' + text[insert_pos:]

    # --- MOBILE nav ---
    mobile_contact_pat = re.compile(
        r'(<a href="contact\.html"\s+class="mobile-nav-link[^"]*"[^>]*>Contact[\s\S]*?Us</a>)'
    )
    mobile_career_pat = re.compile(
        r'\n\s*<a href="career\.html" class="mobile-nav-link[^"]*">Career</a>'
    )

    career_mobile_match = mobile_career_pat.search(text)
    contact_mobile_match = mobile_contact_pat.search(text)

    if career_mobile_match and contact_mobile_match:
        career_str = career_mobile_match.group(0)
        text = text[:career_mobile_match.start()] + text[career_mobile_match.end():]
        contact_mobile_match = mobile_contact_pat.search(text)
        if contact_mobile_match:
            insert_pos = contact_mobile_match.start()
            text = text[:insert_pos] + career_str + '\n' + text[insert_pos:]

    # --- FOOTER ---
    footer_contact_pat = re.compile(
        r'(<li><a href="contact\.html" class="text-gray-400 text-sm[^"]*">Contact Us</a></li>)'
    )
    footer_career_pat = re.compile(
        r'\n\s*<li><a href="career\.html" class="text-gray-400 text-sm[^"]*">Career</a></li>'
    )

    career_footer_match = footer_career_pat.search(text)
    contact_footer_match = footer_contact_pat.search(text)

    if career_footer_match and contact_footer_match:
        career_str = career_footer_match.group(0)
        text = text[:career_footer_match.start()] + text[career_footer_match.end():]
        contact_footer_match = footer_contact_pat.search(text)
        if contact_footer_match:
            insert_pos = contact_footer_match.start()
            text = text[:insert_pos] + career_str + '\n' + text[insert_pos:]

    return text


updated = 0
skipped = 0

for filepath in sorted(html_files):
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    if 'href="career.html"' not in content:
        print(f"  SKIP (no career link): {filename}")
        skipped += 1
        continue

    new_content = swap_career_before_contact(content)

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  UPDATED: {filename}")
        updated += 1
    else:
        print(f"  NO CHANGE: {filename}")
        skipped += 1

print(f"\nDone! Updated: {updated}, No-change/Skipped: {skipped}")
