const htmlmin = require('html-minifier');


module.exports = function (eleventyConfig) {
  eleventyConfig.setUseGitIgnore(false);


  // Watch our compiled assets for changes
  eleventyConfig.addWatchTarget('./src/compiled-assets/main.css');
  eleventyConfig.addWatchTarget('./src/assets/scripts/main.js');

  // Copy _data
  eleventyConfig.addPassthroughCopy({ 'src/_data': 'assets/data' });

  // Copy src/compiled-assets to /assets
  eleventyConfig.addPassthroughCopy({ 'src/compiled-assets': 'assets' });

  // Copy all fonts
  eleventyConfig.addPassthroughCopy({ 'src/assets/fonts': 'assets/fonts' });

  // Copy asset images
  eleventyConfig.addPassthroughCopy({ 'src/assets/images': 'assets/images' });

  // Copy images
  eleventyConfig.addPassthroughCopy('src/presentations/**/images/*.{jpg,png,svg,jpeg}');
  eleventyConfig.addPassthroughCopy('src/presentations/**/images/**/*.{jpg,png,svg,jpeg}');

  // Copy Reveal Stuff
  eleventyConfig.addPassthroughCopy({ 'reveal/dist': 'reveal/dist' });
  eleventyConfig.addPassthroughCopy({ 'reveal/plugin': 'reveal/plugin' });
  
  // Copy Scripts
  eleventyConfig.addPassthroughCopy({ 'src/assets/scripts': 'assets/scripts' });
  eleventyConfig.addWatchTarget("./src/assets/scripts");


  eleventyConfig.addFilter("presentationByTopic", function (topic) {
    eleventyConfig.addCollection(topic, (collection) => {
      return collection.getFilteredByGlob(`./src/presentations/${topic}/*.md`);
    });
    return topic;
  });

  eleventyConfig.addCollection("presentations", (collection) => {
    const presentations = collection.getFilteredByGlob("./src/presentations/**/index.md");
    return presentations;
  });

  eleventyConfig.addCollection("all", function (collection) {
    return collection.getAll();
  });

  eleventyConfig.addCollection("sorted", function (collection) {
    const presentations = collection.getFilteredByGlob("./src/presentations/**/*.md").sort((a, b) => {
      const filenameFromA = a.filePathStem.split(/\//).pop();
      const filenameFromB = b.filePathStem.split(/\//).pop();
      
      if (filenameFromA === 'index') return 1;
      else if (a.fileSlug > b.fileSlug) return 1;
      else if (a.fileSlug < b.fileSlug) return -1;
      
      else return 0;
    }); 

    return presentations;
  });

  if (process.env.ELEVENTY_ENV === 'production') {
    eleventyConfig.addTransform('htmlmin', (content, outputPath) => {
      if (outputPath.endsWith('.html')) {
        const minified = htmlmin.minify(content, {
          collapseInlineTagWhitespace: false,
          collapseWhitespace: true,
          removeComments: true,
          sortClassName: true,
          useShortDoctype: true,
        });

        return minified;
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
    pathPrefix: "",
    markdownTemplateEngine: 'njk',
    htmlTemplateEngine: 'njk',
    templateFormats: [
      'md',
      'html',
      'njk'
    ],
  };
};
