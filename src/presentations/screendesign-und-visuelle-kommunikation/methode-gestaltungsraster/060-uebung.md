---
title: "Mini-Übung"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Mini-Übung (5 Minuten), direkt in der Vorlage für heute.**

  Jede Person legt auf dem Frame der Card-Übersicht ein Raster an: 12 Spalten, Stretch, Rand 80, Spaltenabstand 24. Dazu ein Grid mit 8 px für die Grundlinie. Dann prüfen: Passen drei Cards nebeneinander auf je vier Spalten? Oder vier Cards auf je drei Spalten? Wie breit wird eine Card dann?

  Auflösung: drei Cards je 4 Spalten = 4 × 84,67 + 3 × 24 = 410,67 px. Vier Cards je 3 Spalten = 3 × 84,67 + 2 × 24 = 302 px.

  Kurz zeigen lassen, wer was gewählt hat und warum. Das ist die erste Entscheidung für die Varianten danach.
---

{% interlude "Und jetzt Sie", "Fünf Minuten, in der Vorlage für heute" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Legen Sie das Raster für die Card-Übersicht an</h1>
    {% fragment '<p class="list"><strong>Columns:</strong> 12, Stretch, Margin 80, Gutter 24</p>' %}
    {% fragment '<p class="list"><strong>Grid:</strong> 8 px für die Grundlinie</p>' %}
    {% fragment '<p class="list"><strong>Entscheiden:</strong> drei Cards auf je vier Spalten oder vier Cards auf je drei?</p>' %}
  </div>
</section>
