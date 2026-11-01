---
title: "Schriften mischen"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  Wer zwei Schriften mischt, braucht einen Grund. Die Regel: Kontrast oder Verwandtschaft, aber kein Zufall.

  1. **Eine Familie:** Die sicherste Lösung. Bold und Regular derselben Schrift reichen für die meisten Screens.
  2. **Deutlicher Kontrast:** Zwei Familien, die sich klar unterscheiden, etwa eine Serifenschrift für die Überschrift und eine serifenlose für den Text. Der Unterschied muss wie Absicht aussehen.
  3. **Zu ähnlich:** Zwei ähnliche Schriften wirken wie ein Versehen. Das ist der häufigste Fehler und fällt erst auf den zweiten Blick auf: Es stimmt etwas nicht, und man weiß nicht, was.
  4. **Zufall:** Zwei Schriften, die jede für sich laut sind, streiten miteinander.

  Faustregel: höchstens zwei Familien. Hilfe bei der Suche: fontpair.co, Google Fonts (Rubrik »Pairings« auf den Schriftseiten).
---

{% statement "Kontrast oder Verwandtschaft.", "Aber kein Zufall. Und höchstens zwei Familien." %}

{% screenshot "./images/mischen-familie.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Eine Familie: Bold und Regular. Immer sicher"}' %}

{% screenshot "./images/mischen-kontrast.png", '{"transition":"none", "classes":"no-shadow", "width":"auto", "bu":"Zwei Familien mit deutlichem Kontrast: Absicht"}' %}

{% screenshot "./images/mischen-aehnlich.png", '{"transition":"none", "classes":"no-shadow", "width":"auto", "bu":"Zu ähnlich: wirkt wie ein Versehen"}' %}

{% screenshot "./images/mischen-zufall.png", '{"transition":"none", "classes":"no-shadow", "width":"auto", "bu":"Beide laut: Sie streiten miteinander"}' %}
