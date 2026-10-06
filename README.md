# Slides

HTML-Slidedecks für meine Vorlesungen. Das Projekt nutzt den Static-Site-Generator [11ty](https://www.11ty.dev/docs/) (v2) und als Präsentations-Framework [reveal.js](https://revealjs.com/). Für einzelne Decks gibt es optional [impress.js](https://impress.js.org/).

Veröffentlicht unter [cnoss.github.io/slides](https://cnoss.github.io/slides/).

[Figma für Montagen](https://www.figma.com/design/xXM2JmJMAWsqoOJQyxqaqa/Slides?m=auto&t=ZhJbsnkuKr5jUWYC-1)

Anweisungen für KI-Agenten, die hier Folien erzeugen sollen: [AGENTS.md](AGENTS.md).

**Inhalt**

- [Schnellstart](#schnellstart)
- [Wie ein Deck aufgebaut ist](#wie-ein-deck-aufgebaut-ist)
- [Front Matter](#front-matter)
- [Shortcodes](#shortcodes)
- [Props und Klassen](#props-und-klassen)
- [Inhalte aus dem Front Matter an Shortcodes übergeben](#inhalte-aus-dem-front-matter-an-shortcodes-übergeben)
- [HTML-Bausteine](#html-bausteine)
- [Ein komplettes Beispiel](#ein-komplettes-beispiel)
- [Präsentieren](#präsentieren)
- [Bekannte Macken](#bekannte-macken)
- [Legacy](#legacy)
- [Projekt, Build und Deployment](#projekt-build-und-deployment)

## Schnellstart

```bash
npm install
npm run dev        # SASS im Watch-Mode + 11ty-Dev-Server mit Live-Reload
```

Neues Deck anlegen:

```
src/presentations/<kategorie>/<deck>/
├── 000-intro.md
├── 010-<kapitel>.md
├── 020-<kapitel>.md
├── …
├── index.md
└── images/
```

## Wie ein Deck aufgebaut ist

### Ein Ordner pro Deck, eine Datei pro Kapitel

Ein **Deck ist ein Ordner** unter `src/presentations/<kategorie>/<deck>/`. Das Layout [presentation.11ty.js](src/_layouts/presentation.11ty.js) sammelt alle `.md`-Dateien dieses Ordners ein, sortiert sie nach Dateinamen und baut daraus *eine* reveal.js-Präsentation.

Ursprünglich war jede Datei genau eine Folie. Bewährt hat sich inzwischen: **Eine Datei ist ein Kapitel.** Eine Kapitel-Datei hat `slideClasses: wrap` oder `slideClasses: images` und enthält eine Folge von [Shortcodes](#shortcodes). Jeder Shortcode, der eine `<section>` erzeugt, wird zu einer eigenen Folie. Technisch landen diese Folien als vertikaler Stapel in der äußeren `<section class="mi-slide">` der Datei. Mit Leertaste bzw. Pfeiltasten läuft man ganz normal durch.

Ein Kapitel folgt meist diesem Muster:

```
{% interlude "Kapiteltitel", "Untertitel" %}       ← Kapitelstart
{% screenshot … %} {% screenshot … %} …            ← Beispiele, Fragen, Übungen
{% statement "Merksatz", "Erläuterung" %}          ← Kapitelabschluss
```

Einzelne Dateien mit genau einer Folie gibt es weiterhin dort, wo das Layout die Folie selbst aufbaut: `intro`, `outro`, `simple`, `statement`, `cite`.

### Dateinamen und Reihenfolge

- Dreistellige Präfixe in Zehnerschritten: `010-…`, `020-…`, `030-…`. In die Lücken lassen sich später Kapitel einschieben (`015-…`).
- `000-intro.md` steht am Anfang.
- Sortiert wird **als Zeichenkette**, nicht numerisch. `1260-aufgabe.md` landet also zwischen `120-…` und `130-…`. Präfixe deshalb immer gleich lang halten (Ausnahme: `9999-outro.md`, das ohnehin hinten steht).
- Präfixe nicht doppelt vergeben.
- Dateinamen in kebab-case, ohne Umlaute: `030-fuer-wen.md`.

### `index.md`

Die `index.md` liefert die URL des Decks (`…/<deck>/`) und den Titel in der Übersicht. Sie hat nur Front Matter. Weil die Sortierung `index` ans Ende stellt, **wird sie als letzte Folie mitgerendert.** Daher empfohlen:

```yaml
---
title: Design in der Medieninformatik
layout: presentation.11ty.js
slideClasses: outro
transition: convex
---
```

Die `index.md` ist dann zugleich die Abschlussfolie, eine eigene `9999-outro.md` entfällt. Ältere Decks haben `index.md` mit `slideClasses: intro` plus `9999-outro.md`. Dort erscheint nach dem Outro noch eine leere lila Folie.

### Bilder

- Bilder liegen in `images/` im Deck-Ordner, Unterordner sind erlaubt (`images/kontraste/…`).
- Eingebunden werden sie relativ: `./images/zielgruppe-medikamente.png`.
- Dateinamen in kebab-case, ohne Leerzeichen und Umlaute. Serien werden nummeriert: `pingpong-r1-a.jpg`, `vereinfachung-04a.png`.
- Kopiert werden `jpg`, `jpeg`, `png`, `webp`, `svg` und `gif`.

### Kategorien

Die Übersichtsseite [src/index.md](src/index.md) listet die Decks nach Sammlungen. Jede Sammlung ist in [.eleventy.js](.eleventy.js) definiert und greift auf `src/presentations/<kategorie>/**/index.md` zu:

| Ordner | Collection |
| :--- | :--- |
| `screendesign-und-visuelle-kommunikation` | `screendesignUndVisuelleKommunikation` |
| `screendesign` | `screendesign` |
| `master` | `master` |
| `bachelor` | `bachelor` |
| `misc` | `misc` |

Eine neue Kategorie braucht eine neue Collection in `.eleventy.js` und einen Abschnitt in `src/index.md`.

**Screendesign und visuelle Kommunikation** ist modular aufgebaut. Jede Einheit (Rahmen, Haltung, Phänomen, Prinzip, Methode) ist ein eigenes Deck. Ihre `index.md` trägt zusätzliche Metadaten. Nach `typ` sortiert die Übersichtsseite die Decks in Gruppen:

```yaml
typ: "Prinzip"            # Rahmen | Haltung | Phänomen | Prinzip | Methode
gruppe: "Gewichten"       # wird in der Übersicht neben dem Titel angezeigt
tiefe: ""                 # wird in Klammern angezeigt
einsatz: ""
kurzsatz: ""
begriffe: []
herkunft: "U: wahrnehmungsarbeit/140 bis 220"   # aus welchem alten Deck/Folienbereich das Material stammt
inhalt:
  - "Hierarchisieren"
status: entwurf
```

## Front Matter

Jede Datei beginnt mit Front Matter:

```yaml
---
title: Für wen ist das?
layout: presentation.11ty.js
slideClasses: images
status: ok
transition: zoom
---
```

| Feld | Bedeutung |
| :--- | :--- |
| `title` | Titel der Datei. Bei `simple` die sichtbare Überschrift, bei `statement` die Aussage, bei `index.md` der Deck-Titel. |
| `layout` | Immer `presentation.11ty.js` (impress.js: `impress.11ty.js`). |
| `slideClasses` | Folientyp, siehe [Slide Classes](#slide-classes). |
| `status` | `ok`, `hidden` oder ein ToDo-Text, siehe [Status](#status). |
| `transition` | reveal.js-Übergang beim Wechsel *zu* dieser Datei: `none`, `fade`, `slide`, `convex` (Standard), `concave`, `zoom`. |
| `speaker` | Speaker Notes in Markdown, siehe [Speaker Notes](#speaker-notes). |
| `badge` | Kleines Badge (Markdown/HTML), das auf allen Folien der Datei erscheint. |
| `footer` | Markdown-Fußzeile, z. B. Quellen. Wirkt bei `images`, `wrap`, `code`, `codeSmall`. |
| `img` | Hintergrundbild aus `images/`. Bei `.jpg` kann die Endung entfallen. |
| `imgData` | Position und Größe des Hintergrundbilds: `{"position":"1% 1%", "size": "15%"}` |
| `credits` | Bildnachweis zum Hintergrundbild: `{'name': 'Barbara Iandolo', 'url': 'https://…'}` |
| `author` / `src` / `info` | Autor, Quelle und Zusatzinfo bei `cite`, `bigCite`, `shout`. |
| `additionalClasses` | Weitere Klassen für die äußere Section, siehe [Klassen](#klassen-für-folien-und-html). |
| beliebige weitere | Eigene Variablen, z. B. für längere Texte oder Code, siehe [Inhalte aus dem Front Matter](#inhalte-aus-dem-front-matter-an-shortcodes-übergeben). |

### Slide Classes

**Container für Shortcodes** (aktueller Standard):

| slideClasses | Verwendung |
| :--- | :--- |
| `images` | Kapitel mit Bildern, Screenshots, Übungen. |
| `wrap` | Kapitel aus Shortcodes (interlude, qa, important, shout …). Technisch identisch mit `images`. |
| `wrap is-dark` | Wie `wrap`, mit dunklem Hintergrund und heller Bildunterschrift. |

**Eigenständige Folien** (eine Folie pro Datei, das Layout baut sie auf):

| slideClasses | Verwendung |
| :--- | :--- |
| `intro` | Startfolie. Lila Hintergrund. Inhalt siehe [Beispiel](#000-intromd). |
| `outro` | Endfolie mit Avatar und »Danke für's Mitmachen«. Kein Inhalt nötig. |
| `simple` | `title` als Überschrift, darunter Text, Markdown-Liste oder `fragment`-Kette. |
| `statement` | `title` ist die Aussage, der Inhalt erscheint als Fragment darunter. |
| `cite` | Zitat. Inhalt = Zitattext, dazu `author`, optional `src` und `img`. |
| `bigCite` | Wie `cite`, größer. |
| `shout` | Ausruf auf blauem Grund, dazu `author`, `src`, `info` (Klick blendet `info` ein). |
| `code` / `codeSmall` | `title` plus Markdown mit Code (volle Breite bzw. so breit wie der Code). |
| `video` | Container für ein `<section class="video">`, siehe [Video](#video). |

`question`, `qa`, `split`, `screenshot` und `image` gibt es auch als Klasse. Sie werden aber praktisch nur über die gleichnamigen Shortcodes erzeugt.

### Status

| Wert | Wirkung |
| :--- | :--- |
| `ok` | nichts |
| `hidden` | Die ganze Datei wird nicht ausgegeben. |
| jeder andere Text | Wird als `ToDo: <Text>` oben rechts auf der Folie angezeigt. |

`status` dient als Arbeitsliste: `status: 6 bis 8 Plakate einfügen`.

### Speaker Notes

`speaker` ist Markdown und wird pro Datei, also pro Kapitel, gepflegt. Bewährter Aufbau:

```yaml
speaker: |
  **Ablauf (ca. 22 Minuten)**

  - 3 Min. erklären, 7 Min. schreiben, 7 Min. zeichnen, 5 Min. vergleichen und sammeln.
  - Papier und Stift: Jede Person braucht ein Blatt zum Schreiben und eins zum Zeichnen.

  **Typische Lücken, die an die Tafel gehören:** Größenverhältnisse, Abstände, Ausrichtung …

  **Kernaussage:** Wir merken, dass uns Kriterien und Vokabular fehlen.
```

- Erste Zeile: fette Phase mit Zeitbudget (`**Input (ca. 15 Minuten)**`, `**Sicherung (ca. 5 Minuten)**`).
- Danach Ablauf als Liste, erwartbare Antworten, Hintergrundwissen mit Quelle, Verweise auf spätere Folien.
- Zum Schluss `**Kernaussage:**` in einem Satz.

Anzeige: Taste `i` blendet die Notes auf der Folie ein, `S` öffnet die reveal.js-Speaker-View.

## Shortcodes

Alle Shortcodes stehen in [.eleventy.js](.eleventy.js). Markdown-Dateien laufen durch Nunjucks. Es gelten diese Regeln:

- Argumente werden durch Kommas getrennt: `{% name "a", "b" %}`.
- Props sind ein **JSON-String in einfachen Anführungszeichen**: `'{"transition":"fade", "bu":"Text"}'`. Im JSON gelten doppelte Anführungszeichen, typografische Anführungszeichen im Text sind unproblematisch: `"bu":"»Gefällt mir«"`.
- HTML im Argument: Wenn das Argument in einfachen Anführungszeichen steht, können die Attribute doppelte verwenden: `{% fragment '<p class="list">…</p>' %}`.
- Statt eines Strings geht auch eine Front-Matter-Variable ohne Anführungszeichen: `{% codeSmall "Titel", text, code, "js" %}`.
- `false` lässt ein optionales Argument leer: `{% simpleText false, "Nur Text" %}`.
- Auskommentieren: `{# … #}` (Nunjucks) oder `<!-- … -->` (HTML; der Shortcode wird dann trotzdem ausgeführt).

In Texten, die durch Markdown laufen, erzeugt `*Wort*` ein hervorgehobenes `<mark>` und `**Wort**` eine fette, lila Auszeichnung.

**Folien-Shortcodes** erzeugen eine eigene `<section>`. Sie gehören in `wrap`- oder `images`-Dateien. **Bausteine** (`fragment`, `text`, `niceToKnow`) erzeugen nur ein `<div>` und gehören *in* eine Folie, z. B. in eine `simple`-Datei.

### Übersicht

| Shortcode | Art | Häufigkeit 2025/26 |
| :--- | :--- | ---: |
| [`screenshot`](#screenshot) | Folie | 764 |
| [`fragment`](#fragment) | Baustein | 253 |
| [`interlude`](#interlude) | Folie | 210 |
| [`simpleText`](#simpletext) | Folie | 84 |
| [`screenshotFs`](#screenshotfs) | Folie | 52 |
| [`codeSmall`](#codesmall) | Folie | 41 |
| [`statement`](#statement) | Folie | 38 |
| [`question`](#question) | Folie | 29 |
| [`qa`](#qa) | Folie | 27 |
| [`image`](#image) | Folie | 16 |
| [`important`](#important) | Folie | 12 |
| [`shout`](#shout) | Folie | 7 |
| [`cite`](#cite) | Folie | 7 |
| [`simpleInterlude`](#simpleinterlude) | Folie | 5 |
| [`niceToKnow`](#nicetoknow) | Baustein | 2 |
| [`splitView`](#splitview) | Folie | 1 |
| [`text`](#text) | Baustein | 0 |

### screenshot

`{% screenshot src, props %}`: Bild zentriert auf hellem Grund, mit Schatten und Bildunterschrift. Das Arbeitspferd.

```
{% screenshot "./images/zielgruppe-medikamente.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Für wen ist das? Woran sehen Sie das?"}' %}
```

Props: `transition`, `backgroundTransition`, `classes`, `width`, `bu`, `badge`. Siehe [Props und Klassen](#props-und-klassen).

### screenshotFs

`{% screenshotFs src, props %}`: Bild als bildschirmfüllender Hintergrund, Bildunterschrift als Kasten.

```
{% screenshotFs "./images/translate-canvas-1.png", '{"transition":"fade", "bu":"Wir verschieben und skalieren den Canvas auf die Größe des Screens."}' %}
```

Props: `transition`, `backgroundTransition`, `classes`, `bu` (Markdown), `badge`. `width` wirkt hier nicht.

### image

`{% image src, props %}`: wie `screenshot`, ohne die Klasse `screenshot` (eigenes Layout, kein `backgroundTransition`).

```
{% image "./images/hfg-triade.jpg", '{"transition":"fade", "classes":"no-shadow", "bu":"HfG Ulm"}' %}
```

### interlude

`{% interlude title, subtitle, transition %}`: Kapiteltrenner mit zufälliger Hintergrundfarbe (Blau, Pink, Grün, Lila, Schwarz). Der Untertitel wird verzögert eingeblendet.

```
{% interlude "Für wen ist das?", "Funktion & Zielgruppe" %}
{% interlude "Für wen ist das?", "Funktion & Zielgruppe", "zoom" %}
```

Das dritte Argument ist ein einfacher String. Aus älteren Folien wird auch JSON akzeptiert (`'{"transition":"zoom"}'`).

### statement

`{% statement title, content, props %}`: Merksatz. Der Titel steht groß, `content` erscheint als Fragment darunter.

```
{% statement "Wir gestalten fast nie für uns selbst.", "Die erste Frage ist nicht »Wie sieht es aus?«, sondern »Wofür und für wen?«" %}
```

Props: `backgroundTransition`.

### question

`{% question question, tagline, props %}`: Frage ans Publikum, auch für Arbeitsaufträge mit Zeitangabe.

```
{% question "Welches Plakat funktioniert am besten?", "Einigen Sie sich zu zweit auf einen Favoriten. Und warum?" %}
{% question "Schreiben", "7 Minuten. Nur Text, keine Skizzen." %}
```

Props: `classes`, z. B. `align-left` (linksbündig) oder `fit-text` (Titel an Breite anpassen).

### qa

`{% qa question, answer, props %}`: Frage, darunter die Antwort als Fragment.

```
{% qa "Was ist ein System?", "A group of things that are connected or work together.<br><small>Cambridge Dictionary</small>" %}
```

Props: `transition`, `classes`. Die Antwort wird als rohes HTML ausgegeben, Markdown wirkt hier nicht.

### simpleText

`{% simpleText title, text, transition, props %}`: Text-Folie mit optionaler Überschrift (`false` = ohne).

```
{% simpleText "Headline", "Text mit **Auszeichnung**." %}
{% simpleText "Headline", "Text", "fade", '{"classes":"text-with-list"}' %}
```

Props: `classes` (z. B. `text-with-list`, `image-right`), `badge`, `image` (Bildpfad, wird neben dem Text gezeigt), `backgroundTransition`. Die Transition ist das dritte Argument als String. Steht dort stattdessen ein Props-JSON (`'{"transition":"slide"}'`), wird es als Props gelesen.

### simpleInterlude

`{% simpleInterlude title, text, transition %}`: Text-Folie mit Interlude-Hintergrund.

```
{% simpleInterlude "Pause", "Zehn Minuten." %}
```

### important

`{% important content, props %}`: einzelne zentrale Aussage, groß.

```
{% important "Smartphone, Server, Baum, Werkzeugkiste und Flugzeug" %}
```

Props: `badge`.

### shout

`{% shout title, author, source, info, transition %}`: Ausruf mit Autor, Quelle und aufklappbarer Zusatzinfo. Nur der Titel ist Pflicht.

```
{% shout "You have 50 milliseconds to make a good first impression!", "Gitte Lindgaard", "Behaviour & Information Technology, 2006", "", "fade" %}
```

### cite

`{% cite text, author, props %}`: Zitat, optional mit Autor (Markdown). Die Anführungszeichen « » setzt das CSS, also keine eigenen setzen.

```
{% cite "Man kann nicht nicht kommunizieren." %}
{% cite "Die Grenzen meiner Sprache bedeuten die Grenzen meiner Welt.", "Ludwig Wittgenstein" %}
```

Props: `badge`. Zitat mit Hintergrundbild und ausführlicher Quelle: als eigene Datei mit `slideClasses: cite`, siehe [Beispiel](#cite-als-eigene-datei).

### codeSmall

`{% codeSmall title, content, code, lang, transition %}`: Überschrift, erklärender Text (Markdown) und hervorgehobener Code.

```
{% codeSmall "Hello World", "Kleines Beispiel", "<h1>Hello World</h1>", "html" %}
```

Mehrere Code-Spalten nebeneinander: Statt `code` ein Array übergeben (Code aus Front-Matter-Variablen):

```
{% codeSmall "Nesting", text1, [{code: code, lang: "html"}, {code: code2, lang: "css"}], "", "fade" %}
```

Sprachen: alles, was highlight.js kennt (`html`, `css`, `javascript`, `json`, `bash` …). Ein Kommentar `/**/` im Code wird als sichtbarer Umbruch-Marker dargestellt.

### splitView

`{% splitView title, content %}`: Titel und Text nebeneinander.

```
{% splitView "Kommunikation", "communicare: teilen, mitteilen, teilnehmen lassen" %}
```

### fragment

`{% fragment content %}`: Baustein, der beim Weiterklicken eingeblendet wird. Wird in `simple`-Dateien, in `<section class="simple">` und in Intros verwendet. Der Standard für Aufzählungen:

```
{% fragment '<p class="list">Für wen gestalten wir eigentlich?</p>' %}
{% fragment '<p class="list">Ein Raster, das Sie das ganze Semester begleitet</p>' %}
```

Ohne `class="list"` erscheinen Absätze ohne Aufzählungszeichen (z. B. für eine Zusammenfassung).

### niceToKnow

`{% niceToKnow content %}`: Baustein für eine Randnotiz (Markdown).

```
{% niceToKnow "Die Mike Rode Matrix nutzt das Konzept des [Morphologischen Kastens](https://refa.de/…)." %}
```

### text

`{% text content %}`: hüllt beliebigen Inhalt in ein `<div>`.

## Props und Klassen

### Props für `screenshot`, `screenshotFs`, `image`

| Prop | Wirkung |
| :--- | :--- |
| `transition` | Übergang zu dieser Folie. Standard: `fade`. |
| `backgroundTransition` | Übergang des Hintergrunds (`screenshot`, `screenshotFs`). Standard: `fade`. |
| `classes` | Zusätzliche Klassen, durch Leerzeichen getrennt (siehe unten). |
| `width` | `width`-Attribut des Bildes, meist `"auto"`, sonst z. B. `"40%"`. |
| `bu` | Bildunterschrift (Markdown/HTML). |
| `credit` | Bildnachweis unter der Bildunterschrift, klein (Markdown/HTML): `"credit":"[Arngren Electronics](https://www.arngren.net/)"` |
| `alt` | Alternativtext (`screenshot`, `image`). Ohne Angabe wird der Text der `bu` verwendet. Wenn die `bu` eine Frage ist (»Und hier?«), sollte `alt` beschreiben, was zu sehen ist. |
| `badge` | Badge oben auf der Folie (Markdown/HTML), z. B. `"must have"`. |

### Klassen für Folien und HTML

**Bild-Folien** (`classes` in Props):

| Klasse | Wirkung |
| :--- | :--- |
| `no-shadow` | Kein Schatten ums Bild. Für Grafiken, Freisteller, Plakate. |
| `shadow` | Keine eigene Regel, der Schatten ist Standard. Dient nur der Lesbarkeit. |
| `has-dark-bg` / `has-black-bg` | Dunkler bzw. schwarzer Folienhintergrund. |
| `large-text` | Größere Bildunterschrift. |
| `full-height` | Bildunterschrift über die volle Höhe, vertikal zentriert. |
| `frameless` | Bildunterschrift als Spalte links (33 %). |
| `invert` | Bildunterschrift hell auf dunkel. |
| `is-dark` | Dunkle Bildunterschrift-Variante (z. B. bei Inline-SVG auf grauem Grund). |

**Text-Folien** (`simpleText`, `question`):

| Klasse | Wirkung |
| :--- | :--- |
| `text-with-list` | Abstände für Text plus Liste (`simpleText`). |
| `image-right` | Text links, Bild (Prop `image`) rechts (`simpleText`). |
| `align-left` | Linksbündig (`question`). |
| `fit-text` | Titel passt sich der Breite an (`question`). |

**Allgemeine Hilfsklassen** (in HTML oder `additionalClasses`):

| Klasse | Wirkung |
| :--- | :--- |
| `list` | Absatz mit Aufzählungszeichen: `<p class="list">`. |
| `content-blocks` | Textkästen auf Vollbild-Hintergrund, siehe [Text auf Bild](#text-auf-bild). |
| `is-full-width` | Volle Breite (Intro). |
| `is-fullscreen`, `is-centered`, `is-stacked` | Vollbild, zentriert, Spalte. |
| `has-whitener` | Weißer, leicht transparenter Kasten. |
| `has-gap` | Großer Abstand oben und unten. |
| `is-small` | Kleinere Schrift. |
| `is-purple`, `is-green`, `is-blue` | Textfarben. |
| `js-delay` | Element wird verzögert eingeblendet. |
| `js-fit-text` | Text wird per JavaScript in die Breite eingepasst. |

## Inhalte aus dem Front Matter an Shortcodes übergeben

Längere Texte, Code oder Listen sind als String-Argument unhandlich. Man legt sie als Variable im Front Matter ab und übergibt die Variable ohne Anführungszeichen:

```
---
title: Fit Canvas to Screen Size
layout: presentation.11ty.js
slideClasses: wrap
transition: slide
status: ok
canvasText: |
  This code adjusts the canvas based on the browser window's position on the screen.
canvasCode: |
  function draw() {
    background(0, 0, 0, 100);
    ellipse(posX, posY, 60, 60);
  }
---

{% interlude "Time to assemble.", "Share Window Data Concepts & p5.js" %}

{% codeSmall "Fit Canvas to Screen Size", canvasText, canvasCode, "javascript", "slide" %}
```

Das funktioniert für alle Argumente, auch für `fragment`-Inhalte (`{% fragment ziel1 %}`) und Bildpfade.

## HTML-Bausteine

Wo es keinen passenden Shortcode gibt, wird HTML direkt geschrieben. Jede `<section>` ist eine eigene Folie und gehört in eine `wrap`- oder `images`-Datei. Shortcodes funktionieren auch innerhalb von HTML.

### Text-Folie mit Fragmenten

Wird gebraucht, wenn ein Kapitel mitten im Ablauf eine Anleitung oder Liste zeigen soll:

```html
<section class="simple" data-transition="fade">
  <div>
    <h1>So geht's</h1>
    {% fragment '<p class="list">Zu zweit. Links: Screen A, rechts: Screen B. Nicht spicken!</p>' %}
    {% fragment '<p class="list"><strong>7 Min.</strong> Screen schriftlich beschreiben.</p>' %}
  </div>
</section>
```

### Bild mit Bildnachweis

Mit Shortcode: `{% screenshot "./images/messy-website.jpg", '{"classes":"no-shadow", "bu":"Wie ist die Hierarchie der Elemente?", "credit":"[Arngren Electronics](https://www.arngren.net/)", "alt":"Überladene Website mit vielen Produktbildern"}' %}`. Als HTML:


```html
<section class="image screenshot no-shadow" data-transition="fade">
  <figure>
    <img src="./images/messy-website.jpg" alt="Überladene Website mit vielen Produktbildern">
    <figcaption class="bu">
      <p>Wie ist die Hierarchie der Elemente?</p>
      <p class="credit"><a href="https://www.arngren.net/" target="_blank">Arngren Electronics</a></p>
    </figcaption>
  </figure>
</section>
```

### Vollbild-Bild mit Bildnachweis

```html
<section class="image is-fullscreen" data-background="./images/viel-zu-tun.jpg">
  <div class="bu">
    <p>Viel zu tun</p>
    <p class="credit"><a href="[url]" target="_blank">Iwona Castiello d'Antonio</a> // <a href="[url]" target="_blank">Unsplash</a></p>
  </div>
</section>
```

### Text auf Bild

```html
<section class="image is-fullscreen" data-transition="fade" data-background-transition="fade" data-background="./images/map-cologne.jpg">
  <div class="is-centered">
    <div class="content-blocks">
      {% fragment '<p>Mit zunehmendem Abstand erscheinen uns Dinge:</p>' %}
      {% fragment '<p class="list">kleiner</p>' %}
      {% fragment '<p class="list">mit weniger Kontrast</p>' %}
    </div>
  </div>
</section>
```

### Inline-SVG

Für Demonstrationen, die sich Schritt für Schritt verändern. Mit `data-auto-animate` und gleicher `data-id` animiert reveal.js zwischen zwei Folien.

```html
<section data-auto-animate class="image screenshot" data-transition="fade" data-background-color="#666">
  <figure>
    <svg data-id="frame" height="600" width="600">
      <rect x="0" y="0" width="600" height="600" fill="#ffffff" />
      <circle cx="80" cy="100" r="20" fill="#000000" />
    </svg>
    <figcaption class="bu is-dark"><p>Zufall oder Gestaltung?</p></figcaption>
  </figure>
</section>
```

### Video

```html
<section class="video">
  <figure>
    <iframe width="560" height="315" src="[src]" title="YouTube video player" frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <figcaption class="bu"><p>Kleiner Aufmerksamkeitstest</p></figcaption>
  </figure>
</section>
```

## Ein komplettes Beispiel

Ein kleines Deck nach dem aktuellen Muster, Vorbild: [design-in-der-medieninformatik](src/presentations/screendesign/design-in-der-medieninformatik).

### `000-intro.md`

```
---
title: Design in der Medieninformatik
layout: presentation.11ty.js
slideClasses: intro
transition: zoom
---

<div class="is-full-width">

# Design in der Medieninformatik

## Gutes Auge, präzise Sprache

</div>
```

Ein Zitat als Untertitel: `## Gute Typografie erklärt den Inhalt. Nicht den Gestalter.<br><small>Kurt Weidemann</small>`

### `010-heute.md`

```
---
title: Heute
layout: presentation.11ty.js
slideClasses: simple
status: ok
---

{% fragment '<p class="list">Für wen gestalten wir eigentlich?</p>' %}
{% fragment '<p class="list">Wie beschreiben wir einen Screen präzise?</p>' %}
```

### `020-fuer-wen.md`

```
---
title: Für wen ist das?
layout: presentation.11ty.js
slideClasses: images
status: ok
transition: zoom
speaker: |
  **Ratespiel (ca. 10 Minuten)**

  Pro Bild 30 Sekunden zu zweit: Zielgruppe in drei Stichworten plus **ein** visuelles Indiz.

  **Kernaussage:** Erst Funktion und Zielgruppe, dann die Form.
---

{% interlude "Für wen ist das?", "Funktion & Zielgruppe" %}

{% screenshot "./images/zielgruppe-medikamente.png", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Für wen ist das? Woran sehen Sie das?"}' %}

{% screenshot "./images/zielgruppe-zahnbuersten.png", '{"transition":"fade", "classes":"no-shadow", "width":"auto", "bu":"Gleiche Funktion. Was ist der Unterschied?"}' %}

{% statement "Wir gestalten fast nie für uns selbst.", "Die erste Frage ist nicht »Wie sieht es aus?«, sondern »Wofür und für wen?«" %}
```

### `030-merksatz.md`

```
---
title: Identität
layout: presentation.11ty.js
slideClasses: statement
status: ok
---

ist das Prinzip, durch das sich ein Ding von allen anderen unterscheidet.
```

### Cite als eigene Datei

```
---
title: Watzlawick
layout: presentation.11ty.js
slideClasses: cite
img: paul
author: Paul Watzlawick
src: "Watzlawick, Paul (2016): Man kann nicht nicht kommunizieren. Bern: Hogrefe."
status: ok
---

Man kann nicht nicht kommunizieren.
```

### `index.md`

```
---
title: Design in der Medieninformatik
layout: presentation.11ty.js
slideClasses: outro
transition: convex
---
```

## Präsentieren

| Taste/Aktion | Wirkung |
| :--- | :--- |
| Leertaste, Pfeiltasten | Weiter/zurück (auch durch die vertikalen Folien eines Kapitels) |
| `i` | Speaker Notes direkt auf der Folie ein-/ausblenden |
| `S` | reveal.js-Speaker-View |
| `Esc` / `O` | Übersicht |
| Doppelklick auf ein Bild | Bild zoomen |
| Klick auf `info` (shout) | Zusatzinfo einblenden |
| Code-Block | Button zum Kopieren in die Zwischenablage |

PDF: `?print-pdf` an die URL hängen und im Browser drucken.

## Bekannte Macken

Diese Punkte sind im Code so, die Doku beschreibt den Ist-Zustand:

- `important` ignoriert eine Transition, `statement` kennt nur `backgroundTransition`.
- `qa` gibt die Antwort roh aus, Markdown wird nicht umgesetzt.
- Die `index.md` wird als letzte Folie gerendert (siehe [`index.md`](#indexmd)).
- Sortierung als String (siehe [Dateinamen](#dateinamen-und-reihenfolge)).

## Legacy

Ältere Decks verwenden Arbeitsweisen, die weiterhin funktionieren, für neue Folien aber **nicht mehr bevorzugt** werden.

### Eine Datei pro Folie

Jede Folie ist eine eigene `.md`-Datei, Bilder werden per HTML-Section in `slideClasses: images` eingebunden (z. B. `screendesign/barrierefreiheit`, `screendesign/ausrichtung-von-designprojekten`). Neue Folien besser als Kapitel-Datei mit Shortcodes anlegen.

### Hintergrundbild per Front Matter

`img`, `imgData` und `credits` setzen ein Hintergrundbild für die ganze Datei. Heute meist durch `screenshotFs` ersetzt. Bei `cite` weiterhin üblich.

### Ein-Datei-Decks (`version: 1`)

Ein Deck als *eine* Markdown-Datei, Folien durch `---` getrennt, Folientyp per Zeile `slide-is:<typ>` (z. B. `misc/jam-stack`). Setzt `version: 1` im Front Matter der `index.md` voraus. Noch ältere Dateien mit `separator`/`verticalSeparator`/`revealOptions` stammen aus reveal-md (`bachelor/mi-wtw-kickoff`).

### impress.js

`layout: impress.11ty.js` (z. B. `misc/impress`, `misc/programmierung-in-der-gestaltung`). Styles in `src/assets/styles/scss/impress.scss`.

## Projekt, Build und Deployment

### Befehle

| Befehl | Wirkung |
| :--- | :--- |
| `npm install` | Abhängigkeiten installieren |
| `npm run dev` | SASS im Watch-Mode + 11ty-Dev-Server mit Live-Reload |
| `npm run quiet` | wie `dev`, weniger Konsolenausgabe |
| `npm run build` | Build (CSS + Seite) in den Ordner `docs` |
| `npm run live` | Build und Webserver für `docs` |
| `npm run lint:css` / `lint:css:fix` | stylelint |
| `npm run lint:js` / `lint:js:fix` | eslint |

### Deployment

Bei jedem Push auf `main` baut der Workflow [.github/workflows/build.yml](.github/workflows/build.yml) das Projekt (`npm run build`) und veröffentlicht `docs` auf den Branch `gh-pages`. In Production wird der Pfad-Präfix `slides` gesetzt (`ELEVENTY_ENV=production`).

### Ordnerstruktur

```
docs                kompilierter Output, wird deployed, nichts von Hand ändern
reveal              reveal.js (unverändert)
impress.js          impress.js (unverändert)
static              statische Zusatzdateien
_archive            ausrangierte Stände
src                 hier wird entwickelt
├── _components     Includes
├── _data           Globale Daten & Helper (project.json, cacheBust.js …)
├── _layouts        Templates (presentation.11ty.js, impress.11ty.js, documents.11ty.js …)
├── assets          SCSS, Skripte, Fonts, Icons, Bilder
├── compiled-assets vom SASS-Compiler erzeugt (main.css)
├── presentations   Content: pro Kategorie ein Ordner, darin pro Deck ein Ordner
└── index.md        Übersichtsseite mit allen Decks
.eleventy.js        11ty-Config: Collections, Shortcodes, Passthrough-Copy
.eleventyignore     von 11ty ignorierte Ordner/Dateien
```
