---
title: Ein Augenblick
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Live-Test (ca. 5 Minuten)**

  Jede Seite blitzt beim Weiterschalten für 50 Millisekunden auf. Vorher ansagen, dass es sehr schnell geht. Direkt nach jedem Blitz Daumen zeigen lassen und grob zählen (mehr hoch oder mehr runter), an der Tafel notieren.

  Danach die vier Seiten in Ruhe zeigen. Frage: Hätten Sie jetzt anders abgestimmt? Erfahrungsgemäß kaum.

  Technik: Der Blitz ist ein Fragment. Zurück und wieder vor wiederholt ihn. Bei sehr trägen Beamern wirkt er etwas länger, das schadet dem Effekt nicht.

  Seiten: apple.com (Produktseite, ruhig, ein Bild), arngren.net (norwegischer Elektronikhändler, extrem dicht), craigslist.org (Kleinanzeigen, reine Linklisten, seit Jahrzehnten fast unverändert), stadt-koeln.de (Stadtverwaltung). Alle Screenshots Oktober 2026, 1440 px.
---

{% statement "Gleich sehen Sie vier Websites. Jede nur einen Augenblick.", "Zeigen Sie danach sofort: Daumen hoch, die Seite spricht mich an. Daumen runter, eher nicht." %}

<section class="simple" data-transition="none">
  <div>
    <h1>Seite 1</h1>
    <p>Daumen hoch oder runter?</p>
    <div class="fragment blitz" style="--dauer:50ms;"><img src="./images/eindruck-apple.jpg" alt="Screenshot einer Website"></div><style>
.reveal .slides section .fragment.blitz{opacity:1;visibility:inherit;transition:none;position:absolute;inset:0;display:flex;align-items:center;justify-content:center;pointer-events:none;}
.reveal .slides section .fragment.blitz img{opacity:0;max-height:88%;max-width:94%;width:auto;height:auto;margin:0;box-shadow:0 0 1.5rem rgba(0,0,0,.25);}
.reveal .slides section .fragment.blitz.visible img{animation:blitz-zeigen var(--dauer,50ms) linear 1;}
@keyframes blitz-zeigen{from{opacity:1}to{opacity:1}}
</style>
  </div>
</section>

<section class="simple" data-transition="none">
  <div>
    <h1>Seite 2</h1>
    <p>Daumen hoch oder runter?</p>
    <div class="fragment blitz" style="--dauer:50ms;"><img src="./images/eindruck-arngren.jpg" alt="Screenshot einer Website"></div>
  </div>
</section>

<section class="simple" data-transition="none">
  <div>
    <h1>Seite 3</h1>
    <p>Daumen hoch oder runter?</p>
    <div class="fragment blitz" style="--dauer:50ms;"><img src="./images/eindruck-craigslist.jpg" alt="Screenshot einer Website"></div>
  </div>
</section>

<section class="simple" data-transition="none">
  <div>
    <h1>Seite 4</h1>
    <p>Daumen hoch oder runter?</p>
    <div class="fragment blitz" style="--dauer:50ms;"><img src="./images/eindruck-koeln.jpg" alt="Screenshot einer Website"></div>
  </div>
</section>

{% statement "Und jetzt in Ruhe.", "Hat sich Ihr Urteil geändert?" %}

{% screenshot "./images/eindruck-apple.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Und jetzt? Gleiches Urteil?<br><small>apple.com, Screenshot 2026</small>"}' %}

{% screenshot "./images/eindruck-arngren.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Und jetzt? Gleiches Urteil?<br><small>arngren.net, Screenshot 2026</small>"}' %}

{% screenshot "./images/eindruck-craigslist.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Und jetzt? Gleiches Urteil?<br><small>craigslist.org, Screenshot 2026</small>"}' %}

{% screenshot "./images/eindruck-koeln.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Und jetzt? Gleiches Urteil?<br><small>stadt-koeln.de, Screenshot 2026</small>"}' %}

