---
title: Quantitätskontrast
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Kontrast durch die Menge, also die Fläche, die eine Farbe einnimmt. Wenig von einer Farbe in viel von einer anderen lenkt den Blick. Goethe hat Farben Lichtwerte zugeordnet (Gelb 9, Orange 8, Rot und Grün 6, Blau 4, Violett 3). Ein ausgewogenes Verhältnis entsteht, wenn helle Farben weniger Fläche bekommen: Gelb zu Violett etwa 1 zu 3. Itten übernimmt das in »Kunst der Farbe«.

  Für das Screendesign ist der Gedanke wichtiger als die Zahlen: Die Akzentfarbe wirkt, weil sie wenig Fläche hat. Als Faustregel kursiert die 60-30-10-Regel aus der Innenarchitektur: 60 Prozent Grundfarbe, 30 Prozent Zweitfarbe, 10 Prozent Akzent.

  Beispiel: Caterpillar setzt Gelb sparsam auf viel Schwarz und Weiß.
---

{% interlude "Quantitätskontrast" %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Gelb und Violett zu gleichen Teilen: Gelb dominiert"}' %}
<rect data-id="v" x="50" y="60" width="400" height="380" fill="#6a2fc2" />
<rect data-id="y" x="450" y="60" width="400" height="380" fill="#f7d117" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Gelb zu Violett etwa 1 zu 3: im Gleichgewicht"}' %}
<rect data-id="v" x="50" y="60" width="600" height="380" fill="#6a2fc2" />
<rect data-id="y" x="650" y="60" width="200" height="380" fill="#f7d117" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Wenig Gelb in viel Violett: Der Blick findet sofort das Gelb"}' %}
<rect data-id="v" x="50" y="60" width="800" height="380" fill="#6a2fc2" />
<rect data-id="y" x="400" y="220" width="100" height="60" fill="#f7d117" />
{% endframe %}
{% screenshot "./images/kontrast-cat.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Gelb als kleiner Anteil auf viel Schwarz und Weiß<br><small>cat.com, Screenshot 2026</small>"}' %}
