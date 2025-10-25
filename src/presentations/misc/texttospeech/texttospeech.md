---
title: Sprache im Web
revealOptions:
  controlsTutorial: false
  transition: 'slide'
  backgroundTransition: 'concave'
types: welcome, assignment, simple
---

slide-is:welcome
# Sprache im Web
Technologien und Konzepte zur Sprachsynthese im Online-Kontext

___
slide-is:simple
## Über den Workshop
* **Anmerkungen/Fragen** bitte direkt stellen und einbringen!  
* **Zeitrahmen** - 3x 50 Minuten mit je 10 Minuten Pause
* **Formate** - Input, Diskussion, Coding
* **Motivation** - Nutzung der eigenen Website im Home Assistant
* **Erwartungen** - Beteiligung in Diskussionen, Interesse an Javascript-Coding
* **Ziele** - Überblick gewinnen, Web Speech nutzen, Verständnis und Bewertungskompetenz für TTS-Technologien

___
slide-is:simple
## Inhalt

* Einleitung
* Sprachen und Technologien
* Hands on
* Technologiebewertung
* Neuer Standard: Pronunciation
* Zusammenfassung

___
slide-is:simple
## Einleitung
* Wozu Text to Speech?
* Geschichte
* Potenzial

___
slide-is:interlude
### Wozu Text to Speech?
Welche Anwendungsfälle gibt es?  
Welche Technologien kann es ersetzen?  

https://pingo.coactum.de/752008

___
slide-is:simple
### Wozu Text to Speech?

* Sprachcomputer
* Screenreader (Sehbehinderungen/Dyslexie)
* Home Assistants
* Klassische Bandansagen ersetzen

___
slide-is:simple
### Geschichte

* Ausgabe von Sprache seit dem 18. Jahrhundert ein Thema
* "Vokalmaschinen" und "Sprachorgeln" konnten Worte ausgeben
* 1961: Präsentation von IBM 704
* In den letzten zehn Jahren
  * Deutliche Qualitätssteigerung von TTS
  * Fokus auf die Verkettung von Begriffen

___
slide-is:simple
### Potenzial

* Hotlines
* Lautsprecherdurchsagen
* Sprache von künstlicher Intelligenz
* KI-gesteuerte Medien (Radio, TV, Webstreams)

___
slide-is:simple
## Sprachen und Technologien
* SSML
* CSS Speech
* Web Speech API
* Bestandteile der Web Speech API

___
slide-is:simple
### SSML

* Speech Synthesis Markup Language
* Basiert auf XML
* Kann in Alexa Skills verwendet werden
* Unterstützt Text-to-Speech-API von Google
* Nur von Microsoft Edge teilweise unterstützt
* (Noch) **kein** Teil des HTML-Standards

___
slide-is:simple
### icon:code SSML
```xml
<speak>
  Das ist ein Testtext in <say-as interpret-as="characters">SSML</say-as>. Ich kann Zahlen verschieden aussprechen.
  <break time="2000ms">
  <say-as interpret-as="cardinal">10</say-as>
  <say-as interpret-as="ordinal">10</say-as>
  Auch ein Datum, Abkürzungen oder Zensur machen mir keine Probleme.
  <say-as interpret-as="date" format="yyyymmdd" detail="1">
    2019-04-25
  </say-as>
  <sub alias="Technische Hochschule">TH</sub>Köln.
  <say-as interpret-as="bleep">Zensiert</say-as>
  <emphasis level="moderate">Das ist eine wichtige Aussage.</emphasis>
</speak>
```

___
slide-is:simple
### CSS Speech
* Behandlung von Sprache als Mediatype in CSS
* Auditive Eigenschaften für einzelne Selektoren
* Teilweise kompatibel mit SSML, kann SSML ergänzen
* (Noch) **kein** Teil des CSS-Standards
* Von keinem etablierten Browser (außer Opera) unterstützt

___
slide-is:simple
### icon:css3 CSS Speech
```css
h1 {
  voice-family: female;
  voice-balance: left;
  voice-pitch: high;
  voice-volume: -6dB;
}
p {
  voice-family: male;
  voice-volume: +6dB;
}
.number {
  speak-as: digit;
  pause-before: weak;
}
```

___
slide-is:simple
### Web Speech API
* Teil der JavaScript Web APIs
* Im Vanilla Javascript enthalten
* Von jedem etablierten Browser unterstützt (IE ausgenommen)
* Zwei Teile: SpeechRecognition und SpeechSynthesis
* Sprachausgabe durch Browser-Sprachausgabe
* Manuelles Ansteuern

___
slide-is:simple
### Bestandteile der Web Speech API
* Drei miteinander agierende Objekte:

**SpeechSynthesis**
* Startet, pausiert und stoppt die Wiedergabe
* Abfragen der verfügbaren Stimmen je Gerät
  
**SpeechSynthesisVoice**
* Definiert eine Stimme (inkl. Sprache)
* Jedes Gerät hat eine Default-Stimme
  
**SpeechSynthesisUtterance**
* Definiert eine Äußerung und alle dafür relevanten Parameter
* z.B. Text, Lautstärke, Pitch, Geschwindigkeit etc.

___
slide-is:simple
### icon:file-code Web Speech
```javascript
let synth = window.speechSynthesis;
let utterThis = new SpeechSynthesisUtterance("Das ist ein Testtext.");
utterThis.voice = synth.getVoices()[0];
utterThis.lang = 'de-DE';
utterThis.volume = 0.7;
synth.speak(utterThis);
synth.pause();
setTimeout(function(){
    synth.resume();
}, 3000);
```

___
slide-is:interlude
## Hands on!
Aufgaben: https://github.com/astrutz/texttospeech  
**Bitte Firefox nutzen!**

___
slide-is:simple 
### icon:low-vision Szenario

Die Website der Medieninformatik wird relauncht. Neben Designänderungen soll die Seite auch barrierefrei(er) werden, um das Studium auch für körperlich beeinträchtigte Studienanfänger interessanter zu machen. Ihr werdet von Prof. Noss beauftragt die relevantesten Inhalte für Menschen mit Sehbeeinträchtigung umzugestalten.

___
slide-is:assignment
### icon:tools Aufgabe 1: User-Interface zur Steuerung

Erstellt eine **GUI**, die es dem Nutzer ermöglicht sich den Willkommenstext vorlesen zu lassen. Dazu soll der Nutzer die Wiedergabe starten, pausieren, fortsetzen und stoppen können. Darüber hinaus sollen Geschwindigkeit, Stimme (abhängig vom Gerät), Lautstärke definierbar sein.

Für die Aufgabe habt Ihr **25 Minuten** Zeit. Beschränkt euch auf ein **einfaches Frontend**.

**Hilfsmittel**: jQuery, Design-Frameworks (Bootstrap, Material o.ä.), MDN web docs.

**Material**: aufgabe_1.html, style.css, script.js

---
slide-is:assignment
### icon:lightbulb Bonusaufgabe 1
Prüfe, ob dein Code auch in anderen gängigen Browsern läuft. Wie unterscheiden sich die Stimmen von Browser zu Browser und was bedeutet das für die Entwicklung?  
  
.
![Browser][web-speech]

[web-speech]: /img/web-speech-compatibility.JPG "Web Speech Browser"

___
slide-is:assignment
### icon:table Aufgabe 2: Semantische Anreicherung
Überführt Euer Interface in die Klasse "tts-controls" oder überführt die Beispiellösung, Passwort *sol1*. Passt Eure TTS-Logik so an, dass sie den Inhalt semantisch vorliest. Dazu sollen die Tabelleninhalte logisch verbunden werden. Ziel ist es die Tabelle nur durch das Vorlesen verstehen zu können. 

Für die Aufgabe habt Ihr **20 Minuten** Zeit. 

**Hinweis**: Nutzt die gesetzten Klassen "semester-number" und "credit-points".

**Material**: aufgabe_2.html, style.css, script.js

---
slide-is:assignment
### icon:lightbulb Bonusaufgabe 2
Welche HTML-Elemente und Frontendkonzepte benötigen eine semantische Anreicherung? Wie könnte man eine solche Anreicherung automatisieren oder im Markup bereits festlegen?

___
slide-is:assignment
### icon:magic Aufgabe 3: Simulation von SSML
Überführt Euer Interface in die Klasse "tts-controls" oder überführt die Beispiellösung, Passwort *sol1*. Um semantische Anreicherung dynamisch im Markup nutzen zu können soll grundlegendes SSML in p-Tags verfügbar sein. Dazu sollen über das Attribut "data-ssml" folgende Features umgesetzt werden:

* `<sub alias="text">`
* `<say-as interpret-as="characters">` (Für Strings und Zahlen)
* `<say-as interpret-as="unit">` (Für Streckeneinheiten)

Ziel ist es den mit SSML-Tags gefüllten Text semantisch korrekt wiederzugeben.

Für die Aufgabe habt Ihr **20 Minuten** Zeit. 

**Hinweis**: Den Link zur SSML-Doku findet Ihr in der README.md

**Material**: aufgabe_3.html, style.css, script.js

---
slide-is:assignment
### icon:lightbulb Bonusaufgabe 3
Prüfe inwieweit die folgenden Use Cases ohne SSML-Tags bereits richtig ausgegeben werden:

* Aufzählungen
* Sprechpausen
* Mathematische Brüche
* Datum und Uhrzeit
* Ausgabe von Sounds/Audiofiles

___
slide-is:simple
## Technologiebewertung
* SSML
* CSS Speech
* Web Speech
* Bewertungskriterien
* Bewertungsmatrix

___
slide-is:simple
### Kritikpunkte - SSML
* Definition von Betonungen ist einzigartig
* Spezialisiert auf TTS -> Keine Mischtechnologie
* Äquivalenz zu HTML
* Kein Support durch Web-Browser
* Propietärer Standard
* Keine Steuerung des Vorlesens

___
slide-is:simple
### Kritikpunkte - CSS Speech
* Kapselung von verschiedenen Inhaltstypen
* CSS-übliche Selektoren
* Trennung von Styling und Markup
* Kaum Browsersupport
* Keine Steuerung des Vorlesens

___
slide-is:interlude
### Kritikpunkte - Web Speech
Was fiel leicht?  
Wo gab es Schwierigkeiten?  
Was war nicht möglich?

___
slide-is:simple
### Kritikpunkte - Web Speech
* Kapselung von Code
* Steuerung durch den Nutzer möglich
* Wiedergabe von bestimmten Segmenten
* Anpassung der Reihenfolge
* GUI/Grundlage muss aufgesetzt werden

___
slide-is:interlude
### Bewertungskriterien
Welche Kriterien bestimmen die Qualität und Nutzbarkeit von TTS-Technologien?  
  
https://pingo.coactum.de/752008

___
slide-is:simple
### Bewertungskriterien
* Sprache
* Stimmfamilie/Geschlecht
* Phonetische Aussprache
* Ersetzung von Worten
* Geschwindigkeit/Pitch/Lautstärke
* Abspielen/Fortsetzen/Pausieren

___
slide-is:interlude
### Bewertungsmatrix
Gemeinsame Live-Bewertung

___
slide-is:simple
### Bewertungsmatrix 
Erlaubte Werte: **--**, **-**,  **O**,  **+**, **++** 
  
| Kriterium                        | SSML | CSS Speech | Web Speech API |
|----------------------------------|------|------------|----------------|
| Kompatibilität                   |   --  |    --     |         O       |
| Verlässlichkeit                  |  ++  |      O      |         O       |
| Genauigkeit                      |   ++ |      +      |        +        |
| Steuerbarkeit                    |   -- |      -      |        ++      |
| Implementierungsaufwand          |  O   |      O      |         +       |
| Zugänglichkeit                   |   +   |     O       |      +         |
| Komplexität                      |   O   |     +       |      -        |
| **Gesamt**                       | **1**    | **-1**    | **4**              |

___
slide-is:simple
## Neuer Standard: Pronunciation
* Pronunciation allgemein
* Ziele und Nicht-Ziele
* Technologische Ansätze
* Kritikpunkte
* Bewertungsmatrix
* Ausblick

___
slide-is:simple
### Pronunciation allgemein
* Verbesserung der TTS-Möglichkeiten
* Schaffung eines (!) Standards
* Bisherige Technologien nicht beschädigen

___
slide-is:simple
### Ziele und Nicht-Ziele
**Ziele**

* Standardmechanismus um HTML zu ergänzen
* SSML generalisieren und erweitern
* Assistive Technologien sollen Pronunciation nutzen können

**Nicht-Ziele**

* CSS-Speech wiederbeleben/erweitern
* Einen komplett neuen TTS-Standard konzeptionieren

___
slide-is:simple
### Technologische Ansätze
**In-line SSML**

* Direkt lesbar für Browser
* (Möglicherweise) für Home Assistants einfach lesbar
* (Möglicherweise) für Assistenzsysteme schwer lesbar
```xml
<span>Das ist der <speak-as interpret-as="ordinal">4.</speak-as> Beispieltext.</span>
```

**SSML mit Attributen**

* SSML als JSON in data-Attributen
* HTML-Semantik wird nicht gefährdet
* Erhöht die Komplexität des Markups
```xml
<span>Das ist der <span data-ssml='{"say-as" : {"interpret-as":"digits"}}'>4.</span> Beispieltext.</span>
```
___
slide-is:simple
### Kritikpunkte - Pronunciation
* Versucht bestehende Technologien zu einem Standard zu vereinen
* JSON-Struktur sorgt für Potenzial von TTS-REST-APIs
* Nicht nur Browser werden berücksichtigt (wie bei CSS Speech)


___
slide-is:simple
### Bewertungsmatrix
| Kriterium                        | SSML | CSS Speech | Web Speech API | Pronunciation
|----------------------------------|------|------------|----------------|----------------|
| Kompatibilität                   |   --  |    --     |         O       |      +     |
| Verlässlichkeit                  |  ++  |      O      |         O       |     ++      |
| Genauigkeit                      |   ++ |      +      |        +        |     ++      |
| Steuerbarkeit                    |   -- |      -      |        ++      |      ?     |
| Implementierungsaufwand          |  O   |      O      |         +       |     O      |
| Zugänglichkeit                   |   +   |     O       |      +         |     +      |
| Komplexität                      |   O   |     +       |      -        |      O    |
| **Gesamt**                       | **1**    | **-1**    | **4**       |       **6**    |

___
slide-is:simple
### Wie geht es weiter?
* Recommendation-Status für technische Ansätze wird erlangt
* Implementation von Pronunciation/Erweiterung SSML
* Abgabe an W3C Advisory Council zur Bestätigung
* Etablieren des neuen Standards bei Entwicklern, Browsern und in der Industrie

---
slide-is:image /img/timeline.png
W3C Draft Prozess - Technische Herangehensweise

---
slide-is:simple
### W3C Draft Prozess
#### First Working Draft (min. alle 3 Monate)
Erste Veröffentlichung zu einem Standard.
#### Last Call Working Draft (3 Wochen)
Letzte Chance für Feedback von anderen Arbeitsgruppen und der Community.
#### Candidate Recommendation (max. 1 Jahr)
Arbeitsgruppe ist der Meinung das Ziel erreicht zu haben, signifikante Features stehen.
#### Proposed Recommendation (min. 4 Wochen)
Input der Nutzer wurde berücksichtigt, Standard kann an das W3C Advisory Council abgegeben werden.
#### Recommendation (unbegrenzt)
Bereit zur Verteilung und Integration in Browser und betreffende Systeme.

___
slide-is:conclusion
## Zusammenfassung
* Text to Speech bietet in vielen Bereichen technologisches Potenzial
* Im Web gibt es noch **keinen eindeutigen Standard**
* Web Speech API deckt die meisten Anforderungen ab
* Pronunciation soll SSML öffentlich machen und HTML erweitern
* Überführung in Proposed Recommendation spätestens Juni 2021
* Standardisierung von Pronunciation vermutlich innerhalb der nächsten 2 Jahre

___
slide-is:outro
## Danke für's Mitmachen!

#### Gibt es Fragen, Anmerkungen, Feedback?

* icon:envelope [astrutz@th-koeln.de](mailto:astrutz@th-koeln.de)  
* icon:github [astrutz](https://www.github.com/astrutz)
* icon:xing [Alexander Strutz](https://www.xing.com/profile/Alexander_Strutz3/cv)