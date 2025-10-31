const fs = require('fs');

const imgEndings = ['jpg', 'png'];

const colors = {
  'mi-blau': '#4952e1',
  'mi-pink': '#d16',
  'mi-gruen': '#00ad2f',
  'mi-lila': '#9313ce',
  'mi-black': '#231f20',
  'mi-grau': '#70AE11',
};

const bgColorToClass = {
  intro: 'mi-lila',
  shout: 'mi-blau',
  outro: 'mi-black'
};

const insertColor = (string, colorClass)=>{
  return string; // .replace(/\/\//g, "<span class="+colorClass+">//</span>", string);
}


const outro = `
<div class="outro">
<figure class="outro-avatar">
<img src="../../../assets/images/cnoss.jpeg">
<figcaption>
<p>Danke für's Mitmachen</p>
<p class="small"><a href="https://christiannoss.de">https://christiannoss.de</a></p>
</figcaption>
</figure>
</div>
`;


const codeWraps = {
  cite(data, html, content) { return `<blockquote class="has-whitener">${content}<cite>${data.author}</cite>${html.src}</blockquote>`; },
  bigCite(data, html, content) { return `<blockquote class="is-big has-whitener">${content}<cite>${data.author}</cite>${html.src}</blockquote>`; },
  shout(data, html, content) { return `<blockquote class="has-whitener">${content}<cite>${data.author}</cite>${html.src}</blockquote><p class="info is-passive">${data.info}</p>`; },
  statement(data, html, content) {
    const contentEdit = insertColor(content, "is-purple");
    return `<div class="main-content"><h1>${data.title}</h1><div class="fragment">${contentEdit}</div></div>`;
  },
  simple(data, html, content) {
    const contentEdit = insertColor(content, "is-purple");
    return `<div><h1>${data.title}</h1>${contentEdit}</div>`;
  },
  splitView(data, html, content) {
    return `<div><h1>${data.title}</h1>${content}</div>`;
  },
  interlude(data, html, content) { return `<div class="is-fullscreen"><h1 class="title">${data.title}</h1><h2 class="subtitle js-delay">${data.subtitle}</h2></div>`; },
  outro(data, html, content) { return `<div class="is-fullscreen is-centered"><p>${content}</p>${outro}</div>`; },
  code(data, html, content) { return `<div><h1>${data.title}</h1>${content}</div>${html.footer}`; },
  codeSmall(data, html, content) { return `<div><h1>${data.title}</h1>${content}</div>${html.footer}`; },
  embed(data, html) { return `<div><h1>${data.title}</h1><div class="iframe">${data.embedSrc}</div></div>${html.footer}`; },
  wrap(data, html, content) { return `${content}${html.footer}`; },
};

const injectContent = (wrap, data, html, content) => wrap(data, html, content);


const wrapContentByType = (data, type = 'simple', content) => {

  const html = { src: '' };
  if (data.src) { html.src = `<div class="src">${data.src}</div>`; }
  html.footer = data.footer ? `<footer>${this.markdown(data.footer)}</footer>` : '';
  //return content;
  return codeWraps[type] ? injectContent(codeWraps[type], data, html, content ) : content;
};

const getData = (collections, pattern) => collections.filter((item) => item.url.match(pattern));
const getBgColor = (cssClass) => {
  const colorKey = bgColorToClass[cssClass];
  const color = colors[colorKey];
  return color ? `data-background-color="${color}"` : '';
};

const getBgImage = (img) => {
  if(!img) return '';
  const filename = img.match(/\....$/) ? img : `${img}.jpg`;
  return `data-background-image="./images/${filename}"`;
};

const getBgImageData = (imgData) => {
  if(!imgData) return '';
  const position = imgData.position ? `data-background-position="${imgData.position}"` : '';
  const size = imgData.size ? `data-background-size="${imgData.size}"` : '';

  return `${position} ${size}`;
};

const getBgImageCredits = (credits) => {
  if(!credits) return '';
  const { name, url } = credits;
  const credit = url 
    ? `<a href="${url}" target="_blank">${name}</a>`
    : name;
  return `<div class="bu"><p class="credit">Bild von ${credit}</p></div>`;
};

const enrichSlides = (slideChildren, dataX) => {
  return slideChildren.map((child, index) => {
    const dataZ = index * -1000;
    const rotateZ = index * 15;
    // extract data-slide-class from section tag
    const slideClassMatch = child.match(/class="(.*?)"/); 
    const slideClass = slideClassMatch ? slideClassMatch[1] : '';
    const imageMatch = child.match(/data-background="(.*?)"/);
    const imageSrc = imageMatch ? imageMatch[1] : null;
    // extract inner content of section tag
    const contentMatch = child.match(/<section[\s\S]*?>([\s\S]*?)<\/section>/);
    const content = contentMatch ? contentMatch[1] : '';
    // wrap content in a div with the slideClass as class
    const image = imageSrc !== null ? `<figure><img src="${imageSrc}" alt="${slideClass}"></figure>` : '';

    return `<div class="step mi-slide ${slideClass}" data-z="${dataZ}" data-x="${dataX}" data-rotate-z="${rotateZ}" data-scale="0.5" data-rotate-y="0">${image}${content}</div>`;
  }).join('\n');
};

const getTransition = (transition) => (transition ? `data-transition="${transition}"` : 'data-transition="convex"');
const getAdditionalClasses = (additionalClasses) => (additionalClasses ? additionalClasses : '');
const getStatus = (status) => (status && status !== 'ok' ? `<div class="status">ToDo: ${status}</div>` : '');

exports.render = function (data) {
  // const presentationData = getData(data.collections.sorted, data.page.fileSlug);

  // remove last segment from filePathStem to get base path
  const basePath = data.page.filePathStem.split('/').slice(0, -1).join('/');
  
  const presentationData = (data.version && data.version === 1) 
    ? getLegacyData(data)
    : getData(data.collections.sorted, basePath);

  const slides = presentationData.map((slide, index) => {

    const slideChildren = slide.content ? slide.content.match(/<section[\s\S]*?<\/section>/g) : null;
    

    
    const slideId = `slide-${index}`;
    const dataX = index * 2000;
    const slideClass = slide.data.slideClasses;
    const backgroundColor = getBgColor(slideClass);
    const backgroundImage = getBgImage(slide.data.img);
    const backgroundImageCredits = getBgImageCredits(slide.data.credits);
    const backgroundImageData = getBgImageData(slide.data.imgData);
    const transition = getTransition(slide.data.transition);
    const additionalClasses = getAdditionalClasses(slide.data.additionalClasses);
    const content = wrapContentByType(slide.data, slideClass, slide.content);
    const status = getStatus(slide.data.status);
    
    if(slide.data.status === 'hidden') return '';

    if(slideChildren) {
      return enrichSlides(slideChildren, dataX);
    }

    return `
      <section data-slide-class="${slideClass}" class="step" data-scale="1" id="${slideId}" data-x="${dataX}">
      ${content}
      ${status}

      </section>
    `;
  });

  return `<!doctype html>
  <html lang="de">
    <head>
      <title>${data.title} // Christian Noss</title>
      ${this.meta()}
      <link rel="stylesheet" href="${this.url('/impress.js/css/impress-common.css')}">
      <link rel="stylesheet" href="${this.url('/assets/impress.css')}">
      <link rel="icon" type="image/svg" href="${this.url('/assets/images/preview_black_24dp.svg')}">
  
    </head>
    <body>
      <div id="impress">
            <div id="overview" class="step overview" data-x="-1000" data-y="-1500" data-z="10000" data-scale="3" data-rotate-x="45" data-rotate-y="10">
          <div>
              <h2>Demo of <code>data-rel-position</code></h2>
              <p>This demo use <code>data-rel-position="relative"</code><br>
                  and <code>data-rel-rotate-x/y/z</code><br>
                  to easy 3D positioning of slides.</p>
          </div>
      </div>
        ${slides.join('\n')}  
      </div>

      <script src="${this.url('https://cdn.jsdelivr.net/gh/impress/impress.js@1.1.0/js/impress.js')}"></script>      
      <script>impress().init();</script>
      <script>
document.addEventListener("impress:stepenter", function (event) {
  const step = event.target;
  console.log("Neuer Step:", step.id);

  // Beispiel: Unterschiedlichen Code pro Step ausführen
  if (step.id === "intro") {
    console.log("Willkommen beim Intro!");
  } else if (step.id === "summary") {
    alert("Fast fertig!");
  }
});
</script>
    </body>
  </html>`;
};
