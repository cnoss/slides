const puppeteer = require('puppeteer-core'); const fs=require('fs');
const decks=process.argv.slice(2);
const BASE='http://127.0.0.1:8080/presentations/screendesign-und-visuelle-kommunikation';
(async()=>{
  // Eigenes Chrome-Profil pro Lauf: Parallele Läufe blockieren sich sonst gegenseitig (Profil-Lock)
  const b = await puppeteer.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless:true, userDataDir:`/tmp/shots/profile-${process.pid}`, args:['--no-first-run']});
  const p = await b.newPage(); await p.setViewport({width:1920,height:1080});
  // Live-Reload des Dev-Servers abschalten, sonst bricht ein Neubau den Lauf ab
  await p.setRequestInterception(true); p.on('request',r=>r.url().includes('reload-client')?r.abort():r.continue());
  for (const d of decks){
    fs.mkdirSync(`/tmp/shots/r/${d}`,{recursive:true});
    await p.goto(`${BASE}/${d}/`,{waitUntil:'networkidle0'});
    // Baut der Dev-Server gerade neu, ist Reveal noch nicht da: warten und neu laden
    for(let t=0;t<10;t++){ try{ await p.waitForFunction('window.Reveal && Reveal.isReady && Reveal.isReady()',{timeout:8000}); break; }catch(e){ await new Promise(r=>setTimeout(r,3000)); await p.goto(`${BASE}/${d}/`,{waitUntil:'networkidle0'}); } }
    await new Promise(r=>setTimeout(r,800));
    const idx = await p.evaluate(()=>Reveal.getSlides().map(s=>Reveal.getIndices(s)));
    let n=0;
    for (const i of idx){ await p.evaluate((h,v)=>{Reveal.configure({transition:'none',backgroundTransition:'none'});Reveal.slide(h,v,99);document.querySelectorAll('.js-delay').forEach(e=>e.classList.add('has-delay'))},i.h,i.v||0);
      await new Promise(r=>setTimeout(r,2000)); n++; await p.screenshot({path:`/tmp/shots/r/${d}/${String(n).padStart(3,'0')}.png`}); }
    console.log(d,n);
  }
  await b.close();
  fs.rmSync(`/tmp/shots/profile-${process.pid}`,{recursive:true,force:true});
})();
