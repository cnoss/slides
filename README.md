# Slides

HTML Slidedecks für meine Vorlesungen. Das Projekt nutzt den Static Page Generator [11ty](https://www.11ty.dev/docs/) und [reveal.js](https://revealjs.com/).

## Ordnerstruktur

### `/docs`
kompilierter Code … hier wird nix gemacht

### `/reveal`
Hier lebt Reveal.js und es muss nix gemacht werden.

### `/src` hier wird entwickelt

```
_components         Layout- oder Funktionsschnipsel
_data               Zusätzliche Daten oder Hilffunktionen
_layouts            Templates
assets              SCSS, Skripts, Fonts, etc … alles was kein Content ist
compiled-assets     Kompilierte Dateien, z.B. CSS
presentations       Content, und zwar pro Slidedeck ein Ordner
```

### Weitere Dateien
```
.eleventy.js        Config von 11ty
.eleventyignore     Welche Folder/ Files soll 11ty ignorieren?
.eslintrc.json      Config von eslint
.gitignore          Welche Folder/ Files soll git igorieren?
.stylelintrc.json   Config von stylelint
```

## Funktionen

`npm install`
Installiert die erforderlichen Abhängigkeiten.

`npm run build` 
kompiliert einen Build und speichert diesen im `docs` Folder.

`npm run dev` 
Watchmode für den SASS Compiler und Browsersync, der die Inhalte inkl. livereload serviert.

`npm run live` erzeugt einen Build und startet den Webserver, der die Inhalte serviert.

`npm run lint:css` startet stylelint.

`npm run lint:css:fix` startet stylelint und korrigiert die Fehler, sofern möglich.

`npm run lint:js` startet eslint.

`npm run lint:js:fix` startet eslint und korrigiert die Fehler, sofern möglich.

## Front Matter

```
---
title: Vokabeln
layout: presentation.11ty.js
slideClasses: simple
status: ok
---
```

### Slide Classes

| SlideClass | Layout |
| :--- | :--- |
| [intro](https://cnoss.github.io/slides/presentations/misc/demo/) | Startfolie mit Titel und Untertitel |
| outro | Endfolie ohne Text |
| simple | Einfacher Inhalt mit Headline und Text |
| [cite](https://cnoss.github.io/slides/presentations/misc/demo/#/1) | Zeigt ein Zitat, mit oder ohne Hintergrundbild. |
| [images](https://cnoss.github.io/slides/presentations/misc/demo/#/3) | Wrapper Folie für Bilder, die dann via HTML eingebunden werden |
| [video](https://cnoss.github.io/slides/presentations/misc/demo/#/5) | Wrapper Folie für ein Video, welches dann via HTML eingebunden werden |
| [statement](https://cnoss.github.io/slides/presentations/misc/demo/#/6) | Aussage mit Erklärung |
| [shout](https://cnoss.github.io/slides/presentations/misc/demo/#/8) | Ausruf mit Autor und Erklärung auf Hintergrund |
| wrap | Wrapper Folio für Shortcodes |
| question | kein Beispiel parat :( |
| qa | Frage und Antwort |

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

|:---|:---|
| ok | nichts passiert |
| hidden | Slide wird nicht angezeigt |
| alles andere | Status wird oben rechts in der Folie angezeigt. Ganz praktisch für Todos oder so |

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

### Fragment
```
{% fragment "<h2>Team</h2><p>Calvin Hinzer, Christian Hahn, Volker Schaefer, Christian Noss</p>" %}
```

### Question
```
{% question "Was guckst Du?" %}
```

### Question and Answer
```
{% qa "Was ist ein System?", "A group of things, pieces of equipment, etc. that are connected or work together.<br><small>Cambridge Dictionary</small>" %}
```

### Important
```
{% important "Smartphone, Server, Baum, Werkzeugkiste und Flugzeug" %}
```

### Interlude
```
{% interlude "Lean back", "Lean forward"%}
```

### Nice to Know
```
{% niceToKnow "Die Mike Rode Matrix nutzt übrigens das Konzept des [Morphologischen Kastens](https://refa.de/service/refa-lexikon/morphologischer-kasten)." %}
```

### Screenshot
```
{% screenshot "./images/brain.jpg", '{"transition":"fade", "classes":"no-shadow", "width":"20%", "bu":"Davon muss ich mir erst mal ein Bild machen."}' %}
```

### Statement
```
{% statement "Kräfte", "Auf Linien in einer Gestaltung wirken folgende *Kräfte*.", '{"backgroundTransition":"slide"}' %}
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
