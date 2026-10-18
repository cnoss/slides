---
title: "Farbklima ableiten"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  **Farbklima ableiten** in vier Schritten, am Beispiel eines Brotfotos aus dem Moodboard:

  1. **Bild wählen:** das Bild, das die Stimmung am besten trägt.
  2. **Rastern:** Das Bild wird stark verpixelt. Details verschwinden, die Farbflächen bleiben. Genau das macht der Sketch P_1_2_2_01 in »Generative Gestaltung« (Groß, Bohnacker, Laub, Lazzeroni, 2018) mit Code.
  3. **Farben zählen:** Die häufigsten Farben bestimmen und nach Fläche gewichten. Hier: dunkles Braun dominiert, dann Kruste und Orange, wenig Hell.
  4. **Rollen vergeben:** Ein Farbklima ist noch keine Palette fürs Interface. Jede Farbe bekommt eine Rolle: Fläche (meist die hellste, oft aufgehellt), Text (die dunkelste), Akzent (die kräftigste), Ergänzung. Das Flächenverhältnis kehrt sich dabei oft um: Im Bild dominiert das Dunkel, im Interface wird es zur Schrift.

  Danach: Kontrast prüfen. Die Farben aus dem Bild sind selten auf Anhieb kontrastsicher.

  Werkzeuge: Adobe Color (»Aus Bild extrahieren«), Coolors, Figma-Plugins, oder per Code.
---

{% interlude "Farbklima ableiten", "Vom Bild zur Palette" %}

{% screenshot "./images/ableiten-original.jpg", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"1. Ein Bild, das die Stimmung trägt"}' %}
{% screenshot "./images/ableiten-raster.png", '{"transition":"none", "classes":"no-shadow", "width":"auto", "bu":"2. Rastern: Details verschwinden, Farbflächen bleiben"}' %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"3. Farben zählen: Die Breite zeigt die Fläche im Bild"}' %}
<rect data-id="p0" x="50" y="150" width="293" height="200" rx="0" fill="#523B21" />
<rect data-id="p1" x="343" y="150" width="222" height="200" rx="0" fill="#A36633" />
<rect data-id="p2" x="565" y="150" width="151" height="200" rx="0" fill="#D1995C" />
<rect data-id="p3" x="716" y="150" width="90" height="200" rx="0" fill="#DCBD99" />
<rect data-id="p4" x="806" y="150" width="44" height="200" rx="0" fill="#8E7F80" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"4. Rollen vergeben: Fläche, Text, Akzent, Ergänzung"}' %}
<rect data-id="p3" x="50" y="150" width="420" height="200" rx="0" fill="#DCBD99" />
<rect data-id="p0" x="490" y="150" width="180" height="200" rx="0" fill="#523B21" />
<rect data-id="p1" x="690" y="150" width="100" height="200" rx="0" fill="#A36633" />
<rect data-id="p2" x="810" y="150" width="40" height="200" rx="0" fill="#D1995C" />
<rect data-id="p4" x="850" y="150" width="0" height="200" rx="0" fill="#8E7F80" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Und im Interface: Das Dunkel aus dem Bild wird zur Schrift"}' %}
<rect data-id="bg" x="250" y="30" width="400" height="440" rx="0" fill="#f6efe4" />
<rect data-id="img" x="270" y="50" width="360" height="170" rx="0" fill="#DCBD99" />
<rect data-id="h" x="270" y="245" width="240" height="26" rx="0" fill="#523B21" />
<rect data-id="t0" x="270" y="290" width="340" height="10" rx="0" fill="#c9b49a" />
<rect data-id="t1" x="270" y="312" width="300" height="10" rx="0" fill="#c9b49a" />
<rect data-id="btn" x="270" y="380" width="170" height="46" rx="23" fill="#A36633" />
<rect data-id="tag" x="460" y="388" width="90" height="30" rx="15" fill="#D1995C" />
{% endframe %}
