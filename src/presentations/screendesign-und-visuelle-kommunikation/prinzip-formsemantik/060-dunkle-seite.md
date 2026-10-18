---
title: "Die dunkle Seite"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Gelernte Formbedeutung lässt sich missbrauchen. Werbung tarnt sich als Systemwarnung: rotes Dreieck, kantiger Rahmen, ein Button wie im Betriebssystem. Die Form sagt »Achtung, Ihr System«, gemeint ist ein Verkaufsangebot oder Schlimmeres. Ähnlich: Werbebanner mit falschem Schließen-Kreuz oder falschem Download-Pfeil.

  Brignull nennt das »Disguised ads«. Das Wireframe ist ein Mockup.
---

{% interlude "Die dunkle Seite", "Formen, die etwas vortäuschen" %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Eine Seite"}' %}
<rect data-id="pg" x="150" y="40" width="600" height="420" rx="0" fill="#ffffff" />
<rect x="150" y="40" width="600" height="420" fill="none" stroke="#d9d9d9" stroke-width="2" />
<rect data-id="nav" x="170" y="60" width="560" height="24" rx="0" fill="#d9d9d9" />
<rect data-id="h" x="170" y="110" width="300" height="20" rx="0" fill="#888888" />
<rect data-id="t0" x="170" y="145" width="520" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="t1" x="170" y="165" width="480" height="10" rx="0" fill="#d9d9d9" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Eine Anzeige in der Form einer Systemwarnung: Dreieck, Rahmen, Button"}' %}
<rect data-id="pg" x="150" y="40" width="600" height="420" rx="0" fill="#ffffff" />
<rect x="150" y="40" width="600" height="420" fill="none" stroke="#d9d9d9" stroke-width="2" />
<rect data-id="nav" x="170" y="60" width="560" height="24" rx="0" fill="#d9d9d9" />
<rect data-id="h" x="170" y="110" width="300" height="20" rx="0" fill="#888888" />
<rect data-id="t0" x="170" y="145" width="520" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="t1" x="170" y="165" width="480" height="10" rx="0" fill="#d9d9d9" />
<rect data-id="ad" x="250" y="200" width="400" height="220" rx="4" fill="#ffffff" />
<rect x="250" y="200" width="400" height="220" rx="4" fill="none" stroke="#d81e2c" stroke-width="3" />
<polygon points="450,225 495,300 405,300" fill="#d81e2c" />
<rect data-id="w1" x="330" y="320" width="240" height="14" rx="0" fill="#231f20" />
<rect data-id="w2" x="350" y="345" width="200" height="10" rx="0" fill="#888888" />
<rect data-id="b" x="360" y="375" width="180" height="32" rx="4" fill="#d81e2c" />
{% endframe %}

{% question "Wem nützt diese Form?", "Der Person, die gewarnt werden muss? Oder der Anzeige, die geklickt werden will?" %}
