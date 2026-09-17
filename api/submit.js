// Receives form submissions from the website and stores each one as a JSON
// file in Vercel Blob. Read by /api/submissions for the dashboard page.
// Setup: docs/FORMS_SETUP.md (needs Vercel Blob connected to the project).

const { put } = require('@vercel/blob');

const FORM_TYPES = ['contact', 'enquiry', 'career'];

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    return res.status(405).json({ ok: false, error: 'POST only' });
  }

  try {
    const { form, data } = req.body || {};
    if (!FORM_TYPES.includes(form) || !data || typeof data !== 'object') {
      return res.status(400).json({ ok: false, error: 'Invalid payload' });
    }
    if (!process.env.BLOB_READ_WRITE_TOKEN) {
      // Storage not connected yet — forms still work via FormSubmit email.
      return res.status(200).json({ ok: false, error: 'storage not configured' });
    }

    const record = { form, ts: new Date().toISOString(), data };
    const pathname = `submissions/${form}/${Date.now()}-${Math.random().toString(36).slice(2, 8)}.json`;
    await put(pathname, JSON.stringify(record), {
      access: 'public', // URL is unguessable; the dashboard is password-gated
      contentType: 'application/json',
      addRandomSuffix: false
    });

    return res.status(200).json({ ok: true });
  } catch (err) {
    return res.status(500).json({ ok: false, error: String(err) });
  }
};
