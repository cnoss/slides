---
title: CSS Nesting
layout: presentation.11ty.js
slideClasses: images
transition: fade
status: ok
footer: |
  - [CSS Nesting Module, W3C, 25/06/2024](https://drafts.csswg.org/css-nesting/)
  - [CSS Nesting, MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_nesting)
text1: |
  The CSS nesting module defines a syntax for nesting selectors, providing the ability to nest one style rule inside another, with the selector of the child rule relative to the selector of the parent rule.
text2: |
  CSS nesting is different from CSS preprocessors such as Sass in that it is parsed by the browser rather than being pre-compiled by a CSS preprocessor.
text3: |
  CSS nesting helps with the readability, modularity, and maintainability of CSS stylesheets. It also potentially helps reduce the size of CSS files, thereby decreasing the amount of data downloaded by users.  
code: |
  <body>
    <header>
      <h1>Hello World</h1>
      <p>Kleiner Text der eigentlich keine Aussage hat.</p>
    </header>
    <p>
      Weiterer sinnloser Text, der nichts aussagt.
    </p>
  </body>
code2: |
  header{
    background-color: purple;
    /**/
    h1{
      font-size: 2rem;
    }
    h1, p{
      color: white;
    }
  }
---

{% interlude "CSS Nesting","[Baseline since April 2023](https://caniuse.com/?search=nesting)" %}
{% simpleText "CSS Nesting", text1, "fade" %}
{% simpleText "CSS Nesting", text2, "fade"  %}
{% simpleText "CSS Nesting", text3  %}

{% codeSmall "CSS Nesting", ".", code, "html", "fade" %}
{% codeSmall "CSS Nesting …", "… erlaubt verschachtelte CSS Anweisungen.", [{code: code, lang: "html"}, {code: code2, lang: "css"}], "css", "fade" %}