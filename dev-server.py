"""Local dev server with proper cache headers (replaces `python -m http.server`).

python -m http.server sends no Cache-Control, so browsers heuristically cache
HTML and show stale pages after edits (e.g. an old gallery thumbnail).
This server sends `Cache-Control: no-store` for HTML and short-lived caching
for static assets, so page edits always show up on a normal reload.

Run:  python dev-server.py  →  http://localhost:8000
"""
import http.server
import os
import re

PORT = 8000
ROOT = os.path.dirname(os.path.abspath(__file__))

MIME = {
    '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript',
    '.json': 'application/json', '.png': 'image/png', '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg', '.gif': 'image/gif', '.svg': 'image/svg+xml',
    '.webp': 'image/webp', '.ico': 'image/x-icon', '.pdf': 'application/pdf',
    '.mp4': 'video/mp4', '.webm': 'video/webm', '.docx':
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    '.woff': 'font/woff', '.woff2': 'font/woff2'
}


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def guess_type(self, path):
        ext = os.path.splitext(str(path))[1].lower()
        return MIME.get(ext) or super().guess_type(path)

    def end_headers(self):
        path = self.path.split('?')[0]
        if re.search(r'\.html?$', path, re.I) or path in ('/', ''):
            self.send_header('Cache-Control', 'no-store')
        else:
            self.send_header('Cache-Control', 'public, max-age=300')
        super().end_headers()


if __name__ == '__main__':
    server = http.server.ThreadingHTTPServer(('0.0.0.0', PORT), Handler)
    print(f'Serving {ROOT} at http://localhost:{PORT} (no-store for HTML)')
    server.serve_forever()
