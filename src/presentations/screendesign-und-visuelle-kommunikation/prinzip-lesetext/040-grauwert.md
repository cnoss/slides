---
title: "Grauwert"
layout: presentation.11ty.js
slideClasses: wrap
transition: none
status: ok
speaker: |
  Kneifen Sie die Augen zusammen: Ein guter Textblock wirkt wie eine gleichmäßig graue Fläche. Das ist der Grauwert. Löcher, dunkle Flecken und helle Streifen stören den Lesefluss, auch wenn man sie beim Lesen nicht bewusst wahrnimmt.

  Links und rechts: derselbe Text. Links mit Blocksatz ohne Trennung, gesperrten und fetten Wörtern, rechts ruhig gesetzt. Unscharf sieht man den Unterschied sofort. Das ist derselbe Trick wie beim Unschärfetest.

  Was den Grauwert stört: gesperrter Text, zu viele Auszeichnungen im Absatz, erzwungener Blocksatz ohne Silbentrennung. Dazu mehr bei Satz.

  Die Reihenfolge der Abstände: Buchstabenabstand kleiner als Wortabstand, kleiner als Zeilenabstand, kleiner als Absatzabstand. Wird diese Reihenfolge verletzt, zerfällt der Text.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Zweimal derselbe Text</h1>
    <div style="display:flex;gap:5vw;align-items:flex-start;width:100%;"><p lang="de" style="flex:1;font-family:PTserif;font-size:3vh;line-height:1.45;margin:0;hyphens:none;text-align:justify;">Beim <span style="font-weight:700;">Lesen</span> gleiten die Augen nicht <span style="letter-spacing:.25em;">gleichmäßig</span> über die Zeile. Sie <span style="font-weight:700;">springen von Punkt zu Punkt</span> und ergänzen den Rest aus dem Zusammenhang. Am <span style="letter-spacing:.25em;">Zeilenende</span> müssen sie zurück an den <span style="font-weight:700;">Anfang</span> der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang <span style="letter-spacing:.25em;">schlecht</span> wieder.</p><p lang="de" style="flex:1;font-family:PTserif;font-size:3vh;line-height:1.45;margin:0;hyphens:none;text-align:left;">Beim Lesen gleiten die Augen nicht gleichmäßig über die Zeile. Sie springen von Punkt zu Punkt und ergänzen den Rest aus dem Zusammenhang. Am Zeilenende müssen sie zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang schlecht wieder.</p></div>
  </div>
</section>

<section class="simple" data-transition="none">
  <div>
    <h1>Unscharf sieht man es</h1>
    <div style="display:flex;gap:5vw;align-items:flex-start;width:100%;"><p lang="de" style="flex:1;font-family:PTserif;font-size:3vh;line-height:1.45;margin:0;hyphens:none;text-align:justify;filter:blur(0.35vw);">Beim <span style="font-weight:700;">Lesen</span> gleiten die Augen nicht <span style="letter-spacing:.25em;">gleichmäßig</span> über die Zeile. Sie <span style="font-weight:700;">springen von Punkt zu Punkt</span> und ergänzen den Rest aus dem Zusammenhang. Am <span style="letter-spacing:.25em;">Zeilenende</span> müssen sie zurück an den <span style="font-weight:700;">Anfang</span> der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang <span style="letter-spacing:.25em;">schlecht</span> wieder.</p><p lang="de" style="flex:1;font-family:PTserif;font-size:3vh;line-height:1.45;margin:0;hyphens:none;text-align:left;filter:blur(0.35vw);">Beim Lesen gleiten die Augen nicht gleichmäßig über die Zeile. Sie springen von Punkt zu Punkt und ergänzen den Rest aus dem Zusammenhang. Am Zeilenende müssen sie zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang schlecht wieder.</p></div>
  </div>
</section>

{% statement "Abstände haben eine Reihenfolge.", "Buchstaben sind enger als Wörter. Wörter enger als Zeilen. Zeilen enger als Absätze." %}
