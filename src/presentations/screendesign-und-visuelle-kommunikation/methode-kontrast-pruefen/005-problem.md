---
title: Das Problem
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Unsere Augen sind schlechte Messgeräte. Gesättigte Farben wirken heller, als sie sind (Helmholtz-Kohlrausch), und dieselbe Farbe wirkt je nach Umgebung anders (Simultankontrast). Wer Kontrast nach Augenmaß beurteilt, liegt regelmäßig daneben, und zwar meistens zu optimistisch, weil der eigene Bildschirm gut und hell ist und man weiß, was da steht.

  Das Problem, das die Methode löst: verlässlich und schnell entscheiden, ob Text und Bedienelemente für alle lesbar sind.

  **Der scheinbare Widerspruch zur letzten Woche:** Bei den Täuschungen hieß es »Messen ist gut, Hinschauen ist besser.« Jetzt heißt es messen. Beides stimmt, es sind zwei verschiedene Fragen:

  - **Wirkung (Wie wirkt das?):** Hierarchie, Gleichgewicht, optische Mitte, Farbklima. Es zählt, was gesehen wird. Das Auge ist das richtige Instrument, darum korrigiert man optisch.
  - **Zugänglichkeit (Kommt es bei allen an?):** Hier ist das eigene Auge das falsche Instrument. Wir sind nicht die Zielgruppe: Wir sehen gut, haben einen guten Bildschirm und wissen, was da steht. Die Menschen, um die es geht, sehen wir nicht: mit Sehschwäche, älter, mit billigem Display, in der Sonne. Und die Phänomene der letzten Woche (Simultankontrast, Helmholtz-Kohlrausch) zeigen gerade, dass wir Helligkeit falsch einschätzen. Wenn Wahrnehmung relativ ist, taugt sie nicht als Prüfinstrument für einen festen Mindestwert. Das ist kein Widerspruch, sondern die Konsequenz.

  **Die Messung ist selbst Wahrnehmung, nur gemittelt:** Die WCAG-Formel gewichtet Rot, Grün und Blau so, wie das Auge sie empfindet (relative Leuchtdichte: 0,2126 R + 0,7152 G + 0,0722 B). Sie misst also ein Modell der Wahrnehmung über viele Menschen, unabhängig vom eigenen Auge.

  **Reihenfolge:** Erst messen, dann schauen. 4,5 : 1 ist notwendig, aber nicht hinreichend. Und weil die Formel Schwächen hat (helle Schrift auf Dunkel, kräftige Farben), hat das Auge das letzte Wort, aber nur oberhalb der Untergrenze. Passt zur Haltung »Gefällt mir ist kein Argument«: Ein Messwert ist ein Argument, das man niemandem erklären muss.
---

{% interlude "Ihre Augen sehen nicht für alle.", "Wie prüfen Sie, ob etwas für alle lesbar ist?" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Was denn nun?</h1>
    <p>Letzte Woche: »Messen ist gut, Hinschauen ist besser.« Heute: messen.</p>
    {% fragment '<p class="list"><strong>Wirkung:</strong> Wie wirkt das? Hier entscheidet das Auge.</p>' %}
    {% fragment '<p class="list"><strong>Zugänglichkeit:</strong> Kommt es bei allen an? Hier ist das eigene Auge das falsche Instrument.</p>' %}
  </div>
</section>

{% statement "Messen für die Untergrenze, Hinschauen für die Wirkung.", "Die Messung sagt, ob etwas für alle lesbar ist. Ob es gut ist, sagt sie nicht. Erst messen, dann schauen." %}
