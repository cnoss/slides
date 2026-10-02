---
title: Beschreibungs-Pingpong, Runde 1
layout: presentation.11ty.js
slideClasses: images
status: ok
transition: zoom
speaker: |
  **Ablauf (ca. 22 Minuten)**

  - 3 Min. erklären, 7 Min. schreiben, 7 Min. zeichnen, 5 Min. vergleichen und sammeln.
  - Papier und Stift: Jede Person braucht ein Blatt zum Schreiben und eins zum Zeichnen.
  - Bewusst **ohne** Hilfestellung. Die Lücken sind der Lerneffekt.

  **Typische Lücken, die an die Tafel gehören:** Größenverhältnisse, Abstände, Ausrichtung (links, zentriert), Reihenfolge von oben nach unten, Schriftgröße und Schriftstärke, genaue Farben, Format des Screens.

  Screen A ist das Produktdetail der AirPods Pro 3 auf apple.com, Screen B das Wikipedia-Portal, beide mobil.
---

{% interlude "Beschreibungs-Pingpong", "Runde 1" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>So geht's</h1>
    {% fragment '<p class="list">Zu zweit. Links: Screen A, rechts: Screen B. Nicht spicken!</p>' %}
    {% fragment '<p class="list"><strong>7 Min.</strong> Screen schriftlich beschreiben. Nur Text, keine Skizzen.</p>' %}
    {% fragment '<p class="list"><strong>7 Min.</strong> Zettel tauschen, nach der Beschreibung zeichnen</p>' %}
    {% fragment '<p class="list">Zeichnung und Original vergleichen</p>' %}
  </div>
</section>

<section class="simple" data-transition="fade">
  <div>
    <h1>Runde 1</h1>
    <div style="display:flex; gap:6rem; justify-content:center; align-items:flex-start; margin-top:1rem; width:100%;">
      <figure style="margin:0; text-align:center;"><img src="./images/qr-pingpong-r1-a.svg" alt="QR-Code Screen A" style="width:38vh; height:38vh; margin:0;"><figcaption><p><strong>Screen A</strong><br>links sitzend</p></figcaption></figure>
      <figure style="margin:0; text-align:center;"><img src="./images/qr-pingpong-r1-b.svg" alt="QR-Code Screen B" style="width:38vh; height:38vh; margin:0;"><figcaption><p><strong>Screen B</strong><br>rechts sitzend</p></figcaption></figure>
    </div>
  </div>
</section>

{% question "Schreiben", "7 Minuten. Nur Text, keine Skizzen." %}

{% question "Tauschen und zeichnen", "7 Minuten" %}

{% screenshot "./images/pingpong-r1-a.jpg", '{"transition":"fade", "classes": "shadow", "width":"auto", "bu":"Screen A"}' %}

{% screenshot "./images/pingpong-r1-b.jpg", '{"transition":"fade", "classes": "shadow", "width":"auto", "bu":"Screen B"}' %}

{% question "Was hat in den Beschreibungen gefehlt?", "Sammeln Sie zu zweit drei Dinge, die Sie falsch oder gar nicht zeichnen konnten." %}
