---
title: "Zeilenabstand"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Zu eng:** Die Zeilen kleben zusammen, die Augen rutschen ab. **Zu weit:** Der Text zerfällt in Streifen, weil die Zeilen weiter voneinander entfernt sind als die Wörter voneinander. Das ist Nähe: Was nah ist, gehört zusammen.

  **Gut:** Für Lesetext 120 bis 150 %. Je länger die Zeile, desto mehr Zeilenabstand braucht sie. Große Überschriften brauchen weniger, oft reichen 110 %. Im CSS ohne Einheit angeben (`line-height: 1.5`), dann wächst der Abstand mit der Schrift mit.
---

<section class="simple" data-transition="none">
  <div>
    <h1>Zu eng: 100 %</h1>
    <p style="font-family:PTserif;font-size:3.2vh;line-height:1.0;max-width:65ch;width:100%;margin:0;text-align:left;hyphens:none;">Beim Lesen gleiten die Augen nicht gleichmäßig über die Zeile. Sie springen von Punkt zu Punkt und ergänzen den Rest aus dem Zusammenhang. Am Zeilenende müssen sie zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang schlecht wieder. Ist sie zu kurz, reißt der Lesefluss ständig ab.</p>
  </div>
</section>

<section class="simple" data-transition="none">
  <div>
    <h1>Zu weit: 220 %</h1>
    <p style="font-family:PTserif;font-size:3.2vh;line-height:2.2;max-width:65ch;width:100%;margin:0;text-align:left;hyphens:none;">Beim Lesen gleiten die Augen nicht gleichmäßig über die Zeile. Sie springen von Punkt zu Punkt und ergänzen den Rest aus dem Zusammenhang. Am Zeilenende müssen sie zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang schlecht wieder. Ist sie zu kurz, reißt der Lesefluss ständig ab.</p>
  </div>
</section>

<section class="simple" data-transition="none">
  <div>
    <h1>Gut: 150 %</h1>
    <p style="font-family:PTserif;font-size:3.2vh;line-height:1.5;max-width:65ch;width:100%;margin:0;text-align:left;hyphens:none;">Beim Lesen gleiten die Augen nicht gleichmäßig über die Zeile. Sie springen von Punkt zu Punkt und ergänzen den Rest aus dem Zusammenhang. Am Zeilenende müssen sie zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang schlecht wieder. Ist sie zu kurz, reißt der Lesefluss ständig ab.</p>
  </div>
</section>
