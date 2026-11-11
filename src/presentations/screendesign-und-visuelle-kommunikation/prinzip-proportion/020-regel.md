---
title: "Verhältnis statt Einzelmaß"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  Die Regel: Proportionen entstehen aus Verhältnissen, nicht aus festen Pixelwerten. Bei responsiven Layouts gibt es den einen Pixelwert ohnehin nicht. Eine Card ist mal 170, mal 330 Pixel breit.

  Erste Fassung: Das Bild jeder Card hat dasselbe Seitenverhältnis, 3 : 2. Die drei Cards wirken wie eine Familie, nur verschieden groß. Zweite Fassung: Das Bild hat überall dieselbe Höhe, 140 Pixel. Die schmale Card wirkt fast quadratisch, die breite wie ein Streifen. Jede Card hat plötzlich einen anderen Charakter.

  Im CSS ist genau das eine Zeile: aspect-ratio: 3 / 2. In Figma lässt sich das Seitenverhältnis eines Rahmens sperren.
---

{% interlude "Verhältnis statt Einzelmaß.", "Gute Proportionen entstehen aus Beziehungen, nicht aus Pixeln." %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "animate":false, "bu":"Gleiches Verhältnis, 3 : 2: drei Größen, eine Familie"}' %}
<rect x="60" y="60" width="170" height="197.3" fill="#e4e4e4" />
<rect x="60" y="60" width="170" height="113.3" fill="#c4c4c4" />
<rect x="76" y="191.3" width="102.0" height="14" fill="#888888" />
<rect x="76" y="217.3" width="138" height="9" fill="#aaaaaa" />
<rect x="270" y="60" width="250" height="250.7" fill="#e4e4e4" />
<rect x="270" y="60" width="250" height="166.7" fill="#c4c4c4" />
<rect x="286" y="244.7" width="150.0" height="14" fill="#888888" />
<rect x="286" y="270.7" width="218" height="9" fill="#aaaaaa" />
<rect x="560" y="60" width="330" height="304.0" fill="#e4e4e4" />
<rect x="560" y="60" width="330" height="220.0" fill="#c4c4c4" />
<rect x="576" y="298.0" width="198.0" height="14" fill="#888888" />
<rect x="576" y="324.0" width="298" height="9" fill="#aaaaaa" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "animate":false, "bu":"Gleiche Höhe, 140 Pixel: drei Cards, drei Charaktere"}' %}
<rect x="60" y="60" width="170" height="224.0" fill="#e4e4e4" />
<rect x="60" y="60" width="170" height="140.0" fill="#c4c4c4" />
<rect x="76" y="218.0" width="102.0" height="14" fill="#888888" />
<rect x="76" y="244.0" width="138" height="9" fill="#aaaaaa" />
<rect x="270" y="60" width="250" height="224.0" fill="#e4e4e4" />
<rect x="270" y="60" width="250" height="140.0" fill="#c4c4c4" />
<rect x="286" y="218.0" width="150.0" height="14" fill="#888888" />
<rect x="286" y="244.0" width="218" height="9" fill="#aaaaaa" />
<rect x="560" y="60" width="330" height="224.0" fill="#e4e4e4" />
<rect x="560" y="60" width="330" height="140.0" fill="#c4c4c4" />
<rect x="576" y="218.0" width="198.0" height="14" fill="#888888" />
<rect x="576" y="244.0" width="298" height="9" fill="#aaaaaa" />
{% endframe %}
