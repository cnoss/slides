---
title: "Im Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Eine Startseite als Wireframe. Navigation, Überschrift mit Text und Button, ein Bild, drei Karten. Dann das Raster dahinter: zwölf Spalten. Jedes Element beginnt und endet an einer Spaltenkante. Die Karten belegen je vier Spalten, der Text sechs, das Bild fünf.

  Zwölf Spalten sind im Web so verbreitet, weil sich zwölf durch zwei, drei, vier und sechs teilen lässt. Auf dem Handy sind vier Spalten üblich, auf dem Tablet acht (so etwa im Raster von Material Design, aus dem Gedächtnis, bitte prüfen).

  Die dritte Fassung bricht das Raster bewusst: Das Bild läuft rechts aus dem Format. Ein Rasterbruch wirkt nur, weil alles andere im Raster steht.

  Danach dasselbe im Code. CSS Grid beschreibt genau diese Struktur: Spalten (Columns), Rinne (Gutter, in CSS: gap), Spannweite eines Elements. Wer in Figma mit einem Raster entwirft, kann es eins zu eins übergeben.
---

{% frame '{"w":900,"h":500,"bu":"Eine Startseite"}' %}
  <rect data-id="sc0" x="60" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0" />
  <rect data-id="sc1" x="126.667" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0" />
  <rect data-id="sc2" x="193.333" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0" />
  <rect data-id="sc3" x="260" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0" />
  <rect data-id="sc4" x="326.667" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0" />
  <rect data-id="sc5" x="393.333" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0" />
  <rect data-id="sc6" x="460" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0" />
  <rect data-id="sc7" x="526.667" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0" />
  <rect data-id="sc8" x="593.333" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0" />
  <rect data-id="sc9" x="660" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0" />
  <rect data-id="sc10" x="726.667" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0" />
  <rect data-id="sc11" x="793.333" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0" />
  <rect data-id="nav" x="60" y="30" width="113.333" height="16" fill="#888888" />
  <rect data-id="n1" x="593.333" y="33" width="46.6667" height="10" fill="#d9d9d9" />
  <rect data-id="n2" x="660" y="33" width="46.6667" height="10" fill="#d9d9d9" />
  <rect data-id="n3" x="726.667" y="33" width="46.6667" height="10" fill="#d9d9d9" />
  <rect data-id="n4" x="793.333" y="33" width="46.6667" height="10" fill="#d9d9d9" />
  <rect data-id="h" x="60" y="100" width="380" height="26" fill="#888888" />
  <rect data-id="t1" x="60" y="146" width="380" height="12" fill="#d9d9d9" />
  <rect data-id="t2" x="60" y="168" width="313.333" height="12" fill="#d9d9d9" />
  <rect data-id="btn" x="60" y="206" width="113.333" height="36" fill="#231f20" rx="18" />
  <rect data-id="bild" x="526.667" y="70" width="313.333" height="190" fill="#d9d9d9" />
  <rect data-id="k1" x="60" y="290" width="246.667" height="130" fill="#e4e4e4" />
  <rect data-id="k2" x="326.667" y="290" width="246.667" height="130" fill="#e4e4e4" />
  <rect data-id="k3" x="593.333" y="290" width="246.667" height="130" fill="#e4e4e4" />
{% endframe %}
{% frame '{"w":900,"h":500,"bu":"Zwölf Spalten (Columns) dahinter"}' %}
  <rect data-id="sc0" x="60" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc1" x="126.667" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc2" x="193.333" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc3" x="260" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc4" x="326.667" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc5" x="393.333" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc6" x="460" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc7" x="526.667" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc8" x="593.333" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc9" x="660" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc10" x="726.667" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc11" x="793.333" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="nav" x="60" y="30" width="113.333" height="16" fill="#888888" />
  <rect data-id="n1" x="593.333" y="33" width="46.6667" height="10" fill="#d9d9d9" />
  <rect data-id="n2" x="660" y="33" width="46.6667" height="10" fill="#d9d9d9" />
  <rect data-id="n3" x="726.667" y="33" width="46.6667" height="10" fill="#d9d9d9" />
  <rect data-id="n4" x="793.333" y="33" width="46.6667" height="10" fill="#d9d9d9" />
  <rect data-id="h" x="60" y="100" width="380" height="26" fill="#888888" />
  <rect data-id="t1" x="60" y="146" width="380" height="12" fill="#d9d9d9" />
  <rect data-id="t2" x="60" y="168" width="313.333" height="12" fill="#d9d9d9" />
  <rect data-id="btn" x="60" y="206" width="113.333" height="36" fill="#231f20" rx="18" />
  <rect data-id="bild" x="526.667" y="70" width="313.333" height="190" fill="#d9d9d9" />
  <rect data-id="k1" x="60" y="290" width="246.667" height="130" fill="#e4e4e4" />
  <rect data-id="k2" x="326.667" y="290" width="246.667" height="130" fill="#e4e4e4" />
  <rect data-id="k3" x="593.333" y="290" width="246.667" height="130" fill="#e4e4e4" />
{% endframe %}
{% frame '{"w":900,"h":500,"bu":"Bewusst gebrochen: Das Bild läuft aus dem Format"}' %}
  <rect data-id="sc0" x="60" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc1" x="126.667" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc2" x="193.333" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc3" x="260" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc4" x="326.667" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc5" x="393.333" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc6" x="460" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc7" x="526.667" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc8" x="593.333" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc9" x="660" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc10" x="726.667" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="sc11" x="793.333" y="0" width="46.6667" height="500" fill="#9313ce" fill-opacity="0.1" />
  <rect data-id="nav" x="60" y="30" width="113.333" height="16" fill="#888888" />
  <rect data-id="n1" x="593.333" y="33" width="46.6667" height="10" fill="#d9d9d9" />
  <rect data-id="n2" x="660" y="33" width="46.6667" height="10" fill="#d9d9d9" />
  <rect data-id="n3" x="726.667" y="33" width="46.6667" height="10" fill="#d9d9d9" />
  <rect data-id="n4" x="793.333" y="33" width="46.6667" height="10" fill="#d9d9d9" />
  <rect data-id="h" x="60" y="100" width="380" height="26" fill="#888888" />
  <rect data-id="t1" x="60" y="146" width="380" height="12" fill="#d9d9d9" />
  <rect data-id="t2" x="60" y="168" width="313.333" height="12" fill="#d9d9d9" />
  <rect data-id="btn" x="60" y="206" width="113.333" height="36" fill="#231f20" rx="18" />
  <rect data-id="bild" x="526.667" y="70" width="373.333" height="190" fill="#d9d9d9" />
  <rect data-id="k1" x="60" y="290" width="246.667" height="130" fill="#e4e4e4" />
  <rect data-id="k2" x="326.667" y="290" width="246.667" height="130" fill="#e4e4e4" />
  <rect data-id="k3" x="593.333" y="290" width="246.667" height="130" fill="#e4e4e4" />
{% endframe %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Dasselbe Raster im Code</h1>
<pre style="font-size:2.6vh; line-height:1.5; text-align:left; width:100%; box-shadow:none;"><code class="language-css">.seite {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 20px; /* Rinne, Gutter */
  padding: 0 60px; /* Rand, Margin */
}
.karte { grid-column: span 4; }
.text { grid-column: 1 / 7; }</code></pre>
  </div>
</section>

{% question "Wie viele Spalten hat Ihre meistgenutzte App?", "Legen Sie gedanklich ein Raster darüber. Woran richten sich die Elemente aus?" %}
