---
title: CSS Animations
layout: presentation.11ty.js
slideClasses: wrap
status: ok
footer: |
  - [Using CSS animations, MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations/Using_CSS_animations)
text1: |
  CSS animations make it possible to animate transitions from one CSS style configuration to another. Animations consist of two components: a *style describing the CSS animation* and a *set of keyframes* that indicate the start and end states of the animation's style, as well as possible intermediate waypoints.
codeExample1: |
  .card {
    animation-duration: 3s;
    animation-name: slidein;
  }
  /**/
  @keyframes slidein {
    from {
      translate: 150vw 0;
    }
  /**/
    to {
      translate: 0 0;
    }
  }
codeExample2: |
  @keyframes slidein {
    0% {
      translate: 150vw 0;
    }
  /**/
    50% {
      translate: -10vw 0;
    }
  /**/
    100% {
      translate: 0 0;
    }
  }
---

{% interlude "CSS Animations" %}
{% simpleText "CSS Animations", text1 %}
{% codeSmall "CSS Animations", "Outline einer CSS Animation.", codeExample1, "css", "fade" %}
{% codeSmall "CSS Animations", "How to gain more control? [🛝](https://codepen.io/cnoss/pen/YzoXeXR)", codeExample2, "css", "fade" %}
