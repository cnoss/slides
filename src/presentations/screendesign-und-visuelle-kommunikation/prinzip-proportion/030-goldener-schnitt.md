---
title: "Der Goldene Schnitt"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  Der Goldene Schnitt teilt eine Strecke so, dass sich der kleine Teil zum großen verhält wie der große zum Ganzen. Das ergibt etwa 1 : 1,618. Das goldene Rechteck hat dieses Seitenverhältnis. Trennt man ein Quadrat ab, bleibt wieder ein goldenes Rechteck übrig, und das immer weiter.

  Als Konstruktionshilfe ist er brauchbar: für die Teilung eines Formats, für das Verhältnis von Inhalt und Seitenleiste, für eine Schriftgrößen-Skala. Als Beweis für Schönheit taugt er nicht.

  **Der Mythos-Anteil:** Behauptet wird der Goldene Schnitt im Parthenon, in der Mona Lisa, im Apple-Logo, im Nautilus-Gehäuse. Für die meisten Fälle gibt es keinen Beleg. Die Spiralen werden nachträglich darübergelegt, und weil man Anfangs- und Endpunkte frei wählt, passt fast immer irgendetwas. Der Nautilus wächst nachweislich in einem anderen Verhältnis.

  **Hintergrund**

  Euklid beschreibt die Teilung um 300 v. Chr. als »Teilung im äußeren und mittleren Verhältnis«. Der Name »Goldener Schnitt« taucht erst im 19. Jahrhundert auf (Martin Ohm, 1835) und wurde durch Adolf Zeising (1854) populär, der ihn zum Naturgesetz der Schönheit erklärte. Zum Weiterlesen: Mario Livio, »The Golden Ratio« (2002). Angaben aus dem Gedächtnis, bitte prüfen.
---

{% interlude "Der Goldene Schnitt", "1 : 1,618, und ein bisschen Mythos" %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "animate":false, "bu":"Der kleine Teil verhält sich zum großen wie der große zum Ganzen"}' %}
<line x1="120" y1="250" x2="527.9" y2="250" stroke="#9313ce" stroke-width="10" stroke-linecap="round" />
<line x1="541.9" y1="250" x2="780" y2="250" stroke="#231f20" stroke-width="10" stroke-linecap="round" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "animate":false, "bu":"Quadrat ab, übrig bleibt wieder ein goldenes Rechteck"}' %}
<rect x="190.0" y="60" width="614.9" height="380" fill="none" stroke="#231f20" stroke-width="3" />
<rect x="190.0" y="60.0" width="380.0" height="380.0" fill="#9313ce" fill-opacity="0.25" />
<line x1="570.0" y1="60.0" x2="570.0" y2="440.0" stroke="#231f20" stroke-width="2" stroke-linecap="round" />
<line x1="570.0" y1="294.9" x2="804.9" y2="294.9" stroke="#231f20" stroke-width="2" stroke-linecap="round" />
<line x1="659.7" y1="294.9" x2="659.7" y2="440.0" stroke="#231f20" stroke-width="2" stroke-linecap="round" />
<line x1="570.0" y1="350.3" x2="659.7" y2="350.3" stroke="#231f20" stroke-width="2" stroke-linecap="round" />
<line x1="625.4" y1="294.9" x2="625.4" y2="350.3" stroke="#231f20" stroke-width="2" stroke-linecap="round" />
<line x1="625.4" y1="329.1" x2="659.7" y2="329.1" stroke="#231f20" stroke-width="2" stroke-linecap="round" />
<line x1="638.5" y1="329.1" x2="638.5" y2="350.3" stroke="#231f20" stroke-width="2" stroke-linecap="round" />
{% endframe %}

{% statement "Eine Hilfe, kein Beweis.", "Der Goldene Schnitt kann beim Teilen helfen. Dass etwas schön ist, weil es golden ist, lässt sich nicht belegen." %}
