---
title: "Grenzen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Zu viele Ebenen:** Wenn jede Karte, jeder Button und jede Leiste einen eigenen Schatten hat, gibt es keine Rangfolge mehr, nur Unruhe. Wenige feste Stufen, die meisten Elemente flach.

  **Flat Design:** Mit iOS 7 (2013) und Microsofts Metro-Stil wurden Schatten und Glanz fast vollständig entfernt. Das Ergebnis war ruhiger, aber es gingen Hinweise verloren, was man anklicken kann und was davor liegt. Die Nielsen Norman Group hat das später als Problem der Bedienbarkeit beschrieben (»Flat UI Elements Attract Less Attention and Cause Uncertainty«, 2017, aus dem Gedächtnis, bitte prüfen). Heute sind die meisten Systeme wieder »fast flach«: wenig Schatten, aber gezielt.

  **Schatten allein trägt nicht:** Auf dunklem Grund oder bei schwachem Kontrast sind Schatten kaum zu sehen. Im Dark Mode arbeitet Material Design deshalb mit helleren Flächen statt mit Schatten: Was höher liegt, ist heller (tonal elevation, Material 3). Und wer schlecht sieht, sieht den Schatten nicht. Die Fläche selbst muss sich ausreichend abheben.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Wann trägt Räumlichkeit nicht?</h1>
    {% fragment '<p class="list">Wenn alles schwebt: Dann gibt es keine Rangfolge mehr, nur Unruhe.</p>' %}
    {% fragment '<p class="list">Wenn alles flach ist: Dann fehlt der Hinweis, was vorn liegt und was man bedienen kann.</p>' %}
    {% fragment '<p class="list">Wenn nur der Schatten trennt: Auf dunklem Grund und bei schwachem Kontrast verschwindet er.</p>' %}
  </div>
</section>
