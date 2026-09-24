// Local development server — full site + working dashboard API on localhost.
// Mirrors the Vercel functions in api/ so the dashboard works locally.
//
// One-time: add these two lines to .env.local (values from your Vercel dashboard):
//   BLOB_READ_WRITE_TOKEN=...   (Blob store page → "Environment Variables")
//   DASHBOARD_PASSWORD=...      (Settings → Environment Variables)
//
// Run:  node local-server.js   →  http://localhost:3000
//
// Submissions made locally go into the SAME store as production, so they
// appear on the live dashboard too.

const http = require('http');
const fs = require('fs');
const path = require('path');
const { put, list } = require('@vercel/blob');

// Load .env.local into process.env (no dependency needed)
const envFile = path.join(__dirname, '.env.local');
if (fs.existsSync(envFile)) {
  for (const line of fs.readFileSync(envFile, 'utf8').split('\n')) {
    const m = line.match(/^\s*([A-Za-z0-9_]+)\s*=\s*(.*)\s*$/);
    if (m && process.env[m[1]] === undefined) {
      process.env[m[1]] = m[2].replace(/^["']|["']$/g, '');
    }
  }
}

const PORT = process.env.PORT || 3000;
const ROOT = __dirname;
const FORM_TYPES = ['contact', 'enquiry', 'career'];

const MIME = {
  '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript',
  '.json': 'application/json', '.png': 'image/png', '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg', '.gif': 'image/gif', '.svg': 'image/svg+xml',
  '.webp': 'image/webp', '.ico': 'image/x-icon', '.pdf': 'application/pdf',
  '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  '.woff': 'font/woff', '.woff2': 'font/woff2'
};

function json(res, status, obj) {
  res.writeHead(status, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify(obj));
}

async function handleApi(req, res, url) {
  if (url.pathname === '/api/submit' && req.method === 'POST') {
    let body = '';
    req.on('data', (c) => { body += c; });
    req.on('end', async () => {
      try {
        const { form, data } = JSON.parse(body || '{}');
        if (!FORM_TYPES.includes(form) || !data || typeof data !== 'object') {
          return json(res, 400, { ok: false, error: 'Invalid payload' });
        }
        if (!process.env.BLOB_READ_WRITE_TOKEN) {
          return json(res, 200, { ok: false, error: 'BLOB_READ_WRITE_TOKEN missing in .env.local' });
        }
        const pathname = `submissions/${form}/${Date.now()}-${Math.random().toString(36).slice(2, 8)}.json`;
        await put(pathname, JSON.stringify({ form, ts: new Date().toISOString(), data }), {
          access: 'public', contentType: 'application/json', addRandomSuffix: false
        });
        json(res, 200, { ok: true });
      } catch (err) {
        json(res, 500, { ok: false, error: String(err) });
      }
    });
    return true;
  }

  if (url.pathname === '/api/submissions' && req.method === 'GET') {
    const key = url.searchParams.get('key') || '';
    if (!process.env.DASHBOARD_PASSWORD) {
      return json(res, 501, { ok: false, error: 'DASHBOARD_PASSWORD missing in .env.local' });
    }
    if (key !== process.env.DASHBOARD_PASSWORD) {
      return json(res, 401, { ok: false, error: 'Wrong password.' });
    }
    if (!process.env.BLOB_READ_WRITE_TOKEN) {
      return json(res, 501, { ok: false, error: 'BLOB_READ_WRITE_TOKEN missing in .env.local' });
    }
    try {
      const { blobs } = await list({ prefix: 'submissions/' });
      const records = await Promise.all(blobs.map(async (b) => {
        try {
          const r = await fetch(b.url);
          return r.ok ? await r.json() : null;
        } catch { return null; }
      }));
      json(res, 200, { ok: true, submissions: records.filter(Boolean).sort((a, b) => (a.ts < b.ts ? 1 : -1)) });
    } catch (err) {
      json(res, 500, { ok: false, error: String(err) });
    }
    return true;
  }
  return false;
}

function serveStatic(res, url) {
  let p = decodeURIComponent(url.pathname);
  if (p.endsWith('/')) p += 'index.html';
  const file = path.normalize(path.join(ROOT, p));
  if (!file.startsWith(ROOT)) { res.writeHead(403); return res.end('Forbidden'); }
  fs.readFile(file, (err, buf) => {
    if (err) { res.writeHead(404, { 'Content-Type': 'text/plain' }); return res.end('404 Not Found'); }
    res.writeHead(200, { 'Content-Type': MIME[path.extname(file).toLowerCase()] || 'application/octet-stream' });
    res.end(buf);
  });
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url, `http://localhost:${PORT}`);
  Promise.resolve(handleApi(req, res, url)).then((handled) => {
    if (!handled) serveStatic(res, url);
  }).catch((err) => json(res, 500, { ok: false, error: String(err) }));
});

server.listen(PORT, () => {
  const hasToken = !!process.env.BLOB_READ_WRITE_TOKEN;
  const hasPass = !!process.env.DASHBOARD_PASSWORD;
  console.log(`Site:        http://localhost:${PORT}`);
  console.log(`Dashboard:   http://localhost:${PORT}/dashboard.html`);
  console.log(`Blob token:  ${hasToken ? 'found' : 'MISSING — add BLOB_READ_WRITE_TOKEN to .env.local'}`);
  console.log(`Password:    ${hasPass ? 'found' : 'MISSING — add DASHBOARD_PASSWORD to .env.local'}`);
});
