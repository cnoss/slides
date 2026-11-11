---
title: "Erst die Reihenfolge"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  Bevor es eine Form gibt, gibt es eine Rangfolge. Was ist das Wichtigste auf dieser Karte, was kommt danach?

  Auf dem Smartphone wird das zur harten Entscheidung: Es gibt nur eine Spalte, alles steht untereinander. Die Reihenfolge auf dem kleinen Screen ist die ehrlichste Antwort auf die Frage nach der Priorität. Deshalb Mobile first: erst den kleinsten Screen gestalten, dann den Platz auf großen Screens nutzen.

  Die erste Fassung folgt der Gewohnheit: Bild oben, dann Titel. Die zweite folgt der Priorität einer Nachrichtenkarte: Titel und Datum zuerst, das Bild darf warten. Beides kann richtig sein. Entscheidend ist, dass die Reihenfolge eine Entscheidung ist.

  **Hintergrund**

  Mobile first geht auf Luke Wroblewski zurück (Buch »Mobile First«, 2011). Im Code steckt dieselbe Idee: Die Reihenfolge im HTML ist die Reihenfolge, in der Screenreader vorlesen und in der das Layout auf dem kleinsten Screen erscheint. Mit CSS Grid lässt sich die Anordnung auf großen Screens ändern, die Lesereihenfolge sollte trotzdem sinnvoll bleiben.
---

{% interlude "Erst die Reihenfolge, dann die Form.", "Was ist das Wichtigste?" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Rangfolge einer Nachrichtenkarte</h1>
    {% fragment '<p class="list"><strong>1.</strong> Titel</p>' %}
    {% fragment '<p class="list"><strong>2.</strong> Datum</p>' %}
    {% fragment '<p class="list"><strong>3.</strong> Teaser</p>' %}
    {% fragment '<p class="list"><strong>4.</strong> Bild</p>' %}
    {% fragment '<p class="list"><strong>5.</strong> Weiterlesen</p>' %}
  </div>
</section>

{% frame '{"w":450,"h":900,"bu":"Aus Gewohnheit: Bild zuerst"}' %}
  <rect data-id="bild" x="40" y="60" width="370" height="200" fill="#c4c4c4" />
  <rect data-id="datum" x="40" y="296" width="180" height="14" fill="#d9d9d9" />
  <rect data-id="titel" x="40" y="332" width="370" height="40" fill="#888888" />
  <rect data-id="text" x="40" y="394" width="370" height="70" fill="#d9d9d9" />
  <rect data-id="link" x="40" y="500" width="160" height="40" fill="#9313ce" rx="20" />
{% endframe %}
{% frame '{"w":450,"h":900,"bu":"Nach Priorität: Titel und Datum zuerst"}' %}
  <rect data-id="titel" x="40" y="60" width="370" height="40" fill="#888888" />
  <rect data-id="datum" x="40" y="122" width="180" height="14" fill="#d9d9d9" />
  <rect data-id="text" x="40" y="158" width="370" height="70" fill="#d9d9d9" />
  <rect data-id="bild" x="40" y="264" width="370" height="200" fill="#c4c4c4" />
  <rect data-id="link" x="40" y="500" width="160" height="40" fill="#9313ce" rx="20" />
{% endframe %}
