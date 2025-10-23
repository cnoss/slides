---
title: Visual Thinking
separator: ___
verticalSeparator: ---
revealOptions:
  transition: 'slide'
  backgroundTransition: 'zoom'
  center: false
types: welcome, assignment
---

slide-is:welcome
# Visualisierung
Workshop im Rahmen des Moduls «Einführung in die Medieninformatik»

___

slide-is:assignment
## icon:pencil-alt Fingerübung

Nehmen Sie ein weißes DIN A4 Blatt und falten Sie es mittig über die lange Seite. Zeichnen Sie dann im oberen Teil ein einfaches, aber möglichst charakteristisches Portrait von sich. Nutzen Sie bitte einen mitteldicken Faserstift.

Ergänzen Sie das Portrait um die folgenden Angaben:
* Ihren Vornamen
* zwei Ihrer guten Eigenschaften
* zwei Ihrer schlechten Eigenschaften
* einen Satz, warum Sie ein guter Medieninformatiker sind oder werden

Für die Aufgabe haben Sie ** 10 Minuten ** Zeit. 

___

slide-is: simple

## icon:volume-up Mission Statement // MI Bachelor

Absolventen der Medieninformatik **analysieren**, **realisieren**, **betreiben** und **evaluieren informationstechnische Prozesse** und **Systeme** zur Gestaltung, Produktion, Bearbeitung, Distribution und Nutzung **medienbasierter Informationen**.

Das Studium der Medieninformatik zielt somit im Kern auf die Vermittlung entsprechender Methoden, Techniken und Denkweisen der Informatik. **Absolvent\*innen** der Medieninformatik **arbeiten** dabei vorwiegend in **Teams** und müssen dort ihre erworbenen Kompetenzen einbringen können – hier ist **Interdisziplinarität** gefragt, erwünscht und gefordert. Auch darauf bereitet das Studium der Medieninformatik vor: es **vermittelt Sichtweisen** und Techniken aus verschiedenen Fachgebieten, von **Computergrafik** über **Mensch-Computer-Interaktion** bis **Videoproduktion**, von **Kommunikationsdesign** über **Programmentwicklung** bis **Marketing**.

___

slide-is: assignment
## icon:bullseye Ziel des Workshops …

… ist es, die Teilnehmer zu motivieren und ermächtigen **Stift und Papier** als hilfreiches, effizientes und sympathisches **Werkzeug im Entwurfsprozess** von Softwaresystemen zu nutzen.

___

slide-is: conclusion

## icon:eye Visual Thinking
## icon:map Domänen & Domänenmodelle
## icon:paint-brush Interface Sketching



___

slide-is:interlude
## icon:eye Visual Thinking
icon:link [Zunächst einige Grundgedanken](http://www.christiannoss.de/talks/2017-visual-thinking-emi/#/step-1)


---


slide-is:assignment
## icon:baseball-ball Aufgabe 1: Warm werden

Zeichnen Sie aus den Glyphen folgende Dinge, jeweils drei mal:

* Tasse
* Blumentopf mit Blume drin
* Glühbirne
* Auto
* Computer mit Maus
* Schere
* Smartphone
* Schreibtischleuchte
* fröhliches Gesicht
* Stadt
* Wolke
* einen Stapel Geld

Für diese Aufgabe haben Sie **15 Minuten** Zeit.

---


slide-is:assignment
## icon:search Aufgabe 2: Domäne analysieren

Lesen Sie den [Auszug aus der Prüfungsordnung](http://www.christiannoss.de/talks/2018-visualisierung-emi/material/auszug-po.pdf) und machen Sie in 2er Gruppen eine möglichst vollständige **Liste von Konzepten, Personen, Entitäten, Knoten und Gegenständen** die hier Rollen spielen (u.a. zu nennen: Modul, Prüfung, Prüfungsausschuss etc.).

Entwickeln Sie parallel zu den gefundenen **Begriffen** entsprechende **Visualisierungen**. Nutzen Sie pro Visualisierung ein DIN A6 Blatt Papier. Bedenken Sie dabei folgendes:

**Geschlossene Glyphen** werden für die Visualisierung von Dingen mit einer Identität verwendet, also Konzepten, Personen, Knoten oder Gegenständen.


Für die Aufgabe haben Sie **30 Minuten** Zeit. 

___


slide-is: interlude
## icon:map Domänen & Domänenmodelle

Worum geht es hier eigentlich?




---

slide-is: simple

## Worum geht es hier eigentlich?

Um ein Problem mit Hilfe von Software lösen zu können oder einen Prozess zu digitalisieren, muss man wissen, was das Softwaresystem leisten soll, sprich: die Anwendungsdomäne muss gut verstanden werden. Dieses Wissen haben meist nicht die Entwickler sondern die Domänenexperten, also Menschen, die in dieser Domäne agieren. Die zu entwickelnde Software sollte sich möglichst gut in die Domäne einfügen.

Konzepte und Elemente der Domäne sowie die Beziehungen dazwischen müssen erkannt und fixiert werden. Daraus entsteht das Domänenmodell.



---

slide-is:image images/d-versus-s.jpg


---

slide-is:image images/d-versus-s-blitz.jpg


---


slide-is: simple
## icon:map Domain Driven Design

- ein Konzept von Eric Evans
- Tackling Complexity in the Heart of Software, Evans2003
- Entwicklungsphilosophie für sprach- und domänenzentrierte Entwicklung von (Software-)Systemen
- ist nicht gebunden an einen bestimmten Entwicklungsprozess
- ist domänenorientiert, nicht an UI- oder Technik zentriert

---


slide-is:assignment

## icon:question Was ist eigentlich eine Domäne?

Allgemein betrachtet ist eine Domäne ein Fachgebiet, ein Wissens- oder Aktivitätsbereich, z.B. Orgelbau und -restauration oder Tennis oder eben Prüfungswesen in der Hochschule.

---

slide-is:simple
## Begriffe im DDD

** Domäne: ** eine Domäne ein Fachgebiet, ein Wissens- oder Aktivitätsbereich, z.B. Orgelbau und -restauration oder Tennis oder eben die Prüfungsordnung in der Hochschule.

** Problemraum: ** der Bereich, den es zu bearbeiten gilt.

** Lösungsraum: ** das, was nachher im System abgebildet wird. Der Lösungsraum sollte gut und klar abgrenzbar sein.

** Domain Model: ** ist eine Abstraktion der Wirklichkeit und das, was später Kern der Software ist. Es beschreibt nur die zur Lösung nötigen Teile. Es entsteht in der iterativen Zusammenarbeit zwischen Domänen- und Softwareexperten.

** Ubiquitous Language: ** ist die in der Domäne benutzten Sprache.

** Subdomänen: ** sind Teilgebiete der Domäne, z.b. die Prüfungswesen innerhalb der Prüfungsordnung.

** Bounded Contexts: ** sind Lösungsräume innerhalb einer Subdomäne, die in sich relativ geschlossen sind, z.b. die Abschlussarbeit beim Prüfungswesen.


---

slide-is:image images/ul.jpg

---

slide-is:simple
### Ubiquitous Language

- Kurs
- Modul
- Fach
- Lehrveranstaltung

---

slide-is: conclusion
## Domänenmodell

Ein Domänenmodell ist ein System von Abstraktionen, das ausgewählte Aspekte einer Domäne repräsentiert. Es ist eine destillierte Form von Wissen, Annahmen, Regeln und Selektionen bezogen auf die Domäne und kombiniert Daten und Abläufe. Es wird für einen Bereich (Bounded Context) und in einer allseits verständlichen Form erstellt (Ubiquitous Language, s. u.). Es enthält keinerlei (Umsetzungs-)Technik.

---

slide-is: assignment
## icon:map Konzeptuelles Domänenmodell

Sie haben nun eine recht vollständige Übersicht über die Abläufe und Abhängigkeiten beim Prüfungswesen, entsprechend der Prüfungsordnung. Jetzt entwickeln wir, unter Berücksichtigung der *Ubiquitous Language*, *Subdomänen* und *Bounded Contexts* daraus gemeinsam ein einfaches konzeptuelles Domänenmodell.



---

slide-is: assignment
## icon:pencil Aufgabe für Zuhause: Gesamtübersicht

Entwickeln Sie eine möglichst vollständige Übersicht über die Abläufe und Abhängigkeiten beim Prüfungswesen entsprechend der Prüfungsordnung. Nutzen Sie dabei die bereits erarbeitete Domänenmodel und die Visualisierungen der Konzepte, Personen, Entitäten, Knoten oder Gegenstände.

Fotografieren Sie Ihre Gesamtübersicht ab und laden Sie das Foto im Ilias unterhalb Ihrer Gruppe bei Übungen/Visualisierungsworkshop hoch.


___


slide-is:interlude

## icon:paint-brush Interface Sketching

Wie funktionieren Wireframes und wozu sind sie gut?


---



slide-is:image-text images/wireframes-01.jpg

## Was leisten Wireframes?
<hr>

Im Entwicklungsprozess helfen unterschiedliche Arten von Prototypen 

* ein gemeinsames Bild der Software zu schaffen
* die Software mit Stakeholdern zu testen
* Varianten zu entwickeln
* User Journeys durchzuspielen
* …


---


slide-is:image-text images/wireframes-02.jpg

### Content
<hr>
Was wird auf welchem Screen gezeigt?


---


slide-is:image-text images/wireframes-03.jpg

### Struktur & Layout
<hr>
Welche Elemente gibt es und wie sind sie angeordnet?


---


slide-is:image-text images/wireframes-04.jpg

### Informationsarchitektur
<hr>
Wie sind die Informationen angeordnet und wie bewege ich mich durch die Anwendung?


---


slide-is:image-text images/wireframes-05.jpg

### Funktion & Verhalten
<hr>
Wie arbeitet das Interface und interagiert der Nutzer und wie reagiert die Anwendung?


---

slide-is:video
## Scribbling Conventions

<iframe width="560" height="315" src="https://www.youtube.com/embed/MwidSAlbEB8" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

---


slide-is:simple

## icon:mobile-alt Exam Eddy …

… ist ein (fiktives) Smartphone Tool für Studierende an der TH Köln. Es unterstützt die Studierenden in Sachen Prüfungswesen während ihres Studiums. Es erleichert das An- und Abmelden von Prüfungen, gibt eine Übersicht über die anstehenden Prüfungen, zeigt die Prüfungsergebnisse und mögliche Optionen in Sachen Prüfungswiederholung und Notenverbesserung. 


---


slide-is:assignment
## icon:map Aufgabe 3: Exam Eddy

Entwickeln Sie auf Basis des konzeptuellen Domänenmodells 3 - 5 Wireframes für die Smartphone App rund um das Thema Prüfungen. Beachten Sie dabei den zeitlichen Ablauf:
1. Prüfung und Prüfungsdatum wird angekündigt
2. Anmeldezeitraum beginnt
3. Anmeldezeitraum endet
4. Abmeldezeitraum beginnt
5. Abmeldezeitraum endet
6. Prüfung findet statt
7. Prüfungsergebnis wird veröffentlicht
8. Feedback/ Klausureinsicht wird angekündigt
9. Möglichkeiten der Notenverbesserung und Prüfungswiederholung werden gegeben


Für die Aufgabe haben Sie **45 Minuten** Zeit. Fotografieren Sie Ihr Ergebnis und laden es im Ilias unterhalb Ihrer Gruppe bei Übungen/Visualisierungsworkshop hoch.

___

slide-is:assignment
## Wer mehr wissen will

** Bücher:**
* [Rohde, Mike: Das Sketchnote Handbuch. 1. Auflage. Frechen: mitp Business, 2014](http://www.digibib.net/permalink/832/FHBK-x/HBZ:HT018145300)
* [Greenberg, Saul, et al. Sketching User Experiences: The Workbook, Elsevier Science & Technology, 2011. ProQuest Ebook Central](https://ebookcentral.proquest.com/lib/koln/detail.action?docID=809159)
* [Evans, Eric: Domain-driven design: tackling complexity in the heart of software. Boston [u.a.]: Addison-Wesley, 2004](http://www.digibib.net/permalink/832/FHBK-x/HBZ:HT014003765)

** Videos:**
* [Wireframing for UX: What it is and how to get better at it](https://www.youtube.com/watch?v=8-vTd7GRk-w)
* [Bessere Microservices mit Domain Driven Design](https://www.youtube.com/watch?v=327XraQKsGI)
* [Sketching Techniques](https://www.youtube.com/watch?v=vN2MFF2YZjo)
* [UI Sketching Conventions](https://www.youtube.com/watch?v=MwidSAlbEB8)
* [UX Designer - drawing the problem](https://www.youtube.com/watch?v=LskLyDOSfAc)

** Web: **
* [Pens, Process, Product: sketching for UX](https://uxdesign.cc/pens-process-product-sketching-for-ux-1b4992c47565)
* [Interactive Sketching Notation](https://wireframes.linowski.ca/2009/10/interactive-sketching-notation-v0-1/)







___

slide-is:outro
## Danke für's Mitmachen

icon:twitter [twitter.com/cnoss](http://twitter.com/cnoss)  
icon:facebook [www.facebook.com/cnoss](https://www.facebook.com/cnoss)