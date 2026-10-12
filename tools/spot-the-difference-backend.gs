// Backend for ch4/spot-the-difference.html: stores the answers students send from their phones,
// and the pair the projector is currently showing.
//
// Setup (once, about 5 minutes):
//  1. Create a new Google Sheet (any name). Extensions → Apps Script. Replace the editor's contents with this file. Save.
//  2. Project Settings (gear icon) → Script Properties → Add property: TEACHER_KEY = any word you choose. Save.
//  3. Deploy → New deployment → type "Web app". Execute as: Me. Who has access: Anyone. Deploy, authorize, copy the web-app URL.
//  4. Paste that URL into `const API = '...'` near the top of the script in ch4/spot-the-difference.html, and publish the page.
//  5. In class, open the projector page as  .../ch4/spot-the-difference.html#key=YOUR_WORD
//     The key lets only the projector change the pair; the QR code sends phones to the same page with ?phone and no key.
//
// Each answer becomes one row of the "answers" sheet: time, date of the session, pair number, text. Nothing identifies the student.
// After editing this file, use Deploy → Manage deployments → edit → New version, so the URL stays the same.

const SHEET = 'answers';
const MAX_LEN = 140;

function doGet(e) {
  const p = e.parameter || {};
  let out;
  try {
    if (p.action === 'submit') out = submit_(p);
    else if (p.action === 'list') out = list_(p);
    else if (p.action === 'round') out = state_();
    else if (p.action === 'setRound') out = setRound_(p);
    else out = { ok: false, error: 'unknown action' };
  } catch (err) {
    out = { ok: false, error: String(err) };
  }
  return ContentService.createTextOutput(JSON.stringify(out)).setMimeType(ContentService.MimeType.JSON);
}

function sheet_() {
  const ss = SpreadsheetApp.getActive();
  let sh = ss.getSheetByName(SHEET);
  if (!sh) { sh = ss.insertSheet(SHEET); sh.appendRow(['time', 'session', 'pair', 'answer']); }
  return sh;
}

// the pair on the projector and the date of the session, cached so a room of phones polling it stays fast
function state_() {
  const cache = CacheService.getScriptCache(), hit = cache.get('state');
  if (hit) return JSON.parse(hit);
  const props = PropertiesService.getScriptProperties();
  const st = { round: parseInt(props.getProperty('round') || '1', 10), session: props.getProperty('session') || '' };
  cache.put('state', JSON.stringify(st), 10);
  return st;
}

function setRound_(p) {
  const props = PropertiesService.getScriptProperties();
  if (!p.key || p.key !== props.getProperty('TEACHER_KEY')) return { ok: false, error: 'wrong key' };
  const round = parseInt(p.round, 10);
  if (!(round >= 1 && round <= 20)) return { ok: false, error: 'bad pair number' };
  props.setProperty('round', String(round));
  props.setProperty('session', String(p.session || '').slice(0, 10));
  CacheService.getScriptCache().remove('state');
  return { ok: true };
}

function submit_(p) {
  const text = String(p.text || '').replace(/\s+/g, ' ').trim().slice(0, MAX_LEN);
  const round = parseInt(p.round, 10);
  if (!text || !(round >= 1 && round <= 20)) return { ok: false, error: 'empty answer' };
  const st = state_();
  const lock = LockService.getScriptLock();
  lock.waitLock(5000);
  // the leading apostrophe keeps Sheets from turning the session date into a date value
  try { sheet_().appendRow([new Date(), "'" + st.session, round, text]); }
  finally { lock.releaseLock(); }
  CacheService.getScriptCache().remove('list' + round);
  return { ok: true };
}

// a session cell as 'yyyy-MM-dd', also for rows written before the apostrophe fix, where Sheets stored a date
function sessionOf_(v) {
  if (v instanceof Date) return Utilities.formatDate(v, SpreadsheetApp.getActive().getSpreadsheetTimeZone(), 'yyyy-MM-dd');
  return String(v);
}

// this session's answers for one pair; cached for a few seconds because the projector polls every 3 s
function list_(p) {
  const round = parseInt(p.round, 10), cache = CacheService.getScriptCache(), key = 'list' + round;
  const hit = cache.get(key);
  if (hit) return JSON.parse(hit);
  const session = state_().session;
  const rows = sheet_().getDataRange().getValues().slice(1)
    .filter(r => sessionOf_(r[1]) === session && Number(r[2]) === round)
    .map(r => ({ t: new Date(r[0]).getTime(), text: String(r[3]) }));
  const out = { ok: true, round: round, answers: rows };
  const s = JSON.stringify(out);
  if (s.length < 90000) cache.put(key, s, 4);
  return out;
}
