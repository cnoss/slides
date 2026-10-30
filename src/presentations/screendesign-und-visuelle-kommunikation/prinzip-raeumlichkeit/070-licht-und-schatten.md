---
title: "Licht und Schatten"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Auf dem Screen kommt ein Mittel dazu, das in der Natur selbstverständlich ist: Was über einer Fläche schwebt, wirft einen Schatten. Ein kleiner, scharfer Schatten heißt »liegt knapp darüber«, ein großer, weicher Schatten heißt »schwebt weit darüber«. Der Schatten fällt nach unten, weil wir Licht von oben erwarten.

  In allen anderen Grafiken dieses Moduls gibt es keine Schatten. Hier ist es die Ausnahme, weil das Prinzip selbst davon handelt.

  **Hintergrund**

  Wathan & Schoger, Refactoring UI, Kapitel »Creating Depth«: Licht kommt von oben, Schatten zeigen die Höhe eines Elements, wenige feste Stufen statt beliebiger Werte. Material Design nennt das Elevation und arbeitet mit einer festen Skala von Höhenstufen. Dass wir Licht von oben annehmen, zeigen Studien zur Wahrnehmung von Form aus Schattierung (Ramachandran, 1988, aus dem Gedächtnis, bitte prüfen).
---

{% statement "Schatten zeigen Höhe.", "Ein kleiner Schatten: liegt knapp darüber. Ein großer: schwebt weit darüber." %}

{% frame '{"stage":"#ffffff","w":900,"h":500,"bu":"Drei Flächen auf einer Ebene"}' %}
  <defs><filter id="ev1" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#231f20" flood-opacity="0.22"/></filter><filter id="ev2" x="-40%" y="-40%" width="180%" height="200%"><feDropShadow dx="0" dy="16" stdDeviation="18" flood-color="#231f20" flood-opacity="0.28"/></filter></defs>
  <rect data-id="c0" x="90" y="160" width="200" height="200" fill="#0f6b75" />
  <rect data-id="c1" x="350" y="160" width="200" height="200" fill="#0f6b75" />
  <rect data-id="c2" x="610" y="160" width="200" height="200" fill="#0f6b75" />
{% endframe %}
{% frame '{"stage":"#ffffff","w":900,"h":500,"bu":"Ein kleiner Schatten: Die mittlere hebt sich ab"}' %}
  <defs><filter id="ev1" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#231f20" flood-opacity="0.22"/></filter><filter id="ev2" x="-40%" y="-40%" width="180%" height="200%"><feDropShadow dx="0" dy="16" stdDeviation="18" flood-color="#231f20" flood-opacity="0.28"/></filter></defs>
  <rect data-id="c0" x="90" y="160" width="200" height="200" fill="#0f6b75" />
  <rect data-id="c1" x="350" y="160" width="200" height="200" fill="#0f6b75" filter="url(#ev1)" />
  <rect data-id="c2" x="610" y="160" width="200" height="200" fill="#0f6b75" />
{% endframe %}
{% frame '{"stage":"#ffffff","w":900,"h":500,"bu":"Ein großer Schatten: Die rechte schwebt darüber"}' %}
  <defs><filter id="ev1" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#231f20" flood-opacity="0.22"/></filter><filter id="ev2" x="-40%" y="-40%" width="180%" height="200%"><feDropShadow dx="0" dy="16" stdDeviation="18" flood-color="#231f20" flood-opacity="0.28"/></filter></defs>
  <rect data-id="c0" x="90" y="160" width="200" height="200" fill="#0f6b75" />
  <rect data-id="c1" x="350" y="160" width="200" height="200" fill="#0f6b75" filter="url(#ev1)" />
  <rect data-id="c2" x="610" y="140" width="200" height="200" fill="#0f6b75" filter="url(#ev2)" />
{% endframe %}
