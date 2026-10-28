---
title: "Im Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Ein Artikel als Wireframe. In der ersten Fassung gibt es vier Hervorhebungen im Text, jede sieht anders aus: lila und unterstrichen, schwarz, lila ohne Linie, grau und unterstrichen. Dazu ein lila Etikett neben der Überschrift und zwei Buttons, die nichts miteinander zu tun haben. Fragen: Was davon ist klickbar? Die ehrliche Antwort: Man kann es nicht wissen, man muss es ausprobieren.

  Die zweite Fassung: Alle Links sehen gleich aus, lila und unterstrichen. Beide Buttons sind Pillen, einmal gefüllt, einmal mit Rahmen. Das Etikett ist weg, weil es wie ein Button aussah. Ähnlichkeit macht das Interface lernbar: Wer einen Link erkannt hat, erkennt alle.

  Mini-Übung danach, 3 Minuten zu zweit.
---

{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Was ist hier klickbar?"}' %}
  <rect x="90" y="90" width="300" height="22" fill="#888888" />
  <rect data-id="badge" x="410" y="88" width="90" height="26" rx="13" fill="#9313ce" />
  <rect x="90" y="140" width="420" height="12" fill="#d9d9d9" />
  <rect data-id="a" x="190" y="140" width="90" height="12" fill="#9313ce" />
  <line data-id="au" x1="190" y1="158" x2="280" y2="158" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
  <rect x="90" y="166" width="400" height="12" fill="#d9d9d9" />
  <rect x="90" y="192" width="420" height="12" fill="#d9d9d9" />
  <rect data-id="b" x="300" y="192" width="80" height="12" fill="#231f20" />
  <rect x="90" y="218" width="260" height="12" fill="#d9d9d9" />
  <rect x="90" y="270" width="420" height="12" fill="#d9d9d9" />
  <rect x="90" y="296" width="380" height="12" fill="#d9d9d9" />
  <rect data-id="c" x="150" y="296" width="110" height="12" fill="#9313ce" />
  <rect x="90" y="322" width="420" height="12" fill="#d9d9d9" />
  <rect x="90" y="348" width="300" height="12" fill="#d9d9d9" />
  <rect data-id="d" x="90" y="348" width="70" height="12" fill="#888888" />
  <line data-id="du" x1="90" y1="366" x2="160" y2="366" stroke="#888888" stroke-width="3" stroke-linecap="round" />
  <rect data-id="btn1" x="90" y="430" width="150" height="44" rx="22" fill="#9313ce" />
  <rect data-id="btn2" x="260" y="430" width="150" height="44" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Gleiches gleich: Links lila und unterstrichen, Buttons als Pille"}' %}
  <rect x="90" y="90" width="300" height="22" fill="#888888" />
  <rect x="90" y="140" width="420" height="12" fill="#d9d9d9" />
  <rect data-id="a" x="190" y="140" width="90" height="12" fill="#9313ce" />
  <line data-id="au" x1="190" y1="158" x2="280" y2="158" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
  <rect x="90" y="166" width="400" height="12" fill="#d9d9d9" />
  <rect x="90" y="192" width="420" height="12" fill="#d9d9d9" />
  <rect data-id="b" x="300" y="192" width="80" height="12" fill="#9313ce" />
  <line data-id="bu" x1="300" y1="210" x2="380" y2="210" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
  <rect x="90" y="218" width="260" height="12" fill="#d9d9d9" />
  <rect x="90" y="270" width="420" height="12" fill="#d9d9d9" />
  <rect x="90" y="296" width="380" height="12" fill="#d9d9d9" />
  <rect data-id="c" x="150" y="296" width="110" height="12" fill="#9313ce" />
  <line data-id="cu" x1="150" y1="314" x2="260" y2="314" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
  <rect x="90" y="322" width="420" height="12" fill="#d9d9d9" />
  <rect x="90" y="348" width="300" height="12" fill="#d9d9d9" />
  <rect data-id="d" x="90" y="348" width="70" height="12" fill="#9313ce" />
  <line data-id="du" x1="90" y1="366" x2="160" y2="366" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
  <rect data-id="btn1" x="90" y="430" width="150" height="44" rx="22" fill="#9313ce" />
  <rect data-id="btn2" x="260" y="431" width="150" height="42" rx="21" fill="#ffffff" stroke="#9313ce" stroke-width="2" />
{% endframe %}

{% question "Woran erkennen Sie in Ihrer meistgenutzten App, was klickbar ist?", "Und wo sieht etwas klickbar aus, ohne es zu sein?" %}
