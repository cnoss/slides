---
title: "Irradiation"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Zwei gleich große Quadrate, eines weiß auf Schwarz, eines schwarz auf Weiß. Fragen: Welches ist größer? Das helle wirkt größer. Helles strahlt auf der Netzhaut leicht in die dunkle Umgebung über.

  Korrektur: Das helle Element etwas kleiner zeichnen. In der Typografie: Weiße Schrift auf Schwarz wirkt fetter und größer. Im Dark Mode nimmt man deshalb oft einen etwas leichteren Schriftschnitt oder etwas mehr Laufweite.

  **Hintergrund:** Den Begriff Irradiation prägte Hermann von Helmholtz im »Handbuch der physiologischen Optik« (1867). Ursache ist die Streuung des Lichts im Auge.
---

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Welches Quadrat ist größer?"}' %}
<rect data-id="bg" x="50" y="50" width="400" height="400" fill="#231f20" />
<rect data-id="w" x="175" y="175" width="150" height="150" fill="#ffffff" />
<rect x="450" y="50" width="400" height="400" fill="none" stroke="#d9d9d9" stroke-width="2" />
<rect data-id="k" x="575.0" y="175" width="150" height="150" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Korrigiert: Das helle Quadrat ist etwas kleiner und wirkt jetzt gleich groß"}' %}
<rect data-id="bg" x="50" y="50" width="400" height="400" fill="#231f20" />
<rect data-id="w" x="180" y="180" width="140" height="140" fill="#ffffff" />
<rect x="450" y="50" width="400" height="400" fill="none" stroke="#d9d9d9" stroke-width="2" />
<rect data-id="k" x="575" y="175" width="150" height="150" fill="#231f20" />
{% endframe %}
