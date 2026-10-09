const puppeteer = require('puppeteer-core');
(async()=>{
  const b = await puppeteer.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless:true, userDataDir:'/tmp/shots/profile7', args:['--no-first-run']});
  const p = await b.newPage(); await p.setViewport({width:1280,height:720});
  await p.goto('http://127.0.0.1:8080/presentations/screendesign-und-visuelle-kommunikation/prinzip-visuelle-variablen/',{waitUntil:'networkidle0'});
  await new Promise(r=>setTimeout(r,1000));
  const total=await p.evaluate(()=>Reveal.getTotalSlides());
  let log=[];
  for(let i=0;i<60;i++){
    const st=await p.evaluate(()=>{const s=Reveal.getCurrentSlide();const i=Reveal.getIndices();return {h:i.h,v:i.v,f:i.f,txt:(s.querySelector('h1')||{}).textContent||s.getAttribute('data-slide-shortcode-class')||s.className}});
    log.push(`${st.h}/${st.v}${st.f!==undefined?'.'+st.f:''} ${String(st.txt).trim().slice(0,45)}`);
    if(await p.evaluate(()=>Reveal.isLastSlide()&&!Reveal.availableFragments().next)) break;
    await p.keyboard.press('ArrowRight'); await new Promise(r=>setTimeout(r,250));
  }
  console.log('total',total); console.log(log.join('\n'));
  await b.close();
})();
