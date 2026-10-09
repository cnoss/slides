---
title: Mini-Übung
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Mini-Übung (ca. 12 Minuten)**

  Papier und Stift. Jeder Screen erscheint beim Weiterschalten für genau 5 Sekunden und verschwindet dann von selbst. Danach eine Minute still schreiben, erst dann der nächste Screen. Am Ende zu zweit vergleichen und gemeinsam auflösen.

  Screen 1: linear.app, ein Werkzeug für Projekt- und Aufgabenplanung in Softwareteams. Der Claim »The product development system for teams and agents« ist für Außenstehende schwer zu entschlüsseln. Typische Antworten: »irgendwas mit KI«, »Software«, »keine Ahnung«.

  Screen 2: Too Good To Go, eine App gegen Lebensmittelverschwendung. Der Claim »Rette gute Lebensmittel vor der Verschwendung« ist sofort klar, die Handlung (App herunterladen) meist auch.

  Auswertung an der Tafel: Bei welchem Screen sind die Antworten einheitlicher? Woran liegt das? Was würden Sie bei Screen 1 ändern?

  Technik: Zurück und wieder vor startet die fünf Sekunden neu.
---

{% interlude "Und jetzt Sie.", "Zwei Screens, je fünf Sekunden" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>So geht's</h1>
    {% fragment '<p class="list">Sie sehen einen Screen genau 5 Sekunden.</p>' %}
    {% fragment '<p class="list">Danach schreiben Sie still auf: Worum geht es? Was kann man hier tun? Was ist Ihnen aufgefallen?</p>' %}
    {% fragment '<p class="list">Dann vergleichen Sie zu zweit.</p>' %}
  </div>
</section>

<section class="simple" data-transition="none">
  <div>
    <h1>Screen 1</h1>
    <p>Gleich fünf Sekunden. Bereit?</p>
    <div class="fragment blitz" style="--dauer:5s;"><img src="./images/test-linear.jpg" alt="Screenshot einer Website"></div><style>
.reveal .slides section .fragment.blitz{opacity:1;visibility:inherit;transition:none;position:absolute;inset:0;display:flex;align-items:center;justify-content:center;pointer-events:none;}
.reveal .slides section .fragment.blitz img{opacity:0;max-height:88%;max-width:94%;width:auto;height:auto;margin:0;box-shadow:0 0 1.5rem rgba(0,0,0,.25);}
.reveal .slides section .fragment.blitz.visible img{animation:blitz-zeigen var(--dauer,50ms) linear 1;}
@keyframes blitz-zeigen{from{opacity:1}to{opacity:1}}
</style>
  </div>
</section>

{% question "Schreiben Sie auf.", "Worum geht es? Was kann man hier tun? Was ist Ihnen aufgefallen?" %}

<section class="simple" data-transition="none">
  <div>
    <h1>Screen 2</h1>
    <p>Gleich fünf Sekunden. Bereit?</p>
    <div class="fragment blitz" style="--dauer:5s;"><img src="./images/test-tgtg.jpg" alt="Screenshot einer Website"></div>
  </div>
</section>

{% question "Schreiben Sie auf.", "Worum geht es? Was kann man hier tun? Was ist Ihnen aufgefallen?" %}

{% question "Vergleichen Sie zu zweit.", "Wo sind Sie sich einig? Wo nicht?" %}

{% screenshot "./images/test-linear.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Und, kam es an?<br><small>linear.app, Screenshot 2026</small>"}' %}
{% screenshot "./images/test-tgtg.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Und, kam es an?<br><small>toogoodtogo.com, Screenshot 2026</small>"}' %}
