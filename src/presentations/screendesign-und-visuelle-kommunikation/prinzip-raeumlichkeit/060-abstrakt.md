---
title: "Tiefe abstrakt"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Zwei gleiche Quadrate. Von Folie zu Folie kommt genau ein Tiefenhinweis dazu, das rechte rückt Schritt für Schritt nach hinten, das linke nach vorn. Fragen bei jedem Schritt: Welches ist wichtiger? Welches sehen Sie zuerst?

  Die Reihenfolge entspricht der Playmobil-Sequenz vom Anfang: Größe, Kontrast, Sättigung, Überdeckung. Die Hinweise addieren sich. Je mehr in dieselbe Richtung zeigen, desto eindeutiger die Rangfolge.

  Sättigung: Gesättigte, warme Farben wirken näher als ungesättigte, kühle. Deshalb trägt hier die Akzentfarbe.
---

{% frame '{"stage":"#ffffff","bu":"Zwei gleiche Quadrate: gleich weit weg, gleich wichtig"}' %}
  <rect data-id="a" x="110" y="220" width="160" height="160" fill="#231f20" />
  <rect data-id="b" x="330" y="220" width="160" height="160" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff","bu":"Größe: Das kleinere rückt nach hinten"}' %}
  <rect data-id="a" x="110" y="220" width="160" height="160" fill="#231f20" />
  <rect data-id="b" x="355" y="245" width="110" height="110" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff","bu":"Kontrast: noch weiter"}' %}
  <rect data-id="a" x="110" y="220" width="160" height="160" fill="#231f20" />
  <rect data-id="b" x="355" y="245" width="110" height="110" fill="#d9d9d9" />
{% endframe %}
{% frame '{"stage":"#ffffff","bu":"Sättigung: Das gesättigte kommt nach vorn"}' %}
  <rect data-id="a" x="110" y="220" width="160" height="160" fill="#9313ce" />
  <rect data-id="b" x="355" y="245" width="110" height="110" fill="#d9d9d9" />
{% endframe %}
{% frame '{"stage":"#ffffff","bu":"Überdeckung: Jetzt ist eindeutig, was vorn liegt"}' %}
  <rect data-id="b" x="255" y="180" width="110" height="110" fill="#d9d9d9" />
  <rect data-id="a" x="150" y="240" width="160" height="160" fill="#9313ce" />
{% endframe %}
