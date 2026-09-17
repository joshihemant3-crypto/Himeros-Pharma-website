// Returns all stored submissions for the dashboard page.
// GET /api/submissions?key=YOUR_DASHBOARD_PASSWORD
// The password lives in the DASHBOARD_PASSWORD environment variable.
// Setup: docs/FORMS_SETUP.md

const { list } = require('@vercel/blob');

module.exports = async (req, res) => {
  const key = (req.query && req.query.key) || '';
  const expected = process.env.DASHBOARD_PASSWORD;

  if (!expected) {
    return res.status(501).json({ ok: false, error: 'DASHBOARD_PASSWORD is not set in Vercel project settings yet.' });
  }
  if (key !== expected) {
    return res.status(401).json({ ok: false, error: 'Wrong password.' });
  }
  if (!process.env.BLOB_READ_WRITE_TOKEN) {
    return res.status(501).json({ ok: false, error: 'Vercel Blob is not connected to this project yet.' });
  }

  try {
    const { blobs } = await list({ prefix: 'submissions/' });
    const records = await Promise.all(blobs.map(async (b) => {
      try {
        const r = await fetch(b.url);
        return r.ok ? await r.json() : null;
      } catch {
        return null;
      }
    }));
    const submissions = records.filter(Boolean).sort((a, b) => (a.ts < b.ts ? 1 : -1));
    return res.status(200).json({ ok: true, submissions });
  } catch (err) {
    return res.status(500).json({ ok: false, error: String(err) });
  }
};
