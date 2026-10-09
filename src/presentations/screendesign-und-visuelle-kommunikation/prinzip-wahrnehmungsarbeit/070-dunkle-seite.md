---
title: Die dunkle Seite
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Live-Test (ca. 5 Minuten)**

  Zwei Freiwillige mit Handy, jeweils im privaten Fenster, rufen check24.de auf. Person A stimmt allen Cookies zu. Person B erlaubt nur die notwendigen. Alle anderen stoppen die Zeit. Vorher selbst prüfen, ob das Banner noch so aussieht (Stand Oktober 2026: großer blauer Button »Geht klar«, daneben »Anpassen«, und »Nur notwendige Cookies« als kleiner Textlink oben rechts).

  Auflösung: Ablehnen ist möglich, kostet aber mehr Wahrnehmungsarbeit. Der Link ist klein, steht abseits und sieht nicht aus wie ein Button. Die meisten nehmen den einfachen Weg. Genau darauf ist das gestaltet.

  Zum Vergleich: Bei Otto steht »Einwilligung ablehnen« auf der ersten Ebene, aber grau und flach neben einem roten »OK«. dm und die Deutsche Bahn zeigen beide Möglichkeiten gleichwertig.

  Viele Nachrichtenseiten (z. B. Spiegel, Zeit, Chefkoch, GMX) setzen inzwischen auf »Pur-Abos«: Ablehnen heißt dort bezahlen.

  **Hintergrund**

  Default-Effekt: Menschen bleiben meist bei der Voreinstellung oder dem einfachsten Weg. Eric J. Johnson und Daniel Goldstein zeigten das an der Organspende: In Ländern mit Widerspruchslösung lag die Zustimmung bei fast 100 Prozent (Österreich 99,98 %), in Ländern mit Zustimmungslösung deutlich niedriger (Deutschland 12 %). Do Defaults Save Lives? Science 302 (2003), 1338–1339.

  Die deutschen Datenschutzaufsichtsbehörden (DSK, Orientierungshilfe für Anbieter:innen von digitalen Diensten) erwarten, dass Ablehnen auf der ersten Ebene eines Banners ähnlich einfach möglich ist wie Zustimmen. Der Digital Services Act (2022, Art. 25) verbietet Plattformen manipulative Gestaltung.

  Quellen: Brignull, Deceptive Patterns (2023); Johnson & Goldstein (2003).
---

{% interlude "Die dunkle Seite", "Wahrnehmungsarbeit lässt sich auch gezielt erhöhen" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Live: Cookies auf check24.de</h1>
    {% fragment '<p class="list"><strong>Person A:</strong> Stimmen Sie allen Cookies zu.</p>' %}
    {% fragment '<p class="list"><strong>Person B:</strong> Erlauben Sie nur die notwendigen.</p>' %}
    {% fragment '<p class="list"><strong>Alle anderen:</strong> Stoppen Sie die Zeit.</p>' %}
  </div>
</section>

{% screenshot "./images/banner-check24.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"»Geht klar« als großer Button. »Nur notwendige Cookies« als kleiner Link oben rechts.<br><small>check24.de, Screenshot 2026</small>"}' %}
{% screenshot "./images/banner-otto.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Ablehnen geht, aber grau und flach neben einem roten »OK«.<br><small>otto.de, Screenshot 2026</small>"}' %}

{% statement "Menschen nehmen den Weg mit der geringsten Wahrnehmungsarbeit.", "Default-Effekt: Wer das weiß, kann es nutzen. Für die Nutzenden oder gegen sie." %}

{% screenshot "./images/banner-dm.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"So geht es auch: Beide Wege gleich sichtbar, gleich groß.<br><small>dm.de, Screenshot 2026</small>"}' %}
{% screenshot "./images/banner-bahn.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Auch hier: zwei gleichwertige Buttons.<br><small>bahn.de, Screenshot 2026</small>"}' %}

{% question "Wem nützt das?", "Gestalten Sie den Weg, den Nutzende nicht gehen sollen, genauso sorgfältig wie den, den sie gehen sollen." %}
