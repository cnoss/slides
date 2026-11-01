---
title: "Satzarten"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Linksbündig (Flattersatz):** Der Standard am Screen. Fester Zeilenanfang, gleichmäßige Wortabstände. Der rechte Rand darf unruhig sein.

  **Blocksatz ohne Silbentrennung:** Damit beide Ränder bündig werden, verteilt der Browser den Platz auf die Wortabstände. Es entstehen Löcher und »Gassen«, der Grauwert leidet. Vor allem in schmalen Spalten und auf dem Handy.

  **Blocksatz mit Silbentrennung:** `hyphens: auto` mit gesetzter Sprache im Attribut `lang` hilft viel, braucht aber genug Breite. Am Screen weiß man nie genau, wie breit die Spalte wird, deshalb bleibt es riskant.

  **Zentriert:** Jede Zeile beginnt woanders, die Augen müssen den Anfang jedes Mal suchen. Nur für Kurzes: eine Überschrift, ein Zitat, zwei bis drei Zeilen.

  **Rechtsbündig:** Nur für Ausnahmen, etwa Zahlen in Tabellen oder eine kurze Bildunterschrift.
---

<section class="simple" data-transition="fade">
  <div>
    <h1>Linksbündig gegen Blocksatz</h1>
    <div style="display:flex;gap:4vw;align-items:flex-start;width:100%;"><div style="flex:1;"><p style="font-family:PTsans;font-size:2.6vh;color:#9313ce;margin:0 0 1vh;text-align:left;">Linksbündig: gleichmäßige Wortabstände</p><p lang="de" style="font-family:PTserif;font-size:3.1vh;line-height:1.45;max-width:32ch;width:100%;margin:0;text-align:left;hyphens:none;">Beim Lesen gleiten die Augen nicht gleichmäßig über die Zeile. Sie springen von Punkt zu Punkt und ergänzen den Rest aus dem Zusammenhang. Am Zeilenende müssen sie zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang schlecht wieder. Ist sie zu kurz, reißt der Lesefluss ständig ab.</p></div><div style="flex:1;"><p style="font-family:PTsans;font-size:2.6vh;color:#9313ce;margin:0 0 1vh;text-align:left;">Blocksatz ohne Trennung: Löcher</p><p lang="de" style="font-family:PTserif;font-size:3.1vh;line-height:1.45;max-width:32ch;width:100%;margin:0;text-align:justify;hyphens:none;">Beim Lesen gleiten die Augen nicht gleichmäßig über die Zeile. Sie springen von Punkt zu Punkt und ergänzen den Rest aus dem Zusammenhang. Am Zeilenende müssen sie zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang schlecht wieder. Ist sie zu kurz, reißt der Lesefluss ständig ab.</p></div></div>
  </div>
</section>

<section class="simple" data-transition="none">
  <div>
    <h1>Silbentrennung hilft</h1>
    <div style="display:flex;gap:4vw;align-items:flex-start;width:100%;"><div style="flex:1;"><p style="font-family:PTsans;font-size:2.6vh;color:#9313ce;margin:0 0 1vh;text-align:left;">Blocksatz ohne Trennung</p><p lang="de" style="font-family:PTserif;font-size:3.1vh;line-height:1.45;max-width:32ch;width:100%;margin:0;text-align:justify;hyphens:none;">Beim Lesen gleiten die Augen nicht gleichmäßig über die Zeile. Sie springen von Punkt zu Punkt und ergänzen den Rest aus dem Zusammenhang. Am Zeilenende müssen sie zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang schlecht wieder. Ist sie zu kurz, reißt der Lesefluss ständig ab.</p></div><div style="flex:1;"><p style="font-family:PTsans;font-size:2.6vh;color:#9313ce;margin:0 0 1vh;text-align:left;">Blocksatz mit <code>hyphens: auto</code></p><p lang="de" style="font-family:PTserif;font-size:3.1vh;line-height:1.45;max-width:32ch;width:100%;margin:0;text-align:justify;hyphens:auto;">Beim Lesen gleiten die Augen nicht gleichmäßig über die Zeile. Sie springen von Punkt zu Punkt und ergänzen den Rest aus dem Zusammenhang. Am Zeilenende müssen sie zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang schlecht wieder. Ist sie zu kurz, reißt der Lesefluss ständig ab.</p></div></div>
  </div>
</section>

<section class="simple" data-transition="none">
  <div>
    <h1>Zentriert: nur für Kurzes</h1>
    <div style="display:flex;gap:4vw;align-items:flex-start;width:100%;"><div style="flex:1;"><p style="font-family:PTsans;font-size:2.6vh;color:#9313ce;margin:0 0 1vh;text-align:left;">Langer Text: Der Zeilenanfang fehlt</p><p lang="de" style="font-family:PTserif;font-size:3.1vh;line-height:1.45;max-width:32ch;width:100%;margin:0;text-align:center;hyphens:none;">Beim Lesen gleiten die Augen nicht gleichmäßig über die Zeile. Sie springen von Punkt zu Punkt und ergänzen den Rest aus dem Zusammenhang. Am Zeilenende müssen sie zurück an den Anfang der nächsten Zeile. Ist die Zeile zu lang, finden sie den Anfang schlecht wieder. Ist sie zu kurz, reißt der Lesefluss ständig ab.</p></div><div style="flex:1;"><p style="font-family:PTsans;font-size:2.6vh;color:#9313ce;margin:0 0 1vh;text-align:left;">Kurzer Text: kein Problem</p><p style="font-family:PTserif;font-size:5vh;line-height:1.3;margin:0;text-align:center;hyphens:none;">Typografie ist Auswählen, Gliedern, Anordnen und Lesbarmachen.</p></div></div>
  </div>
</section>

{% statement "Am Screen: linksbündig.", "Blocksatz braucht Silbentrennung und viel Breite. Zentriert nur für Kurzes." %}
