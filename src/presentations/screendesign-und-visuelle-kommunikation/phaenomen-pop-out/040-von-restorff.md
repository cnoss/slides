---
title: "Das Andere bleibt hängen"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Live-Test (ca. 3 Minuten)**

  Die Liste erscheint beim Weiterschalten für fünf Sekunden und verschwindet von selbst. Danach 30 Sekunden: Alle schreiben auf, welche Wörter sie noch wissen. Dann per Handzeichen abfragen, Wort für Wort. Meist nennen die meisten das lila Wort »Spiegel«, obwohl es mitten in der Liste steht. Häufig sind auch das erste und das letzte Wort dabei (Serial-Position-Effekt).

  Eine Demo im Hörsaal ist kein Experiment: kleine Gruppe, alle sehen die Pointe kommen. Aber der Effekt ist robust und gut belegt.

  **Hintergrund**

  Hedwig von Restorff, »Über die Wirkung von Bereichsbildungen im Spurenfeld«, Psychologische Forschung 18, 1933, entstanden am Berliner Psychologischen Institut im Umfeld von Wolfgang Köhler, also mitten in der Gestaltpsychologie. Ein Element, das sich von den anderen abhebt, wird besser erinnert (Isolationseffekt). Yablonski, Laws of UX: »Von Restorff Effect«.
---

<section class="simple" data-transition="none">
  <div>
    <h1>Merken Sie sich so viele Wörter wie möglich.</h1>
    <p>Sie haben fünf Sekunden.</p>
    <div class="fragment wortliste" style="--dauer:5s;"><div style="display:block;width:8em !important;hyphens:none;white-space:nowrap;margin:0;padding:0;font-size:4vh;line-height:1.25;text-align:left;"><div style="margin:0;padding:0.15em 0;">Tisch</div><div style="margin:0;padding:0.15em 0;">Lampe</div><div style="margin:0;padding:0.15em 0;">Fenster</div><div style="margin:0;padding:0.15em 0;">Teppich</div><div style="margin:0;padding:0.15em 0;">Regal</div><div style="margin:0;padding:0.15em 0;">Kissen</div><div style="margin:0;padding:0.15em 0;color:#9313ce;font-weight:700;">Spiegel</div><div style="margin:0;padding:0.15em 0;">Sessel</div><div style="margin:0;padding:0.15em 0;">Vorhang</div><div style="margin:0;padding:0.15em 0;">Schrank</div></div></div>
    <style>
.reveal .slides section .fragment.wortliste{opacity:0;visibility:inherit;transition:none;transform:none;position:fixed;inset:0;width:100% !important;max-width:none !important;margin:0;padding:0;display:flex;align-items:center;justify-content:center;background:#ffffff;pointer-events:none;}
.reveal .slides section .fragment.wortliste.visible{opacity:0;animation:wortliste-zeigen var(--dauer,5s) linear 1;}
@keyframes wortliste-zeigen{from{opacity:1}to{opacity:1}}
    </style>
  </div>
</section>

{% question "Welche Wörter wissen Sie noch?", "Schreiben Sie sie auf. 30 Sekunden." %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Die Liste</h1>
    <div style="margin:0;padding:0;font-size:3.2vh;line-height:1.2;text-align:left;columns:2;"><div style="margin:0;padding:0.15em 0;">Tisch</div><div style="margin:0;padding:0.15em 0;">Lampe</div><div style="margin:0;padding:0.15em 0;">Fenster</div><div style="margin:0;padding:0.15em 0;">Teppich</div><div style="margin:0;padding:0.15em 0;">Regal</div><div style="margin:0;padding:0.15em 0;">Kissen</div><div style="margin:0;padding:0.15em 0;color:#9313ce;font-weight:700;">Spiegel</div><div style="margin:0;padding:0.15em 0;">Sessel</div><div style="margin:0;padding:0.15em 0;">Vorhang</div><div style="margin:0;padding:0.15em 0;">Schrank</div></div>
  </div>
</section>

{% statement "Das Andere bleibt hängen.", "Was sich abhebt, wird nicht nur schneller gefunden, sondern auch besser erinnert." %}
