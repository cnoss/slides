---
title: "Ergebnis zuerst"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  So sieht das Ergebnis aus: eine kleine Skala mit Namen. Mehr nicht. Jeder Abstand im Entwurf stammt aus dieser Tabelle, und jeder hat einen Namen, den Gestaltung und Entwicklung gleich verwenden.

  Die Werte wachsen nicht gleichmäßig. Kleine Schritte unten, wo feine Unterschiede zählen, große Schritte oben, wo ein Unterschied von 4 Pixeln niemandem auffällt. Die Basis ist hier 4 bzw. 8, weil sich damit gut rechnen lässt und viele Bildschirmgrößen durch 8 teilbar sind.

  Die Spalte »In der Card« zeigt, wo die Werte in der Card vom Live-Test sitzen.
---

{% interlude "Ergebnis zuerst", "Eine Skala, sieben Werte, jeder mit Namen" %}

<section class="simple" data-transition="fade">
<div>

# Eine Skala für alle Abstände

| Name | Wert | In der Card |
|---|---|---|
| **space-xs** | 4 px | Abstand im Icon, sehr feine Abstände |
| **space-s** | 8 px | Kategorie zu Titel, Link zu Pfeil |
| **space-m** | 16 px | Titel zu Teaser |
| **space-l** | 24 px | Innenabstand der Card, Teaser zu Link |
| **space-xl** | 32 px | zwischen zwei Cards |
| **space-2xl** | 48 px | zwischen zwei Abschnitten |
| **space-3xl** | 64 px | großer Seitenrand |

</div>
</section>
