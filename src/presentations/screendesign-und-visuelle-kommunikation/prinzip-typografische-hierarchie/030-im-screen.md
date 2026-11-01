---
title: "Im Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Die Lesestufen auf einer echten Seite: Dachzeile »Fehlender Wohnraum«, Headline, Lead, darunter die Autorenzeile. Die Dachzeile ist klein, die Headline trägt Größe und Farbe, und der Lead steht direkt darunter. Wer nur die Überschrift liest, hat die Nachricht verstanden.

  **Für alle:** Die optische Hierarchie muss auch im Code stehen. Überschriften gehören in `h1` bis `h6`, in der richtigen Reihenfolge. Screenreader-Nutzende springen über diese Struktur durch die Seite wie andere mit den Augen. Eine Überschrift, die nur groß und fett aussieht, gibt es für sie nicht.

  Screenshot: tagesschau.de, 2026.
---

{% screenshot "./images/lesestufen-tagesschau.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Dachzeile, Headline, Lead, Autorenzeile<br><small>tagesschau.de, Screenshot 2026</small>"}' %}

{% statement "Sie muss auch im Code stehen.", "Überschriften gehören in h1 bis h6. Screenreader springen über diese Struktur durch die Seite wie andere mit den Augen." %}

{% question "Wie viele Lesestufen hat Ihre meistgenutzte App?", "Welche Mittel nutzt sie dafür: Größe, Schnitt, Farbe oder Abstand?" %}
