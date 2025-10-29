---
title: Competencies
layout: presentation.11ty.js
slideClasses: images
status: ok

material: ./images/Imagenes-Blog-1500x1000_0002_Curvas-1.jpg
materials: ./images/materials.jpg
nextGenM: ./images/next-gen-materials-data-report-material-innovation-initiative-investment-growth-industry-plant-bio-based-2022-0.jpg

webApis: ./images/web-apis.jpg
containerQueries: ./images/container-queries-vs-media-queries.png
ercoDataMock: ./images/erco-lsp-data-mockup.png
ercoDataMockShot: ./images/erco-data-shot.jpg
dbVariants: ./images/db-mob-trans.png
dbVariantsB: ./images/db-mob-b.jpg
aurora: ./images/datenquellen-pruefen.jpg
cranach: ./images/datenkonsitenz-pruefen.jpg
data: ./images/data.png

materialeigenschaften: |
  <p><strong>Strukturelle Eigenschaften:</strong> Modularität, Logik & Regelhaftigkeit, Abhängigkeit & Verkettung, Schichtung / Abstraktionsebenen </p>
  <p><strong>Dynamische Eigenschaften:</strong> Prozessualität, Emergenz, Iterativität, Reaktivität, Temporalität</p>
  <p><strong>Physikalische & technische Eigenschaften:</strong> Performanz, Präzision, Fehleranfälligkeit, Kompatibilität, Transparenz</p>
  <p><strong>Semantische & kulturelle Eigenschaften:</strong> Kollaboration, Automatisierung, Übersetzbarkeit, Lesbarkeit, Kommunikativität, Konventionalität, Pflege & Nachvollziehbarkeit</p>
  <p><strong>Gestalterische Metaeigenschaften:</strong> Experimentierbarkeit, Reproduzierbarkeit, Parametrik & Variabilität, Offenheit & Erweiterbarkeit, Ephemerität</p>

speaker: |
  Strukturelle Eigenschaften
  - Modularität – Code besteht aus Einheiten (Funktionen, Klassen, Komponenten), die sich kombinieren und wiederverwenden lassen.
  - Logik & Regelhaftigkeit – Verhalten entsteht durch Regeln, Bedingungen, Schleifen
  - Abhängigkeit & Verkettung – Ein Teil wirkt auf andere zurück; kleine Änderungen können große Folgen haben (Systemisches Verhalten)
  - Schichtung / Abstraktionsebenen – vom Binärcode bis zum Interface; Gestalt entsteht durch Ebenen, nicht durch Oberflächen.

  Dynamische Eigenschaften
  - Prozessualität – Code ist kein Zustand, sondern ein Ablauf; Gestaltung geschieht über Zeit.
  - Emergenz – Verhalten kann entstehen, das nicht vollständig vorhersehbar ist (z. B. bei generativen Systemen).
  - Iterativität – Entwicklung und Ausführung wiederholen sich ständig (Loops, Feedback).
  - Reaktivität – Systeme antworten auf Input; Interaktion ist Materialeigenschaft
  - Temporalität – Zeit ist eine formbildende Dimension (Animation, Latenz, Verzögerung).

  Physikalische / technische Eigenschaften
  - Performanz – Effizienz und Geschwindigkeit beeinflussen Gestaltung; „leichtfüßiger“ oder „träge“ Code verändert die Wahrnehmung.
  - Präzision – Code erfordert exakte Anweisungen – jedes Verhalten ist determiniert, aber im Zusammenspiel komplex.
  - Fehleranfälligkeit – Bugs sind keine Störung, sondern Ausdruck der Materialität
  - Kompatibilität – Schnittstellen definieren, wie Teile zusammenpassen – eine Frage von Maß, Passung und Toleranz.
  - Transparenz / Opazität – je nach Technologie ist Verhalten nachvollziehbar oder undurchsichtig (Black Box).

  Semantische & kulturelle Eigenschaften
  - Kollaboration – Code ist selten individuell; er entsteht in Ökosystemen, Repositories, Versionierungen.
  - Automatisierung – Code delegiert Handlung – er schreibt Verhalten fort
  - Übersetzbarkeit – Code vermittelt zwischen Mensch und Maschine – eine Sprache mit Syntax, Semantik und Pragmatik.
  - Lesbarkeit – Code ist nicht nur für Maschinen bestimmt, sondern auch für Menschen. Gute Lesbarkeit ist eine Form der Gestaltung von Bedeutung: Struktur, Klarheit, Rhythmus und Benennung sind gestalterische Entscheidungen. 
  - Kommunikativität – Code ist eine Sprache des Zusammenarbeitens. Er dokumentiert Denkmuster, Entscheidungen und Haltung.
  - Konventionalität – Jedes Projekt lebt von  Übereinkünften: Konventionen, Stilregeln, Naming-Patterns. Sie sind kulturelle Codes, die Verständigung ermöglichen.
  - Pflege & Nachvollziehbarkeit – Wie bei langlebigen Produkten zählt nicht nur das Machen, sondern das Erhaltbare: Wartbarkeit, Erweiterbarkeit, Wiederverwendbarkeit.

  Gestalterische Metaeigenschaften
  - Experimentierbarkeit – schnell testbar, reversibel, iterativ
  - Reproduzierbarkeit – identische Ergebnisse sind möglich; Variation entsteht durch Parameter.
  - Parametrik / Variabilität – Form ist nicht fix, sondern durch Werte definiert.
  - Offenheit / Erweiterbarkeit – Systeme können wachsen, verzweigen, forken.
  - Ephemerität – Digitales ist flüchtig, Versionen veralten; Haltbarkeit ist gestaltbare Qualität.
  
---

{% screenshotFs material, '{"transition":"fade", "classes":"no-shadow large-text", "bu":"Verständnis von Material und Produktion"}' %}

{% simpleText "Materialverständnis", materialeigenschaften, false, '{"badge": "must have"}'  %}

{% screenshotFs webApis, '{"transition":"fade", "classes":"no-shadow large-text invert full-height frameless", "bu":"<strong>Gestaltungsräume</strong> kennen und <strong>Komplexität</strong> abschätzen können", "badge": "must have"}' %}

{% screenshotFs containerQueries, '{"transition":"fade", "classes":"no-shadow large-text invert full-height frameless", "bu":"<strong>Implementierungsmöglich-<br>keiten</strong> und <strong>-strategien</strong> kennen (und entwickeln?)", "badge": "should have"}' %}

{% screenshotFs ercoDataMock, '{"transition":"fade", "classes":"no-shadow large-text invert full-height frameless", "bu":"Funktionale <strong>Prototypen</strong> und <strong>Proof-of-concepts</strong> aufbauen<br>(und verproben)", "badge": "could have"}' %}

{% screenshotFs aurora, '{"transition":"fade", "classes":"no-shadow large-text full-height frameless", "bu":"<strong>Datenquellen</strong> und <strong>Datenqualität</strong> prüfen", "badge": "could have"}' %}

{% screenshotFs cranach, '{"transition":"fade", "classes":"no-shadow large-text  full-height frameless", "bu":"<strong>Datenkonsistenz</strong> und <strong>Datenstrukturen</strong> erkunden und prüfen", "badge": "could have"}' %}

{% screenshotFs dbVariantsB, '{"transition":"fade", "classes":"no-shadow large-text invert  full-height frameless", "bu":"<strong>Varianten</strong> erzeugen, mit <strong>echten Daten</strong> auf <strong>echten Geräten</strong> testen", "badge": "could have"}' %}

{% screenshotFs data, '{"transition":"fade", "classes":"no-shadow large-text invert  full-height frameless", "bu":"Sehr gutes <strong>Verständnis von Daten</strong>", "badge": "must have"}' %}