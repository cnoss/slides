---
title: "Grenzen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Das Raster ist ein Werkzeug, kein Käfig.** Wathan und Schoger (Refactoring UI) schreiben ausdrücklich »Grids are overrated«: Nicht alles muss sich in Prozentspalten auflösen. Eine Seitenleiste mit fester Breite oder ein Formular mit fester Maximalbreite ist oft besser als eine Breite, die sich aus Spalten ergibt.

  **Optik schlägt Mathematik:** Kreise, Dreiecke und Icons wirken an einer exakten Kante eingerückt. Dann wird optisch korrigiert, nicht nach dem Raster (siehe Optische Korrektur).

  **Bruch braucht Ordnung:** Ein Rasterbruch wirkt nur vor einem Raster. Wer nie ein Raster hatte, kann es auch nicht brechen, es sieht dann einfach unordentlich aus.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Wann trägt das Raster nicht?</h1>
    {% fragment '<p class="list">Wenn es zum Käfig wird: Manche Elemente brauchen eine feste Breite statt einer Spaltenbreite.</p>' %}
    {% fragment '<p class="list">Wenn die Rechnung stimmt, aber das Auge nicht: Dann optisch korrigieren.</p>' %}
    {% fragment '<p class="list">Wenn alles gebrochen wird: Ein Bruch wirkt nur vor einer Ordnung.</p>' %}
  </div>
</section>
