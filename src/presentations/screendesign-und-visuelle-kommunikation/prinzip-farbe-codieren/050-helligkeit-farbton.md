---
title: Helligkeit und Farbton
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Faustregel nach Colin Ware: Helligkeit für Details und Reihenfolgen, Farbton für Kategorien.

  Erste Grafik: Werte von wenig nach viel, codiert mit Regenbogenfarben. Frage: Welches Feld steht für »am meisten«? Niemand weiß es sicher, denn der Farbkreis hat keine Richtung. Zweite Grafik: dieselbe Reihe über die Helligkeit eines Farbtons. Die Reihenfolge ist sofort klar, auch in Graustufen.

  Umgekehrt gilt: Für Kategorien ohne Rangfolge (Kalender, Projekte, Abteilungen) ist der Farbton richtig. Helligkeitsstufen würden dort eine Rangfolge vortäuschen, die es nicht gibt.

  Praxis: Diagramme, Heatmaps und Status-Skalen mit Helligkeitsverläufen (»sequenzielle Paletten«), Kategorien mit gut unterscheidbaren Farbtönen (»qualitative Paletten«). Gute Vorlagen: ColorBrewer von Cynthia Brewer.
---

{% interlude "Helligkeit für Reihenfolgen.", "Farbton für Kategorien." %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Wenig bis viel, codiert mit Farbton: Welches Feld ist »am meisten«?"}' %}
<rect data-id="c0" x="80" y="170" width="115" height="160" rx="0" fill="#e8002a" />
<rect data-id="c1" x="205" y="170" width="115" height="160" rx="0" fill="#ff7a00" />
<rect data-id="c2" x="330" y="170" width="115" height="160" rx="0" fill="#f7d117" />
<rect data-id="c3" x="455" y="170" width="115" height="160" rx="0" fill="#1a8a3a" />
<rect data-id="c4" x="580" y="170" width="115" height="160" rx="0" fill="#2c6ea8" />
<rect data-id="c5" x="705" y="170" width="115" height="160" rx="0" fill="#6a2fc2" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Dieselbe Reihe über Helligkeit: sofort lesbar"}' %}
<rect data-id="c0" x="80" y="170" width="115" height="160" rx="0" fill="#f3e6fb" />
<rect data-id="c1" x="205" y="170" width="115" height="160" rx="0" fill="#dbb4f2" />
<rect data-id="c2" x="330" y="170" width="115" height="160" rx="0" fill="#c27fe8" />
<rect data-id="c3" x="455" y="170" width="115" height="160" rx="0" fill="#a74fdc" />
<rect data-id="c4" x="580" y="170" width="115" height="160" rx="0" fill="#8a1fc4" />
<rect data-id="c5" x="705" y="170" width="115" height="160" rx="0" fill="#5c0f86" />
{% endframe %}
