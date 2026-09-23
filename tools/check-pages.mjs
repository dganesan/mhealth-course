// Runtime check for the companion pages, driven through headless Chrome (DevTools protocol).
// For each page: loads it at 1920x1080, walks every step with the arrow keys (finish, then advance),
// prints each step's title, tag chip and subtitle, walks back to step 1, and reports any exception.
// With SHOTS=<dir>, it also saves one JPEG per step (after the step has finished animating).
//
//   node tools/check-pages.mjs ch3/*.html
//   SHOTS=/tmp/shots node tools/check-pages.mjs ch2/find-peaks-criteria.html
//
// Requires Node 22+ (built-in WebSocket and fetch) and Google Chrome in /Applications.
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const root = process.cwd(), pages = process.argv.slice(2), SHOTS = process.env.SHOTS;
if (!pages.length) { console.error('usage: node tools/check-pages.mjs <page.html> ...'); process.exit(2); }
if (SHOTS) fs.mkdirSync(SHOTS, { recursive: true });
const PORT = 9335, profile = fs.mkdtempSync(path.join(os.tmpdir(), 'cs328-check-'));
const chrome = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  ['--headless=new', `--remote-debugging-port=${PORT}`, `--user-data-dir=${profile}`, '--allow-file-access-from-files', 'about:blank'], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));
for (let i = 0; i < 50; i++) { try { await fetch(`http://127.0.0.1:${PORT}/json/version`); break; } catch { await sleep(200); } }

let fails = 0;
for (const pg of pages) {
  const t = await (await fetch(`http://127.0.0.1:${PORT}/json/new?about:blank`, { method: 'PUT' })).json();
  const ws = new WebSocket(t.webSocketDebuggerUrl); await new Promise(r => ws.onopen = r);
  let id = 0; const pend = {}, errs = [];
  ws.onmessage = m => {
    const d = JSON.parse(m.data);
    if (d.id && pend[d.id]) { pend[d.id](d); delete pend[d.id]; }
    if (d.method === 'Runtime.exceptionThrown') errs.push(d.params.exceptionDetails.exception?.description || d.params.exceptionDetails.text);
    if (d.method === 'Runtime.consoleAPICalled' && d.params.type === 'error') errs.push('console: ' + d.params.args.map(a => a.value || a.description).join(' '));
  };
  const send = (method, params = {}) => new Promise(r => { const i = ++id; pend[i] = r; ws.send(JSON.stringify({ id: i, method, params })); });
  const ev = async e => (await send('Runtime.evaluate', { expression: e, returnByValue: true })).result?.result?.value;
  const key = k => ev(`document.dispatchEvent(new KeyboardEvent('keydown',{key:'${k}',bubbles:true}))`);
  const cnt = () => ev(`(document.getElementById('counter')||{}).textContent||''`);
  const head = () => ev(`(()=>{const t=document.getElementById('title'); if(!t) return ''; const g=t.querySelector('.tag'); const tag=g?g.textContent:'';
    return t.textContent.slice(0,t.textContent.length-tag.length)+'  [tag: '+tag+']  [sub: '+(document.getElementById('subtitle')||{}).textContent+']'})()`);
  await send('Runtime.enable'); await send('Page.enable');
  await send('Emulation.setDeviceMetricsOverride', { width: 1920, height: 1080, deviceScaleFactor: 1, mobile: false });
  await send('Page.navigate', { url: 'file://' + path.resolve(root, pg) }); await sleep(1500);
  const n = parseInt(((await cnt()).split('/')[1] || '0').trim()) || 0, lines = [];
  for (let k = 1; k <= n; k++) {
    const c0 = await cnt(); await key('ArrowRight'); await sleep(600);              // finish the step's animation
    if ((await cnt()) !== c0) { await key('ArrowLeft'); await sleep(300); await key('ArrowRight'); await sleep(600); }
    lines.push(`  ${await cnt()}  ${await head()}`);
    if (SHOTS) { const r = await send('Page.captureScreenshot', { format: 'jpeg', quality: 70 });
      fs.writeFileSync(path.join(SHOTS, pg.replace(/[\/.]/g, '_') + '_' + k + '.jpg'), Buffer.from(r.result.data, 'base64')); }
    if (k < n) { await key('ArrowRight'); await sleep(400); }
  }
  for (let k = n - 1; k > 0; k--) { await key('ArrowLeft'); await sleep(250); }
  console.log(`\n${pg}  <title>=${await ev('document.title')}  steps=${n}  errors=${errs.length}  back to ${await cnt()}`);
  lines.forEach(l => console.log(l)); errs.forEach(e => console.log('  ERR ' + e));
  fails += errs.length; ws.close();
}
chrome.kill(); fs.rmSync(profile, { recursive: true, force: true });
console.log('\nTOTAL ERRORS', fails); process.exit(fails ? 1 : 0);
