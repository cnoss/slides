# Slides

HTML-Slidedecks für meine Vorlesungen. Das Projekt nutzt den Static-Site-Generator [11ty](https://www.11ty.dev/docs/) und als Präsentations-Framework [reveal.js](https://revealjs.com/) (Standard) sowie optional [impress.js](https://impress.js.org/).

Veröffentlicht unter [cnoss.github.io/slides](https://cnoss.github.io/slides/).

[Figma für Montagen](https://www.figma.com/design/xXM2JmJMAWsqoOJQyxqaqa/Slides?m=auto&t=ZhJbsnkuKr5jUWYC-1)

## Wie es funktioniert

Ein **Slidedeck ist ein Ordner** unter `src/presentations/<kategorie>/<deck>/`. Darin liegen:

- eine `index.md` als Einstiegspunkt (sie legt das Layout fest, üblicherweise `presentation.11ty.js`),
- und beliebig viele **nummerierte Einzelfolien** wie `000-intro.md`, `010-cite.md`, `020-…md`.

Beim Build sammelt das Layout alle `.md`-Dateien desselben Deck-Ordners ein, **sortiert sie nach Dateinamen** und fügt sie zu *einer* reveal.js-Präsentation zusammen. Die Zahlen-Präfixe steuern also die Reihenfolge der Folien – mit Lücken (000, 010, 020 …) lässt sich später bequem etwas dazwischenschieben.

Das Aussehen jeder Folie wird über das [Front Matter](#front-matter) (`slideClasses`, `transition`, `img` …) und über [Shortcodes](#shortcodes) gesteuert.

Die Übersichtsseite ([src/index.md](src/index.md)) listet alle Decks gruppiert nach den vier Kategorien (Sammlungen) **screendesign**, **master**, **bachelor** und **misc**.

## Deployment

Bei jedem Push auf `main` baut der GitHub-Actions-Workflow [.github/workflows/build.yml](.github/workflows/build.yml) das Projekt (`npm run build`) und veröffentlicht den `docs`-Ordner auf den Branch `gh-pages`. In Production wird der Pfad-Präfix `slides` gesetzt (über `ELEVENTY_ENV=production`).

## Ordnerstruktur

```
docs                kompilierter Output → wird deployed, hier nichts von Hand ändern
reveal              reveal.js (unverändert)
impress.js          impress.js (unverändert)
static              statische Zusatzdateien
_archive            ausrangierte Stände
src                 hier wird entwickelt (s.u.)
```

### `/src`

```
_components         Includes (Layout- oder Funktionsschnipsel)
_data               Globale Daten & Helper (project.json, cacheBust.js …)
_layouts            Templates (presentation.11ty.js, impress.11ty.js, documents.11ty.js …)
assets              SCSS, Skripte, Fonts, Icons, Bilder – alles, was kein Content ist
compiled-assets     Vom SASS-Compiler erzeugte Dateien (z.B. main.css)
presentations       Der Content: pro Kategorie ein Ordner, darin pro Deck ein Ordner
  ├── bachelor
  ├── master
  ├── misc
  └── screendesign
index.md            Übersichtsseite mit allen Decks
```

### Weitere Dateien
```
.eleventy.js        Config von 11ty (Collections, Shortcodes, Passthrough-Copy …)
.eleventyignore     Welche Ordner/Dateien soll 11ty ignorieren?
.stylelintrc.yaml   Config von stylelint
.gitignore          Welche Ordner/Dateien soll git ignorieren?
```

## Funktionen

`npm install`
Installiert die erforderlichen Abhängigkeiten.

`npm run dev`
Startet die Entwicklungsumgebung: SASS-Compiler im Watch-Mode plus 11ty-Dev-Server mit Live-Reload.

`npm run quiet`
Wie `dev`, aber mit weniger Konsolen-Ausgabe (`--quiet`).

`npm run build`
Kompiliert einen Build (CSS + Seite) in den `docs`-Ordner.

`npm run live`
Erzeugt einen Build und startet einen Webserver, der den `docs`-Ordner serviert.

`npm run lint:css` / `npm run lint:css:fix`
Startet stylelint (mit `:fix` werden Fehler nach Möglichkeit automatisch korrigiert).

`npm run lint:js` / `npm run lint:js:fix`
Startet eslint (mit `:fix` werden Fehler nach Möglichkeit automatisch korrigiert).

## Front Matter

Jede Folie (und die `index.md` des Decks) wird über Front Matter konfiguriert:

```
---
title: Vokabeln
layout: presentation.11ty.js
slideClasses: simple
status: ok
---
```

Weitere mögliche Felder pro Folie:

| Feld | Bedeutung |
| :--- | :--- |
| `title` | Titel der Folie bzw. des Decks |
| `layout` | Template – meist `presentation.11ty.js`, für impress.js `impress.11ty.js` |
| `slideClasses` | Folientyp, s. [Slide Classes](#slide-classes) |
| `transition` | reveal.js-Übergang, s. [Transition](#transition) |
| `status` | Sichtbarkeit / ToDo-Hinweis, s. [Status](#status) |
| `img` / `imgData` / `credits` | Hintergrundbild und dessen Quelle, s. [Image](#image) |
| `additionalClasses` | zusätzliche CSS-Klassen, s. [Additional Classes](#additional-classes) |
| `author` / `src` / `info` | Autor, Quelle und Zusatzinfo (z.B. bei `cite` und `shout`) |
| `speaker` | Speaker Notes (in reveal.js mit `S` aufrufbar) |
| `badge` | kleines Badge, das auf der Folie eingeblendet wird |

### Slide Classes

| SlideClass | Layout |
| :--- | :--- |
| [intro](https://cnoss.github.io/slides/presentations/misc/demo/) | Startfolie mit Titel und Untertitel |
| outro | Endfolie ohne Text |
| simple | Einfacher Inhalt mit Headline und Text |
| [cite](https://cnoss.github.io/slides/presentations/misc/demo/#/1) | Zeigt ein Zitat, mit oder ohne Hintergrundbild. |
| [images](https://cnoss.github.io/slides/presentations/misc/demo/#/3) | Wrapper Folie für Bilder, die dann via HTML eingebunden werden |
| [video](https://cnoss.github.io/slides/presentations/misc/demo/#/5) | Wrapper Folie für ein Video, welches dann via HTML eingebunden werden |
| [statement](https://cnoss.github.io/slides/presentations/misc/demo/#/6) | Aussage mit Erklärung |
| [shout](https://cnoss.github.io/slides/presentations/misc/demo/#/8) | Ausruf mit Autor und Erklärung auf Hintergrund |
| code | Zeigt schön formatierten Code auf der ganzen Fensterbreite.  |
| codeSmall | Zeigt schön formatierten Code so breit, wie der Code läuft.  |
| wrap | Wrapper Folio für Shortcodes |
| split | Bild links, Text rechts |
| question | kein Beispiel parat :( |
| qa | Frage und Antwort |

### Image
```
img: bildname
```

Url zu einem Hintergrundbild. Das Bild muss in `images` liegen. Bei *.jpg* Formaten kann die Endung weg gelassen werden.

```
imgData: {"position":"1% 1%", "size": "15%"}
```

```
credits: {'name': 'Unbekannt'}
credits: {'name': 'Barbara Iandolo', 'url':'https://link.de'}
```

Quelle des Bildes.

### Additional Classes
```
additionalClasses: is-green
```
- has-gap
- has-whitener
- has-dark-bg
- has-black-bg
- is-full-width
- is-fullscreen
- is-centered
- is-stacked
- js-fit-text
- js-delay
- is-purple
- is-green
- is-add-on-info

### Status

```
status: ok
```
| Wert | Aktion |
|:---|:---|
| ok | nichts passiert |
| hidden | Slide wird nicht angezeigt |
| alles andere | Status wird oben rechts in der Folie angezeigt. Ganz praktisch für Todos oder so |

### Transition
```
transition: slide
```

Hier sind alle [Reveal.js Transitions](https://revealjs.com/transitions/) möglich:
- none
- fade
- slide
- convex
- concave
- zoom

## Shortcodes

Shortcodes erzeugen fertige Folien oder Bausteine direkt im Markdown. Sie sind in [.eleventy.js](.eleventy.js) definiert.

### Fragment
```
{% fragment "<h2>Team</h2><p>Calvin Hinzer, Christian Hahn, Volker Schaefer, Christian Noss</p>" %}
```

### SimpleText
Erzeugt einen kompletten Screen. Headline kann auch `false` sein.
```
{% simpleText "Headline", "Text" %}
```

### SimpleTextInterlude
Erzeugt einen kompletten Screen mit anderem Hintergrund. Headline kann auch `false` sein.
```
{% simpleInterlude "Headline", "Text" %}
```


### Question
Erzeugt einen kompletten Screen.
```
{% question "Was guckst Du?" %}
```

### Question and Answer
Erzeugt einen kompletten Screen.
```
{% qa "Was ist ein System?", "A group of things, pieces of equipment, etc. that are connected or work together.<br><small>Cambridge Dictionary</small>" %}
```

### CodeSmall
Erzeugt einen kompletten Screen.
```
{% codeSmall "Title", "Text", "Code", "Sprache" %}
{% codeSmall "Hello World", "kleines Beispiel", "<h1>Hello World</h1>", "html" %}
```

### Important
```
{% important "Smartphone, Server, Baum, Werkzeugkiste und Flugzeug" %}
```

### Interlude
Erzeugt einen kompletten Screen.
```
{% interlude "Lean back", "Lean forward"%}
```

### Nice to Know
```
{% niceToKnow "Die Mike Rode Matrix nutzt übrigens das Konzept des [Morphologischen Kastens](https://refa.de/service/refa-lexikon/morphologischer-kasten)." %}
```

### Cite
```
{% cite "Man kann nicht nicht kommunizieren." %}
```

### Text
Hüllt beliebigen Inhalt in einen `<div>`.
```
{% text "<p>Beliebiger HTML-Inhalt</p>" %}
```

### Image
```
{% image "./images/hfg-triade.jpg", '{"transition":"fade", "classes":"no-shadow", "bu":"https://www.hfg-gmuend.de/hochschule/geschichte"}' %}
```


### Screenshot
```
{% screenshot "./images/brain.jpg", '{"transition":"fade", "classes":"no-shadow", "width":"20%", "bu":"Davon muss ich mir erst mal ein Bild machen."}' %}

{% screenshot "./images/brain.jpg",  '{"transition":"fade", "classes":"no-shadow large-text full-height", "bu":"Kleine BU"}' %}
```


### Fullscreen Screenshot
Erzeugt einen kompletten Screen.
```
{% screenshotFs "./images/brain.jpg", '{"transition":"fade", "classes":"no-shadow", "width":"20%", "bu":"Davon muss ich mir erst mal ein Bild machen."}' %}
```

### Shout
Erzeugt einen lauten Ausruf. Alle anderen Angaben außer dem Titel sind optional.

```
{% shout "Titel", "autor", "quelle", zusatzinfo, '{"backgroundTransition":"slide"}' %}
```

### Statement
```
{% statement "Kräfte", "Auf Linien in einer Gestaltung wirken folgende *Kräfte*.", '{"backgroundTransition":"slide"}' %}
```

### Split View

```
{% splitView "Kommunikation", "communicare: teilen, mitteilen, teilnehmen lassen", '{"backgroundTransition":"slide"}' %}
```

## HTML

### Bilder, Variante 1

```

<section class="image is-fullscreen" data-background="./images/[src]">
  <div class="bu">
    <p>Viel zu tun</p>
    <p class="credit">
      <a href="[url]" target="_blank">Iwona Castiello d'Antonio</a> // <a href="[url]" target="_blank">Unsplash</a></p>
  </div>
</section>

```

### Bilder, Variante 2

```
<section class="image screenshot">
  <figure>
    <img src="./images/messy-website.jpg">
    <figcaption class="bu">
      <p>Viel zu tun</p>
      <p class="credit">
        <a href="https://www.arngren.net/" target="_blank">Arngren Electronics</a>
      </p> 
    </figcaption>
  </figure>
</section>
```
### Inline SVG

```
<section data-auto-animate class="image screenshot" data-transition="fade" data-background-color="#666">
  <figure>
    <svg data-id="frame" height="600" width="600">
      <rect x="0" y="0" width="600" height="600" fill="#ffffff" />
      <circle cx="80" cy="100" r="20" fill="#000000" />
      <circle cx="220" cy="80" r="20" fill="#000000" />
      <circle cx="480" cy="380" r="20" fill="#000000" />
    </svg>
    <figcaption class="bu is-dark">
      <p>Zufall oder Gestaltung?</p>
    </figcaption>
  </figure>
</section>
```

### Video

```
<section class="video">
  <figure>
    <iframe width="560" height="315" 
        src=[src]" title="YouTube video player" 
        frameborder="0" allow="accelerometer; autoplay; 
        clipboard-write; encrypted-media; gyroscope; 
        picture-in-picture" allowfullscreen></iframe>
    <figcaption class="bu">
      <p>kleiner Aufmerksamkeitstest</p>
    </figcaption>
  </figure>
</section>
```

### Text in Bild 

```
<section class="image is-fullscreen" data-transition="fade"  data-background-transition="fade" data-background="./images/map-cologne.jpg">
  <div class="is-centered">
    <div class="content-blocks">
      {% fragment "<p>Mit zunehmendem Abstand erscheinen uns Dinge:</p>" %}
      {% fragment "<p class=\"list\">kleiner</p>" %}
      {% fragment "<p class=\"list\">mit weniger Kontrast</p>" %}
      {% fragment "<p class=\"list\">mit weniger warmen und gesättigten Farben</p>" %}
    </div>
  </div>
</section>
```


### Screenshot

```
<section class="image screenshot">
  <figure>
    <img src="./images/kronen-zeitung.jpg">
    <figcaption class="bu">
      <p>Wie ist die Hierarchie der Elemente?</p>
     <p class="credit">
        <span>Kronenzeitung (2021)</span> // 
        <a href="https://epaper.krone.at" target="_blank">epaper.krone.at</a>
    </p>
    </figcaption>
  </figure>
</section>
```

## Beispiele

### Intro

```
---
title: Wahrnehmungsarbeit
layout: presentation.11ty.js
slideClasses: intro
transition: zoom
---

<div class="is-full-width">

# Demo Präsentation
## Hier sieht man die verschiedenen Slidetypen und Shotcodes im Einsatz

</div>
```

### Cite 

```
---
title: Cite
layout: presentation.11ty.js
slideClasses: cite
author: Max Mustermann, Beispiel
---

Hier wird ein Zitat hübsch angezeigt.
```

### Cite with Image

```
---
title: Cite with Image
layout: presentation.11ty.js
slideClasses: cite
img: paul
author: Max Mustermann, Beispiel
status: ok
src: "Watzlawick, Paul (2016): Man kann nicht nicht kommunizieren. Das Lesebuch. 2., unveränderte Auflage. Hg. v. Trude Trunk. Bern: Hogrefe. Online verfügbar unter http://d-nb.info/1079675604/04."
---

Cite. Diesmal mit Bild, was im Front Matter angegeben werden kann. Gleiches gilt für die Quelle.

```

### Images
```
---
title: Bilder wo et voll ist
layout: presentation.11ty.js
slideClasses: images
status: ok
---

<section class="image is-fullscreen" data-background="./images/time-square.jpg.jpg" data-background-position="bottom">
…
</section>
```

### Shout

```
---
title: Gitte Lindgaard
layout: presentation.11ty.js
slideClasses: shout
author: Gitte Lindgaard, Psychologin
src: "Lindgaard, G., Fernandes, G., Dudek, C. & Brown, J. (2005). Attention web designers: You have 50 milliseconds to make a good first impression! Behaviour & Information Technology (in Press)."
status: ok
info: "Three studies were conducted to ascertain how quickly people form an opinion about web page visual appeal and its relation to several design features. In the first study, 22 participants twice rated the visual appeal of web pages presented for 500msecs each. Thirty-one participants took part in the second study, which replicated the first, but participants also rated each web page on seven design dimensions. Visual appeal was found to be closely related to several design features.<br><br>Forty participants took part in study 3, which replicated studies 1 and 2, but employed a 50msec condition to allow comparisons between exposure times. Throughout, visual appeal ratings were highly correlated from one trial to the next as were the correlations between the 50msec and 500msec conditions. <br><br>Thus, visual appeal is assessed within 50msecs. These findings suggest that web designers have about 50msecs to make a good first impression."
---

Attention (web) designers: you have 50 milliseconds to make a good first impression!

```

### Code & CodeSmall

```
---
title: View Transitions
layout: presentation.11ty.js
slideClasses: codeSmall
transition: fade
status: ok
---

## Step 2
Adding css-at-Rule. For a cross-document view transition to work, the current and destination documents of the navigation also need to be on the same origin […](https://developer.mozilla.org/en-US/docs/Web/CSS/@view-transition)


<pre>
<code>
@view-transition {
  navigation: auto;
}
</code>
</pre>
```
