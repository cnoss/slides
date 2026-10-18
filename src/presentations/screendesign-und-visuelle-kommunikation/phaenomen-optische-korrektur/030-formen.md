---
title: "Kreis, Quadrat, Dreieck"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Quadrat, Kreis und Dreieck, alle exakt gleich hoch. Fragen: Sind sie gleich groß? Der Kreis wirkt kleiner, das Dreieck noch kleiner. Grund: Das Quadrat füllt die ganze Höhe auf voller Breite, Kreis und Dreieck berühren die Hilfslinien nur in einem Punkt.

  Korrektur: Kreis und Dreieck werden etwas größer gezeichnet und ragen über die Linien hinaus. In der Typografie heißt das Überhang (englisch Overshoot): Ein O ist höher als ein H, ein A spitzer und höher, damit alle Buchstaben gleich groß wirken. Bei Schriften sind das wenige Prozent.
---

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Gleich hoch. Gleich groß?"}' %}
<rect data-id="q" x="90" y="150" width="200" height="200" fill="#231f20" />
<circle data-id="c" cx="450" cy="250.0" r="100" fill="#231f20" />
<polygon data-id="t" points="710,150 825.0,350 595.0,350" fill="#231f20" />
<line data-id="g1" x1="40" y1="150" x2="860" y2="150" stroke="#9313ce" stroke-width="2" stroke-linecap="round" opacity="1" />
<line data-id="g2" x1="40" y1="350" x2="860" y2="350" stroke="#9313ce" stroke-width="2" stroke-linecap="round" opacity="1" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Korrigiert: Kreis und Dreieck ragen über die Linien und wirken jetzt gleich groß"}' %}
<rect data-id="q" x="90" y="150" width="200" height="200" fill="#231f20" />
<circle data-id="c" cx="450" cy="250.0" r="108" fill="#231f20" />
<polygon data-id="t" points="710,126 839.4,356 580.6,356" fill="#231f20" />
<line data-id="g1" x1="40" y1="150" x2="860" y2="150" stroke="#9313ce" stroke-width="2" stroke-linecap="round" opacity="1" />
<line data-id="g2" x1="40" y1="350" x2="860" y2="350" stroke="#9313ce" stroke-width="2" stroke-linecap="round" opacity="1" />
{% endframe %}
