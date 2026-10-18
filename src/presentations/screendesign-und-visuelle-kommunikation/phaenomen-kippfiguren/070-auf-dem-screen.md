---
title: "Auf dem Screen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Zwei Seiten desselben Phänomens.

  **Bewusst eingesetzt:** Die Carlsberg-Anzeigen aus dem bisherigen Foliensatz spielen mit Figur und Grund. Erst sieht man ein Fenster oder zwei Schuhe, dann das Bierglas, das im Zwischenraum entsteht. Das ist Absicht und funktioniert, weil man nach dem Kippen belohnt wird. Die Anzeigen sind älter (um 2008).

  **Unbeabsichtigt:** Ein Schalter, der nur über Graustufen arbeitet. Ist er an oder aus? Der Knopf links oder rechts, das helle oder das dunkle Feld: Beide Lesarten sind möglich. Im Interface ist eine Kippfigur ein Fehler. Lösung: eindeutig. Die Akzentfarbe zeigt »an«, Position und Farbe sagen dasselbe.
---

{% screenshot "./images/carlsberg-01.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Gewollt: Erst das Fenster, dann das Glas<br><small>Carlsberg, Anzeige, aus dem Bestand</small>"}' %}
{% screenshot "./images/carlsberg-02.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Gewollt: Erst die Schuhe, dann das Glas<br><small>Carlsberg, Anzeige, aus dem Bestand</small>"}' %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Ungewollt: Welcher Schalter ist an?"}' %}
<rect data-id="t0" x="200" y="200" width="200" height="100" rx="50" fill="#888888" />
<circle data-id="k0" cx="350" cy="250" r="40" fill="#ffffff" />
<rect data-id="t1" x="500" y="200" width="200" height="100" rx="50" fill="#d9d9d9" />
<circle data-id="k1" cx="550" cy="250" r="40" fill="#ffffff" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Eindeutig: Farbe und Position sagen dasselbe"}' %}
<rect data-id="t0" x="200" y="200" width="200" height="100" rx="50" fill="#9313ce" />
<circle data-id="k0" cx="350" cy="250" r="40" fill="#ffffff" />
<rect data-id="t1" x="500" y="200" width="200" height="100" rx="50" fill="#d9d9d9" />
<circle data-id="k1" cx="550" cy="250" r="40" fill="#ffffff" />
{% endframe %}
