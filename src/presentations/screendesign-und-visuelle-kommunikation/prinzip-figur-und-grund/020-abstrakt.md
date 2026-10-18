---
title: "Was wird Figur?"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Vier Kompositionen, nur zwei Flächen, Schwarz und Weiß.

  1. Halb und halb: Welche Seite ist Figur? Unentschieden, die Fläche kippt.
  2. Kleines schwarzes Quadrat in Weiß: eindeutig Figur, weil klein und umschlossen.
  3. Umgekehrt, weißes Quadrat in Schwarz: Jetzt ist das Weiß die Figur. Die Farbe entscheidet nicht, das Verhältnis entscheidet.
  4. Schwarz unten: wird eher als Boden oder Figur gelesen, weil unten Schwerkraft und Halt sind (Prinzip Kräfte).

  Danach folgen die Visualisierungen aus dem bisherigen Foliensatz mit den Merkmalen im Detail.
---

{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Halb und halb: Was ist Figur?"}' %}
<rect data-id="w" x="0" y="0" width="600" height="600" rx="0" fill="#ffffff" />
<rect data-id="b" x="300" y="0" width="300" height="600" rx="0" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Klein und umschlossen: eindeutig Figur"}' %}
<rect data-id="w" x="0" y="0" width="600" height="600" rx="0" fill="#ffffff" />
<rect data-id="b" x="220" y="220" width="160" height="160" rx="0" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Umgekehrt: Jetzt ist das Weiß die Figur"}' %}
<rect data-id="w" x="0" y="0" width="600" height="600" rx="0" fill="#ffffff" />
<rect data-id="b" x="0" y="0" width="600" height="600" rx="0" fill="#231f20" />
<rect data-id="w2" x="220" y="220" width="160" height="160" rx="0" fill="#ffffff" />
{% endframe %}
{% frame '{"stage":"#666666", "w":600, "h":600, "bu":"Unten wird eher zur Figur als oben"}' %}
<rect data-id="w" x="0" y="0" width="600" height="600" rx="0" fill="#ffffff" />
<rect data-id="b" x="0" y="330" width="600" height="270" rx="0" fill="#231f20" />
{% endframe %}

