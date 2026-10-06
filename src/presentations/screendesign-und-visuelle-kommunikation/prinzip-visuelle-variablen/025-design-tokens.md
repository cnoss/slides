---
title: Design Tokens
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Design Tokens sind benannte Werte für visuelle Variablen: Farbe, Größe, Abstand, Radius, Schrift, Schatten, Dauer. Sie sind die Schnittstelle zwischen Design und Entwicklung: In Figma als Variablen, im Code als CSS Custom Properties oder JSON. Austauschformat: Design Tokens Community Group des W3C.

  Wichtig ist die Ebene: Basis-Tokens benennen Werte, semantische Tokens benennen Zwecke, Komponenten-Tokens benennen Einsatzorte. Gestaltet wird auf der semantischen Ebene.

  Kommt wieder bei: Spacing-System, Typografische Skala, Gestaltungskontext analysieren, Interface-Inventar.
---

{% statement "Design Tokens geben visuellen Variablen einen Namen.", "Statt #9313ce heißt es color-accent. Design und Entwicklung sprechen dieselbe Sprache." %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Drei Ebenen</h1>
    <table style="font-size:1em; width:100%;">
      <tr><td><strong>Basis</strong></td><td>Was gibt es?</td><td><code>purple-500: #9313ce</code></td></tr>
      <tr class="fragment"><td><strong>Semantisch</strong></td><td>Wofür ist es da?</td><td><code>color-accent: purple-500</code></td></tr>
      <tr class="fragment"><td><strong>Komponente</strong></td><td>Wo wird es eingesetzt?</td><td><code>button-primary-bg: color-accent</code></td></tr>
    </table>
  </div>
</section>

{% codeSmall "Im Code", "Dieselben Tokens als CSS Custom Properties", ":root {\n  --purple-500: #9313ce;\n  --color-accent: var(--purple-500);\n  --space-m: 1rem;\n  --radius-pill: 999px;\n}\n\n.button-primary {\n  background: var(--color-accent);\n  padding: var(--space-m);\n  border-radius: var(--radius-pill);\n}", "css" %}

{% statement "Tokens sind die Übergabe vom Design an die Entwicklung.", "Wer in Variablen und Tokens gestaltet, übergibt keine Bilder, sondern Entscheidungen." %}
