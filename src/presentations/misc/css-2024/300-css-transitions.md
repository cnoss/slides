---
title: CSS Transitions
layout: presentation.11ty.js
slideClasses: wrap
transition: fade
status: ok
footer: |
  - [Using CSS transitions, MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_transitions/Using_CSS_transitions)
  - [An Interactive Guide to CSS Transitions](https://www.joshwcomeau.com/animation/css-transitions/)
text1: |
  CSS transitions provide a way to control animation speed when changing CSS properties. 
  
  Instead of having property changes take effect immediately, you can cause the changes in a property to take place over a period of time. With CSS transitions enabled, changes occur at time intervals that follow an acceleration curve, all of which can be customized.
codeExample1: |
  div {
    transition: <property> <duration> <timing-function> <delay>;
  }

  /**/
  div {
    transition: 
      <property> <duration> <timing-function> <delay>, 
      <property> <duration> <timing-function> <delay>;
  }
codeExample2: |
  a{
    transition: background-color 1s ease-in-out 0s;
    background-color: orange;
    /**/
    &:hover{
      background-color: #dd1166;
    }
  }
---

{% interlude "CSS Transitions","[Baseline since ~2019](https://caniuse.com/css-transitions)" %}
{% simpleText "CSS Transitions", text1 %}
{% codeSmall "CSS Transitions", "Outline einer CSS Transition.", codeExample1, "css", "fade" %}
{% codeSmall "CSS Transitions …", "… provide a way to control animation speed when **changing** CSS properties. [🛝](https://codepen.io/cnoss/pen/YzoXeXR)", codeExample2, "css", "fade" %}
