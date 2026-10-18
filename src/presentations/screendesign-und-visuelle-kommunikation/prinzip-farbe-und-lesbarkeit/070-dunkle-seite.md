---
title: Die dunkle Seite
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Geringer Kontrast lässt sich gezielt einsetzen, um Informationen zu verstecken, die rechtlich auf der Seite stehen müssen: Laufzeiten, Folgepreise, Kündigungsfristen. Der Preis ist groß und dunkel, die Bedingungen klein und hellgrau. Formal ist alles da, praktisch liest es niemand.

  Das Beispiel ist ein Mockup, die Werte sind erfunden. Das Hellgrau #aaaaaa hat auf Weiß 2,32 : 1 und fällt damit deutlich unter die 4,5 : 1 der WCAG.

  Brignull nennt das »Visual interference«. Rechtlich: Die Preisangabenverordnung verlangt den Gesamtpreis klar erkennbar, Gerichte haben versteckte Folgekosten wiederholt beanstandet.
---

{% interlude "Die dunkle Seite", "Wenig Kontrast versteckt, was niemand lesen soll." %}

<section class="simple" data-transition="fade">
  <div>
    <p style="font-size:3vh; margin:0;">Handytarif Flex</p>
    <p style="font-size:12vh; font-weight:700; margin:0; line-height:1;">9,99 €</p>
    <p style="font-size:3vh; margin:0 0 3vh;">pro Monat</p>
    <p style="font-size:1.6vh; color:#aaaaaa; margin:0;">In den ersten 6 Monaten, danach 29,99 € monatlich. Mindestlaufzeit 24 Monate. Einmaliger Anschlusspreis 39,99 €.</p>
  </div>
</section>

{% question "Wem nützt dieses Hellgrau?", "2,32 : 1. Weit unter dem, was die WCAG für Text verlangen." %}
