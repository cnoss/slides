---
title: Das Raster
layout: presentation.11ty.js
slideClasses: images
status: ok
transition: zoom
speaker: |
  **Input (ca. 15 Minuten)**

  Rückbezug auf letzte Woche: Dekomposition. Wir zerlegen den Screen vom Großen zum Kleinen und setzen ihn in der Beschreibung wieder zusammen.

  Die Reihenfolge ist kein Zufall. Wer mit Details anfängt ("oben links ist ein kleines Icon"), verliert die Zuhörer:innen, bevor das Gesamtbild steht. Wer erst Format und Grobstruktur nennt, gibt ein Gerüst, in das sich jedes weitere Detail einsortieren lässt.

  Die visuellen Variablen gehen auf Jacques Bertin zurück (Sémiologie graphique, 1967). Ausführlich: Prinzip Visuelle Variablen.
---

{% interlude "Wie beschreiben wir einen Screen?", "Vom Großen zum Kleinen" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Das Raster</h1>
    {% fragment '<p class="list"><strong>1. Format & Gesamteindruck</strong></p>' %}
    {% fragment '<p class="list"><strong>2. Elemente</strong></p>' %}
    {% fragment '<p class="list"><strong>3. Eigenschaften</strong></p>' %}
    {% fragment '<p class="list"><strong>4. Beziehungen</strong></p>' %}
    {% fragment '<p class="list"><strong>5. Wirkung</strong></p>' %}
  </div>
</section>

{% qa "1. Format & Gesamteindruck", "Welches Format, welcher Viewport? Hell oder dunkel, ruhig oder laut, voll oder leer? Wie viele Spalten, wo liegen die großen Blöcke?" %}

{% qa "2. Elemente", "Welche Elementtypen gibt es? Text (Headline, Fließtext, Label), Bild, Grafik und Icon, Interaktionselement (Button, Link, Eingabefeld), Fläche." %}

{% qa "3. Eigenschaften", "Welche visuellen Eigenschaften hat jedes Element? Position, Größe, Form, Helligkeit, Farbe, Richtung, Textur." %}

<section class="image screenshot" data-transition="fade" data-background-color="#666">
  <figure>
    <svg viewBox="0 0 1400 300" width="1400" height="300" style="max-width:100%; height:auto;">
      <defs>
        <pattern id="bertin-stripes" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="4" height="8" fill="#231f20"/></pattern>
        <pattern id="bertin-dots" width="7" height="7" patternUnits="userSpaceOnUse"><circle cx="3.5" cy="3.5" r="1.8" fill="#231f20"/></pattern>
      </defs>
      <g font-family="sans-serif" font-size="30" fill="#fff" text-anchor="middle">
        <text x="90" y="270">Position</text>
        <text x="290" y="270">Größe</text>
        <text x="490" y="270">Form</text>
        <text x="690" y="270">Helligkeit</text>
        <text x="890" y="270">Farbe</text>
        <text x="1090" y="270">Richtung</text>
        <text x="1290" y="270">Textur</text>
      </g>
      <g fill="#fff">
        <rect x="0" y="40" width="180" height="180"/><rect x="200" y="40" width="180" height="180"/><rect x="400" y="40" width="180" height="180"/><rect x="600" y="40" width="180" height="180"/><rect x="800" y="40" width="180" height="180"/><rect x="1000" y="40" width="180" height="180"/><rect x="1200" y="40" width="180" height="180"/>
      </g>
      <g fill="#231f20">
        <circle cx="40" cy="75" r="14"/><circle cx="95" cy="140" r="14"/><circle cx="145" cy="190" r="14"/>
        <circle cx="235" cy="130" r="8"/><circle cx="280" cy="130" r="16"/><circle cx="342" cy="130" r="28"/>
        <circle cx="440" cy="130" r="20"/><rect x="472" y="110" width="40" height="40"/><polygon points="550,110 572,150 528,150"/>
        <circle cx="640" cy="130" r="20" fill="#231f20"/><circle cx="690" cy="130" r="20" fill="#888"/><circle cx="740" cy="130" r="20" fill="#d4d4d4"/>
        <circle cx="840" cy="130" r="20" fill="#4952e1"/><circle cx="890" cy="130" r="20" fill="#dd1166"/><circle cx="940" cy="130" r="20" fill="#00ad2f"/>
        <rect x="1028" y="124" width="36" height="12" rx="6"/><rect x="1072" y="124" width="36" height="12" rx="6" transform="rotate(45 1090 130)"/><rect x="1116" y="124" width="36" height="12" rx="6" transform="rotate(90 1134 130)"/>
        <circle cx="1240" cy="130" r="20"/><circle cx="1290" cy="130" r="20" fill="url(#bertin-stripes)" stroke="#231f20" stroke-width="2"/><circle cx="1340" cy="130" r="20" fill="url(#bertin-dots)" stroke="#231f20" stroke-width="2"/>
      </g>
    </svg>
    <figcaption class="bu is-dark"><p>Visuelle Variablen nach Jacques Bertin (1967)</p></figcaption>
  </figure>
</section>

{% qa "4. Beziehungen", "Wie stehen die Elemente zueinander? Abstand und Nähe, Ausrichtung, Ähnlichkeit und Gruppen, Kontrast. Und die Hierarchie: Was sehe ich zuerst, was danach?" %}

{% qa "5. Wirkung", "Was löst das aus, und bei wem? Passt die Wirkung zu Funktion und Zielgruppe?" %}
