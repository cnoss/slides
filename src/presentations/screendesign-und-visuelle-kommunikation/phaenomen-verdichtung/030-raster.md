---
title: "Erkennen Sie das?"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Dasselbe Prinzip, mit einem Bild. Jeder Punkt ist so groß, wie die Stelle im Bild dunkel ist. Erst raten lassen: Was ist das? Bei 320 Punkten erkennt es kaum jemand, bei 1280 die meisten, bei 6480 alle. Gute Verbindung zum Phänomen Sinnsuche: Wer das Bild kennt, erkennt es früher.

  Die Rasterbilder sind mit einem kleinen Skript aus einem gemeinfreien Foto der Mona Lisa erzeugt (Leonardo da Vinci, um 1503 bis 1519, Musée du Louvre, Wikimedia Commons). Genau so funktioniert der Rasterdruck in Zeitungen.
---

{% interlude "Erkennen Sie das?", "Jeder Punkt ist so groß, wie die Stelle im Bild dunkel ist." %}

{% screenshot "./images/raster-16.svg", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"320 Punkte"}' %}
{% screenshot "./images/raster-32.svg", '{"transition":"none", "classes":"no-shadow", "width":"auto", "bu":"1280 Punkte"}' %}
{% screenshot "./images/raster-72.svg", '{"transition":"none", "classes":"no-shadow", "width":"auto", "bu":"6480 Punkte<br><small>Leonardo da Vinci, Mona Lisa, gerastert. Vorlage gemeinfrei</small>"}' %}
