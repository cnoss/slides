const fs = require('fs');
const { title } = require('process');

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
  cite(data, html) { return `<blockquote class="has-whitener">${data.content}<cite>${data.author}</cite>${html.src}</blockquote>`; },
  bigCite(data, html) { return `<blockquote class="is-big has-whitener">${data.content}<cite>${data.author}</cite>${html.src}</blockquote>`; },
  shout(data, html) { return `<blockquote class="has-whitener">${data.content}<cite>${data.author}</cite>${html.src}</blockquote><p class="info is-passive">${data.info}</p>`; },
  statement(data, html) {
    const content = insertColor(data.content, "is-purple");
    return `<div class="main-content"><h1>${data.title}</h1><div class="fragment">${content}</div></div>`;
  },
  simple(data, html) {
    const content = insertColor(data.content, "is-purple");
    return `<div><h1>${data.title}</h1>${content}</div>`;
  },
  splitView(data, html) {
    return `<div><h1>{data.title}</h1>${data.content}</div>`;
  },
  interlude(data, html) { return `<div class="is-fullscreen"><h1 class="title">${data.title}</h1><h2 class="subtitle js-delay">${data.subtitle}</h2></div>`; },
  outro(data, html) { return `<div class="is-fullscreen is-centered"><p>${data.content}</p>${outro}</div>`; },
  code(data, html) { return `<div><h1>${data.title}</h1>${data.content}</div>${html.footer}`; },
  codeSmall(data, html) { return `<div><h1>${data.title}</h1>${data.content}</div>${html.footer}`; },
  embed(data, html) { return `<div><h1>${data.title}</h1><div class="iframe">${data.embedSrc}</div></div>${html.footer}`; },
  wrap(data, html) { return `${data.content}${html.footer}`; },
};

const injectContent = (wrap, data, html) => wrap(data, html);

const wrapContentByType = (data, type) => {
  const html = { src: '' };
  if (data.src) { html.src = `<div class="src">${data.src}</div>`; }
  html.footer = data.footer ? `<footer>${this.markdown(data.footer)}</footer>` : '';

  const content = codeWraps[type] ? injectContent(codeWraps[type], data, html ) : data.content;
  return content;
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

const getLegacyData = (data) => {
  const { raw, rendered } = this.markdownWithRaw(data);
  const slideSeparator = '---\n';
  const slideContents = raw.split(slideSeparator);

  const slides = slideContents.map((rawContent, index) => {
    const directives = {};
    const content = [];
    let title = `Slide ${index + 1}`;
    rawContent.split('\n').forEach(line => {
      if(line.match(/^slide-is/)){
        const directiveArgs = line.split(' ');
        directiveArgs.forEach(arg => {
          const [key, value] = arg.split(':');
          if(key && value){
            directives[key] = value;
          }
        });
      }else if(line.match(/^##(.*)/)){
        const heading = line.replace(/^##(.*)/, '$1').trim();
        title = heading;
      }else{
        content.push(line);
      }
      
    });
    
    const renderedContent = this.markdown(content.join('\n'));
    return {
      data: {
        slideClasses: directives['slide-is'] || 'normal',
        transition: data.revealOptions && data.revealOptions.transition ? data.revealOptions.transition : '',
        img: directives['bg-img'] || null,
        title: title,
        imgData: {
          position: directives['bg-img-position'] || null,
          size: directives['bg-img-size'] || null,
        },
        additionalClasses: directives['additional-classes'] || null,
        status: directives['status'] || 'ok',
        content: renderedContent,
      }
    };
  });

  

  return slides;
}

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

  const slides = presentationData.map((slide) => {
    const slideClass = slide.data.slideClasses;
    const backgroundColor = getBgColor(slideClass);
    const backgroundImage = getBgImage(slide.data.img);
    const backgroundImageCredits = getBgImageCredits(slide.data.credits);
    const backgroundImageData = getBgImageData(slide.data.imgData);
    const transition = getTransition(slide.data.transition);
    const additionalClasses = getAdditionalClasses(slide.data.additionalClasses);
    const content = wrapContentByType(slide.data, slideClass);
    const status = getStatus(slide.data.status);
    const badge = slide.data.badge ? `<div class="badge"><span>${this.markdown(slide.data.badge)}</span></div>` : '';
    const speakerNotes = slide.data.speaker ? `<aside class="notes"><div>${this.markdown(slide.data.speaker)}</div></aside>` : '';

    
    if(slide.data.status === 'hidden') return '';
    return `
      <section data-slide-class="${slideClass}" class="mi-slide 
      ${slideClass} ${additionalClasses}" ${backgroundColor} ${backgroundImage} ${backgroundImageData} ${transition}>
      ${content}
      ${status}
      ${backgroundImageCredits}
      ${speakerNotes}
      ${badge}
      </section>
    `;
  });

  return `<!doctype html>
  <html lang="de">
    <head>
      <title>${data.title} // Christian Noss</title>
      ${this.meta()}
      <link rel="stylesheet" href="${this.url('/reveal/dist/reset.css')}">
      <link rel="stylesheet" href="${this.url('/reveal/dist/reveal.css')}">
      <link rel="stylesheet" href="${this.url('/assets/main.css')}">
     
      <link rel="icon" type="image/svg" href="${this.url('/assets/images/preview_black_24dp.svg')}">
  
      <!-- Theme used for syntax highlighted code -->
      <link rel="stylesheet" href="${this.url('/reveal/plugin/highlight/github.css')}">
    </head>
    <body>
      <div class="reveal">
        <div class="slides">
          ${slides.join('\n')}  
        </div>

      </div>
      
      <script src="${this.url('/reveal/dist/reveal.js')}"></script>
      <script src="${this.url('/assets/scripts/libs/fittext.js')}"></script>
      <script src="${this.url('/assets/scripts/main.js')}"></script>
      <script src="${this.url('/reveal/plugin/notes/notes.js')}"></script>
      <script src="${this.url('/reveal/plugin/markdown/markdown.js')}"></script>
      <script src="${this.url('/reveal/plugin/highlight/highlight.js')}"></script>
      <script src="${this.url('/reveal/plugin/zoom/zoom.js')}"></script>
      <script>
        // More info about initialization & config:
        // - https://revealjs.com/initialization/
        // - https://revealjs.com/config/
        Reveal.initialize({
          hash: true, 
          center: false,
          disableLayout: true,
          progress: true,
          backgroundTransition: 'fade',
          highlight: {
            highlightOnLoad: false,
          },
          // Learn about plugins: https://revealjs.com/plugins/
          plugins: [RevealMarkdown, RevealHighlight, RevealNotes, RevealZoom]
        }).then(() => {
          const highlight = Reveal.getPlugin('highlight');
          highlight.hljs.configure(
            {
              languages: ['javascript', 'css', 'html', 'bash', 'json', 'markdown', 'xml', 'yaml'],
            }
          );
          highlight.hljs.highlightAll();
        });

        
      </script>
    </body>
  </html>`;
};
