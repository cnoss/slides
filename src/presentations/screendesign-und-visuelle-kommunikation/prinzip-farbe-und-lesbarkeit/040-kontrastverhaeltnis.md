---
title: Kontrastverhältnis
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die WCAG machen Helligkeitskontrast messbar: Das Kontrastverhältnis vergleicht die relative Leuchtdichte von Vorder- und Hintergrund. Es reicht von 1 : 1 (gleiche Farbe) bis 21 : 1 (Schwarz auf Weiß).

  **Die Grenzwerte (WCAG 2.2, Stufe AA):**
  - Text: mindestens 4,5 : 1 (Kriterium 1.4.3)
  - Große Schrift (ab 24 px oder ab ca. 19 px fett): mindestens 3 : 1
  - Bedienelemente und informationstragende Grafik, z. B. Rahmen von Eingabefeldern, Icons: mindestens 3 : 1 (Kriterium 1.4.11)
  - Stufe AAA für Text: 7 : 1 (Kriterium 1.4.6)

  **Die Beispiele (berechnet):** #777777 auf Weiß hat 4,48 : 1 und fällt knapp durch, #767676 hat 4,54 : 1 und besteht. Mit bloßem Auge ist der Unterschied nicht zu sehen, deshalb messen. Weiß auf dem Blau #1f6fff hat 4,4 : 1, also für Fließtext zu wenig, für einen Button mit großer, fetter Schrift genug. Unser Lila #9313ce auf Weiß hat 6,51 : 1.

  In Deutschland verlangt das Barrierefreiheitsstärkungsgesetz seit Juni 2025 für viele digitale Angebote die Einhaltung der WCAG.
---

{% interlude "Kontrast lässt sich messen.", "Das Kontrastverhältnis nach WCAG" %}

<section class="simple" data-transition="fade">
<div>

# Wie viel Kontrast braucht es?

| Was | Mindestens (AA) | Erhöht (AAA) |
|---|---|---|
| **Text** | 4,5 : 1 | 7 : 1 |
| **Große Schrift**<br>ab 24 px oder ca. 19 px fett | 3 : 1 | 4,5 : 1 |
| **Bedienelemente und Grafik**<br>Rahmen, Icons, Diagramme | 3 : 1 | |

</div>
</section>

<section class="simple" data-transition="fade">
  <div>
    <h1>Messen statt schätzen</h1>
    <p style="color:#777777; font-size:3.4vh; margin:0 0 1vh;">#777777 auf Weiß: 4,48 : 1, knapp nicht ausreichend</p>
    <p style="color:#767676; font-size:3.4vh; margin:0 0 1vh;">#767676 auf Weiß: 4,54 : 1, ausreichend</p>
    <p style="color:#9313ce; font-size:3.4vh; margin:0 0 1vh;">#9313ce auf Weiß: 6,51 : 1</p>
    <p style="color:#ffffff; background:#1f6fff; font-size:3.4vh; padding:0.6vh 1vw; display:inline-block; margin:0;">Weiß auf #1f6fff: 4,4 : 1, nur für große Schrift</p>
  </div>
</section>
