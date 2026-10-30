---
title: "Raster abstrakt"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Ein Format mit zwölf Elementen: ein großes Bild, eine Überschrift mit Text, drei Bilder mit Unterzeilen, ein Button. Erst nach Augenmaß platziert. Nichts ist falsch, aber nichts passt zusammen.

  Dann wird ein Raster sichtbar: sechs Spalten (Columns) mit Rinnen (Gutter) dazwischen und einem Rand (Margin). Die Elemente rasten ein, jedes beginnt und endet an einer Spaltenkante. Zum Schluss verschwindet das Raster wieder. Die Ordnung bleibt.

  Fragen: Was hat sich verändert? Nur die Positionen und Breiten. Kein Element ist neu, keine Farbe anders.

  Hier ist die graue Bühne mit weißem Format bewusst gewählt: Beim Raster bedeutet das Format etwas, die Spalten beziehen sich auf seine Kanten.
---

{% frame '{"bu":"Nach Augenmaß"}' %}
  <rect data-id="col0" x="40" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0" />
  <rect data-id="col1" x="130" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0" />
  <rect data-id="col2" x="220" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0" />
  <rect data-id="col3" x="310" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0" />
  <rect data-id="col4" x="400" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0" />
  <rect data-id="col5" x="490" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0" />
  <rect data-id="bild" x="55" y="48" width="300" height="170" fill="#d9d9d9" />
  <rect data-id="h" x="385" y="70" width="150" height="22" fill="#888888" />
  <rect data-id="t1" x="372" y="112" width="170" height="12" fill="#d9d9d9" />
  <rect data-id="t2" x="380" y="134" width="175" height="12" fill="#d9d9d9" />
  <rect data-id="t3" x="368" y="156" width="100" height="12" fill="#d9d9d9" />
  <rect data-id="b1" x="35" y="262" width="150" height="130" fill="#d9d9d9" />
  <rect data-id="b2" x="215" y="250" width="170" height="110" fill="#d9d9d9" />
  <rect data-id="b3" x="410" y="275" width="140" height="125" fill="#d9d9d9" />
  <rect data-id="u1" x="50" y="412" width="140" height="12" fill="#d9d9d9" />
  <rect data-id="u2" x="230" y="380" width="150" height="12" fill="#d9d9d9" />
  <rect data-id="u3" x="415" y="420" width="130" height="12" fill="#d9d9d9" />
  <rect data-id="btn" x="70" y="480" width="150" height="40" fill="#231f20" rx="20" />
{% endframe %}
{% frame '{"bu":"Ein Raster (Grid) aus sechs Spalten (Columns)"}' %}
  <rect data-id="col0" x="40" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0.12" />
  <rect data-id="col1" x="130" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0.12" />
  <rect data-id="col2" x="220" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0.12" />
  <rect data-id="col3" x="310" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0.12" />
  <rect data-id="col4" x="400" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0.12" />
  <rect data-id="col5" x="490" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0.12" />
  <rect data-id="bild" x="55" y="48" width="300" height="170" fill="#d9d9d9" />
  <rect data-id="h" x="385" y="70" width="150" height="22" fill="#888888" />
  <rect data-id="t1" x="372" y="112" width="170" height="12" fill="#d9d9d9" />
  <rect data-id="t2" x="380" y="134" width="175" height="12" fill="#d9d9d9" />
  <rect data-id="t3" x="368" y="156" width="100" height="12" fill="#d9d9d9" />
  <rect data-id="b1" x="35" y="262" width="150" height="130" fill="#d9d9d9" />
  <rect data-id="b2" x="215" y="250" width="170" height="110" fill="#d9d9d9" />
  <rect data-id="b3" x="410" y="275" width="140" height="125" fill="#d9d9d9" />
  <rect data-id="u1" x="50" y="412" width="140" height="12" fill="#d9d9d9" />
  <rect data-id="u2" x="230" y="380" width="150" height="12" fill="#d9d9d9" />
  <rect data-id="u3" x="415" y="420" width="130" height="12" fill="#d9d9d9" />
  <rect data-id="btn" x="70" y="480" width="150" height="40" fill="#231f20" rx="20" />
{% endframe %}
{% frame '{"bu":"Die Elemente rasten ein"}' %}
  <rect data-id="col0" x="40" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0.12" />
  <rect data-id="col1" x="130" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0.12" />
  <rect data-id="col2" x="220" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0.12" />
  <rect data-id="col3" x="310" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0.12" />
  <rect data-id="col4" x="400" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0.12" />
  <rect data-id="col5" x="490" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0.12" />
  <rect data-id="bild" x="40" y="40" width="340" height="180" fill="#d9d9d9" />
  <rect data-id="h" x="400" y="40" width="160" height="22" fill="#888888" />
  <rect data-id="t1" x="400" y="80" width="160" height="12" fill="#d9d9d9" />
  <rect data-id="t2" x="400" y="102" width="160" height="12" fill="#d9d9d9" />
  <rect data-id="t3" x="400" y="124" width="110" height="12" fill="#d9d9d9" />
  <rect data-id="b1" x="40" y="260" width="160" height="120" fill="#d9d9d9" />
  <rect data-id="b2" x="220" y="260" width="160" height="120" fill="#d9d9d9" />
  <rect data-id="b3" x="400" y="260" width="160" height="120" fill="#d9d9d9" />
  <rect data-id="u1" x="40" y="400" width="160" height="12" fill="#d9d9d9" />
  <rect data-id="u2" x="220" y="400" width="160" height="12" fill="#d9d9d9" />
  <rect data-id="u3" x="400" y="400" width="160" height="12" fill="#d9d9d9" />
  <rect data-id="btn" x="40" y="470" width="160" height="40" fill="#231f20" rx="20" />
{% endframe %}
{% frame '{"bu":"Das Raster verschwindet. Die Ordnung bleibt"}' %}
  <rect data-id="col0" x="40" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0" />
  <rect data-id="col1" x="130" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0" />
  <rect data-id="col2" x="220" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0" />
  <rect data-id="col3" x="310" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0" />
  <rect data-id="col4" x="400" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0" />
  <rect data-id="col5" x="490" y="40" width="70" height="520" fill="#9313ce" fill-opacity="0" />
  <rect data-id="bild" x="40" y="40" width="340" height="180" fill="#d9d9d9" />
  <rect data-id="h" x="400" y="40" width="160" height="22" fill="#888888" />
  <rect data-id="t1" x="400" y="80" width="160" height="12" fill="#d9d9d9" />
  <rect data-id="t2" x="400" y="102" width="160" height="12" fill="#d9d9d9" />
  <rect data-id="t3" x="400" y="124" width="110" height="12" fill="#d9d9d9" />
  <rect data-id="b1" x="40" y="260" width="160" height="120" fill="#d9d9d9" />
  <rect data-id="b2" x="220" y="260" width="160" height="120" fill="#d9d9d9" />
  <rect data-id="b3" x="400" y="260" width="160" height="120" fill="#d9d9d9" />
  <rect data-id="u1" x="40" y="400" width="160" height="12" fill="#d9d9d9" />
  <rect data-id="u2" x="220" y="400" width="160" height="12" fill="#d9d9d9" />
  <rect data-id="u3" x="400" y="400" width="160" height="12" fill="#d9d9d9" />
  <rect data-id="btn" x="40" y="470" width="160" height="40" fill="#231f20" rx="20" />
{% endframe %}
