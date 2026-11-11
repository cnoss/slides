---
title: "Schritte"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  Ein Raster entsteht Schritt für Schritt, und jeder Schritt hat einen Grund.

  **1. Format:** Für welche Breite? Desktop 1440, Tablet 834, Smartphone 390 Pixel sind gute Ausgangspunkte. Ein Raster pro Format.

  **2. Rand:** Wie viel Luft braucht der Inhalt zur Kante? Auf großen Formaten mehr, auf kleinen weniger.

  **3. Inhalt messen:** Der Lesetext gibt die wichtigste Breite vor: 45 bis 75 Zeichen pro Zeile (siehe Lesetext). Bei 18 Pixel Schrift sind das etwa 600 Pixel. Und: Wie viele Cards sollen nebeneinander stehen?

  **4. Spalten und Spaltenabstand:** So viele Spalten, dass sich beides sauber abbilden lässt. Zwölf sind beliebt, weil sich zwölf durch zwei, drei, vier und sechs teilen lässt. Der Text belegt sechs Spalten, eine Card vier. Der Spaltenabstand ist so breit wie der Abstand, der zwischen zwei Cards stehen soll.

  **5. Grundlinie:** Für die Senkrechte ein feines Raster, meist in Schritten von 8 Pixeln (hier 24 Pixel für den Zeilenabstand). Höhen und Abstände rasten darauf ein.

  **6. Module:** Wer Bilder und Kacheln in festen Höhen braucht, fasst Spalten und Zeilen zu Modulen zusammen. Hier belegt ein Element zwei Module nebeneinander.

  Der Lila-Ton zeigt in jeder Folie nur, was neu ist. Die Pixelwerte sind im Maßstab 0,625 gezeichnet, die Rechnung steht auf der übernächsten Folie.
---

{% interlude "Schritt für Schritt", "Vom leeren Format zum Raster" %}

{% frame '{"w":900, "h":500, "bu":"1. Das Format"}' %}
{% endframe %}
{% frame '{"w":900, "h":500, "bu":"2. Der Rand: Luft zur Kante"}' %}
<rect data-id="rand-l" x="0" y="0" width="50" height="500" fill="#9313ce" fill-opacity="0.35" />
<rect data-id="rand-r" x="850" y="0" width="50" height="500" fill="#9313ce" fill-opacity="0.35" />
{% endframe %}
{% frame '{"w":900, "h":500, "bu":"3. Den Inhalt messen: Der Lesetext braucht 45 bis 75 Zeichen"}' %}
<rect data-id="rand-l" x="0" y="0" width="50" height="500" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="rand-r" x="850" y="0" width="50" height="500" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="h1" x="50.0" y="50.0" width="314.0" height="24.0" fill="#888888" rx="0" />
<rect data-id="tx0" x="50.0" y="92.0" width="392.5" height="9.0" fill="#aaaaaa" rx="0" />
<rect data-id="tx1" x="50.0" y="110.0" width="392.5" height="9.0" fill="#aaaaaa" rx="0" />
<rect data-id="tx2" x="50.0" y="128.0" width="392.5" height="9.0" fill="#aaaaaa" rx="0" />
<rect data-id="tx3" x="50.0" y="146.0" width="235.5" height="9.0" fill="#aaaaaa" rx="0" />
{% endframe %}
{% frame '{"w":900, "h":500, "bu":"4. Spalten und Spaltenabstand: Der Text belegt sechs Spalten, eine Card vier"}' %}
<rect data-id="rand-l" x="0" y="0" width="50" height="500" fill="#9313ce" fill-opacity="0" />
<rect data-id="rand-r" x="850" y="0" width="50" height="500" fill="#9313ce" fill-opacity="0" />
<rect data-id="col0" x="50.0" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.15" />
<rect data-id="col1" x="117.9" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.15" />
<rect data-id="col2" x="185.8" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.15" />
<rect data-id="col3" x="253.7" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.15" />
<rect data-id="col4" x="321.7" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.15" />
<rect data-id="col5" x="389.6" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.15" />
<rect data-id="col6" x="457.5" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.15" />
<rect data-id="col7" x="525.4" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.15" />
<rect data-id="col8" x="593.3" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.15" />
<rect data-id="col9" x="661.2" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.15" />
<rect data-id="col10" x="729.2" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.15" />
<rect data-id="col11" x="797.1" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.15" />
<rect data-id="h1" x="50.0" y="50.0" width="314.0" height="24.0" fill="#888888" rx="0" />
<rect data-id="tx0" x="50.0" y="92.0" width="392.5" height="9.0" fill="#aaaaaa" rx="0" />
<rect data-id="tx1" x="50.0" y="110.0" width="392.5" height="9.0" fill="#aaaaaa" rx="0" />
<rect data-id="tx2" x="50.0" y="128.0" width="392.5" height="9.0" fill="#aaaaaa" rx="0" />
<rect data-id="tx3" x="50.0" y="146.0" width="235.5" height="9.0" fill="#aaaaaa" rx="0" />
<rect data-id="k0" x="50.0" y="200.0" width="256.7" height="240.0" fill="#e4e4e4" rx="0" />
<rect data-id="kb0" x="62.0" y="212.0" width="232.7" height="120.0" fill="#c4c4c4" rx="0" />
<rect data-id="kt0" x="62.0" y="346.0" width="186.1" height="12.0" fill="#888888" rx="0" />
<rect data-id="kx0" x="62.0" y="370.0" width="232.7" height="8.0" fill="#aaaaaa" rx="0" />
<rect data-id="kl0" x="62.0" y="392.0" width="60.0" height="16.0" fill="#9313ce" rx="8" />
<rect data-id="k1" x="321.7" y="200.0" width="256.7" height="240.0" fill="#e4e4e4" rx="0" />
<rect data-id="kb1" x="333.7" y="212.0" width="232.7" height="120.0" fill="#c4c4c4" rx="0" />
<rect data-id="kt1" x="333.7" y="346.0" width="186.1" height="12.0" fill="#888888" rx="0" />
<rect data-id="kx1" x="333.7" y="370.0" width="232.7" height="8.0" fill="#aaaaaa" rx="0" />
<rect data-id="kl1" x="333.7" y="392.0" width="60.0" height="16.0" fill="#9313ce" rx="8" />
<rect data-id="k2" x="593.3" y="200.0" width="256.7" height="240.0" fill="#e4e4e4" rx="0" />
<rect data-id="kb2" x="605.3" y="212.0" width="232.7" height="120.0" fill="#c4c4c4" rx="0" />
<rect data-id="kt2" x="605.3" y="346.0" width="186.1" height="12.0" fill="#888888" rx="0" />
<rect data-id="kx2" x="605.3" y="370.0" width="232.7" height="8.0" fill="#aaaaaa" rx="0" />
<rect data-id="kl2" x="605.3" y="392.0" width="60.0" height="16.0" fill="#9313ce" rx="8" />
{% endframe %}
{% frame '{"w":900, "h":500, "bu":"5. Die Grundlinie: Höhen und Abstände rasten senkrecht ein"}' %}
<rect data-id="col0" x="50.0" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.08" />
<rect data-id="col1" x="117.9" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.08" />
<rect data-id="col2" x="185.8" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.08" />
<rect data-id="col3" x="253.7" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.08" />
<rect data-id="col4" x="321.7" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.08" />
<rect data-id="col5" x="389.6" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.08" />
<rect data-id="col6" x="457.5" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.08" />
<rect data-id="col7" x="525.4" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.08" />
<rect data-id="col8" x="593.3" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.08" />
<rect data-id="col9" x="661.2" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.08" />
<rect data-id="col10" x="729.2" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.08" />
<rect data-id="col11" x="797.1" y="0" width="52.9" height="500" fill="#9313ce" fill-opacity="0.08" />
<line data-id="g0" x1="0" y1="15.0" x2="900" y2="15.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g1" x1="0" y1="30.0" x2="900" y2="30.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g2" x1="0" y1="45.0" x2="900" y2="45.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g3" x1="0" y1="60.0" x2="900" y2="60.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g4" x1="0" y1="75.0" x2="900" y2="75.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g5" x1="0" y1="90.0" x2="900" y2="90.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g6" x1="0" y1="105.0" x2="900" y2="105.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g7" x1="0" y1="120.0" x2="900" y2="120.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g8" x1="0" y1="135.0" x2="900" y2="135.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g9" x1="0" y1="150.0" x2="900" y2="150.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g10" x1="0" y1="165.0" x2="900" y2="165.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g11" x1="0" y1="180.0" x2="900" y2="180.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g12" x1="0" y1="195.0" x2="900" y2="195.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g13" x1="0" y1="210.0" x2="900" y2="210.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g14" x1="0" y1="225.0" x2="900" y2="225.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g15" x1="0" y1="240.0" x2="900" y2="240.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g16" x1="0" y1="255.0" x2="900" y2="255.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g17" x1="0" y1="270.0" x2="900" y2="270.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g18" x1="0" y1="285.0" x2="900" y2="285.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g19" x1="0" y1="300.0" x2="900" y2="300.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g20" x1="0" y1="315.0" x2="900" y2="315.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g21" x1="0" y1="330.0" x2="900" y2="330.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g22" x1="0" y1="345.0" x2="900" y2="345.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g23" x1="0" y1="360.0" x2="900" y2="360.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g24" x1="0" y1="375.0" x2="900" y2="375.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g25" x1="0" y1="390.0" x2="900" y2="390.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g26" x1="0" y1="405.0" x2="900" y2="405.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g27" x1="0" y1="420.0" x2="900" y2="420.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g28" x1="0" y1="435.0" x2="900" y2="435.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g29" x1="0" y1="450.0" x2="900" y2="450.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g30" x1="0" y1="465.0" x2="900" y2="465.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g31" x1="0" y1="480.0" x2="900" y2="480.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<line data-id="g32" x1="0" y1="495.0" x2="900" y2="495.0" stroke="#9313ce" stroke-opacity="0.45" stroke-width="1" />
<rect data-id="h1" x="50.0" y="50.0" width="314.0" height="24.0" fill="#888888" rx="0" />
<rect data-id="tx0" x="50.0" y="92.0" width="392.5" height="9.0" fill="#aaaaaa" rx="0" />
<rect data-id="tx1" x="50.0" y="110.0" width="392.5" height="9.0" fill="#aaaaaa" rx="0" />
<rect data-id="tx2" x="50.0" y="128.0" width="392.5" height="9.0" fill="#aaaaaa" rx="0" />
<rect data-id="tx3" x="50.0" y="146.0" width="235.5" height="9.0" fill="#aaaaaa" rx="0" />
<rect data-id="k0" x="50.0" y="200.0" width="256.7" height="240.0" fill="#e4e4e4" rx="0" />
<rect data-id="kb0" x="62.0" y="212.0" width="232.7" height="120.0" fill="#c4c4c4" rx="0" />
<rect data-id="kt0" x="62.0" y="346.0" width="186.1" height="12.0" fill="#888888" rx="0" />
<rect data-id="kx0" x="62.0" y="370.0" width="232.7" height="8.0" fill="#aaaaaa" rx="0" />
<rect data-id="kl0" x="62.0" y="392.0" width="60.0" height="16.0" fill="#9313ce" rx="8" />
<rect data-id="k1" x="321.7" y="200.0" width="256.7" height="240.0" fill="#e4e4e4" rx="0" />
<rect data-id="kb1" x="333.7" y="212.0" width="232.7" height="120.0" fill="#c4c4c4" rx="0" />
<rect data-id="kt1" x="333.7" y="346.0" width="186.1" height="12.0" fill="#888888" rx="0" />
<rect data-id="kx1" x="333.7" y="370.0" width="232.7" height="8.0" fill="#aaaaaa" rx="0" />
<rect data-id="kl1" x="333.7" y="392.0" width="60.0" height="16.0" fill="#9313ce" rx="8" />
<rect data-id="k2" x="593.3" y="200.0" width="256.7" height="240.0" fill="#e4e4e4" rx="0" />
<rect data-id="kb2" x="605.3" y="212.0" width="232.7" height="120.0" fill="#c4c4c4" rx="0" />
<rect data-id="kt2" x="605.3" y="346.0" width="186.1" height="12.0" fill="#888888" rx="0" />
<rect data-id="kx2" x="605.3" y="370.0" width="232.7" height="8.0" fill="#aaaaaa" rx="0" />
<rect data-id="kl2" x="605.3" y="392.0" width="60.0" height="16.0" fill="#9313ce" rx="8" />
{% endframe %}
{% frame '{"w":900, "h":500, "bu":"6. Module: Spalten und Zeilen ergeben Felder"}' %}
<rect data-id="m0-0" x="50.0" y="20.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m0-1" x="50.0" y="125.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m0-2" x="50.0" y="230.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m0-3" x="50.0" y="335.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m1-0" x="117.9" y="20.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m1-1" x="117.9" y="125.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m1-2" x="117.9" y="230.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m1-3" x="117.9" y="335.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m2-0" x="185.8" y="20.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m2-1" x="185.8" y="125.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m2-2" x="185.8" y="230.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m2-3" x="185.8" y="335.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m3-0" x="253.7" y="20.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m3-1" x="253.7" y="125.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m3-2" x="253.7" y="230.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m3-3" x="253.7" y="335.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m4-0" x="321.7" y="20.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m4-1" x="321.7" y="125.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.85" />
<rect data-id="m4-2" x="321.7" y="230.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m4-3" x="321.7" y="335.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m5-0" x="389.6" y="20.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m5-1" x="389.6" y="125.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.85" />
<rect data-id="m5-2" x="389.6" y="230.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m5-3" x="389.6" y="335.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m6-0" x="457.5" y="20.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m6-1" x="457.5" y="125.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m6-2" x="457.5" y="230.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m6-3" x="457.5" y="335.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m7-0" x="525.4" y="20.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m7-1" x="525.4" y="125.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m7-2" x="525.4" y="230.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m7-3" x="525.4" y="335.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m8-0" x="593.3" y="20.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m8-1" x="593.3" y="125.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m8-2" x="593.3" y="230.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m8-3" x="593.3" y="335.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m9-0" x="661.2" y="20.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m9-1" x="661.2" y="125.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m9-2" x="661.2" y="230.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m9-3" x="661.2" y="335.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m10-0" x="729.2" y="20.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m10-1" x="729.2" y="125.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m10-2" x="729.2" y="230.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m10-3" x="729.2" y="335.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m11-0" x="797.1" y="20.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m11-1" x="797.1" y="125.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m11-2" x="797.1" y="230.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
<rect data-id="m11-3" x="797.1" y="335.0" width="52.9" height="90.0" fill="#9313ce" fill-opacity="0.12" />
{% endframe %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Ein Raster in sechs Schritten</h1>
    {% fragment '<p class="list"><strong>1. Format:</strong> ein Raster pro Breite</p>' %}
    {% fragment '<p class="list"><strong>2. Rand:</strong> Luft zur Kante</p>' %}
    {% fragment '<p class="list"><strong>3. Inhalt messen:</strong> Lesetext, Cards, kleinstes Element</p>' %}
    {% fragment '<p class="list"><strong>4. Spalten und Spaltenabstand:</strong> so viele, dass der Inhalt aufgeht</p>' %}
    {% fragment '<p class="list"><strong>5. Grundlinie:</strong> ein feines Raster für die Senkrechte</p>' %}
    {% fragment '<p class="list"><strong>6. Module:</strong> nur wenn feste Höhen gebraucht werden</p>' %}
  </div>
</section>
