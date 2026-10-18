---
title: Hell-Dunkel-Kontrast
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Der wichtigste Kontrast im Screendesign: Er trägt Lesbarkeit, Hierarchie und Form. Was in Graustufen nicht unterscheidbar ist, ist auch in Farbe schwer zu lesen. Gelb auf Weiß ist kaum zu sehen, Gelb auf Dunkel leuchtet.

  Prüfen: Graustufentest und Kontrastverhältnis nach WCAG (Methode Kontrast prüfen).

  Beispiel: JetBrains arbeitet mit einer dunklen Oberfläche, helle Schrift und einzelne leuchtende Flächen setzen sich deutlich ab.
---

{% interlude "Hell-Dunkel-Kontrast" %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Gelb auf Weiß: kaum Helligkeitsunterschied"}' %}
<rect data-id="bg" x="50" y="60" width="800" height="380" fill="#ffffff" />
<rect x="50" y="60" width="800" height="380" fill="none" stroke="#d9d9d9" stroke-width="2" />
<rect data-id="q" x="375" y="175" width="150" height="150" fill="#f7d117" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Gelb auf Dunkel: maximaler Hell-Dunkel-Kontrast"}' %}
<rect data-id="bg" x="50" y="60" width="800" height="380" fill="#231f20" />
<rect data-id="q" x="375" y="175" width="150" height="150" fill="#f7d117" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Hell-Dunkel ohne Farbe: Helligkeit allein trägt Form und Hierarchie"}' %}
<rect data-id="g0" x="50.0" y="150" width="117" height="200" fill="#000000" />
<rect data-id="g1" x="186.66666666666669" y="150" width="117" height="200" fill="#333333" />
<rect data-id="g2" x="323.33333333333337" y="150" width="117" height="200" fill="#666666" />
<rect data-id="g3" x="460.00000000000006" y="150" width="117" height="200" fill="#999999" />
<rect data-id="g4" x="596.6666666666667" y="150" width="117" height="200" fill="#cccccc" />
<rect data-id="g5" x="733.3333333333335" y="150" width="117" height="200" fill="#ffffff" />
<rect x="50" y="150" width="800" height="200" fill="none" stroke="#d9d9d9" stroke-width="2" />
{% endframe %}
{% screenshot "./images/kontrast-jetbrains.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Dunkle Fläche, helle Schrift, einzelne helle Akzente<br><small>jetbrains.com, Screenshot 2026</small>"}' %}
