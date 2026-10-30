---
title: "Schritte"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  **1. Sammeln:** Welche Eigenschaften soll die Marke haben? Adjektive, frei und ohne Bewertung. Hilfreich: Was sagen Kundinnen und Kunden? Was soll man nach dem ersten Besuch erzählen? Wodurch unterscheidet sich die Marke von der Konkurrenz?

  **2. Gewichten:** Die Begriffe um den Markenkern anordnen. Je wichtiger, desto näher dran. Die acht nächsten bleiben. Mehr Paare machen das Profil unlesbar und die Bewertung zäh. Wer einen neunten Begriff braucht, schiebt einen anderen nach außen.

  **3. Gegenpole finden:** Zu jedem Begriff ein Gegenbegriff. Beide Pole müssen positiv sein, siehe nächste Folien.

  **4. Soll festlegen:** Auf jeder Skala markieren, wo die Marke landen soll. Nicht überall die Mitte: Eine Marke, die sich nirgends festlegt, hat kein Profil.

  **5. Prüfen:** Andere bewerten den Entwurf mit denselben Paaren, ohne das Soll zu kennen. Dann Soll und Ist übereinanderlegen. Die Lücken sind der Auftrag.

  **Skala:** Wir arbeiten mit fünf Stufen. Osgood hat sieben verwendet. Fünf reichen, um Richtung und Stärke zu zeigen, und sind schneller ausgefüllt.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Semantisches Differenzial in fünf Schritten</h1>
    {% fragment '<p class="list"><strong>1. Sammeln:</strong> Wofür soll die Marke stehen? Adjektive, frei und ohne Bewertung</p>' %}
    {% fragment '<p class="list"><strong>2. Gewichten:</strong> je wichtiger, desto näher am Kern. Die acht nächsten bleiben.</p>' %}
    {% fragment '<p class="list"><strong>3. Gegenpole finden:</strong> beide Pole positiv</p>' %}
    {% fragment '<p class="list"><strong>4. Soll festlegen:</strong> auf einer Skala mit fünf Stufen</p>' %}
    {% fragment '<p class="list"><strong>5. Prüfen:</strong> Andere bewerten, ohne das Soll zu kennen. Soll und Ist vergleichen.</p>' %}
  </div>
</section>

{% frame '{"stage":"#ffffff", "w":600, "h":600, "bu":"Gewichten: je wichtiger der Begriff, desto näher am Kern"}' %}
<circle data-id="kern" cx="300" cy="300" r="48" fill="#9313ce" />
<circle data-id="p0" cx="389" cy="332" r="13" fill="#231f20" />
<circle data-id="p1" cx="216" cy="371" r="13" fill="#231f20" />
<circle data-id="p2" cx="268" cy="179" r="13" fill="#231f20" />
<circle data-id="p3" cx="335" cy="430" r="13" fill="#231f20" />
<circle data-id="p4" cx="159" cy="249" r="13" fill="#231f20" />
<circle data-id="p5" cx="423" cy="197" r="13" fill="#231f20" />
<circle data-id="p6" cx="242" cy="460" r="13" fill="#231f20" />
<circle data-id="p7" cx="330" cy="128" r="13" fill="#231f20" />
<circle data-id="p8" cx="452" cy="452" r="13" fill="#888888" />
<circle data-id="p9" cx="78" cy="360" r="13" fill="#888888" />
<circle data-id="p10" cx="162" cy="103" r="13" fill="#888888" />
<circle data-id="p11" cx="546" cy="234" r="13" fill="#888888" />
<circle data-id="p12" cx="168" cy="529" r="13" fill="#888888" />
{% endframe %}

{% frame '{"stage":"#ffffff", "w":600, "h":600, "bu":"Die acht nächsten bleiben, der Rest fällt raus"}' %}
<circle data-id="kern" cx="300" cy="300" r="48" fill="#9313ce" />
<circle data-id="ring" cx="300" cy="300" r="193" fill="none" stroke="#d9d9d9" stroke-width="2" />
<circle data-id="p0" cx="389" cy="332" r="13" fill="#231f20" />
<circle data-id="p1" cx="216" cy="371" r="13" fill="#231f20" />
<circle data-id="p2" cx="268" cy="179" r="13" fill="#231f20" />
<circle data-id="p3" cx="335" cy="430" r="13" fill="#231f20" />
<circle data-id="p4" cx="159" cy="249" r="13" fill="#231f20" />
<circle data-id="p5" cx="423" cy="197" r="13" fill="#231f20" />
<circle data-id="p6" cx="242" cy="460" r="13" fill="#231f20" />
<circle data-id="p7" cx="330" cy="128" r="13" fill="#231f20" />
<circle data-id="p8" cx="452" cy="452" r="13" fill="#d9d9d9" />
<circle data-id="p9" cx="78" cy="360" r="13" fill="#d9d9d9" />
<circle data-id="p10" cx="162" cy="103" r="13" fill="#d9d9d9" />
<circle data-id="p11" cx="546" cy="234" r="13" fill="#d9d9d9" />
<circle data-id="p12" cx="168" cy="529" r="13" fill="#d9d9d9" />
{% endframe %}
