---
title: "Ergebnis zuerst"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Startseite von Duolingo (2026), erst scharf, dann unscharf und grau. Das Ergebnis des Tests ist eine Rangfolge: Was sehe ich zuerst, was als Zweites, was als Drittes? Und der Abgleich mit dem Ziel der Seite.

  Ziel der Seite: Menschen sollen anfangen. Ergebnis: Die bunte Illustration hat das meiste Gewicht, dann folgt der Button, dann die Headline. In Farbe springt der grüne Button stärker heraus. In Grau verliert er, weil sein Grün kaum dunkler ist als ein mittleres Grau. Die Hierarchie trägt hier also zu einem guten Teil über Farbe. Für die meisten passt das, für Menschen mit Farbsehschwäche oder auf einem schlechten Display weniger.

  Das ist kein Urteil über Duolingo, sondern zeigt, was der Test sichtbar macht.
---

{% screenshot "./images/test-duolingo.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Scharf und farbig<br><small>de.duolingo.com, Screenshot 2026</small>"}' %}

<section class="simple" data-transition="none">
  <div>
    <h1>Unscharf und grau</h1>
    <div style="display:flex; gap:3vw; align-items:center; width:100%;">
      <figure style="flex:3; margin:0;"><img src="./images/test-duolingo.jpg" alt="Startseite von Duolingo, unscharf und in Graustufen" style="width:100%; height:auto; box-shadow:0 0 1.5rem rgba(0,0,0,.2); filter:blur(0.35vw) grayscale(1);"></figure>
      <div style="flex:2;">
        <p class="list"><strong>1.</strong> Illustration</p>
        <p class="list"><strong>2.</strong> Button »Anfangen«</p>
        <p class="list"><strong>3.</strong> Headline</p>
        {% fragment '<p><strong>Ziel:</strong> anfangen. Der Button trägt, aber vor allem über Farbe.</p>' %}
      </div>
    </div>
  </div>
</section>
