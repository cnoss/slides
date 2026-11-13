---
title: "Was ist ein Layout?"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Die Definition, die wir heute brauchen: Ein Layout ordnet Text, Bild und Fläche auf einem Format. Es entscheidet, was zuerst gelesen wird, was zusammengehört und was zurücktritt.

  Das Wort kommt aus dem Englischen: to lay out, auslegen, ausbreiten. In Druckereien und Agenturen hieß so der Entwurf, auf dem die Teile einer Seite ausgelegt wurden, bevor sie gesetzt wurden.

  Für jedes Layout stellen sich dieselben Fragen. Im bisherigen Foliensatz standen sie als fünf W-Fragen: Was (Inhalt), Warum (Ziel), Für wen (Zielgruppe), Wo (Medium) und Wie (stilistische Festlegungen). Die ersten vier kommen vor dem Wie. Ausführlich in der Methode Layoutanalyse.

  Danach die Geräte-Reihe: Desktop, Tablet und Smartphone im richtigen Seitenverhältnis, die übliche Ausrichtung mit schwarzer Kontur, die gedrehte mit grauer. Beim Weiterschalten füllen sich die Umrisse mit demselben Inhalt: drei Spalten auf dem Desktop, zwei auf dem Tablet hoch, eine auf dem Smartphone hoch. Frage: Wer entscheidet, was auf dem Smartphone quer passiert? Antwort: das Layout, also Sie.

  Zum Schluss das Foto von Brad Frost, das er in seinen Vorträgen zu Responsive Design und Atomic Design immer wieder zeigt: Geräte aus seinem eigenen Bestand, 2012. Seitdem ist die Vielfalt nur größer geworden: Uhren, faltbare Smartphones, Autos, Fernseher. Foto: Brad Frost, »Devices«, Flickr, CC BY 2.0, https://www.flickr.com/photos/brad_frost/7387824246

  Die Abgrenzung: Raster, Wireframe, Layout und Screendesign werden oft durcheinander verwendet. Das Raster ist das Gerüst, der Wireframe das Layout ohne Oberfläche, das Screendesign kommt mit Oberfläche, Zuständen und Interaktion dazu. Auf dem Screen ist ein Layout außerdem nie ein einzelnes Bild, sondern ein System aus Regeln für viele Formate (siehe Inhalt bestimmt Form).

  **Hintergrund**

  Der Begriff Makrotypografie meint dasselbe aus Sicht der Typografie: die Anordnung von Text und Bild auf der Seite, im Unterschied zur Mikrotypografie, die sich um Buchstaben, Wörter und Zeilen kümmert. Zum Weiterlesen: Lupton, Thinking with Type (Grid).
---

{% interlude "Was ist ein Layout?", "Und warum reicht es nicht, alles irgendwie unterzubringen?" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Layout</h1>
    <p><em>von englisch »to lay out«: auslegen, ausbreiten</em></p>
    <p>Die Anordnung aller Elemente auf einem Format, also Text, Bild, Fläche und Bedienelemente, nach einer erkennbaren Ordnung.</p>
    {% fragment '<p class="list"><strong>Reihenfolge:</strong> Was wird zuerst gelesen, was danach?</p>' %}
    {% fragment '<p class="list"><strong>Zusammenhang:</strong> Was gehört zusammen, was ist getrennt?</p>' %}
    {% fragment '<p class="list"><strong>Gewicht:</strong> Was ist wichtig, was tritt zurück?</p>' %}
    {% fragment '<p class="list"><strong>Raum:</strong> Was bleibt frei?</p>' %}
  </div>
</section>

{% statement "Ein Layout ordnet Text, Bild und Fläche auf einem Format.", "Es entscheidet, was zuerst gelesen wird, was zusammengehört und was zurücktritt." %}

<section class="simple" data-transition="fade">
<div>

# Nicht dasselbe

| Begriff | Was es ist |
|---|---|
| **Raster** | das unsichtbare Gerüst unter dem Layout |
| **Wireframe** | das Layout ohne Oberfläche: Struktur, Gewicht, Reihenfolge |
| **Layout** | die Anordnung der Elemente auf dem Format |
| **Screendesign** | Layout plus Oberfläche, Zustände und Interaktion |

</div>
</section>

{% statement "Auf dem Screen ist ein Layout kein Bild, sondern ein System.", "Dieselben Inhalte müssen auf vielen Formaten funktionieren. Das Layout legt fest, was sich anpasst und was bleibt." %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Ein Inhalt, viele Formate: Desktop, Tablet und Smartphone, die übliche Ausrichtung schwarz, die gedrehte grau"}' %}
<rect data-id="desk" x="22.1" y="196.5" width="237.6" height="148.5" rx="6" fill="#ffffff" stroke="#231f20" stroke-width="3" />
<rect data-id="tab-h" x="279.7" y="148.0" width="137.6" height="197.0" rx="6" fill="#ffffff" stroke="#231f20" stroke-width="3" />
<rect data-id="tab-q" x="437.3" y="207.4" width="197.0" height="137.6" rx="6" fill="#ffffff" stroke="#888888" stroke-width="3" />
<rect data-id="ph-h" x="654.3" y="205.7" width="64.4" height="139.3" rx="6" fill="#ffffff" stroke="#231f20" stroke-width="3" />
<rect data-id="ph-q" x="738.7" y="280.6" width="139.3" height="64.4" rx="6" fill="#ffffff" stroke="#888888" stroke-width="3" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Das Layout passt sich an: Die Reihenfolge bleibt, die Zahl der Spalten ändert sich"}' %}
<rect data-id="desk" x="22.1" y="196.5" width="237.6" height="148.5" rx="6" fill="#ffffff" stroke="#231f20" stroke-width="3" />
<rect data-id="desk-kopf" x="38.7" y="213.1" width="204.3" height="8.9" fill="#888888" />
<rect data-id="desk-k0" x="38.7" y="231.5" width="61.8" height="55.6" fill="#e4e4e4" />
<rect data-id="desk-b0" x="38.7" y="231.5" width="61.8" height="30.6" fill="#c4c4c4" />
<rect data-id="desk-k1" x="110.0" y="231.5" width="61.8" height="55.6" fill="#e4e4e4" />
<rect data-id="desk-b1" x="110.0" y="231.5" width="61.8" height="30.6" fill="#c4c4c4" />
<rect data-id="desk-k2" x="181.3" y="231.5" width="61.8" height="55.6" fill="#e4e4e4" />
<rect data-id="desk-b2" x="181.3" y="231.5" width="61.8" height="30.6" fill="#c4c4c4" />
<rect data-id="tab-h" x="279.7" y="148.0" width="137.6" height="197.0" rx="6" fill="#ffffff" stroke="#231f20" stroke-width="3" />
<rect data-id="tab-h-kopf" x="289.3" y="157.6" width="118.3" height="11.8" fill="#888888" />
<rect data-id="tab-h-k0" x="289.3" y="174.9" width="56.4" height="50.8" fill="#e4e4e4" />
<rect data-id="tab-h-b0" x="289.3" y="174.9" width="56.4" height="27.9" fill="#c4c4c4" />
<rect data-id="tab-h-k1" x="351.2" y="174.9" width="56.4" height="50.8" fill="#e4e4e4" />
<rect data-id="tab-h-b1" x="351.2" y="174.9" width="56.4" height="27.9" fill="#c4c4c4" />
<rect data-id="tab-h-k2" x="289.3" y="231.2" width="56.4" height="50.8" fill="#e4e4e4" />
<rect data-id="tab-h-b2" x="289.3" y="231.2" width="56.4" height="27.9" fill="#c4c4c4" />
<rect data-id="tab-h-k3" x="351.2" y="231.2" width="56.4" height="50.8" fill="#e4e4e4" />
<rect data-id="tab-h-b3" x="351.2" y="231.2" width="56.4" height="27.9" fill="#c4c4c4" />
<rect data-id="tab-q" x="437.3" y="207.4" width="197.0" height="137.6" rx="6" fill="#ffffff" stroke="#888888" stroke-width="3" />
<rect data-id="tab-q-kopf" x="451.1" y="221.2" width="169.4" height="8.3" fill="#888888" />
<rect data-id="tab-q-k0" x="451.1" y="237.3" width="51.2" height="46.1" fill="#e4e4e4" />
<rect data-id="tab-q-b0" x="451.1" y="237.3" width="51.2" height="25.4" fill="#c4c4c4" />
<rect data-id="tab-q-k1" x="510.2" y="237.3" width="51.2" height="46.1" fill="#e4e4e4" />
<rect data-id="tab-q-b1" x="510.2" y="237.3" width="51.2" height="25.4" fill="#c4c4c4" />
<rect data-id="tab-q-k2" x="569.3" y="237.3" width="51.2" height="46.1" fill="#e4e4e4" />
<rect data-id="tab-q-b2" x="569.3" y="237.3" width="51.2" height="25.4" fill="#c4c4c4" />
<rect data-id="ph-h" x="654.3" y="205.7" width="64.4" height="139.3" rx="6" fill="#ffffff" stroke="#231f20" stroke-width="3" />
<rect data-id="ph-h-kopf" x="659.3" y="210.7" width="54.4" height="8.4" fill="#888888" />
<rect data-id="ph-h-k0" x="659.3" y="222.1" width="54.4" height="48.9" fill="#e4e4e4" />
<rect data-id="ph-h-b0" x="659.3" y="222.1" width="54.4" height="26.9" fill="#c4c4c4" />
<rect data-id="ph-h-k1" x="659.3" y="274.0" width="54.4" height="48.9" fill="#e4e4e4" />
<rect data-id="ph-h-b1" x="659.3" y="274.0" width="54.4" height="26.9" fill="#c4c4c4" />
<rect data-id="ph-q" x="738.7" y="280.6" width="139.3" height="64.4" rx="6" fill="#ffffff" stroke="#888888" stroke-width="3" />
<rect data-id="ph-q-kopf" x="748.4" y="290.4" width="119.8" height="4.0" fill="#888888" />
<rect data-id="ph-q-k0" x="748.4" y="300.0" width="57.1" height="35.3" fill="#e4e4e4" />
<rect data-id="ph-q-b0" x="748.4" y="300.0" width="57.1" height="19.4" fill="#c4c4c4" />
<rect data-id="ph-q-k1" x="811.1" y="300.0" width="57.1" height="35.3" fill="#e4e4e4" />
<rect data-id="ph-q-b1" x="811.1" y="300.0" width="57.1" height="19.4" fill="#c4c4c4" />
{% endframe %}

{% screenshot "./images/geraete-brad-frost.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"So sah das schon 2012 aus: Ein Layout muss auf all dem funktionieren<br><small>Foto: Brad Frost, »Devices«, 2012, Flickr, CC BY 2.0</small>"}' %}
