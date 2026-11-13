---
title: "So klingt Kritik"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  So sieht das Ergebnis einer guten Rückmeldung aus: vier Teile, immer in dieser Reihenfolge. Erst das Ziel, dann was dem Ziel hilft, dann was ihm im Weg steht, jeweils mit Begründung. Zum Schluss eine Frage statt einer fertigen Lösung.

  Das Lob am Anfang ist keine Höflichkeitsfloskel. Es sagt den Gestaltenden, was sie behalten sollen. Wer nur Fehler hört, wirft im Zweifel auch das Gelungene weg.

  Am Beispiel: Die große Headline und die klare Aufteilung in Bild links, Text rechts unterstützen das Ziel. Der Button arbeitet dagegen, er hat denselben Grauwert wie der Fließtext und hebt sich nicht ab (siehe Kontrast und Hervorhebung).
---

{% interlude "So klingt Kritik", "Ziel, Stärke, Schwäche, Frage" %}

<section class="simple" data-transition="fade">
<div>

# Eine Rückmeldung in vier Teilen

{% fragment '<p class="list"><strong>Ziel:</strong> »Die Seite soll zur Anmeldung führen.«</p>' %}
{% fragment '<p class="list"><strong>Das hilft:</strong> »Die große Headline zieht den Blick sofort, Bild und Text sind klar getrennt.«</p>' %}
{% fragment '<p class="list"><strong>Das steht im Weg:</strong> »Der Button ist so grau wie der Fließtext und geht unter.«</p>' %}
{% fragment '<p class="list"><strong>Frage:</strong> »Was wäre, wenn der Button das einzige dunkle Element auf der Seite wäre?«</p>' %}

</div>
</section>

{% frame '{"stage":"#ffffff", "w":900, "h":500, "animate":false, "bu":"Das steht im Weg: Der Button hat denselben Grauwert wie der Text"}' %}
<rect data-id="nav" x="60" y="34" width="110" height="14" fill="#888888" />
<rect data-id="n0" x="560" y="37" width="55" height="8" fill="#d9d9d9" />
<rect data-id="n1" x="635" y="37" width="55" height="8" fill="#d9d9d9" />
<rect data-id="n2" x="710" y="37" width="55" height="8" fill="#d9d9d9" />
<rect data-id="n3" x="785" y="37" width="55" height="8" fill="#d9d9d9" />
<rect data-id="bild" x="60" y="80" width="430" height="230" fill="#c4c4c4" />
<rect data-id="h1" x="520" y="96" width="300" height="24" fill="#888888" />
<rect data-id="h1b" x="520" y="130" width="220" height="24" fill="#888888" />
<rect data-id="t0" x="520" y="180" width="320" height="10" fill="#d9d9d9" />
<rect data-id="t1" x="520" y="200" width="320" height="10" fill="#d9d9d9" />
<rect data-id="t2" x="520" y="220" width="300" height="10" fill="#d9d9d9" />
<rect data-id="t3" x="520" y="240" width="240" height="10" fill="#d9d9d9" />
<rect data-id="btn" x="520" y="272" width="120" height="34" rx="17" fill="#d9d9d9" />
<rect data-id="k0" x="60" y="340" width="265" height="96" fill="#e4e4e4" />
<rect data-id="kb0" x="76" y="356" width="70" height="64" fill="#c4c4c4" />
<rect data-id="kt0" x="162" y="362" width="140" height="10" fill="#aaaaaa" />
<rect data-id="ku0" x="162" y="382" width="110" height="8" fill="#aaaaaa" />
<rect data-id="k1" x="345" y="340" width="265" height="96" fill="#e4e4e4" />
<rect data-id="kb1" x="361" y="356" width="70" height="64" fill="#c4c4c4" />
<rect data-id="kt1" x="447" y="362" width="140" height="10" fill="#aaaaaa" />
<rect data-id="ku1" x="447" y="382" width="110" height="8" fill="#aaaaaa" />
<rect data-id="k2" x="630" y="340" width="265" height="96" fill="#e4e4e4" />
<rect data-id="kb2" x="646" y="356" width="70" height="64" fill="#c4c4c4" />
<rect data-id="kt2" x="732" y="362" width="140" height="10" fill="#aaaaaa" />
<rect data-id="ku2" x="732" y="382" width="110" height="8" fill="#aaaaaa" />
<rect data-id="ring" x="508" y="262" width="144" height="54" rx="27" fill="none" stroke="#9313ce" stroke-width="4" />
{% endframe %}
