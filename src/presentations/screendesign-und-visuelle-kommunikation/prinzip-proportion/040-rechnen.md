---
title: "Mit Verhältnissen rechnen"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  Zwei Verhältnisse, mit denen sich im Alltag arbeiten lässt.

  **Drittel:** Format in drei mal drei Felder teilen, Wichtiges auf eine Linie oder einen Schnittpunkt legen. Das ist eine vereinfachte Annäherung an den Goldenen Schnitt und aus der Fotografie bekannt. Ein Horizont genau in der Mitte wirkt oft starr, auf dem unteren Drittel ruhiger.

  **DIN A:** Die Formate der A-Reihe haben das Verhältnis 1 : √2, etwa 1 : 1,414. Halbiert man ein A-Blatt, hat die Hälfte wieder dasselbe Verhältnis. Darum wird aus A4 durch Falten A5. Festgelegt in DIN 476 (1922), international ISO 216.

  Die Zahlenreihen (Fibonacci, Renard) kommen im nächsten Abschnitt.

  Bildmaterial dazu im bisherigen Foliensatz Proportionen und Abstände. Angaben aus dem Gedächtnis, bitte prüfen.
---

{% interlude "Mit Verhältnissen rechnen", "Drittel und DIN A" %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "animate":false, "bu":"Drittel: Wichtiges auf eine Linie oder einen Schnittpunkt"}' %}
<rect x="150" y="50" width="600" height="400" fill="#e4e4e4" />
<rect x="150" y="316.7" width="600" height="133.3" fill="#c4c4c4" />
<circle cx="550.0" cy="183.3" r="38" fill="#231f20" />
<line x1="350.0" y1="50" x2="350.0" y2="450" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
<line x1="150" y1="183.3" x2="750" y2="183.3" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
<line x1="550.0" y1="50" x2="550.0" y2="450" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
<line x1="150" y1="316.7" x2="750" y2="316.7" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "animate":false, "bu":"DIN A: Halbiert bleibt das Verhältnis gleich, 1 : 1,414"}' %}
<rect x="150" y="40" width="594.0" height="420" fill="#d9d9d9" />
<line x1="447.0" y1="40.0" x2="447.0" y2="460.0" stroke="#231f20" stroke-width="3" stroke-linecap="round" />
<line x1="447.0" y1="250.0" x2="744.0" y2="250.0" stroke="#231f20" stroke-width="3" stroke-linecap="round" />
<line x1="595.5" y1="250.0" x2="595.5" y2="460.0" stroke="#231f20" stroke-width="3" stroke-linecap="round" />
<line x1="595.5" y1="355.0" x2="744.0" y2="355.0" stroke="#231f20" stroke-width="3" stroke-linecap="round" />
<line x1="669.7" y1="355.0" x2="669.7" y2="460.0" stroke="#231f20" stroke-width="3" stroke-linecap="round" />
<line x1="669.7" y1="407.5" x2="744.0" y2="407.5" stroke="#231f20" stroke-width="3" stroke-linecap="round" />
<rect x="669.7" y="407.5" width="74.2" height="52.5" fill="#9313ce" />
{% endframe %}
