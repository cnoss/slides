---
title: "Der Kasten"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Der Kasten ist eine Tabelle: In den Zeilen stehen die Variablen, in den Spalten ihre Ausprägungen. Jede Variante ist ein Weg durch den Kasten, aus jeder Zeile genau eine Zelle.

  Der lila Weg: Bild oben, Titel L, Fläche hellgrau. Das ist eine von 64 Karten.

  Die Variablen kommen aus dem Variieren entlang einer Achse: Jede Achse, bei der man unsicher war, wird eine Zeile. Die Stufen der Achse werden die Ausprägungen.

  **Hintergrund**

  Die Methode geht auf Fritz Zwicky zurück (1898 bis 1974), Schweizer Astrophysiker am California Institute of Technology. Er hat sie in den 1940er-Jahren unter anderem für Raketenantriebe entwickelt, um alle denkbaren Lösungen eines Problems systematisch zu erfassen. Buch: »Entdecken, Erfinden, Forschen im morphologischen Weltbild« (1966). Daten aus dem Gedächtnis, bitte prüfen.
---

{% interlude "Der Kasten", "Variablen in die Zeilen, Ausprägungen in die Spalten" %}

<section class="simple" data-transition="fade">
<div>

# Drei Variablen, je vier Ausprägungen

| Variable | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **Bildposition** | oben | links | als Hintergrund | ohne Bild |
| **Titelgröße** | S | M | L | XL |
| **Fläche** | keine | hellgrau | Rahmen | dunkel |

</div>
</section>

<section class="simple" data-transition="none">
<div>

# Eine Variante ist ein Weg durch den Kasten

| Variable | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **Bildposition** | <span style="background:#9313ce;color:#ffffff;padding:.2em .6em;">oben</span> | links | als Hintergrund | ohne Bild |
| **Titelgröße** | S | M | <span style="background:#9313ce;color:#ffffff;padding:.2em .6em;">L</span> | XL |
| **Fläche** | keine | <span style="background:#9313ce;color:#ffffff;padding:.2em .6em;">hellgrau</span> | Rahmen | dunkel |

</div>
</section>
