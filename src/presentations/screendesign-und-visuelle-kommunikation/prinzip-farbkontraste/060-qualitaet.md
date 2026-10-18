---
title: Qualitätskontrast
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Kontrast zwischen gesättigten, leuchtenden und gedämpften, trüben Farben. Ein einzelnes gesättigtes Element in einer gedämpften Umgebung wirkt besonders kräftig, ohne laut zu sein. Viele hochwertige Marken arbeiten mit gedämpften Paletten und einem gesättigten Akzent.

  Beispiel aus dem Bestand: eine Finanz-App-Landingpage mit gedämpftem Grün und hellen, leuchtenden Akzenten. Der Screenshot ist älter als zwei Jahre, bei Gelegenheit ersetzen.
---

{% interlude "Qualitätskontrast" %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Dasselbe Orange, Schritt für Schritt gedämpft"}' %}
<rect data-id="s0" x="50.0" y="150" width="144" height="200" fill="#ff7a00" />
<rect data-id="s1" x="214.0" y="150" width="144" height="200" fill="#e3833a" />
<rect data-id="s2" x="378.0" y="150" width="144" height="200" fill="#c58b5c" />
<rect data-id="s3" x="542.0" y="150" width="144" height="200" fill="#a7907c" />
<rect data-id="s4" x="706.0" y="150" width="144" height="200" fill="#8f8f8f" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Ein gesättigtes Element unter gedämpften: kräftig, ohne laut zu sein"}' %}
<rect data-id="s0" x="50.0" y="150" width="144" height="200" fill="#a7907c" />
<rect data-id="s1" x="214.0" y="150" width="144" height="200" fill="#a7907c" />
<rect data-id="s2" x="378.0" y="150" width="144" height="200" fill="#ff7a00" />
<rect data-id="s3" x="542.0" y="150" width="144" height="200" fill="#a7907c" />
<rect data-id="s4" x="706.0" y="150" width="144" height="200" fill="#a7907c" />
{% endframe %}
{% screenshot "./images/qualitaets-kontrast-03.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Gedämpfte Fläche, leuchtende Akzente<br><small>Screenshot aus dem Bestand</small>"}' %}
