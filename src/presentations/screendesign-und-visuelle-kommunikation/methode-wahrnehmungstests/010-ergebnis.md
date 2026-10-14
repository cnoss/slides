---
title: Ergebnis zuerst
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  So sieht ein Ergebnis aus: ein erfundenes Beispiel, eine App zum Vorbestellen beim Bäcker, fünf Personen, je fünf Sekunden. Erst den Screen zeigen und kurz fragen: Was fällt Ihnen auf? Dann die Ergebnisse einblenden.

  Die Antworten werden gezählt, nicht gemittelt. Fazit in einem Satz: Die Botschaft kommt an, die Handlung nicht. Das große Foto und die orangefarbene Box mit den Öffnungszeiten ziehen den Blick, die Vorbestellung ist nur ein kleiner grauer Link. Also: Vorbestellung zum Button machen und erneut testen.

  Der Screen ist ein Mockup, keine echte App. Foto: »Korb mit Brötchen«, 3268zauber, CC BY-SA 3.0, Wikimedia Commons.
---

{% screenshot "./images/baeckerei-app.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Eine Bäckerei-App, Startscreen<br><small>Fiktives Beispiel. Foto: 3268zauber, CC BY-SA 3.0, Wikimedia Commons</small>"}' %}

<section class="simple" data-transition="fade">
  <div style="display:flex; gap:3rem; align-items:center; text-align:left;">
    <img src="./images/baeckerei-app.jpg" alt="Startscreen der fiktiven Bäckerei-App Krume" style="height:72vh; width:auto; box-shadow:0 0 1.5rem rgba(0,0,0,.2);">
    <div>
      <h1>So sieht das Ergebnis aus</h1>
      <p>5 Personen, je 5 Sekunden</p>
      {% fragment '<p class="list"><strong>Worum geht es?</strong> 4 von 5: Brötchen vorbestellen</p>' %}
      {% fragment '<p class="list"><strong>Was kann man hier tun?</strong> 1 von 5: bestellen. 3 von 5: wissen es nicht</p>' %}
      {% fragment '<p class="list"><strong>Was ist hängen geblieben?</strong> das große Foto, die Öffnungszeiten</p>' %}
      {% fragment '<p class="list"><strong>Fazit:</strong> Die Botschaft kommt an, die Handlung nicht.</p>' %}
    </div>
  </div>
</section>
