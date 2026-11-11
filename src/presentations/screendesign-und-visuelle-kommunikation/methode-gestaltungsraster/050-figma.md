---
title: "In Figma"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  In Figma heißt das Raster Layout Guide (früher Layout Grid). Es hängt immer an einem Frame.

  - Frame auswählen, rechts bei Layout guide auf Plus.
  - Typ Columns: Count (Zahl der Spalten), Type Stretch, Margin (Rand), Gutter (Spaltenabstand).
  - Stretch streckt die Spalten über die Breite, Center hält sie in fester Breite in der Mitte, Left und Right richten sie an einer Kante aus.
  - Ein zweiter Layout Guide vom Typ Rows für die Zeilen, ein dritter vom Typ Grid (8 px) für die Grundlinie.
  - Ein- und ausblenden: auf dem Mac Ctrl + G (bitte am Rechner prüfen).
  - Das Raster als Style speichern, dann gilt es für alle Frames gleich.

  In CSS ist es dieselbe Struktur: grid-template-columns: repeat(12, 1fr), gap für den Spaltenabstand, padding für den Rand. Siehe Prinzip Ausrichtung und Raster.
---

{% interlude "In Figma", "Das Raster heißt dort Layout Guide" %}

<section class="simple" data-transition="fade">
<div>

# Layout Guide

| Einstellung | Bedeutung |
|---|---|
| **Columns, Count** | Zahl der Spalten |
| **Type: Stretch** | Spalten strecken sich über die Breite |
| **Type: Center** | Spalten in fester Breite, mittig |
| **Margin** | Rand |
| **Gutter** | Spaltenabstand |
| **Rows, Grid** | Zeilen und Grundlinie |

</div>
</section>
