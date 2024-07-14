const fitTextElements = document.querySelectorAll(".js-fit-text");

/* Functions
############################################################################ */

const addCopyToClipboard = () => {
  const present = document.querySelector(".mi-slide.present");
  const codeBlocks = present.querySelectorAll("pre .hljs, pre .code");

  codeBlocks.forEach(codeBlock => {
    const button = document.createElement("button");
    button.classList.add("copy-button");
    button.classList.add("icon");
    button.classList.add("icon-copy");
    button.textContent = "assignment";

    button.addEventListener("click", (ev) => {
      const text = codeBlock.textContent.replace(/assignment/, "");
      navigator.clipboard.writeText(text);
    });
    codeBlock.appendChild(button);
  } );  
};

const reorderFooter = () => {
  const present = document.querySelector(".mi-slide.present");
  if(!present) return;

  const presentChild = present.querySelector(".present");
  if(!presentChild) return;

  const footer = present.querySelector("footer");
  if(!footer) return;
  
  presentChild.appendChild(footer);
  footer.classList.add("is-active");
}

/* Main
############################################################################ */

Reveal.on( 'ready', event => {

  const figures = document.querySelectorAll(".slide figure");
  figures.forEach(figure => {
    figure.addEventListener("dblclick", (ev) => {
      figure.classList.toggle("zoom");
    });
  });

  const info = document.querySelector(".info");
  if (info) {
    info.addEventListener("click", (ev) => {
      info.classList.toggle("is-active");
      info.parentNode.querySelector("blockquote").classList.toggle("is-passive");
    });
  }
} );

Reveal.on('slidechanged', event => {

  addCopyToClipboard();
  reorderFooter();

  fitTextElements.forEach(ele=>{
    window.fitText( ele );
  });

  const BUs = event.currentSlide.querySelectorAll(".bu");
  BUs.forEach(bu => {
    bu.classList.add("is-active");
  });

  const delayedItems = event.currentSlide.querySelectorAll(".js-delay");
  delayedItems.forEach(item => {
    item.classList.add("has-delay");
  });

  if (!event.previousSlide) return;
  
  const lastBUs = event.previousSlide.querySelectorAll(".bu");
  lastBUs.forEach(bu => {
    bu.classList.remove("is-active");
  });

  const lastDelayedItems = event.previousSlide.querySelectorAll(".js-delay");
  lastDelayedItems.forEach(item => {
    item.classList.remove("has-delay");
  });

  

  /* const lastFigures = event.previousSlide.querySelectorAll("figure");
  lastFigures.forEach(figure => {
    figure.removeEventListener("click", (ev) => {
      toggleZoom(figure);
    }, true);
  });*/
} );