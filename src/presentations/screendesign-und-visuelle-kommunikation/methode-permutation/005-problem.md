---
title: "Das Problem"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  Ein einziges Modul: ein Quadrat mit einem Viertelring in der Ecke. Frage ans Publikum: Wie viele verschiedene Formen stecken darin?

  Die meisten denken zuerst an eine Handvoll. Tatsächlich reicht schon ein Feld aus 2 × 2 Kacheln mit vier möglichen Drehungen pro Kachel für 4 hoch 4, also 256 Kombinationen. Bei einem Feld aus 6 × 6 Kacheln sind es mehr, als man je ausprobieren könnte.

  Das Problem ist also nicht, dass es zu wenige Möglichkeiten gibt, sondern zu viele. Wer ohne Regel probiert, landet beim Zufall oder bei der ersten Variante, die halbwegs gefällt. Permutation ist das Verfahren, mit dem man diesen Raum systematisch durchquert.
---

{% frame '{"stage":"#ffffff", "animate":false, "w":600, "h":600, "bu":"Ein Modul"}' %}
<g data-id="k0" transform="translate(300.0,300.0) rotate(0) translate(-100.0,-100.0)"><rect x="0" y="0" width="200" height="200" fill="#d9d9d9" /><path d="M 136.0,0 A 136.0 136.0 0 0 1 0,136.0 L 0,100.0 A 100.0 100.0 0 0 0 100.0,0 Z" fill="#231f20" /><path d="M 100.0,0 A 100.0 100.0 0 0 1 0,100.0 L 0,64.0 A 64.0 64.0 0 0 0 64.0,0 Z" fill="#9313ce" /></g>
{% endframe %}

{% statement "Ein Modul, unendlich viele Formen.", "Das Problem ist nicht, dass es zu wenige Möglichkeiten gibt, sondern zu viele. Permutation bringt eine Regel ins Spiel." %}
