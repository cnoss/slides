---
title: "Mini-Übung"
layout: presentation.11ty.js
slideClasses: wrap
status: ok
speaker: |
  **Mini-Übung (ca. 10 Minuten)**

  Drei Screens, erst unscharf und grau. Zu zweit für jeden Screen die Rangfolge 1, 2, 3 notieren, je etwa eine Minute. Danach die Auflösung scharf und in Farbe. Diskussion: Was ist das Ziel der Seite? Passt die Rangfolge dazu?

  Erwartbar (aus dem eigenen Test, bitte live gegenprüfen):

  - **A, Netflix:** 1. Headline, 2. Eingabe und Button, 3. Login oben rechts. Das dunkle Plakatraster tritt zurück. Ziel ist die Anmeldung, das passt. Der rote Button verliert in Grau deutlich, hier trägt die Headline.
  - **B, IKEA:** 1. das große Foto links, 2. die dunklen Teaser rechts, 3. die Headline »Willkommen«. Die Fotos dominieren. Gewollt? Für einen Shop, der inspirieren will, vielleicht ja.
  - **C, TH Köln:** 1. das dunkle Foto im Slider, 2. die Kästen darunter, 3. Logo und Navigation. Die farbigen Kästen (Rot, Pink) verlieren in Grau ihre Kraft und konkurrieren miteinander. Gute Diskussion: Was soll man auf der Hochschulseite zuerst sehen?

  **Alternative:** Statt der drei Screens das eigene Ergebnis aus dem letzten Workshop testen und mit der Nachbarin oder dem Nachbarn tauschen.
---

{% interlude "Und jetzt Sie.", "Drei Screens, zu zweit, zehn Minuten" %}

<section class="image screenshot shadow" data-transition="fade" data-background-transition="fade"><figure><img src="./images/uebung-netflix.jpg" alt="Screenshot, unscharf und in Graustufen" style="filter:blur(0.7vw) grayscale(1);"><figcaption class="bu"><p>Screen A: Was sehen Sie zuerst, als Zweites, als Drittes?</p></figcaption></figure></section>

<section class="image screenshot shadow" data-transition="fade" data-background-transition="fade"><figure><img src="./images/uebung-ikea.jpg" alt="Screenshot, unscharf und in Graustufen" style="filter:blur(0.7vw) grayscale(1);"><figcaption class="bu"><p>Screen B: Was sehen Sie zuerst, als Zweites, als Drittes?</p></figcaption></figure></section>

<section class="image screenshot shadow" data-transition="fade" data-background-transition="fade"><figure><img src="./images/uebung-thkoeln.jpg" alt="Screenshot, unscharf und in Graustufen" style="filter:blur(0.7vw) grayscale(1);"><figcaption class="bu"><p>Screen C: Was sehen Sie zuerst, als Zweites, als Drittes?</p></figcaption></figure></section>

{% statement "Auflösung", "Jetzt scharf und in Farbe. Stimmt Ihre Reihenfolge? Was will die Seite, und kommt das an?" %}

{% screenshot "./images/uebung-netflix.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Screen A: Stimmt Ihre Reihenfolge? Und passt sie zum Ziel der Seite?<br><small>netflix.com/de, Screenshot 2026</small>"}' %}

{% screenshot "./images/uebung-ikea.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Screen B: Stimmt Ihre Reihenfolge? Und passt sie zum Ziel der Seite?<br><small>ikea.com/de, Screenshot 2026</small>"}' %}

{% screenshot "./images/uebung-thkoeln.jpg", '{"transition":"fade", "classes":"shadow", "width":"auto", "bu":"Screen C: Stimmt Ihre Reihenfolge? Und passt sie zum Ziel der Seite?<br><small>th-koeln.de, Screenshot 2026</small>"}' %}

{% question "Und Ihr eigener Entwurf?", "Testen Sie Ihr Ergebnis aus dem Workshop. Am besten mit jemandem, der es noch nicht kennt." %}
