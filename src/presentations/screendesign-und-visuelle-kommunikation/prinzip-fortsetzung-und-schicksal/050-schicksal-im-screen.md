---
title: "Schicksal im Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Eine Liste, etwa Mails oder Dateien. Beim Weiterschalten rücken drei Einträge gemeinsam nach rechts: Schon das macht sie zur Gruppe, ganz ohne Markierung. Im Interface passiert das beim Auswählen und Ziehen mehrerer Elemente, beim Wischen in Listen oder wenn Inhalte gemeinsam nachladen. Die dritte Fassung ergänzt die Markierung: Bewegung und Ähnlichkeit verstärken sich.

  Weitere Beispiele: Beim Hover über eine Karte reagieren Bild, Titel und Button gemeinsam, also gehören sie zu einer Karte. Beim Öffnen eines Menüs gleiten alle Einträge gemeinsam herein.

  Mini-Übung danach, 2 Minuten.
---

{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Fünf Einträge"}' %}
  <rect x="80" y="60" width="180" height="20" fill="#888888" />
  <rect data-id="cb0" x="81" y="121" width="22" height="22" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="rh0" x="124" y="122" width="200" height="12" fill="#888888" />
  <rect data-id="rt0" x="124" y="144" width="300" height="10" fill="#d9d9d9" />
  <rect data-id="cb1" x="81" y="185" width="22" height="22" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="rh1" x="124" y="186" width="200" height="12" fill="#888888" />
  <rect data-id="rt1" x="124" y="208" width="300" height="10" fill="#d9d9d9" />
  <rect data-id="cb2" x="81" y="249" width="22" height="22" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="rh2" x="124" y="250" width="200" height="12" fill="#888888" />
  <rect data-id="rt2" x="124" y="272" width="300" height="10" fill="#d9d9d9" />
  <rect data-id="cb3" x="81" y="313" width="22" height="22" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="rh3" x="124" y="314" width="200" height="12" fill="#888888" />
  <rect data-id="rt3" x="124" y="336" width="300" height="10" fill="#d9d9d9" />
  <rect data-id="cb4" x="81" y="377" width="22" height="22" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="rh4" x="124" y="378" width="200" height="12" fill="#888888" />
  <rect data-id="rt4" x="124" y="400" width="300" height="10" fill="#d9d9d9" />
{% endframe %}
{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Drei bewegen sich gemeinsam: eine Gruppe"}' %}
  <rect x="80" y="60" width="180" height="20" fill="#888888" />
  <rect data-id="cb0" x="141" y="121" width="22" height="22" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="rh0" x="184" y="122" width="200" height="12" fill="#888888" />
  <rect data-id="rt0" x="184" y="144" width="300" height="10" fill="#d9d9d9" />
  <rect data-id="cb1" x="81" y="185" width="22" height="22" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="rh1" x="124" y="186" width="200" height="12" fill="#888888" />
  <rect data-id="rt1" x="124" y="208" width="300" height="10" fill="#d9d9d9" />
  <rect data-id="cb2" x="141" y="249" width="22" height="22" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="rh2" x="184" y="250" width="200" height="12" fill="#888888" />
  <rect data-id="rt2" x="184" y="272" width="300" height="10" fill="#d9d9d9" />
  <rect data-id="cb3" x="141" y="313" width="22" height="22" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="rh3" x="184" y="314" width="200" height="12" fill="#888888" />
  <rect data-id="rt3" x="184" y="336" width="300" height="10" fill="#d9d9d9" />
  <rect data-id="cb4" x="81" y="377" width="22" height="22" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="rh4" x="124" y="378" width="200" height="12" fill="#888888" />
  <rect data-id="rt4" x="124" y="400" width="300" height="10" fill="#d9d9d9" />
{% endframe %}
{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Dazu ein Häkchen: Bewegung und Ähnlichkeit sagen dasselbe"}' %}
  <rect x="80" y="60" width="180" height="20" fill="#888888" />
  <rect data-id="cb0" x="140" y="120" width="24" height="24" fill="#9313ce" />
  <polyline data-id="ck0" points="146,132 151,137 159,127" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
  <rect data-id="rh0" x="184" y="122" width="200" height="12" fill="#888888" />
  <rect data-id="rt0" x="184" y="144" width="300" height="10" fill="#d9d9d9" />
  <rect data-id="cb1" x="81" y="185" width="22" height="22" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="rh1" x="124" y="186" width="200" height="12" fill="#888888" />
  <rect data-id="rt1" x="124" y="208" width="300" height="10" fill="#d9d9d9" />
  <rect data-id="cb2" x="140" y="248" width="24" height="24" fill="#9313ce" />
  <polyline data-id="ck2" points="146,260 151,265 159,255" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
  <rect data-id="rh2" x="184" y="250" width="200" height="12" fill="#888888" />
  <rect data-id="rt2" x="184" y="272" width="300" height="10" fill="#d9d9d9" />
  <rect data-id="cb3" x="140" y="312" width="24" height="24" fill="#9313ce" />
  <polyline data-id="ck3" points="146,324 151,329 159,319" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
  <rect data-id="rh3" x="184" y="314" width="200" height="12" fill="#888888" />
  <rect data-id="rt3" x="184" y="336" width="300" height="10" fill="#d9d9d9" />
  <rect data-id="cb4" x="81" y="377" width="22" height="22" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="rh4" x="124" y="378" width="200" height="12" fill="#888888" />
  <rect data-id="rt4" x="124" y="400" width="300" height="10" fill="#d9d9d9" />
{% endframe %}

{% question "Wo bewegt sich in Ihrer meistgenutzten App etwas gemeinsam?", "Beim Auswählen, Ziehen, Wischen, Laden?" %}
