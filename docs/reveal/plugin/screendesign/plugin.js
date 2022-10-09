

const Plugin = () => {

  const attributes = {};
  attributes['markdown'] = false;
  attributes['separator'] = "^\n\n\n";
  attributes['separator-vertical'] = "^\n\n";
  attributes['separator-notes'] = "^Note:";
  attributes['charset'] = "iso-8859-15";
  
  let deck;

  function createSlideWraps(slides) {
    console.log(slides);
    const mdSlides = slides.filter(slide => { return slide.dataset.contentFile.length > 0 });
    console.log(mdSlides);
      mdSlides.forEach(mdSlide => {
      console.log(mdSlide);
      for (let attribute in attributes) {
        attributes['markdown'] = mdSlide.dataset.contentFile;
        mdSlide.setAttribute(`data-${attribute}`, attributes[attribute]);
      }
    });
  }


  return {
    id: 'screendesign',
    init: function (reveal) {
      createSlideWraps(reveal.getSlides());
    }
  }
}

export default Plugin;