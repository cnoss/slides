---
title: Separation of Concerns
layout: presentation.11ty.js
slideClasses: wrap
status: ok
leanWeb: |
  <blockquote>We keep throwing more JS at things in attempt to force the control we get in the backend onto the front end. But that’s not how it works. Trying to fight the nature of the medium is the source of a lot of the pain with modern web development.</blockquote>
  <small>Chris Ferdinandi // <a href="https://leanweb.dev/ebook/">The Lean Web</a></small>

embrace: |
  Rather than using dependencies or libraries, use the native JavaScript methods and Browser APIs that are baked right in for free whenever you can.<br>
  <small>Chris Ferdinandi // <a href="https://leanweb.dev/ebook/lean-web-principles/#principle-1-embrace-the-platform">Lean Web Principles</a></small>
---

{% question "What are the three basic building blocks of the web?" %}
{% question "What is the idea behind the concept «Separation of Concerns»?" %}
{% interlude "Separation of Concerns", "HTML, CSS, Javascript" %}
{% qa "Law of instrument", "The law of the instrument, law of the hammer, Maslow's hammer, or golden hammer is a cognitive bias that involves an over-reliance on a familiar tool. Abraham Maslow wrote in 1966, «If the only tool you have is a hammer, it is tempting to treat everything as if it were a nail.»" %}
{% statement "Greenfield vs. Brownfield", "oder: Woran erkenne ich ein erfolgreiches Web Projekt?" %}
{% simpleText "The Lean Web", leanWeb %}
{% simpleText "Embrace the Platform", embrace %}



