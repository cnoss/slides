---
title: Signal und Rauschen
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Eine Karte als Wireframe. Signal: Überschrift, Text, die eine Handlung in Lila. Rauschen: Muster im Hintergrund, dicker Rahmen, Icons ohne Funktion, Trennlinien, ein zweiter gleich lauter Button, ein Badge. Beim Weiterschalten verschwindet nur das Rauschen. Inhalt und Handlung bleiben.

  Frage: Was hat gefehlt? Meist: nichts.

  **Hintergrund**

  Das Signal-Rausch-Verhältnis stammt aus der Nachrichtentechnik (Shannon, 1948). In der Gestaltung: Lidwell, Universal Principles of Design (Signal-to-Noise Ratio). Verwandt ist Edward Tuftes "Data-Ink Ratio" für Diagramme (The Visual Display of Quantitative Information, 1983): Möglichst viel der Tinte soll Daten zeigen.
---

{% frame '{"bu":"Viel Rauschen: Was ist hier das Signal?"}' %}
<line x1="0" y1="0" x2="0" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="24" y1="0" x2="24" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="48" y1="0" x2="48" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="72" y1="0" x2="72" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="96" y1="0" x2="96" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="120" y1="0" x2="120" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="144" y1="0" x2="144" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="168" y1="0" x2="168" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="192" y1="0" x2="192" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="216" y1="0" x2="216" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="240" y1="0" x2="240" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="264" y1="0" x2="264" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="288" y1="0" x2="288" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="312" y1="0" x2="312" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="336" y1="0" x2="336" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="360" y1="0" x2="360" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="384" y1="0" x2="384" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="408" y1="0" x2="408" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="432" y1="0" x2="432" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="456" y1="0" x2="456" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="480" y1="0" x2="480" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="504" y1="0" x2="504" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="528" y1="0" x2="528" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="552" y1="0" x2="552" y2="600" stroke="#f0f0f0" stroke-width="2" />
<line x1="576" y1="0" x2="576" y2="600" stroke="#f0f0f0" stroke-width="2" />
<rect data-id="rahmen" x="90" y="70" width="420" height="460" fill="#ffffff" stroke="#231f20" stroke-width="8" />
<circle data-id="i0" cx="120" cy="110" r="16" fill="#888888" />
<circle data-id="i1" cx="170" cy="110" r="16" fill="#888888" />
<circle data-id="i2" cx="220" cy="110" r="16" fill="#888888" />
<line data-id="t1" x1="110" y1="150" x2="490" y2="150" stroke="#888888" stroke-width="4" />
<line data-id="t2" x1="110" y1="380" x2="490" y2="380" stroke="#888888" stroke-width="4" />
<rect data-id="b2" x="300" y="440" width="170" height="50" rx="25" fill="#888888" />
<rect data-id="badge" x="400" y="90" width="90" height="36" fill="#888888" />
<rect data-id="h" x="130" y="190" width="300" height="28" fill="#231f20" />
<rect data-id="p0" x="130" y="240" width="340" height="12" fill="#d9d9d9" />
<rect data-id="p1" x="130" y="270" width="340" height="12" fill="#d9d9d9" />
<rect data-id="p2" x="130" y="300" width="340" height="12" fill="#d9d9d9" />
<rect data-id="p3" x="130" y="330" width="200" height="12" fill="#d9d9d9" />
<rect data-id="b1" x="130" y="440" width="170" height="50" rx="25" fill="#9313ce" />
{% endframe %}
{% frame '{"bu":"Nur noch Signal: Inhalt und eine Handlung."}' %}
<rect data-id="rahmen" x="90" y="70" width="420" height="460" fill="#ffffff" stroke="#d9d9d9" stroke-width="2" />
<rect data-id="h" x="130" y="140" width="300" height="28" fill="#231f20" />
<rect data-id="p0" x="130" y="200" width="340" height="12" fill="#d9d9d9" />
<rect data-id="p1" x="130" y="230" width="340" height="12" fill="#d9d9d9" />
<rect data-id="p2" x="130" y="260" width="340" height="12" fill="#d9d9d9" />
<rect data-id="p3" x="130" y="290" width="200" height="12" fill="#d9d9d9" />
<rect data-id="b1" x="130" y="380" width="170" height="50" rx="25" fill="#9313ce" />
{% endframe %}
