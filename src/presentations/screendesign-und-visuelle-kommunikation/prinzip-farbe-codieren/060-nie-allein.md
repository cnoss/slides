---
title: Farbe nie allein
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Rund acht Prozent der Männer und etwa 0,5 Prozent der Frauen mit nordeuropäischer Herkunft haben eine Farbsehschwäche, am häufigsten eine Rot-Grün-Schwäche. In einem Hörsaal mit 100 Studierenden sind das statistisch mehrere Personen.

  Die zweite Grafik zeigt die Statusliste, wie sie bei Deuteranopie (Grünblindheit) erscheint. Simulation nach Machado, Oliveira und Fernandes (2009). Rot und Grün werden zu fast demselben Olivton, der Status ist nicht mehr lesbar.

  Die Lösung: Farbe plus ein zweites Merkmal. Form (Kreis gegen Dreieck), Symbol, Text (»Fehler«, »OK«), Position. Dann funktioniert der Code auch in Graustufen, bei Sonnenlicht, auf schlechten Displays und im Schwarzweißdruck.

  **Hintergrund**

  WCAG 2.2, Erfolgskriterium 1.4.1 »Use of Color«: Farbe darf nicht das einzige visuelle Mittel sein, um Information zu vermitteln, eine Aktion anzuzeigen oder ein Element zu unterscheiden. Prüfen: Farbfehlsichtigkeit simulieren, etwa mit den Entwicklerwerkzeugen von Chrome (Rendering, »Emulate vision deficiencies«) oder in Figma mit Plugins.
---

{% interlude "Farbe nie allein.", "Nicht alle sehen dieselben Farben." %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Eine Statusliste: Grün ist in Ordnung, Rot ist ein Fehler"}' %}
<circle data-id="d0" cx="220" cy="100" r="18" fill="#1a8a3a" />
<rect data-id="t0" x="260" y="94" width="300" height="12" rx="0" fill="#d9d9d9" />
<circle data-id="d1" cx="220" cy="162" r="18" fill="#d81e2c" />
<rect data-id="t1" x="260" y="156" width="300" height="12" rx="0" fill="#d9d9d9" />
<circle data-id="d2" cx="220" cy="224" r="18" fill="#1a8a3a" />
<rect data-id="t2" x="260" y="218" width="300" height="12" rx="0" fill="#d9d9d9" />
<circle data-id="d3" cx="220" cy="286" r="18" fill="#1a8a3a" />
<rect data-id="t3" x="260" y="280" width="300" height="12" rx="0" fill="#d9d9d9" />
<circle data-id="d4" cx="220" cy="348" r="18" fill="#d81e2c" />
<rect data-id="t4" x="260" y="342" width="300" height="12" rx="0" fill="#d9d9d9" />
<circle data-id="d5" cx="220" cy="410" r="18" fill="#1a8a3a" />
<rect data-id="t5" x="260" y="404" width="300" height="12" rx="0" fill="#d9d9d9" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Dieselbe Liste mit Rot-Grün-Sehschwäche (Deuteranopie, simuliert)"}' %}
<circle data-id="d0" cx="220" cy="100" r="18" fill="#7f7440" />
<rect data-id="t0" x="260" y="94" width="300" height="12" rx="0" fill="#d9d9d9" />
<circle data-id="d1" cx="220" cy="162" r="18" fill="#8b7c23" />
<rect data-id="t1" x="260" y="156" width="300" height="12" rx="0" fill="#d9d9d9" />
<circle data-id="d2" cx="220" cy="224" r="18" fill="#7f7440" />
<rect data-id="t2" x="260" y="218" width="300" height="12" rx="0" fill="#d9d9d9" />
<circle data-id="d3" cx="220" cy="286" r="18" fill="#7f7440" />
<rect data-id="t3" x="260" y="280" width="300" height="12" rx="0" fill="#d9d9d9" />
<circle data-id="d4" cx="220" cy="348" r="18" fill="#8b7c23" />
<rect data-id="t4" x="260" y="342" width="300" height="12" rx="0" fill="#d9d9d9" />
<circle data-id="d5" cx="220" cy="410" r="18" fill="#7f7440" />
<rect data-id="t5" x="260" y="404" width="300" height="12" rx="0" fill="#d9d9d9" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Farbe plus Form plus Text: lesbar für alle"}' %}
<circle data-id="d0" cx="220" cy="100" r="18" fill="#1a8a3a" />
<rect data-id="t0" x="260" y="94" width="300" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="l0" x="580" y="92" width="60" height="16" rx="3" fill="#1a8a3a" />
<polygon data-id="d1" points="220,144 240,180 200,180" fill="#d81e2c" />
<rect data-id="t1" x="260" y="156" width="300" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="l1" x="580" y="154" width="90" height="16" rx="3" fill="#d81e2c" />
<circle data-id="d2" cx="220" cy="224" r="18" fill="#1a8a3a" />
<rect data-id="t2" x="260" y="218" width="300" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="l2" x="580" y="216" width="60" height="16" rx="3" fill="#1a8a3a" />
<circle data-id="d3" cx="220" cy="286" r="18" fill="#1a8a3a" />
<rect data-id="t3" x="260" y="280" width="300" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="l3" x="580" y="278" width="60" height="16" rx="3" fill="#1a8a3a" />
<polygon data-id="d4" points="220,330 240,366 200,366" fill="#d81e2c" />
<rect data-id="t4" x="260" y="342" width="300" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="l4" x="580" y="340" width="90" height="16" rx="3" fill="#d81e2c" />
<circle data-id="d5" cx="220" cy="410" r="18" fill="#1a8a3a" />
<rect data-id="t5" x="260" y="404" width="300" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="l5" x="580" y="402" width="60" height="16" rx="3" fill="#1a8a3a" />
{% endframe %}

{% statement "Information nie nur über Farbe.", "Immer ein zweites Merkmal dazu: Form, Symbol, Text oder Position. WCAG 2.2, Kriterium 1.4.1" %}
