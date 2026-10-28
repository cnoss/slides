---
title: "Auf dem Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Drei Mittel gegen gefühlte Wartezeit, alle aus dem Alltag:

  **Skeleton Screens:** Platzhalter in der Form des Inhalts, wie eben gesehen. Verbreitet in Feeds, Shops und Videoplattformen.

  **Fortschrittsanzeige:** Bei längeren Vorgängen (Upload, Installation, Bezahlung) zeigt sie, dass etwas passiert und wie lange es noch dauert. Ein Balken, der am Anfang schneller läuft und am Ende langsamer, wirkt länger als einer, der sich am Ende beschleunigt (Harrison u. a., 2007, aus dem Gedächtnis, bitte prüfen).

  **Optimistische Oberfläche:** Das Herz wird sofort gefüllt, wenn man tippt. Der Server antwortet erst später. Geht etwas schief, wird die Änderung zurückgenommen und erklärt. Die Reaktion fühlt sich unmittelbar an, weil sie unter 0,1 Sekunden liegt.

  Frage zum Schluss: Wo warten Sie in Ihrer meistgenutzten App? Und was sehen Sie dabei?
---

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Fortschritt zeigen: Es passiert etwas, und es dauert noch so lange"}' %}

<rect data-id="bar-bg" x="250" y="236" width="400" height="28" rx="14" fill="#e4e4e4" />
<rect data-id="bar" x="250" y="236" width="120" height="28" rx="14" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Fortschritt zeigen: Es passiert etwas, und es dauert noch so lange"}' %}

<rect data-id="bar-bg" x="250" y="236" width="400" height="28" rx="14" fill="#e4e4e4" />
<rect data-id="bar" x="250" y="236" width="300" height="28" rx="14" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Optimistisch reagieren: Vor dem Tippen"}' %}

<path data-id="herz" d="M 450 300 C 430 280 380 250 380 205 C 380 175 405 155 430 160 C 440 162 447 168 450 176 C 453 168 460 162 470 160 C 495 155 520 175 520 205 C 520 250 470 280 450 300 Z" fill="#ffffff" stroke="#231f20" stroke-width="8" stroke-linejoin="round" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Sofort gefüllt. Der Server antwortet später."}' %}

<path data-id="herz" d="M 450 300 C 430 280 380 250 380 205 C 380 175 405 155 430 160 C 440 162 447 168 450 176 C 453 168 460 162 470 160 C 495 155 520 175 520 205 C 520 250 470 280 450 300 Z" fill="#9313ce" stroke="#9313ce" stroke-width="8" stroke-linejoin="round" />
{% endframe %}

{% question "Wo warten Sie in Ihrer meistgenutzten App?", "Und was sehen Sie, während Sie warten?" %}
