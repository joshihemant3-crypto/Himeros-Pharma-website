/**
 * Himeros Pharma website — free form backend (Google Apps Script)
 * =====================================================================
 * SETUP: follow docs/FORMS_SETUP.md (short version below).
 *
 * 1. Create a Google Spreadsheet named e.g. "Himeros Website Forms".
 * 2. In the spreadsheet: Extensions > Apps Script > paste THIS file > Save.
 * 3. Deploy > New deployment > type "Web app"
 *      Execute as: Me
 *      Who has access: Anyone
 *    > Deploy > authorize > copy the Web app URL (ends in /exec).
 * 4. Put that URL into FORM_ENDPOINT in contact.html, product-enquiry.html
 *    and career-apply.html.
 *
 * WHAT IT DOES
 *  - Each website form POSTs JSON here with a "form" field:
 *      contact | enquiry | career
 *  - Submissions are appended as rows to a matching sheet tab
 *    (created automatically with headers on first use).
 *  - Career CVs are decoded and saved into a Drive folder
 *    "Himeros Website — CVs", and the Drive link is stored in the row.
 *  - Every submission sends an email alert to NOTIFY_EMAIL (career alerts
 *    have the CV attached).
 *  - A hidden "honeypot" field silently discards bot submissions.
 *
 * NOTE: after changing this script, use Deploy > Manage deployments >
 * edit > Version: New version, or the old code keeps running.
 */

var NOTIFY_EMAIL = 'joshihemant3@gmail.com';
var CV_FOLDER_NAME = 'Himeros Website — CVs';

// REQUIRED for standalone scripts (created at script.google.com):
// paste your spreadsheet's ID from its URL:
// docs.google.com/spreadsheets/d/THIS-LONG-ID/edit
var SPREADSHEET_ID = '';

var FORMS = {
  contact: { sheet: 'Contact',             subject: 'New Contact message — himerospharma.com' },
  enquiry: { sheet: 'Product Enquiry',     subject: 'New Product Enquiry — himerospharma.com' },
  career:  { sheet: 'Career Applications', subject: 'New Career Application — himerospharma.com' }
};

var HEADERS = {
  'Contact':             ['Timestamp', 'Full Name', 'Email', 'Phone', 'Topic', 'Message'],
  'Product Enquiry':     ['Timestamp', 'Full Name', 'Email', 'Phone', 'Topic', 'Message'],
  'Career Applications': ['Timestamp', 'First Name', 'Last Name', 'Mobile', 'Email', 'Address',
                          'Qualification', 'University', 'Total Work Exp (months)',
                          'Work Experience', 'Notice Period', 'Current CTC (LPA)',
                          'Location Pref 1', 'Location Pref 2', 'Location Pref 3',
                          'Ready to Relocate', 'CV File', 'CV Link']
};

/** Returns the spreadsheet this script writes to (bound or by ID). */
function getSheetBook() {
  if (SPREADSHEET_ID) return SpreadsheetApp.openById(SPREADSHEET_ID);
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  if (!ss) {
    throw new Error('SPREADSHEET_ID is empty. Open your spreadsheet, copy the long ID from its URL, and paste it into SPREADSHEET_ID at the top of this file.');
  }
  return ss;
}

function doPost(e) {
  try {
    var d = JSON.parse(e.postData.contents);
    var cfg = FORMS[d.form];
    if (!cfg) return reply({ status: 'error', message: 'Unknown form type: ' + d.form });
    if (d.honeypot) return reply({ status: 'success' }); // bot hit the hidden field — save nothing

    var ss = getSheetBook();
    var sheet = ensureSheet(ss, cfg.sheet);

    var cvLink = '';
    if (d.form === 'career') cvLink = saveCv(d);

    sheet.appendRow(buildRow(d.form, d, cvLink));
    notify(d, cfg, cvLink);
    return reply({ status: 'success' });
  } catch (err) {
    return reply({ status: 'error', message: String(err) });
  }
}

/* ---------------- helpers ---------------- */

function ensureSheet(ss, name) {
  var sheet = ss.getSheetByName(name);
  if (!sheet) {
    sheet = ss.insertSheet(name);
    sheet.appendRow(HEADERS[name]);
    sheet.getRange(1, 1, 1, HEADERS[name].length).setFontWeight('bold');
    sheet.setFrozenRows(1);
  }
  return sheet;
}

function buildRow(form, d, cvLink) {
  var now = new Date();
  if (form === 'career') {
    return [now, d.firstName || '', d.lastName || '', d.mobile || '', d.email || '',
            d.address || '', d.qualification || '', d.university || '', d.totalWorkEx || '',
            d.workExperience || '', d.noticePeriod || '', d.currentCtc || '',
            d.location1 || '', d.location2 || '', d.location3 || '', d.relocate || '',
            (d.cv && d.cv.name) || '', cvLink];
  }
  return [now, d.fullName || '', d.email || '', d.phone || '', d.topic || '', d.message || ''];
}

/** Decodes the base64 CV from the career form into a Drive file. Returns a shareable link. */
function saveCv(d) {
  if (!d.cv || !d.cv.data) return '';
  var folders = DriveApp.getFoldersByName(CV_FOLDER_NAME);
  var folder = folders.hasNext() ? folders.next() : DriveApp.createFolder(CV_FOLDER_NAME);

  var bytes = Utilities.base64Decode(d.cv.data);
  var blob = Utilities.newBlob(bytes, d.cv.type || 'application/octet-stream', d.cv.name || 'cv');

  // Prefix the filename with the candidate's name for easy browsing
  var safeName = ((d.firstName || '') + '-' + (d.lastName || '')).replace(/[^a-zA-Z0-9-_]/g, '');
  var stamp = Utilities.formatDate(new Date(), 'IST', 'yyyy-MM-dd');
  if (safeName) blob.setName(safeName + '-' + stamp + '-' + blob.getName());

  var file = folder.createFile(blob);
  try { file.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW); } catch (ignore) {}
  return file.getUrl();
}

/** Sends the alert email to NOTIFY_EMAIL. */
function notify(d, cfg, cvLink) {
  var body;
  if (d.form === 'career') {
    body = 'New career application from himerospharma.com:\n\n' +
      'Name: ' + d.firstName + ' ' + d.lastName + '\n' +
      'Mobile: ' + d.mobile + '\nEmail: ' + d.email + '\n' +
      'Address: ' + d.address + '\n' +
      'Qualification: ' + d.qualification + ' (' + d.university + ')\n' +
      'Total experience: ' + d.totalWorkEx + ' months\n' +
      'Experience details:\n' + (d.workExperience || '- (none)') + '\n' +
      'Notice period: ' + d.noticePeriod + '\nCurrent CTC: ' + d.currentCtc + ' LPA\n' +
      'Locations: ' + [d.location1, d.location2, d.location3].filter(Boolean).join(', ') + '\n' +
      'Relocate: ' + d.relocate + '\n' +
      'CV: ' + (cvLink || '(no CV attached)') + '\n\n' +
      'Dashboard: ' + getSheetBook().getUrl();
  } else {
    body = 'New ' + (d.form === 'enquiry' ? 'product enquiry' : 'contact message') +
      ' from himerospharma.com:\n\n' +
      'Name: ' + d.fullName + '\nEmail: ' + d.email + '\nPhone: ' + (d.phone || '-') + '\n' +
      'Topic: ' + (d.topic || '-') + '\n\nMessage:\n' + d.message + '\n\n' +
      'Dashboard: ' + getSheetBook().getUrl();
  }

  var options = { name: 'Himeros Website Forms' };
  if (d.form === 'career' && d.cv && d.cv.data) {
    options.attachments = [Utilities.newBlob(
      Utilities.base64Decode(d.cv.data), d.cv.type || 'application/octet-stream', d.cv.name || 'cv')];
  }
  MailApp.sendEmail(NOTIFY_EMAIL, cfg.subject, body, options);
}

function reply(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
