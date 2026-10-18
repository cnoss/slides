---
title: Mini-Übung
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Mini-Übung (ca. 10 Minuten)**

  Vier Markenfarben, jeweils mit weißer Schrift, wie man sie auf Buttons findet. Zu zweit mit dem WebAIM Contrast Checker auf dem Handy (QR-Code) messen und für jede Farbe entscheiden: Reicht das für Fließtext? Für einen Button mit großer, fetter Schrift?

  Auflösung (berechnet): A 2,52 : 1, fällt auch für große Schrift durch. B 4,59 : 1, besteht knapp. C 2,59 : 1, fällt durch, mit schwarzer Schrift wären es 8,12 : 1, so macht es Spotify auch. D 3,52 : 1, nur für große Schrift.

  Die Hex-Werte sind an die Markenfarben angelehnt und können von den aktuellen Originalen abweichen. Es geht um das Messen, nicht um die Marken.

  Diskussion danach: Was macht eine Marke, deren Farbe für weiße Schrift zu hell ist? Erst Vorschläge sammeln, dann die beiden Beispiele zeigen.

  **Zitro** (erfunden, Gelb #ffd60a): Weiß auf Gelb hat 1,41 : 1, Gelb als Linkfarbe auf Weiß ebenso. Lösung: Gelb bleibt Fläche und Logo, Buttons bekommen dunkle Schrift (11,55 : 1), Links eine dunklere, bräunliche Variante #7a5c00 (6,25 : 1).

  **Minzig** (erfunden, Mint #2ed3b7): Weiß auf Mint hat 1,89 : 1. Lösung: Mint bleibt Fläche, Buttons und Links bekommen die dunklere Variante #0f7c6c (5,1 : 1 mit Weiß).

  Echte Vorbilder: Spotify setzt schwarze Schrift auf das Grün, viele gelbe Marken (z. B. Post, IKEA in Teilen) arbeiten mit dunkler Schrift auf Gelb. In Design-Systemen heißen die Varianten oft brand und brand-strong oder brand-text.
---

{% interlude "Und jetzt Sie.", "Vier Farben, zu zweit, zehn Minuten" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Reicht das?</h1>
    <div style="display:flex; gap:1vw; width:100%;">
      <div style="flex:1; background:#ff8000; color:#ffffff; padding:2vh 1vw; font-weight:600; font-size:3vh;">A<br><span style="font-size:2vh; font-weight:400;">Weiß auf #ff8000</span></div>
      <div style="flex:1; background:#ec0016; color:#ffffff; padding:2vh 1vw; font-weight:600; font-size:3vh;">B<br><span style="font-size:2vh; font-weight:400;">Weiß auf #ec0016</span></div>
      <div style="flex:1; background:#1db954; color:#ffffff; padding:2vh 1vw; font-weight:600; font-size:3vh;">C<br><span style="font-size:2vh; font-weight:400;">Weiß auf #1db954</span></div>
      <div style="flex:1; background:#ff385c; color:#ffffff; padding:2vh 1vw; font-weight:600; font-size:3vh;">D<br><span style="font-size:2vh; font-weight:400;">Weiß auf #ff385c</span></div>
    </div>
    <p style="margin-top:3vh;">Für Fließtext? Für einen Button mit großer, fetter Schrift?</p>
  </div>
</section>

<section class="simple" data-transition="fade">
  <div>
    <h1>Messen Sie hier</h1>
    <div style="display:flex; justify-content:center; width:100%;">
      <figure style="margin:0; text-align:center;"><img src="./images/qr-webaim.svg" alt="QR-Code zum WebAIM Contrast Checker" style="width:40vh; height:40vh; margin:0 auto; display:block;"><figcaption><p>WebAIM Contrast Checker</p></figcaption></figure>
    </div>
  </div>
</section>

<section class="simple" data-transition="fade">
<div>

# Auflösung

| Farbe | Kontrast mit Weiß | Fließtext | Große Schrift |
|---|---|---|---|
| **A** #ff8000 | 2,52 : 1 | fällt durch | fällt durch |
| **B** #ec0016 | 4,59 : 1 | besteht knapp | besteht |
| **C** #1db954 | 2,59 : 1 | fällt durch | fällt durch |
| **D** #ff385c | 3,52 : 1 | fällt durch | besteht |

</div>
</section>

{% question "Und wenn die Markenfarbe zu hell ist?", "Was würden Sie vorschlagen?" %}

{% screenshot "./images/brand-zitro-problem.jpg", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Zitro: Gelb ist die Marke. Für weiße Schrift und Links ist es zu hell.<br><small>Erfundene Marke</small>"}' %}
{% screenshot "./images/brand-zitro-loesung.jpg", '{"transition":"none", "classes":"no-shadow", "width":"auto", "bu":"Lösung: Gelb als Fläche, dunkle Schrift auf Gelb, eine dunklere Variante für Links<br><small>Erfundene Marke</small>"}' %}

{% screenshot "./images/brand-minzig-problem.jpg", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Minzig: Mint ist die Marke. Auch hier reicht der Kontrast nicht.<br><small>Erfundene Marke</small>"}' %}
{% screenshot "./images/brand-minzig-loesung.jpg", '{"transition":"none", "classes":"no-shadow", "width":"auto", "bu":"Lösung: Mint als Fläche, eine dunklere Variante für Buttons und Links<br><small>Erfundene Marke</small>"}' %}

{% statement "Die Marke bleibt, die Funktion bekommt eine Variante.", "Markenfarbe für Flächen und Logo. Für Schrift und Bedienelemente eine dunklere Variante oder dunkle Schrift. Beides als eigene Tokens festhalten." %}
