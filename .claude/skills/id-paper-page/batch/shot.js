const puppeteer = require('puppeteer-core');
const path = require('path');
const exe = path.resolve('node_modules/.remotion/chrome-headless-shell/win64/chrome-headless-shell-win64/chrome-headless-shell.exe');
(async () => {
  const b = await puppeteer.launch({executablePath: exe, headless: true});
  const out = {};
  for (const slug of process.argv.slice(2)) {
    const p = await b.newPage();
    const errs = [];
    p.on('pageerror', e => errs.push(String(e)));
    p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    const width = slug.endsWith('@m') ? 360 : 1100; const s = slug.replace('@m', '');
    await p.setViewport({width, height: 900});
    await p.goto(`http://127.0.0.1:8765/papers/${s}/`, {waitUntil: 'networkidle0'});
    // scroll through the page like a reader so each chart's observer fires
    const H = await p.evaluate(() => document.body.scrollHeight);
    for (let y = 0; y < H; y += 400) { await p.evaluate(yy => window.scrollTo(0, yy), y); await new Promise(r => setTimeout(r, 120)); }
    await new Promise(r => setTimeout(r, 1600));
    const info = await p.evaluate(() => ({
      reveals: [...document.querySelectorAll('.reveal')].map(e => e.classList.contains('in')),
      figures: document.querySelectorAll('figure[data-figure]').length,
      tables: document.querySelectorAll('table.data tr').length,
      charts: window.Chart ? Object.keys(Chart.instances).length : -1,
      bignum: document.querySelectorAll('figure .stat').length,
      missing: document.querySelectorAll('.missing').length,
      overflowX: document.documentElement.scrollWidth > window.innerWidth,
    }));
    await p.evaluate(() => window.scrollTo(0, 0));
    await p.screenshot({path: `../shots/${slug}.png`, fullPage: true});
    out[slug] = {...info, errs};
    await p.close();
  }
  console.log(JSON.stringify(out, null, 1));
  await b.close();
})();
