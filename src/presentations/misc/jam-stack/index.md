---
title: Developing a Community Website on JAMstack with GIT Managed Content and a Isomorphic Rendering Approach
revealOptions:
  transition: 'slide'
  backgroundTransition: 'fade'
  center: false
---

slide-is:image-fullscreen images/header-illustration-bg.svg

---

slide-is:welcome
# Case Study: Developing a Community Website on JAMstack with GIT Managed Content and a Isomorphic Rendering Approach
oder: eine kleine Reise in die Welt des Unwissens

___

slide-is:interlude
## Wie bin ich auf diesen Titel gekommen???
lang, falsch, unverständlich und in der falschen Sprache :/

---

slide-is:interlude
## Christian Noss
Web-(designer|developer|enthusiast) seit … öhm

---

slide-is:simple
## Disclaimer

- Sichtweisen und Kontexte sind eher persönlich
- Sachverhalte sind oft verkürzt dargestellt
- Schlüsse sind zugunsten der Prägnanz oft plakativ

---

slide-is:interlude
## Wen könnte das Thema interessieren?


___

slide-is:welcome
# **Developing a** Community **Website** on JAMstack with GIT Managed Content and a Isomorphic Rendering Approach
irgendwo zwischen **informationsgetriebener Website(z.B. Wikipedia)** und funktionsgetrieber Web-App (z.B. Gmail, Spotify)

---

slide-is:interlude
## Dem Kunden/ User möglichst schnell und gut strukturiert die gesuchten Informationen ausliefern.
Ziel

--- 

slide-is:simple
## 1993

HTML & VIM, Webserver, Telnet, Mosaic > __Seite funktioniert: Waaaaahnsinn!!__

> Kernfrage: läuft die Seite?

---

slide-is:simple
## 1998

HTML, CSS, ~~VIM~~ BBedit, ~~Mosaic~~ Netscape Navigator, Webserver, FTP, Telnet, CGI/Perl > __Seite funktioniert und sieht irgendwie gut aus: yeeeeaaaah!!__

> Kernfragen: laufen die Skripte und sieht die Seite gut aus?


---


slide-is:simple
## 2003

~~HTML~~ XHTML, CSS, Javascript, DHTML oder Flash, BBedit, ~~Netscape Navigator~~ Internet/Explorer/Safari/Firefox, Webserver(Produktiv), Webserver(Dev), SFTP, SSH, ~~CGI/Perl~~ PHP, CMS(Produktiv), CMS(Dev), (My)SQL-DB(Produktiv), (My)SQL-DB(Dev), SVN > __Seite funktioniert, sieht auf verschiedenen Browsern korrekt aus, hat coole grafische Effekte, Kunde versteht das CMS, PHP Skripte laufen, JS Skripte laufen auch im IE, Seite ist barrierefrei, Code ist valide und wohlgeformt, Sync vom Dev ins Live System funktioniert, WebMetrics laufen: yeah!__

> Kernfrage: Findet der Google Bot die Seiten? 

---

slide-is:simple
## 2008

XHTML, CSS, Javascript, script.aculo.us, ~~Flash~~, ~~VIM BBedit~~ Sublime, AJAX, ~~Mosaic Netscape Navigator~~ Chrome/Internet Explorer/Safari/Firefox, iPhone, Webserver(Produktiv), Webserver(Staging), Webserver(Dev), SFTP, SSH, PHP, Code-Ignitor, CMS(Produktiv), CMS(Dev), (My)SQL-DB(Produktiv), (My)SQL-DB(Dev), SVN > __Seite funktioniert, sieht auf verschiedenen Browsern korrekt aus, hat coole grafische Effekte, Kunde versteht das CMS, PHP Skripte laufen, JS Skripte laufen auch im IE, Seite ist barrierefrei, Code ist valide und wohlgeformt, Sync vom Dev ins Live System funktioniert, Site wird von Google indiziert, WebMetrics laufen, Seite funktioniert irgendwie auch auf dem iPhone: yeah!__

> Kernfragen: Läuft die Seite auf dem iPhone vom Chef halbwegs?

---

slide-is:simple
## 2013

~~HTML XHTML~~ HTML5, ~~CSS~~ CSS3, Less/Sass, Javascript, ~~script.aculo.us~~ jQuery, Bootstrap/Foundation, AngularJS, AJAX, ~~VIM BBedit~~ Sublime, ~~Mosaic Netscape Navigator~~/Chrome/Internet Explorer/Safari/Firefox, iPhone/Android/iPad, Webserver(Produktiv), Webserver(Staging), Webserver(Dev), SFTP, SSH, PHP, ~~Code-Ignitor~~ Laravel, Flatfile-CMS(Produktiv), Flatfile-CMS(Dev), (My)SQL-DB(Produktiv), (My)SQL-DB(Dev), Git, Grunt > __Seite funktioniert, sieht auf verschiedenen Browsern korrekt aus, Kunde versteht das CMS, Skripte laufen, Seite ist ~~barrierefrei~~ performant, Code ist ~~valide~~ komprimiert ~~und wohlgeformt~~, Build Chain funktioniert, Deployment Pipeline funktioniert, Site wird von Google indiziert, WebMetrics laufen, Seite funktioniert gut auf allen Desktops, Smartphones und Tablets, wahrgenommene Performance ist gut: puh!__

> Kernfragen: Funktionieren die Build Chain und Deployment Pipeline?

---

slide-is:simple
## 2018

~~HTML XHTML~~ HTML5, ~~CSS~~ CSS3, ~~Less~~ Sass, ~~Javascript~~ ECMAScript 2017, Babel, ~~script.aculo.us~~ ~~jQuery~~, Bootstrap/Foundation/SemnaticUI/Bulma/UIKit/, Angular/React/Vue, ~~AJAX~8, ~~VIM BBedit~~ Sublime, ~~Mosaic Netscape Navigator~~/Chrome/Internet Explorer/Safari/Firefox, iPhone/Android/iPad, Webserver(Produktiv), Webserver(Staging), Webserver(Dev), SFTP, SSH, PHP, ~~Code-Ignitor Laravel, Flatfile-CMS(Produktiv), Flatfile-CMS(Dev), (My)SQL-DB(Produktiv), (My)SQL-DB(Dev)~~, HeadlessCMS, JAMStack, Git, ~~Grunt~~ WebPack, NPM > __Seite funktioniert, sieht auf verschiedenen Browsern korrekt aus, Kunde versteht das CMS, Skripte laufen, Seite ist ~~barrierefrei~~ performant, Code ist ~~valide~~ komprimiert ~~und wohlgeformt~~, Build Chain funktioniert, Deployment Pipeline funktioniert, Site wird von Google indiziert, WebMetrics laufen, Seite funktioniert gut auf allen Desktops, Smartphones und Tablets, wahrgenommene Performance ist gut: puh!__

> Kernfrage: Ist mein Stack noch zeitgemäß?

---

slide-is: conclusion
## Die Ziele haben sich kaum verändert, der Weg zum Ziel enorm!

___

slide-is:welcome
# Developing a **Community** Website on JAMstack with GIT Managed Content and a Isomorphic Rendering Approach

---

slide-is: interlude
## A feeling of fellowship with others, as a result of sharing common attitudes, interests and goals.
Fabian Pfortmüller

---

slide-is:image-fullscreen images/community.svg


___
<!-- Content
	-------------------------------------------------------------------------->
slide-is:welcome
# Case Study: Developing a Community Website on JAMstack with GIT Managed **Content** and a Isomorphic Rendering Approach

---

slide-is: interlude
# Content is king.
Bill Gates

---

slide-is:image-fullscreen images/google-1999.png

---

slide-is:image-fullscreen images/content-creation.png


---

slide-is:conclusion 
## icon:book Content Entwicklung ist jede Menge Arbeit.

___
<!-- Content Management
	-------------------------------------------------------------------------->
slide-is:welcome
# Case Study: Developing a Community Website on JAMstack with GIT **Managed Content** and a Isomorphic Rendering Approach
Oder passender: Content Management

---

slide-is:image images/content-structure.png

---

slide-is:interlude
## Aufgaben eines Content Management Systems

---

slide-is:image images/CMS-Tasks.png

---

slide-is:interlude
## Structured Content vs. „Layouted“ Content
Mental Model of Content

---

slide-is:image images/content-structured.png

---

slide-is:image images/layout-simple.png

---

slide-is:interlude
### „Layouted“ Content

--- 

slide-is:image images/content-layouted-fvf.png

---


slide-is:image images/content-layouted.png 

---

slide-is:interlude
### Content Storage

--- 

slide-is:image images/content-storage.png

--- 

slide-is:image images/cms-nutzung.png zoom

---


slide-is: simple
## Ergebnis

- Content ist da und kann publiziert werden
- Content liegt in den Strukturen des CMS
- Content kann schlecht weiter verarbeitet werden
- Content ist segmentiert
- Semantik geht verloren
- Merging von Content bei vielen parallelen Pflegeprozessen ist schwer

---

slide-is:image images/CMS-Tasks.png

---

slide-is: interlude
# Organizing
Wie wird strukturiert?

---

slide-is: simple
## Wie wird strukturiert?
- im CMS Backend
- mit Kategorien
- mit weiteren Taxonomien, z.B. Tags

---

slide-is: interlude
# Publishing
Wie wird ausgeliefert?

---

slide-is:image images/cms-components.png

---

slide-is:image images/cms-stack.png

---

slide-is:image images/trad-stack.png

---

slide-is:image images/trad-stack-2.png

---

slide-is:image images/trad-stack-3.png
 
---

slide-is:image images/trad-stack-4.png

---

slide-is:image images/trad-stack-5.png

---

slide-is:image images/trad-stack-simple.png

---

slide-is:image images/trad-stack-in-real.png

---

slide-is:image images/trad-stack-content.png

---

slide-is:image images/trad-stack-content-2.png

---

slide-is: conclusion
## icon:ban Wenn wir den Zustand schlecht reden wollten:
- Content Pflege ist mühsam
- Content zerfällt/ wird segmentiert
- Organisation ist umständlich
- Merge von Datenständen ist sau kompliziert
- Content lässt sich schlecht weiter verarbeiten
- Content ist in den Strukturen des Systems „gefangen“
- Content Migration in ein anderen System ist sehr komplex
- Publishing ist langsam
- Bedienung von verschiedenen Ausgabekanälen ist mühsam
- Publishing skaliert schlecht
- System bietet viele Angriffsvektoren
- monolithisches System

---

slide-is: interlude
## Static is the new dynamic!
Why not?

___
<!-- JAM Stack
	-------------------------------------------------------------------------->
slide-is:welcome
# Case Study: Developing a Community Website on **JAMstack** with GIT Managed Content and a Isomorphic Rendering Approach
Coined by Mathias Biilmann, Netlify 

---

slide-is: simple
## Stacks
* **WISA stack:** Windows, IIS, SQL Server, ASP.NET 
* **LAMP:** Linux, Apache, MySQL, Python || Perl || PHP
* **MEAN:** MongoDB, express.js, angular.js, node.js 
* **MERN:** MongoDB, Express.js, React.js, Node.js

---

slide-is: interlude
# JAM

Javascript, APIs and Markup

---

slide-is: assignment
## Javascript
Any dynamic programming during the request/response cycle is handled by JavaScript, running entirely on the client. This could be any frontend framework, library, or even vanilla JavaScript.

---

slide-is: assignment
## APIs
All server-side processes or database actions are abstracted into reusable APIs, accessed over HTTP with JavaScript. These can be custom-built or leverage third-party services.

---

slide-is: assignment
## Markup
Templated markup should be prebuilt at deploy time, usually using a site generator for content sites, or a build tool for web apps.

---

slide-is: interlude
## Aufgaben werden entkoppelt
\#microservices \#decoupling \#antimonolithic

---

slide-is:image images/CMS-Tasks.png

---

slide-is:image images/CMS-Tasks-jamstack.png

---

slide-is: interlude
# Bausteine des Stacks

---

slide-is:image images/jamstack-blocks.png slide

---

slide-is: interlude
# \#1 Creating Content

---

slide-is: simple
## Content in Markdown
- übersichtlich
- in sich geschlossen
- flat
- leicht zu editieren
- leicht weiter zu verarbeiten

---

slide-is:image images/markdown.png

---

slide-is: interlude
# \#2 Organizing Content

---

slide-is: simple
## Organisation im Filesystem … 
- bekanntes mentales Modell
- übersichtlich
- leicht und schnell zu editieren

---

slide-is: simple
## … und via GIT/GITHUB
- Versionierung
- Merging
- Branching
- zusätzliche Tools, z.B. Issues

---

slide-is:image images/filesystem.png slide

---

slide-is:image images/git.png 

---

slide-is:image images/git-2.png 

---

slide-is: interlude
# \#3 Publishing Content

---

slide-is: simple
## Prerendered, static Data
- rendered at buildtime via static site generator
- deployed to simple webserver or cdn
- additional data via javascript and APIs

---

slide-is: simple
## Vorteile
- superschnell und skalierbar
- sehr sicher
- minimale Anforderungen an den Server

---

slide-is:image images/jamstack-example.png

---

slide-is: simple
## Realworld Examples
* [Smashing Magazine](https://www.smashingmagazine.com/)
* Reakkreditierung der Medieninformatik [Repo](https://github.com/th-koeln/mi-2017) // [Web](https://th-koeln.github.io/mi-2017/) // [PDF](http://www.medieninformatik.th-koeln.de/download/modulbeschreibungen-bachelor-bpo4.pdf)

---

slide-is: conclusion
## icon:gratipay Wenn wir den JAMstack schönreden wollten:
- Pflege der Inhalte ist leicht 
- Inhalte bleiben in sich geschlossen
- Inhalte sind portierbar
- Inhalte können versioniert werden
- verschiedene Stände können gemerged werden
- verschiedene Kanäle können recht gut bedient werden
- Trennung von Content und Layout ist gut möglich
- Organisation von Inhalten ist sehr einfach
- Publishing ist schnell
- Publishing ist sicher
- Publishing skaliert gut
- Best-of-Breed Ansatz mit lose gekoppelten Systemen
- unterstützt paralleles Entwickeln von Code und Content

___
<!-- Case Study
	-------------------------------------------------------------------------->
slide-is:welcome
# **Case Study**: Developing a Community Website on JAMstack with GIT Managed Content and a Isomorphic Rendering Approach

---

slide-is:image-fullscreen images/community.svg slide

---

slide-is: simple
## MI Website

Die Medieninformatik Website ist der Schweizer Taschenmesser für die Kommunikation nach außen und innen. Sie richtet sich an alle Zielgruppen und stellt Informationen und Einblicke in das Forschungs- und Lehrgebiet Medieninformatik für die verschiedenen Zielgruppen bereit. Hier landet im Grunde alles, was in den anderen Kanälen nicht passt, oder was für längere Zeit vorgehalten werden soll. Schwerpunkt des Inhalts sind Artefakte, die im Rahmen von Projekten oder Abschlussarbeiten entstanden sind. Inhalte werden folgenden Hauptrubriken zugeordnet:

* **mission:** alles rund im die Mission des Fachgebiets
* **people:** alles rund im die Leute in der MI
* **projects:** Berichte und Ergebnisse aus Projekten
* **pulse:** alles, was gerade so passiert
* **research:** Berichte und Ergebnisse aus Forschungsvorhaben und Kooperationen
* **study:** alles rund ums Studium
* **toolbox:** Helferlein für den Alltag von Medieninformatikern  

---

slide-is: simple
## Was soll die Seite können?
Thanks to [Phil Hawksworth](https://www.hawksworx.com/)

- meaningful URL for every Page (or Piece) of Content
- alle URLs sind Crawable, Curlaable und indizierbar
- jede URL liefert wirklichen Content
- URLs sind möglichst stabil
- schnelles Rendering und gute, wahrgenommene Performance
- hohe Ausfallsicherheit
- geringen Payload
- Möglichkeit für Übergänge and visuelle Effekte
- minimale Hosting Komplexität

---

slide-is: simple
## Warum JAMstack?

- Fokus auf Content/ Dokumente
- Offenheit des Systems
- in sich geschlossene Dokumente
- Zweitverwertung von Dokumenten ist leicht möglich
- unterschiedliche Autoren
- einfache Struktur
- Layout und Content entkoppelt
- …

---

slide-is:interlude
# Building Blocks
Markdown, GitHub, Hugo, Travis.CI, Github.io

---

slide-is: interlude
# Hugo

Ein sehr flexiber und schneller Static Site Generator.

---

slide-is: interlude
## Seiten & Listen
Hugos inhaltliches Basiskonzept

---

slide-is:image-fullscreen images/hugo-list-example.png slide

---

slide-is:image-fullscreen images/hugo-list-example-2.png

---

slide-is:image-fullscreen images/hugo-list-example-3.png

---

slide-is: interlude
## mal kurz rein gucken?

---

slide-is: conclusion
## icon:heartbeat Derzeitige Beurteilung
- Markdown ist wirklich hübsch
- die Kombination aus Markdown und Git ist topp!
- Entwurf eines Systems um den Content herum ist interessant aber gar nicht so leicht
- konsequente Trennung von Content und Layout ist gar nicht so leicht
- Hugo's Lookup Order ist recht komplex
- Hugo's Lists & Pages Konzept ist cool, aber herausforderend

---

slide-is: interlude
## Hugo: multiple Repräsentationen des Contents
HTML, AMP, JSON, XML

___
<!-- Isomorphic Rendering
	-------------------------------------------------------------------------->
slide-is:welcome
# Case Study: Developing a Community Website on JAMstack with GIT Managed Content and a **Isomorphic Rendering** Approach
Javascript Page Rendering 

---

slide-is:image images/isomorphic.png

---

slide-is:image images/isomorphi-2.png

--- 

slide-is: conclusion
## icon:tachometer Speed up your page!
* Bessere wahrgenommene Performance
* Visuelle Effekte
* Suchfunktionen
* maschinenlesbare Inhalte

___

slide-is: interlude
## Was kann JAMstack für uns tun?

--- 

slide-is: conclusion
## Geht es um Content?

--- 

slide-is: conclusion
## Gibt es viele Autoren?

--- 

slide-is: conclusion
## Soll Code und Content schnell parallel entwickelt werden?

--- 

slide-is: conclusion
## Sind die Inhalte überwiegend statisch?

---


slide-is: conclusion
## Hat das Team Dev-Skills und Spaß an einfachen als auch flexiblen Lösungen? 

---

slide-is: interlude
# JAMstack first?

___


slide-is: interlude
## auch interessant
\#Netlify \#Flatfile CMS \#Headless CMS 

___

slide-is:outro
## Danke für's Mitmachen
Slides unter **http://christian-noss.de/latest**

icon:twitter [twitter.com/cnoss](http://twitter.com/cnoss)  
icon:facebook [www.facebook.com/cnoss](https://www.facebook.com/cnoss)