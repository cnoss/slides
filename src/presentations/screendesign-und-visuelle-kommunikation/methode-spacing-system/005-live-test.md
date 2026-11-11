---
title: "Live-Test"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  **Live-Test (ca. 3 Minuten).** Zwei Cards mit denselben Elementen: Bild, Kategorie, Titel, Teaser, Link. Frage: Welche wirkt ruhiger, ordentlicher, »fertiger«? Handzeichen links oder rechts. Erfahrungsgemäß gewinnt rechts deutlich, aber kaum jemand kann sagen, warum.

  Dann die Auflösung: Die Maße erscheinen. Links wurde nach Augenmaß gesetzt: 13, 17, 22, 27 Pixel, jeder Abstand ist anders, und keiner hat einen Grund. Rechts stammen alle Abstände aus einer Skala: 8, 16, 24, 32. Und sie folgen einer Regel: Was zusammengehört (Kategorie und Titel), steht enger als das, was trennt.

  Das ist das Problem, das die Methode löst: Abstände nach Augenmaß sind fast nie falsch genug, dass es jemand bemerkt, aber zusammen ergeben sie Unruhe. Und spätestens im Team oder im Code weiß niemand mehr, welcher Wert gilt.
---

{% interlude "Welche Card wirkt ruhiger?", "Links oder rechts? Entscheiden Sie aus dem Bauch." %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Links oder rechts?"}' %}
<rect data-id="a-karte" x="110.0" y="60.0" width="300.0" height="343.0" fill="#e4e4e4" />
<rect data-id="a-bild" x="110.0" y="60.0" width="300.0" height="150.0" fill="#c4c4c4" />
<rect data-id="a-kat" x="123.0" y="232.0" width="70.0" height="8.0" fill="#888888" />
<rect data-id="a-t1" x="123.0" y="249.0" width="276.0" height="16.0" fill="#888888" />
<rect data-id="a-t2" x="123.0" y="273.0" width="171.1" height="16.0" fill="#888888" />
<rect data-id="a-e0" x="123.0" y="308.0" width="276.0" height="9.0" fill="#aaaaaa" />
<rect data-id="a-e1" x="123.0" y="324.0" width="276.0" height="9.0" fill="#aaaaaa" />
<rect data-id="a-e2" x="123.0" y="340.0" width="193.2" height="9.0" fill="#aaaaaa" />
<rect data-id="a-link" x="123.0" y="376.0" width="64.0" height="10.0" fill="#231f20" />
<path data-id="a-pfeil" d="M195.0 376.0 L200.0 381.0 L195.0 386.0" fill="none" stroke="#231f20" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
<rect data-id="b-karte" x="490.0" y="60.0" width="300.0" height="353.0" fill="#e4e4e4" />
<rect data-id="b-bild" x="490.0" y="60.0" width="300.0" height="150.0" fill="#c4c4c4" />
<rect data-id="b-kat" x="514.0" y="234.0" width="70.0" height="8.0" fill="#888888" />
<rect data-id="b-t1" x="514.0" y="250.0" width="252.0" height="16.0" fill="#888888" />
<rect data-id="b-t2" x="514.0" y="274.0" width="156.2" height="16.0" fill="#888888" />
<rect data-id="b-e0" x="514.0" y="306.0" width="252.0" height="9.0" fill="#aaaaaa" />
<rect data-id="b-e1" x="514.0" y="322.0" width="252.0" height="9.0" fill="#aaaaaa" />
<rect data-id="b-e2" x="514.0" y="338.0" width="176.4" height="9.0" fill="#aaaaaa" />
<rect data-id="b-link" x="514.0" y="371.0" width="64.0" height="10.0" fill="#231f20" />
<path data-id="b-pfeil" d="M586.0 371.0 L591.0 376.0 L586.0 381.0" fill="none" stroke="#231f20" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Links nach Augenmaß, rechts aus einer Skala"}' %}
<rect data-id="a-karte" x="110.0" y="60.0" width="300.0" height="343.0" fill="#e4e4e4" />
<rect data-id="a-bild" x="110.0" y="60.0" width="300.0" height="150.0" fill="#c4c4c4" />
<rect data-id="a-kat" x="123.0" y="232.0" width="70.0" height="8.0" fill="#888888" />
<rect data-id="a-t1" x="123.0" y="249.0" width="276.0" height="16.0" fill="#888888" />
<rect data-id="a-t2" x="123.0" y="273.0" width="171.1" height="16.0" fill="#888888" />
<rect data-id="a-e0" x="123.0" y="308.0" width="276.0" height="9.0" fill="#aaaaaa" />
<rect data-id="a-e1" x="123.0" y="324.0" width="276.0" height="9.0" fill="#aaaaaa" />
<rect data-id="a-e2" x="123.0" y="340.0" width="193.2" height="9.0" fill="#aaaaaa" />
<rect data-id="a-link" x="123.0" y="376.0" width="64.0" height="10.0" fill="#231f20" />
<path data-id="a-pfeil" d="M195.0 376.0 L200.0 381.0 L195.0 386.0" fill="none" stroke="#231f20" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
<line data-id="a-ma" x1="96.0" y1="210.0" x2="96.0" y2="232.0" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
<text data-id="a-mta" x="88.0" y="226.0" text-anchor="end" font-family="sans-serif" font-size="15" font-weight="600" fill="#9313ce">22</text>
<line data-id="a-mb" x1="96.0" y1="240.0" x2="96.0" y2="249.0" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
<text data-id="a-mtb" x="88.0" y="249.5" text-anchor="end" font-family="sans-serif" font-size="15" font-weight="600" fill="#9313ce">9</text>
<line data-id="a-mc" x1="96.0" y1="289.0" x2="96.0" y2="308.0" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
<text data-id="a-mtc" x="88.0" y="303.5" text-anchor="end" font-family="sans-serif" font-size="15" font-weight="600" fill="#9313ce">19</text>
<line data-id="a-md" x1="96.0" y1="349.0" x2="96.0" y2="376.0" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
<text data-id="a-mtd" x="88.0" y="367.5" text-anchor="end" font-family="sans-serif" font-size="15" font-weight="600" fill="#9313ce">27</text>
<line data-id="a-mu" x1="96.0" y1="386.0" x2="96.0" y2="403.0" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
<text data-id="a-mtu" x="88.0" y="399.5" text-anchor="end" font-family="sans-serif" font-size="15" font-weight="600" fill="#9313ce">17</text>
<line data-id="a-ml" x1="110.0" y1="226.0" x2="123.0" y2="226.0" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
<text data-id="a-mtl" x="113.0" y="220.0" font-family="sans-serif" font-size="15" font-weight="600" fill="#9313ce">13</text>
<rect data-id="b-karte" x="490.0" y="60.0" width="300.0" height="353.0" fill="#e4e4e4" />
<rect data-id="b-bild" x="490.0" y="60.0" width="300.0" height="150.0" fill="#c4c4c4" />
<rect data-id="b-kat" x="514.0" y="234.0" width="70.0" height="8.0" fill="#888888" />
<rect data-id="b-t1" x="514.0" y="250.0" width="252.0" height="16.0" fill="#888888" />
<rect data-id="b-t2" x="514.0" y="274.0" width="156.2" height="16.0" fill="#888888" />
<rect data-id="b-e0" x="514.0" y="306.0" width="252.0" height="9.0" fill="#aaaaaa" />
<rect data-id="b-e1" x="514.0" y="322.0" width="252.0" height="9.0" fill="#aaaaaa" />
<rect data-id="b-e2" x="514.0" y="338.0" width="176.4" height="9.0" fill="#aaaaaa" />
<rect data-id="b-link" x="514.0" y="371.0" width="64.0" height="10.0" fill="#231f20" />
<path data-id="b-pfeil" d="M586.0 371.0 L591.0 376.0 L586.0 381.0" fill="none" stroke="#231f20" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
<line data-id="b-ma" x1="804.0" y1="210.0" x2="804.0" y2="234.0" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
<text data-id="b-mta" x="812.0" y="227.0" text-anchor="start" font-family="sans-serif" font-size="15" font-weight="600" fill="#9313ce">24</text>
<line data-id="b-mb" x1="804.0" y1="242.0" x2="804.0" y2="250.0" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
<text data-id="b-mtb" x="812.0" y="251.0" text-anchor="start" font-family="sans-serif" font-size="15" font-weight="600" fill="#9313ce">8</text>
<line data-id="b-mc" x1="804.0" y1="290.0" x2="804.0" y2="306.0" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
<text data-id="b-mtc" x="812.0" y="303.0" text-anchor="start" font-family="sans-serif" font-size="15" font-weight="600" fill="#9313ce">16</text>
<line data-id="b-md" x1="804.0" y1="347.0" x2="804.0" y2="371.0" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
<text data-id="b-mtd" x="812.0" y="364.0" text-anchor="start" font-family="sans-serif" font-size="15" font-weight="600" fill="#9313ce">24</text>
<line data-id="b-mu" x1="804.0" y1="381.0" x2="804.0" y2="413.0" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
<text data-id="b-mtu" x="812.0" y="402.0" text-anchor="start" font-family="sans-serif" font-size="15" font-weight="600" fill="#9313ce">32</text>
<line data-id="b-ml" x1="490.0" y1="228.0" x2="514.0" y2="228.0" stroke="#9313ce" stroke-width="3" stroke-linecap="round" />
<text data-id="b-mtl" x="493.0" y="222.0" font-family="sans-serif" font-size="15" font-weight="600" fill="#9313ce">24</text>
{% endframe %}

{% statement "Gleiche Elemente, andere Abstände.", "Abstände nach Augenmaß sind einzeln kaum falsch. Zusammen ergeben sie Unruhe, und niemand kann sie begründen." %}
