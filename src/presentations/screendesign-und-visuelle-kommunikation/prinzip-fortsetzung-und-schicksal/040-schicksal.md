---
title: "Gemeinsames Schicksal"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Ein Feld aus 40 gleichen Punkten in gleichen Abständen. Nach Nähe und Ähnlichkeit gibt es keine Gruppen. Dann bewegen sich acht Punkte im selben Takt auf und ab. Sofort sind sie eine Gruppe, obwohl sie über das ganze Feld verstreut sind und genauso aussehen wie alle anderen. Die letzte Folie hält die Gruppe fest.

  Die Animation ist reines CSS im SVG. Bei aktivierter Einstellung »Bewegung reduzieren« im Betriebssystem bleibt das Bild stehen. Dann direkt zur dritten Folie weiterschalten.

  **Hintergrund**

  Gemeinsames Schicksal ist eines der stärksten Gruppierungsprinzipien, stärker als Nähe und Ähnlichkeit. Gemeint ist nicht nur Bewegung, sondern jede gemeinsame Veränderung: gemeinsam aufleuchten, gemeinsam die Farbe wechseln, gemeinsam verschwinden. Das Auge reagiert besonders empfindlich auf Bewegung, gerade im Augenwinkel (siehe Phänomen Pop-out und Prinzip Bewegung).
---

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Ein Punktfeld", "animate":false}' %}
  <circle cx="135" cy="145" r="14" fill="#231f20" />
  <circle cx="205" cy="145" r="14" fill="#231f20" />
  <circle cx="345" cy="145" r="14" fill="#231f20" />
  <circle cx="415" cy="145" r="14" fill="#231f20" />
  <circle cx="485" cy="145" r="14" fill="#231f20" />
  <circle cx="555" cy="145" r="14" fill="#231f20" />
  <circle cx="625" cy="145" r="14" fill="#231f20" />
  <circle cx="765" cy="145" r="14" fill="#231f20" />
  <circle cx="135" cy="215" r="14" fill="#231f20" />
  <circle cx="205" cy="215" r="14" fill="#231f20" />
  <circle cx="275" cy="215" r="14" fill="#231f20" />
  <circle cx="415" cy="215" r="14" fill="#231f20" />
  <circle cx="485" cy="215" r="14" fill="#231f20" />
  <circle cx="625" cy="215" r="14" fill="#231f20" />
  <circle cx="695" cy="215" r="14" fill="#231f20" />
  <circle cx="765" cy="215" r="14" fill="#231f20" />
  <circle cx="135" cy="285" r="14" fill="#231f20" />
  <circle cx="275" cy="285" r="14" fill="#231f20" />
  <circle cx="345" cy="285" r="14" fill="#231f20" />
  <circle cx="415" cy="285" r="14" fill="#231f20" />
  <circle cx="485" cy="285" r="14" fill="#231f20" />
  <circle cx="555" cy="285" r="14" fill="#231f20" />
  <circle cx="695" cy="285" r="14" fill="#231f20" />
  <circle cx="765" cy="285" r="14" fill="#231f20" />
  <circle cx="135" cy="355" r="14" fill="#231f20" />
  <circle cx="205" cy="355" r="14" fill="#231f20" />
  <circle cx="275" cy="355" r="14" fill="#231f20" />
  <circle cx="345" cy="355" r="14" fill="#231f20" />
  <circle cx="485" cy="355" r="14" fill="#231f20" />
  <circle cx="555" cy="355" r="14" fill="#231f20" />
  <circle cx="625" cy="355" r="14" fill="#231f20" />
  <circle cx="695" cy="355" r="14" fill="#231f20" />
  <circle cx="275" cy="145" r="14" fill="#231f20" />
  <circle cx="695" cy="145" r="14" fill="#231f20" />
  <circle cx="345" cy="215" r="14" fill="#231f20" />
  <circle cx="555" cy="215" r="14" fill="#231f20" />
  <circle cx="205" cy="285" r="14" fill="#231f20" />
  <circle cx="625" cy="285" r="14" fill="#231f20" />
  <circle cx="415" cy="355" r="14" fill="#231f20" />
  <circle cx="765" cy="355" r="14" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Und jetzt?", "animate":false}' %}
<style>@keyframes gs-hub{from{transform:translateY(0)}to{transform:translateY(-26px)}}.gs-hub{animation:gs-hub .9s ease-in-out infinite alternate}@media (prefers-reduced-motion: reduce){.gs-hub{animation:none}}</style>
  <circle cx="135" cy="145" r="14" fill="#231f20" />
  <circle cx="205" cy="145" r="14" fill="#231f20" />
  <circle cx="345" cy="145" r="14" fill="#231f20" />
  <circle cx="415" cy="145" r="14" fill="#231f20" />
  <circle cx="485" cy="145" r="14" fill="#231f20" />
  <circle cx="555" cy="145" r="14" fill="#231f20" />
  <circle cx="625" cy="145" r="14" fill="#231f20" />
  <circle cx="765" cy="145" r="14" fill="#231f20" />
  <circle cx="135" cy="215" r="14" fill="#231f20" />
  <circle cx="205" cy="215" r="14" fill="#231f20" />
  <circle cx="275" cy="215" r="14" fill="#231f20" />
  <circle cx="415" cy="215" r="14" fill="#231f20" />
  <circle cx="485" cy="215" r="14" fill="#231f20" />
  <circle cx="625" cy="215" r="14" fill="#231f20" />
  <circle cx="695" cy="215" r="14" fill="#231f20" />
  <circle cx="765" cy="215" r="14" fill="#231f20" />
  <circle cx="135" cy="285" r="14" fill="#231f20" />
  <circle cx="275" cy="285" r="14" fill="#231f20" />
  <circle cx="345" cy="285" r="14" fill="#231f20" />
  <circle cx="415" cy="285" r="14" fill="#231f20" />
  <circle cx="485" cy="285" r="14" fill="#231f20" />
  <circle cx="555" cy="285" r="14" fill="#231f20" />
  <circle cx="695" cy="285" r="14" fill="#231f20" />
  <circle cx="765" cy="285" r="14" fill="#231f20" />
  <circle cx="135" cy="355" r="14" fill="#231f20" />
  <circle cx="205" cy="355" r="14" fill="#231f20" />
  <circle cx="275" cy="355" r="14" fill="#231f20" />
  <circle cx="345" cy="355" r="14" fill="#231f20" />
  <circle cx="485" cy="355" r="14" fill="#231f20" />
  <circle cx="555" cy="355" r="14" fill="#231f20" />
  <circle cx="625" cy="355" r="14" fill="#231f20" />
  <circle cx="695" cy="355" r="14" fill="#231f20" />
  <g class="gs-hub"><circle cx="275" cy="145" r="14" fill="#231f20" /><circle cx="695" cy="145" r="14" fill="#231f20" /><circle cx="345" cy="215" r="14" fill="#231f20" /><circle cx="555" cy="215" r="14" fill="#231f20" /><circle cx="205" cy="285" r="14" fill="#231f20" /><circle cx="625" cy="285" r="14" fill="#231f20" /><circle cx="415" cy="355" r="14" fill="#231f20" /><circle cx="765" cy="355" r="14" fill="#231f20" /></g>
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Was sich gemeinsam bewegt, ist eine Gruppe. Quer durch das Feld", "animate":false}' %}
  <circle cx="135" cy="145" r="14" fill="#231f20" />
  <circle cx="205" cy="145" r="14" fill="#231f20" />
  <circle cx="345" cy="145" r="14" fill="#231f20" />
  <circle cx="415" cy="145" r="14" fill="#231f20" />
  <circle cx="485" cy="145" r="14" fill="#231f20" />
  <circle cx="555" cy="145" r="14" fill="#231f20" />
  <circle cx="625" cy="145" r="14" fill="#231f20" />
  <circle cx="765" cy="145" r="14" fill="#231f20" />
  <circle cx="135" cy="215" r="14" fill="#231f20" />
  <circle cx="205" cy="215" r="14" fill="#231f20" />
  <circle cx="275" cy="215" r="14" fill="#231f20" />
  <circle cx="415" cy="215" r="14" fill="#231f20" />
  <circle cx="485" cy="215" r="14" fill="#231f20" />
  <circle cx="625" cy="215" r="14" fill="#231f20" />
  <circle cx="695" cy="215" r="14" fill="#231f20" />
  <circle cx="765" cy="215" r="14" fill="#231f20" />
  <circle cx="135" cy="285" r="14" fill="#231f20" />
  <circle cx="275" cy="285" r="14" fill="#231f20" />
  <circle cx="345" cy="285" r="14" fill="#231f20" />
  <circle cx="415" cy="285" r="14" fill="#231f20" />
  <circle cx="485" cy="285" r="14" fill="#231f20" />
  <circle cx="555" cy="285" r="14" fill="#231f20" />
  <circle cx="695" cy="285" r="14" fill="#231f20" />
  <circle cx="765" cy="285" r="14" fill="#231f20" />
  <circle cx="135" cy="355" r="14" fill="#231f20" />
  <circle cx="205" cy="355" r="14" fill="#231f20" />
  <circle cx="275" cy="355" r="14" fill="#231f20" />
  <circle cx="345" cy="355" r="14" fill="#231f20" />
  <circle cx="485" cy="355" r="14" fill="#231f20" />
  <circle cx="555" cy="355" r="14" fill="#231f20" />
  <circle cx="625" cy="355" r="14" fill="#231f20" />
  <circle cx="695" cy="355" r="14" fill="#231f20" />
  <circle cx="275" cy="145" r="14" fill="#9313ce" />
  <circle cx="695" cy="145" r="14" fill="#9313ce" />
  <circle cx="345" cy="215" r="14" fill="#9313ce" />
  <circle cx="555" cy="215" r="14" fill="#9313ce" />
  <circle cx="205" cy="285" r="14" fill="#9313ce" />
  <circle cx="625" cy="285" r="14" fill="#9313ce" />
  <circle cx="415" cy="355" r="14" fill="#9313ce" />
  <circle cx="765" cy="355" r="14" fill="#9313ce" />
{% endframe %}
