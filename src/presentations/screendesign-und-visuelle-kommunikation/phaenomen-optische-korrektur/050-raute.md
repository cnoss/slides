---
title: "Quadrat gegen Raute"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Zweimal dasselbe Quadrat, einmal um 45 Grad gedreht. Die Raute wirkt deutlich größer. Ihre Diagonale ist etwa 1,4-mal so lang wie die Seite des Quadrats, und genau die sieht man als Höhe und Breite.

  Korrektur: Die Raute verkleinern, bis sie gleich groß wirkt. Praktisch bei Icons und Aufzählungszeichen: Ein Rauten-Icon braucht weniger Fläche als ein Quadrat-Icon.
---

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Dasselbe Quadrat, gedreht. Gleich groß?"}' %}
<rect data-id="q" x="150" y="150" width="200" height="200" fill="#231f20" />
<polygon data-id="r" points="650,108.6 791.4,250 650,391.4 508.6,250" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Korrigiert: Die Raute ist kleiner und wirkt jetzt gleich groß"}' %}
<rect data-id="q" x="150" y="150" width="200" height="200" fill="#231f20" />
<polygon data-id="r" points="650,129.8 770.2,250 650,370.2 529.8,250" fill="#231f20" />
{% endframe %}
