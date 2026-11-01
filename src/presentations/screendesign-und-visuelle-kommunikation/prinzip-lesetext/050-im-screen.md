---
title: "Im Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Auf einer echten Seite: Die deutsche Wikipedia begrenzt die Textbreite in der Standarddarstellung, gibt aber die Wahl, ob der Text schmal oder breit läuft. Das Menü rechts stellt Textgröße und Breite ein. Eine gute Lösung, weil Lesevorlieben verschieden sind.

  Dann die vier Zeilen CSS, mit denen das meiste erledigt ist. `text-wrap: pretty` ist noch nicht überall verfügbar, schadet aber auch nicht: Browser, die es nicht kennen, ignorieren es.

  **Für alle:** WCAG 1.4.12 (Textabstände) verlangt, dass ein Layout nicht bricht, wenn Nutzende den Zeilenabstand auf das 1,5-Fache, den Absatzabstand auf das 2-Fache, den Buchstabenabstand auf das 0,12-Fache und den Wortabstand auf das 0,16-Fache der Schriftgröße stellen. Also keine festen Höhen für Textcontainer.

  Screenshot: de.wikipedia.org, 2026, ausgeschnitten. Der Spendenaufruf über der Seite ist weggelassen.
---

{% screenshot "./images/lesetext-wikipedia.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Begrenzte Breite, und die Lesenden dürfen sie ändern<br><small>de.wikipedia.org, Screenshot 2026, Ausschnitt</small>"}' %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Vier Zeilen CSS</h1>
    <pre style="font-size:3vh;line-height:1.5;text-align:left;width:100%;box-shadow:none;"><code class="language-css">article p {
  font-size: 1rem;      /* mindestens 16 px */
  line-height: 1.5;     /* ohne Einheit */
  max-width: 65ch;      /* Zeilenlänge */
  text-wrap: pretty;    /* keine einsamen Wörter am Ende */
}</code></pre>
  </div>
</section>

{% question "Wie lang sind die Zeilen auf Ihrer Lieblingsseite?", "Zählen Sie nach: Wie viele Zeichen hat eine Zeile? Und wie viele auf dem Handy?" %}
