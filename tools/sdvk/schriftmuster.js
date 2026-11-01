// Rendert HTML-Schnipsel mit Systemschriften zu PNG, damit Schriftmuster auf jedem Rechner gleich aussehen.
// Aufruf: node schriftmuster.js '[{"out":"/pfad/a.png","w":1600,"h":900,"html":"<div>…</div>"}]'
const puppeteer=require('puppeteer-core');
(async()=>{
  const b=await puppeteer.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true,userDataDir:`/tmp/shots/profile-${process.pid}`,args:['--no-first-run']});
  const p=await b.newPage();
  for(const t of JSON.parse(process.argv[2])){
    await p.setViewport({width:t.w,height:t.h,deviceScaleFactor:t.scale||1});
    await p.setContent(`<!doctype html><html lang="de"><body style="margin:0;background:#fff;color:#231f20;width:${t.w}px;height:${t.h}px;overflow:hidden">${t.html}</body></html>`,{waitUntil:'load'});
    await p.evaluate(()=>document.fonts.ready);
    await p.screenshot({path:t.out}); console.log('ok',t.out);
  }
  await b.close();
  require('fs').rmSync(`/tmp/shots/profile-${process.pid}`,{recursive:true,force:true});
})();
