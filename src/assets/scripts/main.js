const fitTextElements = document.querySelectorAll(".js-fit-text");

Reveal.on('slidechanged', event => {
  fitTextElements.forEach(ele=>{
    window.fitText( ele );
  });

  const BUs = event.currentSlide.querySelectorAll(".bu");
  BUs.forEach(bu => {
    bu.classList.add("is-active");
  });

  const info = event.currentSlide.querySelector(".info");
  if (info) {
    info.addEventListener("click", (ev) => { 
      info.classList.toggle("is-active");
      event.currentSlide.querySelector("blockquote").classList.toggle("is-passive");
    });
  }

  if (!event.previousSlide) return;
  
  const lastBUs = event.previousSlide.querySelectorAll(".bu");
  lastBUs.forEach(bu => {
    bu.classList.remove("is-active");
  });
} );