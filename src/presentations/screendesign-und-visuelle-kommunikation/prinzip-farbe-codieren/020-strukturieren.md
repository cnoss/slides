---
title: Farbe zum Strukturieren
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Gleiche Farbe stiftet Zusammengehörigkeit, auch über Entfernung hinweg. Das ist das Gestaltgesetz der Ähnlichkeit, angewendet auf Farbe. Erst sind alle Punkte grau: ein Feld. Dann bekommen sie drei Farben: Sofort entstehen drei Gruppen, obwohl sich an der Position nichts geändert hat. Zum Schluss sortiert.

  Beispiele aus der Welt: Liniennetzpläne (jede Linie eine Farbe), Wegeleitsysteme in Krankenhäusern, Kabel mit Farbcode, Kalender-Apps mit einer Farbe pro Kalender, Labels in GitHub oder Trello.

  Bilder aus dem bisherigen Foliensatz: Netzplan Bahnen in Köln (KVB, 2023), Wegeleitsystem in einem Krankenhaus, Netzwerkkabel.
---

{% interlude "Farbe zum Strukturieren", "Was die gleiche Farbe hat, gehört zusammen." %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Achtzehn Punkte: ein Feld"}' %}
<circle data-id="p0" cx="120" cy="120" r="38" fill="#888888" />
<circle data-id="p1" cx="250" cy="120" r="38" fill="#888888" />
<circle data-id="p2" cx="380" cy="120" r="38" fill="#888888" />
<circle data-id="p3" cx="510" cy="120" r="38" fill="#888888" />
<circle data-id="p4" cx="640" cy="120" r="38" fill="#888888" />
<circle data-id="p5" cx="770" cy="120" r="38" fill="#888888" />
<circle data-id="p6" cx="120" cy="250" r="38" fill="#888888" />
<circle data-id="p7" cx="250" cy="250" r="38" fill="#888888" />
<circle data-id="p8" cx="380" cy="250" r="38" fill="#888888" />
<circle data-id="p9" cx="510" cy="250" r="38" fill="#888888" />
<circle data-id="p10" cx="640" cy="250" r="38" fill="#888888" />
<circle data-id="p11" cx="770" cy="250" r="38" fill="#888888" />
<circle data-id="p12" cx="120" cy="380" r="38" fill="#888888" />
<circle data-id="p13" cx="250" cy="380" r="38" fill="#888888" />
<circle data-id="p14" cx="380" cy="380" r="38" fill="#888888" />
<circle data-id="p15" cx="510" cy="380" r="38" fill="#888888" />
<circle data-id="p16" cx="640" cy="380" r="38" fill="#888888" />
<circle data-id="p17" cx="770" cy="380" r="38" fill="#888888" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Drei Farben, drei Gruppen. Die Positionen sind gleich geblieben"}' %}
<circle data-id="p0" cx="120" cy="120" r="38" fill="#2c6ea8" />
<circle data-id="p1" cx="250" cy="120" r="38" fill="#e86a10" />
<circle data-id="p2" cx="380" cy="120" r="38" fill="#2c6ea8" />
<circle data-id="p3" cx="510" cy="120" r="38" fill="#1a8a3a" />
<circle data-id="p4" cx="640" cy="120" r="38" fill="#e86a10" />
<circle data-id="p5" cx="770" cy="120" r="38" fill="#e86a10" />
<circle data-id="p6" cx="120" cy="250" r="38" fill="#2c6ea8" />
<circle data-id="p7" cx="250" cy="250" r="38" fill="#2c6ea8" />
<circle data-id="p8" cx="380" cy="250" r="38" fill="#2c6ea8" />
<circle data-id="p9" cx="510" cy="250" r="38" fill="#2c6ea8" />
<circle data-id="p10" cx="640" cy="250" r="38" fill="#e86a10" />
<circle data-id="p11" cx="770" cy="250" r="38" fill="#1a8a3a" />
<circle data-id="p12" cx="120" cy="380" r="38" fill="#e86a10" />
<circle data-id="p13" cx="250" cy="380" r="38" fill="#2c6ea8" />
<circle data-id="p14" cx="380" cy="380" r="38" fill="#2c6ea8" />
<circle data-id="p15" cx="510" cy="380" r="38" fill="#1a8a3a" />
<circle data-id="p16" cx="640" cy="380" r="38" fill="#1a8a3a" />
<circle data-id="p17" cx="770" cy="380" r="38" fill="#e86a10" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Sortiert wird die Struktur offensichtlich"}' %}
<circle data-id="p0" cx="120" cy="120" r="38" fill="#2c6ea8" />
<circle data-id="p2" cx="215" cy="120" r="38" fill="#2c6ea8" />
<circle data-id="p6" cx="310" cy="120" r="38" fill="#2c6ea8" />
<circle data-id="p7" cx="405" cy="120" r="38" fill="#2c6ea8" />
<circle data-id="p8" cx="500" cy="120" r="38" fill="#2c6ea8" />
<circle data-id="p9" cx="595" cy="120" r="38" fill="#2c6ea8" />
<circle data-id="p13" cx="690" cy="120" r="38" fill="#2c6ea8" />
<circle data-id="p14" cx="785" cy="120" r="38" fill="#2c6ea8" />
<circle data-id="p1" cx="120" cy="250" r="38" fill="#e86a10" />
<circle data-id="p4" cx="215" cy="250" r="38" fill="#e86a10" />
<circle data-id="p5" cx="310" cy="250" r="38" fill="#e86a10" />
<circle data-id="p10" cx="405" cy="250" r="38" fill="#e86a10" />
<circle data-id="p12" cx="500" cy="250" r="38" fill="#e86a10" />
<circle data-id="p17" cx="595" cy="250" r="38" fill="#e86a10" />
<circle data-id="p3" cx="120" cy="380" r="38" fill="#1a8a3a" />
<circle data-id="p11" cx="215" cy="380" r="38" fill="#1a8a3a" />
<circle data-id="p15" cx="310" cy="380" r="38" fill="#1a8a3a" />
<circle data-id="p16" cx="405" cy="380" r="38" fill="#1a8a3a" />
{% endframe %}
{% screenshot "./images/koeln-fahrplan-01.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Jede Linie eine Farbe<br><small>Bahnen in Köln, KVB, 2023</small>"}' %}
{% screenshot "./images/krankenhaus-01.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Farbe ordnet Bereiche im Wegeleitsystem<br><small>Krankenhaus, Foto aus dem Bestand</small>"}' %}
{% screenshot "./images/kabel-01.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Farbe als technischer Code<br><small>Netzwerkkabel, Grafik aus dem Bestand</small>"}' %}
