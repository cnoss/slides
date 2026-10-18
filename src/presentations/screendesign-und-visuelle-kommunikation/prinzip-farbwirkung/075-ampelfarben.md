---
title: Ampelfarben
layout: presentation.11ty.js
slideClasses: wrap
status: ok
transition: none
speaker: |
  Rot, Gelb und Grün sind im Interface fest belegt, gelernt von der Ampel: Rot heißt Stopp, Fehler, Gefahr, Löschen. Gelb oder Orange heißt Achtung, Warnung. Grün heißt erlaubt, erledigt, erfolgreich. Diese Bedeutungen sind so stark, dass sie Markenfarben überlagern.

  **Das Problem mit roten Marken:** Viele Organisationen haben Rot als Unternehmensfarbe, etwa Deutsche Bahn, Sparkasse, Vodafone, Media Markt, Coca-Cola. Dann liegt es nahe, Rot auch als Akzentfarbe im Interface zu nehmen: für Buttons, Links, Hervorhebungen. Im Formular kollidiert das: Ist der rote Rahmen ein Fehler oder nur Gestaltung? Ist der rote Text eine Warnung oder ein Link? Und ist der rote Button die Hauptaktion oder »Löschen«?

  **Die Wireframes:** Erst ein Formular mit rotem Kopf und rotem Button, alles gut. Dann tritt ein Fehler auf, das Feld wird rot markiert: Fehler und Marke sehen gleich aus. Die Lösung: Hauptaktion in neutralem Dunkel, Fehler zusätzlich mit Symbol und Text.

  **Die Bahn** löst es so: Rot für Logo, Markenelemente und den Suchen-Button. Warnungen in Orange mit Warnsymbol, damit sie sich vom Markenrot absetzen.

  **Lösungswege:**
  - Markenfarbe für Marke: Logo, Kopfbereich, Illustrationen, Kampagnen
  - Statusfarben eigens definieren und bewusst vom Markenrot absetzen, z. B. ein dunkleres oder orangeres Fehlerrot
  - Fehler nie nur über Farbe: Symbol und Text dazu (WCAG 1.4.1)
  - Im Design-System getrennte Tokens: color-brand und color-error, auch wenn sie ähnlich aussehen

  Frage ans Publikum: Welche Apps mit roter Marke kennen Sie? Wie zeigen die einen Fehler an?
---

{% interlude "Rot heißt Stopp.", "Ampelfarben im Interface" %}

<section class="simple" data-transition="fade">
<div>

# Ampelfarben sind fest belegt

| Farbe | Bedeutung im Interface | Typisch für |
|---|---|---|
| **Rot** | Stopp, Fehler, Gefahr | Fehlermeldungen, Löschen, Pflichtfelder |
| **Gelb, Orange** | Achtung, Warnung | Hinweise, ablaufende Fristen |
| **Grün** | Erlaubt, erledigt, Erfolg | Bestätigungen, Online-Status, »Gespeichert« |

</div>
</section>

{% question "Und wenn die Marke rot ist?", "Deutsche Bahn, Sparkasse, Vodafone, Media Markt: Wo ist dann noch Platz für den Fehler?" %}

{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Rote Marke, roter Button: alles gut"}' %}
<rect data-id="bg" x="200" y="30" width="500" height="440" rx="0" fill="#ffffff" />
<rect x="200" y="30" width="500" height="440" fill="none" stroke="#d9d9d9" stroke-width="2" />
<rect data-id="head" x="200" y="30" width="500" height="56" rx="0" fill="#d81e2c" />
<rect data-id="logo" x="224" y="46" width="48" height="24" rx="4" fill="#ffffff" />
<rect data-id="l0" x="240" y="120" width="110" height="12" rx="0" fill="#888888" />
<rect data-id="f0" x="240" y="140" width="420" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="l1" x="240" y="240" width="110" height="12" rx="0" fill="#888888" />
<rect data-id="f1" x="240" y="260" width="420" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="btn" x="240" y="350" width="180" height="48" rx="24" fill="#d81e2c" />
<rect data-id="btn2" x="440" y="350" width="120" height="48" rx="24" fill="#ffffff" />
<rect data-id="btn2r" x="440" y="350" width="120" height="48" rx="24" fill="none" stroke="#888888" stroke-width="2" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Ein Fehler tritt auf: Ist das Rot jetzt Marke oder Warnung?"}' %}
<rect data-id="bg" x="200" y="30" width="500" height="440" rx="0" fill="#ffffff" />
<rect x="200" y="30" width="500" height="440" fill="none" stroke="#d9d9d9" stroke-width="2" />
<rect data-id="head" x="200" y="30" width="500" height="56" rx="0" fill="#d81e2c" />
<rect data-id="logo" x="224" y="46" width="48" height="24" rx="4" fill="#ffffff" />
<rect data-id="l0" x="240" y="120" width="110" height="12" rx="0" fill="#888888" />
<rect data-id="f0" x="240" y="140" width="420" height="44" fill="#ffffff" stroke="#d81e2c" stroke-width="3" />
<rect data-id="err" x="240" y="198" width="220" height="12" rx="0" fill="#d81e2c" />
<rect data-id="l1" x="240" y="240" width="110" height="12" rx="0" fill="#888888" />
<rect data-id="f1" x="240" y="260" width="420" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="btn" x="240" y="350" width="180" height="48" rx="24" fill="#d81e2c" />
<rect data-id="btn2" x="440" y="350" width="120" height="48" rx="24" fill="#ffffff" />
<rect data-id="btn2r" x="440" y="350" width="120" height="48" rx="24" fill="none" stroke="#888888" stroke-width="2" />
{% endframe %}
{% frame '{"stage":"#ffffff", "w":900, "h":500, "bu":"Lösung: Hauptaktion neutral, Fehler mit Symbol und Text"}' %}
<rect data-id="bg" x="200" y="30" width="500" height="440" rx="0" fill="#ffffff" />
<rect x="200" y="30" width="500" height="440" fill="none" stroke="#d9d9d9" stroke-width="2" />
<rect data-id="head" x="200" y="30" width="500" height="56" rx="0" fill="#d81e2c" />
<rect data-id="logo" x="224" y="46" width="48" height="24" rx="4" fill="#ffffff" />
<rect data-id="l0" x="240" y="120" width="110" height="12" rx="0" fill="#888888" />
<rect data-id="f0" x="240" y="140" width="420" height="44" fill="#ffffff" stroke="#d81e2c" stroke-width="3" />
<circle data-id="ico" cx="248" cy="204" r="8" fill="#d81e2c" />
<rect data-id="err" x="262" y="198" width="220" height="12" rx="0" fill="#d81e2c" />
<rect data-id="l1" x="240" y="240" width="110" height="12" rx="0" fill="#888888" />
<rect data-id="f1" x="240" y="260" width="420" height="44" fill="#ffffff" stroke="#888888" stroke-width="2" />
<rect data-id="btn" x="240" y="350" width="180" height="48" rx="24" fill="#231f20" />
<rect data-id="btn2" x="440" y="350" width="120" height="48" rx="24" fill="#ffffff" />
<rect data-id="btn2r" x="440" y="350" width="120" height="48" rx="24" fill="none" stroke="#888888" stroke-width="2" />
{% endframe %}
{% screenshot "./images/ampel-bahn.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Rot für Marke und Suchen, Warnungen in Orange mit Symbol<br><small>bahn.de, Screenshot 2026</small>"}' %}

<section class="simple" data-transition="fade">
  <div>
    <h1>Marke und Status trennen</h1>
    {% fragment '<p class="list">Markenrot für die Marke: Logo, Kopf, Kampagnen</p>' %}
    {% fragment '<p class="list">Statusfarben eigens definieren, deutlich vom Markenrot abgesetzt</p>' %}
    {% fragment '<p class="list">Fehler nie nur über Farbe: Symbol und Text dazu</p>' %}
    {% fragment '<p class="list">Getrennte Design Tokens: <code>color-brand</code> und <code>color-error</code></p>' %}
  </div>
</section>
