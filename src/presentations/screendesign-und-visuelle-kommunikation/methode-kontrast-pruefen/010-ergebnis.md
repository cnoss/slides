---
title: Ergebnis zuerst
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  So sieht das Ergebnis aus: eine Liste aller Farbpaare eines Entwurfs, jeweils mit gemessenem Kontrastverhältnis, dem geltenden Grenzwert und einer Bewertung. Wer mit Design Tokens arbeitet, prüft die Paare der Tokens einmal und hat damit das ganze System abgedeckt.

  Die Werte sind berechnet. Das Beispiel ist erfunden, die Farben stammen aus diesem Modul.
---

<section class="simple" data-transition="fade">
<div>

# So sieht das Ergebnis aus

| Paar | Verwendung | Kontrast | Grenzwert | Ergebnis |
|---|---|---|---|---|
| #231f20 auf #ffffff | Fließtext | 16,3 : 1 | 4,5 : 1 | besteht |
| #888888 auf #ffffff | Bildunterschrift | 3,54 : 1 | 4,5 : 1 | **fällt durch** |
| #6a6a6a auf #ffffff | Bildunterschrift, korrigiert | 5,41 : 1 | 4,5 : 1 | besteht |
| #ffffff auf #9313ce | Button, 18 px fett | 6,51 : 1 | 4,5 : 1 | besteht |
| #d9d9d9 auf #ffffff | Rahmen Eingabefeld | 1,41 : 1 | 3 : 1 | **fällt durch** |

</div>
</section>
