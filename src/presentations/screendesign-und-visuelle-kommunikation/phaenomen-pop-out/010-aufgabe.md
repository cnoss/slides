---
title: "Finden Sie den lila Kreis"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Live-Test (ca. 4 Minuten)**

  Vier Suchbilder, jedes blitzt beim Weiterschalten nur 250 Millisekunden auf. Vorher ansagen: Es geht sehr schnell, und gleich danach zeigen alle mit dem Arm, auf welcher Seite der lila Kreis war.

  Durchgang 1 und 2: Der lila Kreis ist der einzige lila Gegenstand zwischen grauen Kreisen. Fast alle zeigen richtig, obwohl die Zeit kaum zum Hinschauen reicht. Lösung: 1 rechts, 2 links.

  Durchgang 3 und 4: Jetzt gibt es auch lila Quadrate. Der lila Kreis unterscheidet sich von den grauen Kreisen nur durch die Farbe und von den lila Quadraten nur durch die Form. Die Arme zeigen in alle Richtungen, viele zögern. Lösung: 3 links, 4 rechts.

  Danach beide Fassungen in Ruhe zeigen. Im zweiten Bild muss man auch mit Zeit suchen.

  Technik: Der Blitz ist ein Fragment. Zurück und wieder vor wiederholt ihn. Die Suchbilder erzeugt das Bauskript (zufällig, aber fest).
---

{% statement "Finden Sie den lila Kreis.", "Er blitzt nur einen Augenblick auf. Zeigen Sie danach sofort: links oder rechts?" %}

<section class="simple" data-transition="none">
  <div>
    <h1>Durchgang 1</h1>
    <p>Links oder rechts? Zeigen Sie sofort in die Richtung.</p>
    <div class="fragment blitz" style="--dauer:250ms;"><img src="./images/suche-a1.svg" alt="Suchbild mit Kreisen"></div><style>
.reveal .slides section .fragment.blitz{opacity:1;visibility:inherit;transition:none;transform:none;padding:0;margin:0;position:fixed;inset:0;width:100% !important;max-width:none !important;display:flex;align-items:center;justify-content:center;pointer-events:none;}
.reveal .slides section .fragment.blitz img{opacity:0;height:92%;width:auto;max-width:96%;margin:0;box-shadow:0 0 1.5rem rgba(0,0,0,.25);}
.reveal .slides section .fragment.blitz.visible img{animation:blitz-zeigen var(--dauer,50ms) linear 1;}
@keyframes blitz-zeigen{from{opacity:1}to{opacity:1}}
</style>
  </div>
</section>

<section class="simple" data-transition="none">
  <div>
    <h1>Durchgang 2</h1>
    <p>Links oder rechts? Zeigen Sie sofort in die Richtung.</p>
    <div class="fragment blitz" style="--dauer:250ms;"><img src="./images/suche-a2.svg" alt="Suchbild mit Kreisen"></div>
  </div>
</section>

{% statement "Noch einmal.", "Gleiche Aufgabe: Finden Sie den lila Kreis." %}

<section class="simple" data-transition="none">
  <div>
    <h1>Durchgang 3</h1>
    <p>Links oder rechts? Zeigen Sie sofort in die Richtung.</p>
    <div class="fragment blitz" style="--dauer:250ms;"><img src="./images/suche-b1.svg" alt="Suchbild mit Kreisen und Quadraten"></div>
  </div>
</section>

<section class="simple" data-transition="none">
  <div>
    <h1>Durchgang 4</h1>
    <p>Links oder rechts? Zeigen Sie sofort in die Richtung.</p>
    <div class="fragment blitz" style="--dauer:250ms;"><img src="./images/suche-b2.svg" alt="Suchbild mit Kreisen und Quadraten"></div>
  </div>
</section>

{% screenshot "./images/suche-a1.svg", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Und jetzt in Ruhe: Durchgang 1"}' %}
{% screenshot "./images/suche-b1.svg", '{"transition":"none", "classes":"no-shadow", "width":"auto", "bu":"Durchgang 3: Sie müssen suchen, auch mit Zeit"}' %}
