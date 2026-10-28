---
title: "Geschlossenheit"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Vier Winkel, weit auseinander: Man sieht vier Winkel. Rücken sie zusammen, sieht man ein Quadrat, obwohl jede Seite eine Lücke hat. Das Gehirn ergänzt die einfachste geschlossene Form. Dasselbe beim Kreis aus Bogenstücken.

  Wer im Phänomen Kippfiguren das Dreieck von Kanizsa gesehen hat, kennt den Effekt schon: Dort ergänzen wir sogar eine Kante, die gar nicht da ist.

  Das IBM-Logo: Die Streifen zerschneiden die Buchstaben, trotzdem lesen wir drei ganze Buchstaben. Entworfen von Paul Rand, in der heutigen Form mit acht Streifen seit 1972 (aus dem Gedächtnis, bitte prüfen). Viele Logos und Icons arbeiten mit Geschlossenheit: Sie lassen weg, was das Auge ohnehin ergänzt.

  **Hintergrund**

  Die Geschlossenheit hängt eng mit der Prägnanz zusammen (siehe Gestaltpsychologie): Wir sehen die einfachste und vollständigste Form, die zu den Reizen passt.
---

{% frame '{"stage":"#ffffff", "w":600, "h":600, "bu":"Vier Winkel"}' %}
  <polyline data-id="w0" points="180,110 110,110 110,180" fill="none" stroke="#231f20" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" />
  <polyline data-id="w1" points="420,110 490,110 490,180" fill="none" stroke="#231f20" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" />
  <polyline data-id="w2" points="180,490 110,490 110,420" fill="none" stroke="#231f20" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" />
  <polyline data-id="w3" points="420,490 490,490 490,420" fill="none" stroke="#231f20" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":600, "h":600, "bu":"Ein Quadrat. Obwohl alle Seiten Lücken haben"}' %}
  <polyline data-id="w0" points="260,190 190,190 190,260" fill="none" stroke="#231f20" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" />
  <polyline data-id="w1" points="340,190 410,190 410,260" fill="none" stroke="#231f20" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" />
  <polyline data-id="w2" points="260,410 190,410 190,340" fill="none" stroke="#231f20" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" />
  <polyline data-id="w3" points="340,410 410,410 410,340" fill="none" stroke="#231f20" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":600, "h":600, "bu":"Auch ein Kreis mit Lücken bleibt ein Kreis"}' %}
  <circle data-id="kreis" cx="300" cy="300" r="130" fill="none" stroke="#231f20" stroke-width="8" stroke-linecap="round" stroke-dasharray="70 32" />
{% endframe %}

{% screenshot "./images/ibm-logo.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Streifen statt Buchstaben, gelesen wird trotzdem IBM<br><small>IBM-Logo, Paul Rand, 1972</small>"}' %}
