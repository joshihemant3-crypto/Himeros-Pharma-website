"""
Migrate assets: items/ + Gallery/ -> assets/ tree with normalized kebab-case names,
and rewrite every reference in all *.html and scripts/*.py (except this script).

Buckets:
  assets/brand/    logos + corporate identity images
  assets/segments/ segment imagery (andrology, gynecology, ...)
  assets/products/ product shots (referenced by product pages or *_nobg variants)
  assets/blog/     blog article images
  assets/events/   event cover images
  assets/pages/    other page imagery (about, books, career, ...)
  assets/gallery/  the Gallery/ photo tree (folders kept as-is)
  assets/sources/  unreferenced original/source images
  docs/            source documents (*.docx)

Dry-run by default. Execute with:  python scripts/migrate_assets.py --apply

References are found by searching for each file's literal path (and its
URL-encoded variant), so filenames containing spaces, apostrophes or commas
are handled exactly.
"""

import os
import re
import sys
import glob
import shutil
import hashlib
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
APPLY = '--apply' in sys.argv

# Typo corrections verified against product page <title>s on 2026-09-16.
# Keys are lowercase base names without extension and without the _nobg suffix.
BASE_OVERRIDES = {
    'durahaim 60': 'durahim 60',
    'eractlong': 'erectlong',
    'embroyshield': 'embryoshield',
    'himrect gel': 'himract gel',
    'hiimeros pharma white logo': 'himeros white logo',
    'aplha-kd': 'alpha-kd',
    'aplha-kd ds': 'alpha-kd ds',
    'hitam-d': 'himtam-d',
    "tadox-2'5": 'tadox-2.5',
    'tadox 2.25': 'tadox 2.5',
    'foligaurd': 'foliguard',
    'himdrol': 'himdriol',
    'libart caupsule': 'librt capsule',
    'prodky45': 'prokd-45',
    'pro-kd45': 'prokd-45',
    'pro-kd15': 'prokd-15',
    'himeract pro': 'himract pro',
}

SEGMENT_NAMES = {'andrology', 'gynecology', 'nephrology', 'sexology'}
PAGE_PREFIXES = ('about', 'books', 'career', 'contact', 'index', 'andrology_content')


def kebab(filename):
    base, ext = os.path.splitext(filename)
    b = base.strip().lower()
    suffix = ''
    m = re.match(r'^(.*)_nobg$', b)
    if m:
        b, suffix = m.group(1), '_nobg'
    b = BASE_OVERRIDES.get(b, b)
    b = re.sub(r'[^a-z0-9.]+', '-', b)
    b = re.sub(r'-{2,}', '-', b).strip('-')
    return b + suffix + ext.lower()


def classify(name, referrers):
    n = name.lower()
    base = os.path.splitext(n)[0]
    referrers = referrers or []
    if 'logo' in n or n in ('himeros pharma for website.png',
                            'advanced therapeutic innovation.jpg'):
        return 'brand'
    if base in SEGMENT_NAMES or any(r.startswith('segment') for r in referrers):
        return 'segments'
    if any(r.startswith('blog') for r in referrers):
        return 'blog'
    if any(re.match(r'event-|^gallery', r) for r in referrers) or 'cover' in n or '_gallery' in n:
        return 'events'
    if 'book' in n or 'clinical' in n:
        return 'pages'
    if any(r.startswith('product') for r in referrers) or '_nobg' in n:
        return 'products'
    if any(r.startswith(PAGE_PREFIXES) for r in referrers):
        return 'pages'
    if n.endswith('.docx'):
        return 'DOCS'
    return 'sources'


def md5(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


# ---------- collect files ----------
items_files = []
for dirpath, dirnames, filenames in os.walk('items'):
    for fn in filenames:
        items_files.append(os.path.join(dirpath, fn).replace('\\', '/'))
items_files.sort()

# ---------- scan references (literal path + URL-encoded variant) ----------
targets = sorted(glob.glob('*.html'))
script_targets = [p for p in sorted(glob.glob('scripts/*.py'))
                  if os.path.basename(p) != 'migrate_assets.py']
scan_targets = targets + script_targets

contents = {}
for t in scan_targets:
    try:
        contents[t] = open(t, encoding='utf-8', newline='').read()
    except (UnicodeDecodeError, OSError) as e:
        print(f'WARN: cannot read {t}: {e}')

referrers = {}   # items path -> set of files referencing it (literal or encoded)
for old in items_files:
    enc = quote(old)
    for t, c in contents.items():
        if old in c or enc in c:
            referrers.setdefault(old, set()).add(os.path.basename(t))

# ---------- build move plan ----------
plan = []  # (old, newpath, bucket)
for old in items_files:
    name = os.path.basename(old)
    bucket = classify(name, sorted(referrers.get(old, set())))
    if bucket == 'DOCS':
        newpath = 'docs/' + name
    else:
        newpath = f'assets/{bucket}/' + kebab(name)
    plan.append((old, newpath, bucket))

plan.sort(key=lambda x: (x[1], x[0]))
moves = {}       # old -> newpath (or None for dropped duplicates)
ref_target = {}  # old -> newpath used for rewriting refs (deduped -> keeper)
dedupes = []
seen = {}
for old, newpath, bucket in plan:
    if newpath in seen:
        kept = seen[newpath]
        if md5(old) == md5(kept):
            dedupes.append((old, kept))
            moves[old] = None
            ref_target[old] = ref_target[kept]
        else:
            base, ext = os.path.splitext(newpath)
            i = 2
            while f'{base}-{i}{ext}' in seen:
                i += 1
            newpath = f'{base}-{i}{ext}'
            seen[newpath] = old
            moves[old] = ref_target[old] = newpath
    else:
        seen[newpath] = old
        moves[old] = ref_target[old] = newpath

# ---------- report ----------
print('=== CLASSIFICATION ===')
by_bucket = {}
for old, newpath, bucket in plan:
    by_bucket.setdefault(bucket, []).append(old)
for b in sorted(by_bucket):
    print(f'  {b:10s} {len(by_bucket[b]):3d} files')

print('\n=== RENAMES (name changed) ===')
for old, newpath in sorted(moves.items()):
    if newpath and os.path.basename(old) != os.path.basename(newpath):
        print(f'  {os.path.basename(old):55s} -> {newpath}')

print('\n=== DEDUPES (identical content, dropped) ===')
for dup, kept in dedupes:
    print(f'  {dup}  ==  {kept}')

print('\n=== REFERENCED FROM NON-canonical PATH OR ENCODED FORM ===')
for old, refs in sorted(referrers.items()):
    if old.startswith('items/items/'):
        print(f'  {old}  <-  referenced in {sorted(refs)} (repairs broken ref)')

unref = [old for old in items_files if old not in referrers and moves.get(old) is None]
print(f'\nTotals: {len(items_files)} items files, {len(dedupes)} deduped, '
      f'{len(moves) - len(dedupes)} moved, {len(unref)} unreferenced (kept in sources/ or docs/)')

if not APPLY:
    print('\nDRY RUN ONLY. Re-run with --apply to execute.')
    sys.exit(0)

# ---------- apply ----------
for d in ['brand', 'segments', 'products', 'blog', 'events', 'pages', 'sources']:
    os.makedirs(f'assets/{d}', exist_ok=True)
os.makedirs('docs', exist_ok=True)

moved, dropped = 0, 0
for old, newpath in sorted(moves.items()):
    if newpath is None:
        os.remove(old)
        dropped += 1
    else:
        shutil.move(old, newpath)
        moved += 1

shutil.move('Gallery', 'assets/gallery')

for dirpath, dirnames, filenames in os.walk('items', topdown=False):
    for d in dirnames:
        p = os.path.join(dirpath, d)
        if not os.listdir(p):
            os.rmdir(p)
if os.path.exists('items') and not os.listdir('items'):
    os.rmdir('items')

# ---------- rewrite references ----------
replacements = []
for old in items_files:
    new = ref_target[old]
    replacements.append((old, new))
    enc = quote(old)
    if enc != old:
        replacements.append((enc, new))
replacements.sort(key=lambda p: len(p[0]), reverse=True)

changed_files, total_subs = 0, 0
for t in scan_targets:
    content = contents[t]
    orig = content
    n = 0
    for old_s, new_s in replacements:
        if old_s in content:
            n += content.count(old_s)
            content = content.replace(old_s, new_s)
    content = re.sub(r'(["\'])Gallery/', r'\1assets/gallery/', content)
    if content != orig:
        with open(t, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        changed_files += 1
        total_subs += n
print(f'\nApplied: {moved} files moved, {dropped} duplicates dropped, '
      f'{changed_files} files rewritten ({total_subs} reference substitutions).')

# ---------- verify ----------
problems = 0
for t in sorted(glob.glob('*.html')):
    content = open(t, encoding='utf-8', errors='ignore').read()
    if 'items/' in content:
        idx = content.find('items/')
        problems += 1
        print(f'VERIFY FAIL: {t} still has items/ ref near: {content[max(0,idx-30):idx+50]!r}')
    if re.search(r'["\']Gallery/', content):
        problems += 1
        print(f'VERIFY FAIL: {t} still has a Gallery/ ref')
    for m in re.findall(r'(?:src|href)="([^"]+)"', content):
        if m.startswith(('http', 'mailto:', 'tel:', '#', 'data:')) or m == '':
            continue
        local = os.path.normpath(m.split('#')[0].split('?')[0])
        if not os.path.exists(local):
            problems += 1
            print(f'VERIFY FAIL: {t} -> missing target {m}')

for t in script_targets:
    content = open(t, encoding='utf-8', errors='ignore').read()
    if 'items/' in content:
        print(f'NOTE: {t} still mentions items/ (template placeholder or docs path)')

print('VERIFY: all clean' if problems == 0 else f'VERIFY: {problems} problems found')
