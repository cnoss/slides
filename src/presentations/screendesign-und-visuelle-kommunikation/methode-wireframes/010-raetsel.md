---
title: "Was für eine Seite ist das?"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  **Rätsel (ca. 1 Minute):** Ein Screen ganz ohne Text, ohne Bild, ohne Farbe. Frage: Was für eine Seite ist das? Fast alle erkennen sofort eine Produktseite in einem Onlineshop. Nachfragen: Woran? Erwartbare Antworten: großes Bild links mit kleinen Vorschaubildern darunter, eine dicke dunkle Zahl (der Preis), runde Auswahlfelder (Farben oder Varianten), ein breiter Button neben einem kleinen Feld (Menge und »In den Warenkorb«).

  Die Pointe: Die Struktur allein verrät schon die Seite und ihre Rangfolge. Genau das ist ein Wireframe. Und genau deshalb lohnt es sich, über die Struktur zu entscheiden, bevor Farbe, Bilder und Schrift dazukommen.
---

{% interlude "Was für eine Seite ist das?", "Ohne Text, ohne Bild, ohne Farbe" %}

{% frame '{"w":900, "h":500, "bu":"Was für eine Seite ist das? Und woran erkennen Sie es?"}' %}
<rect data-id="nav" x="0" y="0" width="900" height="50" fill="#f2f2f2" rx="0" />
<rect data-id="logo" x="40" y="18" width="90" height="14" fill="#888888" rx="0" />
<rect data-id="n0" x="560" y="22" width="50" height="8" fill="#aaaaaa" />
<rect data-id="n1" x="630" y="22" width="50" height="8" fill="#aaaaaa" />
<rect data-id="n2" x="700" y="22" width="50" height="8" fill="#aaaaaa" />
<rect data-id="n3" x="770" y="22" width="50" height="8" fill="#aaaaaa" />
<circle data-id="cart" cx="860" cy="26" r="11" fill="#888888" />
<rect data-id="bc" x="40" y="70" width="180" height="8" fill="#aaaaaa" rx="0" />
<rect data-id="bild" x="40" y="96" width="400" height="264" fill="#c4c4c4" rx="0" />
<rect data-id="th0" x="40" y="374" width="88" height="52" fill="#d9d9d9" rx="0" />
<rect data-id="th1" x="144" y="374" width="88" height="52" fill="#d9d9d9" rx="0" />
<rect data-id="th2" x="248" y="374" width="88" height="52" fill="#d9d9d9" rx="0" />
<rect data-id="th3" x="352" y="374" width="88" height="52" fill="#d9d9d9" rx="0" />
<rect data-id="h1" x="480" y="100" width="300" height="22" fill="#888888" rx="0" />
<rect data-id="h2" x="480" y="130" width="200" height="22" fill="#888888" rx="0" />
<circle data-id="s0" cx="486" cy="168" r="6" fill="#aaaaaa" />
<circle data-id="s1" cx="506" cy="168" r="6" fill="#aaaaaa" />
<circle data-id="s2" cx="526" cy="168" r="6" fill="#aaaaaa" />
<circle data-id="s3" cx="546" cy="168" r="6" fill="#aaaaaa" />
<circle data-id="s4" cx="566" cy="168" r="6" fill="#aaaaaa" />
<rect data-id="preis" x="480" y="196" width="120" height="26" fill="#231f20" rx="0" />
<circle data-id="f0" cx="494" cy="262" r="14" fill="#d9d9d9" />
<circle data-id="f1" cx="534" cy="262" r="14" fill="#d9d9d9" />
<circle data-id="f2" cx="574" cy="262" r="14" fill="#d9d9d9" />
<circle data-id="f3" cx="614" cy="262" r="14" fill="#d9d9d9" />
<rect data-id="menge" x="480" y="300" width="80" height="44" fill="#ffffff" rx="0" stroke="#888888" stroke-width="2" />
<rect data-id="btn" x="576" y="300" width="284" height="44" fill="#231f20" rx="22" />
<rect data-id="t0" x="480" y="368" width="380" height="9" fill="#d9d9d9" rx="0" />
<rect data-id="t1" x="480" y="388" width="380" height="9" fill="#d9d9d9" rx="0" />
<rect data-id="t2" x="480" y="408" width="260" height="9" fill="#d9d9d9" rx="0" />
{% endframe %}
{% frame '{"w":900, "h":500, "bu":"Großes Bild, eine dicke Zahl, ein breiter Button: ein Produkt im Shop"}' %}
<rect data-id="nav" x="0" y="0" width="900" height="50" fill="#f2f2f2" rx="0" />
<rect data-id="logo" x="40" y="18" width="90" height="14" fill="#888888" rx="0" />
<rect data-id="n0" x="560" y="22" width="50" height="8" fill="#aaaaaa" />
<rect data-id="n1" x="630" y="22" width="50" height="8" fill="#aaaaaa" />
<rect data-id="n2" x="700" y="22" width="50" height="8" fill="#aaaaaa" />
<rect data-id="n3" x="770" y="22" width="50" height="8" fill="#aaaaaa" />
<circle data-id="cart" cx="860" cy="26" r="11" fill="#888888" />
<rect data-id="bc" x="40" y="70" width="180" height="8" fill="#aaaaaa" rx="0" />
<rect data-id="bild" x="40" y="96" width="400" height="264" fill="#c4c4c4" rx="0" />
<rect data-id="th0" x="40" y="374" width="88" height="52" fill="#d9d9d9" rx="0" />
<rect data-id="th1" x="144" y="374" width="88" height="52" fill="#d9d9d9" rx="0" />
<rect data-id="th2" x="248" y="374" width="88" height="52" fill="#d9d9d9" rx="0" />
<rect data-id="th3" x="352" y="374" width="88" height="52" fill="#d9d9d9" rx="0" />
<rect data-id="h1" x="480" y="100" width="300" height="22" fill="#888888" rx="0" />
<rect data-id="h2" x="480" y="130" width="200" height="22" fill="#888888" rx="0" />
<circle data-id="s0" cx="486" cy="168" r="6" fill="#aaaaaa" />
<circle data-id="s1" cx="506" cy="168" r="6" fill="#aaaaaa" />
<circle data-id="s2" cx="526" cy="168" r="6" fill="#aaaaaa" />
<circle data-id="s3" cx="546" cy="168" r="6" fill="#aaaaaa" />
<circle data-id="s4" cx="566" cy="168" r="6" fill="#aaaaaa" />
<rect data-id="preis" x="480" y="196" width="120" height="26" fill="#231f20" rx="0" />
<circle data-id="f0" cx="494" cy="262" r="14" fill="#d9d9d9" />
<circle data-id="f1" cx="534" cy="262" r="14" fill="#d9d9d9" />
<circle data-id="f2" cx="574" cy="262" r="14" fill="#d9d9d9" />
<circle data-id="f3" cx="614" cy="262" r="14" fill="#d9d9d9" />
<rect data-id="menge" x="480" y="300" width="80" height="44" fill="#ffffff" rx="0" stroke="#888888" stroke-width="2" />
<rect data-id="btn" x="576" y="300" width="284" height="44" fill="#231f20" rx="22" />
<rect data-id="t0" x="480" y="368" width="380" height="9" fill="#d9d9d9" rx="0" />
<rect data-id="t1" x="480" y="388" width="380" height="9" fill="#d9d9d9" rx="0" />
<rect data-id="t2" x="480" y="408" width="260" height="9" fill="#d9d9d9" rx="0" />
<rect data-id="m1" x="32" y="88" width="416" height="280" rx="10" fill="none" stroke="#9313ce" stroke-width="4" />
<rect data-id="m2" x="472" y="188" width="136" height="42" rx="10" fill="none" stroke="#9313ce" stroke-width="4" />
<rect data-id="m3" x="568" y="292" width="300" height="60" rx="10" fill="none" stroke="#9313ce" stroke-width="4" />
{% endframe %}

{% statement "Die Struktur verrät die Seite.", "Noch bevor ein Wort dasteht, wissen Sie, was das ist und was am wichtigsten ist." %}
