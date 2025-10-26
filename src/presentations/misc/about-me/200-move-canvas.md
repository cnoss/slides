---
title: Fit Canvas to Screen Size
subtitle: 
layout: presentation.11ty.js
slideClasses: wrap
transition: slide
status: ok
footer: |
  - [Workshop Page](https://cnoss.github.io/multi-window-experiences/)
canvasCode: |
  let posX, posY;

  function draw() {
    background(0, 0, 0, 100);

    if (drawingParams.context === 'screen') {
      // Move the origin of the canvas to the top left corner of the screen
      const originX = -window.screenX;
      const originY = -window.screenY;
      canvas.width = screen.width;
      canvas.height = screen.height;
      translate(originX, originY);
      posX = width / 2;
      posY = height / 2;

    }else{
      posX = window.innerWidth / 2;
      posY = window.innerHeight / 2;
    }

    ellipse(posX, posY, 60, 60);
  }

canvasText: |
  This code adjusts the canvas based on the browser window’s position on the screen, allowing the sketch to stay aligned with the physical screen space.


---

{% interlude "Time to assemble.","Share Window Data Concepts & p5.js" %}

{% screenshotFs "./images/translate-canvas-1.png", '{"transition":"fade", "classes":"no-shadow", "bu":"In order to create a link between the sketch and the screen, we move and scale the canvas to the size of the screen."}' %}

{% screenshotFs "./images/translate-canvas-2.png", '{"transition":"fade", "classes":"no-shadow", "bu":"In order to create a link between the sketch and the screen, we move and scale the canvas to the size of the screen."}' %}

{% codeSmall "Fit Canvas to Screen Size", canvasText, canvasCode , "javascript", "slide" %}


