---
title: Kalt-Warm-Kontrast
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Farben wirken warm (Gelb, Orange, Rot) oder kalt (Blau, Blaugrün). Warme Farben scheinen nach vorne zu kommen, kalte zurückzutreten. Das lässt sich für Räumlichkeit und Hierarchie nutzen: Ein warmer Button auf kühler Fläche drängt nach vorn.

  Die Temperatur ist relativ: Ein Violett wirkt neben Rot kalt, neben Blau warm.

  Frage ans Publikum: Welche Apps setzen warme Akzente auf kühlem Grund?
---

{% interlude "Kalt-Warm-Kontrast" %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Warm auf kalt tritt nach vorne, kalt auf warm weicht zurück"}' %}
<rect data-id="bgl" x="50" y="60" width="390" height="380" fill="#2c6ea8" />
<rect data-id="ql" x="170" y="175" width="150" height="150" fill="#f2672e" />
<rect data-id="bgr" x="460" y="60" width="390" height="380" fill="#f2672e" />
<rect data-id="qr" x="580" y="175" width="150" height="150" fill="#2c6ea8" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Dasselbe Violett: neben Pink kühl, neben Blau warm"}' %}
<rect data-id="bgl" x="50" y="60" width="390" height="380" fill="#d6118f" />
<rect data-id="ql" x="170" y="175" width="150" height="150" fill="#7a3fd1" />
<rect data-id="bgr" x="460" y="60" width="390" height="380" fill="#2c6ea8" />
<rect data-id="qr" x="580" y="175" width="150" height="150" fill="#7a3fd1" />
{% endframe %}
