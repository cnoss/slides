---
title: "Zwei Punkte"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  **Live-Test (ca. 3 Minuten)**

  Dreimal dieselben zwei Punkte. Sie leuchten abwechselnd auf, nur das Tempo ändert sich.

  1. **Langsam** (Takt 2 Sekunden): zwei Punkte, die nacheinander blinken. Niemand sieht Bewegung.
  2. **Mittel** (jeder Punkt ca. 90 ms an, ca. 60 ms Pause): Ein Punkt springt hin und her. Fast alle sehen Bewegung, manche sogar die Strecke dazwischen.
  3. **Sehr schnell** (Takt 40 ms): beide Punkte gleichzeitig, leicht flimmernd. Keine Bewegung mehr.

  Bei jeder Folie fragen: Was sehen Sie? Auf dem Beamer kann das Tempo je nach Bildwiederholrate etwas abweichen. Die mittlere Folie ist die wichtige.

  Die Animation ist reines CSS. Ist im Betriebssystem »Bewegung reduzieren« aktiviert, stehen beide Punkte still. Für die Vorlesung die Einstellung am Präsentationsrechner ausschalten.
---

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Langsam: Was sehen Sie?"}' %}
<style>@keyframes phi-a-1{0%,29.9%{opacity:1}30%,100%{opacity:0}}@keyframes phi-b-1{0%,49.9%{opacity:0}50%,79.9%{opacity:1}80%,100%{opacity:0}}.phi-a-1{animation:phi-a-1 2s linear infinite}.phi-b-1{animation:phi-b-1 2s linear infinite}@media (prefers-reduced-motion: reduce){.phi-a-1,.phi-b-1{animation:none}}</style>
<circle data-id="pa" class="phi-a-1" cx="330" cy="250" r="36" fill="#231f20" />
<circle data-id="pb" class="phi-b-1" cx="570" cy="250" r="36" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Schneller: Und jetzt?"}' %}
<style>@keyframes phi-a-2{0%,29.9%{opacity:1}30%,100%{opacity:0}}@keyframes phi-b-2{0%,49.9%{opacity:0}50%,79.9%{opacity:1}80%,100%{opacity:0}}.phi-a-2{animation:phi-a-2 300ms linear infinite}.phi-b-2{animation:phi-b-2 300ms linear infinite}@media (prefers-reduced-motion: reduce){.phi-a-2,.phi-b-2{animation:none}}</style>
<circle data-id="pa" class="phi-a-2" cx="330" cy="250" r="36" fill="#231f20" />
<circle data-id="pb" class="phi-b-2" cx="570" cy="250" r="36" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Sehr schnell: Und jetzt?"}' %}
<style>@keyframes phi-a-3{0%,29.9%{opacity:1}30%,100%{opacity:0}}@keyframes phi-b-3{0%,49.9%{opacity:0}50%,79.9%{opacity:1}80%,100%{opacity:0}}.phi-a-3{animation:phi-a-3 40ms linear infinite}.phi-b-3{animation:phi-b-3 40ms linear infinite}@media (prefers-reduced-motion: reduce){.phi-a-3,.phi-b-3{animation:none}}</style>
<circle data-id="pa" class="phi-a-3" cx="330" cy="250" r="36" fill="#231f20" />
<circle data-id="pb" class="phi-b-3" cx="570" cy="250" r="36" fill="#231f20" />
{% endframe %}
