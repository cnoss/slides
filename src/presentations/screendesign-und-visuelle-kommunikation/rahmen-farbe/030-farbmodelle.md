---
title: Farbmodelle im Screendesign
layout: presentation.11ty.js
slideClasses: images
transition: none
status: ok
speaker: |
  **Farbmodelle im Screendesign (ca. 10 Minuten)**

  Erst die Übersicht, dann pro Modell eine Folie: Was kann es gut, was nicht? Die Stärken und Schwächen nacheinander einblenden.

  RGB und Hex beschreiben, was der Bildschirm tut. HSB/HSV und HSL beschreiben Farbe so, wie Menschen über sie sprechen, und unterscheiden sich nur in der Helligkeitsachse: Bei HSB ist 100 % Helligkeit die reine Farbe, bei HSL ist 100 % immer Weiß. Das HSB- bzw. HSV-Modell hat Alvy Ray Smith 1978 beschrieben.

  **HSL gegen OKLCH:** Die beiden Farbstreifen zeigen den Kern. In HSL haben alle sechs Farben dieselbe Helligkeit von 50 %, trotzdem wirkt Gelb fast weiß und Blau fast schwarz. In OKLCH haben alle 70 % Helligkeit, und sie wirken auch gleich hell. OKLCH ist die wahrnehmungsgleichmäßige Weiterentwicklung von Lab und LCH (CIE 1976), beschrieben von Björn Ottosson (2020). In CSS seit 2023 in allen großen Browsern.

  Abkürzungen: Bei OKLCH steht »OK« für Oklab, Ottossons Farbraum; L ist Lightness, C Chroma (Buntheit), H Hue. Bei CMYK steht K für Key, die Schlüsselfarbe Schwarz, auf die die anderen Platten ausgerichtet werden.

  CMYK brauchen Sie nur, wenn etwas gedruckt wird. Sonderfarbsysteme wie Pantone oder RAL sind keine Farbmodelle, sondern Farbbibliotheken mit festen Namen und Nummern.

  **Im Code:** CSS kennt mehrere Schreibweisen für dieselbe Farbe. Hex und rgb() sind technisch, hsl() ist näher an der Wahrnehmung, oklch() wahrnehmungsgleichmäßig. Damit lassen sich Farbpaletten und Design Tokens sauberer ableiten.
---

{% interlude "Farbmodelle im Screendesign", "Welches Modell wofür?" %}

<section class="simple" data-transition="fade">
<div>

# Farbmodelle im Screendesign

| Modell | Beschreibt | Begegnet Ihnen in |
|---|---|---|
| **RGB / Hex**<br>Red, Green, Blue / Hexadezimal | Rot, Grün, Blau als Lichtfarben | Bildschirm, CSS, Entwicklung |
| **HSB / HSV**<br>Hue, Saturation, Brightness / Value | Farbton, Sättigung, Helligkeit | Farbwähler in Figma, Photoshop |
| **HSL**<br>Hue, Saturation, Lightness | Farbton, Sättigung, Helligkeit (Weiß bei 100 %) | CSS, Farbvarianten ableiten |
| **OKLCH**<br>Oklab Lightness, Chroma, Hue | Helligkeit, Buntheit, Farbton, wahrnehmungsgleichmäßig | Paletten, Design Tokens, modernes CSS |
| **CMYK**<br>Cyan, Magenta, Yellow, Key (Schwarz) | Cyan, Magenta, Gelb, Schwarz als Druckfarben | Druck, Übergabe an Druckerei |

</div>
</section>

<section class="simple" data-transition="fade">
  <div>
    <h1>RGB und Hex <span style="font-size:0.5em; font-weight:normal;">Red, Green, Blue · Hexadezimal</span></h1>
    <div style="display:flex; gap:4rem; text-align:left;">
      <div style="flex:1;">
        <p><strong>Kann gut</strong></p>
        {% fragment '<p class="list">Beschreibt direkt, was der Bildschirm tut</p>' %}
        {% fragment '<p class="list">Überall verfügbar: CSS, Figma, jedes Werkzeug</p>' %}
        {% fragment '<p class="list">Hex ist kompakt zum Kopieren und Weitergeben</p>' %}
      </div>
      <div style="flex:1;">
        <p><strong>Kann nicht so gut</strong></p>
        {% fragment '<p class="list">Für Menschen kaum lesbar: Welche Farbe ist <code>#9313ce</code>?</p>' %}
        {% fragment '<p class="list">Hellere oder dunklere Varianten lassen sich schwer ableiten</p>' %}
        {% fragment '<p class="list">Die Zahlen sagen nichts über die wahrgenommene Helligkeit</p>' %}
      </div>
    </div>
  </div>
</section>

<section class="simple" data-transition="fade">
  <div>
    <h1>HSB und HSV <span style="font-size:0.5em; font-weight:normal;">Hue, Saturation, Brightness · Value</span></h1>
    <div style="display:flex; gap:4rem; text-align:left;">
      <div style="flex:1;">
        <p><strong>Kann gut</strong></p>
        {% fragment '<p class="list">Intuitiv: erst den Farbton, dann Sättigung und Helligkeit</p>' %}
        {% fragment '<p class="list">Standard im Farbwähler von Figma, Photoshop und Co.</p>' %}
        {% fragment '<p class="list">Gut zum Variieren entlang einer Achse</p>' %}
      </div>
      <div style="flex:1;">
        <p><strong>Kann nicht so gut</strong></p>
        {% fragment '<p class="list">Gibt es nicht in CSS, muss umgerechnet werden</p>' %}
        {% fragment '<p class="list">Gleiche Helligkeitswerte wirken je nach Farbton verschieden hell</p>' %}
        {% fragment '<p class="list">Leicht zu verwechseln mit HSL</p>' %}
      </div>
    </div>
  </div>
</section>

<section class="simple" data-transition="fade">
  <div>
    <h1>HSL <span style="font-size:0.5em; font-weight:normal;">Hue, Saturation, Lightness</span></h1>
    <div style="display:flex; gap:4rem; text-align:left;">
      <div style="flex:1;">
        <p><strong>Kann gut</strong></p>
        {% fragment '<p class="list">In CSS direkt nutzbar</p>' %}
        {% fragment '<p class="list">Varianten über die Helligkeit ableiten, z. B. für Hover-Zustände</p>' %}
        {% fragment '<p class="list">Farbton als Zahl: gut für systematische Paletten</p>' %}
      </div>
      <div style="flex:1;">
        <p><strong>Kann nicht so gut</strong></p>
        {% fragment '<p class="list">Nicht wahrnehmungsgleichmäßig: Gelb wirkt viel heller als Blau</p>' %}
        {% fragment '<p class="list">Gleiche Abstufungen wirken ungleichmäßig</p>' %}
        {% fragment '<p class="list">100 % Helligkeit ist immer Weiß, anders als bei HSB</p>' %}
      </div>
    </div>
    <div style="display:flex; gap:0.6vw; margin-top:3vh; width:100%;"><div style="flex:1; height:9vh; background:hsl(0 100% 50%);"></div><div style="flex:1; height:9vh; background:hsl(60 100% 50%);"></div><div style="flex:1; height:9vh; background:hsl(120 100% 50%);"></div><div style="flex:1; height:9vh; background:hsl(180 100% 50%);"></div><div style="flex:1; height:9vh; background:hsl(240 100% 50%);"></div><div style="flex:1; height:9vh; background:hsl(300 100% 50%);"></div></div>
    <p style="font-size:0.5em; margin-top:1vh;"><code>hsl(h 100% 50%)</code>: gleiche Helligkeit laut Zahl, sehr unterschiedlich hell fürs Auge</p>
  </div>
</section>

<section class="simple" data-transition="fade">
  <div>
    <h1>OKLCH <span style="font-size:0.5em; font-weight:normal;">Oklab Lightness, Chroma, Hue</span></h1>
    <div style="display:flex; gap:4rem; text-align:left;">
      <div style="flex:1;">
        <p><strong>Kann gut</strong></p>
        {% fragment '<p class="list">Wahrnehmungsgleichmäßig: gleiche Zahl, gleiche gefühlte Helligkeit</p>' %}
        {% fragment '<p class="list">Paletten und Design Tokens systematisch ableiten</p>' %}
        {% fragment '<p class="list">Kontraste besser planbar, größerer Farbraum (Display P3)</p>' %}
      </div>
      <div style="flex:1;">
        <p><strong>Kann nicht so gut</strong></p>
        {% fragment '<p class="list">Noch neu und ungewohnt</p>' %}
        {% fragment '<p class="list">Noch nicht in allen Design-Werkzeugen verfügbar</p>' %}
        {% fragment '<p class="list">Manche Werte liegen außerhalb dessen, was ein Bildschirm darstellen kann</p>' %}
      </div>
    </div>
    <div style="display:flex; gap:0.6vw; margin-top:3vh; width:100%;"><div style="flex:1; height:9vh; background:oklch(70% 0.13 25);"></div><div style="flex:1; height:9vh; background:oklch(70% 0.13 85);"></div><div style="flex:1; height:9vh; background:oklch(70% 0.13 145);"></div><div style="flex:1; height:9vh; background:oklch(70% 0.13 205);"></div><div style="flex:1; height:9vh; background:oklch(70% 0.13 265);"></div><div style="flex:1; height:9vh; background:oklch(70% 0.13 325);"></div></div>
    <p style="font-size:0.5em; margin-top:1vh;"><code>oklch(70% 0.13 h)</code>: gleiche Helligkeit laut Zahl, auch fürs Auge gleich hell</p>
  </div>
</section>

<section class="simple" data-transition="fade">
  <div>
    <h1>CMYK <span style="font-size:0.5em; font-weight:normal;">Cyan, Magenta, Yellow, Key (Schwarz)</span></h1>
    <div style="display:flex; gap:4rem; text-align:left;">
      <div style="flex:1;">
        <p><strong>Kann gut</strong></p>
        {% fragment '<p class="list">Sagt das Druckergebnis voraus</p>' %}
        {% fragment '<p class="list">Standard für die Übergabe an die Druckerei</p>' %}
        {% fragment '<p class="list">Sauberes Schwarz durch eigene Druckfarbe (K)</p>' %}
      </div>
      <div style="flex:1;">
        <p><strong>Kann nicht so gut</strong></p>
        {% fragment '<p class="list">Kleinerer Farbraum: Leuchtende Bildschirmfarben lassen sich nicht drucken</p>' %}
        {% fragment '<p class="list">Für Web und App ohne Bedeutung</p>' %}
        {% fragment '<p class="list">Ergebnis hängt von Papier und Druckverfahren ab (Farbprofil)</p>' %}
      </div>
    </div>
  </div>
</section>

<section class="simple" data-transition="fade">
  <div>
    <h1>Im Code: eine Farbe, vier Schreibweisen</h1>
    <div style="display:flex; gap:3rem; align-items:center; margin-top:1rem;">
      <div style="width:22vh; height:22vh; background:#9313ce; flex:none;"></div>
      <div>
        {% fragment '<p class="list"><code>#9313ce</code> Hex</p>' %}
        {% fragment '<p class="list"><code>rgb(147 19 206)</code> Rot, Grün, Blau</p>' %}
        {% fragment '<p class="list"><code>hsl(281 83% 44%)</code> Farbton, Sättigung, Helligkeit</p>' %}
        {% fragment '<p class="list"><code>oklch(51.5% 0.25 310)</code> wahrnehmungsgleichmäßig</p>' %}
      </div>
    </div>
  </div>
</section>
