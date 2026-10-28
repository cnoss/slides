---
title: "Die dunkle Seite"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Ähnlichkeit lässt sich gegen die Nutzenden einsetzen: Was wie ein Suchergebnis aussieht, wird angeklickt wie eines. Was wie ein Download-Button aussieht, auch.

  **Getarnte Anzeigen:** Anzeigen in Suchergebnissen, Feeds und Nachrichtenseiten übernehmen Aufbau, Schrift und Farben der echten Inhalte. Unterscheidbar sind sie oft nur durch ein kleines Wort wie »Gesponsert« oder »Anzeige«. Je ähnlicher die Anzeige, desto mehr Klicks, und genau das ist der Zweck. Suchmaschinen haben ihre Kennzeichnung über die Jahre immer unauffälliger gemacht, von einer farbigen Fläche hinter den Anzeigen bis zu einem kleinen Wort (aus dem Gedächtnis, bitte prüfen).

  **Falsche Download-Buttons:** Auf Download-Portalen stehen große Werbeflächen, die wie der eigentliche Download aussehen. Der echte Link ist klein und unscheinbar. Wer den falschen erwischt, landet bei Werbung oder installiert etwas, das er nicht wollte.

  Prüffrage für den eigenen Entwurf: Wem nützt diese Ähnlichkeit? Hilft sie den Nutzenden, etwas wiederzuerkennen, oder soll sie sie täuschen?

  **Hintergrund**

  Harry Brignull nennt das Muster »Disguised Ads« (Deceptive Patterns, 2023, und deceptive.design). Werbung muss in Deutschland und der EU als solche erkennbar sein (Trennungsgebot, Gesetz gegen den unlauteren Wettbewerb, für Plattformen auch der Digital Services Act). Die Wireframes sind erfunden, das Muster ist es nicht.
---

{% interlude "Die dunkle Seite", "Was wie ein Suchergebnis aussieht, wird angeklickt wie eines." %}

{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Drei Suchergebnisse?"}' %}
  <rect data-id="feld" x="90" y="70" width="420" height="40" rx="20" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="u0" x="90" y="150" width="140" height="10" fill="#d9d9d9" />
  <rect data-id="ad" x="240" y="151" width="22" height="8" fill="#888888" />
  <rect data-id="t0" x="90" y="170" width="300" height="16" fill="#888888" />
  <rect data-id="a0" x="90" y="196" width="420" height="10" fill="#d9d9d9" />
  <rect data-id="b0" x="90" y="214" width="340" height="10" fill="#d9d9d9" />
  <rect data-id="u1" x="90" y="255" width="140" height="10" fill="#d9d9d9" />
  <rect data-id="t1" x="90" y="275" width="300" height="16" fill="#888888" />
  <rect data-id="a1" x="90" y="301" width="420" height="10" fill="#d9d9d9" />
  <rect data-id="b1" x="90" y="319" width="340" height="10" fill="#d9d9d9" />
  <rect data-id="u2" x="90" y="360" width="140" height="10" fill="#d9d9d9" />
  <rect data-id="t2" x="90" y="380" width="300" height="16" fill="#888888" />
  <rect data-id="a2" x="90" y="406" width="420" height="10" fill="#d9d9d9" />
  <rect data-id="b2" x="90" y="424" width="340" height="10" fill="#d9d9d9" />
{% endframe %}
{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Das erste ist eine Anzeige. Erkennbar nur an einer winzigen Markierung"}' %}
  <rect data-id="feld" x="90" y="70" width="420" height="40" rx="20" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="u0" x="90" y="150" width="140" height="10" fill="#d9d9d9" />
  <rect data-id="ad" x="240" y="151" width="22" height="8" fill="#9313ce" />
  <circle data-id="ring" cx="251" cy="155" r="22" fill="none" stroke="#9313ce" stroke-width="3" />
  <rect data-id="t0" x="90" y="170" width="300" height="16" fill="#888888" />
  <rect data-id="a0" x="90" y="196" width="420" height="10" fill="#d9d9d9" />
  <rect data-id="b0" x="90" y="214" width="340" height="10" fill="#d9d9d9" />
  <rect data-id="u1" x="90" y="255" width="140" height="10" fill="#d9d9d9" />
  <rect data-id="t1" x="90" y="275" width="300" height="16" fill="#888888" />
  <rect data-id="a1" x="90" y="301" width="420" height="10" fill="#d9d9d9" />
  <rect data-id="b1" x="90" y="319" width="340" height="10" fill="#d9d9d9" />
  <rect data-id="u2" x="90" y="360" width="140" height="10" fill="#d9d9d9" />
  <rect data-id="t2" x="90" y="380" width="300" height="16" fill="#888888" />
  <rect data-id="a2" x="90" y="406" width="420" height="10" fill="#d9d9d9" />
  <rect data-id="b2" x="90" y="424" width="340" height="10" fill="#d9d9d9" />
{% endframe %}
{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Drei Downloads?"}' %}
  <rect x="90" y="80" width="260" height="22" fill="#888888" />
  <rect x="90" y="130" width="420" height="12" fill="#d9d9d9" />
  <rect x="90" y="156" width="360" height="12" fill="#d9d9d9" />
  <rect data-id="fake1" x="90" y="186" width="420" height="66" rx="33" fill="#231f20" />
  <polyline points="290,215 300,225 310,215" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" /><line x1="300" y1="205" x2="300" y2="225" stroke="#ffffff" stroke-width="4" stroke-linecap="round" />
  <rect data-id="echt" x="90" y="310" width="70" height="10" fill="#888888" />
  <line data-id="echtu" x1="90" y1="326" x2="160" y2="326" stroke="#888888" stroke-width="2" stroke-linecap="round" />
  <rect x="90" y="376" width="420" height="12" fill="#d9d9d9" />
  <rect data-id="fake2" x="160" y="408" width="280" height="56" rx="28" fill="#231f20" />
  <polyline points="290,432 300,442 310,432" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" /><line x1="300" y1="422" x2="300" y2="442" stroke="#ffffff" stroke-width="4" stroke-linecap="round" />
{% endframe %}
{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Der echte Download ist der unscheinbarste. Die großen Buttons sind Werbung"}' %}
  <rect x="90" y="80" width="260" height="22" fill="#888888" />
  <rect x="90" y="130" width="420" height="12" fill="#d9d9d9" />
  <rect x="90" y="156" width="360" height="12" fill="#d9d9d9" />
  <rect data-id="fake1" x="90" y="186" width="420" height="66" rx="33" fill="#231f20" />
  <polyline points="290,215 300,225 310,215" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" /><line x1="300" y1="205" x2="300" y2="225" stroke="#ffffff" stroke-width="4" stroke-linecap="round" />
  <rect data-id="echt" x="90" y="310" width="70" height="10" fill="#9313ce" />
  <line data-id="echtu" x1="90" y1="326" x2="160" y2="326" stroke="#9313ce" stroke-width="2" stroke-linecap="round" />
  <circle data-id="ring2" cx="125" cy="318" r="44" fill="none" stroke="#9313ce" stroke-width="3" />
  <rect x="90" y="376" width="420" height="12" fill="#d9d9d9" />
  <rect data-id="fake2" x="160" y="408" width="280" height="56" rx="28" fill="#231f20" />
  <polyline points="290,432 300,442 310,432" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" /><line x1="300" y1="422" x2="300" y2="442" stroke="#ffffff" stroke-width="4" stroke-linecap="round" />
{% endframe %}

{% question "Wem nützt diese Ähnlichkeit?", "Den Nutzenden, die etwas wiedererkennen sollen? Oder dem, der für den Klick bezahlt wird?" %}
