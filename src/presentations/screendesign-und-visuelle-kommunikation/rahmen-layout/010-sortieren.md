---
title: "Was lesen Sie zuerst?"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  **Einstieg (ca. 3 Minuten), Schätzfrage.** Erst die losen Teile einer Card: ein Bild, eine Kategorie, ein Titel, drei Zeilen Teaser, ein Link. Fragen: Was davon lesen Sie zuerst? Die Antwort ist: Es kommt darauf an, wie die Teile angeordnet sind. Lose gibt es keine Reihenfolge.

  Dann drei Anordnungen derselben Teile. Bei jeder kurz zeigen lassen, was zuerst gesehen wird und in welcher Reihenfolge es weitergeht. Zum Schluss alle drei nebeneinander mit der Leserichtung in Lila.

  Pointe: Die Teile sind immer dieselben, kein Element ist größer, keine Farbe anders. Nur die Anordnung ändert sich, und damit die Reihenfolge, in der gelesen wird. Genau das ist ein Layout.
---

{% interlude "Was lesen Sie zuerst?", "Dieselben Teile, drei Anordnungen" %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Die Teile einer Card: Was lesen Sie zuerst?"}' %}
<rect data-id="karte" x="450" y="250" width="0" height="0" fill="#e4e4e4" />
<rect data-id="bild" x="560" y="70" width="220" height="140" fill="#c4c4c4" rx="0" />
<rect data-id="kat" x="130" y="380" width="70" height="10" fill="#888888" rx="0" />
<rect data-id="titel" x="90" y="90" width="230" height="20" fill="#888888" rx="0" />
<rect data-id="t1" x="420" y="300" width="230" height="10" fill="#aaaaaa" rx="0" />
<rect data-id="t2" x="120" y="210" width="230" height="10" fill="#aaaaaa" rx="0" />
<rect data-id="t3" x="560" y="420" width="161" height="10" fill="#aaaaaa" rx="0" />
<rect data-id="link" x="360" y="150" width="100" height="30" fill="#9313ce" rx="15" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Anordnung A"}' %}
<rect data-id="karte" x="300" y="30" width="300" height="380" fill="#e4e4e4" />
<rect data-id="bild" x="320" y="50" width="260" height="150" fill="#c4c4c4" rx="0" />
<rect data-id="kat" x="320" y="222" width="70" height="10" fill="#888888" rx="0" />
<rect data-id="titel" x="320" y="246" width="220" height="20" fill="#888888" rx="0" />
<rect data-id="t1" x="320" y="282" width="260" height="10" fill="#aaaaaa" rx="0" />
<rect data-id="t2" x="320" y="300" width="260" height="10" fill="#aaaaaa" rx="0" />
<rect data-id="t3" x="320" y="318" width="182" height="10" fill="#aaaaaa" rx="0" />
<rect data-id="link" x="320" y="352" width="100" height="30" fill="#9313ce" rx="15" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Anordnung B"}' %}
<rect data-id="karte" x="300" y="30" width="300" height="380" fill="#e4e4e4" />
<rect data-id="bild" x="320" y="176" width="260" height="150" fill="#c4c4c4" rx="0" />
<rect data-id="kat" x="320" y="50" width="70" height="10" fill="#888888" rx="0" />
<rect data-id="titel" x="320" y="74" width="220" height="20" fill="#888888" rx="0" />
<rect data-id="t1" x="320" y="110" width="260" height="10" fill="#aaaaaa" rx="0" />
<rect data-id="t2" x="320" y="128" width="260" height="10" fill="#aaaaaa" rx="0" />
<rect data-id="t3" x="320" y="146" width="182" height="10" fill="#aaaaaa" rx="0" />
<rect data-id="link" x="320" y="342" width="100" height="30" fill="#9313ce" rx="15" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Anordnung C"}' %}
<rect data-id="karte" x="150" y="110" width="600" height="260" fill="#e4e4e4" />
<rect data-id="bild" x="170" y="130" width="240" height="200" fill="#c4c4c4" rx="0" />
<rect data-id="kat" x="440" y="140" width="70" height="10" fill="#888888" rx="0" />
<rect data-id="titel" x="440" y="164" width="270" height="20" fill="#888888" rx="0" />
<rect data-id="t1" x="440" y="200" width="290" height="10" fill="#aaaaaa" rx="0" />
<rect data-id="t2" x="440" y="218" width="290" height="10" fill="#aaaaaa" rx="0" />
<rect data-id="t3" x="440" y="236" width="203" height="10" fill="#aaaaaa" rx="0" />
<rect data-id="link" x="440" y="280" width="100" height="30" fill="#9313ce" rx="15" />
{% endframe %}

{% question "Welche Anordnung liest sich am klarsten?", "Und in welcher Reihenfolge lesen Sie jeweils?" %}

{% frame '{"animate":false,"stage":"#ffffff", "w":900, "h":500, "bu":"Dieselben Teile, drei Leserichtungen"}' %}
<g transform="translate(-95,60) scale(0.6)"><rect data-x="karte" x="300" y="30" width="300" height="380" fill="#e4e4e4" />
<rect data-x="bild" x="320" y="50" width="260" height="150" fill="#c4c4c4" rx="0" />
<rect data-x="kat" x="320" y="222" width="70" height="10" fill="#888888" rx="0" />
<rect data-x="titel" x="320" y="246" width="220" height="20" fill="#888888" rx="0" />
<rect data-x="t1" x="320" y="282" width="260" height="10" fill="#aaaaaa" rx="0" />
<rect data-x="t2" x="320" y="300" width="260" height="10" fill="#aaaaaa" rx="0" />
<rect data-x="t3" x="320" y="318" width="182" height="10" fill="#aaaaaa" rx="0" />
<rect data-x="link" x="320" y="352" width="100" height="30" fill="#9313ce" rx="15" />
<polyline points="450,125 360,256 360,305 370,367" fill="none" stroke="#9313ce" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />
</g>
<g transform="translate(125,60) scale(0.6)"><rect data-x="karte" x="300" y="30" width="300" height="380" fill="#e4e4e4" />
<rect data-x="bild" x="320" y="176" width="260" height="150" fill="#c4c4c4" rx="0" />
<rect data-x="kat" x="320" y="50" width="70" height="10" fill="#888888" rx="0" />
<rect data-x="titel" x="320" y="74" width="220" height="20" fill="#888888" rx="0" />
<rect data-x="t1" x="320" y="110" width="260" height="10" fill="#aaaaaa" rx="0" />
<rect data-x="t2" x="320" y="128" width="260" height="10" fill="#aaaaaa" rx="0" />
<rect data-x="t3" x="320" y="146" width="182" height="10" fill="#aaaaaa" rx="0" />
<rect data-x="link" x="320" y="342" width="100" height="30" fill="#9313ce" rx="15" />
<polyline points="360,84 360,133 450,251 370,357" fill="none" stroke="#9313ce" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />
</g>
<g transform="translate(477,130) scale(0.45)"><rect data-x="karte" x="150" y="110" width="600" height="260" fill="#e4e4e4" />
<rect data-x="bild" x="170" y="130" width="240" height="200" fill="#c4c4c4" rx="0" />
<rect data-x="kat" x="440" y="140" width="70" height="10" fill="#888888" rx="0" />
<rect data-x="titel" x="440" y="164" width="270" height="20" fill="#888888" rx="0" />
<rect data-x="t1" x="440" y="200" width="290" height="10" fill="#aaaaaa" rx="0" />
<rect data-x="t2" x="440" y="218" width="290" height="10" fill="#aaaaaa" rx="0" />
<rect data-x="t3" x="440" y="236" width="203" height="10" fill="#aaaaaa" rx="0" />
<rect data-x="link" x="440" y="280" width="100" height="30" fill="#9313ce" rx="15" />
<polyline points="290,230 480,174 480,223 490,295" fill="none" stroke="#9313ce" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />
</g>
{% endframe %}
