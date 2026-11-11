---
title: "Schritte"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  **1. Basis wählen:** 4 oder 8 Pixel. Für Interfaces hat sich 8 durchgesetzt, 4 für feine Abstände.

  **2. Skala festlegen:** sechs bis acht Werte, unten fein, oben grob, etwa 4, 8, 16, 24, 32, 48, 64. Nicht jede Achtergröße aufnehmen (8, 16, 24, 32, 40, 48 …): Zwischen 40 und 48 sieht niemand einen Unterschied, aber alle müssen entscheiden.

  **3. Benennen:** Werte bekommen Namen (space-s, space-m …). Dann reden alle über dasselbe.

  **4. Als Token anlegen:** In Figma als Variables (Typ Number), im Code als CSS-Variablen. Ein Wert wird an einer Stelle geändert und gilt überall.

  **5. Anwenden:** In Figma mit Auto Layout, das Padding (Inset) und Gap (Stack und Inline) direkt aus den Variablen nimmt. Ab jetzt wird nicht mehr geschoben, sondern gewählt.

  **Inset, Stack, Inline:** Die drei Begriffe stammen von Nathan Curtis (»Space in Design Systems«, 2016). Inset ist der Innenabstand eines Containers, wie ein Passepartout. Stack ist der Abstand zwischen Elementen, die untereinander stehen. Inline ist der Abstand zwischen Elementen nebeneinander, hier zwischen Link und Pfeil. Im CSS entspricht das grob padding (Inset) und gap (Stack und Inline).

  **Hintergrund**

  Nathan Curtis, »Space in Design Systems«, EightShapes, Medium, 2016. Die 8-Punkt-Skala ist in Material Design und vielen anderen Design-Systemen üblich. Wathan & Schoger, Refactoring UI (»Establish a spacing and sizing system«): Nicht nach Augenmaß, sondern aus einer begrenzten Auswahl wählen, deren Stufen sich deutlich unterscheiden.
---

{% interlude "In fünf Schritten", "Von der Basis bis zum Token" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Eine Skala für alle Abstände</h1>
    {% fragment '<p class="list"><strong>1. Basis wählen:</strong> 4 oder 8 Pixel</p>' %}
    {% fragment '<p class="list"><strong>2. Skala festlegen:</strong> sechs bis acht Werte, unten fein, oben grob</p>' %}
    {% fragment '<p class="list"><strong>3. Benennen:</strong> space-s, space-m, space-l …</p>' %}
    {% fragment '<p class="list"><strong>4. Als Token anlegen:</strong> Figma Variables, CSS-Variablen</p>' %}
    {% fragment '<p class="list"><strong>5. Anwenden:</strong> mit Auto Layout, nur noch Werte aus der Skala</p>' %}
  </div>
</section>

{% interlude "Inset, Stack, Inline", "Drei Sorten Abstand, drei Wörter" %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "animate":false, "bu":"Die Card aus der Skala"}' %}
<rect data-id="g-karte" x="300.0" y="25.0" width="300.0" height="353.0" fill="#e4e4e4" />
<rect data-id="g-bild" x="300.0" y="25.0" width="300.0" height="150.0" fill="#c4c4c4" />
<rect data-id="g-kat" x="324.0" y="199.0" width="70.0" height="8.0" fill="#888888" />
<rect data-id="g-t1" x="324.0" y="215.0" width="252.0" height="16.0" fill="#888888" />
<rect data-id="g-t2" x="324.0" y="239.0" width="156.2" height="16.0" fill="#888888" />
<rect data-id="g-e0" x="324.0" y="271.0" width="252.0" height="9.0" fill="#aaaaaa" />
<rect data-id="g-e1" x="324.0" y="287.0" width="252.0" height="9.0" fill="#aaaaaa" />
<rect data-id="g-e2" x="324.0" y="303.0" width="176.4" height="9.0" fill="#aaaaaa" />
<rect data-id="g-link" x="324.0" y="336.0" width="64.0" height="10.0" fill="#231f20" />
<path data-id="g-pfeil" d="M396.0 336.0 L401.0 341.0 L396.0 346.0" fill="none" stroke="#231f20" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "animate":false, "bu":"Inset: der Innenabstand, wie ein Passepartout"}' %}
<rect data-id="g-karte" x="300.0" y="25.0" width="300.0" height="353.0" fill="#e4e4e4" />
<rect data-id="g-bild" x="300.0" y="25.0" width="300.0" height="150.0" fill="#c4c4c4" />
<rect data-id="g-kat" x="324.0" y="199.0" width="70.0" height="8.0" fill="#888888" />
<rect data-id="g-t1" x="324.0" y="215.0" width="252.0" height="16.0" fill="#888888" />
<rect data-id="g-t2" x="324.0" y="239.0" width="156.2" height="16.0" fill="#888888" />
<rect data-id="g-e0" x="324.0" y="271.0" width="252.0" height="9.0" fill="#aaaaaa" />
<rect data-id="g-e1" x="324.0" y="287.0" width="252.0" height="9.0" fill="#aaaaaa" />
<rect data-id="g-e2" x="324.0" y="303.0" width="176.4" height="9.0" fill="#aaaaaa" />
<rect data-id="g-link" x="324.0" y="336.0" width="64.0" height="10.0" fill="#231f20" />
<path data-id="g-pfeil" d="M396.0 336.0 L401.0 341.0 L396.0 346.0" fill="none" stroke="#231f20" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
<rect x="300.0" y="175.0" width="24.0" height="203.0" fill="#9313ce" fill-opacity="0.45" />
<rect x="576.0" y="175.0" width="24.0" height="203.0" fill="#9313ce" fill-opacity="0.45" />
<rect x="324.0" y="175.0" width="252.0" height="24.0" fill="#9313ce" fill-opacity="0.45" />
<rect x="324.0" y="346.0" width="252.0" height="32.0" fill="#9313ce" fill-opacity="0.45" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "animate":false, "bu":"Stack: Abstände zwischen Elementen untereinander"}' %}
<rect data-id="g-karte" x="300.0" y="25.0" width="300.0" height="353.0" fill="#e4e4e4" />
<rect data-id="g-bild" x="300.0" y="25.0" width="300.0" height="150.0" fill="#c4c4c4" />
<rect data-id="g-kat" x="324.0" y="199.0" width="70.0" height="8.0" fill="#888888" />
<rect data-id="g-t1" x="324.0" y="215.0" width="252.0" height="16.0" fill="#888888" />
<rect data-id="g-t2" x="324.0" y="239.0" width="156.2" height="16.0" fill="#888888" />
<rect data-id="g-e0" x="324.0" y="271.0" width="252.0" height="9.0" fill="#aaaaaa" />
<rect data-id="g-e1" x="324.0" y="287.0" width="252.0" height="9.0" fill="#aaaaaa" />
<rect data-id="g-e2" x="324.0" y="303.0" width="176.4" height="9.0" fill="#aaaaaa" />
<rect data-id="g-link" x="324.0" y="336.0" width="64.0" height="10.0" fill="#231f20" />
<path data-id="g-pfeil" d="M396.0 336.0 L401.0 341.0 L396.0 346.0" fill="none" stroke="#231f20" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
<rect x="324.0" y="207.0" width="252.0" height="8.0" fill="#9313ce" fill-opacity="0.45" />
<rect x="324.0" y="255.0" width="252.0" height="16.0" fill="#9313ce" fill-opacity="0.45" />
<rect x="324.0" y="312.0" width="252.0" height="24.0" fill="#9313ce" fill-opacity="0.45" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "animate":false, "bu":"Inline: Abstände zwischen Elementen nebeneinander"}' %}
<rect data-id="g-karte" x="300.0" y="25.0" width="300.0" height="353.0" fill="#e4e4e4" />
<rect data-id="g-bild" x="300.0" y="25.0" width="300.0" height="150.0" fill="#c4c4c4" />
<rect data-id="g-kat" x="324.0" y="199.0" width="70.0" height="8.0" fill="#888888" />
<rect data-id="g-t1" x="324.0" y="215.0" width="252.0" height="16.0" fill="#888888" />
<rect data-id="g-t2" x="324.0" y="239.0" width="156.2" height="16.0" fill="#888888" />
<rect data-id="g-e0" x="324.0" y="271.0" width="252.0" height="9.0" fill="#aaaaaa" />
<rect data-id="g-e1" x="324.0" y="287.0" width="252.0" height="9.0" fill="#aaaaaa" />
<rect data-id="g-e2" x="324.0" y="303.0" width="176.4" height="9.0" fill="#aaaaaa" />
<rect data-id="g-link" x="324.0" y="336.0" width="64.0" height="10.0" fill="#231f20" />
<path data-id="g-pfeil" d="M396.0 336.0 L401.0 341.0 L396.0 346.0" fill="none" stroke="#231f20" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
<rect x="388.0" y="333.0" width="8.0" height="16.0" fill="#9313ce" fill-opacity="0.6" />
{% endframe %}
