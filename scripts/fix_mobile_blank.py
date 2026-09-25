"""
Fix the mobile blank-page bug: page content and the white transition overlay
relied on CSS animations to become visible. Phones that disable/freeze CSS
animations (Android "Remove animations", some battery savers, tab-restore)
were left with a fullscreen white overlay (opacity 1, z-index 9999) and/or
content stuck at opacity 0.

Changes per page:
  1. Transition overlay: base opacity 1 -> 0, CSS animation -> simple transition.
     (JS still fades it in when navigating; pageshow resets it.)
  2. Remove the body-content fade rule + its keyframes entirely (no hidden state).
Dry-run default; --apply to execute.
"""
import re
import sys
import glob

APPLY = '--apply' in sys.argv
changed = []

for f in sorted(glob.glob('*.html')):
    c = open(f, encoding='utf-8', newline='').read()
    orig = c

    # 1) Overlay: opacity 1 + animation -> opacity 0 + transition
    c = re.sub(
        r'(\n\s*)opacity: 1;(\n\s*)animation: overlayFadeOut[^;]*;',
        r'\1opacity: 0;\2transition: opacity 0.25s ease;',
        c)
    # single-line variant:  background: #ffffff; opacity: 1; \n animation: overlayFadeOut...;
    c = re.sub(
        r'(background: #ffffff; opacity:) 1;(\s*)animation: overlayFadeOut[^;]*;',
        r'\1 0;\2transition: opacity 0.25s ease;',
        c)

    # 2) Drop the overlayFadeOut keyframes (any formatting, one nesting level)
    c = re.sub(r'@keyframes overlayFadeOut\s*\{(?:[^{}]|\{[^{}]*\})*\}\s*', '', c)

    # 3) Remove the body-content fade rule (selector has no braces inside)
    c = re.sub(r'body > \*:not\(\.page-transition-overlay\)[^\{]*\{[^}]*\}\s*', '', c)

    # 4) Drop the contentFadeIn keyframes
    c = re.sub(r'@keyframes contentFadeIn\s*\{(?:[^{}]|\{[^{}]*\})*\}\s*', '', c)

    # tidy: collapse 3+ blank lines left by removals
    c = re.sub(r'\n{4,}', '\n\n\n', c)

    if c != orig:
        if APPLY:
            open(f, 'w', encoding='utf-8', newline='').write(c)
        changed.append(f)

print(('APPLIED to ' if APPLY else 'WOULD fix ') + str(len(changed)) + ' pages:')
for f in changed:
    print(' ', f)

if not APPLY:
    print('\nDRY RUN — re-run with --apply')
