---
title: "Im Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Eine Liste als Wireframe. Ohne Flächen hält nur der Abstand die Einträge zusammen. Das funktioniert, solange die Abstände eindeutig sind. Mit Karten ist jede Fläche eine Gruppe, selbst wenn die Einträge eng stehen. Darum sind Karten im Interface so verbreitet: in Feeds, Shops, Dashboards.

  Dasselbe bei Formularen: Zwei Abschnitte, etwa Adresse und Zahlung. Mit hinterlegten Flächen sieht man auf einen Blick, welches Feld zu welchem Abschnitt gehört. Die Fläche ersetzt keine Überschrift, aber sie zeigt die Gruppe schneller.

  Mini-Übung danach, 3 Minuten zu zweit.
---

{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Ohne Flächen: Gruppen nur durch Abstand"}' %}
  <rect x="80" y="70" width="220" height="20" fill="#888888" />
  <rect data-id="i0" x="86" y="120" width="90" height="90" fill="#d9d9d9" />
  <rect data-id="h0" x="196" y="128" width="200" height="14" fill="#888888" />
  <rect data-id="t0a" x="196" y="156" width="300" height="10" fill="#d9d9d9" />
  <rect data-id="t0b" x="196" y="176" width="220" height="10" fill="#d9d9d9" />
  <rect data-id="i1" x="86" y="245" width="90" height="90" fill="#d9d9d9" />
  <rect data-id="h1" x="196" y="253" width="200" height="14" fill="#888888" />
  <rect data-id="t1a" x="196" y="281" width="300" height="10" fill="#d9d9d9" />
  <rect data-id="t1b" x="196" y="301" width="220" height="10" fill="#d9d9d9" />
  <rect data-id="i2" x="86" y="370" width="90" height="90" fill="#d9d9d9" />
  <rect data-id="h2" x="196" y="378" width="200" height="14" fill="#888888" />
  <rect data-id="t2a" x="196" y="406" width="300" height="10" fill="#d9d9d9" />
  <rect data-id="t2b" x="196" y="426" width="220" height="10" fill="#d9d9d9" />
{% endframe %}
{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Mit Karten: Jede Fläche ist eine Gruppe"}' %}
  <rect x="80" y="70" width="220" height="20" fill="#888888" />
  <rect data-id="c0" x="70" y="106" width="460" height="118" fill="#e4e4e4" />
  <rect data-id="i0" x="86" y="120" width="90" height="90" fill="#c4c4c4" />
  <rect data-id="h0" x="196" y="128" width="200" height="14" fill="#888888" />
  <rect data-id="t0a" x="196" y="156" width="300" height="10" fill="#aaaaaa" />
  <rect data-id="t0b" x="196" y="176" width="220" height="10" fill="#aaaaaa" />
  <rect data-id="c1" x="70" y="231" width="460" height="118" fill="#e4e4e4" />
  <rect data-id="i1" x="86" y="245" width="90" height="90" fill="#c4c4c4" />
  <rect data-id="h1" x="196" y="253" width="200" height="14" fill="#888888" />
  <rect data-id="t1a" x="196" y="281" width="300" height="10" fill="#aaaaaa" />
  <rect data-id="t1b" x="196" y="301" width="220" height="10" fill="#aaaaaa" />
  <rect data-id="c2" x="70" y="356" width="460" height="118" fill="#e4e4e4" />
  <rect data-id="i2" x="86" y="370" width="90" height="90" fill="#c4c4c4" />
  <rect data-id="h2" x="196" y="378" width="200" height="14" fill="#888888" />
  <rect data-id="t2a" x="196" y="406" width="300" height="10" fill="#aaaaaa" />
  <rect data-id="t2b" x="196" y="426" width="220" height="10" fill="#aaaaaa" />
{% endframe %}
{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Ein Formular, zwei Abschnitte"}' %}
  <rect x="90" y="60" width="200" height="20" fill="#888888" />
  <rect data-id="fh0" x="90" y="114" width="140" height="14" fill="#888888" />
  <rect data-id="fl00" x="90" y="150" width="90" height="10" fill="#d9d9d9" />
  <rect data-id="ff00" x="90" y="166" width="420" height="28" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="fl01" x="90" y="206" width="90" height="10" fill="#d9d9d9" />
  <rect data-id="ff01" x="90" y="222" width="420" height="28" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="fh1" x="90" y="304" width="140" height="14" fill="#888888" />
  <rect data-id="fl10" x="90" y="340" width="90" height="10" fill="#d9d9d9" />
  <rect data-id="ff10" x="90" y="356" width="420" height="28" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="fl11" x="90" y="396" width="90" height="10" fill="#d9d9d9" />
  <rect data-id="ff11" x="90" y="412" width="420" height="28" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="fbtn" x="90" y="490" width="140" height="40" rx="20" fill="#9313ce" />
{% endframe %}
{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Mit Flächen: Abschnitte auf einen Blick"}' %}
  <rect x="90" y="60" width="200" height="20" fill="#888888" />
  <rect data-id="fr0" x="70" y="96" width="460" height="168" fill="#e4e4e4" />
  <rect data-id="fh0" x="90" y="114" width="140" height="14" fill="#888888" />
  <rect data-id="fl00" x="90" y="150" width="90" height="10" fill="#aaaaaa" />
  <rect data-id="ff00" x="90" y="166" width="420" height="28" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="fl01" x="90" y="206" width="90" height="10" fill="#aaaaaa" />
  <rect data-id="ff01" x="90" y="222" width="420" height="28" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="fr1" x="70" y="286" width="460" height="168" fill="#e4e4e4" />
  <rect data-id="fh1" x="90" y="304" width="140" height="14" fill="#888888" />
  <rect data-id="fl10" x="90" y="340" width="90" height="10" fill="#aaaaaa" />
  <rect data-id="ff10" x="90" y="356" width="420" height="28" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="fl11" x="90" y="396" width="90" height="10" fill="#aaaaaa" />
  <rect data-id="ff11" x="90" y="412" width="420" height="28" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="fbtn" x="90" y="490" width="140" height="40" rx="20" fill="#9313ce" />
{% endframe %}

{% question "Wo arbeitet Ihre meistgenutzte App mit Karten, Flächen oder Linien?", "Und wäre es ohne sie auch eindeutig?" %}
