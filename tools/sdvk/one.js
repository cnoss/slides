// Rendert eine einzelne Folie, z. B. wenn render.js im Stapel die falsche erwischt hat
// Aufruf: node one.js <deck> <h> <v> <ausgabe.png> [wartezeit-ms]
const puppeteer=require('puppeteer-core'); const fs=require('fs');
const [d,h,v,out,wait]=process.argv.slice(2);
(async()=>{
  const b=await puppeteer.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true,userDataDir:`/tmp/shots/profile-${process.pid}`,args:['--no-first-run']});
  const p=await b.newPage(); await p.setViewport({width:1920,height:1080});
  await p.setRequestInterception(true); p.on('request',r=>r.url().includes('reload-client')?r.abort():r.continue());
  const url=`http://127.0.0.1:8080/presentations/screendesign-und-visuelle-kommunikation/${d}/#/${h}/${v}`;
  await p.goto(url,{waitUntil:'networkidle0'});
  // Baut der Dev-Server gerade neu, ist Reveal noch nicht da: warten und neu laden
  for(let t=0;t<10;t++){ try{ await p.waitForFunction('window.Reveal && Reveal.isReady && Reveal.isReady()',{timeout:8000}); break; }catch(e){ await new Promise(r=>setTimeout(r,3000)); await p.goto(url,{waitUntil:'networkidle0'}); } }
  await new Promise(r=>setTimeout(r,+(wait||3000)));
  console.log(await p.evaluate(()=>JSON.stringify(Reveal.getIndices())));
  await p.screenshot({path:out}); await b.close();
  fs.rmSync(`/tmp/shots/profile-${process.pid}`,{recursive:true,force:true});
})();
