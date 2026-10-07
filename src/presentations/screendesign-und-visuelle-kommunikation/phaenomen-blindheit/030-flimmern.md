---
title: Finden Sie den Unterschied
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  **Live-Test (ca. 3 Minuten)**

  Zwei Fassungen desselben Bildes wechseln sich ab, dazwischen blitzt kurz eine leere Fläche auf. Ein Element verschwindet und taucht wieder auf. Wer es gefunden hat, hebt die Hand, verrät aber nichts. Meist dauert es überraschend lange.

  Ohne die leere Fläche dazwischen würde die Veränderung sofort ins Auge springen: Das periphere Sehen reagiert stark auf Bewegung. Die Unterbrechung löscht genau dieses Signal. Die nächste Folie zeigt die Auflösung.

  Das Flimmern ist eine SVG-Animation. Bei aktivierter Einstellung "Bewegung reduzieren" im Betriebssystem bleibt das Bild stehen.
---

{% frame '{"bu":"Was verändert sich? Hand hoch, wenn Sie es gefunden haben."}' %}
<style>
@keyframes cb-wechsel{0%,46.9%{opacity:1}47%,96.9%{opacity:0}97%,100%{opacity:1}}
@keyframes cb-maske{0%,43.9%{opacity:0}44%,49.9%{opacity:1}50%,93.9%{opacity:0}94%,100%{opacity:1}}
.cb-wechsel{animation:cb-wechsel 2.4s linear infinite}
.cb-maske{animation:cb-maske 2.4s linear infinite}
@media (prefers-reduced-motion: reduce){.cb-wechsel,.cb-maske{animation:none}.cb-maske{opacity:0}}
</style>
<rect data-id="e00" x="67" y="61" width="38" height="38" fill="#231f20" />
<circle data-id="e10" cx="186" cy="93" r="18" fill="#d9d9d9" />
<circle data-id="e20" cx="260" cy="82" r="24" fill="#231f20" />
<circle data-id="e30" cx="341" cy="78" r="26" fill="#231f20" />
<rect data-id="e40" class="cb-wechsel" x="401" y="53" width="48" height="48" fill="#888888" />
<polygon data-id="e50" points="516,72 540,120 492,120" fill="#231f20" />
<circle data-id="e01" cx="77" cy="167" r="22" fill="#888888" />
<polygon data-id="e11" points="173,142 195,186 151,186" fill="#231f20" />
<polygon data-id="e21" points="261,167 280,205 242,205" fill="#888888" />
<polygon data-id="e31" points="346,155 369,201 323,201" fill="#888888" />
<polygon data-id="e41" points="415,159 433,195 397,195" fill="#231f20" />
<rect data-id="e51" x="492" y="143" width="46" height="46" fill="#888888" />
<rect data-id="e02" x="68" y="240" width="44" height="44" fill="#d9d9d9" />
<circle data-id="e12" cx="167" cy="269" r="19" fill="#888888" />
<polygon data-id="e22" points="262,230 285,276 239,276" fill="#888888" />
<rect data-id="e32" x="332" y="239" width="38" height="38" fill="#231f20" />
<circle data-id="e42" cx="428" cy="257" r="20" fill="#d9d9d9" />
<circle data-id="e52" cx="511" cy="257" r="26" fill="#231f20" />
<rect data-id="e03" x="71" y="330" width="46" height="46" fill="#d9d9d9" />
<polygon data-id="e13" points="179,324 198,362 160,362" fill="#888888" />
<rect data-id="e23" x="251" y="311" width="38" height="38" fill="#888888" />
<polygon data-id="e33" points="329,326 354,376 304,376" fill="#d9d9d9" />
<rect data-id="e43" x="403" y="332" width="36" height="36" fill="#d9d9d9" />
<circle data-id="e53" cx="510" cy="339" r="25" fill="#231f20" />
<rect data-id="e04" x="56" y="397" width="42" height="42" fill="#888888" />
<rect data-id="e14" x="152" y="404" width="40" height="40" fill="#231f20" />
<polygon data-id="e24" points="258,404 278,444 238,444" fill="#d9d9d9" />
<polygon data-id="e34" points="354,401 378,449 330,449" fill="#d9d9d9" />
<rect data-id="e44" x="403" y="413" width="40" height="40" fill="#888888" />
<circle data-id="e54" cx="498" cy="417" r="21" fill="#888888" />
<polygon data-id="e05" points="76,489 98,533 54,533" fill="#888888" />
<circle data-id="e15" cx="169" cy="496" r="26" fill="#888888" />
<polygon data-id="e25" points="255,495 275,535 235,535" fill="#d9d9d9" />
<polygon data-id="e35" points="350,498 375,548 325,548" fill="#231f20" />
<polygon data-id="e45" points="440,499 464,547 416,547" fill="#888888" />
<circle data-id="e55" cx="508" cy="508" r="24" fill="#888888" />
<rect class="cb-maske" x="0" y="0" width="600" height="600" fill="#ffffff" />
{% endframe %}
{% frame '{"bu":"Hier: Das Quadrat oben rechts kommt und geht."}' %}
<rect data-id="e00" x="67" y="61" width="38" height="38" fill="#d9d9d9" />
<circle data-id="e10" cx="186" cy="93" r="18" fill="#eeeeee" />
<circle data-id="e20" cx="260" cy="82" r="24" fill="#d9d9d9" />
<circle data-id="e30" cx="341" cy="78" r="26" fill="#d9d9d9" />
<rect data-id="e40" x="401" y="53" width="48" height="48" fill="#9313ce" />
<polygon data-id="e50" points="516,72 540,120 492,120" fill="#d9d9d9" />
<circle data-id="e01" cx="77" cy="167" r="22" fill="#d9d9d9" />
<polygon data-id="e11" points="173,142 195,186 151,186" fill="#d9d9d9" />
<polygon data-id="e21" points="261,167 280,205 242,205" fill="#d9d9d9" />
<polygon data-id="e31" points="346,155 369,201 323,201" fill="#d9d9d9" />
<polygon data-id="e41" points="415,159 433,195 397,195" fill="#d9d9d9" />
<rect data-id="e51" x="492" y="143" width="46" height="46" fill="#d9d9d9" />
<rect data-id="e02" x="68" y="240" width="44" height="44" fill="#eeeeee" />
<circle data-id="e12" cx="167" cy="269" r="19" fill="#d9d9d9" />
<polygon data-id="e22" points="262,230 285,276 239,276" fill="#d9d9d9" />
<rect data-id="e32" x="332" y="239" width="38" height="38" fill="#d9d9d9" />
<circle data-id="e42" cx="428" cy="257" r="20" fill="#eeeeee" />
<circle data-id="e52" cx="511" cy="257" r="26" fill="#d9d9d9" />
<rect data-id="e03" x="71" y="330" width="46" height="46" fill="#eeeeee" />
<polygon data-id="e13" points="179,324 198,362 160,362" fill="#d9d9d9" />
<rect data-id="e23" x="251" y="311" width="38" height="38" fill="#d9d9d9" />
<polygon data-id="e33" points="329,326 354,376 304,376" fill="#eeeeee" />
<rect data-id="e43" x="403" y="332" width="36" height="36" fill="#eeeeee" />
<circle data-id="e53" cx="510" cy="339" r="25" fill="#d9d9d9" />
<rect data-id="e04" x="56" y="397" width="42" height="42" fill="#d9d9d9" />
<rect data-id="e14" x="152" y="404" width="40" height="40" fill="#d9d9d9" />
<polygon data-id="e24" points="258,404 278,444 238,444" fill="#eeeeee" />
<polygon data-id="e34" points="354,401 378,449 330,449" fill="#eeeeee" />
<rect data-id="e44" x="403" y="413" width="40" height="40" fill="#d9d9d9" />
<circle data-id="e54" cx="498" cy="417" r="21" fill="#d9d9d9" />
<polygon data-id="e05" points="76,489 98,533 54,533" fill="#d9d9d9" />
<circle data-id="e15" cx="169" cy="496" r="26" fill="#d9d9d9" />
<polygon data-id="e25" points="255,495 275,535 235,535" fill="#eeeeee" />
<polygon data-id="e35" points="350,498 375,548 325,548" fill="#d9d9d9" />
<polygon data-id="e45" points="440,499 464,547 416,547" fill="#d9d9d9" />
<circle data-id="e55" cx="508" cy="508" r="24" fill="#d9d9d9" />
{% endframe %}
