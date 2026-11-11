---
title: "Typische Fehler"
layout: presentation.11ty.js
slideClasses: simple
status: ok
speaker: |
  Der häufigste Fehler: das Raster anlegen und dann nicht benutzen. Elemente stehen »fast« auf der Kante. Der zweithäufigste: das Raster des Frameworks übernehmen, ohne zu prüfen, ob der Text darin gut lesbar ist.

  Und: Der Spaltenabstand ist nicht beliebig. Er ist der wichtigste Abstand auf der Seite und gehört ins Spacing-System.
---

{% fragment '<p class="list">Das Raster anlegen und nicht benutzen: Elemente stehen »fast« auf der Kante</p>' %}
{% fragment '<p class="list">Ein Raster von der Stange übernehmen, ohne den Inhalt zu messen</p>' %}
{% fragment '<p class="list">Spaltenabstand und Rand nach Gefühl statt aus dem Spacing-System</p>' %}
{% fragment '<p class="list">Ein Raster für alle Formate, statt eines pro Breite</p>' %}
{% fragment '<p class="list">Die Senkrechte vergessen: Höhen und Abstände ohne Grundlinie</p>' %}
