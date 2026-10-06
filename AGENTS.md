# Folien erstellen: Anweisungen für KI-Agenten

Dieses Repo enthält die Vorlesungsfolien von Christian Noss (Hochschule, Medieninformatik). Folien sind Markdown-Dateien mit Nunjucks-Shortcodes, gebaut mit 11ty, präsentiert mit reveal.js.

Die vollständige technische Referenz (alle Shortcodes, Props, Klassen, Front-Matter-Felder) steht in [README.md](README.md). Diese Datei sagt, **wie** du Folien erzeugst. Lies vor der ersten Folie das README, mindestens die Abschnitte »Wie ein Deck aufgebaut ist«, »Shortcodes« und »Bekannte Macken«.

## Vorbilder

Orientiere dich an Decks, die 2025/26 entstanden sind. Das wichtigste Vorbild ist `src/presentations/screendesign/design-in-der-medieninformatik/`. Weitere Vorbilder:

- `src/presentations/screendesign/about-screendesign/`
- `src/presentations/screendesign/punkt/`, `textsatz/`, `typographie/`, `farben/`, `gestaltgesetze/`
- `src/presentations/misc/praesentieren-im-studium-2026/`
- `src/presentations/bachelor/praesentieren-2026/`

Ältere Decks (eine Datei pro Folie, viel rohes HTML, `version: 1`, reveal-md-Dateien mit `separator`) **nicht** als Vorlage nehmen.

## Arbeitsablauf

1. **Auftrag klären.** Bevor du schreibst, brauchst du: Kategorie und Deck-Name, Publikum (Semester, Vorwissen), Dauer der Einheit, Lernziel bzw. Kernaussagen, vorhandenes Material (alte Decks, Bilder, Texte). Fehlt etwas Wesentliches, frag nach.
2. **Gliederung vorschlagen.** Liste die Kapitel-Dateien mit Präfix, Titel, Zweck und Zeitbudget. Lass die Gliederung bestätigen, bevor du alle Dateien schreibst.
3. **Dateien anlegen.** Ein Kapitel pro Datei, siehe Rezepte unten.
4. **Bilder nie erfinden.** Du kannst keine Fotos, Screenshots oder Plakate liefern. Verwende nur Bilder, die bereits in `images/` liegen oder die dir genannt wurden. Für fehlende Bilder: Platzhalter auskommentieren und als ToDo markieren (siehe unten). Einfache Grafiken (Punkte, Linien, Raster) darfst du als Inline-SVG bauen.
5. **Bauen und prüfen**, siehe [Prüfen](#prüfen).
6. **Berichten.** Nenne die angelegten Dateien, alle offenen ToDos (`status`) und was der Mensch noch liefern muss (Bilder, Quellen, Zahlen).

Nicht anfassen ohne ausdrücklichen Auftrag: `.eleventy.js`, `src/_layouts/`, `src/assets/`, `reveal/`, `impress.js/`, `docs/` (Build-Output), die Metadaten in `index.md` von *Screendesign und visuelle Kommunikation*, fremde Decks.

## Aufbau eines Decks

```
src/presentations/<kategorie>/<deck>/
├── 000-intro.md          slideClasses: intro
├── 010-heute.md          slideClasses: simple   (Agenda als fragment-Liste)
├── 020-<kapitel>.md      slideClasses: images oder wrap
├── 030-<kapitel>.md
├── …
├── 1x0-zusammenfassung.md slideClasses: simple
├── index.md              slideClasses: outro    (Abschlussfolie, keine 9999-outro.md)
└── images/
```

- Präfixe dreistellig in Zehnerschritten, gleich lang, nicht doppelt. Sortiert wird als String.
- Dateinamen und Bildnamen in kebab-case, ohne Umlaute und Leerzeichen (`030-fuer-wen.md`, `zielgruppe-speisekarte-1.png`).
- Jede Datei hat `layout: presentation.11ty.js` und `status: ok` (oder einen ToDo-Text).
- `transition: zoom` für Intro und Kapitel-Dateien ist üblich. Sonst weglassen (Standard: `convex`).

## Rezepte

### Intro (`000-intro.md`)

```
---
title: <Deck-Titel>
layout: presentation.11ty.js
slideClasses: intro
transition: zoom
---

<div class="is-full-width">

# <Deck-Titel>

## <Claim oder Zitat><br><small><Autor, falls Zitat></small>

</div>
```

### Agenda und Zusammenfassung (`simple`)

```
---
title: Heute
layout: presentation.11ty.js
slideClasses: simple
status: ok
---

{% fragment '<p class="list">Für wen gestalten wir eigentlich?</p>' %}
{% fragment '<p class="list">Ein Raster, das Sie das ganze Semester begleitet</p>' %}
```

Bei der Zusammenfassung ganze Sätze ohne `class="list"`, je ein `fragment` pro Aussage.

### Kapitel mit Beispielen (`images`)

```
---
title: Für wen ist das?
layout: presentation.11ty.js
slideClasses: images
status: ok
transition: zoom
speaker: |
  **Ratespiel (ca. 10 Minuten)**

  - Pro Bild 30 Sekunden zu zweit: Zielgruppe in drei Stichworten plus **ein** visuelles Indiz.
  - Indizien benennen: Farbe, Schriftgröße, Bildsprache, Dichte, Weißraum.

  **Kernaussage:** Erst Funktion und Zielgruppe, dann die Form.
---

{% interlude "Für wen ist das?", "Funktion & Zielgruppe" %}

{% screenshot "./images/zielgruppe-medikamente.png", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Für wen ist das? Woran sehen Sie das?"}' %}

{% screenshot "./images/zielgruppe-nachrichten.jpg", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Gleiche Funktion: Nachrichten. Für wen ist welche Seite?"}' %}

{% statement "Wir gestalten fast nie für uns selbst.", "Die erste Frage ist nicht »Wie sieht es aus?«, sondern »Wofür und für wen?«" %}
```

- `classes`: `shadow` für Screenshots von Interfaces, `no-shadow` für Grafiken, Freisteller, Plakate.
- `width` fast immer `"auto"`.
- Ganzflächige Bilder: `screenshotFs` statt `screenshot`.

### Übung (`images`)

Ablauf: `interlude` → Anleitung als `<section class="simple">` → `question` mit Zeitangabe → Auflösung → Reflexionsfrage.

```
{% interlude "Beschreibungs-Pingpong", "Runde 1" %}

<section class="simple" data-transition="fade">
  <div>
    <h1>So geht's</h1>
    {% fragment '<p class="list">Zu zweit. Links: Screen A, rechts: Screen B. Nicht spicken!</p>' %}
    {% fragment '<p class="list"><strong>7 Min.</strong> Screen schriftlich beschreiben. Nur Text, keine Skizzen.</p>' %}
  </div>
</section>

{% question "Schreiben", "7 Minuten. Nur Text, keine Skizzen." %}

{% screenshot "./images/pingpong-r1-a.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Screen A"}' %}

{% question "Was hat in den Beschreibungen gefehlt?", "Sammeln Sie zu zweit drei Dinge, die Sie falsch oder gar nicht zeichnen konnten." %}
```

### Input mit Begriffen (`wrap`)

```
{% interlude "Vokabular", "Die fünf Elemente" %}

{% qa "Was ist ein Element?", "Alles, was man auf dem Screen einzeln benennen kann." %}
{% qa "Was ist eine Eigenschaft?", "Größe, Farbe, Form, Position, Schrift." %}

{% important "Format, Elemente, Eigenschaften, Beziehungen, Wirkung" %}
```

### Merksatz als eigene Folie (`statement`)

```
---
title: Identität
layout: presentation.11ty.js
slideClasses: statement
status: ok
---

ist das Prinzip, durch das sich ein Ding von allen anderen unterscheidet.
```

### Code (`wrap`)

Längere Texte und Code gehören als Variable ins Front Matter:

```
---
title: Nesting
layout: presentation.11ty.js
slideClasses: wrap
status: ok
nestingText: |
  Selektoren lassen sich ineinander verschachteln.
nestingCode: |
  .card {
    & .title { font-weight: 700; }
  }
---

{% codeSmall "Nesting", nestingText, nestingCode, "css" %}
```

### Fehlendes Bild als Platzhalter

```
---
title: Ihre Plakate
layout: presentation.11ty.js
slideClasses: images
status: 6 bis 8 Plakate einfügen
---

{% interlude "Ihre Plakate", "Abgabe vom 8. Oktober" %}

{# Plakate hier einfügen, z.B.:
{% screenshot "./images/plakat-01.jpg", '{"transition":"fade", "classes":"no-shadow", "bu":"1"}' %}
#}
```

Der `status`-Text erscheint als »ToDo« auf der Folie. Verweise nie auf Bilddateien, die nicht existieren.

### Abschluss (`index.md`)

```
---
title: <Deck-Titel>
layout: presentation.11ty.js
slideClasses: outro
transition: convex
---
```

## Technische Fallstricke

- **Transition bei `interlude` und `simpleText` ist ein String als drittes Argument**, kein JSON: `{% interlude "Titel", "Untertitel", "slide" %}`. JSON erzeugt kaputtes HTML.
- Props sind ein JSON-String in **einfachen** Anführungszeichen mit **doppelten** innen: `'{"bu":"Text"}'`. Gültiges JSON: keine Kommas am Ende, keine einfachen Anführungszeichen innen. Ein Apostroph im Text (»geht's«) zerbricht den String, wenn das Argument in einfachen Anführungszeichen steht. Dann das Argument in doppelte Anführungszeichen setzen und innere doppelte Anführungszeichen mit `\"` maskieren.
- Folien-Shortcodes (`screenshot`, `interlude`, `question`, `qa`, `statement` …) erzeugen `<section>`s und gehören in `images`- oder `wrap`-Dateien, nicht in `simple`.
- Bausteine (`fragment`, `text`, `niceToKnow`) gehören in eine Folie (`simple`-Datei oder `<section class="simple">`).
- `cite` nimmt nur ein Argument. Autor: eigene Datei mit `slideClasses: cite` und `author:`. Keine eigenen Anführungszeichen, die setzt das CSS.
- `qa` gibt die Antwort als rohes HTML aus. Dort kein Markdown, sondern `<strong>`, `<br>`, `<small>`.
- Prop `credit` wirkt nicht. Bildnachweise in die `bu` schreiben oder das HTML-Muster »Bild mit Bildnachweis« aus dem README nehmen.
- `*Wort*` wird in Shortcodes zu `<mark>`, `**Wort**` zu fettem Lila. Sparsam einsetzen.
- Nutze nur Klassen, die im README stehen. Erfinde keine neuen, und schreib kein Inline-CSS, solange es nicht unvermeidbar ist.
- `speaker`, `badge`, `footer` gelten für die ganze Datei, nicht für einzelne Folien.

## Sprache und Stil

Die Folien sind deutsch, außer das Deck ist ausdrücklich englisch (z. B. Workshops im Master).

- **Siezen.** Das Publikum wird immer mit »Sie« angesprochen.
- **Kurz.** Folientexte sind Stichworte, Fragmente oder kurze Hauptsätze. Eine Aussage pro Folie. Fließtext gehört in die Speaker Notes.
- **Keine Gedankenstriche** (– oder —). Stattdessen Punkt, Doppelpunkt oder Komma: »Letzte Woche: Entscheiden Sie nicht nach Geschmack. Heute: das Werkzeug dafür.«
- **Anführungszeichen auf Folien:** Guillemets »…«. In Speaker Notes sind gerade "…" in Ordnung.
- **Fragen statt Behauptungen.** Überschriften, `question`-Folien und Bildunterschriften fragen das Publikum oft direkt: »Für wen ist das? Woran sehen Sie das?«, »Und hier?«, »Gleiche Funktion. Was ist der Unterschied?«
- **Imperative für Arbeitsaufträge:** »Begründen Sie Ihre Wahl noch einmal. Diesmal mit dem Raster.«
- **Überschriften in Satzschreibung**, ohne Punkt am Ende (außer bei Statements, die ein ganzer Satz sind).
- **Gendern mit Doppelpunkt:** Entwickler:innen, Zuhörer:innen.
- **Trenner in Aufzählungen auf einer Zeile:** ` // ` (»Format // Darstellungsfläche«).
- **Zeitangaben** in Aufgaben konkret: »7 Minuten«, »**7 Min.**«.
- **Fachbegriffe** präzise und konsistent. Wird ein Begriff eingeführt, wird er später genauso verwendet.
- **Quellen** angeben: Zitate mit Autor, Studien mit Autor und Jahr in den Speaker Notes oder im `cite`-Front-Matter (`src`).
- Rechtschreibung prüfen. Umlaute und ß korrekt, nie »ae«/»ss« als Ersatz im Text.

## Didaktische Dramaturgie

Eine Einheit folgt typischerweise diesem Bogen:

1. **Einstieg mit Aktivierung:** eigenes Material des Publikums zeigen oder eine Frage stellen (`question`), dann eine zugespitzte These (`statement`).
2. **Agenda** »Heute« (`simple` mit `fragment`-Liste).
3. **Kapitel**, jeweils eröffnet mit `interlude` (Titel und Untertitel), abgeschlossen mit `statement`-Merksatz oder Reflexionsfrage.
4. **Wechsel zwischen Input und Aktivität:** Ratespiel, Übung in Runden, Live-Analyse mit schrittweise eingeblendeten Fragmenten, dann »Und jetzt Sie.«
5. **Pause** als eigenes Kapitel.
6. **Sicherung:** Vokabular/Glossar, Rückbezug auf den Einstieg (»Und Ihr Favorit von heute Morgen?«).
7. **Brücke** zur nächsten Einheit, **Zusammenfassung** als Fragment-Sätze, Outro.

## Speaker Notes

Jede Kapitel-Datei mit Aktivität oder erklärungsbedürftigem Input bekommt `speaker:`. Umfang etwa 50 bis 120 Wörter, Markdown:

```yaml
speaker: |
  **<Phase> (ca. <n> Minuten)**

  - Ablauf in Schritten, mit Minuten: »3 Min. erklären, 7 Min. schreiben, 5 Min. sammeln.«
  - Material und Organisation (Papier, Paare, QR-Codes).
  - Was bewusst weggelassen wird und warum.

  **Erwartbare Antworten:** … (was an die Tafel gehört)

  Hintergrund mit Quelle, falls nötig (Bertin 1967).

  **Kernaussage:** <ein Satz>
```

- Phasenbezeichnungen: Ablauf, Ratespiel, Input, Übung, Live-Analyse, Sicherung, Brücke zum Workshop.
- Die Zeitbudgets aller Kapitel sollen zur Gesamtdauer passen. Rechne sie in der Gliederung zusammen.
- Verweise auf andere Folien mit deren Titel: »(Folie "Und Ihr Favorit?")«.

## Prüfen

```bash
npx @11ty/eleventy --quiet
```

Das baut in `docs/` (ignoriert, dauert wenige Sekunden). Danach prüfen:

```bash
D=docs/presentations/<kategorie>/<deck>/index.html
grep -c 'data-slide-class=' $D                 # Anzahl Dateien im Deck
grep -o 'data-transition="{[^ ]*' $D           # muss leer sein (JSON als Transition)
grep -o '{%[^%]*%}' $D                         # muss leer sein (nicht verarbeitete Shortcodes)
grep -o 'ToDo: [^<]*' $D                       # offene ToDos
grep -oE '(src|data-background)="(\./)?images/[^"]*"' $D | sort -u   # Bildpfade: existieren alle in images/?
```

Ein Build-Fehler nennt meist Datei und Zeile. Typische Ursachen sind kaputtes Props-JSON oder unmaskierte Anführungszeichen.

Wenn möglich, sieh dir das Deck im Browser an (`npm run dev`, dann `http://localhost:8080/presentations/<kategorie>/<deck>/`), besonders bei neuen HTML-Sections oder Inline-SVG.
