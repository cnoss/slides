---
title: Grenzen
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Nicht jede Variable eignet sich für jede Aufgabe. Farbton unterscheidet Kategorien gut, Rangfolgen schlecht. Helligkeit und Größe zeigen Rangfolgen, suggerieren aber auch eine, wo keine ist. Quellen: Bertin, Sémiologie graphique; Ware, Visual Thinking for Information Design.

  Drei Beispiele, jeweils ungeeignet, dann geeignet. Bei jedem fragen, bevor aufgelöst wird.
---

{% statement "Nicht jede Variable kann alles", "Farbton unterscheidet Kategorien. Helligkeit und Größe zeigen eine Rangfolge. Wer Wichtigkeit über Farbton ausdrückt, wird oft nicht verstanden." %}

{% frame '{"w":900,"h":500,"bu":"Rangfolge über Farbton: Welcher Punkt ist am wichtigsten?"}' %}
  <circle data-id="r0" cx="170" cy="250" r="44" fill="#4952e1" />
  <circle data-id="r1" cx="310" cy="250" r="44" fill="#dd1166" />
  <circle data-id="r2" cx="450" cy="250" r="44" fill="#00ad2f" />
  <circle data-id="r3" cx="590" cy="250" r="44" fill="#9313ce" />
  <circle data-id="r4" cx="730" cy="250" r="44" fill="#231f20" />
{% endframe %}
{% frame '{"w":900,"h":500,"bu":"Rangfolge über Helligkeit: sofort lesbar"}' %}
  <circle data-id="r0" cx="170" cy="250" r="44" fill="#231f20" />
  <circle data-id="r1" cx="310" cy="250" r="44" fill="#555555" />
  <circle data-id="r2" cx="450" cy="250" r="44" fill="#888888" />
  <circle data-id="r3" cx="590" cy="250" r="44" fill="#b3b3b3" />
  <circle data-id="r4" cx="730" cy="250" r="44" fill="#d9d9d9" />
{% endframe %}
{% frame '{"w":900,"h":500,"bu":"Drei Kategorien über Größe: Wirkt, als wäre eine wichtiger"}' %}
  <circle data-id="c0" cx="180" cy="250" r="18" fill="#231f20" />
  <circle data-id="c1" cx="300" cy="250" r="30" fill="#231f20" />
  <circle data-id="c2" cx="420" cy="250" r="44" fill="#231f20" />
  <circle data-id="c3" cx="540" cy="250" r="18" fill="#231f20" />
  <circle data-id="c4" cx="660" cy="250" r="30" fill="#231f20" />
  <circle data-id="c5" cx="780" cy="250" r="44" fill="#231f20" />
{% endframe %}
{% frame '{"w":900,"h":500,"bu":"Drei Kategorien über Farbton: gleichwertig und unterscheidbar"}' %}
  <circle data-id="c0" cx="180" cy="250" r="32" fill="#4952e1" />
  <circle data-id="c1" cx="300" cy="250" r="32" fill="#dd1166" />
  <circle data-id="c2" cx="420" cy="250" r="32" fill="#00ad2f" />
  <circle data-id="c3" cx="540" cy="250" r="32" fill="#4952e1" />
  <circle data-id="c4" cx="660" cy="250" r="32" fill="#dd1166" />
  <circle data-id="c5" cx="780" cy="250" r="32" fill="#00ad2f" />
{% endframe %}
{% frame '{"w":900,"h":500,"bu":"Zusätzlich über Form: auch ohne Farbe unterscheidbar"}' %}
  <circle data-id="c0" cx="180" cy="250" r="32" fill="#4952e1" />
  <rect data-id="c1" x="270" y="220" width="60" height="60" fill="#dd1166" />
  <polygon data-id="c2" points="420,214 454,280 386,280" fill="#00ad2f" />
  <circle data-id="c3" cx="540" cy="250" r="32" fill="#4952e1" />
  <rect data-id="c4" x="630" y="220" width="60" height="60" fill="#dd1166" />
  <polygon data-id="c5" points="780,214 814,280 746,280" fill="#00ad2f" />
{% endframe %}
{% frame '{"w":900,"h":500,"bu":"Drei Buttons, drei Farbtöne: Welcher ist die Hauptaktion?"}' %}
  <rect data-id="b0" x="180" y="225" width="160" height="50" rx="25" fill="#4952e1" />
  <rect data-id="t0" x="225" y="245" width="70" height="10" fill="#ffffff" />
  <rect data-id="b1" x="380" y="225" width="160" height="50" rx="25" fill="#dd1166" />
  <rect data-id="t1" x="425" y="245" width="70" height="10" fill="#ffffff" />
  <rect data-id="b2" x="580" y="225" width="160" height="50" rx="25" fill="#00ad2f" />
  <rect data-id="t2" x="625" y="245" width="70" height="10" fill="#ffffff" />
{% endframe %}
{% frame '{"w":900,"h":500,"bu":"Füllung und Helligkeit zeigen die Rangfolge. Die Akzentfarbe kommt nur einmal vor"}' %}
  <rect data-id="b0" x="180" y="225" width="160" height="50" rx="25" fill="#9313ce" />
  <rect data-id="t0" x="225" y="245" width="70" height="10" fill="#ffffff" />
  <rect data-id="b1" x="380" y="225" width="160" height="50" rx="25" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="t1" x="425" y="245" width="70" height="10" fill="#888888" />
  <rect data-id="b2" x="580" y="225" width="160" height="50" rx="25" fill="#ffffff" />
  <rect data-id="t2" x="625" y="245" width="70" height="10" fill="#b3b3b3" />
{% endframe %}
