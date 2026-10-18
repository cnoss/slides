---
title: Farbe zum Akzentuieren
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Eine einzige Farbe in einer sonst unbunten Fläche springt sofort ins Auge (Pop-out, präattentive Wahrnehmung). Das funktioniert nur, solange die Akzentfarbe selten ist. Wer alles einfärbt, akzentuiert nichts mehr (Prinzip Sparsam hervorheben).

  Die Beispiele aus dem Bestand stammen aus Bedienungsanleitungen: Rot zeigt das Bauteil, um das es gerade geht, der Rest bleibt grau. Ein Prinzip, das jedes Interface übernehmen kann: Die Hauptaktion bekommt die Akzentfarbe, sonst nichts.
---

{% interlude "Farbe zum Akzentuieren", "Was als einziges farbig ist, ist wichtig." %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Sechs gleichwertige Einträge"}' %}
<rect data-id="i0" x="200" y="80" width="40" height="40" rx="4" fill="#888888" />
<rect data-id="t0" x="260" y="88" width="360" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="s0" x="260" y="106" width="220" height="8" rx="0" fill="#eeeeee" />
<rect data-id="i1" x="200" y="142" width="40" height="40" rx="4" fill="#888888" />
<rect data-id="t1" x="260" y="150" width="360" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="s1" x="260" y="168" width="220" height="8" rx="0" fill="#eeeeee" />
<rect data-id="i2" x="200" y="204" width="40" height="40" rx="4" fill="#888888" />
<rect data-id="t2" x="260" y="212" width="360" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="s2" x="260" y="230" width="220" height="8" rx="0" fill="#eeeeee" />
<rect data-id="i3" x="200" y="266" width="40" height="40" rx="4" fill="#888888" />
<rect data-id="t3" x="260" y="274" width="320" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="s3" x="260" y="292" width="220" height="8" rx="0" fill="#eeeeee" />
<rect data-id="i4" x="200" y="328" width="40" height="40" rx="4" fill="#888888" />
<rect data-id="t4" x="260" y="336" width="360" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="s4" x="260" y="354" width="220" height="8" rx="0" fill="#eeeeee" />
<rect data-id="i5" x="200" y="390" width="40" height="40" rx="4" fill="#888888" />
<rect data-id="t5" x="260" y="398" width="360" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="s5" x="260" y="416" width="220" height="8" rx="0" fill="#eeeeee" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Eine Farbe, ein Fokus"}' %}
<rect data-id="i0" x="200" y="80" width="40" height="40" rx="4" fill="#888888" />
<rect data-id="t0" x="260" y="88" width="360" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="s0" x="260" y="106" width="220" height="8" rx="0" fill="#eeeeee" />
<rect data-id="i1" x="200" y="142" width="40" height="40" rx="4" fill="#888888" />
<rect data-id="t1" x="260" y="150" width="360" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="s1" x="260" y="168" width="220" height="8" rx="0" fill="#eeeeee" />
<rect data-id="i2" x="200" y="204" width="40" height="40" rx="4" fill="#888888" />
<rect data-id="t2" x="260" y="212" width="360" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="s2" x="260" y="230" width="220" height="8" rx="0" fill="#eeeeee" />
<rect data-id="i3" x="200" y="266" width="40" height="40" rx="4" fill="#9313ce" />
<rect data-id="t3" x="260" y="274" width="320" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="s3" x="260" y="292" width="220" height="8" rx="0" fill="#eeeeee" />
<rect data-id="i4" x="200" y="328" width="40" height="40" rx="4" fill="#888888" />
<rect data-id="t4" x="260" y="336" width="360" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="s4" x="260" y="354" width="220" height="8" rx="0" fill="#eeeeee" />
<rect data-id="i5" x="200" y="390" width="40" height="40" rx="4" fill="#888888" />
<rect data-id="t5" x="260" y="398" width="360" height="12" rx="0" fill="#d9d9d9" />
<rect data-id="s5" x="260" y="416" width="220" height="8" rx="0" fill="#eeeeee" />
{% endframe %}
{% screenshot "./images/akzentuieren-02.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Rot zeigt das Bauteil, um das es geht<br><small>Bedienungsanleitung, aus dem Bestand</small>"}' %}
{% screenshot "./images/akzentuieren-03.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Blau zeigt den Handgriff<br><small>Bedienungsanleitung, aus dem Bestand</small>"}' %}
