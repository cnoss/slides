---
title: "Im Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  **Dialog:** Ein Screen als Wireframe. Grau: Bild und Text, hellgraue Flächen: Karten, Schwarz: ein Button. Lila: die Hauptaktion im Dialog. Dann öffnet sich ein Dialog. Ohne weitere Hinweise liegt er auf derselben Ebene wie die Seite, man muss erst sortieren, was dazugehört. Mit abgedunkeltem Hintergrund ist sofort klar, was vorn ist: Die Seite verliert Kontrast und rückt optisch nach hinten, der Dialog wird zur einzigen Figur. Luftperspektive auf dem Screen. Frage: Was hat sich zwischen der zweiten und der dritten Folie geändert? Nur der Hintergrund. Im Interface heißt die abdunkelnde Fläche »Scrim« (Material Design) oder Backdrop (CSS: ::backdrop beim Element dialog).

  **Ebenen:** Ein Screen mit drei Ebenen. Ganz hinten die Seite mit ihren Karten. Darüber ein schwebender Button (in Material Design: Floating Action Button) mit kleinem Schatten: Er bleibt beim Scrollen stehen und gehört nicht zum Inhalt. Ganz vorn ein Bottom Sheet mit großem Schatten nach oben: Es verdeckt die Seite und verlangt Aufmerksamkeit. Die Höhe sagt, wie wichtig und wie vorübergehend etwas ist. Je höher, desto eher erwartet man, dass es wieder verschwindet.

  **Echte Beispiele:** Airbnb (2026): Das Suchfeld schwebt mit Schatten über der Seite, die Karten liegen flach. Booking.com (2026): Seite abgedunkelt, Suchleiste, darüber der Dialog. Fragen: Welche Ebenen erkennen Sie? Woran?
---

{% frame '{"w":450,"h":900,"bu":"Eine Seite"}' %}
  <rect data-id="bild" x="40" y="60" width="370" height="200" fill="#d9d9d9" />
  <rect data-id="h1" x="40" y="292" width="250" height="22" fill="#888888" />
  <rect data-id="t1" x="40" y="336" width="370" height="12" fill="#d9d9d9" />
  <rect data-id="t2" x="40" y="360" width="370" height="12" fill="#d9d9d9" />
  <rect data-id="t3" x="40" y="384" width="300" height="12" fill="#d9d9d9" />
  <rect data-id="k1" x="40" y="430" width="370" height="150" fill="#e4e4e4" />
  <rect data-id="k1b" x="60" y="450" width="110" height="110" fill="#c4c4c4" />
  <rect data-id="k1t1" x="190" y="460" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k1t2" x="190" y="490" width="160" height="10" fill="#aaaaaa" />
  <rect data-id="k2" x="40" y="600" width="370" height="150" fill="#e4e4e4" />
  <rect data-id="k2b" x="60" y="620" width="110" height="110" fill="#c4c4c4" />
  <rect data-id="k2t1" x="190" y="630" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k2t2" x="190" y="660" width="160" height="10" fill="#aaaaaa" />
  <rect data-id="btn" x="40" y="780" width="160" height="44" rx="22" fill="#231f20" />
{% endframe %}
{% frame '{"w":450,"h":900,"bu":"Ein Dialog öffnet sich. Was liegt vorn?"}' %}
  <rect data-id="bild" x="40" y="60" width="370" height="200" fill="#d9d9d9" />
  <rect data-id="h1" x="40" y="292" width="250" height="22" fill="#888888" />
  <rect data-id="t1" x="40" y="336" width="370" height="12" fill="#d9d9d9" />
  <rect data-id="t2" x="40" y="360" width="370" height="12" fill="#d9d9d9" />
  <rect data-id="t3" x="40" y="384" width="300" height="12" fill="#d9d9d9" />
  <rect data-id="k1" x="40" y="430" width="370" height="150" fill="#e4e4e4" />
  <rect data-id="k1b" x="60" y="450" width="110" height="110" fill="#c4c4c4" />
  <rect data-id="k1t1" x="190" y="460" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k1t2" x="190" y="490" width="160" height="10" fill="#aaaaaa" />
  <rect data-id="k2" x="40" y="600" width="370" height="150" fill="#e4e4e4" />
  <rect data-id="k2b" x="60" y="620" width="110" height="110" fill="#c4c4c4" />
  <rect data-id="k2t1" x="190" y="630" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k2t2" x="190" y="660" width="160" height="10" fill="#aaaaaa" />
  <rect data-id="btn" x="40" y="780" width="160" height="44" rx="22" fill="#231f20" />

  <rect data-id="dlg" x="45" y="310" width="360" height="290" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="dh" x="75" y="345" width="200" height="20" fill="#888888" />
  <rect data-id="dt1" x="75" y="387" width="300" height="12" fill="#d9d9d9" />
  <rect data-id="dt2" x="75" y="411" width="300" height="12" fill="#d9d9d9" />
  <rect data-id="dt3" x="75" y="435" width="200" height="12" fill="#d9d9d9" />
  <rect data-id="db1" x="75" y="490" width="140" height="44" rx="22" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="db2" x="235" y="490" width="140" height="44" rx="22" fill="#9313ce" />
{% endframe %}
{% frame '{"w":450,"h":900,"bu":"Hintergrund abgedunkelt: Die Seite rückt nach hinten"}' %}
  <rect data-id="bild" x="40" y="60" width="370" height="200" fill="#d9d9d9" />
  <rect data-id="h1" x="40" y="292" width="250" height="22" fill="#888888" />
  <rect data-id="t1" x="40" y="336" width="370" height="12" fill="#d9d9d9" />
  <rect data-id="t2" x="40" y="360" width="370" height="12" fill="#d9d9d9" />
  <rect data-id="t3" x="40" y="384" width="300" height="12" fill="#d9d9d9" />
  <rect data-id="k1" x="40" y="430" width="370" height="150" fill="#e4e4e4" />
  <rect data-id="k1b" x="60" y="450" width="110" height="110" fill="#c4c4c4" />
  <rect data-id="k1t1" x="190" y="460" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k1t2" x="190" y="490" width="160" height="10" fill="#aaaaaa" />
  <rect data-id="k2" x="40" y="600" width="370" height="150" fill="#e4e4e4" />
  <rect data-id="k2b" x="60" y="620" width="110" height="110" fill="#c4c4c4" />
  <rect data-id="k2t1" x="190" y="630" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k2t2" x="190" y="660" width="160" height="10" fill="#aaaaaa" />
  <rect data-id="btn" x="40" y="780" width="160" height="44" rx="22" fill="#231f20" />
  <rect data-id="scrim" x="0" y="0" width="450" height="900" fill="#231f20" fill-opacity="0.55" />

  <rect data-id="dlg" x="45" y="310" width="360" height="290" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="dh" x="75" y="345" width="200" height="20" fill="#888888" />
  <rect data-id="dt1" x="75" y="387" width="300" height="12" fill="#d9d9d9" />
  <rect data-id="dt2" x="75" y="411" width="300" height="12" fill="#d9d9d9" />
  <rect data-id="dt3" x="75" y="435" width="200" height="12" fill="#d9d9d9" />
  <rect data-id="db1" x="75" y="490" width="140" height="44" rx="22" fill="#ffffff" stroke="#888888" stroke-width="2" />
  <rect data-id="db2" x="235" y="490" width="140" height="44" rx="22" fill="#9313ce" />
{% endframe %}

{% frame '{"w":450,"h":900,"animate":false,"bu":"Ebene 0: die Seite"}' %}
  <defs><filter id="ev1" x="-40%" y="-40%" width="180%" height="190%"><feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#231f20" flood-opacity="0.3"/></filter><filter id="ev2s" x="-10%" y="-20%" width="120%" height="140%"><feDropShadow dx="0" dy="-6" stdDeviation="14" flood-color="#231f20" flood-opacity="0.3"/></filter></defs>
  <rect data-id="bild" x="40" y="60" width="370" height="180" fill="#d9d9d9" />
  <rect data-id="h1" x="40" y="272" width="250" height="22" fill="#888888" />
  <rect data-id="k1" x="40" y="320" width="370" height="140" fill="#e4e4e4" />
  <rect data-id="k1b" x="60" y="340" width="100" height="100" fill="#c4c4c4" />
  <rect data-id="k1t1" x="180" y="350" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k1t2" x="180" y="378" width="150" height="10" fill="#aaaaaa" />
  <rect data-id="k2" x="40" y="480" width="370" height="140" fill="#e4e4e4" />
  <rect data-id="k2b" x="60" y="500" width="100" height="100" fill="#c4c4c4" />
  <rect data-id="k2t1" x="180" y="510" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k2t2" x="180" y="538" width="150" height="10" fill="#aaaaaa" />
  <rect data-id="k3" x="40" y="640" width="370" height="140" fill="#e4e4e4" />
  <rect data-id="k3b" x="60" y="660" width="100" height="100" fill="#c4c4c4" />
  <rect data-id="k3t1" x="180" y="670" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k3t2" x="180" y="698" width="150" height="10" fill="#aaaaaa" />
{% endframe %}
{% frame '{"w":450,"h":900,"bu":"Ebene 1: Ein Button schwebt darüber"}' %}
  <defs><filter id="ev1" x="-40%" y="-40%" width="180%" height="190%"><feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#231f20" flood-opacity="0.3"/></filter><filter id="ev2s" x="-10%" y="-20%" width="120%" height="140%"><feDropShadow dx="0" dy="-6" stdDeviation="14" flood-color="#231f20" flood-opacity="0.3"/></filter></defs>
  <rect data-id="bild" x="40" y="60" width="370" height="180" fill="#d9d9d9" />
  <rect data-id="h1" x="40" y="272" width="250" height="22" fill="#888888" />
  <rect data-id="k1" x="40" y="320" width="370" height="140" fill="#e4e4e4" />
  <rect data-id="k1b" x="60" y="340" width="100" height="100" fill="#c4c4c4" />
  <rect data-id="k1t1" x="180" y="350" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k1t2" x="180" y="378" width="150" height="10" fill="#aaaaaa" />
  <rect data-id="k2" x="40" y="480" width="370" height="140" fill="#e4e4e4" />
  <rect data-id="k2b" x="60" y="500" width="100" height="100" fill="#c4c4c4" />
  <rect data-id="k2t1" x="180" y="510" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k2t2" x="180" y="538" width="150" height="10" fill="#aaaaaa" />
  <rect data-id="k3" x="40" y="640" width="370" height="140" fill="#e4e4e4" />
  <rect data-id="k3b" x="60" y="660" width="100" height="100" fill="#c4c4c4" />
  <rect data-id="k3t1" x="180" y="670" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k3t2" x="180" y="698" width="150" height="10" fill="#aaaaaa" />
  <circle data-id="fab" cx="360" cy="810" r="32" fill="#9313ce" filter="url(#ev1)" />
{% endframe %}
{% frame '{"w":450,"h":900,"bu":"Ebene 2: Ein Bottom Sheet schiebt sich nach vorn"}' %}
  <defs><filter id="ev1" x="-40%" y="-40%" width="180%" height="190%"><feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#231f20" flood-opacity="0.3"/></filter><filter id="ev2s" x="-10%" y="-20%" width="120%" height="140%"><feDropShadow dx="0" dy="-6" stdDeviation="14" flood-color="#231f20" flood-opacity="0.3"/></filter></defs>
  <rect data-id="bild" x="40" y="60" width="370" height="180" fill="#d9d9d9" />
  <rect data-id="h1" x="40" y="272" width="250" height="22" fill="#888888" />
  <rect data-id="k1" x="40" y="320" width="370" height="140" fill="#e4e4e4" />
  <rect data-id="k1b" x="60" y="340" width="100" height="100" fill="#c4c4c4" />
  <rect data-id="k1t1" x="180" y="350" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k1t2" x="180" y="378" width="150" height="10" fill="#aaaaaa" />
  <rect data-id="k2" x="40" y="480" width="370" height="140" fill="#e4e4e4" />
  <rect data-id="k2b" x="60" y="500" width="100" height="100" fill="#c4c4c4" />
  <rect data-id="k2t1" x="180" y="510" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k2t2" x="180" y="538" width="150" height="10" fill="#aaaaaa" />
  <rect data-id="k3" x="40" y="640" width="370" height="140" fill="#e4e4e4" />
  <rect data-id="k3b" x="60" y="660" width="100" height="100" fill="#c4c4c4" />
  <rect data-id="k3t1" x="180" y="670" width="190" height="14" fill="#aaaaaa" />
  <rect data-id="k3t2" x="180" y="698" width="150" height="10" fill="#aaaaaa" />
  <circle data-id="fab" cx="360" cy="810" r="32" fill="#9313ce" filter="url(#ev1)" />
  <path data-id="sheet" d="M0 920 L0 560 Q0 540 20 540 L430 540 Q450 540 450 560 L450 920 Z" fill="#ffffff" filter="url(#ev2s)" />
  <line data-id="griff" x1="200" y1="562" x2="250" y2="562" stroke="#d9d9d9" stroke-width="6" stroke-linecap="round" />
  <rect data-id="sh" x="40" y="600" width="220" height="22" fill="#888888" />
  <rect data-id="st1" x="40" y="644" width="370" height="12" fill="#d9d9d9" />
  <rect data-id="st2" x="40" y="668" width="300" height="12" fill="#d9d9d9" />
  <rect data-id="sbtn" x="40" y="712" width="370" height="48" rx="24" fill="#231f20" />
{% endframe %}

{% screenshot "./images/ebenen-airbnb.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Das Suchfeld schwebt, die Karten liegen flach<br><small>airbnb.de, Screenshot 2026</small>"}' %}
{% screenshot "./images/ebenen-booking.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Wie viele Ebenen sehen Sie? Woran erkennen Sie sie?<br><small>booking.com, Screenshot 2026</small>"}' %}

{% question "Welche Ebenen hat Ihre meistgenutzte App?", "Was liegt ganz hinten, was ganz vorn? Und woran erkennen Sie das?" %}
