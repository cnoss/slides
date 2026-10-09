const puppeteer = require('puppeteer-core');
const targets = JSON.parse(process.argv[2]);
const RE = '^(alle |alles )?(cookies )?(akzeptieren|zulassen|annehmen|zustimmen|erlauben)$|^(accept|agree|allow)( all)?( cookies)?$|^ok$|^got it$|^同意する$|^同意$|^موافق$';
async function dismiss(p){for(const f of p.frames()){try{await f.evaluate((src)=>{const re=new RegExp(src,'i');for(const el of document.querySelectorAll('button,a,[role=button]')){const t=(el.innerText||'').trim();if(re.test(t)){el.click();return}}},RE)}catch(e){}}}
(async()=>{
  const b = await puppeteer.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless:true, userDataDir:'/tmp/shots/profile9', args:['--no-first-run']});
  for (const t of targets){ const p=await b.newPage(); await p.setViewport({width:1440,height:900});
    await p.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36');
    try{ await p.goto(t.url,{waitUntil:'domcontentloaded',timeout:35000}); }catch(e){ console.log('warn',t.name); }
    await new Promise(r=>setTimeout(r,6000)); await dismiss(p); await new Promise(r=>setTimeout(r,2000));
    try{ await p.screenshot({path:`/tmp/shots/k-${t.name}.png`}); console.log('ok',t.name);}catch(e){console.log('fail',t.name)}
    await p.close(); }
  await b.close();
})();
