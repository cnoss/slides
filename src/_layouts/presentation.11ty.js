const fs = require('fs');

const imgEndings = ['jpg', 'png'];

const backgroundColors = {
  'mi-blau': '#4952e1',
  'mi-pink': '#d16',
  'mi-gruen': '#00ad2f',
  'mi-lila': '#9313ce',
  'mi-black': '#231f20',
  'mi-grau': '#aaa',
  'mi-hellgrau': '#efefef',
};

const bgColorToClass = {
  intro: 'mi-lila',
  shout: 'mi-blau',
  outro: 'mi-black'
};


const outro = `
<div class="outro">
<figure class="outro-avatar">
<img src="/assets/images/cnoss.jpeg">
<figcaption>
<p>Danke für's Mitmachen</p>
<p class="small"><a href="https://christiannoss.de">https://christiannoss.de</a></p>
</figcaption>
</figure>
</div>
`;


const codeWraps = {
  cite(data, html) { return `<blockquote class="has-whitener">${data.content}<cite>${data.author}</cite>${html.src}</blockquote>`; },
  shout(data, html) { return `<blockquote class="has-whitener">${data.content}<cite>${data.author}</cite>${html.src}</blockquote><p class="info is-passive">${data.info}</p>`; },
  statement(data, html) { return `<div><h1>${data.title}</h1><div class="fragment">${data.content}</div></div>`; },
  interlude(data, html) { return `<div class="is-fullscreen"><h1 class="title">${data.title}</h1><h2 class="subtitle js-delay">${data.subtitle}</h2></div>`; },
  outro(data, html) { return `<div class="is-fullscreen is-centered"><p>${data.content}</p>${outro}</div>`; },
};

const injectContent = (wrap, data, html) => wrap(data, html);

const wrapContentByType = (data, type) => {
  const html = { src: '' };
  if (data.src) { html.src = `<div class="src">${data.src}</div>`; }
  const content = codeWraps[type] ? injectContent(codeWraps[type], data, html) : data.content;
  return content;
};

const getData = (collections, pattern) => collections.filter((item) => item.url.match(pattern));
const getBgColor = (cssClass) => {
  const colorKey = bgColorToClass[cssClass];
  const color = backgroundColors[colorKey];
  return color ? `data-background-color="${color}"` : '';
};

const getBgImage = (img, path) => {
  const base = `${path}images/${img}`;
  const whatEnding = imgEndings.find((ending) => {
    const src = `docs${base}.${ending}`;
    if (!fs.existsSync(src)) return false;
    return true;
  });

  return whatEnding ? `data-background-image="${base}.${whatEnding}"` : '';
};

const getTransition = (transition) => (transition ? `data-transition="${transition}"` : 'data-transition="convex"');
const getAdditionalClasses = (additionalClasses) => (additionalClasses ? additionalClasses : '');
const getStatus = (status) => (status && status !== 'ok' ? `<div class="status">ToDo: ${status}</div>` : '');

exports.render = function (data) {
  const presentationData = getData(data.collections.sorted, data.page.fileSlug);

  const slides = presentationData.map((slide) => {
    const slideClass = slide.data.slideClasses;
    const backgroundColor = getBgColor(slideClass);
    const backgroundImage = getBgImage(slide.data.img, data.page.url);
    const transition = getTransition(slide.data.transition);
    const additionalClasses = getAdditionalClasses(slide.data.additionalClasses);
    const content = wrapContentByType(slide.data, slideClass);
    const status = getStatus(slide.data.status);
    return `
      <section class="mi-slide ${slideClass} ${additionalClasses}" ${backgroundColor} ${backgroundImage} ${transition}>
      ${content}
      ${status}
      </section>
    `;
  });

  return `<!doctype html>
  <html lang="de">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  
      <title>Screendesign // ${data.title}</title>
  
      <link rel="stylesheet" href="/reveal/dist/reset.css">
      <link rel="stylesheet" href="/reveal/dist/reveal.css">
      <link rel="stylesheet" href="/assets/main.css">
  
      <link rel="icon" type="image/svg" href="/assets/images/preview_black_24dp.svg">
  
      <!-- Theme used for syntax highlighted code -->
      <link rel="stylesheet" href="/reveal/plugin/highlight/monokai.css">
    </head>
    <body>
      <div class="reveal">
        <div class="slides">
          ${slides.join('\n')}  
        </div>
      </div>
      
      <script src="/reveal/dist/reveal.js"></script>
      <script src="/assets/scripts/libs/fittext.js"></script>
      <script src="/assets/scripts/main.js"></script>
      <script src="/reveal/plugin/notes/notes.js"></script>
      <script src="/reveal/plugin/markdown/markdown.js"></script>
      <script src="/reveal/plugin/highlight/highlight.js"></script>
      <script src="/reveal/plugin/zoom/zoom.js"></script>
      <script>
        // More info about initialization & config:
        // - https://revealjs.com/initialization/
        // - https://revealjs.com/config/
        Reveal.initialize({
          hash: true, 
          center: false,
          disableLayout: true,
          progress: true,
          backgroundTransition: 'zoom',
          // Learn about plugins: https://revealjs.com/plugins/
          plugins: [RevealMarkdown, RevealHighlight, RevealNotes, RevealZoom]
        });
      </script>
    </body>
  </html>`;
};
