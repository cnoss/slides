---
title: "Zahlenreihen"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  **Zahlenreihen** sind Proportion zum Mitnehmen: Statt jede Größe einzeln zu erfinden, wählt man aus einer Reihe, deren Werte in einem festen Verhältnis zueinander stehen. Dann passen Schriftgrade, Abstände und Flächen von selbst zusammen.

  **Fibonacci-Folge:** Jede Zahl ist die Summe der beiden davor: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144. Das Verhältnis zweier Nachbarn nähert sich schnell dem Goldenen Schnitt (34 : 21 ≈ 1,619). Benannt nach Leonardo von Pisa, genannt Fibonacci, »Liber abaci« (1202), der damit das Wachstum einer Kaninchenpopulation durchrechnet. In der Typografie lässt sich die Reihe direkt als Schriftgrad-Skala nutzen: 13, 21, 34, 55.

  **Renard-Reihen:** Charles Renard, französischer Militäringenieur, standardisierte um 1877 die Kabel für Fesselballone und reduzierte dabei die Zahl der Varianten drastisch (laut bisherigem Foliensatz von 425 auf 17). Seine Reihen teilen jede Zehnerpotenz in gleich große Stufen: R5 in fünf Stufen mit dem Faktor fünfte Wurzel aus 10, also ≈ 1,585, also 10, 16, 25, 40, 63, 100. R10 in zehn Stufen mit dem Faktor zehnte Wurzel aus 10, also ≈ 1,259: 10, 12,5, 16, 20, 25, 31,5, 40, 50, 63, 80, 100. Genormt als Normzahlen (DIN 323, ISO 3). Im Alltag stecken sie zum Beispiel in Leitungsquerschnitten (1,5, 2,5, 4, 6, 10, 16, 25 mm²), bitte prüfen.

  **Die Pointe für den Screen:** R5 liegt nah am Goldenen Schnitt (1,585 gegen 1,618), R10 nah an der beliebten Typo-Skala 1,25 (große Terz). R5 beginnt bei 10 und enthält die 16: Mit 16 px als Grundschrift ergibt sich 10, 16, 25, 40, 63. Die klassische Schriftgradreihe des Bleisatzes (6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 21, 24, 36, 48, 60, 72 Punkt) ist dagegen keine geometrische Reihe, sondern eine über Jahrhunderte gewachsene Auswahl. Bringhurst druckt sie in »The Elements of Typographic Style« ab (bitte prüfen).

  Die Beispiele sind mit IBM Plex Sans live gesetzt. Die Größen sind auf den Beamer skaliert, die Verhältnisse stimmen. Der Seitenaufbau greift das Beispiel aus dem bisherigen Foliensatz auf: Positionen und Schriftgrade aus derselben Reihe.

  **Hintergrund**

  Normzahlen: DIN 323, ISO 3 und ISO 17. Fibonacci: »Liber abaci«, 1202. Renard: um 1877. Angaben teils aus dem Gedächtnis, bitte prüfen.
---

{% interlude "Zahlenreihen", "Größen aus einer Reihe statt aus dem Bauch" %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Fibonacci: Jede Zahl ist die Summe der beiden davor"}' %}
<rect data-id="b0" x="150" y="47.0" width="4.6" height="26" fill="#888888" />
<rect data-id="b1" x="150" y="85.0" width="4.6" height="26" fill="#888888" />
<rect data-id="b2" x="150" y="123.0" width="9.2" height="26" fill="#888888" />
<rect data-id="b3" x="150" y="161.0" width="13.8" height="26" fill="#888888" />
<rect data-id="b4" x="150" y="199.0" width="23.0" height="26" fill="#888888" />
<rect data-id="b5" x="150" y="237.0" width="36.8" height="26" fill="#888888" />
<rect data-id="b6" x="150" y="275.0" width="59.8" height="26" fill="#9313ce" />
<rect data-id="b7" x="150" y="313.0" width="96.6" height="26" fill="#9313ce" />
<rect data-id="b8" x="150" y="351.0" width="156.4" height="26" fill="#9313ce" />
<rect data-id="b9" x="150" y="389.0" width="253.0" height="26" fill="#9313ce" />
<rect data-id="b10" x="150" y="427.0" width="409.4" height="26" fill="#888888" />
{% endframe %}
<section class="simple" data-transition="fade">
  <div>
    <h1>Fibonacci als Schriftgrade</h1>
    <div style="width:100%;text-align:left;"><div style="display:flex;align-items:baseline;gap:2.5vw;margin:0 0 1.6vh;"><div style="width:9vw;flex:none;font-family:RobotoCode;font-size:2vh;color:#6a6a6a;text-align:right;">13</div><div style="width:10vw;flex:none;font-family:IBM;font-size:1.8vh;color:#6a6a6a;">Text</div><div style="font-family:IBM;font-weight:400;font-size:2.08vh;line-height:1.1;white-space:nowrap;color:#231f20;">Gute Proportionen entstehen aus Beziehungen. Wer Größen und  …</div></div><div style="display:flex;align-items:baseline;gap:2.5vw;margin:0 0 1.6vh;"><div style="width:9vw;flex:none;font-family:RobotoCode;font-size:2vh;color:#6a6a6a;text-align:right;">21</div><div style="width:10vw;flex:none;font-family:IBM;font-size:1.8vh;color:#6a6a6a;">Zwischentitel</div><div style="font-family:IBM;font-weight:500;font-size:3.36vh;line-height:1.1;white-space:nowrap;color:#231f20;">Verhältnis statt Einzelmaß</div></div><div style="display:flex;align-items:baseline;gap:2.5vw;margin:0 0 1.6vh;"><div style="width:9vw;flex:none;font-family:RobotoCode;font-size:2vh;color:#6a6a6a;text-align:right;">34</div><div style="width:10vw;flex:none;font-family:IBM;font-size:1.8vh;color:#6a6a6a;">Titel</div><div style="font-family:IBM;font-weight:600;font-size:5.44vh;line-height:1.1;white-space:nowrap;color:#231f20;">Zahlenreihen</div></div><div style="display:flex;align-items:baseline;gap:2.5vw;margin:0 0 1.6vh;"><div style="width:9vw;flex:none;font-family:RobotoCode;font-size:2vh;color:#6a6a6a;text-align:right;">55</div><div style="width:10vw;flex:none;font-family:IBM;font-size:1.8vh;color:#6a6a6a;">Display</div><div style="font-family:IBM;font-weight:600;font-size:8.80vh;line-height:1.1;white-space:nowrap;color:#231f20;">Proportion</div></div></div>
    <p style="font-size:1.8vh;color:#6a6a6a;margin-top:2vh;">Jede Stufe etwa 1,618-mal größer als die vorige</p>
  </div>
</section>
<section class="simple" data-transition="fade">
  <div>
    <h1>Fibonacci im Seitenaufbau</h1>
    <div style="position:relative;width:62vw;height:63.0vh;text-align:left;"><div style="position:absolute;left:0;top:7.2vh;width:7vw;font-family:RobotoCode;font-size:1.8vh;color:#6a6a6a;text-align:right;transform:translateY(-50%);">13</div><div style="position:absolute;left:8vw;right:0;top:7.2vh;border-top:2px solid #9313ce;"></div><div style="position:absolute;left:10vw;top:8.0vh;font-family:IBM;font-weight:600;font-size:1.6vh;line-height:1.15;color:#231f20;max-width:48vw;">Kolumnentitel</div><div style="position:absolute;left:0;top:11.6vh;width:7vw;font-family:RobotoCode;font-size:1.8vh;color:#6a6a6a;text-align:right;transform:translateY(-50%);">21</div><div style="position:absolute;left:8vw;right:0;top:11.6vh;border-top:2px solid #9313ce;"></div><div style="position:absolute;left:10vw;top:12.4vh;font-family:IBM;font-weight:600;font-size:3.4vh;line-height:1.15;color:#231f20;max-width:48vw;">Headline in derselben Reihe</div><div style="position:absolute;left:0;top:18.7vh;width:7vw;font-family:RobotoCode;font-size:1.8vh;color:#6a6a6a;text-align:right;transform:translateY(-50%);">34</div><div style="position:absolute;left:8vw;right:0;top:18.7vh;border-top:2px solid #9313ce;"></div><div style="position:absolute;left:10vw;top:19.5vh;font-family:IBM;font-weight:400;font-size:2.1vh;line-height:1.15;color:#231f20;max-width:48vw;">Gute Proportionen entstehen aus Beziehungen. Wer Größen und Abstände aus einer Reihe wählt, bekommt Verhältnisse, die zusammenpassen.</div><div style="position:absolute;left:0;top:30.3vh;width:7vw;font-family:RobotoCode;font-size:1.8vh;color:#6a6a6a;text-align:right;transform:translateY(-50%);">55</div><div style="position:absolute;left:8vw;right:0;top:30.3vh;border-top:2px solid #9313ce;"></div><div style="position:absolute;left:10vw;top:31.1vh;font-family:IBM;font-weight:400;font-size:2.1vh;line-height:1.15;color:#231f20;max-width:48vw;">Gute Proportionen entstehen aus Beziehungen. Wer Größen und Abstände aus einer Reihe wählt, bekommt Verhältnisse, die zusammenpassen.</div><div style="position:absolute;left:0;top:49.0vh;width:7vw;font-family:RobotoCode;font-size:1.8vh;color:#6a6a6a;text-align:right;transform:translateY(-50%);">89</div><div style="position:absolute;left:8vw;right:0;top:49.0vh;border-top:2px solid #9313ce;"></div><div style="position:absolute;left:10vw;top:49.8vh;font-family:IBM;font-weight:400;font-size:2vh;line-height:1.15;color:#231f20;max-width:48vw;"></div></div>
    <p style="font-size:1.8vh;color:#6a6a6a;margin-top:1vh;">Abstand von oben, in Einheiten: 13, 21, 34, 55, 89</p>
  </div>
</section>

{% interlude "Renard-Reihen", "Zehn bis hundert in gleichen Schritten" %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Renard R5: 10, 16, 25, 40, 63, 100, jede Stufe etwa 1,585-mal größer"}' %}
<rect data-id="b0" x="150" y="85.0" width="72.0" height="40" fill="#888888" />
<rect data-id="b1" x="150" y="143.0" width="115.2" height="40" fill="#9313ce" />
<rect data-id="b2" x="150" y="201.0" width="180.0" height="40" fill="#888888" />
<rect data-id="b3" x="150" y="259.0" width="288.0" height="40" fill="#888888" />
<rect data-id="b4" x="150" y="317.0" width="453.6" height="40" fill="#888888" />
<rect data-id="b5" x="150" y="375.0" width="720.0" height="40" fill="#888888" />
{% endframe %}
<section class="simple" data-transition="fade">
  <div>
    <h1>Renard R5 als Schriftgrade</h1>
    <div style="width:100%;text-align:left;"><div style="display:flex;align-items:baseline;gap:2.5vw;margin:0 0 1.6vh;"><div style="width:9vw;flex:none;font-family:RobotoCode;font-size:2vh;color:#6a6a6a;text-align:right;">10</div><div style="width:10vw;flex:none;font-family:IBM;font-size:1.8vh;color:#6a6a6a;">Klein</div><div style="font-family:IBM;font-weight:400;font-size:1.60vh;line-height:1.1;white-space:nowrap;color:#231f20;">Bildunterschrift und Quellenangabe</div></div><div style="display:flex;align-items:baseline;gap:2.5vw;margin:0 0 1.6vh;"><div style="width:9vw;flex:none;font-family:RobotoCode;font-size:2vh;color:#6a6a6a;text-align:right;">16</div><div style="width:10vw;flex:none;font-family:IBM;font-size:1.8vh;color:#6a6a6a;">Text</div><div style="font-family:IBM;font-weight:400;font-size:2.56vh;line-height:1.1;white-space:nowrap;color:#231f20;">Gute Proportionen entstehen aus Beziehungen. Wer Größen und  …</div></div><div style="display:flex;align-items:baseline;gap:2.5vw;margin:0 0 1.6vh;"><div style="width:9vw;flex:none;font-family:RobotoCode;font-size:2vh;color:#6a6a6a;text-align:right;">25</div><div style="width:10vw;flex:none;font-family:IBM;font-size:1.8vh;color:#6a6a6a;">Zwischentitel</div><div style="font-family:IBM;font-weight:500;font-size:4.00vh;line-height:1.1;white-space:nowrap;color:#231f20;">Verhältnis statt Einzelmaß</div></div><div style="display:flex;align-items:baseline;gap:2.5vw;margin:0 0 1.6vh;"><div style="width:9vw;flex:none;font-family:RobotoCode;font-size:2vh;color:#6a6a6a;text-align:right;">40</div><div style="width:10vw;flex:none;font-family:IBM;font-size:1.8vh;color:#6a6a6a;">Titel</div><div style="font-family:IBM;font-weight:600;font-size:6.40vh;line-height:1.1;white-space:nowrap;color:#231f20;">Zahlenreihen</div></div><div style="display:flex;align-items:baseline;gap:2.5vw;margin:0 0 1.6vh;"><div style="width:9vw;flex:none;font-family:RobotoCode;font-size:2vh;color:#6a6a6a;text-align:right;">63</div><div style="width:10vw;flex:none;font-family:IBM;font-size:1.8vh;color:#6a6a6a;">Display</div><div style="font-family:IBM;font-weight:600;font-size:10.08vh;line-height:1.1;white-space:nowrap;color:#231f20;">Proportion</div></div></div>
    <p style="font-size:1.8vh;color:#6a6a6a;margin-top:2vh;">Mit 16 px als Grundschrift: 10, 16, 25, 40, 63</p>
  </div>
</section>
<section class="simple" data-transition="fade">
  <div>
    <h1>Renard im Seitenaufbau</h1>
    <div style="position:relative;width:62vw;height:69.0vh;text-align:left;"><div style="position:absolute;left:0;top:5.5vh;width:7vw;font-family:RobotoCode;font-size:1.8vh;color:#6a6a6a;text-align:right;transform:translateY(-50%);">10</div><div style="position:absolute;left:8vw;right:0;top:5.5vh;border-top:2px solid #9313ce;"></div><div style="position:absolute;left:10vw;top:6.3vh;font-family:IBM;font-weight:600;font-size:1.6vh;line-height:1.15;color:#231f20;max-width:48vw;">Kolumnentitel</div><div style="position:absolute;left:0;top:8.8vh;width:7vw;font-family:RobotoCode;font-size:1.8vh;color:#6a6a6a;text-align:right;transform:translateY(-50%);">16</div><div style="position:absolute;left:8vw;right:0;top:8.8vh;border-top:2px solid #9313ce;"></div><div style="position:absolute;left:10vw;top:9.6vh;font-family:IBM;font-weight:600;font-size:3.4vh;line-height:1.15;color:#231f20;max-width:48vw;">Headline in derselben Reihe</div><div style="position:absolute;left:0;top:13.8vh;width:7vw;font-family:RobotoCode;font-size:1.8vh;color:#6a6a6a;text-align:right;transform:translateY(-50%);">25</div><div style="position:absolute;left:8vw;right:0;top:13.8vh;border-top:2px solid #9313ce;"></div><div style="position:absolute;left:10vw;top:14.6vh;font-family:IBM;font-weight:400;font-size:2.1vh;line-height:1.15;color:#231f20;max-width:48vw;">Gute Proportionen entstehen aus Beziehungen. Wer Größen und Abstände aus einer Reihe wählt, bekommt Verhältnisse, die zusammenpassen.</div><div style="position:absolute;left:0;top:22.0vh;width:7vw;font-family:RobotoCode;font-size:1.8vh;color:#6a6a6a;text-align:right;transform:translateY(-50%);">40</div><div style="position:absolute;left:8vw;right:0;top:22.0vh;border-top:2px solid #9313ce;"></div><div style="position:absolute;left:10vw;top:22.8vh;font-family:IBM;font-weight:400;font-size:2.1vh;line-height:1.15;color:#231f20;max-width:48vw;">Gute Proportionen entstehen aus Beziehungen. Wer Größen und Abstände aus einer Reihe wählt, bekommt Verhältnisse, die zusammenpassen.</div><div style="position:absolute;left:0;top:34.7vh;width:7vw;font-family:RobotoCode;font-size:1.8vh;color:#6a6a6a;text-align:right;transform:translateY(-50%);">63</div><div style="position:absolute;left:8vw;right:0;top:34.7vh;border-top:2px solid #9313ce;"></div><div style="position:absolute;left:10vw;top:35.5vh;font-family:IBM;font-weight:400;font-size:2.1vh;line-height:1.15;color:#231f20;max-width:48vw;">Gute Proportionen entstehen aus Beziehungen. Wer Größen und Abstände aus einer Reihe wählt, bekommt Verhältnisse, die zusammenpassen.</div><div style="position:absolute;left:0;top:55.0vh;width:7vw;font-family:RobotoCode;font-size:1.8vh;color:#6a6a6a;text-align:right;transform:translateY(-50%);">100</div><div style="position:absolute;left:8vw;right:0;top:55.0vh;border-top:2px solid #9313ce;"></div><div style="position:absolute;left:10vw;top:55.8vh;font-family:IBM;font-weight:400;font-size:2vh;line-height:1.15;color:#231f20;max-width:48vw;"></div></div>
    <p style="font-size:1.8vh;color:#6a6a6a;margin-top:1vh;">Abstand von oben, in Einheiten: 10, 16, 25, 40, 63, 100</p>
  </div>
</section>

<section class="simple" data-transition="fade">
<div>

# Reihen im Vergleich

| Reihe | Faktor | Beispiel | Nah an |
|---|---|---|---|
| **Fibonacci** | ≈ 1,618 | 13, 21, 34, 55 | Goldener Schnitt |
| **Renard R5** | ≈ 1,585 | 10, 16, 25, 40, 63 | Goldener Schnitt |
| **DIN A** | ≈ 1,414 | 210 × 297 mm | Quadratwurzel aus 2 |
| **Typografische Skala** | 1,25 | 16, 20, 25, 31, 39 | Renard R10 (≈ 1,259) |
| **Klassische Schriftgrade** | kein fester | 8, 9, 10, 12, 14, 18, 24, 36 | über Jahrhunderte gewachsen |

</div>
</section>

{% question "Welche Reihe steckt in Ihrer Typografischen Skala?", "Und aus welcher Reihe stammen Ihre Abstände?" %}

{% statement "Die Skala erledigt die Proportion.", "Typografische Skala und Spacing-System sind Proportion zum Mitnehmen: Wer aus einer Reihe wählt, muss nicht jedes Verhältnis neu erfinden." %}
