---
title: "Auf dem Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  **Play-Button:** Das Dreieck ist mathematisch exakt in den Kreis gesetzt (Mitte seines Begrenzungsrahmens). Es wirkt nach links verrutscht, weil seine Masse links liegt. Korrektur: ein Stück nach rechts, bis der Schwerpunkt in der Mitte sitzt. Das machen alle großen Video-Player so.

  **Icon-Raster:** Design-Systeme haben dafür feste Regeln. Material Design arbeitet mit einem Raster von 24 × 24 dp und sogenannten Keylines: Ein quadratisches Icon ist 18 dp groß, ein rundes 20 dp, damit beide gleich wirken. Auch Apple gibt für App-Icons ein Raster mit unterschiedlichen Kreisen und Rechtecken vor.

  Frage ans Publikum: Wo haben Sie schon einmal etwas »nach Gefühl« verschoben, weil es mathematisch richtig, aber falsch aussah?
---

{% interlude "Auf dem Screen", "Wo Interfaces optisch korrigieren" %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Geometrisch mittig. Wirkt es mittig?"}' %}
<circle data-id="c" cx="450" cy="250" r="150" fill="#231f20" />
<polygon data-id="t" points="400,185 512,250 400,315" fill="#ffffff" />
<line data-id="gm" x1="450" y1="60" x2="450" y2="440" stroke="#9313ce" stroke-width="2" stroke-linecap="round" opacity="0" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Optisch mittig: Das Dreieck sitzt ein Stück weiter rechts"}' %}
<circle data-id="c" cx="450" cy="250" r="150" fill="#231f20" />
<polygon data-id="t" points="410,185 522,250 410,315" fill="#ffffff" />
<line data-id="gm" x1="450" y1="60" x2="450" y2="440" stroke="#9313ce" stroke-width="2" stroke-linecap="round" opacity="0" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Quadrat und Kreis, beide 18 von 24 Rastereinheiten"}' %}
<line x1="150" y1="130" x2="150" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="130" x2="390" y2="130" stroke="#eeeeee" stroke-width="1" />
<line x1="160" y1="130" x2="160" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="140" x2="390" y2="140" stroke="#eeeeee" stroke-width="1" />
<line x1="170" y1="130" x2="170" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="150" x2="390" y2="150" stroke="#eeeeee" stroke-width="1" />
<line x1="180" y1="130" x2="180" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="160" x2="390" y2="160" stroke="#eeeeee" stroke-width="1" />
<line x1="190" y1="130" x2="190" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="170" x2="390" y2="170" stroke="#eeeeee" stroke-width="1" />
<line x1="200" y1="130" x2="200" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="180" x2="390" y2="180" stroke="#eeeeee" stroke-width="1" />
<line x1="210" y1="130" x2="210" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="190" x2="390" y2="190" stroke="#eeeeee" stroke-width="1" />
<line x1="220" y1="130" x2="220" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="200" x2="390" y2="200" stroke="#eeeeee" stroke-width="1" />
<line x1="230" y1="130" x2="230" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="210" x2="390" y2="210" stroke="#eeeeee" stroke-width="1" />
<line x1="240" y1="130" x2="240" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="220" x2="390" y2="220" stroke="#eeeeee" stroke-width="1" />
<line x1="250" y1="130" x2="250" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="230" x2="390" y2="230" stroke="#eeeeee" stroke-width="1" />
<line x1="260" y1="130" x2="260" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="240" x2="390" y2="240" stroke="#eeeeee" stroke-width="1" />
<line x1="270" y1="130" x2="270" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="250" x2="390" y2="250" stroke="#eeeeee" stroke-width="1" />
<line x1="280" y1="130" x2="280" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="260" x2="390" y2="260" stroke="#eeeeee" stroke-width="1" />
<line x1="290" y1="130" x2="290" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="270" x2="390" y2="270" stroke="#eeeeee" stroke-width="1" />
<line x1="300" y1="130" x2="300" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="280" x2="390" y2="280" stroke="#eeeeee" stroke-width="1" />
<line x1="310" y1="130" x2="310" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="290" x2="390" y2="290" stroke="#eeeeee" stroke-width="1" />
<line x1="320" y1="130" x2="320" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="300" x2="390" y2="300" stroke="#eeeeee" stroke-width="1" />
<line x1="330" y1="130" x2="330" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="310" x2="390" y2="310" stroke="#eeeeee" stroke-width="1" />
<line x1="340" y1="130" x2="340" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="320" x2="390" y2="320" stroke="#eeeeee" stroke-width="1" />
<line x1="350" y1="130" x2="350" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="330" x2="390" y2="330" stroke="#eeeeee" stroke-width="1" />
<line x1="360" y1="130" x2="360" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="340" x2="390" y2="340" stroke="#eeeeee" stroke-width="1" />
<line x1="370" y1="130" x2="370" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="350" x2="390" y2="350" stroke="#eeeeee" stroke-width="1" />
<line x1="380" y1="130" x2="380" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="360" x2="390" y2="360" stroke="#eeeeee" stroke-width="1" />
<line x1="390" y1="130" x2="390" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="370" x2="390" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="130" x2="550" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="130" x2="790" y2="130" stroke="#eeeeee" stroke-width="1" />
<line x1="560" y1="130" x2="560" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="140" x2="790" y2="140" stroke="#eeeeee" stroke-width="1" />
<line x1="570" y1="130" x2="570" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="150" x2="790" y2="150" stroke="#eeeeee" stroke-width="1" />
<line x1="580" y1="130" x2="580" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="160" x2="790" y2="160" stroke="#eeeeee" stroke-width="1" />
<line x1="590" y1="130" x2="590" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="170" x2="790" y2="170" stroke="#eeeeee" stroke-width="1" />
<line x1="600" y1="130" x2="600" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="180" x2="790" y2="180" stroke="#eeeeee" stroke-width="1" />
<line x1="610" y1="130" x2="610" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="190" x2="790" y2="190" stroke="#eeeeee" stroke-width="1" />
<line x1="620" y1="130" x2="620" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="200" x2="790" y2="200" stroke="#eeeeee" stroke-width="1" />
<line x1="630" y1="130" x2="630" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="210" x2="790" y2="210" stroke="#eeeeee" stroke-width="1" />
<line x1="640" y1="130" x2="640" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="220" x2="790" y2="220" stroke="#eeeeee" stroke-width="1" />
<line x1="650" y1="130" x2="650" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="230" x2="790" y2="230" stroke="#eeeeee" stroke-width="1" />
<line x1="660" y1="130" x2="660" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="240" x2="790" y2="240" stroke="#eeeeee" stroke-width="1" />
<line x1="670" y1="130" x2="670" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="250" x2="790" y2="250" stroke="#eeeeee" stroke-width="1" />
<line x1="680" y1="130" x2="680" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="260" x2="790" y2="260" stroke="#eeeeee" stroke-width="1" />
<line x1="690" y1="130" x2="690" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="270" x2="790" y2="270" stroke="#eeeeee" stroke-width="1" />
<line x1="700" y1="130" x2="700" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="280" x2="790" y2="280" stroke="#eeeeee" stroke-width="1" />
<line x1="710" y1="130" x2="710" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="290" x2="790" y2="290" stroke="#eeeeee" stroke-width="1" />
<line x1="720" y1="130" x2="720" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="300" x2="790" y2="300" stroke="#eeeeee" stroke-width="1" />
<line x1="730" y1="130" x2="730" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="310" x2="790" y2="310" stroke="#eeeeee" stroke-width="1" />
<line x1="740" y1="130" x2="740" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="320" x2="790" y2="320" stroke="#eeeeee" stroke-width="1" />
<line x1="750" y1="130" x2="750" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="330" x2="790" y2="330" stroke="#eeeeee" stroke-width="1" />
<line x1="760" y1="130" x2="760" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="340" x2="790" y2="340" stroke="#eeeeee" stroke-width="1" />
<line x1="770" y1="130" x2="770" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="350" x2="790" y2="350" stroke="#eeeeee" stroke-width="1" />
<line x1="780" y1="130" x2="780" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="360" x2="790" y2="360" stroke="#eeeeee" stroke-width="1" />
<line x1="790" y1="130" x2="790" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="370" x2="790" y2="370" stroke="#eeeeee" stroke-width="1" />
<rect data-id="iq" x="180.0" y="160.0" width="180" height="180" fill="#231f20" />
<circle data-id="ic" cx="670" cy="250" r="90.0" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Korrigiert wie in Material Design: Der Kreis bekommt 20 Einheiten"}' %}
<line x1="150" y1="130" x2="150" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="130" x2="390" y2="130" stroke="#eeeeee" stroke-width="1" />
<line x1="160" y1="130" x2="160" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="140" x2="390" y2="140" stroke="#eeeeee" stroke-width="1" />
<line x1="170" y1="130" x2="170" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="150" x2="390" y2="150" stroke="#eeeeee" stroke-width="1" />
<line x1="180" y1="130" x2="180" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="160" x2="390" y2="160" stroke="#eeeeee" stroke-width="1" />
<line x1="190" y1="130" x2="190" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="170" x2="390" y2="170" stroke="#eeeeee" stroke-width="1" />
<line x1="200" y1="130" x2="200" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="180" x2="390" y2="180" stroke="#eeeeee" stroke-width="1" />
<line x1="210" y1="130" x2="210" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="190" x2="390" y2="190" stroke="#eeeeee" stroke-width="1" />
<line x1="220" y1="130" x2="220" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="200" x2="390" y2="200" stroke="#eeeeee" stroke-width="1" />
<line x1="230" y1="130" x2="230" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="210" x2="390" y2="210" stroke="#eeeeee" stroke-width="1" />
<line x1="240" y1="130" x2="240" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="220" x2="390" y2="220" stroke="#eeeeee" stroke-width="1" />
<line x1="250" y1="130" x2="250" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="230" x2="390" y2="230" stroke="#eeeeee" stroke-width="1" />
<line x1="260" y1="130" x2="260" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="240" x2="390" y2="240" stroke="#eeeeee" stroke-width="1" />
<line x1="270" y1="130" x2="270" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="250" x2="390" y2="250" stroke="#eeeeee" stroke-width="1" />
<line x1="280" y1="130" x2="280" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="260" x2="390" y2="260" stroke="#eeeeee" stroke-width="1" />
<line x1="290" y1="130" x2="290" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="270" x2="390" y2="270" stroke="#eeeeee" stroke-width="1" />
<line x1="300" y1="130" x2="300" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="280" x2="390" y2="280" stroke="#eeeeee" stroke-width="1" />
<line x1="310" y1="130" x2="310" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="290" x2="390" y2="290" stroke="#eeeeee" stroke-width="1" />
<line x1="320" y1="130" x2="320" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="300" x2="390" y2="300" stroke="#eeeeee" stroke-width="1" />
<line x1="330" y1="130" x2="330" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="310" x2="390" y2="310" stroke="#eeeeee" stroke-width="1" />
<line x1="340" y1="130" x2="340" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="320" x2="390" y2="320" stroke="#eeeeee" stroke-width="1" />
<line x1="350" y1="130" x2="350" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="330" x2="390" y2="330" stroke="#eeeeee" stroke-width="1" />
<line x1="360" y1="130" x2="360" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="340" x2="390" y2="340" stroke="#eeeeee" stroke-width="1" />
<line x1="370" y1="130" x2="370" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="350" x2="390" y2="350" stroke="#eeeeee" stroke-width="1" />
<line x1="380" y1="130" x2="380" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="360" x2="390" y2="360" stroke="#eeeeee" stroke-width="1" />
<line x1="390" y1="130" x2="390" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="150" y1="370" x2="390" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="130" x2="550" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="130" x2="790" y2="130" stroke="#eeeeee" stroke-width="1" />
<line x1="560" y1="130" x2="560" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="140" x2="790" y2="140" stroke="#eeeeee" stroke-width="1" />
<line x1="570" y1="130" x2="570" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="150" x2="790" y2="150" stroke="#eeeeee" stroke-width="1" />
<line x1="580" y1="130" x2="580" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="160" x2="790" y2="160" stroke="#eeeeee" stroke-width="1" />
<line x1="590" y1="130" x2="590" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="170" x2="790" y2="170" stroke="#eeeeee" stroke-width="1" />
<line x1="600" y1="130" x2="600" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="180" x2="790" y2="180" stroke="#eeeeee" stroke-width="1" />
<line x1="610" y1="130" x2="610" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="190" x2="790" y2="190" stroke="#eeeeee" stroke-width="1" />
<line x1="620" y1="130" x2="620" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="200" x2="790" y2="200" stroke="#eeeeee" stroke-width="1" />
<line x1="630" y1="130" x2="630" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="210" x2="790" y2="210" stroke="#eeeeee" stroke-width="1" />
<line x1="640" y1="130" x2="640" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="220" x2="790" y2="220" stroke="#eeeeee" stroke-width="1" />
<line x1="650" y1="130" x2="650" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="230" x2="790" y2="230" stroke="#eeeeee" stroke-width="1" />
<line x1="660" y1="130" x2="660" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="240" x2="790" y2="240" stroke="#eeeeee" stroke-width="1" />
<line x1="670" y1="130" x2="670" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="250" x2="790" y2="250" stroke="#eeeeee" stroke-width="1" />
<line x1="680" y1="130" x2="680" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="260" x2="790" y2="260" stroke="#eeeeee" stroke-width="1" />
<line x1="690" y1="130" x2="690" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="270" x2="790" y2="270" stroke="#eeeeee" stroke-width="1" />
<line x1="700" y1="130" x2="700" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="280" x2="790" y2="280" stroke="#eeeeee" stroke-width="1" />
<line x1="710" y1="130" x2="710" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="290" x2="790" y2="290" stroke="#eeeeee" stroke-width="1" />
<line x1="720" y1="130" x2="720" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="300" x2="790" y2="300" stroke="#eeeeee" stroke-width="1" />
<line x1="730" y1="130" x2="730" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="310" x2="790" y2="310" stroke="#eeeeee" stroke-width="1" />
<line x1="740" y1="130" x2="740" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="320" x2="790" y2="320" stroke="#eeeeee" stroke-width="1" />
<line x1="750" y1="130" x2="750" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="330" x2="790" y2="330" stroke="#eeeeee" stroke-width="1" />
<line x1="760" y1="130" x2="760" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="340" x2="790" y2="340" stroke="#eeeeee" stroke-width="1" />
<line x1="770" y1="130" x2="770" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="350" x2="790" y2="350" stroke="#eeeeee" stroke-width="1" />
<line x1="780" y1="130" x2="780" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="360" x2="790" y2="360" stroke="#eeeeee" stroke-width="1" />
<line x1="790" y1="130" x2="790" y2="370" stroke="#eeeeee" stroke-width="1" />
<line x1="550" y1="370" x2="790" y2="370" stroke="#eeeeee" stroke-width="1" />
<rect data-id="iq" x="180.0" y="160.0" width="180" height="180" fill="#231f20" />
<circle data-id="ic" cx="670" cy="250" r="100.0" fill="#231f20" />
{% endframe %}

{% question "Wo haben Sie schon etwas nach Gefühl verschoben?", "Weil es mathematisch richtig war, aber falsch aussah." %}
