---
title: Bunt-Unbunt-Kontrast
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Bunte Farbe gegen Schwarz, Weiß und Grau. Im Screendesign der wichtigste Farbkontrast nach Hell-Dunkel: Die meisten Oberflächen sind unbunt, eine Farbe markiert, worauf es ankommt (Marke, Hauptaktion, Status). Genau so arbeiten auch die Grafiken in diesem Modul: Schwarz, Grau und ein Lila.

  Beispiele: Die TH Köln setzt Orange auf eine sonst unbunte Seite. Vue.js arbeitet fast nur mit Grau und Schwarz und markiert mit Grün.
---

{% interlude "Bunt-Unbunt-Kontrast" %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Eine bunte Farbe zwischen unbunten: sofort sichtbar"}' %}
<rect data-id="u0" x="50.0" y="150" width="117" height="200" fill="#d9d9d9" />
<rect data-id="u1" x="186.66666666666669" y="150" width="117" height="200" fill="#888888" />
<rect data-id="u2" x="323.33333333333337" y="150" width="117" height="200" fill="#d9d9d9" />
<rect data-id="u3" x="460.00000000000006" y="150" width="117" height="200" fill="#e8002a" />
<rect data-id="u4" x="596.6666666666667" y="150" width="117" height="200" fill="#d9d9d9" />
<rect data-id="u5" x="733.3333333333335" y="150" width="117" height="200" fill="#888888" />
{% endframe %}
{% screenshot "./images/kontrast-thkoeln.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Orange auf unbunter Fläche<br><small>th-koeln.de, Screenshot 2026</small>"}' %}
{% screenshot "./images/kontrast-vue.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Fast alles unbunt, Grün markiert Marke und Hauptaktion<br><small>vuejs.org, Screenshot 2026</small>"}' %}
