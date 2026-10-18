---
title: Simultankontrast
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Erst fragen, Hände heben lassen: Ist das linke Quadrat heller oder dunkler als das rechte? Die meisten sehen das linke Grau heller. Dann weiterschalten: Ein Steg in demselben Grau verbindet beide Quadrate, der Unterschied ist weg.

  Zweites Beispiel mit Farbe: Dasselbe Orange wirkt auf Blau leuchtend und warm, auf Gelb stumpf und fast bräunlich. Beim Weiterschalten verschwinden die Hintergründe, die Quadrate rücken zusammen.

  **Hintergrund**

  Simultankontrast: Eine Farbe verändert sich durch ihre Nachbarfarbe. Sie wird heller neben Dunklem, dunkler neben Hellem und nimmt einen Hauch der Komplementärfarbe ihrer Umgebung an. Beschrieben hat das der Chemiker Michel Eugène Chevreul (De la loi du contraste simultané des couleurs, 1839), der als Direktor der Färberei der Pariser Gobelin-Manufaktur Beschwerden über »stumpfe« Wollfarben nachging. Die Farben waren in Ordnung, die Nachbarfarben waren das Problem. Josef Albers hat das mit seinen Studierenden in »Interaction of Color« (1963) systematisch erforscht.
---

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Welches Grau ist heller?"}' %}
<rect data-id="bgl" x="60" y="60" width="380" height="380" fill="#231f20" />
<rect data-id="bgr" x="460" y="60" width="380" height="380" fill="#f2f2f2" />
<rect data-id="ql" x="190" y="190" width="120" height="120" fill="#888888" />
<rect data-id="qr" x="590" y="190" width="120" height="120" fill="#888888" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Es ist dasselbe Grau."}' %}
<rect data-id="bgl" x="60" y="60" width="380" height="380" fill="#231f20" />
<rect data-id="bgr" x="460" y="60" width="380" height="380" fill="#f2f2f2" />
<rect data-id="ql" x="190" y="190" width="120" height="120" fill="#888888" />
<rect data-id="qr" x="590" y="190" width="120" height="120" fill="#888888" />
<rect data-id="brueck" x="250" y="230" width="400" height="40" fill="#888888" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Und welches Orange leuchtet stärker?"}' %}
<rect data-id="bgl" x="60" y="60" width="380" height="380" fill="#2f3a8f" />
<rect data-id="bgr" x="460" y="60" width="380" height="380" fill="#f2d34a" />
<rect data-id="ql" x="190" y="190" width="120" height="120" fill="#e39a3b" />
<rect data-id="qr" x="590" y="190" width="120" height="120" fill="#e39a3b" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Es ist dasselbe Orange."}' %}
<rect data-id="bgl" x="250" y="250" width="0" height="0" fill="#2f3a8f" />
<rect data-id="bgr" x="650" y="250" width="0" height="0" fill="#f2d34a" />
<rect data-id="ql" x="320" y="190" width="120" height="120" fill="#e39a3b" />
<rect data-id="qr" x="460" y="190" width="120" height="120" fill="#e39a3b" />
{% endframe %}
