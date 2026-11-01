---
title: "Grenzen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Blocksatz kann gut sein:** Im Buch und in Zeitungen funktioniert er, weil Menschen dort jede Zeile von Hand oder mit starken Satzprogrammen ausgleichen. Browser können das bisher schlechter, auch wenn sie aufholen.

  **Zentriert kann richtig sein:** Eine Startseite mit wenig Text, eine Einladung, ein Dialog mit einem Satz. Die Frage ist immer die Länge.

  **Sprachen:** Rechts-nach-links-Schriften wie Arabisch und Hebräisch setzen rechtsbündig, und das ist dort der Standard. »Linksbündig« heißt eigentlich: bündig an der Seite, an der die Zeile beginnt. In CSS deshalb `text-align: start` statt `left`.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Wann bricht die Regel?</h1>
    {% fragment '<p class="list">Im Buch und in der Zeitung: Blocksatz funktioniert mit viel Breite und gutem Ausgleich.</p>' %}
    {% fragment '<p class="list">Bei wenig Text: Eine Einladung darf zentriert sein.</p>' %}
    {% fragment '<p class="list">In anderen Schreibrichtungen: Bündig ist die Seite, an der die Zeile beginnt.</p>' %}
  </div>
</section>
