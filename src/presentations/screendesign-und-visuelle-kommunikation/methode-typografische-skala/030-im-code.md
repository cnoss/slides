---
title: "Im Code"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Skala als Variablen. Dann steht im Code keine Größe mehr, sondern eine Stufe. In Figma entspricht das den Text Styles.

  **Für alle:** Größen in `rem` statt `px` angeben. So greift die im Browser eingestellte Schriftgröße, und Menschen, die größere Schrift brauchen, bekommen sie. WCAG 1.4.4 verlangt, dass sich Text ohne Hilfsmittel auf 200 % vergrößern lässt, ohne dass Inhalte oder Funktionen verloren gehen.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Dieselbe Skala im Code</h1>
    <pre style="font-size:2.8vh;line-height:1.5;text-align:left;width:100%;box-shadow:none;"><code class="language-css">:root {
  --text-base: 1rem;     /* 16 px, Fließtext */
  --text-m:    1.25rem;  /* 20 px, Lead */
  --text-l:    1.5625rem; /* 25 px, Zwischentitel */
  --text-xl:   1.9375rem; /* 31 px, Headline klein */
  --text-2xl:  2.4375rem; /* 39 px, Headline groß */
}</code></pre>
  </div>
</section>

{% statement "rem statt px.", "So greift die im Browser eingestellte Schriftgröße. Wer größere Schrift braucht, bekommt sie." %}
