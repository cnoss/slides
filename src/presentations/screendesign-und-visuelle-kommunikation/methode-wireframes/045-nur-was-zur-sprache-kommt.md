---
title: "Nur zeigen, worüber Sie sprechen wollen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Die Unterzeile ist Watzlawicks erstes Axiom (siehe Prinzip Kommunikation): Auch was nur als Platzhalter gedacht war, sendet eine Botschaft.

  Die wichtigste Regel für jeden Prototyp, egal auf welcher Stufe: Alles, was im Entwurf zu sehen ist, wird auch besprochen. Wer ein Foto zeigt, bekommt Feedback zum Foto. Wer einen Werbetext zeigt, diskutiert den Werbetext. Wer Farbe zeigt, redet über Farbe.

  Daraus folgt: In einen Prototyp gehört nur, worüber Sie gerade sprechen wollen. Alles andere bleibt Platzhalter. Wollen Sie nicht über den Bildinhalt sprechen, zeigen Sie kein Bild, sondern eine graue Fläche. Wollen Sie nicht über den Wortlaut sprechen, zeigen Sie Balken. Wollen Sie nicht über Farbe sprechen, bleibt alles grau.

  Das gilt auch umgekehrt: Wollen Sie wissen, ob der lange Produktname in die Zeile passt, dann gehört genau dieser eine Text echt hinein, der Rest bleibt grau. Die Fidelity muss nicht überall gleich sein.

  Der Fehler passiert oft: Ein Wireframe mit einem schönen Stockfoto, und die ganze Runde redet über das Foto statt über die Anordnung.

  Vorführung: erst der Hi-Fi-Screen mit der Frage »Worüber würden Sie hier sprechen?« (Antworten: Hocker, Holz, Lila, Preis). Dann derselbe Screen als Wireframe: Jetzt bleibt nur die Anordnung. Zum Schluss der Wireframe, in dem nur der Produktname echt ist.
---

{% interlude "Nur zeigen, worüber Sie sprechen wollen.", "Man kann nicht nicht kommunizieren." %}

{% frame '{"w":900, "h":500, "bu":"Worüber würden Sie hier sprechen?"}' %}
<rect data-id="nav" x="0" y="0" width="900" height="50" fill="#ffffff" rx="0" />
<line data-id="navlinie" x1="0" y1="50" x2="900" y2="50" stroke="#e4e4e4" stroke-width="2" />
<text data-id="logo" x="40" y="32" font-family="Helvetica Neue, Arial, sans-serif" font-size="17" font-weight="700" fill="#231f20">Hocker &amp; Co.</text>
<text data-id="n0" x="560" y="31" font-family="Helvetica Neue, Arial, sans-serif" font-size="13" font-weight="400" fill="#555555">Stühle</text>
<text data-id="n1" x="630" y="31" font-family="Helvetica Neue, Arial, sans-serif" font-size="13" font-weight="400" fill="#555555">Tische</text>
<text data-id="n2" x="700" y="31" font-family="Helvetica Neue, Arial, sans-serif" font-size="13" font-weight="400" fill="#555555">Lampen</text>
<text data-id="n3" x="770" y="31" font-family="Helvetica Neue, Arial, sans-serif" font-size="13" font-weight="400" fill="#555555">Sale</text>
<circle data-id="cart" cx="860" cy="26" r="11" fill="#9313ce" />
<text data-id="bc" x="40" y="79" font-family="Helvetica Neue, Arial, sans-serif" font-size="11" font-weight="400" fill="#6a6a6a">Möbel / Hocker / Kiel</text>
<rect data-id="bild" x="40" y="96" width="400" height="264" fill="#f3eaf8" rx="0" />
<g data-id="hocker"><rect x="170" y="166" width="140" height="22" rx="6" fill="#c8a27a" /><line x1="190" y1="188" x2="175" y2="306" stroke="#8a6440" stroke-width="10" stroke-linecap="round" /><line x1="290" y1="188" x2="305" y2="306" stroke="#8a6440" stroke-width="10" stroke-linecap="round" /><line x1="240" y1="188" x2="240" y2="310" stroke="#8a6440" stroke-width="10" stroke-linecap="round" /><line x1="182" y1="256" x2="298" y2="256" stroke="#8a6440" stroke-width="6" stroke-linecap="round" /></g>
<rect data-id="th0" x="40" y="374" width="88" height="52" fill="#e4cff0" rx="0" />
<rect data-id="th1" x="144" y="374" width="88" height="52" fill="#f3eaf8" rx="0" />
<rect data-id="th2" x="248" y="374" width="88" height="52" fill="#f3eaf8" rx="0" />
<rect data-id="th3" x="352" y="374" width="88" height="52" fill="#f3eaf8" rx="0" />
<text data-id="h1" x="480" y="118" font-family="Helvetica Neue, Arial, sans-serif" font-size="24" font-weight="700" fill="#231f20">Hocker Kiel</text>
<text data-id="h2" x="480" y="146" font-family="Helvetica Neue, Arial, sans-serif" font-size="16" font-weight="400" fill="#555555">Eiche geölt, Sitzhöhe 46 cm</text>
<circle data-id="s0" cx="486" cy="168" r="6" fill="#9313ce" />
<circle data-id="s1" cx="506" cy="168" r="6" fill="#9313ce" />
<circle data-id="s2" cx="526" cy="168" r="6" fill="#9313ce" />
<circle data-id="s3" cx="546" cy="168" r="6" fill="#9313ce" />
<circle data-id="s4" cx="566" cy="168" r="6" fill="#d9d9d9" />
<text data-id="preis" x="480" y="220" font-family="Helvetica Neue, Arial, sans-serif" font-size="26" font-weight="700" fill="#231f20">249,00 €</text>
<circle data-id="f0" cx="494" cy="262" r="14" fill="#c8a27a" stroke="#9313ce" stroke-width="3" />
<circle data-id="f1" cx="534" cy="262" r="14" fill="#231f20" stroke="#d9d9d9" stroke-width="2" />
<circle data-id="f2" cx="574" cy="262" r="14" fill="#ffffff" stroke="#d9d9d9" stroke-width="2" />
<circle data-id="f3" cx="614" cy="262" r="14" fill="#8a8a8a" stroke="#d9d9d9" stroke-width="2" />
<rect data-id="menge" x="480" y="300" width="80" height="44" fill="#ffffff" rx="0" stroke="#888888" stroke-width="2" />
<text data-id="mz" x="512" y="328" font-family="Helvetica Neue, Arial, sans-serif" font-size="16" font-weight="400" fill="#231f20">1</text>
<rect data-id="btn" x="576" y="300" width="284" height="44" fill="#9313ce" rx="22" />
<text data-id="btnt" x="652" y="328" font-family="Helvetica Neue, Arial, sans-serif" font-size="16" font-weight="600" fill="#ffffff">In den Warenkorb</text>
<text data-id="t0" x="480" y="377" font-family="Helvetica Neue, Arial, sans-serif" font-size="13" font-weight="400" fill="#555555">Massivholz aus Europa, von Hand geölt.</text>
<text data-id="t1" x="480" y="397" font-family="Helvetica Neue, Arial, sans-serif" font-size="13" font-weight="400" fill="#555555">Stapelbar, belastbar bis 120 kg.</text>
<text data-id="t2" x="480" y="417" font-family="Helvetica Neue, Arial, sans-serif" font-size="13" font-weight="400" fill="#555555">Lieferung in 3 bis 5 Werktagen.</text>
{% endframe %}
{% frame '{"w":900, "h":500, "bu":"Als Wireframe: Jetzt bleibt nur die Anordnung"}' %}
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
{% frame '{"w":900, "h":500, "bu":"Nur der Produktname ist echt: Jetzt geht es um genau diesen Text"}' %}
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
<text data-id="h1" x="480" y="118" font-family="Helvetica Neue, Arial, sans-serif" font-size="24" font-weight="700" fill="#231f20">Hocker Kiel</text>
<text data-id="h2" x="480" y="146" font-family="Helvetica Neue, Arial, sans-serif" font-size="16" font-weight="400" fill="#555555">Eiche geölt, Sitzhöhe 46 cm</text>
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

<section class="simple" data-transition="fade">
  <div>
    <h1>Was nicht besprochen werden soll, bleibt Platzhalter</h1>
    {% fragment '<p class="list"><strong>Bild:</strong> Kein Gespräch über den Bildinhalt? Dann eine graue Fläche statt eines Fotos.</p>' %}
    {% fragment '<p class="list"><strong>Text:</strong> Kein Gespräch über den Wortlaut? Dann Balken statt Text.</p>' %}
    {% fragment '<p class="list"><strong>Farbe:</strong> Kein Gespräch über Farbe? Dann bleibt alles grau.</p>' %}
    {% fragment '<p class="list"><strong>Umgekehrt:</strong> Was Sie besprechen wollen, zeigen Sie echt. Auch wenn der Rest grau bleibt.</p>' %}
  </div>
</section>
