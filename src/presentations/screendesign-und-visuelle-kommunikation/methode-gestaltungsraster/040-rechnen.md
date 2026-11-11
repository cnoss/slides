---
title: "Rechnen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Spaltenbreite ist keine Eingabe, sie ergibt sich: Breite minus beide Ränder minus alle Spaltenabstände, geteilt durch die Zahl der Spalten.

  Desktop: (1440 − 2 × 80 − 11 × 24) ÷ 12 = 1016 ÷ 12 = 84,67 px.
  Tablet: (834 − 2 × 40 − 7 × 24) ÷ 8 = 586 ÷ 8 = 73,25 px.
  Smartphone: (390 − 2 × 20 − 3 × 16) ÷ 4 = 302 ÷ 4 = 75,5 px.

  Krumme Werte sind normal. In Figma (Stretch) und in CSS (1fr) werden die Spalten ohnehin gestreckt. Was zählt, sind Rand und Spaltenabstand: Die bleiben fest und kommen aus Ihrem Spacing-System.

  Probe für den Lesetext: Sechs Spalten auf dem Desktop sind 6 × 84,67 + 5 × 24 = 628 px. Bei 18 px Schrift sind das grob 70 Zeichen. Passt.

  Dieselben Werte stehen in der Aufgabe »Textsatz für NOXA Analytik«.
---

{% interlude "Rechnen Sie mit", "Die Spaltenbreite ergibt sich" %}

<section class="simple" data-transition="fade">
<div>

# Spaltenbreite = (Breite − 2 × Rand − Spaltenabstände) ÷ Spalten

| Format | Breite | Spalten | Rand | Spaltenabstand | Spalte |
|---|---|---|---|---|---|
| **Desktop** | 1440 px | 12 | 80 px | 24 px | 84,67 px |
| **Tablet hoch** | 834 px | 8 | 40 px | 24 px | 73,25 px |
| **Smartphone** | 390 px | 4 | 20 px | 16 px | 75,5 px |

</div>
</section>

{% statement "Rand und Spaltenabstand legen Sie fest. Die Spalte ergibt sich.", "Krumme Spaltenbreiten sind normal, Figma und CSS strecken sie ohnehin. Probe: Sechs Spalten auf dem Desktop ergeben 628 px, gut 70 Zeichen Lesetext." %}
