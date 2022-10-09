const htmlmin = require('html-minifier');

const pathPrefix = (process.env.ELEVENTY_ENV === 'production') ? "slides" : "";
const ghPagesFolder = "docs";

const insertMarkup = (string)=>{
 string = string.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>", string);
 return string.replace(/\*(.*?)\*/g, "<mark>$1</mark>", string);
}

const insertColor = (string, colorClass)=>{
 const color = (colorClass) ? colorClass : "is-purple";
 return string.replace(/\/\//g, "<span class="+color+">//</span>", string);
}

const getPresentationData = (collection, pattern)=>{
  const allSlides = collection.getFilteredByGlob(pattern);

  return allSlides.sort((a, b) => {
    if (a.fileSlug > b.fileSlug) return 1;
    else a.fileSlug < b.fileSlug
    return -1;
   });
}

module.exports = function (eleventyConfig) {
 eleventyConfig.setUseGitIgnore(false);

 /* Compilation
   ########################################################################## */

 // Watch our compiled assets for changes
 eleventyConfig.addWatchTarget('./src/compiled-assets/main.css');
 eleventyConfig.addWatchTarget('./src/assets/scripts/main.js');

 // Copy _data
 eleventyConfig.addPassthroughCopy({'src/_data': 'assets/data'});

 // Copy src/compiled-assets to /assets
 eleventyConfig.addPassthroughCopy({'src/compiled-assets': 'assets'});

 // Copy all fonts
 eleventyConfig.addPassthroughCopy({'src/assets/fonts': 'assets/fonts'});

 // Copy asset images
 eleventyConfig.addPassthroughCopy({'src/assets/images': 'assets/images'});
  
 // Copy images
 eleventyConfig.addPassthroughCopy('src/presentations/**/images/*.{jpg,png,svg,jpeg}');
 eleventyConfig.addPassthroughCopy('src/presentations/**/images/**/*.{jpg,png,svg,jpeg}');

 // Copy Reveal Stuff
 eleventyConfig.addPassthroughCopy({'reveal/dist': 'reveal/dist'});
 eleventyConfig.addPassthroughCopy({'reveal/plugin': 'reveal/plugin'});

 // Copy Scripts
 eleventyConfig.addPassthroughCopy({'src/assets/scripts': 'assets/scripts'});
 eleventyConfig.addWatchTarget("./src/assets/scripts");

 /* Functions
 ########################################################################## */

 eleventyConfig.addJavaScriptFunction("urlPrefix", function() {
  return pathPrefix;
 });

 /* Filter
 ########################################################################## */


 eleventyConfig.addFilter("presentationByTopic", function (topic) {
  eleventyConfig.addCollection(topic, (collection) => {
   return collection.getFilteredByGlob(`./src/presentations/${topic}/*.md`);
  });
  return topic;
 });

 /* Collections
 ########################################################################## */

 eleventyConfig.addCollection("screendesign", (collection) => {
  return presentations = getPresentationData(collection, "./src/presentations/screendesign/**/index.md");
 });

 eleventyConfig.addCollection("misc", (collection) => {
  return presentations = getPresentationData(collection, "./src/presentations/misc/**/index.md");
 });

 eleventyConfig.addCollection("all", function (collection) {
  return collection.getAll();
 });

 eleventyConfig.addCollection("sorted", function (collection) {
  return presentations = collection.getFilteredByGlob("./src/presentations/**/*.md").sort((a, b) => {
   const filenameFromA = a.filePathStem.split(/\//).pop();

   if (filenameFromA === 'index') return 1;
   else if (a.fileSlug > b.fileSlug) return 1;
   else if (a.fileSlug < b.fileSlug) return -1;

   else return 0;
  });
 });

 /* Shortcodes
 ########################################################################## */

 eleventyConfig.addShortcode('screenshot', (imgSrc, props) => {
  const propData = (props) ? JSON.parse(props) : {};
  const dataTransition = propData && propData.transition ? `data-transition="${propData.transition}"` : '';
  const dataBackgroundTransition = propData && propData.backgroundTransition ? `data-background-transition="${propData.backgroundTransition}"` : '';
  const classes = propData && propData.classes ? propData.classes : '';
  const width = propData && propData.width ? `width="${propData.width}" ` : '';
  const buCreditHtml = propData && propData.credit ? `<p class="credit">${propData.credit}</p>` : '';
  const buHtml = propData && propData.bu ? `<figcaption class="bu"><p>${insertMarkup(propData.bu)}</p></figcaption>` : '';
  return `<section data-slide-shortcode-class="screenshot" class="image screenshot ${classes}" ${dataTransition} ${dataBackgroundTransition}><figure><img src="${imgSrc}" alt="${imgSrc}" ${width}>${buHtml}</figure></section>`;
 });

 eleventyConfig.addShortcode('screenshotFs', (imgSrc, props) => {
  const propData = (props) ? JSON.parse(props) : {};
  const dataTransition = propData && propData.transition ? `data-transition="${propData.transition}"` : '';
  const dataBackgroundTransition = propData && propData.backgroundTransition ? `data-background-transition="${propData.backgroundTransition}"` : '';
  const classes = propData && propData.classes ? propData.classes : '';
  const buCreditHtml = propData && propData.credit ? `<p class="credit">${propData.credit}</p>` : '';
  const buHtml = propData && propData.bu ? `<div class="bu"><p>${insertMarkup(propData.bu)}</p></div>` : '';
  return `<section data-slide-shortcode-class="screenshot" class="image is-fullscreen ${classes}" data-background="${imgSrc}" ${dataTransition} ${dataBackgroundTransition}>${buHtml}</section>`;
 });

 eleventyConfig.addShortcode('meta',()=>{
  return `<meta name="robots" content="noindex">
    <meta name="googlebot" content="noindex">
    <meta name="googlebot-news" content="noindex">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
`});

 eleventyConfig.addShortcode('interlude', (title, subtitle, transition) => {
  const getRandomBackgroundColor = ()=>{
    const colors = ['#4952e1', '#d16', '#00ad2f', '#9313ce', '#aaa'];
    return colors[colors.length * Math.random() | 0];
  }
  const htmlSubtitle = subtitle ? `<h2 class="subtitle js-delay">${insertMarkup(subtitle)}</h2>` : '';
  const dataTransition = transition ? `data-transition="${transition}"` : '';

  return `<section data-slide-shortcode-class="interlude" data-background-color="${getRandomBackgroundColor()}" class="image screenshot interlude" ${dataTransition}><div><h1 class="title">${insertMarkup(title)}</h1>${htmlSubtitle}</div></section>`;
 });

 eleventyConfig.addShortcode('question', (question, tagline) => {
  const htmlTagline = tagline ? `<h2 class="subtitle js-delay">${tagline}</h2>` : '';
  return `<section data-slide-shortcode-class="question" class="question"><div><h1 class="title">${question}</h1>${htmlTagline}</div></section>`;
 });

 eleventyConfig.addShortcode('statement', (title, content, props) => {
  const propData = (props) ? JSON.parse(props) : {};
  const dataBackgroundTransition = propData && propData.backgroundTransition ? `data-background-transition="${propData.backgroundTransition}"` : '';
  return `<section ${dataBackgroundTransition} class="statement"><div><h1 class="title">${insertMarkup(title)}</h1><div class="fragment">${insertMarkup(content)}</div></div></section>`;
 });

 eleventyConfig.addShortcode('fragment', (content, props) => {
  const propData = (props) ? JSON.parse(props) : {};
  return `<div data-slide-shortcode-class="fragment" class="fragment">${insertMarkup(content)}</div>`;
 });

 eleventyConfig.addShortcode('qa', (q, a, props) => {
  const propData = (props) ? JSON.parse(props) : {};
  const dataTransition = propData && propData.transition ? `data-transition="${propData.transition}"` : '';

  let answer = insertMarkup(a);
  answer = insertColor(answer, "is-green");
  return `<section data-slide-shortcode-class="qa" class="qa" ${dataTransition}><div class="qa-wrap"><h1 class="qa-question">${q}</h1><p class="qa-answer fragment">${answer}</p></div></section>`;
 });

 /* Environment
 ########################################################################## */

 if (process.env.ELEVENTY_ENV === 'production') {
  eleventyConfig.addTransform('htmlmin', (content, outputPath) => {
   if (outputPath.endsWith('.html')) {
    return minified = htmlmin.minify(content, {
     collapseInlineTagWhitespace: false,
     collapseWhitespace: true,
     removeComments: true,
     sortClassName: true,
     useShortDoctype: true,
    });
   }

   return content;
  });
 }

 return {
  dir: {
   includes: '_components',
   input: 'src',
   layouts: '_layouts',
   output: 'docs',
  },
  pathPrefix: pathPrefix,
  markdownTemplateEngine: 'njk',
  htmlTemplateEngine: 'njk',
  templateFormats: [
   'md',
   'html',
   'njk'
  ],
 };
};
