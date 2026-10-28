---
title: "Scanmuster"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Menschen lesen Screens nicht, sie überfliegen sie. Dabei entstehen typische Blickmuster.

  **F-Muster:** bei textlastigen Seiten ohne klare Hierarchie. Erst eine Zeile ganz, dann eine kürzere, dann nur noch den linken Rand hinunter. Was rechts unten steht, sieht kaum jemand.

  **Z-Muster:** bei Seiten mit wenig Text, etwa Einstiegsseiten. Der Blick geht von links oben nach rechts oben, quer nach links unten und wieder nach rechts. Wichtige Punkte liegen auf dem Z: Logo, Navigation, Handlung rechts unten.

  Die Pointe: Das F-Muster ist kein Ziel, sondern ein Symptom. Es entsteht, wenn Hierarchie fehlt. Gute Hierarchie gibt dem Blick einen besseren Weg.

  **Hintergrund**

  Jakob Nielsen beschrieb das F-Muster 2006 nach Eyetracking-Studien der Nielsen Norman Group (»F-Shaped Pattern For Reading Web Content«). Kara Pernice hat die Studien 2017 aktualisiert: Das Muster gibt es weiterhin, vor allem wenn Text nicht gegliedert ist, Zwischenüberschriften, Hervorhebungen und kurze Absätze machen es schwächer. Das Z-Muster geht auf Leserichtung und das Gutenberg-Diagramm aus dem Zeitungsdesign zurück. Steve Krug, »Don't Make Me Think« (2014): »We don't read pages. We scan them.« (Jahreszahlen aus dem Gedächtnis, bitte prüfen.)
---

{% statement "Wir lesen nicht, wir scannen.", "Der Blick springt über einen Screen und sucht nach Einstiegen. Hierarchie bestimmt, wo er landet." %}

{% frame '{"w":900,"h":500,"bu":"Viel Text, wenig Hierarchie"}' %}
  <rect data-id="logo" x="60" y="36" width="90" height="20" fill="#888888" />
  <rect data-id="h" x="60" y="90" width="520" height="28" fill="#888888" />
  <rect data-id="z0" x="60" y="150" width="780" height="10" fill="#d9d9d9" />
  <rect data-id="z1" x="60" y="176" width="760" height="10" fill="#d9d9d9" />
  <rect data-id="z2" x="60" y="202" width="780" height="10" fill="#d9d9d9" />
  <rect data-id="z3" x="60" y="228" width="540" height="10" fill="#d9d9d9" />
  <rect data-id="z4" x="60" y="272" width="780" height="10" fill="#d9d9d9" />
  <rect data-id="z5" x="60" y="298" width="720" height="10" fill="#d9d9d9" />
  <rect data-id="z6" x="60" y="324" width="780" height="10" fill="#d9d9d9" />
  <rect data-id="z7" x="60" y="350" width="760" height="10" fill="#d9d9d9" />
  <rect data-id="z8" x="60" y="376" width="480" height="10" fill="#d9d9d9" />
{% endframe %}
{% frame '{"w":900,"h":500,"bu":"F-Muster: zwei Zeilen, dann nur noch der linke Rand"}' %}
  <rect data-id="logo" x="60" y="36" width="90" height="20" fill="#888888" />
  <rect data-id="h" x="60" y="90" width="520" height="28" fill="#888888" />
  <rect data-id="z0" x="60" y="150" width="780" height="10" fill="#d9d9d9" />
  <rect data-id="z1" x="60" y="176" width="760" height="10" fill="#d9d9d9" />
  <rect data-id="z2" x="60" y="202" width="780" height="10" fill="#d9d9d9" />
  <rect data-id="z3" x="60" y="228" width="540" height="10" fill="#d9d9d9" />
  <rect data-id="z4" x="60" y="272" width="780" height="10" fill="#d9d9d9" />
  <rect data-id="z5" x="60" y="298" width="720" height="10" fill="#d9d9d9" />
  <rect data-id="z6" x="60" y="324" width="780" height="10" fill="#d9d9d9" />
  <rect data-id="z7" x="60" y="350" width="760" height="10" fill="#d9d9d9" />
  <rect data-id="z8" x="60" y="376" width="480" height="10" fill="#d9d9d9" />
  <path data-id="pfad" d="M 70 104 L 560 104 M 70 104 L 70 277 L 420 277 M 70 277 L 70 386" fill="none" stroke="#9313ce" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" opacity="0.85" />
{% endframe %}
{% frame '{"w":900,"h":500,"bu":"Wenig Text, ein Bild, eine Handlung"}' %}
  <rect data-id="logo" x="60" y="36" width="90" height="20" fill="#888888" />
  <rect data-id="n1" x="560" y="42" width="60" height="8" fill="#d9d9d9" />
  <rect data-id="n2" x="640" y="42" width="60" height="8" fill="#d9d9d9" />
  <rect data-id="n3" x="720" y="42" width="60" height="8" fill="#d9d9d9" />
  <rect data-id="bild" x="60" y="96" width="780" height="200" fill="#e4e4e4" />
  <rect data-id="t1" x="60" y="330" width="420" height="12" fill="#d9d9d9" />
  <rect data-id="t2" x="60" y="356" width="360" height="12" fill="#d9d9d9" />
  <rect data-id="btn" x="660" y="330" width="180" height="48" rx="24" fill="#231f20" />
{% endframe %}
{% frame '{"w":900,"h":500,"bu":"Z-Muster: oben quer, diagonal zurück, unten zur Handlung"}' %}
  <rect data-id="logo" x="60" y="36" width="90" height="20" fill="#888888" />
  <rect data-id="n1" x="560" y="42" width="60" height="8" fill="#d9d9d9" />
  <rect data-id="n2" x="640" y="42" width="60" height="8" fill="#d9d9d9" />
  <rect data-id="n3" x="720" y="42" width="60" height="8" fill="#d9d9d9" />
  <rect data-id="bild" x="60" y="96" width="780" height="200" fill="#e4e4e4" />
  <rect data-id="t1" x="60" y="330" width="420" height="12" fill="#d9d9d9" />
  <rect data-id="t2" x="60" y="356" width="360" height="12" fill="#d9d9d9" />
  <rect data-id="btn" x="660" y="330" width="180" height="48" rx="24" fill="#231f20" />
  <path data-id="pfad" d="M 105 46 L 780 46 L 110 336 L 750 354" fill="none" stroke="#9313ce" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" opacity="0.85" />
{% endframe %}
