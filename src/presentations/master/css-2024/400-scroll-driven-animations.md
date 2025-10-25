---
title: CSS Scroll Driven Animations
layout: presentation.11ty.js
slideClasses: wrap
status: ok
footer: |
  - [Scroll Driven Animations, Bramus Demo](https://scroll-driven-animations.style/)
  - [CSS scroll-driven animations, MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll-driven_animations)
text1: |
  The CSS scroll-driven animations module allows you to **animate property values** based on a progression **along a scroll-based timeline** instead of the default time-based document timeline. This means that you can **animate an element by scrolling a scrollable element**, rather than just by the passing of time.

  It is built on top of CSS animations module and Web Animations API.
examples: |
  All taken from [Bramus](https://www.bram.us) Demo.
  - [Reading Progress Indicator](https://scroll-driven-animations.style/demos/progress-bar/css/)
  - [Horizontal Scroll Section](https://scroll-driven-animations.style/demos/horizontal-section/css/)
  - [Image Reveal Effects](https://scroll-driven-animations.style/demos/image-reveal/css/)
  

advantages: |
  <ul class="colored-list">
    <li class="fragment">They're easy to use for simple animations; you can create them without even having to know JavaScript.</li>
    <li class="fragment">The animations run well, even under moderate system load. Simple animations can often perform poorly in JavaScript. The rendering engine can use frame-skipping and other techniques to keep the performance as smooth as possible.</li>
    <li class="fragment">Letting the browser control the animation sequence lets the browser optimize performance and efficiency by, for example, reducing the update frequency of animations running in tabs that aren't currently visible.</li>
  </ul>

codeExample1HTML: |
  <body>
    <div id="progress"></div>
    …
  </body>
codeExample1CSS: |
  html{
    scroll-timeline-name: --page-scroll;
  }
  /**/
  @keyframes grow-progress {  
    from { transform: scaleX(0); }
    to { transform: scaleX(1); }
  }
  /**/
  #progress {
    /* Styling Stuff */
    background-color: red;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 20px;
    transform-origin: 0 50%;
    /**/
    /* Animation Stuff */
    animation-timeline: --page-scroll;
    animation-duration: auto;
    animation-timing-function: linear;
    animation-name: grow-progress;
  }

codeExample2Keyframes: |
  @keyframes scale-in {
    from {
      opacity: 0;
      transform: scale(0);
    }
    to {
      opacity: 1; 
      transform: scale(1);
    }
  }
codeExample2Animation: |
  .scale-in {
    /* Create View Timeline */
    view-timeline-name: --appear-in-viewport;
    /**/
    /* Attach animation, linked to the  View Timeline */
    animation-name: scale-in;
    animation-timing-function: linear;
    animation-timeline: --appear-in-viewport;
    /**/  
    /* Tweak range when effect should run */
    animation-range: entry 25% cover 50%;
  }
---

{% interlude "Scroll-Driven Animations", "[Experimental Feature](https://caniuse.com/?search=scroll-timeline)" %}
{% simpleText "Scroll-Driven Animations", text1 %}
{% simpleText "Scroll-Driven Animations Examples", examples %}
{% simpleText "Advantages of SDA", advantages %}
{% codeSmall "Scroll-Driven Animations", "Outline einer Scroll-Driven Animation als Scroll-Timeline [🛝](https://codepen.io/cnoss/pen/VwJLxNB) am Beispiel eines [Reading Process Indicators](https://scroll-driven-animations.style/demos/progress-bar/css/). Der [Scroll Timeline Progress Visualizer](https://scroll-driven-animations.style/tools/scroll-timeline/progress/) und die [Chrome Extension](https://scroll-driven-animations.style/#debugger) unterstützen beim Verständnis.", [{code:codeExample1HTML, "lang": "html"}, {code:codeExample1CSS, "lang": "css"}], "css", "fade" %}
{% codeSmall "Scroll-Driven Animations", "Outline einer Scroll-Driven Animation als View-Timeline [🛝](https://codepen.io/cnoss/pen/QWXbVRw). Der [View Timeline Ranges Visualizer](https://scroll-driven-animations.style/tools/view-timeline/ranges/#range-start-name=cover&range-start-percentage=0&range-end-name=cover&range-end-percentage=100&view-timeline-axis=block&view-timeline-inset=0&subject-size=smaller&subject-animation=reveal&interactivity=clicktodrag&show-areas=yes&show-fromto=yes&show-labels=yes) unterstützt beim Verständnis.", [{code:codeExample2Keyframes, lang:"css"},{code:codeExample2Animation, lang:"css"}] , "css", "slide" %}
