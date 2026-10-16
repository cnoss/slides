---
title: Grundlagen
layout: presentation.11ty.js
slideClasses: images
transition: none
status: ok
speaker: |
  **Grundlagen (ca. 15 Minuten)**

  Farbe ist keine Eigenschaft der Dinge, sondern eine Empfindung. Sichtbares Licht ist ein schmaler Ausschnitt des elektromagnetischen Spektrums, etwa 380 bis 780 Nanometer, zwischen Ultraviolett und Infrarot. Die Netzhaut hat drei Zapfentypen für kurze, mittlere und lange Wellenlängen. Aus deren Verhältnis konstruiert das Gehirn die Farbe.

  **Additiv und subtraktiv:** Am Bildschirm mischen sich Lichtfarben (RGB): Rot, Grün und Blau zusammen ergeben Weiß. Im Druck filtern Pigmente Licht heraus (CMY, plus K für Schwarz): Alle zusammen ergeben fast Schwarz. Deshalb sehen Farben auf Papier und am Screen nie ganz gleich aus.

  **Farbkreis:** Aus den Grundfarben abgeleitet. Gegenüberliegende Farben sind Komplementärfarben. Es gibt verschiedene Farbkreise, z. B. den symmetrischen und den nach Harald Küppers.

  **HSB:** Für Gestaltende praktischer als RGB, weil es beschreibt, wie wir Farbe wahrnehmen: Farbton (Hue), Sättigung (Saturation), Helligkeit (Brightness). Das HSB- bzw. HSV-Modell hat Alvy Ray Smith 1978 beschrieben. In Figma und anderen Werkzeugen ist es der Standard-Farbwähler.

  Quellen: Itten, Kunst der Farbe (1961); Albers, Interaction of Color (1963); Groß u. a., Generative Gestaltung (2018).
---

{% interlude "Grundlagen", "Was ist Farbe überhaupt?" %}

{% screenshot "./images/farbspektrum-01.png", '{"transition":"fade", "classes":"screenshot no-shadow", "width":"auto", "bu":"Sichtbares Licht: ein schmaler Ausschnitt des elektromagnetischen Spektrums"}' %}

{% screenshot "./images/farbkreis-01.png", '{"transition":"fade", "classes":"screenshot no-shadow", "width":"auto", "bu":"Von Infrarot bis Ultraviolett: das Farbspektrum"}' %}

{% screenshot "./images/farbmodelle-01.png", '{"transition":"fade", "classes":"screenshot no-shadow", "width":"auto", "bu":"Farbspektrum"}' %}

{% screenshot "./images/farbmodelle-02.png", '{"transition":"none", "classes":"screenshot no-shadow", "width":"auto", "bu":"Grundfarben des Farbmodells RGB"}' %}

{% screenshot "./images/farbmodelle-03.png", '{"transition":"none", "classes":"screenshot no-shadow", "width":"auto", "bu":"Grundfarben des Farbmodells CMY"}' %}

{% screenshot "./images/farbmischung-01.png", '{"transition":"fade", "classes":"screenshot no-shadow", "width":"auto", "bu":"Additive Farbmischung: Bildschirm"}' %}

{% screenshot "./images/farbmischung-02.png", '{"transition":"fade", "classes":"screenshot no-shadow", "width":"auto", "bu":"Subtraktive Farbmischung: Druck"}' %}

{% screenshot "./images/farbkreise-01.png", '{"transition":"fade", "classes":"screenshot no-shadow", "width":"auto", "bu":"Der daraus abgeleitete Farbkreis"}' %}

{% screenshot "./images/saettigung-01.png", '{"transition":"fade", "classes":"screenshot no-shadow", "width":"auto", "bu":"Sättigung"}' %}

{% screenshot "./images/saettigung-02.png", '{"transition":"none", "classes":"screenshot no-shadow", "width":"auto", "bu":"Ohne Sättigung bleibt die Helligkeit"}' %}

{% screenshot "./images/saettigung-helligkeit-01.png", '{"transition":"fade", "classes":"screenshot no-shadow", "width":"auto", "bu":"Sättigung und Helligkeit"}' %}

{% screenshot "./images/hue-saturation-brightness-01.png", '{"transition":"fade", "classes":"screenshot no-shadow", "width":"auto", "bu":"Hue, Saturation, Brightness: das HSB-Farbmodell"}' %}
