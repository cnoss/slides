---
title: Graustufentest
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Vier Farbkombinationen. Erst in Farbe zeigen: Welche lesen sich gut? Dann dieselbe Folie in Graustufen. Was dort verschwindet, hat keinen Helligkeitskontrast: Rot auf Grün und Rot auf Blau sind fast gleich hell, Gelb auf Weiß ebenso. Nur Schwarz auf Gelb bleibt.

  Der Graustufentest ist die schnellste Prüfung im Entwurf: In Figma ein Rechteck mit Füllung Schwarz und Ebenenmodus »Color« (oder »Saturation«) über den Entwurf legen. Im Browser: CSS-Filter grayscale. Ausführlich: Methode Kontrast prüfen.

  Die Graustufen-Fassung ist dieselbe Folie mit dem CSS-Filter grayscale(1).
---

<section class="simple" data-transition="none">
  <div>
      <p style="background:#1a8a3a; color:#d81e2c; padding:1.2vh 2vw; margin:0 0 1.2vh; font-size:4vh; font-weight:600;">Rot auf Grün: Kann man das lesen?</p>
      <p style="background:#0082ff; color:#ff2a2a; padding:1.2vh 2vw; margin:0 0 1.2vh; font-size:4vh; font-weight:600;">Rot auf Blau: Kann man das lesen?</p>
      <p style="background:#ffffff; color:#f7d117; padding:1.2vh 2vw; margin:0 0 1.2vh; font-size:4vh; font-weight:600;">Gelb auf Weiß: Kann man das lesen?</p>
      <p style="background:#f7d117; color:#231f20; padding:1.2vh 2vw; margin:0 0 1.2vh; font-size:4vh; font-weight:600;">Schwarz auf Gelb: Kann man das lesen?</p>
  </div>
</section>
<section class="simple" data-transition="none">
  <div style="filter:grayscale(1);">
      <p style="background:#1a8a3a; color:#d81e2c; padding:1.2vh 2vw; margin:0 0 1.2vh; font-size:4vh; font-weight:600;">Rot auf Grün: Kann man das lesen?</p>
      <p style="background:#0082ff; color:#ff2a2a; padding:1.2vh 2vw; margin:0 0 1.2vh; font-size:4vh; font-weight:600;">Rot auf Blau: Kann man das lesen?</p>
      <p style="background:#ffffff; color:#f7d117; padding:1.2vh 2vw; margin:0 0 1.2vh; font-size:4vh; font-weight:600;">Gelb auf Weiß: Kann man das lesen?</p>
      <p style="background:#f7d117; color:#231f20; padding:1.2vh 2vw; margin:0 0 1.2vh; font-size:4vh; font-weight:600;">Schwarz auf Gelb: Kann man das lesen?</p>
  </div>
</section>
