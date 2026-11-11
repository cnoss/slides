---
title: "Grenzen und Fehler"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Kombinatorische Explosion:** Fünf Variablen mit je fünf Ausprägungen ergeben 3125 Varianten. Die baut niemand. Deshalb wenige Variablen, oder nur ausgewählte Wege durch den Kasten bauen statt aller.

  **Typische Fehler:** Kombinationen bauen, ohne sie anzuschauen. Sinnlose Varianten nicht aussortieren und dann zwischen Dubletten entscheiden. Und zu glauben, die beste Variante ergebe sich von selbst: Der Kasten liefert Möglichkeiten, die Entscheidung bleibt Ihre.
---

{% interlude "Und bei fünf Variablen?", "5 × 5 × 5 × 5 × 5 = 3125" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Typische Fehler</h1>
    {% fragment '<p class="list">Zu viele Variablen: Der Kasten explodiert</p>' %}
    {% fragment '<p class="list">Kombinieren, ohne hinzuschauen</p>' %}
    {% fragment '<p class="list">Sinnlose Varianten nicht aussortieren</p>' %}
    {% fragment '<p class="list">Glauben, der Kasten entscheidet: Er liefert Möglichkeiten, entscheiden müssen Sie</p>' %}
  </div>
</section>
