// Rendert eine einzelne Folie, z. B. wenn render.js im Stapel die falsche erwischt hat
// Aufruf: node one.js <deck> <h> <v> <ausgabe.png> [wartezeit-ms]
const puppeteer=require('puppeteer-core'); const fs=require('fs');
const [d,h,v,out,wait]=process.argv.slice(2);
(async()=>{
  const b=await puppeteer.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true,userDataDir:`/tmp/shots/profile-${process.pid}`,args:['--no-first-run']});
  const p=await b.newPage(); await p.setViewport({width:1920,height:1080});
  await p.setRequestInterception(true); p.on('request',r=>r.url().includes('reload-client')?r.abort():r.continue());
  await p.goto(`http://127.0.0.1:8080/presentations/screendesign-und-visuelle-kommunikation/${d}/#/${h}/${v}`,{waitUntil:'networkidle0'});
  await new Promise(r=>setTimeout(r,+(wait||3000)));
  console.log(await p.evaluate(()=>JSON.stringify(Reveal.getIndices())));
  await p.screenshot({path:out}); await b.close();
  fs.rmSync(`/tmp/shots/profile-${process.pid}`,{recursive:true,force:true});
})();
