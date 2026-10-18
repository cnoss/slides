---
title: Farbe-an-sich-Kontrast
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Reine, ungetrübte Farbtöne nebeneinander, am stärksten bei den Grundfarben Gelb, Rot und Blau. Wirkt laut, fröhlich, kindlich, plakativ. Wird er zurückgenommen (gedämpfte Töne), wird es ruhiger. Typisch für Spielzeug, Kinderangebote, Marken, die Energie zeigen wollen.

  Beispiele: DHL kombiniert Gelb und Rot, zwei reine Farbtöne. Die Vitra-Startseite von 2006 (Web Archive) zeigt den Kontrast als Fläche. Das ist ein historisches Beispiel und als solches gekennzeichnet.
---

{% interlude "Farbe-an-sich-Kontrast" %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Reine Farbtöne nebeneinander: laut und plakativ"}' %}
<rect data-id="r0" x="50.0" y="150" width="144" height="200" fill="#e8002a" />
<rect data-id="r1" x="214.0" y="150" width="144" height="200" fill="#f7d117" />
<rect data-id="r2" x="378.0" y="150" width="144" height="200" fill="#1f4fd8" />
<rect data-id="r3" x="542.0" y="150" width="144" height="200" fill="#14a33c" />
<rect data-id="r4" x="706.0" y="150" width="144" height="200" fill="#ff7a00" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Dieselben Farbtöne, gedämpft: Der Kontrast wird schwächer"}' %}
<rect data-id="r0" x="50.0" y="150" width="144" height="200" fill="#b9636b" />
<rect data-id="r1" x="214.0" y="150" width="144" height="200" fill="#c9b36a" />
<rect data-id="r2" x="378.0" y="150" width="144" height="200" fill="#5c6a9b" />
<rect data-id="r3" x="542.0" y="150" width="144" height="200" fill="#6f9077" />
<rect data-id="r4" x="706.0" y="150" width="144" height="200" fill="#c08a5b" />
{% endframe %}
{% screenshot "./images/kontrast-dhl.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Gelb und Rot: zwei reine Farbtöne<br><small>dhl.de, Screenshot 2026</small>"}' %}
{% screenshot "./images/farbe-an-sich-kontrast-06.png", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Der Kontrast als Fläche<br><small>vitra.de 2006, über web.archive.org</small>"}' %}
