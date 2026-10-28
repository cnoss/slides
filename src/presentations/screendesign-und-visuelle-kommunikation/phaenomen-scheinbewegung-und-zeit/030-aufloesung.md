---
title: "Auflösung"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Auf dem Bildschirm hat sich nichts bewegt. Zwei Punkte gehen an und aus, sonst nichts. Die Bewegung dazwischen, die lila Bahn, gibt es nur im Kopf.

  Jeder Film funktioniert so: 24 Einzelbilder pro Sekunde, und wir sehen Bewegung. Jede Animation im Interface auch. Ein Display zeigt nie Bewegung, immer nur eine Folge stehender Bilder.
---

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Auf dem Bildschirm: zwei Punkte, die an- und ausgehen"}' %}

<circle data-id="pa" cx="330" cy="250" r="36" fill="#231f20" />
<circle data-id="pb" cx="570" cy="250" r="36" fill="#231f20" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Im Kopf: eine Bewegung, die es nicht gibt"}' %}

<path d="M 330 250 Q 450 150 570 250" fill="none" stroke="#9313ce" stroke-width="6" stroke-linecap="round" stroke-dasharray="1 18" />
<circle data-id="pa" cx="330" cy="250" r="36" fill="#231f20" />
<circle data-id="pb" cx="570" cy="250" r="36" fill="#231f20" />
{% endframe %}

{% statement "Da bewegt sich nichts.", "Jeder Film, jede Animation, jedes Scrollen: eine Folge stehender Bilder. Die Bewegung macht das Gehirn." %}
