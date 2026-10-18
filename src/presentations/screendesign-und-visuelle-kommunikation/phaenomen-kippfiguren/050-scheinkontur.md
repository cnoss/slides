---
title: "Scheinkonturen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Was sehen Sie? Fast alle sehen ein weißes Dreieck, das über drei schwarzen Kreisen liegt, sogar etwas heller als der Hintergrund. Es gibt aber kein Dreieck, keine einzige Linie davon. Beim Weiterschalten rücken die Formen auseinander, das Dreieck verschwindet. Dann werden die Kreise geschlossen: Ohne die Aussparungen gibt es auch kein Dreieck.

  **Hintergrund**

  Gaetano Kanizsa, italienischer Psychologe, beschrieb die Scheinkonturen 1955. Das Gehirn ergänzt die einfachste Erklärung für die Aussparungen: ein Dreieck, das darüberliegt (Geschlossenheit, Prägnanz).
---

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Was sehen Sie?"}' %}
<path data-id="p0" d="M450,85 L487.5,150.0 A75,75 0 1,0 412.5,150.0 Z" fill="#231f20" />
<path data-id="p1" d="M615,370 L540.0,370.1 A75,75 0 1,0 577.4,305.1 Z" fill="#231f20" />
<path data-id="p2" d="M285,370 L322.6,305.1 A75,75 0 1,0 360.0,370.1 Z" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Etwas weiter auseinander"}' %}
<path data-id="p0" d="M450,43 L487.5,108.0 A75,75 0 1,0 412.5,108.0 Z" fill="#231f20" />
<path data-id="p1" d="M651,391 L576.0,391.1 A75,75 0 1,0 613.4,326.1 Z" fill="#231f20" />
<path data-id="p2" d="M249,391 L286.6,326.1 A75,75 0 1,0 324.0,391.1 Z" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Ohne Aussparungen: kein Dreieck"}' %}
<circle data-id="p0" cx="450" cy="85" r="75" fill="#231f20" />
<circle data-id="p1" cx="615" cy="370" r="75" fill="#231f20" />
<circle data-id="p2" cx="285" cy="370" r="75" fill="#231f20" />
{% endframe %}
