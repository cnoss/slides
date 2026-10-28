---
title: "Auflösung"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Figuren haben sich nicht bewegt. Es ist dieselbe Aufnahme, nur bearbeitet: verkleinert, Kontrast und Sättigung zurückgenommen, hinter die andere Figur geschoben. Und auch Málaga ist eine flache Fläche aus Pixeln. Tiefe steht nicht im Bild, wir lesen sie hinein.

  Das funktioniert so zuverlässig, dass wir es kaum abschalten können. Gestaltung nutzt genau das, auf jedem Screen.

  **Mechanismus:** Die Netzhaut ist eine Fläche. Räumliches Sehen ist eine Leistung des Gehirns, und es nutzt dafür viele Hinweise gleichzeitig. Ein Teil braucht zwei Augen (Querdisparation), ein großer Teil funktioniert mit einem Auge und auf jedem flachen Bild: die monokularen oder bildhaften Tiefenhinweise. Genau die stehen uns auf dem Screen zur Verfügung.

  **Hintergrund**

  - **Relative Größe:** Von zwei gleichen Dingen wirkt das kleinere weiter weg.
  - **Luftperspektive:** Die Luft streut Licht. Ferne Dinge werden heller, kontrastärmer, weniger gesättigt und bläulich. Leonardo da Vinci hat das in seinen Notizen zur Malerei beschrieben (»prospettiva aerea«, um 1500, später zusammengestellt im »Trattato della pittura«) und in seinen Bildhintergründen eingesetzt.
  - **Verdeckung:** Was etwas anderes verdeckt, liegt davor. Der stärkste und eindeutigste Hinweis.
  - **Höhe im Bild:** Was näher am Horizont liegt, wirkt weiter weg.
  - **Texturgradient:** Gleichmäßige Strukturen werden mit der Entfernung feiner und dichter. Beschrieben von James J. Gibson, »The Perception of the Visual World« (1950).

  Zum Nachlesen: E. Bruce Goldstein, Wahrnehmungspsychologie (Kapitel Tiefenwahrnehmung).
---

{% statement "Keine Figur hat sich bewegt.", "Das Bild ist flach. Die Tiefe lesen wir aus Hinweisen hinein." %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Was weiter weg ist, wirkt</h1>
    {% fragment '<p class="list"><strong>kleiner</strong></p>' %}
    {% fragment '<p class="list"><strong>kontrastärmer</strong> und <strong>blasser</strong></p>' %}
    {% fragment '<p class="list"><strong>verdeckt</strong> von dem, was davor liegt</p>' %}
    {% fragment '<p class="list"><strong>höher im Bild</strong>, näher am Horizont</p>' %}
    {% fragment '<p class="list"><strong>dichter</strong> in seiner Struktur</p>' %}
  </div>
</section>
