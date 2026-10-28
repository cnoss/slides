---
title: "Gute Gestalt"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Zweimal dasselbe Spiel. Erst fragen: Was sehen Sie? Fast alle sagen: zwei Kreise, die sich überlagern. Genauso gut könnten es drei Flächen sein, zwei Monde und eine Linse, die zufällig aneinanderstoßen. Diese Lesart wählt kaum jemand, weil zwei Kreise die einfachere Erklärung sind.

  Bei den Quadraten genauso: Zwei Quadrate, eines davon gedreht. Man könnte auch ein Achteck mit acht Dreiecken sehen oder einen Stern. Die zweite Fassung zeigt nur die Dreiecke: Jetzt sehen viele einen Stern, aber kaum jemand kommt von selbst darauf, wenn die Quadrate komplett sind.

  **Hintergrund**

  Die Beispiele folgen klassischen Abbildungen zum Gesetz der guten Gestalt (Wertheimer 1923) und sind dem bisherigen Foliensatz nachempfunden.
---

{% frame '{"stage":"#ffffff", "w":600, "h":600, "bu":"Was sehen Sie?"}' %}

<circle data-id="k1" cx="240" cy="300" r="110" fill="none" stroke="#231f20" stroke-width="5" />
<circle data-id="k2" cx="360" cy="300" r="110" fill="none" stroke="#231f20" stroke-width="5" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":600, "h":600, "bu":"Genauso möglich: drei Flächen. Sieht aber kaum jemand."}' %}

<path data-id="t1" d="M 300,207.8 A 110 110 0 1 0 300,392.2 A 110 110 0 0 1 300,207.8 Z" fill="#231f20" transform="translate(-50 0)" />
<path data-id="t2" d="M 300,207.8 A 110 110 0 0 0 300,392.2 A 110 110 0 0 0 300,207.8 Z" fill="#9313ce" />
<path data-id="t3" d="M 300,207.8 A 110 110 0 1 1 300,392.2 A 110 110 0 0 0 300,207.8 Z" fill="#231f20" transform="translate(50 0)" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":600, "h":600, "bu":"Und hier?"}' %}

<rect data-id="q1" x="180" y="180" width="240" height="240" fill="none" stroke="#231f20" stroke-width="5" stroke-linejoin="round" />
<polygon data-id="q2" points="300,130.3 469.7,300 300,469.7 130.3,300" fill="none" stroke="#231f20" stroke-width="5" stroke-linejoin="round" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":600, "h":600, "bu":"Acht Dreiecke um ein Achteck: genauso möglich. Wir sehen zwei Quadrate."}' %}
<polygon data-id="d0" points="300,130.3 349.7,180 250.3,180" fill="#231f20" />
<polygon data-id="d1" points="469.7,300 420,349.7 420,250.3" fill="#231f20" />
<polygon data-id="d2" points="300,469.7 250.3,420 349.7,420" fill="#231f20" />
<polygon data-id="d3" points="130.3,300 180,250.3 180,349.7" fill="#231f20" />
<polygon data-id="d4" points="180,180 250.3,180 180,250.3" fill="#231f20" />
<polygon data-id="d5" points="420,180 420,250.3 349.7,180" fill="#231f20" />
<polygon data-id="d6" points="420,420 349.7,420 420,349.7" fill="#231f20" />
<polygon data-id="d7" points="180,420 180,349.7 250.3,420" fill="#231f20" />
{% endframe %}
