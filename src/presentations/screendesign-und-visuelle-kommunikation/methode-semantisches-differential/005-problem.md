---
title: "Das Problem"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Live-Test (ca. 5 Minuten):** Erst die Aufgabe zeigen, noch ohne Screenshot: Zettel und Stift raus. Dann drei Startseiten von Finanzanbietern nacheinander zeigen, je ca. eine Minute. Jede Person notiert pro Seite still für sich fünf bis zehn Adjektive. Nicht reinrufen: Sonst lehnen sich alle an die ersten Aussagen an, und die Unterschiede verschwinden. Erst danach einsammeln: Einige lesen ihre Wörter zu einer Seite vor, die Wörter an der Tafel sammeln.

  Was dabei passiert: Für dieselbe Seite fallen sehr unterschiedliche Wörter. »Seriös«, »langweilig«, »vertrauenswürdig«, »kalt«. Teils meinen sie dasselbe, teils das Gegenteil, und vergleichen kann man sie nicht. Genau dieses Problem löst das semantische Differenzial: Es gibt die Begriffe vor und macht aus Eindrücken Werte auf einer Skala.

  **Vergleich:** BlackRock und Flossbach von Storch nebeneinander. Beide verkaufen dasselbe, Geldanlage, und wirken trotzdem verschieden. Inwieweit? Die Adjektive von eben helfen, reichen aber nicht: Man merkt, dass man für den Vergleich gemeinsame Begriffe braucht. Das ist die Überleitung zum nächsten Schritt.

  Screenshots: deka.de, flossbachvonstorch.de, blackrock.com, jeweils 2024.
---

{% interlude "Wie wirkt was?", "Notieren Sie fünf bis zehn Adjektive." %}

{% screenshot "./images/deka.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Wie wirkt diese Seite?<br><small>deka.de, Screenshot 2024</small>"}' %}
{% screenshot "./images/flossbach.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Und diese?<br><small>flossbachvonstorch.de, Screenshot 2024</small>"}' %}
{% screenshot "./images/black-rock.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Und diese?<br><small>blackrock.com, Screenshot 2024</small>"}' %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Inwieweit wirken sie unterschiedlich?</h1>
    <div style="display:flex; gap:3vw; align-items:flex-start; width:100%;">
      <figure style="flex:1; margin:0;"><img src="./images/black-rock.jpg" alt="Startseite von BlackRock" style="width:100%; height:auto; box-shadow:0 0 1.5rem rgba(0,0,0,.2);"><figcaption><small>blackrock.com, Screenshot 2024</small></figcaption></figure>
      <figure style="flex:1; margin:0;"><img src="./images/flossbach.jpg" alt="Startseite von Flossbach von Storch" style="width:100%; height:auto; box-shadow:0 0 1.5rem rgba(0,0,0,.2);"><figcaption><small>flossbachvonstorch.de, Screenshot 2024</small></figcaption></figure>
    </div>
  </div>
</section>

{% statement "Zehn Personen, zehn Wörter.", "Eindrücke lassen sich so nicht vergleichen. Das semantische Differenzial gibt die Begriffe vor und macht aus Eindrücken Werte." %}
