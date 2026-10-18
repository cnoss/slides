---
title: "Optische Mitte"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Ein Quadrat, mathematisch exakt in der Mitte des Formats. Fragen: Sitzt es in der Mitte? Die meisten finden, es hängt etwas zu tief. Dann das korrigierte: ein Stück nach oben gerückt, jetzt wirkt es mittig. Die Hilfslinien zeigen beides: Lila ist die geometrische Mitte, Grau die Mitte des Quadrats.

  Faustregel: Die optische Mitte liegt etwas über der geometrischen, in der Praxis ein paar Prozent der Formathöhe. Darum sitzen Titel auf Plakaten, Logos in App-Icons und Inhalte in Dialogen oft leicht über der Mitte.

  **Hintergrund:** Die Wirkung hängt mit der Schwerkraft zusammen (Prinzip Kräfte): Was exakt in der Mitte sitzt, scheint nach unten zu sinken. Rudolf Arnheim beschreibt das in »Art and Visual Perception« (1954).
---

{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Sitzt das Quadrat in der Mitte?"}' %}
<rect data-id="q" x="240" y="240" width="120" height="120" fill="#231f20" />
<line data-id="gm" x1="0" y1="300" x2="600" y2="300" stroke="#9313ce" stroke-width="2" stroke-linecap="round" opacity="0" />
<line data-id="gq" x1="0" y1="300" x2="600" y2="300" stroke="#888888" stroke-width="2" stroke-linecap="round" opacity="0" />
{% endframe %}
{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Geometrisch ja. Optisch hängt es zu tief."}' %}
<rect data-id="q" x="240" y="240" width="120" height="120" fill="#231f20" />
<line data-id="gm" x1="0" y1="300" x2="600" y2="300" stroke="#9313ce" stroke-width="2" stroke-linecap="round" opacity="0.9" />
<line data-id="gq" x1="0" y1="300" x2="600" y2="300" stroke="#888888" stroke-width="2" stroke-linecap="round" opacity="0.9" />
{% endframe %}
{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Etwas nach oben gerückt: Jetzt wirkt es mittig."}' %}
<rect data-id="q" x="240" y="215" width="120" height="120" fill="#231f20" />
<line data-id="gm" x1="0" y1="300" x2="600" y2="300" stroke="#9313ce" stroke-width="2" stroke-linecap="round" opacity="0.9" />
<line data-id="gq" x1="0" y1="275" x2="600" y2="275" stroke="#888888" stroke-width="2" stroke-linecap="round" opacity="0.9" />
{% endframe %}
