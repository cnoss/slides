---
title: Grenzen
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Mehr Kontrast ist nicht immer besser. Reines Weiß auf reinem Schwarz (21 : 1) blendet im Dark Mode und lässt feine Schrift überstrahlen. Dark-Mode-Systeme nehmen deshalb ein dunkles Grau als Hintergrund und ein helles Grau als Schrift (z. B. #e8e8e8 auf #121212, 15,3 : 1).

  Die WCAG-Formel hat Schwächen: Sie bewertet helle Schrift auf dunklem Grund zu großzügig und berücksichtigt weder Schriftgröße noch Schriftstärke genau. Für WCAG 3 wird ein neues Modell diskutiert, APCA (Accessible Perceptual Contrast Algorithm, Andrew Somers). Bis dahin gilt rechtlich WCAG 2.

  Und Kontrast ist nicht alles: Schriftgröße, Schriftstärke, Zeilenlänge und Zeilenabstand entscheiden genauso über Lesbarkeit (siehe Prinzip Lesetext).
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Wann reicht Kontrast nicht?</h1>
    {% fragment '<p class="list">Wenn er zu hart ist: Reines Weiß auf Schwarz blendet im Dark Mode.</p>' %}
    {% fragment '<p class="list">Wenn die Formel irrt: Helle Schrift auf Dunkel wird zu gut bewertet.</p>' %}
    {% fragment '<p class="list">Wenn die Schrift nicht mitspielt: Größe, Stärke und Zeilenabstand zählen genauso.</p>' %}
  </div>
</section>
