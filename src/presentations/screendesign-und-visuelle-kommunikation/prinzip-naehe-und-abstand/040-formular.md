---
title: Formular
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Ein Formular als Wireframe. Grau: Beschriftung, Rahmen: Eingabefeld, Lila: Absenden. Links sind alle Abstände gleich: Gehört die Beschriftung zum Feld darüber oder darunter? Rechts ist nur der Abstand verändert, sonst nichts.
transition: none
---

{% frame '{"bu":"Gleiche Abstände: Gehört die Beschriftung zum Feld darüber oder darunter?"}' %}
  <rect data-id="l0" x="150" y="90" width="110" height="12" fill="#888888" />
  <rect data-id="f0" x="150" y="138" width="300" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="l1" x="150" y="214" width="110" height="12" fill="#888888" />
  <rect data-id="f1" x="150" y="262" width="300" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="l2" x="150" y="338" width="110" height="12" fill="#888888" />
  <rect data-id="f2" x="150" y="386" width="300" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="btn" x="150" y="476" width="120" height="40" rx="20" fill="#9313ce" />
{% endframe %}
{% frame '{"bu":"Innen enger als außen: Beschriftung und Feld bilden eine Gruppe"}' %}
  <rect data-id="l0" x="150" y="90" width="110" height="12" fill="#888888" />
  <rect data-id="f0" x="150" y="110" width="300" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="l1" x="150" y="224" width="110" height="12" fill="#888888" />
  <rect data-id="f1" x="150" y="244" width="300" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="l2" x="150" y="358" width="110" height="12" fill="#888888" />
  <rect data-id="f2" x="150" y="378" width="300" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="btn" x="150" y="468" width="120" height="40" rx="20" fill="#9313ce" />
{% endframe %}
