---
title: Custom Properties
subtitle: CSS Variables
layout: presentation.11ty.js
slideClasses: wrap
transition: fade
status: ok
footer: |
  - [Using CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)
  - [A Complete Guide to Custom Properties](https://css-tricks.com/a-complete-guide-to-custom-properties/)
code: |
  :root{
    --name: value;
  }
code2: |
  :root{
    --accent-color: #dd1166;
  }
  /* break */
  a{ 
    color: var(--accent-color);
  }
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

{% interlude "Custom Properties","[Baseline since April 2017](https://caniuse.com/css-variables)" %}
{% cite "Custom properties are entities defined by CSS authors that represent specific values to be reused throughout a document." %}
{% question "Was ist der Unterschied zwischen Custom Properties und [Sass Variables](https://sass-lang.com/playground/#eJxtTrsOgCAQ2+8rbtARI7rp15B4eCQIBpk0/rsiPhaHSy9t01bKQi/CqjBShw1NPRSWRTQjxw6lrMtMOB8mZU+mTQwwqYHCBogVU/DpQeQmI6L2LorFrGfkm97fmjWOBFMuuHqyssMF8/bn+yY85nQ7HNr0NEo=)?" %}

{% codeSmall "Custom Properties", "", code , "css", "fade" %}
{% codeSmall "Custom Properties", "Definiert wird via double dash. Anwenden via **var()**.", code2, "css", "fade" %}
{% codeSmall "Custom Properties …", "… können zur Laufzeit verändert werden. 😱🕺🏼", code3, "css", "fade" %}
{% codeSmall "Custom Properties …", "… können Custom Properties enthalten.", code4, "css", "fade" %}
{% codeSmall "Custom Properties …", "… können Custom Properties enthalten.", code5, "css", "fade" %}
