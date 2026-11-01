---
title: "Umbrüche"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Hurenkind:** die letzte Zeile eines Absatzes allein oben auf einer neuen Seite oder Spalte. **Schusterjunge:** die erste Zeile eines Absatzes allein unten. Merksatz aus dem Bleisatz: Ein Hurenkind weiß nicht, wo es herkommt, ein Schusterjunge nicht, wo er hingeht. Die Begriffe sind alt und nicht besonders schön, Sie werden ihnen trotzdem begegnen. Auf Englisch: widow und orphan.

  Am Screen gibt es selten Seiten, das Problem verschiebt sich: Spalten und Karten haben Umbrüche, und im Fließtext steht gern ein einzelnes Wort in der letzten Zeile.

  In CSS gibt es dafür Werkzeuge: `orphans` und `widows` für Umbrüche in Spalten und beim Druck, `text-wrap: balance` für Überschriften (die Zeilen werden gleich lang) und `text-wrap: pretty` für Fließtext (kein einsames letztes Wort). Früher hat man das von Hand mit festen Umbrüchen gelöst, die dann auf dem nächsten Gerät falsch saßen.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Überschriften ausbalancieren</h1>
    <div style="display:flex;gap:4vw;align-items:flex-start;width:100%;"><div style="flex:1;"><p style="font-family:PTsans;font-size:2.6vh;color:#9313ce;margin:0 0 1vh;text-align:left;">Automatisch</p><p style="font-family:PTsans;font-weight:700;font-size:5.4vh;line-height:1.15;margin:0;text-align:left;max-width:20ch;hyphens:none;">Die Bibliothek zieht im Frühjahr in den alten Bahnhof um</p></div><div style="flex:1;"><p style="font-family:PTsans;font-size:2.6vh;color:#9313ce;margin:0 0 1vh;text-align:left;"><code>text-wrap: balance</code></p><p style="font-family:PTsans;font-weight:700;font-size:5.4vh;line-height:1.15;margin:0;text-align:left;max-width:20ch;hyphens:none;text-wrap:balance;">Die Bibliothek zieht im Frühjahr in den alten Bahnhof um</p></div></div>
  </div>
</section>

{% statement "Einsame Zeilen stören.", "Im Druck heißen sie Hurenkind und Schusterjunge. Am Screen hilft CSS: text-wrap, widows, orphans." %}
