const puppeteer = require('puppeteer-core'); const fs=require('fs');
const decks=process.argv.slice(2);
(async()=>{
  const b = await puppeteer.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless:true, userDataDir:'/tmp/shots/profile6', args:['--no-first-run']});
  const p = await b.newPage(); await p.setViewport({width:1920,height:1080});
  for (const d of decks){
    fs.mkdirSync(`/tmp/shots/r/${d}`,{recursive:true});
    await p.goto(`http://127.0.0.1:8080/presentations/screendesign-und-visuelle-kommunikation/${d}/`,{waitUntil:'networkidle0'});
    await new Promise(r=>setTimeout(r,800));
    const idx = await p.evaluate(()=>Reveal.getSlides().map(s=>Reveal.getIndices(s)));
    let n=0;
    for (const i of idx){ await p.evaluate((h,v)=>{Reveal.configure({transition:'none',backgroundTransition:'none'});Reveal.slide(h,v,99);document.querySelectorAll('.js-delay').forEach(e=>e.classList.add('has-delay'))},i.h,i.v||0);
      await new Promise(r=>setTimeout(r,2000)); n++; await p.screenshot({path:`/tmp/shots/r/${d}/${String(n).padStart(3,'0')}.png`}); }
    console.log(d,n);
  }
  await b.close();
})();
