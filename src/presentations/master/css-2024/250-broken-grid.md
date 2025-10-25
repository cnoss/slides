---
title: Broken Grid via CSS Grid
layout: presentation.11ty.js
slideClasses: wrap
status: ok
footer: |
  - [CSS Grid Layouts, MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout)
  - [A Complete Guide to CSS Grid, CSS Tricks](https://css-tricks.com/snippets/css/complete-guide-grid/)

introtext: |
  The CSS grid layout module excels at dividing a page into major regions or defining the relationship in terms of size, position, and layer, between parts of a control built from HTML primitives. Like tables, grid layout enables an author to align elements into columns and rows. 

text1: |
  Outline of a simple grid. [🛝](https://codepen.io/cnoss/pen/poXJXeV)

text2: |
  Adding «brokeability». [🛝](https://codepen.io/cnoss/pen/poXJXeV)


codeExample1: |
  .grid{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 1rem;
  }

codeExample2: |
  .grid{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 1rem;
    
    grid-template-rows: 1fr 1fr 1fr;
    grid-auto-rows: auto;
  }

  .element-1{
    grid-column: 1 / 3;
    grid-row: 1 / 3;
  }

---

{% interlude "Broken Grid via CSS Grid", "[Global Availability > 97%](https://caniuse.com/css-grid)" %}
{% screenshotFs "./images/broken-grid-00.jpg", '{"transition":"fade", "classes":"no-shadow", "bu":"[Broken Grid](https://blog.hubspot.com/website/broken-grid-layouts) Example"}', 'fade' %}
{% simpleText "CSS Grid Layout", introtext %}
{% codeSmall "CSS Grid Layout", text1, codeExample1, "css", "fade" %}
{% codeSmall "CSS Grid Layout", text2, codeExample2, "css", "fade" %}
{% simpleText "🕺🏼", "" %}


