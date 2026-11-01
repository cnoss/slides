---
title: "Zeilenlänge"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Derselbe Text in drei Breiten. Beim Lesen springen die Augen am Zeilenende zurück an den Anfang der nächsten Zeile.

  **Zu lang:** Der Rücksprung ist weit, man landet leicht in der falschen Zeile. **Zu kurz:** Die Augen springen ständig, der Lesefluss reißt ab, die Wörter verteilen sich unruhig. **Richtig:** 45 bis 75 Zeichen, auf dem Handy dürfen es 35 bis 50 sein.

  Die Breite ist unabhängig von der Bildschirmbreite. Genau das ist der häufigste Fehler am Screen: Der Text läuft einfach über die ganze Breite.

  Im CSS gibt es dafür eine eigene Einheit: `ch`, die Breite der Ziffer Null. Die drei Fassungen hier sind so gesetzt: `max-width: 120ch`, `25ch` und `65ch`.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Zu lang: etwa 120 Zeichen</h1>
    <p style="font-family:PTserif;font-size:2.4vh;line-height:1.5;max-width:120ch;width:100%;margin:0;text-align:left;hyphens:none;">Beim Lesen gleiten die Augen nicht gleichmäßig über die Zeile. Sie springen von Punkt zu Punkt und ergänzen den Rest aus dem Zusammenhang. Am Zeilenende müssen sie zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang schlecht wieder. Ist sie zu kurz, reißt der Lesefluss ständig ab.</p>
  </div>
</section>

<section class="simple" data-transition="none">
  <div>
    <h1>Zu kurz: etwa 25 Zeichen</h1>
    <p style="font-family:PTserif;font-size:2.6vh;line-height:1.4;max-width:25ch;width:100%;margin:0;text-align:left;hyphens:none;">Beim Lesen gleiten die Augen nicht gleichmäßig über die Zeile. Sie springen von Punkt zu Punkt und ergänzen den Rest aus dem Zusammenhang. Am Zeilenende müssen sie zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang schlecht wieder. Ist sie zu kurz, reißt der Lesefluss ständig ab.</p>
  </div>
</section>

<section class="simple" data-transition="none">
  <div>
    <h1>Gut: etwa 65 Zeichen</h1>
    <p style="font-family:PTserif;font-size:3.2vh;line-height:1.5;max-width:65ch;width:100%;margin:0;text-align:left;hyphens:none;">Beim Lesen gleiten die Augen nicht gleichmäßig über die Zeile. Sie springen von Punkt zu Punkt und ergänzen den Rest aus dem Zusammenhang. Am Zeilenende müssen sie zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang schlecht wieder. Ist sie zu kurz, reißt der Lesefluss ständig ab.</p>
  </div>
</section>
