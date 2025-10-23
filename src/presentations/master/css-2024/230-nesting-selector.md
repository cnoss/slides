---
title: CSS Nesting Selector &
layout: presentation.11ty.js
slideClasses: wrap
transition: fade
status: ok
footer: |
  - [& nesting selector, MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Nesting_selector)
text1: |
  The CSS & nesting selector explicitly states the relationship between parent and child rules when using CSS nesting.
text2: |
  … erlaubt direkte Referenzierung des Elternselektors. [🛝](https://sass-lang.com/playground/#eJxtjrEKwzAMRHd/habQBurgoYvzNY6tJsGuFeSkFEr+vbHdJdBBcJLuHaeUnJDpIwCkNeyyABiM9SPTFt3NUiDWsMzR9+XXtTAwGg9tV/ZGT/RCruA/dGTEWNld5DknnPiVTUwP4qeGZE3Ai5Lq2hcqNzwuvELzK0ns8MhPFGYHjA7uy7t6d/EFPHs9MA==)

codeExample1: |
  .hero{
    .card{
      background-color: pink;
      /**/
      &:hover{
        background-color: green;
      }
    }
  /**/
    &:hover{
      transform: scale(1.1);
    }
  }

codeExample2: |
  .hero .card{
    background-color: pink;
  }
  /**/
  .hero .card:hover{
    background-color: green;
  }
  /**/
  .hero:hover{
    transform: scale(1.1);
  }

---

{% simpleText "CSS Nesting Selector &", text1 %}
{% codeSmall "Der CSS Nesting Selector …", text2, [{code: codeExample1, lang: "css"}, {code: codeExample2, lang: "css"}], "css", "fade" %}