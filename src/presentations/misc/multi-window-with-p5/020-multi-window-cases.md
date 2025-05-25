---
title: Multi Window Cases
layout: presentation.11ty.js
slideClasses: images
transition: slide
status: ok

ziele: |
  - Wie können Daten zwischen Fenstern ausgetauscht werden?
  - Wie lassen sich diese Ansätze mit p5.js sinnvoll verbinden?
  - Was lässt sich gestalterisch damit machen? 🧐
  - bissl Spaß haben 👻

disclaimer: |
  <div class="fragment">Wir werden die meisten Konzepte & Techniken nur sehr oberflächlich behandeln.</div>
  <div class="fragment">Der Code ist teils leider recht umfassend und unübersichtlich.</div>
  <div class="fragment">Für p5.js wird uns Repertoire fehlen. 😢</div>
  <div class="fragment">Die meisten Konzepte & Techniken hab ich noch nie in der Hand ernsthaft genutzt. 😱</div>
---

{% question "Welche *Multi-Window*-Cases könnten betrachtet werden?" %}
{% screenshotFs "./images/multi-window-1.png", '{"transition":"fade-in", "classes":"no-shadow", "bu":"Position on Screen"}' %}
{% screenshotFs "./images/multi-window-2.png", '{"transition":"fade-in", "classes":"no-shadow", "bu":"Multiple Windows"}' %}
{% screenshotFs "./images/multi-window-2a.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Distance"}' %}
{% screenshotFs "./images/multi-window-2b.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Angle"}' %}
{% screenshotFs "./images/multi-window-2c.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Right or left"}' %}
{% screenshotFs "./images/multi-window-2d.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Intersection"}' %}
{% screenshotFs "./images/multi-window-2e.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Overlap & Casting"}' %}
{% screenshotFs "./images/multi-screen.png", '{"transition":"fade", "classes":"no-shadow", "bu":"Multi Screen"}' %}

{% interlude "Checkin?", "", '{"transition":"none"}'  %}

{% screenshotFs "./images/01-cover-bjorn-stall.jpg", '{"transition":"fade", "classes":"no-shadow", "bu":"[Beispiel von Björn Staal](https://80.lv/articles/a-programmer-presents-a-mind-blowing-multi-window-adaptive-experience)<br>[GitHub Repo](https://github.com/bgstaal/multipleWindow3dScene)<br>[Demo](https://bgstaal.github.io/multipleWindow3dScene/)<br>[Video](https://www.youtube.com/watch?v=4LwHH3r2qNY)"}', 'fade' %}
{% simpleText "Ziele des Workshops", ziele, '{"transition":"none"}'  %}
{% simpleText "Disclaimer ⚠️", disclaimer, '{"transition":"none"}'  %}
{% interlude "Demo", "", '{"transition":"slide"}'  %}


