---
title: "Absätze"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Absätze gliedern den Text in Sinnschritte. Zwei Mittel stehen zur Wahl: Abstand oder Einzug. Beides zugleich ist doppelt gemoppelt.

  Am Screen ist der Abstand üblich: etwa eine halbe bis eine ganze Zeile. Der Einzug kommt aus dem Buch, wo Platz gespart werden musste.

  Im CSS: `p + p { margin-top: 1em; }`, keine leeren Absätze.

  Überschriften gehören zu dem, was folgt: Der Abstand nach oben ist größer als der nach unten. Das ist Nähe.
---

<section class="image screenshot no-shadow" data-transition="fade" data-background-transition="none"><figure><div style="width:84%;text-align:left;"><div style="display:flex;gap:4vw;align-items:flex-start;width:100%;"><div style="flex:1;"><p style="font-family:PTserif;font-size:3.1vh;line-height:1.45;margin:0;text-align:left;max-width:34ch;hyphens:none;margin-bottom:1em;">Am Zeilenende springen die Augen zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie ihn schlecht wieder.</p><p style="font-family:PTserif;font-size:3.1vh;line-height:1.45;margin:0;text-align:left;max-width:34ch;hyphens:none;">Ist sie zu kurz, reißt der Lesefluss ständig ab. Steht die nächste Zeile zu dicht darunter, rutschen die Augen ab.</p></div><div style="flex:1;"><p style="font-family:PTserif;font-size:3.1vh;line-height:1.45;margin:0;text-align:left;max-width:34ch;hyphens:none;">Am Zeilenende springen die Augen zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie ihn schlecht wieder.</p><p style="font-family:PTserif;font-size:3.1vh;line-height:1.45;margin:0;text-align:left;max-width:34ch;hyphens:none;text-indent:1.5em;">Ist sie zu kurz, reißt der Lesefluss ständig ab. Steht die nächste Zeile zu dicht darunter, rutschen die Augen ab.</p></div></div></div><figcaption class="bu"><p>Abstand oder Einzug<br><small>Links: Abstand, üblich am Screen. Rechts: Einzug, üblich im Buch</small></p></figcaption></figure></section>
