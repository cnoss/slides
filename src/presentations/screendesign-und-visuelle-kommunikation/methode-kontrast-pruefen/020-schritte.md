---
title: Schritte
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **1. Graustufentest:** im Entwurf schnell und grob. In Figma ein schwarzes Rechteck mit Ebenenmodus »Color« über den Frame legen. Was verschwindet, hat zu wenig Kontrast.

  **2. Paare erfassen:** alle Kombinationen von Vorder- und Hintergrund. Nicht vergessen: Platzhalter in Eingabefeldern, Links, Bildunterschriften, Text auf Fotos, Icons, Rahmen von Eingabefeldern, Fokus-Rahmen, Zustände wie Hover und Fehler, Dark Mode.

  **3. Messen:** mit einem Werkzeug. WebAIM Contrast Checker (Browser), die Entwicklerwerkzeuge von Chrome und Firefox (Farbwähler zeigt das Verhältnis direkt an), Colour Contrast Analyser von TPGi (kostenlos, mit Pipette für den ganzen Bildschirm), in Figma Plugins wie Stark.

  **4. Bewerten:** Grenzwert passend zum Element. Text 4,5 : 1, große Schrift ab 24 px oder ca. 19 px fett 3 : 1, Bedienelemente und informationstragende Grafik 3 : 1. Deaktivierte Elemente und reine Dekoration sind ausgenommen.

  **5. Korrigieren und festhalten:** Farbe so weit abdunkeln oder aufhellen, bis der Wert passt. Das Ergebnis als Token festhalten, damit es überall gilt.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>In fünf Schritten</h1>
    {% fragment '<p class="list"><strong>1. Graustufentest:</strong> schnell und grob, im Entwurf</p>' %}
    {% fragment '<p class="list"><strong>2. Paare erfassen:</strong> jede Kombination aus Schrift oder Element und Hintergrund</p>' %}
    {% fragment '<p class="list"><strong>3. Messen:</strong> mit einem Werkzeug, nicht nach Augenmaß</p>' %}
    {% fragment '<p class="list"><strong>4. Bewerten:</strong> Grenzwert passend zum Element</p>' %}
    {% fragment '<p class="list"><strong>5. Korrigieren und festhalten:</strong> anpassen, als Token speichern</p>' %}
  </div>
</section>

<section class="simple" data-transition="fade">
<div>

# Die Grenzwerte (WCAG 2.2, AA)

| Element | Mindestens |
|---|---|
| **Text** | 4,5 : 1 |
| **Große Schrift**<br>ab 24 px oder ca. 19 px fett | 3 : 1 |
| **Bedienelemente und Grafik**<br>Rahmen, Icons, Fokus | 3 : 1 |

</div>
</section>
