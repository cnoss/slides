---
title: Stufen gegen Verlauf
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Frage: Ist jede Stufe in sich gleichmäßig grau? Die meisten sehen an jeder Kante einen helleren und einen dunkleren Saum, die Stufen wirken leicht gewölbt. Beim Weiterschalten rücken die Stufen auseinander, die Säume verschwinden: Jede Stufe ist eine einzige, gleichmäßige Fläche.

  **Hintergrund**

  Mach-Bänder, beschrieben von dem Physiker Ernst Mach (1865). Das visuelle System verstärkt Kanten: Nervenzellen in der Netzhaut hemmen ihre Nachbarn (laterale Hemmung). Das schärft Konturen, erzeugt an Helligkeitsstufen aber Säume, die es nicht gibt.

  Im Screendesign sieht man das bei abgestuften Flächen, etwa bei Farbskalen, Tabellenzeilen mit Hintergrund oder Diagrammen mit Tonwertstufen.
---

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Ist jede Stufe gleichmäßig grau?"}' %}
<rect data-id="s0" x="50" y="100" width="100" height="300" fill="#2a2a2a" />
<rect data-id="s1" x="150" y="100" width="100" height="300" fill="#444444" />
<rect data-id="s2" x="250" y="100" width="100" height="300" fill="#5e5e5e" />
<rect data-id="s3" x="350" y="100" width="100" height="300" fill="#787878" />
<rect data-id="s4" x="450" y="100" width="100" height="300" fill="#929292" />
<rect data-id="s5" x="550" y="100" width="100" height="300" fill="#acacac" />
<rect data-id="s6" x="650" y="100" width="100" height="300" fill="#c6c6c6" />
<rect data-id="s7" x="750" y="100" width="100" height="300" fill="#e0e0e0" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Mit Abstand verschwinden die Säume. Jede Stufe ist eine einzige Fläche."}' %}
<rect data-id="s0" x="38" y="100" width="88" height="300" fill="#2a2a2a" />
<rect data-id="s1" x="144" y="100" width="88" height="300" fill="#444444" />
<rect data-id="s2" x="250" y="100" width="88" height="300" fill="#5e5e5e" />
<rect data-id="s3" x="356" y="100" width="88" height="300" fill="#787878" />
<rect data-id="s4" x="462" y="100" width="88" height="300" fill="#929292" />
<rect data-id="s5" x="568" y="100" width="88" height="300" fill="#acacac" />
<rect data-id="s6" x="674" y="100" width="88" height="300" fill="#c6c6c6" />
<rect data-id="s7" x="780" y="100" width="88" height="300" fill="#e0e0e0" />
{% endframe %}
