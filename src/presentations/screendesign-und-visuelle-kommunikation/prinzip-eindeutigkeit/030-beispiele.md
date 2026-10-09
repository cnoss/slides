---
title: Konkrete Beispiele
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  Erst die zwei bekannten Beispiele, dann drei aus dem Interface. Bei jedem zuerst fragen: Was stört? Ist das Absicht oder Zufall?

  **Kanten:** Acht Elemente eines Artikels, fast linksbündig, aber jedes um ein paar Pixel versetzt. Niemand würde es so planen, aber genau so entsteht es, wenn Abstände nach Augenmaß gesetzt werden. Danach: eine gemeinsame Kante.

  **Größen:** Drei Kacheln, fast gleich groß. Ist die erste wichtiger? Eindeutig wird es auf zwei Wegen: alle gleich groß oder die erste deutlich größer und hervorgehoben. Merksatz: Gleich oder deutlich anders, nie fast gleich.

  **Grautöne:** Zwei Buttons in fast gleichem Grau. Ist der rechte deaktiviert? Ist der linke wichtiger? Eindeutig wird es, wenn sich die Buttons klar unterscheiden: gefüllt für die Hauptaktion, nur Kontur für die zweite.

  **Hintergrund**

  Das Prinzip »gleich oder deutlich anders« findet sich in vielen Gestaltungslehren. Bei Wathan und Schoger (Refactoring UI) etwa als Rat, Abstände und Größen aus einer festen Skala zu wählen, deren Stufen sich deutlich unterscheiden. Methoden dazu: Spacing-System, Typografische Skala, Gestaltungsraster.
---

{% interlude "Konkrete Beispiele" %}
{% screenshot "./images/030-eindeutigkeit.002.jpeg", '{"classes":"no-shadow", "bu":"Fast gleich ist schlechter als gleich oder deutlich anders"}' %}
{% screenshot "./images/030-eindeutigkeit.003.jpeg", '{"classes":"no-shadow", "bu":"Eine gemeinsame Kante oder viele fast gleiche?"}' %}

{% frame '{"bu":"Kanten: fast bündig. Absicht oder Versehen?"}' %}
<rect data-id="k0" x="120" y="90" width="260" height="26" fill="#231f20" />
<rect data-id="k1" x="126" y="144" width="360" height="12" fill="#d9d9d9" />
<rect data-id="k2" x="120" y="170" width="330" height="12" fill="#d9d9d9" />
<rect data-id="k3" x="115" y="196" width="350" height="12" fill="#d9d9d9" />
<rect data-id="k4" x="129" y="222" width="360" height="140" fill="#d9d9d9" />
<rect data-id="k5" x="123" y="390" width="200" height="18" fill="#888888" />
<rect data-id="k6" x="120" y="436" width="340" height="12" fill="#d9d9d9" />
<rect data-id="k7" x="116" y="462" width="300" height="12" fill="#d9d9d9" />
<rect data-id="kb" x="127" y="504" width="140" height="40" rx="20" fill="#9313ce" />
{% endframe %}
{% frame '{"bu":"Eine gemeinsame Kante: eindeutig"}' %}
<rect data-id="k0" x="120" y="90" width="260" height="26" fill="#231f20" />
<rect data-id="k1" x="120" y="144" width="360" height="12" fill="#d9d9d9" />
<rect data-id="k2" x="120" y="170" width="330" height="12" fill="#d9d9d9" />
<rect data-id="k3" x="120" y="196" width="350" height="12" fill="#d9d9d9" />
<rect data-id="k4" x="120" y="222" width="360" height="140" fill="#d9d9d9" />
<rect data-id="k5" x="120" y="390" width="200" height="18" fill="#888888" />
<rect data-id="k6" x="120" y="436" width="340" height="12" fill="#d9d9d9" />
<rect data-id="k7" x="120" y="462" width="300" height="12" fill="#d9d9d9" />
<rect data-id="kb" x="120" y="504" width="140" height="40" rx="20" fill="#9313ce" />
{% endframe %}

{% frame '{"bu":"Größen: fast gleich. Ist die erste wichtiger?"}' %}
<rect data-id="t0" x="40.0" y="217.5" width="165" height="165" fill="#d9d9d9" />
<rect data-id="tl0" x="40.0" y="398.5" width="115" height="12" fill="#888888" />
<rect data-id="t1" x="225.0" y="222.5" width="155" height="155" fill="#d9d9d9" />
<rect data-id="tl1" x="225.0" y="393.5" width="108" height="12" fill="#888888" />
<rect data-id="t2" x="400.0" y="220.0" width="160" height="160" fill="#d9d9d9" />
<rect data-id="tl2" x="400.0" y="396.0" width="112" height="12" fill="#888888" />
{% endframe %}
{% frame '{"bu":"Eindeutig gleich"}' %}
<rect data-id="t0" x="47.5" y="222.5" width="155" height="155" fill="#d9d9d9" />
<rect data-id="tl0" x="47.5" y="393.5" width="108" height="12" fill="#888888" />
<rect data-id="t1" x="222.5" y="222.5" width="155" height="155" fill="#d9d9d9" />
<rect data-id="tl1" x="222.5" y="393.5" width="108" height="12" fill="#888888" />
<rect data-id="t2" x="397.5" y="222.5" width="155" height="155" fill="#d9d9d9" />
<rect data-id="tl2" x="397.5" y="393.5" width="108" height="12" fill="#888888" />
{% endframe %}
{% frame '{"bu":"Oder eindeutig anders"}' %}
<rect data-id="t0" x="35.0" y="175.0" width="250" height="250" fill="#9313ce" />
<rect data-id="tl0" x="35.0" y="441.0" width="175" height="12" fill="#888888" />
<rect data-id="t1" x="305.0" y="240.0" width="120" height="120" fill="#d9d9d9" />
<rect data-id="tl1" x="305.0" y="376.0" width="84" height="12" fill="#888888" />
<rect data-id="t2" x="445.0" y="240.0" width="120" height="120" fill="#d9d9d9" />
<rect data-id="tl2" x="445.0" y="376.0" width="84" height="12" fill="#888888" />
{% endframe %}

{% frame '{"bu":"Grautöne: fast gleich. Ist der rechte Button deaktiviert?"}' %}
<rect data-id="hd" x="110" y="150" width="300" height="26" fill="#231f20" />
<rect data-id="p0" x="110" y="200" width="380" height="12" fill="#d9d9d9" />
<rect data-id="p1" x="110" y="226" width="320" height="12" fill="#d9d9d9" />
<rect data-id="b1" x="110" y="330" width="170" height="52" rx="26" fill="#7a7a7a" />
<rect data-id="b2" x="300" y="330" width="170" height="52" rx="26" fill="#8c8c8c" />
{% endframe %}
{% frame '{"bu":"Eindeutig: Hauptaktion gefüllt, zweite Aktion nur als Kontur"}' %}
<rect data-id="hd" x="110" y="150" width="300" height="26" fill="#231f20" />
<rect data-id="p0" x="110" y="200" width="380" height="12" fill="#d9d9d9" />
<rect data-id="p1" x="110" y="226" width="320" height="12" fill="#d9d9d9" />
<rect data-id="b1" x="110" y="330" width="170" height="52" rx="26" fill="#231f20" />
<rect data-id="b2" x="300" y="331" width="168" height="50" rx="25" fill="#ffffff" stroke="#888888" stroke-width="2" />
{% endframe %}
