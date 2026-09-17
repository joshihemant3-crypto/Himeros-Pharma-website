# Forms + Dashboard — Setup Guide (FormSubmit + Vercel, 100% free)

Every form on the website does two things at once:

1. **Emails the submission** instantly to `joshihemant3@gmail.com` via
   [FormSubmit.co](https://formsubmit.co) (free, unlimited, no account needed).
   Career applications arrive with the CV attached.
2. **Stores the submission** for the private dashboard at `/dashboard.html`,
   using Vercel's built-in Blob storage (free tier). The dashboard has one tab
   per form, CSV export, and a password gate.

```
Form ──▶ FormSubmit ──▶ email alert (+ CV attached)
    └─▶ /api/submit ──▶ Vercel Blob ──▶ /dashboard.html (password-gated)
```

## One-time setup

### 1. Deploy to Vercel

1. Push this repo to GitHub (already done — see git history).
2. Go to [vercel.com](https://vercel.com) → sign in **with GitHub**.
3. **Add New → Project → Import** `Himeros-web`.
4. Leave every setting as-is (Framework preset: *Other*, no build command) →
   **Deploy**. Your site goes live at `https://himeros-web.vercel.app`.

### 2. Turn on dashboard storage

1. In your Vercel project: **Storage tab → Create Database → Blob** → give it
   any name → **Create** → then **Connect to Project** (select this project).
   Vercel injects the `BLOB_READ_WRITE_TOKEN` automatically.
2. **Redeploy** once (Deployments → ⋯ → Redeploy) so the function picks up the
   token.

### 3. Set the dashboard password

1. Project **Settings → Environment Variables** → add:
   - Key: `DASHBOARD_PASSWORD`
   - Value: choose a strong password
   - Environments: Production (and Preview)
2. **Redeploy** again. Done — `/dashboard.html` now works.

### 4. Activate FormSubmit (one-time, 1 minute)

Submit any form once from the live site. FormSubmit emails
joshihemant3@gmail.com an **activation link — click it**. From then on every
submission lands in the inbox forever. (Check spam the first time.)

### 5. Test

- Submit the Contact form → check Gmail + open `yoursite.vercel.app/dashboard.html`,
  enter the password, and the message should appear under **Contact**.
- Repeat for Product Enquiry and Career (attach a small test PDF).

## Daily use

- **Email** = instant notifications (reply straight from Gmail).
- **`/dashboard.html`** = searchable history, per-form tabs, CSV export.
  The password stays unlocked in the browser session only.

## Troubleshooting

| Symptom | Cause & fix |
|---|---|
| Form shows an activation message | Click the activation email FormSubmit sent to joshihemant3@gmail.com (see step 4). |
| Forms email fine, but dashboard says "storage not configured" | Blob not connected or no redeploy after connecting (step 2). |
| Dashboard says wrong password | The `DASHBOARD_PASSWORD` env var isn't set, or you typed a different one (step 3). |
| Dashboard table empty but emails work | Storage started after some submissions were emailed — those older ones only exist in Gmail. New ones will appear. |
| Changed code but nothing changed | Push to GitHub, then Deployments → Redeploy (or push again — Vercel auto-deploys every push). |

## Alternative: Google Sheets backend

A fully working Google Apps Script variant (submissions into a Google Sheet
tab per form) is kept in [`forms-backend.gs`](forms-backend.gs) — useful if you
ever prefer spreadsheet storage. The site currently does not use it.
