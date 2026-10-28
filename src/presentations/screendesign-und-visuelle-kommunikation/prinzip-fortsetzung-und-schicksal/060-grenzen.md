---
title: "Grenzen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Gute Fortsetzung ist empfindlich. Eine Kante, die nur fast stimmt, wirkt nicht wie eine Linie, sondern wie ein Versehen. Wenige Pixel genügen. Entweder bündig oder deutlich versetzt, alles dazwischen ist uneindeutig (siehe Prinzip Eindeutigkeit).

  Bewegung ist das stärkste Gruppierungsmittel und darum auch das lauteste. Wenn sich alles bewegt, gruppiert nichts mehr, und der Blick wird ständig abgelenkt. Bewegung braucht einen Zweck: Feedback, Zustandswechsel, Orientierung.

  Und Bewegung erreicht nicht alle. Manche Menschen reagieren auf Bewegung mit Schwindel oder Übelkeit und schalten sie im Betriebssystem ab (»Bewegung reduzieren«, in CSS abfragbar mit prefers-reduced-motion). Dann muss die Gruppe auch ohne Bewegung erkennbar sein, zum Beispiel über ein Häkchen.

  **Hintergrund**

  WCAG 2.2: Inhalte, die sich automatisch länger als fünf Sekunden bewegen, müssen sich anhalten lassen (2.2.2 Pause, Stop, Hide, Stufe A). Animationen, die durch Interaktion ausgelöst werden, sollen sich abschalten lassen (2.3.3 Animation from Interactions, Stufe AAA).
---

{% frame '{"stage":"#ffffff", "w":600, "h":600, "bu":"Bündig: eine gemeinsame Kante"}' %}
  <rect data-id="g0" x="120" y="120" width="260" height="22" fill="#888888" />
  <rect data-id="g1" x="120" y="170" width="360" height="160" fill="#d9d9d9" />
  <rect data-id="g2" x="120" y="350" width="340" height="12" fill="#d9d9d9" />
  <rect data-id="g3" x="120" y="374" width="300" height="12" fill="#d9d9d9" />
  <rect data-id="g4" x="120" y="398" width="320" height="12" fill="#d9d9d9" />
  <rect data-id="g5" x="120" y="440" width="140" height="44" rx="22" fill="#9313ce" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":600, "h":600, "bu":"Fast bündig: Fehler oder Absicht?"}' %}
  <rect data-id="g0" x="127" y="120" width="260" height="22" fill="#888888" />
  <rect data-id="g1" x="115" y="170" width="360" height="160" fill="#d9d9d9" />
  <rect data-id="g2" x="123" y="350" width="340" height="12" fill="#d9d9d9" />
  <rect data-id="g3" x="120" y="374" width="300" height="12" fill="#d9d9d9" />
  <rect data-id="g4" x="116" y="398" width="320" height="12" fill="#d9d9d9" />
  <rect data-id="g5" x="129" y="440" width="140" height="44" rx="22" fill="#9313ce" />
{% endframe %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Wann trägt das nicht?</h1>
    {% fragment '<p class="list">Wenn die Kante nur fast stimmt: Es wirkt wie ein Versehen.</p>' %}
    {% fragment '<p class="list">Wenn sich alles bewegt: Dann gruppiert nichts mehr.</p>' %}
    {% fragment '<p class="list">Wenn Bewegung die einzige Information ist: Mit »Bewegung reduzieren« fällt sie weg.</p>' %}
  </div>
</section>
