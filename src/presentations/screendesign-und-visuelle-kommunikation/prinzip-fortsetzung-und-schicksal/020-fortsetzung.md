---
title: "Gute Fortsetzung"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Erst fragen: Was sehen Sie? Fast alle sagen: zwei Kurven, die sich kreuzen. Dann die Auflösung: Genauso gut könnten es zwei Linien sein, die sich an der Kreuzung berühren und jeweils einen Knick haben. So sieht es kaum jemand. Wir bevorzugen die Lesart, bei der die Linien ohne Knick weiterlaufen.

  Die dritte Grafik: 26 einzelne Punkte. Gesehen werden aber eine Gerade und eine Kurve, die sich kreuzen. Der Blick folgt dem Verlauf, auch über Lücken hinweg.

  **Hintergrund**

  Gute Fortsetzung ist der Grund, warum Diagramme mit Linien funktionieren, warum Ausrichtung an einer Kante wirkt und warum ein angeschnittenes Element »weiter« sagt. Das Auge ergänzt den Verlauf über die Lücke hinaus, verwandt mit der Geschlossenheit.
---

{% frame '{"stage":"#ffffff", "w":600, "h":600, "bu":"Was sehen Sie?"}' %}
  <path data-id="a1" d="M 90.0 520.0 C 112.2 386.8, 162.1 284.4, 246.6 217.9" fill="none" stroke="#231f20" stroke-width="8" stroke-linecap="round" />
  <path data-id="a2" d="M 246.6 217.9 C 314.3 164.6, 404.3 134.4, 520.0 130.0" fill="none" stroke="#231f20" stroke-width="8" stroke-linecap="round" />
  <path data-id="b1" d="M 80.0 170.0 C 148.1 170.0, 201.9 185.7, 246.8 218.3" fill="none" stroke="#231f20" stroke-width="8" stroke-linecap="round" />
  <path data-id="b2" d="M 246.8 218.3 C 320.5 271.8, 370.3 370.8, 420.0 520.0" fill="none" stroke="#231f20" stroke-width="8" stroke-linecap="round" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":600, "h":600, "bu":"Möglich wäre auch das: zwei Linien mit Knick. So sieht es kaum jemand"}' %}
  <path data-id="a1" d="M 90.0 520.0 C 112.2 386.8, 162.1 284.4, 246.6 217.9" fill="none" stroke="#9313ce" stroke-width="8" stroke-linecap="round" />
  <path data-id="b2" d="M 246.8 218.3 C 320.5 271.8, 370.3 370.8, 420.0 520.0" fill="none" stroke="#9313ce" stroke-width="8" stroke-linecap="round" />
  <path data-id="a2" d="M 246.6 217.9 C 314.3 164.6, 404.3 134.4, 520.0 130.0" fill="none" stroke="#231f20" stroke-width="8" stroke-linecap="round" />
  <path data-id="b1" d="M 80.0 170.0 C 148.1 170.0, 201.9 185.7, 246.8 218.3" fill="none" stroke="#231f20" stroke-width="8" stroke-linecap="round" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":600, "h":600, "bu":"26 Punkte. Gesehen werden eine Gerade und eine Kurve", "animate":false}' %}
  <circle cx="80.0" cy="160.0" r="10" fill="#231f20" />
  <circle cx="80.0" cy="470.0" r="10" fill="#231f20" />
  <circle cx="115.4" cy="251.7" r="10" fill="#231f20" />
  <circle cx="116.7" cy="443.3" r="10" fill="#231f20" />
  <circle cx="151.5" cy="327.3" r="10" fill="#231f20" />
  <circle cx="153.3" cy="416.7" r="10" fill="#231f20" />
  <circle cx="188.1" cy="387.2" r="10" fill="#231f20" />
  <circle cx="190.0" cy="390.0" r="10" fill="#231f20" />
  <circle cx="225.2" cy="431.9" r="10" fill="#231f20" />
  <circle cx="226.7" cy="363.3" r="10" fill="#231f20" />
  <circle cx="262.5" cy="461.8" r="10" fill="#231f20" />
  <circle cx="263.3" cy="336.7" r="10" fill="#231f20" />
  <circle cx="300.0" cy="477.5" r="10" fill="#231f20" />
  <circle cx="300.0" cy="310.0" r="10" fill="#231f20" />
  <circle cx="337.5" cy="479.5" r="10" fill="#231f20" />
  <circle cx="336.7" cy="283.3" r="10" fill="#231f20" />
  <circle cx="374.8" cy="468.1" r="10" fill="#231f20" />
  <circle cx="373.3" cy="256.7" r="10" fill="#231f20" />
  <circle cx="411.9" cy="444.1" r="10" fill="#231f20" />
  <circle cx="410.0" cy="230.0" r="10" fill="#231f20" />
  <circle cx="448.5" cy="407.7" r="10" fill="#231f20" />
  <circle cx="446.7" cy="203.3" r="10" fill="#231f20" />
  <circle cx="484.6" cy="359.5" r="10" fill="#231f20" />
  <circle cx="483.3" cy="176.7" r="10" fill="#231f20" />
  <circle cx="520.0" cy="300.0" r="10" fill="#231f20" />
  <circle cx="520.0" cy="150.0" r="10" fill="#231f20" />
{% endframe %}
