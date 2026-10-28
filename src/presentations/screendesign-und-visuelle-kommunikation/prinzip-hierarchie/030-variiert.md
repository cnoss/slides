---
title: "Headline und Text"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Nach der Headline-Copy-Demo aus dem bisherigen Foliensatz (Räumlichkeit), jetzt als Wireframe. Pro Folie ändert sich genau eine Sache.

  1. Alle Zeilen gleich: Headline, Text und Button sind nicht zu unterscheiden.
  2. Die Headline wird größer, dunkler und bekommt Abstand: Jetzt gibt es einen Einstieg.
  3. Der Text wird heller. Die Headline hat sich nicht verändert, wirkt aber noch stärker. Das ist Betonen durch Zurücknehmen.
  4. Der Button bekommt Form und Akzentfarbe: Die Handlung ist das Ziel der Seite.

  **Hintergrund**

  »Emphasize by de-emphasizing«: Wathan und Schoger raten in »Refactoring UI« (2018), Konkurrenz nicht durch immer lautere Hauptelemente zu lösen, sondern die Nebenelemente leiser zu machen. Wer alles lauter macht, landet wieder bei Folie 1, nur in groß.
---

{% frame '{"stage":"#ffffff","w":900,"h":500,"bu":"Alles gleich: Wo fangen Sie an?"}' %}
  <rect data-id="h0" x="150" y="100" width="600" height="14" fill="#888888" />
  <rect data-id="t0" x="150" y="130" width="600" height="14" fill="#888888" />
  <rect data-id="t1" x="150" y="160" width="600" height="14" fill="#888888" />
  <rect data-id="t2" x="150" y="190" width="600" height="14" fill="#888888" />
  <rect data-id="t3" x="150" y="220" width="420" height="14" fill="#888888" />
  <rect data-id="btn" x="150" y="300" width="160" height="14" rx="0" fill="#888888" />
{% endframe %}
{% frame '{"stage":"#ffffff","w":900,"h":500,"bu":"Die Headline wird größer"}' %}
  <rect data-id="h0" x="150" y="100" width="480" height="40" fill="#231f20" />
  <rect data-id="t0" x="150" y="170" width="600" height="14" fill="#888888" />
  <rect data-id="t1" x="150" y="200" width="600" height="14" fill="#888888" />
  <rect data-id="t2" x="150" y="230" width="600" height="14" fill="#888888" />
  <rect data-id="t3" x="150" y="260" width="420" height="14" fill="#888888" />
  <rect data-id="btn" x="150" y="300" width="160" height="14" rx="0" fill="#888888" />
{% endframe %}
{% frame '{"stage":"#ffffff","w":900,"h":500,"bu":"Der Text tritt zurück"}' %}
  <rect data-id="h0" x="150" y="100" width="480" height="40" fill="#231f20" />
  <rect data-id="t0" x="150" y="170" width="600" height="14" fill="#d9d9d9" />
  <rect data-id="t1" x="150" y="200" width="600" height="14" fill="#d9d9d9" />
  <rect data-id="t2" x="150" y="230" width="600" height="14" fill="#d9d9d9" />
  <rect data-id="t3" x="150" y="260" width="420" height="14" fill="#d9d9d9" />
  <rect data-id="btn" x="150" y="300" width="160" height="14" rx="0" fill="#888888" />
{% endframe %}
{% frame '{"stage":"#ffffff","w":900,"h":500,"bu":"Die Handlung bekommt die Akzentfarbe"}' %}
  <rect data-id="h0" x="150" y="100" width="480" height="40" fill="#231f20" />
  <rect data-id="t0" x="150" y="170" width="600" height="14" fill="#d9d9d9" />
  <rect data-id="t1" x="150" y="200" width="600" height="14" fill="#d9d9d9" />
  <rect data-id="t2" x="150" y="230" width="600" height="14" fill="#d9d9d9" />
  <rect data-id="t3" x="150" y="260" width="420" height="14" fill="#d9d9d9" />
  <rect data-id="btn" x="150" y="290" width="180" height="48" rx="24" fill="#9313ce" />
{% endframe %}

{% statement "Betonen durch Zurücknehmen.", "Oft ist es leichter, das Unwichtige leiser zu machen, als das Wichtige lauter." %}
