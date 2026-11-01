---
title: "Auf dem Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die wichtigste Folge fürs Screendesign: Versalien, also durchgehende Großbuchstaben, lesen sich schlechter. Alle Wörter haben dieselbe rechteckige Form, Ober- und Unterlängen fehlen, und wir sind diese Form nicht gewohnt. Versalsatz kostet messbar Zeit und auch Platz.

  Für ein, zwei Wörter ist das kein Problem: ein Label, ein kurzer Button, eine Dachzeile. Für einen Satz oder einen Absatz schon. Und Versalien wirken laut.

  Im Code: Text normal schreiben und über CSS umstellen (`text-transform: uppercase`), nicht in Großbuchstaben tippen. Screenreader lesen getippte Versalien teils Buchstabe für Buchstabe vor.

  **Hintergrund**

  Miles Tinker und Donald Paterson haben schon 1928 gemessen, dass Versalsatz langsamer gelesen wird als gemischte Schreibung. Tinker fasst das in »Legibility of Print« (1963) zusammen. Ein Teil des Effekts ist Übung: Wer viel Versalsatz liest, wird schneller.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Welchen lesen Sie lieber?</h1>
    <div style="display:flex;gap:3vw;align-items:flex-start;width:100%;"><p style="font-family:PTsans;font-size:3.4vh;line-height:1.45;hyphens:none;margin:0;background:#e4e4e4;padding:1.2em 1.4em 2.2em;text-align:left;flex:1;">BITTE BEACHTEN SIE, DASS IHRE BESTELLUNG ERST NACH EINGANG DER ZAHLUNG BEARBEITET WIRD. ÄNDERUNGEN SIND DANACH NUR NOCH ÜBER DEN KUNDENDIENST MÖGLICH.</p><p style="font-family:PTsans;font-size:3.4vh;line-height:1.45;hyphens:none;margin:0;background:#e4e4e4;padding:1.2em 1.4em 2.2em;text-align:left;flex:1;">Bitte beachten Sie, dass Ihre Bestellung erst nach Eingang der Zahlung bearbeitet wird. Änderungen sind danach nur noch über den Kundendienst möglich.</p></div>
  </div>
</section>

{% statement "Versalien nur für Kurzes.", "Ein Label, ein Button, eine Dachzeile: gut. Ein ganzer Satz: schlecht." %}
