---
title: Über den Workshop
layout: presentation.11ty.js
slideClasses: images
status: ok

ziele: |
  - Wie können Daten zwischen Fenstern ausgetauscht werden?
  - Wie lassen sich diese Ansätze mit p5.js sinnvoll verbinden?
  - Was lässt sich gestalterisch damit machen? 🧐
  - bissl Spaß haben 👻

toc: |
  <div class="fragment is-unbalanced"><em>Zielbild:</em> Wo geht die Reise hin?</div>
  <div class="fragment is-unbalanced"><em>Szenarien:</em> Kleiner konzeptioneller Unterbau</div>
  <div class="fragment is-unbalanced"><em>Sharing Data:</em> Verschiedene Ansätze zum Austausch von Daten zwischen Fenstern. <strong>mit Übung</strong></div>
  <div class="fragment is-unbalanced"><em>Working with p5.js:</em> Kleiner Rundflug über p5.js</div>  
  <div class="fragment is-unbalanced"><em>Code-Code-Code:</em> Aufgaben zum selber coden 🎊</div>
  <div class="fragment is-unbalanced"><em>Rückblick/ Ausblick:</em> Was war – was geht?</div>

material: |
  - [Dokumentation](https://cnoss.github.io/multi-window-experiences/)
  - [Repo](https://github.com/cnoss/multi-window-experiences)
  - [Slidedeck](https://cnoss.github.io/slides/presentations/misc/multi-window-with-p5/)


disclaimer: |
  <div class="fragment">Wir werden die meisten Konzepte & Techniken nur sehr oberflächlich behandeln.</div>
  <div class="fragment">Der Code ist teils leider recht umfassend und unübersichtlich.</div>
  <div class="fragment">Für p5.js wird uns Repertoire fehlen. 😢</div>
  <div class="fragment">Babylonisches Sprachgewirr 😱</div>
  <div class="fragment">Die meisten Konzepte & Techniken hab ich noch nie in der Hand gehabt oder gar ernsthaft genutzt. 🧐</div>

disclaimer2: |
  <div class="fragment">Es wurden keine Performance Messungen vorgenommen.</div>
  <div class="fragment">Wir befassen uns nur mit <strong>zwei</strong> Fenstern.</div>
  <div class="fragment">Insgesamt ist sehr wenig getestet worden, insbesondere wurden kaum Cross-Browser Tests gemacht.</div>
  <div class="fragment">Nicht alle sinnvollen Ansätze werden in einem Sketch(?) zusammen gebracht, z.B. Physics & Multi-Window</div>
  <div class="fragment">Alle Implementierungen versuchen möglichst nah an Standards zu sein.</div>

playgrounds: |
  <a href="https://cnoss.github.io/multi-window-experiences/02-single-window-simple-object-example/index.html">Single Window, Simple Object</a> // <a href="https://cnoss.github.io/multi-window-experiences/03-single-window-complex-object-example/index.html">Single Window, Complex Object</a> // <a href="https://cnoss.github.io/multi-window-experiences/04-multi-window-simple-object-example/index.html">Multi-Window, Simple Object</a> // <a href="https://cnoss.github.io/multi-window-experiences/05-multi-window-complex-object-example/index.html">Multi-Window, Complex Object</a> // <a href="https://cnoss.github.io/multi-window-experiences/06-rotating-circles-example/index.html">Rotating Circles</a> // <a href="https://cnoss.github.io/multi-window-experiences/07-handoff-example/index.html">Casting</a>

---

{% interlude "<del>Checkin?</del> 😢", "", '{"transition":"none"}'  %}
{% question "💪 😵‍💫 😖 💪 💪 🏃‍♂️ 😖 🌀 🏃 💪", "Mein Weg zu diesem Workshop" %}
{% question "Was meint *Multi-Window* Experiences?" %}
{% screenshotFs "./images/01-cover-bjorn-stall.jpg", '{"transition":"fade", "classes":"no-shadow", "bu":"[Beispiel von Björn Staal](https://80.lv/articles/a-programmer-presents-a-mind-blowing-multi-window-adaptive-experience)<br>[GitHub Repo](https://github.com/bgstaal/multipleWindow3dScene)<br>[Demo](https://bgstaal.github.io/multipleWindow3dScene/)<br>[Video](https://www.youtube.com/watch?v=4LwHH3r2qNY)"}', 'fade' %}

{% simpleText "Ziele des Workshops", ziele, '{"transition":"slide"}'  %}
{% simpleText "Wie kommen wir dahin?", toc, '{"transition":"slide"}'  %}
{% simpleText "Material", material, '{"transition":"slide"}'  %}

{% simpleText "Disclaimer ⚠️", disclaimer, '{"transition":"slide"}'  %}
{% simpleText "Disclaimer, Teil 2 ‼️", disclaimer2, '{"transition":"slide"}'  %}
{% question "Wohin geht es?", playgrounds, '{"transition":"slide"}'  %}


