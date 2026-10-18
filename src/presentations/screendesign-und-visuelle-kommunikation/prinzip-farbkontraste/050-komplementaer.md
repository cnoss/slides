---
title: Komplementärkontrast
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Farben, die sich im Farbkreis gegenüberliegen: Gelb und Violett, Orange und Blau, Rot und Grün. Nebeneinander steigern sie sich gegenseitig zur höchsten Leuchtkraft. Gemischt ergeben sie Grau.

  Vorsicht: Haben die beiden Farben dieselbe Helligkeit, flimmern sie (siehe Phänomen »Wenn Farbe stört«). Rot und Grün sind außerdem das Paar, das Menschen mit Rot-Grün-Sehschwäche nicht unterscheiden können, rund acht Prozent der Männer.

  Beispiel aus dem Bestand: wodniack.dev, die Portfolioseite des Entwicklers Wodniack, in einer früheren Fassung. Der Screenshot ist älter als zwei Jahre, bei Gelegenheit ersetzen.
---

{% interlude "Komplementärkontrast" %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Gelb und Violett, Orange und Blau: Gegenüber im Farbkreis"}' %}
<rect data-id="a1" x="50" y="80" width="190" height="340" fill="#f7d117" />
<rect data-id="b1" x="240" y="80" width="190" height="340" fill="#6a2fc2" />
<rect data-id="a2" x="470" y="80" width="190" height="340" fill="#ff7a00" />
<rect data-id="b2" x="660" y="80" width="190" height="340" fill="#1f4fd8" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Ineinander gesetzt steigern sie sich zur höchsten Leuchtkraft"}' %}
<rect data-id="a1" x="50" y="80" width="380" height="340" fill="#6a2fc2" />
<rect data-id="b1" x="165" y="195" width="150" height="110" fill="#f7d117" />
<rect data-id="a2" x="470" y="80" width="380" height="340" fill="#1f4fd8" />
<rect data-id="b2" x="585" y="195" width="150" height="110" fill="#ff7a00" />
{% endframe %}
{% screenshot "./images/komplementaer-kontrast-05.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Komplementärkontrast im Screen<br><small>wodniack.dev, Screenshot aus dem Bestand</small>"}' %}
