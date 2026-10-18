---
title: "Variiert"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Dieselbe Karte, nur der Eckenradius ändert sich. Fragen bei jeder Fassung: Wofür könnte das sein? Welche Marke? Welche Zielgruppe?

  Erwartbar: eckig wirkt sachlich, seriös, technisch (Bank, Versicherung, Behörde, Software für Profis). Leicht gerundet wirkt neutral und modern (die meisten Apps). Stark gerundet und pillenförmig wirkt freundlich, verspielt, zugänglich (Lern-Apps, Kinderangebote, Lifestyle).

  Bezug zum Rückgrat: der Klassiker unter den Passungsfehlern. Runde Ecken, die »moderner« sind, aber nicht zur CI passen (siehe Prinzip Identität und Passung).
---

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Eckig: sachlich, seriös, technisch"}' %}
<rect data-id="card" x="150" y="60" width="600" height="384" rx="0.0" fill="#e4e4e4" />
<rect data-id="img" x="180" y="90" width="540" height="140" rx="0.0" fill="#c4c4c4" />
<rect data-id="h" x="180" y="255" width="260" height="22" rx="0" fill="#231f20" />
<rect data-id="t" x="180" y="293" width="380" height="10" rx="0" fill="#aaaaaa" />
<rect data-id="t2" x="180" y="313" width="300" height="10" rx="0" fill="#aaaaaa" />
<rect data-id="b" x="180" y="350" width="170" height="44" rx="0" fill="#9313ce" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Leicht gerundet: neutral, modern"}' %}
<rect data-id="card" x="150" y="60" width="600" height="384" rx="4.8" fill="#e4e4e4" />
<rect data-id="img" x="180" y="90" width="540" height="140" rx="3.2" fill="#c4c4c4" />
<rect data-id="h" x="180" y="255" width="260" height="22" rx="0" fill="#231f20" />
<rect data-id="t" x="180" y="293" width="380" height="10" rx="0" fill="#aaaaaa" />
<rect data-id="t2" x="180" y="313" width="300" height="10" rx="0" fill="#aaaaaa" />
<rect data-id="b" x="180" y="350" width="170" height="44" rx="8" fill="#9313ce" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Stark gerundet: freundlich, verspielt"}' %}
<rect data-id="card" x="150" y="60" width="600" height="384" rx="13.2" fill="#e4e4e4" />
<rect data-id="img" x="180" y="90" width="540" height="140" rx="8.8" fill="#c4c4c4" />
<rect data-id="h" x="180" y="255" width="260" height="22" rx="0" fill="#231f20" />
<rect data-id="t" x="180" y="293" width="380" height="10" rx="0" fill="#aaaaaa" />
<rect data-id="t2" x="180" y="313" width="300" height="10" rx="0" fill="#aaaaaa" />
<rect data-id="b" x="180" y="350" width="170" height="44" rx="22" fill="#9313ce" />
{% endframe %}

{% question "Welche Ecken hat Ihre Lieblings-App?", "Und passt das zu dem, was sie sein will?" %}
