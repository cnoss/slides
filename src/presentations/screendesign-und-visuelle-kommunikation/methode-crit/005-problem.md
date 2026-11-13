---
title: "Drei Rückmeldungen"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  **Einstieg als Zuordnungsfrage (ca. 3 Minuten).** Ein Entwurf, eine Startseite als Wireframe. Gedacht ist sie, damit sich Besucherinnen und Besucher für eine Veranstaltung anmelden. Dann drei Rückmeldungen zum selben Entwurf, nacheinander eingeblendet. Fragen: Welche hilft dem Entwurf weiter? Und was unterscheidet die drei?

  Auflösung:

  - **A** ist eine **Reaktion**. Sie sagt etwas über die Person, die sie gibt, nichts über den Entwurf. Man weiß danach nicht, was zu tun ist.
  - **B** ist eine **Anweisung**. Sie schreibt eine Lösung vor, ohne das Problem zu nennen. Vielleicht ist die Lösung gut, vielleicht nicht, prüfen kann man es nicht. Und Rot bringt neue Probleme mit.
  - **C** ist **Kritik**. Sie nennt das Ziel, beobachtet ein Element und erklärt, warum es dem Ziel im Weg steht. Die Lösung bleibt bei denen, die gestalten.

  **Hintergrund**

  Die Unterscheidung stammt von Adam Connor und Aaron Irizarry, »Discussing Design. Improving Communication and Collaboration through Critique« (O'Reilly, 2015). Sie unterscheiden reaktionsbasiertes Feedback (reaction-based), anweisungsbasiertes Feedback (direction-based) und Kritik (critique). Nur Kritik analysiert einen Entwurf gegen seine Ziele. Passt zur Haltung »Gefällt mir ist kein Argument« (siehe Beobachten und Begründen).
---

{% interlude "Welche Rückmeldung hilft?", "Ein Entwurf, drei Sätze" %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "animate":false, "bu":"Ein Entwurf: Die Startseite soll zur Anmeldung führen"}' %}
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
{% endframe %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Drei Rückmeldungen zum selben Entwurf</h1>
    {% fragment '<p class="list"><strong>A:</strong> »Irgendwie gefällt mir das nicht so.«</p>' %}
    {% fragment '<p class="list"><strong>B:</strong> »Mach den Button größer und rot.«</p>' %}
    {% fragment '<p class="list"><strong>C:</strong> »Die Seite soll zur Anmeldung führen. Der Button ist aber so grau wie der Fließtext, er geht unter.«</p>' %}
  </div>
</section>

{% statement "Reaktion, Anweisung, Kritik.", "A sagt etwas über die Person, B schreibt eine Lösung vor. Nur C misst den Entwurf an seinem Ziel. Das ist eine Crit: Kritik mit Ziel, Ablauf und gemeinsamem Vokabular." %}
