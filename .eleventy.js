const htmlmin = require('html-minifier');

const pathPrefix = (process.env.ELEVENTY_ENV === 'production') ? "slides" : "";

const insertStrong = (string)=>{
 return string.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>", string);
}

const insertColor = (string, colorClass)=>{
 const color = (colorClass) ? colorClass : "is-purple";
 return string.replace(/\/\//g, "<span class="+color+">//</span>", string);
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

 eleventyConfig.addCollection("presentations", (collection) => {
  return presentations = collection.getFilteredByGlob("./src/presentations/**/index.md").sort((a, b) => {
   if (a.fileSlug > b.fileSlug) return 1;
   else a.fileSlug < b.fileSlug
   return -1;

  });
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
  const classes = propData && propData.classes ? propData.classes : '';
  return `<section class="image screenshot ${classes}" ${dataTransition}><figure><img src="${imgSrc}" alt="${imgSrc}"></figure></section>`;
 });

 eleventyConfig.addShortcode('interlude', (title, subtitle, transition) => {
  const htmlSubtitle = subtitle ? `<h2 class="subtitle js-delay">${subtitle}</h2>` : '';
  const dataTransition = transition ? `data-transition="${transition}"` : '';
  return `<section class="image screenshot interlude" ${dataTransition}><div><h1 class="title">${title}</h1>${htmlSubtitle}</div></section>`;
 });

 eleventyConfig.addShortcode('question', (question, tagline) => {
  const htmlTagline = tagline ? `<h2 class="subtitle js-delay">${tagline}</h2>` : '';
  return `<section class="question"><div><h1 class="title">${question}</h1>${htmlTagline}</div></section>`;
 });

 eleventyConfig.addShortcode('fragment', (content, props) => {
  const propData = (props) ? JSON.parse(props) : {};
  return `<div class="fragment">${insertStrong(content)}</div>`;
 });

 eleventyConfig.addShortcode('qa', (q, a, props) => {
  const propData = (props) ? JSON.parse(props) : {};
  const dataTransition = propData && propData.transition ? `data-transition="${propData.transition}"` : '';
  let answer = insertStrong(a);
  answer = insertColor(answer, "is-green");
  return `<section class="qa" ${dataTransition}><div class="qa-wrap"><h1 class="qa-question">${q}</h1><p class="qa-answer fragment">${answer}</p></div></section>`;
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
