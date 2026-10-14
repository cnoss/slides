---
title: Gestalten Sie für die Ränder
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Wer für den Durchschnitt gestaltet, gestaltet für niemanden. Extreme Nutzungssituationen zeigen, was eine Lösung leisten muss, und die Lösung hilft dann auch allen anderen.

  Beispiel aus dem Inclusive Design Toolkit von Microsoft: Ein Arm. Dauerhaft (Amputation), vorübergehend (Arm in Gips), situativ (ein Kind auf dem Arm). Wer eine App für die Bedienung mit einer Hand gestaltet, gestaltet für alle drei.

  Methodischer Partner: Barrierefreiheit prüfen.

  **Hintergrund**

  Das »Persona Spectrum« stammt aus dem Microsoft Inclusive Design Toolkit (2016). Kat Holmes, die es mitentwickelt hat, beschreibt Behinderung dort als Missverhältnis zwischen Mensch und Umgebung, nicht als Eigenschaft eines Menschen (Kat Holmes: Mismatch, 2018).


  **Mini-Übung (ca. 3 Minuten):** Alle schreiben eine kurze Nachricht mit der schwachen Hand, also Rechtshänder:innen mit links. Eine Minute. Dann sammeln: Was war schwer? Erwartbar: Tasten oben links nicht erreichbar, Tippfehler, Autokorrektur hilft, Sprachnachricht wäre einfacher. Überleitung: Genau so geht es Menschen mit einem Arm, mit Gips oder mit Kind auf dem Arm. Und Gestaltung entscheidet, wo die wichtigen Bedienelemente liegen.
---

{% interlude "Gestalten Sie für die Ränder.", "Extreme Nutzungssituationen zeigen, was eine Lösung leisten muss." %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Ein Arm</h1>
    {% fragment '<p class="list"><strong>dauerhaft:</strong> ein Arm fehlt</p>' %}
    {% fragment '<p class="list"><strong>vorübergehend:</strong> der Arm ist eingegipst</p>' %}
    {% fragment '<p class="list"><strong>situativ:</strong> auf dem Arm sitzt ein Kind</p>' %}
  </div>
</section>

{% question "Schreiben Sie eine Nachricht.", "Mit Ihrer schwachen Hand. Eine Minute." %}

{% question "Was war schwer?", "Und was hat geholfen?" %}

{% statement "Woran merken Sie, dass Sie für die Ränder gestalten?", "Sie fragen nicht nur »Wer nutzt das?«, sondern auch »In welcher Lage?«: mit einer Hand, im Sonnenlicht, ohne Ton, unter Zeitdruck." %}
