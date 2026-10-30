---
title: "Ausrichtung abstrakt"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Fünf Formen, verschieden groß, verschieden in der Form. Erst frei verteilt: Jede steht für sich, das Ganze wirkt zufällig. Dann richten sie sich an einer Kante aus, und plötzlich ist es eine Gruppe. Die lila Linie zeigt die Kante einmal, danach verschwindet sie wieder. Gesehen wird sie trotzdem.

  Dann die anderen Möglichkeiten: Mittelachse und Grundlinie (Baseline). Fragen: Welche Fassung wirkt am ruhigsten? Welche am festesten? Meist: die linke Kante am ruhigsten (sie ist am leichtesten zu verfolgen, weil sie gerade ist), die Grundlinie am festesten (alles steht, siehe Kräfte). Die Mittelachse erzeugt einen unruhigen, gezackten Rand auf beiden Seiten.

  Kreise und Quadrate an derselben Kante wirken nicht ganz bündig. Das ist ein Fall für die optische Korrektur (siehe Phänomen Optische Korrektur).
---

{% frame '{"stage":"#ffffff","bu":"Frei verteilt: Jede Form steht für sich"}' %}
  <rect data-id="s0" x="330" y="70" width="120" height="70" fill="#231f20" />
  <circle data-id="s1" cx="160" cy="210" r="40" fill="#231f20" />
  <rect data-id="s2" x="420" y="250" width="60" height="60" fill="#231f20" />
  <rect data-id="s3" x="200" y="330" width="200" height="40" fill="#231f20" />
  <circle data-id="s4" cx="115" cy="495" r="25" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff","bu":"An einer Kante ausgerichtet: eine Gruppe"}' %}
  <rect data-id="s0" x="150" y="70" width="120" height="70" fill="#231f20" />
  <circle data-id="s1" cx="190" cy="220" r="40" fill="#231f20" />
  <rect data-id="s2" x="150" y="300" width="60" height="60" fill="#231f20" />
  <rect data-id="s3" x="150" y="400" width="200" height="40" fill="#231f20" />
  <circle data-id="s4" cx="175" cy="505" r="25" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff","bu":"Die Kante, die man sieht, obwohl sie nicht da ist"}' %}
  <rect data-id="s0" x="150" y="70" width="120" height="70" fill="#231f20" />
  <circle data-id="s1" cx="190" cy="220" r="40" fill="#231f20" />
  <rect data-id="s2" x="150" y="300" width="60" height="60" fill="#231f20" />
  <rect data-id="s3" x="150" y="400" width="200" height="40" fill="#231f20" />
  <circle data-id="s4" cx="175" cy="505" r="25" fill="#231f20" />
  <line data-id="achse" x1="150" y1="40" x2="150" y2="560" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
{% endframe %}
{% frame '{"stage":"#ffffff","bu":"An der Mittelachse"}' %}
  <rect data-id="s0" x="240" y="70" width="120" height="70" fill="#231f20" />
  <circle data-id="s1" cx="300" cy="220" r="40" fill="#231f20" />
  <rect data-id="s2" x="270" y="300" width="60" height="60" fill="#231f20" />
  <rect data-id="s3" x="200" y="400" width="200" height="40" fill="#231f20" />
  <circle data-id="s4" cx="300" cy="505" r="25" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff","bu":"Auf einer Grundlinie (Baseline)"}' %}
  <rect data-id="s0" x="60" y="330" width="120" height="70" fill="#231f20" />
  <circle data-id="s1" cx="240" cy="360" r="40" fill="#231f20" />
  <rect data-id="s2" x="300" y="340" width="60" height="60" fill="#231f20" />
  <rect data-id="s3" x="380" y="360" width="200" height="40" fill="#231f20" />
  <circle data-id="s4" cx="625" cy="375" r="25" fill="#231f20" />
{% endframe %}
