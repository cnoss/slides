---
title: "Auf dem Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Auch Text ist Verdichtung: Buchstaben sind Linien und Punkte, Zeilen verdichten sich zu grauen Flächen. Typografen nennen das den Grauwert eines Textes. Beim Weiterschalten wird der Screen unscharf: Übrig bleiben Flächen, Gewichte, Hierarchie. Das ist der Unschärfetest, eine Methode, die diesen Effekt bewusst nutzt. Wer die Augen zusammenkneift, macht dasselbe.

  **Gemeinsam an der Wand (ca. 5 Minuten):** Zwei Screens, jeweils erst scharf. Alle kneifen die Augen zusammen, bis die Schrift nicht mehr lesbar ist, und sagen, was sie zuerst sehen. Dann die unscharfe Fassung zeigen und vergleichen.

  - **Apple, AirPods:** Übrig bleiben die dunkle Figur auf hellem Blau, darunter eine große Zeile, oben eine ruhige Navigation. Eine Botschaft, klare Rangfolge. Der Blick weiß, wo er anfangen soll.
  - **Temu:** Übrig bleiben gleich große, gleich laute Produktkacheln über die ganze Fläche, dazu der orange Kopf. Nichts setzt sich ab, es gibt keinen Einstieg. Das ist hier Absicht: Der endlose Strom gleichwertiger Angebote soll zum Weiterscrollen verleiten (Bezug zur Haltung Verantwortung und zu Aufmerksamkeit respektieren).

  Fragen für die Diskussion: Wo landet Ihr Blick zuerst? Wie viele Ebenen erkennen Sie? Was würden Sie an Temu ändern, damit nach dem Zusammenkneifen eine Ordnung übrig bleibt? Und warum macht Temu das nicht?

  Screenshot: de.wikipedia.org, Artikel Pointillismus, 2026.
---

{% screenshot "./images/screen-text.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Text, Bilder, Navigation<br><small>de.wikipedia.org, Screenshot 2026</small>"}' %}
{% screenshot "./images/screen-text-unscharf.jpg", '{"transition":"none", "classes":"shadow", "width":"auto", "bu":"Unscharf: Text wird zu grauen Flächen<br><small>de.wikipedia.org, Screenshot 2026</small>"}' %}

{% interlude "Kneifen Sie die Augen zusammen.", "Und schauen Sie auf die Wand. Was bleibt übrig?" %}

{% screenshot "./images/kneifen-apple.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Kneifen Sie die Augen zusammen. Was sehen Sie zuerst?<br><small>apple.com/de/airpods, Screenshot 2026</small>"}' %}
{% screenshot "./images/kneifen-apple-unscharf.jpg", '{"transition":"none", "classes":"shadow", "width":"auto", "bu":"Unscharf: eine Figur, ein Farbfeld, eine Zeile. Die Hierarchie bleibt.<br><small>apple.com/de/airpods, Screenshot 2026</small>"}' %}
{% screenshot "./images/kneifen-temu.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Und hier? Was sehen Sie zuerst?<br><small>temu.com, Screenshot 2026</small>"}' %}
{% screenshot "./images/kneifen-temu-unscharf.jpg", '{"transition":"none", "classes":"shadow", "width":"auto", "bu":"Unscharf: lauter gleich starke Kacheln. Nichts setzt sich ab.<br><small>temu.com, Screenshot 2026</small>"}' %}

{% statement "Was beim Zusammenkneifen übrig bleibt, ist die Hierarchie.", "Bleibt eine klare Ordnung, trägt die Gestaltung. Bleibt nur Rauschen, fehlt sie." %}
