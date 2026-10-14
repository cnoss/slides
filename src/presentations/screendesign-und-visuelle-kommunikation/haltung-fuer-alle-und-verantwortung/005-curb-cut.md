---
title: Curb-Cut-Effekt
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Einstieg (ca. 5 Minuten)**

  Erst nur das Bild zeigen, ohne Bildunterschrift. Fragen in dieser Reihenfolge:

  - Was sehen Sie hier?
  - Wie heißt das? (Bordsteinabsenkung, englisch Curb Cut)
  - Für wen wurde das gebaut?
  - Wem hilft es heute? Sammeln: Rollstuhl, Rollator, Kinderwagen, Koffer, Fahrrad, Lieferwagen, Skateboard.

  Dann das Foto aus Seattle 1975 und das Interlude: Was Menschen mit Einschränkung hilft, hilft allen. Überleitung ins Digitale: Untertitel helfen in der Bahn ohne Kopfhörer, hohe Kontraste in der Sonne, eine klare Sprache allen, die es eilig haben.

  **Hintergrund**

  Die ersten systematischen Bordsteinabsenkungen entstanden in den 1940er-Jahren in Kalamazoo (Michigan) für Kriegsversehrte. Bekannt wurden sie durch die Behindertenrechtsbewegung in Berkeley Anfang der 1970er-Jahre. Den Begriff »Curb-Cut Effect« hat Angela Glover Blackwell 2017 im Stanford Social Innovation Review geprägt.

  Quelle: Laura Kalbag, Accessibility for Everyone (2017).

  Fotos: Bordsteinabsenkung in Philadelphia, 2019 (Nick-philly, CC BY-SA 4.0). Rollstuhlfahrer an einer Bordsteinrampe am Federal Building in Seattle, 1975 (Seattle Municipal Archives, CC BY 2.0). Menschen mit Smartphones in der New Yorker U-Bahn, 2020 (Billie Grace Ward, CC BY 2.0). Alle von Wikimedia Commons.

  **Und im Digitalen:** Untertitel wurden für Gehörlose entwickelt. Laut einer Umfrage von Verizon Media und Publicis (2019) schauen rund 80 Prozent derer, die Untertitel nutzen, nicht wegen einer Hörbehinderung. Die Zahl als Größenordnung nennen, nicht als exakten Wert.
---

{% screenshotFs "./images/curb-cut-heute.jpg", '{"transition":"fade"}' %}

{% screenshotFs "./images/curb-cut-seattle-1975.jpg", '{"transition":"fade", "bu":"Seattle, 1975: eine der frühen Bordsteinrampen", "credit":"Foto: Seattle Municipal Archives, CC BY 2.0, Wikimedia Commons"}' %}

{% interlude "Was Menschen mit Einschränkung hilft, hilft allen.", "Curb-Cut-Effekt" %}

{% screenshotFs "./images/curb-cut-heute.jpg", '{"transition":"fade", "bu":"Gebaut für den Rollstuhl, genutzt mit Kinderwagen, Koffer, Fahrrad und Rollator", "credit":"Foto: Nick-philly, CC BY-SA 4.0, Wikimedia Commons"}' %}

{% interlude "Und im Digitalen?", "Wer profitiert noch von Barrierefreiheit?" %}

{% screenshotFs "./images/curb-cut-digital-bahn.jpg", '{"transition":"fade", "bu":"Untertitel: gedacht für Gehörlose, genutzt in der vollen Bahn ohne Kopfhörer", "credit":"Foto: Billie Grace Ward, CC BY 2.0, Wikimedia Commons"}' %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Gebaut für wenige, genutzt von allen</h1>
    {% fragment '<p class="list"><strong>Untertitel:</strong> in der Bahn, in der Bibliothek, beim Sprachenlernen</p>' %}
    {% fragment '<p class="list"><strong>Hoher Kontrast:</strong> draußen in der Sonne, auf dem alten Beamer</p>' %}
    {% fragment '<p class="list"><strong>Sprachsteuerung:</strong> mit vollen Händen, beim Kochen, beim Fahren</p>' %}
    {% fragment '<p class="list"><strong>Einfache Sprache:</strong> unter Zeitdruck, in einer fremden Sprache</p>' %}
  </div>
</section>

{% statement "Woran merken Sie, dass Sie den Curb-Cut-Effekt nutzen?", "Sie begründen Barrierefreiheit nicht als Pflicht für wenige, sondern als bessere Lösung für alle." %}
