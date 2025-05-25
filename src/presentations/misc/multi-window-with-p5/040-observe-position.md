---
title: Observe Window Position
subtitle: 
layout: presentation.11ty.js
slideClasses: wrap
transition: slide
status: ok
footer: |
  - [Window: screenX property MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/screenX)
  - [Window: screenY property MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/screenY)
code: |
  console.log('Window position:', window.screenX, window.screenY);
code2: |
  const myWindowPosition = {
    x: false,
    y: false
  }
  /**/
  const trackMyWindowPosition = () => {
    if (myWindowPosition.x === window.screenX 
      && myWindowPosition.y === window.screenY) return;
    /**/
    myWindowPosition.x = window.screenX;
    myWindowPosition.y = window.screenY;
    /**/
    // Do something meaningful with the data 🕺🏼
    console.log(myWindowPosition.x, myWindowPosition.y);
  }
  /**/
  trackMyWindowPosition();
  const observeMyWindowPosition = setInterval(trackMyWindowPosition, 500);
  
code3: |
  .hero{
    --accent-color: white;
    /**/
    a{ 
      color: var(--accent-color);
    }
  }
code4: |
  :root{
    --darkest: #000;
    --lightest: #fff;
    /**/
    --background-color: var(--darkest);
    --foreground-color: var(--lightest);
  }
code5: |
  :root{
    --darkest: #000;
    --lightest: #fff;
    /**/
    --background-color: var(--darkest);
    --foreground-color: var(--lightest);
  }
  /**/
  body:has(.lightmode){
    --background-color: var(--lightest);
    --foreground-color: var(--darkest);
  }
---

{% interlude "Observe Window Position","No event listener is available 😢" %}

{% screenshotFs "./images/get-position.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Position on screen via [window.screenX](https://developer.mozilla.org/de/docs/Web/API/Window/screenX) & [window.screenY](https://developer.mozilla.org/de/docs/Web/API/Window/screenY)"}' %}

{% codeSmall "Step 1: Detect Window Position", "", code , "javascript", "slide" %}

{% codeSmall "Step 2: Observe Window Position", "", code2 , "javascript", "fade" %}

{% screenshotFs "./images/get-position.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Position on screen via [window.screenX](https://developer.mozilla.org/de/docs/Web/API/Window/screenX) & [window.screenY](https://developer.mozilla.org/de/docs/Web/API/Window/screenY)"}' %}

