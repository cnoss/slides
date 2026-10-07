const fitTextElements = document.querySelectorAll(".js-fit-text");

/* Functions
############################################################################ */

const updateNotesOverlay = () => {
  const overlay = document.querySelector(".notes-overlay");
  const slide = Reveal.getCurrentSlide();
  if (!overlay || !slide) return;

  // bei verschachtelten Folien (wrap) hängen die Notizen an der äußeren .mi-slide
  const outerSlide = slide.closest(".mi-slide");
  const notes = slide.querySelector("aside.notes") || (outerSlide && outerSlide.querySelector("aside.notes"));
  overlay.innerHTML = notes ? notes.innerHTML : "<p><em>Keine Notizen auf dieser Folie.</em></p>";
  overlay.scrollTop = 0;
};

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
      const text = codeBlock.textContent.replace(/assignment/g, "");
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

  const bu = presentChild.querySelector(".bu");
  
  if(bu){
    footer.classList.remove("is-active");
    return;
  }

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

  // Speaker Notes als eigenes Overlay im body: innerhalb der Folie hebelt
  // der transform von .slides position:fixed und damit das Scrollen aus
  const notesOverlay = document.createElement("div");
  notesOverlay.classList.add("notes-overlay");
  notesOverlay.setAttribute("data-prevent-swipe", "");
  document.body.appendChild(notesOverlay);

  // wenn der Nutzer die taste "i" drückt, dann zeige die Speaker Notes an/ verstecke sie wieder
  document.addEventListener("keydown", (event) => {
    if (event.key === "i") {
      updateNotesOverlay();
      notesOverlay.classList.toggle("is-active");
    }
  });
} );

Reveal.on('slidechanged', event => {

  updateNotesOverlay();
  addCopyToClipboard();
  reorderFooter();

  fitTextElements.forEach(ele=>{
    window.fitText( ele );
  });

  const BUs = event.currentSlide.querySelectorAll(".bu");
  BUs.forEach(bu => {
    bu.classList.add("is-active");
  });

  const parentBadges = event.currentSlide.parentNode.querySelectorAll(".badge");
  const childBadges = event.currentSlide.querySelectorAll(".badge");

  const badges = childBadges.length > 0 ? childBadges : parentBadges;

  badges.forEach(badge => {
    badge.classList.add("is-active");
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