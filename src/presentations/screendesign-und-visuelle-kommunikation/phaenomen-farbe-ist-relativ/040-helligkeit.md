---
title: Bunt wirkt heller
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Frage: Ist die bunte Fläche oben heller oder dunkler als die graue darunter? Die bunten Flächen wirken fast immer heller. Beim Weiterschalten werden die bunten Flächen durch das Grau mit derselben Leuchtdichte ersetzt: Oben und unten sind gleich.

  Die Grauwerte sind berechnet: gleiche relative Leuchtdichte nach sRGB (die Größe, mit der auch die WCAG-Kontrastformel rechnet).

  **Hintergrund**

  Helmholtz-Kohlrausch-Effekt, benannt nach Hermann von Helmholtz und Viktor Arnold Kohlrausch. Gesättigte Farben wirken heller als ein Grau mit gleicher gemessener Leuchtdichte. Die Helligkeit, die wir sehen, ist also nicht die Helligkeit, die ein Messgerät oder eine Formel ausgibt.

  Folge für Barrierefreiheit: Kontrastformeln wie die der WCAG 2 rechnen nur mit Leuchtdichte. Bei kräftigen Farben passen Rechnung und Eindruck deshalb nicht immer zusammen. Der Entwurf für WCAG 3 diskutiert dafür ein neues Kontrastmodell (APCA).
---

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Oben bunt, unten grau: Was wirkt heller?"}' %}
<rect data-id="c0" x="95" y="90" width="140" height="140" fill="#e8002a" />
<rect data-id="g0" x="95" y="270" width="140" height="140" fill="#747474" />
<rect data-id="c1" x="285" y="90" width="140" height="140" fill="#1f6fff" />
<rect data-id="g1" x="285" y="270" width="140" height="140" fill="#787878" />
<rect data-id="c2" x="475" y="90" width="140" height="140" fill="#14a33c" />
<rect data-id="g2" x="475" y="270" width="140" height="140" fill="#8d8d8d" />
<rect data-id="c3" x="665" y="90" width="140" height="140" fill="#d6118f" />
<rect data-id="g3" x="665" y="270" width="140" height="140" fill="#727272" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Messbar sind beide gleich hell."}' %}
<rect data-id="c0" x="95" y="90" width="140" height="140" fill="#747474" />
<rect data-id="g0" x="95" y="270" width="140" height="140" fill="#747474" />
<rect data-id="c1" x="285" y="90" width="140" height="140" fill="#787878" />
<rect data-id="g1" x="285" y="270" width="140" height="140" fill="#787878" />
<rect data-id="c2" x="475" y="90" width="140" height="140" fill="#8d8d8d" />
<rect data-id="g2" x="475" y="270" width="140" height="140" fill="#8d8d8d" />
<rect data-id="c3" x="665" y="90" width="140" height="140" fill="#727272" />
<rect data-id="g3" x="665" y="270" width="140" height="140" fill="#727272" />
{% endframe %}
